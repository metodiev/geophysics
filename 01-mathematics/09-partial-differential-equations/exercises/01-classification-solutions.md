# Solutions — 01-09-01 Classification of PDEs: Elliptic, Parabolic, Hyperbolic

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. They are
> not the only correct route. Where a numeric answer is given, it was computed
> rather than estimated by hand. Several problems have more than one defensible
> answer; where that is true, it is stated explicitly.
>
> **Convention used throughout.** The principal part of a second-order linear
> equation in two independent variables is written
> $A\,u_{xx} + 2B\,u_{xy} + C\,u_{yy}$, and the class is read from
> $\Delta = B^2 - AC$: elliptic if $\Delta<0$, parabolic if $\Delta=0$,
> hyperbolic if $\Delta>0$.

---

## ★1 — Classification of four equations

The factor of two is where most errors happen, so each row states how $(A,B,C)$
was read from the written equation.

| | Equation | $A$ | $B$ | $C$ | $\Delta = B^2-AC$ | Class |
|---|---|---|---|---|---|---|
| (a) | $u_{xx} + 4u_{xy} + 4u_{yy} = 0$ | 1 | 2 | 4 | $4-4 = 0$ | **parabolic** |
| (b) | $u_{xx} + u_{xy} + u_{yy} = 0$ | 1 | $\tfrac12$ | 1 | $\tfrac14-1 = -0.75$ | **elliptic** |
| (c) | $u_{xx} - 4u_{yy} = 0$ | 1 | 0 | $-4$ | $0+4 = +4$ | **hyperbolic** |
| (d) | $3u_{xx} + 2u_{xy} + 3u_{yy} = 0$ | 3 | 1 | 3 | $1-9 = -8$ | **elliptic** |

**Reading the coefficients.** Because the mixed term in the standard form carries
a factor 2, a written $4u_{xy}$ means $2B = 4$, hence $B = 2$; a written
$u_{xy}$ means $B = \tfrac12$. Getting this wrong in (a) gives
$\Delta = 16 - 4 = 12 > 0$, i.e. hyperbolic — the opposite answer. In (d) the
same mistake gives $\Delta = 4 - 9 = -5$, still elliptic, so that case is
forgiving; convergence of the two conventions is not something to rely on.

**Structure worth noticing in (a).** The operator factorises,
$u_{xx} + 4u_{xy} + 4u_{yy} = (\partial_x + 2\partial_y)^2 u$, so the equation
reads $(\partial_x + 2\partial_y)^2u = 0$. It degenerates along the single family
of lines $2y - x = \text{const}$, which is exactly the parabolic signature: one
real characteristic family. Compare ★4, where the same degeneracy appears with a
different coefficient pattern.

**A note on (b).** This is the equation
$u_{xx} + u_{xy} + u_{yy} = 0$, which looks symmetric but is elliptic, because the
mixed coefficient has a factor $\tfrac12$: the quadratic form
$\xi^2 + \xi\eta + \eta^2$ is positive definite (its matrix has eigenvalues
$\tfrac12$ and $\tfrac32$).

---

## ★2 — The data each problem requires

| Problem | Class | Data required | Why |
|---|---|---|---|
| (a) $u_t = \kappa u_{xx}$ | parabolic | $u(x,0)$ for $0<x<1$, plus one condition at $x=0$ and one at $x=1$ for all $t>0$ | one time derivative, two space derivatives |
| (b) $\nabla^2V = 0$ | elliptic | one condition at **every** point of $\partial\Omega$ | no time variable, no characteristics |
| (c) $u_{tt} = c^2u_{xx}$ | hyperbolic | $u(x,0)$ and $u_t(x,0)$, plus one condition at each end | two time derivatives, two characteristic families |

**The justification is the same in each case: count the characteristics that enter
the domain.**

- In (a) the characteristics of the diffusion equation are the lines of constant
  $x$ (degenerate, all parallel to the $x$-axis). At $t=0$ the state must be given;
  at each spatial boundary the single entering characteristic requires one
  condition. Because the parabolic equation is not time-reversible, these
  conditions are needed only for $t>0$; nothing may be imposed at $t$ greater than
  the time of interest.
- In (b) there are no real characteristics at all, so no boundary point is
  privileged: every one must carry data, and exactly one condition per point. Two
  conditions at a point would over-determine the problem; an unconstrained arc of
  the boundary leaves the solution free to vary.
- In (c) there are two characteristic families, so two pieces of Cauchy data are
  required — the displacement and the velocity. On each boundary, one condition is
  required **per incoming characteristic**; at a fixed end both characteristics
  enter and the single condition $u=0$ suffices because the two families are
  related by the boundary condition, as the reflected-wave construction of
  [01-09-03](../03-wave-equation.md) shows.

**What the counts mean in practice.** The three rows are three different
experimental designs. A gravity survey (b) provides boundary data on a surface,
not a closed boundary, and that shortfall is the practical origin of the
non-uniqueness discussed in [01-09-04](../04-laplace-poisson.md). A seismic
survey (c) provides the two Cauchy data implicitly, through the source, and the
arrival times of the two characteristic families are what is actually measured.

---

## ★3 — Convection–diffusion in three regimes

**Read the coefficients in the form $A u_{xx} + 2Bu_{xt} + Cu_{tt}$ with
$(x,t)$ as the independent pair.** Writing the equation as
$-v\,u_x - \kappa\,u_{xx} + u_t = 0$ and collecting principal terms,
$A = -\kappa$, $B = 0$, $C = 0$.

| Case | Equation | $(A,B,C)$ | $\Delta$ | Class | Geophysical process |
|---|---|---|---|---|---|
| (a) | $u_t + vu_x = 0$ | $(0,0,0)$ | — | not classified by $\Delta$; a first-order transport equation with one characteristic family | river or groundwater advection with no dispersion |
| (b) | $u_t = \kappa u_{xx}$ | $(-\kappa,0,0)$ | $0$ | parabolic | heat conduction, pore-pressure diffusion |
| (c) | $u_t + vu_x = \kappa u_{xx}$ | $(-\kappa,0,0)$ | $0$ | parabolic | solute transport in a river or aquifer with dispersion |

**Why (a) is not "parabolic".** The discriminant test applies to a second-order
principal part. With every principal coefficient zero there is nothing to test:
the equation is first order and is solved by characteristics, as in
[01-09-06](../06-characteristics.md). Calling it parabolic is a common
looseness; it is acceptable shorthand in a numerical context (an upwind
discretisation of (a) and (c) share a stability condition), but it is not the
classification of this lesson.

**Why (c) is parabolic and not hyperbolic.** The second-order term is
$-\kappa u_{xx}$ with no $u_{tt}$, so $\Delta = 0$ regardless of how large $v$ is.
This is a physically important point that surprises people: **advection does not
make diffusion hyperbolic.** The equation has one characteristic family
(the transport direction) but the second-order term keeps it diffusive, so the
solution still smooths; what advection changes is the *shape* of the smoothing.
The dimensionless number that decides which effect dominates locally is the cell
Péclet number $v\Delta x/\kappa$; a central difference becomes oscillatory above
about 2, which is why upwind or flux-limiter schemes are used in advection-dominated
problems.

**A caution.** For very small $\kappa$ the mathematical class is parabolic but the
practical behaviour is transport-like over ordinary distances: the diffusion
length $\sqrt{4\kappa t}$ is tiny compared with the advected distance $vt$. Class
is a statement about the equation; regime is a statement about the parameters, and
both matter.

---

## ★4 — Degenerate second-order operator

**Change of variables.** With $\xi = y - x$ and $\eta = y$,

$$\frac{\partial}{\partial x} = -\frac{\partial}{\partial\xi}, \qquad
\frac{\partial}{\partial y} = \frac{\partial}{\partial\xi} +
\frac{\partial}{\partial\eta}.$$

Therefore

$$\frac{\partial}{\partial x} + \frac{\partial}{\partial y}
= \frac{\partial}{\partial\eta}, \qquad\text{so}\qquad
u_{xx} + 2u_{xy} + u_{yy}
= \left(\frac{\partial}{\partial x} + \frac{\partial}{\partial y}\right)^2 u
= u_{\eta\eta}.$$

The equation becomes $u_{\eta\eta} = 0$, whose general solution is

$$\boxed{\ u(\xi,\eta) = A(\xi) + \eta\,B(\xi) = A(y-x) + y\,B(y-x)\ }$$

with $A$ and $B$ arbitrary twice-differentiable functions.

**Verification by substitution.** Differentiate the general solution:
$u_x = -A' - yB'$, $u_y = A' + B + yB'$, and
$u_{xx} = A'' + yB''$, $u_{xy} = -A'' - B' - yB''$, $u_{yy} = 2B' + yB''$. Then

$$u_{xx} + 2u_{xy} + u_{yy}
= (A'' + yB'') - 2(A'' + B' + yB'') + (2B' + yB'') = 0 ,$$

term by term. The cancellation is exact, as it must be: the operator is a perfect
square.

**Characteristics.** Setting the coefficient of $u_{\xi\xi}$ to zero is the
condition for a curve to be characteristic; here
$\Delta = B^2 - AC = 1 - 1 = 0$, so there is one real family,
$y - x = \text{const}$, which is precisely the $\xi$ family used above. The
solution varies along the other coordinate, $\eta = y$.

**Physical reading.** An equation of this type arises wherever a quantity is
advected along one direction with a "double" characteristic — the simplest case of
a degenerate transport. The parabolic $\eta$-behaviour means the solution is not
oscillatory in $\eta$ but grows or decays linearly there, which is the signature of
a marginally stable mode rather than a propagating one.

---

## ★★5 — Deriving the characteristic equation

**Setup.** Let a curve $\Gamma$ be given parametrically by $(x(s), y(s))$, and
suppose $u$ and its first derivatives are prescribed on $\Gamma$. Ask whether the
second derivatives are determined by that data.

**Step 1 — provide the missing equations.** Along $\Gamma$, the total derivative of
$u_x$ and $u_y$ with respect to $s$ is known from the data:

$$\frac{d}{ds}u_x = u_{xx}\frac{dx}{ds} + u_{xy}\frac{dy}{ds}, \qquad
\frac{d}{ds}u_y = u_{xy}\frac{dx}{ds} + u_{yy}\frac{dy}{ds}.$$

Together with the PDE itself,

$$A\,u_{xx} + 2B\,u_{xy} + C\,u_{yy} = F ,$$

these are three linear equations for the three second derivatives
$(u_{xx}, u_{xy}, u_{yy})$.

**Step 2 — when does the system fail to determine them?** Exactly when its
determinant vanishes. Writing $p = dx/ds$ and $q = dy/ds$, the determinant is

$$\begin{vmatrix} A & 2B & C \\ p & q & 0 \\ 0 & p & q \end{vmatrix}
= A q^2 - 2B\,pq + C p^2 .$$

Setting this to zero and dividing by $p^2$ (assuming $p \ne 0$, i.e. the curve is
not vertical) gives

$$A\left(\frac{q}{p}\right)^2 - 2B\left(\frac{q}{p}\right) + C = 0
\qquad\Longrightarrow\qquad
A\left(\frac{dy}{dx}\right)^2 - 2B\frac{dy}{dx} + C = 0 ,$$

which is the required condition.

**Step 3 — solve it.** This is a quadratic in $dy/dx$ with discriminant
$4(B^2 - AC) = 4\Delta$, so

$$\frac{dy}{dx} = \frac{2B \pm 2\sqrt{\Delta}}{2A}
= \frac{B \pm \sqrt{\Delta}}{A} .$$

**Interpretation.** Where $\Delta > 0$ there are two real curve families on which
the second derivatives fail to be determined by Cauchy data: these are the
characteristics, and data propagate along them. Where $\Delta = 0$ there is one
such family. Where $\Delta < 0$ there are none, so no curve is special and the
second derivatives are always determined — which is why an elliptic problem has no
propagation direction and needs data on the whole boundary instead.

**Consistency checks.** For $u_{tt} = c^2u_{xx}$ in variables $(x,t)$,
$A = -c^2$, $B = 0$, $C = 1$, so $dt/dx = \pm\sqrt{c^2}/(-c^2)$ — better to use
the version in $dt/dx$ solved directly: $A(dt/dx)^2 - 2B(dt/dx) + C = 0$ gives
$-c^2(dt/dx)^2 + 1 = 0$, so $dt/dx = \pm 1/c$, i.e. $x \mp ct = \text{const}$ ✓.
For Laplace's equation, $A = C = 1$, $B = 0$ gives
$(dy/dx)^2 + 1 = 0$, whose roots are $\pm i$: the characteristics are complex, and
the combination $x + iy$ is the natural variable. That complex structure is the
reason elliptic problems connect to analytic function theory, and it is where the
conformal-mapping methods of classical potential theory come from.

---

## ★★6 — Skin depth, and when GPR stops being diffusive

**Given.** $\mu_0 = 4\pi\times10^{-7}\ \mathrm{T\,m\,A^{-1}}$ (equivalently
$\mathrm{H\,m^{-1}}$), $\sigma = 0.01\ \mathrm{S\,m^{-1}}$, $f = 1$ Hz,
$\epsilon_r = 6$ so $\epsilon = 6\epsilon_0 = 5.3124\times10^{-11}\ \mathrm{F\,m^{-1}}$.

**(a)** Using $\delta = \sqrt{2/(\omega\mu\sigma)}$ with
$\omega = 2\pi f = 6.2832\ \mathrm{rad\,s^{-1}}$:

$$\omega\mu_0\sigma = 6.2832 \times 1.2566\times10^{-6} \times 0.01
= 7.8957\times10^{-8}\ \mathrm{m^{-2}} ,$$

$$\delta = \sqrt{\frac{2}{7.8957\times10^{-8}}}
= \sqrt{2.5330\times10^{7}} = 5032.9\ \mathrm{m} \approx 5.03\ \mathrm{km} .$$

Equivalently, $\delta = \sqrt{1/(\pi f\mu_0\sigma)} = 5033$ m, which is what the
module's diffusion demonstration reports for this pair of parameters.

**(b)** At $f = 10^8$ Hz, $\omega = 6.2832\times10^8$ and

$$\omega\epsilon = 6.2832\times10^8 \times 5.3124\times10^{-11}
= 3.338\times10^{-2}\ \mathrm{S\,m^{-1}} ,$$

so the loss tangent is

$$\frac{\sigma}{\omega\epsilon} = \frac{0.01}{3.338\times10^{-2}} = 0.30 .$$

Since $\sigma < \omega\epsilon$, the **wave equation** (with a moderate loss) is
the better description, not the diffusion equation. Supporting numbers: the
propagation speed is $c/\sqrt{\epsilon_r} = 3\times10^{8}/2.449
= 1.22\times10^{8}\ \mathrm{m\,s^{-1}}$, so a 100 MHz pulse has a wavelength of
about 1.2 m — the scale at which a GPR survey is designed.

The wave-field skin depth (the $1/e$ amplitude distance) at this loss tangent is
approximately $\lambda/(2\pi)\cdot(1/\tan\delta)$; the exact expression requires the
full complex wavenumber, and quoting it is beyond what this calculation supports.
What the calculation does establish is the *regime*: propagation, not diffusion.

**(c) The criterion.** The full Maxwell equations give

$$\nabla^2\mathbf{E} = \mu\sigma\frac{\partial\mathbf{E}}{\partial t}
+ \mu\epsilon\frac{\partial^2\mathbf{E}}{\partial t^2} ,$$

and the ratio of the conduction term to the displacement term is
$\sigma/(\omega\epsilon)$. The cross-over is at $\sigma = \omega\epsilon$, i.e.
loss tangent $= 1$. For $\sigma \ll \omega\epsilon$ the field propagates (radar
regime); for $\sigma \gg \omega\epsilon$ it diffuses (magnetotelluric regime).
At $\sigma/(\omega\epsilon)$ of order 1 — as here, 0.30 — neither idealisation is
fully accurate at the level of a careful amplitude study, and the general
governing equation must be used.

**The class is a property of the experiment, not only of the rock.** The same rock
with $\sigma = 0.01\ \mathrm{S\,m^{-1}}$ is a wave medium at 100 MHz and a
diffusive medium at 1 Hz. Any sentence of the form "in this rock electromagnetic
energy diffuses" is incomplete without the frequency.

---

## ★★7 — A mixed-type equation

With $A = 1$, $B = x$, $C = 1-y$, the discriminant is

$$\Delta = B^2 - AC = x^2 - (1 - y) = x^2 + y - 1 .$$

| Region | Condition | Class | Characteristics |
|---|---|---|---|
| below the parabola | $y < 1 - x^2$ | elliptic ($\Delta<0$) | complex |
| on the parabola | $y = 1 - x^2$ | parabolic ($\Delta=0$) | one real family |
| above the parabola | $y > 1 - x^2$ | hyperbolic ($\Delta>0$) | two real families |

The dividing curve is the downward parabola $y = 1 - x^2$, through $(0,1)$ and
$(\pm1,0)$. Its apex is at $(0,1)$; the hyperbolic region is unbounded above and
contains the whole half-plane $y>1$ (there $C<0$ forces $\Delta>0$ for any $x$).

**Characteristic slopes** in the hyperbolic region come from
$dy/dx = (B \pm\sqrt{\Delta})/A = x \pm\sqrt{x^2+y-1}$.

**Physical meaning of a mixed type.** In a steady transonic flow, or in a
stress problem near a crack tip, the local Mach number (or the local ratio of
stress intensity to a material threshold) selects the class point by point: elliptic
where the flow is subsonic, hyperbolic where it is supersonic, with a sonic line
in between. The practical consequences are severe and specific:

- the **type of boundary condition** required changes across the dividing curve, so
  a single well-posed formulation must be pieced together region by region;
- the **numerical method** must change too, since an elliptic solve and a
  hyperbolic march are different algorithms;
- solutions typically lose smoothness on the dividing curve, and in many problems
  physical discontinuities (shocks) appear exactly there.

In geophysics the standard instance is not a single mixed-type equation but a
*decomposition*: the same medium supports diffusive and wave behaviour in
different frequency bands, as in ★6. The two situations are related but not
identical, and it is worth keeping them apart: mixed type is one equation whose
class varies in space, whereas the electromagnetic example is one physical system
described by different equations in different regimes.

---

## ★★8 — Relaxation and the telegraph equation

**Principal part.** Write $u_t + \tau u_{tt} = \kappa u_{xx}$ in standard form
with the independent pair $(x,t)$:

$$-\kappa\,u_{xx} + 0\cdot u_{xt} + \tau\,u_{tt} = -u_t ,
\qquad\text{so}\qquad A = -\kappa,\quad B = 0,\quad C = \tau .$$

Then

$$\Delta = B^2 - AC = 0 - (-\kappa)(\tau) = \kappa\tau .$$

| $\tau$ | $\Delta$ | Class |
|---|---|---|
| $\tau = 0$ | $0$ | parabolic |
| $\tau > 0$ | $\kappa\tau > 0$ | hyperbolic |

**The change happens the moment $\tau$ becomes positive, however small.** This is
a genuine discontinuity of behaviour at $\tau = 0$, not a gradual crossover: for
any $\tau>0$ the equation has real characteristics, a finite signal speed, and a
requirement for two initial conditions instead of one. The diffusion equation is
the *singular limit* as $\tau \to 0$ (equivalently, as the relaxation is fast
compared with the times of interest).

**Physical process.** The hyperbolic case is the **telegraph equation** (equivalently
the viscoelastic or Maxwell–Cattaneo model of heat conduction). It arises when the
flux does not respond instantaneously to the gradient, but relaxes:

$$q + \tau\,q_t = -\kappa\,u_x .$$

Combined with conservation $u_t + q_x = 0$ this gives the equation above. Two
consequences: heat (or pore pressure, or any diffusive quantity) propagates at a
finite speed $\sqrt{\kappa/\tau}$ instead of instantaneously, and the solution is no
longer strictly monotone in time, so a temperature step can overshoot before
relaxing — a small, transiently oscillatory wavelike feature.

**Why $\tau = 0$ is special, and why the idealisation is still used.** The
physically correct equation is hyperbolic; the parabolic equation is the
approximation obtained by dropping one term in an asymptotic expansion. That
approximation is excellent whenever
$\sqrt{\kappa\tau} \gg$ the length scales of interest divided by the relevant
time — in rock, the relaxation time is on the order of $10^{-12}$ s, so the
finite-speed correction matters only at frequencies above roughly $10^{11}$ Hz.
**The diffusion equation of [01-09-02](../02-heat-equation.md) is thus an
approximation whose error is negligible in every ordinary geophysical setting, and
the honest statement of the approximation is that the propagation speed is very
large rather than that it is infinite.** Note also that $\tau$ as used here is a
relaxation time, not the diffusive timescale $L^2/\kappa$ of
[01-09-02](../02-heat-equation.md); the two symbols are both conventional and
must not be confused.

---

## ★★★9 — One disturbance, three behaviours

A valid design must isolate the *class* rather than the equation, so the
diagnostic has to be something that behaves differently in the three cases. Two
diagnostics do:

**Diagnostic 1: the radius of influence as a function of time.** Start with a
compact disturbance at an interior point, zero elsewhere, and measure the set of
points where $\lvert u\rvert$ exceeds a fixed fraction (say $10^{-3}$) of the
initial amplitude.

| Class | Expected radius $R(t)$ | Expected $R$ versus grid spacing $h$ |
|---|---|---|
| Hyperbolic | $R = ct$ exactly, independent of $h$ below the resolution limit | converges to $ct$ as $h\to0$; the front is sharp |
| Parabolic | $R \propto \sqrt{\kappa t}$, with $\lvert u\rvert \sim t^{-1/2}\mathrm{e}^{-R^2/4\kappa t}$ | converges slowly; the value at fixed $R$ grows without bound as $h\to0$ |
| Elliptic | no $t$ at all: the solution is a boundary-value problem and does not evolve | $R$ is the whole domain, independent of $h$ |

The parabolic row is the discriminator: for a fixed threshold the radius grows like
$\sqrt{t}$, and — crucially — the *leaked amplitude at a fixed point* is nonzero
for every $t>0$. The hyperbolic case gives exactly zero outside the cone.

**Diagnostic 2: the measured convergence order of a standard scheme.** A scheme of
known order $p$ must return order $p$ for the class it was designed for and fail
otherwise: an explicit scheme for the wave equation converges at order 2 up to its
CFL limit and diverges above it; the same stencil applied to Laplace's equation
converges to the solution of the wrong problem (a steady state), and its "error"
does not shrink with $h$ at all, because refining the grid does not add time steps.

**A concrete experiment, and its numbers.** The `code/pde_classification.py`
script of this module implements exactly this design for one dimension:

- **Hyperbolic.** A compact pulse at Courant number 1, 120 steps, $c = 1$:
  predicted support $[0.460000, 0.540000]$, numerical support
  $[0.461667, 0.538333]$ (one cell), maximum error against the exact translation
  $6.4\times10^{-15}$, and **maximum magnitude outside the cone
  $0.000\times10^{0}$**. The front is sharp and its position is $ct$ to within one
  cell.
- **Parabolic.** The same compact pulse under $u_t = \kappa u_{xx}$: the largest
  value outside the original support is $6.1\times10^{-6}$ after one step,
  $5.2\times10^{-3}$ after five, and $7.7\times10^{-2}$ after fifty. There is no
  cone; the disturbance is everywhere immediately and its size grows.
- **Elliptic.** A one-dimensional Poisson problem solved by iteration: the
  solution is smooth, the error falls at order 2 under refinement, but the
  iteration count grows like $N^2$ (measured $369$, $1241$, $4286$ for
  $N = 10,20,40$) — the diagnostic is that the solution depends on the *whole*
  boundary, so no local disturbance can be isolated.

**Falsification.** A classification is falsified if the measured diagnostic
contradicts the predicted scaling in a regime where the discretisation error is
demonstrably smaller than the effect: for example, if a compactly supported
initial condition produced a nonzero value outside its cone in a hyperbolic
problem at a level above the truncation error, the equation would not be
hyperbolic. Conversely, if a parabolic problem's leakage amplitude were *exactly*
zero for all time, the equation would not be parabolic. The experiment must report
the truncation error alongside the leakage, because a claim of "exactly zero" at a
level below the scheme's error is not a measurement.

**Limits of the method.** This diagnostic separates the three classes but not the
equations: an elliptic relaxation and a steady-state parabolic march look alike at
the level of a support measurement. The classification of a specific equation
still requires reading the coefficients (★1). And in more than one dimension the
cone is a genuine cone, so the measurement needs a two-dimensional probe.

---

## ★★★10 — Critique of a depth–magnetisation trade-off

**The class and the equation.** The anomaly is a magnetic field measured outside
the source. Outside all sources the potential (or the field, componentwise) obeys
Laplace's equation, $\nabla^2V = 0$; inside, Poisson's equation with a source
proportional to the magnetisation. The problem is therefore **elliptic**, and it
requires one boundary condition at every point of the boundary of the region under
study. A survey provides data on a surface — an open patch, not a closed surface —
and at finitely many points, with noise.

**Which properties of harmonic functions bear on the question.**

- *Analyticity.* The field above the source is real-analytic, so its values on any
  open patch determine the whole exterior field. Two models that agree on the
  surveyed patch therefore agree everywhere above it; the question "which is
  right?" cannot be answered from above the surface alone.
- *Maximum principle.* The exterior field has no interior extremum, which is a
  consistency requirement on any model and a diagnostic for processing artefacts —
  but it does not distinguish depth from magnetisation.
- *Uniqueness of the boundary-value problem.* If the field were known on a
  *closed* surface enclosing the body, the potential inside would be unique, and
  hence $\rho$ (or the magnetisation) inside would be unique by Poisson's
  equation. This is the theorem that makes the survey informative in principle.
- *The null space.* Because real data are on a surface patch and band-limited, the
  forward map has a large effective null space; models differing within it produce
  indistinguishable data. The module's numerical experiment exhibits an exact null
  vector — a spherically symmetric density perturbation with zero total mass —
  whose exterior effect is $1.2\times10^{-7}$ in relative terms, i.e. below the
  noise of any real survey, while the density changes by $500\
  \mathrm{kg\,m^{-3}}$ inside.

**Why the paper's claim is not defensible as stated.** A body at 4 km and a larger,
less magnetised body at 8 km are two points in the same equivalence class for
surface data: the deeper body's larger volume compensates its weaker
magnetisation, and the exterior field is close to identical over the resolvable
band. Since the data cannot separate them, the paper is entitled to say that both
models fit the data equally well — that is a *statement about the data*. It is not
entitled to conclude that one is "wrong", because "wrong" would require information
the data do not contain. If the paper's argument is that one model violates an
independent constraint (the magnetisation is unphysically large, the body does not
fit a known geological boundary, or the depth conflicts with a borehole), then that
constraint should be stated explicitly, and it is doing the work — not the anomaly.

**What would break the tie.**

| Additional data | Why it discriminates |
|---|---|
| Higher-resolution or lower-elevation (or borehole) field measurements | the deeper body's field decays more slowly with altitude; the ratio of fields at two heights is a depth indicator |
| A measured density/magnetisation on samples, or a susceptibility log | fixes the magnitude of the source property, leaving only geometry |
| Seismic or gravity data resolving the same interface | an independent geometry constraint |
| Depth extent from other methods (wells, seismic) | removes the ambiguity directly |
| A quantitative uncertainty statement with a noise level | converts "the anomaly requires" into a testable claim |

**What the paper should report to be defensible.** (i) The forward operator and
its discretisation, with the convergence order demonstrated. (ii) The regularisation
used and how its parameter was chosen; whether a positivity or depth-weighting
constraint was imposed. (iii) A resolution analysis or a set of equivalent models,
so the reader can see the null space rather than infer it. (iv) The noise level, and
a statement of which model features are resolved at that level. (v) Explicit
statement of which conclusion rests on the data and which on prior information.
Given (i)–(v), "both models fit, and this constraint favours the shallower one"
would be a defensible sentence; "the anomaly requires a body at 4 km" would not.
