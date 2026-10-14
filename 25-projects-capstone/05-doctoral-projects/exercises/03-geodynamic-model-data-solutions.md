# Solutions — 25-05-03 Project: Geodynamic Model-Data Comparison

Reference solutions. Every number is printed by
[`code/geodynamic_model_demo.py`](../code/geodynamic_model_demo.py); all data are
**SYNTHETIC**.

## ★1. The half-space subsidence coefficient

For $T(z,t) = T_m\,\mathrm{erf}(z/2\sqrt{\kappa t})$ the temperature deficit integrated
over depth is

$$\int_0^\infty \bigl(T_m - T\bigr)\,dz = T_m\int_0^\infty
\mathrm{erfc}\Bigl(\frac{z}{2\sqrt{\kappa t}}\Bigr)dz
= T_m\,\frac{2\sqrt{\kappa t}}{\sqrt{\pi}} ,$$

using $\int_0^\infty\mathrm{erfc}(u)\,du = 1/\sqrt{\pi}$ with
$u = z/2\sqrt{\kappa t}$. Thermal contraction then gives

$$a = \frac{\rho_m\alpha}{\rho_m-\rho_w}\cdot 2T_m\sqrt{\frac{\kappa}{\pi}}
\sqrt{t_\text{Myr}}
= \frac{2\times3300\times3.0\times10^{-5}\times1300}{2270}
\times 5.642\times10^{-4}\times 5.6176\times10^{6}
= 359.5\ \mathrm{m\,Myr^{-1/2}},$$

matching the printed 359.4 (the last digit is rounding). The product that appears is

$$a \propto \alpha T_m\sqrt{\kappa}\cdot\frac{\rho_m}{\rho_m-\rho_w},$$

so $a$ determines $\alpha T_m$ **times** $\sqrt{\kappa}$ and the density ratio — never
$\alpha$ or $T_m$ separately.

## ★2. The plate-model saturation depth

As $t\to\infty$ every exponential vanishes, $T\to T_m z/L$, and
$\int_0^L(T_m - T)dz = T_m L/2$:

$$d_\text{sat} = \frac{\rho_m\alpha T_m (L/2)}{\rho_m-\rho_w}
= \frac{3300\times3.0\times10^{-5}\times1300\times47500}{2270}
= 2693.1\ \mathrm{m},$$

matching the printed 2693 m. This is the entire difference between the plate and
half-space models: the plate model has a finite saturation depth, the half-space
model has none, and the two curves are indistinguishable until the cooling front
reaches $L$, which happens at roughly $t \sim L^2/\kappa$ (here the departure becomes
visible from about 40 Myr).

## ★3. The heat-flow coefficient and the ratio to $a$

The surface gradient of the half-space solution is
$\partial T/\partial z|_{0} = T_m/\sqrt{\pi\kappa t}$, so

$$C = \frac{kT_m}{\sqrt{\pi\kappa t_\text{Myr}}}
= \frac{3.2\times1300}{\sqrt{\pi\times10^{-6}\times3.1557\times10^{13}}}
= \frac{4160}{9957} = 0.4178\ \mathrm{W\,m^{-2}} = 417.8\
\mathrm{mW\,m^{-2}\,Myr^{1/2}},$$

matching the print. Dividing the two coefficients:

$$\frac{a}{C} = \frac{2\rho_m\alpha T_m\sqrt{\kappa/\pi}\sqrt{t_\text{Myr}}}{\rho_m-\rho_w}
\cdot\frac{\sqrt{\pi\kappa t_\text{Myr}}}{kT_m}
= \frac{2\rho_m\alpha\kappa t_\text{Myr}}{(\rho_m-\rho_w)k}
= 860.2 ,$$

so the *ratio* of the two observables measures $\alpha\kappa/k$ (times known
constants). The three combinations available from this dataset are therefore

$$\alpha T_m\ \text{(from bathymetry)},\qquad
\frac{kT_m}{\sqrt{\kappa}}\ \text{(from heat flow)},\qquad
\frac{\alpha\kappa}{k}\ \text{(from their ratio)}.$$

Three combinations for four unknowns ($T_m$, $\alpha$, $k$, $\kappa$): **the data
cannot determine the physical constants individually** unless one of them is supplied
independently. That result is a conclusion of the project, not a caveat.

## ★4. Why the full-range fit is biased low

$$\frac{a_\text{fit}}{a_\text{theory}} = \frac{161.7}{359.4} = 0.450,$$

so the fitted rate is $45\%$ of the theoretical one. The two model curves:

| age (Myr) | half-space $359.4\sqrt{t}$ (m) | plate model (m) | difference (m) |
|---|---|---|---|
| 40 | 2273 | 2144 | $+129$ |
| 80 | 3214 | 2555 | $+659$ |
| 160 | 4546 | 2684 | $+1862$ |

The half-space curve must therefore be pulled down at old ages, and the only way to do
that with the form $d_0 + a\sqrt{t}$ is to reduce $a$ and raise $d_0$: the fitted
intercept is $3426$ m against a true $2500$ m, an excess of $926$ m, and the slope
falls to $45\%$ of its true value. **The bias in $a$ and the bias in $d_\text{ridge}$
are the same error seen twice** — which is exactly what the $-0.94$ correlation
between them states quantitatively.

## ★5. The residual pattern

Residuals are observed minus fitted. The three thirds average $-192$ m (2–55 Myr),
$+205$ m (55–107 Myr) and $-233$ m (107–160 Myr): the fitted curve lies **above** the
observations at both ends and **below** them in the middle. A line of the form
$d_0 + a\sqrt{t}$ cannot produce that pattern by chance; it is the signature of a
single straight line pivoting about the middle of the range to pass through data that
flatten. The physical feature responsible is the **saturation plateau** of the plate
model: from about 40 Myr the real seafloor stops deepening as fast as $\sqrt{t}$, and
a model without a base has no way to represent that.

The operational lesson: **the sign pattern of the residual is the evidence**, more
informative than its rms. A residual of the same amplitude with random signs would
mean noise; the same amplitude with a consistent three-part sign structure means
missing physics.

## ★6. Splitting the 2–39 Myr discrepancy into model and noise

$$359.4 - 323.8 = 35.6\ \mathrm{m\,Myr^{-1/2}}\ \text{total},$$
$$\underbrace{359.4 - 336.8 = 22.6}_{\text{model error (63\%)}},
\qquad
\underbrace{336.8 - 323.8 = 13.0}_{\text{noise (37\%)}} .$$

The model error is the larger component: even restricted to 2–39 Myr, the plate model's
own departure from $\sqrt{t}$ accounts for two thirds of the discrepancy between the
fitted rate and the theoretical half-space rate. The noisy estimate lies
$(359.4-323.8)/18.1 = 2.0\sigma$ below the theoretical coefficient — marginal at the
5% level.

Implication for the claim "the half-space model is valid to 40 Myr": it is defensible
only as *approximately* valid, and the honest statement is that inside 40 Myr the
model error (23 m/Myr$^{1/2}$, 6%) is comparable to the noise-driven uncertainty
(18 m/Myr$^{1/2}$, 5%), so a fit to a real 40 Myr dataset cannot distinguish the
plate model's curvature from measurement scatter. **Separating the two required the
noiseless run** — which is the reason the project specification demands it.

## ★7. The precision of $L$ versus the grid step

$$d_\text{sat}(95) = 2693.1\ \mathrm{m},\qquad
d_\text{sat}(94) = 2693.1\times\frac{94}{95} = 2664.7\ \mathrm{m},$$

a difference of $28.4$ m, against a bathymetry noise of $100$ m rms. So a 1 km change
in $L$ moves the predicted saturation depth by less than a third of the noise — the
grid step does **not** determine the precision of $L$.

What determines it is the curvature of the misfit surface. Evaluating
$\chi^2(L)$ on the grid and taking the interval where
$\chi^2 \le \chi^2_\text{min} + 1$ gives

$$L = 94.0\ \mathrm{km},\qquad 1\sigma:\ [92.0,\ 97.0]\ \mathrm{km},
\qquad \pm 2.5\ \mathrm{km},$$

which is the honest uncertainty. The grid step limits only the search. The
demonstration's own printed phrase "resolved to 1.0 km" is the grid step, and quoting
it as a resolution would be exactly the error this exercise is designed to catch.
Note also that $\pm 2.5$ km is a *statistical* interval for this noise level and this
age distribution; systematic errors (sediment loading, thermal rejuvenation, a
non-uniform $T_m$) are larger and must be reported separately.

## ★8. Where the heat-flow models diverge

| age (Myr) | half-space $C/\sqrt{t}$ | plate model | difference | detectable with 5% noise? |
|---|---|---|---|---|
| 10 | 132.1 | 132.1 | $+0.0$ | no |
| 50 | 59.1 | 59.5 | $+0.4$ ($1\%$) | no |
| 100 | 41.8 | 46.6 | $+4.8$ ($11\%$) | yes |
| 150 | 34.1 | 44.3 | $+10.2$ ($30\%$) | yes |

The observed values (124.5, 64.1 and 47.7 mW m$^{-2}$) are consistent with the plate
model within the 5% noise at all three ages; the half-space model is consistent at 10
and 50 Myr and inconsistent at 150 Myr.

The physics of the divergence is important because the sign is the opposite of the
depth comparison: the plate model predicts **higher** heat flow at old ages than the
half-space model, because holding the base at $T_m$ maintains a finite basal flux that
is conducted to the surface. The depth and heat-flow tests therefore fail in opposite
directions at old ages, and a model that reproduces both is constrained much more
strongly than one that reproduces either — the reason the plate model's $L$ agrees
between the two observables in §3 of the project.

## ★★★9. Separating $\alpha$ from $T_m$

**The problem.** The bathymetry determines $\alpha T_m$ (times $\sqrt{\kappa}$ and the
density ratio), the heat flow determines $kT_m/\sqrt{\kappa}$, and their ratio
determines $\alpha\kappa/k$. With four unknowns and three combinations, one independent
constraint is needed, and it must be chosen so that its sensitivity vector is not
parallel to the existing ones.

**Observables and what each measures.**

| observable | measures | why it is not parallel to the others |
|---|---|---|
| seafloor depth versus age | $\alpha T_m\sqrt{\kappa}\rho_m/(\rho_m-\rho_w)$ | thermal contraction of the whole column |
| surface heat flow versus age | $kT_m/\sqrt{\kappa}$ | the temperature *gradient* at the surface |
| seismic $V_p$/$V_s$ of mantle material, or a petrological thermobarometer | $T_m$ (or the temperature at which a phase transition occurs) | a *temperature* sensor, independent of $\alpha$, $k$, $\kappa$ |
| laboratory/ab-initio thermal expansivity of the relevant minerals | $\alpha(P,T)$ | an *expansion* sensor |
| mantle-convection scaling ($Ra$, $Nu$) or post-glacial uplift / geoid | $\alpha T_m$ in a different combination with viscosity | different physics, different kernel |
| electrical conductivity structure from magnetotellurics | $T(z)$ through the conductivity–temperature relation | another temperature sensor, different depth kernel |

**Why the Jacobians are not parallel.** Depth versus age contains
$\alpha\sqrt{\kappa}$; heat flow contains $k/\sqrt{\kappa}$; a seismic or
petrological temperature constraint contains neither, and the thermal-expansivity
constraint contains $\alpha$ with no $T_m$. The pair (depth, heat flow) spans a
two-dimensional subspace of the three-parameter space
$(\alpha T_m, kT_m/\sqrt{\kappa}, \alpha\kappa/k)$; adding a temperature measurement
removes the $\alpha$–$T_m$ degeneracy because it fixes one of the two factors
directly rather than their product. Formally, the smallest singular value of the
augmented Jacobian must grow by a factor of order
$\sqrt{1 + (\partial d/\partial T_m)^2/\sigma_d^2}$; if it does not, the new
observable is redundant and the splitting has not happened.

**Resolution to claim.**

- $\alpha T_m$: from the bathymetry, with the statistical uncertainty of ★7
  (a few per cent) and the systematic uncertainty from sediment correction and
  hotspot swells reported separately.
- $T_m$: from the seismic/petrological constraint, quoting the depth and lateral
  resolution of the probe (e.g. the resolution length of the tomographic model at
  the relevant depth), and propagating it as a *prior* rather than as a fixed value.
- $\alpha$: as a derived quantity from $\alpha T_m / T_m$, with the uncertainty
  dominated by the $T_m$ error — which is the honest statement of what is
  well and badly determined.

**The synthetic test that demonstrates the separation is real.**

1. **Two-truth test.** Generate datasets from two models with the same $\alpha T_m$
   but different $(\alpha, T_m)$ splits (e.g. $(\alpha, T_m) = (3.0\times10^{-5},
   1300)$ and $(3.9\times10^{-5}, 1000\ ^\circ\mathrm{C})$). If the joint inversion
   returns the same $\alpha T_m$ and correctly distinguishes the two $T_m$ values,
   the separation is real; if it returns the two model pairs interchangeably, the
   constraint has not removed the degeneracy.
2. **Jacobian/singular-value check.** Report the singular values of the augmented
   Jacobian with and without the temperature constraint. The claim "the degeneracy is
   gone" is equivalent to a stated increase in the smallest singular value, not to a
   smaller posterior width that could come from a tightened prior.
3. **Prior-sensitivity test.** Repeat the inversion with the temperature constraint
   weakened by a factor of two and then by four, and confirm that the recovered
   $\alpha T_m$ and $\alpha$ vary by less than the claimed uncertainties. A result
   that tracks the assumed $T_m$ prior is a re-parameterisation of the prior, not a
   measurement.
