---
id: 14-01-05
title: "Groundwater Chemistry and Salinity"
level: intermediate
prereqs: ["14-01-01", "14-01-02", "09-01-02"]
tags: [hydrology, hydrogeophysics, groundwater-chemistry, salinity, seawater-intrusion, charge-balance, archie]
---

# Groundwater Chemistry and Salinity

Water chemistry is where hydrogeology meets geophysics. The electrical
resistivity of a saturated rock is controlled by the conductivity of its pore
water, so a salinity map is a resistivity map; but resistivity also responds to
porosity and clay content, so the chemistry and the geophysics have to be
interpreted together. This lesson builds the chemical quantities that a
geophysical interpretation needs, and it refuses to treat any of them as a pure
measurement: TDS is an accounting convention, the "0.65 factor" is a regression,
and the calcite saturation index depends on activity coefficients that are models.

It also develops the two facts that decide how a salinity dataset is read.
**Chloride mixes conservatively and is therefore the tracer of choice**, while
**calcium and sodium do not mix conservatively in a clay-bearing aquifer**, so a
sample that has exchanged cations plots off the mixing line.

**All models and data in this module are SYNTHETIC.** The water analyses, mixing
fractions and exchanger capacity below are invented teaching values. Standard
reference constants (seawater composition, carbonate equilibrium constants,
Debye–Hückel parameters) are stated with units where they are used.

## Learning objectives

By the end of this lesson you will be able to:

1. **Convert** between mg L$^{-1}$ and meq L$^{-1}$ using equivalent weights, and
   **verify** a major-ion analysis with a charge balance.
2. **Distinguish** TDS from the sum of analysed ions and from an EC-derived
   estimate, and **state** what each is a measure of.
3. **Compute** hardness as CaCO$_3$ two ways and **explain** why the two agree.
4. **Compute** a seawater fraction from chloride and **propagate** it to TDS and
   density, including the density correction to hydraulic head.
5. **Derive** the carbonate speciation of a water from pH and alkalinity and
   **compute** a calcite saturation index with activity coefficients.
6. **Demonstrate** that cation exchange moves a sample off the conservative mixing
   line, and **quantify** by how much.
7. **Convert** a TDS into a water conductivity and a bulk resistivity, and
   **state** the ambiguity that makes a resistivity anomaly non-unique.

## Prerequisites

- [14-01-01 The Hydrologic Cycle and Water Balance](01-hydrologic-cycle.md) — the
  balance that a salinity budget constrains.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](02-aquifer-types-and-properties.md)
  — porosity and formation factor, which convert a water property into a rock
  property.
- [09-01-02 Archie's Law, Porosity and Saturation](../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md)
  — the empirical relation used to connect water resistivity to bulk resistivity.

---

## 1. Intuition: mixing, with reactions in the way

If you know the chemistry of two end-member waters, you can compute the chemistry
of any mixture — provided nothing reacts. In a real aquifer three things react:

1. **Mineral dissolution and precipitation.** Calcite, gypsum and halite dissolve
   and precipitate, changing Ca, SO$_4$ and Cl.
2. **Cation exchange.** Clay surfaces exchange Na for Ca and Mg on a
   charge-equivalent basis, in either direction depending on the water.
3. **Redox reactions.** Nitrate, sulfate, iron and manganese species are consumed
   and produced by microbial activity.

Geophysics sees the *result*: the total dissolved solids through the water
conductivity. So the practical chain is
**chemistry → TDS or salinity → water conductivity → bulk resistivity**, with a
reaction or an ambiguity hiding at every arrow. This lesson makes each arrow
explicit and states where each one fails.

## 2. Definitions, units and the arithmetic that goes with them

| Quantity | Symbol | Unit | Note |
|---|---|---|---|
| concentration | $c_i$ | mg L$^{-1}$ ($\approx$ g m$^{-3}$) | mass per volume of water |
| molar concentration | $m_i$ | mol L$^{-1}$ | mass / molar mass |
| equivalent weight | $E_i$ | mg meq$^{-1}$ | molar mass / $\lvert z_i\rvert$ |
| charge-equivalent concentration | $c_i/E_i$ | meq L$^{-1}$ | the currency of the charge balance |
| total dissolved solids | TDS | mg L$^{-1}$ | defined by an evaporation procedure or by an accounting rule |
| electrical conductivity | EC | µS cm$^{-1}$ | of the water, at a stated temperature |
| ionic strength | $I$ | mol L$^{-1}$ | $I = \tfrac{1}{2}\sum m_i z_i^{2}$ |
| activity coefficient | $\gamma_i$ | – | $a_i = \gamma_i m_i$ |
| seawater fraction | $f_{\text{sw}}$ | – | a mixing fraction, not a salinity |

**Equivalent weights** are the molar mass divided by the absolute charge:
$E = M/\lvert z\rvert$. For the major ions used below, in mg meq$^{-1}$:
Ca 20.04, Mg 12.15, Na 22.99, K 39.10, HCO$_3$ 61.02, SO$_4$ 48.03, Cl 35.45.
(For sulfate the molar mass 96.06 g mol$^{-1}$ divided by $z = 2$ gives
48.03 mg meq$^{-1}$ — the factor of two is the most commonly forgotten thing in
this lesson, because the number 96 appears on the lab sheet and 48 in the
calculation.)

**TDS** has three different definitions in circulation, and they are not
interchangeable:

- the **residue on evaporation** at a stated temperature (a laboratory
  procedure; it loses bicarbonate as CO$_2$ and can gain water of hydration);
- the **sum of analysed ions** plus silica (an accounting rule);
- **$k \times \mathrm{EC}$** with $k$ calibrated per site (a regression).

The three can differ by tens of per cent. State which one you mean.

## 3. The charge balance

Water is electrically neutral, so the equivalents of cations must equal the
equivalents of anions:

$$\sum_{\text{cations}}\frac{c_i}{E_i} = \sum_{\text{anions}}\frac{c_j}{E_j}.$$

Every laboratory analysis is checked with the **charge balance error**

$$\mathrm{CBE} = \frac{\sum c_{\text{cat}} - \sum c_{\text{an}}}{%
\sum c_{\text{cat}} + \sum c_{\text{an}}} \times 100\%,$$

and the usual acceptance convention is $\lvert \mathrm{CBE}\rvert < 5\%$ (tighter
for high-ionic-strength waters, looser — up to 10% — for very dilute ones, where
analytical errors are a larger fraction of each term). Two things must be said:

- $\mathrm{CBE} \approx 0$ is **not** evidence that the analysis is right; it only
  means the numbers are internally consistent. A missing ion, a wrong
  charge-assignment, and a laboratory calibration error can cancel.
- A large CBE is *information*: a missing species (often NO$_3$, Fe, Mn,
  SiO$_2$ at high pH), a charge typo, or a genuinely unusual water.

**Synthetic analysis, worked.** Ca 42.0, Mg 13.0, Na 45.0, K 4.0, HCO$_3$ 210.0,
SO$_4$ 40.0, Cl 25.0 mg L$^{-1}$:

| Species | mg L$^{-1}$ | $E$ (mg meq$^{-1}$) | meq L$^{-1}$ |
|---|---|---|---|
| Ca | 42.0 | 20.04 | 2.0958 |
| Mg | 13.0 | 12.15 | 1.0700 |
| Na | 45.0 | 22.99 | 1.9574 |
| K | 4.0 | 39.10 | 0.1023 |
| HCO$_3$ | 210.0 | 61.02 | 3.4415 |
| SO$_4$ | 40.0 | 48.03 | 0.8328 |
| Cl | 25.0 | 35.45 | 0.7052 |

$$\sum c_{\text{cat}} = 5.2254\ \mathrm{meq\,L^{-1}}, \qquad
\sum c_{\text{an}} = 4.9795\ \mathrm{meq\,L^{-1}},$$
$$\mathrm{CBE} = \frac{0.2459}{10.2049} \times 100\% = +2.41\%.$$

Within the 5% convention, so acceptable. The TDS accounting rule gives
$$42.0 + 13.0 + 45.0 + 4.0 + 210.0 + 40.0 + 25.0 + 15.0\ (\mathrm{SiO_2})
= 394.0\ \mathrm{mg\,L^{-1}},$$
while the synthetic EC of $610\ \mathrm{\mu S\,cm^{-1}}$ with the stated factor
0.65 gives $396.5\ \mathrm{mg\,L^{-1}}$ — agreement to $+0.6\%$. That agreement is
a property of the *chosen* factor, not of the physics: the factor depends on the
ionic proportions, the temperature of the EC measurement (conductivity rises
about 2% per $^\circ$C) and the TDS definition used.

### 3.1 Hardness

Hardness is the divalent-cation content, expressed as if it were CaCO$_3$:

$$\text{hardness} = 2.497\,\mathrm{Ca} + 4.118\,\mathrm{Mg}\
[\mathrm{mg\,L^{-1}\ as\ CaCO_3}],$$

with Ca and Mg in mg L$^{-1}$. The factors are equivalent-weight ratios:
$100.09/40.08 = 2.497$ and $100.09/24.31 = 4.118$. Check against the equivalents:

$$\frac{42.0}{20.04} + \frac{13.0}{12.15} = 2.0958 + 1.0700
= 3.1658\ \mathrm{meq\,L^{-1}},$$

and 1 meq L$^{-1}$ of divalent hardness as CaCO$_3$ is $100.09/2 = 50.04\
\mathrm{mg\,L^{-1}}$, so
$3.1658 \times 50.04 = 158.4\ \mathrm{mg\,L^{-1}}$ — identical to
$2.497(42.0) + 4.118(13.0) = 104.9 + 53.5 = 158.4$. **Both routes give the same
number because both are the same equivalent-weight arithmetic.** Classification
thresholds ("soft", "hard") are conventions that differ between jurisdictions;
report the number and the convention.

## 4. Salinity and seawater intrusion

Coastal aquifers are the standard application: seawater has a nearly constant
composition, so a measured chloride concentration converts directly to a
**seawater fraction**

$$f_{\text{sw}} = \frac{\mathrm{Cl}_{\text{sample}} - \mathrm{Cl}_{\text{fresh}}}
{\mathrm{Cl}_{\text{seawater}} - \mathrm{Cl}_{\text{fresh}}},$$

with the standard seawater chloride $19{,}350\ \mathrm{mg\,L^{-1}}$ and TDS
$35{,}000\ \mathrm{mg\,L^{-1}}$. With a synthetic fresh end member
($\mathrm{Cl} = 25$, TDS $= 394\ \mathrm{mg\,L^{-1}}$):

| Cl (mg L$^{-1}$) | $f_{\text{sw}}$ | TDS (mg L$^{-1}$) | density (kg m$^{-3}$) |
|---|---|---|---|
| 25 | 0.0000 | 394.0 | 1000.28 |
| 100 | 0.0039 | 528.3 | 1000.37 |
| 250 | 0.0116 | 796.9 | 1000.56 |
| 1000 | 0.0505 | 2140.0 | 1001.50 |
| 2500 | 0.1281 | 4826.1 | 1003.38 |
| 19,350 | 1.0000 | 35,000 | 1024.50 |

with density from the linear model
$\rho \approx 1000 + 0.7\,S\ \mathrm{kg\,m^{-3}}$ ($S$ in g kg$^{-1}$, i.e.
TDS/1000 here). Three points deserve emphasis:

1. **A seawater fraction of 1.2% almost doubles the TDS** (394 → 797 mg L$^{-1}$).
   The first per cent of intrusion is the largest change a fresh water ever sees,
   which is why chlorides of a few hundred mg L$^{-1}$ are already a signal.
2. **Chloride is the tracer to use.** It is conservative in most aquifers, it is
   abundant, and it is cheap. Sodium, calcium, sulfate and bicarbonate are all
   reactive somewhere.
3. **Density matters for head.** The density excess of 3.4 kg m$^{-3}$ at
   $f_{\text{sw}} = 0.13$ corresponds to an equivalent-freshwater head correction
   of $(\Delta\rho/\rho_w) z \approx 0.0034 \times z$; over a 30 m screen that is
   0.10 m of head — small, but comparable with the seasonal signal, and it grows
   without limit as salinity rises. In a saline aquifer, always report how head
   was defined (see [03 §1.1](03-hydraulic-head-darcy.md)).

## 5. Carbonate equilibrium: alkalinity, speciation and saturation

The carbonate system sets pH, controls mineral scaling, and is the reason
alkalinity is measured even though nobody drinks it. With

$$\mathrm{CO_2(aq)} \rightleftharpoons \mathrm{HCO_3^{-}} + \mathrm{H^{+}},
\quad K_{a1} = 10^{-6.35}; \qquad
\mathrm{HCO_3^{-}} \rightleftharpoons \mathrm{CO_3^{2-}} + \mathrm{H^{+}},
\quad K_{a2} = 10^{-10.33},$$

at $25\ ^\circ\mathrm{C}$, the **alkalinity** (as meq L$^{-1}$) is, to an excellent
approximation for pH between 6 and 9,

$$\mathrm{Alk} \approx [\mathrm{HCO_3^{-}}] + 2[\mathrm{CO_3^{2-}}]
+ [\mathrm{OH^{-}}] - [\mathrm{H^{+}}]
\approx [\mathrm{HCO_3^{-}}]\left(1 + 2\frac{K_{a2}}{[\mathrm{H^{+}}]}\right).$$

Given pH you can therefore solve for both species:

$$[\mathrm{HCO_3^{-}}] = \frac{\mathrm{Alk}}{1 + 2K_{a2}/[\mathrm{H^{+}}]},
\qquad [\mathrm{CO_3^{2-}}] = [\mathrm{HCO_3^{-}}]\frac{K_{a2}}{[\mathrm{H^{+}}]}.$$

The **calcite saturation index** compares the ion activity product with the
solubility product,

$$\mathrm{SI} = \log_{10}\frac{a_{\mathrm{Ca^{2+}}}\,a_{\mathrm{CO_3^{2-}}}}
{K_{sp}}, \qquad K_{sp} = 10^{-8.48}\ (\mathrm{mol\,L^{-1}})^{2}\
\text{at } 25\ ^\circ\mathrm{C},$$

with activities $a_i = \gamma_i m_i$ and the **extended Debye–Hückel** expression

$$\log_{10}\gamma_i = \frac{-A z_i^{2}\sqrt{I}}{1 + B a_i \sqrt{I}},
\qquad A = 0.509,\ B = 0.328\ \text{(per \AA)}\ \text{at } 25\ ^\circ\mathrm{C}.$$

$\mathrm{SI} < 0$ means the water can dissolve calcite; $\mathrm{SI} > 0$ means it
will precipitate it. The activities are not optional: at $I = 0.0071$ mol L$^{-1}$
the synthetic water gives $\gamma_{\mathrm{Ca^{2+}}} = 0.707$ and
$\gamma_{\mathrm{CO_3^{2-}}} = 0.698$, so ignoring them biases SI by
$\log_{10}(0.707 \times 0.698) = -0.307$ — a third of a log unit, which is the
difference between "undersaturated" and "about saturated".

**Synthetic water (Ca 42 mg L$^{-1}$, alkalinity 3.4415 meq L$^{-1}$,
$I = 0.00710$ mol L$^{-1}$):**

| pH | $[\mathrm{HCO_3^-}]$ (mmol L$^{-1}$) | $[\mathrm{CO_3^{2-}}]$ (µmol L$^{-1}$) | SI (calcite) |
|---|---|---|---|
| 6.8 | 3.4395 | 1.015 | $-0.800$ |
| 7.0 | 3.4383 | 1.608 | $-0.601$ |
| 7.2 | 3.4364 | 2.547 | $-0.401$ |
| 7.4 | 3.4334 | 4.034 | $-0.201$ |
| 7.6 | 3.4287 | 6.385 | $-0.002$ |
| 8.0 | 3.4096 | 15.948 | $+0.396$ |

**Worked line, pH 7.2.** $[\mathrm{H^+}] = 10^{-7.2} = 6.310 \times 10^{-8}$ and
$K_{a2}/[\mathrm{H^+}] = 4.677 \times 10^{-11}/6.310 \times 10^{-8}
= 7.414 \times 10^{-4}$, so

$$[\mathrm{HCO_3^-}] = \frac{3.4415 \times 10^{-3}}{1 + 2(7.414 \times 10^{-4})}
= 3.4364 \times 10^{-3}\ \mathrm{mol\,L^{-1}},$$
$$[\mathrm{CO_3^{2-}}] = 3.4364 \times 10^{-3} \times 7.414 \times 10^{-4}
= 2.547 \times 10^{-6}\ \mathrm{mol\,L^{-1}},$$
$$m_{\mathrm{Ca}} = 42.0 \times 10^{-3}/40.08 = 1.048 \times 10^{-3}\
\mathrm{mol\,L^{-1}},$$
$$\mathrm{IAP} = 0.7067(1.048 \times 10^{-3}) \times 0.6975(2.547 \times
10^{-6}) = 1.316 \times 10^{-9},$$
$$\mathrm{SI} = \log_{10}\frac{1.316 \times 10^{-9}}{3.311 \times 10^{-9}}
= -0.401.$$

Saturation is reached at **pH 7.602** for this water, found by bisection on the SI
function. The sensitivity is the practical message: $[\mathrm{CO_3^{2-}}]$ is
proportional to $10^{\mathrm{pH} - \mathrm{p}K_{a2}}$, so a 0.2-unit pH error moves
SI by 0.2 — the same as a factor of 1.6 in calcium. **A saturation index is only as
good as its pH measurement.**

## 6. Ion exchange: the mixture that leaves the mixing line

Clay and zeolite surfaces hold cations and exchange them on a charge-equivalent
basis. The exchange of Na$^+$ for Ca$^{2+}$ releases one Ca$^{2+}$ for every two
Na$^+$: **the charge balances, but the mass does not.** That single sentence is
enough to understand most confusing salinity datasets.

**Synthetic example.** The freshwater of Section 3 is mixed with seawater to
$f_{\text{sw}}$, then equilibrated with a clay of exchange capacity
$1.20\ \mathrm{meq\,L^{-1}}$ that takes up Ca and releases Na. Using standard
seawater end members (Ca 400, Na 10,800 mg L$^{-1}$):

| $f_{\text{sw}}$ | Ca measured (mg L$^{-1}$) | Ca on the mixing line | Na measured | Na on the mixing line |
|---|---|---|---|---|
| 0.01 | 21.5 | 45.6 | 180.1 | 152.6 |
| 0.05 | 35.9 | 59.9 | 610.3 | 582.8 |
| 0.10 | 53.8 | 77.8 | 1148.1 | 1120.5 |

At $f_{\text{sw}} = 0.05$ the calcium is **40.1% below** the conservative mixing
line while sodium is only 4.7% above it. The apparent percentages look wildly
asymmetric, and the reason is quantitative: the exchange moved 1.20 meq L$^{-1}$ of
charge, which is 24.0 mg L$^{-1}$ of Ca (a 40% change on a pool of 60 mg L$^{-1}$)
but only 27.6 mg L$^{-1}$ of Na (a 4.7% change on a pool of 583 mg L$^{-1}$).

Two consequences:

- **Reading a mixing fraction from Ca is invalid** in a clay-bearing aquifer, and
  the error is not a small correction.
- **A conservative tracer is required** to verify that a sample is a mixture at
  all. Chloride (and, with care, bromide) does this job. If Cl and Na both fit a
  seawater-mixing line but Ca does not, the interpretation is exchange, not
  intrusion — a diagnosis that changes the management response completely.

This is a non-uniqueness in the chemistry, exactly parallel to the $R/K$ ambiguity
of [03](03-hydraulic-head-darcy.md): a single number (Ca) is consistent with a
family of processes.

## 7. The bridge to geophysics

The chain from chemistry to a resistivity measurement is

$$\text{TDS} \xrightarrow{\text{calibration}} \sigma_w
\xrightarrow{\text{Archie}} \rho_{\text{bulk}}.$$

For the synthetic calibration $\sigma_w = 0.15\,(\text{TDS in g L}^{-1})$
[S m$^{-1}$] and Archie with $a = 1$, $m = 2$, $n = 2$, $S_w = 1$,
$\phi = 0.30$:
$\rho_{\text{bulk}} = a\rho_w/(\phi^{m}S_w^{n}) = \rho_w/0.09$:

| TDS (mg L$^{-1}$) | $\sigma_w$ (S m$^{-1}$) | $\rho_w$ ($\Omega$ m) | $\rho_{\text{bulk}}$ ($\Omega$ m) |
|---|---|---|---|
| 394 | 0.0591 | 16.92 | 188.0 |
| 800 | 0.1200 | 8.33 | 92.6 |
| 5,000 | 0.7500 | 1.33 | 14.8 |
| 35,000 | 5.2500 | 0.19 | 2.12 |

A factor of ten in salinity is a factor of ten in bulk resistivity, which is a
factor of 100 in the measured resistivity signal relative to typical
noise — this is why ERT and EM are the workhorse methods for salinity. The price
is the ambiguity, and it is severe: the same bulk resistivity 188 $\Omega$ m can
also arise from $\phi = 0.24$ at the same salinity, or from $\phi = 0.30$ with a
clay fraction adding surface conduction, or from partial saturation. **A
resistivity anomaly is not a salinity; it becomes one only when porosity and clay
content are constrained independently** — which is precisely the assignment of
[module 14-02](../02-hydrogeophysics-methods/README.md).

## 8. Python demonstration

`code/groundwater_chemistry_demo.py` prints all of the above with units. It:

1. converts the synthetic analysis to meq L$^{-1}$, reports
   $\mathrm{CBE} = +2.41\%$, and compares the ion-sum TDS (394.0 mg L$^{-1}$) with
   the EC-derived value (396.5 mg L$^{-1}$);
2. computes hardness two ways, both giving 158.4 mg L$^{-1}$ as CaCO$_3$;
3. tabulates $f_{\text{sw}}$, TDS and density from Cl;
4. solves the carbonate speciation and tabulates SI against pH, locating
   saturation at pH 7.602 by bisection;
5. quantifies the exchange displacement at three mixing fractions;
6. converts TDS to $\sigma_w$ and to $\rho_{\text{bulk}}$ for four salinities;
7. verifies the charge closure, the Debye–Hückel limit
   ($\gamma \to 1$ as $I \to 0$) and the mixing mass balance.

```bash
cd 14-hydrology-hydrogeophysics/01-hydrology-fundamentals/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python groundwater_chemistry_demo.py
```

## 9. Assumptions and regime of validity

1. **Charge balance assumes every significant ion is analysed.** Missing nitrate,
   iron, manganese, ammonium or organic anions inflate the CBE and are common in
   polluted and anoxic waters.
2. **The linear mixing law assumes conservative behaviour.** It is exact for a
   conserved species and wrong for every reactive one.
3. **The seawater end member is assumed constant.** Real seawater varies with
   evaporation and freshwater input; the standard composition is an approximation
   that must be justified where the site is estuarine.
4. **The carbonate constants are for $25\ ^\circ\mathrm{C}$ and low ionic
   strength.** $K_{a1}$, $K_{a2}$ and $K_{sp}$ all shift with temperature (typically
   a few tenths of a log unit over $10\ ^\circ\mathrm{C}$) and the activity model
   degrades above $I \approx 0.1$ mol L$^{-1}$, i.e. above about 1% seawater.
   Brine chemistry needs a Pitzer-type model.
5. **The TDS–EC relation is a regression.** It must be calibrated locally and it
   fails wherever the ionic proportions differ from the calibration set.
6. **Exchange is represented by a single capacity and selectivity.** Real
   exchangers have a composition-dependent selectivity, so the exchanged amount is
   a *bounded family*, not a number.
7. **The density model is linear.** It is good to a few tenths of a kg m$^{-3}$ in
   the oceanographic range and must not be extrapolated to brines.

## Mastery checkpoint

A synthetic sample reports Ca 120, Mg 30, Na 254, K 8, HCO$_3$ 180, SO$_4$ 90,
Cl 500, SiO$_2$ 12 mg L$^{-1}$.

**(a)** Compute the meq L$^{-1}$ of every ion and the charge balance error; is the
analysis acceptable? **(b)** Compute the TDS by the ion sum. **(c)** Compute
$f_{\text{sw}}$ from chloride and the TDS expected on a conservative mixing line
with the fresh end member of Section 4. **(d)** Compute the hardness as CaCO$_3$.
**(e)** Classify the water by its dominant ions and state, with one number, whether
a simple seawater-mixing explanation accounts for the sodium. **(f)** Compute the
bulk resistivity at $\phi = 0.30$ with the stated calibration, and state what
additional measurement you would need before calling a resistivity low here an
intrusion.

## Common pitfalls

1. **Forgetting the factor of two for divalent ions.** 96.06/2 = 48.03 for
   sulfate; using 96 doubles the anion sum and destroys the charge balance.
2. **Treating an EC-derived TDS as a measurement.** It is a calibrated regression.
3. **Reading a salinity from a reactive ion.** Ca, Na, SO$_4$ and HCO$_3$ all react;
   chloride is the tracer.
4. **Ignoring the temperature of a conductivity measurement.** Roughly 2% per
   $^\circ$C, which is comparable with the 1% salinity changes that matter for
   intrusion.
5. **Computing a saturation index without activities.** A third of a log unit at
   $I = 0.007$, and much more in a brine.
6. **Using a fresh-water head in a saline aquifer.** Density differences produce
   real head errors that grow with depth and salinity.
7. **Assuming that a low bulk resistivity means saline water.** Porosity, clay
   content and saturation all do the same thing.

## Related modules

- [03 Hydraulic Head, Darcy's Law and Groundwater Flow](03-hydraulic-head-darcy.md)
  — the head definition that density breaks.
- [09-01-02 Archie's Law, Porosity and Saturation](../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md)
  — the conversion from water to bulk resistivity used in Section 7.
- [02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) — how
  salinity is mapped, and how the porosity ambiguity is reduced.
- [01 ERT for Aquifer Characterisation and Salinity Mapping](../02-hydrogeophysics-methods/01-ert-for-hydrology.md)
  — the survey design that uses the resistivity contrast computed in Section 7.
- [04-06-04 Aquifer Types and Groundwater Occurrence](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)
  — the geological setting of coastal aquifers.

## Code and exercises

- Demonstration: [`code/groundwater_chemistry_demo.py`](code/groundwater_chemistry_demo.py)
- Exercises: [`exercises/05-groundwater-chemistry-exercises.md`](exercises/05-groundwater-chemistry-exercises.md)
- Worked solutions: [`exercises/05-groundwater-chemistry-solutions.md`](exercises/05-groundwater-chemistry-solutions.md)
