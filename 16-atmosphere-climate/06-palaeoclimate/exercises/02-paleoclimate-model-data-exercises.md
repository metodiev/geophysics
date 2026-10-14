# Exercises — 16-06-02 Model-Data Comparison in Palaeoclimate

Attempt these before reading the
[solutions](./02-paleoclimate-model-data-solutions.md). Lesson:
[02 Model-Data Comparison in Palaeoclimate](../02-paleoclimate-model-data.md).
All models and data are **SYNTHETIC**. The demonstration is
[`../code/paleoclimate_model_data_demo.py`](../code/paleoclimate_model_data_demo.py).

## ★ Foundational

**★1.** Derive the scalar update by multiplying the prior density
$\mathcal{N}(\mu_p,\sigma_p^{2})$ with the likelihood
$\mathcal{N}(y,\sigma_o^{2})$ evaluated as a function of the state, and confirm
that the posterior variance is $(1-G)\sigma_p^{2}$ with
$G = \sigma_p^{2}/(\sigma_p^{2}+\sigma_o^{2})$.

**★2.** With $\sigma_p = 2.5\ \mathrm{K}$, $\sigma_o = 1.0\ \mathrm{K}$,
$\mu_p = 282.0\ \mathrm{K}$ and $y = 286.0\ \mathrm{K}$, compute the gain, the
posterior mean and the posterior standard deviation.

**★3.** The observation in ★2 is in fact biased by $+1.0\ \mathrm{K}$. Compute
the error in the posterior mean.

## ★★ Applied

**★★4.** The demonstration's biased-proxy experiment reports a prior RMSE of
$2.0507\ \mathrm{K}$ (prior standard deviation $2.0\ \mathrm{K}$), an observation
RMSE of $0.5399\ \mathrm{K}$ and a gain of $0.9321$. Verify the gain from the
variances and state what the observation's "standard deviation" is being taken
to be.

**★★5.** An analyst understates the observation error: the true observation
standard deviation is $1.0\ \mathrm{K}$, but the update is run with an assumed
value of $0.5\ \mathrm{K}$ and a prior variance of $4.0\ \mathrm{K^{2}}$.
Compute the reported posterior variance, the actual error variance, and the
optimal posterior variance, and state the ratio by which the reported uncertainty
understates the true one.

**★★6.** Explain in two or three sentences why the posterior standard deviation
in the demonstration ($0.5212\ \mathrm{K}$) can be small while the reconstruction
is still biased.

## ★★★ Research-oriented

**★★★7.** Design a model-data comparison that separates calibration error from
structural model error in a palaeoclimate reconstruction. State the data needed,
the diagnostic used, and one confound the design cannot remove.

**★★★8.** A reconstruction is validated by comparing it with instrumental
observations over the last century, and it agrees to within $0.3\ \mathrm{K}$.
State why this does not establish its accuracy for a glacial period, and what
else would be required.
