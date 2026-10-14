# Solutions — 25-05-04 Project: Trans-Dimensional Bayesian Inversion

Reference solutions. Every number is printed by
[`code/transdimensional_demo.py`](../code/transdimensional_demo.py); all data are
**SYNTHETIC**.

## ★1. The joint posterior

$$p(k, b, \mathbf m \mid \mathbf d)\ \propto\
\underbrace{p(\mathbf d \mid \mathbf m)}_{\text{Gaussian likelihood}}
\ \underbrace{\tfrac{1}{K_{\max}}}_{\text{prior on }k}
\ \underbrace{\tfrac{1}{\binom{19}{k-1}}}_{\text{boundaries given }k}
\ \underbrace{\prod_{j=1}^{k} N(m_j; 0, \sigma_m^2)}_{\text{values given }k},\qquad
k = 1,\dots,5 .$$

The prior on the boundary positions is uniform **given $k$**, so its normalisation
$\binom{19}{k-1}$ depends on the dimension: a model with four layers has
$\binom{19}{3} = 969$ possible boundary sets, one with three layers only
$\binom{19}{2} = 171$. That factor is not a technicality — it is one half of the
Occam argument, and it is why the *evidence* and the *posterior odds* differ (★★4).

## ★2. The birth (split) acceptance ratio

For a birth from a $k$-layer model that inserts a boundary at an empty position
(choosing it uniformly from $N_e = 20-k$ possibilities) and splits a layer of value
$v$ into $(v-u,\,v+u)$ with $u \sim N(0,\sigma_u^2)$:

$$\alpha = \min\Bigl(1,\
\frac{L'}{L}\cdot
\frac{N(v-u)N(v+u)}{N(v)}\cdot
\frac{\binom{19}{k-1}}{\binom{19}{k}}\cdot
\frac{p_d(k+1)}{p_b(k)}\cdot
\frac{N_e}{k}\cdot
\frac{1}{q(u)}\cdot 2\ \Bigr),$$

| factor | meaning |
|---|---|
| $L'/L$ | likelihood ratio (the two profiles differ) |
| $N(v-u)N(v+u)/N(v)$ | change in the value prior: one parameter becomes two |
| $\binom{19}{k-1}/\binom{19}{k}$ | change in the boundary-set prior, i.e. one more constraint on where the boundaries may be |
| $p_d(k+1)/p_b(k)$ | the reverse move (death) has a different selection probability |
| $N_e/k$ | the death move chooses one of $k$ boundaries, the birth one of $N_e$ empty positions |
| $1/q(u)$ | the proposal density of the split offset |
| $2 = |J|$ | the Jacobian of $(\mathbf m, u) \to (v_L, v_R)$ |

The death move is the exact inverse: merge
$v = (v_L+v_R)/2$, $u = (v_R-v_L)/2$, $|J| = 1/2$, and the two acceptances multiply
to one on a round trip — the check that the implementation is consistent.

## ★3. The exact Gaussian evidence

Conditioning on the boundary set $b$ and integrating over the layer values,

$$\mathbf d \sim N\bigl(\mathbf 0,\ \mathbf C_b\bigr),\qquad
\mathbf C_b = \mathbf G\mathbf S_b\mathbf G^{\mathsf T} + \sigma_d^2\mathbf I,\qquad
\mathbf S_b = \sigma_m^2\mathbf P_b\mathbf P_b^{\mathsf T},$$

$$\log p(\mathbf d\mid b) = -\tfrac12 \mathbf d^{\mathsf T}\mathbf C_b^{-1}\mathbf d
-\tfrac12\log|\mathbf C_b| - \tfrac{n}{2}\log 2\pi .$$

The $\log|\mathbf C_b|$ term is the Occam factor: adding a layer increases the
volume of data space the model can explain, and $|\mathbf C_b|$ grows with that
volume, so the penalty is *automatic* and grows with the number of parameters that
the data do not constrain. The fitted term
$-\tfrac12\mathbf d^{\mathsf T}\mathbf C_b^{-1}\mathbf d$ always rewards extra
parameters (a larger model can always fit better), and the determinant term balances
it. That is why a maximum-likelihood comparison of models with different dimensions
is meaningless while an evidence comparison is not.

## ★4. Posterior odds, prior odds and the Bayes factor

$$\text{posterior odds} = \frac{P(4)}{P(3)} = \frac{0.0675}{0.9318}
= \frac{1}{13.80},$$
$$\text{prior odds} = \frac{\binom{19}{2}}{\binom{19}{3}} = \frac{171}{969}
= \frac{1}{5.667},$$
$$\mathrm{BF}_{43} = \frac{\text{posterior odds}}{\text{prior odds}}
= \frac{0.07244}{0.17647} = 0.410 = \frac{1}{2.44} .$$

Decomposition: the **prior on the number of boundaries** accounts for a factor
$5.667$ (log 1.734) and the **data** for a factor $2.44$ (log 0.891); together
$5.667 \times 2.44 = 13.8$, the observed odds. So even if the evidence were
completely insensitive to the number of layers ($\mathrm{BF}=1$), the posterior would
still favour $k=3$ by $5.7$ to one — the answer is partly a consequence of the prior.
That is worth reporting explicitly, and it is why the project requires the
decomposition rather than a bare $P(k)$.

## ★5. Counting the model space

| layers $k$ | boundaries | sets | models enumerated |
|---|---|---|---|
| 1 | 0 | 1 | 1 |
| 2 | 1 | 19 | 19 |
| 3 | 2 | 171 | 171 |
| 4 | 3 | 969 | 969 |
| 5 | 4 | 3876 | 3876 |
| total | | | **5036** |

matching the printed 5036. The full space of boundary sets is
$\sum_{k=1}^{20}\binom{19}{k-1} = 2^{19} = 524288$. The missing $k=6$ family contains
$\binom{19}{5} = 11628$ sets — $2.2\%$ of the space, but as they are only weakly
favoured their exclusion changes $P(k\le5)$ by far less than the sampler's bias. This
is the calculation to do before trusting an "exact" enumeration: state what fraction
of the model space was covered and how the truncated prior was renormalised.

## ★6. Bias or Monte Carlo noise?

Birth attempts: the sampler spends $30\%$ of iterations on value perturbations
(accepted $0.354$), $30\%$ on boundary displacement, and the remainder on structural
moves, of which half are births when both birth and death are possible. So

$$n_\text{birth attempts} \approx 0.4 \times 0.5 \times 120000 = 24000,\qquad
n_\text{accepted births} \approx 0.007 \times 24000 \approx 170 .$$

The discrepancy is $0.0675 - 0.0165 = 0.051$. A binomial standard error for a
proportion near $0.068$ with an effective sample size of the order of the number of
transitions ($\sim 340$ births and deaths) is

$$\sqrt{\frac{0.0675 \times 0.9325}{340}} = 0.014,$$

so the discrepancy is about $3.7\sigma$ — larger than the noise but not
overwhelming. **The decisive evidence that it is a bias comes from the run length:**
the same sampler with five times as many iterations gives the same low value
($0.021$ rather than $0.068$), and the profile was already accurate at $0.017$
km/s. A ten-times longer run would reduce the binomial standard error to about
$0.004$ and would leave a discrepancy of $0.05$ — more than ten standard errors.
Extra iterations cannot repair a proposal that rarely enters a region of the model
space; they only measure the biased answer more precisely.

## ★7. How the profile can be right while $P(k)$ is wrong

The posterior mean profile is an average over the model space weighted by the
posterior:

$$\bar m(z) = \sum_k P(k)\,\bar m_k(z) .$$

The $k=3$ contribution is $93\%$ of the mass and its profile is tightly determined
(sd $0.06$–$0.08$ km/s); the $k=4$ contribution is a small, similar-shaped
correction. Changing $P(4)$ from $0.068$ to $0.017$ changes the weighted mean by at
most a few per cent of the difference between the $k=3$ and $k=4$ profiles, which is
why the mean agrees to $0.017$ km/s even when the odds do not. What a user cares about
depends on the question: for a *value* at a depth the sampler is adequate; for a
*structural* question — how many interfaces, how thick is a layer, is there a
discontinuity at all — the sampler's answer is wrong by a factor of three and would
be reported as a confident geological statement. The error bars on the structural
question are precisely what the sampler failed to compute.

## ★8. Why chain agreement is not validation

All three chains share the same proposal. Whether the chain enters the $k=4$ region is
decided by the *proposal*, not by the starting model: if a birth is accepted at rate
$0.007$ and the accepted births cluster in one corner of the $k=4$ region, every chain
will spend the same undersampled time there. Starting-model dependence is the only
pathology that multi-start chains can detect, and it is absent here — which is exactly
the trap.

Diagnostics that would catch the shared bias:

1. **An exact or brute-force reference**, as in this project: require the sampler to
   reproduce $P(k)$ on a synthetic problem whose answer is known exactly before it is
   applied elsewhere.
2. **Different *kinds* of proposal**: a split-based birth and a prior-draw birth have
   different failure modes; agreement between them is far more informative than
   agreement between runs of the same code.
3. **Prior sensitivity**: vary $K_{\max}$ and $\sigma_m$. If the posterior on $k$ moves
   in a way not predicted by the prior-odds ratios of ★4, the sampler is not
   exploring the space it claims to.
4. **Jump-count auditing**: report the number of accepted trans-dimensional moves and
   the posterior mass of each $k$ as a function of run length. A value still drifting
   at the end of the run is not converged, and a value that plateaus at the wrong
   place is biased.
5. **A $\hat R$ on the model indicator is not enough**, because it only measures
   between-chain variance and all chains share the proposal.

## ★★★9. A validation protocol for an unenumerable problem

**1. Build the test-bed before the study.** Take the real problem's data type,
dimensions, noise level and prior, and generate a synthetic dataset from a *known*
model with a *known* number of discontinuities. The test-bed must be hard in the same
way the real problem is hard: the same signal-to-noise ratio, the same spatial
sampling, the same prior breadth. A test-bed that is easier validates nothing.

**2. Obtain a reference posterior.** In order of preference: (a) an exact enumeration
when the model space is small enough (as here, $5036 \ll 2^{19}$); (b) an analytic
evidence for a *restricted* class plus an importance-sampling correction; (c) a
brute-force reference, for example Bayesian model averaging over fixed-dimension
inversions $k=1,\dots,K_{\max}$, each run to convergence with its own evidence — this
is expensive but only needs to be done once, offline, on the test-bed.

**3. Measure the bias, not just the variance.** Run the sampler on the test-bed and
report $\max_k |P_\text{MCMC}(k) - P_\text{ref}(k)|$, the total variation distance,
and the difference between the posterior mean profiles at the depths of interest.
Compare each against the Monte Carlo standard error, and iterate on the proposals
until the bias is below the error at an affordable run length. **Only then apply the
sampler to the real data.**

**4. Diagnostics on the real problem.**

- Multiple chains with dispersed starting dimensions and seeds; report the
  between-chain spread of $P(k)$ *and* the accepted jump counts.
- Prior sensitivity: $K_{\max} \in \{k_\text{MAP}+1, k_\text{MAP}+3\}$ and
  $\sigma_m$ varied by a factor of two, reporting the induced change in $P(k)$
  against the prediction from the changed prior odds.
- Effective sample size of the model indicator and of the profile at the depths of
  interest (not of the raw iteration count).
- Acceptance rates for every move type, and the fraction of iterations in which the
  dimension changed.

**5. Proposal improvements to test, in order of expected value.**

1. **Collapse the linear parameters.** For the linear-Gaussian part, integrate the
   layer values out analytically and sample only the dimension and the boundary
   positions; each proposed dimension change is then evaluated with its exact
   marginal likelihood. This removes the component that made the acceptance rate
   $0.007$ and is the single largest improvement available for this problem class.
2. **Informed birth.** Propose the boundary position and the two new values by
   minimising the local misfit, and correct the acceptance with the resulting
   proposal density (an importance-sampling correction). This is the standard fix for
   sharply peaked likelihoods.
3. **Delayed acceptance.** Screen proposals with a cheap approximation (a linearised
   or coarse-grid misfit) before the full evaluation, which buys many more
   independent samples per second at the cost of a corrected acceptance ratio.
4. **Parallel tempering across dimensions** to escape the low-likelihood valleys
   between the wells of the layer-count space.

**6. What to state if the real and synthetic cases disagree.** Do not report the
layer-count posterior as a result. Report instead: the value uncertainty at the depths
of interest (well constrained and demonstrably accurate), the range of $P(k)$ over the
prior choices tested, and the statement that the structural uncertainty is unresolved
because the sampler's bias on the test-bed exceeded its standard error for the real
problem's configuration. An unresolved structural question reported as unresolved is a
valid result; a structural posterior computed with a biased sampler and reported
without qualification is not.
