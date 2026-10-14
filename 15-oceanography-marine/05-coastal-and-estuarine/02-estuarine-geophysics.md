---
id: 15-05-02
title: "Estuarine and Delta Geophysics"
level: doctoral
prereqs: ["15-05-01", "15-02-04", "15-01-01", "09-02-01"]
tags: [oceanography, marine-geophysics, coastal-and-estuarine, estuaries, deltas, salinity]
---

# Estuarine and Delta Geophysics

> **All models and data in this module are SYNTHETIC.** The sound-speed model, the
> estuaries and the sediment budget are teaching models with stated model
> constants. No real estuary, delta, river or survey is referenced, and no number
> is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a seawater sound speed from a density model, and **state** whether
   a vertical structure refracts sound toward or away from the vertical.
2. **Quantify** the sounding error produced by assuming a constant sound speed in
   a stratified estuary, and **state** its dependence on depth.
3. **Classify** an estuary from its river flow, geometry and density difference
   using a densimetric Froude number, and **state** which of its inputs is a model
   choice.
4. **Derive** the exponential salinity-intrusion profile from a steady
   advection–diffusion balance, and **compute** the position of a chosen
   isohaline.
5. **Compute** the competition between accommodation created by sea-level rise
   and sediment supply, and **state** when a basin fills and when it reaches an
   equilibrium.
6. **Distinguish** what a sub-bottom profile and a resistivity section measure
   from what an estuarine interpretation models.
7. **State** the three quantities in an estuarine survey that are choices rather
   than measurements.

## Prerequisites

- [15-05-01 Coastal Processes, Sediment Transport and Shoreline Change](01-coastal-processes.md) —
  the wave and littoral processes that feed these systems.
- [15-02-04 Sub-Bottom Profiling and Chirp Systems](../02-marine-geophysics-methods/04-sub-bottom-profiling.md) —
  the shallow imaging used here.
- [15-01-01 Seawater Properties](../01-physical-oceanography/01-seawater-properties.md) —
  the temperature–salinity–density relations.
- [09-02-01 The Resistivity Principle](../../09-electrical-em-methods/02-dc-resistivity/01-resistivity-principle.md) —
  the conductivity route to pore-fluid salinity.

## 1. Intuition: the estuary is where two water masses negotiate

An estuary is the place where river water meets seawater, and almost everything
about it follows from that meeting. The two water masses differ in density by a
few per cent, which is enough to make the interface stable, to drive a
gravitational circulation, and to determine whether the system is a thin salt
wedge, a partially mixed channel, or a vertically homogeneous one. The
classification is not a description; it is a prediction about where the salt is,
and therefore about where the geophysical contrasts are.

Geophysics enters in three places.

**The water column is itself a medium.** Sound speed depends on temperature,
salinity and pressure, so an estuary with a strong halocline refracts sound. A
multibeam system that assumes a single sound speed measures a biased depth, and
the bias grows as the square of the depth — 2.5 m at 100 m in the model here,
which is larger than the sediment change most monitoring programmes are looking
for.

**The sediment column records the negotiation.** A sub-bottom profile through an
estuary shows the fill: fluvial channels cut during lowstands, tidal flats,
flood-tidal deltas, and the muddy drape of the modern highstand. The interpretation
requires a geological model, and the model is the part that is not measured.

**The pore fluid is a salinity map.** Conductivity responds to pore-water salinity
so strongly (a factor of 80 in bulk resistivity for a freshwater- to
seawater-saturated sand) that resistivity and EM methods are the natural tool for
mapping the freshwater–saltwater interface in the sediment — which is the subject
of [15-05-03](03-coastal-aquifers-marine.md).

## 2. Precise definitions

**Estuary classification:** a scheme relating the river and tidal flows and the
density difference to the observed stratification, from salt wedge through
partially mixed to well mixed.

**Densimetric Froude number** $\mathrm{Fr}_d=u_r/\sqrt{g'h}$ with
$g'=g\Delta\rho/\rho$ and $u_r=Q/(bh)$: the ratio of the river flow speed to the
internal wave speed of the density interface.

**Mixing parameter** $u_t/u_r$: the ratio of a tidal velocity scale to the river
velocity, measuring how much energy is available to mix the two water masses.

**Intrusion length** $L_d$: the e-folding distance over which salinity decays from
its oceanic value; the distance to a chosen isohaline is a multiple of it.

**Accommodation**: the volume created by sea-level rise (and subsidence) that
sediment must fill to keep a basin's shape; rate $=$ area $\times$ relative
sea-level rise.

**Progradation**: the seaward advance of a shoreline or a delta front; the
sediment supply divided by the depth range over which deposition occurs.

## 3. Derivations and measurements

### 3.1 Sound speed in a stratified estuary

Take a constant bulk modulus $K=2.34\ \mathrm{GPa}$ (a model constant, justified
because the compressibility of water varies far less than its density) and a
linear state equation

$$\rho(T,S)=\rho_0\left[1-\alpha_T(T-T_0)+\beta_S(S-S_0)\right],\qquad
\alpha_T=2.0\times10^{-4}\ \mathrm{K^{-1}},\;
\beta_S=7.8\times10^{-4}\ \mathrm{kg^{-1}\,g}$$

about $\rho_0=1028\ \mathrm{kg\,m^{-3}}$, $T_0=10\ ^\circ\mathrm{C}$,
$S_0=35\ \mathrm{g\,kg^{-1}}$. Then $c=\sqrt{K/\rho}$:

| $T$ (°C) | $S$ (g/kg) | $\rho$ (kg/m³) | $c$ (m/s) |
|---|---|---|---|
| 0 | 0 | 1002.0 | 1528.2 |
| 10 | 35 | 1028.0 | 1508.7 |
| 20 | 30 | 1021.9 | 1513.2 |
| 8 | 2 | 1002.0 | 1528.2 |
| 25 | 36 | 1025.7 | 1510.4 |

**Cold fresh water is faster than warm salty water here**, because the density
term dominates the temperature term: $\alpha_T/\beta_S=0.26$, so a salinity change
of 1 g/kg moves the density 3.9 times as much as a 1 K temperature change. That
ordering is a property of the model's coefficients, and it is the reason estuarine
sound-speed profiles are dominated by salinity.

A stratified column with $T=20\ ^\circ\mathrm{C}$, $S=30$ at the surface and
$T=8\ ^\circ\mathrm{C}$, $S=2$ at 20 m depth has $c=1513.20$ and
$1528.22\ \mathrm{m\,s^{-1}}$, a gradient of $0.751\
\mathrm{m\,s^{-1}\,m^{-1}}$, i.e. $a=4.96\times10^{-4}$ per metre relative.

**The sounding error.** For $c(z)=c_0(1+az)$ and a nadir beam, the two-way travel
time is $t=2(z-az^2/2)/c_0$, so a constant-speed estimate $c_0t/2$ is *low* by
$az^2/2$:

| depth (m) | error (m) | error (%) |
|---|---|---|
| 10 | −0.025 | −0.25 |
| 25 | −0.155 | −0.62 |
| 50 | −0.620 | −1.24 |
| 100 | −2.481 | −2.48 |

**Quadratic in depth** — which is why sound-speed profiles must be measured, not
assumed, in any estuary with a halocline, and why the error is worst exactly where
the survey is deepest.

**Ray bending.** Snell's law for sound is $\sin\theta/c=\text{const}$, so rays bend
*toward* the slower medium. A $45^\circ$ beam crossing from the 1513.2 to the
1528.2 m/s layer arrives at $45.57^\circ$: it steepens by $0.57^\circ$, changing
the footprint spacing and hence the apparent rugosity of any terrain attribute
computed from the swath.

### 3.2 Classification

With $u_r=Q/(bh)$, $g'=g\Delta\rho/\rho$:

| estuary | $Q$ (m³/s) | $b$ (m) | $h$ (m) | $\Delta\rho$ (kg/m³) | $u_r$ (m/s) | $\mathrm{Fr}_d$ | $u_t/u_r$ | class |
|---|---|---|---|---|---|---|---|---|
| model A | 50 | 500 | 8 | 15.0 | 0.0125 | 0.0117 | 8.0 | salt wedge |
| model B | 200 | 800 | 6 | 5.0 | 0.0417 | 0.0779 | 12.0 | partially mixed |
| model C | 500 | 1200 | 4 | 1.0 | 0.1042 | 0.5333 | 9.6 | well mixed |

The thresholds ($\mathrm{Fr}_d<0.02$ salt wedge, $<0.2$ partially mixed) are
**model choices**, stated in the demonstration; they are not universal constants.
What is not a choice is the structure of the argument: stratification survives
when the river flow is too slow to overcome the buoyancy of the density
difference and the tide is too weak to mix it.

### 3.3 Salinity intrusion

For a steady, width-averaged balance between river advection and tidal diffusion,
$uS=K_x\,\mathrm{d}S/\mathrm{d}x$ with $u$ and $K_x$ constant:

$$S(x)=S_0e^{-x/L_d},\qquad L_d=\frac{K_x}{u} .$$

With the model value $K_x=200\ \mathrm{m^2\,s^{-1}}$ and oceanic salinity
$30\ \mathrm{g\,kg^{-1}}$:

| $Q$ (m³/s) | $u_r$ (m/s) | $L_d$ (km) | distance to 1 g/kg (km) |
|---|---|---|---|
| 50 | 0.0125 | 16.00 | 54.42 |
| 100 | 0.0238 | 8.40 | 28.57 |
| 200 | 0.0417 | 4.80 | 16.33 |
| 400 | 0.0800 | 2.50 | 8.50 |

The 1 g/kg isohaline sits $\ln 30=3.40$ e-folding lengths from the mouth, so the
"intrusion length" a field survey would map is 3.4 times the physically meaningful
$L_d$ — a factor worth stating, because intrusion lengths quoted in the literature
may use either convention.

**The model's weakest assumption is $K_x=$ constant.** In reality the tidal
diffusion coefficient grows with tidal energy and with the flow itself, so the
observed dependence of intrusion on river flow is much weaker than the
$L\propto1/Q$ predicted here. The demonstration prints the check: $u_r$ rises
1.92× while $L_d$ falls to 0.52 of its value — exactly the reciprocal, as
$K_x$ constant requires.

### 3.4 Accommodation versus supply

Let a basin of area $A$ and mean depth $d$ receive bulk sediment volume $Q_s$ per
year while relative sea level rises at rate $k$:

$$\frac{\mathrm{d}A}{\mathrm{d}t}=-\frac{Q_s-kA}{d}
\;\Rightarrow\; A(t)=\frac{Q_s}{k}+\left(A_0-\frac{Q_s}{k}\right)e^{kt/d} .$$

With $A_0=100\ \mathrm{km^2}$, $d=5$ m, $k=4\ \mathrm{mm\,yr^{-1}}$,
$Q_s=7.604\times10^{5}\ \mathrm{m^3\,yr^{-1}}$ (a 200 m³/s river carrying
200 mg/L of suspended sediment deposited at a bulk density of
$1660\ \mathrm{kg\,m^{-3}}$):

- **equilibrium area** $Q_s/k=190.1\ \mathrm{km^2}$, larger than the present
  basin, so the basin fills completely rather than tending to an equilibrium;
- **fill time with the rise**, $(d/k)\ln[(Q_s/k)/(Q_s/k-A_0)]=933$ yr;
- **fill time without the rise**, $A_0d/Q_s=658$ yr.

**Sea-level rise lengthens the fill by 42%**, and a naive estimate that holds the
accommodation at its initial value (1387 yr) overstates it by 49% because the
accommodation shrinks as the basin fills. If the basin were larger than
$190\ \mathrm{km^2}$, it would never fill: the accommodation would outrun the
supply forever, and the basin would become an open embayment. **That single
comparison — $A_0$ against $Q_s/k$ — is the whole infilling question**, and both
quantities must be estimated: $Q_s$ from river gauging and sediment load, $k$ from
tide gauges and vertical land motion.

## 4. Physical interpretation

- **Salinity controls the sound speed**, through density, more strongly than
  temperature does; haloclines are sound-speed interfaces.
- **Depth errors from an unmeasured profile are quadratic**, so a survey that is
  fine in the shallows can be badly biased in the channel.
- **The classification is a prediction about the salt**, hence about where the
  conductivity contrasts (and the aquaculture, and the anoxic bottom water) will
  be.
- **The intrusion length depends on a diffusion coefficient that nobody
  measures directly.** It is inferred from salinity surveys, and it is
  parameterised, not measured.
- **A basin fills or does not, depending on one ratio.** The comparison of $A_0$
  with $Q_s/k$ decides the long-term fate, and both terms carry 30–50%
  uncertainties.
- **The stratigraphic record is a stack of these balances** operating at different
  sea levels, which is what a sub-bottom profile shows and what the interpreter
  must supply as a model.

## 5. Assumptions and regime of validity

1. **Constant bulk modulus for sound speed.** The model ignores the pressure and
   temperature dependence of $K$; over an estuary's depth range the error is small,
   but over a full ocean profile it is not.
2. **Linear state equation.** The real equation of state is nonlinear, and
   seawater's thermal expansion vanishes near $4\ ^\circ\mathrm{C}$; the linear
   model fails in cold fresh water.
3. **A single layer for the ray-bending example.** Real estuaries have continuous
   gradients and the ray path curves; the two-layer calculation bounds the effect.
4. **Steady state for the intrusion length.** Tides, river floods and spring–neap
   cycles all vary faster than the intrusion adjusts.
5. **Constant $K_x$.** The most consequential simplification in §3.3, and it
   changes the *scaling* of the answer, not just its value.
6. **Width-averaged, one-dimensional geometry.** Real estuaries have channel–shoal
   structure, and salt intrudes preferentially along the channel.
7. **A single sediment bulk density.** Compaction, grain size and organic content
   all vary; the deposited volume depends on all three.
8. **No subsidence in the fill model.** Add compactional or tectonic subsidence
   and the accommodation term becomes $(k+w)A$; in many deltas $w$ exceeds $k$.
9. **No storm events.** The supply is treated as steady; in reality a few floods
   deliver most of the sediment, so the variability is larger than the mean's
   uncertainty.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| sound speed | $c$ | $\mathrm{m\,s^{-1}}$ | $\sqrt{\mathrm{Pa}/(\mathrm{kg\,m^{-3}})}$ |
| gradient | $a$ | $\mathrm{m^{-1}}$ | $(1/c)\,\mathrm{d}c/\mathrm{d}z$ |
| discharge | $Q$ | $\mathrm{m^3\,s^{-1}}$ | |
| river velocity | $u_r$ | $\mathrm{m\,s^{-1}}$ | $Q/(bh)$ |
| reduced gravity | $g'$ | $\mathrm{m\,s^{-2}}$ | $g\Delta\rho/\rho$ |
| Froude number | $\mathrm{Fr}_d$ | dimensionless | $u_r/\sqrt{g'h}$ |
| diffusion | $K_x$ | $\mathrm{m^2\,s^{-1}}$ | $L_d=K_x/u$ |
| accommodation | — | $\mathrm{m^3\,yr^{-1}}$ | area × rate |
| sediment supply | $Q_s$ | $\mathrm{m^3\,yr^{-1}}$ | mass flux / bulk density |

Two checks: $\sqrt{K/\rho}$ must come out in $\mathrm{m\,s^{-1}}$ (it does, with
$K$ in Pa and $\rho$ in $\mathrm{kg\,m^{-3}}$), and $K_x/u$ must come out in metres
— a diffusion coefficient divided by a velocity is a length. Mixing $\mathrm{mm\,yr^{-1}}$
with $\mathrm{m\,yr^{-1}}$ in $Q_s/k$ changes the equilibrium area by 1000.

## 7. Worked examples

All numbers are printed by `code/estuarine_geophysics_demo.py`.

### Example 1 — sound speeds

$$c(10\ ^\circ\mathrm{C},35)=\sqrt{2.34\times10^{9}/1028}=1508.73\
\mathrm{m\,s^{-1}},\qquad
c(0\ ^\circ\mathrm{C},0)=\sqrt{2.34\times10^{9}/1002.0}=1528.18\
\mathrm{m\,s^{-1}} .$$

### Example 2 — the sounding error

For the model estuary's gradient $a=4.96\times10^{-4}\ \mathrm{m^{-1}}$, a 50 m
sounding with a constant-speed assumption is low by
$a z^2/2=4.96\times10^{-4}\times2500/2=0.620$ m (1.24%).

### Example 3 — classification

Model B: $u_r=200/(800\times6)=0.0417\ \mathrm{m\,s^{-1}}$,
$g'=9.80665\times5/1028=0.0477\ \mathrm{m\,s^{-2}}$,
$\sqrt{g'h}=0.535\ \mathrm{m\,s^{-1}}$, so
$\mathrm{Fr}_d=0.0779$ — partially mixed.

### Example 4 — intrusion length

Model B: $L_d=200/0.0417=4.80$ km, and the 1 g/kg isohaline is at
$4.80\times\ln 30=16.33$ km from the mouth.

### Example 5 — infilling

$Q_s=7.604\times10^{5}\ \mathrm{m^3\,yr^{-1}}$ (from
$1.262\times10^{9}\ \mathrm{kg\,yr^{-1}}$ at a bulk density of
$1660\ \mathrm{kg\,m^{-3}}$) against an accommodation of
$A_0k=4.000\times10^{5}\ \mathrm{m^3\,yr^{-1}}$: net infilling at
$3.604\times10^{5}\ \mathrm{m^3\,yr^{-1}}$ initially, an equilibrium area of
190.1 km², and a fill time of 933 yr with the rise against 658 yr without.

## 8. Python demonstration

`code/estuarine_geophysics_demo.py` prints, with units:

1. the sound-speed model over a table of temperature and salinity, the model
   estuary's profile, the depth error of a constant-speed assumption and the
   ray-bending angle;
2. the classification table with $\mathrm{Fr}_d$ and the mixing parameter;
3. the intrusion lengths and isohaline positions for four discharges, with the
   $1/Q$ check;
4. the accommodation-versus-supply balance, the equilibrium area and both fill
   times;
5. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/05-coastal-and-estuarine/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python estuarine_geophysics_demo.py
```

## 9. Exercises

[`exercises/02-estuarine-geophysics-exercises.md`](./exercises/02-estuarine-geophysics-exercises.md)
and
[`exercises/02-estuarine-geophysics-solutions.md`](./exercises/02-estuarine-geophysics-solutions.md).

## 10. Real-world applications

- **Navigation and dredging.** The intrusion length and the channel's depth
  determine the dredging volume; the sound-speed profile determines whether the
  survey that measures it is correct.
- **Water quality and hypoxia.** The classification predicts where stratification
  will trap anoxic bottom water.
- **Fisheries and aquaculture.** Salinity structure is habitat structure.
- **Coastal protection and restoration.** The accommodation–supply ratio decides
  whether a restored marsh or delta survives a sea-level rise.
- **Geotechnical and foundation surveys.** A biased sound speed is a biased
  bathymetry, and a biased bathymetry is a wrong design
  ([15-05-03](03-coastal-aquifers-marine.md)).

## 11. Further reading

- **Dyer, K. R., *Estuaries: A Physical Introduction*, Wiley.** Level: graduate
  textbook. The classification schemes, mixing and intrusion-length theory.
- **Lurton, X., *An Introduction to Underwater Acoustics*, Springer.** Level:
  graduate textbook. Sound-speed profiles and refraction.
- **Wright, L. D., & Nittrouer, C. A., "Dispersal of river sediments in coastal
  seas: contrasting cases", *Continental Shelf Research*.** Level: research. The
  delta and shelf dispersal framework behind §3.4.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can compute a seawater sound speed and its vertical gradient.
- [ ] I can compute the depth error from assuming a constant sound speed.
- [ ] I can classify an estuary and say which inputs are model choices.
- [ ] I can derive the exponential intrusion profile and locate an isohaline.
- [ ] I can compute the accommodation, the equilibrium area and the fill time.
- [ ] I can state which quantities in an estuarine survey are measured and which
      are modelled.
## Common pitfalls
1. **Assuming a constant sound speed in a stratified estuary.** The error is
   quadratic in depth and exceeds the survey's morphological signal.
2. **Treating the classification thresholds as universal.** They are model
   choices; the physics is the ratio, not the number.
3. **Quoting an intrusion length without saying which isohaline.** The 1 g/kg
   value is 3.4 e-folding lengths, not one.
4. **Reporting $L\propto1/Q$ as an observational law.** It is an artefact of a
   constant diffusion coefficient.
5. **Reading a sub-bottom profile as stratigraphy.** It is acoustic impedance; the
   surfaces must be interpreted with a geological model.
6. **Comparing an infilling rate with a supply without the accommodation term.**
   The difference between them decides whether the basin fills at all.
7. **Ignoring subsidence.** In many deltas it exceeds the sea-level term, and it is
   invisible to a tide gauge that sits on the subsiding sediment.
8. **Confusing conductivity with salinity** in the sediment, which is the subject
   of the next lesson.

## Related modules
- [15-05-01 Coastal Processes, Sediment Transport and Shoreline Change](01-coastal-processes.md) —
  the source of much of the sediment.
- [15-05-03 Coastal Aquifers and Submarine Groundwater Discharge](03-coastal-aquifers-marine.md) —
  the pore-fluid side of the same systems.
- [15-02-04 Sub-Bottom Profiling and Chirp Systems](../02-marine-geophysics-methods/04-sub-bottom-profiling.md) —
  the instrument whose data this lesson interprets.
- [15-01-01 Seawater Properties](../01-physical-oceanography/01-seawater-properties.md) —
  the state equation in full.
- [14-06-01 Catchment Characterisation](../../14-hydrology-hydrogeophysics/06-integrated-catchment-studies/01-catchment-characterisation.md) —
  the upstream half of the sediment and water budget.
- [04-05-04 Quaternary Climate](../../04-earth-science-geology/05-geomorphology-and-quaternary/04-quaternary-climate.md) —
  the sea-level history that produced the incised valleys now filled.
