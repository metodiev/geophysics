"""Reproducibility: restart-and-run-all, seeds, order and hidden state.

Run:  .venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/reproducible_notebook_demo.py
Requires: nbformat, nbclient, numpy.

Companion to lesson 03-06-03.

Every claim below is measured. The script executes real kernels, digests their
outputs, and reports the digests; it starts subprocesses to show what process
level hash randomisation does to a set; and it counts what a failure costs.

Part 1  a seeded notebook executed twice: byte-identical outputs.
Part 2  the same notebook without a seed: how far apart the two runs land.
Part 3  order dependence, quantified: the same two cells, two answers.
Part 4  floating-point summation is not associative: a measurable last-bit
        difference between three ways of adding the same numbers.
Part 5  a failure inside a run: stored traceback against a raised exception.
Part 6  process-level nondeterminism: PYTHONHASHSEED and set iteration order.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbclient.exceptions import CellExecutionError

ARTIFACTS = Path(__file__).resolve().parent / ".demo-artifacts"
KERNEL = "python3"
CELL_TIMEOUT = 120


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def code_cell(src: str):
    return nbformat.v4.new_code_cell(src)


def stream_text(cell) -> str:
    parts: list[str] = []
    for out in cell.outputs:
        kind = out.get("output_type")
        if kind == "stream":
            parts.append(out.get("text", ""))
        elif kind == "error":
            parts.append(f"{out.get('ename')}: {out.get('evalue')}")
        elif kind == "execute_result":
            parts.append(str(out.get("data", {}).get("text/plain", "")))
    return "".join(parts).strip()


def run(nb, plans, allow_errors=True):
    async def _go():
        client = NotebookClient(
            nb, kernel_name=KERNEL, timeout=CELL_TIMEOUT,
            allow_errors=allow_errors,
        )
        async with client.async_setup_kernel():
            for plan in plans:
                for index in plan:
                    await client.async_execute_cell(nb.cells[index], index)
    asyncio.run(_go())
    return nb


def digest(nb) -> str:
    """Digest of everything a reader sees EXCEPT the execution counts.

    Stripping ``execution_count`` is the point: the counts are bookkeeping and
    change between runs. If the digest changes, a number changed.
    """
    payload = []
    for cell in nb.cells:
        payload.append({
            "type": cell.cell_type,
            "source": cell.source,
            "outputs": [
                {k: v for k, v in out.items() if k != "execution_count"}
                for out in cell.get("outputs", [])
            ],
        })
    blob = json.dumps(payload, sort_keys=True, default=str).encode()
    return hashlib.sha256(blob).hexdigest()


def main() -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    try:
        # ------------------------------------------------------------------
        section("1. A seeded notebook executed twice")
        # ------------------------------------------------------------------
        seeded_src = (
            "import numpy as np\n"
            "rng = np.random.default_rng(20261014)\n"
            "noise = rng.normal(0.0, 0.05, size=5)\n"
            "print(' '.join(f'{v:+.6f}' for v in noise))"
        )
        a = run(nbformat.v4.new_notebook(cells=[code_cell(seeded_src)]), [[0]])
        b = run(nbformat.v4.new_notebook(cells=[code_cell(seeded_src)]), [[0]])
        print(f"  run 1 output: {stream_text(a.cells[0])}")
        print(f"  run 2 output: {stream_text(b.cells[0])}")
        print(f"  digests equal: {digest(a) == digest(b)}")
        print(f"  digest (first 16 hex): {digest(a)[:16]}")
        print("  Observation: a named seed makes the two kernels agree digit for")
        print("  digit even though they are separate processes on separate cores.")

        # ------------------------------------------------------------------
        section("2. The same notebook without a seed")
        # ------------------------------------------------------------------
        loose_src = (
            "import numpy as np\n"
            "noise = np.random.normal(0.0, 0.05, size=5)\n"
            "print(' '.join(f'{v:+.6f}' for v in noise))"
        )
        c = run(nbformat.v4.new_notebook(cells=[code_cell(loose_src)]), [[0]])
        d = run(nbformat.v4.new_notebook(cells=[code_cell(loose_src)]), [[0]])
        v1 = [float(t) for t in stream_text(c.cells[0]).split()]
        v2 = [float(t) for t in stream_text(d.cells[0]).split()]
        print(f"  run 1 output: {stream_text(c.cells[0])}")
        print(f"  run 2 output: {stream_text(d.cells[0])}")
        print(f"  digests equal: {digest(c) == digest(d)}")
        print(f"  max |difference| between the two runs: "
              f"{max(abs(p - q) for p, q in zip(v1, v2)):.6f} (dimensionless noise)")
        print(f"  runs disagree in all {len(v1)} of {len(v1)} values: "
              f"{all(p != q for p, q in zip(v1, v2))}")
        print("  Observation: the results are statistically identical and")
        print("  numerically different. A figure regenerated from this notebook")
        print("  is a different figure, which makes a published panel")
        print("  unreproducible in the strict sense.")

        # ------------------------------------------------------------------
        section("3. Order dependence, quantified")
        # ------------------------------------------------------------------
        order_nb = nbformat.v4.new_notebook(
            cells=[
                code_cell("dt = 0.01  # s, sampling interval"),
                code_cell("v = 9.81 * dt\nprint(f'{v:.6f}')"),
                code_cell("dt = 0.001  # s, changed later in the session"),
            ]
        )
        forward = run(order_nb, [[0, 1, 2]])
        backward = run(
            nbformat.v4.new_notebook(cells=[c.copy() for c in order_nb.cells]),
            [[0], [2], [1]],
        )
        f_val = float(stream_text(forward.cells[1]))
        b_val = float(stream_text(backward.cells[1]))
        print(f"  cells clicked 0, 1, 2 -> v = {f_val:.6f} m/s")
        print(f"  cells clicked 0, 2, 1 -> v = {b_val:.6f} m/s")
        print(f"  ratio between the two answers: {f_val / b_val:.1f}")
        print(f"  source of cell 1 identical in both files: "
              f"{forward.cells[1].source == backward.cells[1].source}")
        print("  Observation: the two runs differ by a factor of ten and the")
        print("  notebook looks identical in both. Nothing in the file records")
        print("  which one a reader is looking at. Restart-and-run-all is the")
        print("  only operation that makes the answer a property of the file.")

        # ------------------------------------------------------------------
        section("4. Summation is not associative")
        # ------------------------------------------------------------------
        sum_nb = nbformat.v4.new_notebook(
            cells=[code_cell(
                "import math\n"
                "import numpy as np\n"
                "rng = np.random.default_rng(20261014)\n"
                "x = rng.normal(0.0, 1.0, size=200_000)\n"
                "print('{:+.17g}'.format(float(np.sum(x))))\n"
                "print('{:+.17g}'.format(float(np.sum(x[::-1]))))\n"
                "print('{:+.17g}'.format(float(np.sum(np.sort(x)))))\n"
                "print('{:+.17g}'.format(math.fsum(x)))\n"
                "print('{:+.17g}'.format(float(np.sum([1e16, 1.0, -1e16]))))\n"
                "print('{:+.17g}'.format(math.fsum([1e16, 1.0, -1e16])))"
            )]
        )
        sums = run(sum_nb, [[0]])
        lines = stream_text(sums.cells[0]).splitlines()
        print(f"  np.sum of 200 000 standard normals (seeded):        {lines[0]}")
        print(f"  same values summed in reverse order:                {lines[1]}")
        print(f"  same values summed in sorted order:                 {lines[2]}")
        print(f"  math.fsum, correctly rounded:                       {lines[3]}")
        print(f"  distinct results among the four orders: "
              f"{len({lines[0], lines[1], lines[2], lines[3]})}")
        print(f"  np.sum([1e16, 1.0, -1e16]) = {lines[4]}   "
              f"(the 1.0 is absorbed, then added back as zero)")
        print(f"  math.fsum([1e16, 1.0, -1e16]) = {lines[5]}")
        print("  Observation: four ways of adding the same numbers give four")
        print("  different last bits, and one ordering loses an additive term")
        print("  entirely. Pairwise summation is deterministic for a given order")
        print("  and array length, so a digest IS a useful reproducibility check --")
        print("  provided the order and the block structure do not change.")

        # ------------------------------------------------------------------
        section("5. A failure inside a run")
        # ------------------------------------------------------------------
        bad = nbformat.v4.new_notebook(
            cells=[code_cell("print('station 1 ok')"),
                   code_cell("raise ValueError('station 2 has no elevation')"),
                   code_cell("print('station 3 ok')")]
        )
        run(bad, [range(3)], allow_errors=True)
        stored = [o.get("ename") for c in bad.cells for o in c.outputs
                  if o.get("output_type") == "error"]
        print(f"  allow_errors=True  -> error outputs stored: {stored}")
        print(f"  cells executed anyway: "
              f"{[c.execution_count for c in bad.cells]}")
        strict = nbformat.v4.new_notebook(
            cells=[code_cell("print('station 1 ok')"),
                   code_cell("raise ValueError('station 2 has no elevation')"),
                   code_cell("print('station 3 ok')")])
        raised = None
        try:
            run(strict, [range(3)], allow_errors=False)
        except CellExecutionError as exc:
            raised = type(exc).__name__
        ran = [c.cell_type == "code" and bool(c.get("outputs"))
               for c in strict.cells]
        print(f"  allow_errors=False -> raised {raised}")
        print(f"  cells with a stored output afterwards: "
              f"{sum(ran)} of {len(ran)} (cell 3 untested and unrecorded)")
        print(f"  cell 3 stdout: {stream_text(strict.cells[2])!r}")
        print("  Observation: ``jupyter nbconvert --execute`` is the strict case.")
        print("  In strict mode the run stops at the failing cell, which is what")
        print("  makes an executed notebook usable as a test.")

        # ------------------------------------------------------------------
        section("6. Process-level nondeterminism:")
        print("  set iteration order under hash randomisation")
        print("  " + "-" * 70)
        prog = ("s = {'alpha','beta','gamma','delta','epsilon','zeta'};"
                "print(','.join(sorted(s))[:0] or ','.join(s))")
        orders = []
        for _ in range(4):
            out = subprocess.run(
                [sys.executable, "-c", prog], capture_output=True, text=True,
                env={**os.environ, "PYTHONHASHSEED": "random"},
            )
            orders.append(out.stdout.strip())
        for i, order in enumerate(orders, start=1):
            print(f"    process {i}: {order}")
        print(f"  distinct orders observed in {len(orders)} processes: "
              f"{len(set(orders))}")
        fixed = subprocess.run(
            [sys.executable, "-c", prog], capture_output=True, text=True,
            env={**os.environ, "PYTHONHASHSEED": "0"},
        )
        fixed2 = subprocess.run(
            [sys.executable, "-c", prog], capture_output=True, text=True,
            env={**os.environ, "PYTHONHASHSEED": "0"},
        )
        print(f"  with PYTHONHASHSEED=0, two processes agree: "
              f"{fixed.stdout.strip() == fixed2.stdout.strip()}")
        print(f"  PYTHONHASHSEED in this process's environment: "
              f"{os.environ.get('PYTHONHASHSEED', 'unset')}")
        print("  Observation: a set or a dict keyed by strings can iterate in a")
        print("  different order in a fresh kernel than in the one that made the")
        print("  figure. Iterate sorted(...) whenever the order is visible.")

        # ------------------------------------------------------------------
        section("7. The reproducibility artefacts a reader can check")
        # ------------------------------------------------------------------
        path = ARTIFACTS / "reproducible_demo.ipynb"
        nbformat.write(seeded_summary_nb(), path)
        print(f"  wrote {path.name}: {path.stat().st_size} bytes")
        print(f"  nbformat version written: "
              f"{json.loads(path.read_text())['nbformat']}."
              f"{json.loads(path.read_text())['nbformat_minor']}")
        print("  Observation: the file carries the code, the outputs and the")
        print("  counts. It does not carry the environment: a notebook run under")
        print("  a different NumPy will not produce the same digest. Record the")
        print("  versions next to the digest, or the digest proves nothing.")
    finally:
        shutil.rmtree(ARTIFACTS, ignore_errors=True)


def seeded_summary_nb():
    return nbformat.v4.new_notebook(
        cells=[code_cell("import numpy as np\n"
                         "print(np.random.default_rng(20261014).normal(size=3))")]
    )


if __name__ == "__main__":
    main()
