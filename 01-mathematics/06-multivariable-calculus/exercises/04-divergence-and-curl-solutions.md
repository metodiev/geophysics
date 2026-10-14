# Solutions — 01-06-04 Divergence, Curl and Physical Meaning

> **Read this after attempting the exercises, not before.**
>
> Throughout, $G = 6.674\times10^{-11}$ and $\mu_0 = 4\pi\times10^{-7}$ H/m.

---

## ★1 — Divergence and curl of four fields

**(a)** $\mathbf{F} = (x^2,\ 2xy,\ -z)$

$$\nabla\cdot\mathbf{F} = 2x + 2x - 1 = 4x - 1,$$

$$\nabla\times\mathbf{F} = \left(\frac{\partial(-z)}{\partial y}
- \frac{\partial(2xy)}{\partial z},\
\frac{\partial(x^2)}{\partial z} - \frac{\partial(-z)}{\partial x},\
\frac{\partial(2xy)}{\partial x} - \frac{\partial(x^2)}{\partial y}\right)
= (0,\ 0,\ 2y).$$

**(b)** $\mathbf{F} = (yz,\ xz,\ xy)$

$$\nabla\cdot\mathbf{F} = 0 + 0 + 0 = 0, \qquad
\nabla\times\mathbf{F} = (x-x,\ y-y,\ z-z) = \mathbf{0}.$$

This is the field of a magnetic quadrupole-like configuration: both divergence-free
and curl-free, hence locally a gradient of a harmonic function. Indeed
$\mathbf{F} = \nabla(xyz)$.

**(c)** $\mathbf{F} = (x,y,z) = \mathbf{r}$

$$\nabla\cdot\mathbf{F} = 3, \qquad \nabla\times\mathbf{F} = \mathbf{0}.$$

**(d)** $\mathbf{F} = (-y,\ x,\ 0)$

$$\nabla\cdot\mathbf{F} = 0, \qquad
\nabla\times\mathbf{F} = (0-0,\ 0-0,\ 1-(-1)) = (0,0,2).$$

---

## ★2 — Classification

| Field | $\nabla\cdot\mathbf{F}$ | $\nabla\times\mathbf{F}$ | Classification |
|---|---|---|---|
| (a) $(x^2, 2xy, -z)$ | $4x-1$ | $(0,0,2y)$ | neither |
| (b) $(yz, xz, xy)$ | 0 | $\mathbf{0}$ | both |
| (c) $\mathbf{r}$ | 3 | $\mathbf{0}$ | irrotational only |
| (d) $(-y, x, 0)$ | 0 | $(0,0,2)$ | solenoidal only |

**Reading the table.** (b) is the case where a scalar potential exists *and* the
field is solenoidal: the potential is harmonic. This is precisely the situation
outside all sources in gravity and magnetics, which is why that case gets a whole
lesson (Lesson 08). (d) is the opposite extreme: a field with no sources but with
vorticity everywhere, which is the flow pattern of solid-body rotation.

---

## ★3 — Rigid rotation

**(a)** With $\boldsymbol{\Omega} = (0,0,\Omega)$,
$\mathbf{v} = \boldsymbol{\Omega}\times\mathbf{r} = (-\Omega y,\ \Omega x,\ 0)$.
Then

$$\nabla\cdot\mathbf{v} = 0 + 0 + 0 = 0, \qquad
\nabla\times\mathbf{v} = (0,\ 0,\ \Omega - (-\Omega)) = (0,0,2\Omega).$$

**(b)** The vorticity of a rigid rotation is **$2\boldsymbol{\Omega}$**, not zero.
Every material element rotates at the same rate $\Omega$ as the body, so its
vorticity — twice its angular velocity — is $2\Omega$. The two statements are
different because they refer to different things:

- "the fluid is rotating" describes the *motion of the body as a whole*;
- "the flow has vorticity" describes the *relative motion of neighbouring
  parcels*, which is what a small paddle wheel responds to.

For rigid rotation, the paddle wheel spins, so the vorticity is nonzero, even
though the *pattern* of the flow is steady and unchanged. Conversely, a shear flow
such as $\mathbf{v} = (\gamma y, 0, 0)$ has vorticity $-\gamma$ while nothing
appears to rotate at all. **Vorticity is shear, not rotation of an observer's
frame.**

**(c)** With $\Omega = 7.2921\times10^{-5}$ rad/s,

$$\lvert\nabla\times\mathbf{v}\rvert = 2\Omega = 1.45842\times10^{-4}\ \mathrm{s^{-1}}.$$

The units are inverse seconds: vorticity is an angular velocity, that is, radians
per second with the radian dimensionless.

**Check against the demonstration.** The script
[`../code/divergence_curl_demo.py`](../code/divergence_curl_demo.py) reported
`curl v = ( 0.000000e+00, 0.000000e+00, 1.458420e-04) 1/s` and `2*Omega =
1.458420e-04 1/s`, together with a divergence of $0$ to the last digit — the
Cartesian field is linear, so central differences represent it exactly.

---

## ★4 — Divergence and curl of a point-mass field

**(a)** Outside the source, the field $\mathbf{g} = -GM\hat{r}/r^2$ satisfies
$\nabla\cdot\mathbf{g} = 0$ because the gravitational potential is harmonic there
(see Lesson 08). Numerically, at $\mathbf{r} = (700,400,-900)$ m with
$M = 10^{12}$ kg the demonstration measured

$$\nabla\cdot\mathbf{g} = -7.598\times10^{-14}\ \mathrm{s^{-2}}
\quad (h = 1\ \mathrm{m}), \qquad
-7.598\times10^{-16}\ \mathrm{s^{-2}} \quad (h = 0.1\ \mathrm{m}).$$

Both are truncation error, and both fall by exactly 100 when $h$ falls by 10.

**(b)** $\nabla\times\mathbf{g} = \mathbf{0}$ identically, for the reason proved
in [01-06-07](./07-vector-identities-solutions.md), ★3: a gradient is irrotational.
The measured values were $6.858\times10^{-14}$ and $6.858\times10^{-16}$ s⁻² at
the same two steps — again pure truncation error.

**(c)** At that point $r = 1208.30$ m and

$$\lvert\mathbf{g}\rvert = \frac{GM}{r^2} = \frac{66.74}{1.4600\times10^{6}}
= 4.5712\times10^{-5}\ \mathrm{m\,s^{-2}},$$

so the natural scale is

$$\frac{\lvert\mathbf{g}\rvert}{r} = 3.7832\times10^{-8}\ \mathrm{s^{-2}}.$$

Both measured residuals are then $2.0\times10^{-6}$ of the natural scale at
$h = 1$ m and $2.0\times10^{-8}$ at $h = 0.1$ m. **The field of a point mass is
exactly solenoidal and exactly irrotational everywhere it can be evaluated**; the
residuals are the finite-difference scheme, not the physics. The nonzero flux of
the same field through a closed surface (Section 5.2 of the lesson) is the
complementary statement: the source is a singularity, not a region of nonzero
divergence.

---

## ★★5 — Ampère's law around a circular loop

**(a)** On a circle of radius $\rho$, $\mathbf{B} = \frac{\mu_0I}{2\pi\rho}
\hat{\phi}$ and $d\mathbf{l} = \rho\,d\phi\,\hat{\phi}$, so

$$\oint\mathbf{B}\cdot d\mathbf{l}
= \int_0^{2\pi}\frac{\mu_0 I}{2\pi\rho}\,\rho\,d\phi = \mu_0 I .$$

With $I = 2.5\times10^{3}$ A,

$$\oint\mathbf{B}\cdot d\mathbf{l} = (4\pi\times10^{-7})(2500)
= 3.14159\times10^{-3}\ \mathrm{T\,m}.$$

**(b)** At $\rho = 100$ m the same computation gives
$3.14159\times10^{-3}$ T m. **The radius cancels** because the field falls as
$1/\rho$ while the circumference grows as $\rho$.

**(c)** At $(\rho,\phi,z) = (40, 0.3, 12)$ m the field is
$\mathbf{B} = \frac{\mu_0(2500)}{2\pi(40)}\hat{\phi} = 1.25\times10^{-5}$ T in the
azimuthal direction, and

$$\nabla\times\mathbf{B} = \mathbf{0}$$

at that point (the demonstration measured $\lvert\nabla\times\mathbf{B}\rvert =
2.7\times10^{-16}$ s⁻¹, i.e. zero).

**How can the curl be zero everywhere off the wire while the circulation is not?**
Because $\mathbf{B} = \frac{\mu_0I}{2\pi}\nabla\phi_{\text{azimuthal}}$ is locally
a gradient, but the azimuthal angle $\phi$ is **not a single-valued function** on
the punctured domain: it jumps by $2\pi$ on any loop encircling the wire. The
domain is not simply connected, so the condition "curl-free $\Rightarrow$
gradient of a single-valued potential" fails. This is the textbook example of
that failure, and the physically important one: a current-carrying conductor is a
topological obstruction, and any loop linking it has a circulation that no
potential can reproduce.

---

## ★★6 — The same circulation around a square

**(a)** Let the square have vertices $(\pm a, 0)$ and $(0, \pm a)$... to keep the
arithmetic transparent, take the square with sides at $x = \pm a$ and $y = \pm a$.
On the side $y = +a$, $d\mathbf{l} = (dx, 0, 0)$ and
$\mathbf{B}\cdot d\mathbf{l} = B_x\,dx$. With
$\mathbf{B} = \frac{\mu_0I}{2\pi}\frac{(-y,x,0)}{x^2+y^2}$,

$$B_x\big|_{y=a} = -\frac{\mu_0 I}{2\pi}\frac{a}{x^2+a^2},$$

so the contribution of that side is

$$-\frac{\mu_0I}{2\pi}\int_{-a}^{a}\frac{a\,dx}{x^2+a^2}
= -\frac{\mu_0I}{2\pi}\left[\arctan\frac{x}{a}\right]_{-a}^{a}
= -\frac{\mu_0I}{2\pi}\cdot\frac{\pi}{2} = -\frac{\mu_0 I}{4}.$$

On the side $y = -a$, $B_x = +\frac{\mu_0I}{2\pi}\frac{a}{x^2+a^2}$ and the
direction of travel is $x: a \to -a$, so the contribution is again
$-\frac{\mu_0I}{4}$. The two $x$-sides together contribute $-\frac{\mu_0I}{2}$.
By the same computation the two $y$-sides contribute $-\frac{\mu_0I}{2}$, and the
total is

$$\oint\mathbf{B}\cdot d\mathbf{l} = -\mu_0 I .$$

**(b)** $a$ is absent: the result is independent of the size of the square. (The
sign depends on the direction of travel — traversing the square clockwise rather
than counterclockwise reverses it, and the sign convention is the one imposed by
Stokes' theorem with the normal $+\hat{z}$.)

**(c)** This is **Stokes' theorem** (or, equivalently, Ampère's law in integral
form). It requires $\mathbf{B}$ to be continuously differentiable on a surface
bounded by the path — which fails exactly at the wire, so the surface must not
cross it and the path must link it. It also requires a consistent orientation of
the path relative to the chosen normal. **The value depends only on the enclosed
current**, which is the same statement as Section ★★5(b): the loop's size and
shape are irrelevant, so long as the loop links the wire once.

---

## ★★7 — Divergence of a uniform ball's field

**(a)** In the convention of this module, $\mathbf{g} = \nabla V$ and
$\nabla\cdot\mathbf{g} = \nabla^2V = -4\pi G\rho$. Inside the ball,
$\mathbf{g} = -\tfrac{4}{3}\pi G\rho\,r\,\hat{r}$, and in spherical coordinates

$$\nabla\cdot\mathbf{g} = \frac{1}{r^2}\frac{d}{dr}\left(r^2 g_r\right)
= \frac{1}{r^2}\frac{d}{dr}\left(-\frac{4}{3}\pi G\rho\, r^3\right)
= \frac{1}{r^2}\left(-4\pi G\rho\, r^2\right) = -4\pi G\rho .$$

Outside, $\mathbf{g} = -GM\hat{r}/r^2$ and

$$\nabla\cdot\mathbf{g} = \frac{1}{r^2}\frac{d}{dr}\left(r^2\cdot\left(-\frac{GM}{r^2}\right)\right)
= \frac{1}{r^2}\frac{d}{dr}(-GM) = 0 .$$

**(b)** With $\rho = 3000\ \mathrm{kg\,m^{-3}}$ and $a = 500$ m, so that
$r = 0.5a = 250$ m, the expected value is

$$-4\pi G\rho = -4\pi(6.674\times10^{-11})(3000)
= -2.51604\times10^{-6}\ \mathrm{s^{-2}},$$

and a Cartesian central-difference computation of $\nabla\cdot\mathbf{g}$ at
$r = 0.25a$ and $r = 0.5a$, with steps $h = 10$, $1$ and $0.1$ m, returns
$-2.516039\times10^{-6}$ s⁻² in every case. The agreement is to seven significant
figures and is **independent of the step**, because the field is linear in
$\mathbf{r}$ inside the ball and the central difference is exact for it.
Outside, at $r = 2a$, the same computation returns $7.3\times10^{-13}$ s⁻² against
a natural scale of $1.05\times10^{-7}$ s⁻² — five orders of magnitude smaller, as
required of a numerical zero.

**(c)** If a grid cell straddles the boundary at $r = a$, the computed divergence
in that cell mixes a value $-4\pi G\rho$ inside with $0$ outside, so it returns
some intermediate number that depends on the cell's geometry. It is not an
approximation to either value: the true divergence is **undefined** at the
discontinuity. The correct treatment is the **jump condition** obtained from the
integral form — apply the divergence theorem to a thin pillbox straddling the
surface and let its thickness go to zero. This is why finite-volume schemes store
the divergence as a flux balance across faces: the flux is well defined at a
contrast even though the divergence is not.

---

## ★★8 — Does a potential exist?

**(a)** $\mathbf{F} = (2xy,\ x^2-z^2,\ -2yz)$.

$$\nabla\times\mathbf{F} = \left(\frac{\partial(-2yz)}{\partial y}
- \frac{\partial(x^2-z^2)}{\partial z},\
\frac{\partial(2xy)}{\partial z} - \frac{\partial(-2yz)}{\partial x},\
\frac{\partial(x^2-z^2)}{\partial x} - \frac{\partial(2xy)}{\partial y}\right)$$

$$= (-2z+2z,\ 0-0,\ 2x-2x) = \mathbf{0}.$$

The domain $\mathbb{R}^3$ is simply connected, so a potential exists. Indeed

$$\phi = x^2y - yz^2,$$

since $\phi_x = 2xy$, $\phi_y = x^2-z^2$ and $\phi_z = -2yz$. **A potential exists
if and only if the field is a gradient, and the check is that the curl vanishes
on a simply connected domain — not merely that the curl vanishes pointwise.**

**(b)** $\mathbf{F} = \left(\frac{-y}{x^2+y^2},\ \frac{x}{x^2+y^2},\ 0\right)$ on
$\mathbb{R}^3$ minus the $z$ axis. A direct computation gives
$\nabla\times\mathbf{F} = \mathbf{0}$ and $\nabla\cdot\mathbf{F} = 0$ on that
domain. **No single-valued potential exists**, because

$$\oint\mathbf{F}\cdot d\mathbf{l} = 2\pi \ne 0$$

around any loop encircling the $z$ axis (computed in the lesson's Section 3.6; the
field on a circle of radius $\rho$ is $\hat{\phi}/\rho$, so
$\oint = \int_0^{2\pi}\rho\,d\phi/\rho = 2\pi$). The domain is not simply
connected, so the theorem does not apply. **This is the mathematical form of the
wire in ★★5, and the reason a "potential" for the magnetic field can exist
locally but not globally around a current.**

**(c)** $\mathbf{F} = (y,\ -x,\ 0)$ on the unit disk. Then

$$\left(\nabla\times\mathbf{F}\right)_z = \frac{\partial(-x)}{\partial x}
- \frac{\partial y}{\partial y} = -1-1 = -2 \ne 0,$$

so no potential exists. The disk is simply connected, so the failure is not
topological: the field genuinely has circulation (indeed
$\oint\mathbf{F}\cdot d\mathbf{l} = -2\times\text{area}$, the negative of twice
the disk's area).

**Summary of the three cases.** (a) curl-free on a simply connected domain:
potential exists. (b) curl-free on a non-simply connected domain: no global
potential. (c) not curl-free: no potential. All three matter in geophysics, and
(b) is the one most often forgotten.

---

## ★★★9 — Numerical floor of $\nabla\cdot\mathbf{B}$ for a dipole

**Method.** $\mathbf{B} = \frac{\mu_0}{4\pi}\frac{3(\mathbf{m}\cdot\hat{r})\hat{r}
- \mathbf{m}}{r^3}$ with $\lvert\mathbf{m}\rvert = 8\times10^{22}$ A m² along
$z$; divergence by central differences on the ray
$\mathbf{r} = t(5,3,4)$ Mm.

**Results.** Measured divergence, in T/m, and its ratio to the natural scale
$\lvert\mathbf{B}\rvert/r$:

| $t$ | $h = 10^2$ m | $h = 10^3$ m | $h = 10^4$ m | scale $\lvert\mathbf{B}\rvert/r$ |
|---|---|---|---|---|
| 1 | $5.168\times10^{-21}$ | $5.175\times10^{-19}$ | $5.175\times10^{-17}$ | $4.480\times10^{-12}$ |
| 2 | $7.603\times10^{-23}$ | $8.086\times10^{-21}$ | $8.086\times10^{-19}$ | $2.800\times10^{-13}$ |
| 4 | $3.888\times10^{-25}$ | $1.263\times10^{-22}$ | $1.263\times10^{-20}$ | $1.750\times10^{-14}$ |

**(a)** Reported above.

**(b)** At $t=1$ the ratios are $1.15\times10^{-9}$, $1.16\times10^{-7}$ and
$1.16\times10^{-5}$ for the three steps. Each factor of 10 in $h$ multiplies the
residual by about 100, so **the computed divergence scales as $h^2$** — second
order, the truncation order of the central-difference first derivative. The
residual is not a failure of $\nabla\cdot\mathbf{B}=0$ but the size of the
approximation used to test it. With $h = 100$ m and a length scale of $7\times10^6$
m, the relative residual of $10^{-9}$ is what a second-order stencil should give.

Note also the dependence on distance: the ratio *relative to the natural scale*
falls as the observation point moves out, because the field becomes smoother
relative to the step. The relative residual at $h = 10^2$ m drops from
$1.15\times10^{-9}$ at $t=1$ to $2.2\times10^{-11}$ at $t=4$.

**(c)** Convergence order: with $h$ from $10^2$ to $10^4$ the residual changes by
a factor of $10^{4}$ for a factor of $100$ in $h$ — exactly the $h^2$ of a
second-order stencil.

**(d)** **What this establishes:** that the magnetic field of a dipole is
divergence-free at every point tested, to an accuracy set by the discretisation,
and that the residual behaves like the truncation error of the scheme used, which
is evidence that it *is* truncation error rather than physics. **What it does not
establish:** that $\nabla\cdot\mathbf{B} = 0$ *exactly*, at a singularity, or in
the sense of distributions. A numerical test can only confirm a statement at the
resolution of the discretisation, a limitation made concrete in
[01-06-07](./07-vector-identities-solutions.md), ★★★10: the same central
differences return zero for $\nabla^2(1/r)$ at a point $5\times10^{-3}$ from a
singularity, where the computation is meaningless. The exact statement rests on the
vector-potential identity $\mathbf{B} = \nabla\times\mathbf{A}$, which is analytic.

---

## ★★★10 — Gauss's law through a deformed cube

**(a)** The surface encloses the point mass once. By Gauss's law for gravity,

$$\oint\mathbf{g}\cdot d\mathbf{A} = -4\pi GM
= -4\pi(6.674\times10^{-11})(10^{12})
= -8.3868\times10^{2}\ \mathrm{m^{3}\,s^{-2}} .$$

Numerically $-838.6796$ m³/s².

**(b)** The flux is independent of the deformation because the divergence
theorem converts the surface integral into a volume integral of
$\nabla\cdot\mathbf{g}$, and inside that volume (excluding the mass) the divergence
is zero *almost everywhere*. The hypotheses being used are: (i) the field is
continuously differentiable on the region, with the singular point excised by a
small ball; (ii) the boundary is piecewise smooth (a cube plus a hemispherical
cap satisfies this); (iii) the outward orientation is consistent over the whole
closed surface. The excision step is what makes the argument work: strictly, the
flux is evaluated on the surface of the region *minus* a small ball about the
mass, and the ball's contribution is shown to be $-4\pi GM$ in the limit while the
rest vanishes. **Nothing about the deformation of the outer surface enters, which
is the geometric content of the theorem.**

**(c)** Numerically: parametrise each planar face and the hemispherical cap, use a
midpoint rule with $n$ cells per side, and sum the oriented flux. The midpoint
rule error on a smooth integrand is $O(h^2)$ where $h \propto 1/n$, so the flux
error is $O(n^{-2})$; the cap contributes an additional error of the same order.
The lesson's demonstration measured relative errors of $6.8\times10^{-5}$ at
$n = 60$ and $4.25\times10^{-6}$ at $n = 240$ for the undeformed cube — a factor
of 16 for a factor of 4 in $n$, the signature of second-order convergence.

**(d)** If the surface enclosed only half the mass distribution, the flux would be
$-4\pi G\,M_{\text{enc}}$ with $M_{\text{enc}}$ the mass actually inside — but
computing it requires care. The divergence theorem may be applied to the whole
region only if $\mathbf{g}$ is continuously differentiable there, which fails both
at the mass and at the cut where the mass distribution crosses the surface. The
correct procedure is to split the surface into the part enclosing one mass and the
part enclosing the other, apply the theorem to each sub-region, and add — or,
equivalently, to excise small balls about every singular point and account for
each one's contribution separately. **The flux of a closed surface is additive
over the enclosed sources, but only when each source is enclosed by a complete
sub-surface; a surface that slices through a source has a singularity on it, and
the theorem's hypotheses fail there.**
