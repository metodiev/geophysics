---
id: 05-02-04
title: "Reduction of Observations to Anomalies"
level: advanced
prereqs: ["05-02-03"]
tags: [reductions, free-air, bouguer, normal-field, datum, residual-anomaly]
---

# Reduction of Observations to Anomalies

## Learning objectives

1. **Derive** the free-air and Bouguer corrections from first principles, with
   units, rather than recalling their coefficients.
2. **Explain** the role of the normal (latitude) field and why it is treated as
   a reference rather than a correction in a small survey.
3. **Order** the corrections and state what each removes.
4. **Quantify** the sensitivity of a Bouguer anomaly to the assumed density.
5. **State** which parts of a reduction are measurement, which are model, and
   which are convention.

## Prerequisites

- [05-02-03 Noise, Drift, Tides and Instrument Bias](./03-noise-and-drift.md)
- [02-08-05 Equipotential Surfaces, Geoid and Level Surfaces](../../02-physics/08-potential-theory/05-equipotentials.md)

## 1. Intuition

A raw reading contains, in order of size: the bulk attraction of the whole
Earth, the elevation effect of the station, the attraction of the rock between
the station and the datum, the latitude effect, the tide, the drift, and last
the target anomaly. Reductions remove the first five so that the sixth becomes
visible. Every reduction is a *model*, and its assumptions are the dominant
uncertainty in shallow interpretation.

## 2. Definitions

**Normal field** $g_\text{norm}(\varphi)$: the gravity of the reference
ellipsoid at latitude $\varphi$. Reference, not correction.

**Free-air correction**: the change in $g$ with elevation above the datum,
assuming no rock between station and datum.

**Bouguer correction**: removes the attraction of the slab of rock between the
station and the datum, using an assumed density $\rho_B$ (the *Bouguer
density*).

**Bouguer anomaly**: the residual after normal field, free-air, Bouguer and
terrain (and often isostatic, regional) reductions.

## 3. Derivations

### 3.1 Free-air

Differentiate $g = GM/r^2$ with respect to $r$:

$$\frac{dg}{dr} = -\frac{2GM}{r^3} = -\frac{2g}{r}.$$

$M$ is never needed. With $g = 9.8$ m s⁻² and $R = 6378137$ m (WGS 84
semi-major axis, a defining constant):

$$\frac{dg}{dh} = -\frac{2(9.8)}{6378137} = -3.0730\times10^{-6}\ \mathrm{(m\,s^{-2})\,m^{-1}}
= -0.30730\ \mathrm{mGal\,m^{-1}}.$$

The conventional $0.3086$ mGal/m differs by about 0.4% because it also includes
a second-order term and uses the full ellipsoidal normal gravity. **Use the
derived leading term and say so**, or cite the standard formula explicitly —
but do not quote 0.3086 as though it fell out of $GM/r^2$.

### 3.2 Bouguer slab

The vertical attraction of an infinite slab of thickness $t$ and density
$\rho$ is $g_\text{slab} = 2\pi G\rho\, t$. (Proof: integrate
$G\rho\,z/(r^2+z^2)^{3/2}$ over the plane; the angular integral gives $2\pi$.)
Therefore

$$\frac{dg}{dh}\bigg|_\text{Bouguer} = 2\pi G\rho
= 2\pi(6.6743\times10^{-11})(2400) = 1.0065\times10^{-6}\ \mathrm{(m\,s^{-2})\,m^{-1}}
= 0.10065\ \mathrm{mGal\,m^{-1}}.$$

Note the ratio
$(dg/dh)_\text{Bouguer}/|(dg/dh)_\text{free-air}| = 2\pi G\rho/(2g/R) = \pi G\rho R/g = \rho/\rho_*$
with the *derived* reference density

$$\rho_* = \frac{g}{\pi G R} = \frac{9.8}{\pi(6.6743\times10^{-11})(6378137)}
= 7328\ \mathrm{kg\,m^{-3}}.$$

For $\rho = 2400$ the ratio is $2400/7328 = 0.3275$, which the demonstration
confirms to six figures ($0.327518$). Note $\rho_* \approx 1.33\bar\rho_E$: the
free-air gradient is equivalent to the Bouguer attraction of a slab of about
$7.3\times10^{3}$ kg/m³, *not* of the Earth's mean density. (An earlier draft of
this lesson claimed the ratio was $\rho/(3\bar\rho_E)$ with
$\bar\rho_E = 5515$ kg/m³, which gives 0.145 — the numerical check in the
demonstration contradicted it, and the correct statement is the one above.
This is precisely why the demonstration prints the ratio.)

### 3.3 Sign bookkeeping

For a station *above* the datum by $h$:
- the observable is **lower** by $0.3073\,h$ mGal, so the free-air *correction*
  added is $+0.3073h$;
- the slab between station and datum **adds** attraction $0.10065\,h$ mGal
  (for $\rho = 2400$), so the Bouguer *correction* subtracts it.

Getting these two signs wrong produces a doubled error, not a missing term —
the single most common arithmetic blunder in gravity processing.

## 4. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $dg/dh$ free-air | s⁻² | $[g]/[r] = \mathrm{m\,s^{-2}/m}$ |
| $dg/dh$ Bouguer | s⁻² | $[G\rho] = \mathrm{s^{-2}}$ |
| $2\pi G\rho$ | s⁻² | $[\mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-3}}] = \mathrm{s^{-2}}$ ✓ |
| Bouguer density | kg m⁻³ | assumed, not measured |
| anomaly | mGal | $10^{-5}$ m s⁻² |

## 5. Assumptions

1. **Infinite slab** for the Bouguer term; terrain corrections are required
   where relief is significant.
2. **Constant Bouguer density** over the survey area. This is a *choice*.
3. **An ellipsoidal normal field.** The geoid deviates from it by up to ~100 m,
   which is handled by geoid models, not by these corrections.
4. **Vertical station positioning** accurate to better than the target divided
   by $0.31$ mGal/m — for a 0.01 mGal target, about 3 cm.
5. **Tide and drift already removed**, which is the subject of the previous
   lesson.

## 6. Worked examples (measured)

From `code/noise_reduction_demo.py`, with relief from $-8$ to $+8$ m relative to
the base station:

- free-air effect on the readings: $-2.397$ to $+2.397$ mGal;
- Bouguer slab effect: $+0.785$ to $-0.785$ mGal;
- applied free-air correction: $-2.397$ to $+2.397$ mGal;
- applied Bouguer correction: $+0.785$ to $-0.785$ mGal.

**Sensitivity to the Bouguer density** — peak recovered anomaly:

| $\rho_B$ (kg/m³) | peak (mGal) | shift (mGal) |
|---|---|---|
| 2000 | 3.8946 | $-0.1049$ |
| 2200 | 3.9470 | $-0.0525$ |
| 2400 | 3.9995 | 0.0000 |
| 2670 | 4.0703 | $+0.0708$ |
| 3000 | 4.1569 | $+0.1574$ |

A 670 kg/m³ change in the assumed density moves the anomaly by 0.27 mGal — of
the same order as the target for a subtle body. **The Bouguer density must be
reported with the anomaly.**

## 7. Python demonstration

`code/noise_reduction_demo.py` derives both gradients before using them, builds
the readings with the terrain effect included, and prints the correction
magnitudes. Then it sweeps the Bouguer density. Predict the sign of the shift
for $\rho_B = 3000$ before running.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/04-reduction-of-observations-exercises.md`](./exercises/04-reduction-of-observations-exercises.md).

**Common mistakes.** (1) Sign errors between the two corrections. (2) Quoting a
Bouguer anomaly without the density. (3) Omitting terrain corrections in
mountainous ground — where they can exceed the free-air term. (4) Applying a
free-air correction without a tide/drift correction first. (5) Treating the
normal field as negligible over a survey that spans several degrees of latitude.

**Applications.** Regional gravity maps (e.g. for isostasy) use Bouguer or
isostatic anomalies; microgravity surveys for voids use a *local* Bouguer
density measured from a Nettleton-style profile; airborne gravimetry requires
the same reductions with a moving datum.

## Extended worked example: the full correction chain, end to end

The demonstration implements the whole sequence on a synthetic survey: relief
from $-8$ to $+8$ m relative to the base station, Bouguer density 2400 kg/m³,
target anomaly 4.0 mGal, drift 0.05 mGal/h, tide 0.15 mGal, noise 0.02 mGal.

**Derived gradients.** Free air: $-2g/R = -2(9.8)/6378137
= -3.0730\times10^{-6}$ (m s⁻²) m⁻¹ $= -0.307300$ mGal/m. Bouguer:
$2\pi G\rho = 1.0065\times10^{-6}$ (m s⁻²) m⁻¹ $= 0.100646$ mGal/m. Their ratio
is **0.327518**.

**What that ratio is.** The Bouguer-to-free-air ratio is
$2\pi G\rho/(2g/R) = \pi G\rho R/g = \rho/\rho_*$ with the derived
$\rho_* = g/(\pi GR) = 7327.9$ kg m⁻³. So the free-air gradient is equivalent to
the Bouguer attraction of a slab of about $7.3\times10^{3}$ kg m⁻³ — *not* the
Earth's mean density of 5515 kg m⁻³. For $\rho = 2400$ the ratio is
$2400/7327.9 = 0.3275$, matching the measured 0.327518 to six figures. (This is
the check that corrected an earlier draft's claim that the ratio was
$\rho/(3\bar\rho_E)$ with $\bar\rho_E = 5515$, which would give 0.145 and is
wrong by a factor of 2.26.)

**The correction magnitudes.** Over $\pm8$ m of relief: the free-air effect on
the readings spans $-2.397$ to $+2.397$ mGal, and the Bouguer slab effect
$+0.785$ to $-0.785$ mGal. The applied free-air correction is
$-2.397$ to $+2.397$; the applied Bouguer correction is $+0.785$ to $-0.785$.

**Read the signs carefully.** A station *above* the datum reads *low* by
$0.3073h$ (it is further from the Earth's centre), so the free-air correction
*adds* $+0.3073h$. The slab between station and datum *adds* attraction, so the
Bouguer correction *subtracts* it. With $h = +8$ m: the reading contains
$-2.397+0.785 = -1.612$ mGal of terrain effect, and the corrections remove it
with the opposite signs. **Swapping the two signs doubles the error rather than
cancelling it** — the classic blunder.

**The payoff.** The residual after all corrections is 0.0212 mGal against the
stated noise of 0.02 mGal, and the peak recovered anomaly is 3.9995 mGal against
a true 4.0000 mGal. The chain works.

**The dominant uncertainty.** Sweeping $\rho_B$ moves the peak:
2000 → 3.8946, 2200 → 3.9470, 2400 → 3.9995, 2670 → 4.0703, 3000 → 4.1569
mGal. A 670 kg m⁻³ error costs 0.27 mGal, and the shift is *linear* in
$\rho_B$ because the slab term is: the sensitivity is
$2\pi G\,\mathrm{relief}/\mathrm{mGal}$ per unit density. This is why the
Bouguer density is quoted with the anomaly, and why the Nettleton method
(grid-search the density minimising the correlation of the Bouguer anomaly with
topography) is standard practice in areas of significant relief.

## 9. Further reading

- **Blakely (1995).** Chapters 2 and 9. Level: advanced.
- **Telford, Geldart & Sheriff (1990).** Chapter 2. Level: intermediate.
- **Hinze, W. J. et al. (2013). *Gravity and Magnetic Exploration*.**
  Chapters 5–6. Level: graduate. The definitive modern treatment of reductions
  and their assumptions.

## 10. Related lessons

- [05-02-03 Noise, Drift, Tides and Instrument Bias](./03-noise-and-drift.md)
- [07-01-04 Gravity Reduction](../../07-gravity-geodesy/01-gravity-fundamentals/04-gravity-reduction.md)
- [08-03-03 Reduction to Pole](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/03-reduction-to-pole.md)

## Self-assessment checklist

- [ ] I can derive both gradients and check their units.
- [ ] I can state the sign of each correction for a station above the datum.
- [ ] I can compute the sensitivity of an anomaly to $\rho_B$.
- [ ] I can list the corrections in order and say what each removes.
- [ ] I can state which reductions are measurement-based and which are model.
