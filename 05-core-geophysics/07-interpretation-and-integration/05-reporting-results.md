---
id: 05-07-05
title: "Reporting Geophysical Results with Honest Uncertainty"
level: advanced
prereqs: ["05-07-02", "18-06-01", "18-06-05"]
tags: [reporting, uncertainty, uncertainty-budget, detectability, reproducibility, communication]
---

# Reporting Geophysical Results with Honest Uncertainty

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** an uncertainty statement that separates measurement uncertainty,
   model-choice uncertainty and structural (assumption) uncertainty, and name
   each.
2. **Compute** an uncertainty budget for a depth estimate and identify which term
   dominates.
3. **Decide** whether better instruments, more stations or an independent
   constraint is worth buying for a stated target, and justify the answer with a
   number.
4. **Report** a detection, a non-detection and a conflict as three distinct
   outcomes, each with a stated threshold and a stated test.
5. **Specify** the processing metadata a reader needs to reproduce an
   interpretation.
6. **Recognise** and remove the four phrases that make a report unfalsifiable.

## Prerequisites

- [05-07-02 Quantitative Interpretation and Depth Estimation](./02-quantitative-interpretation.md)
  — the statistical error and the model spread whose separation this lesson
  formalises.
- [18-06-01 Taxonomy of Uncertainty: Aleatory, Epistemic, Structural](../../18-inverse-problems/06-uncertainty-quantification/01-uncertainty-taxonomy.md)
  — the general vocabulary.
- [18-06-05 Visualising and Communicating Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/05-uncertainty-visualisation.md)
  — how to display a feasible set instead of a best-fit map.

## 1. Intuition: an unquantified number is a claim to know something you do not

A report is a promise that someone else can act on. If an interpretation carries
no uncertainty, the reader has no basis for deciding whether to drill, to
excavate, to buy more data, or to walk away, and the decision falls back on
whether they trust the author. That is a failure of the document, independent of
the quality of the geophysics.

The discipline this lesson enforces has three parts:

- **Separate the terms.** A number like "depth = 500 ± 10 m" is not honest, it
  is *incomplete*: the 10 m is the statistical error under an assumed model, and
  the model choice is worth another 117 m (Section 4). Both numbers are needed,
  and they are different kinds of thing.
- **Name the assumptions.** Every interpretation rests on assumptions that, if
  false, invalidate it. A report that does not list them cannot be criticised and
  therefore cannot be trusted.
- **State the acceptance and rejection conditions before presenting the result.**
  A detection threshold chosen after seeing the anomaly is not a threshold.

Underlying all three is a discipline of *what a measurement can support*. This is
harder than it sounds, because the pressures on a report — commercial, academic,
and human — all push towards a single confident number.

## 2. Precise definitions

### 2.1 The three uncertainty types, applied

- **Measurement (aleatory) uncertainty.** The noise of the observation. Reducible
  by averaging, up to the point where correlated error dominates. For the running
  example, a half-width measured to 2 per cent.
- **Model-choice (epistemic) uncertainty.** The spread over the family of models
  that fit. For the running example, the choice between compact, cylindrical and
  sheet geometries.
- **Structural uncertainty.** The possibility that the model family itself is
  wrong: 1-D geology where the Earth is 3-D, a sharp boundary where it is
  gradational, an isolated source where there are three. This is not quantified
  by any covariance and is the term most often omitted.

### 2.2 Uncertainty budget

An **uncertainty budget** is a table of the contributions to the total
uncertainty, each in the same units, with the dominant term identified. It is the
counterpart of a physical error budget and it is the reason a report can say
*where the money should go next*.

### 2.3 Detectability statement

A **detectability statement** has four parts: the target (size and property
contrast), the depth, the noise level, and the acceptance threshold. Without all
four it is not a statement. "We can see to 500 m" is not one.

### 2.4 Falsifiability

A claim is **falsifiable** if it specifies an observation that would contradict
it. "The anomaly may indicate a mineralised zone" is not falsifiable. "A body of
at least 400 kg m⁻³ contrast lies between 250 and 400 m at this location" is.

## 3. Derivations

### 3.1 Propagating the half-width measurement to a depth

With $z = c\,w$ and $c$ a shape constant,

$$\frac{\sigma_z}{z} = \sqrt{\left(\frac{\sigma_c}{c}\right)^2 +
\left(\frac{\sigma_w}{w}\right)^2 }. \tag{1}$$

If $c$ were known, the second term would be the whole story. The demonstration
measures $\sigma_w/w = 2$ per cent, giving a measurement-only depth uncertainty of
$1.30477 \times 7.66 = 10.0$ m. The model term is not a standard deviation in the
same sense — $c$ takes one of two discrete values in the example — and it
contributes a spread of $|1.30477 - 1.00000| \times 383.23 = 116.8$ m. The ratio
is **11.7**, so the total is 117 m and the instrument contributes 8.5 per cent of
it.

A discrete model uncertainty can be represented as a mixture distribution. The
demonstration draws the shape at random with equal prior weight and obtains the
depth percentiles

$$q_{5}, q_{16}, q_{50}, q_{84}, q_{95} = 373.4,\ 379.7,\ 469.6,\ 504.7,\ 512.8\
\mathrm{m},$$

which is not a Gaussian and whose 5–95 range (373–513 m) is exactly the 30 per cent
model spread. **Reporting the mean of a bimodal distribution would be worse than
reporting the two modes.**

### 3.2 The uncertainty floor set by physics

Equation (1) tells you whether better instruments help. To get a depth bound
tighter than the model spread $\Delta z_{\text{model}} = 116.8$ m, the measurement
term must satisfy

$$1.30477\,\sigma_w < \Delta z_{\text{model}}
\;\Longrightarrow\; \sigma_w < \frac{116.8}{1.30477} = 89.5\ \mathrm{m}, \tag{2}$$

i.e. the half-width must be read to better than 23 per cent. The actual reading
precision is 2 per cent. **Therefore no improvement in the gravity data can
reduce the depth uncertainty**, and the money should go to an independent
constraint on the *shape*: a second method with transverse sensitivity, or a
borehole.

This calculation is what turns "we should get better data" into a decision, and
it takes two lines.

### 3.3 Detectability, stated properly

For a compact body of mass $M$ at depth $z$ and station noise $\sigma$, detection
at $k$ standard deviations requires

$$k\sigma \le \frac{GM}{z^2}
\;\Longrightarrow\;
z_{\max} = \sqrt{\frac{GM}{k\sigma}}, \qquad
M_{\min} = \frac{k\sigma z^2}{G}. \tag{3}$$

With $k=3$, $M = 5.79\times10^{9}$ kg, $\sigma = 0.02$ mGal: the peak anomaly is
0.429 mGal, 21.5 times the noise, and $z_{\max} = 802.5$ m. Halving the noise
pushes it to 1134.9 m — a factor of only $\sqrt{2}$, which is the whole content of
"depth of investigation goes as the square root of the noise". Doubling the mass
does the same.

### 3.4 Reporting a non-detection

A non-detection is a result, and it is reportable:

> "No anomaly exceeding 3σ = 0.06 mGal was found over the target window. At this
> noise level and a 3σ threshold, a compact body of 400 kg m⁻³ contrast at 300 m
> would produce 0.43 mGal and would have been detected; the same body at 800 m
> would produce 0.06 mGal and is at the detection limit. We therefore exclude
> bodies larger than about 10⁹ kg shallower than 800 m; we make no statement about
> smaller or deeper targets."

Every clause is a bound, every bound has a stated threshold, and the last clause
states the null space. This form is also the strongest possible defence of a
survey that found nothing.

## 4. Worked examples

### 4.1 A complete uncertainty budget

Running example: an isolated anomaly, half-width 383.23 ± 7.66 m (2 per cent),
amplitude 0.267 mGal, 289 stations, 0.02 mGal noise.

| Term | Type | Value | Share of variance |
|---|---|---|---|
| Half-width reading | measurement | 10.0 m | 0.7 % |
| Regional-removal order | structural | 0–40 m | up to 10 % |
| Shape family (sphere vs cylinder) | model choice | 116.8 m | ~85 % |
| Density contrast (for the mass estimate) | measurement | — | affects mass, not depth |
| 3-D geometry (two-body vs one-body) | structural | unbounded | not quantified |

The budget says: the answer is a *model statement*, the total depth uncertainty is
about 120 m, and the only way to reduce it is to attack the model term.

### 4.2 Reporting a conflict

From [05-07-03 §3.5](./03-multi-method-integration.md): a seismic pick of 150 m
would require the MT data to accept a misfit 6.6 times their tolerance. The report
writes:

> "The MT and seismic interpretations are inconsistent at the stated
> uncertainties. The MT data admit layer thicknesses of 278–327 m at the 1 per
> cent misfit level; the seismic pick of 150 m lies outside that set and would
> require a 6.6-fold increase in the MT misfit. We do not present a compromise
> model. The most likely cause is a mis-picked multiple on the seismic section,
> which should be checked before the interpretation is used."

Note what this does *not* do: it does not average 150 and 300 to get "about
200 m". A compromise is a statement about the analyst's discomfort, not about the
Earth.

### 4.3 Four phrases to delete

| Phrase | Why it fails | Replacement |
|---|---|---|
| "The data indicate a possible target" | No target, no threshold, unfalsifiable | "An anomaly of 0.27 mGal exceeds three times the 0.02 mGal noise" |
| "Depth to the top is about 500 m" | Which model? What uncertainty? | "Depth 383–500 m, the two ends corresponding to a cylinder and a compact body" |
| "The anomaly is caused by massive sulphide" | Identification presented as detection | "Consistent with a body of ≥400 kg m⁻³ contrast; requires drilling to identify" |
| "After standard processing" | Not reproducible | "Reduction: Bouguer, density 2670 kg m⁻³, terrain correction to 167 km, regional removed as a 2nd-order polynomial shown in Figure 3" |

The last row is the one that most often decides whether a result can be checked.
Reproducibility is not a formality: an interpretation whose processing cannot be
repeated is not evidence.

## 5. Assumptions

A report's assumptions section is where the honest work goes. At minimum:

1. **Physics.** Which forward operator, and its validated range (do not use a
   half-space skin depth where the layer is thin).
2. **Model family.** What shapes were considered, and which were excluded, and on
   what basis.
3. **Reduction and processing.** Datum, corrections, filters, trend order,
   parameters, software versions.
4. **Noise model.** How the uncertainty was estimated (repeat readings, crossover
   statistics, residual scatter) and whether it is correlated.
5. **Geological priors.** Any regional knowledge used, and its source.
6. **Independence claims.** Why a "second dataset" is independent, or not.
7. **What would falsify the interpretation.** Stated in advance.

## 6. Units and dimensional analysis

- Report every number with its unit, and report the unit of the *uncertainty*: "±10 m",
  not "±10".
- Percentages must name their base: a 20 per cent density uncertainty is 20 per
  cent of what?
- Do not mix mGal and m s⁻², or m and km, in one table. The most common
  report-level error is a units mismatch between a text figure and a table.
- Dimensionless statistics (standardised residuals, misfit ratios) are the most
  robust way to communicate, because they survive unit changes: "6.6 times the
  tolerance" needs no units.
- For a mass, quote kg and state the equivalent volume at the assumed contrast, so
  the reader can see the hidden assumption.

## 7. Python demonstration

`code/reporting_demo.py` builds the Monte Carlo uncertainty, the detectability
thresholds, and the measurement floor. Predict each number before running.

```python
is_point = rng.random(n) < 0.5
depth = np.where(is_point, 1.30477 * x_half, 1.0 * x_half)
print(np.percentile(depth, [5, 16, 50, 84, 95]))
```

Measured output:

```
half-width                        = 383.23 +/- 7.66 m (2.0 per cent)
depth percentiles 5/16/50/84/95   = 373.4 / 379.7 / 469.6 / 504.7 / 512.8 m
depth from the measurement alone  = 10.00 m (1 sigma, shape fixed)
spread from the shape assumption  = 116.80 m
shape spread / measurement spread = 11.7

body mass 5.790e+09 kg at 300 m -> peak anomaly 0.429 mGal
station noise 0.02 mGal -> peak/noise = 21.5
greatest depth for this mass at 3 sigma  =   802.5 m
smallest mass at 300 m for 3 sigma      = 8.091e+08 kg
a factor of 2 less noise pushes the depth limit to  1134.9 m

  half-width read to better than 89.7 m (23 per cent)
  measured half-width is read to 7.66 m (2 per cent), which already meets it
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| The depth distribution is bimodal, not Gaussian | Report the modes and the range; a mean ± σ misrepresents it |
| Measurement contributes 10.0 m, model choice 116.8 m | The budget names where the uncertainty is, and it is not the instrument |
| The required half-width precision is 23 %, already achieved | Better data would buy nothing for the depth; a shape constraint would |
| $z_{\max}$ improves only as $\sqrt{2}$ when noise halves | Depth of investigation is a weak function of instrument quality |
| $M_{\min}$ is $8.1\times10^{8}$ kg at 300 m, 3σ | A detectability statement, in the form of §3.3 |

> **Breaking exercise.** Change the prior weight on the two shapes to
> $(0.9, 0.1)$. Predict how the percentiles move, then run it. Note that the
> *prior* is now a stated assumption and must appear in the report; this is the
> prior-influence problem of
> [18-05-03 Priors: Informative, Reference and Their Influence](../../18-inverse-problems/05-bayesian-inversion/03-priors.md).

## 8. Exercises

[`exercises/05-reporting-results-exercises.md`](./exercises/05-reporting-results-exercises.md)
and
[`exercises/05-reporting-results-solutions.md`](./exercises/05-reporting-results-solutions.md).

### ★ Foundational

**★1.** Write a one-sentence detectability statement for a 300 m deep,
$5\times10^{9}$ kg compact body at 0.02 mGal noise and a 3σ threshold, including
all four required parts.

**★2.** Convert "depth = 500 ± 10 m" into an honest statement given that the
model choice is worth 117 m.

**★3.** List the four metadata items a reader needs to reproduce a Bouguer
anomaly map.

### ★★ Applied

**★★4.** Rerun the uncertainty budget with the half-width measured to 10 per cent
instead of 2 per cent. Does the dominant term change? At what measurement
precision do the two terms become equal?

**★★5.** Write the "non-detection" paragraph of §3.4 for a survey with
0.05 mGal noise, a 4σ threshold, and a target contrast of 200 kg m⁻³ at 500 m.

**★★6.** A report claims "the gravity data confirm the seismic interpretation".
Rewrite it honestly, distinguishing what gravity can and cannot confirm, and
using the language of feasible sets.

### ★★★ Research-oriented

**★★★7.** Build a full uncertainty budget for a depth estimate that includes
regional-removal order, profile length, station noise, and shape family. Compute
each term by direct simulation, report the shares, and state which two terms a
further field campaign could reduce.

**★★★8.** Review a published interpretation of your choice (or the nearest
available paper to your field). Produce a one-page critique structured as: stated
model, stated uncertainties, assumptions, falsifiability, and what an independent
dataset would test. Use the vocabulary of this lesson throughout, and state which
claims you could not assess because the information was not given.

## 9. Common mistakes

1. **Reporting a mean of a bimodal distribution.** §3.1: it describes a model that
   does not exist.
2. **Quoting a covariance as the total uncertainty.** The model term is larger by
   an order of magnitude.
3. **Chosen-after-the-fact thresholds.** Selecting 2.5σ because it makes the
   anomaly significant is not a detection.
4. **Compromise models for conflicting data.** They fit neither dataset and they
   hide the finding.
5. **Omitting the processing parameters.** The interpretation is not reproducible
   and therefore not checkable.
6. **Reporting a non-detection as a failure.** It is a bound, and a bound is a
   result (§3.4).
7. **Failing to state what would falsify the interpretation.** Without it, the
   report is unfalsifiable and so is not a scientific claim.

## 10. Real-world applications

- **Exploration decision documents.** The uncertainty budget is what a drilling
  decision actually consumes; a point estimate forces the decision onto
  personality.
- **Regulatory and environmental reporting.** Contaminated-site and geological
  storage assessments require quantified uncertainty and a stated detection limit;
  a bounded non-detection has legal weight.
- **Geothermal and mining resource statements.** The distinction between a
  measured quantity and a model quantity is a regulatory requirement, not a
  stylistic preference
  ([04-06-03 Geothermal Systems](../../04-earth-science-geology/06-petroleum-and-mineral-systems/03-geothermal-systems.md)).
- **Academic publication.** Reviewers increasingly require uncertainty on
  inverted models; a feasible-set figure is more informative than a best-fit map.
- **Hazard assessment.** A false positive is cheap and a false negative is not, so
  the threshold and its consequences must be stated explicitly.

## 11. Further reading

- **Taylor, J. R. (1997). *An Introduction to Error Analysis* (2nd ed.).
  University Science Books.** Chapters 1–5. Level: beginner to intermediate. The
  uncertainty vocabulary in its clearest form, including why the dominant term is
  the one worth attacking.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Chapters 1–2. Level: graduate. Uncertainty as a state of
  information, and the formal status of a feasible set.
- **Ellison, S. L. R. & Williams, A. (eds.) (2012). *Eurachem/CITAC Guide:
  Quantifying Uncertainty in Analytical Measurement* (3rd ed.).** Level:
  intermediate. The standard structure of an uncertainty budget; transferable
  directly to geophysics.
- **Spiegelhalter, D., Pearson, M. & Short, I. (2011). Visualizing uncertainty
  about the future. *Science*, 333(6048), 1393–1400.** Level: intermediate. Why
  and how to display a range rather than a number.
- **BIPM (2008). *Evaluation of Measurement Data — Guide to the Expression of
  Uncertainty in Measurement (GUM)*.** Level: reference. The normative definition
  of standard uncertainty and of an uncertainty budget.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core](./04-ground-truthing.md)
  — reporting a failed test, and designing the test so it can fail.
- [05-07-06 Common Interpretation Pitfalls and False Positives](./06-interpretation-pitfalls.md)
  — the statistics behind the thresholds this lesson requires you to state.
- [18-06-05 Visualising and Communicating Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/05-uncertainty-visualisation.md)
  — the figures that go with an honest report.
- [18-06-06 Decision-Making Under Uncertainty and Value of Information](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — what the reader does with the uncertainty once you have reported it.
- [05-07-03 Integrating Multiple Methods and Constraints](./03-multi-method-integration.md)
  — the conflict report of §4.2.

## Self-assessment checklist

- [ ] I can name the three uncertainty types and give an example of each in a
      depth estimate. (§2.1)
- [ ] I can build an uncertainty budget and identify the dominant term. (§4.1)
- [ ] I can compute the measurement precision needed to beat the model spread,
      and decide whether to buy instruments or an independent constraint. (§3.2)
- [ ] I can write a four-part detectability statement. (§2.3, §3.3)
- [ ] I can write a non-detection as a bound with a stated null space. (§3.4)
- [ ] I can report a conflict without inventing a compromise. (§4.2)
- [ ] I can list the metadata needed to reproduce an interpretation. (§5)
- [ ] I can run the demonstration and explain why the depth distribution is
      bimodal. (§7)
