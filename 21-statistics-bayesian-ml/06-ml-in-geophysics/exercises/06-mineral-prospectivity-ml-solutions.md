# Solutions — 21-06-06 ML for Mineral Prospectivity Mapping

> Read after attempting. Lesson:
> [06 Mineral Prospectivity](../06-mineral-prospectivity-ml.md). Values are
> **SYNTHETIC**, printed by
> [`code/mineral_prospectivity_ml_demo.py`](../code/mineral_prospectivity_ml_demo.py).

---

## ★1 — Budget, chance, uplift

A 10% budget is $0.10 \times 3600 = 360$ cells. A random selection of 360 cells
would contain, in expectation,

$$0.10 \times 95 = 9.5\ \text{deposits}.$$

The model captures $0.116 \times 95 = 11.0$ deposits, so the uplift is
$0.116/0.10 = 1.16\times$.

It is worth checking whether 11 differs from 9.5 in any meaningful sense. For a
random selection of $n = 360$ cells from $N = 3600$ containing $K = 95$ deposits,
the count is hypergeometric with variance

$$\mathrm{Var} = n\frac{K}{N}\left(1-\frac{K}{N}\right)\frac{N-n}{N-1}
= 360 \times 0.02639 \times 0.97361 \times 0.90025 = 8.33, \qquad
\mathrm{sd} = 2.89 .$$

The observed excess of $1.5$ deposits is **$0.5\sigma$**. The uplift is not
distinguishable from chance. Any write-up of this model must say so, and that is
the most useful output of the exercise: the metric that a decision-maker wants
must be accompanied by its own sampling error, which for counts over a finite
inventory is hypergeometric, not binomial.

---

## ★2 — Which analyst choice dominates?

Negative design: $0.619 - 0.513 = 0.106$ (uniform to matched under random folds),
or $0.619 - 0.539 = 0.080$ block-to-block; the largest swing is
$0.619 - 0.513 = 0.106$.

Fold design: the largest change is $\lvert -0.026 \rvert = 0.026$.

Ratio: $0.106/0.026 = 4.1$. The negative design moves the reported number about
four times as much as the fold design, and it must be described first — together
with the rule used to draw the negatives, because "800 random non-deposit cells"
is not a description unless the sampling population is stated.

---

## ★3 — Matching radius against correlation length

$$\frac{r_{\text{match}}}{L} = \frac{3\ \text{cells}}{6\ \text{cells}} = 0.5 .$$

A matched negative lies within **half a correlation length** of a deposit, so its
evidence values are drawn from nearly the same distribution as the deposit's; the
two classes overlap almost completely and the AUC collapses to $0.513$, which is
chance. The implication for the map is direct: it cannot resolve targets at a
spacing of a few cells, whatever its AUC against uniform negatives says.

---

## ★4 — Why a uniform-negative AUC is an upper bound

The AUC is a probability of a random pair:

$$\mathrm{AUC} = \Pr\left[s(x^{+}) > s(x^{-})\right],$$

where $x^{+}$ is drawn uniformly from the positives and $x^{-}$ from the negative
population. With **uniform** negatives, $x^{-}$ is drawn from the whole grid, and
because deposits occupy a small fraction of the cells, the typical negative is
*far* from any deposit: its evidence values are typical of background ground, and
the comparison $s(x^{+}) > s(x^{-})$ is easy.

With **matched** negatives, the negative population is conditioned on proximity,
$N(r) = \{x : \lvert x - \text{nearest deposit}\rvert \le r\}$. Because the
evidence fields are spatially correlated, the scores of cells in $N(r)$ are
stochastically larger than those of uniformly drawn cells:

$$\mathrm{AUC}_{\text{matched}} = \Pr\left[s(x^{+}) > s(x^{-}) \mid x^{-} \in N(r)\right]
\le \mathrm{AUC}_{\text{uniform}} .$$

So the uniform-negative AUC is an **upper bound** whose looseness is set by how
far the typical negative is from a deposit — a quantity the analyst controls, not
a property of the district.

**What would replace it for a decision-maker.** Precision at the budget: for a
budget of the top $q$ fraction of cells, the expected number of deposits captured
per 100 cells selected, together with its uncertainty, and the cost per deposit
found. That is a count with a hypergeometric (or bootstrap) interval, as in ★1,
not a rank statistic.

---

## ★★★5 — Block-size sensitivity

**Design.** Re-run the identical model and data with block sizes
$b \in \{5, 10, 15, 20, 30\}$ cells, plus the random-fold case ($b = 1$) as the
reference, using leave-one-block-out and pooling the out-of-fold predictions each
time. Report the pooled AUC and the spread of the per-block AUCs.

**Metric and plot.** Pooled out-of-fold AUC against $b$, with the random-fold value
drawn as a horizontal reference line, and the per-block AUC spread as an error
band.

**Prediction for $L = 6$ cells.** For $b \ll L$ the leak is large and the AUC
exceeds the reference; the curve falls as $b$ grows, and flattens once
$b \gtrsim 2L$–$3L$ (12–18 cells), where the held-out block is wide enough that
neighbouring training cells no longer share the held-out cells' anomalies. The
measured values are consistent with this: at $b = 15$ and $b = 30$ the difference
from random folds is at most $0.026$, i.e. within the metric's own sampling
error. The prediction that the curve is *flat* at small $b$ would disconfirm the
mechanism and should be stated as the alternative.

**Rule for a new district.** Estimate the correlation length of each evidence
layer from a variogram, take the largest, and set the block size to at least
twice it; then report the AUC at two block sizes — the chosen one and one
smaller — so the reader can see the sensitivity. Choosing a block size in cells
without reference to the data's own length scale is the error this exercise
exists to prevent.

---

## ★★★6 — Leave-one-out distance-to-deposit, and what still leaks

**Construction.** For a spatial split into blocks, fix the held-out block $B$.
Let $D_{-B}$ be the set of deposit locations **outside** $B$. For every cell
$x$ — including every cell inside $B$ — compute

$$f(x) = \min_{d \in D_{-B}} \lvert x - d\rvert,$$

which is a Euclidean distance transform evaluated once per fold on the point set
$D_{-B}$. The held-out block's own deposits never enter its own feature, so a
model cannot read the answer off the feature for the cells it is being scored on.

**What it still leaks.**

1. **The exploration history.** Deposits exist where someone looked and was
   successful. The pattern of $D_{-B}$ encodes where previous campaigns went,
   which is correlated with the same evidence layers (access, previous anomalies)
   that the model is trying to learn. The feature therefore imports the *prior
   exploration's* bias into the score.
2. **Spatial correlation of the geology itself.** If $L$ exceeds the block size, the
   deposits just outside $B$ are drawn from the same mineralised structures as
   those inside it, so their locations genuinely predict the held-out ones. This
   is not a validation artefact — it is real information — but it means the
   measured performance describes *infill* discovery inside a known district, not
   discovery in an unexplored one.

No fold design can remove either leak, because neither is caused by the split:
the first is a property of the inventory's origin and the second a property of the
Earth. The mitigation is disclosure: state the inventory vintage, the
exploration history, and whether the performance claim is about infill or
greenfields ground.

---

## ★★★7 — Measuring the inventory reporting bias

**Simulating an access-biased inventory.** Build an accessibility surface $A(x)$
(here, distance to a synthetic road network). Then:

1. draw the *true* deposits from the geology as before;
2. record a true deposit with probability $p_{\text{rec}}(x)$ that decreases with
   $A(x)$ — the further from a road, the less likely it was ever found and
   described;
3. draw the manufactured negatives only from accessible ground, because
   inaccessible ground was never examined and therefore contributes no
   "no deposit here" observation.

The result is an inventory whose positives and negatives are both drawn from a
subset of the district selected by access rather than by geology.

**Metrics.**

1. AUC of the model against the biased inventory (expected: high).
2. AUC against a *held-out unbiased* set — for example deposits from an
   independent later campaign, or a synthetic truth set retained by the
   experimenter and never shown to the model.
3. The correlation between the predicted score and the accessibility surface
   $A(x)$, computed over the whole grid. Compare it with the correlation between
   the score and the latent geological score, which only the synthetic
   experiment knows.

**The pattern that shows the bias is learned.** The model's ranking correlates
with accessibility at least as strongly as with the geology, and the AUC drop
between (1) and (2) is large. A second signature: the model's highest scores
cluster along roads, so the top cells are *accessible* rather than *favourable* —
visible immediately in a map, and invisible in every aggregate metric.

---

## ★★★8 — Evaluating an economic claim from a $1.16\times$ uplift

**Geological information.**

- The **deposit type** and its target size distribution — an uplift matters only
  relative to the size of the target that a $1.16\times$ efficiency can find.
- **Inventory completeness** at the size and depth cutoff used: a district's
  recorded deposit density saturates as exploration proceeds, so the uplift
  measured against an old inventory is not the uplift against the truth.
- **Accessibility and land status** of the top cells: the captured deposits may be
  in ground that cannot be worked.

**Economic information.**

- Exploration cost per cell and per drill hole, at the resolution the map is
  used.
- Commodity price and the distribution of deposit grades and tonnages, since
  deposits are not equal: capturing 11 small occurrences is not capturing
  11 economic deposits.
- The discount rate and the time to discovery, since an uplift that concentrates
  deposits in ground that takes a decade to permit is not an economic uplift.

**Statistical information.**

- The **uncertainty of the uplift**, as in ★1: the hypergeometric standard error for
  an inventory count, or a block bootstrap over deposits for an efficiency curve.
  A $1.16\times$ uplift with a $\pm0.3$ interval contains $1.0$.
- The **sensitivity to the negative design**, which in this lesson spans $0.513$ to
  $0.619$ AUC and therefore moves the shape of the efficiency curve.
- The **concentration** of the captured deposits: if the 11 captured deposits are
  one cluster, the result is a statement about one target, not about the method.
- The **dependence on the budget**: report the curve, not the value at 10%.

**The result that would falsify the claim.** Any one of: the efficiency
interval including $1.0$; the entire uplift arising from a single deposit cluster;
the uplift vanishing when the negatives are drawn as matched negatives; or the
top cells lying in ground that the economic layer rules out. The claim is
falsified by *measurement*, not by argument, so each of these is an experiment the
study must contain.
