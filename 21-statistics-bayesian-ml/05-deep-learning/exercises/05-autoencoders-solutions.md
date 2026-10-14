# Solutions — 21-05-05 Autoencoders for Compression and Denoising

> Read after attempting. Lesson:
> [05 Autoencoders](../05-autoencoders.md). Numbers quoted from the demonstration
> reproduce its output.

---

## ★1 — The objective and the bottleneck

$$\min_{\theta,\phi}\ \frac{1}{n}\sum_{i=1}^{n}
\big\|x_i - g_\phi\big(f_\theta(x_i)\big)\big\|^{2} .$$

The bottleneck dimension $k$ sets how much information can survive the channel.
If $k$ is at least the intrinsic dimension of the data, the network can reconstruct
everything including noise; if $k$ is smaller, the network must rank the directions
by how much variance they explain and discard the rest. That is why the bottleneck,
not the depth, is the parameter that decides what the code represents.

---

## ★2 — Why the linear case is PCA

With a linear encoder and decoder and squared error, the optimal reconstruction is
the projection onto the leading $k$ principal directions of the centred data. The
result follows from the Eckart–Young theorem: among all rank-$k$ matrices, the
truncated SVD minimises the Frobenius norm of the residual, and $W_2W_1$ is exactly
such a rank-$k$ matrix. The agreement at $0.010474$ against $0.010474$, ratio
$1.000000$, is therefore required rather than lucky.

It is a useful test because it is an **internal consistency check on the
implementation**. A linear autoencoder that misses PCA by a wide margin has a bug
or has not converged; once it matches, any improvement from a nonlinear autoencoder
can be attributed to the nonlinearity rather than to the optimiser.

---

## ★3 — The gain from nonlinearity on a curve

$$\frac{0.000013}{0.046119} = 0.000282, \qquad
1 - 0.000282 = 99.97\ \% \text{ reduction}.$$

The parabola $y = x^{2}$ is one-dimensional but not linear, and no straight line
through the origin can follow it: PCA must choose between tracking the ends or the
apex and leaves a systematic residual behind. The nonlinear encoder learns a
coordinate *along the curve* — effectively a parameterisation of $x \mapsto (x,
x^{2})$ — so the residual is only the added noise. The gain comes from curvature,
not from extra parameters: the bottleneck is one-dimensional in both cases.

---

## ★★4 — Fraction of the corruption removed

$$1 - \frac{0.072169}{0.082538} = 1 - 0.8744 = 12.6\ \% \quad\text{(clean-trained)},$$
$$1 - \frac{0.052103}{0.082538} = 1 - 0.6313 = 36.9\ \% \quad\text{(denoising)}.$$

The clean-trained network was asked to reproduce its input, so on noisy input it
reproduces the noise as well; the only smoothing it performs is accidental and
comes from the bottleneck. The denoising network was asked to map a corrupted input
to the **clean** target, so the noise is unexplainable by construction and the only
way to lower the loss is to learn the underlying signal.

---

## ★★5 — Ratio, and what the experiment controls

$$\frac{0.052103}{0.072169} = 0.7220, \qquad \text{reduction} = 27.8\ \% .$$

**Changes:** the training target — clean input versus corrupted input.
**Stays fixed:** the architecture, the bottleneck width, the optimiser, the
learning-rate schedule, the number of steps and the evaluation data. The data
generating process is unchanged too: the same clean signal, the same corruption
level and the same seed.

Because only the target differs, the $27.8\ \%$ improvement can be attributed to
the training signal. This is the whole point of a controlled comparison: if the
denoising network had also been wider, the gain would have been confounded with
capacity.

---

## ★★6 — Choosing the corruption, and why a wide bottleneck fails

**Criterion.** Sweep the corruption level and select the value that minimises the
reconstruction error on **clean** held-out data. The evaluation set must be clean,
because a denoiser's task is to recover the signal: scoring it on noisy targets
would reward reproducing the noise, and scoring it on the training data would
reward memorisation.

**Wide bottleneck.** If the bottleneck has at least as many dimensions as the
input, the identity map is a feasible solution with zero reconstruction error. The
network then learns to copy, so the code carries the noise as faithfully as the
signal and there is no pressure to discover structure. The bottleneck is the only
source of that pressure in a plain autoencoder, which is why a representation
learner needs $k$ strictly smaller than the ambient dimension — and why adversarial
or contrastive objectives are needed once collapse is a concern.

---

## ★★7 — Is the code useful?

**Task.** Pick a supervised target that is expensive to label: for example
lithology class from well-log curves, or a facies label from a seismic window.

**Design.** Split by **spatial block** (well, survey, or time window), never by
sample, so no record appears in both training and test. Pretrain the autoencoder on
the *unlabelled* portion only, freeze the encoder, and fit a linear (or shallow)
classifier on the codes using a small labelled budget; repeat at several label
budgets.

**Metric.** Held-out accuracy or macro-$F_1$ on the blocked test set, always
reported against two baselines: (a) the same classifier on raw features, and
(b) the same classifier on randomly projected features of the same dimension. The
second baseline is what makes the result interpretable, since it controls for the
capacity of the classifier itself.

**Falsification.** If the code's accuracy is not above the raw-feature baseline at
any label budget, the representation is worthless for this task: it compresses, but
the compressed information does not include what the label depends on. A result
that only beats a random projection is evidence of capacity, not of representation
quality.

---

## ★★8 — Learned denoiser against a classical filter

**Design.** Generate $N = 200$ synthetic traces from a known reflectivity model,
and add noise under three models: (i) the model used in training (matched
Gaussian), (ii) a heavier-tailed model (student-$t$ or spiky bursts), and (iii) a
coherent model (a second reflection train with a different moveout). Train the
autoencoder on the clean/noisy pairs of model (i) only. Apply the classical filter
with its assumed noise statistics taken from model (i) as well.

**Metric.** Signal-to-noise ratio improvement in dB, and the MSE against the
**clean** trace, on a held-out set of realisations; report both, since an SNR gain
can be bought by over-smoothing.

**Conditions.** Three noise models $\times$ two methods $\times$ ten noise seeds,
with the reflectivity realisations paired across cells so the comparison is
within-realisation. Add a fourth cell with a **mismatched** training noise to
measure how quickly the learned denoiser degrades when its assumption is wrong.

**Predicted ordering.** Under the matched model the learned denoiser should win,
because it can use the signal's non-Gaussian structure that the filter's
stationarity assumption ignores. Under the heavy-tailed model both degrade, but the
classical filter should overtake the learned one: its assumption (Gaussian noise
with the right variance) is less wrong than the learned model's assumption (the
exact training noise distribution), and the filter has no training distribution to
overfit. Under the coherent model the learned denoiser should fail badly unless it
was trained on coherent noise, because a structured interferer is not
distinguishable from signal by any filter fitted to independent noise.
