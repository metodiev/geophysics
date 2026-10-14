---
id: 11-01-02
title: "Targeting Strategy and Method Selection"
level: advanced
prereqs: ["05-01-01", "05-01-03", "08-03-01", "11-01-01"]
tags: [exploration-geophysics, method-selection, detectability, depth-scaling, survey-design]
---

# Targeting Strategy and Method Selection

A targeting strategy is a claim about **what the target is** — its size, depth
and property contrasts — followed by a calculation of which measurement can see
that claim at a tolerable cost. This lesson builds that calculation. It derives
the anomaly of one buried body for gravity, magnetics and EM, converts each into
a detection probability against a stated noise level, and then shows that the
ranking of methods changes with **depth** and with **target type**. There is no
method that is best in general.

**All models and data in this module are SYNTHETIC.** The target geometry,
property contrasts, resistivities, noise levels, costs and target value below are
chosen teaching values. They are not measured properties of any real deposit, and
not quotations from any tender or report.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the maximum gravity anomaly of a buried sphere from the point-mass
   potential, and the axial magnetic anomaly of an induced dipole, and **state**
   the property contrast each measurement really depends on.
2. **Measure** the depth scaling of each method (power laws in $z$) and
   **explain** why the two signal-to-noise ratios must cross at some depth.
3. **Derive** the skin depth from the diffusive Helmholtz equation and **use** it
   to explain why frequency is a depth selector rather than a quality setting.
4. **Compute** the gamma attenuation of a soil cover from the mass attenuation
   coefficient, and **state** the consequence for radiometric mapping.
5. **Convert** an anomaly and a noise level into a Gaussian detection probability
   $P_d$, and **compute** the depth at which $P_d$ falls to $0.5$ for each method.
6. **Rank** candidate methods for a stated target model and depth, and **identify**
   the two ways the ranking can reverse.
7. **State** what a target model is and why the choice of method is a test of a
   hypothesis rather than a measurement of the ground.

## Prerequisites

- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md)
  — the contrast logic used throughout.
- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](../../05-core-geophysics/01-what-geophysics-measures/03-resolution-depth-tradeoff.md)
  — the general form of the trade-off specialised here.
- [08-03-01 Magnetic Anomaly Basics](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/01-magnetic-anomaly-basics.md)
  — induced magnetisation and the dipole field.
- [11-01-01 Exploration Lifecycle](01-exploration-lifecycle.md) — the stage
  structure inside which this selection happens.

## 1. What a target model is

A **target model** is an explicit statement of the body you claim to be looking
for, in the terms each method can use:

| Element | Example value (SYNTHETIC) | Used by |
|---|---|---|
| Shape and volume | sphere of radius $150\ \mathrm{m}$, $1.414\times10^{7}\ \mathrm{m^3}$ | all |
| Depth to centre | $300\ \mathrm{m}$ | all |
| Density contrast | $400\ \mathrm{kg\,m^{-3}}$ | gravity |
| Susceptibility contrast | $0.001$ SI | magnetics |
| Resistivity | $1\ \Omega\,\mathrm{m}$ in a $100\ \Omega\,\mathrm{m}$ host | EM |
| Radioelement contrast | $K$, $U$, $Th$ concentrations | radiometrics |

Three of the three synthetic bodies of the demonstration share geometry and
differ only in contrasts:

| Target | $\Delta\rho$ (kg m⁻³) | $\kappa$ (SI) | $\rho_{\text{target}}$ (Ω m) |
|---|---|---|---|
| T1 sulphide | 400 | 0.001 | 1 |
| T2 chromite | 400 | 0.000 | 5000 |
| T3 magnetite | 50 | 0.100 | 5000 |

T2 is invisible to magnetics and to EM **at any depth**, because the fields those
methods measure are produced by contrasts it does not have. This is the first and
most important selection rule: *the target model, not the tool, decides what can
be detected.*

## 2. Deriving the anomaly of one body

### 2.1 Gravity: the sphere is a point mass

Outside a spherically symmetric body, the potential is that of a point mass at
its centre, $V = GM/r$ with $M = \tfrac{4}{3}\pi R^{3}\Delta\rho$. Directly above
the centre at depth $z$ the vertical (downward) acceleration is therefore

$$\boxed{\;\Delta g_{\max} = \frac{GM}{z^{2}}
= \frac{4}{3}\pi G \Delta\rho \frac{R^{3}}{z^{2}}\;}$$

in SI; divide by $10^{-5}$ for mGal. **The anomaly depends on the mass, not on the
shape**: at fixed $M$ it is the same for a sphere and for a cube of the same mass,
and the demonstration verifies that the formula tends to
$G\Delta\rho V/z^{2}$ exactly (sphere/point-mass ratio $1.000000$ at
$z = 300$, $3000$ and $30000\ \mathrm{m}$).

*Numerical check.* $\Delta\rho = 400\ \mathrm{kg\,m^{-3}}$,
$R = 150\ \mathrm{m}$, $z = 300\ \mathrm{m}$:

$$M = \frac{4}{3}\pi (150)^{3}(400) = 4.18879 \times 3.375\times10^{6} \times 400
= 5.6549\times10^{9}\ \mathrm{kg},$$

$$\Delta g = \frac{6.67430\times10^{-11} \times 5.6549\times10^{9}}{300^{2}}
= \frac{0.37743}{9\times10^{4}} = 4.1936\times10^{-6}\ \mathrm{m\,s^{-2}}
= 0.4194\ \mathrm{mGal},$$

which is the demo's value. A voxel integration of the same body on a $61^{3}$ grid
gives $0.419223$ mGal, a difference of $0.032\%$ from the closed form — the voxel
approximation of the sphere surface, not a physical discrepancy.

### 2.2 Magnetics: an induced dipole

A body of volume $V$ and susceptibility $\kappa$ in an ambient field
$\mathbf{B}_0$ acquires the induced magnetisation

$$\mathbf{M} = \kappa \mathbf{H} = \kappa \frac{\mathbf{B}_0}{\mu_0}
\qquad (\mathrm{A\,m^{-1}}),$$

so its dipole moment is $m = M V$ (A m²). On the axis of a dipole, the field
component along the axis is $(\mu_0/4\pi)\,2m/z^{3}$, so

$$\boxed{\;\Delta B_{\max} = \frac{\mu_0}{4\pi}\frac{2\kappa V B_0}{\mu_0 z^{3}}
= \frac{V \kappa B_0}{2\pi z^{3}}\;}$$

with $\mu_0/4\pi = 10^{-7}$ H m⁻¹. **Two powers of $z$ in the denominator plus one
in the numerator's volume**: the body's *size* does not cancel as it did for
gravity, because magnetism depends on the local magnetisation, not on the mass.

*Numerical check.* $V = 1.414\times10^{7}\ \mathrm{m^3}$, $\kappa = 0.001$,
$B_0 = 50\ \mathrm{\mu T}$:

$$m = 0.001 \times \frac{50\times10^{-6}}{4\pi\times10^{-7}}
\times 1.414\times10^{7} = 0.001 \times 39.789 \times 1.414\times10^{7}
= 5.626\times10^{5}\ \mathrm{A\,m^{2}},$$

$$\Delta B = 10^{-7}\times\frac{2(5.626\times10^{5})}{300^{3}}
= 10^{-7}\times\frac{1.1252\times10^{6}}{2.7\times10^{7}}
= 4.167\times10^{-9}\ \mathrm{T} = 4.167\ \mathrm{nT},$$

again matching the demonstration. Note how much the answer depends on
$\kappa$: a body with $\kappa = 0.1$ SI — magnetite-rich, entirely plausible —
gives $416.7\ \mathrm{nT}$ at the same depth, a hundred times larger. **A single
number in the target model changes the whole strategy.**

### 2.3 The depth scaling, measured

| $z$ (m) | $\Delta g$ (mGal) | SNR$_{\text{grav}}$ | $\Delta B$ (nT) | SNR$_{\text{mag}}$ |
|---|---|---|---|---|
| 100 | 3.7742 | 188.7 | 112.500 | 562.5 |
| 200 | 0.9436 | 47.2 | 14.063 | 70.3 |
| 300 | 0.4194 | 21.0 | 4.167 | 20.8 |
| 450 | 0.1864 | 9.3 | 1.235 | 6.2 |
| 600 | 0.1048 | 5.2 | 0.521 | 2.6 |
| 900 | 0.0466 | 2.3 | 0.154 | 0.8 |
| 1500 | 0.0168 | 0.8 | 0.033 | 0.2 |

Fitting power laws to the demo output over $100$–$1500\ \mathrm{m}$ gives
$\Delta g \propto z^{-2.000}$ and $\Delta B \propto z^{-3.000}$: the exponents are
recovered to three decimals, which is the check that the closed forms are
consistent with the numbers.

Because the exponents differ, the two signal-to-noise ratios must be equal at
exactly one depth. **The demonstration solves for it: $z = 298\ \mathrm{m}$ for
T1.** This is the whole idea of depth-dependent method selection, and it is a
derived quantity, not a rule of thumb. For a *fixed* target model there is a
depth below which gravity beats magnetics — and a different such depth for every
target model.

## 3. EM: skin depth, induction number and frequency

### 3.1 Skin depth from the diffusion equation

In a good conductor with negligible displacement current, the electric field
satisfies $\nabla^{2}\mathbf{E} = i\omega\mu_0\sigma\mathbf{E}$, a diffusion
equation whose plane-wave solution is $e^{-ikz}$ with

$$k^{2} = i\omega\mu_0\sigma, \qquad k = (1+i)\sqrt{\frac{\omega\mu_0\sigma}{2}}
= \frac{1+i}{\delta}, \qquad
\boxed{\;\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}\;}.$$

The amplitude decays as $e^{-z/\delta}$, so $\delta$ is the depth over which the
field falls by $1/e$. The demonstration checks the algebra by evaluating
$1/\mathrm{Im}\,k$ numerically: $503.2921\ \mathrm{m}$ both ways at $100\
\mathrm{Hz}$ in $100\ \Omega\,\mathrm{m}$, a difference of $0.00\times10^{0}$.

| $f$ (Hz) | $\delta_{\text{host}}$ (m) at 100 Ω m | $\delta_{\text{target}}$ (m) at 1 Ω m |
|---|---|---|
| 10 | 1591.5 | 159.2 |
| 100 | 503.3 | 50.3 |
| 1000 | 159.2 | 15.9 |
| 10000 | 50.3 | 5.0 |

### 3.2 The two competing effects, and the frequency optimum

A buried conductor's secondary field at the surface has three multiplicative
factors, which is the structure the demonstration uses:

$$\text{EM index} =
\underbrace{\left(\frac{a}{z}\right)^{3}}_{\text{geometric coupling}}
\times \underbrace{\vphantom{\frac{1}{2}}e^{-2z/\delta}}_{\text{host attenuation}}
\times \underbrace{\frac{\omega\tau}{\sqrt{1+(\omega\tau)^{2}}}}_{\text{induction}} ,$$

where $\tau = \mu_0\sigma a^{2}/\pi^{2} = 2.865\ \mathrm{ms}$ is the decay time
constant of a conducting sphere. The geometric factor is the dipole fall-off
derived in §2.2; the exponential is the two-way consequence of §3.1; the
induction factor is a one-parameter circuit response with the correct
resistive-limit growth ($\propto\omega$) and high-frequency saturation. **This is
an index, not a forward model**, and it is labelled as such: the quantitative
forward model for a sphere in a uniform field is developed in
[11-02-04 EM for Conductors](../02-mineral-exploration/04-em-for-minerals.md)
and [08-05 Controlled-Source EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/README.md).

Measured behaviour for the synthetic T1:

| $f$ (Hz) | $\delta_{\text{host}}$ (m) | induction factor | EM index | SNR |
|---|---|---|---|---|
| 10 | 1591.5 | 0.1772 | 0.01519 | 0.76 |
| 30 | 918.9 | 0.4751 | 0.03091 | 1.55 |
| 100 | 503.3 | 0.8742 | 0.03317 | 1.66 |
| 300 | 290.6 | 0.9833 | 0.01559 | 0.78 |
| 1000 | 159.2 | 0.9985 | 0.00288 | 0.14 |
| 10000 | 50.3 | 1.0000 | 0.00000 | 0.00 |

The index **peaks near 60 Hz**: below the peak the induced current is too weak,
above it the primary field is attenuated before it arrives. Frequency is
therefore a *depth-and-target selector*, and the optimum depends on the target's
own $\tau$ — which is exactly the quantity an EM survey is trying to measure. That
circularity is the honest difficulty of EM targeting and it is why multi-frequency
or time-domain (broadband) systems are used rather than a single frequency.

## 4. Radiometrics: a surface method, by physics

Gamma rays are attenuated as $I = I_0 e^{-\mu\rho d}$ with $\mu/\rho$ the mass
attenuation coefficient. For $\sim\!1\ \mathrm{MeV}$ photons in rock-forming
oxides, $\mu/\rho \approx 0.06\ \mathrm{cm^{2}\,g^{-1}}$ (a standard tabulated
value). Then

$$\text{HVL} = \frac{\ln 2}{\mu} = \frac{0.6931}{0.06\times1.6}
= 7.22\ \mathrm{cm\ of\ soil}\ (\rho = 1.6\ \mathrm{g\,cm^{-3}}),$$

$$= 4.28\ \mathrm{cm\ of\ rock}\ (\rho = 2.70\ \mathrm{g\,cm^{-3}}).$$

Ten half-value layers is $72.2\ \mathrm{cm}$ of soil; the transmitted fractions
are $0.383$ at $10\ \mathrm{cm}$, $0.0561$ at $30\ \mathrm{cm}$, $0.0082$ at
$50\ \mathrm{cm}$ and $6.8\times10^{-5}$ at $100\ \mathrm{cm}$. **Radiometrics is
a geochemical mapper of the top half-metre, and that is a consequence of one
constant, not a limitation of instrument design.** A target that has no surface
expression cannot be found by radiometrics however good the spectrometer is —
which is why it is used for alteration *mapping* over outcrop and residual soil,
and why its targets are patterns, not bodies.

## 5. From anomaly to detection probability

Detection of a known waveform of amplitude $A$ in additive Gaussian noise of
standard deviation $\sigma$ has the likelihood-ratio test "declare a detection if
the matched-filter output exceeds $\eta$". For the one-sided case the false-alarm
probability is $P_{fa} = Q(\eta/\sigma)$ and the detection probability is

$$\boxed{\;P_d = Q\!\left(Q^{-1}(P_{fa}) - d'\right), \qquad d' = A/\sigma\;}$$

with $Q(x) = 1-\Phi(x)$. Only the ratio $d'$ matters: the *absolute* anomaly is
irrelevant, which is why a noise budget is as much a part of survey design as the
target model.

With $P_{fa} = 0.05$ ($Q^{-1} = 1.6449$) the demo's T1 gives:

| $z$ (m) | $P_d$ gravity | $P_d$ magnetics | $P_d$ EM (100 Hz) |
|---|---|---|---|
| 100 | 1.0000 | 1.0000 | 1.0000 |
| 200 | 1.0000 | 1.0000 | 1.0000 |
| 300 | 1.0000 | 1.0000 | 0.5055 |
| 400 | 1.0000 | 1.0000 | 0.1201 |
| 600 | 0.9998 | 0.8313 | 0.0568 |
| 800 | 0.9038 | 0.2925 | 0.0512 |
| 1200 | 0.3691 | 0.0935 | 0.0501 |

Solving $P_d = 0.5$ numerically:

| Method | Depth at $P_d=0.5$ | In target radii |
|---|---|---|
| gravity | 1071 m | 7.1 |
| magnetics | 699 m | 4.7 |
| EM at 100 Hz | 301 m | 2.0 |

The depths differ by a factor of $3.6$, so "how deep does this method see?"
is a question with no method-only answer: it depends on the contrasts, and on
which $P_d$ you are willing to accept. Note also the floor: for EM, $P_d \to 0.05$
at large $z$, which is *the false-alarm rate* — a detector with no signal
declares detections at exactly $P_{fa}$.

## 6. Worked example — the ranking, at a stated depth and target

Take T1 at $z = 300\ \mathrm{m}$, a target area of $100\ \mathrm{km^{2}}$ per
target tested, and the SYNTHETIC costs and value of the demonstration.

| Method | USD/km² | cost (MUSD) | $P_d$ | $E[\text{net}] = P_d V - \text{cost}$ |
|---|---|---|---|---|
| gravity | 250 | 0.025 | 1.000 | 500.0 MUSD |
| magnetics | 60 | 0.006 | 1.000 | 500.0 MUSD |
| EM | 350 | 0.035 | 0.505 | 252.7 MUSD |

with $V = 500$ MUSD. The value metric saturates because both $P_d \approx 1$: at
$300\ \mathrm{m}$ the *cheapest* method with a saturated $P_d$ wins, and that is
magnetics. Push the target to $900\ \mathrm{m}$ and the same table becomes
gravity $376.6$, magnetics $95.6$, EM $25.3$ MUSD — **gravity wins**, because
magnetics has fallen to $P_d = 0.191$ while gravity is still at $0.753$.

Hold depth at $300\ \mathrm{m}$ and vary the target instead:

| Target | $P_d$ grav | $P_d$ mag | $P_d$ EM | Winner |
|---|---|---|---|---|
| T1 sulphide | 1.000 | 1.000 | 0.505 | magnetics |
| T2 chromite | 1.000 | 0.050 | 0.050 | gravity |
| T3 magnetite | 0.836 | 1.000 | 0.050 | magnetics |

Two reversals, two mechanisms:

1. **Depth reversal** (T1, 300 → 900 m): the $\Delta B \propto z^{-3}$ fall-off
   against $\Delta g \propto z^{-2}$, quantified as a crossover depth.
2. **Target-type reversal** (T1 → T2 at fixed depth): a contrast that is *absent*
   cannot be measured at any depth or budget.

This second reversal is why the target model is the hypothesis and the method
choice is the test. `E[net] = P_d V - cost` is deliberately crude: it credits a
detection with the full value $V$, gives a *negative* result nothing, and ignores
the prior probability that the target exists at all. The correct treatment —
value of information, the worth of a null result, and the optimal stopping rule —
is the subject of [11-01-03](03-cost-benefit.md).

## 7. Assumptions and regime of validity

1. **The target model is correct.** Every number above is conditional on the
   stated geometry and contrasts. If the real body is $1.5\times$ larger and
   twice as deep, all three rankings change. This is the central honest
   limitation: selection is a test of a hypothesis, not a measurement.
2. **Noise is additive, white and Gaussian, and known.** Real noise is
   correlated (cultural, geological, diurnal), often non-Gaussian with outliers,
   and estimated from the data. $P_d$ from $d'$ is an optimistic benchmark
   unless the noise model has been measured.
3. **The detector is optimal and the anomaly amplitude is known.** In practice the
   amplitude is fitted, so $d'$ is an estimated parameter with its own
   uncertainty, and the effective $d'$ is smaller than the peak-amplitude value.
4. **The bodies are isolated spheres or dipoles in a uniform half-space.** Real
   targets are irregular, have remanent magnetisation (which can dominate
   induced, and which the demonstration omits entirely), and sit in hosts whose
   conductivity is not constant with depth.
5. **Gravity, magnetics: no self-demagnetisation.** A strongly magnetic body is
   demagnetised by its own field, so $\Delta B$ for large $\kappa$ grows *sub*
   linearly in $\kappa$; the linear relation used here over-predicts for
   $\kappa \gtrsim 0.1$.
6. **The EM index is not a forward model.** It has the right limits and the right
   multiplicative structure, and it is *not* calibrated to Maxwell's equations.
7. **All costs, noise levels and the target value are SYNTHETIC**, and no
   discounting, mobilisation or permitting cost is included.

## 8. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $\Delta g$ | m s⁻² (report mGal, $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$) | $G$ (m³ kg⁻¹ s⁻²) × $\Delta\rho$ (kg m⁻³) × $R^3$ (m³) / $z^2$ (m²) = m s⁻² ✔ |
| $\Delta B$ | T (report nT, $1\ \mathrm{nT} = 10^{-9}$ T) | $\mu_0/4\pi$ (H m⁻¹) × A m² / m³ = (N A⁻²) A m⁻¹ = T ✔ |
| $\delta$ | m | $\sqrt{2/(\mathrm{s^{-1}} \times \mathrm{H\,m^{-1}} \times \mathrm{S\,m^{-1}})} = \sqrt{\mathrm{m^2}}$ ✔ |
| EM index | – | $(a/z)^3$ dimensionless × dimensionless exponentials ✔ |
| $d'$ | – | anomaly over noise, same units ✔ |

The check that catches mistakes most often is the magnetic one: $m = \kappa H V$
has units A m², and dividing by $z^3$ gives A m⁻¹, which multiplied by
$\mu_0/4\pi$ gives tesla. Forgetting the $\mu_0$ between $H$ and $B$ produces a
factor of $4\pi\times10^{-7}$ — a thousandfold error in nT that looks like a
"very magnetic" body.

## 9. Python demonstration

`code/targeting_strategy_demo.py` prints, with units:

1. the three SYNTHETIC targets and their property contrasts
   ($\Delta\rho$, $\kappa$, $\rho_{\text{body}}$, and the radioelement
   contrasts of T1: $\Delta\rho = 400\ \mathrm{kg\,m^{-3}}$,
   $\kappa = 0.001$ SI, $1.0\ \mathrm{\Omega\,m}$);
2. the gravity and magnetic anomaly of the same sphere against depth, and the
   depth at which their signal-to-noise ratios cross (298 m for this body);
3. skin depth, induction number and the EM frequency index, whose maximum sits
   near 60 Hz;
4. the radiometric half-value layer of the synthetic soil
   ($7.22\ \mathrm{cm}$, ten HVLs $= 72.2\ \mathrm{cm}$) and the height loss
   of the K and Th windows;
5. the detection probability $P_d = Q\!\left(Q^{-1}(P_{fa}) - d'\right)$
   against depth for every method;
6. the ranking table, which changes with depth *and* with target type;
7. verification of the closed forms used in the sections above.

Run it with the project virtual environment:

```bash
cd 11-exploration-geophysics/01-exploration-workflow/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python targeting_strategy_demo.py
```

## 10. Exercises


Full sets with worked solutions:
[`exercises/02-targeting-and-strategy-exercises.md`](exercises/02-targeting-and-strategy-exercises.md)
and
[`exercises/02-targeting-and-strategy-solutions.md`](exercises/02-targeting-and-strategy-solutions.md).

## Mastery checkpoint

Without notes:

> A SYNTHETIC target is a sphere of radius $100\ \mathrm{m}$ and
> $\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$, $\kappa = 0.02$ SI, resistivity
> $2\ \Omega\,\mathrm{m}$ in a host of $200\ \Omega\,\mathrm{m}$, centred at
> $200\ \mathrm{m}$ depth; the field is $52\ \mathrm{\mu T}$. **(a)** Compute
> $\Delta g$ at the surface above the centre, in mGal. **(b)** Compute $\Delta B$
> in nT. **(c)** Compute the skin depth in the host at $200\ \mathrm{Hz}$ and
> decide whether the host or the target dominates the attenuation. **(d)** With
> noise of $0.03$ mGal and $0.3$ nT, compute $d'$ for both methods at
> $P_{fa} = 0.05$, and state which you would choose at $z = 600\ \mathrm{m}$.
> **(e)** State the two assumptions that would most change your answer.

A worked version of (a)–(d) is in the
[solutions](exercises/02-targeting-and-strategy-solutions.md).

## Common pitfalls

1. **Choosing a method out of habit.** "Magnetics first" is a strategy only if the
   target model has susceptibility; for T2 it is a way of finding nothing.
2. **Quoting a detection depth without a target model.** Depth of investigation is
   a property of a *target-and-method pair* at a stated $P_d$.
3. **Confusing detection with resolution.** A body can be detected after its size
   and depth have become unresolvable; the two thresholds are different numbers.
4. **Forgetting remanence.** A strongly remanent body produces a different,
   sometimes inverted, anomaly; the induced-dipole formula does not apply.
5. **Treating the anomaly peak as the signal.** $d'$ uses the matched-filter
   amplitude against measured noise, not the peak of an unfiltered profile.
6. **Ignoring the cost side.** Ranking by anomaly alone gives the same answer as
   ranking by value only when the methods cost the same per unit area.
7. **Adding surveys without adding information.** Two methods sensitive to the
   same property (for example FEM conductivity and TEM conductivity) are
   correlated, and their combination is not worth the sum of the costs — see
   [11-02-07](../02-mineral-exploration/07-multi-method-targeting.md).

## Related modules

- [11-01-01 Exploration Lifecycle: Reconnaissance to Reserve Definition](01-exploration-lifecycle.md)
  — the staged decision structure this lesson allocates budget inside.
- [11-01-03 Cost, Risk and Value of Information in Exploration](03-cost-benefit.md)
  — what a survey is worth before it is flown.
- [11-02-01 Geophysical Signatures of Major Deposit Types](../02-mineral-exploration/01-deposit-signatures.md)
  — target models for real deposit classes, with contrasts.
- [05-01-05 Choosing a Method: A Decision Framework](../../05-core-geophysics/01-what-geophysics-measures/05-choosing-a-method.md)
  — the general framework specialised here.
