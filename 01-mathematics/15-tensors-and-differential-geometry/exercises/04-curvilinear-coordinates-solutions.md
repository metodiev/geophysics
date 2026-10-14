# Solutions — 01-15-04 Differential Operators in Curvilinear Coordinates

> **Read this after attempting the exercises, not before.** Every number below was
> computed: analytic results were checked against finite differences of the
> Cartesian form of the same field, and the quadratures are stated with their
> resolution.

---

## ★1 — Parabolic cylinder coordinates

**(a)** With $\mathbf r = \left(\tfrac12(u^{2}-v^{2}),\ uv,\ z\right)$:

$$\frac{\partial\mathbf r}{\partial u} = (u,\ v,\ 0), \qquad
\frac{\partial\mathbf r}{\partial v} = (-v,\ u,\ 0), \qquad
\frac{\partial\mathbf r}{\partial z} = (0,\ 0,\ 1).$$

**(b)** The lengths are $h_u = \sqrt{u^{2}+v^{2}}$,
$h_v = \sqrt{(-v)^{2}+u^{2}} = \sqrt{u^{2}+v^{2}}$ and $h_z = 1$.

**(c)** At $(u,v) = (2,1)$: $h_u = h_v = \sqrt{5} = 2.236068$, $h_z = 1$.

**(d)** The tangent vectors are mutually orthogonal
($\partial_u\cdot\partial_v = -uv + uv = 0$), so

$$ds^{2} = (u^{2}+v^{2})\left(du^{2} + dv^{2}\right) + dz^{2}, \qquad
dV = (u^{2}+v^{2})\,du\,dv\,dz .$$

Two features are worth naming. First, $h_u = h_v$: the system is *conformal* in the
$(u,v)$ plane (the two scale factors are equal), which is why Laplace's equation
takes a simple form there. Second, $h_u$ vanishes on the line $u = v = 0$ — the
parametrisation is singular there, and any operator dividing by $h_u$ must be
specialised or the grid staggered, exactly as at the poles in spherical
coordinates.

---

## ★2 — The operators

**(a)** Cylindrical $(\rho,\phi,z)$ with $h = (1,\rho,1)$:

$$\nabla f = \frac{\partial f}{\partial\rho}\hat{\boldsymbol\rho}
+ \frac1\rho\frac{\partial f}{\partial\phi}\hat{\boldsymbol\phi}
+ \frac{\partial f}{\partial z}\hat{\mathbf z}, \qquad
\nabla\cdot\mathbf F = \frac1\rho\frac{\partial(\rho F_\rho)}{\partial\rho}
+ \frac1\rho\frac{\partial F_\phi}{\partial\phi}
+ \frac{\partial F_z}{\partial z},$$

$$(\nabla\times\mathbf F)_z = \frac1\rho\left[
\frac{\partial(\rho F_\phi)}{\partial\rho}
- \frac{\partial F_\rho}{\partial\phi}\right], \qquad
\nabla^{2}f = \frac1\rho\frac{\partial}{\partial\rho}\left(\rho\frac{\partial f}
{\partial\rho}\right) + \frac{1}{\rho^{2}}\frac{\partial^{2}f}{\partial\phi^{2}}
+ \frac{\partial^{2}f}{\partial z^{2}} .$$

**(b)** Spherical $(r,\theta,\phi)$ with $h = (1,r,r\sin\theta)$:

$$\nabla\cdot\mathbf F = \frac{1}{r^{2}}\frac{\partial(r^{2}F_r)}{\partial r}
+ \frac{1}{r\sin\theta}\frac{\partial(\sin\theta\,F_\theta)}{\partial\theta}
+ \frac{1}{r\sin\theta}\frac{\partial F_\phi}{\partial\phi},$$

$$\nabla^{2}f = \frac{1}{r^{2}}\frac{\partial}{\partial r}
\left(r^{2}\frac{\partial f}{\partial r}\right)
+ \frac{1}{r^{2}\sin\theta}\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{\partial f}{\partial\theta}\right)
+ \frac{1}{r^{2}\sin^{2}\theta}\frac{\partial^{2}f}{\partial\phi^{2}} .$$

**(c)** The **area** factors are the $h_jh_k$ inside the derivatives of the
divergence: $\rho$ in the cylindrical radial term (the $\phi$–$z$ face area grows
with $\rho$), $r^{2}$ in the spherical radial term, and $\sin\theta$ in the
spherical polar term (a latitude band narrows toward the poles). The **arc length**
factors are the $h_i$ that divide in the gradient: $1/\rho$ for
$\partial_\phi$ and $1/(r\sin\theta)$ for $\partial_\phi$ in spherical. Confusing
the two is the lesson's second common mistake and produces an error of tens of per
cent, not a rounding difference.

---

## ★3 — A radial divergence two ways

**(a)** With $F_r = r^{2}\sin\theta$ and $F_\theta = F_\phi = 0$, only the radial
term survives:

$$\nabla\cdot\mathbf F = \frac{1}{r^{2}}\frac{\partial}{\partial r}
\left(r^{2}\cdot r^{2}\sin\theta\right)
= \frac{1}{r^{2}}\cdot4r^{3}\sin\theta = 4r\sin\theta .$$

**(b)** In Cartesian form, $r^{2}\sin\theta\,\hat{\mathbf r}$ becomes
$\mathbf F = \left(x\rho,\ y\rho,\ \rho z\right)$ with
$\rho = \sqrt{x^{2}+y^{2}} = r\sin\theta$, because
$r\sin\theta\cos\phi = x$ and $r\cos\theta = z$ give
$r^{2}\sin^{2}\theta\cos\phi = x\rho$ and $r^{2}\sin\theta\cos\theta = \rho z$.
Then

$$\nabla\cdot\mathbf F = \rho + \frac{x^{2}}{\rho} + \rho + \frac{y^{2}}{\rho}
+ \rho = 3\rho + \frac{x^{2}+y^{2}}{\rho} = 4\rho = 4r\sin\theta . \qquad\square$$

**(c)** At $r = 3$, $\theta = 0.5$:
$4r\sin\theta = 12(0.4794255) = 5.753106$. A finite-difference evaluation of the
Cartesian divergence at that point gives $5.75310646$ — agreement to eight digits,
which is the truncation level of the central difference.

**(d)** Coordinate components $dq^i/dt$ are per-radian and per-second; the physical
component is $r$ times larger for $\theta$ and $r\sin\theta$ times larger for
$\phi$. If the three numbers were read as coordinate components, the field would
have units of the function per second per radian and the divergence would be
dimensionally mixed — a factor of $r$ and $r\sin\theta$ per angular index, i.e.
$1/3$ of the answer at $r = 3$ in the radial slot but a different factor in the
others. This is why every spherical stress or velocity table must state its
convention.

---

## ★4 — Four Laplacians

**(a)** $f = r^{2}$ is radial, so
$\nabla^{2}f = \frac{1}{r^{2}}\frac{d}{dr}\left(r^{2}\cdot2r\right)
= \frac{6r^{2}}{r^{2}} = \boxed{6}$ — the dimension of the space, three
derivatives each contributing two.

**(b)** $f = 1/r$:
$\nabla^{2}f = \frac{1}{r^{2}}\frac{d}{dr}\left(r^{2}\cdot(-1/r^{2})\right)
= \frac{1}{r^{2}}\frac{d}{dr}(-1) = \boxed{0}$ for $r>0$.

**(c)** $f = \ln r$:
$\nabla^{2}f = \frac{1}{r^{2}}\frac{d}{dr}\left(r^{2}\cdot\frac1r\right)
= \frac{1}{r^{2}}\frac{d}{dr}(r) = \boxed{\frac{1}{r^{2}}}$.

**(d)** $f = \sin\theta/r^{2}$ is not radial, so the polar term contributes:

$$\frac{1}{r^{2}}\frac{\partial}{\partial r}\left(r^{2}\frac{\partial f}{\partial r}\right)
= \frac{1}{r^{2}}\frac{\partial}{\partial r}\left(-\frac{2\sin\theta}{r}\right)
= \frac{2\sin\theta}{r^{4}},$$

$$\frac{1}{r^{2}\sin\theta}\frac{\partial}{\partial\theta}
\left(\sin\theta\frac{\partial f}{\partial\theta}\right)
= \frac{1}{r^{2}\sin\theta}\frac{\partial}{\partial\theta}
\left(\frac{\sin\theta\cos\theta}{r^{2}}\right)
= \frac{\cos2\theta}{r^{4}\sin\theta},$$

and the two terms combine:

$$\nabla^{2}\left(\frac{\sin\theta}{r^{2}}\right)
= \frac{2\sin^{2}\theta + \cos 2\theta}{r^{4}\sin\theta}
= \frac{2\sin^{2}\theta + \cos^{2}\theta - \sin^{2}\theta}{r^{4}\sin\theta}
= \boxed{\frac{1}{r^{4}\sin\theta}},$$

using $\sin^{2}\theta + \cos^{2}\theta = 1$. Only (b) requires a delta function: it
is zero everywhere except at the origin while its flux is $-4\pi$ (exercise ★★8),
so the *distributional* statement is
$\nabla^{2}(1/r) = -4\pi\delta^{3}(\mathbf r)$. The other three are ordinary
functions, and (d) is finite except on the polar axis, where the coordinate system
— not the field — is singular.

---

## ★★5 — Divergence from a flux

**(a)** The box is bounded by the surfaces $q^i$ and $q^i + dq^i$. The pair of faces
normal to $q^1$ have area $h_2h_3\,dq^2dq^3$; the pair normal to $q^2$ have area
$h_3h_1\,dq^3dq^1$; the pair normal to $q^3$ have area $h_1h_2\,dq^1dq^2$. The
volume is $h_1h_2h_3\,dq^1dq^2dq^3$.

**(b)** The outward flux through the face at $q^1 + dq^1$ is
$\left(h_2h_3F_1\right)|_{q^1+dq^1}dq^2dq^3$ and the inward flux through the face at
$q^1$ is the same quantity evaluated at $q^1$; subtracting,

$$\text{net flux} = \frac{\partial}{\partial q^1}\left(h_2h_3F_1\right)
dq^1dq^2dq^3 .$$

Dividing by the volume gives the $q^1$ contribution
$\frac{1}{h_1h_2h_3}\partial_{q^1}(h_2h_3F_1)$.

**(c)** Adding the three cyclic contributions:

$$\nabla\cdot\mathbf F = \frac{1}{h_1h_2h_3}\left[
\partial_{q^1}(h_2h_3F_1) + \partial_{q^2}(h_3h_1F_2)
+ \partial_{q^3}(h_1h_2F_3)\right] . \qquad\square$$

**(d)** The factor inside each derivative is the **area of the face through which
the flux passes**, and the prefactor is $1/\text{volume}$: the divergence is a net
flux per unit volume in every coordinate system, which is why the formula cannot be
guessed but can always be reconstructed. The same reading makes the Laplacian
immediate: substituting $F_i = (1/h_i)\partial_{q^i}f$ gives the $h_jh_k/h_i$ inside
each derivative, which is the *face area divided by the arc-length factor*.

---

## ★★6 — Rigid rotation

**(a)** For $\boldsymbol\Omega = \omega\hat z$,
$\mathbf v = \boldsymbol\Omega\times\mathbf r = \omega(-y, x, 0)$, whose spherical
physical components are

$$v_r = \mathbf v\cdot\hat{\mathbf r} = 0, \qquad
v_\theta = \mathbf v\cdot\hat{\boldsymbol\theta} = 0, \qquad
v_\phi = \mathbf v\cdot\hat{\boldsymbol\phi}
= \omega r\sin\theta .$$

The first two vanish because $\hat{\mathbf r}\times\mathbf r = 0$ and
$\boldsymbol\Omega$ has no component in the $\hat{\boldsymbol\phi}$ direction after
projection; the third is the tangential speed at colatitude $\theta$.

**(b)** With $\mathbf v = \left(0, 0, \omega r\sin\theta\right)$ in spherical
physical components, the curl components are

$$(\nabla\times\mathbf v)_r = \frac{1}{r\sin\theta}\frac{\partial}
{\partial\theta}\left(\sin\theta\,F_\phi\right) = \frac{\omega r}{r\sin\theta}
\frac{\partial(\sin^{2}\theta)}{\partial\theta} = 2\omega\cos\theta,$$

$$(\nabla\times\mathbf v)_\theta = -\frac{1}{r}\frac{\partial}
{\partial r}\left(rF_\phi\right) = -\frac{2\omega r\sin\theta}{r}
= -2\omega\sin\theta, \qquad (\nabla\times\mathbf v)_\phi = 0 .$$

So $\nabla\times\mathbf v = 2\omega\left(\cos\theta\,\hat{\mathbf r} -
\sin\theta\,\hat{\boldsymbol\theta}\right) = 2\omega\hat z = 2\boldsymbol\Omega$,
using the identity $\hat z = \cos\theta\,\hat{\mathbf r} -
\sin\theta\,\hat{\boldsymbol\theta}$. $\square$ (The Cartesian route gives the same
thing in one line:
$\nabla\times(\boldsymbol\Omega\times\mathbf r) =
\boldsymbol\Omega(\nabla\cdot\mathbf r) -
(\boldsymbol\Omega\cdot\nabla)\mathbf r = 3\boldsymbol\Omega - \boldsymbol\Omega$.)

**(c)** At $r = 2$, $\theta = \pi/2$, $\omega = 1$: $v_r = v_\theta = 0$,
$v_\phi = 2$, and $\nabla\times\mathbf v =
2\left(\cos\frac\pi2, -\sin\frac\pi2, 0\right) = (0,-2,0)$ in spherical
components — which is $2\hat z$ at that colatitude, as it must be.

**(d)** The $r$ and $\theta$ components of the *velocity* vanish and only the
azimuthal one is present, yet the *curl* is a vector in the $r$–$\theta$ plane. That
is a statement about the **basis**: in spherical coordinates a rigid rotation looks
like azimuthal flow whose speed grows with the distance from the axis,
$\omega r\sin\theta$, and the curl is reconstructed from the way
$\hat{\boldsymbol\phi}$ changes with $\theta$. The corresponding statement in
Cartesian coordinates — where the same field has all three components varying in
space — is that the basis is constant, which is why the Cartesian derivation is one
line and the curvilinear one is three. This contrast is the practical reason the
vector-identity lesson of
[01-06-07](../../06-multivariable-calculus/07-vector-identities.md) restricts index
notation to Cartesian coordinates.

---

## ★★7 — A uniform spherical shell

**(a)** $M = 4\pi R^{2}\sigma = 4\pi(6.371\times10^{6})^{2}(1000)
= 5.100645\times10^{17}$ kg.

**(b)** A Gaussian surface of radius $r<R$ encloses no mass, and the flux of
$\mathbf g$ through it is $4\pi r^{2}g_r$ by spherical symmetry. With
$\oint\mathbf g\cdot\hat{\mathbf n}\,dA = -4\pi GM_{\text{enc}} = 0$ (in the
$\mathbf g = \nabla V$, $\nabla^{2}V = -4\pi G\rho$ convention of the lesson),
$g_r = 0$: the field vanishes **strictly** throughout the interior, not merely at
the centre.

**(c)** Just outside, $M_{\text{enc}} = M$ and

$$g(R) = \frac{GM}{R^{2}} = \frac{4\pi G R^{2}\sigma}{R^{2}}
= 4\pi G\sigma = 4\pi(6.674\times10^{-11})(1000)
= 8.386796\times10^{-7}\ \mathrm{m\,s^{-2}} .$$

Note that $R$ cancels: for a surface layer of fixed mass per area, the field just
outside depends on $\sigma$ alone. That is the statement "the $r^{2}$ in the area
cancels the $1/r^{2}$ in the field".

**(d)** Part (b) is a consequence of the **flux form and the mass enclosed** — the
$4\pi r^{2}$ area and the $1/r^{2}$ field cancel for any spherically symmetric
distribution whose enclosed mass is zero, and it would hold for a shell of any
thickness. Part (c) is also a flux statement, but its *simplicity* comes from
spherical symmetry, which lets the shell mass be written as $4\pi R^{2}\sigma$. The
two are the same theorem applied to the inside and the outside; the physical
content is that gravitational shielding does not exist, because the flux depends on
the enclosed mass only.

---

## ★★8 — The delta function

**(a)** For a radial function, $\nabla^{2}f = \frac{1}{r^{2}}\frac{d}{dr}(r^{2}f')$.
With $f = 1/r$, $f' = -1/r^{2}$, $r^{2}f' = -1$, and its derivative is zero: so
$\nabla^{2}(1/r) = 0$ for every $r>0$. $\square$

**(b)** Using the divergence theorem,

$$\iiint_{r<a}\nabla\cdot\nabla\!\left(\frac1r\right)dV
= \oiint_{r=a}\nabla\!\left(\frac1r\right)\cdot\hat{\mathbf n}\,dA
= \oiint_{r=a}\left(-\frac{1}{a^{2}}\right)dA
= -\frac{4\pi a^{2}}{a^{2}} = -4\pi,$$

independent of $a$, because $\nabla(1/r) = -\hat{\mathbf r}/r^{2}$ and the area
grows exactly as $r^{2}$. $\square$

**(c)** (a) says the function is zero almost everywhere; (b) says its integral over
any ball containing the origin is $-4\pi$. A function that is zero almost everywhere
cannot have a nonzero integral, so the object being integrated is not a function:
$\nabla^{2}(1/r)$ is the distribution $-4\pi\delta^{3}(\mathbf r)$, defined by its
action on test functions, $\int\varphi\,(-4\pi\delta^{3})dV = -4\pi\varphi(0)$. It is
used inside integrals — as in the step from the integral form of the potential to
Poisson's equation — and never evaluated pointwise at the origin, where it has no
value.

**(d)** The two conventions are $\mathbf g = \nabla V$,
$\nabla^{2}V = -4\pi G\rho$ and $\mathbf g = -\nabla\Phi$,
$\nabla^{2}\Phi = +4\pi G\rho$, with $\Phi = -V$. The two errors are (i) quoting
$\nabla^{2}\Phi = -4\pi G\rho$ while also using $\mathbf g = -\nabla\Phi$ (a sign
error in the source term that survives to the outside solution), and (ii) mixing the
two potentials in one derivation, e.g. using $V$ inside a source region and $\Phi$
outside it — the classic sign error of potential-field work, because the exterior
solution $V = GM/r$ is correct in one convention and $-GM/r$ in the other.

---

## ★★★9 — A general orthogonal-coordinate operator library

**(a)** The interface: the caller supplies (i) the parametrisation
$\mathbf r(q^1,q^2,q^3)$, or a function returning $h_i$ for given $(q^i)$; (ii) the
field $f$ or $\mathbf F$ as a *function of the curvilinear coordinates*, returning
physical components; and (iii) the coordinate values and a step for the numerical
derivatives. The library returns $\nabla f$, $\nabla\cdot\mathbf F$,
$\nabla\times\mathbf F$, $\nabla^{2}f$ at the requested point, computed from the
general formulas (4)–(7) of the lesson — never from a table of special cases. The
scale factors are obtained once, by differencing the parametrisation.

**(b)** For prolate spheroidal coordinates with $a = 1$:

$$h_u = h_v = \sqrt{\sinh^{2}u + \sin^{2}v}, \qquad
h_\phi = \sinh u\sin v .$$

The system is orthogonal: the $u$-, $v$- and $\phi$-tangent vectors are pairwise
perpendicular, and $h_u = h_v$ makes the $(u,v)$ part conformal.

**(c)** Numerical scale factors at $(u,v) = (1.0, 0.8)$, $\phi = 0.3$, by central
differences with $h = 10^{-6}$ of the parametrisation:

| quantity | numerical | closed form | relative error |
|---|---|---|---|
| $h_u$ | 1.37684334854 | 1.37684334864 | $7.5\times10^{-11}$ |
| $h_v$ | 1.37684334866 | 1.37684334864 | $1.8\times10^{-11}$ |
| $h_\phi$ | 0.84303773428 | 0.84303773429 | $1.8\times10^{-11}$ |

The agreement is at the finite-difference truncation level: the errors are
$O(h^{2}) = 10^{-12}$-ish, and the residual is round-off amplified by the division
by $2h$. The equality $h_u = h_v$ holds to $10^{-10}$, which is the measured
statement of conformality.

**(d)** Two checks a Cartesian-only implementation cannot perform:

1. **Metric consistency**: the Laplacian of a coordinate function must equal the
   value implied by the metric — $\nabla^{2}r^{2} = 6$ in *any* three-dimensional
   system, and $\nabla^{2}f = 0$ for any function that is linear in Cartesian
   coordinates, e.g. $\nabla^{2}(r\cos\theta) = 0$ and $\nabla^{2}(r\sin\theta\cos\phi) = 0$.
   A missing scale factor breaks these immediately, and they are cheap.
2. **Curl and divergence compatibility**, $\nabla\cdot(\nabla\times\mathbf F) = 0$
   and $\nabla\times\nabla f = \mathbf 0$, evaluated on a field with derivatives in
   every coordinate. A Cartesian implementation satisfies these identically because
   all the $\Gamma$'s vanish; in a curvilinear system they fail unless the metric
   factors are exactly right, and their failure is the diagnostic that a factor is
   missing rather than merely misscaled.

The numerical experiment of the lesson's demonstration is exactly check (2) applied
to a field of the form $f = r^{2}\sin\theta\cos\phi$, whose spherical and Cartesian
gradients agree to $6.9\times10^{-11}$ and whose divergence agrees to $4.6\times10^{-10}$.

---

## ★★★10 — A two-layer Earth

**(a)** For spherical symmetry,

$$M = 4\pi\int_0^{R}\rho(r)r^{2}dr
= 4\pi\left[\rho_c\int_0^{r_c}r^{2}dr + \rho_m\int_{r_c}^{R}r^{2}dr\right]
= \frac{4\pi}{3}\left[\rho_cr_c^{3} + \rho_m\left(R^{3} - r_c^{3}\right)\right],$$

which with $\rho_c = 3000$, $r_c = 3.48\times10^{6}$ m, $\rho_m = 5500$ and
$R = 6.371\times10^{6}$ m gives

$$M = \boxed{5.5163\times10^{24}}\ \text{kg}.$$

**(b)** From $GM/R^{2}$:

$$g(R) = \frac{6.674\times10^{-11}\times5.5163\times10^{24}}
{(6.371\times10^{6})^{2}} = 9.0703\ \mathrm{m\,s^{-2}},$$

and from the flux form, which uses the *same* enclosed mass,
$g = 4\pi G\langle\rho\rangle R/3$ with $\langle\rho\rangle = M/(\tfrac43\pi R^{3})$
— identical by construction, since the two expressions are the same equation
rearranged. The agreement is a check on the arithmetic, not on the physics: the
physics is entirely in $M$ being the enclosed mass.

**(c)** At the core–mantle boundary the enclosed mass is the core's,
$M_c = \tfrac43\pi\rho_cr_c^{3} = 5.30\times10^{23}$ kg, so

$$g_{\text{CMB}} = \frac{GM_c}{r_c^{2}} = 2.9186\ \mathrm{m\,s^{-2}} .$$

It is **lower** than the surface value despite the mantle being denser than the
core: gravity at depth is not about the density *below* the point, it is about the
mass *inside* the radius divided by $r^{2}$, and the mantle contributes about
$5.0\times10^{24}$ kg — ten times the core's mass in this model — which is all
outside the CMB. The general consequence is that $g$ is not monotonic in $r$, and
the real Earth's $g$ actually *increases* with depth through the upper mantle before
falling, because $\rho$ falls faster than $r^{2}$.

**(d)** The mean density is

$$\langle\rho\rangle = \frac{M}{\tfrac43\pi R^{3}}
= \frac{5.5163\times10^{24}}{1.0832\times10^{21}}
= \boxed{5092.6}\ \mathrm{kg\,m^{-3}}.$$

A uniform sphere of that density reproduces the mass, the *surface* gravity and the
exterior potential exactly (by Gauss's law, the exterior field of any spherically
symmetric body depends only on its total mass and radius). It does **not** reproduce
the interior field — the uniform model has $g\propto r$ rising linearly to the
surface value, whereas the two-layer model drops to $2.92\ \mathrm{m\,s^{-2}}$ at
the CMB — nor the potential's second derivative, nor the flattening, nor the moment
of inertia. So a uniform model is a legitimate model of the *exterior* field and a
misleading model of anything that samples the interior.
