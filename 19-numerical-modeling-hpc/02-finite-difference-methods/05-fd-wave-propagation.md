---
id: 19-02-05
title: "Finite-Difference Acoustic and Elastic Wave Propagation"
level: research
prereqs: ["19-02-02", "19-02-03", "19-02-04"]
tags: [numerical-modelling, hpc, wave-propagation, acoustic, elastic, staggered-grids, dispersion]
---

# Finite-Difference Acoustic and Elastic Wave Propagation

Everything derived in this folder now has to work at once: a stencil, a time
step, a boundary, a heterogeneous medium, and a source. This lesson builds a
two-dimensional fourth-order acoustic model, verifies its phase speed against the
discrete dispersion relation computed independently from the stencil, measures
the grid anisotropy in the same run, and measures a reflection coefficient
against the exact impedance contrast. The point is not that the code produces a
wavefield; it is that every number the code produces can be checked against
something derived. **All models and data in this module are SYNTHETIC.** Every
number quoted here is printed by `code/fd_wave_propagation_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** a two-dimensional fourth-order acoustic solver: stencil, source,
   time step and absorbing edges.
2. **Derive** the discrete dispersion relation
   $\cos(\omega\,dt) = 1 - C^{2}S/2$ of that scheme and **compute** the phase
   speed it predicts for a chosen direction and wavenumber.
3. **Measure** the phase speed in a run by unwrapping the spatial phase along a
   receiver line and fitting its slope, and **compare** it with the prediction.
4. **Quantify** the numerical anisotropy as the difference between the diagonal
   and the axis, and **explain** how it depends on resolution.
5. **Compute** the exact von Neumann limit of the two-dimensional fourth-order
   scheme and **verify** the measured growth rate just beyond it.
6. **Measure** a normal-incidence reflection and transmission coefficient in a
   staggered one-dimensional model and **show** that they converge to the exact
   impedance values.

## Prerequisites

- [19-02-02 High-Order and Compact Stencils; Staggered Grids](02-fd-stencils.md) —
  the fourth-order stencil and the staggered derivative used here.
- [19-02-03 Boundary Conditions: Dirichlet, Neumann, Absorbing, PML](03-fd-boundary-conditions.md) —
  the absorbing treatment that keeps the edges out of the answer.
- [19-02-04 Explicit vs Implicit Time Stepping and Stability Limits](04-fd-time-stepping.md) —
  the CFL analysis that sets $dt$.

## 1. Intuition: what a wavefield can and cannot tell you

A wavefield image looks like evidence. In fact it is the output of four
independent approximations stacked on top of one another: the stencil (phase
error and anisotropy), the time step (CFL and dispersion), the boundary (spurious
reflections), and the source (its own bandwidth). A modelling study that reports
arrival times without stating which of the four dominates has reported an
unattributed number.

The discipline that fixes this is to make the model's predictions checkable.
The discrete dispersion relation is such a prediction: given the stencil, the
time step and the wavenumber, it says what phase speed the run *must* produce.
If the run disagrees, one of the four approximations is not what you think. That
test is performed here before any geology enters the model.

## 2. Precise definitions

**Acoustic system.** With pressure $p$ and particle velocity $v$,
$\rho v_t = -\nabla p$, $p_t = -K\nabla\!\cdot\!v$, $K = \rho c^{2}$.

**Second-order pressure equation.** $\dfrac{1}{\rho c^{2}}p_{tt}
= \nabla\!\cdot\!\left(\dfrac{1}{\rho}\nabla p\right)$, which in a
constant-density medium reduces to $p_{tt} = c^{2}\nabla^{2}p$ — the form used
in the two-dimensional demonstration.

**Fourth-order Laplacian stencil (second derivative).**
$(-u_{i+2} + 16u_{i+1} - 30u_i + 16u_{i-1} - u_{i-2})/(12h^{2})$.

**Symbol of the negative Laplacian.** For a mode $e^{\mathrm i(k_xx+k_yy)}$ the
stencil returns $-S\,p$ with

$$S = \frac{30 - 32\cos(k_xh) + 2\cos(2k_xh)}{12}
    + \frac{30 - 32\cos(k_yh) + 2\cos(2k_yh)}{12}.$$

**Discrete dispersion relation.** Inserting a mode in the leapfrog pressure
update gives $\cos(\omega\,dt) = 1 - \tfrac12 C^{2}S$, hence
$\omega = \arccos(1 - C^{2}S/2)/dt$; the phase speed is $\omega/\lvert k\rvert$.

**Normal-incidence impedance.** $Z = \rho c$; the reflection and transmission
coefficients across an interface are

$$R = \frac{Z_2-Z_1}{Z_2+Z_1}, \qquad T = \frac{2Z_2}{Z_2+Z_1}.$$

## 3. Derivations

### 3.1 The scheme and its dispersion relation

Discretise $p_{tt} = c^{2}\nabla^{2}p$ with the fourth-order stencil in space and
the three-level centred difference in time:

$$p^{n+1} = 2p^{n} - p^{n-1} + C^{2}\,\mathsf L_4 p^{n},
\qquad
\mathsf L_4 u = \frac{1}{12}\sum_{\text{axes}}\left(-u_{+2}+16u_{+1}-30u
+16u_{-1}-u_{-2}\right),$$

where $\mathsf L_4$ is in units of $h^{2}$. Substituting
$p^{n}_{jk} = G^{n}e^{\mathrm i(k_xjh+k_ykh)}$:

$$G^{2} - 2\left(1 - \tfrac12C^{2}S\right)G + 1 = 0
\qquad\Longrightarrow\qquad
\omega\,dt = \arccos\!\left(1 - \tfrac12 C^{2}S\right).$$

In the small-$\theta$ limit $S \to (k_xh)^{2}+(k_yh)^{2} = (kh)^{2}$ and
$\omega\,dt \to Ckh$, i.e. $\omega \to ck$: consistent, as it must be. The
fourth-order stencil's next term is $+(\theta^{6})/90$ per axis, so $S$ slightly
*exceeds* $(\theta)^{2}$ at moderate $\theta$, which means the discrete phase
speed slightly exceeds $c$ before dropping below it at the coarsest resolutions —
the measured table below shows both sides of that crossover.

### 3.2 Measuring the phase speed in a run

A phase-speed measurement needs (i) a narrow-band source so that a single
wavenumber is meaningful, (ii) a *line* of receivers so that the spatial phase
can be unwrapped cell by cell rather than resolved modulo $2\pi$, and (iii) a
time window in which the field is steady.

The demonstration uses a monochromatic point source with a Gaussian spatial
envelope of half-wavelength width, 40 periods of run time, and 60 receivers
spaced one cell apart along the ray; each trace is projected onto
$e^{-\mathrm i\omega_0t}$ with a Hann window, the phase is unwrapped along the
ray, and its slope is $k_{\text{num}}$. The result:

| PPW | $f_0$ (Hz) | axis $v_{\text{num}}/c$ | predicted | diagonal | predicted | diagonal − axis % |
|---|---|---|---|---|---|---|
| 4 | 25.00 | 0.98989001 | 0.98825285 | 1.01615039 | 1.00921889 | 2.65286 |
| 8 | 12.50 | 1.00206249 | 1.00213077 | 1.00360724 | 1.00363795 | 0.15416 |
| 16 | 6.25 | 0.99983721 | 1.00090022 | 1.00153672 | 1.00099804 | 0.16998 |

The prediction comes from the stencil alone (§3.1) and is evaluated at the
carrier wavenumber; agreement is $0.2\,\%$ at PPW $= 4$ and $0.01\,\%$ at
PPW $= 8$. The axis speed also changes sign of its error with resolution: it is
$1.1\,\%$ *below* the continuum at PPW $=4$, $0.2\,\%$ *above* it at PPW $=8$,
and $0.02\,\%$ below it at PPW $=16$. That crossover is a property of the
fourth-order stencil's sixth-order symbol term, and it is the reason a
fourth-order code can be slightly *fast* rather than uniformly slow — an
important distinction when an apparent structural dip is really a numerical
phase error.

The diagonal is consistently faster than the axis — by $2.65\,\%$ at PPW $=4$ and
$0.15\text{–}0.17\,\%$ at PPW $\ge 8$. This is grid anisotropy measured in a
wavefield, not in a symbol table, and it is the practical form of the result of
[19-01-04](../01-numerical-foundations/04-numerical-dispersion-diffusion.md).

### 3.3 The exact von Neumann limit of the 2-D fourth-order scheme

The growth factor has modulus one whenever the radicand
$1-(1-C^{2}S/2)^{2}\ge0$, i.e. while $C^{2}S/2 \le 2$ for every mode. $S$ is
maximised at the Nyquist corner $k_xh = k_yh = \pi$:

$$S_{\max} = 2\times\frac{30 - 32(-1) + 2(1)}{12}
= 2\times\frac{64}{12} = 10.666667,
\qquad
C_{\max} = \frac{2}{\sqrt{S_{\max}}} = 0.612372.$$

For the five-point second-order stencil $S_{\max} = 8$ and the familiar
$C_{\max} = 1/\sqrt2 = 0.707107$. The fourth-order stencil is therefore
*stricter* — a real cost of the wide stencil that is often forgotten. Measured
against the prediction, starting in the pure Nyquist eigenmode:

| $C$ | predicted $\lvert G\rvert$ | measured growth/step | stable? |
|---|---|---|---|
| 0.5500 | 1.00000000 | 1.00000000 | yes |
| 0.6000 | 1.00000000 | 1.00000000 | yes |
| 0.6124 | 1.01915738 | 1.01915738 | no |
| 0.6500 | 2.00887582 | 2.00887582 | no |
| 0.7000 | 2.87936826 | 2.87936826 | no |

The limit itself is reproduced to four figures: $C = 0.6124$ is already unstable
and $0.6000$ is not.

### 3.4 Reflection and transmission at an interface

The two-dimensional *travel-time* test above says nothing about amplitudes, so
the reflection coefficient is measured in a one-dimensional staggered model where
the geometry is unambiguous:

$$v_t = -\tfrac{1}{\rho}p_x, \qquad p_t = -\rho c^{2}v_x,$$

with the source at $5\lambda$, a receiver in front of the interface at $8\lambda$,
the interface at $15\lambda$, and a receiver behind it at $25\lambda$. The
scattered field is isolated by differencing the layered run against a uniform
run, which removes both the direct arrival and the reflection from the domain
end. With $\rho_1 = 1$, $c_1 = 1$, $\rho_2 = 1.2$, $c_2 = 1.5$:

$$Z_1 = 1.00,\quad Z_2 = 1.80,\quad
R_{\text{exact}} = 0.285714,\quad T_{\text{exact}} = 1.285714.$$

| cells per wavelength | measured $R$ | $R$ error % | measured $T$ | $T$ error % |
|---|---|---|---|---|
| 8 | 0.204728 | $-28.35$ | 1.137387 | $-11.54$ |
| 16 | 0.218459 | $-23.54$ | 1.048296 | $-18.47$ |
| 32 | 0.276858 | $-3.10$ | 1.256081 | $-2.30$ |
| 64 | 0.285424 | $-0.10$ | 1.283070 | $-0.21$ |

At 64 cells per wavelength the measured coefficients are within $0.2\,\%$ of the
impedance values, and the convergence is monotone in resolution. The two things
this measurement buys are a calibration of the amplitude accuracy of the scheme
(a number a wavefield image cannot give you) and a demonstration that the
staggered placement of $\rho$ at the velocity nodes is what makes the interface
transparent to the coefficient rather than to an average.

Note the error at 8 cells per wavelength: $-28\,\%$ on the reflection. A
one-dimensional test at coarse resolution is not a formality — it is the fastest
way to discover that an amplitude measurement needs more resolution than an
arrival-time measurement of the same wavefield.

## 4. Worked example: budgeting errors for a 2-D survey

*A 2-D acoustic model is planned with the fourth-order scheme of §3.1, $c = 3000\
\mathrm{m\,s^{-1}}$, a 25 Hz source, and a target phase error of $0.5\,\%$.*

1. Wavelength: $\lambda = c/f = 120$ m.
2. Phase error at PPW $=8$ from the measured table: $0.21\,\%$ on the axis and
   $0.36\,\%$ on the diagonal — inside the target. At PPW $=4$ it is $1.0\,\%$
   and $1.6\,\%$ — outside.
3. Choose $h = \lambda/8 = 15$ m, then check the CFL limit:
   $dt \le C_{\max}h/c = 0.612\times15/3000 = 3.06\times10^{-3}$ s. Use
   $dt = 2.5\times10^{-3}$ s ($C = 0.5$) for margin.
4. Domain for a 10 km × 10 km survey: $667\times667$ cells, $4.4\times10^{5}$
   unknowns, three field copies at float64 $\approx10.7$ MB — comfortable.
   Time to $6$ s (four seconds of record plus
   source delay): $2400$ steps.
5. Boundary: the sponge calibration of
   [19-02-03](03-fd-boundary-conditions.md) requires either a wide layer or a
   windowed record; budget 40–80 cells of layer and place no receiver closer than
   one wavelength to it.
6. State all four error sources with numbers at the end: stencil phase
   $0.2$–$0.4\,\%$, anisotropy $0.15\,\%$, CFL-driven temporal dispersion
   $O(C^{2})\lesssim0.1\,\%$, boundary reflection to be measured. A report that
   lists only the first is incomplete by construction.

## 5. Assumptions and regime of validity

1. **Constant density in the 2-D model.** The displayed two-dimensional scheme
   solves $p_{tt} = c^{2}\nabla^{2}p$; for variable density the divergence form
   of §3.4 must be used, or the interface amplitudes will be wrong.
2. **Isotropic, isotropic medium.** The measured anisotropy is the *grid's*, not
   the rock's; intrinsic anisotropy of the medium would add to it and cannot be
   separated by a single isotropic test.
3. **Narrow-band sources for phase measurements.** The measured $v_{\text{num}}$
   is a phase speed at the carrier wavenumber; a broadband source has no single
   carrier and the measurement degrades.
4. **The measurement window must exclude wrap-around.** The demonstration damps
   the edges precisely so that the steady-state window contains only the outgoing
   wave; without that, a periodic grid's wrap-around arrival can exceed the
   direct one.
5. **The CFL limit depends on the stencil.** $C_{\max} = 0.6124$ for the
   fourth-order 2-D stencil against $0.7071$ for the five-point one; copying a
   time step from a second-order code is a stability bug.
6. **Reflection measurements are normal-incidence.** The staggered 1-D test gives
   $R$ and $T$ for normal incidence only; oblique incidence adds mode conversion
   and angle-dependent coefficients that this test does not see.

## 6. Python demonstration

`code/fd_wave_propagation_demo.py` prints:

1. the phase-speed measurement along the axis and the diagonal against the
   dispersion relation of the stencil, at three resolutions;
2. the anisotropy difference between the two directions;
3. the exact von Neumann limit $C_{\max} = 0.612372$ with measured growth rates
   on both sides;
4. the reflection and transmission coefficients at four resolutions converging to
   $0.285714$ and $1.285714$.

```bash
cd 19-numerical-modeling-hpc/02-finite-difference-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python fd_wave_propagation_demo.py
```

## Mastery checkpoint

Without notes:

> A 2-D fourth-order acoustic model runs at 12 points per wavelength with
> $C = 0.55$. **(a)** State whether it is stable and justify with the limit.
> **(b)** Predict roughly the phase error on the axis and on the diagonal, using
> the measured table, and say which of the two dominates a travel-time
> measurement between two points separated diagonally. **(c)** A reflector at
> 1200 m depth is imaged: describe how you would verify the *amplitude* of the
> reflection rather than its arrival time, and what a $-20\,\%$ amplitude error
> at 12 points per wavelength would imply. **(d)** Name the three other error
> sources that must be reported alongside the stencil error.

Parts (a)–(c) are worked in
[`exercises/05-fd-wave-propagation-solutions.md`](exercises/05-fd-wave-propagation-solutions.md).

## Common pitfalls

1. **Believing the picture.** A wavefield can look physical while carrying a
   $28\,\%$ amplitude error.
2. **Copying a time step between schemes.** The fourth-order stencil's CFL limit
   is $13\,\%$ stricter than the five-point one.
3. **Measuring phase speed with a broadband source or two receivers.** Unwrap
   along a line with a narrow-band source, or measure nothing.
4. **Leaving the boundaries periodic.** The wrap-around arrival can dominate the
   direct one; damp the edges and window the record.
5. **Assuming anisotropy is small because the stencil is fourth order.** It is
   $2.65\,\%$ at four points per wavelength.
6. **Forgetting that a staggered scheme needs the material property where the
   field is.** Density belongs at the velocity nodes; averaging it onto them
   re-creates the interface error the staggering removed.

## Related modules

- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  the stencil-level origin of the measured anisotropy.
- [19-02-06 FD for Diffusion, Laplace and Poisson Problems](06-fd-diffusion-and-potential.md) —
  the steady-state counterpart of the same discretisations.
- [06-01-01 From Hooke's Law and Newton to the Elastodynamic Equation](../../06-seismology/01-elastic-wave-propagation/01-wave-equation-elastic.md) —
  the elastic equations the acoustic model approximates.
- [19-08 Simulating a 2-D/3-D Seismic Wavefield](../08-geophysical-simulation-case-studies/01-simulate-seismic-wavefield.md).
- [Module 19-02 Finite-Difference Methods](README.md).

Exercises and worked solutions:
[`exercises/05-fd-wave-propagation-exercises.md`](exercises/05-fd-wave-propagation-exercises.md)
and
[`exercises/05-fd-wave-propagation-solutions.md`](exercises/05-fd-wave-propagation-solutions.md).
