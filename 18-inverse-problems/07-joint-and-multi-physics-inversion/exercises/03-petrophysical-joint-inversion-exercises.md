# Exercises — 18-07-03 Petrophysically Coupled Joint Inversion

Attempt these before reading the
[solutions](./03-petrophysical-joint-inversion-solutions.md). The lesson is
[03 Petrophysically Coupled Joint Inversion](../03-petrophysical-joint-inversion.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Write the normal-equation block structure for
$\Phi = \|G_1m_1-d_1\|^2 + \|G_2m_2-d_2\|^2 + \lambda_p\|m_2-am_1-b\|^2$,
stating which blocks are diagonal and which couple the two properties.

**★2.** With $\lambda_p = 0$ the two normal equations decouple. Show that adding
the coupling term modifies both diagonal blocks and adds off-diagonal blocks
$-\lambda_p a I$.

**★3.** A relation has been calibrated with $\sigma_p = 0.03$ in the units of the
property. State the value of $\lambda_p$ that makes the penalty statistically
consistent with that calibration, and explain the assumption you had to make.

## ★★ Applied

**★★4.** From the demonstration's true-relation sweep, report the optimal
$\lambda_p$, the error reduction in property 2, and the misfit rise in property 2
as a fraction of its stated noise level. State whether the trade is worth it and
on what criterion.

**★★5.** The deviation term has rms $0.1061$ and the error of property 2
plateaus at $0.0918$ as $\lambda_p\to\infty$. Explain the difference between the
two numbers and why the plateau is below the deviation rms.

## ★★ Applied

**★★6.** A colleague reports a joint inversion "constrained by rock physics"
with no misfit table. Write the two questions you would ask first, and for each
state the number you would expect to see in a well-reported study.

## ★★★ Research-oriented

**★★★7.** Design a coupled inversion in which the petrophysical relation is
*determined by wells* in the survey area but the coupling coefficient
$\lambda_p$ is chosen by a discrepancy criterion on the coupled property's
misfit. Specify how you would set $\lambda_p$, and what you would do if the
chosen value produced a misfit that could not be brought to the noise level.

**★★★8.** Clustering-based coupling estimates the relation from the models being
inverted. Construct a concrete scenario in which this is harmless and one in
which it is circular, and state the experiment that distinguishes them.
