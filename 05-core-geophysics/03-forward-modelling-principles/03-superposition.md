---
id: 05-03-03
title: "Superposition and Building Complex Models"
level: intermediate
prereqs: ["05-03-01", "05-03-02"]
tags: [superposition, linearity, composite-models, kronecker]
---

# Superposition and Building Complex Models

## Learning objectives

1. **State** the superposition principle and the conditions under which each
   geophysical method obeys it.
2. **Build** an arbitrary body as a sum of simple bodies, and compute its field
   as a sum of fields.
3. **Use** the decomposition to isolate the effect of a single target or to
   subtract an unwanted contribution.
4. **Recognise** the cases where superposition fails, and quantify the
   consequences.
5. **Implement** superposition as a matrix operation and explain its
   computational structure.

## Prerequisites

- [05-03-01 The Forward Problem](./01-forward-problem.md)
- [05-03-02 Analytical Solutions for Simple Bodies](./02-analytical-solutions.md)

## 1. Intuition

Superposition is the reason simple bodies are not just tutorial exercises. Any
field that obeys a *linear* equation can be built from parts, so a complex
geology is a sum of simple pieces, and an interpretation can peel it apart
again. When superposition fails — magnetic saturation, non-linear seismic
amplitude, mutual interaction of sources — the whole analytical toolkit must be
replaced by a non-linear treatment.

## 2. Precise statement

If $F$ is linear, then for models $\mathbf{m}_1, \mathbf{m}_2$ and scalars
$\alpha, \beta$:

$$F[\alpha\mathbf{m}_1 + \beta\mathbf{m}_2] = \alpha F[\mathbf{m}_1] +
\beta F[\mathbf{m}_2].$$

Equivalently, $\mathbf{G}(\mathbf{m}_1+\mathbf{m}_2) =
\mathbf{G}\mathbf{m}_1+\mathbf{G}\mathbf{m}_2$: the field of a sum is the sum of
the fields.

**Which methods are linear?**

| Method | Linear in | Notes |
|---|---|---|
| Gravity | density | exact |
| Magnetics (induced) | magnetisation, if demagnetisation is neglected | approximate |
| Magnetics (total, with self-demagnetisation) | no | non-linear in susceptibility |
| DC resistivity | potential, for fixed conductivity | linear in potential; non-linear in conductivity |
| EM | fields, for fixed conductivity | as above |
| Seismic travel time | no | travel time is not additive along different paths in a useful way |
| Seismic amplitude | only for weak scattering | otherwise no |
| Thermal | temperature, for fixed conductivity | linear |

The subtle but crucial distinction is *linear in what*. Resistivity is linear in
the potential but non-linear in the conductivity, which is why resistivity
inversion is a non-linear problem even though the governing equation is linear.

## 3. Derivations

### 3.1 Composite prism model

A body of arbitrary shape is approximated by $N$ prisms. Its anomaly is

$$g_z(\mathbf{r}_i) = \sum_{j=1}^{N} g_z^{(j)}(\mathbf{r}_i; \mathbf{p}_j),
\qquad \mathbf{p}_j = (x_1,x_2,y_1,y_2,z_1,z_2,\Delta\rho)_j.$$

In matrix form, $\mathbf{d} = \mathbf{G}\mathbf{m}$ where column $j$ of
$\mathbf{G}$ is the anomaly of unit density in prism $j$. Building $\mathbf{G}$
once and re-using it is the standard efficiency trick: a model change is a
matrix–vector product.

### 3.2 Subtracting a nuisance effect

The anomaly of a target is often buried under a known field (a large regional
gradient, a neighbouring body, the attraction of the topographic slab). Because
$F$ is linear, that field can be computed for its own model and subtracted:

$$\mathbf{d}_\text{target} = \mathbf{d}_\text{observed} -
F[\mathbf{m}_\text{nuisance}].$$

The uncertainty propagates: $\sigma^2_\text{target} =
\sigma^2_\text{observed} + \sigma^2_\text{nuisance}$, so subtracting a poorly
known contribution makes things *worse*, not better.

### 3.3 Failure of superposition: demagnetisation

For a body of susceptibility $\chi$ in field $\mathbf{H}_0$, the internal field
is reduced by the body's own magnetisation: for a sphere,
$\mathbf{H}_\text{int} = \mathbf{H}_0 - \mathbf{M}/3$, giving an *effective*
susceptibility

$$\chi_\text{eff} = \frac{\chi}{1+\chi/3}.$$

This is non-linear in $\chi$: doubling $\chi$ does not double the anomaly. For
small $\chi$ it hardly matters; for $\chi \gtrsim 0.1$ it is essential. The
magnetisation of the sphere in a stated 50 000 nT field with $\chi = 0.5$ is
**not** $0.5\times H_0$ but the reduced value, and treating it as linear
overestimates the anomaly by the factor
$1+\chi/3 = 1.167$ for a sphere.

## 4. Units and dimensional analysis

| Quantity | Unit |
|---|---|
| prism anomaly $g_z^{(j)}$ | m s⁻², or mGal |
| kernel column unit density | m³ s⁻² kg⁻¹ per unit density |
| $\chi_\text{eff}$ | dimensionless (SI) |

## 5. Assumptions

1. **Linearity** of the governing equation *in the model parameter*, as above.
2. **No interaction between parts.** In magnetics, adjacent magnetic cells
   interact through their own fields — the demagnetisation effect made local.
3. **Additivity of noise.** Independent noise adds in quadrature; correlated
   noise does not.
4. **Fixed geometry.** Building $\mathbf{G}$ once assumes cell geometry does
   not change between iterations.

## 6. Worked examples

**6.1 A composite dyke.** Two prisms of the same density, offset laterally, sum
to a wider anomaly whose shape is the convolution of the single-prism shape with
the two-point geometry. Doubling the width doubles the amplitude at large depth
but the *shape* changes — amplitude and geometry are not separable.

**6.2 Subtracting the slab.** In the module demonstration, the readings contain
a free-air effect of $\pm2.397$ mGal and a slab effect of $\mp0.785$ mGal; both
are subtracted exactly, leaving a residual of 0.0212 mGal against a stated noise
of 0.02 mGal. If the Bouguer density were wrong by 670 kg/m³, the *subtraction*
would inject 0.157 mGal of spurious signal — larger than the target for a
subtle anomaly.

**6.3 Superposition in the non-uniqueness demonstration.** The parallel-conductance
model in Section 4 of `code/petrophysics_demo.py` adds an Archie conduction term
and a clay-conduction term. The two paths add (parallel conduction), so the
total conductivity is a superposition of independent mechanisms — and the
resulting inversion bias confirms that fitting one mechanism to two mechanisms'
data fails.

## 7. Python demonstration

Use `code/prism_gravity_demo.py` to obtain a single prism's anomaly, then sum
several prisms with a short script to build a step or a dipping body, and check
that the sum equals the anomaly of the union computed directly by quadrature.
The measured agreement is the test that superposition is implemented correctly.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/03-superposition-exercises.md`](./exercises/03-superposition-exercises.md).

**Common mistakes.** (1) Assuming magnetic linearity with high susceptibility.
(2) Subtracting a model contribution as though it were noise-free. (3) Thinking
superposition lets you separate a sum uniquely — it does not; that is the
inverse problem. (4) Using 2-D solutions for 3-D bodies and adding them as if
both were valid. (5) Rebuilding $\mathbf{G}$ on every iteration.

**Applications.** Regional–residual separation; terrain correction (summing the
effects of topographic elements); building arbitrary bodies from prisms or
polygons; joint inversion, where the total data vector is the concatenation of
several physics operators applied to shared parameters.

## Extended worked example: superposition inside a reduction chain

The reduction sequence of
[05-02-04](../02-geophysical-fields-and-observables/04-reduction-of-observations.md)
is an exercise in superposition, and the module demonstration lets it be checked
numerically. The synthetic survey has relief from $-8$ to $+8$ m relative to the
base station, a Bouguer density of 2400 kg/m³, a target anomaly of 4.0 mGal, a
drift of 0.05 mGal/h, a tide of 0.15 mGal amplitude and reading noise of 0.02
mGal.

**Each contribution is computed separately, then summed** — that is
superposition applied to the *forward* direction:

| contribution | range (mGal) |
|---|---|
| free-air effect on the readings | $-2.397$ to $+2.397$ |
| Bouguer slab effect | $-0.785$ to $+0.785$ |
| drift over 4 h | 0 to 0.20 |
| tide | $-0.15$ to $+0.15$ |
| target anomaly | 0 to 4.0 |
| noise ($\sigma$) | 0.02 |

The raw readings depart from the truth by 0.2324 mGal RMS with a largest single
error of 0.3623 mGal — the contamination exceeds the target, and the elevation
terms alone are larger than the anomaly.

**Then each contribution is subtracted** — superposition applied in the
*inverse* direction. After drift and tide removal the RMS departure is 0.0212
mGal; after the free-air and Bouguer corrections it is still 0.0212 mGal, now
equal to the stated noise. The corrections removed exactly what the model added.

**The instructive failure.** If the Bouguer density is wrong, the *subtraction*
injects signal rather than removing it:

| $\rho_B$ (kg/m³) | peak recovered anomaly (mGal) | shift from $\rho_B = 2400$ |
|---|---|---|
| 2000 | 3.8946 | $-0.1049$ |
| 2200 | 3.9470 | $-0.0525$ |
| 2400 | 3.9995 | 0.0000 |
| 2670 | 4.0703 | $+0.0708$ |
| 3000 | 4.1569 | $+0.1574$ |

A 670 kg/m³ density error moves the answer by 0.27 mGal — 7% of the target, and
comparable to the anomaly from a subtle body. **Superposition tells you that the
terms add; it does not tell you that your estimates of them are right.** The
uncertainty of a sum of independently estimated terms is the quadrature sum of
their uncertainties: subtracting a term known only to $\pm0.9$ mGal from data
known to $\pm0.2$ mGal yields a residual known only to $\pm0.92$ mGal. When the
nuisance term's uncertainty dominates, the subtraction has made the data
*less* informative than they were.

## 9. Further reading

- **Blakely (1995).** Chapters 3, 9. Level: advanced.
- **Menke.** Chapter 1. Level: graduate.
- **Telford, Geldart & Sheriff (1990).** Chapter 3. Level: intermediate.

## 10. Related lessons

- [05-03-02 Analytical Solutions for Simple Bodies](./02-analytical-solutions.md)
- [05-03-04 Numerical Forward Modelling and Discretisation](./04-numerical-forward-modelling.md)
- [18-07-01 Joint Inversion Concepts](../../18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md)

## Self-assessment checklist

- [ ] I can state the superposition principle and list which methods obey it.
- [ ] I can distinguish linearity in the field from linearity in the parameter.
- [ ] I can build a composite model as a sum of prisms and verify it.
- [ ] I can explain demagnetisation as a failure of superposition.
- [ ] I can propagate uncertainty through a subtraction.
