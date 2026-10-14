---
id: 09-02-05
title: "Electrical Resistivity Tomography (ERT) Acquisition and Design"
level: graduate
prereqs: ["09-02-03", "09-02-04"]
tags: [electrical-methods, ert, acquisition-design, depth-of-investigation, coverage, scaling]
---

# Electrical Resistivity Tomography (ERT) Acquisition and Design

A multi-electrode ERT survey is not "a lot of soundings". It is a designed set of
four-electrode measurements whose sensitivities must overlap where the target is
and not overlap where it is not. This lesson turns design into a quantitative
exercise: how many measurements, which separations, what signal, what depth, and
what lateral smearing. The key scaling result — that DC sensitivity depends only
on $z/a$ — makes the design calculus cheap, and the demo verifies it to under a
millimetre.

**All models and data in this module are SYNTHETIC.** The electrode layout, the
resistivities, the current and the noise floor are chosen teaching values; no
instrument, site or data set is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Count** the measurements a dipole-dipole ERT line delivers and relate the
   count to the electrode number and the separation $n$.
2. **Explain and verify** the scaling $F(z; a) = F(z/a; 1)$, i.e. that DC
   sensitivity depends only on $z/a$.
3. **Compute** the depth of investigation of a range of separations from a
   single scaled computation.
4. **Compute** the usable range of $n$ for a stated current, noise floor and
   ground resistivity.
5. **Compute** a depth-coverage curve for a whole survey and read a coverage
   depth from it.
6. **Compute** the lateral footprint width at the depth of investigation and
   state the resolution it implies.
7. **Design** an array for a stated target depth and size, and state the cost in
   signal, electrodes and footprint.

## Prerequisites

- [09-02-03 Apparent Resistivity and Geometric Factors](03-apparent-resistivity.md) —
  geometric factors and $\Delta V = \rho_a I/k$.
- [09-02-04 Vertical Electrical Sounding vs Profiling](04-sounding-profiling.md) —
  detection versus resolution, and the footprint idea.

## 1. Geometry and count

SYNTHETIC line: 48 electrodes at 2.0 m spacing, so the line is 94 m long. For
dipole-dipole with separation $n$ the four electrodes occupy 4 positions of
index spacing, giving an aperture $(n+2)a$:

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| measurements | 44 | 43 | 42 | 41 | 40 | 39 |
| aperture (m) | 10.0 | 12.0 | 14.0 | 16.0 | 18.0 | 20.0 |

Total for $n = 1..6$: **249 measurements**. The count is nearly independent of
$n$: adding depth to a fixed electrode layout costs almost no extra data — it
costs signal. (For a real survey the count also grows with the number of
electrode *positions*, which is why a 96-electrode cable has four times the
measurements of a 48-electrode one.)

## 2. Signal, depth and the scaling law

The demo measures $F(z)$ (the cumulative sensitivity of
[09-02-02](02-electrode-arrays.md)) with a unit spacing of 1 m and rescales. The
justification is exact: the DC problem is scale-invariant, since
$\nabla\cdot(\sigma\nabla V) = 0$ has no intrinsic length, so an array scaled by
$a$ has the same normalised sensitivity in units of $z/a$. The demo verifies it
for $n = 3$ at $a = 2$ m: DOI computed directly $= 2.002$ m against
$a\times(\text{DOI}/a) = 2.003$ m, a difference of **0.46 mm** — i.e. the
quadrature and discretisation limit.

| $n$ | $|k|/a$ | $\Delta V$ (mV) at $\rho = 100\ \Omega\,\mathrm{m}$, $I = 0.1$ A | DOI$/a$ | DOI at $a = 2$ m (m) | peak depth$/a$ |
|---|---|---|---|---|---|
| 1 | 18.8496 | 265.2582 | 0.456 | 0.91 | 0.300 |
| 2 | 75.3982 | 66.3146 | 0.735 | 1.47 | 0.550 |
| 3 | 188.4956 | 26.5258 | 1.001 | 2.00 | 0.800 |
| 4 | 376.9911 | 13.2629 | 1.264 | 2.53 | 1.050 |
| 5 | 659.7345 | 7.5788 | 1.524 | 3.05 | 1.050 |
| 6 | 1055.5751 | 4.7368 | 1.787 | 3.57 | 1.300 |

The DOI grows roughly linearly with $n$ (log-log slope printed as 0.845 over
$n = 3..6$), while $\Delta V$ falls as $n^{-2.25}$ over $n = 1..6$ — an
empirical slope measured by the demo, close to the asymptotic $n^{-3}$, because
the near-separations are not yet asymptotic. **Depth is linear in the design
variable; signal is cubic.** That is the exchange rate of ERT.

## 3. The usable range of $n$

With a SYNTHETIC noise floor of 0.5 mV and a requirement that the half-space
$\Delta V$ exceed ten times it (1% relative precision):

| $n$ | $\Delta V$ at $\rho = 100$ (mV) | usable? | $\Delta V$ at $\rho = 1000$ (mV) | usable? |
|---|---|---|---|---|
| 1 | 265.2582 | yes | 2652.5824 | yes |
| 3 | 26.5258 | yes | 265.2582 | yes |
| 5 | 7.5788 | yes | 75.7881 | yes |
| 6 | 4.7368 | **no** | 47.3675 | yes |
| 8 | 2.2105 | no | 22.1049 | yes |

The resistive ground still passes at $n = 8$; the conductive ground fails at
$n = 6$. Since $\Delta V = \rho I/k$, the ground resistivity is part of the
signal budget: **what an array can reach depends on the ground it stands on**.
The practical consequence is that a conductive site needs more current,
more stacking, or both — and that a design evaluated only for
$\rho = 100\ \Omega\,\mathrm{m}$ will be over-optimistic in a clay.

## 4. Depth coverage of a survey

Summing $|\mathrm{d}F/\mathrm{d}z|$ over the measurements whose centre lies
within 20 m of the line centre gives the survey's depth-coverage curve:

| design | measurements | median coverage depth | 90% coverage depth |
|---|---|---|---|
| shallow, $n = 1..2$ | 41 | 1.1 m | 2.5 m |
| deep, $n = 1..6$ | 123 | 2.0 m | 5.3 m |

Adding long-offset measurements triples the count and roughly triples the 90%
coverage depth (2.5 → 5.3 m). But the *median* moves little (1.1 → 2.0 m),
because the short offsets dominate the sensitivity mass: **the survey is
overwhelmingly a shallow measurement with a thin deep tail**, and if the target
is deep, most of the data are wasted on the overburden. Design means choosing
which part of the sensitivity budget to spend where.

## 5. Lateral resolution at depth

From the analytic kernel of [09-02-02](02-electrode-arrays.md), the footprint
width at a given depth (10–90% of the cumulative $|$kernel$|$):

| $n$ | depth $z$ (m) | 10–90% width (m) | ratio $z/\text{width}$ |
|---|---|---|---|
| 1 | 0.91 | 3.95 | 0.23 |
| 3 | 2.00 | 8.60 | 0.23 |
| 6 | 3.57 | 15.03 | 0.24 |

The footprint widens in proportion to depth: $z/\text{width}$ is constant at
about 0.23. So the statement "resolution trades with depth, one for one" is not
a slogan here: it is a slope measured on the models. Note also that the width is
*always larger than the depth*: at 3.57 m, the array averages over 15 m
laterally. **ERT is a blunt lateral instrument at depth**, and that is a
property of the physics, not of the inversion.

## 6. Worked example: design for a 10 m target

Target: a body of size ~10 m at 10 m depth, in $\rho = 100\
\Omega\,\mathrm{m}$ ground, with a 0.5 mV floor and $I = 0.1$ A.

1. Required spacing: $a = d/(\text{DOI}/a)$ with the deepest usable $n$. From
   Section 2, $\text{DOI}/a = 1.787$ for $n = 6$, so $a = 10/1.787 = 5.6$ m.
2. Aperture: $(n+2)a = 8\times5.6 = 44.8$ m.
3. Footprint at the target: $a\times(\text{width}/a) = 5.6\times2.51 \approx
   14$ m (the table's ratio 15.03/6.0 = 2.51), comparable with the 10 m target:
   **detectable but not well resolved**.
4. Signal: with $a = 5.6$ m the geometric factor scales with $a$, so
   $|k| = 1055.58\times5.6 = 5911$ m and $\Delta V = 100\times0.1/5911 =
   1.69\ \mathrm{mV}$ — 3.4 times the noise floor. Stacking by 16 gives a
   factor 4: usable, but not comfortable.
5. Electrodes for a 100 m line: $\lceil 100/5.6\rceil + 1 + 8 \approx 27$.

The honest summary: to see 10 m in this ground you need a 5.6 m electrode
spacing, a 45 m aperture, a very quiet receiver, and you will still only *detect*
the target. Doubling the current or using a 2 A transmitter is what makes the
difference, and that is an engineering decision the physics has already
dictated.

## 7. Regime of validity

1. **Homogeneous reference model** for the sensitivity profiles and scaling.
   Scaling holds exactly for any *scaled* model, so it also holds for a layered
   model provided all depths scale — it is the design tool, not the survey
   answer.
2. **The DOI uses $|s|$.** Arrays with sign changes have a Definition-dependent
   DOI; the number must always be quoted with its convention.
3. **Three-dimensional effects** are ignored: real ERT lines bend, electrodes sit
   at different elevations, and topography changes $k$.
4. **The footprint uses the linearised kernel**, valid for small contrasts.
5. **Noise is treated as a floor on $\Delta V$.** Real noise is
   contact-impedance dependent and often much larger on a dry, resistive
   electrode; see [09-07 EM Data Processing, QC and Uncertainty](../07-em-data-processing-and-qc/README.md).

## 8. Mastery checkpoint

1. A line has 64 electrodes at 3 m spacing. Count the dipole-dipole measurements
   for $n = 1..6$.
2. Using the scaling law, compute the DOI of $n = 4$ for $a = 4$ m, and verify
   against the table.
3. A conductive site has $\rho = 20\ \Omega\,\mathrm{m}$. Which $n$ values are
   usable with $I = 0.1$ A and a 0.5 mV floor? What changes if the transmitter
   reaches 1 A?
4. For a target of 5 m size at 15 m depth, decide whether this line (48
   electrodes, 2 m spacing) can help at all, and justify your answer with the
   footprint and signal numbers.

## 9. Common pitfalls

1. **Treating more measurements as automatically better.** The sensitivity mass
   is what matters, and most of it is shallow.
2. **Forgetting the $n^{-3}$ signal cost.** The deepest separations may be
   below the noise.
3. **Quoting a DOI without a convention.** With the surface step in, half the
   sensitivity is at the surface.
4. **Assuming the inversion creates resolution.** It cannot recover what the
   footprint removed.
5. **Designing for one resistivity.** A conductive ground changes which
   measurements are usable.

## 10. Related modules

- [09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](02-electrode-arrays.md).
- [09-02-04 Vertical Electrical Sounding vs Profiling](04-sounding-profiling.md).
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](07-resistivity-inversion.md) —
  what the data can and cannot support once acquired.
- [09-02-08 ERT Applications](08-ert-applications.md) — the same design questions
  for aquifers, contamination, landslides and archaeology.
- [09-07 EM Data Processing, QC and Uncertainty](../07-em-data-processing-and-qc/README.md).

## 11. Demonstration and exercises

- [`code/ert_tomography_demo.py`](code/ert_tomography_demo.py) prints the
  geometry and count, the signal/DOI table with the scaling verification, the
  usable-$n$ table, the coverage curves, the footprint widths and the design
  table.
- [Exercises](exercises/05-ert-tomography-exercises.md) and
  [worked solutions](exercises/05-ert-tomography-solutions.md).
