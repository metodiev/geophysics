# Solutions — 25-01-02 Project: Mapping Global Seismicity from a Real Catalogue

> Read after attempting. Lesson:
> [02 Earthquake Map](../02-earthquake-map.md). All values are **SYNTHETIC**
> teaching numbers printed by
> [`code/earthquake_map_demo.py`](../code/earthquake_map_demo.py).

---

## ★1 — The mean magnitude step

$$\frac{1}{\beta} = \frac{1}{b \ln 10}
\qquad
b = 1.00:\ \frac{1}{2.302585} = 0.4343,
\qquad
b = 0.80:\ \frac{1}{1.842068} = 0.5429 .$$

The unit is a **magnitude unit** (magnitudes are logarithmic and conventionally
reported without a physical unit). A larger $b$ means a **steeper** decay: for
$b = 1$ each unit of magnitude multiplies the number of events by $10^{-1}$,
whereas for $b = 0.8$ it multiplies by $10^{-0.8} = 0.158$. So a larger $b$
means relatively more small events for the same number of large ones.

The demonstration measures $0.4341$ against the exact $0.4343$ — a $0.05\%$
deficit from the finite sample, which propagates directly into the $+0.0005$
offset in $\hat b$.

---

## ★2 — A b-value from a quoted mean

$$M_c - \frac{\Delta M}{2} = 3.5 - 0.05 = 3.45, \qquad
\overline{M} - 3.45 = 3.72 - 3.45 = 0.27,$$

$$\hat b = \frac{\log_{10} e}{0.27} = \frac{0.434294}{0.27} = 1.6085 .$$

Unit: dimensionless (both numerator and denominator are in magnitude units).
A value of $1.61$ is high for a regional compilation and would normally prompt a
check of the completeness assumption before a tectonic interpretation.

---

## ★3 — Standard errors and the discarded events

$$\sigma_b(N = 3000) = \frac{1.0005}{\sqrt{3000}} = \frac{1.0005}{54.772}
= 0.0183,$$

$$\sigma_b(N = 920) = \frac{0.9672}{\sqrt{920}} = \frac{0.9672}{30.332}
= 0.0319 .$$

Events discarded: $3000 - 920 = 2080$, i.e. **69.3%** of the catalogue. Note that
raising $M_c$ both moves the point estimate *and* inflates its uncertainty by a
factor of 1.74 — the second effect is the one usually omitted.

---

## ★4 — Sensitivity of b to Mc

$$\frac{\mathrm{d}b}{\mathrm{d}M_c} \approx
\frac{0.9672 - 1.0005}{4.5 - 4.0} = \frac{-0.0333}{0.5}
= -0.0666 \ \text{per magnitude unit}.$$

Extrapolated two units to $M_c = 5.0$:

$$\hat b(5.0) \approx 1.0005 + 2 \times (-0.0666) = 0.8673 .$$

The extrapolation is unsafe, and the reason is instructive: with a correctly
specified exponential the MLE is **unbiased at any** $M_c$, so the $-0.0333$
shift is mostly *sampling noise*, not a systematic trend. At $N = 920$,
$\sigma_b = 0.0319$, so the shift is $1.0\sigma$ — entirely consistent with zero.
A linear fit through two noisy points extrapolates the noise, and at
$M_c = 5.0$ the sample would be smaller still, with a correspondingly larger
$\sigma_b$. The honest statement in the report is "the estimate is stable to
within its uncertainty over this $M_c$ range", not "$b$ decreases by
$0.067$ per unit of $M_c$".

---

## ★5 — Choosing a map cell size

Total events within 2° of the line: $2319$ over a box of
$120° \times 120° = 14\,400\ \mathrm{deg^2}$.

$$\text{density} = \frac{2319}{14\,400}\ \text{per deg}^2
= 0.161\ \text{per deg}^2,$$

so a $5°\times5°$ box ($25\ \mathrm{deg^2}$) holds
$25 \times 0.161 = 4.03$ events, and a $1°\times1°$ box holds $0.161$ events.
The demonstration's $10°\times10°$ box holds $100 \times 0.161 = 16.1$ events,
matching its printed value.

**Choice.** A $5°\times5°$ box. At $1°$ most cells are empty (probability of zero
count $= e^{-0.161} = 0.851$), so the map would encode the sampling, not the
geology; at $10°$ the line and its surroundings merge into two blocks. Five
degrees gives about four counts per occupied cell — enough to show contrast and
still resolve the line's position to a few hundred kilometres. The cell size is
a stated part of the result.

---

## ★6 — A mixed magnitude scale

Adding $+0.2$ to 40% of the magnitudes raises the mean by
$0.4 \times 0.2 = 0.08$:

$$\overline{M}_{\text{bias}} = 4.3841 + 0.08 = 4.4641,$$

$$\hat b_{\text{bias}} = \frac{0.434294}{4.4641 - 3.95}
= \frac{0.434294}{0.5141} = 0.8448 .$$

Bias relative to $1.0005$:

$$\frac{0.8448 - 1.0005}{1.0005} = -15.6\%.$$

A 0.2-magnitude scale inconsistency on 40% of events moves $b$ by $-0.156$ —
**eight times** the statistical standard error of $0.0183$. This is the single
most common cause of an apparently significant regional $b$-anomaly, and it is
invisible in the frequency-magnitude plot because the two populations overlap.

---

## ★★★7 — A declustering experiment

**Rule and parameters.** Use a windowing decluster (Gardner–Knopoff type): a
mainshock is an event larger than every event in the preceding $T_1$ and
following $T_2$ seconds within a distance $L$, with
$T_1 = 10\ \text{d}$, $T_2 = 20\ \text{d}$ and $L = 50\ \mathrm{km}$ — the
conventional values, stated explicitly because the result depends on them. Report
the rule's parameters in the caption.

**Two statistics.**

1. The **$b$-value**, because aftershock sequences are drawn from the same
   Gutenberg-Richter population as their mainshock *at the time of the
   sequence*, so removing them changes the weights of large events relative to
   small ones. Expect $b$ to move by up to a few hundredths.
2. The **event count and its time distribution**, because a declustered
   catalogue is what a Poisson recurrence model needs; the residual clustering
   shows up as variance in the annual count.

**Separating declustering from the $M_c$ effect.** Hold $M_c$ fixed at the value
estimated on the *declustered* catalogue, then apply it to both catalogues; the
completeness of a declustered catalogue differs from the raw one because removing
aftershocks removes many small events. Estimate $M_c$ first on each catalogue and
report both, so the two effects are not confounded.

**Decision rule.** Declustering changes the answer materially if it moves $b$ by
more than $\sigma_b^{\text{raw}}$ or if the annual counts cease to be
over-dispersed. With the real ComCat catalogue over a decade and $N$ of order
$10^{4}$, $\sigma_b \approx 0.01$, so a shift of more than $0.01$ is the
criterion — and any published $b$-value that omits the declustering choice should
be read with that tolerance attached.
