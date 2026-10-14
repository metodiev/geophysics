---
id: 08-05-03
title: "EM Forward Modelling: Integral Equation, FD, FE Methods"
level: research
prereqs: ["08-05-01", "08-05-02", "02-07-06", "01-09-02"]
tags: [geomagnetism, electromagnetism, forward-modelling, finite-difference, finite-element, integral-equation]
---

# EM Forward Modelling: Integral Equation, FD, FE Methods

Every quantitative statement in this module is a forward model. A response curve,
an apparent conductivity, an inversion result — each is a prediction of some
model, compared with data. The purpose of this lesson is to make the *forward*
half of that comparison explicit and checkable, because a forward model that has
never been verified against anything except itself is not evidence.

There are three families of EM forward model, and they differ in what they
discretise rather than in the physics. The **layered (analytic) family** solves
Maxwell's equations exactly for a one-dimensional Earth and needs no mesh at all.
The **integral-equation family** discretises only the anomalous volume and uses a
Green's function for the background. The **differential family** (finite
difference, finite element) discretises the whole region and solves a sparse
linear system. This lesson derives the first exactly, states the second with its
validity criterion measured against the first, and measures the convergence of
the third on a problem with an exact solution.

All models and data in this module are **SYNTHETIC**. The conductivities,
thicknesses, frequencies, separations and meshes are chosen teaching values, not
measurements of a real ground.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the quasi-static curl-curl equation for the electric field and
   **explain** why a magnetic dipole source needs only the TE (or TM) part of the
   field in a one-dimensional Earth.
2. **Derive** the admittance recursion for a layered halfspace from the interface
   conditions, and relate it to the reflection coefficient
   $R(\lambda)=(\lambda-q)/(\lambda+q)$.
3. **Verify** a layered code against a closed form, against a direct elimination
   of the interface conditions, and against the matched-layer identity.
4. **Quantify** model equivalence: how much a response changes when the layer
   thickness changes at fixed conductance, with a stated resolution check.
5. **State** the integral equation and its first-order (Born) term, and
   **measure** the contrast range over which the linearisation holds for a given
   target.
6. **Derive** the finite-difference and linear finite-element discretisations of a
   one-dimensional diffusion problem and **measure** their convergence orders.
7. **Report** a modelling result with the mesh, the range of wavenumbers and the
   resolution check that make it reproducible.

## Prerequisites

- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md)
  — the response integral and the skin depth.
- [08-05-02 Time-Domain EM (TDEM): Sounding, Transients and Decay Curves](02-time-domain-em.md)
  — the diffusion equation and its exact solutions.
- [02-07-06 EM Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md)
  — the diffusion limit of Maxwell's equations.
- [01-09-02 The Heat Equation](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md)
  — separation of variables and similarity solutions.

## 1. What a forward model is asked to do

A forward model is a map from a model $\mathbf{m}$ to a prediction
$\mathbf{d}^{\text{pred}}(\mathbf{m})$ that can be compared with data
$\mathbf{d}^{\text{obs}}$ through a misfit. Three things must be stated about any
forward model before its predictions are usable:

- **its discretisation** — what was approximated and how finely;
- **its error** — measured against a problem with a known answer, not asserted;
- **its domain of validity** — the physical regime in which the approximation
  holds, with the criterion written down.

For EM the physical regimes are set by three dimensionless groups: the induction
number $\theta=r/\delta$ of
[08-05-01](01-frequency-domain-em.md), the contrast within the model, and the
number of skin depths spanned by the model. A modelling result that does not name
these is not reproducible.

### 1.1 The governing equation

With $e^{+i\omega t}$ and no displacement current, the electric field satisfies

$$\nabla\times\nabla\times\mathbf{E}
=\nabla(\nabla\cdot\mathbf{E})-\nabla^2\mathbf{E}
=i\omega\mu_0\sigma\mathbf{E}
\qquad\Longrightarrow\qquad
\nabla^2\mathbf{E}+i\omega\mu_0\sigma\mathbf{E}=0$$

away from free charge, with $\nabla\cdot\mathbf{E}=0$ in a piecewise-uniform
medium. Conductivity enters exactly as a complex wavenumber squared:
$k^2=i\omega\mu_0\sigma$, so the whole apparatus of Helmholtz equations applies —
with the difference from the wave equation that $\sigma$ can vary over orders of
magnitude across a single interface, so the **interface conditions, not the
equation, do the work**.

For a one-dimensional Earth (conductivity a function of depth only), symmetry
splits the problem cleanly. A vertical magnetic dipole (horizontal loop) excites
the **TE** part, in which $\mathbf{E}$ is toroidal and can be derived from a
vertical Hertz vector; a horizontal electric dipole (grounded wire) excites both
TE and TM. This lesson's exact solver treats the TE case, which is the geometry
of the coil systems in [08-05-01](01-frequency-domain-em.md) and
[08-05-05](05-airborne-em.md).

## 2. The layered solution and the admittance recursion

### 2.1 Hankel transform of the source-free problem

Because the medium is layered, we expand in cylindrical harmonics
$J_0(\lambda\rho)$, where $\lambda$ is the horizontal wavenumber. In layer $j$ a
field that is bounded away from the source must be of the form

$$\Pi_j = A_j\,e^{-u_j z}+B_j\,e^{+u_j z},\qquad
u_j=\sqrt{\lambda^2+k_j^2},\qquad k_j^2=i\omega\mu_0\sigma_j,$$

with $\operatorname{Re}u_j>0$ so that the terms decay with distance. Define the
**input admittance** of a stack as $q \equiv -\partial_z\Pi/\Pi$ evaluated at the
top of the stack. This is the single complex number that communicates everything
a stack does to the region above it.

### 2.2 The interface conditions give a recursion

At an interface where $\Pi$ and $\partial_z\Pi$ are continuous (equivalently:
tangential $\mathbf{E}$ and tangential $\mathbf{H}$), matching the two solutions
over a layer of thickness $h$ gives, for a layer of admittance $u_j$ sitting on a
stack of admittance $q_{j+1}$,

$$\boxed{\;q_j=u_j\,
\frac{q_{j+1}+u_j\tanh\left(u_jh_j\right)}
{u_j+q_{j+1}\tanh\left(u_jh_j\right)}.\;}$$

Starting from the bottom halfspace, where $q=u_N$ by definition, the recursion
propagates upward one layer at a time. The same result follows in one line from
the up-to-down amplitude ratio: if the interface at depth $h$ gives
$B/A=e^{-2u_jh}(u_j-u_{j+1})/(u_j+u_{j+1})$, then

$$q_j=u_j\frac{1-B/A}{1+B/A}
=u_j\frac{q_{j+1}+u_j\tanh(u_jh_j)}{u_j+q_{j+1}\tanh(u_jh_j)}.$$

### 2.3 From admittance to a measured response

At the air/ground interface the TE reflection coefficient is

$$R(\lambda)=\frac{\lambda-q_1}{\lambda+q_1},$$

which reduces to $R=(\lambda-u)/(\lambda+u)$ for a homogeneous halfspace — the
coefficient used, and separately verified against image theory, in
[08-05-01](01-frequency-domain-em.md). The response of a coplanar coil pair then
follows from the same Sommerfeld integral as before,

$$S(\omega)=-r^3\int_0^\infty\lambda^2R(\lambda)
e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda,$$

with the large-$\lambda$ behaviour $R_\infty=\lim_{\lambda\to\infty}\lambda^2R$
subtracted analytically: as $\lambda\to\infty$, writing
$q=\lambda+c/\lambda+\dots$ gives $\lambda^2R\to-c/2=:R_\infty$, so

$$S(\omega)=-r^3\left[
\frac{R_\infty}{\sqrt{r^2+4h^2}}
+\int_0^\infty\left(\lambda^2R(\lambda)-R_\infty\right)
e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda\right].$$

For a homogeneous halfspace $R_\infty=-k^2/4$ exactly, which reproduces
[08-05-01](01-frequency-domain-em.md) term by term — a useful consistency anchor.

## 3. Verification of the layered code

A layered solver has three independent anchors, and the demonstration uses all
three. None of them is the response itself, which is the point.

**(a) Reduction to a closed form.** With one layer the recursion must return the
homogeneous halfspace response. At $10$, $100$, $10^3$ and $10^4\ \mathrm{Hz}$ the
two routes agree to $5.55\times10^{-17}$ or better (at $1\ \mathrm{kHz}$ the
difference is exactly $0.00\times10^{0}$).

**(b) Direct elimination of the interface conditions.** For one layer over a
halfspace, write the potentials explicitly and solve for the amplitude ratio
$B/A$; the resulting admittance agrees with the recursion over 20 001
wavenumbers with a maximum relative difference of $6.1\times10^{-16}$ to
$8.6\times10^{-16}$ across the same band. The recursion is algebraically
equivalent to the interface elimination, and the numerics confirm it.

**(c) The matched-layer identity.** If a layer's conductivity equals the
underlying stack's, the admittance must equal $u$ whatever the thickness. For
thicknesses of $0.1$, $10$ and $1000\ \mathrm{m}$ the maximum relative difference
is $3.6\times10^{-16}$, $1.4\times10^{-16}$ and $1.4\times10^{-16}$. This is the
check that catches a sign error in a $u_j\leftrightarrow q_{j+1}$ swap, which the
other two anchors can miss when the layer is thin.

**(d) Limits.** At $100\ \mathrm{Hz}$ over a $0.01\ \mathrm{S\,m^{-1}}$ host the
halfspace response is $+2.48276492\times10^{-4}+i\,2.89099628\times10^{-3}$. A
layer whose conductivity barely differs ($0.0101\ \mathrm{S\,m^{-1}}$, $40\
\mathrm{m}$) moves it by $1.79\times10^{-5}$; a resistive layer
($10^{-6}\ \mathrm{S\,m^{-1}}$, $40\ \mathrm{m}$) by $1.72\times10^{-3}$; a thin
high-conductivity layer ($5\ \mathrm{S\,m^{-1}}$, $0.2\ \mathrm{m}$) by
$4.76\times10^{-4}$; a thick weakly conductive layer
($0.02\ \mathrm{S\,m^{-1}}$, $100\ \mathrm{m}$) by $2.46\times10^{-3}$; and a real
conductor ($0.05\ \mathrm{S\,m^{-1}}$, $40\ \mathrm{m}$) by
$6.82\times10^{-3}$. The ordering tracks the layer conductance, which is the
physical variable — if a code returned these in a different order, the
conductivity would be entering somewhere other than where it belongs.

## 4. Layered responses and departure curves

The demonstration computes the quadrature response of a $40\ \mathrm{m}$ coplanar
pair on the ground over three SYNTHETIC models:

| $f$ (Hz) | halfspace $0.01$ | H-type $0.01/0.002/0.05$ | K-type $0.01/0.05/0.002$ |
|---|---|---|---|
| 10 | 307.4 | 423.7 | 685.9 |
| 100 | 2891.0 | 3123.5 | 6626.5 |
| 1000 | 23252.1 | 18003.8 | 43050.7 |
| 10000 | 81392.6 | 80003.5 | 56293.9 |

(all in ppm of the primary; layer boundaries at $30$ and $90\ \mathrm{m}$).
Relative to the halfspace the H-type model gives $1.38$, $0.77$ and $0.98$ at
$10\ \mathrm{Hz}$, $1\ \mathrm{kHz}$ and $10\ \mathrm{kHz}$; the K-type gives
$2.23$, $1.85$ and $0.69$. **The ratio is not monotone in frequency and its sign
changes**, which is why layered interpretation works with a *departure curve*
(response minus a best-fit halfspace, as a function of frequency) rather than
with a single anomaly number: the shape of the departure, not its size, tells
resistive-over-conductive from conductive-over-resistive.

## 5. Equivalent models, and what the data do not contain

Take a host of $0.01\ \mathrm{S\,m^{-1}}$, a layer starting at $50\ \mathrm{m}$
with conductance $\sigma d=1\ \mathrm{S}$, and vary how the conductance is packed
into thickness. Thin-sheet theory says the response depends only on $\sigma d$.
The exact layered solution says otherwise:

| layer $\sigma$ (S/m) | $d$ (m) | $d/\delta_{\text{layer}}$ | dev. at 10 Hz | 100 Hz | 1 kHz | resolution check |
|---|---|---|---|---|---|---|
| 0.05 | 20 | 0.089 | reference | reference | reference | — |
| 0.5 | 2 | 0.028 | 0.168 | 0.168 | 0.166 | 0.004 |
| 0.02 | 50 | 0.141 | 0.161 | 0.157 | 0.147 | 0.006 |
| 0.01 | 100 | 0.199 | 0.286 | 0.285 | 0.256 | 0.003 |

The "resolution check" column is the largest change in the deviation when the
wavenumber range of the quadrature is multiplied by eight: all values are below
$0.006$, so the tabulated differences are properties of the models, not of the
integration. A fifth model ($\sigma=0.1\ \mathrm{S\,m^{-1}}$, $d=10\ \mathrm{m}$)
is deliberately absent because its own deviation moved by $0.078$ under the same
change — quoting it would have been quoting the quadrature.

The physical conclusion is the one that matters for interpretation: **at
$\sigma d=1\ \mathrm{S}$ and a $20$–$100\ \mathrm{m}$ thickness range, the
conductance is determined but the thickness is not, and the residual dependence
on thickness is $16$–$29\%$.** S-equivalence is an asymptotic limit, approached
as $d/\delta_{\text{layer}}\to0$, not an identity. The departure from the
thin-sheet limit *is* the thickness information in the data; when the departure is
smaller than the noise, the thickness is unresolvable, and reporting one from an
inversion is reporting a prior.

## 6. Linearisation: the integral equation and the Born term

The differential form of Section 1.1 is not the only way to organise the same
physics. Write the conductivity as a background plus an anomaly,
$\sigma=\sigma_b+\Delta\sigma$, and let $G$ be the Green's function of the
background. Then the electric field inside the anomaly satisfies the integral
equation

$$\mathbf{E}(\mathbf{r})=\mathbf{E}_b(\mathbf{r})
+\int_V G(\mathbf{r},\mathbf{r}')\,\Delta\sigma(\mathbf{r}')\,
\mathbf{E}(\mathbf{r}')\,\mathrm{d}V',$$

which is exact and implicit: the unknown field appears under the integral. The
**first-order (Born) approximation** replaces $\mathbf{E}$ inside the anomaly by
$\mathbf{E}_b$, giving an explicit linear map from $\Delta\sigma$ to the
scattered field. That is the basis of Born inversion, of many airborne-EM
"susceptibility/conductivity" products, and of every linearised sensitivity in
[08-05-04 EM Inversion](04-em-inversion.md).

The approximation is exact at zero contrast, and the question that matters is how
fast it fails. The demonstration measures it with the exact layered solution: for
a $20\ \mathrm{m}$ layer at $50\ \mathrm{m}$ depth in a
$0.01\ \mathrm{S\,m^{-1}}$ host at $100\ \mathrm{Hz}$, the response difference
divided by the contrast (normalised at contrast $0.1$) is

| contrast $\Delta\sigma/\sigma_b$ | 0.1 | 0.3 | 0.5 | 1 | 2 | 4 | 9 | 19 |
|---|---|---|---|---|---|---|---|---|
| relative slope | 1.0000 | 0.9814 | 0.9784 | 0.9757 | 0.9731 | 0.9691 | 0.9589 | 0.9363 |

So the linearised response is good to about $2\%$ for contrasts up to a factor of
$1.5$, to $3\%$ up to a factor of $5$, and to $6\%$ at a factor of $20$, for
*this* target. The criterion is not "weak contrast" in the abstract: it is that
the *scattered* field be small compared with the background field, which involves
the anomaly's conductance and its induction number as well as the contrast ratio.
The exact solver is what locates the edge for a particular target, which is why
production EM workflows keep a layered or 3-D exact solver in the loop even when
the inversion is linearised.

## 7. Differential methods: FD and FE on a problem with a known answer

### 7.1 The two discretisations

Reduce the Helmholtz problem to the canonical one-dimensional form

$$u''-\kappa^2u=0,\qquad u(0)=0,\quad u(1)=1,\qquad
u(z)=\frac{\sinh\kappa z}{\sinh\kappa},$$

which contains both the diffusion operator and a boundary-driven solution.

**Finite differences.** Replace the second derivative by the three-point
difference at interior nodes $z_i=ih$:

$$\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}-\kappa^2u_i=0,$$

a tridiagonal complex system solved by the Thomas algorithm in $O(N)$ operations.

**Linear finite elements.** Multiply by a test function $v$, integrate by parts,

$$\int_0^1\left(u'v'+\kappa^2uv\right)\mathrm{d}z=[u'v]_0^1,$$

and use hat functions. On a uniform mesh the element stiffness and mass matrices
are

$$K_e=\frac{1}{h}\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\qquad
M_e=\frac{h}{6}\begin{pmatrix}2&1\\1&2\end{pmatrix},$$

the boundary term vanishes for hat functions that are zero at both ends, and the
assembled system is again tridiagonal. **Both schemes are only as good as their
mesh**, which is why the convergence table below is part of the method and not an
appendix to it.

### 7.2 Measured convergence

With $\kappa=1+3i$ (a complex wavenumber, as in a diffusive EM problem):

| cells | $h$ | FD $L_2$ error | FD max error | FEM $L_2$ error | FEM max error | $L_2$ ratio |
|---|---|---|---|---|---|---|
| 8 | 0.1250 | $1.443\times10^{-2}$ | $2.093\times10^{-2}$ | $1.444\times10^{-2}$ | $2.095\times10^{-2}$ | — |
| 16 | 0.0625 | $3.665\times10^{-3}$ | $5.236\times10^{-3}$ | $3.666\times10^{-3}$ | $5.237\times10^{-3}$ | 3.94 |
| 32 | 0.0312 | $9.181\times10^{-4}$ | $1.311\times10^{-3}$ | $9.181\times10^{-4}$ | $1.311\times10^{-3}$ | 3.99 |
| 64 | 0.0156 | $2.296\times10^{-4}$ | $3.280\times10^{-4}$ | $2.296\times10^{-4}$ | $3.280\times10^{-4}$ | 4.00 |
| 128 | 0.0078 | $5.740\times10^{-5}$ | $8.201\times10^{-5}$ | $5.740\times10^{-5}$ | $8.201\times10^{-5}$ | 4.00 |

Both are second order, as theory requires. Their errors agree to three or four
digits *for this problem*, which is a property of the constant-coefficient
one-dimensional case rather than a general result: at $\kappa=3+9i$ the same
comparison separates the two schemes by about $0.4\%$. The transferable lesson is
the ratio column: **a halving of the mesh must quarter the error, and if it does
not, either the mesh is not in the asymptotic regime or the scheme is
inconsistent.**

### 7.3 Mesh rules that follow

- The smallest physical length in a diffusive EM model is the shortest skin depth
  $\delta=\sqrt{2/(\omega\mu_0\sigma_{\max})}$. Use $5$–$10$ nodes per $\delta$;
  the second-order convergence above is what makes that number, rather than a
  guess, defensible.
- The quadrature in a layered solver has the same duty: it must resolve
  $\lambda\sim1/r$ (geometry), $\lambda\sim|k|$ (diffusion) and
  $\lambda\sim1/d_{\min}$ (the thinnest layer). Omitting the third is the classic
  silent error in thin-layer modelling, and it is how a "16%" equivalence result
  can become "29%".
- Report the change in the answer under a mesh or range refinement. In this
  lesson's tables that column is called a resolution check, and it is the only
  evidence that a quoted number is a property of the model.

## 8. Assumptions and regime of validity

1. **Quasi-static.** $\omega\varepsilon_0/\sigma\ll1$; the criterion and its
   measured margin are in [08-05-01](01-frequency-domain-em.md).
2. **Non-magnetic ground** in the TE formulation used here; magnetic
   susceptibility requires either a modified standard equation or a full
   Sommerfeld treatment.
3. **One-dimensional (layered) Earth** for Sections 2–5. Laterally varying models
   need the differential or integral-equation families of Sections 6–7. A 2-D or
   3-D model's misfit to layered data is not a small correction: it is the
   dominant error in most field surveys, and it is diagnosed, not removed, by
   layered inversions (see [08-05-04](04-em-inversion.md)).
4. **TE only** in the coil geometry. Grounded-wire and marine CSEM sources excite
   TM as well and need both potentials.
5. **The Born approximation (Section 6)** additionally assumes the scattered field
   is small; the measured contrast range above is specific to one target and must
   be re-measured for another.
6. **Dipole sources.** Finite loop size is a separate approximation; its error was
   measured in [08-05-01](01-frequency-domain-em.md) ($0.57\%$ at $a/s=0.05$,
   $10\%$ at $a/s=0.2$).
7. **No dispersion or induced polarisation.** The response is assumed to be
   independent of the transmitter waveform beyond a linear filter.

## 9. Fully worked numeric example

Compute the admittance at $\lambda=0.025\ \mathrm{m^{-1}}$ for the H-type model of
Section 4 at $100\ \mathrm{Hz}$ ($\omega=628.3185\ \mathrm{rad\,s^{-1}}$,
$\mu_0=4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$), where the layer boundaries are at
$30$ and $90\ \mathrm{m}$.

1. Wavenumbers: $k_j^2=i\omega\mu_0\sigma_j$, so
   $k_1^2=i\,7.8957\times10^{-6}$, $k_2^2=i\,1.5791\times10^{-6}$,
   $k_3^2=i\,3.9478\times10^{-5}\ \mathrm{m^{-2}}$.
2. Vertical wavenumbers at $\lambda=0.025$:
   $u_1=0.0250005+0.0001579i$, $u_2=0.0250000+3.16\times10^{-5}i$,
   $u_3=0.0250125+0.0007892i$ (all $\mathrm{m^{-1}}$).
3. Bottom halfspace: $q_3=u_3$.
4. Across the $60\ \mathrm{m}$ second layer,
   $\tanh(u_2\times60)=0.90515+0.00034i$, so
   $q_2=u_2\left(q_3+u_2\tanh\right)/\left(u_2+q_3\tanh\right)
   =0.0250013+6.927\times10^{-5}i$.
5. Across the $30\ \mathrm{m}$ first layer, $\tanh(u_1\times30)
   =0.63517+0.00283i$, so $q_1=0.0250005+0.0001381i$.
6. Reflection coefficient:
   $R=(0.025-q_1)/(0.025+q_1)=-1.8086\times10^{-5}-2.7626\times10^{-3}i$.
   The homogeneous halfspace of the host would give
   $R_{\text{host}}=-1.9948\times10^{-5}-3.1581\times10^{-3}i$: the resistive
   second layer has *raised* the admittance and therefore reduced $|R|$ by about
   $12\%$ at this wavenumber. That reduction, integrated over all $\lambda$ and
   over frequency, is the departure curve of Section 4.

The full quadrature over $\lambda$ gives the tabulated $3123.5\ \mathrm{ppm}$
against the halfspace's $2891.0\ \mathrm{ppm}$, a ratio of $1.08$ at
$100\ \mathrm{Hz}$ — the sign of the H-type departure at low frequency.

## 10. Python demonstration

`code/em_modelling_demo.py` computes everything above. It:

1. builds the layered admittance recursion and verifies it four ways (reduction to
   a closed form, direct interface elimination, the matched-layer identity, and
   the limit table);
2. tabulates H-type and K-type responses against a halfspace;
3. measures the equivalence of equal-conductance models with a resolution check
   on every row;
4. measures the contrast range over which the linearised (Born) response holds;
5. solves the canonical one-dimensional problem by finite differences and linear
   finite elements and reports both convergence orders;
6. states the cost and mesh rules for 1-D, 2-D and 3-D work.

It is print-only, uses no random numbers beyond the fixed seed required by the
module convention (`np.random.default_rng(20261014)`, unused here), needs no
network, and finishes in under a second.

## 11. Exercises

Full sets with worked solutions are in
[`exercises/03-em-modelling-exercises.md`](./exercises/03-em-modelling-exercises.md)
and
[`exercises/03-em-modelling-solutions.md`](./exercises/03-em-modelling-solutions.md).

- **★** Compute $u_j$ for three layers at a stated $\lambda$ and carry the
  recursion through by hand.
- **★★** Prove that the recursion returns $q=u$ for a matched layer of any
  thickness.
- **★★** Derive the finite-element element matrices and verify by hand that the
  assembled system is tridiagonal.
- **★★★** Design a resolution check for a 3-D finite-element EM model that would
  detect a mesh that is too coarse in one direction only.

## Mastery checkpoint

Without notes:

> A layered solver returns a response of $1.0\times10^{-2}+i\,3.0\times10^{-2}$
> for a model with a $25\ \mathrm{m}$ layer of $0.04\ \mathrm{S\,m^{-1}}$ at
> $40\ \mathrm{m}$ depth in a $0.01\ \mathrm{S\,m^{-1}}$ host, at
> $f=500\ \mathrm{Hz}$. **(a)** Name the four checks you would run before
> believing it. **(b)** State what the matched-layer test would return and why it
> catches a class of error the closed-form test misses. **(c)** A colleague
> reports the same response for a $5\ \mathrm{m}$ layer of $0.2\
> \mathrm{S\,m^{-1}}$. What is the conductance of each model, and what does the
> equality of the two responses mean? **(d)** Say which single additional
> frequency would most help separate them, and why.

## Common pitfalls

1. **Reporting a forward model without its mesh or wavenumber range.** A number
   whose resolution is unknown is not a result.
2. **Trusting a limit test alone.** The matched-layer and closed-form tests fail
   in different ways; use both.
3. **Forgetting the third length scale.** In layered modelling the quadrature must
   resolve $1/r$, $|k|$ *and* $1/d$; thin layers are where this bites.
4. **Believing S-equivalence.** It is an asymptotic limit; at
   $d/\delta_{\text{layer}}\approx0.1$ the departure is of order $15\%$ (measured).
5. **Using "weak contrast" as the Born criterion.** The measured criterion is a
   statement about the scattered field, not about the ratio of conductivities.
6. **Assuming a mesh convergence rate.** Measure it; second order is a result, not
   a default.
7. **Confusing model error with noise.** In the examples here, equivalence and
   dimensionality errors exceed the noise-driven uncertainty by orders of
   magnitude.

## Related modules

- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md)
  — the response integral this lesson evaluates for a layered Earth.
- [08-05-02 Time-Domain EM (TDEM): Sounding, Transients and Decay Curves](02-time-domain-em.md)
  — the same solvers applied after switch-off.
- [08-05-04 EM Inversion and Dimensionality](04-em-inversion.md) — what the
  ambiguity measured here does to an inversion.
- [08-05-05 Airborne EM for Conductivity Mapping](05-airborne-em.md) — the same
  layered solver with a source at tens of metres' height.
- [05-03-04 Numerical Forward Modelling](../../05-core-geophysics/03-forward-modelling-principles/04-numerical-forward-modelling.md)
  — the general statements about discretisation and validation.
- [01-12-07 PDE Discretisation](../../01-mathematics/12-numerical-methods/07-pde-discretisation.md)
  — the finite-difference and finite-element discretisations used here.
