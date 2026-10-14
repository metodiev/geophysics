# Solutions — 21-03-04 MCMC in Practice

> Read after attempting. Lesson:
> [04 MCMC in Practice](../04-mcmc-practice.md). Numbers quoted from the
> demonstration reproduce its output.

---

## ★1 — The acceptance probability

$$\alpha = \min\!\left(1,\
\frac{\pi(\theta')\,q(\theta\mid\theta')}{\pi(\theta)\,q(\theta'\mid\theta)}
\right).$$

For a symmetric proposal $q(\theta'\mid\theta) = q(\theta\mid\theta')$ — a centred
random walk — the two proposal densities are equal, so the ratio is $1$ and

$$\alpha = \min\!\left(1, \frac{\pi(\theta')}{\pi(\theta)}\right).$$

The chain therefore always accepts an uphill move and accepts a downhill move
with probability equal to the density ratio. Detailed balance holds because the
probability of being at $\theta$ and accepting a move to $\theta'$ equals the
reverse flow, which makes $\pi$ the stationary distribution.

---

## ★2 — Effective sample size and Monte-Carlo error

$$N_{\text{eff}} = \frac{N_{\text{steps}}}{\tau_{\text{int}}}
= \frac{19\,000}{4.8} = 3918.3,$$

the demonstration's value ✔.

$$\mathrm{MCSE} = \frac{\sigma_{\text{post}}}{\sqrt{N_{\text{eff}}}}
= \frac{0.497930}{\sqrt{3918.3}} = \frac{0.497930}{62.60} = 0.007954,$$

against the measured $0.007936$ — a difference of $0.2\ \%$, i.e. the agreement
expected when the chain is sampling the right distribution.

---

## ★3 — Split-R-hat

$$W = \frac{0.25 + 0.30}{2} = 0.275, \qquad
B = L\,\operatorname{var}(\bar\theta_c) = 100 \times
\operatorname{var}(2.70, 2.76).$$

The sample variance of the two chain means with the $n-1$ denominator is
$\big((2.70-2.73)^{2} + (2.76-2.73)^{2}\big)/1 = 0.0018$, so $B = 0.18$.

$$\hat R = \sqrt{\frac{W(L-1)/L + B/L}{W}}
= \sqrt{\frac{0.275\times0.99 + 0.0018}{0.275}}
= \sqrt{\frac{0.27225 + 0.0018}{0.275}} = \sqrt{0.99655} = 0.99827 .$$

The value is slightly below one, which is normal for a short run — $\hat R$ is
not guaranteed to exceed $1$ — and it is comfortably inside the threshold
$1.01$. The two chains agree on the mean to within $0.06$ on a posterior of
spread $0.5$, so the sampler has mixed.

---

## ★★4 — The Jacobian on a log scale

Sampling $\ell = \ln\theta$ requires the transformed density

$$p(\ell) = \pi(\theta)\Big|\frac{\mathrm d\theta}{\mathrm d\ell}\Big|
= \pi(\theta)\,e^{\ell} = \pi(\theta)\,\theta .$$

For $\pi(\theta) \propto \theta^{\alpha-1}e^{-\beta\theta}$,

$$p(\ell) \propto \theta^{\alpha}e^{-\beta\theta},$$

whose implied distribution in $\theta$ is $\mathrm{Gamma}(\alpha+1-1,\beta) =
\mathrm{Gamma}(\alpha,\beta)$ — the correct target — while **omitting** the
Jacobian leaves density $\propto\theta^{\alpha-1}e^{-\beta\theta}$ as a function
of $\theta$, i.e. $\mathrm{Gamma}(\alpha-1, \beta)$.

For the demonstration's $\alpha = 30$: the correct mean is $30/11 = 2.727273$ and
the erroneous one is $29/11 = 2.636364$,

$$\text{shift} = \frac{2.727273 - 2.636364}{2.727273} = 0.03333 = 3.3\ \%.$$

The error is exactly $1/\alpha$, so it shrinks as the posterior concentrates —
which is why it can persist unnoticed in a long-running project.

---

## ★★5 — Proposal scale, acceptance and the autocorrelation time

Halving the proposal standard deviation makes almost every proposal a small
step, so the acceptance rate rises — potentially to $0.8$ or higher. But the
chain now moves half as far per accepted step, so successive samples are more
alike: $\rho_1$ rises, and $\tau_{\text{int}}$ rises roughly as the **square** of
the step-size reduction in the diffusion regime.

The net effect on $N_{\text{eff}} = N/\tau_{\text{int}}$ is a **reduction** of
roughly a factor of four for a halving, until the acceptance rate becomes so high
that the chain is barely moving. This is the counter-intuitive point: a higher
acceptance rate is not an improvement. The quantity to optimise is
$N_{\text{eff}}$ per unit of computation, and for a one-dimensional random walk
this is close to optimal near an acceptance rate of $0.4$–$0.5$ on a transformed
scale.

---

## ★★6 — Is the transient over?

Chain 1's first $500$ steps average $2.599$ and the next $500$ average $2.785$ —
a difference of $0.186$, or $0.37$ posterior standard deviations. The exact
posterior mean is $2.727$, and the second segment is within $0.058$ of it.

**Conclusion:** the first segment is still inside the transient, and the second
is not. The evidence is the segment-to-segment difference, not the proximity of
the first segment to any prior belief: a chain that has forgotten its start
produces segments that differ by the Monte-Carlo error, which for $500$ correlated
samples with $\tau_{\text{int}} = 4.8$ is
$0.498/\sqrt{104} = 0.049$ — so a $0.186$ difference is nearly four Monte-Carlo
standard errors and signals residual transient. Discarding the first $500$ steps
is therefore justified; discarding a fixed $10\ \%$ would also have worked here,
but that is a coincidence, not a rule.

---

## ★★★7 — Proposal-tuning study

**Target.** A one-dimensional posterior with a known scale: the
$\mathrm{Gamma}(30, \text{rate }11)$ posterior of the lesson, with a posterior
standard deviation on the log scale of $\approx 1/\sqrt{30} = 0.183$.

**Sweep.** Proposal standard deviations on the log scale
$s \in \{0.01, 0.02, 0.05, 0.1, 0.18, 0.3, 0.5, 1.0, 2.0\}$.

**Design.** For each $s$, run $M = 200$ independent chains of $50\,000$ steps,
discard the first $10\ \%$, and record the acceptance rate, $\tau_{\text{int}}$
and $N_{\text{eff}} = N/\tau_{\text{int}}$.

**Metric.** $N_{\text{eff}}$ per $50\,000$ evaluations, with its own scatter
across the $M$ chains (relative standard error $\approx 1/\sqrt{2M} = 5\ \%$ on a
variance-like quantity).

**Prediction.** $N_{\text{eff}}$ is maximised at $s \approx 2.4/\sqrt{\alpha}
\approx 2.4\times0.183 = 0.44$ on the log scale — the classic scaling
$s_{\text{opt}} \propto \sigma_{\text{post}}$ for a Gaussian target — with an
acceptance rate near $0.44$. Scaling the proposal with the posterior standard
deviation is the transferable rule; a fixed proposal that works for one data set
will not work for another with a different posterior scale.

---

## ★★★8 — Pseudo-convergence on a bimodal target

**Target.** A one-dimensional mixture
$\pi(\theta) = 0.5\,\mathcal N(-4, 0.5^{2}) + 0.5\,\mathcal N(+4, 0.5^{2})$, whose
two modes are separated by $16$ posterior standard deviations: a random walk
essentially never crosses between them.

**Design.** For each of $M = 1000$ replicates, run four chains of $20\,000$ steps:
(i) all started in the left basin at $\theta = -4$; (ii) started over-dispersed at
$\theta \in \{-12, -4, +4, +12\}$. Record $\hat R$ and the fraction of chains
that end in each basin.

**Metric.** The fraction of replicates in which all four chains end in the same
basin, and the fraction in which $\hat R < 1.01$.

**Prediction.** With clustered starts, **all** replicates end in one basin —
whichever the first chain found — and $\hat R < 1.01$ in essentially $100\ \%$ of
them, so the diagnostic reports a convergence that is entirely an artefact of
where the chains were placed. With over-dispersed starts, the two modes are
found in roughly half the chains each, the reported basin split approaches
$50/50$, and $\hat R$ computed on the *pooled* chains rises towards $1.5$–$2.0$ —
correctly flagging that the chains do not agree. The study's headline is the
detection rate: $\hat R$ detects the second mode only when the starts are
over-dispersed, which is the practical rule the demo's design encodes.
