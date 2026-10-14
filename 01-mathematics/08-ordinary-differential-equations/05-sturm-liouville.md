---
id: 01-08-05
title: "Sturm-Liouville Theory and Eigenfunction Expansions"
level: graduate
prereqs: ["01-08-02", "01-07-06"]
estimated_minutes: 90
tags: [sturm-liouville, eigenfunction-expansion, orthogonal-functions, boundary-value-problem, normal-modes]
---

# Sturm–Liouville Theory and Eigenfunction Expansions

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a second-order linear ODE in self-adjoint (Sturm–Liouville) form
   and identify $p$, $q$ and the weight $w$.
2. **Derive** the Lagrange identity and explain why separated boundary
   conditions make the operator symmetric — and therefore why the
   eigenfunctions are orthogonal.
3. **Compute** the expansion coefficients of an arbitrary function in an
   eigenfunction basis, and state the completeness property that makes the
   expansion valid.
4. **Verify** orthogonality numerically for two concrete problems: the sine
   basis of a slab and the Legendre polynomials.
5. **Use** the Rayleigh quotient as a variational principle, obtain certified
   upper bounds on the lowest eigenvalue from arbitrary trial functions, and
   assess convergence of a Rayleigh–Ritz calculation.
6. **Recognise** the same structure in heat-conduction modes, vibrating
   strings, and the spheroidal and toroidal free oscillations of the Earth, and
   explain why a modal expansion is the natural solution method for each.

## Prerequisites

- [02 Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) —
  the scalar equation whose "frequency" becomes an eigenvalue here.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md) —
  the finite-dimensional analogue this lesson generalises to operators.
- [01-05-05 Integration Techniques and Definite Integrals](../05-single-variable-calculus/05-integration.md) —
  the quadrature used for every inner product below.

## 1. Intuition: the eigenvalue problem behind every modal method

Pushing a lever eigenproblem through a scalar oscillator gives one frequency.
Do the same for a *continuum* — a string, a bar, the whole Earth — and you get
an infinite set of frequencies, indexed by an integer, each with its own
spatial shape. Sturm–Liouville theory is the theorem that this works: that a
large class of physical boundary-value problems has a discrete, ordered,
complete set of real eigenvalues and orthogonal eigenfunctions, so that any
admissible initial state can be written as a sum of modes.

Everything modal in geophysics rests on that theorem. The free oscillations of
the Earth are spheroidal and toroidal modes. Heat conduction into a half-space
or a slab is a sum of decaying modes. A vibrating string, a standing wave in a
lake, and a waveguide mode in a borehole are all eigenfunctions of a
Sturm–Liouville operator. And the ordinary Fourier series of
[01-10-01](../10-fourier-analysis/01-fourier-series.md) is the special case
$p = w = 1$, $q = 0$.

The practical payoff is a solution method with three steps, and the rest of
this lesson is spent justifying each:

1. Find the eigenvalues $\lambda_n$ and eigenfunctions $y_n(x)$.
2. Expand the initial condition in the $y_n$, using orthogonality to get the
   coefficients.
3. Evolve each mode separately, because in a linear problem the modes do not
   interact.

## 2. Definitions

### 2.1 Self-adjoint form

The **Sturm–Liouville problem** on an interval $[a,b]$ is

$$\boxed{\;-\frac{d}{dx}\left(p(x)\frac{dy}{dx}\right) + q(x)\,y
= \lambda\,w(x)\,y\;}$$

together with boundary conditions, where $p$ is positive and continuously
differentiable on $(a,b)$, $q$ is continuous, and $w>0$ is the **weight
function**. The eigenvalue $\lambda$ multiplies $w$, and $w$ is what makes the
orthogonality relation non-trivial:

$$\int_a^b y_m(x)\,y_n(x)\,w(x)\,dx = 0 \quad (m \neq n).$$

The boundary conditions are **separated** (or *Sturm*) if each is imposed at
one endpoint:

$$\alpha_1y(a) + \alpha_2y'(a) = 0, \qquad
\beta_1y(b) + \beta_2y'(b) = 0 .$$

Dirichlet ($y=0$), Neumann ($y'=0$) and Robin ($\alpha y + \beta y' = 0$) are
all of this form. If $p(a)=0$ or $p(b)=0$ the interval endpoint is
**singular**, and the requirement that the solution be bounded there replaces a
condition; the Legendre problem below is of this kind.

**Not every second-order equation arrives in self-adjoint form**, but almost
every one can be put there. Given

$$A(x)y'' + B(x)y' + C(x)y + \lambda D(x)y = 0,$$

multiply by $\exp\!\left(\int (B/A)\,dx\right)/A$ to obtain the form above.
The integrating factor from
[01 First-Order ODEs](./01-first-order-odes.md) is doing the same job in a
simpler setting: both are ways of writing an equation so that its operator is
symmetric.

### 2.2 The Lagrange identity

For two functions $y$ and $z$, define the **Lagrange bracket**

$$\{y,z\} \equiv p(x)\left(z\,y' - y\,z'\right).$$

Then a two-line calculation (Section 3.1) gives the **Lagrange identity**

$$y\,L[z] - z\,L[y] = \frac{d}{dx}\{y,z\},$$

where $L[y] = -(py')' + qy$. Integrating,

$$\int_a^b\left(y\,L[z] - z\,L[y]\right)dx = \{y,z\}\Big|_b - \{y,z\}\Big|_a .$$

**If the boundary term vanishes, $L$ is symmetric**: the left side is zero for
every pair of eigenfunctions, and choosing $y = y_m$, $z = y_n$ with
$L[y_n] = \lambda_nwy_n$ gives

$$(\lambda_n - \lambda_m)\int_a^bw\,y_my_n\,dx = 0 .$$

So distinct eigenvalues give orthogonal eigenfunctions, and that is the whole
reason orthogonality works: **it is a boundary statement, not a property of
sines or Bessel functions.**

## 3. Derivations, step by step

### 3.1 The Lagrange identity, verified numerically

Check it for $p=1$, $q=0$, $y = \sin\pi x$, $z = \sin 2\pi x$ on $[0,1]$. Both
satisfy Dirichlet conditions, so the boundary term should vanish. The
demonstration evaluates both sides by Simpson quadrature with 20 000 intervals
and obtains

$$\text{left side} = -2.4\times10^{-15}, \qquad \text{boundary term} = 0,
$$

which is the round-off floor. Then it repeats the calculation with
$y_2 = \cos\pi x$, which does **not** satisfy $y(0)=0$, and finds

$$\text{left side} = 12.566371, \qquad \text{boundary term} = 12.566371,$$

agreeing to six decimals and equal to $4\pi$. **The boundary term is not a
technicality.** It is the difference between an operator that has an orthogonal
basis and one that does not, and a mixed boundary condition can destroy
symmetry even for the same differential expression.

### 3.2 The sine basis on a slab

Take $p=w=1$, $q=0$ on $[0,L]$ with $y(0)=y(L)=0$. Then the problem
$-y'' = \lambda y$ has the claimed solution family

$$\lambda_n = \left(\frac{n\pi}{L}\right)^2, \qquad
y_n(x) = \sin\!\left(\frac{n\pi x}{L}\right), \qquad n = 1,2,3,\dots$$

The demonstration substitutes each claimed eigenfunction into a fourth-order
finite-difference approximation of $-y''$ at $x_0 = 0.37$ and reports the
residual. With $L = 1$:

| $n$ | $\lambda_n$ | $-y_n''(x_0)$ | $\lambda_ny_n(x_0)$ | residual |
|---|---|---|---|---|
| 1 | 9.869604 | 9.057875093 | 9.057875093 | $-5.3\times10^{-11}$ |
| 2 | 39.478418 | 28.778527893 | 28.778527894 | $-9.9\times10^{-10}$ |
| 3 | 88.826440 | $-30.088883413$ | $-30.088883416$ | $3.1\times10^{-9}$ |
| 4 | 157.913670 | $-157.602063817$ | $-157.602063861$ | $4.4\times10^{-8}$ |
| 5 | 246.740110 | $-112.017665781$ | $-112.017665857$ | $7.6\times10^{-8}$ |

**The residuals grow with $n$, and that is expected.** The truncation error of
the stencil scales as $h^4y^{(6)}$, and $y^{(6)} \propto n^6$, so a check at
high mode number costs accuracy. The largest residual, $7.6\times10^{-8}$, is
still eight orders below the size of the terms being cancelled, so the check
is conclusive — but the growth pattern is the reason one should not simply
tighten a tolerance for higher modes and expect it to pass.

Orthogonality is then verified by quadrature:

$$\int_0^1\sin(n\pi x)\sin(m\pi x)\,dx = \begin{cases}0.5 & n=m\\ 0 & n\neq m\end{cases}$$

The demonstration obtains exactly $0.500000000$ on the diagonal and values at
the $10^{-13}$ floor off it.

### 3.3 A singular problem: Legendre's equation

Legendre's equation in self-adjoint form is

$$-\frac{d}{dx}\left[(1-x^2)\frac{dy}{dx}\right] = \lambda y, \qquad
x\in[-1,1],$$

so $p(x) = 1-x^2$ vanishes at both endpoints: the problem is **singular** at
both ends, and the boundary condition is that $y$ stay bounded. The solutions
are the Legendre polynomials $P_n$ with

$$\lambda_n = n(n+1), \qquad n = 0,1,2,\dots$$

The demonstration verifies the differential equation with a fourth-order
nested stencil at $x = 0.3$, $h = 10^{-2}$:

| $n$ | $n(n+1)$ | residual |
|---|---|---|
| 0 | 0 | $-0.0\times10^{0}$ |
| 1 | 2 | $-1.6\times10^{-14}$ |
| 2 | 6 | $3.1\times10^{-13}$ |
| 3 | 12 | $-2.3\times10^{-13}$ |
| 4 | 20 | $-7.0\times10^{-7}$ |
| 5 | 30 | $-3.0\times10^{-6}$ |
| 6 | 42 | $2.6\times10^{-6}$ |

and orthogonality with weight $w=1$:

$$\int_{-1}^{1}P_n(x)P_m(x)\,dx = \frac{2}{2n+1}\delta_{nm},$$

obtaining $2.000000000$ for $n=m=0$, $0.666666667$ for $n=m=1$,
$0.400000000$ for $n=m=2$ and $0.285714286$ for $n=m=3$ — against
$2/3$, $2/5$ and $2/7$ respectively.

**The structural difference from the sine problem matters.** The Legendre
eigenfunctions are not sines; the weight is 1 but the coefficient $p$ varies;
and the eigenvalue spacing is $n(n+1)$, quadratic like the sine case but with a
different constant. Any claim that "orthogonal eigenfunctions are always
sinusoidal" is refuted by this one example. What *is* general is the existence
of a complete orthogonal family with a weight — that is the theorem.

### 3.4 Eigenfunction expansion and its convergence

Given a complete orthogonal family $\{y_n\}$ with weight $w$, the expansion of
an admissible $f$ is

$$f(x) = \sum_{n=1}^\infty b_n\,y_n(x), \qquad
b_n = \frac{\int_a^b f\,y_n\,w\,dx}{\int_a^b y_n^2\,w\,dx} .$$

Take $f(x)=1$ on $(0,1)$ expanded in the sine basis. The coefficients are

$$b_n = 2\int_0^1\sin(n\pi x)\,dx = \frac{2(1-\cos n\pi)}{n\pi}
= \begin{cases}\dfrac{4}{n\pi} & n\ \text{odd}\\[2mm] 0 & n\ \text{even}\end{cases}$$

so only odd modes appear. The demonstration reports the $L^2$ error and the
peak value as the number of retained modes grows:

| $N$ (odd modes, $n\le N$) | $L^2$ error | ratio to $N=1$ | max value |
|---|---|---|---|
| 1 | $4.352\times10^{-1}$ | 1.000 | 1.273240 |
| 3 | $3.152\times10^{-1}$ | 1.381 | 1.200422 |
| 11 | $1.836\times10^{-1}$ | 2.371 | 1.181298 |
| 51 | $8.827\times10^{-2}$ | 4.931 | 1.178958 |
| 101 | $6.302\times10^{-2}$ | 6.907 | 1.178617 |
| 501 | $2.838\times10^{-2}$ | 15.337 | 1.178965 |
| 1001 | $2.005\times10^{-2}$ | 21.711 | 1.178976 |

Three facts are worth extracting, and all three are general:

1. **The error falls like $N^{-1/2}$.** Between $N = 101$ and $N = 1001$ — a
   factor of 10 in $N$ — the error falls by $3.14$, against $\sqrt{10}=3.162$.
   For a function with a jump discontinuity the coefficients decay like $1/n$,
   and $L^2$ error accumulates as $\left(\sum_{n>N}n^{-2}\right)^{1/2} \sim
   N^{-1/2}$. **Convergence is guaranteed but slow, and the *rate* is set by
   the smoothness of $f$**, which is the central lesson of
   [01-05-07 Sequences, Series and Convergence Tests](../05-single-variable-calculus/07-sequences-and-series.md).
2. **The overshoot does not go away.** The peak settles at $1.178976$ and
   stays there. The demonstration computes the Wilbraham–Gibbs constant
   directly, $(2/\pi)\int_0^\pi (\sin t/t)\,dt = 1.178980$, and the table's
   limit matches it. For a jump of magnitude $J$ the overshoot is about
   $0.0895\,J$; here $J=2$ because the sine series is the odd $2$-periodic
   extension. **The error at the discontinuity is $O(1)$ in the sup norm no
   matter how many modes are kept.** Convergence in $L^2$ and uniform
   convergence are different properties.
3. **Even modes are absent by symmetry.** Only the coefficients that respect
   the symmetry of $f$ survive. Recognising this before computing saves half
   the work and is the reason modal expansions are done in
   symmetry-adapted bases.

### 3.5 The Rayleigh quotient: a certified bound from an arbitrary guess

Multiply the Sturm–Liouville equation by $y$ and integrate by parts:

$$\lambda = \frac{\displaystyle\int_a^b\left[p\,(y')^2 + q\,y^2\right]dx
+ \left[-p\,y\,y'\right]_a^b}
{\displaystyle\int_a^bw\,y^2\,dx} .$$

With separated boundary conditions the bracket vanishes, leaving the
**Rayleigh quotient**

$$R[y] = \frac{\int_a^b\left[p\,(y')^2 + q\,y^2\right]dx}
{\int_a^b w\,y^2\,dx}, \qquad
\lambda_1 = \min_{y}R[y],$$

the minimum being taken over all admissible, non-zero functions. The equality
$\lambda_1 = \min R[y]$ is the **variational characterisation** of the lowest
eigenvalue, and it turns a differential equation into an optimisation problem.

Worked example, $p=w=1$, $q=0$ on $[0,1]$, where $\lambda_1 = \pi^2 =
9.869604401$. With the one-term trial $y = x(1-x)$ the demonstration obtains

$$R[x(1-x)] = 10.000000000,$$

an excess of 1.32 % over $\lambda_1$ — from a trial function that is not even
close to the true eigenfunction. Now enlarge the trial space to
$\operatorname{span}\{x(1-x),\ x^2(1-x)^2\}$ and solve the generalised
eigenproblem $\det(\mathsf{A}-\lambda\mathsf{B}) = 0$ for the smaller root. The
demonstration finds

$$\lambda_{\text{Ritz}} = 9.869749621,$$

with the corresponding trial vector having coefficient $c = 1.133141$, and
verifies that $R$ of that vector reproduces $9.869749621$ to nine decimals. The
excess over $\lambda_1$ has dropped from 1.32 % to **0.001471 %**.

**Two properties make this a method rather than a curiosity.** First, every
Ritz value is an *upper bound*: the error is always on the safe side, which
matters when the eigenvalue is a physical threshold. Second, enlarging the
trial space lowers the value monotonically toward $\lambda_1$. Nothing about
the argument required an exact eigenfunction, which is why the Rayleigh–Ritz
method is the working tool for eigenvalues of complicated operators (and, in
its finite-element form, for entire industrial codes).

### 3.6 Heat conduction: modal decay and the separation of timescales

The reason modal methods win is visible in the diffusion problem. With
$u(0,t)=u(L,t)=0$ and $\kappa$ the diffusivity,

$$u(x,t) = \sum_{n=1}^{\infty}b_n\sin\!\left(\frac{n\pi x}{L}\right)
\exp\!\left(-\kappa\left(\frac{n\pi}{L}\right)^2t\right).$$

Every mode decays exponentially, and the decay rates are $\kappa\lambda_n$.
For $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and $L = 1$ m the demonstration
prints

| $n$ | $\lambda_n$ | rate $\kappa\lambda_n$ (s⁻¹) | time constant (s) |
|---|---|---|---|
| 1 | 9.8696 | $9.8696\times10^{-6}$ | $1.0132\times10^{5}$ |
| 2 | 39.4784 | $3.9478\times10^{-5}$ | $2.5330\times10^{4}$ |
| 3 | 88.8264 | $8.8826\times10^{-5}$ | $1.1258\times10^{4}$ |
| 4 | 157.9137 | $1.5791\times10^{-4}$ | $6.3326\times10^{3}$ |
| 5 | 246.7401 | $2.4674\times10^{-4}$ | $4.0528\times10^{3}$ |

At $t = 1/(\kappa\lambda_1) = 1.0132\times10^{5}$ s, mode 1 has decayed to
$0.367879$ of its initial amplitude, mode 3 to $1.234\times10^{-4}$, and mode 5
to $1.389\times10^{-11}$. **Long-time behaviour is governed by a single mode**,
which is why the asymptotic cooling of a body is described by one exponential
with one time constant, and why the higher modes appear only in early-time data.
The same reasoning is why the diffusion timescale of a body is $L^2/(\pi^2\kappa)$
and not $L^2/\kappa$ — the $\pi^2$ comes from the first eigenvalue, not from
geometry.

## 4. Physical interpretation

**An eigenvalue is a squared frequency or an inverse time.** In the vibrating
string, $\omega_n = \sqrt{\lambda_n}\,\cdot$(wave speed), so $\lambda_n$ is the
squared angular frequency. In diffusion, $\lambda_n$ is an inverse time
multiplied by $\kappa$. **The same mathematical object plays both roles**, and
that duality is why the heat equation has no oscillation while the wave
equation does: the sign of the time derivative, not the spatial operator,
decides.

**The weight $w$ is a physical distribution.** Where $w$ is mass per unit
length, the orthogonality relation is the statement that modes are orthogonal
with respect to kinetic energy. Where $w$ is heat capacity per unit length, it
is the statement of an energy inner product. Ignoring $w$ — that is, using
$\int y_my_ndx = 0$ when the problem needs $\int y_my_nw\,dx = 0$ — is the most
common error in applying these expansions, and it produces coefficients that
look reasonable and are wrong.

**Completeness is the physical assumption.** The theorem says that the modes
span the space of admissible states, so any initial condition can be expanded.
When it fails — an operator that is not self-adjoint, a problem with a
continuous spectrum — the expansion needs a generalised statement. Two
physically important cases are worth naming: the whole real line (where the
"sum" becomes an integral, the Fourier transform of
[01-10-02](../10-fourier-analysis/02-fourier-transform.md)), and a
non-conservative medium with attenuation (where the modes are complex and
orthogonality must be re-derived with respect to a different inner product).

**The variational principle is why low modes are robust.** $\lambda_1$ is a
minimum, so it is stationary with respect to errors in the trial function:
first-order errors in $y$ produce second-order errors in $\lambda_1$. This is
the reason a rough eigenfunction estimate still gives a good eigenvalue, and
the reason Rayleigh's method historically produced accurate frequencies for
structures long before computers existed.

**The normal modes of the Earth.** The spheroidal and toroidal free
oscillations are eigenfunctions of a Sturm–Liouville-type problem in the radial
coordinate, with $p$ built from elastic moduli and density, and with
eigenvalues $\omega^2$. The index $n$ is the radial order, and the surface
spherical harmonic degree $l$ labels the horizontal pattern. **The theory above
is not an analogy for that problem; it is the problem**, with the simplification
that the Earth's operator is a coupled vector system rather than a scalar
equation. The scalar version's structure — real ordered eigenvalues, orthogonal
eigenfunctions, a variational bound — survives. See
[12-05-01 Free Oscillations of the Earth (Normal Modes)](../../12-global-geophysics-interior/05-earth-tides-rotation-global/01-free-oscillations.md).

## 5. Python demonstration

The companion script is
[`code/sturm_liouville_demo.py`](./code/sturm_liouville_demo.py), standard
library only.

| Section | Claim being tested | Observed result |
|---|---|---|
| 1 | $\lambda_n = (n\pi/L)^2$ for the sine problem | residuals $\le 7.6\times10^{-8}$ for $n = 1\dots5$ |
| 2 | Sine orthogonality | $0.500000000$ on the diagonal; $10^{-13}$ off it |
| 3 | $\lambda_n = n(n+1)$ for Legendre | residuals $\le 3.0\times10^{-6}$ for $n=0\dots6$; $\int P_1^2 = 0.666666667 = 2/3$ |
| 4 | Expansion convergence and Gibbs overshoot | $L^2$ error $2.005\times10^{-2}$ at $N=1001$; peak $\to 1.178976$ vs computed Gibbs constant $1.178980$ |
| 5 | Rayleigh quotient is an upper bound | $R[x(1-x)] = 10.0$; two-term Ritz value $9.869749621$, excess 0.0015 % |
| 6 | Modal decay rates $\kappa\lambda_n$ | mode 1: $1.0132\times10^{5}$ s; mode 5: $4.0528\times10^{3}$ s |
| 7 | Self-adjointness is a boundary statement | separated BCs: boundary term 0, left side $-2.4\times10^{-15}$; non-separated: both $12.566371$ |

Section 4 is the one to study, because it separates three properties that are
routinely conflated. Convergence of the *coefficients* to zero (visible in the
$1/n$ decay) does not give uniform convergence (the Gibbs overshoot persists),
and neither of those is the same as convergence of the *series in $L^2$* (which
does hold, at rate $N^{-1/2}$). A learner who has only seen smooth-function
Fourier series will find the contrast instructive; a practitioner who
reconstructs a discontinuous physical field from a finite mode set needs to know
that the ringing they see is not an error in the coefficients.

> **Breaking exercise.** In Section 5, replace the second trial function with
> $x(1-x)(1-2x)^2$ and predict whether the two-term Ritz value will be lower or
> higher than $9.869749621$. Then compute it. (Hint: think about symmetry.)

## 6. Exercises

Attempt these closed-book. See
[`exercises/05-sturm-liouville-exercises.md`](./exercises/05-sturm-liouville-exercises.md)
and the worked
[`exercises/05-sturm-liouville-solutions.md`](./exercises/05-sturm-liouville-solutions.md).

## 7. Common mistakes

1. **Forgetting the weight function.** Orthogonality is with respect to $w$;
   using $dx$ instead of $w\,dx$ silently gives wrong coefficients for any
   problem with variable density or heat capacity.
2. **Assuming the eigenfunctions are sines.** Legendre polynomials, Bessel
   functions and Chebyshev polynomials are all Sturm–Liouville eigenfunctions
   with non-trigonometric shapes.
3. **Applying a separated boundary condition where the endpoint is singular.**
   At $x = \pm1$ in Legendre's problem, $p$ vanishes and the condition is
   boundedness, not a derivative statement.
4. **Expecting a truncated expansion to converge uniformly at a
   discontinuity.** It cannot; the overshoot is $O(1)$ and the convergence is
   only in $L^2$.
5. **Judging an expansion by the first few terms.** The $1/n$ coefficient decay
   of the square pulse gives an error that only halves as $N$ quadruples.
   Measure the rate, as Section 3.4 does.
6. **Using the trial function's own Rayleigh quotient as an estimate of
   $\lambda_1$ without noting it is an upper bound.** For $\lambda_1$ that is
   safe; for higher eigenvalues a Rayleigh–Ritz value is not bounded in the
   same direction by a naive one-term trial.
7. **Treating the eigenfunction expansion as valid when the operator is not
   self-adjoint.** Absorbing media, advection-dominated problems and
   non-conservative couplings break the symmetry, and the expansion must be
   rebuilt.

## 8. Real-world applications

- **Normal-mode seismology.** Spheroidal and toroidal free oscillations are the
  Sturm–Liouville eigenfunctions of the Earth's radial operator; their
  frequencies constrain the radial structure. See
  [12-05-01 Free Oscillations of the Earth](../../12-global-geophysics-interior/05-earth-tides-rotation-global/01-free-oscillations.md)
  and [06-seismology](../../06-seismology/README.md).
- **Heat conduction and geothermal problems.** The modal solution of Section 3.6
  is how cooling times are computed for sills, lava lakes and boreholes.
  See [05-09-01 Measuring Terrestrial Heat Flow](../../05-core-geophysics/09-geothermal-and-heat-flow-methods/01-heat-flow-measurement.md).
- **Separation of variables for the diffusion and wave equations.** Every
  separation of variables in
  [01-09-05](../09-partial-differential-equations/05-separation-of-variables.md)
  produces a Sturm–Liouville problem for the spatial factor.
- **Spectral methods in modelling.** Modal and spectral expansions are the
  basis of pseudospectral wave propagation and of
  [01-10 Fourier Analysis](../10-fourier-analysis/README.md).
- **Vibration of structures, ice shelves and instrument frames.** Structural
  modes are Sturm–Liouville eigenfunctions, and the variational bound is why
  finite-element eigenvalue estimates are trustworthy.
- **Quantum and atomic analogues.** The same theory with $p = \hbar^2/2m$
  gives the energy eigenvalues of a one-dimensional potential; the mathematics
  does not change when the physics does.

## 9. Further reading

- **Courant, R., & Hilbert, D. *Methods of Mathematical Physics, Vol. I.*
  Wiley.** The chapters on eigenfunction expansions and the variational
  method are the classic treatment, and they establish the completeness
  theorems. Level: advanced.
- **Al-Gwaiz, M. A. *Sturm–Liouville Theory and Its Applications.* Springer.**
  A focused modern account from the definition through the expansion and
  Green's-function construction, with worked examples. Level: graduate.
- **Zettl, A. *Sturm–Liouville Theory.* American Mathematical Society.** The
  rigorous reference, including singular problems, self-adjoint boundary
  conditions and the oscillation theorems. Level: graduate to doctoral.
- **Arfken, G. B., Weber, H. J., & Harris, F. E. *Mathematical Methods for
  Physicists.* Academic Press.** The chapters on orthogonal functions,
  Legendre and Bessel equations, and the Sturm–Liouville problem, with tables
  of the classical families. Level: advanced.
- **Boyce, W. E., & DiPrima, R. C. *Elementary Differential Equations and
  Boundary Value Problems.* Wiley.** The boundary-value chapter gives the
  least intimidating introduction to eigenfunction expansions and their
  convergence. Level: intermediate.
- **Dahlen, F. A., & Tromp, J. *Theoretical Global Seismology.* Princeton
  University Press.** The normal-mode chapter derives the Earth's eigenvalue
  problem and its variational formulation. Level: graduate to doctoral.
- **Carslaw, H. S., & Jaeger, J. C. *Conduction of Heat in Solids.* Oxford
  University Press.** The modal solutions of Section 3.6 in every coordinate
  system a geophysicist is likely to need.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted
> text, and you should confirm current editions and availability through your
> library before citing them yourself.

## 10. Related lessons

- [02 Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) —
  the scalar eigenvalue problem that this lesson generalises.
- [04 Systems of ODEs, Phase Portraits and Stability](./04-systems-of-odes.md) —
  the matrix eigenvalue problem, of which this is the continuum limit.
- [06 Green's Functions and Impulse Response](./06-green-functions.md) —
  the same operator inverted in a different way; the two constructions are
  linked by an eigenfunction expansion of the Green's function.
- [01-09-05 Separation of Variables and Boundary Conditions](../09-partial-differential-equations/05-separation-of-variables.md) —
  where these problems are actually used.
- [01-10-01 Fourier Series and Periodic Decomposition](../10-fourier-analysis/01-fourier-series.md) —
  the trigonometric special case.
- [01-16 Functional Analysis for Inverse Problems](../16-functional-analysis/README.md) —
  the rigorous setting of completeness and self-adjointness.
- [02-03-03 Coupled Oscillators and Normal Modes](../../02-physics/03-oscillations-and-waves/03-coupled-oscillators.md) —
  the finite-degree-of-freedom path to the same idea.

## Self-assessment checklist

- [ ] I can put a second-order equation into self-adjoint form and read off
      $p$, $q$ and $w$. (2.1)
- [ ] I can state and use the Lagrange identity, and say why the boundary term
      must vanish. (2.2, 3.1)
- [ ] I can verify orthogonality numerically for a given family, with the right
      weight. (3.2, 3.3)
- [ ] I can compute expansion coefficients and state the completeness property
      being used. (3.4)
- [ ] I can explain the difference between coefficient convergence, $L^2$
      convergence and uniform convergence, with the Gibbs overshoot as the
      example. (3.4)
- [ ] I can compute a Rayleigh quotient, state that it is an upper bound for
      $\lambda_1$, and set up a two-term Rayleigh–Ritz problem. (3.5)
- [ ] I can turn eigenvalues into decay rates and identify the dominant mode at
      long times. (3.6)
- [ ] I can name the Sturm–Liouville problem behind the Earth's normal modes.
      (Section 4)
