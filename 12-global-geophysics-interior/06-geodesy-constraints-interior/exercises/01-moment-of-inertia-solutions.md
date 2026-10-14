# Solutions — 12-06-01 Moment of Inertia, Figure and Interior Constraints

> **Read after attempting the exercises.** Several problems have more than one
> defensible answer; where that is true it is said so. Numbers were computed, not
> estimated by hand.

Lesson: [01 Moment of Inertia, Figure and Interior Constraints](../01-moment-of-inertia.md).

---

## ★1 — Two-layer moment of inertia

With $x = 0.25$: $x^{3} = 0.015625$ and $x^{5} = 9.7656\times10^{-4}$, so

$$
m_{c} = \alpha x^{3} = 1.5\times0.015625 = 0.0234375,\qquad
m_{m} = 1 - x^{3} = 0.984375,\qquad M = 1.0078125,
$$

$$
\frac{1-x^{5}}{1-x^{3}} = \frac{0.9990234}{0.984375} = 1.014881.
$$

$$
C = 0.4\,m_{c}x^{2} + 0.4\,m_{m}\frac{1-x^{5}}{1-x^{3}}
= 0.4(0.0234375)(0.0625) + 0.4(0.984375)(1.014881)
= 0.0005859 + 0.399610 = 0.400196,
$$

$$
\frac{C}{MR^{2}} = \frac{0.400196}{1.0078125} = 0.39709 .
$$

The mantle term dominates by nearly three orders of magnitude: the core's
contribution is $0.0006$ against $0.3996$. A small core matters to $C/MR^{2}$ only
through the mass it removes from the mantle, not through its own inertia.

---

## ★2 — Uniform sphere

$\mathrm{d}m = 4\pi\rho r^{2}\,\mathrm{d}r$ and the shell contribution is
$\tfrac{2}{3}r^{2}\,\mathrm{d}m$, so

$$
C = \int_{0}^{R}\frac{2}{3}r^{2}\,4\pi\rho r^{2}\,\mathrm{d}r
= \frac{8\pi\rho}{3}\int_{0}^{R}r^{4}\,\mathrm{d}r
= \frac{8\pi\rho R^{5}}{15}.
$$

With $M = \tfrac{4}{3}\pi\rho R^{3}$,

$$
\frac{C}{MR^{2}} = \frac{8\pi\rho R^{5}/15}{\tfrac{4}{3}\pi\rho R^{3}\cdot R^{2}}
= \frac{8\pi/15}{\tfrac43\pi} = \frac{8}{15}\times\frac{3}{4} = \frac{2}{5} .
$$

**Units.** $\rho\,r^{4}\,\mathrm{d}r$ has
$\mathrm{kg\,m^{-3}\cdot m^{4}\cdot m} = \mathrm{kg\,m^{2}}$, which is a moment of
inertia; dividing by $MR^{2}$ (kg m²) gives a pure number. ✔

---

## ★3 — Shell factor

At $x = 0.5$: $x^{3} = 0.125$, $x^{5} = 0.03125$, so
$(1-0.03125)/(1-0.125) = 0.96875/0.875 = 1.107143$.

At $x = 0.9$: $x^{3} = 0.729$, $x^{5} = 0.59049$, so
$(1-0.59049)/(1-0.729) = 0.40951/0.271 = 1.511107$.

As $x\to1$ both numerator and denominator vanish; l'Hôpital gives
$5x^{4}/(3x^{2}) = (5/3)x^{2}\to5/3$. Physically the shell becomes infinitely thin
and the body approaches a thin shell, for which $C = \tfrac23 MR^{2}$; the factor
multiplying $\tfrac{2}{5}m_{m}R^{2}$ is therefore $\tfrac23/\tfrac25 = 5/3$. ✔

---

## ★4 — Core densities on the ridge

Mean density: $\rho_{\text{mean}} = M/(\tfrac43\pi R^{3})$.

$$
R^{3} = (3.0\times10^{6})^{3} = 2.7\times10^{19}\ \mathrm{m^{3}},\qquad
\tfrac43\pi R^{3} = 1.1310\times10^{20}\ \mathrm{m^{3}},
$$

$$
\rho_{\text{mean}} = \frac{4.0\times10^{24}}{1.1310\times10^{20}}
= 3.537\times10^{4}\ \mathrm{kg\,m^{-3}} .
$$

The volume fractions are $f_{c} = 0.45^{3} = 0.091125$ and
$f_{m} = 0.908875$, and the density is
$\rho_{\text{mean}} = f_{c}\rho_{c} + f_{m}\rho_{m}$ with
$\rho_{c} = 3.8083\rho_{m}$:

$$
\rho_{m} = \frac{3.537\times10^{4}}{0.908875 + 0.091125\times3.8083}
= \frac{3.537\times10^{4}}{1.25594} = 2.8161\times10^{4}\ \mathrm{kg\,m^{-3}},
\qquad
\rho_{c} = 1.0725\times10^{5}\ \mathrm{kg\,m^{-3}} .
$$

Both values are *high* for a planetary interior: the core density is more than
three times the mean. The row is therefore admissible arithmetically but
questionable physically, which is exactly how mineral physics narrows the ridge
(the lesson's §4 makes the same point for $x = 0.10$, where
$\rho_{c} = 5.8\times10^{5}\ \mathrm{kg\,m^{-3}}$).

---

## ★5 — Ellipticity, wobble and sensitivity

$$
H = \frac{J_{2}}{C/MR^{2}} = \frac{0.005}{0.335} = 1.4925\times10^{-2},
$$

and the rigid-body inertial free-wobble period is

$$
T = \frac{1}{H} = 67.0\ \text{sidereal days}.
$$

(The body-frame period is $(1-H)/H = 66.0$ sidereal days; the difference is the
$H$ correction discussed in lesson 03.)

With $C/MR^{2}$ 2% larger, $H = 0.005/0.3417 = 1.4633\times10^{-2}$ and
$T = 68.3$ sidereal days: a 2% change. The period is linear in $H$, hence linear
in $J_{2}$ and inversely linear in $C/MR^{2}$: **the wobble period is equally
sensitive to both**, which is why the pair must be quoted together.

---

## ★6 — First-order figure error

At $q = 4\times10^{-3}$:

$$
\text{error} = \frac{1.2500 - 1.2451}{1.2451} = 3.9\times10^{-3} = 0.39\% .
$$

At $q = 3\times10^{-2}$:

$$
\text{error} = \frac{1.2500 - 1.2144}{1.2144} = 2.9\times10^{-2} = 2.9\% .
$$

The error grows roughly as $q$ (second order in the deformation, first order in
$q$ relative to the leading term): it is negligible at slow rotation and
material at fast rotation. Rule of thumb from these two points: the first-order
formula is good to about 0.4% at $q = 4\times10^{-3}$ and 3% at
$q = 3\times10^{-2}$, i.e. the fractional error is $\approx q$.

---

## ★7 — Specification (no single unique answer)

**What 0.5% in $C/MR^{2}$ does.** It confines the model to a *band* around the
ridge. From the lesson's ridge table, adjacent rows differ in $C/MR^{2}$ by more
than 0.5% only for large changes in $x$; but all rows are on the ridge by
construction, so the band is a band in $(x,\alpha)$ and the core radius is still
undetermined at the level of the ridge spacing.

**What to add.** A figure observable: the fluid Love number $k_{f} = 3J_{2}/q$
(lesson [01-terrestrial-planets-interiors](../../07-planetary-interiors-comparative/01-terrestrial-planets-interiors.md)
§5 shows the mechanics). Along the ridge of that lesson, $k_{f}$ varies from
$0.9922$ at $x = 0.20$ to $0.9607$ at $x = 0.60$ — a 3% span for a factor 3 in
core radius. To resolve a factor-2 change in $x$ one therefore needs $k_{f}$ to
about 1 to 2%, which for a body with a measurable $J_{2}$ and a known $q$ means
measuring $J_{2}$ to about 1%.

**The assumption that remains.** $k_{f}$ is a *hydrostatic* quantity. If part of
the observed $J_{2}$ is fossil (or dynamically supported), the inferred $k_{f}$
is contaminated and the core-radius inference inherits the error. Any
specification that omits this sentence is incomplete.

---

## ★8 — The exact identity and its error propagation

From the definitions:

$$
H = \frac{C-A}{C} = \frac{C-A}{MR^{2}}\cdot\frac{MR^{2}}{C}
= J_{2}\cdot\frac{1}{C/MR^{2}} .
$$

Logarithmic differentiation gives

$$
\frac{\delta H}{H} = \frac{\delta J_{2}}{J_{2}}
- \frac{\delta(C/MR^{2})}{C/MR^{2}},
$$

so for independent errors the variances add in quadrature:

$$
\frac{\sigma_{H}}{H} = \sqrt{(0.01)^{2} + (0.02)^{2}} = \sqrt{0.0001+0.0004}
= 0.0224 = 2.2\% .
$$

If instead $J_{2}$ were known to 0.01%, then
$\sigma_{H}/H = \sqrt{(0.0001)^{2}+(0.02)^{2}} \approx 2.0\%$: the inertia factor
is the limiting term, and improving the gravity field alone would buy nothing. An
observed $H$ at 0.1% would, with the same $J_{2}$ precision, require and imply
$C/MR^{2}$ to about 0.1% — at which point the *parameterisation* of the density
profile, not the measurement, becomes the limiting uncertainty.
