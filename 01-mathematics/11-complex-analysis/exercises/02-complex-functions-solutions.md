# Solutions — 01-11-02 Holomorphic Functions and Cauchy-Riemann Equations

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*. Where a residual is quoted, it is the value the
> companion script in [`../code/`](../code/holomorphic_laplace_demo.py) actually
> prints, not an estimate.

---

## ★1 — Cauchy-Riemann for $z^{3}$

With $z = x+iy$, $z^{3} = (x^{3}-3xy^{2}) + i(3x^{2}y - y^{3})$, so

$$u = x^{3}-3xy^{2}, \qquad v = 3x^{2}y-y^{3}.$$

Derivatives:

$$u_{x} = 3x^{2}-3y^{2}, \qquad u_{y} = -6xy, \qquad
v_{x} = 6xy, \qquad v_{y} = 3x^{2}-3y^{2}.$$

Hence $u_{x} = v_{y}$ ✓ and $u_{y} = -v_{x}$ ✓, and the equations hold for all
$(x,y)$: $z^{3}$ is holomorphic on $\mathbb{C}$.

The derivative, written both ways:

$$f'(z) = u_{x} + iv_{x} = 3(x^{2}-y^{2}) + 6ixy = 3z^{2},$$

using the first form; and $v_{y} - iu_{y} = 3(x^{2}-y^{2}) + 6ixy$, identical, as
the Cauchy-Riemann equations require.

**Point of method.** The Cauchy-Riemann equations are *verified*, not assumed: it
would be equally legitimate to differentiate $z^{3}$ as a polynomial and read off
the derivatives, which is the check that the two routes agree.

---

## ★2 — A harmonic cubic and its conjugate

**Harmonic.** $u_{x} = 3x^{2}-3y^{2}$, $u_{xx} = 6x$; $u_{y} = -6xy$,
$u_{yy} = -6x$. So $u_{xx}+u_{yy} = 6x - 6x = 0$ ✓ for all $(x,y)$.

**Conjugate.** Impose $v_{y} = u_{x} = 3x^{2}-3y^{2}$, so
$v = 3x^{2}y - y^{3} + g(x)$. Then $v_{x} = 6xy + g'(x)$, which must equal
$-u_{y} = 6xy$; hence $g'(x) = 0$ and $g$ is constant. With $v(0,0)=0$,

$$v = 3x^{2}y - y^{3}.$$

**Identification.** $u+iv = (x^{3}-3xy^{2}) + i(3x^{2}y-y^{3}) = z^{3}$, which is
exactly ★1. The conjugate is unique up to an additive constant, and the constant
is fixed by one datum; the *pattern* of $u$ and $v$ is not affected.

**At $(2,1)$:** $u = 8-6 = 2$ and $v = 12-1 = 11$. Check:
$z^{3} = (2+i)^{3} = 2 + 11i$ ✓.

---

## ★3 — Holomorphy of four candidates

**(a) $f = \bar z = x - iy$.** Here $u = x$, $v = -y$, so $u_{x} = 1$ and
$v_{y} = -1$: the first Cauchy-Riemann equation fails everywhere. Not holomorphic
anywhere; it is an orientation-reversing reflection, and any holomorphic map is
orientation-preserving.

**(b) $f = \operatorname{Re}z = x$.** $u_{x} = 1$, $v_{y} = 0$: fails everywhere.
Note this function is smooth and real-valued; smoothness is irrelevant.

**(c) $f = 1/z = \bar z/|z|^{2}$.** Holomorphic on $\mathbb{C}\setminus\{0\}$,
the largest open set on which it is defined. That is the *punctured plane*: it is
open, and $f$ is holomorphic at every point of it.

**(d) $f = |z|^{2} = x^{2}+y^{2}$.** $u_{x} = 2x$, $v = 0$ so $v_{y} = 0$: the
equations hold only at $x = 0$; and $u_{y} = 2y$, $v_{x} = 0$, so only at $y = 0$.
Both hold only at the origin, and a single point is not an open set. There is **no
open set** on which this is holomorphic — complex differentiability at an isolated
point implies nothing about holomorphy (which requires an open neighbourhood).

---

## ★4 — The exponential

$f(z) = e^{z} = e^{x}(\cos y + i\sin y)$, so $u = e^{x}\cos y$ and
$v = e^{x}\sin y$. Then

$$u_{x} = e^{x}\cos y, \quad u_{y} = -e^{x}\sin y, \quad
v_{x} = e^{x}\sin y, \quad v_{y} = e^{x}\cos y,$$

so $u_{x} = v_{y}$ ✓ and $u_{y} = -v_{x}$ ✓. The derivative is

$$f'(z) = u_{x} + iv_{x} = e^{x}\cos y + ie^{x}\sin y = e^{z} = f(z),$$

which is the expected property. Both parts are harmonic, consistent with the
general theorem:

$$u_{xx} = e^{x}\cos y, \quad u_{yy} = -e^{x}\cos y, \quad u_{xx}+u_{yy} = 0 .$$

---

## ★★5 — The line mass

**(a)** $z = re^{i\theta}$, so $\log z = \ln r + i\theta$ and

$$\phi = m\ln r, \qquad \psi = m\theta .$$

**(b)** $\phi_{r} = m/r$, $\phi_{rr} = -m/r^{2}$, $\phi_{\theta\theta} = 0$, so

$$\phi_{rr} + \frac{\phi_{r}}{r} + \frac{\phi_{\theta\theta}}{r^{2}}
= -\frac{m}{r^{2}} + \frac{m}{r^{2}} + 0 = 0 .$$

The polar Laplacian vanishes for every $r>0$: the source is the only failure, at
$r = 0$.

**(c)** The potential of a line mass is the integral of $1/r$ over the line, and
$\int \mathrm{d}r/r = \ln r$: in two dimensions a point source's potential is
logarithmic. In three dimensions the corresponding integral is
$\int \mathrm{d}r/r^{2} = -1/r$, which is a *different functional form*, not a
different approximation.

The implication for interpretation is severe and practical: a logarithmic
potential is unbounded both at $r\to0$ and as $r\to\infty$, so a 2-D gravity
anomaly never falls off completely, and a profile interpreted with 2-D formulae
is sensitive to the assumed regional field over the whole length of the profile.
That is why 2-D modelling is always accompanied by a statement about the regional
trend.

**(d)** The two numbers establish that the residual **quarters when $h$ halves**:

$$\frac{2.7\times10^{-6}}{6.7\times10^{-7}} \approx 4 .$$

Since the five-point Laplacian has an $O(h^{2})$ truncation error and the exact
Laplacian is zero, this is exactly the signature of a correctly evaluated
harmonic function. A *single* residual proves nothing; the ratio is the evidence.
If both values were $4.0$, the function would not be harmonic, and the constant
value would be the exact Laplacian — exactly the counterexample
$\phi = x^{2}+y^{2}$ of the lesson.

---

## ★★6 — The 2-D dipole

**(a)** $w = \mu/z = \mu e^{-i\theta}/r$, so

$$\phi = \frac{\mu\cos\theta}{r} = \frac{\mu x}{x^{2}+y^{2}}, \qquad
\psi = -\frac{\mu\sin\theta}{r} = -\frac{\mu y}{x^{2}+y^{2}} .$$

**(b)** The field is $\mathbf{F} = -\nabla\phi$ with

$$F_{x} = -\phi_{x} = \mu\frac{x^{2}-y^{2}}{(x^{2}+y^{2})^{2}}, \qquad
F_{y} = -\phi_{y} = \frac{2\mu xy}{(x^{2}+y^{2})^{2}} .$$

The pattern is a **doublet**: the anomaly is antisymmetric about the vertical
axis through the source. Along the axis above the pole
($x=0$, $y>0$): $F_{x} = -\mu y^{2}/y^{4} = -\mu/y^{2}$ and $F_{y} = 0$, so the
response is along the axis and maximal there; along the horizontal line $y=0$ it
is $+\mu/x^{2}$ in the opposite sense. The magnitude falls off as $1/r^{2}$ — one
power faster than the line source. Both statements follow from
$\phi \propto \cos\theta/r$, i.e. from the single factor $e^{-i\theta}$ that the
pole of order one contributes.

**(c)** Two distinct reasons:

1. **Dimensionality.** $w = \mu/z$ is the field of a *two-dimensional* dipole
   (two oppositely signed line sources in the plane of the cross-section), whose
   potential decays as $1/r$. A buried sphere is a three-dimensional body whose
   potential decays as $1/r^{2}$ and whose horizontal derivative (the field
   measured) is a different function of position.
2. **The observable.** A gravity or magnetic survey measures the *field*, related
   to the potential by a derivative. Using a closed form for the potential
   directly as though it were the anomaly introduces both a dimensional error and
   a wrong power law — and the error is invisible once an arbitrary scale factor is
   allowed, which is exactly the trap.

The correct 3-D analogue is $w_{\text{3D}} \sim \partial_{z}(1/r)$, and its
horizontal derivative is the anomaly of the lesson's
[01-06-08 Potential theory](../../06-multivariable-calculus/08-potential-theory.md).

---

## ★★7 — Conjugate of $e^{x}\cos y$

**(a)** $u_{xx} = e^{x}\cos y$ and $u_{yy} = -e^{x}\cos y$, so
$u_{xx}+u_{yy} = 0$ ✓ for all $(x,y)$.

**(b)** $v_{y} = u_{x} = e^{x}\cos y$ gives $v = e^{x}\sin y + g(x)$; then
$v_{x} = e^{x}\sin y + g'(x)$ must equal $-u_{y} = e^{x}\sin y$, so $g(x) =
\text{const}$ and, with $v(0,0)=0$,

$$v = e^{x}\sin y .$$

**(c)** $v(0.5,1.0) = e^{0.5}\sin 1.0 = 1.648721\times0.841471 = 1.387351$ to
seven figures, matching the value obtained from $u+iv = e^{z}$ at
$z = 0.5+i$. The conjugate of $e^{x}\cos y$ is $e^{x}\sin y$, which is the
statement $e^{x+iy} = e^{z}$.

---

## ★★8 — The map $w = z^{2}$

**(a)** Write $z = re^{i\theta}$ with $\theta \in [0,\pi/4]$; then
$w = r^{2}e^{2i\theta}$ with $2\theta \in [0,\pi/2]$. The wedge of opening
$\pi/4$ maps onto the **first-quadrant wedge of opening $\pi/2$**, with angles
doubled and radii squared.

**(b)** $w' = 2z$, so the map is conformal wherever $z \neq 0$: at the origin the
derivative vanishes and angles are doubled rather than preserved (which is where
the factor 2 in the wedge angles comes from). At a critical point of a map,
angles are multiplied by the order of the zero of $w'$.

**(c)** A re-entrant corner of interior angle $3\pi/2$ in the physical region is
the image of a half plane under a map whose critical point sits at the corner,
with the local behaviour $w \sim \text{const}\cdot(z-z_{c})^{2/3}$ or similar.
Inverting, the solution near the corner varies as
$(z-z_{c})^{\lambda}$ with a non-integer $\lambda$, so derivatives diverge. That
is a *property of the solution*, not of the numerical method, and it is why
uniform meshes converge slowly at re-entrant corners and why grading or a
singular element is used there
([19-numerical-modeling-hpc](../../../19-numerical-modeling-hpc/README.md)).

---

## ★★★9 — The half-plane Dirichlet problem

**(a)** With $z = x+iy$,

$$1 - iz = 1 - i(x+iy) = (1+y) - ix,$$

so

$$g(z) = \frac{1}{(1+y)-ix} = \frac{(1+y)+ix}{(1+y)^{2}+x^{2}},$$

whose real part is $(1+y)/[(1+y)^{2}+x^{2}]$, as required. On the real axis
($y=0$) this is $1/(1+x^{2}) = f(x)$ ✓.

**(b)** The singularity is at $1-iz = 0$, i.e. $z = 1/i = -i$: the **lower** half
plane. Since the closed form has no singularity in the upper half plane, it is
holomorphic there and its real part is harmonic there — which is the hypothesis
of the Dirichlet problem, whose domain *is* the upper half plane. Had the pole
been at $+i$, the same real part would be harmonic nowhere in the domain, and the
extension would have to be written with the conjugate kernel instead.

**(c)** Write $\phi = (1+y)/D$ with $D = (1+y)^{2}+x^{2}$. Then, with
$s = 1+y$, $D = s^{2}+x^{2}$:

$$\phi_{x} = \frac{-s(2x)}{D^{2}}, \qquad
\phi_{y} = \frac{D - s(2s)}{D^{2}} = \frac{x^{2}-s^{2}}{D^{2}},$$

$$\phi_{xx} = \frac{2s(3x^{2}-s^{2})}{D^{3}}, \qquad
\phi_{yy} = \frac{2s(s^{2}-3x^{2})}{D^{3}} .$$

Adding, $\phi_{xx}+\phi_{yy} = 0$ for $D \neq 0$, i.e. everywhere except at
$(x,y) = (0,-1)$. The finite-difference check in the companion script gives
$-5.50\times10^{-5}$, $-1.37\times10^{-5}$, $-3.44\times10^{-6}$ at
$h = 10^{-2}, 5\times10^{-3}, 2.5\times10^{-3}$ — a factor of about four per
halving, the $O(h^{2})$ signature.

**(d)** For data on the lower half plane the domain is $\operatorname{Im}z < 0$,
so the *lower* half plane must be free of singularities and the conjugate of
$g$ must be used: with the same $f$, take $\tilde g(z) = 1/(1+iz)$, whose
singularity is at $z = i$ (upper half plane) and whose real part on the real axis
is again $1/(1+x^{2})$. The extension is
$\operatorname{Re}\tilde g = (1-y)/[(1-y)^{2}+x^{2}]$, the mirror image of the
upper solution in $y$. The rule is: **choose the branch of the analytic function
whose singularity is outside the domain**, and the answer is the reflection of the
upper solution.

---

## ★★★10 — Designing a holomorphy test

**(a)** Compute both Cauchy-Riemann residuals with **central** differences:

$$r_{1} = u_{x} - v_{y}, \qquad r_{2} = u_{y} + v_{x},$$

at several points, and at a *sequence* of step sizes (say
$h = 10^{-2}, 5\times10^{-3}, 2.5\times10^{-3}, 1.25\times10^{-3}$). Central
differences have truncation error $h^{2}|u_{xxx}|/6$, so the residual should
shrink by about 4 per halving if the exact residual is zero.

**(b)** Convergence: $r \propto h^{2}$ for a holomorphic function, until round-off
takes over. The round-off floor is set by the cancellation in the difference
quotient: $u(x+h)-u(x-h)$ is computed to absolute accuracy $\sim\varepsilon|u|$
with $\varepsilon \approx 2\times10^{-16}$, and divided by $2h$, so the noise
floor is about $\varepsilon|u|/(2h)$. For $|u|\sim1$ and $h = 10^{-4}$ this is
$10^{-12}$ — which is exactly the measured $1.1\times10^{-12}$. **The optimal
step is therefore around $h \sim \varepsilon^{1/3}\sim6\times10^{-6}$**, balancing
$h^{2}$ truncation against $1/h$ noise; smaller steps make the test *worse*.

**(c)** Both values are at the noise floor of the stencil, not measures of
non-holomorphy. For the polynomial the difference quotient is exact (a cubic's
central difference of a quadratic derivative is exact), so only round-off
remains: $1.1\times10^{-12}$. For the transcendental function the truncation term
$h^{2}|u_{xxx}|/6$ is itself non-zero, giving $\sim10^{-8}$ at $h = 10^{-4}$ — the
same order as the measured $2.3\times10^{-9}$. Neither is evidence against
holomorphy; both are evidence about the *stencil*. The failure test is a residual
that **stops shrinking** with $h$, not a residual that is merely non-zero.

**(d)** $g(z) = \sqrt z$ with the principal branch analytic on
$\mathbb{C}\setminus(-\infty,0]$. At $z = 0.01$ (on the positive real axis) the
function is holomorphic, and the test passes. At $z = -0.01$ the point lies on
the **branch cut**, where the principal square root is discontinuous; the
function is not even continuous there, let alone complex differentiable, so the
residual is $O(1)$ and does not shrink. The test is behaving correctly: it is
detecting a failure of the *hypothesis* (a neighbourhood on which the function is
defined and differentiable), not a failure of the numerical method. Practically,
this is the reason a test point near a branch cut, a pole or a discontinuity must
be chosen deliberately.

---

## Self-assessment: have you actually learned this?

You have if you can, without notes:

- derive the Cauchy-Riemann equations from two directions of approach and state
  the continuity hypothesis needed for sufficiency;
- derive $u_{xx}+u_{yy} = 0$ from them and say which symmetry of mixed partials is
  used;
- test a candidate function and interpret the residual, including its convergence
  in $h$ and its round-off floor;
- construct a harmonic conjugate by integration and name a domain where the
  construction fails;
- write the complex potential of a line mass and of a 2-D dipole and say which
  part is potential and which is stream function;
- state why the half-plane Poisson integral is the real part of an analytic
  function, and where that function's singularity must lie.
