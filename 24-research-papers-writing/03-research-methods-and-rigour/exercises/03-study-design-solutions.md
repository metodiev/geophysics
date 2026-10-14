# Solutions — 24-03-03 Designing Studies

> Read after attempting. Numbers computed. Lesson:
> [03 Designing Studies](../03-study-design.md).

---

## ★1 — Sample size and its quadratic cost

For $d = 0.40$:

$$n = \frac{2(1.960 + 0.842)^{2}}{0.40^{2}}
= \frac{2 \times 7.849}{0.16} = 98.1 \approx 99\ \text{per group}.$$

For $d = 0.20$:

$$n = \frac{2 \times 7.849}{0.04} = 392.5 \approx 393\ \text{per group}.$$

$$\text{ratio} = \frac{392.5}{98.1} = 4.0 .$$

Halving the effect quadruples the sample, exactly as the $d^{2}$ denominator
implies. Units: $n$ is a count of units (stations, samples, sites).

---

## ★2 — Standard error and power at $n = 64$

$$\text{SE} = \sqrt{\frac{2}{n}} = \sqrt{\frac{2}{64}} = 0.1768,$$
$$\lambda = \frac{d}{\text{SE}} = \frac{0.50}{0.1768} = 2.828,$$
$$\text{power} = \Phi(\lambda - 1.96) + 1 - \Phi(\lambda + 1.96)
= \Phi(0.868) + 1 - \Phi(4.788) = 0.8073 + 0.0000 = 80.7\%.$$

The demonstration's simulation gives $81.0\%$, so the approximation is adequate.
Note that $n = 64$ is just above the analytic requirement of $62.8$: the design sits
right at the $80\%$ boundary, which is a fragile place to be, because a slightly
smaller true effect or a slightly larger noise level drops it well below.

---

## ★3 — Attenuation

$$\hat\beta_{\text{observed}} = \lambda\,\beta_{\text{true}}
= 0.75 \times 1.60 = 1.20 .$$

$$\text{bias} = \frac{1.20 - 1.60}{1.60} = -25.0\%.$$

The bias is systematic and survives any sample size. Reporting $1.20$ as the
physical sensitivity would understate the true relation by a quarter.

---

## ★4 — Marginal power per station

$$n = 64 \to 128:\quad \Delta\text{power} = 97.6 - 81.0 = 16.6\ \text{points},
\qquad \frac{16.6}{64} = 0.26\ \text{points per station}.$$

$$n = 128 \to 192:\quad \Delta\text{power} = 99.8 - 97.6 = 2.2\ \text{points},
\qquad \frac{2.2}{64} = 0.03\ \text{points per station}.$$

The marginal value falls by a factor of about $8$. Moving from $64$ to $128$
stations is worth $16.6$ points of power; the next $64$ stations are worth $2.2$.
Unless the effect size estimate is very uncertain, the third block of stations is
better spent reducing measurement noise or increasing the number of independent
sites.

---

## ★5 — Spurious slope from a $0.40$ confounder

With a common cause $z$ loading $0.40$ on both $x$ and $y$ and no direct effect,

$$\text{slope} \approx \frac{\text{cov}(x,y)}{\text{var}(x)}
= \frac{0.40 \times 0.40}{1} = 0.16 .$$

With a standard error of $0.07$, the $z$-statistic is

$$\frac{0.16}{0.07} = 2.29,$$

which exceeds $1.96$: the spurious association would be declared significant at
$n = 200$. The measured slope in the demonstration at loading $0.60$ is $+0.3585$,
consistent with the same arithmetic ($0.60^{2} = 0.36$). The lesson is that a
modest confounder loading is enough to produce a publishable result, which is why
the confounder list belongs in the design.

---

## ★6 — Correcting an attenuated slope

$$\hat\beta_{\text{corrected}} = \frac{\hat\beta_{\text{observed}}}{\hat\lambda}
= \frac{0.42}{0.60} = 0.70 .$$

The correction assumes that the measurement error is (a) additive and independent
of the true value, (b) independent of the outcome, and (c) of known variance,
estimated from repeated measurements or a validation subset. If the error is
multiplicative (a percentage of the true value) or correlated with the outcome, the
simple division is not valid, and the honest option is to report the attenuated
slope and state the direction and approximate size of the bias.

---

## ★7 — Detecting a $5\%$ velocity change

Two arrays with $n = 20$ stations each, per-station standard deviation $6\%$. The
standard error of the difference in array means is

$$\text{SE} = 6\% \times \sqrt{\frac{2}{20}} = 6\% \times 0.316 = 1.90\%.$$

The standardised effect is

$$d_{\text{std}} = \frac{5\%}{1.90\%} = 2.64,$$

giving power

$$\Phi(2.64 - 1.96) + 1 - \Phi(2.64 + 1.96)
= \Phi(0.68) + 1 - \Phi(4.60) = 0.7517 .$$

So the design has about $75\%$ power — close to but below the conventional $80\%$.

**What would fix it.** Three options, in increasing cost:

1. Add stations: $80\%$ power requires $\text{SE} = 5/2.80 = 1.79\%$, i.e.
   $n = 2(6/1.79)^{2} = 22.5$, so about $23$ stations per array — two more each.
2. Reduce per-station noise by longer recordings: SE scales as $1/\sqrt{\text{time}}$,
   so halving the noise needs four times the recording time.
3. Use a paired comparison (same sites reoccupied), which removes the between-site
   variance and can reduce the effective SE by a large factor; state how many sites
   can be reoccupied.

**Assumptions.** Independent stations with equal variance, Gaussian errors, no
spatial correlation between stations, and a pilot standard deviation that transfers
to the new arrays. The spatial-correlation assumption is the fragile one: if nearby
stations share an error, the effective $n$ is smaller than $20$ and the power is
lower than calculated.

---

## ★8 — Separating a confounded association

**Question.** Does the observed correlation between the depth of the water table
and the measured shear-wave velocity reflect a physical relation or a common
dependence on surface geology?

**Confounder list.** Surface geology class, elevation, seasonal timing of the
measurement, and measurement operator. Each is a plausible common cause: geology
affects both water-table depth and velocity; elevation affects both through soil
development; season affects water table and near-surface velocity; operator affects
processing choices.

**Measurement.** Geology from a published map at a stated scale (and its mapping
uncertainty), elevation from a quoted datum, season from the acquisition log, and
operator from the field records. Each variable must be recorded for every site,
which means the list must be settled before the survey.

**Identification assumption.** Conditional on the measured confounders, the
remaining variation in water-table depth is as good as random with respect to
unmeasured determinants of velocity. That is a strong assumption, and it is worth
stating in these words so that a reader can judge it.

**If a confounder is unmeasurable.** Use the pattern: report the association with
and without the measured confounders; compute an E-value-style bound (how strong an
unmeasured confounder would have to be, relative to the measured ones, to explain
the association away); and, if possible, find a subsample in which the unmeasured
variable is nearly constant, where the association can be estimated without it. The
sensitivity analysis is the deliverable, not a hedge: it converts "there may be
confounding" into a number a reader can weigh.
