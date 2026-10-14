---
id: 05-01-04
title: "Non-Uniqueness of Geophysical Models"
level: advanced
prereqs: ["05-01-01", "05-01-03"]
tags: [non-uniqueness, null-space, ambiguity, regularisation, annihilator]
---

# Non-Uniqueness of Geophysical Models

## Learning objectives

1. **State** why a finite, noisy, band-limited data set cannot determine a
   continuous source distribution.
2. **Distinguish** measurement error from inherent non-uniqueness: more data do
   not remove the latter.
3. **Construct** an exact null-space vector for a discretised forward operator
   and verify numerically that it leaves the data unchanged.
4. **Explain** the equivalent-stratum and equivalent-source ambiguities with a
   concrete example.
5. **State** what actually selects one model from the equivalence class, and
   why that choice must be reported.

## Prerequisites

- [05-01-01 The Central Idea](./01-physical-property-contrast.md)
- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](./03-resolution-depth-tradeoff.md)

## 1. Intuition: the data constrain the field, not the source

A gravity survey measures $g_z$ on a surface. The map from source distribution
to surface field is an integral operator. Integral operators are *smoothing*:
they average over a volume and they suppress high-wavenumber structure at
depth. Smoothing is not invertible. Infinitely many source distributions
produce exactly the same surface field.

This is not a defect of instruments or of noise. Adding data does not remove it
in principle, because a finite data set has finitely many numbers while a
continuous model has infinitely many. Noise *does* make it worse in practice.

The practical consequence: **"this model fits the data" is a weak claim.** A
model is meaningful only with a statement of the class considered, the
regularisation used, and the prior information applied.

## 2. Precise definitions

**Non-uniqueness (ambiguity).** The existence of distinct models $\mathbf{m}_1
\neq \mathbf{m}_2$ with $F(\mathbf{m}_1) = F(\mathbf{m}_2)$ to within
measurement uncertainty, where $F$ is the forward operator.

**Null space.** The set $\{\mathbf{n} : \mathbf{G}\mathbf{n} = \mathbf{0}\}$ for
a linear discretised operator $\mathbf{G}$. Every null-space vector can be added
to a model without changing the data at all.

**Equivalent stratum.** For a *monopole* (gravity) source, every surface field
can be reproduced exactly by a suitable surface density on a shallower plane.
In two dimensions, a sheet density $\sigma(x)$ at depth $d$ gives

$$g_z(x) = 2G\int \frac{d\,\sigma(x')}{(x-x')^2+d^2}\,dx',$$

whose spatial Fourier transform is $\hat{g}_z(k) = 2\pi G\,e^{-|k|d}\hat\sigma(k)$.
Because the depth enters only through the factor $e^{-|k|d}$, two sheets at
depths $d_1 \neq d_2$ give identical fields whenever
$\hat\sigma_2(k) = \hat\sigma_1(k)\,e^{-|k|(d_1-d_2)}$.

**Annihilator.** A nonzero model perturbation whose data signature is negligible
or exactly zero.

## 3. Derivation: an explicit equivalence and an explicit null space

### 3.1 Equivalent sheets

From the transform relation, if $d_2 < d_1$ (put the equivalent source
*shallower*) then $\hat\sigma_2 = \hat\sigma_1 e^{-|k|(d_1-d_2)}$, a *smoothing*
filter. The shallow equivalent source is therefore a blurred, spread-out
version of the deep one. If instead $d_2 > d_1$, the factor $e^{+|k|(d_1-d_2)}$
amplifies high wavenumbers without bound: the deeper equivalent exists
mathematically but is unstable. **This asymmetry is the whole of the
"downward continuation is unstable" result**, and it explains why equivalent
sources are always built shallow, never deep.

Dimensional check: $|k|$ has units m⁻¹ and $d$ has m, so $|k|d$ is
dimensionless and $e^{-|k|d}$ is dimensionless as required for a filter.

### 3.2 A discrete null space

Discretise: $n_s$ sheet cells, $n_o$ observation points. Then $\mathbf{G}$ is
$n_o \times n_s$. If $n_s > n_o$ and the rows are independent, the null space
has dimension at least $n_s - n_o$. Any right singular vector of $\mathbf{G}$
with a zero singular value is a null vector.

## 4. Units and dimensional analysis

| Symbol | Meaning | SI unit |
|---|---|---|
| $\sigma$ | sheet density | kg m⁻² |
| $k$ | horizontal wavenumber | rad m⁻¹ |
| $\hat{g}_z$ | transform of the anomaly | (m s⁻²) m |
| $\mathbf{G}_{ij}$ | operator entry | m³ s⁻² kg⁻¹ (so $\mathbf{G}\sigma$ is m s⁻²) |

The operator entries follow from $2Gd\,\Delta x/[(x_i-x_j)^2+d^2]$ with
$[G] = \mathrm{m^3kg^{-1}s^{-2}}$, so $\mathbf{G}\mathbf{m}$ carries
m s⁻², an acceleration. This is the check performed inside the demonstration.

## 5. Assumptions

1. **Linearity.** The demonstration uses a linear operator. Nonlinear
   forward operators have a *local* null space (the Jacobian's null space), and
   the ambiguity is usually worse, not better.
2. **A 2-D (sheet) source.** The 3-D equivalent-stratum statement is
   structurally identical with $e^{-|k_z|d}$ replaced by $e^{-|\mathbf{k}|d}$.
3. **Accuracy of the transform argument.** The equivalence is exact only for
   infinite transforms; on a finite grid the tails are truncated, which is why
   the measured mismatch below is not exactly zero.
4. **No prior information.** With a hard bound on density the equivalence class
   shrinks; it does not vanish.

## 6. Worked examples (measured)

Run `code/annihilator_nonuniqueness_demo.py`. Synthetic 2-D model: a Gaussian
sheet at 300 m depth, width 400 m, total mass $10^{10}$ kg per metre of strike,
400 source cells over 12 km, 120 observation points.

**(a) Equivalent sources at other depths fit the data.** Inverting for a sheet
at 100 m gives relative data misfit $1.199\times10^{-15}$ with
$\lVert m - m_\text{true}\rVert/\lVert m_\text{true}\rVert = 0.274$. At 600 m
the misfit is $1.555\times10^{-15}$ and the model difference is 1.309. Two
models at 100 m and 600 m both explain the data to machine precision, and both
differ from the true model and from each other.

**(b) An exact discrete annihilator.** The operator is $120\times400$. All 120
singular values exceed $10^{-12}\sigma_\text{max}$, so the null-space dimension
is at least 280. The last right singular vector $\mathbf{n}$ satisfies

$$\frac{\lVert \mathbf{G}\mathbf{n}\rVert}{\sigma_\text{max}\lVert\mathbf{n}\rVert} = 8.286\times10^{-17},$$

and adding $0.6\,\lVert m_\text{true}\rVert/\lVert n\rVert \cdot \mathbf{n}$ to
the model changes the computed field by a relative $1.311\times10^{-16}$ — while
changing the total mass by only 0.002%. **A large model change with a
non-measurable data change.**

**(c) Why deeper equivalents are unstable.** With 0.02 mGal additive noise, the
condition number of $\mathbf{G}$ grows from 3.33 at 50 m to $8.27\times10^{15}$
at 1200 m, and the recovered model RMS grows from $1.80\times10^{6}$ to
$5.66\times10^{14}$ kg/m². The data misfit stays at $10^{-15}$ for all five
depths (until round-off limits the deepest). **All five models fit the data
equally well; only one is physically plausible.** Fitting the data is not
evidence that a model means anything.

## 7. Python demonstration

`code/annihilator_nonuniqueness_demo.py` prints all three experiments. Predict
which of the five depths in part (c) will produce an absurd density before you
run it. Then ask the harder question: absent prior information, *which* depth
would you report, and on what grounds?

## 8. Exercises, mistakes, applications

Exercises: [`exercises/04-ambiguity-and-nonuniqueness-exercises.md`](./exercises/04-ambiguity-and-nonuniqueness-exercises.md).

**Common mistakes.**

1. **Believing more data removes ambiguity.** More data shrinks the equivalence
   class; it does not make it a point.
2. **Reporting a model without the regularisation.** A minimum-norm solution is
   a *choice* and it must be named.
3. **Confusing non-uniqueness with noise.** Noise gives scatter; the null space
   gives structure that is perfectly reproducible.
4. **Assuming a unique depth.** Depth is among the worst-constrained parameters
   in potential-field inversion — the demonstration shows a 6× depth change
   with a machine-precision fit.
5. **Treating an equivalent source as a real body.** It is a mathematical
   device for continuing or filtering a field, not a geological interpretation.

**Real-world applications.**

- **Deep-crustal gravity modelling** produces smooth, non-unique density
  distributions; published models must state the constraints used (seismic
  velocities, petrophysics).
- **Magnetic depth estimation** relies on the depth rule, which assumes an
  isolated compact source — an assumption that is itself an equivalence-class
  restriction.
- **Borehole-constrained inversion** works precisely because drilling supplies
  the prior information the data lack.
- **Joint inversion** reduces ambiguity by intersecting two equivalence
  classes, which is rarely a single point either
  ([18-07-01](../../18-inverse-problems/07-joint-and-multi-physics-inversion/01-joint-inversion-concepts.md)).

## 9. Further reading

- **Blakely (1995). *Potential Theory in Gravity and Magnetic Applications*.**
  Chapter 9 (equivalent sources, continuation). Level: advanced.
- **Parker, R. L. (1994). *Geophysical Inverse Theory*.** Chapters 1–3. Level:
  graduate. The rigorous statement of what data can and cannot determine.
- **Menke, W. *Geophysical Data Analysis: Discrete Inverse Theory* (any
  edition).** Chapter 1. Level: graduate. The null-space construction in
  Section 3.2 follows this treatment.

## 10. Related lessons

- [05-01-05 Choosing a Method: A Decision Framework](./05-choosing-a-method.md)
- [05-03-03 Superposition and Building Complex Models](../03-forward-modelling-principles/03-superposition.md)
- [18-01-03 Null Space](../../18-inverse-problems/01-inverse-problem-foundations/03-null-space.md)
- [18-03-01 Why Regularise](../../18-inverse-problems/03-regularization/01-why-regularize.md)

## Self-assessment checklist

- [ ] I can explain why a smoothing operator cannot be inverted uniquely.
- [ ] I can derive the equivalent-stratum filter $e^{-|k|\Delta d}$ and check
      its dimensions.
- [ ] I can explain why equivalent sources must be placed shallow.
- [ ] I can construct a null-space vector for a rectangular operator.
- [ ] I can state, for any model I report, what prior information selected it.
