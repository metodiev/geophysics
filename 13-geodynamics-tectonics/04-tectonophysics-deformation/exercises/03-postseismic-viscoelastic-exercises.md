# Exercises — 13-04-03 Postseismic Relaxation and Viscoelastic Models

Attempt these before reading the
[solutions](03-postseismic-viscoelastic-solutions.md). The lesson is
[03 Postseismic Relaxation and Viscoelastic Models](../03-postseismic-viscoelastic.md).
All models and data in this module are **SYNTHETIC**.

Unless stated otherwise use $\mu_e = 30\ \mathrm{GPa}$ and
$1\ \mathrm{yr} = 3.1558\times10^{7}\ \mathrm{s}$.

## ★ Foundational

**★1.** Compute $\tau = \eta/\mu_e$ in seconds and in years for
$\eta = 3\times10^{19}$, $10^{20}$ and $3\times10^{20}\ \mathrm{Pa\,s}$ with
$\mu_e = 30\ \mathrm{GPa}$.

**★2.** Starting from $\dot e = \dot\sigma/(2\mu_e) + \sigma/(2\eta)$, derive
$\sigma(t) = \sigma_0 e^{-t/\tau}$ and state the value of $\tau$. Show explicitly
that $\tau$ does not depend on $\sigma_0$.

**★3.** A transient is fitted by $D(t) = 0.25 - 0.15e^{-t/12}$ m. Compute
$D(0)$, $D(12)$ and $D(60)$, and state the fraction of the total transient
completed at each time.

## ★★ Applied

**★★4.** For the same transient, compute the displacement rate at $t = 1$, $12$
and $60\ \mathrm{yr}$, and show that the rate halves every $\tau\ln 2$ years. By
what time has the rate fallen below $0.5\ \mathrm{mm\,yr^{-1}}$?

**★★5.** A campaign measures a transient with $3\ \mathrm{mm}$ noise per epoch
and wants $\tau$ to $\pm15\%$. Using the demonstration's short-window result as a
guide ($1.5\ \mathrm{yr}$ window on a $10.56\ \mathrm{yr}$ transient gave a
$13.4$–$23.6\ \mathrm{yr}$ range), estimate the window needed and state the
assumption in your extrapolation.

**★★6.** A two-layer response is
$D(t) = 0.09(1-e^{-t/10}) + 0.06(1-e^{-t/50})$ m. Evaluate it at
$t = 5, 20, 100\ \mathrm{yr}$ and estimate what a single-exponential fit over
$0$–$100\ \mathrm{yr}$ would return for $\tau$, arguing from the two modes'
contributions.

**★★7.** A published-style SYNTHETIC study reports $\eta = 10^{20}\
\mathrm{Pa\,s}$ from $\tau = 106\ \mathrm{yr}$ based on $20\ \mathrm{yr}$ of
data, with an rms residual of $2\ \mathrm{mm}$ against $3\ \mathrm{mm}$ noise.
State two reasons the residual does not validate the viscosity, and one
measurement that would.

## ★★★ Research-oriented

**★★★8.** Design a SYNTHETIC experiment to determine whether a layered viscosity
or a single viscosity fits a postseismic transient, specifying: the synthetic
data generator, the two forward models, the noise model, the model-selection
metric, and the layer contrast below which the two become indistinguishable. A
specification that could not be executed is a failed answer.

**★★★9.** Poroelastic rebound, afterslip and viscoelastic relaxation all produce
postseismic transients. For each, name the parameter that controls its timescale
and its expected spatial signature, then explain why a single exponential fitted
to a sum of all three can be extremely misleading even when the residual is
below the noise.
