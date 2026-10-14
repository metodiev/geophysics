---
id: 18-06-05
title: "Visualising and Communicating Uncertainty"
level: doctoral
prereqs: ["18-05-06", "18-06-02"]
tags: [inverse-problems, uncertainty-quantification, visualisation, credible-intervals, communication]
---

# Visualising and Communicating Uncertainty

All models in this module are **SYNTHETIC**. The velocity ensemble below is drawn
from a chosen covariance, not from an inversion of real data, and no measured value
appears anywhere. Every number quoted is printed by
[`code/uncertainty_visualisation_demo.py`](./code/uncertainty_visualisation_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** pointwise from simultaneous coverage, and **measure** the
   difference on an ensemble of curves.
2. **Compute** the widening factor required to convert a pointwise band into a
   simultaneous one, and state the assumptions it rests on.
3. **Choose** between an equal-tailed and a highest-posterior-density interval for a
   figure, and **justify** the choice from the shape of the posterior.
4. **Demonstrate** that overlapping credible bands are not evidence that two models
   agree, by measuring both the overlap and a Bayes factor on the same data.
5. **Identify** the encoding choices that make an uncertainty figure misleading
   without being wrong.
6. **Write** a figure caption that makes the uncertainty statement auditable.
7. **State** what a figure cannot convey, and what must be reported numerically
   instead.

## Prerequisites

- [18-05-06 Posterior Summaries: Marginals, Credible Intervals, Correlations](../05-bayesian-inversion/06-posterior-summary.md)
  — the intervals being displayed.
- [18-06-02 Monte Carlo Propagation and Its Convergence](02-monte-carlo-uq.md) —
  where the ensemble comes from and how much information it contains.
- [03-05 Plotting, Visualisation and Scientific Figures](../../03-scientific-computing/05-plotting-and-visualisation/README.md)
  — the mechanics of producing the figure.

## 1. Intuition: a figure is a quantitative claim

A plot of a model with an uncertainty band asserts, implicitly, that the true
quantity lies inside the band with some probability, over some range, under some
model. Every one of those qualifiers is a claim, and most published uncertainty
figures leave all of them unstated. This lesson is about making the claims
explicit — and, where necessary, about measuring them so that the caption can say
something true.

Three failures recur, and each is measured below:

- a band computed pointwise and read as a band for the whole curve;
- a symmetric band drawn for a skewed posterior, so that the interval has the wrong
  shape and can extend into physically impossible values;
- an overlap of two bands read as evidence that the two models are
  indistinguishable.

## 2. The SYNTHETIC ensemble

The demonstration builds $5000$ velocity profiles on a grid of $120$ depths from
$0.5$ to $40$ km, with mean

$$
v(z) = 5.8 + 0.02\,z \quad (\mathrm{km\,s^{-1}})
$$

and a stationary squared-exponential covariance with standard deviation
$0.35\ \mathrm{km\,s^{-1}}$ and correlation length $8$ km. At $z = 20.1$ km the
ensemble has mean $6.197\ \mathrm{km\,s^{-1}}$ and standard deviation
$0.352\ \mathrm{km\,s^{-1}}$; the $68\%$ band is
$[5.847,\,6.543]\ \mathrm{km\,s^{-1}}$ (width $0.696$) and the $95\%$ band is
$[5.504,\,6.886]\ \mathrm{km\,s^{-1}}$ (width $1.382$).

A stationary covariance is used deliberately: it makes the pointwise width constant
with depth, which isolates the effect being studied. In a real inversion the width
would grow with depth wherever the data are silent, and the growth is itself part of
the message — see
[18-06-01 Taxonomy of Uncertainty](01-uncertainty-taxonomy.md), where the epistemic
term grows as $x^{*2}$ outside the aperture.

## 3. Pointwise coverage is not simultaneous coverage

Measure coverage against $20\,000$ *new* members drawn from the same distribution:

| band | pointwise coverage | coverage for the whole curve |
|---|---|---|
| $68\%$ | $67.74\%$ | $13.11\%$ |
| $95\%$ | $95.23\%$ (worst depth $94.77\%$) | $74.25\%$ |

The pointwise numbers are what the bands claim, and they are correct. The second
column is what a reader often assumes. A figure with a $95\%$ band and $120$ depths
has a $26\%$ chance that the true curve leaves the band somewhere — and that is for
a well-behaved stationary Gaussian process. For a curve with strong correlation
along the depth axis the discrepancy is of the same order; for a curve with
independent errors at each depth it is *much* worse, because the deviations add.

To make a simultaneous band, widen the pointwise one. The demonstration computes the
$95\%$ quantile of the maximum standardised deviation across all depths and finds

$$
k_{\text{simultaneous}} = 2.651 \quad\text{against}\quad
k_{\text{pointwise}} = 1.959963984540054,
$$

a factor $1.35$ wider. At $z = 20$ km that is a band of width
$1.866\ \mathrm{km\,s^{-1}}$ instead of $1.379\ \mathrm{km\,s^{-1}}$. The
construction assumes a Gaussian ensemble with a roughly constant standard deviation
along the curve; for a skewed or strongly heteroscedastic ensemble the maximum
deviation is not a simple multiple of the pointwise one, and the correct route is a
bootstrap over curves.

**Rule.** Say which band it is. "Pointwise $95\%$" and "simultaneous $95\%$" are
different figures with different widths, and both are legitimate.

## 4. The shape problem: skewed posteriors and symmetric bars

The demonstration forms the two-way travel time through a $2$ km layer,
$t = 2h/v$, from the ensemble's layer-averaged velocity:

| quantity | value |
|---|---|
| mean | $0.64788$ s |
| median | $0.64512$ s |
| mean $-$ median | $+0.00277$ s |
| $95\%$ equal-tailed interval | $[0.58141,\,0.72699]$ s, width $0.14558$ s |
| $95\%$ HPD interval | $[0.57853,\,0.72002]$ s, width $0.14148$ s |
| ratio of widths | $1.0289$ |

The skew here is mild, so the two intervals nearly coincide: a measurement, not a
licence to use either silently. Make the uncertainty larger and the difference grows.
With a SYNTHETIC lognormal velocity whose log-standard deviation is $0.6$ — a
coefficient of variation of $0.66$ — the travel time has

$$
\text{mean} = 0.9246\ \mathrm{s}, \quad \text{median} = 0.7724\ \mathrm{s}, \quad
\text{skewness} = 2.25, \quad \text{s.d.} = 0.6082\ \mathrm{s},
$$

$$
\text{equal-tailed} = [0.2385,\,2.5046]\ \mathrm{s}, \qquad
\text{HPD} = [0.1381,\,2.0971]\ \mathrm{s},
$$

and the HPD interval is $1.157$ times narrower. More importantly,

$$
\text{mean} - 2\,\text{s.d.} = 0.9246 - 1.2164 = -0.2918\ \mathrm{s},
$$

which is a **negative travel time**. A symmetric mean $\pm 2\sigma$ bar drawn on
this posterior reports an impossible value, and no amount of care in the caption
repairs a figure whose lower edge is below zero. Whenever the posterior is skewed,
a symmetric bar is not merely conservative or aggressive: it is the **wrong shape**.

### 4.1 What to draw instead

- **Quantile bands** (equal-tailed) drawn from the ensemble, with the intervals
  stated in the caption.
- **HPD intervals** when the shortest interval is what the reader needs, declared as
  such.
- **The full ensemble** when the shape is the message — but see Section 5 on
  overplotting: a hundred curves communicate the shape and the spread, a thousand
  communicate only a blur.
- **Two summaries plus the shape**: a median line, a quantile band, and a small
  inset or a second panel with the marginal distribution at a depth of interest.
  This is the combination that survives a reader who looks for one second.

## 5. Overlap is not evidence

Two SYNTHETIC models are compared: a constant-velocity model with one uncertain
speed and a gradient model. Their $95\%$ bands overlap at $100.0\%$ of depths. A
SYNTHETIC data set of $12$ picks with $\sigma = 0.15\ \mathrm{km\,s^{-1}}$ gives a
$\log_{10}$ Bayes factor of $3.86$ in favour of the gradient model — a factor of
about $7200$ in evidence — while the bands still overlap everywhere.

The point is structural, not numerical. Overlap is a statement about *marginal
widths at each depth*; the evidence is a statement about the *likelihood of the
whole data set* under each model. A model can be wrong by a small, consistent
amount at every depth, which accumulates in the likelihood and never shows in a
marginal band. Conversely, a wide band around a wrong model's prediction overlaps a
narrow band around the truth, which is why a figure cannot demonstrate agreement.

Report evidence numerically (a Bayes factor, a likelihood ratio, a difference of
information criteria) and use the figure to show *where* the models differ. The
comparison machinery is in
[18-05-07 Bayesian Evidence and Model Selection](../05-bayesian-inversion/07-evidence-and-model-selection.md).

## 6. Encoding choices that mislead without being wrong

| choice | what it can convey | how it misleads |
|---|---|---|
| one line, no band | a point estimate | implies the estimate is the answer |
| symmetric $\pm 1\sigma$ band | a Gaussian-ish posterior | wrong shape for a skew |
| pointwise band, unlabelled | per-depth coverage | read as a simultaneous band |
| 1000-curve spaghetti | the ensemble exists | the density is unreadable |
| a filled band with no ensemble size | a range | hides how few samples it came from |
| a colour map with a rainbow palette | magnitude ordering | introduces spurious structure |
| truncated axes | detail | hides values that matter for a decision |
| a log axis without a stated base | wide ranges | arithmetic errors in reading it |

Three of these deserve emphasis because they are so common. **Spaghetti plots**
answer "is there an ensemble?" but not "what is the distribution?" — showing the
$5\%$, $25\%$, $50\%$, $75\%$ and $95\%$ quantiles is readable and quantitative.
**Truncated axes** are legitimate and must be declared, because a reader may need to
know whether the uncertainty range crosses a decision threshold that lies outside
the plotted window. **Rainbow palettes** are perceptually non-uniform, and in a
sequential quantity they create apparent edges where the data are smooth.

## 7. A caption that can be audited

Every uncertainty figure needs, in the caption or the text it sits in:

1. **What the band is**: pointwise or simultaneous; equal-tailed or HPD; which
   probability.
2. **What the ensemble is**: posterior samples, prior samples, or propagated
   predictive draws.
3. **How many draws**, and the effective sample size if the draws are correlated.
4. **What the model is**: the prior and the likelihood, at least by reference.
5. **What is not included**: model discrepancy, unmodelled correlation, the
   surrogate's own error.
6. **Units and the meaning of the axes**, including any axis transform.

The demonstration's final section prints this checklist, and it is worth treating as
a template rather than a suggestion: a reader who cannot answer "pointwise or
simultaneous?" from the caption has been given a picture, not a result.

## 8. Assumptions and regime of validity

1. **The ensemble must be a sample from the distribution it is claimed to
   represent.** A prior ensemble plotted as if it were posterior is a different
   claim, and it is usually much wider.
2. **Coverage claims need a generating process.** The measured coverages here are
   against new draws from the same synthetic distribution. For real data only a
   synthetic recovery test can check coverage, and that test is itself conditional
   on the model.
3. **The simultaneous-band factor depends on the correlation structure.** The
   measured factor of $1.35$ is for this stationary process; independent errors
   along the axis give a much larger factor.
4. **Marginal bands do not show correlation between depths.** A ridge in the
   posterior appears as nothing when only marginals are drawn.
5. **A figure cannot carry a model comparison.** Use a number.
6. **Accessibility matters.** Colour-blind-safe palettes, sufficient contrast, and
   a text or tabular summary of the key numbers make the result usable by readers
   who cannot see the plot at all.
7. **The caption is part of the result.** An unauditable caption transfers the
   burden of correctness to the reader.

## 9. Demonstration and exercises

[`code/uncertainty_visualisation_demo.py`](./code/uncertainty_visualisation_demo.py)
builds the ensemble, measures pointwise and simultaneous coverage, computes the
widening factor, compares equal-tailed with HPD intervals for a mild and a strong
skew, and measures the overlap-versus-evidence contrast. It prints every table above
and exits $0$ in a fraction of a second; it produces no plots by design, so the
numbers in a figure caption can be checked against the terminal output. Exercises
and solutions:
[`exercises/05-uncertainty-visualisation-exercises.md`](./exercises/05-uncertainty-visualisation-exercises.md),
[`exercises/05-uncertainty-visualisation-solutions.md`](./exercises/05-uncertainty-visualisation-solutions.md).

## Mastery checkpoint

**(a)** State the difference between pointwise and simultaneous coverage in one
sentence each, and give the two measured numbers from Section 3.
**(b)** A $95\%$ pointwise band has half-width $1.96\sigma$. Compute the
half-width of the simultaneous band from the measured factor and express the
increase in per cent.
**(c)** Explain why a mean $\pm 2\sigma$ bar on the skewed travel-time posterior
reaches a negative value, and compute the value.
**(d)** Two models' credible bands overlap at every depth. State what may and may
not be concluded, and name the quantity that must be reported instead.

## Common pitfalls

1. **Drawing a pointwise band and describing it as "the $95\%$ credible range".**
   Measured: the whole curve was inside it only $74.25\%$ of the time.
2. **Using a symmetric bar for a skewed posterior.** The measured lower edge was
   $-0.2918$ s, an impossible travel time.
3. **Reading overlap as agreement.** Measured: $100\%$ overlap with a $\log_{10}$
   Bayes factor of $3.86$ against one of the two models.
4. **Plotting a thousand curves and calling it the distribution.** Quantile bands are
   readable; a blur is not.
5. **Omitting the ensemble size and effective sample size.** A $5000$-draw ensemble
   with no diagnostic is indistinguishable from a $5$-draw one in a figure.
6. **Truncating an axis without saying so**, when the truncation hides a threshold
   crossing.
7. **Letting the caption say less than the data supports.** The numbers are
   available; the caption is where they belong.

## Further reading

- **Spiegelhalter, D., Pearson, M., & Short, I. (2011). Visualizing uncertainty
  about the future. *Science*, 333(6048), 1393–1400.** Level: research. The
  grammar of uncertainty graphics, and the failure modes of common encodings.
- **Wilke, C. O. (2019). *Fundamentals of Data Visualization*. O'Reilly.** Level:
  advanced. Perceptual and design reasoning behind the encoding table in Section 6.
- **Gelman, A., Carlin, J. B., Stern, H. S., Dunson, D. B., Vehtari, A., &
  Rubin, D. B. (2013). *Bayesian Data Analysis* (3rd ed.). CRC Press.** Level:
  research. Credible and predictive intervals, which are the objects a figure shows.
- **BIPM, IEC, ISO, IUPAC, IUPAP, & OIML (2008). *Evaluation of Measurement
  Data — Guide to the Expression of Uncertainty in Measurement* (JCGM 100:2008).**
  Level: reference. The standard language for stating an uncertainty, usable in a
  caption.

## Related modules

- [01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](01-uncertainty-taxonomy.md)
  — which component the band is showing.
- [02 Monte Carlo Propagation and Its Convergence](02-monte-carlo-uq.md) — the
  ensemble and its information content.
- [04 Surrogate Models and Polynomial Chaos for UQ](04-surrogate-uq.md) — a source of
  ensemble members whose own error must be shown.
- [06 Decision-Making Under Uncertainty and Value of Information](06-decision-under-uncertainty.md)
  — the decisions a figure must not silently make.
- [18-05-06 Posterior Summaries](../05-bayesian-inversion/06-posterior-summary.md).
- [18-08-04 Reporting Inversion Results Responsibly](../08-practical-inversion-workflow/04-reporting-inversion.md).
