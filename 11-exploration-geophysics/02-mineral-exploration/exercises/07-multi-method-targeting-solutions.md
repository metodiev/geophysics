# Solutions — 11-02-07 Multi-Method Targeting and Prospectivity Analysis

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All constructions are **SYNTHETIC**.

Lesson: [07 Multi-Method Targeting](../07-multi-method-targeting.md).

---

## ★1 — Weights of evidence

$5000$ cells, $30$ training deposits, favourable class $1500$ cells containing
$15$ deposits.

$$\mathbb{P}(B|D) = \frac{15}{30} = 0.5000, \qquad
\mathbb{P}(B|\bar D) = \frac{1500-15}{5000-30} = \frac{1485}{4970} = 0.298793,$$

$$w^{+} = \ln\frac{0.5000}{0.298793} = \ln(1.67340) = 0.514858,$$

$$\mathbb{P}(\bar B|D) = 0.5000, \qquad
\mathbb{P}(\bar B|\bar D) = 0.701207, \qquad
w^{-} = \ln\frac{0.5}{0.701207} = \ln(0.713056) = -0.338195,$$

$$C = w^{+}-w^{-} = 0.853053 .$$

**Reading:** the odds of a deposit are $e^{0.5149} = 1.67\times$ higher inside the
favourable class than outside it — a useful but not decisive layer. For comparison,
the SYNTHETIC layers of the lesson had contrasts of $2.26$ and $2.05$.

---

## ★2 — The posterior equals the empirical rate

Prior $= 30/5000 = 0.006$, prior odds $= 0.006/0.994 = 0.006036$.

$$p_{B} = \frac{0.006036 \times 1.67340}{1 + 0.006036 \times 1.67340}
= \frac{0.010100}{1.010100} = 0.010000 = \frac{15}{1500}\ \checkmark$$

$$p_{\bar B} = \frac{0.006036 \times 0.713056}{1+0.006036\times0.713056}
= \frac{0.004304}{1.004304} = 0.0042857 = \frac{15}{3500}\ \checkmark$$

Both agree exactly (to $10^{-15}$ in the demonstration's four-class check). **WofE
is an algebraic rewriting of the contingency table for a single layer**: the
posterior in a class *is* the observed deposit fraction in that class. Therefore
there is no modelling assumption in the single-layer calculation at all, and every
difficulty in a prospectivity study lies in the combination step and in the
training data.

---

## ★3 — A second layer

$15\%$ coverage ($750$ cells) containing $12$ deposits:

$$\mathbb{P}(B_2|D) = 0.4000, \qquad
\mathbb{P}(B_2|\bar D) = \frac{738}{4970} = 0.148491, \qquad
w^{+}_2 = \ln(2.69376) = 0.990941,$$

$$w^{-}_2 = \ln\frac{0.6000}{0.851509} = \ln(0.704632) = -0.350080, \qquad
C_2 = 1.341021 .$$

**Layer 2 is the stronger of the two** (contrast $1.34$ against $0.85$) despite
covering half the area, because its favourable class is much more enriched
($\mathbb{P}(B|D)/\mathbb{P}(B|\bar D) = 2.69$ against $1.67$). The lesson's
caution applies: **a contrast is not a probability of success**, and a narrow
favourable class with a high contrast often has a large sampling error because the
proportion of deposits inside it is estimated from few cells.

---

## ★4 — A four-cell AUC

$$\mathrm{AUC} = \frac{\sum_{i,j} p_i(1-p_j)\mathbf{1}[s_i > s_j]}
{\left(\sum_i p_i\right)\left(\sum_j(1-p_j)\right)}
= \frac{2.83}{1.6 \times 2.4} = \frac{2.83}{3.84} = 0.7370 .$$

Pair enumeration with $s = (4,3,1,2)$ and $1-p = (0.1,0.6,0.8,0.9)$:

| pair $(i,j)$ | $s_i>s_j$? | contribution $p_i(1-p_j)$ |
|---|---|---|
| (0,1) | 4>3 ✔ | 0.54 |
| (0,2) | 4>1 ✔ | 0.72 |
| (0,3) | 4>2 ✔ | 0.81 |
| (1,2) | 3>1 ✔ | 0.32 |
| (1,3) | 3>2 ✔ | 0.36 |
| (3,2) | 2>1 ✔ | 0.08 |
| **sum** | | **2.83** |

$\mathrm{AUC} = 2.83/3.84 = 0.7370$. The denominator counts every
positive–negative pair once in each direction, which is why the same $3.84$ appears
whether the pairs are enumerated by hand or by the sorted rank formula.

---

## ★5 — The coincidence test

Under conditional independence, the fraction of deposits falling in *both*
favourable classes would be the product of the individual fractions:

$$\mathbb{P}(B_1 \cap B_2 \mid D) = 0.5 \times 0.4 = 0.20
\;\Longrightarrow\; \mathbb{E}[\text{deposits in both}] = 30 \times 0.20 = 6.0 .$$

| case | observed coincidence | direction of the error in the both-favourable class |
|---|---|---|
| (a) 6.0 (independent) | 6.0 | none: the log-odds sum is the correct joint table |
| (b) 8.4 (+40%) | 8.4 | **over-confident**: the sum counts the shared association twice |
| (c) 3.6 (−40%) | 3.6 | **under-confident**: the layers are *negatively* associated, and the sum ignores the redundancy that makes them disagree |

The direction follows from one line of algebra: with a positive association in the
target, $\mathbb{P}(B_1\cap B_2|D) > \mathbb{P}(B_1|D)\mathbb{P}(B_2|D)$, so the
product of the likelihood ratios understates the joint likelihood ratio — the sum
*overstates* the evidence. A **negative** association (two methods that see the
same thing in opposite senses, or a layer that is high where the other is low)
reverses the direction: the sum then *understates* the joint evidence, and a
prospectivity map can be too conservative in exactly the areas where two
independent observations agree.

---

## ★6 — The magnitude of the error, from the lesson's numbers

$10\,000$ cells, $40$ deposits, layers at $20\%$ coverage, $18$ and $16$ deposits
in the favourable classes, $9$ in both, and $600$ cells favourable in both.

**Both-favourable class.** Prior odds $= 40/9960 = 0.0040161$.
Likelihood ratios: $0.45/0.198996 = 2.2613$ and $0.40/0.199196 = 2.0081$, product
$4.5409$. Summed-log-odds posterior:

$$p_{\text{sum}} = \frac{0.0040161 \times 4.5409}{1 + 0.0040161 \times 4.5409}
= \frac{0.018237}{1.018237} = 0.017910 .$$

Empirical rate from the joint table: $9/600 = 0.015000$.

$$\text{ratio} = \frac{0.017910}{0.015000} = 1.194 .$$

**The summed log odds overstate the posterior by 19%** in the class where both
layers agree. (Note also that the prior itself is wrong by a factor: the training
density $40/10\,000 = 0.004$ against the true base rate $0.005$, another source of
error of the same order.)

**Layer-1-only class.** Summed posterior $= 0.009000$; empirical rate
$18/2000 = 0.009000$; ratio $= 1.0000000$. **The error vanishes exactly**, and for
the reason established in ★2: with one layer there is no combination, so the
posterior is the table. The entire approximation of WofE lives in the sum.

**Conclusion for reporting.** A prospectivity map built by summing log odds should
be reported with the *joint* statistics of the layer pairs it combines, or with the
capture curve that measures the consequence. Reporting only the per-layer
contrasts (the usual practice) reveals nothing about the error.

---

## ★7 — Identical AUC, different capture

Two-component construction on $10\,000$ cells with a base rate of $0.005$:
$100$ "favourable" cells with mean $p = 0.15$ ($15$ expected deposits) and $9900$
"poor" cells with $p = 0.003535$ ($35$ expected deposits). Total $50$ expected.

- **Map A** ranks all $100$ favourable cells first. Capture at $50$ sites:
  $50 \times 0.15 = 7.5$ deposits.
- **Map B** ranks $50$ favourable cells and $50$ poor cells in its top $50$.
  Capture at $50$ sites: $50\times0.15 + 0 = 7.5$ — the same number, because the
  ordering *within* the favourable group is irrelevant to the count.
- **Map C** ranks $25$ favourable cells first and then poor cells; to reach $50$
  sites it must use $25$ poor cells: capture
  $= 25\times0.15 + 25\times0.003535 = 3.75 + 0.088 = 3.84$.

Maps A and B have the *same* AUC (both are monotone in the mixture indicator) and
the same capture; map C has a *lower* AUC and a capture differing by a factor of
$1.95$. **The mechanism:** the AUC is an average over all pairs, dominated by the
$9900 \times 9900/2$ within-poor pairs that no map can order, while the capture
curve at a small budget depends only on the top of the ranking. Two maps can
therefore share an AUC and differ substantially in capture *if they order the top
of the ranking differently* — which is what happens when a spurious factor with a
large spatial scale competes with the true signal for the top slots (the lesson's
WofE case).

The honest statement of the exercise's premise: identical AUCs do **not** by
themselves imply equal captures, and the reason is that the AUC integrates over the
whole ranking while the decision reads only its head.

---

## ★8 — How many realisations are needed?

With a null mean of $0.5126$ and standard deviation $0.0768$, a layer with a true
AUC of $A$ is distinguished at $3\sigma$ when

$$n \ge \left(\frac{3\sigma}{A - 0.5126}\right)^{2}.$$

For $A = 0.60$: $n \ge (3 \times 0.0768/0.0874)^{2} = 6.95$, i.e. at least **7
realisations**.

For $A = 0.55$: $n \ge (3\times0.0768/0.0374)^{2} = 38.0$, i.e. **38
realisations**.

**The lesson's 30-realisation experiment could detect a true AUC of $0.60$ but not
one of $0.55$.** This is the quantitative reason a single-realisation study
cannot claim a layer "works": the null spread is $0.0768$, so an AUC of $0.60$ is
only $1.1\sigma$ above the null *on a single realisation*, and it takes a
simulation — not a comparison with the conventional $0.5$ — to establish that it
is real. Reporting "AUC $= 0.62$, therefore the layer is predictive" is a claim
about an unstated null.

---

## ★9 — The duplicate-layer test

**Proof.** If a layer is entered twice, the summed log odds gain $w^{+}$ (or
$w^{-}$) twice, so the composite likelihood ratio is
$\Lambda^{2}$ instead of $\Lambda$.

**Numerical.** Prior $\pi = 0.01$, so prior odds $= 0.01/0.99 = 0.010101$.
With $w^{+} = 1.0$ the likelihood ratio is $\Lambda = e^{1} = 2.718282$:

| entries | likelihood ratio | posterior odds | posterior |
|---|---|---|---|
| 1 (correct) | $e^{1} = 2.718282$ | 0.027458 | **0.026724** |
| 2 | $e^{2} = 7.389056$ | 0.074637 | 0.069453 |
| 3 | $e^{3} = 20.0855$ | 0.202890 | 0.168665 |

**The correct posterior is $p_1 = 0.026724$.** Duplicating the layer raises it to
$0.069453$ — **a factor of $2.60$ in probability and a factor of $4$ in odds** —
and tripling raises it to $0.168665$, a factor of $6.3$ in probability. There is
no new information anywhere; the only change is that the same observation has been
counted again.

**Detecting it without a truth.** Three tests, all available in a real study:

1. **The coincidence test of ★5.** Compute the observed number of training sites
   in the joint favourable class and compare with the independence product. A
   ratio above 1 is the signature.
2. **The deliberate-duplication test.** Add a *copy* of an existing layer and
   observe whether the posterior changes. If it does, the combination is
   double-counting by construction, and the size of the change measures the
   sensitivity of the map to the assumption.
3. **Layer correlation and residualisation.** Regress one layer on the others and
   report the residual's variance fraction; a layer that is $>80\%$ explained by
   its fellows contributes almost nothing new, and its weights are almost entirely
   redundant.

---

## ★10 — A validation protocol without a known truth

| element | detects | does **not** detect |
|---|---|---|
| **Spatial block cross-validation** (hold out contiguous districts, not cells) | leakage between neighbouring training and test cells; over-fitting to the spatial pattern | bias in the training *label* (which deposits were found) |
| **Temporal audit** (score against ground explored after the model was built) | exploration bias, including the bias toward shallow/accessible ground | whether the *target definition* is the right one |
| **Null simulation** (score deliberately irrelevant smooth layers, ≥30 realisations) | chance AUCs from spatial autocorrelation and small effective sample size | a real but weak signal (which is the point: it gives the *threshold*) |
| **Effective-sample-size reporting** | false precision: "16 384 cells" is really "256 patches" | nothing on its own — it is a caveat, not a test |
| **Capture-curve reporting at real budgets** | failures that the AUC hides; the decision-relevant behaviour | calibration; a map can rank well and still mis-state probabilities |
| **Joint-table check / coincidence ratio** | the conditional-independence failure and its direction | the magnitude of its effect on a *ranking* (which requires the capture curve) |
| **Layer residualisation** | redundant layers; spurious shared factors | a shared factor that is genuinely geological and genuinely relevant |

**The honest summary a client needs:** a validated prospectivity map comes with a
**null distribution**, a **capture curve at the budgets in question**, a **spatial
cross-validation score**, and an explicit statement that the calibration level
depends on a base rate estimated from biased data.

---

## ★11 — Adding a third correlated layer

Predictions, stated conditionally because the answer depends on the new layer's
composition:

**(a) AUC.** Let $\lambda$ be the fraction of the new layer's variance explained by
the shared trend $r$.
- If $\lambda$ is large (mostly trend), the AUC **falls further**: the trend's
  weight is multiplied a third time, and the top of the ranking is captured even
  more completely by the trend.
- If $\lambda$ is small and the layer carries independent signal, the AUC
  **rises**: averaging three noisy views of $g$ reduces the noise, exactly as the
  lesson's "plain average of the two layers" ($0.8218$) beat WofE ($0.7938$) in the
  trend-free sense.

**(b) Calibration ratio across the trend.** The change in the ratio from the
lowest to the highest trend quintile must **increase** whenever the new layer
contains any of the shared trend, because the trend's total log-odds contribution
is the sum over layers. Predicted: the ratio change grows from the measured $6.9$
toward a value proportional to the number of trend-bearing layers.

**(c) Capture at a 10-site budget.** **Decreases** if the new layer is
trend-dominated (the head of the ranking is displaced further from the true high
cells) and **increases** if it is signal-dominated. The two cases are distinguished
by the residual variance fraction $\lambda$.

**The experiment that tests the prediction.** Re-run the demonstration with three
layers,
$$L_3 = \gamma g + \delta r + \varepsilon_3,$$
and sweep $\delta/\gamma$ over, say, $0, 0.5, 1, 2, 4$; for each, compute the AUC,
the calibration ratio across the trend quintiles and the 10-site capture. Plot all
three against $\delta/\gamma$. The prediction is a monotone degradation in (b) and
(c) with $\delta/\gamma$ and a non-monotone AUC with a maximum at the
$\delta/\gamma$ that best balances noise reduction against trend amplification.

**The diagnostic that identifies the responsible layers.** Regress each layer on
$r$ and report $R^{2}$. For the lesson's construction, with unit variances and
noise variance $0.8^{2} = 0.64$,

$$R^{2}(L_1) = \frac{0.6^{2}}{1 + 0.6^{2} + 0.8^{2}} = \frac{0.36}{2.00}
= 0.180, \qquad
R^{2}(L_2) = \frac{0.8^{2}}{0.49 + 0.64 + 0.64} = \frac{0.64}{1.77} = 0.362,$$

so layer 2 carries twice the trend fraction of layer 1 and is the one to
residualise first.

A cleaner and directly computable version: partial out the trend from each layer
and recompute the weights and the map. If the capture improves when the trend is
removed from the layers, the trend was the culprit, and the amount of improvement
ranks the layers by their trend content. This is exactly the "residualise before
combining" step of the lesson's diagnostic list, and it is available without any
knowledge of the truth.
