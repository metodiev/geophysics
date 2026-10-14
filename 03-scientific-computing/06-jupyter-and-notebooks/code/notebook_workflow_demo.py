"""Notebook workflow: cells, kernels, execution order and hidden state.

Run:  .venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/notebook_workflow_demo.py
Requires: nbformat, nbclient (both present in the repository virtual environment).

Companion to lesson 03-06-01.

Everything is measured, never assumed. The script builds notebooks in memory,
executes them through a real IPython kernel with ``nbclient``, and reports what
the kernel actually did: execution counts, error types, kernel language and
version, and the execution counts that survive a save to disk.

Part 1  a five-cell notebook executed top to bottom: what the kernel records.
Part 2  re-executing one cell: why stored outputs stop describing a linear run.
Part 3  execution order decides the answer: a NameError from a swapped pair.
Part 4  a fresh kernel loses all memory: the state-model experiment.
Part 5  what a save to disk actually persists.
"""

from __future__ import annotations

import asyncio
import hashlib
import json
import shutil
from pathlib import Path

import nbformat
from jupyter_client.kernelspec import KernelSpecManager
from nbclient import NotebookClient

ARTIFACTS = Path(__file__).resolve().parent / ".demo-artifacts"
KERNEL = "python3"
CELL_TIMEOUT = 120


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def code_cell(src: str):
    return nbformat.v4.new_code_cell(src)


def md_cell(src: str):
    return nbformat.v4.new_markdown_cell(src)


def stream_text(cell) -> str:
    """Flatten a cell's outputs into the text a reader would see."""
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


async def _execute(nb, plans) -> None:
    client = NotebookClient(
        nb, kernel_name=KERNEL, timeout=CELL_TIMEOUT, allow_errors=True
    )
    # ``async_setup_kernel`` is an async context manager: entering it starts the
    # kernel, leaving it shuts the kernel down again. Every plan in ``plans``
    # runs against the SAME kernel, in the order given -- which is exactly how a
    # human works: one kernel, cells run in whatever order they click.
    async with client.async_setup_kernel():
        for plan in plans:
            for index in plan:
                await client.async_execute_cell(nb.cells[index], index)


def run(nb, plans) -> None:
    """Execute ``plans`` (a list of cell-index sequences) in one fresh kernel."""
    asyncio.run(_execute(nb, plans))


def collect_errors(nb) -> list[str]:
    return [o.get("ename") for cell in nb.cells for o in cell.outputs
            if o.get("output_type") == "error"]


def report_counts(nb, label: str) -> None:
    counts = [cell.get("execution_count") for cell in nb.cells
              if cell.cell_type == "code"]
    print(f"  {label}: execution_count = {counts}")


def main() -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    try:
        # ------------------------------------------------------------------
        section("1. A five-cell notebook executed top to bottom")
        # ------------------------------------------------------------------
        nb = nbformat.v4.new_notebook(
            cells=[
                md_cell("# Gravity reduction\n\nStation spacing $\\Delta x$ in metres."),
                code_cell("import sys\nG = 6.674e-11\nprint('G =', G, 'm3 kg-1 s-2')"),
                code_cell("station_spacing = 25.0  # m\nprint('spacing =', station_spacing, 'm')"),
                code_cell("line_length = 40 * station_spacing\nprint('line length =', line_length, 'm')"),
                code_cell("print('python', sys.version.split()[0])"),
            ]
        )
        print(f"  cells in notebook: {len(nb.cells)} "
              f"({sum(c.cell_type == 'markdown' for c in nb.cells)} markdown, "
              f"{sum(c.cell_type == 'code' for c in nb.cells)} code)")
        run(nb, [range(len(nb.cells))])
        report_counts(nb, "after run-all")
        for i, cell in enumerate(nb.cells):
            if cell.cell_type != "code":
                continue
            print(f"    cell {i}: count={cell.execution_count:<3} "
                  f"-> {stream_text(cell).splitlines()[0]}")
        lang = nb.metadata.get("language_info", {})
        spec = KernelSpecManager().get_kernel_spec(KERNEL)
        print(f"  kernelspec on this machine: name={KERNEL!r}, "
              f"argv={spec.argv}, resource_dir={spec.resource_dir}")
        print(f"  notebook format on disk: nbformat {nb.nbformat}.{nb.nbformat_minor}")
        print(f"  language_info populated by the run: {lang or 'not populated'}")
        print("  Observation: the counts are 1..4 in file order, which is what")
        print("  'a notebook whose stored outputs came from a linear run' means.")

        # ------------------------------------------------------------------
        section("2. Re-executing one cell makes the stored outputs stale")
        # ------------------------------------------------------------------
        # One kernel; first the linear run, then the first code cell clicked again.
        run(nb, [range(len(nb.cells)), [1]])
        report_counts(nb, "after re-running code cell 1 (same kernel)")
        stale = [i for i, c in enumerate(nb.cells)
                 if c.cell_type == "code" and c.execution_count != max(
                     x.get("execution_count", 0) for x in nb.cells
                     if x.cell_type == "code")]
        print(f"  cells whose count is below the highest count: {len(stale)} of 4")
        print("  Observation: nothing was recomputed for those cells, yet the")
        print("  notebook is now self-inconsistent: a reader cannot tell which")
        print("  numbers share a single kernel state. Only a restart-and-run-all")
        print("  makes the stored outputs self-describing again.")

        # ------------------------------------------------------------------
        section("3. Execution order decides the answer")
        # ------------------------------------------------------------------
        # A cell that uses a name its neighbour defines. Clicked on its own
        # (which is what happens when a reader scrolls and hits Shift+Enter in
        # the middle of a notebook), it fails.
        dep = nbformat.v4.new_notebook(
            cells=[
                code_cell("rho = 2670.0  # kg m-3, mean crustal density"),
                code_cell("print(f'rho = {rho / 1000.0:.3f} g cm-3')"),
            ]
        )
        run(dep, [[1]])
        print(f"  clicking cell 1 on its own -> {stream_text(dep.cells[1])!r}")
        print(f"  error outputs stored: {collect_errors(dep)}")
        run(dep, [[0, 1]])
        print(f"  then cell 0 followed by cell 1 -> {stream_text(dep.cells[1])!r}")
        print(f"  error outputs left in the notebook afterwards: {collect_errors(dep)}")
        print(f"  execution counts: {[c.execution_count for c in dep.cells]}")
        print("  Observation: the failure is stored as an ordinary output, and")
        print("  re-running the cell *replaces* it. There is no record in the file")
        print("  that a reader ever saw a NameError here.")

        # ------------------------------------------------------------------
        section("4. A fresh kernel loses everything")
        # ------------------------------------------------------------------
        half = nbformat.v4.new_notebook(
            cells=[
                code_cell("kappa = 1.1e-6  # m2 s-1, thermal diffusivity"),
            ]
        )
        run(half, [[0]])
        print(f"  after first kernel: kappa defined, "
              f"count={half.cells[0].execution_count}")
        late = nbformat.v4.new_notebook(
            cells=[code_cell("print('kappa =', kappa)")]
        )
        run(late, [[0]])
        err = [o.get("ename") for o in late.cells[0].outputs
               if o.get("output_type") == "error"]
        print(f"  new kernel, same-looking cell -> {stream_text(late.cells[0])!r}")
        print(f"  error type: {err}")
        print("  Observation: state lives in the kernel process, not in the")
        print("  file. Two notebooks open at once are two independent states even")
        print("  when they share an interpreter name.")

        # ------------------------------------------------------------------
        section("5. What a save to disk actually persists")
        # ------------------------------------------------------------------
        path = ARTIFACTS / "workflow_demo.ipynb"
        nbformat.write(nb, path)
        raw = json.loads(path.read_text(encoding="utf-8"))
        on_disk = [c.get("execution_count") for c in raw["cells"]
                   if c.get("cell_type") == "code"]
        print(f"  wrote {path.name}: {path.stat().st_size} bytes")
        print(f"  execution_count persisted in the file: {on_disk}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        print(f"  sha256 of the file (first 16 hex): {digest[:16]}")
        print("  Observation: outputs and counts are saved; the kernel, its")
        print("  variables and any library state are not. Reopening the file and")
        print("  pressing Restart does not reproduce Section 1 -- re-running does.")

        # ------------------------------------------------------------------
        section("6. How many execution orders are legal?")
        # ------------------------------------------------------------------
        import itertools

        def valid_orders(n_cells, dependencies):
            """Count permutations in which every dependency comes first."""
            count = 0
            for order in itertools.permutations(range(n_cells)):
                position = {cell: index for index, cell in enumerate(order)}
                if all(position[before] < position[after]
                       for before, after in dependencies):
                    count += 1
            return count

        total = __import__("math").factorial(4)
        for label, deps in [
            ("no dependencies", []),
            ("one dependency (2 needs 1)", [(1, 2)]),
            ("a chain 1 -> 2 -> 3 -> 4", [(0, 1), (1, 2), (2, 3)]),
            ("a fork (4 needs 1 and 3)", [(0, 3), (2, 3)]),
        ]:
            legal = valid_orders(4, deps)
            print(f"  {label:<28} legal orders {legal:>2} of {total} "
                  f"= {legal / total:.4f}")
        print(f"  1/2 = {0.5:.4f}, 1/24 = {1 / 24:.4f}")
        print("  Observation: a single dependency halves the legal orders and")
        print("  a chain leaves exactly one. Clicking cells at random is")
        print("  therefore a coin toss for a two-cell dependency and a")
        print("  certainty of failure for a chain.")

        # ------------------------------------------------------------------
        section("7. Determinism of the counts across two identical runs")
        # ------------------------------------------------------------------
        nb_a = nbformat.v4.new_notebook(cells=[code_cell("print(6 * 7)")])
        nb_b = nbformat.v4.new_notebook(cells=[code_cell("print(6 * 7)")])
        run(nb_a, [[0]])
        run(nb_b, [[0]])
        ca = [c.execution_count for c in nb_a.cells]
        cb = [c.execution_count for c in nb_b.cells]
        print(f"  run A counts: {ca}, output {stream_text(nb_a.cells[0])!r}")
        print(f"  run B counts: {cb}, output {stream_text(nb_b.cells[0])!r}")
        print(f"  counts and output identical: {ca == cb and stream_text(nb_a.cells[0]) == stream_text(nb_b.cells[0])}")
    finally:
        shutil.rmtree(ARTIFACTS, ignore_errors=True)


if __name__ == "__main__":
    main()
