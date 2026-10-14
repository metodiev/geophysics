# Exercises — 21-05-05 Autoencoders for Compression and Denoising

Attempt these before reading the
[solutions](./05-autoencoders-solutions.md). The lesson is
[05 Autoencoders](../05-autoencoders.md). All data are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the autoencoder objective and state what the bottleneck dimension
controls.

**★2.** A linear $2\to1\to2$ autoencoder gives a reconstruction MSE of $0.010474$
and a one-component PCA gives $0.010474$. State the theoretical reason they agree
and why that agreement is a useful test.

**★3.** On the parabola, PCA gives $0.046119$ and the nonlinear autoencoder
$0.000013$. Compute the ratio and state in one sentence where the gain comes from.

## ★★ Applied

**★★4.** The noisy input has MSE $0.082538$ against the clean signal. The
clean-trained network achieves $0.072169$ and the denoising network $0.052103$.
Compute the fraction of the corruption removed by each and state which one was
asked to do what.

**★★5.** Compute the ratio of the denoising network's error to the clean-trained
network's error, and express it as a percentage reduction. State what changes in
the experiment and what stays fixed.

**★★6.** State the criterion for choosing the corruption level and the data it
must be evaluated on. Then state why a bottleneck wider than the input is
guaranteed to fail as a representation learner.

## ★★★ Research-oriented

**★★★7.** Specify an experiment that tests whether an autoencoder's latent code is
**useful** rather than merely compressive on a geophysical task of your choice.
State the downstream task, the metric, the comparison against a raw-feature
baseline, the blocked split, and what outcome would show the code is worthless.

**★★★8.** Specify a study comparing an autoencoder denoiser against a classical
denoiser (for example a Wiener or $f$–$x$ deconvolution filter) on synthetic data
with a **mismatched** noise model. State the design, the metric, the number of
noise models, and the predicted ordering, including which method should win when
the assumed noise model is wrong.
