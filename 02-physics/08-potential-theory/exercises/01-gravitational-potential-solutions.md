# Solutions — 02-08-01 Newtonian Gravitational Potential and Field

> **Read this after attempting the exercises, not before.** Convention throughout:
> $V > 0$, $\mathbf{g} = \nabla V$, $\nabla^2V = -4\pi G\rho$, with
> $G = 6.674\,30\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$. Values attributed to the
> demonstration are its actual output.

---

## ★1 — A point mass

**(a)** $V = GM/r = 6.674\,30\times10^{-11}\times10^{12}/1000
= 6.674\,300\times10^{-2}$ m$^2$ s$^{-2}$.

**(b)** $\lvert\mathbf{g}\rvert = GM/r^2 = 6.674\,30\times10^{-5}$ m s$^{-2}$
$= 6.6743$ mGal.

**(c)** For a radial potential, $\nabla V = (dV/dr)\hat{\mathbf{r}}$, and
$dV/dr = -GM/r^2$. So $\nabla V = -GM\hat{\mathbf{r}}/r^2$, which points *inward*,
toward the mass — the physically required direction. The minus sign is the
statement that $V$ *increases* toward the mass while $\mathbf{g}$ points toward it,
which is exactly why this convention has $\mathbf{g} = +\nabla V$ rather than
$-\nabla V$.

**(d)** $V = GM/r = 1$ gives $r = GM = 66.743$ m.

---

## ★2 — A spherical shell

**(a)** Outside a spherically symmetric body the field is the point-mass field of
the same total mass: $\lvert\mathbf{g}\rvert = GM/r^2 = 6.674\,30\times10^{-11}
\times10^{13}/4\times10^6 = 1.668\,575\times10^{-4}$ m s$^{-2}$ $= 16.6858$ mGal.

**(b)** Inside the shell the field is **exactly zero**: no mass is enclosed, and the
shell's contributions cancel in every direction. The demonstration's quadrature
returns a value of order $10^{-19}$ m s$^{-2}$, i.e. zero to the arithmetic.

**(c)** The potential is non-zero even where the field vanishes, because the
potential is not a force: at $r=500$ m inside the shell,
$V = GM/a = 6.674\,30\times10^{-11}\times10^{13}/1000 = 6.674\,30\times10^{-1}$
m$^2$ s$^{-2}$ — a constant everywhere inside, as it must be if the field is zero.
At $r = 2000$ m, $V = GM/r = 3.337\,15\times10^{-1}$ m$^2$ s$^{-2}$.

**(d)** The three parts of the theorem:
1. a shell exerts no field in its interior — this is what (b) tests;
2. a shell exerts, outside itself, exactly the field of a point mass at its centre
   with the same total mass — this is what (a) tests;
3. therefore any spherically symmetric body behaves as a point mass when viewed
   from outside.
Part (c) tests a fourth, related statement: the potential inside a shell is
constant, which is the integral form of (1).

---

## ★3 — A uniform sphere

**(a)** Inside, $g = \tfrac43\pi G\rho r$:

| $r$ | $g$ (m s$^{-2}$) |
|---|---|
| $0.25R$ | $2.455\,323$ |
| $0.50R$ | $4.910\,647$ |
| $0.75R$ | $7.365\,970$ |
| $1.00R$ | $9.821\,294$ |

**(b)** $M = \tfrac43\pi R^3\rho = 5.972\,803\times10^{24}$ kg, so
$GM/R^2 = 9.821\,294$ m s$^{-2}$ — identical to the value from the interior formula
at $r=R$. The field is continuous because the enclosed mass is continuous.

**(c)** $g$ rises linearly from $0$ at the centre, reaches $\tfrac43\pi G\rho R$ at
the surface, and then falls as $GM/r^2$; the maximum is **at the surface** (for this
density profile). For a uniform body the interior branch is always increasing, so
the maximum sits at the boundary of the two branches.

**(d)** At $r<R$ the interior formula (which uses $M_{\text{enc}}\propto r^3$); at
$r\ge R$ the exterior formula (which uses the constant $M$). Using the exterior
formula inside would give $GM/r^2$, which diverges as $r\to0$ and is wrong by a
factor $R^3/r^3$.

---

## ★4 — A point mass at depth

**(a)** $g_z(x) = GMh/(x^2+h^2)^{3/2}$ with $M = 1.5708\times10^{12}$ kg and
$h = 1500$ m:

| $x$ (m) | $g_z$ (m s$^{-2}$) |
|---|---|
| $0$ | $4.659\,55\times10^{-5}$ |
| $750$ | $3.334\,10\times10^{-5}$ |
| $1500$ | $1.647\,40\times10^{-5}$ |

**(b)** $x_{1/2} = h\sqrt{2^{2/3}-1} = 0.766\,421h = 1149.63$ m. At $x=750$ m the
profile is at $71.6$ per cent of the peak, so it is above half: consistent, since
$750 < 1149.63$. The half maximum is crossed between $x=750$ and $x=1500$ m, where
the value $1.647\,40\times10^{-5}$ is $35.4$ per cent of the peak.

**(c)** The centre is at $1000+500 = 1500$ m depth — the *same* depth as the point
mass. Since a sphere is spherically symmetric, and since they have the same mass
and the same centre, they produce **exactly the same external field**. The only
difference is inside the sphere, which the surface data never see.

**(d)** Using the top depth: $g_z(0) = GM/1000^2 = 1.048\,398\times10^{-4}$
m s$^{-2}$. Ratio to (a): $1.048\,398\times10^{-4}/4.659\,55\times10^{-5} = 2.250$.
This is the error of the classic conflation — a factor $2.25$ at the peak. Note that
the erroneous profile is *sharper* and crosses the correct one at large distance,
as the demonstration's table shows (ratio $0.742$ at $x = 4000$ m), so the error does
not merely scale the amplitude.

---

## ★5 — Reading the demonstration

**(a)** Worst relative error of $\lvert\mathbf{g}\rvert$ against $GM/r^2$:
$5.03\times10^{-15}$, at $n_{\cos} = 80$, $n_{\phi} = 160$ (the coarsest grid). The
error does not decrease systematically with resolution because it is already at
round-off — that is the point.

**(b)** Worst interior field value: $2.10\times10^{-15}$ of $GM/a^2$, at the
off-axis point $(0.7a, -0.3a)$; the on-axis centre gives $2.67\times10^{-17}$. Note
that the value is not zero exactly, because quadrature of a function that integrates
to zero is limited by round-off.

**(c)** Worst relative error of the interior profile against
$\tfrac43\pi G\rho r$: $1.56\times10^{-6}$ at $r/R = 0.10$, with
$n_{\text{shells}} = 4000$. The profile's column in the demonstration's table falls
from $4.000\times10^{-4}$ at $n_{\text{shells}} = 50$ to $1.000\times10^{-4}$ at
$100$, $2.500\times10^{-5}$ at $200$ and $3.906\times10^{-7}$ at $1600$ — a factor
$4$ per doubling, i.e. **second order** in the shell spacing, because the shell sum
is the midpoint rule for the enclosed-mass integral.

**(d)** $x_{1/2}/h = 1.0000000000$ (ten decimal places). The finite-line deviation
from the two-dimensional formula is $3.775\times10^{-2}$ at $L = 5h$ and
$4.000\times10^{-6}$ at $L = 500h$.

**(e)** (a)–(c) are limited by **numerics** (round-off for the exterior field and the
interior zero, first-order quadrature for the interior profile); (d) is limited by
**physics** — the two-dimensional formula is exact only for infinite strike length,
and a finite line genuinely differs from it. The distinction matters: refining a grid
removes (a)–(c); no refinement removes (d).

---

## ★6 — Two buried point masses

**(a)** At the origin, with $G M_1 = 6.674\,30\times10^{-11}\times2\times10^{12}
= 133.486$ m$^3$ s$^{-2}$ and $G M_2 = 66.743$ m$^3$ s$^{-2}$:

$$g_z(0) = \frac{GM_1}{800^2} + \frac{GM_2\times2000}
{(1500^2+2000^2)^{3/2}}
= 2.085\,72\times10^{-4} + 8.543\,1\times10^{-6}
= 2.171\,15\times10^{-4}\ \text{m s}^{-2} = 21.711\ \text{mGal}.$$

**(b)** At $(1500,0,0)$:

$$g_z = \frac{GM_1\times800}{(1500^2+800^2)^{3/2}} + \frac{GM_2}{2000^2}
= 3.175\,10\times10^{-5} + 1.668\,58\times10^{-5}
= 3.842\,17\times10^{-5}\ \text{m s}^{-2} = 3.842\ \text{mGal}.$$

**(c)** $21.711$ mGal and $3.842$ mGal.

**(d)** At the origin the first body dominates by a factor $24$: it is twice as
massive and much shallower, and the peak of a point-mass anomaly scales as $M/h^2$.
At $(1500,0,0)$ the second body contributes $43$ per cent of the total even though
it is less massive, because the station is directly above it while the first body is
$1700$ m away horizontally. The lesson is that neither mass nor depth alone predicts
which body dominates a given station — the solid angle does.

---

## ★7 — A cylinder inferred from its profile

**(a)** For the infinite cylinder the half-width at half maximum equals the depth:
$h = 2000$ m.

**(b)** $g_z(0) = 2G\lambda/h$, so

$$\lambda = \frac{g_z(0)h}{2G} = \frac{3.6694\times10^{-5}\times2000}
{2\times6.674\,30\times10^{-11}} = 5.4978\times10^{8}\ \text{kg\,m}^{-1}.$$

**(c)** $\rho = \lambda/(\pi a^2) = 5.4978\times10^{8}/(\pi\times250^2)
= 2800.0$ kg m$^{-3}$. This is a *nominal* rock density, chosen so the example is
self-consistent; it is not a measured value.

**(d)** Neither inference is exactly valid. The demonstration's finite-line table
gives a deviation of $3.775\times10^{-2}$ at $L/h = 5$, $2.491\times10^{-3}$ at
$L/h = 20$, $9.999\times10^{-5}$ at $L/h = 100$ and $4.000\times10^{-6}$ at
$L/h = 500$. With $L = 2000$ m and $h = 2000$ m, $L/h = 1$, so the deviation is
*larger* than the $3.8$ per cent quoted for $L/h = 5$ — the two-dimensional formula
will overestimate the amplitude appreciably and the half-width rule will be
correspondingly unreliable. A short body must be modelled as a three-dimensional
body; the depth would come out too shallow if the two-dimensional rule were applied
naively. Note that $L/h \gtrsim 10$ (here $L \gtrsim 20$ km) is the working threshold
for a few per cent.

---

## ★8 — Units and dimensions

**(a)** $3.6694\times10^{-5}$ m s$^{-2}$ $= 3.6694$ mGal (since
$1$ mGal $= 10^{-5}$ m s$^{-2}$).

**(b)** $0.01$ mGal $= 1.0\times10^{-7}$ m s$^{-2}$.

**(c)** $[G\lambda h] = (\text{m}^3\text{kg}^{-1}\text{s}^{-2})(\text{kg}\,\text{m}^{-1})
(\text{m}) = \text{m}^3\text{s}^{-2}$, and dividing by $[x^2+h^2] = \text{m}^2$
gives m s$^{-2}$. ✓ Note that the two-dimensional kernel carries a *different* power
of length from the three-dimensional one; the check is a good way to catch a kernel
error.

**(d)** $[\nabla^2V] = \text{m}^2\text{s}^{-2}\text{m}^{-2} = \text{s}^{-2}$; and
$[4\pi G\rho] = (\text{m}^3\text{kg}^{-1}\text{s}^{-2})(\text{kg}\,\text{m}^{-3})
= \text{s}^{-2}$. ✓

**(e)** $1$ E $= 10^{-9}$ s$^{-2}$, so over $1$ m the fractional change in $g$ is
$10^{-9}\times1/9.81 = 1.02\times10^{-10}$ — that is $10^{-10}g$, which for a
$100$ mGal anomaly is a $10^{-10}\times9.81/(100\times10^{-5}) = 10^{-6}$ fractional
change, or $10^{-4}$ mGal. That is well below the resolution of any relative
gravimeter, which is why gravity gradiometry needs dedicated instruments rather
than differentiating gravimeter data.

---

## ★★★9 — A linearly decreasing density profile

**(a)** $M(r) = \int_0^r4\pi\rho_0(1-r'/R)r'^2dr'
= 4\pi\rho_0\left(\frac{r^3}{3} - \frac{r^4}{4R}\right)$, and at $r=R$,
$M = 4\pi\rho_0R^3\left(\frac13-\frac14\right) = \frac{\pi\rho_0R^3}{3}
= 1.4932\times10^{24}$ kg, which is $5.9728\times10^{24}/4$ — a quarter of the
uniform sphere's mass, as expected since the mean density is $\rho_0/3$.

**(b)** $g(r) = GM_{\text{enc}}(r)/r^2 = 4\pi G\rho_0\left(\frac{r}{3}
-\frac{r^2}{4R}\right)$ — quadratic in $r$, not linear. The physical reason: even
though the *enclosed mass* still grows, the mass is depleted near the surface, so
the $1/r^2$ weighting changes.

**(c)** $dg/dr = 0$ gives $\frac13 - \frac{r}{2R} = 0$, i.e. $r = \frac{2R}{3}
= 4.247\times10^6$ m. For the uniform sphere the maximum was at the surface. The
maximum moves inward because the mass is concentrated toward the centre: the field
grows as the enclosed mass grows, but once the local density is low enough the
$1/r^2$ falloff wins *before* the surface is reached.

**(d)** $g_{\max} = \frac{4\pi G\rho_0R}{9} = 3.2738$ m s$^{-2}$ and
$g(R) = \frac{\pi G\rho_0R}{3} = 2.4553$ m s$^{-2}$, so the ratio is exactly $4/3$.

**(e)** The two profiles differ inside the body only (both give
$GM/r^2$ outside, with the same $M$ if the total masses match). Surface gravity
alone therefore *cannot* distinguish them for equal total mass — the difference is
entirely in the interior field and in the interior potential. Distinguishing them
requires either a measurement inside the body (borehole gravity) or an independent
constraint on the density profile. This is a concrete instance of the
non-uniqueness of lesson 06: the external field determines the external field.

---

## ★★★10 — The shell null experiment

**(a)** Inside the shell the field is exactly zero. The same mass $10^{13}$ kg at a
distance of $100$ m gives $G\times10^{13}/10^4 = 6.674\,30\times10^{-2}$ m s$^{-2}$
$= 6674$ mGal.

**(b)** The ratio is infinite: zero versus $6674$ mGal. A gravimeter with a
$0.01$ mGal resolution could detect the concentrated mass thousands of times over
and would detect the shell as *nothing at all*. That is the null experiment: a
shell, and more generally any spherically symmetric redistribution of the enclosed
mass, is invisible from inside.

**(c)** The cave as a sphere of radius $10$ m with density contrast
$1.2 - 2650 = -2648.8$ kg m$^{-3}$: mass
$\tfrac43\pi(10)^3\times(-2648.8) = -1.1095\times10^{7}$ kg. With the *centre* at
$60$ m depth (top at $50$ m),

$$g_z = \frac{G\lvert M\rvert}{60^2} = 2.057\times10^{-7}\ \text{m s}^{-2}
= 0.0206\ \text{mGal}.$$

**(d)** Two approximations, in opposite directions:
- Treating the cavity as a sphere rather than a void of the correct shape makes the
  estimate **too small** if the real cavity is elongated (more mass removed at depth
  contributes less per unit volume, but more of it is at the shallower end); for a
  spherical void in a half-space truncation, ignoring the free surface also makes the
  estimate slightly too small, because the missing rock above reduces the field.
- Using the centre depth in the point-mass formula rather than integrating over the
  sphere's volume is an excellent approximation here ($R/d = 1/6$), and the first
  correction is $O((R/d)^2) = 3$ per cent; its direction depends on which moments
  are retained, so it is stated as a systematic of that order rather than as an
  over- or under-estimate.
The physically meaningful caveats are the assumed shape and the assumed density
contrast ($2648.8$ kg m$^{-3}$ assumes an empty cavity, which is rarely true — a
partially filled or air-filled cavity has a larger density and a smaller anomaly).
