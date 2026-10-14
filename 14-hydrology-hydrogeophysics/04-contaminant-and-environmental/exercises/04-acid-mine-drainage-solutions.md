# Solutions — 14-04-04 Acid Mine Drainage and Mining Environmental Geophysics

> Read after attempting. Lesson:
> [04 Acid Mine Drainage and Mining Environmental Geophysics](../04-acid-mine-drainage.md).
> All models **SYNTHETIC**.

---

## ★1 — The reaction and its balance

$$
\text{FeS}_2 + \tfrac{15}{4}\text{O}_2 + \tfrac{7}{2}\text{H}_2\text{O}
\to \text{Fe(OH)}_3 + 2\,\text{SO}_4^{2-} + 4\,\text{H}^{+} .
$$

| element | left | right |
|---|---|---|
| Fe | $1$ | $1$ |
| S | $2$ | $2$ |
| O | $\tfrac{15}{4}\times2 + \tfrac{7}{2} = 7.5 + 3.5 = 11$ | $3 + 8 = 11$ |
| H | $7$ | $3 + 4 = 7$ |

Charge: $2(-2) + 4(+1) = 0$. Balanced.

---

## ★2 — Molar masses and sulphate yield

$$
M(\text{FeS}_2) = 55.845 + 2\times32.060 = 119.965\ \mathrm{g\,mol^{-1}},
$$

$$
M(\text{SO}_4) = 32.060 + 4\times15.999 = 96.056\ \mathrm{g\,mol^{-1}} .
$$

Two moles of sulphate per mole of pyrite:

$$
\frac{2\times96.056}{119.965} = 1.6014\ \mathrm{g\,SO_4^{2-}\,g^{-1}}
= 1601.4\ \mathrm{g\,kg^{-1}} = 16.67\ \mathrm{mol\,kg^{-1}} .
$$

---

## ★3 — Acidity and neutralisation

Four moles of $\mathrm{H^+}$ per mole of pyrite:

$$
\frac{4}{119.965}\times1000 = 33.34\ \mathrm{mol\,H^{+}\,kg^{-1}}
= 33.34\ \mathrm{eq\,kg^{-1}} .
$$

The equivalent weight of calcium carbonate is half its molar mass,
$(40.078 + 12.011 + 3\times15.999)/2 = 50.043\
\mathrm{g\,eq^{-1}}$, so

$$
33.34\times50.043 = 1669\ \mathrm{g\,CaCO_3\ per\ kg\ pyrite} .
$$

**Note the size.** The neutralisation demand exceeds the mass of the pyrite that
generates it by a factor of $1.67$. This is the arithmetic behind the statement
that acid drainage is a long-term liability rather than a one-off treatment cost.

---

## ★★4 — Waste composition and concentration

**(a)** Per $\mathrm{m^{3}}$ of waste: mass $= 1800\ \mathrm{kg}$, so

$$m_\text{pyrite} = 0.004\times1800 = 7.20\ \mathrm{kg},$$

$$m_\text{sulphate} = 7.20\times1.6014 = 11.53\ \mathrm{kg}.$$

**(b)** Water volume $= 3.0\ \mathrm{m^{3}} = 3000\ \mathrm{L}$:

$$C = \frac{11.53\times10^{6}\ \mathrm{mg}}{3000\ \mathrm{L}}
= 3843\ \mathrm{mg\,L^{-1}} .$$

**(c) Why it is an upper bound.** (i) Complete oxidation is assumed, whereas the
real extent of reaction is limited by oxygen supply, grain size, bacterial
catalysis and passivation by iron-oxide coatings. (ii) No solubility limit or
secondary-mineral sink is applied: gypsum and ferrihydrite remove sulphate and
iron from solution, so the measured concentration is below the produced amount.
(iii) No attenuation or dilution by uncontaminated water is included. (iv) No
neutralisation by carbonate minerals, which is the largest single control in
practice and reduces the acidity (though not the sulphate) substantially.

---

## ★★5 — Conductivity and resistivity

$\sigma_b = 0.09\,\sigma_w$ and $\rho_b = 1/\sigma_b$:

| $C$ ($\mathrm{mg\,L^{-1}}$) | $\sigma_w$ ($\mathrm{S\,m^{-1}}$) | $\rho_b$ ($\Omega$ m) | change |
|---|---|---|---|
| 0 (background) | 0.050 | 222.2 | — |
| 1000 | 0.070 | 158.7 | $-28.6\%$ |
| 3843 | 0.1269 | 87.6 | $-60.6\%$ |

At $3843\ \mathrm{mg\,L^{-1}}$:
$\sigma_w = 0.050 + 2.0\times10^{-5}\times3843 = 0.1269\
\mathrm{S\,m^{-1}}$, $\sigma_b = 0.01142\ \mathrm{S\,m^{-1}}$,
$\rho_b = 87.6\ \Omega\,\mathrm{m}$, a $60.6\%$ reduction from the background.

---

## ★★6 — Transport of the front

**(a)** $t_\text{arrival} = 40/0.040 = 1000$ days.

**(b)** $D = \alpha_L v = 2.0\times0.040 = 0.080\
\mathrm{m^{2}\,day^{-1}}$; with $t = 1000$ days,

$$w_{10\text{–}90} = 2.563\sqrt{2\times0.080\times1000}
= 2.563\times12.65 = 32.4\ \mathrm{m}.$$

**(c)** Yes — comfortably. The transition is $32.4\ \mathrm{m}$ wide, so
electrode spacings of $5\ \mathrm{m}$ oversample it by a factor of six. A
spacing of $10$–$20\ \mathrm{m}$ would resolve it adequately at a fraction of the
survey cost, which is the practical recommendation of Section 7 of the lesson: go
finer than the transition width, not finer than habit.

---

## ★★★7 — Closure monitoring (model answer)

**(a) Three questions and their measurements.**

| question | measurement |
|---|---|
| Where are the reaction products now? | time-lapse ERT/EM for the bulk conductivity field, plus SP for the redox front |
| How much sulphide remains, and how fast is it reacting? | waste-characterisation sampling (sulphide sulphur and neutralisation potential) and a water balance on oxygen supply |
| How much water is moving through the waste? | a water balance from precipitation, cover performance, and a seepage measurement at the toe |

**(b) Why a conductivity map cannot measure remaining sulphide mass.** The
conductivity responds to the *products in solution* — sulphate and acidity — and
that solution is transported, diluted and partly removed by secondary minerals.
A conductive zone therefore records where the products have gone, which is
down-gradient of the reaction and displaced in time. Two facilities with the same
conductivity map can have sulphide inventories differing by orders of magnitude,
because the reaction *rate* is not in the data. What could measure the remaining
mass: direct sampling for sulphide sulphur with acid-base accounting on
representative waste, and a mass balance combining that inventory with the oxygen
flux — both chemistry and hydrology, not geophysics.

**(c) Largest uncertainty and its reduction.** The percolation ratio (how much
water passes through the waste per unit mass) dominates the predicted discharge
concentration, because the concentration is inversely proportional to it
(Section 5 of the lesson: $64\,056$ to $1\,601\ \mathrm{mg\,L^{-1}}$ across a
factor of $40$ in ratio) whereas the stoichiometric yield is known to better than
a per cent. It is reduced by a cover water balance with a measured seepage at the
toe — a lysimeter, a weir, or a temperature/conductivity profile through the
waste — not by a better analysis of the rock.

---

## ★★★8 — Self-potential: separability and distribution

**(a) Non-separability.** $V$ depends on $\rho$ and $I$ only through the product
$\rho I$; the transformation $(\rho, I) \to (\lambda\rho, I/\lambda)$ leaves every
potential unchanged. One number is determined from two unknowns, and the null
space is one-dimensional. An independent resistivity measurement of the
half-space fixes $\rho$, leaving $I$.

**(b) Distributed sources.** A redox front of finite length is a *superposition*
of compact sources along the front. The potential of a line of sources is broader
than that of a single source with the same peak value: at large distance the
line source decays as $1/x$ while the point source decays as $1/x^{2}$. Fitting
the point-source profile to line-source data therefore returns a half-width
larger than the true depth, and the depth estimate based on
$x_{1/2} = \sqrt3\,d$ is **biased deep**. The size of the bias grows with the
ratio of the source length to the depth; when the length exceeds roughly the
depth, the depth is not determined by the half-width at all.

**(c) Distinguishing the two.** Measure the anomaly along two orthogonal
profiles and at several offsets. A compact source gives a radially symmetric,
isotropic hump whose half-width is the depth on every profile; a linear
distributed front gives an elongated anomaly whose width along the strike of the
front grows without limit while the across-strike width stays close to the
depth. The resolution limit is set by the survey extent: if the profile is shorter
than the front's length, the elongation is not observable, and the two models
cannot be distinguished. As a rule, the profile must extend to at least two to
three times the larger of the two length scales, and the electrode spacing must
be small compared with the source depth to keep the half-width measurement
meaningful.
