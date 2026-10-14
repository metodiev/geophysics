# Exercises — 04-03-02 Stratigraphic Principles and Relative Dating

Attempt these **closed-book** before opening the
[solutions](./02-stratigraphic-principles-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/02-stratigraphic_principles_demo.py`](../code/02-stratigraphic_principles_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** Three events P, Q and R are related by the single observation that P
predates Q.

(a) List every total order consistent with the observation.
(b) State how many there are.
(c) Add the observation that R predates P and list the orders again.
(d) State, in one sentence, what a set of relations determines that a single
preferred order does not.

---

**★2.** Name the principle each observation instantiates:

(a) a sandstone bed lies above a shale;
(b) a dyke truncates bedding in a limestone;
(c) a granite contains a sandstone fragment;
(d) a graded bed has a sharp top and a coarse base;
(e) a fossil assemblage in one outcrop differs from that in another 40 km away.

---

**★3.** A dyke cuts units 1, 2 and 3, and is overlapped by unit 4.

(a) Bracket the dyke's age between two units.
(b) State what determines how sharp the bracket is.
(c) State whether the bracket is a date, and why.

---

## ★★ Applied

**★★4.** Five events A, B, C, D, E are related by

$$A \prec B, \quad B \prec C, \quad C \prec D, \quad D \prec B.$$

(a) Identify the cycle.
(b) State how many consistent total orders exist and why.
(c) Explain what a geologist should do next, and what the algorithm can and
cannot tell them.

---

**★★5.** Run
[`../code/02-stratigraphic_principles_demo.py`](../code/02-stratigraphic_principles_demo.py).

(a) Report how many events and how many relations the first section uses, and
how many consistent total orders exist.
(b) Report which positions are partially constrained and list the candidate
events for each.
(c) Report the output of the contradiction test and the solver's verdict.
(d) Explain why the number in (a) is a result rather than a failure.

---

**★★6.** Two sections record the first appearances of three taxa in the order

$$\text{Section 1}: \quad T1, T2, T3; \qquad
\text{Section 2}: \quad T1, T3, T2.$$

(a) Count the sequence violations for the ordering $T1, T2, T3$.
(b) Count them for the ordering $T1, T3, T2$.
(c) State which arrangement is the minimum-violation one and how many violations
it has.
(d) Explain why a third section that agrees with section 1 changes the count.

---

## ★★★ Research-oriented

**★★★7.** A correlation of six taxa across three sections gives a minimum of two
violations, and a leave-one-out test reports that removing one particular datum
reduces the minimum to zero.

(a) State what a non-zero minimum proves about the data set.
(b) Explain why the leave-one-out test is the right test rather than a prior
belief about which taxon is likely to be reworked.
(c) Propose four geological interpretations of the outlier and state the
observation that would distinguish each from the others.
(d) Construct a data set in which **two** data are simultaneously out of place,
and state what the leave-one-out test reports. Explain why the method's output
must then be interpreted with care.

---

**★★★8.** A taxon takes 2 Ma to migrate across a basin 500 km wide.

(a) Compute the average migration rate.
(b) A correlation places two sections 150 km apart; state the diachroneity that
the migration implies between their first-appearance datums.
(c) A stratigraphic interval in the basin accumulates at 20 cm/ka. Compute the
thickness that the diachroneity of (b) corresponds to, and compare it with a
typical correlation resolution of one biostratigraphic zone.
(d) State the condition under which a first-appearance datum may be treated as a
synchronous surface, and say what happens to a correlation built on it when that
condition fails.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
