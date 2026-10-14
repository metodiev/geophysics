# Solutions — 16-01-02 Hydrostatic Balance and Pressure-Height Relations

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [02 Hydrostatic Balance](../02-hydrostatic-balance.md).

---

## ★1 — Thickness sensitivity coefficients

$$K = \frac{R_d}{g_0}\ln\frac{p_1}{p_2},
\qquad \frac{R_d}{g_0} = \frac{287.041}{9.80665} = 29.2722\ \mathrm{m\,K^{-1}}.$$

| layer | $\ln(p_1/p_2)$ | $K$ (m K⁻¹) |
|---|---|---|
| 1000–850 hPa | 0.162519 | **4.757** |
| 850–700 hPa | 0.194156 | **5.683** |
| 500–200 hPa | 0.916291 | **26.820** |

The logarithm is **dimensionless** (it is the ratio of two pressures), which is
why $K$ carries the whole unit structure: metres per kelvin. Note the asymmetry
worth remembering — the $500\text{–}200\ \mathrm{hPa}$ layer has the same
temperature sensitivity per kelvin but five times the thickness response of the
$1000\text{–}850\ \mathrm{hPa}$ layer, because its pressure ratio is larger.

---

## ★2 — Thickness of a warm low layer

$$\Delta Z = K\bar T = 4.757 \times 285 = 1355.7\ \mathrm{m}.$$

At $\bar T = 283\ \mathrm{K}$: $\Delta Z = 4.757 \times 283 = 1346.2\ \mathrm{m}$.

Difference: $1355.7 - 1346.2 = 9.5\ \mathrm{m}$ for $2\ \mathrm{K}$ — i.e. the
$4.76\ \mathrm{m\,K^{-1}}$ coefficient, exactly as the linear relation requires.

---

## ★3 — Mean temperature from a thickness

$$\bar T = \frac{\Delta Z}{K} = \frac{5400}{20.2884} = 266.16\ \mathrm{K},$$

$$\bar T = 266.16 - 273.15 = -6.99\ \mathrm{^\circ C}.$$

*Statement to include:* this is a **virtual** temperature. The layer contains water
vapour, which is lighter than dry air, so the actual kinetic temperature is lower
than $266.16\ \mathrm{K}$ by about $0.608\,q\,\bar T$ for a specific humidity $q$.
At $q = 6\ \mathrm{g\,kg^{-1}}$, that is
$0.608 \times 0.006 \times 266.16 = 0.97\ \mathrm{K}$.

---

## ★4 — Geopotential heights

$$Z = z\frac{R_E}{R_E+z}, \qquad R_E = 6.371\times10^{6}\ \mathrm{m}.$$

| $z$ (m) | $Z$ (m) | $Z - z$ (m) |
|---|---|---|
| 3000 | 2998.588 | $-1.41$ |
| 8000 | 7989.967 | $-10.03$ |
| 15000 | 14964.767 | $-35.23$ |

These agree with the approximation $Z-z \approx -z^2/R_E$: at $3\ \mathrm{km}$,
$-9\times10^{6}/6.371\times10^{6} = -1.41\ \mathrm{m}$; at $15\ \mathrm{km}$,
$-2.25\times10^{8}/6.371\times10^{6} = -35.3\ \mathrm{m}$. ✔

---

## ★5 — The pressure-coordinate form, and geometric versus geopotential thickness

**Derivation.** Hydrostatic balance gives $\partial p/\partial z = -\rho g$, hence
$\partial z/\partial p = -1/(\rho g)$ (valid because the transformation is
one-dimensional and monotonic). Since $\Phi = \int_0^z g(z')\mathrm{d}z'$,
$\partial\Phi/\partial z = g$, so by the chain rule

$$\frac{\partial\Phi}{\partial p} = \frac{\partial\Phi}{\partial z}
\frac{\partial z}{\partial p} = g\left(-\frac{1}{\rho g}\right)
= -\frac{1}{\rho}. \qquad \checkmark$$

This is the reason pressure is a natural vertical coordinate: geopotential is the
integral of *specific volume* over pressure, and $\Phi$ is what enters the
momentum equations.

**Numbers.** Geometric thickness from ★2: $\Delta z = 1355.726\ \mathrm{m}$,
between $z_1 = 111\ \mathrm{m}$ and $z_2 = 1466.726\ \mathrm{m}$.

$$Z_1 = 111\frac{R_E}{R_E+111} = 110.998\ \mathrm{m}, \qquad
Z_2 = 1466.726\frac{R_E}{R_E+1466.726} = 1466.388\ \mathrm{m},$$

$$\Delta Z = 1466.388 - 110.998 = 1355.391\ \mathrm{m}.$$

Difference: $\Delta Z - \Delta z = -0.336\ \mathrm{m}$, i.e. $-0.0248\%$ of the
layer. Small, and *the same sign* as the correction itself (the correction grows
with height, so a geopotential thickness is slightly smaller than a geometric
one). It matters only when the temperature accuracy is better than $0.017\
\mathrm{K}$, which is never; but it is exactly the size of the thickness errors
discussed in Example 2 of the lesson, so the two must not be confused.

---

## ★6 — A sensor bias, and the same thickness error in two layers

**Bias.** $\delta(\Delta Z) = K\,\delta\bar T = 4.757 \times 0.4 = 1.903\
\mathrm{m}$ in the $1000\text{–}850\ \mathrm{hPa}$ layer.

**Thickness uncertainty expressed as temperature.** Inverting
$\delta\bar T = \delta(\Delta Z)/K$:

| layer | $K$ (m K⁻¹) | $\delta\bar T$ for $\delta(\Delta Z) = 5\ \mathrm{m}$ |
|---|---|---|
| 1000–850 hPa | 4.757 | **1.051 K** |
| 500–200 hPa | 26.820 | **0.186 K** |

**Comment.** *In metres*, a fixed temperature bias hurts the deep, high layer more
($0.4\ \mathrm{K} \rightarrow 10.7\ \mathrm{m}$ for $500\text{–}200\ \mathrm{hPa}$
against $1.9\ \mathrm{m}$ for $1000\text{–}850\ \mathrm{hPa}$). *In kelvin*, a
fixed thickness uncertainty is far more damaging to the shallow layer: $5\
\mathrm{m}$ of thickness noise is $1.05\ \mathrm{K}$ of temperature error down
low, but only $0.19\ \mathrm{K}$ up high. Both statements are true and they point
in opposite directions, which is why an error budget must state whether its
currency is metres or kelvin.

---

## ★7 — Fractional errors are equal

Differentiate $\Delta Z = (R_d\bar T/g_0)\ln(p_1/p_2)$ at fixed $p_1, p_2$:

$$\delta(\Delta Z) = \frac{R_d}{g_0}\ln\frac{p_1}{p_2}\,\delta\bar T
= \Delta Z\,\frac{\delta\bar T}{\bar T}
\qquad\Longrightarrow\qquad
\frac{\delta(\Delta Z)}{\Delta Z} = \frac{\delta\bar T}{\bar T}. \qquad\checkmark$$

*Prediction:* for $\bar T = 270\ \mathrm{K}$ and $\delta\bar T = 2\ \mathrm{K}$,
$\delta(\Delta Z)/\Delta Z = 2/270 = 7.407\times10^{-3}$.

*Verification:* with the $1000\text{–}500\ \mathrm{hPa}$ coefficient,
$\Delta Z = 20.2884 \times 270 = 5477.87\ \mathrm{m}$ and
$\delta(\Delta Z) = 20.2884 \times 2 = 40.577\ \mathrm{m}$; then
$40.577/5477.87 = 7.407\times10^{-3}$. ✔

The practical reading of this identity: **thickness measurements are as accurate
as temperature measurements, in relative terms** — a $1\%$ temperature error is a
$1\%$ thickness error, so a $0.1\%$ thickness change requires $0.1\%$ temperature
accuracy, i.e. $0.27\ \mathrm{K}$ on a $270\ \mathrm{K}$ layer.

---

## ★8 — From pressure accuracy to mass and height

Mass: $\delta(m/A) = \delta p/g_0 = 50/9.80665 = 5.099\ \mathrm{kg\,m^{-2}}$.

Height, using the isothermal relation $\mathrm{d}Z = H\,\mathrm{d}p/p$:

$$\mathrm{d}Z = 8434.2 \times \frac{50}{101325} = 4.162\ \mathrm{m}.$$

Interpretation: a $0.5\ \mathrm{hPa}$ pressure error is worth about $5\
\mathrm{kg\,m^{-2}}$ of column mass, or $4.2\ \mathrm{m}$ of height near sea
level. Both conversions need the *same* stated assumption (hydrostatic balance);
the height one additionally needs a temperature, because $H \propto T$.

---

## ★9 — Non-hydrostatic error budget

The fractional departure is $|a_z|/g$, and the column pressure offset scales as
$(|a_z|/g)p_0$:

| column | $a_z$ (m s⁻²) | $|a_z|/g$ | $\Delta p$ (Pa) | $\Delta p$ (hPa) | height-equivalent (m) |
|---|---|---|---|---|---|
| strong updraught | $0.2$ | $2.04\times10^{-2}$ | 2066.5 | **20.66** | 172.0 |
| quiescent | $10^{-5}$ | $1.02\times10^{-6}$ | 0.103 | $1.0\times10^{-3}$ | 0.01 |

(Height-equivalent uses $\mathrm{d}Z = H \Delta p/p$ with $H = 8434.2\
\mathrm{m}$ and $p = 101325\ \mathrm{Pa}$.)

**Comparison with the other terms.**

- Sensor accuracy of ★8: $0.5\ \mathrm{hPa}$. Non-hydrostatic dominance when
  $(a_z/g)p_0 > 50\ \mathrm{Pa}$, i.e. $a_z > (50/101325)\times9.80665 =
  \mathbf{4.8\times10^{-3}\ m\,s^{-2}}$. A strong updraught exceeds this by two
  orders of magnitude; a quiescent column is three orders below it.
- Temperature-induced thickness error of ★6: $1.9$ to $10.7\ \mathrm{m}$ for a
  $0.4\ \mathrm{K}$ bias. The updraught's height-equivalent ($172\ \mathrm{m}$)
  dwarfs both.

**Conclusion.** For $a_z \gtrsim 5\ \mathrm{mm\,s^{-2}}$ the non-hydrostatic term
is the largest single error in a pressure-based height, larger than any plausible
instrument bias. Because such accelerations occur at convective scales
($\sim1\text{–}10\ \mathrm{km}$), the *scale* at which hydrostatic balance becomes
the dominant error is the convective scale. The measurement that detects the
violation is not a pressure profile — which hardly notices — but a direct
measurement of vertical motion (Doppler radar, or a pair of closely spaced
soundings showing a mass-flux divergence).

---

## ★10 — Why two laboratories report different layer temperatures

At least four distinct causes; the classification is the answer.

1. **Different definition of the vertical coordinate** (geometric $z$ versus
   geopotential $Z$, or pressure versus height interpolation). *Definitional.*
   Removable by agreement; magnitude $\sim10^{-3}$ relative, from ★4.
2. **Different layer-mean convention** (arithmetic versus $\ln p$-weighted mean).
   *Definitional.* The lesson measures the difference: $0.390\ \mathrm{K}$ on the
   1000–500 hPa layer, $0.145\%$ of the thickness. Removable by agreement.
3. **Moisture treatment** (virtual temperature versus true temperature, and whether
   a humidity correction is applied). *Physical*, but systematic and correctable
   *given* a humidity measurement; the residual is then a physical uncertainty from
   humidity sensor error.
4. **Radiation and lag errors of the sensor, and the sounding's own ascent time.**
   *Physical.* Partly reducible with better instruments, but the sounding measures
   the air along a slanted, drifting path, not a vertical column: the horizontal
   displacement of a radiosonde is a physical difference, not an instrument
   defect, and it cannot be removed in principle from a single ascent.

A fifth, genuinely unresolvable-in-principle source: the atmosphere is not
horizontally uniform, so "the temperature of the layer above the station" is not a
well-defined quantity independent of the averaging volume. That is a definitional
statement about the Earth, not about instruments.

---

## ★11 — Specification for a satellite thickness-change measurement

**(a) Required thickness accuracy.** From ★7,
$\delta(\Delta Z) = \Delta Z\,\delta\bar T/\bar T$. With
$\Delta Z = 5463\ \mathrm{m}$, $\bar T = 269.3\ \mathrm{K}$ and
$\delta\bar T = 0.5\ \mathrm{K}$:
$\delta(\Delta Z) = 5463 \times 0.5/269.3 = \mathbf{10.1\ m}$, so the *change* in
thickness over ten years must be resolved to about $10\ \mathrm{m}$ — better than
$0.2\%$ of the layer, and this is a requirement on the *difference*, not on either
absolute value.

**(b) Two error sources with different scaling with averaging time.**

- **Random instrument noise**, which falls as $N^{-1/2}$ in the number $N$ of
  independent soundings/retrievals. Averaging a decade of data helps.
- **Orbital drift and calibration degradation**, which do *not* average down: they
  are slowly varying biases that can masquerade as a trend. Averaging cannot
  separate them from the signal; only inter-satellite cross-calibration or an
  independent, overlapping record can.

**(c) A confounder a static correction cannot remove.** A change in the *vertical
distribution* of temperature within the layer (for example cooling aloft with
warming below, a pattern that is physically expected) can leave the
$\ln p$-weighted layer mean unchanged. No static correction can remove it because
it is not an instrument error: the observable and the quantity of interest are
different integrals of the same temperature field. The remedy is
pattern-based detection — comparing the vertical structure, not just the mean —
which is exactly the logic of fingerprinting in
[16-07-02](../../07-climate-extremes-and-attribution/02-detection-attribution.md).

**Stated assumptions.** (i) The thickness-to-temperature conversion is the
hypsometric relation with a known $R_d$; (ii) the temperature field is the only
thing changing (no change in the composition that alters $R_d$ — see exercise
★11 of [lesson 01](01-atmospheric-composition-solutions.md), where a
$3\times10^{-4}$ change in $R_d$ would be a $0.03\%$ thickness effect,
i.e. $1.6\ \mathrm{m}$); (iii) the geopotential correction is stable in time.
