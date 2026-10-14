# Exercises — 14-03-02 Archie's Law and Saturation Estimation

Attempt before the [solutions](./02-archie-and-saturation-solutions.md). Lesson:
[02 Archie's Law and Saturation Estimation](../02-archie-and-saturation.md).
All models are **SYNTHETIC** teaching values. Unless stated, use
$a = 1.00$, $m = 2.00$, $n = 2.00$.

## ★ Foundational

**★1.** For $\phi = 0.22$ compute the formation factor $F$ with $a = 1$,
$m = 2$. State the unit of $F$ and of each symbol in $F = a/\phi^{m}$.

**★2.** A synthetic sand has $\phi = 0.30$, $\rho_w = 1.50\ \Omega\,\mathrm{m}$.
Compute $\rho_0$ and then $S_w$ for a measured
$\rho_t = 30.0\ \Omega\,\mathrm{m}$. State the result with its assumptions.

**★3.** For $S_w = 0.60$ and $n = 2$, compute the resistivity index $I$ and say
whether a partially saturated rock is more or less resistive than the same rock
at $S_w = 1$.

## ★★ Applied

**★★4.** Write $S_w$ as a function of $(\rho_t, \rho_w, \phi, a, m, n)$ and show
by differentiation that
$\partial\ln S_w/\partial\ln\phi = -m/n$. Evaluate it for $m = 2$, $n = 2$ and
state what a $5\%$ porosity error does to the reported saturation.

**★★5.** In a synthetic shaly sand ($\phi = 0.28$, $\rho_w = 2.50\
\Omega\,\mathrm{m}$) with a clay surface conductance of
$\sigma_\text{clay} = 0.020\ \mathrm{S\,m^{-1}}$, the true water saturation is
$S_w = 0.50$. **(a)** Compute the measured $\rho_t$. **(b)** Compute the
saturation that Archie returns. **(c)** Find the value of
$\sigma_\text{clay}$ for which Archie would return exactly $S_w = 1.00$ at a true
$S_w = 0.50$, and interpret it.

**★★6.** A measured $\rho_t = 15.0\ \Omega\,\mathrm{m}$ in the same synthetic
rock ($\phi = 0.28$, $\rho_w = 2.50\ \Omega\,\mathrm{m}$) invertis to
$S_w > 1$. **(a)** Compute the value. **(b)** Compute the highest resistivity
that is physically admissible and the saturation it corresponds to. **(c)** State
two physical explanations and the measurement that would separate them.

**★★7.** Using the lesson's synthetic pore-fluid relation
$\rho_w = 2.00 + 0.60/C$ (with $C$ in $\mathrm{mol\,L^{-1}}$) and a fixed
measured $\rho_t = 50.0\ \Omega\,\mathrm{m}$ with $S_w = 0.7986$, reproduce the
$(\phi, C)$ pairs for $\phi = 0.24, 0.26, 0.28, 0.30$ and state which end of the
range the data exclude and why.

## ★★★ Research-oriented

**★★★8.** Starting from the parallel-conduction model
$\sigma_t = \phi^{m}S_w^{n}/(a\rho_w) + \sigma_\text{clay}$, derive the corrected
saturation estimator for a *known* $\sigma_\text{clay}$. **(a)** Give the
formula. **(b)** Show that it reduces to Archie when
$\sigma_\text{clay} = 0$. **(c)** Evaluate it for the case of ★5(a) and compare
with both the true value and the uncorrected Archie value. **(d)** Explain why
the correction is only as good as the calibration of $\sigma_\text{clay}$.

**★★★9.** Design a study to separate the saturation exponent $n$ from the
saturation $S_w$ in a field where only resistivity is available. **(a)** State
what additional measurement is unavoidable and why. **(b)** Specify the
experiment, the quantities held fixed, and the plot that yields $n$. **(c)** State
one reason a laboratory $n$ may not transfer to the field, and how you would
detect the failure from field data alone.
