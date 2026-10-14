# Exercises — 05-03-05 Validating Forward Codes Against Analytic Benchmarks

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** Distinguish verification from validation in one sentence each.

**★2.** State the six kinds of benchmark a suite should contain.

**★3.** Explain why "the test must be able to fail" is a requirement, and how
you demonstrate it.

---

## ★★ Applied

**★★4.** Design a benchmark for a magnetic forward code using the fact that a
uniformly magnetised sphere is exactly a dipole outside it. State the reference,
the test quantity, the tolerance, and the grid you would use.

**★★5.** A prism-versus-dipole comparison shows a relative difference of
$1.29\times10^{-1}$ at 200 m and $4.88\times10^{-4}$ at 3200 m. Is this a code
error or a modelling difference? State the experiment that decides, and the
expected result of that experiment.

**★★6.** A tolerance of $10^{-18}$ is proposed for a double-precision float
comparison. Explain why it is meaningless and propose a defensible value.

---

## ★★★ Research-oriented

**★★★7.** Build a four-test benchmark suite for the prism gravity code:
(a) closed form versus quadrature, (b) thin-sheet limit versus $2\pi G\rho t$,
(c) symmetry of the anomaly about a symmetric body, (d) manufactured-solution
order for a Poisson solver. For each, state the tolerance, run it, record the
measured number, and then inject a bug that each test should catch, confirming
that it does. Report which test catches which bug, and which bug no test caught.

**★★★8.** Write a validation report for a forward code you have written,
following the structure: purpose, equations, benchmarks, measured results with
tolerances, known limitations, and a statement of what the code has *not* been
validated for. Identify honestly at least two things your code could still be
wrong about despite passing every benchmark.
