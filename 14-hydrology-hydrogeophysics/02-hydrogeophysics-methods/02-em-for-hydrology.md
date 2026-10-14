---
id: 14-02-02
title: "EM and TDEM for Groundwater Exploration"
level: graduate
prereqs: ["14-02-01", "14-01-02", "09-05-01"]
tags: [hydrogeophysics, electromagnetics, tdem, skin-depth, diffusion, salinity, conductance]
---

# EM and TDEM for Groundwater Exploration

Electromagnetic methods replace the galvanic current of ERT with an induced one,
and that single change buys depth, speed and freedom from electrode contact. A
transmitter loop is laid on the ground, switched off, and the ground's own decay
is recorded: the later the signal you can still measure, the deeper you have
sounded. This lesson derives the diffusion relations that set that depth, solves
the diffusion equation to verify them, and turns the result into the design rule
that governs every TDEM survey.

The physics of the EM response — Maxwell's equations in the quasi-static limit,
the skin depth, the frequency-domain and time-domain formulations — is derived in
[09-05 EM Methods](../../09-electrical-em-methods/05-em-methods-applications/README.md)
and [08-05 Controlled-Source EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/README.md).
This lesson assumes those and concentrates on what the hydrogeologist needs: the
depth a survey can reach in a stated ground, the salinity contrast it can resolve,
and the conductance equivalence that limits what a model of a thin aquifer means.

**All models and data in this module are SYNTHETIC.** The conductivities, depths,
times and responses below are invented teaching values or the exact output of
equations derived here. No real survey, instrument or field dataset is used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the skin depth from the diffusion equation and **compute** it for a
   stated frequency and conductivity.
2. **Compute** the diffusion depth $\sqrt{2\rho t/\mu_0}$ and the time needed to
   sound a stated depth in a stated ground.
3. **Solve** the 1-D magnetic diffusion equation with a step-off source and
   **verify** the solution against the analytic error-function solution.
4. **Derive** the step-off surface response $g(t) = 1/\sqrt{\pi D t}$ and the
   apparent-conductivity relation $\sigma_a = \pi t g^{2}/\mu_0$, and **measure**
   the decay exponent.
5. **Propagate** measurement noise through the square in the apparent-conductivity
   formula and **explain** why the noise doubles.
6. **Quantify** conductance equivalence for a thin conductive aquifer and **state**
   the thickness-to-depth ratio at which it breaks down.
7. **Choose** between TDEM, FDEM and DC ERT for a stated target, with arithmetic.

## Prerequisites

- [14-02-01 ERT for Aquifer Characterisation and Salinity Mapping](01-ert-for-hydrology.md)
  — the galvanic alternative and the Archie inversion this lesson shares.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md)
  — the aquifer geometry a sounding is trying to see.
- [09-05-01 TEM Sounding](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md)
  — the instrumentation, the induction number and the median-depth-of-investigation
  conventions used in practice.

---

## 1. From a step in the field to a decaying signal

The method is three steps long:

1. A loop of wire (or a grounded dipole) carries a current, which sets up a
   magnetic field in the ground.
2. The current is switched **off** abruptly. By Faraday's law the changing field
   induces currents in the ground, and those currents diffuse downwards and
   outwards.
3. The decaying magnetic field of those currents is measured at a receiver. **Early
   times carry shallow information; late times carry deep information.**

The governing equation is the magnetic diffusion equation. Inside a conductor with
conductivity $\sigma$, for the magnetic field $\mathbf{B}$ in the quasi-static limit
($\sigma \gg \omega\varepsilon$),

$$\nabla^{2}\mathbf{B} = \mu_0\sigma\frac{\partial \mathbf{B}}{\partial t},$$

a diffusion equation with diffusivity

$$D = \frac{1}{\mu_0\sigma}\ [\mathrm{m^2\,s^{-1}}],$$

with $\mu_0 = 4\pi \times 10^{-7}\ \mathrm{H\,m^{-1}}$ (exact in SI).

## 2. Skin depth and diffusion depth

For a **harmonic** source of angular frequency $\omega$, the solution of the
diffusion equation is exponential in depth with a decay length — the **skin
depth**:

$$\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}
= \frac{503}{\sqrt{f\sigma}}\ \mathrm{m}
\qquad (f \text{ in Hz},\ \sigma \text{ in S\,m}^{-1}).$$

| $f$ (Hz) | $\sigma = 0.01$ | $0.1$ | $1.0$ S m$^{-1}$ |
|---|---|---|---|
| 10 | 1591.6 | 503.3 | 159.2 |
| 100 | 503.3 | 159.2 | 50.3 |
| 1000 | 159.2 | 50.3 | 15.9 |
| 10 000 | 50.3 | 15.9 | 5.0 |

For a **step-off** (time-domain) source the equivalent length scale follows from
the same equation by similarity: $\delta$, $D$ and $t$ combine into the only
length available,

$$z = \sqrt{\frac{2\rho t}{\mu_0}}
\qquad\Longleftrightarrow\qquad
t = \frac{\mu_0 z^{2}}{2\rho},$$

with $\rho = 1/\sigma$ the resistivity. The physical content is the square root: to
sound twice as deep you need **four times** as long a decay, and in a ground ten
times more conductive you need ten times as long.

| $\rho$ ($\Omega$ m) | 0.1 ms | 1 ms | 10 ms | 100 ms |
|---|---|---|---|---|
| 1 | 12.6 | 39.9 | 126.2 | 398.9 |
| 10 | 39.9 | 126.2 | 398.9 | 1261.6 |
| 100 | 126.2 | 398.9 | 1261.6 | 3989.4 |

(depths in metres)

| depth (m) | $\rho = 1$ | $\rho = 10$ | $\rho = 100\ \Omega$ m |
|---|---|---|---|
| 10 | 0.063 | 0.006 | 0.001 ms |
| 50 | 1.571 | 0.157 | 0.016 ms |
| 100 | 6.283 | 0.628 | 0.063 ms |
| 200 | 25.13 | 2.513 | 0.251 ms |

**The hydrogeological consequence is a paradox worth stating plainly.** Sounding
100 m in a resistive (100 $\Omega$ m) aquifer needs only 0.063 ms — easy. Sounding
the same 100 m in a saline (1 $\Omega$ m) aquifer needs 6.3 ms, which is often
beyond the noise floor of a practical system, because the same conductivity that
makes the target a strong anomaly also screens the signal that would reach it.
**Saline ground is the easiest target in principle and the hardest to sound
deeply**, and larger transmitter moments (or a different geometry) are the only
answers.

## 3. A finite-difference solution, verified

The demonstration solves the 1-D form of the diffusion equation for a step-off
source,

$$\frac{\partial B}{\partial t} = \frac{\partial}{\partial z}
\left[D(z)\frac{\partial B}{\partial z}\right],
\qquad B(z,0) = B_0,\quad B(0,t) = 0,\quad B(\infty,t) = B_0,$$

with an explicit finite-volume scheme. For uniform $\sigma$ the exact solution is

$$B(z,t) = B_0\,\mathrm{erf}\!\left(\frac{z}{2\sqrt{Dt}}\right),$$

which satisfies all three conditions and the PDE identically. On a 400 m grid with
$\Delta z = 1$ m, $\Delta t = 2.5 \times 10^{-8}$ s (0.4 of the explicit stability
limit $\Delta t \le 0.5\Delta z^{2}/D$) and $\sigma = 0.1\ \mathrm{S\,m^{-1}}$
($D = 7.96 \times 10^{6}\ \mathrm{m^2\,s^{-1}}$), the maximum difference over the
interior after 1 ms is

$$\max\lvert B_{\text{num}} - B_{\text{analytic}}\rvert = 1.40 \times 10^{-3},$$

with the diffusion length $\sqrt{4Dt} = 178$ m comfortably inside the domain. That is
a verification of the stencil, the boundary treatment and the time step — not of
the physics, which is what the analytic solution *is*.

## 4. The surface response, derived and measured

The receiver measures the rate of change of the magnetic field, which in the 1-D
geometry is proportional to the surface gradient
$\partial B/\partial z$ at $z = 0$. Differentiating the error-function solution:

$$\frac{\partial B}{\partial z}\bigg|_{z=0}
= \frac{B_0}{\sqrt{\pi D t}}
\qquad\Longrightarrow\qquad
g(t) \equiv \frac{1}{B_0}\frac{\partial B}{\partial z}\bigg|_{0}
= \frac{1}{\sqrt{\pi D t}} \propto t^{-1/2}.$$

The demonstration measures the exponent on the last 80% of the window:
**$g \propto t^{-0.5000}$** — the derived $\tfrac{1}{2}$ recovered to four figures.
(The measured values of $g$ agree with the analytic formula to 0.09% for
$t > 0.02$ ms; the larger relative errors at the earliest samples, up to 7.7%, are
*discretisation*: when the diffusion length is only a few grid cells, the
error-function profile is not resolved near the surface. That is a resolution
limit of the grid, and it is the numerical version of the real instrument's
early-time limitation.)

**A note on geometry.** A 3-D small-loop system over a half-space decays as
$t^{-5/2}$ at late time, not $t^{-1/2}$. The difference is geometry (a
plane-wave-like 1-D source versus a localised loop), not physics. This lesson
derives and measures the 1-D result because it can be verified exactly here;
the 3-D formula should be taken from the EM literature and verified against a
3-D code.

### 4.1 Apparent conductivity, and why noise doubles

From $g = 1/\sqrt{\pi D t}$ and $D = 1/(\mu_0\sigma)$,

$$g^{2} = \frac{\mu_0\sigma}{\pi t}
\qquad\Longrightarrow\qquad
\boxed{\ \sigma_a = \frac{\pi t\,g^{2}}{\mu_0}\ }$$

Inverting the measured $g$ with this relation for the synthetic half-space
($\sigma = 0.1\ \mathrm{S\,m^{-1}}$) recovers:

| $t$ (ms) | $g$ | $\sigma_a$ (S m$^{-1}$) | $\rho_a$ ($\Omega$ m) | diffusion depth (m) |
|---|---|---|---|---|
| 0.020 | 0.0447 | 0.09983 | 10.02 | 17.9 |
| 0.050 | 0.0283 | 0.09993 | 10.01 | 28.2 |
| 0.100 | 0.0200 | 0.09997 | 10.00 | 39.9 |
| 0.200 | 0.0141 | 0.09998 | 10.00 | 56.4 |
| 0.500 | 0.0089 | 0.09999 | 10.00 | 89.2 |

**The apparent conductivity is exact at every time**, as it must be for a
half-space, and the small early-time deficit is the same grid-resolution effect.

Now propagate noise. Since $\sigma_a \propto g^{2}$, a fractional amplitude error
$\epsilon$ produces

$$\frac{\delta\sigma_a}{\sigma_a} = 2\epsilon + O(\epsilon^{2}),$$

so **the noise on an apparent conductivity is twice the noise on the amplitude**. A
Monte Carlo over 2000 realisations with 3% amplitude noise gives a mean error of
$+0.11\%$ (second order, as predicted) and a standard deviation of **5.96%**
against the predicted 6.0%. That factor of two is a design constraint: to resolve a
10% conductivity change you need amplitude data good to 5%, which sets the stacking
and the averaging.

## 5. Conductance equivalence, measured

For a conductive layer whose thickness $b$ is small compared with the diffusion
length, the response depends on the layer's **conductance**

$$S = b\,\sigma = \frac{b}{\rho}\ [\mathrm{S}],$$

and not on $b$ and $\sigma$ separately: a thin, very saline layer and a thick,
brackish one look identical. This is the same $S$-equivalence that appears in DC
resistivity ([14-02-01](01-ert-for-hydrology.md)) and it is the single most
important limitation on interpreting a hydrogeophysical model of a clay or saline
layer.

The demonstration embeds a layer of fixed conductance $S = 2.0$ S at 20 m depth in
a $50\ \Omega$ m host ($\sigma = 0.02\ \mathrm{S\,m^{-1}}$) and sounds to
$t = 0.0628$ ms, where the host diffusion depth is 70.7 m:

| $b$ (m) | $\sigma_{\text{layer}}$ (S m$^{-1}$) | surface $g$ | deviation from the thinnest |
|---|---|---|---|
| 2 | 1.0000 | 0.00575 | 0.00% |
| 4 | 0.5000 | 0.00581 | 1.19% |
| 8 | 0.2500 | 0.00596 | 3.78% |
| 16 | 0.1250 | 0.00631 | 9.85% |
| 32 | 0.0625 | 0.00724 | 25.91% |

All five models have **exactly the same conductance**, yet the response changes by
26% across the range. The equivalence is good while $b$ is a small fraction of the
diffusion depth ($b \lesssim 0.1\,z_{\text{diff}}$: 1.2% at $b = 4$ m against
$z = 70.7$ m) and fails as $b$ approaches it. **What a survey determines is the
conductance; what a report should say is $S = b/\rho$, with $b$ and $\rho$ flagged
as not separately resolved** unless borehole control fixes one of them.

## 6. Choosing between TDEM, FDEM and DC ERT

| Method | Typical depth | Behaviour in conductive ground | Resolution at depth |
|---|---|---|---|
| DC ERT | 50–200 m | poor: the current follows the conductor and the array must span the target | good at shallow depth, poor deep |
| FDEM (frequency domain) | 10–100 m | strong screening at high frequency | poor |
| TDEM (time domain) | 50–500 m | the conductor is a strong target, but the same conductivity limits the depth reached in a given time | moderate |
| Groundwater NMR ([05 Surface NMR](05-nmr-for-groundwater.md)) | 0–150 m | independent of conductivity (it is a magnetic resonance) | moderate, and directly sensitive to water |

The arithmetic that decides it, from Section 2: sounding 100 m in 10 $\Omega$ m
ground needs 0.63 ms of usable decay; at 200 m it needs 2.51 ms; and in
$1\ \Omega$ m ground, 200 m needs **25.1 ms**. Since $z \propto \sqrt{\rho t}$,
**each factor of ten in target resistivity buys a factor of $\sqrt{10} \approx 3.2$
in depth for the same time window** — which is why TDEM dominates deep, resistive
aquifer exploration (and geothermal prospecting), and why it is not the tool for a
saline aquifer at 300 m. For a shallow conductive target, ERT is cheaper and
better resolved; for a deep saline one, no surface EM method is comfortable, and
the answer is boreholes.

## 7. Python demonstration

`code/em_for_hydrology_demo.py` prints all of the above with units. It:

1. tabulates the skin depth over four frequencies and three conductivities;
2. tabulates the diffusion depth and the time-to-depth relation;
3. solves the 1-D diffusion equation by finite volume, verifies it against the
   analytic error-function solution (maximum interior difference
   $1.40 \times 10^{-3}$) and reports the stability limit it used;
4. measures the step-off decay exponent ($-0.5000$ against the derived $-0.5$),
   compares $g$ with the analytic formula (0.09% for $t > 0.02$ ms) and inverts
   for apparent conductivity;
5. runs a 2000-realisation noise Monte Carlo, recovering the factor-of-two
   amplification (standard deviation 5.96% against the predicted 6.0%);
6. measures conductance equivalence for five layer thicknesses at constant $S$,
   showing the deviation growing from 0% to 25.9%;
7. computes the time needed to sound a stated depth in a stated resistivity for
   the method comparison of Section 6.

```bash
cd 14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python em_for_hydrology_demo.py
```

Runtime is about 1.3 s.

## 8. Assumptions and regime of validity

1. **Quasi-static, low-frequency.** Displacement currents are neglected; valid for
   groundwater depths and conductivities ($\sigma \gg \omega\varepsilon$), and
   violated at radar frequencies, which is why GPR
   ([04](04-gpr-for-soil-moisture.md)) is a different physics regime.
2. **The 1-D model is a plane-wave idealisation.** Real systems have finite loops
   and 3-D geometry; the $\sqrt{\rho t}$ scaling survives, the exponents and
   amplitudes do not.
3. **Conductivity is a real scalar.** Induced polarisation (complex conductivity)
   is neglected; it matters in clay-rich and sulphidic ground.
4. **Negligible magnetisation and permittivity contrast.** Valid for soils and
   sediments; not for magnetic rocks or lateritic profiles.
5. **A usable signal window.** The relation $z = \sqrt{2\rho t/\mu_0}$ gives the
   depth at which the *diffusion front* has arrived, not the depth at which your
   system can still measure it. Noise, transmitter moment and the receiver's
   bandwidth set the actual depth, and the honest number is an inversion-derived
   depth of investigation with a stated uncertainty.
6. **No cultural noise.** Metal fences, pipes and power lines are the dominant
   practical limitation in populated areas.
7. **Conductance equivalence.** As measured in Section 5, $b$ and $\rho$ are not
   separately determined for a thin layer; a model report must say so.

## Mastery checkpoint

A synthetic survey must resolve a $15\ \Omega$ m saturated sand at 80 m depth under
$100\ \Omega$ m of dry cover.

**(a)** Compute the time needed for the diffusion to reach 80 m in a $15\
\Omega$ m target and in the $100\ \Omega$ m cover, and state which governs the
survey design. **(b)** Compute the skin depth at 100 Hz in the cover and in the
target, and explain in one sentence why a single frequency cannot sound both.
**(c)** The target is a 5 m thick aquifer. Compute its conductance and compare it
with the conductance of the 80 m of cover; what does the comparison tell you about
detectability? **(d)** If the aquifer's salinity doubles, by what factor does its
conductance change, and by what factor does the required sounding time change?
**(e)** A colleague proposes DC ERT instead. Give the two numbers that decide the
argument.

## Common pitfalls

1. **Reading depth directly from time or frequency.** Both give a diffusion length,
   which is a scale, not a boundary.
2. **Forgetting the square root.** Doubling the required depth quadruples the
   required time; it does not double it.
3. **Assuming a conductive target is easy.** It is a strong anomaly and a hard
   depth problem at the same time.
4. **Reporting a thin layer's thickness and resistivity separately.** The data
   constrain their ratio (the conductance).
5. **Ignoring the noise amplification from squaring.** Apparent conductivity has
   twice the relative error of the amplitude.
6. **Applying the 1-D exponent to a 3-D system.** Late-time exponents depend on
   geometry ($t^{-1/2}$ in 1-D, $t^{-5/2}$ for a small loop over a half-space).
7. **Treating a depth of investigation as a resolution.** You may detect a layer
   long before you can resolve its properties.

## Related modules

- [09-05 EM Methods and Applications](../../09-electrical-em-methods/05-em-methods-applications/README.md) —
  TEM sounding in practice, with the induction number and median-depth conventions.
- [08-05-02 Time-Domain EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/02-time-domain-em.md) —
  the decay-curve phenomenology and the eigenmode description of a conductor.
- [09-01-01 Resistivity and Conductivity](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  what sets $\sigma$ in a rock.
- [14-01-05 Groundwater Chemistry and Salinity](../01-hydrology-fundamentals/05-groundwater-chemistry.md) —
  the salinity-to-conductivity link.
- [03 Saline Intrusion and Coastal Aquifer Monitoring](../04-contaminant-and-environmental/03-saline-intrusion.md) —
  the classic application, in 2-D and time-lapse.

## Code and exercises

- Demonstration: [`code/em_for_hydrology_demo.py`](code/em_for_hydrology_demo.py)
- Exercises: [`exercises/02-em-for-hydrology-exercises.md`](exercises/02-em-for-hydrology-exercises.md)
- Worked solutions: [`exercises/02-em-for-hydrology-solutions.md`](exercises/02-em-for-hydrology-solutions.md)
