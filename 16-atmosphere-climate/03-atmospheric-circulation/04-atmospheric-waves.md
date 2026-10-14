---
id: 16-03-04
title: "Atmospheric Waves: Rossby, Kelvin, Gravity Waves"
level: research
prereqs: ["16-03-01", "16-03-03", "02-06-07"]
tags: [atmosphere, climate, rossby-waves, kelvin-waves, gravity-waves, equatorial-dynamics]
---

# Atmospheric Waves: Rossby, Kelvin, Gravity Waves

Every large-scale atmospheric motion is a superposition of a small number of
wave types, and each type is defined by the **balance** that supports it and the
**restoring force** that drives it:

- **Rossby waves** exist because planetary vorticity varies with latitude. Their
  restoring mechanism is the gradient of $f$, their frequencies are low, and
  their phase propagates west while their energy propagates east.
- **Equatorial Kelvin waves** exist because the Coriolis parameter vanishes at
  the equator, which lets a non-dispersive, purely eastward disturbance exist
  there and nowhere else — a mode trapped within about
  $1.7\times10^3$ km of the equator in the demonstration's synthetic setting.
- **Internal gravity waves** exist because a stably stratified fluid resists
  vertical displacement. Their frequency depends only on the *direction* of the
  wavevector, not on its length, and their energy travels perpendicular to it.

This lesson derives all three dispersion relations from the same linearised
equations, and then does something the derivations cannot do for themselves: it
**verifies** each one numerically. The Rossby frequency is measured by
time-stepping the linear barotropic vorticity equation and is shown to converge
to the continuum dispersion relation as the grid is refined. The equatorial
dispersion relation is confirmed by showing that the Hermite structure functions
solve the meridional equation to the accuracy of the finite-difference second
derivative. Two of the three verifications are checks on the *algebra and the
code*; the third — comparing a predicted frequency with an observed one — is not
done here, and the lesson says so.

All models and data in this module are **SYNTHETIC**. Wavenumbers, equivalent
depths, stratification and background winds below are chosen teaching values
printed by [`code/atmospheric_waves_demo.py`](code/atmospheric_waves_demo.py).
Standard constants ($\Omega$, $a$, $g$) are used as constants.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the barotropic and baroclinic Rossby dispersion relation
   $\omega = -\beta k/(k^2+l^2+1/L_D^2)$ from the linearised vorticity equation.
2. **Compute** the phase speed, the group velocity and the stationary
   wavenumber, and **explain** why they require opposite signs of propagation.
3. **Verify** a dispersion relation numerically, and **demonstrate** the
   convergence of a finite-difference scheme to the continuum result.
4. **Derive** the equatorial Kelvin wave solution, including the trapping scale
   $\sqrt{c/\beta}$, and **prove** from the equations that it propagates eastward
   only.
5. **Use** the unified equatorial dispersion relation to classify the Kelvin,
   mixed Rossby-gravity, Rossby and inertia-gravity branches, and **check** the
   long- and short-wave limits.
6. **Derive** the internal gravity wave dispersion relation
   $\omega = N\cos\theta$ and the perpendicularity of the group velocity to the
   wavevector, and **compute** the vertical wavelength of a stationary mountain
   wave.
7. **State** what each numerical check in this lesson verifies and what it
   cannot verify.

## Prerequisites

- [16-03-01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets](01-global-circulation.md) —
  the Coriolis parameter, the Rossby number and the thermal wind.
- [16-03-03 Cyclones, Fronts and Severe Weather Dynamics](03-storms-and-fronts.md) —
  the baroclinic instability these waves organise and the Fourier normal-mode
  framework used here.
- [02-06-07 Geophysical Fluids](../../02-physics/06-fluid-mechanics/07-geophysical-fluids.md) —
  rotating-fluid kinematics, including the shallow-water equations.

## 1. Intuition: three restoring mechanisms

Take a fluid parcel in the atmosphere and displace it.

- **Vertically.** Buoyancy restores it, at a frequency related to the
  stratification $N$: this is the gravity wave branch.
- **Meridionally.** The local planetary vorticity changes, and conservation of
  potential vorticity generates a vorticity anomaly that advects the
  displacement: this is the Rossby wave branch, and it is intrinsically slow
  because $\beta$ is small.
- **At the equator.** The Coriolis parameter is zero, so meridional displacement
  generates no vorticity at leading order; the response is instead a
  special non-dispersive mode — the Kelvin wave.

The mathematical content of this lesson is that these three statements become
three dispersion relations, and the practical content is that each relation is
a *testable* prediction that a particular measurement can confirm or refute.

## 2. Definitions

| Term | Meaning used here |
|---|---|
| $\beta$ | $\mathrm{d}f/\mathrm{d}y = 2\Omega\cos\phi/a$ (midlatitude) or $2\Omega/a$ (equatorial $\beta$-plane) |
| $c = \sqrt{gH}$ | Gravity-wave speed in the shallow-water (equivalent-depth) description |
| $L_D$ | Deformation radius $NH/f$ or $\sqrt{gH}/f$ |
| $K_s = \sqrt{\beta/U}$ | Stationary wavenumber for a background wind $U$ |
| Hermite function | $\mathrm{e}^{-\lambda y^2/2}H_n(\sqrt{\lambda}y)$ with $\lambda = \beta/c$; the equatorial meridional structure |
| Poincaré / inertia-gravity | The high-frequency branch of the shallow-water system |
| Critical level | A height where the background wind equals the wave's phase speed, so the intrinsic frequency vanishes |

## 3. Rossby waves

### 3.1 Derivation

Linearise the barotropic vorticity equation on a $\beta$-plane about a uniform
westerly $U$ and look for a plane wave
$\psi = \hat\psi\mathrm{e}^{\mathrm{i}(kx+ly-\omega t)}$:

$$\left(\frac{\partial}{\partial t} + U\frac{\partial}{\partial x}\right)
\nabla^2\psi' + \beta\frac{\partial\psi'}{\partial x} = 0
\;\Longrightarrow\;
(-\mathrm{i}\omega + \mathrm{i}kU)(-(k^2+l^2))\hat\psi
+ \mathrm{i}\beta k\hat\psi = 0,$$

$$\boxed{\;\omega = kU - \frac{\beta k}{k^2+l^2+1/L_D^2}.\;}$$

The term $kU$ is the Doppler shift by the background flow; with $U = 0$ (or
working in the flow's frame) only the second term remains. The $1/L_D^2$ enters
when the medium is equivalent-barotropic with a deformation radius (a baroclinic
mode in disguise): it *reduces* the frequency by lengthening the effective
wavenumber.

### 3.2 Numbers

With $\beta(45^\circ) = 1.6187\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$ and
$L_D = 1000$ km, $l = 0$:

| $\lambda_x$ (km) | $k$ (m⁻¹) | $\omega$ (s⁻¹) | period (d) | $c_x$ (m s⁻¹) | $c_{gx}$ (m s⁻¹) |
|---|---|---|---|---|---|
| 20000 | $3.142\times10^{-7}$ | $-5.15242\times10^{-5}$ | 1.41 | $-164.01$ | $+164.01$ |
| 10000 | $6.283\times10^{-7}$ | $-2.57621\times10^{-5}$ | 2.82 | $-41.00$ | $+41.00$ |
| 5000 | $1.257\times10^{-6}$ | $-1.28810\times10^{-5}$ | 5.65 | $-10.25$ | $+10.25$ |
| 3000 | $2.094\times10^{-6}$ | $-7.72863\times10^{-6}$ | 9.41 | $-3.69$ | $+3.69$ |
| 2000 | $3.142\times10^{-6}$ | $-5.15242\times10^{-6}$ | 14.11 | $-1.64$ | $+1.64$ |
| 1000 | $6.283\times10^{-6}$ | $-2.57621\times10^{-6}$ | 28.23 | $-0.41$ | $+0.41$ |

Three features to read off, all of which matter downstream:

1. **Phase speed is westward, group velocity eastward**, and for $l=0$ they are
   equal in magnitude: $|c_x| = |c_{gx}| = \beta/k^2$. A downstream region can
   therefore be modulated by a wave whose crests are moving upstream.
2. **Longer waves are faster** — $c_x\propto\beta/k^2$. The planetary-scale
   response arrives first, which is why teleconnection patterns are
   planetary-scale (see [16-03-02](02-monsoons-and-regional.md) §7).
3. **Periods are long**: 1.4–28 days across this range of wavelengths, i.e. the
   Rossby branch lives in the weather-to-subseasonal band.

### 3.3 Stationary waves

If the flow has a background wind $U$, a wave is stationary when
$\omega = 0$, i.e. when $l^2 = \beta/U - k^2$. Writing $K_s = \sqrt{\beta/U}$,

| $U$ (m s⁻¹) | $K_s$ (m⁻¹) | $\lambda_s$ (km) | $m_\text{crit}$ at 45° |
|---|---|---|---|
| 5 | $1.7993\times10^{-6}$ | 3492 | 8.11 |
| 10 | $1.2723\times10^{-6}$ | 4939 | 5.73 |
| 15 | $1.0388\times10^{-6}$ | 6048 | 4.68 |
| 30 | $7.3455\times10^{-7}$ | 8554 | 3.31 |

The same numbers appeared in the teleconnection lesson as an assumption; here
they are a consequence of the dispersion relation.

## 4. Verification by finite differences

### 4.1 The experiment

The demonstration integrates

$$\frac{\partial\zeta}{\partial t} = -\beta\frac{\partial\psi}{\partial x},
\qquad \zeta = \nabla^2\psi,$$

on a doubly periodic 16 000 km square with a single initial plane wave
($k = 2\pi/\text{domain}$, $l = 0$), using centered differences, a discrete
Laplacian, a fourth-order Runge–Kutta step with $\Delta t = 600$ s, and phase
sampling with unwrapping to measure the frequency.

The discrete operators have their own dispersion relation: the centered
$x$-derivative has symbol $\mathrm{i}\sin(k\Delta x)/\Delta x$ and the periodic
five-point Laplacian has symbol $-(4/\Delta x^2)[\sin^2(k\Delta x/2) +
\sin^2(l\Delta x/2)]$, so the discrete frequency is

$$\omega_\text{FD} = -\frac{\beta\,\sin(k\Delta x)/\Delta x}
{(4/\Delta x^2)\left[\sin^2(k\Delta x/2)+\sin^2(l\Delta x/2)\right]}.$$

### 4.2 Results

| $n$ | $\Delta x$ (km) | $\omega_\text{meas}$ (s⁻¹) | $\omega_\text{FD}$ (s⁻¹) | $\omega_\text{cont}$ (s⁻¹) | error | amplitude drift |
|---|---|---|---|---|---|---|
| 32 | 500 | $-4.108683\times10^{-5}$ | $-4.108683\times10^{-5}$ | $-4.121934\times10^{-5}$ | $3.22\times10^{-3}$ | $-2.2\times10^{-9}$ |
| 64 | 250 | $-4.118623\times10^{-5}$ | $-4.118623\times10^{-5}$ | $-4.121934\times10^{-5}$ | $8.03\times10^{-4}$ | $-2.3\times10^{-9}$ |
| 128 | 125 | $-4.121106\times10^{-5}$ | $-4.121106\times10^{-5}$ | $-4.121934\times10^{-5}$ | $2.01\times10^{-4}$ | $-2.3\times10^{-9}$ |

The measured frequency reproduces the discrete prediction to all six printed
figures, and the error against the continuum dispersion relation falls by a
factor of 4.0 and 4.0 per refinement — exactly the $\Delta x^2$ signature of a
second-order scheme. The amplitude is conserved to two parts in $10^9$, so the
mode is neither growing nor decaying.

**What this verifies:** that the code solves the equation it claims to solve,
that the discretisation error behaves as advertised, and that the frequency
measurement is unbiased. **What it does not verify:** that the barotropic
vorticity equation describes the atmosphere, or that the framework of a
$\beta$-plane with a uniform $U$ is the right idealisation for a particular
observed wave. That requires an observed frequency, and it is a different kind
of statement.

## 5. Equatorial waves

### 5.1 Why the equator is special

The Coriolis parameter vanishes at the equator and changes sign across it. On
the equatorial $\beta$-plane, $f = \beta y$ with $\beta = 2\Omega/a
= 2.2892\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$, and the linear shallow-water
equations are

$$\frac{\partial u}{\partial t} - \beta y v = -g\frac{\partial h}{\partial x},
\qquad
\frac{\partial v}{\partial t} + \beta y u = -g\frac{\partial h}{\partial y},
\qquad
\frac{\partial h}{\partial t} + H\left(\frac{\partial u}{\partial x}
+ \frac{\partial v}{\partial y}\right) = 0 .$$

### 5.2 The Kelvin wave

Set $v \equiv 0$ and try $u, h\propto\mathrm{e}^{\mathrm{i}(kx-\omega t)}$.
The zonal momentum budget gives $\hat u = (gk/\omega)\hat h$ and the mass budget
gives $\hat h = (c/g)\hat u$; both hold simultaneously only if
$\omega = ck$ with $c = \sqrt{gH}$. The meridional momentum budget, which would
normally determine $v$, becomes a *structure* equation

$$\beta y u = -g\frac{\partial h}{\partial y}
\;\Longrightarrow\;
h \propto \exp\left(-\frac{\beta y^2}{2c}\right).$$

So the Kelvin wave is a **trapped** mode whose amplitude decays on the scale
$\sqrt{c/\beta}$, and it is **non-dispersive**: phase and group velocity are both
$+c$ at every wavenumber. Because $u\propto ck/\omega = +1 > 0$ is required for
consistency, only eastward propagation exists — the asymmetry is a consequence
of the equations, not a modelling choice.

The demonstration prints, for the equivalent depth $H$:

| $H$ (m) | $c$ (m s⁻¹) | $\sqrt{c/\beta}$ (km) | period at $k = 1/a$ (d) |
|---|---|---|---|
| 100 | 31.3 | 1169.7 | 14.79 |
| 200 | 44.3 | 1391.0 | 10.46 |
| 400 | 62.6 | 1654.2 | 7.40 |
| 800 | 88.6 | 1967.2 | 5.23 |

and the profile for $H = 400$ m: $1.0000$ at the equator, $0.9553$ at 500 km,
$0.8330$ at 1000 km, $0.6629$ at 1500 km, $0.4815$ at 2000 km, $0.1931$ at
3000 km. A least-squares fit of $\ln h$ against $-y^2$ returns an e-folding
scale of 1654.2239 km, matching $\sqrt{c/\beta}$ to four figures — a check that
the analytic structure is the exponential the theory claims.

### 5.3 All the equatorial modes

With $\mathrm{e}^{\mathrm{i}(kx-\omega t)}$ dependence, the meridional structure
functions are Hermite functions with eigenvalues $(2n+1)\beta/c$, and the
frequencies satisfy the **unified dispersion relation**

$$\boxed{\;\omega^3 - \omega\left(c^2k^2 + \beta c(2n+1)\right) - \beta c^2k = 0,\;}$$

whose branches are labelled by $n$: $n = -1$ is the Kelvin wave, $n = 0$ gives
the mixed Rossby-gravity and inertia-gravity modes, and $n \ge 1$ gives one
Rossby and two inertia-gravity branches each. With $c = 62.6$ m/s ($H = 400$ m)
and zonal wavenumber 1 ($k = 1.5696\times10^{-7}$ m⁻¹, wavelength 40 030 km):

| $n$ | branch | $\omega$ (s⁻¹) | period (d) | $c_x$ (m s⁻¹) |
|---|---|---|---|---|
| 0 | mixed Rossby-gravity | $-3.32694\times10^{-5}$ | 2.19 | $-211.96$ |
| 0 | $-ck$ branch | $-9.83234\times10^{-6}$ | 7.40 | $-62.64$ |
| 0 | inertia-gravity | $+4.31018\times10^{-5}$ | 1.69 | $+274.60$ |
| 1 | gravity (westward) | $-6.46570\times10^{-5}$ | 1.12 | $-411.93$ |
| 1 | Rossby | $-3.21295\times10^{-6}$ | 22.63 | $-20.47$ |
| 1 | gravity (eastward) | $+6.78699\times10^{-5}$ | 1.07 | $+432.40$ |
| 2 | gravity (westward) | $-8.42567\times10^{-5}$ | 0.86 | $-536.80$ |
| 2 | Rossby | $-1.94131\times10^{-6}$ | 37.46 | $-12.37$ |
| 2 | gravity (eastward) | $+8.61980\times10^{-5}$ | 0.84 | $+549.17$ |
| 3 | gravity (westward) | $-9.99672\times10^{-5}$ | 0.73 | $-636.89$ |
| 3 | Rossby | $-1.39149\times10^{-6}$ | 52.26 | $-8.87$ |
| 3 | gravity (eastward) | $+1.01359\times10^{-4}$ | 0.72 | $+645.76$ |

The Kelvin wave is the $n = -1$ root, $\omega = 9.83234\times10^{-6}$ s⁻¹
(period 7.40 d), which is the same number Section 3.2 predicted for
$k = 1/a$ — the two derivations agree by construction, which is the point of
checking them.

For $n=0$ the cubic factors exactly: $\omega = -ck$ is always a root, and the
other two solve $\omega^2 - ck\omega - \beta c = 0$. The Kelvin branch is the
**only one-directional mode** in the entire set: every other branch has a
westward partner at the same $|k|$.

### 5.4 Checking the two limits

Both classical approximations come out of the same cubic rather than being
assumed. Comparing the slow root with the long-wave Rossby form
$-ck/(2n+1)$, and the fast root with the inertia-gravity form
$\sqrt{c^2k^2+\beta c(2n+1)}$:

| $k$ (m⁻¹) | $n$ | Rossby root | $-ck/(2n+1)$ | ratio | gravity root | $\sqrt{c^2k^2+\beta c(2n+1)}$ | ratio |
|---|---|---|---|---|---|---|---|
| $1.571\times10^{-7}$ | 1 | $-3.215\times10^{-6}$ | $-3.280\times10^{-6}$ | 0.980 | $6.787\times10^{-5}$ | $6.632\times10^{-5}$ | 1.023 |
| $1.571\times10^{-7}$ | 2 | $-1.943\times10^{-6}$ | $-1.968\times10^{-6}$ | 0.987 | $8.620\times10^{-5}$ | $8.524\times10^{-5}$ | 1.011 |
| $3.142\times10^{-6}$ | 1 | $-6.565\times10^{-6}$ | $-6.560\times10^{-5}$ | 0.100 | $2.106\times10^{-4}$ | $2.074\times10^{-4}$ | 1.015 |
| $3.142\times10^{-6}$ | 2 | $-6.153\times10^{-6}$ | $-3.936\times10^{-5}$ | 0.156 | $2.172\times10^{-4}$ | $2.142\times10^{-4}$ | 1.014 |

At the long zonal wavelength the Rossby limit holds to 2%. At the shorter one the
ratio collapses to 0.10–0.16: **the long-wave limit has stopped applying**, and
knowing where a limit stops is part of using it. The inertia-gravity
approximation is accurate to 1–2.5% throughout, which is why it is the more
robust of the two.

Finally, the Hermite function is substituted into the meridional equation
directly at $n=2$, $k = 1.047\times10^{-6}$ m⁻¹: the residual is
$2.5\times10^{-8}$ of the term it balances, which is the finite-difference
truncation error. The dispersion relation is therefore confirmed numerically,
not merely asserted.

## 6. Internal gravity waves

### 6.1 Dispersion and geometry

For a stably stratified fluid with uniform $N$, linear internal gravity waves
satisfy

$$\boxed{\;\omega = \frac{N k_h}{\sqrt{k_h^2+m^2}} = N\cos\theta,\;}$$

where $\theta$ is the angle of the wavevector from the **vertical**. Two
consequences are unusual and worth stating carefully:

- The frequency does **not** depend on $|\mathbf{k}|$ at all, only on direction.
  There is no dispersion in the usual sense. The mode exists only for
  $\omega < N$; at $\omega = N$ the wave is evanescent.
- The **group velocity is perpendicular to the wavevector** (not merely
  non-parallel to the phase velocity). Differentiating,

$$c_{gx} = \frac{N m^2}{(k^2+m^2)^{3/2}},
\qquad
c_{gz} = -\frac{N k m}{(k^2+m^2)^{3/2}}
\;\Longrightarrow\;
\mathbf{c}_g\cdot\mathbf{k} = 0 .$$

For the demonstration's case ($\lambda_h = 200$ km, $\lambda_z = 800$ km,
$N = 10^{-2}$ s⁻¹):

| quantity | value |
|---|---|
| $\omega$ | $9.7014\times10^{-3}$ s⁻¹ (period 0.18 h) |
| $\mathbf{c}_p$ | $(308.81, 1235.22)$ m s⁻¹ |
| $\mathbf{c}_g$ | $(18.17, -72.66)$ m s⁻¹ |
| $\mathbf{c}_g\cdot\mathbf{k}$ | $0.000\times10^{0}$ (round-off) |
| $\mathbf{c}_p\cdot\mathbf{c}_g$ | $-8.41\times10^{4}$ m² s⁻² (not zero) |

The energy travels *along* the phase fronts while the crests travel across them;
when $k$ and $m$ have the same sign the vertical components of $\mathbf{c}_p$
and $\mathbf{c}_g$ have opposite signs — "phase up, energy down", which is why a
mountain can radiate momentum upward while its phase lines move downward.

### 6.2 Frequency is a direction, not a size

| $\theta$ (deg) | $\omega$ (s⁻¹) | period (h) | $\lambda_z/\lambda_h$ |
|---|---|---|---|
| 0 | $1.00000\times10^{-2}$ | 0.175 | infinite |
| 15 | $9.65926\times10^{-3}$ | 0.181 | 3.73 |
| 30 | $8.66025\times10^{-3}$ | 0.202 | 1.73 |
| 45 | $7.07107\times10^{-3}$ | 0.247 | 1.00 |
| 60 | $5.00000\times10^{-3}$ | 0.349 | 0.58 |
| 75 | $2.58819\times10^{-3}$ | 0.674 | 0.27 |
| 85 | $8.71557\times10^{-4}$ | 2.003 | 0.09 |

A horizontal wavevector ($\theta\to90^\circ$) gives $\omega\to0$; a vertical one
gives $\omega\to N$ and the wave ceases to exist. A 15° tilt produces a vertical
wavelength about four times the horizontal — the reason gravity waves are
observed as thin, nearly horizontal bands of temperature and wind perturbation.

### 6.3 The critical level

A stationary mountain wave in a wind $U$ has $m = N/U$. For
$U = 15\ \mathrm{m\,s^{-1}}$ and $N = 10^{-2}\ \mathrm{s^{-1}}$,
$m = 6.6667\times10^{-4}$ m⁻¹, so the vertical wavelength is 9.42 km. More
important than the number is what happens as $U$ varies with height: the
stationary condition $Uk = \omega$ forces $m \to \infty$ wherever $U\to0$, so
the vertical wavelength collapses and the wave is absorbed. That is a **critical
level**, and it is why gravity-wave drag depends on the *profile* of the wind
rather than on its value, and why climate models that omit it get the
stratospheric circulation wrong. The effect is not computed here; the
scaling $m = N/U$ is the entire content of the estimate.

## 7. Assumptions and regime of validity

1. **Linearity.** Every dispersion relation above is a linear result. Finite
   amplitude brings wave–wave interaction, breaking and saturation, which the
   relations do not describe.
2. **Uniform background.** $U$, $N$ and $H$ are held constant. Real refraction —
   by a jet, by the stratosphere — bends ray paths and can trap waves; the
   $\beta$-plane step is the leading behaviour only.
3. **Equivalent barotropic / shallow water.** The $1/L_D^2$ and $c=\sqrt{gH}$
   forms assume a single vertical mode. A multi-mode decomposition changes the
   speeds, not the sign structure.
4. **Doubly periodic, inviscid numerics** in Section 4: no sponge, no
   boundaries, and a scheme whose only error is dispersive (second order).
5. **The equatorial relations assume $f = \beta y$ exactly.** The true $2\Omega
   \sin\phi$ departs from this within tens of degrees, so the Hermite structure
   is a low-latitude idealisation.
6. **The Kelvin-wave derivation assumes $v \equiv 0$.** If $v$ were nonzero the
   mode would be a different branch; the assumption is part of the definition.
7. **Nothing here is compared with an observation.** Three numerical checks are
   performed, and all three test algebra, code or discretisation.

## 8. Worked examples

### Example 1 — Rossby frequency and speed

At $45^\circ$, $\beta = 2(7.292115\times10^{-5})(0.707107)/6.371\times10^6
= 1.6187\times10^{-11}\ \mathrm{m^{-1}s^{-1}}$. For
$\lambda_x = 5000$ km, $l=0$:

$$k = \frac{2\pi}{5\times10^6} = 1.2566\times10^{-6}\ \mathrm{m^{-1}},$$

$$\omega = -\frac{\beta}{k}
= -\frac{1.6187\times10^{-11}}{1.2566\times10^{-6}}
= -1.288\times10^{-5}\ \mathrm{s^{-1}},$$

period $2\pi/|\omega| = 4.878\times10^5$ s $= 5.65$ d,
$c_x = \omega/k = -10.25\ \mathrm{m\,s^{-1}}$,
$c_{gx} = \beta/k^2 = +10.25\ \mathrm{m\,s^{-1}}$. All three match the
demonstration's row.

### Example 2 — the Kelvin trapping scale

With $H = 400$ m, $c = \sqrt{9.81\times400} = 62.64\ \mathrm{m\,s^{-1}}$, and

$$\sqrt{\frac{c}{\beta}} = \sqrt{\frac{62.64}{2.2892\times10^{-11}}}
= \sqrt{2.736\times10^{12}} = 1.654\times10^6\ \mathrm{m} = 1654\ \mathrm{km}.$$

At $y = 1654$ km the amplitude is $\mathrm{e}^{-1} = 0.368$; the demonstration's
table shows $0.4815$ at 2000 km, i.e. already outside the nominal scale, which
is what an exponential does.

### Example 3 — gravity-wave geometry

$k = 2\pi/(2\times10^5) = 3.1416\times10^{-5}$ m⁻¹,
$m = 2\pi/(8\times10^5) = 7.8540\times10^{-6}$ m⁻¹:

$$\omega = \frac{10^{-2}\times3.1416\times10^{-5}}
{\sqrt{(3.1416\times10^{-5})^2+(7.8540\times10^{-6})^2}}
= \frac{3.1416\times10^{-7}}{3.2384\times10^{-5}}
= 9.7014\times10^{-3}\ \mathrm{s^{-1}},$$

$$c_{gx} = \frac{10^{-2}(7.8540\times10^{-6})^2}
{(3.2384\times10^{-5})^3} = 18.17\ \mathrm{m\,s^{-1}},$$

$$c_{gz} = -\frac{10^{-2}(3.1416\times10^{-5})(7.8540\times10^{-6})}
{(3.2384\times10^{-5})^3} = -72.66\ \mathrm{m\,s^{-1}},$$

and $c_{gx}k + c_{gz}m
= 18.17\times3.1416\times10^{-5} - 72.66\times7.8540\times10^{-6}
= 5.709\times10^{-4} - 5.707\times10^{-4}
= 2\times10^{-7}$, i.e. zero to the printed precision.

## 9. Python demonstration

[`code/atmospheric_waves_demo.py`](code/atmospheric_waves_demo.py) prints every
number above in five labelled sections: the Rossby dispersion, its phase and
group velocities and the stationary wavenumber; the finite-difference
verification with its convergence study; the Kelvin-wave speed, trapping scale
and profile fit; the full equatorial mode table with both limit checks and the
Hermite residual; and the gravity-wave direction table with the phase/group
geometry and the mountain-wave scale. It prints no figures, needs no network,
runs in under two seconds, and exits 0.

## 10. Exercises

Full sets with worked solutions are in
[`exercises/04-atmospheric-waves-exercises.md`](exercises/04-atmospheric-waves-exercises.md)
and
[`exercises/04-atmospheric-waves-solutions.md`](exercises/04-atmospheric-waves-solutions.md).

- **★** Compute $\beta$ at $30^\circ$ and $60^\circ$, and the Rossby period for
  $\lambda_x = 4000$ km with $l = 0$ at each.
- **★** For $H = 200$ m, compute $c$ and the Kelvin trapping scale, and the
  period of the $k = 1/a$ Kelvin wave.
- **★★** Derive $\mathbf{c}_g\cdot\mathbf{k} = 0$ for internal gravity waves
  from $\omega = Nk_h/\sqrt{k_h^2+m^2}$.
- **★★** Show that $\omega = -ck$ is always a root of the $n=0$ equatorial
  cubic, and find the other two roots in closed form.
- **★★★** Design a numerical experiment that distinguishes a numerical from a
  physical reason why a simulated Kelvin wave might decay as it propagates.

## 11. Common mistakes

1. **Reporting a group velocity with the sign of the phase velocity.** For
   Rossby waves they are opposite; for internal gravity waves they are
   perpendicular.
2. **Assuming dispersion in $\lvert\mathbf{k}\rvert$ for gravity waves.** The
   frequency depends only on direction.
3. **Forgetting that the Kelvin wave is one-directional.** A westward
   equatorial Kelvin wave is not a thing.
4. **Applying a long-wave limit outside its range.** Section 5.4's table shows
   the Rossby ratio collapsing from 0.98 to 0.10 with one change of wavenumber.
5. **Reading a convergence study as a physical validation.** Section 4.2 is the
   worked example of the difference.
6. **Treating $L_D$ as a constant.** It is $NH/f$: it varies with stratification,
   depth and latitude, and so does every wavelength built from it.
7. **Ignoring critical levels.** A wave's fate depends on the wind profile, not
   on the wind.

## Mastery checkpoint

Complete this without notes.

> At $45^\circ$ the atmosphere supports a barotropic Rossby wave of zonal
> wavelength 5000 km, an equatorial Kelvin wave on an equivalent depth of 400 m
> and an internal gravity wave with $\lambda_h = 200$ km,
> $\lambda_z = 800$ km in a stratification $N = 10^{-2}$ s⁻¹.
> **(a)** Compute $\beta$ at $45^\circ$ and the Rossby period, phase speed and
> group velocity.
> **(b)** Compute the Kelvin wave speed and trapping scale, and state why only
> one propagation direction is possible.
> **(c)** For the gravity wave, compute $\omega$ and the angle between the
> wavevector and the horizontal, then state the direction of energy propagation
> relative to the crests.
> **(d)** For a stationary mountain wave in a 15 m s⁻¹ wind, compute the
> vertical wavelength and explain what happens at a critical level.
> **(e)** State one quantity in this lesson that a numerical verification cannot
> check, and what kind of evidence could.

A worked version of (a)–(c) appears in the lesson-04
[solutions](exercises/04-atmospheric-waves-solutions.md).

## Common pitfalls

- **Measuring a frequency from a wrapped phase.** The demonstration unwraps
  before fitting; a single final phase is ambiguous modulo $2\pi$.
- **Quoting a dispersion relation without its background state.** $\beta$,
  $U$, $N$ and $H$ are part of the answer.
- **Confusing a critical level with a turning point.** At a critical level the
  intrinsic frequency vanishes and absorption occurs; at a turning point the
  vertical wavenumber goes imaginary and reflection occurs.
- **Using the equatorial $\beta = 2\Omega/a$ at midlatitudes** or the midlatitude
  $\beta = 2\Omega\cos\phi/a$ at the equator.
- **Assuming $c = \sqrt{gH}$ without saying what $H$ is.** It is an equivalent
  depth, not an ocean depth.

## Related modules

- [01 Global Circulation: Hadley, Ferrel, Polar Cells, Jets](01-global-circulation.md) —
  the eddy fluxes these waves carry.
- [02 Monsoons, Regional Circulation and Teleconnections](02-monsoons-and-regional.md) —
  the stationary-wave waveguide built from Section 3.3.
- [03 Cyclones, Fronts and Severe Weather Dynamics](03-storms-and-fronts.md) —
  the baroclinic instability whose cutoffs Section 3.4 of that lesson explains
  in the same language.
- [16-01 Atmospheric Structure and Thermodynamics](../01-atmospheric-structure-and-thermodynamics/README.md) —
  the stratification $N$ that sets the gravity-wave branch.
- [15-01 Physical Oceanography](../../15-oceanography-marine/01-physical-oceanography/README.md) —
  the same equatorial wave theory applied to the ocean, where $c$ is 200 times
  smaller and the modes are correspondingly slower.
- [20-02 Fourier and Spectral Analysis](../../20-signal-processing/02-fourier-and-spectral-analysis/README.md) —
  the Fourier normal-mode framework, dispersion relations and group velocity
  used throughout this lesson.
