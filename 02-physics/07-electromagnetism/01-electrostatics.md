---
id: 02-07-01
title: "Electrostatics, Coulomb's Law and Electric Potential"
level: intermediate
prereqs: ["01-06-04", "01-06-05", "01-06-08"]
estimated_minutes: 90
tags: [electrostatics, coulomb-law, electric-potential, laplace-equation, gravity-analogy]
---

# Electrostatics, Coulomb's Law and Electric Potential

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Coulomb's law in SI form, and explain why the constant
   $1/(4\pi\varepsilon_0)$ is a unit-system convention rather than a measured
   property of nature.
2. **Derive** Gauss's law from Coulomb's law and explain the role of the
   $\delta$-function source.
3. **Derive** Poisson's and Laplace's equations for the electrostatic potential,
   and state the boundary conditions that make them well posed.
4. **Construct** the potential of a charge distribution by superposition, and
   verify $E = -\nabla V$ numerically.
5. **Explain** the exact mathematical analogy with Newtonian gravity —
   $1/r^2$ force, $1/r$ potential, harmonic potential outside the source — and
   **state precisely where the analogy breaks**: two signs of charge versus one
   sign of mass, screening versus the absence of gravitational shielding, the
   coupling-constant ratio of about $10^{20}$, and the absence of a
   gravitational dipole term.
6. **Apply** the image-charge method to a charge above a grounded plane and
   prove the potential vanishes on the plane.
7. **Verify** every claim numerically, including the harmonic property of the
   point-charge potential and its $O(h^2)$ finite-difference convergence.

## Prerequisites

- [01-06-04 Divergence and Curl](../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md)
  — the definition of divergence and the meaning of $\nabla\cdot\mathbf F$.
- [01-06-08 Introduction to Potential Theory](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  — scalar potentials, conservative fields, and why $\nabla\times(\nabla V) = \mathbf 0$.
- [01-06-05 Line and Surface Integrals; Flux and Circulation](../../01-mathematics/06-multivariable-calculus/05-line-surface-integrals.md)
  — flux, and Gauss's law as a statement about flux through a closed surface.

## 1. Why electrostatics is in a geophysics curriculum at all

Electrostatics describes *charges at rest*. In the Earth, charge almost never
stays where you put it: any macroscopic free charge in a rock conductor is
neutralised in an extraordinarily short time, which is why you cannot detect a
buried charge with a surface voltmeter. The honest first statement about this
subject is therefore negative: **electrostatic methods do not see deep into the
Earth.**

The reason electrostatics nevertheless underpins all of electromagnetic
geophysics is that the *same mathematical structure* reappears three times:

1. **Directly.** Self-potential (SP) surveys measure natural electric fields at
   the surface produced by electrokinetic and thermoelectric charge separation.
   The measurement is a potential difference; the interpretation is potential
   theory.
2. **As the steady limit of current flow.** The DC resistivity and
   induced-polarisation methods drive currents through the ground and measure
   potentials. In a region with no sources of current, the electric potential of
   a steady current field obeys **Laplace's equation**, $\nabla^2V = 0$, exactly
   as the electrostatic potential does. This is why the "electrostatic" solution
   of a buried sphere, a vertical contact or a half-space is the standard model of
   a DC resistivity sounding — the physics differs (current flow, not static
   charge) but the mathematics is identical.
3. **As the static limit of Maxwell's equations.** Electric fields in
   conductors and magnetic fields in rocks inherit their boundary conditions and
   their harmonic behaviour from the electrostatics studied here, and
   [02-08 Potential Theory](../08-potential-theory/README.md) develops that
   machinery once and uses it for gravity, magnetics and electricity alike.

So learn this lesson for its mathematics and for the physical reasoning about
fields and potentials. Do not learn it expecting to "detect charges" in the
subsurface.

## 2. Coulomb's law in SI units

Two point charges $q_1$ and $q_2$ separated by a distance $r$ in vacuum exert on
each other a force along the line joining them:

$$F = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2},
\qquad
\frac{1}{4\pi\varepsilon_0} = 8.987\,551\,787\ldots\times10^{9}\ \mathrm{N\,m^2\,C^{-2}} . \tag{1}$$

The force is repulsive for like charges and attractive for opposite charges;
in vector form, the force on $q_1$ due to $q_2$ is

$$\mathbf F_{12} = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r^2}\,\hat{\mathbf r}_{12},
\qquad
\hat{\mathbf r}_{12} = \frac{\mathbf r_1 - \mathbf r_2}{|\mathbf r_1 - \mathbf r_2|} . \tag{2}$$

**On the constant.** In SI, $\varepsilon_0$ is not a free parameter of the theory;
it is fixed by the definition of the ampere and (since 2019) by the measured
value of the vacuum permeability,
$\varepsilon_0 = 1/(\mu_0 c^2)$. With $\mu_0 = 1.256\,637\,062\,12\times10^{-6}$
N/A² (CODATA, a **measured** constant since the 2019 SI redefinition — it was
exact before 2019) and $c = 299\,792\,458$ m/s (exact), we get
$\varepsilon_0 = 8.854\,187\,812\,8\times 10^{-12}$ F/m. Section 9 verifies that
identity numerically.

The electric field of a point charge follows from (2) by defining
$\mathbf E \equiv \mathbf F/q$ for a small test charge:

$$\mathbf E(\mathbf r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\hat{\mathbf r} . \tag{3}$$

Because (3) is linear in $q$, fields of many charges superpose:

$$\mathbf E(\mathbf r) = \frac{1}{4\pi\varepsilon_0}\sum_k\frac{q_k(\mathbf r - \mathbf r_k)}{|\mathbf r - \mathbf r_k|^3}
= \frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\mathbf r')(\mathbf r-\mathbf r')}{|\mathbf r-\mathbf r'|^3}\,\mathrm d^3r' . \tag{4}$$

## 3. Gauss's law and the divergence of $\mathbf E$

Take the divergence of (4). The integrand is $\rho(\mathbf r')(\mathbf r-\mathbf r')/|\mathbf r-\mathbf r'|^3$,
and for $\mathbf r \neq \mathbf r'$,
$\nabla\cdot\left[(\mathbf r-\mathbf r')/|\mathbf r-\mathbf r'|^3\right] = 0$ —
a direct computation, and the same identity that makes the point-charge potential
harmonic. But the integral over a small sphere around $\mathbf r'$ is not zero:
its value is $4\pi$. Therefore

$$\nabla\cdot\mathbf E = \frac{\rho}{\varepsilon_0} \qquad\text{(differential form of Gauss's law).} \tag{5}$$

Integrating (5) over a volume and using the divergence theorem gives the integral
form: the flux of $\mathbf E$ out of any closed surface equals the enclosed charge
divided by $\varepsilon_0$,

$$\oint_{\partial\Omega}\mathbf E\cdot\mathrm d\mathbf A = \frac{Q_{\text{enc}}}{\varepsilon_0} . \tag{6}$$

**Why this is the right way to remember the $1/r^2$ law.** Equations (5)–(6) say
that field lines begin and end on charge with a fixed density. Because the solid
angle subtended by a patch of area grows as $r^{-2}$, a flux density falling as
$r^{-2}$ is precisely what is needed for the flux through a closed surface to
record the enclosed charge and nothing else. Any $1/r^2$ force has this property;
any other power does not. Gauss's law is not a separate law but the statement
that the force law is exactly inverse-square in three dimensions.

## 4. The electric potential

Since $\nabla\times\mathbf E = \mathbf 0$ for static fields (the curl of (3) and
of every term in (4) vanishes), $\mathbf E$ is conservative and can be written as
the gradient of a scalar:

$$\mathbf E = -\nabla V, \qquad
V(\mathbf r) = \frac{1}{4\pi\varepsilon_0}\sum_k \frac{q_k}{|\mathbf r-\mathbf r_k|}
= \frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\mathbf r')}{|\mathbf r-\mathbf r'|}\,\mathrm d^3r' . \tag{7}$$

$V$ is the **electric potential**, in volts (V = J/C). The work done moving a
unit charge from $A$ to $B$ is $\int_A^B\mathbf E\cdot\mathrm d\boldsymbol\ell = V(A)-V(B)$;
only potential *differences* are measurable.

Substituting (7) into (5) gives **Poisson's equation**, and in a region free of
charge, **Laplace's equation**:

$$\nabla^2 V = -\frac{\rho}{\varepsilon_0},
\qquad
\nabla^2 V = 0 \quad (\rho = 0) . \tag{8}$$

The identification of the point charge as a $\delta$-function source is the whole
content of the step from (7) to (8): $V = 1/(4\pi\varepsilon_0 r)$ satisfies
$\nabla^2 V = 0$ everywhere except at $r = 0$, where the Laplacian is
$-q\delta^3(\mathbf r)/\varepsilon_0$.

## 5. Conductors, boundary conditions and the image-charge method

Two boundary conditions do most of the work in electrostatics:

- $V$ is continuous everywhere (a discontinuity would imply infinite $\mathbf E$).
- The tangential component of $\mathbf E$ is continuous across any interface, and,
  at a conductor surface in equilibrium, $\mathbf E$ inside is zero, so
  $\mathbf E$ just outside is **normal** to the surface and the conductor surface
  is an **equipotential**.

Combined with $\nabla^2V = 0$ in the intervening space, this makes the problem
well posed: a harmonic function is determined by its values on the boundary (the
uniqueness theorem of
[02-08-06](../08-potential-theory/06-uniqueness-theorems.md)).

**Image charges.** The standard trick: a point charge $q$ at height $d$ above an
infinite grounded conducting plane ($V = 0$ on the plane) is equivalent, in the
region above the plane, to the pair $+q$ at $+d$ and $-q$ at $-d$. The pair's
potential is zero on the plane by symmetry, so it satisfies the boundary
condition, and by uniqueness it *is* the solution. The force on the real charge is
attractive and equals

$$F = -\frac{q^2}{16\pi\varepsilon_0 d^2} . \tag{9}$$

Section 9 verifies both the vanishing potential and equation (9) numerically.

> **This is the first place the gravitational analogy fails.** There is no
> gravitational image mass and no gravitational shield: the equivalence principle
> forbids it. An "anti-mass" would violate the observation that all masses fall
> the same way, and no material screens gravity the way a conductor screens
> electric fields. This single asymmetry is why gravity penetrates the whole
> Earth while electrostatics penetrates nothing.

## 6. Physical interpretation: the analogy with gravity, and where it breaks

Newton's law of gravitation has the same shape as Coulomb's law:

$$\mathbf F_g = -G\frac{m_1m_2}{r^2}\hat{\mathbf r},
\qquad
\mathbf g = -\nabla\Phi, \qquad
\nabla^2\Phi = 4\pi G\rho_m , \tag{10}$$

with $\Phi = -GM/r$ the gravitational potential and $\rho_m$ the mass density.
Compare equation (1) with (10), and (8) with the last of (10):

| Feature | Electrostatics | Gravity |
|---|---|---|
| Force law | $q_1q_2/(4\pi\varepsilon_0 r^2)$ | $-Gm_1m_2/r^2$ |
| Potential of a point source | $q/(4\pi\varepsilon_0 r)$ | $-GM/r$ |
| Source equation | $\nabla^2V = -\rho/\varepsilon_0$ | $\nabla^2\Phi = 4\pi G\rho_m$ |
| Sign of the coupling | two signs of charge | one sign of mass |
| Outward field of a point source | $\propto q/r^2$, signed | $\propto M/r^2$, always attractive |
| Field outside a spherically symmetric body | point-charge result | point-mass result |
| Screening | a conductor sets $V=0$ on its surface | none |
| Relative strength | $1/(4\pi\varepsilon_0) = 8.9876\times10^{9}$ | $G = 6.674\times10^{-11}$ |

The bottom line of the table is the number that matters: the ratio

$$\frac{1/(4\pi\varepsilon_0)}{G} = 1.347\times10^{20} \tag{11}$$

so two 1 kg masses each carrying one coulomb repel each other electrically
$1.3\times10^{20}$ times more strongly than they attract each other
gravitationally. Cosmically, gravity wins only because bulk matter is almost
exactly neutral: the positive and negative charges cancel to a part in
$10^{20}$ or better, while mass never cancels.

**Four places where the analogy breaks, and why each matters:**

1. **Two signs.** Charge can be screened. A rock with pore water full of ions is
   a conductor, and electrostatic fields are excluded from it; a Faraday cage
   works. Gravitational fields cannot be excluded by any arrangement of matter.
2. **Coupling strength and the units that hide it.** $1/(4\pi\varepsilon_0)$ and
   $G$ have different dimensions, so equation (11) is a ratio of numbers in a
   chosen unit system, not a dimensionless constant of nature. What is
   dimensionless is the ratio of electric to gravitational forces between two
   elementary charges of mass $m$: it grows as $1/m^2$, so it is enormous for
   electrons and merely large for macroscopic charged bodies. Both statements are
   correct; they are statements about different comparisons.
3. **No shielding, therefore no "inverse problem of the shield".** Because
   gravity cannot be screened, a gravity anomaly is a weighted integral of the
   density over the whole body — diffuse, non-unique and smooth. Electric fields
   *can* be screened, which is exactly why they carry information about
   conductivity structure at the scale of the screening length.
4. **No dipole of the same kind.** Gravity in the solar system is monopole-
   dominated (there is no negative mass to make a dipole moment), so the
   gravitational field of the Earth is $\approx GM/r^2$ to a few parts in $10^{5}$
   and its anomalies are *relative perturbations* of that monopole. The magnetic
   field has **no monopole at all** — $\nabla\cdot\mathbf B = 0$ — so it is
   entirely dipole, quadrupole and higher. A magnetic anomaly is therefore
   comparable in size to the field it perturbs, in a way a gravity anomaly is
   not. This one structural difference explains a great deal of why magnetic
   surveying is analytically harder but empirically more sensitive to shallow
   sources than gravity surveying.

**Where the analogy is exact.** For the *mathematical* inverse problem the two are
the same: Laplace's equation, the mean-value property, the multipole expansion,
Poisson's integral and the uniqueness theorem all apply unchanged. Learning them
for one potential buys the other for free. That is why this module and
[02-08 Potential Theory](../08-potential-theory/README.md) share their machinery.

## 7. Assumptions and regime of validity

| Assumption | Where it entered | What breaks outside it |
|---|---|---|
| Charges at rest ($\partial/\partial t = 0$) | Throughout | Anything time-varying: Faraday's law and the full Maxwell set are needed (lesson [02-07-03](./03-maxwell-equations.md)) |
| No magnetic fields, no magnetic forces | The definition of $\mathbf E$ as the whole story | Moving charges: $\mathbf F = q\mathbf v\times\mathbf B$ (lesson [02-07-02](./02-magnetostatics.md)) |
| Linear, isotropic, non-dispersive dielectric ($\varepsilon$ a scalar constant) | The constitutive relation | Anisotropy, dielectric relaxation and induced polarisation; $\varepsilon$ becomes complex and frequency-dependent |
| Point charges, or infinitesimal source elements | Coulomb's law and its superposition | Sources comparable to the observation distance: the finite source size must be integrated over (Section 9's line and shell examples) |
| Superposition | Adding contributions | Nonlinear media; not relevant in the Earth at these field strengths |
| An infinite grounded conducting plane for the image method | Section 5 | A finite plate: edge effects, and a resistive plane which does not impose $V = 0$ |
| Electrostatic fields persist in rock | Section 1 | They do not: the dielectric relaxation time is $\varepsilon/\sigma\approx5$ ns for a typical rock. **This is the assumption whose failure defines the whole subject**: what survives in the Earth is the *steady current* field, which obeys Laplace's equation for the potential but is driven by continuous sources rather than by stored charge |
| The gravitational analogy | Section 6 | Breaks in four named respects (two signs, coupling strength, screening, and the presence or absence of a monopole); it is a *mathematical* analogy, not a physical one |

The last two rows are the ones to carry away. Everything in this lesson's
electrostatics is correct and none of it explains a deep geophysical measurement on
its own: its role is to supply the mathematics (potentials, boundary conditions,
harmonic functions, multipoles) that the *current* methods and the potential-field
methods then use.

## 8. Units and dimensional analysis

- Coulomb's law (1): $[\mathrm N] = [\mathrm{C^2}/(\varepsilon_0\,\mathrm{m^2})]$,
  so $[\varepsilon_0] = \mathrm{C^2\,N^{-1}\,m^{-2}} = \mathrm{F/m}$ ✓.
- Electric field: $[\mathbf E] = \mathrm{N/C} = \mathrm{V/m}$. Both forms are used;
  $\mathrm{V/m}$ is the geophysical one because surveys measure volts and metres.
- Potential: $[V] = \mathrm J/C = \mathrm V$ ✓.
- Poisson (8): $[\nabla^2V] = \mathrm{V/m^2}$ and
  $[\rho/\varepsilon_0] = \mathrm{C\,m^{-3}/(C^2N^{-1}m^{-2})} = \mathrm{N\,C^{-1}m^{-1}} = \mathrm{V/m^2}$ ✓.
- The ratio in (11): $[1/(4\pi\varepsilon_0 G)] = \mathrm{N\,m^2C^{-2}}/(\mathrm{N\,m^2kg^{-2}}) = \mathrm{kg^2C^{-2}}$,
  which is why it is not a pure number.
- A useful anchor: the field at 1 m from a 1 µC charge is
  $8.9876\times10^9\times10^{-6} = 8988$ V/m. For scale, the fair-weather
  atmospheric field at the Earth's surface is *commonly quoted* as of order
  100 V/m — a nominal figure that varies strongly with weather, altitude and dust
  loading, and which must be measured rather than assumed for quantitative work —
  so a microcoulomb of
  *unbalanced* charge at 1 m is already a hundred times the natural field. Such a
  charge cannot exist in the ground for long, which is the quantitative form of
  the statement opening Section 1.

## 9. Python demonstration

[`code/electrostatics_demo.py`](./code/electrostatics_demo.py) verifies every
claim above. Observed output:

```text
mu0            = 1.25663706212000e-06 N/A^2   (CODATA 2022, measured)
c              = 299792458 m/s     (exact by definition)
1/(mu0 c^2)    = 8.85418781280039e-12 F/m
quoted eps0    = 8.85418781280000e-12 F/m
relative difference = 4.343e-14
```

```text
charges: +2 nC at (-0.05,0,0), -1 nC at (+0.05,0,0)
test point (0, 0.04, 0) m
V      =  140.361977 V
E      = ( 5135.194294,  1369.385145,  0.000000) V/m
-gradV = ( 5135.194293,  1369.385145, -0.000000) V/m
|E - (-gradV)| / |E| = 1.738e-11
```

```text
r =  0.1 m:  d2V/dr2 + (2/r)dV/dr = -3.638e-12 V/m^2
r =  0.5 m:  d2V/dr2 + (2/r)dV/dr =  0.000e+00 V/m^2
r =  2.0 m:  d2V/dr2 + (2/r)dV/dr =  0.000e+00 V/m^2
(b) finite-difference Laplacian error converges as O(h^2):
    h = 1.0e-03 m:  Laplacian =  5.752123e-04 V/m^2   predicted (h^2/12)V'''' = 5.752033e-04
    h = 5.0e-04 m:  Laplacian =  1.438029e-04 V/m^2   predicted (h^2/12)V'''' = 1.438008e-04   ratio to previous = 4.00
    h = 2.5e-04 m:  Laplacian =  3.595390e-05 V/m^2   predicted (h^2/12)V'''' = 3.595021e-05   ratio to previous = 4.00
```

```text
r (m)     |E| numeric   mu0-free dipole |E|     ratio
0.0400    2.564472e+03          2.808610e+03    0.9131
0.1000    1.770881e+02          1.797510e+02    0.9852
0.4000    2.805979e+00          2.808610e+00    0.9991
2.0000    2.246804e-02          2.246888e-02    1.0000
```

```text
V on the plane z = 0 for several (x,y):
    (x,y) = (0.00, 0.00) m : V =  0.000e+00 V
    (x,y) = (0.03, 0.04) m : V =  0.000e+00 V
analytic image force on the charge: q E_image = -5.055498e-05 N
closed form -q^2/(16 pi eps0 d^2)  = -5.055498e-05 N
```

```text
L (m)     E_s numeric   infinite-line limit     ratio
   0.1    1.271032e+02          1.797510e+02    0.7071
   1.0    1.788590e+02          1.797510e+02    0.9950
  10.0    1.797420e+02          1.797510e+02    1.0000
(b) uniformly charged spherical shell (radius a = 1 m, total Q = 1 nC):
    r = 0.5 m: E_r numeric = -1.642658e-08 V/m ; exact = 0.000000e+00
    r = 1.0 m: E_r numeric =  4.493776e+00 V/m ; exact = 4.493776e+00
    r = 2.0 m: E_r numeric =  2.246888e+00 V/m ; exact = 2.246888e+00
    r = 5.0 m: E_r numeric =  3.595021e-01 V/m ; exact = 3.595021e-01
```

```text
coupling ratio (1/(4 pi eps0)) / G = 1.346591e+20
field needed to support 1 kg carrying 1 C against gravity: E = q g / m = 9.80665 V/m
```

### What to observe

| Observation | Consequence |
|---|---|
| $1/(\mu_0c^2)$ reproduces the handbook $\varepsilon_0$ to $4\times10^{-14}$ relative | $\varepsilon_0$ is derived, not independently measured; the residual is the rounding of the tabulated value |
| $E = -\nabla V$ holds to $1.7\times10^{-11}$ relative | The potential is the complete description of the static field; the numerical residual is the central-difference truncation |
| The analytic Laplacian of $V=q/(4\pi\varepsilon_0r)$ is $3.6\times10^{-12}$ V/m² at $r = 0.1$ m and 0 at larger $r$ | The point-charge potential is harmonic away from the source (round-off only) |
| The finite-difference Laplacian is *non-zero* but matches $(h^2/12)V''''$ and falls by exactly 4.00 per halving of $h$ | The non-zero value is scheme truncation, not physics; this is how you tell the two apart |
| The two-charge field converges to the $1/r^3$ dipole field as $r/d$ grows, reaching ratio 1.0000 at $r = 2$ m | Multipole expansion is quantitative, not just qualitative: $V\sim1/r^2$, $\mathbf E\sim1/r^3$ |
| The image-charge potential is exactly 0 on the plane and the force matches the closed form to all printed digits | The image method solves the boundary-value problem exactly |
| The finite-line field is 0.7071 of the infinite-line value when $L = s$, and 1.0000 when $L = 100s$ | Two-dimensional idealisations are only valid within an aspect ratio $L/s \gg 1$, routinely violated in a borehole |
| The shell field is $Q/(4\pi\varepsilon_0r^2)$ outside, exactly $Q/(8\pi\varepsilon_0a^2)$ *at* the surface and 0 inside (to $1.6\times10^{-8}$ V/m) | The shell theorem, and the factor 2 at the surface, verified from a surface integral rather than assumed |
| The coupling ratio is $1.347\times10^{20}$ and a 1 C/kg body needs only 9.81 V/m to levitate | The two forces are not merely different in size; their *usable* regimes are disjoint by twenty orders of magnitude |

> **Breaking exercise.** Before running the script, predict the sign and magnitude
> of the residual in line 2(b) if $h$ is increased to $10^{-2}$ m. Then modify the
> script to compute the Laplacian with a five-point stencil
> $( -V_{r-2h}+16V_{r-h}-30V_r+16V_{r+h}-V_{r+2h})/(12h^2)$ and measure the new
> convergence order. Explain why the higher-order stencil reaches round-off sooner.

## 10. Common mistakes

1. **Confusing $\varepsilon_0$ with a measured constant of nature that "belongs"
   to Coulomb's law.** In SI it is fixed by the definition of the ampere together
   with the measured $\mu_0$; in Gaussian units the constant is absent and charge
   is measured in statcoulombs. The physics is the same; the bookkeeping is not.
2. **Writing $1/(4\pi\varepsilon_0) = 9\times10^9$ and then using it in a
   dimensional formula with mixed units.** The value holds only for SI.
3. **Using the infinite-line or infinite-plane result at finite scale.** The demo
   shows the finite line at $L = s$ gives only $1/\sqrt2$ of the infinite-line
   field. Borehole electrodes are exactly in this regime.
4. **Assuming a grounded conductor boundary condition without a conductor.**
   Image charges require a real conducting surface; a "ground" that is dry
   resistive rock does not set $V = 0$.
5. **Treating the potential of a charge distribution as additive in the *field
   magnitude*.** Potentials add as scalars, fields as vectors. Adding
   $|\mathbf E|$ of two sources without geometry produces the classic
   factor-of-$\sqrt2$ error.
6. **Forgetting that $\mathbf E = -\nabla V$ holds only in the electrostatic
   (curl-free) case.** With time-varying fields, Faraday's law adds
   $-\partial\mathbf A/\partial t$
   ([02-07-04](./04-em-induction.md)).
7. **Believing that the gravity analogy extends to dynamics.** It does not:
   gravitational radiation, frame dragging and the equivalence principle have no
   electrostatic counterparts, and the analogy is a statement about *potentials of
   static fields* only.
8. **Reporting a potential without stating the reference.** $V$ is defined up to a
   constant; for an infinite line or plane the natural reference is at infinity
   only if the source is bounded.

## 11. Real-world applications

- **Self-potential (SP) surveys.** Natural potentials of order tens to hundreds
  of millivolts (nominal; strongly site-dependent) arise from electrokinetic flow,
  redox gradients and thermoelectric effects. The interpretation is a potential
  field problem with a source distribution, i.e. a Poisson equation.
- **DC resistivity and induced polarisation.** Both measure a *steady current*
  field. In homogeneous ground the potential
  $V = \rho I/(2\pi r)$ of a point current source is the direct analogue of the
  point-charge potential of equation (7), with $1/\varepsilon_0$ replaced by the
  resistivity — which is why the two subjects share their mathematics.
- **Instrumentation and shielding.** Any measurement of microvolt-level
  potentials must live inside a Faraday cage; the image-charge argument of
  Section 5 is the reason a grounded enclosure removes external static fields
  but not external magnetic fields, which is why magnetometers are shielded with
  mu-metal rather than copper
  ([08-02 Magnetic Instruments and Surveys](../../08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/README.md)).
- **Lightning and atmospheric electricity.** Charge separation in thunderclouds,
  the resulting fields and the return stroke are a large-scale electrostatic
  problem; the induced currents in buried pipelines and cables are the
  geophysical nuisance version of it.
- **Laboratory rock physics.** Complex conductivity measurements of rocks are
  calibrated against electrostatic models of the pore network; the
  Gouy–Chapman and Stern models of the electrical double layer are
  electrostatic problems with a screening length.
- **Cross-checks on other potential fields.** The multipole expansion verified in
  Section 9 is the same expansion used for the geomagnetic field and the
  geopotential ([02-08-03 Spherical Harmonics](../08-potential-theory/03-spherical-harmonics.md)).

## 12. Further reading

- **Griffiths, D. J. *Introduction to Electrodynamics* (4th ed., Cambridge
  University Press, 2017).** Chapters 1–3 develop Coulomb's law, Gauss's law, the
  potential and the image-charge method at exactly the level used here, with the
  multipole expansion in Chapter 3. Level: intermediate.
- **Jackson, J. D. *Classical Electrodynamics* (3rd ed., Wiley, 1999).** The
  rigorous graduate treatment: boundary-value problems, Green functions and the
  multipole expansion in its general form. Level: graduate.
- **Purcell, E. M., & Morin, D. J. *Electricity and Magnetism* (3rd ed.,
  Cambridge University Press, 2013).** The clearest physical account of *why*
  Gauss's law follows from the inverse-square law, and of the field-energy
  viewpoint. Level: intermediate.
- **Kellogg, O. D. *Foundations of Potential Theory* (Springer, 1929; Dover
  reprint).** The classical mathematical treatment of harmonic functions,
  uniqueness and boundary conditions. Level: graduate.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics* (2nd
  ed., Cambridge University Press, 1990).** The SP and DC resistivity chapters
  show how the potential theory of this lesson is used in the field, with the
  conventions survey geophysicists actually use. Level: intermediate.
- **NIST, *CODATA Internationally Recommended Values of the Fundamental Physical
  Constants*.** The authoritative source for $G$, $\mu_0$ and $\varepsilon_0$ with
  full uncertainties, distributed at <https://physics.nist.gov/cuu/Constants/>.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [02 Magnetostatics, Biot–Savart and Ampère's Law](./02-magnetostatics.md) — the
  magnetostatic counterpart, where the monopole term is absent entirely.
- [04 Faraday's Law, Induction and Eddy Currents](./04-em-induction.md) — what
  appears in $\mathbf E$ once the fields are allowed to change.
- [02-08-02 Laplace's Equation and Harmonic Functions](../08-potential-theory/02-laplace-equation.md)
  — the mathematics shared by electrostatics, gravity and steady current flow.
- [01-06-08 Introduction to Potential Theory](../../01-mathematics/06-multivariable-calculus/08-potential-theory.md)
  — the prerequisite statement of conservative fields and potentials.
- [02-03 Direction and Magnitude: Oscillations and Waves](../03-oscillations-and-waves/README.md)
  — the wave toolkit that the later lessons in this module use.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the provenance of $\mu_0$, $\varepsilon_0$, $G$ and the rule on quoting them.

Exercises:
[`exercises/01-electrostatics-exercises.md`](./exercises/01-electrostatics-exercises.md)
and
[`exercises/01-electrostatics-solutions.md`](./exercises/01-electrostatics-solutions.md).

## Self-assessment checklist

Work through this without notes. Every item should be a clear "yes".

- [ ] I can write Coulomb's law and the electric field of a point charge in SI
      units, and say what $1/(4\pi\varepsilon_0)$ does and does not mean.
      (Section 2)
- [ ] I can derive $\nabla\cdot\mathbf E = \rho/\varepsilon_0$ from the
      $1/r^2$ field, and explain why any other power would fail. (Section 3)
- [ ] I can define the potential, prove $\mathbf E = -\nabla V$ for static fields,
      and derive Poisson's and Laplace's equations. (Section 4)
- [ ] I can state the two boundary conditions that make an electrostatic problem
      well posed, and explain why a conductor surface is an equipotential.
      (Section 5)
- [ ] I can solve the grounded-plane problem by images, including the force.
      (Section 5)
- [ ] I can list the four respects in which the gravity analogy breaks, and name
      the observation that establishes each. (Section 6)
- [ ] I can explain why the absence of a magnetic monopole and the absence of
      negative mass have opposite consequences for anomaly interpretation.
      (Section 6)
- [ ] I can verify $E = -\nabla V$, Laplace's equation, the dipole limit, the
      image charge and the shell theorem numerically, and distinguish scheme
      truncation from physics. (Section 9)
- [ ] I can state what a self-potential survey measures and why DC resistivity
      shares the mathematics of electrostatics without sharing its physics.
      (Section 11)
