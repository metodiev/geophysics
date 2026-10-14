# Solutions — 16-09-04 Geophysics for Carbon Capture and Storage Monitoring

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [04 Geophysics for Carbon Capture and Storage Monitoring](../04-geophysics-carbon-storage.md).

---


## ★ Foundational

## ★1 — Gassmann substitution

$$\frac{K_{\text{dry}}}{K_{\min}} = \frac{12}{37} = 0.324324,
\qquad \left(1 - 0.324324\right)^{2} = 0.675676^{2} = 0.456538,$$

$$\frac{\phi}{K_{\text{fl}}} = \frac{0.20}{2.5} = 0.080000, \qquad
\frac{1-\phi}{K_{\min}} = \frac{0.80}{37} = 0.021622,$$
$$\frac{K_{\text{dry}}}{K_{\min}^{2}} = \frac{12}{37^{2}} = \frac{12}{1369}
= 0.008766,$$

$$\text{denominator} = 0.080000 + 0.021622 - 0.008766 = 0.092856,$$

$$K_{\text{sat}} = 12 + \frac{0.456538}{0.092856}
= 12 + 4.917 = \mathbf{16.917\ GPa}.$$

The saturated rock is $41\%$ stiffer than the dry frame: the brine, though
compressible, is far stiffer than air or vacuum and resists the pore collapse.

---

## ★2 — Saturated densities

Brine: $\rho = 0.80(2650) + 0.20(1050) = 2120 + 210
= \mathbf{2330.0\ kg\,m^{-3}}$.

CO2: $\rho = 0.80(2650) + 0.20(700) = 2120 + 140
= \mathbf{2260.0\ kg\,m^{-3}}$.

Change: $(2260 - 2330)/2330 = \mathbf{-3.0\%}$. The density change is small
because only the pore fraction changed; the seismic contrast comes mostly from the
*modulus*, not the density.

---

## ★3 — Reflection coefficient

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1} = \frac{7.0 - 8.0}{15.0}
= \mathbf{-0.0667}.$$

A **negative** $R$ means the impedance decreases across the interface in the
direction of propagation (from the upper medium $Z_1$ into the lower $Z_2$): the
reflected wavelet is polarity-reversed relative to a positive-contrast interface.
In the CCS context a negative reservoir reflection is exactly the expected
signature of a light, compressible pore fluid beneath a denser caprock.

---

## ★★ Applied

## ★★4 — Velocities for both saturations

Brine case, $K_{\text{sat}} = 16.917\ \mathrm{GPa}$,
$\mu = 9.0\ \mathrm{GPa}$, $\rho = 2330\ \mathrm{kg\,m^{-3}}$:

$$v_p = \sqrt{\frac{(16.917 + 12.0)\times10^{9}}{2330}}
= \sqrt{1.2411\times10^{7}} = \mathbf{3523\ m\,s^{-1}},$$
$$v_s = \sqrt{\frac{9.0\times10^{9}}{2330}} = \sqrt{3.8627\times10^{6}}
= \mathbf{1965\ m\,s^{-1}}.$$

CO2 case, $K_{\text{sat}} = 12.114\ \mathrm{GPa}$, same $\mu$,
$\rho = 2260\ \mathrm{kg\,m^{-3}}$:

$$v_p = \sqrt{\frac{(12.114 + 12.0)\times10^{9}}{2260}}
= \sqrt{1.0666\times10^{7}} = \mathbf{3266\ m\,s^{-1}},$$
$$v_s = \sqrt{\frac{9.0\times10^{9}}{2260}} = \sqrt{3.9823\times10^{6}}
= \mathbf{1996\ m\,s^{-1}}.$$

Directions: $v_p$ falls by $7.3\%$, $v_s$ **rises** by $1.5\%$. The $v_s$ rise is
not a stiffening of the rock — the shear modulus is unchanged — but the effect of
a lower density on the same modulus. Getting the *sign* of the $v_s$ change right
is a good check that the substitution has been done correctly.

---

## ★★5 — Gravity anomaly and detection

$$\Delta g = \frac{G\,\Delta m}{d^{2}}
= \frac{6.674\times10^{-11} \times 5.0\times10^{9}}{1500^{2}}
= \frac{0.3337}{2.25\times10^{6}}
= 1.483\times10^{-7}\ \mathrm{m\,s^{-2}}.$$

Converting with $1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$:

$$\Delta g = \mathbf{-14.83\ \mu Gal}.$$

Against a $5\ \mathrm{\mu Gal}$ noise, $|\Delta g|/\text{noise} = 2.97 > 2$: the
plume is **detected** at $2\sigma$. Note the sign: the anomaly is negative
because the plume is a *deficit* — the same sign as any low-density body, which is
why a gravity survey alone cannot distinguish CO2 from a dry (gas-filled) zone
without additional information.

---

## ★★6 — Depth error to mass error

The inferred mass is $\Delta m_{\text{inf}} = \Delta g\, d_{\text{used}}^{2}/G$. With
$d_{\text{used}} = 1.08\,d_{\text{true}}$,

$$\frac{\Delta m_{\text{inf}}}{\Delta m_{\text{true}}}
= (1.08)^{2} = 1.1664,$$

so the inferred mass is too large by $\mathbf{+16.6\%}$.

**General rule:** because $\Delta g \propto \Delta m/d^{2}$ (i.e.
$\Delta m \propto \Delta g\,d^{2}$), a fractional depth error $f$ produces a mass
error of

$$\frac{\delta(\Delta m)}{\Delta m} = (1+f)^{2} - 1 \approx 2f
\ \text{for small } f.$$

**The mass error is approximately twice the depth error**, and it is signed: an
over-estimated depth over-estimates an inferred deficit. This is why a
gravity-derived mass must be reported as conditional on the geometry, ideally with
the geometry from an independent measurement (seismic depth conversion,
well data).

---

## ★★★ Research-oriented

## ★★★7 — Distinguishing lateral spreading from leakage (design)

**Observables and what each measures.**

1. **Time-lapse seismic** — the plume's *shape* and the elastic contrast. Lateral
   spreading changes the footprint; mass loss to a leak thins the anomaly and
   eventually makes it disappear.
2. **Repeat microgravity** — the *mass* (as a deficit). This is the decisive
   observable: a spreading plume conserves mass, a leaking plume does not.
3. **Repeat gravity gradiometry (if available)** — the *depth distribution* of the
   mass, which distinguishes a deepening/lateral plume from a rising leak.
4. **Wells and pressure** — reservoir pressure, which identifies injection-driven
   pressurisation and any unexpected communication.
5. **Microseismic** — induced events, which can indicate reactivation along a
   possible leakage pathway (with the operating-point caveat of a detection
   threshold).

**Metric.** The time series of (i) the total mass deficit from gravity, and
(ii) the areal extent from seismic, converted to an average thickness through a
stated saturation model. Lateral spreading predicts **constant mass with
increasing area**; leakage predicts **decreasing mass** at a rate above the
propagated uncertainty.

**Time sampling.** Sampling must resolve the expected rates: gravity and seismic
at intervals shorter than the timescale over which a detectable mass change would
accumulate — for a chosen leak rate, the interval is set by
$\Delta m_{\text{detect}}/\dot{m}_{\text{leak}}$, with both numbers stated.

**Falsification of the leak hypothesis.** The leak hypothesis is falsified if the
mass deficit stays constant within its uncertainty while the plume's footprint
grows, over a period long enough that the claimed (or instrumentally detectable)
leak rate would have produced a detectable mass loss. Equivalently: report the
upper bound the data place on the leak rate — that bound, rather than "no leak
detected", is the quantitative result.

**Also required:** the detection threshold for a *mass loss*, which is larger than
the threshold for detecting the plume itself, and the shallow-mass noise budget
that limits it (Section 4c of the lesson).

---

## ★★★8 — A joint seismic–gravity inversion (design)

**Why the combination is natural.** Seismic data measure a contrast in elastic
properties ($v_p$, $v_s$, $\rho$ through impedance), which depends on
*saturation* and on the fluid's properties. Gravity measures *mass*, which depends
on the volume and the density contrast. Saturation appears in both; geometry
(volume, depth) appears in both but with different weightings — seismic depends
weakly on depth (through travel time and tuning), gravity depends on depth
squared. That difference is the lever.

**Forward models required.**
1. A rock-physics model mapping (porosity, mineralogy, saturation, fluid
   properties) to $v_p$, $v_s$, $\rho$ — Gassmann plus a dry-frame model, with the
   dry frame itself a parameter.
2. A seismic forward model mapping the elastic field to amplitudes and travel
   times — at minimum a convolution with the wavelet over the plume's geometry,
   including tuning.
3. A gravity forward model mapping the density field to a surface anomaly.

**Parameterisation.** Plume geometry (depth, thickness, lateral extent, shape
parameters) plus saturation (uniform or a saturation profile) plus the dry-frame
parameters.

**Inversion and the testable question.** Invert jointly, with a misfit that
combines seismic and gravity residuals weighted by their noise, and report the
posterior (or a resolution analysis) for the saturation and geometry parameters
separately. Then ask the testable question: **does the joint dataset reduce the
saturation–geometry trade-off compared with either dataset alone?** The
quantitative answer is a comparison of the parameter covariance (or of the
singular-value spectra of the two design matrices and the joint one).

**Pattern that would show the methods are not separable here.** If the joint
posterior for saturation is as broad as the seismic-only posterior — because
saturation and thickness trade off along a direction that changes impedance and
mass in the same proportion — then the combination has not resolved the ambiguity,
and the honest report is a statement of the residual trade-off direction rather
than a unique saturation. This is the same non-uniqueness logic as
[16-09-03 §6](../03-geothermal-climate-records.md), and it is the reason the
analysis is worth doing before the monitoring programme is designed rather than
after.
