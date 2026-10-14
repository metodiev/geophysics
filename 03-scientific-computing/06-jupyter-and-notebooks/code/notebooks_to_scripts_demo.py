"""From notebook to script, test and report: what conversion keeps and loses.

Run:  .venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/notebooks_to_scripts_demo.py
Requires: nbformat, nbclient, nbconvert.

Companion to lesson 03-06-04.

Part 1  build and execute a small analysis notebook, capturing its stdout.
Part 2  export it with nbconvert's PythonExporter and compare the two.
Part 3  what the export does with IPython magics -- and the exit code when the
        exported script is run.
Part 4  the percent (``# %%``) module format, and why it is the better target.
Part 5  the command line equivalent, ``jupyter nbconvert --to script``.
Part 6  what an executed notebook is worth as a regression test.
"""

from __future__ import annotations

import asyncio
import shutil
import subprocess
import sys
from pathlib import Path

import nbformat
from nbclient import NotebookClient
from nbconvert import PythonExporter

ARTIFACTS = Path(__file__).resolve().parent / ".demo-artifacts"
KERNEL = "python3"
CELL_TIMEOUT = 120
PY = sys.executable


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def code_cell(src: str):
    return nbformat.v4.new_code_cell(src)


def stream_text(cell) -> str:
    parts = []
    for out in cell.outputs:
        if out.get("output_type") == "stream":
            parts.append(out.get("text", ""))
        elif out.get("output_type") == "error":
            parts.append(f"{out.get('ename')}: {out.get('evalue')}")
    return "".join(parts)


def run(nb, plans, allow_errors=True) -> None:
    async def _go():
        client = NotebookClient(nb, kernel_name=KERNEL, timeout=CELL_TIMEOUT,
                                allow_errors=allow_errors)
        async with client.async_setup_kernel():
            for plan in plans:
                for index in plan:
                    await client.async_execute_cell(nb.cells[index], index)
    asyncio.run(_go())


def build_notebook():
    return nbformat.v4.new_notebook(
        cells=[
            nbformat.v4.new_markdown_cell(
                "# Bouguer slab correction\n\n"
                "The slab correction is $2\\pi G\\rho h$ in SI units."
            ),
            code_cell(
                "%matplotlib inline\n"
                "import numpy as np\n"
                "G = 6.674e-11\n"
                "rho = 2670.0  # kg m-3"
            ),
            code_cell(
                "h = 100.0  # m\n"
                "slab = 2.0 * np.pi * G * rho * h\n"
                "print(f'slab correction = {slab:.6e} m/s^2')"
            ),
            code_cell(
                "print(f'            in mGal = {slab / 1e-5:.6f}')"
            ),
        ]
    )


def main() -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    try:
        # ------------------------------------------------------------------
        section("1. Execute the notebook and capture what it printed")
        # ------------------------------------------------------------------
        nb = build_notebook()
        run(nb, [range(len(nb.cells))])
        notebook_stdout = "".join(
            stream_text(c) for c in nb.cells if c.cell_type == "code"
        )
        print(f"  cells: {len(nb.cells)} "
              f"({sum(c.cell_type == 'markdown' for c in nb.cells)} markdown, "
              f"{sum(c.cell_type == 'code' for c in nb.cells)} code)")
        print(f"  execution counts: "
              f"{[c.execution_count for c in nb.cells if c.cell_type == 'code']}")
        print("  stdout the notebook produced:")
        for line in notebook_stdout.strip().splitlines():
            print(f"    | {line}")
        nb_path = ARTIFACTS / "analysis.ipynb"
        nbformat.write(nb, nb_path)
        print(f"  saved {nb_path.name}: {nb_path.stat().st_size} bytes with outputs")

        # ------------------------------------------------------------------
        section("2. Export to a script and compare")
        # ------------------------------------------------------------------
        default_body, _ = PythonExporter().from_notebook_node(nb)
        promptless_body, _ = PythonExporter(
            exclude_input_prompt=True, exclude_markdown=True
        ).from_notebook_node(nb)
        print(f"  default export:      {len(default_body.splitlines())} lines, "
              f"{len(default_body)} characters")
        print(f"  prompts stripped:    {len(promptless_body.splitlines())} lines, "
              f"{len(promptless_body)} characters")
        print(f"  '# In[' markers in default export: "
              f"{default_body.count('# In[')}")
        print(f"  '# In[' markers in stripped export: "
              f"{promptless_body.count('# In[')}")
        print(f"  occurrences of the printed value in the default export: "
              f"{default_body.count('slab correction')}")
        print("  Observation: the converter keeps the code and the Markdown")
        print("  (as comments) and discards every output. A script is therefore a")
        print("  *rerun* of the analysis, never a transcript of it.")

        # ------------------------------------------------------------------
        section("3. Magics do not survive")
        # ------------------------------------------------------------------
        n_magic = default_body.count("get_ipython()")
        print(f"  'get_ipython()' calls in the exported script: {n_magic}")
        print(f"  the rewritten line: "
              f"{[l.strip() for l in default_body.splitlines() if 'run_line_magic' in l]}")
        script_path = ARTIFACTS / "analysis_from_notebook.py"
        script_path.write_text(default_body, encoding="utf-8")
        result = subprocess.run([PY, str(script_path)], capture_output=True, text=True)
        print(f"  running that script: exit code {result.returncode}")
        print(f"  first stderr line: "
              f"{result.stderr.strip().splitlines()[-1] if result.stderr else 'none'}")
        print(f"  stdout produced before the failure: {result.stdout.strip()!r}")

        cleaned = "\n".join(
            line for line in default_body.splitlines()
            if "get_ipython()" not in line
        )
        clean_path = ARTIFACTS / "analysis_cleaned.py"
        clean_path.write_text(cleaned, encoding="utf-8")
        result2 = subprocess.run([PY, str(clean_path)], capture_output=True, text=True)
        print(f"  after deleting the magic line: exit code {result2.returncode}")
        print(f"  script stdout matches the notebook stdout exactly: "
              f"{result2.stdout == notebook_stdout}")
        print("  Observation: a notebook that runs perfectly can export to a")
        print("  script that cannot start. Magics, shell escapes and the display")
        print("  protocol are notebook-level features and the converter cannot")
        print("  translate them into anything a plain interpreter understands.")

        # ------------------------------------------------------------------
        section("4. The percent format as a first-class module")
        # ------------------------------------------------------------------
        percent_lines = []
        for cell in nb.cells:
            if cell.cell_type == "markdown":
                continue
            body = "\n".join(l for l in cell.source.splitlines()
                             if not l.strip().startswith("%"))
            percent_lines.append("# %%")
            percent_lines.append(body)
        percent_path = ARTIFACTS / "analysis_percent.py"
        percent_path.write_text("\n\n".join(percent_lines) + "\n", encoding="utf-8")
        result3 = subprocess.run([PY, str(percent_path)], capture_output=True, text=True)
        print(f"  '# %%' cell markers written: "
              f"{percent_path.read_text().count('# %%')}")
        print(f"  exit code: {result3.returncode}")
        print(f"  stdout matches the notebook: {result3.stdout == notebook_stdout}")
        print("  Observation: the percent format is plain Python -- no tool is")
        print("  needed to run, import, lint, debug or test it -- and it still")
        print("  carries the cell boundaries that a notebook editor needs. It is")
        print("  the format that keeps both audiences served.")

        # ------------------------------------------------------------------
        section("5. The command line equivalent")
        # ------------------------------------------------------------------
        script_cli = subprocess.run(
            [PY, "-m", "nbconvert", "--to", "script", "--output",
             "analysis_script", str(nb_path)],
            capture_output=True, text=True, cwd=str(ARTIFACTS),
        )
        produced_script = sorted(ARTIFACTS.glob("analysis_script.*"))
        print(f"  '--to script'  exit code: {script_cli.returncode}; "
              f"wrote {[p.name for p in produced_script]}")
        py_cli = subprocess.run(
            [PY, "-m", "nbconvert", "--to", "python", "--output",
             "analysis_python", str(nb_path)],
            capture_output=True, text=True, cwd=str(ARTIFACTS),
        )
        produced_py = sorted(ARTIFACTS.glob("analysis_python.*"))
        print(f"  '--to python'  exit code: {py_cli.returncode}; "
              f"wrote {[p.name for p in produced_py]}")
        if produced_py:
            ran = subprocess.run([PY, str(produced_py[0])],
                                 capture_output=True, text=True)
            print(f"  running the CLI-produced .py: exit code {ran.returncode} "
                  f"({ran.stderr.strip().splitlines()[-1] if ran.stderr.strip() else 'no stderr'})")
        print("  Observation: in nbconvert 7.17.2 '--to script' names its output")
        print("  '.txt' while '--to python' names it '.py' -- the same content,")
        print("  different extension. If a build step globs for '*.py' it will")
        print("  silently find nothing.")

        html = subprocess.run(
            [PY, "-m", "nbconvert", "--to", "html", "--output",
             "analysis_report", str(nb_path)],
            capture_output=True, text=True, cwd=str(ARTIFACTS),
        )
        html_file = ARTIFACTS / "analysis_report.html"
        print(f"  '--to html'    exit code: {html.returncode}")
        if html_file.exists():
            text = html_file.read_text()
            print(f"  produced {html_file.name}: {html_file.stat().st_size} bytes")
            expected_line = notebook_stdout.strip().splitlines()[0]
            print(f"  contains the notebook stdout line '{expected_line}': "
                  f"{expected_line in text}")
            print(f"  contains the LaTeX source '2\\pi G\\rho h' verbatim: "
                  f"{'2\\pi G\\rho h' in text}")
            print(f"  '<span class=\"math' wrappers (server-side rendering): "
                  f"{text.count('class=\"math')}")
        print("  Observation: the HTML export embeds the outputs and passes the")
        print("  LaTeX through untouched for MathJax to typeset in the browser.")
        print("  It is a report, not a script, and it is the only artefact a")
        print("  non-Python reader can open directly.")

        # ------------------------------------------------------------------
        section("6. An executed notebook as a regression test")
        # ------------------------------------------------------------------
        nb_ok = build_notebook()
        run(nb_ok, [range(len(nb_ok.cells))])
        nb_bad = build_notebook()
        nb_bad.cells[2].source = nb_bad.cells[2].source.replace("2670.0", "2900.0")
        nb_bad.cells[1].source = nb_bad.cells[1].source.replace("2670.0", "2900.0")
        run(nb_bad, [range(len(nb_bad.cells))])
        good = "".join(stream_text(c) for c in nb_ok.cells if c.cell_type == "code")
        bad = "".join(stream_text(c) for c in nb_bad.cells if c.cell_type == "code")
        print(f"  baseline rho = 2670 kg/m3 -> "
              f"{good.strip().splitlines()[0]}")
        print(f"  changed  rho = 2900 kg/m3 -> "
              f"{bad.strip().splitlines()[0]}")
        print(f"  stdout identical: {good == bad}")
        ratio_2670 = 2 * 3.14159 * 1e-5 * 2670.0 * 100.0
        print(f"  expected ratio of the corrections, 2900/2670 = "
              f"{2900.0 / 2670.0:.6f}")
        print("  Observation: 'execute the notebook and diff the outputs' is a")
        print("  real test -- cheap to write, hard to fool -- as long as the")
        print("  notebook is deterministic. It detects a unit change, a sign")
        print("  flip and a dropped correction; it cannot detect a formula that")
        print("  is wrong in the same way in both versions. Anything that must")
        print("  be *correct* rather than *unchanged* needs an assertion with a")
        print("  tolerance, i.e. pytest, not a diff.")
    finally:
        shutil.rmtree(ARTIFACTS, ignore_errors=True)


if __name__ == "__main__":
    main()
