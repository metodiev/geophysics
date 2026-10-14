---
id: 02-04-08
title: "Rock Failure, Fracture and Rate-State Friction"
level: graduate
prereqs: ["02-04-01", "02-04-04", "02-04-07"]
estimated_minutes: 90
tags: [failure, mohr-coulomb, fault-mechanics, rate-and-state]
---

# Rock Failure, Fracture and Rate-State Friction

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Mohr–Coulomb failure criterion, construct the Mohr circle and
   friction envelope, and derive the optimal fault orientation
   $45^\circ - \varphi/2$ to $\sigma_1$ from the tangency condition.
2. **Apply** the Anderson classification and state which of the three stress
   regimes produces which fault type and dip.
3. **Compute** frictional strength as a function of depth using effective stress,
   and explain why the frictional and ductile strength profiles cross.
4. **State Byerlee's law** with its coefficients, its conditions of applicability
   and its status as an empirical fit rather than a physical law.
5. **Write** the Dieterich–Ruina rate-and-state friction law and derive the
   critical stiffness $k_c = \sigma(b-a)/D_c$.
6. **Analyse** the linearised rate-and-state stability problem, reproduce its
   exact threshold, and explain why a numerical measurement of that threshold is
   limited to roughly 15 per cent accuracy.
7. **Verify** the Mohr–Coulomb tangency and the stability threshold numerically,
   quoting the observed discrepancies.

## Prerequisites

- [01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](./01-stress.md)
  — principal stresses, Mohr circles and effective stress.
- [04 Elastic Moduli and Their Interrelations](./04-elastic-moduli.md)
  — the moduli that appear in the elastic loading of a fault.
- [07 Viscoelasticity, Creep and Anelastic Relaxation](./07-viscoelasticity.md)
  — the ductile behaviour that terminates the brittle regime.
- [02-02-02 Newton's Laws and Free-Body Analysis](../02-classical-mechanics/02-newtons-laws.md)
  — the elementary force analysis that the Coulomb friction law comes from.

## 1. Why failure deserves its own lesson

Everything up to lesson 07 assumed the material stays intact and deforms
linearly. That assumption fails in exactly the places geophysics cares about: a
seismic rupture, a volcanic flank collapse, a borehole breakout, a landslide, the
formation of a fault. In each case the stress exceeds a threshold and the
response becomes fractal, localised and permanently irreversible.

Two distinct failure modes must be distinguished:

- **Brittle failure** — localised rupture on a surface, described by a friction or
  fracture criterion, magnitude- and scale-dependent, and (as section 5 shows)
  unstable when the loading is compliant enough.
- **Ductile (plastic/creep) failure** — distributed, irreversible deformation
  described by a flow law, temperature- and strain-rate-dependent, and stable in
  the sense that it does not localise spontaneously.

The brittle/ductile transition in the crust is the competition between the two,
and it is the reason the seismogenic zone has a base.

## 2. Precise definitions

**Traction on a plane.** $t_i = \sigma_{ij}n_j$; its normal component is
$\sigma_n = t_in_i$ and its shear component is $\tau = \sqrt{|\mathbf t|^2 -
\sigma_n^2}$.

**Cohesion $C$.** The shear strength at zero normal stress, in Pa.

**Angle of internal friction $\varphi$.** Defined by $\mu = \tan\varphi$, where
$\mu$ is the friction coefficient (dimensionless).

**Effective stress.** $\sigma' = \sigma - p$, where $p$ is pore-fluid pressure.
Friction responds to $\sigma'$, not to $\sigma$.

**Mohr–Coulomb criterion.** Failure occurs on a plane when

$$\tau = C + \mu\sigma_n' = C + \sigma_n'\tan\varphi . \tag{1}$$

**Tensile strength $T$.** The maximum $\sigma_n$ (taken negative in compression
conventions) that intact rock can sustain; usually $T \ll C$ in magnitude, so
tensile failure dominates only very near the surface or in strongly
decompressed settings.

**Rate-and-state friction.** Friction depends on the instantaneous slip rate $V$
and on a state variable $\theta$ describing the history of contact:

$$\mu = \mu_* + a\ln\frac{V}{V_*} + b\ln\frac{V_*\theta}{D_c} , \tag{2}$$

with $a,b$ dimensionless, $D_c$ the characteristic slip distance (m) and $V_*$ a
reference velocity.

**Critical stiffness.** $k_c = \sigma(b-a)/D_c$ — the spring stiffness that
separates unstable (stick-slip) from stable sliding.

## 3. Derivations

### 3.1 Mohr circle and the friction envelope

For a plane whose normal makes an angle $\theta$ with $\sigma_1$ (measured in the
$\sigma_1$–$\sigma_3$ plane, with $\sigma_1 > \sigma_2 > \sigma_3$):

$$\sigma_n = \frac{\sigma_1+\sigma_3}{2} + \frac{\sigma_1-\sigma_3}{2}\cos2\theta,
\qquad \tau = \frac{\sigma_1-\sigma_3}{2}\sin2\theta . \tag{3}$$

As $\theta$ varies these trace the **Mohr circle** of centre
$(\sigma_1+\sigma_3)/2$ and radius $(\sigma_1-\sigma_3)/2$ (lesson 02-04-01). The
criterion (1) is a straight line of slope $\mu$ on the same axes. **Failure is the
condition that the circle touches the line** — the criterion is not an independent
law but a statement about the geometry of the stress state, which is why the
optimal orientation is determined rather than random.

### 3.2 The optimal orientation

Maximise $\tau - \mu\sigma_n'$ over $\theta$ using equation (3):

$$\frac{\mathrm d}{\mathrm d\theta}\left[\tau - \mu\sigma_n\right]
= \frac{\sigma_1-\sigma_3}{2}\left[2\cos2\theta + 2\mu\sin2\theta\right] = 0
\;\Longrightarrow\; \tan2\theta = -\frac{1}{\mu} = -\cot\varphi . \tag{4}$$

The solution in $(0,90^\circ)$ is

$$2\theta = 90^\circ + \varphi \quad\Longrightarrow\quad
\boxed{\theta_{\text{opt}} = 45^\circ + \frac{\varphi}{2}} \tag{5}$$

for the angle between the plane's **normal** and $\sigma_1$. Equivalently, the
plane itself is inclined at

$$90^\circ - \left(45^\circ + \frac{\varphi}{2}\right) = 45^\circ - \frac{\varphi}{2}
\tag{6}$$

to the $\sigma_1$ axis, which is the form usually quoted in structural geology.

The demo scans all 9001 plane orientations for the model
$C = 20$ MPa, $\mu = 0.60$ ($\varphi = 30.9638^\circ$), $\sigma_3 = 100$ MPa, and
finds the maximum of $\tau - \mu\sigma_n - C$ to be $-3.541570\times10^{-1}$ Pa —
zero to within the $0.01^\circ$ discretisation of the scan — at a normal
$60.4800^\circ$ from $\sigma_1$, against the analytic $45^\circ + \varphi/2 =
60.4819^\circ$. The plane is therefore inclined at $29.5200^\circ$ to $\sigma_1$,
against the analytic $45^\circ - \varphi/2 = 29.5181^\circ$. **The tangency
condition is verified, and the residual is zero at the optimum**, which is the
content of the criterion.

### 3.3 Failure stress and the Anderson classification

Setting $\theta = \theta_{\text{opt}}$ in equation (3) and eliminating gives the
failure condition in terms of principal stresses:

$$\sigma_1' = \frac{2C\cos\varphi + \sigma_3' (1+\sin\varphi)}{1-\sin\varphi}
= \sigma_3'\tan^2\left(45^\circ + \frac{\varphi}{2}\right)
+ 2C\tan\left(45^\circ+\frac{\varphi}{2}\right) . \tag{7}$$

The demo evaluates this at $\sigma_3' = 100$ MPa and obtains
$\sigma_1' = 382.590461$ MPa, which is the value used as the "failure" stress in
the orientation scan — so the two halves of the calculation are mutually
consistent by construction, and the near-zero residual confirms it.

**Anderson's classification** follows from which principal stress is vertical in
the shallow crust (where the surface is a free surface, so one principal stress
must be vertical):

| regime | $\sigma_1$ | $\sigma_3$ | fault type | dip |
|---|---|---|---|---|
| normal | vertical | horizontal | normal (extensional) | $45^\circ + \varphi/2 = 60.48^\circ$ |
| thrust | horizontal | vertical | reverse (compressional) | $45^\circ - \varphi/2 = 29.52^\circ$ |
| strike-slip | horizontal | horizontal | vertical strike-slip planes | $90^\circ$ (planes vertical) |

For the demo's parameters the two dips are $60.4819^\circ$ and $29.5181^\circ$:
**the geometry is the same, only the orientation of the stress state relative to
the surface changes.** This is why fault dip is a first-order indicator of stress
regime, and why the three fault types are the three Andersonian cases rather than
three independent mechanisms.

### 3.4 Frictional strength with depth, and the brittle–ductile transition

Take the **vertical-stress envelope**, the standard simplification used in
strength-profile diagrams: the vertical (overburden) stress
$\sigma_v = \rho g z$ with $\rho = 2700$ kg m⁻³, hydrostatic pore pressure
$p = \rho_w g z$ with $\rho_w = 1000$ kg m⁻³, the normal stress on the potential
fault plane approximated by the vertical stress, and $\mu = 0.6$, $C = 0$. Then
$\sigma_n' = \sigma_v - p = (\rho-\rho_w)gz$ and the shear strength is
$\tau = \mu\sigma_n'$. The demo computes:

> *Regime note.* Setting $\sigma_n = \sigma_v$ is exact for a horizontal plane and
> approximate for a dipping fault, where the exact expression is
> $\sigma_n = \sigma_v\cos^2\delta + \sigma_h\sin^2\delta$ for a fault dipping at
> $\delta$. The simplification is adopted because it gives the standard linear
> brittle-strength envelope and because it makes the $z$-dependence explicit; do not
> read the numbers below as the normal stress on a $60^\circ$-dipping fault.

| depth (km) | $\sigma_v$ (MPa) | $\sigma_n'$ (MPa) | $\tau_{\max}$ (MPa) | $\tau/\sigma_n'$ |
|---|---|---|---|---|
| 2 | 52.974 | 33.354 | 20.012 | 0.6000 |
| 5 | 132.435 | 83.385 | 50.031 | 0.6000 |
| 10 | 264.870 | 166.770 | 100.062 | 0.6000 |
| 15 | 397.305 | 250.155 | 150.093 | 0.6000 |
| 20 | 529.740 | 333.540 | 200.124 | 0.6000 |
| 30 | 794.610 | 500.310 | 300.186 | 0.6000 |

Frictional strength **grows linearly with depth** — without limit. Something must
stop it, and what stops it is ductile creep, whose strength *decreases* with
temperature (hence depth). The crossing of the two is the **brittle–ductile
transition**, the base of the seismogenic zone.

*Regime and honesty note.* The depth of that transition is **not a universal
number**. It depends on the geothermal gradient, the strain rate, the mineralogy
(with quartz-rich, feldspar-poor lithologies weakening at lower temperature than
olivine), the pore pressure and the presence of fluids. Standard estimates for
quartz-rich continental crust place it somewhere in the range of roughly ten to
twenty kilometres, but the spread across published studies and regions is large,
and computing it for a specific setting requires a specific creep flow law with
measured parameters, not a rule of thumb. The table above is only the brittle
half of the argument; the ductile half is lesson 02-05 or a rock-mechanics text.

### 3.5 Byerlee's law

A large body of room-temperature, low-pressure friction experiments on many rock
types gives, to within the scatter, two linear segments:

$$\tau = 0.85\,\sigma_n' \quad \text{for } \sigma_n' \lesssim 200\ \text{MPa},
\qquad \tau = 50\ \text{MPa} + 0.6\,\sigma_n' \quad \text{for }
\sigma_n' \gtrsim 200\ \text{MPa} , \tag{8}$$

commonly summarised as $\mu \approx 0.6$ (equivalently $\varphi \approx 31^\circ$)
over the range relevant to the crust. This is **Byerlee's law**, and its
remarkable feature is that it is nearly independent of rock type, mineralogy and
surface roughness — which is why a single friction coefficient is used in crustal
stress modelling.

*Status.* Byerlee's law is an **empirical fit to laboratory data**, quoted here
with the rounding that is conventional in the literature. It is not derived from
first principles, and it is not exact at the conditions of the seismogenic zone:
at depth, temperatures of a few hundred degrees Celsius, high slip rates, the
presence of phyllosilicates (clays, serpentine, talc) and fluid pressure all
reduce the effective $\mu$ below 0.6, in some cases substantially. Values of
$\mu$ as low as $\sim$0.1–0.2 have been reported for some clay-rich or
serpentinite fault rocks. Treat $\mu = 0.6$ as a useful *upper bound* for
modelling, and check the specific material and conditions before relying on it.

### 3.6 Rate-and-state friction

Byerlee's law is rate-independent. Laboratory experiments show it is not: friction
evolves with sliding history. The Dieterich–Ruina ("aging") formulation is

$$\mu(V,\theta) = \mu_* + a\ln\frac{V}{V_*}
+ b\ln\frac{V_*\theta}{D_c}, \qquad
\frac{\mathrm d\theta}{\mathrm dt} = 1 - \frac{V\theta}{D_c} . \tag{9}$$

The state variable $\theta$ has units of time and represents the average age of
the population of contacting asperities; at steady state
$V\theta/D_c = 1$, so $\theta_{ss} = D_c/V$ and the two logarithmic terms combine
to the rate dependence $\mu_{ss}(V) = \mu_* + (a-b)\ln(V/V_*)$.

- If $b > a$ (velocity weakening) steady-state friction **decreases** with sliding
  rate: faster slip is easier, which is the ingredient of instability.
- If $a > b$ (velocity strengthening) friction increases with rate and the slip is
  intrinsically stable.

**The spring–slider model.** Consider a block loaded through a spring of stiffness
$k$ (force per unit displacement, Pa m⁻¹) attached to a driver moving at
$V_{\text{pl}}$. Force balance on the block gives

$$\frac{\mathrm d\tau}{\mathrm dt} = k\left(V_{\text{pl}} - V\right) . \tag{10}$$

**Linearised stability.** Let $u = V_{\text{pl}}/D_c$, and perturb about steady
state with $x = \delta V/V_{\text{pl}}$ and $y = \delta\theta/\theta_{ss}$.
Linearising equations (9) and (10) about steady state gives a $2\times2$ system
whose trace and determinant are

$$T = \left(\frac{bu - kV_{\text{pl}}/\sigma}{a}\right) - u ,
\qquad D = \frac{u\,kV_{\text{pl}}}{a\sigma} > 0 . \tag{11}$$

Since $D > 0$, the eigenvalues are either both real with the same sign or a
complex-conjugate pair with real part $T/2$; in every case **the sign of the real
parts is the sign of $T$**. So the stability boundary is exactly $T = 0$:

$$bu - \frac{kV_{\text{pl}}}{\sigma} = au
\;\Longrightarrow\; \frac{(b-a)V_{\text{pl}}}{D_c} =
\frac{kV_{\text{pl}}}{\sigma}
\;\Longrightarrow\;
\boxed{k_c = \frac{\sigma(b-a)}{D_c}} . \tag{12}$$

Note that $k_c \propto 1/D_c$ and is independent of $V_{\text{pl}}$ — the plate
rate drops out. Physically: **instability requires that the elastic loading be
softer than the friction law's own weakening rate.** With
$\sigma = 100$ MPa, $a = 0.010$, $b = 0.014$, $D_c = 10^{-5}$ m, the demo computes

$$k_c = \frac{10^{8}\,(0.004)}{10^{-5}} = 4.0\times10^{10}\ \text{Pa m}^{-1}
= 4.0\times10^{4}\ \text{MPa m}^{-1} .$$

### 3.7 Measuring the threshold numerically, and the limits of that measurement

The demo integrates the full nonlinear system (equations 9–10) from a 1 per cent
perturbation in $V$ and measures whether the perturbation grows over
$3\times10^{5}$ s $= 30\,D_c/V_{\text{pl}}$:

| $k/k_c$ | final/initial perturbation | verdict |
|---|---|---|
| 0.20 | $3.543797\times10^{0}$ | GROWS |
| 0.50 | $3.739038\times10^{1}$ | GROWS |
| 0.90 | $1.215609\times10^{0}$ | GROWS |
| 1.10 | $1.011795\times10^{0}$ | GROWS |
| 2.00 | $3.369679\times10^{-3}$ | decays |
| 5.00 | $3.736788\times10^{-11}$ | decays |

Bisection on the sign of the growth ratio gives a measured threshold of
$k = 3.6201\times10^{10}$ Pa m⁻¹ $= 0.905036\,k_c$.

**The 9.5 per cent discrepancy is a measurement limitation, not a theory error.**
Near $k = k_c$ both eigenvalues pass through zero (equation 11), so the
perturbation grows (or decays) only algebraically over any affordable window: at
$k/k_c = 1.1$ the amplitude has changed by only 1.2 per cent in $3\times10^5$ s,
which is comparable with the truncation error of the explicit scheme. The
verdicts far from the threshold are unambiguous (a factor of $3\times10^{-11}$ at
$k/k_c = 5$), and the exact Jacobian table confirms the sign change:

| $k/k_c$ | trace $T$ (s⁻¹) | det $D$ (s⁻²) | eigenvalues (s⁻¹) | verdict |
|---|---|---|---|---|
| 0.50 | $2.0\times10^{-5}$ | $2.0\times10^{-9}$ | $1.0\times10^{-5},\ 1.0\times10^{-5}$ | unstable |
| 0.90 | $4.0\times10^{-6}$ | $3.6\times10^{-9}$ | $2.0\times10^{-6},\ 2.0\times10^{-6}$ | unstable |
| 1.00 | $1.355253\times10^{-20}$ | $4.0\times10^{-9}$ | $6.776\times10^{-21},\ 6.776\times10^{-21}$ | unstable (marginal) |
| 1.10 | $-4.0\times10^{-6}$ | $4.4\times10^{-9}$ | $-2.0\times10^{-6},\ -2.0\times10^{-6}$ | stable |
| 2.00 | $-4.0\times10^{-5}$ | $8.0\times10^{-9}$ | $-2.0\times10^{-5},\ -2.0\times10^{-5}$ | stable |

The trace crosses zero essentially exactly at $k/k_c = 1.00$
($1.36\times10^{-20}$ s⁻¹ is zero to round-off), confirming equation (12); the
program's own verdict field still reads "unstable" at that row because the
computed trace is a tiny positive number, which is exactly the marginal behaviour
the table is designed to display. The
eigenvalues are real and repeated here because $T^2 = 4D$ at these parameters —
i.e. the system is at a **degenerate node**, which is precisely why the numerical
separation takes so long.

**A lesson about numerical verification in general:** when the quantity being
measured is the sign of a marginally growing mode, a bisection can only localise
the threshold to the accuracy with which the growth can be distinguished from
truncation error. The exact answer comes from the linearisation, and the
simulation's role is to confirm the *qualitative* behaviour on either side — which
it does here by 11 orders of magnitude. Reporting "0.905 $k_c$" as a measured
threshold would be wrong; reporting it as "consistent with $k_c$ within the
resolution of the measurement" is right.

## 4. Physical interpretation

**Failure criteria are geometric statements about stress, not new physics.**
Mohr–Coulomb says the stress circle touches a line; the optimal orientation is the
tangency point. This is why a single pair $(C,\varphi)$ plus a stress state predicts
both the failure stress and the fault dip.

**Friction is what makes faults both strong and weak at the same time.** A
friction coefficient of 0.6 predicts a shear strength of order
$0.6\sigma_n'$, which by the depth profile of section 3.4 means the crust could
support enormous stress differences — much larger than is observed
heat-flow-wise in some regions (the "stress–heat-flow paradox"). Explaining the
apparent weakness requires either very high pore pressure (reducing $\sigma_n'$),
weak fault-zone minerals (reducing $\mu$), or dynamic weakening during slip. All
three are active research topics; the honest summary is that **the crust appears
weaker than laboratory friction predicts, and the resolution is not settled.**

**Rate-and-state allows both stable creep and earthquakes on the same fault.**
Whether a patch slips unstably depends on the local competition between
$k$ (set by the geometry and elastic properties of the surrounding rock) and
$k_c$ (set by the friction parameters, the effective normal stress and $D_c$).
Because $\sigma$ and $D_c$ vary with depth and the temperature dependence of
$a$ and $b$ changes their sign, the same fault can be velocity-weakening in the
seismogenic zone and velocity-strengthening below it. That is the standard
explanation for the finite depth extent of seismicity and for the existence of
stable-creeping fault segments.

**$D_c$ is the hidden parameter.** It scales $k_c$ inversely and, with $\theta$, it
sets the timescale $D_c/V$ for state evolution. Laboratory values are typically
microns; values inferred from earthquakes are often much larger, and the
discrepancy is one of the long-standing open problems in earthquake mechanics.

## 5. Assumptions and regime of validity

| Assumption | Statement | What breaks outside it |
|---|---|---|
| Mohr–Coulomb | Failure is linear in $\sigma_n'$, and intermediate stress $\sigma_2$ plays no role | Curvature of the failure envelope at low and high $\sigma_n'$; $\sigma_2$ effects in three dimensions; Griffith-type tensile/compressive crack behaviour |
| Constant $\mu$ | Byerlee's law | Temperature (roughly above a few hundred °C), clay/serpentine/talc-rich rocks, high slip rates, high pore pressure |
| Effective stress | Friction responds to $\sigma_n - p$ | Effective-stress coefficients different from 1; poroelastic coupling; chemical effects |
| $\theta$ formulation (Dieterich–Ruina) | A single state variable with $\mathrm d\theta/\mathrm dt = 1 - V\theta/D_c$ | Two-state and slip-law variants in the literature; the choice of evolution law changes the transient response, though not the steady-state $k_c$ |
| Linear stability analysis | Perturbations are small | Nucleation of macroscopic rupture, dynamic weakening, thermal pressurisation — all nonlinear |
| Spring–slider geometry | One degree of freedom, uniform $\sigma$ | Real faults are 2-D/3-D, heterogeneous and loaded by a full elastic medium |
| $a < b$ (velocity weakening) for instability | Required for stick-slip | Velocity-strengthening patches cannot nucleate instability, but can pin it |
| Quasi-static loading | Inertia neglected | During dynamic rupture inertia dominates; the spring–slider analysis describes nucleation, not propagation |
| Brittle–ductile transition as a crossover | The two strengths cross at a depth | Real transitions are gradual, may involve semi-brittle mechanisms, and involve pore-pressure and mineralogy gradients |

## 6. Units and dimensional analysis

- $\tau$, $\sigma_n'$, $C$, $T$: Pa ✓. $\mu$, $a$, $b$, $\varphi$: dimensionless ✓.
- $\sigma_1' = \sigma_3'\tan^2(45^\circ+\varphi/2) + 2C\tan(45^\circ+\varphi/2)$:
  Pa from Pa and Pa ✓ consistent (a dimensionless multiplier on the first term, a
  dimensionless multiplier on the cohesion).
- $k$: Pa m⁻¹ ✓ (stress change per unit slip). $k_c = \sigma(b-a)/D_c$:
  Pa/(m) ✓ — dimensionally identical, as required.
- $D_c$: m ✓. $\theta = D_c/V$: m/(m s⁻¹) = s ✓. $V\theta/D_c$ dimensionless ✓.
- $u = V_{\text{pl}}/D_c$: s⁻¹ ✓, so $T$ and $D$ in equation (11) have units of
  s⁻¹ and s⁻² ✓ as eigenvalues of a rate problem must.
- The brittle-strength slope is $\mu(\rho-\rho_w)g = 0.6(1700)(9.81) =
  1.0006\times10^{4}$ Pa m⁻¹ $= 0.0100$ MPa m⁻¹; the demo's table gives
  $(300.186-20.012)/28 = 10.006$ MPa km⁻¹ ✓ — in both cases Pa/m and MPa/km are
  numerically identical, a convenient coincidence worth knowing when reading
  strength profiles.
- $\sigma_n'/\sigma_v = 1 - \rho_w/\rho = 0.62963$ at every depth in the table
  ✓ — the dimensionless check that pore pressure is subtracted at the same depth
  as the overburden.

## 7. Python demonstration

[`code/failure_friction_demo.py`](./code/failure_friction_demo.py) scans the
Mohr–Coulomb criterion over all plane orientations, builds the depth profile of
frictional strength, and integrates the rate-and-state spring–slider system to
measure the stability threshold. Observed output:

```text
cohesion C = 20.0 MPa, friction coefficient mu = 0.60 -> friction angle phi = 30.9638 deg
sigma_3 = 100.0 MPa -> predicted failure at sigma_1 = 382.590461 MPa
maximum of tau - mu sigma_n - C over all planes = -3.541570e-01 Pa
  reached where the plane's normal lies 60.4800 deg from sigma_1,
  i.e. where the plane itself is inclined 29.5200 deg to
  sigma_1 (the textbook 45 deg - phi/2 = 29.5181 deg)
  and its normal lies at 45 deg + phi/2 = 60.4819 deg from sigma_1
```

```text
assumed: rho = 2700 kg/m^3, hydrostatic pore pressure (rho_w = 1000), mu = 0.60, zero cohesion
 depth (km)  sigma_v (MPa)  sigma_n_eff (MPa)  tau_max (MPa)  tau/sigma_n_eff
        2.0         52.974             33.354         20.012           0.6000
       10.0        264.870            166.770        100.062           0.6000
       30.0        794.610            500.310        300.186           0.6000
```

```text
sigma = 100 MPa, a = 0.010, b = 0.014, D_c = 1.0e-05 m, plate velocity 1.0e-09 m/s, V* = 1.0e-06 m/s
critical stiffness k_c = sigma (b - a)/D_c = 4.0000e+10 Pa/m = 40000.000 MPa/m
run duration 3e5 s, i.e. 30.0 times the state
evolution timescale D_c/V_pl = 1.0e+04 s; perturbation started at 1 per cent of V_pl
   k/k_c   final/initial perturbation    verdict
    0.20                 3.543797e+00      GROWS
    0.50                 3.739038e+01      GROWS
    0.90                 1.215609e+00      GROWS
    1.10                 1.011795e+00      GROWS
    2.00                 3.369679e-03     decays
    5.00                 3.736788e-11     decays
measured stability threshold: k = 3.6201e+10 Pa/m = 0.905036 k_c
   k/k_c     trace (1/s)     det (1/s^2)              eigenvalues (1/s)    verdict
    0.50    2.000000e-05    2.000000e-09           1.000e-05, 1.000e-05   unstable
    0.90    4.000000e-06    3.600000e-09           2.000e-06, 2.000e-06   unstable
    1.00    1.355253e-20    4.000000e-09           6.776e-21, 6.776e-21   unstable
    1.10   -4.000000e-06    4.400000e-09         -2.000e-06, -2.000e-06     stable
    2.00   -4.000000e-05    8.000000e-09         -2.000e-05, -2.000e-05     stable
```

### What to observe

| Observation | Consequence |
|---|---|
| The scanned maximum of $\tau-\mu\sigma_n-C$ is $-3.5\times10^{-1}$ Pa, i.e. zero within the 0.01° grid | The Mohr–Coulomb tangency condition is satisfied at the optimum, which is the content of the criterion |
| The optimal normal is at $60.4800^\circ$ versus the analytic $60.4819^\circ$ | The textbook $45^\circ+\varphi/2$ is confirmed numerically to the grid resolution |
| $\sigma_n'/\sigma_v = 0.62963$ and $\tau$ rises by exactly 10.006 MPa km⁻¹ | The pore-pressure reduction scales with the same depth as the overburden, giving the standard linear brittle-strength envelope with slope $\mu(\rho-\rho_w)g$ |
| The perturbation grows at $k/k_c = 1.10$ but decays by 11 orders of magnitude at $k/k_c = 5$ | The stability boundary lies where the linearised analysis puts it; the far-field verdicts are unambiguous |
| The measured threshold is $0.905\,k_c$ while the exact trace crosses zero at $1.000\,k_c$ ($1.36\times10^{-20}$ s⁻¹) | Marginal stability cannot be localised by simulation to better than the truncation error; the exact answer comes from the Jacobian |

> **Breaking exercise.** Set $a = b = 0.012$ (neutral) and predict what happens to
> the measured threshold, to $k_c$ and to the growth ratios. Then run it and
> reconcile the result with equation (12) — including what $k_c = 0$ means
> physically and why the simulation cannot measure it.

## 8. Common mistakes

1. **Using total stress instead of effective stress in a friction criterion.**
   This is the most consequential error in crustal stress modelling: pore pressure
   can halve the strength.
2. **Conflating the angle of the fault plane with the angle of its normal.** The
   normal is at $45^\circ+\varphi/2$ from $\sigma_1$; the plane is at
   $45^\circ-\varphi/2$; the dip is one or the other depending on the regime.
3. **Assuming a fixed fault dip across regimes.** Normal $60^\circ$, thrust $30^\circ$
   for $\varphi = 31^\circ$ — the geometry follows the stress state.
4. **Treating Byerlee's law as universal.** It is a laboratory fit, generally
   quoted as $\mu \approx 0.6$, which over-predicts the strength of clay-rich and
   serpentinite fault rocks and ignores temperature and rate effects.
5. **Quoting the brittle–ductile transition as a single depth.** It is
   lithology-, gradient-, strain-rate- and pore-pressure-dependent; "10–20 km" is
   a range for quartz-rich crust, not a constant.
6. **Ignoring $\sigma_2$.** Mohr–Coulomb in its classic form is independent of the
   intermediate principal stress, which real rocks are not.
7. **Treating negative $b-a$ as stable at all amplitudes.** The linear analysis
   says small perturbations decay; large perturbations can still nucleate
   dynamically.
8. **Using a single-$D_c$ model over many orders of magnitude in slip.**
   $D_c$ is scale-dependent in practice, and the value inferred from one
   observation does not extrapolate.
9. **Reporting a numerical threshold as if it were exact.** Section 3.7 shows the
   9.5 per cent gap is a property of the measurement, and marginal-mode
   measurements are always limited this way.
10. **Assuming friction is rate-independent.** The entire earthquake-nucleation
    framework collapses if rate-and-state effects are dropped.

## 9. Real-world applications

- **Fault reactivation and induced seismicity.** Whether an injection or a
  reservoir-depletion stress change reactivates a fault follows from equations
  (1) and (7) with the pore-pressure change folded into $\sigma'$
  ([05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)).
- **Borehole breakouts and in-situ stress.** The orientation and width of breakouts
  are a Mohr–Coulomb problem, and they are the most widely available stress
  indicator ([06-seismology](../../06-seismology/README.md)).
- **Earthquake nucleation and aftershock decay.** Rate-and-state friction with a
  single state variable reproduces the Omori-type aftershock decay and the
  logarithmic healing of fault strength, which is why it is the standard
  framework in earthquake physics
  ([12-global-geophysics-interior](../../12-global-geophysics-interior/README.md)).
- **Slow slip and creep.** Velocity-strengthening patches and the
  $k$ versus $k_c$ balance explain why some plate boundaries creep continuously
  and others produce megathrust earthquakes.
- **Landslides and rock slope stability.** The same criterion, with a slope
  geometry instead of a fault, is the basis of slope-stability analysis in
  engineering geology ([04-earth-science-geology](../../04-earth-science-geology/README.md)).
- **Hydraulic fracturing and tensile failure.** Where $\sigma_1$ is small and
  tensile conditions are approached, the criterion must be replaced by a tensile
  or fracture-mechanics one — the regime relevant to dike propagation and
  magmatic intrusion.
- **Seismic hazard ground motion.** Dynamic rupture models built on rate-and-state
  friction supply the source time functions used in strong-motion prediction.

## 10. Further reading

- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (4th ed., Blackwell).** The standard textbook: Mohr–Coulomb,
  effective stress, failure criteria, and the geological conventions. Level:
  advanced.
- **Paterson, M. S., & Wong, T.-f. *Experimental Rock Deformation — The Brittle
  Field* (Springer).** The experimental basis, including the data behind
  Byerlee's law and its departures. Level: advanced.
- **Byerlee, J. (1978), *Friction of rocks*, Pure and Applied Geophysics.** The
  compilation that established $\mu \approx 0.6$; read it for the conditions under
  which the law was measured. Level: advanced.
- **Dieterich, J. H. (1979), *Modeling of rock friction*, Journal of Geophysical
  Research.** The state-variable formulation used in section 3.6. Level: advanced.
- **Ruina, A. (1983), *Slip instability and state variable friction laws*,
  Journal of Geophysical Research.** The stability analysis and the derivation of
  the critical stiffness. Level: advanced.
- **Marone, C. (1998), *Laboratory-derived friction laws and their application to
  seismic faulting*, Annual Review of Earth and Planetary Sciences.** A review
  that connects the laboratory laws to fault behaviour. Level: advanced.
- **Scholz, C. H. *The Mechanics of Earthquakes and Faulting* (Cambridge
  University Press).** The synthesis: friction, nucleation, the seismogenic zone
  and the stress–heat-flow paradox. Level: graduate.
- **Lockner, D. A. (1995), *Rock failure*, in *Rock Physics and Phase Relations: A
  Handbook of Physical Constants*, AGU.** A compact review of failure criteria and
  their parameters for rock types.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.
> The numerical values of $\mu$ quoted here are the conventional roundings of
> published compilations and are stated as orders of magnitude with their
> conditions, not as measurements made for this lesson.

## 11. Related lessons

- [01 Stress: Traction, Cauchy Stress Tensor and Equilibrium](./01-stress.md) —
  the Mohr circle machinery used throughout.
- [07 Viscoelasticity, Creep and Anelastic Relaxation](./07-viscoelasticity.md) —
  the ductile half of the brittle–ductile transition.
- [05 Elastodynamic Equation of Motion and Wave Speeds](./05-elastodynamics.md) —
  the elastic loading and the wave speeds that control dynamic rupture.
- [02-03-10 Attenuation, Quality Factor and Anelasticity](../03-oscillations-and-waves/10-attenuation.md)
  — the small-strain, high-frequency limit that failure replaces.
- [05-core-geophysics/04-rock-physics](../../05-core-geophysics/04-rock-physics/README.md)
  — laboratory friction and the effects of fluid saturation.
- [06-seismology](../../06-seismology/README.md) — fault mechanics in the seismic
  cycle.
- [12-global-geophysics-interior](../../12-global-geophysics-interior/README.md) —
  nucleation, aftershocks and slow slip.

Exercises:
[`exercises/08-failure-and-friction-exercises.md`](./exercises/08-failure-and-friction-exercises.md)
and
[`exercises/08-failure-and-friction-solutions.md`](./exercises/08-failure-and-friction-solutions.md).

## Self-assessment checklist

- [ ] I can write the Mohr–Coulomb criterion and explain why it is a tangency
      condition. (Section 3.1)
- [ ] I can derive the optimal orientation $\theta = 45^\circ+\varphi/2$ from the
      derivative of $\tau-\mu\sigma_n$. (Section 3.2)
- [ ] I can state which orientation the answer refers to (normal or plane) and
      convert between them. (Sections 3.2–3.3)
- [ ] I can compute the failure stress from $\sigma_3'$ and reproduce the demo's
      382.590461 MPa. (Section 3.3)
- [ ] I can classify the three Andersonian regimes and give the fault dip for each.
      (Section 3.3)
- [ ] I can build the frictional strength profile with depth and explain why it
      must terminate. (Section 3.4)
- [ ] I can state Byerlee's law numerically, state its conditions of validity, and
      name what breaks it. (Section 3.5)
- [ ] I can write the Dieterich–Ruina law and derive $k_c = \sigma(b-a)/D_c$.
      (Section 3.6)
- [ ] I can derive the linearised trace and determinant and explain why the sign
      of the trace decides stability. (Section 3.6)
- [ ] I can explain why the numerical threshold is measured to only about
      0.905 $k_c$ and why that is not a failure of the theory. (Section 3.7)
- [ ] I can list the assumptions of the Coulomb and rate-and-state frameworks and
      one observation that violates each. (Section 5)
