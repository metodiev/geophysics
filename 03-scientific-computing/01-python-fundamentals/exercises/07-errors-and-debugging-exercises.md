# Exercises — 03-01-07 Exceptions, Assertions and Systematic Debugging

Attempt these **closed-book** before opening the
[solutions](./07-errors-and-debugging-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/errors_debugging_demo.py`](../code/errors_debugging_demo.py) require you
to run it and report its **actual** output.

---

## ★ Foundational

**★1.** Classify each check as an **assertion** (about the model) or **validation**
(about the input), and say what happens to each under `python3 -O`.

(a) `assert 0 < vs < vp`
(b) `if rho <= 0: raise ValueError(...)`
(c) `assert 0 <= latitude <= 90`
(d) `if len(samples) == 0: raise ValueError(...)`
(e) `assert isclose(vp, expected, rel_tol=1e-12)`

---

**★2.** Write a `UnitError(ValueError)` whose message contains the parameter name,
the value, the *expected* unit and the unit that was inferred. Show two raises and
their exact messages.

---

**★3.** Which clause of `try` would you use for each, and why?

(a) write a header to a file that must exist before the computation;
(b) release a lock;
(c) return a parsed value only if no exception occurred;
(d) convert a `ZeroDivisionError` from a velocity of zero into a domain error.

---

## ★★ Applied

**★★4.** Run `python3 errors_debugging_demo.py` and report:

(a) the six density-validation lines;
(b) the `try`/`else`/`finally` output for both velocities;
(c) the traceback's frame list and the exception line.

Then answer: why does 8 100 kg m⁻³ *not* raise while 30 000 kg m⁻³ does, and what
is the physical basis for the 22 590 kg m⁻³ bound?

---

**★★5.** Run the demo and report the two totals and the skipped count from §4.

(a) Explain why both totals are 21.5 and why only one of them is trustworthy.
(b) Add a third input class — a physically impossible magnitude of 12.0 — and show
what each approach reports.
(c) State the one-line change that makes the silent version auditable.

---

**★★6.** The demo's §5 shows `anomaly(0, 0.5) = 8.000000e+00` where the caller
believed the depth was 500 m.

(a) Compute the correct value for a depth of 500 m and the ratio between the two.
(b) Explain why no `except` clause can catch this.
(c) Write the known-answer test that *does* catch it, in five lines.
(d) State the two naming changes that would have prevented it.

---

## ★★★ Research-oriented

**★★★7.** Write a validator for a layered velocity model:
a list of `(top_depth_km, vp_m_s, vs_m_s, density_kg_m3)` layers.

(a) Derive and state the physical bounds you will enforce for each field, with a
one-line justification for each bound.
(b) Implement it, raising one exception type that carries the layer index and the
field.
(c) Add the cross-field checks (depths strictly increasing; $v_p > v_s \sqrt{2}$ …
state the relation you actually use and why).
(d) Demonstrate it on one valid model and three invalid ones, printing the exact
messages.

---

**★★★8.** A pipeline reports "processed 999 412 of 1 000 000 rows".

(a) List four distinct mechanisms that could account for the missing 588 rows, and
say which is detectable from the inputs alone.
(b) For each, state whether the resulting statistic is biased, and in which
direction, or merely noisier.
(c) Write the audit line you would add so that the cause is visible in the log
without a re-run.

---

**★★★9.** Design the failure policy for ingesting a 10⁶-row catalogue with a 0.1
per cent defect rate.

(a) For each defect class (blank field, unparseable number, physically impossible
value, duplicate event ID, missing required column) decide: raise, skip and count,
repair, or warn.
(b) Justify each decision in terms of the *physics* and of what the catalogue will
be used for.
(c) State the threshold at which a skip-and-count policy must escalate to a
failure, and how you would set it.
