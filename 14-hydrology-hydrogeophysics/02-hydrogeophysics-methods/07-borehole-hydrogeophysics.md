---
id: 14-02-07
title: "Borehole Geophysics for Aquifer Characterisation"
level: graduate
prereqs: ["14-02-01", "14-01-02", "05-08-07"]
tags: [hydrogeophysics, borehole-geophysics, logging, flowmeter, packer-test, temperature-log, sdr]
---

# Borehole Geophysics for Aquifer Characterisation

A borehole is the only place where a geophysical measurement and a hydrological
measurement share the same volume of rock. That single fact makes borehole
geophysics the calibration layer of the whole subject: surface methods give
continuity, boreholes give truth. This lesson assembles a synthetic log suite,
interprets it for the quantities a hydrogeologist needs — clay content, porosity,
saturation, permeability and transmissivity — and then adds the three borehole
measurements that no surface method can replace: the flowmeter, the temperature
log, and the packer test.

Two themes run through it. First, **each log measures one thing well and several
things badly**, so the interpretation is the agreement between them; a unit where
the density and NMR porosities disagree is telling you something (gas, clay, or a
bad hole). Second, **permeability is not porosity**, and the NMR log is the
wireline measurement that separates them.

The logging-tool physics and the log-interpretation workflow are in
[05-08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md);
this lesson applies them to aquifers and connects them to the surface methods of
this module.

**All models and data in this module are SYNTHETIC.** Every log, unit, test result
and calibration constant below is an invented teaching value. No real borehole,
log or field test is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** a log suite from stated unit properties and **compute** the
   synthetic gamma, resistivity, density and NMR responses.
2. **Interpret** clay volume from gamma, porosity from density, and **verify** the
   porosity against an independent NMR measurement.
3. **Invert** Archie's law for water saturation and **rank** the three
   uncertainties (cementation exponent, porosity, water resistivity) by their
   effect.
4. **Compute** permeability from an NMR $T_2$ log with the SDR model and
   **integrate** it into a transmissivity, identifying which units contribute.
5. **Interpret** a flowmeter profile, **check** its closure, and **state** what it
   adds that no log can.
6. **Derive** the advection-perturbed geothermal gradient and **use** a temperature
   log as a vertical-flow detector.
7. **Compute** formation conductivity from a packer test and **state** the
   assumption that dominates its uncertainty.
8. **Design** a borehole programme for a stated hydrogeological question, naming
   the log or test that answers each part.

## Prerequisites

- [14-02-01 ERT for Aquifer Characterisation and Salinity Mapping](01-ert-for-hydrology.md)
  — where the surface measurement needs the calibration a borehole provides.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md)
  — porosity, specific yield and permeability, the quantities being logged.
- [05-08-07 Log Interpretation, Petrophysics and Uncertainty](../../05-core-geophysics/08-geophysical-logging/07-log-interpretation.md)
  — the general workflow and uncertainty budget this lesson specialises.

---

## 1. A synthetic log suite

The demonstration's stratigraphy, with each unit's density porosity, clay volume,
NMR relaxation time and water resistivity:

| unit | depth (m) | $\phi$ | $V_{\text{clay}}$ | $T_2$ (ms) | $R_w$ ($\Omega$ m) |
|---|---|---|---|---|---|
| sand (unsaturated) | 0–6 | 0.30 | 0.12 | 25.0 | 25.0 |
| sand aquifer | 6–24 | 0.32 | 0.05 | 90.0 | 20.0 |
| silty aquitard | 24–32 | 0.38 | 0.45 | 12.0 | 15.0 |
| sand aquifer | 32–48 | 0.30 | 0.08 | 60.0 | 18.0 |
| clay basement | 48–60 | 0.42 | 0.85 | 5.0 | 10.0 |

Each log is generated from those properties by a stated response function
($\mathrm{GR} = 30 + 150\,V_{\text{clay}}$ in API,
$R_t = R_w/\phi^{2}$ for a fully saturated unit,
$\rho_b = (1-\phi)\rho_{\text{matrix}} + \phi\rho_w$ with
$\rho_{\text{matrix}} = 2650\ \mathrm{kg\,m^{-3}}$, NMR amplitude $\propto \phi$ and
$T_2$ from the pore size), with 2% noise added.

| $z$ (m) | GR (API) | $R_t$ ($\Omega$ m) | $\rho_b$ (kg m$^{-3}$) | $T_2$ (ms) | unit |
|---|---|---|---|---|---|
| 3 | 48.0 | 277.8 | 2155 | 25.0 | sand (unsaturated) |
| 10 | 37.5 | 195.3 | 2122 | 90.0 | sand aquifer |
| 20 | 37.5 | 195.3 | 2122 | 90.0 | sand aquifer |
| 28 | 97.5 | 103.9 | 2023 | 12.0 | silty aquitard |
| 40 | 42.0 | 200.0 | 2155 | 60.0 | sand aquifer |
| 52 | 157.5 | 56.7 | 1957 | 5.0 | clay basement |

**The suite is deliberately redundant.** Gamma gives clay, density gives total
porosity, resistivity plus porosity gives saturation, and NMR gives water content
and pore size. Redundancy is the point: it is what makes an interpretation
checkable.

## 2. Interpretation, and the cross-check that validates it

With the stated linear gamma mapping $V_{\text{clay}} = (\mathrm{GR}-30)/150$ and
the density relation $n = (\rho_{\text{matrix}} - \rho_b)/(\rho_{\text{matrix}} -
\rho_w)$, over six depths:

| $z$ (m) | $V_{\text{clay}}$ (gamma) | $\phi$ (density) | $\phi$ (NMR) | difference |
|---|---|---|---|---|
| 3 | 0.11 | 0.2972 | 0.2959 | $+0.0013$ |
| 10 | 0.07 | 0.3289 | 0.3187 | $+0.0101$ |
| 20 | 0.06 | 0.3103 | 0.3208 | $-0.0105$ |
| 28 | 0.47 | 0.3878 | 0.3701 | $+0.0177$ |
| 40 | 0.05 | 0.3012 | 0.3042 | $-0.0030$ |
| 52 | 0.85 | 0.4214 | 0.4140 | $+0.0074$ |

The recovered clay volumes track the true values (0.12, 0.05, 0.05, 0.45, 0.08,
0.85) to within the 2-API noise, which is what a correctly scaled gamma mapping
must do. **A mismatched scale between the response function and the inversion
saturates the estimate at 0 and 1** — an artefact that looks like a real
shaly-sand interpretation and is purely arithmetic.

The rms density-minus-NMR porosity difference is **0.0099**, i.e. 3.3% of a typical
porosity, consistent with the injected noise. That agreement is the check that
justifies using either porosity alone; a *systematic* offset would instead indicate
gas (NMR < density), a shaly-sand effect, or a washed-out hole. **Always run the
cross-check before building on a log.**

## 3. Water saturation, and which uncertainty dominates

The synthetic aquifer at 6–24 m has $\phi = 0.32$, $R_w = 20\ \Omega$ m and a true
water saturation of **0.75** (a capillary zone above a water table at 6 m). Archie's
forward relation gives the logged resistivity:
$R_t = R_w/(\phi^{2}S_w^{2}) = 347.2\ \Omega$ m.

Inverting with the wrong assumptions:

| assumption changed | value | $S_w$ recovered | error |
|---|---|---|---|
| $m = 1.8$ | | 0.669 | $-10.8\%$ |
| $m = 2.0$ (correct) | | 0.750 | $0.0\%$ |
| $m = 2.2$ | | 0.841 | $+12.1\%$ |
| $\phi = 0.28$ | | 0.857 | $+14.3\%$ |
| $\phi = 0.32$ (correct) | | 0.750 | $0.0\%$ |
| $\phi = 0.36$ | | 0.667 | $-11.1\%$ |
| $R_w = 10\ \Omega$ m | | 0.530 | $-29.3\%$ |
| $R_w = 20\ \Omega$ m (correct) | | 0.750 | $0.0\%$ |
| $R_w = 40\ \Omega$ m | | 1.000* | $+33.3\%$ |

(*clipped at saturation — and that clipping is itself diagnostic: **a log that
reports full saturation almost always has the wrong $R_w$**, because a genuinely
saturated sand is rare and a mis-estimated water resistivity is common.)

$S_w$ scales as $R_w^{-1/2}$, so a factor of two in $R_w$ moves $S_w$ by
$1/\sqrt{2} = 0.71$ or 1.41. Porosity and $m$ enter with comparable weight. But
only $R_w$ is fixed by a *measurement* — a water sample — while $\phi$ and $m$ are
model choices. **The water sample is worth more than the log quality**, which is
why a hydrogeophysical borehole programme must include sampling, not just logging.

## 4. Permeability from NMR, and the transmissivity

The SDR relation converts the NMR log into permeability:

$$k = C\,\phi^{4}\,T_2^{2},$$

with $C$ a **calibration constant** (here a stated synthetic
$C = 4.0 \times 10^{-9}$ in SI units, m² s$^{-3}$ per unit $\phi^4 T_2^2$).

| unit | $\phi$ | $T_2$ (ms) | $k$ (m²) | $k$ (m/s) | $k$ (m/d) | $T$ over the unit (m²/s) |
|---|---|---|---|---|---|---|
| sand (unsaturated) | 0.30 | 25 | $2.03 \times 10^{-14}$ | $1.98 \times 10^{-7}$ | 0.017 | $1.19 \times 10^{-6}$ |
| sand aquifer | 0.32 | 90 | $3.40 \times 10^{-13}$ | $3.33 \times 10^{-6}$ | 0.287 | $5.99 \times 10^{-5}$ |
| silty aquitard | 0.38 | 12 | $1.20 \times 10^{-14}$ | $1.18 \times 10^{-7}$ | 0.010 | $9.41 \times 10^{-7}$ |
| sand aquifer | 0.30 | 60 | $1.17 \times 10^{-13}$ | $1.14 \times 10^{-6}$ | 0.099 | $1.83 \times 10^{-5}$ |
| clay basement | 0.42 | 5 | $3.11 \times 10^{-15}$ | $3.05 \times 10^{-8}$ | 0.003 | $3.66 \times 10^{-7}$ |

**Total transmissivity $T = 8.06 \times 10^{-5}\ \mathrm{m^2\,s^{-1}}
= 6.97\ \mathrm{m^2\,d^{-1}}$.**

Look at the ordering, because it is the lesson: the 18 m aquifer with
$T_2 = 90$ ms supplies 5.17 of the 6.97 m² d$^{-1}$, while the **silty aquitard —
with the second-largest porosity in the suite (0.38) — supplies 0.08**, because
its short $T_2$ says its pores are small. **Porosity is not transmissivity**, and
NMR is the wireline measurement that separates them.

Two cautions. The $k$ conversion used
$k = K\mu_w/(\rho_w g)$ with $\mu_w = 1.002 \times 10^{-3}$ Pa s; and the absolute
values depend entirely on $C$, which must be fixed against a core measurement or a
pumping test ([14-01-04](../01-hydrology-fundamentals/04-well-hydraulics.md)). The
*ratios* between units come from the log without calibration.

## 5. The flowmeter: where the water actually enters

A spinner survey during pumping records the cumulative flow upward through the
borehole. Differencing it gives the inflow at each depth:

| depth (m) | flow (L s$^{-1}$) | incremental inflow (L s$^{-1}$) |
|---|---|---|
| 5 | 0.05 | 0.00 |
| 10 | 0.35 | 0.30 |
| 16 | 1.80 | 1.45 |
| 22 | 3.10 | 1.30 |
| 30 | 3.35 | 0.25 |
| 38 | 4.85 | 1.50 |
| 46 | 5.00 | 0.15 |

Closure: the increments sum to 4.950 L s$^{-1}$ against a pumped 5.00 L s$^{-1}$
(1.0% error). **61% of the total inflow enters between 10 and 22 m**, confirming
the log interpretation's assignment of the productive interval.

The flowmeter answers a question no other measurement answers: *which* interval
produces water, and in what proportion. A log can say an interval has high
permeability; only a flowmeter says whether the well actually draws from it (it may
not, if a shallower or deeper unit has lower head or higher conductivity in the
screen). It is the direct check on an interpretation and on a well design.

## 6. Temperature, and what a cross-hole measurement sees

In steady state with a vertical Darcy velocity, heat conduction and advection
balance:

$$k_{\text{th}}\frac{\mathrm{d}^{2}T}{\mathrm{d}z^{2}}
= \rho_w c_w v_z \frac{\mathrm{d}T}{\mathrm{d}z}
\qquad\Longrightarrow\qquad
T(z) = T_0 + G\,z^{*}\left(1 - e^{-z/z^{*}}\right),
\qquad z^{*} = \frac{k_{\text{th}}}{\rho_w c_w v_z},$$

with $G$ the undisturbed geothermal gradient and $z^{*}$ the depth over which
advection suppresses the gradient. With $k_{\text{th}} = 2.0\
\mathrm{W\,m^{-1}\,K^{-1}}$, $\rho_w c_w = 4.18 \times 10^{6}\
\mathrm{J\,m^{-3}\,K^{-1}}$, $T_0 = 12.0\ ^\circ$C and $G = 0.025\
^\circ$C m$^{-1}$:

| $v_z$ (m s$^{-1}$) | $z^{*}$ (m) | $T$ at 20 m (°C) | $T$ at 50 m | gradient at 20 m (°C m$^{-1}$) |
|---|---|---|---|---|
| 0 | $\infty$ | 12.500 | 13.250 | 0.0250 |
| $10^{-9}$ | 478 | 12.490 | 13.187 | 0.0240 |
| $10^{-8}$ | 47.9 | 12.409 | 12.775 | 0.0165 |
| $10^{-7}$ | 4.78 | 12.118 | 12.120 | 0.00038 |
| $10^{-6}$ | 0.48 | 12.012 | 12.012 | 0.00000 |

A downward Darcy velocity of $10^{-8}\ \mathrm{m\,s^{-1}}$ (0.86 mm d$^{-1}$)
reduces the gradient at 20 m by a third, and $10^{-7}$ m s$^{-1}$ suppresses it
within a few metres. **A temperature log is a sensitive vertical-flow detector that
costs nothing extra**, because it runs in the same pass as the gamma and
resistivity logs — and it is the only log that sees flow *between* boreholes as a
gradient anomaly rather than as a point measurement.

**Cross-hole measurements, and what they can and cannot see.** In a unit of
$\phi = 0.30$, a water-content change from 0.10 to 0.30 changes the radar or
seismic velocity by about 40%, so a cross-hole travel time resolves saturation
changes easily. Salinity, by contrast, leaves the permittivity almost unchanged but
raises the conductivity, so it is visible only in the **attenuation**: at 50 MHz,
using the exact lossy-dielectric attenuation with the calibration
$\sigma_w = 0.15\,\mathrm{TDS}$ [g L$^{-1}$] S m$^{-1}$,

| TDS (mg L$^{-1}$) | $\sigma_w$ (S m$^{-1}$) | $\alpha$ at 50 MHz (dB m$^{-1}$) | one-way loss over 12 m (dB) | 60 dB depth (m) |
|---|---|---|---|---|
| 500 | 0.075 | 24.6 | 295 | 2.44 |
| 5 000 | 0.750 | 102.3 | 1228 | 0.59 |
| 35 000 | 5.250 | 278.3 | 3340 | 0.22 |

**A 5 g L$^{-1}$ brine is opaque to 50 MHz radar within 0.6 m**, so cross-hole
radar cannot monitor salinity beyond very fresh contrasts: the same conductivity
that makes salinity an easy electrical target makes it an impossible radar one.
Salinity between boreholes is measured with cross-hole ERT or low-frequency EM
([09-06 Borehole Electrical Methods](../../09-electrical-em-methods/06-borehole-electrical/README.md)).

## 7. The packer test

A constant-head injection test between packers isolates a length $L$ of the hole
and drives water into the formation. For steady radial flow,

$$Q = \frac{2\pi L K\,\Delta h}{\ln(R/r_w)}
\qquad\Longrightarrow\qquad
K = \frac{Q\ln(R/r_w)}{2\pi L\,\Delta h}.$$

With $Q = 0.12\ \mathrm{L\,s^{-1}} = 1.2 \times 10^{-4}\ \mathrm{m^{3}\,s^{-1}}$,
$\Delta h = 12.0$ m, $L = 5.0$ m, $r_w = 75$ mm and an assumed
$R = 30$ m:

$$\ln(R/r_w) = \ln 400 = 5.9915, \qquad
K = \frac{1.2 \times 10^{-4} \times 5.9915}{2\pi \times 5.0 \times 12.0}
= 1.907 \times 10^{-6}\ \mathrm{m\,s^{-1}} = 0.165\ \mathrm{m\,d^{-1}},$$

and the transmissivity of the packed interval is
$T = KL = 9.54 \times 10^{-6}\ \mathrm{m^2\,s^{-1}} = 0.82\ \mathrm{m^2\,d^{-1}}$.

**The assumption that dominates.** $R$ enters only logarithmically, but it is not
zero: changing $R$ from 30 m to 120 m changes $\ln(R/r_w)$ from 5.99 to 7.38 and
$K$ by $+23\%$. State $R$, or use a method without it (a slug test's analysis has
no radius of influence, which is why slug tests are preferred in tight
formations). The other assumptions — a homogeneous, isotropic, fully saturated
formation around the packed interval, and no leakage past the packers — are worth
more than the radius assumption and are tested by *repeating* the test at several
heads: a plot of $Q$ against $\Delta h$ must be linear through the origin, and a
systematic curvature indicates non-Darcy flow near the hole or a leaking packer.

## 8. Python demonstration

`code/borehole_hydrogeophysics_demo.py` prints all of the above with units. It:

1. tabulates the synthetic units and their log responses;
2. interprets clay volume, density porosity and NMR porosity, and reports the rms
   cross-check difference (0.0099, i.e. 3.3% of a typical porosity);
3. inverts Archie for $S_w$ under nine assumption changes and ranks their effect
   ($R_w$ the largest, with the saturation clipping as a diagnostic);
4. computes SDR permeability for five units, integrates to
   $T = 6.97\ \mathrm{m^2\,d^{-1}}$, and shows the silty aquitard contributing
   0.08 m² d$^{-1}$ despite the second-largest porosity;
5. interprets a flowmeter profile, closing to 1.0% and locating 61% of the inflow
   between 10 and 22 m;
6. solves the advection-perturbed geothermal profile over five Darcy velocities and
   tabulates the cross-hole travel-time and attenuation sensitivities to water
   content and salinity;
7. computes a packer test ($K = 1.91 \times 10^{-6}$ m s$^{-1}$) and quantifies the
   radius-of-influence sensitivity;
8. verifies the density-porosity inversion (exact to $0.00 \times 10^{0}$), the
   temperature solution against its ODE (relative residual $7.3 \times 10^{-7}$,
   limited by the finite difference), and flowmeter closure.

```bash
cd 14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python borehole_hydrogeophysics_demo.py
```

## 9. Assumptions and regime of validity

1. **The log response functions are simplified linear or power laws.** Real gamma
   responses depend on the clay *type* and on potassium feldspar; a
   gamma-derived clay volume saturates at both ends, as the demonstration's noisy
   values show.
2. **Archie's law applies.** A clay-bearing unit needs a shaly-sand model; the
   silty aquitard in this suite would not be interpretable with a clean-sand
   Archie relation at all.
3. **The density-porosity relation needs the right matrix and fluid densities.**
   A wrong $\rho_{\text{matrix}}$ (heavy minerals, coal, anhydrite) biases the
   porosity linearly, and the error appears as a disagreement with NMR rather than
   as an obviously wrong number.
4. **The SDR relation requires calibration.** $C$ is site- and lithology-specific;
   an uncalibrated $C$ gives correct ratios and wrong magnitudes.
5. **Borehole logs measure the invaded zone in a permeable unit.** Drilling-fluid
   invasion alters the resistivity and can displace the NMR water; the shallow
   resistivities are the least reliable in the most permeable units.
6. **The temperature model is one-dimensional and steady.** Transient
   borehole-disturbance effects (drilling, circulation) last days to weeks, and
   lateral flow produces two-dimensional patterns that a 1-D model misreads.
7. **Flowmeter measurements assume steady radial inflow at each depth** and no
   vertical flow behind casing; the spinner's calibration and its sensitivity to
   borehole diameter must be stated.
8. **The packer test assumes steady, saturated, single-phase radial flow** in a
   homogeneous medium. Fractured rock gives an effective $K$ that depends on
   whether the packed interval intersects a fracture — the same scale problem as
   [14-01-02 §7](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md).

## Mastery checkpoint

A synthetic borehole programme must characterise a two-aquifer system for a new
supply well.

**(a)** The gamma log reads 45, 60 and 190 API in three units. Using
$V_{\text{clay}} = (\mathrm{GR}-30)/150$, compute the clay volume of each and state
which unit is the most likely confining layer. **(b)** Density logs give bulk
densities of 2130, 2200 and 2450 kg m$^{-3}$. Using
$\rho_{\text{matrix}} = 2650$ and $\rho_{\text{water}} = 1000\
\mathrm{kg\,m^{-3}}$, compute the three porosities. **(c)** The resistivity log
reads 220, 95 and 18 $\Omega$ m in the same units with $R_w = 5\ \Omega$ m (a
synthetic teaching value fixed by a water sample);
compute the water saturation from Archie with $m = n = 2$ and comment on the
third value. **(d)** The NMR $T_2$ values are 85, 18 and 4 ms. Using
$k = C\phi^{4}T_2^{2}$ with $C = 4.0 \times 10^{-9}$, compute the three
permeabilities in m s$^{-1}$ and state which unit should be screened. **(e)** A
packer test in the best unit gives $Q = 0.08\ \mathrm{L\,s^{-1}}$ at
$\Delta h = 10$ m over $L = 3$ m with $R = 50$ m and $r_w = 75$ mm. Compute $K$.
**(f)** State the one measurement you would add to confirm that the screened
interval is the one actually producing water.

## Common pitfalls

1. **Building a permeability estimate on a porosity log.** The silty unit here has
   the second-highest porosity and almost no transmissivity.
2. **Accepting $S_w = 1$.** It usually means the wrong $R_w$, not a saturated
   aquifer.
3. **Skipping the density-versus-NMR porosity cross-check.** It is the cheapest
   available early warning of gas, shale or hole problems.
4. **Using an uncalibrated SDR constant as an absolute permeability.** Calibrate
   against a core or a pumping test, or report ratios only.
5. **Quoting an uncalibrated flowmeter profile.** The spinner's calibration and
   the borehole diameter must be stated.
6. **Reading a vertical-flow velocity from an uncorrected temperature gradient.**
   Separate the background geothermal gradient from the advective perturbation.
7. **Forgetting the radius-of-influence assumption in a packer test.** It is
   logarithmic but not negligible (23% in the lesson's example).
8. **Expecting radar to see salinity between boreholes.** A few g L$^{-1}$ is
   opaque; use ERT or low-frequency EM.

## Related modules

- [05-08 Geophysical Logging](../../05-core-geophysics/08-geophysical-logging/README.md) —
  the tools, the environment and the interpretation workflow.
- [09-06 Borehole Electrical Methods](../../09-electrical-em-methods/06-borehole-electrical/README.md) —
  cross-hole ERT and borehole radar, the subsurface geophysics of the same volume.
- [14-01-04 Well Hydraulics and Pumping Tests](../01-hydrology-fundamentals/04-well-hydraulics.md)
  — the pumping test that calibrates an SDR permeability and gives the storativity.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md)
  — the properties being logged and the scale problem they carry.
- [05 Surface NMR for Direct Water Detection](05-nmr-for-groundwater.md) — the
  surface version of the NMR measurement used in §4.
- [01 ERT for Aquifer Characterisation and Salinity Mapping](01-ert-for-hydrology.md)
  — where the borehole porosity converts an ERT section into a salinity map.

## Code and exercises

- Demonstration:
  [`code/borehole_hydrogeophysics_demo.py`](code/borehole_hydrogeophysics_demo.py)
- Exercises: [`exercises/07-borehole-hydrogeophysics-exercises.md`](exercises/07-borehole-hydrogeophysics-exercises.md)
- Worked solutions: [`exercises/07-borehole-hydrogeophysics-solutions.md`](exercises/07-borehole-hydrogeophysics-solutions.md)
