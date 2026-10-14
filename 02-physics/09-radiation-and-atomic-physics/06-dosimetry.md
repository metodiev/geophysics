---
id: 02-09-06
title: "Dosimetry, Radiation Safety and Regulatory Limits"
level: intermediate
prereqs: ["02-09-02", "02-09-03", "02-01-02"]
estimated_minutes: 90
tags: [dosimetry, radiation-protection, alara, radon, norm, detection-limits]
---

# Dosimetry, Radiation Safety and Regulatory Limits

Every part of a dose calculation except one is straightforward arithmetic. The
one part that is not is the set of numbers that the arithmetic is *about*: the
fluence-to-dose conversion coefficients, the radiation and tissue weighting
factors, and the dose limits themselves. Those are decisions — scientific
committees recommend, national regulators adopt, and the values are revised on a
timescale of years. A dose assessment that quotes them from memory is not an
assessment.

This lesson therefore does something unusual, and deliberately. It derives and
computes everything that can be computed, keeps the regulatory limits symbolic
throughout, and shows the reader how to present a calculation in which the
*sourced* numbers and the *computed* numbers are visibly separated. The demo
prints occupancy times as `L / dose-rate` with `L` the limit, so that the
arithmetic is on the page and the number that must be looked up is not smuggled
in.

The lesson also covers the part of dosimetry that is exact — counting statistics
— because that is where the geophysical applications actually live: a
radionuclide measurement is a count above a background, and the detection limit
follows from the Poisson distribution with no tabulated input at all.

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** activity, exposure, absorbed dose, equivalent dose and
   effective dose, and state the unit of each.
2. **Explain** why the same photon fluence gives different effective doses for
   different particles, and why the weighting factors are committee decisions
   rather than derived quantities.
3. **Derive** the point-source fluence rate and the inverse-square law, and the
   factor-of-two distance rule.
4. **Compute** a dose rate from a source with a declared conversion coefficient,
   and quantify how much the answer depends on that coefficient.
5. **Compute** a required shield thickness, its dependence on the tabulated
   attenuation coefficient, and the effect of the build-up factor.
6. **Explain** why a beta source is shielded low-$Z$ first, and compute the
   bremsstrahlung yield ratio for two absorbers.
7. **Compute** Poisson counting uncertainties, a detection limit and its floor,
   and explain why a detection limit without a stated counting time and
   background is meaningless.
8. **Describe** the structure of a radiation-protection regime — limits,
   constraints, optimisation, monitoring, clearance — and state which of its
   numerical values must be taken from the current recommendations and the
   national regulation.
9. **Present** a dose assessment in which computed, model and sourced quantities
   are separately labelled.

## Prerequisites

- [02-09-02 Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md) —
  activity, and the mass of nuclide in a source of a stated activity.
- [02-09-03 Interaction of Radiation with Matter](./03-radiation-interaction.md)
  — attenuation coefficients, half-value layers and charged-particle ranges.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — the Poisson statistics that §6 uses, and the discipline of error bars.

## 1. The quantities and their units

Radiation protection is built from four quantities in a chain, each one a
weighted version of the one before. Getting the chain right is most of the
bookkeeping.

**Activity $A$** (becquerel, Bq = s⁻¹; 1 curie = $3.7 \times 10^{10}$ Bq
exactly) counts *decays per second*. It says nothing about what is emitted or
where the energy goes.

**Exposure** (coulomb per kilogram, or the legacy roentgen) is the ionisation
produced in air. It is a dose-free measurable quantity and is now largely of
historical and instrument-calibration interest.

**Absorbed dose $D$** (gray, Gy = J kg⁻¹; 1 rad = 0.01 Gy) is the energy
deposited per unit mass at a point:

$$D = \frac{\mathrm{d}\bar\varepsilon}{\mathrm{d}m} \quad[\mathrm{J\,kg^{-1}}].
\tag{1}$$

This is a physical quantity, and it is the one a calorimeter or a TLD measures.

**Equivalent dose $H$** (sievert, Sv; 1 rem = 0.01 Sv) folds in the biological
effectiveness of the radiation type:

$$H = \sum_R w_R D_R \quad[\mathrm{J\,kg^{-1}} = \mathrm{Sv}]. \tag{2}$$

**Effective dose $E$** (sievert) folds in the differing sensitivity of tissues:

$$E = \sum_T w_T H_T . \tag{3}$$

Because $w_R = 1$ for photons and electrons, $H = D$ numerically for the
gamma-ray and beta fields that dominate geophysics; because the weighting
factors for neutrons and alpha particles are larger, the *same absorbed dose*
from an alpha emitter corresponds to a much larger equivalent dose. That is why
"twenty microsievert per hour" cannot be checked against a survey meter reading
in grays without saying what the radiation is.

**Where the weighting factors come from.** They are recommendations of the
International Commission on Radiological Protection, based on radiobiological
evidence, adopted with modifications by national regulators, and revised
periodically. The photon and electron factor is unity by definition; the neutron
factor varies strongly with energy; the alpha factor is large. **The numerical
values must be taken from the current ICRP recommendations**, with the
publication and the year cited, and the same applies to the tissue weighting
factors. Nothing in this lesson quotes them.

**Why dose is not activity.** A becquerel is a rate and a sievert is energy per
unit mass; the conversion depends on the decay scheme, the geometry, the
material between the source and the person, and the weighting factors. A
4 GBq check source and a 4 GBq contaminated floor are not the same hazard, and
the difference is entirely in the conversion — which is the subject of §2 to §5.

## 2. From activity to dose rate, derived

**Fluence.** For an unshielded point source of activity $A$ emitting $y$ photons
of interest per decay, the number crossing unit area per unit time at distance
$r$ is

$$\varphi = \frac{A y}{4\pi r^2}, \tag{4}$$

because the emission is isotropic and the sphere has area $4\pi r^2$. Nothing is
tabulated in (4) except $y$, which comes from a decay-data compilation. The demo
evaluates it:

```text
   r (m)       r^2   phi (photons/cm2/s)
     0.3      0.09            7.5157e+04
     0.5      0.25            2.7056e+04
     1.0      1.00            6.7641e+03
     2.0      4.00            1.6910e+03
     4.0     16.00            4.2276e+02
     8.0     64.00            1.0569e+02
```

Doubling the distance quarters the fluence and therefore halves the dose rate.
Halving the distance multiplies it by four. This is the **factor-of-two rule**,
and it is the cheapest and most reliable protective measure available. It also
fails in a specific way worth knowing: a long line source falls off as $1/r$
rather than $1/r^2$, and a large plane source does not fall off at all. A
contaminated floor is a plane source, which is why surface contamination is
monitored with a different instrument and a different geometry from a point
source.

**Dose rate.** The conversion from fluence to a protection quantity is a
tabulated coefficient,

$$\dot H = \varphi\, h, \tag{5}$$

where $h$ has units of Sv m² per photon (or per unit fluence, in whatever
geometry convention the compilation uses). For a point source this gives

$$\dot H = \frac{A y h}{4\pi r^2}, \tag{6}$$

which is the origin of the "specific gamma-ray constant" tables: those are
$y h/(4\pi)$ for a particular nuclide, expressed in a conventional unit. They are
convenient, they are tabulated, and they are only as good as the conversion
coefficients they were built from — which changed when the ICRP recommendations
changed.

The demo evaluates (6) for 1 GBq at 1 m with a declared $h$ and then shows the
sensitivity, which is the honest way to present it:

```text
    phi   = 6.7641e+07 photons per m^2 per s
    H_dot = 2.7056e-02 microSv/s = 0.0974 mSv/h

  h multiplier    H_dot (mSv/h)   change (%)
           0.5           0.0487          -50
           1.0           0.0974            0
           2.0           0.1948          100
```

The dose rate is linear in the conversion coefficient, so a factor of two in the
coefficient is a factor of two in the answer. Every dose assessment must
therefore cite the coefficient, its publication and its date. "The dose rate is
0.097 mSv/h" is not a statement about the world; it is a statement about a
choice of coefficients.

## 3. Shielding and the time–distance–shielding triangle

For a narrow beam, the fluence behind a thickness $x$ of material of linear
attenuation coefficient $\mu$ is $\varphi(x) = \varphi_0e^{-\mu x}$, so the
attenuation factor is exponential and the half-value layer is
$\mathrm{HVL} = \ln 2/\mu$. The demo's illustrative coefficients at 662 keV give:

```text
material       mu (1/cm)   HVL (cm)  tenth-value (cm)  x for 100x (cm)
water             0.0870      7.967            26.466           52.933
concrete          0.1800      3.851            12.792           25.584
iron              0.5770      1.201             3.991            7.981
lead              1.2500      0.555             1.842            3.684
```

The coefficient is the input that matters, and the required thickness scales as
$1/\mu$:

```text
  mu error   x for 100x (cm)   x error (%)
      -20%            4.6052         25.00
        0%            3.6841         -0.00
       20%            3.0701        -16.67
       50%            2.4561        -33.33
```

For a fractional coefficient error $d$ the thickness error is $-d/(1+d)$: a
10 per cent overestimate of $\mu$ gives a 9 per cent underestimate of the
thickness, and a 50 per cent overestimate gives 33 per cent. **And the table
does not contain the build-up factor.** A broad beam is attenuated *less* than a
narrow one, by a factor that can exceed 2 for a thick shield, so the exponential
law is a lower bound on the required thickness. For a thin shield the build-up
correction is tens of per cent; for a thick one it dominates.

**Distance versus thickness.** Holding the shield fixed and moving the observer
back:

```text
   r (m)   exp(-mu x)/r^2  relative to 0.5 m  shield area for 10 deg cone (m2)
     0.5           1.1460              1.000                            0.0244
     2.0           0.0716              0.062                            0.3907
     4.0           0.0179              0.016                            1.5628
```

Moving from 0.5 m to 2.0 m buys a factor of sixteen for no material — but a
shield at 2.0 m must subtend the same solid angle, and its area (and hence mass)
grows as $r^2$, which cancels the gain. What actually helps is distance between
the *shield* and the observer, put there by giving the shield a finite thickness,
not distance as such. That is why a shield is mounted as close to the source as
it can be, and why a radiography collimator is bolted to the source housing.

## 4. Beta sources: bremsstrahlung and the ordering of absorbers

A beta particle slowing in a material radiates. The radiative yield per beta is
of order $ZE_{\max}/3000$ with $E_{\max}$ in MeV, so the *absorber* decides how
much hard X-radiation the shield itself will produce. The demo computes it:

```text
absorber        Z  E_max (MeV)  Y per beta  photons per 1000 betas
aluminium    13.0        2.280  9.8800e-03                    9.88
iron         26.0        2.280  1.9760e-02                   19.76
lead         82.0        2.280  6.2320e-02                   62.32
```

A strontium-90 source with its yttrium-90 daughter has a maximum beta energy near
2.28 MeV. Shielded with lead, about 6 per cent of the betas produce a
bremsstrahlung photon; shielded with aluminium, about 1 per cent. The lead shield
must then attenuate a hard photon flux that the aluminium shield never produced.
The standard practice — low-$Z$ material against the source, high-$Z$ material
outside — is nothing more than this ratio. The estimate itself is crude: the
coefficient and the spectral shape come from the Bethe–Heitler cross section, and
self-absorption and angular distribution are neglected. Use it to decide the
*order* of the layers and use a transport calculation for a design.

## 5. Internal exposure and the two environments

External exposure is what the previous sections describe: a source outside the
body, shielded by distance and material. Internal exposure is a different
problem with a different geometry, and it is usually the larger one in
geophysics.

**Why internal dose is different.** A source inside the body has no distance to
be moved and no shield to be added; its dose depends on the emitted particle's
range and on the radionuclide's chemistry. An alpha emitter (range of
micrometres) deposited on the bronchial epithelium concentrates all of its energy
in a thin layer of living cells, and its weighting factor is large; the same
activity outside the body cannot even penetrate dead skin. A beta emitter
deposited in bone irradiates the bone marrow. The two mechanisms — energy
concentration and chemical targeting — are why the same becquerel count can mean
a thousandfold different risk depending on whether it can be inhaled.

**Radon.** The largest single contributor to the natural background effective
dose, in most compilations, is radon and its short-lived progeny, which are
inhaled rather than irradiating from outside. Radon's source is uranium and
radium in soil and rock, which is exactly what a radiometric survey maps
([04](./04-gamma-spectrometry.md) §4). A poorly ventilated core shed, an
underground working or a basement in a uranium-bearing terrain is where a
radiation-protection limit is most likely to be approached in this field, and the
assessment requires the current national reference level and the current IAEA
guidance — neither of which is reproduced here.

**The committed dose convention.** An intake is expressed as a **committed
effective dose**, integrated over a stated period (conventionally 50 years for
adults), through a tabulated dose coefficient per unit intake — the "e(50)"
coefficients of the ICRP. These are jurisdiction-independent in their scientific
content and are published per radionuclide and per route of intake (inhalation,
ingestion) and per chemical form. Use them from the current publication and cite
the table.

**NORM.** Naturally occurring radioactive material — oilfield scale and produced
water, some mineral sands, some industrial residues and some building materials
— concentrates radionuclides to levels that bring material into the regulatory
system. The threshold concentrations that define when a material is regulated
are set by national regulation, are conventionally expressed per gram of
material, and are revised. Classify such a material by looking up the current
national values, not from memory.

## 6. Counting statistics, detection limits and the part that is exact

Everything in §2 to §5 needed a tabulated coefficient. This section needs none.

Counting radioactive decays is a Poisson process, so a count $N$ has standard
deviation $\sqrt N$ and a rate $N/t$ has relative uncertainty
$1/\sqrt N$:

```text
    counts     sigma    rel unc (%)   time for 1% (s at 1 cps)
        10      3.16          31.62                     1000.0
      1000     31.62           3.16                       10.0
     10000    100.00           1.00                        1.0
   1000000   1000.00           0.10                        0.0
```

To reach 1 per cent on a count rate you need 10 000 counts, and the time that
takes scales as $1/$rate. That single line explains why a low-activity sample is
counted for a day and a high-activity one for a minute, and why a survey
instrument trades counting time against speed over the ground.

**Detection limit.** For a sample counted for time $t_s$ against a background
counted for $t_b$ at rate $R_b$, the standard deviation of the net rate is

$$\sigma_\mathrm{net} = \sqrt{\frac{R_b}{t_b} + \frac{R_b}{t_s}}, \tag{7}$$

and the Curie criterion for the minimum detectable activity at three standard
deviations is $\mathrm{MDA} = 3\sigma_\mathrm{net}/(\epsilon y)$ with $\epsilon$
the detection efficiency and $y$ the gamma yield. The demo computes it with
declared efficiency and background:

```text
   t_s (s)  3 sigma of net rate (cps)    MDA (Bq)   MDA (kBq)
        60                   0.552268        13.0      0.0130
      3600                   0.100000         2.4      0.0024
     36000                   0.074162         1.7      0.0017
```

The limit improves only as $\sqrt{t_s}$ and it has a **floor** set by the
background counting time: as $t_s$ grows, $\sigma_\mathrm{net} \to
\sqrt{R_b/t_b}$ and the MDA approaches 1.66 Bq whatever you do to the sample.
Counting ten times longer buys a factor of two, not ten. This is why "detection
limit" is meaningless without a stated counting time, background and efficiency:
quote all three or quote none.

The geophysical reason this matters is that a survey anomaly is a count-rate
contrast above a background that is itself Poisson-distributed. An anomaly that
is two standard deviations of the background is not an anomaly; it is a coin
toss. The only way for a reader to tell the difference is to state the
background, the counting time and the area over which counts were accumulated.

## 7. Physical interpretation

**Protection is an optimisation, not a threshold.** The numerical limit is the
boundary of what is permitted, not a target: the framework requires that doses be
kept as low as reasonably achievable, economic and social factors being taken
into account. That principle — usually known by its acronym, ALARA — is what
turns a dose calculation into a design exercise: if a task gives 3 mSv with tongs
and 0.3 mSv with a longer pair, the ALARA requirement makes the longer tongs a
requirement and not a preference.

**The three controls are qualitatively different.** *Time* is linear: half the
time is half the dose. *Distance* is quadratic in the near field, which is why it
is the first thing to reach for. *Shielding* is exponential in *mass per unit
area*, which is why it is what you buy when the other two have been exhausted.
Any protection plan that names only one of the three is incomplete.

**The two environments are different sciences.** External dosimetry is geometry
and attenuation; internal dosimetry is chemistry, biology and time. The alarm
that matters in a core shed is not a personal alarm dosimeter — those respond to
the gamma field — but a radon monitor, and the control is ventilation. That a
gamma survey instrument reads nothing while the radon level is high is not a
paradox; it is the difference between the two environments.

## 8. Assumptions and regime of validity

1. **The conversion coefficients are the dominant uncertainty.** Equations (5)
   and (6) are exact given $h$; $h$ is a tabulated recommendation that changes
   between ICRP publications, and the dose inherits that change linearly. In a
   thick shield the build-up factor is a second such input, of comparable size.
2. **Point-source, narrow-beam geometry.** Equation (4) assumes isotropy and no
   scattering in the intervening air. Both are good to tens of per cent at a
   metre in air, and neither is good inside a room with concrete walls, where
   scattered photons can dominate the field. Calibration, not calculation, is the
   tool for a real room.
3. **Equilibrium and no self-absorption in the source.** A sealed source's
   encapsulation absorbs some of the low-energy output. The quoted output of a
   source is a measured quantity with an uncertainty, and it should be used
   instead of an activity computed from a decay scheme where possible.
4. **The weighting factors are not physics.** The factor of unity for photons and
   electrons is a definition; the others are recommendations based on
   radiobiological evidence and revised periodically. Using them as though they
   were measured constants with the status of $c$ is a category error.
5. **Dose limits are regulatory instruments.** They are jurisdiction-specific,
   differ between categories of worker, and are revised. Nothing in this lesson
   states one, and no calculation should embed one without a citation to the
   regulation in force and its date.
6. **The Poisson model assumes a single counting process.** Dead time, drift in
   the background, and correlated background from a nearby source all violate
   it. A detection limit computed from (7) is a statistical statement about a
   stable measurement, not a guarantee about a changing one.
7. **The bremsstrahlung estimate is order-of-magnitude.** It decides the order of
   the absorber layers, not their thicknesses.

## 9. Units and dimensional analysis

| Quantity | Unit | Relationship |
|---|---|---|
| Activity | Bq = s⁻¹; Ci = 3.7 × 10¹⁰ Bq | $A = \lambda N$ |
| Exposure | C kg⁻¹; R (legacy) | Ionisation produced in air |
| Absorbed dose | Gy = J kg⁻¹; rad = 0.01 Gy | $D = \mathrm{d}\bar\varepsilon/\mathrm{d}m$ |
| Equivalent dose | Sv; rem = 0.01 Sv | $H = \sum_R w_R D_R$ |
| Effective dose | Sv | $E = \sum_T w_T H_T$ |
| Fluence | photons m⁻² or cm⁻² | $\varphi = Ay/4\pi r^2$ |
| Fluence-to-dose coefficient | Sv m² (per photon or per unit fluence) | Tabulated |
| Counting uncertainty | dimensionless | $\sqrt N/N$ |

Three checks.

**Gray against sievert.** Both are J kg⁻¹, and the difference is a set of
dimensionless factors. A dose quoted in "mSv" for a photon field is numerically
equal to the absorbed dose in mGy; for an alpha field it is much larger. Any
comparison of a dosimeter reading with a limit must establish which quantity the
instrument reports, and a survey meter reading in µSv h⁻¹ is reporting an
equivalent dose computed with an assumed radiation type.

**Legacy factors are exact conversions, not approximations.** 1 rad = 0.01 Gy
and 1 rem = 0.01 Sv and 1 Ci = 3.7 × 10¹⁰ Bq are definitions. Use them as exact.

**Fluence and dose rate.** Check the algebra of (6) once by hand: $Ay$ is in s⁻¹,
divided by $r^2$ in m² gives m⁻² s⁻¹; multiplied by $h$ in Sv m² gives Sv s⁻¹.
A result in µSv h⁻¹ is that times 3.6 × 10⁹, since there are 3600 s per hour and
10⁶ µSv per Sv. Getting the 10⁶ wrong produces a dose rate that is either
trivially small or obviously impossible, and it is the commonest arithmetic error
in this subject after the cm/m confusion.

## 10. Python demonstration

[`code/dosimetry_demo.py`](./code/dosimetry_demo.py) converts activities,
masses and atoms; computes fluence and the inverse-square law; does the shielding
and sensitivity arithmetic; computes the bremsstrahlung yield for four absorbers;
computes Poisson uncertainties and a detection limit with its floor; and presents
the occupancy-time calculation with the limit left symbolic. Its docstring states
that it deliberately does not print a dose limit, and why.

Activity, atoms and mass:

```text
nuclide      A (GBq)         atoms    mass (g)   mass (mg)          Ci
Cs-137         1.000    1.3695e+18  3.1134e-04  3.1134e-01  2.7027e-02
Co-60          1.000    2.3998e+17  2.3884e-05  2.3884e-02  2.7027e-02
Ir-192        10.000    9.2025e+16  2.9334e-05  2.9334e-02  2.7027e-01
Am-241         1.000    1.9695e+19  7.8838e-03  7.8838e+00  2.7027e-02
```

Occupancy time, with the limit symbolic:

```text
   L (mSv/a)   H_dot (mSv/h)   hours at 1 m   hours, 50 cm back
         1.0          0.0974          10.27               23.10
         5.0          0.0974          51.33              115.50
        20.0          0.0974         205.33              462.00
```

### What to observe

- A 10 GBq industrial radiography source contains about 0.03 mg of iridium-192.
  The activity is not visible and not proportional to the size of the object,
  which is why sealed sources are inventoried by activity and serial number and
  why an unlabelled source must be treated as a maximum-activity source until
  identified.
- The dose rate is exactly linear in the conversion coefficient, so the
  coefficient — not the arithmetic — is the input whose provenance decides
  whether the answer means anything.
- The detection limit improves as $\sqrt{t_s}$ and then stops improving at
  1.66 Bq, set by the background counting time. The floor is the reason a
  detection limit is a quadruple (rate, background, time, efficiency) and not a
  number.
- The occupancy-time table contains one symbolic column and three computed ones.
  That separation is the deliverable of a dose assessment, and it is the reason
  this script prints no limit.

## 11. Common mistakes

1. **Quoting a dose limit from memory.** Limits are jurisdiction-specific and
   revised. Cite the regulation in force and its date, or do not state a number.
2. **Confusing gray and sievert.** They are the same unit with different
   weighting; for photons they coincide numerically, which is exactly why the
   error is easy to make and hard to notice.
3. **Comparing a µSv h⁻¹ meter reading with a limit without stating the
   radiation type assumed.** The meter has already applied weighting factors.
4. **Using the exponential attenuation law as an exact broad-beam result.** The
   build-up factor can double the transmission through a thick shield.
5. **Shielding a beta source with lead first.** The bremsstrahlung yield scales
   with $Z$; the low-$Z$ layer goes against the source.
6. **Reporting a detection limit without counting time, background and
   efficiency.** It is not a property of the instrument alone.
7. **Treating the internal and external problems as one.** Radon, dust and
   contaminated surfaces are a different physics from a sealed source.
8. **Assuming a sealed source's output equals its activity times a yield.** The
   encapsulation absorbs part of it; use the measured output.
9. **Forgetting the cm/m and s/h conversions.** $\mu$ in cm⁻¹ with a thickness in
   metres, or Sv s⁻¹ reported as µSv h⁻¹ without the 10⁶ and 3600, are the two
   errors that produce confidently wrong answers.
10. **Writing an assessment that does not distinguish computed from sourced
    numbers.** A reader cannot check the second kind without the citation, and
    cannot check the first without the method.

## 12. Real-world applications

- **Sealed-source handling in logging and radiography.** Inventory, leak testing,
  transport classification, and the time–distance–shielding calculation of §3 are
  the entire operational content of the licence
  ([05](./05-neutron-interaction.md)).
- **Airborne and ground radiometric surveys.** The instruments are
  low-activity by design, and the survey crew's dose is dominated by external
  gamma exposure and by transport and storage of calibration sources
  ([04](./04-gamma-spectrometry.md)).
- **Radon in buildings and in exploration work.** The dominant natural
  contributor, mapped from the uranium distribution, controlled by ventilation.
- **NORM in the oil and gas industry.** Scale, sludge and produced water with
  elevated radium, with the regulatory thresholds set nationally.
- **Environmental and geochemical laboratories.** Counting statistics and
  detection limits decide what a laboratory can report, and the floor of §6 is
  why "not detected" must be accompanied by the limit.
- **Medical and industrial applications of the same physics.** The same
  quantities, coefficients and conventions apply, which is why the field has a
  shared vocabulary.

## 13. Further reading

- **ICRP, *The 2007 Recommendations of the International Commission on
  Radiological Protection* (Publication 103) and its successors.** The
  source of the radiation and tissue weighting factors, the dose limit
  recommendations and the optimisation principle. Level: reference. Confirm the
  current publication; the recommendations are periodically revised.
- **ICRP, *Conversion Coefficients for Use in Radiological Protection against
  External Radiation* (Publication 74 and successors) and the *Dose Coefficients
  for Intakes of Radionuclides* series (Publications 68, 119 and successors).**
  The $h$ and $e(50)$ coefficients of §2 and §5. Level: reference.
- **IAEA, *Radiation Protection and Safety of Radiation Sources: International
  Basic Safety Standards* (General Safety Requirements, current edition).** The
  framework that national regulations implement, including exemption and
  clearance levels and the categorisation of sealed sources. Level: reference
  and professional practice.
- **UNSCEAR, *Sources and Effects of Ionizing Radiation* (current report).** The
  compilation of natural and artificial background doses, and the place to look
  for the regional radon figures. Level: reference.
- **Attix, F. H. *Introduction to Radiological Physics and Radiation Dosimetry*
  (Wiley).** The physical quantities and their measurement, in full. Level:
  graduate.
- **Knoll, G. F. *Radiation Detection and Measurement* (Wiley).** Counting
  statistics, background, detection limits and the instruments. Level: graduate.
- **Turner, J. E. *Atoms, Radiation, and Radiation Protection* (Wiley).** A
  compact treatment that connects the physics of this module to the protection
  framework, including the internal-dosimetry models. Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.
> For the regulatory documents in particular, always work from the edition in
> force in your jurisdiction on the day you use them.

## 14. Related lessons

- [02 Radioactive Decay, Half-Life and Dating](./02-radioactive-decay.md) — the
  activity and the mass of nuclide that a dose assessment starts from.
- [03 Interaction of Radiation with Matter](./03-radiation-interaction.md) — the
  attenuation coefficients and stopping powers behind §3 and §4.
- [04 Gamma-Ray Spectrometry and Natural Radioelements](./04-gamma-spectrometry.md)
  — the uranium mapping that underlies radon hazard assessment.
- [05 Neutron Interactions and Borehole Nuclear Measurements](./05-neutron-interaction.md)
  — the neutron fields whose weighting factors are energy dependent.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — the statistics that §6 applies in the radiation context.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the discipline of labelling a value's provenance, which this lesson applies
  to regulatory numbers.

Exercises:
[`exercises/06-dosimetry-exercises.md`](./exercises/06-dosimetry-exercises.md)
and
[`exercises/06-dosimetry-solutions.md`](./exercises/06-dosimetry-solutions.md).

## Self-assessment checklist

- [ ] I can distinguish activity, exposure, absorbed dose, equivalent dose and
      effective dose, with the unit of each. (§1)
- [ ] I can explain why the weighting factors are recommendations rather than
      measured constants, and where they come from. (§1)
- [ ] I can derive the point-source fluence rate and apply the factor-of-two
      rule. (§2)
- [ ] I can compute a dose rate with a declared coefficient and state how the
      answer scales with it. (§2)
- [ ] I can compute a shield thickness and state how it scales with the
      tabulated $\mu$. (§3)
- [ ] I can explain why a beta source is shielded with low-$Z$ material first and
      compute the yield ratio. (§4)
- [ ] I can explain why internal and external exposure are different problems
      and why radon dominates the natural background. (§5)
- [ ] I can compute a Poisson uncertainty, a detection limit and its floor. (§6)
- [ ] I can describe the structure of a protection regime and name the documents
      from which its numerical values come. (§7, §13)
- [ ] I can present a dose assessment that labels computed, model and sourced
      quantities separately. (§10)

