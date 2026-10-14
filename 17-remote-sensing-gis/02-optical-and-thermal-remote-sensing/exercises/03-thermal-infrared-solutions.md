# Solutions — 17-02-03 Thermal Infrared: Land Surface Temperature and Heat Flow

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All parameters are **SYNTHETIC** teaching values.

Lesson: [03 Thermal Infrared: Land Surface Temperature and Heat Flow](../03-thermal-infrared.md).

---

## ★1 — Sensitivity at $12\ \mathrm{\mu m}$

$$\frac{\partial T}{\partial\ln\varepsilon}
= \frac{\lambda k_B T^{2}}{hc}
= \frac{12.0\times10^{-6}\times1.380649\times10^{-23}\times290^{2}}
{6.62607015\times10^{-34}\times2.99792458\times10^{8}}
= \frac{1.3905\times10^{-23}}{1.9864\times10^{-25}}
= 70.14\ \mathrm{K}.$$

For a $2\%$ emissivity error:

$$\Delta T \approx 70.14\ln(1.02) = 70.14\times0.019803 = 1.389\ \mathrm{K}
\approx 1.4\ \mathrm{K}.$$

(The linear estimate $70.14\times0.02 = 1.40\ \mathrm{K}$ differs by $1\%$, which
is the expected curvature over a $2\%$ change.) A $1.4\ \mathrm{K}$ systematic
error is larger than most geophysical signals of interest, which is the
quantitative form of the lesson's warning about emissivity.

---

## ★2 — Semi-diurnal skin depth

$$\omega = \frac{2\pi}{12\times3600} = 1.4544\times10^{-4}\ \mathrm{s^{-1}},$$
$$\delta = \sqrt{\frac{2\alpha}{\omega}}
= \sqrt{\frac{2\times1.0\times10^{-6}}{1.4544\times10^{-4}}}
= \sqrt{0.013751} = 0.11726\ \mathrm{m}.$$

Compare with the diurnal value $0.1658\ \mathrm{m}$: the ratio is
$\sqrt{2} = 1.414$ against the measured $0.1658/0.11726 = 1.414$, confirming the
$\delta\propto\sqrt{\text{period}}$ scaling exactly. **The semi-diurnal solar tide
is a real forcing with a different penetration depth from the diurnal cycle**, and
a two-frequency measurement can separate them.

---

## ★3 — Flux anomaly to temperature anomaly

$$\Delta T = \Delta q\,\frac{L}{k} = 0.15\times\frac{50}{3.0} = 2.50\ \mathrm{K}.$$

Significance: $2.50/0.14 = 17.9\sigma$ per pixel. So this anomaly is detectable
*if the only source of surface temperature variation were this flux anomaly and
detector noise*. The lesson's caveat applies with full force: a moisture
difference of $2\%$ by volume, or a $0.02$ albedo difference, produces a surface
temperature change of order $1$–$2\ \mathrm{K}$ with a similar spatial structure —
the same order as the signal.

---

## ★4 — Deriving the split window

Write the radiative transfer of each band with a surface emissivity $\varepsilon$
(the same in both bands to leading order) and transmittance $\tau_i$:

$$L_i = \tau_i\left[\varepsilon B_\lambda(T_s)
+ (1-\varepsilon)B_\lambda(T_a)\right]
+ (1-\tau_i)B_\lambda(T_a).$$

Linearise the Planck function about $T_s$:
$B_\lambda(T_a) \approx B_\lambda(T_s) + (T_a-T_s)\,\partial_TB_\lambda$.
Then

$$L_i \approx B_\lambda(T_s) + (1-\tau_i)\left[(1-\varepsilon)
+ \text{surface term}\right](T_a-T_s)\,\partial_TB_\lambda .$$

The essential structure is that the atmospheric perturbation of band $i$ is
proportional to $(1-\tau_i)$, while the surface term $\varepsilon B_\lambda(T_s)$
is common. Converting radiance to brightness temperature via the local
derivative, $T_{b,i} - T_s \propto (1-\tau_i)(T_a-T_s)$, so

$$T_{b,1}-T_{b,2} \propto \left(\tau_2-\tau_1\right)\left(T_a-T_s\right),$$

which contains the atmosphere–surface contrast and **not** $T_s$ to leading order.
Hence $T_s \approx T_{b,1} + a(T_{b,1}-T_{b,2}) + b$ with $a,b$ fitted.

**Cancelled:** the leading atmospheric absorption and emission term, i.e. the
dependence on the water-vapour (or any absorbing-gas) amount, through the
$(1-\tau_i)$ contrast.
**Retained:** the surface emissivity $\varepsilon$ and its spectral variation
$\Delta\varepsilon$ — both bands still contain $\varepsilon B_\lambda(T_s)$. Also
retained: any systematic spectral error (band calibration), the non-linearity of
the Planck function over the band (second order), and any surface spectral contrast
that differs between the two windows.

---

## ★5 — Damping at $0.60\ \mathrm{m}$

$$\text{annual: } e^{-0.60/3.1694} = e^{-0.18931} = 0.8275,$$
$$\text{diurnal: } e^{-0.60/0.1658} = e^{-3.619} = 0.02681.$$

So an annual surface amplitude of $10\ \mathrm{K}$ leaves $8.28\ \mathrm{K}$ at
$0.60\ \mathrm{m}$, while a $10\ \mathrm{K}$ diurnal amplitude leaves
$0.27\ \mathrm{K}$. **A $0.60\ \mathrm{m}$ soil-temperature record is a climate
record contaminated by a $2.7\%$ weather signal**, which is why shallow borehole
climatology requires the daily cycle to be filtered (and why its phase lag,
$0.60/0.1658 = 3.62$ rad $= 13.8\ \mathrm{h}$, is itself a diagnostic that the
measurement is working).

---

## ★6 — Band average versus band centre

$$\bar L(9\text{–}11\ \mathrm{\mu m}, 300\ \mathrm{K}) = 9.8501\times10^{6}
\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}},$$
$$B_\lambda(10\ \mathrm{\mu m}, 300\ \mathrm{K}) = 9.9240\times10^{6}
\ \mathrm{W\,m^{-2}\,sr^{-1}\,m^{-1}},$$
$$\text{relative difference} = \frac{9.8501-9.9240}{9.8501} = -0.751\%.$$

**Verdict: not acceptable.** A $0.75\%$ radiance error at $300\ \mathrm{K}$ and
$10\ \mathrm{\mu m}$ corresponds to

$$\Delta T = \frac{\Delta\ln L}{\partial_T\ln B} = 0.0075\times67.56
= 0.51\ \mathrm{K},$$

five times the $0.1\ \mathrm{K}$ budget. Over the narrower $1\ \mathrm{\mu m}$ band
of the lesson the error is $0.093\%$–$0.156\%$, i.e. $0.06$–$0.11\ \mathrm{K}$ —
marginal. **Band integration against the measured spectral response is mandatory
for any product claiming sub-$0.1\ \mathrm{K}$ accuracy.**

---

## ★7 — Detection thresholds for two anomaly thicknesses

$$\Delta q_{\min} = \frac{n\,\mathrm{NE}\Delta T\,k}{L}.$$

For $n = 3$, NEΔT $= 0.14\ \mathrm{K}$, $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$:

| $L$ (m) | $\Delta q_{\min}$ (W m⁻²) |
|---|---|
| 10 | $3\times0.14\times2.5/10 = 0.105$ |
| 100 | $3\times0.14\times2.5/100 = 0.0105$ |

**Comment.** The threshold scales as $1/L$: the *same* radiometric performance
detects a ten-times smaller flux anomaly if the anomaly is expressed over a
ten-times thicker column. This is not a property of the instrument at all — it is
the thermal-resistance conversion $\Delta T = \Delta q\,L/k$. The practical
consequence is that **geothermal detection statements must always state the
inferred depth/thickness of the anomaly**, since without it the threshold is
meaningless. It also explains why shallow anomalies (hot springs, fumaroles,
hydrothermal alteration) are the easy targets and deep-seated flux anomalies are
the hard ones.

---

## ★8 — Counting unknowns in a two-band thermal retrieval

**Unknowns.** For two bands: the surface temperature $T_s$, the two emissivities
$\varepsilon_1, \varepsilon_2$ (assuming the surface is spectrally varying), and
the atmospheric state. If the atmosphere is known (from an independent profile or
a reanalysis), the remaining unknowns are $3$: $T_s, \varepsilon_1,
\varepsilon_2$.

**Equations.** Two radiance measurements:

$$L_i = \tau_i\left[\varepsilon_i B_{\lambda_i}(T_s)
+ (1-\varepsilon_i)B_{\lambda_i}(T_a)\right]
+ (1-\tau_i)B_{\lambda_i}(T_a),\qquad i = 1, 2 .$$

So $2$ equations, $3$ unknowns: **underdetermined**, with a one-parameter family of
solutions $(T_s, \varepsilon_1, \varepsilon_2)$ — the multiband generalisation of
the single-band degeneracy. With $n$ bands the count is $n$ equations and
$n+1$ unknowns, so the deficiency is always exactly one, regardless of how many
bands are used. This is the "temperature–emissivity separation" problem.

**Two physically defensible constraints.**

1. **Emissivity range / spectral-shape constraint.** Restrict $\varepsilon$ to a
   physically plausible interval (e.g. $0.9 \le \varepsilon \le 1$) and require the
   spectral *shape* of $\varepsilon$ to lie in a family with few parameters
   (empirical relations between band emissivities, or a minimum-emissivity
   anchoring). This reduces the number of effective unknowns by at least one and
   is the standard operational approach.
2. **A known-emissivity band, or a known-surface reference.** Use a band where the
   surface is known to be effectively black (deep, clear water; dense, closed
   vegetation) so that $\varepsilon = 1$ is an assumption with an error budget, or
   use a reflectometer measurement of a reference target to anchor $\varepsilon$.

**Which for bare rock.** The **range/shape constraint**, because bare rock has a
spectrally varying emissivity (silicates show a well-known reststrahlen-like
contrast between the shorter and longer thermal bands, of order a few per cent in
this synthetic framing) and there is no band in which bare rock can be assumed
black. The constraint is a *prior* on emissivity shape, and its effect on $T_s$
must be propagated: from ★1, a residual emissivity error of $1\%$ is
$0.7\ \mathrm{K}$ at $10.8\ \mathrm{\mu m}$, so a shape prior good to only $2\%$
delivers $T_s$ to about $1.4\ \mathrm{K}$ — not better than the single-band
retrieval unless the prior is well validated. **The degradation of the result to
the quality of the prior is the honest statement, and it is why
temperature–emissivity-separation products publish validation against in-situ
radiometers rather than claiming per-pixel performance.**

---

## ★9 — Detecting a $0.1\ \mathrm{W\,m^{-2}}$ flux anomaly

**Target.** $\Delta q = 0.10\ \mathrm{W\,m^{-2}}$. Expressed over a $25\ \mathrm{m}$
layer with $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$ this is
$\Delta T = 0.10\times25/2.5 = 1.00\ \mathrm{K}$, i.e. $7.1\times$ NEΔT per pixel.
So the *radiometric* requirement is met with room to spare; the design problem is
entirely in the confounds.

**Acquisitions.** Two thermal bands (for the split window and for
temperature–emissivity separation) at **(i)** a pre-dawn overpass (a few hours
before sunrise), when the surface energy balance is closest to steady and the
subsurface flux dominates the surface skin temperature; and **(ii)** a midday
overpass, used to measure the diurnal amplitude, which is a proxy for thermal
inertia and hence for the surface materials. Repeat for at least a full year so
that the annual wave — which is what the geothermal flux actually modulates at
depth — is sampled; a single-season acquisition cannot separate the annual phase
from the flux.

**Ancillary data required.** Emissivity (from the retrieval or a laboratory
library resampled to the band responses); atmospheric profiles at each overpass
(temperature, water vapour) or an independent retrieval; a digital elevation model
for topographic correction and for computing slope/aspect-dependent insolation;
soil-moisture or a proxy (radar backscatter, a microwave product) because
evaporative cooling produces structure at the same scale; vegetation cover
(index or fractional cover); and albedo for the midday scene.

**Confounds to model.**

1. **Emissivity** — Section 3.3's systematic error, $0.7\ \mathrm{K}$ per $1\%$,
   which is comparable to the signal. Must be modelled, not assumed constant.
2. **Topography and insolation** — slope and aspect change the midday surface
   temperature by several kelvin; a pre-dawn scene reduces (not removes) this.
3. **Soil moisture and evaporation** — latent heat flux changes the surface
   temperature by $1$–$3\ \mathrm{K}$ with spatial patterns set by drainage, not
   by the geothermal flux.
4. **Vegetation** — canopy temperature differs from soil temperature, and cover
   changes both the emissivity and the partitioning of energy.
5. **Atmosphere and cloud** — a residual atmospheric error and any undetected
   cloud contaminate the retrieval; multi-temporal compositing must not smear the
   diurnal signal that is used as a diagnostic.
6. **Seasonal and annual cycles** — the annual wave has an amplitude of metres of
   penetration; sampling one season cannot distinguish an annual phase shift from
   a flux anomaly.

**The discriminating test.** The geothermal anomaly has a specific signature that
the energy-balance confounds do not: it should

1. appear at **pre-dawn** (when latent and sensible fluxes are small) *and* be
   **anti-correlated with the diurnal amplitude** — a geothermal area is warmer
   at night and radiates a larger fraction of its energy conductively, so its
   diurnal amplitude is *reduced* while its mean temperature is *elevated*;
2. be **spatially stationary** across seasons in the pre-dawn product, whereas a
   moisture- or vegetation-driven anomaly follows the growing season;
3. scale with the **thermal-resistance model** of Section 3.6: the anomaly's
   amplitude should correlate with the mapped thickness of the resistive layer
   (e.g. a known alteration cap or a shallow water table) rather than with
   surface cover.

**Positive control.** Apply the method to a site with a documented surface
manifestation (a hot spring or fumarole field, or a synthetic scene with a known
injected anomaly in a validation exercise) and check that the recovered
$\Delta q$ matches the known value to within the propagated uncertainty. **Without
such a control, a $1\ \mathrm{K}$ pre-dawn anomaly map is not evidence of a
geothermal flux anomaly — it is a map of the confounds listed above.**
