# Solutions — 14-05-01 Time-Lapse ERT for Infiltration and Transport

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Where more than one answer is defensible it is said so.

Lesson: [01 Time-Lapse ERT](../01-time-lapse-ert.md).

---

## ★1 — Archie mapping

$\phi^{-m} = 0.35^{-1.80} = 6.6171$, so $\rho = 10 \times 6.6171 \times S^{-2}$.

- $S = 0.40$: $\rho = 10 \times 6.6171 \times 6.2500 = 413.6\ \Omega\,\mathrm{m}$.
- $S = 0.80$: $\rho = 10 \times 6.6171 \times 1.5625 = 103.4\ \Omega\,\mathrm{m}$.

Ratio $= 1.5625/6.2500 = 0.2500 = (S_2/S_1)^{-n} = (0.8/0.4)^{-2}$, exactly. ✔

---

## ★2 — The Wenner series at both limits

*Small $a/h$.* Every bracket
$\left[1+(2nh/a)^2\right]^{-1/2} - \left[4+(2nh/a)^2\right]^{-1/2} \to 0$, so
the sum vanishes and $\rho_a \to \rho_1$. ✔

*Large $a/h$.* Every bracket $\to 1 - \tfrac12 = \tfrac12$, so

$$\rho_a \to \rho_1\left(1 + 4 \times \tfrac12 \sum k^n\right)
= \rho_1\left(1 + \frac{2k}{1-k}\right) = \rho_1\frac{1+k}{1-k}.$$

With $\rho_1 = 90$, $\rho_2 = 330$: $k = (330-90)/(330+90) = 0.5714$, and

$$\rho_1\frac{1+k}{1-k} = 90 \times \frac{1.5714}{0.4286} = 90 \times 3.6667
= 330.0\ \Omega\,\mathrm{m} = \rho_2. ✔$$

---

## ★3 — Units

$R_t = \Delta V/I$ in $\Omega$; the geometric factor has units of length (m, for
a Wenner array $k = 2\pi a$), so $\rho_a = kR_t$ in $\Omega\,\mathrm{m}$; the
ratio of two resistivities is dimensionless. ✔

---

## ★4 — Detectability across the spacings

For a 0.5 m front:

| $a$ (m) | 0.5 | 1 | 2 | 4 | 8 | 16 |
|---|---|---|---|---|---|---|
| $r$ | 0.3477 | 0.4881 | 0.6776 | 0.8416 | 0.9402 | 0.9818 |
| $\lvert 1-r\rvert$ | 0.6523 | 0.5119 | 0.3224 | 0.1584 | 0.0598 | 0.0182 |
| sd at 1.5% noise | 43.5 | 34.1 | 21.5 | 10.6 | 4.0 | 1.2 |

Detectable at 3 sd: **0.5, 1, 2, 4 and 8 m**. Not detectable: **16 m**.
The 5%-change analogue of the lesson gives only 0.1 sd at 8 m, so a *small*
change is detectable only at the two shortest spacings — the conclusion is
scale-dependent, which is exactly why the expected magnitude of the change must
be stated before the array is designed.

---

## ★5 — The equivalence family

The constraint is $\left(S/S_0\right)^{n}\left(\rho_w/\rho_{w,0}\right) = r$ with
$n = 2$, $S_0 = 0.45$, $\rho_{w,0} = 10\ \Omega\,\mathrm{m}$,
$r = 0.2934$. Parameterising by the split $x$ of the log-ratio:
$\rho_w = 10\,r^{x}$ and $S = 0.45\,r^{(x-1)/2}$.

| $x$ | $\rho_w$ ($\Omega$ m) | $S$ | $\theta$ |
|---|---|---|---|
| 0.0 | 10.0000 | 0.8308 | 0.2908 |
| 0.5 | 5.4166 | 0.6115 | 0.2140 |
| 1.0 | 2.9340 | 0.4500 | 0.1575 |

Check each row forward through Archie, with $\phi^{-m} = 6.6171$:

- $x = 0$: $\rho = 10 \times 6.6171 \times 0.8308^{-2} = 10 \times 6.6171
  \times 1.4488 = 95.9\ \Omega\,\mathrm{m}$.
- $x = 0.5$: $\rho = 5.4166 \times 6.6171 \times 0.6115^{-2}
  = 5.4166 \times 6.6171 \times 2.6743 = 95.9\ \Omega\,\mathrm{m}$.
- $x = 1$: $\rho = 2.9340 \times 6.6171 \times 0.4500^{-2}
  = 2.9340 \times 6.6171 \times 4.9383 = 95.9\ \Omega\,\mathrm{m}$.

Every row reproduces the lesson's $95.8766\ \Omega\,\mathrm{m}$. ✔

One measurement that excludes the salinity member: **a water sample (or a
borehole conductivity log) from the interval**, giving $\rho_w$ directly. A
surface-NMR measurement of water content would exclude it independently, and a
second survey a few days later would resolve a moving front from a dispersing
plume.

---

## ★6 — A 4 m minimum spacing against a 0.5 m front

At $a = 4$ m the ratio for a 0.5 m front is 0.8416, so
$\lvert 1-r\rvert = 0.1584$ — **15.8 sd against 1% noise: the front is detectable**.
But detection is not the question a monitoring design has to answer. With a
single 4 m spacing, the measured ratio is a weighted average over a depth range
of order a few metres, and the *same* ratio can be produced by a thicker layer
with a smaller water-content change. The design cannot distinguish a shallow,
strong change from a deep, weak one, and it cannot report the depth of the front
at all.

What must be changed: **add spacings of the order of the target depth** (0.5 and
1 m here), and if the change is small (the 5% case), reduce the noise (repeat
stacking, better electrode contact, reciprocal measurements) rather than add more
long spacings.

---

## ★7 — Choosing the regularisation weight defensibly (specification)

**Metric.** The data misfit normalised by the stated data error,
$\chi^2(\alpha) = \frac{1}{N}\sum_i \left(d_i - (Gm_\alpha)_i\right)^2/\sigma_i^2$,
together with the model-resolution trace $\operatorname{tr}R(\alpha)$.

**Data needed.** (i) a defensible estimate of $\sigma_i$, from repeat surveys or
from reciprocal measurements; (ii) a set of candidate weights spanning at least
four orders of magnitude; (iii) *synthetic recovery tests*: the same survey
inverted for a suite of known models (a sharp front, a smooth front, a
two-interface model) to measure the bias each $\alpha$ induces.

**Procedure.** Choose the largest $\alpha$ whose $\chi^2$ remains within the
statistically acceptable band around 1 (the discrepancy principle), then check
that the synthetic tests show the recovered depth within an acceptable tolerance
for the sharpest model you are prepared to encounter. Report $\alpha$,
$\operatorname{tr}R(\alpha)$, the $\chi^2$ band and the bias measured on the
synthetic tests.

**Why the last step matters.** The lesson's $\alpha = 10^{-2}$ gives a data fit
within the noise and a $-16\%$ depth bias. A discrepancy-principle rule alone
would not have caught it; only the synthetic test does.

---

## ★8 — Rebuttal (model answer)

**(a)** The ratio data *do* constrain quantities, and they are often the ones of
interest: the presence and position of a change (the pattern across spacings in
Section 3.2), its total magnitude through the ratio at the shortest usable
spacing, its timing and rate (a time series), and — given one independent
constraint — the split between saturation and salinity. The equivalence is
between two *interpretations* of a measured quantity, not a statement that the
measurement is uninformative.

**(b)** The measurements that break it: pore-water chemistry (a sample, a
conductivity log, or a time-lapse salinity map), water content by surface NMR or
neutron probe, and a mass balance on any injected tracer. Each fixes one factor
of the product.

**(c)** A design where the ambiguity does not matter: **a controlled infiltration
experiment with a known, chemically neutral infiltrate** (for example, water from
the site's own supply, whose conductivity is measured). The pore-water
conductivity is then constrained by construction, the only remaining variable is
saturation, and the ratio data convert to water content with the stated Archie
parameters. The monitoring is legitimate; what is illegitimate is the *unstated*
transfer of the same interpretation to a site with an unknown salinity history.
