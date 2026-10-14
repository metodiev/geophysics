# Solutions — 10-05-05 Integrating Near-Surface Methods

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Teaching constants: $k_s = 3.00$, $k_w = 0.60$,
> $k_a = 0.025\ \mathrm{W\,m^{-1}\,K^{-1}}$;
> $\sigma = \sigma_w\theta^{m}$ with $m = 1.5$,
> $k = k_s^{1-\phi}k_w^{\theta}k_a^{\phi-\theta}$.

Lesson: [05 Integrating Near-Surface Methods](../05-multi-method-nearsurface.md).

---

## ★1 — Logarithmic differentiation

$$\ln\sigma = \ln\sigma_w + m\ln\theta
\;\Longrightarrow\;
\frac{\mathrm d\sigma}{\sigma} = \frac{\mathrm d\sigma_w}{\sigma_w}
+ m\frac{\mathrm d\theta}{\theta},$$

so at fixed $\sigma$,

$$\frac{\mathrm d\theta}{\theta} = -\frac{1}{m}\frac{\mathrm d\sigma_w}{\sigma_w}.$$

For $m = 2$, a 10% uncertainty in $\sigma_w$ becomes a **5%** uncertainty in
$\theta$ — but only if $\sigma$ itself is exact. With a 5% error on $\sigma$ as
well, the water-content error is
$\sqrt{(0.05)^2 + (0.05)^2} = 7.1\%$ at $m = 2$, and $8.6\%$ at $m = 1.5$. The
$1/m$ factor means **lower exponents amplify the problem**: the same pore-water
uncertainty costs more water-content uncertainty in a soil with a smaller Archie
exponent (typically a clean sand).

---

## ★2 — Thermal conductivity of a dry-ish soil

$$k = k_s^{1-\phi}k_w^{\theta}k_a^{\phi-\theta}
= 3.00^{0.60}(0.60)^{0.15}(0.025)^{0.25}$$
$$= 1.9307 \times 0.9333 \times 0.3976
= 0.7120\ \mathrm{W\,m^{-1}\,K^{-1}}.$$

Units: each factor is a conductivity in $\mathrm{W\,m^{-1}\,K^{-1}}$ raised to a
dimensionless power, so the product has the same unit ✔. Compare with the lesson's
moist case ($\phi = 0.45$, $\theta = 0.20$, $k = 0.6569$): *less* water but *more*
solid gives a **higher** conductivity, which is the whole point of the mixing
model and of the degeneracy in Section 3.5 of the lesson.

---

## ★3 — Why two methods can together

Each method's reading is a function of several parameters; one reading is one
equation in several unknowns, which leaves a set of solutions. Two methods give
two equations, and if their **sensitivities to the parameters are not
proportional** the intersection of the two solution sets is smaller than either
set. The two methods here are complementary in shape as well as in number:
electrical sensitivity to water content scales as $m/\theta$ (large when dry) and
thermal sensitivity is $k\ln(k_w/k_a)$ (large when wet). Different shapes, not just
different physics, are what make the pair informative.

---

## ★★4 — A water sample that contradicts the data

Electrical reading alone, with $\sigma_w = 0.100\ \mathrm{S\,m^{-1}}$:

$$\theta = \left(\frac{\sigma}{\sigma_w}\right)^{1/m}
= \left(\frac{0.02183}{0.100}\right)^{2/3} = 0.3626 .$$

Propagating the $\pm 0.010$ in $\sigma_w$ (and ignoring the 5% reading error for
clarity):

$$\theta = 0.3626 \quad (0.3402 \text{ to } 0.3889,\ \text{width } 0.049).$$

The thermal reading gives $\theta = 0.2043 \pm 0.0094$ (width $0.0189$). The two
intervals do not overlap: the discrepancy is

$$\frac{0.3626-0.2043}{\sqrt{0.0244^2+0.0094^2}} = \frac{0.1583}{0.0262} = 6.0\sigma .$$

**What it means.** The assumed pore-water conductivity is *excluded by the data*.
The pair of readings does not need an external value of $\sigma_w$ — it determines
one, $\sigma_w = 0.2364\ \mathrm{S\,m^{-1}}$ — and the job of the water sample is
to test that determination, not to supply it. A sample that disagrees at $6\sigma$
is evidence of either a relation that does not apply (clay surface conduction
raising $\sigma$ at low salinity), a sample that is not representative, or an
error in the thermal inversion (a wrong $k_s$ or $\phi$).

---

## ★★5 — Assuming the wrong porosity

Invert the observed $k = 0.6661\ \mathrm{W\,m^{-1}\,K^{-1}}$ twice:

| assumed $\phi$ | recovered $\theta$ | change from the $\phi = 0.45$ answer |
|---|---|---|
| 0.45 (true) | 0.2043 | — |
| 0.40 (wrong) | 0.1290 | $-37\%$ |

**Sign, explained physically.** In the mixing model the mineral and air terms
compete: $k \propto (k_s/k_a)^{1-\phi}$ at fixed $\theta$, and
$k_s/k_a = 120 \gg 1$. **Assuming less pore space therefore predicts a larger
conductivity at the same water content**, so less water is needed to explain the
measured $k$. Underestimating porosity underestimates water content — by 37%
for a 5-percentage-point error in $\phi$ in this example. That is a larger error
than either measurement's statistical uncertainty, and it is systematic: the
Monte Carlo of the lesson would not see it, because it perturbs the readings, not
the assumed constants.

---

## ★★6 — Is $(0.19, 0.30)$ inside the joint one-sigma region?

Use the Mahalanobis distance for two correlated estimates:

$$\chi^{2} = \frac{1}{1-\rho^{2}}\left[d_\theta^2 + d_{\sigma_w}^2
- 2\rho\,d_\theta d_{\sigma_w}\right],
\qquad d_i = \frac{x_i - \hat x_i}{\sigma_i},$$

with $\rho = -0.808$:

$$d_\theta = \frac{0.19-0.2042}{0.0093} = -1.53, \qquad
d_{\sigma_w} = \frac{0.30-0.2373}{0.0203} = +3.09,$$
$$\chi^{2} = \frac{2.33 + 9.54 - 2(-0.808)(-1.53)(3.09)}{1-0.653}
= \frac{2.33+9.54-7.63}{0.347} = 12.2, \qquad \sqrt{\chi^2} = 3.50 .$$

For two parameters the one-sigma contour is $\chi^2 = 2.30$, so the point is
**outside** the joint one-sigma region, at $3.5\sigma$. Note the mechanism: the
point is $1.5\sigma$ high in $\theta$ *and* $3.1\sigma$ high in $\sigma_w$ — but
because the two are anti-correlated, a high $\theta$ should pair with a *low*
$\sigma_w$, whereas this point is high in both. It is the **correlation** that
makes the pair inconsistent, not either marginal alone; assessing the two
parameters as independent would have given a different (and wrong) answer.

---

## ★★★7 — A clay-rich agricultural soil (specification)

**Methods.** Electrical conductivity (EMI at two spacings, plus a galvanic sounding
if a profile is needed) for the pore-water term; thermal conductivity from a probe
(the only *calibration* measurement that is in situ and cheap) for the geometry
term; and seismic $v_s$ (surface waves) because it responds to the frame rather
than to the fluid, which is what a clay-rich soil changes most.

**Depth requirement.** Water content at $1\ \mathrm{m}$ is the deliverable, so the
electrical method must have a weight function reaching $1\ \mathrm{m}$, and the
thermal probe and the surface-wave array must be able to reach it. State the
weights explicitly (the lesson's EMI table) rather than assuming the reading
belongs to the target depth.

**Calibrations and constants.** For each number carried in the inversion, name its
source: porosity and $k_s$ from cores at two or three sites; $m$ from a
saturation series on the same cores; clay content from a laboratory measurement or
from gamma spectrometry. A calibration curve from *another* soil is an assumption
and must be labelled as one.

**Metric.** Volumetric water content with its admissible set and the
$\theta$–$\sigma_w$ correlation, reported per station; plus the misfit of the
joint inversion against the stated measurement errors (a $\chi^2$ per degree of
freedom near 1 means the errors are honest).

**Falsification test.** Hold out one calibration site and predict its water content
from the geophysics alone. If the prediction misses by more than the stated
uncertainty at more than about $5\%$ of the stations, the assumed constants do not
transfer and the reported uncertainty is too small.

**What the design cannot test.** Whether the relation form is right. A
saturation-series calibration validates $m$ *given* the chosen functional form; if
the true relation includes a clay surface-conduction term independent of
$\sigma_w$, a single-site calibration will absorb it into $m$ and the survey will
fail silently at a different clay content. Only a multi-site calibration series
spanning the clay range can detect that.

---

## ★★★8 — Adding seismic $v_s$: the sensitivity vectors

Write the two parameters as $\mathbf p = (\theta, \phi)$ and take plausible
teaching forms:

$$\sigma = \sigma_w\theta^{m}, \qquad
k = k_s^{1-\phi}k_w^{\theta}k_a^{\phi-\theta}, \qquad
v_s = v_{s0}\,(1 - a\phi)\,(1 + b\theta),$$

the last being a linearised frame-softening plus fluid-stiffening form with
teaching coefficients $a = 0.5$, $b = 0.3$. The **logarithmic sensitivity
vectors** at the truth $(\theta,\phi) = (0.20, 0.45)$ are

$$\mathbf s_\sigma = \left(\frac{m}{\theta}, 0\right) = (7.50, 0),$$
$$\mathbf s_k = \left(\ln\frac{k_w}{k_a}, \ln\frac{k_a}{k_s}\right)
= (3.18, -4.79),$$
$$\mathbf s_{v_s} = \left(\frac{b}{1+b\theta}, \frac{-a}{1-a\phi}\right)
= (0.283, -0.645).$$

**Is the third vector independent?** $\mathbf s_{v_s}$ is *parallel* to
$(\frac{b}{1+b\theta})/\mathbf{...}$ — compare the ratios of the two components:
$\mathbf s_k$ has ratio $-4.79/3.18 = -1.51$ and $\mathbf s_{v_s}$ has ratio
$-0.645/0.283 = -2.28$. They are not parallel (a 51% difference in ratio), so the
third measurement **does add rank**. In two dimensions, however, the rank is
already 2: adding a third row cannot increase the rank of a $2\times3$ sensitivity
matrix, so what the third method buys is not rank but **redundancy** — it lets the
degeneracy be tested rather than assumed, and it reduces the variance of the joint
estimate along the previously poorly constrained direction.

**The honest conclusion.** With two parameters and two methods the system is
already full rank, so the residual degeneracy of the lesson's Section 3.5 is not a
rank deficiency at all — it is the *material* ambiguity (a different $\phi$ and
$k_s$ with a different $\theta$). A third method only helps if a *third* parameter
is also fitted (say clay content), which is exactly the situation in the clay-rich
soil of ★7. **Adding measurements does not remove the need to know the material;
it changes which material parameters are being traded.**
