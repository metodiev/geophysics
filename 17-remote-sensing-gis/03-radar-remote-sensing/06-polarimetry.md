---
id: 17-03-06
title: "SAR Polarimetry and Polarimetric Decomposition"
level: research
prereqs: ["17-03-01", "02-07-05", "01-07-07"]
tags: [remote-sensing, radar, polarimetry, scattering, decomposition, entropy]
---

# SAR Polarimetry and Polarimetric Decomposition

> All models and data in this module are **SYNTHETIC**. The scattering matrices,
> dielectric constants, roughness statistics and look counts in this lesson are
> teaching values computed by the demonstration. No real target, scene or
> measured polarimetric dataset is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the $2\times2$ scattering matrix for the canonical targets, and
   **explain** why reciprocity reduces it to three independent complex numbers.
2. **Transform** a scattering matrix to the Pauli vector and **build** the
   multilook coherency matrix, **verifying** that it is Hermitian with trace
   equal to the total power.
3. **Derive** the eigen-decomposition parameters (entropy, anisotropy, mean
   alpha) and **interpret** their measured values for surface, double-bounce and
   volume scattering.
4. **Demonstrate** that a single-look coherency matrix is rank one, so entropy is
   identically zero, and **measure** how it converges with the look count.
5. **Derive** the Bragg resonance condition, **compute** the resonant surface
   wavelength, and **evaluate** the first-order HH/VV ratio as a function of
   incidence angle.
6. **Show** that a degenerate coherency matrix admits more than one eigenvector
   set, and **quantify** which parameters are invariant and which are not.
7. **State** why the number of scattering components in a decomposition is a
   model decision rather than a measurement.

## Prerequisites

- [17-03-01 SAR Principles: Geometry, Polarisation, Backscatter](01-sar-principles.md) —
  $\sigma^{0}$, the channels and the geometry.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../../02-physics/07-electromagnetism/05-em-waves.md) —
  polarisation states and the plane-wave description.
- [01-07-07 Orthogonality, Projections and Least Squares](../../01-mathematics/07-linear-algebra/07-orthogonality.md) —
  Hermitian operators, orthogonal bases and eigen-decomposition.

## 1. Intuition: three numbers instead of one

A single-polarisation radar measures one number per pixel: the backscattered
power in one channel. A fully polarimetric radar measures four complex numbers —
the response to horizontal and vertical transmission, received on both
polarisations — and reciprocity reduces them to three independent complex
quantities, i.e. six real numbers per resolution cell. That is the entire content
of this lesson: what those six numbers mean, and how honestly they can be turned
into "this pixel is a rough surface", "this pixel is a building", "this pixel is
a forest canopy".

The honest part matters. The map from a scene to a coherency matrix is not
invertible: many mixtures plus noise produce the same matrix, and one parameter
(the mean scattering angle) is not even unique for a degenerate matrix. This
lesson derives the machinery, measures what is invariant, and states plainly
which conclusions are model-dependent.

## 2. Definitions

The **scattering matrix** (Sinclair matrix) relates the transmitted field
$\mathbf{E}^{t}$ to the received field $\mathbf{E}^{r}$ in the linear (H, V)
basis:

$$\begin{pmatrix} E_H^{r} \\ E_V^{r} \end{pmatrix}
= \frac{e^{-\mathrm{i}kr}}{r}
\begin{pmatrix} S_{HH} & S_{HV} \\ S_{VH} & S_{VV} \end{pmatrix}
\begin{pmatrix} E_H^{t} \\ E_V^{t} \end{pmatrix}.$$

For monostatic backscatter **reciprocity** requires $S_{HV} = S_{VH}$, so the
matrix carries three independent complex numbers. The **Pauli vector** is

$$\mathbf{k} = \frac{1}{\sqrt{2}}
\begin{pmatrix} S_{HH}+S_{VV} \\ S_{HH}-S_{VV} \\ 2S_{HV}\end{pmatrix},$$

and the **coherency matrix** is the multilook average
$T = \langle \mathbf{k}\mathbf{k}^{\dagger}\rangle$, a $3\times3$ Hermitian
positive-semidefinite matrix. Its trace equals the total power (span).

## 3. Derivations

### 3.1 Why three numbers

Reciprocity for a monostatic radar follows from the symmetry of the scattering
process under interchange of transmitter and receiver: the same physical path is
traversed in the same sense, so the matrix is symmetric,
$S_{HV} = S_{VH}$. Together with the $2\times2$ complex structure this leaves
three complex numbers, and the Pauli vector above is the standard orthonormal
mapping from those three numbers to a three-component complex vector whose
squared norm is the total power:

$$\left|\mathbf{k}\right|^{2}
= \tfrac{1}{2}\left(\left|S_{HH}+S_{VV}\right|^{2}
+ \left|S_{HH}-S_{VV}\right|^{2} + 4\left|S_{HV}\right|^{2}\right)
= \left|S_{HH}\right|^{2} + \left|S_{VV}\right|^{2}
+ 2\left|S_{HV}\right|^{2}.$$

The factor $2$ in the cross-polarised term is the reciprocity accounting: one
measurement stands for two channels. The demonstration prints the Pauli vectors
of the canonical targets:

| target | $S$ | $\mathbf{k}$ |
|---|---|---|
| trihedral, sphere | $\mathrm{diag}(1,1)$ | $(+1.41,\ 0,\ 0)$ |
| dihedral (double bounce) | $\mathrm{diag}(1,-1)$ | $(0,\ +1.41,\ 0)$ |
| horizontal dipole | $\mathrm{diag}(1,0)$ | $(+0.71,\ +0.71,\ 0)$ |
| $45^\circ$ dipole | $\tfrac{1}{2}\mathrm{ones}$ | $(+0.71,\ 0,\ +0.71)$ |

Each mechanism lands on a different axis: the **surface/odd-bounce** on
$k_1$, the **double bounce** on $k_2$ and the **depolarising volume** on $k_3$.
The whole enterprise is quantifying how a real pixel is distributed among these.

### 3.2 The coherency matrix and its eigen-decomposition

For a single look $T = \mathbf{k}\mathbf{k}^{\dagger}$ is a rank-one outer
product; multilooking averages many such outer products. Since $T$ is Hermitian
and positive semidefinite, it has real non-negative eigenvalues
$\lambda_1 \ge \lambda_2 \ge \lambda_3 \ge 0$ and orthonormal eigenvectors
$\mathbf{u}_i$. Define the probabilities $p_i = \lambda_i/\sum_j\lambda_j$, then

$$H = -\sum_i p_i\log_3 p_i \in [0,1], \qquad
\alpha = \sum_i p_i\alpha_i, \quad
\alpha_i = \arccos\left|u_{i,1}\right|, \qquad
A = \frac{\lambda_2-\lambda_3}{\lambda_2+\lambda_3}.$$

$H$ (entropy) measures *how many* mechanisms are present, $\alpha$ (mean
scattering angle) measures *which*, and $A$ (anisotropy) measures whether the two
weaker mechanisms differ. The demonstration builds each canonical target from a
cloud of 200 realisations with 8% complex perturbation and measures:

| target | $H$ | $\alpha$ (deg) | $A$ | $\lambda_1/\lambda_2/\lambda_3$ |
|---|---|---|---|---|
| trihedral, sphere | 0.0706 | 1.71 | 0.0866 | 2.010 / 0.014 / 0.012 |
| dihedral | 0.0715 | 89.25 | 0.1587 | 2.000 / 0.015 / 0.011 |
| horizontal dipole | 0.1204 | 45.23 | 0.0845 | 1.009 / 0.014 / 0.012 |
| $45^\circ$ dipole | 0.1142 | 45.18 | 0.1470 | 1.009 / 0.014 / 0.010 |
| random volume | 0.9119 | 42.35 | 0.0761 | 0.548 / 0.245 / 0.210 |

The pattern is the diagnostic: **low $H$ and $\alpha \approx 0^\circ$** is surface
scattering, **low $H$ and $\alpha \approx 90^\circ$** is double bounce, and **high
$H$ with $\alpha \approx 45^\circ$** is volume scattering. The random volume has
$H = 0.9119$ because its three eigenvalues are comparable: three mechanisms of
similar strength. Note that the dipoles also sit near $\alpha = 45^\circ$ — a
single dipole is *not* volume scattering, which is why $\alpha$ alone is never
sufficient and entropy must be read with it.

### 3.3 Statistics: what a single look cannot say

A one-look coherency matrix is $\mathbf{k}\mathbf{k}^{\dagger}$, exactly rank
one, so its eigenvalues are $(\lambda,0,0)$, its entropy is **identically zero
for every target**, and $\alpha$ is the angle of that single vector. The
demonstration measures the convergence of $H$ for a deterministic trihedral seen
through 15% complex noise:

| looks | mean $H$ | median | 10% | 90% |
|---|---|---|---|---|
| 1 | $-0.0000$ | 0.0000 | 0.0000 | 0.0000 |
| 2 | 0.0878 | 0.0814 | 0.0299 | 0.1542 |
| 4 | 0.1380 | 0.1318 | 0.0830 | 0.2003 |
| 16 | 0.1743 | 0.1730 | 0.1426 | 0.2083 |
| 64 | 0.1831 | 0.1826 | 0.1669 | 0.1997 |

Two conclusions. First, a single-look entropy is worthless — every pixel would
report $H = 0$ and be classified as surface scattering. Second, even at 64 looks
this *deterministic* target reports $H = 0.18$, not zero, because the noise itself
populates the second and third eigenvalues. A threshold such as "$\alpha > 40^\circ$
and $H > 0.5$ means volume" is therefore only meaningful with the look count, the
noise level and the measured convergence stated alongside it. The same caution
applied to the coherence estimator in [02](02-insar.md) applies here.

### 3.4 Bragg scattering and the polarisation ratio

First-order (small-perturbation) surface scattering selects the roughness
component whose wavenumber satisfies the resonance condition

$$k_B = 2k\sin\theta = \frac{4\pi\sin\theta}{\lambda}
\qquad\Longrightarrow\qquad
\Lambda_B = \frac{\lambda}{2\sin\theta}.$$

*Numerical check.* With $\lambda = 5.6565\ \mathrm{cm}$ and $\theta = 35^\circ$:
$k_B = 127.43\ \mathrm{rad\,m^{-1}}$, so $\Lambda_B = 4.9309\ \mathrm{cm}$. A
$5.66\ \mathrm{cm}$ radar at $35^\circ$ is resonant with surface ripples about
$4.93\ \mathrm{cm}$ long — the scale at which soil roughness and wind-generated
water waves live.

To first order the polarisation dependence is contained in the coefficients
$g_{HH}$ and $g_{VV}$ of the perturbation solution, which the demonstration
evaluates for a teaching dielectric constant $\epsilon = 6.0$:

| $\theta$ | $HH/VV$ (linear) | dB |
|---|---|---|
| $0^\circ$ | 1.000000 | 0.000 |
| $10^\circ$ | 0.965059 | $-0.309$ |
| $23^\circ$ | 0.836505 | $-1.551$ |
| $35^\circ$ | 0.679805 | $-3.352$ |
| $45^\circ$ | 0.548037 | $-5.224$ |
| $60^\circ$ | 0.368561 | $-8.670$ |

At normal incidence the two coefficients coincide ($g = 0.420204$, ratio
$1.000000$) **as symmetry requires**, and the ratio falls steeply with incidence.
That is the measurement that makes polarimetry useful: over a bare surface
$\sigma^{0}_{HH}/\sigma^{0}_{VV}$ is a function of $\epsilon$ *and* $\theta$, so a
measured ratio constrains the dielectric constant only if the local incidence
angle is known. Inverting a polarisation ratio for soil moisture without a
geometrically correct incidence angle is the polarimetric version of reading
$\sigma^{0}$ as a material constant
([01](01-sar-principles.md)).

### 3.5 A decomposition is not unique

Build a coherency matrix from an orthonormal basis
$\mathbf{e}_1 = (0.6,-0.8,0)$, $\mathbf{e}_2 = (0.8,0.6,0)$, $\mathbf{e}_3 = (0,0,1)$
with eigenvalues $(2.0, 0.8, 0.8)$. The eigenvalues are degenerate, so the
eigenvectors of the pair $(\lambda_2 = \lambda_3)$ are determined only up to a
rotation within their two-dimensional subspace. The demonstration rotates them by
$45^\circ$ and rebuilds the matrix:

$$\left\|T - T_{\text{rotated}}\right\| = 4.7\times10^{-16},$$

i.e. the same observable matrix, exactly. But the parameters differ:

| parameter | convention 1 | convention 2 |
|---|---|---|
| per-eigenvector $\alpha_i$ | $(53.13,\ 36.87,\ 90.00)$ | $(53.13,\ 55.55,\ 55.55)$ |
| mean $\alpha$ | $57.7100^\circ$ | $54.2057^\circ$ |
| $H$ | 0.905713 | 0.905713 |
| $A$ | 0.000000 | 0.000000 |

$H$ and $A$ depend only on the eigenvalues and are **invariant**; the mean
$\alpha$ depends on the eigenvectors and is **not**. The discrepancy here is
$3.50^\circ$; the size grows with how much the degenerate subspace overlaps the
$(HH+VV)$ axis. Every implementation therefore chooses a convention (typically
ordering the degenerate eigenvectors to maximise $\alpha$) and the choice must be
reported with the result.

The deeper statement: two mechanisms with equal weights, and a single mechanism
plus noise, can produce the *same* $T$. The number of components in a
decomposition is a **model decision**, and the honest output is the decomposed
matrix *with its fit residual* and a statement that an alternative decomposition
fits as well. This is the same non-uniqueness discussed for the receiver-function
trade-off in [06-08](../../06-seismology/08-receiver-functions-and-crustal-structure/README.md):
data constrain a combination, and the interpretation must state which
combination.

## 4. Worked example — reading six numbers

*All values SYNTHETIC.* A pixel over a wetland margin has a coherency matrix
whose eigenvalues, after 16 looks, are
$\lambda = (0.90,\ 0.55,\ 0.05)$ in arbitrary units, and whose eigenvectors have
$|u_{i,1}| = (0.99,\ 0.30,\ 0.10)$.

1. **Probabilities.** $\sum\lambda = 1.50$, so $p = (0.600,\ 0.367,\ 0.033)$.
2. **Entropy.**
   $H = -\left[0.6\ln 0.6 + 0.367\ln 0.367 + 0.033\ln 0.033\right]/\ln 3
   = (0.3065 + 0.3679 + 0.1125)/1.0986 = 0.7163$.
3. **Mean alpha.**
   $\alpha_i = \arccos(0.99, 0.30, 0.10) = (8.11^\circ, 72.54^\circ, 84.26^\circ)$,
   so $\alpha = 0.600(8.11) + 0.367(72.54) + 0.033(84.26) = 4.87 + 26.62 + 2.78
   = 34.27^\circ$.
4. **Anisotropy.** $A = (0.55-0.05)/(0.55+0.05) = 0.8333$ — the two weaker
   eigenvalues differ strongly, so there is a definite second mechanism rather
   than a symmetric mixture.
5. **Reading.** $H = 0.72$ is moderately high but the dominant eigenvector has
   $\alpha_1 = 8^\circ$: the strongest single contribution is *surface*. The
   secondary mechanisms are double-bounce-like and cross-polarised. The honest
   description is "a dominant surface with a strong, ordered secondary
   contribution" — not "volume scattering", which would require all three angles
   near $45^\circ$ with comparable weights.
6. **Check.** The same eigenvalues with a *rotated* degenerate pair would change
   the mean $\alpha$ by a few degrees (Section 3.5); here the eigenvalues are
   well separated ($A = 0.83$), so the ambiguity is small, and that is worth
   stating as the reason the number can be quoted.

## 5. Assumptions and regime of validity

1. **Reciprocity** ($S_{HV} = S_{VH}$). Valid for monostatic backscatter from a
   reciprocal medium; violated by Faraday rotation in the ionosphere and by
   ferrite-like media.
2. **A single dominant scattering direction per cell.** Multipath between distant
   structures breaks the plane-wave description.
3. **Statistical stationarity over the multilook window.** Scattering statistics
   must not change within the window, or the average is a mixture of populations.
4. **First-order (small-perturbation) Bragg theory** for the polarisation ratio:
   valid for surface roughness much smaller than the wavelength with small
   slopes. It fails for very rough or very steep surfaces.
5. **Known incidence angle.** The HH/VV ratio constrains $\epsilon$ only with it.
6. **Enough looks.** Section 3.3: a single look gives $H = 0$ for everything, and
   even 64 looks leaves a measurable offset for a deterministic target.
7. **Teaching values.** $\epsilon = 6.0$, the 8% perturbation, the 15% noise and
   the 200-realisation clouds are synthetic; they are not measured scene
   statistics.

## 6. Python demonstration

`code/polarimetry_demo.py` prints five sections: the canonical scattering
matrices and their Pauli vectors; the coherency matrices and their $H$/$\alpha$/$A$
parameters; the entropy-versus-looks convergence table; the Bragg resonance and
the HH/VV ratio versus incidence angle; and the degenerate-decomposition
non-uniqueness with both conventions.

```bash
cd 17-remote-sensing-gis/03-radar-remote-sensing/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python polarimetry_demo.py
```

## 7. Exercises

See
[`exercises/06-polarimetry-exercises.md`](./exercises/06-polarimetry-exercises.md)
and
[`exercises/06-polarimetry-solutions.md`](./exercises/06-polarimetry-solutions.md).

## Mastery checkpoint

Without notes: **(a)** write the scattering matrix of a dihedral reflector and
its Pauli vector, and say why it is called double bounce. **(b)** For
$\lambda = 5.6565\ \mathrm{cm}$ and $\theta = 45^\circ$, compute the Bragg
resonant surface wavelength. **(c)** Explain why a single-look entropy is zero for
every target. **(d)** State which of $H$, $A$ and $\alpha$ are invariant under a
rotation of degenerate eigenvectors, and why.

A worked version of (a)–(c) is in the lesson-06
[solutions](./exercises/06-polarimetry-solutions.md).

## Common pitfalls

1. **Classifying by $\alpha$ alone.** The dipoles in Section 3.2 sit at $\alpha
   \approx 45^\circ$ without any volume scattering.
2. **Using entropy from a single look.** It is identically zero.
3. **Quoting a decomposition without the look count or the residual.** The number
   of components is a choice.
4. **Treating the HH/VV ratio as a moisture measurement.** It is a function of
   incidence angle too.
5. **Ignoring degeneracy.** Mean alpha can move by degrees between two
   conventions that describe the same data.
6. **Forgetting Faraday rotation** for low-frequency systems, which breaks
   reciprocity as measured.
7. **Averaging over a mixed scene.** A multilook window spanning two populations
   produces a matrix that corresponds to neither.

## Related modules

- [01 SAR Principles: Geometry, Polarisation, Backscatter](01-sar-principles.md) —
  the channels, $\sigma^{0}$ and the resonance idea.
- [02 InSAR: Interferometric Phase and Deformation Measurement](02-insar.md) —
  the complex statistics shared with the coherency matrix.
- [17-01 Remote Sensing Physics](../01-remote-sensing-physics/README.md) — the
  radiometric and spectral framing.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../../02-physics/07-electromagnetism/05-em-waves.md) —
  the $2\times2$ field description used throughout.
- [01-07-07 Orthogonality, Projections and Least Squares](../../01-mathematics/07-linear-algebra/07-orthogonality.md) —
  Hermitian eigen-decomposition and degenerate subspaces.
