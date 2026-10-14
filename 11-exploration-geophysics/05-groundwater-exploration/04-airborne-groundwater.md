---
id: 11-05-04
title: "Airborne EM for Regional Aquifer Mapping"
level: doctoral
prereqs: ["11-05-02", "08-05-05", "09-05-01"]
tags: [exploration-geophysics, groundwater, airborne-em, diffusion, conductance, depth-of-investigation, decision]
---

# Airborne EM for Regional Aquifer Mapping

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the diffusive diffusion depth $d(t) = \sqrt{2\rho t/\mu_0}$ from
   the induction equation and **compute** the depth a given gate reaches in a
   given resistivity.
2. **Derive** the sensitivity kernel of a 1-D diffusive sounder and **explain**
   why an apparent conductivity is a weighted average rather than a depth probe.
3. **Compute** a depth of investigation from a stated sensitivity level and
   **show** that it depends on the gate time and the conductivity.
4. **Quantify** the exchange between survey altitude, transmitter moment and
   penetration, and **state** which one a design must fix first.
5. **Demonstrate** the conductance equivalence of a layered section and **state**
   why AEM products are delivered as conductance maps.
6. **Convert** an anomaly into a decision with Bayes' rule, and **state** why the
   base rate of usable aquifers controls the interpretation more than the data
   quality does.

## Prerequisites

- [11-05-02 EM and ERT for Groundwater Mapping](../05-groundwater-exploration/02-em-and-ert-groundwater.md)
  — the diffusive physics and the conductance concept in the ground-based form.
- [08-05-05 Airborne EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/05-airborne-em.md)
  — the system engineering and the survey platform.
- [09-05-01 TEM Sounding](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md)
  — the ground time-domain method this lesson generalises.
- [18-06 Uncertainty Quantification](../../18-inverse-problems/06-uncertainty-quantification/06-decision-under-uncertainty.md)
  — value of information and decision under uncertainty.

> All models and data in this module are **SYNTHETIC**. The section, the system
> geometry and the noise level are chosen teaching values. The forward model used
> in the demonstration is an explicitly stated **1-D diffusion-kernel
> teaching model**, not a real system's response.

## 1. Intuition: the only method that surveys a region

Ground-based ERT and TEM answer a question at a point or along a line; an
airborne EM (AEM) survey answers it over thousands of square kilometres in a
week. That change of scale changes what the method is *for*. An AEM survey is not
a set of soundings; it is a **regional screening tool** whose product is a map of
apparent conductivity and conductance, used to decide where the expensive
ground-based work and drilling should go.

Two honest statements must accompany that product.

- **The map is a weighted average of the subsurface.** AEM is sensitive to
  conductivity contrasts, but its response integrates over a volume whose size
  grows with the depth probed and with the flight altitude. A thin aquifer and a
  thick aquitard can produce the same map value.
- **A conductive anomaly is not a resource.** In an arid region the conductive
  anomalies include clays, saline groundwater, mineralised bedrock and cultural
  features. The fraction that is a usable aquifer is a *prior* question, answered
  by regional geology and hydrogeology, and the survey only updates it.

This lesson derives the depth physics, measures the altitude and equivalence
limits, and then does the decision arithmetic that turns an anomaly into a
drilling recommendation with an explicit error rate.

## 2. Precise definitions

### 2.1 System geometry

A **transmitter loop** (or a grounded dipole) induces currents in the ground; a
**receiver** measures the secondary field. **Frequency-domain** systems (FDEM)
measure at fixed frequencies; **time-domain** systems (TDEM) switch the
transmitter off and measure the decaying secondary field in **gates** — windows
of time after switch-off. Both are towed on a **bird** at an altitude $h$,
typically tens of metres, with a **footprint** (the effective surface area from
which a single reading collects its signal) that grows with altitude and with the
gate time.

### 2.2 Apparent conductivity and conductance

An AEM system reports an **apparent conductivity** $\sigma_a$ (or, for a layered
inversion, a conductivity–depth model). For a **thin** conductive layer the
resolvable quantity is the **conductance**

$$ S = \int \sigma(z)\,\mathrm{d}z \qquad (\mathrm{S}), $$

and it is $S$, not $\sigma$ or the thickness, that a sounding constrains. AEM
products are therefore often delivered as conductance maps.

### 2.3 The diffusion depth

The induction equation in a conductor reduces to a diffusion equation, whose
characteristic depth at time $t$ after switch-off is

$$ \boxed{\;d(t) = \sqrt{\frac{2\rho t}{\mu_0}} = 1261.6\sqrt{\rho t}\ \mathrm{m}\;}, $$

with $\rho$ in $\Omega\,\mathrm{m}$, $t$ in s and
$\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$. Early gates see shallow ground;
late gates see deeper ground but with a weaker signal and a wider footprint.

### 2.4 Depth of investigation

The **depth of investigation (DOI)** is the depth below which a survey has little
or no sensitivity. It is not a fixed number: it depends on the latest usable gate,
on the conductivity, on the system's noise floor and on the *stated* sensitivity
level used to define it. This lesson computes it from the cumulative sensitivity
kernel, and quotes the definition with the number.

## 3. Derivations

### 3.1 The diffusion depth

For negligible displacement current, the magnetic field in a uniform conductor of
conductivity $\sigma$ obeys $\partial B/\partial t = D\,\partial^{2}B/\partial
z^{2}$ with $D = 1/(\mu_0\sigma)$. The response to a step change at the surface is
the complementary error function,

$$ B(z,t) = B_0\,\mathrm{erfc}\!\left(\frac{z}{2\sqrt{Dt}}\right), $$

whose transition from 1 to 0 occurs near $z \approx 2\sqrt{Dt}$. The convention
used throughout this lesson is the maximum-sensitivity depth

$$ d(t) = \sqrt{2Dt} = \sqrt{\frac{2t}{\mu_0\sigma}} = \sqrt{\frac{2\rho t}{\mu_0}}, $$

which is $\sqrt{2}$ times smaller than the erfc transition depth; the factor is a
**convention**, not a physical constant, and both appear in the literature.
Substituting the constants gives $d = 1261.6\sqrt{\rho t}$ m, and the
demonstration prints a table. At $\rho = 10\ \Omega\,\mathrm{m}$,
$t = 1\ \mathrm{ms}$: $d = 126.2\ \mathrm{m}$.

Note the square root: to double the depth, the gate time must be **quadrupled**
at fixed conductivity, or the conductivity quadrupled at fixed time.

### 3.2 The sensitivity kernel and why $\sigma_a$ is an average

In a 1-D diffusive sounder the sensitivity of the measured response to the
conductivity at depth is concentrated in a window that moves downward with time.
The diffusion equation's first-moment Green's function gives the kernel

$$ K(z,t) = \frac{z}{2Dt}\,e^{-z^{2}/(4Dt)},
\qquad \int_0^{\infty}K(z,t)\,\mathrm{d}z = 1, $$

whose peak is at $z = \sqrt{2Dt} = d(t)$ — the diffusion depth. The demonstration
verifies the normalisation numerically (integral $0.99990$ to $1.00000$ over
$0$-$4000\ \mathrm{m}$) and the peak position (printed $28.0\ \mathrm{m}$ against
a diffusion depth of $28.2\ \mathrm{m}$ at $t = 0.1\ \mathrm{ms}$ for
$\sigma = 0.2\ \mathrm{S\,m^{-1}}$). The window is *wide*: it has appreciable
weight between roughly $0.3d$ and $3d$, so

$$ \sigma_a(t) = \int_0^{\infty}\sigma(z)\,K(z,t)\,\mathrm{d}z $$

is a weighted average, not a reading at one depth. A thin target and a thick
background layer can contribute the same amount to $\sigma_a$ — which is
precisely the equivalence of Section 3.3.

The **cumulative** kernel
$\int_0^{z}K\,\mathrm{d}z' = 1 - e^{-z^{2}/(4Dt)}$ gives a DOI definition from a
stated level: for "30% of the weight lies below the DOI",

$$ 1 - e^{-z^{2}/(4Dt)} = 0.7
\;\Longrightarrow\;
z_{\mathrm{DOI}} = \sqrt{4Dt\ln(1/0.3)} \approx 1.55\,d(t). $$

The demonstration prints $43.8\ \mathrm{m}$ at $0.1\ \mathrm{ms}$,
$138.4\ \mathrm{m}$ at $1\ \mathrm{ms}$ and $437.7\ \mathrm{m}$ at
$10\ \mathrm{ms}$ for $\sigma_{\text{ref}} = 0.2\ \mathrm{S\,m^{-1}}$. Quote the
level with the number, because the DOI is *defined* by the level.

### 3.3 Conductance equivalence

A thin conductive layer of conductivity $\sigma$ and thickness $h$ is seen by a
diffusing field as a **conducting sheet**: current crosses it and spreads
laterally, so to first order the response depends on the sheet conductance
$S = \sigma h$ alone. Two layers with the same $S$ at the same depth are
therefore equivalent. The demonstration compares

- **A:** $20\ \mathrm{m}$ of $0.10\ \mathrm{S\,m^{-1}}$ ($S = 2.0\ \mathrm{S}$),
- **B:** $5\ \mathrm{m}$ of $0.40\ \mathrm{S\,m^{-1}}$ ($S = 2.0\ \mathrm{S}$).

Their apparent conductivities differ by at most $8.1\%$ (at
$t = 0.3\ \mathrm{ms}$) and by less than $1.6\%$ for $t \ge 3\
\mathrm{ms}$. Against a $2\%$ noise floor the two models are indistinguishable in
the late gates: **the thickness and the conductivity cannot be separated; only
their product is resolved.** An inversion that returns a thickness is returning a
choice made by its regularisation and its prior, not a measurement.

### 3.4 From anomaly to aquifer: the base rate

Let $p$ be the prior probability that a conductive anomaly is a usable aquifer,
$\mathrm{TPR}$ the probability that an aquifer produces the conductive signature,
and $\mathrm{FPR}$ the probability that a non-aquifer (clay, saline brine,
mineralised rock) does. Bayes' rule gives the **positive predictive value**

$$ \mathrm{PPV} = \frac{p\,\mathrm{TPR}}{p\,\mathrm{TPR} + (1-p)\,\mathrm{FPR}}. $$

With the demonstration's stated values $p = 0.08$, $\mathrm{TPR} = 0.80$,
$\mathrm{FPR} = 0.30$:

$$ \mathrm{PPV} = \frac{0.08(0.80)}{0.08(0.80) + 0.92(0.30)}
= \frac{0.064}{0.064 + 0.276} = 0.188. $$

Of every 100 anomalies, 19 are aquifers. The test is informative — the prior of
$8\%$ rises to $19\%$ — and four fifths of the drilling targets are still wrong.
The screening only becomes decisive when the prior is better (at $p = 0.5$ the
posterior is $0.727$), which is another way of saying that the survey cannot
substitute for regional understanding.

## 4. Worked examples

### Example 1 — the gate needed for a target at 60 m

At $\rho = 30\ \Omega\,\mathrm{m}$ the diffusion depth is
$d = 1261.6\sqrt{30t}$. Setting $d = 60\ \mathrm{m}$:

$$ t = \frac{d^{2}}{1261.6^{2}\rho} = \frac{3600}{1.5916\times10^{6}\times30}
= 7.54\times10^{-5}\ \mathrm{s} \approx 75\ \mu\mathrm{s}. $$

So a $75\ \mu\mathrm{s}$ gate is centred on 60 m in this ground. If the system's
first usable gate is $100\ \mu\mathrm{s}$, the target is already inside the first
gate's window and the shallow part of the section contaminates it.

### Example 2 — a thick section, read from the table

The synthetic three-layer section of the demonstration is $0.02\
\mathrm{S\,m^{-1}}$ to $10\ \mathrm{m}$, $0.40\ \mathrm{S\,m^{-1}}$ from 10 to
30 m, and $0.02\ \mathrm{S\,m^{-1}}$ below. The printed apparent conductivities:

| Gate (ms) | Kernel in the target | $\sigma_a$ ($\mathrm{S\,m^{-1}}$) |
|---|---|---|
| 0.05 | 0.558 | 0.2320 |
| 0.10 | 0.366 | 0.1591 |
| 0.30 | 0.148 | 0.0762 |
| 1.0 | 0.048 | 0.0381 |
| 10.0 | 0.005 | 0.0219 |

At the earliest gate the reading ($0.232\ \mathrm{S\,m^{-1}}$) is dominated by
the target but is still only $58\%$ of the target's true conductivity, because
the kernel also sees the resistive top and basement. As the window moves past the
target, $\sigma_a$ falls back to the background ($0.0206\
\mathrm{S\,m^{-1}}$ at 30 ms). **No single gate is the target's conductivity.**

### Example 3 — reading the ambiguity honestly

An AEM inversion delivers a $20\ \mathrm{m}$-thick layer of $0.10\
\mathrm{S\,m^{-1}}$ at 10-30 m depth. Because the equivalence of Section 3.3
allows the equally good model $5\ \mathrm{m}$ of $0.40\
\mathrm{S\,m^{-1}}$, the report must give the *conductance*, $S = 2.0\
\mathrm{S}$, with the admitted range of thicknesses. The hydrogeological reading
differs sharply between the two: a $20\ \mathrm{m}$ aquifer is a resource; a
$5\ \mathrm{m}$ clay aquitard is not. The data do not choose between them; a
borehole does.

### Example 4 — altitude, moment and penetration

The demonstration's synthetic coupling of a loop at altitude $h$ to a layer at
depth $z$ gives, normalised to a surface layer at $h = 30\ \mathrm{m}$:

| Depth $z$ (m) | $h=30$ m | $h=60$ m | $h=90$ m | $h=120$ m |
|---|---|---|---|---|
| 0 | 1.000 | 0.140 | 0.043 | 0.018 |
| 20 | 0.239 | 0.060 | 0.024 | 0.011 |
| 100 | 0.014 | 0.008 | 0.005 | 0.003 |

Against a $2\%$ noise floor with a $3\times$ detection threshold, the deepest
detectable layer is about $50\ \mathrm{m}$ at $30\ \mathrm{m}$ altitude,
$20\ \mathrm{m}$ at $60\ \mathrm{m}$, and nothing at all at $90\ \mathrm{m}$ or
above — because the coupling to a near-surface conductor has fallen to
$4\%$ and then $2\%$ of its reference value. Altitude is exchanged for
penetration, and paying it back requires a **larger transmitter moment**
(a bigger loop or current), not a cleverer inversion.

## 5. Assumptions and regime of validity

1. **1-D layered earth.** The kernel model assumes layers are laterally
   invariant. A narrow palaeochannel is *smeared* by the footprint, so its
   conductivity is underestimated and its width overestimated; a 3-D response
   must be computed numerically.
2. **The kernel is a teaching model.** It is the exact 1-D diffusion
   first-moment kernel, not the true Fréchet derivative of a specific system.
   Absolute values depend on the system; the *scaling* conclusions (depth
   $\propto\sqrt{\rho t}$, DOI $\propto\sqrt{t}$) do not.
3. **Quasi-static, resistive-limit approximation.** Displacement currents and
   dielectric effects are neglected; the model is inapplicable to very resistive
   ground and very high frequencies.
4. **Purely conductive response.** Induced polarisation (chargeability) is
   neglected; in clay-rich and sulphidic ground the negative transients this
   produces are a diagnostic, not a nuisance, but they are outside this model.
5. **Geometry and calibration are fixed.** Bird altitude, loop attitude and the
   zero level (bucking) must be monitored and corrected; an altitude error of a
   few metres changes the inferred depth systematically.

## 6. Python demonstration

`code/airborne_groundwater_demo.py` prints:

1. the diffusion depth for a table of resistivities and gate times;
2. the sensitivity kernel, its normalisation and its peak against the diffusion
   depth;
3. the apparent conductivity of a synthetic three-layer section, with the
   fraction of the kernel inside the target at each gate;
4. the DOI at three gates and the altitude/coupling table with the depth limit at
   each altitude;
5. the conductance equivalence of two models with $S = 2.0\ \mathrm{S}$;
6. the Bayes arithmetic of Section 3.4 for four priors.

```bash
cd 11-exploration-geophysics/05-groundwater-exploration/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python airborne_groundwater_demo.py
```

Companions:
[`exercises/04-airborne-groundwater-exercises.md`](./exercises/04-airborne-groundwater-exercises.md)
and
[`exercises/04-airborne-groundwater-solutions.md`](./exercises/04-airborne-groundwater-solutions.md).

## Common pitfalls

1. **Treating $\sigma_a$ at one gate as a layer conductivity.** It is an average
   with a stated kernel; the demonstration's earliest gate recovers only $58\%$
   of the target's true conductivity.
2. **Quoting a layer thickness.** Only the conductance is resolved; the thickness
   is a regularisation choice unless the section is thick relative to the window.
3. **Ignoring the base rate.** A technically excellent survey in a region where
   $8\%$ of anomalies are aquifers still delivers mostly clay.
4. **Comparing surveys of different altitude directly.** The coupling changes by
   a factor of $7$ between $30\ \mathrm{m}$ and $60\ \mathrm{m}$; a "deeper"
   anomaly may only be a higher flight line.
5. **Using the deep gates for depth.** Late gates have low signal and wide
   windows; the depth they "see" is $1.55d$ by the level definition, and the
   width is comparable.

## Mastery checkpoint

Complete this without notes:

> An AEM survey at $45\ \mathrm{m}$ altitude over $\rho \approx 40\
> \Omega\,\mathrm{m}$ ground reports a conductance anomaly of $S = 3.0\
> \mathrm{S}$ between 20 and 55 m depth, with a stated noise level of $2\%$ and a
> latest usable gate of $0.5\ \mathrm{ms}$. **(a)** Compute the diffusion depth
> and the DOI at $0.5\ \mathrm{ms}$. **(b)** Convert the conductance into two
> alternative layered models, and state why the data cannot choose between them.
> **(c)** Using $p = 0.10$, $\mathrm{TPR} = 0.75$, $\mathrm{FPR} = 0.35$, compute
> the posterior probability that the anomaly is a usable aquifer. **(d)** State
> the single next measurement that would most improve (c), and why it improves
> the decision rather than the dataset.

A worked version of (a) and (c) is in the lesson-05-04
[solutions](./exercises/04-airborne-groundwater-solutions.md).

## Related modules

- [11-05-02 EM and ERT for Groundwater Mapping](./02-em-and-ert-groundwater.md) —
  the ground-based methods that follow up an AEM anomaly.
- [11-05-03 Seismic Refraction and Surface Waves for Aquifers](./03-seismic-groundwater.md)
  — the independent porosity constraint.
- [11-05-01 Geophysical Signatures of Aquifers and Saline Interfaces](./01-aquifer-signatures.md)
  — what the conductivity means hydrogeologically.
- [08-05 Airborne EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/05-airborne-em.md)
  and [09-05-01 TEM Sounding](../../09-electrical-em-methods/05-em-methods-applications/01-tem-sounding.md).
- [14-02 Hydrogeophysical Methods](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/02-em-for-hydrology.md)
  — how AEM products enter a water-resource assessment.

## Self-assessment checklist

- [ ] I can derive $d = \sqrt{2\rho t/\mu_0}$ and use the constant $1261.6$.
- [ ] I can explain why $\sigma_a$ is an average and verify a kernel's normalisation.
- [ ] I can compute a DOI from a stated sensitivity level.
- [ ] I can quantify altitude against penetration and moment.
- [ ] I can state the conductance equivalence in one sentence.
- [ ] I can compute a PPV and interpret it as a drilling error rate.
