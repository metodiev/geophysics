---
id: 08-04-04
title: "MT Inversion: 1-D, 2-D and 3-D Approaches"
level: research
prereqs: ["08-04-02", "18-03-02"]
tags: [electromagnetism, geomagnetism, magnetotellurics, inversion, occam, regularization, resolution]
---

# MT Inversion: 1-D, 2-D and 3-D Approaches

An MT inversion turns apparent-resistivity and phase curves into a conductivity
model. This lesson builds a complete 1-D Occam inversion from the recursion of
[02](02-magnetotellurics.md), uses it on synthetic data whose structure is known,
and measures three things that a published MT model usually states only
qualitatively: how much the answer depends on the regularisation, how badly a
thin layer is smeared, and how completely a static shift is absorbed into the
structure. The lesson closes with what a 2-D or 3-D inversion adds and what it
does not.

> All models and data in this module are **SYNTHETIC**.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** the 1-D MT inverse problem, including the parametrisation, the
   data vector and the misfit.
2. **Implement** a Gauss–Newton step with a roughness penalty and **explain** why
   a line search is needed.
3. **Compute** the misfit-versus-roughness trade-off and **select** a
   regularisation parameter with a stated criterion.
4. **Quantify** the smearing of a thin conductor and **show** that its
   *conductance* survives while its thickness does not.
5. **Demonstrate** conductance equivalence for three different models fitting the
   same data.
6. **Measure** the effect of a static shift on the inverted model.
7. **State** what 2-D and 3-D inversions add, what they cost, and which of the
   1-D conclusions survive.

## Prerequisites

- [08-04-02 Magnetotellurics](02-magnetotellurics.md) — the forward model and the
  data functionals.
- [18-03-02 Tikhonov Regularization](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the penalty and parameter-choice theory used here.

## 1. The inverse problem

**Parametrisation.** $M$ layers of fixed thickness, each with a resistivity
$\rho_j > 0$. Inverting for $\log_{10}\rho_j$ keeps the model positive without
constraints and makes the sensitivity roughly scale-free.

**Data.** At $N$ periods, the log-amplitude and the phase of $Z$:

$$\mathbf{d} = \left(\ln\left|Z_1\right|,\dots,\ln\left|Z_N\right|,
\phi_1,\dots,\phi_N\right), \qquad \phi = \arg Z .$$

Using $\ln\left|Z\right|$ rather than $\left|Z\right|$ makes the misfit
approximately Gaussian in the presence of multiplicative noise, and it makes the
amplitude and phase contributions comparable in size.

**Model.** $\mathbf{m} = \left(\log_{10}\rho_1,\dots,\log_{10}\rho_M\right)$, with
forward operator $\mathbf{F}(\mathbf{m})$ given by the recursion of
[02](02-magnetotellurics.md).

**Objective.**

$$\Psi(\mathbf{m}) = \frac{1}{N_{\text{d}}}\left\|\mathbf{d}-\mathbf{F}(\mathbf{m})\right\|^{2}
+ \mu\left\|\mathbf{D}\mathbf{m}\right\|^{2}, \qquad
\mathbf{D} = \text{first-difference operator},$$

where the data term is the mean squared misfit and $\mu$ is the trade-off
parameter. **Regularisation is not optional:** the MT inverse problem is
non-linear and its data are smooth functions, so without a penalty the inversion
will construct oscillations that fit noise — as Section 4 will show.

**Linearisation.** At each iteration, with $\mathbf{J} = \partial\mathbf{F}/
\partial\mathbf{m}$ computed by finite differences,

$$\left(\mathbf{J}^{T}\mathbf{J} + \mu\mathbf{D}^{T}\mathbf{D}\right)\delta\mathbf{m}
= \mathbf{J}^{T}\mathbf{r} - \mu\mathbf{D}^{T}\mathbf{D}\mathbf{m},$$

and $\mathbf{m}\leftarrow\mathbf{m}+\alpha\delta\mathbf{m}$ with a step length
$\alpha$ chosen by a backtracking line search. The line search is not
cosmetic: the model is parametrised in $\log_{10}\rho$, the forward operator is
exponential in the model, and an unconstrained Gauss–Newton step readily drives a
layer to $10^{\pm 30}$ and the misfit to NaN. Bounding the model and requiring the
objective to decrease at each step is what makes the algorithm usable, and both
were needed in the demonstration.

## 2. A synthetic test model

A four-layer model, quoted as resistivity and thickness above the half-space:

| Layer | $\rho$ ($\Omega$m) | Thickness |
|---|---|---|
| 1 | 200 | 1 km |
| 2 | 20 | 2 km |
| 3 | 400 | 5 km |
| half-space | 50 | — |

Data are computed at 24 periods logarithmically spaced from $0.01$ to $1000$ s.
Gaussian noise is added to the 48-element data vector with
$\sigma = 0.02\times$ the spread of the clean data, giving
$\sigma = 0.05885$ in the same units — a 2% multiplicative uncertainty, which is
optimistic but not unrealistic for a good site.

The response (apparent resistivity and phase) is the model's *observable*, not
the model: a reader comparing two models should compare these curves.

## 3. The trade-off, measured

Running the inversion for eight values of $\mu$, 60 Gauss–Newton iterations each:

| $\mu$ | rms misfit | Model roughness | Conductance of the conductor (S) |
|---|---|---|---|
| $10^{-7}$ | 0.06087 | 3.6499 | 116.67 |
| $10^{-6}$ | 0.06089 | 2.6469 | 115.16 |
| $10^{-5}$ | 0.06099 | 1.8016 | 109.69 |
| $10^{-4}$ | 0.06143 | 1.2415 | 102.81 |
| $10^{-3}$ | 0.06268 | 1.0396 | 97.01 |
| $10^{-2}$ | 0.07689 | 0.7877 | 81.66 |
| $10^{-1}$ | 0.15181 | 0.3383 | 49.91 |
| $1$ | 0.22198 | 0.0726 | 34.95 |

The noise level is $\sigma = 0.05885$, and the smallest misfit achieved is
$0.06087$ — a fit at the noise level, as it should be. Two observations:

- over **four decades** of $\mu$ (from $10^{-7}$ to $10^{-4}$) the misfit is
  essentially unchanged while the roughness falls by a factor of 3. Models inside
  that band are indistinguishable; the regularisation is choosing among them, not
  being constrained by the data;
- the *conductance* of the conductive layer nevertheless moves from 117 S to
  103 S across that band, which is the honest uncertainty on a quantity that
  people often quote to three digits.

**Choosing $\mu$.** The Occam criterion used here — take the *smoothest* model
whose misfit is within 10% of the best achieved — selects $\mu = 10^{-3}$, with a
misfit of $0.06268$, a conductance of 97.01 S, and the recovered model

$$219.9,\ 33.4,\ 15.9,\ 35.5,\ 69.7,\ 108.4,\ 139.5,\ 154.7,\ 152.4,\ 136.1,\
112.5,\ 87.8,\ 66.9,\ 52.1\ \Omega\mathrm{m}$$

in 14 layers of $0.8$ km. Compare with the truth ($200$, $20$, $400$ then $50$):
the first layer is right to 10%, the conductor is right in *conductance* (97.01 S
against 100 S) but its resistivity is spread over three layers, and the resistive
layer at 5–10 km is smeared into a broad high-resistivity plateau. This is what a
1-D MT inversion of good data actually produces.

## 4. Resolution: what survives and what does not

**The thin layer is smeared; its conductance is not.** The true 20 $\Omega$m layer
is 2 km thick with $S = 2000/20 = 100$ S. The inverted model puts
$33.4$, $15.9$ and $35.5\ \Omega$m in successive 0.8 km layers, with a
total conductance of 97.01 S: **97% of the truth in the integral, and no
information at all in the profile.** Reporting "a 2 km thick layer of
20 $\Omega$m" from this inversion would be over-claiming; reporting "a
conductance of $100\pm10$ S between about 1 and 4 km depth" would be honest.

**Different models with the same conductance fit equally well.**

| Model | rms misfit | Conductance (S) |
|---|---|---|
| Truth: 20 $\Omega$m over 2 km | 0.06176 | 100 |
| 10 $\Omega$m over 1 km | 0.08415 | 100 |
| 40 $\Omega$m over 4 km | 0.11518 | 100 |

All three fit at roughly the noise level; the misfit differences (0.062, 0.084,
0.115) are small compared with the model differences (a factor of four in
resistivity and in thickness). The data constrain the conductance; the split
between thickness and resistivity comes from *where in period* the response bends
away from the thin-sheet limit, and for a layer this thin that lever arm is
short.

**Why a smoother model is physically reasonable, and why it is still a choice.**
Smoothness is a prior, defended by the argument that real conductivity structure
is unlikely to oscillate with depth. It is a good prior; it is not information
from the data. When the prior is wrong — a genuinely sharp interface — the
inversion produces a gradual transition, and only forward modelling of a sharp
alternative can test whether the data reject it.

## 5. The static shift

Multiply the synthetic impedance by $s = 1.6$ (a plausible galvanic distortion at
a real site), add fresh noise, and invert with the same $\mu$:

| Quantity | Unshifted | Shifted |
|---|---|---|
| $\rho_a$ at the longest period ($\Omega$m) | 51.89 | 132.84 |
| Phase at the longest period (deg) | 45.788 | 45.788 |
| rms misfit after inversion | 0.06268 | 0.04764 |
| Inverted layer 1 ($\Omega$m) | 219.9 | 515.6 |
| Inverted layer 2 ($\Omega$m) | 33.4 | 519.3 |

The shifted data are fitted *better* than the unshifted data (0.048 against
0.063), and the model that fits them is wrong by a factor of 2.3 in the top layer
and by a factor of 15 in the second. The phase was untouched, and the inversion
still absorbed the amplitude change into structure. **A static shift is not a
noise problem and cannot be averaged or processed away**; it must be removed by
an independent measurement, jointly inverted with a shift parameter per station,
or accepted as an unknown in the final interpretation.

## 6. What 2-D and 3-D inversion add

| | 1-D | 2-D | 3-D |
|---|---|---|---|
| Forward solver | Recursion (this lesson) | Finite difference/element in $(x,z)$ | Full 3-D, usually finite difference |
| Data used | One station | Profile, TE and TM | Array, full tensor plus tipper |
| Cost | Milliseconds | Minutes to hours | Hours to days per inversion |
| Regularisation | Roughness in $z$ | Roughness in $(x,z)$ | Roughness in $(x,y,z)$ |
| Adds | Depth structure | Lateral structure, strike, the TE/TM split | Full geometry, arbitrary strike |
| Does not add | — | Uniqueness, or freedom from static shift | Uniqueness, or freedom from static shift |

Three points that survive the generalisation:

1. **The trade-off remains.** Each $\mu$ produces a different model, and the
   misfit surface is flat over decades of $\mu$ — more so in 3-D, where the
   null space is larger.
2. **Conductance remains better determined than resistivity.** The equivalence of
   Section 4 is a property of diffusive physics, not of the 1-D assumption.
3. **The static shift remains.** In 2-D and 3-D inversions, one station's shift is
   usually inverted as an unknown; ignoring it produces long-wavelength striping
   along the profile.

## 7. Assumptions and regime of validity

1. **The noise model.** Gaussian, additive in $(\ln|Z|,\phi)$; the choice of
   regularisation parameter depends on it. Wrong noise gives a wrong $\mu$, but
   not a wrong family.
2. **The parametrisation bounds.** Model resistivities were bounded in
   $[0.1,10^{6}]\ \Omega$m; unbounded, the algorithm diverges, and the bounds are
   themselves a prior.
3. **Fixed layer thicknesses.** The inversion cannot sharpen an interface beyond
   the layer size. That is a *choice* that limits the achievable resolution, and it
   is why finer grids need more regularisation.
4. **Adequate period coverage.** The inversion can only resolve structure in the
   depth range its periods reach; extrapolating an inverted model outside its band
   is unsupported.
5. **1-D structure.** For real 2-D or 3-D data, a 1-D inversion of each station
   returns different, orientation-dependent answers, and the differences are
   real information about the departure from layering rather than noise.
6. **The starting model does not matter *if* the misfit surface is well
   behaved.** Non-linear MT inversion can settle in local minima; multi-start or
   a global search is the standard defence, and the demonstration's line search
   is a partial one.

## 8. Python demonstration

`code/mt_inversion_demo.py`:

1. computes the response of a synthetic four-layer model at 24 periods;
2. inverts with a Gauss–Newton scheme, a roughness penalty and a line search, for
   eight values of $\mu$;
3. tabulates misfit, roughness and conductance, and applies the Occam criterion;
4. prints the recovered 14-layer model and compares its conductance with the
   truth;
5. fits three different models with the same conductance and reports the misfits;
6. applies a $\times1.6$ static shift and shows the resulting model and misfit.

```bash
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mt_inversion_demo.py
```

Fixed seed, print-only, exits 0.

## 9. Exercises

[`exercises/04-mt-inversion-exercises.md`](./exercises/04-mt-inversion-exercises.md)
and
[`exercises/04-mt-inversion-solutions.md`](./exercises/04-mt-inversion-solutions.md).

## Mastery checkpoint

Without notes:

> A **synthetic** MT data set has 1% phase noise and 3% amplitude noise, and its
> inverted model shows a conductor of 50 $\Omega$m between 3 and 5 km.
> **(a)** State which of these two numbers the data constrain better and why.
> **(b)** Compute the conductance and state the depth range over which it is
> constrained. **(c)** An independent TEM sounding gives $\rho_a$ a factor of two
> lower at the same periods. State what you would change in the inversion and
> what you would *not* change. **(d)** State the criterion you would use to
> choose $\mu$ and what makes it defensible. **(e)** State one statement a report
> of this inversion must not make.

## Common pitfalls

1. **Reporting the inverted model as the Earth.** The information is in the
   conductance and the depth range.
2. **Choosing $\mu$ for a pretty picture.** State the criterion and the noise
   level.
3. **Reading an interface position from a smooth model.** The transition width is
   largely the regularisation, not the Earth.
4. **Fitting the static shift with structure.** The fit improves and the model
   gets worse.
5. **Comparing misfits between different parametrisations or data sets.**
6. **Extrapolating outside the period band.** Nothing in the data supports it.

## Related modules

- [02 Magnetotellurics](02-magnetotellurics.md) — the forward model inverted here.
- [03 MT Processing](03-mt-processing.md) — the estimate that goes into the
  inversion, and its biases.
- [05 MT Interpretation](05-mt-interpretation.md) — what the resulting
  conductivity means.
- [18-03 Regularization](../../18-inverse-problems/03-regularization/README.md) —
  the general theory, including parameter choice.
- [19-08 Geophysical Simulation Case Studies](../../19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/README.md) —
  2-D and 3-D forward solvers of the kind a 2-D inversion iterates.
