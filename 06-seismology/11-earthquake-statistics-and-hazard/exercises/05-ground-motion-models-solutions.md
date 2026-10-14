# Solutions — 06-11-05 Ground-Motion Prediction Equations and Their Uncertainty

> Read after attempting the exercises. Numbers were computed with the formulas of
> the lesson. All values are **SYNTHETIC**.

Lesson: [05 Ground-Motion Models](../05-ground-motion-models.md).

---

## ★1 — a median value

$$\ln \hat z = 1.411 + 0 + (-1.30)\ln(35) = 1.411 - 1.30\times3.55535
= 1.411 - 4.6220 = -3.2110,$$
$$\hat z = e^{-3.2110} = 0.0403\ \mathrm{g}.$$

Per magnitude unit the median is multiplied by $\exp(1.00) = 2.718$.

---

## ★2 — scatter decomposition

$$\tau^2 = \sigma_\text{total}^2 - \sigma_\varepsilon^2
= 0.65^2 - 0.52^2 = 0.4225 - 0.2704 = 0.1521,$$
$$\tau = \sqrt{0.1521} = 0.390.$$

Between-event fraction of the variance:
$0.1521/0.4225 = 0.360$, i.e. 36%. So a scenario analysis of the *median* of the
next event carries an uncertainty of 0.39 in $\ln IM$ — the within-event 0.52 has
already been averaged out over the records of one event.

---

## ★3 — mean versus median

$$\frac{\mathrm{mean}}{\mathrm{median}} = e^{\sigma^2/2} = e^{0.64/2} = e^{0.32}
= 1.377.$$

The mean exceeds the median by 37.7%. At $\sigma = 0.6$ the same factor is 1.197
(19.7%); the gap grows rapidly with $\sigma$, which is why the distinction matters
most for the poorly constrained intensity measures.

---

## ★4 — the effect of $\sigma$ on a tail probability

$$\ln \frac{0.4}{0.1376} = \ln 2.9070 = 1.0672.$$

For $\sigma = 0.60$: argument $= 1.0672/0.60 = 1.7787$,
$\Phi = 0.9624$, so $P = 0.0377$.

For $\sigma = 0.80$: argument $= 1.0672/0.80 = 1.3340$, $\Phi = 0.9089$, so
$P = 0.0911$.

Ratio: $0.0911/0.0377 = 2.42$.

A hazard calculation adopting $\sigma = 0.60$ when the true scatter is 0.80 would
**understate** the rate of exceeding $0.4\ \mathrm{g}$ by a factor of 2.4 at this
scenario — and the discrepancy grows as the threshold moves further into the tail.
The mechanism is the one derived in Section 5 of the lesson:
$\partial P/\partial\sigma = \varphi(d/\sigma)\,d/\sigma^2 > 0$ for $d>0$.

---

## ★5 — epistemic uncertainty of the median

$$\frac{\sigma}{\sqrt n} = \frac{0.60}{\sqrt{50}} = \frac{0.60}{7.071} = 0.0849.$$

For a standard error of 0.05:

$$\sqrt n = \frac{0.60}{0.05} = 12 \;\Longrightarrow\; n = 144 \text{ records}.$$

Note what this does *not* buy: the aleatory scatter remains 0.60 per record. The
144 records sharpen the model's median, not the next earthquake's ground motion.

---

## ★6 — divergence of two fits outside the data range

Model A: $\ln PGA = 1.0091m - 8.8194$.
Model B: $\ln PGA = 5.2615\ln m - 12.2224$.

| $M$ | A: $\ln PGA$ | A: PGA (g) | B: $\ln PGA$ | B: PGA (g) | ratio A/B |
|---|---|---|---|---|---|
| 6.0 | $-2.765$ | 0.0629 | $-2.796$ | 0.0610 | 1.03 |
| 7.5 | $-1.251$ | 0.2863 | $-1.621$ | 0.1976 | 1.45 |
| 8.0 | $-0.746$ | 0.4744 | $-1.281$ | 0.2776 | 1.71 |

(The $M8.0$ row reproduces the demonstration's printed values to the last digit
quoted there.)

The ratio grows from 1.03 inside the data range ($M4.5$–$M6.0$) to 1.71 at $M8.0$.
**What this demonstrates:** the data cannot arbitrate between the two forms because
inside the range they agree to within the observational scatter (0.02 in
$\ln PGA$); the divergence is produced entirely by the extrapolation. Any hazard
statement that depends on $M8$ shaking therefore contains a model choice that no
additional in-range data can settle, and it must be carried as epistemic
uncertainty rather than hidden inside a "best fit".

---

## ★7 — measuring the magnitude dependence of $\sigma$

**Design.** Assemble a dataset with many records per event, spanning at least three
magnitude decades with adequate distance coverage. Estimate the event terms $\eta_i$
and within-event residuals $\varepsilon_{ij}$ by the standard two-stage procedure
(regress the event means on the median relation; the residual of the event mean is
$\hat\eta_i$), then:

- $\sigma_\varepsilon(m)$: bin events by magnitude and compute the RMS of
  $\varepsilon_{ij}$ in each bin, with bootstrap intervals;
- $\tau(m)$: compute the s.d. of $\hat\eta_i$ corrected for the estimation error of
  each event mean ($\sigma_\varepsilon/\sqrt{n_i}$);
- test for trend with a likelihood-ratio comparison between constant and
  magnitude-dependent $\sigma$; report the profile likelihood.

**Algebra of the effect on hazard.** The hazard integrand carries
$P(IM > z \mid m,r) = 1 - \Phi[\ln(z/\hat z)/\sigma(m)]$. For a threshold above the
median, $P$ increases with $\sigma$ at fixed $(m,r)$. Splitting the magnitude
integral into a small-magnitude part (where $\sigma$ is typically larger) and a
large-magnitude part:

- a larger $\sigma$ in the *small-magnitude* bins raises their contribution to the
  hazard at high thresholds, so a constant-$\sigma$ model that uses the
  large-magnitude value **understates** the contribution of the numerous small
  events;
- a smaller $\sigma$ at *large* magnitudes lowers their contribution, partially
  offsetting the first effect.

The net direction depends on the relative sizes of the two effects and on the
threshold, so the honest answer is a computation, not a slogan: the study must
report $\lambda(z)$ for the constant- and variable-$\sigma$ models over the design
range, and the difference is the effect being measured.

**Control:** verify that both models reproduce the observed residuals equally well
(for example by a likelihood-ratio test) so that the comparison is between two
defensible descriptions, not between a model and a misspecification.

---

## ★8 — one record, one inversion, and what to do about it

**The posterior uncertainty with one record.** Inverting a single record for layer
thickness means treating it as an observation of $\ln IM$ whose residual has
standard deviation $\sqrt{\sigma_\varepsilon^2 + \tau^2} = \sqrt{0.5^2 + 0.35^2}
= \sqrt{0.25+0.1225} = \sqrt{0.3725} = 0.610$. Mapping that to thickness requires
the sensitivity $\partial \ln IM/\partial H$ of the observable to the parameter of
interest: if the medium amplifies with a logarithmic sensitivity
$k = \partial\ln IM/\partial H$ per metre, the posterior standard deviation of $H$
is $0.610/k$ metres. With only one record there is nothing to average: the estimate
inherits the full aleatory scatter.

**Programme that reduces it most per unit cost.** Ranked by information per unit
cost:

1. **More records of the same event at the same station** — this reduces the
   within-event component only, at a rate $1/\sqrt{n}$, with the cheapest
   incremental cost (the station already exists). It removes
   $\sigma_\varepsilon/\sqrt n$ from the uncertainty.
2. **The same station with several events** — this reduces the event component
   $\tau$, which more records of one event cannot touch. Needed once
   $\sigma_\varepsilon/\sqrt n < \tau$.
3. **A second station at a different azimuth** — reduces the component common to a
   single path (directivity, site 3D structure) that neither of the first two can
   address, and its cost is the highest of the three.

The design conclusion: alternate between (1) and (2) until
$\sigma_\varepsilon/\sqrt n \approx \tau$, then spend on (3). Spending everything
on (1) leaves the estimate pinned at $\tau/k$, which is the floor of the method.
