---
id: 12-06-01
title: "Moment of Inertia, Figure and Interior Constraints"
level: doctoral
prereqs: ["12-01-01", "07-01-03", "02-02-05"]
tags: [global-geophysics, earth-interior, geodesy, moment-of-inertia, figure, non-uniqueness]
---

# Moment of Inertia, Figure and Interior Constraints

> All models and data in this module are **SYNTHETIC**. The "planet" used
> throughout is a teaching body with chosen mass, radius, density contrast and
> rotation rate. No number below is a measurement of the Earth or of any other
> real body. The only externally quoted quantities are exact standard constants
> ($G$) and exact mathematical results (the inertia factors $2/5$ and $2/3$, and
> the small-rotation values derived in the text).

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the moment-of-inertia factor $C/MR^{2}$ of a spherically symmetric
   body as a weighted integral of its density profile, and **bound** it between
   the exact values for a uniform sphere and a thin shell.
2. **Compute** $C/MR^{2}$ for a two-layer body in closed form and **show** that
   the mass and radius are already used up in the normalisation.
3. **Demonstrate** the non-uniqueness of the density profile from a single
   $C/MR^{2}$: construct the one-parameter family of interiors that reproduces it.
4. **Derive** the hydrostatic figure of a rotating homogeneous body from the
   exact spheroid potential, and **measure** the classical limits
   $f/q = 5/4$ and $J_{2}/q = 1/2$.
5. **Apply** the first-order (Clairaut-style) figure solver to layered fluid
   bodies and **calibrate** it against the exact homogeneous result.
6. **Combine** the moment of inertia with the figure response and **state** what
   is determined, what is assumed, and how adding a third structure parameter
   creates a ridge of equally acceptable models.
7. **Convert** an adopted $(C/MR^{2}, J_{2})$ pair into the dynamical ellipticity
   $H$ and the rigid-body free-wobble period, and **state** why the observed
   wobble is not that number.

## Prerequisites

- [12-01-01 PREM, IASP91 and Reference Earth Models](../01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) —
  the reference models whose radial density profiles make moments of inertia
  computable in the first place.
- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../../07-gravity-geodesy/01-gravity-fundamentals/03-normal-gravity.md) —
  the ellipsoidal figure, normal gravity and the hydrostatic flattening relation.
- [02-02-05 Rotational Motion, Moment of Inertia and Angular Momentum](../../02-physics/02-classical-mechanics/05-rotation.md) —
  the inertia tensor and angular momentum, which this lesson applies to a planet.

## 1. What a moment of inertia is, and what it is not

A moment of inertia is not a measurement. For a planetary body we infer a
*ratio*: the ratio of the polar moment of inertia to $MR^{2}$. What a spacecraft
(or a satellite's orbit, or a precession rate) delivers is a number that depends
on the *internal distribution* of mass; the interpretation step — "this number
means the core is such-and-such a size" — is a model, and this lesson is about
making the size of that step explicit.

Three things follow immediately, and they organise the whole lesson:

- $C/MR^{2}$ is a **functional of the density profile** $\rho(r)$, not a local
  property. Two profiles that agree in a weighted radial average are
  indistinguishable in this observable.
- Every measurement is made **relative to a reference model**: a radius, a
  reference figure, a mass. Changing the reference changes the number.
- The figure of a rotating body delivers a *second* functional of the same
  profile. Two observables and one unknown profile give either a constrained
  family or, if the family is parameterised with only two numbers, an apparently
  unique answer — which is an artefact of the parameterisation, not of the data.

## 2. $C/MR^{2}$ as a weighted integral

For a spherically symmetric body of mass $M$ and radius $R$, take the rotation
axis through the centre. A shell of thickness $\mathrm{d}r$ at radius $r$ has
mass $\mathrm{d}m = 4\pi r^{2}\rho(r)\,\mathrm{d}r$ and contributes
$(2/3)\,\mathrm{d}m\,r^{2}$ to the polar moment. Hence

$$
\boxed{\;\frac{C}{MR^{2}} = \frac{1}{M R^{2}}\int_{0}^{R}
\frac{2}{3}\,r^{2}\,\rho(r)\,4\pi r^{2}\,\mathrm{d}r
= \frac{8\pi}{3MR^{2}}\int_{0}^{R}\rho(r)\,r^{4}\,\mathrm{d}r.}
$$

The weight $r^{4}/R^{4}$ shows why a moment of inertia says almost nothing about
the outermost layers and a great deal about the middle: a mass element at
$r = 0.5R$ contributes 14 times as much as one at the surface, per unit mass.

**Exact bounds.** A uniform sphere gives

$$
\int_{0}^{R}\rho_{0}r^{4}\,\mathrm{d}r = \frac{\rho_{0}R^{5}}{5},
\qquad M = \frac{4\pi}{3}\rho_{0}R^{3}
\;\Longrightarrow\;
\frac{C}{MR^{2}} = \frac{2}{5},
$$

and a thin shell (all mass at $r = R$) gives $C = MR^{2}$ with $C$ replaced by
the shell value $(2/3)MR^{2}$:

$$
\frac{C}{MR^{2}} = \frac{2}{3}.
$$

So $0.4 \le C/MR^{2} \le 0.6667$ for any spherically symmetric body. The
demonstration checks both by numerically integrating the profile:

```text
uniform sphere : C/MR^2 = 2/5 = 0.400000   quadrature 0.400000   error 1.46e-08
thin shell     : C/MR^2 = 2/3 = 0.666667   quadrature 0.666600   error 6.67e-05
```

The thin-shell error is $6.7\times10^{-5}$: the quadrature resolves a slab of
finite thickness, not a true delta function. Saying so is part of the result.

## 3. Fully worked example: a two-layer body

Let the body have a uniform core of radius $r_{c} = x R$ and density
$\rho_{c} = \alpha\rho_{m}$, and a uniform mantle of density $\rho_{m}$ out to
$R$. The moment of inertia is the sum of a solid sphere and a uniform shell:

$$
C = \frac{2}{5}m_{c}r_{c}^{2}
+ \frac{2}{5}m_{m}R^{2}\,\frac{1-x^{5}}{1-x^{3}},
$$

with $m_{c} = \tfrac{4}{3}\pi\rho_{c}x^{3}R^{3}$ and
$m_{m} = \tfrac{4}{3}\pi\rho_{m}(1-x^{3})R^{3}$. The shell factor
$(1-x^{5})/(1-x^{3})$ is the standard result for a uniform shell; it tends to
$5/3$ as $x\to1$, giving $(2/3)m_{m}R^{2}$, and to 1 as $x\to0$.

*Numerical check.* With $x = 0.5$ and $\alpha = 2.0$, the demonstration reports
$C/MR^{2} = 0.3667$; the same body with $\alpha = 1$ (uniform) gives $0.4000$, and
with $\alpha = 3.5$ gives $0.3286$. The full table is

```text
   x_core  alpha=1.0  alpha=1.5  alpha=2.0  alpha=2.5  alpha=3.5
    0.20      0.4000     0.3985     0.3970     0.3954     0.3925
    0.35      0.4000     0.3926     0.3856     0.3788     0.3660
    0.50      0.4000     0.3824     0.3667     0.3526     0.3286
    0.65      0.4000     0.3721     0.3502     0.3326     0.3060
    0.80      0.4000     0.3706     0.3512     0.3374     0.3192
```

Note the non-monotonic column for $\alpha = 3.5$: a very dense *small* core
contributes little inertia even though it dominates the mass, because the weight
$r^{4}$ penalises it. That is the first hint that "core size from the moment of
inertia" is a statement about a compromise, not a boundary.

## 4. Non-uniqueness: one number, a family of interiors

Adopt the synthetic constraint $C/MR^{2} = 0.3350$ for a body with
$M = 4.0\times10^{24}\ \mathrm{kg}$ and $R = 3.0\times10^{6}\ \mathrm{m}$.
Solving the two-layer expression for $\alpha$ at each core size gives

```text
   x_core   alpha required   mantle rho (kg/m^3)   core rho (kg/m^3)
    0.15        60.0775              29488.2          1771577.6
    0.25        14.4194              29237.4           421583.8
    0.35         6.3008              28818.2           181578.2
    0.45         3.8083              28161.2           107245.9
    0.55         2.8256              27128.0            76653.4
    0.65         2.4258              25415.8            61654.2
```

Every row reproduces the same $C/MR^{2}$. The constraint is a **curve** in the
$(x, \alpha)$ plane and the mass and radius have already been used up in forming
$C/MR^{2}$; nothing remains to pick a row. A real study has a measured
$C/MR^{2}$ with an error bar, and the answer is then the band of rows within that
bar — still a band.

## 5. The figure: an exact homogeneous result and a first-order machine

### 5.1 Why the figure is a second, independent functional

A rotating fluid body adjusts its shape until its surface is an equipotential of
gravity plus centrifugal potential. For a homogeneous body the answer is known
exactly: the figure is an oblate spheroid, and its flattening follows from the
closed-form internal potential of a spheroid,

$$
V(\varpi,z) = -\pi G\rho\left[I_{0} - A_{1}\varpi^{2} - A_{3}z^{2}\right],
\qquad
A_{1} = \frac{\sqrt{1-e^{2}}}{e^{3}}\arcsin e - \frac{1-e^{2}}{e^{2}},
\quad
A_{3} = \frac{2}{e^{2}}\left(1 - \frac{\sqrt{1-e^{2}}}{e}\arcsin e\right),
$$

with $I_{0} = 2ac\arcsin(e)/e$ and eccentricity $e = \sqrt{1-c^{2}/a^{2}}$.
Requiring equal potential at the pole and the equator gives the **Maclaurin
condition**

$$
A_{1}a^{2} - A_{3}c^{2} = \tfrac{2}{3}\,q\,ac,
\qquad
q \equiv \frac{\omega^{2}a^{3}}{GM},
$$

where $M = \tfrac{4}{3}\pi\rho a^{2}c$ is the mass of the spheroid and $a$ its
equatorial semi-axis. With $x = c/a$ this is a single equation for $x$ at each
$q$: a body spun faster is flatter, and the relation is exact for a homogeneous
fluid, not first order.

The demonstration solves this condition numerically and reports

```text
   q          c/a        f=(a-c)/a       f/q        J2/q
      1e-04    0.99988   1.249877e-04     1.2499     0.4999
      1e-03    0.99875   1.248774e-03     1.2488     0.4992
      3e-03    0.99626   3.738989e-03     1.2463     0.4976
      1e-02    0.98762   1.237865e-02     1.2379     0.4921
      3e-02    0.96357   3.643240e-02     1.2144     0.4769
```

so in the small-rotation limit

$$
\frac{f}{q} \longrightarrow \frac{5}{4} = 1.2500,
\qquad
\frac{J_{2}}{q} \longrightarrow \frac{1}{2} = 0.5000 ,
$$

with $J_{2} \equiv (C-A)/(MR^{2})$ for the deformed body. These are the classical
homogeneous-fluid values, obtained here by solving the exact condition rather
than by quoting them; note that they *drift* at finite $q$ (at $q = 0.03$ they
are $1.2144$ and $0.4769$), which is the price of using a first-order formula
outside its regime.

### 5.2 The first-order machine, calibrated

For layered bodies the exact spheroid potential is unavailable, and the standard
route is first order in the deformation: each displaced interface *is* a
degree-2 surface-density shell, whose potential is known in closed form:

$$
V_{2}(r) = -\frac{4\pi G\sigma_{2}}{5}
\times
\begin{cases}
R^{4}/r^{3}, & r \ge R,\\[2pt]
r^{2}/R, & r < R,
\end{cases}
\qquad
V = V_{2}\,P_{2}(\cos\theta).
$$

A displaced interface with radial P2 amplitude $\varepsilon$ carries
$\sigma_{2} = (\rho_{\text{in}} - \rho_{\text{out}})\,r\,\varepsilon$. Imposing
that the degree-2 part of the potential vanish on every interface gives a linear
system for the interface amplitudes. The demonstration checks the kernel against
direct quadrature

```text
   r/R    closed form (J/kg)     quadrature (J/kg)    relative error
    0.4        -8.05168583e-02        -8.05163944e-02    5.8e-06
    0.9        -4.07616595e-01        -4.07567937e-01    1.2e-04
    1.5        -1.49105293e-01        -1.49104292e-01    6.7e-06
    3.0        -1.86381616e-02        -1.86380265e-02    7.3e-06
```

and then calibrates the machine on the case whose exact answer is known:

```text
   x_core  alpha    eps_core     eps_surf     f/q     J2/q    C/MR^2
    0.00   1.00           ---   -3.3333e-03   1.2500  0.4979    0.4000
    0.30   1.50   -2.7626e-03   -3.2729e-03   1.2273  0.4829    0.3952
    0.50   2.00   -2.3316e-03   -2.9404e-03   1.1027  0.4003    0.3667
    0.70   3.50   -1.9462e-03   -2.3597e-03   0.8849  0.2558    0.3058
```

The uniform row reproduces $f/q = 1.2500$ against the exact $1.2499$: the
residual is the finite-$q$ term, not a solver error. Two physical results fall
out. First, **central condensation lowers both** $C/MR^{2}$ and $J_{2}/q$: a body
that concentrates its mass towards the axis is harder to make oblate *and* has a
smaller inertia factor. Second, the core interface is *less* flattened than the
surface, $|\varepsilon_{\text{core}}| < |\varepsilon_{\text{surf}}|$: the
rotational bulge does not propagate inwards undiminished, because the deeper
material is confined by the weight above it.

## 6. Combining the two observables: what is determined, what is assumed

Take the two-layer family and require both $C/MR^{2} = 0.3350$ and a value of
$J_{2}/q$. A two-parameter family matched to two numbers has an isolated
solution — but the solution is a statement about the *family*. Add a third
parameter (a linear density gradient across the mantle, with $\gamma$ the
fractional density drop) and let the same two numbers be the entire data set.
The demonstration recovers

```text
   x_core   alpha     gamma     C/MR^2    J2/q      misfit
    0.30    2.7304    0.5306    0.3411    0.3347    1.1e-14
    0.37    2.3542    0.4577    0.3411    0.3347    3.7e-14
    0.45    2.2000    0.3500    0.3411    0.3347    1.1e-16
    0.53    2.2348    0.1937    0.3411    0.3347    6.2e-14
    0.60    2.4430   -0.0297    0.3411    0.3347    4.1e-14
```

Five different interiors, all fitting the same two numbers to machine precision,
and the true model ($x = 0.45$, $\alpha = 2.20$, $\gamma = 0.35$) is among them —
recovered, but not distinguished. The honest summary is: **geodesy constrains the
family; the family is an assumption.**

## 7. From figure to rotation: the dynamical ellipticity

Two exact identities connect the geodesy to the rotation, and neither involves a
model:

$$
J_{2} = \frac{C-A}{MR^{2}},
\qquad
H \equiv \frac{C-A}{C} = \frac{J_{2}}{C/MR^{2}} .
$$

The second is exact for any body with $A = B$. A rigid body with dynamical
ellipticity $H$, spinning at $\Omega$, has a free wobble whose inertial period is
$1/H$ sidereal days; the demonstration tabulates it:

```text
   C/MR^2      J2         H        1/H (sidereal days, rigid body)
   0.4000   5.00e-03    1.2500e-02             80.0
   0.3350   5.00e-03    1.4925e-02             67.0
   0.3350   2.50e-03    7.4627e-03            134.0
   0.3350   7.50e-03    2.2388e-02             44.7
```

Two things must be said about the last column. It is the period of a **rigid**
body: a real body deforms, and the deformation lengthens the wobble, so an
observed wobble is *not* a measurement of $H$ until the deformation is modelled
(lesson [03](03-nutation-constraints.md)). And it is a period of the *free*
motion: it appears in an observation only if the body is left to wobble, which
requires that its free mode be excited and not damped away.

## 8. Assumptions and regime of validity

| Assumption | Where it enters | What breaks it |
|---|---|---|
| Spherical symmetry of the density profile | §§2–4 | Rotation, tides, large-scale heterogeneity |
| Uniform layers | §§3–4 | Graded profiles (the ridge of §6 uses a gradient to show this) |
| Hydrostatic equilibrium | §5 | A fossil or dynamically supported figure; then $J_{2}$ cannot be used as a figure datum |
| Small deformation ($\varepsilon \ll 1$) | §5.2 | Rapid rotation: at $q = 0.03$ the linear results are already 3% off |
| Linear figure theory, first order in $\varepsilon$ | §6 | The same, and any interface whose density contrast is not sharp |
| $A = B$ (no triaxiality) | §7 | A body in a spin–orbit resonance with a permanent triaxiality |

The first-order machine of §5.2 is calibrated on the one case where the exact
answer is known. That is the strongest check available inside the model; it does
not certify the model outside its regime, and a study that uses it on a rapidly
rotating body must re-derive the finite-$q$ corrections.

## 9. Python demonstration

[`code/moment_of_inertia_demo.py`](code/moment_of_inertia_demo.py) runs in under
a second and prints every number quoted above:

1. inertia factors of a uniform sphere and a thin shell, exact and by quadrature;
2. the two-layer $C/MR^{2}$ table and its limits;
3. the non-uniqueness ridge for an adopted $C/MR^{2}$;
4. the degree-2 shell potential, closed form against quadrature;
5. the exact Maclaurin spheroid and the measured limits $f/q$ and $J_{2}/q$;
6. the exact internal spheroid potential against a three-dimensional quadrature;
7. the layered figure solver, calibrated on the homogeneous case;
8. the three-parameter ridge of §6;
9. the exact conversion of an adopted $(C/MR^{2}, J_{2})$ pair into $H$.

```bash
cd 12-global-geophysics-interior/06-geodesy-constraints-interior/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python moment_of_inertia_demo.py
```

## 10. Exercises

The graded problem set with full solutions is in
[`exercises/01-moment-of-inertia-exercises.md`](exercises/01-moment-of-inertia-exercises.md)
and
[`exercises/01-moment-of-inertia-solutions.md`](exercises/01-moment-of-inertia-solutions.md).

## Mastery checkpoint

Without notes:

> A synthetic planet has $M = 4.0\times10^{24}\ \mathrm{kg}$,
> $R = 6.0\times10^{6}\ \mathrm{m}$, an adopted $C/MR^{2} = 0.3350$ and an
> adopted $J_{2}$ such that $H = 1.5\times10^{-2}$.
> **(a)** Compute the rigid-body free-wobble period in sidereal days.
> **(b)** For a two-layer model with $x = 0.45$, state the density contrast
> required by the moment of inertia (use the ridge table of §4 as a guide) and
> say in one sentence why the same $C/MR^{2}$ admits $x = 0.25$.
> **(c)** Explain why the layered figure solver's $J_{2}/q$ falls from $0.4979$ to
> $0.2558$ between the uniform and the $x = 0.7$ models.
> **(d)** Name the single extra observable that would most reduce the remaining
> ambiguity, and say what assumption would still remain afterwards.

Worked versions of (a) and (c) appear in the lesson-01
[solutions](exercises/01-moment-of-inertia-solutions.md).

## Common pitfalls

1. **Reporting a core radius from a moment of inertia alone.** §4 is the
   counter-example: the observable defines a curve.
2. **Forgetting that $M$ and $R$ are already inside $C/MR^{2}$.** There is no
   second constraint hiding in them.
3. **Using a first-order figure formula at large $q$.** At $q = 0.03$ the
   homogeneous result is $1.2144$ instead of $1.2500$: a 3% systematic error.
4. **Treating $J_{2}$ as a hydrostatic quantity without checking.** A
   non-hydrostatic figure contaminates every inference drawn from the figure.
5. **Quoting a rigid-body wobble period as an observation.** Rigidity is the
   assumption that needs testing, not the result.
6. **Confusing detection with determination.** $C/MR^{2}$ detects central
   condensation immediately and determines a boundary only with an assumed
   family.

## Related modules

- [12-06-02 Love Numbers and Theoretical Tides](02-tidal-love-numbers.md) — the
  same figure theory in a tidal setting, and the observables that follow.
- [12-06-03 Nutation and Constraints on Core Properties](03-nutation-constraints.md) —
  what rotation observations add to the interior picture, and the free core
  nutation.
- [12-01-01 PREM, IASP91 and Reference Earth Models](../01-seismic-structure-of-the-earth/01-prem-and-reference-models.md) —
  where the density profiles used here come from in practice.
- [07-04 Geodesy and Reference Frames](../../07-gravity-geodesy/04-geodesy-reference-frames/README.md) —
  the frames, datums and heights in which such results are expressed.
- [07-05 Satellite Gravimetry](../../07-gravity-geodesy/05-satellite-gravimetry/README.md) —
  how the degree-2 coefficients of a real body are actually determined.
- [18-03 Regularization](../../18-inverse-problems/03-regularization/README.md) —
  the systematic treatment of ridges, null spaces and parameterisation choices.
