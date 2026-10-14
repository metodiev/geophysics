---
id: 19-08-02
title: "Simulating Gravity and Magnetic Responses"
level: doctoral
prereqs: ["19-07-03", "05-03-05", "19-07-01"]
tags: [numerical-modelling, verification, gravity, magnetics, potential-fields, quadrature]
---

# Simulating Gravity and Magnetic Responses

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the vertical gravity of a uniform sphere and of an infinite slab, and
   use both as exact benchmarks for a volume-quadrature code.
2. **Verify** a quadrature forward model against an exact solution of the same
   equations, and **distinguish** that from validating the model against data.
3. **Quantify** the error of a point-mass (or dipole) approximation to a compact
   body as a function of distance, and **state** the distance at which it becomes
   usable.
4. **Explain** why two bodies with the same mass and centroid can have identical
   far-field anomalies and different near-field anomalies, and **measure** the
   difference.
5. **Compute** the magnetic field of a uniformly magnetised sphere from the exact
   dipole relation and **verify** a quadrature implementation against it.
6. **Report** a potential-field forward model with its exact benchmarks, its
   approximation error and its remaining model-form uncertainty distinguished.

## Prerequisites

- [19-07-03 Model Validation Against Observations](../07-verification-validation-uncertainty/03-model-validation.md)
  — the calibration/validation split and the admitted set used here.
- [19-07-01 Code Verification: Order-of-Accuracy and Manufactured Solutions](../07-verification-validation-uncertainty/01-code-verification.md)
  — the verification discipline.
- [05-03-05 Validating Forward Codes Against Analytic Benchmarks](../../05-core-geophysics/03-forward-modelling-principles/05-forward-model-validation.md)
  — the geophysical version of the same benchmarks.

All models and data in this module are **SYNTHETIC**: chosen bodies, chosen density
and magnetisation contrasts. The analytic sphere and slab fields are exact
solutions of the stated equations, and every other number is printed by this
lesson's demonstration.

## 1. Intuition: potential fields are integrals, and integrals hide the model

A gravity or magnetic anomaly is an integral of a source distribution against a
kernel that decays with distance. That structure has three consequences that
shape the whole of potential-field modelling.

- **The forward problem is easy and the inverse problem is hard.** Evaluating the
  integral is a quadrature, and a quadrature can be verified exactly against the
  handful of bodies whose integrals have closed forms. Recovering the source from
  the anomaly is where the difficulty lives
  ([18-inverse-problems](../../18-inverse-problems/README.md)).
- **The kernel is smooth and slowly decaying, so the *shape* of the source matters
  mostly at short range.** At long range every compact body looks like its total
  mass. A model fitted to distant stations is a mass estimate, not a shape
  estimate, and the demonstration measures exactly how much of the shape survives.
- **Approximations that are excellent at range are worthless up close.** The
  point-mass model is a *far-field* approximation; its error is second order in
  the ratio of body size to distance, and at typical survey offsets it is several
  per cent. Nothing in a synthetic demonstration of the far field reveals this.

Those three facts make potential-field modelling a natural home for the
verification/validation distinction of module 19-07: the exact benchmarks are
abundant, the discretisation choices are few, and essentially all of the risk sits
in the model-form choices that no benchmark can detect.

## 2. Definitions

**Gravity anomaly (vertical component).** For a source with density contrast
$\Delta\rho(\mathbf{r}')$,

$$g_z(\mathbf{x}) = G\iiint \Delta\rho(\mathbf{r}')\,
\frac{z - z'}{\lvert \mathbf{x} - \mathbf{r}'\rvert^{3}}\,\mathrm{d}V' ,
\qquad G = 6.67430\times10^{-11}\ \mathrm{m^{3}kg^{-1}s^{-2}}.$$

**Magnetic field of a magnetisation distribution.**
$\mathbf{B}(\mathbf{x}) = \frac{\mu_0}{4\pi}\iiint \big[3(\mathbf{M}\cdot\hat{\mathbf{r}})
\hat{\mathbf{r}} - \mathbf{M}\big]/\lvert\mathbf{r}\rvert^{3}\,\mathrm{d}V'$ with
$\mathbf{r}$ from source to station and $\mu_0 = 4\pi\times10^{-7}$ H m$^{-1}$
exactly.

**Quadrature.** A weighted sum approximating an integral. Gauss-Legendre is the
standard choice: for an analytic integrand it converges faster than any power of
the node count.

**Equivalent source / point-mass model.** A lumped representation that reproduces a
body's total mass (or moment) at its centroid. Exact at infinite range, approximate
at every finite range.

**Model-form error.** The part of the difference between model and data that no
parameter choice removes. It is invisible to verification and is measured only by
comparing models against each other and against held-out data.

## 3. Derivations

### 3.1 The uniform sphere: an exact benchmark

For a uniform sphere of radius $a$, centre depth $z_c$ and density contrast
$\Delta\rho$, the shell theorem states that the external field equals that of a
point mass $M = \frac{4}{3}\pi a^{3}\Delta\rho$ at the centre:

$$g_z(x) = \frac{GM z_c}{\left(x^{2} + z_c^{2}\right)^{3/2}}
= \frac{G\frac{4}{3}\pi\Delta\rho\,a^{3}z_c}{\left(x^{2} + z_c^{2}\right)^{3/2}} .$$

This is the cleanest benchmark in the subject: an exact, closed-form reference for a
three-dimensional volume integral, with no approximation anywhere. A quadrature code
that cannot reproduce it has a bug, and Section 5.1 measures the convergence that
establishes it.

### 3.2 The infinite slab: an exact limit

Integrate $g_z$ above an infinite horizontal slab of thickness $t$ and contrast
$\Delta\rho$. In cylindrical coordinates about the station,

$$g_z = G\Delta\rho\int_0^{2\pi}\int_0^{\infty}\int_{z_1}^{z_2}
\frac{z\,\rho\,\mathrm{d}z\,\mathrm{d}\rho\,\mathrm{d}\phi}
{\left(\rho^{2} + z^{2}\right)^{3/2}}
= 2\pi G\Delta\rho\int_0^{\infty}\rho\left[
\frac{1}{\sqrt{\rho^{2}+z_1^{2}}} - \frac{1}{\sqrt{\rho^{2}+z_2^{2}}}
\right]\mathrm{d}\rho .$$

With $\int \rho/\sqrt{\rho^{2}+z^{2}}\,\mathrm{d}\rho = \sqrt{\rho^{2}+z^{2}}$,

$$g_z = 2\pi G\Delta\rho\left[
\sqrt{\rho^{2}+z_2^{2}} - \sqrt{\rho^{2}+z_1^{2}}\right]_{\rho = 0}^{\infty}
= 2\pi G\Delta\rho\,(z_2 - z_1) = 2\pi G\Delta\rho\,t .$$

The limit is independent of the slab's depth and of the station's position: a
genuine exact benchmark for the *far-field* limit of a wide body.

### 3.3 The magnetic dipole

A uniformly magnetised sphere of radius $a$ and magnetisation $M$ has moment
$m = \frac{4}{3}\pi a^{3}M$ and produces exactly a dipole field outside itself:

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}\,
\frac{3(\mathbf{m}\cdot\hat{\mathbf{r}})\hat{\mathbf{r}} - \mathbf{m}}{r^{3}} .$$

Directly above the centre at depth $z_c$ this gives
$B_z = \frac{\mu_0}{4\pi}\frac{2m}{z_c^{3}}$, and with the numbers of Section 5.3
the magnitude is tens of nanoteslas — the same order as a survey anomaly, which is
why the dipole is the standard first model of a compact magnetic body.

### 3.4 Why the point-mass error is second order

Expand the kernel for a small body at distance $r \gg a$. The leading correction to
the monopole term comes from the body's second moment and scales as $(a/r)^{2}$.
The demonstration measures it: the discrepancy between a cube and its point-mass
equivalent falls from about $6$ per cent directly above the body to $0.3$ per cent
at one body-width of horizontal offset and to nothing in the far field. **The
approximation error is a function of the station offset, so a single
"point-mass model" number cannot characterise it.**

## 4. What follows for interpretation

Three operational statements, all of which the demonstration measures:

1. **A far-field fit determines mass, not shape.** Two bodies with the same mass
   and centroid produce anomalies that agree to a fraction of a per cent at long
   range and differ by tens of per cent close in.
2. **A near-field survey cannot be interpreted with a point mass.** The
   approximation error at the offset where the anomaly is largest is exactly where
   the model is worst.
3. **An exact benchmark does not validate the body.** The sphere benchmark verifies
   the integrator; whether the *Earth* is better represented by a sphere, a cube or
   a dyke is a modelling question answered by data and by the admitted set
   ([19-07-03](../07-verification-validation-uncertainty/03-model-validation.md)).

## 5. Measured evidence

The demonstration `code/simulate_gravity_response_demo.py` runs in about $0.2$ s.

### 5.1 Verification: quadrature against the exact sphere

Synthetic sphere, radius $120$ m, centre depth $300$ m,
$\Delta\rho = 400$ kg m$^{-3}$; maximum relative difference from the exact field at
$x = 200$, $400$ and $800$ m, against the number of Gauss-Legendre nodes per axis:

| nodes per axis | max relative difference |
|---:|---:|
| 6 | $7.234\times10^{-5}$ |
| 10 | $3.992\times10^{-8}$ |
| 14 | $7.172\times10^{-10}$ |
| 20 | $1.335\times10^{-14}$ |

The convergence is faster than any power of $1/n$ — the signature of Gauss-Legendre
on an analytic integrand — and it establishes that the code evaluates the stated
volume integral. It says nothing about the body, the density or the Earth.

### 5.2 The exact slab limit, approached

Synthetic slab, thickness $200$ m, top at $100$ m, $\Delta\rho = 300$ kg m$^{-3}$.
Exact limit $2\pi G\Delta\rho t = 2.5162$ mGal, computed by a one-dimensional
quadrature after integrating $z$ analytically:

| half-width | computed (mGal) | ratio to the exact limit |
|---:|---:|---:|
| 0.5 km | 1.5953 | 0.63403 |
| 1 km | 2.0250 | 0.80478 |
| 2 km | 2.2661 | 0.90062 |
| 5 km | 2.4156 | 0.96004 |
| 20 km | 2.4910 | 0.99000 |
| 100 km | 2.5111 | 0.99800 |

The approach is algebraic in the half-width — the edge effect decays only as
$1/L$ — so a "wide" body is wide only relative to its depth. **An exact limit is
still a limit, and the *rate* at which a code approaches it is part of what must be
verified.**

### 5.3 A compact body against its point-mass equivalent

Synthetic cube, side $200$ m, $100$–$300$ m deep, $\Delta\rho = 300$ kg m$^{-3}$
(mass $2.400\times10^{9}$ kg), computed by quadrature and compared with a point mass
of the same mass at the centroid depth $200$ m:

| offset (m) | cube $g_z$ (mGal) | point mass (mGal) | difference |
|---:|---:|---:|---:|
| 0 | 0.3776 | 0.4005 | −5.70% |
| 100 | 0.2856 | 0.2865 | −0.33% |
| 200 | 0.1420 | 0.1416 | +0.28% |
| 400 | 0.0357 | 0.0358 | −0.33% |
| 800 | 0.0057 | 0.0057 | −0.06% |
| 1600 | 0.0008 | 0.0008 | −0.00% |

The largest error is where the anomaly is largest. Note also the sign change: the
cube's field is *larger* than the point mass's at $200$ m and smaller above the
centre, because the body's mass is not concentrated at its centroid.

### 5.4 Magnetics: a magnetised sphere against the exact dipole

Synthetic sphere, radius $100$ m, centre depth $300$ m, magnetisation $1.0$ A m$^{-1}$
(moment $4.1888\times10^{6}$ A m$^{2}$):

| nodes per axis | max relative difference | $\lvert\mathbf{B}\rvert$ above the centre (nT) |
|---:|---:|---:|
| 6 | $1.835\times10^{-4}$ | 31.034 |
| 10 | $2.207\times10^{-7}$ | 31.028 |
| 16 | $2.132\times10^{-11}$ | 31.028 |
| 24 | $3.756\times10^{-16}$ | 31.028 |

The differences contract to round-off against an independently derived exact
dipole: verification of the magnetic integrator against an exact solution of the
same equations. A cube or a dyke is *not* a dipole, and the size of that failure is
a model-form error that must be measured against the body actually assumed.

### 5.5 The far-field degeneracy, with numbers

Three bodies with the same mass ($2.4\times10^{9}$ kg) and the same centroid depth
($200$ m): a cube of side $200$ m ($\Delta\rho = 300$ kg m$^{-3}$), a sphere of
equivalent volume (radius $124$ m, same $\Delta\rho$), and a $4\times 4$ km sheet
$200$ m thick ($\Delta\rho = 0.750$ kg m$^{-3}$):

| geometry | $g_z$ at 0 m | 200 m | 400 m | 800 m | 2 km |
|---|---:|---:|---:|---:|---:|
| cube, side 200 m | 0.3776 | 0.1420 | 0.0357 | 0.0057 | 0.0004 |
| sphere, radius 124 m | 0.4005 | 0.1416 | 0.0358 | 0.0057 | 0.0004 |
| sheet, $4\times4$ km | 0.0057 | 0.0057 | 0.0057 | 0.0057 | 0.0057 |

Read the columns, not the rows. At $800$ m the three bodies agree to two
significant figures, so a survey confined to that offset cannot distinguish a
compact body from a sheet with the same mass. At $2$ km the sheet is still at its
constant value while the compact bodies have decayed by another factor of $14$; at
the centre the sheet is $66$ times weaker. **The data decide, and the choice of
station offsets decides what the data can decide.**

## 6. Assumptions and regime of validity

1. **Newtonian gravity, uniform density contrast.** Variable density needs the
   density divided into cells, and the quadrature error then depends on the
   density contrast between neighbouring cells.
2. **Station outside the source.** The kernel is singular inside the body; the
   quadrature must not evaluate it there, and a body straddling a station is a
   different (and much more delicate) problem.
3. **The quadrature resolves the body.** Gauss-Legendre nodes per axis must be
   increased until the benchmark convergence of Section 5.1 is reproduced; a fixed
   node count "because it looked fine" is not a justification.
4. **Dipole approximation for magnetics only.** The dipole field is exact for a
   uniformly magnetised sphere and approximate for anything else, including a
   cube, a dyke or a body with remanence at an angle.
5. **The reduction is part of the model.** A magnetic anomaly is a difference from
   a reference field and depends on the ambient field direction and the reduction
   applied; two models can differ by more in that choice than in the body.
6. **What these benchmarks do not establish.** They do not verify the equations for
   a variable-density Earth, and they cannot validate the body: only independent
   data can do that ([19-07-03](../07-verification-validation-uncertainty/03-model-validation.md)).

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| gravitational constant | $G$ | m$^{3}$kg$^{-1}$s$^{-2}$ | $6.67430\times10^{-11}$ |
| gravity | $g_z$ | m s$^{-2}$; mGal $= 10^{-5}$ m s$^{-2}$ | |
| density contrast | $\Delta\rho$ | kg m$^{-3}$ | |
| slab limit | $2\pi G\Delta\rho t$ | m s$^{-2}$ | $\mathrm{m^{3}kg^{-1}s^{-2}}\cdot\mathrm{kg\,m^{-3}}\cdot\mathrm{m}$ |
| magnetic moment | $m$ | A m$^{2}$ | |
| flux density | $\mathbf{B}$ | T; nT $= 10^{-9}$ T | |
| vacuum permeability | $\mu_0$ | H m$^{-1}$ | exactly $4\pi\times10^{-7}$ |

Two checks catch most unit blunders: the slab limit must come out in acceleration
units, and a magnetic anomaly in the hundreds of nanoteslas corresponds to a
magnetised body of the size and depth used here — if a computation returns teslas
or microteslas, a factor of $\mu_0$ or $10^{9}$ is misplaced.

## 8. Worked examples

### Example 1 — the slab limit by hand

$\Delta\rho = 300$ kg m$^{-3}$, $t = 200$ m:

$$2\pi G\Delta\rho t = 2\pi \times 6.67430\times10^{-11}\times300\times200
= 2.5162\times10^{-5}\ \mathrm{m\,s^{-2}} = 2.5162\ \mathrm{mGal},$$

which is the value the demonstration prints. A slab half-width of $20$ km reaches
$99.0$ per cent of it, so a body can be "infinite" for a station $600$ m above it
only if it extends tens of kilometres — a scale that matters in basin and
crustal-scale surveys and not in a near-surface one.

### Example 2 — the point-mass error at the worst offset

Above the centre the cube's field is $0.3776$ mGal against the point mass's
$0.4005$ mGal: a relative difference of $(0.3776 - 0.4005)/0.4005 = -5.70$ per
cent. The expected scaling is $(a/z_c)^{2}$ with $a$ the body's half-width
($100$ m) and $z_c = 200$ m: $0.25$, so a coefficient of about $0.23$ reproduces
the measured $5.7$ per cent. **The error is predictable from geometry alone**, and
that is what makes it possible to state, in advance, the offset at which a
point-mass interpretation is defensible.

### Example 3 — the dipole field of a compact body

Sphere radius $100$ m, magnetisation $1.0$ A m$^{-1}$, centre depth $300$ m:

$$m = \frac{4}{3}\pi (100)^{3}(1.0) = 4.1888\times10^{6}\ \mathrm{A\,m^{2}},$$

$$B_z(0) = \frac{\mu_0}{4\pi}\frac{2m}{z_c^{3}}
= 10^{-7}\times\frac{2\times4.1888\times10^{6}}{2.7\times10^{7}}
= 3.103\times10^{-8}\ \mathrm{T} = 31.03\ \mathrm{nT},$$

matching the demonstration's $31.028$ nT. A survey anomaly of this size is easily
measured, which is why compact magnetised bodies are the standard textbook target
and why the dipole formula is the first model to try.

### Example 4 — a verification and validation statement

> Verification: volume quadrature against the exact sphere field, maximum relative
> error $1.3\times10^{-14}$ at $20$ nodes per axis; against the exact infinite-slab
> limit, $99.8$ per cent at $100$ km half-width, with the $1/L$ approach measured;
> magnetic quadrature against the exact dipole, $3.8\times10^{-16}$. Model-form
> error: point-mass approximation to a compact body, $-5.70$ per cent above the
> centre, below $0.4$ per cent beyond one body-width; far-field degeneracy between
> a compact body and an equal-mass sheet, unresolved at $800$ m and a factor of
> $14$ at $2$ km. Not established: the body. No independent data were used.

## 9. Python demonstration

```bash
cd 19-numerical-modeling-hpc/08-geophysical-simulation-case-studies/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python simulate_gravity_response_demo.py
```

Prints the four tables above and the arithmetic that explains them. Print-only,
no file output, no network, exits 0.

## 10. Exercises

[`exercises/02-simulate-gravity-response-exercises.md`](exercises/02-simulate-gravity-response-exercises.md)
and
[`exercises/02-simulate-gravity-response-solutions.md`](exercises/02-simulate-gravity-response-solutions.md)
include deriving the slab limit, computing the offset at which a point-mass model
reaches a stated accuracy, and designing a survey that can tell a sheet from a
compact body.

## 11. Applications

- **Basin and crustal studies.** Long-wavelength gravity and magnetic anomalies
  constrain Moho depth and crustal thickness, where the equivalent-source and
  point-mass approximations are appropriate because the sources are deep and
  extended.
- **Mineral and near-surface targets.** Compact, shallow bodies are exactly where
  the far-field approximations fail, so interpretation must use the body geometry
  with the measured approximation error attached.
- **Joint inversion.** Gravity and magnetics share the geometry but not the
  sensitivity, so their combination is a shape constraint; the kernels differ, and
  the joint problem inherits both models' form errors
  ([18-07-01 Why Joint Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md)).
- **Data reduction.** The reference field, the Bouguer and terrain corrections, and
  the ambient-field removal are model choices that enter every anomaly
  ([07-gravity-geodesy](../../07-gravity-geodesy/README.md)).

## 12. Further study

- [19-07-03](../07-verification-validation-uncertainty/03-model-validation.md) —
  the validation protocol applied to these models.
- [05-03-05](../../05-core-geophysics/03-forward-modelling-principles/05-forward-model-validation.md)
  — the repository's core forward-modelling benchmarks.
- [19-05-02 Boundary Element Methods for Potential Fields](../05-integral-equation-and-boundary-methods/02-boundary-element.md)
  — the alternative to volume quadrature for potential-field modelling.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the inversion of
  these kernels, and its non-uniqueness.

## Mastery checkpoint

Without notes:

> A compact body of mass $M$ centred at $200$ m depth produces a $1.00$ mGal
> anomaly directly above it. **(a)** Estimate the anomaly at $400$, $800$ and
> $1600$ m using the point-mass model and state the functional form of the decay.
> **(b)** A $200$-m cube of the same mass gives $0.94$ mGal at the centre; compute
> the model-form error and explain its sign. **(c)** A sheet of the same mass gives
> $0.014$ mGal at the centre but $0.014$ mGal at $2$ km; state which observations
> would distinguish the sheet from the cube. **(d)** The magnetics of the same body
> are modelled as a dipole; state the two conditions under which that is exact and
> the one body shape for which it is not.

Worked answers appear in
[`exercises/02-simulate-gravity-response-solutions.md`](exercises/02-simulate-gravity-response-solutions.md).

## Common pitfalls

1. **Using a point mass at short range.** The demonstration measures $5.7$ per cent
   above the centre of a cube, where the anomaly is largest.
2. **Reporting a body from a far-field fit.** The mass is determined; the shape is
   not (Section 5.5).
3. **Treating a slab as infinite too early.** The approach to the exact limit is
   algebraic: $99.0$ per cent at $20$ km half-width.
4. **A fixed quadrature node count.** Verification requires a measured convergence
   against an exact solution, not a plausible-looking field.
5. **Forgetting the reduction.** A magnetic anomaly depends on the reference field
   and the ambient-field removal, which are choices, not measurements.
6. **Claiming validation from a benchmark.** An exact sphere benchmark verifies the
   code and says nothing at all about the Earth
   ([19-07-03](../07-verification-validation-uncertainty/03-model-validation.md)).

## Related modules

- [19-08 Geophysical Simulation Case Studies](README.md) — the module that contains
  this lesson.
- [19-07 Verification, Validation and Numerical Uncertainty](../07-verification-validation-uncertainty/README.md).
- [05-core-geophysics](../../05-core-geophysics/README.md) — gravity and magnetic
  methods.
- [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md).
- [18-inverse-problems](../../18-inverse-problems/README.md).

## Self-assessment checklist

- [ ] I can derive the exact sphere and slab fields and use them as benchmarks.
- [ ] I can verify a quadrature against them and interpret the convergence.
- [ ] I can quantify the point-mass error and predict its scaling.
- [ ] I can construct two bodies with identical far fields and different near
      fields.
- [ ] I can compute a dipole field in nanoteslas from a stated magnetisation.
- [ ] I can write a statement that separates verification, model-form error and
      validation.
