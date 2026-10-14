# Solutions — 16-08-02 Reanalysis: ERA5, MERRA, JRA and Their Caveats

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand; the arithmetic is shown.

Lesson: [02 Reanalysis: ERA5, MERRA, JRA and Their Caveats](../02-reanalysis-products.md).

---


## ★ Foundational

## ★1 — One analysis step

$$K = \frac{B}{B+R} = \frac{0.04}{0.04+0.01} = 0.800.$$

$$x^{a} = x^{b} + K\left(y - x^{b}\right) = 1.0 + 0.8\,(1.5-1.0)
= \mathbf{1.40\ K}.$$

$$B^{a} = (1-K)B = 0.2 \times 0.04 = \mathbf{0.008\ K^{2}}.$$

The analysis is $80\%$ of the way from the background to the observation, because
the observation is four times more precise than the background. The analysis
variance is five times smaller than the background variance — the observation
added information.

---

## ★2 — The two model-dominated limits

- $R \to \infty$: the observation is useless, $K = B/(B+R) \to 0$, and
  $x^{a} \to x^{b}$ — the analysis is the model forecast.
- $B \to 0$: the model is believed perfect, $K \to 0$, and $x^{a} \to x^{b}$ —
  again the analysis is the model forecast.

The two limits are the same failure because $K$ depends on the **ratio** $B/R$, not
on either alone. Treating your model as perfect and treating your observations as
worthless produce identical behaviour: the product is a simulation, and no
observational information enters. This is why a reanalysis is only as good as its
stated error covariances — not only as good as its model or its data.

---

## ★3 — Steady-state background variance

$$B^{b}_{\infty} = \frac{Q}{1-\varphi^{2}} = \frac{0.0025}{1-0.49}
= \frac{0.0025}{0.51} = 0.004902\ \mathrm{K^{2}},$$

$$\sqrt{B^{b}_{\infty}} = 0.0700\ \mathrm{K}.$$

Without observations the product settles at the model's own variability, which is
the model's internal climate, not the observed one.

---

## ★★ Applied

## ★★4 — Steady-state analysis bias

$$\text{bias} = \frac{(1-K)(c_{\text{model}}-c_{\text{truth}})}{1-\varphi(1-K)}
= \frac{0.5\,(-0.10-0.05)}{1-0.70\times0.5}
= \frac{-0.075}{0.65} = -0.1154\ \mathrm{K}.$$

The sign is **negative**: the analysis is biased cold, toward the model's colder
climate. Two features matter. First, the bias is *not* removed by the observations
unless $K = 1$ — a fraction of the model bias survives the update. Second, the
bias is smaller than the full $0.25\ \mathrm{K}$ climate-mean difference
$(0.15/(1-\varphi)$ in the state, $0.5\ \mathrm{K})$ because the observations pull
the analysis part of the way. A large $K$ reduces the residual bias: at $K = 0.9$,
$\text{bias} = 0.1(-0.15)/(1-0.07) = -0.0161\ \mathrm{K}$. This is the quantitative
statement of "the analysis is a weighted compromise".

---

## ★★5 — Apparent trend from a discontinuity

$$\delta(\text{trend}) = \delta_{\text{jump}}\,
\frac{\sum_{t\ge30}(t-\bar t)}{\sum_t(t-\bar t)^{2}}
= 0.40 \times \frac{450}{17{,}995}
= 0.40 \times 0.02501 = \mathbf{0.01000\ \mathrm{K\,yr^{-1}}}.$$

A $0.40\ \mathrm{K}$ level change at the record centre appears as a trend of
$0.010\ \mathrm{K\,yr^{-1}}$ — which is the same order as the trends that
reanalysis products are used to quantify. **A discontinuity and a trend are
degenerate in a linear fit**, and the observing-system history is the only thing
that can break the degeneracy.

---

## ★★6 — Spread versus error

$$\text{ratio} = \frac{0.10}{0.40} = 0.250.$$

The spread covers the model's **internal** (random, within-climate) uncertainty
and the analysis's own estimation error, but it does not contain the model's
**climate bias** — the systematic offset between the model's climatology and
reality. Averaging more members cannot reduce a bias that every member shares, so
the ensemble spread converges to a number that is too small, and a sparse-era
product can be confidently wrong.

---

## ★★★ Research-oriented

## ★★★7 — Distinguishing a product artefact from a trend (design)

**Diagnostic: the innovation trend.** For each observing-system sub-period, compute
the mean of the innovation $\mathbf{y}-\mathbf{H}\mathbf{x}^{b}$ (normalised by its
expected standard deviation) and test whether it drifts across the record. If the
model were unbiased and the error covariances correct, the innovations would be
zero-mean and serially uncorrelated with the observing-system schedule. A
systematic drift of the innovations *across* an observing-system change is direct
evidence that the analysis is being pulled from one climate toward another.

**Null hypothesis.** $H_0$: the normalised innovations have zero mean in every
sub-period, and their mean does not change across observing-system boundaries
(a two-sample test on the innovations with a serial-correlation-robust standard
error).

**Complementary diagnostics.** (i) Re-run the trend over a sub-period with stable
observing coverage; (ii) compare with an independent homogenised station product;
(iii) perturb $\mathbf{B}$ and $\mathbf{R}$ within plausible ranges and check the
trend's stability.

**When the two remain indistinguishable.** They are indistinguishable when the
observing-system change and the true trend have the same functional shape — for
example a monotone increase in data density over exactly the period in which the
climate trend is suspected. In that case the design cannot separate them, and the
honest conclusion is that this product alone cannot establish the trend; an
independent record with a different observing history is required. Stating that
boundary, rather than choosing the more convenient explanation, is the deliverable.

---

## ★★★8 — Correlated errors across products

Response:

> "Agreement between two reanalyses is not confirmation, because the two products
> are not independent. They assimilate largely the same observations — the same
> radiosonde network, the same satellite radiances — and they belong to the same
> class of physical models, with similar parameterisations and similar
> observational bias-correction techniques. Their errors therefore share a large
> common component: a common observing-system change, a common satellite bias, or
> a common model bias will appear in both, and the fact that both show it is
> evidence about the inputs they share, not about the atmosphere. The homogenised
> station product, built from a different data stream with different bias
> handling, is arguably the more informative disagreement here. What is needed
> is a common error model quantifying the shared component, not a vote among
> products."

Synthetic experiment to measure the shared component:

1. Build two "analysis systems" $A$ and $B$ with different models
   (different $\varphi$, $Q$, biased forcing terms) but **the same observing
   stream** — the same synthetic stations, with the same shared biases, and the
   same observation-error magnitudes.
2. Run both against a known truth, over a schedule with an observing-system
   change.
3. Measure (i) each system's error correlation with the truth, (ii) the
   correlation of the two systems' errors with *each other*, and (iii) how the
   apparent "agreement" between $A$ and $B$ changes when the two are given
   independent observing streams instead of a shared one.
4. Report the fraction of the $A$–$B$ agreement that survives when the observing
   streams are made independent. That surviving fraction is an upper bound on how
   much of the real products' agreement could be evidence about the atmosphere;
   the difference measures how much was shared-input agreement.

A result in which the $A$–$B$ agreement collapses when the streams are made
independent demonstrates that product-to-product agreement is, in that setting,
evidence about shared observations rather than about truth.
