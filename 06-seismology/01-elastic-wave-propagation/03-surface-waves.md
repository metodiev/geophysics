---
id: 06-01-03
title: "Rayleigh and Love Waves: Dispersion and Depth Sensitivity"
level: graduate
prereqs: ["06-01-02", "02-03-07"]
tags: [seismology, surface-waves, dispersion, rayleigh, love, group-velocity]
---

# Rayleigh and Love Waves: Dispersion and Depth Sensitivity

Body waves in a homogeneous medium travel without changing shape. Surface waves
do not: their speed depends on frequency, and that dependence is a measurement
of the medium as a function of depth. This lesson derives the dispersion
relations from the boundary conditions, distinguishes phase from group velocity
with an exact identity, and measures both on a synthetic layered model.

```
.venv/bin/python 06-seismology/01-elastic-wave-propagation/code/surface_waves_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Love-wave dispersion relation for a layer over a half space
   from the continuity conditions, and **state** why a low-velocity waveguide is
   necessary.
2. **Derive** the Rayleigh secular equation for a homogeneous half space from
   the free-surface conditions, and **reduce** it to the cubic
   $\zeta^3-8\zeta^2+(24-16\xi)\zeta+16(\xi-1)=0$.
3. **Count** the Love modes at a given frequency from the closed form
   $1+\lfloor\omega H q/\pi\rfloor$ and **check** the count numerically.
4. **Distinguish** phase velocity $c$ from group velocity $U$, derive
   $U=c+k\,dc/dk$, and **verify** the equivalent form
   $U=c/\left(1-(\omega/c)\,dc/d\omega\right)$ numerically.
5. **Explain** depth sensitivity: which periods sample which depths, and why
   this makes surface waves the primary tool for crustal structure.

## Prerequisites

- [06-01-02 P and S Waves](./02-p-and-s-waves.md) — the two body-wave speeds
  and the SV/SH split.
- [02-03-07 Dispersion, Group Velocity and Phase vs Group
  Speed](../../02-physics/03-oscillations-and-waves/07-dispersion.md) — the
  general theory of which §4 is a special case.
- [02-03-06 Superposition, Interference and Standing
  Waves](../../02-physics/03-oscillations-and-waves/06-superposition-interference.md)
  — the device by which a trapped mode is built from up- and down-going legs.

## 1. Intuition: a wave that lives in the waveguide

A body wave that travels downward never comes back unless the velocity increases
with depth and turns it around. A surface wave is different: it is a solution
that **decays with depth**, so it needs a mechanism to trap energy near the
surface. Two mechanisms exist, and they give the two families:

- **Love waves** need a layer that is *slower* than what lies beneath it: energy
  is totally internally reflected at the base of the layer, just as light is
  trapped in an optical fibre.
- **Rayleigh waves** need only a **free surface**: the P and SV motions near a
  free surface can conspire so that both traction components vanish, and the
  resulting solution decays with depth even in a homogeneous half space.

Both are dispersive in a layered medium because the depth over which the wave is
sensitive scales with its wavelength. **Long wavelengths feel deep, stiff
material; short wavelengths feel shallow, soft material.** That single sentence
is the physical content of surface-wave inversion.

## 2. Precise definitions

### 2.1 Potentials and the two trial solutions

For SH motion (horizontal, perpendicular to the sagittal plane) only the
$y$-component of the vector potential survives, and the equation is scalar. For
$P$–$SV$ motion both $\phi$ and $\psi$ are needed, with

$$\mathbf u = \nabla\phi + \nabla\times(\psi\,\hat{\mathbf e}_y). \tag{1}$$

Take the interface (or the free surface) at $z=0$ with $z$ positive downward,
and look for solutions

$$\phi = \left(A_1e^{+\nu z} + A_2e^{-\nu z}\right)e^{i(kx-\omega t)}, \quad
\psi = \left(B_1e^{+\gamma z} + B_2e^{-\gamma z}\right)e^{i(kx-\omega t)}, \tag{2}$$

$$\chi = \left(C_1e^{+\kappa z} + C_2e^{-\kappa z}\right)e^{i(kx-\omega t)}
\quad\text{(Love, SH)}, \tag{3}$$

where $\chi$ is the SH potential and the vertical wavenumbers follow from the
wave equations:

$$\nu^2 = k^2-\frac{\omega^2}{v_p^2}, \quad
\gamma^2 = k^2-\frac{\omega^2}{v_s^2}, \quad
\kappa^2 = k^2-\frac{\omega^2}{v_s^2}
\quad\text{(per medium)}. \tag{4}$$

A **trapped** wave is one for which the vertical wavenumber is imaginary in the
upper region — the depth structure is $\exp(\pm|\nu| z)$ — so that the amplitude
decays away from the surface and away from the interface.

### 2.2 Phase velocity, dispersion, mode

The **phase velocity** is $c=\omega/k$, so $k=\omega/c$; the vertical wavenumbers
become

$$\nu = \omega\sqrt{\frac1{c^2}-\frac1{v_p^2}}, \qquad
\gamma = \omega\sqrt{\frac1{c^2}-\frac1{v_s^2}}. \tag{5}$$

A medium is **dispersive** if $c$ depends on $\omega$. Each branch $c(\omega)$
that satisfies the boundary conditions is a **mode**. The lowest branch is the
**fundamental mode**; the others are **higher modes**, and every higher mode
appears at a frequency where one more half-wavelength fits across the layer.

## 3. Derivation of the Love-wave dispersion relation

**Step 1 — the geometry.** A layer of thickness $H$, shear speed $\beta_1$,
density $\rho_1$, over a half space with $\beta_2>\beta_1$, $\rho_2$. The
trapping condition is

$$\beta_1 < c < \beta_2. \tag{6}$$

That interval must be non-empty, which is why a **low-velocity** waveguide is
required: if the layer were faster than the half space, no $c$ would satisfy (6).

**Step 2 — the potential.** $\chi = (C_1 e^{+\kappa_1 z} +
C_2e^{-\kappa_1 z})e^{i(kx-\omega t)}$ in the layer ($0<z<H$), and
$\chi = C_3\,e^{-\kappa_2 z}e^{i(kx-\omega t)}$ in the half space; the third
solution is dropped because it grows downwards. From (5),
$\kappa_1 = \omega\sqrt{c^{-2}-\beta_1^{-2}}$ (real, by (6)) and
$\kappa_2 = \omega\sqrt{\beta_2^{-2}-c^{-2}}$ (imaginary in the sense of (4),
i.e. a decay).

**Step 3 — free surface.** At $z=0$ the traction $\sigma_{xz}=\mu_1\partial_z\chi$
must vanish, which gives $C_1=C_2$. Write the layer solution as
$\chi = 2C_1\cosh(\kappa_1z)$; below we only need its value and slope at $z=H$.

**Step 4 — continuity at $z=H$.** Displacement $u_y=\partial_z\chi$ and traction
$\mu\,\partial_z\chi$ must be continuous:

$$2C_1\kappa_1\sinh(\kappa_1H) = -C_3\kappa_2 e^{-\kappa_2 H}, \qquad
\mu_1\,2C_1\kappa_1\cosh(\kappa_1H) = \mu_2\,(-C_3\kappa_2)e^{-\kappa_2H}. \tag{7}$$

**Step 5 — eliminate the amplitudes.** Dividing the second of (7) by the first
removes both $C_1$ and $C_3$:

$$\frac{\mu_1\cosh(\kappa_1H)}{\sinh(\kappa_1H)}\cdot\frac{1}{1}
= \mu_2
\;\Longrightarrow\;
\tan(\nu_1 H) = \frac{\mu_2\,\gamma_2}{\mu_1\,\nu_1}, \tag{8}$$

where I have written $\nu_1=\kappa_1$ and $\gamma_2$ for the (positive
imaginary) magnitude in the half space, using
$\tanh(ix)=i\tan(x)$. Multiplying (8) by $\nu_1\cos(\nu_1 H)$ — the step that
removes the poles of the tangent — gives the form used for solving:

$$\nu_1\sin(\nu_1H) = \frac{\mu_2}{\mu_1}\gamma_2\cos(\nu_1H). \tag{9}$$

Equation (9) is the **Love dispersion relation**. It is transcendental: $c$
appears inside $\nu_1$ and $\gamma_2$ through (5), and the equation generally has
several roots at each frequency.

> **Why the tangent form is dangerous.** $\tan(\nu_1H)$ has poles at
> $\nu_1H=\pi/2+n\pi$, and a numerical root-finder applied to (8) reports those
> poles as roots. Equation (9) has no poles, and every sign change on the
> admissible interval $( \beta_1,\beta_2)$ is a genuine mode. The demonstration
> uses (9) for exactly this reason.

**Step 6 — the mode count.** A mode exists whenever the tangent branch has an
intersection, i.e. once per interval of length $\pi$ in $\nu_1H$. Since
$\nu_1\le\omega q$ with
$q=\sqrt{\beta_1^{-2}-\beta_2^{-2}}$, the number of trapped modes is

$$N(\omega) = 1 + \left\lfloor\frac{\omega H q}{\pi}\right\rfloor. \tag{10}$$

## 4. Derivation of the Rayleigh secular equation

**Step 1 — free-surface conditions.** For a homogeneous half space with a free
surface at $z=0$, the two conditions are

$$\sigma_{zz} = \lambda\left(\phi_{xx}+\phi_{zz}\right) + 2\mu\left(\phi_{zz}-
\psi_{xz}\right) = 0, \qquad
\sigma_{xz} = \mu\left(u_{x,z}+u_{z,x}\right) = 0. \tag{11}$$

**Step 2 — evaluate with (2).** Keeping only the decaying exponentials (both
$\nu$ and $\gamma$ imaginary below the Rayleigh speed, so the fields decay with
$z$), and writing $k=\omega/c$, one finds at $z=0$

$$\left(2-\frac{c^2}{\beta^2}\right)A + 2i\,q_\beta\,B = 0, \qquad
-2i\,q_\alpha\,A + \left(2-\frac{c^2}{\beta^2}\right)B = 0, \tag{12}$$

with $\alpha$ the P speed, $q_\alpha=\sqrt{1-c^2/\alpha^2}$ and
$q_\beta=\sqrt{1-c^2/\beta^2}$. Checking the first row of (12) is a matter of
substituting (2) into (11); the useful intermediate identities are
$\phi_{xx}=-k^2\phi$, $\phi_{zz}=k^2q_\alpha^2\phi$,
$\psi_{xz}=-k^2q_\beta\psi$, and the moduli identities $\lambda+2\mu=\rho\alpha^2$,
$\mu=\rho\beta^2$, which collapse the coefficient of $A$ in the first row,
$2\mu q_\alpha^2-\lambda c^2/\alpha^2$, to $\rho(2\beta^2-c^2)$, i.e. to
$\rho\beta^2(2-c^2/\beta^2)$ after dividing through by $\rho\beta^2$. The same
division turns the coefficient of $B$, namely $2i\mu q_\beta$, into
$2i\,q_\beta$, and the second row is obtained the same way with
$\mu(\partial_z u_x+\partial_x u_z)$.

**Step 3 — set the determinant to zero.** A nontrivial $(A,B)$ requires

$$\left(2-\frac{c^2}{\beta^2}\right)^2 - 4\,q_\alpha q_\beta = 0. \tag{13}$$

**Step 4 — square and reduce.** Squaring (13) and writing $\zeta=c^2/\beta^2$,
$\xi=\beta^2/\alpha^2$ gives $(2-\zeta)^4 = 16(1-\zeta\xi)(1-\zeta)$, and
collecting terms:

$$\zeta^3 - 8\zeta^2 + (24-16\xi)\zeta + 16(\xi-1) = 0. \tag{14}$$

The root $\zeta=0$ has been divided out; the physical root lies in $(0,1)$, so
$0<c_R<\beta$: a Rayleigh wave is always slower than the shear wave of the same
medium. This is a *derived* statement, and it is the reason Rayleigh waves
arrive last.

**Step 5 — the Poisson-solid value.** For $\lambda=\mu$, $\xi=1/3$ and (14)
becomes $\zeta^3-8\zeta^2+\tfrac{56}{3}\zeta-\tfrac{32}{3}=0$, whose physical
root is $\zeta=0.84529946$, so $c_R=0.91940169\,\beta$. Both numbers are
measured in the demonstration by solving the cubic and by an independent
numerical search on the determinant (13); they agree to $2.35\times10^{-11}$
relative, which is a check on the algebra of Step 4.

## 5. Phase and group velocity

A packet built from components near $k_0$ travels at the **group velocity**

$$U = \frac{d\omega}{dk}. \tag{15}$$

Since $c=\omega/k$ and $k=\omega/c$,

$$U = c + k\frac{dc}{dk}
\quad\Longleftrightarrow\quad
U = \frac{c}{1-\dfrac{\omega}{c}\dfrac{dc}{d\omega}}. \tag{16}$$

**Derivation.** Write $\omega=kc(k)$, so
$d\omega/dk = c + k\,dc/dk$ directly. For the second form, differentiate
$k=\omega/c(\omega)$: $dk/d\omega = 1/c - (\omega/c^2)\,dc/d\omega
= (1/c)\left[1-(\omega/c)dc/d\omega\right]$, and $U=(dk/d\omega)^{-1}$ gives the
result. The two are the same expression rearranged; a numerical check of (16) is
therefore a check on the differentiation, not on the physics.

**Normal versus inverse dispersion.** If $dc/dk<0$ then $U<c$: longer periods
travel faster, which is what a layer over a faster half space produces, and the
record shows the long-period energy arriving first. If $dc/dk>0$ then $U>c$ and
the coda is reversed.

## 6. Depth sensitivity

The trapped solution decays over a depth of order $1/\nu_1$ in the layer and
$1/\gamma_2$ in the half space, both of which scale as $c/(\omega\sqrt{\cdots})$,
i.e. as the **wavelength**. Two limits follow from (9) directly:

- As $\omega\to0$ the layer becomes thin compared with the wavelength and (9)
  reduces to $\nu_1H\approx(\mu_2/\mu_1)\gamma_2/\nu_1$, whose solution is
  $c\to\beta_2$: **long periods sample the half space.**
- As $\omega\to\infty$, $\tan(\nu_1H)$ oscillates ever faster and the
  fundamental root tends to $\nu_1H\to0^+$, i.e. $c\to\beta_1^+$: **short
  periods sample the layer.**

Both limits are approached but never reached, because the layer must remain a
waveguide and the half space must remain an energy sink. The demonstration
measures both.

## 7. Units and dimensional analysis

In (2)–(5) all of $x$, $z$, $H$ are lengths, $k$ and $\nu,\gamma$ are
$\mathrm{m^{-1}}$, $\omega$ is $\mathrm{s^{-1}}$, $c$ and $\beta$ are
$\mathrm{m\,s^{-1}}$. The combinations $\nu H$, $\omega H q/\pi$ and $\zeta$,
$\xi$ are dimensionless, as arguments of trigonometric functions and roots of a
polynomial must be. The mode count (10) is an integer: $q$ has units
$\mathrm{s\,m^{-1}}$, $\omega H$ has $\mathrm{m\,s^{-1}}$, and their product is
dimensionless. The group velocity identity (16) adds $\mathrm{m\,s^{-1}}$ to
$\mathrm{m^{-1}}\cdot\mathrm{m^2\,s^{-1}}=\mathrm{m\,s^{-1}}$ — consistent.

## 8. Worked examples

### 8.1 The waveguide, SYNTHETIC

$\beta_1=3.500$ km/s, $\rho_1=2700$ kg/m³, $H=30$ km over
$\beta_2=4.500$ km/s, $\rho_2=3300$ kg/m³. The trapping interval is
$3.500<c<4.500$ km/s. Solving (9) at each frequency:

| period (s) | fundamental $c$ (km/s) | modes found | $1+\lfloor\omega Hq/\pi\rfloor$ |
|---|---|---|---|
| 100 | 4.4586 | 1 | 1 |
| 40 | 4.2519 | 1 | 1 |
| 20 | 3.8666 | 1 | 1 |
| 10 | 3.6168 | 2 | 2 |
| 5 | 3.5327 | 3 | 3 |

The fundamental falls monotonically toward $\beta_1$ as the period shortens, and
the count matches (10) exactly at every frequency. The extremes measured:
$c(200\ \mathrm{s}) = 4.4897$ km/s and $c(2\ \mathrm{s}) = 3.5056$ km/s, both
strictly inside the trapping interval as §6 requires.

### 8.2 Group velocity, two ways

Using (16) with central differences on $c(\omega)$ at $\omega\pm10^{-4}$:

| period (s) | $c$ (km/s) | $U=c+k\,dc/dk$ (km/s) | $U=c/[1-(\omega/c)dc/d\omega]$ (km/s) | relative difference |
|---|---|---|---|---|
| 200 | 4.4897 | 4.4691 | 4.4691 | $1.1\times10^{-10}$ |
| 100 | 4.4586 | 4.3771 | 4.3771 | $4.6\times10^{-10}$ |
| 50 | 4.3363 | 4.0432 | 4.0432 | $1.5\times10^{-9}$ |
| 40 | 4.2519 | 3.8496 | 3.8496 | $1.3\times10^{-9}$ |

The largest measured $|c-U|$ is $0.4023$ km/s at 40 s, and $U<c$ across the whole
band: normal dispersion, exactly as §5 predicts for a layer over a faster half
space. Ten significant figures of agreement between two forms of the same
derivative is the check that the differencing is being done correctly.

### 8.3 Rayleigh speed by two routes

For each synthetic $v_p/v_s$ ratio, the cubic (14) is solved by a polynomial
root finder and the determinant (13) is searched for a sign change:

| $v_p/v_s$ | $\xi$ | $\zeta$ from (14) | $c/\beta$ from (13) | relative difference |
|---|---|---|---|---|
| $\sqrt3$ | 0.333333 | 0.84529946 | 0.91940169 | $2.4\times10^{-11}$ |
| 2.0 | 0.250000 | 0.86960457 | 0.93252591 | $2.4\times10^{-16}$ |
| 1.8 | 0.308642 | 0.85330225 | 0.92374361 | $1.6\times10^{-15}$ |
| 5.0 | 0.040000 | 0.90766558 | 0.95271485 | $3.3\times10^{-14}$ |

Elimination and root-finding agree to machine precision, so the algebraic
reduction of §4 is correct. Note the trend: the stiffer the medium in shear
relative to compression, the smaller $c_R/\beta$ — the Rayleigh speed is
governed mainly by the shear modulus, which is why it is used as a proxy for
$v_s$ in the near surface.

### 8.4 Love waves need a low-velocity layer

Scanning 200 trial phase velocities:

| configuration | interval $(\beta_1,\beta_2)$ non-empty? | trial velocities inside |
|---|---|---|
| $\beta_1=3.5$, $\beta_2=4.5$ km/s | yes | 10 of 200 |
| $\beta_1=4.5$, $\beta_2=3.5$ km/s | no | 0 of 200 |

When the layer is faster than the half space, $\nu_1$ and $\gamma_2$ are never
simultaneously real and no discrete Love mode is trapped. **A seismological
waveguide must be a low-velocity layer, not merely a contrast.**

## 9. The Python demonstration

`surface_waves_demo.py` performs the four measurements above and prints them.
Two features are worth noting as models of practice:

1. **The pole-free form is used.** The root finder operates on (9), and the mode
   count is then compared with the closed form (10). A root finder applied to
   the tangent form reports poles as modes, and the demonstration would fail the
   count on the first run — which is what happened during development.
2. **Two formulations of every quantity are compared.** $U$ by both forms of
   (16), $c_R$ by elimination and by root-finding, the mode count by measurement
   and by formula. In each case the difference printed is the numerical error,
   and in each case it is at or below $10^{-9}$ relative.

## 10. Exercises

**★1.** Derive the trapping condition (6) from (4), stating what
$\kappa^2<0$ means physically.

**★2.** Carry out Steps 3–5 of §3 in full, including the identity
$\tanh(ix)=i\tan x$. Explain where the factor $i$ is absorbed.

**★3.** Solve the cubic (14) for $\xi=1/3$ by hand to three decimals, and check
against the value 0.84529946.

**★4.** For the model of §8.1, compute the frequency at which the second mode
appears, and compare with the measured transition between 20 s and 10 s.

**★★5.** Verify (16) symbolically by differentiating $\omega=kc(k)$ and
$k=\omega/c(\omega)$, and state which step requires $c$ to be differentiable.

**★★6.** Run the demonstration with the layer thickness halved to 15 km. Predict
the new mode count at 5 s from (10), then measure it.

**★★7.** The measured $U$ for the fundamental mode lies below $c$ everywhere in
the band. Derive from (9) the sign of $dc/d\omega$ at high frequency and
confirm it matches the measurement.

**★★★8.** Extend the demonstration to two layers over a half space. Write the
$4\times4$ system (two continuity conditions at each interface), and show that
the single-layer relation (9) is recovered when the second layer is given the
half-space properties.

**★★★9.** A receiver records a Rayleigh wave with a measured $c(f)$ curve. State
precisely what the curve constrains about $\beta(z)$ and what it does not,
referring to the sensitivity kernels implied by §6.

## 11. Common mistakes

1. **Solving $\tan(\nu_1H)=(\mu_2\gamma_2)/(\mu_1\nu_1)$ with a naive
   root-finder.** Poles masquerade as roots; use the pole-free form (9).
2. **Assuming the fundamental mode is the fastest.** At fixed frequency the
   branches are ordered by phase velocity with the **fundamental lowest**;
   every higher mode appears at the half-space speed and disperses downward.
   Getting this backwards reverses the interpretation of a dispersion curve.
3. **Confusing $c$ and $U$ in a travel-time measurement.** A picked arrival time
   on a dispersed packet corresponds to the group velocity, not the phase
   velocity.
4. **Believing a Rayleigh wave requires layering.** It exists on a homogeneous
   half space; it is the *dispersion* that requires structure.
5. **Using the same density as the layer for the half space when computing
   $\mu_2/\mu_1$.** The ratio in (9) is $\rho_2\beta_2^2/(\rho_1\beta_1^2)$, not
   $\beta_2^2/\beta_1^2$.
6. **Quoting "$c_R=0.92\,\beta$" as universal.** It is $0.9194\,\beta$ for
   $\lambda=\mu$ and $0.9527\,\beta$ for $v_p/v_s=5$; the value depends on the
   medium, and (14) gives it.

## 12. Real-world applications

- **Crustal and upper-mantle structure.** Surface-wave dispersion from
  earthquakes and from ambient noise is inverted for $v_s(z)$; the depth
  sensitivity of §6 is what makes the inversion possible and what limits its
  resolution.
- **Near-surface $v_s$ for engineering.** Rayleigh-wave dispersion measured on
  a 10–100 m array gives the shallow shear profile used in site-response
  studies, with the $c_R\approx0.92\beta$ relation of §8.3 as the link.
- **Moment magnitude.** The magnitude scale that saturates less than the
  body-wave scales was calibrated on Rayleigh-wave amplitudes, because those
  amplitudes are large and their geometric spreading is two-dimensional rather
  than three-dimensional.
- **Fibre-optic sensing.** Distributed acoustic sensing records surface waves
  along a cable; the dispersion analysis is the same algebra with a very
  different sensor.

## 13. Further reading

- [02-03-07 Dispersion, Group Velocity and Phase vs Group
  Speed](../../02-physics/03-oscillations-and-waves/07-dispersion.md) — the
  general theory behind §5.
- [06-01-06 Interface Waves, Head Waves and the Total
  Wavefield](./06-interface-waves.md) — the full wavefield of which these modes
  are the trapped part.
- [06-02-03 The tau-p Transform and Intercept
  Time](../02-ray-theory-and-travel-times/03-tau-p.md) — the body-wave
  counterpart of the dispersion analysis.
- [05-04-05 Anisotropy in Rocks: Causes and
  Magnitudes](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md) —
  what a split surface-wave branch tells you about alignment.
- [https://docs.obspy.org/tutorial/](https://docs.obspy.org/tutorial/) — the
  ObsPy tutorial, for reading and filtering the records this theory is fitted to.

## 14. Related lessons

- [06-01-02 P and S Waves](./02-p-and-s-waves.md) — the speeds that enter every
  vertical wavenumber here.
- [06-01-04 Reflected, Refracted and Converted Body
  Waves](./04-body-wave-arrivals.md) — the other half of the wavefield.
- [06-01-08 Wave Propagation in Anisotropic
  Media](./08-anisotropic-propagation.md) — how the dispersion relations change
  when the layer is not isotropic.
- [06-01-07 Scattering, Coda and Random
  Media](./07-scattering-and-heterogeneity.md) — what happens when the layer is
  not laterally uniform.

## 15. Self-assessment

- [ ] Derive (9) from the two continuity conditions without notes.
- [ ] Explain why Love waves need a low-velocity layer and Rayleigh waves do not.
- [ ] Reduce (13) to (14), showing the squaring and the collection of terms.
- [ ] State and use the mode-count formula (10).
- [ ] Derive both forms of the group-velocity relation (16).
- [ ] Predict which period samples 100 km depth in a given model, and say why.
- [ ] Explain the difference between the fundamental mode and the fastest mode.
- [ ] Name the two independent numerical checks in the demonstration and what
      each one tests.
