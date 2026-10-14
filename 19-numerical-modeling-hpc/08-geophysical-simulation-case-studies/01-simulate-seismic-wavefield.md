---
id: 19-08-01
title: "Simulating a 2-D/3-D Seismic Wavefield"
level: research
prereqs: ["19-02-05", "19-07-01", "19-07-02"]
tags: [numerical-modelling, verification, seismic-wavefield, finite-difference, numerical-dispersion, cfl]
---

# Simulating a 2-D/3-D Seismic Wavefield

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the exact discrete dispersion relation of the second-order leapfrog
   scheme and the group velocity it implies, from a plane-wave substitution.
2. **Measure** the numerical group velocity of a simulated pulse and **compare** it
   with the analytic prediction at stated points per wavelength.
3. **Derive** the stability limits $C \le 1$ (1-D) and $C \le 1/\sqrt{2}$ (2-D) and
   **verify** both against measured amplitude growth.
4. **Quantify** grid anisotropy from the exact discrete dispersion relation, and
   **state** the resolution at which it falls below a stated tolerance.
5. **Estimate** the cost of the same simulation in three dimensions, in nodes,
   floating-point operations and memory traffic, and **decide** whether it is
   feasible on a stated machine.
6. **Report** a wavefield simulation with its dispersion error, its stability
   margin and its boundary treatment stated, rather than as a picture.

## Prerequisites

- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](../02-finite-difference-methods/05-fd-wave-propagation.md)
  — the scheme used here.
- [19-07-01 Code Verification: Order-of-Accuracy and Manufactured Solutions](../07-verification-validation-uncertainty/01-code-verification.md)
  — the discipline this lesson applies to a wavefield.
- [19-07-02 Solution Verification](../07-verification-validation-uncertainty/02-solution-verification.md)
  — how to attach an error to a modelled travel time.
- [19-01-04 Numerical Dispersion, Dissipation and Grid Anisotropy](../01-numerical-foundations/04-numerical-dispersion-diffusion.md)
  — the general theory of the error measured here.

All models and data in this module are **SYNTHETIC**: a chosen velocity, frequency
and grid. No real survey, station, event or waveform is used, and every number is
printed by this lesson's demonstration.

## 1. Intuition: a wavefield is a claim about travel times

A seismic wavefield simulation exists to produce *arrival times and amplitudes* at
receivers, and every decision made from it — a depth, a velocity, an image — is a
function of those arrivals. That is what makes the numerical dispersion of a
finite-difference scheme a modelling error rather than a cosmetic one. The scheme
does not propagate all frequencies at the medium velocity. It propagates the short
wavelengths at the wrong speed, and it therefore places reflectors at the wrong
depth, with an error that is smooth, systematic and invisible in a snapshot.

The first thing to establish, then, is not "does the wavefield look like a wave",
which it always does, but **how fast the numerical wave travels compared with the
medium**. That question has an exact answer for the standard scheme: substituting a
plane wave into the update gives a *discrete* dispersion relation, not an
approximation of the continuum one but the exact relation for the scheme. The
simulation can then be scored against it, which is code verification in the sense
of [19-07-01](../07-verification-validation-uncertainty/01-code-verification.md),
applied to a quantity a seismologist actually cares about.

The second thing is stability. An explicit scheme has a hard stability limit — not
a safety margin, a cliff — and it is set by the sound speed, the grid spacing and
the time step. The demonstration measures the cliff to three digits in one and two
dimensions, and it is worth seeing once, because the failure mode above the limit
is not a small error but an overflow within a few hundred steps.

## 2. Definitions

**Acoustic wave equation.** With pressure $p$, velocity $c$ and density $\rho$
constant, $\partial_t^2 p = c^{2}\nabla^{2}p$. The scheme below discretises this
second-order form and needs two time levels.

**Courant number.** $C = c\,\Delta t/h$, the distance the wave moves per time step
in units of the grid spacing. The stability limit is expressed in it.

**Points per wavelength.** $\mathrm{ppw} = \lambda/h$ at a stated frequency, with
$\lambda = c/f$. It is the single number that predicts the dispersion error.

**Numerical phase and group velocity.** The speed at which a monochromatic wave's
phase, and a packet's envelope, travel in the discrete scheme. They differ from
each other and from $c$; the group velocity is what a travel-time pick measures.

**Grid anisotropy.** The dependence of the numerical velocity on propagation
direction at fixed wavelength, arising because the five-point stencil is not
rotationally symmetric.

**Absorbing boundary.** A boundary condition that lets outgoing energy leave
rather than reflecting. Its quality is a modelling choice, and an imperfect one
contaminates the same arrivals the dispersion error does.

## 3. Derivations

### 3.1 The scheme and its exact dispersion relation

The explicit second-order scheme in one dimension is

$$p_i^{n+1} = 2p_i^{n} - p_i^{n-1}
+ C^{2}\left(p_{i-1}^{n} - 2p_i^{n} + p_{i+1}^{n}\right), \qquad C = \frac{c\,\Delta t}{h}.$$

Substitute the plane wave $p = e^{\mathrm{i}(k x_i - \omega t_n)}$:

$$e^{\mathrm{i}\omega\Delta t} - 2 + e^{-\mathrm{i}\omega\Delta t}
= C^{2}\left(e^{\mathrm{i}kh} - 2 + e^{-\mathrm{i}kh}\right),$$

$$-4\sin^{2}\!\left(\frac{\omega\Delta t}{2}\right)
= -4C^{2}\sin^{2}\!\left(\frac{kh}{2}\right)
\quad\Longrightarrow\quad
\boxed{\;\sin\!\left(\frac{\omega\Delta t}{2}\right)
= C\sin\!\left(\frac{kh}{2}\right).}$$

This is exact for the scheme. It has three consequences used below.

- **Stability.** A real $\omega$ exists only if $C\sin(kh/2) \le 1$ for every
  representable $k$, i.e. $C \le 1$: the 1-D limit. In two dimensions the same
  substitution with the five-point Laplacian gives
  $C \le 1/\sqrt{2}$, because the Laplacian's largest eigenvalue is now twice the
  one-dimensional one at the corner wavenumber.
- **Dispersion.** With $\theta = kh$ and $C$ fixed, the numerical phase speed is
  $c_{\text{num}}/c = \omega/(ck) = 2\arcsin(C\sin(\theta/2))/(C\theta)$, which is
  less than $1$ and tends to $1 - (1-C^{2})\theta^{2}/24$ for small $\theta$.
  The error is second order in the *resolution*, not in $h$ alone: halving $h$ at
  fixed frequency quarters it.
- **Group velocity.** Differentiating $\omega(k)$:

$$\frac{c_g}{c} = \frac{\cos(\theta/2)}{\sqrt{1 - C^{2}\sin^{2}(\theta/2)}},$$

which is the quantity a pulse timing measures.

### 3.2 Why the two-dimensional limit is smaller

For the five-point Laplacian the symbol is
$-\left(\frac{4}{h^{2}}\right)\left[\sin^{2}(k_xh/2) + \sin^{2}(k_yh/2)\right]$,
whose magnitude is largest when both sines are $1$, i.e. at the corner
wavenumbers $k_x = k_y = \pi/h$. The stability condition then reads
$C^{2}\cdot 2 \le 1$, so $C \le 1/\sqrt{2} = 0.70711$ — a factor $1.414$ smaller
than in one dimension. Nothing about the physics changed; the stencil did.

### 3.3 What three dimensions cost

An explicit scheme touches about seven field-size arrays per step (two old time
levels, one new, plus temporaries). Per node that is about seven flops and
$7\times8 = 56$ bytes of traffic. The consequences for a real survey are worked in
Section 8; they are the reason seismic modelling is a high-performance computing
subject rather than a scripting exercise
([19-06-01](../06-hpc-and-parallel-computing/01-hpc-architecture.md)).

## 4. Measured evidence

The demonstration `code/simulate_seismic_wavefield_demo.py` uses a synthetic medium
with $c = 3000$ m/s and a Ricker source with $f_0 = 15$ Hz (dominant wavelength
200 m), a 20 km periodic domain and a Courant number of $0.5$.

### 4.1 Measured pulse velocity against the exact prediction

| ppw | $\Delta x$ (m) | $\Delta t$ (s) | measured $c_g/c$ | analytic $c_g/c$ | difference (%) |
|---:|---:|---:|---:|---:|---:|
| 4 | 50.0 | $8.33\times10^{-3}$ | 0.84433 | 0.75593 | +11.69 |
| 6 | 33.3 | $5.56\times10^{-3}$ | 0.94675 | 0.89443 | +5.85 |
| 8 | 25.0 | $4.17\times10^{-3}$ | 0.95808 | 0.94127 | +1.79 |
| 12 | 16.7 | $2.78\times10^{-3}$ | 0.99174 | 0.97412 | +1.81 |
| 20 | 10.0 | $1.67\times10^{-3}$ | 0.98462 | 0.99072 | −0.62 |
| 32 | 6.2 | $1.04\times10^{-3}$ | 0.99805 | 0.99638 | +0.17 |

Two readings matter. First, the analytic relation is the right reference: at 8–32
points per wavelength the measured and predicted values agree to $0.2$–$1.8$ per
cent, the residual being the finite-bandwidth group delay of a Ricker pulse
measured at a single frequency. Second, **the error is large**: at $4$ points per
wavelength the pulse travels at $0.84c$, a $16$ per cent velocity error that would
place a $3$ km reflector about $480$ m too deep. The rule of thumb that emerges
from the table is that $10$ points per wavelength buys roughly one per cent, and
that resolving to $0.2$ per cent needs about $30$.

### 4.2 The stability limits, measured

One dimension, amplitude after 200 steps from a point source:

| $C$ | $\max\lvert p\rvert$ growth |
|---:|---:|
| 0.50 | 1.0000 |
| 0.90 | 1.0000 |
| 0.99 | 1.0512 |
| 1.00 | 7.0000 |
| 1.01 | $2.37\times10^{23}$ |
| 1.05 | $2.41\times10^{53}$ |

Two dimensions, same experiment on a $48\times48$ grid:

| $C$ | $\max\lvert p\rvert$ after 200 steps |
|---:|---:|
| 0.600 | 1.0000 |
| 0.700 | 1.0000 |
| 0.7071 | 1.0000 |
| 0.720 | $1.03\times10^{15}$ |
| 0.800 | $6.56\times10^{70}$ |

The measured cliffs sit at $C = 1$ and at $C = 1/\sqrt{2} = 0.70711$, the exact
values from Section 3. The margin is not a safety factor: at $C = 0.99$ the
amplitude has already grown $5$ per cent in 200 steps, and one step above the
limit the run is destroyed. **Any production run must state its Courant number and
the limit it is compared with**, because "it ran" and "it will finish" are not the
same claim.

### 4.3 Grid anisotropy

From the exact two-dimensional discrete relation
$\sin^{2}(\omega\Delta t/2) = C^{2}\left[\sin^{2}(k_xh/2) + \sin^{2}(k_yh/2)\right]$
at $C = 0.5$:

| ppw | $c_{\text{num}}/c$ at $0^\circ$ | $15^\circ$ | $30^\circ$ | $45^\circ$ | anisotropy |
|---:|---:|---:|---:|---:|---:|
| 8 | 0.98054 | 0.98379 | 0.99027 | 0.99349 | 1.312% |
| 16 | 0.99517 | 0.99597 | 0.99758 | 0.99839 | 0.323% |
| 32 | 0.99879 | 0.99900 | 0.99940 | 0.99960 | 0.080% |

The fastest direction is $45^\circ$ to the grid (the diagonal), the slowest is
along an axis, and the difference falls as $\theta^{2}$. At $8$ points per
wavelength a point source becomes a diamond by about $1.3$ per cent; at $32$ it is
a circle to $0.08$ per cent. This is a discretisation error that mimics a
physically implausible anisotropy, and it is exactly why a simulation claiming to
measure real anisotropy must demonstrate that this term is negligible.

## 5. Assumptions and regime of validity

1. **Constant density and an acoustic medium.** An elastic simulation adds a
   second wave type and, in the standard staggered schemes, turns the dispersion
   behaviour into a function of $v_p/v_s$ as well.
2. **Second order in space and time.** The relations above are for this scheme;
   a fourth-order or a spectral-element scheme has different coefficients
   ([19-02-02](../02-finite-difference-methods/02-fd-stencils.md)), and its
   dispersion error must be measured again.
3. **Homogeneous medium.** A heterogeneous medium varies the local resolution and
   therefore the local error; the reported dispersion applies to the *slowest* and
   most poorly resolved part of the model.
4. **A stated resolution.** Every statement about accuracy must come with
   points per wavelength at the *highest* frequency present, including the source's
   high-frequency tail and any receiver filter.
5. **A stated boundary treatment.** The measurements above use a periodic domain
   so that no boundary contributes. A free surface, an absorbing boundary or a PML
   each adds its own error and its own stability constraint
   ([19-02-03](../02-finite-difference-methods/03-fd-boundary-conditions.md)).
6. **What these tests do not establish.** They do not verify the viscoelastic or
   anisotropic physics, the source radiation pattern or the free-surface
   interaction; each needs its own manufactured or analytic benchmark.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| velocity | $c$ | m s$^{-1}$ | |
| grid spacing | $h$ | m | |
| time step | $\Delta t$ | s | |
| Courant number | $C$ | dimensionless | $c\Delta t/h$ |
| wavelength, ppw | $\lambda$, ppw | m, dimensionless | $\lambda = c/f$ |
| travel time error | — | s | $\Delta x(1/c_g - 1/c)$ |
| depth error | — | m | $\approx z\,\lvert c_g/c - 1\rvert$ for a reflection |

A dimension check catches the commonest implementation error: using the metres per
second velocity with a kilometres per second model, or $\Delta t$ in milliseconds
inside a formula expecting seconds. Both produce a stable-looking run with the
wrong travel times.

## 7. Worked examples

### Example 1 — predicting the measured velocity at 8 points per wavelength

With $\mathrm{ppw} = 8$, $\theta = 2\pi/8 = 0.7854$ rad, $C = 0.5$:

$$\frac{c_g}{c} = \frac{\cos(0.3927)}{\sqrt{1 - 0.25\sin^{2}(0.3927)}}
= \frac{0.92388}{\sqrt{1 - 0.25(0.38268)^{2}}}
= \frac{0.92388}{\sqrt{0.96339}} = \frac{0.92388}{0.98153} = 0.94127 .$$

The demonstration measured $0.95808$ at this resolution: the pulse's finite
bandwidth averages the velocity over neighbouring wavenumbers, which are faster,
so the measurement is $1.8$ per cent above the single-frequency prediction. Both
numbers are consistent with the theory; quoting only one of them without saying
which would be the error.

### Example 2 — the time step and the cost of a 3-D survey

Medium velocity $4000$ m/s, source band up to $30$ Hz, target $10$ points per
wavelength, Courant number $0.5$:

$$h = \frac{c}{f\,\mathrm{ppw}} = \frac{4000}{30\times10} = 13.33\ \mathrm{m},
\qquad
\Delta t = \frac{C h}{c} = \frac{0.5\times13.33}{4000} = 1.67\ \mathrm{ms}.$$

For a $20\ \mathrm{km} \times 20\ \mathrm{km} \times 10\ \mathrm{km}$ model the
node count is $1500 \times 1500 \times 750 = 1.69\times10^{9}$ nodes. With seven
field arrays at eight bytes each ($56$ bytes per node), the working set is
$9.4\times10^{10}$ bytes, about $95$ GB, and one time step moves that much data
through memory. A three-second record needs $1800$ time steps: about $1.7\times10^{14}$
bytes of traffic in total. **The time step is set by stability, the cost by
memory traffic, and neither is negotiable by writing the loop more cleverly.**

### Example 3 — turning a measured velocity error into a depth error

At $20$ points per wavelength the demonstration measures $c_g/c = 0.98462$, i.e.
the numerical pulse is $1.56$ per cent slow. A reflection imaged at $3.00$ km with
the medium velocity therefore sits at

$$z_{\text{apparent}} = \frac{1}{2}c\,t_{\text{measured}}
\approx z_{\text{true}}\frac{c}{c_g} = 3.00 \times 1.0156 = 3.047\ \mathrm{km},$$

about $47$ m too deep. That is the size of the discretisation error in a depth
that a report should carry; whether it matters depends on the target, which is the
argument for stating the resolution alongside the interpretation
([19-07-02](../07-verification-validation-uncertainty/02-solution-verification.md)).

### Example 4 — a verification statement for this simulation

> Scheme: second-order leapfrog, five-point Laplacian, constant density, periodic
> boundaries so that no boundary term contributes. Synthetic medium
> $c = 3000$ m/s. Verification: measured group velocity against the exact discrete
> relation (Section 4.1), agreement within $1.8$ per cent at 8–12 ppw and
> $0.2$ per cent at 32 ppw; stability thresholds measured at $C = 1.000$ and
> $C = 0.7071$ against the exact $1$ and $1/\sqrt{2}$; anisotropy computed from the
> exact relation, $1.3$ per cent at 8 ppw. Not verified: attenuation, anisotropy,
> free-surface interaction, source radiation. Reported: dispersion error,
> Courant margin, and the boundary treatment.

## 8. Python demonstration

```bash
cd 19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_seismic_wavefield_demo.py
```

Runs in about $0.3$ s and prints the exact discrete dispersion relation, the
measured pulse velocities, both stability thresholds, the anisotropy table and the
3-D cost arithmetic. It is print-only: no figures, no file output, no network.

## 9. Exercises

[`exercises/01-simulate-seismic-wavefield-exercises.md`](exercises/01-simulate-seismic-wavefield-exercises.md)
and
[`exercises/01-simulate-seismic-wavefield-solutions.md`](exercises/01-simulate-seismic-wavefield-solutions.md)
include deriving the dispersion relation, designing a grid for a stated depth
tolerance, and a cost-feasibility exercise.

## 10. Applications

- **Imaging and inversion.** Every reverse-time migration and full-waveform
  inversion uses a scheme of this kind; its dispersion error propagates into the
  image and into the velocity model
  ([18-inverse-problems](../../18-inverse-problems/README.md)).
- **Hazard and ground-motion simulation.** Basin response and scenario shaking are
  computed with the same schemes, where the low-velocity near-surface sediments
  set the worst-case resolution.
- **Anisotropy measurement.** Because the *numerical* anisotropy is of the same
  order as the physical anisotropy at coarse grids, the two must be separated
  explicitly ([19-01-04](../01-numerical-foundations/04-numerical-dispersion-diffusion.md)).
- **Performance engineering.** The arithmetic in Section 3.3 is the reason for
  the memory-hierarchy discussion in
  [19-06-01](../06-hpc-and-parallel-computing/01-hpc-architecture.md).

## 11. Further study

- [19-02-05](../02-finite-difference-methods/05-fd-wave-propagation.md),
  [19-02-02](../02-finite-difference-methods/02-fd-stencils.md),
  [19-02-03](../02-finite-difference-methods/03-fd-boundary-conditions.md) — the
  scheme, higher-order stencils and the boundary treatment.
- [19-07-01](../07-verification-validation-uncertainty/01-code-verification.md) —
  the verification discipline, of which Section 4 is one instance.
- [19-01-04](../01-numerical-foundations/04-numerical-dispersion-diffusion.md) —
  dispersion and anisotropy in general.
- [06-09 Reflection Seismology](../../06-seismology/09-reflection-seismology/README.md)
  — the acquisition and processing context that decides what resolution is needed.

## Mastery checkpoint

Without notes:

> A 2-D acoustic simulation uses $c = 2500$ m/s, $h = 5$ m, $\Delta t = 1.0$ ms and
> a source with a 40 Hz upper corner. **(a)** Compute the Courant number and say
> whether the run is stable. **(b)** Compute the points per wavelength at 40 Hz and
> estimate the group-velocity error from the tables. **(c)** A reflector appears at
> $1.50$ km; convert the velocity error into a depth error and state the corrected
> depth. **(d)** The same model must be run in 3-D over $10 \times 10 \times 5$ km
> for 2 s; estimate the node count, the memory traffic per step and the number of
> steps, and state whether it fits in 128 GB of RAM.

Worked answers appear in
[`exercises/01-simulate-seismic-wavefield-solutions.md`](exercises/01-simulate-seismic-wavefield-solutions.md).

## Common pitfalls

1. **Judging a wavefield by eye.** Dispersion is invisible in a snapshot and costs
   per cent-level travel times.
2. **Using $\Delta t$ at the stability limit.** At $C = 0.99$ the demonstration
   already measures $5$ per cent amplitude growth in 200 steps.
3. **Assuming the 1-D Courant limit in 2-D.** The limit is $1/\sqrt{2}$, and the
   factor of $1.414$ is the difference between a run and an overflow.
4. **Reporting accuracy without a resolution.** "The simulation is accurate" is not
   a statement until points per wavelength are stated.
5. **Forgetting the source and receiver bandwidth.** The resolution must be
   computed at the highest frequency that reaches the receivers, not at the source's
   dominant frequency.
6. **Confusing numerical anisotropy with physical anisotropy.** At 8 ppw the
   numerical term is $1.3$ per cent and must be shown to be negligible before any
   physical anisotropy is claimed.

## Related modules

- [19-08 Geophysical Simulation Case Studies](README.md) — the module that contains
  this lesson.
- [19-02 Finite-Difference Methods](../02-finite-difference-methods/README.md).
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md).
- [19-06 High-Performance and Parallel Computing](../06-hpc-and-parallel-computing/README.md).
- [06-seismology](../../06-seismology/README.md) — the science the wavefield
  serves.
- [13-05-03 Benchmarking Geodynamic Codes](../../13-geodynamics-tectonics/05-geodynamic-modelling/03-benchmarking-geodynamics.md)
  — how another modelling community organises the same comparisons.

## Self-assessment checklist

- [ ] I can derive $\sin(\omega\Delta t/2) = C\sin(kh/2)$ and the group velocity.
- [ ] I can derive both stability limits and state them without notes.
- [ ] I can convert a velocity error into a depth error for a reflection.
- [ ] I can compute points per wavelength and turn it into an expected error.
- [ ] I can estimate 3-D node count, memory and traffic for a stated survey.
- [ ] I can write a verification statement for a wavefield simulation.
