# Solutions — 16-05-02 GCMs, Resolution and Parameterisation

> Read after attempting the exercises. Lesson:
> [02 GCMs, Resolution and Parameterisation](../02-gcms-and-parameterisation.md).

---

## ★1 — Numerical diffusivity

$$K_{\text{num}} = \tfrac12 u\,\Delta x\,(1-C)
= 0.5 \times 10 \times 2.5\times10^{4} \times 0.5
= 6.25\times10^{4}\ \mathrm{m^{2}\,s^{-1}}.$$

Units: $(\mathrm{m\,s^{-1}})(\mathrm{m}) = \mathrm{m^{2}\,s^{-1}}$, the unit of a
diffusivity; the factors $\tfrac12$ and $(1-C)$ are pure numbers. For comparison,
air's molecular diffusivity is of order $10^{-5}\ \mathrm{m^{2}\,s^{-1}}$, so the
scheme's smoothing exceeds it by about nine orders of magnitude.

---

## ★2 — Lapse rate and stability

$$\Gamma_d = \frac{g}{c_p}
= \frac{9.81\ \mathrm{m\,s^{-2}}}{1004\ \mathrm{J\,kg^{-1}\,K^{-1}}}
= 9.77\times10^{-3}\ \mathrm{K\,m^{-1}} = 9.77\ \mathrm{K\,km^{-1}}.$$

(The standard trick: $\mathrm{J\,kg^{-1}} = \mathrm{m^{2}\,s^{-2}}$, so
$\mathrm{m\,s^{-2}}/\mathrm{m^{2}\,s^{-2}} = \mathrm{m^{-1}}$.)

Column lapse:

$$\Gamma = \frac{300-250}{5} = 10.0\ \mathrm{K\,km^{-1}}.$$

Since $10.0 > 9.77$, the column is **superadiabatic**: it is statically
unstable, and a model without a convective parameterisation has no way to remove
the instability.

---

## ★3 — Effective resolution

Four grid spacings: $4 \times 12 = 48\ \mathrm{km}$. Features smaller than about
$48\ \mathrm{km}$ are not acceptably represented. At $\Delta x = 12\
\mathrm{km}$, convective clouds, individual convective plumes (order 1 km),
boundary-layer turbulence and most gravity waves remain sub-grid. The
largest convective systems (tens of kilometres) are only marginally resolved.

---

## ★4 — Verifying the measured variance growth

Variance growth expected from a diffusion coefficient $K$ over time $t$:

$$\Delta\mathrm{Var} = 2Kt = 2 \times 9765.6 \times 86400
= 1.6875\times10^{9}\ \mathrm{m^{2}} = 1687.5\ \mathrm{km^{2}}.$$

Measured growth:

$$8077.64 - 6391.55 = 1686.09\ \mathrm{km^{2}}.$$

Agreement:

$$\frac{|1687.5-1686.1|}{1687.5} = 8.3\times10^{-4} = 0.083\%.$$

The residual ($0.083\%$) is at the level expected from the leading-order modified
equation plus the finite spectral content of the Gaussian; the demonstration
reports a ratio of measured to analytic diffusivity of $1.000$ at all four
resolutions.

---

## ★5 — Convective adjustment by hand

$s_i = c_pT_i + gz_i$ with $T_i = 300 - 10.5z_i$ and $z_i = 0.25i\ \mathrm{km}$,
$i = 0,\dots,20$:

$$s_i = 1004(300-10.5z_i) + 9810z_i
= 301200 + (9810 - 10542)z_i = 301200 - 732\,z_i\ \mathrm{J\,kg^{-1}}.$$

The mean height of the 21 levels is

$$\bar z = \frac{0.25\,(0+1+\dots+20)}{21} = \frac{0.25 \times 210}{21}
= 2.5\ \mathrm{km},$$

so the uniform final $s$ is

$$\bar s = 301200 - 732 \times 2.5 = 301200 - 1830
= 299370\ \mathrm{J\,kg^{-1}}.$$

Recovering the temperature profile, $T(z) = (\bar s - gz)/c_p$:

$$T(z) = \frac{299370}{1004} - \frac{9810}{1004}z
= 298.18 - 9.77 z\ \mathrm{K}\quad (z\ \text{in km}).$$

The final lapse rate is exactly $g/c_p = 9.77\ \mathrm{K\,km^{-1}}$ and the
surface temperature is $298.18\ \mathrm{K}$. The demonstration's iterative
pairwise mixing gives $298.20\ \mathrm{K}$ with a measured lapse of
$9.78\ \mathrm{K\,km^{-1}}$: the two agree to the precision of the reported
profile, and the residual reflects the finite-difference estimate of the lapse
rate over a $250\ \mathrm{m}$ spacing.

---

## ★6 — Why two energy-conserving closures differ

Both schemes replace pairs of levels by a weighted average of their dry static
energies, and averaging preserves the sum $\sum_i s_i$ exactly; that is why both
conserve energy (the demonstration verifies conservation to a relative
$2.96\times10^{-16}$). They differ because the *half* scheme stops mixing before
the profile becomes neutral: it removes only part of each instability, so the
final state retains a small superadiabatic component (measured lapse
$9.91\ \mathrm{K\,km^{-1}}$ against $9.78\ \mathrm{K\,km^{-1}}$). Since the
surface is the level whose $s$ is reduced least when the mixing is incomplete, it
stays warmer ($298.54\ \mathrm{K}$ against $298.20\ \mathrm{K}$).

The $0.34\ \mathrm{K}$ difference is **structural uncertainty of the
parameterisation**: it is not numerical error (both schemes are converged), not
rounding, and not reducible by more grid points. It reflects a genuine choice in
how unresolved convection is represented.

---

## ★7 — Convergence test design

**Metric.** The $L_1$ or $L_2$ error between the numerical solution and an
analytic or highly resolved reference, evaluated at a fixed physical time, on a
common physical grid via interpolation.

**Sequence.** $\Delta x, \Delta x/2, \Delta x/4, \Delta x/8$, holding the
Courant number $C$ fixed by adjusting $\Delta t$ proportionally — otherwise the
error changes for two reasons at once and the test is uninterpretable.

**Expected slope.** First order: a log-log plot of error against $\Delta x$ has
slope $1$, because the leading truncation term is
$\tfrac12u\Delta x(1-C)\partial_x^{2}c$.

**A measured slope of 2** would indicate that a second-order-accurate
reconstruction (or an error-cancelling combination of steps) is at work, or
that the error is dominated by the time discretisation, or that the reference
solution is not accurate enough to resolve the differences. Each of those has a
different diagnostic; the first step is to refine further and see whether the
slope persists.

---

## ★8 — Critique of the "parameterisation-free" claim

A $1\ \mathrm{km}$ grid resolves features larger than about $4\ \mathrm{km}$.
Convective *plumes* (order $1\ \mathrm{km}$ or less), boundary-layer turbulence
(centimetres to hundreds of metres), cloud microphysics and droplet spectra
(centimetres to metres) and much of the gravity-wave spectrum (wavelengths under
$10\ \mathrm{km}$) remain sub-grid and must be parameterised. So the model is not
parameterisation-free; it has *fewer and different* parameterisations than a
$100\ \mathrm{km}$ model.

Two further points. First, as $\Delta x$ shrinks, the closure problem becomes
harder to formulate well, not easier: the resolved dynamics begin to overlap with
the scales the closure was calibrated for, and the "grey zone" at
$\Delta x \sim 1$–$4\ \mathrm{km}$ is a known source of structural error.
Second, effective resolution is four to seven spacings, not one, so the smallest
resolved feature is $4$–$7\ \mathrm{km}$, not $1\ \mathrm{km}$. The claim should
be restated as: "the model resolves scales down to a few kilometres and
parameterises everything below."
