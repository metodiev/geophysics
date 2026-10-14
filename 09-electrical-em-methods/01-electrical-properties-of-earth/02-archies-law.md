---
id: 09-01-02
title: "Archie's Law, Porosity and Saturation"
level: advanced
prereqs: ["09-01-01", "05-04-01"]
tags: [electrical-methods, archie, porosity, saturation, formation-factor]
---

# Archie's Law, Porosity and Saturation

Archie's law is the most used and the most over-extended equation in
near-surface geophysics. Stated as an empirical relation it is simple; stated as
a physical law it is false. This lesson derives what can be derived from a
capillary-tube model, states the empirical forms explicitly as empirical, and
then does the thing that matters operationally: quantifies what the data can and
cannot separate.

**All models and data in this module are SYNTHETIC.** Constants such as $a$,
$m$ and $n$ below are chosen teaching values, not calibrated measurements.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the formation factor $F = \rho_0/\rho_w$ and derive the
   capillary-tube result $F = \tau/\phi$.
2. **State** Archie's empirical laws
   $\rho_0 = a\,\rho_w\,\phi^{-m}$ and $\rho_t = \rho_0 S_w^{-n}$, identifying
   precisely which parts are derivable and which are fits.
3. **Compute** $F$, $\phi$ and $S_w$ from given electrical data, including the
   inversion for $\phi$ and its error amplification $1/m$.
4. **Demonstrate** that $a$ and $m$ are exactly compensating at a single
   porosity, and state what additional data break that degeneracy.
5. **Quantify** the trade-off between the saturation exponent $n$ and the
   assumed $\rho_0$, and explain why a wrong $n$ beats measurement noise.
6. **Explain** why saturation becomes hard to resolve as $S_w \to 1$.
7. **State** the assumptions of Archie's law and name the rocks that violate
   each one.

## Prerequisites

- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](01-resistivity-conductivity.md) —
  $\rho$, $\sigma$, geometry and units.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  porosity as a rock property and how it is measured.

## 1. Where the porosity dependence comes from

Consider an insulating matrix permeated by a bundle of straight tubes of total
cross-sectional area fraction $\phi$. The rock's conductivity is that of the
fluid, diluted by the *area* fraction: $\sigma_0 = \phi\,\sigma_w$, hence
$F = \sigma_w/\sigma_0 = 1/\phi$. Straight tubes are unrealistic: the current
must zig-zag, and a longer path length $L_e$ and smaller effective area both
increase the resistance. Writing $\tau = (L_e/L)^2$ for the tortuosity gives the
classical geometric result

$$F = \frac{\rho_0}{\rho_w} = \frac{\tau}{\phi}.$$

This is a derivation with a stated assumption, and it already identifies the two
knobs: **how much pore space** and **how well connected it is**.

## 2. Archie's laws, stated as empirical forms

In practice the exponent form is used:

$$\rho_0 = a\,\rho_w\,\phi^{-m}, \qquad
\rho_t = \rho_0\,S_w^{-n}, \qquad S_w\in(0,1],$$

where $a$ is a dimensionless prefactor of order one, $m$ the **cementation
exponent**, and $n$ the **saturation exponent**. Both are fitted, both depend on
the rock type, and neither is a physical constant. Substituting the first into
the second:

$$\rho_t = a\,\rho_w\,\phi^{-m}S_w^{-n}.$$

Three of the four unknowns ($\rho_w$, $m$, $n$) must be supplied before a
resistivity can be read as a porosity or a saturation.

## 3. What the fit quietly assumes

Put the empirical form and the geometric result side by side. $F = a\phi^{-m}$
implies $\tau = a \phi^{1-m}$. For the common choice $a=1$, $m=2$ this reads
$\tau = 1/\phi$: the *tortuosity becomes a function of porosity*, growing from
$2.5$ at $\phi = 0.40$ to $20$ at $\phi = 0.05$ — the demonstration prints
exactly those numbers, together with the ratio

$$\frac{F(0.05)}{F(0.30)} = \frac{400.0}{11.111} = 36,$$

for a porosity ratio of 6. A porosity proxy with a gain of six-to-one on a
paired change is a good proxy; a *geometry-independent* one it is not. The
honest reading is: **$m$ is a rock-type label, not a measured tortuosity.**

## 4. Worked example: inverting Archie for porosity

Let $a = 1$, $\phi = 0.25$, so

$$F = 0.25^{-2} = 16.000, \qquad \rho_0 = F\rho_w = 16.0\
\Omega\,\mathrm{m}\ \text{for}\ \rho_w = 1.0\ \Omega\,\mathrm{m}.$$

Now the inverse problem. From $F = a\phi^{-m}$,

$$\phi = \left(\frac{a}{F}\right)^{1/m},
\qquad \frac{\mathrm{d}\phi}{\phi} = -\frac{1}{m}\frac{\mathrm{d}F}{F}.$$

The demo prints the consequence of using the wrong exponent:

| $m$ used | inferred $\phi$ | error against 0.25 |
|---|---|---|
| 1.5 | 0.1575 | $-37.00\%$ |
| 2.0 | 0.2500 | $0.00\%$ |
| 2.5 | 0.3299 | $+31.95\%$ |

A 25% error in $m$ costs more than 30% in porosity, while a 10% error in a
*measured* $F$ costs only 5%. **The exponent is a bigger error source than the
measurement.** This is a pattern that recurs in every lesson of this folder:
calibration uncertainty beats instrumental uncertainty.

## 5. The $(a,m)$ degeneracy

One measurement cannot give both parameters. The demo takes a synthetic
observation $\phi = 0.25$, $F = 25.0$ and prints the family
$a = F\phi^{m}$:

| $m$ | 1.5 | 1.8 | 2.0 | 2.2 | 2.5 | 3.0 |
|---|---|---|---|---|---|---|
| $a$ | 3.125 | 2.062 | 1.5625 | 1.184 | 0.781 | 0.391 |

Every row reproduces the datum *exactly*. The degeneracy is broken only by a
second porosity: with $F_1 = a\phi_1^{-m}$ and $F_2 = a\phi_2^{-m}$,

$$m = \frac{\ln(F_2/F_1)}{\ln(\phi_1/\phi_2)}, \qquad a = F_1\phi_1^{m}.$$

Two porosity–formation-factor pairs, measured on the same rock type, determine
the pair. One pair determines a curve. That is the entire content of "$a$ and
$m$ are correlated" in the literature.

## 6. Saturation and its resolution

With $\rho_0 = 16.0\ \Omega\,\mathrm{m}$ and $n = 2$ the demo prints

| $S_w$ | 1.00 | 0.80 | 0.60 | 0.40 | 0.20 |
|---|---|---|---|---|---|
| $\rho_t$ ($\Omega\,\mathrm{m}$) | 16.00 | 25.00 | 44.44 | 100.00 | 400.00 |
| change for $\Delta S = 0.01$ | $-2.00\%$ | $-2.50\%$ | $-3.33\%$ | $-5.00\%$ | $-10.00\%$ |

Because $\mathrm{d}\rho_t/\rho_t = -n\,\mathrm{d}S/S$,

$$\frac{\delta S}{S} = -\frac{1}{n}\frac{\delta\rho_t}{\rho_t},$$

so to resolve $S = 0.60$ to 10% the resistivity must be known to
$10\%/2 = 5.0\%$ — the demo prints both that and the 20% case (10.0%). Note the
direction: a **large** $n$ makes the measurement *less* sensitive to saturation,
because it divides the observable change.

The worked synthetic case: a 5% noise realisation gives
$\rho_t = 43.40\ \Omega\,\mathrm{m}$ instead of $44.44$, and

$$S = \left(\frac{\rho_0}{\rho_t}\right)^{1/n}
= \left(\frac{16.00}{43.40}\right)^{1/2} = 0.6072,$$

a $+1.20\%$ error from a 5% measurement error — the exponent divides. Using
$n = 2.5$ instead gives $S = 0.6709$, an error of $+11.8\%$: **the exponent
error is ten times the measurement noise.**

## 7. Regime of validity

Archie's law is an *empirical* relation and its validity is bounded:

1. **Clean, water-wet rocks.** Clays add a parallel conduction path; see
   [09-01-04](04-clay-and-surface-conduction.md), where the same synthetic
   sample is shown to produce a saturation of 370% if the clay term is ignored.
2. **No conductive minerals.** Sulphides and graphite conduct electronically and
   break the assumption that the matrix is insulating;
   [09-01-03](03-conduction-mechanisms.md) quantifies the parallel and series
   bounds.
3. **Uniform, non-fractured pore structure at the sample scale.** Fractures,
   vugs and dual porosity do not follow a single power law.
4. **A single saturating fluid, no wettability change.** Mixed saturation and
   oil-wet surfaces change $n$ itself.
5. **$\rho_w$, $m$ and $n$ are calibrated for the rock in question** — from
   core, logs or water samples. Uncalibrated Archie is a hypothesis, not a
   measurement.
6. **The measurement is in the same frequency band as the calibration.** Surface
   conduction and polarisation both disperse; see
   [09-01-05](05-temperature-and-pressure-effects.md).

## 8. Mastery checkpoint

1. Derive $F = \tau/\phi$ and state the two assumptions that fail in a clay.
2. A clean sand has $a = 1$, $m = 2.1$, $\phi = 0.30$, $\rho_w = 0.5\
   \Omega\,\mathrm{m}$. Compute $F$, $\rho_0$ and $\rho_t$ at $S_w = 0.5$ with
   $n = 2$.
3. Two cores from the same unit give $F = 32$ at $\phi = 0.18$ and $F = 12$ at
   $\phi = 0.30$. Compute $m$ and $a$.
4. The measured $\rho_t$ is 5% higher than expected. List, in order, the three
   explanations you would test first, and say what measurement each needs.

## 9. Common pitfalls

1. **Treating $m$ as universal.** It is a fit for a rock type; quoting it to
   three figures implies a precision the model does not have.
2. **Reading a resistivity as a saturation.** Without $m$, $n$ and $\rho_w$ it
   is not a saturation; it is a resistivity.
3. **Fitting $a$ and $m$ from one porosity.** Section 5 shows the result is a
   curve.
4. **Ignoring the 1/n division.** Saturation uncertainty is *bigger* than
   resistivity uncertainty whenever $n > 1$, and $n$ is nearly always $> 1$.
5. **Applying Archie where the matrix conducts.** Sulphide or graphite
   mineralisation destroys the premise.
6. **Forgetting that $\rho_w$ varies with temperature and salinity.** A 20 K
   change moves $\rho_w$ by tens of per cent — see
   [09-01-05](05-temperature-and-pressure-effects.md).

## 10. Related modules

- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](01-resistivity-conductivity.md).
- [09-01-03 Electrolytic, Electronic and Surface Conduction](03-conduction-mechanisms.md) —
  what to do when the matrix conducts.
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](04-clay-and-surface-conduction.md) —
  the clay correction, worked numerically.
- [14-03-02 Archie's Law and Saturation Estimation](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/02-archie-and-saturation.md) —
  the hydrogeological use of the same relation, with field practice.
- [09-02 Resistivity Methods](../02-dc-resistivity/README.md) — how $\rho$ is
  measured in the ground.

## 11. Demonstration and exercises

- [`code/archies_law_demo.py`](code/archies_law_demo.py) prints every table used
  above, including the tortuosity reading, the $(a,m)$ family, the saturation
  sensitivity and the round-trip checks.
- [Exercises](exercises/02-archies-law-exercises.md) and
  [worked solutions](exercises/02-archies-law-solutions.md).
