---
id: 02-04-04
title: "Young's Modulus, Poisson's Ratio and the Elastic Constants"
level: advanced
prereqs: ["02-04-03", "01-01-03"]
estimated_minutes: 90
tags: [elastic-moduli, poisson-ratio, gassmann, rock-physics]
---

# Young's Modulus, Poisson's Ratio and the Elastic Constants

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** each of the six isotropic elastic constants in terms of the
   geometry of the measurement that determines it.
2. **Convert** between any pair of them, and verify the conversions by two
   independent routes.
3. **Derive** the exact bounds on $v_p/v_s$ in terms of the stability conditions,
   and explain why the familiar $\sqrt2$ minimum is conditional.
4. **Compute** the sensitivity of the seismic velocities to each modulus and to
   density, and rank them by importance.
5. **Apply** Gassmann fluid substitution to a gas sand, and state precisely which
   regime the answer describes and which observations it fails to explain.
6. **Verify** the modulus algebra numerically, including the uniaxial-stress test
   that defines $E$ and $\nu$.

## Prerequisites

- [02-04-03 Constitutive Laws and Generalised Hooke's Law](./03-constitutive-laws.md)
  — the stiffness tensor and the Lamé parameters.
- [01-01-03 Units and Dimensional Analysis](../../01-mathematics/01-arithmetic/03-units-and-dimensional-analysis.md)
  — the unit and dimensional checks used throughout.

## 1. Why there are so many constants

Six symbols — $\lambda$, $\mu$, $E$, $\nu$, $K$ and $M$ — describe the same
two-parameter isotropic material. The multiplication of names is historical and
practical rather than physical:

- $\lambda$ and $\mu$ are the natural constants of the *tensor* form (lesson
  02-04-03) and appear directly in the wave speeds;
- $K$ and $\mu$ are the natural constants of *volume* and *shape* change;
- $E$ and $\nu$ are the natural constants of a **laboratory test** (uniaxial
  stress), which is why they dominate the engineering and rock-mechanics
  literature;
- $M = \lambda + 2\mu$ is the natural constant of a **seismic measurement**
  (plane-wave, uniaxial-strain geometry), and it is the one that appears in
  $v_p$.

The practical lesson of the lesson is: **always ask which geometry a modulus
describes**, because the algebra between them is exact and uninteresting, while
the geometry is what makes a number right or wrong by tens of per cent.

## 2. Precise definitions

| Constant | Symbol | Definition (measurement geometry) | Units |
|---|---|---|---|
| Shear modulus | $\mu$ (or $G$) | shear stress ÷ shear strain, at constant volume | Pa |
| Bulk modulus | $K$ | hydrostatic pressure ÷ volumetric strain | Pa |
| Young's modulus | $E$ | axial stress ÷ axial strain in a **uniaxial stress** test (lateral faces free) | Pa |
| Poisson's ratio | $\nu$ | $-$lateral strain ÷ axial strain in the same test | — |
| Constrained modulus | $M$ | axial stress ÷ axial strain in a **uniaxial strain** test (lateral strain zero) | Pa |
| Lamé's first parameter | $\lambda$ | $K - 2\mu/3$; the volumetric stiffness in the tensor form | Pa |

Two of these are "primitive" in the sense that they are defined by a single
stress–strain pair with no coupling ($\mu$ and $K$); the others involve a
constraint, which is why they can be negative ($\lambda$) and why $\nu$ has a
bounded range.

## 3. Derivations

### 3.1 The modulus relations

Start from the isotropic law in the form
$\sigma_{ij} = \lambda\varepsilon_{kk}\delta_{ij}+2\mu\varepsilon_{ij}$ and impose
the geometry of each test.

**Hydrostatic compression.** $\sigma_{ij} = -p\delta_{ij}$ and
$\varepsilon_{ij} = (\varepsilon_{kk}/3)\delta_{ij}$. Then
$-p = (3\lambda+2\mu)\varepsilon_{kk}/3$, so

$$K = \lambda + \frac{2\mu}{3} \qquad\Longleftrightarrow\qquad
\lambda = K-\frac{2\mu}{3} . \tag{1}$$

**Uniaxial stress.** $\sigma_{11} = \sigma$, all other stress components zero.
Then $\varepsilon_{22} = \varepsilon_{33} = -\nu\varepsilon_{11}$ by symmetry,
and substituting:

$$\sigma = (\lambda+2\mu)\varepsilon_{11} + \lambda(\varepsilon_{22}+\varepsilon_{33})
= \left[(\lambda+2\mu) - \frac{2\lambda^2}{\lambda+\mu}\right]\varepsilon_{11} ,
\tag{2}$$

where the lateral strains were eliminated using the zero lateral-stress
conditions. Hence

$$E = \frac{\mu(3\lambda+2\mu)}{\lambda+\mu}, \qquad
\nu = \frac{\lambda}{2(\lambda+\mu)} . \tag{3}$$

**Uniaxial strain.** $\varepsilon_{22} = \varepsilon_{33} = 0$ but the lateral
stresses are not zero; then $\sigma_{11} = (\lambda+2\mu)\varepsilon_{11}$, so

$$M = \lambda+2\mu = K+\frac{4\mu}{3} . \tag{4}$$

**The inverse relations** (inverting equation (3)):

$$\lambda = \frac{E\nu}{(1+\nu)(1-2\nu)}, \qquad
\mu = \frac{E}{2(1+\nu)}, \qquad
K = \frac{E}{3(1-2\nu)} . \tag{5}$$

Equation (5) is where the stability constraints become visible, and §3.2 derives
them properly.

**The velocity ratios.** Combining equations (1) and (4):

$$v_p^2 = \frac{\lambda+2\mu}{\rho} = \frac{M}{\rho} = \frac{K+\frac43\mu}{\rho},
\qquad
v_s^2 = \frac{\mu}{\rho} , \tag{6}$$

$$\frac{v_p^2}{v_s^2} = \frac{K}{\mu}+\frac43
= \frac{2(1-\nu)}{1-2\nu} = \frac{\lambda+2\mu}{\mu} . \tag{7}$$

All three forms are the same statement; the last is the one to use when a
Poisson's ratio is given, and the second when a bulk-to-shear ratio is given.

### 3.2 The exact bounds on $v_p/v_s$

The stability conditions from the strain-energy positivity (lesson 02-04-03 §3.3)
are

$$\mu > 0, \qquad K = \lambda+\tfrac23\mu > 0 . \tag{8}$$

Then

$$\frac{v_p^2}{v_s^2} = \frac{K}{\mu}+\frac43 > \frac43
\quad\Longrightarrow\quad
\boxed{\ \frac{v_p}{v_s} > \frac{2}{\sqrt3} = 1.154701\ } \tag{9}$$

as an **unconditional** bound for any stable isotropic elastic solid. If, in
addition, $\lambda \ge 0$ — which is true of every ordinary material, since
$\lambda = 0$ corresponds to $\nu = 0$ — then $K \ge \tfrac23\mu$ and

$$\frac{v_p}{v_s} \ge \sqrt2 = 1.414214 , \qquad\text{with equality at } \nu = 0.
\tag{10}$$

The demo tabulates the ratio from $\nu = -0.9$ to $\nu = 0.49$ and confirms both
bounds: 1.164965 at $\nu = -0.9$ (above $2/\sqrt3$ ✓), exactly 1.414214 at
$\nu = 0$, 1.732051 ($=\sqrt3$) at $\nu = 0.25$, and 7.141428 at $\nu = 0.49$
(diverging as $\nu\to1/2$ with $K\to\infty$).

**Two things to state whenever you quote the ratio.** First, the $\sqrt2$ minimum
requires $\lambda \ge 0$; the rigorous bound is $2/\sqrt3$. Second, the ratio says
nothing about absolute velocities: a soft and a stiff rock can share the same
$v_p/v_s$.

The **unconditional** statement that survives all conventions is

$$v_p > v_s \quad\text{always, for any stable isotropic elastic solid} \tag{11}$$

because $\lambda+2\mu-\mu = \lambda+\mu = K+\mu/3 > 0$ from equation (8). That is
the inequality that must appear in the mastery checkpoint, and it holds without
any sign assumption on $\lambda$.

### 3.3 Which parameters matter for the velocities?

Differentiating equation (6),

$$\frac{\delta v_p}{v_p} = \frac12\frac{\delta M}{M}
-\frac12\frac{\delta\rho}{\rho}, \qquad
\frac{\delta v_s}{v_s} = \frac12\frac{\delta\mu}{\mu}
-\frac12\frac{\delta\rho}{\rho} . \tag{12}$$

Three consequences, all of which the demo's numerics confirm:

- **Density and modulus errors are equally weighted** in the fractional sense,
  which is why an accurate velocity requires an accurate density — and why
  density is often the weakest-known input.
- **Volume changes affect both speeds with the same sign through density, but
  differently through the moduli**: adding a fluid raises $K$ (and hence $v_p$
  through $M$) while barely touching $\mu$, so $v_s$ falls and $v_p$ can rise or
  fall. That asymmetry is the basis of fluid detection.
- **$\lambda$ is poorly constrained by seismic data.** Velocities give $M$ and
  $\mu$; $K$ follows only if $\mu$ is known and the material is isotropic, and
  $\lambda$ is then a derived quantity with a large relative uncertainty when $K$
  is small.

### 3.4 Gassmann fluid substitution

For a fluid-saturated porous rock at low frequency, with $\phi$ the porosity,
$K_{\min}$ the mineral bulk modulus, $K_f$ the fluid modulus and
$K_{\text{dry}}$ the dry frame modulus:

$$K_{\text{sat}} = K_{\text{dry}} + \frac{\left(1-K_{\text{dry}}/K_{\min}\right)^2}
{\dfrac{\phi}{K_f}+\dfrac{1-\phi}{K_{\min}}-\dfrac{K_{\text{dry}}}{K_{\min}^2}} ,
\qquad
\mu_{\text{sat}} = \mu_{\text{dry}} , \qquad
\rho = (1-\phi)\rho_{\min}+\phi\rho_f . \tag{13}$$

Two structural features of equation (13) matter more than the algebra:

- **$\mu$ is unchanged**, because a fluid cannot support shear. Therefore
  $v_s = \sqrt{\mu/\rho}$ changes only through the density, and adding fluid
  always *lowers* $v_s$. This is the robust statement of the lesson.
- **$K_{\text{sat}}$ depends on $K_f$ through a harmonic average** ($\phi/K_f$
  term), so when the fluid is a gas with $K_f$ of order $10^7$ Pa the saturation
  has almost no effect on $K$ until the water saturation approaches 1.

The demo's numbers for a synthetic sandstone ($\phi = 0.2$,
$K_{\min} = 36$ GPa, $G = 10$ GPa, $K_{\text{dry}} = 10$ GPa, $K_w = 2.2$ GPa,
$K_g = 10$ MPa) illustrate the consequence:

| $S_w$ | $K_{\text{sat}}$ (GPa) | $\rho$ (kg m⁻³) | $v_p$ (m s⁻¹) | $v_s$ (m s⁻¹) | $v_p$ patchy (m s⁻¹) |
|---|---|---|---|---|---|
| 0.00 | 10.026 | 2120 | 3319.24 | 2171.74 | 3319.24 |
| 0.50 | 10.052 | 2220 | 3245.50 | 2122.32 | 3378.12 |
| 0.90 | 10.249 | 2300 | 3202.03 | 2085.13 | 3462.95 |
| 0.99 | 11.713 | 2318 | 3287.11 | 2077.03 | 3488.45 |
| 1.00 | 14.948 | 2320 | 3491.46 | 2076.14 | 3491.46 |

Read the table carefully:

- $v_s$ falls monotonically, 2171.74 → 2076.14 m s⁻¹, by 4.4 per cent. Robust.
- $v_p$ *falls* from 3319.24 to a minimum of 3201.96 m s⁻¹ and only returns to
  the dry value at $S_w = 0.9935$. So the uniform-saturation (Gassmann) model
  predicts that partial water saturation makes a gas sand *slower*, not faster —
  a result that surprises and is often misquoted.
- The **patchy-saturation** column, computed as the harmonic average of the two
  fully saturated end members, is *higher* than Gassmann at every intermediate
  saturation, reaching 3437.69 m s⁻¹ at $S_w = 0.8$ where Gassmann gives 3207.75.

**Regime of validity.** Equation (13) assumes a homogeneous pore fluid, low
frequency (the pore pressure equilibrates every cycle), and no chemical
interaction with the frame. Patchy saturation violates the first assumption when
the gas pockets are larger than the diffusion length
$\sqrt{D/\omega}$; the high-frequency (squirt-flow) regime violates the second.
Laboratory measurements often show a *decrease* of $v_p$ at the first few per cent
of saturation, in qualitative agreement with the Gassmann dip but with a
frequency-dependent magnitude. Which model applies must be established by
measurement; what can be stated unconditionally is that $v_s$ decreases as fluid
is added, whatever the distribution.

## 4. Physical interpretation

**$K$ is the resistance to volume change; $\mu$ is the resistance to shape
change.** Everything else is algebra. A fluid has $\mu = 0$ and $K$ finite; a
solid has both; and the ratio $K/\mu$ (equivalently $\nu$) says whether the
material prefers to change volume or shape, which is why it correlates with
porosity, fluid content and temperature in rocks.

**Poisson's ratio is a derived number, and it is bounded.** $\nu > -1$ from
$\mu > 0$; $\nu < 1/2$ from $K > 0$. A measured $\nu$ outside that range means the
measurement is wrong or the material is not elastic (a negative $\nu$ near $-1$
is possible in principle for auxetic engineered materials).

**Dynamic moduli exceed static ones in most rocks.** A laboratory static test
(loading over seconds to hours) allows time-dependent deformation — microcrack
sliding, pore-pressure diffusion — that an ultrasonic measurement (microseconds)
does not. The ratio of dynamic to static modulus is commonly of order 1.1 to 3 in
fractured or high-porosity rock, and much closer to 1 in tight crystalline rock.
These are order-of-magnitude statements from the literature; the value must be
measured for the rock and the conditions at hand.

**Fluid substitution is a thought experiment with a clear geometry.** It answers:
"if I replaced the pore fluid of this rock, holding the frame fixed, what would
the moduli become?" The frame is held fixed by assumption, which is why Gassmann
is a statement about fluids and not about rocks.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Isotropic, homogeneous | Two elastic constants describe the rock | Anisotropy (lesson 02-04-06); heterogeneity at the measurement scale |
| Linear elastic | Moduli independent of strain | Nonlinearity at strains above $\sim10^{-6}$ in soils |
| Low frequency (for Gassmann) | Pore pressure equilibrated each cycle | Patchy saturation and squirt flow; use a frequency-dependent model |
| Homogeneous pore fluid | Single fluid modulus | Mixed fluids with patchy geometry; use the two end members |
| Frame unchanged | No chemical or mechanical alteration | Clay swelling, dissolution, compaction with production |
| No stress dependence | Moduli independent of the stress state | Cracked rock: moduli rise strongly with confining pressure |
| Dynamic = static | Not assumed here; the two usually differ | Static measurements are lower; the difference must be calibrated |

## 6. Units and dimensional analysis

- All of $E$, $K$, $\mu$, $M$, $\lambda$: Pa ✓; $\nu$ dimensionless ✓.
- $[(1+\nu)(1-2\nu)]$ dimensionless, so $\lambda = E\nu/[(1+\nu)(1-2\nu)]$ has
  the units of $E$ ✓ — and it is worth checking the sign: for $\nu > 0$ and
  $\nu < 1/2$ all three factors are positive, so $\lambda > 0$ ✓.
- $v_p = \sqrt{M/\rho}$: $\mathrm{Pa/(kg\,m^{-3})} = \mathrm{m^2\,s^{-2}}$ ✓.
- Equation (13): every term inside the bracket has units of 1/Pa, so the ratio is
  Pa ✓, and $K_{\text{sat}}$ is a modulus.
- **A useful numerical anchor**: for a typical crustal rock,
  $\rho \approx 2700$ kg m⁻³, $v_p \approx 6000$ m s⁻¹ and $v_s \approx 3500$
  m s⁻¹ give $M \approx 97$ GPa, $\mu \approx 33$ GPa, $K \approx 53$ GPa,
  $E \approx 87$ GPa and $\nu \approx 0.25$ — all consistent with the equations of
  §3.1, which is the check to perform on any set of quoted values.

## 7. Python demonstration

[`code/elastic_moduli_demo.py`](./code/elastic_moduli_demo.py) computes every
constant for a granite-like model and verifies the relations and the Gassmann
table. Observed output with $\rho = 2700$ kg m⁻³, $\lambda = 25$ GPa,
$\mu = 30$ GPa:

```text
E = mu (3 lambda + 2 mu)/(lambda + mu) = 73.636364 GPa
nu = lambda / (2 (lambda + mu))       = 0.227272727
K = lambda + 2 mu/3                   = 45.000000 GPa
M = lambda + 2 mu (= K + 4 mu/3)      = 85.000000 GPa
v_p = sqrt((lambda + 2 mu)/rho)       = 5610.836077 m/s
v_s = sqrt(mu/rho)                    = 3333.333333 m/s
v_p/v_s                               = 1.683250823

  Independent routes to the same numbers:
    E from 9 K G /(3K + G) = 73.636364 GPa
    nu from (3K - 2G)/(2(3K + G)) = 0.227272727
    v_p/v_s from sqrt(2(1 - nu)/(1 - 2 nu)) = 1.683250823
```

```text
    eps_11 = 1.358024691e-04  vs sigma_11/E = 1.358024691e-04
    eps_22 = -3.086419753e-05  vs -nu sigma_11/E = -3.086419753e-05
    implied axial-extension ratio -eps_22/eps_11 = 0.227272727 (Poisson's ratio)
```

```text
      nu   lambda/mu    v_p/v_s   sqrt(K/mu + 4/3)
   -0.90    -0.64286   1.164965           1.164965
   -0.50    -0.50000   1.224745           1.224745
    0.00     0.00000   1.414214           1.414214
    0.25     1.00000   1.732051           1.732051
    0.40     4.00000   2.449490           2.449490
    0.49    49.00000   7.141428           7.141428

  Two bounds, of different strength, must be kept apart:
   * stability alone (K > 0, mu > 0) gives v_p/v_s = sqrt(K/mu + 4/3)
     > 2/sqrt(3) = 1.154701, approached as nu -> -1.
   * if lambda >= 0, i.e. nu >= 0, then v_p/v_s >= sqrt(2) = 1.414214, with
     equality at nu = 0.
```

```text
   Sw  K_fl (GPa)      rho  K_sat (GPa)  v_p (m/s)  v_s (m/s)  v_p patchy
 0.00      0.0100   2120.2      10.0261  3319.2371  2171.7383   3319.2371
 0.50      0.0199   2220.1      10.0518  3245.5041  2122.3244   3378.1234
 1.00      2.2000   2320.0      14.9481  3491.4570  2076.1370   3491.4570
Gassmann v_p at Sw = 0 is 3319.2371 m/s and returns to that value
  at Sw = 0.9935; in between v_p is LOWER than dry.
the minimum of the Gassmann curve is 3201.9563 m/s
```

### What to observe

| Observation | Consequence |
|---|---|
| Every constant computed by two independent routes agrees exactly | The modulus algebra is internally consistent; the double route is the standard way to catch a transcription error |
| The uniaxial test reproduces $\varepsilon_{11} = \sigma/E$ and $\varepsilon_{22} = -\nu\sigma/E$ | $E$ and $\nu$ are defined by that test, so this is the definition checked rather than the algebra |
| $v_p/v_s = 1.6833$ at $\nu = 0.2273$, and $\sqrt3 = 1.7321$ at $\nu = 0.25$ | The $\sqrt3$ "Poisson solid" value is a special case, not a default |
| The ratio is 1.164965 at $\nu = -0.9$, above $2/\sqrt3$ but *below* $\sqrt2$ | The unconditional bound and the conditional one are different; quoting $\sqrt2$ as universal is wrong |
| $v_s$ falls monotonically with $S_w$ (2171.74 → 2076.14 m s⁻¹) | A fluid cannot support shear, so adding fluid lowers $v_s$ through density only — the one robust statement of fluid substitution |
| $v_p$ *dips* to 3201.96 m s⁻¹ and only exceeds the dry value at $S_w = 0.9935$ | The uniform-saturation Gassmann model does not predict a monotonic bright spot; a naive "water makes it faster" intuition is wrong for a gas sand |
| The patchy column exceeds Gassmann at every intermediate saturation | The fluid distribution, not just the saturation, controls the modulus — which is why the frequency and the patchiness must be established by measurement |

> **Breaking exercise.** Set $K_{\text{dry}} = 25$ GPa (a stiffer frame) and
> predict, before running, whether the Gassmann dip in $v_p$ persists and whether
> it deepens or shallows. Then explain the answer in terms of the numerator
> $(1-K_{\text{dry}}/K_{\min})^2$.

## 8. Common mistakes

1. **Quoting $v_p/v_s \ge \sqrt2$ as universal.** It requires $\lambda \ge 0$; the
   unconditional bound is $2/\sqrt3$.
2. **Using $K = E/(3(1-2\nu))$ with a $\nu$ close to 0.5 and not noticing the
   divergence.** Small errors in $\nu$ produce enormous errors in $K$ there; the
   condition number of the conversion is $K/(K-\ldots)$ and should be estimated.
3. **Treating $\lambda$ as a measured quantity.** It is a difference, $K-2\mu/3$,
   and is poorly constrained when $K$ and $\mu$ are comparable.
4. **Assuming fluid saturation raises $v_p$.** In a gas sand the uniform-
   saturation model predicts a dip (table above); and in the squirt regime the
   first few per cent of saturation can also lower $v_p$.
5. **Assuming saturation leaves $v_s$ alone.** $\mu$ is unchanged but $\rho$ rises,
   so $v_s$ falls — by 4.4 per cent in the table.
6. **Using a laboratory (static) modulus in a seismic computation without
   conversion.** Dynamic and static moduli differ, sometimes by a factor of two.
7. **Forgetting that $M$, not $K$, appears in $v_p$.** Substituting $K$ for $M$
   underestimates $v_p$ by the factor $\sqrt{M/K} = \sqrt{1+4\mu/(3K)}$, which is
   1.36 in the granite model — a 36 per cent error.
8. **Using a single $\rho$ for a saturated rock.** The density must include the
   fluid mass; using the mineral density overestimates $v$ by several per cent.

## 9. Real-world applications

- **Seismic interpretation and lithology discrimination.** $v_p/v_s$ is a
  standard lithology and fluid indicator; its value, its uncertainty and its
  conditional bounds must all be stated ([06-seismology](../../06-seismology/README.md)).
- **Time-lapse (4-D) seismic monitoring.** Production changes the fluid content
  and the effective stress; the resulting velocity changes are predicted by
  Gassmann plus stress-sensitivity relations, and the $v_s$ change is the more
  robust part of the signal.
- **Rock-physics templates.** Cross-plots of $v_p/v_s$ against impedance are built
  from the modulus relations of this lesson, and are the standard tool for
  interpreting seismic amplitudes in terms of porosity and saturation
  ([05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).
- **Laboratory-to-field upscaling.** Static and dynamic moduli, drained and
  undrained conditions, and the frequency dependence of the moduli must all be
  reconciled before a laboratory number can be compared with a log or a seismic
  velocity.
- **Geotechnical characterisation.** $E$ and $\nu$ from in-situ tests (pressuremeter,
  plate load) design foundations; the same two constants appear in the seismic
  response of the soil column, which is why geotechnical and geophysical
  measurements are routinely compared.
- **Concrete, ceramics and metals.** The same relations are used across materials
  science; the numerical ranges differ, the algebra does not.

## 10. Further reading

- **Mavko, G., Mukerji, T., & Dvorkin, J. *The Rock Physics Handbook* (Cambridge
  University Press).** The modulus relations, the dynamic/static distinction, and
  Gassmann and its extensions, with the original references. Level: advanced.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The elastic constants and the wave-speed relations from
  the seismological direction. Level: advanced.
- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (Blackwell).** The laboratory definitions of $E$ and $\nu$ and the
  measurement geometries. Level: advanced.
- **Bourbié, T., Coussy, O., & Zinszner, B. *Acoustics of Porous Media* (Gulf
  Publishing).** Poroelasticity and the fluid-substitution problem in full. Level:
  graduate.
- **Wang, Z. (ed.) *Seismic and Acoustic Velocities in Reservoir Rocks* (SEG
  Geophysics Reprint Series).** Laboratory measurements and the dynamic/static
  comparison; useful for calibrating the ranges quoted in §4. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics*
  (2nd ed., Cambridge University Press, 1990).** The applied constant tables and
  typical ranges. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [03 Constitutive Laws and Generalised Hooke's Law](./03-constitutive-laws.md)
  — where the constants come from.
- [05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md) —
  the derivation that uses $M$ and $\mu$, and the mastery checkpoint.
- [06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](./06-anisotropic-elasticity.md)
  — what happens when two constants become nine (or more).
- [07 Viscoelasticity, Creep and Anelastic Relaxation](./07-viscoelasticity.md) —
  the frequency dependence of the moduli.
- [05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)
  — where these parameters are measured for real rocks.
- [06-seismology](../../06-seismology/README.md) — $v_p/v_s$ as an
  interpretation tool.

Exercises:
[`exercises/04-elastic-moduli-exercises.md`](./exercises/04-elastic-moduli-exercises.md)
and
[`exercises/04-elastic-moduli-solutions.md`](./exercises/04-elastic-moduli-solutions.md).

## Self-assessment checklist

- [ ] I can define every isotropic constant by the measurement geometry that
      determines it. (Section 2)
- [ ] I can derive the relations among $\lambda$, $\mu$, $E$, $\nu$, $K$ and $M$
      and verify two independent routes. (Section 3.1)
- [ ] I can derive the exact bounds on $v_p/v_s$ and explain why $\sqrt2$ is
      conditional. (Section 3.2)
- [ ] I can state and prove $v_p > v_s$ for any stable isotropic solid.
      (Section 3.2)
- [ ] I can compute the sensitivity of the velocities to each input and rank them.
      (Section 3.3)
- [ ] I can apply Gassmann's relation and state its regime of validity.
      (Section 3.4)
- [ ] I can explain the robust and non-robust parts of the saturation response.
      (Sections 3.4, 4)
- [ ] I can explain why static and dynamic moduli differ and what the difference
      does to a velocity comparison. (Section 4)
