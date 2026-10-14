# Solutions — 01-06-06 Gauss, Stokes and Green Theorems

> **Read this after attempting the exercises, not before.**

---

## ★1 — Divergence theorem for $\mathbf{F} = (x, 2y, 3z)$

**Volume side.** $\nabla\cdot\mathbf{F} = 1 + 2 + 3 = 6$, so

$$\iiint_{[0,1]^3}\nabla\cdot\mathbf{F}\,dV = 6 \times 1 = 6 .$$

**Surface side.** Six faces, each of area 1, outward normals $\pm\hat{x}$,
$\pm\hat{y}$, $\pm\hat{z}$:

| Face | normal | $\mathbf{F}\cdot\hat{n}$ | flux |
|---|---|---|---|
| $x=1$ | $+\hat{x}$ | $x = 1$ | 1 |
| $x=0$ | $-\hat{x}$ | $-x = 0$ | 0 |
| $y=1$ | $+\hat{y}$ | $2y = 2$ | 2 |
| $y=0$ | $-\hat{y}$ | $-2y = 0$ | 0 |
| $z=1$ | $+\hat{z}$ | $3z = 3$ | 3 |
| $z=0$ | $-\hat{z}$ | $-3z = 0$ | 0 |

Total flux $= 6$ ✓. **The two sides agree**, and each face's contribution is
individually meaningful: the three nonzero faces are exactly the three whose
coordinate is at its maximum.

---

## ★2 — Stokes' theorem on a triangle

**(a)** $\mathbf{F} = (z,x,y)$:

$$\nabla\times\mathbf{F} = \left(\frac{\partial y}{\partial y}
- \frac{\partial x}{\partial z},\
\frac{\partial z}{\partial z} - \frac{\partial y}{\partial x},\
\frac{\partial x}{\partial x} - \frac{\partial z}{\partial y}\right)
= (1,\ 1,\ 1).$$

**(b)** On the surface $z = 0$ the upward normal is $\hat{z}$, so
$(\nabla\times\mathbf{F})\cdot\hat{n} = 1$ and

$$\iint_S(\nabla\times\mathbf{F})\cdot d\mathbf{A} = \text{area of the triangle}
= \frac{1}{2}\cdot1\cdot1 = \frac{1}{2}.$$

**(c)** Boundary traversed counterclockwise as seen from $+z$: $(0,0,0)\to(1,0,0)
\to(0,1,0)\to(0,0,0)$. With $z = 0$ throughout,
$\mathbf{F}\cdot d\mathbf{l} = z\,dx + x\,dy + y\,dz = x\,dy$.

- $(0,0)\to(1,0)$: $dy = 0$ → contributes $0$.
- $(1,0)\to(0,1)$: $x = 1-y$, $dy$ from $0$ to $1$ →
  $\int_0^1(1-y)\,dy = \frac{1}{2}$.
- $(0,1)\to(0,0)$: $x = 0$ → contributes $0$.

Circulation $= \frac{1}{2}$.

**(d)** $\frac{1}{2} = \frac{1}{2}$ ✓. **Note what made the surface integral
trivial:** the curl is constant, so the flux is the curl's component times the
area. With a non-constant curl the surface integral would require the full
parametrisation — the subject of ★★★9.

---

## ★3 — Green's theorem for $P = -y^2$, $Q = x^2$

**Boundary (counterclockwise).**

- $(0,0)\to(1,0)$: $dy = 0$, $y = 0$, so $P\,dx = -y^2dx = 0$ → $0$.
- $(1,0)\to(1,1)$: $dx = 0$, so only $Q\,dy = x^2dy = 1\,dy$ survives →
  $\int_0^1 dy = 1$.
- $(1,1)\to(0,1)$: $dy = 0$, $y = 1$, so $P\,dx = -1\,dx$ and the traversal runs
  $x: 1\to0$ → $\int_1^0(-1)\,dx = 1$.
- $(0,1)\to(0,0)$: $dx = 0$, $x = 0$, so $Q\,dy = 0$ → $0$.

Total: $\oint(P\,dx+Q\,dy) = 2$.

**Area integral.**

$$\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}
= 2x - (-2y) = 2x + 2y,$$

$$\iint_{[0,1]^2}(2x+2y)\,dx\,dy = 2\cdot\frac{1}{2} + 2\cdot\frac{1}{2} = 2 . \checkmark$$

Both sides equal $\boxed{2}$.

**Observation.** The two edge contributions come from *different terms* of the
line integral: the vertical edges contribute through $Q\,dy$ and the horizontal
one through $P\,dx$. Writing the boundary as four pieces and being careful with
the direction of traversal on each is where the sign errors live.

---

## ★4 — Flux of $\mathbf{F} = \mathbf{r}$

**(a)** $\nabla\cdot\mathbf{r} = 1+1+1 = 3$.

**(b)** By the divergence theorem the flux out of **any** closed surface bounding
a volume $V$ is

$$\oint\mathbf{r}\cdot d\mathbf{A} = 3V .$$

**(c)** For the cube of side 2 centred at the origin, $V = 8$ and the flux is 24.
Directly: on the face $x = 1$, $\mathbf{r}\cdot\hat{x} = 1$, area 4 → flux 4; six
faces, three of them with nonzero outward normal component, give
$4+4+4 = 12$, and the three faces at $-1$ each contribute
$\mathbf{r}\cdot(-\hat{x}) = -x = +1$ times area 4 → another 12. Total 24 ✓.

For the unit ball, $V = \frac{4}{3}\pi$ and the flux is
$4\pi = 12.5664$. Directly: on the sphere, $\mathbf{r}\cdot\hat{r} = 1$, so the
flux is $\oint dA = 4\pi$ ✓.

**Why this is worth doing.** The identity is a special case of the one used
throughout elasticity and fluid dynamics: the flux of a field that scales linearly
with position measures the volume, which is the discrete statement that
"$\nabla\cdot\mathbf{r} = 3$" is a dimension count.

---

## ★★5 — Interior and exterior field of a uniform ball

**(a)** By spherical symmetry the field is radial, and by Gauss's law the flux
through a sphere of radius $r$ is $-4\pi G M_{\text{enc}}(r)$. The natural surface
is a **sphere centred on the body**, because on it the field has constant
magnitude and is aligned with the normal, so the flux reduces to
$4\pi r^2 g_r$ with no angular integration:

$$4\pi r^2 g_r = -4\pi G M_{\text{enc}} \qquad\Longrightarrow\qquad
g_r = -\frac{G M_{\text{enc}}}{r^2} .$$

Inside ($r \le a$), $M_{\text{enc}} = \tfrac{4}{3}\pi\rho r^3$, so

$$g(r) = -\frac{4}{3}\pi G\rho\, r \qquad\text{(linear in } r\text{)}.$$

Outside ($r \ge a$), $M_{\text{enc}} = M = \tfrac{4}{3}\pi\rho a^3$ and

$$g(r) = -\frac{GM}{r^2} .$$

**This is Newton's shell theorem obtained without computing a single integral over
an aspherical body**, and it is the reason that only the enclosed mass matters.

**(b)** At $r = a$ the interior expression gives
$-\tfrac{4}{3}\pi G\rho a$ and the exterior gives
$-GM/a^2 = -\tfrac{4}{3}\pi G\rho a^3/a^2 = -\tfrac{4}{3}\pi G\rho a$. They agree
✓, so $g$ is continuous at the surface. (Its *derivative* is not: the gradient
tensor jumps, which is why the gravity gradient tensor responds to the boundary.)

**(c)** With $\mathbf{g} = \nabla V$ and $g_r = \partial V/\partial r =
-\tfrac{4}{3}\pi G\rho r$ inside,

$$V(r) = V(0) - \frac{2}{3}\pi G\rho r^2 .$$

At the surface, $V(a) = GM/a = \tfrac{4}{3}\pi G\rho a^2$ (from the exterior
formula $V = GM/r$). Therefore

$$V(0) = \frac{4}{3}\pi G\rho a^2 + \frac{2}{3}\pi G\rho a^2
= 2\pi G\rho a^2,$$

and

$$V(0) - V(a) = \left(2\pi - \frac{4}{3}\pi\right)G\rho a^2
= \frac{2}{3}\pi G\rho a^2 .$$

For $\rho = 3000\ \mathrm{kg\,m^{-3}}$ and $a = 6.4\times10^6$ m:

$$V(0)-V(a) = \frac{2}{3}\pi(6.674\times10^{-11})(3000)(6.4\times10^6)^2
= 1.7176\times10^{7}\ \mathrm{m^2\,s^{-2}} .$$

**Sanity check.** $V(0)/V(a) = 2\pi G\rho a^2 / \left(\tfrac{4}{3}\pi G\rho
a^2\right) = 1.5$, the classical result for a uniform sphere. Since
$V(a) = 3.4352\times10^{7}$ m²/s², the difference is half of it —
$1.7176\times10^{7}$ ✓. **A sign check matters here:** with the positive-potential
convention used in this module, $V$ is *larger* at the centre than at the surface,
because the centre is deeper in the potential well.

**(d)** The argument used only (i) spherical symmetry of the mass distribution and
(ii) the fact that no mass is enclosed by a sphere inside a cavity. Neither
depends on how the mass is arranged *radially*, so the interior field of the cavity
of **any** spherically symmetric body is zero — a shell of arbitrary thickness,
a body with a radially varying density, or a nest of shells. This is the "null
experiment" that makes the gravitational field inside a hollow shell an
experimental test of the inverse-square law, and it is the same statement as the
non-uniqueness of the inverse problem seen from the inside.

---

## ★★6 — Green's first identity on the cube

The identity is

$$\iiint_\Omega\left(\nabla\phi\cdot\nabla\psi + \phi\nabla^2\psi\right)dV
= \oint_{\partial\Omega}\phi\,\frac{\partial\psi}{\partial n}\,dA .$$

With $\phi = x^2$, $\psi = y^2$ on $[0,1]^3$:

**Right-hand side.**

- $\nabla\psi = (0, 2y, 0)$, so $\partial\psi/\partial n$ vanishes on the four
  faces whose normal has no $y$ component ($x = 0,1$ and $z = 0,1$).
- On $y = 1$: $\partial\psi/\partial n = +2y = 2$, and
  $\phi = x^2$, so the contribution is
  $\int_0^1\int_0^1 2x^2\,dx\,dz = 2\cdot\frac{1}{3} = \frac{2}{3}$.
- On $y = 0$: $\partial\psi/\partial n = -2y = 0$ → $0$.

Total right-hand side: $\frac{2}{3}$.

**Left-hand side.**

- $\nabla\phi\cdot\nabla\psi = (2x,0,0)\cdot(0,2y,0) = 0$.
- $\nabla^2\psi = 2$, so
  $\phi\nabla^2\psi = 2x^2$ and
  $\iiint 2x^2\,dV = 2\cdot\frac{1}{3} = \frac{2}{3}$.

Both sides equal $\boxed{\tfrac{2}{3}}$ ✓.

**What this identity is for.** It is the one that turns a differential equation on
$\Omega$ into data on $\partial\Omega$ — used in the next-to-last step of the
proof in ★★★10 below, and the mechanism behind every finite-element
discretisation of Laplace's equation. The exercise is a worked instance of it on a
region where both sides can be evaluated in closed form, which is the only way to
be sure you have the signs right.

---

## ★★7 — Conservation in divergence form

**(a)** With $u$ the density of a conserved quantity and $\mathbf{J}$ its flux,

$$\frac{\partial u}{\partial t} + \nabla\cdot\mathbf{J} = 0 .$$

The first term is the local rate of accumulation; the second is the net outflow
per unit volume.

**(b)** Integrate over a fixed volume $\Omega$ and apply the divergence theorem:

$$\frac{d}{dt}\iiint_\Omega u\,dV = -\oint_{\partial\Omega}\mathbf{J}\cdot d\mathbf{A} .$$

**The total of $u$ inside changes only by what crosses the boundary.** That is the
statement in a form that a finite-volume code can enforce exactly, face by face,
and it does not require $u$ or $\mathbf{J}$ to be differentiable inside.

**(c)** For a steady state with $\partial u/\partial t = 0$ but $\mathbf{J} = u\mathbf{v}$,

$$\nabla\cdot(u\mathbf{v}) = 0
\qquad\Longrightarrow\qquad
u\nabla\cdot\mathbf{v} + \mathbf{v}\cdot\nabla u = 0 .$$

For an **incompressible** medium ($u = \text{const}$) this reduces to
$\nabla\cdot\mathbf{v} = 0$: the velocity field is solenoidal. For a compressible
one, the density gradient can balance a nonzero divergence — which is why mantle
convection codes must distinguish the anelastic and incompressible approximations.

**(d)** The natural scale for the divergence of a velocity field is
$\lvert\mathbf{v}\rvert/L = 10^{-9}/10^{6} = 10^{-15}\ \mathrm{s^{-1}}$. The
reported maximum of $10^{-9}\ \mathrm{s^{-1}}$ is **a million times that scale**,
so either the code does not conserve mass, or the quoted "typical magnitude" is
unrepresentative — for instance if the velocity is much larger in a thin
thermochemical boundary layer whose thickness, not the domain size, sets the scale.
Dividing the reported divergence into the velocity gives an implied variation
length of $\lvert\mathbf{v}\rvert/\lvert\nabla\cdot\mathbf{v}\rvert = 1$ m, which
is not a plausible feature scale for a $10^6$ m domain. **The residual divergence
is meaningless without a length scale to compare it with**; that comparison, not
the raw number, is the diagnostic.

---

## ★★8 — A jump condition at a density contrast

**(a)** Take a pillbox of cross-sectional area $A$ and thickness $\epsilon$
straddling the interface at $z = 0$, with its flat faces parallel to the
interface. Apply the divergence theorem:

$$\oint_{\partial\,\text{pillbox}}\mathbf{g}\cdot d\mathbf{A}
= -4\pi G\,M_{\text{enc}} = -4\pi G\int_{\text{pillbox}}\rho\,dV .$$

As $\epsilon\to0$ the enclosed mass tends to zero for a *finite* density (the
volume shrinks, even though $\Delta\rho \ne 0$), while the flux through the curved
side wall also tends to zero because its area is proportional to $\epsilon$.
Only the two flat faces survive, and their outward normals are $+\hat{z}$ and
$-\hat{z}$:

$$\left(g_z^{+} - g_z^{-}\right)A \to 0
\qquad\Longrightarrow\qquad
\left[g_z\right] \equiv g_z^{+} - g_z^{-} = 0 .$$

**(b)** **The normal component of the gravitational field is continuous across a
density contrast.**

**(c)** The interpretation is that a finite density contrast carries **no surface
mass**: the mass enclosed by a vanishingly thin pillbox vanishes with the
thickness. Consequently the field itself does not jump; what jumps is its *spatial
derivative*, because $\nabla\cdot\mathbf{g}$ takes different values on the two
sides. This contrasts with electrostatics, where a surface *charge* density does
produce a jump in the normal component of $\mathbf{E}$ — and the difference is
exactly that mass is a volume density while surface charge is a surface density.

**Had there been a surface mass density** $\sigma$ (a mathematical idealisation of
a very thin dense layer), the enclosed mass would have been $\sigma A$ and the
jump condition would instead read

$$\left[g_z\right] = -4\pi G\sigma .$$

**Why the differential form is unusable on the interface.** $\rho$ is undefined
there — it takes two different values on the two sides and no value on the
surface — so $\nabla\cdot\mathbf{g} = -4\pi G\rho$ cannot be evaluated. The jump
condition, by contrast, is a statement about well-defined one-sided limits, and it
is what a numerical scheme must implement at a contrast. In practice this is done
by taking the divergence to be a flux balance across cell faces, so that the
ambiguity never arises.

---

## ★★★9 — Stokes' theorem on a hemisphere

**(a)** The boundary of the upper hemisphere (outward normal, so the induced
boundary orientation is counterclockwise viewed from above) is the unit circle in
the plane $z = 0$. On it, $\mathbf{F} = (-y, x, 0) = \hat{\phi}$ and
$d\mathbf{l} = \hat{\phi}\,d\phi$, so

$$\oint_{\partial S}\mathbf{F}\cdot d\mathbf{l} = \int_0^{2\pi}d\phi = 2\pi
= 6.283185307\ldots$$

**(b)** $\nabla\times\mathbf{F} = (0,0,2)$, and on the hemisphere the outward
normal is $\hat{r}$, so

$$\iint_S(\nabla\times\mathbf{F})\cdot d\mathbf{A}
= 2\iint_S \hat{z}\cdot\hat{r}\,dA = 2\iint_S\cos\theta\,dA .$$

With $dA = R^2\sin\theta\,d\theta\,d\phi$ and $R = 1$:

$$2\int_0^{2\pi}\!\!\int_0^{\pi/2}\cos\theta\sin\theta\,d\theta\,d\phi
= 2\cdot2\pi\cdot\left[\frac{\sin^2\theta}{2}\right]_0^{\pi/2} = 2\pi . \checkmark$$

**Equality confirmed analytically.** Note the geometric reading: the flux of a
constant field through a surface equals that field's component along the normal
times the *projected* area, and the projection of the hemisphere onto the $xy$
plane is the unit disk of area $\pi$. So the surface integral is $2\times\pi$
with no integration required.

**(c)** Measured, with an $n\times n$ midpoint grid on $(\theta,\phi)$:

| $n$ | surface integral | relative error |
|---|---|---|
| 100 | 6.283443700 | $4.11\times10^{-5}$ |
| 400 | 6.283201456 | $2.57\times10^{-6}$ |

**(d)** A factor of 4 in $n$ reduced the error by a factor of 16.0, exactly the
second-order convergence of the midpoint rule on a smooth integrand. The reason
this integrand is easier than the disk case of the course demonstration is that
**the hemisphere has a smooth parametrisation with no boundary in the integrand's
domain of dependence**: the integrand $\cos\theta\sin\theta$ is analytic on the
whole rectangle $[0,\pi/2]\times[0,2\pi]$, so the midpoint rule sees a smooth
function. The disk case failed to reach second order because the *region* is
circular and had to be represented by a staircase of square cells, which introduces
an $O(h)$ geometric error. **Smoothness of the region's parametrisation, not just
of the integrand, controls convergence.**

---

## ★★★10 — Uniqueness of the exterior Dirichlet problem

**Statement.** Let $\Omega$ be the region outside a closed surface $S$, let
$\nabla^2u = 0$ in $\Omega$, $u = f$ on $S$, and
$u(\mathbf{r})\to0$ uniformly as $\lvert\mathbf{r}\rvert\to\infty$. Then $u$ is
unique.

**(a)** Set $w = u_1 - u_2$. Then $\nabla^2w = 0$ in $\Omega$ (linearity), $w = 0$
on $S$ (the difference of equal boundary values), and
$w\to0$ uniformly at infinity.

**(b)** Let $\Omega_R$ be the region between $S$ and a sphere $\Sigma_R$ of radius
$R$ enclosing $S$, and apply Green's first identity with $\phi=\psi=w$:

$$\iiint_{\Omega_R}\left(\lvert\nabla w\rvert^2 + w\nabla^2w\right)dV
= \oint_{\partial\Omega_R} w\,\frac{\partial w}{\partial n}\,dA .$$

The $\nabla^2w$ term vanishes by harmonicity. The boundary $\partial\Omega_R$
consists of $S$ (where $w = 0$) and $\Sigma_R$, so

$$\iiint_{\Omega_R}\lvert\nabla w\rvert^2\,dV
= \oint_{\Sigma_R} w\,\frac{\partial w}{\partial n}\,dA .$$

**The hypothesis that does the work** is the uniform decay
$u \to 0$ at infinity: it gives $\lvert w\rvert \le \epsilon_R$ and
$\lvert\partial w/\partial n\rvert \le \eta_R$ on $\Sigma_R$ with
$\epsilon_R,\eta_R\to0$, so the surface term is bounded by
$4\pi R^2\epsilon_R\eta_R$. For a harmonic function of a finite mass distribution
$w \sim C/r$ and $\partial w/\partial n \sim -C/r^2$, giving
$4\pi R^2\cdot(C/R)(C/R^2) = 4\pi C^2/R \to 0$. **Without a decay assumption the
argument fails**, and indeed $\nabla^2 u = 0$ with $u = \text{const}$ and
$u = $ linear function of the coordinates are harmonic exterior solutions that do
not decay.

**(c)** Hence $\iiint_{\Omega_R}\lvert\nabla w\rvert^2\,dV = 0$ for every $R$,
so $\nabla w = \mathbf{0}$ on $\Omega_R$ for every $R$ and therefore on all of
$\Omega$; $w$ is a constant, and since $w\to0$ at infinity that constant is zero.
Thus $u_1 = u_2$ ✓.

**(d)** If the decay hypothesis is replaced by $u\to c$ for an unknown constant
$c$, the conclusion is **weaker and depends on the boundary condition**:

- With a **Dirichlet** condition $u = f$ on $S$, uniqueness still holds *if the
  same* $c$ is in force for both candidates: $w$ is harmonic, bounded, constant
  in the limit, and $w = 0$ on $S$; the strong maximum principle (or the parabolic
  argument via the boundary) forces $w = 0$ everywhere. So the constant is fixed by
  the boundary data.
- With a **Neumann** condition, a constant is genuinely a null function: adding
  any constant to $u$ leaves $\partial u/\partial n$ unchanged and preserves
  $\nabla^2u = 0$. The solutions differ by an additive constant, exactly as in the
  interior problem ([01-06-08](./08-potential-theory-solutions.md), ★★5), and the
  exterior decay condition is what would normally remove it.

**What the theorem does and does not deliver.** It says: *given the boundary data,
the field above the surface is unique.* It says nothing about the distribution of
mass below the surface that produced those data — and that gap is the subject of
Lesson 08.
