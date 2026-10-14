---
id: 23-06-02
title: "Ultrasonic Velocity Measurement and Pressure Dependence"
level: research
prereqs: ["23-06-01", "05-04-03"]
estimated_minutes: 115
tags: [laboratory, ultrasonic, velocity, elastic-moduli, effective-pressure, uncertainty]
---

# Ultrasonic Velocity Measurement and Pressure Dependence

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a velocity from a travel time with the transducer delay included, and
   **measure** that delay from two specimen lengths.
2. **Choose** a transducer frequency from the wavelength criterion and the specimen
   length, and **state** what limits it from above.
3. **Convert** a P- and S-wave velocity pair into the elastic moduli, and **state** what
   each one depends on.
4. **Evaluate** a pressure-velocity relation, its local slope, and the effective pressure
   that governs it.
5. **Build** an uncertainty budget for a velocity measurement and **identify** the
   dominant term.
6. **State** which errors are systematic and which are scatter, and how each is reported.

All velocities, lengths, times, densities and pressures here are **SYNTHETIC** teaching
values combined with the standard relations quoted in the text (travel time with a
transducer delay, the isotropic elastic-moduli relations, wavelength, the effective
pressure, first-order error propagation). No instrument specification, calibration
standard or measured rock property is reproduced.

## Prerequisites

- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the geometry that the end effect and the aspect ratio come from.
- [05-04-03 Gassmann Fluid Substitution and Saturation Effects](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md) —
  what the measured velocities are used for.

## 1. Intuition: the measurement is a time, and a time is a difference

An ultrasonic velocity measurement times a pulse through a specimen. The quantity the
experiment actually produces is a **transit time**, and the velocity follows from a
difference — the time *through the rock* rather than the time through the whole
electrical and mechanical path. Everything difficult about the measurement is in that
word "difference":

- the **transducer delay** (the time spent in the buffer, the coupling and the
  electronics) is usually comparable to the travel time in the specimen, so ignoring it
  is a percent-level error, not a correction;
- the **path length** is not the specimen length if the transducers are not in contact,
  if the faces are not parallel, or if there is a coupling layer;
- the delay and the coupling are **systematic**, so they do not average out.

The design answer is the standard one in metrology: measure the difference, not the
absolute. Two lengths from one material give both the delay and the velocity, and the
delay becomes a *measured* number that can be checked and reported.

## 2. Travel time and the transducer delay

The measured time is

$$t = t_0 + \frac{L}{v} ,$$

with $t_0$ the delay. For a synthetic rock with $v = 4500$ m/s and $t_0 = 2.5\ \mu s$:

| $L$ | $t$ | Naive $v = L/t$ | Error |
|---|---|---|---|
| 40.0 mm | 11.3889 µs | 3512.2 m/s | −21.95 % |
| 60.0 mm | 15.8333 µs | 3789.5 m/s | −15.79 % |

so ignoring the delay costs 22 % at 40 mm — and the error *changes with length*, which is
the signature of a delay: a systematic error that scales as $1/L$ looks like a
length-dependent velocity, and it is often misread as dispersion or heterogeneity.

Two lengths solve for both unknowns exactly:

$$v = \frac{L_2 - L_1}{t_2 - t_1}, \qquad
t_0 = \frac{t_1 L_2 - t_2 L_1}{L_2 - L_1} ,$$

giving 4500.00 m/s and 2.500 µs here, to machine precision. Three practical points. The two lengths must be the **same material and the same
transducer setup**, so the pair is cut from one plug and measured without changing
anything in the chain. The delay is a **calibration that drifts** with couplant
thickness, contact pressure and temperature, so the pair is repeated at the end of the
session. And a delay error costs $-\delta t_0/(t-t_0)$ of velocity, i.e. more for short
specimens and fast rocks: the demonstration shows 0.10 µs costing 1.11 %, larger than
the whole timing budget below.

## 3. Frequency and the wavelength criterion

The measurement needs enough wavelengths in the specimen for the travel time of a pulse
to be well defined, the conventional criterion being $L \ge 5\lambda$ with
$\lambda = v/f$. At $v = 4500$ m/s:

| $f$ | $\lambda$ | Minimum $L$ for $L \ge 5\lambda$ |
|---|---|---|
| 0.25 MHz | 18.000 mm | 90.00 mm |
| 0.50 MHz | 9.000 mm | 45.00 mm |
| 1.00 MHz | 4.500 mm | 22.50 mm |
| 2.25 MHz | 2.000 mm | 10.00 mm |
| 5.00 MHz | 0.900 mm | 4.50 mm |

Equivalently, a 40 mm specimen requires $f \ge 5v/L = 0.562$ MHz. The criterion
therefore sets a **minimum** frequency, and it is met more comfortably the higher the
frequency — which is why the real upper bound comes from something else:

1. **Attenuation.** A pulse absorbed before it crosses the specimen produces no travel
   time; attenuation rises with frequency, most steeply in cracked or saturated rock.
2. **Beam spread and mode conversion.** Above the near-field the beam diverges, the path
   length stops equalling the specimen length, and the first arrival may be a converted
   or edge-diffracted wave.
3. **Specimen heterogeneity.** A high frequency averages a smaller volume, so the result
   becomes more variable and less representative — the reason 1 MHz, not 5 MHz, is chosen
   for a heterogeneous plug.

The usable window is therefore between a minimum set by the specimen's length and a
maximum set by the rock's attenuation and homogeneity, and the *frequency dependence of
the result* — dispersion — must be tested by measuring at two frequencies, not assumed.

## 4. From two velocities to the elastic moduli

The P and S velocities give the elastic moduli directly, for an isotropic material with
density $\rho$:

$$M = \rho V_P^{2}, \qquad G = \rho V_S^{2}, \qquad
K = \rho\left(V_P^{2} - \tfrac{4}{3}V_S^{2}\right),$$

$$\nu = \frac{V_P^{2} - 2V_S^{2}}{2\left(V_P^{2} - V_S^{2}\right)}, \qquad
E = 2G(1+\nu) .$$

For $\rho = 2650$ kg/m³, $V_P = 4500$ m/s and $V_S = 2600$ m/s:

| Quantity | Value |
|---|---|
| $M$ | 53.66 GPa |
| $G$ | 17.91 GPa |
| $K$ | 29.78 GPa |
| $\nu$ | 0.2494 |
| $E$ | 44.77 GPa |
| $V_P/V_S$ | 1.7308 |
| $K/\rho$ | 11.237 km²/s² |

Three points that matter more than the arithmetic:

1. **$K$ depends on a difference of squares**, $V_P^2 - \frac43 V_S^2$, so a small error
   in either velocity is amplified in $K$ and in $\nu$: a 1 % error in $V_S$ moves $K$ by
   1.6 % and a 1 % error in $V_P$ by 3.6 %, because $\partial K/\partial V_P = 2\rho V_P$
   while $\partial K/\partial V_S = -\frac{8}{3}\rho V_S$. Poisson's ratio is the most
   sensitive quantity of the set and should carry the largest uncertainty.
2. **The relations assume elastic isotropy.** A fluid-saturated rock is isotropic in its
   elastic response if the pores are equant and randomly oriented, and then they are
   valid; for a cracked or layered rock they are not, and the velocity depends on
   direction as well.
3. **$V_S$ requires a shear transducer.** A dataset with $V_P$ only cannot produce $G$,
   $K$, $E$ or $\nu$, and no relation based on $V_P$ alone substitutes for the measurement.

## 5. Pressure dependence and effective pressure

Velocity rises with pressure because pressure closes the compliant part of the void
space — cracks first, then the stiffer pores. A convenient synthetic model is

$$V_P(P) = V_0 + aP - bP^{2} \quad [\mathrm{km/s},\ \mathrm{MPa}],$$

with $V_0 = 4.50$, $a = 5.0\times10^{-3}$ and $b = 1.2\times10^{-5}$:

| $P$ (MPa) | $V_P$ (m/s) | $\mathrm{d}V_P/\mathrm{d}P$ (m/s/MPa) |
|---|---|---|
| 0 | 4500.0 | 5.00 |
| 10 | 4548.8 | 4.76 |
| 25 | 4617.5 | 4.40 |
| 50 | 4720.0 | 3.80 |
| 100 | 4880.0 | 2.60 |
| 150 | 4980.0 | 1.40 |

Two features generalise to every real rock: the **slope falls with pressure** (the
cracks are closed first, then the response is dominated by the stiff pores and the solid
frame), and the **velocity saturates** rather than reaching the mineral velocity. The same
asymmetry appears on unloading as hysteresis: a rock measured on the way up and on the way
down follows different curves because crack closure is partly irreversible. That is why a
velocity-pressure curve must be reported with its path, and why a single measurement at
one pressure says little.

The pressure that governs the response is not the confining pressure but the **effective
pressure**:

$$P_e = P_c - \alpha P_p ,$$

with $\alpha$ the effective-stress coefficient, taken as 1 in this synthetic example:

| $P_c$ (MPa) | $P_p$ (MPa) | $P_e$ (MPa) | $V_P$ (m/s) | $V_S$ (m/s) |
|---|---|---|---|---|
| 50 | 0 | 50 | 4720.0 | 2732.5 |
| 50 | 10 | 40 | 4680.8 | 2708.8 |
| 100 | 20 | 80 | 4823.2 | 2795.2 |
| 150 | 50 | 100 | 4880.0 | 2830.0 |

So two specimens at the same confining pressure differ by 39 m/s when their pore
pressures differ by 10 MPa — comparable to the whole between-specimen scatter of many
studies, and invisible if the pore pressure is not recorded. Two rules follow: measure
$V_P$ and $V_S$ **as a function of effective pressure** and report the pore-pressure
history, and never compare two datasets whose effective pressures differ without saying
so.

## 6. The uncertainty budget

The velocity is $v = L/(t - t_0)$, so with independent errors

$$\frac{\delta v}{v} = \sqrt{\left(\frac{\delta L}{L}\right)^{2}
+ \left(\frac{\delta t}{t - t_0}\right)^{2} + \left(\frac{\delta t_0}{t - t_0}
\right)^{2}} .$$

For $L = 40.0$ mm ± 0.010 mm and $t - t_0 = 8.8889\ \mu s$:

| Term | Contribution |
|---|---|
| length resolution 0.010 mm | 0.0250 % |
| timing resolution 0.010 µs | 0.1125 % |
| **combined** | **0.1152 % = 5.19 m/s** |

so the **timing term dominates by 4.5×** — which is the usual outcome and the reason a
better micrometer does not improve a velocity measurement. The budget also shows why the
delay belongs in the denominator's budget as a separate term: a 0.10 µs delay error adds
1.112 % of velocity, i.e. ten times the timing resolution's contribution, and it is
*systematic* — it shifts every specimen in the session in the same direction.

The reporting rules that follow: quote the velocity with the combined uncertainty, the
coverage factor and the specimen count — "$4500 \pm 5$ m/s ($k = 2$, $n = 5$), with
1.1 % between-specimen variability" — and keep the **repeatability** of one specimen
separate from the **reproducibility** across specimens, because it is the second that the
science uses. Say which terms are systematic: delay, coupling, length calibration and
pore pressure belong in the method description, not only in the error bar.

## 7. Assumptions and regime of validity

1. **The path is the specimen length.** True only with parallel faces, full contact and
   a wave that is not edge-diffracted; the end effect of the previous lesson is part of
   this term.
2. **The delay is constant.** Coupling, temperature and contact pressure move it; the
   two-length check repeated at the end of a session is the control.
3. **The material is isotropic and homogeneous at the measurement scale.** A layered or
   cracked plug violates this, and the measured velocity depends on orientation and on
   frequency.
4. **The strain amplitude is small.** Ultrasonic strains are of order $10^{-7}$, so the
   *dynamic* moduli measured here are not automatically the static moduli of a mechanical
   test — the difference is real, commonly tens of percent in soft rocks, and it must be
   stated when both are quoted.
5. **The pulse is a pulse, not a sinusoid.** The arrival-time convention (first break,
   first maximum, cross-correlation) defines the velocity, and two conventions give
   different numbers; the convention belongs in the metadata.
6. **The pore fluid is known and controlled.** A partially saturated specimen has a
   velocity that depends on the fluid distribution, not just its amount, and it is not
   reproducible between sessions unless the saturation protocol is.

## 8. The honest summary

- The experiment measures a time; the velocity is a difference that needs the delay.
- Ignoring a 2.5 µs delay cost 22 % at $L = 40$ mm, and the error scaled as $1/L$, which
  mimics dispersion.
- Two lengths give both $v$ and $t_0$: 4500.00 m/s and 2.500 µs, exactly, from a clean
  synthetic pair.
- A 40 mm specimen requires $f \ge 0.562$ MHz; the upper bound comes from attenuation,
  beam spread and heterogeneity, not from the wavelength rule.
- $M = 53.66$, $G = 17.91$, $K = 29.78$ GPa, $\nu = 0.2494$, $E = 44.77$ GPa — with $K$ and
  $\nu$ the most sensitive to velocity errors.
- Effective pressure governs the response: a 10 MPa pore-pressure difference moves $V_P$
  by 39 m/s at 50 MPa confining pressure.
- The timing term dominates the budget (0.1125 % against 0.0250 % for the length), and a
  0.10 µs delay error is ten times larger and systematic.

## 9. Python demonstration

[`code/ultrasonic_velocity_demo.py`](./code/ultrasonic_velocity_demo.py) prints every
number quoted above: the naive and two-length velocities with the recovered delay, the
wavelength table and the minimum frequency, the elastic moduli from $V_P$ and $V_S$, the
pressure-velocity relation with its local slope and an effective-pressure table, and the
uncertainty budget with the sensitivity to a delay error.

```bash
cd 23-field-methods-instruments/06-laboratory-measurements/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ultrasonic_velocity_demo.py
```

## 10. Exercises

Worked problem sets are in
[`exercises/02-ultrasonic-velocity-exercises.md`](./exercises/02-ultrasonic-velocity-exercises.md)
and
[`exercises/02-ultrasonic-velocity-solutions.md`](./exercises/02-ultrasonic-velocity-solutions.md).

## 11. Mastery checkpoint

Without notes:

1. A 30.0 mm specimen gives a travel time of 9.20 µs. Compute the naive velocity, then
   the velocity and delay from a second specimen of 50.0 mm with a time of 13.40 µs.
2. Compute the minimum frequency for a 25 mm specimen at 3800 m/s with $L \ge 5\lambda$.
3. With $\rho = 2400$ kg/m³, $V_P = 3800$ m/s and $V_S = 2100$ m/s, compute $M$, $G$, $K$,
   $\nu$ and $E$.
4. Using the lesson's synthetic relation, compute $V_P$ at 75 MPa and its local slope.
5. Compute the relative velocity uncertainty for $\delta L/L = 0.02$ % and
   $\delta t/(t-t_0) = 0.10$ %, and state which term you would improve first.

## 12. Common pitfalls

1. **Forgetting the delay.** It is a percent-level error that grows as $1/L$.
2. **Measuring the delay once.** Coupling and temperature move it during a session.
3. **Quoting a velocity at one pressure.** The curve and its path are the measurement.
4. **Comparing datasets at different effective pressures.** The confining pressures may
   match while the pore pressures do not.
5. **Confusing dynamic and static moduli.** The strains differ by orders of magnitude.
6. **Using a different arrival convention than the one calibrated.** First break and
   first maximum are different velocities.
7. **Reporting the repeatability as the uncertainty.** The between-specimen variability
   is what the science uses.

## 13. Where this is used

- Rock-physics laboratories producing the velocity, density and modulus inputs to
  seismic interpretation and to fluid substitution — see
  [05-04-03 Gassmann Fluid Substitution and Saturation Effects](../../05-core-geophysics/04-rock-physics/03-gassmann-fluid-substitution.md).
- Pressure-dependent studies of reservoir, caprock and geothermal rocks, where effective
  pressure is a design variable.
- Time-lapse and 4D feasibility work, where a velocity change of a fraction of a percent
  must be resolved — see
  [23-06-08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md).
- Every laboratory result quoted in a rock-physics model: the velocity's uncertainty is
  the model's uncertainty.

## 14. Related lessons

- [01 Sample Preparation, Coring and Drying Protocols](01-sample-preparation.md) —
  the geometry and drying that precede this measurement.
- [03 Laboratory Density, Porosity and Permeability Measurement](03-density-porosity-lab.md) —
  the density that converts velocity to modulus.
- [07 Rock Mechanics Testing: Strength, Friction and Fracture](07-rock-mechanics-lab.md) —
  the static moduli measured in the same laboratory.
- [08 Laboratory Uncertainty Budgets and Reporting](08-lab-data-uncertainty.md) —
  how the budget here is combined and reported.

## 15. Self-assessment checklist

- [ ] I can compute a velocity with the delay included and measure the delay from two
      lengths.
- [ ] I can choose a frequency from the wavelength criterion and name the upper limit.
- [ ] I can convert $V_P$ and $V_S$ into $M$, $G$, $K$, $\nu$ and $E$.
- [ ] I can evaluate a pressure-velocity relation and its local slope.
- [ ] I can compute an effective pressure and state why it, not $P_c$, governs.
- [ ] I can build and interpret a velocity uncertainty budget.
- [ ] I can separate systematic from scatter terms.
