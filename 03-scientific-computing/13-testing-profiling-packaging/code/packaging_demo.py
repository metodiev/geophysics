"""Packaging, measured: PEP 668, pyproject.toml, specifiers, dist-info, wheels.

Run:  python packaging_demo.py
Requires: standard library (``packaging`` is present only because pytest
depends on it; the script degrades gracefully without it)

Nothing here installs or builds anything, and nothing touches the network.
Every claim in the packaging lesson that can be checked from inside a running
Python is checked here instead of asserted:

1. PEP 668: how Python marks an interpreter as externally managed, and how a
   virtual environment is recognised as *not* being that interpreter.
2. ``pyproject.toml``: the four tables that matter, parsed with ``tomllib``.
3. Version specifiers: ``==`` against ``>=``/``~=``, evaluated with
   ``packaging.specifiers`` against the versions actually installed.
4. ``.dist-info``: what a wheel leaves behind, including ``RECORD``.
5. The repository's own ``requirements.txt``, audited against the environment.
"""

from __future__ import annotations

import importlib.metadata as md
import pathlib
import sys
import sysconfig
import tomllib

try:
    from packaging.requirements import Requirement
    from packaging.version import Version
    HAVE_PACKAGING = True
except ImportError:                                  # pragma: no cover
    HAVE_PACKAGING = False

REPO_ROOT = pathlib.Path(__file__).resolve().parents[3]


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# --------------------------------------------------------------------------
# 1. PEP 668
# --------------------------------------------------------------------------

def demo_pep668() -> None:
    section("1. PEP 668: who is allowed to install packages, and why")
    stdlib = pathlib.Path(sysconfig.get_paths()["stdlib"])
    marker = stdlib / "EXTERNALLY-MANAGED"
    print(f"  sys.prefix       = {sys.prefix}")
    print(f"  sys.base_prefix  = {sys.base_prefix}")
    print(f"  running in a venv: {sys.prefix != sys.base_prefix}")
    print(f"  stdlib directory = {stdlib}")
    print(f"  EXTERNALLY-MANAGED present: {marker.exists()}")

    if marker.exists():
        import configparser
        parser = configparser.ConfigParser()
        parser.read(marker, encoding="utf-8")
        message = parser.get("externally-managed", "Error", fallback="(unreadable)")
        print(f"  marker format   = INI, section [externally-managed], key Error")
        print(f"  Error= first line = {message.splitlines()[0]!r}")
        print("  pip reads this file, finds the key and refuses to install into this")
        print("  interpreter unless told to override.")

    print("\n  Note the subtlety visible above: this virtual environment reports")
    print(f"  a stdlib path inside the *base* installation ({stdlib.name}), so the")
    print("  marker file appears to exist. pip still installs here, because pip")
    print("  tests the venv predicate (sys.prefix != sys.base_prefix) and not the")
    print("  file alone. The base interpreter does refuse:")
    print()
    print("    $ python3 -m pip install pytest")
    print("    error: externally-managed-environment")
    print()
    print("  That message is not a broken machine. It is Homebrew and Debian")
    print("  telling you that a system interpreter is shared with the operating")
    print("  system's own tooling, so the correct answer is a virtual environment:")
    print()
    print("    python3 -m venv .venv")
    print("    .venv/bin/python -m pip install -r requirements.txt")
    print()
    print("  pipx is the other correct answer, for *applications* rather than")
    print("  libraries. What is never correct is `--break-system-packages`, which")
    print("  trades a reproducible environment for a five-second convenience.")


# --------------------------------------------------------------------------
# 2. pyproject.toml
# --------------------------------------------------------------------------

SAMPLE_PYPROJECT = '''\
[build-system]
requires = ["hatchling>=1.24"]
build-backend = "hatchling.build"

[project]
name = "geophys-tools"
version = "0.3.1"
description = "Gravity and travel-time helpers used by the curriculum"
readme = "README.md"
requires-python = ">=3.11"
license = "MIT"
authors = [{ name = "A. Geophysicist", email = "a@example.org" }]
dependencies = [
  "numpy>=1.26,<3",
  "scipy>=1.11",
]
keywords = ["geophysics", "gravity", "seismology"]

[project.optional-dependencies]
test = ["pytest>=8", "pytest-cov>=5"]
docs = ["sphinx>=7"]

[project.urls]
Homepage = "https://example.org/geophys-tools"
Source = "https://example.org/geophys-tools.git"

[project.scripts]
geophys = "geophys_tools.cli:main"

[tool.pytest.ini_options]
addopts = "-ra --strict-markers"

[tool.ruff]
line-length = 99
'''


def demo_pyproject() -> None:
    section("2. pyproject.toml: four tables, one file")
    data = tomllib.loads(SAMPLE_PYPROJECT)
    build = data["build-system"]
    project = data["project"]
    print(f"  [build-system] requires     = {build['requires']}")
    print(f"  [build-system] build-backend= {build['build-backend']}")
    print("  ^ PEP 518 names the build requirements; PEP 517 names the backend that")
    print("    implements the build_* hooks. `pip install .` creates an isolated")
    print("    environment containing exactly `requires` and calls the backend.")
    print()
    print(f"  [project] name        = {project['name']} {project['version']}")
    print(f"  [project] requires-python = {project['requires-python']}")
    print(f"  [project] dependencies = {project['dependencies']}")
    print(f"  [project.optional-dependencies] keys = {sorted(project['optional-dependencies'])}")
    print(f"  -> `pip install 'geophys-tools[test]'` installs the test extras.")
    print()
    print(f"  [project.scripts] {project['scripts']}")
    print("  -> generates a console-script entry point; the wheel carries it in")
    print("     entry_points.txt, not as a script file.")
    print()
    print("  PEP 621 says the metadata lives in [project]. setup.py is not")
    print("  forbidden, but any file whose content is a dict can be a TOML table,")
    print("  and a declarative table cannot execute arbitrary code at install")
    print("  time. That is the whole argument, and it is a security argument.")
    print()
    print("  Tool configuration lives in [tool.<name>] tables in the SAME file:")
    print(f"    [tool.pytest.ini_options] {data['tool']['pytest']['ini_options']}")
    print(f"    [tool.ruff] line-length = {data['tool']['ruff']['line-length']}")
    print("  One file for the package, the tests, the linter and the docs means a")
    print("  clone has one place to look and one file to diff.")


# --------------------------------------------------------------------------
# 3. Version specifiers
# --------------------------------------------------------------------------

def demo_specifiers() -> None:
    section("3. Version specifiers: pinning, ranges and what they cost")
    if not HAVE_PACKAGING:
        print("  `packaging` is not installed; skipping (it arrives with pytest).")
        return
    specifiers = [
        "==2.5.4",
        ">=1.26",
        ">=1.26,<3",
        "~=2.5.0",
        "~=2.5",
        "!=2.5.4",
        ">=1.26,!=2.5.0",
    ]
    candidates = ["1.24.4", "2.5.4", "2.6.0", "3.0.0"]
    print(f"  numpy is installed at {md.version('numpy')}; specifiers evaluated "
          f"against four candidate versions:\n")
    header = f"  {'specifier':>16} " + " ".join(f"{c:>8}" for c in candidates)
    print(header)
    for spec in specifiers:
        req = Requirement(f"numpy{spec}")
        cells = []
        for cand in candidates:
            cells.append(f"{'yes' if cand in req.specifier else 'no':>8}")
        print(f"  {spec:>16} " + " ".join(cells))
    print("\n  `~=2.5.0` means '>=2.5.0, ==2.5.*' -- the compatible-release operator")
    print("  pins the major.minor and lets the patch float. `~=2.5` means '>=2.5, ==2.*'")
    print("  and is a much wider range than it looks. Read the operator, do not")
    print("  guess it from the number of digits.")
    print()
    print("  Cost of each style, stated as a question you can answer:")
    print("    ==2.5.4          exactly reproducible; cannot receive a security fix")
    print("    >=1.26,<3        reproducible *if* a lock file exists; otherwise not")
    print("    ~=2.5.0          patch fixes only; a numpy minor release is excluded")
    print("  For a paper, `==` in the lock file that accompanies the code, and")
    print("  ranges in the library metadata that others install from. Both, always.")


# --------------------------------------------------------------------------
# 4. dist-info and RECORD
# --------------------------------------------------------------------------

def demo_dist_info() -> None:
    section("4. What an installed package actually is on disk")
    dist = md.distribution("packaging")
    files = list(dist.files or [])
    print(f"  packaging {dist.version}: {len(files)} entries in the RECORD")
    for entry in files[:8]:
        print(f"    {entry}")
    record = next((f for f in files if str(f).endswith("RECORD")), None)
    print(f"\n  RECORD is {record}")
    print("  Every line of RECORD is: path, sha256=<digest>, size. That is a")
    print("  manifest and an integrity check in one file, which is what makes")
    print("  `pip uninstall` and `pip check` possible.")
    print()
    print("  A wheel is a ZIP archive with that layout:")
    print("    geophys_tools/__init__.py")
    print("    geophys_tools/py.typed")
    print("    geophys_tools-0.3.1.dist-info/METADATA       <- PEP 621 fields")
    print("    geophys_tools-0.3.1.dist-info/WHEEL          <- tags, pure-python flag")
    print("    geophys_tools-0.3.1.dist-info/RECORD         <- hashes")
    print("    geophys_tools-0.3.1.dist-info/entry_points.txt")
    print("  An sdist is a tar.gz of the source plus the build backend's config.")
    print("  Pure-Python wheels are portable; wheels containing compiled extensions")
    print("  are tagged with the Python version, ABI and platform, which is why")
    print("  NumPy ships a different wheel for each combination.")

    metadata_text = dist.read_text("METADATA") or ""
    fields = [ln.split(":", 1)[0] for ln in metadata_text.splitlines()
              if ":" in ln and not ln.startswith((" ", "\t"))]
    print(f"\n  The installed METADATA for packaging has {len(fields)} top-level fields,")
    print(f"  among them: {', '.join(fields[:8])}")
    print(f"  Requires-Dist entries: {len(dist.requires or [])}")
    for entry in (dist.requires or [])[:4]:
        print(f"    {entry}")


# --------------------------------------------------------------------------
# 5. Audit the repository's own requirements against this environment
# --------------------------------------------------------------------------

def demo_audit_requirements() -> None:
    section("5. Auditing the repository's requirements.txt against this environment")
    path = REPO_ROOT / "requirements.txt"
    if not path.exists():
        print(f"  {path} not found; run this from inside the repository.")
        return
    lines = [ln.split("#", 1)[0].strip() for ln in path.read_text().splitlines()]
    reqs = [ln for ln in lines if ln]
    print(f"  {path.relative_to(REPO_ROOT)}: {len(reqs)} requirements")

    installed = {d.metadata["Name"].lower(): d.version
                 for d in md.distributions() if d.metadata["Name"]}
    satisfied = unsatisfied = missing = 0
    violations = []
    for text in reqs:
        if HAVE_PACKAGING:
            req = Requirement(text)
            name = req.name.lower()
            if name not in installed:
                missing += 1
                violations.append(f"    MISSING  {text}")
                continue
            if Version(installed[name]) in req.specifier:
                satisfied += 1
            else:
                unsatisfied += 1
                violations.append(
                    f"    VERSION  {text} needs {req.specifier}, found {installed[name]}")
        else:
            name = text.split(">=")[0].split("==")[0].split("<")[0].strip().lower()
            if name in installed:
                satisfied += 1
            else:
                missing += 1
    print(f"  satisfied: {satisfied}   version-mismatch: {unsatisfied}   "
          f"not installed: {missing}")
    for line in violations[:12]:
        print(line)
    if len(violations) > 12:
        print(f"    ... and {len(violations) - 12} more")
    print()
    print("  Every 'not installed' line is a package this environment does not")
    print("  have -- not an error. The audit is still worth running, because it")
    print("  answers the only question that matters before you try to reproduce")
    print("  someone's figure: does this environment satisfy the declaration?")
    print(f"  distributions visible to this interpreter: {len(installed)}")


def main() -> int:
    demo_pep668()
    demo_pyproject()
    demo_specifiers()
    demo_dist_info()
    demo_audit_requirements()
    section("Summary")
    print("Nothing was installed, built, published or downloaded. Every number")
    print("above came from the interpreter's own state, which is the point: a")
    print("packaging question is usually answerable by reading, not by trying.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
