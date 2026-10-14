# Solutions — 24-03-04 Reproducible Research Practice

> Read after attempting. Numbers computed. Lesson:
> [04 Reproducible Research Practice](../04-reproducible-research-practice.md).

---

## ★1 — A reproducibility claim

> Given the archived code at commit `<hash>`, the pinned environment file
> `environment.yml`, the parameter file `params/baseline.yaml` and the seed
> $20261014$, the six quantities in Table 2 are reproduced to four significant
> digits by running `bash make.sh`.

The four inputs the claim names are **code, environment, parameters and seed**;
the fifth, implicit in the rounding, is the **tolerance**. Drop any one of them and
the claim becomes unfalsifiable: a reader cannot tell whether a difference means an
error or a different library version.

---

## ★2 — What two identical runs establish

They establish **repeatability**: the pipeline is deterministic and free of
thread-order dependence and unseeded randomness. They do not establish
reproducibility (no independent person or machine has run it) and they certainly do
not establish replicability (that requires new data). Identical reruns are also
insensitive to a systematic error in the code: if the implementation is wrong
twice, both runs agree and both are wrong. That is why an independent
implementation, or a check against an analytic special case, carries information
that a rerun cannot.

---

## ★3 — Digest computation and why rounding comes first

Rounded to three significant digits, $(1.0, 2.50, 3.125)$ becomes

$$(1.00,\ 2.50,\ 3.12).$$

The digest is the SHA-256 of those three float64 values written in bytes:

$$d = \operatorname{SHA256}\big(\text{bytes}(1.00, 2.50, 3.12)\big).$$

Rounding first is what makes the digest encode the *claim* rather than the bytes.
Unrounded, the digest would differ for differences far below the claimed tolerance —
for example a change of $10^{-12}$ in the third element — and every comparison
would fail for reasons that have nothing to do with reproducibility. The digest is
a test of agreement at the stated precision, and it is deliberately blind to
everything finer.

---

## ★4 — How $0.095\%$ changes the fourth significant digit

Take a reported value of $145.0$, which has four significant digits with a
resolution of $0.1$ in the last place, i.e. a relative resolution of

$$\frac{0.1}{145.0} = 6.9\times10^{-4} = 0.069\%.$$

A shift of $0.095\%$ is larger than $0.069\%$, so it moves the value by at least one
unit in the last reported place — for example to $145.1$. Nothing is wrong with the
computation; the number simply crossed a rounding boundary. The general rule: **the
sensitivity of the last reported digit is the resolution of that digit**, so the
smaller the relative change needed to flip it, the more digits a claim commits you
to.

---

## ★5 — Why the flip count is unstable

Whether a digit flips depends on the distance between each value and the nearest
rounding boundary, not only on the size of the perturbation. Two values perturbed
by exactly the same relative amount will flip differently if one sits at $145.049$
and the other at $145.001$: the first is $0.05$ from a boundary at the resolution of
$0.1$, the second is $0.05$ away in the other direction. The count of flipped digits
is therefore a random variable with a large variance even for a fixed perturbation.

**Implication for an exact-reproduction claim.** "We reproduced every number
exactly" is partly a statement about the rounding convention and about the
accidental distances of the numbers from boundaries. It is not evidence of a
higher-quality implementation than one that reports agreement to three digits. The
honest claim states the tolerance and, where relevant, how many values were within
it — not that none moved.

---

## ★6 — How many parameters must be specified?

Every parameter influences every reported value, and an unstated parameter with a
$1\%$ plausible range can move each value by up to about $0.3\%$ (the largest
measured relative change in the demonstration is $0.298\%$ for the elevation
correction). Four significant digits correspond to a relative resolution between
about $0.03\%$ and $0.1\%$ depending on the magnitude of the value (from ★4:
$0.069\%$ at $145.0$; at $999.9$ it is $0.01\%$).

Since one unstated parameter is enough to move several values by more than that
resolution, the Methods section must specify **all** of them to support four-digit
agreement. Reporting four digits with one parameter unstated is a claim the paper
cannot meet; the alternatives are to specify the parameter, or to report fewer
digits. Both are honest; only the first keeps the four digits.

---

## ★7 — Reproducibility check for a paper

**Request.** Code repository with a tagged version; the parameter files and seeds;
the raw data or a representative subset with a checksum; the environment
specification; and the command that regenerates the paper's main table.

**Order of attempts.** (1) Run the pipeline on the supplied subset and compare the
main table — cheapest, and it tests the code path. (2) Run on the full data if
available. (3) Reimplement one reported quantity from the Methods text alone, with
no code — the strongest test, because it does not use the authors' implementation.

**Tolerance.** Set it before running, in the units of the reported quantity, and
state it: for a velocity table, four significant digits; for a figure, a stated
relative difference in the plotted quantity. A tolerance chosen after seeing the
difference is not a test.

**Conclusions.**

- *Exact agreement.* The pipeline is deterministic and the claim holds at the
  stated precision. This says nothing about whether the method is right.
- *Agreement within tolerance.* The claim holds; report the tolerance and the
  largest observed difference, and check whether an environment difference is a
  plausible explanation before looking for a bug.
- *Disagreement.* Do not conclude misconduct. Record which quantity disagrees, by
  how much, and whether the disagreement is systematic (a scaled value implies a
  units or parameter error) or scattered (implies environment or seed). Contact the
  authors with the specific quantity and the command used, which is the fastest
  route to a resolution and the most useful possible contribution.

---

## ★8 — How much of a subfield is reproducible?

**Sampling.** All research articles in a stated window and set of venues that
include a data-availability statement with a repository link; sample them randomly
and report the flow from all articles to those with usable material, because that
flow is itself a headline result.

**Outcome.** A binary per paper: the main reported table or figure is reproduced to
two significant digits by an operator following only the archived material. Two
significant digits rather than four is a deliberate choice: it makes the target
achievable across environment differences while still being informative, and it
must be fixed before the study starts.

**Effort model.** Budget the operator's time explicitly — for example $2$ person-
days per paper for environment setup, $1$ day for the run, and $1$ day for
comparison and documentation — and report the realised median. The effort is the
reason the study cannot cover hundreds of papers, and reporting it converts the
sample size from an accident into a stated constraint.

**Two upward biases.** First, availability: papers with archived material are the
ones whose authors expected to be checked, and they are systematically better
documented than the rest, so the measured rate is an upper bound for the literature.
Second, operator expertise: an experienced operator recovers a pipeline that a
reader would abandon, and the study uses a small number of operators who learn
across papers. Mitigate the second by pre-registering the number of hours per paper
and treating exceeding it as a failure of the paper's packaging rather than of the
operator's skill, and report the failure count separately.
