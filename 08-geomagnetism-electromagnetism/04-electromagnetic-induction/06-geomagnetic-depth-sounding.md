---
id: 08-04-06
title: "Geomagnetic Depth Sounding and Long-Period Induction"
level: doctoral
prereqs: ["08-04-01", "08-01-04"]
tags: [electromagnetism, geomagnetism, geomagnetic-depth-sounding, induction-arrows, mantle-conductivity, c-response]
---

# Geomagnetic Depth Sounding and Long-Period Induction

Below a few hundred kilometres, magnetotellurics cannot help: the electric field
is too small to measure. What remains is the magnetic field itself, and the
method that uses it — **geomagnetic depth sounding** (GDS) — infers conductivity
from the way long-period variations penetrate the mantle. This lesson develops
the response function used at those periods, computes it for a synthetic mantle,
and then does what most treatments avoid: it quantifies how badly the method
depends on a source the Earth does not control.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** skin depths at the periods that probe the mantle and **state** the
   depth ranges they correspond to.
2. **Define** the Schmucker C-response, **derive** its half-space limits
   $\left|C\right| = \delta/\sqrt2$ and $\mathrm{Re}\,C = \delta/2$, and **verify**
   them numerically.
3. **Compute** C, apparent resistivity and phase for a layered mantle model and
   **interpret** the curve in terms of a conductive layer.
4. **Demonstrate** the conductance equivalence at mantle depths and **show** where
   it breaks.
5. **Define** the tipper, **compute** induction-arrow azimuths, and **state** why
   a non-zero tipper over a 1-D Earth indicates a source or structure problem.
6. **Derive** and **apply** the $k\delta$ criterion for the validity of the
   plane-wave source assumption, and **decide** for a given source width and
   period whether the assumption holds.
7. **State** which mantle conductivity questions long-period induction can and
   cannot answer.

## Prerequisites

- [08-04-01 Induction, Skin Depth and Diffusion](01-em-induction-basics.md) — the
  skin depth and the diffusion equation.
- [08-01-04 Secular Variation, Jerks and Core Dynamics](../01-earth-magnetic-field/04-secular-variation.md) —
  the long-period magnetic variations that provide the source.

## 1. The periods, and the depths they reach

Below $\left|\mathbf{E}\right|$ becomes unmeasurable the only usable signal is
the magnetic variation, driven by the magnetosphere and the ionosphere, with
periods from hours to months. The skin depth sets the depth sampled:

| Period | $\rho = 1\ \Omega$m | $\rho = 10$ | $\rho = 100$ |
|---|---|---|---|
| 1 hour | 30.2 km | 95.5 km | 302.0 km |
| 6 hours | 74.0 km | 233.9 km | 739.7 km |
| 1 day | 147.9 km | 467.8 km | 1479.4 km |
| 10 days | 467.8 km | 1479.4 km | 4678.2 km |
| 100 days | 1479.4 km | 4678.2 km | 14793.7 km |

A day reaches the upper mantle; a month reaches the transition zone. Note the
depth *is* the period, rescaled by $\sqrt{\rho}$: because the mantle's
resistivity is uncertain by a factor of ten, a factor of three in depth is
uncertain before any measurement is made. The response function below is the
measurement that resolves it.

## 2. The Schmucker C-response

Define the response by

$$Z(\omega) = i\omega\mu_0\,C(\omega) \qquad\Longleftrightarrow\qquad
C(\omega) = \frac{Z(\omega)}{i\omega\mu_0},$$

so $C$ has units of length. For a uniform half-space,

$$C = \frac{\sqrt{i\omega\mu_0\rho}}{i\omega\mu_0}
= \sqrt{\frac{\rho}{i\omega\mu_0}}
= \left(1-i\right)\frac{\delta}{2},$$

using $\delta = \sqrt{2\rho/(\omega\mu_0)}$. Hence the two exact limits quoted
above:

$$\left|C\right| = \frac{\delta}{\sqrt{2}}, \qquad \mathrm{Re}\,C = \frac{\delta}{2}.$$

$\mathrm{Re}\,C$ is read as the depth of the conductor: the depth at which the
in-phase part of the response originates. The imaginary part carries the
information about the gradient beneath it — a half-space gives
$\mathrm{Im}\,C = -\delta/2$, and any departure from that is structure.

**Numerical check.** The demonstration computes $\left|C\right|$ and
$\mathrm{Re}\,C$ from the layered recursion of
[02 Magnetotellurics](02-magnetotellurics.md) at $T = 1$ day for two half-space
resistivities:

| $\rho$ ($\Omega$m) | $\left|C\right|$ (km) | $\delta/\sqrt2$ (km) | $\mathrm{Re}\,C$ (km) | $\delta/2$ (km) |
|---|---|---|---|---|
| 10 | 330.797 | 330.797 | 233.909 | 233.909 |
| 100 | 1046.073 | 1046.073 | 739.685 | 739.685 |

Exact to all printed digits, at both resistivities.

## 3. A synthetic mantle model

Resistivity and thickness above the half-space:

| Layer | $\rho$ ($\Omega$m) | Depth range (km) |
|---|---|---|
| 1 | 1000 | 0–50 |
| 2 | 100 | 50–150 |
| 3 | 10 | 150–250 |
| 4 | 100 | 250–550 |
| half-space | 30 | below 550 |

The response:

| Period | $\left|C\right|$ (km) | $\mathrm{Re}\,C$ (km) | $\rho_a$ ($\Omega$m) | Phase (deg) |
|---|---|---|---|---|
| 0.04 d (1 h) | 179.3 | 168.4 | 70.51 | 69.91 |
| 1 d | 619.1 | 449.5 | 35.03 | 46.56 |
| 10 d | 1896.3 | 1376.1 | 32.86 | 46.53 |
| 100 d | 5820.2 | 4169.1 | 30.96 | 45.75 |

The conductive layer at 150–250 km holds the phase above $45^\circ$ through the
day-to-ten-day band, and holds $\rho_a$ near $30\ \Omega$m at long periods — close
to the $30\ \Omega$m half-space beneath it, which is the correct behaviour: at the
longest period the response is a conductance-weighted average of everything
above, dominated by the deepest layer whose skin depth has been exceeded.

At 1 hour the phase is $69.9^\circ$, far above $45^\circ$: at that period the
current is concentrated in the conductive layer, and the conductivity is
increasing with depth.

## 4. What long periods constrain, and where the equivalence breaks

The same conductance equivalence as in MT applies, with one difference: at mantle
depths the layers are *thick* compared with the skin depth far more often, and
the equivalence breaks sooner. Two models with the same asthenospheric
conductance of 10000 S:

| Layer $\rho$ ($\Omega$m) | Thickness (km) | $S$ (S) | max $\left|\Delta\rho_a\right|$ (%) | max $\left|\Delta\phi\right|$ (deg) |
|---|---|---|---|---|
| 10 | 100 | 10000 | 0.00 (reference) | 0.00 |
| 20 | 200 | 10000 | 21.27 | 3.94 |
| 5 | 50 | 10000 | 13.67 | 1.83 |

The discrepancies are tens of per cent — far larger than in the crustal case of
[05 MT Interpretation](05-mt-interpretation.md) — because 100–200 km layers are
comparable to the skin depth at the periods that see them. The practical
consequence is the opposite of the crustal case: at mantle depths the *thickness*
is better constrained and the conductance is not the whole story, *provided* the
period band extends to the periods where the equivalence breaks.

## 5. The tipper and induction arrows

Over a 1-D Earth the tipper is zero at every period, because a uniform source
produces no vertical field. A measured non-zero tipper therefore indicates
**lateral structure**, and its direction indicates the orientation of the
contrast. For a synthetic 2-D contrast at strike $40^\circ$:

| $\left|T\right|$ | $T_{zx}$ | $T_{zy}$ | Arrow azimuth (deg) | Angle from strike (deg) |
|---|---|---|---|---|
| 0.15 | $-0.0964$ | $+0.1149$ | 130.0 | 90.0 |
| 0.35 | $-0.2250$ | $+0.2681$ | 130.0 | 90.0 |
| 0.60 | $-0.3857$ | $+0.4596$ | 130.0 | 90.0 |

The arrow azimuth is exactly $90^\circ$ from the strike and the magnitude scales
independently: the tipper gives a *direction* and an *amplitude* at each period,
but no depth. Two cautions, both of which the GDS literature takes seriously:

- **A non-zero tipper over a 1-D Earth means the source is not uniform.** A
  spatially varying source (an electrojet, a polar current system) produces a
  vertical field even over a layered Earth, and a naive interpretation would
  place a spurious conductor. The $k\delta$ test below is how this is bounded.
- **A zero tipper does not mean 1-D.** A structure aligned with the array, or one
  whose induction arrows cancel, can give a null tipper.

## 6. When the plane-wave source is not good enough

Every response function above assumes a **spatially uniform source**. Real
long-period sources have horizontal scales of a few thousand kilometres, and the
correctness of the assumption is controlled by the dimensionless product of the
source's horizontal wavenumber and the skin depth:

$$k = \frac{2\pi}{L_{\text{source}}}, \qquad
\text{plane wave valid when } k\delta \ll 1 .$$

With $\delta$ computed for a $10\ \Omega$m mantle:

| Source width (km) | Period | $\delta$ (km) | $k\delta$ |
|---|---|---|---|
| 2000 | 1 day | 467.8 | 1.47 |
| 2000 | 10 days | 1479.4 | 4.65 |
| 5000 | 1 day | 467.8 | 0.59 |
| 5000 | 10 days | 1479.4 | 1.86 |
| 20000 | 1 day | 467.8 | 0.15 |
| 20000 | 10 days | 1479.4 | 0.46 |

A 2000 km wide electrojet at a 1-day period gives $k\delta = 1.47$: the
assumption is **not** satisfied, and the depth scale derived from that response
is not the plane-wave skin depth. Even a 20000 km source fails at 10 days. The
resolution of this difficulty is the research frontier of the subject:

1. **Restrict the periods** to those where $k\delta$ is small, which restricts the
   depths that can be claimed.
2. **Model the source** — use a magnetospheric current system as the known input
   instead of assuming uniformity.
3. **Use the tipper as a source diagnostic**, since a non-zero tipper over
   otherwise-layered structure is the signature of a non-uniform source.

The honest statement is that the deep-mantle conductivity models which exist are
limited as much by the source geometry as by the data, and that any depth scale
reported from a long-period response is conditional on the source model.

## 7. What GDS can and cannot answer

**Can:**

- the presence and depth range of a high-conductivity layer in the upper mantle
  or transition zone, expressed as a conductance with a depth range;
- lateral contrasts, through the tipper and induction arrows, in regions where
  the source is well understood;
- time changes in conductivity at long periods, at the level set by the
  repeatability of the response estimate.

**Cannot, without independent information:**

- the mechanism of a conductor: melt fraction, water content or graphite
  ([05 MT Interpretation](05-mt-interpretation.md));
- a depth scale at periods where the source is not a plane wave;
- absolute resistivity of a thick layer, as distinct from its conductance; and
- anything at depths the periods do not reach, which is most of the lower mantle.

## 8. Assumptions and regime of validity

1. **A uniform source.** Quantified in Section 6; the dominant limitation.
2. **Quasi-static, $\mu = \mu_0$, scalar isotropic $\sigma$.** As in
   [01](01-em-induction-basics.md).
3. **1-D structure for the response functions**, with lateral structure inferred
   from the tipper rather than from the impedance.
4. **The source spectrum is known or irrelevant.** The 1-D response is
   source-independent in the plane-wave limit; at long periods it is not.
5. **The external and internal parts of the variation can be separated.**
   Separation of the observed field into its source and induced parts is the
   mathematical step that makes GDS possible, and it requires array data or a
   source model.
6. **No ocean or coastline effect.** The oceans are excellent conductors; a
   station near a coast measures the ocean as much as the mantle. This is the
   classic "coast effect" and it is why continental interior sites are preferred
   for mantle work.

## 9. Python demonstration

`code/geomagnetic_depth_sounding_demo.py`:

1. tabulates skin depths from one hour to a hundred days;
2. verifies $\left|C\right| = \delta/\sqrt2$ and $\mathrm{Re}\,C = \delta/2$ on a
   half-space at two resistivities;
3. computes C, $\rho_a$ and phase for a synthetic mantle model;
4. tests the conductance equivalence for three asthenospheric layers;
5. computes induction-arrow azimuths for four strikes;
6. computes $k\delta$ for three source widths at two periods.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geomagnetic_depth_sounding_demo.py
```

Fixed seed, print-only, exits 0.

## 10. Exercises

[`exercises/06-geomagnetic-depth-sounding-exercises.md`](./exercises/06-geomagnetic-depth-sounding-exercises.md)
and
[`exercises/06-geomagnetic-depth-sounding-solutions.md`](./exercises/06-geomagnetic-depth-sounding-solutions.md).

## Mastery checkpoint

Without notes:

> A **synthetic** station records a response with $\left|C\right| = 900$ km and
> $\mathrm{Re}\,C = 640$ km at a 2-day period. **(a)** Compute the apparent
> resistivity and state whether the structure looks like a half-space at that
> period. **(b)** Compute the resistivity implied if the response were a
> half-space, and the depth it would correspond to. **(c)** A nearby station gives
> $\left|C\right|$ twice as large at the same period: state two explanations and
> how you would distinguish them. **(d)** The source is a 3000 km electrojet;
> compute $k\delta$ and decide whether you may report a depth. **(e)** State one
> mantle question this sounding can answer and one it cannot.

## Common pitfalls

1. **Reporting a mantle depth without stating the source model.** The $k\delta$
   criterion is the quantitative statement of the problem.
2. **Reading $\left|C\right|$ as a depth.** It is $\delta/\sqrt2$; the depth scale
   is $\mathrm{Re}\,C$ for a half-space, and neither is a sharp boundary.
3. **Treating a non-zero tipper as proof of a conductor.** It may be the source.
4. **Ignoring the coast effect.** Oceans conduct, and the effect is large near
   coastlines.
5. **Assuming the mantle's resistivity is known to a factor of two.** It is
   uncertain by a decade in places, and the depth scale inherits the square root.
6. **Extrapolating conductivity to temperature or melt without a mechanism.**
   The same trap as in [05](05-mt-interpretation.md).

## Related modules

- [01 Induction, Skin Depth and Diffusion](01-em-induction-basics.md) — the physics
  of the response functions.
- [02 Magnetotellurics](02-magnetotellurics.md) — the tensor and the recursion
  reused here.
- [05 MT Interpretation](05-mt-interpretation.md) — interpreting a conductor at
  any depth.
- [01 The Earth's Magnetic Field](../01-earth-magnetic-field/README.md) — the
  source variations and their spectra.
- [12 Global Geophysics and the Interior](../../12-global-geophysics-interior/README.md) —
  the mantle questions these soundings address.
