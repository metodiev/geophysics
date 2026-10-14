#!/usr/bin/env python3
"""Project structure: path portability and import hygiene, SYNTHETIC.

Run with the project venv:

    /Users/miroslav/Documents/workspace/geophysics/.venv/bin/python project_structure_demo.py

Everything here is SYNTHETIC: the project tree and the file contents are generated
with chosen parameters, and the breakage model is arithmetic on that tree.  No real
repository is inspected.

Sections
--------
1. A generated project tree: files, data and outputs.
2. Path portability: which references break when the project moves.
3. Import hygiene: flat layout against a package layout, and shadowing risk.
4. A portability score, and the two changes that raise it most.
"""

import numpy as np

RNG = np.random.default_rng(20261014)

# --- SYNTHETIC project model (chosen, not measured) -------------------------
N_SCRIPTS = 60
N_DATA_FILES = 40
README_ITEMS = 8


def section(title):
    print(f"\n{'=' * 70}\n{title}\n{'=' * 70}")


def main():
    section("1. A generated project tree")
    print(f"SYNTHETIC project: {N_SCRIPTS} scripts, {N_DATA_FILES} data files, "
          f"{README_ITEMS} documented entry points (chosen)")
    print("  typical flat layout:")
    for line in ("project/", "  analysis.py", "  helper.py", "  plot_fig3.py",
                 "  data/catalogue.csv", "  data/model_v2_FINAL.npz",
                 "  results/", "  figures/"):
        print(f"    {line}")
    print("  -> a flat layout has no boundary between code, data and outputs, so")
    print("     every script's path assumptions are implicit")

    section("2. Path portability")
    refs = RNG.choice(["absolute", "relative", "cwd-dependent", "config"],
                      N_SCRIPTS, p=[0.25, 0.45, 0.20, 0.10])
    breaks_move = np.isin(refs, ["absolute", "cwd-dependent"]).sum()
    print("  reference kind | scripts | breaks if the project moves")
    for kind in ("absolute", "relative", "cwd-dependent", "config"):
        n = int((refs == kind).sum())
        breaks = kind in ("absolute", "cwd-dependent")
        print(f"  {kind:<14} | {n:>7d} | {'yes' if breaks else 'no'}")
    print(f"  scripts that break on a move = {breaks_move} of {N_SCRIPTS} "
          f"({100 * breaks_move / N_SCRIPTS:.0f} %)")
    print("  -> moving a project is the cheapest portability test there is, and it")
    print("     is free to run before publishing")

    section("3. Import hygiene")
    modules = [f"module_{i:03d}.py" for i in range(24)]
    flat_shadow = int(RNG.random() < 0.3)      # one name colliding with stdlib
    print(f"  flat layout: {len(modules)} modules in one directory")
    print(f"  name collisions with installed packages: "
          f"{1 if flat_shadow else 0} (chosen risk)")
    print("  package layout: src/<package>/<module>.py with an installed "
          "distribution")
    print("  consequences of the package layout:")
    for line in ("imports resolve from one place, not from the working directory",
                 "tests import the installed package, not the checkout",
                 "an accidental stdlib shadow cannot happen by file name alone"):
        print(f"    - {line}")

    section("4. A portability score, and what raises it")
    checks = {
        "paths are relative to the project root": 0.45,
        "data and outputs are separate from code": 0.80,
        "a package layout with one import root": 1.00,
        "configuration is a file, not a constant": 0.10,
        "the README names the entry points": 0.50,
    }
    print("  check                                      | coverage")
    for k, v in checks.items():
        print(f"  {k:<42} | {100 * v:>7.0f} %")
    score = float(np.mean(list(checks.values())))
    print(f"  portability score = mean coverage = {score:.3f}")
    worst = sorted(checks.items(), key=lambda kv: kv[1])[:2]
    print(f"  the two changes that raise it most: {worst[0][0]}, {worst[1][0]}")
    print("  -> a score is only useful if each item is a check someone can run;")
    print("     the two above are 'read a path from config' and 'relative paths'")


if __name__ == "__main__":
    main()
