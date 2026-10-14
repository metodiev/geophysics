---
id: 07-02-02
title: "Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex"
level: advanced
prereqs: ["07-02-01", "02-03-02", "07-01-05"]
tags: [gravity, instruments, relative-gravimeter, spring, astatisation, force-balance, drift]
---

# Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex

**All models and data in this module are SYNTHETIC.** The masses, stiffnesses,
geometry, temperature coefficients, readout noise and non-linearity are chosen
teaching values. No manufacturer's instrument, model number or specification is
used, quoted or implied. The design families associated in practice with the names
in this lesson's title are described generically: a **zero-length-spring astatic
lever** and a **nulled force-balance sensor**. The only exact constants used are the
module's SYNTHETIC station value $g = 9.820250\ \mathrm{m\,s^{-2}}$ (as a scale) and
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the sensitivity of a spring balance to gravity,
   $\mathrm{d}x/\mathrm{d}g = 1/\omega_{0}^{2}$, and **compute** the displacement
   resolution a microgal demands at a given natural frequency.
2. **Explain** the dynamical period and the zero-length-spring geometry by which
   astatisation reduces the effective stiffness, and **compute** the amplification
   factor $A = 1/(1-\eta)$.
3. **Show**, from measured numbers, that astatisation amplifies the response to
   gravity and to the instrument's own geometry by the *same* factor, so it buys
   readout resolution and not stability.
4. **Compute** the temperature stability and geometric stability required for a
   stated accuracy, and **state** why this is a first-order design constraint.
5. **Describe** a nulled force-balance sensor, and **compute** the dynamic range and
   bit depth needed to cover the Earth's gravity range at microgal resolution.
6. **Quantify** the residual left by a sensor non-linearity after a linear
   calibration, and **explain** why the calibration span must be reported.
7. **Distinguish** drift from noise, **measure** a drift rate from a record, and
   **explain** why a linear drift model fitted over a settling record is biased.

## Prerequisites

- [07-02-01 Absolute Gravimeters: Free-Fall and Interferometry](01-absolute-gravimeters.md)
  — the absolute values that give a relative survey its datum, and the distinction
  between statistical and systematic error developed there.
- [02-03-02 Damped and Driven Oscillators](../../02-physics/03-oscillations-and-waves/02-damped-driven.md)
  — natural frequency, damping and the response of a mass–spring system.
- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md)
  — the calibration and uncertainty framework this lesson supplies hardware for.

## 1. What a relative instrument must do

A relative gravimeter is asked for one thing: the **difference** in gravity between
two points, as precisely and as cheaply as possible, with a level that comes from an
absolute datum. Its design is therefore an exercise in squeezing a displacement out
of a force and then reading the displacement without introducing anything that
mimics gravity.

Two families dominate.

| family | what is measured | how sensitivity is obtained |
|---|---|---|
| spring balance (astatic lever, zero-length spring) | displacement of a proof mass | a very small effective stiffness, so gravity produces a large motion |
| nulled force balance (electrostatic or optical, fused-quartz or metal spring) | the force needed to hold a proof mass at a fixed position | a stiff suspension and a precise force measurement, so the mass does not move |

The two designs choose opposite sides of the same trade. A soft spring produces a
large signal but is sensitive to its own geometry; a stiff nulled sensor does not
move, so its geometry is stable, but it must measure a force precisely. Everything
in this lesson follows from that choice.

## 2. The plain spring: sensitivity and the readout it needs

A mass $m$ hangs on a spring of stiffness $k$ in local gravity $g$. Equilibrium gives

$$mg = kx \qquad\Longrightarrow\qquad
x = \frac{mg}{k} = \frac{g}{\omega_{0}^{2}},
\qquad \omega_{0}^{2} = \frac{k}{m},$$

and differentiating at fixed spring constant,

$$\boxed{\;\frac{\mathrm{d}x}{\mathrm{d}g} = \frac{m}{k} = \frac{1}{\omega_{0}^{2}}\;}$$

**Numerical values (SYNTHETIC $m = 0.05\ \mathrm{kg}$):**

| $f_{0} = \omega_{0}/2\pi$ (Hz) | $k$ (N/m) | static extension (mm) | $\mathrm{d}x$ for $1\ \mathrm{\mu Gal}$ (nm) |
|---|---|---|---|
| 10.0 | 197.3921 | 2.487 | 0.003 |
| 1.0 | 1.9739 | 248.750 | 0.253 |
| 0.2 | 0.0790 | 6218.746 | 6.333 |

Two facts stand out. First, a *stiffer* spring is *less* sensitive: the 10 Hz spring
moves 3 picometres for a microgal. Second, softening the spring to 0.2 Hz raises the
static extension to $6.2\ \mathrm{m}$ — not a practical instrument. So a direct
spring cannot be both sensitive and compact, and the readout requirement of the
$1\ \mathrm{Hz}$ column ($0.253\ \mathrm{nm}$) is already at the limit of optical
interferometry.

This is the design pressure that produced astatisation.

## 3. Astatisation: the zero-length spring and the astatic lever

### 3.1 The idea

If a spring's force is proportional to its **full length** rather than to its
extension,

$$F = k\,l \qquad\text{(a "zero-length" spring)},$$

then its contribution to the torque about a beam pivot can be arranged to be nearly
independent of the beam angle: the lever arm grows as the spring length shrinks, and
the two effects cancel. The restoring torque is then the *difference* of two large
torques, and it can be made very small. Writing the residual stiffness as

$$k_{\text{eff}} = k\left(1-\eta\right), \qquad
\eta = \frac{l_{0}}{l},$$

the response to gravity is amplified by

$$A = \frac{1}{1-\eta} = \frac{k}{k_{\text{eff}}}.$$

This is the classical **astatic** or *long-period* design, and the geometry that
realises it most simply — a spring whose unstretched length is zero, attached so
that the torque balance is independent of angle — is the design principle associated
with the LaCoste-Romberg family of instruments. The alternative family, associated
with Scintrex, uses a small fused-quartz or metal suspension with electrostatic or
photoelectric nulling rather than a long-period lever: it accepts a stiffer
suspension and pays for it with a more demanding force readout.

### 3.2 Measured consequences

Starting from the 1 Hz reference spring ($k/m = 39.478\ \mathrm{s^{-2}}$):

| $\eta$ | $A$ | period $T$ (s) | static extension (m) | $\mathrm{d}x$ for $1\ \mathrm{\mu Gal}$ (nm) |
|---|---|---|---|---|
| 0.000 | 1.0 | 1.00 | 0.249 | 0.25 |
| 0.900 | 10.0 | 3.16 | 2.487 | 2.53 |
| 0.990 | 100.0 | 10.00 | 24.875 | 25.33 |
| 0.999 | 1000.0 | 31.62 | 248.750 | 253.30 |

With $\eta = 0.99$ one microgal is $25.3\ \mathrm{nm}$ of motion instead of
$0.253\ \mathrm{nm}$ — the readout requirement is relaxed by *exactly* the
amplification factor $A = 100$, and the natural period lengthens to
$10\ \mathrm{s}$. Those long periods are the signature of the design, and they are
also why a relative gravimeter takes seconds to settle after being moved.

## 4. What astatisation costs

The amplification is not free. A change in the anchor geometry changes the
equilibrium position, and converting that to an equivalent gravity change brings the
small denominator $l - l_{0}$ into the answer:

$$\delta g_{\text{equiv}} = g\,\frac{\delta l_{0}}{l-l_{0}}
= g\,A\,\frac{\delta l_{0}}{l}.$$

**Measured (SYNTHETIC, $\eta = 0.99$, $l = 0.250\ \mathrm{m}$, so
$l - l_{0} = 2.500\times10^{-3}\ \mathrm{m}$):**

| $\delta l_{0}$ (m) | equivalent gravity change (µGal) |
|---|---|
| $10^{-12}$ (1 pm) | 0.393 |
| $10^{-11}$ | 3.928 |
| $10^{-9}$ (1 nm) | 392.810 |
| $10^{-6}$ (1 µm) | 392 810 |

Read the table against the previous section. Astatisation multiplies the response to
gravity by $A = 100$ **and** the response to a geometry error by the same $A$: the
ratio of signal to geometric error is unchanged. What astatisation buys is readout
resolution; what it does not buy is stability. A one-micrometre geometric change — a
thermal expansion any bench experiment would call negligible — is
$392\,810\ \mathrm{\mu Gal}$.

**Temperature.** With a SYNTHETIC effective geometry coefficient of
$10^{-8}\ \mathrm{m\,K^{-1}}$ the sensitivity is

$$\frac{\mathrm{d}g}{\mathrm{d}T} = 3928.1\ \mathrm{\mu Gal\,K^{-1}},$$

so a $1\ \mathrm{mK}$ change gives $3.93\ \mathrm{\mu Gal}$, and holding a
$0.4\ \mathrm{\mu Gal}$ budget requires about $10^{-4}\ \mathrm{K}$ of thermal
stability. That is why such instruments are thermostatted, why they are
transported in insulated cases, and why — crucially — a survey **measures** drift
rather than assuming the sensor is stable. Lesson [03](03-survey-procedures.md)
turns that measurement into the loop and tie procedures.

## 5. Nulled force-balance sensors

A nulled sensor holds the proof mass at a fixed position and measures the force
required. Nothing moves, so the geometric sensitivity that dominated Section 4 is
absent; the price is that a force must be measured precisely, and the reading is a
current, a voltage or a count.

**Measured design arithmetic (SYNTHETIC: 10 counts per µGal, $0.5\
\mathrm{\mu Gal}$ readout noise per sample, $7000\ \mathrm{mGal}$ range):**

| quantity | value |
|---|---|
| range in counts | $7.000\times10^{7}$ |
| bits needed for the full range | $26.06$ |
| bits needed to resolve $0.5\ \mathrm{\mu Gal}$ | $23.74$ |
| dynamic range (range / 1 µGal) | $7.000\times10^{6}$ |
| averaged noise over 4 samples | $0.250\ \mathrm{\mu Gal}$ |
| drift over 1 h at $20\ \mathrm{\mu Gal\,h^{-1}}$ | $20.0\ \mathrm{\mu Gal}$ ($= 200$ counts) |

Two conclusions:

1. **The digitisation is comfortable; the stability is not.** A 24-bit readout covers
   the whole range at microgal resolution, but a drift of $20\ \mathrm{\mu Gal\,h^{-1}}$
   is 200 counts in an hour — forty times the single-sample noise. Averaging four
   samples reduces the noise to $0.25\ \mathrm{\mu Gal}$ and does nothing to the
   drift.
2. **The instrument is drift-limited.** Over a ten-hour day the same drift is
   $200\ \mathrm{\mu Gal}$, which is why a survey re-occupies a base about hourly.
   The number $20\ \mathrm{\mu Gal\,h^{-1}}$ is SYNTHETIC, but the *structure* of the
   conclusion is general: compare the drift rate with the noise per sample and with
   the survey duration, and the larger product sets the design of the field
   procedure.

## 6. Calibration, sensitivity and non-linearity

The meter equation of lesson [07-01-05](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md)
applies unchanged: $g = g_{\text{base}} + c\left(R - R_{\text{base}}\right)$, with
$c$ in mGal per count. Two properties of the sensor determine how well $c$ can be
determined.

**Sensitivity.** A larger $\mathrm{d}R/\mathrm{d}g$ makes each count worth less
gravity, so the quantisation error in gravity is smaller. In the SYNTHETIC design
above, one count is $0.1\ \mathrm{\mu Gal}$ — a fine quantum — but the *scale*
accuracy of $c$ is what limits a survey, exactly as measured in lesson 07-01-05.

**Non-linearity.** Suppose the response is

$$R(g) = c_{1}g + c_{2}g^{2}.$$

Fitting a straight line over a symmetric span $\left[-L, L\right]$ leaves the
residual

$$R - \text{(line)} = c_{2}\left(g^{2} - \frac{L^{2}}{3}\right),
\qquad
\max\left|\text{residual}\right| = \tfrac{2}{3}c_{2}L^{2}\ \text{at } g = \pm L.$$

**Measured (SYNTHETIC, $c_{1} = 10^{-3}$ counts/µGal, calibration span
$L = 50\,000\ \mathrm{\mu Gal} = 100\ \mathrm{mGal}$):**

| $c_{2}$ (counts/µGal²) | non-linearity at the span end | residual after linear calibration (µGal) |
|---|---|---|
| $10^{-12}$ | $5.00\times10^{-5}$ | 1.658 |
| $10^{-11}$ | $5.00\times10^{-4}$ | 16.583 |
| $10^{-10}$ | $5.00\times10^{-3}$ | 165.833 |

A non-linearity of $5\times10^{-5}$ of the reading at the end of the span leaves
$1.7\ \mathrm{\mu Gal}$ — comparable with a microgal-level target. The residual is a
*parabola in the range*, so it correlates with where in the range the reading sits:
calibrating over a narrow span hides it, and the same instrument used over a wider
span reveals it. **Report the calibration span and the residual, not only the scale
factor.** A known-mass or electrostatic calibration is usually preferred for the
scale because it does not depend on another gravimeter's own errors.

## 7. Drift is a measurement, not a defect

**Measured (SYNTHETIC, six-hour record: a linear rate of
$18.0\ \mathrm{\mu Gal\,h^{-1}}$, an exponential settling term of
$-35\ \mathrm{\mu Gal}$ with a $0.8\ \mathrm{h}$ time constant, and
$0.8\ \mathrm{\mu Gal}$ of noise):**

| fit interval | fitted rate (µGal/h) | residual rms (µGal) |
|---|---|---|
| whole record (0–6 h) | 21.82 | 6.94 |
| last four hours (2–6 h) | 18.23 | — |

The full-record fit is biased by $3.8\ \mathrm{\mu Gal\,h^{-1}}$ ($21\%$) because the
exponential settling is absorbed into the slope, and it leaves residuals of nearly
$18\ \mathrm{\mu Gal}$ at the start. A survey that fits a line to a settling
instrument therefore mis-corrects its first stations by more than its target
uncertainty — a systematic error that looks like geology in a map.

Three practices follow, and all three are quantitative rather than conventional:

1. **Let the instrument settle** before the first reading, or start the drift model
   after the settling interval.
2. **Re-occupy the base** often enough that the drift model is extrapolated over a
   short interval (Section 5's arithmetic: an hour at
   $20\ \mathrm{\mu Gal\,h^{-1}}$ is $20\ \mathrm{\mu Gal}$).
3. **Report the drift model's residuals.** They are the only evidence that the model
   is adequate; a fit whose residuals exceed the target uncertainty has not solved
   the problem it was introduced for.

## 8. Assumptions and regime of validity

1. **Linear response over the working range.** Measured in Section 6, and the
   residual is the test.
2. **Thermal stability** at the level Section 4 computes, or a temperature model.
3. **No transport hysteresis.** A soft-spring sensor moved between stations must
   re-settle; the period after a move is the diagnostic, and a changed reading at a
   repeat station is the test.
4. **Level and tilt.** The sensor measures one component; a tilt mixes horizontal
   accelerations into the reading, and the level must be set to the accuracy implied
   by the target.
5. **Seismic and cultural noise.** Microseisms and vibrations degrade the reading and
   are reduced by averaging, which requires the sensor to be in a quiet regime.
6. **Magnetic and electrostatic environment.** A nulled sensor's feedback force may
   depend on the local field and on the electronics' reference voltage, which is
   another reason the *scale* is calibrated against an external standard.
7. **The datum is external.** A relative instrument cannot establish its own level;
   every survey value is a difference plus an absolute tie.
8. **Drift is bounded and slow.** A step change (a shock, a large temperature
   excursion) invalidates the drift model for that interval, and the residuals reveal
   it.

## 9. Python demonstration

`code/relative_gravimeters_demo.py` prints, with units:

1. the plain-spring sensitivity and static extension at three natural frequencies,
   with the readout each one demands for a microgal;
2. the astatic amplification table ($A = 1/(1-\eta)$, period, static extension,
   displacement per microgal);
3. the geometric and thermal sensitivities that astatisation *does not* improve,
   including the picometre and $10^{-4}\ \mathrm{K}$ requirements;
4. the nulled-sensor dynamic range, bit depth, averaged noise and drift arithmetic;
5. the non-linearity residual after a linear calibration over a stated span;
6. the six-hour drift record with its linear and settling components, the fitted
   rates and the residuals.

Exercises and solutions:
[`exercises/02-relative-gravimeters-exercises.md`](exercises/02-relative-gravimeters-exercises.md),
[`exercises/02-relative-gravimeters-solutions.md`](exercises/02-relative-gravimeters-solutions.md).

## Mastery checkpoint

Answer without notes.

> A SYNTHETIC relative meter has a proof mass of $0.05\ \mathrm{kg}$, an effective
> stiffness of $k_{\text{eff}} = 0.019739\ \mathrm{N\,m^{-1}}$, a readout noise of
> $10\ \mathrm{nm}$ per sample and a measured drift of
> $25\ \mathrm{\mu Gal\,h^{-1}}$. **(a)** Compute its amplification factor relative
> to a $1\ \mathrm{Hz}$ spring, its natural period and the displacement per
> microgal. **(b)** Compute the gravity noise per sample and the number of samples
> needed to reach $0.2\ \mathrm{\mu Gal}$. **(c)** Compute the drift over a 4-hour
> occupation and state which of the two limits the survey. **(d)** State one design
> change that would reduce the drift-limited error and one that would not.

A worked version is in the
[solutions](exercises/02-relative-gravimeters-solutions.md).

## Common pitfalls

1. **Believing that sensitivity means accuracy.** Section 4 measures the same
   amplification factor on the signal and on the geometry.
2. **Quoting a resolution without the drift rate.** A $0.5\ \mathrm{\mu Gal}$
   readout noise with a $20\ \mathrm{\mu Gal\,h^{-1}}$ drift is a
   drift-limited instrument.
3. **Calibrating over a narrow span.** The non-linearity residual vanishes over a
   narrow range and reappears over a wide one; the span is part of the calibration.
4. **Fitting a line to a settling record.** Measured bias: $21.82$ against
   $18.0\ \mathrm{\mu Gal\,h^{-1}}$.
5. **Forgetting the long settling time.** A long-period (astatic) sensor takes
   seconds to minutes to settle after a move, and readings taken earlier are biased.
6. **Ignoring tilt.** A relative meter measures the component along its sensitive
   axis; the level is part of the measurement, not a formality.
7. **Treating drift as random error.** It is correlated in time, so more readings at
   the same place do not reduce it — only re-occupying the base does.
8. **Assuming the two design families differ only in brand.** They differ in *what is
   traded*: readout resolution against geometric stability. A specification that
   ignores which trade was made cannot be audited.

## Related modules

- [Module 02 — Gravity Instruments and Surveys](README.md) — this module; lesson
  [01](01-absolute-gravimeters.md) supplies the absolute datum, lesson
  [03](03-survey-procedures.md) the loop and drift procedures, and lesson
  [05](05-airborne-marine-gravity.md) the moving-platform case where the sensor's
  dynamics matter most.
- [07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement](../01-gravity-fundamentals/05-gravity-units-and-instruments-relative.md) —
  calibration, uncertainty propagation and the ppb scale.
- [02-03 Oscillations and Waves](../../02-physics/03-oscillations-and-waves/README.md) —
  damped oscillators, the physics of the spring balance.
- [02-04 Elasticity and Continuum Mechanics](../../02-physics/04-elasticity-and-continuum-mechanics/README.md) —
  the elastic and thermal behaviour of real springs and quartz suspensions.
- [Module 23 — Field Methods and Instruments](../../23-field-methods-instruments/README.md) —
  instrument handling, transport and field logistics.
