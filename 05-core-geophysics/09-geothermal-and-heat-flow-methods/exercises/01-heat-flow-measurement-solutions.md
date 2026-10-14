# Solutions — 05-09-01 Measuring Terrestrial Heat Flow

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — The convention

Depth $z$ is positive **downward**; temperature increases downward and heat flows
upward. The reported heat flow is the upward **magnitude**:

$$q = +k\,\frac{\mathrm{d}T}{\mathrm{d}z}\ \ (z\ \text{downward}),
\qquad q = -k\,\frac{\mathrm{d}T}{\mathrm{d}z}\ \ (z\ \text{upward}).$$

Both are correct; mixing them within one report is not.

---

## ★2 — Heat flow

$q = 2.8 \times 22\ \mathrm{mW\,m^{-2}} = 61.6\ \mathrm{mW\,m^{-2}}$. The
multiplication is valid only because 22 K km⁻¹ has already been expressed as
22 × 10⁻³ K m⁻¹; without that conversion the arithmetic gives 61.6 W m⁻², which is
the flux at the surface of a star.

---

## ★3 — Equilibrium versus BHT

$T_{\text{eq}}$ is the formation temperature with no drilling disturbance; a BHT is
the temperature recorded during or shortly after drilling. In a conventionally
cooled hole the mud is cooler than the formation at depth, so **BHT < $T_{\text{eq}}$**
and a positive correction is needed. The correction is not a constant: it depends
on the elapsed time, the circulation history and the hole's thermal properties.

---

## ★4 — The demonstration

**(a)**

| Depth (m) | $k$ (W m⁻¹ K⁻¹) | $\mathrm{d}T/\mathrm{d}z$ (K km⁻¹) | $q$ (mW m⁻²) |
|---|---|---|---|
| 499 | 1.50 | 40.00 | 60.0 |
| 501 | 3.00 | 20.00 | 60.0 |

The **gradient halves** across the contrast; the **flux is unchanged**. That is
steady-state flux continuity, and it is the first check on any heat-flow profile.

**(b)** 0.69 per cent at 120 h, 0.35 per cent at 240 h and 0.12 per cent at 720 h,
so the 1 per cent level is crossed at about **three days (≈ 72 h)**. Extrapolating
the table, 1 per cent lies between the 48 h value (1.71 per cent) and the 120 h value
(0.69 per cent).

**(c)** The bias is **negative** (the measured gradient is too small, so the
estimated heat flow is too low) because the mud is cooler than the formation at
depth: the disturbance reduces the temperature most at depth, flattening the
gradient. The sign therefore depends on the mud being cooler at depth than the
formation, which is the normal case in a drilled hole and can be reversed in a
stimulated or recently produced well.

---

## ★5 — A two-layer model

Gradients: $q/k_1 = 70/2.0 = 35.0$ K km⁻¹; $q/k_2 = 70/4.0 = 17.5$ K km⁻¹.

$T(800) = 12 + 800 \times 35.0\times10^{-3} = 12 + 28.0 = 40.0$ °C.

$T(2000) = 40.0 + 1200 \times 17.5\times10^{-3} = 40.0 + 21.0 = 61.0$ °C.

Note how the **conductive** layer (the one with higher $k$) has the *smaller*
gradient: the same flux through a better conductor needs less temperature drop. If
the two were interchanged the temperature at 2000 m would be
$12 + 800(17.5\times10^{-3}) + 1200(35.0\times10^{-3}) = 12 + 14 + 42 = 68$ °C —
a 7 K error, which is larger than most of the uncertainties being tracked.

---

## ★6 — Diffusion depth of a 10 per cent change

The perturbation is $\Delta T\,\mathrm{erfc}(z/(2\sqrt{\kappa t}))$; 10 per cent
means $\mathrm{erfc}(x) = 0.10 \Rightarrow x = 0.9062$, so
$z = 2(0.9062)\sqrt{\kappa t} = 1.8124\sqrt{\kappa t}$.

| Age | $\sqrt{\kappa t}$ | $z$ |
|---|---|---|
| 100 yr | $\sqrt{1.2\times10^{-6}\times3.156\times10^{9}} = 61.5$ m | 111.5 m |
| 1 ka | 194.6 m | 352.7 m |
| 10 ka | 615.4 m | 1115.4 m |

The square-root scaling (a factor of $\sqrt{10} = 3.16$ per decade of time) is the
whole basis of borehole palaeoclimatology: the top hundred metres records the last
century, the top kilometre the last ten millennia, and deeper than that the signal
is gone.

---

## ★7 — Inverting for a GST history

Method: parameterise the history as five step changes at stated times (e.g. 100,
300, 600, 1200, 3000 yr before present) with unknown amplitudes; forward-model the
profile with the erfc superposition; sample the posterior with Metropolis–Hastings
using a 0.02 K Gaussian likelihood.

Expected outcome: the amplitudes of the recent steps (100, 300 yr) are constrained
to a few tenths of a kelvin; the older steps are correlated and poorly constrained
(their posteriors are elongated along a degenerate direction); and the deepest part
of the profile carries essentially no information about any of them.

**Which intervals are resolved:** roughly the last few centuries to a millennium,
for signals of a few tenths of a kelvin. **Which are not:** everything older than a
few millennia, and any fine structure within the last century that the diffusion
has already smoothed. Report the marginal posteriors and the correlations, and say
which features the data *require* and which they merely *permit*.

---

## ★8 — Curvature from advection

Model: $k\,\mathrm{d}^2T/\mathrm{d}z^2 - \rho_f c_f v\,\mathrm{d}T/\mathrm{d}z = 0$
with $v$ the Darcy velocity (positive upward for discharge), giving an exponential
approach to a linear profile with a characteristic length $k/(\rho_f c_f v)$.

A curvature scale of a few hundred metres with $k = 2.5$ W m⁻¹ K⁻¹ and
$\rho_f c_f = 4.2\times10^{6}$ J m⁻³ K⁻¹ implies

$$v = \frac{k}{\rho_f c_f L} = \frac{2.5}{(4.2\times10^{6})(300)}
= 2.0\times10^{-9}\ \mathrm{m\,s^{-1}} \approx 6\ \mathrm{cm\,yr^{-1}} .$$

Within the range of real groundwater fluxes, which is why the model is plausible.

**The ambiguity:** a depth-dependent conductivity produces curvature of the same
sign and similar magnitude. The two are not separable from a temperature profile
alone. They are separated by (i) an independent conductivity profile from core or a
borehole conductivity tool, and (ii) a second hole, since advection is a
*geological* process with a lateral structure while a conductivity variation follows
lithology. Report both models and state which data would discriminate them.
