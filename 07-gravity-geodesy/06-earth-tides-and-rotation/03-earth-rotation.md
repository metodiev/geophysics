---
id: 07-06-03
title: "Earth Rotation, Polar Motion, LOD and Excitation"
level: doctoral
prereqs: ["07-06-01", "02-02-08", "02-02-05"]
tags: [gravity, geodesy, earth-rotation, polar-motion, angular-momentum]
---

# Earth Rotation, Polar Motion, LOD and Excitation

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the angular-momentum budget for the rotating Earth and **derive**
   the length-of-day relation $\Delta\mathrm{LOD}/\mathrm{LOD} =
   \Delta H_3/(C\Omega)$ for the non-solid part.
2. **Compute** the axial angular momentum of a zonal wind field from first
   principles, and **verify** the $C$-factor $(2/3)M\Omega R^{2}$ for solid-body
   rotation by quadrature.
3. **Derive** the rigid-body Euler wobble frequency $\sigma_c = \Omega(C-A)/A$ and
   **measure** the free-wobble period by numerically integrating the linearised
   wobble equations.
4. **Compute** the forced wobble response $1/(1-\sigma/\sigma_c)$ and explain why
   a forcing's *spectrum* rather than its amplitude decides the polar motion.
5. **Define** the excitation function $\chi$ for a mass redistribution and
   **convert** it into a pole displacement in milliarcseconds.
6. **State** which physical effects the rigid-body treatment omits, and in which
   direction each of them moves the predicted period and amplitude.
7. **Explain** why Earth-orientation parameters are a *product* of a geodetic
   measurement and a set of models, and how that affects their use in a reference
   frame.

## Prerequisites

- [01 Solid Earth Tides and Their Gravity Signature](01-solid-earth-tides.md) —
  the tidal potential, which is one of the torques acting on the rotation.
- [02-02-05 Rotation](../../02-physics/02-classical-mechanics/05-rotation.md) —
  angular momentum, moments of inertia and the inertia tensor.
- [02-02-08 Rigid-Body Dynamics](../../02-physics/02-classical-mechanics/08-rigid-body.md) —
  Euler's equations for a rotating body.

> **All models and data in this module are SYNTHETIC.** The Earth model is a
> two-layer sphere without ellipticity; the winds, mass redistributions and
> damping are chosen teaching values. No observed rotation parameter is quoted.

## 1. The budget: one equation that runs the whole subject

The Earth's total angular momentum is conserved, so any change in the angular
momentum of the atmosphere, oceans, ice or the fluid core must appear as an equal
and opposite change in the angular momentum of the solid Earth:

$$\Delta \mathbf{H}_{\text{solid}} + \Delta\mathbf{H}_{\text{other}} = 0 .$$

Two observables follow, and they are different projections of the same vector
equation:

- **Length of day** is the axial component ($z$). A change $\Delta H_3$ in the
  non-solid part changes the rotation rate $\Omega$ through
  $H_{\text{solid}} = C\Omega$:
  $$\boxed{\;\frac{\Delta \mathrm{LOD}}{\mathrm{LOD}} =
  \frac{\Delta H_3}{C\Omega}\;}$$
  with the sign convention that the atmosphere gaining *westerly* momentum
  lengthens the day. The demonstration checks the signs: its synthetic
  $30\ \mathrm{m\,s^{-1}}$ zonal wind carries
  $H_3 = +5.798\times10^{26}\ \mathrm{kg\,m^{2}\,s^{-1}}$ and lengthens the day by
  $+8.15\ \mathrm{ms}$.
- **Polar motion** is the equatorial component: the rotation axis wanders
  relative to the body because the body's inertia tensor is not perfectly
  aligned with the rotation vector.

*Worked example 1 (how much momentum is 1 ms?).* With the demonstration's
$C = 8.4022\times10^{37}\ \mathrm{kg\,m^{2}}$ and
$\Omega = 7.2921150\times10^{-5}\ \mathrm{rad\,s^{-1}}$,

$$\Delta H_3 = C\,\Omega\,\frac{\Delta \mathrm{LOD}}{\mathrm{LOD}}
= (8.4022\times10^{37})(7.2921150\times10^{-5})
\frac{10^{-3}}{86164} = 7.11\times10^{25}\ \mathrm{kg\,m^{2}\,s^{-1}} .$$

That is $12\%$ of the demonstration's synthetic wind momentum — so realistic
levels of atmospheric angular momentum move the day by a millisecond, and a
millisecond is easily measured by modern techniques. **This is why LOD is a
usable window on the general circulation**, and why nothing about the solid Earth
can be inferred from LOD until the atmosphere's momentum has been removed.

## 2. The axial angular momentum of a wind field

The $z$-component of the angular momentum of a velocity field $\mathbf{u}$ in a
thin shell of surface density $\sigma$ is

$$H_3 = \int \sigma\,u_\phi\,r\sin\theta\;\mathrm{d}A ,$$

where the moment arm $r\sin\theta$ appears **once**, because it came from
$\mathbf{r}\times(\sigma\mathbf{u})$. A common error is to include it twice,
which inflates the result by a factor $R$ — in the demonstration's check, a
factor $6.4\times10^{6}$.

*Worked example 2 (the $(2/3)$ factor, verified).* For solid-body rotation
$u_\phi = \Omega R\sin\theta$ and a thin shell of mass $M$:

$$H_3 = \frac{M}{4\pi R^{2}}R^{2}\Omega R^{2}\!\!\int_0^{2\pi}\!\!\mathrm{d}\phi
\int_0^{\pi}\!\sin^{3}\theta\,\mathrm{d}\theta
= M\Omega R^{2}\frac{2\pi(4/3)}{4\pi} = \frac{2}{3}M\Omega R^{2}.$$

The demonstration evaluates the same integral by quadrature and matches the
analytic value to $2.2\times10^{-16}$ relative — the check is exact, not
indicative. Note which mass is used: the *atmosphere's* ($5.15\times10^{18}\
\mathrm{kg}$), not the Earth's; using the Earth's would inflate the wind
momentum by $1.16\times10^{6}$.

## 3. Polar motion: the free wobble

For a rigid body with principal moments $A = B$ (equatorial) and $C$ (axial),
Euler's equations linearise, for small wobble $\mathbf{m}$ of the rotation axis
relative to the body, to

$$\frac{\mathrm{d}\mathbf{m}}{\mathrm{d}t} + i\,\sigma_c\,\mathbf{m}
= i\,\sigma_c\,\boldsymbol{\chi}(t),
\qquad
\sigma_c = \Omega\,\frac{C-A}{A} ,$$

where $\boldsymbol{\chi}$ is the *excitation function* (the same equation in
complex form for the two equatorial components) and
$H = (C-A)/A$ is the **dynamical ellipticity**.

*Worked example 3 (the rigid period).* With the stated synthetic
$H = 0.00327$,

$$\sigma_c = (7.2921150\times10^{-5})(0.00327) = 2.384522\times10^{-7}\
\mathrm{rad\,s^{-1}}
\;\Longrightarrow\;
T = \frac{2\pi}{\sigma_c} = 2.6350\times10^{7}\ \mathrm{s} = 304.98\ \mathrm{d}.$$

The demonstration integrates the wobble equation numerically with a step
excitation and measures the free period from the maxima of $\mathrm{Im}(m)$:
$304.9687\ \mathrm{d}$ against the analytic $304.9754\ \mathrm{d}$, an agreement
of $2.2\times10^{-5}$ limited by the sampling grid — and it verifies the whole
numerical solution against the analytic
$m(t) = \chi\,(1-e^{-i\sigma_ct})$ to $3.5\times10^{-11}$ relative.

**The real Earth's wobble period is longer than this rigid value** because the
Earth is elastic and carries oceans; the lengthening is an Earth-model result
that this model does not contain, so the lesson reports only the rigid value and
labels the omission. Honest practice in this subject is to say which of the
three numbers — rigid, elastic, elastic-plus-ocean — is being quoted, because
they differ by tens of per cent.

## 4. Forced wobble, and why the spectrum matters

For a periodic excitation $\chi = \chi_0e^{i\sigma t}$ the steady solution is

$$\mathbf{m} = \frac{\boldsymbol{\chi}_0}{1-\sigma/\sigma_c} ,$$

so the response is amplified **near the free frequency**, whatever the size of
the forcing. The demonstration's table: amplification $6.06$ for an annual
($365.25\ \mathrm{d}$) forcing, $60.30$ for a $300\ \mathrm{d}$ forcing, and
$0.97$ for a $150\ \mathrm{d}$ forcing — all from the same amplitude.

Two consequences that recur throughout geodesy:

1. **A resonance is a spectral filter.** An excitation whose spectrum has power
   near $\sigma_c$ produces a large wobble even if its total amplitude is modest,
   and the same forcing at a different frequency produces almost nothing.
2. **The free wobble must be damped, or it would be enormous.** The real Chandler
   wobble decays with a time constant of decades, which requires anelasticity or
   ocean dissipation. In a rigid, undamped model a step excitation wobbles
   forever at constant amplitude; the demonstration's model shows exactly that,
   and the absence of damping is the largest physics omission in this lesson.

## 5. Excitation: from a mass redistribution to a pole displacement

Rotation is also excited by *mass* redistribution, not only by momentum. A change
in the inertia tensor changes the body's principal axes, so the same rotation
vector appears as a different wobble. To leading order the excitation is

$$\boldsymbol{\chi} \approx \frac{\Delta I_{xz} - i\Delta I_{yz}}{C} ,$$

i.e. the change in the off-diagonal (product-of-inertia) components, divided by
the axial moment.

*Worked example 4.* A synthetic redistribution of $10^{-8}$ of the Earth's mass
across a radius $R$ changes the products of inertia by
$\Delta I = 10^{-8}MR^{2} = 2.4241\times10^{30}\ \mathrm{kg\,m^{2}}$, so

$$\chi = \frac{2.4241\times10^{30}}{8.4022\times10^{37}} = 2.8851\times10^{-8}
\;\Longrightarrow\;
|\mathbf{m}| = 2.8851\times10^{-8}\ \mathrm{rad}.$$

Converting: $1\ \mathrm{rad} = 206264.8$ arcsec, so
$m = 2.8851\times10^{-8}\times206264.8\times10^{3} = 5.95\ \mathrm{mas}$.

**A pole displacement of a few milliarcseconds corresponds to a mass
redistribution of $10^{-8}$ of the Earth's mass.** That is why polar motion is a
sensitive probe of climate-scale mass transport — and why the excitation budget
must account for the atmosphere, the oceans, the terrestrial water and the
cryosphere before any residual can be attributed to the solid Earth.

## 6. Assumptions and regime of validity

1. **Rigid body.** No elastic or ocean compliance; the real wobble period is
   longer than the rigid one by an *Earth-model* factor that this treatment
   cannot supply.
2. **No damping.** The free wobble does not decay here. Real damping (decadal)
   comes from anelasticity in the mantle and dissipation in the oceans.
3. **Axisymmetric body, $A = B$.** Triaxiality introduces a second free mode and
   couples the wobble to the diurnal band.
4. **Linearised.** Products of the wobble components and of the excitation are
   dropped; for the real Earth ($m \sim 10^{-7}$) this is excellent.
5. **The fluid core is not modelled.** The core's rotation lags the mantle and
   alters the effective moments; this is the largest *structural* omission.
6. **The equation of motion is decoupled from the gravity field.** The centrifugal
   change due to the wobble also changes the inertia tensor (the centrifugal
   feedback), which shifts the free period further.
7. **Observations are frame-dependent.** A pole position is defined relative to a
   reference frame and to models of the tides and the atmosphere; the numbers are
   products of measurement and convention (see
   [07-04-05](../04-geodesy-reference-frames/05-itrf-and-plate-models.md)).

## 7. Python demonstration

`code/earth_rotation_demo.py` prints, with units:

1. **A two-layer Earth model**: mantle density solved from the mass
   ($4464.6\ \mathrm{kg\,m^{-3}}$), $C = A = 8.4022\times10^{37}\ \mathrm{kg\,m^{2}}$
   and $C/(MR^{2}) = 0.34661$ — overestimating the real ratio because the model
   has neither ellipticity nor a mantle density gradient.
2. **The wind momentum**: the $(2/3)M\Omega R^{2}$ check to $2.2\times10^{-16}$,
   the warning that using the Earth's mass inflates it by $1.16\times10^{6}$, and
   a synthetic $30\ \mathrm{m\,s^{-1}}$ zonal wind with
   $H_3 = 5.798\times10^{26}\ \mathrm{kg\,m^{2}\,s^{-1}}$.
3. **LOD**: $+8.154\ \mathrm{ms}$ for that wind, and the $7.11\times10^{25}\
   \mathrm{kg\,m^{2}\,s^{-1}}$ that corresponds to $1\ \mathrm{ms}$.
4. **Polar motion**: $\sigma_c = 2.384522\times10^{-7}\ \mathrm{rad\,s^{-1}}$,
   the rigid period $304.98\ \mathrm{d}$, the numerical free-wobble period
   $304.9687\ \mathrm{d}$ and the numerical solution verified against the
   analytic one.
5. **The forced response** $1/(1-\sigma/\sigma_c)$ at four periods, showing the
   resonance.
6. **Excitation**: a $10^{-8}M$ redistribution giving $\chi = 2.885\times10^{-8}$
   and $5.95\ \mathrm{mas}$ of pole displacement.

Print-only, fixed seed, no network, exits 0.

## 8. Exercises

Full sets with worked solutions are in
[`exercises/03-earth-rotation-exercises.md`](./exercises/03-earth-rotation-exercises.md)
and
[`exercises/03-earth-rotation-solutions.md`](./exercises/03-earth-rotation-solutions.md).

- **★** Compute the wind momentum needed for a $0.5\ \mathrm{ms}$ change in LOD
  with $C = 8.4022\times10^{37}\ \mathrm{kg\,m^{2}}$.
- **★** Compute the rigid Euler period for $H = 0.00300$ and $0.00350$ and state
  the range.
- **★★** Verify the $(2/3)M\Omega R^{2}$ factor analytically for a thin shell and
  state what changes for a thick shell with a radial density profile.
- **★★** A forcing at exactly $T = 400\ \mathrm{d}$ with $\chi_0 = 1\times10^{-8}$
  produces what pole displacement? And at $T = 305\ \mathrm{d}$?
- **★★★** Design a synthetic experiment that measures the effect of omitting the
  fluid core on the inferred free period, and state what observation would
  distinguish the omission from a damping term.

## 9. Mastery checkpoint

Do this without notes:

> Using $C = 8.4022\times10^{37}\ \mathrm{kg\,m^{2}}$,
> $\Omega = 7.2921150\times10^{-5}\ \mathrm{rad\,s^{-1}}$ and $H = 0.00327$:
> **(a)** compute the axial angular momentum that corresponds to a $0.2\
> \mathrm{ms}$ change in LOD; **(b)** give the sign of the LOD change if the
> atmosphere loses westerly momentum, and justify it in one sentence;
> **(c)** compute the rigid Euler period; **(d)** compute the amplification of a
> forcing with a $200$-day period; **(e)** state two physical effects your
> answer omits and the direction in which each moves the period.

*Answers.* **(a)**

$$\Delta H_3 = C\Omega\frac{\Delta\mathrm{LOD}}{\mathrm{LOD}}
= (8.4022\times10^{37})(7.2921150\times10^{-5})
\frac{0.2\times10^{-3}}{86164} = 1.422\times10^{25}\
\mathrm{kg\,m^{2}\,s^{-1}} .$$

**(b)** The day *shortens* (negative $\Delta$LOD): if the atmosphere loses
westerly momentum, conservation gives the solid Earth an equal gain, and a faster
rotation is a shorter day.
**(c)** $\sigma_c = \Omega H = 2.384522\times10^{-7}\ \mathrm{rad\,s^{-1}}$,
$T = 2\pi/\sigma_c = 2.6350\times10^{7}\ \mathrm{s} = 304.98\ \mathrm{d}$.
**(d)** $\sigma/\sigma_c = 304.98/200 = 1.5249$, so the amplification is
$1/|1-1.5249| = 1.905$.
**(e)** Elasticity and the oceans *lengthen* the period (the Earth's compliance
means the body's axes follow the load, reducing the restoring torque); the fluid
core and dissipation also modify it, the core shifting the effective moments and
damping controlling the wobble's lifetime rather than its period. Neither can be
computed from the rigid model, which is why a wobble period is always quoted with
its Earth model.

## 10. Common pitfalls

1. **Including the moment arm twice** in an angular-momentum integral, a
   $10^{6}$-fold error in the atmosphere's momentum.
2. **Using the Earth's mass for an atmospheric momentum.** Same mistake, and it
   makes the LOD budget nonsense.
3. **Getting the sign wrong.** Westerly momentum in the atmosphere lengthens the
   day; the observation of a winter LOD maximum is the standard check.
4. **Quoting a wobble period without saying which Earth model produced it.**
   Rigid, elastic and elastic-plus-ocean values differ by tens of per cent.
5. **Assuming a small forcing makes a small wobble.** The response is resonant;
   the spectrum decides.
6. **Treating the excitation as a solid-Earth quantity.** Atmosphere, ocean,
   water and ice all contribute, and the largest terms are usually not solid.
7. **Forgetting the frame.** A pole position is relative to a frame that itself
   deforms and rotates.

## 11. Real-world applications

- **Reference frames.** Earth-orientation parameters are required to rotate
  between the celestial and terrestrial frames; see
  [07-04-05](../04-geodesy-reference-frames/05-itrf-and-plate-models.md).
- **Climate and mass transport.** Polar motion and LOD are global integrals of
  mass and momentum redistribution, complementary to gravity.
- **Core dynamics.** The 6-year and decadal LOD variations are attributed to
  core–mantle coupling, which is one of the few windows onto the core's flow.
- **Satellite geodesy.** Rotation parameters enter orbit determination and the
  reduction of satellite gravity and altimetry data.

## 12. Further reading

- **Lambeck, K., *The Earth's Variable Rotation: Geophysical Causes and
  Consequences*** — the standard monograph on LOD, polar motion and excitation.
- **Stacey, F. D. & Davis, P. M., *Physics of the Earth*** — the moments of
  inertia, ellipticity and core coupling.
- **Torge, W. & Müller, J., *Geodesy*** — rotation parameters as part of a
  terrestrial reference system.
- **Turcotte, D. L. & Schubert, G., *Geodynamics*** — the mass redistribution
  processes (isostasy, convection, ice) that excite the rotation.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Editions and years are omitted
> because they differ between printings.

## 13. Related lessons

- [01 Solid Earth Tides and Their Gravity Signature](01-solid-earth-tides.md) —
  the tidal torque, which is one of the LOD drivers on long timescales.
- [04 Post-Glacial Rebound: Viscosity and Ice History Inference](04-post-glacial-rebound.md) —
  the mass redistribution that excites both rotation and gravity changes.
- [07-04-05 ITRF, Plate Motion Models and Frame Transformations](../04-geodesy-reference-frames/05-itrf-and-plate-models.md) —
  where these parameters are used.
- [07-05-01 GRACE and GRACE-FO](../05-satellite-gravimetry/01-grace-gracefo.md) —
  the gravity counterpart of the same mass redistributions.

## 14. Related modules

- [07-01 Gravity Fundamentals](../01-gravity-fundamentals/README.md).
- [07-04 Geodesy and Reference Frames](../04-geodesy-reference-frames/README.md).
- [02 Physics](../../02-physics/README.md) — rigid-body dynamics.
- [12 Global Geophysics and the Interior](../../12-global-geophysics-interior/README.md) —
  core–mantle coupling and the deep interior.
- [26-reference-library](../../26-reference-library/README.md).

## 15. Self-assessment checklist

- [ ] I can derive and apply the LOD budget with the correct sign.
- [ ] I can compute the axial angular momentum of a wind field and check it against $(2/3)M\Omega R^{2}$.
- [ ] I can compute the rigid Euler period from the dynamical ellipticity.
- [ ] I can measure a free-wobble period numerically and verify the integration.
- [ ] I can compute the forced response and explain the resonance.
- [ ] I can convert an excitation into a pole displacement in mas.
- [ ] I can list the omitted physics and the direction of each effect.
