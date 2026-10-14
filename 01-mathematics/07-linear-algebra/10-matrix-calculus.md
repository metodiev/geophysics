---
id: 01-07-10
title: "Matrix Calculus and Sensitivity Derivatives"
level: graduate
prereqs: ["01-07-07", "01-06-01"]
estimated_minutes: 90
tags: [linear-algebra, matrix-calculus, sensitivity, gauss-newton, adjoint]
---

# Matrix Calculus and Sensitivity Derivatives

## Learning objectives

By the end of this lesson you will be able to:

1. **Differentiate** scalar-valued functions of vectors and obtain the gradient in
   closed form, without index-bookkeeping errors.
2. **Write** the Jacobian of a vector-valued function of a vector, and state its
   dimensions and units.
3. **Derive** the gradient of a least-squares misfit as $G^\mathsf{T}(Gm - d)$, and
   show that the normal equations are its stationarity condition.
4. **Apply** the eigenvalue perturbation formula
   $\mathrm{d}\lambda/\mathrm{d}p = v^\mathsf{T}(\partial A/\partial p)v$ and explain
   why no eigenvector derivative is needed.
5. **Derive** a physical sensitivity kernel — the Fréchet derivative of a travel time
   with respect to model parameters — and interpret it geometrically.
6. **Construct** a Gauss–Newton iteration, verify its quadratic convergence
   numerically, and state the conditions under which it fails.
7. **Explain** the adjoint method and count the linear solves it saves over forming an
   explicit Jacobian.

## Prerequisites

[01-07-07 Orthogonality, Projections and Least Squares](./07-orthogonality.md) for the
normal equations whose derivation this lesson completes, and
[01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md)
for the component-level gradient and Jacobian that are here assembled into matrix
form.

## 1. Intuition: the derivative is the thing you must get right

Inversion is an optimisation, and optimisation needs derivatives. The question this
lesson answers is how to write them down *for matrix expressions* — correctly, in a
form a compiler can evaluate, and with a clear statement of what each derivative means
physically.

Two examples set the agenda.

**The misfit gradient.** For $\phi(m) = \tfrac12\|Gm - d\|^{2}$, the gradient is

$$\nabla_m\phi = G^\mathsf{T}(Gm - d) ,$$

and setting it to zero gives the normal equations. A student who memorises the normal
equations can pass an examination; a student who can derive them can handle the
constrained, weighted, nonlinear and regularised variants that no one has memorised.

**The adjoint count.** Suppose a forward model has $10^{4}$ data and $10^{5}$ model
parameters. Forming the full Jacobian explicitly requires $10^{4}$ linear solves of
size $10^{5}$ — about $10^{9}$ operations, and $10^{4}$ times whatever the forward
solver costs. The adjoint method requires two solves, about $2\times10^{5}$ operations,
for a saving factor of $5\times10^{3}$ at that size. That ratio is why gradient-based
inversion of large models is possible at all, and it is nothing more exotic than

$$(Ax)^\mathsf{T}y = x^\mathsf{T}(A^\mathsf{T}y) ,$$

the transpose identity of [01-07-02](./02-matrices-and-operations.md) Section 2.3.

Everything in this lesson is verified against a central finite difference in
[`code/matrix_calculus_demo.py`](./code/matrix_calculus_demo.py). That is not
pedantry: index errors in derivatives are invisible in the code, plausible in the
results, and expensive in a paper. A five-line numerical check is the cheapest
insurance in scientific computing.

## 2. Precise definitions

### 2.1 Layout conventions, and why they must be stated

Let $f : \mathbb{R}^{n} \to \mathbb{R}$ be a scalar function of a vector. The
**gradient** is the $n$-vector of partial derivatives,
$\nabla f = (\partial f/\partial x_1, \dots, \partial f/\partial x_n)^\mathsf{T}$.
This is sometimes called the *denominator layout*: derivatives are arranged to match
the vector being differentiated with respect to.

For a vector-valued function $F : \mathbb{R}^{n} \to \mathbb{R}^{m}$, the
**Jacobian** is the $m \times n$ matrix

$$J_{ij} = \frac{\partial F_i}{\partial x_j} ,$$

so that $F(x + \delta) \approx F(x) + J\delta$ for small $\delta$: the Jacobian is
the matrix of the local linear map, exactly in the sense of
[01-07-02](./02-matrices-and-operations.md). Its units are (units of $F$) per (units
of $x$).

Conventions differ (numerator versus denominator layout, and the placement of
transposes) and the literature is not uniform. **State your convention.** This module
uses denominator layout throughout: gradients are column vectors and the Jacobian is
$\partial F_i/\partial x_j$.

### 2.2 The identities worth knowing

With $a$ a constant vector, $A$ a constant matrix, $x$ a variable vector and
$B$ a constant matrix of compatible shape:

| Expression | Derivative | Notes |
|---|---|---|
| $a^\mathsf{T}x$ | $a$ | linear in $x$ |
| $x^\mathsf{T}a$ | $a$ | the same scalar |
| $Ax$ | $A$ (as a Jacobian) | the map itself |
| $x^\mathsf{T}Ax$ | $(A + A^\mathsf{T})x$ | reduces to $2Ax$ when $A$ is symmetric |
| $x^\mathsf{T}x = \|x\|^{2}$ | $2x$ | the special case $A = I$ |
| $b^\mathsf{T}Ax$ | $A^\mathsf{T}b$ | a classic scalar objective |
| $\tfrac12\|Ax - b\|^{2}$ | $A^\mathsf{T}(Ax - b)$ | the misfit gradient |
| $\log\det A$ | $A^{-\mathsf{T}}$ | $A$ square, invertible; used in covariance estimation |
| $\operatorname{tr}(AB)$ | $B^\mathsf{T}$ | with respect to $A$ |

The third and seventh rows are the ones used constantly. Notice that every identity can
be re-derived in two lines from the definition
$\left.\frac{d}{d\epsilon}F(x + \epsilon\delta)\right|_{\epsilon=0}$ — the *directional
derivative* — which is the safe method when an identity is not memorised and the
tempting method is to guess. Section 3.1 does this for the quadratic form.

### 2.3 The chain rule, in matrix form

If $y = f(x)$ and $z = g(y)$ then

$$J_{z,x} = J_{z,y}\,J_{y,x} ,$$

Jacobians multiplying in the order the maps compose. For a scalar objective
$\phi(m)$ with $d = F(m)$, the chain rule gives
$\nabla_m\phi = J_{F}^{\mathsf{T}}\nabla_d\phi$: the gradient with respect to the model
is the transposed Jacobian applied to the gradient with respect to the data. That single
identity is the engine of every linearised inversion, and the case $F(m) = Gm$ gives
$\nabla_m\phi = G^\mathsf{T}\nabla_d\phi$.

### 2.4 Sensitivity and the Fréchet derivative

For a (possibly nonlinear) forward operator $F$, the **Fréchet derivative** at $m_0$
is the linear operator $J$ with

$$F(m_0 + \delta m) = F(m_0) + J\,\delta m + o(\|\delta m\|) .$$

Physically $J$ is the **sensitivity kernel**: $J_{ij} = \partial F_i/\partial m_j$ is
how much datum $i$ changes per unit change in parameter $j$. In a ray-tomography
setting $J_{ij}$ is the path length of ray $i$ in cell $j$ — the very matrix $G$ of
[01-07-03](./03-systems-and-elimination.md) — and it is exactly the statement that
travel time is linear in slowness along a fixed ray.

### 2.5 Gauss–Newton

For a nonlinear least-squares problem $\min_m \tfrac12\|F(m) - d\|^{2}$, expand to
first order about $m_k$ and minimise the linearised problem:

$$m_{k+1} = m_k + \left(J_k^\mathsf{T}J_k\right)^{-1}J_k^\mathsf{T}\left(d - F(m_k)\right),$$

with $J_k$ the Jacobian at $m_k$. This is Newton's method with the second-derivative
term neglected: the exact Hessian would be $J^\mathsf{T}J + \sum_i r_i\nabla^{2}F_i$,
and Gauss–Newton drops the second sum. The neglect is justified when the residuals
$r_i = d_i - F_i(m)$ are small or the model is nearly linear, and it is the reason
Gauss–Newton converges quadratically for small residuals and linearly (or not at all)
otherwise. Damping the step — Levenberg–Marquardt — restores robustness when
$J^\mathsf{T}J$ is nearly singular.

### 2.6 The adjoint method

To compute the gradient of a scalar objective that depends on a model through the
solution of a linear system $A(m)u = f(m)$: differentiate the system,
$A\,\delta u + (\partial A/\partial m)\delta m\,u = (\partial f/\partial m)\delta m$,
and use the adjoint variable $\lambda$ defined by $A^\mathsf{T}\lambda =
\partial\phi/\partial u$. Then

$$\frac{\mathrm{d}\phi}{\mathrm{d}m} = \frac{\partial\phi}{\partial m} +
\lambda^\mathsf{T}\left(\frac{\partial f}{\partial m} - \frac{\partial A}{\partial m}u
\right),$$

which requires one solve with $A$ and one with $A^\mathsf{T}$ — two solves,
independent of the number of parameters. The transpose in a numerical sense becomes the
*adjoint* in a continuous one, and verifying an adjoint implementation against finite
differences is a standard and necessary test.

## 3. Step-by-step derivations

### 3.1 Every identity, verified

The demonstration checks each derivative against a central difference with step
$h = 10^{-6}$:

| expression | analytic | numerical | max error |
|---|---|---|---|
| $a^\mathsf{T}x$, $a = (1.5, -2.0, 0.5)$, $x = (0.3, -0.7, 1.1)$ | $(1.5, -2.0, 0.5)$ | $(1.5, -2.0, 0.5)$ | $1.645\times10^{-10}$ |
| $x^\mathsf{T}Ax$ with $A$ non-symmetric | $(1.2, -3.1, 1.5)$ | $(1.2, -3.1, 1.5)$ | $3.451\times10^{-11}$ |
| $\tfrac12\|Gm - d\|^{2}$ | $(8.0, 17.0)$ | $(8.0, 17.000000001)$ | $5.999\times10^{-10}$ |
| $Gm$ (Jacobian) | $G$ | $G$ | $1.398\times10^{-10}$ |

The quadratic-form case is worth deriving, because the non-symmetric version is where
people go wrong. Write

$$x^\mathsf{T}Ax = \sum_{i,j}A_{ij}x_ix_j , \qquad
\frac{\partial}{\partial x_k} = \sum_j A_{kj}x_j + \sum_i A_{ik}x_i
= (Ax)_k + (A^\mathsf{T}x)_k ,$$

so $\nabla(x^\mathsf{T}Ax) = (A + A^\mathsf{T})x$, and for symmetric $A$ this is
$2Ax$. The two occurrences of $x_k$ — one as the first index, one as the second — are
what produce the two terms, and dropping one of them is the classic error.

### 3.2 The misfit gradient, and the normal equations

Using the last identity with $A = G$ and $b = d$:

$$\phi(m) = \tfrac12\|Gm - d\|^{2}
\;\Longrightarrow\;
\nabla_m\phi = G^\mathsf{T}(Gm - d) ,$$

verified numerically as $(8.0, 17.0)$. Setting this to zero:

$$G^\mathsf{T}Gm = G^\mathsf{T}d .$$

The normal equations of [01-07-07](./07-orthogonality.md) are not a separate fact to
be memorised; they are the stationarity condition of a quadratic, and this is why the
derivation generalises. Adding a regularisation term $\alpha\|Dm\|^{2}$ gives

$$\nabla_m\left[\tfrac12\|Gm - d\|^{2} + \tfrac{\alpha}{2}\|Dm\|^{2}\right]
= G^\mathsf{T}(Gm - d) + \alpha D^\mathsf{T}Dm ,$$

hence $(G^\mathsf{T}G + \alpha D^\mathsf{T}D)m = G^\mathsf{T}d$: Tikhonov
regularisation, derived in one line rather than looked up. The same procedure with a
weight matrix $W$ gives $G^\mathsf{T}WGm = G^\mathsf{T}Wd$ and with a constraint
$Cm = c$ gives the Lagrange-multiplier system. Only the derivation scales; the
formulas do not.

### 3.3 A physical sensitivity kernel: the reflection travel time

For a horizontal reflector at depth $h$ with constant velocity $v$ above it, the
two-way travel time at offset $x$ is

$$T(x) = \frac{\sqrt{x^{2} + 4h^{2}}}{v} ,$$

so the Jacobian row is

$$\frac{\partial T}{\partial h} = \frac{4h}{v\sqrt{x^{2} + 4h^{2}}} , \qquad
\frac{\partial T}{\partial v} = -\frac{\sqrt{x^{2} + 4h^{2}}}{v^{2}}
= -\frac{T}{v} .$$

At $(h, v) = (1.2, 3.7)$ km and km/s:

| $x$ (km) | $\partial T/\partial h$ (s/km) | $\partial T/\partial v$ (s per km/s) |
|---|---|---|
| 0.0 | $0.540540541$ | $-0.175310446$ |
| 1.0 | $0.498960499$ | $-0.189919649$ |
| 2.0 | $0.415254746$ | $-0.228203058$ |
| 3.0 | $0.337672999$ | $-0.280633641$ |

The numerical Jacobian agrees to $1.154\times10^{-10}$.

The physics in the table: at zero offset $T = 2h/v$, so $\partial T/\partial h = 2/v =
0.5405$ s/km, and $\partial T/\partial v = -2h/v^{2} = -0.1753$ s per (km/s). Moving
to larger offset lengthens the ray, so the travel time becomes relatively *more*
sensitive to velocity and *less* to depth. By $x = 3$ km the depth sensitivity has
fallen by about 38 % and the velocity sensitivity has risen by about 60 %.

That asymmetry is the classic **depth–velocity trade-off**. Over a limited offset
range the two columns of the Jacobian are nearly parallel, $J^\mathsf{T}J$ is nearly
singular, and the inversion cannot separate $h$ from $v$ — which is
[01-07-08](./08-svd.md)'s small singular value, appearing here as a statement about
which offsets were recorded. The remedy is either a wider offset range or a
constraint; there is no third option.

### 3.4 The derivative of an eigenvalue

Let $A(p)$ be symmetric and differentiable in $p$, with eigenpair
$A(p)v = \lambda v$ and $\|v\| = 1$. Differentiating and taking the inner product with
$v$:

$$\frac{\mathrm{d}A}{\mathrm{d}p}v + A\frac{\mathrm{d}v}{\mathrm{d}p}
= \frac{\mathrm{d}\lambda}{\mathrm{d}p}v + \lambda\frac{\mathrm{d}v}{\mathrm{d}p}
\;\Longrightarrow\;
v^\mathsf{T}\frac{\mathrm{d}A}{\mathrm{d}p}v + \lambda\underbrace{v^\mathsf{T}
\frac{\mathrm{d}v}{\mathrm{d}p}_{=\,0}
= \frac{\mathrm{d}\lambda}{\mathrm{d}p} + \lambda v^\mathsf{T}\frac{\mathrm{d}v}
{\mathrm{d}p} ,$$

where $v^\mathsf{T}\mathrm{d}v/\mathrm{d}p = \tfrac12 \mathrm{d}(v^\mathsf{T}v)/
\mathrm{d}p = 0$ because $\|v\| = 1$. Hence

$$\boxed{\;\frac{\mathrm{d}\lambda}{\mathrm{d}p} = v^\mathsf{T}
\frac{\partial A}{\partial p}v\;}$$

**no eigenvector derivative is required.** That is what makes the formula usable on
large problems: an eigenvector derivative costs a solve, while this costs one
matrix–vector product.

Verified for $A(p) = \begin{bmatrix} 2+p & 1 & 0 \\ 1 & 3-p & 0 \\ 0 & 0 &
1+p/2\end{bmatrix}$ at $p = 0.4$: the eigenvalues are $3.504987562$, $1.495012438$,
$1.2$, the largest eigenvector is $(0.671005321,\ 0.741452534,\ 0)$, and

$$\frac{\mathrm{d}\lambda}{\mathrm{d}p} = v^\mathsf{T}\begin{bmatrix} 1 & 0 & 0 \\
0 & -1 & 0 \\ 0 & 0 & 0.5\end{bmatrix}v = -0.0995037190 ,$$

against a finite-difference value of $-0.0995037195$ — agreement to
$4.652\times10^{-10}$.

The physical reading: the sensitivity of a natural frequency to a parameter is the
mode's energy in the part of the operator that the parameter changes. This is the
perturbation formula of normal-mode seismology and of structural stability analysis,
and its geometric content — energy integrated against a perturbation — recurs in the
Born approximation and in kernel-based tomography. See
[06-seismology](../../06-seismology/README.md).

### 3.5 Gauss–Newton, with its convergence rate

Fit $(h, v)$ to travel times at offsets $x = 0, 0.5, 1, 1.5, 2, 3$ km, generated from
$(h, v) = (1.0, 4.0)$, starting from $(1.5, 3.0)$:

| iteration | $h$ | $v$ | $\|r\|$ (s) | $\|$error$\|$ | error/prev$^{2}$ |
|---|---|---|---|---|---|
| 1 | 1.0900667163 | 3.6734621485 | $1.222\times10^{0}$ | $3.387\times10^{-1}$ | — |
| 2 | 1.0062907183 | 3.9689700180 | $2.382\times10^{-1}$ | $3.166\times10^{-2}$ | $0.275941$ |
| 3 | 1.0000436646 | 3.9997334287 | $1.859\times10^{-2}$ | $2.701\times10^{-4}$ | $0.269468$ |
| 4 | 1.0000000027 | 3.9999999810 | $1.482\times10^{-4}$ | $1.922\times10^{-8}$ | $0.263395$ |
| 5 | 1.0000000000 | 4.0000000000 | $1.014\times10^{-8}$ | $2.220\times10^{-16}$ | — |

The last column converges to a constant near $0.26$: that is the signature of
**quadratic convergence**, $\|e_{k+1}\| \approx C\|e_k\|^{2}$, and it is the same
mechanism as Newton's method in
[01-05-07](../05-single-variable-calculus/07-sequences-and-series.md) Section 3.7. The
number of correct digits doubles per iteration: $1$, $2$, $4$, $8$, $16$. Iteration
stops automatically once the error reaches round-off.

The constant $C$ is not a property of the computer; it is determined by the
second-order term of the residual expansion and by the curvature of the forward
operator. Where that curvature is large — and where the residuals are large — the
neglected Hessian term dominates, and Gauss–Newton can diverge. Practical codes add a
line search or a trust region for exactly this reason.

### 3.6 The adjoint, by counting

For a forward problem with $N_d$ data and $N_m$ parameters:

| $N_d$ | $N_m$ | explicit Jacobian | adjoint gradient | saving |
|---|---|---|---|---|
| $10^{3}$ | $10^{4}$ | $10^{3}$ solves, $10^{7}$ operations | $2$ solves, $2\times10^{4}$ operations | $500$ |
| $10^{4}$ | $10^{5}$ | $10^{4}$ solves, $10^{9}$ operations | $2$ solves, $2\times10^{5}$ operations | $5\times10^{3}$ |
| $10^{5}$ | $10^{6}$ | $10^{5}$ solves, $10^{11}$ operations | $2$ solves, $2\times10^{6}$ operations | $5\times10^{4}$ |

The saving grows linearly with the number of data, which is why the adjoint method is
mandatory, not optional, in any large inversion. These are operation counts from a
model in which a solve costs $N_m$ operations; the *ratio* is the robust part of the
claim, and the absolute numbers should be recomputed for a specific solver.

Note the exact statement of the identity required:
$(Ax)^\mathsf{T}y = x^\mathsf{T}(A^\mathsf{T}y)$. A code needs only two operations —
"apply $A$" and "apply $A^\mathsf{T}$" — to run a full gradient-based inversion, which
is why the phrase *matrix-free* is meaningful and why the adjoint is the thing to test
first when a new forward code is written.

## 4. Physical interpretation

**Sensitivity kernels are the physical content of a Jacobian.** $\partial T_i/\partial
m_j$ is the answer to "if I change this cell, how much does this measurement change?"
In ray tomography the answer is geometric — the ray's path length in the cell — and in
potential-field problems it is a smooth, long-ranged kernel falling off as an inverse
power of distance. The shape of the kernel decides everything: which parameters are
resolved (large kernel entries, [01-07-08](./08-svd.md)), how smooth an inversion must
be to be stable, and how deep a source can be detected.

**The eigenvalue perturbation formula is energy against perturbation.** It appears in
normal-mode inversion, in structural stability, in the sensitivity of a buckling load
to a stiffness change, and in the Born approximation of scattering. Recognising the
same formula in all four settings is a substantial saving in reading time.

**The trade-off structure of a Jacobian is a design property.** The depth–velocity
example of Section 3.3 is not specific to reflection seismology; every multiparameter
problem has parameter combinations that the available data cannot separate, and they
are visible as nearly parallel Jacobian columns *before* the inversion is run. Doing
that check — a singular-value decomposition of the Jacobian — is the difference
between designing an experiment and discovering its limitations afterwards.

**Gauss–Newton inherits the conditioning of $J^\mathsf{T}J$.** Each iteration solves a
normal system, so it inherits the squaring of the condition number and all the caveats
of [01-07-05](./05-determinants-inverses.md) Section 3.6 and
[01-07-07](./07-orthogonality.md) Section 3.4. Production codes use QR or an SVD of the
Jacobian, or a damped variant, for exactly that reason. See
[18-inverse-problems](../../18-inverse-problems/README.md).

**The adjoint is the transpose made physical.** "Apply $A^\mathsf{T}$" in a
discretised PDE means "solve the adjoint equation", which is a different physical
problem — a back-propagation in time, or a migration — and it is usually
straightforward to implement but easy to get subtly wrong. The standard test is a dot
product test against finite differences, and no serious code ships without it.

## 5. Python demonstration

The companion script is
[`code/matrix_calculus_demo.py`](./code/matrix_calculus_demo.py), with five sections:
scalar-valued derivatives checked against finite differences, Jacobians for a linear
and a nonlinear model, the eigenvalue perturbation formula, Gauss–Newton with its
convergence rate, and the adjoint cost counting.

The quantified outputs:

| Section | Observed | Interpretation |
|---|---|---|
| 1, linear | gradient $= a$ exactly; max error $1.645\times10^{-10}$ | the finite difference confirms the identity |
| 1, quadratic | $(A + A^\mathsf{T})x = (1.2, -3.1, 1.5)$; error $3.451\times10^{-11}$ | the two index sums are both real |
| 1, misfit | $G^\mathsf{T}(Gm - d) = (8.0, 17.0)$; error $5.999\times10^{-10}$ | the normal equations as a stationarity condition |
| 2, linear Jacobian | $J = G$ to $1.398\times10^{-10}$ | the Jacobian of a linear map is the map |
| 2, reflection kernel | $\partial T/\partial h = (0.540541, 0.498960, 0.415255, 0.337673)$; error $1.154\times10^{-10}$ | depth sensitivity falls, velocity sensitivity rises with offset |
| 3, eigenvalue | analytic $-0.0995037190$ against numerical $-0.0995037195$ | no eigenvector derivative needed |
| 4, Gauss–Newton | error ratio settles at $0.26$; digits double per iteration | quadratic convergence, as Newton |
| 5, adjoint | saving factor $500 \to 5\times10^{4}$ as $N_d$ grows | the transpose identity is why large inversions exist |

> **Breaking exercise.** In Section 3 of the script, add a third model parameter to the
> reflection problem — a constant time shift $\tau$ with $\partial T/\partial\tau = 1$
> — and set the data to a pure time shift of the true model, so that the depth and the
> shift trade off exactly. Predict the singular values of the new Jacobian before
> running: one of them must vanish, and the corresponding singular vector is the trade
> between $h$ and $\tau$. Then verify, and relate the result to the depth–velocity
> trade-off of Section 3.3.

## 6. Exercises

Full set and worked solutions:
[`exercises/10-matrix-calculus-exercises.md`](./exercises/10-matrix-calculus-exercises.md)
and
[`exercises/10-matrix-calculus-solutions.md`](./exercises/10-matrix-calculus-solutions.md).
Four to start with:

**★1.** Differentiate with respect to $x$: (a) $a^\mathsf{T}x$ with
$a = (2, -1, 3)$; (b) $x^\mathsf{T}Ax$ with
$A = \begin{bmatrix} 1 & 2 \\ 0 & 1\end{bmatrix}$; (c) $\|x\|^{4}$; (d)
$b^\mathsf{T}Ax$ with $b = (1,1)$. State the dimensions of each answer.

**★2.** Derive $\nabla_m\tfrac12\|Gm - d\|^{2} = G^\mathsf{T}(Gm - d)$ by writing out
the components, and then derive the regularised normal equations for a penalty
$\alpha\|Dm\|^{2}$.

**★★3.** A gravity station sits at offset $x$ from a buried sphere of radius $R$ and
density contrast $\Delta\rho$ at depth $z$. (a) Write down the vertical gravity
anomaly in the point-mass limit. (b) Compute the derivatives with respect to $z$ and
$R$, stating the units. (c) Evaluate the Jacobian at $x = 0$, $z = 2$ km,
$R = 0.5$ km, $\Delta\rho = 500$ kg/m³ and state which parameter the measurement
constrains better, and why.

**★★4.** A Gauss–Newton iteration has residuals large enough that the neglected
Hessian term matters. Construct a one-parameter example — for instance
$F(m) = e^{m}$ fitted to a datum far from the true value — and (a) compute the
Gauss–Newton step and the exact Newton step analytically; (b) iterate both and report
the convergence for each; (c) state the condition on the residual under which
Gauss–Newton converges quadratically.

**★★★5.** Implement and verify an adjoint. Take the 1-D diffusion problem
$A(m)u = f$ with $A$ tridiagonal and parameterised by the layer diffusivities, and an
objective $\phi = \tfrac12\|Su - d\|^{2}$ with $S$ sampling a subset of nodes.
(a) Implement forward solve, objective, and the adjoint gradient. (b) Verify the
gradient against finite differences using the dot-product test
$\langle A^\mathsf{T}y, x\rangle = \langle y, Ax\rangle$ for random vectors and for the
actual gradient. (c) Report the number of linear solves used by the adjoint gradient
and by an explicit Jacobian, as functions of the number of parameters, and verify the
counts by instrumenting your code.

**★★★6.** Design a two-parameter experiment whose Jacobian is nearly singular, and
quantify the trade-off. (a) Choose a physical parameterisation and a set of
measurements such that two Jacobian columns have a cosine above $0.999$. (b) Report
the singular values and the condition number. (c) With a measurement uncertainty of
1 % of the datum, report the standard deviation of each parameter and of the
difference combination. (d) State what additional measurement would eliminate the
trade-off, and quantify the improvement.

## 7. Common mistakes

1. **Dropping one of the two terms in $\nabla(x^\mathsf{T}Ax)$.** Both index sums
   contribute; the symmetric case hides the error.
2. **Mixing layout conventions without saying so.** Gradient as a row or a column
   changes every transposition in a derivation, and reviewers notice.
3. **Forgetting the units of a Jacobian.** $\partial F_i/\partial m_j$ carries (data
   units) per (model units), and a Jacobian quoted without units cannot be checked.
4. **Assuming Gauss–Newton converges because it is Newton-like.** With large residuals
   the neglected Hessian term dominates and the method can diverge; add damping or a
   line search.
5. **Forming an explicit Jacobian when an adjoint will do.** The saving grows linearly
   with the number of data (Section 3.6).
6. **Implementing an adjoint without a dot-product test.** The transpose identity
   $\langle A^\mathsf{T}y, x\rangle = \langle y, Ax\rangle$ for random $x, y$ is a
   one-line test that catches nearly all adjoint errors.
7. **Treating $\mathrm{d}\lambda/\mathrm{d}p = v^\mathsf{T}(\partial A/\partial p)v$ as
   valid for repeated eigenvalues.** At a degeneracy the eigenvectors are not
   differentiable and the formula fails; the correct statement involves the
   $2\times2$ subspace.
8. **Using an eigenvector derivative that is only defined up to a scale.** Eigenvectors
   are defined up to a sign and, for a defective matrix, not at all.
9. **Ignoring the second derivative when computing an uncertainty.** A gradient gives a
   direction, not a covariance; the covariance comes from the curvature, as
   [01-07-08](./08-svd.md) Section 2.5 shows.

## 8. Real-world applications

- **Full-waveform inversion.** The gradient of the waveform misfit with respect to
  velocity is computed by the adjoint-state method, cross-correlating the forward and
  adjoint wavefields — a direct application of Section 2.6 at industrial scale. See
  [06-seismology](../../06-seismology/README.md).
- **Travel-time and amplitude tomography.** The Jacobian is the ray-path matrix; its
  transposed application is back-projection, which is why the same matrix serves
  forward modelling and inversion. See [18-inverse-problems](../../18-inverse-problems/README.md).
- **Normal-mode inversion.** The eigenvalue perturbation formula of Section 3.4 gives
  the sensitivity of a mode's frequency to a structural parameter, and it is the basis
  of free-oscillation inversions for the deep Earth. See
  [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md).
- **Potential-field inversion.** Gravity and magnetic kernels are the derivatives of a
  Green's function with respect to source position and density; their very smoothness is
  what makes the problem ill-posed. See
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Neural-network and variational training.** Backpropagation *is* the adjoint method
  applied layer by layer; the reverse-mode automatic differentiation that a modern
  machine-learning framework implements is the discrete version of Section 2.6. See
  [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md).
- **Optimal experimental design.** Choosing source and receiver positions to maximise
  the information in $J$ — for instance by maximising $\det(J^\mathsf{T}J)$ or
  minimising its condition number — is a matrix-calculus problem, and the derivative
  identities of Section 2.2 are exactly what an optimisation needs. See
  [11-exploration-geophysics](../../11-exploration-geophysics/README.md).
- **Stability and modal analysis.** The sensitivity of a structure's vibration
  frequencies to stiffness or mass changes, with the perturbation formula as the
  workhorse.

## 9. Further reading

- **Magnus, J. R., & Neudecker, H. *Matrix Differential Calculus with Applications in
  Statistics and Econometrics* (3rd ed.). Wiley.** The systematic reference, including
  a careful account of layout conventions. Level: advanced.
- **Petersen, K. B., & Pedersen, M. S. *The Matrix Cookbook*.** Widely circulated
  technical report; a compact catalogue of the identities in Section 2.2. Verify each
  identity you use against a finite difference rather than trusting a catalogue.
  Level: reference.
- **Nocedal, J., & Wright, S. J. *Numerical Optimization* (2nd ed.). Springer.**
  Chapters 3, 10 and 11 for Gauss–Newton, Levenberg–Marquardt and convergence rates.
  Level: advanced.
- **Trefethen, L. N., & Bau, D. *Numerical Linear Algebra.* SIAM.** Lecture 20 for
  the conditioning of the Gauss–Newton system, and the eigenvalue perturbation material
  earlier. Level: intermediate to advanced.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory.* Academic Press.**
  Linearised inversion, the Jacobian and the Gauss–Newton iteration in the notation of
  geophysics. Level: intermediate.
- **Tarantola, A. *Inverse Problem Theory and Methods for Model Parameter
  Estimation.* SIAM.** The Fréchet derivative as the central object of inverse theory,
  with the adjoint-state formulation. Level: advanced.
- **Plessix, R.-E. (2006). "A review of the adjoint-state method for computing the
  gradient of a functional with geophysical applications." *Geophysical Journal
  International* 167, 495–503.** The standard reference for Section 2.6 in a
  geophysical setting. Level: advanced.
- **Giles, M. B., & Pierce, N. A. (2000). "An introduction to the adjoint approach to
  design." *Flow, Turbulence and Combustion* 65, 393–415.** A clear exposition of the
  adjoint cost argument. Level: advanced.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm editions and current availability through your library
> before citing them yourself.

## 10. Self-assessment checklist

- [ ] I can state my layout convention and apply it consistently.
- [ ] I can differentiate $a^\mathsf{T}x$, $x^\mathsf{T}Ax$, $\|x\|^{2}$, $b^\mathsf{T}Ax$
      and $\tfrac12\|Ax - b\|^{2}$, and verify each against a finite difference.
- [ ] I can derive the normal equations and their regularised and weighted variants
      from the stationarity condition.
- [ ] I can write the Jacobian of a physical forward model, with units.
- [ ] I can derive and apply the eigenvalue perturbation formula, and state when it
      fails.
- [ ] I can describe the depth–velocity trade-off as a statement about Jacobian
      columns, and say what measurement breaks it.
- [ ] I can implement a Gauss–Newton iteration and verify quadratic convergence, and I
      can explain when it will not.
- [ ] I can state the adjoint identity, use it to count solves, and test an adjoint
      implementation.

## 11. Related lessons

- [01-07-02 Matrices, Matrix Multiplication and Linear Maps](./02-matrices-and-operations.md) —
  the transpose identity that the adjoint method rests on.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](./06-eigenvalues.md) — the
  eigenproblem this lesson differentiates.
- [01-07-07 Orthogonality, Projections and Least Squares](./07-orthogonality.md) —
  the linear problem that Section 3.2 re-derives and generalises.
- [01-07-08 Singular Value Decomposition and Rank Truncation](./08-svd.md) — how to
  detect the trade-offs a Jacobian contains before running an inversion.
- [01-07-09 Sparse Matrices and Structured Systems](./09-sparse-matrices.md) — the
  matrix–vector and transposed matrix–vector products an adjoint must provide.
- [01-05-07 Sequences, Series and Convergence Tests](../05-single-variable-calculus/07-sequences-and-series.md) —
  Newton's method, whose quadratic convergence Gauss–Newton inherits.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  the component-level foundations of this entire lesson.
- [01-14 Optimization and Variational Methods](../14-optimization/README.md) —
  what to do when the problem is not a least-squares problem.
- [18-inverse-problems](../../18-inverse-problems/README.md) — where these derivatives
  become a working inversion.
