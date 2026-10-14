# Solutions — 06-06-07 Resolving Discrepancies Between Tomographic Models

Exercises:
[07-tomography-controversies-exercises.md](07-tomography-controversies-exercises.md).

## ★ Foundational

**1.** $1.42/2.60 = 0.546$ of the first model's rms; $1.42/2.21 = 0.642$ of the
second; $1.42/3.12 = \mathbf{0.455}$ of the true anomaly's rms. So the two
images differ by about half of the signal they both claim to contain — the
typical situation that makes "which model is right?" a well-posed question only
after the resolution is quoted.

**2.** $1-\rho = 0.584$, i.e. the two images share only about 42 per cent of
their variance: a reader who averages them (a common practice) is averaging two
partly independent answers, and the mean is not an estimate of the Earth unless
the differences are random. They are not: the difference is a systematic
displacement caused by the two different regularisations.

**3.** Agreement 0.966 means 96.6 per cent of the ensemble agrees with the
majority, so about $0.034\times30 \approx \mathbf{1}$ model per cell disagrees.

## ★★ Applied

**4.** Only the second claim is supported. The measured correlation in the
worst-covered quarter is 0.050, i.e. the two models are essentially unrelated
there, while in the best-covered quarter it is 0.447 — the disagreement is
concentrated exactly where the ray count is low, which is the signature of a
resolution difference rather than of a structural disagreement. To support the
first claim one would need high *and* resolved agreement in the well-covered
region together with a systematic difference in the poorly covered one, i.e. the
opposite pattern.

**5.** The reader gains a model in which the *unconstrained* part of the model —
the part that was arbitrary in one geometry and invisible in the other — has been
removed: mutual agreement rises to 0.934 and the difference between the two
inversions of the joint data falls to $2.2\times10^{-3}$. The reader does **not**
gain accuracy: the rms error against the truth is unchanged at
$1.37\times10^{-2}$, because the missing angular coverage is still missing. The
correct sentence for a paper is therefore "the joint inversion resolves the
inconsistency between the two data sets", not "the joint inversion is more
accurate".

**6.** Candidate explanations, each with the number to request: (i) damping
difference — ask for $\lambda$ and the achieved misfit (measured factor of two
here); (ii) different parametrisation, e.g. cell size — ask for the grid and the
grid-sensitivity test (measured rms model error change of 22 per cent across
grids); (iii) different coverage — ask for the ray counts per cell and the
resolution matrix column (measured correlation drop from 0.447 to 0.050 between
the best- and worst-covered quarters); (iv) different noise level assumed —
ask for $\sigma$ and the misfit target; (v) a different reference model —
ask for $v_0$; (vi) different data subsets within the same catalogue — ask for
the station and event lists.

## ★★★ Research-oriented

**7.** Protocol: (1) compare *data*, not models — list common events/stations
and the residuals each model predicts; (2) project both models into a common
basis with a stated maximum degree, and report the projection residual;
(3) compute the mutual correlation as a function of local coverage, reporting the
correlation for each coverage quartile; (4) compute each model's resolution
matrix (or its first singular vectors) and report $|R_{kk}|$ and the point-spread
length at the disputed cells; (5) build an ensemble for each model by varying
damping within its own reported misfit range, and compare the two ensembles'
spread with the difference being disputed; (6) decide: if the difference lies
inside the union of the two ensembles' spreads, report it as unresolvable with the
current data and specify the rays that would resolve it; if it lies outside, report
it as a data-driven discrepancy and test it with independent data. The decision
rule at every step is the same: compare the disputed difference with the
measured resolution and uncertainty of the two models, never with zero.

**8.** The objection is partly right and can be answered quantitatively. The
ensemble is arbitrary in *composition* — five dampings and six realisations is a
choice — but the conclusions drawn from it are not, because (i) the measured
amplitude spread across that ensemble (a factor of two) is the same order as the
spread produced by damping alone in the single-data-set test, and (ii) the sign
agreement is high (0.966) *and stable* across the whole damping range. A reviewer
can therefore accept "the sign is robust to damping and noise within the tested
range" while rejecting "the amplitude is known to a factor of two" — which is the
honest reading. To strengthen the construction, the ensemble should include the
damping values that the model's own parameter-choice rule can justify, and the
prior range of the noise level, rather than an arbitrary ladder of five numbers.
