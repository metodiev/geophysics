# Solutions — 01-05-05 Integration Techniques and Definite Integrals

> **Read this after attempting the exercises, not before.** Numerical values were
> computed; the quadrature error formulas are used, not merely quoted.

---

## ★1 — Four integrals

**(a)** $\displaystyle\int_0^{2}(3x^{2}-2x)\,dx = \left[x^{3}-x^{2}\right]_0^{2} = 8-4 = \boxed{4}$.

**(b)** $\displaystyle\int_1^{e}\frac{dx}{x} = \left[\ln x\right]_1^{e} = \ln e - \ln 1 = \boxed{1}$.

**(c)** By parts with $u = x$, $dv = e^{-x}dx$:

$$\int x e^{-x}dx = -xe^{-x} + \int e^{-x}dx = -(x+1)e^{-x} + C,$$

so

$$\int_0^{1}xe^{-x}dx = \left[-(x+1)e^{-x}\right]_0^{1}
= -\frac{2}{e} - (-1) = 1 - \frac{2}{e} = \boxed{0.26424111765711533} .$$

**(d)** Substitute $z = 2u$, $dz = 2du$:

$$\int\frac{dz}{z^{2}+4} = \frac{1}{2}\int\frac{du}{u^{2}+1} = \boxed{\frac{1}{2}\arctan\frac{z}{2} + C} .$$

---

## ★2 — Checks

| | Differentiate the answer | Units of integrand × differential |
|---|---|---|
| (a) | $\dfrac{d}{dx}(x^{3}-x^{2}) = 3x^{2}-2x$ $\checkmark$ | (dimensionless integrand) × m = m — the answer is an *area*, not a length. If $x$ were a length in m and $f$ a density per unit length, the answer would be a mass; the check is on the product, not on the integral alone |
| (b) | $\dfrac{d}{dx}\ln x = 1/x$ $\checkmark$ | $(1/x)\,dx$ is dimensionless / dimensionless; the result 1 is a pure number, which is why $\ln$ is the natural variable for ratios |
| (c) | $\dfrac{d}{dx}\left[-(x+1)e^{-x}\right] = -(e^{-x} - (x+1)e^{-x}) = xe^{-x}$ $\checkmark$ | $x\,e^{-x}\,dx$: with $x$ a time in yr, the answer has units of yr |
| (d) | $\dfrac{d}{dz}\left[\tfrac12\arctan(z/2)\right] = \tfrac12\cdot\dfrac{1/2}{1+z^{2}/4} = \dfrac{1}{z^{2}+4}$ $\checkmark$ | $dz/(z^{2}+4)$ has units of 1/(length) if $z$ is a length (and so does the logarithm-free answer) |

The differentiation check is exact and should be automatic. The dimensional check
catches a different class of error — the missing $4\pi r^{2}$ in a mass integral, for
instance.

---

## ★★3 — Compaction column

**(a)** With $\rho(z) = \rho_g - (\rho_g-\rho_f)\phi_0 e^{-z/\lambda}$ and
$\phi_0 = 0.55$, $\lambda = 800$ m, $\rho_g-\rho_f = 1620\ \mathrm{kg\,m^{-3}}$:

$$\frac{m}{A} = \int_0^{H}\rho(z)\,dz
= \rho_g H - (\rho_g-\rho_f)\phi_0\lambda\left(1 - e^{-H/\lambda}\right)
= 2650H - 712800\left(1-e^{-H/800}\right),$$

using the substitution $u = z/\lambda$, $dz = \lambda\,du$.

**(b)** For $H = 2000$ m, $H/\lambda = 2.5$ and $e^{-2.5} = 0.082085$:

$$\frac{m}{A} = 2650\times2000 - 712800(1 - 0.082085)
= 5\,300\,000 - 654\,289.8
= \boxed{4\,645\,710.19\ \mathrm{kg\,m^{-2}}} .$$

(Computed value: `4645710.187019115`.)

**(c)** Trapezoid results and relative errors:

| $n$ | $h$ (m) | trapezoid (kg/m²) | relative error |
|---|---|---|---|
| 10 | 200 | `4642305.972052` | `7.328e-04` |
| 20 | 100 | `4644858.468935` | `1.833e-04` |
| 40 | 50 | `4645497.215919` | `4.584e-05` |

The ratio between successive errors is `3.997`, i.e. 4.00, the $O(h^{2})$ signature.

**(d)** The trapezoid error formula is
$I - T_n = -\dfrac{(b-a)h^{2}}{12}f''(\xi)$ with $a = 0$, $b = 2000$. Here

$$f''(z) = -\frac{(\rho_g-\rho_f)\phi_0}{\lambda^{2}}e^{-z/\lambda}
= -\frac{1620\times0.55}{640000}e^{-z/800}
= -1.3922\times10^{-3}e^{-z/800} .$$

With $h = 200$ m the coefficient is
$\dfrac{2000\times200^{2}}{12} = 6.667\times10^{6}$, so the predicted error magnitude
is $6.667\times10^{6}\times1.3922\times10^{-3}e^{-\xi/800}
= 9281\,e^{-\xi/800}$.

The observed error is $\lvert 4642305.972 - 4645710.187\rvert = 3404.2$, giving

$$e^{-\xi/800} = 0.3668 \;\Longrightarrow\; \xi = 802.5\ \mathrm{m},$$

which lies in $(0, 2000)$ as the mean-value theorem requires. **The error formula is
not only an order statement; the unknown point $\xi$ is a real point of the
interval.**

---

## ★★4 — Excess mass and the ambiguity

**(a)** The excess mass is the volume integral of the density contrast:

$$M_{\text{ex}} = \int_V \Delta\rho\,dV = \Delta\rho\int_0^{R}4\pi r^{2}dr
= \frac{4}{3}\pi R^{3}\Delta\rho
= \frac{4}{3}\pi(500)^{3}(250)
= \boxed{1.309\times10^{11}\ \mathrm{kg}} .$$

(Computed value: `130899693899.57469` kg.)

**(b)** An integral over a body is a **weighted average** of the integrand. The
gravity anomaly at distance $d \gg R$ is controlled by the monopole term $GM/d^{2}$,
which contains only the total excess mass. Different density contrasts and radii that
produce the same $M_{\text{ex}}$ produce indistinguishable far-field anomalies. The
data therefore constrain the *projection* $M_{\text{ex}}$, and recovering
$\Delta\rho$ separately requires either near-field data (where the next multipole is
measurable) or an independent constraint on the body's size.

**(c)** For a uniform sphere $I/(MR^{2}) = 2/5 = 0.400000$ exactly, whatever its
size. It is therefore *useless* for this body: it is a constant of the shape, not an
observation, and it cannot be compared with anything measured about the body. For a
planet the situation is reversed: the planet's shape is known from geodesy, its mass
from orbital dynamics, and $I$ from precession and tidal response — so the observed
0.3308 is a genuine measurement that constrains the radial density distribution,
because the planet is not uniform. **The same number is informative or vacuous
depending on which quantities are independently known.**

---

## ★★★5 — Conductivity varying with depth

**(a)** With $q = k(z)\dfrac{dT}{dz} = k_0(1-\beta z)\dfrac{dT}{dz}$ held constant,

$$\frac{dT}{dz} = \frac{q}{k_0(1-\beta z)}
\;\Longrightarrow\;
T(z) = T_0 - \frac{q}{k_0\beta}\ln(1-\beta z) + C,$$

and $T(0) = T_0$ fixes $C = 0$. Check by differentiation:

$$\frac{d}{dz}\left[-\frac{q}{k_0\beta}\ln(1-\beta z)\right]
= -\frac{q}{k_0\beta}\cdot\frac{-\beta}{1-\beta z}
= \frac{q}{k_0(1-\beta z)},$$

so $k(z)\,dT/dz = k_0(1-\beta z)\cdot\dfrac{q}{k_0(1-\beta z)} = q$ $\checkmark$.

**(b)** Solve $T(z) - T_0 = 100$ K:

$$-\frac{q}{k_0\beta}\ln(1-\beta z) = 100
\;\Longrightarrow\;
\ln(1-\beta z) = -\frac{100\,k_0\beta}{q}.$$

With $q = 0.0625\ \mathrm{W\,m^{-2}}$, $k_0 = 2.5$, $\beta = 10^{-5}\ \mathrm{m^{-1}}$
(0.01 km⁻¹):

$$\frac{100\,k_0\beta}{q} = \frac{100\times2.5\times10^{-5}}{0.0625} = 0.04,$$

$$1-\beta z = e^{-0.04} = 0.960789
\;\Longrightarrow\;
z = \frac{0.039211}{10^{-5}} = \boxed{3921.1\ \mathrm{m}} .$$

For constant $k_0$ the same rise needs $z = 100k_0/q = 4000.0$ m. The variable
conductivity therefore *shortens* the depth by
$4000.0 - 3921.1 = 78.9$ m, or 2.0 %.

**(c)** The assumption doing the work is that the **flux is the same at every depth**
— no internal heat production, no advection — because only then can the varying
conductivity be converted into a varying gradient. With radiogenic heat production
$\sim1\ \mu\mathrm{W\,m^{-3}}$ in the crust, the flux at the surface differs from
that at depth by $A H \sim 3\ \mathrm{mW\,m^{-2}}$ over 3 km, which is 5 % of
$62.5\ \mathrm{mW\,m^{-2}}$ — larger than the 2 % conductivity effect under
discussion. **An effect can be computed correctly and still be irrelevant.** Check the
size of the terms you have neglected before quoting the second decimal of the terms
you have kept.

---

## ★★★6 — Means, and what they hide

**(a)** For $T(z) = T_0 + \Gamma z$,

$$\int_0^{H}T\,dz = T_0H + \frac{\Gamma H^{2}}{2}
\;\Longrightarrow\;
\bar T = T_0 + \frac{\Gamma H}{2} = \frac{T(0)+T(H)}{2},$$

so the mean value theorem holds with $c = H/2$ — the midpoint. For a linear profile
the point $c$ is *the* midpoint, and the "mean value" contains no information beyond
the endpoints.

**(b)** With $T(z) = T_0 + \Gamma z - \Delta e^{-z/\lambda}$,

$$\int_0^{H}\Delta e^{-z/\lambda}dz = \Delta\lambda\left(1 - e^{-H/\lambda}\right),$$

$$\bar T = T_0 + \frac{\Gamma H}{2} - \frac{\Delta\lambda}{H}\left(1-e^{-H/\lambda}\right).$$

The endpoint average is

$$\frac{T(0)+T(H)}{2} = T_0 + \frac{\Gamma H}{2}
- \frac{\Delta}{2}\left(1 + e^{-H/\lambda}\right),$$

and the two differ by

$$\bar T - \frac{T(0)+T(H)}{2}
= \frac{\Delta}{2}\left(1+e^{-H/\lambda}\right)
- \frac{\Delta\lambda}{H}\left(1-e^{-H/\lambda}\right) \ne 0 .$$

So the mean of a curved profile is not the average of its endpoints; the difference
is the "area" the curvature adds or removes.

**(c)** With $T_0 = 10$ °C, $\Gamma = 25\ \mathrm{K\,km^{-1}}$, $\Delta = 5$ °C,
$\lambda = 0.5$ km, $H = 3$ km: $T(0) = 5.000$ °C,
$T(H) = 10 + 75 - 5e^{-6} = 84.988$ °C. Hence

$$\bar T = 46.669\ \text{°C}, \qquad \frac{T(0)+T(H)}{2} = 44.994\ \text{°C},$$

a difference of $\boxed{1.675}$ °C (about 3.7 % of the mean).

**Why the surface gradient cannot tell them apart.** The surface heat flux is
proportional to $dT/dz$ at $z = 0$, which for this profile is
$\Gamma + \Delta/\lambda = 25 + 10 = 35\ \mathrm{K\,km^{-1}}$ — affected by the
perturbation only through the ratio $\Delta/\lambda$. Any pair $(\Delta,\lambda)$ with
the same ratio gives the same surface gradient and different means; the perturbation's
*decay scale* is invisible from the boundary. Separating them requires temperatures at
depth, which is precisely why borehole temperature profiles, not heat-flow maps, are
used to study past climate.

---

## Extension notes

- **Midpoint rule on a linear integrand.** For $T = T_0+\Gamma z$, the midpoint rule
  on a panel $[z_i, z_{i+1}]$ gives
  $h\left(T_0+\Gamma(z_i+h/2)\right) = \Gamma h^{2}/2 + \cdots$, and the sum over
  panels telescopes to the exact value: the midpoint rule is exact for linear
  integrands, since its error involves $f''$, which vanishes.
- **Two-layer Earth mass.** With $r_c = 3.480\times10^{6}$ m,
  $\rho_c = 11000$, $R = 6.371\times10^{6}$ m, $\rho_m = 4400$:

$$M = \frac{4}{3}\pi\left(\rho_c r_c^{3} + \rho_m(R^{3}-r_c^{3})\right)
= 5.9312\times10^{24}\ \mathrm{kg},$$

against the real Earth's $5.972\times10^{24}$ kg — a 0.7 % deficit, which a real
density profile closes by having a denser transition zone and a slightly denser
lower mantle. The arithmetic is identical to the numerical quadrature in the
companion script.
