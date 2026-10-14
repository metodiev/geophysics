---
id: 13-06-01
title: "Isostasy and Flexure: Modelling Lithospheric Strength"
level: doctoral
prereqs: ["13-01-03", "13-03-04", "07-03-01"]
tags: [geodynamics, tectonophysics, isostasy, flexure, lithosphere, admittance]
---

# Isostasy and Flexure: Modelling Lithospheric Strength

> **All models and data in this module are SYNTHETIC.** The densities, elastic
> thicknesses and loads below are chosen teaching values with stated units, not
> measured lithospheres. Every number is printed by
> [`code/isostasy_flexure_modelling_demo.py`](code/isostasy_flexure_modelling_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Airy compensation condition $r = [\rho_c/(\rho_m-\rho_c)]h$ and
   **compute** crustal roots and Moho depths for a load.
2. **Compute** the attraction of a sinusoidally corrugated interface,
   $2\pi G\,\Delta\rho\,a\,e^{-kz}$, and use it to show why compensation reduces
   an anomaly without removing it.
3. **Derive** the flexural equation $D\nabla^4w + \Delta\rho\,g\,w = q$, the
   rigidity $D = E T_e^3/[12(1-\nu^2)]$, the flexural parameter
   $\alpha = (D/\Delta\rho g)^{1/4}$ and the periodic reduction factor
   $1/(1+X)$ with $X = Dk^4/(\Delta\rho g)$.
4. **Compute** the deflection under a line load and **verify** the exact ratio
   $1/8$ between it and the naive load-over-$\alpha$ estimate.
5. **Derive** the gravity admittance of a compensated load,
   $Z(k) = 2\pi G\rho_c[1 - e^{-kt}/(1+Dk^4/\Delta\rho g)]$, and **measure** the
   $(T_e, t)$ trade-off it leaves open.
6. **State** the elastic thickness of a lithosphere as a *conditional* result,
   naming the load model and the compensation depth it assumes.
7. **Report** an admitted set of models rather than a single elastic thickness.

## Prerequisites

- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md) —
  the concept of an effective elastic thickness.
- [13-03-04 Basin Formation and Subsidence Modelling](../03-plate-tectonics-quantitative/04-basin-geodynamics.md) —
  the tectonic setting in which flexural loads are measured.
- [07-03-01 Anomaly Interpretation](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md) —
  the gravity anomaly this lesson predicts.
- [02-04-07 Viscoelasticity](../../02-physics/04-elasticity-and-continuum-mechanics/07-viscoelasticity.md) —
  what the elastic approximation replaces.

## 1. Two ways to support a load

A load on the lithosphere can be supported locally — the crust thickens into a
root directly beneath it — or regionally, by the bending strength of an elastic
plate that spreads the support over a distance. Real lithospheres do both, and
the whole craft of "elastic thickness" studies is deciding which, and stating
what was assumed about the other.

The two pictures make different predictions that are both measurable:

| | local (Airy) | regional (flexure) |
|---|---|---|
| crustal root | exactly beneath the load | spread laterally |
| gravity anomaly | reduced by the root | reduced further where the plate is stiff |
| length scale | none | $\alpha = (D/\Delta\rho g)^{1/4}$ |
| observable that discriminates | — | the wavelength dependence of the admittance |

The only way to tell them apart is with data that resolves length scales, which
is why the admittance enters later in the lesson.

## 2. Airy isostasy and its gravity effect

Local compensation balances the weight of a load against the buoyancy of a root:

$$\rho_c\,g\,h = (\rho_m-\rho_c)\,g\,r \quad\Longrightarrow\quad
r = \frac{\rho_c}{\rho_m-\rho_c}\,h .$$

With $\rho_c = 2700$ and $\rho_m = 3300\ \mathrm{kg\,m^{-3}}$ (chosen teaching
values), $r/h = 2700/600 = 4.500$, so the *Moho deepens 4.5 times the topographic
height*:

| $h$ (km) | root $r$ (km) | Moho depth (reference 35 km + $r$) | mass excess (kg/m²) |
|---|---|---|---|
| 0.5 | 2.25 | 37.25 | $1.350\times10^{6}$ |
| 1.0 | 4.50 | 39.50 | $2.700\times10^{6}$ |
| 2.0 | 9.00 | 44.00 | $5.400\times10^{6}$ |
| 3.0 | 13.50 | 48.50 | $8.100\times10^{6}$ |
| 5.0 | 22.50 | 57.50 | $1.350\times10^{7}$ |

Compensation does not simply cancel the gravity anomaly. The topography is a
mass excess at zero depth and the root is a mass deficit at depth $t$; the
attraction of a sinusoidally corrugated interface of amplitude $a$ and density
contrast $\Delta\rho$ at depth $z$ is *exactly*

$$g(k) = 2\pi G\,\Delta\rho\,a\,e^{-kz},$$

so the deeper interface is attenuated. Measured for a periodic load of wavelength
$200\ \mathrm{km}$ and amplitude $2.0\ \mathrm{km}$ over a $35\ \mathrm{km}$ crust:

| contribution | value |
|---|---|
| surface topography attraction | $+226.443$ mGal |
| root attraction at 35 km depth | $-75.410$ mGal |
| **residual (isostatic anomaly)** | $\mathbf{+151.034}$ mGal |
| uncompensated attraction | $+226.443$ mGal |

The residual is **66.7%** of the uncompensated value. Compensation reduced the
anomaly by a third, not to zero. A "fully compensated" load at this wavelength
still produces a large anomaly because the compensating interface is a full
wavelength-scale depth below the surface — and that residual is itself a
measurement of the depth of compensation.

## 3. Derivation: the flexural equation and its solutions

An elastic plate floating on a fluid substrate obeys

$$D\,\nabla^4 w + \Delta\rho\,g\,w = q(x), \qquad
D = \frac{E\,T_e^3}{12(1-\nu^2)},$$

where $w$ is the vertical deflection, $q$ the applied load per unit area,
$\Delta\rho$ the density contrast between the substrate and whatever fills the
deflection, and $T_e$ the effective elastic thickness. The biharmonic term is the
plate's resistance to bending; the $\Delta\rho g w$ term is the buoyancy of the
fluid it displaces.

**Periodic load.** For $q = q_k\cos kx$, $w = w_k\cos kx$ with

$$\boxed{\ w_k = \frac{q_k}{D k^4 + \Delta\rho g} = \frac{q_k}{\Delta\rho g}
\cdot\frac{1}{1+X}, \qquad X = \frac{Dk^4}{\Delta\rho g}\ }$$

so the Airy deflection $q_k/\Delta\rho g$ is reduced by $1/(1+X)$: the plate
filters out short wavelengths. Defining the **flexural parameter**

$$\alpha = \left(\frac{D}{\Delta\rho g}\right)^{1/4}$$

makes $X = (k\alpha)^4$, and the transition $X = 1$ occurs at

$$\lambda_c = 2\pi\left(\frac{4D}{\Delta\rho g}\right)^{1/4} = 2\pi\sqrt{2}\,\alpha .$$

**Line load.** For a line load $V_0$ (force per unit length) the decaying solution
is

$$w(x) = \frac{V_0\alpha^3}{8D}\,e^{-x/\alpha}
\bigl[\cos(x/\alpha) + \sin(x/\alpha)\bigr],$$

with a zero crossing at $x = 3\pi\alpha/4$ and a small negative bulge beyond it —
the flexural moat.

## 4. Worked example: rigidity, length scale and deflection

*Problem.* Compute $D$, $\alpha$ and the peak deflection for
$T_e = 5, 10, 25, 50\ \mathrm{km}$, with $E = 70\ \mathrm{GPa}$,
$\nu = 0.25$, $\Delta\rho = 600\ \mathrm{kg\,m^{-3}}$ and a line load
$V_0 = 1.0\times10^{12}\ \mathrm{N\,m^{-1}}$ (which is a 3 km high, 12 km wide
ridge of crustal rock).

1. $12(1-\nu^2) = 12(1-0.0625) = 11.25$, so $D = 70\times10^9 T_e^3/11.25 =
   6.222\times10^9 T_e^3$ (SI, $T_e$ in metres).
2. For $T_e = 25\ \mathrm{km}$: $T_e^3 = 1.5625\times10^{13}$, $D = 9.722\times10^{22}$ N m.
3. $\alpha = [D/(600\times9.81)]^{1/4} = (1.652\times10^{19})^{1/4} = 6.38\times10^4$ m
   $= 63.8$ km.
4. $w(0) = V_0\alpha^3/(8D) = 10^{12}\times2.60\times10^{14}/(8\times9.722\times10^{22})
   = 3.34\times10^{2}$ m $= 0.33$ km.

Measured for the four thicknesses:

| $T_e$ (km) | $D$ (N m) | $\alpha$ (km) | $w(0)$ (km) | $w(\alpha)/w(0)$ | $w(3\alpha)/w(0)$ |
|---|---|---|---|---|---|
| 5 | $7.778\times10^{20}$ | 19.1 | 1.11 | 0.5083 | $-0.0423$ |
| 10 | $6.222\times10^{21}$ | 32.1 | 0.66 | 0.5083 | $-0.0423$ |
| 25 | $9.722\times10^{22}$ | 63.8 | 0.33 | 0.5083 | $-0.0423$ |
| 50 | $7.778\times10^{23}$ | 107.2 | 0.20 | 0.5083 | $-0.0423$ |

The two ratios are **independent of $T_e$** because they are properties of the
shape function alone — a useful consistency check on any implementation. Third,
the deflection decreases as $T_e$ increases even though $\alpha$ grows: the peak
deflection scales as $\alpha^3/D \propto D^{-1/4}$.

The demonstration also checks an exact algebraic identity. The naive "Airy"
estimate for the same force spread over a width $\alpha$ is $V_0/(\Delta\rho g
\alpha)$; its ratio to the line-load value is

$$\frac{w(0)}{V_0/(\Delta\rho g\alpha)} = \frac{\alpha^4\,\Delta\rho\,g}{8D}
= \frac{1}{8}$$

because $\alpha^4 \equiv D/(\Delta\rho g)$. The measured ratio is 0.1250 in every
row. The ratio is a constant, not a limit, and the measurement is a test of the
algebra rather than of the Earth.

## 5. The compensation wavelength, measured

The reduction factor $1/(1+X)$ is the fraction of the Airy deflection the plate
actually achieves:

| $T_e$ (km) | $\alpha$ (km) | $\lambda_c$ (km) | reduction at $\lambda = 500$ km |
|---|---|---|---|
| 5 | 19.1 | 169.4 | 0.9967 |
| 10 | 32.1 | 284.9 | 0.9743 |
| 25 | 63.8 | 566.5 | 0.7083 |
| 50 | 107.2 | 952.7 | 0.2328 |

and for a fixed $\lambda = 300$ km:

| $T_e$ (km) | 1 | 5 | 10 | 25 | 50 |
|---|---|---|---|---|---|
| $w$/Airy | 0.99980 | 0.97520 | 0.83098 | 0.23934 | 0.03784 |

This table is the physical content of "elastic thickness": it says over which
wavelengths the lithosphere behaves locally. It also says why $T_e$ is hard to
measure: at $\lambda \ll \lambda_c$ every $T_e$ gives a reduction near 1 and at
$\lambda \gg \lambda_c$ every $T_e$ gives a reduction near $1/(k\alpha)^4$, which
is a steep function of $T_e$ but a very small deflection.

## 6. The admittance, and the trade-off it leaves open

Combine the load and its compensation. A surface load of amplitude $h$ with the
Moho deflected by $\delta$ at depth $t$ gives, using the interface formula of
Section 2 and the flexural relation $\delta = -(\rho_c/\Delta\rho_m)h/(1+X)$,

$$\boxed{\ Z(k) = \frac{g(k)}{h(k)} = 2\pi G\rho_c
\left[1 - \frac{e^{-kt}}{1 + Dk^4/(\Delta\rho g)}\right]\ }$$

The demonstration builds a synthetic "measurement" of $Z(k)$ with $T_e = 25$ km
and $t = 35$ km at six wavelengths from 100 to 800 km, adds 1% noise, and asks
which $(T_e,t)$ pairs reproduce it:

| wavelength (km) | 100 | 150 | 200 | 300 | 500 | 800 |
|---|---|---|---|---|---|---|
| $Z$ (mGal/km) | 0.1132 | 0.1127 | 0.1110 | 0.1002 | 0.0616 | 0.0323 |
| noisy $Z$ | 0.1126 | 0.1132 | 0.1101 | 0.1021 | 0.0607 | 0.0322 |

Searching the plane, with the compensation depth fitted at each $T_e$:

| $T_e$ (km) | 10 | 15 | 20 | 25 | 30 | 40 | 60 | 100 |
|---|---|---|---|---|---|---|---|---|
| best $t$ (km) | 50.3 | 46.1 | 41.0 | 34.7 | 27.2 | 8.7 | 5.0 | 5.0 |
| rms misfit | 11.98% | 8.13% | 4.10% | 1.01% | 4.26% | 10.86% | 38.13% | 82.13% |

The ridge is the point: **the compensation depth demanded by the data falls as
$T_e$ rises**, because the data constrain the combination
$e^{-kt}/(1+Dk^4/\Delta\rho g)$. Raising the admissible misfit to twice the
injected noise (2%) admits

$$T_e \in [23.0,\ 26.5]\ \mathrm{km}
\quad\text{with}\quad t \in [32.6,\ 37.3]\ \mathrm{km},$$

8 of 111 trial thicknesses. The admitted *thickness* range is 3.5 km wide against
a value of 25 km, and every model in it has a *different* compensation depth. A
result quoted as "$T_e = 25$ km" therefore omits three things: the range, the
compensation depth that goes with it, and the assumption that the load is at the
surface and the compensation a single interface. A buried load or a distributed
compensation changes $Z(k)$ and hence the admitted set.

## 7. Assumptions and regime of validity

1. **The plate is thin, elastic and continuous.** $T_e$ is an *effective*
   parameter that stands in for a temperature- and stress-dependent rheology; it
   is not a measured elastic layer.
2. **Deflections are small compared with $T_e$ and the load wavelength.** The
   linear plate equation drops the membrane term; for large deflections the
   problem becomes non-linear and the inferred $T_e$ depends on the load.
3. **The load and the compensation are one interface each.** Real loads are
   distributed in depth and in time; each extra degree of freedom trades against
   $T_e$.
4. **The substrate is a fluid of constant density contrast.** Viscoelastic
   relaxation, a layered mantle and the finite depth of the asthenosphere all
   change the long-wavelength response.
5. **$E$ and $\nu$ are assumed.** $T_e \propto D^{1/3}$, so a 20% error in $E$ is
   a 6% error in $T_e$ — smaller than the $T_e$–$t$ trade-off, but not
   negligible.
6. **The admittance is measured over a band.** The admitted set is conditional on
   the wavelengths, the noise level and the model form; none of those is a
   property of the Earth.

## Mastery checkpoint

Without notes:

1. Derive the Airy root formula and compute $r$ for $h = 3$ km with
   $\rho_c = 2800$, $\rho_m = 3350\ \mathrm{kg\,m^{-3}}$.
2. Derive $w_k = q_k/(Dk^4+\Delta\rho g)$ from the plate equation, and show that
   $\alpha^4 = D/(\Delta\rho g)$ makes $X = (k\alpha)^4$.
3. Compute $D$ and $\alpha$ for $T_e = 30$ km, $E = 70$ GPa, $\nu = 0.25$,
   $\Delta\rho = 500\ \mathrm{kg\,m^{-3}}$, and state the compensation wavelength.
4. Show that the ratio of the line-load deflection to $V_0/(\Delta\rho g\alpha)$
   is exactly $1/8$, and explain why the demonstration's measured ratio is
   constant across four thicknesses.
5. Write down the admittance formula for a surface load with a single
   compensation interface, and explain in two sentences why $T_e$ and $t$ trade
   off.
6. A study reports $T_e = 40 \pm 2$ km from an admittance fit. List three
   assumptions that must hold for that error bar to mean what it appears to mean.

## Common pitfalls

1. **Reporting $T_e$ without the load model.** Surface versus buried loading
   changes the answer by more than the quoted error in most studies.
2. **Treating the elastic thickness as a real elastic layer.** It is an
   effective parameter that varies with load age and curvature.
3. **Assuming Airy compensation to compute a root and then using it to interpret
   a short-wavelength anomaly.** At $\lambda \ll \lambda_c$ the plate does not
   compensate at all.
4. **Reading a single admittance value.** Only the wavelength dependence carries
   information about $T_e$.
5. **Forgetting the $1/8$ factor.** Comparing a line-load deflection with a
   distributed-load estimate without the shape factor introduces a factor of
   eight.
6. **Quoting an error bar from the noise only.** The admitted set is dominated by
   the model form and the $T_e$–$t$ ridge, not by the noise.

## Related modules

- [13-01-03 Lithospheric Strength, Effective Elastic Thickness and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md) —
  the theory of the effective elastic thickness.
- [13-06-03 Glacial Isostatic Adjustment: Ice, Viscosity and Sea Level](03-glacial-isostatic-adjustment.md) —
  what happens when the substrate is viscous rather than elastic.
- [07-03 Gravity Anomalies and Modelling](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/README.md) —
  the observations this model predicts.
- [13-03-04 Basin Formation and Subsidence Modelling](../03-plate-tectonics-quantitative/04-basin-geodynamics.md) —
  the tectonic application.
- [18-07 Joint and Multi-Physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md) —
  how a second observable breaks the $(T_e,t)$ trade-off.

Companion exercises:
[`exercises/01-isostasy-flexure-modelling-exercises.md`](exercises/01-isostasy-flexure-modelling-exercises.md)
and
[`exercises/01-isostasy-flexure-modelling-solutions.md`](exercises/01-isostasy-flexure-modelling-solutions.md).
Run the demonstration with

```bash
cd 13-geodynamics-tectonics/06-crustal-and-lithospheric-dynamics/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python isostasy_flexure_modelling_demo.py
```
