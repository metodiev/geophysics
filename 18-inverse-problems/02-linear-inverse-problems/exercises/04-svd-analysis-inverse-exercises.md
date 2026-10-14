# Exercises — 18-02-04 SVD Analysis: Model Resolution and Data Importance

Attempt these before reading the
[solutions](./04-svd-analysis-inverse-solutions.md). The lesson is
[04 SVD Analysis](../04-svd-analysis-inverse.md). All models are **SYNTHETIC**
teaching values.

## ★ Foundational

**★1.** State what each singular triplet $(\sigma_i,\mathbf{u}_i,\mathbf{v}_i)$
means physically, and write the truncated-SVD estimator.

**★2.** Twelve rays include three exact duplicates and one half-amplitude copy.
Compute the importance of each duplicate and of the half-amplitude ray, and state
the sum of all importances.

**★3.** The measured rms noise in the estimate rises from
$5.36\times10^{-4}\ \mathrm{s}$ at $k=1$ to $7.503\times10^{-3}\ \mathrm{s}$ at
$k=8$. Compute the ratio and explain which singular values drive it.

## ★★ Applied

**★★4.** The resolution matrix has $\operatorname{tr}R = 8$ for a 12-cell model.
(a) How many independent model combinations does the experiment support?
(b) What is the mean value of $\operatorname{diag}R$? (c) What happens to
$\operatorname{tr}R$ and to $\dim\mathcal{N}(G)$ if one additional independent ray
is added?

**★★5.** Cell 0 has $R_{jj} = 0.8182$ and a kernel width of 4.43 km; cell 3 has
$R_{jj} = 0.7760$ and a width of 2.44 km. (a) Which cell would you quote for a
regional statement? (b) Explain the trap in reporting $R_{jj}$ alone.

**★★6.** The retrieval error decomposes into a bias
$\lVert(R-I)\mathbf{m}_{\text{true}}\rVert = 0.368770\ \mathrm{s}$ and a noise term
of expected norm $0.025992\ \mathrm{s}$. (a) Which dominates? (b) Predict the rms
per-cell error if both terms are spread over 12 cells. (c) The demonstration measures
$0.101661\ \mathrm{s}$ over 300 realisations — reconcile this with (b).

## ★★★ Research-oriented

**★★★7.** Using the two-noise trade-off table, construct the rule you would use to
choose $k$ in an automated pipeline when $\sigma$ is estimated from the data rather
than known. State the estimand, the criterion, and what you would report when the
$k$-versus-error curve is flat.

**★★★8.** Design a survey addition worth at most five new rays that maximises the
increase in $\sum_{i\le8}\log\sigma_i$ (the $D$-optimality criterion) for the
demonstration's geometry. Give the rays, the predicted rank and resolution change,
and the one assumption about the existing rays that your design relies on.
