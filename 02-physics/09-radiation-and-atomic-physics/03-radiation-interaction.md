---
id: 02-09-03
title: "Interaction of Radiation with Matter (Alpha, Beta, Gamma)"
level: advanced
prereqs: ["02-09-02", "02-07-05", "02-03-10"]
estimated_minutes: 90
tags: [stopping-power, attenuation, shielding, compton, photoelectric, bremsstrahlung]
---

# Interaction of Radiation with Matter (Alpha, Beta, Gamma)

Three particles leave a decaying nucleus, and they interact with matter by three
different mechanisms at three different strengths. An alpha particle from
uranium stops in about 20 µm of rock, or in a sheet of paper. A beta particle
from potassium-40 travels a few millimetres. The 1461 keV gamma from the same
potassium-40 nucleus passes through tens of centimetres of rock and needs
centimetres of lead to be attenuated by a factor of ten. The reason for that
enormous range of behaviour is not the energy of the particles — the gamma is
only a few hundred times more energetic than the alpha — it is the *coupling*:
a charged particle interacts continuously with every electron it passes, while a
photon flies until it happens to hit one.

This lesson builds the three interaction laws and the attenuation law that
follows from them. It is also where this module is most explicit about what can
be computed and what must be looked up. The Compton cross section can be
computed exactly, from quantum electrodynamics at tree level, and the demo
verifies its numerical integral against the closed form to one part in 10¹⁰. The
photoelectric and pair-production cross sections cannot be computed to the
accuracy a shield design needs, and the demo says so and does something more
useful instead: it quantifies how much the required thickness moves when the
tabulated coefficient is uncertain, so that the reader can see which input
carries the risk.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the Bethe stopping-power formula, identify what each factor comes
   from, and explain the $1/\beta^2$ dependence without calculus.
2. **Compute** a stopping power and a CSDA range, state the cutoff below which
   the formula is unphysical, and explain the Bragg peak.
3. **Convert** a range in air into a range in rock using the mass range, and
   explain why that conversion works.
4. **Derive** the Compton wavelength shift from energy and momentum
   conservation, and compute the Compton edge and backscatter energies.
5. **Verify** the Klein–Nishina total cross section by quadrature against the
   closed form and against the Thomson limit.
6. **Derive** the exponential attenuation law from a cross section and a number
   density, and compute a half-value layer.
7. **Explain** the $Z$ and $E$ scaling of the photoelectric, Compton and pair
   production processes, and use the scalings to decide which dominates.
8. **Distinguish** attenuation from energy absorption, and state which one a
   dose calculation needs.
9. **State** which numbers in a shielding calculation are computed, which are
   tabulated, and which are model inputs, and cite the compilation for the
   second kind.

## Prerequisites

- [02-09-02 Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md) —
  which particles a nuclide emits, and with what energy distribution.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../07-electromagnetism/05-em-waves.md)
  — the photon as an electromagnetic field, and the meaning of intensity.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../03-oscillations-and-waves/10-attenuation.md)
  — exponential decay of an amplitude or flux in a medium, which is the same
  mathematics as §4.

## 1. Charged particles: continuous energy loss

A charged particle interacts with matter through the Coulomb field of every
electron it passes. Each encounter transfers a little energy, and a single
particle makes of order $10^4$ to $10^6$ such encounters before stopping. The
result is a *continuous* slowing down, and the mean energy lost per unit path
length is the **stopping power** $-\mathrm{d}E/\mathrm{d}x$.

**Where the formula comes from.** In the impulse approximation, a fast particle
of charge $ze$ and speed $v$ passes an electron at impact parameter $b$ and
transfers a momentum of order $ze^2/(4\pi\varepsilon_0 b v)$. Squaring gives an
energy transfer $\Delta E \propto z^2/(b^2v^2)$. Integrating over the electrons in
an annulus of area $2\pi b\,\mathrm{d}b$ with number density $n_e = N_A\rho Z/A$
diverges at both ends, and the divergences are cut off physically: at large $b$
by the binding of the electron, at small $b$ by the kinematics of the collision.
The logarithm that survives is the **stopping number**. In SI-consistent form
the **Bethe formula** is

$$-\frac{\mathrm{d}E}{\mathrm{d}x} = 4\pi N_A r_e^2 m_ec^2\frac{Z}{A}\rho
\frac{z^2}{\beta^2}\left[\ln\left(\frac{2m_ec^2\beta^2\gamma^2}{I}\right)
- \beta^2\right], \tag{1}$$

where $r_e$ is the classical electron radius, $\beta = v/c$, $\gamma$ the
Lorentz factor, and $I$ the **mean excitation energy** of the medium — a
TABULATED quantity of order 10 eV per unit $Z$ (about 85.7 eV for air, from the
ICRU stopping-power tables). Three features of (1) are worth reading out:

- The $z^2$ factor makes stopping power a charge-squared property. A doubly
  charged alpha deposits four times the energy per unit path of a proton at the
  same speed.
- The $1/\beta^2$ factor, i.e. $1/E$ at non-relativistic energies, makes the
  stopping power *large at low energy*. This is the opposite of intuition from
  the cross-section language of photons, and it is the whole origin of the Bragg
  peak.
- The $\beta^2$ inside the logarithm gives a minimum near $\beta\gamma \approx 3$
  (a few hundred MeV for a proton): a mildly relativistic particle is the *least*
  strongly stopped one. The "minimum-ionising particle" is the standard
  calibration reference of particle physics.

**Range and the Bragg peak.** Integrating (1) gives the **continuous slowing
down approximation** (CSDA) range,

$$R(E_0) = \int_0^{E_0}\frac{\mathrm{d}E}{-\mathrm{d}E/\mathrm{d}x}. \tag{2}$$

Because $-\mathrm{d}E/\mathrm{d}x$ grows as the particle slows, most of the
energy is deposited near the end of the track. The demo computes the curve for
an alpha in air:

```text
   E (MeV)      beta    gamma   -dE/dx (MeV/cm)   /(dE/dx at 5.5)
     5.486   0.05419  1.00147              0.90             1.000
       3   0.04009  1.00080              1.36             1.517
       2   0.03274  1.00054              1.76             1.963
       1   0.02316  1.00027              2.57             2.857
     0.4   0.01465  1.00011              3.25             3.616
```

The stopping power rises by a factor of 3.6 between the emission energy and
0.4 MeV. That is the **Bragg curve**, and it has two direct consequences: a
thin dead layer of skin protects the basal cells from an external alpha emitter,
and the same emitter inside the body is far more damaging because the Bragg peak
lands in living tissue.

**Range, and the mass range.** Integrating (2) from 5.486 MeV (the alpha from
Am-241) down to the 0.30 MeV cutoff where the Bethe bracket changes sign gives
3.6688 cm in air at 1.205 kg m⁻³, by two independent quadratures agreeing to
better than 10⁻⁴ cm. The commonly tabulated range for a 5.49 MeV alpha in air is
about 4 cm; the 8 per cent shortfall is the truncated low-energy tail, and the
demo states the cutoff rather than hiding it.

Converting to rock uses the **mass range** $R\rho$. For air,
$3.6688\ \mathrm{cm} \times 1.205 \times 10^{-3}\ \mathrm{g\,cm^{-3}} =
4.42 \times 10^{-3}\ \mathrm{g\,cm^{-2}}$. Dividing by a rock density of
2.65 g cm⁻³ gives 17 µm. This is why the *mass* range is the useful quantity:
to within the difference in $Z/A$ and in $\ln(1/I)$, the range of a given
charged particle is the same in grams per square centimetre of any material, and
the geometric range then follows by dividing by density. A sheet of paper
(≈80 g m⁻² ≈ 8 × 10⁻³ g cm⁻²) stops an alpha of 5.5 MeV; so does 20 µm of
rock; so does 4 cm of air.

**Beta particles.** A beta is an electron, so the same formula applies with
$z = 1$ and with the additional complication that the incident and target
particles are identical, which requires an exchange term. Two differences matter
in practice. First, beta ranges are usually described by a power law fitted to
measurements, $R \propto E^{1.1\text{–}1.3}$, rather than by the integral of
(1), because the continuous spectrum makes "the" energy ambiguous. Second, a
beta radiates: **bremsstrahlung** is emitted with a yield per beta of order
$ZE_{\max}/3000$, so a 2.28 MeV beta stopped in lead converts to a photon about
6 per cent of the time against about 1 per cent in aluminium. Shielding a beta
source with a high-$Z$ material *creates* hard X-rays; the standard practice of
putting low-$Z$ material next to the source and high-$Z$ material outside it is
this ratio ([06](./06-dosimetry.md) §4).

## 2. Photons: three processes, and the attenuation law

A photon has no charge, so it cannot be slowed continuously. It travels until it
interacts, and each interaction either removes it from the beam or scatters it
to a new direction and energy. Only three processes matter from a few keV to
tens of MeV.

### 2.1 Photoelectric absorption

A photon is absorbed by a bound atomic electron, which is ejected. Because the
electron is bound, the process requires the photon to carry at least the binding
energy, and because the electron's wavefunction is concentrated near the
nucleus, the cross section grows steeply with the nuclear charge. The
parametric behaviour is

$$\sigma_\mathrm{pe} \propto \frac{Z^n}{E^3}, \qquad n \approx 4\text{–}5,
\tag{3}$$

an empirical scaling accurate to order of magnitude and useful for ratios. Two
consequences:

- **Edges.** Below the K-shell binding energy the 1s electron is unavailable, so
  the cross section drops abruptly. A material is a very different absorber at
  60 keV and at 90 keV, and the difference is a property of its atoms
  ([01](./01-atomic-structure.md) §3).
- **The heavy-element effect.** Going from aluminium to lead is a factor of 6.3
  in $Z$, hence $1.6 \times 10^3$ to $1.0 \times 10^4$ in $\sigma_\mathrm{pe}$
  — four orders of magnitude from a factor of six in atomic number. This is why
  lead is the shielding material for X-rays and low-energy gammas, and why it is
  *not* special for high-energy gammas.

### 2.2 Compton scattering

The photon scatters off an essentially free electron. Energy and momentum
conservation give the **Compton shift**:

$$\lambda' - \lambda = \frac{h}{m_ec}(1 - \cos\theta), \tag{4}$$

with $h/m_ec = 2.426$ pm. In energy form,

$$E' = \frac{E}{1 + \alpha(1 - \cos\theta)}, \qquad
\alpha = \frac{E}{m_ec^2}. \tag{5}$$

The differential cross section is the Klein–Nishina formula, and its integral
over solid angle has a closed form. The demo verifies the quadrature against the
closed form at ten energies and against the tabulated Thomson limit:

```text
   E (MeV)     alpha   numeric (r_e^2)   analytic (r_e^2)    rel diff   sigma (barn)
     0.001   0.00196      8.3449573797       8.3449573388    4.91e-09       0.662655
     0.662   1.29550      3.2256290348       3.2256290348    7.02e-15       0.256140
         1   1.95695      2.6597850455       2.6597850455    3.04e-14       0.211208
        10  19.56951      0.6421077986       0.6421077986    7.61e-15       0.050988

  Low-energy limit from the closed form: 8 pi r_e^2 / 3 = 0.6652459 barn
  The tabulated Thomson cross section is                  0.6652459 barn
  Relative difference: 7.55e-12
```

That agreement is the verification: the quadrature, the closed form and the
independently tabulated constant are the same object. The physical reading is
that the cross section falls from 0.665 barn at low energy to 0.051 barn at
10 MeV, and becomes strongly forward-peaked. Above about 1 MeV, Compton
scattering ceases to be an isotropic obstacle and becomes a forward-directed
process, which is why a Compton shield "leaks" along the beam direction.

The spectral landmarks follow directly from (5). For 662 keV:

```text
  E = 0.662 MeV:
    backscatter (theta = 180 deg): E' = 184.35 keV, deposited = 477.65 keV
    Compton edge (maximum electron energy) = 477.65 keV
    at 90 deg: E' = 288.39 keV
```

The backscatter energy tends to $m_ec^2/2 = 255.5$ keV as the incident energy
rises, so the "backscatter peak" in a spectrum is a fixed landmark, not a line
from the source. A spectrum recorded through a wall therefore shows a feature
near 200 keV whatever the primary energy was.

### 2.3 Pair production

Above a threshold, a photon in the field of a nucleus converts into an
electron–positron pair. The threshold is a kinematic identity: the pair's rest
energy is $2m_ec^2 = 1.022$ MeV, and a photon in free space cannot satisfy energy
and momentum conservation simultaneously, so a third body is required. In the
field of a nucleus of mass $M$ the true threshold is $2m_ec^2(1 + m_e/M)$,
which the demo computes as 1.022138 MeV for a proton — 0.014 per cent above the
naive value. The cross section scales as $Z^2$ and grows with energy, and the
pair carries the excess:

```text
 E (MeV)    excess (MeV)   T_each (MeV)  T_each / E
   1.022         2.1e-06       1.05e-06     0.00000
     2        0.978002       0.489001     0.24450
    10           8.978          4.489     0.44890
```

At tens of MeV the pair carries most of the photon energy, and it then radiates
bremsstrahlung of its own. This is why the dose rate behind a very thick shield
can *rise* with thickness (build-up), and why dose limits are written for a
stated energy and geometry rather than as a single number.

### 2.4 The attenuation law, derived

Let the number density of target atoms be $N = \rho N_A/\bar A$ and the
interaction cross section per atom be $\sigma$. In a slab of thickness
$\mathrm{d}x$ the fraction of photons removed is

$$\frac{\mathrm{d}\phi}{\phi} = -N\sigma\,\mathrm{d}x
\equiv -\mu\,\mathrm{d}x, \qquad \mu = N\sigma . \tag{6}$$

Integrating gives the **exponential attenuation law** $\phi = \phi_0e^{-\mu x}$,
and the definitions that come with it: the mean free path $1/\mu$, the
half-value layer $\mathrm{HVL} = \ln 2/\mu$, and the tenth-value layer
$\ln 10/\mu$. Note that (6) contains no approximation beyond the assumption that
each photon is removed by at most one interaction — no coherence, no build-up,
no geometry.

Because $\sigma$ is a sum of three processes, so is $\mu$:

$$\mu = N(\sigma_\mathrm{pe} + \sigma_\mathrm{C} + \sigma_\mathrm{pp}) . \tag{7}$$

This is the whole content of a photon attenuation table. The quantity $\mu/\rho$
is the mass attenuation coefficient, in cm² g⁻¹, and it is nearly the same for
all materials in the Compton-dominated regime because $N/\rho = N_AZ/\bar A$ and
$Z/A$ is between 0.4 and 0.6 for almost all stable matter. The demo computes the
Compton-only coefficient:

```text
material         Z/A  rho (g/cm3)    N_e (1/cm3)   mu/rho (cm2/g)   mu (1/cm)
air           0.4991     0.001205     3.6218e+20         0.076987     0.00009
water         0.5546        0.998     3.3334e+23         0.085554     0.08538
aluminium     0.4818          2.7     7.8340e+23         0.074319     0.20066
iron          0.4656        7.874     2.2077e+24         0.071815     0.56547
lead          0.3958       11.34     2.7026e+24         0.061045     0.69225
```

$\mu/\rho$ spans 0.061 to 0.086 cm² g⁻¹, a spread of 40 per cent, while $\mu$
itself spans a factor of $7.5 \times 10^3$. A shield attenuates because it is
heavy, not because it is special.

The computed Compton-only figure for lead is 0.69225 cm⁻¹. The true total at
662 keV is larger, because photoelectric absorption is not negligible for lead
at that energy; a photon cross-section compilation gives a total $\mu/\rho$ of
order 0.1 cm² g⁻¹, roughly 1.7 times the Compton-only value. That factor must be
looked up, not derived, and the demo quantifies what it costs to get it wrong:

```text
 total/Compton  assumed mu (1/cm)    HVL (cm)  tenth-value (cm)   factor 100 (cm)
             1           0.69225      1.0013            3.3262            6.6524
             2           1.38451      0.5006            1.6631            3.3262
             3           2.07676      0.3338            1.1087            2.2175
```

## 3. Physical interpretation

**Coupling, not energy, sets the ranges.** The alpha and the gamma in the
opening paragraph differ by a factor of a few hundred in energy and by four
orders of magnitude in range. The alpha has charge and loses energy at every
atomic encounter; the gamma has none and must hit something. Every shielding
strategy in radiation protection follows from that single distinction: charged
particles are stopped by *thickness*, photons by *mass per unit area of
high-Z material*, and neutrons (lesson 05) by *moderation*.

**$Z$ is the shield designer's variable.** In the Compton regime $\mu \propto
Z/A$, so mass is all that matters and a kilogram of water does about as well as
a kilogram of lead per unit mass per unit area — but occupies a thousand times
the volume. Below a few hundred keV, photoelectric absorption makes high $Z$
enormously better per unit mass. Above a few MeV, pair production does the same
for any high-$Z$ material but adds a bremsstrahlung problem. The optimum shield
for a given spectrum is therefore an energy-dependent choice, and the flat
statement "lead is the best shield" is true only for the lower half of the
range.

**Attenuation is not absorption.** A photon removed from the beam by Compton
scattering is still in the room, with somewhat less energy and a new direction.
The *attenuation* coefficient $\mu$ counts removals from the beam; the *energy
absorption* coefficient $\mu_\mathrm{en}$ counts the fraction of energy actually
deposited in the material. For a dose calculation behind a thin shield the
distinction is worth tens of per cent; for a thick shield it is part of the
build-up factor. Both coefficients come from the same compilation and both must
be cited.

## 4. Assumptions and regime of validity

1. **Narrow beam.** The exponential law assumes every interaction removes the
   photon from the beam. Written for a broad geometry it is a lower bound on the
   transmitted intensity, because scattered photons may still arrive at the
   detector. The correction is a **build-up factor** $B$, of order 1.1 for a
   thin shield and exceeding 2 for a thick one, and it is tabulated per geometry
   rather than derived.
2. **Single interaction.** Multiple scattering inside a thick shield is not in
   (6). For a shield of a few mean free paths the exponential with a build-up
   factor is the standard first approximation; for more, a transport
   calculation is the only defensible answer.
3. **The Bethe formula's own limits.** Equation (1) is invalid below the energy
   at which the logarithm changes sign — 0.16 MeV for an alpha in air, which is
   why the range integral is truncated at 0.30 MeV. It also neglects the
   charge-state changes of a slowing ion (important below about 1 MeV per
   nucleon), the density effect at high energy, and for electrons the exchange
   term and the fact that an electron can lose all its energy in one collision.
4. **Cross-section scaling laws are order-of-magnitude.** Equation (3) is a
   parametrisation, not a theory. Use it for ratios and for understanding
   trends; never for an absolute cross section in a design.
5. **Composition, not just density.** $\mu/\rho$ depends on $Z/A$ and on the
   presence of high-$Z$ traces. A few per cent of iron in a concrete changes its
   attenuation measurably; a baryte aggregate changes it a great deal.
6. **Edges.** Any calculation within a factor of two of a K edge must use
   tabulated coefficients at the actual energy, because the scaling laws do not
   reproduce the jump.
7. **What is computed and what is looked up.** In this lesson: the Bethe
   stopping power and range (computed from $I$, which is tabulated), the
   Klein–Nishina cross section (exact), the attenuation law (exact), the
   Compton-only $\mu$ (computed), the total $\mu$ (**tabulated**), the response
   functions of detectors (**model**). A shielding specification that does not
   distinguish these three categories cannot be checked.

## 5. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| Stopping power | $-\mathrm{d}E/\mathrm{d}x$ | MeV cm⁻¹ | $\times\ 1/\rho$ gives MeV cm² g⁻¹ |
| Mass stopping power | $-\mathrm{d}E/\mathrm{d}x / \rho$ | MeV cm² g⁻¹ | Nearly material-independent |
| CSDA range | $R$ | cm | $R\rho$ in g cm⁻² |
| Cross section | $\sigma$ | barn = 10⁻²⁸ m² = 10⁻²⁴ cm² | Per atom or per electron |
| Linear attenuation coefficient | $\mu$ | cm⁻¹ or m⁻¹ | $\mu = N\sigma$ |
| Mass attenuation coefficient | $\mu/\rho$ | cm² g⁻¹ | The tabulated form |
| Half-value layer | HVL | cm | $\ln 2/\mu$ |

Three checks.

**The attenuation law is dimensionally forced.** $\sigma$ in cm² times $N$ in
cm⁻³ gives cm⁻¹; multiplying by a thickness in cm gives a dimensionless
exponent. If $\mu$ comes out in m⁻¹ and $x$ in cm, the attenuation is wrong by
10². This is the most common unit error in shielding work and the easiest to
avoid.

**The mass range is the invariant.** $R\rho$ for a charged particle is nearly
independent of the material because (1) depends on the medium only through $Z/A$
and $\ln(1/I)$, and $Z/A$ varies little. That is why range tables are published
in g cm⁻² and why 4 cm of air, 20 µm of rock and 80 g m⁻² of paper stop the same
alpha. Check the arithmetic once: $3.6688\ \mathrm{cm} \times 1.205 \times
10^{-3}\ \mathrm{g\,cm^{-3}} = 4.42 \times 10^{-3}\ \mathrm{g\,cm^{-2}}$, and
$4.42\times10^{-3}/2.65 = 1.67\times10^{-3}$ cm = 16.7 µm.

**The Compton cross section has a known limit.** The Thomson cross section is
$8\pi r_e^2/3 = 0.6652$ b, a number that follows from $r_e$ alone. Any
numerical integration of the Klein–Nishina differential cross section must
approach it as $E \to 0$; the demo verifies one part in 10¹². A disagreement
here means the quadrature or the formula is wrong, and it is checkable without
any table.

## 6. Python demonstration

[`code/radiation_interaction_demo.py`](./code/radiation_interaction_demo.py)
integrates the Klein–Nishina cross section and compares it with the closed form,
computes Compton kinematics, the Compton-only attenuation coefficient and its
sensitivity to the tabulated total, the pair-production threshold and energy
partition, the Bethe stopping power and CSDA range for alphas in air, and the
allowed shape of a beta spectrum. Run it; the numbers below are its actual
output.

The stopping power and range for alphas, quoting the script's own caveat:

```text
quadrature             n   range in air (cm)
midpoint             200             3.66874
midpoint           20000             3.66876
Simpson              200             3.66876
Simpson             2000             3.66876

  The two quadratures agree to better than 1e-4 cm, so the integral
  is under control; the physics is not. The computed range is
  3.669 cm, and the range commonly tabulated for a 5.49 MeV alpha in
  air is about 4 cm at room temperature. The bracket is truncated at
  0.30 MeV because the Bethe formula becomes unphysical below about
  0.16 MeV for an alpha in air, which omits a few millimetres of
  track and biases the result low. A range calculation is a
  modelling calculation with a stated cutoff, not a measurement.
```

The beta spectrum, from the same script:

```text
   Q (MeV)   mean T (MeV)   mean T / Q   modal T (MeV)  modal T / Q
     0.156        0.05421      0.34752         0.03512      0.22510
     1.311        0.53438      0.40761         0.47635      0.36335
      2.28        0.98270      0.43101         0.93275      0.40910
```

### What to observe

- Two independent quadratures agree to $10^{-4}$ cm on the alpha range, so the
  *integral* is verified; the *physics* is a model with a stated cutoff, and the
  8 per cent difference from the tabulated range is that cutoff, not an error
  discovered. Saying which of the two you are reporting is the whole discipline
  of this lesson.
- The mean energy of a beta is between 0.35 and 0.43 of its end point, so a beta
  emitter's "energy" quoted as a single number is always the end point and never
  the energy actually deposited. Only about five parts per million of the decays
  fall in the top 1 per cent of the energy range for a 1.311 MeV emitter, which
  is why end points are fitted and not read off the last channel.
- The Compton-only attenuation of lead is 0.692 cm⁻¹ at 662 keV. Every number
  downstream of that — the half-value layer, the shield thickness, the dose rate
  — is proportional to $1/\mu$, so a 20 per cent error in the tabulated
  coefficient is a 20 per cent error in the concrete.

## 7. Common mistakes

1. **Using attenuation coefficients for energy absorption.** $\mu$ counts
   photons removed from the beam; $\mu_\mathrm{en}$ counts energy deposited. A
   dose calculation needs the second and a shielding calculation the first, and
   they differ by the energy the scattered photon takes away.
2. **Quoting a Compton cross section as if it were the total.** At 662 keV the
   Compton cross section is about 0.26 barn and the photoelectric term for lead
   is larger than the difference; at 100 keV in lead, Compton is the minority
   process outright.
3. **Using the scaling laws for absolute numbers.** $Z^{4\text{–}5}/E^3$ is a
   ratio rule. It gets the ordering right and the magnitude wrong.
4. **Forgetting the sign of the logarithm's argument.** A stopping power
   computed below the energy where $\ln(2m_ec^2\beta^2\gamma^2/I)$ becomes
   negative gives a *negative* $-\mathrm{d}E/\mathrm{d}x$, which is the formula
   announcing its own invalidity. State the cutoff.
5. **Treating a beta range as a definite depth.** Beta ranges are maximum
   ranges; the attenuation of betas is approximately exponential with an
   absorption coefficient rather than a sharp cutoff, and backscattering from a
   high-$Z$ substrate sends a substantial fraction of the incident betas
   backwards.
6. **Shielding a beta with lead.** Bremsstrahlung yield scales with $Z$; put
   low-$Z$ material first and high-$Z$ material outside it.
7. **Ignoring build-up.** The exponential law is a lower bound on transmission
   in a broad geometry. For a thick shield the build-up factor dominates the
   error budget.
8. **Mixing $\mu$ in cm⁻¹ with a thickness in metres.** A factor of 10² and a
   confident-looking nonsense answer.
9. **Using a coefficient at the wrong energy.** Attenuation coefficients change
   by factors across an absorption edge; quoting "the" coefficient for lead
   without a photon energy is not a statement.
10. **Not saying where the coefficient came from.** Half of this lesson's
    numbers are computed and half are looked up; the report must say which.

## 8. Real-world applications

- **Borehole gamma logging.** The measurement is depth against count rate,
  the attenuation is described by this lesson, and the depth of investigation of
  a natural-gamma or density log follows directly from $\mu$ and the geometry
  ([05-08-02](../../05-core-geophysics/08-geophysical-logging/02-gamma-logging.md)).
- **Spectral gamma-ray surveying.** The three standard windows sit at 1.46,
  1.76 and 2.61 MeV, where Compton scattering dominates and the mass attenuation
  coefficient is nearly composition-independent — which is exactly why one
  calibration curve can serve many soils
  ([04](./04-gamma-spectrometry.md)).
- **Density and Pe logging.** A density tool is a gamma–gamma backscatter
  measurement, and the Pe measurement is the photoelectric cross section of
  §2.1 used deliberately ([05](./05-neutron-interaction.md) §7).
- **Shielding design and dose assessment.** Everything here is expressed in
  the half-value layer, and the dose calculation is lesson 06.
- **Radiography and industrial inspection.** Source energy is chosen just above
  or below a K edge to control contrast; the same principle as medical imaging.
- **Detector physics.** A NaI crystal stops gammas by all three processes; the
  shape of the resulting spectrum — photopeak, Compton continuum, escape peaks —
  is this lesson plus the resolution of a real detector
  ([04](./04-gamma-spectrometry.md)).
- **Radon progeny dosimetry.** Alpha emitters deposited on the bronchial
  epithelium deliver their energy within micrometres, which is why the
  alpha dose per unit activity is orders of magnitude above the gamma dose
  ([06](./06-dosimetry.md)).

## 9. Further reading

- **Knoll, G. F. *Radiation Detection and Measurement* (Wiley).** The standard
  text. Chapters on photon and charged-particle interactions are the reference
  for everything in this lesson, including the build-up factor and the
  energy-absorption distinction. Level: graduate.
- **Attix, F. H. *Introduction to Radiological Physics and Radiation
  Dosimetry* (Wiley).** The dosimetry-oriented treatment: stopping powers,
  cavity theory, and the relation between fluence and dose. Level: graduate.
- **ICRU, *Stopping Powers and Ranges for Protons and Alpha Particles* (Report
  49) and *Stopping Powers for Electrons and Positrons* (Report 37).** The
  tabulated $I$ values and range tables used as inputs here. Level: reference.
- **NIST, *XCOM: Photon Cross Sections Database*, and the *Physical Reference
  Data* pages.** The source for $\mu/\rho$, the partial cross sections and the
  energy-absorption coefficients. Confirm the current release and cite it.
  Level: reference.
- **Ziegler, J. F., Biersack, J. P., & Littmark, U. *The Stopping and Range of
  Ions in Solids* (Pergamon).** The origin of the widely used semi-empirical
  stopping tables, and the place to look when (1) is not good enough. Level:
  graduate.
- **ICRP, *Conversion Coefficients for Use in Radiological Protection against
  External Radiation* (Publication 74, and its successors).** The bridge from
  fluence to effective dose, needed for anything in lesson 06. Level:
  reference.
- **NIST, *CODATA Internationally Recommended Values of the Fundamental Physical
  Constants*.** The source of $r_e$, $m_e$ and the exact SI constants used in
  the cross-section calculations. Distributed at
  <https://physics.nist.gov/cuu/Constants/>. Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 10. Related lessons

- [01 Atomic Structure and Energy Levels](./01-atomic-structure.md) — the
  binding energies that set the photoelectric cross section and its edges.
- [02 Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md) — the
  sources of the particles whose interaction this lesson describes.
- [04 Gamma-Ray Spectrometry and Natural Radioelements](./04-gamma-spectrometry.md)
  — what the three interaction processes look like in a measured spectrum.
- [05 Neutron Interactions and Borehole Nuclear Measurements](./05-neutron-interaction.md)
  — the uncharged particle that this lesson's logic does not cover.
- [06 Dosimetry, Radiation Safety and Regulatory Limits](./06-dosimetry.md) — the
  attenuation coefficients and stopping powers turned into a dose.
- [02-03-10 Attenuation, Absorption and the Quality Factor Q](../03-oscillations-and-waves/10-attenuation.md)
  — the same exponential law applied to seismic waves.
- [02-07-05 Electromagnetic Waves, Impedance and Polarisation](../07-electromagnetism/05-em-waves.md)
  — what a photon is, and what "intensity" means for a beam.

Exercises:
[`exercises/03-radiation-interaction-exercises.md`](./exercises/03-radiation-interaction-exercises.md)
and
[`exercises/03-radiation-interaction-solutions.md`](./exercises/03-radiation-interaction-solutions.md).

## Self-assessment checklist

- [ ] I can write the Bethe formula and say where the $z^2$, the $1/\beta^2$ and
      the logarithm come from in first-order terms. (§1)
- [ ] I can compute a stopping power and a CSDA range, and state the cutoff
      below which the formula is unphysical. (§1)
- [ ] I can explain the Bragg peak and give two biological or engineering
      consequences of it. (§1)
- [ ] I can convert a range in air into a range in rock via the mass range, and
      say why that works. (§5)
- [ ] I can derive the Compton wavelength shift and compute the Compton edge and
      backscatter energies for a given line. (§2.2)
- [ ] I can verify a numerical Klein–Nishina integral against the Thomson limit.
      (§2.2, §6)
- [ ] I can derive $\phi = \phi_0e^{-\mu x}$ from a cross section and a number
      density, and compute an HVL. (§2.4)
- [ ] I can state the $Z$ and $E$ dependence of all three photon processes and
      decide which dominates for a given photon and material. (§2)
- [ ] I can distinguish attenuation from energy absorption and say which a dose
      calculation requires. (§3)
- [ ] I can name the compilation I would use for $\mu/\rho$ and for a stopping
      power, and say when I last confirmed it. (§9)
