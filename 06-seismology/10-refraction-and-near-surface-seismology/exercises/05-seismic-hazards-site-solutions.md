# Solutions — 06-10-05 Site Characterisation: Vs30 and Site Response

**Read after attempting the exercises.** Numbers were computed, not estimated.
Lesson: [05 Site Characterisation: Vs30 and Site Response](../05-seismic-hazards-site.md).
All models are SYNTHETIC.

---

## ★1 — Vs30, site class and the arithmetic mean

$$\Delta t = \frac{5}{150} + \frac{10}{250} + \frac{15}{500}
= 0.0333333 + 0.0400000 + 0.0300000 = 0.1033333\ \mathrm{s},$$
$$V_{S30} = \frac{30}{0.1033333} = 290.32\ \mathrm{m\,s^{-1}}.$$

Against the standard boundaries $1500/760/360/180\ \mathrm{m\,s^{-1}}$:
$290.32$ lies between $180$ and $360$, so the class is **D**.

Thickness-weighted arithmetic mean:
$\frac{5 \times 150 + 10 \times 250 + 15 \times 500}{30}
= \frac{750 + 2500 + 7500}{30} = 358.33\ \mathrm{m\,s^{-1}}$, which is
$+23.4\%$ above $V_{S30}$ and would put a naive calculation in class C.
The arithmetic–harmonic inequality guarantees $V_{S30} \le$ arithmetic mean, with
equality only for a uniform column.

---

## ★2 — The weights

$$w_1 = \frac{0.0333333}{0.1033333} = 0.32258, \quad
w_2 = \frac{0.0400000}{0.1033333} = 0.38710, \quad
w_3 = \frac{0.0300000}{0.1033333} = 0.29032.$$

$$w_1 + w_2 + w_3 = 1.00000. \qquad ✔$$

Note that the middle layer has the largest weight although it is neither the
thinnest nor the thickest: the weights are proportional to $h_i/V_{S,i}$, i.e. to
*time*, and a $10\ \mathrm{m}$ layer at $250\ \mathrm{m\,s^{-1}}$ takes longer to
cross than a $15\ \mathrm{m}$ layer at $500\ \mathrm{m\,s^{-1}}$.

---

## ★3 — The uniform-column rule

$$T_0 = \frac{4H}{V_{S30}} = \frac{4 \times 30}{290.32} = 0.41333\ \mathrm{s},
\qquad f_0 = 2.4194\ \mathrm{Hz}.$$

The rule assumes the column is **uniform at $V_{S30}$ and sits on a rigid base**.
Neither is true here: the profile spans a factor of $3.3$ in velocity, and the
half-space at $900\ \mathrm{m\,s^{-1}}$ is only a modest contrast above the deepest
soil layer. The rule therefore gives the right order of magnitude and not the
period — the demonstration measures overestimates of $29\%$ and $35\%$ on its own
two profiles.

---

## ★★4 — A 20% stiffness increase in the top layer

$$\frac{\delta V_{S30}}{V_{S30}} = w_1 \times 0.20 = 0.32258 \times 0.20
= 0.06452 = +6.45\%,$$

$$\delta V_{S30} = 0.06452 \times 290.32 = 18.73\ \mathrm{m\,s^{-1}},
\qquad V_{S30} \to 309.05\ \mathrm{m\,s^{-1}}.$$

**The site class is unchanged**, because $309.05$ is still inside $180$–$360$. This
is the practical reason the weights matter: a $20\%$ improvement in the stiffest,
fastest, easiest-to-measure layer moves the headline number by only $6.5\%$, and a
class boundary is $180\ \mathrm{m\,s^{-1}}$ wide.

---

## ★★5 — Uncertainty of Vs30 for 10% velocity errors

$$\frac{\sigma_{V_{S30}}}{V_{S30}}
= \sqrt{\sum_i \left(w_i\frac{\sigma_{V,i}}{V_{S,i}}\right)^{2}}
= 0.10\sqrt{0.32258^{2} + 0.38710^{2} + 0.29032^{2}}$$
$$= 0.10\sqrt{0.104058 + 0.149846 + 0.084286}
= 0.10\sqrt{0.338190} = 0.10 \times 0.581541 = 0.058154.$$

$$\sigma_{V_{S30}} = 0.058154 \times 290.32 = 16.88\ \mathrm{m\,s^{-1}},$$

i.e. $5.82\%$ of $V_{S30}$ for a $10\%$ error in every layer velocity.

**Why smaller than $10\%$?** Because the weights form a partition
($\sum_i w_i = 1$) and the errors are independent, so the errors partially cancel.
The fractional variance of $V_{S30}$ is the weighted sum of the fractional
variances, $\sum_i w_i^{2}\sigma_i^{2}/V_i^{2}$, and for weights that must sum to
one the sum of squares is always less than the largest weight; here it is
$0.338$ against a maximum possible of $1$. **Independent errors in a partition
average down; correlated errors would not**, which is why a systematic velocity bias
(say a wrong assumed Poisson's ratio in the inversion) is far more dangerous than
random scatter.

---

## ★★6 — Impedance ratio and peak

$$Z_{\text{soil}} = 1900 \times 200 = 3.80\times10^{5},
\qquad Z_{\text{hs}} = 2200 \times 900 = 1.98\times10^{6},$$
$$\frac{Z_{\text{hs}}}{Z_{\text{soil}}} = \frac{1.98\times10^{6}}{3.80\times10^{5}}
= 5.2105.$$

For a lossless single layer the peak of $|T|$ **equals** the impedance ratio:
$|T|_{\max} = 5.2105$. The demonstration measures exactly this at $5\ \mathrm{Hz}$,
which is the third resonance of a $30\ \mathrm{m}$, $200\ \mathrm{m\,s^{-1}}$ layer
($f_0 = 200/120 = 1.6667\ \mathrm{Hz}$).

In a real calculation the peak is finite because **damping** consumes energy at the
resonance: at $Q = 20$ the demonstration measures $4.8886$ instead of $5.8759$ for
its layered profile, $83\%$ of the lossless value. A residual impedance ratio of
exactly the lossless peak should be read as a missing damping term, not as a
physical prediction.

---

## ★★★7 — Two profiles, one Vs30, different responses

Target $\Delta t = 0.1033333\ \mathrm{s}$ over $30\ \mathrm{m}$ so that
$V_{S30} = 290.32\ \mathrm{m\,s^{-1}}$. Two constructions:

**A′ — gradual stiffening.** $5\ \mathrm{m}$ at $150$, $10\ \mathrm{m}$ at $250$,
$15\ \mathrm{m}$ at $500\ \mathrm{m\,s^{-1}}$ (the profile of ★1).

**B′ — a two-layer contrast with a thin soft cap.**

$$\frac{6}{150} + \frac{9}{250} + \frac{15}{548.8}
= 0.0400000 + 0.0360000 + 0.0273333 = 0.1033333\ \mathrm{s} \quad ✔$$

so $V_{S30} = 30/0.1033333 = 290.32\ \mathrm{m\,s^{-1}}$, identical to A′ — the
third layer's velocity was chosen to make the travel times match exactly.

**Prediction.** The periods should agree to a few per cent and the peak
amplifications should *not*: A′ has a gradual velocity increase (weak internal
contrasts) while B′ has a $150 \to 250\ \mathrm{m\,s^{-1}}$ step near the surface
and a much weaker one below. A stronger shallow contrast raises the peak, and the
band-averaged factors should agree more closely than the peaks, since band averages
are the summary in which different arrangements look alike.

**Metric.** The fundamental frequency $f_0$ and peak $|T|$ from the 1-D SH transfer
function, plus the mean of $|T|$ over $0.1$–$10\ \mathrm{Hz}$.

**Check (same code as the demonstration, half-space $900\ \mathrm{m\,s^{-1}}$,
$2200\ \mathrm{kg\,m^{-3}}$, $Q = 20$ in the soil, $Q = 100$ in the rock, densities
$1800$, $1850$, $1900\ \mathrm{kg\,m^{-3}}$):**

| quantity | A′ | B′ |
|---|---|---|
| $V_{S30}$ | $290.32$ | $290.33$ |
| $f_0$ | $3.3560\ \mathrm{Hz}$ | $3.4240\ \mathrm{Hz}$ |
| $T_0$ | $0.2980\ \mathrm{s}$ | $0.2921\ \mathrm{s}$ |
| peak $|T|$ | $3.8426$ | $4.1724$ |
| mean $|T|$, 0.1–10 Hz | $2.4059$ | $2.4043$ |

The prediction holds in detail: the periods agree to $2.0\%$, the peaks differ by
$8.6\%$, and the band means agree to $0.07\%$. Once again the two sites are
indistinguishable by $V_{S30}$ and by a band average, and distinguishable by their
resonance — which is the whole argument for keeping the profile rather than its
summary.

---

## ★★★8 — A number with two classes

> The value is $V_{S30} = 370 \pm 25\ \mathrm{m\,s^{-1}}$, which against the
> standard boundaries $360$ and $760\ \mathrm{m\,s^{-1}}$ admits **both class C
> (above 360) and class D (180–360)**; the uncertainty is comparable to the distance
> to the boundary, so the correct label is the pair, not the single letter.
>
> The boundary is a **convention with legal force rather than a physical
> threshold**: there is no discontinuity in ground behaviour at
> $360\ \mathrm{m\,s^{-1}}$, and a site whose measured value sits on the line is
> classified by the convention, not by the ground. Reporting the value, its
> uncertainty and both admitted classes costs one line and removes a false
> precision that a reader would otherwise be entitled to rely on.

A defensible design response is to carry both classes through the calculation and
report the envelope, or to acquire the measurement that resolves the ambiguity (a
longer-wavelength dispersion measurement, or a deeper borehole) if the class
difference matters to the structure being designed.
