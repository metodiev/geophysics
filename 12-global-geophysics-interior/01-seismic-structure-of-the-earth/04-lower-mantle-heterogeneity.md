---
id: 12-01-04
title: "Lower-Mantle Heterogeneity and LLSVPs"
level: research
prereqs: ["12-01-01", "12-01-03", "06-06-03", "06-06-06"]
tags: [global-geophysics, earth-interior, mantle-heterogeneity, tomography, llsvp, inverse-problems, resolution]
---

# Lower-Mantle Heterogeneity and LLSVPs

> **All models and data in this module are SYNTHETIC.** The reference profile, the
> anomaly model, the ray geometry, the noise level and the
> $\partial\ln v_s/\partial T$ sensitivity used here are chosen teaching values.
> No tomographic model, catalogue, station or measured anomaly is used. "LLSVP"
> labels a class of large low-velocity features near the base of the mantle; it is
> not a claim that this lesson's synthetic bodies are those features.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the first-order relation between a velocity anomaly and a
   travel-time residual, $\delta t = \int \delta u\,\mathrm{d}l$, and **explain**
   why the signal is three orders of magnitude smaller than the travel time.
2. **Derive** the damped least-squares solution
   $\mathbf{m} = \left(\mathbf{G}^{T}\mathbf{G} + \lambda^{2}\mathbf{I}\right)^{-1}
   \mathbf{G}^{T}\mathbf{d}$ and state what the damping term means physically.
3. **Compute** and **interpret** the resolution matrix
   $\mathbf{R} = \left(\mathbf{G}^{T}\mathbf{G}+\lambda^{2}\mathbf{I}\right)^{-1}
   \mathbf{G}^{T}\mathbf{G}$, its diagonal, and a point-spread function.
4. **Distinguish** a resolution deficit from a damping deficit in a recovered
   amplitude, and **quantify** each from a given inversion.
5. **Explain** why an undamped solution may not exist, and choose a damping from
   the data noise (discrepancy principle).
6. **Convert** a recovered velocity anomaly to a temperature, and **bound** the
   answer using the range of admissible damping.
7. **State** the assumption chain from a travel-time residual to a claim about
   structure and composition at the base of the mantle.

## Prerequisites

- [12-01-01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  the reference model subtracted from the data.
- [12-01-03 Upper-Mantle Discontinuities at 410 and 660 km](03-upper-mantle-discontinuities.md) —
  the same inference chain in the transition zone.
- [06-06-03 Resolution, Null Space and Model Covariance](../../06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) —
  the general theory this lesson applies.
- [06-06-06 Global Mantle Tomography and Its Geodynamic Interpretation](../../06-seismology/06-seismic-tomography/06-global-mantle-tomography.md) —
  the practical inversion and its geodynamic reading.

## 1. The measurement, and its smallness

The lower mantle is sampled by body waves whose travel times are compared with
the predictions of a reference model. The **residual** is

$$\delta t = t_\text{observed} - t_\text{reference}.$$

For a ray path $\Gamma$ and a slowness perturbation
$\delta u(\mathbf{x}) = u - u_\text{ref}$,

$$\boxed{\;\delta t = \int_\Gamma \delta u\,\mathrm{d}l
\;\approx\; -\int_\Gamma \frac{\delta v}{v^{2}}\,\mathrm{d}l.\;}$$

The linearisation replaces the perturbed path by the reference path, which is
Fermat's principle at work: the travel time is stationary with respect to path
perturbations, so the first-order error from using the reference geometry
vanishes. This is why teleseismic travel-time tomography can be written as a
*linear* inverse problem even though the underlying physics is not linear.

The magnitude deserves emphasis. In the demonstration, the reference travel times
of the 120 synthetic rays run from **226.2 s to 1065.7 s**, while the residuals
produced by a realistic anomaly model have an rms of only **2.290 s** — one part
in a thousand. A 1 % velocity error over a 1000 km segment at
$v = 12\ \mathrm{km\,s^{-1}}$ gives

$$\delta t = \frac{0.01 \times 12}{12^{2}} \times 1000 = 0.833\ \mathrm{s}$$

(Section 9 makes this exact). So the *reference model*, the *earthquake locations*
and the *origin times* must all be good to much better than the anomaly signal,
and any systematic error in them appears directly as structure. This is the
reason the same data set can support different-looking tomography models without
anyone having made a mistake.

## 2. The forward problem as a matrix

Discretise the model volume into $N$ cells. In the demonstration the region is
670–2891 km deep and 20 000 km wide, divided into $12 \times 40 = 480$ cells of
185 km $\times$ 500 km, and there are $M = 120$ ray paths. For the $i$-th ray,

$$d_i = \delta t_i = \sum_{j=1}^{N} G_{ij} m_j, \qquad
G_{ij} = \frac{L_{ij}}{v_j},$$

where $L_{ij}$ is the length of ray $i$ inside cell $j$, $v_j$ the reference
velocity there, and $m_j$ the **fractional slowness perturbation** in cell $j$.
The choice of $m = \delta u/u$ rather than $\delta v$ is deliberate: it makes the
model dimensionless, it makes the kernel positive (a path length times a
reference slowness is always positive, so $\mathbf{G}$ has no sign structure to
confuse the interpretation), and it makes the sign convention explicit — a
*positive* $m$ means *slow*, hence a *delay*, hence a *positive* residual.

The demonstration's forward residuals are of the expected size:

| ray | $p$ (s km$^{-1}$) | turning depth (km) | reference $T$ (s) | residual (s) |
|---|---|---|---|---|
| 0 | 0.09196 | 763 | 226.7 | +0.1484 |
| 30 | 0.08694 | 1232 | 556.2 | +0.9128 |
| 60 | 0.08192 | 1760 | 770.2 | +1.8150 |
| 90 | 0.07690 | 2356 | 952.4 | +3.4464 |
| 105 | 0.07522 | 2572 | 1009.6 | +3.0755 |

The residuals grow towards the deep rays, because the anomalies were placed near
the base of the mantle and because a deep ray spends more of its path there.

## 3. The inverse problem: damping is not optional

### 3.1 Derivation of damped least squares

Choose the model that minimises data misfit *plus* a penalty on model size:

$$\Phi(\mathbf{m}) = \left\|\mathbf{G}\mathbf{m} - \mathbf{d}\right\|^{2}
+ \lambda^{2}\left\|\mathbf{m}\right\|^{2}.$$

Setting $\partial\Phi/\partial\mathbf{m} = 0$:

$$2\mathbf{G}^{T}\left(\mathbf{G}\mathbf{m}-\mathbf{d}\right)
+ 2\lambda^{2}\mathbf{m} = 0
\;\Longrightarrow\;
\boxed{\;\mathbf{m} = \left(\mathbf{G}^{T}\mathbf{G}
+ \lambda^{2}\mathbf{I}\right)^{-1}\mathbf{G}^{T}\mathbf{d}.\;}$$

Three readings of the same equation:

- **Statistical.** If the data have covariance $\sigma^{2}\mathbf{I}$ and the
  model parameters have prior variance $\sigma^{2}/\lambda^{2}$, this is the
  maximum a posteriori estimate under a Gaussian prior. The damping is a *prior*
  that anomalies are small.
- **Numerical.** $\lambda^{2}\mathbf{I}$ makes the matrix invertible and bounds
  the amplification of data noise: a data eigenvector with singular value $s$ is
  amplified by $s/(s^{2}+\lambda^{2})$ instead of $1/s$.
- **Physical.** The penalty says that, among all models that fit the data, the one
  with the smallest norm is preferred. That is a choice, not a measurement.

### 3.2 Why the undamped solution does not exist here

With $M = 120$ data and $N = 480$ unknowns, $\mathbf{G}^{T}\mathbf{G}$ is a
480×480 matrix of rank at most 120. It is singular, and
$\lambda = 0$ fails in the demonstration. This is not a numerical accident: it
says that **more than three quarters of the model space is unconstrained**, and
the damping term is what selects a particular member of the infinite family of
exact-fit solutions.

### 3.3 Choosing $\lambda$ from the data

The **discrepancy principle** chooses the damping that fits the data to the noise
level — no better (which would fit noise) and no worse (which would ignore
information). The demonstration's data carry $\sigma = 0.030\ \mathrm{s}$ of
independent noise, and the matching solution is $\lambda = 30.0$, with rms misfit
0.02934 s. That is the inversion carried forward, and everything below is
conditional on it.

## 4. What the inversion recovers

The true model has two LLSVP-like bodies reaching 1.228 % slow near the base, plus
a broad 0.30 % slow anomaly at mid-depth. The recovered peak amplitude, as a
function of damping:

| $\lambda$ | rms misfit (s) | peak recovered (% slow) | peak/true |
|---|---|---|---|
| 1.0 | 0.00005 | 0.876 | 0.714 |
| 10.0 | 0.00435 | 0.869 | 0.707 |
| **30.0** | **0.02934** | **0.826** | **0.673** |
| 100.0 | 0.20117 | 0.652 | 0.531 |
| 300.0 | 0.89827 | 0.361 | 0.294 |
| 1000.0 | 1.96496 | 0.076 | 0.062 |
| 3000.0 | 2.24419 | 0.010 | 0.008 |
| 0.0 | — | — | singular |

Two *different* deficits are visible, and conflating them is the commonest error
in reading a tomography paper:

- **Resolution deficit.** Even at the smallest defensible damping the peak is only
  71 % of the truth. The rays do not sample cells independently, so a single cell's
  amplitude is necessarily spread over its neighbours. No amount of tuning fixes
  this; only more or better-distributed data does.
- **Damping deficit.** Increasing $\lambda$ from 1 to 3000 reduces the recovered
  peak from 0.876 % to 0.010 %, a factor of 88, while the misfit rises from
  essentially zero to 2.2 s. This part *is* under the analyst's control, and it is
  why the "amplitude" of a tomographic anomaly is not a measurement.

The trade-off curve makes the same point:

| $\lambda$ | $\lVert \mathbf{G}\mathbf{m}-\mathbf{d}\rVert$ (s) | $\lVert\mathbf{m}\rVert\times100$ (% slow) | misfit² |
|---|---|---|---|
| 1.0 | 0.0005 | 7.1924 | 0.0000 |
| 10.0 | 0.0477 | 7.1599 | 0.0023 |
| 30.0 | 0.3214 | 7.0022 | 0.1033 |
| 100.0 | 2.2037 | 6.2555 | 4.8564 |
| 300.0 | 9.8400 | 3.9137 | 96.8256 |
| 1000.0 | 21.5251 | 0.8660 | 463.33 |
| 3000.0 | 24.5839 | 0.1115 | 604.37 |

Every row is an admissible answer to exactly the same 120 numbers. The curve is
the *set* of answers; the choice of a point on it is an additional assumption.

## 5. Resolution: the diagonal and the point-spread function

The resolution matrix is defined by asking how the estimate responds to the truth:

$$\hat{\mathbf{m}} = \mathbf{R}\,\mathbf{m}_\text{true}
+ \left(\mathbf{G}^{T}\mathbf{G}+\lambda^{2}\mathbf{I}\right)^{-1}\mathbf{G}^{T}
\mathbf{n}, \qquad
\mathbf{R} = \left(\mathbf{G}^{T}\mathbf{G}+\lambda^{2}\mathbf{I}\right)^{-1}
\mathbf{G}^{T}\mathbf{G}.$$

$R_{ij}$ is the weight with which cell $j$'s true value contributes to cell $i$'s
estimate. Along the diagonal (for $\lambda = 30$):

| depth (km) | mean $R_{ii}$ | min | max |
|---|---|---|---|
| 763 | 0.504 | 0.352 | 0.592 |
| 1133 | 0.349 | 0.000 | 0.486 |
| 1503 | 0.243 | 0.000 | 0.434 |
| 1873 | 0.180 | 0.000 | 0.320 |
| 2243 | 0.130 | 0.000 | 0.256 |
| 2798 | 0.065 | 0.000 | 0.156 |

Reading:

- **Nothing is close to 1.** The best-resolved cells retain half their own
  amplitude; the deepest retain 6 %.
- **Some cells are exactly 0.** Those cells are in the null space: no combination
  of the data, with this geometry and this damping, determines them at all. A
  tomographic image that colours every cell of a grid is therefore showing
  model values, not measurements.
- **The deepest layers are the worst.** Long, steep paths provide almost no
  independent depth information at the base of the mantle: the same ray samples a
  broad depth range, so a displacement of the anomaly in depth barely changes the
  travel time.

The **point-spread function** — one row of $\mathbf{R}$ — shows how a single cell's
truth is smeared. For the cell at depth 2798 km, $x = 5250$ km:

| depth (km) | max $\lvert R\rvert$ in the layer | row sum over the layer |
|---|---|---|
| 763 | 0.0232 | +0.0047 |
| 1688 | 0.0332 | +0.0076 |
| 2428 | 0.0402 | +0.0064 |
| 2613 | 0.0623 | +0.0798 |
| 2798 | 0.0606 | +0.2844 |

The response is spread across the *entire* mantle column, with the largest weights
in the deepest layers, and it contains negative values. The negative lobes are the
signature of damping: to keep $\lVert\mathbf{m}\rVert$ small while fitting the
data, the inversion must borrow amplitude from neighbours with the opposite sign.
An isolated negative anomaly in a tomography model may therefore be an artefact of
the regularisation rather than a feature.

## 6. LLSVPs: what an image of them does and does not establish

With the machinery above, the honest statement about a large low-velocity region
at the base of the mantle from travel-time tomography is:

- **its location and lateral extent** are constrained, because many rays pass
  through or near it and the lateral sampling is comparatively dense;
- **its sign** is constrained, provided the reference model and the data
  processing are adequate;
- **its amplitude** is *not* determined: the demonstration's factor-of-88 range as
  $\lambda$ varies, and the factor-of-1.4 resolution deficit at the smallest
  damping, both sit inside the signal;
- **its vertical extent** is weakly constrained, because the resolution diagonal
  falls to 0.065 in the deepest layer and the point-spread function smears over
  the whole column.

Amplitude recovery in the demonstration varies systematically with depth:

| depth (km) | true rms (% slow) | $\mathbf{R}\mathbf{m}_\text{true}$ rms | recovered rms | ratio | mapped noise rms |
|---|---|---|---|---|---|
| 763 | 0.0717 | 0.1325 | 0.1379 | 1.92 | 0.0214 |
| 1318 | 0.2550 | 0.2556 | 0.2522 | 0.99 | 0.0136 |
| 2058 | 0.2823 | 0.3046 | 0.3047 | 1.08 | 0.0086 |
| 2428 | 0.5926 | 0.4235 | 0.4222 | 0.71 | 0.0080 |
| 2613 | 0.7139 | 0.4519 | 0.4497 | 0.63 | 0.0075 |
| 2798 | 0.6097 | 0.4116 | 0.4133 | 0.68 | 0.0063 |

with an overall true-versus-recovered correlation of **0.5646**. The table also
carries the *diagnosis*, and it is worth reading carefully because the obvious
guess is wrong. The **third column** is the noise-free prediction
$\mathbf{R}\mathbf{m}_\text{true}$: it reproduces the recovered rms to two decimal
places. The **last column** is the data noise mapped into the model (the square
root of the diagonal of
$\sigma^{2}\mathbf{A}^{-1}\mathbf{G}^{T}\mathbf{G}\mathbf{A}^{-1}$), and it is
five to ten times smaller. So the amplitude pattern is **resolution, not noise**:
the inversion smears the strong deep anomalies upward and flattens them, so the
shallow layers *gain* rms (a factor of 1.9 where the truth is smallest) and the
deep layers *lose* it (a factor of 0.63 where the truth is largest).

The image therefore flattens the real heterogeneity: it systematically makes large
anomalies smaller and small ones bigger. This is the quantitative version of a
sentence that appears in every tomography paper — "amplitudes should not be
overinterpreted" — and it is the reason LLSVP *size* and *shape* are more robust
conclusions than LLSVP *strength*.

## 7. From anomaly to temperature, and the assumption chain

Converting a recovered anomaly to a temperature uses

$$\Delta T = \frac{\delta \ln v_s}{\partial \ln v_s/\partial T},$$

with the demonstration's chosen sensitivity
$\partial\ln v_s/\partial T = -1.2\times10^{-5}\ \mathrm{K^{-1}}$ — that is,
**833 K per 1 %** of velocity anomaly. Applying it to the recovered peaks:

| $\lambda$ | peak recovered (% slow) | implied $\lvert\Delta T\rvert$ (K) |
|---|---|---|
| 1.0 | 0.876 | 730 |
| 30.0 | 0.826 | 689 |
| 100.0 | 0.652 | 544 |
| 300.0 | 0.361 | 301 |
| 1000.0 | 0.076 | 64 |

The true peak would give 1023 K. Across the defensible damping range
($\lambda = 1$ to 300, where the misfit stays within a second), the answer varies
by a factor of **2.4** — 730 K down to 301 K — before any uncertainty in the
temperature sensitivity is considered.

The chain from residual to temperature has five links, each of which can fail:

1. **reference model** — a wrong reference velocity is indistinguishable from
   structure;
2. **source and path** — event locations, origin times, and outside-the-model
   structure contribute;
3. **linearisation and discretisation** — the cell size is chosen, and a body
   thinner than a cell cannot be recovered whatever the damping;
4. **regularisation** — sets the amplitude;
5. **mineral physics** — converts velocity to temperature, and is itself
   composition-dependent (see
   [12-02-01 Mantle Composition](../02-composition-and-mineral-physics/01-mantle-composition.md)).

A temperature is therefore the *last* link of a chain, and quoting it without the
other four is a claim the data cannot support. What the data *can* support is the
ranking: within one inversion, a region with twice the recovered anomaly is
probably twice as anomalous, because the resolution and damping deficits act
similarly on neighbouring regions.

## 8. Assumptions and regime of validity

1. **First-order (ray) perturbation theory.** Valid when the anomaly is small
   compared with the background and smooth compared with the wavelength. Near
   caustics, and for strong, sharp anomalies, the true sensitivity kernel is
   *banana–doughnut* shaped rather than a line, and the linear approximation
   misplaces the sensitivity.
2. **Fixed ray geometry.** Paths are computed in the reference model. For a 1 %
   anomaly the path perturbation is a second-order effect, which is exactly why
   the linearisation is legitimate; for a 10 % anomaly it is not.
3. **Gaussian, independent, zero-mean data noise.** Picking errors are
   approximately Gaussian; *travel-time* errors also contain correlated
   components (source mislocation, station statics) that this assumption misses,
   and their presence is why the misfit at the "correct" damping often exceeds
   the formal noise level.
4. **No trade-off with outside-the-model structure.** Anomalies above 670 km, in
   the crust beneath a station, or outside the modelled volume are mapped into the
   model. This is usually the largest single uncertainty.
5. **An isotropic, elastic Earth.** Anisotropy (lesson
   [06](06-outer-and-inner-core.md)) and anelastic dispersion both contaminate
   amplitudes.
6. **A stationary sensitivity kernel.** The kernel depends on the reference
   velocity model, so the same data inverted in two reference models give two
   answers.

## 9. Worked examples

### Example 1 — the size of a residual

A 1000 km segment of a ray with local $v = 12.0\ \mathrm{km\,s^{-1}}$ crosses an
anomaly with $\delta v = -0.12\ \mathrm{km\,s^{-1}}$ (1 % slow). Then

$$\delta u = -\frac{\delta v}{v^{2}} = -\frac{-0.12}{144}
= +8.333\times10^{-4}\ \mathrm{s\,km^{-1}},$$
$$\delta t = 8.333\times10^{-4} \times 1000 = +0.833\ \mathrm{s}.$$

A 1 % anomaly produces a sub-second residual. Compare the demonstration's
residuals (0.15–3.4 s), which come from multi-percent anomalies accumulating over
thousands of kilometres of deep path.

### Example 2 — an exactly unresolved pair of cells (a null space, in closed form)

Two cells, two rays, and $\mathbf{G} = \begin{pmatrix}1 & 1\\ 1 & 1\end{pmatrix}$:
the rays sample the two cells identically, which is what happens when a cell size
is finer than the data can distinguish. Then $\mathbf{G}^{T}\mathbf{G} =
\begin{pmatrix}2&2\\2&2\end{pmatrix}$ and

$$\mathbf{R} = \frac{2\lambda^{2}}{\left(2+\lambda^{2}\right)^{2}-4}
\begin{pmatrix}1&1\\1&1\end{pmatrix}
= \frac{2}{\lambda^{2}+4}\begin{pmatrix}1&1\\1&1\end{pmatrix}.$$

Both diagonal entries equal both off-diagonal entries, so $R_{11} = R_{12}$: cell
1's estimate contains exactly as much of cell 2's truth as of its own. The
diagonal is $2/(\lambda^{2}+4)$, which tends to **1/2** as the damping vanishes
and equals 1/3 at $\lambda^{2} = 2$; it can never approach 1 for any damping. The
difference $m_1 - m_2$ is never recovered at all — it is the null-space direction,
and no damping removes the ambiguity, because the ambiguity is in the data, not in
the inversion. Reducing $\lambda$ buys the average, not the difference.

### Example 3 — temperature and its damping uncertainty

A recovered peak of 1.00 % slow at the base of the mantle, with
$\partial\ln v_s/\partial T = -1.2\times10^{-5}\ \mathrm{K^{-1}}$:

$$\Delta T = \frac{0.01}{-1.2\times10^{-5}} = -833\ \mathrm{K},$$

i.e. 833 K hot. Now suppose the same study, rerun with a damping twice as large
(which is entirely defensible), recovers 0.75 % instead. The temperature becomes

$$\Delta T = \frac{0.0075}{-1.2\times10^{-5}} = -625\ \mathrm{K}.$$

A factor-of-1.33 change in the recovered amplitude is a 208 K change in the
temperature — larger than most of the physical effects the temperature is used to
test. **The correct way to report this is as a range with the damping stated**, or
as a comparison with another region inverted identically.

## 10. Python demonstration

`code/lower_mantle_heterogeneity_demo.py` builds the ray geometry and the matrix
$\mathbf{G}$ from first principles, generates synthetic residuals, and inverts
them with damped least squares. It prints: the reference travel times and
residuals; the recovered peak amplitude versus $\lambda$; the trade-off curve; the
resolution diagonal and one point-spread function; amplitude recovery by depth;
and the temperature range implied by the damping choice. It runs in under a
second:

```bash
cd 12-global-geophysics-interior/01-seismic-structure-of-the-earth/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lower_mantle_heterogeneity_demo.py
```

## 11. Exercises

Full sets with worked solutions are in
[`exercises/04-lower-mantle-heterogeneity-exercises.md`](exercises/04-lower-mantle-heterogeneity-exercises.md)
and
[`exercises/04-lower-mantle-heterogeneity-solutions.md`](exercises/04-lower-mantle-heterogeneity-solutions.md).

- **★** Compute a residual from a given anomaly and path length, with units.
- **★★** Compute $\mathbf{R}$ for a two-cell problem in closed form and interpret
  the off-diagonal.
- **★★** Propagate a damping change through to a temperature range.
- **★★★** Design a data set that raises the resolution diagonal at the base of the
  mantle, and predict the improvement quantitatively.

## Mastery checkpoint

Without notes:

> A travel-time inversion uses 300 rays and a grid of 2000 cells, with
> $\lambda = 50$ chosen so that the rms misfit equals a stated 0.04 s noise level.
> The recovered peak in a deep region is 1.4 % slow.
> **(a)** State with a number how many model-space directions are left
> unconstrained.
> **(b)** Explain why the recovered 1.4 % is a lower bound on the true anomaly
> *only if* the resolution diagonal exceeds the damping-induced bias, and state
> what you would need to compute to check.
> **(c)** Convert the 1.4 % to a temperature with
> $\partial\ln v_s/\partial T = -1.2\times10^{-5}\ \mathrm{K^{-1}}$, and then
> recompute it assuming the true resolution diagonal at that depth is 0.5.
> **(d)** Name two observations that would tighten the *vertical* extent of the
> anomaly.

A worked version appears in the lesson-04
[solutions](exercises/04-lower-mantle-heterogeneity-solutions.md).

## Common pitfalls

1. **Reading the colour scale as data.** The resolution diagonal in the
   demonstration never exceeds 0.60 and falls to 0.065; uncoloured grid cells are
   model values, not measurements.
2. **Quoting a percentage anomaly without the damping.** The same data give
   0.010 % to 0.876 % depending on $\lambda$.
3. **Confusing resolution with damping deficits.** They have different fixes:
   resolution needs better data coverage, damping needs a justified choice.
4. **Assuming the recovery bias is uniform.** It is depth-dependent (ratios 0.63
   to 1.92 in the demonstration), so comparing amplitudes across depths within one
   model is biased even when comparing across *regions* is safer. And the cause is
   resolution, not noise: the noise-free estimate
   $\mathbf{R}\mathbf{m}_\text{true}$ already reproduces the pattern.
5. **Interpreting a negative lobe as structure.** It is usually the fingerprint of
   regularisation.
6. **Treating a temperature as a measurement.** It is the fifth link of a chain
   that begins with the reference model.
7. **Forgetting that unmodelled shallow structure maps into the model.** Crustal
   and upper-mantle errors are frequently larger than the deep signal.

## Related modules

- [01 PREM, IASP91 and Reference Earth Models](01-prem-and-reference-models.md) —
  what the residuals are measured against.
- [03 Upper-Mantle Discontinuities at 410 and 660 km](03-upper-mantle-discontinuities.md) —
  the transition-zone version of the same inference.
- [05 Core-Mantle Boundary: ULVZ, D'' and Post-Perovskite](05-core-mantle-boundary.md) —
  the thinnest and least resolvable structure of all, directly beneath LLSVP depths.
- [06 Outer Core, Inner Core Anisotropy and Rotation](06-outer-and-inner-core.md) —
  the region the deepest rays must cross.
- [12-02-01 Mantle Composition and Peridotite Models](../02-composition-and-mineral-physics/01-mantle-composition.md) —
  whether a velocity anomaly can be compositional rather than thermal.
- [06-06-03 Resolution, Null Space and Model Covariance](../../06-seismology/06-seismic-tomography/03-resolution-and-nullspace.md) —
  the full theory, including the Bayesian framing.
- [18-inverse-problems](../../18-inverse-problems/README.md) — regularisation,
  trade-off curves and model selection in general.

## Self-assessment checklist

- [ ] I can derive $\delta t = \int \delta u\,\mathrm{d}l$ and give the sizes.
- [ ] I can write down the damped least-squares solution and say what $\lambda$
      means in three ways.
- [ ] I can explain why an undamped solution may not exist.
- [ ] I can compute and read a resolution matrix diagonal.
- [ ] I can distinguish a resolution deficit from a damping deficit with numbers.
- [ ] I can choose a damping from a stated noise level.
- [ ] I can convert an anomaly to a temperature and bound it with the damping
      range.
- [ ] I can list the five links from a residual to a temperature claim.
