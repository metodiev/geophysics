---
id: 04-07-05
title: "Tsunami Generation, Propagation and Warning"
level: advanced
prereqs: ["04-07-01", "15-01-01", "02-03-07"]
estimated_minutes: 75
tags: [tsunami, shallow-water, shoaling, warning, hazard]
---

# Tsunami Generation, Propagation and Warning

A tsunami is the most predictable of the geological hazards once it exists and
the most surprising before it does. Its propagation is governed by one of the
simplest equations in fluid dynamics — the shallow-water phase speed
$c = \sqrt{gh}$ — and the same relation explains why the wave crosses an ocean at
the speed of a jet, why it is invisible in deep water, why it grows as it
approaches a shore, and why a bottom-pressure sensor can detect it while
ignoring the sea state above it. Almost the entire subject is a single
dispersion relation and one conservation law.

Generation is the hard part, and warning is the part where the physics meets an
operational deadline. This lesson derives everything that follows from
$c = \sqrt{gh}$, states exactly what the approximation requires, and treats the
warning problem quantitatively: what a pressure sensor measures, what a warning
centre can and cannot know in the first ten minutes, and why the arrival time is
much better known than the arrival amplitude.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the shallow-water phase speed from the statement that the wave is
   long compared with the depth, and state the condition $kh \ll 1$ in terms of a
   period and a depth.
2. **Compute** the exact finite-depth phase speed and show numerically that the
   relative error of the shallow-water approximation is $k^2h^2/6$ at leading
   order.
3. **Compute** the wavelength from the period and the depth, and verify that a
   real tsunami is two orders of magnitude inside the shallow-water regime while
   a wind wave is not.
4. **Derive** Green's law, $A \propto h^{-1/4}$, from conservation of energy
   flux, and compute a shoaling amplification.
5. **Derive** the Kajiura filter from Laplace's equation with a moving bottom,
   and compute the fraction of a seafloor displacement of a given wavelength
   that reaches the surface.
6. **Derive** Snell's law for a tsunami from $c = \sqrt{gh}$ and compute the
   refraction of a wave approaching a coast.
7. **Derive** the bore speed and the flow behind a bore from mass and momentum
   conservation across a hydraulic jump, and compute their values for a given
   height.
8. **Compute** the seafloor pressure corresponding to a sea-surface elevation,
   state the detection threshold in centimetres, and explain why the ocean is
   transparent to a tsunami and opaque to a wind sea.
9. **Compute** a travel time across a basin from a depth profile and state why
   the arrival time is much better constrained than the amplitude.

## Prerequisites

- [04-07-01 Earthquake Hazard and Ground Motion](./01-earthquake-hazard.md) —
  the source: how large the seafloor displacement is, and why the rupture length
  matters as much as the magnitude.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md)
  — the long-wave limit, the dispersion relation of surface gravity waves, and
  the vocabulary of phase and group velocity.
- [02-03-07 Dispersion, Group Velocity and Phase vs Group Speed](../../02-physics/03-oscillations-and-waves/07-dispersion.md)
  — the difference between the speed of an individual crest and the speed of a
  wave packet, which matters for the arrival time and not for the speed.

## 1. Why the shallow-water approximation is the whole subject

A surface gravity wave in water of depth $h$ obeys the dispersion relation

$$\omega^2 = gk\tanh(kh) . \tag{1}$$

The **long-wave** limit is $kh \ll 1$, for which $\tanh(kh) \to kh$ and hence

$$\omega^2 \to gk^2h
\quad\Longrightarrow\quad
c \equiv \frac{\omega}{k} = \sqrt{gh} , \tag{2}$$

which is **non-dispersive**: the speed does not depend on the wavelength, so a
tsunami propagates as a shape-preserving train rather than as a spreading packet.
That single property is why a tsunami arrives as a coherent front rather than as
a slow crescendo, and it is why arrival times can be predicted from bathymetry
alone.

The condition is worth turning into the numbers a practitioner uses. With
$k = 2\pi/L$ and $L = Tc$, the condition $kh \ll 1$ becomes
$L \gg 2\pi h$: **the wavelength must be much larger than about six times the
depth.** For a 20-minute wave in 4000 m of water, (2) gives
$L = 1200\times198.06 = 238$ km, and $h/L = 0.017$ — a factor of 60 *inside* the
regime, not marginally in it. A 10 s wind wave in the same depth has
$L = 10\times198 = 1.98$ km and $h/L = 2.0$: it is a deep-water wave, it
disperses, and that is why a storm sea arrives as a mess and a tsunami arrives as
a front.

The error of (2) is worth knowing because it tells you where the approximation
fails first. Expanding $\tanh x = x - x^3/3$, the exact phase speed for a finite
depth is $c_\mathrm{exact} = \sqrt{(g/k)\tanh(kh)}
\approx \sqrt{gh}\left(1 - k^2h^2/6\right)$, so

$$\frac{c_\mathrm{exact} - \sqrt{gh}}{\sqrt{gh}} \approx -\frac{k^2h^2}{6} . \tag{3}$$

In a 4000 m ocean the error is 0.19 per cent at a 20-minute period, 0.75 per cent
at 10 minutes and 3.1 per cent at 5 minutes. The approximation is excellent for
the band that carries the destructive energy — and it is worst for the shortest
periods, which arrive first and carry least.

## 2. Speed, wavelength and travel time

Everything practical follows from (2):

$$c = \sqrt{gh}, \qquad L = Tc = T\sqrt{gh}, \qquad
t_\mathrm{travel} = \int\frac{\mathrm{d}s}{\sqrt{gh(s)}} . \tag{4}$$

The integral in (4) is the important one: a tsunami's travel time is the integral
of the depth along its path, so it is dominated by the **deepest** water on the
route and is insensitive to shallow features. For a uniform 4000 m basin,
$c = 198.06$ m s⁻¹ $= 713$ km h⁻¹ and an 8000 km crossing takes 11.2 h — four
fifths of the cruising speed of a commercial jet, and well over a day's sailing.

The consequence for a warning centre is the following asymmetry: a **travel time**
depends only on bathymetry and the origin time, and both are known to a few per
cent, so an arrival time can be issued within minutes of detection. An
**amplitude** depends on the seafloor displacement (which is inferred from a
magnitude and a fault model), the shoaling (which depends on a bathymetric
profile the tsunami has not yet reached) and the local coast (which may produce
run-up several times the offshore wave height). Arrival *times* are predictions;
arrival *heights* are estimates with factors of two in them. Any public warning
system is built around that distinction.

## 3. Shoaling: Green's law, derived

In the shallow-water limit the energy in a wave travels at the group velocity,
which for a non-dispersive wave equals the phase velocity, $c_g = c = \sqrt{gh}$.
The energy per unit surface area is $E = \tfrac12\rho gA^2$ for amplitude $A$.
Conservation of energy flux across a crest line, $E c_g \times (\text{width}) =
\text{const}$, with the width taken per unit crest length, gives

$$A^2\sqrt{gh} = \text{const}
\quad\Longrightarrow\quad
A \propto h^{-1/4} . \tag{5}$$

This is **Green's law**, and its content is complete: shoaling from 4000 m to
20 m multiplies the amplitude by $(4000/20)^{1/4} = 3.76$, with no dissipation
anywhere in the argument. A 0.5 m deep-ocean tsunami becomes 1.9 m at the 20 m
contour, before run-up, before harbour resonance and before breaking.

Two boundaries on (5) matter. It is a WKB result and it fails where the bottom
slope is steep compared with the wavelength — in the last few hundred metres of
water, which is precisely where the run-up happens. And it assumes no
dissipation, no breaking and no lateral spreading; a tsunami that spreads
radially loses amplitude for a reason (5) does not contain.

## 4. Generation: the Kajiura filter

Why is a tsunami not simply proportional to the seafloor displacement? Because
the ocean filters it. Consider a seafloor displacement of wavenumber $k$ under an
ocean of uniform depth $h$. The water is incompressible and irrotational, so the
velocity potential satisfies Laplace's equation with a bottom boundary condition
that the flow follows the (moving) ocean floor and a linearised free-surface
condition. The solution gives a surface elevation

$$\eta(k) = \frac{\eta_0(k)}{\cosh(kh)} , \tag{6}$$

which decays as $e^{-kh}$ for $kh \gg 1$. The physics is a mass-conservation
argument that can be stated without the algebra: for the surface to move, water
must be moved horizontally out of the way, and a short-wavelength bottom
undulation does not give the water enough room to respond, so it is short-
circuited.

For $h = 4000$ m the transmitted fraction is 52.7 per cent at a 20 km
wavelength, 16.1 per cent at 10 km and 1.3 per cent at 5 km, while a 100 km
wavelength passes 96.9 per cent. **The scale that matters is $2\pi h = 25$ km**:
seafloor motion at wavelengths below it generates almost nothing.

This is the single most important reason that tsunami size is not proportional
to magnitude. Two earthquakes with the same moment may differ by a factor of
three in rupture length; the longer one has more of its displacement at long
wavelength, and it generates a much larger tsunami — typically a factor of
several in deep-water amplitude, which shoals into a much larger factor at the
coast. The consequence for forecasting is uncomfortable and honest: a magnitude
issued two minutes after a rupture does not determine the tsunami, because the
rupture geometry does, and the geometry takes longer to determine than the
magnitude does.

## 5. Refraction, and why tsunamis face the coast

In shallow water the phase speed depends only on the depth, so a wave crossing a
depth gradient refracts exactly as a light ray crosses an interface, with Snell's
law applied to $c = \sqrt{gh}$:

$$\frac{\sin\theta_1}{\sin\theta_2} = \frac{c_1}{c_2}
= \sqrt{\frac{h_1}{h_2}}
\quad\Longrightarrow\quad
\frac{\sin\theta}{\sqrt{h}} = \text{const} . \tag{7}$$

With $\theta$ measured from the normal to the depth contours, the angle
*decreases* as the water shallows: a ray at $30^\circ$ in 4000 m is at
$14.5^\circ$ in 1000 m and $4.5^\circ$ in 100 m. This is why a tsunami arriving
on a long, straight coast comes in nearly parallel to the coast, and why the same
effect focuses energy onto promontories — the rays converge where the depth
contours converge, and that is a harbour-specific hazard that no open-ocean
measurement resolves.

## 6. The bore: the wave when it hits the shore

Once the wave reaches water of a depth comparable with its height, the
shallow-water equations become nonlinear and the front steepens into a bore — a
hydraulic jump. Its speed follows from conservation of mass and momentum across
a stationary front, in the frame of the front. With still-water depth $h_1$
ahead, depth $h_2$ behind, and $v$ the water velocity behind the front, mass
conservation gives $ch_1 = (c-v)h_2$ and momentum conservation gives

$$\tfrac12\rho g(h_2^2 - h_1^2) = \rho c h_1 v . \tag{8}$$

Eliminating $v$:

$$c = \sqrt{\frac{g\,h_2(h_1+h_2)}{2h_1}},
\qquad
v = c\left(1 - \frac{h_1}{h_2}\right) . \tag{9}$$

For a 2 m high front advancing into 1 m of water, $c = 7.67$ m s⁻¹ $= 27.6$
km h⁻¹ and the water behind the front runs onshore at 5.11 m s⁻¹. Those two
numbers are what a person on foot is trying to outrun, and they come from mass
and momentum conservation, not from measurement. Note also the limit: as
$h_2 \to h_1$, (9) reduces to $c \to \sqrt{gh_1}$, the ordinary shallow-water
speed, which is the check that the bore relation *contains* the linear theory
rather than replacing it.

The scaling is brutal: with $H = h_2 - h_1$, the speed grows as
$\sqrt{gH}$ for $H \gg h_1$, so a 4 m front in 1 m of water moves at 12.1 m s⁻¹
(43.7 km h⁻¹). The conclusion for evacuations is that the relevant warning time
is measured in minutes, and the relevant distance is measured in hundreds of
metres.

## 7. Warning: what a sensor on the seafloor measures

A sea-surface elevation $\eta$ changes the pressure at the seafloor by the
hydrostatic increment

$$\Delta p = \rho_w g\,\eta . \tag{10}$$

One centimetre of sea surface is 101 Pa — about one thousandth of an atmosphere.
A modern bottom-pressure recorder resolves a few pascals, so the detection
threshold is a few millimetres of sea surface, and a 1 cm signal is comfortably
detected at ocean-basin distances.

The reason this works is the same dispersion relation that governs the
propagation. The pressure under a surface wave decays with depth as
$1/\cosh(kh)$, which for $kh \gg 1$ is $\approx 2e^{-kh}$:

| Wavelength | $kh$ at 4000 m | $1/\cosh(kh)$ |
|---|---|---|
| 100 m | 251 | $7.1\times10^{-110}$ |
| 250 m | 101 | $2.2\times10^{-44}$ |
| 1000 m | 25 | $1.2\times10^{-11}$ |
| 25 km | 1.005 | 0.645 |
| 100 km | 0.251 | 0.969 |

**A storm sea with wavelengths of a few hundred metres is attenuated by tens of
orders of magnitude; a 100 km tsunami is attenuated by 3 per cent.** The ocean is
transparent to one and opaque to the other, and it is the same formula in both
rows. This is why a pressure sensor on the abyssal plain can see a 1 cm tsunami
through a 10 m swell.

Two operational consequences deserve to be stated. First, a detection is a
*threshold crossing* on a noisy record, so the practical threshold is an
amplitude at which the false-alarm rate is acceptable, not the sensor's
resolution. Second, a single sensor measures a wave passing over it: it gives the
amplitude and the period at one point on one path, so the inversion to a
source is a model calculation with a non-uniqueness of its own.

## 8. Physical interpretation

- The entire propagation problem is (2). A tsunami is a **non-dispersive** wave
  because it is 100 to 1000 times longer than the water is deep, and that is why
  a front survives an ocean crossing.
- Energy conservation across a shrinking depth gives $A \propto h^{-1/4}$, so
  shoaling is *slow*: a factor of 200 in depth gives only a factor of 3.8 in
  amplitude. The large run-up heights of historical tsunamis come from harbour
  and bay resonance and from the nonlinear run-up on the beach, not from shoaling
  alone.
- The Kajiura filter makes generation a **long-wavelength** phenomenon: the ocean
  responds to the part of the seafloor displacement with wavelengths above about
  $6h$ and ignores the rest.
- The bore speed is $\sqrt{gH}$-like, so the destructive front is fast compared
  with anything a person can do, and comparable with a car in town traffic.
- The warning problem decomposes cleanly: **travel time is a geometric
  prediction; amplitude is a model estimate.** Everything a public message
  promises should respect that split.

## 9. Units and dimensional analysis

| Quantity | Expression | Units |
|---|---|---|
| Phase speed | $\sqrt{gh}$ | (m s⁻² × m)$^{1/2}$ = m s⁻¹ |
| Wavelength | $T\sqrt{gh}$ | s × m s⁻¹ = m |
| Shoaling factor | $(h_1/h_2)^{1/4}$ | dimensionless |
| Kajiura factor | $1/\cosh(kh)$ | dimensionless |
| Bore speed | $\sqrt{gh_2(h_1+h_2)/(2h_1)}$ | m s⁻¹ |
| Seafloor pressure | $\rho_w g\eta$ | kg m⁻³ × m s⁻² × m = Pa |
| Travel time | $\int\mathrm{d}s/\sqrt{gh}$ | m/(m s⁻¹) = s |

The shoaling exponent is worth checking by a separate route: energy flux is
$\rho gA^2c/2$ and $c = \sqrt{gh}$, so $A^2\sqrt h$ is conserved, which is
$-1/4$ for the exponent on $h$. A dimensionally consistent alternative exponent
would have to come from a different conservation law, and there is none in this
problem — which is the check.

## 10. Assumptions and regime of validity

1. **$kh \ll 1$** in §1 to §5. Quantified in (3): the error is 3 per cent at
   $kh = 0.44$ (a 5-minute wave in 4000 m) and negligible at 20 minutes.
2. **Linear** in §1 to §5. The linear theory is used for open-ocean propagation,
   where the amplitude-to-depth ratio is $10^{-4}$. It fails in the last few
   metres of water, which is where (9) takes over.
3. **No dissipation and no lateral spreading** in (5). A radially spreading
   tsunami loses amplitude as $1/\sqrt{r}$ as well, and bottom friction matters
   over shallow shelves.
4. **A uniform ocean of constant depth** in (6). The filter's scale is set by the
   local depth, so over a trench the response extends to shorter wavelengths than
   over a ridge.
5. **Instantaneous seafloor displacement** in (6). The filter assumes the bottom
   moves faster than the ocean can respond, i.e. that the rupture duration is
   shorter than the time $\sqrt{gh}/L$; a slow rupture (a tsunami earthquake)
   satisfies this at long periods and generates a disproportionately large
   tsunami for its magnitude.
6. **A plane, straight, uniform front** in (8) and (9). Real bores are
   three-dimensional, they refract, and they interact with the beach profile and
   with coastal structures.
7. **Hydrostatic pressure at the sensor** in (10). The sensor measures total
   pressure, which includes the atmospheric pressure and the instrument's own
   drift; both must be removed, and the removal is what sets the practical
   detection threshold.
8. **A single depth profile along one path** in (4). Refraction means the ray
   path from source to receptor is not known a priori, so a travel-time
   computation is iterative except in the very long-wavelength limit, where
   refraction is weak.

## 11. Python demonstration

[`code/tsunami_demo.py`](./code/tsunami_demo.py) derives every quantity in this
lesson and verifies the shallow-water limit against the exact finite-depth
dispersion relation. No event, travel time, run-up or warning record is quoted.

The speed, and the check of the approximation against the exact relation:

```text
     h (m)    c = sqrt(gh) (m/s)   c (km/h)   time for 1000 km (min)
      4000               198.06      713.0                   84.2
      6000               242.57      873.2                   68.7
```

```text
     T (s)    k h     c exact    c = sqrt(gh)   relative error   (kh)^2/6
       300     0.436     192.136        198.057        3.082e-02    3.169e-02
       600     0.213     196.579        198.057        7.516e-03    7.567e-03
      1200     0.106     197.688        198.057        1.868e-03    1.871e-03
      3600     0.035     198.016        198.057        2.071e-04    2.072e-04
```

The shoaling law, and the filter that decides what can be generated:

```text
       h (m)    A/A0 (from 4000 m)   A (m) for A0 = 0.5 m
      4000                 1.0000                    0.500
       200                 2.1147                    1.057
        20                 3.7606                    1.880
        10                 4.4721                    2.236
```

```text
     L (km)    k h   1/cosh(kh)   transmitted (per cent)
       10.0   2.513      0.16095                16.09
       20.0   1.257      0.52657                52.66
       25.0   1.005      0.64544                64.54
      100.0   0.251      0.96923                96.92
```

### What to observe

- The relative error column and the $(kh)^2/6$ column agree to three figures at
  every period. That is not a coincidence but the leading term of the expansion
  of $\tanh$, and it is a good example of a numerical check confirming an
  analytic prediction rather than merely repeating it.
- The shoaling table applied from 4000 m to 4000 m returns 1.0000, which is the
  check that (5) contains no hidden constant. A formula that fails its own
  identity is a transcription error, and this one passes.
- The filter table is the quantitative answer to "why is a tsunami not just a
  big seafloor displacement": 10 km wavelengths are attenuated by 84 per cent,
  100 km wavelengths by 3 per cent, and the crossover is at the wavelength
  $2\pi h$.
- The bore table gives 7.67 m s⁻¹ for a 2 m front in 1 m of water, and the flow
  behind it at 5.11 m s⁻¹. Both are derived; neither is a measurement.

## 12. Common mistakes

1. **Using $c = \sqrt{gh}$ for the wave as it runs up a beach.** Above the
   shoreline the depth goes to zero and the formula is meaningless; run-up needs
   the nonlinear shallow-water equations and a beach profile.
2. **Treating the tsunami speed as constant along a path.** It varies as
   $\sqrt h$, so a travel-time computation must be an integral, and the deep
   segments dominate.
3. **Assuming that a bigger magnitude means a bigger tsunami.** The generation
   efficiency depends on the rupture wavelength through (6), so the geometry
   matters more than the moment.
4. **Expecting shoaling alone to explain run-up.** Green's law is a factor of a
   few; bays, harbours and the beach profile supply the rest.
5. **Quoting an arrival amplitude with the same confidence as an arrival time.**
   One is geometry and the other is a model with the source model inside it.
6. **Forgetting the atmospheric correction on a bottom-pressure record.** A
   one-millibar change in air pressure is a centimetre of sea surface, which is
   the whole detectable signal.
7. **Assuming the first wave is the largest.** A tsunami is a train; the largest
   arrival may be the second or third, and the interval between crests is set by
   the source dimension.
8. **Using a wind-wave dispersion relation for a tsunami, or vice versa.** The
   two live at opposite ends of the same curve, and the consequences (dispersive
   versus non-dispersive, invisible versus visible at depth) are opposite too.
9. **Ignoring refraction in a warning.** The same wave can be modest at one
   coastal segment and focused at the next.
10. **Presenting a single-number run-up estimate.** It is a model output with the
    source, the bathymetry and the beach profile all inside it.

## 13. Real-world applications

- **Warning centres.** Detection networks of bottom-pressure and surface
  instruments, with the travel-time computation of (4) on a bathymetric grid, and
  pre-computed inundation scenarios as the basis for messages.
- **Coastal planning.** Inundation maps derived from scenario modelling, used for
  evacuation routes and land-use zoning.
- **Seafloor geodesy and pressure.** The same instruments that detect a tsunami
  constrain slow deformation of the seafloor, which is the source term
  ([15-03 Seafloor Tectonics and Structure](../../15-oceanography-marine/03-seafloor-tectonics/README.md)).
- **Tsunami earthquakes.** Events that rupture slowly and generate a tsunami
  much larger than their magnitude suggests; the failure of (6) for a slow
  rupture is the physics behind them
  ([06-03 Earthquake Sources](../../06-seismology/03-earthquake-sources/README.md)).
- **Volcanic and landslide tsunamis.** The same propagation physics with a
  different, and much more poorly constrained, source
  ([04-07-02 Volcanic Hazards, Monitoring and Precursors](./02-volcanic-hazards.md)).
- **Marine geohazards in general.** Submarine landslides and gas-hydrate
  instability are assessed with the same toolbox
  ([15-02 Marine Geophysical Methods](../../15-oceanography-marine/02-marine-geophysics-methods/README.md)).

## 14. Further reading

- **Lamb, H. *Hydrodynamics* (Cambridge University Press).** The classical
  derivation of the long-wave dispersion relation and the shoaling law; still the
  clearest account of why (2) and (5) are what they are. Level: graduate,
  historical.
- **Satake, K., & Tanioka, Y., and the tsunami-review literature.** The physics
  of generation, including the Kajiura filter and the slow-rupture problem, in
  the standard review form. Level: graduate.
- **Synolakis, C. E., & Bernard, E. N. (2006). "Tsunami science before and beyond
  Boxing Day 2004." *Philosophical Transactions of the Royal Society A*.** A
  review of the science and of the warning-system response, useful for the
  operational half of this lesson. Level: advanced.
- **NOAA National Centers for Environmental Information and the NOAA Tsunami
  Program, <https://www.ncei.noaa.gov> and <https://www.noaa.gov>.** The
  authoritative archives for historical tsunami data and the source of the
  observation records that calibrate any model; the main NOAA site blocks
  automated requests and is intended for a browser. Level: reference.
- **Intergovernmental Oceanographic Commission and national warning centres.**
  The operational products — bulletins, travel-time charts and alert levels —
  are the documents that show what a warning actually contains. Confirm current
  procedures with the responsible agency. Level: reference.
- **OpenTopography, <https://www.opentopography.org/>.** High-resolution
  topography and bathymetry, the input every travel-time and inundation
  calculation needs. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 15. Related lessons

- [04-07-01 Earthquake Hazard and Ground Motion](./01-earthquake-hazard.md) —
  the rupture that supplies the seafloor displacement.
- [04-07-02 Volcanic Hazards, Monitoring and Precursors](./02-volcanic-hazards.md)
  — flank collapse as a tsunami source.
- [04-07-04 Subsidence, Sinkholes and Karst](./04-subsidence-sinkholes.md) —
  the coastal setting, including the subsidence that changes the shoreline a
  tsunami runs against.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md)
  — the full dispersion theory from which (1) is taken.
- [15-06 Sea Level Change and Marine Records](../../15-oceanography-marine/06-sea-level-change-marine/README.md)
  — the sea level that a tsunami is superimposed on.
- [17-03 Radar Remote Sensing](../../17-remote-sensing-gis/03-radar-remote-sensing/README.md)
  — the remote sensing of sea surface height and roughness used in tsunami
  detection and in observing the ionospheric signature.

Exercises:
[`exercises/05-tsunami-exercises.md`](./exercises/05-tsunami-exercises.md)
and
[`exercises/05-tsunami-solutions.md`](./exercises/05-tsunami-solutions.md).

## Self-assessment checklist

- [ ] I can derive $c = \sqrt{gh}$ as the $kh \to 0$ limit of the dispersion
      relation and state the condition as $L \gg 2\pi h$. (§1)
- [ ] I can compute the exact finite-depth phase speed and the leading-order
      error $k^2h^2/6$. (§1)
- [ ] I can compute a wavelength, a travel time, and say which segments of a path
      dominate the travel time. (§2)
- [ ] I can derive Green's law and compute a shoaling amplification. (§3)
- [ ] I can derive the Kajiura filter, evaluate it, and state the crossover
      wavelength. (§4)
- [ ] I can derive and apply Snell's law for a tsunami. (§5)
- [ ] I can derive the bore speed and the flow behind the front from mass and
      momentum conservation. (§6)
- [ ] I can compute the seafloor pressure for a given sea-surface elevation and
      state the detection threshold. (§7)
- [ ] I can explain why a bottom-pressure sensor sees a tsunami and not a wind
      sea, using one formula. (§7)
- [ ] I can state why a warning contains a better arrival time than an arrival
      height. (§2, §8)
