# Solutions — 06-01-02 P and S Waves: Particle Motion, Speeds and Polarisation

> **Read after attempting the exercises.** Numbers were computed, not estimated;
> demonstration values are quoted directly.

Lesson: [02 P and S Waves](../02-p-and-s-waves.md).

---

## ★1 — Three forms of the ratio

With $v_p^2 = (\lambda+2\mu)/\rho$ and $v_s^2 = \mu/\rho$,

$$\frac{v_p^2}{v_s^2} = \frac{\lambda+2\mu}{\mu} = 2 + \frac{\lambda}{\mu}.$$

Substituting $\lambda = K - 2\mu/3$ gives
$\lambda/\mu + 2 = K/\mu - 2/3 + 2 = K/\mu + 4/3$. Substituting
$\lambda = 2\mu\nu/(1-2\nu)$ gives
$2 + \frac{2\nu}{1-2\nu} = \frac{2-4\nu+2\nu}{1-2\nu} = \frac{2(1-\nu)}{1-2\nu}$.

For the base model: $(5610.84/3333.33)^2 = 1.683251^2 = 2.833333$ and
$2 + \lambda/\mu = 2 + 25/30 = 2.833333$ ✔. The demonstration prints all three
columns agreeing to $10^{-6}$ or better.

---

## ★2 — The two bounds

- $v_p/v_s = \sqrt{2 + \lambda/\mu} \ge \sqrt{2}$ requires $\lambda \ge 0$, i.e.
  a positive first Lamé parameter. $\sqrt{2} = 1.414214$.
- $v_p/v_s = \sqrt{K/\mu + 4/3} \ge 2/\sqrt{3}$ requires $K \ge 0$, i.e.
  $\lambda \ge -2\mu/3$. $2/\sqrt{3} = 1.154701$.

The second is the weaker assumption and the physically necessary one: a stable
solid must have non-negative bulk modulus, but $\lambda$ may be negative. A
measurement of $v_p/v_s < \sqrt{2}$ is therefore possible in a real rock and does
**not** by itself indicate an error.

---

## ★3 — Weak shear

$$v_p = \sqrt{\frac{\lambda+2\mu}{\rho}} \to \sqrt{\frac{\lambda}{\rho}}
\quad\text{as }\mu\to0,$$
$$v_s = \sqrt{\frac{\mu}{\rho}} \to 0 .$$

For $\lambda = 25\ \mathrm{GPa}$, $\mu = 0.01\ \mathrm{GPa}$:

$$\frac{v_p}{v_s} = \sqrt{2 + \frac{25}{0.01}} = \sqrt{2502} = 50.019996,$$

which is the demonstration's first sweep endpoint. The demonstration's
weak-shear row ($v_p = 4483.30$, $v_s = 223.61\ \mathrm{m\,s^{-1}}$) corresponds
to a much smaller $\mu$, where the ratio reaches $20.049938$.

---

## ★4 — The $\mu$ sweep

At $\mu = 0.01\ \mathrm{GPa}$: $v_p/v_s = \sqrt{2 + 25/0.01} = \sqrt{2502} =
50.019996$ ✔.

At $\mu = 60\ \mathrm{GPa}$: $v_p/v_s = \sqrt{2 + 25/60} = \sqrt{2.416667}
= 1.554563$ ✔.

As $\mu \to \infty$ at fixed $\lambda$ the ratio tends to
$\sqrt{2 + 0} = \sqrt{2} = 1.414214$. The sweep's reported range therefore brackets
$\sqrt{2}$ from above and never crosses it, which is the bound of ★2 appearing as
a numerical limit.

---

## ★5 — Bulk modulus at the sweep ends

$K = \lambda + 2\mu/3$ with $\mu = 30\ \mathrm{GPa}$:

- $\lambda = -20\ \mathrm{GPa}$: $K = -20 + 20 = 0\ \mathrm{GPa}$.
- $\lambda = 200\ \mathrm{GPa}$: $K = 200 + 20 = 220\ \mathrm{GPa}$.

$K = 0$ is exactly the boundary of the admissible range: a negative $K$ means the
material expands under pressure and the wave equation loses hyperbolicity. Setting
$K = 0$ in $v_p/v_s = \sqrt{K/\mu + 4/3}$ gives $\sqrt{4/3} = 2/\sqrt{3} =
1.154701$, the demonstration's lower endpoint. The consistency is exact:
the minimum of the sweep and the theoretical bound are the same statement.

Check of the upper endpoint: $\sqrt{220/30 + 4/3} = \sqrt{7.333333 + 1.333333}
= \sqrt{8.666667} = 2.943920$ ✔.

---

## ★6 — Divergence/curl leakage and step size

In the ideal case the P field has $\nabla\times\mathbf u = 0$ and the S field has
$\nabla\cdot\mathbf u = 0$, so the ratio is $\infty$ or $0$ respectively and
$|\nabla\cdot|/|\nabla\times|$ for P is the reciprocal of the same quantity for S.
Here the S value is $4.675\times10^{-3}$, whose reciprocal is $213.9$; the measured
P value is $1.662\times10^{2} = 166.2$. They differ by about 29% because the two
fields are sampled at different wavenumbers rather than being the same field.

The leakage comes from the central-difference truncation of the derivative
operators: a second-order difference has error $O(\Delta x^2)$, so multiplying the
step by four multiplies the truncation error by 16. The leakage therefore **grows**
by roughly a factor of 16 — P's leakage increases from $1/166.2 = 6.02\times10^{-3}$
to about $9.6\times10^{-2}$, and S's from $4.675\times10^{-3}$ to about
$7.5\times10^{-2}$. In the limit of a large step the two diagnostics become
unusable and the "which field is P" test fails. That is why the demonstration
reports the leakage as an artefact of the derivative, not as physics.

---

## ★★★7 — Angle versus noise level (specification)

**Metric.** $\theta_{\text{err}} = \arccos\big(\hat{\mathbf p}\cdot
\mathbf p_{\text{true}}\big)$ in degrees, where $\hat{\mathbf p}$ is the principal
eigenvector of the $3\times3$ covariance matrix of the three traces, computed over
the analysis window.

**Range.** $\sigma \in \{0, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2\}$ in units of the
peak amplitude, at least 200 realisations per $\sigma$ using
`RNG = np.random.default_rng(20261014)`, and the same source wavelet and geometry
as the demonstration.

**Predicted form.** For small perturbations the leading eigenvector error of a
symmetric matrix is first order in the perturbation amplitude divided by the
eigenvalue gap, so $\theta_{\text{err}} \propto \sigma$ (radians) for small
$\sigma$, flattening toward the isotropic case ($\approx 57^\circ$ expected angle
for a uniformly random direction) as $\sigma$ grows past the eigenvalue gap.

**Conclusion expected.** Log-log slope $\approx 1$ over the small-$\sigma$ range;
a slope near 0.5 would indicate a squared-noise-dominated regime, which would be
evidence the estimator is not the principal-axis method claimed.

---

## ★★★8 — Poisson ratio from the speed ratio

Starting from $(v_p/v_s)^2 = 2(1-\nu)/(1-2\nu)$ and writing $R^2$ for the squared
ratio:

$$R^2(1-2\nu) = 2(1-\nu)
\Longrightarrow R^2 - 2R^2\nu = 2 - 2\nu
\Longrightarrow 2\nu(1 - R^2) = 2 - R^2,$$

$$\nu = \frac{R^2 - 2}{2(R^2 - 1)} = \frac{(v_p/v_s)^2 - 2}{2\,(v_p/v_s)^2 - 2}.$$

Using the demonstration's ratios: base $1.683251 \to \nu = 0.227273$; Poisson
$1.732051 \to \nu = 0.250000$ (exactly, as the name requires); stiff/nearly
incompressible $4.690416 \to \nu = 0.476190$; weak shear $20.049938 \to \nu =
0.498753$.

The sensitivity is the interesting part, and it runs opposite to intuition.
Since $\mathrm{d}\nu/\mathrm{d}R^2 = 1/(2(R^2-1)^2)$, a fixed *relative* error in
$R^2$ moves $\nu$ by

| model | $R^2$ | $\delta\nu$ for a 1% error in $R^2$ |
|---|---|---|
| base | 2.833 | 0.00422 |
| Poisson | 3.000 | 0.00375 |
| stiff | 22.00 | 0.00025 |
| weak shear | 402.0 | 0.00001 |

An inferred ratio near $0.5$ is therefore *precisely* determined — but for that
very reason it is **uninformative**: the mapping saturates, so rocks whose shear
moduli differ by two orders of magnitude all map into the same narrow band of
$\nu$. The value $\nu \approx 0.5$ says "nearly incompressible", and beyond that
the ratio cannot discriminate. The genuinely sensitive regime is near the lower
bound $R^2 = 2$, where a 1% error in $R^2$ moves $\nu$ by about $0.01$.

---

## ★★★9 — Why the polarisation check is weak

The check compares a recovered direction with an injected direction, both of
which are constructed in the same code from the same assumed ray geometry. If the
injected polarisation were wrong (say the ray direction were wrong), the recovered
direction would match it and the angle column would still read near zero. It tests
the covariance estimator and the sensor bookkeeping, not the physics of
polarisation.

A genuine test needs an **independent** constraint. Two are available from the
present model without new data:

1. Compare the recovered P direction with the direction of the injected
   **wavenumber vector** — a quantity built from geometry, not from the amplitudes
   that were fed into the estimator. Then the check tests whether the polarisation
   is parallel to propagation, which is the physical claim.
2. Check that the recovered S direction is perpendicular to the recovered P
   direction to within the noise level, and that the residual component (the
   out-of-plane one) is at the noise floor. This tests the *orthogonality*
   structure that isotropic elasticity requires, and would fail for a
   deliberately mis-specified medium.

Both would also be the checks that fail first in the anisotropic case of
[08 Anisotropic Propagation](../08-anisotropic-propagation.md), where the
polarisation is no longer locked to the ray — which is exactly why the isotropic
test above must be set up as an orthogonality test rather than a
parallelism-to-ray test.
