---
id: 02-04-07
title: "Viscoelasticity, Creep and Anelastic Relaxation"
level: doctoral
prereqs: ["02-04-05", "02-03-10", "01-08-02"]
estimated_minutes: 90
tags: [viscoelasticity, attenuation, quality-factor, maxwell-time]
---

# Viscoelasticity, Creep and Anelastic Relaxation

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why perfectly elastic behaviour cannot be the whole story, and name
   the two observations (attenuation and dispersion) that force a time-dependent
   constitutive law.
2. **Derive** the stress–strain relations of the Maxwell, Kelvin–Voigt and
   standard linear solid (SLS) elements, and solve each for creep and stress
   relaxation.
3. **Define** the quality factor $Q$ three equivalent ways, and show that they
   agree to first order in $1/Q$.
4. **Compute** $Q(\omega)$ for each element: $Q = \omega\tau$ for Maxwell,
   $Q = 1/(\omega\tau)$ for Kelvin–Voigt, and the exact SLS result
   $Q(f) = \tfrac12 Q_{\min}(f/f_{\min} + f_{\min}/f)$.
5. **Derive** the connection between attenuation and dispersion (Kramers–Kronig;
   the nearly-constant-$Q$ relation) and **state its regime of validity**.
6. **Compute** the Maxwell time $\tau = \eta/\mu$ and use it to explain why the
   same mantle is an elastic solid to a seismic wave and a viscous fluid to a
   rebounding ice sheet.
7. **Verify** every one of those statements numerically and quote the observed
   discrepancies.

## Prerequisites

- [02-04-05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md)
  — the elastic wave speeds whose time-dependent generalisation this is.
- [02-03-10 Attenuation, Quality Factor and Anelasticity](../03-oscillations-and-waves/10-attenuation.md)
  — $Q$ for a damped oscillator, which is the single-degree-of-freedom version of
  this lesson.
- [02-03-07 Dispersion, Group Velocity and Phase vs Group Speed](../03-oscillations-and-waves/07-dispersion.md)
  — the phenomenology of dispersion, which here is *forced* by attenuation.
- [01-08-02 Second-Order Linear Equations](../../01-mathematics/08-ordinary-differential-equations/02-second-order-linear.md)
  — solving the relaxation equations.
- [02-04-04 Elastic Moduli and Their Interrelations](./04-elastic-moduli.md)
  — $\mu$, $K$ and their meanings, used as the elastic limit of the viscoelastic
  moduli.

## 1. Why anelasticity is unavoidable

Two observations cannot be described by a perfectly elastic medium:

1. **Amplitude decay that is not geometric.** Body-wave amplitudes fall off faster
   than $1/r$ (spreading) even after all interface and scattering effects are
   accounted for; the extra decay is intrinsic absorption.
2. **Velocity dispersion.** Seismic velocities measured at different frequencies
   differ. In rocks the difference is small (fractions of a per cent to a few per
   cent) but systematic, and it is a *consequence* of absorption, not an
   independent fact — a material cannot absorb without dispersing if its response
   is causal (section 5).

A third observation is outside wave propagation entirely: **the Earth flows.**
Postglacial rebound, mantle convection and the isostatic adjustment of mountain
belts all require that rock sustain a finite stress for a finite time and then
deform irreversibly. The same material that transmits shear waves at 1 Hz also
relaxes over $10^4$ years.

A time-dependent (viscoelastic) constitutive law accounts for all three. The
framing for this lesson: **elasticity is the short-time (or high-frequency) limit
of a viscoelastic law, and viscosity is the long-time limit; between them the
material has memory.**

## 2. Precise definitions

**Creep.** Deformation as a function of time under constant applied stress.

**Relaxation.** Stress as a function of time under constant applied strain.

**Creep compliance $J(t)$.** $\varepsilon(t) = J(t)\,\sigma_0$ for a unit step
stress.

**Relaxation modulus $G(t)$.** $\sigma(t) = G(t)\,\gamma_0$ for a unit step strain.
For a linear viscoelastic material, $J$ and $G$ are related by a convolution
inverse; they are not reciprocals.

**Storage and loss modulus.** For a harmonic strain
$\gamma(t) = \gamma_0 e^{i\omega t}$, the stress is
$\sigma(t) = G^*(\omega)\gamma_0 e^{i\omega t}$ with
$G^* = G' + iG''$. $G'$ is the storage (in-phase, elastic) modulus and $G''$ the
loss (out-of-phase, dissipative) modulus.

**Quality factor.** Three equivalent definitions, exact only in the
high-$Q$ limit:

$$Q = \frac{2\pi(\text{energy stored})}{\text{energy dissipated per cycle}}
= \frac{G'}{G''} = \frac{1}{\tan\delta} , \tag{1}$$

where $\delta$ is the phase lag of strain behind stress. Different texts use
different sign and inversion conventions for the ratio of $G'$ to $G''$; all
conventions agree to first order in $1/Q$, which is the only regime in which
"the" quality factor is unambiguous. This lesson uses $Q = G'/G''$, as the demo
does.

**Maxwell time.** $\tau_M = \eta/\mu$: the time separating elastic from viscous
behaviour in a Maxwell element.

## 3. Derivations

### 3.1 The two basic elements

**Elastic spring** (modulus $\mu$):

$$\sigma = \mu\gamma . \tag{2}$$

**Viscous dashpot** (viscosity $\eta$):

$$\sigma = \eta\dot\gamma . \tag{3}$$

Dimension check: $\eta$ in Pa s; $\eta\dot\gamma$ in Pa ✓. A dashpot has *no*
equilibrium modulus: hold it at fixed stress and it strains without limit.

### 3.2 Maxwell element: spring and dashpot in series

In series the **stress is common** and the strains add:

$$\gamma = \frac{\sigma}{\mu} + \frac{1}{\eta}\int_0^t \sigma(t')\,\mathrm dt'
\quad\Longrightarrow\quad
\dot\gamma = \frac{\dot\sigma}{\mu} + \frac{\sigma}{\eta} , \tag{4}$$

or, in the standard form,

$$\sigma + \tau\dot\sigma = \eta\dot\gamma, \qquad \tau = \frac{\eta}{\mu} . \tag{5}$$

**Stress relaxation** at constant strain ($\dot\gamma = 0$) in equation (4):

$$\frac{\dot\sigma}{\mu} = -\frac{\sigma}{\eta}
\;\Longrightarrow\;
\sigma(t) = \sigma_0 e^{-t/\tau} . \tag{6}$$

So the modulus decays:

$$G(t) = \mu e^{-t/\tau} . \tag{7}$$

**Creep** at constant stress:
$\gamma(t) = \sigma_0/\mu + \sigma_0 t/\eta$ — an instantaneous elastic strain
followed by steady linear flow at rate $\sigma_0/\eta$. The Maxwell element is a
**fluid** in the long-time limit, yet it responds elastically at short times.

The demo integrates equation (5) with fourth-order Runge–Kutta and compares with
equation (6): the maximum absolute difference over three relaxation times is
$1.601\times10^{-8}$ Pa on a 1 MPa signal, i.e. $1.6\times10^{-14}$ relative — the
integration is exact to round-off for this linear problem. In the creep test the
implicit viscosity recovered from the steady strain rate is exactly
$1.000000\times10^{18}$ Pa s against an input of $1.0\times10^{18}$ Pa s.

### 3.3 Kelvin–Voigt element: spring and dashpot in parallel

In parallel the **strain is common** and the stresses add:

$$\sigma = \mu\gamma + \eta\dot\gamma . \tag{8}$$

**Creep** at constant stress:

$$\gamma(t) = \frac{\sigma_0}{\mu}\left(1 - e^{-t/\tau}\right), \qquad \tau = \eta/\mu .
\tag{9}$$

There is **no instantaneous strain** (the dashpot forbids it) and the creep strain
is **bounded** (the spring limits it). So Kelvin–Voigt is a solid. The demo
verifies equation (9) numerically to $3.065\times10^{-9}$ in strain.

Its behaviour in the frequency domain is $G^*(\omega) = \mu + i\omega\eta
= \mu(1 + i\omega\tau)$, so

$$Q = \frac{G'}{G''} = \frac{1}{\omega\tau} \propto \frac{1}{f} . \tag{10}$$

That trend — $Q$ rising as frequency falls — is backwards for rocks, where $Q$ is
observed to increase slowly with frequency or to be nearly constant. A
single-element Kelvin–Voigt solid is therefore a poor field model. Its value is
pedagogical: it isolates *delayed elasticity*, which is one of the two
ingredients of a real rock response.

### 3.4 Standard linear solid: the minimum useful model

Put a Maxwell arm in parallel with an elastic spring. The response is

$$\sigma + \tau_\sigma\dot\sigma = \mu_R(\gamma + \tau_\varepsilon\dot\gamma),
\qquad \tau_\varepsilon > \tau_\sigma , \tag{11}$$

equivalently $G(t) = \mu_R\left[1 + \Delta e^{-t/\tau_\sigma}\right]$ with
$\Delta = (G_U-G_R)/G_R$ the modulus contrast. In the frequency domain

$$G^*(\omega) = G_R\frac{1 + i\omega\tau_\varepsilon}{1 + i\omega\tau_\sigma}
= G_R\left[1 + \frac{i x (1+\Delta)}{1 + ix}\right], \qquad x = \omega\tau_\sigma .
\tag{12}$$

Separating real and imaginary parts of the bracket:

$$G' = G_R\frac{1 + x^2(1+\Delta)}{1+x^2}, \qquad
G'' = G_R\frac{x\Delta}{1+x^2} , \tag{13}$$

so

$$\frac{G'}{G''} = \frac{1 + x^2(1+\Delta)}{x\Delta} . \tag{14}$$

This ratio is *minimal* where $x = 1/\sqrt{1+\Delta}$, giving

$$Q_{\min} = \frac{2\sqrt{1+\Delta}}{\Delta} . \tag{15}$$

**The exact SLS quality factor.** Away from the minimum, equation (14) divided by
equation (15) collapses to a remarkably simple form. Writing
$f_{\min}$ for the frequency at the minimum,

$$Q(f) = \frac{Q_{\min}}{2}\left(\frac{f}{f_{\min}} + \frac{f_{\min}}{f}\right)
\qquad\text{(exact)}. \tag{16}$$

*Proof.* With $x\sqrt{1+\Delta} = f/f_{\min}$ (the peak condition),
equation (14) is $[1+x^2(1+\Delta)]/(x\Delta)
= \frac{\sqrt{1+\Delta}}{\Delta}\left(x\sqrt{1+\Delta} + \frac{1}{x\sqrt{1+\Delta}}\right)$
and equation (15) is $2\sqrt{1+\Delta}/\Delta$; the ratio is
$\tfrac12(u + 1/u)$ with $u = f/f_{\min}$. $\square$

The demo's SLS has $Q_{\min} = 30$ at $f_{\min} = 10$ Hz, and its measured
$Q$ values — 151.5 at 1 Hz, 78.0 at 2 Hz, 37.5 at 5 Hz, 30.0 at 10 Hz, 37.5 at
20 Hz, 78.0 at 50 Hz, 151.5 at 100 Hz — reproduce equation (16) **exactly** at
every tabulated frequency (at 1 Hz: $\tfrac12(0.1+10)\times30 = 151.5$). Solving
equation (15) for $\Delta$ gives $\Delta = 0.068925916$; the resulting total
velocity contrast between the relaxed and unrelaxed limits is
$\sqrt{1+\Delta}-1 = 3.3889$ per cent, and between 1 Hz and 100 Hz the demo
measures 3.3206 per cent (an independent reconstruction of the same element gives
3.3206 per cent, the small difference from the 3.3889 per cent limit being simply
that 1 Hz and 100 Hz are one decade either side of the minimum rather than the
true limits).

**The SLS is not a good model over wide bands.** Equation (16) shows
$Q \propto 1/f$ well below $f_{\min}$ and $Q \propto f$ well above it. Real rocks
show a much weaker frequency dependence of $Q$ across many decades, so a single
SLS either fits a narrow band or misfits the rest. Seismic practice therefore
uses a **superposition** of SLS elements (a discrete or continuous distribution of
relaxation times) chosen to keep $Q$ nearly constant over the band of interest.
That is a modelling choice, not a measured material law.

### 3.5 Attenuation, $Q$ and the amplitude decay law

Consider a plane wave with $\exp[i(\omega t - kx)]$ where the modulus is complex,
$M = M'(1 + i/Q)$. Then $k = \omega\sqrt{\rho/M}$ acquires an imaginary part, and
the amplitude decays:

$$A(x) = A_0\exp\left(-\frac{\omega x}{2QV}\right) \equiv A_0 e^{-\alpha x},
\qquad \alpha = \frac{\omega}{2QV} = \frac{\pi f}{QV} . \tag{17}$$

*Derivation.* Write $k = k_r + i\alpha$; then
$|e^{-ikx}| = e^{\alpha x}$ with $\alpha = -\mathrm{Im}\,k$. With
$k = \omega\sqrt{\rho}/M^{1/2}$ and $M = M'(1+i/Q)$, $M^{-1/2} \approx
M'^{-1/2}(1 - i/(2Q))$ for $Q\gg1$, so
$\mathrm{Im}\,k \approx -\omega\sqrt{\rho/M'}/(2Q) = -\omega/(2QV)$, giving
equation (17). $\square$

Equivalently, the amplitude decays by the factor $e^{-\pi/Q}$ **per cycle**,
because one period corresponds to $\omega t = 2\pi$ and
$\alpha V T = \omega T/(2Q) = \pi/Q$. This is the same statement as
$\Delta E/E_{\text{stored}} = 2\pi/Q$ per cycle, and it is the form derived for the
damped oscillator in
[02-03-10](../03-oscillations-and-waves/10-attenuation.md). It also shows the
useful rule of thumb: **$Q^{-1}$ is the fractional energy loss per radian.**

## 4. The Maxwell time: one rock, three behaviours

The Maxwell relaxation time $\tau = \eta/\mu$ is the crossover between solid-like
and fluid-like response. The dimensionless group that decides which regime you are
in is

$$\omega\tau = \frac{\text{time to relax}}{\text{time of one cycle}} . \tag{18}$$

| Phenomenon | Period | $\omega\tau$ ($\eta = 10^{21}$ Pa s, $\mu = 70$ GPa, $\tau = 452.7$ yr) | Behaviour |
|---|---|---|---|
| Seismic wave (30 Hz) | $3.333\times10^{-2}$ s | $2.693\times10^{12}$ | elastic solid |
| Solid-earth tide (M2) | $4.471\times10^{4}$ s | $2.008\times10^{6}$ | elastic solid |
| Postglacial rebound | $3.156\times10^{11}$ s ($10^4$ yr) | $0.284$ | viscous fluid |

These are the demo's numbers for $\eta = 10^{21}$ Pa s and $\mu = 70$ GPa, giving
$\tau = 1.429\times10^{10}$ s $= 452.7$ years. The same material, the same
moduli, three different apparent rheologies — decided only by the timescale of the
forcing. **This table is the single most important regime-of-validity statement in
the module**, and the numbers behind it are order-of-magnitude values typical of
the upper mantle rather than measurements of a specific place: $\eta$ varies by
orders of magnitude with temperature, pressure, water content and stress, and
quoted upper-mantle viscosities from postglacial-rebound studies commonly span
roughly $10^{20}$–$10^{21}$ Pa s depending on region and on the analysis.

There is a consistency problem to notice: applying $Q = \omega\tau$ (the Maxwell
result) at seismic frequency gives $Q \approx 2.7\times10^{12}$ — essentially no
attenuation. Observed seismic $Q$ in the mantle is many orders of magnitude
smaller. **The Maxwell element explains why the mantle flows, but it cannot
explain seismic attenuation**: the mechanisms that absorb seismic energy
(grain-boundary sliding, dislocation motion, fluid flow in cracks, thermoelastic
relaxation) operate at frequencies and stress amplitudes far from the conditions
of mantle creep. This is a genuine open area of rock physics, and it is why
seismic $Q$ and the viscosity inferred from rebound are treated as independent
observables even though both are "anelastic".

## 5. Attenuation and dispersion are one phenomenon

Because the response is causal and linear, the real and imaginary parts of
$G^*(\omega)$ cannot be chosen independently: they are a Hilbert-transform pair
(the **Kramers–Kronig** relations). A consequence is that a medium with
$Q < \infty$ must have $\mathrm dV/\mathrm d\omega \ne 0$.

For a **nearly constant $Q$** over a band around a reference frequency $f_0$, the
leading-order relation is

$$\frac{V(f)-V(f_0)}{V(f_0)} \approx \frac{1}{\pi Q}\ln\frac{f}{f_0}
\qquad (Q \gg 1,\ |\ln(f/f_0)| \lesssim \text{a few}). \tag{19}$$

The sign is the physical statement: **attenuation makes velocity increase with
frequency**, and the two are locked together by equation (19).

The demo tests it against its SLS, using the reference $Q_{\min} = 30$ at
$f_0 = 10$ Hz (a *constant* value, as equation (19) assumes):

| $f$ (Hz) | $Q(f)$ | $V$ (m s⁻¹) | $V/V_0-1$ | $\frac{1}{\pi Q}\ln\frac{f}{f_0}$ | difference |
|---|---|---|---|---|---|
| 1 | 151.5 | 3397.9159 | $-0.015938$ | $-0.024431$ | $8.493\times10^{-3}$ |
| 2 | 78.0 | 3401.0511 | $-0.015030$ | $-0.017077$ | $2.046\times10^{-3}$ |
| 5 | 37.5 | 3418.9485 | $-0.009847$ | $-0.007355$ | $-2.493\times10^{-3}$ |
| 10 | 30.0 | 3452.9500 | $0$ | $0$ | $0$ |
| 20 | 37.5 | 3487.9864 | $+0.010147$ | $+0.007355$ | $2.792\times10^{-3}$ |
| 50 | 78.0 | 3507.2996 | $+0.015740$ | $+0.017077$ | $-1.337\times10^{-3}$ |
| 100 | 151.5 | 3510.7477 | $+0.016739$ | $+0.024431$ | $-7.693\times10^{-3}$ |

Read the table honestly:

- The **shape** is right — both sides are odd in $\ln(f/f_0)$, both vanish at the
  reference frequency, and both have the same sign. The mechanism is confirmed.
- The **magnitude** is not: at a factor of ten from $f_0$ the approximation is off
  by $8.5\times10^{-3}$, which is more than half the size of the effect it is
  trying to predict. Equation (19) is a leading-order result with an error of the
  same order as $1/(\pi Q)\ln$, precisely because this SLS has $Q = 30$, not
  $Q \gg 1$.
- Using the *local* $Q(f) = 151.5$ at 1 Hz in equation (19) instead gives
  $-0.00484$, an error of the same size in the other direction. Neither choice is
  "the" answer: the relation assumes $Q$ is constant, and here it is not.

The moral is the ordinary one for asymptotic relations: equation (19) is the right
tool for ordering-of-magnitude work, and the wrong tool for quantitative
prediction of a specific material's dispersion.

## 6. Physical interpretation

**Viscoelasticity is the statement that stress and strain are not instantaneously
proportional.** The spring says "stress now", the dashpot says "stress is whatever
is needed to keep straining", and real rock says something intermediate whose
position depends on the timescale.

**$Q^{-1}$ is a fractional energy loss, not a decay rate.** One radian of phase
costs a fraction $Q^{-1}$ of the stored energy. This is why $Q$ is the natural
language for comparing absorption across frequency: a pure decay rate $\alpha$
mixes frequency and material properties (through $V$), while $Q^{-1}$ separates
them.

**Intrinsic and apparent attenuation are different things.** Scattering by
heterogeneities, interbed multiples and thin-layer interference all remove energy
from a direct arrival, and all are frequency-dependent. They are sometimes
parameterised as an "apparent $Q$", but it is not a material property: it depends
on the geology, the acquisition geometry and the processing. Confusing the two is
the most consequential error in attenuation work, and it is why laboratory $Q$ and
field $Q$ are never compared without stating the mechanism.

**The mantle's dual behaviour is the clearest demonstration of the time-dependent
law.** Same rock, same moduli: solid to a seismic wave, fluid to an ice sheet.

## 7. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Linearity | $\sigma \propto \gamma$ at every instant, superposition holds | Finite-strain and nonlinear creep; rock failure; yield; nonlinear attenuation at high strain amplitude |
| Causality | No response before its cause | Violating it would allow non-dissipative attenuation (and is unphysical) |
| $Q \gg 1$ for the simple relations | Equations (1), (17) and (19) are first order in $1/Q$ | At $Q < 10$ the three definitions of $Q$ in (1) differ and the sign conventions matter |
| Constant $Q$ for equation (19) | $Q$ independent of frequency over the band | Real rocks show a weak but non-zero dependence; a single SLS is strongly frequency-dependent (equation 16) |
| Single relaxation mechanism | One $\tau$ | Real rocks need a distribution of relaxation times; the SLS is a one-parameter fit to a spectrum |
| Isotropic moduli | Scalar $G^*$ | Anisotropic rocks have direction-dependent attenuation (and shear-wave splitting with differential attenuation) |
| Small strain | $\gamma \ll 1$ | Nonlinear viscoelasticity, brittle damage |
| Intrinsic mechanism | The dissipation is inside the material | Scattering produces apparent, not intrinsic, attenuation |
| Maxwell as a mantle model | Viscous flow in the long-time limit | The observed seismic $Q$ is inconsistent with $\omega\tau$ from creep — the two must be modelled separately |

## 8. Units and dimensional analysis

- $\mu$, $G'$, $G''$, $M'$: Pa ✓. $\eta$: Pa s ✓. $\tau = \eta/\mu$: s ✓.
- $Q$ is dimensionless ✓, and so is $\omega\tau$ ✓. Both are the natural
  dimensionless groups of the problem.
- $\alpha = \omega/(2QV)$: (s⁻¹)/(m s⁻¹) = m⁻¹ ✓.
- $\Delta = (G_U-G_R)/G_R$ dimensionless ✓; equation (15) then gives a
  dimensionless $Q$ from a dimensionless contrast ✓.
- Equation (19): $\ln(f/f_0)$ dimensionsless ✓, so the right side is a pure
  number, as required for a relative velocity change ✓ — a quick check that
  neither $Q$ nor a velocity has been accidentally omitted.

## 9. Python demonstration

[`code/viscoelasticity_demo.py`](./code/viscoelasticity_demo.py) integrates the
Maxwell and Kelvin–Voigt equations, computes the SLS complex modulus and its
$Q(\omega)$, tests the nearly-constant-$Q$ relation, and tabulates the Maxwell
time against the three timescales. Selected observed output:

```text
shear modulus mu = 30.0 GPa, viscosity eta = 1.0e+18 Pa s
Maxwell relaxation time tau = eta/mu = 33333333.3 s = 1.0563 years
stress relaxation at constant strain: sigma(t) = sigma_0 exp(-t/tau)
   t/tau  sigma numeric (GPa)  sigma analytic (GPa)  difference
    0.00          1.000000000           1.000000000   0.000e+00
    1.00          0.367879441           0.367879441   9.837e-09
    2.00          0.135335283           0.135335283   1.601e-08
    3.00          0.049787068           0.049787068   8.818e-09
max |numerical - analytic| over 3 tau = 1.601e-08 Pa
implicit viscosity recovered from the steady strain rate: 1.000000e+18 Pa s (input 1.0e+18)
```

```text
creep: eps(t) = (sigma_0/mu) (1 - exp(-t/tau)); no instantaneous strain
   t/tau    strain numeric          analytic  difference
    1.00   2.106762027e-05   2.107068529e-05   3.065e-09
    3.00   3.167251966e-05   3.167376439e-05   1.245e-09
max |numerical - analytic| = 3.065e-09
```

```text
relaxed modulus M(0) = 30.000000 GPa, unrelaxed modulus M(inf) = 32.067777 GPa, contrast Delta = 0.068925916
Q minimum = 30.0 at f0 = 10 Hz, V(f0) = 3452.9500 m/s (rho = 2600 kg/m^3)
   f (Hz)       Q(f)     V (m/s)     V/V0 - 1   ln(f/f0)/(pi Q)  difference
      1.0   151.5000   3397.9159    -0.015938         -0.024431   8.493e-03
     10.0    30.0000   3452.9500     0.000000          0.000000   0.000e+00
    100.0   151.5000   3510.7477     0.016739          0.024431  -7.693e-03
```

```text
  For a Maxwell solid the same calculation gives Q = omega tau exactly,
  which is verified by the numbers below:
    f =    1.0 Hz: Q = Re/Im = 2.094395e+08, omega tau = 2.094395e+08
    f =  100.0 Hz: Q = Re/Im = 2.094395e+10, omega tau = 2.094395e+10
```

```text
assumed upper-mantle values: eta = 1.0e+21 Pa s, mu = 70 GPa
Maxwell time tau = eta/mu = 1.429e+10 s = 452.7 years
          seismic wave: period = 3.333e-02 s, omega tau = 2.693e+12, Q = omega tau = 2.693e+12
           tidal cycle: period = 4.471e+04 s, omega tau = 2.008e+06, Q = omega tau = 2.008e+06
   postglacial rebound: period = 3.156e+11 s, omega tau = 2.844e-01, Q = omega tau = 2.844e-01
```

### What to observe

| Observation | Consequence |
|---|---|
| The RK4 relaxation and creep curves match the analytic solutions to $1.6\times10^{-8}$ Pa and $3.1\times10^{-9}$ strain | The linear viscoelastic constitutive laws were integrated correctly; the residual is truncation, not model error |
| The creep test recovers $\eta$ as exactly $1.000000\times10^{18}$ Pa s | The steady creep rate $\sigma_0/\eta$ is a direct viscosity measurement — the principle behind laboratory creep experiments |
| $Q(f)$ for the SLS is 30 at 10 Hz and 151.5 at 1 Hz and at 100 Hz | The SLS has an attenuation peak (a $Q$ minimum) at one frequency and $Q \propto 1/f$ or $\propto f$ away from it; equation (16) reproduces the table exactly |
| The constant-$Q$ dispersion formula deviates by up to $8.5\times10^{-3}$ | The relation is first-order in $1/Q$; at $Q = 30$ the error is of the same size as the effect |
| Maxwell $Q$ equals $\omega\tau$ to all printed digits at 1 Hz and 100 Hz | The single-element result $Q = \omega\tau$ (equation 14) is exact, not approximate |
| The mantle is elastic at seismic and tidal periods and viscous at $10^4$ yr | The controlling group is $\omega\tau$: 2.7×10¹², 2.0×10⁶ and 0.28 respectively |

> **Breaking exercise.** Take the SLS and *double* $\Delta$ while keeping
> $\tau_\sigma$ fixed. Predict, before computing, what happens to $Q_{\min}$, to
> the frequency of the minimum, and to the total velocity dispersion. Then check
> equations (15) and (16) and explain the direction of each change.

## 10. Common mistakes

1. **Treating $Q$ as a constant of the material.** It is a function of frequency,
   and in a single-mechanism model it varies by a factor of five across one decade
   (equation 16).
2. **Using the three definitions of $Q$ in equation (1) interchangeably at low
   $Q$.** They agree only to first order in $1/Q$.
3. **Expecting attenuation without dispersion, or the reverse.** Causality forbids
   it (section 5).
4. **Modelling a rock with a single SLS and extrapolating over decades.** The
   superposition of mechanisms is the point; a one-element fit is a narrow-band
   approximation.
5. **Confusing intrinsic with apparent (scattering) attenuation.** Only the former
   is a material property.
6. **Using the Maxwell element for seismic attenuation because it explains mantle
   flow.** At seismic frequencies it predicts $Q \sim 10^{12}$.
7. **Ignoring the temperature and pressure dependence of $\eta$.** Quoted
   viscosities without a stated temperature and stress regime are not comparable;
   $\eta$ can vary by orders of magnitude.
8. **Assuming $Q_P = Q_S$.** In rocks they differ, often substantially, and in
   fluid-saturated rocks the difference is a diagnostic of the saturation state.
9. **Reading $\tau = \eta/\mu$ as a single physical time for a rock.** It is the
   crossover time of a *model* element; a real rock has a spectrum of relaxation
   times.
10. **Assuming the viscoelastic moduli are real.** The whole point is
    $G^* = G' + iG''$; taking the real modulus alone discards the physics.

## 11. Real-world applications

- **Seismic amplitude inversion for $Q$.** Attenuation tomography maps
  $Q^{-1}$ from amplitude and spectral decay; the resulting anomalies are used as
  temperature, fluid and melt indicators
  ([06-seismology](../../06-seismology/README.md)).
- **Dispersion correction in processing.** Because $V$ depends on frequency,
  surface-wave and body-wave velocity models must state the frequency at which
  they are defined; mixing a 10 Hz and a 50 Hz velocity without correction
  introduces systematic error.
- **Mantle rheology and glacial isostatic adjustment.** Postglacial rebound
  inversions for upper-mantle viscosity use the Maxwell (or Burgers) framework of
  section 4 ([12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)).
- **Reservoir characterisation.** Frequency-dependent $Q$ distinguishes
  fluid-saturated from dry rock, and is used in seismic attribute analysis
  ([05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).
- **Tidal and earthquake-cycle deformation.** Tides load the solid Earth at
  $\omega\tau \sim 10^{6}$ (elastic), while the earthquake cycle at years to
  centuries sits near $\omega\tau \sim 1$ — where both elastic and viscous
  behaviour matter and the modelling is hardest.
- **Laboratory rock mechanics.** Creep tests are run precisely to measure
  $\eta(T, \sigma)$ from the steady strain rate, as the demo's section 1
  illustrates.
- **Attenuation in seismic hazard.** Path attenuation of strong ground motion is
  parameterised by a $Q$ or $\kappa$ term, and its frequency dependence controls
  the high-frequency content of the predicted motion.

## 12. Further reading

- **Nowick, A. S., & Berry, B. S. *Anelastic Relaxation in Crystalline Solids*
  (Academic Press).** The standard treatment of relaxation mechanisms, $Q$ and the
  Kramers–Kronig relations. Level: advanced.
- **Fung, Y. C. *Foundations of Solid Mechanics* (Prentice-Hall).** Viscoelastic
  constitutive laws, correspondence principle and the element models of
  section 3. Level: graduate.
- **Aki, K., & Richards, P. G. *Quantitative Seismology* (2nd ed., University
  Science Books, 2002).** The seismological treatment: attenuation, $Q$, and the
  dispersion relation used in section 5. Level: advanced.
- **Futterman, W. I. (1962), *Dispersive body waves*, Journal of Geophysical
  Research.** A foundational derivation that attenuation forces dispersion, and
  the origin of the standard relations of section 5. Level: advanced.
- **Kjartansson, E. (1979), *Constant Q-wave propagation and attenuation*,
  Journal of Geophysical Research.** The constant-$Q$ model, useful as the
  continuum limit of a superposition of SLS elements. Level: advanced.
- **Mavko, G., Mukerji, T., & Dvorkin, J. *The Rock Physics Handbook* (Cambridge
  University Press).** Practical formulae for $Q$ and dispersion in rocks, and the
  fluid-flow mechanisms specific to saturated rocks. Level: applied.
- **Karato, S. *Deformation of Earth Materials* (Cambridge University Press).**
  The creep physics behind the viscosity and its strong temperature and water
  dependence. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.
> The specific numeric values used here (viscosities, $Q$ values, moduli) are
> quoted as typical orders of magnitude, not as measurements.

## 13. Related lessons

- [05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md) —
  the elastic limit that this lesson generalises.
- [06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](./06-anisotropic-elasticity.md)
  — the other way the constitutive law departs from the two-constant ideal;
  anisotropic attenuation is the combination of both.
- [08 Rock Failure, Fracture and Rate-State Friction](./08-failure-and-friction.md)
  — the strongly nonlinear end of the material response, where linear
  viscoelasticity stops applying.
- [02-03-10 Attenuation, Quality Factor and Anelasticity](../03-oscillations-and-waves/10-attenuation.md)
  — the single-oscillator derivation of $Q$ and of the per-cycle decay
  $e^{-\pi/Q}$.
- [02-03-07 Dispersion, Group Velocity and Phase vs Group Speed](../03-oscillations-and-waves/07-dispersion.md)
  — dispersion produced by geometry and by structure, which must be separated
  from the intrinsic dispersion forced by equation (19).
- [06-seismology](../../06-seismology/README.md) — $Q$ tomography and dispersion
  correction.
- [05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)
  — laboratory $Q$ and fluid-saturation mechanisms.

Exercises:
[`exercises/07-viscoelasticity-exercises.md`](./exercises/07-viscoelasticity-exercises.md)
and
[`exercises/07-viscoelasticity-solutions.md`](./exercises/07-viscoelasticity-solutions.md).

## Self-assessment checklist

- [ ] I can write the constitutive ODEs of the Maxwell, Kelvin–Voigt and standard
      linear solid elements. (Section 3)
- [ ] I can solve each for creep and for stress relaxation under a step load.
      (Sections 3.2–3.4)
- [ ] I can state three definitions of $Q$ and say when they agree. (Section 2)
- [ ] I can derive $Q = \omega\tau$ for Maxwell and $Q = 1/(\omega\tau)$ for
      Kelvin–Voigt. (Sections 3.3–3.4)
- [ ] I can prove equation (16) and explain why a single SLS cannot give nearly
      constant $Q$ over decades. (Section 3.4)
- [ ] I can derive $\alpha = \pi f/(QV)$ and the per-cycle amplitude factor
      $e^{-\pi/Q}$. (Section 3.5)
- [ ] I can state the nearly-constant-$Q$ dispersion relation, its sign, and its
      regime of validity, and I know it failed by $8.5\times10^{-3}$ in the demo.
      (Section 5)
- [ ] I can compute the Maxwell time and tabulate $\omega\tau$ for seismic, tidal
      and rebound periods. (Section 4)
- [ ] I can explain why the Maxwell model explains postglacial rebound but not
      seismic attenuation. (Section 4)
- [ ] I can distinguish intrinsic from apparent attenuation. (Section 6)
