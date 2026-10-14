---
id: 17-03-03
title: "InSAR Time Series: PS-InSAR and SBAS"
level: research
prereqs: ["17-03-02", "18-01-03", "01-14-04"]
tags: [remote-sensing, radar, insar, time-series, sbas, ps-insar, inversion]
---

# InSAR Time Series: PS-InSAR and SBAS

> All models and data in this module are **SYNTHETIC**. The deformation history,
> acquisition dates, interferometric network, noise and scatterer statistics in
> this lesson are teaching values computed by the demonstration. No real
> acquisition list, scene or station is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Assemble** a phase system $d = A\varphi$ from a set of interferometric pairs
   and **compute** its rank and null space from the connectivity of the pair
   graph.
2. **State** exactly what a disconnected network leaves undetermined, and
   **distinguish** that ambiguity from a noise limitation.
3. **Derive** the minimum-norm solution and **explain** why it is a
   regularisation choice rather than the truth.
4. **Measure** how the velocity uncertainty scales with the number of pairs and
   **explain** why the measured exponent differs from $-\tfrac12$.
5. **Quantify** the bias that a model error (an omitted seasonal term) introduces
   into a fitted rate, and **state** the condition under which it is negligible.
6. **Compute** amplitude dispersion, **interpret** it as a screening statistic,
   and **measure** its false-positive rate as a function of the number of dates.
7. **Explain** what temporal coherence does and does not detect — in particular
   why a velocity error can be invisible to it — and **use** closure phase to
   locate an unwrapping error.

## Prerequisites

- [17-03-02 InSAR: Interferometric Phase and Deformation Measurement](02-insar.md) —
  the phase, its ambiguity, coherence and speckle.
- [18-01-03 Null Space and Rank of a Linear Inverse Problem](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  what rank deficiency means for the recovered model.
- [01-14-04 Linear and Nonlinear Least Squares](../../01-mathematics/14-optimization/04-least-squares.md) —
  the estimator whose covariance is propagated here.

## 1. Intuition: one fragile measurement becomes a network

Lesson [02](02-insar.md) ended with a warning: unwrapping a single interferogram
relocates the ambiguity from one integer per pixel to one integer per region.
The remedy is not a better unwrapper. It is **more pairs**: instead of one long
interferogram, form many short ones, require them to agree, and let the
disagreement say where the unwrapping went wrong.

Two families of methods implement that idea. **SBAS** (small-baseline subsetting)
links acquisitions whose perpendicular baselines are short, which keeps coherence
high and makes unwrapping easy, and then solves for the phase at every date.
**PS-InSAR** (persistent scatterers) selects pixels that are dominated by a single
stable scatterer, so their phase is well defined even over long time spans, and
relies on a dense network of pairs to separate motion from atmosphere and orbit.

Both are linear inverse problems with an incidence matrix built from the pair
list. This lesson works that structure out from scratch, measures its limits,
and is deliberately careful about three things that are usually assumed away:
what the null space contains, what the "best" solution means, and what the
diagnostics can and cannot see.

## 2. Definitions and the phase system

Let there be $N$ acquisition dates with unknown phases $\varphi_1\ldots\varphi_N$
and $M$ interferometric pairs $(i_k, j_k)$. Each pair measures

$$d_k = \varphi_{j_k} - \varphi_{i_k} + \varepsilon_k,
\qquad \varepsilon_k \sim \text{(pair error)},$$

so

$$d = A\,\varphi + \varepsilon, \qquad
A_{k,i} = -1,\; A_{k,j} = +1 \text{ for pair } (i,j).$$

$A$ is the **incidence matrix** of a graph whose vertices are the dates and whose
edges are the pairs. The residual for a triple of pairs forming a triangle —
$\varphi_j - \varphi_i + \varphi_k - \varphi_j - (\varphi_k - \varphi_i)$ — is
identically zero if all three differences are correct: the **closure phase**.
A non-zero closure is the fingerprint of an integer error in at least one edge.

**Temporal coherence** is
$\gamma_t = \left|\frac{1}{M}\sum_k \exp\!\left(\mathrm{i}\,r_k\right)\right|$
with $r_k$ the residual of pair $k$ under a candidate model. **Amplitude
dispersion** is $D_A = \sigma_A/\mu_A$ over the dates, the standard
persistent-scatterer screening statistic.

## 3. Derivations

### 3.1 Rank, null space, and what is undetermined

The incidence matrix of a graph with $c$ connected components has

$$\operatorname{rank}(A) = N - c,
\qquad
\dim\ker(A) = c.$$

**Proof sketch.** A vector $x$ with $Ax=0$ has $x_j = x_i$ on every edge, so $x$
is constant on each connected component; those $c$ vectors are independent, and
they span the kernel because $A$ can otherwise be ordered triangularly along a
spanning tree with $N-c$ pivots.

For the demonstration's network of $N = 40$ dates and $M = 379$ pairs with
baselines up to 0.70 yr, $c=1$ and

$$\operatorname{rank}(A) = 39, \qquad \dim\ker(A) = 1.$$

The single null vector is the constant: adding a constant to every date's phase
changes no difference, so **the absolute phase of the region is never determined
by the data**. That is not noise; it is a statement about the observation.

Now delete the 45 pairs that bridge $t = 1.5\ \mathrm{yr}$, splitting the graph
into two components:

$$\operatorname{rank}(A) = 38, \qquad \dim\ker(A) = 2,$$

one constant per component. The demonstration measures what changes:

| recovered quantity | connected network | split network |
|---|---|---|
| velocity, component 1 ($t < 1.5$ yr) | 7.2315 mm/yr | 7.2315 mm/yr |
| velocity, component 2 ($t > 1.5$ yr) | 10.5124 mm/yr | 10.5124 mm/yr |
| offset between components | — | shifts by $-3.2473$ rad ($-14.617$ mm LOS) |

Two conclusions, and they must be kept apart:

- The **trend inside a component survives** disconnection exactly: the same
  numbers to four decimals. Disconnection does not degrade a rate estimate.
- The **relative offset between components is arbitrary** and must come from
  outside the network — a GNSS station, a corner reflector, or a physical
  assumption of continuity.

(The two velocities differ from each other and from the true 12 mm/yr because a
straight line cannot represent a signal containing a seasonal term; Section 3.4
quantifies that bias. This is a *model* error, not a network error, and the fact
that it produces different numbers in two different windows is exactly why a
seasonal term belongs in the model.)

### 3.2 The minimum-norm solution is a choice

Because $\dim\ker(A) > 0$, the normal equations have infinitely many solutions.
The pseudoinverse returns the one with the smallest $\|\varphi\|$:

$$\hat{\varphi} = A^{+}d = \sum_{i:\,\sigma_i>0}\frac{u_i^{\mathsf T} d}{\sigma_i}v_i,$$

computed from the singular value decomposition $A = U\Sigma V^{\mathsf T}$. The
minimum-norm solution sets each connected component's mean phase to zero. That is
a *regularisation choice*, not a property of the Earth: it reports the internal
shape of the phase history and silently fixes the reference level. Every SBAS or
PS time series has this choice buried in it, and any comparison between two
networks over the same area must compare differences, not levels.

With unbiased noise the min-norm estimate is unbiased *up to that null-space
component*. The demonstration, with pair phase noise
$\sigma_\varphi = 0.50\ \mathrm{rad}$ ($2.251\ \mathrm{mm}$ of LOS), recovers

$$\hat{v} = 11.8798\ \mathrm{mm\,yr^{-1}} \quad (\text{true } 12.000,
\text{ error } -0.1202),$$

with a residual rms of $0.4683\ \mathrm{rad}$ and $379 - 39 = 340$ degrees of
redundancy. Redundancy is what makes the fit *checkable*: with 340 more
observations than unknowns, a residual larger than the noise level is evidence of
a modelling or unwrapping error rather than bad luck.

### 3.3 How the uncertainty scales with the network

For independent pair errors of variance $\sigma^{2}$,
$\operatorname{cov}(\hat{\varphi}) = \sigma^{2}(A^{\mathsf T}A)^{+}$, so the rate
uncertainty falls as the network grows. The naive expectation is the $1/\sqrt{M}$
averaging law. The demonstration tests both parts of that expectation.

First, **connectivity before noise.** Thinning a 379-pair network at random
leaves it disconnected far more often than one would guess:

| pairs kept | fraction of random subsets that disconnect |
|---|---|
| 20 | 1.000 |
| 50 | 1.000 |
| 100 | 0.460 |
| 200 | 0.020 |

Two hundred of the 379 pairs still disconnect one time in fifty, because random
thinning isolates dates. Redundancy has to be *distributed* over the time span,
not merely large.

Second, **with connectivity held fixed** (every subset contains the 39
consecutive-date pairs, plus random extras):

| $M$ pairs | velocity error (mm/yr) | $\sqrt{M_0/M}$ |
|---|---|---|
| 59 | 2.103856 | 1.000 |
| 99 | 1.111455 | 0.772 |
| 199 | 0.631281 | 0.545 |
| 339 | 0.563234 | 0.417 |

Measured log-log slope: $-0.760$, steeper than the $-0.5$ of pure averaging. The
reason is structural: extra pairs in this network are not independent
measurements of new information, they are redundant combinations of the same
$N$ unknown phases, so their information saturates and the error falls faster
than $1/\sqrt{M}$ once the graph is well connected. **How much a given network
buys must be measured for that network**, not assumed from the pair count.

### 3.4 Model error is not noise, and it does not average away

Add no noise and fit a *straight line* to the true phases of Section 1
($v = 12\ \mathrm{mm\,yr^{-1}}$ plus an 8 mm seasonal term):

$$\hat{v} = 12.464\ \mathrm{mm\,yr^{-1}} \quad \Longrightarrow
\text{bias } +0.464\ \mathrm{mm\,yr^{-1}} \;(+3.9\%).$$

The bias exists because a sinusoid sampled over a non-integer number of cycles is
correlated with the linear term in the design matrix. It does not shrink with
more dates over the same span; it shrinks only when the record covers an integer
number of cycles or the sinusoid is modelled. With the seasonal term included the
residuals collapse from an rms of 1.59 rad to 0.00 rad in the demonstration
(noise-free) — a factor that dwarfs every network improvement in Section 3.3.

### 3.5 What temporal coherence can and cannot detect

Temporal coherence measures the **dispersion** of the residual, not its mean: a
residual phase that is the same for every pair rotates every term in the sum
equally and leaves $|\cdot|$ unchanged. The demonstration makes this concrete
with noiseless residuals and two networks — A with baselines 0.002–0.699 yr, B
with baselines 0.002–2.427 yr:

| model | network | mean residual (rad) | residual std (rad) | $\gamma_t$ |
|---|---|---|---|---|
| true, no seasonal | A | $-0.1432$ | 1.5946 | 0.1982 |
| true, no seasonal | B | $-0.0946$ | 1.4484 | 0.2932 |
| true, with seasonal | A | 0.0000 | 0.0000 | 1.0000 |
| $v \times 0.90$, with seasonal | A | $-0.0733$ | 0.0425 | 0.9991 |
| $v \times 0.90$, with seasonal | B | $-0.1818$ | 0.1299 | 0.9916 |
| $v \times 0.50$, with seasonal | A | $-0.3664$ | 0.2123 | 0.9776 |
| $v \times 0.50$, with seasonal | B | $-0.9090$ | 0.6496 | 0.8070 |

Read the last four rows together. A factor-of-two velocity error moves $\gamma_t$
by only $0.022$ in network A but by $0.193$ in network B, because the error
appears in the residual multiplied by the baseline $\Delta t$, and only the long
baselines spread it enough to dephase the sum. **The velocity information lives
in the long baselines**, and a small-baseline network — which is exactly what one
builds to keep coherence high — is structurally weak on rate. A single $\gamma_t$
number over a whole network cannot reveal that. Report the residual mean, its
spread, and the network's baseline distribution, or the diagnostic hides the
problem it was computed to detect.

### 3.6 Persistent scatterers: a screening statistic with a measurable error rate

A persistent scatterer is a pixel whose echo is dominated by one stable scatterer,
so its phase is meaningful across years. Its standard screen is the amplitude
dispersion over the $N$ dates:

$$D_A = \frac{\sigma_A}{\mu_A}.$$

The demonstration measures the distribution of $D_A$ for two populations: a
simulated stable target (amplitude $1 + 0.08\,\mathcal{N}$) and pure speckle
($|$circular complex Gaussian$|$):

| $N$ dates | stable median $D_A$ | speckle median $D_A$ | speckle fraction below 0.25 |
|---|---|---|---|
| 4 | 0.062 | 0.412 | 0.156 |
| 8 | 0.071 | 0.467 | 0.033 |
| 16 | 0.076 | 0.495 | 0.001 |
| 40 | 0.078 | 0.512 | 0.000 |

The two populations are separated by a factor of about six, so a threshold near
0.25 works well — **provided enough dates**. At four dates, 15.6% of pure-noise
pixels pass it; at forty, none do. $D_A$ is a screening statistic, so the honest
report is the threshold *and* the number of dates *and* the measured
false-positive rate on a control population. Quoting "0.25" alone is not
reproducible.

### 3.7 Closure phase and locating an unwrapping error

For three dates the differences must satisfy

$$\left(\varphi_2-\varphi_1\right) + \left(\varphi_3-\varphi_2\right)
- \left(\varphi_3-\varphi_1\right) = 0 \quad (\text{mod } 2\pi \text{ if wrapped}).$$

The demonstration computes it on clean data ($0.000000$ rad) and then injects a
single cycle slip of $2\pi$ into one pair:

$$\text{closure} = 6.283185\ \mathrm{rad}
= 28.2823\ \mathrm{mm of LOS displacement},$$

which is precisely the ambiguity of lesson [02](02-insar.md). The consequence is
practical: an integer error is invisible in the pair that contains it and
*detectable* in every triangle that includes it. Testing all triangles of the
network therefore both detects and localises unwrapping errors, and pair-level
integers can be corrected before the inversion rather than absorbed into the
answer. This is the single most useful property of a redundant network.

## 4. Worked example — a five-date network by hand

*All values SYNTHETIC.* Five dates whose true phases, referenced to the first
date, are $\varphi = (0,\ 3.0,\ 7.0,\ 11.0,\ 14.0)$ rad. The pair list is
$(1,2), (2,3), (3,4), (4,5), (1,3), (3,5)$, and the observed differences
(assumed clean except for the injected error of step 3) are the true differences
of these phases.

1. **Observations.** The observations are exactly the phase differences along
   each edge: $d = (3.0,\ 4.0,\ 4.0,\ 3.0,\ 7.0,\ 7.0)$ rad.
2. **Rank and null space.** There are $N = 5$ dates and the graph is connected
   (every date is joined through the chain $1-2-3-4$ and $-5$), so
   $\operatorname{rank}(A) = N - 1 = 4$ and $\dim\ker(A) = 1$. The null vector is
   the constant, so the common level of the five phases is undetermined: adding
   any constant to all five reproduces the same $d$ exactly.
3. **Closure tests.** Triangle $(1,2,3)$:
   $d_{23} - d_{13} + d_{12} = 4.0 - 7.0 + 3.0 = 0.000$ rad. Triangle
   $(3,4,5)$: $d_{45} + d_{34} - d_{35} = 3.0 + 4.0 - 7.0 = 0.000$ rad. Now
   suppose an operator has mis-unwrapped the pair $(3,5)$ by one cycle, so the
   reported value is $7.0 - 2\pi = 0.7168$ rad. The closure of triangle
   $(3,4,5)$ becomes $3.0 + 4.0 - 0.7168 = 6.2832$ rad — a multiple of
   $2\pi$, the unambiguous signature of an integer slip.
4. **A non-integer failure.** If instead the measured closure were
   $-4.0$ rad, no integer cycle slip could produce it ($-4.0/2\pi = -0.637$).
   That is a processing error, a decorrelation-induced phase noise excursion, or
   a genuinely aliased gradient, and it must be found and fixed rather than
   absorbed by an integer correction.
5. **Interpretation.** Four numbers and two subtractions (i) test every triangle
   in the network, (ii) distinguish an integer slip from a gross error, and (iii)
   localise the fault to the edges of the failing triangle. The inversion is then
   solved as in Section 3.2, with the common level supplied from outside.

## 5. Assumptions and regime of validity

1. **The phase is dominated by one mechanism per pixel** (a deformation plus a
   delay). Mixtures of scattering mechanisms violate the model.
2. **Errors are independent between pairs.** This is *false* in reality: pairs
   sharing an acquisition share its atmospheric screen and its orbital error, so
   the true covariance is dense and the $\sqrt{M}$ law overstates the gain.
   Section 3.3's measured exponent is what a network does under the optimistic
   assumption; the correlated case is worse
   ([04](04-insar-atmospheric-correction.md)).
3. **The deformation model is adequate.** Section 3.4 shows a +0.46 mm/yr bias
   from one omitted seasonal term — larger than most networks' noise.
4. **Unwrapping errors are integer and rare**, so closure testing finds them.
   A region with dense aliasing produces non-integer residuals that no closure
   test can repair.
5. **The look geometry is fixed** between dates (same track and pass); mixing
   geometries mixes projections and biases the rates.
6. **Amplitude dispersion screens scatterers, not targets.** A distributed
   surface can deform steadily and fail the $D_A$ test; a stable scatterer on a
   stable surface can pass and measure nothing.

## 6. Python demonstration

`code/insar_time_series_demo.py` prints seven sections: the synthetic truth and
its wrapped phases; the network's rank and null space, with the connected-versus-
split comparison; the min-norm inversion and its redundancy; the disconnection
and $\sqrt{M}$ measurements; the temporal-coherence table for the residual mean
and spread; the amplitude-dispersion distributions; and the closure phase.

```bash
cd 17-remote-sensing-gis/03-radar-remote-sensing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python insar_time_series_demo.py
```

## 7. Exercises

See
[`exercises/03-insar-time-series-exercises.md`](./exercises/03-insar-time-series-exercises.md)
and
[`exercises/03-insar-time-series-solutions.md`](./exercises/03-insar-time-series-solutions.md).

## Mastery checkpoint

Without notes: **(a)** for a network of 25 dates in two disconnected components
of 10 and 15 dates, state the rank and the dimension of the null space. **(b)** A
best-fit rate is quoted as $11.88\ \mathrm{mm\,yr^{-1}}$ from a 40-date network;
list the three assumptions that must accompany that number. **(c)** A closure
residual of $+2\pi$ on the triangle $(1,2,3)$ means what, precisely? **(d)** Why
can a factor-of-two velocity error leave the temporal coherence almost unchanged?

A worked version of (a)–(c) is in the lesson-03
[solutions](./exercises/03-insar-time-series-solutions.md).

## Common pitfalls

1. **Reporting an absolute phase (or an absolute offset) from a network.** Only
   differences within a connected component are determined.
2. **Assuming more pairs is always better.** Random thinning disconnects a
   network; information saturates.
3. **Trusting a rate from a network with no long baselines.** The velocity
   information is in the long baselines, and $\gamma_t$ will not tell you.
4. **Fitting a straight line to a seasonal signal.** The bias is a few per cent
   and does not average away.
5. **Quoting a $D_A$ threshold without the number of dates.**
6. **Treating $\gamma_t$ as a probability.** It is a similarity measure, and a
   constant model error can leave it at 1.0.
7. **Correcting the inverted phases instead of the pair integers.** Closure
   testing must happen before the inversion, otherwise the error is smeared into
   every date.

## Related modules

- [02 InSAR: Interferometric Phase and Deformation Measurement](02-insar.md) —
  the ambiguity this lesson manages.
- [04 Atmospheric and Orbital Error Correction in InSAR](04-insar-atmospheric-correction.md) —
  the correlated errors that break the independence assumed here.
- [05 InSAR for Earthquakes, Volcanoes, Subsidence and Landslides](05-insar-applications.md) —
  the geophysical interpretation of the estimated time series.
- [18-01-03 Null Space and Rank of a Linear Inverse Problem](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the same rank and null-space arguments in general form.
- [01-14-04 Linear and Nonlinear Least Squares](../../01-mathematics/14-optimization/04-least-squares.md) —
  the estimator and its covariance.
