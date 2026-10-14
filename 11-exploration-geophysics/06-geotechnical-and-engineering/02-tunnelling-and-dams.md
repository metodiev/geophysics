---
id: 11-06-02
title: "Geophysics for Tunnels, Dams and Foundations"
level: doctoral
prereqs: ["11-06-01", "09-04-01", "06-10-06"]
tags: [exploration-geophysics, geotechnical, tunnelling, dams, seepage, self-potential, internal-erosion]
---

# Geophysics for Tunnels, Dams and Foundations

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the propagation of a picking error into a refraction depth and
   **compute** the depth uncertainty for a stated velocity contrast.
2. **Compute** the first-arrival delay produced by a thin low-velocity zone and
   **state** the thickness below which it is undetectable, distinguishing
   detection from resolution.
3. **Derive** the self-potential profile of a buried current dipole from the
   point-source potential in a half-space, and **compute** its amplitude and
   half-width.
4. **Derive** the steady one-dimensional advection-diffusion temperature profile
   and **compute** the Péclet number at which seepage becomes visible.
5. **Quantify** the look-ahead detection range of a tunnel face survey for a
   stated signal-to-noise ratio.
6. **State**, for each method, the false-negative mode that matters on a dam or a
   tunnel, and the observation that would expose it.

## Prerequisites

- [11-06-01 Site Investigation: Objectives and Method Selection](./01-site-investigation.md)
  — the objective-and-method logic this lesson applies to large structures.
- [09-04-01 Sources of the Self-Potential](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/01-self-potential-sources.md)
  — electrokinetic coupling and its geometry.
- [06-10-06 Engineering Seismics](../../06-seismology/10-refraction-and-near-surface-seismology/06-engineering-seismics.md)
  — the refraction and tomographic acquisition used ahead of a face.
- [02-05-04 Heat Conduction](../../02-physics/05-thermodynamics/04-heat-conduction.md)
  — the diffusion equation used in Section 3.4.

> All models and data in this module are **SYNTHETIC**. No real tunnel, dam,
> reservoir or site is used, and no design value or observed seepage rate is
> quoted.

## 1. Intuition: on a large structure, the false negative is the product

A geotechnical site investigation (lesson 01) can tolerate a miss if a borehole
or a design margin catches it. A tunnelling or dam investigation is different in
one decisive way: the consequence of a missed feature is not a recalculation but
an accident or a failure. A water-bearing fault ahead of a tunnel face becomes
an inflow; a permeable zone beneath a dam becomes internal erosion, which is
progressive and often invisible until it is advanced.

Two consequences follow, and they shape the whole lesson.

- **The false-negative rate is the headline, not the detection rate.** A method
  that detects 90% of karst cavities sounds good until the same number is applied
  to the hundred cavities under a reservoir. Section 3.3 in
  [11-06-03](./03-buried-objects-uxo.md) does that arithmetic.
- **The measurements are indirect and the interpretation is geometric.** A
  refraction delay tells you a low-velocity zone exists *somewhere* ahead; it
  does not tell you whether it is water-bearing. The geophysics narrows the
  possibilities and prioritises the probe drilling, and the decision rule must be
  written before the survey.

## 2. Precise definitions

### 2.1 Look-ahead, and what it can and cannot see

**Look-ahead** methods (seismic ahead of the face, tunnel GPR, tunnel
resistivity, probe drilling) sense the rock mass ahead of an advancing face. The
detectable quantity is a *contrast* in velocity, permittivity or resistivity
relative to the surrounding rock, at a range that decreases with the contrast and
increases with the array's offset and the rock's transparency. What is not
measurable directly is **water content** or **permeability**: a low-velocity,
low-resistivity zone could be wet or could be clay-rich and dry.

### 2.2 Seepage, self-potential, temperature

- **Electrokinetic (streaming) potential**: flow of water through a charged pore
  surface drags charge, producing a current and therefore a potential field at
  the surface. Its geometry follows the *current sources* (inflow and outflow
  regions) and its amplitude follows the head difference and the coupling
  coefficient of the rock.
- **Temperature tracer**: seepage transports heat by advection, so a steady
  temperature log in a borehole departs from the conductive (linear) profile. The
  controlling dimensionless number is the **Péclet number**

$$ \mathrm{Pe} = \frac{vL}{\kappa}, $$

with $v$ the Darcy (seepage) velocity, $L$ the depth interval and $\kappa$ the
thermal diffusivity.

### 2.3 Rippability and excavatability

A tunnel or foundation excavation is planned from the rock mass's
**excavatability**, which correlates with $v_p$ (and with the degree of
weathering and fracturing). This is a classification, not a physical law: the
same measured $v_p$ can correspond to different excavation classes in different
rock types, and a hard band a fraction of a metre thick can stop a machine. The
geophysical contribution is to map the *variability*, not to quote a class.

## 3. Derivations

### 3.1 A picking error becomes a depth error

From the intercept time, $z = v_1 t_i/(2\cos\theta_c)$ with
$\theta_c = \arcsin(v_1/v_2)$, so

$$ \frac{\partial z}{\partial t_i} = \frac{v_1}{2\cos\theta_c}. $$

The demonstration prints this coefficient for $v_2 = 3500\
\mathrm{m\,s^{-1}}$:

| $v_1$ (m/s) | $\theta_c$ (deg) | $z$ for $t_i = 20$ ms (m) | $\mathrm{d}z$ per 1 ms (m) |
|---|---|---|---|
| 800 | 13.21 | 8.22 | 0.41 |
| 1200 | 20.05 | 12.77 | 0.64 |
| 1500 | 25.38 | 16.60 | 0.83 |
| 2000 | 34.85 | 24.37 | 1.22 |

A 1 ms picking error is a 0.4-1.2 m depth error on the *intercept* — before the
velocity error is even considered. In a tunnel, where pick quality is poor
because of the confined geometry and machine noise, this is often the dominant
term, and it is systematic if the picker has a personal bias.

Note also the second route: from the crossover distance, $z = x_c/2\,
\sqrt{(v_2-v_1)/(v_2+v_1)}$, and $\mathrm{d}z/\mathrm{d}x_c = z/x_c$, so a 1 m
offset error is a $z/x_c$ metre depth error. Poorly surveyed shot positions
therefore bias the depth linearly.

### 3.2 A thin low-velocity zone: delay, detection and resolution

For a vertical path through a zone of thickness $h$ and velocity $v_{\text{slow}}$
in a host of velocity $v_{\text{fast}}$, the first-arrival delay is

$$ \Delta t = 2h\left(\frac{1}{v_{\text{slow}}}
- \frac{1}{v_{\text{fast}}}\right). $$

Setting $\Delta t$ equal to the picking error $\delta t = 1\ \mathrm{ms}$ gives
the minimum detectable thickness for $v_{\text{fast}} = 3500\
\mathrm{m\,s^{-1}}$:

| $v_{\text{slow}}$ (m/s) | contrast | $h_{\min}$ (m) |
|---|---|---|
| 1000 | 0.29 | 0.70 |
| 1500 | 0.43 | 1.31 |
| 2000 | 0.57 | 2.33 |
| 2500 | 0.71 | 4.38 |
| 3000 | 0.86 | 10.50 |

The table is the honest face of refraction ahead of a face: a strongly weathered
zone must be about a metre thick to be seen at all, and a mildly weathered one
tens of metres. **Detection is not resolution**: even when the delay is
detectable, the *thickness* and the *velocity contrast* enter only through the
product $h(1/v_{\text{slow}} - 1/v_{\text{fast}})$, so the two cannot be
separated without an independent constraint. Worse, a *faster* thin layer is
invisible to first arrivals altogether (no head wave is generated), so the
method has a blind spot that no amount of processing removes.

### 3.3 Self-potential from a buried current pair

In a uniform half-space with an insulating surface, the potential of a point
current source $I$ at depth $d$ is

$$ V(r) = \frac{I\rho}{2\pi r}, \qquad r = \sqrt{x^{2}+d^{2}} $$

(the factor 2 difference from the full-space formula is the surface boundary
condition). A seepage path is modelled as a **current dipole**: a source where
water enters the loss zone and a sink where it leaves, separated vertically. With
depths $d_1$ and $d_2$:

$$ V(x) = \frac{I\rho}{2\pi}\left[\frac{1}{\sqrt{x^{2}+d_1^{2}}}
- \frac{1}{\sqrt{x^{2}+d_2^{2}}}\right]. $$

The demonstration evaluates this with $\rho = 100\ \Omega\,\mathrm{m}$ and
sources at 10 m and 30 m:

| Current | Peak amplitude | Half-width at half maximum |
|---|---|---|
| 10 mA | 10.61 mV | 23.8 m |
| 50 mA | 53.05 mV | 23.8 m |

Two facts to read from the table. The amplitude scales **linearly with the
current** (a property of the seepage and the coupling, not of the target), and the
width is **independent of the current** and set by the source geometry — the
half-width is about $2.4\times$ the shallower source depth when the dipole is
long. So depth must be read from the *shape* of the profile and from the ratio of
the two lobes if the flow is horizontal, and never from the amplitude. A single
electrode reading has no depth information at all.

### 3.4 Temperature as a seepage tracer

Ignore lateral conduction and assume steady state. Heat conservation in one
dimension is

$$ \kappa \frac{\mathrm{d}^{2}T}{\mathrm{d}z^{2}}
= v\frac{\mathrm{d}T}{\mathrm{d}z}
\quad\Longrightarrow\quad
T(z) = A + B\,e^{vz/\kappa}. $$

Applying $T(0) = T_{\text{top}}$ and $T(L) = T_{\text{bot}}$:

$$ T(z) = T_{\text{top}}
+ (T_{\text{bot}}-T_{\text{top}})
\frac{e^{\mathrm{Pe}\,z/L}-1}{e^{\mathrm{Pe}}-1},
\qquad \mathrm{Pe} = \frac{vL}{\kappa}. $$

The demonstration uses $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$,
$L = 10\ \mathrm{m}$, $T$ from 10 to $20\ ^\circ$C, and reports the departure
from the linear (conductive) profile at 4 m depth:

| $v$ (m/s) | $\mathrm{Pe}$ | departure at 4 m (K) |
|---|---|---|
| 0 | 0 | 0.00 |
| $10^{-7}$ | 1.0 | $-1.14$ |
| $10^{-6}$ | 10.0 | $-3.98$ |
| $10^{-5}$ | 100 | $-4.00$ |

A departure of $0.5\ \mathrm{K}$ is a practical detection threshold for a logged
borehole, so this calculation puts the lower limit of detectable Darcy velocity
between $\mathrm{Pe} = 0$ and $\mathrm{Pe} = 1$, i.e. around
$v \approx \kappa/L = 10^{-7}\ \mathrm{m\,s^{-1}}$ — a seepage velocity, **not**
a permeability. Converting it to a permeability requires the hydraulic gradient,
which is an assumption, and converting it to a flow rate requires the area, which
is the very thing the survey is trying to find.

### 3.5 Look-ahead detection range

Model the look-ahead response as a stated teaching function of the distance to
the feature,

$$ A(d) = \frac{A_0}{1 + (d/d_0)^{2}}, $$

with $d_0$ a system- and geology-dependent scale and $A_0$ the response of a
feature at the face. Requiring $A(d) > 3\sigma$ gives the detection ranges in the
demonstration:

| Noise $\sigma/A_0$ | Look-ahead limit ($d_0 = 15$ m) |
|---|---|
| 0.05 | 35.5 m |
| 0.10 | 22.5 m |
| 0.20 | 12.0 m |

Doubling the noise roughly halves the range. The functional form is a teaching
choice; the **scaling** — range grows only as $\sqrt{A_0/\sigma}$ and not in
proportion to it — is the useful result, and it is why the advance rate, not the
instrument, usually sets the safe probe interval.

## 4. Worked examples

### Example 1 — a tunnel face with a 2 m clay-filled fault

A refraction look-ahead with $v_1 = 1500\ \mathrm{m\,s^{-1}}$, refractor
$v_2 = 3500\ \mathrm{m\,s^{-1}}$, intercept time picked to $\pm1.5\
\mathrm{ms}$.

$$ \frac{\partial z}{\partial t_i} = \frac{1500}{2\cos(25.38^\circ)}
= \frac{1500}{1.807} = 830\ \mathrm{m\,s^{-1}}
\quad\Longrightarrow\quad 0.83\ \mathrm{m\ per\ ms}, $$

so the depth uncertainty is $\pm1.25\ \mathrm{m}$ from picking alone (for a
$\pm1.5\ \mathrm{ms}$ pick). A 2 m
clay-filled fault in a $3500\ \mathrm{m\,s^{-1}}$ host with
$v_{\text{slow}} = 2000\ \mathrm{m\,s^{-1}}$ gives

$$ \Delta t = 2(2)\left(\frac{1}{2000}-\frac{1}{3500}\right)
= 4(2.143\times10^{-4}) = 0.86\ \mathrm{ms}, $$

which is *below* the picking error — the fault would be missed by first arrivals
even though it is 2 m thick and 43% slower. This is the concrete sense in which
the false-negative rate, not the resolution, is the headline number.

### Example 2 — reading a seepage SP profile

A profile across a dam foundation shows a symmetric positive anomaly peaking at
$12\ \mathrm{mV}$ with a half-width at half maximum of $25\ \mathrm{m}$. Matching
the demonstration's table (23.8 m half-width for sources at 10 and 30 m), the
geometry is consistent with shallow and deep current sources roughly 20 m apart,
and the current is about $11\ \mathrm{mA}$ for $\rho = 100\
\Omega\,\mathrm{m}$ (interpolating the 10.61 mV at 10 mA). What the profile does
**not** say is whether the flow is a leak or natural groundwater discharge of the
same magnitude: the survey locates a flow path, and the interpretation of its
significance needs the head data.

### Example 3 — a temperature log that shows seepage

A borehole 10 m from a reservoir logs $10.0\ ^\circ$C at 0 m and
$20.0\ ^\circ$C at 10 m. The conductive profile would give $14.0\ ^\circ$C at
4 m; the log reads $10.02\ ^\circ$C. From the table this matches
$\mathrm{Pe} \approx 10$, i.e. $v = \mathrm{Pe}\,\kappa/L = 10^{-6}\
\mathrm{m\,s^{-1}}$. If the gradient is $0.05$, the hydraulic conductivity would
be $K = v/i = 2\times10^{-5}\ \mathrm{m\,s^{-1}}$ — but the gradient is *assumed*,
and the area of the seepage path is unknown, so the honest output is "an
advective velocity of order $10^{-6}\ \mathrm{m\,s^{-1}}$ along the logged
interval", not a leak rate.

## 5. Assumptions and regime of validity

1. **Refraction depth** assumes two layers, a laterally invariant structure and
   a velocity *increase* with depth. A hidden fast layer biases the depth shallow
   (see the [11-05-03 §5](../05-groundwater-exploration/03-seismic-groundwater.md)
   treatment), and a velocity reversal is invisible.
2. **First-arrival delays** assume a vertical path through the zone; a zone wider
   than it is deep changes the geometry and the delay.
3. **Self-potential** assumes electrokinetic coupling is the dominant source;
   redox, corrosion of steel, and telluric fields also contribute, and the
   coupling coefficient is a rock property that must be measured locally if an
   amplitude is to be interpreted.
4. **Temperature tracer** assumes steady state, one-dimensional vertical
   conduction and negligible lateral flow. Transient responses (seasonal,
   operational) and three-dimensional flow both change the profile; a
   time-series of logs is far more informative than a single log.
5. **Look-ahead model** is a stated teaching function, not a system response. The
   scaling result is robust; the absolute ranges are not.

## 6. Python demonstration

`code/tunnelling_and_dams_demo.py` prints:

1. refraction depth and $\mathrm{d}z$ per 1 ms of picking error for four
   velocities;
2. the look-ahead detection limit for three noise levels;
3. the minimum detectable thickness of a thin low-velocity zone for five velocity
   contrasts;
4. the self-potential profile, amplitude and half-width of a buried current
   dipole at two current strengths;
5. temperature profiles for four Péclet numbers with the departure from the
   conductive profile at 4 m.

```bash
cd 11-exploration-geophysics/06-geotechnical-and-engineering/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tunnelling_and_dams_demo.py
```

Companions:
[`exercises/02-tunnelling-and-dams-exercises.md`](./exercises/02-tunnelling-and-dams-exercises.md)
and
[`exercises/02-tunnelling-and-dams-solutions.md`](./exercises/02-tunnelling-and-dams-solutions.md).

## Common pitfalls

1. **Quoting a detection rate without the false-negative count.** On a reservoir,
   the relevant number is how many features remain after the survey.
2. **Reading a seepage amplitude as a flow rate.** Amplitude scales with the
   coupling and the current, not with the target.
3. **Using a temperature log alone.** One log gives one profile; the seasonal
   and operational transients are what distinguish a leak from a background
   gradient.
4. **Assuming refraction finds thin weathering.** A metre-thick or a
   mildly-slowed zone is below the picking error.
5. **Treating an SP anomaly as a leak.** The same anomaly comes from natural
   discharge; the head and the reservoir level are needed to interpret it.

## Mastery checkpoint

Complete this without notes:

> A tunnelling project runs a refraction look-ahead with
> $v_1 = 1800\ \mathrm{m\,s^{-1}}$ and $v_2 = 4000\ \mathrm{m\,s^{-1}}$;
> intercept times are picked to $\pm1\ \mathrm{ms}$. **(a)** Compute
> $\cos\theta_c$ and $\mathrm{d}z/\mathrm{d}t_i$. **(b)** A 3 m zone of
> $v = 2200\ \mathrm{m\,s^{-1}}$ crosses the face: compute the first-arrival
> delay and state whether it is detectable. **(c)** A temperature log 15 m from a
> reservoir shows a $3.0\ \mathrm{K}$ departure from the conductive profile over
> 10 m; using $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, estimate the Darcy
> velocity order of magnitude. **(d)** Name one observation that would tell you
> whether (c) is a reservoir leak or natural discharge.

A worked version of (a) and (b) is in the lesson-06-02
[solutions](./exercises/02-tunnelling-and-dams-solutions.md).

## Related modules

- [11-06-01 Site Investigation: Objectives and Method Selection](./01-site-investigation.md)
  — the decision framework, including value of information.
- [11-06-03 Buried Objects, UXO Detection and Clearance](./03-buried-objects-uxo.md)
  — the false-negative arithmetic in its starkest form.
- [11-06-04 Landfill, Waste and Brownfield Site Assessment](./04-landfill-and-waste.md)
  — seepage and leachate as a conductivity problem.
- [09-04 Self-Potential and Related Methods](../../09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/01-self-potential-sources.md).
- [14-04 Contaminant and Environmental Geophysics](../../14-hydrology-hydrogeophysics/04-contaminant-and-environmental/02-landfill-investigation.md)
  — the monitoring context.

## Self-assessment checklist

- [ ] I can compute $\mathrm{d}z/\mathrm{d}t_i$ for a refraction look-ahead.
- [ ] I can compute the delay from a thin low-velocity zone and its detection
      limit.
- [ ] I can derive and evaluate a self-potential profile from two point sources.
- [ ] I can derive the advection-diffusion temperature profile and compute
      $\mathrm{Pe}$.
- [ ] I can state the false-negative mode of each method on a dam or tunnel.
- [ ] I can explain why an amplitude alone does not give depth or flow rate.
