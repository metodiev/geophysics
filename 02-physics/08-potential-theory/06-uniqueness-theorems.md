---
id: 02-08-06
title: "Uniqueness Theorems and Boundary Conditions"
level: graduate
prereqs: ["02-08-02", "01-06-06", "01-07-04"]
estimated_minutes: 90
tags: [uniqueness, boundary-value-problem, non-uniqueness, equivalent-stratum, null-space, inversion]
---

# Uniqueness Theorems and Boundary Conditions

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the exterior Dirichlet and Neumann problems precisely, including the
   regularity conditions at infinity without which neither is well posed.
2. **Prove** uniqueness of the exterior Dirichlet problem using Green's first
   identity, and explain why the boundary term at infinity vanishes for this
   problem but does not for the Neumann problem.
3. **State** the exterior Neumann existence condition correctly, and explain why
   it is *not* the $\oint g\,dA = 0$ of the bounded problem.
4. **Derive** the corollary that uniqueness of the *field* does not imply
   uniqueness of the *source*, and prove it by exhibiting an infinite family of
   sources with identical exterior fields.
5. **Derive** the equivalent stratum in two dimensions in closed form, and state
   the three-dimensional wavenumber form.
6. **Explain** what an annihilator is, why the null space of the gravity forward
   operator is infinite-dimensional, and why regularisation selects a
   representative rather than resolving the ambiguity.
7. **List** the additional information that does reduce the ambiguity — and the
   information that does not.
8. **Verify** all of this numerically: the uniqueness proof by relaxation from two
   starting points, and the non-uniqueness by computing two genuinely different
   sources whose fields agree to within quadrature error.

## Prerequisites

- [02-08-02 Laplace's Equation and Harmonic Functions](./02-laplace-equation.md)
  — harmonicity, the mean value property and the maximum principle.
- [01-06-06 Gauss, Stokes and Green Theorems](../../01-mathematics/06-multivariable-calculus/06-integral-theorems.md)
  — Green's first identity, which is the entire proof.
- [01-07-04 Rank, Null Space and Solvability (Existence and Uniqueness)](../../01-mathematics/07-linear-algebra/04-rank-and-nullspace.md)
  — null space, existence and uniqueness for linear maps; this lesson is the
  infinite-dimensional version.
- [02-08-01 Newtonian Gravitational Potential and Field](./01-gravitational-potential.md)
  — the point mass, the line mass and the surfaces of observation.

## 1. Two questions that are constantly confused

Potential-field work has two different uniqueness questions, and almost every
serious error in interpretation comes from answering one when the other was asked.

**Question A: is the field unique given the boundary data?**
*Yes.* This is a theorem, proved in Section 3.2. It says that if you know the
gravity field on a closed surface, there is exactly one harmonic field above it
consistent with those values. This is why upward continuation, filtering and
field interpolation are legitimate operations.

**Question B: is the source unique given the field?**
*No, not even close.* The set of density distributions producing a given exterior
field is infinite-dimensional. This is a theorem too, proved by construction in
Section 3.5, and it is the central fact of potential-field interpretation.

The two answers are not in conflict, because the theorems are about different
objects. Uniqueness holds for the *field*, which lives in the harmonic region
above the sources. Non-uniqueness holds for the *source*, which lives in the
non-harmonic region below. The boundary data determine everything above them and
nothing below them, and the "nothing below them" is where the geology is.

Stated as an operator: let $\mathcal{F}$ map a density distribution to its
exterior field. Then

$$\mathcal{F}\ \text{is injective}\ =\ \text{false}, \qquad
\dim\ker\mathcal{F} = \infty , \qquad
\mathcal{F}\ \text{restricted to the field above the survey is invertible} . \tag{1}$$

The last clause is Question A restated: restricted to the field, the map from
boundary data to interior-of-the-harmonic-region values is invertible (and, in the
upward direction, stable). Restricted to the sources, it is wildly non-invertible.

## 2. Precise definitions

**The exterior Dirichlet problem.** Find $u$ with

$$\nabla^2u = 0 \ \text{ in } \Omega = \{\lvert\mathbf{x}\rvert > a\} , \qquad
u = f \ \text{ on } \lvert\mathbf{x}\rvert = a , \tag{2}$$

subject to the **regularity condition**

$$u = O(1/r), \qquad \lvert\nabla u\rvert = O(1/r^2) \quad\text{as } r\to\infty . \tag{3}$$

Without (3) the problem has infinitely many solutions — $u = 1$, $u = x$, $u = x^2-y^2$
are all harmonic and all vanish on no prescribed data — so (3) is part of the
problem statement, not a technicality.

**The exterior Neumann problem.** The same, with

$$\frac{\partial u}{\partial n} = g \ \text{ on } \lvert\mathbf{x}\rvert = a ,
\tag{4}$$

where $n$ is the outward normal of $\Omega$ (pointing *into* the source region).

**Well posedness.** A problem is well posed (Hadamard) if a solution exists, is
unique, and depends continuously on the data. Uniqueness and stability are
independent properties: the exterior Dirichlet problem is unique and, in the
upward direction, stable; the inverse direction (downward continuation) is unique
and violently unstable. See Section 3.7.

**Null space (annihilator).** A source distribution $\delta\rho$ whose exterior
field vanishes identically in the region of observation. Equivalently, an element
of $\ker\mathcal{F}$. The existence of one annihilator implies the existence of an
infinite family, since any multiple of it is also one.

**Equivalent stratum.** Given a field measured on a surface and any chosen depth
$h$ below it, a surface density $\sigma_h$ on the surface $z = h$ that reproduces
the measured field. The family $\{\sigma_h\}$ over all $h$ is the classical
statement of the ambiguity.

## 3. Derivations

### 3.1 Green's first identity, the tool

For a region $V$ with boundary $S$ and outward normal $n$,

$$\iiint_V\left(\lvert\nabla w\rvert^2 + w\nabla^2w\right)dV
= \oint_S w\frac{\partial w}{\partial n}\,dS . \tag{5}$$

This is the divergence theorem applied to $w\nabla w$, using
$\nabla\cdot(w\nabla w) = \lvert\nabla w\rvert^2 + w\nabla^2w$. It converts a
volume integral of a quantity that is manifestly non-negative into a boundary
integral, and it is the only tool the uniqueness proofs need.

### 3.2 Uniqueness of the exterior Dirichlet problem

**Claim.** The problem (2)–(3) has at most one solution.

*Proof.* Suppose $u_1$ and $u_2$ both solve it. Set $w = u_1 - u_2$. Then
$\nabla^2w = 0$ throughout $\Omega$, $w = 0$ on $\lvert\mathbf{x}\rvert = a$, and
by (3) $w = O(1/r)$ and $\lvert\nabla w\rvert = O(1/r^2)$.

Apply Green's first identity (5) to $w$ over the truncated region
$\Omega_R = \{a < \lvert\mathbf{x}\rvert < R\}$, whose boundary is the sphere
$r = a$ (with outward normal $-\hat{\mathbf{r}}$) and the sphere $r = R$ (with
outward normal $+\hat{\mathbf{r}}$):

$$\iiint_{\Omega_R}\left(\lvert\nabla w\rvert^2
+ w\underbrace{\nabla^2w}_{=\,0}\right)dV
= \oint_{r=a} w\frac{\partial w}{\partial n}\,dS
+ \oint_{r=R} w\frac{\partial w}{\partial n}\,dS . \tag{6}$$

The first boundary integral is zero because $w = 0$ on $r = a$. For the second,
bound the integrand using the regularity conditions:
$\lvert w\rvert \le A/R$ and $\lvert\partial w/\partial n\rvert\le B/R^2$ for
constants $A$, $B$ and all large $R$. Then

$$\left\lvert\oint_{r=R}w\frac{\partial w}{\partial n}dS\right\rvert
\le \frac{A}{R}\cdot\frac{B}{R^2}\cdot4\pi R^2 = \frac{4\pi AB}{R}
\longrightarrow 0 . \tag{7}$$

Hence, taking $R\to\infty$,

$$\iiint_\Omega\lvert\nabla w\rvert^2\,dV = 0 . \tag{8}$$

The integrand is non-negative, so $\nabla w = \mathbf{0}$ and $w$ is constant
throughout $\Omega$. The regularity condition forces that constant to be zero, so
$w\equiv0$ and $u_1 = u_2$. $\square$

Three remarks matter.

- **The regularity condition is doing real work.** With $w = O(1)$ instead of
  $O(1/r)$, the boundary term would be $O(R)$ and would not vanish; with
  $w = O(r)$, it would diverge. The theorem is about the *physical* class of
  solutions, those that decay at infinity.
- **The proof is constructive about which data matter.** The Dirichlet data are
  used only at $r = a$; nothing else about the boundary is needed.
- **The proof is a template.** Replacing $w\nabla^2w$ by anything else changes the
  conclusion: this is exactly why the source problem behaves differently.

### 3.3 The exterior Neumann problem: existence, and why the condition is not zero

The uniqueness half carries over almost unchanged. If $w$ has
$\partial w/\partial n = 0$ on $r = a$ and satisfies (3), then the first boundary
term of (6) vanishes for a different reason, the second still vanishes by (7), and
$\nabla w = \mathbf{0}$, so $w$ is constant — and the regularity condition (3)
again forces it to zero. **The exterior Neumann problem is unique with no free
additive constant**, because decay at infinity pins the constant. That is a
genuine difference from the bounded-domain problem, where the additive constant is
unconstrained.

Existence is where the interesting difference lies. Apply the divergence theorem to
$\nabla u$ over $\Omega_R$:

$$0 = \iiint_{\Omega_R}\nabla^2u\,dV
= \oint_{r=a}\frac{\partial u}{\partial n}dS + \oint_{r=R}\frac{\partial u}{\partial n}dS . \tag{9}$$

Now the second term does **not** vanish: with
$u \sim C/r$ at infinity (the regularity class), $\partial u/\partial n \sim -C/R^2$
on $r = R$, so

$$\oint_{r=R}\frac{\partial u}{\partial n}dS \longrightarrow -4\pi C . \tag{10}$$

Substituting into (9),

$$\oint_{r=a}\frac{\partial u}{\partial n}dS = 4\pi C , \qquad
\text{equivalently}\qquad
\oint_{r=a}g\,dS = 4\pi C . \tag{11}$$

**This is the existence condition for the exterior Neumann problem, and it is not
$\oint g\,dS = 0$.** In the bounded-domain problem there is no boundary at
infinity, so the divergence theorem gives $\oint g\,dS = 0$ directly; for the
exterior problem the flux through the far sphere is what balances the flux through
the near sphere. Physics: the flux of the gravity field through a closed surface is
$-4\pi G$ times the enclosed mass (lesson 01, equation 7), and the far-sphere
contribution is the same quantity seen at infinity. The prescribed normal
derivative thus *determines* the $1/r$ coefficient, which is the total mass — it
does not have to vanish.

In Newtonian gravity with the sign convention $V>0$, $\mathbf{g} = \nabla V$ (this
module), a surface mass $M$ inside $r = a$ gives $\partial V/\partial n = +GM/a^2$
on $r=a$, so $\oint g\,dS = 4\pi GM$ and $C = GM$: the far field is $V\sim GM/r$,
as it must be. The existence condition (11) is then just the statement that the
prescribed normal derivatives are consistent with some enclosed mass. Consistency
is automatic for any data of the right class; what is *not* automatic is that the
data come from that mass.

**Practical corollary for measurement.** A set of measured normal derivatives
(that is, a gravity survey) that fails (11) — because of levelling error, drift or
a datum bias — cannot be the boundary data of any harmonic field. That is a
statement about the data, not about the geology, and it is the theoretical basis
of the closure tests used to quality-control a survey.

### 3.4 Uniqueness of the field: what it does and does not constrain

Section 3.2 says: the field in $\Omega$ is a function of the boundary data. Write
$\mathcal{H}: f\mapsto u$ for the solution operator. $\mathcal{H}$ is injective,
so *the field is as well determined as the data*.

What $\mathcal{H}$ does not do is say anything about the density. The density lives
in $\Omega^c$, on the other side of the boundary on which the data are prescribed.
The theorem is silent there by construction: the boundary condition at $r = a$ is
all the information $\Omega$ ever receives about $\Omega^c$. Two different mass
distributions in $\Omega^c$ that happen to produce the same $f$ are, from the point
of view of the exterior problem, the *same problem*.

This is the logical hinge of the whole module:

$$\underbrace{\text{field unique given data}}_{\text{theorem}} \quad\not\Rightarrow\quad
\underbrace{\text{source unique given field}}_{\text{false}} . \tag{12}$$

### 3.5 The equivalent stratum: an infinite family, constructed

Now the constructive proof of non-uniqueness. Work in two dimensions, where the
algebra is exact and short.

**The field of a line mass.** A line (horizontal cylinder) of mass per unit length
$\lambda$ at depth $z_0$ produces (lesson 01, equation 13)

$$g_z(x) = \frac{2G\lambda z_0}{x^2+z_0^2} . \tag{13}$$

**The field of a surface layer.** A horizontal layer at depth $h$ with areal
density $\sigma(x)$ produces, by superposing line masses $\sigma\,dx'$,

$$g_z(x) = 2Gh\int_{-\infty}^{\infty}\frac{\sigma(x')}
{(x-x')^2+h^2}\,dx' . \tag{14}$$

**Match them in the wavenumber domain.** The Fourier transform of the kernel in
(13) is $\pi e^{-\lvert k\rvert z_0}$ (the standard Poisson-kernel transform), and
of the kernel in (14) is $\pi e^{-\lvert k\rvert h}$. Equating transforms,

$$2\pi G\,e^{-\lvert k\rvert h}\tilde\sigma(k) = 2\pi G\lambda\,e^{-\lvert k\rvert z_0}
\qquad\Longrightarrow\qquad
\tilde\sigma(k) = \lambda\,e^{-\lvert k\rvert(z_0-h)} . \tag{15}$$

Inverting the transform gives a closed form,

$$\boxed{\ \sigma_h(x) = \frac{\lambda}{\pi}\frac{z_0-h}{x^2+(z_0-h)^2}\ }
\qquad\text{for every } h < z_0 . \tag{16}$$

Equation (16) is the **equivalent stratum**. Three properties make it the cleanest
statement of the ambiguity in the whole subject:

- **It works for every $h < z_0$.** The family is one-parameter and infinite: pick
  any depth shallower than the true source and there is a density profile that
  reproduces the field exactly.
- **The total mass is the same.** $\int\sigma_h\,dx = \lambda$ for every $h$, as it
  must be, since the far-field monopole is unchanged.
- **The required density gets rougher as the stratum is placed deeper.** Here
  $\sigma_h$ has half-width $z_0-h$, so placing the stratum *shallower* (smaller
  $h$) gives a *wider, smoother* profile; placing it *deeper* (larger $h$) gives a
  *narrower, rougher, higher-amplitude* profile, with peak
  $\lambda/(\pi(z_0-h))$ diverging as $h\to z_0$. This is the spectral statement
  again: a deeper source must contain more high-wavenumber content to produce the
  same short wavelengths at the surface, and in the limit $h\to z_0$ the required
  density becomes a delta function.

The demonstration verifies (16) numerically, integrating (14) with the trapezoid
rule at five stations and comparing with (13):

| $h$ (m) | peak $\sigma_h$ (kg m$^{-2}$) | FWHM (m) | $g_z(0)$ (m s$^{-2}$) |
|---|---|---|---|
| $500$ | $1.061033\times10^{5}$ | $3000.0$ | $3.3371489379\times10^{-5}$ |
| $1000$ | $1.591549\times10^{5}$ | $2000.0$ | $3.3371485838\times10^{-5}$ |
| $1500$ | $3.183099\times10^{5}$ | $1000.0$ | $3.3371489379\times10^{-5}$ |
| $1800$ | $7.957747\times10^{5}$ | $400.0$ | $3.3371494902\times10^{-5}$ |

against the line-mass value $g_z(0) = 3.3371500000\times10^{-5}$ m s$^{-2}$. The
worst relative difference over $x = 0$, $500$, $1000$, $2000$, $5000$ m and the
three depths $h = 500$, $1000$, $1500$ m is $3.09\times10^{-6}$, and it is
**quadrature error, not physics**: refining the sheet integral at $x = 0$ for
$h = 1000$ m gives $4.244\times10^{-7}$ at half-width $50z_0$, $6.631\times10^{-9}$
at $200z_0$ and $1.036\times10^{-10}$ at $800z_0$. The four source distributions
have peaks differing by up to a factor $7.5$ and widths by a factor $7.5$, and
they are indistinguishable above the survey.

### 3.6 The annihilator, and the infinite-dimensional null space

Since every $\sigma_h$ reproduces the same field, the difference of any two of them
must produce **zero** field. The demonstration verifies this directly:

| quantity | value |
|---|---|
| peak $\lvert\sigma_{500}(0)\rvert$ | $1.061033\times10^{5}$ kg m$^{-2}$ |
| peak $\lvert\sigma_{1500}(0)\rvert$ | $3.183099\times10^{5}$ kg m$^{-2}$ |
| peak $\lvert\sigma_{500}-\sigma_{1500}\rvert$ | $2.122066\times10^{5}$ kg m$^{-2}$ |
| annihilator's field at $x=0$ | $0$ |
| largest annihilator field over the stations | $1.97\times10^{-12}$ of the peak |

The annihilator carries structure of the **same order as the signal** (its peak is
twice the peak of $\sigma_{500}$) and produces a field of order $10^{-12}$ of the
signal — the arithmetic noise floor. That is the definition of an annihilator, and
it is why the inversion problem has no unique answer: **a source contribution of
order 100 per cent of the total is invisible in the data.**

Because the null space is a linear subspace containing one non-zero element, it
contains all its multiples; and because $h$ is a continuous parameter, it is
infinite-dimensional. No finite parameterisation can remove it, and no amount of
data *of the same type* can remove it — only more or different data.

### 3.7 Uniqueness without stability

Uniqueness and stability are independent, and this is the point at which the
potential-field problem joins the general theory of
[18-inverse-problems](../../18-inverse-problems/README.md).

Consider upward continuation: given $f$ on $r = a$, find $u$ on $r = R > a$. In
the wavenumber domain the operator multiplies by $e^{-\lvert k\rvert(R-a)}$, which
is bounded by $1$ and decays. The map is injective (Section 3.2) and its norm is
$1$: **stable**.

Now reverse it: given $u$ on $r = R$, find $f$ on $r = a$. The operator multiplies
by $e^{+\lvert k\rvert(R-a)}$, which is unbounded: a noise component at wavenumber
$k$ is amplified by $e^{\lvert k\rvert(R-a)}$, without limit. The map is still
injective — the theorem guarantees a unique answer exists — but it is not
continuous. **Same theorem, same uniqueness, opposite stability.**

This is the cleanest possible demonstration that "unique" and "well determined"
are different words, and it is why every practical downward continuation is a
*stabilised* problem whose answer depends on the regularisation chosen — which is
exactly the statement that the practical answer is not unique either.

### 3.8 The three classical equivalence classes, and what breaks them

| Class | Statement | Broken by |
|---|---|---|
| Radial redistribution (Newton) | Any spherically symmetric body of mass $M$ gives $V = GM/r$ outside | Strip the sphericity assumption; add another data type that is not spherically symmetric-sensitive |
| Equivalent stratum | For every depth $h$ there is a density reproducing the field | Constrain the source's depth range or bound its density; add gravity *gradient* data (which is still harmonic and still ambiguous — it does not break the null space) |
| Slab | $g_z = 2\pi G\rho t$ fixes only the product | Measure $\rho$ by another method (logs, cores, seismic velocity) |

Notice that the third row is broken by an *independent measurement of one of the
two parameters*. That is the general pattern: the ambiguity is not resolved by more
careful inversion of the same data, and not by data of the same physical type at
more locations (which is still harmonic above the sources); it is resolved by
information that is not a value of the same harmonic field — a density
measurement, a depth constraint, a borehole that finds rock rather than air, or a
geological plausibility argument made explicit.

A useful way to remember the pattern: **the null space is the set of things the
data cannot see. Only something the data does not contain can exclude them.**

## 4. Physical interpretation

**The data live on one side of the boundary; the answer lives on the other.** A
gravity survey is a set of boundary values for the exterior Dirichlet problem.
Every theorem about that problem is a theorem about the survey, and every
interpretation step is an inference about the other side of the boundary, which
no theorem constrains. Reading Section 3.2 and Section 3.5 together is the whole of
the theory of potential-field ambiguity.

**This is not a statement about precision.** The equivalence is exact, not
approximate. Better instruments, denser stations, lower noise: none of them touch
it. They improve the *estimate of the field*, which improves the estimate of the
boundary data, which determines the field above the survey more precisely — and
says nothing new about the source.

**Why the ambiguity is nonetheless tolerable in practice.** Two reasons, and both
are legitimate:

1. *Geological constraints are strong.* Densities are positive, bounded below by
   about $1000$ kg m$^{-3}$ (saturated sediments) and above by about
   $13\,000$ kg m$^{-3}$ (the inner core, of which only a small shell is relevant
   to crustal work); sources are bounded in depth by the planet; and most crustal
   density contrasts lie in a narrow range. The feasible set is a small subset of
   the null space's complement.
2. *The ambiguity is depth-confined.* The equivalent stratum at depth $h$ requires
   density structure at scale $z_0-h$; if the data resolve a depth, the roughness
   required to place the source deeper becomes geologically absurd. Backus–Gilbert
   and Tikhonov methods formalise "absurd" as a penalty, and the resulting model is
   a *representative of the feasible set*.

The honest phrasing of a potential-field interpretation is therefore: "these data
are consistent with these sources, and here is the class of alternatives that
produce the same field."

**Deflection of the vertical, gradients and the tensor do not help, in principle.**
Every derivative of a harmonic function is harmonic, so adding gradient or
gradient-tensor data adds more constraints of the *same* type, and the null space
survives: the annihilator's field vanishes, and so do all its derivatives. The
demonstration checks this: the horizontal derivative $dg_z/dx$ of the line mass
agrees with that of the equivalent stratum to $4.8\times10^{-10}$ relative. What
gradients *do* buy is sensitivity to shorter wavelengths and hence to shallower
structure — a change in the *conditioning* of the problem, not in its null space.

**Non-uniqueness is not the same as unknowability.** Frequentist and Bayesian
formalisations make the distinction precise. The data determine a posterior
distribution over sources; that posterior is non-degenerate (the null space is
real) but it is not flat (many sources are excluded by bounds and by the data's
sensitivity profile). The useful output of a gravity inversion is the posterior or
the resolution operator, not a single density model presented as if it were
determined.

## 5. Assumptions and regime of validity

- **Harmonic region and a smooth boundary.** The proofs assume a $C^2$ boundary
  (or a Lipschitz boundary and a suitable weak formulation) and a domain with a
  well-defined exterior. For a fractal or very irregular boundary the conclusions
  survive with a more careful formulation; the physics does not change.
- **Regularity at infinity is essential.** Drop (3) and the Dirichlet problem has
  infinitely many solutions. In gravity the condition is physically automatic: a
  finite total mass produces $V = O(1/r)$.
- **Linear superposition.** The whole analysis is linear. A problem with a
  density-dependent gravitational effect (self-gravitating fluids) is nonlinear and
  the arguments change.
- **A single type of data.** The null space survives additional derivatives and
  additional stations. It does not survive an independent measurement of a
  parameter that is not a value of the same harmonic field.
- **The model class matters.** "Non-unique" is a statement about a chosen
  parameterisation. A model restricted to a single body of prescribed shape has
  finitely many parameters and the remainder of the null space manifests as a
  non-degenerate posterior over those parameters rather than as a family. Reducing
  the model class does not reduce the ambiguity; it relocates it into the model
  choice.
- **The forward operator's conditioning.** In practice the "infinite-dimensional"
  null space is accompanied by a very large ratio of largest to smallest singular
  value, so many directions are *nearly* invisible even when formally constrained.
  Truncation of a singular-value expansion is therefore not a cosmetic choice.
- **Nothing here is specific to gravity.** The same pair of results — unique field,
  non-unique source — holds for magnetics (with the extra complication of
  remanence, which makes it worse), for static electricity, for steady heat
  conduction and for DC resistivity. Only the source parameterisation changes.

## 6. Units and dimensional analysis

- Equation (11): $[\partial u/\partial n] = \text{m}^2\text{s}^{-2}\text{m}^{-1} =
  \text{m}\,\text{s}^{-2}$ (an acceleration, as it should be for a normal
  derivative of a potential), times area m$^2$ gives m$^3$ s$^{-2}$; and
  $[4\pi C]$ with $C = GM$ in m$^3$ s$^{-2}$. ✓
- Equation (16): $[\lambda/\text{length}] = \text{kg}\,\text{m}^{-1}/\text{m} =
  \text{kg}\,\text{m}^{-2}$, an areal density. ✓ The factor $(z_0-h)/(x^2+(z_0-h)^2)$
  has units of $1/\text{length}$, so $\sigma_h$ has the right units for every $h$ —
  a reminder that the family is dimensionally consistent even though its members
  are physically very different.
- The annihilator's "size" is dimensionless when expressed as a ratio of fields or
  of densities; it is worth quoting both, because the density ratio is of order
  unity while the field ratio is $10^{-12}$.

A convenient sanity relation from (15): the ratio of the required density
amplitudes at two depths is
$\tilde\sigma(h_1)/\tilde\sigma(h_2) = e^{\lvert k\rvert(h_1-h_2)}$, which is
$1$ at $k=0$ (same mass) and grows without bound as $k\to\infty$ (rougher as you
push the source deeper). That single exponential is the entire content of the
depth ambiguity and of the instability of downward continuation.

## 7. Python demonstration

[`code/uniqueness_demo.py`](./code/uniqueness_demo.py) computes every number in
Section 3, in standard-library Python:

1. **Uniqueness, numerically.** Laplace's equation on the unit square with
   $u = 1$ on the top edge, solved by Gauss–Seidel from two completely different
   initial fields. The maximum difference between the two solutions falls
   $1.290\times10^{-1}$ (10 sweeps) $\to 7.168\times10^{-5}$ (100) $\to
   9.367\times10^{-13}$ (1000) $\to 0$ (4000), while the numerical solution agrees
   with the exact series solution to $7.188\times10^{-3}$ (the discretisation error
   of a $25\times25$ grid).
2. **The equivalent stratum.** The four depth profiles, all reproducing
   $g_z(0) = 3.3371500000\times10^{-5}$ m s$^{-2}$, with the station table and the
   quadrature-refinement evidence.
3. **The annihilator.** The difference of two equivalent strata: structure of
   order the signal, field of order $2.0\times10^{-12}$ of the peak.
4. **Derivatives.** $dg_z/dx$ agrees to $4.784\times10^{-10}$ relative — gradients
   do not break the ambiguity.
5. **The slab ambiguity.** Four $(\rho,t)$ pairs with the same $\rho t$ give
   $4.478750242702\times10^{-4}$ m s$^{-2}$ to twelve decimal places.

The block worth modifying is Section 2: add a fifth depth, $h = 1950$ m with
$z_0 = 2000$ m, and watch the required peak density blow up. That divergence is
the mathematical content of "the source cannot be pushed arbitrarily deep", and it
is the reason a depth is often better determined than a density.

## 8. Common mistakes

1. **Believing the uniqueness theorem rules out ambiguity.** It is a theorem about
   the field given boundary data. The source is on the other side of the boundary.
2. **Quoting the interior Neumann existence condition for the exterior problem.**
   For a bounded domain $\oint g\,dS = 0$; for the exterior problem it is
   $\oint g\,dS = 4\pi C$ with $C$ the $1/r$ coefficient. The difference is the
   flux through the sphere at infinity.
3. **Forgetting the regularity condition.** Without $u = O(1/r)$ the exterior
   problem has infinitely many solutions and the uniqueness proof fails at (7).
4. **Thinking more data of the same type will resolve the source.** More stations,
   smaller errors and higher derivatives all leave the null space untouched; only
   independent information does.
5. **Confusing non-uniqueness with poor conditioning.** The null space is exact and
   no computation can shrink it. Conditioning is about how badly the *constrained*
   directions are amplified, and that can be improved.
6. **Presenting a single inverted density model as the answer.** It is one
   representative of an infinite class; state the class, the constraints and the
   regularisation.
7. **Assuming the ambiguity is small because the bodies look different.** The
   annihilator's *field* is $10^{-12}$ of the signal while its *density* is twice
   the signal's peak: the invisibility is total, not marginal.
8. **Expecting gravity gradients to break the ambiguity.** They are derivatives of
   a harmonic function and are harmonic themselves; the annihilator's field and
   every derivative of it vanish.
9. **Using the two-dimensional logarithmic potential without a strike length.**
   The equivalent-stratum derivation above is two-dimensional; the three-dimensional
   version (below) has the same structure with the 3-D kernels, and the two must
   not be mixed.

> **The three-dimensional version, for completeness.** Repeating Section 3.5 with
> the 3-D kernels — $(x^2+z_0^2)^{-3/2}$ for a point mass instead of
> $(x^2+z_0^2)^{-1}$ for a line mass — the same construction works: the density
> required at a chosen depth $h$ is again the inverse Fourier transform of
> $\tilde g(k)$ divided by the transform of the 3-D kernel, which is again
> *strictly positive for every $k$* and again vanishes exponentially as
> $\lvert k\rvert\to\infty$. So a one-parameter family exists for every $h < z_0$
> and the required density again grows in high-wavenumber content as $h$ increases.
> The quantitative difference from (15) is that the transform of the 3-D kernel
> involves a modified Bessel function rather than a bare exponential, so the
> amplification is no longer a pure $e^{\lvert k\rvert h}$; the qualitative
> conclusion — an infinite family of sources per field, and an unstable one in the
> deeper direction — is identical. The two-dimensional case is the one to
> remember because it is exact, closed-form and checkable by quadrature, which is
> what the demonstration does.

## 9. Real-world applications

- **Gravity and magnetic inversion.** Every "inverted" density or susceptibility
  model in the literature is a representative of an equivalence class; the
  scientific content is in the constraints and in the resolution analysis, not in
  the picture. See
  [07-03-04 Gravity Inversion and Its Severe Non-Uniqueness](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/04-inversion-gravity.md)
  and
  [08-03-06 Magnetic Inversion and Its Non-Uniqueness](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/06-magnetic-inversion.md).
- **Bouguer and terrain corrections.** The slab ambiguity of Section 3.8 is why an
  assumed density is unavoidable; the residual ambiguity then propagates into
  every anomaly and every mass estimate built on it.
- **Isostasy.** Airy and Pratt models are two *different* density distributions
  that produce almost the same gravity field, and distinguishing them requires
  independent information about crustal thickness. This is the ambiguity in its
  most consequential form —
  see [07-01-06 Isostasy: Pratt, Airy and Flexural Models](../../07-gravity-geodesy/01-gravity-fundamentals/06-isostasy.md).
- **Equivalent-source geoid modelling.** A dense layer of small masses is fitted to
  reproduce the gravity field, then used to evaluate the geoid. The depth of that
  layer is a free choice precisely because of the equivalent stratum, and the
  choice affects the result at the level of the neglected high wavenumbers.
- **Joint and multi-physics inversion.** The practical answer to ambiguity: gravity
  plus seismic, gravity plus magnetics, gravity plus well logs. Independent data
  constrain different directions and shrink the feasible set. See
  [18-07 Joint and Multi-Physics Inversion](../../18-inverse-problems/07-joint-and-multi-physics-inversion/README.md).
- **Survey design.** Since more stations do not remove the ambiguity but do improve
  the field estimate, survey design optimises the *stability* of the interpretation
  problem — station spacing against the depth of interest — rather than pretending
  to resolve it.
- **Magnetics with remanence.** The magnetic case has all the gravity ambiguity
  plus a magnetisation-direction ambiguity, which is why magnetic inversions are
  routinely run with several assumed directions and reported as a range. See
  [08-03-01 Magnetic Anomaly Physics and Remanent vs Induced Magnetisation](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md).
- **Borehole gravity and downhole gradients.** Placing the measurement *inside* the
  source region breaks the harmonic-region assumption of the theorem, which is
  exactly why borehole gravity is so much better at resolving deep structure.

## 10. Further reading

- **Kellogg, O. D. *Foundations of Potential Theory* (Springer).** The classical
  treatment of the Dirichlet and Neumann problems, existence and uniqueness, with
  the regularity conditions treated properly. Level: graduate.
- **Courant, R., & Hilbert, R. *Methods of Mathematical Physics*, Vol. II
  (Interscience).** The exterior problems and the behaviour at infinity, with the
  proofs in their general form. Level: graduate.
- **Blakely, R. J. *Potential Theory in Gravity and Magnetic Applications*
  (Cambridge University Press).** The equivalent stratum and the ambiguity as they
  are used in practice, including the wavenumber-domain statements. Level:
  advanced.
- **Grant, F. S., & West, G. F. *Interpretation Theory in Applied Geophysics*
  (McGraw-Hill).** The classical statement of the ambiguity and the standard
  counterexamples. Level: advanced.
- **Parker, R. L. *Geophysical Inverse Theory* (Princeton University Press).** The
  general theory: null spaces, resolution operators and the Backus–Gilbert
  approach, with the gravity problem as the worked example. Level: graduate.
- **Aster, R. C., Borchers, B., & Thurber, C. H. *Parameter Estimation and
  Inverse Problems* (Academic Press).** The practical formulation: regularisation,
  resolution and the honest reporting of a non-unique solution. Level: graduate.
- **Backus, G. E., & Gilbert, F. (1967–1970). Numerical applications of a
  formalism for geophysical inverse problems. *Geophysical Journal International*,
  several papers.** The origin of the resolution-operator formalism; read the
  first for the statement and the third for the gravity application. Level:
  graduate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (Cambridge University Press).** The ambiguity discussed as an operational
  problem with worked examples. Level: advanced.
- **ICGEM, International Centre for Global Earth Models.**
  <https://icgem.gfz-potsdam.de/> — the coefficient sets that are *determined*
  (the field, Question A), as opposed to the mass distributions that are not
  (Question B). Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [01 Newtonian Gravitational Potential and Field](./01-gravitational-potential.md)
  — the forward operator whose null space this lesson characterises.
- [02 Laplace's Equation and Harmonic Functions](./02-laplace-equation.md) — the
  properties the uniqueness proof uses.
- [03 Spherical Harmonics and Multipole Expansions](./03-spherical-harmonics.md) —
  the unique-but-truncated description of the field, in the basis where Question A
  is answered.
- [04 Poisson's Equation and Source Distributions](./04-poisson-equation.md) — the
  source equivalences that make the ambiguity constructive.
- [05 Equipotential Surfaces, Geoid and Level Surfaces](./05-equipotentials.md) —
  a boundary-value problem whose solution (the geoid) is unique while the mass
  distribution inside is not.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the general theory
  of which this lesson is the canonical example.
- [01-07-04 Rank, Null Space and Solvability (Existence and Uniqueness)](../../01-mathematics/07-linear-algebra/04-rank-and-nullspace.md)
  — the finite-dimensional version of the same dichotomy.

Exercises:
[`exercises/06-uniqueness-theorems-exercises.md`](./exercises/06-uniqueness-theorems-exercises.md)
and
[`exercises/06-uniqueness-theorems-solutions.md`](./exercises/06-uniqueness-theorems-solutions.md).

## Self-assessment checklist

- [ ] I can state the exterior Dirichlet problem including its regularity
      condition, and explain why the condition is not optional. (Section 2)
- [ ] I can prove uniqueness of the exterior Dirichlet problem and say where each
      term of the proof is used. (Section 3.2)
- [ ] I can derive the exterior Neumann existence condition and explain why it is
      not $\oint g\,dS = 0$. (Section 3.3)
- [ ] I can explain why the free additive constant of the bounded Neumann problem
      disappears for the exterior problem. (Section 3.3)
- [ ] I can state and prove the corollary that uniqueness of the field does not
      imply uniqueness of the source. (Section 3.4)
- [ ] I can derive the equivalent stratum in two dimensions and describe how the
      required density depends on the chosen depth. (Section 3.5)
- [ ] I can explain what an annihilator is and why its existence makes the null
      space infinite-dimensional. (Section 3.6)
- [ ] I can explain why uniqueness does not imply stability and give the upward and
      downward continuation example. (Section 3.7)
- [ ] I can list three equivalence classes and say what would break each one.
      (Section 3.8)
- [ ] I can state what additional information actually reduces the ambiguity and
      what does not. (Sections 3.8, 4)
