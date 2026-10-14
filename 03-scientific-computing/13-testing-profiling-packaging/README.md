# Module 03-13 — Testing, Profiling, and Packaging

**Stages:** intermediate → advanced · **Prerequisites:**
[03-01-04 Functions, Scope, Modules and Packages](../01-python-fundamentals/04-functions-modules.md)
for the function-and-module model every test exercises,
[03-01-07 Errors, Exceptions and Debugging](../01-python-fundamentals/07-errors-and-debugging.md)
for `AssertionError` and `pytest.raises`, and
[01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../../01-mathematics/01-arithmetic/04-floating-point.md)
for the error model that makes a tolerance necessary and computable.

Code that produces a number is not yet evidence. This module is about the four
things that turn a script into evidence: **tests** that state what the numbers
must be, **profiles** that state where the time and the memory go, **static
checks** that remove the defects no test reaches, and an **environment** that
makes the whole thing re-runnable by somebody else. It ends with the two
collaboration mechanisms without which none of the rest propagates — git and
HTTP — because a result nobody can fetch and nobody can check is a result nobody
can use.

The module has four habits that distinguish it from a tools reference:

- **Every numeric claim is measured, including the ones that contradict the
  folklore.** The profiling lesson reports that `a*a` is *slower* than `a**2` in
  NumPy 2.x, that `np.sqrt` and `**0.5` are indistinguishable, that summing along
  axis 0 costs 7% rather than the factor of two to eight that cache reasoning
  predicts, and that changing the thread count changed nothing on this machine.
  The environments lesson reports that negative result as a result, with the
  caveat that attaches to it.
- **Tolerances are derived, never chosen.** Every test in the module says what
  justifies its tolerance: the discretisation error that was measured, the
  conditioning that was estimated, or the round-off bound $n u$. A tolerance
  without a derivation is a number somebody will loosen.
- **The tools are the worked example.** The coverage instrument is built from
  `sys.settrace`, the linter from `ast`, the profiler from `cProfile`,
  `tracemalloc` and a line-hit counter, and the FDSN client from a local
  `ThreadingHTTPServer`. Nothing is described that is not also implemented, and
  where a tool is absent (`ruff`, `mypy`, `line_profiler`, `memory_profiler`,
  `pip-tools`, `build`) the module says so and reconstructs the measurement
  instead of pretending.
- **Nothing needs the network.** Every demo runs offline, installs nothing,
  downloads nothing and publishes nothing. The one place a URL appears in an
  executed script is `http://127.0.0.1:9/...`, a deliberately dead loopback port
  used to show what a transport failure looks like.

## Learning objectives

By the end of this module you will be able to:

1. Design an approximate comparison whose tolerance is derived from the
   floating-point model and the conditioning of the computation, and state the
   acceptance band of `pytest.approx` and `numpy.testing.assert_allclose` from
   memory.
2. Verify a numerical routine against an independently derived analytic solution,
   measure an observed order of convergence, and explain why refining a step is
   not a monotone improvement.
3. Profile a mixed Python-and-NumPy workload, distinguish the counts that
   reproduce from the timings that do not, measure a peak allocation, and falsify
   a performance claim with a paired A/B benchmark.
4. Write a static check for a defect class that matters in numerical code, and say
   precisely what static analysis cannot establish.
5. Write a `pyproject.toml`, evaluate version specifiers, diagnose PEP 668, and
   audit a requirements declaration against an environment.
6. Audit what a git repository contains, demonstrate that a clone equals the
   committed tree, and explain why a commit hash is a citation and a dataset is
   not.
7. Consume an HTTP data service correctly: paginate to the server's total,
   cache with `ETag`, retry with backoff, honour `Retry-After`, and record the
   provenance of the payload you used.
8. Reduce an environment to a reviewable hash, state what a lock file pins and
   what it does not, and choose between `venv`, conda and a container with a
   reason.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [pytest: Tests, Fixtures, Parametrisation and Approximate Comparisons](./01-pytest-basics.md) | intermediate | Why `==` is not an assertion about physics; the exact bands of `approx` and `assert_allclose`; deriving a tolerance from conditioning |
| 02 | [Testing Numerical Code Against Analytic Solutions](./02-testing-scientific-code.md) | advanced | Verification against a closed form; measured orders 1.83 → 1.99; a refinement study whose error *grows*; quadrature against the shell theorem |
| 03 | [Profiling CPU and Memory](./03-profiling.md) | advanced | Counts versus seconds; the profiler's 76 ns per call; line hits from `sys.settrace`; five performance claims tested, three of them false as stated |
| 04 | [Linting, Formatting, Type Hints and Static Analysis](./04-code-quality.md) | intermediate | Seven AST checks over this module's own code; coverage as a weak signal in five measured scenarios; the sign error no linter can see |
| 05 | [Packaging and Distributing a Python Library](./05-packaging.md) | advanced | PEP 668 and the venv predicate; the four tables of `pyproject.toml`; specifiers evaluated; `RECORD` and wheel layout |
| 06 | [Git for Scientific Collaboration](./06-git-workflow.md) | intermediate | Content addressing as citation; 1012 tracked files and zero binaries; a clone is the commit; worktrees |
| 07 | [Consuming APIs and Web Services for Earth Data](./07-apis-and-web-data.md) | intermediate | A local FDSN-style server: 137 events in six pages, a 304 that saves 3729 bytes, a `Retry-After` honoured, and a payload digest |
| 08 | [Reproducible Environments](./08-reproducible-environment.md) | advanced | An environment fingerprint over 155 pins; reduction order in ulp; a **negative** thread-count result reported as one; lock files and what they cannot pin |

## Suggested path

Read 01 → 02 → 03 → 04 in order: the tolerance argument in 01 is the input to
the convergence argument in 02, the measurement protocol in 03 is 02's protocol
applied to time, and 04 is the layer that sits above all three. Then read 05 → 08
as the "make it re-runnable" arc (packaging, environments) and 06 → 07 as the
"make it fetchable and checkable" arc (git, HTTP). A reader who needs only one
thing: lesson 01 for the tolerance recipe, lesson 03 for the benchmark protocol,
lesson 08 for the environment fingerprint.

## How to run the demos

Everything runs offline with the project virtual environment. From the
repository root:

```bash
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/pytest_basics_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/analytic_solutions_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/profiling_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/benchmark_folklore_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/coverage_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/code_quality_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/packaging_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/git_workflow_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/apis_demo.py
.venv/bin/python 03-scientific-computing/13-testing-profiling-packaging/code/environments_demo.py
```

Two of these are genuine pytest suites — run them rather than the scripts:

```bash
.venv/bin/pytest 03-scientific-computing/13-testing-profiling-packaging/code/test_pytest_basics.py -q
.venv/bin/pytest 03-scientific-computing/13-testing-profiling-packaging/code/test_analytic_solutions.py -q
```

Measured in this environment, those report **22 passed, 1 xfailed** and
**13 passed** respectively; the `xfail` is the bitwise-equality expectation that
the arithmetic refutes, kept in the suite so nobody removes the tolerance that
replaces it.

Every script exits 0, writes nothing outside the module, and needs no network.
`benchmark_folklore_demo.py` takes about 20 seconds because it repeats each
experiment three times, which is the point of it.

## Code and companions

| directory | contents |
|---|---|
| `code/` | 14 Python files: the object under test (`geophys_tools.py`, `survey_stats.py`), two pytest suites, and ten demonstration scripts |
| `exercises/` | 16 files: an exercise set and a solution set for each of the eight lessons, difficulty-tagged ★ / ★★ / ★★★ |

The exercises are closed-book and refer back to the demos for their numbers;
the solutions quote measured values and state, for every derived result, the
arithmetic that produced it.

## What this module does not do

- **It does not publish anything.** No wheel is built, no index is contacted, no
  DOI is minted. The packaging lesson describes the sequence in prose and says so.
- **It does not run CI.** The GitHub Actions workflows appear as YAML in the
  lessons, described rather than executed; this repository has no workflow files
  and the module claims nothing about a run.
- **It does not contact a real data service.** The FDSN material is taught against
  a local mock server with the same protocol behaviour. No external endpoint was
  queried, and no claim is made about any archive's current content or limits.
- **It does not install the tools it discusses.** `ruff`, `mypy`, `line_profiler`,
  `memory_profiler`, `pip-tools` and `build` are absent from this environment; the
  module reconstructs their measurement class with the standard library and labels
  every description as documentation rather than as a measurement.

## Related modules

- [03-12 Numerical Simulation in Python](../12-numerical-simulation-python/README.md)
  — the solvers whose correctness this module's verification techniques test.
- [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md)
  — the wider treatment of reproducibility, workflow managers and research data
  management.
- [01-mathematics/01-arithmetic](../../01-mathematics/01-arithmetic/README.md)
  — floating point, error and conditioning, the theory behind every tolerance in
  this module.
- [03-02 NumPy](../02-numpy/README.md) — memory layout and vectorisation, the
  mechanisms behind the profiling measurements.

## Self-assessment checklist

- [ ] I can state the acceptance band of `pytest.approx(1e6)` and of
      `assert_allclose(1e-13, 0.0)` without running them. (§01)
- [ ] I can derive a tolerance from $u$ and an amplification factor I measured,
      and write the derivation in a comment. (§01)
- [ ] I can distinguish verification, solution verification and validation, and
      say which one a given test performs. (§02)
- [ ] I can compute an observed order of convergence and state its asymptotic
      range. (§02)
- [ ] I can explain why refining a step size can *increase* the error, from two
      competing terms. (§02)
- [ ] I can obtain deterministic per-line execution counts with the standard
      library alone. (§03)
- [ ] I can name a NumPy performance claim I used to repeat that measurement
      contradicted. (§03)
- [ ] I can say what a clean lint run does and does not claim, with a measured
      example of a defect that is lint-clean, type-clean and wrong. (§04)
- [ ] I can state what line coverage is genuinely good for, and give a measured
      scenario where 90.9% coverage passes over a 61.72 mGal error. (§04)
- [ ] I can explain PEP 668 and the venv predicate that the marker file does not
      decide. (§05)
- [ ] I can evaluate `~=2.5` against three candidate versions from memory. (§05)
- [ ] I can demonstrate that a clone equals the committed tree, and say why that
      makes "works on my machine" testable. (§06)
- [ ] I can paginate an FDSN-style service to its own total and explain what a
      first-page-only client gets wrong. (§07)
- [ ] I can record the provenance of a fetched payload in four items. (§07)
- [ ] I can say what a lock file pins and list three things it cannot. (§08)
- [ ] I can report a negative experimental result without over-claiming it. (§08)
