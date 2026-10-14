# Solutions — 21-02-04 Conditional Simulation and Uncertainty Realisations

> Read after attempting. Lesson:
> [04 Conditional Simulation](../04-simulation-geostatistics.md). Numbers quoted
> from the demonstration reproduce its output.

---

## ★1 — Monte-Carlo error of an ensemble variance

$$\mathrm{RSE}(s^{2}) = \sqrt{\frac{2}{L}}, \qquad
\mathrm{RSE}(s) \approx \frac{1}{\sqrt{2L}} .$$

- $L = 200$: $\sqrt{2/200} = \sqrt{0.01} = 0.1000$, i.e. $10.0\ \%$ on the
  variance and $1/\sqrt{400} = 5.0\ \%$ on the standard deviation.
- $L = 1000$: $\sqrt{2/1000} = 0.0447$, i.e. $4.5\ \%$ on the variance and
  $2.2\ \%$ on the standard deviation.

The variance is the noisier target, which is why a study reporting *spread*
rather than variance can get away with fewer realisations than one reporting
variance components.

---

## ★2 — The smoothing ratio

$$\frac{\text{Var}(E\text{-type})}{s^{2}_{\text{ens}}} = \frac{0.3138}{0.5022}
= 0.6249 \approx 62.5\ \% .$$

The ratio measures how much of the field's spatial variability survives the
averaging that turns an ensemble into a conditional mean. A ratio of $1$ would
mean the estimate is as variable as a single realisation — which happens only
when the data determine the field completely. A ratio near $0$ means the
estimate is nearly flat. At $62.5\ \%$ the demonstration's estimate is
substantially smoother than reality but far from flat, and the missing $37.5\ \%$
is exactly the texture that a resource or flow model needs and that an E-type map
cannot supply.

---

## ★3 — Exceedance probability and its uncertainty

$$\hat p = \frac{30}{200} = 0.150, \qquad
\mathrm{se}(\hat p) = \sqrt{\frac{\hat p(1-\hat p)}{L}}
= \sqrt{\frac{0.15\times0.85}{200}} = \sqrt{0.0006375} = 0.0252 .$$

The estimate is $p = 0.150 \pm 0.025$, i.e. $15\ \% \pm 2.5\ \%$ at one standard
error. Realisations are independent, so the binomial form applies directly; the
reported uncertainty is a Monte-Carlo error on top of the model uncertainty, and
it shrinks as $1/\sqrt L$ — four times as many realisations would halve it.

---

## ★★4 — Properties of the error-simulation identity

Let $Z_k$ and $Z_{uk}$ be the kriging estimates from the data of the true field
and of an unconditional simulation $Z_u$ with the target covariance.

**Honouring the data.** At a data location $x_j$, kriging is an exact
interpolator, so $Z_k(x_j) = z_j$ and $Z_{uk}(x_j) = Z_u(x_j)$ (the same kriging
weights applied to the simulation reproduce its value at the datum). Therefore

$$Z_{cs}(x_j) = z_j + \big[Z_u(x_j) - Z_u(x_j)\big] = z_j .$$

The bracket vanishes at every datum, and the realisation passes through the data.

**Correct conditional mean.** Conditional on the data, $Z_k$ is a deterministic
function of the data and $Z_u$ is independent of the data (it is an
unconditional draw). Taking expectations,

$$\mathbb E[Z_{cs} \mid \text{data}] = Z_k + \mathbb E[Z_u] -
\mathbb E[Z_{uk} \mid \text{data}] = Z_k + 0 - 0 = Z_k ,$$

since both $Z_u$ and its kriging estimate have zero mean (kriging of a zero-mean
field is unbiased with expectation zero). The realisation's conditional mean is
therefore the kriging estimate, and its conditional covariance is that of the
kriging error — the two properties a conditional simulation must have.

---

## ★★5 — Realisations for a $2\ \%$ variance target

$$\mathrm{RSE} = \sqrt{\frac{2}{L}} \le 0.02
\;\Longrightarrow\;
L \ge \frac{2}{0.02^{2}} = \frac{2}{0.0004} = 5000 .$$

So $5000$ realisations are needed for a $2\ \%$ relative precision on a variance,
against the demonstration's $200$ for $10\ \%$. The cost is linear in $L$ for
SGS, so this is a $25$-fold increase in run time.

**A confidence interval is a different target.** A $95\ \%$ interval on
exceedance probability or on a percentile requires the *tails* of the ensemble
distribution to be resolved, which needs more than the variance; sampling error
in a $95$th percentile is roughly $\sqrt{p(1-p)/L}/f(q_p)$, and because the
density $f$ at the $95$th percentile is small, the requirement is typically
several times larger than the $5000$ the variance needs. Design for the
percentile, not the variance, if the deliverable is a risk map.

---

## ★★6 — Why the E-type estimate is smoother, and what more data does

The E-type estimate is an average of $L$ fields that share a common conditional
mean and differ by zero-mean kriging errors. Spatially, the conditional mean is
the projection of the field onto the space of functions the data can resolve, so
it contains only the wavelengths the data support; the components the data cannot
resolve are present in individual realisations but cancel in the average. Hence
the E-type estimate's spatial variance is smaller than the mean realisation
variance, by the $62.5\ \%$ measured.

**With forty conditioning data instead of four**, the data resolve shorter
wavelengths, so the conditional mean becomes closer to the true field. The true
field is spiky (it has a total variance of about $1$ here), so the E-type
estimate's spatial variance **increases** towards the field variance, and the
ratio rises towards $1$. Equivalently, more data reduce the kriging variance,
which reduces the difference between the estimate and a realisation.

---

## ★★★7 — Connectivity study

**Grid.** A $100\times100\times50$ cell model at $1\ \mathrm m$ resolution.

**Field construction.** Simulate indicator fields above a threshold by
truncating a Gaussian field generated from a spherical covariance with range
$a \in \{5, 10, 20, 40\}$ cells; $200$ realisations per range.

**Connectivity metric.** The fraction of the total volume above the threshold
that belongs to the largest connected component, evaluated with a six-connected
flood fill from the base of the model; also the shortest-path length across the
model.

**Prediction.** As the range grows the field becomes more organised, so the
largest connected cluster grows and the metric rises steeply — typically from
near $0$ at a range comparable to the cell size to above $0.8$ at a range of a
tenth of the model dimension. The study's headline is the connected fraction
against range and its ensemble spread, and the finding to report is that the
metric is **not** a function of the threshold alone: two fields with identical
proportions above the cut-off can differ by an order of magnitude in connected
volume.

---

## ★★★8 — Convergence of the ensemble mean

**Metric.** $\displaystyle D(L) = \frac{1}{n}\sum_{x}
\big[\hat Z^{(L)}(x) - Z_k(x)\big]^{2}$, the mean squared difference between the
ensemble mean of $L$ realisations and the kriging estimate; normalised by the
mean kriging variance, it should fall as $1/L$.

**Tolerance.** Require the normalised $D(L) \le 0.01$, i.e. the ensemble mean
within $10\ \%$ of the kriging standard deviation.

**Design.** Conditioning sets of $4$, $10$, $20$ and $40$ data on the $50$-node
grid; $L$ swept over $\{50, 100, 200, 400, 800, 1600, 3200\}$; $M = 100$
independent outer replicates so that $D(L)$ has a reported scatter.

**Predicted scaling.** Because each realisation has the conditional covariance of
the kriging error, $\mathbb E D(L) = \frac{1}{L}\,\overline{\sigma^{2}_K}$, so
$D(L)\propto 1/L$ and the number of realisations needed scales as
$1/(L)$ independent of the conditioning count — but the *absolute* requirement
scales with the mean kriging variance, which is larger with four data than with
forty. The study's headline is the constant of proportionality as a function of
the conditioning count.
