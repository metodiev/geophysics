# Exercises — 03-12-04 Verification vs Validation: Benchmarks and Convergence Tests

Attempt these **closed-book** before opening the
[solutions](./04-verification-and-validation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first:

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/verification_and_validation_demo.py
```

---

## ★ Foundational

**★1.** State the difference between verification and validation in one sentence
each, and give one example of each from the demonstration.

**★2.** Write down the manufactured solution and explain why it contains two
harmonics rather than one.

**★3.** State the three things that must accompany a measured order of accuracy,
and give the values the demonstration uses.

**★4.** Give the Richardson extrapolation formula, the assumption it rests on,
and the measured improvement it produced.

**★5.** State the GCI formula, the meaning of $F_s$, and what the resulting
number is (and is not).

---

## ★★ Applied

**★★6.** Reproduce the manufactured-solution convergence table with a single
harmonic and a nonlinear source term. Report the measured order and state
whether the leading-order coefficient changes.

**★★7.** Show that the measured GCI values 0.023007, 0.005787, 0.001464 fall by
a factor of 4 per doubling, as a second-order scheme requires.

**★★8.** The Green's-function validation reports a 2.05 % amplitude error at 30
cells per wavelength. Predict the error at 60 and 120 cells per wavelength if the
discrepancy is second-order discretisation, and state the test that would confirm
it.

**★★9.** Explain why the displacement reflection coefficient is
$(Z_1-Z_2)/(Z_1+Z_2)$ rather than its negative, using the free-end limit
$Z_2 \to 0$.

**★★10.** Design a manufactured solution for the diffusion equation, state the
order you expect, and state the norm you would use and why.

---

## ★★★ Research-oriented

**★★★11.** Perform the refinement study that ★★8 requires: measure the Green's
function peak error at four grid spacings, report the observed order, and state
whether the 2 % discrepancy is discretisation or a bug in the solver.

**★★★12.** Design a validation test for a solver that uses an *independent
numerical method* rather than an analytic result. State what makes the
comparison independent, and report the agreement and its uncertainty.

**★★★13.** Write a verification report for the 1-D solver of lesson 01,
following the seven-point checklist printed by the demonstration. Include one
failure and its resolution, and state the uncertainty on the final quantity of
interest.
