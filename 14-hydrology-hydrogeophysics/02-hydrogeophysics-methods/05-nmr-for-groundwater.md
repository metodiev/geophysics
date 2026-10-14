---
id: 14-02-05
title: "Surface NMR for Direct Water Detection"
level: research
prereqs: ["14-02-02", "14-01-06", "05-04-07"]
tags: [hydrogeophysics, surface-nmr, magnetic-resonance, water-content, larmor, t2-relaxation]
---

# Surface NMR for Direct Water Detection

Every other method in this module measures a *proxy* for water and then inverts
through a petrophysical relation: resistivity needs porosity and clay content,
seismic needs a rock-physics model, gravity needs a mass-to-water assumption.
Surface nuclear magnetic resonance is different in kind. It excites the nuclear
spins of hydrogen nuclei in water molecules and records their precession, so the
signal is generated **by the water itself**. A null result means no water, not
unfavourable porosity.

That directness buys three things and costs three things. It buys freedom from
the porosity ambiguity that dominates
[ERT](01-ert-for-hydrology.md), immunity to the conductivity that blinds
[TDEM](02-em-for-hydrology.md), and a measurement of *mobile* water — the
producible fraction — through the relaxation time. It costs signal strength, so
deployed depths are modest and resolution is poor; it costs dependence on the
Earth's field, which changes from site to site; and it costs an insensitivity to
anything that relaxes too fast to be seen.

**All models and data in this module are SYNTHETIC.** The kernel, water-content
profiles, pore sizes and synthetic soundings below are invented teaching values.
The proton gyromagnetic ratio is a CODATA constant and is stated where used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the Larmor frequency from the local magnetic field and **explain**
   why a system must be tuned to the site.
2. **Describe** the sensitivity kernel, **compute** its peak depth from the pulse
   moment, and **quantify** how the resolution degrades with depth.
3. **Build** a synthetic sounding from a water-content profile and **invert** it
   with a regularised non-negative solver.
4. **Select** the regularisation with the discrepancy principle and **state** why
   an unregularised fit to an underdetermined problem is meaningless.
5. **Compute** the detection limit for a layer at a stated depth from the noise
   level and the kernel, and explain the depth dependence.
6. **Convert** a relaxation time to a pore radius and **identify** the water that
   the measurement cannot see.
7. **Distinguish** what surface NMR determines (mobile water content and its depth
   distribution) from what it cannot (salinity, permeability without calibration,
   total porosity).

## Prerequisites

- [14-02-02 EM and TDEM for Groundwater Exploration](02-em-for-hydrology.md) —
  the diffusion and conductivity physics that surface NMR escapes, and the
  contrasting sounding logic.
- [14-01-06 The Unsaturated Zone](../01-hydrology-fundamentals/06-unsaturated-zone.md)
  — water content as a state variable, and its depth distribution.
- [05-04-07 Electrical Properties of Rock](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md)
  — the pore-scale properties that relaxivity connects to.

---

## 1. The Larmor frequency: everything is set by the local field

A proton in a magnetic field precesses at the Larmor frequency

$$f_L = \frac{\gamma}{2\pi}B, \qquad
\gamma = 2.6752218744 \times 10^{8}\ \mathrm{rad\,s^{-1}\,T^{-1}}\
\text{(CODATA)},$$

so with $B$ in nanotesla,

$$\frac{\gamma}{2\pi}B = 42.577\ \mathrm{Hz\,nT^{-1}} \times B_{\mathrm{nT}}
\ \mathrm{Hz}.$$

| $B$ (nT) | $f_L$ (kHz) |
|---|---|
| 42 000 | 1.7883 |
| 45 000 | 1.9160 |
| 48 000 | 2.0437 |
| 50 000 | 2.1289 |
| 52 000 | 2.2140 |
| 55 000 | 2.3418 |

Three practical consequences follow immediately, and they distinguish surface NMR
from every other geophysical method in this folder:

1. **The frequency is a field measurement, not a system setting.** In a location
   where the geomagnetic field varies laterally — near a magnetic anomaly, a
   basaltic intrusion or a landfill — the Larmor frequency varies across the loop,
   and the excitation bandwidth must cover that variation or the signal is
   attenuated in ways that look like a water-content change.
2. **The signal amplitude is proportional to the field, and the noise is not.** A
   high-field site (60,000 nT) has a substantially better signal-to-noise ratio
   than a low-field one (42,000 nT) for the same water and the same system.
3. **The measurement is a *magnetic* one.** Unlike resistivity and EM, it is
   almost independent of the ground's electrical conductivity, so it works in
   saline and clay-rich settings where the electrical methods fail — the sharpest
   contrast to be found anywhere in this module.

## 2. The sounding kernel

A pulse of current in a loop creates a magnetic field that tips the spins by an
angle that depends on position: **the pulse moment $q$ (amplitude × duration)
selects a depth band.** The band is described by a sensitivity kernel $K(q,z)$.
In this lesson the kernel is the stated synthetic model

$$K(q,z) = \left(\frac{z}{z_q}\right)^{2}
e^{\,1 - (z/z_q)^{2}} \cdot \frac{1}{1 + (z/z_c)^{2}},
\qquad z_q = 12\sqrt{q}\ \mathrm{[m]},\quad z_c = 25\ \mathrm{m},$$

whose first factor peaks at exactly $1$ at $z = z_q$ (its derivative vanishes
there by construction) and whose second factor is a stated loop-coupling decay.

| $q$ (A ms) | $z_{\text{peak}}$ (m) | normalized FWHM (m) | $K$ at 40 m |
|---|---|---|---|
| 0.25 | 6.00 | 7.00 | 0.0000 |
| 0.50 | 8.49 | 9.80 | 0.0000 |
| 1.00 | 12.00 | 13.90 | 0.0001 |
| 2.00 | 16.97 | 19.60 | 0.0164 |
| 4.00 | 24.00 | 27.70 | 0.1319 |
| 8.00 | 33.94 | 39.20 | 0.2644 |
| 16.00 | 48.00 | 55.40 | 0.2648 |

Two structural facts decide every design:

- **The peak depth grows as $\sqrt{q}$**, so a factor of four in pulse moment
  doubles the depth. Depth costs amplitude *squared* in the moment.
- **The width grows in proportion to the depth.** The normalized full width at
  half maximum is $1.1548\,z_q$, obtained by solving $u e^{1-u} = 0.5$ twice
  ($u = 0.2320$ and $2.6780$, giving $r = 0.4817$ and $1.6365$). **Resolution
  degrades linearly with depth**, before any consideration of signal strength —
  the verification section of the demonstration recovers this constant to the grid
  resolution (9.80 m against 9.80 m predicted at $q = 0.5$).

The measured signal for a profile $\theta(z)$ is the depth integral

$$A(q) = \int_0^\infty K(q,z)\,\theta(z)\,\mathrm{d}z,$$

which is **linear in the water content** (verified in the demonstration to a ratio
of 2.000000000 for a doubled profile). That linearity is why a bounded linear
solver is the appropriate inversion tool, and it is an idealisation: a realistic
kernel, with relaxation during the pulse and a spatially varying transmit field,
is nonlinear.

## 3. A synthetic sounding and its inversion

**Synthetic profile** (four units):

| 0–10 m | 10–25 m | 25–45 m | 45–70 m |
|---|---|---|---|
| $\theta = 0.05$ | $\theta = 0.25$ | $\theta = 0.08$ | $\theta = 0.20$ |

Seven pulse moments (0.25 to 16 A ms) give the modelled amplitudes 0.581, 1.430,
2.727, 3.820, 4.532, 6.208, 9.711 (arbitrary units). With 2% noise added
($\sigma = 0.0504$), the inverse problem has **7 data and 28 depth cells**: it is
badly underdetermined, and an unregularised fit has a misfit of 0.0000 while
returning a spiky, physically meaningless profile. The demonstration instead
minimises

$$\lVert K\theta - d\rVert^{2} + \lambda\lVert L\theta\rVert^{2},
\qquad \theta \ge 0,$$

with $L$ the first-difference operator, and selects $\lambda$ by the **discrepancy
principle** — the largest $\lambda$ whose data misfit is still consistent with the
noise:

| $\lambda$ | data misfit (rms) | water column (mm) | roughness |
|---|---|---|---|
| 0.0 | 0.0000 | 10 691 | 0.0334 |
| 0.2 | 0.0027 | 10 884 | 0.0312 |
| 0.5 | 0.0057 | 10 941 | 0.0304 |
| 1.0 | 0.0171 | 10 901 | 0.0285 |
| **2.0** | **0.0516** | **10 592** | **0.0234** |
| 3.0 | 0.0863 | 10 292 | 0.0187 |
| 5.0 | 0.1361 | 10 071 | 0.0125 |
| 20.0 | 0.2500 | 11 067 | 0.0022 |

$\lambda = 2.0$ gives a data misfit of 0.0516 against $\sigma = 0.0504$ ✓.
The recovered profile:

| depth (m) | true $\theta$ | inverted $\theta$ |
|---|---|---|
| 5 | 0.05 | 0.065 |
| 15 | 0.25 | 0.254 |
| 20 | 0.25 | 0.223 |
| 30 | 0.08 | 0.114 |
| 40 | 0.08 | 0.102 |
| 55 | 0.20 | 0.159 |
| 65 | 0.20 | 0.181 |

**Water column: 10 725 mm true against 10 592 mm inverted ($-1.2\%$); layer
average in the 10–25 m unit: 0.25 true against 0.222.** The robust products are
the integrals; the sharp boundaries are not recovered and should be reported as
conditional on the regularisation. This is the same lesson as
[ERT](01-ert-for-hydrology.md) and [TDEM](02-em-for-hydrology.md), in a different
physics: **the deliverable is a bounded family of models, not a log.**

## 4. Noise and the detection limit

With independent noise of standard deviation $\sigma$ on each sounding, the
standard error on the water content of a depth band is approximately

$$\sigma_\theta \;\approx\; \frac{\sigma}
{\sqrt{\sum_q\sum_{z \in \text{band}} K(q,z)^{2}\,\Delta z}},$$

summed over every pulse moment used. Because the kernel's amplitude falls with
depth while its width grows, the denominator grows slowly, and the detection limit
deteriorates:

| depth band (m) | $\sigma_\theta$ at $\sigma = 0.05$ | at $\sigma = 0.2$ | minimum $\theta$ at SNR = 1 |
|---|---|---|---|
| 5–10 | 0.016 | 0.064 | 0.32 |
| 10–20 | 0.013 | 0.052 | 0.26 |
| 20–30 | 0.019 | 0.078 | 0.39 |
| 30–45 | 0.027 | 0.110 | 0.55 |
| 45–60 | 0.057 | 0.228 | 1.14 |

Read the last column literally: at 45–60 m, with this system's noise, a water
content below about 1.1 (i.e. nothing physically meaningful) is undetectable in a
single sounding — **the deepest band is not measurable at all in this
configuration**, and the honest statement is a bounding depth rather than a
profile. Adding pulse moments and stacking improves the denominator, but the
kernel's depth decay sets the ceiling.

**Surface NMR is a bulk-water detector, not a high-resolution imager.** Its
natural products are: the total water column, the depth range within which water
is present, and the mobile-water fraction. Attempting a well-log-like profile from
a sounding is the most common over-claim in the method's literature.

## 5. Relaxation: the water that is invisible

The measured signal decays as $e^{-t/T_2^{*}}$, and for water in a pore

$$\frac{1}{T_2} = \rho_2\frac{S}{V} = \frac{3\rho_2}{r}
\quad \text{for a sphere}
\qquad\Longrightarrow\qquad
T_2 = \frac{r}{3\rho_2},$$

with $\rho_2$ the **surface relaxivity** [m s$^{-1}$], a property of the mineral
surface. With a stated synthetic $\rho_2 = 20\ \mathrm{\mu m\,s^{-1}}$
(note: $20 \times 10^{-6}$ m/s):

| pore radius (µm) | $T_2$ (ms) | visible with a 2.3 ms echo time? |
|---|---|---|
| 0.005 | 0.083 | no |
| 0.020 | 0.333 | no |
| 0.050 | 0.833 | no |
| 0.140 | 2.333 | yes (the threshold value) |
| 0.500 | 8.333 | yes |
| 2.0 | 33.33 | yes |
| 10 | 166.7 | yes |
| 100 | 1667 | yes |

With a 2.3 ms echo time (a typical value for a shallow system) the shortest
resolvable $T_2$ is about 2.3 ms, corresponding to a pore radius of

$$r_{\min} = 3\rho_2 \times 2.3\ \mathrm{ms} = 0.14\ \mathrm{\mu m}.$$

**Water in pores smaller than about 0.14 µm is invisible.** That is exactly the
clay-bound and capillary-water regime, so:

- A surface-NMR water content is a **mobile-water content**, systematically lower
  than a gravimetric or neutron-log total, and the difference is diagnostic rather
  than an error.
- In a clay-rich unit the NMR water content can be a small fraction of the total,
  which is *correct* for a water-supply question but wrong for a mass-balance
  question. Say which one you are answering.
- The ratio of NMR mobile water to a total-porosity measurement is the practical
  proxy for **specific yield** ([14-01-02 §2](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md)),
  which is otherwise very hard to measure.

## 6. What surface NMR determines, and what it does not

| Quantity | Determined? | Why |
|---|---|---|
| depth distribution of mobile water | **yes**, with the resolution of §2 | the signal is water |
| water column (integrated content) | **yes**, to a few per cent in favourable settings | linear in $\theta$, verified |
| mobile-water fraction | **yes**, from the $T_2$ spectrum | fast-relaxing water is excluded |
| rough pore size | **yes**, but only through $\rho_2$ | $T_2 = r/(3\rho_2)$ needs a calibrated $\rho_2$ |
| permeability | **only with calibration** | a $T_2$-based estimate (SDR or Coates) has a site-specific constant |
| salinity | **no** | dissolved ions change nothing about the proton resonance |
| total porosity | **no** | bound water is invisible |
| hydraulic head or gradient | **no** | it is not a potential measurement |

The salinity row is the deepest contrast in this module: at the same site,
resistivity and EM are sensitive to salinity and blind to the difference between
water and clay, while surface NMR is blind to salinity and directly sensitive to
water. That complementarity is the argument for a combined survey, not a
competition.

## 7. Python demonstration

`code/nmr_for_groundwater_demo.py` prints all of the above with units. It:

1. tabulates the Larmor frequency over six fields and verifies its exact
   linearity in $B$ (ratio 2.000000 at doubled field);
2. tabulates the kernel over seven pulse moments, reporting the peak depth, the
   normalized FWHM and the amplitude at 40 m, and verifies the peak location
   (8.50 m measured against 8.49 m predicted) and the FWHM constant
   (1.1548 $z_q$, derived by solving $ue^{1-u} = 0.5$);
3. builds a synthetic sounding over a four-unit profile;
4. inverts it with Tikhonov regularisation and a non-negativity bound, selecting
   $\lambda = 2.0$ by the discrepancy principle and recovering the water column to
   $-1.2\%$;
5. tabulates the detection limit by depth band, showing the deepest band to be
   unmeasurable;
6. converts $T_2$ to pore radius and identifies the 0.14 µm invisibility
   threshold;
7. verifies the forward model's linearity in water content (2.000000000).

```bash
cd 14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python nmr_for_groundwater_demo.py
```

## 8. Assumptions and regime of validity

1. **The kernel is a stated model, not a full solution.** A real kernel requires
   the transmit and receive fields of a specific loop, the pulse envelope, the
   relaxation during the pulse, and the off-resonance effect of field
   inhomogeneity. The *scalings* used here ($z_q \propto \sqrt{q}$, width
   $\propto z_q$, amplitude decaying with depth) are the physical content; the
   constants are illustrative.
2. **Linear in water content.** True for the NMR excitation at a single
   frequency; violated where the field varies across the loop so that part of the
   water is off-resonance.
3. **$T_2 = r/(3\rho_2)$ assumes isolated, spherical, water-filled pores with a
   single relaxivity.** Real rocks have a distribution of pore sizes, a
   distribution of relaxivities, and diffusive coupling between pores; the $T_2$
   spectrum is therefore only a *proxy* for pore size, not a measurement of it.
4. **The echo time sets the invisibility threshold.** A long echo time (a
   larger loop, deeper target, noisier site) hides more water; quoting a water
   content without the echo time is not reproducible.
5. **Assumption of a single magnetic resonance species.** Free water, and
   hydrocarbons if present, both contribute; a survey over a contaminated site must
   state how that is handled.
6. **Noise is additive, Gaussian and independent across pulse moments.** Real
   noise is dominated by environmental electromagnetic noise, which is
   *correlated* between moments and often the limiting factor; that makes the
   detection limits here optimistic.
7. **The water is in pores and connected.** Water in fractures and conduits
   relaxes slowly and is measured, but its volume may be a tiny fraction of the
   bulk, so a fracture aquifer can be productive and nearly invisible at once.

## Mastery checkpoint

A synthetic site has $B = 50\ 000\ \mathrm{nT}$ and a target aquifer of
$\theta = 0.18$ between 20 and 35 m depth, with 2% of the peak signal as noise
($\sigma = 0.05$ in the units of §4).

**(a)** Compute the Larmor frequency. **(b)** Compute the pulse moment whose
kernel peaks at 27 m, and state the normalized FWHM at that moment. **(c)** Using
the §4 detection-limit scaling, state whether this aquifer is resolvable at 1σ and
at 2σ, and compute the water column in the aquifer. **(d)** The same unit is
measured by a neutron log as $\theta_{\text{total}} = 0.26$. Compute the
invisible fraction and state two distinct physical explanations. **(e)** A
colleague proposes to map salinity in the same unit with surface NMR. Explain in
two sentences why that cannot work, and name the method that can.

## Common pitfalls

1. **Assuming the Larmor frequency.** It is a field measurement that varies
   laterally and in time; a mistuned system loses signal that looks like dry ground.
2. **Reporting a profile without the regularisation and the misfit.** The water
   column is robust; the layer boundaries are not.
3. **Ignoring the resolution degradation with depth.** The kernel's width grows in
   proportion to its depth.
4. **Forgetting the echo time.** It sets which water is invisible, so it belongs in
   every water-content statement.
5. **Calling NMR water content "porosity".** It is mobile water.
6. **Expecting salinity sensitivity.** Dissolved ions are invisible to the proton
   resonance.
7. **Treating $T_2$-derived pore size as measured.** It is calibrated through
   $\rho_2$.
8. **Assuming the noise is independent.** Environmental noise is correlated and
   usually dominates, making the detection limits optimistic.

## Related modules

- [02 EM and TDEM for Groundwater Exploration](02-em-for-hydrology.md) — the
  conductivity-limited alternative.
- [01 ERT for Aquifer Characterisation and Salinity Mapping](01-ert-for-hydrology.md) —
  the porosity-limited alternative, and the method that *does* see salinity.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md)
  — specific yield, which the mobile-water fraction estimates.
- [07 Borehole Geophysics for Aquifer Characterisation](07-borehole-hydrogeophysics.md) —
  the borehole NMR log that calibrates and extends the surface measurement.
- [05-04-07 Electrical Properties of Rock](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md)
  — pore-scale properties, including surface relaxivity's mineral dependence.
- [03 Geophysical Data Assimilation in Hydrology](../05-hydrogeophysical-monitoring/03-geophysical-data-assimilation-hydrology.md)
  — how a sounding becomes a hydrological model constraint.

## Code and exercises

- Demonstration: [`code/nmr_for_groundwater_demo.py`](code/nmr_for_groundwater_demo.py)
- Exercises: [`exercises/05-nmr-for-groundwater-exercises.md`](exercises/05-nmr-for-groundwater-exercises.md)
- Worked solutions: [`exercises/05-nmr-for-groundwater-solutions.md`](exercises/05-nmr-for-groundwater-solutions.md)
