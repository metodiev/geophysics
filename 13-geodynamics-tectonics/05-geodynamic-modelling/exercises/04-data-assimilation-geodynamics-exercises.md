# Exercises — 13-05-04 Data Assimilation and Adjoint Geodynamics

Attempt these before reading the
[solutions](./04-data-assimilation-geodynamics-solutions.md). The lesson is
[04 Data Assimilation and Adjoint Geodynamics](../04-data-assimilation-geodynamics.md)
and its numbers come from
[`code/data_assimilation_geodynamics_demo.py`](../code/data_assimilation_geodynamics_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the adjoint of one explicit diffusion step
$\theta^{n+1} = \theta^n + \nu L\theta^n$ and explain why the adjoint
integration runs backwards in time.

**★2.** The measured singular values of the forward map are
$8.939\times10^{-1}$ (mode 1) and $9.229\times10^{-5}$ (mode 9). Compute the
ratio and state how many digits of a mode-9 amplitude survive a 0.1% noise level.

**★3.** For the misfit $J = \tfrac12\|M m - d\|^2$, write $\nabla J$ and explain
in one sentence why the transpose of $M$ is all that is required.

## ★★ Applied

**★★4.** The measured adjoint gradient differs from central finite differences
with $\epsilon = 10^{-7}$ by $5.727\times10^{-9}$ relative. Estimate the accuracy
of the difference quotient itself and state what the agreement therefore proves.

**★★5.** From the Picard spectrum of the lesson, state how many modes a noise
level of $10^{-2}$, $10^{-4}$ and $10^{-6}$ admits, and explain why increasing
the number of grid points does not change the answer.

**★★6.** The demonstration takes 0.0027 ms per forward application and 0.0116 ms
per forward-plus-adjoint pair. Compute the cost of a finite-difference gradient
for $p = 25$ and $p = 5000$ parameters, and state the break-even value of $p$
against the adjoint.

**★★7.** Two initial conditions differ by 16.7% and produce observables
differing by $1.3\times10^{-16}$. Explain in two sentences why this is a property
of the forward map and not of any inversion algorithm, and name the direction of
the difference.

## ★★★ Research-oriented

**★★★8.** An ensemble of 25 members reports a viscosity of $1.0\times10^{21}$ Pa s
with a standard deviation of $0.2\times10^{21}$. Using the lesson's measured
sampling error, estimate the uncertainty *of that uncertainty* and state what you
would report instead.

**★★★9.** Design an observation strategy that would remove one of the modes the
Picard plot shows as unrecoverable. State the observable, the reason it changes
the singular-value spectrum, and the cost.

**★★★10.** A study reports a "recovered initial condition" from a time-dependent
inverse problem with a figure showing structure at the grid scale. Write the
three questions you would ask, in order, and the answer to each that would make
the claim defensible.
