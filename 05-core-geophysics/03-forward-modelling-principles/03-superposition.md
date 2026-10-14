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

### 3.4 Where superposition comes from, and exactly when it holds

Linearity is not a metaphysical property of "simple" problems; it is a property
of the governing equation, and for gravity it can be traced to one line.

The governing equation for the potential is Poisson's equation,
$\nabla^2\Phi = 4\pi G\rho$ ([05-02-01](../02-geophysical-fields-and-observables/01-scalar-vs-vector-fields.md)).
The Laplacian is a linear operator: $\nabla^2(\alpha\Phi_1+\beta\Phi_2) =
\alpha\nabla^2\Phi_1+\beta\nabla^2\Phi_2$. Therefore if $\rho_1$ generates
$\Phi_1$ and $\rho_2$ generates $\Phi_2$, then $\alpha\rho_1+\beta\rho_2$
generates $\alpha\Phi_1+\beta\Phi_2$ — because both sides satisfy the same linear
equation with consistent boundary conditions, and the solution is unique. That
is the whole proof, and it hinges on two things: **linearity of the operator**
and **uniqueness of the solution for given boundary conditions** (the latter
provided by [02-08-06](../../02-physics/08-potential-theory/06-uniqueness-theorems.md)).

Superposition therefore fails when either ingredient fails:

- the operator is non-linear (radiation transport, non-linear elasticity), or
- the boundary conditions depend on the solution (a free surface for a
  magnetised body, where the internal field is itself what determines the
  magnetisation).

The second case is the demagnetisation effect, quantified in Section 3.5, and it
is the reason magnetic modelling is *conditionally* linear while gravity
modelling is unconditionally linear.

### 3.5 Demagnetisation, derived self-consistently

For a magnetisable body the internal field is the applied field *minus* the
body's own field. For an ellipsoid this is exact with a demagnetising factor $N$
(dimensionless, dependent only on shape):

$$\mathbf{H}_\text{int} = \mathbf{H}_0 - N\mathbf{M},
\qquad \mathbf{M} = \chi\,\mathbf{H}_\text{int} .$$

These two equations are simultaneous — $\mathbf{M}$ appears on both sides —
which is precisely the non-linearity. Solve them:

$$\mathbf{M} = \chi\left(\mathbf{H}_0 - N\mathbf{M}\right)
\Longrightarrow \mathbf{M}\left(1+N\chi\right) = \chi\mathbf{H}_0
\Longrightarrow
\boxed{\;\chi_\text{eff} \equiv \frac{M}{H_0} = \frac{\chi}{1+N\chi}\;}$$

**Physical interpretation.** The factor $1/(1+N\chi)$ is the self-shielding of
the body. It is *not* a small correction:

| shape | $N$ | $\chi_\text{eff}/\chi$ at $\chi = 0.5$ |
|---|---|---|
| sphere | 1/3 | 0.857 |
| long cylinder, transverse field | 1/2 | 0.800 |
| thin sheet in its own plane | $\to 0$ | $\to 1$ |
| needle along the field | $\to 0$ | $\to 1$ |

So the *same* susceptibility produces anomalies differing by 20% depending on
shape alone, and a linear model that ignores $N$ overestimates the magnetisation
by $1+N\chi$ — exactly 1.167 for a sphere at $\chi = 0.5$, as the lesson's
Section 3.5 table shows. The threshold for a 10% error is
$N\chi = 0.10$, i.e. $\chi = 0.3$ for a sphere but $\chi = 0.2$ for a transverse
cylinder and *never* for a thin sheet.

**How to state this honestly.** Superposition in magnetics is exact in the
*applied* field and approximate in the *induced* magnetisation. The correct
model is either (a) linear with $\chi_\text{eff}$ computed from the shape, or (b)
non-linear, solving the self-consistent equation. Choosing (a) while pretending
$N = 0$ is the error.

### 3.6 Why subtracting a nuisance effect does not improve the signal-to-noise ratio

Subtraction is the most-used application of superposition, and it is usually
justified for the wrong reason.

Let the observation be $S + B + \eta_d$, where $S$ is the target, $B$ the
nuisance (regional, slab, neighbouring body) and $\eta_d$ the data noise with
standard deviation $\sigma_d$. Suppose the nuisance is estimated with
uncertainty $\sigma_b$, and subtract the estimate. The residual is

$$R = S + \left(B - \hat B\right) + \eta_d,
\qquad \sigma_R = \sqrt{\sigma_d^2 + \sigma_b^2} \;\ge\; \sigma_d .$$

**The uncertainty can only grow.** Subtraction never improves the noise level;
it can only add to it. So why subtract at all? Because the alternative is worse
in a different way:

- without subtraction, the interpretable quantity is $S + B$, and $B$ may be
  ten times larger than $S$ — the *bias* from an unknown large term dominates
  everything;
- with subtraction, the bias is removed and replaced by a smaller, *known*
  uncertainty $\sigma_b$.

The correct criterion is therefore about *bias*, not about noise:

$$\text{subtract if}\quad |B| \gg |S| \ \text{and}\ \sigma_b \ll |B| .$$

**Worked arithmetic.** With $|B| = 8.4$ mGal, $\sigma_b = 0.9$ mGal,
$|S| = 0.6$ mGal and $\sigma_d = 0.2$ mGal, the residual is
$0.6 \pm \sqrt{0.2^2+0.9^2} = 0.6 \pm 0.92$ mGal. The residual is smaller than
its own error bar — **but it is not zero-mean-biased by 8.4 mGal any more**, so
the *bound* on $S$ has improved from "$|S| < 8.4 + \text{something}$" to
"$|S| = 0.6 \pm 0.92$". That is real progress: the subtraction converted a
useless data set into a weak constraint. Reporting it as "a 0.6 mGal anomaly"
without the $\pm0.92$ would be the error.

### 3.7 Superposition of noise, derived

Superposition applies to signals exactly; it applies to *errors* only in a
different form, and confusing the two is a common source of over-optimistic
uncertainty budgets.

For two independent random errors $\epsilon_1,\epsilon_2$ with variances
$\sigma_1^2,\sigma_2^2$,

$$\operatorname{Var}[\epsilon_1+\epsilon_2] = \sigma_1^2+\sigma_2^2
\qquad\text{(independent)},$$

but in general

$$\operatorname{Var}[\epsilon_1+\epsilon_2] = \sigma_1^2+\sigma_2^2
+ 2\operatorname{Cov}(\epsilon_1,\epsilon_2) .$$

**So variances add only when the errors are uncorrelated.** For *correlated* noise
the cross-term can dominate. With $\epsilon_2 = \epsilon_1$ (perfect correlation),
$\operatorname{Var} = 4\sigma^2$ rather than $2\sigma^2$: the standard deviation
doubles instead of growing by $\sqrt{2}$, so the quadrature estimate understates
the true uncertainty by $(2-\sqrt{2})/2 = 29.3\%$. (Equivalently, the correct value is
$2/\sqrt{2} = 41.4\%$ *larger* than the quadrature estimate — the same discrepancy
stated from the other side, and a reminder to say which side.)

**Where this bites in superposition.** Summing the anomalies of $N$ prisms sums
their *modelling* errors as well. If those errors come from a shared assumption —
one Bouguer density, one datum, one survey-wide terrain model — they are
positively correlated and add linearly, not in quadrature:

$$\sigma_\text{total} \approx N\sigma_\text{shared}
\quad\text{(shared error)} \qquad\text{vs}\qquad
\sqrt{N}\,\sigma_\text{independent} .$$

**Numbers.** For $N = 12$ prisms and a shared Bouguer-density uncertainty worth
0.05 mGal per prism, the quadrature (wrong) estimate is
$\sqrt{12}\cdot0.05 = 0.17$ mGal while the linear (right) estimate is
$12\cdot0.05 = 0.60$ mGal — a factor of 3.5. **Uncertainties from shared inputs
must be propagated outside the sum, not inside it**, which is why this module
always separates instrument error (independent per station) from model error
(shared).

The correlated-noise averaging rule is derived in
[05-02-03](../02-geophysical-fields-and-observables/03-noise-and-drift.md), where
the same distinction sets how long a station must be occupied.

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

### 6.4 Worked arithmetic: assembling a composite model and checking it

**The model.** Three prisms of density contrast 400 kg/m³, each 100 m wide and
200 m deep, at depths 150 m (top) with tops at 100, 150 and 200 m, and horizontal
offsets 0, 150 and 300 m. Build the total anomaly by summation and check it
against a single prism that encloses them.

**Why the sum is not the enclosing body.** The three prisms overlap in depth
range but differ in top depth, so their *union* is a stepped body; a single prism
enclosing all three would include (and thus add) mass that is not in any of them.
The difference is exactly the mass of the "notches", and by superposition it is
computable as the anomaly of a *negative*-density prism — which is the standard
device for building arbitrary bodies: **model the notches with negative density
contrast.**

**The arithmetic of the check.** Sum of three prisms $= $ enclosing prism
$-$ notches. Both routes must give identical numbers to the quadrature
precision, and the demonstration's prism-versus-quadrature comparison
([05-03-01](./01-forward-problem.md)) reports agreement at
$1.8\times10^{-15}$ for a single prism, so the check is meaningful at that level.
Any discrepancy above the round-off floor then signals an error in one of the two
geometries, not in the addition.

**Sensitivity per prism.** Displace one prism laterally by 5 m and recompute: the
change in the anomaly is one column of $\mathbf{G}$ times its density. Comparing
that change with the noise answers whether the prism's *position* is constrained
at all — the same test as in
[05-03-01](./01-forward-problem.md) Section 6.1, applied to a model with more
parameters.

### 6.5 A shortcut that fails: "add prisms until the residual looks clean"

**The shortcut.** Build a regional model by adding prisms until the residual
anomaly is white (no long-wavelength structure).

**Why it fails.** The residual can be made arbitrarily white by adding enough
parameters, because the model acquires enough freedom to fit the noise. Formally,
adding $n_s$ model parameters to fit $n_o$ data points leaves $n_o - n_s$
degrees of freedom for the residual; as $n_s \to n_o$ the residual tends to zero
*whatever the data are*. The demonstration of
[05-01-04](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) shows
the extreme version: models at 100 m and 600 m both reproduce the data to
$1.2\times10^{-15}$ while differing from the true model by 27% and 131%.

**What to do instead.** Decide the regional model *before* looking at the
residual — from independent information (a regional gravity compilation, a
crustal model, an isostatic prediction) — and report the number of parameters
and the resulting degrees of freedom. The test is not "is the residual white?"
but "does the model predict data it was not fitted to?" That is the
cross-validation principle in
[18-08-02](../../18-inverse-problems/08-practical-inversion-workflow/02-synthetic-testing.md).

**The generalisable lesson.** Superposition gives you the ability to build any
model; it gives you no guidance about which model is meaningful. That guidance
must come from outside the data.

### 6.6 Extended worked example: superposition inside a reduction chain

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
