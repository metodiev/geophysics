# Solutions — 01-09-08 Weak Solutions, Variational Forms and Well-Posedness

> **Read this after attempting the exercises, not before.**
>
> Worked solutions with the reasoning; numbers were computed rather than estimated.
> Conventions: $\langle u,v\rangle = \int_0^1 uv\,dx$; $H^1$ with weak derivatives;
> energy norm $\lVert v\rVert_E = \lVert v'\rVert_{L^2}$.

---

## ★1 — A weak formulation with a lower-order term

**Strong form.** $-u'' + u = f$ on $(0,1)$, $u(0) = u(1) = 0$.

**Weak form.** Multiply by a test function $v$, integrate over $(0,1)$, and
integrate the second-derivative term by parts:

$$-\int_0^1 u''v\,dx + \int_0^1 uv\,dx = \int_0^1 fv\,dx
\qquad\Longrightarrow\qquad
\left[-u'v\right]_0^1 + \int_0^1 u'v'\,dx + \int_0^1 uv\,dx
= \int_0^1 fv\,dx .$$

The boundary term vanishes because $v(0) = v(1) = 0$. So:

> Find $u\in H^1_0(0,1)$ such that
> $$a(u,v) := \int_0^1\left(u'v' + uv\right)dx = \int_0^1 fv\,dx =: \ell(v)
> \qquad\text{for all } v\in H^1_0(0,1).$$

**Spaces.** The trial space is $H^1_0(0,1)$ and the test space is the same
(Galerkin). The right-hand side $\ell$ is defined for $f\in L^2$, and more generally
for $f\in H^{-1}$ — the dual of $H^1_0$, which is where point sources live.

**Which condition is essential.** $u(0) = u(1) = 0$ is **essential**: it is imposed
by restricting the trial and test spaces. There is no natural condition here,
because the boundary term vanished identically: for Dirichlet data the problem has
no flux to supply. If the boundary condition at, say, $x=1$ were instead
$u'(1) = g$, the boundary term would contribute $-u'(1)v(1) = -g\,v(1)$ to the
right-hand side, and that condition would be **natural** — imposed through the
equation rather than through the space.

**Why the lower-order term matters for well-posedness.** The form is now
$a(v,v) = \lVert v'\rVert_{L^2}^2 + \lVert v\rVert_{L^2}^2 = \lVert v\rVert_{H^1}^2$,
so coercivity holds with constant $1$ and does **not** need Poincaré. That is the
practical meaning of adding the $u$ term: it makes the operator positive definite on
all of $H^1$ rather than only on $H^1_0$, which is why the Helmholtz-type equations
of geophysics are usually posed with a positive lower-order term (a "mass" or
"damping" term) — it is what makes them well posed without a Dirichlet condition.

---

## ★2 — A function with a corner

**Weak derivative.** With $u(x) = \lvert x-\tfrac12\rvert$,
$u = \tfrac12 - x$ on $(0,\tfrac12)$ and $u = x-\tfrac12$ on $(\tfrac12,1)$. For any
test function $v$ with compact support in $(0,1)$,

$$-\int_0^1 u\,v'\,dx = -\left[\int_0^{1/2}\left(\tfrac12-x\right)v'\,dx
+ \int_{1/2}^1\left(x-\tfrac12\right)v'\,dx\right] .$$

Integrating each by parts (the boundary terms at $0$ and $1$ vanish because $v$ has
compact support, and the terms at $\tfrac12$ combine):

$$-\int u\,v'\,dx = \int_0^{1/2}(-1)v\,dx + \int_{1/2}^1(+1)v\,dx
= \int_0^1 w\,v\,dx
\quad\text{with}\quad
w(x) = \begin{cases}-1, & x<\tfrac12,\\ +1, & x>\tfrac12.\end{cases}$$

So the **weak derivative** is $w = -1$ on $(0,\tfrac12)$ and $+1$ on
$(\tfrac12,1)$ — a step function, which is in $L^2$ even though $u$ has no classical
derivative at $x = \tfrac12$. (The value of $w$ at the single point $x=\tfrac12$ is
immaterial: $L^2$ functions are defined up to sets of measure zero.)

**The $H^1$ norm.**

$$\int_0^1 u^2\,dx = 2\int_0^{1/2}\left(\tfrac12-x\right)^2dx
= 2\cdot\frac{(1/2)^3}{3} = \frac{1}{12}, \qquad
\int_0^1 w^2\,dx = 1 ,$$

$$\lVert u\rVert_{H^1} = \sqrt{\frac{1}{12} + 1} = \sqrt{1.0833\ldots}
= 1.04083 .$$

**Is $u\in H^1_0$?** No. $H^1_0(0,1)$ contains the $H^1$ functions that vanish at
the endpoints. Here $u(0) = \tfrac12$ and $u(1) = \tfrac12$, so $u\notin H^1_0$.
This is not a technicality: a function that is nonzero at a boundary cannot be a
Dirichlet trial function, and if one is used as though it were, the resulting
solution converges to the wrong limit (with an $O(1)$ boundary-layer error that does
not shrink under refinement). A useful corollary for practice: the *interpolant* of a
prescribed boundary datum lies in $H^1$ but not in $H^1_0$, which is why Dirichlet
data must be lifted before the variational problem is posed — the "lifting" step that
converts an inhomogeneous condition into a homogeneous one for the deviation.

---

## ★3 — Stiffness matrix entries

**Diagonal.** On an element containing node $i$, $\varphi_i$ is the linear ramp with
slope $+1/h$ on the left element $(x_{i-1},x_i)$ and $-1/h$ on the right element
$(x_i,x_{i+1})$. So

$$A_{ii} = \int(\varphi_i')^2dx
= \int_{x_{i-1}}^{x_i}\left(\frac{1}{h}\right)^2dx
+ \int_{x_i}^{x_{i+1}}\left(-\frac{1}{h}\right)^2dx
= \frac{1}{h} + \frac{1}{h} = \frac{2}{h} .$$

**Off-diagonal, adjacent nodes.** On the single element $(x_i,x_{i+1})$ both hats are
nonzero: $\varphi_i$ has slope $-1/h$ there and $\varphi_{i+1}$ has slope $+1/h$, so

$$A_{i,i+1} = \int_{x_i}^{x_{i+1}}\left(-\frac{1}{h}\right)\left(\frac{1}{h}\right)dx
= -\frac{1}{h} .$$

**Non-adjacent nodes.** $A_{ij} = 0$ for $\lvert i-j\rvert\ge2$, because the two hats
have disjoint supports.

**The matrix.** $A = h^{-1}\,\mathrm{tridiag}(-1,2,-1)$, exactly the classical
second-difference matrix scaled by $1/h$ — which is why a finite-element solution of
Poisson's equation in one dimension with linear elements and a *lumped* load vector
reproduces the finite-difference solution. Two remarks:

- **the two methods are the same only here.** In one dimension, with linear
  elements, constant coefficients and a uniform mesh, the equivalence is exact for
  the stiffness matrix; the load vectors differ (the consistent load is the element
  average of $f$, the lumped load is $h\,f(x_i)$), and in two or three dimensions
  with irregular meshes the finite-element method is not a difference scheme at all;
- **the symmetry is physical.** $A_{ij} = A_{ji}$ reflects the symmetry of the
  bilinear form, which in turn reflects reciprocity: the same stiffness matrix
  couples $i$ to $j$ and $j$ to $i$. Losing that symmetry (a sign error in the
  assembly, or a non-symmetric boundary treatment) is immediately visible as a
  non-symmetric matrix, which is the first thing to check after assembling.

---

## ★4 — Lax–Milgram and the Neumann problem

**The hypotheses.** For a Hilbert space $V$ and a bilinear form $a(\cdot,\cdot)$:

1. **Boundedness (continuity):** there is $C<\infty$ with
   $\lvert a(u,v)\rvert\le C\lVert u\rVert_V\lVert v\rVert_V$ for all $u,v$.
2. **Coercivity (ellipticity):** there is $c>0$ with
   $a(v,v)\ge c\lVert v\rVert_V^2$ for all $v$.

If both hold and $\ell$ is a bounded linear functional, the theorem gives existence,
uniqueness and the stability bound $\lVert u\rVert_V\le c^{-1}\lVert\ell\rVert_{V^*}$.

**Which fails for the pure Neumann problem.** Coercivity. For
$a(u,v) = \int u'v'\,dx$ on $H^1$ (no boundary restriction), take $v\equiv1$:

$$a(1,1) = \int(\text{const})'^2dx = 0, \qquad\text{but}\qquad
\lVert 1\rVert_{H^1}^2 = 1 \ne 0 .$$

So no positive $c$ works, and the theorem does not apply. **Physical meaning:** the
constant function is a genuine solution of the homogeneous problem — adding a
constant to the potential changes no field, so the solution is not unique. This is
exactly the Neumann non-uniqueness proved in
[01-09-04](../exercises/04-laplace-poisson-solutions.md) ★★5, appearing here as the
failure of a hypothesis.

**What replaces the theorem's conclusion.** Two standard repairs:

1. **Restrict the space.** Work on the quotient $H^1/\mathbb{R}$ (functions modulo
   constants) or fix the mean value by adding the constraint $\int u = 0$. On that
   space, Poincaré's inequality supplies coercivity with
   $c = 1/(1+\pi^{-2})$, and Lax–Milgram applies. Uniqueness then holds for the
   *equivalence class*, i.e. for the field rather than the potential.
2. **Add a lower-order term**, as in ★1: with $a(u,v) = \int(u'v' + uv)\,dx$,
   coercivity holds on all of $H^1$ and the problem becomes well posed without any
   boundary restriction. This is the mathematical reason such terms appear in
   physical models as damping, mass or absorption.

At the discrete level the same statement appears as a zero eigenvalue of the
stiffness matrix with the constant vector as eigenvector, and the practical
consequence is a singular linear system — solvable only with a constraint, a
regularisation, or an iterative method that is allowed to leave the constant
component unconstrained.

---

## ★★5 — Adjoint of the Laplacian with Robin data

**Setup.** $L = -d^2/dx^2$ acting on functions satisfying $u'(0) = hu(0)$ and
$u(1) = 0$. Compute $\langle Lu,v\rangle = -\int_0^1 u''v\,dx$ and integrate by
parts:

$$\langle Lu,v\rangle = -\left[u'v\right]_0^1 + \int_0^1u'v'\,dx
= -u'(1)v(1) + u'(0)v(0) + \int_0^1u'v'\,dx .$$

Apply the boundary conditions to the *first* factor: $u(1) = 0$ and
$u'(0) = hu(0)$,

$$\langle Lu,v\rangle = -u'(1)v(1) + h\,u(0)v(0) + \int_0^1u'v'\,dx .$$

Now the same computation with the roles exchanged,
$\langle u,Lv\rangle = -u(1)v'(1) + u(0)v'(0) + \int_0^1u'v'\,dx$, and impose the
conditions on the *second* factor: $v'(0) = hv(0)$, $v(1) = 0$:

$$\langle u,Lv\rangle = u(0)v'(0) + \int_0^1u'v'\,dx
= h\,u(0)v(0) + \int_0^1u'v'\,dx .$$

Subtracting,

$$\langle Lu,v\rangle - \langle u,Lv\rangle = -u'(1)v(1) ,$$

which vanishes because $v(1) = 0$. Therefore $\langle Lu,v\rangle = \langle u,Lv\rangle$
for all $u,v$ in the admissible class:

**the operator is self-adjoint** with this pair of boundary conditions.

**Why the Robin condition is self-adjoint but "mixed" data are not.** The key step
was that applying the condition to either factor produced the *same* boundary term
$h\,u(0)v(0)$. That happened because the condition $u'(0) = hu(0)$ is symmetric in
$u$ and $v$ — it is one relation of the same type for each. If instead the boundary
conditions were $u(0) = 0$ at one end and $u'(1) = g$ at the other, then:

$$\langle Lu,v\rangle = -g\,v(1) + \int u'v'\,dx, \qquad
\langle u,Lv\rangle = u(0)v'(0) + \int u'v'\,dx = 0 + \int u'v'\,dx ,$$

using $u(0) = v(0) = 0$ and $u'(1) = v'(1) = g$. The difference is $-g\,v(1)$, which
does **not** vanish in general, so the operator is *not* self-adjoint as an operator
on the constrained space. What happens is that the boundary condition migrates into
the functional: the problem becomes a *natural*-condition problem whose adjoint
carries the flux term. The general rule, established in the lesson's §6.1, is:

> The adjoint of a differential operator is determined by the operator **plus the
> boundary conditions**, and the boundary term in the integration by parts is the
> whole content of the statement.

**Practical consequence.** In an inversion that uses an adjoint solve, the adjoint
must be implemented with the *same* boundary conditions as the forward problem, and
the boundary term must appear in the gradient formula. The identity test used in the
module's demonstration (see ★★★10(a)) — checking
$\langle Lu,v\rangle = \langle u,L^*v\rangle$ numerically on the discrete operators —
takes one line and catches the error class that otherwise survives to publication.

---

## ★★6 — The optimal step for a noisy derivative

**The two error contributions.** From the lesson's measurements, a central difference
of data with noise amplitude $\varepsilon$ has

$$E_{\text{noise}}(h) \approx \frac{c_2\varepsilon}{h}, \qquad
E_{\text{trunc}}(h) \approx c_1h^2 ,$$

where $c_1$ is set by the third derivative of the underlying function and $c_2$ by the
noise's structure (for the module's random-noise test, $c_2\approx1$; the measured
ratios of noise-induced error to $\varepsilon/h$ were $0.982$, $0.976$ and $0.998$).

**Minimise the total.** With $E(h) = c_1h^2 + c_2\varepsilon h^{-1}$ (adding the two
in quadrature gives the same exponent),

$$E'(h) = 2c_1h - c_2\varepsilon h^{-2} = 0
\qquad\Longrightarrow\qquad
h^{\ast} = \left(\frac{c_2\varepsilon}{2c_1}\right)^{1/3} .$$

**Verification that it is a minimum.**
$E''(h) = 2c_1 + 2c_2\varepsilon h^{-3} > 0$ for all $h>0$, so the stationary point is
a minimum (there is no maximum; the function is convex).

**Numbers for $\varepsilon = 10^{-6}$.** Taking $c_1 = c_2 = 1$ (unit-scale smooth
data):

$$h^{\ast} = \left(\frac{10^{-6}}{2}\right)^{1/3} = (5\times10^{-7})^{1/3}
= 7.94\times10^{-3} ,$$

$$E(h^{\ast}) = (7.94\times10^{-3})^2 + \frac{10^{-6}}{7.94\times10^{-3}}
= 6.30\times10^{-5} + 1.26\times10^{-4} = 1.89\times10^{-4} .$$

The two contributions at the optimum are within a factor of two of each other
($6.3\times10^{-5}$ and $1.26\times10^{-4}$), as they must be at a minimum of a sum
of a decreasing and an increasing term.

**Interpretation as a resolution limit.** The minimum error scales as

$$E_{\min} \sim \varepsilon^{2/3} ,$$

since $h^{\ast}\sim\varepsilon^{1/3}$ gives $E\sim (h^{\ast})^2\sim\varepsilon^{2/3}$.
For $\varepsilon = 10^{-6}$ this is $10^{-4}$ — compare with the noise level itself,
$10^{-6}$. **Differentiating data costs four orders of magnitude in accuracy**, and
that loss is intrinsic: no choice of stencil recovers it. The practical
consequences:

- a derivative-based interpretation of noisy data cannot resolve structure below
  about $10^{-4}$ in the derivative when the data are good to $10^{-6}$;
- refining the grid *past* $h^{\ast}$ makes the answer worse, so "use the finest
  grid available" is the wrong instinct for a derivative (it remains right for the
  forward problem);
- the exponent $\tfrac23$ is why smoothing before differentiating is so effective:
  reducing $\varepsilon$ by a factor 100 by averaging reduces $E_{\min}$ by
  $100^{2/3}\approx21$.

**Limits.** The constants $c_1$, $c_2$ depend on the function and on the noise's
spectrum; correlated noise (from processing) behaves quite differently from the
independent noise assumed here, and can change the effective exponent. The estimate
is therefore an order-of-magnitude guide, and the honest practice is to measure the
error-versus-$h$ curve on the actual data rather than to trust the formula.

---

## ★★7 — The Tikhonov filter

**Derivation.** Minimise
$\phi(m) = \lVert Fm-d\rVert^2 + \alpha\lVert m\rVert^2$. The gradient is

$$\nabla\phi = 2F^{\mathsf T}(Fm-d) + 2\alpha m
= 2\left[(F^{\mathsf T}F + \alpha I)m - F^{\mathsf T}d\right] ,$$

and setting it to zero gives the normal equations

$$(F^{\mathsf T}F + \alpha I)m_\alpha = F^{\mathsf T}d
\qquad\Longrightarrow\qquad
\boxed{\ m_\alpha = (F^{\mathsf T}F + \alpha I)^{-1}F^{\mathsf T}d\ }$$

For $\alpha>0$ the matrix is positive definite even when $F^{\mathsf T}F$ is
singular (which it is, for a compact or rank-deficient forward operator), so the
inverse exists. That is the entire stabilisation.

**The filter in the singular-value basis.** Write the singular value decomposition
$F = U\Sigma V^{\mathsf T}$ with singular values $\sigma_n$. Then

$$m_\alpha = V\,\mathrm{diag}\!\left(\frac{\sigma_n}{\sigma_n^2+\alpha}\right)
U^{\mathsf T}d , \qquad\text{i.e.}\qquad
m_\alpha = \sum_n \frac{\sigma_n}{\sigma_n^2+\alpha}\,(u_n^{\mathsf T}d)\,v_n ,$$

so mode $n$ is weighted by $\sigma_n/(\sigma_n^2+\alpha)
= \frac{1}{\sigma_n}\cdot\frac{\sigma_n^2}{\sigma_n^2+\alpha}$: the
**unregularised** inverse weights it by $1/\sigma_n$, and the **filter factor**

$$f_n = \frac{\sigma_n^2}{\sigma_n^2 + \alpha}$$

multiplies that. With $x = \sigma_n/\sqrt{\alpha}$,

$$f(x) = \frac{x^2}{1+x^2} ,$$

which is 0 at $x=0$, $\tfrac12$ at $x=1$, and $\to1$ as $x\to\infty$.

**The two limits.**

- $\sigma_n\ll\sqrt{\alpha}$: $f_n\approx\sigma_n^2/\alpha\ll1$ — the mode is
  **suppressed**. These are the modes whose inverse would have been dominated by
  noise, and they are exactly the (near-)null-space directions of $F$.
- $\sigma_n\gg\sqrt{\alpha}$: $f_n\approx1$ — the mode is **passed unchanged**, so
  well-determined components of the model are not biased.

**Reading the filter.** The parameter $\sqrt{\alpha}$ is the **resolution threshold**:
modes with singular value above it are recovered, modes below it are discarded. The
transition is smooth rather than a sharp cutoff, which is the advantage of Tikhonov
over truncation — no ringing from a hard cut. The bias introduced is
$1-f_n = \alpha/(\sigma_n^2+\alpha)$ per mode, and the total error is
(bias) + (amplified noise):

$$m_\alpha - m_{\text{true}} = -\sum_n\frac{\alpha}{\sigma_n^2+\alpha}
(u_n^{\mathsf T}d_{\text{true}})v_n
+ \sum_n\frac{\sigma_n}{\sigma_n^2+\alpha}(u_n^{\mathsf T}\delta d)v_n .$$

The first term decreases with $\alpha$, the second increases, and the minimum is the
bias–variance trade-off whose optimal $\alpha$ depends on the noise level and on the
true model — which is why the parameter must be chosen by a principled rule
(discrepancy principle, L-curve, generalised cross-validation) rather than by eye.
This is the discrete form of everything in ★1 and ★2 of
[01-09-07](07-boundary-value-problems-solutions.md): **regularisation makes the
operator invertible by filtering the directions in which it is nearly singular, and
the filter threshold is the resolution.**

---

## ★★8 — Galerkin versus interpolant, and a one-dimensional special property

**The verification.** For the problem $-u'' = \pi^2\sin\pi x$, $u(0) = u(1) = 0$,
with $n = 40$ interior nodes ($h = 1/41 = 0.024390$), evaluating the energy-norm
error of the Galerkin solution and of the linear interpolant of the exact solution
by 4-point Gauss quadrature on each element gives

```text
h=0.02439  Galerkin energy err=4.913238e-02  interpolant energy err=4.913238e-02  ratio=1.0000
```

The two errors are equal to machine precision — measured, at three mesh sizes, as
ratio $-1 = 0$ to within $\pm4\times10^{-16}$ (tested at $h = 1/11$, $1/41$ and
$1/161$; the *nodal values* of the Galerkin solution also equal $\sin(\pi x_i)$ to
$1.7\times10^{-13}$ at the coarsest grid and $6.7\times10^{-16}$ at the finest).

**This is not a coincidence, and the explanation is worth having.** In one dimension
with linear elements:

1. the derivative of the *interpolant* of any function $w$ is piecewise constant, and
   on each element its value is the secant slope
   $\bigl(w(x_{i+1})-w(x_i)\bigr)/h = \frac{1}{h}\int_{x_i}^{x_{i+1}}w'\,dx$, by the
   mean value property for integrals. So

   $$(I_hw)' = \Pi_h\,w' ,$$

   where $\Pi_h$ is the $L^2$ **projection onto piecewise constants**;

2. the Galerkin equations say $\int u_h'\varphi_i'\,dx = \int u'\varphi_i'\,dx$ for
   every basis function $i$. The derivatives $\varphi_i'$ span the space of
   piecewise-constant functions, so this is exactly the statement that

   $$u_h' = \Pi_h\,u' ,$$

   the $L^2$ projection of the exact derivative onto piecewise constants;

3. comparing (1) and (2): $u_h' = (I_hu)'$, hence $u_h = I_hu + \text{const}$, and the
   constants are fixed by the same boundary conditions.

So **in one dimension with linear elements the Galerkin solution *is* the interpolant
of the exact solution**, and the finite-element error is exactly the interpolation
error. Two consequences:

- the "best approximation in the energy norm" property (5) of the lesson is
  realised *exactly* by the interpolant here, which is why the two errors coincide;
- the $L^2$ order 2 and energy order 1 measured in the lesson's §4.2 are therefore
  *interpolation* orders, and this problem cannot distinguish the two properties.

**Why it does not generalise — and why that matters.** In two or three dimensions
with linear elements the argument fails at step 1: the gradient of the interpolant is
piecewise constant but is not the $L^2$ projection of the exact gradient (the
spaces of vector-valued piecewise constants per element have the wrong dimensions
relative to the nodal degrees of freedom). The Galerkin solution is then *strictly
better* than the interpolant in the energy norm — a measurable difference, and the
standard superconvergence and optimal-accuracy results depend on it. Likewise, in
one dimension with quadratic elements the identity fails. So the correct statement
of the result is narrow and precise:

> *For a one-dimensional second-order elliptic problem discretised with continuous
> piecewise-linear elements and a uniform mesh, the Galerkin solution equals the
> nodal interpolant of the exact solution.*

Anyone who verifies their first code against an interpolant and finds agreement to
machine precision should read that as confirmation of *this* fact rather than as
general evidence of correctness. A two-dimensional verification must use a
convergence study.

---

## ★★★9 — A discontinuous coefficient

**(a) The exact solution.** With $k = 1$ for $x<0.5$ and $k = 10$ for $x>0.5$, the
equation $-(ku')' = 1$ reduces to $u'' = -1/k$ on each half, so $u$ is quadratic on
each side. Imposing $u(0) = 0$, $u(1) = 0$, continuity of $u$ at $0.5$ and continuity
of the flux $ku'$ at $0.5$ gives the four constants; the resulting solution satisfies

$$u'(0.5^-) = -0.20455, \qquad u'(0.5^+) = -0.020455 ,$$

so the slope jumps by a factor of ten, while $u$ itself is continuous. Therefore:

- $u\in H^1(0,1)$: the weak derivative is square-integrable (it is bounded and
  piecewise continuous);
- $u\notin H^2(0,1)$: the second weak derivative contains a Dirac measure at
  $x = 0.5$ and is not in $L^2$.

This is the *generic* situation for a layered Earth: the potential, head or
temperature is continuous across an interface but its flux-weighted derivative is
not.

**(b) and (c) Measured convergence.** Section 5 of `code/weak_solutions.py` assembles
the problem with the element-wise local $k$ and reports:

```text
  mesh ALIGNED with the interface (n odd)
      n          h     L2 error  order     H1 error  order
     11     0.0833    4.505e-04           1.710e-02       
     21     0.0455    1.340e-04   1.75    9.325e-03   0.87
     41     0.0238    3.678e-05   1.87    4.884e-03   0.93
     81     0.0122    9.648e-06   1.93    2.502e-03   0.97
    161     0.0062    2.472e-06   1.96    1.266e-03   0.98

  mesh NOT aligned (n even)
      n          h     L2 error  order     H1 error  order
     10     0.0909    3.121e-03           3.960e-02       
     20     0.0476    1.635e-03   0.93    2.857e-02   0.47
     40     0.0244    8.376e-04   0.97    2.040e-02   0.49
     80     0.0123    4.239e-04   0.98    1.449e-02   0.49
    160     0.0062    2.123e-04   1.00    1.030e-02   0.49
```

| Mesh | $L^2$ order | Energy order | Condition |
|---|---|---|---|
| Interface on a node | 2 | 1 | optimal, the kink is in the trial space |
| Interface inside an element | 1 | 0.5 | degraded by half in each norm, and errors an order of magnitude larger |

**The explanation.** With the interface on a node, the exact solution is *piecewise
quadratic* with the kink at a node, so on each element it is smooth; the standard
interpolation estimates apply element by element and give $O(h^2)$ in $L^2$ and
$O(h)$ in the energy norm. With the interface inside an element, the solution's
second derivative is a measure concentrated at an interior point of that element, and
the trial space cannot represent the slope jump at that point at all. The error is
then controlled by the *worst* element, whose local error is $O(h)$ in $L^2$ on that
element alone — and since a single element occupies a fraction $h$ of the domain, the
global $L^2$ error is $O(h)\cdot h^{1/2} = O(h^{3/2})$ in principle. The measured
$O(h)$ in $L^2$ and $O(h^{1/2})$ in the energy norm are consistent with the standard
estimate for a solution in $H^{1+s}$ with $s<\tfrac12$: the convergence rate is
$\min(2, 1+s)$ in $L^2$ and $\min(1, s)$ in the energy norm, and an interior kink
gives $s\approx0$ measured *at the interface*, degrading the rates to the observed
values. The empirically important point is the pairing: **the orders halve and the
error constants grow by an order of magnitude.**

**(d) The practical rule.** Put element boundaries where the material properties
jump. The weak formulation makes this easy — the element integrals simply use the
local $k$, with no special interface condition to code, because the continuity of the
flux is built into the weak form (it is the natural condition associated with the
interface). Consequences for practice:

- **mesh the geology, not the geometry**: a conductivity or density interface should
  coincide with an element boundary wherever the contrast is significant;
- **check the alignment**: comparing two meshes with the same $h$ but a different
  phase relative to the interface is a cheap test that reveals whether the model's
  accuracy is limited by the material geometry rather than by the mesh size (this is
  the exact experiment in the table above);
- **consider higher-order or enriched elements** where the interface cannot be
  aligned (a dipping or curved contact), or use a discontinuous-Galerkin
  formulation, which represents the jump explicitly;
- **remember that the condition number of the stiffness matrix also degrades** with a
  large contrast in $k$, so the linear solver may need scaling even when the mesh is
  aligned.

---

## ★★★10 — Methods section for a potential-field inversion

*(The task is to write a defensible methods section; the model answer is given as the
section itself, with a note after it identifying which lesson supplies each
requirement.)*

---

**Methods.** We invert surface gravity data for a subsurface density distribution
$\rho$ on a two- or three-dimensional grid. The forward problem is elliptic: outside
the sources the potential satisfies Laplace's equation and inside it satisfies
Poisson's equation, $\nabla^2V = -4\pi G\rho$, with the convention $V>0$ and
$\mathbf{g} = \nabla V$ throughout what follows.

*Weak formulation.* We solve for $V$ in the weak (variational) form obtained by
integrating $\nabla^2V = -4\pi G\rho$ against a test function and applying the
divergence theorem, which places only first derivatives of the trial function and
treats the free-air boundary condition as *natural* rather than essential. The
principal reason for the weak form is the density model itself: layer boundaries
involve discontinuous $\rho$, so the classical (strong) form is not satisfied in the
usual sense, whereas the weak form is. Dirichlet data (a fixed potential on the
survey boundary, where used) are imposed as *essential* conditions on the trial
space.

*Discretisation and demonstrated accuracy.* The domain is discretised into
hexahedra; the potential is represented by continuous piecewise-linear (or, where the
geometry demands it, piecewise-quadratic) elements, and the density by piecewise
constants on the same mesh. The discretised problem is the weak form restricted to
this finite-dimensional space (a Galerkin method), not a separate difference scheme.
We verify accuracy against exact solutions and report both norms: the $L^2$ error
converges at order 2 and the energy-norm error at order 1 for smooth solutions, and
we report the orders that are actually observed on the test problems rather than the
theoretical ones. For a layered test model we note the meshing rule that layer
boundaries must coincide with element boundaries: with an interface inside an element
the observed orders degrade to 1 in $L^2$ and 0.5 in the energy norm, with an order
of magnitude larger error constant.

*Stability.* The bilinear form is symmetric and coercive on the Dirichlet space
(Poincaré), so the Lax–Milgram theorem gives a unique weak solution with continuous
dependence on the data, $\lVert V\rVert \le c^{-1}\lVert\ell\rVert$. We verify
coercivity numerically by checking the smallest eigenvalue of the assembled stiffness
matrix against the discrete Poincaré value, and we check symmetry of the matrix as a
guard against assembly errors.

*Regularisation.* The inverse problem is ill posed: the forward map from density to
exterior field is compact, its singular values decay, and the two effects that matter
are (i) an exact null space — spherically symmetric perturbations of zero total mass
produce no exterior field, which we demonstrate on a synthetic model — and (ii) a
large effective null space at the survey's noise level. We therefore minimise

$$\lVert F\rho - g_{\text{obs}}\rVert^2 + \alpha\lVert L\rho\rVert^2 ,$$

with $L$ a depth-weighted gradient operator and $\alpha$ chosen by the discrepancy
principle from the estimated data noise; we report $\alpha$, the noise level, the
final misfit and the model norm, so that a reader can see the bias–variance trade-off.
The filter acts on the singular spectrum as $\sigma^2/(\sigma^2+\alpha)$, so
$\sqrt{\alpha}$ is the resolution threshold in singular-value units.

*Adjoint.* The gradient is computed by the adjoint-state method. We implement the
adjoint operator with the *same* boundary conditions as the forward problem and verify
the identity $\langle Fm,v\rangle = \langle m,F^{*}v\rangle$ numerically on the
assembled operators, plus the discrete integration-by-parts identity including its
boundary term. This test is reported because a mismatched adjoint produces a biased
model and a converged-looking inversion.

*Resolution.* Because the problem is ill posed, we report the resolution explicitly:
the singular spectrum of the (regularised) operator, the depth of investigation
implied by the recovered model norm, and a set of equivalent models that fit the data
to within the noise. We state which features of the preferred model are required by
the data and which are imposed by the regularisation and the positivity/depth
constraints. We do not describe the preferred model as "the" solution.

---

**Which lesson supplies which requirement.**

| Requirement | Where it comes from |
|---|---|
| the class of the equation and the data it needs | [01-09-01](../01-classification.md) |
| elliptic behaviour, harmonicity, and the data requirement | [01-09-04](../04-laplace-poisson.md) |
| the uniqueness theorem and its precise limits | [01-09-04](../04-laplace-poisson.md) §4–5 |
| the exact null space (spherically symmetric, zero mass) | [01-09-04](../04-laplace-poisson.md) §5.2 and [★★★9 of its exercises](../exercises/04-laplace-poisson-solutions.md) |
| the weak formulation and the two convergence orders | this lesson, §3–4 |
| the meshing rule at a discontinuity | [★★★9 of this set](#-9--a-discontinuous-coefficient) |
| coercivity, Lax–Milgram and the stability bound | this lesson, §5 |
| the adjoint with its boundary terms | this lesson, §6 |
| the singular spectrum and the filter | this lesson, §7.2–7.3 |
| why the backward/derivative problem is unstable | [01-09-07](../07-boundary-value-problems.md) §6 |
| regularisation as a *replacement* assumption | this lesson, §7.3 |

**What the section deliberately does not claim.** It does not claim that the
inversion recovers the true density, that the preferred model is unique, or that the
resolution is uniform. Each of those claims would contradict one of the theorems
derived in this module, and the honest methods section is the one that states the
trade-off rather than hiding it. This is not scepticism for its own sake: a reader who
knows the null space exists will assume it was handled, and a section that does not
mention it reads as either uninformed or evasive.
