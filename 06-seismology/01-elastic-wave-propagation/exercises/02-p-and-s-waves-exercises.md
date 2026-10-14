# Exercises — 06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation

Attempt these before reading the
[solutions](./02-p-and-s-waves-solutions.md). The lesson is
[02 P and S Waves](../02-p-and-s-waves.md) and the numbers are printed by
[`../code/p_s_waves_demo.py`](../code/p_s_waves_demo.py). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Show algebraically that
$$\frac{v_p}{v_s} = \sqrt{2 + \frac{\lambda}{\mu}}
= \sqrt{\frac{K}{\mu} + \frac{4}{3}}
= \sqrt{\frac{2(1-\nu)}{1-2\nu}},$$
and evaluate all three forms for the demonstration's base model
($v_p = 5610.84$, $v_s = 3333.33\ \mathrm{m\,s^{-1}}$).

**★2.** State which inequality each of the two classical lower bounds requires:
$v_p/v_s \ge \sqrt{2}$ and $v_p/v_s \ge 2/\sqrt{3}$. Give the numerical value of
each bound to six decimal places.

**★3.** For the weak-shear row of the demonstration ($\mu \to 0$), explain why
$v_p$ stays finite while $v_s \to 0$, and compute $v_p/v_s$ for
$\lambda = 25\ \mathrm{GPa}$, $\mu = 0.01\ \mathrm{GPa}$.

## ★★ Applied

**★★4.** The demonstration sweeps $\mu$ from $0.01$ to $60\ \mathrm{GPa}$ at fixed
$\lambda = 25\ \mathrm{GPa}$ and reports the ratio falling from $50.019996$ to
$1.554563$. Verify both endpoints from the formula, and state the limit the sweep
approaches as $\mu \to \infty$.

**★★5.** In the second sweep ($\mu = 30\ \mathrm{GPa}$ fixed) the ratio rises from
$1.154701$ at $\lambda = -20\ \mathrm{GPa}$ to $2.943920$ at
$\lambda = 200\ \mathrm{GPa}$. Compute the bulk modulus $K = \lambda + 2\mu/3$ at
both ends and explain, using the bound in ★2, why $\lambda = -20\ \mathrm{GPa}$ is
exactly the smallest admissible value for this $\mu$.

**★★6.** From the polarisation measurement, the P field gives
$|\nabla\cdot\mathbf u|/|\nabla\times\mathbf u| = 1.662\times10^{2}$ and the S
field $4.675\times10^{-3}$. Explain why these two numbers should be reciprocals
in the ideal limit, and compute what the leakage would be if the central
difference used a step four times larger. State whether you expect the leakage to
grow or shrink, and why.

## ★★★ Research-oriented

**★★★7.** A three-component stream sampled at $100\ \mathrm{Hz}$ for $400$
samples (4.00 s) with noise of $\sigma = 0.02$ of the peak gives recovered
polarisation angles of $0.4224^\circ$ (P), $0.9829^\circ$ (SV) and $0.1358^\circ$
(SH). Design an experiment that determines how the recovered angle scales with
the noise level. State the metric, the range of $\sigma$ you would use, and the
functional form you expect. A specification that could not be executed is a
failed answer.

**★★★8.** The $v_p/v_s$ ratio is often used as a lithology indicator. Starting
from $v_p/v_s = \sqrt{2(1-\nu)/(1-2\nu)}$, derive
$\nu = (2 - (v_p/v_s)^2)/(2 - 2(v_p/v_s)^2)$ and compute $\nu$ for the
demonstration's four rows. Then explain why an inferred Poisson ratio near $0.5$
is numerically fragile.

**★★★9.** The demonstration's final check compares the measured polarisation with
the injected one. Explain why this check would pass even if the injected
polarisation were wrong, and state what additional check would make it a genuine
test of the physics rather than of the bookkeeping.
