---
id: 18-03-03
title: "Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle"
level: research
prereqs: ["18-03-02"]
tags: [inverse-problems, regularization, parameter-choice, l-curve, cross-validation]
---

# Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the L-curve corner criterion, the generalised cross-validation
   function and the discrepancy principle from their definitions, and **state**
   the assumption each one needs.
2. **Measure** how reproducibly each rule selects the regularisation parameter
   over many noise realisations of the same experiment.
3. **Measure** the price each rule pays in model error relative to an oracle that
   knows the truth.
4. **Demonstrate** three failure modes: a wrong noise level, correlated noise and
   a trade-off curve with no corner.
5. **Diagnose** a badly chosen parameter from residual information alone, without
   knowing the truth.
6. **Report** a parameter choice so that a reader can reproduce it, and
   **explain** why no rule in this lesson is "the correct one".

All models and data in this module are **SYNTHETIC**. The kernel is the exact
2-D line-mass gravity formula; the density distribution, station grid, depth and
noise are chosen teaching values. The only physical constant is
$G = 6.67430\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$.

## Prerequisites

- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](02-tikhonov.md) —
  the filter factors, the exact bias–variance decomposition and the oracle
  parameter that this lesson tries to approximate.

## 1. The problem

Lesson [18-03-02](02-tikhonov.md) produced an optimal $\alpha$ from a formula
that contains $m_{\mathrm{true}}$. In a real inversion $m_{\mathrm{true}}$ does
not exist, so the entire question is: **what function of the data selects
$\alpha$, and what does that function assume?**

Three rules dominate practice.

- **L-curve**: plot $\log\|Km_\alpha-d\|$ against $\log\|m_\alpha\|$ and take the
  corner. Assumes the curve has a corner. Uses no noise estimate.
- **Generalised cross validation (GCV)**: choose the $\alpha$ that minimises an
  estimate of the misfit on data left out of the fit. Assumes the noise is white
  and the data are exchangeable. Uses no noise estimate.
- **Discrepancy principle**: choose the $\alpha$ whose residual matches the
  known noise level, $\|Km_\alpha-d\|^2 \approx n\sigma_e^2$. Assumes
  $\sigma_e$ is known and the noise is white.

Each is a *statistical or geometric* statement, and each can fail. This lesson
measures the failures rather than ranking the rules, because the ranking depends
on the problem to a degree that makes a general ranking dishonest.

## 2. Derivations

### 2.1 The L-curve and its curvature

Define $\rho(\alpha) = \|Km_\alpha - d\|_2$ (rising in $\alpha$) and
$\eta(\alpha) = \|m_\alpha\|_2$ (falling in $\alpha$). In coordinates
$X(t) = \log\rho$, $Y(t) = \log\eta$, $t = \log\alpha$, the curvature is

$$\kappa_L(t) = \frac{|X'Y'' - Y'X''|}{\left(X'^2+Y'^2\right)^{3/2}} .$$

The corner is $\arg\max_t \kappa_L$. Two practical points follow from the formula
rather than from experience:

1. The derivatives must be estimated, and any smoothing of the discrete curve
   changes the maximum. The rule therefore has a **second, usually unreported
   parameter**.
2. Where the curve is straight, $\kappa_L \to 0$ and the corner is not
   identifiable at all. The corner exists only when the trade-off has a
   well-defined knee.

### 2.2 Generalised cross validation

Let $A(\alpha) = K(K^{\mathsf T}K+\alpha I)^{-1}K^{\mathsf T} = U\mathrm{diag}(f_i)U^{\mathsf T}$
be the influence (hat) matrix, so $Km_\alpha = A d$. The ordinary cross-validation
estimate of predictive error deletes one datum at a time and refits; the
shortcut that avoids $n$ refits is the "leverage" identity, giving the
generalised form

$$G(\alpha) = \frac{\|(I-A)d\|_2^2/n}{\left(1-\mathrm{tr}A/n\right)^2}
= \frac{\|Km_\alpha-d\|_2^2/n}{\left(1-\sum_i f_i/n\right)^2}.$$

Because $Km_\alpha = \sum_i f_i y_i u_i$, the numerator is
$\sum_i(1-f_i)^2y_i^2$: GCV balances the *unexplained* data against the
*effective number of fitted parameters* $\sum_i f_i$. No noise level appears.

### 2.3 The discrepancy principle

If the noise is white with known standard deviation $\sigma_e$, then
$\mathbb E\|e\|^2 = n\sigma_e^2$ and $\|e\|^2/\sigma_e^2 \sim \chi^2_n$. Choosing
$\alpha$ so that

$$\|Km_\alpha - d\|_2^2 = n\sigma_e^2$$

gives the *most smoothed* model whose residual is still statistically consistent
with the noise. In the demonstration the residual ratio at the selected
$\alpha$ is $1.0027$, i.e. the crossing is located by construction.

Note what the rule does *not* do: it does not use the shape of the trade-off
curve, and it says nothing about the model norm. It is a pure
goodness-of-fit test with a one-sided interpretation.

## 3. What is measured on one realisation

The demonstration uses the same synthetic profile as
[18-03-02](02-tikhonov.md): 64 stations and 64 cells at $0.6\ \mathrm{km}$ depth,
$\kappa_2 = 1.163\times10^{6}$, noise $1.1063\ \mathrm{mGal}$ ($0.50\%$ of the
peak), $n\sigma_e^2 = 6.6178\times10^{-5}$ in standard-form units.

| rule | $\alpha$ | relative model error | ratio to oracle |
|---|---|---|---|
| oracle (needs the truth) | $9.331\times10^{-3}$ | $0.02553$ | 1.00 |
| L-curve corner | $2.673\times10^{-5}$ | $0.26884$ | 10.53 |
| GCV | $7.848\times10^{-4}$ | $0.05596$ | 2.19 |
| discrepancy principle | $3.778\times10^{-3}$ | $0.03198$ | 1.25 |
| no regularisation | $10^{-12}$ | $1333.98$ | $5.2\times10^{4}$ |
| extreme smoothing | $10^{1}$ | $0.92744$ | 36.33 |

The rules differ from each other by more than two decades in $\alpha$, and their
errors differ by a factor of $8$. On this problem the discrepancy principle is
closest to the oracle and the L-curve corner is farthest, which is the opposite
of the folklore that the L-curve is a safe default.

### The L-curve corner is systematically too small here

The corner solution has $\|Km_\alpha-d\|^2 = 0.507\,n\sigma_e^2$: a residual
**below** the noise level, which means the solution is partly fitting noise. That
is a diagnostic available without the truth, and it is the reason to distrust a
corner that sits at the left end of the curve.

The hidden smoothing parameter is visible in the same run:

| spline smoothing $s$ | corner $\alpha$ | max curvature | error | res$^2/(n\sigma^2)$ |
|---|---|---|---|---|
| none (interpolating) | $2.673\times10^{-5}$ | 2.56 | 0.2688 | 0.507 |
| $10^{-6}$ | $4.190\times10^{-5}$ | 29.8 | 0.2192 | 0.519 |
| $10^{-4}$ | $6.903\times10^{-5}$ | 28.4 | 0.1717 | 0.534 |
| $10^{-3}$ | $2.123\times10^{-4}$ | 31.9 | 0.0990 | 0.571 |
| $10^{-1}$ | $1.828\times10^{-4}$ | $3.9\times10^{4}$ | 0.1066 | 0.566 |

The corner moves by a factor of $6.8$ across the choices, and the resulting
error changes by a factor of $2.7$. A paper that reports "the L-curve corner"
without saying how the curvature was computed has not reported its method.

## 4. How reproducible is a rule?

A single realisation cannot distinguish a rule that is *biased* from a rule that
is *noisy*. The demonstration therefore repeats the whole inversion 300 times
with fresh noise and measures both.

| rule | median $\alpha$ | IQR of $\log_{10}\alpha$ | 10–90% error range | median error | error / oracle |
|---|---|---|---|---|---|
| oracle | $6.912\times10^{-3}$ | 0.07 | 0.0169 – 0.0267 | 0.02187 | 1.000 |
| L-curve | $6.990\times10^{-5}$ | 0.39 | 0.0749 – 0.3057 | 0.16533 | 7.558 |
| GCV | $8.153\times10^{-4}$ | 0.20 | 0.0347 – 0.4392 | 0.05122 | 2.341 |
| discrepancy | $3.301\times10^{-3}$ | 0.15 | 0.0192 – 0.0470 | 0.02730 | 1.248 |

Three readings, and they are the substance of this lesson:

1. **Reproducibility is decent on this problem.** An interquartile range of
   0.15–0.39 decades means the selected $\alpha$ varies by a factor of 1.4 to 2.5
   between realisations of the *same* experiment. The parameter is not chaotic,
   but it is not a property of the Earth either: it is a function of the noise
   realisation.
2. **The rules are biased, and that is the dominant error.** The L-curve's median
   error is 7.6 times the oracle's; its IQR in $\alpha$ accounts for only part of
   that. Bias, not variance, is what makes the corner rule expensive here.
3. **The oracle is not attainable, and the gap to it is not small.**
   $2.34\times$ for GCV means a model error 2.3 times larger than the best
   achievable with the same estimator family. That factor is the price of not
   knowing the answer, and it belongs in the error budget.

The 10–90% error range is the number to quote for a single experiment: for GCV
it spans $0.035$ to $0.44$, a factor of 13. A method whose error varies by a
factor of 13 across noise realisations cannot be described by a single number.

## 5. Failure mode 1: the noise level the discrepancy principle assumes

The rule needs $\sigma_e$; nearly everyone estimates it. The demonstration
supplies $\sigma_{\text{assumed}} = \text{factor}\times\sigma_{\text{true}}$ and
measures the consequence over 300 realisations.

| $\sigma_{\text{assumed}}/\sigma_{\text{true}}$ | median $\alpha$ | median error | error / oracle |
|---|---|---|---|
| 0.25 | $5.561\times10^{-12}$ | 626.7 | $2.86\times10^{4}$ |
| 0.50 | $1.431\times10^{-9}$ | 40.01 | 1829 |
| 1.00 | $3.301\times10^{-3}$ | 0.0273 | 1.248 |
| 2.00 | $1.187\times10^{-2}$ | 0.02563 | 1.172 |
| 4.00 | $2.661\times10^{-2}$ | 0.04751 | 2.172 |

The failure is **asymmetric**, and the asymmetry is large. Underestimating
$\sigma_e$ by a factor of four drives $\alpha$ to the bottom of the grid and the
error up by four orders of magnitude: the rule concludes that the data are
excellent, stops regularising, and fits noise. Overestimating by a factor of two
actually *improves* the error slightly here, and by a factor of four it costs
only a factor of $2.17$.

That asymmetry is a measurement about this problem, not a law: it follows from
the curvature of the trade-off, which is much steeper on the under-smoothing
side. The practical rule it does justify is: **when in doubt, err on the side of
too much smoothing**, and never quote a discrepancy-principle $\alpha$ without
the $\sigma_e$ that produced it.

## 6. Failure mode 2: correlated noise

GCV's denominator counts $n$ independent data. Real potential-field noise is
correlated along a profile. The demonstration generates white noise, smooths it
with a 5-sample moving average and rescales to the *same rms*, so $\sigma_e$ is
unchanged but the effective number of independent data is smaller.

| noise | median $\alpha$ (GCV) | GCV error/oracle | median $\alpha$ (discrepancy) | discrep. error/oracle |
|---|---|---|---|---|
| white | $7.848\times10^{-4}$ | 2.408 | $3.317\times10^{-3}$ | 1.242 |
| correlated | $6.754\times10^{-4}$ | 2.830 | $3.255\times10^{-3}$ | 1.324 |

Both rules degrade, GCV more (2.41 to 2.83; 1.24 to 1.32), and both choose a
slightly smaller $\alpha$ — the under-smoothing direction. The mechanism is
instructive: GCV under-smooths because $\mathrm{tr}\,A$ computed for independent
data over-counts the parameters that are actually free; the discrepancy
principle under-smooths because $\|e\|^2$ is no longer distributed as
$\sigma_e^2\chi^2_n$ — with correlated noise its variance is larger, so the true
threshold is above $n\sigma_e^2$ and the rule stops smoothing too early.

Neither failure is large here (factors of 1.2–1.3 in error), which is why
correlated noise is a common and quiet source of optimistic inversions. The
assumption, not the arithmetic, is what failed.

## 7. Failure mode 3: there is no corner to find

The corner rule needs a knee. The demonstration raises the noise level and
measures both the maximum curvature and the corner's error:

| noise (% of peak) | max curvature | median corner $\alpha$ | IQR $\log_{10}\alpha$ | corner error/oracle | corner res$^2/(n\sigma^2)$ |
|---|---|---|---|---|---|
| 0.5 | 47.6 | $7.440\times10^{-5}$ | 0.42 | 7.35 | 0.621 |
| 5.0 | 52.2 | $8.127\times10^{-3}$ | 0.07 | 1.75 | 0.788 |
| 20.0 | 8.13 | $2.762\times10^{-2}$ | 0.22 | 1.49 | 0.831 |

Two findings that a textbook presentation would hide:

1. **The curvature is not monotone in noise.** It rises from 47.6 to 52.2 before
   falling to 8.13. Only at $20\%$ noise does the curve visibly lose its knee.
   "The corner becomes ill-defined" is a measurement, and at moderate noise it
   can be false.
2. **The error ratio improves as the noise grows** (7.35 to 1.49) while the
   absolute error rises. The ratio improves because the *oracle's own* error
   grows with the noise, not because the corner improves. Quoting the ratio
   without the absolute numbers would invert the conclusion.

What does hold in every case is the residual diagnostic: the corner sits at
$0.62$–$0.83$ times $n\sigma_e^2$, i.e. below the noise level, so the corner
solution is fitting noise at every noise level tested.

## 8. A fully worked numeric example

**Problem.** For one realisation, decide between the GCV $\alpha$ and the
discrepancy $\alpha$ using only data and a noise estimate.

**Step 1 — recover the residual from the GCV value.** At GCV's choice,
$\alpha = 7.848\times10^{-4}$, the demonstration's table gives
$G = 1.1716\times10^{-6}$. Since $G = (\|Km_\alpha-d\|^2/n)/(1-\sum f_i/n)^2$
and $\sum_i f_i$ is fixed by $\alpha$ alone, the residual follows:

$$\sum_i f_i = 16.547, \qquad
\|Km_\alpha-d\|^2 = nG\Big(1-\tfrac{16.547}{64}\Big)^{2}
= 64\times1.1716\times10^{-6}\times0.54975 = 4.123\times10^{-5},$$

which is $0.623\,n\sigma_e^2$ with $n\sigma_e^2 = 6.6178\times10^{-5}$.

**Step 2 — test the residual.** $0.623\,n\sigma_e^2$ is well below the expected
residual $\|e\|^2 = 6.6178\times10^{-5}$, so the GCV solution is fitting
roughly $38\%$ of the noise, in variance terms. The discrepancy principle says
the admissible amount of smoothing has not been reached.

**Step 3 — move $\alpha$ up.** At $\alpha = 3.778\times10^{-3}$ the residual
crosses the target: the demonstration prints a ratio of $1.0027$, and
$\sum_i f_i$ falls from $16.547$ to $13.051$. The model error falls from
$0.05596$ to $0.03198$, a factor of $1.75$ — consistent with the Monte Carlo,
where the discrepancy rule beat GCV for the median realisation and lost for
others.

**Step 4 — report.** A defensible sentence is: "Tikhonov with $L=I$; $\alpha$
chosen by the discrepancy principle using the instrument noise of
$1.106\ \mathrm{mGal}$ rms ($0.5\%$ of the peak anomaly); the achieved residual
is $1.00\,n\sigma_e^2$; the solution has about 13 effective parameters." Every
number in that sentence is checkable by a reader, and none of them is the answer.

## 9. Assumptions and regime of validity

1. **The forward operator is exact.** All three rules treat $K$ as known. Model
   error in $K$ biases the residual and therefore every rule, usually towards
   under-smoothing because it inflates the residual.
2. **The noise is white and additive** for GCV and for the $\chi^2_n$ form of the
   discrepancy test. Section 6 measures the cost of violating this.
3. **$\sigma_e$ is known** for the discrepancy principle; Sections 5 shows the
   cost of violating this, and the cost is asymmetric.
4. **The trade-off curve is smooth enough for a numerical second derivative.**
   With very few $\alpha$ values the L-curve curvature is not estimable.
5. **The minimum is not flat enough to make the choice meaningless.** For GCV,
   32 of 400 grid points are within $5\%$ of the minimum, spanning
   $1.62\times10^{-4}$ to $1.66\times10^{-3}$: GCV identifies a *region* of
   parameters, and quoting four significant figures would misrepresent it.
6. **One rule per report.** Averaging two rules' $\alpha$ values produces a
   number that satisfies neither criterion and cannot be checked.

## 10. The honest summary

- There is no rule that is right in general. Each encodes an assumption, and
  the measurement of what happens when the assumption fails is the useful
  content.
- On this synthetic problem the discrepancy principle came nearest the oracle
  (median error 1.25 times the oracle) and the L-curve corner farthest
  (7.6 times), but the discrepancy principle is the rule that needs the most
  input and fails catastrophically when that input is wrong.
- Reproducibility (an IQR of 0.15–0.39 decades) is not accuracy (biases of
  1.25–7.6 in error). Report both.
- The residual ratio to $n\sigma_e^2$ is the cheapest available audit of any
  chosen parameter, and it works without the truth.
- The final sentence of any inversion report should name the rule and the
  statistic it produced, not the parameter alone.

## 11. Python demonstration

`code/parameter_choice_demo.py` prints: the L-curve with its measured curvature,
the spline-smoothing sensitivity table and the residual diagnostic; the GCV
function with its minimum and the width of the flat region; the discrepancy
$\alpha$ with the residual it achieves; a head-to-head table against the oracle;
a 300-realisation Monte Carlo giving the IQR of $\alpha$ and the error
distribution for each rule; and the three failure modes (wrong $\sigma_e$,
correlated noise, no corner).

```bash
cd 18-inverse-problems/03-regularization/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python parameter_choice_demo.py
```

Print-only, seeded with `np.random.default_rng(20261014)`, about one second.

## 12. Exercises

Full sets with worked solutions are in
[`exercises/03-parameter-choice-exercises.md`](exercises/03-parameter-choice-exercises.md)
and
[`exercises/03-parameter-choice-solutions.md`](exercises/03-parameter-choice-solutions.md).

- **★** Given $\|Km_\alpha-d\|^2 = 0.4\,n\sigma_e^2$ at the selected $\alpha$,
  state whether the parameter is too small or too large and why.
- **★★** Reproduce the GCV value in Step 1 of Section 8 from the definition,
  showing every factor.
- **★★★** Design and specify a Monte Carlo experiment that would decide whether
  the L-curve's bias or its variance dominates on a *different* spectrum
  ($q \approx 1.6$ rather than $3.2$), and predict the outcome with an argument
  based on the shape of the trade-off curve.

## 13. Mastery checkpoint

Complete this without notes:

> Three rules are applied to the same noisy data set and return
> $\alpha_{\text{LC}} = 2.7\times10^{-5}$,
> $\alpha_{\text{GCV}} = 7.8\times10^{-4}$ and
> $\alpha_{\text{DP}} = 3.8\times10^{-3}$, with $n\sigma_e^2 = 6.62\times10^{-5}$.
> **(a)** Which rule assumed the most prior knowledge, and which assumed the
> least? **(b)** The residual at $\alpha_{\text{LC}}$ is $0.51\,n\sigma_e^2$.
> What does that say about the corner? **(c)** With $\sigma_e$ underestimated by
> a factor of four, which rule fails and in which direction? **(d)** Write two
> sentences a reader could use to reproduce the parameter choice you would
> recommend, naming the statistic you would report with it.

A worked version of (a)–(c) appears in
[`exercises/03-parameter-choice-solutions.md`](exercises/03-parameter-choice-solutions.md).

## 14. Common pitfalls

1. **Reporting "the L-curve corner" as if it were unique.** It is not: the
   smoothing of the curve moves it by a factor of 6.8 in the measurement above.
2. **Believing a low residual means a good model.** The corner's residual is
   *below* the noise level, which means part of the answer is noise.
3. **Estimating $\sigma_e$ optimistically.** Underestimating it is the dangerous
   direction: four orders of magnitude of error in the demonstration.
4. **Assuming correlated noise matters little.** It does matter, quietly:
   factors of 1.2–1.3 in error, and always in the under-smoothing direction.
5. **Quoting the ratio to the oracle as the error.** The oracle's own error grows
   with the noise level, so the ratio can improve while the absolute error
   worsens — Section 7 measures exactly that.
6. **Treating the GCV minimum as a point.** It is a flat region 32 grid points
   wide; two significant figures is the honest precision.

## 15. Where this is used

- **Potential-field and EM inversions** routinely offer all three criteria in
  software; users must know which one the default implements, because the
  defaults differ between packages.
- **Seismic tomography** usually fixes $\alpha$ by trial and residual plots; the
  residual ratio is the discrepancy principle applied informally and without
  acknowledgement.
- **Machine learning** uses cross-validation as the default, which is GCV's
  empirical cousin; the assumption of exchangeable white noise is inherited
  unchanged; see
  [21-04-02 Bias-Variance Trade-Off, Underfitting and Overfitting](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/02-bias-variance.md).
- **Reproducibility.** A parameter choice that is not named cannot be reproduced;
  see [05-06-06 Documenting Processing: Reproducibility in Practice](../../05-core-geophysics/06-data-processing-principles/06-processing-transparency.md).

## 16. Related modules

- [18-03-04 L1 Regularisation, Sparsity and Compressive Sensing](04-sparsity.md) —
  a different penalty, whose parameter has a different and more interpretable
  meaning.
- [18-03-07 Regularisation of Nonlinear Problems](07-nonlinear-regularization.md) —
  where the parameter choice interacts with the starting model.
- [18-06-02 Monte Carlo Propagation and Its Convergence](../06-uncertainty-quantification/02-monte-carlo-uq.md) —
  the machinery used to measure the reproducibility of a rule.
- [18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](../08-practical-inversion-workflow/02-synthetic-testing.md) —
  how to benchmark a rule on a problem where the truth is known.
- [01-14-04 Linear and Nonlinear Least Squares](../../01-mathematics/14-optimization/04-least-squares.md) —
  the numerical core that every rule calls.

## 17. Self-assessment checklist

- [ ] I can write the GCV function and say where each factor comes from.
- [ ] I can write the curvature formula for the L-curve and explain why the
      smoothing is a hidden parameter.
- [ ] I can state the assumption behind each rule and the failure it causes.
- [ ] I can interpret a residual ratio to $n\sigma_e^2$ without the truth.
- [ ] I can distinguish bias from variance in a table of chosen parameters.
- [ ] I can write a reproducible sentence describing a parameter choice.
