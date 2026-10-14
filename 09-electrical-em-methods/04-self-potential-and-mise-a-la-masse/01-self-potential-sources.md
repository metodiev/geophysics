---
id: 09-04-01
title: "Sources of Self-Potential: Electrokinetic, Electrochemical"
level: graduate
prereqs: ["09-01-01", "09-03-03", "02-07-01", "01-05-05"]
tags: [electrical-methods, self-potential, electrokinetic, streaming-potential, nernst, membrane-polarisation, non-uniqueness]
---

# Sources of Self-Potential: Electrokinetic, Electrochemical

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a self-potential (SP) survey measures a *current
   distribution* in the ground rather than a property of the ground, and
   **state** the consequences of the measurement being relative to a moving
   reference electrode.
2. **Derive** the Helmholtz-Smoluchowski electrokinetic coupling coefficient
   $\partial V/\partial P = \varepsilon\zeta/(\eta\sigma)$ and **compute** the
   hydraulic head that a stated SP anomaly requires.
3. **Compute** Nernst electrochemical potentials from standard reduction
   potentials, and **derive** the membrane (diffusion) potential as a function
   of the cation transference number.
4. **Derive** the half-space potential of a buried point current electrode by the
   image method, and the potential of a buried current dipole.
5. **Derive and verify** the two profile-width rules — $2\sqrt{3}$ for a point
   source and $2\sqrt{2^{2/3}-1}$ for a point dipole — and use the measured width
   of an anomaly to obtain a depth.
6. **Demonstrate** that a surface profile constrains a ridge of
   $(\text{depth},\ \text{length},\ \text{current})$ triples, and **report** the
   admitted set.
7. **State** which of the two source mechanisms dominates in a given setting and
   what measurement would test that claim.

## Prerequisites

- [09-01-01 Resistivity and Conductivity: Definitions and Ranges](../01-electrical-properties-of-earth/01-resistivity-conductivity.md)
  — the bulk conductivity that converts a current distribution into a potential.
- [09-03-03 IP Acquisition, Chargeability and Phase Units](../03-induced-polarisation/03-ip-acquisition.md)
  — electrode effects and the noise that limits a small-potential measurement.
- [02-07-01 Electrostatics, Coulomb's Law and Electric Potential](../../02-physics/07-electromagnetism/01-electrostatics.md)
  — the potential of a point charge in a medium, and the boundary condition at an
  insulating surface.
- [01-05-05 Integration Techniques and Definite Integrals](../../01-mathematics/05-single-variable-calculus/05-integration.md)
  — the integrals used for the image method and the diffusion potential.

**All models and data in this module are SYNTHETIC.** The coupling coefficient,
zeta potential, redox couples, conductivity, geometry and noise are chosen
teaching values, not measurements of any real fluid, mineral, ore body, dam,
landfill or instrument. Physical constants (the permittivity of vacuum, standard
gravity, the gas constant, the Faraday constant) are standard values with units
stated.

---

## 1. Intuition: SP measures a current, not a property

An SP survey plants two electrodes, measures a voltage between them, and repeats
that along a profile without ever injecting current. The voltage is not a
property of the ground in the way a resistivity is. It is the *surface effect of
charges and currents inside the ground*, and those currents come from two very
different sources:

- **Electrokinetic**, where moving pore water drags its excess charge along with
  it and drives a current — a *streaming* current;
- **Electrochemical**, where a geochemical difference (an oxidising mineral body,
  a salinity contrast across a clay layer) creates a potential difference that
  drives a current.

Both produce the same surface field, and the surface field is all that is
measured. So the organising idea of this lesson is a three-step chain:

$$\text{source mechanism} \;\longrightarrow\; \text{current distribution}
\;\longrightarrow\; \text{surface potential}$$

The first step is chemistry and fluid mechanics, the second is the same
potential theory used everywhere in this folder, and the third is Laplace's
equation with an insulating surface above. Two consequences run through the whole
module:

1. **The measurement is relative.** SP is a potential difference between two
   electrodes, and a drifting reference electrode contributes to every
   measurement. Absolute SP is a convention, not an observable.
2. **The inverse problem is non-unique in a specific, quantifiable way.** A
   source of a given surface expression can be deeper and stronger, or shallower
   and weaker; only the *width* of the pattern constrains the depth, and it does
   so weakly. Section 5 measures how weakly.

## 2. Precise definitions

### 2.1 Electrokinetic coupling

For a pore fluid of conductivity $\sigma$ [S/m], dynamic viscosity
$\eta$ [Pa s], permittivity $\varepsilon = \varepsilon_r\varepsilon_0$ [F/m] and
zeta potential $\zeta$ [V], the coupling coefficient is

$$\boxed{\;\frac{\partial V}{\partial P} =
\frac{\varepsilon\zeta}{\eta\sigma}\quad
[\mathrm{V\,Pa^{-1}}],\;}$$

the **Helmholtz-Smoluchowski** coefficient. It converts a pore-pressure gradient
into an electric field. It is negative for the usual mineral-water interface
($\zeta < 0$), so the potential rises in the direction of flow.

### 2.2 Electrochemical potentials

The **Nernst potential** of a half-reaction with $n$ electrons and reaction
quotient $Q$ is

$$E = E^{0} + \frac{RT}{nF}\ln Q ,$$

with $R = 8.314462618\ \mathrm{J\,mol^{-1}\,K^{-1}}$ and
$F = 96485.33212\ \mathrm{C\,mol^{-1}}$ (both exact by definition) and
$E^{0}$ the standard reduction potential [V]. A buried mineral body acts as a
short-circuited cell whose two half-reactions occur at different places, so a
potential difference of order the cell potential appears across it.

### 2.3 The membrane (diffusion) potential

For a 1:1 electrolyte separating two reservoirs of activities $a_1$ and $a_2$
across a medium that transmits cations and anions unequally, the steady
zero-current potential drop is

$$E = \frac{RT}{F}\left(t_{+} - t_{-}\right)\ln\frac{a_1}{a_2},
\qquad t_{+} + t_{-} = 1 ,$$

where $t_{\pm}$ are the transference numbers. A perfectly cation-selective
medium ($t_+ = 1$) gives the full Nernst value
$\frac{RT}{F}\ln(a_1/a_2)$; a neutral medium ($t_+ = t_- = 1/2$) gives zero.

### 2.4 Source geometry

In the ground the three mechanisms are represented by a **current
distribution**. Two idealised elements are enough for this module:

- a **point current electrode** of current $I$ [A] at depth $h$ [m] — a strongly
  polarised compact body or an injection or leakage point;
- a **current dipole**, a source and a sink separated by a length $L$ [m] — a
  polarised body with two chemically different ends, or a seepage line with an
  inflow and an outflow region.

## 3. Derivations

### 3.1 The streaming potential

Two equations couple in a fluid-filled pore: the flow obeys Darcy's law (or, in a
capillary, Poiseuille's law) and the charge transport obeys Ohm's law with a
convective term. In a cylindrical capillary of radius $r_c$ the net charge
density near the wall is
$\rho_e \approx \varepsilon\zeta$ per unit of specific surface; the assumption
that the double layer is thin compared with $r_c$ (the **Debye-Hückel**
limit) makes this a statement about the wall charge alone. The convective current
is $\rho_e$ times the fluid velocity integrated over the cross-section, the
conduction current is $\sigma$ times the electric field, and their balance under
zero net current gives

$$\sigma E = -\varepsilon\zeta\,\frac{\Delta P}{L}
\;\Longrightarrow\;
E = -\frac{\varepsilon\zeta}{\eta\sigma}\,\frac{\partial P}{\partial x}
\quad\left(\text{with } \frac{\partial P}{\partial x} = \frac{\eta u}{r_c^{2}}\right),$$

where the last step uses Poiseuille's relation between the pressure gradient and
the mean velocity, and the $\eta$ in the coefficient is the viscosity. Writing
this as $\partial V/\partial P = \varepsilon\zeta/(\eta\sigma)$ gives the
coefficient of Section 2.1.

**Measured consequences.** With $\varepsilon_r = 80.1$ and
$\varepsilon_0 = 8.8541878128\times10^{-12}$ F/m, so
$\varepsilon = 7.092204\times10^{-10}$ F/m, with $\zeta = -20$ mV and
$\eta = 10^{-3}$ Pa s, the coefficient falls as $1/\sigma$:

| $\sigma$ (S/m) | $\partial V/\partial P$ (V/Pa) | $\partial V/\partial h$ (mV per m of head) | head for 10 mV (m) |
|---|---|---|---|
| 0.001 | $-1.418441\times10^{-5}$ | $-139.102$ | 0.072 |
| 0.010 | $-1.418441\times10^{-6}$ | $-13.910$ | 0.719 |
| 0.100 | $-1.418441\times10^{-7}$ | $-1.391$ | 7.189 |
| 1.000 | $-1.418441\times10^{-8}$ | $-0.139$ | 71.890 |

One metre of water head is $9806.6$ Pa with
$\rho_w = 1000\ \mathrm{kg\,m^{-3}}$ and $g = 9.80665\ \mathrm{m\,s^{-2}}$. Read
the last column carefully: at a bulk conductivity of $0.001$ S/m, a *7 cm* head
difference produces 10 mV, while in saline ground of $1$ S/m the same anomaly
needs **72 m** of head. This single table is why SP works well for seepage in
resistive ground and poorly in saline ground.

### 3.2 Nernst potentials, worked from standard couples

$$\frac{RT}{F}\Big|_{T = 298.15\ \mathrm{K}} = 25.693\ \mathrm{mV},
\qquad \frac{RT}{F}\ln 10 = 59.159\ \mathrm{mV per decade}.$$

Standard reduction potentials used here (V vs the standard hydrogen electrode,
25 °C, unit activity) are $\mathrm{O_2/H_2O} = +1.229$,
$\mathrm{Fe^{3+}/Fe^{2+}} = +0.771$, $\mathrm{Cu^{2+}/Cu} = +0.342$,
$\mathrm{H^{+}/H_2} = 0.000$, $\mathrm{Zn^{2+}/Zn} = -0.762$. A cell formed by a
cathodic and an anodic half-reaction has $E^{0}_{\text{cell}} = E^{0}_{\text{cathode}}
- E^{0}_{\text{anode}}$, giving, in the demonstration's table, $+0.458$ V for
$\mathrm{O_2/H_2O}$ against $\mathrm{Fe^{3+}/Fe^{2+}}$, $+0.887$ V for
$\mathrm{O_2/H_2O}$ against $\mathrm{Cu^{2+}/Cu}$ and $+1.104$ V for
$\mathrm{Cu^{2+}/Cu}$ against $\mathrm{Zn^{2+}/Zn}$.

The *measured* SP difference across a mineralised zone is far smaller than a
cell potential, because the two half-cells are short-circuited by the conducting
body itself and the ground around it. What survives is the $IR$ drop in the
surrounding ground, of order tens to hundreds of millivolts. The concentration
dependence sets that scale: $59.159$ mV per decade of activity ratio, i.e.
$0.592$ V for ten decades — and only a few decades are chemically available,
which caps the electrochemical contribution at a few hundred millivolts.

### 3.3 The membrane potential, and why clay matters

For a salinity contrast of one decade ($\ln 10 = 2.302585$), the demonstration
computes $E = \frac{RT}{F}\left(t_+ - t_-\right)\ln 10$:

| $t_+$ | $E$ (mV) | reading |
|---|---|---|
| 0.20 | $-35.496$ | anion-selective medium |
| 0.40 | $-11.832$ | anion-selective |
| 0.50 | $0.000$ | no selectivity |
| 0.60 | $+11.832$ | cation-selective (clay-like) |
| 0.80 | $+35.496$ | cation-selective |
| 1.00 | $+59.159$ | ideal cation-selective membrane |

A clay-rich bed is cation-selective because its negatively charged surfaces
concentrate cations in the double layer, raising $t_+$ above $0.5$. So a salinity
contrast *across* a clay layer produces a potential difference of up to
$59.159$ mV per decade, with the sign set by the direction of the contrast. This
is the mechanism behind most electrochemical SP in sedimentary settings, and it
is also the mechanism behind the membrane polarisation of
[09-01-04](../01-electrical-properties-of-earth/04-clay-and-surface-conduction.md).

### 3.4 The potential of a buried source, by the image method

In a half-space of conductivity $\sigma$ with an insulating surface at $z = 0$, a
point current electrode at depth $z_0$ is handled by mirroring it: the boundary
condition $\partial V/\partial z = 0$ at $z = 0$ is satisfied by a **second
electrode of the same sign** at $-z_0$. So

$$V(x,z) = \frac{I}{4\pi\sigma}\left(\frac{1}{r_1} + \frac{1}{r_2}\right),
\qquad r_{1,2} = \sqrt{x^{2} + (z \mp z_0)^{2}} .$$

On the surface this reduces to the familiar half-space result

$$V(x) = \frac{I}{2\pi\sigma\sqrt{x^{2} + z_0^{2}}}
= \frac{\rho I}{2\pi\sqrt{x^{2} + z_0^{2}}} ,$$

which the demonstration checks at $x = 0$: $39.789$ mV at $r = 40$ m for
$I = 0.1$ A and $\sigma = 0.01$ S/m. A source and a sink separated by $L$
(so the total current is zero, as it must be in the ground) superpose.

### 3.5 Two width rules, both exact

For a **point source** at depth $h$, the profile is
$V(x) \propto 1/\sqrt{x^{2}+h^{2}}$. Setting $V = V_{\max}/2$ gives
$x^{2} + h^{2} = 4h^{2}$, so the full width at half maximum is

$$\mathrm{FWHM} = 2\sqrt{3}\,h = 3.464\,h .$$

For a **point dipole** (source above sink, $L \ll h$) the surface profile is
$V(x) \propto h/\left(x^{2}+h^{2}\right)^{3/2}$. Setting
$V = V_{\max}/2$ gives $\left(x^{2}+h^{2}\right)^{3/2} = 2h^{3}$, so
$x^{2} = h^{2}\left(2^{2/3}-1\right)$ and

$$\mathrm{FWHM} = 2\sqrt{2^{2/3}-1}\,h = 1.5328\,h .$$

The demonstration measures $3.4640$ against $3.4641$ for a point source and
$1.5328$ against $1.5328$ for a dipole of length $1$ m at $100$ m depth — the
agreement is limited only by the sampling of the profile, and it validates the
image-method code end to end.

The practical use is the *ratio*: a measured width of $244$ m for the model with
a $20$ m long dipole at $160$ m depth gives $1.525$ (the table's last row),
against the asymptotic $1.5328$ — so the source geometry, not only its depth,
enters the constant, and a depth derived from a width carries that model
dependence.

### 3.6 What one profile can and cannot determine

The demonstration fits the three-parameter family (depth, length, current) to a
synthetic profile with $41$ stations over $400$ m and $2.1\%$ noise. The best fit
recovers the depth exactly and the length and current to within $10\%$, but the
admitted set ($\chi^{2} \le \chi^{2}_{\min} + 4$) is

| parameter | admitted range |
|---|---|
| depth | $[38.0,\ 44.0]$ m |
| length | $[4.0,\ 36.0]$ m |
| correlation between the two | $+0.854$ |

The admitted set is a **ridge**, not a point: a deeper, longer body with a larger
current reproduces the same profile. This is the same structure as the
depth–velocity trade-off in seismology and the depth–contrast trade-off in
potential-field methods; it is a property of the physics, not of the fitting
code, and the honest report is the ridge with its correlation.

## 4. Physical interpretation

- **A surface SP map is a picture of currents, not of minerals.** The same
  current distribution can arise from a chemical cell, a flowing fluid or a
  temperature gradient. Discriminating them requires additional information:
  the shape of the anomaly, its correlation with topography or hydrology, and
  the conductivity structure from an independent survey.
- **Scale is set by conductivity, twice.** The streaming coefficient carries
  $1/\sigma$ and the potential of any source carries another $1/\sigma$, so an
  anomaly amplitude is inversely proportional to conductivity squared. This is
  why an SP survey is most sensitive in resistive ground.
- **Signs are diagnostic.** With $\zeta < 0$ the potential *increases* in the
  direction of flow, so a positive anomaly downslope of a recharge area and a
  negative anomaly at the outflow are the classical pattern for seepage. A redox
  cell's sign follows the polarity of the dominant half-reaction.
- **The two mechanisms have different frequency content in principle, but SP
  measurements are DC.** They are separated by their *geometry* and their
  *chemistry*, not by frequency; this is why they are so often ambiguous.

## 5. Assumptions and regime of validity

1. **Steady state.** The measured potential is assumed to be the DC solution of
   $\nabla\cdot\left(\sigma\nabla V\right) = \nabla\cdot \mathbf{j}_s$ with the
   source current density $\mathbf{j}_s$ from one of the mechanisms. Transient
   effects (electrode drift, rainfall events, tidal pumping) are treated as
   noise in [02 SP for Seepage, Dams, Landfills and Mineralisation](02-sp-applications.md).
2. **Thin double layer (Debye-Hückel).** The streaming relation in the form used
   here assumes the Debye length is much smaller than the pore radius, which
   holds for most natural pore fluids but fails in very fresh water.
3. **Homogeneous host conductivity** in every forward model of this lesson. A
   real survey's anomalies are the product of the source *and* the conductivity
   distribution, and the two cannot be separated from SP alone.
4. **An insulating surface** ($\partial V/\partial z = 0$ at $z=0$). The image
   method relies on it; a conductive surface layer changes the profile.
5. **Locally uniform field** nowhere in this lesson — that assumption appears in
   [03 Mise-à-la-Masse and Induced Polarisation Mapping](03-mise-a-la-masse.md),
   where its limits are measured.
6. **Point or dipole sources.** Real sources are distributed; Section 3.6
   quantifies what that costs when a distributed source is fitted by a dipole.
7. **The reference electrode is stable.** Everything below assumes the
   measurement errors are random; a drifting reference is a systematic error with
   a spatial signature, and it is treated explicitly in lesson 02.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| permittivity | $\varepsilon = \varepsilon_r\varepsilon_0$ | F/m | $\varepsilon_0 = 8.8541878128\times10^{-12}$ F/m |
| zeta potential | $\zeta$ | V | |
| viscosity | $\eta$ | Pa s | |
| conductivity | $\sigma$ | S/m | |
| coupling coefficient | $\partial V/\partial P$ | V/Pa | $\mathrm{F\,V\,m^{-1}/(Pa\,s\,S\,m^{-1})} = \mathrm{V\,Pa^{-1}}$ |
| pressure | $P$ | Pa | $\rho_w g h$, $\rho_w$ in kg/m³, $g$ in m/s² |
| Nernst slope | $RT/F$ | V | $\mathrm{J\,mol^{-1}}/\mathrm{C\,mol^{-1}} = \mathrm{J/C} = \mathrm{V}$ |
| current | $I$ | A | |
| potential | $V$ | V | $\rho I/r$: $\Omega\,\mathrm{m}\cdot\mathrm{A}/\mathrm{m} = \Omega\,\mathrm{A} = \mathrm{V}$ |

A useful sanity check on the coupling coefficient: with
$\varepsilon\sim10^{-9}$ F/m, $\zeta\sim0.02$ V, $\eta\sim10^{-3}$ Pa s and
$\sigma\sim10^{-2}$ S/m, the coefficient is
$\sim10^{-6}$ V/Pa, i.e. of order 1 mV per metre of head. If a computation gives
$\sim1$ V/Pa, a factor of $10^{3}$ has been lost between S/m and mS/m.

## 7. Worked examples

### Example 1 — the head behind a 10 mV anomaly

Take $\sigma = 0.010$ S/m. From the measured table,
$\partial V/\partial h = -13.910$ mV per metre of head. For a $10.0$ mV anomaly:

$$h = \frac{10.0\ \mathrm{mV}}{13.910\ \mathrm{mV\,m^{-1}}} = 0.719\ \mathrm{m}.$$

Check directly: $1$ m of head is
$\rho_w g = 1000 \times 9.80665 = 9806.6$ Pa; the coefficient is
$-1.418441\times10^{-6}$ V/Pa; so
$\partial V/\partial h = -1.418441\times10^{-6} \times 9806.6 = -1.3910\times10^{-2}$
V per metre $= -13.910$ mV per metre ✓, and
$10.0/13.910 = 0.719$ m ✓ — the demonstration's printed value.

### Example 2 — a depth from a measured width

A synthetic profile has a full width at half maximum of $56.0$ m. Which depths
does that admit?

- If the source is a point dipole ($L \ll h$):
  $h = 56.0/1.5328 = 36.5$ m.
- If it is a point source: $h = 56.0/3.4641 = 16.2$ m.

The demonstration's table shows the actual model — a $20$ m long dipole at
$40$ m — gives FWHM $= 56.0$ m, i.e. a ratio of $1.400$, between the two
asymptotes. So the width alone converts to a depth only once the source
*geometry* is assumed, and the two assumptions differ by a factor $2.26$:
$36.5$ against $16.2$ m for the same measurement. This is the cleanest available
illustration of why SP depths are model-dependent.

### Example 3 — a redox cell and its surface expression

A synthetic body in which $\mathrm{Fe^{3+}/Fe^{2+}}$ is oxidised at one end and
$\mathrm{O_2/H_2O}$ is reduced at the other forms a cell with
$E^{0} = 1.229 - 0.771 = +0.458$ V. Suppose the conducting path and the ground
impose a total resistance such that only a fraction of that potential appears
across the ground: the SP anomaly is the $IR$ drop in the ground, not the cell
potential. With a body-to-ground current of $I = 0.05$ A in a half-space of
$\sigma = 0.01$ S/m, the surface potential above an electrode-like end is

$$V = \frac{\rho I}{2\pi h} = \frac{100 \times 0.05}{2\pi \times 40}
= 0.0199\ \mathrm{V} = 19.9\ \mathrm{mV}$$

at $h = 40$ m if the end behaves as a point electrode. That is the right order
for an SP anomaly, and it is two orders of magnitude below the cell potential:
**the cell potential is not the anomaly.** The distinguishing measurement is the
*surface pattern*: one compact electrode-like end gives a single lobe with
$\mathrm{FWHM} = 3.464\,h = 138.6$ m, while a dipole with two ends gives the
narrower, $1.533\,h$ pattern of Example 2.

## 8. Python demonstration

`code/self_potential_sources_demo.py` prints every number in this lesson. It:

1. tabulates the Helmholtz-Smoluchowski coefficient over four decades of
   conductivity, in V/Pa, in mV per metre of head, and as the head needed for a
   $10$ mV anomaly;
2. computes Nernst cells from five standard reduction potentials, including the
   concentration sensitivity (59.159 mV per decade);
3. tabulates the membrane potential against the cation transference number;
4. solves the buried-point-electrode and buried-dipole forward models by the
   image method, verifies the half-space potential against
   $\rho I/(2\pi r)$, and checks the two width rules against their exact values
   ($3.4640$ vs $3.4641$ and $1.5328$ vs $1.5328$);
5. fits the three-parameter dipole family to a noisy synthetic profile with a
   grid search and reports the admitted ranges and their correlation
   ($+0.854$).

Run it with the project virtual environment:

```bash
cd 09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python self_potential_sources_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-self-potential-sources-exercises.md`](./exercises/01-self-potential-sources-exercises.md)
and
[`exercises/01-self-potential-sources-solutions.md`](./exercises/01-self-potential-sources-solutions.md).

- **★** Compute $\partial V/\partial P$ for $\sigma = 0.02$ S/m with
  $\zeta = -25$ mV and the same $\varepsilon$, $\eta$; then the head needed for
  a $5$ mV anomaly.
- **★** Compute the Nernst potential of a $\mathrm{Cu^{2+}/Cu}$ cathode against a
  $\mathrm{Zn^{2+}/Zn}$ anode and state the sign convention.
- **★★** Derive $\mathrm{FWHM} = 2\sqrt{2^{2/3}-1}\,h$ for a point dipole from
  $V \propto h/(x^{2}+h^{2})^{3/2}$.
- **★★** A profile of width $120$ m is interpreted first as a point source and
  then as a point dipole; compute both depths and the ratio, and state which
  additional measurement would discriminate.
- **★★★** Design a survey that separates a streaming-potential source from a
  redox source with the same anomaly amplitude: state the measurements, the
  predictions of each mechanism, and the statistic that decides.

## 10. Common mistakes

1. **Reporting an absolute SP value.** SP is measured between two electrodes and
   is only meaningful relative to a stated reference or to a levelled profile.
2. **Assuming a coupling coefficient.** It carries $1/\sigma$ and a zeta
   potential that depends on the fluid chemistry; two orders of magnitude
   variation across a survey area is routine.
3. **Converting a width to a depth without stating the source geometry.** The
   same $56.0$ m width gives $36.5$ or $16.2$ m depending on that choice.
4. **Quoting a single depth from a fitted profile.** The admitted set is a ridge;
   Section 3.6 measures its correlation at $+0.854$.
5. **Attributing every anomaly to a mineral body.** With $\zeta < 0$ a hill
   with infiltration produces the same sign of anomaly as an oxidising body.
6. **Forgetting that the cell potential is not the anomaly.** The anomaly is an
   $IR$ drop in the ground, typically tens of millivolts against cell potentials
   of volts.

## 11. Real-world applications

- **Seepage and dam safety.** Streaming potentials map preferential flow paths
  and leakage through embankments; the $1/\sigma$ dependence explains why the
  method works in resistive fills and struggles in saline foundations.
- **Mineral exploration.** Sulphide bodies self-potentialise through redox
  reactions; the classical compact anomaly with a single lobe over the body and
  a bipolar pattern around elongated bodies is the historical core of the method.
- **Geothermal and volcanic systems.** Electrokinetic SP responds to
  hydrothermal upflow and to the movement of fluids near magmatic bodies.
- **Environmental and hydrological work.** SP has been used to locate
  contaminant plumes through redox contrast and to monitor infiltration fronts,
  where the anomaly follows the front in time.

## 12. Further reading

- **Revil, A., & Jardani, A., *The Self-Potential Method: Theory and
  Applications in Environmental Geosciences* (Cambridge University Press).**
  Level: research monograph. The standard modern reference, with the
  electrokinetic derivation used here.
- **Telford, W. M., Geldart, L. P., & Sheriff, R. E., *Applied Geophysics*
  (2nd ed., Cambridge University Press).** Level: textbook. The classical
  treatment of the method and of the SP anomaly shapes.
- **Reynolds, J. M., *An Introduction to Applied and Environmental
  Geophysics* (2nd ed., Wiley-Blackwell).** Level: textbook. Field procedure
  and the practical problems of non-polarisable electrodes and drift.
- **Sato, M., & Mooney, H. M., "The electrochemical mechanism of sulfide
  self-potentials", *Geophysics* 25 (1960).** Level: research. The classical
  electrochemical interpretation of mineral SP anomalies.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. **No number in this lesson is
> quoted from any of them.** Every figure comes from
> [`code/self_potential_sources_demo.py`](./code/self_potential_sources_demo.py) or is a standard
> constant with its units stated (the constants in Section 2 and the standard
> reduction potentials in Section 3.2).

## 13. Related lessons

- [02 SP for Seepage, Dams, Landfills and Mineralisation](02-sp-applications.md) —
  what the sources look like in a survey, and how noise and drift limit them.
- [03 Mise-à-la-Masse and Induced Polarisation Mapping](03-mise-a-la-masse.md) —
  the same potential theory with an injected current.
- [09-03-03 IP Acquisition, Chargeability and Phase Units](../03-induced-polarisation/03-ip-acquisition.md) —
  the electrode and noise environment shared with SP.
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](../01-electrical-properties-of-earth/04-clay-and-surface-conduction.md) —
  the surface chemistry behind the membrane potential of Section 3.3.
- [02-07-01 Electrostatics, Coulomb's Law and Electric Potential](../../02-physics/07-electromagnetism/01-electrostatics.md) —
  the potential theory used throughout.

## 14. Self-assessment checklist

- [ ] I can write and use the Helmholtz-Smoluchowski coupling coefficient.
- [ ] I can convert a head difference into an SP anomaly, in the right units.
- [ ] I can compute a Nernst cell potential and its concentration sensitivity.
- [ ] I can derive the membrane potential and say which medium is cation
      selective.
- [ ] I can derive the half-space potential of a buried electrode by the image
      method.
- [ ] I can derive and check both width rules.
- [ ] I can state why a profile gives a ridge of depths and lengths, and quote a
      measured correlation.
