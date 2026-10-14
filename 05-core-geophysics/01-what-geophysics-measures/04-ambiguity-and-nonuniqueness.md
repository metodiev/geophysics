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

### 3.3 The operator is a convolution, so it is a low-pass filter

Write the sheet integral as a convolution. Put the observation at $x$ and the
source at $x'$, and define

$$h(x - x') \;=\; \frac{2Gd}{(x-x')^2+d^2},\qquad\text{so}\qquad
g_z(x) = \int_{-\infty}^{\infty} h(x-x')\,\sigma(x')\,\mathrm{d}x'.$$

Units of the kernel: $[G] = \mathrm{m^3\,kg^{-1}\,s^{-2}}$ and
$[d/\text{length}^2] = \mathrm{m^{-1}}$, so
$[h] = \mathrm{m^2\,kg^{-1}\,s^{-2}}$; then $[h\sigma] =
\mathrm{m^2kg^{-1}s^{-2}\cdot kg\,m^{-2}} = \mathrm{s^{-2}}$ per metre of
integration, i.e. $\mathrm{m\,s^{-2}}$ — an acceleration. ✓

Now take the Fourier transform $\hat{g}(k) = \int g_z(x)e^{-ikx}\,\mathrm{d}x$.
Because a convolution transforms to a product,

$$\hat{g}_z(k) = \hat{h}(k)\,\hat\sigma(k).$$

We need $\hat{h}(k)$. Since $h = 2G\,d/(x^2+d^2)$, compute

$$I(k) = \int_{-\infty}^{\infty}\frac{d\,e^{-ikx}}{x^2+d^2}\,\mathrm{d}x .$$

The integrand has simple poles at $x = \pm id$. Take $k>0$: the factor
$e^{-ikx} = e^{-i k\,\mathrm{Re}\,x}\,e^{k\,\mathrm{Im}\,x}$ decays as
$\mathrm{Im}\,x\to-\infty$, so close the contour in the **lower** half-plane,
clockwise, enclosing $x=-id$. Its residue is

$$\operatorname*{Res}_{x=-id}\frac{d}{(x-id)(x+id)}
= \frac{d}{-id-id} = \frac{d}{-2id} = \frac{i}{2}.$$

Evaluate the exponential at the pole: $e^{-ik(-id)} = e^{-kd}$. Closing clockwise
contributes $-2\pi i$ times the residue, so

$$I(k) = -2\pi i \cdot \frac{i}{2}\,e^{-kd} = \pi e^{-kd}\qquad (k>0).$$

For $k<0$ the decay is in the upper half-plane and the same calculation returns
$\pi e^{+kd}$. Combining, and restoring the factor $2G$,

$$\boxed{\;\hat{h}(k) = 2\pi G\,e^{-|k|d}\;}\qquad\Longrightarrow\qquad
\hat{g}_z(k) = 2\pi G\,e^{-|k|d}\,\hat\sigma(k).$$

**Physical interpretation.** The factor $e^{-|k|d}$ is the whole story. It is
real and positive, so it introduces **no phase shift** — the field is in phase
with the source, unlike a wave — and it decays exponentially in $|k|d$. The
operator is therefore a **low-pass filter whose cutoff is set by depth**:

- at long wavelength ($|k|d \ll 1$) the factor is $\approx 1$: the field carries
  nearly all the source's amplitude;
- at $|k| = 1/d$ the factor is $e^{-1} = 0.368$;
- at $|k|d \gg 1$ the factor is exponentially small.

The cut-off is not a property of the instrument, the survey, or the processing.
It is $\nabla^2\Phi = 0$ written in the wavenumber domain.

### 3.4 How fine a feature can the field contain? Two independent answers

**Answer 1, from the filter.** Ask at what wavelength the transfer function has
fallen to one tenth: $e^{-2\pi d/\lambda} = 0.1$, so $2\pi d/\lambda = \ln 10 =
2.3026$ and

$$\lambda_{10} = \frac{2\pi}{\ln 10}\,d = 2.729\,d .$$

The field contains essentially nothing shorter than this. The finest *feature*
resolvable is about half a wavelength, so the finest resolvable structure is
$\approx 1.36\,d$.

**Answer 2, from the anomaly half-width** (derived independently in
[05-01-03](./03-resolution-depth-tradeoff.md) by solving $g(x) = \tfrac12g(0)$):
$w_{1/2} = 2\sqrt{2^{2/3}-1}\,d = 1.533\,d$.

$$\frac{1.533}{1.364} = 1.124 .$$

Two derivations that share no algebra — one in the wavenumber domain, one in the
space domain — agree to **12%** on a statement of the form "resolution is
proportional to depth, with a constant of order 1.5". This is the kind of
agreement that makes a physical scaling credible; it is also why the constant
may be quoted loosely while the *proportionality* may not be violated.

### 3.5 Which direction of continuation is stable

Return to the equivalence. Two sheets at depths $d_1$ and $d_2$ produce identical
fields when, for every $k$,

$$e^{-|k|d_1}\hat\sigma_1(k) = e^{-|k|d_2}\hat\sigma_2(k)
\qquad\Longrightarrow\qquad
\hat\sigma_2(k) = \hat\sigma_1(k)\,e^{-|k|(d_1-d_2)} .$$

Read the exponent as a direction:

- **$d_2 < d_1$ (equivalent source is *shallower*).** The exponent
  $-|k|(d_1-d_2)$ is negative, so the factor decays in $|k|$: the equivalent
  source is a *smoothed* version of the original. The operation is stable — it
  loses information but does not amplify anything.
- **$d_2 > d_1$ (equivalent source is *deeper*).** The exponent is positive, so
  the factor is $e^{+|k|(d_2-d_1)}$ and it grows without bound in $|k|$. The
  operation is unstable.

**Quantify the instability.** Downward continuation by $\Delta d$ multiplies a
wavenumber-$k$ component by $e^{|k|\Delta d} = e^{2\pi\Delta d/\lambda}$. For
$\Delta d = 300$ m:

| $\lambda$ (m) | $e^{2\pi\Delta d/\lambda}$ |
|---|---|
| 1000 | $6.59$ |
| 500 | $43.4$ |
| 200 | $1.23\times10^{4}$ |
| 100 | $1.53\times10^{8}$ |

So a 1% error in the data becomes a **123-times** error in the model at
$\lambda = 200$ m, and $1.53\times10^{6}$ times at 100 m. This is why every
downward-continuation routine is regularised, and why the regularisation weight
must be reported: it is the only thing standing between noise and the answer.

### 3.6 The discrete null space, derived

Discretise the sheet into $n_s$ cells and observe at $n_o$ points. Then
$\mathbf{g} = \mathbf{G}\boldsymbol{\sigma}$ with $G_{ij}$ as in
[05-03-01](../03-forward-modelling-principles/01-forward-problem.md):

$$G_{ij} = \frac{2G\,d\,\Delta x}{(x_i-x_j)^2+d^2},\qquad
[G_{ij}] = \mathrm{m^3\,kg^{-1}\,s^{-2}} .$$

By rank–nullity, $\dim\ker\mathbf{G} = n_s - \operatorname{rank}\mathbf{G}$. If
the $n_o$ rows are linearly independent then $\operatorname{rank} =
n_o = \min(n_o,n_s)$, so for $n_s > n_o$

$$\dim\ker\mathbf{G} = n_s - n_o .$$

With $n_o = 120$ and $n_s = 400$, $\dim\ker\mathbf{G} = 280$. In the singular
value decomposition $\mathbf{G} = \mathbf{U}\boldsymbol{\Sigma}\mathbf{V}^{\!\top}$,
the null space is spanned by the columns of $\mathbf{V}$ whose singular values
vanish. Numerically "vanish" means $\sigma_i \le \epsilon\,\sigma_{\max}$ with
$\epsilon$ of order the working precision times the conditioning; the
demonstration checks this and finds all 120 singular values above
$10^{-12}\sigma_{\max}$, confirming rank 120 and null dimension exactly 280.

The consequence is immediate: for any null vector $\mathbf{n}$ and any scalar
$\alpha$,

$$\mathbf{G}(\boldsymbol{\sigma} + \alpha\mathbf{n}) =
\mathbf{G}\boldsymbol{\sigma} + \alpha\,\mathbf{G}\mathbf{n} =
\mathbf{G}\boldsymbol{\sigma} .$$

**The data are identical, for every $\alpha$, including $\alpha\to\infty$.**
The only bound on $\alpha$ is physical plausibility, which is prior
information — not data.

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

**Each assumption, what breaks when it fails, and by how much.**

### 5.1 Linearity

*What it buys:* superposition, hence a matrix operator and the whole linear
algebra of Sections 3.6 and 6.

*What breaks:* for gravity it never breaks — Newtonian gravity in a density field
is exactly linear, and the demonstration's factor-of-$10^{15}$ misfits confirm
that the implementation is not the limitation. For magnetics with high
susceptibility, the self-demagnetising field makes
$\chi_\text{eff} = \chi/(1+\chi/3)$ for a sphere, an error of $1+\chi/3$
(i.e. 17% at $\chi = 0.5$) — quantified in
[05-03-03](../03-forward-modelling-principles/03-superposition.md).

### 5.2 Two dimensions

*What it buys:* the scalar kernel $2Gd/((x-x')^2+d^2)$ and the one-dimensional
transform of Section 3.3, which is what makes the derivation elementary.

*What breaks:* nothing structural. In three dimensions the kernel is the same
function of $|\mathbf{k}| = \sqrt{k_x^2+k_y^2}$:

$$\hat{g}_z(\mathbf{k}) = 2\pi G\,e^{-|\mathbf{k}|d}\,\hat\sigma(\mathbf{k}),$$

a convolution with the *same* exponential low-pass factor. Every conclusion about
the equivalence class, the stable direction and the null space carries over with
$|k|\to|\mathbf{k}|$. Note only that a 3-D body also decays faster with distance
in the space domain ($r^{-2}$ for a point mass, as against $r^{-1}$ for a line),
which narrows the anomaly but does not change the depth-controlled cutoff.

### 5.3 Finite truncation of the transform

*What it buys:* a computable, finite matrix.

*What breaks:* the demonstration's sheet has width 400 m inside a 12 km window,
so its amplitude at the window edge is
$\exp\!\left[-\tfrac12(6000/400)^2\right] = e^{-112.5}$, which is zero to every
representable precision. **The truncation is harmless here by construction, and
that is an assumption worth stating rather than a result to generalise.** A sheet
that filled the window (a uniform layer) would not be compact, the convolution
would be periodic, and the finite window would introduce a genuine edge
artefact. The honest statement is: *"for a source compact relative to the model
window, truncation is negligible; the demonstration's measured misfit of
$1.2\times10^{-15}$ is a check of that, not of truncation in general."*

### 5.4 No prior information

*What it buys:* the clean statement that infinitely many models fit.

*What breaks:* the statement itself, once a bound exists. A hard constraint
$0 \le \rho \le \rho_{\max}$ restricts $\alpha$ in
$\boldsymbol{\sigma} + \alpha\mathbf{n}$, and a depth constraint removes the
100 m and 600 m alternatives outright. Prior information does not restore
uniqueness; it *shrinks the equivalence class* to a set that may or may not be
useful. Reporting the class — for example the range of depths consistent with the
data at a stated misfit — is more honest than reporting its minimum-norm member.

### 5.5 Round-off

*What it buys:* the machine-precision misfits quoted above.

*What breaks:* at 1200 m depth the conditioning reaches $8.27\times10^{15}$.
Since $1/\epsilon_\text{mach} \approx 4.5\times10^{15}$ for double precision,
the solve can no longer satisfy the data at all, and the demonstration's misfit
degrades from $1.3\times10^{-15}$ to $1.0\times10^{-4}$ — a **ten-order-of-magnitude**
loss of fit, purely numerical, while the "model" reaches an absurd RMS of
$5.66\times10^{14}$ kg/m². The practical rule: a condition number approaching the
reciprocal of machine epsilon marks the point past which the linear algebra,
not the physics, is deciding the answer.

### 5.6 What actually selects a model

Collecting the above, the ordering of influence is:

1. **Prior information** (depth from a borehole, density bounds, geological
   plausibility) — the only thing that can exclude a member of the class;
2. **regularisation** (which member of the class the algorithm returns);
3. **the data** (which class, i.e. the misfit level, not the point);
4. **the discretisation** (how the class is parameterised).

A model without an explicit statement of items 1 and 2 is not a result.

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

**The two shortcuts that fail, with the arithmetic.**

### 6.1 "The misfit is at machine precision, so the model is right"

The demonstration fits the same synthetic data with sheets at three depths:

| assumed depth | relative data misfit | model error vs truth |
|---|---|---|
| 100 m | $1.199\times10^{-15}$ | $0.274$ |
| 300 m (truth) | $1.573\times10^{-15}$ (measured) | $0$ |
| 600 m | $1.555\times10^{-15}$ | $1.309$ |

The 100 m and 600 m models are wrong by **27%** and **131%** of the true model
norm, judged by the quantity a practitioner usually looks at first. All three
misfits are at the round-off floor; two of them are wrong.

The arithmetic of why: a sheet at the wrong depth has a *broader or narrower*
kernel, and a compensating density profile exists that makes the convolutions
agree. Because the kernel is a smooth low-pass filter (Section 3.3), the
compensation is always possible for the wavenumbers present in the data. The
misfit measures how well the model explains *the band-limited field*, and nothing
else.

### 6.2 "I will report the minimum-norm model"

The minimum-norm model is a legitimate choice, but it is a *choice*, and the
demonstration shows how large the alternative space is. Build a null vector
$\mathbf{n}$ from the last right singular vector and add
$\alpha\mathbf{n}$ with $\alpha = 0.6\,\lVert\boldsymbol{\sigma}_\text{true}\rVert
/ \lVert\mathbf{n}\rVert$. Then

$$\frac{\lVert\boldsymbol{\sigma}_\text{alt} - \boldsymbol{\sigma}_\text{true}\rVert}
{\lVert\boldsymbol{\sigma}_\text{true}\rVert} = 0.6,\qquad
\frac{\lVert\mathbf{G}\boldsymbol{\sigma}_\text{alt} -
\mathbf{G}\boldsymbol{\sigma}_\text{true}\rVert}
{\lVert\mathbf{G}\boldsymbol{\sigma}_\text{true}\rVert} = 1.311\times10^{-16},$$

and the ratio that matters for interpretation, total mass, barely moves:

$$\frac{\sum_j\boldsymbol{\sigma}_{\text{alt},j}\,\Delta x}{\sum_j
\boldsymbol{\sigma}_{\text{true},j}\,\Delta x} = \frac{1.0002\times10^{10}}
{1.0000\times10^{10}} = 1.0002 .$$

**A 60% change in the model norm for a data change of $1.3\times10^{-16}$ and a
mass change of 0.02%.** The model changed almost entirely in a direction the
data cannot see; the interpretable integral changed almost not at all. This is
the shape of non-uniqueness: large in model space, invisible in data space,
often small in *integrated* quantities — but not always, which is why integrated
quantities must be checked case by case rather than assumed safe.

### 6.3 Worked arithmetic: how much does the filter suppress?

At $d = 300$ m, $\hat{h}(k) = 2\pi G e^{-2\pi d/\lambda}$:

| $\lambda$ (m) | $2\pi d/\lambda$ | transfer magnitude |
|---|---|---|
| 1000 | 1.885 | 0.152 |
| 2000 | 0.942 | 0.390 |
| 5000 | 0.377 | 0.686 |
| 10000 | 0.188 | 0.828 |
| 20000 | 0.094 | 0.910 |

A 20 km feature passes at 91% of its source amplitude while a 1 km feature passes
at 15%. **Six times less information in the amplitude alone at a wavelength
20 times shorter**, before any consideration of the noise floor — and the
recoverable band is narrower still in the inverse problem, because the inverse
amplifies what the forward suppressed.

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
