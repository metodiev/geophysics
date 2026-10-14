---
id: 25-01-03
title: "Project: Computing Gravity Through a Layered Earth"
level: beginner
prereqs: ["25-01-01", "07-01-01", "02-08-05", "02-11-01"]
estimated_minutes: 120
tags: [projects, gravity, shell-theorem, earth-interior, teaching]
---

# Project: Computing Gravity Through a Layered Earth

## Learning objectives

By the end of this project you will be able to:

1. **State** the shell theorem for a spherically symmetric density distribution
   and **use** it to write $g(r) = G M(r)/r^{2}$.
2. **Compute** the enclosed mass of a piecewise-constant layered Earth and
   **evaluate** $g$ at every layer boundary.
3. **Locate** the radius at which $g$ is maximum and **explain** why it lies near
   the core-mantle boundary rather than at the surface.
4. **Compare** a layered model with a uniform sphere of equal mass and radius and
   **measure** where the two disagree.
5. **Propagate** an uncertainty in one layer's density to surface gravity by Monte
   Carlo and **report** the result in mGal.
6. **Diagnose** the three errors that corrupt a layered-model computation: a
   radius in kilometres inside an SI formula, a doubled shell, and a
   non-monotonic $M(r)$.
7. **Judge** whether a model's surface gravity is evidence that the model is
   right, and **state** what it does not constrain.

The layered model, its densities and every number quoted below are
**SYNTHETIC** teaching values used by
[`code/layered_earth_gravity_demo.py`](./code/layered_earth_gravity_demo.py).
They are *not* a published Earth model: the arithmetic is exact for the model as
specified, and the model itself is chosen.

## Prerequisites

- [25-01-01 Project: Units, Conversions and First Scientific Plots](./01-units-and-plotting.md) —
  the SI conversion habits that this project's radii and densities demand.
- [07-01-01 Newtonian Gravitation, Field and Acceleration](../../07-gravity-geodesy/01-gravity-fundamentals/01-newtonian-gravity.md) —
  the field, the potential and the superposition rule.
- [02-08-05 Equipotential Surfaces, Geoid and Level Surfaces](../../02-physics/08-potential-theory/05-equipotentials.md) —
  why spherical symmetry is the special case in which the field is radial.
- [02-11-01 Pressure, Density and Gravity Inside the Earth](../../02-physics/11-physics-of-earths-interior-and-atmosphere/01-pressure-density-depth.md) —
  the interior structure this project models in five shells.

## 1. The question

*If the Earth is a stack of uniform shells, what is gravity at every depth, and
what does that profile tell you about the interior?*

This is the first project in which a physical model produces a **profile** rather
than a single number, and the profile is the point: the surface value is one
constraint, and the *shape* of $g(r)$ between the surface and the centre is where
the density structure shows up. It is also the first project where the answer is
counter-intuitive — gravity is largest **not** at the surface but about
$2900\ \mathrm{km}$ down, and the reason is pure arithmetic.

## 2. The model and its data (SYNTHETIC)

| layer | $\rho$ (kg m$^{-3}$) | $r_\text{in}$ (km) | $r_\text{out}$ (km) | shell mass (kg) | share |
|---|---|---|---|---|---|
| inner core | 13 090 | 0 | 1221.5 | $9.9933\times10^{22}$ | 1.7% |
| outer core | 11 000 | 1221.5 | 3480.0 | $1.8579\times10^{24}$ | 31.2% |
| lower mantle | 4900 | 3480.0 | 5701.0 | $2.9381\times10^{24}$ | 49.3% |
| upper mantle | 3500 | 5701.0 | 6346.6 | $1.0313\times10^{24}$ | 17.3% |
| crust | 2800 | 6346.6 | 6371.0 | $3.4714\times10^{22}$ | 0.6% |
| **total** | — | — | 6371.0 | $5.9620\times10^{24}$ | 100% |

**Provenance.** These densities are chosen round numbers in the right
neighbourhood for each shell, and the radii are likewise chosen. The model is
**SYNTHETIC**; the total mass it produces,
$5.9620\times10^{24}\ \mathrm{kg}$, is close to the standard reference figure for
the Earth of $5.972\times10^{24}\ \mathrm{kg}$ (a published constant, not a
measurement made here), which is a coincidence of the chosen numbers and not
evidence that the model is correct.

## 3. The project specification

**Steps.**

1. Build the layer table: name, inner radius, outer radius and density, in SI.
2. Write two functions: `shell_mass(r_in, r_out, rho)` and
   `mass_enclosed(r, layers)`, and test them at $r = 0$ (mass $= 0$) and at
   $r = R$ (mass $=$ total).
3. Evaluate $g(r) = GM(r)/r^{2}$ at the centre and at every layer boundary, and
   find the radius of maximum $g$ on a fine grid.
4. Compare with a uniform sphere of the same mass and radius, and report the
   disagreement at the surface and at the core-mantle boundary.
5. Perturb the crustal density and propagate the change to surface gravity, both
   analytically and by Monte Carlo.
6. Write a short report: the table, the boundary values of $g$, the location of
   the maximum, and the one measurement that the model is least able to
   constrain.

**Deliverable.** The layer table, a table of $g$ at boundaries, the location of
$\max g$, the uniform-sphere comparison, and the density-sensitivity result in
mGal.

**Success criterion.** Every quantity is in SI; $M(r)$ is non-decreasing and
$M(0) = 0$; $g$ is continuous; the maximum's location is stated to the nearest
10 km; the sensitivity is quoted with an uncertainty.

## 4. The shell theorem and the profile

For a spherically symmetric density $\rho(r')$, only the mass inside the
evaluation radius contributes, and it acts as if concentrated at the centre:

$$g(r) = \frac{G M(r)}{r^{2}},
\qquad
M(r) = 4\pi \int_0^{r} \rho(r')\, r'^{2}\,\mathrm{d}r'.$$

For piecewise-constant layers the integral is exact,

$$M(r) = \frac{4\pi}{3}\sum_i \rho_i
\left(\min(r, r_{\text{out},i})^{3} - r_{\text{in},i}^{3}\right)\Theta(r - r_{\text{in},i}),$$

with $\Theta$ the step function, and the mass of one complete shell is
$\frac{4\pi}{3}\rho(r_\text{out}^{3} - r_\text{in}^{3})$.

Two consequences follow immediately.

- **A uniform shell exerts no force inside.** Every element of a thin shell has a
  cancelling partner, so $g$ does not change as you cross a shell's *inner*
  boundary from inside — the profile is continuous, with kinks at boundaries.
- **Inside a uniform sphere**, $M(r) = \frac{4\pi}{3}\rho r^{3}$, so
  $g(r) = \frac{4\pi G}{3}\rho\, r$: linear in $r$, zero at the centre, maximum
  at the surface. The Earth is *not* uniform, so this linear result is exactly
  what §6 shows to be wrong.

## 5. Worked example: the boundary values

Using $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and the model
of §2, the demonstration prints:

| location | $r$ (km) | $M(r)$ (kg) | $g$ (m s⁻²) |
|---|---|---|---|
| centre | 0.0 | 0 | 0.0000 |
| top of inner core | 1221.5 | $9.9933\times10^{22}$ | 4.4702 |
| top of outer core (CMB) | 3480.0 | $1.9578\times10^{24}$ | 10.7900 |
| top of lower mantle | 5701.0 | $4.8959\times10^{24}$ | 10.0540 |
| top of upper mantle (Moho) | 6346.6 | $5.9272\times10^{24}$ | 9.8215 |
| surface | 6371.0 | $5.9620\times10^{24}$ | 9.8035 |

The maximum on a 400-point grid is $g = 10.7881\ \mathrm{m\,s^{-2}}$ at
$r = 3480.9\ \mathrm{km}$ — the core-mantle boundary, to within the grid step.
The reason is that $g \propto \rho r$ locally for a uniform shell and
$\rho r$ grows through the core ($13\,090 \times 1221.5$ at the top of the inner
core is much less than $11\,000\times3480$ at the CMB), while $r^{2}$ in the
denominator cannot keep up until the density drops at the CMB. At
$r = 1000\ \mathrm{km}$ the demonstration prints $g = 3.6596\ \mathrm{m\,s^{-2}}$,
so gravity is already $37\%$ of its surface value a sixth of the way out.

## 6. Why a uniform sphere fails in the interior

A uniform sphere with the same total mass and radius has
$\rho_\text{mean} = 5504.0\ \mathrm{kg\,m^{-3}}$ and produces exactly the same
**surface** value, $9.8035\ \mathrm{m\,s^{-2}}$ — the surface difference is
$+0.00\%$ by construction, since $g = GM/R^{2}$ depends only on $M$ and $R$.

At the core-mantle boundary the two models disagree drastically:

| model | $g$ at 3480 km (m s⁻²) |
|---|---|
| layered | 10.7881 |
| uniform | 5.3563 |

The uniform model is wrong by a factor of two where it matters. **A model that
reproduces surface gravity has not been tested by surface gravity**; the interior
profile is the test, and the interior profile needs seismic travel times, normal
modes, or free oscillations to constrain it.

## 7. Sensitivity to a layer density

Changing the crust density from 2800 to $3000\ \mathrm{kg\,m^{-3}}$ raises surface
gravity by $415.90$ ppm, i.e. $+4.078\ \mathrm{mGal}$ — because it changes the
mass of the whole crust, and a global change in enclosed mass moves $g$ by
$G\,\Delta M/R^{2}$.

The Monte Carlo over $\rho_\text{crust} = 2800 \pm 100\ \mathrm{kg\,m^{-3}}$
(400 draws, seeded) gives surface gravity
$9.803301 \pm 0.002005\ \mathrm{m\,s^{-2}}$, a scatter of $200.51\ \mathrm{mGal}$.
The huge size of that number is a warning about the experiment, not about the
Earth: a globally uniform change of the entire crust is not a physical
perturbation. Real surveys vary density locally over tens of kilometres, where
the effect is a correction, not a reinterpretation of the whole field.

## 8. Failure modes and how to detect them

1. **Radii in kilometres inside an SI formula.** $G$ carries $\mathrm{m^{3}}$;
   a radius in km makes $g$ too large by $10^{6}$. *Detect:* compute
   $GM/R^{2}$ for the total mass and check it against $9.8\ \mathrm{m\,s^{-2}}$.
2. **Doubled shells or overlapping radii.** A layer list whose $r_\text{in}$
   does not equal the previous $r_\text{out}$ double-counts mass. *Detect:*
   assert contiguity; print $M(r)$ at each boundary and check monotonicity.
3. **A non-monotonic $M(r)$.** Impossible physically; it always means an index
   or a `min`/`max` error in the integral. *Detect:* difference successive
   $M(r)$ values and assert they are non-negative.
4. **Confusing $g$ with the potential.** $\Phi = -GM/r$ decreases monotonically;
   $g$ does not. *Detect:* plot both or print both at the CMB.
5. **Treating a surface match as validation.** *Detect:* compare the interior
   profile against a second model, as in §6.

## 9. Rubric

| Criterion | 4 — exemplary | 3 — competent | 2 — developing | 1 — incomplete |
|---|---|---|---|---|
| Model table | SI, contiguous, masses and shares | SI and contiguous | SI only | Mixed units |
| $M(r)$ | Non-decreasing, verified at both ends | Correct | Monotonic but unverified | Wrong |
| Profile | Boundaries plus the maximum located to 10 km | Boundaries | Surface only | One number |
| Comparison | Uniform-sphere contrast at surface *and* CMB | Surface | Qualitative | Absent |
| Sensitivity | Analytic *and* Monte Carlo, in mGal | Monte Carlo | Analytic | None |

## 10. Assumptions and regime of validity

1. **Spherical symmetry and uniform layers.** Real shells have lateral density
   variations; the shell theorem gives the *mean* field and says nothing about
   regional anomalies.
2. **No rotation.** The Earth's rotation reduces the *effective* surface gravity
   (the measured value includes a centrifugal term of about
   $0.034\ \mathrm{m\,s^{-2}}$ at the equator) and makes the geoid an
   ellipsoid. The model here is non-rotating and spherical.
3. **Newtonian gravity, static.** Post-Newtonian corrections are irrelevant at
   this precision; a time-varying field is not modelled.
4. **Densities are chosen, not inverted.** A model that matches surface gravity
   and the CMB value is not thereby correct — the inverse problem has a null
   space, and this model is one point in it.
5. **The crust is a single shell.** Real crust differs between continents and
   oceans by several hundred kg m⁻³; §7 shows what that is worth at the surface.

## The honest summary

The project turns a five-layer model into a gravity profile with one
non-obvious result: $g$ peaks at about $3480\ \mathrm{km}$ radius near the
core-mantle boundary at $10.7881\ \mathrm{m\,s^{-2}}$, not at the surface, where
it is $9.8035\ \mathrm{m\,s^{-2}}$. The uniform-sphere comparison makes the point
that a matching surface value validates almost nothing: the two models agree at
the surface to $0.00\%$ and disagree at the CMB by a factor of two. What
transfers to real work is the shell-theorem machinery, the habit of checking
$M(0) = 0$ and monotonic $M(r)$, and the reading of a gravity profile as a weak
probe of interior density — weak because §7 shows that a globally uniform
crustal density change moves surface gravity by hundreds of mGal while a real
survey's anomalies are tens.

## Python demonstration

[`code/layered_earth_gravity_demo.py`](./code/layered_earth_gravity_demo.py)
prints every number quoted above. It:

1. tabulates the layers with their shell masses and mass shares, totalling
   $5.9620\times10^{24}\ \mathrm{kg}$;
2. evaluates $g(r)$ at the centre and at every boundary, and locates the maximum
   at $r = 3480.9\ \mathrm{km}$ with $g = 10.7881\ \mathrm{m\,s^{-2}}$;
3. compares with a uniform sphere, printing the CMB values $10.7881$ against
   $5.3563\ \mathrm{m\,s^{-2}}$;
4. perturbs the crust density analytically ($+415.90$ ppm at
   $+200\ \mathrm{kg\,m^{-3}}$) and by a seeded 400-draw Monte Carlo
   ($9.803301 \pm 0.002005\ \mathrm{m\,s^{-2}}$, $200.51\ \mathrm{mGal}$).

Run it with the project virtual environment:

```bash
cd 25-projects-capstone/01-beginner-projects/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python layered_earth_gravity_demo.py
```

The script prints only, writes no files, uses no network and exits 0.

## Exercises

Graded problems and worked solutions are in
[`exercises/03-gravity-of-earths-layers-exercises.md`](./exercises/03-gravity-of-earths-layers-exercises.md)
and
[`exercises/03-gravity-of-earths-layers-solutions.md`](./exercises/03-gravity-of-earths-layers-solutions.md).
The ★★★ item asks you to design an inversion of the profile, not to recompute it.

## Mastery checkpoint

Without notes:

1. State the shell theorem in one sentence and write $g(r)$ for a general
   spherically symmetric $\rho(r)$.
2. Compute the shell mass of a layer with $\rho = 4000\ \mathrm{kg\,m^{-3}}$,
   $r_\text{in} = 5000\ \mathrm{km}$ and $r_\text{out} = 6000\ \mathrm{km}$.
3. The CMB value is $10.7900\ \mathrm{m\,s^{-2}}$ and the surface value
   $9.8035\ \mathrm{m\,s^{-2}}$. Explain in two sentences why the profile is not
   decreasing everywhere.
4. A colleague matches the surface value with a two-layer model. Name the two
   additional observations that would test it.

## Common pitfalls

1. **Reporting the surface value as the model's validation.** It is one
   constraint on two parameters, and §6 shows how little it means.
2. **Assuming $g$ is maximum at the surface.** It is maximum near the CMB for
   the real Earth and for this model.
3. **Using the mean density as if it were the density at depth.** The mean,
   $5504.0\ \mathrm{kg\,m^{-3}}$, is a specific radius-weighted average and
   exceeds the crustal density by a factor of two.
4. **Forgetting that the shell theorem needs symmetry.** A laterally varying
   crust breaks the argument, and the shell theorem then says nothing.

## Where this is used

The shell-theorem profile is the reference against which gravity anomalies are
defined: subtracting a normal field is only meaningful if you know what the
normal field is. The next step in this folder is
[25-02-02](../02-intermediate-projects/02-simple-gravity-model.md), which takes a
*local* density contrast and computes the anomaly it produces, and the graduate
project [25-04-05](../04-graduate-projects/05-joint-inversion-project.md) inverts
such anomalies jointly with seismic data. In professional practice the same
computation appears in every gravity-reduction pipeline as the normal-gravity
term, and in resource exploration as the density model that a survey's regional
field is removed against.

## Related lessons

- [07-01-03 Reference Ellipsoid, Normal Gravity and Clairaut's Theorem](../../07-gravity-geodesy/01-gravity-fundamentals/03-normal-gravity.md) —
  the rotating, ellipsoidal version of this profile.
- [07-01-02 Gravitational Potential, Equipotentials and the Geoid](../../07-gravity-geodesy/01-gravity-fundamentals/02-gravity-potential.md) —
  the potential whose gradient is computed here.
- [05-01-04 Non-Uniqueness of Geophysical Models](../../05-core-geophysics/01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md) —
  why a matching profile is not a proof.
- [25-02-02 Project: Gravity Anomaly of Simple Bodies](../02-intermediate-projects/02-simple-gravity-model.md) —
  the next project in this folder.

## Self-assessment checklist

- [ ] I can state the shell theorem and write $M(r)$ for a layered model.
- [ ] I can compute a shell mass and check $M(0) = 0$.
- [ ] I can evaluate $g$ at any boundary in SI without a unit error.
- [ ] I can explain why $g$ peaks near the core-mantle boundary.
- [ ] I can show where a uniform sphere disagrees with a layered model.
- [ ] I can propagate a density uncertainty to surface gravity in mGal.
