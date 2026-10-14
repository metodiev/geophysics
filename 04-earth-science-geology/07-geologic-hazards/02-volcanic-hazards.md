---
id: 04-07-02
title: "Volcanic Hazards, Monitoring and Precursors"
level: intermediate
prereqs: ["04-02-05", "02-01-02"]
estimated_minutes: 75
tags: [volcanoes, monitoring, precursors, deformation, hazard-assessment]
---

# Volcanic Hazards, Monitoring and Precursors

Volcano monitoring is the part of geophysics with the shortest distance between
a measurement and a decision. Everything in this lesson is measured on a
mountain that people live on, and the measurements are used to decide whether to
close a road, order an evacuation, or do nothing. That makes the *epistemic*
content of the subject as important as the mechanical content, and this lesson
treats them as equally quantitative.

There are two halves. The first half is physics: what deformation a pressurised
magma body produces, what a gravity change means, how a plume scales, and how a
gas measurement turns into a mass flux. The second half is decision theory: what
a precursor actually tells you when the base rate of eruptions is low, and how
good a false-alarm rate you would need for a forecast to be worth acting on.
Both halves are computed here. The second one is the reason this lesson is
honest rather than promotional.

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** volcanic hazards by the physical process that delivers them —
   fall, flow, surge, lahar, gas — and state which measurement bears on each.
2. **Derive** the displacement of a pressurised spherical cavity in an elastic
   medium and use the Mogi solution to compute the far-field surface
   displacement and its $1/r^3$ decay.
3. **Compute** the surface tilt of a Mogi source, show that it peaks at half the
   source depth, and state what a tiltmeter and a GNSS network can therefore
   resolve about source depth.
4. **Compute** the gravity change produced by a compact mass change and state
   why gravity is a *mass* measurement and deformation is not.
5. **Derive** the $H \propto F^{1/4}$ scaling of a buoyant plume by dimensional
   analysis, and state which part of the relation is empirical.
6. **Explain** why seismic, geodetic, gas and thermal precursors are all
   *ambiguous* signals, and compute the posterior probability of an eruption
   given a precursor from a stated base rate, sensitivity and false-alarm rate.
7. **Compute** the false-alarm rate required for a stated posterior probability,
   and explain why that number, rather than sensitivity, is the hard one to
   obtain.
8. **State** the assumptions in each of these models and the conditions under
   which they fail.

## Prerequisites

- [04-02-05 Tectonics and the Distribution of Earthquakes and Volcanoes](../02-plate-tectonics/05-tectonics-hazards.md)
  — where volcanoes are and why, and the tectonic settings that determine what
  kind of volcano it is.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../../02-physics/01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — the vocabulary of uncertainty used throughout, and the base-rate arithmetic
  in §7.

## 1. The hazards, and the measurement that bears on each

Volcanic hazards are usually grouped by the physical process that delivers the
material, because the process determines both the reach and the measurement.

| Hazard | Physical process | Reach | Measurement that bears on it |
|---|---|---|---|
| Tephra fall | buoyant plume, then settling | tens to thousands of km | plume height, wind profile, grain size |
| Pyroclastic density current | gravitational collapse of a column or dome | a few to tens of km | topography, deposit mapping, seismicity of dome growth |
| Lava flow | gravity-driven viscous flow | metres to tens of km | effusion rate, topography, thermal imagery |
| Lahar | remobilisation of ash by water | valley-confined, tens of km | deposit mapping, rainfall, hydrology |
| Debris avalanche | flank collapse | tens of km | flank deformation, hydrothermal alteration mapping |
| Gas and aerosol | passive or explosive degassing | regional to global | SO₂ flux, plume composition |

The single most important structural fact about the table is that **the
hazards with the largest reach are the ones with the weakest monitoring
signal**, because the signal is the plume and the plume is only visible from
outside. A tephra-fall forecast needs the wind field, which is weather, and a
column height, which is a measurement of something that has already happened.

## 2. Deformation: what a pressurised body does to the surface

Start with the simplest elastic problem that has an exact answer, because it
fixes the amplitude of everything else.

**A pressurised spherical cavity in an infinite elastic medium.** Take a
spherically symmetric displacement field $u_r = B/r^2$. Then
$\nabla\cdot\mathbf{u} = 0$, the radial strain is $\varepsilon_{rr} = -2B/r^3$,
and the radial stress is

$$\sigma_{rr} = 2\mu\,\varepsilon_{rr} = -\frac{4\mu B}{r^3} . \tag{1}$$

At the cavity wall $r = a$ the stress must equal the applied pressure change
$-\Delta P$, so $B = \Delta P\,a^3/(4\mu)$ and the wall displacement is

$$u_r(a) = \frac{\Delta P\,a}{4\mu},
\qquad
\Delta V = 4\pi a^2 u_r(a) = \frac{\pi a^3 \Delta P}{\mu} . \tag{2}$$

The cavity's volume change is what a deformation measurement actually measures.
For a source 1 km in radius with a 10 MPa overpressure in rock of shear modulus
30 GPa, (2) gives $u_r(a) = 0.083$ m and $\Delta V = 1.05\times10^6$ m³ — a
cubic kilometre is 10⁹ m³, so this is a thousandth of a cubic kilometre, and
that is the scale of a real intrusion episode rather than a Hollywood one.

**The Mogi solution.** A point pressure source at depth $d$ in an elastic
half-space produces the surface displacements

$$u_z(r) = C\,\frac{d}{(r^2 + d^2)^{3/2}}, \qquad
u_r(r) = C\,\frac{r}{(r^2 + d^2)^{3/2}}, \qquad
C = \frac{3a^3\Delta P}{4\mu} , \tag{3}$$

which is a quoted solution — the half-space Green's function behind it is not
derived here — but whose *structure* is what matters and can be checked. Three
consequences follow immediately from (3) and are exact:

- The maximum uplift is $u_z(0) = C/d^2$: **the amplitude is a source strength
  divided by the square of the depth.** For $C = 2.5\times10^5$ m³ and
  $d = 3$ km, $u_z(0) = 27.8$ mm.
- The far field falls as $C d / r^3$, a **dipole** decay, so a source twice as
  deep is eight times harder to see at the same radial distance.
- $u_r = u_z$ exactly at $r = d$.

**Tilt.** Differentiate $u_z$:

$$\frac{\partial u_z}{\partial r} = -3Cd\,\frac{r}{(r^2+d^2)^{5/2}} , \tag{4}$$

whose magnitude is maximised where $d^2 - 4r^2 = 0$, i.e. at

$$r = \tfrac{1}{2}d . \tag{5}$$

**The peak surface tilt occurs at half the source depth.** That is why a
radially distributed tilt or GNSS array can locate a source depth at all: the
*shape* of the profile sets the depth while its amplitude sets the strength.
For the numbers above the peak tilt is 7.95 µrad, which a borehole tiltmeter
resolves with a comfortable margin.

**Where the model fails.** A Mogi source is a point, a sphere, and elastic. Real
intrusions are sills, dykes and irregular volumes; the host rock is
heterogeneous, fractured and often already above the elastic limit near the
chamber; and the medium is not a half-space but a volcanic edifice with
topography that perturbs the near-field displacements by tens of per cent. A
Mogi inversion therefore returns an *equivalent* point source whose depth and
volume change are model quantities. That is still useful — the equivalent source
is a compact summary of whether the system is inflating or deflating — but it is
not a picture of a magma chamber.

## 3. Microgravity: the measurement that sees mass, not just motion

Deformation and gravity are complementary, and the reason is dimensional. A
compact mass change of volume $V$ and density change $\Delta\rho$ at depth $d$
produces

$$\Delta g = \frac{G\,V\,\Delta\rho}{d^2} . \tag{6}$$

For a body of radius 1 km, $\Delta\rho = 300$ kg m⁻³ (a few per cent of the
density difference between magma and its host) at 3 km depth,
$\Delta g = 9.32\times10^{-6}$ m s⁻² = 0.93 mGal. A modern relative gravimeter
repeats to a few µGal, so a 0.93 mGal signal is two orders of magnitude above
the noise, and (6) shows the catch: at 10 km the same body gives 84 µGal, and
at 30 km it would be below 10 µGal.

The value of gravity is that it responds to **mass** while GNSS responds to
**displacement**. A chamber that is inflating by injecting volatile-rich magma
gains volume and loses density; a chamber that is crystallising gains density at
constant volume. Both look similar in GNSS and completely different in gravity.
The combination is therefore diagnostic in a way neither measurement is alone,
and the classic ambiguity — is this new magma or a pressurised gas phase? — is
one that only a joint inversion can address.

## 4. Plumes: the quarter-power law

A volcanic plume is a turbulent buoyant jet in a stratified atmosphere. The
dimensional content of that statement is complete:

- buoyancy flux $F$ (the source's excess buoyancy per unit time), units
  $\mathrm{L^4\,T^{-3}}$;
- buoyancy frequency $N$ of the stratified atmosphere, units $\mathrm{T^{-1}}$;
- the height $H$ reached, units $\mathrm{L}$.

The **only** combination of $F$ and $N$ with the dimensions of a length is

$$\left(\frac{F}{N^3}\right)^{1/4} , \tag{7}$$

so dimensional analysis alone gives

$$H = C\left(\frac{F}{N^3}\right)^{1/4} , \tag{8}$$

with $C$ a dimensionless constant that the argument does not determine. This is
the whole result: **the column height scales as the quarter power of the
buoyancy flux**, so a factor of 16 in eruption rate is a factor of 2 in height,
and a factor of 2 in height requires 16 times the mass flux.

The exponent $1/4$ is derived. The constant is not, and neither is the
assumption that the plume is in a uniformly stratified atmosphere with a single
$N$. In a real atmosphere the tropopause, moisture and wind shear all matter, and
(8) is the *scaling* that a full plume model reproduces rather than a formula
that predicts a height from a first principle. Report the exponent, and quote a
constant with its source or not at all.

## 5. Gas: turning a concentration into a flux

The most direct measure of what a volcano is *emitting* is the SO₂ flux, and the
measurement is a closed-path or remote-sensing column amount combined with a
wind speed:

$$\Phi = \bar{C}\,\bar{u}\,L , \tag{9}$$

where $\bar C$ is a line-averaged concentration along the measurement path,
$\bar u$ the wind speed component across that path and $L$ the plume width. It
is a mass balance and it is exact; every difficulty is in the three factors. The
concentration depends on the plume being optically thin and on the retrieval
model; the wind speed is usually taken from a numerical weather model rather
than measured in the plume; and $L$ is estimated from the same image that
produced the concentration, which correlates the errors in the numerator and the
denominator.

A useful sanity condition is that the flux must be consistent with the
deformation: a sustained $\Phi$ corresponds to a magma supply rate, and a supply
rate integrated over an inflation episode has to be compatible with the volume
change (2) inferred from GNSS. When they disagree by an order of magnitude,
something in the chain is wrong, and finding out which is the actual work.

## 6. Seismicity as a monitoring signal

Volcano-tectonic earthquakes, long-period events and tremor are the standard
seismic signals, and the distinctions among them are physical rather than
cosmetic. Volcano-tectonic events are brittle failure of rock under stress
changes, with a spectrum whose corner frequency scales with the source
dimension. Long-period events and tremor involve a fluid — a resonating crack or
conduit — and their spectra are dominated by the resonance rather than by the
source duration.

The practical measure in a volcano observatory is usually not a moment magnitude
but a *rate* and an *amplitude*: counts per hour above a threshold, or a
real-time amplitude average. Both are relative measures tied to a specific
instrument and a specific threshold, and neither transfers between networks
without recalibration. That is why an escalation in a monitoring report is
described in terms of a change relative to the volcano's own baseline, not in
absolute units.

## 7. Precursors are ambiguous: a calculation

Consider a monitoring interval — say one year — at a volcano with an annual
eruption probability $p$. A precursor has sensitivity $s$ (the probability it
appears before an eruption) and false-alarm rate $f$ (the probability it appears
in an interval with no eruption). Bayes gives the probability of an eruption
given that the precursor appeared:

$$P(\text{erupt} \mid \text{precursor})
= \frac{s\,p}{s\,p + f\,(1-p)} . \tag{10}$$

For $p = 0.01$, $s = 0.90$ and $f = 0.05$:

$$P = \frac{0.009}{0.009 + 0.0495} = 0.154 .$$

**A 90 per cent sensitive precursor raises a 1 per cent chance to 15 per cent.**
That is a real gain — a factor of 15 in the odds — and it is nowhere near a
prediction. The reason is arithmetic, not pessimism: when the base rate is low,
almost all precursor episodes occur at volcanoes that are not about to erupt,
because there are so many more of them.

Inverting (10) for the false-alarm rate needed to reach a target posterior $P^*$:

$$f = \frac{s\,p\,(1-P^*)}{P^*\,(1-p)} . \tag{11}$$

At $p = 0.01$ and $s = 0.90$:

| Target $P^*$ | Required $f$ | One false alarm per |
|---|---|---|
| 0.50 | 0.00909 | 110 quiet intervals |
| 0.80 | 0.00227 | 440 quiet intervals |
| 0.90 | 0.00101 | 990 quiet intervals |
| 0.99 | 0.00009 | 10 890 quiet intervals |

**The binding constraint on a forecast is the false-alarm rate, and it is the
quantity that is hardest to measure**, because measuring it requires a long
record of *quiet* intervals that were monitored as carefully as the restless
ones. Observatories remember their eruptions; they keep far patchier records of
the hundreds of occasions on which nothing happened. So the honesty requirement
is not modesty: it is that the quantity a decision needs is the quantity the
record is least able to supply.

Two further points make the situation worse in practice and are worth stating
because they are often omitted. First, the intervals are not independent: a
volcano that has just produced a precursor is more likely to produce another, so
the Poisson-like arithmetic above is optimistic. Second, $p$ is itself estimated
from a short record with a large uncertainty, and it enters (10) linearly.

## 8. Physical interpretation

- The three monitoring streams measure **different physical quantities**:
  deformation measures displacement, gravity measures mass, gas measures flux,
  seismicity measures brittle failure and fluid resonance. They are not four
  views of one variable; they are four variables, which is why a joint
  interpretation can be diagnostic and a single stream usually is not.
- The **depth** of a deformation source is inferred from the *shape* of the
  displacement field and the **strength** from its amplitude, so a sparse
  network constrains a combination of the two rather than either.
- Plume height scales as $F^{1/4}$, so the eruption rate is very poorly
  constrained by a measured height: a factor of 2 in height is a factor of 16
  in flux.
- A precursor changes a probability; it does not determine an outcome. A
  forecast is a statement about a *population* of similar situations, and a
  volcano with no historical record contributes nothing to the false-alarm
  statistics it needs.

## 9. Units and dimensional analysis

| Quantity | Expression | Units |
|---|---|---|
| Cavity volume change | $\pi a^3\Delta P/\mu$ | m³ |
| Mogi strength $C$ | $3a^3\Delta P/(4\mu)$ | m³ |
| Far-field displacement | $Cd/r^3$ | m³ × m / m³ = m |
| Tilt | $\partial u_z/\partial r$ | rad |
| Gravity change | $GV\Delta\rho/d^2$ | m³ s⁻² kg⁻¹ × m³ × kg m⁻³ / m² = m s⁻² |
| Plume scaling | $(F/N^3)^{1/4}$ | (m⁴ s⁻³ × s³)^{1/4} = m |
| Gas flux | $\bar C\bar u L$ | kg m⁻³ × m s⁻¹ × m = kg s⁻¹ |
| Posterior probability | $sp/(sp + f(1-p))$ | dimensionless |

The tilt column is worth pausing over: a tilt is a *dimensionless* ratio, which
is why a tiltmeter's output is usually quoted in microradians and why a tilt of
1 µrad corresponds to 1 mm of differential motion over 1 km. The gravity change
in the table has the units of acceleration, so it can be quoted in µGal without
conversion arithmetic and compared directly with instrument noise.

## 10. Assumptions and regime of validity

1. **Elastic half-space** in §2 and §3. Volcanoes are layered, fractured and
   partly ductile below the brittle–ductile transition. An elastic inversion of
   deformation data returns an equivalent source, not a chamber.
2. **Point source** in (3). Valid when the observation distance is much greater
   than the source dimension. A 3 km deep source that is 2 km across is being
   described by a formula that assumes it is a point, and the near-field
   displacements will be wrong.
3. **Boussinesq and steady-state buoyancy** in (8). A plume that is bent over by
   wind, that partly collapses, or that is denser than the surrounding air at
   the level of neutral buoyancy does not obey it.
4. **Uniform, constant-$N$ stratification** in (8). Real atmospheres have a
   tropopause, and a plume that reaches it changes regime.
5. **Optically thin, uniformly mixed, still plume** in (9). Ash-rich plumes are
   optically thick and the retrieval fails; a plume moving across the field of
   view invalidates the steady-state assumption.
6. **Independence of monitoring intervals and a known base rate** in (10) and
   (11). Both are idealisations, and both move the answer in the optimistic
   direction.

## 11. Python demonstration

[`code/volcanic_hazards_demo.py`](./code/volcanic_hazards_demo.py) computes the
Mogi deformation and tilt, the microgravity signal, the plume scaling and the
Bayesian precursor calculation. Every scenario is labelled SYNTHETIC; no
eruption, date, volume or monitoring record appears anywhere in it.

The cavity result and the far field:

```text
    wall displacement u(a) = a dP/(4 mu) = 0.083333 m
    cavity volume change dV = pi a^3 dP/mu = 1.047198e+06 m^3  (derived)
    Mogi strength C = 3a^3 dP/(4 mu)       = 2.500000e+05 m^3
    C / dV = 3/(4 pi) = 0.238732
```

```text
     r (km)   u_z (mm)   u_r (mm)   u_r/u_z   far-field r^3 u_z / C
       0.0    27.7778     0.0000     0.0000          nan
       1.0    23.7171     7.9057     0.3333    94.868330
       3.0     9.8209     9.8209     1.0000  1060.660172
      10.0     0.6591     2.1968     3.3333  2636.219134
      20.0     0.0907     0.6045     6.6667  2901.524752
```

And the tilt maximum, which is the diagnostic that locates the depth:

```text
  tilt |du_z/dr| peaks at r = 1.5000 km, against d/2 = 1.5000 km
  peak tilt = 7.950464e-06 rad = 7.950 microrad
```

### What to observe

- The far-field column $r^3u_z/C$ grows towards $d = 3000$ m as $r$ increases:
  that is $u_z \to Cd/r^3$ verified numerically rather than asserted. The
  1/r³ decay is what makes a deep source invisible rather than merely weaker.
- $u_r = u_z$ exactly at $r = d = 3$ km, where the ratio column reads 1.0000.
  This is a zero-parameter prediction of the model and a good internal check
  that the two components were coded consistently.
- The tilt peak lands on $d/2$ to four decimal places. The derivation in §2
  proved it; the numerical scan confirms that the derivative was implemented
  correctly.
- The gravity table makes the point about depth quantitatively: 0.93 mGal at
  3 km, 84 µGal at 10 km. A microgravity survey can therefore see a shallow
  intrusion and cannot see a deep one, whatever its precision.

## 12. Common mistakes

1. **Reading a Mogi inversion as a magma chamber.** The result is an equivalent
   point source in a homogeneous elastic half-space; its "depth" is a
   best-fitting number, not a lithological boundary.
2. **Assuming a bigger precursor means a bigger eruption.** Precursor amplitude
   and eruption size are only loosely related, and the relation is not
   established well enough to use for sizing.
3. **Using plume height to estimate mass flux linearly.** The scaling is
   $F^{1/4}$; a factor of 2 in height is 16 in flux.
4. **Quoting a precursor as a prediction.** Compute the posterior and quote it,
   with the base rate you used.
5. **Forgetting that gas flux and deformation must be consistent.** Checking
   them against each other is one of the few available internal consistency
   tests.
6. **Comparing amplitude-based seismic rates across different networks.** They
   are instrument- and threshold-dependent.
7. **Treating an unrest episode with no eruption as a failure of the science.**
   It is the dominant outcome and it must be counted if the statistics are to
   mean anything.
8. **Assuming the atmosphere is uniformly stratified.** The tropopause sets the
   level of neutral buoyancy for large plumes.
9. **Ignoring topography in a near-field deformation model.** On a volcano the
   edifice is the near field.
10. **Quoting a monitoring threshold as a physical law.** Every threshold in
    volcano monitoring was chosen by somebody, for a purpose.

## 13. Real-world applications

- **Observatory practice.** GNSS, tilt, seismicity, gas and thermal data are
  combined into a routine assessment; the value of the combination is that the
  measurements have independent failure modes.
- **Aviation safety.** Ash advisories are issued from a combination of plume
  models, satellite imagery and dispersion modelling; the height at the source
  is the dominant uncertainty.
- **Lahar warning.** Acoustic-flow-monitor detection on a valley approach is a
  geophysical measurement with a decision attached.
- **Geothermal exploration and drilling safety.** The same deformation and
  microgravity tools are used on hydrothermal systems
  ([04-06-03 Geothermal Systems, Heat Flow and Resource
  Assessment](../06-petroleum-and-mineral-systems/03-geothermal-systems.md)).
- **Volcanic flank stability.** The interaction of hydrothermal alteration,
  clay layers and rainfall is the same problem as a landslide
  ([04-07-03 Landslides, Slope Stability and Geotechnical Geophysics](./03-landslides.md)).
- **Long-term hazard mapping.** The geological record of past flows and falls is
  the input to land-use planning, and it is what makes up for the short
  instrumental record.

## 14. Further reading

- **Mogi, K. (1958). "Relations between the eruptions of various volcanoes and
  the deformations of the ground surfaces around them." *Bulletin of the
  Earthquake Research Institute*.** The original point-source solution in (3).
  Level: advanced, historical.
- **Dzurisin, D. *Volcano Deformation: Geodetic Monitoring Techniques*
  (Springer/Praxis).** The standard reference on the measurement side, including
  what each technique can resolve and what it costs. Level: graduate.
- **Segall, P. *Earthquake and Volcano Deformation* (Princeton University
  Press).** The elastic theory behind §2 in full, with the half-space Green's
  functions that this lesson quotes. Level: graduate.
- **Sparks, R. S. J., et al. (2012). "Monitoring volcanoes." *Science*.** A
  compact review of what monitoring can and cannot deliver, useful as a
  counterweight to instrument-led accounts. Level: advanced.
- **Turner, J. S. (1962). "The 'starting plume' in neutral surroundings."
  *Journal of Fluid Mechanics*.** The plume theory whose scaling appears in (8),
  and the source of the buoyancy-flux formulation. Level: graduate.
- **USGS Volcano Hazards Program and its observatory pages, reached from
  <https://www.usgs.gov>.** The authoritative source for current activity,
  alert levels and the vocabulary used in official notices; note that the main
  site blocks automated requests and is intended for a browser. Level:
  reference.
- **NASA Earth Observatory and the wider Earth-observation record at
  <https://www.nasa.gov>.** Thermal and SO₂ imagery used in monitoring. Level:
  reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 15. Related lessons

- [04-07-01 Earthquake Hazard and Ground Motion](./01-earthquake-hazard.md) —
  the seismic signal used in volcano monitoring, and the site and path terms
  that a volcano seismic network has to live with.
- [04-07-03 Landslides, Slope Stability and Geotechnical Geophysics](./03-landslides.md)
  — flank collapse and lahar initiation.
- [04-07-04 Subsidence, Sinkholes and Karst](./04-subsidence-sinkholes.md) —
  the other place where deformation and gravity are interpreted together.
- [05-08 Borehole and Well-Log Geophysics](../../05-core-geophysics/08-geophysical-logging/README.md)
  — logging techniques used in geothermal and volcano-hosted hydrothermal
  systems.
- [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md)
  — the same base-rate logic applied to a different hazard, where the base rate
  is even lower.
- [07-01 Gravity Fundamentals](../../07-gravity-geodesy/01-gravity-fundamentals/README.md)
  — the field theory behind (6).

Exercises:
[`exercises/02-volcanic-hazards-exercises.md`](./exercises/02-volcanic-hazards-exercises.md)
and
[`exercises/02-volcanic-hazards-solutions.md`](./exercises/02-volcanic-hazards-solutions.md).

## Self-assessment checklist

- [ ] I can list five volcanic hazards and name the measurement that bears on
      each. (§1)
- [ ] I can derive the wall displacement of a pressurised cavity from the
      elastic displacement field and the boundary condition. (§2)
- [ ] I can compute the Mogi surface displacement, its maximum and its far-field
      decay. (§2)
- [ ] I can derive the tilt maximum at $r = d/2$ and compute a tilt in
      microradians. (§2)
- [ ] I can compute a microgravity change from a compact mass and say why depth
      is the limiting factor. (§3)
- [ ] I can derive $H \propto F^{1/4}$ and say which part of the relation is
      determined by the argument. (§4)
- [ ] I can compute a posterior probability of eruption given a precursor, and
      state the base rate I used. (§7)
- [ ] I can compute the false-alarm rate required for a target posterior
      probability. (§7)
- [ ] I can explain why the false-alarm rate is harder to measure than the
      sensitivity. (§7)
- [ ] I can name three ways the elastic point-source model fails on a real
      volcano. (§10)
