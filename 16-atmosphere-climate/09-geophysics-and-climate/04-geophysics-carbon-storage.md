---
id: 16-09-04
title: "Geophysics for Carbon Capture and Storage Monitoring"
level: research
prereqs: ["05-04-03", "16-09-02", "06-11-07"]
tags: [atmosphere, climate, carbon-capture, storage, gassmann, time-lapse, microgravity, monitoring]
---

# Geophysics for Carbon Capture and Storage Monitoring

> **All models and data in this module are SYNTHETIC.** The rock and fluid
> properties, plume geometry and instrument noise in
> `code/geophysics_carbon_storage_demo.py` are chosen teaching values, anchored on
> standard mineral and physical constants. No real storage site, reservoir,
> plume, instrument or published monitoring result is used.

Storing CO2 underground is a problem in *verification*, not only in geology. A
storage project must show, repeatedly and quantitatively, that the CO2 is where it
was put and that it is not leaking — a task that falls to geophysical monitoring:
time-lapse (4-D) seismic for the plume's shape, microgravity for its mass,
microseismic and well data for pressure and integrity. The physics is compact and
clean: **CO2 in a brine-filled reservoir makes the pore fluid far more
compressible and slightly lighter**, so the P-wave velocity falls, the S-wave
velocity rises a little, and the density falls.

This lesson follows that chain end to end — Gassmann substitution, impedance and
reflectivity, then mass and gravity — and then makes the distinction that decides
how a monitoring result should be used. **Detection is robust; quantification is
assumption-laden.** In the demonstration a compact plume is detectable to about
$2500\ \mathrm{m}$ depth at a $5\ \mathrm{\mu Gal}$ survey noise, yet a $10\%$
error in the assumed plume depth changes the inferred mass by $21\%$, because the
gravity signal depends on depth squared. A monitoring report that quotes a mass
without the geometric assumptions behind it has buried the uncertainty in a
constant.

## Learning objectives

By the end of this lesson you will be able to:

1. **Apply** Gassmann fluid substitution to compute saturated moduli, velocities
   and density for a brine-filled and a CO2-filled reservoir rock.
2. **Explain** why the CO2 signature is a strong $v_p$ decrease with a slight
   $v_s$ increase, and why that combination is diagnostic.
3. **Compute** acoustic impedances, reflection coefficients and the time-lapse
   change in reflectivity, including a polarity reversal.
4. **Compute** the gravity anomaly of a plume's mass deficit and **state** its
   depth dependence.
5. **Distinguish** detection from quantification, and **quantify** how a depth or
   geometry error propagates into an inferred mass.
6. **State** the assumptions a monitoring programme relies on and the
   measurements that could test them.
7. **Design** a monitoring statement that separates what is detected from what is
   quantified.

## Prerequisites

- [05-04-03 Gassmann Fluid Substitution and Saturation Effects](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md) —
  the fluid-substitution theory applied here.
- [16-09-02 Geodesy for Sea Level, Ice Mass and Water Storage](02-geodesy-climate.md) —
  the gravity and budget reasoning this lesson reuses.
- [06-11-07 Declustering, Completeness and Catalogue Physics](../../06-seismology/11-earthquake-statistics-and-hazard/07-catalog-declustering.md) —
  the detection-threshold logic that a microseismic monitoring network needs.

## 1. The rock-physics chain

**Gassmann's relation** gives the saturated bulk modulus $K_{\text{sat}}$ of a
rock from the dry-frame modulus $K_{\text{dry}}$, the mineral modulus $K_{\min}$
and the pore-fluid modulus $K_{\text{fl}}$ at porosity $\phi$:

$$K_{\text{sat}} = K_{\text{dry}}
+ \frac{\left(1 - K_{\text{dry}}/K_{\min}\right)^{2}}
{\dfrac{\phi}{K_{\text{fl}}} + \dfrac{1-\phi}{K_{\min}}
- \dfrac{K_{\text{dry}}}{K_{\min}^{2}}}.$$

The **shear modulus is unchanged** by the saturating fluid, $\mu_{\text{sat}} =
\mu_{\text{dry}}$, because a fluid cannot support shear. Density follows
$\rho = (1-\phi)\rho_{\min} + \phi\rho_{\text{fl}}$, and the velocities follow the
elastic relations

$$v_p = \sqrt{\frac{K_{\text{sat}} + \tfrac{4}{3}\mu}{\rho}}, \qquad
v_s = \sqrt{\frac{\mu}{\rho}}.$$

The demonstration uses a synthetic sandstone with $\phi = 0.25$,
$K_{\text{dry}} = 10\ \mathrm{GPa}$, $\mu_{\text{dry}} = 8\ \mathrm{GPa}$, on a
quartz grain ($K_{\min} = 37\ \mathrm{GPa}$, $\rho_{\min} = 2650\
\mathrm{kg\,m^{-3}}$), with brine ($K = 2.5\ \mathrm{GPa}$, $\rho = 1050\
\mathrm{kg\,m^{-3}}$) and supercritical CO2 ($K = 0.05\ \mathrm{GPa}$,
$\rho = 700\ \mathrm{kg\,m^{-3}}$):

| quantity | brine-filled | CO2-filled | change |
|---|---|---|---|
| saturated $K$ (GPa) | 14.714 | 10.106 | $-31.3\%$ |
| density ($\mathrm{kg\,m^{-3}}$) | 2250.0 | 2162.5 | $-3.9\%$ |
| $v_p$ (m/s) | 3358.6 | 3099.3 | $-7.7\%$ |
| $v_s$ (m/s) | 1885.6 | 1923.4 | $+2.0\%$ |

Two features make this signature diagnostic. First, the $v_p$ change is *large*,
because $K_{\text{fl}}$ fell by a factor of fifty: the pore fluid's
compressibility dominates the saturated bulk modulus at this porosity. Second,
$v_s$ *increases* slightly even though the rock is unchanged, because $\mu$ is
constant while $\rho$ falls. A saturation change that raised $v_p$ and $v_s$
together would be a different process (a stiffer fluid or a stiffer frame, not a
compressible one).

## 2. Impedance, reflectivity and polarity

Acoustic impedance is $Z = \rho v_p$, and the normal-incidence reflection
coefficient at an interface is $R = (Z_2 - Z_1)/(Z_2 + Z_1)$. With a chosen
caprock impedance of $7.000\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}}$, the
reservoir impedance falls from $7.5569\times10^{6}$ (brine) to
$6.7023\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}}$ (CO2), an $11.3\%$ decrease,
and

$$R_{\text{brine}} = +0.0383, \qquad R_{\text{CO2}} = -0.0217,
\qquad \Delta R = -0.0600.$$

**The reflection coefficient changes sign.** The CO2 turns a weak positive
reflection into a negative one, so the time-lapse signal contains both an
amplitude change and a **polarity flip**. That is unusually favourable: a
polarity flip is easier to detect than a change of similar size in amplitude
alone, and it is harder to produce by an artefact. It is worth stating the
assumptions, though: $R$ here is the normal-incidence value, the caprock
impedance is chosen, and the actual seismic response depends on the wavelet, the
tuning thickness and the overburden — the rock physics gives the *contrast*, not
the *seismogram*.

## 3. The gravity signature of the mass deficit

CO2 is lighter than the brine it displaces, so filling a reservoir creates a
**mass deficit**:

$$\Delta m = \left(\rho_{\text{CO2}} - \rho_{\text{brine}}\right) V
= -350\ \mathrm{kg\,m^{-3}} \times V.$$

For a compact plume modelled as a sphere at depth $d$, the surface gravity change
is approximately that of a point mass, $\Delta g = G\,\Delta m/d^{2}$, with
$G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$. The demonstration
computes it in microGal ($1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$):

| radius (m) | mass deficit (kg) | $\Delta g$ at 1200 m ($\mathrm{\mu Gal}$) | at 1800 m |
|---|---|---|---|
| 100 | $-1.466\times10^{9}$ | $-6.8$ | $-3.0$ |
| 200 | $-1.173\times10^{10}$ | $-54.4$ | $-24.2$ |
| 300 | $-3.958\times10^{10}$ | $-183.5$ | $-81.5$ |

The signal is tens of microGal for a compact plume — within reach of repeat
gravimetry, whose repeated-survey noise is taken here as
$5.0\ \mathrm{\mu Gal}$ — and it falls as $d^{2}$, so depth is the dominant
factor. Note also that the gravity signal measures the **mass** while the seismic
signal measures **contrast in elastic properties**: they are complementary
observables of the same plume, and a discrepancy between them is information
about saturation or geometry, not automatically an error.

## 4. Detection versus quantification

Split the two questions cleanly.

**(a) Detection.** Holding the plume fixed (radius $200\ \mathrm{m}$), the signal
against depth is:

| depth (m) | $|\Delta g|$ ($\mathrm{\mu Gal}$) | signal/noise | detectable at $2\times$ noise? |
|---|---|---|---|
| 800 | 122.3 | 24.46 | yes |
| 1200 | 54.4 | 10.87 | yes |
| 1800 | 24.2 | 4.83 | yes |
| 2500 | 12.5 | 2.50 | yes |
| 3500 | 6.4 | 1.28 | **no** |

Detection has a clear depth limit given the noise, and that limit is a
*falsifiable, reportable number*: below about $2500\ \mathrm{m}$ this survey can
see this plume, and below $3500\ \mathrm{m}$ it cannot. (The calculation uses the
point-mass approximation, so a real study would refine it with the actual geometry
— but the scaling and the threshold logic are exactly this.)

**(b) Quantification.** Inverting the anomaly for a mass requires the depth, and
the dependence is quadratic:

| depth error | inferred mass error |
|---|---|
| $-10\%$ | $-19.0\%$ |
| $-5\%$ | $-9.8\%$ |
| $+5\%$ | $+10.2\%$ |
| $+10\%$ | $+21.0\%$ |

A $10\%$ depth error — entirely plausible from a seismic depth conversion —
becomes a $21\%$ mass error. **The mass estimate is only as good as the
geometric model, and the geometric model is not measured by the gravity data.**
This is the non-uniqueness of potential-field data appearing in its practical
form: a deeper, denser deficit produces the same anomaly as a shallower, lighter
one.

**(c) Leakage.** A leak is a *mass movement*, not a mass change, so it is a harder
target: the demonstration takes $1\%$ of the plume's mass and places it at
$100\ \mathrm{m}$ depth, giving a deficit of $1.17\times10^{8}\ \mathrm{kg}$ and
an anomaly of $78.3\ \mathrm{\mu Gal}$ — large, but from a very shallow source,
where it is easily confused with near-surface hydrology, soil moisture, or
instrument drift. A deep leak moving the same mass would be far smaller and
compete directly with the survey noise. The honest framing is that **the same
instrumental sensitivity that detects the plume at depth is overwhelmed by
near-surface mass variability when looking for small leaks shallowly.**

## 5. What monitoring measures and what it must report

| Category | Content |
|---|---|
| Measured | reflection amplitudes and travel times; gravity differences; microseismic arrivals; well pressures and temperatures |
| Inferred | presence of CO2, saturation, spatial distribution, mass |
| Assumed | the rock-physics model and its applicability; caprock properties; plume geometry; fluid density at reservoir conditions; depth |

A defensible monitoring statement therefore reports:

1. the **detection threshold** (the smallest anomaly the survey can see at a
   stated noise level), separately from any mass estimate;
2. the **observed anomaly** with its uncertainty;
3. the **quantification** with the geometric and rock-physics assumptions named,
   and a sensitivity of the result to each (the $2\times$ depth amplification is
   the first entry);
4. the **independent checks** — seismic and gravity together constrain saturation
   and geometry better than either alone;
5. the **caveat about shallow sources** for leakage detection.

## 6. Assumptions and regime of validity

1. **Gassmann's assumptions.** The rock is isotropic and microscopically
   homogeneous, the pore fluid is well mixed and at frequencies low enough for
   pressure to equilibrate (the "Gassmann limit"); at seismic frequencies this
   usually holds, but patchy saturation and heavy oil break it.
2. **Drained (dry) frame moduli are known.** They are derived from velocities
   measured at some saturation, so a substitution is only as good as the
   inversion that produced the dry frame.
3. **Fluid properties at reservoir conditions.** $K$ and $\rho$ of supercritical
   CO2 vary strongly with pressure and temperature; a single chosen pair is a
   simplification.
4. **Geometry.** The point-mass (or simple-shape) gravity model assumes a compact
   source and ignores the surrounding structure; it is adequate for scaling and
   threshold statements, not for a mass estimate.
5. **Repeatability.** Time-lapse interpretation requires that non-repeatable
   noise (source, receivers, near-surface) be small compared with the signal; the
   $5\ \mathrm{\mu Gal}$ noise is a chosen value.
6. **Microseismic detection is an operating point.** As in
   [16-09-01](01-seismic-monitoring-climate.md), a microseismic catalogue's rate
   is a function of the network and its threshold, not a property of the
   reservoir.
7. **Monitoring is not verification of a global budget.** A site's mass balance is
   a local statement; integrating it into a climate accounting framework carries
   its own assumptions.

## 7. Python demonstration

[`code/geophysics_carbon_storage_demo.py`](code/geophysics_carbon_storage_demo.py)
runs the whole chain and prints labelled results with units. It:

1. performs the Gassmann substitution for brine and CO2 and reports moduli,
   densities and velocities;
2. computes impedances and reflection coefficients and identifies the polarity
   flip;
3. computes the gravity anomaly of the plume's mass deficit against depth and
   radius;
4. separates detection from quantification, with the depth-error amplification
   and a leakage case;
5. states what is measured, inferred and assumed.

Every number in this lesson is printed by that demonstration, or is the standard
constant $G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$.

## Mastery checkpoint

> The demonstration's synthetic sandstone has $\phi = 0.25$,
> $K_{\text{dry}} = 10\ \mathrm{GPa}$, $\mu_{\text{dry}} = 8\ \mathrm{GPa}$, with
> brine ($K = 2.5\ \mathrm{GPa}$, $\rho = 1050$) and CO2 ($K = 0.05\ \mathrm{GPa}$,
> $\rho = 700$).
>
> **(a)** State why the shear modulus does not change under fluid substitution and
> what that implies for $v_s$.
> **(b)** The saturated $K$ falls from $14.714$ to $10.106\ \mathrm{GPa}$ while the
> density falls only $3.9\%$. Compute, in words, why $v_p$ falls more than density
> does.
> **(c)** $R$ changes from $+0.0383$ to $-0.0217$. Explain why a polarity flip is
> more diagnostic than an equal-sized purely positive change.
> **(d)** A plume has a mass deficit of $-1.173\times10^{10}\ \mathrm{kg}$ at
> $1800\ \mathrm{m}$. Compute the gravity anomaly with
> $G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and state its
> depth scaling.
> **(e)** A $10\%$ depth error changes the inferred mass by $21\%$. Explain the
> factor of two and name the assumption that makes it relevant.
> **(f)** State the difference between what a seismic survey detects and what it
> quantifies, for CO2 in a reservoir.

## Common pitfalls

1. **Reporting a mass without the geometry assumptions.** A $10\%$ depth error
   gave a $21\%$ mass error.
2. **Treating detection and quantification as the same claim.** Detection is
   robust; quantification is conditional.
3. **Applying Gassmann outside its regime.** Patchy saturation and high-frequency
   (ultrasonic) measurements violate the low-frequency limit.
4. **Using a single fluid modulus and density for supercritical CO2.** Both vary
   strongly with pressure and temperature.
5. **Reading a polarity flip as a processing artefact.** It is the expected
   signature — which is why it requires careful, repeatable processing to trust.
6. **Assuming a shallow leak is easy to detect because it is close.** Shallow
   anomalies compete with near-surface noise and drift.
7. **Quoting a microseismic event rate without the network's detection
   threshold.**

## Related modules

- [16-09-02 Geodesy for Sea Level, Ice Mass and Water Storage](02-geodesy-climate.md) —
  the same gravity logic applied to ice and water.
- [16-09-01 Seismic and Geodetic Monitoring of Cryosphere Change](01-seismic-monitoring-climate.md) —
  the detection-versus-resolution discipline in a different monitoring context.
- [16-09-03 Borehole Temperature Records of Past Climate](03-geothermal-climate-records.md) —
  another inversion whose answer depends on assumptions, not just data.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  the full theory of fluid substitution and effective media.
- [11-03 Hydrocarbon Exploration Geophysics](../../11-exploration-geophysics/03-hydrocarbon-exploration/README.md) —
  the reservoir-characterisation and 4-D seismic practice this monitoring
  inherits.
- [07-02 Gravity Instruments and Surveys](../../07-gravity-geodesy/02-gravity-instruments-and-surveys/README.md) —
  the microgal-level repeat gravimetry the mass estimates require.

## Self-assessment checklist

- [ ] I can apply Gassmann substitution and compute $v_p$, $v_s$ and $\rho$.
- [ ] I can explain the CO2 velocity signature and its diagnostic value.
- [ ] I can compute a reflection coefficient and identify a polarity flip.
- [ ] I can compute a plume's gravity anomaly and state its depth scaling.
- [ ] I can separate detection from quantification and quantify a depth-error
      amplification.
- [ ] I can write a monitoring statement with measured, inferred and assumed
      quantities labelled.
