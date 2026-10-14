# Solutions — 06-01-06 Interface Waves, Head Waves and the Total Wavefield

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [06 Interface Waves, Head Waves and the Total
Wavefield](../06-interface-waves.md).

---

## ★1 — Head-wave geometry

$$\sin\theta_c = \frac{v_1}{v_2} = \frac{1500}{3000} = 0.5
\;\Longrightarrow\; \theta_c = 30.000000^\circ,\qquad
\cos\theta_c = 0.8660254 .$$

Intercept time:

$$t_i = \frac{2H\cos\theta_c}{v_1}
= \frac{2 \times 20\ \mathrm{m} \times 0.8660254}{1500\ \mathrm{m\,s^{-1}}}
= \frac{34.641016\ \mathrm{m}}{1500\ \mathrm{m\,s^{-1}}}
= 0.023094011\ \mathrm{s} = 23.094011\ \mathrm{ms}.$$

Crossover distance:

$$x_{\text{cross}} = \frac{t_iv_1v_2}{v_2 - v_1}
= \frac{0.023094011 \times 1500 \times 3000}{1500}
= 69.2820\ \mathrm{m}.$$

Units: $H\cos\theta_c$ is a length (m); divided by $v_1$ gives s. In the crossover
expression, $\mathrm{s}\times\mathrm{m\,s^{-1}}\times\mathrm{m\,s^{-1}}/
\mathrm{m\,s^{-1}} = \mathrm{m}$ ✔. All three values match the demonstration.

---

## ★2 — Inverting an intercept time

The apparent velocity of a head wave is the velocity of the **lower** medium, so
$v_2 = 2500\ \mathrm{m\,s^{-1}}$.

$$\cos\theta_c = \sqrt{1 - (v_1/v_2)^{2}} = \sqrt{1 - 0.36} = 0.8,$$

$$H = \frac{t_iv_1}{2\cos\theta_c} = \frac{0.015 \times 1500}{2 \times 0.8}
= \frac{22.5}{1.6} = 14.0625\ \mathrm{m}.$$

The apparent velocity measures $v_2$, the lower-medium speed — *not* an average
speed of the two layers and not the interface property. That is why refraction
profiles are read as a velocity-versus-depth function of the refractors.

---

## ★3 — Existence condition

$$\sin\theta_c = \frac{v_1}{v_2} \le 1 \;\Longrightarrow\; v_2 \ge v_1,
\quad\text{strictly } v_2 > v_1 \text{ for a distinct arrival}.$$

When $v_2 < v_1$ there is no incidence angle whose transmitted ray runs along the
interface, the branch-point contribution leaves the real slowness axis, and no
head wave is generated. The faster layer is then **hidden**: a travel-time curve
shows only the direct arrival from the top layer and, if the deeper medium is
reached at all, arrivals from further down, so a joint inversion that assumes
monotonic velocity increase will misplace both $H$ and $v_2$.

---

## ★4 — Measured convergence order

Consecutive ratios at $x = 400\ \mathrm{m}$:

$$\frac{2.733\times10^{-2}}{1.777\times10^{-2}} = 1.538,
\qquad
\frac{1.777\times10^{-2}}{1.299\times10^{-2}} = 1.368 .$$

A factor 1.538 per halving of $\Delta x$ means the error behaves as
$\Delta x^{m}$ with $2^{m} = 1.538$, so

$$m = \frac{\ln 1.538}{\ln 2} = 0.62,
\qquad m = \frac{\ln 1.368}{\ln 2} = 0.45 .$$

The measured order is therefore about **0.5**, not 2. A second-order scheme would
show a factor of 4 per halving (an order of 2.0). The cause is the 8-neighbour
stencil: it measures a staircase path, so the error is dominated by the
*geometry* of the stencil, which improves only as $\Delta x^{1/2}$ because the
staircase deviation scales as the square root of the number of steps in this
setting. Refining the grid with the same stencil cannot recover second order;
a 16-neighbour stencil or an eikonal/fast-marching solver would be needed.

---

## ★5 — The trapped-mode bound and the measured lower limit

**Derivation.** A trapped mode must decay away from the contact on both sides, so
the vertical decay constants must be real:

$$\alpha_1^2 = k^2\left(1 - \frac{c^2}{\alpha_{v1}^2}\right) > 0,\qquad
\beta_1^2 = k^2\left(1 - \frac{c^2}{\beta_{v1}^2}\right) > 0,$$

and likewise in medium 2. Since $\beta_v < \alpha_v$ in any elastic solid, the
binding constraint from each medium is $c < \beta_{vi}$, so
$0 < c < \min(\beta_{v1},\beta_{v2})$.

**Why a lower bound at $0.980676$ is informative.** The mathematical interval
allows $c$ anywhere in $(0,\min\beta_v)$, but the *solutions* found by the scan sit
within 2% of the smaller shear speed. The measured lower bound says how far the
mode's speed can drop below the shear speed for the contrasts scanned: at most
about 1.9%. Practically, that means the arrival is nearly coincident with the
direct S arrival at short offset and will be separated only at offsets where
differential moveout exceeds a wavelength — a *statement about separability*,
which is what an interpreter needs, and which the abstract inequality does not
supply.

---

## ★6 — What the singular-value test measures

For a homogeneous linear system $\mathbf M\mathbf v = \mathbf 0$, a nonzero
solution exists iff $\mathbf M$ is rank-deficient, i.e. iff its smallest singular
value is zero. The reported ratio
$\sigma_{\min}/\sigma_{\max} = 5.916\times10^{-16}$ is the numerical realisation of
that condition: the matrix has a null vector to machine precision.

A sign change of the determinant only says the determinant *crossed zero*
somewhere in the bracketing interval; on a coarse scan it can be produced by a
pole, by an interval containing two roots, or by a continuously small
determinant. The rank test is stronger because it certifies the actual condition
for a mode.

The contrast between the two numbers:

$$\frac{1.542\times10^{-1}}{5.916\times10^{-16}} = 2.6\times10^{14},$$

i.e. the matrix is about fourteen orders of magnitude better conditioned away
from the root. A near-miss model would show a small but non-negligible ratio
(say $10^{-3}$) at the candidate speed; this one does not.

---

## ★★★7 — Locating the density-ratio boundary (specification)

**Fixed:** $v_{p1} = 5000$, $v_{s1} = 2900$, $\rho_1 = 2600\
\mathrm{kg\,m^{-3}}$ (the demonstration's medium 1), $v_{s2}/v_{s1} = 1.00$
(hence $v_{p2}$ fixed by the same $v_p/v_s$ ratio), and $c$ scanned on
$0 < c < \min(v_s)$.

**Scan range:** $\rho_2/\rho_1 \in [0.10, 1.00]$ on a log-spaced grid of at least
400 points, since the interesting structure sits at low density ratio.

**Root finding:** for each density ratio, evaluate $\det\mathbf M(c)$ on at least
2000 values of $c/\min(v_s) \in (0,1)$ and bracket sign changes; refine each
bracket by bisection to $10^{-10}\ \mathrm{km\,s^{-1}}$ in $c$; require the
refined smallest/largest singular-value ratio to be below $10^{-10}$ before
accepting the root.

**Resolution and reported quantity:** report the *interval* of density ratios over
which a root is found, plus, for each root, the pair
$(c/\min(v_s),\ \sigma_{\min}/\sigma_{\max})$. Report the smallest density ratio
with a root as a bracket $[\rho_{\text{lo}},\rho_{\text{hi}}]$ whose width is the
grid spacing, and state that width explicitly. A single number without a bracket
would misrepresent a sign-change search.

---

## ★★★8 — Measuring head-wave amplitude decay (specification)

**Experiment.** Place a line source at the surface of the two-layer model and
compute the full field with a spectral-element or finite-difference solver on a
grid with at least 10 points per minimum wavelength. Record on the surface at
offsets $x$ well beyond $x_{\text{cross}}$, window the head-wave arrival using the
analytic time $t = x/v_2 + t_i$ widened by one source period, and measure its
peak amplitude.

**Fit.** Fit $\ln A$ against $\ln x$ over a decade of offsets:

$$\ln A = a + m\ln x .$$

**Expected form.** For a line (2-D) source the head wave is weaker than the direct
wave and decays with a larger negative exponent; the asymptotic theory predicts a
specific $m$ for the 2-D case. The measurement should be reported as the fitted
$m$ with its standard error, and compared with the asymptotic value rather than
asserted to equal it.

**Assumption the asymptotic result needs.** Asymptotic ray theory assumes the
interface is locally straight and the observation point is far enough that the
branch-line integral is dominated by its endpoint contribution. A purely numerical
experiment needs none of that, but it *cannot* isolate the head-wave branch from
the near-field and the downgoing reflection without a separation argument — so it
measures the total field, not the branch contribution. This is exactly why the
lesson quotes times and declines to quote amplitudes.

---

## ★★★9 — What "no root found" proves

**Proves:** for the five density ratios tested, at the stated grid resolution in
$c$ and with the stated determinant scan, no sign change of $\det\mathbf M(c)$ was
detected on the admissible interval. That is a statement about the *scan*.

**Does not prove:** that no trapped mode exists for $v_{s2}/v_{s1} = 0.60$ at any
density ratio. Reasons: (i) the five density ratios are a coarse subset of a
continuous parameter; (ii) a determinant that touches zero without changing sign
(an even-order root) is invisible to a sign-change test; (iii) a mode whose
determinant is very small over a wide interval could be missed by any coarse grid.

**The single numerical change.** Replace the sign-change test by a **minimisation
of the smallest singular value** of the row-normalised matrix over $c$, and accept
a mode only when $\sigma_{\min}/\sigma_{\max} < 10^{-10}$ at the minimum. That
converts "no sign change was seen" into "the smallest singular value stays above
$10^{-10}$ everywhere on the interval", which is a genuine exclusion for the
scanned interval — and it still leaves the density-ratio grid resolution to be
declared, because that is a separate limitation.
