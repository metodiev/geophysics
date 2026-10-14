---
id: 25-03-06
title: "Project: Gravity Inversion with Uncertainty Quantification"
level: advanced
prereqs: ["25-02-02", "18-02-04", "18-03-02", "18-03-03"]
estimated_minutes: 180
tags: [projects, gravity, inversion, uncertainty, resolution, teaching]
---

# Project: Gravity Inversion with Uncertainty Quantification

## Learning objectives

1. **Build** the gravity kernel of a discretised 2-D density model and **state** the
 discretisation's units and its limitations.
2. **Solve** the Tikhonov-regularised inverse problem and **choose** the regularisation
 parameter by the discrepancy principle.
3. **Compute** the posterior model covariance and **derive** the resolution matrix from it.
4. **Report** the effective number of resolved parameters (the trace of the resolution matrix)
 rather than the number of parameters.
5. **Quantify** the equivalence class by sampling the posterior, and **compare** the data spread
 it predicts with the data noise.
6. **State** why a mean parameter uncertainty of $15.09\ \mathrm{kg\,m^{-3}}$ coexists with a
 mean model error of $24.43\ \mathrm{kg\,m^{-3}}$, and which of the two belongs in a report.

## Prerequisites

- [25-02-02 Project: Gravity Anomaly of Simple Bodies](../02-intermediate-projects/02-simple-gravity-model.md) —
  the non-uniqueness this project quantifies rather than states.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../../18-inverse-problems/02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  resolution and data importance as spectral quantities.
- [18-03-02 Tikhonov Regularisation and the Smoothing Trade-Off](../../18-inverse-problems/03-regularization/02-tikhonov.md) —
  the estimator, its filter factors and its bias.
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../../18-inverse-problems/03-regularization/03-parameter-choice.md) —
  the rule used to pick $\alpha$.

## 1. The question

*What does this anomaly determine about the density structure, and what is merely
consistent with it?*

Gravity inversion is the textbook ill-posed problem, and the honest deliverable is
not a density section but three statements: an estimate, a resolution, and the
size of the set of models that fit equally well. The demonstration's numbers make
the point sharply: the inversion resolves **21.42 of 32 parameters**, its mean
parameter uncertainty is $15.09\ \mathrm{kg\,m^{-3}}$, and the actual mean model
error is $24.43\ \mathrm{kg\,m^{-3}}$ — the error bar understates the error because
it does not include the regularisation bias.

## 2. The data

**Synthetic model and data (SYNTHETIC).** Eight blocks of $6.25\ \mathrm{km}$ width
and four depth layers with boundaries at 0, 1, 3, 6 and 10 km — **32 parameters** —
observed as vertical gravity at 25 stations every $2\ \mathrm{km}$ along a profile
from $-25$ to $+25\ \mathrm{km}$. The true model has
$+300\ \mathrm{kg\,m^{-3}}$ in blocks 2–4 of layer 1 and
$-250\ \mathrm{kg\,m^{-3}}$ in blocks 2–3 of layer 3. Data noise is
$0.05\ \mathrm{mGal}$; the resulting anomaly ranges from $-11.173$ to
$+23.589\ \mathrm{mGal}$, and the largest kernel entry is
$0.0672\ \mathrm{mGal}$ per $\mathrm{kg\,m^{-3}}$.

**Provenance.** SYNTHETIC. The block model is a discretisation choice, not a
geology; the data are exact forward computations plus Gaussian noise.

## 3. The project specification

**Steps.**

1. Define the model grid and **count** the parameters against the data: here
   32 against 25, an under-determined problem by construction.
2. Build the kernel $A$ with $A_{ji} = \partial g_j/\partial\rho_i$ by quadrature
   over each block, and verify its magnitude against a hand calculation for one
   block.
3. Solve $(A^{\mathsf T}W_d A + \alpha L^{\mathsf T}L)\,m = A^{\mathsf T}W_d d$
   for a range of $\alpha$, and choose $\alpha$ as the largest value whose
   $\chi^{2}/n$ is still $\le 1$ (the discrepancy principle).
4. Compute the posterior covariance
   $C_m = (A^{\mathsf T}W_dA + \alpha L^{\mathsf T}L)^{-1}$ and the resolution
   matrix $R = C_m A^{\mathsf T}W_d A$; report $\operatorname{tr}R$ and the
   per-layer diagonal.
5. Draw 2000 models from $\mathcal N(m, C_m)$, and report (i) the parameter spread
   per layer, (ii) the spread of the **predicted data**, and (iii) the fraction of
   draws that contradict the sign of the true body.
6. Write the report: the estimate, the resolution trace, the uncertainty, the
   equivalence class, and the statement of what the data do not determine.

**Deliverable.** The kernel check, the $\alpha$ scan, the covariance and resolution
table, and the posterior ensemble statistics.

**Success criterion.** The regularisation parameter is chosen by a stated rule; the
resolution is reported as a trace and per layer; the uncertainty is compared with
the actual error; the equivalence class is measured, not described.

## 4. The forward kernel

The vertical gravity of a 2-D body of density contrast $\Delta\rho$ is

$$g_z(x) = 2G\Delta\rho \iint_{\text{body}}
\frac{z'}{(x-x')^{2}+z'^{2}}\,\mathrm{d}x'\,\mathrm{d}z',$$

so the kernel element for block $i$ is the integral over that block, evaluated by
Gauss–Legendre quadrature. Two checks belong in the deliverable: the units
($\mathrm{mGal}$ per $\mathrm{kg\,m^{-3}}$), and an order-of-magnitude estimate for
one block,

$$g \approx \frac{2G\Delta\rho A}{d}
= \frac{2 \times 6.6743\times10^{-11} \times 1 \times 6.25\times10^{6}}
{2.5\times10^{3}}
= 3.337\times10^{-7}\ \mathrm{m\,s^{-2}} = 0.0334\ \mathrm{mGal}$$

per $\mathrm{kg\,m^{-3}}$ for a $6.25\ \mathrm{km}\times1\ \mathrm{km}$ block at
$2.5\ \mathrm{km}$ depth. The computed maximum kernel entry, $0.0672\ \mathrm{mGal}$
per $\mathrm{kg\,m^{-3}}$, is twice as large because it belongs to a shallower block
whose contribution falls off as $1/r$ rather than as the crude $1/d$ of this
estimate — a factor-two agreement from a one-line calculation is exactly what a
kernel check is for.

The unregularised normal matrix has a condition number of $3.4\times10^{17}$:
numerically singular, and physically so, because a deep block and a shallower
broader block produce nearly the same surface field.

## 5. Choosing the smoothing parameter

| $\alpha$ | $\chi^{2}/n$ | model rms ($\mathrm{kg\,m^{-3}}$) |
|---|---|---|
| $10^{-6}$ | $0.0001$ | $93.38$ |
| $10^{-4}$ | $0.1978$ | $89.08$ |
| $3.16\times10^{-4}$ | $0.8641$ | $85.39$ |
| $10^{-3}$ | $2.8044$ | $81.11$ |
| $10^{-2}$ | $27.3837$ | $69.70$ |
| $10^{-1}$ | $149.0883$ | $58.16$ |

The chosen value is $\alpha = 3.16\times10^{-4}$, the largest with
$\chi^{2}/n \le 1$. The choice matters: at $10^{-6}$ the inversion fits the noise
($\chi^{2}/n = 0.0001$, far below 1, i.e. over-fitting), and at $10^{-2}$ it
under-fits by a factor of 27. **The discrepancy principle is not a formality — it
is the difference between explaining the data and explaining the data's noise.**

## 6. Covariance, resolution and the resolved count

$$C_m = \left(A^{\mathsf T}W_dA + \alpha L^{\mathsf T}L\right)^{-1},
\qquad
R = C_m\,A^{\mathsf T}W_d A.$$

| layer | mean 1σ ($\mathrm{kg\,m^{-3}}$) | mean $\lvert$error$\rvert$ | mean resolution |
|---|---|---|---|
| 1 (0–1 km) | $17.23$ | $64.62$ | $0.612$ |
| 2 (1–3 km) | $15.30$ | $17.97$ | $0.656$ |
| 3 (3–6 km) | $14.28$ | $8.26$ | $0.665$ |
| 4 (6–10 km) | $13.54$ | $6.86$ | $0.745$ |

$$\operatorname{tr}R = 21.42\ \text{of}\ 32, \qquad
\overline{\sigma}_m = 15.09\ \mathrm{kg\,m^{-3}}, \qquad
\overline{|m-m_\text{true}|} = 24.43\ \mathrm{kg\,m^{-3}}.$$

Three results, each of which contradicts a common expectation.

1. **Resolution is not simply "worse with depth".** It *rises* with depth here
   ($0.612 \to 0.745$) because the deeper layers are **thicker**: a thick layer is
   well determined as an average, while two thin shallow layers trade against each
   other. Resolution is a property of the parameterisation as much as of the
   physics, and the honest headline is the trace, $21.42/32$, with the per-layer
   profile beside it.
2. **The mean uncertainty understates the mean error** by a factor of $1.6$
   ($15.09$ against $24.43$). The covariance measures the *random* propagation of
   the data noise through the estimator; the actual error also contains the
   regularisation **bias**, which no covariance term includes. A report that quotes
   only $\sigma_m$ is quoting the smaller of two numbers.
3. **A third of the parameter space is unresolved** — $10.6$ of $32$ parameters'
   worth — and those directions are exactly the deep, long-wavelength combinations
   that gravity cannot see.

## 7. The equivalence class

Drawing 2000 models from $\mathcal N(m, C_m)$:

| quantity | value |
|---|---|
| shallow body (blocks 2–4, true $+300$) | spread $19.04\ \mathrm{kg\,m^{-3}}$ |
| deep body (blocks 2–3 of layer 3, true $-250$) | spread $21.08\ \mathrm{kg\,m^{-3}}$ |
| rms spread of the **predicted data** | $0.0459\ \mathrm{mGal}$ (noise $0.05$) |
| draws in which the deep body is **positive** | $16.8\%$ |
| draws in which the deep body is more negative than $-100$ | $0.0\%$ |

The predicted-data spread being *smaller* than the noise is the definition of an
equivalence class: these models are indistinguishable **at the data's own
precision**. And the $16.8\%$ figure is the result that matters for interpretation
— roughly one draw in six of a defensible posterior says the deep body has the
**opposite sign** to the truth, which no single best-fit section would ever reveal.

Note what the class does *not* contain: $0\%$ of draws place the deep body more
negatively than $-100\ \mathrm{kg\,m^{-3}}$, so the *existence* of a negative
density contrast there is well supported even though its magnitude is not. The
distinction between "the sign is determined" and "the amplitude is not" is the
most useful sentence an inversion report can contain.

## 8. Failure modes and how to detect them

1. **A density section with no resolution statement.** *Detect:* compute
   $\operatorname{tr}R$; here it is $21.42$ of $32$.
2. **A covariance quoted as the total uncertainty.** *Detect:* compare the mean
   $\sigma_m$ with the actual error; here $15.09$ against $24.43$, a factor $1.6$.
3. **A regularisation parameter chosen by taste.** *Detect:* report the
   $\chi^{2}/n$ at the chosen $\alpha$; $0.86$ here, against $0.0001$ and $27.4$
   at neighbouring values.
4. **A grid finer than the data can resolve.** *Detect:* the condition number and
   the trace of $R$; refining the grid without new data reduces
   $\operatorname{tr}R/\!\!\text{parameters}$ and does not add information.
5. **Assuming the posterior is Gaussian and unimodal.** *Detect:* in a linear
   problem with a Gaussian prior the covariance is exact; the moment the problem
   becomes non-linear (a bound, an interface, a sparse prior) the equivalence class
   is not an ellipsoid and must be sampled, not diagonalised.
6. **Reading the resolved count as a data count.** $\operatorname{tr}R$ counts
   *parameters*, and each unit of it corresponds to one well-determined direction
   in model space, not to one data point.

## 9. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Kernel | Built, unit-checked, magnitude verified | Built | From a library | Not built |
| Regularisation | $\alpha$ by the discrepancy principle with the $\chi^2$ scan | $\alpha$ stated | Trial and error | None |
| Covariance | $C_m$ and $R$ computed and interpreted | $C_m$ | Stated | Absent |
| Resolution | Trace plus per-layer profile | Trace | Mentioned | Absent |
| Equivalence class | Posterior sampled, predicted-data spread quoted | Uncertainty quoted | Qualitative | Absent |

## 10. Assumptions and regime of validity

1. **Two-dimensional, uniform-density blocks.** Three-dimensional bodies need a
   different kernel; a density that varies within a block is not representable.
2. **A Gaussian data error.** $W_d = \sigma^{-2}I$ assumes independent, equal
   errors; correlated errors make both the estimate and its covariance wrong.
3. **A Gaussian, smoothness-type prior.** $L^{\mathsf T}L$ asserts that
   neighbouring densities are similar — a model choice, and the resolution and the
   equivalence class are conditional on it.
4. **A linear forward model.** Gravity of a fixed grid *is* linear in $\Delta\rho$,
   which is why the covariances here are exact; introduce a free interface position
   or a bound and that ends.
5. **A flat Earth over the profile.** At a 50 km aperture negligible; at 500 km it
   is not.

## The honest summary

The project's output is four numbers and a caveat. $\chi^{2}/n = 0.864$ at
$\alpha = 3.16\times10^{-4}$ chosen by the discrepancy principle;
$\operatorname{tr}R = 21.42$ of $32$ resolved parameters; a mean parameter
uncertainty of $15.09\ \mathrm{kg\,m^{-3}}$ against a mean model error of
$24.43\ \mathrm{kg\,m^{-3}}$; and a posterior ensemble whose predicted data spread
($0.0459\ \mathrm{mGal}$) is below the data noise ($0.05\ \mathrm{mGal}$) while
$16.8\%$ of its members give the deep body the wrong sign. The transferable result
is that **an inversion is a probability statement about a set of models**, and the
best-fit section is a summary of that set that deliberately hides its size.

## Python demonstration

[`code/gravity_inversion_uq.py`](./code/gravity_inversion_uq.py) prints every number quoted above, writes no files,
uses no network and exits 0:

```bash
cd 25-projects-capstone/03-advanced-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gravity_inversion_uq.py
```

It is seeded with `np.random.default_rng(20261014)` and runs in under a second.
## Exercises

Graded problems and worked solutions are in
[`exercises/06-gravity-inversion-uq-exercises.md`](./exercises/06-gravity-inversion-uq-exercises.md)
and
[`exercises/06-gravity-inversion-uq-solutions.md`](./exercises/06-gravity-inversion-uq-solutions.md).
The ★★★ item asks you to design an experiment that reduces the unresolved
directions, not to rerun the inversion.

## Mastery checkpoint

Without notes:

1. Write the 2-D gravity kernel and state its unit per unit density contrast.
2. State the discrepancy principle and what it assumes about the noise.
3. A model has 40 parameters, 30 data and $\operatorname{tr}R = 12$. State what
   that means and what it does not mean.
4. The mean parameter uncertainty is $15\ \mathrm{kg\,m^{-3}}$ and the mean actual
   error is $24\ \mathrm{kg\,m^{-3}}$. Name the missing term.

## Common pitfalls

1. **Quoting a formal error from an over-parameterised, barely regularised inversion.** The damping choice must come from the data.
2. **Reporting a depth and an amplitude without their correlation.** Gravity inversion trades mass against depth, and the trade-off must be quoted.
3. **Ignoring the reference model.** The density contrast and the datum are assumptions; the anomaly defines the product.
4. **Treating a resolution test as a precision statement.** A point-spread function is a bias and resolution statement, not a standard error.
5. **Presenting one posterior sample as the model.** The posterior's spread is the result, and one realisation is a picture.

## Where this is used

The same four-part deliverable appears in every quantitative inversion: the
tomographic resolution tests of
[25-05-01](../05-doctoral-projects/01-tomography-project.md), the Bayesian
equivalence classes of
[25-05-04](../05-doctoral-projects/04-bayesian-inversion-project.md), and the joint
inversion of [25-04-05](../04-graduate-projects/05-joint-inversion-project.md). In
professional practice a gravity inversion is commissioned to answer a question
about a *range* of densities — a resource tonnage, a cavity, a salt thickness — and
the equivalence class is the answer, with the best-fit model as its illustration.

## Related lessons

- [07-03-04 Gravity Inversion and Its Severe Non-Uniqueness](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/04-inversion-gravity.md) —
  the same problem without the probabilistic machinery.
- [18-05-01 Bayes' Theorem as an Inverse-Problem Formulation](../../18-inverse-problems/05-bayesian-inversion/01-bayes-inverse-formulation.md) —
  the framework behind $C_m$ and the posterior draws.
- [18-01-03 Null Space, Non-Uniqueness and Equivalence Classes](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md) —
  the deterministic statement of §7.
- [25-05-02 Project: A Small-Scale Full-Waveform Inversion](../05-doctoral-projects/02-full-waveform-inversion-project.md) —
  the same discipline for a non-linear problem.

## Self-assessment checklist

- [ ] I can build a gravity kernel and check its magnitude.
- [ ] I can choose $\alpha$ by the discrepancy principle.
- [ ] I can compute a posterior covariance and a resolution matrix.
- [ ] I can report a resolved-parameter count and interpret it.
- [ ] I can sample an equivalence class and measure its data spread.
- [ ] I can explain why the covariance understates the error.
