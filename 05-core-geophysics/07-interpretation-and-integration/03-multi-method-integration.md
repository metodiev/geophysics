---
id: 05-07-03
title: "Integrating Multiple Methods and Constraints"
level: graduate
prereqs: ["05-07-02", "18-07-01", "02-08-06"]
tags: [joint-interpretation, ambiguity, equivalence, conductance, multi-physics, priors]
---

# Integrating Multiple Methods and Constraints

## Learning objectives

By the end of this lesson you will be able to:

1. **State** what a second, physically independent dataset actually buys: it
   reduces the feasible set of models, and it never collapses it to a point.
2. **Derive** the equivalent-stratum result for potential fields and the
   conductance equivalence for a thin conducting layer, and show they are the
   same failure in different physics.
3. **Compute** the feasible set of a simple 1-D model by grid search, and
   quantify how much a seismic thickness and a borehole conductivity each shrink
   it.
4. **Distinguish** *ambiguity* (many models fit) from *insensitivity* (the data
   cannot see the parameter at all), and show that a parameter can be constrained
   yet ambiguous.
5. **Recognise** a conflict between two datasets, compute the misfit that each
   would require of the other, and report that the data do not agree.
6. **Explain** why "the model" is a choice constrained by assumptions, and why a
   resolution or detectability study belongs *before* acquisition.

## Prerequisites

- [05-07-02 Quantitative Interpretation and Depth Estimation](./02-quantitative-interpretation.md)
  — misfit, model families and parameter covariance.
- [18-07-01 Why Joint Inversion: Complementary Sensitivities](../../18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md)
  — the general theory of which dataset constrains which parameters.
- [02-08-06 Uniqueness Theorems and Boundary Conditions](../../02-physics/08-potential-theory/06-uniqueness-theorems.md)
  — the proof of the equivalent stratum used in Section 3.1.
- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — the conductivity scale and the skin-depth relation.

## 1. Intuition: independence is the only thing that pays

Every geophysical method measures a *field* and infers a *property distribution*.
Two datasets constrain the same geology only if two conditions hold:

- **Different physics.** Gravity senses mass density; seismics sense elastic
  moduli; MT senses electrical conductivity. If two datasets respond to the same
  property through the same kernel, adding the second is re-weighting, not
  integration.
- **Transverse sensitivity.** Even different physics can fail to help. What
  constrains a model is sensitivity in the *null-space direction* of the other
  dataset. A dataset whose sensitivity is parallel to an ambiguity cannot remove
  it.

This lesson's central demonstration is quantitative. A three-layer MT model is
inverted by exhaustive search. Then two independent measurements are added — a
seismic thickness (elasticity) and a borehole conductivity (a direct rock
measurement). The feasible set shrinks, and then stops shrinking, and the reason
it stops is physics rather than data volume.

The second, more important point is that integration does not manufacture
agreement. When two independent datasets are fitted by models that cannot both be
true, the honest output is *"the data disagree, and here is by how much"*. That
outcome is more valuable than a compromise model, because it tells you something
about the Earth that neither dataset contained.

Finally: none of this can be done after the survey. Whether a second dataset will
help is decided by the *sensitivity kernels* and the *null spaces*, both of which
are properties of the acquisition geometry and physics. That is what a resolution
study is, and it is why it belongs in the survey plan
([05-05-01 Survey Planning](../05-survey-design-and-acquisition/01-survey-planning.md)).

## 2. Precise definitions

### 2.1 Feasible set

Given a data vector $\mathbf{d}$ with covariance $\mathbf{C}_d$ and a forward
operator $\mathcal{F}$, the **feasible set** at a stated misfit threshold is

$$\mathcal{S}(\chi^2_{\max}) = \left\{\mathbf{m} : \left(\mathbf{d} -
\mathcal{F}[\mathbf{m}]\right)^{\!\top}\mathbf{C}_d^{-1}
\left(\mathbf{d} - \mathcal{F}[\mathbf{m}]\right) \le \chi^2_{\max}\right\}.$$

In this lesson the threshold is expressed as an RMS misfit in
$\log_{10}\rho_a$ and set to 0.01 (1 per cent), and the set is found by exhaustive
grid search over $(h_2, \rho_2)$ — 40 000 models at 200 × 200 resolution.

### 2.2 Equivalence class

An **equivalence class** is a connected component of the feasible set along which
the model changes substantially while the data do not. The equivalent stratum of
potential theory and the conductance equivalence of EM are the two canonical
examples.

### 2.3 Ambiguity versus insensitivity

- **Ambiguous:** the data constrain the model, and the feasible set is a
  non-degenerate set. Every model in it fits equally well.
- **Insensitive:** the data do not depend on the parameter at all, so the
  feasible set is unbounded in that direction.

Both are reported as "uncertain", and only the first is reduced by a better
inversion. The demonstration measures both and shows they behave differently.

### 2.4 Joint misfit

For two independent datasets the joint objective is the sum, not the product, and
only when the forward maps share model parameters:

$$\Phi_{\text{joint}}(\mathbf{m}) = \Phi_1(\mathbf{m}) + \Phi_2(\mathbf{m}). \tag{1}$$

Writing it as a sum is not a convenience: it follows from the two likelihoods
being independent, and it is the reason an outlier in one dataset cannot be
"averaged out" by the other.

## 3. Derivations

### 3.1 The equivalent stratum, restated

For a 2-D potential field, the uniqueness theorem for the exterior Dirichlet
problem guarantees that the *field* above the sources is unique, while the
*source* is not. The constructive counterexample is the equivalent stratum: for
every depth $h$ there is a surface density $\sigma(x)$ (the "stratum") that
reproduces the same external field. The proof, and its construction, are in
[02-08-06](../../02-physics/08-potential-theory/06-uniqueness-theorems.md); the
operational consequence is that

$$\text{depth and mass are separately undetermined by a potential field alone,}$$

and no amount of additional gravity data — including gravity gradiometry —
changes that, because the annihilator (the null-space element) is itself
harmonic.

### 3.2 Conductance equivalence for a thin conductor

Consider a horizontal layer of resistivity $\rho$ and thickness $h$. The skin
depth in it is $\delta = \sqrt{2\rho/(\mu_0\omega)}$. When $h \ll \delta$, the
electric field is nearly uniform across the layer, so the total sheet current is

$$\int_0^h \sigma E\,\mathrm{d}z \approx \sigma h E = \frac{h}{\rho}E = S E,
\qquad S \equiv \frac{h}{\rho}. \tag{2}$$

The layer therefore enters the boundary conditions only through its **conductance**
$S$, to first order in $h/\delta$: the tangential electric field is continuous and
the tangential magnetic field jumps by an amount proportional to $S E$. Two
layers with the same $S$ and the same bounding media are then indistinguishable,
which is exactly what the demonstration measures: models of
$(h_2, \rho_2) = (50, 1)$, $(100, 2)$ and $(200, 4)$ — all with $S = 50$ m Ω⁻¹ —
agree to 0.0006 and 0.0017 in log₁₀.

**Where it breaks.** The equivalence is a first-order result in $h/\delta$. Push
to $(1000, 20)$ — same $S = 50$ m Ω⁻¹ — and the deviation rises to 0.0109 in
log₁₀, a factor of six worse, because $h/\delta$ is no longer small. Equivalence
is a regime with a boundary, and the boundary is a physical statement, not a
numerical one.

### 3.3 Why the feasible set is a curve

Equations (2) constrains one combination, $S$. With three unknowns
$(h_2, \rho_2)$ plus the bounding resistivities, one constraint leaves a
one-parameter family: a curve. The demonstration's feasible set spans a 16.4 per
cent relative thickness range while its conductance spans only 5.5 per cent —
the data constrain the product about three times better than either factor.

Only at longer periods does the response begin to depend on $h_2$ and $\rho_2$
separately (through the second-order term in $h/\delta$), which is the entire
mechanism by which a *broadband* sounding narrows the curve. Broadband acquisition
is therefore not a luxury: it is the only EM-internal way to reduce the
equivalence.

### 3.4 How much an independent dataset buys

Adding the seismic thickness $h_2 = 300 \pm 15$ m removes 6 of 21 models: the
thickness spread falls from 16.4 per cent to 9.6 per cent, and the
resistivity range narrows from $[9.44, 10.72]$ to $[9.44, 10.45]$ — a factor of
only 1.3. Adding the borehole resistivity $10 \pm 1$ Ω m removes none, because
every surviving model already lies inside that interval.

The lesson is structural: **a constraint removes model space in the direction it
is sensitive to.** Seismic is sensitive to thickness, so it prunes the ends of
the curve; it says nothing about resistivity, so it cannot collapse it.

### 3.5 The conflict: when two datasets cannot both be right

Suppose a seismic pick puts the layer at 150 m. Compute, for that thickness, the
best achievable MT misfit over all $\rho_2$:

$$\min_{\rho_2}\ \left\|\log_{10}\rho_a^{\text{model}}(h_2 = 150) -
\log_{10}\rho_a^{\text{obs}}\right\|_{\text{RMS}} = 0.0660, \tag{3}$$

against an MT tolerance of 0.0100 — the required misfit is **6.6 times** what the
MT data can absorb. There is no compromise model: the two datasets are
inconsistent at the stated uncertainties. The correct report is a statement of
inconsistency plus an investigation of which dataset has the wrong model — in
this case, a mis-picked multiple on the seismic section is the usual culprit.

### 3.6 The prediction test

A fitted model can be used to *predict* an observation it was not fitted to. The
demonstration adopts $h_2 = 299.5$ m, $\rho_2 = 9.99$ Ω m from the joint feasible
set (log-RMS 0.0087 against its own data) and predicts a neighbouring MT sounding
whose true layer is 420 m. The prediction log-RMS is **0.1154**, thirteen times
its own misfit. The 1-D model was an assumption; the neighbouring site violates
it.

Prediction tests are the cheapest validation available and the least used,
because they cost nothing and they can fail.

## 4. Worked examples

### 4.1 Building and reading a feasible set

**Problem.** A three-layer MT model with $\rho_1 = 100$ Ω m, $h_1 = 100$ m,
$\rho_2 = 10$ Ω m, $h_2 = 300$ m, $\rho_3 = 500$ Ω m produces a synthetic sounding
over periods 0.01–1000 s. How well is $h_2$ determined?

*Step 1 — validate the forward operator.* A half-space of 50 Ω m returns
$\rho_a = 50$ Ω m with maximum relative error $4.4\times10^{-16}$, and a
two-layer model returns its 50 Ω m top layer at $T \le 10^{-5}$ s. Without these
two checks no inversion result means anything.

*Step 2 — grid the model space.* 200 values of $h_2$ from 80 to 900 m, 200 values
of $\rho_2$ from 2.5 to 400 Ω m, 40 000 forward computations of 21 periods.

*Step 3 — count the feasible models.* 21 models fit to within 1 per cent in
$\log_{10}\rho_a$. Their thicknesses span 278–327 m and their resistivities
9.44–10.72 Ω m.

*Step 4 — report.* $h_2 = 300$ m, with a feasible range of $\pm$8 per cent at the
1 per cent misfit level, *given the three-layer model family*. The statement is
conditional on the family, and if the boundary is gradational the answer changes
(Section 4.3).

### 4.2 What "unresolved" is not

**Problem.** Does the basement resistivity matter? Change $\rho_3$ by a factor of
two and re-run.

*Measured.* $\rho_3 \times 2$ changes the apparent resistivity by up to
**92.8 per cent**; $\rho_3 \times 0.5$, by **48.7 per cent**. The basement is
strongly constrained.

This is the distinction of §2.3: the layer is *ambiguous* (a curve of models fits)
but not *insensitive*. Claiming "MT cannot see the basement" would be false;
claiming "MT cannot separate $h_2$ from $\rho_2$" is true and is a different
statement.

### 4.3 Where the residual ambiguity actually lives

With all three constraints applied, the demonstration still cannot determine:

- **$h_2$ to better than $\pm$4 per cent** — the seismic pick's own uncertainty.
- **$\rho_2$ to better than 0.5 Ω m** — set by the conductance curve.
- **The sharpness of the boundary.** A 25 m gradational transition fits the sharp
  model's response to 0.0076 in log₁₀ (inside the 1 per cent tolerance); a 100 m
  transition misfits by 0.0314; a 200 m transition by 0.0659. So the sharpness is
  constrained to be less than roughly 50 m — a *bound*, not a value, and on an
  unconformity or a fault that bound is the geologically interesting number.

None of these can be removed by inverting harder. They are properties of what the
data contain.

## 5. Assumptions

1. **Each forward operator is validated** against an exact limit before it is
   used. Section 4.1 does this for MT; it must be done for every method.
2. **The noise model is correct.** The 1 per cent tolerance here is *synthetic*;
   real MT noise is non-Gaussian, correlated between periods, and often
   underestimated by static shifts.
3. **Both datasets are fitted by the same earth.** The conflict of §3.5 violates
   this and that is the diagnosis.
4. **1-D (layered) geology.** All of Section 3 survives only if the structure is
   laterally uniform; the prediction test of §3.6 is designed to catch the case
   where it is not.
5. **Independence of the datasets.** If the "independent" dataset shares a source
   of error with the first — the same velocity model, the same static shift — the
   joint misfit is not a sum and the apparent agreement is illusory.
6. **The chosen model family contains the truth.** If it does not, the feasible
   set is the wrong set, however narrow it looks.

## 6. Units and dimensional analysis

- **Conductance** $S = h/\rho$: m/(Ω m) = Ω⁻¹ = S (siemens). The demonstration
  quotes it in m Ω⁻¹, which is the same thing; the unit is worth writing
  explicitly because conductance and resistivity are easy to confuse.
- **Apparent resistivity** $\rho_a = |Z|^2/(\omega\mu_0)$:
  $(\Omega^2)/(\mathrm{s^{-1}\cdot H\,m^{-1}}) =
  \Omega^2 \mathrm{m\,s\,H^{-1}} = \Omega\,\mathrm{m}$ ✓ using $\mathrm{H} =
  \Omega\,\mathrm{s}$.
- **Misfit in log₁₀** is dimensionless, and a value of 0.01 is exactly a 2.3 per
  cent multiplicative error. Comparing an RMS in log space with an RMS in linear
  space is meaningless; state which is used.
- **Skin depth** $\delta = \sqrt{2\rho/(\mu_0\omega)}$: m ✓. The "503 √(ρT)" rule
  with $\rho$ in Ω m and $T$ in s gives metres; it is used in the demonstration to
  show that $T = 0.01$ s already sees through a 100 m, 50 Ω m layer.
- **Misfit ratio** (6.6 in §3.5) is dimensionless — always quote it, because
  *"the misfit was 0.066"* means nothing without the level the data can absorb.

## 7. Python demonstration

`code/multimethod_demo.py` implements the 1-D MT operator, validates it, grid
searches the feasible set, applies the two independent constraints, and runs the
conflict and prediction tests. Predict each block before running.

```python
Z = 1j * w * MU0 / np.sqrt(1j * w * MU0 / layers[-1][0])
for i in range(len(layers) - 2, -1, -1):          # recursion upward
    k_i = np.sqrt(1j * w * MU0 / layers[i][0])
    Z_int = 1j * w * MU0 / k_i
    t = np.tanh(k_i * layers[i][1])
    Z = Z_int * (Z + Z_int * t) / (Z_int + Z * t)
rho_a = abs(Z) ** 2 / (w * MU0)
```

Measured output, abridged:

```
half-space rho = 50 ohm m -> max relative error in rho_a = 4.44e-16
two-layer, T = 1e-6 to 1e-5 s: rho_a = 50.0000 to 50.0000 ohm m (top layer is 50)

models searched                = 40000
models within 1 per cent       = 21
thickness range                = 278 to 327 m   (truth 300 m)
resistivity range              = 9.44 to 10.72 ohm m   (truth 10.00)
conductance h/rho along the set= 29.2 to 30.9 m ohm^-1   (truth 30.0)
relative spread of thickness   = 16.4 per cent
relative spread of conductance = 5.5 per cent

h2 =     50 m, rho2 =   1.0 ohm m, conductance =  50.0 m/ohm : log-RMS = 0.0000
h2 =    100 m, rho2 =   2.0 ohm m, conductance =  50.0 m/ohm : log-RMS = 0.0006
h2 =    200 m, rho2 =   4.0 ohm m, conductance =  50.0 m/ohm : log-RMS = 0.0017
h2 =   1000 m, rho2 =  20.0 ohm m, conductance =  50.0 m/ohm : log-RMS = 0.0109

seismic thickness = 300 +/- 15 m
MT models compatible           = 15 of 21
thickness spread falls from 16.4 to 9.6 per cent
resistivity range narrowed by a factor of 1.3, not collapsed.

basement resistivity x2.0: max change in rho_a =  92.82 per cent
basement resistivity x0.5: max change in rho_a =  48.66 per cent

transition zone    25 m thick: log-RMS vs a sharp boundary = 0.0076
transition zone   100 m thick: log-RMS vs a sharp boundary = 0.0314
transition zone   200 m thick: log-RMS vs a sharp boundary = 0.0659

seismic pick h2 = 150 m; best achievable MT log-misfit over all rho2 = 0.0660
required misfit / tolerance = 6.6

a nearby sounding has a 420 m layer instead of 300 m
model prediction vs that sounding: log-RMS = 0.1154
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Half-space returns its own resistivity to $4\times10^{-16}$ | A forward operator that fails this test invalidates every inversion built on it |
| 21 of 40 000 models fit, spanning a curve | The feasible set must be mapped, not summarised by its best model |
| Conductance spread (5.5 %) is 3× smaller than thickness spread (16.4 %) | The data constrain the product; the factors trade off |
| Equal-conductance models agree to 0.002 in log₁₀ up to $h/\delta \sim 0.1$, then fail | Equivalence is a regime with a measurable boundary |
| Seismic narrows resistivity by only 1.3× | A constraint buys most where its sensitivity is transverse to the ambiguity |
| Basement resistivity changes the response by 92.8 % | Ambiguous ≠ insensitive; say which one you mean |
| A 150 m seismic pick needs 6.6× the MT tolerance | When two datasets conflict, report the conflict |
| The neighbouring sounding misfits by 13× the fitted model's own residual | Prediction is the cheapest test and the most informative |

> **Breaking exercise.** Raise the misfit tolerance from 1 per cent to 2 per cent
> and re-count the feasible set. Predict, before running, whether the *conductance*
> spread or the *thickness* spread grows faster, and explain why from §3.3.

## 8. Exercises

Full sets and solutions:
[`exercises/03-multi-method-integration-exercises.md`](./exercises/03-multi-method-integration-exercises.md)
and
[`exercises/03-multi-method-integration-solutions.md`](./exercises/03-multi-method-integration-solutions.md).

### ★ Foundational

**★1.** Show that $\rho_a = |Z|^2/(\omega\mu_0)$ returns $\rho$ for a uniform
half-space, given $k = \sqrt{\mathrm{i}\omega\mu_0\sigma}$ and
$Z = \mathrm{i}\omega\mu_0/k$.

**★2.** Compute the conductance of layers with $(h, \rho)$ equal to
$(50, 1)$, $(100, 2)$, $(500, 5)$ m Ω m and identify which two are equivalent
and which is not.

**★3.** State, in one sentence each, the difference between an ambiguous
parameter and an insensitive one, and give a geophysical example of each.

### ★★ Applied

**★★4.** Reproduce the feasible-set search with a 3 per cent tolerance. Report
the new thickness and conductance ranges and the ratio of their spreads.

**★★5.** Add a third independent dataset: a borehole temperature gradient that
constrains the thermal conductivity of the layer, hence (weakly, via a
petrophysical relation you must state) its porosity. Explain whether it helps
with $h_2$ or $\rho_2$, and why.

**★★6.** For the conflict of §3.5, compute the misfit ratio for
$h_2 = 200$ m and for $h_2 = 400$ m. At what thickness does the required misfit
fall inside the 1 per cent tolerance, and what does that tell you about the
direction of the inconsistency?

### ★★★ Research-oriented

**★★★7.** Extend the model family to include a linear conductivity gradient
within the layer. Show numerically whether a 100 m gradational transition can be
distinguished from a sharp boundary at the 1 per cent tolerance, and report the
transition thickness at which it can. Relate your answer to the geological
question the survey was asked.

**★★★8.** Design a resolution study for a two-method survey over a target at
800 m depth: choose a second method, derive its sensitivity kernel, identify the
transverse direction, and estimate the reduction in the feasible-set volume that
the second method would deliver. State explicitly which assumptions your estimate
rests on, and what would falsify it. Compare your design with
[18-07-01](../../18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md).

## 9. Common mistakes

1. **Adding a dataset that measures the same physics.** Two gravity datasets do
   not break the equivalent stratum; they refine the same numbers.
2. **Reporting the best-fitting model as "the model".** The feasible set is the
   result; the best fit is one point in it.
3. **Confusing ambiguity with insensitivity.** Section 4.2 shows a parameter
   (basement resistivity) that is constrained by tens of per cent while the
   overlying layer's thickness and resistivity remain ambiguous.
4. **Averaging conflicting datasets into a compromise.** A compromise model
   reproduces neither dataset and hides the disagreement that is the finding.
5. **Assuming independence.** Two datasets sharing a velocity model or a static
   shift are not independent, and their joint misfit is not a sum.
6. **Doing the resolution study after acquisition.** By then the geometry that
   determines the null space is fixed.
7. **Quoting a misfit without its tolerance.** "Misfit 0.066" is uninterpretable;
   "6.6 times what the data can absorb" is a finding.

## 10. Real-world applications

- **Hydrocarbon exploration.** Seismic (elastic) plus CSEM (conductive) plus
  gravity (dense) is the standard multi-physics combination precisely because the
  three sensitivities are transverse; the interpretation is a joint feasible set,
  not a stack of maps
  ([18-07-03 Petrophysically Coupled Joint Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/03-petrophysical-joint-inversion.md)).
- **Geothermal resource assessment.** MT for clay-cap and reservoir extent, gravity
  for structure, microseismics for permeability, with the resolution study done
  first ([11-04-01 Geophysical Signatures of Geothermal Reservoirs](../../11-exploration-geophysics/04-geothermal-exploration-geophysics/01-geothermal-signatures.md)).
- **Mineral exploration.** Gravity plus magnetics plus EM over a target, where the
  potential-field ambiguity is only resolved by the EM conductance and the
  drilling.
- **Groundwater and contamination.** ERT, EM and borehole logs combined to
  separate salinity (conductive) from clay (conductive) — the classic case where a
  second method is *required* to break a petrophysical ambiguity, and where a
  wrong choice of second method buys nothing
  ([09-05-05 EM for Contaminant Plumes, Salinity and Leachate](../../09-electrical-em-methods/05-em-methods-applications/05-em-environmental.md)).
- **Any report.** The feasible-set language of this lesson is the honest form of
  an interpretation and should replace the phrases "the model shows" and "the
  data indicate".

## 11. Further reading

- **Lines, L. R., Schultz, A. K. & Treitel, S. (1988). Cooperative inversion of
  geophysical data. *Geophysics*, 53(1), 8–20.** Level: advanced. The paper that
  framed multi-method integration as a joint feasible set.
- **Gallardo, L. A. & Meju, M. A. (2003). Characterization of heterogeneous
  near-surface materials by joint 2D inversion of DC resistivity and seismic
  data. *Geophysical Research Letters*, 30(13), 1658.** Level: advanced. A worked
  structural (cross-gradient) coupling.
- **Parker, R. L. (1994). *Geophysical Inverse Theory*. Princeton University
  Press.** Chapters 2 and 6. Level: graduate. The rigorous treatment of null
  spaces and equivalence classes that §3.1–3.3 demonstrates.
- **Tarantola, A. (2005). *Inverse Problem Theory and Methods for Model Parameter
  Estimation*. SIAM.** Chapters 1–3. Level: graduate. The probabilistic account of
  feasible sets and what a measurement can and cannot add.
- **Zhdanov, M. S. (2015). *Inverse Theory and Applications in Geophysics*
  (2nd ed.). Elsevier.** Chapters on joint inversion. Level: graduate. A modern
  survey of joint inversion formulations and their pitfalls.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 12. Related lessons

- [05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core](./04-ground-truthing.md)
  — the prediction test of §3.6, carried out with real measurements.
- [05-07-05 Reporting Geophysical Results with Honest Uncertainty](./05-reporting-results.md)
  — how to write a feasible set into a report.
- [05-07-06 Common Interpretation Pitfalls and False Positives](./06-interpretation-pitfalls.md)
  — the false-positive statistics behind the 1 per cent tolerance used here.
- [18-07-05 Pitfalls: Inconsistent Physics, Weighting, Over-Coupling](../../18-inverse-problems/07-joint-and-multi-physics-inversion/05-joint-inversion-pitfalls.md)
  — the failure modes of joint inversion in general.
- [02-08-06 Uniqueness Theorems and Boundary Conditions](../../02-physics/08-potential-theory/06-uniqueness-theorems.md)
  — the theorem and the construction behind §3.1.

## Self-assessment checklist

- [ ] I can state the two conditions under which a second dataset constrains a
      model, and give a counterexample to each. (§1)
- [ ] I can compute and interpret a feasible set from a grid search. (§2.1, §4.1)
- [ ] I can derive conductance equivalence from the thin-sheet boundary
      condition and state its regime of validity. (§3.2)
- [ ] I can distinguish ambiguity from insensitivity with measured numbers.
      (§4.2)
- [ ] I can detect and report a conflict between two datasets, including the
      misfit ratio. (§3.5)
- [ ] I can run a prediction test and state what a failure means. (§3.6)
- [ ] I can check conductance, apparent resistivity and skin depth for
      dimensional consistency. (§6)
- [ ] I can explain why a resolution study belongs in the survey plan. (§1, §10)
