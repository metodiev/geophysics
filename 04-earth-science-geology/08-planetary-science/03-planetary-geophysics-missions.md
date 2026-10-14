---
id: 04-08-03
title: "Planetary Geophysics from Orbiters and Landers"
level: advanced
prereqs: ["04-08-02", "06-01-02", "06-08-02"]
estimated_minutes: 75
tags: [planetary-geophysics, seismology, radio-tracking, radar-sounding, magnetometry]
---

# Planetary Geophysics from Orbiters and Landers

The geophysics of other planets is done with the same instruments as the
geophysics of this one, and under a constraint that changes everything:
**you get one instrument, one location, and one chance.** There is no array to
deploy, no line to roll out, no second visit if a cable fails, and no ground
truth to calibrate against. Every measurement must therefore be designed so that
its interpretation is possible from the measurement alone, and the decisive
engineering question is not precision but *what the measurement can be inverted
for*.

This lesson computes what each of four techniques can see, from the
measurement's own uncertainty rather than from any published result. The
techniques are: **seismology from a lander** (a single three-component station
that records the body's own quakes), **radio tracking** (the Doppler shift of a
carrier as a spacecraft flies through a gravity field), **radar sounding** (a
radar that penetrates ice to a buried interface), and **magnetometry** (a
magnetometer in orbit over a magnetised crust). The four are the ones that have
supplied essentially all of what is known about the interiors of bodies other
than the Earth, and each has a characteristic limiting factor that is *not* the
instrument.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** an epicentral distance from a P–S time difference under the
   simplest possible model, and state why the result is not robust and what the
   robustness comes from instead.
2. **Derive** the conversion delay of a Ps phase at vertical incidence and use it
   to compute a crustal thickness, and demonstrate the trade-off between
   thickness and velocity ratio that makes one phase insufficient.
3. **Compute** the two-way Doppler signature of a range rate and the velocity
   change produced by a gravity anomaly, and state what actually limits gravity
   from an orbiter.
4. **Compute** the vertical resolution of a radar sounder from its bandwidth, the
   depth of an interface from an echo delay, the Fresnel reflectivity of an
   interface, and the penetration depth as a function of the loss tangent.
5. **Compute** the field of a magnetised dipole at depth and explain how the
   width of an anomaly constrains the depth while its amplitude constrains the
   magnetisation.
6. **State**, for each technique, which measurement is direct and which is an
   inference with a model inside it.
7. **Explain** why a targeted mission returns a value with a model attached, and
   construct the honest sentence that reports it.

## Prerequisites

- [04-08-02 Planetary Interiors and Magnetic Fields](./02-planetary-interiors.md)
  — what these measurements are used to infer, and why an interior is a model.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md)
  — the two body-wave types whose travel-time difference the lander seismology
  uses.
- [06-08-02 H-K Stacking and Crustal Thickness Estimation](../../06-seismology/08-receiver-functions-and-crustal-structure/02-h-k-stacking.md)
  — the terrestrial method whose single-station version this lesson computes,
  and the trade-off it exists to resolve.

## 1. The constraint that shapes everything

Three limitations distinguish planetary geophysics from terrestrial geophysics,
and every technique in this lesson is a response to one of them.

**No spatial arrays.** A terrestrial refraction line has tens of receivers and
several shots, so the inverse problem is overdetermined. A lander has one station
and must use the *body's own* sources — quakes, impacts, or a controlled source —
and locate them with a single station's phase arrivals and polarisation.

**No repeat visits, and no repair.** An instrument that fails is a mission that
ends. This is why planetary instruments are built to be simple, why redundancy is
preferred over sophistication, and why a single well-understood measurement is
worth more than a subtle one.

**No ground truth.** A terrestrial gravity survey can be calibrated against
drilled densities; a terrestrial seismic line can be calibrated against a well.
On another body there is nothing to tie to, so the interpretation rests entirely
on the model — which is why the honest form of a planetary result names the model
in the same sentence as the number.

## 2. Seismology from a single station

**Distance from a P–S time difference.** In the crudest possible model — a
homogeneous body with straight rays — the P and S arrivals from the same event
arrive at

$$t_P = \frac{D}{v_P}, \qquad t_S = \frac{D}{v_S}
\quad\Longrightarrow\quad
D = (t_S - t_P)\frac{v_Pv_S}{v_P - v_S} . \tag{1}$$

The conversion factor for $v_P = 6.0$ and $v_S = 3.5$ km s⁻¹ is
8.40 km per second of S-minus-P time. Its sensitivity is worth computing, because
it is unfavourable: the logarithmic derivatives are

$$\frac{v_P}{f}\frac{\partial f}{\partial v_P} = \frac{v_S}{v_P - v_S} = 1.40,
\qquad
\frac{v_S}{f}\frac{\partial f}{\partial v_S} = \frac{v_P}{v_P - v_S} = 2.40, \tag{2}$$

so **a 1 per cent error in $v_S$ is a 2.4 per cent error in the distance**, and a
distance error displaces the estimated origin by the same amount. A single
station therefore cannot separate origin time, depth and distance, whatever its
timing precision — the number of stations, not the quality of one, is what makes
a location determinate.

**Crustal thickness from a converted phase.** The useful single-station
measurement is the **Ps** phase: a P wave converted to an S wave at a velocity
contrast beneath the station. At vertical incidence the conversion delay is

$$t_{Ps} = H\left(\frac{1}{v_S} - \frac{1}{v_P}\right)
\quad\Longrightarrow\quad
H = \frac{t_{Ps}}{1/v_S - 1/v_P} , \tag{3}$$

which is the simplest form of the receiver-function problem. For $t_{Ps} = 4$ s
and $v_P/v_S = 1.71$ this gives $H = 33.8$ km; for $v_P/v_S = 1.90$ it gives
26.7 km. **An 11 per cent difference in the velocity ratio is a 21 per cent
difference in the thickness**, and the delay alone cannot separate the two.

The remedy is a second phase whose delay depends on $H$ and $v_P/v_S$
differently — a multiple, or the Ps + PpSs arrival pair. Two equations, two
unknowns; one equation is a curve, not a point. This is precisely the logic of
the H–k stacking method used on Earth
([06-08-02](../../06-seismology/08-receiver-functions-and-crustal-structure/02-h-k-stacking.md)),
reduced to its single-station limit.

**What a single station is good at.** Not location and not thickness from one
phase. It is good at: the *presence* of a low-velocity structure, the polarisation
of arrivals (which distinguishes a P from an S, and a deep event from a shallow
one), the detection of a core phase (which establishes a core), and the sheer
*existence* of a quake, which is the statement that the body is seismically
active at all. The last is a large claim from a small measurement, and it is the
reason a single seismometer has been worth a mission.

## 3. Gravity from radio tracking

A spacecraft's range rate is measured by the Doppler shift of a coherent carrier.
For a one-way range rate $\dot r$ the returned frequency is shifted by

$$\frac{\Delta f}{f} = \frac{2\dot r}{c} , \tag{4}$$

the factor of 2 because the path is traversed twice. At X-band
($f = 8.4$ GHz) a range rate of 1 mm s⁻¹ gives 0.056 Hz, and a Doppler
measurement stable to 0.01 Hz over a 60 s count corresponds to
**0.18 mm s⁻¹** of range rate. That sensitivity is why gravity is measurable from
an orbiter at all: the observable is a frequency, and frequency is what a radio
system measures best.

**What an anomaly does.** A spacecraft passing over a 10 mGal anomaly
($10^{-4}$ m s⁻²) accumulates a velocity change of $a\,t$: 1.0 mm s⁻¹ in 10 s,
6.0 mm s⁻¹ in 60 s and 30 mm s⁻¹ in 300 s. In Doppler terms, at X-band, those are
0.056, 0.336 and 1.68 Hz — 5.6, 34 and 168 times the assumed noise floor.
**A 10 mGal anomaly is a small anomaly and it produces an enormous Doppler
signal**, so the limitation on gravity from an orbiter is not the instrument. It
is:

- **Geometry.** The resolution at the surface is set by the spacecraft's altitude
  and velocity: a low, slow pass resolves shorter wavelengths. The altitude is a
  resource, and it is spent by atmospheric drag.
- **Non-gravitational accelerations.** Solar radiation pressure, atmospheric drag
  and thruster activity all produce accelerations comparable with the anomalies
  being measured. They are removed by an accelerometer, by modelling, or by a
  drag-free system, and the residual is the dominant error.
- **The reference frame and the field model.** The measured Doppler is inverted
  for a spherical-harmonic field, and the inversion must be regularised because
  the problem is non-unique: a deep mass anomaly and a shallow one can produce
  the same field outside the body
  ([07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md)).

## 4. Radar sounding

A radar sounder transmits a chirp into a low-loss medium and records the echoes
from internal interfaces and the base. Four numbers characterise what it can do.

**Vertical resolution from bandwidth.** The two-way travel time is resolved to
the reciprocal of the bandwidth, so in a medium of permittivity
$\varepsilon_r$

$$\Delta z = \frac{c}{2B\sqrt{\varepsilon_r}} . \tag{5}$$

For a 10 MHz chirp in cold ice ($\varepsilon_r \approx 3.15$, a commonly used
value) this is 8.45 m; a 60 MHz chirp gives 1.41 m. Note the direction of the
permittivity dependence: a medium of *higher* permittivity has a shorter
wavelength, so the resolution in depth is **finer**, and the only free lever is
the bandwidth.

**Depth from the echo delay.** $z = ct/(2\sqrt{\varepsilon_r})$: 10 µs of
two-way delay is 845 m in ice.

**Reflectivity from the Fresnel coefficient.** At normal incidence between two
non-magnetic dielectrics,

$$R = \frac{\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2}}{\sqrt{\varepsilon_1} + \sqrt{\varepsilon_2}} . \tag{6}$$

For ice over water (80) the power reflection coefficient is $|R|^2 = 0.447$; for
ice over dry rock (6) it is $0.0255$. **A water interface returns 17.5 times the
power of a dry-rock interface** — about 12 dB more — which is the entire basis of
subglacial lake detection: the signal is not the echo, it is the difference
between two echoes.

**Penetration from the loss tangent.** For a low-loss dielectric the field
attenuation coefficient is
$\alpha = (\omega/c)\sqrt{\varepsilon_r}\tan\delta/2$, so the power decays as
$e^{-2\alpha z}$ and the 1/e depth for power is

$$z_{1/e} = \frac{1}{2\alpha}
= \frac{c}{\omega\sqrt{\varepsilon_r}\tan\delta} . \tag{7}$$

At 10 MHz in ice this is 269 km for $\tan\delta = 10^{-5}$, 26.9 km for
$10^{-4}$, 2.7 km for $10^{-3}$ and 269 m for $10^{-2}$. **Three orders of
magnitude in the loss tangent is three orders of magnitude in penetration**, and
$\tan\delta$ is a temperature-dependent material property that must come from a
measurement or a dielectric-properties compilation. A penetration depth quoted
without it is not a penetration depth.

## 5. Magnetometry from orbit

The crustal field of a body that has no dynamo today is the fossil of one that
did, and a magnetometer in orbit measures it. For a vertically magnetised dipole
of moment $m$ at depth $d$, the vertical field at surface radius $r$ is

$$B_z(r) = \frac{\mu_0m}{4\pi}\frac{2d^2 - r^2}{(r^2+d^2)^{5/2}} . \tag{8}$$

The two properties that matter are exact and easy to derive:

- The peak amplitude at $r = 0$ is $(\mu_0m/4\pi)\cdot 2/d^3$, i.e. it falls as
  $1/d^3$.
- The **half-width** — the offset at which the anomaly falls to half its peak —
  is $0.50\,d$ to within half a per cent. That is the classical rule for a point
  dipole, and it is why the *width* of an anomaly gives the depth while its
  *amplitude* gives the magnetisation times the volume.

Because the two are separate, a single-altitude survey is ambiguous but a
two-altitude one is not: directly above a dipole the field is
$(\mu_0m/4\pi)\cdot2/(d+h)^3$, so the ratio of the anomaly at the surface to the
anomaly at altitude $h$ is $((d+h)/d)^3$ — monotonic in $d$ and independent of
$m$. That is why a low-altitude pass is combined with a higher one, and why the
altitude history of a mission is part of its data product rather than an
engineering detail.

For a real crustal layer the source is not a point dipole, and its thickness, its
magnetisation distribution and the altitude sensitivity of the instrument all
enter. A "depth to the top of the magnetised layer" is a model parameter with a
stated trade-off, exactly as it is on Earth.

## 6. Physical interpretation

- **The limiting factor is different for each technique, and it is never the
  instrument.** For lander seismology it is the number of stations; for gravity it
  is the non-gravitational accelerations and the altitude; for radar it is the
  loss tangent; for magnetometry it is the altitude history and the unknown
  geometry of the source.
- **A single station can establish existence, not structure.** Detecting that a
  body has quakes at all is a major result; locating them well is a different
  mission.
- **Doppler is a frequency measurement, and frequency is easy.** The precision of
  radio tracking is so far above what is needed that it is not the error budget —
  which is a rare and enviable position in geophysics.
- **Radar sounding is a contrast detector.** It works because water and rock have
  very different permittivities, and it fails when the interface has no contrast
  or when the medium absorbs the wave before it arrives.
- **The width of a magnetic anomaly is the depth, and the height is the
  magnetisation.** The pair is the classic potential-field ambiguity, and the
  second altitude is the classic remedy.

## 7. Units and dimensional analysis

| Quantity | Expression | Units |
|---|---|---|
| Distance from S–P | $(t_S-t_P)v_Pv_S/(v_P-v_S)$ | s × m s⁻¹ = m |
| Conversion delay | $H(1/v_S - 1/v_P)$ | m/(m s⁻¹) = s |
| Doppler shift (two-way) | $2\dot r/c$ | dimensionless |
| Velocity change from an anomaly | $a\,t$ | m s⁻² × s = m s⁻¹ |
| Radar vertical resolution | $c/(2B\sqrt{\varepsilon_r})$ | (m s⁻¹)/(s⁻¹) = m |
| Depth from delay | $ct/(2\sqrt{\varepsilon_r})$ | m |
| Fresnel coefficient | $(\sqrt{\varepsilon_1}-\sqrt{\varepsilon_2})/(\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2})$ | dimensionless |
| Penetration depth | $c/(\omega\sqrt{\varepsilon_r}\tan\delta)$ | m |
| Dipole field | $(\mu_0m/4\pi)(2d^2-r^2)/(r^2+d^2)^{5/2}$ | T |

Two checks are worth making. The Doppler shift must be dimensionless, and it is:
$\dot r/c$ is a ratio of speeds. The radar resolution has the units of length only
if $B$ is a frequency in Hz, which is why a bandwidth is always quoted in Hz and
never in metres — a common slip when a chirp is described by its wavelength
rather than by its frequency sweep.

## 8. Assumptions and regime of validity

1. **A homogeneous body and straight rays** in (1). This is the simplest possible
   locator and it is used here only to show what the conversion factor is and how
   sensitively it depends on the velocities. A real location uses a velocity model
   and several stations.
2. **Vertical incidence** in (3). At non-zero ray parameter the delay involves
   $\sqrt{1/v^2 - p^2}$ terms, and the H–k trade-off changes with the ray
   parameter, which is one reason the method stacks over a range of distances.
3. **A one-dimensional layered structure beneath the station** in (3). A dipping
   interface or a lateral velocity gradient biases the thickness in a
   distance-dependent way, which is diagnosable only with more than one station.
4. **A coherent two-way transponder and a known turnaround ratio** in (4). The
   absolute frequency shift depends on the transponder's oscillator; the
   frequency *change* does not.
5. **A known spacecraft trajectory** in §3. The Doppler measures a line-of-sight
   velocity, and subtracting the trajectory to obtain the gravity field is the
   largest single data-reduction step in the analysis.
6. **A low-loss, homogeneous subsurface** in (5) to (7). A medium with a
   significant clay or brine content loses the ability to sound at all, and a
   medium with internal layering produces reflections that complicate the base
   echo.
7. **A point dipole source** in (8). Real magnetised layers are extended, so the
   half-width is a lower bound on the depth in a layer sense, and both the
   thickness and the magnetisation distribution are unknown.
8. **A measurement of one body, once.** Nothing in this lesson is calibrated
   against ground truth on another body, because there is none.

## 9. Python demonstration

[`code/planetary_geophysics_missions_demo.py`](./code/planetary_geophysics_missions_demo.py)
computes the sensitivity of all four techniques from assumed instrument
performance and assumed material properties, all labelled. No mission,
instrument, discovery or published result is named.

Seismology, including the sensitivity that makes a single station insufficient:

```text
  The conversion factor is v_P v_S/(v_P - v_S) = 8.40 km per
  second of S-minus-P time.  It AMPLIFIES velocity error, because it
  contains the difference in the denominator:
    a 1 per cent error in v_P becomes 1.40 per cent in distance
    a 1 per cent error in v_S becomes 2.40 per cent in distance
```

```text
     t_Ps (s)   H at v_P/v_S = 1.71   H at 1.80   H at 1.90 (km)
         4.0                    33.80         30.00            26.67
```

Radio tracking, where the conclusion is the *inverse* of the usual one:

```text
     duration (s)   dv (mm/s)   df (Hz)   signal/noise
            30        3.00      0.168            16.8
            60        6.00      0.336            33.6
```

Radar sounding, and the numbers that decide whether a subglacial interface is
visible:

```text
     B (MHz)   dz (m)
       10.0      8.45
       60.0      1.41

  over water (80)                    -0.6688        0.4474     -3.5
  over dry rock (6)                  -0.1597        0.0255    -15.9

     tan(delta)   power 1/e depth (m)   two-way loss (dB/km)
       1.0e-04                26883                     0.32
       1.0e-03                 2688                     3.23
```

### What to observe

- The seismological conversion factor amplifies velocity error, and it amplifies
  $v_S$ errors more than $v_P$ errors because $v_S$ is the smaller number. That
  asymmetry is the reason a velocity model is worth more to a single-station
  location than a better clock.
- The Ps delay table contains the trade-off in one line: 4 s is 33.8 km at
  $v_P/v_S = 1.71$ and 26.7 km at 1.90. Neither the delay nor a plausible velocity
  range alone determines the thickness, and that is why two-phase methods exist.
- The gravity sensitivity is the surprise. A 10 mGal anomaly over 60 s produces a
  Doppler signal 34 times the assumed noise, so the instrument is not the
  limitation. **A measurement that is easy is not the same as an inference that
  is easy**, and the difficulty in orbiter gravity is in the trajectory and the
  non-gravitational accelerations.
- The radar tables show the two independent ways a sounding fails: no
  permittivity contrast at the interface, or a loss tangent that absorbs the wave
  before it arrives. The reflection contrast table says that a water interface is
  detectable; the loss table says whether the wave reaches it.

## 10. Common mistakes

1. **Treating a single-station distance as a location.** Equations (1) and (2)
   show why it cannot be.
2. **Quoting a crustal thickness from a Ps delay alone.** It requires a velocity
   ratio, and the trade-off is large.
3. **Assuming that Doppler precision limits orbiter gravity.** It does not;
   the trajectory and the non-gravitational accelerations do.
4. **Quoting a radar penetration depth without a loss tangent.** The dependence
   is linear in $1/\tan\delta$, over three orders of magnitude.
5. **Confusing a radar echo's delay with a depth.** The conversion needs the
   permittivity, and a 10 per cent permittivity error is a 5 per cent depth error.
6. **Reporting a magnetic depth from amplitude alone.** Amplitude gives
   magnetisation times volume; the depth is in the width.
7. **Forgetting the altitude history in a magnetic interpretation.** The same
   crust gives different anomaly maps at different altitudes, and only the
   combination constrains the depth.
8. **Comparing an orbiter-derived quantity with a terrestrial one without the
   model.** A gravity field, a moment of inertia and a heat flow all require a
   model, and the models are not the same.
9. **Assuming a null result is a negative result.** No detected quakes may mean a
   quiet body or a noisy instrument, and telling them apart is an analysis in
   itself.
10. **Quoting a planetary value without its source and epoch.** These are revised;
    a radius or a field strength from an old paper is a systematic error.

## 11. Real-world applications

- **Mission design.** The trade between altitude (resolution) and lifetime (drag)
  for a gravity mission is set by the arithmetic of §3.
- **Subsurface exploration.** The same radar sounding methods are used on Earth's
  ice sheets, where the loss tangent is measured rather than assumed
  ([17-03 Radar Remote Sensing](../../17-remote-sensing-gis/03-radar-remote-sensing/README.md)).
- **Planetary seismology.** The terrestrial receiver-function and location
  techniques transferred to another body are the subject of
  [06-13 Planetary and Applied Seismology Frontiers](../../06-seismology/13-planetary-and-exploration-seismology/README.md).
- **Crustal magnetism and geological history.** Magnetic mapping is the cheapest
  way to date a surface, and the same potential-field methods are used on Earth
  and in exploration
  ([11 Exploration Geophysics](../../11-exploration-geophysics/README.md)).
- **Geodesy of slow deformation.** Radio tracking also measures the rotation and
  the tides of a body, which are interior constraints of a different kind
  ([07-04 Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md)).
- **Ground truth by proxy.** Earth's ice sheets and deserts are the calibration
  sites for the instruments that will be flown elsewhere, which is why terrestrial
  analogue work is part of every planetary geophysics programme.

## 12. Further reading

- **Aki, K., & Richards, P. G. *Quantitative Seismology* (University Science
  Books).** The travel-time and receiver-function theory that (1) and (3) simplify,
  and the place to look before extracting structure from a single station.
  Level: graduate.
- **Lognonné, P., & Johnson, C. L. *Planetary Seismology* (Springer).** The
  dedicated reference on single-station and very-small-array seismology, including
  the detection-limit problem. Level: doctoral.
- **Tapley, B. D., Schutz, B. E., & Born, G. H. *Statistical Orbit
  Determination* (Elsevier).** The estimation theory behind turning a Doppler
  series into a gravity field. Level: graduate.
- **Hanssen, R. F. *Radar Interferometry* (Kluwer)**, and the ice-sounding radar
  literature that followed the terrestrial sounding programmes. The dielectric
  and loss-tangent values for ice must come from a measured compilation rather
  than from memory. Level: graduate.
- **Blakely, R. J. *Potential Theory in Gravity and Magnetic Applications*
  (Cambridge University Press).** The dipole relations in (8) and the
  depth-versus-amplitude ambiguity in full. Level: advanced.
- **NASA and ESA mission pages at <https://www.nasa.gov> and
  <https://www.esa.int>.** The authoritative source for instrument
  specifications, results and the revisions that follow; planetary values are
  revised, and a mission's own archive is the primary reference. Level: reference.
- **The Goddard Space Flight Center and NOAA geomagnetic reference products at
  <https://www.ngdc.noaa.gov/IAGA/vmod/igrf.html>.** Model coefficients and
  calculators for the field used as a reference in magnetic surveys. Level:
  reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [04-08-02 Planetary Interiors and Magnetic Fields](./02-planetary-interiors.md)
  — what these measurements are inverted for.
- [04-08-04 Exoplanets, Habitability and Observational Constraints](./04-exoplanets-habitability.md)
  — what happens to interior inference when a mission is not possible at all.
- [06-13 Planetary and Applied Seismology Frontiers](../../06-seismology/13-planetary-and-exploration-seismology/README.md)
  — the seismological side in full.
- [06-08-02 H-K Stacking and Crustal Thickness Estimation](../../06-seismology/08-receiver-functions-and-crustal-structure/02-h-k-stacking.md)
  — the multi-station method whose single-station limit is (3).
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md)
  — how the same field is recovered from an Earth-orbiting mission.
- [17-03 Radar Remote Sensing](../../17-remote-sensing-gis/03-radar-remote-sensing/README.md)
  — radar systems, sounding and interferometry from a remote-sensing perspective.

Exercises:
[`exercises/03-planetary-geophysics-missions-exercises.md`](./exercises/03-planetary-geophysics-missions-exercises.md)
and
[`exercises/03-planetary-geophysics-missions-solutions.md`](./exercises/03-planetary-geophysics-missions-solutions.md).

## Self-assessment checklist

- [ ] I can compute a distance from a P–S time difference and state its
      sensitivity to each velocity. (§2)
- [ ] I can derive the Ps delay and compute a thickness, and state the
      thickness/velocity-ratio trade-off. (§2)
- [ ] I can compute a two-way Doppler shift and the velocity change from a
      gravity anomaly, and name what actually limits orbiter gravity. (§3)
- [ ] I can compute a radar vertical resolution from a bandwidth. (§4)
- [ ] I can compute a Fresnel reflection coefficient and compare two interfaces.
      (§4)
- [ ] I can compute a penetration depth from a loss tangent and state its
      sensitivity. (§4)
- [ ] I can compute a dipole anomaly, the half-width rule, and the two-altitude
      depth discrimination. (§5)
- [ ] I can state, for each of the four techniques, what is measured and what is
      inferred. (§6)
- [ ] I can name three things a single-station seismic experiment cannot do.
      (§2, §8)
- [ ] I can write the honest sentence that reports a planetary result with its
      model attached. (§6, §8)
