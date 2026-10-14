---
id: 10-05-02
title: "Surface-Wave Methods for Shallow Layers"
level: advanced
prereqs: ["05-01-01", "05-04-02", "06-01-01", "10-05-01"]
tags: [near-surface, surface-waves, dispersion, rayleigh, love, sensitivity]
---

# Surface-Wave Methods for Shallow Layers

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Rayleigh-wave speed of a homogeneous half-space from the
   free-surface boundary conditions, and **solve** the resulting cubic for a
   given Poisson's ratio.
2. **Derive** the Love-wave dispersion equation for one layer over a half-space,
   **state** its branch structure, and **compute** the higher-mode cut-off
   frequencies $f_{c,n}$.
3. **Derive** the depth sensitivity kernel of a Love mode from the variational
   form of the dispersion relation, and **verify** it against a finite-difference
   perturbation.
4. **Measure** how the sensitivity kernel scales with wavelength, and explain why
   the "one-third of a wavelength" rule of thumb is not a constant.
5. **Quantify** the thickness–velocity trade-off: construct alternative models
   that fit the same dispersion curve, and state the band in which the ridge is
   wide.
6. **State** why a *slow* layer over a *fast* half-space supports trapped surface
   waves while the reverse configuration does not, and what that means for a
   fast surface layer.

## Prerequisites

- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md) —
  what a measureable contrast is.
- [05-04-02 Effective-Medium Theory](../../05-core-geophysics/04-rock-physics/02-effective-medium-theory.md) —
  how $v_s$, $\rho$ and the elastic moduli are related.
- [06-01-01 The Elastic Wave Equation](../../06-seismology/01-elastic-wave-propagation/01-wave-equation-elastic.md) —
  P and S waves, free surfaces and interface conditions.
- [10-05-01 EM Induction and Conductivity Meters](01-electromagnetic-induction-nearsurface.md) —
  the sibling lesson on a measurement that is a weighted depth average.

> All models and data in this module are **SYNTHETIC**. The two-layer models,
> velocities, densities and thicknesses below are chosen teaching values, not
> measurements and not site parameters.

## 1. Intuition: the shallowest wave that carries a depth scale

A hammer blow on the ground radiates P and S body waves, but the largest arrival
on a line of geophones a few metres away is usually something else: energy
trapped in the top few metres, travelling horizontally with a speed that depends
on frequency. That is a **surface wave**, and the reason it is useful is exactly
the reason seismologists use it at crustal scale: its speed at a given frequency
reflects the elastic properties of a depth range set by its wavelength.

Two surface-wave families matter here.

- **Rayleigh waves** — the coupled P–SV motion that exists at the free surface of
  any elastic half-space. Their particle motion at the surface is retrograde
  elliptical, and they exist even in a *uniform* half-space, where they travel at
  one speed $c_R$ with no dispersion.
- **Love waves** — horizontally polarised shear motion trapped in a *slower*
  layer over a faster half-space. They cannot exist in a uniform half-space: they
  need the layering.

Both become **dispersive** when the ground is layered: different frequencies
sample different depths, so $c(f)$ carries a depth profile. The method is
therefore not "measure a velocity" but "measure a curve and invert it", and — as
with every inverse problem in this curriculum — the inversion returns a **ridge,
not a point**. The honest content of this lesson is the derivation of the
dispersion relations, the derivation and verification of the depth kernel that
makes the curve interpretable, and a measured statement of how wide that ridge is.

The acquisition workflow, the multichannel analysis of surface waves (MASW) and
the engineering outputs ($V_{S30}$, site class, site period) are the subject of
[06-10-04 MASW and SASW](../../06-seismology/10-refraction-and-near-surface-seismology/04-masw-sasw.md).
This lesson supplies the physics and the inverse-problem structure that the
workflow assumes.

## 2. Precise definitions

**Phase velocity.** For a harmonic wave $e^{i(kx-\omega t)}$, the phase velocity
is $c = \omega/k$. The **dispersion curve** is $c$ as a function of frequency $f$
or wavelength $\lambda = c/f$. The **group velocity** is $U = \mathrm{d}\omega/
\mathrm{d}k$; it is what carries energy, and it equals $c$ only when there is no
dispersion.

**Mode.** A layered medium supports several guided modes, indexed
$n = 0, 1, 2, \ldots$, each with its own curve $c_n(f)$. Mode $0$ (the
fundamental) exists at every frequency for the configurations considered here;
higher modes appear only above a **cut-off frequency** and carry depth
information that the fundamental cannot supply.

**Wavelength as a depth scale.** The kernel derived in Section 3.3 shows that a
measurement at frequency $f$ constrains a depth range centred near a *fraction*
of $\lambda$. That fraction is not universal — Section 4 measures it — but the
$\lambda$ scaling is, and it is why a surface-wave survey needs a band of
frequencies rather than one.

**Retrograde and prograde.** For a Rayleigh wave at the free surface the particle
motion is an ellipse traversed **retrograde** (anticlockwise as seen looking along
the propagation direction in the usual convention). The ratio of horizontal to
vertical surface displacement is a function of Poisson's ratio only, and Section 5
computes it.

**Elastic constants used below.** With $\alpha$ the P-wave speed,
$\beta$ the S-wave speed and $\nu$ Poisson's ratio for an isotropic solid,
$\mu = \rho\beta^2$, $\lambda = \rho(\alpha^2-2\beta^2)$ and

$$\frac{\alpha}{\beta} = \sqrt{\frac{2(1-\nu)}{1-2\nu}} .$$

## 3. Derivations

### 3.1 The Rayleigh speed of a homogeneous half-space

Write the displacement as $\mathbf u = \nabla\phi + \nabla\times(\psi\hat{\mathbf
y})$ with $\phi = A e^{-kqz}e^{ikx}$ and $\psi = B e^{-ksz}e^{ikx}$,
$q = \sqrt{1-c^2/\alpha^2}$ and $s = \sqrt{1-c^2/\beta^2}$. Both potentials
satisfy their Helmholtz equations by construction, and both decay with depth,
which requires $c < \beta$.

The free surface carries no traction, which fixes $A$ and $B$:

$$\sigma_{zz} = \lambda\nabla^2\phi + 2\mu\left(\phi_{,zz} + \psi_{,xz}\right) = 0,$$
$$\sigma_{xz} = \mu\left(2\phi_{,xz} + \psi_{,xx} - \psi_{,zz}\right) = 0,$$

where the first line uses $\varepsilon_{xx}+\varepsilon_{zz} = \nabla^2\phi$:
the $\psi$ terms of the two normal strains cancel, so no $\psi$ appears in the
$\lambda$ term. Evaluating at $z = 0$ and dividing by $k^2$:

$$\rho(2\beta^2 - c^2)A - 2i\mu s\,B = 0,$$
$$-2iq\mu A - \mu(1+s^2)B = 0 .$$

The first row follows from $\lambda(-c^2/\alpha^2) + 2\mu q^2 = \rho(2\beta^2-c^2)$.
Eliminating $B$, or setting the determinant to zero, and using $\mu = \rho\beta^2$
gives

$$\boxed{\;(2 - \zeta^2)^2 = 4\sqrt{1-\eta^2\zeta^2}\,\sqrt{1-\zeta^2}\;},
\qquad \zeta = \frac{c_R}{\beta}, \quad \eta = \frac{\beta}{\alpha}.$$

Squaring and collecting gives the classical sextic
$\zeta^6 - 8\zeta^4 + 8(3-2\eta^2)\zeta^2 - 16(1-\eta^2) = 0$, whose root in
$(0,1)$ is the Rayleigh speed. Note there is no frequency in the equation — a
uniform half-space is **not** dispersive — and that $\zeta$ depends on the
material only through $\nu$ (or $\eta$).

### 3.2 Love waves in a layer over a half-space

Take a layer $0 \le z \le h$ with $(\beta_1,\rho_1)$ over a half-space
$z > h$ with $(\beta_2,\rho_2)$, and look for $v(z)e^{ikx}$ solving

$$\frac{\mathrm d}{\mathrm dz}\left(\mu\frac{\mathrm dv}{\mathrm dz}\right)
+ \omega^2\rho\,v = \mu k^2 v .$$

For a trapped mode we need $\beta_1 < c < \beta_2$, so that the motion oscillates
in the layer and decays in the half-space:

$$v = A\cos(k_1 z), \qquad k_1 = \omega\sqrt{\frac{1}{\beta_1^2}-\frac{1}{c^2}},$$
$$v = A\cos(k_1h)\,e^{-k_2(z-h)}, \qquad
k_2 = \omega\sqrt{\frac{1}{c^2}-\frac{1}{\beta_2^2}} .$$

The free surface requires $\mathrm dv/\mathrm dz = 0$ at $z = 0$ (hence the cosine),
continuity of $v$ at $h$ is already imposed, and continuity of traction
$\mu\,\mathrm dv/\mathrm dz$ gives the dispersion equation

$$\boxed{\;\tan(k_1h) = \frac{\mu_2 k_2}{\mu_1 k_1} \equiv B(c)\;}.$$

Because the right-hand side is positive, the solutions lie on the branches
$k_1h \in (n\pi, n\pi + \pi/2)$, $n = 0, 1, 2,\ldots$ — one mode per branch. A
branch is reachable only if $k_1h$ can reach $n\pi$ somewhere in
$(\beta_1,\beta_2)$, which gives the exact cut-off

$$f_{c,n} = \frac{n\pi}{h\sqrt{1/\beta_1^2 - 1/\beta_2^2}} .$$

Three consequences follow from the equation alone, and the demonstration measures
all three.

1. **The fundamental always exists** and has no cut-off: for $n=0$ the branch
   $k_1h \in (0,\pi/2)$ is reachable at any frequency.
2. **Long wavelengths see the half-space**, short ones see the layer:
   as $f \to 0$, $c \to \beta_2$; as $f \to \infty$, $k_1h \to 0$ and
   $c \to \beta_1$.
3. **A fast layer supports no trapped Love mode.** If $\beta_1 > \beta_2$ the
   interval $(\beta_1,\beta_2)$ is empty and the equation has no solution: the
   motion in the layer is evanescent rather than oscillatory, energy leaks away
   into the half-space, and nothing is trapped. The demonstration returns `nan`
   for this case. This mirrors the hidden-layer blindness of first-arrival
   refraction in
   [06-10-01 Refraction Survey Geometry and Travel-Time Interpretation](../../06-seismology/10-refraction-and-near-surface-seismology/01-refraction-basics.md).

### 3.3 The depth sensitivity kernel

Take the exact relation $\omega^2 = \left[\int\mu(v')^2\mathrm dz +
k^2\int\mu v^2\mathrm dz\right]\big/\int\rho v^2\mathrm dz$, obtained by
multiplying the equation of motion by $v$ and integrating. It is equivalent to

$$k^2 = \frac{\omega^2\int\rho v^2\mathrm dz - \int\mu(v')^2\mathrm dz}
{\int\mu v^2\mathrm dz}
\equiv \frac{N}{I},$$

and this functional is **stationary** at the true eigenfunction: perturbing
$v \to v + \delta v$ gives
$\delta(k^2) = (2/I)\int\delta v\left[\omega^2\rho v + (\mu v')' - k^2\mu v\right]
\mathrm dz = 0$ by the equation itself. This is what makes first-order
perturbation theory legitimate.

So the only explicit dependence on the model is through $\mu$:
$\delta N = -\int\delta\mu\,(v')^2\mathrm dz$ and $\delta I = \int\delta\mu\,v^2
\mathrm dz$. With $N = k^2I$,

$$\delta(k^2) = \frac{\delta N\, I - N\,\delta I}{I^2}
= -\,\frac{\int\delta\mu\left[(v')^2 + k^2v^2\right]\mathrm dz}{I}.$$

At fixed frequency $c = \omega/k$, so $\delta c/c = -\delta k/k = -\delta(k^2)
/(2k^2)$, and therefore

$$\boxed{\;\frac{\delta c}{c} = \int_0^\infty \frac{\delta\mu(z)}{\mu(z)}\,
K(z)\,\mathrm dz, \qquad
K(z) = \frac{\mu(z)\left[(v')^2 + k^2v^2\right]}
{2k^2\displaystyle\int_0^\infty \mu v^2\,\mathrm dz}\;}.$$

Three remarks are worth stating before any number.

- The kernel is **not normalised to one**, and it need not be positive
  everywhere. Its integral is $\int K = \tfrac{1}{2}\,c^2\int\rho v^2/
  \int\mu v^2$, which equals $\tfrac12$ only in special cases; the fraction of the
  kernel above a depth is the meaningful quantity, not the value of $K$ itself.
- Because $\mu = \rho\beta^2$, a relative velocity perturbation obeys
  $\delta\mu/\mu = 2\,\delta\beta/\beta$ at constant density. A **1% velocity**
  increase over the whole layer is therefore a **2%** perturbation of $\mu$, and
  in the confined limit ($v \approx$ constant in the layer) it changes $c$ by
  **1%** — as it must, since $c \to \beta_1$.
- The demonstration verifies the kernel against an exact finite difference of the
  dispersion equation, and the agreement is at the level of the second-order term
  ($\sim10^{-5}$ relative for $\epsilon = 10^{-5}$).

### 3.4 Why thickness and velocity trade against each other

In the long-wavelength limit $\lambda \gg h$ the mode samples the layer as a thin
perturbation, and the first-order effect of the layer on the half-space velocity
enters through the **product of thickness and modulus contrast**,
$h(\mu_1 - \mu_2)$. Two models with different $h$ and compensating $\beta_1$
therefore produce almost the same curve: the inversion has a **valley**, not a
minimum. Section 4 measures the width of that valley, and the result is a
statement about the data, not about the algorithm:

- with a band that reaches the confining regime, no acceptable alternative model
  exists beyond about $\pm10\%$ in thickness (measured: a $0.5\ \mathrm{m}$ change
  in a $5\ \mathrm{m}$ layer with a compensating velocity deviates by
  $4.7$–$5.1\%$ over $4$–$128\ \mathrm{Hz}$);
- with a band entirely in the long-wavelength regime, alternatives with
  **three times** the thickness (or a fifth of it, at $55\ \mathrm{m\,s^{-1}}$)
  reproduce the curve to better than $1\%$.

The remedy is not a better inversion. It is more information: a wider band, a
higher mode, an independent $v_s$ measurement, or a borehole.

## 4. Physical interpretation

**The kernel is wavelength-scaled but its depth is not a fixed fraction of
$\lambda$.** For the teaching model ($\beta_1 = 180$, $\rho_1 = 1800$,
$h = 5\ \mathrm{m}$ over $\beta_2 = 400\ \mathrm{m\,s^{-1}}$,
$\rho_2 = 2000\ \mathrm{kg\,m^{-3}}$) the demonstration measures the depth
containing half the kernel:

| $f$ (Hz) | $\lambda$ (m) | $z_{50}$ (m) | $z_{50}/\lambda$ | fraction in the layer |
|---|---|---|---|---|
| 8 | 39.92 | 4.88 | 0.122 | 0.517 |
| 16 | 13.14 | 2.00 | 0.152 | 0.949 |
| 32 | 5.84 | 1.49 | 0.255 | 0.994 |
| 64 | 2.84 | 1.38 | 0.485 | 0.999 |
| 128 | 1.41 | 1.34 | 0.953 | 1.000 |

The ratio $z_{50}/\lambda$ spans a factor of eight across one decade. At
$8\ \mathrm{Hz}$ the mode is fast ($\lambda = 39.9\ \mathrm{m}$, eight times the
layer thickness), only $0.517$ of the kernel lies inside the layer, and the
sensitivity that remains is smeared over tens of metres. At $128\ \mathrm{Hz}$ the
mode is confined ($\lambda = 1.41\ \mathrm{m}$, *less* than the layer thickness),
the layer holds all of the kernel, and $z_{50}$ saturates at $0.27\,h$ — a fraction
of the **layer**, not of the wavelength. Any rule of thumb that quotes one number
for "the depth of a surface-wave measurement" is quoting the middle of this table
and should be replaced by the kernel.

**Two limits worth memorising.** $\int K\,\mathrm dz$ measures the whole-model
sensitivity: it falls from $0.833$ at $8\ \mathrm{Hz}$ to $0.502$ at
$128\ \mathrm{Hz}$. The limit $0.5$ is exact in the confined regime: there
$v \approx$ constant in the layer and the half-space contributes nothing, so
$\int K = c^2\int\rho v^2/(2\int\mu v^2) \to c^2/(2\beta_1^2) \to \tfrac12$. The
long-wavelength value exceeds it because the half-space then holds a large share
of the displacement without holding a corresponding share of the elastic energy.

**Mode content.** At $128\ \mathrm{Hz}$ the reference model has
$c_0 = 180.44$ and $c_1 = 184.06\ \mathrm{m\,s^{-1}}$, closely spaced because
$f$ is just above the first cut-off $f_{c,1} = 126.64\ \mathrm{Hz}$. A model that
fits the fundamental but not the higher modes is detectable
($c_0 = 161.62$, $c_1 = 169.11$ for the best $h = 3\ \mathrm{m}$ alternative),
which is precisely why multichannel acquisition records higher modes rather than
trying to suppress them.

**Group versus phase velocity.** A measured dispersion curve is normally a phase
velocity obtained from the phase of the cross-spectrum between receivers. Where
the curve is steep the group velocity differs strongly from the phase velocity,
and a time-domain "arrival" will not coincide with $c(f)$. Reporting which one
was measured is part of the measurement.

## 5. Worked examples

### Example 1 — Rayleigh speed from a Poisson's ratio

For $\nu = 0.25$, $\alpha/\beta = \sqrt{2(1-0.25)/(1-0.5)} = \sqrt{3} = 1.73205$.
Solving $(2-\zeta^2)^2 = 4\sqrt{1-\zeta^2/3}\sqrt{1-\zeta^2}$ in $(0,1)$ gives the
last root of the sextic:

$$\zeta = 0.91940169, \qquad
c_R = 0.919402\,\beta .$$

The demonstration reports the same value from both the equation and the sextic, and
for other ratios: $\zeta = 0.91099589$ ($\nu = 0.20$), $0.93252591$
($\nu = 1/3$), $0.94219543$ ($\nu = 0.40$). With $\beta = 200\ \mathrm{m\,s^{-1}}$
the Rayleigh speed is $183.88\ \mathrm{m\,s^{-1}}$. Because $c_R < \beta$ always,
a surface-wave measurement can never be read as an S-wave velocity directly — the
$0.9194$ factor is part of the interpretation.

### Example 2 — a Love mode by hand

The teaching model at $f = 16\ \mathrm{Hz}$ has $c = 210.208\ \mathrm{m\,s^{-1}}$.
Check it against the dispersion equation:

$$\omega = 2\pi(16) = 100.531\ \mathrm{rad\,s^{-1}},$$
$$k_1 = 100.531\sqrt{\frac{1}{180^2}-\frac{1}{210.208^2}}
= 100.531\sqrt{3.08642\times10^{-5}-2.26310\times10^{-5}}
= 0.288465\ \mathrm{rad\,m^{-1}},$$
$$k_1h = 0.288465\times5 = 1.44232\ \mathrm{rad} \in (0,\pi/2) \;\Rightarrow\;
\text{fundamental},$$
$$k_2 = 100.531\sqrt{\frac{1}{210.208^2}-\frac{1}{400^2}} = 0.406883,$$
$$B = \frac{\mu_2k_2}{\mu_1k_1}
= \frac{(2000)(400^2)(0.406883)}{(1800)(180^2)(0.288465)} = \frac{1.3021\times10^{8}}
{1.6826\times10^{7}} = 7.7395,$$
$$\tan(k_1h) = \tan(1.44232) = 7.7395 .\;✔$$

The residual printed by the demonstration is $7\times10^{-15}$.

### Example 3 — kernel sensitivity and the thickness trade-off

**Kernel.** At $16\ \mathrm{Hz}$ the layer holds $0.949$ of a kernel whose
integral is $0.6607$, so $\int_{\text{layer}}K\,\mathrm dz = 0.627$. A 1% increase
of $\beta_1$ in the layer is $\delta\mu/\mu = 2\%$, hence

$$\frac{\delta c}{c} = 2(0.01)(0.627) = 1.25\%,$$

which is the demonstration's value and agrees with an exact finite difference to
$10^{-5}$ relative. Note that the same 1% velocity change at $8\ \mathrm{Hz}$ moves
$c$ by only $0.86\%$: the layer is a smaller fraction of what the mode samples.

**Trade-off.** Assume a borehole gives $\beta_1$ with a 5% error. Fitting the
thickness to the same dispersion curve gives

| assumed $\beta_1$ (m/s) | fitted $h$ (m), 4–16 Hz | fitted $h$ (m), 4–128 Hz |
|---|---|---|
| 171.00 | 4.576 | 4.534 |
| 180.00 | 5.000 | 5.000 |
| 189.00 | 5.469 | 5.515 |

A 5% velocity error becomes a $9$–$10\%$ thickness error, and **the wider band does
not help**: the trade-off is between parameters, not a shortage of data. Only an
independent measurement of one of them breaks it.

## 6. Assumptions and regime of validity

1. **Horizontally layered, isotropic, laterally homogeneous** along the spread.
   A dipping interface or a lateral velocity change makes $c(f)$ a mixture of
   different structures along the line — the usual "1-D inversion of 2-D data"
   error, which
   [06-10-03 First-Arrival Tomography](../../06-seismology/10-refraction-and-near-surface-seismology/03-tomography-refraction.md)
   quantifies for the refraction case.
2. **Small strain, linear elasticity.** Surface-wave strains are small even for a
   sledgehammer source, unless the ground is at the onset of failure.
3. **$c < \beta$ in the half-space for a trapped mode**, hence a slow layer over a
   fast half-space. A fast surface layer over a slow half-space supports no
   trapped Love mode (Section 3.2, measured) and leaks; a *hidden* fast layer is
   invisible to the method in the same way a hidden slow layer is invisible to
   refraction.
4. **The half-space is deep enough** to be treated as infinite. If a rigid
   reflector sits within a wavelength, use a three-layer model.
5. **Density is imperfectly constrained.** The kernel responds to $\mu = \rho
   \beta^2$; almost all surface-wave practice fixes $\rho$ from another source and
   interprets the result as $\beta$. The velocity–density trade-off is weaker than
   the thickness–velocity one but not zero.
6. **Anelasticity is neglected.** Material damping broadens and attenuates the
   curve; the phase velocity of the *elastic* mode is what the equation above
   gives. Attenuation measurements are a separate observable
   ([05-04-06 Attenuation and Dispersion in Rocks](../../05-core-geophysics/04-rock-physics/06-attenuation-dispersion-rock.md)).
7. **Noise and mode misidentification.** Picking a higher mode as the
   fundamental, or picking the group-velocity envelope as the phase velocity, is
   the commonest practical failure; both produce a smooth, plausible, wrong curve.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| phase velocity | $c$ | $\mathrm{m\,s^{-1}}$ | $\omega/k$ |
| frequency | $f$ | Hz | $\omega/2\pi$ |
| wavelength | $\lambda$ | m | $c/f$ |
| wavenumber | $k$ | $\mathrm{rad\,m^{-1}}$ | $\omega/c$ |
| layer wavenumber | $k_1$ | $\mathrm{rad\,m^{-1}}$ | $\omega\sqrt{\beta_1^{-2}-c^{-2}}$ |
| thickness | $h$ | m | |
| shear modulus | $\mu$ | Pa | $\rho\beta^2$ |
| kernel | $K$ | $\mathrm{m^{-1}}$ | $\int K\,\mathrm dz$ dimensionless |
| cut-off frequency | $f_{c,n}$ | Hz | $n\pi/(h\sqrt{\beta_1^{-2}-\beta_2^{-2}})$ |

Two checks that catch most algebra errors: $k_1h$ must be dimensionless (it is
an angle, so a solution outside $(n\pi, n\pi+\pi/2)$ is on the wrong branch), and
$\int K\,\mathrm dz$ must be dimensionless and of order unity (it is exactly
$1/2$ in the confined limit).

## 8. Python demonstration

`code/surface_wave_demo.py` implements the whole chain and prints labelled results
with units. It:

1. solves the Rayleigh equation and the classical sextic for four Poisson's
   ratios, verifying that the two agree to eight decimals, and prints the surface
   displacement ratio $|u_x/u_z|$;
2. computes the exact Love dispersion of the teaching model, the higher-mode
   cut-offs ($126.64$ and $253.29\ \mathrm{Hz}$), the mode curves at seven
   frequencies, and the residual of the dispersion equation at four roots
   ($10^{-11}$ or better);
3. derives and evaluates the depth kernel, its cumulative, $z_{50}/\lambda$, and
   verifies it against exact finite differences;
4. measures the thickness–velocity ridge in three bands and shows the ridge width
   is a property of the data;
5. reports the inverse configuration ($\beta_1 > \beta_2$) returning `nan`, that
   is, no trapped mode.

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and runs in under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-seismic-surface-wave-nearsurface-exercises.md`](./exercises/02-seismic-surface-wave-nearsurface-exercises.md)
and
[`exercises/02-seismic-surface-wave-nearsurface-solutions.md`](./exercises/02-seismic-surface-wave-nearsurface-solutions.md).

- **★** Compute $c_R$ for $\nu = 1/3$ and $\beta = 250\ \mathrm{m\,s^{-1}}$.
- **★** Compute the first three cut-off frequencies for $h = 3\ \mathrm{m}$,
  $\beta_1 = 150$, $\beta_2 = 350\ \mathrm{m\,s^{-1}}$.
- **★★** Verify a Love root at $32\ \mathrm{Hz}$ for the teaching model by hand,
  as in Example 2, and state the branch index.
- **★★** Use the measured kernel table to convert a 2% velocity change in the top
  metre into a phase-velocity change at $16$ and $64\ \mathrm{Hz}$.
- **★★★** Design a band that would make the ridge of Section 3.4 narrow, and state
  the tolerance you would claim.

## Mastery checkpoint
Complete this without notes:

> Three Love-wave phase velocities are measured over a two-layer ground:
> $c = 319.3$, $210.2$ and $187.0\ \mathrm{m\,s^{-1}}$ at $8$, $16$ and
> $32\ \mathrm{Hz}$. **(a)** Compute $\lambda$ for each and say which measurement
> constrains the shallower depth. **(b)** State the depth range the $16\ \mathrm{Hz}$
> point constrains, using the kernel table. **(c)** A colleague proposes a
> $10\ \mathrm{m}$ thick layer at $200\ \mathrm{m\,s^{-1}}$ over a
> $400\ \mathrm{m\,s^{-1}}$ half-space. Check the three predictions against the
> data and decide. **(d)** State the thickness–velocity non-uniqueness in one
> sentence and name one measurement that would break it. **(e)** State what the
> method cannot see at all, and why.

A worked version of (a)–(c) appears in the exercise solutions.

## Common pitfalls
1. **Quoting "depth = $\lambda/3$".** The measured $z_{50}/\lambda$ runs from
   $0.12$ to $0.95$ for one model, and it saturates at a fraction of the *layer*
   thickness at high frequency. Use the kernel.
2. **Inverting a single-mode, narrow-band curve and reporting a profile.** The
   ridge is wide exactly where near-surface surveys usually operate.
3. **Reading $c$ as $v_s$.** For a half-space $c_R = 0.9194\beta$ at
   $\nu = 0.25$, and in a layered medium the relation is not local.
4. **Suppressing higher modes.** They carry the shallowest and the most
   independent information.
5. **Treating the picked envelope as the phase velocity.** Dispersion curves are
   phase velocities; state which quantity was measured.
6. **Assuming the method sees a fast surface layer.** A fast layer over a slow
   half-space supports no trapped Love mode.
7. **Ignoring anelasticity when amplitudes are used.** Phase velocities are
   insensitive to modest attenuation; amplitudes are not.

## Related modules
- [10-05-01 EM Induction and Conductivity Meters](01-electromagnetic-induction-nearsurface.md) —
  a different physics with the same structure: a reading is a weighted depth
  average, and one reading is not a profile.
- [10-05-03 Thermal Methods for Shallow Subsurface Investigation](03-thermal-nearsurface.md) —
  the third near-surface method whose depth resolution is set by a diffusion
  length rather than a wavelength.
- [10-04 Near-Surface Seismic and Geotechnical Methods](../04-near-surface-seismic-and-geotechnical/README.md) —
  what an engineer does with a $v_s$ profile once it exists.
- [06-10 Refraction and Near-Surface Seismology](../../06-seismology/10-refraction-and-near-surface-seismology/README.md) —
  the MASW/SASW workflow, $V_{S30}$ and site classification.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — the systematic
  treatment of the ridge and of regularisation.
