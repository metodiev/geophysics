# Solutions — 02-04-02 Strain: Infinitesimal Strain Tensor and Compatibility

> **Read this after attempting the exercises, not before.** Convention:
> extension-positive. Values attributed to the demo are its actual output.

---

## ★1 — A linear displacement field

**(a)** $u_{i,j} = \begin{pmatrix}0.002&0.001\\-0.001&0.003\end{pmatrix}$;
symmetrising: $\varepsilon_{xx} = 0.002$, $\varepsilon_{yy} = 0.003$,
$\varepsilon_{xy} = \varepsilon_{yx} = (0.001-0.001)/2 = 0$.

**(b)** $\omega_{xy} = (0.001-(-0.001))/2 = 0.001$,
$\omega_{yx} = -0.001$; the rotation vector is
$\boldsymbol{\omega} = (0, 0, 0.001)$ — a rotation of 0.001 rad about $z$.

**(c)** $\Delta = 0.002+0.003 = 0.005$: a 0.5 per cent volume increase.

**(d)** Both: a pure shear/normal strain plus a rigid rotation. The fields are
separable by construction (equation (1) of the lesson).

---

## ★2 — Principal strains

**(a)** The characteristic polynomial for the $xy$ block is
$\lambda^2 - 2\lambda - 19 = 0$ (in units of $10^{-4}$), giving
$\lambda = 1\pm\sqrt{20} = 1\pm4.472136$, i.e. 5.472136 and $-3.472136$. With the
$z$-direction contributing $\lambda = 1$, the ordered principal strains are
$\varepsilon_1 = 5.472136\times10^{-4}$,
$\varepsilon_2 = 1.000000\times10^{-4}$,
$\varepsilon_3 = -3.472136\times10^{-4}$.

**(b)** $\Delta = 5+(-3)+1 = 3\times10^{-4}$ (check: the sum of the eigenvalues
$5.472136+1-3.472136 = 3$ ✓).

**(c)** $(\varepsilon_1-\varepsilon_3)/2 = (5.472136+3.472136)/2\times10^{-4} =
4.472136\times10^{-4}$.

**(d)** The in-plane principal directions satisfy
$\tan2\theta = 2\varepsilon_{xy}/(\varepsilon_{xx}-\varepsilon_{yy}) = 4/8 = 0.5$,
so $\theta = 13.2825^\circ$ from the $x$-axis for the greater principal strain.

---

## ★3 — A concrete core

**(a)** $\varepsilon = 0.045\times10^{-3}/300 = 1.5\times10^{-7}$ =
0.15 microstrain.

**(b)** Yes: $\varepsilon \sim 10^{-7} \ll 1$, so the infinitesimal tensor is valid
by many orders of magnitude.

**(c)** Lateral strain $= 0.012\times10^{-3}/300 = 4.0\times10^{-8}$; the ratio of
lateral to axial strain is $4.0\times10^{-8}/1.5\times10^{-7} = 0.266667$.

**(d)** That ratio is Poisson's ratio $\nu$ (the ratio of lateral contraction to
axial extension in a uniaxial stress test), here 0.267 — a typical value for
concrete.

---

## ★4 — Rigid rotation

**(a)** $u_x = x(\cos\theta-1)-y\sin\theta$,
$u_y = x\sin\theta+y(\cos\theta-1)$ with $\theta = 5° = 0.0872665$ rad.

**(b)** $\varepsilon_{xx} = \cos\theta-1 = -0.0038072$.

**(c)** $\theta^2/2 = 0.0038077$; the ratio is $-0.999866$, so the expansion is
accurate to $1.3\times10^{-4}$ relative at 5° (the next term is
$-\theta^4/24 = -2.4\times10^{-6}$, which is exactly the difference).

**(d)** One would report a spurious contraction of $3.8\times10^{-3}$ — 3800
microstrain — for a motion that involves no deformation at all. Since tectonic
strain rates are of order 0.01–0.1 $\mu\varepsilon$/yr, this is three to four
orders of magnitude larger than the signal, which is why geodetic processing
removes rotations explicitly.

---

## ★5 — Reading the demo

**(a)** Strain tensor (dimensionless, as printed):
$\varepsilon_{xx} = 0.00308430$, $\varepsilon_{yy} = 0.00634858$,
$\varepsilon_{zz} = 0$, $\varepsilon_{xy} = 0.00302281$,
$\varepsilon_{xz} = -0.00035$, $\varepsilon_{yz} = 0.00442892$; maximum difference
from the analytic value $6.096\times10^{-10}$.

**(b)** $\boldsymbol{\omega} = (0.00312892, -0.00035, 0.00302281)$;
dilatation $0.00943289$, agreeing with the analytic
$a\cos(ax)\cos(by)+c\,e^{cy}z$ to nine digits.

**(c)** Because the displacement field was constructed with comparable
sinusoidal and exponential terms in both the diagonal and the off-diagonal
gradient components; there is no reason for a general field to favour either. In a
seismic wave the strain and the rotation are also comparable — which is exactly
why an elastic wave has both a P (dilatational) and an S (rotational) part.

**(d)** The *components* of the strain tensor would change (it would rotate), but
the principal strains, the invariants and the dilatation would not. This is the
point of a tensor: components are representation-dependent, the state is not.

---

## ★6 — Convergence

**(a)** Errors $2.868\times10^{-8}$, $7.170\times10^{-9}$, $1.792\times10^{-9}$,
$4.481\times10^{-10}$ at $h = 10^{-2}$ to $1.25\times10^{-3}$; orders 2.000 in
every row.

**(b)** The central difference has error
$\frac{h^2}{6}f'''(\xi)$, so the error is $O(h^2)$; the measured order of exactly
2.000 confirms it.

**(c)** Extrapolating with a factor of four per halving:
$h = 3.125\times10^{-4}$ should give $1.120\times10^{-10}$. Verify numerically.

**(d)** Round-off enters as $\sim\epsilon_{\text{mach}}\,|u|/h$ with
$|u|\sim10^{-2}$ m: at $h = 10^{-3}$ m this is
$2.2\times10^{-16}\times10^{-2}/10^{-3} = 2.2\times10^{-15}$, which is four orders
of magnitude below the truncation error at the same step. Round-off becomes
comparable when $h^2\times(\text{curvature term}) \approx 2.2\times10^{-15}$, i.e.
around $h \sim 10^{-8}$ m — which is far below any geodetic station spacing and
therefore irrelevant in practice, but it is the reason a purely numerical
differentiation has an optimum step (compare lesson 02-03-01 §7).

---

## ★7 — GNSS strain precision

**(a)** With $L = 50$ km and $\sigma_u = 1$ mm:
$\sigma_\varepsilon = \sqrt2\times10^{-3}/5\times10^4 = 2.83\times10^{-8}$ =
0.028 $\mu\varepsilon$.

**(b)** With $L = 15$ km: $\sigma_\varepsilon = 9.4\times10^{-8}$ =
0.094 $\mu\varepsilon$.

**(c)** With $\sigma_u = 0.2$ mm: 0.0057 and 0.019 $\mu\varepsilon$ respectively.

**(d)** Use the longest baselines that still resolve the deformation field of
interest: they give the best per-component precision (by a factor of 3 here), but
they average over any structure with a scale shorter than the baseline. For a
regional map on a 50 km grid, a differencing length comparable to the grid
spacing is the natural choice — the noise-versus-resolution trade-off is explicit
and should be stated.

---

## ★8 — Compatibility testing

**(a)** $\varepsilon_{xx,yy} = 0$, $\varepsilon_{yy,xx} = 0$,
$2\varepsilon_{xy,xy} = 0$: the residual is zero, so this field *is* compatible.
(It corresponds to a displacement $u_x = 0.5xy + f(y)$, $u_y = 0.5xy + g(x)$ with
$f$ and $g$ chosen to satisfy the shear strain.)

**(b)** Yes — but the check in (a) is not sufficient on its own in general; the
full compatibility conditions (all six in 3-D) must be satisfied, and here the
$z$-dependence is absent so the 2-D condition is the relevant one.

**(c)** $\varepsilon_{xx,yy} = 0$, $\varepsilon_{yy,xx} = 0$,
$2\varepsilon_{xy,xy} = 0$: again compatible (the residual is zero). The example is
a reminder that sign changes in the diagonal components do not by themselves break
compatibility — the curvature terms are what matter.

**(d)** Only fields satisfying the compatibility conditions can be integrated to a
single-valued displacement. In practice, measured fields never satisfy them
exactly, so the standard procedure is a least-squares projection onto the
compatible subspace (equivalently, the standard geodetic practice of fitting a
bilinear or spline displacement field and differentiating *that*, which is
compatible by construction). Integrating a raw measured strain field directly
gives a path-dependent answer.

---

## ★★★9 — Finite strain measures

**(a)** With $\varepsilon = \delta/L$ and $\ell/L = 1+\varepsilon$:

- infinitesimal: $\varepsilon$;
- Green: $\frac12[(1+\varepsilon)^2-1] = \varepsilon+\frac{\varepsilon^2}{2}$;
- logarithmic: $\ln(1+\varepsilon) = \varepsilon-\frac{\varepsilon^2}{2}+\frac{\varepsilon^3}{3}-\cdots$.

**(b)**

| $\varepsilon$ | infinitesimal | Green | logarithmic | max difference |
|---|---|---|---|---|
| 0.001 | 0.001000 | 0.0010005 | 0.0009995 | $5\times10^{-7}$ |
| 0.01 | 0.010000 | 0.010050 | 0.009950 | $1.0\times10^{-4}$ |
| 0.1 | 0.100000 | 0.105000 | 0.095310 | $9.7\times10^{-3}$ |
| 0.5 | 0.500000 | 0.625000 | 0.405465 | 0.219535 |
| 1.0 | 1.000000 | 1.500000 | 0.693147 | 0.806853 |

**(c)** The 1 per cent threshold on the *difference between measures* is crossed
near $\varepsilon \sim 0.1$ for the Green measure and about $\varepsilon \sim 0.02$
for the logarithmic one. Seismic strains ($10^{-6}$) and typical GNSS tectonic
strains ($10^{-7}$ per epoch, perhaps $10^{-5}$ over a plate-boundary cycle) are
far below it, so the infinitesimal tensor is safe; ductile shear zones with shear
strains of order 1 (which is common in structural geology) are far above it.

**(d)** The measures differ at second order, so they agree to first order — which
is precisely why the *choice* of measure is immaterial at small strain and
essential at large strain. Any finite-strain analysis must state which measure is
used, because two workers reporting "strain of 0.5" may mean Green, logarithmic or
principal stretch, and the numbers differ by tens of per cent.

---

## ★★★10 — Strain rosette

**(a)** With gauges at 0°, 45° and 90°,
$\varepsilon_0 = \varepsilon_{xx}$,
$\varepsilon_{90} = \varepsilon_{yy}$ and
$\varepsilon_{45} = \frac{\varepsilon_{xx}+\varepsilon_{yy}}{2} +
\varepsilon_{xy}$. Hence

$$\varepsilon_{xx} = \varepsilon_0, \qquad
\varepsilon_{yy} = \varepsilon_{90}, \qquad
\varepsilon_{xy} = \varepsilon_{45} - \frac{\varepsilon_0+\varepsilon_{90}}{2} .$$

**(b)** $\varepsilon_{xx} = 120$, $\varepsilon_{yy} = -20$,
$\varepsilon_{xy} = 40-(120-20)/2 = -10\ \mu\varepsilon$. Principal strains:
$\frac{120-20}{2}\pm\sqrt{(70)^2+(-10)^2} = 50\pm70.710678$, i.e.
$\varepsilon_1 = 120.710678$ and $\varepsilon_2 = -20.710678\ \mu\varepsilon$.
Direction: $\tan2\theta = 2(-10)/140 = -0.142857$, so
$\theta = -4.0690^\circ$ from the $x$-axis.

**(c)** The principal strains depend on the three measurements with different
weights: $(\varepsilon_{xx}+\varepsilon_{yy})/2$ involves both normal gauges and
is well determined, while the shear term involves a combination and is the least
well determined. Propagating independent errors $\sigma$: the mean has standard
error $\sigma/\sqrt2$, and $\varepsilon_{xy}$ has
$\sigma\sqrt{3/2}$ — so the shear (and therefore the principal direction near
isotropy) is the weakest determination.

**(d)** A simulation with $\sigma = 5\ \mu\varepsilon$ on each gauge should give
standard deviations of about 3.5 and 3.5 $\mu\varepsilon$ on the two principal
strains (they are correlated through the mean), and a large scatter in the
principal angle — of order tens of degrees when the two principal strains are
nearly equal, because the direction becomes indeterminate there. Report your
measured standard deviations and the angle scatter; the conclusion that the
principal angle is poorly determined when $|\varepsilon_1-\varepsilon_2| \ll
\sigma$ is the practically important one, and it applies equally to geodetic
strain maps and to borehole breakouts.
