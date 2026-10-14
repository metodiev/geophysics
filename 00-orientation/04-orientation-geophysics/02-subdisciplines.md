---
id: 00-04-02
title: "The Subdisciplines and What Each One Measures"
level: beginner
prereqs: ["00-04-01"]
estimated_minutes: 45
tags: [geophysics, subdisciplines, methods, sensitivity]
---

# The Subdisciplines and What Each One Measures

## Learning objectives

- For each major subdiscipline, state the physical property it senses, the
  physical mechanism that makes the measurement possible, and its typical depth
  and resolution limits.
- Explain why two methods that "see the same rocks" give different information,
  and how that difference is used deliberately.
- Compute a skin depth and a radar velocity, and say what each implies about
  achievable depth and resolution.
- Choose a method, or a pair of methods, for a stated target.

## Prerequisites

[What Geophysics Is: Physics of the Earth by Remote Measurement](./01-what-is-geophysics.md).
You need the property-contrast idea and the resolution–penetration trade-off from
that lesson.

## 1. How to read this lesson

Geophysics is conventionally divided by *method family*, and each family has its
own folder in this curriculum. For each one, four questions matter:

1. **What property contrast does it detect?** No contrast, no signal.
2. **What is the physical mechanism?** Why does the contrast produce a
   measurable response?
3. **What does it resolve, and at what depth?** The resolution–penetration
   trade-off decides this.
4. **What is it blind to?** Every method has a characteristic ambiguity.

The table is the summary; the sections that follow explain the "why", which is
the part that transfers to situations you have not met before.

| Subdiscipline | Primary contrast | Typical depth reach | Characteristic strength | Characteristic blind spot |
|---|---|---|---|---|
| Seismology | Elastic moduli and density | Metres to the whole Earth | Highest spatial resolution | Needs a source or noise; expensive for large 3-D volumes |
| Gravity and geodesy | Mass density; surface displacement | Metres to global | Cheap regional coverage; direct mass information | Non-uniqueness; weak depth resolution |
| Geomagnetism | Magnetic susceptibility and remanent magnetisation | Metres to tens of kilometres (crust) | Fast, cheap, portable | Dipole decay favours shallow sources |
| Electrical and EM | Electrical conductivity | Metres to hundreds of kilometres | Directly sensitive to fluids and clays | Conductivity is ambiguous in its cause |
| Ground-penetrating radar | Dielectric permittivity | Centimetres to tens of metres | Very high shallow resolution | Attenuates rapidly in conductive ground |
| Heat flow | Thermal conductivity and heat production | Whole lithosphere | Direct constraint on thermal state | Requires boreholes; sparse |
| Remote sensing and satellite geodesy | EM radiation; range and phase | Surface to orbit | Global, repeatable coverage | Indirect; needs ground truth |
| Well logging | Many, measured in situ | Borehole | Direct calibration of other methods | Spatially sparse |

## 2. Seismology: elastic waves

**Contrast:** elastic moduli (bulk modulus $K$, shear modulus $\mu$) and density
$\rho$, which together set wave speeds:

$$v_P = \sqrt{\frac{K + \tfrac{4}{3}\mu}{\rho}}, \qquad
v_S = \sqrt{\frac{\mu}{\rho}} .$$

**Mechanism.** A disturbance — an earthquake, an explosion, a vibrator, or the
ambient vibration of the Earth — excites elastic waves. Where a boundary separates
media with different speeds and densities, energy reflects and refracts; the
recorded ground motion therefore carries travel times and amplitudes that depend
on the medium the waves crossed. Because $v_S = \sqrt{\mu/\rho}$, the existence of
shear waves is itself proof that the medium resists shear — one of the classical
arguments that the outer core is liquid, since shear waves do not pass through it.

**What it resolves.** The finest resolution of any geophysical method, because
wavelengths can be made short: a few kilometres for regional crustal studies, and
sub-metre for shallow high-frequency surveys.

**Blind spot.** Seismic speed depends on several rock properties at once
(porosity, fluid content, mineralogy, pressure), so an inversion gives velocity
structure, not a unique rock type. Fluids are inferred from the *combination* of
$v_P$, $v_S$ and density, which is why multi-component and repeated (4-D) surveys
exist. Start at [06-seismology](../../06-seismology/README.md).

## 3. Gravity and geodesy: measuring mass

**Contrast:** density. Gravity responds to the distribution of mass; geodesy
measures the shape of the Earth and its changes in time.

**Mechanism.** Newton's law of gravitation gives the field of a point mass as
$g = GM/r^{2}$, and outside its sources the gravitational potential satisfies
Laplace's equation, $\nabla^{2}\Phi = 0$ (in the source region, Poisson's
equation, with density on the right-hand side). Because contributions from every
element of mass add, an anomaly is a weighted sum over the whole body — smooth,
broad and, crucially, non-unique. A relative gravimeter measures the local
*acceleration of a proof mass*; typical exploration anomalies are of order
$10^{-5}\ \text{m}\,\text{s}^{-2}$ (milliGals), which is a few parts in
$10^{9}$ of the Earth's field. That is why instrument drift, tides, elevation and
terrain all have to be modelled and removed.

**Geodesy** extends the same physics to the whole planet: satellite gravimetry
infers large-scale mass distribution and its changes (for example ice-mass loss
or groundwater depletion), while GNSS and radar interferometry measure surface
displacement directly.

**What it resolves.** Excellent for large, dense, shallow-to-moderate bodies and
for global mass change; poor at separating a deep, large contrast from a shallow,
small one.

**Blind spot.** Depth, in a word. See
[07-gravity-geodesy](../../07-gravity-geodesy/README.md).

## 4. Geomagnetism: the Earth's field, internal and crustal

**Contrast:** magnetic susceptibility (the induced magnetisation of rock in the
present field) and remanent magnetisation (a permanent, geologically acquired
magnetisation).

**Mechanism.** The main field is generated by dynamo action in the liquid outer
core, and near the surface it is approximately dipolar; its field lines are what a
compass follows. Crustal rocks carry additional magnetisation, so a magnetic
survey measures the *sum* of the main field, induced crustal magnetisation and any
remanence. A dipole's field falls off as $r^{-3}$ — faster than gravity's $r^{-2}$
— so magnetic surveys emphasise shallow sources. Anomalies are quoted in
nanoteslas ($1\ \text{nT} = 10^{-9}\ \text{T}$), with the Earth's field of order
tens of thousands of nanoteslas and useful anomalies often in the hundreds.

Because the anomaly depends on the *direction* of both the inducing field and the
remanence, magnetic anomalies are usually asymmetric away from the magnetic
poles, while gravity anomalies over the same body are symmetric. That asymmetry is
information, not a nuisance, and it is one of the most instructive contrasts in
applied geophysics.

**Blind spot.** Non-magnetic rocks are invisible, and a strong remanence can
produce an anomaly that has nothing to do with present-day composition.

## 5. Electrical and electromagnetic methods: fluids and conductivity

**Contrast:** electrical conductivity $\sigma$, whose reciprocal is resistivity
$\rho_e$. In most rocks, conductivity is controlled by connected pore fluid, by
clay content, and by conductive minerals.

**Mechanism.** Two mechanisms coexist. *Galvanic* methods inject current through
electrodes and measure the resulting potential difference, from which an apparent
resistivity is computed. *Inductive* methods use time-varying electromagnetic
fields, which induce currents in the ground; the secondary field from those
currents is measured. Depth of investigation scales with the **skin depth**,

$$\delta = \sqrt{\frac{2}{\mu_0 \omega \sigma}},$$

with $\mu_0 = 4\pi\times10^{-7}\ \text{H}\,\text{m}^{-1}$, angular frequency
$\omega$ and conductivity $\sigma$. Magnetotellurics uses natural, very
low-frequency fields to reach crustal and mantle depths.

The skin depth in numbers, for three representative cases:

| Conductivity | Frequency | Skin depth $\delta$ | Physical setting |
|---|---|---|---|
| $0.001\ \text{S}\,\text{m}^{-1}$ | $10^{-3}\ \text{Hz}$ | about $500\ \text{km}$ | Resistive lithosphere, magnetotelluric band |
| $0.01\ \text{S}\,\text{m}^{-1}$ | $1\ \text{Hz}$ | about $5\ \text{km}$ | Moderately resistive rock, deep sounding |
| $1\ \text{S}\,\text{m}^{-1}$ | $1\ \text{Hz}$ | about $500\ \text{m}$ | Conductive, water-bearing ground |

Compare the second and third rows, where the frequency is the same: one hundred
times the conductivity gives one tenth of the skin depth, because the dependence
is on the square root. The first and second rows differ in both frequency and
conductivity, which is why magnetotellurics reaches the mantle only by using
periods of seconds to thousands of seconds. This square-root scaling is worth
internalising, because it explains why distinguishing a moderately conductive
body from a very conductive one requires careful survey design rather than simply
"a stronger signal".

**Blind spot.** Conductivity alone rarely identifies *why* the ground is
conductive: saline pore water, clay and sulphide mineralisation can look similar,
so electrical methods are usually combined with seismic or geochemical evidence.
See [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md)
and [09-electrical-em-methods](../../09-electrical-em-methods/README.md).

## 6. Ground-penetrating radar: the shallowest method

**Contrast:** dielectric permittivity $\varepsilon_r$. In a low-loss material the
electromagnetic wave speed is

$$v = \frac{c}{\sqrt{\varepsilon_r}},$$

where $c$ is the speed of light in vacuum. Typical dry soil and rock have
$\varepsilon_r$ in the single digits to low tens, giving speeds of order
$0.1\text{–}0.15\ \text{m}\,\text{ns}^{-1}$; water has a much larger
$\varepsilon_r$, so a water table is a strong reflector.

**Mechanism.** A short high-frequency pulse is radiated into the ground and
reflections are recorded at boundaries where wave speed — equivalently, impedance
$Z = \sqrt{\mu/\varepsilon}$ — changes. The reflection coefficient at normal
incidence is $R = (Z_2 - Z_1)/(Z_2 + Z_1)$, so contrast determines amplitude and
polarity, and two-way travel time converts to depth once $v$ is known.

**What it resolves.** Centimetres to tens of centimetres in the top metres — the
best shallow resolution available — but attenuation rises sharply with
conductivity, so clay-rich or saline ground may limit penetration to a metre or
less.

**Blind spot.** Conductors, and the fact that depth conversion needs a velocity
estimate, which usually comes from a common-midpoint measurement or a borehole.
See [10-gpr-near-surface](../../10-gpr-near-surface/README.md).

## 7. Heat flow: the thermal state

**Contrast:** thermal conductivity $k$ and radiogenic heat production. Heat moves
by conduction according to Fourier's law,

$$\mathbf{q} = -k \nabla T,$$

so measuring the temperature gradient in a borehole and the conductivity of the
rocks gives the heat flux, conventionally reported in $\text{mW}\,\text{m}^{-2}$.
Global averages differ between oceanic and continental lithosphere of different
ages; the exact values depend on the compilation used, so consult a current
reference rather than quoting a single figure from memory.

**Why it matters.** Heat flow constrains the thermal structure of the lithosphere,
the depth of the brittle–ductile transition, the geothermal resource base, and the
thermal history of sedimentary basins for hydrocarbon maturity.

**Blind spot.** It requires boreholes, so it is sparse, and separating conductive
from convective transport is a genuine problem in permeable formations.

## 8. Remote sensing and satellite geophysics

**Contrast:** the electromagnetic radiation reflected or emitted by the surface
(optical and thermal), the radar backscatter (microwave), and the range or phase
of a radar or GNSS signal.

**Mechanism.** Optical and thermal sensors measure reflected sunlight and emitted
radiation, from which surface properties are inferred. Radar measures the
amplitude and phase of a transmitted pulse; in *interferometric* mode (InSAR),
differences in phase between two acquisitions record surface displacement, with
each full phase cycle of $2\pi$ corresponding to a line-of-sight displacement of
half the radar wavelength. GNSS measures position precisely and repeatedly, giving
a displacement time series at a point.

**What it resolves.** Spatial coverage that no ground survey can match, with
repeat times of days, at the cost of being indirect — a displacement is not a
material property, and optical data need atmospheric correction and ground truth.

**Blind spot.** Depth. Satellite methods see the surface (though they sense mass
distribution and interior structure indirectly through gravity and the geoid).
See [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md) and the
geodetic modules of [07-gravity-geodesy](../../07-gravity-geodesy/README.md).

## 9. Well logging and rock physics: the bridge to direct observation

**Well logging** measures properties inside a borehole — natural gamma
radiation, electrical resistivity, acoustic travel time, density and porosity —
using tools lowered on a wireline. It is *direct* in the sense that it is at the
rock, and *sparse* in the sense that it samples a line, not a volume.

**Rock physics** is the discipline that connects what a geophysical measurement
sees to what a geologist describes: relations between porosity, saturation,
mineralogy, pressure and the measured property. Some of these are empirical —
Archie's law, for example, relates the conductivity of a clean, water-bearing
sandstone to porosity and water saturation — and empirical relations carry
calibration assumptions that must be stated when used.

This is the most practically important complementary pairing in the subject:
well logs calibrate surface measurements, and surface measurements extrapolate
well logs into three dimensions. See
[05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)
and [23-field-methods-instruments](../../23-field-methods-instruments/README.md).

## 10. Why methods are combined

The subdisciplines are not competitors. They are complementary because they sense
*different properties*, and the strength of an interpretation usually comes from
constraining one model with two independent measurements. Three standard
combinations:

1. **Seismic geometry plus gravity or magnetics for property.** Seismic gives
   the shape of a structure precisely; a potential-field measurement constrains
   what the rocks are (density or magnetisation).
2. **Seismic velocity plus resistivity for fluid content.** Neither alone
   identifies a fluid; together they can separate, for example, brine from
   hydrocarbon under the same porosity.
3. **Borehole logs plus surface geophysics for coverage.** Logs pin the
   property–response relation at a point; surface data map it.

Joint inversion formalises this by inverting two datasets for one model, which is
covered in [18-inverse-problems/07-joint-and-multi-physics-inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md).

## 11. A worked choice

*Target: a shallow aquifer, expected at 10–30 m depth in sandy, moderately
resistive ground, and you also need to know where the clay layer that confines it
lies.*

- **Sensitivity:** water content changes both dielectric permittivity and
  conductivity; clay changes conductivity. So GPR (permittivity) and resistivity
  or EM (conductivity) are the natural pair.
- **Depth and resolution:** at 10–30 m, GPR will likely penetrate in resistive
  sand but may struggle below the water table; a resistivity sounding will reach
  the depth comfortably but with coarser vertical resolution.
- **Discrimination:** low resistivity marks clay, but also brine; a seismic
  refraction or surface-wave measurement can separate a *soft* saturated sand
  from *plastic* clay, which helps.
- **Plan:** EM or resistivity for the framework, GPR where ground conditions
  permit for shallow detail, and a borehole to calibrate both.

Notice that the reasoning never began with "which instrument do I like?" It began
with the property contrast and the depth and resolution required. That is the
transferable skill.

## Common mistakes

1. **Choosing a method by habit rather than by contrast.** An instrument is
   useful only if the expected contrast exceeds its detection threshold.
2. **Expecting depth resolution from a potential field.** Gravity and magnetics
   constrain products and geometry, not depth directly.
3. **Reading conductivity as a lithology.** It is a fluid and mineralogy
   indicator with several possible causes.
4. **Using GPR in clay or saline ground and blaming the instrument.** Attenuation
   is the physics, not a fault.
5. **Quoting a single global heat-flow number as a constant.** It varies strongly
   with tectonic setting, and compilations differ; cite the source and the region.
6. **Running one method where two would have resolved the ambiguity.** The
   complementarity in section 10 is the remedy.

## Real-world applications

- **Groundwater and contamination.** Electrical, EM and GPR methods map aquifers
  and plumes; see [14-hydrology-hydrogeophysics](../../14-hydrology-hydrogeophysics/README.md).
- **Mineral and energy exploration.** Magnetics, gravity, EM and seismic are
  combined routinely; see [11-exploration-geophysics](../../11-exploration-geophysics/README.md).
- **Engineering and infrastructure.** GPR and shallow seismic locate buried
  services and assess ground conditions before construction.
- **Hazard assessment.** Seismology constrains ground shaking; geodesy and InSAR
  track deformation before volcanic eruptions and on creeping faults; seafloor
  mapping supports tsunami modelling.
- **Climate.** Satellite gravity and radar altimetry measure ice-mass change and
  sea level, linking the solid-Earth and climate disciplines.
- **Planetary exploration.** The same method families are flown to other bodies;
  see [12-global-geophysics-interior/07-planetary-interiors-comparative](../../12-global-geophysics-interior/07-planetary-interiors-comparative/README.md).

## Further reading

- Lowrie, W., & Fichtner, A. (2020). *Fundamentals of Geophysics* (3rd ed.).
  Cambridge University Press. — Method-by-method treatment aligned with sections
  2–8.
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied Geophysics*
  (2nd ed.). Cambridge University Press. — The reference work for applied method
  physics, including the sensitivities discussed here.
- Reynolds, J. M. (2011). *An Introduction to Applied and Environmental
  Geophysics* (2nd ed.). Wiley-Blackwell. — Detailed near-surface treatment,
  including GPR and resistivity practice.
- Mussett, A. E., & Khan, M. A. (2000). *Looking into the Earth: An Introduction
  to Geological Geophysics.* Cambridge University Press. — Particularly clear on
  what each method contributes to a geological interpretation.
  These are bibliographic records; confirm availability through your library or a
  DOI resolver before citing them yourself.

## Related lessons

- [What Geophysics Is: Physics of the Earth by Remote Measurement](./01-what-is-geophysics.md)
- [Historical Development: From Pendulums to Satellites](./03-history.md)
- [Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface](../02-curriculum-map/03-domain-tracks.md)
- [Master Curriculum Map: How the 27 Folders Connect](../02-curriculum-map/01-master-map.md)
