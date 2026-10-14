---
id: 25-03-02
title: "Project: ERT Inversion with Resolution Assessment"
level: advanced
prereqs: ["25-02-04", "09-02-07", "18-02-04", "18-03-03"]
estimated_minutes: 180
tags: [projects, resistivity, inversion, resolution, equivalence, teaching]
---

# Project: ERT Inversion with Resolution Assessment

## Learning objectives

By the end of this project you will be able to:

1. **Compute** a Wenner apparent-resistivity sounding over a layered earth from
   the image series, and **state** the reflectance and its limits.
2. **Invert** the sounding for layer resistivities and thickness in
   log-parameters, and **report** the misfit against the number of degrees of
   freedom.
3. **Derive** the linearised parameter covariance from the Jacobian and **read**
   the correlation matrix as a statement of which parameters are separable.
4. **Measure** the equivalence class by profile likelihood, and **compare** it
   with the linearised interval.
5. **Quantify** the depth of investigation from the model's sensitivity to the
   deepest parameter, and **state** the depth beyond which the sounding is
   extrapolating.
6. **Explain** why a $+15.5\%$ error in the half-space resistivity coexists with
   a $\chi^2$ of $1.07$ per datum and is therefore not a failure of the inversion.
7. **Report** an inverted model as a trade-off curve plus a depth of
   investigation, rather than as a table of best-fit numbers.

All data in this project are **SYNTHETIC**: a two-layer sounding generated from
chosen resistivities with chosen noise by
[`code/ert_inversion_demo.py`](./code/ert_inversion_demo.py). Real resistivity
data are acquired in the field and are usually proprietary to the client; nothing
here is measured.

## Prerequisites

- [25-02-04 Project: Interpreting a Refraction Survey](../02-intermediate-projects/04-refraction-interpretation.md) —
  the same "which layer is invisible" question in the seismic domain.
- [09-02-07 Resistivity Inversion: Smoothness, Robustness, Constraints](../../09-electrical-em-methods/02-dc-resistivity/07-resistivity-inversion.md) —
  the algorithm being applied, and why it is regularised in practice.
- [18-02-04 SVD Analysis: Model Resolution and Data Importance](../../18-inverse-problems/02-linear-inverse-problems/04-svd-analysis-inverse.md) —
  the resolution matrix and its diagonal.
- [18-03-03 Choosing the Trade-Off: L-Curve, GCV, Discrepancy Principle](../../18-inverse-problems/03-regularization/03-parameter-choice.md) —
  what changes when a smoothing penalty is added.

## 1. The question

*What can this sounding resolve, and what does it merely accommodate?*

Resistivity inversion is a first-kind problem: the data are the potential
differences, the model is the conductivity structure, and the mapping is
smoothed by the physics. A least-squares inversion of a two-layer
sounding will always produce numbers, and the numbers will always fit the data,
so the fitted values are not a result. The result is the **set** of models that
fit equally well, and it is large: the demonstration's half-space resistivity is
recovered as $1155\ \Omega\,\mathrm{m}$ against a true
$1000\ \Omega\,\mathrm{m}$ — a $+15.5\%$ error at a misfit of $1.07$ per datum.
Nothing is broken; the data simply do not determine that parameter to better than
about $11\%$.

## 2. The data

**Synthetic sounding (SYNTHETIC).** A two-layer earth with
$\rho_1 = 100\ \Omega\,\mathrm{m}$,
$\rho_2 = 1000\ \Omega\,\mathrm{m}$ and $h = 10.0\ \mathrm{m}$, measured with a
Wenner array at 25 spacings from 1.0 to 60.0 m, with $3\%$ relative plus
$1\ \Omega\,\mathrm{m}$ absolute noise. The forward model is the two-layer image
series

$$\rho_a(a) = 2\rho_1\!\left[F(a) - \tfrac{1}{2}F(2a)\right],
\qquad
F(r) = 1 + 2\sum_{n=1}^{\infty}
\frac{k^{n}}{\sqrt{1 + (2nh/r)^{2}}},
\qquad
k = \frac{\rho_2-\rho_1}{\rho_2+\rho_1}.$$

The reflectance is $k = 0.8182$, the curve runs from
$100.07\ \Omega\,\mathrm{m}$ at 1 m to $483.29\ \Omega\,\mathrm{m}$ at 60 m, and
it approaches but never reaches $\rho_2$ — the first hint of the equivalence in
§5.

**Provenance.** SYNTHETIC. The model is a chosen two-layer structure, the noise
is Gaussian by construction, and no field measurement is used.

## 3. The project specification

**Steps.**

1. Compute the forward sounding on a log-spaced set of spacings and add the
   stated noise; record the noise model, because it defines $\chi^2$.
2. Invert for $\log\rho_1$, $\log\rho_2$ and $\log h$ by unregularised
   least squares, and report $\chi^2$ against $n_\text{data} - n_\text{par}$.
3. Compute the Jacobian at the solution and the linearised covariance
   $\hat\sigma^{2}(J^{\mathsf T}J)^{-1}$, with
   $\hat\sigma^{2} = \chi^{2}/(n-m)$; report each parameter's relative
   uncertainty and the full correlation matrix.
4. Profile-likelihood the thickness: fix $h$ on a grid, re-optimise the other two
   parameters, and plot the resulting $\chi^{2}(h)$; report the $h$ and
   $\rho_2$ ranges with $\chi^{2} \le \chi^{2}_{\min} + 1$.
5. Quantify the depth of investigation from the sensitivity of $\rho_a$ to the
   deepest parameter as a function of spacing.
6. Write the report: the fitted model, the misfit, the trade-off curve, the
   depth of investigation, and the statement that a model without a resolution
   assessment is not a result.

**Deliverable.** The sounding curve with the fitted response, the trade-off table
($h$ against the $\rho_2$ that fits it), the correlation matrix and the
depth-of-investigation calculation.

**Success criterion.** The misfit is quoted per datum; each parameter has an
uncertainty; the trade-off between $\rho_2$ and $h$ is measured rather than
asserted; the depth beyond which the model is extrapolation is stated.

## 4. Inversion and misfit

Fitting in log-parameters keeps all three physical quantities positive and
makes the uncertainty in the resistivities *relative*, which is the natural
currency for a quantity spanning orders of magnitude. The unregularised fit
gives

| parameter | fitted | true | error | relative 1σ (linearised) |
|---|---|---|---|---|
| $\rho_1$ | $100.367\ \Omega\,\mathrm{m}$ | $100$ | $+0.37\%$ | $1.43\%$ |
| $\rho_2$ | $1155.38\ \Omega\,\mathrm{m}$ | $1000$ | $+15.54\%$ | $11.42\%$ |
| $h$ | $10.5558\ \mathrm{m}$ | $10.0$ | $+5.56\%$ | $4.20\%$ |

with $\chi^{2} = 28.631$ for 25 data and 3 parameters, i.e. $1.07$ per degree of
freedom ($22$ dof). **The $\rho_2$ error is only $1.36\sigma$** — a good fit and a
poorly determined parameter are entirely compatible, and the uncertainty column
is what says so.

## 5. Resolution: three measurements of the same thing

**(a) The correlation matrix.**

| | $\rho_1$ | $\rho_2$ | $h$ |
|---|---|---|---|
| $\rho_1$ | $+1.000$ | $+0.224$ | $+0.584$ |
| $\rho_2$ | $+0.224$ | $+1.000$ | $+0.834$ |
| $h$ | $+0.584$ | $+0.834$ | $+1.000$ |

$\rho_2$ and $h$ are correlated at $+0.834$: **they rise and fall together**, so
the data determine a combination rather than the two separately. This is the
**equivalence** of resistivity sounding — a conductivity-thickness product rather
than a unique pair — and it is the reason an unregularised two-layer fit is
well-posed only in the sense that it has a unique *minimum*, not a unique
*answer*.

**(b) The profile likelihood.** Fixing $h$ and re-optimising the other two:

| $h$ (m) | $\chi^2$ | $\rho_2$ that fits ($\Omega\,\mathrm{m}$) |
|---|---|---|
| 8.00 | $87.654$ | $721.1$ |
| 9.25 | $41.974$ | $893.6$ |
| 10.50 | $28.652$ | $1141.7$ |
| 11.75 | $37.226$ | $1531.7$ |
| 13.00 | $60.622$ | $2233.8$ |

The $\chi^{2} \le \chi^{2}_{\min}+1$ interval is $h = 10.20$–$10.90\ \mathrm{m}$,
i.e. $\pm 0.35\ \mathrm{m}$, against the linearised $\pm 0.44\ \mathrm{m}$. The
profile interval is **$21\%$ narrower**, which is the standard signature of a
mildly non-quadratic misfit surface; the linearised interval is the conservative
of the two. The corresponding $\rho_2$ range is $1073$–$1246\
\Omega\,\mathrm{m}$, so the honest statement is
$\rho_2 = 1150^{+100}_{-80}\ \Omega\,\mathrm{m}$ **with $h$ traded against it**,
not a single value.

**(c) Depth of investigation.** The sensitivity of $\rho_a$ to $\rho_2$ reaches
half its maximum at $a = 36.68\ \mathrm{m}$; with the Wenner median
depth-of-investigation rule of roughly $a/2$, that is about
$18.3\ \mathrm{m}$. The longest spacing (60 m) probes to about 30 m. A 10 m layer
is comfortably inside that, which is why it is resolved at $4\%$; a 30 m layer
would not be, and the fit would report a thickness driven by the regularisation
or the starting model rather than by the data.

## 6. Why the answer is a curve, not a table

The three measurements agree and say the same thing in different currencies: the
correlation says the degeneracy exists, the profile likelihood says how far it
extends, and the depth of investigation says where it stops being constrained at
all. A report that gives only the best-fit row of §4 tells the reader that $\rho_2$
is $1155\ \Omega\,\mathrm{m}$, which is true, uninformative and misleading: the
same data are fit by $721\ \Omega\,\mathrm{m}$ at 8 m and by $2234\
\Omega\,\mathrm{m}$ at 13 m, both outside the $\Delta\chi^{2}=1$ contour but
inside $\Delta\chi^{2}=4$. Quoting the trade-off curve costs one table and removes
the ambiguity.

## 7. Failure modes and how to detect them

1. **Reporting the best fit as the answer.** *Detect:* add the $\Delta\chi^{2}=1$
   ranges; the $+15.5\%$ $\rho_2$ error at a $\chi^2$ of $1.07$ per datum is the
   demonstration.
2. **A misfit quoted without degrees of freedom.** *Detect:* $\chi^{2}$/dof here is
   $28.631/22 = 1.30$; quoted per datum it is $1.07$. State which.
3. **Reading the linearised interval as exact.** *Detect:* compare it with the
   profile interval ($\pm 0.44$ against $\pm 0.35\ \mathrm{m}$).
4. **Ignoring the depth of investigation.** *Detect:* a model parameter whose
   sensitivity never reaches half its maximum on the observed spacings is not
   determined by the data at all.
5. **A regularised inversion reported without its penalty.** *Detect:* rerun with
   two different penalties; if the layer boundary moves by more than the
   linearised uncertainty, the penalty is controlling the answer.

## 8. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Forward | Image series, reflectance, spacing range stated | Curve computed | Curve from a table | None |
| Inversion | Log-parameters, $\chi^2$/dof, residuals reported | Fit | Values | Not inverted |
| Uncertainties | Linearised plus profile likelihood, compared | Linearised | Stated | Absent |
| Trade-off | Curve of $h$ against $\rho_2$ with the accepted range | Correlation quoted | Mentioned | Absent |
| DOI | Sensitivity-based, in metres, with the rule cited | Stated | Qualitative | Absent |

## 9. Assumptions and regime of validity

1. **One-dimensional layering.** A dipping interface, a lateral change or
   topography makes the sounding a weighted average of a 2-D structure; the
   residual pattern is the only warning.
2. **Isotropic resistivity.** Anisotropy in a layered sequence is indistinguishable
   from a different layer thickness in a 1-D sounding.
3. **The noise model is correct.** $\chi^{2}$ is only a misfit per datum until the
   noise model is defensible; a wrong $\sigma$ makes the misfit meaningless while
   leaving the trade-off shape intact.
4. **No induced polarisation.** A polarisable ground makes $\rho_a$ complex and a
   real-only inversion biased.
5. **The image series has converged.** With $N_\text{terms} = 60$ and
   $|k| = 0.82$, the neglected remainder is of order $k^{60} \sim 10^{-6}$ —
   negligible here but not at $|k| \to 1$.

## The honest summary

A two-layer sounding with $3\%$ noise, inverted without regularisation, recovers
$\rho_1$ to $1.4\%$, $h$ to $4.2\%$ and $\rho_2$ to $11.4\%$, at a misfit of
$1.07$ per datum — and the $\rho_2$ error is only $1.36\sigma$, so the
inversion is behaving correctly. The parameter pair $(\rho_2, h)$ is correlated
at $+0.834$; the $\Delta\chi^{2}=1$ contour spans $h = 10.20$–$10.90\ \mathrm{m}$
and $\rho_2 = 1073$–$1246\ \Omega\,\mathrm{m}$; and the sensitivity-based depth of
investigation is about $18\ \mathrm{m}$. The transferable result is that the
deliverable of a resistivity inversion is the **trade-off curve and the depth of
investigation**, and the best-fit numbers are a by-product of both.

## Python demonstration

[`code/ert_inversion_demo.py`](./code/ert_inversion_demo.py) prints every number
quoted above. It:

1. prints the two-layer forward curve at five spacings with its noise level;
2. inverts for the three log-parameters and prints the fitted values, the
   percentage errors and $\chi^{2} = 28.631$ for 25 data;
3. prints the linearised relative uncertainties ($1.43\%$, $11.42\%$, $4.20\%$)
   and the full correlation matrix including $\mathrm{corr}(\rho_2,h) = +0.834$;
4. profiles $\chi^{2}$ over $h$ on a 101-point grid and prints the
   $\Delta\chi^{2}=1$ ranges for $h$ and $\rho_2$, plus the sensitivity-based
   depth of investigation ($36.68\ \mathrm{m}$ spacing, $\approx 18.3\ \mathrm{m}$).

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/03-advanced-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ert_inversion_demo.py
```

The script prints only, writes no files, uses no network and exits 0. It runs in
under a second (SciPy's `least_squares` on a three-parameter problem).

## Exercises

Graded problems and worked solutions are in
[`exercises/02-ert-inversion-project-exercises.md`](./exercises/02-ert-inversion-project-exercises.md)
and
[`exercises/02-ert-inversion-project-solutions.md`](./exercises/02-ert-inversion-project-solutions.md).
The ★★★ item asks you to design an acquisition that resolves a specified layer,
not to re-run the fit.

## Mastery checkpoint

Without notes:

1. State the reflectance $k$ and the two limits of $\rho_a$ at very short and very
   long spacing.
2. A fit gives $\chi^{2} = 40$ for 30 data and 4 parameters. State the misfit per
   datum and per degree of freedom, and say which belongs in a report.
3. The correlation between $\rho_2$ and $h$ is $+0.83$. State in one sentence what
   an equally good fit with a larger $h$ implies for $\rho_2$.
4. A colleague reports $\rho_2 = 1155 \pm 130\ \Omega\,\mathrm{m}$ from this
   dataset. Name the one thing missing from the report.

## Common pitfalls

1. **Treating a good misfit as a determined model.** $1.07$ per datum coexists
   with an $11\%$ parameter uncertainty.
2. **Quoting a resistivity without a depth of investigation.** Below the DOI the
   inversion is extrapolating.
3. **Averaging away the trade-off by quoting a single best fit.** Report the
   curve.
4. **Forgetting that regularisation, not data, sets the layer boundary.** The
   unregularised fit is the honest starting point for the resolution question.
5. **Ignoring the noise model.** $3\%$ relative and $1\ \Omega\,\mathrm{m}$
   absolute are different regimes at different spacings.

## Where this is used

The same three resolution measurements structure every geophysical inversion that
follows: the linearised covariance of
[25-03-06](./06-gravity-inversion-uq.md), the profile likelihood of
[25-05-04](../05-doctoral-projects/04-bayesian-inversion-project.md), and the
sensitivity-based depth of investigation that appears in field reports as the
"confidence depth". In professional practice a resistivity survey is commissioned
for a target depth, and the DOI calculation of §5(c) is what tells the client
whether that depth is achievable before the survey is paid for.

## Related lessons

- [09-02-05 Electrical Resistivity Tomography (ERT) Acquisition and Design](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md) —
  the array design that sets the DOI before any inversion.
- [09-02-02 Electrode Arrays: Wenner, Schlumberger, Dipole-Dipole, Pole-Dipole](../../09-electrical-em-methods/02-dc-resistivity/02-electrode-arrays.md) —
  how the array changes the sensitivity kernel.
- [18-02-05 Resolution and Information Matrices in Interpretation](../../18-inverse-problems/02-linear-inverse-problems/05-resolution-matrices.md) —
  the resolution matrix behind §5.
- [25-05-01 Project: Local Earthquake Tomography with Resolution Tests](../05-doctoral-projects/01-tomography-project.md) —
  the same resolution assessment in three dimensions.

## Self-assessment checklist

- [ ] I can write the two-layer Wenner forward model and check its limits.
- [ ] I can invert a sounding in log-parameters and report $\chi^2$/dof.
- [ ] I can compute a linearised covariance and read a correlation matrix.
- [ ] I can profile-likelihood a parameter and compare intervals.
- [ ] I can estimate a sensitivity-based depth of investigation.
- [ ] I can state why the deliverable is a trade-off curve.
