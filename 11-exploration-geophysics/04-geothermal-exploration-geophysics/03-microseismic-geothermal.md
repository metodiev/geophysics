---
id: 11-04-03
title: "Microseismic Monitoring of Geothermal Fields"
level: doctoral
prereqs: ["11-04-01", "06-12-01", "06-03-05"]
tags: [exploration-geophysics, geothermal, microseismic, monitoring, induced-seismicity]
---

# Microseismic Monitoring of Geothermal Fields

**All models and data in this module are SYNTHETIC.** The stress drops, rupture
radii, noise levels, network geometries and hydraulic properties below are
chosen teaching values. No field, operator, well or published catalogue is
described. Physical constants and stated conventions are given with units.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the moment–area–stress-drop scaling for a circular rupture and
   **compute** moment, magnitude, mean slip and corner frequency for a stated
   rupture radius.
2. **Explain** the non-uniqueness in interpreting a single event, and **state**
   which quantity is assumed rather than measured.
3. **Build** a detection model from geometric spreading and absorption and
   **compute** the detection radius as a function of magnitude.
4. **Explain** why the magnitude of completeness is a function of position, and
   **demonstrate** the bias it produces in a fitted $b$-value.
5. **Quantify** the location error of a monitoring geometry and the systematic
   bias produced by a velocity-model error.
6. **Compute** the pore-pressure diffusion front for a stated permeability and
   time, and **relate** it to where microseismicity can occur.
7. **Write** an uncertainty statement for a microseismic interpretation that a
   reviewer could check.

## Prerequisites

- [11-04-01 Geophysical Signatures of Geothermal Reservoirs](01-geothermal-signatures.md) —
  the heat, permeability and caprock framework.
- [06-12-01 Causes of Induced Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/01-induced-seismicity-causes.md) —
  injection, pore pressure and triggering mechanisms.
- [06-03-05 Source Spectra, Corner Frequency and Stress Drop](../../06-seismology/03-earthquake-sources/05-source-spectra.md) —
  the source physics used for the magnitude and corner-frequency relations.

## 1. Why monitor microseismicity at all

Every surface geophysical method measures a proxy for the rock, and none of them
responds to **fluid movement**. Microseismicity does: it is the elastic
radiation from small shear slips on pre-existing fractures whose effective
normal stress was reduced by a pressure increase. That makes it the only
measurement in this module that is caused by the process the resource depends
on — circulation through a fracture network.

The discipline, however, is in what the resulting event cloud means:

| interpretation people make | what the data support |
|---|---|
| "the cloud is the flow path" | the cloud is where rock slipped |
| "the cloud volume is the stimulated volume" | the cloud is a location set with error bars (§5) |
| "the event rate is the flow rate" | the event rate is a response to a pressure and stress change in an already-fractured rock |
| "a bigger event means a bigger fracture" | moment, stress drop and rupture area trade off in a single event (§2) |

The rest of the lesson computes each of those statements to the precision the
data permit.

## 2. Source scaling

For a circular rupture of radius $a$ and a uniform static stress drop
$\Delta\sigma$, the seismic moment is

$$M_0 = \frac{16}{7}\,\Delta\sigma\,a^{3},
\qquad
M_w = \frac{2}{3}\left(\log_{10}M_0 - 9.1\right)\quad (M_0\ \text{in N m}),$$

and the mean slip follows from the definition of moment, $M_0 = \mu A\bar{u}$
with $A = \pi a^{2}$:

$$\bar{u} = \frac{M_0}{\mu\,\pi a^{2}} = \frac{16}{7\pi}\frac{\Delta\sigma\,a}{\mu}.$$

The corner frequency of the far-field spectrum is inversely proportional to
rupture size,

$$f_c = \frac{K\,v_s}{2\pi a},$$

with $K = 2.34$ the standard Brune-model coefficient (a stated convention, not
a derived constant).

*Numbers* ($\mu = 25$ GPa, $\Delta\sigma = 3$ MPa, $v_s = 3.0\
\mathrm{km\,s^{-1}}$):

| radius $a$ (m) | $M_0$ (N m) | $M_w$ | mean slip (mm) | $f_c$ (Hz) |
|---|---|---|---|---|
| 50 | $8.571\times10^{11}$ | 1.89 | 4.4 | 22.35 |
| 100 | $6.857\times10^{12}$ | 2.49 | 8.7 | 11.17 |
| 200 | $5.486\times10^{13}$ | 3.09 | 17.5 | 5.59 |
| 500 | $8.571\times10^{14}$ | 3.89 | 43.7 | 2.23 |

Three interpretative facts to take from this table:

1. **Magnitude scales as the cube of the radius**, so an order of magnitude in
   moment is a factor 2.15 in radius. A magnitude difference of 1 is a factor
   5.6 in radius and 2.15 in slip.
2. **Slip is millimetres to centimetres.** These are not faults moving as
   geological structures; they are small patches of an existing fracture
   network releasing accumulated elastic strain.
3. **The corner frequency falls below the useful band for large events.** A
   500 m rupture radiates at 2.2 Hz, close to the low-frequency limit set by
   attenuation and instrument response in many settings — which is exactly why
   large events are detected far away (§3).

**The non-uniqueness.** A single event yields $M_0$ (from amplitude) and $f_c$
(from spectrum), and hence $a$; but $\Delta\sigma$ is then *assumed*, and
$\bar{u}$ follows from it. Two analysts assuming 1 MPa and 10 MPa will report
slips differing by an order of magnitude and identical moments. Reporting a
stress drop requires either many events with an independent magnitude scale or
an explicit statement that it is assumed.

## 3. Detection: why a network sees what it sees

A working amplitude model for a point source in a lossy half-space is geometric
spreading times absorption:

$$A(r) = \frac{A_0}{r}\exp\left(-\frac{\pi f_c\,r}{Q\,v_s}\right),$$

where the frequency used is the *source's own* corner frequency, because that is
where its energy is concentrated. The demonstration normalises amplitudes so
that an $M_w = 0$ event at 1 km has amplitude 1.0 and adopts a detection
threshold of $10^{-2}$ (Q = 50):

| $M_w$ | radius (m) | $f_c$ (Hz) | detection radius (m) | absorption loss at 2 km (%) |
|---|---|---|---|---|
| −1.0 | 2 | 621.64 | 650 | 100.0 |
| −0.5 | 3 | 349.57 | 1100 | 100.0 |
| 0.0 | 6 | 196.58 | 2000 | 100.0 |
| 0.5 | 10 | 110.54 | 3500 | 99.0 |
| 1.0 | 18 | 62.16 | 6200 | 92.6 |
| 1.5 | 32 | 34.96 | 11000 | 76.9 |
| 2.0 | 57 | 19.66 | 19600 | 56.1 |
| 2.5 | 101 | 11.05 | 34800 | 37.1 |
| 3.0 | 180 | 6.22 | 61850 | 22.9 |

The pattern is counter-intuitive until the frequency is read alongside it:
**large events are detected far away because their energy sits at low
frequency, where the rock is transparent**, while a $M_w = -1$ event radiates at
620 Hz and is gone within a kilometre. Consequently:

- the **magnitude of completeness is a function of position**, not a network
  property;
- a catalogue assembled from a real network is **spatially biased**: near the
  sensors it is complete to a much lower magnitude than far away;
- the spatial bias is *not* fixed by better processing — only by adding sensors
  or lowering the noise floor.

## 4. Catalogue statistics, and a bias worth measuring

Magnitudes in a catalogue follow the Gutenberg–Richter relation

$$\log_{10}N(\ge M) = a - bM,$$

with $b \approx 1$ for tectonic seismicity (a convention in wide use). The
maximum-likelihood estimator for $b$ above a completeness threshold $M_c$ is
Aki's formula

$$\hat{b} = \frac{\log_{10}e}{\bar{M} - M_c} = \frac{1}{\ln 10\,
\left(\bar{M}-M_c\right)} .$$

The demonstration simulates 40 000 events uniformly in a half-space to 6 km
radius, with $b = 1$ above $M_w = -1.5$, applies the detection model of §3, and
fits $b$ to the *detected* catalogue:

| $M_c$ used | events above | fitted $b$ |
|---|---|---|
| −1.5 | 4021 | **0.347** |
| −0.5 | 2682 | 0.744 |
| 0.0 | 1247 | 0.980 |
| 0.5 | 407 | 0.979 |
| 1.0 | 138 | 1.028 |

Of 40 000 events, only **4021 (10.1%)** were detected at all. Fitting the raw
catalogue at a low $M_c$ returns $b = 0.35$ against a true $b = 1.0$ — a
two-thirds error, entirely manufactured by the detection geometry: distant small
events are missing while nearby small events are kept, so the surviving
magnitude distribution is flattened. Above $M_c \approx 0$ the fit is correct
(0.98–1.03) because the catalogue is complete at those magnitudes out to 6 km.

**The methodological rule: never fit a $b$-value to a raw geothermal catalogue.**
Estimate $M_c$ as a function of position (using a detection model like §3, or
the maximum-curvature and stability methods per node), keep only events above
the local $M_c$, and report the $M_c$ map alongside $b$
([06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)).

## 5. Location: geometry, then velocity

Two error sources dominate, and they are of different character.

**Random (picking) error.** With a 2 ms pick error, $v = 3.0\
\mathrm{km\,s^{-1}}$, a known origin time and 100 realisations, the demonstration
locates an event at (500, 200, −3000) m with an 8-level downhole array
(−2000 to −3500 m) plus four surface stations:

| case | 3-D offset (m) | horizontal (m) | depth (m) |
|---|---|---|---|
| picks and location both at 3.15 km/s | 35 | 35 | +0 |
| picks 3.15, location 3.00 (5% slow) | 158 | 157 | −7 |
| picks 2.85, location 3.00 (5% fast) | 186 | 186 | +3 |

Two results deserve emphasis:

1. **With the right velocity the error is tens of metres and unbiased in
   depth**, because combining downhole and surface stations breaks the
   depth–origin-time trade-off that a purely vertical array suffers from
   ([11-03-05 §6](../03-hydrocarbon-exploration/05-unconventional-geophysics.md)).
2. **A 5% velocity error multiplies the error by about five and pushes it into
   the horizontal coordinates.** It is *systematic*: it does not average out over
   a thousand events, it biases the whole cloud, and it is the reason a
   calibration shot into the reservoir is the highest-value single measurement
   in a monitoring programme.

The corollary for interpretation: any statement about cloud dimensions, growth
direction or the asymmetry of a cloud must be compared with the location bias,
not only with the location scatter. A 200 m horizontal bias will make a
symmetric cloud look azimuthally organised.

## 6. Pressure diffusion, triggering and mitigation

The pressure disturbance from an injection diffuses; for a homogeneous, single
phase, isothermal reservoir the hydraulic diffusivity is

$$D = \frac{k}{\mu_w\,\phi\,c_t}, \qquad
L \approx \sqrt{4Dt},$$

where $k$ is permeability, $\mu_w$ the fluid viscosity, $\phi$ porosity and
$c_t$ total compressibility. The demonstration uses
$\mu_w = 3\times10^{-4}\ \mathrm{Pa\,s}$, $\phi = 0.05$ and
$c_t = 10^{-9}\ \mathrm{Pa^{-1}}$:

| permeability | $D$ (m²/s) | $L$ at 1 day | 30 days | 365 days |
|---|---|---|---|---|
| 0.1 mD | 0.0066 | 48 m | 261 m | 911 m |
| 1 mD | 0.0658 | 151 m | 826 m | 2881 m |
| 10 mD | 0.6579 | 477 m | 2612 m | 9110 m |
| 100 mD | 6.5795 | 1508 m | 8259 m | 28 809 m |

The front grows as $\sqrt{t}$: ten times the time moves it 3.2×, and ten times
the permeability moves it 3.2× as well. Two conclusions:

- the **footprint of a stimulation experiment** is a square-root function of
  time and a square-root function of permeability, so a decade of uncertainty in
  permeability is a factor 3 in the extent;
- where the front reaches a fracture already close to failure, slip occurs; the
  Coulomb condition is $\tau \ge \mu_f(\sigma_n-P)$
  ([11-03-05 §7](../03-hydrocarbon-exploration/05-unconventional-geophysics.md)),
  and the pressure change needed can be anywhere from zero (a critically
  stressed fault) to tens of MPa.

This is why mitigation is organised as a **response protocol** rather than a
prediction ([06-12-04](../../06-seismology/12-induced-and-triggered-seismicity/04-monitoring-and-mitigation.md)):
the traffic-light scheme maps observed magnitude to an action (continue, reduce,
stop), because no model available before the event can predict which fracture
will slip. The physical content of the protocol is that it converts a
statistical observation into a controlled operational decision — and its
effectiveness depends on the location and magnitude accuracy computed in §3–§5.

## 7. Worked examples

### Example 1 — an event, end to end

A recorded event has $M_0 = 5\times10^{11}$ N m and $f_c = 15$ Hz, with
$v_s = 3.0\ \mathrm{km\,s^{-1}}$ and $\mu = 25$ GPa.

1. $M_w = \tfrac23(\log_{10}5\times10^{11} - 9.1) = \tfrac23(11.699 - 9.1) =
   1.73$.
2. Radius: $a = K v_s/(2\pi f_c) = 2.34\times3000/(2\pi\times15) = 74.5$ m.
3. With an assumed $\Delta\sigma = 3$ MPa, $M_0 = (16/7)\Delta\sigma a^3$ gives
   $2.286\times3\times10^{6}\times4.13\times10^{5} = 2.8\times10^{12}$ N m,
   which is **5.6× the measured moment** — so the assumed stress drop is
   inconsistent with the measured moment and corner frequency. Either
   $\Delta\sigma \approx 0.53$ MPa, or the corner frequency is biased by
   attenuation and the radius is smaller than 74.5 m. **This is the
   non-uniqueness in action**: the same event supports both statements, and the
   physics of attenuation must be invoked to choose.
4. Slip with $\Delta\sigma = 0.53$ MPa:
   $\bar{u} = M_0/(\mu\pi a^2) = 5\times10^{11}/(25\times10^{9}\times\pi
   \times5.55\times10^{3}) = 1.15\times10^{-3}$ m = 1.15 mm.

### Example 2 — a detection budget

An operator wants to detect $M_w = 0$ events throughout a 3 km radius. From §3
the detection radius for $M_w = 0$ is 2000 m at the assumed noise floor — not
enough. Options, with the resulting radii from the same model: raise the sensor
sensitivity (a factor 10 in amplitude raises $A_0$, i.e. the effective radius
rises roughly in proportion: the demonstration's 3× amplitude gain moved the
radius from 840 to 1990 m, a factor 2.4); add sensors so the maximum
source–receiver distance falls below 2000 m (a coverage problem, not a
detection problem); or accept a higher $M_c$ beyond 2 km and report it. The
wrong answer is to report a complete catalogue.

### Example 3 — the pressure front versus a well spacing

Wells are 1.2 km apart and the target permeability is 1 mD. From the table the
front reaches 826 m in 30 days and 2881 m in a year. The 1.2 km spacing is
therefore flooded (in the diffusive sense) within roughly $t = L^2/(4D)$ with
$L = 600$ m: $t = 3.6\times10^{5}/0.263 = 1.37\times10^{6}$ s ≈ 16 days. So
interference between wells is expected within weeks at 1 mD, and the monitoring
geometry should be designed for that.

## 8. Assumptions and regime of validity

1. **Circular-crack, uniform-stress-drop source.** Real ruptures are irregular,
   and the 16/7 coefficient assumes a specific crack model; the scaling
   $M_0\propto a^3$ is robust, the constant is not.
2. **The Brune coefficient ($K = 2.34$) is a convention.** Different source
   models give different constants, so radii from $f_c$ carry a systematic
   factor of order 2.
3. **Amplitude model is isotropic point radiation.** Radiation patterns,
   directivity, and site effects modify amplitudes by factors comparable to the
   magnitude differences used to build detection curves.
4. **Constant $Q$, homogeneous velocity.** Real attenuation and velocity vary;
   the detection model is a design tool, not a calibration.
5. **Gutenberg–Richter with $b = 1$.** The $b$-value is a *measured* property of
   a catalogue, not a constant, and it requires a magnitude of completeness
   (§4).
6. **Homogeneous, single-phase, isothermal diffusion.** Two-phase flow,
   thermo-elastic stress changes, fracture opening and poroelastic coupling all
   change the front; the square-root scaling is robust, the coefficient is not.
7. **Location requires a velocity model.** The demonstrated 5% bias is typical;
   a calibration shot is the standard remedy.
8. **Non-uniqueness is intrinsic.** Moment, stress drop and area cannot all be
   determined from a single event, and no processing trick changes that.

## 9. Units and dimensional consistency

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| seismic moment | $M_0$ | N m | $\mu A \bar{u}$ |
| corner frequency | $f_c$ | Hz | $v/a$ |
| mean slip | $\bar{u}$ | m | moment/(modulus × area) |
| diffusivity | $D$ | m² s⁻¹ | $k/(\mu\phi c_t)$ |
| front distance | $L$ | m | $\sqrt{Dt}$ |
| permeability | $k$ | m² | 1 D = $9.869\times10^{-13}$ m² |
| compressibility | $c_t$ | Pa⁻¹ | |

The moment–magnitude relation requires $M_0$ in **N m**; using dyn·cm
(1 N m = $10^{7}$ dyn cm) is a classic source of a 2.33 magnitude error — the
constant 9.1 is defined for SI.

## 10. Python demonstration

`code/microseismic_geothermal_demo.py` prints:

1. moment, magnitude, slip and corner frequency for four rupture radii;
2. the detection radius by magnitude, with the absorption loss at 2 km;
3. a 40 000-event synthetic Gutenberg–Richter catalogue, the detected fraction,
   and the biased $b$-values fitted at five completeness thresholds;
4. location error, horizontal error and depth error for three velocity-model
   cases;
5. the hydraulic-diffusivity and pressure-front table.

It is print-only, seeded with `np.random.default_rng(20261014)` and exits 0.

## 11. Exercises

- [`exercises/03-microseismic-geothermal-exercises.md`](exercises/03-microseismic-geothermal-exercises.md)
- [`exercises/03-microseismic-geothermal-solutions.md`](exercises/03-microseismic-geothermal-solutions.md)

## Mastery checkpoint

> An event is recorded by a five-station array at 1.5–2.5 km range with a 1.5 ms
> pick error on a homogeneous $v_s = 3.2\ \mathrm{km\,s^{-1}}$ model. Its moment
> is $2\times10^{12}$ N m and its corner frequency is 8 Hz. **(a)** Compute
> $M_w$ and the rupture radius (with the stated Brune coefficient). **(b)** With
> an assumed stress drop of 5 MPa, compute the moment the scaling predicts and
> state the inconsistency, if any. **(c)** Compute the mean slip for the
> measured moment and the radius of (a). **(d)** Using $L=\sqrt{4Dt}$ with
> $D = 0.2\ \mathrm{m^{2}\,s^{-1}}$, compute how long a pressure front takes to
> reach 500 m. **(e)** State one sentence about what the event cloud does *not*
> tell you.

## Common pitfalls

1. **Calling an event cloud a flow path.** It is a set of locations where rock
   slipped, in an assumed velocity model.
2. **Quoting a stress drop as a measurement.** It is an assumption unless there
   is an independent constraint.
3. **Fitting $b$ to a raw catalogue.** The demonstration's bias is a factor of
   three at a naive $M_c$.
4. **Ignoring the spatial variation of $M_c$.** A single completeness value
   describes no real network.
5. **Reporting cloud dimensions without the velocity-model bias.** It is
   systematic and larger than the scatter.
6. **Treating the traffic-light thresholds as a physical prediction.** They are
   an operational response framework.

## Related modules

- [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md) —
  mechanisms, pore-pressure diffusion and mitigation protocols.
- [06-04 Earthquake Location and Magnitude](../../06-seismology/04-earthquake-location-and-magnitude/README.md) —
  the location and magnitude machinery this lesson specialises.
- [11-03-05 Geophysics for Unconventional Reservoirs](../03-hydrocarbon-exploration/05-unconventional-geophysics.md) —
  the same monitoring physics with a stimulation focus.
- [06-07 Ambient Noise and Interferometry](../../06-seismology/07-ambient-noise-and-interferometry/README.md) —
  passive methods that complement microseismic monitoring.
- [11-04-02 Magnetotellurics for Geothermal Resource Assessment](02-mt-for-geothermal.md) —
  the resistivity constraint on the same reservoir.
- [11-07-03 Case Study: Geothermal Field Development](../07-exploration-case-studies/03-case-study-geothermal.md) —
  how monitoring enters a development decision.

## Further reading

- Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press. Level: textbook. Source scaling and survey
  geometry for small events.
- Telford, W. M., Geldart, L. P., & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press. Level: textbook. Seismic
  sources and amplitudes.
- Kearey, P., Brooks, M., & Hill, I. (2002). *An Introduction to Geophysical
  Exploration* (3rd ed.). Blackwell. Level: textbook. Monitoring and method
  integration in resource exploration.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.
