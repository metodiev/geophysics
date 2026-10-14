# Solutions — 07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [04 Gravity Reductions](../04-gravity-reduction.md).

---

## ★1 — Free-air corrections

$$\mathrm{FA} = 0.308555\ \mathrm{mGal\,m^{-1}} \times h.$$

| $h$ (m) | FA (mGal) | in units of 1 mGal |
|---|---|---|
| 250 | $77.1388$ | $77.14$ |
| 1500 | $462.8325$ | $462.83$ |
| 4000 | $1234.22$ | $1234.22$ |

Even a $250\ \mathrm{m}$ hill already produces a free-air term 77 times a
milligal, i.e. far larger than the anomalies that a near-surface survey targets.
This is why the correction is not optional and why its own accuracy (Section 2 of
the lesson) sets the achievable anomaly accuracy.

---

## ★2 — Bouguer slab at 1500 m

$$2\pi G\rho = 0.0419300\ \mathrm{mGal\,m^{-1}}\ \text{per }
\mathrm{g\,cm^{-3}} = 4.19300\times10^{-5}\ \rho\ [\mathrm{kg\,m^{-3}}]\
\mathrm{mGal\,m^{-1}}.$$

More directly, $2\pi G\rho h$ with $\rho$ in $\mathrm{kg\,m^{-3}}$:

| $\rho$ ($\mathrm{kg\,m^{-3}}$) | $2\pi G\rho$ (mGal/m) | $h = 1500$ m (mGal) |
|---|---|---|
| 2200 | $0.0922589$ | $138.388$ |
| 2670 | $0.111969$ | $167.953$ |
| 3000 | $0.125808$ | $188.711$ |

**Difference between extremes:** $188.711 - 138.388 = 50.323\ \mathrm{mGal}$,
which is $50.323/462.833 = 10.87\%$ of the free-air term at the same elevation.
A density uncertainty of $\pm400\ \mathrm{kg\,m^{-3}}$ therefore moves a
$1500\ \mathrm{m}$ Bouguer anomaly by about $50\ \mathrm{mGal}$ — an order of
magnitude more than most targets.

---

## ★3 — The three gradients at $45^\circ$

$$\frac{\mathrm{d}g_{\text{obs}}}{\mathrm{d}h}
= -\frac{\mathrm{d}\gamma}{\mathrm{d}h} + 2\pi G\rho
= -0.308555 + 0.111969 = -0.196586\ \mathrm{mGal\,m^{-1}},$$

$$\frac{\mathrm{d}(\text{free-air anomaly})}{\mathrm{d}h}
= +2\pi G\rho = +0.111969\ \mathrm{mGal\,m^{-1}},$$

$$\frac{\mathrm{d}(\text{simple Bouguer anomaly})}{\mathrm{d}h}
= -\frac{\mathrm{d}\gamma}{\mathrm{d}h} + 2\pi G\rho
+ \frac{\mathrm{d}\gamma}{\mathrm{d}h} - 2\pi G\rho = 0.000000\
\mathrm{mGal\,m^{-1}}.$$

**Why the third is zero.** The simple Bouguer anomaly adds back the free-air term
and subtracts the slab term, and those two are exactly the two contributions that
make observed gravity depend on elevation over a uniform surface. What remains is
the deviation of the real Earth from that model, which is the interpretable part.
The *observed* field's $-0.196586\ \mathrm{mGal\,m^{-1}}$ belongs to the data, not
to the anomaly, and misquoting it as the anomaly's gradient is the error Section 5
of the lesson measures.

---

## ★★4 — Terrain corrections for $H = 100$ m, $R = 500$ m, $\rho = 2400\ \mathrm{kg\,m^{-3}}$

$$2\pi G\rho = 1.00646\times10^{-6}\ \mathrm{s^{-2}} = 0.100646\
\mathrm{mGal\,m^{-1}}.$$

$$\sqrt{R^{2}+H^{2}} = \sqrt{250000 + 10000} = \sqrt{260000} = 509.9019\
\mathrm{m}.$$

**(a) Hill, station at the centre of the top:**

$$T_{\text{hill}} = 0.100646 \times \left(509.9019 - 500\right)
= 0.100646 \times 9.9019 = 0.9966\ \mathrm{mGal}.$$

**(b) Valley, station on the floor:**

$$T_{\text{valley}} = 0.100646 \times \left(100 + 500 - 509.9019\right)
= 0.100646 \times 90.0981 = 9.0680\ \mathrm{mGal}.$$

**The factor:** $9.0680/0.9966 = 9.10$.

**Why.** In the hill case the extra mass is a ring-like body whose elements are at
horizontal distances comparable to the height, so the vertical component of each
element's attraction is reduced by the factor $z/\sqrt{s^{2}+z^{2}}$. In the valley
case the same volume of missing mass sits exactly beneath and around the station,
inside the slab that the Bouguer correction assumed to be there, so the vertical
component is close to full. The lesson's own example shows the same phenomenon at
$H = 60$, $R = 300$ m: $6.0529/0.6652 = 9.10$ — identical, because for
$H/R$ and the same geometry the ratio depends only on $H/R$ and not on the scale.

---

## ★★5 — A complete reduction and its two sensitivities

$\gamma(50^\circ) = 981\,070.2136\ \mathrm{mGal}$; free-air coefficient
$0.3085175\ \mathrm{mGal\,m^{-1}}$, so for $h = 2200$ m:

$$\mathrm{FA} = 0.3085175 \times 2200 = 678.7385\ \mathrm{mGal},$$

$$2\pi G\rho h = 0.1090332 \times 2200 = 239.8731\ \mathrm{mGal},$$

$$\Delta g_{B} = 980\,651.0000 - 981\,070.2136 + 678.7385 - 239.8731
= 19.6518\ \mathrm{mGal}.$$

**(a) Elevation error of $+10$ m.** Both the free-air and the Bouguer terms change;
the net coefficient is $0.3085175 - 0.1090332 = 0.1994843\
\mathrm{mGal\,m^{-1}}$, so

$$\Delta\left(\Delta g_{B}\right) = -0.1994843 \times 10 = -1.9948\
\mathrm{mGal}, \qquad \Delta g_{B} = 17.6570\ \mathrm{mGal}.$$

**(b) Density change to $\rho = 2300\ \mathrm{kg\,m^{-3}}$.** The slab coefficient
becomes $2\pi G \times 2300 = 0.0964526\ \mathrm{mGal\,m^{-1}}$ and the Bouguer
term is $212.196\ \mathrm{mGal}$ instead of $239.873$, so

$$\Delta g_{B} = 19.6518 + 239.8731 - 212.1957 = 47.3292\ \mathrm{mGal}.$$

A $300\ \mathrm{kg\,m^{-3}}$ density change shifts the anomaly by
$+27.68\ \mathrm{mGal}$, fourteen times the $2\ \mathrm{mGal}$ from a $10\ \mathrm{m}$
height error. The ranking in the lesson's error budget is reproduced here on a
different station: **density first, elevation second.**

---

## ★★6 — What the Nettleton bias costs

$\Delta(\Delta g) = -2\pi G\,\delta\rho\,h$, with $\delta\rho$ the density error.

| case | $\delta\rho$ ($\mathrm{kg\,m^{-3}}$) | error at $h = 600$ m (mGal) |
|---|---|---|
| uncorrelated geology | $+25$ | $-0.6290$ |
| correlated geology | $+125$ | $-3.1452$ |

($-2\pi G \times 25 \times 600 \times 10^{5} = -0.6290$ mGal;
$-2\pi G \times 125 \times 600 \times 10^{5} = -3.1452$ mGal.)

**Which is dangerous?** The correlated case. An error that is a *constant multiple
of elevation* is not a constant offset: it tilts the anomaly field and therefore
mimics a real geological gradient, and it also correlates with terrain, which is
exactly the confound the density scan was supposed to remove. A $3.1\ \mathrm{mGal}$
tilt at $600$ m would be interpreted as structure. The uncorrelated case's
$0.63\ \mathrm{mGal}$ error is closer to a bias in the level of the map, which is
comparatively benign. The lesson's diagnostic — reporting the residual
$|$correlation$|$ at the optimum, $0.0022$ versus $0.5984$ — distinguishes the two
cases without knowing the true density.

---

## ★★★7 — Specifying the terrain-model radius (specification)

**Requirement.** The omitted contribution of the terrain outside radius $R$ must be
below $0.05\ \mathrm{mGal}$.

**Model.** For the dominant case of a station standing above its surroundings, the
omitted annulus is a ring of "missing" material at distance $s > R$ whose vertical
attraction falls off roughly as $s^{-1}$ in the thin-plate limit (the ring's
vertical component decreases with distance, and the area grows as $s\,\mathrm{d}s$).
A usable specification therefore needs an actual relief model in the annulus, not a
one-line formula, and the honest way to fix $R$ is to compute the correction twice,
at $R$ and at $2R$, and to increase $R$ until the difference is below the
requirement. For a station $h$ above a plateau, the classic rule of thumb is
$R \gtrsim 20h$ to $50h$; the lesson's own finite-body measurement gives the
quantitative anchor: at $R/h = 20$ a cylinder is $2.5\%$ short of the slab value
and at $R/h = 50$ it is $1.0\%$ short, and these fractions multiply the slab term
$2\pi G\rho h$, not the anomaly.

**Design.**

1. Choose a candidate radius $R_0$, compute the terrain correction with a digital
   elevation model clipped at $R_0$, then repeat with $2R_0$.
2. Report the difference; if it exceeds $0.05\ \mathrm{mGal}$, increase $R_0$
   (roughly doubling) and repeat.
3. Report the converged radius, the elevation-model resolution used, and the
   residual difference as the correction's uncertainty.

**What it depends on besides $h$:** the relief in the annulus (a flat plain needs a
small radius; a station in a canyon needs a large one), the density used, the
station's own height above the local surroundings rather than above the ellipsoid,
and the elevation model's accuracy. A specification that fixed $R$ as a multiple of
$h$ alone, without the convergence test, would be unfalsifiable and therefore not a
specification.

---

## ★★★8 — Error budget for a 200-station survey (specification and worked core)

**Inputs and plausible uncertainties** (SYNTHETIC, but stated so they can be
challenged): differential-GNSS height $\sigma_h = 0.05\ \mathrm{m}$; horizontal
position $\sigma_{xy} = 0.10\ \mathrm{m}$; density $\sigma_\rho = 120\
\mathrm{kg\,m^{-3}}$ (from a regional average, with $500\ \mathrm{m}$ of relief);
terrain model truncated at a radius where the residual is
$\sigma_t = 0.02\ \mathrm{mGal}$; instrument repeatability
$\sigma_i = 0.01\ \mathrm{mGal}$.

**Propagation**, using the measured coefficients from the lesson at $45^\circ$
(free air $0.308555$, slab $0.111969$, latitude gradient
$0.8131\ \mathrm{mGal\,km^{-1}}$ at $45^\circ$):

| term | formula | value (mGal) |
|---|---|---|
| height | $\left|0.308555 - 0.111969\right|\sigma_h$ | $0.0098$ |
| position | $0.8131 \times 10^{-3} \times \sigma_{xy}$ (mGal per m, at $45^\circ$) | $0.00008$ |
| density | $\left|2\pi G\right| \times 10^{5} \times \sigma_\rho \times 500$ | $6.290$ |
| terrain model | given | $0.020$ |
| instrument | given | $0.010$ |

**Total** in quadrature:
$\sqrt{0.0098^{2} + 0.00008^{2} + 6.290^{2} + 0.020^{2} + 0.010^{2}} =
6.290\ \mathrm{mGal}$ — dominated entirely by the density term.

**Best design change.** The density dominates by a factor of more than 300, so
nothing else matters until it is reduced: recovering the density from rock samples,
a borehole, or a gravity-based scan (lesson Section 6) to
$\sigma_\rho = 30\ \mathrm{kg\,m^{-3}}$ would bring the total to about
$1.57\ \mathrm{mGal}$, a factor of four. Improving the height from $5\ \mathrm{cm}$
to $1\ \mathrm{cm}$ would change the total from $6.290$ to $6.290\
\mathrm{mGal}$ — no measurable improvement. **Spending on positioning before
spending on density would be money wasted**, and the budget is the evidence.

A caveat to state with the budget: $\sigma_\rho$ is not a statistical uncertainty
in the ordinary sense, because the density is a model choice rather than a
repeated measurement; the honest description is a plausible range, and the
sensitivity coefficient is what makes the range matter.

---

## ★★★9 — Why the isostatic anomaly is different

**The logical difference.** The Bouguer anomaly is a difference between an
observation and a *computable* reference: normal gravity, the free-air gradient and
the slab attraction are fixed functions of position, height and one assumed
density. Reduce the data and the answer is determined, up to the density. The
isostatic anomaly removes the modelled attraction of the deep compensation of
topography, and that compensation is not observable from the gravity data alone:
it is inferred from a model (Airy, Pratt, flexural) with free parameters
(crustal and mantle densities, elastic thickness, reference depth). The reduced
number therefore depends on a hypothesis about the subsurface, so a nonzero
isostatic anomaly is simultaneously (i) a possible geological signal and (ii)
possible evidence that the compensation model is wrong. That dual reading is what
makes it logically different, not its magnitude.

**Test design.**

1. Choose two compensation models that differ materially (for example, local Airy
   compensation with a stated root density contrast, and a flexural model with a
   finite elastic thickness).
2. Reduce the same SYNTHETIC or real data set with both, and map the difference of
   the two isostatic anomalies.
3. Predict, before computing, the *spatial signature* that distinguishes them: a
   local Airy model compensates each load where it sits, so the isostatic anomaly
   should be flat over a large load; a flexural model supports loads regionally, so
   the residual should have a long-wavelength tail and an edge signature at load
   boundaries.
4. Compute the residual correlation between the isostatic anomaly and topography as
   a function of the model's free parameter (elastic thickness, or root-density
   contrast), the same Nettleton logic applied to a deeper parameter.

**Falsification.** If the residual is uncorrelated with topography for a whole
range of the free parameter, then the data cannot distinguish the models and the
correct conclusion is to report the range, not a preferred value. If the residual
correlates strongly with topography for *every* parameter value, the compensation
model is wrong in a way no parameter choice can fix. Either outcome is
falsifiable and quantitative, which is what makes it a test rather than an
opinion.
