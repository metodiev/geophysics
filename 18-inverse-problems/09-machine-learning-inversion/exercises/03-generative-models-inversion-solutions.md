# Solutions — 18-09-03 Generative Priors: GANs, VAEs, Diffusion Models

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC**.

Lesson: [03 Generative Priors: GANs, VAEs, Diffusion Models](../03-generative-models-inversion.md).

---

## ★1 — Posterior and provenance

$$p(\mathbf{m}\mid\mathbf{d}) \propto
\exp\!\left[-\tfrac12\left(\mathbf{d}-G\mathbf{m}\right)^{T}
C_d^{-1}\left(\mathbf{d}-G\mathbf{m}\right)\right]
\exp\!\left[-\tfrac12\left(\mathbf{m}-\boldsymbol{\mu}\right)^{T}
\Sigma_\phi^{-1}\left(\mathbf{m}-\boldsymbol{\mu}\right)\right].$$

From the **ensemble**: $\boldsymbol{\mu}$ and $\Sigma_\phi$ (and, for a deep
model, the generator parameters $\phi$). From the **physics**: $G$ and $C_d$.
The two are independent inputs; neither is measured by the survey.

---

## ★2 — Variance accounting

$$0.412+0.267+0.129+0.058 = 0.866 \;\Rightarrow\; 86.6\% \text{ explained},$$

residual $=1-0.866 = 0.134$, i.e. 13.4% (the demonstration's printed 13.47%).

The residual is the part of the ensemble's variability that the four-component
prior cannot represent. A model needing structure in that residual is one the
prior will reject — regardless of whether the data support it.

---

## ★3 — Null directions

For $G$ of shape $20\times30$, $\operatorname{nullity} = 30 - \operatorname{rank}
= 10$ exact null directions (given rank 20).

The posterior variance in those directions describes the **width of the claim**
about model features that no observation constrains. It is set entirely by the
prior; the data contribute nothing.

---

## ★4 — Two readings of the null-space sigma

*If the ensemble is representative:* "the models in our ensemble vary by only
0.148 (one sigma) in the directions the data cannot see, so the inversion's
small uncertainty there reflects genuine prior knowledge of the geology."

*If the ensemble may not be representative:* "the inversion's small uncertainty
in the unseen directions is a restatement of the ensemble's own narrowness; it is
not evidence from the data, and if the target's structure lies outside the
ensemble the reported confidence is meaningless."

Which reading applies is not something the inversion can tell you.

---

## ★5 — Lower MSE but wrong energy

Both hold because MSE is an *average* over the whole model: for a spike target,
the learned prior's smooth, biased answer happens to land closer in aggregate
than the smoothness prior's answer, while being structurally wrong. The energy
projection shows the mechanism: 95.1% of the recovered energy sits in a subspace
that contains only 11.2% of the truth's energy.

The second number is more important because it is *systematic*: it holds for
every target outside the ensemble, and it describes where the answer's content
comes from. An aggregate error can improve by luck; a subspace projection can be
predicted and reported, and it tells a reader that the structure in the image is
the prior's, not the data's.

---

## ★6 — Is the prior valid for a faulted target?

Answer: **unknown, and probably not.** A prior learned from layered models
represents layered structure; a fault offsets layering, which the linear (or
deep) family may not span, and the inversion will then fit the data with layered
structure as far as its prior weight allows.

Experiment that would settle it: extend the ensemble with faulted models (of a
stated throw distribution), refit the prior, and run the in-family comparison
again on a held-out set of faulted models. Decision rule: if the extended prior's
error on held-out faulted models is materially lower than the layered-only
prior's, the layered prior was inadequate; if it is not, the faulted structure is
not being represented even by the extended family, which points to the
forward/parameterisation rather than the prior.

---

## ★7 — Broad versus narrow ensembles

Metric: a **held-out cross-family error** — for a target family of interest,
invert a set of models from that family (not used in training) with both priors
and report (i) model error, (ii) the fraction of the recovered energy inside each
prior's subspace, and (iii) the chi of the misfit.

Decision rule: the narrow prior wins if its error is lower *and* the target models
are well represented by its subspace; the broad prior wins if the narrow prior's
subspace projection is high (near 1) while the target's is low, because that is a
signature of forcing.

The narrow prior gains accuracy and confidence inside its family; it loses
everything outside it, silently, and its reported uncertainty understates the
error by an amount that grows with the mismatch.

---

## ★8 — Inversion without a likelihood

1. **Sample-and-filter (approximate Bayesian computation).** Draw
   $\mathbf{m}\sim p_\phi$, forward-model, and keep samples whose data residual is
   below a tolerance. Guarantee lost: the posterior is approximated by a
   tolerance and no exact normalisation; the tolerance is a chosen quantity.
2. **Posterior sampling through the generator plus a data term** (e.g. Langevin
   or stochastic-gradient optimisation on $\mathbf{z}$ with
   $\|\mathbf{d}-Gg_\phi(\mathbf{z})\|^2$). Guarantee lost: the mapping from
   $\mathbf{z}$ to $\mathbf{m}$ is not invertible, so a density over
   $\mathbf{z}$ induces a density over $\mathbf{m}$ only through the generator's
   Jacobian, which is generally unavailable; what one reports is a mode or a set
   of samples with no calibrated uncertainty.

Both are legitimate, and both must state that the reported uncertainty is not a
posterior probability in the sense of lesson 04 unless it has been calibrated.
