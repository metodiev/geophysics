# Exercises — 06-08-05 Joint Inversion of Receiver Functions and Surface Waves

Attempt before the [solutions](./05-joint-inversion-rf-solutions.md). Lesson:
[05 Joint Inversion](../05-joint-inversion-rf.md). SYNTHETIC values.

## ★ Foundational

**★1.** Evaluate $\chi^{2}$ for a candidate with $\Delta t = 3.65\
\mathrm{s}$ against $\Delta t^{\text{obs}} = 3.60\ \mathrm{s}$,
$\sigma_t = 0.05\ \mathrm{s}$, and dispersion residuals $+0.02$, $-0.03\
\mathrm{km\,s^{-1}}$ with $\sigma_c = 0.02\ \mathrm{km\,s^{-1}}$.

**★2.** State why each residual is divided by its uncertainty.

## ★★ Applied

**★★3.** Show that the Love-wave dispersion relation tends to $b_1$ as
$\omega\to\infty$ and to $b_2$ as $\omega\to0$, by examining the tangent
argument and the right-hand side.

**★★4.** In the demonstration, the receiver function alone admits $H$ over
$16\ \mathrm{km}$, the dispersion alone over $2\ \mathrm{km}$, and the joint over
$1\ \mathrm{km}$. Explain what each number means and which data set does the
constraining.

**★★5.** A colleague halves $\sigma_c$ so that the dispersion dominates. What
happens to the receiver function's influence on the answer, and what must be
reported?

## ★★★ Research-oriented

**★★★6.** Design a numerical experiment that tests whether the two objectives'
null directions are nearly orthogonal for a given model. State the quantity you
would compute and what value would indicate that joint inversion cannot help.

**★★★7.** The demonstration's model has a single layer. Propose how the joint
objective would change for a two-layer crust, and predict one way in which the
recovered parameters would remain non-unique even after adding dispersion.
