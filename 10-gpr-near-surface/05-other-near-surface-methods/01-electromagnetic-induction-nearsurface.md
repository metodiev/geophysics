---
id: 10-05-01
title: "EM Induction (EMI) and Conductivity Meters"
level: advanced
prereqs: ["05-01-01", "05-02-02", "08-04-01", "09-01-01"]
tags: [near-surface, electromagnetics, emi, conductivity, induction-number]
---

# EM Induction (EMI) and Conductivity Meters

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** from Faraday's law and Ohm's law why, in the low-induction-number
   (LIN) limit, the secondary field of a small-loop conductivity meter is in
   **quadrature** with the primary field and **linear** in the ground
   conductivity.
2. **Define** the skin depth $\delta$, the induction number $B = s/\delta$, and
   **state** the regime in which the linear reading is defensible.
3. **Derive** the LIN depth weighting $w(z)$ of a coil pair from the reciprocity
   relation, and explain why the reading is a *weighted depth average* of
   conductivity rather than a conductivity.
4. **Compute** the apparent conductivity of a layered ground from the layer
   weights, and **verify** the additive rule against a hand calculation.
5. **Quantify** the non-uniqueness of a single reading: construct two different
   layered grounds that give the same reading, and show how much a second
   spacing separates them.
6. **State** the assumptions (LIN, quasi-static, $\mu = \mu_0$, horizontal
   layering, no cultural conductors) and the error each one introduces when it
   fails.

## Prerequisites

- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md) —
  what a method measures and why a contrast is needed.
- [05-02-02 Units of Field Measurements](../../05-core-geophysics/02-geophysical-fields-and-observables/02-field-measurement-units.md) —
  SI units for magnetic fields and conductivities.
- [08-04-01 EM Induction Basics](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/01-em-induction-basics.md) —
  eddy currents, the diffusion equation and the skin depth.
- [09-01-01 Resistivity and Conductivity of Earth Materials](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  what makes a soil conductive, and the range of values.

## 1. Intuition: a reading that is an average, not a value

A conductivity meter is a pair of coils holding a fixed separation $s$. One coil
carries an alternating current and radiates a magnetic field into the ground.
Because the field is changing, Faraday's law drives **eddy currents** in any
conducting material beneath the coils. Those currents radiate a magnetic field of
their own — the **secondary field** — which the second coil measures on top of
the primary field it would see in air.

The instantaneous reading is therefore two numbers, not one: the part of the
secondary field in phase with the primary (the **in-phase** component) and the
part a quarter-cycle behind it (the **quadrature** component). Instruments
convert the quadrature component into an **apparent conductivity** $\sigma_a$ and
display it in millisiemens per metre.

The central honest difficulty of the method follows from a single question: *the
eddy currents fill the whole ground, so what part of the ground does the reading
represent?* The answer is that a reading is a **weighted depth average** of
conductivity, and the weights depend on the coil separation, the coil size and
the frequency. Change the spacing and you change the weights — and, in a layered
ground, the number on the display. A conductivity meter does not measure
conductivity. It measures a convolution of conductivity with a weighting
function, and this lesson derives that weighting and quantifies what it costs.

The method's practical reach comes from the same physics: it needs no electrodes,
no galvanic contact, and can be towed or carried at walking pace. That makes it
the standard first-look tool for soil salinity, landfill cover integrity, buried
metal, and moisture in embankments — the subjects of
[05 Multi-Method Integration](05-multi-method-nearsurface.md) and
[06-02 Monitoring Dams, Embankments and Foundations](../06-nearsurface-monitoring/02-geotechnical-monitoring.md).

> All models and data in this module are **SYNTHETIC**. The coil radius, spacings,
> frequencies and conductivities used below are chosen teaching values. They are
> not instrument specifications and not field measurements, and no site is
> modelled.

## 2. Precise definitions

**Conductivity and resistivity.** Electrical conductivity $\sigma$ is the
reciprocal of resistivity $\rho$, so $\sigma = 1/\rho$; the SI unit is the siemens
per metre ($\mathrm{S\,m^{-1}}$). Soil conductivity spans several orders of
magnitude and is controlled mainly by water content, pore-water salinity and clay
content. The teaching values used throughout this lesson are $10$, $30$, $100$ and
$1000\ \mathrm{mS\,m^{-1}}$, all printed by the demonstration; they are chosen to
span the range a meter meets between a dry sand and a saline clay, not quoted from
any survey.

**Quasi-static regime.** The displacement current is negligible when
$\omega\varepsilon \ll \sigma$. Near-surface EMI instruments operate in the
kilohertz band — the teaching frequencies here are $9.8$ and
$24.5\ \mathrm{kHz}$ — where the inequality holds comfortably for the soil
conductivities above, so the ground obeys the magnetic **diffusion** equation,
not the wave equation. This is one of the sharpest contrasts with GPR
([01-01 GPR Physics](../01-gpr-principles/01-gpr-physics.md)), which works in the
wave regime at frequencies three to four orders of magnitude higher.

**Skin depth.** For a harmonic field in a uniform conductor,

$$\delta = \sqrt{\frac{2}{\omega \mu_0 \sigma}}
\qquad (\mathrm{m}), \qquad \omega = 2\pi f ,$$

the depth over which the amplitude falls by $1/e$. It is an *exact* solution of
the diffusion equation for a uniform half-space driven by a uniform tangential
field. Note the two consequences: $\delta$ falls as $1/\sqrt{f}$ and as
$1/\sqrt{\sigma}$, so a more conductive or higher-frequency measurement reaches
less far.

**Induction number.** The dimensionless ratio

$$B \equiv \frac{s}{\delta} = s\sqrt{\frac{\omega\mu_0\sigma}{2}}$$

compares the coil separation to the skin depth. **The low-induction-number (LIN)
approximation assumes $B \ll 1$**, meaning that the secondary field is weak
compared with the primary and that the eddy currents are driven by the primary
field alone. This is exactly the first Born approximation, and it is what makes
the response linear in $\sigma$.

**Primary and secondary field.** Write $\mathbf H = \mathbf H_p + \mathbf H_s$.
$\mathbf H_p$ is the free-space field of the transmitter loop; $\mathbf H_s$ is
everything the ground adds. A conductivity meter's *voltage ratio* output is the
complex dimensionless quantity

$$Q \equiv \frac{H_s}{H_p}\bigg|_{\text{receiver}}.$$

**Apparent conductivity.** $\sigma_a$ is defined operationally, by calibration:
the instrument is scaled so that over a homogeneous reference half-space of
conductivity $\sigma$ it reads $\sigma_a = \sigma$. Everything in this lesson
follows from that definition and from the LIN linearity; no absolute calibration
constant is needed.

## 3. Derivations

### 3.1 Why the LIN response is quadrature and linear in $\sigma$

Work in the quasi-static limit, so that a loop current $I e^{-i\omega t}$ produces
a magnetic dipole field and the magnetic vector potential

$$\mathbf A = -\,\frac{\mu_0}{4\pi}\,\mathbf m \times \nabla\frac{1}{R},
\qquad \mathbf m = N A_{\text{loop}} I \, \hat{\mathbf n},$$

where $R$ is the distance from the loop centre and $\mathbf m$ the dipole moment.
The electric field in the ground is $\mathbf E_p = i\omega \mathbf A$ (from
$\mathbf E = -\partial \mathbf A/\partial t$ in the quasi-static limit), so

$$|\mathbf E_p| \propto \omega \mu_0\,|\mathbf m|\,\frac{\rho}{R^3},$$

with $\rho$ the horizontal distance from the loop axis. Ohm's law then gives the
eddy current density

$$\mathbf J = \sigma \mathbf E_p \ \propto \ i\,\omega\mu_0\sigma \ \times\ (\text{geometry}),$$

and the secondary field at the receiver is the Biot–Savart integral of $\mathbf
J$ over the ground:

$$\mathbf H_s = \frac{1}{4\pi}\int_V \frac{\mathbf J \times \hat{\mathbf R}}{R^{2}}\,dV
\ \propto\ i\,\omega\mu_0\sigma .$$

Two things are now visible, and they are the whole basis of the method:

1. **The factor $i$.** $H_s$ is $90^\circ$ out of phase with $H_p$, so the LIN
   response lives entirely in the **quadrature** channel. A non-zero *in-phase*
   reading is therefore evidence of something outside the LIN model: a ferrous or
   highly conductive target, or a high induction number.
2. **The linear factor $\sigma$.** At LIN the current density is proportional to
   the ground conductivity, so a layered ground gives the sum of the
   contributions of its layers, each weighted by its own conductivity.

Linearity is what allows a *superposition rule* rather than a full inversion —
and it is also what makes the interpretation non-unique, because a linear
functional of a profile cannot determine the profile.

### 3.2 The depth weighting from reciprocity

Attach currents $I_1$ and $I_2$ to the two coils. The reciprocity theorem for a
conducting body in the LIN limit states that the *anomalous mutual impedance*
(the part produced by the ground) is

$$Z_s = \frac{1}{I_1I_2}\int_V \sigma\,\mathbf E_1\cdot\mathbf E_2\; dV ,$$

where $\mathbf E_1$ and $\mathbf E_2$ are the electric fields that coil 1 and
coil 2 would each produce *alone* at that point of the volume. This is the
standard small-perturbation (Born) form of reciprocity: the ground acts as a
volume of sources whose strength is $\sigma\mathbf E_1$ driven by the primary
field of the transmitter, and it is sampled by the primary field of the
receiver.

For a horizontally layered ground $\sigma = \sigma(z)$, and with
$\mathbf E = i\omega\mathbf A$, the integral factors into a depth integral and a
planar integral. Define the **per-depth weight**

$$w(z) = \iint_{\text{plane at depth } z} \mathbf A_1(\mathbf x,z)\cdot
\mathbf A_2(\mathbf x,z)\; dA .$$

Then the anomalous coupling is

$$Z_s \propto -\omega^2\int_0^\infty \sigma(z)\,w(z)\,dz ,$$

and, since the instrument is calibrated so that a homogeneous ground returns its
own conductivity, the reading is the normalised average

$$\boxed{\ \sigma_a = \frac{\displaystyle\int_0^\infty \sigma(z)\,w(z)\,dz}
{\displaystyle\int_0^\infty w(z)\,dz}
= \sum_i \sigma_i W_i ,\qquad
W_i = \frac{\int_{z_i}^{z_{i+1}} w\,dz}{\int_0^\infty w\,dz}\ }$$

with $\sum_i W_i = 1$. **This is the central result of the lesson**: an apparent
conductivity is a weighted mean of the true conductivity profile, and the weights
$W_i$ are what a two-layer equivalence problem trades against each other.

For a circular loop of radius $a$ carrying current $I$ in the horizontal coplanar
(HCP) mode, the vector potential at horizontal distance $\rho$ and depth $z$ is

$$A_\phi(\rho,z) = \frac{\mu_0 I}{\pi k}\sqrt{\frac{a}{\rho}}
\left[\left(1 - \frac{k^2}{2}\right)K(k) - E(k)\right],
\qquad k^2 = \frac{4a\rho}{(a+\rho)^2 + z^2},$$

where $K$ and $E$ are the complete elliptic integrals of the first and second
kind. Both coils are modelled as finite loops of the same radius $a$, and the
geometric factor in the planar integral is $\hat{\boldsymbol\phi}_1\cdot
\hat{\boldsymbol\phi}_2 = (\rho_1^2 - x s)/(\rho_1\rho_2)$.

Two remarks matter physically.

- **The finite loop radius is essential.** With a point-dipole idealisation the
  planar integral diverges logarithmically as $z \to 0$, because the model puts an
  infinite field gradient at the coil centre. A real instrument has finite coils,
  the weight peaks near $z \approx a$, and — as the demonstration measures — it is
  *weakly negative* in the topmost centimetres for the larger spacing ($-12\%$ of
  the peak magnitude at $z = 2\ \mathrm{mm}$ for $s = 2.50\ \mathrm{m}$). The
  weight is a sensitivity, not a probability density, and it is not
  sign-definite.
- **Normalisation is the calibration.** Because $\sum_i W_i = 1$, the rule
  reproduces $\sigma_a = \sigma$ for any homogeneous ground, which is exactly the
  calibration convention of Section 2. No absolute scale factor enters the
  interpretation.

### 3.3 What a weight vector can and cannot resolve

A layered ground has a conductivity profile; a reading returns one number. Even in
the ideal LIN world, a profile with $n$ layers needs $n$ measurements. The
information available is the set of weight vectors $\{W^{(j)}\}$ — one for each
spacing/frequency combination $j$ — because a different spacing is a different
weighting (Section 4 measures this), not merely a different sensitivity.

For a two-layer ground described by contrast $\Delta\sigma = \sigma_1 - \sigma_2$
and interface depth $h$, two spacings give

$$\begin{pmatrix} W_1^{(1)} & W_2^{(1)} \\ W_1^{(2)} & W_2^{(2)} \end{pmatrix}
\begin{pmatrix} \sigma_1 \\ \sigma_2 \end{pmatrix}
= \begin{pmatrix} \sigma_a^{(1)} \\ \sigma_a^{(2)} \end{pmatrix},$$

solvable only insofar as the two weight vectors are *different*. Their
difference is a number, not a qualitative property, and Section 3.4 shows what it
buys. Where the weight vectors are nearly parallel the system is ill-conditioned
and a small reading error becomes a large layer-conductivity error; this is the
same rank-deficiency that
[18 Inverse Problems](../../18-inverse-problems/README.md) treats systematically.

### 3.4 Equivalence: the conductance–depth trade-off

Complete a two-layer model with the half-space conductivity $\sigma_{\text{hs}}$.
Because $\sum_i W_i = 1$, the rule simplifies to a sum over *contrasts*:

$$\sigma_a = \sigma_{\text{hs}} + \sum_i (\sigma_i - \sigma_{\text{hs}})\,W_i .$$

A conductive layer of thickness $t$ and conductivity $\sigma_1$ therefore
contributes $(\sigma_1 - \sigma_{\text{hs}}) W_1$, and its **layer conductance**
$\sigma_1 t$ does not appear alone: only the product of the contrast with the
weight does. Doubling the thickness and halving the contrast can be arranged to
leave one reading unchanged, while changing the weight of the layer (a second
spacing) changes it. That is the entire basis of multi-spacing sounding, and
Section 5 solves such a pair exactly with the measured weights.

## 4. Physical interpretation

**Shape of the weight.** For the teaching parameters of the demonstration
($a = 0.25\ \mathrm{m}$, $s = 1.00\ \mathrm{m}$) the measured cumulative
weight reaches 10% of the response above $0.21\ \mathrm{m}$, 50% above
$0.71\ \mathrm{m}$ and 90% above $2.47\ \mathrm{m}$. The reading is therefore
dominated by the first metre, and about a fifth of it comes from below
$1.5\ \mathrm{m}$. For $s = 2.50\ \mathrm{m}$ the same fractions are reached at
$0.54$, $1.56$ and $4.16\ \mathrm{m}$: **a larger spacing senses deeper**. A
useful convention is to quote the *depth containing half the weight* and to give
it in units of the spacing, because it shows how much of the physics is set by
geometry alone: $0.71\,s$ at $s = 1.00\ \mathrm{m}$ and $0.62\,s$ at
$s = 2.50\ \mathrm{m}$ in this model — close to, but not equal to, a constant,
because the coil radius $a$ does not scale with $s$.

**Layered contributions are not additive in conductivity.** The rule
$\sigma_a = \sigma_{\text{hs}} + \sum(\sigma_i-\sigma_{\text{hs}})W_i$ is written
against a chosen reference. Changing the reference changes the individual terms
but not the sum; when reading a published "layer contribution" table, check which
reference was used.

**Both channels carry information, but not the same information.** The quadrature
channel is the one calibrated into a conductivity. The in-phase channel responds
only to the *induction number*: it vanishes at LIN and grows as a higher-order
term in $B$, so it is sensitive to the product $\omega\mu_0\sigma s^2$ without
distinguishing the factors. That is why in-phase and quadrature together are used
to detect metal, whose $\mu \ne \mu_0$ and high $\sigma$ give a signature that a
conductive soil cannot imitate.

**Where the nonlinear terms appear.** The LIN response is exact only at $B \to 0$.
At finite $B$ the currents in different parts of the ground are no longer in phase
with one another: the induced currents have their own skin effect, and the reading
becomes a nonlinear functional of $\sigma$. The demonstration tabulates $B$ for
teaching soils: for $\sigma = 30\ \mathrm{mS\,m^{-1}}$ at
$9.8\ \mathrm{kHz}$, $B = 0.034$ and $0.085$ for the two spacings, comfortably
inside the linear regime, whereas for a saline ground
($\sigma = 1\ \mathrm{S\,m^{-1}}$) at $24.5\ \mathrm{kHz}$, $B = 0.31$ and $0.78$,
where the linear interpretation is no longer safe.

## 5. Worked examples

### Example 1 — is the linear reading defensible?

Take $f = 24.5\ \mathrm{kHz}$, $\sigma = 0.100\ \mathrm{S\,m^{-1}}$,
$s = 2.50\ \mathrm{m}$.

$$\omega = 2\pi f = 1.5394\times10^{5}\ \mathrm{rad\,s^{-1}},$$
$$\omega\mu_0\sigma = 1.5394\times10^{5}\times1.2566\times10^{-6}\times0.100
= 1.9345\times10^{-2}\ \mathrm{m^{-2}},$$
$$\delta = \sqrt{2/1.9345\times10^{-2}} = \sqrt{103.39} = 10.17\ \mathrm{m},$$
$$B = s/\delta = 2.50/10.17 = 0.246 .$$

$B = 0.25$ is a quarter of unity. The LIN interpretation is acceptable but no
longer negligible; the demonstration reports the same $0.246$ to three decimals.
At the same frequency but a saline ground ($\sigma = 1.000\ \mathrm{S\,m^{-1}}$)
the skin depth is $3.22\ \mathrm{m}$ and $B = 0.78$.

### Example 2 — apparent conductivity of a buried conductive lens

A $1\ \mathrm{m}$ thick lens of $200\ \mathrm{mS\,m^{-1}}$ sits between $1$ and
$2\ \mathrm{m}$ in a host of $20\ \mathrm{mS\,m^{-1}}$. The measured layer weight
of the $1.0$–$2.0\ \mathrm{m}$ interval is $W_1 = 0.2171$ at
$s = 1.00\ \mathrm{m}$ (demonstration, Section 4c). Then

$$\sigma_a = \sigma_{\text{hs}} + (\sigma_1 - \sigma_{\text{hs}})W_1
= 20 + (200-20)\times0.2171 = 20 + 39.1 = 59.1\ \mathrm{mS\,m^{-1}},$$

which agrees with the value $59.08\ \mathrm{mS\,m^{-1}}$ printed by the
demonstration. Note what has been *lost*. The lens is ten times the host
conductivity, yet the reading rises only from $20$ to $59\ \mathrm{mS\,m^{-1}}$:
the recovered contrast is $39.1$ of the true $180\ \mathrm{mS\,m^{-1}}$, i.e.
$21.7\%$ — exactly the layer weight $W_1$, as the rule demands. The missing
response is not lost by accident; it is charged to the host, which is why an
inversion of a single reading returns a *smoothed* profile. Moving the same lens
to $3$–$4\ \mathrm{m}$ depth lowers $W_1$ to $0.0326$ and the reading to
$25.9\ \mathrm{mS\,m^{-1}}$, only $29\%$ above the host.

### Example 3 — two grounds, one reading

Let the host be $20\ \mathrm{mS\,m^{-1}}$, model A be $0.50\ \mathrm{m}$ of
$100\ \mathrm{mS\,m^{-1}}$, and model B be $1.50\ \mathrm{m}$ of unknown
conductivity. From the demonstration, $W_A = 0.3501$ for the $0$–$0.50\ \mathrm{m}$
interval and $W_B = 0.7806$ for the $0$–$1.50\ \mathrm{m}$ interval, both at
$s = 1.00\ \mathrm{m}$.

Model A reads $\sigma_a = 20 + (100-20)\times0.3501 = 20 + 28.01
= 48.0\ \mathrm{mS\,m^{-1}}$.

Model B reproduces the reading if

$$20 + (\sigma_B - 20)\times0.7806 = 48.01
\quad\Longrightarrow\quad
\sigma_B - 20 = \frac{28.01}{0.7806} = 35.88
\quad\Longrightarrow\quad \sigma_B = 55.9\ \mathrm{mS\,m^{-1}} .$$

Two grounds differing by a factor of three in layer thickness and by
$-44\%$ in layer conductivity give the **same** reading. They are not
equivalent, however, at the larger spacing, where the layer weights are
$0.0845$ and $0.4811$:

$$\sigma_a^{A}(2.50) = 20 + 80\times0.0845 = 26.8\ \mathrm{mS\,m^{-1}},$$
$$\sigma_a^{B}(2.50) = 20 + 35.88\times0.4811 = 37.3\ \mathrm{mS\,m^{-1}},$$

a difference of $+39\%$. **One reading cannot separate them; two can.** The
demonstration prints $48.00$, $26.76$, $55.88$ and $37.26\ \mathrm{mS\,m^{-1}}$
for these four quantities.

## 6. Assumptions and regime of validity

1. **Low induction number, $B \ll 1$.** The response is linear in $\sigma$ and
   the quadrature channel dominates. Quantified in Section 4; violated by saline
   ground, high frequency or large spacing, in which case the reading
   under-reports high conductivities in a way that depends on the profile.
2. **Quasi-static (diffusion) physics.** $\omega\varepsilon \ll \sigma$; true for
   near-surface soils below ~1 MHz. Where it fails the measurement becomes a
   radar measurement (see [01 GPR Physics](../01-gpr-principles/01-gpr-physics.md)).
3. **Non-magnetic ground, $\mu = \mu_0$.** Ferrous objects (pipes, reinforcement,
   ordnance) change $\mu$ as well as $\sigma$ and are detected through the
   in-phase channel; they are not interpretable as conductivity.
4. **Horizontal layering.** The weight derivation assumes $\sigma = \sigma(z)$.
   Lateral contrasts inside the footprint are averaged, not located: a small
   strong anomaly and a large weak one can give the same reading, exactly as in
   every potential-field measurement
   ([05-01-04 Ambiguity and Non-uniqueness](../../05-core-geophysics/01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)).
5. **No above-ground coupling.** Cable loops, fences, vehicles and the operator
   are inside the coil footprint for the near-surface weighting and can dominate
   the reading.
6. **Idealised dipoles and known geometry.** The weights assume the coil axes are
   vertical, coplanar and exactly separated by $s$. Tilting or raising the
   instrument changes the coupling and therefore the effective weights; the
   practical defence is to keep both coils parallel to the ground and at the same
   height, and to repeat a line in both directions as a geometry check.
7. **No polarisation or dispersion of $\sigma$.** Frequency-dependent
   conductivity (the induced-polarisation effect,
   [09-03 IP](../../09-electrical-em-methods/03-induced-polarisation/README.md))
   adds a quadrature-like term that is *not* the eddy-current response; the two
   are separated by measuring several frequencies.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| conductivity | $\sigma$ | $\mathrm{S\,m^{-1}}$ | $= 1/\rho$ |
| permeability | $\mu_0$ | $\mathrm{H\,m^{-1}}$ | exact constant, $1.2566\times10^{-6}$ |
| angular frequency | $\omega$ | $\mathrm{rad\,s^{-1}}$ | $= 2\pi f$ |
| skin depth | $\delta$ | m | $\sqrt{2/(\omega\mu_0\sigma)}$: $\mathrm{s\,H^{-1}\,m}$ = $\mathrm{m^2}$ |
| induction number | $B$ | dimensionless | $s/\delta$ |
| spacing | $s$ | m | |
| vector potential | $A_\phi$ | $\mathrm{T\,m}$ | $= \mathrm{kg\,m\,s^{-2}\,A^{-1}}$ |
| weight | $w(z)$ | $\mathrm{T^2\,m}$ | $\int A_1A_2\,dA$: $\mathrm{T^2m^3/m^2}$ |
| layer weight | $W_i$ | dimensionless | ratio of integrals of $w$ |
| apparent conductivity | $\sigma_a$ | $\mathrm{S\,m^{-1}}$ | $\sum \sigma_i W_i$, $\sum W_i = 1$ |

The dimensional chain to check at every step is
$\sigma \to \omega\mu_0\sigma \to \delta \to B$. Only $B$ is dimensionless, and
only $B$ decides whether the linear interpretation of the meter is safe.

## 8. Python demonstration

`code/em_induction_demo.py` implements the whole chain and prints labelled
results with units. It:

1. tabulates the skin depth and the induction number for teaching soils at two
   frequencies and two spacings;
2. verifies the elliptic-integral vector potential of a loop against the
   defining Neumann line integral, agreeing to $4.8\times10^{-15}$;
3. computes the LIN per-depth weight $w(z)$ for the HCP mode at
   $s = 1.00$ and $2.50\ \mathrm{m}$ by Gauss–Legendre quadrature, checks
   convergence (the 50% depth moves by less than $2\ \mathrm{mm}$ when the
   quadrature is refined from $150\times120$ to $300\times240$ nodes), and prints
   the cumulative weighting;
4. verifies the calibration convention ($\sigma_a = \sigma$ for a homogeneous
   ground, weights summing to $1.000000000000$);
5. builds the two-layer equivalence pair of Example 3 and the lens model of
   Example 2, and prints the readings at both spacings.

The demonstration is print-only, uses the fixed seed
`np.random.default_rng(20261014)`, needs no network, and runs in about six
seconds.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/01-electromagnetic-induction-nearsurface-exercises.md`](./exercises/01-electromagnetic-induction-nearsurface-exercises.md)
and
[`exercises/01-electromagnetic-induction-nearsurface-solutions.md`](./exercises/01-electromagnetic-induction-nearsurface-solutions.md).

- **★** Compute $\delta$ and $B$ for $\sigma = 50\ \mathrm{mS\,m^{-1}}$,
  $f = 9.8\ \mathrm{kHz}$, $s = 1.00\ \mathrm{m}$.
- **★★** Use the measured layer weights to compute $\sigma_a$ for a three-layer
  soil profile, and state which layer dominates.
- **★★** Construct a two-layer model that matches the reading of Example 3 at
  $s = 1.00\ \mathrm{m}$ but differs by more than $20\%$ at
  $s = 2.50\ \mathrm{m}$.
- **★★★** Quantify how a $\pm 0.5\ \mathrm{mS\,m^{-1}}$ reading error propagates
  into the recovered layer conductivity for the two-spacing system of
  Section 3.3, and state the conditioning of the weight matrix.

## Mastery checkpoint
Complete this without notes:

> A meter with $s = 1.00\ \mathrm{m}$ and $a = 0.25\ \mathrm{m}$ reads
> $32.0\ \mathrm{mS\,m^{-1}}$ at $9.8\ \mathrm{kHz}$ over a two-layer ground whose
> half-space is known from a borehole to be $20.0\ \mathrm{mS\,m^{-1}}$.
> **(a)** Compute the skin depth and the induction number, and say whether the
> reading is in the linear regime. **(b)** Explain in one sentence why the reading
> is not the layer conductivity. **(c)** Using the weight of a $0$–$0.5\ \mathrm{m}$
> surface layer given in this lesson, find the layer conductivity that would
> explain the reading. **(d)** Name two *different* profiles that would explain
> the same reading, and state the measurement that would separate them. **(e)**
> State one physical process that would make the answer wrong even if the data
> were perfect.

A worked version of (a)–(c) appears in the exercise solutions.

## Common pitfalls
1. **Reporting $\sigma_a$ as a conductivity.** It is a weighted depth average
   with weights that depend on the coil geometry, and it changes when the spacing
   changes. Always state the spacing and frequency.
2. **Using one spacing for a layered target.** One reading and two unknowns is a
   line, not a point (Example 3). Either add a second spacing or state the
   ambiguity.
3. **Ignoring the induction number.** In saline or clay-rich ground $B$ approaches
   unity and the linear calibration under-reports the conductivity. The check costs
   one square root.
4. **Treating a metal target as conductivity.** Ferrous metal changes $\mu$, and
   the in-phase channel is the diagnostic. A conductivity-only interpretation of a
   steel pipe reading is wrong by orders of magnitude.
5. **Calibrating by the manufacturer's constant instead of a reference site.** The
   definition of $\sigma_a$ is a convention; a site-specific null or reference
   measurement is what makes two surveys comparable.
6. **Forgetting that the coils themselves are in the pattern.** The near-surface
   weight is small only because the coils are finite; raising the instrument or
   laying it on a conductive mat changes the reading.

## Related modules
- [10-01 GPR Principles](../01-gpr-principles/README.md) — the same induction
  physics in the wave regime, where the target is resolved rather than averaged.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md) —
  what changes when a measurement becomes an image.
- [10-03 GPR Applications](../03-gpr-applications/README.md) — near-surface
  targets and how methods are chosen for them.
- [10-05-02 Surface-Wave Methods for Shallow Layers](02-seismic-surface-wave-nearsurface.md) —
  the elastic counterpart of a weighted depth average.
- [10-05-05 Integrating Near-Surface Methods](05-multi-method-nearsurface.md) —
  how a conductivity reading is combined with an elastic or thermal one.
- [09 Electrical and EM Methods](../../09-electrical-em-methods/README.md) —
  galvanic resistivity, induced polarisation and the processing of EM data.
- [08-04 EM Induction in the Earth](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/README.md) —
  the same diffusion equation at crustal and mantle scales.
