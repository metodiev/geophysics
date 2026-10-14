---
id: 06-03-03
title: "Moment Tensors, Decomposition and Physical Meaning"
level: doctoral
prereqs: ["06-03-02", "06-01-05"]
tags: [seismology, moment-tensor, decomposition, clvd, moment-magnitude]
---

# Moment Tensors, Decomposition and Physical Meaning

> **All models and data in this module are SYNTHETIC.** Every tensor, eigenvalue
> and magnitude below is computed by
> [`code/moment_tensor_demo.py`](code/moment_tensor_demo.py) from chosen teaching
> tensors. No observed moment tensor, event or catalogue magnitude is quoted.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the moment tensor as a volume integral of a force-couple density
   and **explain** why it has six independent components.
2. **Derive** the three principal axes from the eigenvalue problem and
   **compute** the scalar moment $M_0 = (\lambda_1-\lambda_3)/2$.
3. **Decompose** an arbitrary tensor into isotropic, double-couple and
   compensated-linear-vector-dipole parts, and **compute** the CLVD strength
   $\varepsilon = -\lambda_2/\max(|\lambda_1|,|\lambda_3|)$.
4. **Prove** that the three parts are mutually orthogonal under the Frobenius
   inner product, and **verify** the reconstruction to machine precision.
5. **Convert** a scalar moment to moment magnitude using the exact offset in
   SI units, and **quantify** the $0.0367$-unit error introduced by the commonly
   quoted rounded offset.
6. **Distinguish** an algebraic identity from its floating-point realisation, by
   **interpreting** a printed trace that sits at the round-off floor.
7. **State** what a moment tensor inversion does and does not determine, and why
   a CLVD is a modelling statement rather than a physical object.

## Prerequisites

- [06-03-02 The Double-Couple Source and Radiation Patterns](02-double-couple.md) —
  the special tensor out of which the general one is built.
- [06-01-05 Helmholtz Decomposition and Wavefield Potentials](../01-elastic-wave-propagation/05-wavefield-potentials.md) —
  the potentials from which the representation theorem is built.

## 1. Intuition: a source is a small machine, not a picture

A double couple is one point in a larger family. If a patch of rock opens, or if
a crack closes, or if a fault slips while the volume around it simultaneously
contracts, the radiated field is no longer that of a pure double couple. To
describe all of these with one object we need the **moment tensor**: nine
numbers (six independent) that say, for each pair of coordinate directions, how
much force-couple strength the source applied.

The moment tensor is not a picture of the fault. It is the source term of an
elastic wave equation, and everything observable — amplitudes, polarities,
spectra — is produced from it by a linear operator. That makes the *inverse*
problem (infer $M$ from data) harder than the forward problem, and it means every
number in this lesson is a property of a model, not a measurement.

This lesson does three things: it defines $M$, it decomposes $M$ into parts with
distinct physical meanings, and it shows that the decomposition is an identity —
so exact that the only numbers in the demo that are *not* properties of the
source are the residuals of the arithmetic.

## 2. Precise definitions

The moment tensor is the volume integral of the force-couple density
$m_{ij}(\xi)$ over the source volume $\Omega$:

$$M_{ij} = \iiint_\Omega m_{ij}(\xi)\,\mathrm{d}V \qquad (\mathrm{N\,m}).$$

It enters the far-field displacement through the representation theorem,

$$u_i(x,t) = M_{jk}\int_\Omega \frac{\partial G_{ij}}{\partial \xi_k}(x,\xi;t)
\;*\; \dot s(t)\,\mathrm{d}V,$$

where $G_{ij}$ is the Green's function of the medium and $s(t)$ is the source
time function (the subject of
[04 Source Time Functions](04-source-time-function.md)). The important structure
is the separation: $M$ carries the **geometry and strength** of the source, $G$
carries the **medium**, and $\dot s$ carries the **timing**.

Frame: $x$ = North, $y$ = East, $z$ = Down. The six independent components are
$M_{xx}, M_{yy}, M_{zz}, M_{xy}, M_{xz}, M_{yz}$; symmetry $M_{ij} = M_{ji}$ holds
because a source cannot apply a net torque.

Derived invariants used in this lesson:

| Quantity | Definition | Meaning |
|---|---|---|
| $M_{\text{iso}}$ | $\tfrac13 \mathrm{tr}(M)$ | mean isotropic (volume-changing) strength |
| $M'$ | $M - M_{\text{iso}}I$ | deviatoric (volume-preserving) part |
| $\lambda_1\ge\lambda_2\ge\lambda_3$ | eigenvalues of $M'$ | principal deviatoric strengths, $\sum\lambda_i = 0$ |
| $M_0$ | $\tfrac12(\lambda_1-\lambda_3)$ | scalar moment |
| $\varepsilon$ | $-\lambda_2/\max(\lvert\lambda_1\rvert,\lvert\lambda_3\rvert)$ | CLVD strength, $-1/2\le\varepsilon\le1/2$ |

## 3. Derivations

### 3.1 Why six components, and what each is

A general $3\times3$ tensor has $9$ components. Symmetry removes $3$, leaving
$6$. Physically, $M_{ij}$ is the $i$-th component of a force couple acting on the
$j$-th face of a unit cube: $M_{xy}$, for example, is a pair of forces in the
$x$ direction separated along $y$ (a strike-slip couple on a vertical fault
striking east–west). The diagonal entries are couples whose force and separation
are along the same axis; their sum $\mathrm{tr}(M)$ is three times the isotropic
part, and it is the only combination that changes volume.

*Numerical check (SYNTHETIC).* For strike 32, dip 63, rake $-41$ and
$M_0 = 3.4\times10^{18}\ \mathrm{N\,m}$, the demo prints

$$M_{xx} = -1.548187\times10^{18},\quad
M_{yy} = +3.352781\times10^{18},\quad
M_{zz} = -1.804594\times10^{18},$$
$$M_{xy} = +1.912837\times10^{17},\quad
M_{xz} = -1.682714\times10^{18},\quad
M_{yz} = +4.945609\times10^{17}.$$

The demo reports $\max|M - M^{\mathsf T}| = 0$ exactly: symmetry is built into the
construction, so the check is trivially satisfied and is printed only to make the
claim explicit.

### 3.2 The eigenvalue problem and the scalar moment

Diagonalising $M$ gives three orthogonal principal axes and their signed
strengths. Two facts are worth stating precisely:

- The **trace is invariant**: $\mathrm{tr}(M) = \sum_i \lambda_i$, for the full
  tensor. A source with $\mathrm{tr}(M)>0$ expands the material (an explosion),
  $\mathrm{tr}(M)<0$ contracts it (an implosion), and $\mathrm{tr}(M)=0$ is
  volume-preserving.
- The **scalar moment** is half the range of the deviatoric eigenvalues,
  $M_0 = \tfrac12(\lambda_1-\lambda_3)$.

*Numerical check (SYNTHETIC).* The demo prints eigenvalues
$+3.400000\times10^{18}$, $-4.824072\times10^{2}$ and
$-3.400000\times10^{18}$, and then $M_0 = \tfrac12(\lambda_1-\lambda_3)
= 3.400000\times10^{18}\ \mathrm{N\,m}$ — the value used to build the tensor.

**A caution about the trace line.** The demo prints a trace of
$+2.56\times10^{2}\ \mathrm{N\,m}$ and an eigenvalue sum of
$-5.12\times10^{2}\ \mathrm{N\,m}$. These *must* be equal algebraically, and
they are not, because the source is constructed to be traceless and both numbers
are round-off. The spacing of double-precision numbers near
$3.4\times10^{18}$ is $2^{9} = 512\ \mathrm{N\,m}$, so both printed values lie
below one unit in the last place of the largest component
($512/3.4\times10^{18} \approx 1.5\times10^{-16}$). The two numbers differ
because one is a direct sum of diagonal entries and the other is a sum of
eigenvalues whose intermediate partial sums cancel; the rounding differs.
**Neither number is a property of the source.** This is the general lesson: an
identity verified to $10^{-16}$ is verified, and a violation of $10^{-16}$ is
also verified.

The middle eigenvalue $-4.824072\times10^{2}$ is the same kind of artefact. As a
CLVD strength it would give $\varepsilon \approx 4.824\times10^{2}/3.4\times10^{18}
= 1.4\times10^{-16}$, i.e. the source is a double couple to machine precision.

### 3.3 Isotropic plus deviatoric

Split $M$ into a volume-changing and a volume-preserving part:

$$M_{\text{iso}} = \frac{\mathrm{tr}(M)}{3}I,
\qquad M' = M - M_{\text{iso}}, \qquad \mathrm{tr}(M') = 0.$$

This split is **orthogonal** under the Frobenius inner product
$A:B = \sum_{ij}A_{ij}B_{ij}$, because
$M_{\text{iso}}:M' = M_{\text{iso}}\mathrm{tr}(M') = 0$. The demo verifies both
cosines: $\cos(M_{\text{iso}},I) = +1.000$ and
$\cos(M-M_{\text{iso}},I) = -4.18\times10^{-17}$.

### 3.4 The DC / CLVD decomposition

Work in the eigenbasis of $M'$, where $M' = \mathrm{diag}(\lambda_1,\lambda_2,
\lambda_3)$ with $\lambda_1\ge\lambda_2\ge\lambda_3$ and $\sum\lambda_i = 0$.
Define

$$M_0^{\text{dc}} = \frac{\lambda_1-\lambda_3}{2},\qquad
M^{\text{dc}} = M_0^{\text{dc}}\begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix},\qquad
M^{\text{clvd}} = \lambda_2\begin{pmatrix}-\tfrac12&0&0\\0&1&0\\0&0&-\tfrac12\end{pmatrix}.$$

Adding the three diagonal entries of $M^{\text{dc}}+M^{\text{clvd}}$ and using
$\lambda_1+\lambda_2+\lambda_3 = 0$:

$$\text{entry }1:\ M_0^{\text{dc}} - \tfrac{\lambda_2}{2}
= \frac{\lambda_1-\lambda_3-\lambda_2}{2} = \frac{\lambda_1+\lambda_1}{2} = \lambda_1,$$
$$\text{entry }2:\ \lambda_2, \qquad
\text{entry }3:\ -M_0^{\text{dc}} - \tfrac{\lambda_2}{2} = \lambda_3.$$

So the three-term decomposition is the identity

$$\boxed{\;M = \underbrace{M_{\text{iso}}}_{\text{volume}}
+ \underbrace{M^{\text{dc}}}_{\text{shear}}
+ \underbrace{M^{\text{clvd}}}_{\text{non-shear deviatoric}},\;}$$

with $\varepsilon = -\lambda_2/\max(|\lambda_1|,|\lambda_3|)\in[-1/2,1/2]$.
Check the two extremes: a pure double couple has $\lambda = (a,0,-a)$, so
$\varepsilon = 0$; a pure CLVD with $\lambda = (2,-1,-1)a/3$ has
$\varepsilon = -(-1)/(2) = +1/2$. That is why $|\varepsilon| = 1/2$ is called
"pure CLVD".

*Numerical check.* The demo's table, reproduced from the run:

| source | $M_{\text{iso}}/\max\lvert M_{ij}\rvert$ | $M_0^{\text{dc}}$ (N m) | CLVD $\varepsilon$ | residual$/\max\lvert M_{ij}\rvert$ |
|---|---|---|---|---|
| pure double couple | $-0.000000$ | $1.0000\times10^{19}$ | $0.0000$ | $4.15\times10^{-16}$ |
| pure CLVD ($\lambda = 2,-1,-1$) | $0.000000$ | $1.0000\times10^{19}$ | $0.5000$ | $7.68\times10^{-17}$ |
| explosion, $M_{\text{iso}} = 10^{19}$ | $1.000000$ | $0$ | $0.0000$ | $0.00\times10^{0}$ |
| isotropic + DC | $0.336744$ | $2.0000\times10^{19}$ | $0.0000$ | $1.38\times10^{-16}$ |
| isotropic + CLVD | $0.272727$ | $1.0000\times10^{19}$ | $0.5000$ | $2.79\times10^{-17}$ |

Note the column heading. The demo's printed label is "M_iso/||M||", but the
quantity it evaluates is $M_{\text{iso}}/\max|M_{ij}|$, the isotropic scalar
divided by the **largest single component** — not the Frobenius norm. With that
reading the explosion row is exactly $1$ (the whole tensor is isotropic) and the
isotropic+DC row is $10^{19}/2.9696\times10^{19} = 0.336745$, as printed.

### 3.5 The three parts are orthogonal projections

In the deviatoric eigenbasis the two patterns are $D_{\text{dc}} =
\mathrm{diag}(1,0,-1)$ and $D_{\text{clvd}} = \mathrm{diag}(-\tfrac12,1,-\tfrac12)$.
Then

$$D_{\text{dc}}:D_{\text{clvd}} = (1)(-\tfrac12) + (0)(1) + (-1)(-\tfrac12)
= -\tfrac12 + 0 + \tfrac12 = 0.$$

Both are traceless: $\mathrm{tr}(D_{\text{dc}}) = 0$ and
$\mathrm{tr}(D_{\text{clvd}}) = -\tfrac12 + 1 - \tfrac12 = 0$. Their squared norms
are $\lVert D_{\text{dc}}\rVert^2 = 1+0+1 = 2$ and
$\lVert D_{\text{clvd}}\rVert^2 = \tfrac14+1+\tfrac14 = \tfrac32$. Two orthogonal
traceless basis tensors in a two-dimensional deviatoric-eigenvalue space (the
third direction is fixed by $\sum\lambda=0$): **every deviatoric moment tensor is
a point on the line segment between them.**

The demo verifies this numerically: $\cos(M^{\text{dc}},M^{\text{clvd}})
= +0.00\times10^{0}$, $\cos(M_{\text{iso}},M^{\text{dc}})
= +9.64\times10^{-17}$, $\cos(M_{\text{iso}},M^{\text{clvd}})
= -2.93\times10^{-17}$, $\mathrm{trace}(M^{\text{dc}})/\max|M|
= +1.73\times10^{-16}$, $\mathrm{trace}(M^{\text{clvd}})/\max|M|
= -4.79\times10^{-33}$, and the Pythagorean residual
$\bigl(\lVert M\rVert^2 - \sum_{\text{parts}}\lVert\cdot\rVert^2\bigr)/
\lVert M\rVert^2 = -3.56\times10^{-16}$.

### 3.6 Scalar moment to moment magnitude, exactly

Hanks & Kanamori's definition, as published, uses cgs units:

$$M_{\mathrm w} = \tfrac23\log_{10}\!\left(M_0\,[\mathrm{dyn\,cm}]\right) - 10.7.$$

Convert exactly with $1\ \mathrm{N\,m} = 10^{7}\ \mathrm{dyn\,cm}$:

$$\tfrac23\log_{10}\!\left(M_0[\mathrm{N\,m}]\times10^{7}\right) - 10.7
= \tfrac23\log_{10}M_0[\mathrm{N\,m}] + \tfrac{14}{3} - 10.7
= \tfrac23\log_{10}M_0[\mathrm{N\,m}] - 6.033333.$$

The value usually written is $-6.07$, which differs by
$\Delta = 0.0367$ magnitude units. A difference of $\Delta$ in magnitude is a
factor $10^{1.5\Delta} = 10^{0.05505} = 1.1350$ in moment. The demo prints both
offsets, the difference, and the factor.

## 4. Physical interpretation

**Isotropic part.** $M_{\text{iso}}>0$ is a volume increase — an explosion or a
rapid phase change — and it radiates compression in *every* direction, with no
nodal planes at all. This is the basis of the polarity discriminant in
[07 Discriminating Explosions from Earthquakes](07-nuclear-explosion-sources.md).

**Deviatoric part.** Volume-preserving; this is what a shear fault produces.
A pure double couple is the extreme member with $\varepsilon = 0$; it is what
elastic slip on a plane gives.

**CLVD part.** Compensated linear vector dipole: a deviatoric pattern that is
*not* a double couple. It has one principal axis of one sign and two of the
other, with the two equal ones opposite in sign to the third. Physically it is
what a source with a changing aspect ratio produces — a tensile crack opening
rapidly, or a volume change that is not isotropic because the surrounding medium
is not symmetric. **Its value in a reported tensor is not a measurement of a
physical CLVD.** It absorbs (i) genuine non-double-couple radiation, (ii)
anisotropy or heterogeneity near the source that the double-couple model
mislabels, (iii) noise and (iv) the effect of a finite source that the point
model cannot represent. A large $|\varepsilon|$ is therefore a *discrepancy
flag*, and its interpretation requires more data, not more algebra.

**$M_0$ is the size; $\varepsilon$ is the shape.** $M_0$ carries the moment and
hence the energy scale; $\varepsilon$ and $M_{\text{iso}}$ describe the nature of
the source. Neither is independent of the assumed source model, and neither is
observed directly.

## 5. Assumptions and regime of validity

1. **Point source, far field.** $M$ is the leading term in a multipole
   expansion. Its validity requires $r \gg$ source dimension; a finite source
   radiates a directional pattern that no single tensor reproduces
   ([04](04-source-time-function.md)).
2. **Linear elasticity and a known Green's function.** The tensor is only as good
   as the velocity model used to compute $G$.
3. **Instantaneous and complete.** $\dot s(t)$ is separated from $M$; if the
   source time function is wrong, the inverted $M$ absorbs the error.
4. **Individual components are frame-dependent.** $M_{xx}, M_{xy}, \ldots$ change
   when the coordinate frame rotates; only the invariants
   ($\mathrm{tr}M$, $\lambda_i$, $M_0$, $\varepsilon$) do not.
5. **The decomposition is an identity, the interpretation is not.** Sections
   3.3–3.5 are exact algebra valid for any symmetric tensor. Calling the parts
   "volume change", "shear" and "tensile" is a physical model.
6. **Magnitude is a convention.** $M_{\mathrm w}$ depends on the stated offset
   and on the unit inside the logarithm. Quoting $M_{\mathrm w}$ without the
   offset is quoting a number with a $0.04$-unit ambiguity.

**Non-uniqueness to keep in view.** An inversion returns one tensor that fits the
data under the assumptions; a rotated source and an anisotropic medium can
produce the same data, and both are *outside* the assumed model. The residual of
a moment-tensor inversion is therefore a lower bound on the true mismatch.

## 6. Units and dimensional analysis

| Quantity | Unit | Note |
|---|---|---|
| $M_{ij}$ | $\mathrm{N\,m}$ | energy per unit strain; equals $\mathrm{J}$ dimensionally |
| $M_{\text{iso}}$ | $\mathrm{N\,m}$ | $\mathrm{tr}(M)/3$ has the same units as $M$ |
| $M_0$ | $\mathrm{N\,m}$ | eigenvalue difference, so $\mathrm{N\,m}$ |
| $\varepsilon$, $\cos$, fractions | — | ratios of like quantities |
| $M_{\mathrm w}$ | — | $M_0$ enters through a logarithm, so the *unit* must be stated |
| $\dot M_0$ | $\mathrm{N\,m\,s^{-1}}$ | used in [01](01-faulting-and-slip.md) |

A dimensional check on the logarithm: $\log_{10}$ requires a dimensionless
argument, which is exactly why the unit ($\mathrm{dyn\,cm}$ or $\mathrm{N\,m}$)
must be written inside the formula. Dropping it changes $M_{\mathrm w}$ by
$(2/3)\log_{10}(10^{7}) = 4.667$, a catastrophic error.

## 7. Worked examples

### Example 1 — invariants of the demo tensor

From the printed eigenvalues $\lambda_1 = +3.4\times10^{18}$,
$\lambda_3 = -3.4\times10^{18}$:

$$M_0 = \tfrac12\left(3.4\times10^{18} - (-3.4\times10^{18})\right)
= 3.4\times10^{18}\ \mathrm{N\,m},$$

matching the value used to build the tensor. The middle eigenvalue gives
$\varepsilon \approx 1.4\times10^{-16}$: this source is a pure double couple to
within double precision.

### Example 2 — decompose a simple tensor by hand

Take $M = \mathrm{diag}(3,-1,-2)\times10^{19}\ \mathrm{N\,m}$.

1. Isotropic part: $\mathrm{tr}M = (3-1-2)\times10^{19} = 0$, so
   $M_{\text{iso}} = 0$ — already deviatoric.
2. Order $\lambda = (3,-1,-2)\times10^{19}$.
3. $M_0^{\text{dc}} = \tfrac12(3-(-2))\times10^{19} = 2.5\times10^{19}\ \mathrm{N\,m}$.
4. $M^{\text{clvd}}$ coefficient $\lambda_2 = -1\times10^{19}$,
   $\varepsilon = -(-1)/\max(3,2) = +1/3 \approx 0.3333$.
5. Reconstruct:
   $M^{\text{dc}} = \mathrm{diag}(2.5,0,-2.5)\times10^{19}$,
   $M^{\text{clvd}} = \mathrm{diag}(0.5,-1,0.5)\times10^{19}$;
   the sum is $\mathrm{diag}(3.0,-1.0,-2.0)\times10^{19}$ ✔.

**Reading.** About a third of this source's deviatoric strength is non-double-couple.
A tensor like this from an inversion would be flagged for scrutiny.

### Example 3 — the magnitude offset in practice

For $M_0 = 10^{19}\ \mathrm{N\,m}$:

$$M_{\mathrm w}^{\text{exact}} = \tfrac23(19) - 6.033333 = 12.6667 - 6.0333 = 6.6333,$$
$$M_{\mathrm w}^{\text{quoted}} = \tfrac23(19) - 6.07 = 6.5967.$$

Difference $0.0367$ — the same for every moment, because the two formulas differ
only by a constant. The demo tabulates it for $10^{15}$, $10^{18}$, $10^{19}$,
$10^{21}$ and $10^{23}$.

To change $M_{\mathrm w}$ by $0.1$ you need a moment factor
$10^{1.5\times0.1} = 10^{0.15} = 1.4125$: $M_0 = 1.4125\times10^{19}\ \mathrm{N\,m}$
raises $6.6333$ to $6.7333$.

### Example 4 — orthogonality of the two basis tensors

$$D_{\text{dc}}:D_{\text{clvd}}
= (1)\!\left(-\tfrac12\right) + (0)(1) + (-1)\!\left(-\tfrac12\right) = 0,$$
$$\lVert D_{\text{dc}}\rVert^2 = 2,\qquad \lVert D_{\text{clvd}}\rVert^2
= \tfrac32.$$

The two are non-parallel, orthogonal and both traceless: they span the full
two-dimensional space of deviatoric *eigenvalue* patterns (a third direction in
the three-dimensional traceless space is fixed by the sum rule). This is why the
demo can say every deviatoric tensor is a point on the line between them.

## 8. Python demonstration

[`code/moment_tensor_demo.py`](code/moment_tensor_demo.py):

```bash
cd 06-seismology/03-earthquake-sources/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moment_tensor_demo.py
```

Five numbered parts:

1. The six components of the SYNTHETIC source (strike 32, dip 63, rake $-41$,
   $M_0 = 3.4\times10^{18}\ \mathrm{N\,m}$) with the physical meaning of each, the
   trace, and $\max|M-M^{\mathsf T}| = 0$.
2. The eigenvalue problem on the full tensor: eigenvalues and upward-oriented
   eigenvectors, $M_0$, the trace line, and the reconstruction residual
   $2.048\times10^{3}\ \mathrm{N\,m}$ (relative $6.11\times10^{-16}$).
3. The decomposition table for five sources, with reconstruction residuals
   between $0$ and $7.68\times10^{-17}$.
4. The $M_{\mathrm w}$ offsets: $-10.7$ in cgs, $-6.033333$ exact in SI,
   $-6.07$ quoted, difference $0.0367$, factor $1.1350$ in $M_0$, plus the
   five-row magnitude table.
5. Orthogonality: the cosines, the Pythagorean residual, and the basis-tensor
   inner product $D_{\text{dc}}:D_{\text{clvd}} = 0$.

## 9. Exercises

- [`exercises/03-moment-tensors-exercises.md`](exercises/03-moment-tensors-exercises.md)
- [`exercises/03-moment-tensors-solutions.md`](exercises/03-moment-tensors-solutions.md)

## 10. Real-world applications

- **Routine moment-tensor catalogues.** Global and regional centres report full
  tensors with $M_0$, $M_{\mathrm w}$, $\varepsilon$ and the isotropic fraction;
  the decomposition of Section 3.4 is the reporting standard.
- **Discriminating source types.** $\varepsilon$ and $\mathrm{tr}(M)$ separate
  earthquakes from explosions, mine collapses (implosive, $\mathrm{tr}M<0$) and
  volcanic sources.
- **Stress and deformation studies.** Principal axes of $M$ constrain stress
  orientation and the geometry of active faults.
- **Tsunami and ground-motion modelling.** $M_0$ and the focal geometry are the
  inputs to forward simulations of shaking and seafloor displacement.
- **Induced seismicity.** Non-double-couple components in small induced events
  are a diagnostic of fluid-driven and tensile-dominated failure.

## 11. Further reading

- **Aki, K., & Richards, P. G. (1980). *Quantitative Seismology*.** Level:
  graduate textbook. Chapters 3–4: the representation theorem and the moment
  tensor as its first moment.
- **Hanks, T. C., & Kanamori, H. (1979). A moment magnitude scale.** *Journal of
  Geophysical Research*. Level: research. The definition and its constants, which
  Section 3.6 converts between unit systems.
- **Jost, M. L., & Herrmann, R. B. (1989). A student's guide to and review of
  moment tensors.** *Seismological Research Letters*. Level: tutorial. The
  standard reference for the isotropic/DC/CLVD decomposition and its conventions.
- **Vavryčuk, V. (2015). Moment tensor decompositions revisited.** *Journal of
  Seismology*. Level: research. Where the CLVD conventions differ, and why.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC inversion returns
> $M = \begin{pmatrix} 2 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & -3\end{pmatrix}\times10^{18}\ \mathrm{N\,m}$.
> **(a)** Compute $\mathrm{tr}(M)$, $M_{\text{iso}}$ and $M'$. **(b)** Compute
> $M_0$ and $\varepsilon$. **(c)** Write the DC and CLVD parts explicitly and add
> them back. **(d)** Compute $M_{\mathrm w}$ with the exact SI offset and with the
> quoted offset, and state the difference in moment factor. **(e)** State one
> physical and one modelling reason why a non-zero $\varepsilon$ should not be
> read as a physical CLVD, and **(f)** say what additional observation would help
> distinguish the reasons.

## Common pitfalls

1. **Reporting a magnitude without the offset or the unit inside the log.** The
   difference is $0.0367$ magnitude units, a factor $1.135$ in $M_0$.
2. **Reading a CLVD as a physical object.** It absorbs anisotropy, noise, finite
   source effects and model error.
3. **Quoting the components as if they were frame-independent.** Only the
   invariants are.
4. **Confusing the isotropic part with the trace.** $M_{\text{iso}} =
   \mathrm{tr}(M)/3$.
5. **Treating $M_0$ as an observed quantity.** It is derived from a tensor that
   was itself inverted under assumptions.
6. **Over-reading a residual of $10^{-16}$.** It validates the arithmetic, not
   the model.
7. **Assuming $\mathrm{tr}(M) = \sum\lambda_i$ holds in floating point.** The demo
   shows two different printed values, both at the round-off floor.

## Related modules

- [02 The Double-Couple Source and Radiation Patterns](02-double-couple.md) —
  the $\varepsilon = 0$ extreme.
- [04 Source Time Functions, Rupture Kinematics and Directivity](04-source-time-function.md) —
  what the point-source assumption discards.
- [05 Source Spectra, Corner Frequency and Stress Drop](05-source-spectra.md) —
  how $M_0$ is measured from a spectrum.
- [06-04 Earthquake Location and Magnitude](../04-earthquake-location-and-magnitude/README.md) —
  magnitude scales and their saturation.
- [07 Discriminating Explosions from Earthquakes](07-nuclear-explosion-sources.md) —
  the isotropic source in the field.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of the inversion that produces a moment tensor.
