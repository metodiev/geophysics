---
id: 02-01-03
title: "Scaling Laws, Similarity and Dimensional Reasoning"
level: intermediate
prereqs: ["02-01-01", "02-01-02"]
estimated_minutes: 90
tags: [scaling-laws, buckingham-pi, similarity, dimensional-analysis, regime-of-validity]
---

# Scaling Laws, Similarity and Dimensional Reasoning

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Buckingham's π theorem, and use a null-space computation on the
   exponent matrix to produce the independent dimensionless groups of a problem
   exactly, including checking a named group against the algebra.
2. **Distinguish** geometric, kinematic and dynamic similarity, and say precisely
   which equality of π groups each requires.
3. **Derive** the scaling of a diffusive process, explain why it is quadratic,
   and convert it into a lithospheric cooling estimate.
4. **Quantify** the error of a small-angle approximation at a stated angle
   (computed, not estimated), and state the angle at which it stops being usable.
5. **Decide** whether a laboratory or numerical experiment is dynamically
   similar to a mantle-scale process, and justify the answer with numbers.

## Prerequisites

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](./01-physical-quantities.md) —
  exponent vectors and the homogeneity principle, which this lesson generalises.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](./02-measurement-uncertainty.md) —
  an error bar is what makes "the regime of validity" quantitative.

## 1. Intuition: the same physics at three scales, and where it stops

Consider three things that look nothing alike:

| System | Length | Speed | Viscosity |
|---|---|---|---|
| laboratory convection tank | 0.3 m | 0.01 m/s | $10^{-6}$ m²/s (water) |
| ocean gyre | $10^{6}$ m | 0.1 m/s | $10^{-6}$ m²/s |
| mantle convection | $10^{6}$ m | $3\times10^{-10}$ m/s | $10^{15}$ m²/s (effective) |

Dimensional reasoning asks a sharp question: **do these three systems have the
same dimensionless numbers?** If they do, one is a scale model of the other and
laboratory measurements transfer to the Earth. If they do not, the laboratory
tank is a physics experiment about a different regime, and its results cannot be
scaled up by multiplying by a length ratio.

This is the practical content of scaling. It is why geophysics uses a centrifuge
to model a salt dome (where gravity is the only way to match the π groups),
why analogue models of subduction are quoted with an explicit list of similarity
conditions, and why numerical models — which have no scale at all — have become
the dominant tool for the mantle.

## 2. Precise definitions

### 2.1 Buckingham's π theorem

Let a physical problem be characterised by $n$ dimensional parameters involving
$r$ independent dimensions. Then

- the parameters can be combined into exactly $n - r$ independent
  **dimensionless groups** $\Pi_1,\dots,\Pi_{n-r}$, and
- the relationship between them can be written
  $f(\Pi_1,\dots,\Pi_{n-r}) = 0$, equivalently
  $\Pi_1 = \phi(\Pi_2,\dots,\Pi_{n-r})$.

The theorem is proved by writing each parameter as a monomial in the base
dimensions. With $D$ the $r\times n$ exponent matrix, a dimensionless group is a
vector $c \in \mathbb{Q}^{n}$ with $Dc = 0$: an element of the **null space** of
$D$. Its dimension is $n - \mathrm{rank}(D) = n - r$ by the rank–nullity
theorem. Buckingham's π theorem is, in modern language, a statement about null
spaces — and this is why the computation below can be done exactly with rational
arithmetic rather than by guessing.

### 2.2 Three kinds of similarity

| Kind | Condition | What it preserves |
|---|---|---|
| geometric | all length ratios equal | shapes; nothing dynamic |
| kinematic | length ratios **and** time ratios equal (so velocity ratios equal) | the sequence of events |
| dynamic | all relevant π groups equal | forces and energy budgets |

Only dynamic similarity allows scaling of results. A model that is
geometrically similar but not dynamically similar reproduces the *appearance* of
a process, not its behaviour.

### 2.3 Scaling law, similarity variable, self-similarity

A **scaling law** is a power-law relation between dimensional quantities,
$y \propto x^{p}$, with the exponent fixed by dimensions or by the governing
equation. A **similarity variable** is a dimensionless combination of
independent variables in terms of which a partial differential equation becomes
an ordinary one, e.g. $\eta = z/\sqrt{\kappa t}$ for diffusion. A solution
expressible with a single similarity variable is **self-similar**: it looks the
same at every time, rescaled.

### 2.4 Dimensionless groups used throughout this folder

| Group | Definition | Meaning | Where it decides the physics |
|---|---|---|---|
| Reynolds $\mathrm{Re}$ | $\rho u L/\eta$ | inertia / viscosity | laminar vs turbulent flow ([02-06-03](../06-fluid-mechanics/03-viscous-flow.md)) |
| Rayleigh $\mathrm{Ra}$ | $\rho g\alpha\Delta T L^{3}/(\kappa\eta)$ | buoyancy / (diffusion × viscosity) | onset of convection ([02-06-06](../06-fluid-mechanics/06-mantle-convection.md)) |
| Fourier $\mathrm{Fo}$ | $\kappa t/L^{2}$ | elapsed time / diffusion time | how far heat has moved |
| Péclet $\mathrm{Pe}$ | $uL/\kappa$ | advection / diffusion | whether conduction matters in a flow |
| Deborah | $\tau_{\text{relax}}/\tau_{\text{obs}}$ | memory / observation time | elastic vs viscous behaviour of rock |
| Quality factor $Q$ | energy stored / lost per radian | dissipation | seismic attenuation ([02-03-10](../03-oscillations-and-waves/10-attenuation.md)) |
| Eötvös / gravity gradient | $\partial g/\partial z \cdot L / g$ | is a gravity model isostatic or dynamic? | [`02-01-01`](./01-physical-quantities.md) |

The **Deborah number** is the geophysically decisive one: the same rock is a
linear elastic solid at seismic frequencies ($\mathrm{De}\ll 1$ for a short
observation time relative to relaxation) and a viscous fluid for postglacial
rebound ($\mathrm{De}\gg 1$). The material has not changed; the ratio has.

## 3. Derivations

### 3.1 The pendulum by π theorem, and the small-angle error computed

Take the period $T$ of a simple pendulum as depending on length $l$, gravity $g$,
bob mass $m$ and amplitude $\theta_0$. The exponent matrix for
$(l,g,T,m)$ with dimensions $[(M, L, T)]$ is

$$D = \begin{pmatrix}
0 & 0 & 0 & 1\\
1 & 1 & 0 & 0\\
0 & -2 & 1 & 0
\end{pmatrix}.$$

Its rank is 3 (mass appears only in $m$, so $m$ cannot enter a dimensionless
group; $l,g,T$ span $L$ and $T$), so there is $4-3 = 1$ π group. Solving
$Dc = 0$ gives $c \propto (-1/2,\ 1/2,\ 1,\ 0)$, i.e.

$$\Pi = T\sqrt{\frac{g}{l}}, \qquad\text{so}\qquad
T = \sqrt{\frac{l}{g}}\,\phi(\theta_0).$$

Mass cannot appear, and the exponent $1/2$ is forced. The remaining function
$\phi$ requires the dynamics; the exact result is

$$T = 4\sqrt{\frac{l}{g}}\,K\!\left(\sin^{2}\frac{\theta_0}{2}\right)
= 2\pi\sqrt{\frac{l}{g}}\left(1 + \frac{\theta_0^{2}}{16}
+ \frac{11\theta_0^{4}}{3072} + \cdots\right),$$

with $K$ the complete elliptic integral of the first kind.

**The error of the small-angle approximation, computed** (not estimated), for
$l = 1$ m, $g = 9.81$ m s⁻², $T_0 = 2.006067$ s:

| $\theta_0$ | exact $T$ (s) | $T_0$ (s) | error | series $1+\theta^2/16+11\theta^{4}/3072$ | series residual |
|---|---|---|---|---|---|
| 1° | 2.006105 | 2.006067 | +0.0019% | 2.006105 s | < 10⁻⁷ s |
| 5° | 2.007022 | 2.006067 | +0.0476% | 2.007022 s | 2×10⁻¹⁰ s |
| 20° | 2.021451 | 2.006067 | +0.7611% | 2.021450 s | 8.6×10⁻⁷ s |
| 45° | 2.086256 | 2.006067 | +3.8437% | 2.086140 s | 1.2×10⁻⁴ s |
| 90° | 2.367842 | 2.006067 | +15.28% | 2.359159 s | 8.7×10⁻³ s |

**Regime of validity.** The small-angle form is exact to better than 0.05% for
$\theta_0 \le 5°$, better than 1% up to $\theta_0 \approx 23°$ (exact quadrature gives
0.998% at 22.9°, 1.10% at 24°), and unusable beyond
about $45°$. Note also that the *two-term* series is accurate to 0.006% at 45°
while the zero-order small-angle form is 3.8% wrong: keeping one more term buys
two orders of magnitude. That asymmetry — cheap improvement near the edge of the
regime — is the general reason to keep the next term.

### 3.2 Diffusion: why the exponent is always 1/2

For the diffusion equation $\partial T/\partial t = \kappa\,\nabla^{2}T$, apply
π reasoning to a length scale: the variables are $L$, $t$, $\kappa$, and
$\kappa$ has dimensions $\mathrm{L^{2}T^{-1}}$. The group
$\Pi = \kappa t/L^{2}$ is the only one, so

$$L \sim \sqrt{\kappa t}, \qquad t \sim \frac{L^{2}}{\kappa}.$$

This is *not* an assumption about materials. Any diffusive process obeys
$L \propto \sqrt{t}$ with the diffusivity as the only dimensional input, which
is why the result is identical for heat, for magnetic field diffusion in a
conductor ([02-07-06](../07-electromagnetism/06-em-in-conductors.md)) and for
pore-pressure diffusion ([02-06-05](../06-fluid-mechanics/05-porous-media-flow.md)).

Numerically, with the nominal crustal thermal diffusivity
$\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ (constant handbook, nominal):

| $L$ | $L^{2}/\kappa$ | in years |
|---|---|---|
| 0.1 m | $10^{4}$ s | $3.2\times10^{-4}$ yr (2.8 h) |
| 1 m | $10^{6}$ s | 0.0317 yr (11.6 d) |
| 1 km | $10^{12}$ s | $3.2\times10^{4}$ yr |
| 10 km | $10^{14}$ s | $3.2\times10^{6}$ yr |
| 100 km | $10^{16}$ s | $3.2\times10^{8}$ yr |

**Worked geophysical consequence.** A lithospheric column of age $t$ has a
thermal boundary-layer thickness of order $\sqrt{\kappa t}$. At $t = 1$ Ma,

$$\sqrt{(10^{-6})(3.156\times10^{13})} = 5.62\times10^{3}\ \mathrm{m}
= 5.6\ \mathrm{km},$$

and at 100 Ma it is 56 km — a factor of 10, from a factor of 100 in time. The
half-space cooling heat flow follows the reciprocal
$q = k\Delta T/\sqrt{\pi\kappa t}$; with $k = 2.5\ \mathrm{W\,m^{-1}K^{-1}}$
and $\Delta T = 1300$ K it gives 326, 103, 46 and 33 mW m⁻² at 1, 10, 50 and
100 Ma. The observed flattening of heat flow beyond ~50–100 Ma is therefore
*evidence against* pure half-space cooling and in favour of a convecting
mantle — a conclusion reached by comparing a scaling law with data, which is
the standard role of scaling laws in geophysics.

**Regime of validity.** The $\sqrt{\kappa t}$ scaling holds while the diffusive
length is smaller than the domain and while $\kappa$ is constant. In the
lithosphere the second condition fails slowly as temperature-dependent
conductivity and radiogenic heating accumulate; the deviation from
$\sqrt{t}$ is itself the diagnostic.

### 3.3 Dynamic similarity, quantified

Dynamic similarity requires the π groups to match. For convection the
controlling group is the Rayleigh number. Evaluating with the constant
handbook's nominal values ($\rho = 3300\ \mathrm{kg\,m^{-3}}$,
$\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$, $\eta = 10^{21}$ Pa s, $L = 2.89\times
10^{6}$ m) and with two **assumed inputs** — thermal expansivity
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$ and temperature drop
$\Delta T = 3000$ K across the mantle:

$$\mathrm{Ra} = \frac{\rho g\alpha\Delta T L^{3}}{\kappa\eta}
= \frac{3300\times9.81\times3\times10^{-5}\times3000\times(2.89\times10^{6})^{3}}
{10^{-6}\times10^{21}} = 7.03\times10^{7}.$$

The onset of convection in this geometry is of order $10^{3}$, so the mantle is
supercritical by some 4–5 orders of magnitude. Note carefully what that number
is: a product of two nominal and two assumed inputs. The demonstration prints
the sensitivity: varying $\eta$ over just the decade $10^{20}$–$10^{22}$ Pa s
moves $\mathrm{Ra}$ from $7.0\times10^{8}$ to $7.0\times10^{6}$ — three orders
of magnitude from one nominal input, with the whole nominal range being
$10^{19}$–$10^{22}$ Pa s. The
*conclusion* (vigorous convection) is robust; the *number* is not. That
distinction is the single most important habit this lesson can give you.

### 3.4 Similitude that fails: Reynolds number across 28 orders

$$\mathrm{Re} = \frac{\rho u L}{\eta}.$$

| System | $\rho$ (kg m⁻³) | $u$ (m s⁻¹) | $L$ (m) | $\eta$ (Pa s) | $\mathrm{Re}$ |
|---|---|---|---|---|---|
| mantle convection | 3300 | $3.17\times10^{-10}$ | $10^{6}$ | $10^{21}$ | $1.05\times10^{-21}$ |
| ridge hydrothermal plume | 3300 | 0.1 | $10^{3}$ | $10^{21}$ | $3.3\times10^{-16}$ |
| ocean current | 1025 | 0.1 | $10^{2}$ | $10^{-3}$ | $1.03\times10^{7}$ |
| aquifer flow | 1025 | $10^{-5}$ | 1 | $10^{-3}$ | 10.3 |

The ratio of the first and third is $9.8\times10^{27}$. No laboratory tank can
bridge that: to make a 0.3 m water tank have $\mathrm{Re} = 10^{-21}$ you would
need to slow the fluid to $3\times10^{-18}$ m/s, i.e. 0.1 nm per million years,
at which point Brownian motion and laboratory vibration dominate. **Mantle
convection has no dynamically similar laboratory analogue in a normal
gravitational field.** Analogue and centrifuge experiments therefore target
specific sub-problems (buoyancy of a Rayleigh–Taylor instability, for instance)
rather than "mantle convection".

The interesting counterexample in the same table is the aquifer: $\mathrm{Re}
\approx 10$ means Darcy flow is genuinely laminar, which is why Darcy's law is
linear. Dimensional reasoning tells you when a linear law is safe.

### 3.5 Isostasy: a scaling law with a dimensionless coefficient

Airy isostasy requires the pressure of a topographic column to be balanced by a
root. With crustal density $\rho_c$ and mantle density $\rho_m$,

$$\rho_c h = (\rho_m - \rho_c) r
\quad\Longrightarrow\quad
r = \frac{\rho_c}{\rho_m-\rho_c}\,h.$$

The coefficient is dimensionless and *independent of the height*: with the
nominal $\rho_c = 2700$ and $\rho_m = 3300\ \mathrm{kg\,m^{-3}}$ it is

$$\frac{\rho_c}{\rho_m-\rho_c} = \frac{2700}{600} = 4.5,$$

so a 5 km mountain has a 22.5 km root, and a 500 m plateau has a 2.25 km root.
Two cautions, both dimensional in character:

- The ratio depends on the *density contrast*, so a 5% error in $\rho_m-\rho_c$
  is a 5% error in the root — here 0.05 × 600 = 30 kg m⁻³ gives ±1.1 km on the
  22.5 km root.
- The linear law assumes local (Airy) compensation. If the load is supported by
  the strength of a plate over a flexural length scale, the root is *smaller*
  and spread over a wider region. The dimensionless flexural parameter — the
  ratio of the flexural wavelength to the load width — decides which regime
  applies. See [07-gravity-geodesy](../../07-gravity-geodesy/README.md).

### 3.6 When scaling fails outright: strength versus weight

Scale a structure by a factor $s$. Its weight scales as $s^{3}$, the
load-bearing cross-section as $s^{2}$, so the stress scales as $s^{1}$. A
material constant such as rock strength does not scale at all. Therefore:

- A 1:100 model of a mountain carries 1/100 of the prototype stress and cannot
  fail the way the prototype fails.
- The largest mountain on Earth and the largest on Mars differ by a factor of
  about 2.5 in height, and that difference is a *gravity* difference
  (surface gravity differs), not a rock difference. Gravity is present in every
  geophysical π group with exponent 1 and cannot be scaled.

## 4. Physical interpretation

### 4.1 What scaling laws are for

1. **Order-of-magnitude estimates** before any computation (Fermi reasoning
   formalised).
2. **Design of experiments** — which similarity conditions must be enforced.
3. **Collapse of data.** Plot $\mathrm{Re}$ against a friction factor and many
   pipes become one curve. Plot the same data dimensionally and nothing is
   visible. This is the same statement as: physics lives in the dimensionless
   groups.
4. **Assumption audits.** A scaling law makes explicit exactly which quantities
   enter. When you write $t \sim L^{2}/\kappa$, you have asserted that $\kappa$
   is the only relevant transport coefficient.

### 4.2 What a scaling law cannot do

It cannot give the dimensionless coefficient. The π theorem produced
$T = \sqrt{l/g}\,\phi(\theta_0)$; the value $\phi = 2\pi$ (small angles) requires
the equation of motion. So a scaling law is a *parametric form*, and it must be
calibrated or derived. Data collapse gives the exponent; only theory or
experiment gives the coefficient. This is exactly why it is safe to say that
lithospheric heat flow should fall as $t^{-1/2}$ while its amplitude needs a
thermal model.

### 4.3 Regime diagrams

Combining two groups produces a regime diagram, and geophysics is full of them:

| Axes | Regimes | Example |
|---|---|---|
| $\mathrm{Re}$, roughness | laminar / transitional / turbulent | pipe flow, groundwater |
| $\mathrm{Ra}$, $\mathrm{Pe}$ | conduction / steady convection / time-dependent | mantle |
| $\mathrm{De}$, viscosity ratio | elastic / viscoelastic / viscous | rock deformation |
| $f$-plane vs $\beta$-plane balance | geostrophic / Rossby-wave | ocean and atmosphere |

A "regime of validity" is a region on one of these diagrams. When this
repository says an approximation has a regime, it means: *here is the
dimensionless number, and here is the value at which the approximation fails.*

## 5. Units and dimensional analysis

Scaling laws are invariant under a change of units, which is a *test* you can
apply: if a relation changes form when you switch from SI to cgs, the relation
was calibrated to a unit system rather than derived. Two practical rules:

1. **Report the groups, not the formula.** $t = 0.083\,L^{2}/\kappa$ with $L$ in
   km, $t$ in Ma and $\kappa$ in m²/s is a formula with a unit-dependent
   constant. $t \sim L^{2}/\kappa$ with everything in SI is a scaling law. Write
   the constant only when you can name its origin.
2. **Check the group is dimensionless in the units you are using.** The Fourier
   number $\kappa t/L^{2}$ must come out dimensionless: with $\kappa$ in
   m² yr⁻¹, $t$ in yr and $L$ in m, it does. With $\kappa$ in m² s⁻¹ and $t$ in
   Ma, it does not — a factor of $3.156\times10^{13}$ error, which the
   dimensions *cannot* catch because Ma and s are both times.

That last clause is the practical warning: converting times by eye is the most
common scaling error in geophysics, precisely because it is dimensionally
invisible.

## 6. Assumptions and regime of validity

1. **Complete variable list.** π theorem gives $n - r$ groups *for the list of
   parameters you supplied*. Omit thermal expansivity and you will get a
   self-consistent but wrong set. There is no mechanical check for this; a
   physics argument is required.
2. **Dimensional independence.** The rank $r$ must be computed, not assumed.
   If two of your parameters have proportional dimension vectors, the rank drops
   and the count of groups rises.
3. **Only dimensional information is used.** π groups are necessary, not
   sufficient: two systems with equal groups are dynamically similar *provided*
   the governing equations are the same and the boundary conditions scale too.
4. **Constants are not dimensionless.** The presence of a dimensional constant
   (like $G$) that appears nowhere in your list invalidates the scaling. This is
   why the "why is gravity the same for a scaled mountain" failure of §3.6
   occurs.
5. **Power laws hold over the range fitted.** A scaling law fitted over one
   decade may not extrapolate to four. Mantle rheology, for instance, is
   non-Newtonian; the effective viscosity is a function of stress, so $\eta$ in
   the Rayleigh number is itself scale-dependent.
6. **Self-similarity can break.** The half-space cooling law breaks when the
   boundary layer reaches the base of the plate.

## 7. Python demonstration

The script does five things: (a) computes the small-angle pendulum error by
exact quadrature; (b) builds the exponent matrix for three problems and obtains
the π groups from its null space in exact rational arithmetic, then verifies
that $\mathrm{Ra}$ is dimensionless; (c) tabulates diffusion times and the
conduction/advection balance; (d) evaluates $\mathrm{Re}$ for four geophysical
flows; (e) evaluates the isostatic ratio, a wavelength scaling, $\mathrm{Ra}$
with an explicit sensitivity table, and the strength-versus-weight failure.

Full listing: [`code/scaling_demo.py`](./code/scaling_demo.py).

The null-space machinery — the part that makes π theorem checkable rather than
decorative:

```python
def null_space(rows, ncols):
    """Basis of the null space of the exponent matrix, dimension n - rank."""
    a, pivots = rref(rows)
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for f in free:
        v = [Fraction(0)] * ncols
        v[f] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -a[i][f]
        basis.append(v)
    return basis, pivots
```

Observed output (Python 3.14.4, standard library only):

```text

========================================================================
1. Buckingham Pi: what the pendulum period cannot depend on
========================================================================
  Variables: l [L], g [L T^-2], m [M], theta0 [1].
  Three dimensional variables in two dimensions -> one Pi group,
  Pi = T sqrt(g/l) = const * f(theta0).  Mass cannot appear.
  theta0 =   1.0 deg: T = 2.006105 s (small-angle 2.006067 s, series 2.006105 s, error +0.0019 %)
  theta0 =   5.0 deg: T = 2.007022 s (small-angle 2.006067 s, series 2.007022 s, error +0.0476 %)
  theta0 =  20.0 deg: T = 2.021451 s (small-angle 2.006067 s, series 2.021450 s, error +0.7611 %)
  theta0 =  45.0 deg: T = 2.086256 s (small-angle 2.006067 s, series 2.086140 s, error +3.8437 %)
  theta0 =  90.0 deg: T = 2.367842 s (small-angle 2.006067 s, series 2.359159 s, error +15.2787 %)

========================================================================
1b. Buckingham Pi by null space, done exactly
========================================================================
  simple pendulum: 4 variables, rank 3, 1 independent Pi group(s)
      Pi = g^(1/2) T^1 / l^(1/2)
  Rayleigh-Benard convection: 7 variables, rank 4, 3 independent Pi group(s)
      Pi = alpha^1 dT^1
      Pi = kappa^1 / g^(1/2) L^(3/2)
      Pi = eta^1 / rho^1 g^(1/2) L^(3/2)
  heat diffusion (L, t, kappa): 3 variables, rank 2, 1 independent Pi group(s)
      Pi = t^1 kappa^1 / L^2
  Candidate named group Ra = rho g alpha dT L^3 / (kappa eta):
      dimensionless? True
  The null space is a vector space: any product of the basis
  groups is also dimensionless, and the *choice* of basis is
  arbitrary.  Ra is one convenient member of the same space.

========================================================================
2. Heat diffusion: t ~ L^2 / kappa
========================================================================
  kappa = 1.0e-06 m^2/s (nominal, crustal rock)
      L                L^2/kappa (s)        (years)
        0.1 m           1.0000e+04       3.1689e-04
          1 m           1.0000e+06       3.1689e-02
      1e+03 m           1.0000e+12       3.1689e+04
      1e+04 m           1.0000e+14       3.1689e+06
      1e+05 m           1.0000e+16       3.1689e+08
  The quadratic is why a 10 cm sample equilibrates in hours, a 1 m
  block in about a fortnight, and a 100 km column in ~10^8 years.
  Doubling L quadruples t; no material property changes that.
  Conduction balances advection at u = 1e-09 m/s when L = 1e+03 m
  Conduction balances advection at u = 1e-11 m/s when L = 1e+05 m
  Conduction balances advection at u = 1e-04 m/s when L = 0.01 m

========================================================================
3. Reynolds number: two geophysical fluids, 28 orders apart
========================================================================
      system                rho      u (m/s)    L (m)      Re
  mantle convection        3300   3.169e-10     1e+06   1.046e-21
  mid-ocean ridge plume    3300   1.000e-01     1e+03   3.300e-16
  ocean current            1025   1.000e-01       100   1.025e+07
  aquifer flow             1025   1.000e-05         1   1.025e+01
  Dynamic similarity between a laboratory tank and the mantle would
  require Reynolds numbers equal to within a factor of order 1.
  They differ by ~28 orders of magnitude, so no laboratory tank is
  a scale model of the mantle in the ordinary sense.

========================================================================
4. Airy isostasy: the root is not the height
========================================================================
  rho_c = 2700, rho_m = 3300 kg/m^3 (nominal)
  root / topography = rho_c / (rho_m - rho_c) = 4.5000
  topography  0.5 km -> root   2.25 km (Moho depth below the reference crust ~ 2.25 km deeper)
  topography  2.0 km -> root   9.00 km (Moho depth below the reference crust ~ 9.00 km deeper)
  topography  5.0 km -> root  22.50 km (Moho depth below the reference crust ~ 22.50 km deeper)
  topography  8.0 km -> root  36.00 km (Moho depth below the reference crust ~ 36.00 km deeper)
  A linear scaling with a dimensionless coefficient: the physics
  fixes the coefficient, the density contrast alone.

========================================================================
5. Seismic wavelength scaling: lambda = v / f
========================================================================
  v =   5500 m/s, f =   10.0 Hz -> lambda =   550.00 m; half-wavelength =   275.00 m
  v =   5500 m/s, f =    1.0 Hz -> lambda =  5500.00 m; half-wavelength =  2750.00 m
  v =   3000 m/s, f =   50.0 Hz -> lambda =    60.00 m; half-wavelength =    30.00 m
  v =   1500 m/s, f =  250.0 Hz -> lambda =     6.00 m; half-wavelength =     3.00 m
  Resolution scales with wavelength.  This one relation, not any
  instrument specification, sets what a seismic survey can see.
  Values of v here are nominal handbook anchors; f is an assumed
  source frequency.

========================================================================
6. Rayleigh number: an assumed-parameter calculation
========================================================================
  Assumed: alpha = 3.0e-05 1/K, dT = 3000 K
  Nominal: rho = 3300 kg/m^3, kappa = 1.0e-06 m^2/s,
           eta = 1e+21 Pa s, L = 2.89e+06 m
  Ra = rho g alpha dT L^3 / (kappa eta) = 7.033e+07
  The onset of convection is of order 10^3 in this geometry, so
  the mantle is supercritical by ~7 orders of magnitude -- but note
  that Ra here contains four assumed or nominal inputs, and the
  answer inherits their uncertainty.  Conduct the sensitivity:
    eta = 1e+20 Pa s -> Ra = 7.033e+08
    eta = 1e+21 Pa s -> Ra = 7.033e+07
    eta = 1e+22 Pa s -> Ra = 7.033e+06

========================================================================
7. A scaling that fails: strength versus weight
========================================================================
  A body scaled by a factor s has weight scaling as s^3 and
  load-bearing cross-section as s^2, so the stress scales as s.
  scale factor    1: weight x        1, area x      1, stress x   1.0
  scale factor   10: weight x     1000, area x    100, stress x  10.0
  scale factor  100: weight x  1000000, area x  10000, stress x 100.0
  This is why a scale model of a mountain is not a model of a
  mountain: gravity is not scalable, and rock strength is a
  material constant rather than a scaled quantity.
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| 4 variables, rank 3 → 1 π group for the pendulum | mass is absent from the group, so the period is independent of the bob — a *derived* statement, not a memorised one |
| Rayleigh–Bénard: 7 variables, rank 4 → 3 groups | the physical literature uses a *chosen* combination (Ra) from a 3-dimensional space of combinations |
| `Ra` printed `dimensionless? True` | the named group is verified against the algebra instead of being trusted |
| pendulum error +0.0476% at 5°, +0.761% at 20°, +3.84% at 45° | the small-angle regime has a numeric boundary; state it |
| diffusion 0.1 m → 10⁴ s, 100 km → 3.2×10⁸ yr | one quadratic law spans 12 orders of magnitude of time |
| $\mathrm{Re}$ from $10^{-21}$ to $10^{7}$ | dynamic similarity across these is impossible; state that rather than implying a tank models the mantle |
| Root/topography = 4.5000 | the coefficient comes from the density contrast alone |

> **Breaking exercise.** Delete `alpha` from the Rayleigh–Bénard variable list
> and rerun. Predict the new group count before running ($7 \to 6$ variables,
> rank $4 \to 3$, so still 3 groups — but the groups change meaning). Then add
> the thermal conductivity $k$ as well and see whether the count rises (it does
> not: $k = \rho c_p \kappa$ introduces no new dimension, so the rank rises by 1
> and the count stays at 3).

## 8. Common mistakes

1. **Assuming a scale model scales results.** Similarity is a list of conditions,
   not a length ratio.
2. **Quoting a power law with a unit-dependent constant.** Give the group and
   the coefficient's origin.
3. **Forgetting that time units hide in "Ma".** $\kappa$ in m² s⁻¹ with $t$ in
   Ma is a $3.156\times10^{13}$ error that dimensions cannot detect.
4. **Treating $\pi$ groups as unique.** The null space is a vector space; there
   are infinitely many bases. Choose the one that names physics.
5. **Using the small-angle approximation outside its regime.** The numbers are
   in §3.1: 3.84% at 45°, 15.3% at 90°.
6. **Reading more precision into a dimensionless number than its inputs
   support.** $\mathrm{Ra} = 7.03\times10^{7}$ contains two assumed inputs;
   quote it as $10^{8}$ and state the sensitivity.
7. **Assuming a scaling exponent is universal.** Exponents that came from
   dimensions ($1/2$ for diffusion) are robust; exponents that came from a fit
   are not.
8. **Neglecting a dimensional constant.** If $G$, $c$, $h$ or $k_B$ is
   physically present, no pure π argument applies without including it.

## 9. Real-world applications

1. **Analogue modelling of tectonics.** A sandbox model must match density
   ratios, viscosity ratios and the ratio of gravity-driven stress to yield
   stress. Published models list these explicitly; the ones that do not are not
   interpretable.
2. **Centrifuge modelling.** Increasing effective gravity by $N$ allows a
   smaller model to match a gravity-driven π group — the standard trick for salt
   diapirs and slope stability.
3. **Reservoir simulation.** Upscaling from a core plug to a grid cell requires
   matching the relevant groups (capillary number, Péclet number); this is why
   relative permeability curves are scale-dependent.
4. **Earthquake source scaling.** Empirical scaling relations between rupture
   length, slip and magnitude are power laws, and their exponents are *measured*,
   not derived. Dimensional analysis constrains the functional form only.
5. **Climate and energy balance.** The ratio of radiative to advective transport
   (a Péclet-like group) separates regimes of atmospheric heat transport.
6. **Instrument design.** A gravimeter's readout is a displacement; the scale
   factor converts to mGal. Its thermal stability must be matched to the
   *gradient* scale (0.308 mGal/m) — again a ratio of two dimensional
   quantities.

## 10. Further reading

- **Buckingham, E. (1914). On physically similar systems; illustrations of the
  use of dimensional equations. *Physical Review*, 4(4), 345–376.** The original
  statement of the π theorem; short and still readable. Level: intermediate.
  (Obtain through a library; this repository cites it bibliographically only.)
- **Barenblatt, G. I. *Scaling, Self-similarity, and Intermediate Asymptotics.*
  Cambridge University Press.** The graduate treatment, including when
  self-similarity fails. Level: graduate.
- **Sedov, L. I. *Similarity and Dimensional Methods in Mechanics.*** The
  classical reference for similarity arguments in continua. Level: graduate.
- **Fowler, C. M. R. *The Solid Earth* (2nd ed.).** Chapters on heat flow and
  convection use the scaling arguments of §3.2 and §3.3. Level: intermediate.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (3rd ed.).** Contains the
  Rayleigh number, the boundary-layer scaling, and the isostatic relations used
  here, with the coefficients derived. Level: advanced.
- **JCGM 100:2008 (GUM).** For the uncertainty language applied to the assumed
  inputs in §3.3. Level: reference.

> Citation note: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text.

## 11. Related lessons

- [02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity](./01-physical-quantities.md) —
  the exponent algebra this lesson turns into a machine.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](./02-measurement-uncertainty.md) —
  what makes "the inputs are nominal" an honest statement.
- [02-01-04 Conservation Laws as the Engine of Physical Modelling](./04-conservation-laws.md) —
  scaling plus a conservation law is how a governing equation is guessed.
- [02-03-04 Wave Description: Amplitude, Frequency, Wavelength, Phase Velocity](../03-oscillations-and-waves/04-wave-basics.md) —
  the wavelength scaling of §5.
- [02-06-06 Mantle Convection and Rayleigh–Bénard Instability](../06-fluid-mechanics/06-mantle-convection.md) —
  the Rayleigh number used quantitatively.
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md) —
  where similarity becomes grid design and dimensionless time stepping.

## Exercises

Attempt the graded problems in
[`exercises/03-scaling-laws-exercises.md`](./exercises/03-scaling-laws-exercises.md),
then compare with
[`exercises/03-scaling-laws-solutions.md`](./exercises/03-scaling-laws-solutions.md).

## Self-assessment checklist

- [ ] I can state Buckingham's π theorem and explain why the number of groups is
      a null-space dimension. (Section 2.1)
- [ ] I can build an exponent matrix, compute its rank and null space, and
      produce the π groups for a problem I have not seen. (Section 7)
- [ ] I can verify that a named group such as $\mathrm{Ra}$ is dimensionless
      using the algebra. (Section 3.3)
- [ ] I can state the small-angle pendulum error at 5°, 20° and 45° from the
      computed table and give the angle beyond which the approximation is
      unusable. (Section 3.1)
- [ ] I can derive $L \sim \sqrt{\kappa t}$ by π reasoning and apply it to a
      lithospheric thickness and heat-flow estimate. (Section 3.2)
- [ ] I can explain, with numbers, why a laboratory tank cannot be dynamically
      similar to the mantle. (Section 3.4)
- [ ] I can derive the Airy root coefficient and state its two main
      limitations. (Section 3.5)
- [ ] I can give an example where scaling fails because a material constant or a
      dimensional constant does not scale. (Section 3.6)
