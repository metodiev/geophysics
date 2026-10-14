---
id: 06-07-03
title: "Ambient-Noise Tomography and Monitoring"
level: doctoral
prereqs: ["06-07-02", "06-06-01"]
tags: [seismology, ambient-noise, tomography, surface-waves, dispersion, null-space]
---

# Ambient-Noise Tomography and Monitoring

**All models and data in this module are SYNTHETIC.** The layered model, the
station geometry, the anomaly amplitudes and the noise realisations are chosen
teaching values, and every number below is printed by
[`code/noise_tomography_demo.py`](code/noise_tomography_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Love-wave dispersion relation for a layer over a half-space
   and **explain** why the phase velocity is bounded by the two shear speeds.
2. **Measure** phase and group velocity from a retrieved correlation, and
   **state** the frequency grid that avoids a $2\pi$ phase ambiguity.
3. **Derive** the group-velocity relation $U = c/(1+(T/c)\,dc/dT)$ and
   **distinguish** a group from a phase measurement.
4. **Formulate** the tomographic forward problem as a path integral and
   **solve** the damped least-squares system.
5. **Interpret** the damping trade-off and the resolution matrix, and
   **identify** cells that are in the null space of the path geometry.
6. **State** the difference between a tomographic inversion and a monitoring
   inversion, and why the second is harder.

## Prerequisites

- [06-07-02 Retrieving the Green's Function](02-cross-correlation-green.md) —
  the empirical Green's function is the input here.
- [06-06-01 The Tomography Principle](../06-seismic-tomography/01-tomography-principle.md) —
  data as path integrals.

---

## 1. The measurement chain

Ambient-noise tomography is four operations, each of which can fail
independently:

$$\underbrace{\text{noise records}}_{\text{lesson 01-02}}
\;\longrightarrow\;
\underbrace{\text{empirical Green's functions}}_{\text{per station pair}}
\;\longrightarrow\;
\underbrace{c(T),\ U(T)}_{\text{dispersion per pair}}
\;\longrightarrow\;
\underbrace{c(T,x,y)}_{\text{2-D maps, per period}}.$$

The first arrow needs an isotropic-enough source field (lesson 02 §5). The
second needs a stable phase measurement. The third needs a parametrisation of
the Earth — the 1-D dispersion relation is where the physics lives, and this
lesson derives it rather than quoting it. The fourth needs a path-coverage
assessment, which is where the honesty lives.

## 2. Deriving the dispersion of the fundamental Love mode

Consider an SH wave in an elastic layer of thickness $H$, shear speed $v_{s1}$
and density $\rho_1$, over a half-space of shear speed $v_{s2}>v_{s1}$ and
density $\rho_2$. Seek a mode that propagates horizontally with horizontal wave
number $k=\omega/c$ and does not radiate into the half-space:

$$u_y(z) = \begin{cases}
A\cos(k_1 z), & 0 \le z \le H,\\[1mm]
B\,e^{-k_2 z}, & z > H,
\end{cases}
\qquad
k_1 = \sqrt{\frac{1}{v_{s1}^{2}}-\frac{1}{c^{2}}},\quad
k_2 = \sqrt{\frac{1}{c^{2}}-\frac{1}{v_{s2}^{2}}}.$$

Both $k_1$ and $k_2$ must be real: $k_1$ real means $c>v_{s1}$ (the mode is
slower than nothing inside the layer), and $k_2$ real means $c<v_{s2}$ (or the
half-space would carry the energy away and the mode would decay). Hence

$$v_{s1} < c(T) < v_{s2} \qquad\text{for every period } T.$$

Continuity of displacement and of shear traction at $z=H$ gives two equations;
eliminating the constants yields the **dispersion relation**

$$\boxed{\;\tan\!\left(\omega H k_1\right)
= \frac{\mu_2}{\mu_1}\,\frac{k_2}{k_1},\qquad \mu_i = \rho_i v_{si}^{2}.\;}$$

For the teaching model ($v_{s1}=2.00\ \mathrm{km\,s^{-1}}$,
$\rho_1=2.80\ \mathrm{g\,cm^{-3}}$, $H=20.0\ \mathrm{km}$;
$v_{s2}=4.00\ \mathrm{km\,s^{-1}}$,
$\rho_2=3.30\ \mathrm{g\,cm^{-3}}$), the stiffness ratio is an exact number of
the model:

$$\frac{\mu_2}{\mu_1}=\frac{3.30\times 4.00^{2}}{2.80\times 2.00^{2}}
=\frac{52.8}{11.2}=4.71429 .$$

**Bracketing the fundamental root.** The fundamental branch is the one with
$0<\omega H k_1<\pi/2$, and its bracket follows from the two limits of the
right-hand side:

- as $c\to v_{s1}^{+}$: $k_1\to 0^{+}$, so $\tan\to 0^{+}$ and
  $(\mu_2/\mu_1)k_2/k_1\to+\infty$: the residual goes to $-\infty$;
- as $c\to v_{s2}^{-}$: $k_2\to 0$, so the residual
  $\tan(\omega H k_1) - 0$ is positive **provided** $\omega H k_{1}^{\max}<\pi/2$
  with $k_1^{\max}=\sqrt{1/v_{s1}^2-1/v_{s2}^2} = \sqrt{0.25-0.0625} =
  0.433013\ \mathrm{rad\,km^{-1}}$.

Otherwise the tangent hits its first pole first, and the bracket is closed by
the pole rather than by $c\to v_{s2}$. The crossover is

$$\omega H k_1^{\max}=\frac{\pi}{2}
\;\Longrightarrow\;
T^{*}=\frac{2\pi H k_1^{\max}}{\pi/2}
=\frac{2\pi\times 20.0\times 0.433013}{1.570796}=34.6\ \mathrm{s}.$$

Below $T^{*}$ the mode is trapped by the layer's resonant tangent; above it, it
leaks towards the half-space speed. This is why the demonstration solves the
relation by bracketing between $k_1\to 0$ and the first pole, and why a naive
grid search over $c$ can return a **higher mode** by mistake.

The solved curve is:

| period (s) | $c$ (km/s) | wavelength $cT$ (km) | $c/v_{s1}$ |
|---|---|---|---|
| 5.0 | 2.0152 | 10.1 | 1.008 |
| 8.0 | 2.0387 | 16.3 | 1.019 |
| 10.0 | 2.0604 | 20.6 | 1.030 |
| 15.0 | 2.1372 | 32.1 | 1.069 |
| 20.0 | 2.2500 | 45.0 | 1.125 |
| 30.0 | 2.6046 | 78.1 | 1.302 |
| 40.0 | 3.0878 | 123.5 | 1.544 |
| 50.0 | 3.4701 | 173.5 | 1.735 |

Three properties are visible and all three are general: $c$ increases with $T$
at every tabulated period; $c$ is strictly inside $(2.00,4.00)$; and the
wavelength crosses the layer thickness $H = 20\ \mathrm{km}$ between 8 s and
10 s, which is the classic statement that a surface wave at period $T$ senses
structure to a depth of order $cT$. The last row (50 s) has
$c/v_{s2} = 0.868$, so the mode is approaching, but has not reached, the
half-space speed — as the bracket argument requires.

## 3. Measuring phase velocity from the retrieved correlation

With the dispersion curve known, the demonstration builds the pair's empirical
Green's function in the frequency domain with phase
$\phi(f)=2\pi f d/c(f)$, transforms to time, and then measures the curve back:

$$c_{\text{meas}}(T) = \frac{2\pi f\,d}{-\angle C(f)} .$$

| period (s) | $c$ from phase (km/s) | $c$ model (km/s) | error (km/s) |
|---|---|---|---|
| 5.0 | 2.0152 | 2.0152 | $-0.0000$ |
| 10.0 | 2.0605 | 2.0604 | $+0.0002$ |
| 20.0 | 2.2506 | 2.2500 | $+0.0005$ |
| 40.0 | 3.0884 | 3.0878 | $+0.0006$ |

The residuals of order $10^{-4}\ \mathrm{km\,s^{-1}}$ come from the finite
frequency grid used to differentiate the phase, not from the physics.

**The $2\pi$ trap.** A phase is known only modulo $2\pi$. Between adjacent
frequency samples separated by $\Delta f$ the measured phase advances by
$2\pi\Delta f\,d/c$; if that exceeds $\pi$ the unwrapping assumption fails and
the velocity is wrong by a multiple of $c^{2}/(\Delta f\,d)$. The condition is

$$\Delta f < \frac{c}{2d} = \frac{3.20}{2\times 60} = 0.0267\ \mathrm{Hz}
\quad\text{(for } c = 3.20\ \mathrm{km\,s^{-1}},\ d = 60\ \mathrm{km)}.$$

The demonstration uses $600$ frequencies over $0.02$-$0.25\ \mathrm{Hz}$, i.e.
$\Delta f = 3.8\times10^{-4}\ \mathrm{Hz}$, comfortably inside the limit. A
longer path or a faster phase velocity tightens the limit linearly.

**Worked numeric example (the 10 s row).** With $d = 60\ \mathrm{km}$ and
$c = 2.0604\ \mathrm{km\,s^{-1}}$:

$$f = 0.100\ \mathrm{Hz},\qquad
\phi = \frac{2\pi f d}{c} = \frac{2\pi \times 0.1 \times 60}{2.0604}
= 18.297\ \mathrm{rad},$$
$$c_{\text{meas}} = \frac{2\pi \times 0.1 \times 60}{18.297}
= 2.0605\ \mathrm{km\,s^{-1}},$$

which is the tabulated value. Note that $\phi$ exceeds $2\pi$ three times: the
measurement *requires* unwrapping, and therefore requires the frequency grid
condition derived above.

## 4. Group velocity: a different measurement of the same wave

The wave packet travels at the group velocity. With $k=\omega/c(T)$ and
$T=2\pi/\omega$,

$$\frac{dk}{d\omega} = \frac{1}{c} - \frac{\omega}{c^{2}}\frac{dc}{d\omega},
\qquad
\frac{dc}{d\omega} = -\frac{T}{\omega}\frac{dc}{dT},$$

$$U \equiv \left(\frac{dk}{d\omega}\right)^{-1}
= \frac{c}{1+\dfrac{T}{c}\dfrac{dc}{dT}} .$$

For a normally dispersive mode ($dc/dT>0$) this gives $U<c$; the two velocities
coincide only when $c$ is constant.

| period (s) | $c$ (km/s) | $dc/dT$ (km/s per s) | $U$ (km/s) |
|---|---|---|---|
| 5.0 | 2.0152 | 0.00610 | 1.9852 |
| 8.0 | 2.0387 | 0.00962 | 1.9645 |
| 10.0 | 2.0604 | 0.01209 | 1.9461 |
| 15.0 | 2.1372 | 0.01879 | 1.8882 |
| 20.0 | 2.2500 | 0.02656 | 1.8203 |
| 30.0 | 2.6046 | 0.04430 | 1.7246 |
| 40.0 | 3.0878 | 0.04732 | 1.9144 |
| 50.0 | 3.4701 | 0.02838 | 2.4630 |

The envelope of the same broadband retrieval peaks at $t = 30.435\ \mathrm{s}$,
giving an average speed of $60/30.435 = 1.971\ \mathrm{km\,s^{-1}}$ over a
frequency band whose energy is dominated by the short periods, where $U$ is
$1.95$-$1.99\ \mathrm{km\,s^{-1}}$. Reading a *phase* velocity from that number
would be a category error: the envelope measures $U$.

**Worked numeric example (the 10 s row).** With $T = 10.0\ \mathrm{s}$,
$c = 2.0604$ and $dc/dT = 0.01209\ \mathrm{km\,s^{-1}\,s^{-1}}$:

$$U = \frac{2.0604}{1 + \dfrac{10.0}{2.0604}\times 0.01209}
= \frac{2.0604}{1.05867} = 1.9461\ \mathrm{km\,s^{-1}},$$

a $5.5\%$ difference from the phase velocity. A study that mixes the two
without saying which it measured will disagree with any other study that did.

## 5. From pairs to a map: the tomographic inversion

At a fixed period, let the map be a grid of $M$ cells with slowness
perturbation $m_j$ relative to a reference $s_0$. For a straight ray $i$ of
length $L_i$ crossing cell $j$ over a length $\ell_{ij}$, the data are the
relative path-averaged slowness anomaly

$$d_i = \sum_{j=1}^{M}\frac{\ell_{ij}}{L_i}\,m_j
\qquad\Longleftrightarrow\qquad \mathbf{d} = \mathbf{G}\,\mathbf{m},$$

which is **linear**. The demonstration uses a $6\times 6$ grid of $20\ \mathrm{km}$
cells, 13 stations (a ring of 12 plus a centre) giving 78 pairs, a reference
slowness of $0.3333\ \mathrm{s\,km^{-1}}$ (i.e. $3.00\ \mathrm{km\,s^{-1}}$), a
true anomaly of $+3.0\%$ slowness in two adjacent cells, and Gaussian data noise
of $0.1\%$ relative slowness. The damped least-squares solution is

$$\hat{\mathbf{m}} = \left(\mathbf{G}^{\!\top}\mathbf{G}
+ \lambda^{2}\mathbf{I}\right)^{-1}\mathbf{G}^{\!\top}\mathbf{d}.$$

| damping $\lambda$ | rms misfit | model norm | recovered peak | peak/true |
|---|---|---|---|---|
| 0.003 | $7.76\times10^{-4}$ | 0.04547 | 2.92% | 0.973 |
| 0.010 | $7.76\times10^{-4}$ | 0.04545 | 2.92% | 0.973 |
| 0.030 | $7.77\times10^{-4}$ | 0.04534 | 2.92% | 0.972 |
| 0.100 | $7.81\times10^{-4}$ | 0.04429 | 2.88% | 0.960 |
| 0.300 | $9.10\times10^{-4}$ | 0.03963 | 2.67% | 0.891 |
| 1.000 | $2.47\times10^{-3}$ | 0.02327 | 1.66% | 0.552 |

Read the table as a trade-off, not as a menu. For $\lambda\le 0.03$ the model
reproduces the anomaly to $97\%$ and fits the data to its noise level
($0.78\times10^{-3}$, consistent with the $0.1\%$ input noise). At
$\lambda = 1.0$ the misfit has tripled while the recovered anomaly has lost
nearly half its amplitude: the damping is now a **bias** that no amount of data
can remove. The minimum-misfit model ($\lambda\to 0$) is not the answer either:
with 36 unknowns and 78 data there is enough null space to make it oscillatory,
and the *a priori* choice of $\lambda$ is a statement about how much structure
you are willing to believe. That statement belongs in the methods section, not
in a footnote.

## 6. Resolution and the null space

The **resolution matrix** $\mathbf{R} =
(\mathbf{G}^{\!\top}\mathbf{G}+\lambda^2\mathbf{I})^{-1}\mathbf{G}^{\!\top}\mathbf{G}$
says how much of each true cell appears in its own estimate. The demonstration
reports, for $\lambda=0.03$:

| diagnostic | value |
|---|---|
| checkerboard recovered/true norm ratio | 0.935 |
| checkerboard pattern correlation | 0.943 |
| mean diagonal of $\mathbf{R}$ | 0.884 |
| worst diagonal of $\mathbf{R}$ | 0.000 |
| path counts per cell (min / max) | 0 / 17 |
| cells crossed by no path | 4 |

A checkerboard of $2.0\%$ amplitude is recovered with a pattern correlation of
$0.943$ and $93.5\%$ of its norm — good, but the *worst* diagonal of the
resolution matrix is exactly zero, and four cells are crossed by no path at all.
Those cells cannot be recovered from these data by any inversion; their
apparent values are entirely leakage from their neighbours. Reporting a map
without its path coverage and resolution diagonal is reporting a
parametrisation, not an Earth.

## 7. From tomography to monitoring

The same machinery is used to *watch* a medium change: measure $c(T)$ on every
pair at repeated epochs, invert each epoch separately, and difference the
resulting maps. Two things change the error budget.

- **Common-mode error.** Atmospheric pressure, temperature and instrument
  changes affect all pairs at once. They are not removed by averaging pairs;
  they are removed by differencing epochs (which is why monitoring is
  *relative*), or by a cross-correlation between the reconstructed change and
  independent pressure data.
- **Source-direction bias.** A change in the noise source distribution between
  epochs changes the retrieved travel times without any change in the medium —
  lesson 01 §6 quantifies how strongly (a $45^\circ$ sector raises the
  coherence from $0.184$ to $0.929$). No inversion can distinguish this from
  structure, because it enters the data as a travel-time perturbation.

The precision actually achievable for a *local* velocity change is measured in
lesson 05; the point here is structural: the tomographic inversion converts
path-averaged measurements into a map, and in doing so it **amplifies**
whatever is common to many paths while mixing the null-space components of the
geometry into every cell.

## 8. Assumptions and regime of validity

1. **Straight rays, or known rays.** The forward operator used $\ell_{ij}/L_i$
   for a straight line. For a laterally varying medium the path bends, and the
   operator is a functional of the unknown — the inversion becomes non-linear.
2. **Isotropic, single-mode propagation.** Two modes with different speeds
   produce two overlapping dispersion curves, and the measured phase is a
   mixture that no 1-D model explains.
3. **Correct reference model.** The inversion recovers *relative* perturbations;
   the absolute level and the sensitivity kernels come from the reference. A
   wrong reference biases $c(T,x,y)$ everywhere.
4. **Local 1-D approximation.** Each cell is treated as a 1-D structure. This is
   exactly what breaks for the smallest cells and the longest periods, where the
   first Fresnel zone is much larger than the cell.
5. **Stationary noise field between epochs** (monitoring). Testable by comparing
   the retrieved *amplitudes* with the travel times: a source change perturbs
   both, a medium change perturbs mainly the times.

## Mastery checkpoint

> **(a)** State the two limits that bound $c(T)$ for a Love mode and show with
> the model numbers which of them applies at $T = 5\ \mathrm{s}$ and at
> $T = 50\ \mathrm{s}$. **(b)** For $d = 60\ \mathrm{km}$ and
> $c = 2.06\ \mathrm{km\,s^{-1}}$, compute the phase at 0.1 Hz and confirm the
> measured phase velocity. **(c)** Compute $U$ at $T = 20\ \mathrm{s}$ from the
> table and state whether the envelope of the retrieval should arrive before or
> after the phase. **(d)** In the tomographic table, which damping value fits
> the data at the noise level, and what is the cost of damping at
> $\lambda=1.0$? **(e)** Four cells are crossed by no path. What can and cannot
> be said about them?

## Common pitfalls

1. **Mixing group and phase velocities.** The envelope measures $U$; the phase
   of the cross-spectrum measures $c$; the two differ by $5.5\%$ at 10 s in this
   model.
2. **Unwrapping a phase that wrapped twice.** Check $\Delta f < c/(2d)$ before
   trusting any phase velocity.
3. **Choosing damping for the prettiest map.** The misfit-versus-norm table is
   the evidence; the choice of $\lambda$ is a prior.
4. **Publishing a map without the resolution diagonal.** A cell with no path is
   not a measurement.
5. **Confusing a reference-model error with a data error.** A wrong $s_0$ shifts
   the whole map and does not appear in the misfit.

## Related modules

- [06-07-02 Retrieving the Green's Function by Cross-Correlation](02-cross-correlation-green.md).
- [06-06 Seismic Tomography](../06-seismic-tomography/README.md) — the general
  theory of path-based inversion.
- [06-06-03 Resolution, Null Space and Model Covariance](../06-seismic-tomography/03-resolution-and-nullspace.md) —
  the resolution matrix in full.
- [18-03 Regularization](../../18-inverse-problems/03-regularization/README.md) —
  choosing damping with a criterion.

## Code and exercises

- Demonstration:
  [`code/noise_tomography_demo.py`](code/noise_tomography_demo.py).
- Exercises:
  [`exercises/03-noise-tomography-exercises.md`](exercises/03-noise-tomography-exercises.md)
  with worked [solutions](exercises/03-noise-tomography-solutions.md).
