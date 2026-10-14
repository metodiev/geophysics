# Solutions — 07-03-02 Analytical Formulas for Sphere, Cylinder, Sheet and Dyke

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [02 Analytical Formulas](../02-simple-body-formulas.md).

---

## ★1 — Infinite sheet

$$g_z = 2\pi G\Delta\rho t
= 2\pi(6.67430\times10^{-11})(250)(100)
= 1.0484\times10^{-5}\ \mathrm{m\,s^{-2}}
= \mathbf{1.0484\ mGal}.$$

Independent of depth and of position, as the formula requires.

---

## ★2 — Dimensions of the 2-D kernel

$z'$ is a length; $u^{2}+z'^{2}$ is a length squared; so the kernel has
dimensions $\mathrm{m/m^{2}} = \mathrm{m^{-1}}$. The area integral gives
$\mathrm{m^{-1}}\times\mathrm{m^{2}} = \mathrm{m}$. Then

$$[2G\Delta\rho\times\text{length}]
= \left[\mathrm{m^{3}kg^{-1}s^{-2}}\right]\left[\mathrm{kg\,m^{-3}}\right]
\left[\mathrm{m}\right] = \mathrm{m\,s^{-2}}. ✔$$

The same check applied to the 3-D volume integral gives
$\mathrm{m^{-2}}\times\mathrm{m^{3}} = \mathrm{m}$, i.e. the same acceleration —
but with no factor of 2. The factor of two is purely the reduction of the volume
integral to an area integral along an infinite strike.

---

## ★3 — Semi-infinite sheet at the edge

$g_z(0) = 2G\Delta\rho\left[\tfrac{\pi}{2}(z_2-z_1)\right] = \pi G\Delta\rho t$,
which is **exactly half** the slab value $2\pi G\Delta\rho t$. The thickness
appears in both and cancels in the ratio, so the 50% point sits over the edge
whatever the thickness — a property the demonstration verifies numerically
($1.25808\ \mathrm{mGal}$ against half of $2.51615\ \mathrm{mGal}$).

---

## ★4 — Derivative of the semi-infinite sheet

$$\frac{\mathrm{d}g_z}{\mathrm{d}x}
= 2G\Delta\rho\left[
z_2\frac{1/z_2}{1+(x/z_2)^{2}}
- z_1\frac{1/z_1}{1+(x/z_1)^{2}}
+ \tfrac{1}{2}\ln\frac{x^{2}+z_2^{2}}{x^{2}+z_1^{2}}
+ \tfrac{x}{2}\left(\frac{2x}{x^{2}+z_2^{2}}-\frac{2x}{x^{2}+z_1^{2}}\right)
\right].$$

The first two terms collapse to
$\frac{z_2^{2}}{x^{2}+z_2^{2}} - \frac{z_1^{2}}{x^{2}+z_1^{2}}$; the last two give
$\tfrac{1}{2}\ln\frac{x^{2}+z_2^{2}}{x^{2}+z_1^{2}}
+ x^{2}\left(\frac{1}{x^{2}+z_2^{2}}-\frac{1}{x^{2}+z_1^{2}}\right)$. At $x = 0$
the logs vanish, and the remaining terms are $1-1 = 0$: **the derivative is zero
at the edge, as required by symmetry of the two half-planes about the edge**.
Writing $s = x^{2}$ and expanding for small $s$ shows the logarithmic term is
second order in $x$ while the algebra gives
$\frac{z_2^{2}-z_1^{2}}{z_1^{2}z_2^{2}}s + O(s^{2})$ — the derivative therefore
rises quadratically away from zero in both directions, so $x = 0$ is a maximum of
$\left|\mathrm{d}g/\mathrm{d}x\right|$, with value

$$\left(\frac{\mathrm{d}g_z}{\mathrm{d}x}\right)_{x=0}
= 2G\Delta\rho\ln\frac{z_2}{z_1},$$

which is the rule used in the lesson to recover the top depth. For
$z_1 = 500$, $z_2 = 700$, $\Delta\rho = 300$:
$\ln(700/500) = 0.33647$ and the derivative is
$2G\Delta\rho\times0.33647 = 1.35\times10^{-8}\ \mathrm{m\,s^{-2}\,m^{-1}}
= 1.3\times10^{-3}\ \mathrm{mGal\,m^{-1}}$, matching the demonstration's printed
$0.0013\ \mathrm{mGal/m}$.

---

## ★5 — $800\ \mathrm{m}$-wide dyke, $400$–$4000\ \mathrm{m}$ depth

Closed form (§2.5 of the lesson) evaluated numerically:

- at $x = 0$: $g_z = \mathbf{8.1191\ mGal}$;
- at $x = 2000\ \mathrm{m}$: $g_z = \mathbf{2.9597\ mGal}$;
- infinite slab for the same $3600\ \mathrm{m}$ thickness:
  $2\pi G\Delta\rho t = 2\pi(6.67430\times10^{-11})(350)(3600)
  = 52.8392\ \mathrm{mGal}$.

The narrow dyke reaches only $8.12/52.84 = 15.4\%$ of the slab.
**The slab formula is not a good approximation for a body whose width is smaller
than its depth extent.**

---

## ★6 — A $200\ \mathrm{m}$-wide dyke

At $x = 0$: $g_z = \mathbf{2.1421\ mGal}$, i.e. $4.05\%$ of the slab. The narrower
body is a proportionally smaller fraction, confirming that the slab value is a
limit of *width*, not of thickness: the fraction scales with the solid angle the
body subtends, and halving the width roughly halves the fraction.

---

## ★7 — Deriving $J(u)$ and the slab limit

Inner integral over depth:

$$\int_{z_1}^{z_2}\frac{z'}{u^{2}+z'^{2}}\,\mathrm{d}z'
= \tfrac{1}{2}\ln\frac{u^{2}+z_2^{2}}{u^{2}+z_1^{2}}.$$

Integrating that over $u$, using
$\int\ln(u^{2}+a^{2})\,\mathrm{d}u = u\ln(u^{2}+a^{2}) - 2u + 2a\arctan(u/a)
\equiv P(u,a)$:

$$J(u) = \int \tfrac{1}{2}\left[\ln(u^{2}+z_2^{2}) - \ln(u^{2}+z_1^{2})\right]\mathrm{d}u
= \tfrac{1}{2}\left[P(u,z_2) - P(u,z_1)\right],$$

and $J'(u) = \tfrac{1}{2}\left[\ln(u^{2}+z_2^{2})-\ln(u^{2}+z_1^{2})\right]$ ✔.

**Slab limit.** As $u\to\pm\infty$,
$P(u,z_2)-P(u,z_1) \to \pm\pi(z_2-z_1)$: differentiating, the log terms cancel to
order $u^{-2}$, and the arctangents give $\pm\pi(z_2-z_1)$. Hence
$J(+\infty) = \tfrac{\pi}{2}(z_2-z_1)$ and
$J(-\infty) = -\tfrac{\pi}{2}(z_2-z_1)$, and the closed form gives

$$g_z = 2G\Delta\rho\left[J(+\infty)-J(-\infty)\right]
= 2G\Delta\rho\pi(z_2-z_1) = 2\pi G\Delta\rho t,$$

which is the slab value ✔. The full derivation therefore contains the slab as a
limit, which is the strongest available verification of the closed form.

---

## ★8 — When is the slab a legitimate approximation?

For a rectangle of half-width $w$ at depth $z$ the deficit from the slab behaves
as $O(z/w)$ for $w \gg z$. Using the demonstration's data point — a $200\
\mathrm{m}$-thick body at $500\!-\!700\ \mathrm{m}$ depth, $2\ \mathrm{km}$ wide,
reaching $99.9618\%$ of the slab — the empirical rule is

$$\text{error} \approx \frac{z_{\text{mean}}}{w}\times 5\% ,$$

so a $1\%$ accuracy requires $w \gtrsim 5 z_{\text{mean}}$, and $0.1\%$ requires
$w \gtrsim 50 z_{\text{mean}}$. For the case here
($z_{\text{mean}} = 600\ \mathrm{m}$) a $1\%$ slab reduction needs the sheet to
extend about $3\ \mathrm{km}$ from the station in every direction, and a $0.1\%$
reduction over $30\ \mathrm{km}$. **The rule for a survey:** the extent of a
gravity survey must exceed several times the depth of the deepest body whose
Bouguer slab term you intend to trust.
