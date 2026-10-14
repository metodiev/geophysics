# Solutions — 09-05-02 FEM Conductivity Mapping and Apparent Conductivity

> **Read after attempting.** Lesson:
> [02 FEM Conductivity Mapping](../02-fem-conductivity-mapping.md).

---

## ★1 — Induction number

$$\theta = \frac{2\pi\times2.5\times10^{4} \times 4\pi\times10^{-7}
\times 0.02 \times 100}{4}
= \frac{1.5708\times10^{5} \times 1.2566\times10^{-6} \times 2}{4}
= 0.0987 .$$

The measured error table gives $-0.00\%$ at $\theta = 0.01$ and $-44.05\%$ at
$\theta = 0.10$, so an interpolation puts the LIN error near $-43\%$ at
$\theta = 0.0987$: **the calibration does not apply.**

---

## ★2 — Reading the response table

At $100$ Hz, $\sigma = 0.05$ S/m, $r = 20$ m the printed quadrature is
$-3570.75$ ppm, i.e. $-3570.75\times10^{-6} = -3.571\times10^{-3}$ of the primary
field. The negative sign is the secondary-field convention (total minus primary);
only the magnitude is used in the conductivity calibration.

---

## ★3 — Why the quadrature

The quadrature is first order in the induction number and hence first order in
conductivity, so a single multiplicative factor converts it into a conductivity
over a wide range. The in-phase response is second order (measured exponent
$1.47$ over a range that already includes the end of the LIN regime), so at small
induction numbers it is quadratic in conductivity and its own variation is
smaller than the quadrature's by a factor of order $\theta$ — it is insensitive
precisely where the calibration is used.

---

## ★4 — Channel ratio at $\theta = 10^{-3}$

$$\frac{\text{in-phase}}{\text{quadrature}}
\approx \frac{\theta^{1.4723}}{\theta^{0.9701}} = \theta^{0.5022}
= 10^{-3\times0.5022} = 0.0315 .$$

So at $\theta = 10^{-3}$ the in-phase channel is about $3\%$ of the quadrature:
with a $1\%$ relative noise level the in-phase is measurable, but its *variation*
with conductivity is $1.47$ times the relative variation of $\theta$ rather than
$0.97$ times, so per unit of conductivity change it carries comparable
information — at the cost of a much smaller signal. Mappers therefore use the
quadrature for conductivity and the in-phase as a check against
non-LIN conditions.

---

## ★5 — Where the LIN error reaches $10\%$

Linear interpolation between $(0.01, 0.00)$ and $(0.10, -44.05)$ gives

$$\theta_{10\%} \approx 0.01 + 0.09\times\frac{10}{44.05} = 0.0304 .$$

For $r = 20$ m and $f = 1000$ Hz,

$$\sigma_{\max} = \frac{4\theta_{10\%}}{\omega\mu_0r^{2}}
= \frac{4\times0.0304}{6283.2 \times 1.2566\times10^{-6}\times400}
= \frac{0.1216}{3.158} = 0.0385\ \mathrm{S/m}.$$

So an instrument at these settings reports a calibrated conductivity only up to
about $0.04$ S/m ($25\ \Omega$ m); beyond that the LIN calibration is wrong by
more than $10\%$.

---

## ★6 — Two apparent conductivities

The measured equivalence band for the four fortyfold-different grounds spans
$0.0211$ to $0.0361$ S/m. Both numbers lie inside that band, so a single-frequency
survey can conclude: "the ground at these two stations differs by a factor $1.7$ in
its conductance-like average, at the depth range this separation and frequency
sample". It **cannot** conclude anything about the thickness or the conductivity
of a layer at either station, because the same band contains grounds differing by
a factor $40$ in both.

---

## ★7 — Two separations (specification)

**Separations.** $20$ m and $80$ m at the same frequency. The measured depths of
exploration are $13.19$ m and $31.89$ m, so the two data average over overlapping
but different kernels — exactly what is needed to separate a conductance from a
thickness.

**Model and statistic.** Fit a two-layer model (conductivity and thickness of the
top layer) to the two quadratures jointly and compare with the single-layer
alternative by an $F$-test on the residual: require $\Delta\chi^{2} > 9$ for the
extra parameter (about $3\sigma$).

**Noise level.** The measured spread within the equivalence family is up to
$71\%$ at one separation, so a $3\sigma$ discrimination needs a repeatability of
roughly $71/(3\sqrt{2}) \approx 17\%$ — attainable with careful field procedure
and repeat readings, and the reason multi-separation acquisition is standard
practice rather than a refinement.

---

## ★8 — An alternative depth-of-exploration definition

**Alternative.** Define the depth of exploration as the *median* of the
normalised sensitivity kernel $K(z) = \partial |H_s|/\partial\ln\sigma(z)$
evaluated for a thin layer, i.e. the depth below which half of the kernel's
integral lies. This is the standard "half-space sensitivity" rule and it is
defined for any model, not only a half-space.

**Why it may be preferable.** The cumulative $10\%$-scaling definition of the
lesson depends on the *magnitude* of the perturbation and saturates when the
perturbation becomes large (the measured saturation column moves from $9.68\%$ to
$7.92\%$), so a layered ground can move the answer through saturation rather than
through physics. The kernel definition is linear and additive, so kernels for
different layers can be compared directly.

**Predicted change.** The measured depths would fall, because the cumulative
definition integrates the kernel's tail (which extends deeper) while the median
is by construction half of it; the ordering with separation would be preserved,
and the measured exponent $p$ in $z \propto \delta^{p}$ would rise slightly
because the kernel's median tracks the diffusion depth more closely than the
cumulative half-value does — but it would still be far below $1$, since the
geometric factor $1/r$ sets the absolute scale.
