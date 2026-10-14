---
id: 03-07-04
title: "Symbolic Tensors and Index Notation"
level: advanced
prereqs: ["03-07-02", "03-07-03"]
estimated_minutes: 120
tags: [sympy, tensors, index-notation, elasticity, continuum-mechanics]
---

# Symbolic Tensors and Index Notation

Stress, strain, elasticity and the wave equation are tensor equations, and the
reason they are written in index notation is that the alternative — writing out
all 81 components of an elasticity tensor — is not an activity a human performs
reliably. The trade is that index notation hides sign and factor errors, so the
usual practice is to write the compact form and then check a few components by
hand.

Symbolic computation changes that trade. This lesson does the derivations in
index notation **and** checks them in components, symbolically, so that the
contraction is verified exactly rather than sampled. It also reports what I found
when using SymPy's abstract tensor module as a calculator, which is less than its
documentation might suggest.

```bash
.venv/bin/python 03-scientific-computing/07-sympy/code/tensor_symbolic_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the strain tensor from a displacement gradient and **show**
   symbolically that a rigid rotation contributes nothing to it.
2. **State** what SymPy's abstract index notation does well and, with measured
   examples, where it is not a reliable calculator.
3. **Contract** the isotropic elasticity tensor with a strain tensor in explicit
   indices and **verify** the result against the direct formula.
4. **Invert** the Lamé relations symbolically to obtain elastic parameters from
   engineering constants, and **evaluate** the seismic velocities.
5. **Compute** the deviatoric stress and the second invariant $J_2$, and
   **verify** two algebraic forms against each other and against a numerical
   eigenvalue calculation.
6. **Check** a tensor contraction against `numpy.einsum`, and state why the index
   form is still worth writing.

## Prerequisites

- [03-07-02 Symbolic Differentiation, Integration and Limits](./02-symbolic-calculus.md)
- [03-07-03 Symbolic Solvers for Algebraic and Differential Equations](./03-solving-equations.md)
  — the symbolic solve used in Section 6.
- [02-04-01 Stress](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md)
  and [02-04-02 Strain](../../02-physics/04-elasticity-and-continuum-mechanics/02-strain.md)
  — the physical definitions this lesson manipulates.

## 1. Intuition: index notation is a compression with a cost

A second-rank tensor has nine components in three dimensions; a fourth-rank
elasticity tensor has 81. Writing them out is unreadable, so we write

$$\sigma_{ij} = C_{ijkl}\,\varepsilon_{kl},$$

with the convention that a repeated index is summed. The compression is
enormous, and the cost is that a missing factor of 2 or a transposed index pair
is invisible on the page.

Two facts make the index form safe. First, **symmetry reduces the content**: the
demonstration counts 21 non-zero entries in a $3\times3\times3\times3$ isotropic
elasticity tensor assembled by brute force:

```
  non-zero entries of C_ijkl: 21 of 81
```

Those 21 are the two independent constants $\lambda$ and $\mu$ plus their index
pattern. Second, **contractions can be checked symbolically and exhaustively**,
which is what this lesson does.

## 2. Precise definitions

**Free index.** An index that appears once in a term. The term is a tensor of
that rank.

**Dummy index.** An index that appears exactly twice, once up and once down (or
twice in a contraction you have defined). It is summed.

**Kronecker delta.** $\delta_{ij} = 1$ if $i = j$, else 0.

**Strain tensor.** $\varepsilon_{ij} = \frac12(u_{i,j} + u_{j,i})$, where
$u_{i,j} = \partial u_i/\partial x_j$. Symmetric by construction.

**Rotation tensor.** $\omega_{ij} = \frac12(u_{i,j} - u_{j,i})$. Antisymmetric.

**Isotropic elasticity tensor.**
$C_{ijkl} = \lambda\,\delta_{ij}\delta_{kl} +
\mu\,(\delta_{ik}\delta_{jl} + \delta_{il}\delta_{jk})$.

**Lamé parameters.** $\lambda$ and $\mu$ (the shear modulus). Together with
density they fix the seismic velocities.

## 3. Derivation: strain, rotation and the rigid motion

Take the displacement field

$$u = \left(a x + \omega y,\; -\omega x + a y,\; 0\right).$$

The demonstration forms the Jacobian symbolically and splits it:

```
  displacement gradient u_(i,j) = [[a, omega, 0], [-omega, a, 0], [0, 0, 0]]
  strain    eps_ij = (u_(i,j)+u_(j,i))/2 = [[a, 0, 0], [0, a, 0], [0, 0, 0]]
  rotation  w_ij   = (u_(i,j)-u_(j,i))/2 = [[0, omega, 0], [-omega, 0, 0], [0, 0, 0]]
  trace of the strain (dilatation) = 2*a
  strain is symmetric: True
```

Three results, each exactly:

**The rotation is pure.** $\omega_{ij}$ is antisymmetric with a single
independent component, which is the rotation vector; the parameter $\omega$ does
not appear in the strain at all, because the two off-diagonal contributions
cancel exactly.

**The dilatation is $2a$.** The trace of the strain is $\nabla\cdot u = 2a$,
which measures the fractional volume change.

**The strain is symmetric**, which is why it has six independent components
rather than nine.

That the strain is *independent of $\omega$* is the reason the elastic wave
equation separates into a dilatational (P) part and a rotational (S) part: a
rigid rotation costs no elastic energy.

## 4. Abstract index notation in SymPy: measured capabilities and measured edges

SymPy has a module for index notation, `sympy.tensor.tensor`. What it does well:

```
  sigma_ij v_i v_j  -> sigma(L_0, L_1)*v(-L_0)*v(-L_1)
  free indices: [] (empty means the expression is a scalar)
  index positions are explicit: v(-i) is v_i and v(i) is v^i
  g_ij T^ij -> g(-L_0, -L_1)*T(L_0, L_1) -> contract_metric -> T(L_0, -L_0)
  a symmetric TensorHead declares symmetry: TensorSymmetry((), ((3),))
```

It tracks free indices, distinguishes upper and lower positions, renames dummy
indices automatically (the reproduced `L_0`, `L_1`), and knows a `TensorHead`'s
symmetry. The metric contraction gives the trace, which is correct:
$g_{ij}T^{ij} = T^i{}_i$.

Three edges that I measured, and that anyone using this module should know:

```
    (a) eps(i,j)*eps(j,i) raises: ValueError: Repeated index: j
    (b) eps(i,j)*eps(-i,-j) -> eps(L_0, L_1)*eps(-L_0, -L_1)
        ...and .canon_bp() on it returns 0, which is wrong: eps:eps is not zero
    (c) sig(i,j)*eps(-i,-j).canon_bp() -> -eps(L_0, L_1)*sig(-L_0, -L_1)
        ...reports a minus sign for a trace-like contraction that
        has no intrinsic sign
```

Read those carefully, because they are the reason this lesson does its
quantitative work in components:

- **(a)** You cannot write a contraction in which the same index appears twice
  with the same position. In a fully contracted product of two symmetric tensors
  this is exactly what one wants to write.
- **(b)** `canon_bp()`, the canonicaliser that uses symmetry, returned **0** for
  $\varepsilon_{ij}\varepsilon^{ij}$, which is the squared norm of a symmetric
  tensor and is not zero for a general symmetric tensor. That is not a
  simplification; it is a wrong answer.
- **(c)** A signed expression appeared where the contraction of two symmetric
  tensors has no intrinsic sign.

**Conclusion, stated as a limit of what I verified:** the abstract module is
excellent for *stating* a tensor equation and for tracking indices, and I do not
trust it as a calculator for fully contracted products. Every quantitative result
below therefore goes through explicit components, and every one is checked
numerically.

## 5. Hooke's law by explicit contraction

The demonstration assembles $C_{ijkl}$ from Kronecker deltas and contracts it
with a symmetric symbolic strain tensor, summing over the non-zero index pairs
only:

```
  strain components: [[e_xx, e_xy, e_xz], [e_xy, e_yy, e_yz], [e_xz, e_yz, e_zz]]
  C_ijkl eps_kl summed over 21 non-zero index pairs
  max |index contraction - direct formula| = 0
```

The residual is **exactly zero**, not small: the index contraction and the direct
formula

$$\sigma_{ij} = \lambda\,\varepsilon_{kk}\,\delta_{ij} + 2\mu\,\varepsilon_{ij}$$

are the same expression, and the symbolic route proves it for every component
that exists.

The count is worth noting: of the $3^4 = 81$ index quadruples, only 21
contribute. That is the compression index notation performs, made quantitative.

### 5.1 Two calibration cases that isolate the constants

**Pure shear**, $\varepsilon_{xy} = \varepsilon_{yx} = e_s$:

```
  pure shear eps_xy = eps_yx = e_s -> sigma = [[0, 2*e_s*mu, 0], [2*e_s*mu, 0, 0], [0, 0, 0]]
      sigma_xy - 2 mu e_s = 0
      sigma_xx = 0, sigma_zz = 0  (both zero)
```

A pure shear measures $\mu$ alone, and produces no normal stress. Both statements
are exact.

**Pure dilation**, $\varepsilon = e_v I$:

```
  pure dilation eps = e_v I -> sigma_xx = e_v*(3*lambda + 2*mu)
      sigma_xx - 3 K e_v = 0        with K = lambda + 2 mu/3
```

A pure dilation measures $3K = 3\lambda + 2\mu$ alone. Together the two cases
determine $(\lambda, \mu)$ from two experiments, which is exactly how a rock
mechanics laboratory measures them.

## 6. Lamé parameters from engineering constants

Young's modulus $E$ and Poisson's ratio $\nu$ are what a materials laboratory
reports; $\lambda$ and $\mu$ are what the wave equation needs. The relations are

$$E = \frac{\mu(3\lambda + 2\mu)}{\lambda + \mu}, \qquad
\nu = \frac{\lambda}{2(\lambda + \mu)},$$

and the demonstration inverts them symbolically:

```
  solved for the Lame parameters:
      lambda = -E*nu/((nu + 1)*(2*nu - 1))
      mu     = E/(2*(nu + 1))
  check against the textbook forms: lambda difference = 0, mu difference = 0
```

The sign structure of $\lambda$ is the interesting part: $\lambda$ is *negative*
for $\nu < 1/2$ in this form, and diverges as $\nu \to 1/2$, which is the
incompressible limit where $\lambda$ loses meaning and $K$ is the useful
constant. The symbolic form makes that visible; a numerical evaluation at a
single $\nu$ would not.

Evaluated:

```
  E = 70.0 GPa, nu = 0.25, rho = 2700.0 kg/m^3
      lambda = 28.000000 GPa, mu = 28.000000 GPa, K = 46.666667 GPa
      v_p = sqrt((lambda + 2 mu)/rho) = 5577.73 m/s
      v_s = sqrt(mu/rho)               = 3220.31 m/s
      v_p/v_s = 1.732051; sqrt(3) = 1.732051; difference 2.22e-16
      Poisson's ratio recovered from (vp/vs)^2: 0.250000000
```

The dimensional check:

$$[v_p] = \sqrt{\frac{\mathrm{Pa}}{\mathrm{kg\,m^{-3}}}} =
\sqrt{\frac{\mathrm{kg\,m^{-1}\,s^{-2}}}{\mathrm{kg\,m^{-3}}}} =
\mathrm{m\,s^{-1}}.$$

And $\nu = 0.25$ forces $\lambda = \mu$, so

$$\frac{v_p}{v_s} = \sqrt{\frac{\lambda + 2\mu}{\mu}} = \sqrt{3} =
1.732051,$$

which the measurement confirms to $2.2\times10^{-16}$ — machine precision. The
recovered $\nu$ from the velocity ratio is $0.250000000$, which is the standard
seismological route from a $v_p/v_s$ ratio to a Poisson's ratio, and it works
because the relation

$$\nu = \frac{(v_p/v_s)^2 - 2}{2\left((v_p/v_s)^2 - 1\right)}$$

is exact. A $v_p = 5578$ m/s and $v_s = 3220$ m/s pair in a rock of density
2700 kg/m³ is a realistic granite-or-gneiss value, which is a useful sanity check
on the arithmetic.

## 7. Deviatoric stress and the second invariant

Any stress tensor splits into an isotropic part and a deviator:

$$\sigma_{ij} = \frac{I_1}{3}\delta_{ij} + s_{ij}, \qquad I_1 =
\sigma_{kk}, \qquad s_{kk} = 0,$$

and the second invariant of the deviator is

$$J_2 = \tfrac12 s_{ij}s_{ij} = \tfrac12 \sigma_{ij}\sigma_{ij} -
\tfrac16 I_1^2.$$

Measured:

```
  mean normal stress p = trace(sigma)/3 = s_xx/3 + s_yy/3 + s_zz/3
  deviator trace = 0
  J2 = (1/2) s_ij s_ij                has 23 operations
  J2 = (1/2) sigma_ij sigma_ij - I1^2/6 has 23 operations
  difference of the two identities: 0
  J2 as a polynomial in the six components:
      s_xx**2/3 - s_xx*s_yy/3 - s_xx*s_zz/3 + s_xy**2 + s_xz**2 + s_yy**2/3 - s_yy*s_zz/3 + s_yz**2 + s_zz**2/3
```

Two algebraically different expressions for $J_2$ differ by exactly zero, and
both cost 23 operations — so there is no performance reason to prefer either, and
the identity is available as a check.

For a concrete stress state,

$$\sigma = \begin{pmatrix} 100 & 20 & 0\\ 20 & 50 & 0\\ 0 & 0 & 30 \end{pmatrix}
\mathrm{MPa},$$

the demonstration reports

```
      principal stresses = [ 30.          42.98437881 107.01562119] MPa
      J2 = 1.700000e+15 Pa^2 = 1700.000000 MPa^2
      from the symbolic expression with those numbers: 1700.000000 MPa^2
```

The numerical route (through `numpy.linalg.eigvalsh` and the trace formula) and
the symbolic route agree to the printed precision. A hand check:

$$\tfrac12\left(\sum_{ij}\sigma_{ij}^2 - \frac{I_1^2}{3}\right)
= \tfrac12\left(14200 - \frac{180^2}{3}\right) = \tfrac12(14200 - 10800) = 1700
\ \mathrm{MPa^2}.$$

$J_2$ is what von Mises and Drucker–Prager yield criteria are written in, so
having it as a differentiable symbolic expression matters for any problem that
asks how close a stress state is to failure.

## 8. The numeric check: `numpy.einsum`

```
  strain (dimensionless): [[0.001, 0.0002, 0.0], [0.0002, -0.0005, 0.0], [0.0, 0.0, 0.0003]]
  stress from einsum (Pa): [[78400000.0, 11200000.0, 0.0], [11200000.0, -5600000.000000001, 0.0], [0.0, 0.0, 39200000.0]]
  max |einsum - (lambda tr(eps) I + 2 mu eps)| = 2.794e-09 Pa (relative 3.56e-17)
  volumetric part: tr(sigma)/3 = 3.733333e+07 Pa;  K tr(eps) = 3.733333e+07 Pa
  deviatoric part: max |sigma - mean(sigma) I| = 4.293333e+07 Pa
```

The array contraction and the component formula agree to $3.6\times10^{-17}$
relative — the last bit, as expected for two orderings of the same arithmetic.
Note the volumetric check: $\mathrm{tr}(\sigma)/3 = K\,\mathrm{tr}(\varepsilon) =
3.733\times10^7$ Pa, which is the physical meaning of the bulk modulus used in
Section 6.

Writing $C_{ijkl}$ once in index notation and generating the 81-entry array from
it is the auditable route; hand-coding $C$ as a literal is how a transposition
gets into a wave-propagation code.

## 9. The spherical Laplacian, as a closing check

The Laplacian of a radial function in spherical coordinates is

$$\nabla^2 f = \frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{df}{dr}\right),$$

and applying it:

```
  with f = 1/r:  0
  general f(r): Derivative(f(r), (r, 2)) + 2*Derivative(f(r), r)/r
  for f = 1/r the result is exactly zero, which is Laplace's equation ...
  the same operator applied to r^2 gives 6
  spherical Laplacian of the potential inside a uniform sphere of
  density rho,  V = (2/3) pi G rho (r^2 - 3 R^2):
      4*pi*G*rho = 4 pi G rho, which is Poisson's equation inside the
      body; residual 0
```

So $\nabla^2(r^{-1}) = 0$ outside the source and $\nabla^2 V = 4\pi G\rho$
inside the body: **Laplace's equation outside, Poisson's equation inside, with the
source term appearing exactly**. The residual is 0, and the test costs one line.

## 10. Assumptions and limitations

- **The abstract tensor module has sharp edges.** Section 4 records three; the
  one that matters is `canon_bp()` returning 0 for a non-zero contraction. I did
  not investigate whether that is a fixed limitation or a misuse of the API on my
  part; what I can say is that I could not obtain a correct answer from it, and
  that I therefore did not use it for quantitative work.
- **Component verification is exhaustive but small.** Every check above is over
  $3\times3$ or $3\times3\times3\times3$ arrays, so "verified" means verified for
  all components in 3-D — which is complete, unlike a sampled check.
- **Isotropy is an assumption, not a fact.** Real rocks are anisotropic; the
  isotropic $C_{ijkl}$ above has two independent constants, and a transversely
  isotropic rock has five. The symbolic method extends unchanged; the algebra
  does not get easier.
- **Small strains only.** The linearised strain tensor is $\frac12(u_{i,j} +
u_{j,i})$, valid when the displacement gradient is small. Large-strain
  formulations need the deformation gradient $F_{ij}$ and its polar decomposition.
- **Sign conventions differ between fields.** The stress sign convention here
  (tension positive) is the mechanic's; seismology uses the opposite for the
  moment tensor. State yours.
- **No performance measurement.** The operation counts are static; no wall-clock
  times are quoted.

## 11. Worked examples

### 11.1 Verifying a published elasticity relation

The demonstration's Lamé inversion produced

$$\lambda = -\frac{E\nu}{(\nu+1)(2\nu-1)} =
\frac{E\nu}{(1+\nu)(1-2\nu)},$$

which is the textbook form, and the check against it differed by exactly 0. Note
that the two printed forms look different and are identical — which is exactly
why the check is done by subtraction rather than by eye. The general procedure for
verifying any published tensor relation symbolically:

1. Substitute the published RHS and the symbolic LHS into one expression.
2. Simplify the difference.
3. Require the result to be **0**, not "small".

That is what
`check against the textbook forms: lambda difference = 0, mu difference = 0`
means, and it is a stronger statement than any tolerance.

### 11.2 A seabed Poisson's ratio from a velocity ratio

Given a marine seismic refraction giving $v_p = 1800$ m/s and $v_s = 500$ m/s in
the shallow seabed:

$$\nu = \frac{(v_p/v_s)^2 - 2}{2\left((v_p/v_s)^2 - 1\right)}
= \frac{12.96 - 2}{2(12.96 - 1)} = 0.4582.$$

A Poisson's ratio of 0.458 just below 0.5 is characteristic of water-saturated
unconsolidated sediment, which is the geological reading: high $\nu$ means the
material resists volumetric change far more than shear, as a fluid-saturated
granular medium does. The formula is exact; the interpretation is the
interpretation.

### 11.3 Where the index form earns its keep

In a finite-difference elastic solver the stress update is $\sigma_{ij} \mathrel{+}=
C_{ijkl}\,\Delta\varepsilon_{kl}$. Written in indices, the nine stress updates
are nine lines; written as components, they are nine lines of 21 terms each.
Generating the update from the index form — programmatically, as the
demonstration's `C_ijkl eps_kl summed over 21 non-zero index pairs` does — removes
the transcription step in which the transposition error would occur.

## 12. Python demonstration

`code/tensor_symbolic_demo.py` runs in seven parts:

| Part | Result | Verification |
|---|---|---|
| 1 | Strain and rotation of a displacement field | rotation absent from strain; dilatation $2a$ |
| 2 | Abstract index notation | free/dummy indices tracked; three edges recorded |
| 3 | Hooke's law by contraction | residual `0`, 21 of 81 non-zero |
| 4 | Lamé inversion and velocities | `v_p/v_s = 1.732051` against $\sqrt3$, difference `2.22e-16` |
| 5 | Deviator, $J_2$ | two forms differ by `0`; `1700.000000 MPa^2` both ways |
| 6 | `einsum` check | relative difference `3.56e-17` |
| 7 | Spherical Laplacian | $0$ for $1/r$, $4\pi G\rho$ inside, residual `0` |

## 13. Exercises

Solutions are in
[`exercises/04-tensor-symbolic-solutions.md`](./exercises/04-tensor-symbolic-solutions.md).

### ★ Foundational

**★1.** Compute $\delta_{ii}$ and $\delta_{ij}\delta_{jk}$ in 3-D, and state the
result in index-free notation.

**★2.** For $\sigma_{ij}$ symmetric and $A_{ij}$ antisymmetric, show that
$\sigma_{ij}A_{ij} = 0$.

**★3.** Write out $\varepsilon_{xy}$ in terms of $u_x$ and $u_y$ and identify
which part corresponds to a shear and which to a rotation.

**★4.** Evaluate $C_{ijkl}$ for $\lambda = \mu$ and count the non-zero components.

### ★★ Applied

**★★5.** Derive the strain tensor for the displacement field
$u = (0, 0, w(z))$ and interpret the result physically. Which elastic constant
alone relates $\sigma_{zz}$ to $\varepsilon_{zz}$, and why?

**★★6.** Verify symbolically that the isotropic elasticity tensor is symmetric
under $i \leftrightarrow j$, $k \leftrightarrow l$ and $(ij) \leftrightarrow
(kl)$. Report which of the three SymPy confirms with a zero difference.

**★★7.** For a transversely isotropic medium with five independent constants,
write down $C_{ijkl}$ explicitly and count the non-zero components. Compare with
the 21 of the isotropic case and explain the difference in terms of symmetry.

**★★8.** Compute $J_2$ for a pure shear stress state $\sigma_{xy} = \tau$ (all
other components zero). Compare with $\tau^2$ and state the general result
$J_2 = \tau^2$ for pure shear.

### ★★★ Research-oriented

**★★★9.** Build a symbolic validation of a $v_p/v_s$ inversion. Derive
$v_p(\lambda, \mu, \rho)$ and $v_s(\mu, \rho)$ symbolically, then solve for
$(\lambda, \mu)$ from $(v_p, v_s, \rho)$ and verify by substitution that both
equations are satisfied exactly. Evaluate for a saturated sandstone
($v_p = 3000$ m/s, $v_s = 1600$ m/s, $\rho = 2300\ \mathrm{kg\,m^{-3}}$) and
report $\lambda$, $\mu$, $K$, $E$ and $\nu$, with the Poisson's ratio you would
quote in a paper.

**★★★10.** Assess the abstract tensor module independently. Using only
`sympy.tensor.tensor`, attempt to compute $\varepsilon_{ij}\varepsilon_{ij}$,
$A_{ij}B_{ij}$ and $C_{ijkl}\varepsilon_{kl}$ for symmetric symbolic tensors, and
report for each whether the result is correct when checked against an explicit
3-D component calculation. State your findings as a recommendation with the
evidence.

## 14. Common mistakes

1. **Trusting `canon_bp()` on fully contracted products.** Measure it against
   components first.
2. **Forgetting that the strain is symmetric.** Nine components, six independent.
3. **Mixing stress sign conventions between mechanics and seismology.**
4. **Assuming isotropy.** Two constants is a choice, not a default.
5. **Hand-coding $C_{ijkl}$.** Generate it from the index form.
6. **Using the linearised strain tensor for large deformation.**
7. **Treating a small residual as zero.** Require exact zero where the algebra
   permits it, and say when it does not.
8. **Confusing $J_2$ with the shear stress magnitude.** They differ by a factor
   of 2 in the pure-shear case; derive it rather than remembering it.

## 15. Real-world applications

- **Elastic wave propagation.** $C_{ijkl}$ and the momentum equation are the
  starting point of every full-waveform code; generating the update from indices
  removes a transcription error class.
- **Rock physics.** Converting between engineering constants and Lamé parameters,
  and between velocities and elastic moduli, is routine, and it is exact algebra
  that belongs in code, not in a spreadsheet.
- **Failure criteria.** $J_2$ and the stress invariants determine whether a
  borehole, a tunnel or a fault is close to failure.
- **Anisotropy.** Shale, ice and mantle fabrics need five or more constants; the
  symbolic route is how the component bookkeeping stays correct.
- **Potential fields.** The spherical Laplacian check of Section 9 is the standard
  verification for a gravity or magnetic code: Laplace outside the source,
  Poisson inside.

## 16. Further reading

- **SymPy documentation** (sympy.org). Level: advanced. The `sympy.tensor.tensor`
  module reference and its documented limitations; read Section 4's measurements
  alongside it.
- **Malvern, L. E. (1969). *Introduction to the Mechanics of a Continuous
  Medium*. Prentice-Hall.** Level: advanced. The definitive treatment of strain,
  rotation and the elasticity tensor used here; check your library.
- **Aki, K. & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Chapter 2. Level: advanced. Stress, strain and the
  elastic constants, with the seismological sign conventions.
- **Nye, J. F. (1985). *Physical Properties of Crystals*. Oxford University
  Press.** Level: advanced. Symmetry arguments for the elasticity tensor,
  including the transversely isotropic case of exercise 7.
- **numpy documentation** (numpy.org). Level: intermediate. `einsum`, the array
  contraction used in Section 8, including the index mini-language.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 17. Related lessons

- [03-07-01 Symbolic Variables, Expressions and Assumptions](./01-symbolic-basics.md)
- [03-07-02 Symbolic Differentiation, Integration and Limits](./02-symbolic-calculus.md)
- [03-07-05 Generating Fast Numerical Code from Symbolic Results](./05-code-generation.md)
  — turning the contracted forms here into arrays and C.
- [03-02-05 Linear Algebra with NumPy](../02-numpy/05-linear-algebra-numpy.md)
  — the array side of the eigenvalue calculation in Section 7.
- [02-04-01 Stress](../../02-physics/04-elasticity-and-continuum-mechanics/01-stress.md)
  and [02-04-02 Strain](../../02-physics/04-elasticity-and-continuum-mechanics/02-strain.md)

## 18. Self-assessment checklist

- [ ] I can derive strain and rotation from a displacement gradient. (§3)
- [ ] I can say what the abstract index module does and does not do reliably.
      (§4)
- [ ] I can contract $C_{ijkl}$ with a strain tensor and verify the result. (§5)
- [ ] I can invert the Lamé relations and evaluate the wave speeds. (§6)
- [ ] I can compute $J_2$ two ways and confirm they agree. (§7)
- [ ] I can check a tensor contraction against `numpy.einsum`. (§8)
- [ ] I can verify the spherical Laplacian of $1/r$ and of the interior
      potential. (§9)
