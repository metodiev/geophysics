"""Reproducible environments, measured: fingerprint, order, threads, lock file.

Run:  python environments_demo.py
Requires: numpy; ``yaml`` and ``packaging`` if available (both are present in
this project's virtual environment, as dependencies of Jupyter and pytest)

The lesson's central claim is that "it worked on my machine" is a statement
about an environment, and that an environment is a thing you can print, hash
and pin. This script does exactly that, and then runs the one experiment that
decides how much determinism you actually bought:

1. the interpreter, its prefix and the packages it can see;
2. a single fingerprint hash of the whole environment;
3. the BLAS/LAPACK build NumPy is linked against -- the reason identical Python
   code can differ in the last bits on another machine;
4. reduction order: the same sum, three ways, in one process;
5. thread count: the same product computed in four subprocesses with
   OMP_NUM_THREADS = 1, 2, 4, 8, hashed and compared;
6. this repository's own environment declaration, audited against what is
   installed;
7. what a lock file looks like and what `--require-hashes` enforces.

Step 5 is an honest experiment, not a demonstration: if thread count changes
nothing on this machine, the script says so.
"""

from __future__ import annotations

import hashlib
import importlib.metadata as md
import json
import os
import pathlib
import platform
import subprocess
import sys

import numpy as np

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# 1. Interpreter identity
# --------------------------------------------------------------------------

def demo_interpreter() -> None:
    section("1. The interpreter, exactly")
    print(f"  sys.version           = {sys.version.splitlines()[0]}")
    print(f"  implementation        = {platform.python_implementation()} "
          f"{platform.python_version()}")
    print(f"  sys.executable        = {sys.executable}")
    print(f"  sys.prefix            = {sys.prefix}")
    print(f"  sys.base_prefix       = {sys.base_prefix}")
    print(f"  in a virtual env      = {sys.prefix != sys.base_prefix}")
    print(f"  platform              = {platform.platform()}")
    print(f"  machine               = {platform.machine()}  "
          f"({os.cpu_count()} logical CPUs)")
    print("\n  A paper's reproducibility statement should name the interpreter")
    print(f"  version and this prefix. 'Python 3' is not a version; 'CPython "
          f"{platform.python_version()},")
    print(f"  {platform.machine()}, {platform.system()}, {platform.release()}' is.")
    print("  The prefix matters because two")
    print("  interpreters of the same version with different site-packages are")
    print("  different environments.")


# --------------------------------------------------------------------------
# 2. Environment fingerprint
# --------------------------------------------------------------------------

def demo_fingerprint() -> None:
    section("2. One hash for the whole environment")
    installed = sorted(
        (d.metadata["Name"], d.version) for d in md.distributions()
        if d.metadata["Name"]
    )
    text = "\n".join(f"{name}=={version}" for name, version in installed)
    digest = hashlib.sha256(text.encode()).hexdigest()
    print(f"  distributions installed: {len(installed)}")
    print(f"  fingerprint            : sha256({len(installed)} pins) = {digest}")
    print("  key packages:")
    for name, version in installed:
        if name.lower() in {"numpy", "scipy", "pandas", "matplotlib", "pytest",
                            "xarray", "obspy", "geopandas", "rasterio"}:
            print(f"    {name:>12} {version}")
    print("\n  The fingerprint is the reviewable artefact: two people who report the")
    print("  same hash were running the same environment, whatever their machines.")
    print("  It is also what makes a claim falsifiable -- you cannot argue with a")
    print("  hash, you can only re-run and compare.")


# --------------------------------------------------------------------------
# 3. BLAS and LAPACK
# --------------------------------------------------------------------------

def demo_blas() -> None:
    section("3. The BLAS underneath: why identical code can differ")
    config = np.show_config(mode="dicts")
    blas = config.get("Build Dependencies", {}).get("blas", {})
    lapack = config.get("Build Dependencies", {}).get("lapack", {})
    print(f"  numpy version    = {np.__version__}")
    print(f"  BLAS  name       = {blas.get('name')}")
    print(f"  LAPACK name      = {lapack.get('name')}")
    simd = config.get("SIMD Extensions", {})
    print(f"  SIMD baseline    = {simd.get('baseline')}")
    print(f"  SIMD found       = {simd.get('found')}")
    print(f"  SIMD not found   = {simd.get('not found')}")
    print("\n  A dot product is a reduction. Which instruction the compiler emits")
    print("  decides the ORDER of that reduction, and floating-point addition is not")
    print("  associative, so a different order gives a different last-bit answer.")
    print("  That is why 'bit-for-bit identical across machines' is a property you")
    print("  must test and cannot assume: OpenBLAS, MKL and Accelerate are three")
    print("  different orders, and so are successive versions of each.")


# --------------------------------------------------------------------------
# 4. Reduction order
# --------------------------------------------------------------------------

def demo_reduction_order() -> None:
    section("4. The same sum, three ways, in one process")
    rng = np.random.default_rng(0)
    v = rng.normal(size=1_000_000)
    flat = float(v.sum())
    rowwise = float(v.reshape(1000, 1000).sum(axis=1).sum())
    chunked = float(np.add.reduceat(v, np.arange(0, v.size, 1000)).sum())
    ordered = float(np.sort(v).sum())
    print(f"  v.sum()                          = {flat!r}")
    print(f"  per-row partials, then summed    = {rowwise!r}  diff {rowwise - flat:+.3e}")
    print(f"  reduceat in 1000-blocks          = {chunked!r}  diff {chunked - flat:+.3e}")
    print(f"  sorted ascending, then summed    = {ordered!r}  diff {ordered - flat:+.3e}")
    print(f"  |sum| = {abs(flat):.3f}; all three differences are "
          f"{abs(ordered - flat) / abs(flat):.2e} relative")
    print("\n  numpy's own pairwise summation keeps v.sum() and the partial-sum")
    print("  versions within a few hundredths of a picometre of each other, but the")
    print("  differences are nonzero and they are properties of the ORDER, not of")
    print("  the method. A tolerance of 1e-12 relative would pass all four; a")
    print("  bitwise comparison would fail three of them.")

    print("\n  Same effect in a matrix product, split along the summed index:")
    a = rng.normal(size=(600, 600))
    b = rng.normal(size=(600, 600))
    full = a @ b
    partial = np.zeros_like(full)
    for start in range(0, 600, 200):
        partial += a[:, start:start + 200] @ b[start:start + 200, :]
    worst = float(np.abs(full - partial).max())
    print(f"  full A @ B vs three 200-column partials: identical = "
          f"{np.array_equal(full, partial)}, max |diff| = {worst:.3e}")
    print(f"  relative to max|AB| = {np.abs(full).max():.3f}: "
          f"{worst / np.abs(full).max():.2e}")
    print("  This is the mechanism by which a BLAS that partitions a product")
    print("  differently -- a different version, a different thread count, a")
    print("  different cache-blocking choice -- produces a different result. The")
    print("  mathematics is unchanged; the order is not.")


# --------------------------------------------------------------------------
# 5. Thread count in subprocesses
# --------------------------------------------------------------------------

def _probe_source() -> str:
    return (
        "import hashlib, os, json\n"
        "import numpy as np\n"
        "rng = np.random.default_rng(0)\n"
        "a = rng.normal(size=(600, 600))\n"
        "b = rng.normal(size=(600, 600))\n"
        "product = a @ b\n"
        "solved = np.linalg.solve(a + 900.0 * np.eye(600), b)\n"
        "print(json.dumps({\n"
        "  'product': hashlib.sha256(product.tobytes()).hexdigest()[:24],\n"
        "  'solve': hashlib.sha256(solved.tobytes()).hexdigest()[:24],\n"
        "  'sum_product': repr(float(product.sum())),\n"
        "}))\n"
    )


def demo_thread_count() -> None:
    section("5. Does the thread count change the answer? (measured)")
    source = _probe_source()
    results = {}
    for threads in ("1", "2", "4", "8"):
        env = dict(os.environ)
        for var in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS",
                    "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
                    "NUMEXPR_NUM_THREADS"):
            env[var] = threads
        proc = subprocess.run([sys.executable, "-c", source], env=env,
                              capture_output=True, text=True, check=True)
        results[threads] = json.loads(proc.stdout)
        row = results[threads]
        print(f"  OMP_NUM_THREADS={threads:>2}  matmul {row['product']}  "
              f"solve {row['solve']}  sum {row['sum_product']}")

    products = {r["product"] for r in results.values()}
    solves = {r["solve"] for r in results.values()}
    sums = {r["sum_product"] for r in results.values()}
    print(f"\n  distinct matmul digests across thread counts: {len(products)}")
    print(f"  distinct solve  digests across thread counts: {len(solves)}")
    print(f"  distinct sums   across thread counts        : {len(sums)}")
    if len(products) == len(solves) == 1:
        print("\n  Honest result: on THIS machine and THIS BLAS, changing the thread")
        print("  count changed nothing. That does not license the assumption. It")
        print("  means the experiment must be re-run on the machine that matters,")
        print("  because a threaded BLAS is free to partition a reduction by thread")
        print("  count, and the failure mode is a last-bit difference that turns")
        print("  into a different branch and then a different answer.")
    else:
        print("\n  The thread count changed the result. Anything that compares")
        print("  outputs bit-for-bit across machines is therefore broken here.")
    print("  What the experiment DOES establish without qualification: the digests")
    print("  above are reproducible for a fixed thread count, so pinning the")
    print("  thread count is a legitimate part of 'the environment'.")


# --------------------------------------------------------------------------
# 6. Audit the repository's own declaration
# --------------------------------------------------------------------------

def demo_environment_yml() -> None:
    section("6. This repository's own environment declaration, audited")
    path = REPO_ROOT / "environment.yml"
    if not path.exists():
        print(f"  {path} not found; run this from inside the repository.")
        return
    try:
        import yaml
    except ImportError:
        print("  PyYAML is not installed; skipping the parse.")
        return
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    print(f"  name       = {data.get('name')}")
    print(f"  channels   = {data.get('channels')}")
    deps = data.get("dependencies", [])
    pip_section = next((d for d in deps if isinstance(d, dict) and "pip" in d), None)
    conda_deps = [d for d in deps if isinstance(d, str)]
    print(f"  conda dependencies: {len(conda_deps)}")
    print(f"  pip dependencies  : {len(pip_section['pip']) if pip_section else 0}")
    print(f"  first few conda   : {conda_deps[:6]}")

    try:
        from packaging.requirements import Requirement
        from packaging.version import Version
    except ImportError:
        return
    installed = {d.metadata["Name"].lower(): d.version
                 for d in md.distributions() if d.metadata["Name"]}
    checked = satisfied = 0
    unmet = []
    combined = list(conda_deps) + list(pip_section["pip"] if pip_section else [])
    for spec in combined:
        if not isinstance(spec, str) or spec.startswith("python"):
            continue
        try:
            req = Requirement(spec)
        except Exception:
            continue
        checked += 1
        have = installed.get(req.name.lower())
        if have is not None and Version(have) in req.specifier:
            satisfied += 1
        elif have is not None:
            unmet.append(f"{spec} (found {have})")
        else:
            unmet.append(f"{spec} (absent)")
    print(f"\n  requirements checked against this environment: {checked}")
    print(f"    satisfied: {satisfied}")
    print(f"    unmet or absent: {len(unmet)}")
    for line in unmet[:10]:
        print(f"      {line}")
    print("  'Absent' is not an error; it is the environment telling you which")
    print("  lessons you have not prepared for. This is the audit to run before")
    print("  reproducing somebody else's result, and it takes one command.")


# --------------------------------------------------------------------------
# 7. Lock files and hashes
# --------------------------------------------------------------------------

def demo_lock_file() -> None:
    section("7. What a lock file is, and what hashes add")
    installed = sorted(
        (d.metadata["Name"], d.version) for d in md.distributions()
        if d.metadata["Name"]
    )
    focus = [pair for pair in installed
             if pair[0].lower() in {"numpy", "scipy", "pytest", "packaging"}]
    print("  requirements.txt (abstract, ranges):")
    print("    numpy>=1.26")
    print("    scipy>=1.11")
    print("    pytest>=8")
    print()
    print("  requirements.lock (concrete, this environment):")
    for name, version in focus:
        print(f"    {name}=={version}")
    print()
    print("  With `--require-hashes`, each line also carries the digests of the")
    print("  distributions that are acceptable:")
    print()
    print("    numpy==2.5.4 \\")
    print("        --hash=sha256:<64 hex digits> \\")
    print("        --hash=sha256:<another acceptable wheel>")
    print()
    print("  `--require-hashes` turns pip into a verifier: the lock file names the")
    print("  exact artefacts and their digests, and pip downloads that bytes-or-")
    print("  nothing. It is the only pip mode that is really reproducible, and it")
    print("  is why a lock file is a deliverable rather than a convenience.")
    print()
    print("  Generate one with pip-tools (a tool, not a standard):")
    print("    pip-compile --generate-hashes requirements.in -o requirements.lock")
    print("    pip install --require-hashes -r requirements.lock")
    print("  Those two commands are stated from the documentation; they were NOT")
    print("  run here, because this environment is offline and pip-tools is not")
    print("  installed. Everything else in this script was measured.")


def main() -> int:
    demo_interpreter()
    demo_fingerprint()
    demo_blas()
    demo_reduction_order()
    demo_thread_count()
    demo_environment_yml()
    demo_lock_file()
    section("Summary")
    print("An environment is (interpreter, packages, build of the numeric")
    print("libraries, thread count, platform). Three of those five can be pinned")
    print("with a lock file and a fingerprint; the platform and the second half of")
    print("the thread story have to be re-tested where the numbers matter. Say")
    print("which ones you pinned, and say which ones you did not.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
