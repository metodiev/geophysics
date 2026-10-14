---
id: 07-02-05
title: "Airborne and Marine Gravity: Platforms and Eotvos Corrections"
level: doctoral
prereqs: ["07-02-04", "07-01-04", "02-02-05"]
tags: [gravity, instruments, airborne-gravity, marine-gravity, eotvos, moving-platform, navigation]
---

# Airborne and Marine Gravity: Platforms and Eotvos Corrections

**All models and data in this module are SYNTHETIC.** Platform speeds, headings,
GNSS noise, filter cut-offs, line biases and turbulence amplitudes are chosen
teaching values. No aircraft, ship, survey or published dataset is used or implied.
The exact quantities used are the WGS84 rotation rate
$\omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$,
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$, and the unit relations
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$,
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$, with the SI definition
$1\ \mathrm{knot} = 0.514444\ \mathrm{m\,s^{-1}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Eötvös correction from the rotating-frame acceleration, and
   **verify** the familiar coefficient for speeds in knots from $\omega$ and the
   definition of the knot.
2. **Compute** the correction for aircraft and ship speeds, and **explain** its
   heading dependence, including the counter-intuitive behaviour of *sensitivity*
   versus *magnitude*.
3. **Compute** the centrifugal term $V^{2}/R$ for a turn and **state** why turns are
   discarded or modelled rather than corrected.
4. **Derive** the noise amplification $\sigma_{a} \approx \sigma_{z}\left(2\pi
   f\right)^{2}$ of a doubly differentiated GNSS position, and **compute** the
   position accuracy a target gravity accuracy demands.
5. **Explain** why no filter can remove platform acceleration that overlaps the
   signal band, and **quantify** the leakage with a stated spectrum.
6. **Perform** a cross-over adjustment of a marine grid, and **state** what is and is
   not recoverable from cross-overs alone.
7. **Assemble** a moving-platform error budget and **identify** which terms the
   navigation, not the gravimeter, controls.

## Prerequisites

- [07-02-04 Practical Correction Workflow and Processing Sequence](04-corrections-workflow.md)
  — the reduction chain into which the moving-platform corrections enter.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md)
  — the terms applied after the platform corrections.
- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](../../02-physics/02-classical-mechanics/05-rotation.md)
  — rotating and non-inertial frames, from which the Eötvös term follows.

## 1. What changes when the instrument moves

A stationary gravimeter measures one number at one place. A moving gravimeter
measures the vector sum of gravity, the platform's own acceleration, and the
accelerations that appear because the Earth rotates:

$$a_{\text{measured}} = g + a_{\text{platform}} + a_{\text{frame}}.$$

The three terms have completely different sizes, and the whole engineering of
airborne and marine gravity lies in separating them:

| term | typical size | how it is handled |
|---|---|---|
| gravity | $10^{6}\ \mathrm{mGal}$, anomaly $1$–$100\ \mathrm{mGal}$ | the target |
| frame acceleration (Eötvös) | up to $10^{3}\ \mathrm{mGal}$ for aircraft | computed from position, speed and heading |
| platform acceleration | up to $10^{5}\ \mathrm{mGal}$ in turbulence | measured and subtracted |

The lesson is that **the two nuisance terms are two to five orders of magnitude
larger than the signal**, and that both are *navigation* problems rather than
instrument problems. On a moving platform, the gravimeter is only one of several
sensors.

## 2. The Eötvös correction, derived

### 2.1 Derivation

In the rotating frame of the Earth, a platform moving with horizontal velocity
$\mathbf{V}$ experiences the Coriolis acceleration $-2\boldsymbol{\Omega}\times
\mathbf{V}$ and, on a curved path, a centrifugal acceleration. Taking only the
vertical components, with $\Omega$ the rotation rate, $\varphi$ the latitude and
$\alpha$ the heading measured from north,

$$a_{E} = 2\,\Omega\,V\cos\varphi\,\sin\alpha + \frac{V^{2}}{R},$$

where the second term is the centrifugal term for a turn or course change of radius
$R$ (zero on a straight, great-circle course when the $V^{2}/R$ is absorbed into the
Earth's curvature correction). **Derived check:** in mGal per unit speed,

$$2\Omega \times 10^{5} = 14.5842\ \mathrm{mGal\ per\ m\,s^{-1}},$$

and converting to knots,

$$2\Omega \times 0.514444 \times 10^{5} = 7.5028\
\mathrm{mGal\ per\ knot},$$

which is the familiar coefficient $7.503$ for speeds in knots. It is *derived* here
from $\omega$ and the definition of the knot; quoting it without that derivation
would hide the fact that it contains the Earth's rotation rate and the whole
conversion chain.

### 2.2 Size and heading dependence (SYNTHETIC, $45^\circ$ latitude)

| platform | speed | $0^\circ$ | $45^\circ$ | $90^\circ$ | $180^\circ$ | $270^\circ$ |
|---|---|---|---|---|---|---|
| aircraft | 70 m/s (136.1 kn) | 0.00 | +510.45 | +721.88 | 0.00 | $-721.88$ |
| aircraft | 90 m/s (174.9 kn) | 0.00 | +656.29 | +928.13 | 0.00 | $-928.13$ |
| ship | 5 m/s (9.7 kn) | 0.00 | +36.46 | +51.56 | 0.00 | $-51.56$ |
| ship | 10 m/s (19.4 kn) | 0.00 | +72.92 | +103.13 | 0.00 | $-103.13$ |

(all values in mGal). On east-west headings the correction is *equal and opposite*
for the two directions, and a $70\ \mathrm{m\,s^{-1}}$ aircraft differs by
$1443.77\ \mathrm{mGal}$ between a due-east and a due-west line: three orders of
magnitude above any target anomaly. On north-south headings the correction vanishes
identically.

### 2.3 The counter-intuitive part: magnitude versus sensitivity

Since $a_{E} = A\sin\alpha$ with $A = 721.88\ \mathrm{mGal}$ at this speed and
latitude,

$$\frac{\partial a_{E}}{\partial\alpha} = A\cos\alpha
\;\Longrightarrow\;
\begin{cases}
12.599\ \mathrm{mGal\ per\ degree} & \text{at } \alpha = 0^\circ \text{ or } 180^\circ,\\
8.909\ \mathrm{mGal\ per\ degree} & \text{at } \alpha = 45^\circ,\\
0.000\ \mathrm{mGal\ per\ degree} & \text{at } \alpha = 90^\circ.
\end{cases}$$

**The correction is largest where its sensitivity to heading vanishes, and its
sensitivity is largest where the correction itself is zero.** A $0.1^\circ$ heading
error costs $1.26\ \mathrm{mGal}$ on a north-south line and only
$0.89\ \mathrm{mGal}$ at $45^\circ$; the heading must therefore be known best where
the correction is *smallest*. This is the kind of conclusion that must be computed
rather than intuited, and it is the reason navigation requirements are set per line
direction rather than globally.

## 3. Turns: the centrifugal term

During a turn of radius $R$ the platform also feels $V^{2}/R$ toward the turn
centre, whose vertical component must be modelled or the line abandoned:

| speed (m/s) | turn radius (m) | $V^{2}/R$ ($\mathrm{m\,s^{-2}}$) | $V^{2}/R$ (mGal) |
|---|---|---|---|
| 5.0 (ship) | 2000 | 0.012500 | 1250.0 |
| 5.0 | 5000 | 0.005000 | 500.0 |
| 5.0 | 20000 | 0.001250 | 125.0 |
| 70.0 (aircraft) | 2000 | 2.450000 | 245 000.0 |
| 70.0 | 5000 | 0.980000 | 98 000.0 |
| 70.0 | 20000 | 0.245000 | 24 500.0 |

An aircraft turn at $70\ \mathrm{m\,s^{-1}}$ and a 5 km radius produces
$98\,000\ \mathrm{mGal}$ of vertical acceleration — five orders of magnitude above
the anomaly being measured. Three practices follow, and all three are used in
practice:

1. **Fly straight and level while measuring**, and place all turns between lines,
   where the data are discarded.
2. **Model the turn** with the measured heading rate, speed and roll angle when the
   platform is good enough to keep the data.
3. **Use the cross-overs**: lines that cannot be corrected can still be tied to
   others at their intersections (Section 6).

## 4. Separating platform acceleration with GNSS

A gravimeter on a platform measures $g + a_{\text{platform}}$, so the platform
acceleration must be measured independently. GNSS positions are differentiated twice
for it, and differentiation amplifies noise as $\left(2\pi f\right)^{2}$:

$$\sigma_{a} \approx \sigma_{z}\left(2\pi f\right)^{2},$$

where $f$ is the cut-off of the band in which the differentiated position is used.

**Measured (SYNTHETIC, $f = 0.005\ \mathrm{Hz}$, a 200 s draper cut-off):**

| $\sigma_{z}$ (m) | $\sigma_{a}$ ($\mathrm{m\,s^{-2}}$) | $\sigma_{a}$ (mGal) |
|---|---|---|
| 0.01 | $9.870\times10^{-6}$ | 0.987 |
| 0.05 | $4.935\times10^{-5}$ | 4.935 |
| 0.10 | $9.870\times10^{-5}$ | 9.870 |
| 0.50 | $4.935\times10^{-4}$ | 49.348 |

**A 5 cm vertical position accuracy gives $4.93\ \mathrm{mGal}$ of noise in the band
that matters; 50 cm gives $49.3\ \mathrm{mGal}$.** The survey's accuracy is set by
the position accuracy, not by the gravimeter, and the quadratic dependence on $f$ is
why the correction is *split*: the long-wavelength part comes from GNSS, and the
short-wavelength part from a vertical accelerometer or a gyro-stabilised platform.
Choosing $f$ is choosing which sensor supplies which band, and it must be stated.

## 5. Why filtering cannot replace measuring

A natural hope is that the platform acceleration, being in a different band from the
gravity signal, could be filtered out. It cannot, for two reasons: the bands overlap,
and the amplitude ratio is enormous.

**Measured (SYNTHETIC spectrum).** Take white acceleration of
$0.5\ \mathrm{m\,s^{-2}}$ (turbulence) over the band below $0.05\ \mathrm{Hz}$, a
gravity band signal of $1.0\times10^{-4}\ \mathrm{m\,s^{-2}}$, and a 4-pole filter
at $0.005\ \mathrm{Hz}$:

| quantity | value |
|---|---|
| turbulence amplitude | $0.5\ \mathrm{m\,s^{-2}} = 50\,000\ \mathrm{mGal}$ |
| gravity band amplitude | $1.0\times10^{-4}\ \mathrm{m\,s^{-2}} = 10\ \mathrm{mGal}$ |
| amplitude ratio | 5000 : 1 |
| leakage into the signal band after filtering | $5.438\times10^{-4}\ \mathrm{m\,s^{-2}} = 54.376\ \mathrm{mGal}$ |

The leakage exceeds the signal by a factor of five. **No filter removes a component
that overlaps the signal band**, and here the overlapping component is 5000 times
larger than the signal. The engineering conclusion is unambiguous: the platform
acceleration must be *measured* (accelerometer, GNSS, or a gyro-stabilised platform)
and subtracted, and the filter's role is only to define which measurement is used in
which band.

This also explains why the correction chain has the structure it does: a low-pass
part from GNSS (accurate at long wavelength), a high-pass part from the accelerometer
(or the platform's own feedback), and a hand-off frequency chosen so that both
sensors' errors are below the target in their assigned bands.

## 6. Cross-overs: the marine equivalent of a loop closure

Marine surveys are usually flown/sailed as a grid. Where an east-west line crosses a
north-south line, both measure the same gravity, so the difference between them
measures the *mismatch of the two lines' errors* — the marine analogue of a loop
closure. **Measured (SYNTHETIC grid, 6 × 6 lines):**

| quantity | value |
|---|---|
| cross-overs | 36 |
| per-line bias scatter (SYNTHETIC) | 3.67 mGal |
| cross-over noise | 0.3 mGal |
| cross-over difference rms, before adjustment | 5.211 mGal |
| after a weighted least-squares line-bias adjustment | 0.245 mGal (predicted 0.30) |
| difference between recovered and true *relative* biases | 0.111 mGal rms |

Three properties of the adjustment matter.

1. **It works.** The residual falls from $5.211$ to $0.245\ \mathrm{mGal}$, i.e. to
   the cross-over noise level. The adjustment is a least-squares solution of
   $\Delta_{ij} = b_{i} - b_{j} + \epsilon$ for the line biases $b$.
2. **Only relative biases are determined.** Cross-overs constrain *differences* of
   line biases, so the average bias is unobservable from cross-overs alone: the
   recovered values differ from the truth by exactly a constant, and the demonstration
   fixes one line as the gauge. The absolute level still needs a tie.
3. **The residual is the test.** If the post-adjustment residual exceeds the
   cross-over noise, the model (a constant bias per line) is inadequate — a
   time-dependent drift, a heading-dependent error, or an Eötvös error on some lines.

The cross-over adjustment is therefore the moving-platform version of the base
occupation: a set of observations, independent of the target signal, that measures
the *procedure*.

## 7. A moving-platform error budget

**Measured (SYNTHETIC, aircraft at $70\ \mathrm{m\,s^{-1}}$, $45^\circ$ latitude):**

| term | mGal |
|---|---|
| gravimeter noise (1 mGal per reading, 0.1 mGal after averaging) | 0.100 |
| Eötvös from a $0.1^\circ$ heading error at a $45^\circ$ heading | 0.890 |
| Eötvös from a $0.5\ \mathrm{m\,s^{-1}}$ speed error | 5.156 |
| platform acceleration leaking through filtering (Section 5) | 54.376 |
| GNSS-derived vertical acceleration (5 cm at 5 mHz) | 4.935 |
| latitude/position error ($0.0001^\circ$) | 0.045 |
| reduction density error ($100\ \mathrm{kg\,m^{-3}}$ through 500 m of terrain) | 0.500 |
| **total in quadrature** | **54.852** |

Two readings of the table:

1. **The filtering row is a design choice, not a law.** If the platform acceleration
   is *measured* rather than filtered, that row is replaced by the GNSS row
   ($4.935\ \mathrm{mGal}$) and the budget falls by an order of magnitude, to about
   $7\ \mathrm{mGal}$. That single comparison is the design argument for modern
   airborne gravity: the gain comes from an accelerometer and good navigation, not
   from a quieter gravimeter.
2. **The navigation terms dominate the instrument by an order of magnitude.** A
   $0.5\ \mathrm{m\,s^{-1}}$ speed error alone costs $5.16\ \mathrm{mGal}$; a
   $0.1^\circ$ heading error costs $0.89\ \mathrm{mGal}$ on the worst line. The
   gravimeter's $0.1\ \mathrm{mGal}$ is the smallest number in the table.

## 8. Worked example — a full platform correction for one flight line

A SYNTHETIC aircraft flies $220\ \mathrm{s}$ at $70\ \mathrm{m\,s^{-1}}$ and a
heading of $45^\circ$ at $45^\circ$ latitude, with a measured vertical acceleration
from turbulence of $0.02\ \mathrm{m\,s^{-2}}$ rms.

1. **Eötvös:** $a_{E} = 2\times7.292115\times10^{-5}\times70\times\cos45^\circ
   \times\sin45^\circ = 5.1045\times10^{-3}\ \mathrm{m\,s^{-2}} =
   510.45\ \mathrm{mGal}$.
2. **Centrifugal:** the aircraft holds a constant heading and altitude, so
   $V^{2}/R$ is not applicable within the line; the *heading-change* contribution
   during the turns between lines is discarded with the turn data.
3. **Platform acceleration:** $0.02\ \mathrm{m\,s^{-2}}$ rms = $2000\ \mathrm{mGal}$
   rms, removed using the measured accelerometer signal and GNSS at a
   $0.005\ \mathrm{Hz}$ hand-off; the GNSS part contributes
   $4.935\ \mathrm{mGal}$ (Section 4) and the accelerometer part contributes its own
   bias, which must be calibrated.
4. **Latitude/free air:** the line spans $220\times70 = 15.4\ \mathrm{km}$ of ground
   distance, so the latitude correction changes by up to
   $15.4\times0.813 = 12.5\ \mathrm{mGal}$ along the line, and the aircraft's altitude
   variations ($\pm50\ \mathrm{m}$) produce $\pm0.308555\times50 = \pm15.4\
   \mathrm{mGal}$ of free-air term.
5. **Total platform-related correction:** about $510\ \mathrm{mGal}$ of Eötvös plus
   tens of milligal of free-air and latitude variation, against a target anomaly of a
   few milligal. Every term is computed from the navigation solution, and each is
   known only as well as that solution.

## 9. Assumptions and regime of validity

1. **Rigid-body rotation at constant $\Omega$.** True to $10^{-8}$ for survey
   purposes; polar motion and length-of-day changes are irrelevant here.
2. **The vertical is defined.** "Vertical acceleration" requires a defined vertical,
   normally the ellipsoidal normal at the platform, not the local gravity vector;
   mixing them injects deflections of the vertical (up to $0.01^\circ$, which at
   $70\ \mathrm{m\,s^{-1}}$ is tens of milligal).
3. **The platform attitude is known.** A vertical accelerometer aligned with the
   wrong axis measures a component of horizontal acceleration; attitude accuracy is
   as important as position accuracy.
4. **Straight and level within a line.** Turns and large attitude changes invalidate
   the simple Eötvös/centrifugal split and are discarded or modelled.
5. **The hand-off frequency is chosen and stated.** It determines which sensor
   supplies which band, and therefore which sensor's errors dominate where.
6. **The cross-over model is a constant bias per line.** A time-dependent drift
   violates it and is detected as an excess post-adjustment residual.
7. **The reduction uses the same conventions as a ground survey.** The moving-platform
   corrections precede the free-air, Bouguer and terrain steps of lesson
   [04](04-corrections-workflow.md), which then apply unchanged.
8. **The absolute level still requires a tie.** Nothing in a moving-platform survey
   fixes the datum; cross-overs and overlaps constrain internal consistency only.

## 10. Python demonstration

`code/airborne_marine_gravity_demo.py` prints, with units:

1. the Eötvös derivation and the knots-coefficient check ($7.5028\ \mathrm{mGal}$ per
   knot);
2. the correction for aircraft and ship speeds at five headings, and the
   heading-sensitivity table;
3. the centrifugal term for turns, up to $245\,000\ \mathrm{mGal}$;
4. the GNSS differentiation noise table and its $(2\pi f)^{2}$ dependence;
5. the spectral leakage through a 4-pole filter, and why measuring beats filtering;
6. the cross-over adjustment, before and after, with its gauge-fixing caveat;
7. the moving-platform error budget, with the filtering row identified as a design
   choice.

Exercises and solutions:
[`exercises/05-airborne-marine-gravity-exercises.md`](exercises/05-airborne-marine-gravity-exercises.md),
[`exercises/05-airborne-marine-gravity-solutions.md`](exercises/05-airborne-marine-gravity-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC marine survey is sailed at $10\ \mathrm{m\,s^{-1}}$ on east-west and
> north-south lines at $45^\circ$ latitude, with 5 cm vertical GNSS accuracy and a
> $0.005\ \mathrm{Hz}$ hand-off. **(a)** Compute the Eötvös correction on the
> eastbound and westbound lines. **(b)** Compute the GNSS contribution to the
> platform-acceleration error. **(c)** State what a $0.2\ \mathrm{m\,s^{-1}}$ speed
> error contributes and how it differs between the two line directions. **(d)**
> Compute how many cross-overs 5 × 5 lines produce and state what their adjustment
> can and cannot determine. **(e)** Rank the four largest budget terms.

A worked version of (a)–(d) is in the
[solutions](exercises/05-airborne-marine-gravity-solutions.md).

## Common pitfalls

1. **Quoting the Eötvös coefficient without deriving it.** It contains $\omega$ and
   the knot definition, and it changes with speed units.
2. **Setting a single navigation requirement for all lines.** Section 2.3 measures
   the sensitivity as largest where the correction is smallest.
3. **Trying to filter out platform acceleration.** Measured leakage:
   $54.376\ \mathrm{mGal}$ against a $10\ \mathrm{mGal}$ signal.
4. **Ignoring the $(2\pi f)^{2}$ amplification.** A position accuracy that looks
   adequate for navigation can be useless for gravity.
5. **Using turns as data without a model.** $V^{2}/R$ reaches
   $10^{5}\ \mathrm{mGal}$.
6. **Believing cross-overs fix the datum.** They determine relative line biases only.
7. **Forgetting that a moving-platform survey still needs the terrain and density
   model** of lessons 07-01-04 and 07-02-04.
8. **Reporting an accuracy without the navigation terms.** On a moving platform the
   navigation *is* the gravimeter's calibration.

## Related modules

- [Module 02 — Gravity Instruments and Surveys](README.md) — this module; lessons
  [01](01-absolute-gravimeters.md)–[04](04-corrections-workflow.md) supply the
  sensors, the survey procedures, the reductions and the platform corrections used
  here.
- [07-01-04 Gravity Reductions: Free-Air, Bouguer, Isostatic and Terrain](../01-gravity-fundamentals/04-gravity-reduction.md) —
  the reductions applied after the platform corrections.
- [02-02 Classical Mechanics](../../02-physics/02-classical-mechanics/README.md) —
  rotating frames and the Coriolis term.
- [20 Signal Processing and Time Series](../../20-signal-processing/README.md) —
  filtering, spectral hand-off and the noise amplification of differentiation.
- [Module 15 — Oceanography and Marine Geophysics](../../15-oceanography-marine/README.md),
  [Module 17 — Remote Sensing, GIS and Satellite Geophysics](../../17-remote-sensing-gis/README.md) —
  where marine and airborne gravity data are used alongside altimetry.
- [Module 05 — Satellite Gravimetry](../05-satellite-gravimetry/README.md) —
  the global coverage that airborne and marine surveys complement.
