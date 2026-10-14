---
id: 06-04-02
title: "Dependence on the Velocity Model and Joint Inversion"
level: graduate
prereqs: ["06-04-01", "06-02-01", "06-02-04", "18-01-03"]
tags: [seismology, location, velocity-model, bias, joint-inversion]
---

# Dependence on the Velocity Model and Joint Inversion

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the exact effect of a uniform velocity scaling on travel times, and
   use it to construct a controlled velocity-model error.
2. **Derive** the linearised sensitivity of a located depth to that scaling, and
   explain the sign of the bias from ray geometry rather than by rule of thumb.
3. **Quantify** how far a location moves for a 2, 4 and 8 per cent velocity
   error, and compare each with the nominal 95 per cent pick-based bound.
4. **Compute** the largest velocity error that the picks themselves can absorb,
   and explain why the honest depth interval is a joint interval over
   (depth, velocity).
5. **Judge** when a joint inversion is required and when reporting a depth with
   a stated velocity model is enough.
6. **State** which part of a catalogue depth is a measurement and which part is
   a modelling assumption.

## Prerequisites

- [01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses](01-hypocentre-location.md) —
  the Jacobian, the normal equations and the covariance.
- [06-02-01 Eikonal Equation, Rays and Fermat's Principle](../02-ray-theory-and-travel-times/01-eikonal-and-rays.md) —
  the travel-time integral used in Section 3.
- [06-02-04 Ray Tracing in Laterally Varying Media](../02-ray-theory-and-travel-times/04-ray-tracing.md) —
  the forward model that replaces a half-space.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the language in which Section 4 is written.

## 1. Intuition: the model you assume is part of the answer

Lesson [01](01-hypocentre-location.md) produced a confidence ellipsoid. That
ellipsoid is a statement about the picks *conditional on a velocity model*, and
the condition is where the real uncertainty lives. A depth is not measured the
way an arrival time is measured; it is inferred from arrival-time differences
using model velocities, so a velocity error of a few per cent translates into a
depth error of kilometres.

Two properties make this tractable rather than merely worrying.

- A **uniform scaling** of a velocity model, $v \to s\,v$ with $s$ a constant,
  scales every travel time by exactly $1/s$. That gives a controlled error whose
  consequences can be derived in closed form instead of guessed.
- The resulting bias is **systematic and shared**: every station moves the event
  in the same direction, so it cannot be averaged away and it does not appear in
  the residual as random scatter. It appears as a *large* residual at a *wrong*
  location, which is exactly what the demonstration measures.

## 2. Precise statement of the experiment

Place a synthetic event at $(x, y, z)$ with origin time $t_0$, and record its
arrivals at a set of distances $\Delta$ through a reference velocity model. Let
$T_i(z)$ be the reference travel time to station $i$. The synthetic data are

$$
T_i^{\text{obs}} = T_i(z_{\text{true}}) + t_0^{\text{true}} .
$$

Now locate the event with a **perturbed** model in which every velocity has been
multiplied by $s = 1 + d$. Because the perturbation is uniform, the predicted
travel time in the perturbed model is exactly $T_i(z)/s$. The locator searches a
grid of depths and, for each depth, fits the origin time by the mean residual,

$$
t_0(z) = \frac{1}{N}\sum_i \left(T_i^{\text{obs}} - T_i(z)/s\right) ,
\qquad
\mathrm{rms}(z) = \sqrt{\frac{1}{N}\sum_i
\left(r_i(z) - \bar{r}(z)\right)^{2}} ,
$$

and reports the depth with the smallest rms. The quantity of interest is the
**depth bias** $z_{\text{loc}} - z_{\text{true}}$ as a function of $d$. Nothing
in the experiment is random: with exact data and a wrong model, the bias is
reproducible arithmetic.

## 3. Derivations

### 3.1 Uniform scaling scales all travel times exactly

The travel time along a ray is the integral of slowness over the path,

$$
T = \int_{\text{ray}} \frac{\mathrm{d}\ell}{v(\mathbf{x})} .
$$

Replacing $v(\mathbf{x})$ by $s\,v(\mathbf{x})$ divides the integrand by $s$ at
every point, so

$$
T \rightarrow \frac{1}{s}\int_{\text{ray}} \frac{\mathrm{d}\ell}{v(\mathbf{x})}
= \frac{T}{s} ,
$$

and Fermat's principle guarantees the same path is stationary for both models,
so the ray itself does not change. A uniform scaling is therefore the *cleanest
possible* velocity error: it is a single multiplicative number with no
trade-off with the ray geometry. Everything the demonstration measures is
attributable to $d$ alone.

### 3.2 Why a depth can absorb a scaling error

With the origin time free and the geometry fixed, the residual for a scaling
error $d$ is

$$
r_i = T_i^{\text{obs}} - \frac{T_i(z_{\text{true}})}{1 + d}
= T_i\left(1 - \frac{1}{1+d}\right)
\approx d\,T_i ,
\qquad d \ll 1 .
$$

So the misfit is **not** random scatter: it is a systematic residual
proportional to the arrival time itself, and therefore larger at large distances.
That is the signature that lets a depth change absorb part of it. The
sensitivity of a predicted time to depth is

$$
\frac{\partial T_i}{\partial z} = \frac{z}{v\,r_i}
\qquad\text{with } r_i = \sqrt{\Delta_i^{2} + z^{2}} ,
$$

which *decreases* with epicentral distance, because a distant ray leaves the
source at a shallower angle to the horizontal. The depth is therefore a
mechanism for redistributing predicted time **between near and far stations**:
raising the source removes more time from the nearby stations than from the
distant ones, which is precisely the pattern needed to compensate a residual
that grows with distance.

To first order, with the origin time removed by the mean, the depth adjusts to
minimise $\|\,d\,\tilde{T}_i + \delta z\,\widetilde{\partial T_i/\partial z}\,\|$
where the tilde denotes removal of the mean. The solution is the one-parameter
least-squares value

$$
\delta z = -\,d\,
\frac{\sum_i \tilde{T}_i\, \widetilde{\partial T_i/\partial z}}
{\sum_i \left(\widetilde{\partial T_i/\partial z}\right)^{2}} ,
$$

whose *sign* is set by the geometry through the correlation between $T_i$ and
$\partial T_i/\partial z$. This is the quantitative content of the rule "a
faster model makes a regional event shallower": it is a statement about the
sign of that correlation for grazing rays, not a universal law — at teleseismic
distances, where the rays steepen, the sign can reverse.

### 3.3 The nominal bound does not contain the bias

Lesson [01](01-hypocentre-location.md) gave the covariance
$C = \sigma_t^{2}(J^{T}J)^{-1}$. The depth uncertainty implied by the misfit
curvature is the standard one-parameter result

$$
\chi^{2}(z) = \frac{1}{\sigma_t^{2}}\sum_i \left(r_i - \bar{r}\right)^{2},
\qquad
\sigma_z^{2} = \frac{2}{\mathrm{d}^{2}\chi^{2}/\mathrm{d}z^{2}} ,
\qquad
\text{95 per cent bound} = 1.96\,\sigma_z .
$$

The factor 2 is the variance of a $\chi^{2}$ variable with one parameter; the
pick uncertainty cancels because it is already divided into $\chi^{2}$. Both
quantities are computed under the assumption that the velocity model is the true
one. Section 4 shows what that assumption costs.

## 4. Worked examples

All numbers come from `code/velocity_model_dependence_demo.py`. The reference
model is the one distributed with ObsPy; it is used **as a model**, not as a
measurement of any region. The synthetic event is at $12.0\ \mathrm{km}$ depth
with origin time $2.00\ \mathrm{s}$, recorded at 10 distances from
$0.6^\circ$ to $8.0^\circ$, with pick uncertainty
$\sigma_t = 0.050\ \mathrm{s}$. The observed arrival times run from
$14.423\ \mathrm{s}$ at the nearest station to $118.029\ \mathrm{s}$ at the
farthest, a ratio of 8.18.

### Example 1 — the control

Located with the model that generated the data, the depth is
$12.00\ \mathrm{km}$ (bias $+0.00\ \mathrm{km}$), the origin time
$2.000\ \mathrm{s}$ (bias $+0.000\ \mathrm{s}$), and the rms residual is
$0.0\ \mathrm{s}$. The grid step is $0.25\ \mathrm{km}$, so the control recovers
the input to the grid. Every bias below is therefore attributable to the
velocity model, not to the numerical method.

### Example 2 — the bias as a function of the scaling error

| $d$ (%) | located depth (km) | depth bias (km) | $t_0$ (s) | $t_0$ bias (s) | rms residual (s) |
|---|---|---|---|---|---|
| $-8.0$ | 30.00 | $+18.00$ | $-0.861$ | $-2.861$ | $2.516\times10^{0}$ |
| $-4.0$ | 30.00 | $+18.00$ | 1.472 | $-0.528$ | $1.141\times10^{0}$ |
| $-2.0$ | 20.00 | $+8.00$ | 1.826 | $-0.174$ | $5.857\times10^{-1}$ |
| $0.0$ | 12.00 | $0.00$ | 2.000 | $0.000$ | $0.000\times10^{0}$ |
| $+2.0$ | 6.25 | $-5.75$ | 2.412 | $+0.412$ | $5.794\times10^{-1}$ |
| $+4.0$ | 6.25 | $-5.75$ | 3.426 | $+1.426$ | $1.183\times10^{0}$ |
| $+8.0$ | 6.25 | $-5.75$ | 5.341 | $+3.341$ | $2.327\times10^{0}$ |

Three readings matter.

- **The sign follows the geometry.** A *negative* $d$ is a slower locating model,
  which fits the same late arrivals with a *deeper* source; a positive $d$ is
  faster and fits them with a *shallower* source. Section 3.2 explains why.
- **The grid saturates.** With $d \le -4$ per cent the best depth is the deepest
  grid node ($30.00\ \mathrm{km}$), and with $d \ge +4$ per cent it is the
  shallowest that still fits, so the bias stops growing. A grid search that
  reports "depth = 30 km" is sometimes reporting the edge of its own grid, which
  is a modelling artefact and must be stated.
- **The residual grows with the error**, from $0.580\ \mathrm{s}$ at 2 per cent
  to $2.327\ \mathrm{s}$ at 8 per cent. Those residuals are 12 to 47 times the
  pick uncertainty, so the wrong velocity model is not a subtle effect: it is
  visible in the misfit of any competent locator.

### Example 3 — the pick-based bound, and the bias that exceeds it

From the curvature of $\chi^{2}$ in depth at the true depth, the demonstration
obtains

$$
\frac{\mathrm{d}^{2}\chi^{2}}{\mathrm{d}z^{2}} = 2.2295\ \mathrm{km^{-2}},
\qquad
\sigma_z = 0.947\ \mathrm{km},
\qquad
1.96\,\sigma_z = 1.856\ \mathrm{km} .
$$

Comparing the bias with that bound:

| $d$ (%) | depth bias (km) | bias / 95 % bound | inside the nominal bound? |
|---|---|---|---|
| $-8.0$ | $+18.00$ | 9.696 | no |
| $-4.0$ | $+18.00$ | 9.696 | no |
| $-2.0$ | $+8.00$ | 4.309 | no |
| $0.0$ | 0.00 | 0.000 | yes |
| $+2.0$ | $-5.75$ | $-3.097$ | no |
| $+4.0$ | $-5.75$ | $-3.097$ | no |
| $+8.0$ | $-5.75$ | $-3.097$ | no |

A 2 per cent uniform velocity error already moves the depth by 3.1 times the
nominal 95 per cent bound, in a direction the bound cannot foresee; 8 per cent
moves it by 9.7 times. The bound is not wrong; it is answering a different
question. It describes the precision of the picks **given** the model, while the
bias is the cost of the model being wrong.

A related number that is easy to confuse with this one: Section 4 accepts a depth
whenever the rms residual stays below the pick uncertainty, which is a much
looser criterion than 95 per cent confidence, and it admits depths from 9.25 to
14.75 km — a half-width of 2.75 km against the 1.856 km bound here. Two
criteria, two intervals, both defensible, and they must not be quoted
interchangeably.

### Example 4 — how much velocity error do the picks themselves allow?

Accept a (velocity scale, depth) pair when the rms residual after fitting $t_0$
stays below $\sigma_t = 0.050\ \mathrm{s}$. With the reference model, the depths
that pass span $9.25$ to $14.75\ \mathrm{km}$, a width of $5.50\ \mathrm{km}$ —
the depth/origin-time trade-off of lesson [01](01-hypocentre-location.md) doing
its work.

Now let the velocity scale vary and repeat. The demonstration reports:

| $d$ (%) | min rms residual over depth (s) | best depth (km) | depths consistent with the picks (km) |
|---|---|---|---|
| $-2.0$ | 0.5857 | 20.00 | none |
| $-1.0$ | 0.2685 | 20.00 | none |
| $-0.5$ | 0.1308 | 17.50 | none |
| $0.0$ | 0.0000 | 12.00 | 9.25 – 14.75 |
| $+0.5$ | 0.1295 | 6.25 | none |
| $+1.0$ | 0.2733 | 6.25 | none |
| $+2.0$ | 0.5794 | 6.25 | none |

Bisection on that criterion gives the largest velocity error the picks can still
absorb:

$$
d_{\text{tol}} = 0.19\ \text{per cent} .
$$

Beyond **0.19 per cent** no depth at all fits the picks within the pick
uncertainty. Over the whole admitted velocity range, the union of acceptable
depths is $8.50$ to $15.50\ \mathrm{km}$: a width of $7.00\ \mathrm{km}$, against
$5.50\ \mathrm{km}$ with the model held fixed.

This is the sharpest result in the lesson, and it cuts in a surprising
direction. The velocity dimension widens the depth interval only slightly,
because the picks pin the velocity scale to a fifth of a per cent — far tighter
than any real velocity model is known. So the nominal error bar is *narrow for
the wrong reason*: it is precise about a quantity (the velocity scale) that
real models get wrong by one to eight per cent, and it is silent about whether
the model is right at all. The relevant comparison is not $7.00\ \mathrm{km}$
against $5.50\ \mathrm{km}$; it is $0.19$ per cent against 2 per cent.

### Example 5 — one scaling error, two stations, by hand

Take $d = +0.02$ and read the residual formula of Section 3.2:

$$
1 - \frac{1}{1.02} = 0.019608 ,
$$

so at the nearest station the residual is
$0.019608 \times 14.423 = 0.283\ \mathrm{s}$, and at the farthest it is
$0.019608 \times 118.029 = 2.315\ \mathrm{s}$. Both are far above the pick
uncertainty of $0.050\ \mathrm{s}$, the second by a factor of 46, which is why
the first row of Example 4's table has *no* consistent depth. The residual is
not noise: it is 0.0196 times the arrival time, and it is the same at every
station to within a per cent, growing with distance.

## 5. Joint inversion as the honest alternative

Since depth and velocity trade off, the honest object is a **joint** set of
solutions. Two practical forms:

1. **Consistency scan.** For every velocity in a defensible range and every
   depth on a grid, accept the pair if the residual is consistent with the pick
   uncertainty; report the union, exactly as Example 4 does. Cheap, transparent,
   and it makes the assumption explicit.
2. **Joint inversion with a prior.** Include the velocity scale (or a few
   layered velocities) as parameters with a prior from an independent
   measurement — a borehole, a receiver function, a tomography model — and
   report the *posterior* depth interval. The answer is then conditional on the
   prior, which is the point: it is honest about what is being assumed.

What a joint inversion cannot do is remove the trade-off entirely. Adding
parameters adds directions to the null space; only *independent* data, or a
prior, constrain them. Lesson [06-04-01](01-hypocentre-location.md) Section 3.2
is the geometric statement of why.

## 6. Assumptions and regime of validity

1. The velocity error is a **uniform scaling**. Real model error is depth- and
   region-dependent; a uniform scaling is the smallest, best-case error, so the
   biases above are lower bounds on what a wrong model does.
2. The forward model in the *locating* stage is the reference model's own
   family, differing only by the scale. If the locating model has a different
   shape — a different crustal thickness, say — there is no closed form and the
   bias must be measured case by case.
3. The picks are **exact**. Pick noise adds scatter on top of the bias; with
   $\sigma_t = 0.050\ \mathrm{s}$ and 10 stations, the scatter is of order the
   1.9 km bound of Example 3, so the two effects are comparable, not nested.
4. The depth grid is finite. Grid saturation is a real feature of Example 2 and
   is not a property of the Earth.
5. The event is inside the distance range where the reference model is
   appropriate. Extrapolating the numbers here to teleseismic or local
   geometries is not justified; the *method* transfers, the numbers do not.

## 7. The demonstration

`code/velocity_model_dependence_demo.py` computes the control, the bias table,
the nominal bound, the joint consistency scan and the velocity tolerance:

```bash
cd 06-seismology/04-earthquake-location-and-magnitude/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python velocity_model_dependence_demo.py
```

It builds a 117 × 10 travel-time table (117 depths from 1.0 to 30.0 km in
0.25 km steps, 10 distances) and reuses it for every experiment, so the whole
script runs in a few seconds without repeating a ray calculation.

Exercises:
[`exercises/02-velocity-model-dependence-exercises.md`](exercises/02-velocity-model-dependence-exercises.md)
and
[`exercises/02-velocity-model-dependence-solutions.md`](exercises/02-velocity-model-dependence-solutions.md).

> All models and data in this module are **SYNTHETIC**. The event, the network
> and the pick uncertainty are teaching values. The reference velocity model is
> used as a model and is not a measurement of any region.

## Mastery checkpoint

Without notes:

1. Show that replacing $v(\mathbf{x})$ by $s\,v(\mathbf{x})$ scales a travel
   time by $1/s$ and leaves the ray path unchanged.
2. Explain, using $\partial T/\partial z = z/(v r)$, why a faster locating model
   makes this regional event shallower.
3. Given $\sigma_z = 0.947\ \mathrm{km}$, compute the 95 per cent bound and state
   whether a $+2$ per cent velocity error lies inside it.
4. State the largest uniform velocity error these picks can absorb and contrast
   it with a realistic model error of 2 per cent.
5. Write one sentence that a catalogue entry could add to make its depth honest.

## Common pitfalls

1. **Quoting a depth without the velocity model.** The depth is conditional on
   it in the same way the ellipse is.
2. **Reading the error ellipse as total uncertainty.** It excludes model error,
   which for a 2 per cent velocity error is 2 to 3 times larger.
3. **Assuming the sign of the velocity bias is universal.** It follows from the
   correlation between travel time and depth sensitivity, which changes with the
   distance range.
4. **Reporting a grid-edge depth as a measurement.** "Depth = 30 km" with a grid
   that stops at 30 km is a statement about the grid.
5. **Trying to average the bias away.** The bias is common to all stations;
   more stations shrink the random part and leave the systematic part.
6. **Treating a joint inversion as free.** Every added parameter needs either
   independent data or a prior, or it only widens the null space.

## Related modules

- [01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses](01-hypocentre-location.md).
- [03 Relative Location: Master-Event, Double-Difference, HypoDD](03-relative-location.md) —
  what happens when the velocity error is common to a cluster and therefore
  cancels.
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — the other side
  of the same coin: using located events to improve the model.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md).
