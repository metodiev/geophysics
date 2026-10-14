---
id: 02-07-03
title: "Maxwell's Equations and Their Physical Meaning"
level: advanced
prereqs: ["02-07-01", "02-07-02", "01-06-07", "02-03-05"]
estimated_minutes: 90
tags: [maxwell-equations, displacement-current, wave-equation, diffusion-equation, gpr, magnetotellurics]
---

# Maxwell's Equations and Their Physical Meaning

## Learning objectives

By the end of this lesson you will be able to:

1. **State** all four Maxwell equations in differential and integral form, and
   give the physical meaning of each in one sentence.
2. **Explain** why the displacement current is forced by charge conservation, and
   what fails without it.
3. **Derive** the electromagnetic wave equation from Maxwell's equations, obtain
   $c = 1/\sqrt{\mu_0\varepsilon_0}$, and verify the derivation numerically.
4. **Derive** the **diffusion equation** $\nabla^2\mathbf E = \mu\sigma\,
   \partial\mathbf E/\partial t$ from the *same* equations in a conductor, and
   explain the precise approximation that turns one into the other.
5. **State** the single dimensionless ratio $\sigma/(\omega\varepsilon)$ that
   decides which behaviour you get, and evaluate it for magnetotellurics and for
   ground-penetrating radar.
6. **Verify** numerically that a plane wave satisfies all four equations to
   $O(h^2)$, that the discrete curl–curl operator has the expected dispersion,
   and that the diffusion solution's decay length matches
   $\delta = \sqrt{2/(\mu\sigma\omega)}$.
7. **Explain** why this wave-versus-diffusion dichotomy is the organising
   principle of all electromagnetic geophysics.

## Prerequisites

- [02-07-01 Electrostatics, Coulomb's Law and Electric Potential](./01-electrostatics.md)
  — Gauss's law and the potential.
- [02-07-02 Magnetostatics, Biot–Savart and Ampère's Law](./02-magnetostatics.md)
  — Ampère's law, and the displacement current that is missing there.
- [01-06-07 Vector Identities and Their Role in Geophysics](../../01-mathematics/06-multivariable-calculus/07-vector-identities.md)
  — $\nabla\times(\nabla\times\mathbf F) = \nabla(\nabla\cdot\mathbf F) - \nabla^2\mathbf F$,
  the identity that does all the work in the derivation.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](../03-oscillations-and-waves/05-wave-equation-derivation.md)
  — what a wave equation is, and how to read its solutions.

## 1. The four equations

In SI units, with $\mathbf E$ in V/m, $\mathbf B$ in T, $\mathbf H$ in A/m,
$\mathbf D$ in C/m² and $\mathbf J$ in A/m²:

| # | Differential form | Integral form | Physical meaning in one sentence |
|---|---|---|---|
| I | $\nabla\cdot\mathbf D = \rho$ | $\oint\mathbf D\cdot\mathrm d\mathbf A = Q_{\text{enc}}$ | Electric field lines begin and end on electric charge. |
| II | $\nabla\cdot\mathbf B = 0$ | $\oint\mathbf B\cdot\mathrm d\mathbf A = 0$ | Magnetic field lines never begin or end: there are no magnetic monopoles. |
| III | $\nabla\times\mathbf E = -\dfrac{\partial\mathbf B}{\partial t}$ | $\oint\mathbf E\cdot\mathrm d\boldsymbol\ell = -\dfrac{\mathrm d\Phi_B}{\mathrm dt}$ | A changing magnetic flux drives a circulating electric field. |
| IV | $\nabla\times\mathbf H = \mathbf J + \dfrac{\partial\mathbf D}{\partial t}$ | $\oint\mathbf H\cdot\mathrm d\boldsymbol\ell = I_{\text{enc}} + \dfrac{\mathrm d\Phi_D}{\mathrm dt}$ | Currents and changing electric flux drive a circulating magnetic field. |

Two of these are new only in their *time-dependent* parts:

- **III** is Faraday's law ([02-07-04](./04-em-induction.md)); the static version
  is $\nabla\times\mathbf E = \mathbf 0$, which is what makes the electrostatic
  potential possible.
- **IV** contains Maxwell's addition, the **displacement current**
  $\partial\mathbf D/\partial t$. Strip it and you recover Ampère's law.

Together with the constitutive relations for a linear, isotropic, dispersive-free
medium,

$$\mathbf D = \varepsilon\mathbf E, \qquad \mathbf B = \mu\mathbf H,
\qquad \mathbf J = \sigma\mathbf E , \tag{1}$$

the four equations determine $\mathbf E$ and $\mathbf B$ completely once sources
and boundary conditions are given.

## 2. Why the displacement current must exist

Two independent arguments, both worth knowing.

**Charge conservation.** Take the divergence of IV:
$\nabla\cdot(\nabla\times\mathbf H) = 0 = \nabla\cdot\mathbf J + \partial(\nabla\cdot\mathbf D)/\partial t$.
Using I, this is

$$\nabla\cdot\mathbf J + \frac{\partial\rho}{\partial t} = 0 , \tag{2}$$

which is exactly the continuity equation — charge is conserved. Without the
displacement current, IV would force $\nabla\cdot\mathbf J = 0$ always, i.e. it
would describe only steady currents in closed circuits and would fail the moment
a capacitor charges. **The displacement current is not an optional extra; it is
what makes Maxwell's equations consistent with conservation of charge.**

**Wave propagation.** Take the curl of III in a region with no free charge and no
current:

$$\nabla\times(\nabla\times\mathbf E) = -\frac{\partial}{\partial t}(\nabla\times\mathbf B)
= -\mu\frac{\partial}{\partial t}\left(\mu_0\varepsilon_0\frac{\partial\mathbf E}{\partial t}\right)
= -\mu\varepsilon\frac{\partial^2\mathbf E}{\partial t^2} ,$$

where the middle step used IV; without $\partial\mathbf D/\partial t$ it would be
zero, and no wave would exist. Maxwell's addition to Ampère's law is the reason
electromagnetic radiation is possible at all.

## 3. The wave equation in a non-conducting medium

Use the vector identity
$\nabla\times(\nabla\times\mathbf E) = \nabla(\nabla\cdot\mathbf E) - \nabla^2\mathbf E$.
In a charge-free, uniform medium, I gives $\nabla\cdot\mathbf E = \rho/\varepsilon = 0$,
so

$$\boxed{\ \nabla^2\mathbf E = \mu\varepsilon\,\frac{\partial^2\mathbf E}{\partial t^2}\ }
\qquad\text{and identically}\qquad
\nabla^2\mathbf B = \mu\varepsilon\,\frac{\partial^2\mathbf B}{\partial t^2} . \tag{3}$$

Both fields obey the same wave equation with speed

$$\boxed{\ v = \frac{1}{\sqrt{\mu\varepsilon}}\ } ,
\qquad
c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = 299\,792\,458\ \mathrm{m/s} . \tag{4}$$

The last number is not derived from the wave equation; it is the *defined* speed of
light, and in the SI the identity fixes $\varepsilon_0 = 1/(\mu_0c^2)$ given the
measured $\mu_0$. Historically (1861–1865) Maxwell derived $1/\sqrt{\mu_0\varepsilon_0}$
from purely electrical measurements and found it equal, within experimental error,
to the measured speed of light. That coincidence — between a quantity fixed by
electrostatic and magnetostatic experiments and the speed of light — is the single
strongest piece of evidence that light is electromagnetic. Every remote-sensing
method in this curriculum is downstream of it.

In a non-magnetic dielectric ($\mu = \mu_0$, $\varepsilon = \varepsilon_r\varepsilon_0$)
the speed falls to $v = c/\sqrt{\varepsilon_r}$: for $\varepsilon_r = 4$,
$v = 1.499\times10^8$ m/s. This is why a GPR velocity is reported directly as a
dielectric permittivity.

**Wave impedance.** Dividing the two plane-wave amplitudes gives
$E/H = \sqrt{\mu/\varepsilon} \equiv \eta$, in ohms; in vacuum
$\eta_0 = \sqrt{\mu_0/\varepsilon_0} = \mu_0c = 376.730\,314$ Ω. This ratio is
measured directly by a magnetotelluric survey — see lesson
[02-07-05](./05-em-waves.md).

## 4. The same equations in a conductor give a *diffusion* equation

Now keep the conduction current and drop only the displacement current. With
$\mathbf J = \sigma\mathbf E$, IV becomes $\nabla\times\mathbf H = \sigma\mathbf E$,
and the same curl-of-the-curl manipulation gives

$$\boxed{\ \nabla^2\mathbf E = \mu\sigma\,\frac{\partial\mathbf E}{\partial t}\ }
\qquad\text{and}\qquad
\nabla^2\mathbf B = \mu\sigma\,\frac{\partial\mathbf B}{\partial t} . \tag{5}$$

This is the **diffusion equation**, not a wave equation. Its solutions are
exponential decays in space with a $\sqrt t$ spreading in time; it has no
characteristic propagation speed, no reflection coefficient in the usual sense and
no wavefront. The coefficient $D \equiv 1/(\mu\sigma)$ is a diffusivity, with
units m²/s, and the natural time to diffuse a distance $L$ is

$$\tau_{\text{diff}} \sim \mu\sigma L^2 . \tag{6}$$

**The approximation, stated exactly.** Comparing the two terms that would appear
on the right of the general equation,

$$\underbrace{\mu\sigma\frac{\partial\mathbf E}{\partial t}}_{\text{conduction}}
\quad\text{versus}\quad
\underbrace{\mu\varepsilon\frac{\partial^2\mathbf E}{\partial t^2}}_{\text{displacement}} ,$$

and taking both fields to vary as $e^{i\omega t}$, the ratio of their amplitudes is

$$\boxed{\ \frac{|\mu\sigma\,i\omega E|}{|\mu\varepsilon\,(i\omega)^2E|}
= \frac{\sigma}{\omega\varepsilon}\ } . \tag{7}$$

So:
- $\sigma/(\omega\varepsilon) \gg 1$: the conduction term dominates and the field
  **diffuses**.
- $\sigma/(\omega\varepsilon) \ll 1$: the displacement term dominates and the field
  **propagates as a wave**.
- $\sigma/(\omega\varepsilon) \approx 1$: neither limit applies and neither simple
  equation is accurate; the full Helmholtz equation must be used.

The crossover frequency is $f_c = \sigma/(2\pi\varepsilon)$, which depends on both
conductivity and permittivity — a point often lost when the ratio is quoted as if
$\varepsilon$ were a constant of nature.

**The full time-harmonic equation, which covers both.** For a time dependence
$e^{i\omega t}$, Maxwell's equations give

$$\nabla^2\mathbf E = \left(i\omega\mu\sigma - \omega^2\mu\varepsilon\right)\mathbf E
\equiv -k^2\mathbf E ,
\qquad
k^2 = \omega^2\mu\varepsilon - i\omega\mu\sigma . \tag{8}$$

Writing $k = \beta - i\alpha$:

$$\alpha = \omega\sqrt{\frac{\mu\varepsilon}{2}}\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2}-1\right]^{1/2},
\qquad
\beta = \omega\sqrt{\frac{\mu\varepsilon}{2}}\left[\sqrt{1+\left(\frac{\sigma}{\omega\varepsilon}\right)^2}+1\right]^{1/2}. \tag{9}$$

As $\sigma/(\omega\varepsilon)\to0$, $\alpha\to(\sigma/2)\sqrt{\mu/\varepsilon}$ and
$\beta\to\omega\sqrt{\mu\varepsilon}$: a wave that attenuates slowly, with
$\lambda = 2\pi/\beta$ the wavelength. As $\sigma/(\omega\varepsilon)\to\infty$,
$\alpha\to\beta\to1/\delta$ with $\delta = \sqrt{2/(\mu\sigma\omega)}$, and the
"wavelength" equals $2\pi\delta$ — the field decays by a factor $e^{-2\pi}$ per
"wavelength", which is another way of saying it does not wave at all.

## 5. The dichotomy, quantified

Section 8 prints the ratio (7) for three media; the essential numbers are:

| Medium (nominal) | $\sigma$ (S/m) | $\varepsilon_r$ | $f_c$ (Hz) | $\sigma/(\omega\varepsilon)$ at 1 mHz | at 100 MHz |
|---|---|---|---|---|---|
| sea water | 4 | 81 | $8.88\times10^8$ | $8.9\times10^{11}$ | 8.9 |
| wet soil | 0.01 | 20 | $8.99\times10^6$ | $9.0\times10^{9}$ | 0.090 |
| dry granite | $10^{-3}$ | 6 | $3.00\times10^6$ | $3.0\times10^{9}$ | 0.030 |

The two columns are ten orders of magnitude apart. That is the whole story of
electromagnetic geophysics:

- **Magnetotellurics** operates from about $10^{-4}$ to $10^{3}$ Hz, where
  $\sigma/(\omega\varepsilon)\sim10^{9}$–$10^{12}$ — utterly diffusive. Its
  governing equation is (5), and its data are amplitude **and phase**, because a
  diffusion equation produces a complex response.
- **Ground-penetrating radar** operates from about $10^{7}$ to $10^{9}$ Hz in
  resistive ground, where $\sigma/(\omega\varepsilon)\lesssim1$ — wave-like. Its
  governing equation is (3)–(9), and its data are travel times and reflection
  coefficients.
- **In between** (roughly $10^{5}$–$10^{7}$ Hz in wet rock) there is a transition
  zone in which EM systems operate in a *lossy-dielectric* regime: propagation
  with significant attenuation, describable only by equations (8)–(9).

Two systems, one set of four equations, opposite limiting behaviour. If you
understand nothing else in this module, understand this.

The same statement has a time-domain form. A step change applied to the surface of
a conductor penetrates as $z\sim\sqrt{Dt}$ (no wavefront), whereas a step applied
to a lossless dielectric propagates at $v$ (with a wavefront). A seismic analogy
is close at hand: the wave regime is like a seismic arrival, the diffusive regime
is like heat conduction; and the reason magnetotellurics has to invert *complex*
impedances while GPR has to pick *times* is exactly this difference.

## 6. Physical interpretation: energy, flux and dissipation

Taking the dot product of the field equations with the fields and combining them
gives the **Poynting theorem**:

$$-\frac{\partial u}{\partial t} - \nabla\cdot\mathbf S = \mathbf J\cdot\mathbf E ,
\qquad
u = \frac12\left(\varepsilon E^2 + \mu H^2\right),
\qquad
\mathbf S = \mathbf E\times\mathbf H . \tag{10}$$

- $u$ is the electromagnetic energy density (J/m³).
- $\mathbf S$ has units $\mathrm{(V/m)(A/m)} = \mathrm{W/m^2}$: the energy flux
  density.
- $\mathbf J\cdot\mathbf E = \sigma E^2$ is the **ohmic dissipation** — the term
  that makes a conducting ground lossy and that the demo computes in lesson
  [02-07-04](./04-em-induction.md).

For a plane wave in a lossless medium, $S = E^2/\eta = \eta H^2$: the impedance
of the medium sets the flux for a given field amplitude.

In a geophysical setting the theorem is the bookkeeping behind the whole subject.
A transmitter radiates a Poynting flux into the ground; part of it is stored in the
fields, the rest is delivered to $\sigma E^2$ and becomes heat. A magnetotelluric
"signal" is the small fraction of the ionospheric energy flux that is transmitted
rather than reflected at the surface, and the reason it carries information is that
the *partition* between storage and dissipation depends on $\sigma$ and on
frequency. Two consequences follow immediately and are worth stating: penetration
is limited by dissipation rather than geometry, and a measurement of the fields
(the $\mathbf E$ and $\mathbf H$ of the surface) determines the flux, so the
energy budget of an EM survey is closed by the same quantities the survey records.

## 7. Assumptions and regime of validity

| Assumption | Where it enters | What breaks outside it |
|---|---|---|
| Linear constitutive relations (1) | Replacing $\mathbf D,\mathbf J$ by $\varepsilon\mathbf E,\sigma\mathbf E$ | Nonlinear materials; large fields (not a concern for the Earth) |
| Isotropic media | Constitutive relations are scalars | Anisotropy is real in shales and fractured rock; $\sigma$ becomes a tensor and the MT impedance becomes a full $2\times2$ tensor |
| Instantaneous response (no dispersion) | $\varepsilon$, $\mu$, $\sigma$ real constants | Induced polarisation; dielectric relaxation; $\sigma$ becomes complex and frequency-dependent |
| Neglect of the displacement current | Section 4 | Fails when $\sigma/(\omega\varepsilon)\lesssim1$ |
| Quasi-static (neglect of $\partial\mathbf B/\partial t$ in the induction equation? no) — precise statement: neglecting the *propagation* term means neglecting $\omega\mu\sigma L^2$-type retardation, valid when the diffusion time across the region is short compared with the period | Induction methods | At very large scales or very high frequencies, propagation and retardation matter |
| Charge neutrality in the bulk ($\rho = 0$) | Setting $\nabla\cdot\mathbf E = 0$ | Fails at charge separation interfaces (the electrical double layer); in practice relevant only within the screening length of a few nanometres to micrometres, except for SP sources |
| Classical (non-quantum) fields | Throughout | Not relevant at these length and energy scales |

**Charge neutrality deserves a warning.** In a homogeneous conductor the free
charge density decays with the dielectric relaxation time
$\tau_e = \varepsilon/\sigma$, which for rock is of order nanoseconds or faster.
The reason is beautiful: if charge accumulates, the resulting field drives a
current that cancels it. So electrostatic charge *cannot* be maintained inside a
conducting rock, and $\rho = 0$ is an excellent approximation in the bulk. This is
why every EM method is ultimately a measurement of the conductivity distribution,
not of any charge distribution.

## 8. Python demonstration

[`code/maxwell_demo.py`](./code/maxwell_demo.py) verifies every claim above.
Observed output:

```text
E = E0 exp(i(kz - wt)) xhat,  B = (E0/c) exp(i(kz - wt)) yhat
f = 1.0e+08 Hz, omega = 6.283185e+08 rad/s, k = 2.095845e+00 rad/m, lambda = 2.9979 m
c from 1/sqrt(mu0 eps0) = 299792458.000006 m/s   (exact: 299792458)
  dz (m)       Faraday        Ampere         div E         div B
 1.0e-02     9.016e-06     3.007e-14     0.000e+00     0.000e+00
 5.0e-03     2.254e-06     7.519e-15     0.000e+00     0.000e+00   ratios: 4.00 4.00
 2.5e-03     5.635e-07     1.880e-15     0.000e+00     0.000e+00   ratios: 4.00 4.00
```

```text
  k dx       -(D2)/k^2     (k dx)^2/12     ratio
0.015340  0.999980391011       1.961e-05
0.030680  0.999921565892       7.844e-05     4.000
0.061359  0.999686293098       3.137e-04     4.000
0.122718  0.998745644728       1.255e-03     3.998
```

```text
(a) fixed 15 points per wavelength, varying the Courant number c dt/dx:
    cfl =  1.00:  c_num/c = 1.000000000   error =  0.000e+00
    cfl =  0.50:  c_num/c = 0.994501948   error = -5.498e-03
    cfl =  0.25:  c_num/c = 0.993152743   error = -6.847e-03
(b) fixed cfl = 0.5, varying the sampling:
 points/period      k dx       c_num/c         error    error/(k dx)^2
            60   0.10472   0.999657247    -3.428e-04          0.031255
            30   0.20944   0.998628284    -1.372e-03          0.031271
            15   0.41888   0.994501948    -5.498e-03          0.031335
             8   0.78540   0.980541829    -1.946e-02          0.031544
```

```text
sigma = 0.0100 S/m (rho = 100 ohm m)
choose delta = 10.0 m => omega = 2 rho/(mu0 delta^2) = 1.591549e+06 rad/s, f = 2.533e+05 Hz, T = 3.948e-06 s
analytic delta = sqrt(2/(mu0 sigma omega)) = 10.000000 m
explicit scheme: D = 1/(mu0 sigma) = 7.9577e+07 m^2/s, dz = 0.5 m, dt = 1.0e-09 s, CFL = 0.3183 (stable below 0.5)
after 78960 steps (t = 7.8960e-05 s = 20 periods) the largest departure from the exact solution is 2.891e-03 V/m
  z (m)   |E| numeric   exp(-z/delta)   phase (deg)  +z/delta (deg)
   0.00      1.000040        1.000000        0.0000          0.0000
  10.00      0.367961        0.367879       57.3282         57.2958
  20.00      0.135744        0.135335      114.5473        114.5916
  30.00      0.049019        0.049787      171.1147        171.8873
  40.00      0.017752        0.018316     -121.7927        229.1831
least-squares decay length from the numerical solution: delta_measured = 9.888347 m
relative error vs the analytic formula delta = sqrt(2/(mu0 sigma omega)): 1.117e-02
```

```text
      medium  sigma (S/m)  eps_r    f_c (Hz)    s/(we) @ 1 mHz  s/(we) @ 100 MHz
   sea water            4     81  8.8766e+08         8.877e+11         8.877e+00
    wet soil         0.01     20  8.9876e+06         8.988e+09         8.988e-02
 dry granite        0.001      6  2.9959e+06         2.996e+09         2.996e-02
```

### What to observe

| Observation | Consequence |
|---|---|
| $1/\sqrt{\mu_0\varepsilon_0}$ reproduces $c$ to 6 parts in $10^{15}$ (round-off in the printed digits) | Equation (4) is satisfied; the residual is double-precision arithmetic, not physics |
| Faraday's and Ampère's residuals for the plane wave both fall by exactly 4.00 per halving of $h$, to $5.6\times10^{-7}$ and $1.9\times10^{-15}$ | Both curl equations are satisfied by the plane wave, to second order in the step |
| Ampère's residual is nine orders smaller than Faraday's and reaches $10^{-15}$ | The two terms of IV *cancel* to all available digits once $\partial\mathbf D/\partial t$ is included — direct numerical evidence that the displacement current is the missing term of Ampère's law |
| $\nabla\cdot\mathbf E$ and $\nabla\cdot\mathbf B$ are identically zero for the sampled plane wave | Equations I and II hold; the transverse geometry does it |
| The discrete second-difference eigenvalue deviates from $-k^2$ by exactly $(k\Delta x)^2/12$, confirmed to three digits | The discrete operator *is* the continuum operator plus a truncation term; this is the numerical dispersion line every EM modeller budgets for |
| The 1-D Yee scheme is exact at Courant number 1 and second-order accurate otherwise, with error $0.0313\,(k\Delta x)^2$ | Numerical dispersion is predictable, not mysterious; the "magic time step" is a 1-D special case |
| The time-domain solution of the diffusion equation reproduces $\exp(-z/\delta)$ to better than 1 % and recovers $\delta$ to 1.1 % by least squares | The diffusion equation derived in Section 4 is the equation the field actually obeys; the residual is the scheme's $O(\Delta z^2)$ error and the finite domain |
| The phase at depth is $+z/\delta$ radians, numerically equal to the amplitude exponent | In a diffusive field, decay and phase lag are the *same* number. This is why MT impedances are complex and why half-space MT phase is 45° |
| $\sigma/(\omega\varepsilon)$ spans $9\times10^{9}$ to $0.09$ across the table | The wave/diffusion dichotomy is not a subtlety; it is ten orders of magnitude wide |

> **Breaking exercise.** Modify the diffusion solver to use CFL = 0.6 and run it.
> Predict first what happens (recall the explicit scheme's stability limit is
> CFL $\le 1/2$), then observe. Then use the *frequency-domain* equation (8) with
> $\sigma/(\omega\varepsilon) = 1$ and compute $\alpha$ and $\beta$; confirm that
> the ratio $\alpha/\beta$ there is neither 0 nor 1, i.e. that this is a genuinely
> intermediate regime that neither of the two simple equations describes.

## 9. Common mistakes

1. **Forgetting the displacement current, then wondering where waves come from.**
   Ampère's law alone cannot produce a wave.
2. **Believing the wave equation is "the" consequence of Maxwell's equations.**
   In a conductor at low frequency the same equations give diffusion. Both are
   consequences; which one you get is decided by $\sigma/(\omega\varepsilon)$.
3. **Treating a diffusive EM signal like a seismic arrival.** There is no
   wavefront and no arrival time; reporting a "velocity" from an EM delay is a
   category error (see the $z\sim\sqrt{Dt}$ result).
4. **Using the lossless wavelength $\lambda = v/f$ in a lossy medium.** In the
   diffusive limit the *skin depth* is the meaningful length scale, and the
   nominal wavelength is $2\pi\delta$, which describes decay rather than
   oscillation.
5. **Mixing up $\mathbf B$ and $\mathbf H$ in the constitutive relation.** In SI,
   $\mathbf B = \mu\mathbf H$; the ratio $\mathbf E/\mathbf B$ then has units of
   m/s while $\mathbf E/\mathbf H$ has units of ohms. Both are used, in different
   contexts, and conflating them costs a factor $\mu$.
6. **Using a sign convention without stating it.** With $e^{+i\omega t}$ the
   propagation factor is $e^{-ikz}$; with $e^{-i\omega t}$ it is $e^{+ikz}$, and
   the sign of the imaginary part of the impedance flips. MT phases are quoted
   both ways in the literature. State the convention, always.
7. **Assuming $\sigma$ is a real constant.** Induced polarisation makes it
   complex and frequency-dependent; the imaginary part is the target of the IP
   method.
8. **Assuming the ground is non-magnetic.** Mostly true ($\mu_r \approx 1$), but
   magnetite-rich rocks can have $\mu_r$ measurably above 1, which changes the
   skin depth through the $\sqrt\mu$ factor.

## 10. Real-world applications

- **Ground-penetrating radar.** 10–1000 MHz in resistive ground;
  $\sigma/(\omega\varepsilon)\lesssim1$; the wave equation governs, and the data
  are reflection times and amplitudes
  ([10 GPR and Near-Surface](../../10-gpr-near-surface/README.md)).
- **Magnetotellurics.** $10^{-4}$–$10^{3}$ Hz; $\sigma/(\omega\varepsilon)\sim10^{11}$;
  the diffusion equation governs, and the data are complex impedances
  ([09 Electrical and EM Methods](../../09-electrical-em-methods/README.md)).
- **Controlled-source EM (TEM, FDEM, AEM).** Diffusive for most of the
  time–frequency window, with a wave-like early-time/air-wave component at large
  offsets.
- **Induction logging.** Diffusive at borehole frequencies; the sonde geometry is
  the loop problem of lesson [02-07-02](./02-magnetostatics.md).
- **Atmospheric and ionospheric electromagnetics.** The ionosphere is the region
  where the wave description is essential at ELF/VLF; the Earth–ionosphere
  waveguide is why Schumann resonances exist.
- **Every radio system.** The same equation (3) with $\varepsilon_r$ of air near
  1 governs communication, navigation and radar — the reason geophysical EM shares
  its instrumentation culture with radio engineering.
- **Optical and infrared remote sensing.** Equation (3) with $\sigma\approx0$
  over the whole visible spectrum; the substrate of lesson
  [02-10 Optics and Photometry](../10-optics-and-photometry/README.md).

## 11. Further reading

- **Griffiths, D. J. *Introduction to Electrodynamics* (4th ed., Cambridge
  University Press, 2017).** Chapters 7 and 9 derive the displacement current, the
  wave equation and the Poynting theorem in exactly this order. Level:
  intermediate.
- **Jackson, J. D. *Classical Electrodynamics* (3rd ed., Wiley, 1999).** The
  rigorous treatment of waves in conducting and dispersive media (§7.3–7.6),
  including the skin-depth limit and the Kramers–Kronig relations. Level:
  graduate.
- **Ward, S. H., & Hohmann, G. W. "Electromagnetic theory for geophysical
  applications", in Nabighian, M. N. (ed.) *Electromagnetic Methods in Applied
  Geophysics*, Vol. 1 (SEG, 1988).** The standard reference for the quasi-static
  approximation and its justification in the geophysical range. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics* (2nd
  ed., Cambridge University Press, 1990).** The EM chapters translate equations
  (3)–(9) into survey practice and units. Level: intermediate.
- **Chave, A. D., & Jones, A. G. (eds) *The Magnetotelluric Method: Theory and
  Practice* (Cambridge University Press, 2012).** The diffusive regime in full
  geophysical detail. Level: graduate.
- **Daniels, D. J. *Ground Penetrating Radar* (2nd ed., IET, 2004).** The wave
  regime in full engineering detail. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [04 Faraday's Law, Induction and Eddy Currents](./04-em-induction.md) — the
  physical content of equation III, and the diffusion equation (5) solved in the
  time domain.
- [05 Electromagnetic Waves, Impedance and Polarisation](./05-em-waves.md) — the
  wave regime in detail, and why $E/H$ is an ohm.
- [06 EM Fields in Conductors: Skin Depth and Diffusion](./06-em-in-conductors.md)
  — the diffusive regime in detail.
- [02-03-05 Deriving the Wave Equation from Continuum Physics](../03-oscillations-and-waves/05-wave-equation-derivation.md)
  — the scalar wave equation whose structure equation (3) reproduces.
- [01-09-02 The Heat Equation](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md)
  — the mathematics of equation (5), including the similarity solutions.
- [02-04-04 Young's Modulus, Poisson's Ratio and the Elastic Constants](../04-elasticity-and-continuum-mechanics/04-elastic-moduli.md)
  — the *elastic* wave speed $v=\sqrt{M/\rho}$, structurally identical to
  $v=1/\sqrt{\mu\varepsilon}$ but with a completely different physical origin; a
  comparison worth making explicitly.

Exercises:
[`exercises/03-maxwell-equations-exercises.md`](./exercises/03-maxwell-equations-exercises.md)
and
[`exercises/03-maxwell-equations-solutions.md`](./exercises/03-maxwell-equations-solutions.md).

## Self-assessment checklist

Work through this without notes. Every item should be a clear "yes".

- [ ] I can write all four Maxwell equations in differential and integral form
      and give the meaning of each. (Section 1)
- [ ] I can derive the continuity equation from Ampère–Maxwell + Gauss and
      explain why that forces the displacement current to exist. (Section 2)
- [ ] I can derive the wave equation from the curl equations, and obtain
      $c = 1/\sqrt{\mu_0\varepsilon_0}$. (Section 3)
- [ ] I can derive the diffusion equation for a conductor and state exactly which
      term was dropped. (Section 4)
- [ ] I can write the dimensionless ratio $\sigma/(\omega\varepsilon)$ and explain
      what it controls. (Sections 4–5)
- [ ] I can write the full Helmholtz equation (8) and take both of its limits.
      (Section 4)
- [ ] I can say which regime magnetotellurics and which regime GPR occupy, with
      the ratio evaluated, not just named. (Section 5)
- [ ] I can state the Poynting theorem and identify the ohmic dissipation term.
      (Section 6)
- [ ] I can list six assumptions of the derivation and name an observation that
      would falsify each. (Section 7)
- [ ] I can verify all four equations numerically for a plane wave, explain why
      the Ampère residual is so much smaller than Faraday's, and demonstrate the
      discrete dispersion relation. (Section 8)
