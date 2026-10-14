# Solutions — 06-10-06 Engineering Seismology Applications

**Read after attempting the exercises.** Numbers were computed, not estimated.
Lesson: [06 Engineering Seismology Applications](../06-engineering-seismics.md).
All models are SYNTHETIC.

---

## ★1 — Crossover and spread

$$x_c = 2h\sqrt{\frac{v_2+v_1}{v_2-v_1}}
= 2 \times 20\sqrt{\frac{3000+1000}{3000-1000}}
= 40\sqrt{2} = 56.5685\ \mathrm{m},$$
$$L = 3x_c = 3 \times 56.5685 = 169.71\ \mathrm{m},$$

say $170\ \mathrm{m}$ of cable. With the crossover at one third of the line the far
branch runs from $56.6$ to $170\ \mathrm{m}$, a $113\ \mathrm{m}$ baseline — more
than half the spread, which is what makes the slope of the far branch well
determined.

Note that $v_2/v_1 = 3$ here, so the answer is exactly the same as for
$v_1 = 1200$, $v_2 = 3600\ \mathrm{m\,s^{-1}}$ at the same depth: the design depends
on the **contrast ratio only**.

---

## ★2 — Depth uncertainty

The least-squares intercept uncertainty for $N$ equally spaced picks is

$$\sigma_{t_i} = \sigma_t\sqrt{\frac{1}{N} + \frac{\bar{x}^{2}}{S_{xx}}}.$$

With $N = 40$ picks between $x_c = 56.5685$ and $3x_c = 169.706\ \mathrm{m}$,
$\bar{x} = 113.137$, $S_{xx} = \sum (x-\bar{x})^{2} = 4.485\times10^{4}\
\mathrm{m^{2}}$ (the exact discrete sum for 40 picks, not the continuous
$NW^{2}/12$ approximation), so

$$\frac{\bar{x}^{2}}{S_{xx}} = \frac{12800}{44855} = 0.28537, \qquad
\frac{1}{N} = 0.02500,$$

$$\sigma_{t_i} = 1\ \mathrm{ms}\sqrt{0.31037} = 0.55710\ \mathrm{ms}.$$

The depth sensitivity is

$$\frac{\mathrm{d}h}{\mathrm{d}t_i} = \frac{v_1v_2}{2\sqrt{v_2^{2}-v_1^{2}}}
= \frac{1000 \times 3000}{2\sqrt{9.0\times10^{6}-1.0\times10^{6}}}
= \frac{3.0\times10^{6}}{5656.85} = 530.33\ \mathrm{m\,s^{-1}},$$

$$\sigma_h = 0.55710\times10^{-3} \times 530.33 = 0.2954\ \mathrm{m}
= 1.48\%\ \text{of}\ 20\ \mathrm{m}.$$

**The $\pm 0.5\ \mathrm{m}$ specification is met with a factor of $1.7$ to spare**,
and the margin is worth quantifying rather than assuming: if the contrast were
$1.5$ instead of $3$, $\mathrm{d}h/\mathrm{d}t_i$ would be $670.82\
\mathrm{m\,s^{-1}}$ and $\sigma_h$ would rise to $0.374\ \mathrm{m}$ — still
acceptable, but the crossover would have moved to $2 \times 20\sqrt{2.5/0.5}
= 89.44\ \mathrm{m}$ and the required spread to $268\ \mathrm{m}$.

---

## ★3 — Elastic moduli of the gravel

$$\mu = \rho V_s^{2} = 2000 \times 450^{2} = 4.05\times10^{8}\ \mathrm{Pa}
= 0.405\ \mathrm{GPa},$$
$$\nu = \frac{V_p^{2}-2V_s^{2}}{2(V_p^{2}-V_s^{2})}
= \frac{3.61\times10^{6} - 2(2.025\times10^{5})}
{2(3.61\times10^{6} - 2.025\times10^{5})}
= \frac{3.205\times10^{6}}{6.815\times10^{6}} = 0.4703,$$
$$E = 2\mu(1+\nu) = 2(0.405)(1.4703) = 1.191\ \mathrm{GPa},$$
$$M = \rho V_p^{2} = 2000 \times 3.61\times10^{6} = 7.22\times10^{9}\ \mathrm{Pa}
= 7.22\ \mathrm{GPa}.$$

**Exact, given the assumed model:** all four. $\mu = \rho V_s^{2}$,
$\nu$, $M = \rho V_p^{2}$ and $E = 2\mu(1+\nu)$ are identities of homogeneous,
isotropic, linearly elastic media. The **assumption** is that the medium *is* such a
material: homogeneous, isotropic and linear at the strain level of interest. At
$450\ \mathrm{m\,s^{-1}}$ in a gravel, homogeneity and isotropy are both
approximations, and linearity is the one Section 3.5 of the lesson examines.

---

## ★★4 — A 5% Vs error

$$\mu \propto V_s^{2} \;\Rightarrow\;
\frac{\delta\mu}{\mu} = 2\frac{\delta V_s}{V_s} = 2(0.05) = 0.1025 = 10.25\%,$$

$$\mu \to 0.405 \times 1.1025 = 0.4465\ \mathrm{GPa}.$$

**The velocity error is amplified by the square**, so a $5\%$ velocity error is a
$10.25\%$ modulus error. This is the single most important error-propagation fact in
engineering seismology: the quantity that enters design (a modulus) is quadratic in
the quantity that is measured (a velocity).

Poisson's ratio, by contrast, moves very little:

$$\frac{\partial\nu}{\partial V_s} = -\frac{V_sV_p^{2}}{(V_p^{2}-V_s^{2})^{2}}
= -\frac{450 \times 3.61\times10^{6}}{(3.4075\times10^{6})^{2}}
= -\frac{1.6245\times10^{9}}{1.1611\times10^{13}}
= -1.399\times10^{-4}\ \mathrm{s\,m^{-1}},$$

$$\delta\nu = -1.399\times10^{-4} \times 22.5\ \mathrm{m\,s^{-1}} = -0.0031,$$

so $\nu$ runs from about $0.4672$ to $0.4733$ — matching the demonstration's
$0.4670$–$0.4733$ from its finite differences. **A stiff, water-saturated layer is
insensitive to a velocity error in $\nu$ and doubly sensitive in $\mu$**, which is
the reverse of the bedrock case in the lesson, where a $5\%$ $V_s$ error moved $\nu$
by $0.026$.

---

## ★★5 — Site period and the stiffness that matches it

$$T_0 = \frac{4H}{V_{S,\text{avg}}} = \frac{4 \times 18}{263.0}
= 0.2738\ \mathrm{s}, \qquad f_0 = 3.653\ \mathrm{Hz}.$$

For an oscillator of mass $m$ on stiffness $k$, resonance with the site requires
$T = T_0$, hence

$$k_{\text{res}} = m\left(\frac{2\pi}{T_0}\right)^{2}
= 2.0\times10^{5} \times \left(\frac{2\pi}{0.2738}\right)^{2}
= 2.0\times10^{5} \times 526.5 = 1.053\times10^{8}\ \mathrm{N\,m^{-1}}.$$

A $5.0\times10^{5}\ \mathrm{kg}$ structure would need
$2.634\times10^{8}\ \mathrm{N\,m^{-1}}$ for the same resonance, and the
demonstration's design value of $8.0\times10^{6}\ \mathrm{N\,m^{-1}}$ is $33$ times
smaller — i.e. the design structure's period ($1.5708\ \mathrm{s}$) is far longer
than the site period, and it is not the site it has to worry about.

Note the sensitivity: $k_{\text{res}} \propto T_0^{-2}$, so a $10\%$ error in the
site period is a $21\%$ error in the required stiffness. Once again the square-law
amplification appears, and it is a reason to compute the site period from the
measured profile rather than to trust a rule of thumb.

---

## ★★6 — Strain and the operative modulus

$$\gamma \approx \frac{\mathrm{PGV}}{V_s} = \frac{0.15}{150}
= 1.0\times10^{-3}.$$

With the SYNTHETIC reduction curve,

$$\frac{G}{G_{\max}} = \frac{1}{1 + \gamma/10^{-3}} = \frac{1}{1 + 1.0} = 0.500.$$

Since $V_s \propto \sqrt{G/\rho}$ at fixed density,

$$V_s \to 150\sqrt{0.500} = 106.07\ \mathrm{m\,s^{-1}},$$

a $29.3\%$ reduction. If the reduction applied to the whole column, the site period
would lengthen by $1/\sqrt{0.5} = 1.414$, i.e. $+41.4\%$ — the sign is certain and
the size depends entirely on whether the strain is concentrated in the top layer or
spread through the column (the lesson measures $+11.3\%$ and $+29.1\%$ for those two
cases at a smaller strain).

---

## ★★★7 — Is ±2 m/s achievable for Vs30?

**No, not with the current pick error.** The budget is

$$\sigma_{V_{S30}}^{2} = \sigma_{\text{velocity}}^{2} + \sigma_{\text{thickness}}^{2}
= 3.020^{2} + 3.841^{2} = 9.12 + 14.75 = 23.87, \qquad
\sigma_{V_{S30}} = 4.880\ \mathrm{m\,s^{-1}}.$$

Since the velocity term alone is $3.020\ \mathrm{m\,s^{-1}}$, it already exceeds the
$\pm 2\ \mathrm{m\,s^{-1}}$ target. Driving the boundary tolerance to zero would
still leave $3.02\ \mathrm{m\,s^{-1}}$; to reach $2\ \mathrm{m\,s^{-1}}$ the
velocity errors must shrink by a factor $3.020/2 = 1.51$, i.e. the $0.2\ \mathrm{ms}$
pick standard deviation must fall to about $0.13\ \mathrm{ms}$ **and** the boundary
tolerance must be essentially zero. Neither is a realistic tender item, so the
correct answer is that the specification is not achievable by this survey design and
that the client should be told so with the arithmetic.

**If only the boundary tolerance can be halved**, to $0.05\ \mathrm{m}$:

$$\sigma_{\text{thickness}} = 3.841 \times \frac{0.05}{0.10}
= 1.920\ \mathrm{m\,s^{-1}},$$
$$\sigma_{V_{S30}} = \sqrt{3.020^{2} + 1.920^{2}} = \sqrt{9.12 + 3.69}
= 3.58\ \mathrm{m\,s^{-1}}.$$

**A defensible target is therefore $\pm 3.6\ \mathrm{m\,s^{-1}}$** ($0.90\%$ of
$V_{S30}$) with the same seismograms and tighter control of the layer boundaries —
obtained by better survey geometry, not by better picks. This is the same
conclusion the lesson draws from the variance shares ($62\%$ thickness, $38\%$
velocity): **the cheapest improvement to $V_{S30}$ is usually geometric.**

---

## ★★★8 — What each survey resolves

**Criterion.** A layer thinner than about a quarter of the dominant wavelength is
not resolved as a separate arrival ($\lambda/4 = V/(4f)$, a rule of thumb). At
$f = 50\ \mathrm{Hz}$:

| layer | thickness (m) | P: $\lambda/4$ (m) | resolved in P? | S: $\lambda/4$ (m) | resolved in S? |
|---|---|---|---|---|---|
| fill | 4 | 400/200 = 2.00 | yes (4 > 2.00) | 150/200 = 0.75 | yes |
| clay | 6 | 1500/200 = 7.50 | **no** (6 < 7.50) | 250/200 = 1.25 | yes |
| gravel | 8 | 1900/200 = 9.50 | **no** (8 < 9.50) | 450/200 = 2.25 | yes |
| bedrock | 12 | 3500/200 = 17.50 | **no** (12 < 17.50) | 1800/200 = 9.00 | yes |

**A P-wave refraction survey at $50\ \mathrm{Hz}$ resolves only the $4\ \mathrm{m}$
surface layer as a distinct unit**; the three deeper layers are each thinner than
their own P quarter-wavelength, so their first arrivals merge into a single fast
branch and the interpretation collapses to "one layer over a faster half-space",
with all the depth ambiguity that implies. **An S-wave (or surface-wave) survey
resolves every layer**, because the S wavelengths are shorter by the $V_p/V_s$
ratio.

**The frequency at which the clay becomes P-resolvable:**

$$\frac{\lambda}{4} = 6\ \mathrm{m} \;\Rightarrow\; \lambda = 24\ \mathrm{m}
\;\Rightarrow\; f = \frac{V_p}{\lambda} = \frac{1500}{24} = 62.5\ \mathrm{Hz}.$$

Note what that does *not* fix. Raising the dominant frequency to
$62.5\ \mathrm{Hz}$ resolves the clay but leaves the gravel needing
$f > 1900/(4 \times 8) = 59.4\ \mathrm{Hz}$ (already met at $62.5$) and the bedrock
needing $f > 3500/(4 \times 12) = 72.9\ \mathrm{Hz}$. Higher frequency also means
faster attenuation and a weaker head wave, so the fix trades resolution against
penetration — which is exactly why the shallow engineering solution is to change the
*wave type* rather than the frequency.
