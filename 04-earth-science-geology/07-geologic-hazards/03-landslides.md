---
id: 04-07-03
title: "Landslides, Slope Stability and Geotechnical Geophysics"
level: advanced
prereqs: ["04-04-01", "04-01-05", "04-05-01"]
estimated_minutes: 75
tags: [landslides, slope-stability, pore-pressure, refraction, ground-penetrating-radar]
---

# Landslides, Slope Stability and Geotechnical Geophysics

A slope fails when the shear stress on a surface exceeds the shear strength
along it. That sentence is the whole of slope stability, and everything that
follows is bookkeeping about the two sides of the comparison: which surface,
how much water is on it, and how much strength is left after the ground has
already been shaken. The interest of the subject for a geophysicist is that
**both sides of the comparison depend on quantities a geophysical survey can
measure** — water content, layer geometry, and small-strain stiffness — while
the strength itself usually cannot be measured remotely at all.

That asymmetry is the honest core of this lesson. Geophysics does not measure
the factor of safety. It measures the geometry and the water, and it converts a
velocity into a stiffness through a square root, which is a lossy conversion.
What a survey delivers is an *input* to a stability calculation, and the value
of the survey is that the input was previously unknown over an entire hillside
rather than at three boreholes.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the infinite-slope factor of safety from the normal and shear
   stresses on a plane parallel to the surface, including the pore-pressure
   term.
2. **Compute** the pore-pressure ratio at failure and compare it with the
   fully-saturated value, and identify the slope angles that can and cannot fail
   by pore pressure alone.
3. **Derive** the critical (Newmark) acceleration of a slope, distinguish the
   exact expression from the small-slope approximation that is usually quoted,
   and state the direction of the approximation's error.
4. **Compute** a sliding-block displacement from a rectangular acceleration
   pulse, derive the closed form, and verify a numerical integrator against it.
5. **Derive** the depth of a refractor from an intercept time and state what the
   method can and cannot see.
6. **Compute** a water content from a GPR velocity by inverting a stated mixing
   model, and state the assumptions that make the inversion an inference.
7. **Explain** why the shear modulus is the quantity stability wants, why $v_S$
   is the quantity seismics measures, and what the square root between them
   costs.
8. **State** the conditions under which an infinite-slope analysis is
   applicable, and name the mechanisms it cannot represent.

## Prerequisites

- [04-04-01 Stress, Strain and Brittle vs Ductile Deformation](../04-structural-geology/01-stress-strain-rocks.md)
  — the stress tensor, normal and shear components, and the difference between
  brittle and ductile behaviour that decides whether the sliding-block
  idealisation is appropriate.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — porosity, saturation, and the elastic moduli that connect $v_S$ to $G$.
- [04-05-01 Landform Processes and Shapes](../05-geomorphology-and-quaternary/01-landforms.md)
  — the slope angles and materials that actually occur, which is what decides
  which of these models is relevant.

## 1. Classification, and why the mechanism matters

Landslides are classified by *material* and *mechanism*, and the mechanism
determines the velocity, which determines whether anything can be done about it.
A practical ordering, from slow to fast:

| Mechanism | Typical material | Order of velocity | Warning possible? |
|---|---|---|---|
| Creep | soil, rock | mm to cm per year | not needed |
| Deep-seated rotational slide | clay, weak rock | mm per day to m per hour | yes, with monitoring |
| Translational slide | soil over bedrock | m per hour | sometimes |
| Debris flow | saturated soil, ash | m per second | acoustic detection only |
| Rock avalanche | rock | tens of m per second | no |

The physical quantity that separates the rows is not the volume and not the
slope angle; it is the **degree of disaggregation**. A coherent block sliding on
a discrete surface is a solid-mechanics problem with a well-defined strength. A
debris flow is a granular-fluid problem with a rheology, and its runout is not
predicted by the strength of any surface.

## 2. Infinite-slope stability, derived

Take a slope of uniform angle $\beta$, uniform material of unit weight $\gamma$
and a potential slip surface parallel to the surface at vertical depth $z$. This
geometry — the *infinite slope* — is the only one with a closed-form answer, and
it is a good approximation for a shallow failure on a long, straight slope.

Resolve the weight of the column above unit area of the slip plane into
components normal and parallel to it. The weight per unit area of slip plane is
$\gamma z\cos\beta$, so

$$\sigma_n = \gamma z\cos^2\beta, \qquad
\tau = \gamma z\sin\beta\cos\beta . \tag{1}$$

The Mohr–Coulomb strength is $c' + (\sigma_n - u)\tan\phi'$, with $u$ the pore
pressure on the slip plane and primes denoting effective stress, so

$$FS = \frac{c' + \left(\gamma z\cos^2\beta - u\right)\tan\phi'}
{\gamma z\sin\beta\cos\beta} . \tag{2}$$

Three checks of (2) are worth doing, because they are what make it credible:

- **Dry, cohesionless.** $c' = 0$, $u = 0$: $FS = \tan\phi'/\tan\beta$, so
  failure occurs at $\beta = \phi'$ exactly. This is the textbook angle of
  repose, and it falls out of the algebra.
- **Saturated to the surface.** The pore pressure ratio
  $r_u = u/(\gamma z)$ is then $\gamma_w/\gamma \approx 9.81/18 = 0.545$ for a
  typical soil. With $c' = 0$ the factor of safety can be written in terms of
  the critical ratio (3):

$$FS = \frac{\cos^2\beta - r_u}{\cos^2\beta - r_u^\mathrm{crit}} . \tag{3a}$$

  For $\phi' = 32^\circ$ this is below 1 for every $\beta$ above about
  $14.6^\circ$: **a cohesionless slope steeper than about 15 degrees cannot
  stand saturated**, whatever its water content was when it was built. Note the
  form of (3a): it is *not* $r_u^\mathrm{crit}/r_u$, because the pore pressure
  also appears in the definition of $r_u^\mathrm{crit}$ itself. At
  $\beta = 20^\circ$ and $\phi' = 32^\circ$, a head of 1 m in the 3 m column
  gives $FS = 1.36$ and a head of 2 m gives $FS = 1.01$.
- **Critical pore pressure.** Setting $FS = 1$ and solving for $u$ gives the
  pore pressure that would just cause failure, and hence a *monitoring
  threshold*: a piezometer reading above it is the actionable signal. With
  $c' = 0$ the result simplifies neatly:

$$r_u^\mathrm{crit} = \cos^2\beta\left(1 - \frac{\tan\beta}{\tan\phi'}\right). \tag{3}$$

For $\beta = 20^\circ$ and $\phi' = 32^\circ$, $r_u^\mathrm{crit} = 0.369$
against a saturated 0.545, so the slope is stable dry and fails wet. For
$\beta = 10^\circ$, $r_u^\mathrm{crit} = 0.696$, above saturation, so it cannot
fail by pore pressure alone in this model. **The difference between a slope that
fails when it rains and one that does not is mainly the slope angle against the
friction angle, and both are measurable.**

## 3. Earthquake triggering: critical acceleration and sliding block

Add a horizontal pseudo-static acceleration $k_h g$ to (1). The inertial force
contributes $k_hW\cos\beta$ to the driving shear and *reduces* the normal force
by $k_hW\sin\beta$, so with $c' = 0$ and no pore pressure,

$$FS = \frac{(\cos\beta - k_h\sin\beta)\tan\phi'}{\sin\beta + k_h\cos\beta} . \tag{4}$$

Setting $FS = 1$ and eliminating $\phi'$ in favour of the static factor of
safety $FS_0 = \tan\phi'/\tan\beta$ gives

$$k_h = \tan\beta\,\frac{FS_0 - 1}{1 + FS_0\tan^2\beta} , \tag{5}$$

and the **critical acceleration** is $a_c = k_h g$. The small-slope
approximation that is usually quoted,

$$k_h^\mathrm{approx} = (FS_0 - 1)\tan\beta , \tag{6}$$

drops the $FS_0\tan^2\beta$ term in the denominator. It is **high** by 6 per
cent at $\beta = 5^\circ$, 23 per cent at $20^\circ$ and 29 per cent at
$25^\circ$. Since an overestimate of $a_c$ is an underestimate of the
displacement, the approximation is non-conservative for a hazard estimate, and
on a steep slope it is worth the extra line of algebra.

**Displacement.** Newmark's insight was that the sliding mass is not a static
problem but an integral one: when the ground acceleration exceeds $a_c$ the mass
starts to slide, and it stops when the relative velocity returns to zero. For a
rectangular pulse of amplitude $a$ and duration $t_0$, integrating
$\ddot s = a - a_c$ during the pulse and $-a_c$ after it gives

$$d = \frac{a\,t_0^2\,(a - a_c)}{2\,a_c} . \tag{7}$$

The displacement is **quadratic** in the excess acceleration and in the pulse
duration. This is the single most consequential fact in earthquake-triggered
landslide assessment: a factor of 2 in the excess $(a - a_c)$ is a factor of 4 in
the displacement, and a slope that is marginally stable ($a_c$ close to $a$) is
enormously more sensitive to a change in $a_c$ than a slope with a large margin.

## 4. What geophysics contributes

### 4.1 Water, from a velocity

Water is the controlling variable and it is the one a geophysical survey
measures best. The chain is permittivity to water content, and the standard
mixing model — the **Complex Refractive Index Model** — is *assumed*, not
derived:

$$\sqrt{\varepsilon_r} = \theta\sqrt{\varepsilon_w}
+ (1-\phi)\sqrt{\varepsilon_s} + (\phi - \theta)\sqrt{\varepsilon_a} , \tag{8}$$

with $\theta$ the volumetric water content, $\phi$ the porosity, and
$\varepsilon_w = 80.4$, $\varepsilon_a = 1$ and $\varepsilon_s \approx 5$ as
tabulated values. The velocity follows from the same relation that governs all
low-loss dielectrics, $v = c/\sqrt{\varepsilon_r}$. For $\phi = 0.35$, going
from $\theta = 0.05$ to $0.30$ takes $v$ from 0.136 to 0.072 m ns⁻¹ — nearly a
factor of 2 — and the slope of the inverse relation is
$\mathrm{d}\theta/\mathrm{d}v \approx 3.87$ per m ns⁻¹, so a velocity measured to
0.001 m ns⁻¹ fixes the water content to about 0.004. That is the quantitative
case for GPR as a moisture instrument, and it is conditional on (8) being the
right model for the soil.

The same water is what electrical resistivity measures, with a much weaker and
more empirical relation to water content and a much larger sensitivity to pore
water conductivity — but with a penetration depth GPR cannot reach in a
conductive clay. The two methods are complementary for the same reason they
differ: GPR responds to the dielectric polarisability of water, resistivity to
its ionic conductivity.

### 4.2 The failure surface, from a travel time

The two-layer refraction problem gives the depth to a refractor from the
intercept time $t_i$ of the head-wave branch:

$$z = \frac{t_i\,v_1 v_2}{2\sqrt{v_2^2 - v_1^2}} , \tag{9}$$

which follows from Snell's law at the critical angle. For $v_1 = 600$ m s⁻¹,
$v_2 = 2200$ m s⁻¹ and $t_i = 12.5$ ms, $z = 3.90$ m. The failure surface of a
translational slide is often exactly this kind of boundary, and the depth comes
out with an uncertainty dominated by the two velocities, which enter
multiplicatively.

The limitation is the **hidden layer**. Equation (9) is only valid if the
refractor is faster than everything above it. A saturated clay layer is
*slower* than the dry or partly saturated soil above it and slower than the
bedrock below, and no first arrival ever samples it: the head wave travels
through the layer above and then through the bedrock beneath. Inverting the
observed travel times with (9) then places the bedrock at an apparent depth that
is **much too large**. Worked through in the exercises, a 3 m layer of
500 m s⁻¹ over a 5 m layer of 300 m s⁻¹ over bedrock at 8 m is inverted as
bedrock at **11.9 m** — a 49 per cent overestimate — and the weak layer, which
is the one that matters, is invisible.

### 4.3 Stiffness, and the square root that costs

The stability calculation wants a *strength*. Seismics measures a velocity.
They are connected by

$$v_S = \sqrt{G/\rho} \quad\Longrightarrow\quad G = \rho v_S^2 , \tag{10}$$

so a 20 per cent velocity error is a 44 per cent modulus error. Worse, the
modulus that (10) measures is the **small-strain** modulus $G_\mathrm{max}$,
while the relevant modulus during failure is the one at the strain level the
slope actually experiences. Soils soften: a hyperbolic model
$G/G_\mathrm{max} = 1/(1 + \gamma/\gamma_r)$ with $\gamma_r$ a measured
reference strain gives $G/G_\mathrm{max} = 0.5$ at $\gamma = \gamma_r$, which is
$v_S/v_{S,\max} = 0.707$. **A halving of the modulus is a 29 per cent fall in
$v_S$**, and because a site's fundamental frequency is $f_0 = v_S/(4H)$, a
halving of the modulus also lowers the resonant frequency by 29 per cent.

This is why a velocity change during a wet season is a *weaker* signal than the
stiffness change it reflects, and why $v_S$ alone is a weak constraint on
stability: the quantity the survey measures is the square root of the quantity
the mechanics wants, and the conversion factor is a small-strain assumption.

## 5. Physical interpretation

- The factor of safety compares a strength with a stress **on a specific
  plane**. Change the plane and you change both sides; that is why a
  geophysical survey's contribution is mostly *geometric*.
- Pore pressure enters the numerator only, as a subtraction from the normal
  stress. It does not affect the driving shear at all. So the entire effect of
  water is to make the material weaker, never to push it harder down the slope.
- The pore-pressure ratio at failure, (3), is a measurable threshold and the
  most useful single number in a slope-monitoring programme.
- The displacement is quadratic in the excess acceleration, so the slopes worth
  instrumenting are the marginally stable ones, not the obviously weak ones that
  have already failed.
- **A velocity is not a strength.** Every conversion in §4.3 loses information,
  and no amount of survey precision recovers it.

## 6. Units and dimensional analysis

| Quantity | Expression | Units |
|---|---|---|
| Normal stress on the slip plane | $\gamma z\cos^2\beta$ | N m⁻³ × m = Pa |
| Shear stress | $\gamma z\sin\beta\cos\beta$ | Pa |
| Factor of safety | stress ratio | dimensionless |
| Pore-pressure ratio | $u/(\gamma z)$ | dimensionless |
| Critical acceleration | $k_h g$ | dimensionless × m s⁻² = m s⁻² |
| Sliding displacement | $a t^2(a-a_c)/(2a_c)$ | (m s⁻²)(s²) = m |
| Refractor depth | $t_i v_1v_2/\sqrt{v_2^2-v_1^2}$ | s × m s⁻¹ = m |
| Dielectric velocity | $c/\sqrt{\varepsilon_r}$ | m s⁻¹ |
| Shear modulus from $v_S$ | $\rho v_S^2$ | kg m⁻³ × m² s⁻² = Pa |

The factor of safety is dimensionless and therefore *portable*: it is the same
number whether you work in Pa or kPa, which is why unit errors in a stability
calculation almost always appear as a $10^3$ in $c'$ rather than as a
wrong-looking $FS$.

## 7. Assumptions and regime of validity

1. **A single planar slip surface parallel to the surface** in §2. Real failures
   have curved (rotational) surfaces, and the infinite-slope idealisation
   applies to shallow translational slides on long slopes. A deep rotational
   slide needs a method of slices.
2. **Rigid-perfectly-plastic Mohr–Coulomb strength** in (2). This ignores
   strain softening, which makes a progressive failure possible at a stress
   below the peak strength, and rate effects, which make a fast slide weaker.
3. **Pore pressure specified, not computed** in §2. In reality $u$ is a
   transient result of rainfall infiltration and groundwater flow, so a
   stability calculation is coupled to a hydrological one.
4. **Pseudo-static analysis** in §3 and §4. The pseudo-static factor of safety
   is not a dynamic analysis; it is a screening tool, and Newmark displacement
   is the standard refinement.
5. **Rigid sliding block** in (7). There is no internal deformation, no
   degradation of strength during sliding, and no pore-pressure generation
   within the sliding mass.
6. **Two-layer, flat, faster-refractor** in (9). A hidden low-velocity layer
   invalidates the depth, and a dipping interface invalidates the assumption
   that the refractor velocity is the measured apparent velocity.
7. **CRIM** in (8). It is one of several mixing models; Topp-type empirical fits
   are used instead in many soils, and all of them fail on a soil with a
   significant clay fraction or a large organic content.
8. **Small-strain elasticity** in (10). Above roughly $10^{-4}$ shear strain the
   modulus is strain-dependent and the conversion from $v_S$ is no longer valid.

## 8. Python demonstration

[`code/landslides_demo.py`](./code/landslides_demo.py) derives every quantity in
this lesson from the printed inputs and verifies two of them: the sliding-block
integrator against the closed form (7), and the CRIM inversion against the
forward model. Every soil parameter is labelled NOMINAL.

The factor of safety and the pore-pressure threshold:

```text
     beta (deg)   FS (r_u = 0.5450)   r_u at FS = 1
        10.0            1.5524         0.6962
        15.0            0.9698         0.5329
        20.0            0.6572         0.3687
        25.0            0.4509         0.2084
        30.0            0.2958         0.0570
```

The critical-acceleration comparison:

```text
     beta (deg)   FS0     k_h exact   k_h approx   ratio
         5.0    7.142       0.5095       0.5374     0.9482
        15.0    2.332       0.3057       0.3569     0.8566
        25.0    1.340       0.1228       0.1586     0.7744
```

And the integrator check, where the analytic result (7) is the reference:

```text
    t0 (s)   numeric d (m)   closed form (m)   rel. diff
      0.10         0.010000          0.010000   2.86e-14
      0.20         0.040000          0.040000   7.55e-14
      0.50         0.250000          0.250000   5.14e-13
      1.00         1.000000          1.000000   6.50e-13
```

### What to observe

- The pore-pressure table contains the whole monitoring strategy of a slope: a
  1 m rise of head in a 3 m soil column changes $r_u$ by
  $\gamma_w/(\gamma z) = 0.18$, and at $\beta = 20^\circ$ that is the
  difference between $FS = 1.36$ (1 m of head) and $FS = 1.01$ (2 m of head).
  The margin is gone before the slope looks wet.
- At 15 degrees the critical $r_u$ is 0.533, just below the fully saturated
  0.545: this slope fails when saturated and only then, and the threshold in
  slope angle is $14.6^\circ$. That is why the *first* big storm after a dry
  spell is often the trigger — it is the moment when the pore pressure crosses a
  threshold that a marginally steeper slope never descends from.
- The integrator agrees with (7) to 6 parts in 10¹³. That agreement is what
  licenses the use of the same integrator on a real acceleration record, where
  the answer is not known in advance.
- The refraction table shows $z$ varying only slightly across refractor
  velocities from 1800 to 3000 m s⁻¹, because for $v_2 \gg v_1$ the expression
  approaches $z \approx t_i v_1/2$. The depth is controlled by the *shallow*
  velocity and the intercept time, and the deeper velocity contributes weakly —
  which is precisely why a wrong $v_1$ is the dominant error.

## 9. Common mistakes

1. **Using the total stress in the strength term.** The Mohr–Coulomb criterion
   is written in effective stress; omitting $u$ is the classic error and it is
   always unsafe.
2. **Treating the pore-pressure ratio as a constant.** It is a ratio of a
   transient to a static quantity, and $z$ in the denominator means a deep slip
   surface needs a higher absolute pressure to reach the same $r_u$.
3. **Applying the small-slope $k_h$ approximation on a steep slope.** It is high
   by 23 per cent at 20 degrees, and the error is non-conservative.
4. **Quoting a Newmark displacement from a single $a_c$.** The sensitivity to
   $a_c$ grows without bound as $a_c \to a$; the answer is a distribution.
5. **Inverting refraction travel times for the depth of a low-velocity layer.**
   First arrivals cannot see one, and the inversion will produce a plausible and
   badly wrong depth.
6. **Treating $v_S$ as a strength.** It is the small-strain stiffness, and the
   square root and the strain dependence both intervene.
7. **Using CRIM on a clay-rich soil.** The mixing model and the empirical
   alternatives both break down; the survey result becomes a relative indicator,
   not a water content.
8. **Ignoring the direction of slope in an airborne or satellite survey.** A
   slope-parallel 3-D geometry is needed to resolve both the failure surface and
   its dip.
9. **Forgetting that a landslide deposit is a *material*, not a surface.** The
   remobilised material has different permeability, porosity and strength from
   the intact slope.
10. **Reporting a factor of safety without its pore pressure.** $FS$ is a
    function of $u$, so a single number is a statement about one water level.

## 10. Real-world applications

- **Landslide early warning.** Piezometers and inclinometers in boreholes,
  supported by a displacement time series from GNSS or InSAR, with the trigger
  threshold from (3).
- **Earthquake-triggered landslide hazard maps.** Newmark displacement with the
  ratio $a_c/a_\mathrm{max}$ as the mapping variable, which is the standard
  practice in regional assessments
  ([06-11 Earthquake Statistics and Hazard](../../06-seismology/11-earthquake-statistics-and-hazard/README.md)).
- **Slope stability in open-pit mining.** The same mechanics at a much larger
  scale, with a monitoring regime driven by the cost of a failure.
- **Railway and road cut assessment.** Refraction and MASW lines along the
  cut, converted to a layer model, then to a stability calculation.
- **Reservoir-induced seismicity and slope failure.** Rapid drawdown changes the
  pore pressure on a timescale set by the reservoir operation, not the weather.
- **Volcanic flank collapse.** Hydrothermal alteration produces clay, and clay
  produces a low-velocity, weak layer, which is the same hidden-layer problem
  ([04-07-02 Volcanic Hazards, Monitoring and Precursors](./02-volcanic-hazards.md)).

## 11. Further reading

- **Terzaghi, K. *Theoretical Soil Mechanics* (Wiley).** The origin of the
  effective-stress principle that (2) is built on. Level: advanced, historical.
- **Newmark, N. M. (1965). "Effects of earthquakes on dams and
  embankments." *Géotechnique*.** The paper that introduced the sliding-block
  displacement; worth reading for how a simple idealisation became a standard
  engineering tool. Level: advanced.
- **Kramer, S. L. *Geotechnical Earthquake Engineering* (Prentice Hall).** The
  standard text for §3 and §4.1, including the modulus-reduction curves that
  §4.3 summarises. Level: graduate.
- **Topp, G. C., Davis, J. L., & Annan, A. P. (1980). "Electromagnetic
  determination of soil water content." *Water Resources Research*.** The
  empirical alternative to CRIM in (8), and a model of how a calibration is
  published with its soil range. Level: advanced.
- **Turner, A. K., & Schuster, R. L. (eds), *Landslides: Investigation and
  Mitigation* (Transportation Research Board).** The reference handbook for
  practice: classification, investigation methods and case histories. Level:
  professional.
- **USGS Landslide Hazards Program, reached from <https://www.usgs.gov>.** The
  authoritative public source for landslide inventories, monitoring practice and
  terminology; the main site blocks automated requests and is intended for a
  browser. Level: reference.
- **Copernicus and ESA Earth-observation data at <https://www.esa.int> and
  <https://dataspace.copernicus.eu/>.** The InSAR and optical data used in
  regional landslide inventory work. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04-07-01 Earthquake Hazard and Ground Motion](./01-earthquake-hazard.md) —
  the ground motion that drives the sliding block.
- [04-07-04 Subsidence, Sinkholes and Karst](./04-subsidence-sinkholes.md) —
  the same effective-stress mechanics applied to a different failure mode.
- [04-04-01 Stress, Strain and Brittle vs Ductile Deformation](../04-structural-geology/01-stress-strain-rocks.md)
  and [04-04-04 Fractures, Joints and Their Geophysical Signature](../04-structural-geology/04-fractures-joints.md)
  — the mechanics and the discontinuity sets that decide where the slip plane
  is.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md)
  — the full treatment of the method whose two-layer result is used in §4.2.
- [14-02 Hydrogeophysical Methods](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/README.md)
  — resistivity, GPR and their joint use for water content.
- [05-04 Rock Physics and Property Relations](../../05-core-geophysics/04-rock-physics/README.md)
  — the empirical relations between porosity, saturation and elastic moduli.

Exercises:
[`exercises/03-landslides-exercises.md`](./exercises/03-landslides-exercises.md)
and
[`exercises/03-landslides-solutions.md`](./exercises/03-landslides-solutions.md).

## Self-assessment checklist

- [ ] I can derive (2) from the normal and shear stresses on a slope-parallel
      plane. (§2)
- [ ] I can show that a dry cohesionless slope fails at $\beta = \phi'$. (§2)
- [ ] I can compute the critical pore-pressure ratio and compare it with the
      saturated value. (§2)
- [ ] I can derive the exact critical acceleration and state the error of the
      small-slope approximation. (§3)
- [ ] I can compute a sliding-block displacement and state its quadratic
      sensitivity to the excess acceleration. (§3)
- [ ] I can invert an intercept time for a refractor depth and explain the
      hidden-layer failure. (§4.2)
- [ ] I can convert a velocity to a water content and state the model I assumed.
      (§4.1)
- [ ] I can convert $v_S$ to $G$ and explain what the square root costs.
      (§4.3)
- [ ] I can name three mechanisms an infinite-slope analysis cannot represent.
      (§7)
- [ ] I can state the one geophysical measurement I would make first on a
      suspected slide, and why.
