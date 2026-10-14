---
id: 02-07-04
title: "Faraday's Law, Induction and Eddy Currents"
level: advanced
prereqs: ["02-07-02", "02-07-03", "01-06-06"]
estimated_minutes: 90
tags: [faraday-law, induction, eddy-currents, magnetic-diffusion, geodynamo]
---

# Faraday's Law, Induction and Eddy Currents

## Learning objectives

By the end of this lesson you will be able to:

1. **State** Faraday's law in flux form and explain the three distinct ways the
   flux through a circuit can change.
2. **Distinguish** transformer EMF (changing field, fixed loop) from motional EMF
   (moving conductor in a steady field) and compute both.
3. **Apply** Lenz's law as an energy statement rather than a sign rule, and
   explain why a conductor screens a *changing* field but not a static one.
4. **Derive** the magnetic induction equation for a moving conductor,
   $\partial\mathbf B/\partial t = \nabla\times(\mathbf u\times\mathbf B) + \eta\nabla^2\mathbf B$,
   and the **magnetic Reynolds number** $R_m = \mu\sigma u L$ that decides whether
   advection or diffusion wins.
5. **Derive** and verify the similarity solution of magnetic diffusion from a step
   field, $\mathbf B/B_0 = \operatorname{erfc}\!\left(z/2\sqrt{Dt}\right)$, and
   the $z \propto \sqrt{Dt}$ penetration law.
6. **Compute** the eddy-current density and the ohmic dissipation
   $\mathbf J\cdot\mathbf E = \sigma E^2$.
7. **Quantify** the diffusion time $\mu_0\sigma L^2$ at laboratory, crustal and
   core scales, and use it to show that the geomagnetic field **must** be
   maintained by dynamo action.

## Prerequisites

- [02-07-02 Magnetostatics, Biot–Savart and Ampère's Law](./02-magnetostatics.md)
  — the flux of a dipole field, and the field of a loop.
- [02-07-03 Maxwell's Equations and Their Physical Meaning](./03-maxwell-equations.md)
  — Faraday's law as equation III, and the diffusion equation.
- [01-06-06 The Integral Theorems](../../01-mathematics/06-multivariable-calculus/06-integral-theorems.md)
  — Stokes' theorem, needed to move between the integral and differential forms.

## 1. Faraday's law

For a circuit bounding a surface $S$ threaded by magnetic flux
$\Phi_B = \int_S\mathbf B\cdot\mathrm d\mathbf A$, the electromotive force around
the circuit is

$$\boxed{\ \mathcal E = \oint\mathbf E\cdot\mathrm d\boldsymbol\ell
= -\frac{\mathrm d\Phi_B}{\mathrm dt}\ }
\qquad\text{(Faraday's law),} \tag{1}$$

and in differential form

$$\nabla\times\mathbf E = -\frac{\partial\mathbf B}{\partial t} . \tag{2}$$

The minus sign is not a convention; it is the content of **Lenz's law**: the
induced EMF drives currents whose magnetic effect *opposes the change* that
produced them. Equivalently, the induced effect always dissipates energy taken
from the agent doing the changing. If the sign were positive, nature would
amplify any fluctuation and no stable configuration would exist.

**Three ways to change the flux.** From
$\Phi_B = \int_S\mathbf B\cdot\mathrm d\mathbf A$, a change can come from

1. a **time-varying field** in a fixed circuit — the *transformer* EMF, the basis
   of EM soundings, induction logging and every transformer;
2. a **moving circuit** in a steady field — the *motional* EMF,
   $\mathcal E = \oint(\mathbf u\times\mathbf B)\cdot\mathrm d\boldsymbol\ell = BLv$
   for the textbook rod, the basis of the geodynamo, of magnetometer noise on a
   moving vehicle, and of the Faraday disc generator;
3. a **changing geometry** (a loop being deformed, a coil being rotated) — the
   basis of every electric generator.

The three are often mislabelled "the same thing". They are the same *law*, but the
first is a field property and the second is a material property: the motional EMF
exists even when $\partial\mathbf B/\partial t = 0$ everywhere, and it is the one
that couples velocity to magnetic field in a fluid.

**Magnitude.** A 10 cm radius, single-turn loop in a 50 µT field
(the geomagnetic field) oscillating at 50 Hz sees a peak EMF

$$\mathcal E_{\text{peak}} = \pi a^2 B_0\omega
= \pi(0.1)^2(50\times10^{-6})(2\pi\times50) = 4.93\times10^{-4}\ \mathrm V
= 0.49\ \mathrm{mV}. \tag{3}$$

Half a millivolt at mains frequency from a small coil in the Earth's field. This
single number explains why: EM receivers are shielded and their mains harmonics
notched; why the "telluric" noise below 1 Hz is dominated by natural fields while
the 50/60 Hz band is dominated by human sources; and why a stationary
magnetotelluric site is fussier about power lines than about geology.

## 2. Physical interpretation: eddy currents and what they measure

Put a conductor in a time-varying magnetic field and Faraday's law does the rest.
The induced electric field drives currents — **eddy currents** — that circulate in
closed loops inside the conductor, dissipate energy as $\sigma E^2$ per unit
volume, and generate a **secondary** magnetic field that opposes the change of the
primary field. That secondary field is what every EM method measures.

- **The measured quantity is a ratio.** A receiver measures
  $\mathbf B_{\text{total}} = \mathbf B_{\text{primary}} + \mathbf B_{\text{secondary}}$,
  and the useful datum is $\mathbf B_{\text{secondary}}/\mathbf B_{\text{primary}}$
  or some equivalent (a transfer function, an apparent resistivity, a decay
  curve). This is why EM systems are *ratio* instruments: source strength cancels
  to first order.
- **Frequency and geometry select depth.** The eddy currents are excluded from
  the interior of a good conductor at high frequency (the skin effect;
  [02-07-06](./06-em-in-conductors.md)) and penetrate deeper at low frequency.
- **Lenz is why a conductor screens.** A sheet of copper does not block a static
  magnetic field, but it strongly attenuates a changing one: the eddy currents
  are induced precisely in proportion to the rate of change, so a good conductor
  looks like a perfect diamagnet at high enough frequency. This is the physics of
  EM shielding, of the "screen" used in TEM surveys, and of the difficulty of
  measuring anything magnetic next to moving metal.

## 3. Induction in a moving conductor: the induction equation

Combine Faraday's law (2) with Ampère's law
$\nabla\times\mathbf H = \mathbf J$ (quasi-static), Ohm's law *in the frame of the
moving conductor*, $\mathbf J = \sigma(\mathbf E + \mathbf u\times\mathbf B)$, and
$\nabla\cdot\mathbf B = 0$. The result, after using
$\nabla\times(\nabla\times\mathbf B) = -\nabla^2\mathbf B$, is the **magnetic
induction equation**:

$$\boxed{\ \frac{\partial\mathbf B}{\partial t}
= \underbrace{\nabla\times(\mathbf u\times\mathbf B)}_{\text{advection}}
+ \underbrace{\eta\nabla^2\mathbf B}_{\text{diffusion}}\ }
\qquad
\eta \equiv \frac{1}{\mu\sigma} . \tag{4}$$

The relative size of the two terms, for a flow of speed $u$ over a length $L$, is
the **magnetic Reynolds number**

$$\boxed{\ R_m = \frac{|\nabla\times(\mathbf u\times\mathbf B)|}{|\eta\nabla^2\mathbf B|}
\sim \mu\sigma u L\ } . \tag{5}$$

- $R_m \ll 1$: diffusion wins. The field is slaved to the source, its structure is
  set by conductivity, and this is the regime of every exploration EM method (the
  ground does not move, or moves far too slowly to matter).
- $R_m \gg 1$: advection wins. Field lines are frozen into the fluid and are
  stretched, twisted and amplified by the flow. This is the regime of the
  geodynamo.

For the core with $\sigma \approx 10^{6}$ S/m (a **nominal** value; the core
conductivity is genuinely uncertain and actively debated, with published estimates
differing by a factor of a few) and $u \approx 10^{-3}$ m/s (a nominal
large-scale flow speed inferred from secular variation), equation (5) gives

$$R_m = \mu_0\sigma u L \approx (1.2566\times10^{-6})(10^{6})(10^{-3})(3.5\times10^{6})
\approx 4.4\times10^{3} \gg 1 . \tag{6}$$

The necessary condition for a self-sustaining dynamo is therefore met. It is *not*
sufficient — the flow must also have the right geometry, which is why dynamo
theory is a research subject
([08-01-05 Dynamo Theory](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md)).

## 4. Magnetic diffusion: the solution that has no wavefront

With $\mathbf u = 0$ (or $R_m\ll1$), equation (4) reduces to the diffusion
equation of the previous lesson:

$$\frac{\partial\mathbf B}{\partial t} = \frac{1}{\mu\sigma}\nabla^2\mathbf B
\equiv D\nabla^2\mathbf B . \tag{7}$$

**The cosine solution.** A field imposed at the surface of a half-space,
$B(0,t) = B_0\cos\omega t$, penetrates as

$$B(z,t) = B_0\,e^{-z/\delta}\cos\!\left(\omega t - z/\delta\right),
\qquad
\delta = \sqrt{\frac{2}{\mu\sigma\omega}} . \tag{8}$$

The field decays *and* lags by exactly the same amount $z/\delta$ in radians. That
identity — decay exponent equals phase lag — is the signature of a diffusion
equation, and it is why magnetotelluric impedances are complex and why every
half-space MT phase is 45°. Lesson [02-07-06](./06-em-in-conductors.md) derives
$\delta$ and verifies it numerically.

**The step solution.** A field switched on at $t = 0$ and held at $B_0$ at the
surface gives the similarity solution

$$B(z,t) = B_0\,\operatorname{erfc}\!\left(\frac{z}{2\sqrt{Dt}}\right) , \tag{9}$$

so the depth at which the field has fallen to any given fraction grows as
$\sqrt{Dt}$: **diffusion has no front**. A signal does not "arrive"; it seeps. The
half-amplitude depth in the demo is $z_{1/2} = 0.9538\sqrt{Dt}$ at every time, and
the constant $0.9538$ is $2\times0.4769$ where
$\operatorname{erfc}(0.4769) = 0.5$.

**Diffusion time.** From $\tau \sim \mu\sigma L^2$:

| Scale | $\sigma$ (S/m) | $L$ (m) | $\tau = \mu_0\sigma L^2$ | $\tau$ |
|---|---|---|---|---|
| laboratory, copper-like | $5.96\times10^{7}$ | 1 | $7.49\times10^{1}$ s | 75 s |
| crust | $10^{-2}$ (100 Ω·m) | $10^4$ (10 km) | 1.2566 s | 1.3 s |
| core | $10^{6}$ (nominal) | $3.48\times10^{6}$ | $1.52\times10^{13}$ s | $4.8\times10^{5}$ yr |

The crustal entry is remarkable and explains a great deal of practice: **the
magnetic field re-arranges itself across 10 km of 100 Ω·m rock in about a
second.** That is why magnetotellurics at periods of seconds probes the mid-crust,
why geomagnetic depth sounding at periods of hours probes the mantle, and why a
magnetic observatory records secular variation driven by core flow rather than by
crustal diffusion.

For the fundamental free-decay mode of a sphere, $\tau = \mu_0\sigma R^2/\pi^2$,
which for the core gives about $4.9\times10^{4}$ years (again with the nominal
$\sigma = 10^{6}$ S/m). Compare that with the age of the Earth,
$4.5\times10^{9}$ yr: the ratio is $1.1\times10^{-5}$. **Diffusion alone would
destroy the geomagnetic field in tens of thousands of years, four to five orders
of magnitude faster than the Earth is old.** This is the quantitative argument for
dynamo action, and it is one of the strongest inferences in geophysics: from a
measured field, a measured Earth age and a plausible conductivity, one concludes
that the core must be a self-sustaining dynamo.

**Observable consequences of the dynamo.** The induction equation plus core flow
predicts: secular variation on decadal timescales (observed); westward drift of
field features (observed); geomagnetic reversals recorded in magnetised rocks
(observed, ~hundreds of events in the record); magnetohydrodynamic waves in the
core (inferred from rapid field changes); and a dipole moment that is not
constant (observed, currently decreasing). Palaeomagnetic records are the
long-term observable, and the persistent near-axial dipole despite reversals is
the key constraint on dynamo models.

## 5. Assumptions and regime of validity

| Assumption | Where it entered | What breaks outside it |
|---|---|---|
| Quasi-static: displacement current neglected | Deriving equation (4) from Ampère's law | The wave regime: $\sigma/(\omega\varepsilon)\lesssim1$, i.e. GPR frequencies in resistive ground (lesson [02-07-06](./06-em-in-conductors.md) §6) |
| Ohmic conductor with a *real*, frequency-independent $\sigma$ | $\mathbf J = \sigma\mathbf E$ | Induced polarisation: $\sigma$ is complex and frequency-dependent, and its imaginary part is the target of the IP method |
| Stationary medium | $\mathbf u = 0$ in equations (7)–(9) | The geodynamo and any moving-conductor problem; then $R_m$ decides whether the motional term matters |
| Neglect of propagation (retardation) in the air | The quasi-static field of a transmitter | When the coil separation approaches an air wavelength, an "air wave" arrives before the ground response and must be modelled separately |
| Linear response, hence superposition | Every forward solution | Dynamo problems (nonlinear through the Lorentz force) but not exploration EM |
| No interaction between the induced and remanent magnetisation | The diffusive formulation with $\mu = \mu_0$ | Strongly magnetic rock, where the magnetic permeability enters both the induction equation and the skin depth |
| The observed decay is caused by conductivity alone | Interpreting a decay curve | Coupling to conductive overburden, transmitter geometry and receiver response all appear in the same curve; the inversion must include them |
| For the free-decay estimate: uniform, scalar core conductivity, known length scale | Section 4 | The core conductivity is uncertain by a factor of a few and is anisotropic in a strong field; this is the weakest link in the dynamo argument (and it does not change the conclusion) |

The third and fifth rows deserve a comment. The induction equation is *linear in
$\mathbf B$ for a given flow*, which is why every exploration method can rely on
superposition and on transfer functions — but it is *nonlinear in the flow*, which
is why the dynamo is a different kind of problem. Reading a dynamo paper and an EM
survey paper side by side, the equations look alike and the mathematical structure
is not: one is a linear filter, the other a nonlinear dynamical system.

## 6. Units and dimensional analysis

- Faraday (1): $[\mathrm d\Phi/\mathrm dt] = \mathrm{Wb/s} = \mathrm{T\,m^2/s} = \mathrm{V}$ ✓.
- Differential form: $[\nabla\times\mathbf E] = \mathrm{(V/m)/m} = \mathrm{kg\,s^{-3}A^{-1}}$
  and $[\partial\mathbf B/\partial t] = \mathrm{T/s} = \mathrm{kg\,s^{-3}A^{-1}}$ ✓.
- Diffusivity: $[D] = [1/(\mu\sigma)] = \mathrm{(H/m)^{-1}(S/m)^{-1}}
  = \mathrm{m\,A^{-1}T^{-1}\cdot m\,S^{-1}}$; the SI check that is easier to
  trust is dimensional: from (7), $[\nabla^2B]/[\partial B/\partial t] = \mathrm{m^{-2}/s^{-1}} = \mathrm{m^2/s}$ ✓ so $D$ is m²/s and $\eta$ is m²/s.
- $R_m$: $[\mu\sigma uL] = \mathrm{(T\,m/A)(A\,V^{-1}m^{-1})(m/s)(m)} = \mathrm{T\,m^2V^{-1}s^{-1}}
  = \mathrm{Wb\,V^{-1}s^{-1}}$, dimensionless ✓.
- Motional EMF: $[vBL] = \mathrm{(m/s)(T)(m)} = \mathrm{(m/s)(kg\,s^{-2}A^{-1})(m)} = \mathrm{kg\,m^2s^{-3}A^{-1}} = \mathrm V$ ✓.

## 7. Python demonstration

[`code/em_induction_demo.py`](./code/em_induction_demo.py) verifies every claim
above. Observed output:

```text
loop radius a = 0.10 m, B = B0 sin(wt) with B0 = 50 uT, f = 50 Hz
loop area = 0.031416 m^2,  Phi0 = A B0 = 1.570796e-06 Wb
   t (s)        Phi (Wb)    -dPhi/dt numeric   -A B0 w cos(wt)
0.000000    0.000000e+00       -4.934802e-04     -4.934802e-04
0.005000    1.570796e-06       -0.000000e+00     -3.021695e-20
0.010000    1.923671e-22        4.934802e-04      4.934802e-04
peak EMF = A B0 omega = 4.934802e-04 V = 0.4935 mV
```

```text
rod of length 1.00 m moving at  1.00 m/s in B = 50 uT: EMF = v B L = 5.000000e-05 V
rod of length 1.00 m moving at  0.01 m/s in B = 50 uT: EMF = v B L = 5.000000e-07 V
rod of length 0.10 m moving at  1.00 m/s in B = 50 uT: EMF = v B L = 5.000000e-06 V
```

```text
sigma = 1 S/m, D = 1/(mu0 sigma) = 7.9577e+05 m^2/s
dz = 0.005 m, dt = 5.0e-12 s, CFL = 0.1592 (stable below 0.5), domain 1.20 m
z (m)     B(z,10ns)     B(z,20ns)     B(z,40ns)   erfc(z/2sqrt(Dt))
0.000      1.000000      1.000000      1.000000            1.000000
0.020      0.874021      0.910739      0.936819            0.936821
0.040      0.751163      0.822591      0.874033            0.874037
0.080      0.525942      0.653844      0.751186            0.751193
0.120      0.341443      0.501175      0.634349            0.634360
0.160      0.204648      0.369796      0.525981            0.525994
t (ns)    z at B=0.5 (m)    z/sqrt(Dt)     J = -(1/mu0)dB/dz
  10.0          0.085082      0.953764            5.0322e+06
  20.0          0.120333      0.953836            3.5586e+06
  40.0          0.170178      0.953849            2.5164e+06
residual of dB/dt = D d2B/dz2 for the similarity solution at z = 0.1 m, t = 40 ns:
  dB/dt = 3.654270e+06,  D d2B/dz2 = 3.654272e+06,  |residual|/|dB/dt| = 5.559e-07
```

```text
at t = 40 ns, z = 2 cm, sigma = 1.0 S/m:
  B/B0 = 0.936821, dB/dz = -3.152359e+00 T/m
  eddy current density J = -(1/mu0) dB/dz = 2.508567e+06 A/m^2
  electric field E = J/sigma = 2.508567e+06 V/m
  ohmic dissipation J E = 6.292910e+12 W/m^3
```

```text
tau = mu0 sigma L^2 (the order-of-magnitude magnetic diffusion time):
                       scale   sigma (S/m)       L (m)       tau (s)      tau (yr)
laboratory (1 m, copper-like)      5.96e+07           1    7.4896e+01     2.373e-06
    crust (10 km, 100 ohm m)          0.01       1e+04    1.2566e+00     3.982e-08
     core (3480 km, 1e6 S/m)         1e+06    3.48e+06    1.5218e+13     4.822e+05

fundamental free-decay mode of a sphere, tau = mu0 sigma R^2/pi^2:
  sigma_core = 1e+06 S/m (NOMINAL and debated; L = 3.48e+06 m)
  tau = 1.5419e+12 s = 4.886e+04 yr
  ratio tau / age of the Earth (4.5e9 yr) = 1.086e-05

magnetic Reynolds number Rm = mu0 sigma u L with u = 0.001 m/s
(NOMINAL core flow speed), L = 3.5e+06 m: Rm = 4.3982e+03
```

### What to observe

| Observation | Consequence |
|---|---|
| The finite-difference derivative of the flux matches $-\pi a^2B_0\omega\cos\omega t$ to four significant figures at every sampled time | Faraday's law as an identity about a *flux*, with the numerical residual at the level of the differencing step |
| Peak EMF is 0.4935 mV for a 10 cm coil in a 50 µT, 50 Hz field | The mains-frequency pickup scale that every EM receiver is designed around |
| $vBL$ for $v = 1$ m/s, $L = 1$ m, $B = 50$ µT is 50 µV | Real motional noise for a moving sensor; it is why MT coils are levelled and why towed systems have motion sensors |
| The explicit diffusion solve matches $\operatorname{erfc}(z/2\sqrt{Dt})$ to $10^{-5}$ absolute, and the PDE residual is $5.6\times10^{-7}$ relative | Equation (9) is the solution of equation (7); the similarity solution is verified, not assumed |
| $z_{1/2}/\sqrt{Dt}$ is 0.9538, 0.9538, 0.9538 at three times spanning a factor 4 | The penetration law is exactly $\sqrt t$: there is no wavefront and no "velocity" |
| $\mathbf J = -(1/\mu_0)\,\mathrm dB/\mathrm dz$ reaches $2.5\times10^6$ A/m² | Eddy currents can be enormous locally; the dissipation $\sigma E^2$ is what makes diffusion irreversible |
| At 10 km and $\sigma = 0.01$ S/m, $\tau = 1.2566$ s | Seconds-scale MT data reach the mid-crust; hours-scale data reach the mantle |
| The core diffusion time is $\sim5\times10^5$ yr, or $4.9\times10^4$ yr for the fundamental mode, against an Earth age of $4.5\times10^{9}$ yr | Diffusion alone cannot sustain the geomagnetic field: the dynamo conclusion is quantitative |
| $R_m \approx 4.4\times10^{3}$ for nominal core parameters | The necessary condition for dynamo action is satisfied by three orders of magnitude |

> **Breaking exercise.** Change the demo's conductivity from 1 S/m to 0.01 S/m
> (a rock-like value) and predict the new values of $D$, the required
> $\Delta t$ for stability, and the time at which the 0.5 contour reaches 0.2 m.
> Then verify by running. Finally, estimate the largest time step that would be
> needed, and explain why time-domain EM modelling of the crust at laboratory
> precision is a computational problem rather than a physical one.

## 8. Common mistakes

1. **Treating the induced EMF as "voltage across the loop".** It is an EMF, an
   integral of $\mathbf E$ around a path; only when the loop has a resistance does
   it become a current.
2. **Applying Lenz's law as a sign convention only.** The sign encodes energy
   conservation; if a change were amplified, the system would be unstable.
3. **Believing a conductor blocks magnetic fields.** It blocks *changes*; a static
   field passes through unchanged (no magnetic screening by a non-magnetic
   conductor).
4. **Using $D = 1/(\mu\sigma)$ but with a resistivity in the wrong units.** In
   geophysics $\rho$ is in Ω·m and $\sigma = 1/\rho$ in S/m; a factor of $10^{3}$
   error here is easy and is common in field reports.
5. **Reading an "arrival time" from a diffusive response.** Penetration is
   $\sqrt{Dt}$, not a constant speed; a "velocity" quoted from an EM delay is not
   a physical transport speed.
6. **Forgetting that the motional EMF requires a conductor that moves through the
   field.** A stationary observer in a changing field measures the transformer
   EMF; the two must be added only with attention to the reference frame.
7. **Assuming the core conductivity is known.** Published estimates differ by a
   factor of a few; every conclusion that depends on it should be reported with
   that caveat, as the free-decay estimate above is.
8. **Concluding that a large $R_m$ proves a dynamo.** It is a necessary condition.
   Whether a given flow sustains a field is a question for dynamo theory.

## 9. Real-world applications

- **Time-domain EM (TEM).** A transmitter current is switched off and the decaying
  secondary field is recorded. The decay is diffusive; late-time data see deeper.
- **Frequency-domain and airborne EM.** Same physics in the frequency domain; the
  in-phase and quadrature components carry the ratio information.
- **Induction logging.** A borehole coil induces eddy currents in the formation and
  measures the secondary field, which depends on formation conductivity.
- **Ore-body and metal detection.** Massive sulphides and buried metal have
  conductivities orders of magnitude above their host, which is why EM is the
  primary exploration tool for them (and why it is also the primary tool for
  finding buried pipes and unexploded ordnance).
- **Geomagnetic depth sounding and magnetotellurics.** The diffusive penetration of
  natural magnetic variations, measured as amplitude and phase, maps conductivity
  with depth.
- **Geodynamo and palaeomagnetism.** The induction equation explains magnetic
  reversals, secular variation and palaeomagnetic recording; the free-decay
  argument establishes that the field must be maintained
  ([08-01-06 Palaeomagnetism](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/06-palaeomagnetism.md)).
- **Magnetometer noise and instrument design.** Motion-induced EMF (Section 1) sets
  a floor on the usable sensitivity of any moving magnetic sensor.
- **Eddy-current non-destructive testing.** The same physics detects cracks in
  pipelines and rails.

## 10. Further reading

- **Griffiths, D. J. *Introduction to Electrodynamics* (4th ed., Cambridge
  University Press, 2017).** Chapter 7 covers Faraday's law, motional EMF and the
  energy interpretation of Lenz's law. Level: intermediate.
- **Jackson, J. D. *Classical Electrodynamics* (3rd ed., Wiley, 1999).** §5.15–5.18
  derive the moving-conductor form of Faraday's law carefully, including the
  Galilean subtleties the elementary treatment hides. Level: graduate.
- **Roberts, P. H., & King, E. M. "On the genesis of the Earth's magnetism",
  *Reports on Progress in Physics* 76 (2013) 096801.** A review of the dynamo
  problem, including the free-decay argument and the modern conductivity debate.
  Level: graduate.
- **Nabighian, M. N. (ed.) *Electromagnetic Methods in Applied Geophysics*, Vol. 1
  (SEG, 1988).** The induction and eddy-current chapters, with the time-domain and
  frequency-domain formulations used in practice. Level: advanced.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E. *Applied Geophysics* (2nd
  ed., Cambridge University Press, 1990).** The EM and geomagnetic sections give
  the survey-scale numbers. Level: intermediate.
- **Simpson, F., & Bahr, K. *Practical Magnetotellurics* (Cambridge University
  Press, 2005).** How the diffusive response is measured, with the noise sources of
  Section 1 in their engineering context. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 11. Related lessons

- [03 Maxwell's Equations and Their Physical Meaning](./03-maxwell-equations.md) —
  where the diffusion equation comes from, and the ratio that decides it.
- [06 EM Fields in Conductors: Skin Depth and Diffusion](./06-em-in-conductors.md)
  — the frequency-domain version of equation (8), with $\delta$ derived and
  verified.
- [07 Magnetisation, Susceptibility and Magnetic Materials](./07-magnetisation-materials.md)
  — the other half of rock magnetism: the field that is *carried*, not induced.
- [08-01-05 Dynamo Theory](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/05-dynamo-theory.md)
  — where the induction equation of Section 3 leads.
- [01-09-02 The Heat Equation](../../01-mathematics/09-partial-differential-equations/02-heat-equation.md)
  — the mathematics of equation (9), including similarity solutions and the
  absence of a wavefront.
- [09 Electrical and EM Methods](../../09-electrical-em-methods/README.md) — the
  survey practice built entirely on this lesson.

Exercises:
[`exercises/04-em-induction-exercises.md`](./exercises/04-em-induction-exercises.md)
and
[`exercises/04-em-induction-solutions.md`](./exercises/04-em-induction-solutions.md).

## Self-assessment checklist

Work through this without notes. Every item should be a clear "yes".

- [ ] I can state Faraday's law in both forms and name the three ways the flux can
      change. (Section 1)
- [ ] I can compute both a transformer and a motional EMF, and explain what
      physically distinguishes them. (Section 1)
- [ ] I can explain eddy currents, and why the measured quantity in EM surveying is
      a ratio. (Section 2)
- [ ] I can explain why a conductor screens a changing field but not a static one,
      with Lenz's law and energy conservation. (Section 2)
- [ ] I can derive equation (4) from Faraday, Ampère and Ohm's law, and define
      $R_m$. (Section 3)
- [ ] I can write the cosine and step solutions of magnetic diffusion and explain
      why there is no wavefront. (Section 4)
- [ ] I can compute the diffusion time at laboratory, crustal and core scales and
      use it to argue for dynamo action. (Section 4)
- [ ] I can verify the erfc similarity solution and the $\sqrt{Dt}$ law
      numerically, and distinguish the PDE residual from the scheme error.
      (Section 7)
- [ ] I can state four observable consequences of the geodynamo and say which are
      direct measurements and which are inferences. (Section 4)
