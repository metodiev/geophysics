---
id: 08-02-05
title: "Airborne Magnetic Surveys and Compensation"
level: graduate
prereqs: ["08-02-01", "08-02-03", "08-02-04"]
tags: [geomagnetism, instruments, airborne-survey, compensation, tolles-lawson, aliasing]
---

# Airborne Magnetic Surveys and Compensation

An airborne magnetometer is the only way to cover a province in a season, and it
turns the instrument problem into an aircraft problem: the platform is itself a
magnetised body moving through a varying field, and its signature is far larger
than the geology. This lesson develops the standard interference model, shows how
its coefficients are solved for and what a stale solution costs, and then treats
the two geometric penalties of flying — height loss and line-spacing aliasing —
as calculated quantities rather than rules of thumb.

**All models and data in this module are SYNTHETIC.** The aircraft coefficients,
attitude manoeuvre, noise, target moment and flight parameters are chosen teaching
values. No aircraft, survey or published specification is described.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the three interference terms — permanent, induced and eddy — from
   the airframe's magnetisation and from Faraday's law.
2. **Write** the 18-coefficient Tolles–Lawson model and explain why it is linear
   in the coefficients.
3. **Compensate** a synthetic manoeuvre by least squares and **choose** the model
   order from a stated noise floor.
4. **Quantify** the residual left by a stale compensation solution.
5. **Compute** the loss of anomaly amplitude with flying height for a dipole
   target.
6. **Compute** the worst-case loss of amplitude with line spacing and state the
   quarter-wavelength design rule and the trap at spacing equal to wavelength.

## Prerequisites

- [08-02-01 Fluxgate Magnetometers: Principle and Use](01-fluxgate-magnetometers.md) —
  the vector sensors used for attitude-correlated terms.
- [08-02-03 Optically Pumped Cesium and Potassium Magnetometers](03-cesium-optically-pumped.md) —
  the scalar sensor the compensation protects.
- [08-02-04 Gradiometers, Arrays and Noise Rejection](04-gradiometers-arrays.md) —
  the rejection logic that compensation generalises.

## 1. Why fly, and what it costs

| property | airborne | ground |
|---|---|---|
| coverage rate | hundreds of line-km per day | a few km per day |
| cost per line-km | low | high |
| sensor-to-source distance | tens to hundreds of metres | metres |
| noise environment | platform, manoeuvre, turbulence | cultural, near-surface |
| anomaly amplitude at the sensor | reduced by height | full |

The whole engineering content of the lesson follows from the third and fifth rows:
flying raises the sensor away from the target (a computed loss, section 5),
and it places the sensor inside a magnetised, moving body (section 2).

## 2. The aircraft as a magnetic source

Write $\mathbf{u}$ for the unit vector of the ambient field **expressed in the
aircraft frame**. As the aircraft manoeuvres, $\mathbf{u}$ sweeps over the unit
sphere while the ambient field's magnitude is almost constant, so the
interference is naturally parameterised by $\mathbf{u}$ and its time derivative:

$$I(t) = \underbrace{\sum_k a_k u_k}_{\text{permanent}}
+ \underbrace{\sum_{i \le j} b_{ij} u_i u_j}_{\text{induced}}
+ \underbrace{\sum_{i,j} c_{ij} u_i \frac{\mathrm{d}u_j}{\mathrm{d}t}}_{\text{eddy}}.$$

The three terms have distinct physical origins, and each is worth deriving:

- **Permanent.** The airframe carries a remanent magnetisation (from its
  construction history and the fields it has flown through). That magnetisation
  is fixed in the aircraft frame, so its projection onto the sensor axis is a
  fixed vector $\mathbf{a}$ dotted with $\mathbf{u}$ — three coefficients.
- **Induced.** The airframe acquires $\mathbf{M} = \kappa\mathbf{H}$ in the
  ambient field. Its contribution to the sensor is quadratic in the field
  direction, because both the induced moment and the projection scale with
  $\mathbf{u}$: hence the six independent products $u_iu_j$.
- **Eddy.** Currents induced in conducting structure are proportional to the rate
  of change of flux, i.e. to $\dot{\mathbf{u}}$; the field they produce is
  projected onto the sensor, giving the nine products
  $u_i\dot u_j$.

**All three scale with the ambient field**, which is why the model is built from
$\mathbf{u}$ (a unit vector) and not from the angles directly: a coefficient is
then an aircraft property, not a property of the flying latitude.

The demonstration's synthetic manoeuvre (roll $\pm25^{\circ}$, pitch
$\pm12^{\circ}$, yaw $\pm18^{\circ}$ over 120 s, sampled at 10 Hz) produces

$$|\mathbf{u}(t)| = 1.000000 \ \text{(to machine precision)}, \qquad
\max\left|\frac{\mathrm{d}u}{\mathrm{d}t}\right| = 0.1371\ \mathrm{s^{-1}},$$

and, with chosen coefficients, an interference of

$$\text{rms} = 3.599\ \mathrm{nT}, \qquad \text{peak} = 32.187\ \mathrm{nT}.$$

That is the same order as the crustal anomalies a survey maps (a few to tens of
nanotesla) and orders of magnitude above the sub-nanotesla resolution of the
sensor. Without compensation, **the aircraft's own field is the largest anomaly
in the map**.

## 3. Solving for the coefficients

Because $I$ is linear in the 18 coefficients, compensation is a linear
least-squares problem: form the design matrix $A$ whose columns are the three
$u_k$, the six $u_iu_j$ and the nine $u_i\dot u_j$, and solve

$$\hat{\mathbf{c}} = \arg\min_{\mathbf{c}}\left\|A\mathbf{c} - \mathbf{m}\right\|^{2},$$

where $\mathbf{m}$ are the measured total-field values during a **manoeuvre**.
The manoeuvre is the experiment: without attitude changes, $\mathbf{u}$ barely
moves, the columns of $A$ are nearly collinear, and the fit is ill-conditioned.
That is why a survey flies a calibration manoeuvre rather than relying on a
magnetically smooth flight.

The demonstration adds $0.30\ \mathrm{nT}$ rms of sensor noise to a constant
$25\ \mathrm{nT}$ anomaly and fits models of increasing order:

| model order | coefficients | rms residual (nT) | reduction factor |
|---|---|---|---|
| permanent only | 3 | 1.3026 | 2.8 |
| permanent + induced | 9 | 0.2930 | 12.3 |
| permanent + eddy + induced (full) | 18 | 0.2905 | 12.4 |

Read the table as a specification, not as a score:

- **The permanent-only model is inadequate.** Its residual, $1.30\ \mathrm{nT}$,
  is more than four times the $0.30\ \mathrm{nT}$ noise floor.
- **The 9- and 18-term models are indistinguishable.** $0.2930$ against
  $0.2905\ \mathrm{nT}$, with a noise floor of $0.30\ \mathrm{nT}$: the eddy terms
  are *not justified by these data*. A larger model that does not push the
  residual below the noise is fitting nothing, and its extra coefficients will
  amplify the noise when applied elsewhere.
- **The model order is an inference about the aircraft, made from a residual
  comparison.** With a noisier sensor the eddy terms would be even less
  identifiable; with a faster manoeuvre or a longer eddy time constant they would
  matter.

## 4. A stale solution, and why compensation is per flight

The coefficients depend on the aircraft's magnetisation state, its fuel and stores
load, and on the field it flies in, so a solution from one flight is not valid for
the next. The demonstration quantifies the cost of pretending otherwise: change
the permanent coefficients by 20% and apply the *previous* solution:

$$\text{rms uncompensated interference after the change} = 0.522\ \mathrm{nT}.$$

Note the structure of that number. It is not random: it is correlated with
attitude, so it appears as a smooth, repeatable deflection along each flight line
— exactly the shape of a geological anomaly, and exactly the shape that levelling
cannot remove because it is different on each line. The remedy is procedural:

- fly a calibration manoeuvre at the start and end of each flight (or of each
  survey block);
- compute a **figure of merit** (the residual rms after fitting on the manoeuvre
  and predicting on a held-out interval);
- reject the flight if the figure of merit exceeds a stated multiple of the noise
  floor.

## 5. Height: the loss is computed, not estimated

For a dipole on the axis, $|B| = (\mu_0/4\pi)(2m/z^{3})$: the anomaly falls as the
inverse cube of the total distance from the source. With a SYNTHETIC body of
$m = 3000\ \mathrm{A\,m^{2}}$ at $20\ \mathrm{m}$ depth:

| altitude (m) | $|B|$ (nT) | fraction of the ground value |
|---|---|---|
| 0 | 75.000 | 1.0000 |
| 30 | 4.800 | 0.0640 |
| 60 | 1.172 | 0.0156 |
| 100 | 0.347 | 0.0046 |
| 200 | 0.056 | 0.0008 |

Thirty metres of altitude removes **93.6%** of the amplitude; 100 m removes
99.5%. Two design consequences:

- **Fly low.** Height is the single largest determinant of what a survey can see,
  and a drape (following terrain at a fixed clearance) is worth its cost.
- **Height is a quantitative caveat on every anomaly.** An anomaly measured at
  altitude cannot be inverted for a depth without assuming the height, and a
  varying altitude along a line imposes an apparent gradient that must be removed
  — the "terrain effect" of aeromagnetic processing.

## 6. Line spacing, aliasing, and the quarter-wavelength rule

Along a survey line the anomaly is sampled at the line's own sample interval;
between lines it is sampled at the line spacing $s$. For a sinusoid of wavelength
$\lambda$, consider the worst case over the anomaly's phase: the demonstration
computes, for each spacing, the smallest over phases of the largest sampled
amplitude, and then tries to recover the wavelength from the samples restricted to
those the spacing can resolve (two samples per wavelength or better):

| spacing (m) | $s/\lambda$ | worst retention | recovered wavelength |
|---|---|---|---|
| 50 | 0.125 | 0.9239 | 400 m (correlation 1.0000) |
| 100 | 0.250 | 0.7071 | 400 m (correlation 1.0000) |
| 200 | 0.500 | 0.0000 | 400 m (correlation 1.0000) |
| 400 | 1.000 | 0.0000 | none — the samples are constant |
| 800 | 2.000 | 0.0000 | none — the samples are constant |

Read the table in two ways.

**Amplitude.** At a quarter of the wavelength ($s = \lambda/4$, spacing 100 m
here) the sample nearest the peak is within 29.3% of it in the worst case; at
$s = \lambda/8$ within 7.6%. The standard design rule is therefore to space lines
at about **one quarter of the shortest target wavelength**.

**Wavelength.** Notice the trap at $s = \lambda$: the samples are *all equal*, so
the retained amplitude is full and the anomaly has **vanished** from the data
while leaving no sign of its absence. Amplitude retention is not a test of
sampling; only the wavelength question is. At $s > \lambda/2$ the anomaly folds to
a longer apparent wavelength, and the map shows a feature that is not there.

For a $400\ \mathrm{m}$-wavelength target the rule gives a line spacing of 100 m
— and the example shows why a survey that used 200 m ("Nyquist") has already lost
the ability to place the anomaly, even before amplitudes are considered.

## 7. Putting the design together

| parameter | set by | statement |
|---|---|---|
| sensor | target amplitude and platform | scalar sensor + dead-zone-safe mounting |
| flying height / drape | target amplitude and terrain | the loss table of §5 |
| line spacing | shortest target wavelength | $s \le \lambda_{\min}/4$ |
| along-line sampling | same rule, applied along track | typically $s/4$ or the sensor's rate |
| speed | sampling rate and required along-line spacing | $v = \Delta x/\Delta t$ |
| manoeuvre | compensation identifiability | frequent, with attitude coverage |
| base station | diurnal variation | see [08-02-06](06-magnetic-survey-procedures.md) |

Every row is a number with a unit, and each is derived from a target
specification rather than from convention.

## 8. Assumptions and regime of validity

1. **The interference is linear in the 18 terms.** Field-dependent coefficients,
   saturation of the airframe's magnetisation, and the sensor's own heading error
   all break the model.
2. **The geology is constant during the manoeuvre.** A manoeuvre flown over an
   anomaly absorbs part of that anomaly into the coefficients; compensating
   manoeuvres belong over magnetically quiet ground.
3. **The manoeuvre excites all the terms.** A manoeuvre with no yaw variation
   leaves some columns of $A$ nearly collinear and the corresponding coefficients
   undetermined.
4. **The residual is compared with a known noise floor.** Without a stated floor,
   "the residual is small" is not a model-selection argument.
5. **A constant altitude along the line.** A varying drape imposes its own
   apparent gradient, which is removed by a height-correction step, not by
   compensation.
6. **Synthetic parameters.** The coefficients, manoeuvre, moments and sizes are
   teaching values.

## 9. Python demonstration

`code/airborne_magnetic_surveys_demo.py` prints, with units:

1. the Tolles–Lawson model structure and the physical origin of each term;
2. a simulated manoeuvre with $|\mathbf{u}|$ and $|\dot{\mathbf{u}}|$, and the
   resulting interference rms and peak;
3. compensation residuals for 3, 9 and 18 coefficients against a stated noise
   floor;
4. the anomaly against altitude for a synthetic dipole;
5. worst-case retention and wavelength recovery versus line spacing;
6. the residual left by a stale 20%-changed compensation solution.

Exercises and solutions:
[`exercises/05-airborne-magnetic-surveys-exercises.md`](./exercises/05-airborne-magnetic-surveys-exercises.md),
[`exercises/05-airborne-magnetic-surveys-solutions.md`](./exercises/05-airborne-magnetic-surveys-solutions.md).

## Mastery checkpoint

1. Write the three interference terms and state the number of coefficients each
   contributes.
2. Explain why a magnetically smooth flight cannot be used to solve for the
   coefficients.
3. From the table of §3, state which model order you would report and why.
4. Compute the fraction of a dipole's anomaly retained at 60 m for a body at
   30 m depth.
5. A survey must resolve an anomaly of $300\ \mathrm{m}$ wavelength. State the
   maximum line spacing and the resulting along-line sampling under the
   quarter-wavelength rule.
6. Explain in two sentences why a stale compensation solution produces features
   that look like geology.

## Common pitfalls

1. **Compensating over an anomaly.** The manoeuvre must be over quiet ground.
2. **Keeping 18 coefficients because they fit.** Compare the residual with the
   noise floor.
3. **Quoting an anomaly without its flying height.**
4. **Using Nyquist spacing as a design rule.** It is the failure threshold, not a
   target.
5. **Assuming a level flight line.** A varying drape imposes an apparent
   gradient.
6. **Compensating once per survey.** The coefficients belong to a flight, not to
   a project.

## Related modules

- [08-02-04 Gradiometers, Arrays and Noise Rejection](04-gradiometers-arrays.md) —
  rejection of common signals by differencing.
- [08-02-06 Magnetic Survey Design, Diurnal Correction and Levelling](06-magnetic-survey-procedures.md) —
  the rest of the processing chain.
- [08-02-03 Optically Pumped Cesium and Potassium Magnetometers](03-cesium-optically-pumped.md) —
  the sensor, and the dead zone a manoeuvre must avoid.
- [05-05-03 Spatial Sampling, Wavenumber Aliasing and Reconstruction](../../05-core-geophysics/05-survey-design-and-acquisition/03-spatial-sampling-theory.md) —
  the general sampling theory behind §6.

## Self-assessment checklist

- [ ] I can derive the three interference terms.
- [ ] I can set up and justify the compensation fit.
- [ ] I can choose a model order from a residual and a noise floor.
- [ ] I can compute the height loss for a dipole target.
- [ ] I can apply the quarter-wavelength rule and explain the trap at $s = \lambda$.
- [ ] I can list the survey-design parameters and what each is derived from.
