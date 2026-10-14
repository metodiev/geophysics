# Exercises — 22-01-04 Documentation, Docstrings and READMEs That Work

Attempt these before reading the
[solutions](./04-documentation-solutions.md). The lesson is
[04 Documentation, Docstrings and READMEs That Work](../04-documentation.md).
Numbers refer to the **SYNTHETIC** simulation in
`code/documentation_demo.py`: 120 public functions, 15 % signature change per
release, 4 new functions per release, 55 % update rate, 8 releases.

## ★ Foundational

**★1.** At release 8 the demonstration reports 152 functions, 64.5 % documented
and 21.1 % stale. Compute the number of documented, stale and accurate functions,
and verify that the "accurate" percentage is consistent with the first two.

**★2.** Write a docstring for

```python
def depth_from_pressure(p, rho):
    return p / (rho * 9.81)
```

that states the unit of every argument, the unit of the result, and one failure
mode. Do not change the code.

**★3.** Put the following README sections in the order of §4 of the lesson and
state which audience each serves: *How to cite · Install · Licence · What this
code does · Data provenance · Quickstart · Known limitations*.

## ★★ Applied

**★★4.** Derive the model's long-run ratio $S/D$ for the fraction of documented
functions that are stale, given a signature-change probability $P$ and an update
probability $u$. Evaluate it for $u = 0.55$, and find the smallest $u$ for which
the long-run stale fraction of documented functions is below 10 %.

**★★5.** The demonstration estimates a reader cost of 38 minutes per team pass at
release 8, from 32 stale functions, 12 reader-minutes each and a 10 %
consultation fraction. Recompute the value if the consultation fraction is 30 %
and state how the number should be reported.

**★★6.** A repository's CI runs `pytest --doctest-modules`. State three classes of
documentation defect it catches and two it cannot, and give one concrete example
of each from a function that returns `np.diff(data, axis=0) / dt`.

## ★★★ Research-oriented

**★★★7.** Design a measurement of documentation decay in a real project: state
the population of functions, the operational definition of "stale", how you would
establish ground truth, and the two confounders. State what the demonstration's
$(1-u)/u$ limit would predict and how you would test it.

**★★★8.** Propose a documentation *test* beyond doctests that would catch a
changed **convention** — for example a switch of a difference scheme from forward
to central. State its false-positive mode and what it cannot check.

**★★★9.** A group must choose between two policies: (A) document every new
function and accept a 55 % update rate; (B) document only functions used outside
their own module and require a 95 % update rate. Using the $(1-u)/u$ limit,
compare the long-run stale fraction of the documented set under (A) and (B), and
state the measurement that would decide which policy produces fewer stale
docstrings *in total*.
