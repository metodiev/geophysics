# Exercises — 05-06-06 Documenting Processing: Reproducibility in Practice

Attempt these **closed-book** before opening the
[solutions](./06-processing-transparency-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Reference results from the lesson's measurement (three-step pipeline on a synthetic
200-station profile, despike window 5 at 4 sigma, level order 1, Gaussian low-pass
at a 400 m cutoff): re-running the same record gave an identical output hash and a
maximum difference of 0.000e+00; swapping the despike and level steps changed the
hash and produced an RMS difference of 0.007976 (1.027 % of the 0.7765 peak) while
both orders flagged 3 samples; a parameter written as `0.3` against `0.1 + 0.2`
differed by $5.551\times10^{-17}$ in value yet gave a bit-identical output.

---

## ★ Foundational

**★1.** Name the four levels of reproducibility and state which is the weakest
useful form.

---

**★2.** List the five components of a processing record (items 1–5 of the lesson's
Section 2.2) and say which one turns the record into a *claim*.

---

**★3.** State why a content hash must be accompanied by units and by the exact
representation that was hashed.

---

**★4.** Give the four ordering rules of Section 7 of the lesson, each with its
one-line justification.

---

**★5.** State the rule relating a verification tolerance to the data's noise level.

---

## ★★ Applied

**★★6.** A processed gravity grid has a measured noise level of 0.008 mGal and an
anomaly peak of 0.35 mGal. A colleague proposes a verification tolerance of
0.05 mGal.

(a) Is that tolerance acceptable? Justify with numbers.
(b) Propose a defensible tolerance.
(c) State what level of reproducibility each tolerance corresponds to.

---

**★★7.** A pipeline is documented as "despike, filter, level, grid" with parameters
for each.

(a) What is missing, and what is the measured consequence of that omission?
(b) Rewrite the documentation so that it is executable.
(c) State two outcomes of data-dependent steps that should be recorded.

---

**★★8.** A processing sequence includes a k-means classification used to define a
regional/residual split, and a bootstrap used to estimate an uncertainty.

(a) What must be recorded for each to be reproducible?
(b) Explain why a *different* result on a re-run is not necessarily a bug.
(c) State what verification is meaningful in this case.

---

**★★9.** Two analysts process the same raw gravity data. Analyst A levels with a
first-order polynomial fitted per line; analyst B uses a second-order polynomial
fitted to tie-line crossings. Their anomaly maps differ by up to 0.04 mGal over a
50 km area.

(a) Is this a reproducibility failure? Distinguish the two levels.
(b) What must each record so that the difference can be attributed?
(c) State which differences could be resolved by re-running and which cannot.

---

## ★★★ Research-oriented

**★★★10.** Construct a pipeline with at least five steps, in which at least two steps
are non-commuting and one step is stochastic. Produce its record, verify it by
re-execution, then deliberately omit one parameter and demonstrate that the omission
is detectable *only* through the hash. Report which of the lesson's items 1–8 of
Section 9 apply to your pipeline.

---

**★★★11.** Design and implement a verification harness that classifies a
re-execution into the four levels of Section 2.1 automatically: it reports
bit-identical, numerically equivalent (with tolerance), statistically equivalent
(against a noise level) and conceptually equivalent (the same derived quantity to
within its uncertainty). Demonstrate it on a pipeline whose parameter is perturbed in
small steps, and report the perturbation at which the classification changes.

---

**★★★12.** The lesson claims that thread-count dependence makes bit-identical
reproduction environment-specific. Design an experiment that tests this claim on the
machine you are using: run a large reduction (for example a stack of many traces, or
a matrix product) with varying thread counts, and compare the output hashes bit by
bit. Report the result honestly, including the case where no difference is found, and
state what that case does and does not establish.
