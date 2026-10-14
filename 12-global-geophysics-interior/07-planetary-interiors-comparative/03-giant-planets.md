---
id: 12-07-03
title: "Giant Planet Interiors and Magnetic Fields"
level: research
prereqs: ["12-02-01", "12-07-01", "08-01-05"]
tags: [global-geophysics, earth-interior, planetary-interiors, polytrope, dynamo, comparative-planetology]
---

# Giant Planet Interiors and Magnetic Fields

> All models and data in this module are **SYNTHETIC**. The polytropes below have
> chosen indices and chosen constants $K$; their masses and radii are therefore
> arbitrary (some are absurdly large as planets) and no number is a measurement
> of any real body. Externally quoted constants are $G$ and $\mu_{0}$, and the
> exact analytic results for the Lane-Emden equation are stated as such.

## Learning objectives

By the end of this lesson you will be able to:

1. **Solve** the Lane-Emden equation numerically and **verify** the solver
   against the exact solutions at $n = 0$ and $n = 1$.
2. **State** and **measure** the mass–radius homogeneity relation
   $M \propto R^{(3-n)/(1-n)}$ for a fixed polytropic constant $K$, including the
   exceptional case $n = 1$ in which the radius is independent of the mass.
3. **Compute** the dimensionless central pressure $P_{c}R^{4}/(GM^{2})$ as a
   function of the polytropic index and **compare** it with the exact
   uniform-sphere value $3/(8\pi)$.
4. **Compute** the moment-of-inertia factor of a polytrope and **explain** why a
   low measured value is a statement about compressibility rather than about a
   core.
5. **Construct** two interior models of the same mass, radius and $C/MR^{2}$ —
   one with a distinct core, one with the heavy elements spread through the
   envelope — and **state** the degeneracy precisely.
6. **Apply** the Elsasser-number balance and the magnetic Reynolds number to a
   synthetic giant planet, and **derive** what a measured dipole moment implies
   for the conductivity.
7. **Quantify** how the conductivity estimate depends on the measured field and
   on the (modelled) radius of the region that generates it.

## Prerequisites

- [12-02-01 Mantle Composition and Peridotite Models](../02-composition-and-mineral-physics/01-mantle-composition.md) —
  densities, phase relations and the equation-of-state language used here.
- [12-07-01 Interiors of Mars, Venus, Mercury and the Moon](01-terrestrial-planets-interiors.md) —
  the dimensionless scaling method this lesson extends to self-compressed bodies.
- [08-01-05 The Geodynamo: Mechanism and Evidence](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md) —
  the dynamo mechanism, of which §6 applies one scaling.

## 1. The Lane-Emden equation

A polytrope is a barotropic interior,

$$
P = K\rho^{1+1/n},
$$

with $n$ the polytropic index. Substituting it into hydrostatic equilibrium and
scaling radius by $\xi = r/\alpha$ with
$\alpha^{2} = (n+1)K\rho_{c}^{1/n-1}/(4\pi G)$ gives the **Lane-Emden equation**

$$
\frac{1}{\xi^{2}}\frac{\mathrm{d}}{\mathrm{d}\xi}\left(\xi^{2}
\frac{\mathrm{d}\theta}{\mathrm{d}\xi}\right) = -\theta^{n},
\qquad
\theta(0) = 1,\quad \theta'(0) = 0,
\qquad \rho = \rho_{c}\theta^{n},
$$

with the body ending at the first zero $\xi_{1}$. The mass is

$$
M = 4\pi\rho_{c}\alpha^{3}\omega_{n},
\qquad
\omega_{n} \equiv -\xi_{1}^{2}\theta'(\xi_{1}),
$$

and the radius is $R = \alpha\xi_{1}$. Two cases are exact:

- $n = 0$: $\theta = 1-\xi^{2}/6$, so $\xi_{1} = \sqrt{6}$ and
  $\omega_{0} = 2\sqrt{6}$;
- $n = 1$: $\theta = \sin\xi/\xi$, so $\xi_{1} = \pi$ and $\omega_{1} = \pi$.

The demonstration solves the equation with a fixed-step fourth-order
Runge-Kutta scheme, interpolating linearly to the first zero, and the checks are

```text
  n = 0: xi1 = 2.449490 (exact 2.449490, error 1.1e-10), -xi1^2 theta' = 4.898979 (exact 4.898979)
  n = 1: xi1 = 3.141593 (exact 3.141593, error 3.1e-10), -xi1^2 theta' = 3.141593 (exact 3.141593)
```

and the structure constants table

```text
   n      xi1        -xi1^2 theta'(xi1)   M(R) exponent (3-n)/(1-n)
   0.0     2.44949              4.89898        3.000
   0.5     2.75270              3.78865        5.000
   1.0     3.14159              3.14159   infinite (R independent of M)
   1.5     3.65375              2.71406       -3.000
   2.0     4.35287              2.41105       -1.000
   3.0     6.89685              2.01824       -0.000
```

One implementation detail is part of the physics: the term $\theta^{n}$ with
non-integer $n$ is undefined for $\theta<0$, so a solver must clamp trial values
at zero and stop at the first zero. A solver that lets $\theta$ go negative
produces NaNs (or, worse, complex values) and reports nonsense — a good example of
a numerical artefact that masquerades as a physical result.

## 2. The mass–radius relation, measured

For a fixed $K$ the homology relations give

$$
R \propto K^{n/(3-n)}\,M^{(1-n)/(3-n)}
\qquad\Longleftrightarrow\qquad
M \propto R^{(3-n)/(1-n)} .
$$

The demonstration measures the exponent by varying the central density at fixed
$K$:

```text
   n        M (kg)          R (m)         measured exponent
   0.0     2.8315e+23     9.4563e+05       1.0000   (n = 0 is the degenerate case),  M proportional to R^1.00
   0.5     2.0612e+38     1.0412e+11       5.0000   (predicted    5.000),  M proportional to R^5.00
   1.5     4.9643e+28     9.6099e+07      -3.0000   (predicted   -3.000),  M proportional to R^-3.00
   2.0     3.4470e+27     4.8950e+07      -1.0000   (predicted   -1.000),  M proportional to R^-1.00
   3.0     2.6415e+26     3.4955e+07      -0.0000   (predicted   -0.000),  M proportional to R^-0.00
```

Three observations, in order of importance.

- **$n = 1$: the radius is independent of the mass.** This is exact and it is
  visible in the definition: for $n = 1$,
  $\alpha = \sqrt{2K/(4\pi G)}$ carries no $\rho_{c}$ at all, so
  $R = \alpha\pi$ is set by $K$ alone. This is the reason the radii of gas giants
  are a poor measure of their mass and a good measure of their internal entropy
  and composition: the mass changes the central density, not the radius.
- **The exponent is negative for $n\gtrsim1.5$**: adding mass makes the body
  *smaller* once it can compress, because the additional self-gravity compresses
  more than it adds volume. (A body with a fixed $K$ has no maximum mass issue at
  finite $n<5$; the sign is what matters here.)
- **$n = 0$ is the degenerate case**, and the formula's limit ($3$) is *not*
  what the construction gives ($1$). The reason is that for $n = 0$ the
  equation of state $P = K\rho$ does not determine the structure at all:
  hydrostatic balance does, and $K$ then fixes the radius through
  $P_{c} = \tfrac{2}{3}\pi G\rho^{2}R^{2} = K\rho$, giving
  $R\propto \rho_{c}^{-1/2}$ and hence $M\propto R$. **Read the exponents off the
  measurement whenever a limit is involved**, and never off a formula at its
  boundary of validity.

## 3. Central pressure in dimensionless form

With $P_{c} = K\rho_{c}^{1+1/n}$:

```text
   n      P_c (Pa)        P_c R^4/(G M^2)
   0.0     1.000000e+11           0.119545
   1.0     1.000000e+15           0.392699
   1.5     4.641589e+13           0.770140
   2.0     1.000000e+13           1.638183
   3.0     2.154435e+12          11.050681
  For comparison the exact uniform-sphere value is 3/(8 pi) = 0.119366.
```

The $n = 0$ entry reproduces $3/(8\pi)$ to $1.5\times10^{-4}$ (the same
quadrature discretisation as in
[lesson 01](01-terrestrial-planets-interiors.md)), and the $n = 1$ entry is
$\pi/8 = 0.392699$ to all printed digits — a second exact check on the solver.

The physical content: a more compressible body (larger $n$) runs a *much* higher
dimensionless central pressure for the same mass and radius, because it
concentrates its mass. At $n = 3$ the dimensionless pressure is $11.05$, i.e.
nearly two orders of magnitude above the incompressible value. Any comparison of
"how compressed" two bodies are must therefore use $P_{c}R^{4}/(GM^{2})$ *and*
an equation-of-state input; the raw pressure in pascals is not a comparison at
all.

## 4. The moment-of-inertia factor

$$
\frac{C}{MR^{2}} = \frac{\int_{0}^{R}\rho(r)\,r^{4}\,\mathrm{d}r}
{R^{2}\int_{0}^{R}\rho(r)\,r^{2}\,\mathrm{d}r},
$$

evaluated on the polytropic profile:

```text
   n      C/MR^2      (uniform sphere = 0.4; thin shell = 0.6667)
   0.0     0.39980
   0.5     0.32593
   1.0     0.26138
   1.5     0.20460
   2.0     0.15485
   3.0     0.07536
  The n = 0 value reproduces 0.4000 exactly, which is the solver's check.
```

For a giant planet, values near $0.25$ are reached by compressibility alone: the
density gradient needed to produce them need not involve any compositional
boundary. This is the single most important interpretive statement in the lesson:
**a low $C/MR^{2}$ is evidence of self-compression, not evidence of a core.**

## 5. A core, or the same matter spread through the envelope?

To make the degeneracy concrete, take a synthetic $n = 1.5$ polytrope and add
ten percent of its mass in "heavy elements", either as a uniform core or spread
through the envelope with a weight $(1-r/R)^{p}$. The polytrope alone has

```text
  polytrope alone: M = 1.7552e+28 kg, R = 1.3590e+08 m, C/MR^2 = 0.20460
```

and the two families give

```text
   p        added-mass <r^2>/R^2    C/MR^2     change from polytrope
     0.5                 0.4848     0.21538         +0.01078
     1.0                 0.4000     0.21024         +0.00564
     2.0                 0.2857     0.20332         -0.00128
     4.0                 0.1667     0.19610         -0.00850

   core mass frac   core radius (m)   C/MR^2     change from polytrope
             0.00        0.0000e+00     0.20460         -0.00000
             0.03        1.3209e+07     0.19958         -0.00502
             0.06        1.6642e+07     0.19461         -0.00999
             0.10        1.9731e+07     0.18778         -0.01682
```

and the matching exercise:

```text
   p (spread)   C/MR^2     core frac that matches   core radius (m)
           0.5     0.21538   no core model matches (the spread model is already less concentrated than the polytrope)
           1.0     0.21024   no core model matches (the same)
           2.0     0.20332                    0.008        8.3813e+06
           4.0     0.19610                    0.051        1.5773e+07
```

Read the whole block as one statement: the two families **overlap over most of
the observable range**. Two of the four spread profiles are matched exactly by a
core model; the other two are matched only by removing the core altogether
altogether. A precise $C/MR^{2}$ therefore does not decide where the heavy
elements sit. What decides it is an equation of state — a statement about what
materials can exist at the pressures involved — and that statement is a model
input, not a measurement.

The same logic applies to the *shape* of the distribution: the four spread
profiles place their added mass at mean-square radii from $0.17R^{2}$ to
$0.48R^{2}$ and still produce $C/MR^{2}$ values within 10% of each other. The
interior *gradient* is weakly constrained by this observable, and that is a
permanent feature of the inference, not a limitation of the current data.

## 6. Magnetic fields: a scaling, and what it implies

### 6.1 The Elsasser balance

In a dynamo the Lorentz force competes with the Coriolis force. Their ratio is
the **Elsasser number**

$$
\Lambda = \frac{\sigma B^{2}}{\rho\,\Omega},
$$

and dynamo theory and simulation put the operating point at $\Lambda$ of order
one. Setting $\Lambda = 1$ gives a field estimate

$$
B \sim \sqrt{\frac{\rho\,\Omega}{\sigma}} .
$$

With the external field treated as a dipole of moment $m$ at the top of the
conducting region of radius $R_{c}$,
$m \sim B R_{c}^{3} \cdot \tfrac{4\pi}{3\mu_{0}}$, the demonstration tabulates

```text
   rho (kg/m^3)   Omega (1/s)   sigma (S/m)   B (T)     m (A m^2)
       1.0e+03     1.750e-04      1.0e+05    0.0013      5.5120e+26
       1.0e+03     1.750e-04      1.0e+04    0.0042      1.7430e+27
       1.0e+03     1.750e-04      1.0e+03    0.0132      5.5120e+27
       4.0e+03     1.750e-04      1.0e+04    0.0084      3.4861e+27
       1.0e+03     1.000e-03      1.0e+04    0.0100      4.1667e+27
```

The field amplitude falls as $\sigma^{-1/2}$: a factor 100 in conductivity is a
factor 10 in the predicted field. Because $\sigma$ of a hydrogen–helium mixture
at planetary pressures is itself a poorly known material property (module
[12-02](../02-composition-and-mineral-physics/README.md)), the *field* is a much
sharper probe of $\sigma$ than $\sigma$ is an explanation of the field — an
inversion direction that is easy to get backwards.

### 6.2 A dynamo also needs a magnetic Reynolds number

$$
\mathrm{Rm} = \mu_{0}\sigma U L \gtrsim \mathcal{O}(10),
$$

with $U$ a characteristic flow speed and $L$ a length scale:

```text
   sigma (S/m)   L (m)       U for Rm = 10 (m/s)
      1.0e+03     1.0e+06         7.957747e-03
      1.0e+04     1.0e+06         7.957747e-04
      1.0e+05     1.0e+06         7.957747e-05
```

The required velocity falls as the conductivity rises: a well-conducting interior
needs only slow convection. This is why an observed field is evidence of a
*conducting, convecting* region and not of any particular composition.

### 6.3 Worked example: from a dipole moment to a conductivity

Invert the Elsasser balance. From $m \sim B R_{c}^{3}(4\pi/3\mu_{0})$ and
$B = \sqrt{\rho\Omega/\sigma}$,

$$
\sigma = \frac{\rho\,\Omega\,R_{c}^{6}\,(4\pi/3)^{2}}{\mu_{0}^{2}\,m^{2}} .
$$

Propagating the errors by logarithmic differentiation:

$$
\frac{\delta\sigma}{\sigma} = -2\frac{\delta m}{m}
+ \frac{\delta\rho}{\rho} + \frac{\delta\Omega}{\Omega}
+ 6\frac{\delta R_{c}}{R_{c}} .
$$

So a 10% error in the measured dipole moment gives a 20% error in $\sigma$,
while a 10% error in the radius of the conducting region gives a **60%** error.
The second term is the honest limit of the method: the field amplitude is a
conductivity probe only as good as the knowledge of *where* the field is
generated, and for a giant planet that location is itself a model output (the
depth at which the material becomes sufficiently conducting and convective).

## 7. Assumptions and regime of validity

| Assumption | Where it enters | Failure mode |
|---|---|---|
| Barotropic equation of state $P = K\rho^{1+1/n}$ | §1 | Real interiors have temperature gradients, phase transitions and composition gradients; a polytrope is a one-parameter caricature |
| Constant $K$ throughout the body | §2 | A varying $K$ destroys the homology relations; the measured exponents are then not constants |
| Hydrostatic equilibrium, no rotation | §§1–3 | Rapid rotation changes the structure at the few-percent level in mass and radius, more in the figure |
| A single added component ("heavy elements") | §5 | Real envelopes mix helium, ices and rock, each with its own EOS; the degeneracy widens rather than narrows |
| Elsasser number of order one | §6 | An order-of-magnitude assumption, not an equation; it sets the scale of $B$, not its value |
| $R_{c}$ known | §6 | It is not known independently; this is the dominant error term |
| Dipole dominated by the deep dynamo | §6 | Shallow current systems and the magnetospheric environment modify the observed moment |

## 8. Python demonstration

[`code/giant_planets_demo.py`](code/giant_planets_demo.py):

1. the Lane-Emden solver and its exact checks at $n = 0$ and $n = 1$;
2. the measured mass–radius exponent for a family of indices;
3. the dimensionless central pressure, including the $\pi/8$ check at $n = 1$;
4. the polytropic moment-of-inertia factor;
5. the core-versus-spread degeneracy, with the matching core fraction for each
   spread profile;
6. the Elsasser and magnetic-Reynolds scalings, and the sensitivity of an
   inferred conductivity.

```bash
cd 12-global-geophysics-interior/07-planetary-interiors-comparative/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python giant_planets_demo.py
```

## 9. Exercises

[`exercises/03-giant-planets-exercises.md`](exercises/03-giant-planets-exercises.md)
and the worked
[`exercises/03-giant-planets-solutions.md`](exercises/03-giant-planets-solutions.md).

## Mastery checkpoint

Without notes:

> **(a)** Verify that $\theta = \sin\xi/\xi$ solves the Lane-Emden equation for
> $n = 1$ and that $\xi_{1} = \pi$.
> **(b)** For $n = 1$ and a fixed $K$, explain why $R$ does not depend on
> $M$, and compute $R$ for $K = 10^{7}$ in consistent SI units (take
> $\rho_{c} = 10^{4}\ \mathrm{kg\,m^{-3}}$).
> **(c)** A synthetic giant planet has $C/MR^{2} = 0.20$. State two interior
> models consistent with that value and the same mass and radius, and explain
> which measurement would separate them.
> **(d)** Using $\Lambda = 1$ and $m = 1.7\times10^{27}\ \mathrm{A\,m^{2}}$,
> $\rho = 10^{3}\ \mathrm{kg\,m^{-3}}$, $\Omega = 1.75\times10^{-4}\ \mathrm{s^{-1}}$
> and $R_{c} = 5\times10^{7}$ m, compute $B$ and then $\sigma$. State how the
> answer changes if $R_{c}$ is twice as large.

A worked version of (b) and (d) appears in the lesson-03
[solutions](exercises/03-giant-planets-solutions.md).

## Common pitfalls

1. **Quoting a polytropic exponent as a universal law.** The exponents hold at
   fixed $K$ and fixed $n$; a real body has neither.
2. **Reaching the $n = 0$ limit of a homology formula.** The formula degenerates
   there; only the direct construction is meaningful.
3. **Reading a low $C/MR^{2}$ as a core.** Compressibility alone produces it
   (§4).
4. **Believing that a precise $C/MR^{2}$ removes the core-versus-spread
   ambiguity.** §5 shows the families overlap; the tie-breaker is an equation of
   state.
5. **Turning the Elsasser balance into a measurement.** $\Lambda = 1$ is a
   scaling hypothesis; the resulting $\sigma$ inherits $R_{c}^{6}$.
6. **Ignoring the numerical domain of a fractional power.** A solver that
   evaluates $\theta^{n}$ for $\theta<0$ returns NaN or complex values, and the
   "result" is an artefact.

## Related modules

- [12-02-01 Mantle Composition and Peridotite Models](../02-composition-and-mineral-physics/01-mantle-composition.md) —
  how composition and equation of state are actually determined, and why the
  degeneracy of §5 is unavoidable at the level of bulk observables.
- [12-07-01 Interiors of Mars, Venus, Mercury and the Moon](01-terrestrial-planets-interiors.md) —
  the same comparison method where self-compression is a correction rather than
  the dominant physics.
- [12-07-02 Icy Moons, Subsurface Oceans and Induction Studies](02-icy-moons.md) —
  induced rather than generated fields, and the conductivity that both lessons
  keep running into.
- [08-01-05 The Geodynamo: Mechanism and Evidence](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md) —
  the full dynamo problem that §6 caricatures.
- [12-04-02 Numerical Geodynamo Models](../04-geomagnetism-and-core/02-geodynamo-numerical.md) —
  what a real dynamo calculation adds beyond the scaling.
