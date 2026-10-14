---
id: 19-01-04
title: "Numerical Dispersion, Dissipation and Grid Anisotropy"
level: research
prereqs: ["19-01-03", "02-03-07", "01-12-07"]
tags: [numerical-modelling, hpc, dispersion, dissipation, anisotropy, dispersion-relation]
---

# Numerical Dispersion, Dissipation and Grid Anisotropy

A stable, consistent, convergent scheme can still be wrong in a way that
refinement makes expensive rather than wrong: waves of different wavelength
travel at different speeds (dispersion), lose amplitude (dissipation), and
travel at different speeds in different directions (anisotropy). These are not
errors of magnitude but errors of *shape*, and they survive every convergence
study because the scheme converges to the right answer only as $h\to0$. This
lesson derives the discrete dispersion relation, verifies it against simulation,
measures the group-velocity lag of a pulse, and quantifies the angular
anisotropy of the five-point Laplacian. **All models and data in this module are
SYNTHETIC.** Every number quoted here is printed by
`code/numerical_dispersion_diffusion_demo.py`.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the discrete dispersion relation of the leapfrog (CTCS) scheme,
   $\omega\,dt = \arcsin(C\sin\theta)$, and the corresponding phase speed.
2. **Explain** why $|G| = 1$ exactly for CTCS means no numerical dissipation, and
   **predict** the phase error in the small-$\theta$ limit,
   $v_{\text{num}}/v \approx 1 - (1-C^{2})\theta^{2}/6$.
3. **Measure** the phase speed of a Fourier mode in a simulation and **compare**
   it with the closed-form relation, including the spurious root that a general
   initial condition excites.
4. **Measure** the arrival lag of a narrow-band pulse and relate it to the group
   velocity of the discrete scheme.
5. **Quantify** numerical dissipation as an equivalent diffusivity,
   $D_{\text{num}} = \tfrac12 a h(1-C)$, and **verify** it against a run.
6. **Compare** the angular anisotropy of the five-point and nine-point
   Laplacians and **state** the remedy it implies for wave modelling.

## Prerequisites

- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](03-consistency-stability.md) —
  amplification factors and the Courant number.
- [02-03-07 Dispersion, Group Velocity and Phase vs Group Speed](../../02-physics/03-oscillations-and-waves/07-dispersion.md) —
  phase and group velocity in the continuous setting.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md) —
  the modified-equation view of a scheme's error.

## 1. Intuition: the grid has its own wave physics

A discrete grid cannot represent a wavelength shorter than two cells, and it
represents a wavelength of ten cells only approximately. The consequence is that
the *grid* has a dispersion relation: the speed at which a mode travels depends
on how many cells resolve it. In a simulation this appears as

- a pulse that arrives late (or early) by a percentage set by its wavelength
  content and the grid spacing;
- a pulse that spreads out even though the equation it approximates has no
  spreading;
- a wavefront that is a square near the axes and a diamond near the diagonals,
  because the stencil sees the grid directions, not the physics.

For seismic and electromagnetic modelling this is the practical design rule
"ten points per wavelength". This lesson derives where that rule comes from and
measures how much it is worth.

## 2. Precise definitions

**Discrete dispersion relation.** Insert $U_j^{n} = e^{\mathrm i(kx_j-\omega t_n)}$
into the scheme. The relation between $\omega$ and $k$ that results is the
discrete dispersion relation; it replaces $\omega = ck$.

**Phase speed.** $v_{\text{ph}} = \omega/k$: the speed of a crest. Phase errors
show up as an arrival-time error at a monochromatic receiver.

**Group speed.** $v_{\text{g}} = \mathrm d\omega/\mathrm dk$: the speed of an
envelope. Group errors show up as an arrival-time error of a pulse, which is
what a reflection survey actually measures.

**Numerical dissipation.** $|G(\theta)|<1$: amplitude decays. Pure-dispersion
schemes have $|G|\equiv1$.

**Anisotropy.** Dependence of $v_{\text{ph}}$ on the direction of the
wavenumber vector at fixed $|k|$.

**Points per wavelength (PPW).** $\mathrm{PPW} = \lambda/h = 2\pi/\theta$: the
resolution of the mode, used throughout below.

## 3. Derivations

### 3.1 The discrete dispersion relation of CTCS

For $u_t + a u_x = 0$ the centred-in-space, centred-in-time (leapfrog) scheme is

$$U_j^{n+1} = U_j^{n-1} - C\left(U_{j+1}^{n} - U_{j-1}^{n}\right).$$

Substituting $U_j^n = G^{n}e^{\mathrm i\theta j}$ and dividing by
$G^{n-1}e^{\mathrm i\theta j}$ gives

$$G^{2} + 2\mathrm i\,C\sin\theta\;G - 1 = 0
\qquad\Longrightarrow\qquad
G = -\mathrm i C\sin\theta \pm \sqrt{1-C^{2}\sin^{2}\theta}.$$

For $|C\sin\theta|\le1$ both roots have modulus one:

$$|G|^{2} = C^{2}\sin^{2}\theta + 1 - C^{2}\sin^{2}\theta = 1.$$

**No numerical dissipation at all** for the stable range. Writing the physical
root as $G = e^{-\mathrm i\omega dt}$ gives the discrete dispersion relation

$$\boxed{\;\omega\,dt = \arcsin\!\left(C\sin\theta\right),
\qquad \theta = kh,\qquad C = a\,dt/h\;}$$

and hence

$$\frac{v_{\text{num}}}{v} = \frac{\omega}{ak}
= \frac{\arcsin(C\sin\theta)}{C\,\theta},
\qquad
\frac{v_{\text{g}}}{v} = \frac{\cos\theta}{\sqrt{1-C^{2}\sin^{2}\theta}}.$$

Two exact facts follow immediately. At $C = 1$, $\arcsin(\sin\theta) = \theta$
for $\theta \le \pi/2$, so $v_{\text{num}} = v$ **exactly** for every mode with
$\text{PPW} \ge 4$. And for small $\theta$,

$$\frac{v_{\text{num}}}{v} \approx 1 - \frac{1-C^{2}}{6}\theta^{2}
= 1 - \frac{(1-C^{2})2\pi^{2}}{3\,\mathrm{PPW}^{2}},$$

a second-order phase error that vanishes at $C = 1$.

### 3.2 Measured phase speeds

The demonstration tabulates the closed form and its small-angle estimate:

| C | PPW | $\theta$ | $v_{\text{num}}/v$ | phase error % | small-$\theta$ estimate % |
|---|---|---|---|---|---|
| 0.50 | 4 | 1.570796 | 0.66666667 | $-33.3333$ | $-30.8425$ |
| 0.50 | 5 | 1.256637 | 0.78871529 | $-21.1285$ | $-19.7392$ |
| 0.50 | 8 | 0.785398 | 0.92021382 | $-7.9786$ | $-7.7106$ |
| 0.50 | 10 | 0.628319 | 0.94950813 | $-5.0492$ | $-4.9348$ |
| 0.50 | 16 | 0.392699 | 0.98054183 | $-1.9458$ | $-1.9277$ |
| 0.50 | 20 | 0.314159 | 0.98758798 | $-1.2412$ | $-1.2337$ |
| 0.50 | 40 | 0.157080 | 0.99691101 | $-0.3089$ | $-0.3084$ |
| 1.00 | 4–40 | — | 1.00000000 | $0.0000$ | $0.0000$ |

At four points per wavelength a wave is **one third slow** — a 33 % travel-time
error, larger than any target in seismology. The estimate is accurate to a few
per cent of the error itself, which is why the estimate is used for design and
the closed form for reporting.

### 3.3 Verifying the relation in a simulation

A dispersion relation is a statement about eigenvectors of the update operator.
To test it, start the run in a state that admits only the physical root
($U^{0} = e^{\mathrm i\theta j}$, $U^{-1} = U^{0}/G$), run one period, and
measure the phase against the exact continuum solution:

| C | PPW | measured $v_{\text{num}}/v$ | predicted | amplitude |
|---|---|---|---|---|
| 0.50 | 4 | 0.6666666667 | 0.6666666667 | 1.0000000000 |
| 0.50 | 8 | 0.9202138247 | 0.9202138247 | 1.0000000000 |
| 0.50 | 16 | 0.9805418292 | 0.9805418292 | 1.0000000000 |
| 0.50 | 32 | 0.9951693091 | 0.9951693091 | 1.0000000000 |
| 1.00 | 4–32 | 1.0000000000 | 1.0000000000 | 1.0000000000 |

Agreement to the last printed digit, and the amplitude is preserved to
round-off — the measured statement of "no numerical dissipation".

Now the honest complication. Real initial data are not eigenmodes. Starting
instead from the exact solution at $t = -dt$ excites **both** roots, and the
spurious root is neutral too, so it does not decay:

| PPW | measured $v_{\text{num}}/v$ | predicted | amplitude after one period |
|---|---|---|---|
| 8 | 0.9198911117 | 0.9202138247 | 0.9840298051 |
| 16 | 0.9805472805 | 0.9805418292 | 0.9995265245 |
| 32 | 0.9951694645 | 0.9951693091 | 0.9999855717 |

A scheme with $|G|\equiv1$ loses $1.6\,\%$ of the amplitude at PPW $= 8$. That
energy has not been dissipated; it has been transferred to a mode travelling in
the opposite direction that beats against the physical one. Spurious roots are a
property of leapfrog-type schemes and must be recognised as artefacts, not
physics.

### 3.4 Group velocity: the arrival lag of a pulse

A pulse's envelope travels at the group speed. The demonstration advects a
Gaussian-modulated packet (carrier at PPW $= 8$, envelope width $6$ m) over
$400$ m and reports the lag relative to travel at $a$:

| C | $v_{\text{g}}/v$ predicted | predicted lag % | measured lag % |
|---|---|---|---|
| 0.50 | 0.75592895 | 24.407105 | 24.790179 |
| 0.80 | 0.85749293 | 14.250707 | 14.599724 |
| 1.00 | 1.00000000 | 0.000000 | $-0.250000$ |

At $C = 0.5$ a pulse resolved by eight cells per wavelength arrives a quarter of
its travel time late. At $C = 1$ the lag is zero to within the measurement
window. The residual $0.25\,\%$ at $C = 1$ is the finite width of the packet:
its spectrum contains modes with $\theta > \pi/2$, where arcsin is no longer
invertible and the exactness argument fails. **This is the practical reason
$C = 1$ is not used in production**: exactness at $C = 1$ holds for the physical
branch only, and any broadband source has a tail outside it.

### 3.5 Numerical dissipation and an equivalent diffusivity

Upwind differencing has $|G|^{2} = 1 - 2C(1-C)(1-\cos\theta)$: strictly less
than one for $0<C<1$, so the scheme dissipates. Writing the modified equation,

$$u_t + a u_x = D_{\text{num}}\,u_{xx}, \qquad
D_{\text{num}} = \frac{a h}{2}(1-C),$$

the damping of a Fourier mode over time $t$ is $\exp(-D_{\text{num}}k^{2}t)$.
For PPW $= 16$ the demonstration compares the two descriptions:

| C | $\lvert G\rvert$ per step | $\lvert G\rvert^{n}$ over 320 s | $D_{\text{num}}$ (m²/s) | $\exp(-Dk^{2}t)$ |
|---|---|---|---|---|
| 0.25 | 0.98562408 | $8.922162\times10^{-9}$ | 0.3750 | $9.186707\times10^{-9}$ |
| 0.50 | 0.98078528 | $4.048752\times10^{-6}$ | 0.2500 | $4.386383\times10^{-6}$ |
| 0.75 | 0.98562408 | $2.064083\times10^{-3}$ | 0.1250 | $2.094369\times10^{-3}$ |
| 1.00 | 1.00000000 | $1.000000\times10^{0}$ | 0.0000 | $1.000000\times10^{0}$ |

Running the actual scheme and measuring the amplitude of the mode reproduces
$|G|^{n}$ digit for digit ($1\times10^{-8}$ against $1\times10^{-8}$,
$4.05\times10^{-6}$ against $4.05\times10^{-6}$, and so on). Two facts are worth
carrying away. The dissipation is *maximal at $C = 1/2$* — the same Courant
number where the phase error is largest — and it vanishes at $C = 1$, where the
scheme is exact.

### 3.6 Grid anisotropy of the Laplacian

For a plane wave $e^{\mathrm i(k_xx+k_yy)}$ the five-point Laplacian and the
nine-point (Mehrstellen) Laplacian have symbols

$$S_{5} = \frac{2\cos k_xh + 2\cos k_yh - 4}{h^{2}},\qquad
S_{9} = \frac{8(\cos k_xh+\cos k_yh) + 4\cos k_xh\cos k_yh - 20}{6h^{2}},$$

and the effective wavenumber is $k_{\text{eff}} = \sqrt{-S}$. At fixed $|k|$ the
deviation of $k_{\text{eff}}/|k|$ from one measures how badly that direction is
modelled:

| scheme | PPW | $k_{\text{eff}}/\lvert k\rvert$ at 0° | at 45° | anisotropy % |
|---|---|---|---|---|
| 5-point | 4 | 0.90031632 | 0.94938273 | 5.4499 |
| 9-point | 4 | 0.90031632 | 0.90432678 | 0.4455 |
| 5-point | 8 | 0.97449536 | 0.98719841 | 1.3036 |
| 9-point | 8 | 0.97449536 | 0.97475620 | 0.0268 |
| 5-point | 16 | 0.99358685 | 0.99679033 | 0.3224 |
| 9-point | 16 | 0.99358685 | 0.99360331 | 0.0017 |
| 5-point | 32 | 0.99839439 | 0.99919700 | 0.0804 |
| 9-point | 32 | 0.99839439 | 0.99839542 | 0.0001 |

Both schemes share the same along-axis error and differ in the diagonal; the
nine-point operator reduces the angular variation by roughly a factor of $50$ at
PPW $= 8$ and carries a stencil whose matrix has nine non-zeros per row instead
of five. Anisotropy therefore has a price and it is paid in bandwidth, which is
the subject of [19-02-02](../02-finite-difference-methods/02-fd-stencils.md).

## 4. Worked example: choosing a grid for a travel-time target

*A seismic modelling study must deliver travel times accurate to $0.5\,\%$ at
$C = 0.5$, using a second-order CTCS scheme.*

1. Phase error from §3.1: $\varepsilon \approx (1-C^{2})2\pi^{2}/(3\,\mathrm{PPW}^{2})
   = (0.75)(19.739)/\mathrm{PPW}^{2} = 14.80/\mathrm{PPW}^{2}$.
2. Solve for PPW: $\mathrm{PPW} = \sqrt{14.80/0.005} = 54.4$.
3. Check against the exact relation: at PPW $= 54$ the exact error is
   $1 - \arcsin(0.5\sin\theta)/(0.5\theta) \approx 0.5\,\%$ as designed — the
   estimate is adequate at this resolution because the $O(\theta^{4})$ correction
   is only $1.7\,\%$ of the error.
4. Consequence for the grid: a 30 Hz seismic wavelet in a 3000 m/s medium has
   $\lambda = 100$ m, so $h = 100/54.4 = 1.8$ m — an order of magnitude finer
   than the familiar "ten points per wavelength". Raising the order of the
   spatial scheme, or driving the run at $C = 1$, is the only way to bring the
   cost down; §3.1 quantifies both.

## 5. Assumptions and regime of validity

1. **Constant coefficients, periodic, uniform grid.** Anisotropy and dispersion
   are properties of the stencil; a heterogeneous medium adds scattering and
   mode conversion on top, and the numbers above no longer describe the total
   error.
2. **Stable Courant numbers.** The closed forms assume $|C\sin\theta|\le1$; for
   $C>1$ the roots are real and the scheme grows rather than disperses.
3. **Long-wavelength estimates.** The small-$\theta$ forms are accurate to a
   few per cent of the error for $\mathrm{PPW}\ge8$ and useless below
   $\mathrm{PPW} = 5$; the measured table shows the gap at PPW $=4$ ($-33.3\,\%$
   exact against $-30.8\,\%$ estimated).
4. **Physical branch only.** The dispersion relation describes the physical
   root; the spurious root of §3.3 coexists, is neutral, and contaminates
   amplitudes measured from general initial data.
5. **Pulse measurements include the envelope.** The measured lag of §3.4 is a
   group-velocity measurement and carries the bandwidth of the packet; a
   broad-band source mixes behaviours from different $\theta$ and the single
   number $v_{\text{g}}(\theta_0)$ is an approximation.
6. **Isotropic stencils only.** Higher-order and compact stencils change every
   coefficient here; the method of measurement is what transfers, not the
   numbers.

## 6. Python demonstration

`code/numerical_dispersion_diffusion_demo.py` prints:

1. the closed-form phase-speed table with the small-angle estimate;
2. measured phase speeds from runs in the pure physical eigenmode, and the
   amplitude loss caused by the spurious root when a general start is used;
3. the group-velocity lag of a Gaussian packet at three Courant numbers;
4. the upwind decay rate against its equivalent diffusivity, verified by a run;
5. the anisotropy table for the five-point and nine-point Laplacians.

```bash
cd 19-numerical-modeling-hpc/01-numerical-foundations/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python numerical_dispersion_diffusion_demo.py
```

## Mastery checkpoint

Without notes:

> A CTCS scheme is run at $C = 0.5$ on a grid with $h = 5$ m in a medium with
> $a = 1500\ \mathrm{m\,s^{-1}}$. **(a)** Compute the phase error for a mode
> with $\mathrm{PPW} = 8$ from the closed form and from the small-angle estimate.
> **(b)** A pulse travels $3$ km: predict its arrival lag from the group
> velocity and state whether it arrives early or late. **(c)** State what
> happens to the amplitude of a pure mode and why, and what additional effect a
> general initial condition has. **(d)** Name the two changes to the scheme or
> the run that remove the phase error entirely, and give the condition under
> which each works.

Parts (a) and (b) are worked in
[`exercises/04-numerical-dispersion-diffusion-solutions.md`](exercises/04-numerical-dispersion-diffusion-solutions.md).

## Common pitfalls

1. **Assuming convergence implies accuracy.** A converging scheme converges to
   the *discrete* dispersion relation, not to the continuum one.
2. **Ignoring the Courant number when quoting a dispersion error.** At PPW $=8$
   the error is $7.98\,\%$ at $C = 0.5$ and zero at $C = 1$.
3. **Quoting a "ten points per wavelength" rule as universal.** It corresponds
   to about a $1.9\,\%$ phase error at $C = 0.5$; a $0.5\,\%$ target needs 54
   points.
4. **Confusing phase and group errors.** They differ; a survey measures arrival
   times of envelopes, which is the group velocity.
5. **Calling amplitude loss "dissipation" without checking $|G|$.** For CTCS the
   loss at §3.3 is a spurious mode, not damping.
6. **Forgetting that anisotropy grows as the grid coarsens in *both* directions
   of the stencil.** Refining isotropically helps; refining one direction only
   can make the angular variation worse.

## Related modules

- [19-02-02 High-Order and Compact Stencils; Staggered Grids](../02-finite-difference-methods/02-fd-stencils.md) —
  the stencils that trade anisotropy and bandwidth for accuracy.
- [19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation](../02-finite-difference-methods/05-fd-wave-propagation.md) —
  the same dispersion and anisotropy measured in two dimensions.
- [06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation](../../06-seismology/01-elastic-wave-propagation/02-p-and-s-waves.md) —
  what the modelled waves are.
- [01-12-07 Discretising PDEs: Consistency, Stability, Convergence](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md).
- [Module 19-01 Numerical Foundations for Simulation](README.md).

Exercises and worked solutions:
[`exercises/04-numerical-dispersion-diffusion-exercises.md`](exercises/04-numerical-dispersion-diffusion-exercises.md)
and
[`exercises/04-numerical-dispersion-diffusion-solutions.md`](exercises/04-numerical-dispersion-diffusion-solutions.md).
