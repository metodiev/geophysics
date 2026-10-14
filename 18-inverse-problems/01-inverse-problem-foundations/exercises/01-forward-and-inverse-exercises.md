# Exercises — 18-01-01 Forward vs Inverse Problems and the Practical Asymmetry

Attempt these before reading the
[solutions](./01-forward-and-inverse-solutions.md). The lesson is
[01 Forward vs Inverse Problems](../01-forward-and-inverse.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A forward operator maps $\mathbb{R}^{4}\to\mathbb{R}^{25}$. State $M$,
$N$ and the shape of $G$, and give the unit of $G_{ik}$ if data are in mGal and
model parameters in kg.

**★2.** In the demonstration a $1\%$ perturbation of the mass vector changed the
data by $0.1904\%$. (a) Compute the forward gain. (b) State in one sentence why a
gain below $1$ is expected for gravity.

**★3.** The kernel column norms for masses at $1,2,3,4\ \mathrm{km}$ are
$7.5174\times10^{-12}$, $2.5618\times10^{-12}$, $1.3940\times10^{-12}$ and
$9.0512\times10^{-13}\ \mathrm{mGal\,kg^{-1}}$. Compute the ratio between the
first and the last, and the surface anomaly produced by $10^{10}\ \mathrm{kg}$ at
each depth.

## ★★ Applied

**★★4.** $\kappa(G) = 3.6307\times10^{2}$ and the measured error gain is $166.5$.
For a $0.2\%$ data error, compute (a) the worst-case model error from $\kappa$,
(b) the expected mean model error from the measured gain. Explain the factor
between them.

**★★5.** Target a $5\%$ model error. Using the measured gain of $166.5$ and a peak
anomaly of $0.10104\ \mathrm{mGal}$, give the required noise level in percent of
peak and in mGal rms. Then state what an instrument with $5\times10^{-5}\
\mathrm{mGal}$ rms noise would actually deliver.

**★★6.** The demonstration reports $\kappa = 1.9838\times10^{3}$ and gain $417.6$
when the same masses are moved to $5,10,15,20\ \mathrm{km}$. A colleague proposes
to halve the station spacing instead, keeping the depth range, arguing that "more
stations means better conditioning". Using the scale-invariance result in the
lesson, evaluate the proposal.

## ★★★ Research-oriented

**★★★7.** Design an acquisition experiment for a buried target at $3\ \mathrm{km}$
depth in which you want $4$ independent density levels resolved to $10\%$ with
$0.05\%$ data noise. State the geometry, predict the conditioning from the
scale-invariance argument, and specify the check you would run *before* the
survey. A specification that could not be executed is a failed answer.

**★★★8.** The measured gain is constant across two orders of magnitude of noise
level ($179.6$, $161.2$, $166.7$, $165.4$, $169.5$). Derive the theoretical reason
that the gain must be independent of the noise level for a linear problem, and
explain what would break the constancy (name two mechanisms and predict the
direction of the change).
