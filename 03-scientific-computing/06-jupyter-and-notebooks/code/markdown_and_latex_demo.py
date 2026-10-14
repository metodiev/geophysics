"""Markdown and LaTeX in notebooks: what is stored, what renders, what breaks.

Run:  .venv/bin/python 03-scientific-computing/06-jupyter-and-notebooks/code/markdown_and_latex_demo.py
Requires: nbformat, nbconvert, sympy.

Companion to lesson 03-06-02.

Part 1  a notebook of prose and mathematics, and what nbformat stores verbatim.
Part 2  the delimiter-balance check this repository runs on its Markdown,
        applied to notebook Markdown cells -- including why fenced code has to
        be stripped first.
Part 3  generating LaTeX from SymPy instead of typing it by hand.
Part 4  what an HTML export actually contains: mathematics is left for MathJax.
"""

from __future__ import annotations

import re
import shutil
from pathlib import Path

import nbformat
import sympy as sp
from nbconvert.filters import markdown2html

ARTIFACTS = Path(__file__).resolve().parent / ".demo-artifacts"
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


def _strip_code(text: str) -> list[str]:
    """Blank out fenced code blocks -- the same job tools/check_all.py does."""
    out: list[str] = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return out


def math_report(text: str, strip_code: bool) -> tuple[int, int, bool]:
    """Return (display delimiters, inline span parity ok, all spans)."""
    lines = _strip_code(text) if strip_code else text.splitlines()
    doubled = sum(line.count("$$") for line in lines)
    open_at = None
    for index, line in enumerate(lines, start=1):
        residue = line.replace("$$", "")
        count = residue.count("$") - residue.count(r"\$")
        if count % 2 == 1:
            open_at = index if open_at is None else None
    return doubled, open_at is None, doubled % 2 == 0


def main() -> None:
    ARTIFACTS.mkdir(exist_ok=True)
    try:
        # ------------------------------------------------------------------
        section("1. A prose cell, and what nbformat stores")
        # ------------------------------------------------------------------
        prose = (
            "## Gravity anomaly of a point mass\n"
            "\n"
            "The vertical attraction at horizontal offset $x$ and depth $z$ is\n"
            "\n"
            "$$g_z = \\frac{G M z}{(x^2 + z^2)^{3/2}}$$\n"
            "\n"
            "| symbol | meaning | SI unit |\n"
            "|---|---|---|\n"
            "| $G$ | gravitational constant | m³ kg⁻¹ s⁻² |\n"
            "| $M$ | anomalous mass | kg |\n"
            "| $g_z$ | vertical attraction | m s⁻² |\n"
            "\n"
            "At $x = 0$ this reduces to $GM/z^2$, the result used in every\n"
            "feasibility calculation. Do not write `$` for currency: `USD 5`.\n"
        )
        nb = nbformat.v4.new_notebook(
            cells=[nbformat.v4.new_markdown_cell(prose)]
        )
        cell = nb.cells[0]
        print(f"  markdown cell source length: {len(cell.source)} characters, "
              f"{len(cell.source.splitlines())} lines")
        print(f"  round-trips through nbformat unchanged: "
              f"{nbformat.reads(nbformat.writes(nb), as_version=4).cells[0].source == cell.source}")
        print(f"  '$' characters in the source: {cell.source.count('$')}")
        print(f"  '$$' occurrences: {cell.source.count('$$')} "
              f"(display math spans: {cell.source.count('$$') // 2})")
        print(f"  pipe-table rows (lines starting with '|'): "
              f"{sum(l.startswith('|') for l in cell.source.splitlines())}")
        print("  Observation: a notebook is JSON. Nothing is rendered at save")
        print("  time -- the source is stored character for character, so a")
        print("  broken delimiter is persisted, not repaired.")

        # ------------------------------------------------------------------
        section("2. The delimiter-balance check, with and without code stripped")
        # ------------------------------------------------------------------
        tricky = (
            "Inline $g_z$ and a display span:\n"
            "\n"
            "$$\\nabla^2 V = 0 \\qquad (r > 0)$$\n"
            "\n"
            "```python\n"
            "price_usd = 12.50  # a '$' in code is not mathematics\n"
            "print(f'{price_usd:.2f}')\n"
            "```\n"
            "\n"
            "And a second inline span, $\\mu = 4\\pi\\times10^{-7}$ H m⁻¹.\n"
        )
        with_code = math_report(tricky, strip_code=False)
        without = math_report(tricky, strip_code=True)
        print(f"  raw text:      '$$' count = {with_code[0]}, "
              f"even = {with_code[2]}, inline balance ok = {with_code[1]}")
        print(f"  code stripped: '$$' count = {without[0]}, "
              f"even = {without[2]}, inline balance ok = {without[1]}")
        print(f"  unescaped '$' inside the fenced block: {tricky.count('$', tricky.index('```')) - 2}")
        print("  Observation: the raw count sees an odd number of single '$'")
        print("  because the dollar sign inside the code fence is not a")
        print("  delimiter. That is why tools/check_all.py blanks fenced blocks")
        print("  before counting -- otherwise every listing that shows a shell")
        print("  prompt or a price would be reported as a broken formula.")

        # ------------------------------------------------------------------
        section("3. Write formulas by generating them, not typing them")
        # ------------------------------------------------------------------
        G, M, x, y, z, r, t, f = sp.symbols("G M x y z r t f")
        potential = -G * M / r
        r_of_xyz = sp.sqrt(x**2 + y**2 + z**2)
        gz = sp.simplify(-sp.diff(potential.subs(r, r_of_xyz), z))
        print(f"  potential V(r)        -> {sp.latex(potential)}")
        print(f"  dV/dr partial         -> {sp.latex(sp.diff(potential, r))}")
        print(f"  vertical attraction   -> {sp.latex(gz)}")
        print(f"  g_z at y = 0          -> {sp.latex(sp.simplify(gz.subs(y, 0)))}")
        ricker = (1 - 2 * sp.pi**2 * f**2 * t**2) * sp.exp(-sp.pi**2 * f**2 * t**2)
        print(f"  Ricker wavelet        -> {sp.latex(ricker)}")
        barometric = sp.exp(-z / sp.Symbol("H", positive=True))
        print(f"  barometric factor     -> {sp.latex(barometric)}")
        kappa, T0 = sp.symbols("kappa T_0", positive=True)
        diffusion = sp.erfc(z / (2 * sp.sqrt(kappa * t)))
        print(f"  diffusion front       -> {sp.latex(diffusion)}")
        for name, expr in (("V", potential), ("Ricker", ricker), ("erfc", diffusion)):
            print(f"    {name:>7}: {len(sp.latex(expr)):>3} characters of LaTeX, "
                  f"{int(sp.count_ops(expr))} operations")
        print("  Observation: SymPy is the source of truth for the formula; the")
        print("  notebook cell only carries the result. A derivation that is")
        print("  generated cannot disagree with the code that implements it.")

        # ------------------------------------------------------------------
        section("4. What an HTML export contains")
        # ------------------------------------------------------------------
        html = markdown2html(nb.cells[0].source)
        print(f"  exported HTML length: {len(html)} characters")
        print(f"  '$' preserved: {html.count('$')} of {nb.cells[0].source.count('$')}")
        print(f"  '$$' preserved: {html.count('$$')} of 2")
        print(f"  '<table>' elements produced from the pipe table: {html.count('<table>')}")
        print(f"  '<td>' cells produced: {html.count('<td>')}")
        print("  Observation: the mathematics arrives in the HTML unchanged and")
        print("  is typeset in the browser by MathJax. The cost is that a PDF or")
        print("  a figure-only reader without MathJax sees the raw dollar signs.")
        path = ARTIFACTS / "prose_demo.md"
        path.write_text(nb.cells[0].source, encoding="utf-8")
        print(f"  wrote {path.name} for inspection: {path.stat().st_size} bytes")
    finally:
        shutil.rmtree(ARTIFACTS, ignore_errors=True)


if __name__ == "__main__":
    main()
