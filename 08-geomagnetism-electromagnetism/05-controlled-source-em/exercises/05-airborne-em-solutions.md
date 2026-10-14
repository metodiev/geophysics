# Solutions — 08-05-05 Airborne EM for Conductivity Mapping

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [05 Airborne EM](../05-airborne-em.md).

---

## ★1 — Height factor at 25 m

$$\frac{r}{\sqrt{r^2+4h^2}}=\frac{8}{\sqrt{64+4\times625}}
=\frac{8}{\sqrt{2564}}=\frac{8}{50.636}=0.1580.$$

As a loss: $1-0.1580=84.2\%$ of the signal lost, or in decibels
$20\log_{10}0.1580=-16.03\ \mathrm{dB}$.

**Check the asymptotics:** for $h\gg r$ the factor tends to $r/(2h)=0.16$ here,
so at $25\ \mathrm{m}$ the approximation is already within $1.3\%$ of the exact
value. The $(2h/r)$ growth of the loss is why doubling flight height roughly
halves the signal, and why height is quoted in metres on every survey report.

---

## ★2 — Conductivity error from 1 m of height error

From the lesson's table at $1.6\ \mathrm{kHz}$:

| height (m) | equivalent conductivity change per metre |
|---|---|
| 20 | 9.62% |
| 40 | 7.31% |
| 60 | 6.59% |

The three are within $50\%$ of each other and decrease slowly with height: the
trade-off is *not* proportional to the signal loss, because the conductivity
sensitivity also falls with height. That is why the height problem cannot be
solved by flying lower (which reduces the absolute error very slowly) but only by
measuring height better.

---

## ★3 — Masking by 8 S of cover

From the masking table, a cover of conductance $8\ \mathrm{S}$ (e.g. $0.2\
\mathrm{S\,m^{-1}}$ over $40\ \mathrm{m}$) leaves $0.223$ of the target's anomaly —
about a fifth. Ten times the stacking improves the signal-to-noise by
$\sqrt{10}=3.2$ but **does not change the fraction $0.223$**: the cover attenuates
signal and target together, so the target's contribution remains one fifth of what
the receiver sees. The remedy is to change the *response*, not the averaging: use
a higher frequency (which weights the cover more heavily and the deep target less
— often unhelpful), a different geometry, or accept and report the conductance.

---

## ★4 — Deriving the height factor

Start from the layered response (lesson 08-05-03 §2.3)

$$S(\omega,h)=-r^3\left[\frac{R_\infty}{\sqrt{r^2+4h^2}}
+\int_0^\infty\left(\lambda^2R-R_\infty\right)e^{-2\lambda h}
J_0(\lambda r)\,\mathrm{d}\lambda\right],$$

where $R_\infty=\lim_{\lambda\to\infty}\lambda^2R(\lambda)$ is a constant. For a
homogeneous ground $R=-k^2/(\lambda+u)^2$ with $u=\sqrt{\lambda^2+k^2}$, so
$\lambda^2R\to-k^2/4$ and $R_\infty=-k^2/4$. The first term is then

$$\frac{R_\infty}{\sqrt{r^2+4h^2}}=\frac{-k^2}{4\sqrt{r^2+4h^2}},$$

using $\int_0^\infty e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda
=1/\sqrt{(2h)^2+r^2}$ — the identity quoted. Multiplying by $-r^3$ and writing
$k^2=i\omega\mu_0\sigma$,

$$S_{\text{first term}}=\frac{k^2r^3}{4\sqrt{r^2+4h^2}}
=\frac{k^2r^2}{4}\cdot\frac{r}{\sqrt{r^2+4h^2}}
=S_{\text{LIN}}(h=0)\times\frac{r}{\sqrt{r^2+4h^2}},$$

which is the boxed factor of the lesson. The second (integral) term is the
correction; it also carries $\exp(-2\lambda h)$ and therefore also decays with
height, which is why the full response falls faster than the factor alone at
higher induction numbers — the $1\ \mathrm{kHz}$ column of the lesson's table.

---

## ★5 — Frequencies usable with a $0.5\ \mathrm{m}$ altimeter

Requirement: trade-off $\times0.5\ \mathrm{m}<5\%$, i.e. trade-off $<10\%$ per
metre. From the table ($\sigma=0.05\ \mathrm{S\,m^{-1}}$):

| frequency | at 20 m | at 60 m | acceptable? |
|---|---|---|---|
| 400 Hz | 7.29% | 4.08% | yes, both heights |
| 1.6 kHz | 9.62% | 6.59% | marginal at 20 m (4.8% error), yes at 60 m |
| 6.4 kHz | 14.40% | 12.30% | no |
| 25.6 kHz | 24.97% | 25.54% | no |

So with a $0.5\ \mathrm{m}$ altimeter the survey can quote conductivity to better
than $5\%$ only at and below about $1.6\ \mathrm{kHz}$, and only if the height
error is uncorrelated with position. Interpolating between $400\ \mathrm{Hz}$
and $1.6\ \mathrm{kHz}$ suggests a practical ceiling near $2\ \mathrm{kHz}$ at
$60\ \mathrm{m}$ flight height. **The higher channels are still useful** — for
detecting, not for quantifying: a $20\%$ height-driven bias still leaves a
recognisable anomaly.

---

## ★6 — A $2\ \mathrm{S}$ sheet at 120 m depth

From the depth-of-investigation table at $120\ \mathrm{m}$:

| channel | relative anomaly |
|---|---|
| 100 Hz | 27.08% |
| 400 Hz | 18.66% |
| 1.6 kHz | 7.26% |
| 6.4 kHz | 0.96% |
| 25.6 kHz | 0.21% |
| 100 kHz | 0.46% |

The best channel *in the table* is $100\ \mathrm{Hz}$ with $27\%$, and the
$400\ \mathrm{Hz}$ channel — the lowest in the hypothetical system — gives $19\%$.

**Can a $400\ \mathrm{Hz}$-limited system see it?** Yes for *detection*: a $19\%$
relative anomaly is far above any reasonable noise floor. But the comparison with
the $100\ \mathrm{Hz}$ value ($27\%$) shows the system is on the wrong side of the
optimum, so its estimates of depth and conductance will be biased and strongly
correlated: the $400\ \mathrm{Hz}$ response to a deep target is largely degenerate
between "shallower and more resistive" and "deeper and more conductive", the
conductance–depth ambiguity of lesson 08-05-03 §5. The honest answer is:
detectable, not quantitatively resolvable, and a system with a channel near
$100\ \mathrm{Hz}$ would be the cheapest improvement.

---

## ★7 — Levelling and QC against a height-correlated bias

**Geometry.** Straight, evenly spaced flight lines at the designed spacing, plus
**tie lines** perpendicular to them at roughly five to ten times the spacing.
Record the radar and laser altimeters, the bird's attitude, and the position
independently for every sounding.

**Statistics to monitor.** For each flight line $i$ and each channel $j$: the
median and the interquartile range of the apparent conductivity, the median
height, and the slope of a regression of apparent conductivity against height
*within* the line (a within-line slope of conductivity on height is the direct
fingerprint, because the geology does not know the bird's height).

**Procedure.** (1) Invert every sounding including height as a free parameter with
a prior from the altimeter. (2) Compute the within-line regression slope
$\partial\sigma_{\text{app}}/\partial h$ per channel and compare it with the
theoretical trade-off of the lesson's Section 3 (sign and magnitude). (3) Compute
the line-mean misfit between the levelled conductivity and the tie-line
conductivity, and regress that misfit against the line's mean height. (4) Inspect
the residuals for spatial correlation at the footprint scale.

**Null result giving confidence.** The measured within-line slope matches the
theoretical trade-off within its statistical error, the tie-line misfit shows no
significant dependence on height, and the residual line-to-line bias is smaller
than the pixel-level uncertainty. The theoretical trade-off being *known* is what
makes this a test rather than a plausibility argument.

**Alternative explanations for a positive result.** (1) Real geology varying with
topography (conductive valley fill, clay-rich lowlands) — the most common false
positive, testable by comparing the sign of the effect across terrain types;
(2) a genuine height-dependent system response (bird attitude, transmitter
coupling) that mimics an altimeter error; (3) levelling or drift in the base
station; (4) footprint effects where the conductive structure is narrower than the
support. Distinguishing (1) from the others requires the raw (unlevelled) data
plus independent geology.

---

## ★8 — Distinguishing $0.05$ from $0.02\ \mathrm{S\,m^{-1}}$ at 80 m under a 20 S cover

**Scale analysis.** Three separate specifications are packed into the request:

1. **A conductivity contrast of $0.05$ vs $0.02\ \mathrm{S\,m^{-1}}$** — a factor
   of $2.5$, i.e. $0.4$ in $\log_{10}$. From the trade-off table at
   $1.6\ \mathrm{kHz}$, reaching this requires a height accuracy of
   $0.4/0.0731=5.5\ \mathrm{m}$; at $6.4\ \mathrm{kHz}$ it requires $0.4/0.1257
   =3.2\ \mathrm{m}$. So the contrast is *plausible* with any altimeter better
   than a few metres, provided the section is layered.
2. **At $80\ \mathrm{m}$ depth.** From the depth-of-investigation table, an $80\
   \mathrm{m}$ target sits between the $60\ \mathrm{m}$ and $120\ \mathrm{m}$ rows:
   the relative anomaly at $1.6\ \mathrm{kHz}$ is of order $20\%$, at
   $6.4\ \mathrm{kHz}$ of order $5\%$. Detectable, and the channel carrying the
   most information is near $400\ \mathrm{Hz}$–$1.6\ \mathrm{kHz}$. **A system
   must therefore have channels in that band.**
3. **Under a $20\ \mathrm{S}$ cover.** This is the fatal one. The masking table
   shows a $20\ \mathrm{S}$ cover passes $0.050$ of the target's anomaly: a $20\%$
   relative anomaly becomes $1\%$. Distinguishing the $2.5\times$ contrast inside
   a $1\%$ signal requires the noise floor to be below $0.4\%$ of the total
   response — plausible for the *detection* of the conductor, implausible for a
   quantitative conductivity, and hopeless if any part of that cover's
   conductance is unknown (since it trades against the target's).

**Verdict.** Specifications 1 and 2 are plausible with a low-frequency-channel
system and a good altimeter; specification 3 is not deliverable by processing.

**Cheapest improvement.** Not more frequency channels and not more stacking: the
limiting term is the cover's conductance. The cheapest changes that genuinely
help are (a) a **larger source moment and a lower-frequency channel** (a bigger
loop at $100$–$400\ \mathrm{Hz}$ buys depth of investigation directly), and (b)
**line spacing matched to the footprint** at $40\ \mathrm{m}$ height, so that the
budget is spent on coverage at the resolution actually achievable rather than on
oversampled lines. If the cover's conductance must be known, a single
ground-based TEM sounding on it will cost less than any airborne re-flight.
