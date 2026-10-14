---
id: 08-05-04
title: "EM Inversion and Dimensionality"
level: research
prereqs: ["08-05-01", "08-05-03", "18-01-03"]
tags: [geomagnetism, electromagnetism, inversion, resolution, non-uniqueness, dimensionality]
---

# EM Inversion and Dimensionality

An EM inversion takes a set of responses and returns a conductivity model. The
hard part is not the algebra; it is knowing what the returned model is a
statement about. A one-dimensional inversion of a one-dimensional data set still
has a null space, and a one-dimensional inversion of a data set containing
two-dimensional structure returns a confident, smooth, wrong answer. This lesson
makes both statements quantitative, on synthetic data whose true model is known
exactly — which is the only situation in which the words "wrong answer" have a
defensible meaning.

The lesson builds the apparatus in the order it is used: a misfit with a stated
noise model and therefore a target misfit; a regularised (Occam) functional and
its misfit-versus-roughness trade-off; the singular-value decomposition of the
Jacobian as the honest statement of resolution; and a static-shift experiment
that shows the difference between an error a 1-D model can absorb and one it
cannot.

All models and data in this module are **SYNTHETIC**. The Earth model in this
lesson generates its own data, the noise comes from a fixed seed, and no real
survey appears anywhere.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** a weighted least-squares misfit for complex EM data, **state** the
   target value implied by the noise model, and **explain** why a misfit below
   the target is not an achievement.
2. **Derive** the Occam (minimum-structure) functional and its Gauss-Newton normal
   equations, and **compute** them for a layered parametrisation.
3. **Produce** a misfit-versus-roughness trade-off and **select** the models that
   are defensible rather than the single model that fits best.
4. **Demonstrate** non-uniqueness by exhibiting two different models with the same
   misfit, and **state** what extra information the choice between them requires.
5. **Compute** the singular values of the weighted Jacobian, the model resolution
   kernel, and the formal uncertainty along each singular direction, and
   **interpret** them in metres and in log-conductivity units.
6. **Distinguish** dimensional errors that a 1-D inversion absorbs (amplitude
   errors, which become conductivity bias) from those it cannot (phase errors,
   which remain as misfit).
7. **Specify** the five items that make an EM inversion reproducible and
   falsifiable.

## Prerequisites

- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md)
  — the response and its noise-relevant scaling.
- [08-05-03 EM Forward Modelling: Integral Equation, FD, FE Methods](03-em-modelling.md)
  — the forward solver, its verification and its equivalence classes.
- [18-01-03 Null Space and Resolution](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)
  — the general theory of what an inverse problem can and cannot determine.

## 1. The three choices that define an inversion

Every inversion is fixed by three decisions, and all three must be reported.

1. **The parametrisation.** Here: $\log_{10}\sigma$ in six layers, thicknesses
   fixed at $10, 20, 30, 60, 120\ \mathrm{m}$ plus a halfspace, with bounds
   $-4 \le \log_{10}\sigma \le 1$. Conductivity is parametrised logarithmically
   because it spans orders of magnitude, and the roughness penalty is then applied
   to $\log_{10}\sigma$, which makes it a statement about *ratios* of
   conductivity between neighbouring layers.
2. **The misfit.** For complex data $d_i$ with standard deviations $w_i$, the
   weighted misfit is
   $$\chi^2=\frac{1}{N}\sum_{i=1}^{N}
   \frac{\left|d_i^{\text{pred}}-d_i^{\text{obs}}\right|^2}{w_i^2},$$
   with each complex datum contributing its real and imaginary parts. If the
   $w_i$ are the true standard deviations, $\mathbb{E}[\chi^2]=1$: **one is the
   target, and lower is not better.** In this lesson's synthetic data the noise
   is $2\%$ of the amplitude plus a $2\ \mathrm{ppm}$ floor, and the true model
   scores $\chi^2=0.7468$ against the particular realisation — so the target for
   this data set is $0.75$, not $1.00$. Synthetic work has that luxury; field work
   has to argue for its weights.
3. **The regularisation.** Minimum structure: add $\mu\lVert R\mathbf{m}\rVert^2$
   with $R$ a first-difference operator, and solve
   $$\Phi(\mathbf{m})=\lVert W(\mathbf{d}^{\text{pred}}(\mathbf{m})
   -\mathbf{d}^{\text{obs}})\rVert^2+\mu\lVert R\mathbf{m}\rVert^2
   \quad\text{minimised over }\mathbf{m}.$$
   $\mu$ is not a physical parameter. It is the dial that trades misfit against
   model structure, and the honest output of an Occam inversion is a *family* of
   models along that trade-off.

## 2. The Occam functional and its normal equations

Write the weighted residual $\mathbf{r}(\mathbf{m})=W(\mathbf{d}^{\text{pred}}
-\mathbf{d}^{\text{obs}})$ and let $J=\partial\mathbf{r}/\partial\mathbf{m}$ be the
Jacobian. Expanding $\mathbf{r}$ to first order about the current model,

$$\Phi\approx\lVert\mathbf{r}+J\Delta\mathbf{m}\rVert^2
+\mu\lVert R(\mathbf{m}+\Delta\mathbf{m})\rVert^2,$$

and setting $\partial\Phi/\partial\Delta\mathbf{m}=0$ gives the **normal
equations**

$$\boxed{\;\left(J^{\mathsf{T}}J+\mu R^{\mathsf{T}}R\right)\Delta\mathbf{m}
=-J^{\mathsf{T}}\mathbf{r}-\mu R^{\mathsf{T}}R\,\mathbf{m}.\;}$$

This is a $6\times6$ complex system here — tiny — but the same equation governs
inversions with $10^4$ parameters, where $J^{\mathsf{T}}J$ is never formed and a
conjugate-gradient method is used instead. The demonstration computes $J$ by
central differences in $\log_{10}\sigma$ (one perturbation per parameter per
iteration, $6$ parameters) and applies a line search: if the full step increases
$\Phi$, the step is halved, then quartered. Two implementation points carry more
weight than they look:

- **The forward model must be smooth in the parameters.** The
  [wavenumber grid](03-em-modelling.md) in the layered solver depends on the
  smallest layer thickness and on $|k|$; if it is recomputed per model, the
  response jumps discontinuously at grid changes and the numerical Jacobian is
  garbage. Fix the grid per frequency, once, from the parametrisation.
- **The sign of the update matters more than its size.** Writing
  $\mathbf{r}=\mathbf{d}^{\text{pred}}-\mathbf{d}^{\text{obs}}$, the descent
  direction is $-J^{\mathsf{T}}\mathbf{r}$; a sign slip there produces exactly the
  symptom of an inversion that never leaves its starting model, which is easy to
  misread as "the data are uninformative".

## 3. The trade-off, measured

With the starting model uniform at $0.01\ \mathrm{S\,m^{-1}}$:

| $\mu$ | $\chi^2$ | roughness | $\sigma$ range (S/m) |
|---|---|---|---|
| $10^{-3}$ | 0.3999 | 2.1466 | 0.00283 – 0.11390 |
| $10^{-2}$ | 0.4003 | 1.8642 | 0.00490 – 0.11286 |
| $10^{-1}$ | 0.4035 | 1.5358 | 0.00820 – 0.11033 |
| $1$ | 0.4173 | 1.3531 | 0.00816 – 0.10677 |
| $10$ | 0.5906 | 1.1672 | 0.01003 – 0.10635 |
| $100$ | 3.1621 | 0.7403 | 0.01757 – 0.10884 |
| $10^{3}$ | 13.4538 | 0.3675 | 0.02577 – 0.09023 |

Three readings, in order of importance.

- **The fitted $\sigma$ range is stable** across four orders of magnitude of
  $\mu$: the conductive layer is found at $0.09$–$0.11\ \mathrm{S\,m^{-1}}$
  whatever the regularisation. The *robust* part of the answer is the existence
  and conductivity of that layer.
- **The structure is not stable.** Roughness ranges from $2.15$ to $0.37$: the
  model can be a sharp interface or a gradual ramp, and the misfit of the smooth
  one is worse but still acceptable.
- **The target misfit selects a band of $\mu$**, here roughly
  $10^{-3}\lesssim\mu\lesssim10$: everything in that band has $\chi^2$ at or
  below the target, so the data do not choose within it. Reporting the smallest-$\mu$
  model would be reporting an arbitrary member of a set.

## 4. Non-uniqueness, exhibited rather than asserted

Two inversions of the *same* six data, differing only in the starting model and
the regularisation:

| layer | centre depth (m) | model A ($\mu=10$) | model B ($\mu=0.1$) | A/B |
|---|---|---|---|---|
| 1 | 5 | 0.01209 | 0.01130 | 1.07 |
| 2 | 20 | 0.01003 | 0.00821 | 1.22 |
| 3 | 45 | 0.09705 | 0.10096 | 0.96 |
| 4 | 90 | 0.10635 | 0.11047 | 0.96 |
| 5 | 180 | 0.02659 | 0.00985 | 2.70 |
| 6 | 360 | 0.01921 | 0.01862 | 1.03 |

with $\chi^2_A=0.5906$, roughness $1.1672$, and $\chi^2_B=0.4033$, roughness
$1.5449$; the true model is
$[0.01,0.01,0.10,0.10,0.02,0.02]$. Both fit the data at least as well as the true
model does ($0.75$), both recover the conductive layer correctly, and they differ
by a factor of $2.7$ in the third layer below the conductor. **The data do not
choose between them.** What chooses is prior information: a borehole, a
geological cross-section, a nearby sounding with a different geometry, or an
explicitly stated preference for smoothness.

This is the same structure that [08-05-03](03-em-modelling.md) §5 measured from
the modelling side: equivalence classes of models with indistinguishable
responses. Inversion does not create the ambiguity; it inherits it, and the only
defence is to report it.

## 5. Resolution: what the Jacobian can and cannot see

### 5.1 The resolution matrix

Linearising about the Occam solution $\mathbf{m}_\infty$, the estimate is a
filtered version of the true perturbation:

$$\hat{\mathbf{m}}-\mathbf{m}_\infty
=\underbrace{\left(J^{\mathsf{T}}J+\mu R^{\mathsf{T}}R\right)^{-1}
J^{\mathsf{T}}J}_{R_m}\,
\left(\mathbf{m}^{\text{true}}-\mathbf{m}_\infty\right)+\text{noise}.$$

$R_m$ is the **model resolution matrix**: its $i$-th row is the resolution kernel
of layer $i$ — the pattern of true-model perturbations that would produce an
apparent perturbation in layer $i$ alone. If $R_m$ were the identity, every layer
would be independently determined; in practice its rows are smeared over
neighbouring layers, and the width of the smear is the depth resolution.

### 5.2 Singular values, measured

The demonstration computes $J$ at the Occam solution and takes its singular
values:

$$s=[145.7011,\ 39.4459,\ 10.8823,\ 5.3525,\ 2.9098,\ 1.0397].$$

The ratio of largest to smallest is $1.4\times10^{2}$: there is no exact null
direction, but there are directions the data barely see. Counting those above $5\%$
of the largest gives **3 of 6** — the honest headline number for this
parametrisation and this frequency band. The formal $1\sigma$ uncertainty along
direction $k$ is $\sqrt{\chi^2}/s_k$ in $\log_{10}$ units:

$$[0.005,\ 0.019,\ 0.071,\ 0.144,\ 0.264,\ 0.739].$$

So the best-determined *combination* of layer conductivities is pinned to about
$1\%$, and the worst to a factor of five. A published model that quotes one number
per layer without these figures is quoting the projection of a five-fold
uncertainty onto an arbitrary basis.

### 5.3 Resolution kernels, measured

Taking the row-wise widths of $R_m$ (sum over layers of the absolute kernel value
times the distance from the centre, normalised):

| layer | centre depth (m) | kernel width (m) | kernel peak |
|---|---|---|---|
| 1 | 5 | 46.0 | 0.125 |
| 2 | 20 | 22.0 | 0.912 |
| 3 | 45 | 13.0 | 0.968 |
| 4 | 90 | 25.2 | 0.967 |
| 5 | 180 | 119.9 | 0.027 |
| 6 | 360 | 296.2 | 0.002 |

The pattern is exactly what the physics predicts and it is worth reading
carefully. Layer 1 has a peak of only $0.125$: a perturbation of the top layer is
almost entirely explained by perturbing its neighbours, because a thin resistive
surface layer and a slightly different second layer produce nearly the same
response. Layers 2–4 have peaks above $0.9$ and widths of $13$–$25\ \mathrm{m}$,
comparable with their thicknesses: the conductor is genuinely resolved. Layers 5
and 6 have negligible peaks and widths of hundreds of metres: **the deepest part
of the model is not resolved at all**, and any structure reported there is
inherited from the roughness penalty, not from the data. A typical published
"layered model" hides this by drawing the same line weight at every depth.

## 6. Dimensionality: the error a 1-D model can absorb

One-dimensional inversion of a 1-D data set is a solved problem. The hard case is
a 1-D inversion of data containing 2-D or 3-D effects, and the key question is
which errors are *absorbed* (and therefore invisible) and which are not.

Multiply the synthetic data by a frequency-independent factor $F$ — what a
lateral conductivity change, a calibration error or a coil misorientation
produces:

| $F$ | $\chi^2$ to its own data | $\sigma$ in layer 3 (S/m) | $\chi^2$ to the real data |
|---|---|---|---|
| $1.15$ (real) | 0.548 | 0.11228 | 29.16 |
| $1.15e^{+0.35i}$ | 107.548 | 0.05215 | 47.76 |
| $1.15e^{-0.35i}$ | 44.184 | 0.03460 | 158.74 |

- A **real amplitude factor is absorbed**: the inversion reaches $\chi^2=0.548$ to
  its own data — indistinguishable from a good fit — with a $+12\%$ bias in the
  conductor's conductivity ($0.112$ against the true $0.100$). Nothing in the
  inversion output looks wrong. Only an independent constraint reveals it.
- A **complex factor is not absorbed**: the misfit to the shifted data stays at
  $107$ or $44$, i.e. tens of times the target. A conductivity model cannot
  produce a frequency-independent phase rotation, so the failure is *visible*.

That asymmetry is the practical rule: **amplitude errors masquerade as
conductivity bias; phase errors leave a fingerprint in the misfit.** It is also
why a phase-calibrated system is worth its price, and why a single-station 1-D
inversion of data containing 3-D effects must be accompanied by an independent
dimensionality test: the full impedance tensor's off-diagonal symmetry, the
tipper (vertical-field) response, or consistency between neighbouring soundings
with different geometry. Fitting a *tensor* rather than one component is the same
idea applied to the data rather than to the model.

## 7. Assumptions and regime of validity

1. **The noise model is correct.** $\chi^2$ is only a misfit if the $w_i$ are the
   standard deviations. The demonstration's $2\%+2\ \mathrm{ppm}$ model is
   synthetic and known; in the field it must be estimated, and an underestimated
   weight drives the inversion to over-fit structure.
2. **The forward model is adequate.** Everything here uses the verified layered
   solver of [08-05-03](03-em-modelling.md). Model error of a few per cent (as
   measured there) is larger than the noise-driven error and sets the real
   uncertainty floor.
3. **The parametrisation bounds the answer.** Six layers with fixed thicknesses
   cannot represent a thin buried sheet; its conductance will be smeared into a
   layer. This is a statement about the parametrisation, not about the data.
4. **The Jacobian is local.** Gauss-Newton assumes the misfit is approximately
   quadratic near the current model. For a very poor starting model the update
   may point uphill, which is why the line search (and, in principle, a global
   search) is part of the method.
5. **Resolution statements are conditional.** The singular values and kernels
   above belong to *this* parametrisation, *this* band and *this* geometry.
   Change the frequency range and they change; quoting them without the
   conditions quotes nothing.
6. **The 1-D assumption is the dominant error.** The static-shift experiment
   quantifies one consequence; real 3-D effects do not multiply the data by a
   single complex number, they distort the frequency dependence.

## 8. Fully worked numeric example

Compute the target misfit and the resolution-based uncertainty for the
demonstration's data.

1. Noise per datum: $w_i=\sqrt{(0.02|d_i|)^2+(2\times10^{-6})^2}$. At $10\ \mathrm{Hz}$,
   $|d|=\sqrt{69.5^2+1438.4^2}\times10^{-6}=1.4401\times10^{-3}$, so
   $0.02|d|=2.8802\times10^{-5}$ and
   $w_i=\sqrt{(2.8802\times10^{-5})^2+(2\times10^{-6})^2}=2.8872\times10^{-5}$,
   i.e. $28.87\ \mathrm{ppm}$. At $3\ \mathrm{kHz}$,
   $|d|=\sqrt{95500^2+64875.6^2}\times10^{-6}=1.1545\times10^{-1}$,
   $w_i=2.3090\times10^{-3}$, i.e. $2309\ \mathrm{ppm}$: the weights differ by a
   factor of $80$ across the band, which is why an unweighted fit would be
   dominated by the highest frequency.
2. For six complex data and six parameters with a roughness penalty, the
   expected $\chi^2$ of the true model is $1$ if the weights are the standard
   deviations; this realisation gives $0.7468$, and the two Occam models give
   $0.5906$ and $0.4033$. Both are *below* the target, i.e. they fit the
   fluctuation as well as the signal — the signature of over-fitting a single
   realisation, and the reason a set of models is reported.
3. Formal uncertainty: from $\delta m_k=\sqrt{\chi^2}/s_k$ with
   $\sqrt{0.591}=0.769$, the weakest direction has
   $\delta m_6=0.769/1.0397=0.739$ in $\log_{10}$ units, i.e. a factor
   $10^{0.739}=5.5$ in conductivity. No feature of the model that requires
   distinguishing $\sigma_6$ from its neighbours can be supported by these data.

## 9. Python demonstration

`code/em_inversion_demo.py` computes everything above. It:

1. builds a synthetic layered Earth, its response at six frequencies, and one
   noise realisation with a stated weighting;
2. runs a Gauss-Newton Occam inversion with a line search for seven values of the
   roughness weight, and prints the misfit-versus-roughness trade-off;
3. inverts the same data from two different starting models to exhibit
   non-uniqueness;
4. computes the weighted Jacobian, its singular values, the formal uncertainty
   per singular direction and the resolution kernel widths per layer;
5. multiplies the data by real and complex static factors and reports what the
   inversion does with each;
6. lists what an EM inversion must report to be reproducible.

It is print-only, uses `np.random.default_rng(20261014)`, needs no network, and
finishes in about four seconds.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/04-em-inversion-exercises.md`](./exercises/04-em-inversion-exercises.md)
and
[`exercises/04-em-inversion-solutions.md`](./exercises/04-em-inversion-solutions.md).

- **★** Compute the weighted misfit of a stated model against stated data and say
  whether it is over- or under-fitting.
- **★★** Derive the Occam normal equations and explain the role of each term.
- **★★** Given $s_{\min}=1.04$ and $\chi^2=0.59$, compute the formal uncertainty
  in the weakest direction in $\log_{10}\sigma$ and in percent.
- **★★★** Design a survey and inversion strategy that would resolve the layer-6
  conductivity of the demonstration's model to a factor of two, and say how much
  it costs.

## Mastery checkpoint

Without notes:

> An inversion of a six-frequency coplanar-coil sounding returns a smooth model
> with $\chi^2=0.6$ and a conductor of $0.1\ \mathrm{S\,m^{-1}}$ at a depth of
> about $40\ \mathrm{m}$. **(a)** Why is $\chi^2=0.6$ not better than
> $\chi^2=1.0$? **(b)** The singular values of the Jacobian are $[146, 39, 11,
> 5.4, 2.9, 1.0]$. How many independent conductivity combinations does the data
> set constrain? **(c)** The resolution kernel for the deepest layer has a peak of
> $0.002$ and a width of $296\ \mathrm{m}$. State in one sentence what you can
> claim about that layer. **(d)** A colleague's survey has a $10^\circ$ phase
> calibration error. Predict, with a reason, whether their inversion will show a
> large misfit or a plausible model with a biased conductivity.

## Common pitfalls

1. **Reporting the best-fitting model.** The best fit is the roughest model and
   usually the least believable.
2. **Treating $\chi^2<1$ as success.** It means the weights are too large or the
   realisation is being fitted rather than the signal.
3. **Quoting one number per layer.** The resolution kernel and the singular-value
   spectrum are part of the model.
4. **Recomputing the quadrature per model.** It makes the Jacobian discontinuous
   and the inversion stall, which then gets blamed on the data.
5. **Assuming a 1-D inversion detects 2-D structure.** Amplitude effects are
   absorbed silently; only phase effects and multi-component data protest.
6. **Fixing the parametrisation and calling the result resolution-free.** The
   layer boundaries were chosen by the analyst; a thin sheet between boundaries
   cannot be recovered.
7. **Confusing model error with noise.** In these examples the dimensional error
   ($\chi^2$ of tens) exceeds the noise-driven misfit by more than an order of
   magnitude.

## Related modules

- [08-05-03 EM Forward Modelling: Integral Equation, FD, FE Methods](03-em-modelling.md)
  — the forward solver and the equivalence classes the inversion inherits.
- [08-05-01 Frequency-Domain EM (FDEM) Systems and Responses](01-frequency-domain-em.md)
  — the response and the conductivity–separation ambiguity.
- [08-05-05 Airborne EM for Conductivity Mapping](05-airborne-em.md) — the same
  inversion with an unknown height.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of regularisation, null spaces and resolution.
- [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md) — the
  probabilistic formulation of the same trade-off.
