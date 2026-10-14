---
id: 08-04-01
title: "Induction, Skin Depth, Diffusion and Conductivity Structure"
level: graduate
prereqs: ["02-07-06", "02-07-04"]
tags: [electromagnetism, geomagnetism, induction, skin-depth, diffusion, conductivity, magnetotellurics]
---

# Induction, Skin Depth, Diffusion and Conductivity Structure

A time-varying magnetic field penetrates a conductor only so far. That single
fact is the foundation of every electromagnetic method in this folder: because
the depth of penetration depends on **period** and on **conductivity**, a
measurement of the field at the surface at a range of periods is a measurement of
how conductivity varies with depth. This lesson derives the penetration depth
from Maxwell's equations, verifies the analytic solution with a time-domain
solution of the diffusion equation, and quantifies the two scales — skin depth
and diffusion time — that every later lesson assumes.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the quasi-static diffusion equation for the magnetic field in a
   conductor from Maxwell's equations, and **state** the approximation made.
2. **Derive** the plane-wave solution and the **skin depth**
   $\delta = \sqrt{2\rho/(\omega\mu_0)}$, and **compute** it for a table of
   periods and resistivities.
3. **Verify** the plane-wave solution by an independent time-domain solution of
   the diffusion equation, and **report** the amplitude and phase errors.
4. **Explain** the phase lag of one radian per skin depth and why phase is used
   as an independent measurement.
5. **Compute** the diffusion time $\mu_0\sigma L^{2}$ and the period that skins
   to a given depth, and **use** them to decide which periods probe which depths.
6. **State** the conductivity range of Earth materials and **explain** why the
   method is sensitive to fluids, melt and sulphides.
7. **Distinguish** diffusion from wave propagation in a conductor, and **state**
   when each description applies.

## Prerequisites

- [02-07-06 Electromagnetic Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md) —
  Maxwell's equations, the conduction current, the displacement current.
- [02-07-04 Electromagnetic Induction](../../02-physics/07-electromagnetism/04-em-induction.md) —
  Faraday's law, the physical origin of the induced fields measured here.

## 1. From Maxwell to diffusion

Take Maxwell's equations in a medium of uniform conductivity $\sigma$ and
magnetic permeability $\mu_0$, with no free charge and no source in the region of
interest:

$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t},
\qquad \nabla\times\mathbf{H} = \mathbf{J} + \frac{\partial\mathbf{D}}{\partial t},
\qquad \mathbf{J} = \sigma\mathbf{E}, \qquad \mathbf{B} = \mu_0\mathbf{H}.$$

**The quasi-static approximation.** In the Earth at the periods used here the
displacement current is negligible: its ratio to the conduction current is
$\omega\epsilon_0/\sigma$, which for $\sigma = 10^{-2}$ S m$^{-1}$ and a period of
1 s is about $5.6\times10^{-10}$. Dropping
$\partial\mathbf{D}/\partial t$ is therefore not a marginal decision.

Taking the curl of Faraday's law and substituting,

$$\nabla\times\nabla\times\mathbf{E} = -\mu_0\sigma\frac{\partial\mathbf{E}}{\partial t}
\quad\Longrightarrow\quad
\nabla^{2}\mathbf{E} = \mu_0\sigma\frac{\partial\mathbf{E}}{\partial t},$$

using $\nabla\cdot\mathbf{E}=0$. The same equation holds for $\mathbf{B}$. **The
field obeys a diffusion equation, not a wave equation.** Its diffusivity is

$$D = \frac{1}{\mu_0\sigma} \qquad \left(\mathrm{m^{2}\,s^{-1}}\right),$$

and there is no finite speed of propagation: a change at the surface is felt at
depth immediately in principle, and only in practice after the diffusion time of
Section 4.

## 2. The plane wave and the skin depth

For a field varying sinusoidally at angular frequency $\omega$,
$\mathbf{B}(z,t) = \mathrm{Re}\left[\mathbf{B}_0e^{i\omega t}e^{-\gamma z}\right]$
with $z$ downward, substitution gives $\gamma^{2} = i\omega\mu_0\sigma$, so

$$\gamma = \left(1+i\right)\sqrt{\frac{\omega\mu_0\sigma}{2}}
= \frac{1+i}{\delta}, \qquad
\boxed{\;\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}} = \sqrt{\frac{2\rho}{\omega\mu_0}}
= \sqrt{\frac{\rho T}{\pi\mu_0}}\;}$$

where $\rho = 1/\sigma$. The solution is

$$B(z,t) = B_0 e^{-z/\delta}\cos\left(\omega t - \frac{z}{\delta}\right).$$

Two statements of equal importance:

- the **amplitude** decays as $e^{-z/\delta}$, one decade per
  $\delta\ln 10 = 2.303\delta$;
- the **phase** lags by exactly $z/\delta$ radians — one radian per skin depth —
  so amplitude and phase carry related but independent information about the
  same structure.

### 2.1 Numerical values

Skin depth in kilometres, from the demonstration:

| Period (s) | $\rho = 1$ $\Omega$m | $\rho = 10$ | $\rho = 100$ | $\rho = 1000$ |
|---|---|---|---|---|
| 0.001 | 0.016 | 0.050 | 0.159 | 0.503 |
| 1 | 0.503 | 1.592 | 5.033 | 15.915 |
| 10 | 1.592 | 5.033 | 15.915 | 50.329 |
| 100 | 5.033 | 15.915 | 50.329 | 159.155 |
| 1000 | 15.915 | 50.329 | 159.155 | 503.292 |
| 86400 (1 day) | 147.937 | 467.818 | 1479.371 | 4678.181 |

Because $\delta \propto \sqrt{\rho T}$, one decade of period buys half a decade of
depth, and the dependence on resistivity is the same square root. *That square
root is the source of every non-uniqueness in this folder*: a factor of two in
depth can be traded for a factor of four in resistivity, and the measured
$\delta$ is unchanged.

## 3. An independent verification

The plane-wave solution is a derivation, and derivations have mistakes. The
demonstration solves the same physics as a **time-domain initial-boundary-value
problem**: the 1-D diffusion equation $B_t = D B_{zz}$ on $0 \le z \le 6\delta$
with $B(0,t) = \cos\omega t$, $B(6\delta,t)=0$, by Crank–Nicolson with
$301$ nodes ($\mathrm{d}z = 1006.6$ m, $\mathrm{d}t = 0.25$ s, and
$r = D\,\mathrm{d}t/(2\,\mathrm{d}z^{2}) = 9.82$). Transients are discarded over
five periods and the steady state is extracted by complex demodulation.

The analytic parameters: $\rho = 100\ \Omega$m, $T = 100$ s,
$\delta = 50.329$ km, $D = 7.96\times10^{7}$ m$^{2}$ s$^{-1}$.

| $z/\delta$ | Numeric amplitude | Analytic $e^{-z/\delta}$ | Numeric phase (rad) | Expected $-z/\delta$ |
|---|---|---|---|---|
| 0.50 | 0.60652 | 0.60653 | $-0.49999$ | $-0.50$ |
| 1.00 | 0.36787 | 0.36788 | $-0.99998$ | $-1.00$ |
| 2.00 | 0.13531 | 0.13534 | $-1.99972$ | $-2.00$ |
| 3.00 | 0.04966 | 0.04979 | $-3.00124$ | $-3.00$ |

Agreement is to a few tenths of a per cent in amplitude and to better than
$0.05\%$ in phase. The demonstration also shows something worth noticing: the
Crank–Nicolson parameter $r = 9.82$ is far above the value of $\frac12$ that an
explicit scheme would require for stability, and the solution is stable anyway —
that is what "unconditionally stable" means, and it is the reason implicit
schemes are used for diffusion problems.

## 4. Diffusion times

The skin depth answers "how deep at this period". The complementary scale answers
"how long to reach this depth". Dimensional analysis on
$u_t = D u_{zz}$ gives the only time available from $L$ and $D$:

$$\tau \sim \frac{L^{2}}{D} = \mu_0\sigma L^{2}, \qquad
\text{and the period that skins to } L \text{ is } T = \pi\mu_0\sigma L^{2}
\text{ (from } \delta = L\text{)}.$$

| $L$ (km) | $\sigma = 0.01$ S m$^{-1}$, $\tau$ (s) | $\sigma = 0.1$, $\tau$ (s) | $\sigma = 1$, $\tau$ (s) |
|---|---|---|---|
| 1 | $1.257\times10^{-2}$ | $1.257\times10^{-1}$ | $1.257$ |
| 10 | $1.257$ | $1.257\times10^{1}$ | $1.257\times10^{2}$ |
| 100 | $1.257\times10^{2}$ | $1.257\times10^{3}$ | $1.257\times10^{4}$ |
| 1000 | $1.257\times10^{4}$ | $1.257\times10^{5}$ | $1.257\times10^{6}$ |

*Worked example.* For $L = 100$ km and $\sigma = 0.01$ S m$^{-1}$ (a resistive
mantle), $\tau = 1.257\times10^{2}$ s. The period that skins to that depth is
$T = \pi\mu_0\sigma L^{2} = 3.948\times10^{2}$ s, about 6.6 minutes. So the
mantle below 100 km is reached by periods of minutes to hours, and the crust by
periods of seconds to minutes. **Period is the depth control; there is no other.**

Note that $\tau$ is a *scale*, not a threshold. The response varies smoothly with
period, and the transition between "sees the layer" and "sees what is beneath it"
spans a decade or more.

## 5. What is being measured, and what it is sensitive to

Since $\delta$ depends on $\sigma$, an induction measurement is a conductivity
measurement. Conductivity in rocks varies over eight decades, far more than any
elastic or density property, and it is controlled by the *connected* phases:

| Synthetic material | $\sigma$ min (S m$^{-1}$) | $\sigma$ max (S m$^{-1}$) | $\rho$ range ($\Omega$m) |
|---|---|---|---|
| dry crystalline rock | $1.0\times10^{-5}$ | $1.0\times10^{-3}$ | $10^{3}$–$10^{5}$ |
| wet crystalline rock | $1.0\times10^{-4}$ | $1.0\times10^{-2}$ | $10^{2}$–$10^{4}$ |
| sedimentary rock | $1.0\times10^{-3}$ | $1.0\times10^{-1}$ | $10^{1}$–$10^{3}$ |
| clay-rich soil | $1.0\times10^{-2}$ | 1.0 | $1$–$10^{2}$ |
| sea water | 3.0 | 4.0 | $0.25$–$0.33$ |
| graphite film (bulk) | $1.0\times10^{-2}$ | $1.0\times10^{-1}$ | $10$–$10^{2}$ |
| molten basalt | 1.0 | 10.0 | $0.1$–$1$ |

Dry silicates are insulators; almost all the conductivity comes from
electrolytes in pores, from melt, or from connected mineral phases such as
graphite and sulphides. That is the physical reason an EM survey can map fluids
and melt while a seismic survey maps rock fabric, and it is also why the
interpretation is ambiguous — the same conductivity can be produced by brine in
pores or by a little connected melt
([05 MT Interpretation](05-mt-interpretation.md)).

## 6. Diffusion versus wave propagation

Because the displacement current is negligible, there is no wave: the field
diffuses. The distinction has observable consequences:

- **Dispersion.** A diffusing field has no single speed; the phase velocity
  $v = \omega/k$ with $k = 1/\delta$ grows with frequency, $v = \omega\delta$, so
  a pulse spreads while it penetrates. A wave's speed is a material constant.
- **Attenuation.** A wave attenuates through a quality factor; a diffusing field
  attenuates through $\delta$, which is *defined* by the attenuation.
- **Geometry of the travelling field.** In a diffuser, amplitude and phase are
  tied together by the same $\delta$; in the plane-wave solution here they are
  exactly correlated, which is why a single measurement of amplitude gives a
  single number — and why using amplitude *and* phase is a consistency check
  rather than an additional constraint in a 1-D Earth.
- **Where the distinction matters.** At very high frequency or in very resistive
  rock the ratio $\omega\epsilon_0/\sigma$ grows, and at radio frequencies and in
  ice the full wave equation (with $\epsilon$) is required. Ground-penetrating
  radar is in that regime; the methods in this folder are not.

## 7. Assumptions and regime of validity

1. **Quasi-static.** $\omega\epsilon_0 \ll \sigma$; quantified in Section 1 for
   terrestrial conductivities and periods. It fails in very resistive rock at
   high frequency.
2. **Ohm's law with a scalar, frequency-independent $\sigma$.** Real rocks show
   induced polarisation and a mild frequency dependence; both are second-order at
   the periods used here.
3. **A plane wave source.** True only if the source field varies slowly compared
   with $\delta$; quantified in
   [06 Geomagnetic Depth Sounding](06-geomagnetic-depth-sounding.md).
4. **A 1-D Earth** for the plane-wave solution derived here. Lateral structure
   requires the full tensor treatment of
   [02 Magnetotellurics](02-magnetotellurics.md).
5. **$\mu = \mu_0$.** Rocks are essentially non-magnetic for this purpose; a few
   per cent of magnetite changes $\mu$ by less than a per cent in most cases.
6. **Diffusion, not propagation.** Stated above.

## 8. Python demonstration

`code/em_induction_basics_demo.py`:

1. tabulates the skin depth for six periods and four resistivities;
2. solves the diffusion equation by Crank–Nicolson on a $6\delta$ domain and
   compares amplitude and phase with $e^{-z/\delta}$;
3. tabulates diffusion times and the period that skins to a given depth;
4. prints a synthetic table of Earth-material conductivities.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_induction_basics_demo.py
```

Fixed seed, print-only, exits 0.

## 9. Exercises

[`exercises/01-em-induction-basics-exercises.md`](./exercises/01-em-induction-basics-exercises.md)
and
[`exercises/01-em-induction-basics-solutions.md`](./exercises/01-em-induction-basics-solutions.md).

## Mastery checkpoint

Without notes:

> **(a)** Compute the skin depth for $\rho = 25\ \Omega$m at $T = 4$ s.
> **(b)** At what period does $\rho = 400\ \Omega$m give the same skin depth?
> **(c)** A 1-D model has a conducting layer whose top is at 2 km. State the
> period at which the layer is first sensed, and the period at which the field
> beneath it is measured. **(d)** The amplitude at 2 km depth at that period is
> what fraction of the surface value? **(e)** State the approximation that makes
> this a diffusion problem rather than a wave problem, and compute the ratio
> $\omega\epsilon_0/\sigma$ for $\sigma = 0.01$ S m$^{-1}$ at $T=1$ s.

## Common pitfalls

1. **Treating $\delta$ as a sharp depth of investigation.** The sensitivity
   extends above and below it, and the response is smooth in period.
2. **Forgetting the square root.** A factor of four in resistivity is a factor of
   two in depth, and the data cannot separate them.
3. **Assuming a wave.** There is no propagation speed; the phase lag is
   $\pi$-per-two-skin-depths by construction.
4. **Using the displacement current "to be safe".** It changes the answer by
   $10^{-10}$ and adds a spurious wave.
5. **Quoting a depth without the period and resistivity it came from.**
6. **Confusing conductivity with lithology.** Conductivity responds to connected
   fluids and phases, not to rock type.

## Related modules

- [02 Magnetotellurics](02-magnetotellurics.md) — the measurement that uses this
  physics most directly.
- [06 Geomagnetic Depth Sounding](06-geomagnetic-depth-sounding.md) — the same
  diffusion at the periods that reach the mantle.
- [02-07-06 Electromagnetic Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md) —
  the physics prerequisite, in more generality.
- [05-04 Rock Physics](../../05-core-geophysics/04-rock-physics/README.md) —
  where rock conductivity comes from.
- [01-09-02 The Heat Equation](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md) —
  the same parabolic equation and its numerical treatment.
