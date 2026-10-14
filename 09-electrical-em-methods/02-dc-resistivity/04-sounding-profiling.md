---
id: 09-02-04
title: "Vertical Electrical Sounding vs Profiling"
level: advanced
prereqs: ["09-02-02", "09-02-03"]
tags: [electrical-methods, sounding, profiling, vés, lateral-resolution, smearing]
---

# Vertical Electrical Sounding vs Profiling

Two surveys can be made with the same electrodes and the same instrument, and
they answer different questions. A **sounding** varies the spacing at a fixed
centre and resolves vertical structure; a **profile** fixes the spacing and moves
the array, resolving lateral structure — at a resolution set by the array's
footprint. This lesson computes both, quantifies the smearing a profile cannot
avoid, and states the failure mode that catches most beginners: reading a lateral
change as a depth change.

**All models and data in this module are SYNTHETIC.** The models, the dip and the
noise level are chosen teaching values; no field data are used. The profiling
experiment uses the *locally one-dimensional* approximation, which is stated
where it is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** a sounding over a four-layer model and relate each feature of the
   curve to a layer.
2. **Distinguish** detection from resolution with numbers: show that a thin
   aquifer is detected long before its thickness is measured.
3. **Compute** a profile across a dipping contact in the locally 1-D
   approximation and explain what the approximation does and does not contain.
4. **Compute** the lateral footprint of an array from the analytic kernel and
   the 10–90% edge-smearing width it implies.
5. **Convolve** a step change with the footprint and measure the resulting
   smearing.
6. **State** when a lateral change and a depth change are indistinguishable, and
   what additional data would separate them.
7. **Choose** between sounding and profiling for a stated target.

## Prerequisites

- [09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](02-electrode-arrays.md) —
  sensitivity, DOI and signal.
- [09-02-03 Apparent Resistivity and Geometric Factors](03-apparent-resistivity.md) —
  sounding curves and equivalence.

## 1. A sounding over an aquifer model

SYNTHETIC teaching model: dry sand ($200\ \Omega\,\mathrm{m}$, 4 m) over an
aquifer ($30\ \Omega\,\mathrm{m}$, 6 m) over a clay aquitard
($5\ \Omega\,\mathrm{m}$, 8 m) over bedrock ($500\ \Omega\,\mathrm{m}$). The demo
prints:

| $a$ (m) | 1 | 3 | 5 | 8 | 12 | 20 | 30 | 50 | 80 | 120 |
|---|---|---|---|---|---|---|---|---|---|---|
| $\rho_a$ ($\Omega\,\mathrm{m}$) | 199.7 | 195.5 | 181.6 | 156.0 | 129.1 | 108.2 | 101.3 | 101.8 | 106.9 | 115.0 |
| $\Delta V$ (mV) | — | — | — | — | 269.8 | 218.0 | 170.6 | 128.7 | 102.6 | 84.4 |
| 2% noise on $\rho_a$ ($\Omega\,\mathrm{m}$) | 4.0 | 3.9 | 3.6 | 3.1 | 2.6 | 2.2 | 2.0 | 2.0 | 2.1 | 2.3 |

The curve falls into the aquifer minimum, rises through the clay, and climbs
toward bedrock; each *feature* corresponds to a layer, but the correspondence is
blurred because every spacing averages several layers. The demo prints the
closest $\rho_a$ value to each layer resistivity: the top layer is approached to
199.7 $\Omega\,\mathrm{m}$ at $a = 1$ m, the aquifer to 108.2 at 20 m, the clay
to 101.3 at 30 m, and the bedrock is never approached within the measured range —
$\rho_a$ reaches only 115.0 at $a = 120$ m against a bedrock value of 500. **A
thick resistive basement under a conductive overburden is poorly constrained by
any sounding**, which is the most common real-world version of non-uniqueness in
this method.

## 2. Detection is not resolution

Replace the 6 m aquifer by layers of the same resistivity but different
thickness, and read the sounding at $a = 12$ m:

| $h_\text{aquifer}$ (m) | 2 | 4 | 6 | 8 | 12 |
|---|---|---|---|---|---|
| $\rho_a$ at $a = 12$ m ($\Omega\,\mathrm{m}$) | 113.32 | 115.68 | 117.86 | 119.55 | 121.59 |
| difference from 6 m | $-3.85\%$ | $-1.86\%$ | 0 | $+1.43\%$ | $+3.16\%$ |

A 2 m aquifer differs from a 4 m one by $1.99\%$ in $\rho_a$ at this spacing —
**the same order as the 2% noise floor**. The aquifer is *detected* (the curve
drops well below the top layer for every thickness), but its thickness is
resolved only to a factor of two or so. This is the single most useful sentence
in the lesson: *detection requires the anomaly to be larger than the noise;
resolution requires the anomaly's dependence on the parameter to be larger than
the noise, which is a much stronger requirement.* The same distinction appears
in [09-02-08](08-ert-applications.md) for monitoring.

## 3. A profile across a dipping contact

SYNTHETIC model: two layers, $\rho_1 = 200\ \Omega\,\mathrm{m}$ over
$\rho_2 = 20\ \Omega\,\mathrm{m}$, with the interface at
$z(x) = 4\ \mathrm{m} + 0.20\,(x - 100\ \mathrm{m})$, so it outcrops at
$x = 80$ m. The demo uses the **locally 1-D approximation**: at each position it
computes the layered response for the local thickness $z(x)$. This is *not* an
exact two-dimensional solution — a true 2-D solution requires a numerical
solver — and it deliberately omits lateral current channelling, which for a
strong contrast is a first-order effect. What it does show correctly is where
the apparent edge sits.

| $x$ (m) | 80 | 85 | 90 | 95 | 100 | 105 | 110 | 115 | 120 |
|---|---|---|---|---|---|---|---|---|---|
| $z(x)$ (m) | 0.0 | 1.0 | 2.0 | 3.0 | 4.0 | 5.0 | 6.0 | 7.0 | 8.0 |
| $\rho_a$, $a = 2$ m | 200.0 | 133.9 | 173.4 | 188.6 | 194.4 | 196.9 | 198.1 | 198.8 | 199.2 |
| $\rho_a$, $a = 5$ m | 200.0 | 111.3 | 123.7 | 144.1 | 161.4 | 173.4 | 181.4 | 186.7 | 190.3 |
| $\rho_a$, $a = 10$ m | 200.0 | 110.2 | 111.3 | 115.5 | 123.7 | 133.9 | 144.1 | 153.4 | 161.4 |

Three observations. At $x = 80$ m, where the conductor reaches the surface, every
spacing reads 200 $\Omega\,\mathrm{m}$ — the locally 1-D model has a zero-thickness
first layer and therefore reports the half-space value, a reminder that the
approximation is degenerate at the outcrop. Away from it, the **long spacing
shows the larger drop at every position**, because it samples deeper where the
conductor is closer; what it pays is a wider footprint. And near the edge the
short spacing recovers towards 200 $\Omega\,\mathrm{m}$ faster, as it samples
shallow resistive material.

## 4. The lateral footprint, and the smearing it causes

Integrate the analytic kernel of [09-02-02](02-electrode-arrays.md) over the
direction across the line and over depth to get the **footprint** $h(x)$ of a
Wenner array with $a = 5$ m (normalised so that $\int h\,\mathrm{d}x = 1$). The
demo first checks the raw normalisation: the integral over the half-space is
$1.2268$ and the value required by the kernel constant is $V/(2\rho)\times
8\pi^{2}/I = 1.2566$ — agreement to 2.4%, the difference being the truncation of
the numerical integration ranges. Selected values:

| $x$ (m) | $-40$ | $-8$ | $-4$ | 0 | 4 | 8 | 40 |
|---|---|---|---|---|---|---|---|
| $h(x)$ ($\mathrm{m^{-1}}$) | $5.6\times10^{-5}$ | 0.09590 | $-0.01450$ | 0.10243 | $-0.01450$ | 0.09590 | $5.6\times10^{-5}$ |

The footprint is symmetric, peaked under the array, and — importantly — **has
negative sidelobes** at $x = \pm4$ m: there are places where *adding*
resistivity to the ground *lowers* the apparent resistivity. Convolving a step
change (200 $\to$ 20 $\Omega\,\mathrm{m}$ at $x = 0$) with this footprint gives:

| $x$ (m) | $-40$ | $-8$ | $-4$ | 0 | 4 | 8 | 16 | 20 | 40 |
|---|---|---|---|---|---|---|---|---|---|
| true $\rho$ | 200 | 200 | 200 | 20 | 20 | 20 | 20 | 20 | 20 |
| smoothed $\rho$ | 199.99 | 159.67 | 166.32 | 100.78 | 56.29 | 43.06 | 22.02 | 20.94 | 20.00 |

The demo measures the 10–90% width of the smoothed step as **18.2 m**, against a
zero-width true step, for an array whose aperture is $3a = 15$ m. So a lateral
contact is smeared over a distance of the order of the array aperture. Two
consequences: (i) a fine lateral target needs a small footprint, which needs
short spacings, which cost depth; (ii) **no processing recovers the wavelengths
the array never measured** — deconvolution can sharpen a little, but the
footprint has zeros and the information is genuinely absent.

## 5. Worked example: the classic confusion

A profile at $a = 10$ m reads $\rho_a = 150\ \Omega\,\mathrm{m}$ at $x = 0$ and
$95\ \Omega\,\mathrm{m}$ at $x = 30$ m. Two explanations, both consistent with
the numbers:

1. **Lateral:** the array crossed into a more conductive unit.
2. **Vertical (locally 1-D):** the same unit became thicker, or the water table
   rose.

From Section 3 the drop at $a = 10$ m across the dip is $200\to123.7\
\Omega\,\mathrm{m}$ over 20 m of traverse, comparable with the observed change.
The discriminator is to **repeat the profile at two or three spacings**: a
lateral change appears at *all* spacings with roughly similar amplitude, whereas
a depth change shifts the response strongly between spacings (compare the $a = 2$
and $a = 10$ rows of Section 3, which differ by a factor 3). A single-spacing
profile cannot make the distinction, and the demo's Section 5 table prints that
conclusion with the numbers.

## 6. Regime of validity

1. **Locally 1-D profiling** is an approximation. It is exact only for
   horizontally layered ground; for a strong lateral contrast, two- and
   three-dimensional current channelling changes amplitudes (often by tens of per
   cent) while leaving the *position* of an edge approximately right.
2. **Sounding assumes lateral uniformity** under the array. In folded or
   faulted terrain this is the dominant error.
3. **The footprint is computed for a homogeneous half-space**; a conductive
   overburden broadens it further.
4. **Detectability is limited by $\Delta V \propto 1/a$**: the deep information a
   long spacing would provide may simply be below the noise.
5. **Equivalence limits both surveys.** A sounding cannot separate $h$ from
   $\rho$ of a thin layer ([09-02-03](03-apparent-resistivity.md)); a profile
   cannot separate lateral from vertical change (Section 5).

## 7. Mastery checkpoint

1. From the sounding table, state which spacing you would choose to detect the
   6 m aquifer and which to estimate its resistivity, and why they differ.
2. Explain why the two 2 m and 4 m aquifer cases differ by only 2% while the
   6 m and 12 m cases differ by 5%.
3. Compute the footprint's 10–90% width for a Wenner array with $a = 10$ m,
   given that it scales with the aperture, and state the implied lateral
   resolution at 10 m depth.
4. Give a three-spacing field procedure that distinguishes the two
   explanations of Section 5, and state the test you would apply.

## 8. Common pitfalls

1. **Reading a single-spacing profile as a depth section.** It is a lateral
   average at one approximate depth.
2. **Confusing detection with resolution.** Section 2 quantifies the gap.
3. **Expecting a sounding to see a resistive basement under a conductor.**
   Section 1 shows it does not.
4. **Ignoring the negative sidelobes.** An edge can overshoot before it settles.
5. **Using a locally 1-D model to predict amplitudes** next to a strong
   contrast; it will be wrong by tens of per cent even when the edge position is
   right.

## 9. Related modules

- [09-02-05 ERT Acquisition and Design](05-ert-tomography.md) — many spacings and
  many positions at once.
- [09-02-08 ERT Applications](08-ert-applications.md).
- [09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](02-electrode-arrays.md).
- [09-02-03 Apparent Resistivity and Geometric Factors](03-apparent-resistivity.md).
- [18-01-04 Discretisation, Parameterisation and Model Choice](../../18-inverse-problems/01-inverse-problem-foundations/04-discretisation-reality.md).

## 10. Demonstration and exercises

- [`code/sounding_profiling_demo.py`](code/sounding_profiling_demo.py) prints the
  four-layer sounding, the thickness-resolution table, the dipping-contact
  profiles, the footprint and the smeared step.
- [Exercises](exercises/04-sounding-profiling-exercises.md) and
  [worked solutions](exercises/04-sounding-profiling-solutions.md).
