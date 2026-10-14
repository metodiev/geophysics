# Module 01-01 — Arithmetic and Numerical Reasoning

**Stages:** beginner → intermediate · **Prerequisites:** none

This module establishes the numerical habits that everything else depends on:
how to write numbers so their magnitude and precision are unambiguous, how to
reason about scale before computing, how units carry physical meaning, and where
the computer will silently betray you.

It is deliberately first. Nearly every mistake in later modules that looks like a
geophysics error turns out to be a units error, a precision error, or a
floating-point error.

## Learning objectives

By the end of this module you will be able to:

1. Write and read any physical quantity in scientific and engineering notation,
   and state the precision that a written value implies.
2. Perform an order-of-magnitude (Fermi) estimate before computing, and use it to
   detect arithmetic blunders.
3. Convert between SI and field-conventional units (mGal, Gal, nT, γ, Ω·m)
   correctly, and verify conversions by dimensional analysis.
4. Check any equation for dimensional homogeneity and use that check to catch
   algebra errors.
5. Explain floating-point representation, machine epsilon, and catastrophic
   cancellation, and predict where each causes trouble in geophysical code.
6. Distinguish absolute from relative error, and explain conditioning and
   numerical stability.

## Lessons

| # | Lesson | Level | Key idea |
|---|---|---|---|
| 01 | [Number Systems, Precision and Scientific Notation](./01-number-systems-and-precision.md) | beginner | Magnitude and precision must be visible in the notation |
| 02 | [Orders of Magnitude and Fermi Estimation in Earth Science](./02-orders-of-magnitude.md) | beginner | Estimate before you compute; the estimate is a check |
| 03 | [Units, SI Conventions and Dimensional Analysis](./03-units-and-dimensional-analysis.md) | beginner | Units carry physics; dimensions catch errors |
| 04 | [Floating-Point Representation, Round-Off and Catastrophic Cancellation](./04-floating-point.md) | intermediate | The computer represents a *finite* set of reals |
| 05 | [Absolute vs Relative Error, Conditioning and Stability](./05-error-and-conditioning.md) | intermediate | Error depends on the problem, not just the algorithm |

## Suggested path

**If you are new to numerical work:** all five lessons, in order, with the
exercises. This is roughly 8–12 hours of genuine work and it saves many times
that later.

**If you already write scientific Python:** attempt
[01-04](./04-floating-point.md) and [01-05](./05-error-and-conditioning.md)
exercises first. If you can do ★★9 in both without notes, skip to
[Module 01-02](../02-algebra/README.md).

**If you are an experienced practitioner:** read
[01-05](./05-error-and-conditioning.md) as a refresher on conditioning, which is
the conceptual bridge to
[18-inverse-problems](../../18-inverse-problems/README.md).

## Materials in this module

| Path | Contents |
|---|---|
| [`01-number-systems-and-precision.md`](./01-number-systems-and-precision.md) | Lesson 01 — the reference exemplar for lesson structure |
| [`exercises/01-number-systems-and-precision-exercises.md`](./exercises/01-number-systems-and-precision-exercises.md) | Ten graded exercises |
| [`exercises/01-number-systems-and-precision-solutions.md`](./exercises/01-number-systems-and-precision-solutions.md) | Full worked solutions with verified arithmetic |
| [`code/number_systems_demo.py`](./code/number_systems_demo.py) | Runnable demonstration of every numerical hazard discussed |

## Mastery checkpoint

Complete this without notes and without a calculator beyond arithmetic:

> A gravimeter with 0.01 mGal resolution records a −18.4 mGal anomaly over a
> target at 250 m depth. **(a)** Convert the anomaly to SI. **(b)** Estimate, by
> order of magnitude, the excess mass required. **(c)** Compute it precisely.
> **(d)** State your answer with defensible significant figures and justify the
> choice. **(e)** Explain what a reviewer would mean if they said your result
> suffered catastrophic cancellation.

A worked version of (a)–(d) appears in the
[solutions](./exercises/01-number-systems-and-precision-solutions.md) for
exercise ★7, from which you can check your method.

## Common pitfalls across this module

1. **Thinking precision is free.** It is bounded by the instrument, the survey
   design, and the physics — never by your calculator.
2. **Skipping the estimation step.** Without an order-of-magnitude check you
   cannot distinguish a correct answer from a mis-keyed one.
3. **Treating units as an afterthought.** Unit analysis is the cheapest error
   detector available.
4. **Assuming computers do real arithmetic.** They do finite-precision
   arithmetic on a discrete subset of the reals.

## Related modules

- [01-02 Algebra, Functions and Modelling](../02-algebra/README.md) — builds
  directly on this module.
- [01-13 Probability and Statistics Foundations](../13-probability-and-statistics-foundations/README.md) —
  the rigorous treatment of uncertainty that lesson 05 previews.
- [03-scientific-computing](../../03-scientific-computing/README.md) — the
  practical tools for applying these habits at scale.
