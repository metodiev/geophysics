# Solutions — 09-06-03 Downhole EM Logging and Induction Tools

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All models are **SYNTHETIC**.

Lesson: [03 Downhole EM Logging and Induction Tools](../03-downhole-em-logging.md).

---

## ★1 — Skin depth and induction number

$$\delta = 503.2921\sqrt{\frac{\rho}{f}}
= 503.2921\sqrt{\frac{20}{20000}} = 503.2921\times0.0316228
= 15.9155\ \mathrm{m}.$$

| $L$ (m) | $p = L/\delta$ | regime |
|---|---|---|
| 0.50 | 0.0314 | induction |
| 1.00 | 0.0628 | induction |
| 1.50 | 0.0942 | induction |

All three are in the induction regime ($p\ll1$): the quadrature calibration
should be accurate to about $(2/3)p$, i.e. $2.1\%$, $4.2\%$ and $6.3\%$
respectively.

---

## ★2 — Dimensions and the two square roots

$\omega$ has units $\mathrm{s^{-1}}$, $\mu$ has $\mathrm{H\,m^{-1}}$ and $\sigma$
has $\mathrm{S\,m^{-1}}$. Then
$\omega\mu\sigma$ has units $\mathrm{s^{-1}}\cdot\mathrm{H\,m^{-1}}\cdot
\mathrm{S\,m^{-1}} = (\mathrm{H\,S})\,\mathrm{m^{-2}\,s^{-1}}$. Because
$\mathrm{H} = \Omega\,\mathrm{s}$ and $\mathrm{S} = \Omega^{-1}$, the product
$\mathrm{H\,S}$ is dimensionless, so $\omega\mu\sigma$ has units
$\mathrm{m^{-2}}$ and its reciprocal square root is a length. ✔

The two scalings are inverse: $\delta \propto \sigma^{-1/2}$, and since
$p = L/\delta \propto \sigma^{1/2}$ the bias $\tfrac23p$ rises as
$\sigma^{1/2}$. A formation ten times more conductive has a bias
$\sqrt{10} = 3.16$ times larger — which is why the calibration problem is a
*conductive-formation* problem.

---

## ★3 — The bias for three spacings

| $p$ | $\tfrac23p$ | exact $\sigma_a/\sigma - 1$ | difference |
|---|---|---|---|
| 0.0314 | +2.09% | +2.10% | 0.01 pp |
| 0.0628 | +4.19% | +4.22% | 0.03 pp |
| 0.0942 | +6.28% | +6.39% | 0.11 pp |

The approximation is excellent at these induction numbers; its error grows as the
next term in the series, of order $p^{2}$, which is why it fails (by about 5%) at
$p\approx0.5$ and completely at $p\approx1$.

---

## ★4 — The resistivity at which the bias reaches 10%

Approximation: $\tfrac23p = 0.10 \Rightarrow p = 0.15$, so
$\delta = L/p = 1.00/0.15 = 6.6667$ m, and

$$\rho = f\left(\frac{\delta}{503.2921}\right)^{2}
= 20000\left(\frac{6.6667}{503.2921}\right)^{2}
= 20000\times(0.0132463)^{2} = 3.509\ \Omega\,\mathrm{m}.$$

Exact: at $p = 0.15$ the lesson's table interpolates to a bias of about
$+10.1\%$, so the exact threshold is a little above
$3.5\ \Omega\,\mathrm{m}$ — the same answer to the precision that matters. Below
about $3.5\ \Omega\,\mathrm{m}$ the quadrature calibration of this sonde is not a
10% measurement, whatever the receiver's own accuracy.

---

## ★5 — Bed thickness for a 5% reading

The reading is within 5% of the bed value when the background contributes less
than 5%, i.e. when the geometric-factor fraction inside the bed is at least
0.95. From the lesson's measured fractions (0.8840 at $|z|\le 2L$, 0.9258 at
$3L$, 0.9467 at $4L$, 0.9591 at $5L$), the 0.95 threshold is crossed at about
$4.2L$: a bed must be roughly **8.4 half-spacings**, i.e. $4L$–$5L$ thick, to be
read to 5%.

Cross-check: a 1 m bed with $L = 0.25$ m is $4L$ thick, and the measured reading
is 0.9484 (94.8%), which is exactly the fraction 0.9467 predicted for $|z|\le4L$.
The two independent routes agree to 0.2 percentage points. This is the kind of
cross-check that turns a rule of thumb ("about four spacings") into a number you
can defend.

---

## ★6 — Saturation error from a thin-bed reading

$\sigma \propto S_w^{2} \Rightarrow S_w \propto \sigma^{1/2}$. The reading is
0.7922/1.0000 = 0.7922 of the true bed conductivity, so the inferred saturation is
$\sqrt{0.7922} = 0.890$ of the true value: a **$-11.0\%$ relative saturation
error**, i.e. an 11 percentage-point error on a fully saturated bed
(1.00 → 0.89).

Independent measurement that settles it: a **density-neutron or NMR porosity log**
in the same hole, or a higher-resolution resistivity log with a shorter spacing
(a micro-resistivity pad tool, or a shorter induction sonde). If the bed is
genuinely 1 m thick and the alternative tool reads the bed value close to
$1.00\ \mathrm{S\,m^{-1}}$, the deficit is the shoulder effect of the long sonde;
if the alternative also reads low, the deficit is real and the bed is thinner or
less conductive than assumed.

---

## ★7 — Separating salinity from clay

Model answer. Two frequencies give two equations per depth because the response
depends on $\sigma$ through $p = L/\delta\propto\sqrt{\sigma}$: the same
conductivity at two frequencies produces two different ratios
$\sigma_a/\sigma$, and the *pair* constrains $\sigma$ and $p$, i.e. $\sigma$ and
the frequency dependence. Two spacings add geometric information: the short
spacing is dominated by the near-sonde volume (borehole and invaded zone) and the
long spacing by the formation. Invert a model with, per depth interval,
(a) formation conductivity, (b) an interfacial (clay-related) polarisation
term whose magnitude scales with cation-exchange capacity (module 09-03), and
(c) borehole and invaded-zone conductivities.

Data to weight most: the **quadrature at the low frequency** (linear in
conductivity, least skin-effect bias) and the **frequency difference** of the
quadrature between the two frequencies (which isolates the polarisation term).
The degeneracy that remains: at low clay content the polarisation term is weak,
and then a small salinity increase produces the same two-frequency signature as a
small clay increase — the separation fails exactly where the conductivity is
small. Independent information (a gamma-ray log for clay volume, or a
temperature log for the salinity calibration) is required in that limit, and no
choice of frequencies removes the degeneracy.

---

## ★8 — Measuring the borehole error, and separating it from skin effect

Model answer. Build the same synthetic formation twice: (i) homogeneous, with a
borehole of a stated conductivity and radius; (ii) homogeneous with no borehole.
Compute the exact tool response in both — the whole-space closed form of the
lesson for (ii), a finite-difference or integral-equation solution for the
borehole case (i) — and report

$$\varepsilon_{\text{bh}}(\sigma) = \frac{\sigma_a^{\text{(bh)}} - \sigma_a^{\text{(no bh)}}}{\sigma}
\quad\text{as a function of the borehole/formation contrast.}$$

**Statistic that reveals it:** $\varepsilon_{\text{bh}}$ normalised by the
borehole-to-formation conductivity ratio, plotted against $p$. Separation from
skin effect: the skin-effect bias is a function of $p$ alone (measured in the
lesson as $+6.65\%$ at $p = 0.10$, i.e. about $0.67$ per unit $p$ to first order)
and is independent of the borehole conductivity, whereas
$\varepsilon_{\text{bh}}$ is independent of $p$ at
low $p$ and scales with the borehole contrast. So run the same experiment at two
borehole contrasts and two frequencies: the component that varies with borehole
contrast is the borehole term, and the component that varies with $p$ at fixed
contrast is the skin effect. A study that varied only one of them could not
separate the two, which is precisely why the design must cross the two.
