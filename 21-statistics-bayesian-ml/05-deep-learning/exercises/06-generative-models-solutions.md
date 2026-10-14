# Solutions — 21-05-06 GANs, VAEs and Diffusion Models

> Read after attempting. Lesson:
> [06 Generative Models](../06-generative-models.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — The evidence lower bound

$$\mathcal L = \mathbb E_{q_\phi(z\mid x)}\big[\ln p_\theta(x\mid z)\big]
- \mathrm{KL}\big(q_\phi(z\mid x)\,\|\,p(z)\big) \;\le\; \ln p_\theta(x).$$

The first term is the **reconstruction** term: it rewards decoders that put mass on
the observed data. The second is a **regulariser**: it pulls the approximate
posterior towards the prior so that samples drawn from the prior land where the
decoder expects them. The difference is exactly the KL divergence between the
approximate and the true posterior,

$$\ln p_\theta(x) - \mathcal L = \mathrm{KL}\big(q_\phi(z\mid x)\,\|\,p_\theta(z\mid x)\big)
\ge 0,$$

which is why $\mathcal L$ is a lower bound, and why it becomes exact only when the
variational family contains the true posterior.

---

## ★2 — The adversarial objective

$$\min_G \max_D\ \mathbb E_{x\sim p_{\text{data}}}[\ln D(x)]
+ \mathbb E_{z\sim p_z}\big[\ln\big(1 - D(G(z))\big)\big] .$$

For a fixed generator, maximising the integrand pointwise gives

$$D^{*}(x) = \frac{p_{\text{data}}(x)}{p_{\text{data}}(x) + p_G(x)} ,$$

which is the posterior probability that a sample came from the data under equal
priors. That is exactly the output of a two-sample classifier, so the discriminator
is a learned goodness-of-fit test and the generator's objective is to make that
test uninformative. The goal is not a better generator in a likelihood sense; it is
the point where the classifier cannot separate the samples at all.

---

## ★3 — The forward diffusion step

$$q(x_t\mid x_{t-1}) = \mathcal N\big(\sqrt{1-\beta_t}\,x_{t-1},\ \beta_t I\big),
\qquad
x_t = \sqrt{\bar\alpha_t}\,x_0 + \sqrt{1-\bar\alpha_t}\,\varepsilon,
\qquad \bar\alpha_t = \prod_{s\le t}(1-\beta_s).$$

The forward process is **fixed and untrained** — it is a noise schedule, not a
model. Training learns the reverse step, usually by predicting the noise
$\varepsilon$ that was added, which is equivalent to predicting the score of the
noisy marginal. Because the schedule is known, the difficulty of each reverse step
is fully determined by the local signal-to-noise ratio $\bar\alpha_t/(1-\bar\alpha_t)$.

---

## ★★4 — The ELBO at three settings

$$-7\,285.4324 - (-11\,682.9057) = 4\,397.4733 \text{ nats},$$
$$-7\,285.4324 - (-7\,285.4335) = 0.0011 \text{ nats}.$$

The exact posterior gives the largest bound, $4\,397.4733$ nats above the prior —
a likelihood ratio of $e^{4397.4733}$, which is why the prior is a hopeless model of
these data. The residual gap of $0.0011$ nats between the sample-mean setting and
the exact posterior is numerical: with $1.5^{2} = 2.25$ of observation variance,
$4000$ observations and a unit prior variance, the posterior variance is
$1/(4000/2.25 + 1) = 0.0005622$, so the variance is estimated to within $0.1\ \%$ and
the two optima agree to four significant figures.

The maximum equals the log evidence because the Gaussian family contains the true
posterior. The variational bound is a bound only relative to the family: give the
family the truth and the inequality collapses to an equality. That is the
calibration check for a variational implementation — an implementation whose optimum
does not reach the analytic evidence on a conjugate problem has a bug or has not
converged.

---

## ★★5 — AUC as a two-sample statistic

Chance is $0.5$. The distances are

$$0.9692 - 0.5 = 0.4692 \quad\text{and}\quad 0.4857 - 0.5 = -0.0143 .$$

The poor generator is separated almost perfectly; the matched generator is *below*
chance, which is within sampling noise of $0.5$ and therefore indistinguishable from
a coin flip — the training objective attained.

An AUC near $0.5$ is **necessary**: a generator that matches the data cannot be
separated by any classifier, least of all this one. It is **not sufficient**:

1. AUC compares only the ranking of the two samples' scores at the decision
   threshold; two distributions can have identical AUC while differing in their
   tails.
2. The discriminator is finite-capacity and trained, so a weak discriminator can
   fail to separate distributions that are in fact different.
3. Distribution agreement in a learned feature space says nothing about physical
   properties — connectivity, spectral content, facies proportions.

A generator must therefore be reported with several statistics, and with at least
one that is computed on the physics of the problem rather than on a learned score.

---

## ★★6 — The diffusion schedule

At step 1, $\bar\alpha_1 = 1 - 10^{-4} = 0.999900$ and

$$\frac{0.999900}{1 - 0.999900} = \frac{0.999900}{0.000100} = 9999 .
\quad ✓ \text{(matches the reported SNR)}$$

At step 100, $\bar\alpha_{100} = 0.897018$:

$$\mathrm{SNR}_{100} = \frac{0.897018}{1 - 0.897018} = \frac{0.897018}{0.102982}
= 8.7104 ,$$

which matches the demonstration's $8.7104$. The schedule destroys information
geometrically: the SNR falls from $9999$ at step 1 to $8.71$ at step 100 — three
orders of magnitude in a hundred steps — and reaches $1$ at step $259$ of $1000$.
The reverse process must therefore first undo large, easy changes and then small,
hard ones, which is why the later steps of diffusion sampling carry most of the
detail.

---

## ★★7 — VAE against GAN against diffusion for facies simulation

**Design.** Build a synthetic reservoir from a known process — a truncated
Gaussian or a training-image-based model — so the true facies proportions,
variogram ranges, connectivity and channel-width distribution are known. Generate a
training set of realisations by resampling the process, then train all three
families on it with the same conditioning variables (well locations, proportion
constraints) and comparable parameter counts.

**Evaluation statistics.** Physical, not learned:

1. facies proportions per category;
2. variogram ranges and sill in the principal directions, per facies;
3. a connectivity measure, for example the fraction of cells connected to a well;
4. the distribution of channel widths or object thicknesses, obtained by a fixed
   morphological measurement;
5. a multipoint statistic such as a two-point/three-point histogram, to detect
   higher-order structure the variogram cannot see.

**Metrics.** For each statistic, the discrepancy between generated and reference
sets — the Wasserstein distance or the absolute difference in quantiles — with
uncertainty from the finite sample. Report coverage: for each realisation, the
distribution of the statistic over generated samples should contain the reference
value at the nominal rate.

**Replicates.** At least 20 independent training runs per family, each with its own
data draw, so the reported discrepancy separates model error from run-to-run
variance; evaluate each trained model on at least 200 generated realisations.

**Mode collapse.** Detected by three symptoms together: (a) low variability
**between** generated samples for a statistic that should vary — the empirical
spread of the statistic is much narrower than the reference's; (b) nearest-neighbour
duplicates, with some generated realisation an almost exact copy of a training
sample; and (c) good marginal agreement in the low-order statistics together with a
large three-point-statistic discrepancy. Any of the three alone is ambiguous, since
a well-trained model can legitimately be less variable than the reference sample.

---

## ★★8 — Conditional augmentation with leakage controlled

**Split protocol.** Partition by **spatial block** — well, survey, or reservoir
panel — never at random. The generative model is trained **only** on the training
blocks. The validation blocks are never shown to it, in any form: not to train the
generator, not to select its hyperparameters, not to fit a discriminator, and not
to tune the confidence of its conditioning. This is the whole point — a generator
trained on validation data turns augmentation into a lookup table, and every
downstream metric improves for the wrong reason.

**Arms.** Three, with identical downstream architecture, optimiser, budget and
validation set:

1. **No augmentation** — the baseline accuracy at the available label budget.
2. **Generative augmentation** — the real labels plus synthetic samples drawn by the
   conditional model.
3. **Noise augmentation** — the real labels plus samples with randomly permuted
   labels (or simple geometric/amplitude corruption), the same number of them. This
   arm is what makes the result interpretable: any gain from doing *something*
   shows up here.

Run the sweep over label budgets, from very few to many, so the shape of the
gain can be seen: augmentation should help most where labels are scarcest.

**Metric.** Held-out accuracy or macro-$F_1$ on the untouched validation blocks,
with a confidence interval from spatial blocks; and, where the target is
probabilistic, calibration or proper scoring rules rather than accuracy alone,
since synthetic data can sharpen probabilities without improving them.

**Outcome showing augmentation is merely a regulariser.** If arm 2 beats arm 1 by
about the same margin as arm 3 beats arm 1 — statistically indistinguishable gains —
the synthetic samples contributed no information beyond extra training steps and
added noise. The same conclusion follows if the gain disappears as the label budget
grows, and if arm 2's improvement vanishes when the generator is trained on a
strictly smaller, disjoint data subset: a gain that tracks the generator's exposure
to data, rather than the amount of synthetic data, is leakage rather than
augmentation.
