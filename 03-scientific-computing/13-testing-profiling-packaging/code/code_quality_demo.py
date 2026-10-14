"""Static analysis with the standard library: a small, real AST linter.

Run:  python code_quality_demo.py
Requires: standard library only

``ruff``, ``black`` and ``mypy`` are the tools to use in a real project, and
none of them is installed in this offline environment. Rather than describe
them, this script builds the class of check they perform -- analysis of the
*source*, without executing it -- from ``ast``, and runs it on two things:

1. a deliberately defective snippet, where each check fires exactly once, and
2. this module's own ``code/`` directory, where the checks report real counts.

It then demonstrates two things a linter cannot do from a single file and a
type checker can: a call whose argument count cannot be right, and a
forward-referenced annotation that only resolves when the module is imported.

Nothing is written to disk; every check is a pure function of a string.
"""

from __future__ import annotations

import ast
import builtins
import dataclasses
import pathlib
import typing


def section(title: str) -> None:
    print(f"\n{'=' * 74}\n{title}\n{'=' * 74}")


# `dir(builtins)` is the right source. `dir(__builtins__)` looks equivalent
# and is not: `__builtins__` is a module in `__main__` but a *dict* inside an
# imported module, and `dir()` of a dict returns dict methods. Using it made
# this checker report `get` and `__init__` as shadowed builtins when the module
# was imported -- a false positive that only appeared in the test context.
BUILTINS = frozenset(dir(builtins)) | {
    "list", "dict", "set", "tuple", "sum", "min", "max", "id", "type", "len",
    "range", "float", "int", "str", "bytes", "open", "print", "input", "hash",
    "object", "filter", "map", "next", "all", "any", "abs", "round", "sorted",
}


# --------------------------------------------------------------------------
# The checks
# --------------------------------------------------------------------------

def check_float_equality(tree: ast.AST) -> list[str]:
    """`==` or `!=` against a float literal -- a defective numerical assertion."""
    problems = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Compare):
            continue
        if not any(isinstance(op, (ast.Eq, ast.NotEq)) for op in node.ops):
            continue
        operands = [node.left, *node.comparators]
        for operand in operands:
            if isinstance(operand, ast.Constant) and isinstance(operand.value, float):
                problems.append(f"line {node.lineno}: float equality against "
                                f"{operand.value!r}; use a tolerance")
    return problems


def check_mutable_defaults(tree: ast.AST) -> list[str]:
    problems = []
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        for default in (*node.args.defaults, *node.args.kw_defaults):
            if isinstance(default, (ast.List, ast.Dict, ast.Set)) or (
                isinstance(default, ast.Call)
                and isinstance(default.func, ast.Name)
                and default.func.id in {"list", "dict", "set"}
            ):
                problems.append(f"line {node.lineno}: mutable default in "
                                f"{node.name}() is shared between calls")
    return problems


def check_bare_except(tree: ast.AST) -> list[str]:
    problems = []
    for node in ast.walk(tree):
        if isinstance(node, ast.ExceptHandler) and node.type is None:
            problems.append(f"line {node.lineno}: bare `except:` swallows "
                            f"KeyboardInterrupt and SystemExit")
    return problems


def check_unused_imports(tree: ast.AST) -> list[str]:
    imported: dict[str, int] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                imported[(alias.asname or alias.name).split(".")[0]] = node.lineno
        elif isinstance(node, ast.ImportFrom):
            if node.module == "__future__":
                continue                 # a compiler directive, not a binding
            for alias in node.names:
                if alias.name != "*":
                    imported[alias.asname or alias.name] = node.lineno
    used = {n.id for n in ast.walk(tree) if isinstance(n, ast.Name)}
    used |= {n.attr for n in ast.walk(tree) if isinstance(n, ast.Attribute)}
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name):
            used.add(node.value.id)
    return [f"line {line}: import '{name}' is never used"
            for name, line in sorted(imported.items()) if name not in used]


def check_shadowed_builtins(tree: ast.AST) -> list[str]:
    problems = []
    for node in ast.walk(tree):
        targets = []
        if isinstance(node, ast.Assign):
            targets = node.targets
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            targets = [ast.Name(id=node.name)]
        elif isinstance(node, ast.arg):
            targets = [ast.Name(id=node.arg)]
        for target in targets:
            if isinstance(target, ast.Name) and target.id in BUILTINS:
                problems.append(f"shadows the builtin '{target.id}'")
    return problems


def check_long_lines(source: str, limit: int = 99) -> list[str]:
    return [f"line {i}: {len(line)} characters (limit {limit})"
            for i, line in enumerate(source.splitlines(), 1) if len(line) > limit]


def check_missing_return_annotation(tree: ast.AST) -> list[str]:
    problems = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.returns is None:
            problems.append(f"line {node.lineno}: {node.name}() has no return annotation")
    return problems


CHECKS = {
    "float-equality": check_float_equality,
    "mutable-default": check_mutable_defaults,
    "bare-except": check_bare_except,
    "unused-import": check_unused_imports,
    "shadowed-builtin": check_shadowed_builtins,
    "missing-return-annotation": check_missing_return_annotation,
}


def lint(source: str, name: str) -> dict[str, list[str]]:
    """Run every AST check on a source string. ``long-line`` is text-based."""
    try:
        tree = ast.parse(source, filename=name)
    except SyntaxError as exc:
        return {"syntax-error": [f"line {exc.lineno}: {exc.msg}"]}
    report = {key: fn(tree) for key, fn in CHECKS.items()}
    report["long-line"] = check_long_lines(source)
    return {k: v for k, v in report.items() if v}


# --------------------------------------------------------------------------
# Demonstration 1: a snippet where every check fires
# --------------------------------------------------------------------------

DEFECTIVE = '''\
import os
import json


def scale(values=[]):
    out = []
    for v in values:
        out.append(v * 2)
    return out


def ratio(a, b):
    try:
        result = a / b
    except:
        result = 0.0
    return result


def matches(x):
    return x == 0.1


sum = 4
'''

def demo_defective_snippet() -> None:
    section("1. Seven checks, one deliberately defective snippet")
    report = lint(DEFECTIVE, "snippet.py")
    total = 0
    for key in sorted(report):
        for message in report[key]:
            print(f"  [{key:>24}] {message}")
            total += 1
    print(f"\n  total findings: {total}")
    print("  Every finding is derived from the syntax tree; the snippet was")
    print("  never imported and no line of it ran. That is the whole idea of")
    print("  static analysis: defects that do not depend on execution.")
    print("  (This checker originally used `dir(__builtins__)`, which is a dict")
    print("   inside an imported module; it then reported the dict methods `get`")
    print("   and `__init__` as shadowed builtins. Same code, different result")
    print("   when imported rather than run -- see the source comment.)")
    print("  The nine findings are: 2 unused imports, 1 mutable default, 1 bare")
    print("  except, 1 float equality, 1 shadowed builtin, and 3 missing return")
    print("  annotations.")


# --------------------------------------------------------------------------
# Demonstration 2: run the linter over this module's own code/
# --------------------------------------------------------------------------

def demo_lint_real_files() -> None:
    section("2. The same checks over this module's own code/ directory")
    here = pathlib.Path(__file__).resolve().parent
    files = sorted(here.glob("*.py"))
    print(f"  {'file':>34} {'lines':>6} {'findings':>9}  first finding")
    grand_total = 0
    for path in files:
        source = path.read_text(encoding="utf-8")
        report = lint(source, path.name)
        total = sum(len(v) for v in report.values())
        grand_total += total
        first = next((m for key in sorted(report) for m in report[key]), "-")
        print(f"  {path.name:>34} {len(source.splitlines()):>6} {total:>9}  {first[:38]}")
    print(f"\n  findings across {len(files)} files: {grand_total}")
    print("  (fixing the long lines in a file reduces its count immediately; that")
    print("  is the point -- a format check is cheap, mechanical and unreviewable)")
    print("  A clean run here would be a *claim about this code*, not a proof of")
    print("  correctness: these seven checks are a tiny subset of what ruff knows")
    print("  (which itself reports syntax-level facts, not semantics), and none of")
    print("  them can tell you the free-air sign in survey_stats.py is wrong.")
    print("  Linters remove noise so that review can spend its attention on")
    print("  physics. They do not review the physics.")


# --------------------------------------------------------------------------
# Demonstration 3: syntax errors, and what only a type checker catches
# --------------------------------------------------------------------------

def demo_syntax_error() -> None:
    section("3. A syntax error is caught before anything runs")
    bad = "def f(x)\n    return x + 1\n"
    try:
        compile(bad, "bad.py", "exec")
    except SyntaxError as exc:
        print(f"  compile() raised SyntaxError: line {exc.lineno}: {exc.msg}")
    print("  compile() is the cheapest gate in existence: it costs microseconds")
    print("  and it rejects a whole class of broken commits. `python -m compileall`")
    print("  runs it over a tree; every CI system runs it implicitly on import.")


def demo_argument_count_check() -> None:
    section("4. A call with the wrong number of arguments -- caught statically")
    source = '''\
def bouguer_slab(dg_mgal, drho_kgm3):
    return dg_mgal / drho_kgm3


result = bouguer_slab(2.5)
'''
    tree = ast.parse(source)
    signatures: dict[str, ast.arguments] = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            signatures[node.name] = node.args
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        args = signatures.get(node.func.id)
        if args is None:
            continue
        n_positional_required = len(args.args) - len(args.defaults)
        n_positional_given = len(node.args)
        ok = n_positional_required <= n_positional_given <= len(args.args)
        if ok:
            verdict = "OK"
        else:
            verdict = (f"ERROR: expected {n_positional_required}.."
                       f"{len(args.args)}, got {n_positional_given}")
        print(f"  line {node.lineno}: {node.func.id}() with {n_positional_given} "
              f"positional argument(s) -> {verdict}")
    print("\n  This is exactly the class of error a type checker reports as")
    print("  'Missing positional argument', and exactly the class that a test")
    print("  which never calls this line cannot find. Note the difference from the")
    print("  linter: this check needs the *signature*, i.e. the interface, not just")
    print("  the shape of one function's body.")


# --------------------------------------------------------------------------
# Demonstration 5: annotations are data
# --------------------------------------------------------------------------

@dataclasses.dataclass
class GravityStation:
    """A station record -- annotations are readable at runtime."""

    name: str
    latitude_deg: float
    elevation_m: float
    observed_mgal: float
    tags: list[str] = dataclasses.field(default_factory=list)


class VelocityPick(typing.NamedTuple):
    offset_m: float
    time_s: float


def resolve(value: "GravityStation") -> float:
    """Return elevation; annotated with a forward reference on purpose."""
    return value.elevation_m


def demo_annotations() -> None:
    section("5. Annotations are runtime data, not decoration")
    print(f"  GravityStation.__annotations__ = "
          f"{', '.join(f'{k}: {v}' for k, v in GravityStation.__annotations__.items())}")
    fields = dataclasses.fields(GravityStation)
    print(f"  dataclasses.fields -> {len(fields)} fields: "
          f"{', '.join(f.name for f in fields)}")
    print(f"  resolve() raw annotation        = {resolve.__annotations__['value']!r} "
          f"(a string: a forward reference)")
    print(f"  typing.get_type_hints(resolve)  = "
          f"{typing.get_type_hints(resolve)['value']}")
    print(f"  VelocityPick._fields            = {VelocityPick._fields}")
    print("\n  A type checker is a program that reads these annotations plus the")
    print("  bodies and checks consistency without running anything. It rejects")
    print("  `GravityStation('A', 45.0, 'one hundred', 979000.0)` -- a string where")
    print("  a float is required -- at edit time. mypy is the tool; it is not")
    print("  installed here, but the annotations above are exactly what it reads.")


def main() -> int:
    demo_defective_snippet()
    demo_lint_real_files()
    demo_syntax_error()
    demo_argument_count_check()
    demo_annotations()
    section("Summary")
    print("Run these in this order and in CI: compileall (syntax), ruff (lint and")
    print("format), mypy (types), pytest (behaviour). Each is cheaper than the")
    print("next and each catches a class the next would otherwise have to.")
    print("`python -m pip install ruff mypy` needs a virtual environment on this")
    print("machine; see the packaging lesson for why.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
