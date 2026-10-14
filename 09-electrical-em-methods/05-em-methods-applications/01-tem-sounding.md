---
id: 09-05-01
title: "TEM Sounding for Aquifers and Mineral Targets"
level: graduate
prereqs: ["08-05-02", "09-01-02", "09-02-06", "01-10-04"]
tags: [electrical-methods, transient-em, time-domain-em, induction-number, diffusion-depth, apparent-conductivity, non-uniqueness]
---

# TEM Sounding for Aquifers and Mineral Targets

## Learning objectives

By the end of this lesson you will be able to:

1. **Write** the layered-earth diffusion response of a loop source and **verify**
   the integral kernel against a closed-form dipole field and against the
   reduction of a stack of identical layers.
2. **Derive** the diffusion depth $\delta = \sqrt{2t/(\mu_0\sigma)}$ and convert
   between a time window and a frequency, stating that this conversion is exact
   but is *not* a depth of investigation.
3. **Explain** and **measure** the induction-number scaling of a loop response,
   including the measured offset scaling of its amplitude.
4. **Define** a median depth of investigation, measure it against frequency, and
   **state** the measured exponent that replaces the naive $\delta$ scaling.
5. **Measure** the response of a synthetic aquifer model across four decades of
   frequency and identify the window in which a resistive layer is visible.
6. **Demonstrate** the conductance equivalence of a thin and a thick conductor,
   and quantify the error of assuming it is exact.
7. **Report** a TEM sounding as a conductance with an admitted range of
   thickness–conductivity pairs, not as a layer thickness.

## Prerequisites

- [08-05-02 Time-Domain EM (TDEM): Sounding, Transients and Decay Curves](../../08-geomagnetism-electromagnetism/05-controlled-source-em/02-time-domain-em.md)
  — the transient system and its decay curves.
- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md)
  — why an aquifer is a resistivity contrast.
- [09-02-06 Forward Modelling Resistivity Data](../02-dc-resistivity/06-resistivity-forward-modelling.md)
  — what a forward model is for, and how to validate one.
- [01-10-04 Discrete Fourier Transform and the FFT](../../01-mathematics/10-fourier-analysis/04-discrete-fourier.md)
  — the band-limited description of a transient.

**All models and data in this module are SYNTHETIC.** Conductivities, thicknesses,
offsets, frequencies, heights and noise are chosen teaching values, not
measurements of any real aquifer, ore body, survey or instrument.

---

## 1. Intuition: a sounding is a set of windows, not a depth

A transient electromagnetic sounding works by switching a current off and
watching the ground relax. Early after switch-off the currents flow near the
surface; later they have diffused deeper. The measured decay curve is therefore
a *time-sequenced* set of sensitivities to depth, and the entire interpretive
apparatus is about converting time into depth — carefully.

Three facts set every limit in this lesson.

1. **The conversion time → depth is diffusive, not geometric.** The depth scale
   is $\delta = \sqrt{2t/(\mu_0\sigma)}$, which depends on the conductivity the
   survey is trying to measure, and which grows only as the square root of time.
2. **The measurable frequency and the measurable depth are linked.** A frequency
   $f$ corresponds to a diffusion time $t = 1/(2\pi f)$ exactly, so "high
   frequency" and "early time" are the same statement. What that *does not* mean
   is that $\delta$ at that frequency is the depth being sampled; Section 4
   measures how far off that is.
3. **What a datum constrains is a conductance, not a layer.** A thin, conductive
   layer and a thick, less conductive one produce almost the same response; the
   admitted range of thickness–conductivity pairs is what an honest report
   carries.

## 2. Precise definitions

### 2.1 The response used here

A horizontal loop (a vertical magnetic dipole) of moment $m$ at height $h$, with
the receiver at the same height and a horizontal offset $r$, over a layered
earth. In the quasi-static limit the secondary vertical field is

$$H_s = \frac{m}{4\pi}\int_0^{\infty} \lambda^{2}\,R(\lambda)\,
e^{-2\lambda h}\,J_0(\lambda r)\,\mathrm{d}\lambda ,$$

with $R(\lambda)$ the magnetic-field reflection coefficient of the layered stack,
computed from the TE-mode admittance recursion
$u_j = \sqrt{\lambda^{2} + i\omega\mu_0\sigma_j}$ and the wave impedance
$Z_j = i\omega\mu_0/u_j$. The **response ratio** is $H_s/H_p$ with the free-space
value $H_p = -m/(4\pi r^{3})$ at the same location.

### 2.2 Quantities

| Quantity | Symbol | Definition | Unit |
|---|---|---|---|
| diffusion depth | $\delta$ | $\sqrt{2t/(\mu_0\sigma)}$ | m |
| induction number | $\theta$ | $\omega\mu_0\sigma r^{2}/4$ | — |
| conductance | $S$ | $\sigma h$ | S |
| median depth of investigation | $z_{50}$ | depth above which half the cumulative response change lies | m |

## 3. Derivations

### 3.1 Validation before use

The integral kernel in Section 2.1 is validated in two independent ways, both
printed by the demonstration.

**(a) A closed form for the same integral.** With $R$ replaced by the image
exponential (a source at height $h$ and its image at $-h$), the integral reduces
to the dipole field at a separation $2h$:

$$\int_0^{\infty}\lambda^{2}e^{-2\lambda h}J_0(\lambda r)\,\mathrm{d}\lambda
= \frac{2(2h)^{2} - r^{2}}{\left[r^{2} + (2h)^{2}\right]^{5/2}} .$$

At $h = 0.5$ m and $r = 20$ m the demonstration's quadrature and this closed form
agree to a relative $1.21\times10^{-15}$ — round-off, i.e. the quadrature and the
kernel structure are correct.

**(b) A physical reduction.** A stack of three layers with identical
conductivity must reproduce a half-space. The measured relative difference is
$6.81\times10^{-13}$.

The truncation of the integral is also verified: changing the upper limit by a
factor ten changes the response by less than $1\times10^{-9}$ relative, because
the integrand is controlled by three decay mechanisms — the geometry $1/r$, the
diffusion $1/\delta$ and the height factor $1/2h$ — and the limit is chosen to
resolve all three.

### 3.2 The low-induction-number limit

For a weakly conducting ground ($\theta \ll 1$) the reflection coefficient tends
to $R \approx ik^{2}/(4\lambda^{2})$ with $k^{2} = i\omega\mu_0\sigma$, so
$\lambda^{2}R \to i\omega\mu_0\sigma/4$ and the response acquires a term linear in
$\sigma$. The demonstration measures the ratio of the response to $i\theta$:

| $\theta$ | $H_s/H_p \div i\theta$ |
|---|---|
| $1\times10^{-4}$ | $-0.98368 + 0.01484i$ |
| $1\times10^{-3}$ | $-0.95115 + 0.04542i$ |
| $1\times10^{-2}$ | $-0.84947 + 0.12972i$ |
| $1\times10^{-1}$ | $-0.55053 + 0.29504i$ |

The limit is $H_s/H_p \to -i\theta$: a **quadrature response linear in
conductivity** and an in-phase channel that is second order. The minus sign is
the sign convention of the secondary field (total minus primary) and is stated so
that it can be checked; only magnitudes are used below.

### 3.3 The induction number, measured

At a *fixed* offset the half-space response depends on $\sigma$ and $\omega$ only
through $\theta$. The demonstration tests this with three combinations that share
$\theta = 0.007106$ — $(\sigma, f) = (0.01\ \mathrm{S/m}, 100\ \mathrm{Hz})$,
$(0.001, 1000)$ and $(0.04, 25)$ — and finds the same value to a spread of
$0.0000\%$.

Changing the offset at constant $\theta$ scales the response by a factor
$8.0001$ for a factor two in $r$, i.e. as $r^{-3}$: the geometric spreading is
separate from the diffusion physics. **A single response number therefore cannot
give both the conductivity and the geometry**, which is the mildest form of the
non-uniqueness measured in Section 3.6.

### 3.4 The diffusion depth, and what it is not

$$\delta(t) = \sqrt{\frac{2t}{\mu_0\sigma}},
\qquad
\delta(f) = \sqrt{\frac{2}{2\pi f\,\mu_0\sigma}},
\qquad
t = \frac{1}{2\pi f}.$$

The demonstration prints, for four conductivities:

| $\sigma$ (S/m) | $\delta$ at 1 ms | $\delta$ at 10 ms | $\delta$ at 100 ms |
|---|---|---|---|
| 0.001 | 1261.57 m | 3989.42 m | 12 615.66 m |
| 0.010 | 398.94 m | 1261.57 m | 3989.42 m |
| 0.100 | 126.16 m | 398.94 m | 1261.57 m |
| 1.000 | 39.89 m | 126.16 m | 398.94 m |

$\delta$ is the depth scale of a diffusing field, not a depth of investigation.
Section 3.5 measures the difference.

### 3.5 A median depth of investigation, and its measured scaling

Define the **cumulative sensitivity** as the relative change in $|H_s|$ when the
conductivity of the top $z$ metres is scaled by $10\%$, and let $z_{50}$ be the
depth at which that cumulative change reaches half of its saturated value. For a
half-space of $0.01$ S/m at $60$ m offset:

| frequency | $\delta$ (m) | $z_{50}$ (m) | $z_{50}/\delta$ | saturation (%) |
|---|---|---|---|---|
| 1 Hz | 5032.92 | 48.2 | 0.01 | 9.600 |
| 10 Hz | 1591.55 | 47.4 | 0.03 | 9.680 |
| 100 Hz | 503.29 | 42.5 | 0.08 | 9.343 |
| 1000 Hz | 159.15 | 33.2 | 0.21 | 7.923 |

Over these three decades $\delta$ falls by a factor $31.6$ while $z_{50}$ falls
by only $1.45$, a measured scaling

$$z_{50} \propto \delta^{0.107} .$$

**The diffusion depth massively overstates how fast the depth range of a sounding
moves with frequency.** The exponent is a property of the offset and of this
definition, and it is the number to quote — not $\delta$.

### 3.6 Conductance equivalence, measured

Take a thin conductor at $40$ m depth in a $0.01$ S/m half-space and vary its
conductivity and thickness at constant conductance $S = \sigma h = 2$ S:

| model | $S$ (S) | thickness | rms difference in $|H_s|$ over 0.1–1000 Hz |
|---|---|---|---|
| 2 m at 1.0 S/m | 2.00 | 2 m | reference |
| 4 m at 0.5 S/m | 2.00 | 4 m | 2.19% |
| 20 m at 0.1 S/m | 2.00 | 20 m | 17.27% |
| 2 m at 0.5 S/m | 1.00 | 2 m | 32.47% |

The same-conductance family spans $2.19\%$ to $17.27\%$: **the equivalence is
exact only in the vanishing-thickness limit**, and its error grows with the
thickness ratio. Halving the conductance differs from the family by $32.47\%$. So
the data constrain the conductance to a band whose width is set by the thickness
of the responding layer — and a depth quoted without that band is a claim the
data do not support.

## 4. Physical interpretation

- **Time is frequency, depth is not time.** $t = 1/(2\pi f)$ is exact and free;
  converting either to a depth requires an assumed conductivity and a measured
  sensitivity kernel.
- **The response grows with conductance, saturating in contrast.** Because the
  quadrature is linear in $\sigma$ at small $\theta$ and the section as a whole
  controls $\theta$, a *conductive* target saturates and a *resistive* target —
  an aquifer, a gas sand, a resistive unit — is seen as a reduction in the
  response. Mineral targets (conductors) and aquifer targets (resistors) are
  therefore at opposite ends of the same measurement.
- **Sensitivity is non-monotone in offset.** For a target at a fixed depth there
  is an offset at which the diffusion depth in the section matches the target's
  depth; shallower targets favour shorter offsets.
- **Non-uniqueness is structural.** Conductance, depth and thickness cannot all
  be recovered from one offset and one band; adding offsets or frequencies adds
  equations, and each one is worth roughly one order of magnitude in the admitted
  range.

## 5. Assumptions and regime of validity

1. **A layered, isotropic earth** — no lateral variation, no anisotropy. A
   dipping or faulted aquifer is a three-dimensional problem.
2. **A loop (vertical magnetic dipole) source and receiver at a stated height.**
   The height is not a formality: the kernel's convergence depends on it, and a
   real system has one.
3. **Quasi-static (diffusive) physics.** Displacement currents are neglected; the
   demonstration's own Section 7 shows that a normal-incidence plane-wave model
   has *no* transient response, so the geometry must be retained.
4. **No induced polarisation, no magnetisation.** Both add a response this model
   does not contain; [09-03-01](../03-induced-polarisation/01-ip-principle.md)
   quantifies that response.
5. **Noise-free forward model.** Detectability enters only through the stated
   thresholds and the equivalence band; a real survey's random error multiplies
   the admitted range.
6. **The layered model is the answer to a different question than "what is the
   aquifer".** A resistivity model is a conductivity profile; the conversion to
   porosity or saturation needs Archie's law and its own assumptions
   ([09-01-02](../01-electrical-properties-of-earth/02-archies-law.md)).

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| diffusion depth | $\delta$ | m | $\sqrt{\mathrm{s}/(\mathrm{H\,m^{-1}}\,\mathrm{S\,m^{-1}})}$ |
| induction number | $\theta$ | — | $\mathrm{s^{-1}}\times\mathrm{H\,m^{-1}}\times\mathrm{S\,m^{-1}}\times\mathrm{m^{2}}$ |
| response | $H_s/m$ | $\mathrm{m^{-3}}$ | $\mathrm{A\,m^{-1}}/\mathrm{A\,m^{2}}$ |
| response ratio | $H_s/H_p$ | — | same units cancel |
| conductance | $S$ | S | $\mathrm{S\,m^{-1}}\times\mathrm{m}$ |
| median depth | $z_{50}$ | m | a length |

A check worth doing on any sounding calculation: the response ratio must be a
pure number and must be independent of the source moment, since both $H_s$ and
$H_p$ scale with $m$. If a computed ratio changes when the moment is doubled, the
primary field has been coded with the wrong normalisation.

## 7. Worked examples

### Example 1 — a depth from a time and a conductivity

An aquifer at $60$ m depth in a section whose bulk conductivity is $0.05$ S/m.
The diffusion depth equals $60$ m at

$$t = \frac{\mu_0\sigma\delta^{2}}{2}
= \frac{4\pi\times10^{-7} \times 0.05 \times 3600}{2} = 1.13\times10^{-4}\ \mathrm{s}
= 0.113\ \mathrm{ms},$$

i.e. at $f = 1/(2\pi t) = 1409$ Hz. So the window that can *reach* that depth is
of order $0.1$ ms — and the median depth of investigation at $1000$ Hz measured
in Section 3.5 is $33.2$ m, not the $159$ m that $\delta$ would suggest. The two
numbers differ by a factor $4.8$, which is exactly the content of the measured
exponent $0.107$.

### Example 2 — the same measurement from two different grounds

From Section 3.6, a $2$ m layer of $1$ S/m and a $20$ m layer of $0.1$ S/m both
have $S = 2$ S. Their responses differ by $17.27\%$ rms over the band. To make
that difference *smaller* than a stated $5\%$ noise level, the thickness ratio
must be reduced: interpolating the two measured entries, a thickness ratio of
about $2.4$ (i.e. a $5$ m layer at $0.4$ S/m against a $2$ m layer at $1$ S/m)
sits at the $5\%$ threshold. **A sounding therefore resolves a layer's thickness
only to within a factor of about $2.4$ at $5\%$ noise**, and that factor, not a
thickness, is the honest output.

### Example 3 — why an aquifer and a sulphide body look different

An aquifer is a *resistor*: at $20$ m depth its response ratio (Section 3.5's
synthetic model) departs from the background by $2.5\%$ at $0.1$ Hz and by
$78.9\%$ at $10$ kHz — a rise in $|H_s|$ because the currents must flow around
the resistor. A sulphide body is a *conductor*: the same machinery applied to a
conductive layer gives a *fall* in $|H_s|$. The sign of the response ratio is
therefore the first discriminant, and it requires only that the reference model
be stated.

## 8. Python demonstration

`code/tem_sounding_demo.py` prints every number in this lesson:

1. the kernel validation ($1.21\times10^{-15}$ against the closed form,
   $6.81\times10^{-13}$ for the identical-layer reduction) and the truncation
   sweep;
2. the low-induction-number limit and the induction-number collapse
   ($0.0000\%$ spread) with the measured $r^{-3}$ offset scaling;
3. the diffusion-depth table;
4. the median depth of investigation against frequency, with the measured
   exponent $0.107$;
5. a synthetic aquifer model across four decades of frequency;
6. the conductance-equivalence family;
7. the demonstration that a normal-incidence (plane-wave) reflection coefficient
   is frequency-independent ($R \to +1$ as $\lambda \to 0$), which is why the
   geometry must be retained.

```bash
cd 09-electrical-em-methods/05-em-methods-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python tem_sounding_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-tem-sounding-exercises.md`](./exercises/01-tem-sounding-exercises.md)
and
[`exercises/01-tem-sounding-solutions.md`](./exercises/01-tem-sounding-solutions.md).

- **★** Compute $\delta$ for $\sigma = 0.02$ S/m at 0.1, 1 and 10 ms, and the
  frequency corresponding to 1 ms.
- **★** State the induction number for a $50$ m offset, $1000$ Hz and
  $0.01$ S/m, and say whether the response is in the linear regime.
- **★★** Derive $H_s/H_p \to -i\theta$ from $R \approx ik^{2}/(4\lambda^{2})$ and
  the low-$\lambda$ regularisation, and state the two approximations.
- **★★** Using the measured $z_{50}$ table, estimate the frequency needed to
  investigate $100$ m in a $0.01$ S/m section, and compare with the $\delta$
  estimate.
- **★★★** Design a two-offset sounding that separates a $2$ m layer at $1$ S/m
  from a $20$ m layer at $0.1$ S/m, and state the statistic.

## 10. Common mistakes

1. **Quoting $\delta$ as a depth of investigation.** Measured $z_{50}$ is a small
   fraction of it, and it scales as a much weaker power.
2. **Forgetting that the response is a ratio.** It is independent of the source
   moment, so an amplitude comparison across surveys needs the same geometry.
3. **Reading a conduction equivalence as a layer.** The admitted thickness range
   is a factor of about $2.4$ at $5\%$ noise for the model of Example 2.
4. **Assuming a plane-wave or normal-incidence model.** It has no transient
   response in the quasi-static limit (Section 8, item 7).
5. **Ignoring the loop height.** It sets both the near-surface sensitivity and
   the numerical convergence of the kernel.
6. **Converting a conductivity model into a saturation without stating Archie's
   parameters.** The petrophysical step has its own assumptions.

## 11. Real-world applications

- **Groundwater and aquifer mapping.** A resistive (fresh-water) layer in a
  conductive (saline or clay-rich) section is the classical TEM target.
- **Mineral exploration.** Conductive massive-sulphide bodies are the opposite
  sign of anomaly, and the conductance equivalence of Section 3.6 is the reason
  resource estimates quote conductance rather than thickness.
- **Permafrost and engineering.** A frozen layer is resistive; the detectability
  of its base is a window question of the kind measured in
  [04 EM for Geothermal Systems and Permafrost](04-em-geothermal-permafrost.md).
- **Hydrocarbon and gas-hydrate exploration.** The same diffusive window logic
  underlies a marine sounding, with the water column as an extra attenuating
  layer ([03 Marine CSEM](03-csem-marine.md)).

## 12. Related lessons

- [02 FEM Conductivity Mapping and Apparent Conductivity](02-fem-conductivity-mapping.md) —
  the frequency-domain equivalent of the same measurement.
- [03 Marine CSEM for Hydrocarbon and Gas Hydrate Exploration](03-csem-marine.md) —
  the same response with a conductive water column above it.
- [08-05-02 Time-Domain EM](../../08-geomagnetism-electromagnetism/05-controlled-source-em/02-time-domain-em.md) —
  the system and its transients.
- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md) —
  the petrophysical step from conductivity to saturation.
- [18-inverse-problems](../../18-inverse-problems/README.md) — the systematic
  treatment of the equivalence measured here.

## 13. Self-assessment checklist

- [ ] I can write the layered loop response and describe its validation.
- [ ] I can derive $\delta$, and state what it is not.
- [ ] I can test a response for the induction-number collapse.
- [ ] I can measure and interpret a median depth of investigation.
- [ ] I can state the conductance equivalence and its measured error.
- [ ] I can explain why an aquifer and a sulphide body give opposite signs.
- [ ] I can write an inversion report as a conductance range with the band stated.
