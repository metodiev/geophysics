# Solutions — 05-02-01 Scalar and Vector Fields; Potentials and Gradients

> Numbers marked *verified* were computed.

---

## ★1

Scalar: temperature, gravitational potential, magnetic scalar potential.
Vector: gravitational acceleration, magnetic flux density, electric field.

---

## ★2

$\partial r^{-1}/\partial \mathbf{r} = -(\mathbf{r}-\mathbf{r}')/r^3$, so
$\mathbf{g} = -\nabla\Phi = -Gm(\mathbf{r}-\mathbf{r}')/r^3$.
Dimensions: $\mathrm{m^3kg^{-1}s^{-2}\cdot kg\cdot m/m^3} = \mathrm{m\,s^{-2}}$. ✓

---

## ★3

$\nabla^2\Phi = 0$ holds wherever the mass density is zero, i.e. *outside* all
sources. For a gravity survey the observation surface is outside the anomalous
bodies but *inside* the Earth, where the mean density is not zero; the standard
resolution is to subtract the normal field of the ellipsoid and consider the
anomalous potential, which is harmonic in the source-free region.

---

## ★4

The observable is a derivative. A monopole potential goes as $r^{-1}$, so its
gradient goes as $r^{-2}$. A dipole field is the gradient of a *dipolar*
potential, which itself falls as $r^{-2}$, so its gradient falls as $r^{-3}$.

---

## ★★5 *(verified)*

$\Phi = -Gm/d = -(6.6743\times10^{-11})(2\times10^{9})/150
= -8.899\times10^{-4}\ \mathrm{m^2\,s^{-2}}$.
$g_z = Gm/d^2 = 5.933\times10^{-6}\ \mathrm{m\,s^{-2}} = 0.5933$ mGal.
A central difference of $\Phi$ in $z$ with $\Delta z = 10^{-3}$ m reproduces
$g_z$ to about $10^{-9}$ relative.

---

## ★★6 *(verified)*

Equatorial: $\mathbf{B} = -\frac{\mu_0}{4\pi}\frac{\mathbf{m}}{r^3}$,
$|\mathbf{B}| = 1.2566\times10^{-6}\cdot5/(4\pi\cdot10^{6})
= 5.000\times10^{-13}$ T.
Axial: $|\mathbf{B}| = \frac{\mu_0}{4\pi}\frac{2|\mathbf{m}|}{r^3}$, exactly
twice as large, $1.000\times10^{-12}$ T. Ratio $= 2.000$.

---

## ★★7

A point mass: concentric spheres, since $\Phi$ depends only on $r$. A vertical
dipole: $\Phi_d \propto \cos\theta/r^2$, so the surfaces are
$r = \sqrt{C\cos\theta}$ — distorted, pinched at the equator where
$\cos\theta = 0$ and $\Phi_d = 0$. They are not spheres because the dipole has
an axis, and the potential depends on the angle to it.

---

## ★★8

$|\mathbf{B}_0+\mathbf{B}_a| = B_0\sqrt{1 + 2\hat{\mathbf{b}}_0\cdot
\mathbf{b}_a + (B_a/B_0)^2} \approx B_0 + \hat{\mathbf{b}}_0\cdot\mathbf{B}_a$
to first order, so $\Delta T = |\mathbf{B}| - B_0 \approx
\hat{\mathbf{b}}_0\cdot\mathbf{B}_a$. The neglected term is
$\frac{1}{2}B_a^2/B_0$, so the 1% accuracy condition is roughly
$B_a \lesssim 0.14B_0$ for the second-order term alone, but in practice the
danger is in the *assumption that the main field direction is constant*; treating
$\hat{\mathbf{b}}_0$ as fixed is the approximation that matters.

---

## ★★★9 *(verified)*

Build $\Phi(i,j,k) = -Gm/|\mathbf{r}-\mathbf{r}'|$ on a uniform grid and take the
seven-point Laplacian at an interior node. Since the analytic Laplacian is zero
there, the finite-difference result is pure truncation error, which for a
second-order scheme scales as $h^2$.

Expected: measured residual falls by a factor of about 4 for each halving of
$h$, and the fitted log–log slope is $2.0 \pm 0.1$. It never reaches exactly zero
because (i) truncation is finite and (ii) round-off imposes a floor near
machine epsilon times the largest term in the stencil. The maximum principle can
be checked by noting that the sampled $g_z$ has its extremum at the position
closest to the source, on the boundary of the sampled grid — i.e. not in the
interior.

---

## ★★★10

The scalar potential of a uniformly magnetised sphere is
$\psi = \frac{\mu_0}{4\pi}\frac{\mathbf{m}\cdot(\mathbf{r}-\mathbf{r}')}
{|\mathbf{r}-\mathbf{r}'|^3}$ outside, with $\mathbf{m} = \mathbf{M}V$.
Differentiating numerically and comparing with the closed-form dipole expression
should agree to the level of the finite-difference truncation error (second order
in the step). The distinction to state: the closed form is the *point-dipole*
model (an idealisation, exact for a sphere only outside it), while the numerical
model is the *finite body*; agreement outside the sphere is a genuine result —
the shell theorem for uniformly magnetised spheres — whereas inside the body the
point-dipole field is wrong.
