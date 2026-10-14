---
id: 14-03-04
title: "Building Geophysical Proxies for Hydrological Properties"
level: research
prereqs: ["14-03-01", "14-03-02", "14-03-03", "18-01-01", "21-03-01"]
tags: [hydrology, hydrogeophysics, petrophysics, proxy, uncertainty, joint-inversion, error-propagation]
---

# Building Geophysical Proxies for Hydrological Properties

> **All models, data, priors and posteriors in this module are SYNTHETIC.** The
> truth values, noise levels, grids and entropies below are computed from chosen
> teaching constructs. No site, log, field campaign or published dataset is used.

The previous three lessons each produced a transform: resistivity to porosity,
resistivity to saturation, velocity to saturation. This lesson is about
*composing* them into a proxy — a function that takes a geophysical measurement
and returns a hydrological property — and about the two things that determine
whether the result is worth reporting: the amplification of error through the
chain, and the reduction of the non-uniqueness volume when a second measurement
is added.

The two are independent, and conflating them is the most common methodological
error in the applied literature. Error amplification is a property of the
transform and is not reduced by more data of the same kind. Non-uniqueness is a
property of the data and is reduced by data of a different kind. A proxy reported
without both an amplification factor and a posterior is a number, not a
measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Formulate** a hydrological proxy as a composition $h = f(g^{-1}(d))$ of a
   geophysical forward operator $g$ and a petrophysical transform $f$, and
   **identify** which part is physics and which is fitted.
2. **Compute** the amplification factor of a chained transform analytically and
   **confirm** it by finite difference, for the concrete chain
   $\rho_t \to \phi \to k$.
3. **Propagate** a measurement uncertainty through a nonlinear transform by Monte
   Carlo, and **distinguish** the spread of the result from the bias of the
   plug-in estimate.
4. **Build** a two-parameter hypothesis grid with two forward operators, and
   **compute** the posterior marginals for each datum alone and combined.
5. **Quantify** the information gain from a second measurement in bits, and
   **state** what the joint posterior still does not determine.
6. **Decide**, from the posterior width, whether a proposed proxy can answer a
   stated hydrological question, and **recommend** the next measurement rather
   than another inversion of the same data.

## Prerequisites

- [14-03-01 Porosity-Permeability and Kozeny-Carman Relations](01-porosity-permeability-relations.md) —
  the $\phi \to k$ transform whose amplification factor is computed here.
- [14-03-02 Archie's Law and Saturation Estimation](02-archie-and-saturation.md) —
  the $\rho_t \to \phi, S_w$ inverse transform.
- [14-03-03 Seismic Velocity vs Saturation and Gassmann](03-seismic-velocity-saturation.md) —
  the second forward operator, and its own non-uniqueness.
- [18-01-01 Forward vs Inverse Problems](../../18-inverse-problems/01-inverse-problem-foundations/01-forward-and-inverse.md) —
  forward operators, the asymmetry of the inverse problem, and why $g^{-1}$ needs
  regularisation.
- [21-03-01 The Bayesian Paradigm](../../21-statistics-bayesian-ml/03-bayesian-inference/01-bayesian-paradigm.md) —
  likelihood, prior, posterior and entropy as used here.

## 1. What a proxy is, and what it is not

A **proxy** is a map from what you measured to what you wanted:

$$
h = f\big(g^{-1}(d)\big),
$$

where $d$ is the data vector, $g$ the geophysical forward operator,
$g^{-1}$ its (usually regularised, usually non-unique) inversion, $f$ the
petrophysical transform, and $h$ the hydrological target. For the running example
of this module, $d = \rho_t$, $g^{-1}$ is Archie inverted for porosity,
$f$ is Kozeny–Carman, and $h = k$.

Three distinctions do the work in this lesson.

- **Physics versus fit.** $g$ (resistivity forward modelling) is physics and can
  be checked by a synthetic test. $g^{-1}$ is an inverse problem with a null
  space. $f$ is a *model*, part derived (the $\phi^{3}$ and $(1-\phi)^{-2}$
  scaling), part fitted ($c_K$, $S_0$). A proxy inherits the weakest link.
- **Amplification versus non-uniqueness.** Amplification multiplies the width of
  an input uncertainty; it does not change which hypotheses are admitted.
  Non-uniqueness is the admitted set itself. Section 3 measures amplification;
  Section 5 measures non-uniqueness.
- **Point estimate versus distribution.** Because $f$ is nonlinear, $f(\bar{m})$
  is not $\overline{f(m)}$. Section 4 measures how much that matters.

## 2. The running example

A synthetic sand with the KC grain size $d = 0.20\ \mathrm{mm}$ and
$\tau = 2.5$, and the Archie parameters of lesson 02:

$$
k(\phi) = \frac{\phi^{3}}{2\tau S_0^{2}(1-\phi)^{2}}, \qquad
\rho_t(\phi, S_w) = \frac{a\,\rho_w}{\phi^{m}S_w^{n}},
$$

with $a = 1$, $m = 2$, $n = 2$, $\rho_w = 2.50\ \Omega\,\mathrm{m}$. The
velocity operator is Gassmann with a synthetic critical-porosity dry frame
$K_\text{dry} = K_\text{min}(1 - \phi/\phi_c)$,
$\mu_\text{dry} = \mu_\text{min}(1-\phi/\phi_c)$, $\phi_c = 0.42$,
$K_\text{min} = 36\ \mathrm{GPa}$, $\mu_\text{min} = 45\ \mathrm{GPa}$,
and a Wood fluid mixture. Every one of these is a *chosen* model; the arithmetic
below is exact for those choices and transfers to real rock only if the same
models do.

The synthetic "truth" used to generate the observations is $\phi = 0.25$,
$S_w = 0.60$, which gives $\rho_t = 111.111\ \Omega\,\mathrm{m}$ and
$V_p = 4.2636\ \mathrm{km\,s^{-1}}$.

## 3. Amplification: the chain $\rho_t \to \phi \to k$

Differentiate the chain logarithmically. From KC,

$$
\frac{\mathrm{d}\ln k}{\mathrm{d}\phi} = \frac{3}{\phi} + \frac{2}{1-\phi}
= 12 + 2.667 = 14.667 \quad \text{at } \phi = 0.25 .
$$

From Archie at fixed $S_w$, $\ln\phi = -\tfrac1m(\ln\rho_t + \text{const})$, so

$$
\frac{\mathrm{d}\ln\phi}{\mathrm{d}\ln\rho_t} = -\frac{1}{m} = -0.500 ,
$$

and therefore

$$
\frac{\mathrm{d}\ln k}{\mathrm{d}\ln\rho_t}
= \underbrace{\frac{\mathrm{d}\ln k}{\mathrm{d}\phi}}_{14.667}
\times \underbrace{\phi}_{0.25}
\times \underbrace{\frac{\mathrm{d}\ln\phi}{\mathrm{d}\ln\rho_t}}_{-0.500}
= -1.8333 .
$$

The demonstration prints $-1.8333$ twice: once from this closed form and once
from a finite difference of the composed function, which agrees to four decimal
places:

| error in $\rho_t$ | error in $k$ |
|---|---|
| 1% | 1.8% |
| 2% | 3.7% |
| 5% | 9.2% |

**Read the factor carefully.** The amplification is modest *in these units*
because a relative resistivity error becomes a relative porosity error divided
by $m$, and the KC factor $14.667$ acts on an *absolute* porosity. Written in
relative porosity units, the factor is
$\phi \times 14.667 = 3.67$: a $1\%$ *relative* porosity error is a $3.67\%$
permeability error. Both statements are the same statement; the lesson is to say
which units you mean. This ambiguity is a common source of published factors that
differ by an order of magnitude.

## 4. Monte Carlo: spread, skew and the plug-in estimate

The demonstration draws $\phi$ from a normal distribution around $0.25$ and pushes
each draw through KC:

| $\sigma_\phi$ | $\sigma_\phi/\phi$ | median $k$ ($\mathrm{m^2}$) | mean $k$ ($\mathrm{m^2}$) | relative sd of $k$ | $k(\bar\phi)$ minus median |
|---|---|---|---|---|---|
| 0.012 | 4.8% | $6.16955\times10^{-12}$ | $6.24534\times10^{-12}$ | 17.5% | +0.05% |
| 0.025 | 10.0% | $6.17951\times10^{-12}$ | $6.50806\times10^{-12}$ | 36.7% | -0.11% |
| 0.050 | 20.0% | $6.15427\times10^{-12}$ | $7.49432\times10^{-12}$ | 72.1% | +0.30% |

Three measured facts:

1. **The spread is amplified by $3.65$** relative to the relative porosity
   spread — exactly the factor predicted in Section 3.
2. **The distribution is skewed.** $k$ is convex in $\phi$, so the mean sits
   $1.2\%$ above the median even at a $4.8\%$ porosity spread.
3. **The plug-in estimate is nearly unbiased at these levels** ($+0.05\%$, and
   the sign is not even stable at $0.3\%$, which is Monte Carlo noise at
   $2\times10^{5}$ draws). The correct conclusion is not "use the median"; it is
   that **the spread, not the bias, is the problem**. A $72\%$ one-sigma spread
   in $k$ cannot be fixed by choosing a better point estimator.

## 5. Non-uniqueness: a two-parameter grid with two operators

Now treat $\phi$ and $S_w$ as unknown and forward model both data sets on a grid
of $111 \times 95 = 10545$ hypotheses, with stated synthetic noise of $2\%$ on
$\rho_t$ and $1\%$ on $V_p$. The observations come from the truth
$\phi = 0.25$, $S_w = 0.60$.

| data used | $\phi$ (mean $\pm$ sd) | $S_w$ (mean $\pm$ sd) |
|---|---|---|
| $\rho_t$ only | $0.2540 \pm 0.0636$ | $0.6294 \pm 0.1578$ |
| $V_p$ only | $0.2518 \pm 0.0077$ | $0.5338 \pm 0.2742$ |
| **joint** | $\mathbf{0.2498 \pm 0.0043}$ | $\mathbf{0.6010 \pm 0.0122}$ |

The two data sets fail in *different directions*, which is the whole reason to
collect both:

- **Resistivity is nearly blind to porosity** ($\mathrm{sd} = 0.064$, five per
  cent of the value) because the 5–95% range of the $\rho_t$-only marginal spans
  $\phi$ from $0.166$ to $0.364$. A change in $\phi$ and a change in $S_w$
  produce the same measured resistivity — this is the trade-off curve of
  lesson 02, seen as a posterior.
- **Velocity is nearly blind to saturation** ($\mathrm{sd} = 0.274$) for exactly
  the reasons measured in lesson 03: $V_p$ depends on the fluid mixing geometry,
  which is a nuisance parameter here.
- **Together** they give $0.0043$ in $\phi$ and $0.012$ in $S_w$, both roughly
  ten times better than either alone.

**But the joint posterior is still a distribution, not a point.** Its width
encodes the residual trade-off that survives: the model still cannot distinguish
a slightly softer frame with slightly more water from a stiffer frame with less,
and that direction is the residual null space of the two-operator system.

## 6. Information gain in bits

Treating the discretised posterior as a probability mass function, the Shannon
entropy gives an absolute currency for "how much did the data tell me":

| posterior | entropy (bits) | gain over the flat prior (bits) |
|---|---|---|
| flat prior over the grid | 13.3643 | — (13.3643 bits for the uniform grid) |
| $\rho_t$ only | 8.0846 | 5.2797 |
| $V_p$ only | 9.6339 | 3.7304 |
| joint | **4.4695** | **8.8948** |

Two honest readings.

- The joint gain ($8.89$ bits) is larger than either single gain, and larger than
  their sum minus the prior ($5.28 + 3.73 = 9.01$ bits, close but not identical,
  because the two likelihoods are nearly independent given the parameters: the
  difference of $0.11$ bits is the small redundancy in the two data sets).
- No amount of bit-counting turns a ridge into a peak. The absolute entropy
  depends on the grid resolution, so **the gains are meaningful and the absolute
  numbers are not**. Report gains, or report posterior standard deviations with
  units; do not report "the entropy of the posterior" as though it were a
  physical quantity.

## 7. Worked example — is the proxy good enough?

**Problem.** A groundwater study needs permeability to within a factor of two, to
choose between two remediation designs. The available measurements and models are:
a resistivity with $2\%$ uncertainty; a cementation exponent known to
$\pm 0.2$ (i.e. $m = 2.0 \pm 0.2$ at one sigma); and a grain diameter known to
$\pm 30\%$ from sieving a few samples. Decide whether the proxy qualifies, and if
not, say what to do.

**Solution.** Work in $\ln k$ and combine the three contributions in quadrature,
each evaluated by finite difference at the reference state $\phi = 0.25$,
$S_w = 0.60$, $d = 0.20\ \mathrm{mm}$.

*Resistivity route.* A $2\%$ error in $\rho_t$ moves the inferred porosity to
$0.24754$ and $k$ to $e^{-0.0363}$ times its reference value, so
$\sigma_1 = 0.0363$ in $\ln k$.

*Exponent route.* With $C \equiv a\rho_w/(\rho_t S_w^{n}) = 0.062500$, the
inferred porosity is $\phi = C^{1/m}$. Changing $m$ from $2.0$ to $2.2$ gives
$\phi = 0.0625^{1/2.2} = 0.28358$, a $13.5\%$ increase in porosity, and

$$
\ln\frac{k(0.28358)}{k(0.250)} = \ln 1.5995 = 0.4697 \;\;\Rightarrow\;\;
\sigma_2 = 0.4697 .
$$

*Grain-size route.* KC gives $k \propto d^{2}$ exactly, so a $30\%$ error in
$d$ contributes $\sigma_3 = 2\times0.30 = 0.6000$.

*Combine.*

$$
\sigma_{\ln k} = \sqrt{0.0363^{2} + 0.4697^{2} + 0.6000^{2}}
= \sqrt{0.00132 + 0.22062 + 0.36000} = 0.7628 .
$$

A factor of two is $\ln 2 = 0.6931$, so the requirement is
$\sigma_{\ln k} \le 0.6931$ and the proxy delivers $0.7628$ — it **fails**, with a
one-sigma range of $\times0.47$ to $\times2.14$.

**The dominant term is the grain size ($0.6000$), then the exponent ($0.4697$);
the resistivity contributes $0.0363$, five per cent of the total.** Buying a
four-times better resistivity changes the total from $0.7628$ to $0.7620$ —
nothing. The action is to constrain $S_0$ (grain-size analysis on more samples,
or an NMR-derived surface-to-volume ratio) and $m$ (core calibration, or a
porosity measurement that does not use $m$ at all), not to acquire more
resistivity.

## 8. Constructing a defensible proxy

A checklist that follows from the measurements above.

1. **Write the chain explicitly**, with each operator and each fitted parameter
   named. If a step cannot be written down, it is not a proxy, it is a guess.
2. **Validate each operator separately** on synthetic data where the answer is
   known: does $g(m_\text{true})$ equal $d_\text{true}$ to machine precision?
3. **Compute the amplification analytically**, then confirm it with a finite
   difference. Publish the factor *with its units convention*.
4. **Report the posterior**, not the maximum. A map of $S_w$ without an error bar
   is a map of the model, not of the aquifer.
5. **Rank the error sources by contribution** to $\sigma_{\ln h}$ and act on the
   largest. Section 7's example shows that this is frequently a *model*
   parameter, not the data.
6. **Test the transform's range.** KC diverges as $\phi \to 1$; Archie fails in
   clay; Gassmann fails at high frequency. Cap the proxy where its own physics
   ends, and say so on the map.
7. **State what is a model and what is a measurement** in the caption. A reader
   must be able to tell which numbers would change if the geology changed.

## 9. Assumptions and regime of validity

**Of the composition.** Each operator's assumptions (lessons 01–03) apply to the
composition without dilution. A proxy is only as valid as its narrowest operator.
In particular: the resistivity route assumes a clean matrix and a single
conducting phase; the velocity route assumes an isotropic, low-frequency,
homogeneous medium and a *chosen* fluid geometry; the porosity-to-permeability
step assumes a grain size and a Kozeny constant.

**Of the uncertainty treatment.** The grid likelihood assumes independent
Gaussian errors with known variance — honest only when the noise level has been
estimated from data, and misleading when the dominant error is model error, which
is *not* Gaussian and does not average down with more data or more grid points.
Augmenting a likelihood with a model-error term is the honest extension and it
widens posteriors, sometimes enough to change the engineering decision.

**Of extrapolation.** A proxy calibrated on one lithology and one saturation
range is not a law. The quantities that carry the geology — $c_K$, $S_0$, $m$,
$n$, $K_\text{dry}$ — are exactly the ones that are fitted, and they are the ones
that change between sites.

## 10. Python demonstration

[`code/geophysical_proxy_relations_demo.py`](./code/geophysical_proxy_relations_demo.py)
prints the analytic and finite-difference amplification factors, the Monte Carlo
table with the plug-in bias, the hypothesis grid with the two forward operators,
the three posterior marginals, the entropy table in bits, and the reference
numbers used above.

```bash
cd 14-hydrology-hydrogeophysics/03-petrophysics-hydrology/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python geophysical_proxy_relations_demo.py
```

## 11. Exercises

Graded problems are in
[`exercises/04-geophysical-proxy-relations-exercises.md`](./exercises/04-geophysical-proxy-relations-exercises.md)
with worked solutions in
[`exercises/04-geophysical-proxy-relations-solutions.md`](./exercises/04-geophysical-proxy-relations-solutions.md).

## Mastery checkpoint

Answer without notes.

> **(a)** Write a proxy as a composition and identify which part is physics and
> which is fitted. **(b)** Derive $\mathrm{d}\ln k/\mathrm{d}\ln\rho_t$ for the
> chain $\rho_t \to \phi \to k$ at $\phi = 0.25$, $m = 2$, and state the units
> convention. **(c)** A Monte Carlo gives $k$ a one-sigma spread of $72\%$ from a
> $20\%$ porosity spread. Explain the ratio with the amplification factor.
> **(d)** In a two-parameter grid, resistivity alone gives $\phi$ to $\pm0.064$
> and velocity alone gives $S_w$ to $\pm0.274$; together they give $\pm0.0043$ and
> $\pm0.012$. Explain why the improvement is so much larger than either
> individual measurement. **(e)** A study needs $\sigma_{\ln k} \le 0.693$; the
> cementation exponent is known to $\pm0.2$ and the grain diameter to $\pm30\%$.
> Compute the achievable $\sigma_{\ln k}$ and state the single most effective
> action.

## Common pitfalls

1. **Reporting a proxy without its amplification factor.** The factor is a
   property of the transform and is not reducible by more of the same data.
2. **Confusing $\mathrm{d}\ln k/\mathrm{d}\ln\phi$ with
   $\mathrm{d}\ln k/\mathrm{d}\phi$.** They differ by a factor of $\phi$.
3. **Treating the posterior maximum as the answer.** The width carries the
   information needed for a decision.
4. **Using a Gaussian likelihood for a model error.** Model error does not
   average down; it must be added as a bias term, and it usually dominates.
5. **Reporting the entropy without the grid.** Entropy depends on resolution;
   report gains.
6. **Extrapolating a fitted transform.** $c_K$, $S_0$, $m$ and $n$ carry the
   geology and change between sites.
7. **Acquiring more of the same data.** When the dominant error is a model
   parameter, a second *kind* of measurement is the only thing that helps.

## Related modules

- [01 Porosity-Permeability and Kozeny-Carman Relations](01-porosity-permeability-relations.md).
- [02 Archie's Law and Saturation Estimation](02-archie-and-saturation.md).
- [03 Seismic Velocity vs Saturation and Gassmann](03-seismic-velocity-saturation.md).
- [Module 14-05 Time-Lapse and Monitoring Hydrogeophysics](../05-hydrogeophysical-monitoring/README.md) —
  where the same proxies are applied repeatedly to differences in time.
- [Module 18-05 Bayesian Inversion](../../18-inverse-problems/05-bayesian-inversion/README.md) —
  the systematic theory behind Section 5.
- [Module 18-07 Joint and Multi-Physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md) —
  formal joint inversion of the two operators used here.
- [18-06-01 Taxonomy of Uncertainty](../../18-inverse-problems/06-uncertainty-quantification/01-uncertainty-taxonomy.md) —
  aleatory versus epistemic versus structural error, which Section 9 depends on.
- [21-04-01 ML Taxonomy](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/01-ml-taxonomy.md) —
  learned proxies, which inherit every warning above and add a training-set one.
