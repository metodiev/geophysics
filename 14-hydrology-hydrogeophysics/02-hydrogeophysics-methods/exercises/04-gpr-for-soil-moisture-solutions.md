# Solutions — 14-02-04 GPR for Soil Moisture and Water Table

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All soils are **SYNTHETIC**.

Lesson: [04 GPR for Soil Moisture and Water Table](../04-gpr-for-soil-moisture.md).

---

## ★1 — Permittivity, velocity and travel time

$$\sqrt{\varepsilon_{\text{eff}}} = (1-0.42)\sqrt{4.5} + 0.18\sqrt{81}
+ (0.42-0.18)(1) = 1.2304 + 1.62 + 0.24 = 3.0904,$$
$$\varepsilon_{\text{eff}} = 9.550, \qquad
v = \frac{0.299792458}{\sqrt{9.550}} = 0.09701\ \mathrm{m\,ns^{-1}},$$
$$\mathrm{TWT} = \frac{2 \times 1.2}{0.09701} = 24.74\ \mathrm{ns}.$$

A velocity of 0.097 m/ns is 9.7 cm/ns — typical of a moist soil and roughly
two-thirds of the dry value (0.14–0.16 m/ns).

---

## ★2 — Reflection coefficient and polarity

$$\varepsilon_2 = \left[(0.58)\sqrt{4.5} + 0.08\sqrt{81} + (0.34)\right]^{2}
= (1.2304 + 0.72 + 0.34)^{2} = (2.2904)^{2} = 5.246,$$
$$R = \frac{\sqrt{9.550} - \sqrt{5.246}}{\sqrt{9.550} + \sqrt{5.246}}
= \frac{3.0904 - 2.2904}{3.0904 + 2.2904} = \frac{0.8000}{5.3808} = +0.1487.$$

**Polarity in words:** positive — the wave passes from a *wetter* (higher
permittivity) medium into a *drier* one, so the reflection has the same polarity as
the incident pulse. Compare the lesson's water-table case, which is negative
because the wave enters a wetter medium. **The sign is the diagnostic**: a
downward increase in water content gives a reversed pulse, a downward decrease
gives an unreversed one.

---

## ★3 — What a single-offset profile determines

| quantity | determined by a single-offset profile? | why |
|---|---|---|
| (a) water content | **no**, not without a velocity | the travel time gives $v$ only if the reflector depth is known |
| (b) layer thickness | **no**, not without a velocity | same circularity |
| (c) pore-water salinity | **no** | salinity affects conductivity (attenuation), not directly the permittivity |
| (d) clay-bound water | **no** | it has $\varepsilon \approx 5$–6, not 81, and is undercounted |

The exercise's point is that a single-offset profile measures **travel times**, and
every hydrologically interesting quantity needs either a velocity (from multi-offset
or from a borehole tie) or a calibration. That is why the CMP analysis of ★★4
matters.

---

## ★★4 — CMP velocity and depth

Fit $t^2 = t_0^2 + x^2/v^2$ by least squares on $(x^2, t^2)$:

| $x$ (m) | 0.5 | 1.0 | 1.5 | 2.0 |
|---|---|---|---|---|
| $t$ (ns) | 41.2 | 43.0 | 46.4 | 51.4 |
| $t^2$ (ns²) | 1697.4 | 1849.0 | 2153.0 | 2642.0 |
| $x^2$ (m²) | 0.25 | 1.00 | 2.25 | 4.00 |

Fitted slope $= 253.7\ \mathrm{ns^2\,m^{-2}}$, so
$$v = \frac{1}{\sqrt{253.7}} = 0.06278\ \mathrm{m\,ns^{-1}},$$
and the intercept $t_0^2 = 1609.7\ \mathrm{ns^2}$ gives
$$t_0 = 40.12\ \mathrm{ns}, \qquad
d = \frac{v\,t_0}{2} = \frac{0.06278 \times 40.12}{2}
= 1.259\ \mathrm{m}.$$

With $1.3v$ instead:
$$d_{\text{wrong}} = \frac{1.3 \times 0.06278 \times 40.12}{2}
= 1.637\ \mathrm{m}, \qquad \text{error} = +30.0\%.$$

**A 30% velocity error is a 30% depth error**, exactly as $d = vt/2$ requires. The
CMP fit removes the assumption entirely: the fitted $v$ comes from the data's own
curvature, and the depth then follows from $t_0$. The only thing that would spoil
this is a reflector that is not flat or a soil whose velocity varies with depth —
both of which produce moveout that is not hyperbolic, which is why a residual
NMO curvature is itself a diagnostic.

---

## ★★5 — Attenuation, regime and penetration

With $\theta = 0.25$, $\phi = 0.40$: $\varepsilon_{\text{eff}} = 13.489$ (from ★1's
CRIM form with the same parameters, since $\theta$ and $\phi$ are unchanged).

**Loss tangent** $\sigma/(\omega\varepsilon)$:

| $f$ | $\omega\varepsilon$ (S m$^{-1}$) | loss tangent | regime |
|---|---|---|---|
| 100 MHz | $2\pi(10^{8})(13.489)(8.854 \times 10^{-12}) = 7.50 \times 10^{-2}$ | 0.533 | transition |
| 250 MHz | $1.876 \times 10^{-1}$ | 0.213 | transition |

**Attenuation from the exact lossy-dielectric formula** (the low-loss approximation
is not reliable at a loss tangent near 0.2–0.5, which is the point):

| $f$ | $\alpha$ (dB m$^{-1}$) | 60 dB depth (m) |
|---|---|---|
| 100 MHz | 17.25 | 3.48 |
| 250 MHz | 17.72 | 3.39 |

**Does lowering the frequency help?** Barely: 3.48 m against 3.39 m, a 2.7%
improvement for a factor of 2.5 loss of resolution. This is the lesson's
frequency-independence result appearing in a real number: at a loss tangent of
0.2–0.5 the attenuation is still close to the frequency-independent low-loss value
$(\sigma/2)\sqrt{\mu_0/\varepsilon} = 0.02 \times 161 \times 8.686/\ldots$, and the
frequency dependence only becomes strong when the loss tangent exceeds about 1.
**Choose the frequency for resolution, not for penetration, unless the loss tangent
is above 1** — and if it is, the ground is usually too conductive for radar anyway.

---

## ★★6 — Calibration bias

| location | CRIM | gravimetric | bias |
|---|---|---|---|
| 1 | 0.17 | 0.22 | $+0.05$ |
| 2 | 0.05 | 0.09 | $+0.04$ |
| 3 | 0.13 | $0.18$ (predicted) | $+0.05$ |

**Form of the bias: constant (additive)**, about $+0.045$ in absolute water
content, not proportional. A proportional bias would give a constant *ratio*; here
the ratio at CRIM 0.05 is 1.8 and at 0.17 is 1.29, so the ratio is not constant and
the difference is.

**Third point:** a constant bias of $+0.045$ predicts a true value of
$0.13 + 0.045 = 0.175$ (approximately 0.18 given the scatter in the two
calibration points), so the calibration is
$\theta_{\text{true}} = \theta_{\text{CRIM}} + 0.045$ over this range.

**Why the relative error is worse at low water content.** The bias is fixed by the
amount of bound water (a property of the clay fraction), while the signal scales
with free water. So the *absolute* error is set by the clay and the *relative*
error is that absolute error divided by the free-water content — which becomes
large exactly where the free water is small, i.e. in the dry season, at the wilting
point, and near the top of a drying profile. **This matters hydrologically: the
driest part of the record is where a CRIM-only inversion is least trustworthy, and
it is also where the soil-moisture deficit (the quantity of interest for
infiltration) is defined.**

---

## ★★★7 — Survey design for $\pm 0.02$ over 2 m with
$\sigma = 0.03\ \mathrm{S\,m^{-1}}$

**Antenna frequency.** For a target at 2 m, the round-trip time in a soil of
$\varepsilon \approx 10$ is $2 \times 2/0.0948 = 42$ ns, so a 2 m profile needs a
time window of at least 60 ns with adequate resolution. At 250 MHz the wavelength
in the soil is $v/f = 0.0948/0.25 = 0.38$ m, giving a quarter-wavelength resolution
of 0.09 m — far better than needed. The binding constraint is **penetration and
signal-to-noise**, not resolution: with $\sigma = 0.03\ \mathrm{S\,m^{-1}}$ the
loss tangent at 250 MHz is
$\sigma/(\omega\varepsilon) = 0.03/(2\pi \times 2.5 \times 10^{8} \times
10 \times 8.854 \times 10^{-12}) = 0.216$, so from the lesson's table the
attenuation is of order 20–25 dB m$^{-1}$ at 250 MHz and **only about 2–3 m of soil
is reachable at the 60 dB convention.** A **250 MHz ground-coupled antenna** is
therefore the right choice, and a 100 MHz air-coupled system would buy almost no
extra depth (frequency-independence) at a large resolution cost.

**Geometry: CMP, not fixed-offset.** The quantity to be determined is a velocity
(hence water content), and a fixed-offset profile cannot determine it. A
**wide-angle reflection (CMP) gather every 10 m along the line**, with separations
from 0.25 to 3 m, gives the NMO velocity at each station with the fit of
[$t^2 = t_0^2 + x^2/v^2$](../04-gpr-for-soil-moisture.md). Between the CMP stations,
a fixed-offset profile interpolates the travel time at the local velocity.

**Calibration programme.** Five gravimetric samples across the water-content range
(dry to wet), each co-located with a CMP station, with replicate rings at each
point. From ★★6 the bias form (additive or multiplicative) is established
empirically; the calibration is then applied as an offset or a factor, not as an
assumption.

**Error budget for $\theta$.**

| source | magnitude | effect on $\theta$ |
|---|---|---|
| travel-time picking (0.2 ns on 42 ns) | 0.5% | $\delta v/v = 0.5\%$ → $\delta\varepsilon/\varepsilon = 1\%$ → $\delta\theta \approx 0.003$ |
| CMP velocity fit | 2–3% | $\delta\theta \approx 0.006$–0.010 |
| gravimetric calibration | $\pm 0.006$ absolute | 0.006 |
| porosity assumption ($\pm 0.03$ in $\phi$) | | 0.007 (from [14-02-01 ★★4](01-ert-for-hydrology-solutions.md)'s CRIM sensitivity) |
| clay-bound water (uncalibrated) | up to 0.04 | the dominant term |
| Combined (calibrated) | | $\approx 0.013$ |

So $\pm 0.02$ is achievable **provided the clay-bound-water bias is calibrated**;
without that calibration the error is $\pm 0.05$ and the survey fails its own
specification. That is the single most important design conclusion.

**Site condition that makes it impossible.** A **saline** profile: with
$\sigma = 0.3\ \mathrm{S\,m^{-1}}$ (brackish pore water) the loss tangent at
250 MHz is 2.16, the attenuation is over 100 dB m$^{-1}$, and the 60 dB depth is
0.5 m — the 2 m target is unreachable at any frequency that resolves it. The
alternative is **surface NMR** ([05](../05-nmr-for-groundwater.md)), which is
insensitive to conductivity and responds to water directly: its resolution is
poorer in depth (the kernel's width grows in proportion to its depth) but it does
not fail on conductivity. Computed support: at 250 MHz with $\sigma = 0.3$, the
one-way loss over 2 m is $2 \times 100 = 200$ dB, which is 40 dB beyond any
practical dynamic range.

---

## ★★★8 — Time-lapse: a travel-time increase with no amplitude change

**(a) Water-content change.** The two-way time to a shallow reflector at fixed
depth in a single layer scales as $\sqrt{\varepsilon}$, so an 8% increase in
travel time is a

$$(1.08)^{2} = 1.166 \ \text{factor in } \varepsilon_{\text{eff}},
\text{ i.e. } +16.6\%.$$

At $\phi = 0.40$, CRIM requires $\sqrt{\varepsilon} = (0.6)\sqrt{4.5} +
\theta(9-1) + 0.4$, so
$$\theta_2 - \theta_1 = \frac{\sqrt{1.166\,\varepsilon_1} - \sqrt{\varepsilon_1}}{8}.$$
If the initial water content were 0.10 ($\varepsilon_1 = 6.115$, $\sqrt{} = 2.473$),
then $\sqrt{\varepsilon_2} = 2.473\sqrt{1.166} = 2.670$ and
$$\theta_2 = \frac{2.670 - 0.6(2.1213) - 0.4}{8} = \frac{2.670 - 1.6728}{8}
= 0.1246.$$
So the inferred change is $\theta: 0.10 \to 0.125$, i.e. $+0.025$ — a modest but
hydrologically meaningful wetting, and consistent with an autumn rewetting of the
upper layer.

**(b) What cannot explain it.**

- **Temperature.** A temperature change alters the *dielectric* permittivity of
  water only weakly (about $-0.4\%$ per K near $20\ ^\circ$C, so a 10 K change moves
  $\varepsilon_w$ from 81 to about 78, changing $\sqrt{\varepsilon_{\text{eff}}}$
  by roughly $0.1\%$ of the water term). The travel time effect is two orders of
  magnitude smaller than the observed 8%. **A temperature change cannot explain a
  travel-time change of this size.**
- **Salinity** raises the conductivity and therefore the **attenuation**, but leaves
  the permittivity of the pore water almost unchanged (dissolved ions do not
  contribute to the orientational polarisation at radar frequencies). So salinity
  *can* change amplitudes and cannot change travel time — the **opposite** of the
  observation. In this dataset the amplitudes are unchanged anyway, which is
  further evidence against a salinity change.

**(c) The additional measurement and the confirming arithmetic.** The ambiguity
that remains is between added water and a changed porosity or clay content at
constant water content (both change the permittivity). The measurement that
resolves it is a **co-located point sensor or gravimetric sample**: if the water
content rose from 0.10 to 0.125 by gravimetry, the GPR interpretation is confirmed
directly; if the gravimetric content is unchanged at 0.10, then the permittivity
change must come from something else, most plausibly a **shrink–swell or structural
change in the soil** altering $\phi$ rather than $\theta$.

The confirming arithmetic: for pure water-content change,
$$\Delta\theta = \Delta\sqrt{\varepsilon}/8 = (2.670 - 2.473)/8 = 0.0246,$$
whereas for a pure **porosity** change at constant $\theta$,
$\sqrt{\varepsilon} = (1-\phi)\sqrt{4.5} + \theta\cdot 9 + (\phi - \theta)$ gives
$\partial\sqrt{\varepsilon}/\partial\phi = 1 - \sqrt{4.5} = -1.121$, so

$$\Delta\phi = \frac{\Delta\sqrt{\varepsilon}}{1 - \sqrt{4.5}}
= \frac{0.197}{-1.121} = -0.176.$$

A **17.6-point porosity decrease** would be needed to explain the same travel-time
change with no change in water content — physically implausible for a soil that is
wetting, and a decisive number. **The travel time is therefore measuring water, and
the porosity explanation is excluded by arithmetic, not by opinion.**
