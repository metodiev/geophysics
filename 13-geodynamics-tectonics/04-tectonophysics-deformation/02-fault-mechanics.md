---
id: 13-04-02
title: "Fault Mechanics, Coulomb Stress and Stress Transfer"
level: research
prereqs: ["13-04-01", "02-04-08", "04-04-02"]
tags: [geodynamics, tectonophysics, faults, coulomb-stress, friction, stress-transfer, earthquake-triggering]
---

# Fault Mechanics, Coulomb Stress and Stress Transfer

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the resolved normal and shear stress on a plane of given
   orientation from a principal stress state, and **find** the optimal failure
   angle analytically and by scanning.
2. **Derive** Anderson's fault dips from the friction coefficient alone, and
   **state** the assumption that makes them predictions rather than
   observations.
3. **Write down** the exact 2-D anti-plane (screw-dislocation) solution for a
   surface-breaking strike-slip fault, and **verify** it against the free-surface
   condition and a finite-difference derivative.
4. **Resolve** a stress change onto receiver faults of arbitrary strike, and
   **derive** $\Delta\mathrm{CFS} = \sigma_{xy}(\cos 2\phi + \mu\sin 2\phi)$.
5. **Compute** the promoted and shadowed regions around a slipped fault,
   including the closed-form zero crossing $z = \sqrt{x^{2}+d^{2}}$.
6. **State** the failure differential stress at depth for a cohesionless Coulomb
   material, $\Delta\sigma = 2\sin\phi\,\sigma_v(1-\lambda)$.
7. **State** the assumptions of the 2-D anti-plane model and **name** the
   physical effects a 3-D dislocation solution adds.

## Prerequisites

- [13-04-01 Crustal Deformation from GNSS and Strain Rates](01-crustal-deformation-gps.md) —
  the strain that loads faults.
- [02-04-08 Failure and Friction](../../02-physics/04-elasticity-and-continuum-mechanics/08-failure-and-friction.md) —
  the Coulomb criterion and friction laws.
- [04-04-02 Fault Geometry, Kinematics and Fault Classification](../../04-earth-science-geology/04-structural-geology/02-faults.md) —
  strike, dip, rake and the geological vocabulary.

All models and data in this module are **SYNTHETIC**. The stress state, friction
coefficient, slip, modulus and geometry are chosen teaching values. The
stress-transfer model is the exact 2-D anti-plane screw dislocation, which is a
teaching analogue of a strike-slip fault; it is not a full 3-D dislocation
solution and its limitations are stated in Section 5. The exact constant used is
$g = 9.81\ \mathrm{m\,s^{-2}}$.

## 1. Resolved stresses, and the optimum angle

For a two-dimensional stress state with principal stresses $\sigma_1 \ge
\sigma_3$ in the plane, the normal and shear stress on a plane whose normal makes
an angle $\theta$ with $\sigma_1$ are

$$
\sigma_n = \frac{\sigma_1+\sigma_3}{2} + \frac{\sigma_1-\sigma_3}{2}\cos 2\theta,
\qquad
\tau = \frac{\sigma_1-\sigma_3}{2}\sin 2\theta .
$$

With the Coulomb criterion $\lvert\tau\rvert = C + \mu(\sigma_n - p)$ for cohesion
$C$ and pore pressure $p$, the **Coulomb failure function** is
$\mathrm{CFF} = \lvert\tau\rvert - \mu(\sigma_n - p)$, and the plane that fails
first maximises it. Differentiating with respect to $\theta$:

$$
\frac{\mathrm d\,\mathrm{CFF}}{\mathrm d\theta} = (\sigma_1-\sigma_3)
\left[\cos 2\theta + \mu\sin 2\theta\right] = 0
\;\;\Longrightarrow\;\;
\tan 2\theta = -\frac{1}{\mu} .
$$

Taking the relevant root ($2\theta$ in the second quadrant) gives the classical
result

$$
\boxed{\;2\theta_{\text{opt}} = 90^\circ + \phi, \qquad
\theta_{\text{opt}} = 45^\circ + \frac{\phi}{2}, \qquad \tan\phi \equiv \mu ,}
$$

where $\theta$ is measured from the fault **normal** to $\sigma_1$, so the fault
**plane** makes $90^\circ - \theta_{\text{opt}} = 45^\circ - \phi/2$ with
$\sigma_1$.

For the SYNTHETIC $\mu = 0.75$: $\phi = 36.87^\circ$ and
$\theta_{\text{opt}} = 63.435^\circ$ measured **from the normal to $\sigma_1$**.
The fault plane itself therefore makes
$90^\circ - \theta_{\text{opt}} = 26.565^\circ = 45^\circ - \phi/2$ with
$\sigma_1$ — the form usually quoted, and the source of endless confusion
because the two conventions differ by the complement.

The demonstration scans $881$ orientations over $1^\circ$–$89^\circ$ (a step of
$0.100^\circ$) and finds the maximum at $63.400^\circ$, agreeing with
$45^\circ+\phi/2 = 63.435^\circ$ to within one step. At that orientation the
SYNTHETIC state $\sigma_1 = 120$, $\sigma_3 = 40\ \mathrm{MPa}$ gives
$\sigma_n = 56.04\ \mathrm{MPa}$, $\lvert\tau\rvert = 32.03\ \mathrm{MPa}$ and a
failure function of $-10.00\ \mathrm{MPa}$, i.e. the state is
$10\ \mathrm{MPa}$ short of failure.

**Two things to carry away.** First, the function to maximise is
$\lvert\tau\rvert - \mu(\sigma_n-p)$, not $\lvert\tau\rvert + \mu(\sigma_n-p)$:
maximising the latter finds the plane with the largest clamping stress, which is
the opposite end of the range, and it returns the complement of the correct
angle. That error is easy to make and produces a plausible-looking number.
Second, derive the closed form and find it numerically, then check that they
agree to within the resolution of the search — a scan cannot resolve better than
its step, and a $0.1^\circ$ step is the natural place to stop.

## 2. Anderson's dips, and what they assume

Anderson's theory of faulting follows from Section 1 once one principal stress is
known to be vertical:

| regime | $\sigma_1$ direction | optimal dip |
|---|---|---|
| normal | vertical | $45^\circ + \phi/2 = 63.4^\circ$ |
| thrust | horizontal | $45^\circ - \phi/2 = 26.6^\circ$ |
| strike-slip | horizontal | $90^\circ$ (vertical fault) |

The familiar "normal faults dip about $60^\circ$, thrusts about $30^\circ$" is
therefore a **prediction of $\mu = 0.75$ and a free surface**, not an
independent observation. Its assumptions are worth listing because they fail
routinely: a free surface, no inherited anisotropy or weak bedding, no
significant topographic load, and a stress state that is not itself
rotating. Where those fail — most thrust belts — the observed dips scatter
widely around $30^\circ$, and the scatter is the information.

A second consequence is easy to miss: the theory predicts the dip with respect
to $\sigma_1$, so **measuring a fault's dip does not tell you the stress
orientation unless you know which principal stress is vertical**. Inverting
focal mechanisms for stress orientation uses exactly this freedom.

## 3. A stress change that can be computed exactly

For teaching stress transfer, one case is solvable in closed form: **anti-plane
strain**, in which the medium moves only along strike ($y$), the fault is the
plane $x = 0$, and the displacement is

$$
u_y(x,z) = \frac{s}{\pi}\left[\operatorname{atan2}(z-d,\,x)
- \operatorname{atan2}(z+d,\,x)\right],
$$

where $d$ is the depth of the base of the slipped patch and $s$ the slip. The
second term is an **image** dislocation at $z = -d$; it exists only to make the
surface traction-free, and Section 3.1 verifies that it does.

The non-zero stresses follow by differentiation:

$$
\sigma_{xy} = \frac{\mu_e s}{\pi}\left[
\frac{z+d}{(z+d)^{2}+x^{2}} - \frac{z-d}{(z-d)^{2}+x^{2}}\right],
\qquad
\sigma_{yz} = \frac{\mu_e s}{\pi}\left[
\frac{x}{(z-d)^{2}+x^{2}} - \frac{x}{(z+d)^{2}+x^{2}}\right].
$$

Note what is missing: in anti-plane strain $\sigma_{xx}$, $\sigma_{yy}$ and
$\sigma_{zz}$ do not change at all. That single fact makes the Coulomb stress
change on a parallel fault equal to the shear stress change, and it is also the
model's main limitation.

### 3.1 Verification

With the SYNTHETIC parameters $\mu_e = 30\ \mathrm{GPa}$, $s = 1\ \mathrm{m}$,
$d = 12\ \mathrm{km}$:

1. **Free surface.** $\max\lvert\sigma_{yz}(x, 0)\rvert = 0$ to machine
   precision. A traction-free surface requires exactly zero, and the image
   dislocation is what enforces it.
2. **Finite-difference derivative.** At $(x, z) = (20, 6)\ \mathrm{km}$ the
   analytic $\sigma_{xy} = 3.688258\times10^{5}\ \mathrm{Pa}$ and
   $\mu_e\,\partial u_y/\partial x$ computed by central differences gives the
   same value with a relative difference of $1.09\times10^{-9}$.
3. **Far-field decay.** On the surface,
   $\sigma_{xy}(x,0) = 2\mu_e s d/(\pi x^{2})$ asymptotically. The measured
   ratios to that asymptote are $0.9964$ at $200\ \mathrm{km}$,
   $0.9991$ at $400\ \mathrm{km}$, $0.9998$ at $800\ \mathrm{km}$ and
   $0.9999$ at $1600\ \mathrm{km}$.
4. **On-fault value.** $\sigma_{xy}(0,0) = 2\mu_e s/(\pi d) =
   1.592\ \mathrm{MPa}$ — finite at the fault trace, because the singularity of a
   2-D dislocation is integrable.

## 4. Coulomb stress change on receiver faults

Consider a vertical receiver plane striking at angle $\phi$ from the main fault.
With the main fault striking along $y$ and $x$ perpendicular to it, the receiver
normal is $n = (\cos\phi, \sin\phi, 0)$ and its strike direction is
$\hat s = (-\sin\phi, \cos\phi, 0)$. Of the stress-change tensor only
$\sigma_{xy} = \sigma_{yx}$ is non-zero, so

$$
\Delta\sigma_n = n_i\,\Delta\sigma_{ij}\,n_j = \sigma_{xy}\sin 2\phi,
\qquad
\Delta\tau = \hat s_i\,\Delta\sigma_{ij}\,n_j = \sigma_{xy}\cos 2\phi,
$$

and therefore

$$
\boxed{\;\Delta\mathrm{CFS}(\phi) = \Delta\tau + \mu\,\Delta\sigma_n
= \sigma_{xy}\left(\cos 2\phi + \mu\sin 2\phi\right).}
$$

Two consequences follow immediately, and both are testable:

- **A parallel fault has no normal-stress change.** At $\phi = 0$,
  $\Delta\sigma_n = 0$ and $\Delta\mathrm{CFS} = \sigma_{xy}$: the Coulomb change
  is purely the shear change. At the demonstration's receiver,
  $(x,z) = (8, 5)\ \mathrm{km}$, that is $1.0542\ \mathrm{MPa}$.
- **The most promoted strike is not the main fault's.** Maximising
  $\cos 2\phi + \mu\sin 2\phi$ gives $\tan 2\phi = \mu$, i.e.
  $\phi = \tfrac12\arctan\mu = 18.43^\circ$ for $\mu = 0.75$; the scan finds
  $18.40^\circ$ and $\Delta\mathrm{CFS} = 1.3143\ \mathrm{MPa}$, a factor
  $\sqrt{1+\mu^{2}} = 1.25$ more than the parallel case. The most inhibited
  strike is $108.40^\circ$ with $-1.3143\ \mathrm{MPa}$.

So a Coulomb stress calculation **cannot be reported without stating the
receiver mechanism.** The same stress change promotes faults at $18^\circ$,
shadows faults at $108^\circ$, and does something in between at all other
orientations.

### 4.1 Where the stress change is positive

On the fault-parallel mechanism ($\Delta\mathrm{CFS} = \sigma_{xy}$), the sign
of $\sigma_{xy}$ changes at

$$
z = \sqrt{x^{2}+d^{2}},
$$

which the demonstration measures as $12.9$, $15.6$, $23.4$ and
$41.7\ \mathrm{km}$ at $x = 5$, $10$, $20$ and $40\ \mathrm{km}$, against the
closed form $13.0$, $15.6$, $23.3$ and $41.8\ \mathrm{km}$. The boundary passes
exactly through the fault tip $(0, d)$. Over the sampled grid, $82.8\%$ of the
area has positive $\Delta\mathrm{CFS}$ — promoted near the surface beside the
slip zone, shadowed deeper than the fault tip and beyond the ends.

**What that does and does not mean.** A positive $\Delta\mathrm{CFS}$ means the
fault is brought closer to failure by the elastic stress change. Real aftershock
distributions correlate with it, which is why the calculation is used. But the
correlation is not a prediction of *how many* events occur or *when*: that
requires the background stressing rate and a rate-and-state nucleation model,
and the fraction of seismicity explicable by stress transfer alone is a
long-running argument. The honest use of this section is as a **susceptibility**
map, not a forecast.

## 5. Friction, depth and the failure stress

For a cohesionless Coulomb material on its optimal plane, and assuming the mean
principal stress equals the lithostatic stress $\sigma_v = \rho g z$, the
differential stress at failure is (derived in
[13-03-03](../03-plate-tectonics-quantitative/03-orogenic-systems.md) and
re-derived here for convenience)

$$
\Delta\sigma = \frac{2\mu\,\sigma_v(1-\lambda)}{\cos\phi + \mu\sin\phi}
= 2\sin\phi\;\sigma_v(1-\lambda),
$$

where the identity $2\mu/(\cos\phi+\mu\sin\phi) = 2\sin\phi$ holds because
$\mu = \tan\phi$; the demonstration checks it either way and both give
$1.200000\sigma_v(1-\lambda)$ for $\mu = 0.75$.

| depth (km) | $\sigma_v$ (MPa) | $\Delta\sigma$, $\lambda=0$ (MPa) | $\Delta\sigma$, $\lambda=0.4$ (MPa) |
|---|---|---|---|
| 2 | 54.9 | 65.9 | 39.6 |
| 5 | 137.3 | 164.8 | 98.9 |
| 10 | 274.7 | 329.6 | 197.8 |
| 15 | 412.0 | 494.4 | 296.7 |
| 20 | 549.4 | 659.2 | 395.5 |

The strength rises linearly with depth while the ductile (creep) strength falls
exponentially with temperature, so the two cross at the **brittle–ductile
transition**, and the depth of that transition — not the friction coefficient —
is what controls whether a fault can host large earthquakes
([13-01-03](../01-geodynamic-principles/03-lithospheric-strength.md)). Pore
pressure matters at the same order: $\lambda = 0.4$ removes $40\%$ of the
effective normal stress and therefore $40\%$ of the strength, which is why
overpressured faults slip at lower shear stress than the friction coefficient
alone suggests.

## 6. Assumptions and regime of validity

1. **2-D anti-plane strain.** Displacement is along strike only. This is the
   exact solution for a vertical strike-slip fault in the far field of a long
   fault, and it is **wrong** in detail: a real 3-D dislocation also changes
   $\sigma_{xx}$, $\sigma_{yy}$, $\sigma_{zz}$ and $\sigma_{xz}$, and those normal
   stress changes add a term to $\Delta\mathrm{CFS}$ even on parallel planes. The
   parallel-fault simplification of Section 4 is therefore a property of the
   model, not of nature.
2. **A vertical fault.** The screw-dislocation solution applies to a vertical
   plane. A dipping megathrust requires a full dislocation solution, and the
   surface deformation pattern is qualitatively different.
3. **Elastic, homogeneous, isotropic half-space.** No layering, no topography,
   no viscoelastic relaxation. Postseismic relaxation redistributes stress for
   decades after an event
   ([13-04-03](03-postseismic-viscoelastic.md)).
4. **Instantaneous slip of prescribed magnitude.** The slip distribution is an
   input, not a prediction; the calculation says nothing about why the fault
   slipped where it did.
5. **Friction is a constant.** $\mu = 0.75$ is a SYNTHETIC value here. Real
   faults show velocity-weakening/strengthening, healing, and $\mu$ that depends
   on slip rate and history; the Coulomb criterion is a static, rate-independent
   approximation.
6. **No pore-pressure change from the earthquake itself.** $\Delta p$ is
   neglected; in a real stress transfer calculation it can dominate, and it is the
   least well constrained term.
7. **The mean principal stress equals the lithostatic value** in the strength
   table. That is an assumption about the stress state, and it is not implied by
   the friction law.

## 7. Worked example — two receivers, one stress change

Take the demonstration's receiver point $(x, z) = (8, 5)\ \mathrm{km}$ and the
same main shock ($s = 1\ \mathrm{m}$, $d = 12\ \mathrm{km}$,
$\mu_e = 30\ \mathrm{GPa}$).

1. **Stress change.** $\sigma_{xy} = 1.0514\ \mathrm{MPa}$ (demonstration).
2. **A parallel fault** ($\phi = 0$): $\Delta\sigma_n = 0$,
   $\Delta\tau = 1.0514\ \mathrm{MPa}$, $\Delta\mathrm{CFS} = 1.0514\
   \mathrm{MPa}$.
3. **The most promoted strike** ($\phi = 18.43^\circ$):
   $\Delta\tau = \sigma_{xy}\cos 36.87^\circ = 1.0514\times0.8 =
   0.8411\ \mathrm{MPa}$; $\Delta\sigma_n = \sigma_{xy}\sin 36.87^\circ =
   1.0514\times0.6 = 0.6308\ \mathrm{MPa}$;
   $\Delta\mathrm{CFS} = 0.8411 + 0.75\times0.6308 = 1.3142\ \mathrm{MPa}$,
   matching the demonstration's $1.3143$.
4. **The most inhibited strike** ($\phi = 108.43^\circ$): the same magnitude with
   the opposite sign, $-1.3142\ \mathrm{MPa}$.
5. **Interpretation.** A fault already close to failure and oriented at
   $\sim18^\circ$ to the main shock is brought $1.3\ \mathrm{MPa}$ closer; one at
   $\sim108^\circ$ is moved $1.3\ \mathrm{MPa}$ further away. Since a typical
   stress drop is a few megapascals, a $1.3\ \mathrm{MPa}$ change is a
   first-order perturbation, not a rounding error.

## 8. Python demonstration

`code/fault_mechanics_demo.py` prints labelled results with units and exits 0.
It:

1. scans the Coulomb failure function over 881 plane orientations and compares
   the maximum with $45^\circ-\phi/2$, reporting the mean-stress state relative to
   failure;
2. derives Anderson's dips for the three regimes;
3. computes the anti-plane stress change and verifies it three ways: the
   free-surface condition, a finite-difference derivative, and the far-field
   $1/x^{2}$ decay;
4. resolves the stress change onto receiver faults of every strike and finds the
   most promoted and most inhibited orientations;
5. maps the promoted and shadowed regions and checks the zero crossing against
   $z = \sqrt{x^{2}+d^{2}}$;
6. tabulates the failure differential stress with depth and pore pressure, with
   the algebraic identity $2\mu/(\cos\phi+\mu\sin\phi) = 2\sin\phi$ checked
   numerically.

## Mastery checkpoint

Complete this without notes.

> A SYNTHETIC strike-slip fault ($\mu_e = 30\ \mathrm{GPa}$) slipped $2\
> \mathrm{m}$ from the surface to $10\ \mathrm{km}$. **(a)** Compute
> $\sigma_{xy}$ at the surface directly above the fault trace and at
> $x = 20\ \mathrm{km}$ on the surface. **(b)** At the point
> $(x,z) = (20, 4)\ \mathrm{km}$ compute $\Delta\mathrm{CFS}$ for a parallel
> vertical fault and for a fault striking $18.4^\circ$ from it with
> $\mu = 0.75$. **(c)** State at what depth the sign of $\Delta\mathrm{CFS}$
> changes on the parallel mechanism at $x = 20\ \mathrm{km}$, and check it against
> $\sqrt{x^{2}+d^{2}}$. **(d)** Explain in two sentences why the parallel-fault
> $\Delta\sigma_n = 0$ is an artefact of the 2-D model.

## Common pitfalls

1. **Reporting a stress change without the receiver mechanism.** The same stress
   change is $+1.31$ and $-1.31\ \mathrm{MPa}$ on faults $90^\circ$ apart.
2. **Reading Anderson's dips as data.** They are predictions of $\mu = 0.75$ and
   a free surface; observed dips scatter.
3. **Forgetting the image dislocation.** Without it the surface traction is
   non-zero and the solution is wrong everywhere near the fault.
4. **Using the scale $\sigma_{xy} \sim \mu s/(\pi d)$** without the image term:
   the on-fault value is $2\mu s/(\pi d)$, a factor of two.
5. **Treating a positive $\Delta\mathrm{CFS}$ as a prediction.** It is a
   susceptibility; the rate and number of aftershocks require more.
6. **Ignoring pore pressure.** $\lambda = 0.4$ changes the failure stress by
   $40\%$, comparable to doubling the friction coefficient's effect on the
   strength.
7. **Believing the 2-D normal-stress result.** In 3-D, parallel faults do
   experience normal-stress changes.

## Related modules

- [13-04-03 Postseismic Relaxation and Viscoelastic Models](03-postseismic-viscoelastic.md) —
  what happens to this stress change over the following decades.
- [13-04-04 Interseismic Coupling and Megathrust Locking](04-interseismic-coupling.md) —
  the stress that is accumulating before the event.
- [13-03-03 Orogenic Systems, Crustal Thickening and Collapse](../03-plate-tectonics-quantitative/03-orogenic-systems.md) —
  where the $\Delta\sigma = 2\sin\phi\,\sigma_v(1-\lambda)$ result is derived.
- [04-04-01 Stress, Strain and Brittle vs Ductile Deformation](../../04-earth-science-geology/04-structural-geology/01-stress-strain-rocks.md).
- [13-01-03 Lithospheric Strength and Flexure](../01-geodynamic-principles/03-lithospheric-strength.md) —
  the brittle–ductile transition that limits the seismogenic depth.
- [06-12 Induced and Triggered Seismicity](../../06-seismology/12-induced-and-triggered-seismicity/README.md) —
  the practical application and its controversies.
