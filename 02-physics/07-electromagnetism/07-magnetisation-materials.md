---
id: 02-07-07
title: "Magnetisation, Susceptibility and Magnetic Materials"
level: graduate
prereqs: ["02-07-02", "02-07-03", "02-07-04"]
estimated_minutes: 90
tags: [magnetisation, susceptibility, rock-magnetism, curie-temperature, remanence]
---

# Magnetisation, Susceptibility and Magnetic Materials

## Learning objectives

By the end of this lesson you will be able to:

1. **Distinguish** $\mathbf B$, $\mathbf H$ and $\mathbf M$ dimensionally and
   physically, and use $\mathbf B = \mu_0(\mathbf H+\mathbf M)$,
   $\mathbf M = \chi\mathbf H$, $\mu_r = 1+\chi$ without conflating them.
2. **Explain** the physical origins of dia-, para-, ferro-, ferri- and
   antiferromagnetism, and the temperature dependence of each, including the
   Curie law and the Curie temperature.
3. **Distinguish** induced from remanent magnetisation, define the Koenigsberger
   ratio $Q = M_r/(\chi H)$, and say what governs which dominates.
4. **Compute** the Curie depth from a stated geothermal gradient and state every
   assumption involved.
5. **Apply** demagnetising factors and the resulting effective susceptibility
   $\chi_{\text{eff}} = \chi/(1+N\chi)$, and explain why $\chi_{\text{eff}}$
   saturates.
6. **Convert** between SI and cgs susceptibility and explain the factor $4\pi$,
   which is a genuine hazard in reading the older literature.
7. **Estimate** the surface anomaly of a buried magnetised body and the moment
   required for a nanotesla-scale anomaly, and estimate the mean magnetisation of
   the core implied by the geomagnetic dipole.
8. **Verify** all of the above numerically.

## Prerequisites

- [02-07-02 Magnetostatics, Biot–Savart and Ampère's Law](./02-magnetostatics.md)
  — the dipole field, which is the kernel of every magnetic anomaly.
- [02-07-04 Faraday's Law, Induction and Eddy Currents](./04-em-induction.md) —
  why the core's field must be maintained, and how it varies in time.
- [02-07-03 Maxwell's Equations and Their Physical Meaning](./03-maxwell-equations.md)
  — $\nabla\cdot\mathbf B = 0$, which is what makes the anomaly formulation work.

## 1. Three fields, three meanings, three sets of units

Magnetism uses three vector fields where electrostatics uses two, and the
distinction is not cosmetic:

| Field | Symbol | SI unit | What it is |
|---|---|---|---|
| Magnetic flux density (magnetic induction) | $\mathbf B$ | tesla, T | what a magnetometer measures; what exerts force $\mathbf F = q\mathbf v\times\mathbf B$ |
| Magnetic field strength | $\mathbf H$ | A/m | the "applied" field, defined by free currents through $\nabla\times\mathbf H = \mathbf J$ |
| Magnetisation | $\mathbf M$ | A/m | magnetic dipole moment per unit volume of material |

The constitutive relation for a linear, isotropic material is

$$\boxed{\ \mathbf B = \mu_0(\mathbf H+\mathbf M)\ }
\qquad\text{with}\qquad
\mathbf M = \chi\mathbf H , \qquad \mu_r = 1 + \chi , \qquad \mathbf B = \mu_r\mu_0\mathbf H . \tag{1}$$

Three warnings that the rest of the lesson depends on:

1. **$\mathbf B$ and $\mathbf H$ have different dimensions and cannot be added.**
   $\mu_0$ carries the units. In vacuum $\mathbf H = \mathbf B/\mu_0$, and a
   50 µT field corresponds to $H = 39.79$ A/m — a number the demo prints, because
   getting from nanoteslas to A/m is the first step in every susceptibility
   calculation.
2. **$\chi$ is dimensionless but not unit-free across systems.** In SI, volume
   susceptibility $\chi$ is dimensionless and equation (1) holds as written. In
   the older cgs system the same physical material has
   $\chi_{\text{SI}} = 4\pi\chi_{\text{cgs}}$; a table value of 0.001 in cgs is
   0.0126 in SI. Nearly every pre-1980 rock-magnetism table is in cgs. **Always
   check the system before using a tabulated susceptibility.**
3. **$\chi$ is not a material constant.** It depends on mineralogy, grain size,
   temperature, field strength and frequency. Nominal values are a starting
   hypothesis; a specific rock must be measured.

## 2. Where magnetism comes from

**Diamagnetism.** Every atom has paired electron orbitals; an applied field
induces a small orbital current that *opposes* it. The effect is universal,
weak, temperature-independent, and gives a small negative susceptibility —
of order $-10^{-5}$ in SI for common rock-forming silicates such as quartz and
calcite. Diamagnetism is the baseline for "non-magnetic" rock.

**Paramagnetism.** Unpaired electron spins align partially with the applied field.
The alignment competes with thermal disorder, giving the **Curie law**

$$\chi = \frac{C}{T} , \qquad\text{or, with interactions, the Curie–Weiss law}\qquad
\chi = \frac{C}{T-\theta} , \tag{2}$$

with $C$ the Curie constant (material-specific, measured) and $\theta$ the Weiss
temperature. The susceptibilities are small and positive, typically
$10^{-5}$–$10^{-3}$ SI for iron-bearing silicates, and they *decrease* with
temperature — the opposite of the ferromagnetic behaviour below.

**Ferromagnetism.** Below a critical temperature the exchange interaction between
electron spins aligns them spontaneously, producing a large spontaneous
magnetisation. The critical temperature is the **Curie temperature** $T_C$, above
which the material is paramagnetic and follows (approximately) the Curie–Weiss
law. For the minerals that matter in rock magnetism, widely tabulated measured
values are approximately:

| Mineral | Curie (or Néel) temperature | Note |
|---|---|---|
| magnetite (Fe₃O₄) | ≈ 580 °C (≈ 853 K) | the dominant carrier of rock magnetism |
| hematite (Fe₂O₃) | ≈ 675 °C (≈ 948 K) | weakly magnetic, but chemically stable |
| pyrrhotite (Fe₁₋ₓS) | ≈ 320 °C (≈ 590 K) | common in sulphide-bearing rock |

These are measured mineral-physical properties; confirm them against a
mineral-physics or rock-magnetism reference before using them quantitatively,
because the exact values depend on composition, oxidation state and pressure.
Titanomagnetites, which are what most igneous rocks actually contain, have Curie
temperatures that fall as the titanium content rises — which is why
thermomagnetic curves are a standard rock-magnetic measurement rather than a
textbook constant.

**Ferrimagnetism and antiferromagnetism.** In a ferrimagnet (magnetite,
titanomagnetite) two or more magnetic sublattices are antiparallel but unequal in
magnitude, so a net spontaneous magnetisation survives. In an antiferromagnet
(hematite, above its spin-flop transition) the sublattices cancel almost exactly
and the susceptibility is small. Both orders disappear above the ordering
temperature (Curie for ferri-, Néel for antiferro-).

**Domains, hysteresis and the origin of remanence.** A large crystal does not
carry a single uniform moment; it subdivides into **magnetic domains** to reduce
the magnetostatic energy of the field it would otherwise produce. Domain
processes give the hysteresis loop, which is the source of everything that
matters practically:

- **saturation magnetisation** $M_s$ — the maximum a mineral can carry;
- **coercivity** $H_c$ — the field needed to reverse the magnetisation;
- **remanent magnetisation** $M_r$ — the magnetisation retained at zero applied
  field;
- **grain size** — single-domain (SD) grains are the most stable remanence
  carriers; multi-domain (MD) grains are magnetically soft with low coercivity;
  pseudo-single-domain (PSD) grains lie between.

Only three magnetic minerals are important in most rocks — magnetite (and its
titanium-substituted relatives), hematite and pyrrhotite — with greigite and
maghemite mattering in specific environments. Everything else is present in too
small a quantity or carries too little moment per volume.

## 3. Physical interpretation: induced versus remanent magnetisation

Every rock in the Earth's field carries both:

$$\mathbf M_{\text{total}} = \chi\mathbf H + \mathbf M_r . \tag{3}$$

The relative size is the **Koenigsberger ratio**

$$\boxed{\ Q = \frac{M_r}{\chi H}\ } . \tag{4}$$

- $Q\ll1$: **induced** magnetisation dominates. The anomaly maps the present field
  direction and the spatial distribution of susceptibility — i.e. the geology.
- $Q\gg1$: **remanent** magnetisation dominates. The anomaly records the field
  *at the time the rock acquired its remanence*, which may point in a completely
  different direction — the basis of palaeomagnetism, and the reason magnetic
  anomalies can look "wrong" relative to the present field.

The demo evaluates (4) for representative rock classes with nominal parameters
against a 50 µT ambient field ($H = 39.79$ A/m):

| Rock class (nominal) | $\chi$ (SI) | $M_r$ (A/m) | $M_i = \chi H$ (A/m) | $Q$ |
|---|---|---|---|---|
| sedimentary, weakly magnetic | $10^{-4}$ | 0.001 | 0.0040 | 0.25 |
| granite, typical | $10^{-3}$ | 0.05 | 0.0398 | 1.26 |
| basalt, typical | $5\times10^{-2}$ | 5.0 | 1.99 | 2.51 |
| metamorphic, magnetite-bearing | $10^{-2}$ | 1.0 | 0.398 | 2.51 |

**The values in this table are nominal order-of-magnitude ranges, not
measurements of any particular rock.** Susceptibility in nature spans from
$-10^{-5}$ (pure quartz) to about 1 SI (massive magnetite); remanent magnetisation
in nature spans from $10^{-4}$ A/m in weakly magnetised sediments to $10^1$ A/m or
more in some basalts. A rock with $Q>1$ can be *demagnetised* by a laboratory
alternating-field treatment and its induced response measured separately; that
separation is the standard rock-magnetic procedure, and it is the only reliable
way to determine which term dominates for a specific sample.

**Kinds of remanence** you will meet, in one line each: thermal remanent
magnetisation (TRM), acquired as igneous rock cools through its blocking
temperatures — the palaeomagnetic workhorse; depositional remanent magnetisation
(DRM) in sediments, aligned by the field as grains settle; chemical remanent
magnetisation (CRM), acquired as magnetic minerals grow during diagenesis; and
viscous remanent magnetisation (VRM), acquired slowly in the present field and
the main contaminant in older rocks.

## 4. Demagnetising factors, and why strong magnets look weak

The field inside a magnetised body is not the applied field: the body's own
magnetisation produces a **demagnetising field** opposing it,

$$\mathbf H_{\text{in}} = \mathbf H_0 - N\mathbf M , \tag{5}$$

where the demagnetising factor $N$ depends only on shape ($N = 1/3$ for a sphere,
$N\to0$ for a long needle along its axis, $N\to1$ for a thin sheet normal to its
plane). Combining (5) with $\mathbf M = \chi\mathbf H_{\text{in}}$ gives an
*effective* susceptibility measured from outside:

$$\boxed{\ \chi_{\text{eff}} = \frac{\chi}{1+N\chi}\ }
\qquad\xrightarrow[\chi\to\infty]{}\qquad \frac{1}{N} . \tag{6}$$

The consequence is quantitative and often surprising. For a sphere ($N = 1/3$) the
demo's table gives $\chi_{\text{eff}} = 0.75$ for $\chi = 1$ and only **2.31** for
$\chi = 10$. No matter how magnetic the material, a sphere cannot appear more
magnetic than $\chi_{\text{eff}} = 3$. This is why a body containing 5 % magnetite
does not have five times the anomaly of one containing 1 %: shape and internal
demagnetisation, not just mineral content, set the response. Any inversion for
susceptibility that ignores $N$ will overestimate the mineral content, sometimes
by an order of magnitude.

## 5. The Curie depth and the magnetic crust

Rock magnetism has a temperature ceiling. Below the depth at which the
temperature reaches the Curie temperature of magnetite, no mineral can retain
spontaneous magnetisation, and the rock contributes nothing to long-wavelength
anomalies. That depth — the **Curie depth** — is

$$z_C = \frac{T_C - T_{\text{surface}}}{\mathrm dT/\mathrm dz} , \tag{7}$$

if the geotherm is taken as linear with gradient $\mathrm dT/\mathrm dz$. With
$T_C = 580$ °C and a surface temperature of 10 °C:

| Geothermal gradient (°C/km) | Curie depth (km) |
|---|---|
| 10 | 57.0 |
| 15 | 38.0 |
| 20 | 28.5 |
| 25 | 22.8 |
| 30 | 19.0 |
| 40 | 14.3 |

**Read this table as an illustration of a formula, not as a statement about the
Earth.** Every entry depends on assumed values: the gradient is nominal here
(real gradients depend on heat flow, radiogenic heating and thermal conductivity,
and must be measured locally or modelled); the geotherm is almost never linear
over tens of kilometres; the Curie temperature depends on composition; and the
magnetic mineralogy may vanish before the temperature does. The Curie depth is
nonetheless a genuinely useful concept — the *bottom of the magnetic crust* — and
estimating it is a recognised geothermal-exploration technique, precisely because
a shallow Curie depth requires a high heat flow.

## 6. Anomalies: how much magnetisation do you need?

The surface anomaly of a buried magnetic body, approximated by a dipole of moment
$\mathbf m = \mathbf M V$ at depth $d$, follows from the dipole field of lesson
[02-07-02](./02-magnetostatics.md):

$$B_z = \frac{\mu_0}{4\pi}\frac{2m}{d^3}
\qquad\text{(directly above a vertically magnetised body).} \tag{8}$$

The demo's table:

| Volume (km³) | $M$ (A/m) | $m$ (A m²) | Depth (km) | $B_z$ (nT) |
|---|---|---|---|---|
| 1 | 1.0 | $10^{9}$ | 2 | 25.0 |
| 10 | 1.0 | $10^{10}$ | 2 | 250.0 |
| 100 | 1.0 | $10^{11}$ | 5 | 160.0 |
| 1 | 5.0 | $5\times10^{9}$ | 1 | 1000.0 |
| 1000 | 0.1 | $10^{11}$ | 10 | 20.0 |

The lesson: **a nanotesla-scale anomaly requires a moment of order
$10^{8}$–$10^{10}$ A m².** A cubic kilometre of rock magnetised at 1 A/m carries
$10^{9}$ A m² and gives 25 nT at 2 km. Aeromagnetic surveys detect magnetite-rich
plutons, dykes, ore bodies and buried topography — not individual magnetic
minerals, and not thin magnetised layers unless they are large in extent.

**How magnetised is the core?** Using the dipole moment from a nominal 30 000 nT
equatorial surface field, $m_\oplus = 7.76\times10^{22}$ A m², and the outer-core
volume $1.765\times10^{20}$ m³, the implied mean magnetisation is

$$M_{\text{core}} = \frac{m_\oplus}{V_{\text{core}}} \approx 440\ \mathrm{A/m}
\qquad\Longrightarrow\qquad
B_{\text{core}} \approx \mu_0M \approx 0.55\ \mathrm{mT} , \tag{9}$$

about 18 times the equatorial surface field. Dynamo models with core fields of
order 1 mT are consistent with this estimate. Note what kind of statement this
is: **not** a measurement of the core field — no instrument has ever been there —
but an inference that assumes a uniform magnetisation, a nominal dipole moment and
a nominal core radius. The measured *surface* field, the measured *remanent*
magnetisation in rocks, and the inferred core field are three different epistemic
categories and should never be mixed in a sentence.

## 7. Assumptions and regime of validity

| Assumption | Where it entered | What breaks outside it |
|---|---|---|
| Linear induced magnetisation ($\chi$ independent of $H$) | $\mathbf M = \chi\mathbf H$ | In situ $H\approx40$ A/m is far below the coercive fields of rock-forming minerals, so the linear form is safe; in the laboratory at kA/m it is not |
| Uniform magnetisation of each body | The dipole kernels, equations (8) | Large or strongly magnetic bodies have internal gradients; the anomaly then requires an integral over the body |
| The demagnetising tensor is a *constant* for the body | Equation (5) | True for an ellipsoid only; for an arbitrary shape $N$ varies from point to point and the internal field is non-uniform |
| Induced and remanent terms add without interacting | equation (3) | The remanence biases the internal field, so the two are coupled for strongly magnetic rock; the interaction is what the "effective" $\chi_{\text{eff}}$ only partly captures |
| Remanence is a fixed vector per grain population | The Koenigsberger ratio | VRM grows with time; CRM is acquired after deposition; the recorded direction can be a mixture |
| A single Curie temperature and a linear geotherm | Section 5 | Titanomagnetites have a range of Curie temperatures; geotherms are curved by radiogenic heating and by advection; both are routinely violated |
| SI bookkeeping | Section 8 | The older literature is in cgs, where $\chi_{\text{SI}} = 4\pi\chi_{\text{cgs}}$; a slip produces impossible rocks, which is the check to apply |
| The ambient field is the geomagnetic field of the present epoch | Every induced calculation | The rock may have recorded a different direction (Q > 1) or a different intensity; the palaeofield is the inferred quantity, not the input |

**The most useful habit from this lesson**: state, for every magnetic number, whether
it is *measured* (a field, a susceptibility of a sample, a Curie temperature), 
*inferred* (a dipole moment, a Curie depth, a mean core magnetisation) or *nominal*
(a typical rock property, a geotherm). The three are not interchangeable, and the
sentence "the magnetite content is 2 %" is only defensible if it is accompanied by
the assumed shape, the assumed $Q$, and the measured $\chi$.

## 8. Units, dimensional analysis and the cgs hazard

- $[\mathbf B] = \mathrm T = \mathrm{kg\,s^{-2}A^{-1}}$;
  $[\mathbf H] = \mathrm{A/m}$; $[\mathbf M] = \mathrm{A/m}$ ✓ (moment per volume,
  $\mathrm{A\,m^2/m^3}$).
- $[\mu_0] = \mathrm{T\,m/A} = \mathrm{H/m}$ ✓; equation (1) is dimensionally
  consistent: $\mu_0\mathbf M$ has units $\mathrm{(T\,m/A)(A/m)} = \mathrm T$ ✓.
- $\chi$ is dimensionless, so $Q$ in (4) is dimensionless ✓
  ($\mathrm{(A/m)/((dimensionless)(A/m))}$).
- $[B_z] = \mathrm{T\,m/A\cdot A\,m^2/m^3} = \mathrm T$ ✓ for equation (8).
- **The cgs conversion, worked once.** In cgs, $\mathbf B = \mathbf H + 4\pi\mathbf M$
  with $\mathbf B$ in gauss and $\mathbf H$, $\mathbf M$ in oersted/emu. Matching
  the physics gives
  $\chi_{\text{SI}} = 4\pi\chi_{\text{cgs}}$ for volume susceptibility, so
  $\chi_{\text{cgs}} = 0.01$ corresponds to $\chi_{\text{SI}} = 0.1257$, and
  $\chi_{\text{cgs}} = 1$ (a common threshold for "magnetic rock" in old papers)
  is $\chi_{\text{SI}} = 12.6$, which is not attainable by any natural rock.
  A factor-of-$4\pi$ error in susceptibility propagates directly into an
  estimated magnetite percentage, which is why this is worth memorising.
- **Saturation.** $\chi$ is only defined for induced magnetisation well below
  saturation. Magnetite saturates at a spontaneous magnetisation of order
  $10^{5}$ A/m (a measured mineral property, about 480 kA/m at room temperature);
  a field strong enough to saturate it ($H_c$ of order tens of kA/m) never occurs
  in the Earth's 40 A/m ambient field, so in situ the linear relation is safe. In
  the laboratory it is not.

## 9. Python demonstration

[`code/magnetisation_materials_demo.py`](./code/magnetisation_materials_demo.py)
verifies every claim above. Observed output:

```text
ambient B = 50 uT = 50000 nT
ambient H = B/mu0 = 39.7887 A/m
  Units are different and must not be conflated:
    [H] = A/m,   [M] = A/m,   [B] = T = kg s^-2 A^-1
    B = mu0 (H + M),  so  B = mu0 (1 + chi) H  and  mu_r = 1 + chi.
       chi       M (A/m)   B = mu0(1+chi)H (T)      B/B0   B - B0 (nT)
  -0.00001     -0.000398       4.999950000e-05   0.99999       -0.5000
   0.00010      0.003979       5.000500000e-05   1.00010        5.0000
   0.00100      0.039789       5.005000000e-05   1.00100       50.0000
   0.01000      0.397887       5.050000000e-05   1.01000      500.0000
   0.10000      3.978874       5.500000000e-05   1.10000     5000.0000
   1.00000     39.788736       1.000000000e-04   2.00000    50000.0000
```

```text
  geothermal gradient (C/km)    Curie depth (km)
                          10               57.00
                          25               22.80
                          40               14.25
```

```text
                        rock class       chi   M_r (A/m)   M_i (A/m)         Q
     sedimentary (weakly magnetic)   0.00010      0.0010    0.003979      0.25
                 granite (typical)   0.00100      0.0500    0.039789      1.26
                  basalt (typical)   0.05000      5.0000    1.989437      2.51
   metamorphic (magnetite-bearing)   0.01000      1.0000    0.397887      2.51
```

```text
   volume (km^3)   M (A/m)     m (A m^2)  depth (km)    B_z (nT)
               1      1.00     1.000e+09         2.0     25.0000
              10      1.00     1.000e+10         2.0    250.0000
             100      1.00     1.000e+11         5.0    160.0000
               1      5.00     5.000e+09         1.0   1000.0000
            1000      0.10     1.000e+11        10.0     20.0000
```

```text
  m_earth from B_equator = 30000 nT (NOMINAL) and R = 6371000 m: 7.758e+22 A m^2
  outer-core volume = 1.765e+20 m^3
  mean magnetisation M = m/V = 439.5 A/m
  implied mean field inside the core B = mu0 M = 0.552 mT = 552.2 uT
  surface equatorial field = 30.0 uT, i.e. 18 times smaller
```

```text
     chi    N = 0 (needle)    N = 1/3 (sphere)    N = 1 (thin sheet)
   0.001           0.00100             0.00100               0.00100
   0.010           0.01000             0.00997               0.00990
   0.100           0.10000             0.09677               0.09091
   1.000           1.00000             0.75000               0.50000
  10.000          10.00000             2.30769               0.90909
```

### What to observe

| Observation | Consequence |
|---|---|
| $H = 39.7887$ A/m for $B = 50$ µT | The conversion from the measured field to the field strength is the first step of every susceptibility calculation, and it is not a unit conversion in the trivial sense — $\mu_0$ does the work |
| $\chi = 10^{-5}$ changes the field by $-0.5$ nT, $\chi = 1$ by $+50\,000$ nT | The full geologically relevant range spans a field change from half a nanotesla to a factor of two — five orders of magnitude in anomaly, which is why magnetic surveying has such a large dynamic range |
| $\chi = 1$ doubles the field but $\chi = 0.1$ changes it by only 10 % | Anomalies are small perturbations for all realistic rocks; the linearisation in $\mu_r = 1+\chi$ is therefore always safe in situ |
| Curie depth falls from 57 km at 10 °C/km to 14.3 km at 40 °C/km | A shallow magnetic crust requires high heat flow: the geotherm and the magnetic mineralogy are coupled, which is the physical basis of Curie-depth geothermal exploration |
| $Q$ ranges from 0.25 (sediment) to 2.5 (basalt) for nominal parameters | Both induced and remanent terms are geologically common; neither can be assumed away without measurement |
| A $10^{9}$ A m² moment gives 25 nT at 2 km; $10^{11}$ A m² gives 20 nT at 10 km | Anomaly amplitude depends as strongly on depth as on moment ($1/d^3$), so depth estimates from magnetic data are powerful but also sensitive |
| The core estimate gives $M\approx440$ A/m and $B_{\text{core}}\approx0.55$ mT | The inference is internally consistent with dynamo models; note that every input to it is nominal |
| $\chi_{\text{eff}}$ for a sphere rises only from 0.75 to 2.31 as $\chi$ goes from 1 to 10 | Demagnetisation bounds the apparent susceptibility; ignoring $N$ is a first-order error in any mineral-content estimate |

> **Breaking exercise.** Take a body with $\chi = 0.05$ and compute its
> $\chi_{\text{eff}}$ for $N = 0$, $N = 1/3$ and $N = 1$. Then compute the anomaly
> at 1 km for all three, and explain why the *shape* of a magnetic body cannot be
> inverted from its anomaly without an assumption about $N$ — and why that
> ambiguity is the same in kind as the depth–magnetisation trade-off in the same
> inversion.

## 10. Common mistakes

1. **Adding or comparing $\mathbf B$ and $\mathbf H$.** Different dimensions;
   always write the units.
2. **Reading a cgs susceptibility as SI.** A factor of $4\pi$ — and, in the older
   literature, a further factor of $10^{-6}$ if the table is in emu/cm³ with a
   different normalisation of the moment definition. Check the system and the
   normalisation.
3. **Treating $\chi$ as a constant of the rock.** It depends on mineralogy, grain
   size, temperature, field amplitude and frequency.
4. **Assuming remanence scales with susceptibility.** It does not: $M_r$ depends
   on the domain state and on the rock's thermal history, not on $\chi$.
5. **Applying the Curie law to magnetite.** Magnetite is ferrimagnetic: its
   susceptibility *rises* as temperature falls below the Curie point in a way the
   Curie law does not describe. The Curie law describes paramagnets only.
6. **Ignoring the demagnetising factor.** Equation (6) can change $\chi_{\text{eff}}$
   by a factor of three or more for plausible shapes.
7. **Quoting the geomagnetic dipole moment as a constant.** It is time-varying
   (and currently decreasing); evaluate it from the current IGRF.
8. **Reporting a Curie depth without stating the gradient, the Curie temperature
   and the assumption of a linear geotherm.** It is a model output, not a
   measurement.
9. **Confusing the anomaly with the field.** A 25 nT "anomaly" is measured against
   a 50 000 nT background; forgetting the background makes the anomaly look
   physically impossible.
10. **Assuming induced magnetisation only.** In many igneous and metamorphic
    terrains $Q>1$, and an induced-only interpretation produces a *systematically
    wrong* anomaly pattern — not merely a noisy one.

## 11. Real-world applications

- **Magnetic surveying and interpretation.** Aeromagnetic and ground surveys map
  susceptibility contrasts (geology) and remanence contrasts (history). The dipole
  kernel of equation (8) is the basis of every depth estimate, and the induced/
  remanent ambiguity is the basis of every caveat
  ([07 Gravity and Geodesy](../../07-gravity-geodesy/README.md),
  [08 Geomagnetism and Electromagnetic Fields](../../08-geomagnetism-electromagnetism/README.md)).
- **Palaeomagnetism and magnetostratigraphy.** TRM/DRM recording of the field
  direction, used for plate reconstructions and for dating
  ([08-01-06 Palaeomagnetism](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/06-palaeomagnetism.md),
  [08-01-07 Rock Magnetism](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/07-rock-magnetism.md)).
- **Curie-depth geothermal exploration.** A shallow Curie depth implies high heat
  flow; magnetic depth estimates are a low-cost reconnaissance tool for geothermal
  prospects ([05-09 Geothermal](../05-thermodynamics/README.md)).
- **Mineral exploration.** Magnetite-rich skarns, banded iron formations, magmatic
  sulphide bodies and kimberlites all have diagnostic magnetic signatures.
- **Instrument design.** Fluxgate magnetometers rely on high-permeability cores;
  mu-metal shielding relies on the same physics; the choice of core material is a
  hysteresis-loop decision, not an electrical one
  ([08-02-01 Fluxgate Magnetometers](../../08-geomagnetism-electromagnetism/02-magnetic-instruments-and-surveys/01-fluxgate-magnetometers.md)).
- **Environmental magnetism.** Susceptibility is used as a rapid, cheap proxy for
  anthropogenic pollution and for palaeoclimate records in lake and marine
  sediments.
- **Geodynamo constraints.** The magnetic properties of the core (and therefore
  the electrical and thermal properties of iron at core conditions) bound dynamo
  models, and the palaeomagnetic record of the field's long-term behaviour is the
  observable they must reproduce.
- **Separation of induced and remanent components in the laboratory.** The
  standard procedure — measure susceptibility, then demagnetise and measure the
  remanence — is what makes $Q$ an observational quantity rather than a guess.

## 12. Further reading

- **Dunlop, D. J., & Özdemir, Ö. *Rock Magnetism: Fundamentals and Frontiers*
  (Cambridge University Press, 1997).** The definitive graduate text on domain
  theory, hysteresis, remanence mechanisms and the mineralogy behind Section 2.
  Level: graduate.
- **Butler, R. F. *Paleomagnetism: Magnetic Domains to Geologic Terranes*
  (Blackwell, 1992).** The measurements, the demagnetisation procedures and the
  field observations; the clearest bridge from Section 3 to practice. Level:
  advanced.
- **Tauxe, L. *Essentials of Paleomagnetism* (University of California Press,
  2010).** Modern, freely available treatment including the statistics of
  palaeomagnetic data. Level: advanced.
- **Blakely, R. J. *Potential Theory in Gravity and Magnetic Applications*
  (Cambridge University Press, 1995).** The anomaly kernels, depth estimation and
  the induced/remanent ambiguity as an inverse problem. Level: graduate.
- **Griffiths, D. J. *Introduction to Electrodynamics* (4th ed., Cambridge
  University Press, 2017).** The $\mathbf B$, $\mathbf H$, $\mathbf M$ relations
  and the demagnetising field, treated cleanly. Level: intermediate.
- **Purcell, E. M., & Morin, D. J. *Electricity and Magnetism* (3rd ed.,
  Cambridge University Press, 2013).** The physical origin of dia-, para- and
  ferromagnetism. Level: intermediate.
- **Jackson, J. D. *Classical Electrodynamics* (3rd ed., Wiley, 1999).** §5.9 for
  the macroscopic field definitions, and the boundary conditions that determine
  $N$. Level: graduate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [02 Magnetostatics, Biot–Savart and Ampère's Law](./02-magnetostatics.md) — the
  dipole field, and why a magnetised body is a distribution of dipoles.
- [06 EM Fields in Conductors: Skin Depth and Diffusion](./06-em-in-conductors.md)
  — how $\mu_r\neq1$ changes the skin depth.
- [02-08 Potential Theory](../08-potential-theory/README.md) — the harmonic
  machinery that magnetic anomalies share with gravity.
- [08 Geomagnetism and Electromagnetic Fields](../../08-geomagnetism-electromagnetism/README.md)
  — the module that takes this lesson into the main field, rock magnetism,
  palaeomagnetism and instrument design.
- [08-01-07 Rock Magnetism](../../08-geomagnetism-electromagnetism/01-earth-magnetic-field/07-rock-magnetism.md)
  — the same physics from the geological side, including magnetic mineralogy in
  detail.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the nominal geomagnetic parameters, and the warning that the dipole moment
  must not be quoted as a constant.

Exercises:
[`exercises/07-magnetisation-materials-exercises.md`](./exercises/07-magnetisation-materials-exercises.md)
and
[`exercises/07-magnetisation-materials-solutions.md`](./exercises/07-magnetisation-materials-solutions.md).

## Self-assessment checklist

Work through these without notes. Every item should be a clear "yes".

- [ ] I can state the units of $\mathbf B$, $\mathbf H$ and $\mathbf M$ and write
      equation (1) consistently. (Section 1)
- [ ] I can explain the physical origin of dia-, para-, ferro- and
      ferrimagnetism, and the temperature dependence of each. (Section 2)
- [ ] I can state the Curie law and the Curie–Weiss law and say which materials
      obey them. (Section 2)
- [ ] I can define the Koenigsberger ratio and explain which rocks are induced-
      and which remanence-dominated, with the caveat that the ranges are nominal.
      (Section 3)
- [ ] I can compute an effective susceptibility with a demagnetising factor and
      explain the saturation $\chi_{\text{eff}}\to1/N$. (Section 4)
- [ ] I can compute a Curie depth and list every assumption in the calculation.
      (Section 5)
- [ ] I can estimate the anomaly of a buried dipole and state the moment needed
      for a nanotesla-scale anomaly. (Section 6)
- [ ] I can convert a cgs susceptibility to SI and explain the factor $4\pi$.
      (Section 8)
- [ ] I can distinguish a measured, an inferred and a nominal magnetic quantity in
      a sentence about the Earth. (Section 6)
