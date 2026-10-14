---
id: 00-02-04
title: "Cross-Cutting Skills: Mathematics, Computing, Inverse Theory"
level: beginner
prereqs: ["00-02-02"]
estimated_minutes: 40
tags: [curriculum, mathematics, computing, inverse-theory]
---

# Cross-Cutting Skills: Mathematics, Computing, Inverse Theory

## Learning objectives

- Explain what makes a skill *cross-cutting*: it is used in many folders, it is
  nobody's speciality, and it fails silently when missing.
- Trace mathematics, computing and inverse theory through the curriculum, and
  name the specific modules in which each is used rather than merely introduced.
- Interleave a cross-cutting skill with the domain material that needs it,
  instead of deferring it until "later".
- Recognise the three failure signatures of a missing cross-cutting skill.

## Prerequisites

[Dependency Graph and Valid Study Orders](./02-dependency-graph.md) for the
folder-level structure that these skills thread through.

## 1. What "cross-cutting" means

A **cross-cutting skill** has three properties:

1. **Many consumers.** It is used in a large number of folders.
2. **No owner.** It does not belong to any one domain, so no domain folder takes
   responsibility for teaching it fully. Mathematics, computing and inverse
   theory all behave this way.
3. **Silent failure.** When it is missing, the failure does not announce itself as
   a gap; it appears as "this topic is too hard", "my results keep coming out
   wrong", or "my model fits the data but I cannot defend it".

That third property is why cross-cutting skills deserve an explicit plan rather
than good intentions. Compare it with a domain gap, which is obvious: you know
when you cannot explain what a magnetotelluric sounding is.

Two further skills are cross-cutting-adjacent and worth naming here:
**statistics and uncertainty quantification** ([21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md))
and **communication and reproducibility** ([24-research-papers-writing](../../24-research-papers-writing/README.md),
[22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md)).
They behave exactly like the main three: used everywhere, owned nowhere, and
silently fatal when missing. They are treated separately in those folders.

## 2. Mathematics: the notation of the physics

**What it is for.** Mathematics in geophysics is not a hurdle before the
interesting part; it *is* the language in which the physics is stated. A velocity
model is a function, an inversion is a linear or nonlinear operator problem, and
a wavefield is a solution of a partial differential equation with boundary
conditions.

**Where it is introduced.** [01-mathematics](../../01-mathematics/README.md), 16
modules: arithmetic, algebra, trigonometry, geometry and coordinates,
single-variable calculus, multivariable and vector calculus, linear algebra,
ODEs, PDEs, Fourier analysis, complex analysis, numerical methods, probability
and statistics foundations, optimization, tensors and differential geometry,
functional analysis.

**Where it is actually used.**

| Mathematical skill | Used in (examples) |
|---|---|
| Units, dimensional analysis | every observational lesson in 05–17, 23 |
| Trigonometry and spherical geometry | [07-gravity-geodesy](../../07-gravity-geodesy/README.md), [15-oceanography-marine](../../15-oceanography-marine/README.md), [17-remote-sensing-gis](../../17-remote-sensing-gis/README.md) |
| Partial derivatives and gradients | [02-physics/08-potential-theory](../../02-physics/08-potential-theory/README.md), all potential-field modelling in 07, 08 |
| Divergence and curl | [02-physics/07-electromagnetism](../../02-physics/07-electromagnetism/README.md), [08-geomagnetism-electromagnetism](../../08-geomagnetism-electromagnetism/README.md), [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) |
| Line and surface integrals, Gauss and Stokes | [02-physics](../../02-physics/README.md), [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) |
| Linear algebra, eigenproblems | [18-inverse-problems](../../18-inverse-problems/README.md), [20-signal-processing](../../20-signal-processing/README.md), [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) (normal modes) |
| Fourier analysis | [20-signal-processing](../../20-signal-processing/README.md), [06-seismology](../../06-seismology/README.md), [16-atmosphere-climate](../../16-atmosphere-climate/README.md) |
| Complex analysis | frequency-domain responses in [08](../../08-geomagnetism-electromagnetism/README.md), [09](../../09-electrical-em-methods/README.md), [20](../../20-signal-processing/README.md) |
| PDEs and numerical methods | [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md), [13](../../13-geodynamics-tectonics/README.md), [16](../../16-atmosphere-climate/README.md) |
| Probability and statistics | [21-statistics-bayesian-ml](../../21-statistics-bayesian-ml/README.md), [18-inverse-problems](../../18-inverse-problems/README.md), every uncertainty statement in this curriculum |
| Optimization | [18-inverse-problems/04-nonlinear-inversion](../../18-inverse-problems/04-nonlinear-inversion/README.md), [21-statistics-bayesian-ml/04-machine-learning-fundamentals](../../21-statistics-bayesian-ml/04-machine-learning-fundamentals/README.md) |

**The failure signature.** You follow a derivation step by step but cannot
reproduce it the next day, and you cannot say what the result means physically.
The usual cause is that you learned the *steps* without the *operations* — you
have seen a divergence, but you cannot state what it measures.

**The fix.** For each mathematical technique, force three questions: what does it
measure physically, what are its units, and what happens in the limiting cases?
That is the same discipline as [How to Learn Geophysics](../01-study-roadmap/01-how-to-learn-geophysics.md),
applied to notation.

## 3. Computing: turning method into thing

**What it is for.** Almost nothing in geophysics is done by hand. Computation is
how a method becomes a capability: you produce numbers, plots, and models that
other people can inspect and re-run.

**Where it is introduced.** [03-scientific-computing](../../03-scientific-computing/README.md),
13 modules: Python fundamentals, NumPy, SciPy, pandas, plotting and
visualisation, Jupyter and notebooks, SymPy, gridded geospatial data, geospatial
Python, ObsPy and seismic data, PyGMT and mapping, numerical simulation, testing
profiling and packaging.

**Where it is actually used.** Everywhere from
[05-core-geophysics](../../05-core-geophysics/README.md) onwards. The parts that
are commonly *underestimated*:

| Skill | Why it matters more than it looks |
|---|---|
| Version control | Every result has a provenance; git is how provenance is recorded |
| Numerical simulation | Forward modelling is how you test an inversion |
| Testing | A model that cannot be verified cannot be defended |
| Profiling | Geophysical grids and time series are large; naive code is unusable |
| File formats and I/O | Data arrive as SEG-Y, netCDF, HDF5, GeoPackage, ASCII; each has traps |
| Environment management | Results must be reproducible by someone else on another machine |
| Packaging | Analysis code is a deliverable, not a scratch file |

**The failure signature.** Your results change when you re-run the code, or you
cannot tell whether a strange feature in a figure is physics or a bug. Both come
from missing *verification* habits, not from missing syntax.

**The fix.** Adopt one rule immediately: **every numerical method must reproduce a
case whose answer you already know before it is used on a case you do not.**
That is the computational form of the fundamental-practice loop, and it is worth
more than any amount of extra library knowledge.

## 4. Inverse theory: getting from measurement to model

**What it is for.** Geophysics never observes the subsurface directly. It observes
a response and infers a model. That inference step has a structure of its own
which is logically independent of the physics: it is about *ill-posedness*,
resolution, trade-offs and uncertainty.

**Where it is introduced.** [18-inverse-problems](../../18-inverse-problems/README.md),
9 modules: foundations, linear inverse problems, regularisation, nonlinear
inversion, Bayesian inversion, uncertainty quantification, joint and
multi-physics inversion, practical inversion workflow, machine learning in
inversion.

**Why it is cross-cutting and not just another method folder.** Every domain
folder performs inversions, and each of them assumes the same apparatus. In
matrix form, a discretised problem is

$$\mathbf{d} = G\mathbf{m} + \boldsymbol{\epsilon},$$

where $\mathbf{d}$ collects the data, $\mathbf{m}$ the model parameters,
$\boldsymbol{\epsilon}$ the noise, and $G$ the sensitivity (Jacobian) matrix
whose entries are computed by the physics of the particular method. The physics
determines $G$; the *difficulty* is determined by the properties of $G$ — its
singular values, its null space, and the noise level. That is why the same
lessons about regularisation and resolution apply to a gravity inversion, an
impedance inversion and a seismic tomography problem.

**Where it is used.**

| Inverse-theory idea | Where it appears |
|---|---|
| Ill-posedness, non-uniqueness | [07-gravity-geodesy](../../07-gravity-geodesy/README.md) (potential fields), [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) |
| Regularisation and damping | every tomographic, resistivity and potential-field inversion |
| Resolution and averaging kernels | [06-seismology/06-seismic-tomography](../../06-seismology/06-seismic-tomography/README.md), [12](../../12-global-geophysics-interior/README.md) |
| Bayesian inference and posteriors | [18-inverse-problems/05-bayesian-inversion](../../18-inverse-problems/05-bayesian-inversion/README.md), [21](../../21-statistics-bayesian-ml/README.md) |
| Joint inversion | combining gravity with seismology, or EM with seismic, in [14](../../14-hydrology-hydrogeophysics/README.md), [11](../../11-exploration-geophysics/README.md) |
| Uncertainty quantification | every stated result in [25-projects-capstone](../../25-projects-capstone/README.md) |

**The failure signature.** Your model fits the data and you cannot say anything
else about it: not which features are resolved, not how sensitive it is to the
regularisation weight, not what a different but equally acceptable model would
look like. The figure looks convincing, and that is precisely the danger.

**The fix.** Require of every inversion you produce: a synthetic test with a
known answer, a stated noise model, a stated criterion for the regularisation
parameter, and a resolution or posterior analysis. This is the M4 milestone in
[Research Milestones](../01-study-roadmap/05-milestones.md).

## 5. Why these three compound

Cross-cutting skills have a property that domain knowledge does not: they
multiply. Learning one more seismology module adds one module of knowledge.
Learning linear algebra better makes *ten* downstream modules easier at once,
because matrix structure appears in all of them.

The practical consequence is an allocation rule:

- **Early on, spend disproportionately on cross-cutting skills.** They are the
  prerequisites of the largest number of downstream lessons.
- **Do not spend indefinitely.** Diminishing returns set in when you have enough
  to use the material; the remaining mathematics is best learned in the context
  of a problem that needs it.
- **Return to them at intervals.** Each domain folder reveals a piece of
  mathematics or computing that you skimmed; going back with a concrete
  application is far more effective than the first abstract pass.

A workable balance for a learner at the beginner-to-intermediate transition is
roughly one third of study time on the cross-cutting skills, two thirds on
physics and domain material, adjusted whenever a specific gap appears.

## 6. Interleaving in practice: the linear-algebra thread

Rather than "doing linear algebra before geophysics", thread the topic through
the domains. A realistic sequence for one thread:

```text
Week 1-2   01-mathematics/07-linear-algebra: vectors, matrices, multiplication,
           rank, determinant, inverse. Verify everything numerically with NumPy.
Week 3     07-gravity-geodesy: build a small sensitivity matrix for a few
           prisms and a few observation points; check the matrix by finite
           differences against the analytic anomaly.
Week 4     18-inverse-problems/02-linear-inverse-problems: least squares,
           normal equations, why the normal equations square the condition
           number, and what happens when G has a null space.
Week 5     18-inverse-problems/03-regularization: add damping, sweep the
           parameter, produce the L-curve, and state what changed in the model.
Week 6     06-seismology: apply the same machinery to a small travel-time
           tomography problem with a synthetic checkerboard.
Week 7     20-signal-processing: the discrete Fourier transform as a matrix,
           and convolution as a matrix multiply.
```

At the end, linear algebra is not a completed prerequisite; it is a *working
tool* that has been used in four different physics settings. That is what
transfer looks like, and it is only achievable by interleaving.

## 7. Diagnosing a missing cross-cutting skill

Three symptoms, and what each usually means:

| Symptom | Likely missing skill | First thing to do |
|---|---|---|
| "I understand the lesson but I cannot redo it" | Mathematical operations, not steps | Re-derive with the physical meaning, units and limits written for each line |
| "My results are wrong and I do not know why" | Verification habit in computing | Reproduce a known case; add a dimension check and an independent estimate |
| "My model is good, I just cannot say more about it" | Inverse theory | Add a resolution test and a regularisation sweep to the existing result |

Notice that none of the three is fixed by reading more domain material, which is
what learners usually try first.

## Common mistakes

1. **Treating mathematics as a preliminary to be cleared.** It is used inside
   every domain lesson; clearing it once is not possible.
2. **Learning a library instead of a method.** You can call a solver without
   knowing whether the problem is well posed.
3. **Deferring inverse theory to the end.** It is needed by roughly the middle of
   every track.
4. **Substituting machine learning for inference.** A flexible model that fits the
   data still needs a resolution and uncertainty argument.
5. **Endless preparation.** More than about a third of your time on cross-cutting
   skills, with no application in sight, is usually displacement activity.
6. **Treating computing as tooling rather than method.** Reproducibility and
   verification are scientific requirements, not housekeeping.

## Real-world applications

- **Research software in practice.** Every professional result ships with code,
  and the code's quality is what makes the result reusable — see
  [22-data-engineering-reproducibility](../../22-data-engineering-reproducibility/README.md).
- **Technical review.** Reviewers check exactly three things in a geophysical
  paper: is the forward physics right, is the inversion set up defensibly, and is
  the analysis reproducible. Those are the three cross-cutting skills.
- **Career mobility.** Cross-cutting skills are what transfer between tracks;
  specialities change more often than the underlying mathematics does.

## Further reading

- Strang, G. (2016). *Introduction to Linear Algebra* (5th ed.). Wellesley-Cambridge
  Press. — Matrix structure and the geometry of least squares, which is the
  backbone of linear inversion.
- Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and Inverse
  Problems.* Academic Press. — The standard bridge from linear algebra and
  statistics to geophysical inversion; check the latest edition's date and
  contents, as the text has been revised across editions.
- Menke, W. (2012). *Geophysical Data Analysis: Discrete Inverse Theory*
  (3rd ed.). Academic Press. — Inverse theory written specifically for
  geophysicists, with attention to non-uniqueness and resolution.
- Wilson, G., Bryan, J., Cranston, K., Kitzes, J., Nederbragt, L., & Teal, T. K.
  (2017). Good enough practices in scientific computing. *PLOS Computational
  Biology*, 13(6), e1005510. — A pragmatic checklist for the computing habits in
  section 3.
  These are bibliographic records; confirm availability through your library or a
  DOI resolver before citing them yourself.

## Related lessons

- [Prerequisite Dependency Graph and Valid Study Orders](./02-dependency-graph.md)
- [Domain Tracks: Seismology, Potential Fields, EM, Climate, Near-Surface](./03-domain-tracks.md)
- [Deliberate Practice, Spaced Repetition and Problem-Solving Habits](../01-study-roadmap/04-study-habits.md)
- [Running the Link, Formula and Duplication Checks](../03-how-to-use-this-repo/03-quality-gate.md)
