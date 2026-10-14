# Solutions — 05-05-01 Survey Planning: Objectives, Target Resolution, Budget

> **Read this after attempting the exercises, not before.**
>
> Values quoted from the module's demonstration script are the values it printed.
> Everything else is computed here from the stated formulae.

---

## ★1 — Peak anomaly of the sphere

The exterior field of a uniform sphere is exactly that of a point mass at its
centre, because the shell theorem applies to every shell from the radius outward —
derived in
[02-08-01](../../../02-physics/08-potential-theory/01-gravitational-potential.md).
So

$$g_z^{\max} = \frac{GM}{h^{2}}, \qquad
M = \tfrac{4}{3}\pi R^{3}\Delta\rho = \tfrac{4}{3}\pi (50)^{3}(1000)
= 5.236\times10^{8}\ \mathrm{kg}.$$

$$g_z^{\max} = \frac{(6.67430\times10^{-11})(5.236\times10^{8})}{(200)^{2}}
= \frac{3.4947\times10^{-2}}{4.0\times10^{4}}
= 8.737\times10^{-7}\ \mathrm{m\,s^{-2}}.$$

In mGal: $8.737\times10^{-7}/10^{-5} = \boxed{0.08737\ \mathrm{mGal}}$.

This is the first row of the lesson's target table, so the lesson's number is
confirmed.

---

## ★2 — Signal-to-noise for three noise levels

Using $\mathrm{SNR} = 0.08737/\sigma$ and the $3\sigma$ test
$\mathrm{SNR} > 3$:

| $\sigma$ (mGal) | SNR | detectable at $3\sigma$? |
|---|---|---|
| 0.010 | 8.737 | **yes** |
| 0.005 | 17.47 | **yes** |
| 0.050 | 1.747 | **no** |

Note the third case: the body is a large, dense, shallow target — and a 0.05 mGal
noise level makes it undetectable. Detectability is a property of the *pair*
(target, noise), never of the body alone.

---

## ★3 — Doubling the radius

For fixed $\Delta\rho$ and fixed noise, equation (3) of the lesson gives
$h_{\max}\propto R^{3/2}$, so

$$\frac{h_{\max}(2R)}{h_{\max}(R)} = 2^{3/2} = \boxed{2.83}.$$

The exponent comes from the mass, which grows as $R^{3}$ while the depth penalty
is $h^{-2}$: $h_{\max}^{2}\propto R^{3}$. This is confirmed by the lesson's table,
where $965.4/341.3 = 2.83$.

---

## ★4 — Repeated measurements

**(a)** $\mathrm{SNR} = 0.030/0.010 = \boxed{3.0}$.

**(b)** Averaging $N$ independent measurements reduces the noise by $\sqrt{N}$, so
$3\sqrt{N} = 6 \Rightarrow \sqrt N = 2 \Rightarrow N = \boxed{4}$.

**(c)** $4 \times 90\ \mathrm{s} = \boxed{6\ \mathrm{min}}$ per station, against
1.5 min — a 4× cost for a factor 2 in S/N. The lesson's measured table for the
same scaling gives, over 40 000 realisations, $N=4$: 0.50141 against a predicted
0.50000.

---

## ★5 — Three budgets

- **Resolution** is controlled by the shortest resolvable wavelength — set by
  bandwidth, geometry and the physics (Fresnel zone $\sqrt{\lambda h/2}$ or the
  two-body limit $h$).
- **Spatial sampling** is controlled by the station spacing through the Nyquist
  wavenumber $k_N=\pi/\Delta x$.
- **Depth of investigation** is controlled by the target's amplitude relative to
  the noise floor, i.e. by source strength, depth and $\sigma$.

Improving one does not improve another: finer sampling does not lower the noise per
station, and lower noise does not shrink the Fresnel zone.

---

## ★★6 — Station spacing, count and cost

**(a)** $\Delta x \le h/4 = 300/4 = \boxed{75\ \mathrm{m}}$. The rule gives eight
stations across the anomaly (half-width $\sim h$ each side), the minimum for the
*shape* to be characterised; the Nyquist-only requirement would be 150 m.

**(b)** $20\,000 \times 15\,000 / 75^{2} = 3.0\times10^{8}/5625 = 53\,333$
stations. Round to $\boxed{5.3\times10^{4}}$ stations.

**(c)** $5.3\times10^{4} \times 4\ \mathrm{min} = 2.13\times10^{5}\ \mathrm{min}
= 3556\ \mathrm{h}$, i.e. $3556/8 = \boxed{445\ \text{field days}}$ — about
1.8 crew-years at 250 field days per year. This is why the spacing rule is applied
to the target footprint, not to a whole regional map.

**(d)** At 25 m the count scales as $1/\Delta x^{2}$:
$(75/25)^{2} = 9$, so $4.8\times10^{5}$ stations and 4000 field days. The survey
becomes infeasible, and — per Section 5 of the lesson — it does not thereby resolve
anything below the physical limit.

---

## ★★7 — The magnetic case

**(a)** For a vertical dipole of moment $m$ at depth $h$ measured vertically, the
peak field is

$$B_z^{\max} = \frac{\mu_0}{4\pi}\cdot\frac{2m}{h^{3}}
= 10^{-7}\times\frac{2\times10^{8}}{2.7\times10^{7}}
= 7.41\times10^{-7}\ \mathrm{T} = \boxed{741\ \mathrm{nT}}.$$

**(b)** $\mathrm{SNR} = 741/1 = \boxed{741}$.

**(c)** Yes, emphatically.

*Two cautions about comparing this with ★★6.* First, the two questions are not
comparable in magnitude: nT and mGal are different units for different physical
quantities, and a SNR of 741 versus 8.7 says only that each method was given
different (synthetic) contrast assumptions. What *is* comparable is the depth
behaviour, and there the magnetic case is worse: the dipole amplitude falls as
$h^{-3}$, so at fixed moment a magnetic survey loses its target faster with depth
than a gravity survey does. The lesson's positioning demonstration measures the
consequence of that steep decay directly: a synthetic vertical dipole of moment
$10^{5}\ \mathrm{A\,m^{2}}$ gives 20000.0 nT at 10 m depth and 20.0 nT at 100 m
depth — a factor 1000 for a factor 10 in depth.

Second, the *gradient* is also steeper, which is why the same $h^{-3}$ behaviour
that makes the amplitude large at shallow depth makes the positioning requirement
severe: a 0.5 m horizontal mislocation costs 1371 nT at 10 m depth in the measured
table of [05-05-04](../04-positioning-gnss.md).

---

## ★★8 — The height accuracy a 0.02 mGal budget requires

**(a)** Let the positioning term be $\sigma_z \times 0.30785$ and the others
0.010 mGal. Then

$$\left(\sigma_z \times 0.30785\right)^{2} + 0.010^{2} = 0.020^{2}$$
$$\sigma_z \times 0.30785 = \sqrt{0.000400 - 0.000100} = \sqrt{0.000300}
= 0.01732\ \mathrm{mGal}$$
$$\sigma_z = \frac{0.01732}{0.30785} = \boxed{0.0563\ \mathrm{m}} .$$

**(b)** About 5.6 cm vertical — **RTK class**. DGPS at 0.5 m gives 0.154 mGal,
which alone is 7.7× the proposed total budget.

**(c)** The claim is false as stated. It is a statement about the *instrument*, and
the budget is dominated by the *positioning*. The instrument's 0.01 mGal
repeatability is 25 % of the budget in variance; the total is 0.1642 mGal in the
lesson's measured budget (87.9 % of the variance in the positioning term), so the
survey's real threshold is about 0.49 mGal, not 0.02 mGal.

---

## ★★9 — The fold taper

**(a)** $185/891 = \boxed{20.8\ \%}$ of the bins (measured 185 below full fold, i.e.
79.2 % at full fold — the lesson's printed figures).

**(b)** $\sqrt{48/24} = \sqrt{2} = \boxed{1.41}$; the edge bins are about 1.4×
noisier, so the S/N there is 71 % of the interior value.

**(c)** Report: the interior 79 % of the profile is at full fold; the outer
185 bins (about 925 m of midpoint axis at each end, measured vs a predicted ramp of
$N\Delta x/2-\Delta s = 940$ m) are at reduced fold and should not be interpreted at
the same confidence. The client should be told the *usable* extent, not the
*acquired* extent — the distinction is the whole content of the taper measurement.

---

## ★★★10 — Measuring the detection threshold

A satisfactory answer will:

1. **Define the experiment.** Signal $s(x)$ = the known anomaly shape; noise
   Gaussian with $\sigma$; $M = 2000$ realisations per SNR; a matched filter
   $h\propto s$ with the statistic $z = (h\cdot d)/\lVert h\rVert$, which is
   optimal for known signal shape and white noise.
2. **Set the false-alarm rate.** From the noise-only distribution, take the
   threshold $z_{0}$ at the 95th percentile; this fixes a 5 % per-cell false-alarm
   rate *by construction*, which is why the same realisation set must be used.
3. **Measure the detection probability** as the fraction of signal-present
   realisations with $z > z_{0}$, and report the SNR at which it reaches 0.90.
4. **Compare with the amplitude rule.** The matched-filter threshold in SNR units
   for $P_d = 0.90$, $P_{fa} = 0.05$ is approximately
   $z_{0}/\lVert h \rVert + 1.28$; the amplitude rule uses 3. They are different
   numbers measuring different things: the amplitude rule is a *per-station*
   amplitude test, the matched filter is an *optimal* test using the whole profile.
5. **State the limits.** The experiment fixes the shape, the noise colour and the
   independence assumption. Change any of these — a different anomaly shape, pink
   noise, spatially correlated noise — and the threshold moves. The result is a
   threshold for *this* experiment, not a universal constant.

A strong answer will also note that a per-cell 5 % false-alarm rate over a survey of
$10^{5}$ cells produces $5\times10^{3}$ false anomalies, which is why the
*per-survey* rate of question ★★★11 is the relevant one.

---

## ★★★11 — Multiplicity of the detection test

The Gaussian two-sided tail probabilities are:

| threshold | tail probability $P(\lvert z\rvert > k)$ | expected false positives in $10^{5}$ cells |
|---|---|---|
| $3\sigma$ | $2.700\times10^{-3}$ | 270 |
| $4\sigma$ | $6.334\times10^{-5}$ | 6.3 |
| $5\sigma$ | $5.733\times10^{-7}$ | 0.057 |

For a *survey-wide* false-alarm rate of 5 %, the per-cell rate must be
$0.05/10^{5} = 5\times10^{-7}$, i.e. a threshold of about $5.06\sigma$.

The cells are **not** independent: the field is spatially correlated over the
anomaly width, and the noise is correlated after any filtering or gridding. With
$N_{\text{eff}}$ independent cells rather than $10^{5}$, the required threshold
*falls*; for $N_{\text{eff}} = 10^{3}$ the per-cell rate is $5\times10^{-5}$ and the
threshold is about $4.06\sigma$. So the honest statement is that the threshold
depends on the *effective* number of independent tests, which requires knowledge of
the correlation length — and quoting a $3\sigma$ threshold without it is incomplete.

---

## ★★★12 — Technical memorandum

A satisfactory memorandum will contain:

- **Reframing.** "Larger than 20 m radius at 100 m depth" is not decidable without a
  property contrast, a noise level and a target count. Propose: detect spheres of
  radius $\ge 20$ m, density contrast $\ge \Delta\rho_{\min}$, centre depth
  $\le 100$ m, at a false-alarm rate of 5 % per survey.
- **Arithmetic.** With the lesson's formula,
  $g^{\max} = 4\pi G R^{3}\Delta\rho/(3h^{2})$; for $R = 20$ m and
  $\Delta\rho = 200\ \mathrm{kg\,m^{-3}}$, $h = 100$ m:
  $M = 6.70\times10^{6}$ kg and $g^{\max} = 4.47\times10^{-8}\ \mathrm{m\,s^{-2}}
  = 0.0045$ mGal. A 0.01 mGal instrument gives SNR 0.45 — **not detectable**.
- **What would be needed.** Either a contrast $\ge 1000\ \mathrm{kg\,m^{-3}}$
  (giving 0.022 mGal, SNR 2.2, still marginal at $3\sigma$), or a noise level
  $\le 0.0015$ mGal (a 4-D class procedure with repeat occupations and
  millimetre positioning), or a shallower depth.
- **The one condition for "no".** If the target's contrast is at the low end
  (a weathered cavity, a low-density void of a few hundred kg m⁻³) the amplitude
  is below the achievable noise at 100 m, and the correct answer is that the
  objective requires a different method — for example microgravity with a
  high-repeatability procedure, or a geophysical method with a different depth
  reach.
- **Assumptions stated.** Sphere geometry; point-mass approximation; Gaussian noise;
  a $3\sigma$ criterion per station; no correlated noise.
