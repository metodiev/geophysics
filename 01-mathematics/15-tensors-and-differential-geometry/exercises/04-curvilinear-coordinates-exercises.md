# Exercises — 01-15-04 Differential Operators in Curvilinear Coordinates

Attempt these **closed-book** before opening the
[solutions](./04-curvilinear-coordinates-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $(q^1,q^2,q^3)$ are the coordinates, $h_i$ the scale factors,
$\hat{\mathbf e}_i$ the orthonormal physical basis, and $F_i$ the **physical**
components of a vector field (so $\mathbf F = F_1\hat{\mathbf e}_1 + \dots$).
$V$ is the potential with $\mathbf g = \nabla V$ and
$\nabla^{2}V = -4\pi G\rho$; $G = 6.674\times10^{-11}$ in SI. State any convention
you add, and always name the coordinate system in your answer.

Problems referring to
[`../code/curvilinear_operators_demo.py`](../code/curvilinear_operators_demo.py)
require you to run it and report its actual output.

---

## ★ Foundational

**★1.** **Parabolic cylinder coordinates** are defined by
$x = \tfrac12(u^{2} - v^{2})$, $y = uv$, $z = z$.

(a) Compute the three tangent vectors $\partial\mathbf r/\partial q^i$.
(b) Compute the scale factors $h_u$, $h_v$, $h_z$.
(c) Evaluate them at $(u,v) = (2,1)$.
(d) Write $ds^{2}$ and $dV$, and state whether the system is orthogonal.

---

**★2.** Write down, without consulting a table, the gradient, divergence, curl
(one component) and Laplacian in

(a) cylindrical coordinates $(\rho,\phi,z)$;
(b) spherical coordinates $(r,\theta,\phi)$;
(c) for each, name the factor that comes from an *area* rather than from an arc
length, and say where it appears.

---

**★3.** For the spherical field $\mathbf F = (r^{2}\sin\theta,\,0,\,0)$ in
physical components:

(a) compute $\nabla\cdot\mathbf F$ from the curvilinear formula;
(b) compute it again by converting to Cartesian components and differentiating
there;
(c) evaluate both at $r = 3$, $\theta = 0.5$;
(d) state what changes if the same three numbers are interpreted as coordinate
components $dq^i/dt$ instead.

---

**★4.** Compute $\nabla^{2}f$ for

(a) $f = r^{2}$;
(b) $f = 1/r$;
(c) $f = \ln r$;
(d) $f = \sin\theta/r^{2}$;

and state in which cases the answer is a delta function rather than a function.

---

## ★★ Applied

**★★5.** Derive the divergence formula from the flux through a curvilinear box.

(a) Sketch the box bounded by the coordinate surfaces $q^i$ and $q^i + dq^i$ and
write the area of each pair of faces.
(b) Compute the net flux in the $q^1$ direction and divide by the volume
$h_1h_2h_3\,dq^1dq^2dq^3$.
(c) Add the three pairs and recover the general formula.
(d) Explain where each factor inside the derivative comes from, in words.

---

**★★6.** Rigid rotation.

(a) Write the velocity field of a rigid body rotating with angular velocity
$\boldsymbol\Omega = \omega\hat z$, in spherical physical components.
(b) Compute $\nabla\times\mathbf v$ and show it equals $2\boldsymbol\Omega$.
(c) Evaluate the components at $r = 2$, $\theta = \pi/2$, $\omega = 1$.
(d) State which components vanish and why the answer is a statement about the
*basis* turning rather than about the rotation.

---

**★★7.** A uniform spherical shell has radius $R = 6371$ km and surface density
$\sigma = 1000\ \mathrm{kg\,m^{-2}}$.

(a) Compute its mass.
(b) Using the flux form, show that the gravitational field vanishes strictly inside
the shell.
(c) Compute the field just outside.
(d) State which of (b) and (c) is a consequence of the $1/r^{2}$ in the flux and
which is a consequence of spherical symmetry.

---

**★★8.** The delta function from a flux.

(a) Show $\nabla^{2}(1/r) = 0$ for $r>0$ from the radial Laplacian.
(b) Integrate $\nabla\cdot\nabla(1/r)$ over a ball of radius $a$ and show the
result is $-4\pi$ independently of $a$.
(c) Reconcile (a) and (b) and state the sense in which
$\nabla^{2}(1/r) = -4\pi\delta^{3}(\mathbf r)$ is a statement about distributions.
(d) State the two sign errors that arise from mixing the conventions
$\nabla^{2}V = -4\pi G\rho$ and $\nabla^{2}\Phi = +4\pi G\rho$.

---

## ★★★ Research-oriented

**★★★9.** Write a general orthogonal-coordinate operator library driven by a
scale-factor function, and test it on a system of your choice.

(a) State the interface: what the caller supplies and what the library returns.
(b) Apply it to **prolate spheroidal coordinates**
$x = a\sinh u\sin v\cos\phi$, $y = a\sinh u\sin v\sin\phi$,
$z = a\cosh u\cos v$, whose scale factors are
$h_u = h_v = a\sqrt{\sinh^{2}u + \sin^{2}v}$ and $h_\phi = a\sinh u\sin v$.
(c) Verify the scale factors numerically by differencing the parametrisation, and
report the relative error at $(u,v) = (1.0, 0.8)$ with $a = 1$.
(d) State the two checks the library must perform that a Cartesian-only
implementation cannot, and what the tests would catch.

---

**★★★10.** A two-layer Earth model has a core of density
$\rho_c = 3000\ \mathrm{kg\,m^{-3}}$ out to $r_c = 3480$ km and a mantle of
density $\rho_m = 5500\ \mathrm{kg\,m^{-3}}$ out to $R = 6371$ km.

(a) Compute the total mass by quadrature of the spherically symmetric form.
(b) Compute the surface gravity two ways: from $GM/R^{2}$ and from the flux form,
and show they agree.
(c) Compute the gravity at the core–mantle boundary, and explain why it is *lower*
than at the surface although the density below it is higher.
(d) Compute the model's mean density and compare it with a uniform sphere of the
same mass and radius; state which quantity the uniform model reproduces and which
it does not.

---

## Self-check

For every result, check the dimensions before believing the number: a divergence
has the units of the field per metre, a Laplacian of a potential has the units of
the potential per metre squared, and angular derivatives carry the scale factor
that converts per-radian into per-metre.
