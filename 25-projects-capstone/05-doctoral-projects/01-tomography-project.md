---
id: 25-05-01
title: "Project: Local Earthquake Tomography with Resolution Tests"
level: doctoral
prereqs: ["06-06-02", "06-06-03", "18-03-02", "25-04-04"]
estimated_minutes: 240
tags: [projects, seismology, tomography, inverse-problems, resolution, doctoral]
---

# Project: Local Earthquake Tomography with Resolution Tests

## Learning objectives

By the end of this project you will be able to:

1. **Assemble** a ray-path matrix for a local-earthquake travel-time tomography
   problem and **state** the forward relation exactly.
2. **Invert** the travel times with damped least squares and **choose** the damping
   from the data rather than from taste, using the discrepancy principle.
3. **Demonstrate** that a better data fit can correspond to a useless model.
4. **Quantify** resolution with three independent diagnostics — amplitude recovery,
   a checkerboard test and point-spread functions — and **report** a resolution
   length rather than a cell size.
5. **Distinguish** what the data determine (a blurred, amplitude-damped image) from
   what the damping determines (the level of blur).
6. **Design** an experiment that separates source location from velocity, which is
   the doctoral-level difficulty of this problem.
7. **Write** the resolution section of a tomography paper, with the phrases that
   are required and the claims that are forbidden.

All data in this project are **SYNTHETIC**: straight rays are traced through a
5-cell-thick model in [`code/tomography_demo.py`](./code/tomography_demo.py). For the
project itself, earthquake arrival times and station metadata are available from the
IRIS/EarthScope FDSN services at
<https://service.iris.edu/fdsnws/dataselect/1/query> and
<https://service.iris.edu/fdsnws/station/1/query>.

## Prerequisites

- [06-06-02 Travel-Time Tomography](../../06-seismology/06-seismic-tomography/02-travel-time-tomography.md) —
  the forward operator built here.
- [06-06-03 Resolution and Null Space](../../06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) —
  the theory behind the PSF test.
- [18-03-02 Tikhonov Regularisation and Damping](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  where the objective function comes from.
- [25-04-04 Project: Earthquake Catalogue Analysis](../04-graduate-projects/04-earthquake-catalog-analysis.md) —
  the catalogue that supplies the arrival times.

## 1. The question

*Which features of a local-earthquake velocity image are demanded by the data, and
which are demanded by the damping?*

A tomography image is one of the few published geophysical products where the
resolution is usually more informative than the values. The demonstration makes
that concrete: the same dataset, inverted with two dampings that fit the data almost
equally well (rms residual $3.18$ ms at $\alpha = 0.001$ and $4.49$ ms at
$\alpha = 1$), yields one model that correlates with the truth at
$r = -0.04$ and another that correlates at $r = 0.83$. The residual difference is
$1.30$ ms against a $5.0$ ms noise level; the model difference is a factor $9.6$ in
model norm. **The data do not choose between them. The damping does.**

## 2. The forward problem

Straight rays through a $10 \times 5$ grid of $3\ \mathrm{km}$ cells
($x \in [0,30]$, $z \in [0,15]$ km) with a uniform background velocity of
$6.00\ \mathrm{km\,s^{-1}}$. The arrival time of ray $i$ is

$$t_i = \sum_j l_{ij}\,\bigl(s_0 + \delta s_j\bigr)
= t_i^{(0)} + \sum_j l_{ij}\,\delta s_j ,$$

where $l_{ij}$ is the length of ray $i$ in cell $j$ and $\delta s_j$ is the slowness
perturbation of cell $j$. The inversion parameters are the $\delta s_j$, so the
matrix is $G_{ij} = s_0 l_{ij}$ — the geometry $l$ scaled by the background slowness.

**Measured geometry (demo).** $100$ rays from $10$ sources to $10$ receivers,
$830$ non-zero ray–cell segments, $8.3$ cells per ray, mean ray length
$19.14\ \mathrm{km}$, and a path length per cell between $5.9$ and $74.4\ \mathrm{km}$
with no unlit cells. Coverage is *present* but *uneven by a factor $12.6$* — that
factor, not the ray count, sets the resolution.

**Synthetic data.** A Gaussian velocity anomaly of peak $+5.0\%$ (slowness
$\delta s/s_0 = -5\%$, rms $1.237\%$), centred at $x = 13.5\ \mathrm{km}$,
$z = 7.5\ \mathrm{km}$, half-widths $5 \times 3.5\ \mathrm{km}$. Its travel-time
signature is rms $36.16$ ms with a peak of $62.28$ ms, against $5.0$ ms of picking
noise: signal-to-noise $7.2$. That ratio, not the inversion code, decides what can
be recovered.

## 3. The project specification

**Steps.**

1. Build the ray-path matrix for the geometry you choose (sources at the surface,
   receivers at the surface) and report its dimensions, sparsity and coverage
   statistics.
2. Build a synthetic model, compute its travel times, add realistic picking noise,
   and report the signal-to-noise ratio.
3. Invert with damped least squares over a range of $\alpha$; tabulate the rms data
   residual, the model norm, the peak amplitude and the correlation with the truth.
4. Select $\alpha$ by the discrepancy principle and **state the rule you used**.
5. Report the amplitude recovery, the recovered position and the recovered rms.
6. Run a checkerboard test at one-cell scale and report the correlation and the
   amplitude recovery.
7. Compute point-spread functions for spikes at several depths and report the
   own-cell recovery and the fraction of magnitude leaking outside the cell.
8. State the resolution length for the shallowest and deepest well-recovered depth.
9. Write the resolution section: what is determined, at what length scale, and by
   what data.

**Deliverable.** The velocity model, the $\alpha$ table, the three resolution
diagnostics, and a one-paragraph resolution section with a stated resolution length.

**Success criterion.** The report quotes the damping rule, the noise level, the
recovered amplitude as a fraction of the true amplitude, and a resolution length in
kilometres. Any claim about a feature is qualified by whether the checkerboard test
resolved a structure of that scale at that depth.

## 4. Choosing the damping from the data

The objective is

$$\min_{\mathbf{m}} \ \|\mathbf{Gm}-\mathbf{d}\|_2^2 + \alpha^2\|\mathbf{m}\|_2^2 .$$

Tabulated on the demo's synthetic data:

| $\alpha$ | rms residual (ms) | model rms (%) | peak (%) | corr. with truth |
|---|---|---|---|---|
| 0.001 | 3.18 | 9.979 | $-22.19$ | $-0.040$ |
| 0.005 | 3.18 | 9.261 | $-20.21$ | $-0.016$ |
| 0.020 | 3.25 | 5.220 | $-12.87$ | $0.171$ |
| 0.050 | 3.39 | 2.623 | $-7.47$ | $0.433$ |
| 0.100 | 3.53 | 1.683 | $-6.14$ | $0.638$ |
| 0.500 | 3.92 | 1.117 | $-3.87$ | $0.830$ |
| 1.000 | 4.49 | 1.037 | $-3.46$ | $0.828$ |
| 5.000 | 18.98 | 0.511 | $-1.44$ | $0.805$ |
| 20.000 | 34.64 | 0.062 | $-0.16$ | $0.788$ |

Read the first two rows against the seventh. **Every statistic except the residual
improves as $\alpha$ grows from $0.001$ to $1.0$**, and the residual degrades by a
mere $1.3$ ms. The over-parameterised solutions ($\alpha \le 0.02$) have models with
a peak of $-20\%$ slowness where the truth is $-5\%$ — they are noise fitted into
cell-scale structure, and *they fit the data better*. This is the classic
tomographic trap and the reason the residuals in a tomography paper are not evidence
that the model is right.

For a rigorous choice, use the discrepancy principle: pick the **largest** $\alpha$
whose rms residual does not exceed the estimated noise level (here $5.0$ ms),
which gives $\alpha = 1.000$ on this dataset. (Equivalently, minimise the
generalised cross-validation or the Akaike/Bayesian information criterion; the three
agree to within a factor of a few on well-conditioned problems.)

## 5. What the inversion actually delivers

At $\alpha = 1.000$:

| diagnostic | value |
|---|---|
| rms data residual | $4.49$ ms (noise $5.0$ ms) |
| recovered peak | $3.46\%$ vs true $5.00\%$ ($69\%$ amplitude recovery) |
| recovered model rms | $1.037\%$ vs true $1.237\%$ |
| recovered position of the peak | $x = 13.5$, $z = 7.5$ km — exactly correct |
| checkerboard correlation | $r = 0.888$ |
| checkerboard amplitude recovery | $54.9\%$ (best cell $3.66\%$, worst $0.04\%$ of $4.00\%$) |
| PSF own-cell recovery (three depths) | $62.3\%$, $63.5\%$, $63.3\%$ |
| PSF magnitude outside the spike cell | $68.0\%$, $72.7\%$, $67.4\%$ |

Three doctoral-level readings:

1. **Positions are recovered better than amplitudes.** The anomaly is placed
   exactly while its magnitude is underestimated by $31\%$. A tomography image is a
   *location* map more reliably than it is an *amplitude* map, and reporting a
   velocity contrast from an uncalibrated amplitude is a known error.
2. **The checkerboard recovers less than the smooth anomaly** ($54.9\%$ vs $69\%$)
   because damping penalises the sign alternation that a one-cell checkerboard
   requires. A checkerboard test therefore reports a *conservative* resolution: if a
   feature of that scale appears in the image, it is real.
3. **The PSF says the same thing quantitatively.** For a spike in one cell the
   inversion returns $63.5\%$ of the input there and spreads the rest over roughly
   three other cells; the absolute gain summed over the grid is about $2.33$, i.e.
   the spike is smeared over $2.33/0.635 \approx 3.7$ effective cells even though
   the row of the resolution matrix sums to about unity. A $3\ \mathrm{km}$ cell
   does not carry a $3\ \mathrm{km}$ resolution.

## 6. Assumptions and failure modes

1. **Straight rays.** At local-earthquake distances rays bend; a straight-ray matrix
   misplaces structure, and the error is largest where the velocity contrast is
   largest. A two-step (bent-ray) or eikonal forward solver is the standard fix.
2. **Source location–velocity coupling.** The hypocentres are unknowns in the real
   problem, and a velocity error relocates events, which then re-interprets the
   travel times. This coupling is the central doctoral difficulty of local
   tomography and it is *not* resolved by a better inversion of fixed locations.
3. **The background velocity is assumed known.** $s_0$ enters every datum; an error
   in it trades off against a long-wavelength velocity perturbation.
4. **Anisotropy and heterogeneity outside the grid** alias into the model,
   especially under-station gaps (`tomography-controversies` in
   [06-06-07](../../06-seismology/06-seismic-tomography/07-tomography-controversies.md)).
5. **A checkerboard that looks good is not a licence to believe any single feature.**
   Correlation is a whole-image statistic; a specific anomaly can still be an
   artefact, which is why the PSF test is reported alongside it.

## 7. Rubric

| Criterion | Weight | Full marks |
|---|---|---|
| Forward operator correct and reported | 15% | dimensions, sparsity and coverage statistics given |
| Damping chosen from data | 20% | rule stated, table shown, over-parameterised models identified |
| Amplitude and position reported separately | 15% | $69\%$ recovery quoted for the amplitude, exact position for the peak |
| Three resolution diagnostics | 25% | checkerboard **and** PSF **and** coverage, with numbers |
| Resolution stated as a length | 15% | a resolution length in km for a stated depth, not a cell size |
| Source-location coupling discussed | 10% | named as the dominant limitation, with a design to break it |

## 8. The honest summary

The project's product is a velocity image *and a statement of what the image can
support*. The demonstration recovers a $+5\%$ anomaly at $69\%$ of its amplitude at
exactly the right place from $100$ noise-contaminated rays, with a checkerboard
correlation of $0.888$ and a PSF that keeps $63.5\%$ of a spike in its own cell and
leaks the rest. The defensible claims are a resolution length and a lower bound on
the amplitude; the indefensible ones are cell-scale structure, velocity contrasts
read off the image without an amplitude calibration, and hypocenter depths obtained
from a velocity model that the hypocentres themselves constrained.

## Python demonstration

[`code/tomography_demo.py`](./code/tomography_demo.py) prints every number above:

1. ray geometry and coverage per cell;
2. the synthetic dataset and its signal-to-noise ratio;
3. the damping table with the discrepancy-principle rule applied to it;
4. the recovery of the anomaly at the selected damping;
5. the one-cell checkerboard test;
6. point-spread functions for three depths.

```bash
cd 25-projects-capstone/05-doctoral-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tomography_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, no network, no files, no
plots, exits 0, runs in about $0.2$ s.

## Exercises

Graded problems and worked solutions are in
[`exercises/01-tomography-project-exercises.md`](./exercises/01-tomography-project-exercises.md)
and
[`exercises/01-tomography-project-solutions.md`](./exercises/01-tomography-project-solutions.md).
The ★★★ item asks for a design that breaks the source-location–velocity coupling.

## Mastery checkpoint

Without notes:

1. Write the forward relation for a straight-ray travel-time tomography datum.
2. State the discrepancy principle and apply it to the table above.
3. Explain why the model with the smallest residual is the worst model in the table.
4. Give the three resolution diagnostics and what each one measures.
5. State two reasons why a resolution claimed in kilometres is more useful than one
   quoted in cells.

## Common pitfalls

1. **Reporting the data residual as evidence of model quality.** The best residual
   belongs to the noise model.
2. **Choosing the damping by looking at the image.** Choose it from the noise level,
   then accept what the image shows.
3. **Quoting the cell size as the resolution.** It is the pixel size, not the
   resolving power; use the PSF width or the checkerboard.
4. **Presenting cell-scale structure from an under-damped inversion.** It is noise
   with geographical coordinates.
5. **Forgetting the location–velocity trade-off** when interpreting hypocentre depths.

## Where this is used

Local earthquake tomography underlies most volcanic and fault-zone imaging studies,
and its outputs — the velocity model and the relocated catalogue — are inputs to
hazard and tectonic interpretation. The resolution machinery developed here is the
same as that used for the ambient-noise and global tomography of
[06-07-01](../../06-seismology/07-ambient-noise-and-interferometry/01-noise-sources.md)
and [06-06-06](../../06-seismology/06-seismic-tomography/06-global-mantle-tomography.md),
and the damping-selection problem is the same one that confronts every
over-parameterised geophysical inversion, including the capstone-scale ones in
[Module 06](../06-capstone-research/README.md).

## Related lessons

- [06-06-04 Full-Waveform Inversion](../../06-seismology/06-seismic-tomography/04-full-waveform-inversion.md) —
  the alternative that uses the waveform instead of picked arrivals.
- [06-06-05 Adjoint Methods](../../06-seismology/06-seismic-tomography/05-adjoint-methods.md) —
  how the gradient of a waveform misfit is computed.
- [18-06-01 The Taxonomy of Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/01-uncertainty-taxonomy.md) —
  the Bayesian alternative to a resolution test.
- [25-05-02 Project: Full-Waveform Inversion](./02-full-waveform-inversion-project.md) —
  the next project, which replaces picked times by waveforms.

## Self-assessment checklist

- [ ] I can build a ray-path matrix and report its coverage statistics.
- [ ] I can choose damping from the noise level and defend the rule.
- [ ] I can show that a smaller residual can mean a worse model.
- [ ] I can run a checkerboard test and a PSF test and interpret both.
- [ ] I can state a resolution length in kilometres.
- [ ] I can describe the source-location–velocity coupling and how to attack it.
