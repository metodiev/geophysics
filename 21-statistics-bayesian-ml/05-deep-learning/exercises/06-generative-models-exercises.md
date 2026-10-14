# Exercises — 21-05-06 GANs, VAEs and Diffusion Models

Attempt these before reading the
[solutions](./06-generative-models-solutions.md). The lesson is
[06 Generative Models](../06-generative-models.md). All data are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the variational autoencoder's evidence lower bound and name its two
terms.

**★2.** Write the adversarial objective and state what the discriminator's optimal
solution is.

**★3.** Write the forward diffusion step and state what quantity the model is
trained to predict.

## ★★ Applied

**★★4.** The demonstration's ELBO values are $-11\,682.9057$ (prior),
$-7\,285.4335$ (sample mean) and $-7\,285.4324$ (exact posterior). Compute the
improvement from the prior and the residual gap to the exact posterior, and state
why the maximum equals the log evidence here.

**★★5.** A poor generator gives a discriminator AUC of $0.9692$ and a matched
generator $0.4857$. State the chance level, compute each as a distance from it, and
state why an AUC near $0.5$ is necessary but not sufficient.

**★★6.** For the linear schedule from $\beta_1 = 10^{-4}$ to
$\beta_{1000} = 0.02$, the demonstration reports $\bar\alpha_1 = 0.999900$ and
$\mathrm{SNR} = 9999.0000$ at step 1. Verify that $\bar\alpha_1/(1-\bar\alpha_1)$
gives the reported SNR, and compute the SNR at step $100$ from
$\bar\alpha_{100} = 0.897018$.

## ★★★ Research-oriented

**★★★7.** Specify a study that compares a VAE, a GAN and a diffusion model for
**facies simulation** on a synthetic reservoir with known statistics. State the
design, the physical statistics used for evaluation, the metrics, the replicate
count, and how mode collapse would be detected.

**★★★8.** Specify an experiment that uses a conditional generative model to
**augment** a small labelled data set, with the leakage risk explicitly controlled.
State the split protocol, the control arm without augmentation, the metric, and the
outcome that would show the augmentation is merely a regulariser.
