---
id: 09-01-04
title: "Clay Effects, CEC and Membrane Polarisation"
level: graduate
prereqs: ["09-01-02", "09-01-03", "05-04-07"]
tags: [electrical-methods, clay, cec, surface-conduction, induced-polarisation, debye]
---

# Clay Effects, CEC and Membrane Polarisation

Clay is the single largest source of error in resistivity interpretation, and
the single largest source of signal in induced polarisation. Both facts come from
one mechanism: a negatively charged mineral surface attracts a diffuse cloud of
cations, and that cloud conducts and polarises. This lesson carries the
mechanism from a measurable rock property (the cation exchange capacity, CEC)
to a conductivity, then to a saturation that is physically impossible if the
term is ignored, and finally to the frequency dependence that IP measures.

**All models and data in this module are SYNTHETIC.** The CEC values, grain
density, counter-ion conductance and Debye parameters are chosen teaching
values, not measurements.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the pore-volume cation excess $Q_v$ from the CEC, grain density
   and porosity, and state its units.
2. **Compute** the surface conductivity $\sigma_s$ from $Q_v$ and the
   counter-ion equivalent conductance, and compare it with the electrolytic
   term.
3. **Show** that ignoring the clay term produces water saturations greater than
   one, and **repair** the calculation.
4. **Quantify** the conditioning of the repair: how a wrong surface term
   propagates into saturation.
5. **Derive** a Debye complex conductivity and compute its amplitude and phase
   spectra.
6. **Verify** the exact identity $(2/\pi)\int|\varphi|\,\mathrm{d}\ln f =
   \ln(\sigma_\infty/\sigma_0)$ numerically, and state how it relates the phase
   spectrum to a chargeability.
7. **State** which quantities must be measured rather than assumed.

## Prerequisites

- [09-01-02 Archie's Law, Porosity and Saturation](02-archies-law.md) —
  $\rho_0$, $F$, $S_w$.
- [09-01-03 Electrolytic, Electronic and Surface Conduction](03-conduction-mechanisms.md) —
  the three-mechanism picture.
- [05-04-07 Electrical Properties, Archie's Law and Clay Effects](../../05-core-geophysics/04-rock-physics/07-electrical-properties-rock.md) —
  the rock-physics catalogue of clay behaviour.

## 1. From CEC to the pore-volume cation excess

The cation exchange capacity is quoted per unit **mass** of solid, in
$\mathrm{meq}/100\,\mathrm{g}$. The electrical effect depends on the cation
excess per unit **pore volume**, $Q_v$ in $\mathrm{eq/L}$. The conversion is
pure bookkeeping. Per unit bulk volume, the solid mass is $\rho_g(1-\phi)$ and
the pore volume is $\phi$, so

$$Q_v = \frac{\mathrm{CEC}}{100}\,\rho_g\,\frac{1-\phi}{\phi}
\qquad(\mathrm{eq/L}),$$

using $1\ \mathrm{meq\,cm^{-3}} = 1\ \mathrm{eq\,L^{-1}}$. With
$\rho_g = 2.65\ \mathrm{g\,cm^{-3}}$ (SYNTHETIC teaching value) the demo prints:

| CEC (meq/100 g) | $Q_v$ at $\phi = 0.15$ | at $\phi = 0.25$ | at $\phi = 0.40$ |
|---|---|---|---|
| 1 | 0.1502 | 0.0795 | 0.0397 |
| 5 | 0.7508 | 0.3975 | 0.1987 |
| 10 | 1.5017 | 0.7950 | 0.3975 |
| 25 | 3.7542 | 1.9875 | 0.9937 |

Units: $\mathrm{eq/L}$. The same clay fabric concentrated into less pore space
gives a larger $Q_v$: the surface charge is fixed and the water volume is not.

## 2. Surface conductivity and its size

Writing the surface contribution as a counter-ion conduction with an equivalent
conductance $\beta$ (SYNTHETIC teaching value
$\beta = 0.10\ \mathrm{(S\,m^{-1})/(eq\,L^{-1})}$),

$$\sigma = \frac{\sigma_w}{F} + \beta Q_v.$$

For $\phi = 0.25$, $F = 16$, $\sigma_w = 0.10\ \mathrm{S\,m^{-1}}$, the
electrolytic term is $\sigma_w/F = 0.00625\ \mathrm{S\,m^{-1}}$, and the demo
prints:

| CEC (meq/100 g) | $Q_v$ (eq/L) | $\sigma_s$ ($\mathrm{S\,m^{-1}}$) | $\sigma_s/(\sigma_w/F)$ |
|---|---|---|---|
| 1 | 0.0795 | 0.00795 | 1.3 |
| 5 | 0.3975 | 0.03975 | 6.4 |
| 10 | 0.7950 | 0.07950 | 12.7 |
| 25 | 1.9875 | 0.19875 | 31.8 |

At $\mathrm{CEC} = 10\ \mathrm{meq/100\,g}$ the surface path already carries
more than ten times the electrolytic current. **$\beta$ is the largest
uncertainty in this model**, and it is the quantity that must be calibrated: it
depends on the cation species, the temperature and the mineralogy.

## 3. The clay problem: a saturation of 370%

Continue with $\mathrm{CEC} = 10$, $\phi = 0.25$, $n = 2$. The measurement is

$$\sigma_\text{meas} = \frac{\sigma_w}{F} + \sigma_s = 0.00625 + 0.07950
= 0.08575\ \mathrm{S\,m^{-1}},$$

and the surface term is $92.7\%$ of it. Read with Archie alone:

$$S = \left(\frac{\sigma_\text{meas}}{\sigma_0}\right)^{1/n}
= \left(\frac{0.08575}{0.00625}\right)^{1/2} = 3.704,$$

i.e. a water saturation of **370%**. The answer is not merely wrong; it violates
the definition of saturation. That is the value of the check: any resistivity
interpretation that produces $S_w > 1$ has forgotten a conduction mechanism, and
the arithmetic says so immediately.

The repair subtracts the surface term *before* inverting:

$$S = \left(\frac{\sigma_\text{meas} - \sigma_s}{\sigma_0}\right)^{1/2}
= \left(\frac{0.08575 - 0.07950}{0.00625}\right)^{1/2} = 1.000.$$

The demo then asks how good $\beta$ must be:

| assumed $\beta$ | 0.00 | 0.05 | 0.10 | 0.20 | 0.30 |
|---|---|---|---|---|---|
| $S$ | 3.7041 | 2.7129 | 1.0000 | no real solution | no real solution |

The last two rows matter: over-correcting makes the numerator negative, and the
model has no solution at all. The operation
$S = [(\sigma - \sigma_s)/\sigma_0]^{1/n}$ is a square root of a difference of
comparable numbers, so the *relative* error in $S$ is roughly half the relative
error in that difference — and the difference can be an order of magnitude
smaller than either term. **This is the worst-conditioned step in the
resistivity workflow.**

## 4. Membrane polarisation and the Debye model

Why does the same mechanism produce a frequency-dependent conductivity? Charge
accumulates at the interface between the cation-rich double layer and the bulk
pore water, and it takes a finite time to build up and relax. The simplest
model is a Debye relaxation of the complex conductivity:

$$\sigma^*(\omega) = \sigma_\infty - \frac{\sigma_\infty - \sigma_0}
{1 + \mathrm{i}\omega\tau}, \qquad \tau = \frac{1}{2\pi f_c},$$

with $\sigma_0$ the DC limit and $\sigma_\infty$ the high-frequency limit. With
the SYNTHETIC values $\sigma_0 = 0.050$, $\sigma_\infty = 0.060\
\mathrm{S\,m^{-1}}$, $f_c = 2.0\ \mathrm{Hz}$ (so $\tau = 79.577\ \mathrm{ms}$),
the demo prints:

| $f$ (Hz) | 0.001 | 0.1 | 0.5 | 2.0 | 5.0 | 50 | $10^{4}$ |
|---|---|---|---|---|---|---|---|
| $\lvert\sigma\rvert$ ($\mathrm{S\,m^{-1}}$) | 0.050000 | 0.050027 | 0.050643 | 0.055227 | 0.058722 | 0.059985 | 0.060000 |
| phase (mrad) | 0.1000 | 9.9698 | 46.4781 | 90.6599 | 58.7558 | 6.6577 | 0.0333 |

The phase peaks at $5.2159^\circ$ very close to $f_c$ (printed maximum at
$1.8197\ \mathrm{Hz}$, not exactly $f_c$ because the peak of $\varphi$ depends on
the ratio $\sigma_\infty/\sigma_0$). A DC resistivity survey sits at the far left
of that table, where the phase is essentially zero: that is what makes "DC"
resistivity legitimate for a *resistivity* measurement and useless for a
*polarisation* measurement.

The DC chargeability is the usual scalar: $m = (\sigma_\infty -
\sigma_0)/\sigma_\infty = 0.1667$.

## 5. A verified phase-area identity

Field IP is often reported as a phase, and the phase spectrum has a rigorous
integral property for models of this kind. The demo computes

$$\frac{2}{\pi}\int_{-\infty}^{\infty}\lvert\varphi(f)\rvert\,\mathrm{d}\ln f
= 0.182321529$$

and compares it with

$$\ln\frac{\sigma_\infty}{\sigma_0} = 0.182321557, \qquad
-\ln(1-m) = 0.182321557,$$

finding a difference of $2.8\times10^{-8}$ against a quadrature error estimate
of $1.3\times10^{-8}$. So for this model

$$\frac{2}{\pi}\int \lvert\varphi\rvert\,\mathrm{d}\ln f
= \ln\frac{\sigma_\infty}{\sigma_0} = -\ln(1-m),$$

and the "phase area" measures $-\ln(1-m)$, **not** $m$. The demo prints that the
first-order reading differs from the area by $9.4\%$: calling the phase area a
chargeability is a small-$m$ approximation, and when $m$ is large the two numbers
diverge (at $m = 0.5$ the area is $0.693$ against $m = 0.500$). This identity is
the frequency-domain face of the Kramers–Kronig relation and it is why a
frequency-domain phase measurement and a time-domain chargeability are related
at all.

## 6. Worked example: full budget of a clay sample

Model $\phi = 0.25$, $\sigma_w = 0.10\ \mathrm{S\,m^{-1}}$,
$\mathrm{CEC} = 10\ \mathrm{meq/100\,g}$, $\rho_g = 2.65$, $\beta = 0.10$:

1. $F = \phi^{-2} = 16.00$; electrolytic term $= 0.00625\ \mathrm{S\,m^{-1}}$.
2. $Q_v = 0.1\times2.65\times0.75/0.25 = 0.795\ \mathrm{eq/L}$.
3. $\sigma_s = 0.10\times0.795 = 0.0795\ \mathrm{S\,m^{-1}}$.
4. total $\sigma = 0.08575\ \mathrm{S\,m^{-1}}$, i.e. $\rho = 11.66\
   \Omega\,\mathrm{m}$.
5. The electrolytic term accounts for $7.3\%$ of the current. At
   $S_w = 0.5$ the electrolytic term halves ($S^{-n} = 4$ multiplies
   $\rho_0$, so $\sigma_w/F$ divides by 4 — the *resistivity* of the pore fluid
   path rises) while $\sigma_s$ is largely unchanged, so the measured
   conductivity becomes $0.00156 + 0.0795 = 0.0811\ \mathrm{S\,m^{-1}}$:
   **a 50% reduction in water saturation changes the measured conductivity by
   5%.** The clay has made the rock insensitive to its own water content.

The check that matters: had the analyst reported $S_w$ from the uncorrected
number, the answer would have been $\sqrt{0.0811/0.00625} = 3.60$, again
impossible.

## 7. Regime of validity

1. **The two-term sum is an empirical model.** It assumes additive, independent
   electrolytic and surface paths; real clays show coupling.
2. **$Q_v$ from CEC assumes all exchange sites contribute to conduction.**
   Sorbed water and blocked sites invalidate the count.
3. **Single relaxation time.** The Debye model is the simplest polarisation; real
   rocks need a distribution of relaxation times (Cole–Cole), treated in
   [09-03-02](../03-induced-polarisation/02-ip-models.md).
4. **Low-frequency, quasi-static regime.** The phase is small ($\lesssim$ tens of
   mrad); above the charge-relaxation frequency of
   [09-01-05](05-temperature-and-pressure-effects.md) the model is irrelevant.
5. **Temperature dependence is ignored here.** Both $\beta$ and $\tau$ are
   strongly temperature dependent; that is the subject of the next lesson.

## 8. Mastery checkpoint

1. Derive $Q_v$ from CEC, $\rho_g$ and $\phi$, and check the units.
2. Compute $\sigma$ for CEC $= 5\ \mathrm{meq/100\,g}$, $\phi = 0.20$,
   $\rho_g = 2.65$, $\sigma_w = 0.2\ \mathrm{S\,m^{-1}}$, $\beta = 0.1$.
3. Use your answer to compute $S_w$ with and without the surface term at
   $n = 2$, and state which one is admissible.
4. Show that the phase-area identity reduces to $\approx m$ for small $m$, and
   give the numerical error of that approximation at $m = 0.1667$.

## 9. Common pitfalls

1. **Using CEC as if it were $Q_v$.** The conversion factor is
   $\rho_g(1-\phi)/\phi$, and it can approach 10.
2. **Forgetting that $\beta$ is calibration, not physics.** It is the number
   that must be measured for the rock in question.
3. **Not checking $S_w \le 1$.** It is a free and decisive test.
4. **Reading the phase area as chargeability.** They differ by 9% at
   $m = 0.17$ and by 39% at $m = 0.50$.
5. **Reporting a clay-rich formation's water content from resistivity alone.**
   Section 6 shows a 50% saturation change moving the conductivity by 5%.

## 10. Related modules

- [09-01-02 Archie's Law, Porosity and Saturation](02-archies-law.md).
- [09-01-03 Electrolytic, Electronic and Surface Conduction](03-conduction-mechanisms.md).
- [09-01-05 Temperature, Pressure and Frequency Dependence](05-temperature-and-pressure-effects.md).
- [09-03 Induced Polarisation](../03-induced-polarisation/README.md) and
  [09-03-02 IP Models](../03-induced-polarisation/02-ip-models.md) — the
  measurement and the models this lesson introduces.
- [14-03-02 Archie's Law and Saturation Estimation](../../14-hydrology-hydrogeophysics/03-petrophysics-hydrology/02-archie-and-saturation.md).

## 11. Demonstration and exercises

- [`code/clay_and_surface_conduction_demo.py`](code/clay_and_surface_conduction_demo.py)
  prints the $Q_v$ table, the surface-conductivity comparison, the impossible
  saturation and its repair, the Debye spectra and the verified phase-area
  identity.
- [Exercises](exercises/04-clay-and-surface-conduction-exercises.md) and
  [worked solutions](exercises/04-clay-and-surface-conduction-solutions.md).
