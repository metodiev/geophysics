---
id: 04-03-04
title: "Sedimentary Basins: Formation, Fill and Subsidence"
level: intermediate
prereqs: ["04-03-02", "02-05-01"]
estimated_minutes: 90
tags: [basins, subsidence, isostasy, backstripping, stretching]
---

# Sedimentary Basins: Formation, Fill and Subsidence

A sedimentary basin is a place where the lithosphere has been made able to hold a
thickness of sediment. Everything else — the facies, the sequences, the
unconformities — is a consequence of that capacity being created, filled, and
sometimes destroyed.

The quantitative content of basin analysis is therefore a **subsidence
history**, and the central skill is not computing it but **decomposing** it. The
total subsidence recorded by a stratigraphic column contains at least four
contributions: the tectonic driving mechanism, the isostatic response to the
sediment and water load, the compaction of the sediment as it buried itself, and
changes in water depth or sea level. Only the first is a tectonic signal. A
subsidence curve that has not separated the other three is a curve about density
and porosity as much as about tectonics.

This lesson builds the two halves of the decomposition. It models the tectonic
mechanism with the uniform-stretching model, in which the lithosphere is thinned
and then cools, and it removes the loading and compaction contributions by
**backstripping**. It then does the part that most treatments skip: it quantifies
how much of each answer is a consequence of the parameters chosen.

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why thinning the lithosphere creates space, and separate the
   instantaneous (crustal-thinning) subsidence from the thermal subsidence that
   follows.
2. **Solve** the one-dimensional heat-conduction problem for a stretched
   lithosphere numerically, and verify the solver against a case with an exact
   solution.
3. **State** why the familiar single-exponential law
   $S(t) = E_0(1 - e^{-t/\tau})$ is an approximation, identify the modes it
   discards, and quantify the error it makes.
4. **Invert** an observed total subsidence for a stretching factor, and state why
   one number does not determine a history.
5. **Backstrip** a stratigraphic column: decompact each unit, remove the sediment
   and water load, and report a water-loaded tectonic subsidence.
6. **Report** the sensitivity of a backstripped curve to the porosity model and
   the grain density, and say why that sensitivity is usually comparable to the
   tectonic signal.
7. **Distinguish** accommodation, sediment supply and water depth, and state what
   each controls in the stratigraphic record.

## Prerequisites

- [02 Stratigraphic Principles and Relative Dating](./02-stratigraphic-principles.md)
  — the column that a subsidence history is extracted from.
- [04-01-05 Density, Porosity, Permeability and Elastic Properties](../01-earth-structure/05-rock-physics-basics.md)
  — porosity, density and the relations between them.
- [02-05-01 The First Law, State Functions and the Energy Balance](../../02-physics/05-thermodynamics/02-first-law.md)
  — the energy bookkeeping that a heat-conduction calculation is.
- The geological context of the mechanisms is in
  [04-02-02 Divergent, Convergent and Transform Boundaries](../02-plate-tectonics/02-plate-boundaries.md).

## 1. Why thinning creates space

Consider a lithospheric column with a crust of thickness $t_c$, crustal density
$\rho_c$, mantle density $\rho_m$, and a load (water or sediment) of density
$\rho_L$ on top. If the crust is thinned from $t_c$ to $t_c/\beta$ with
$\beta > 1$ — the lithosphere stretched by a factor $\beta$ — the column contains
less light crust and more dense mantle. Isostatic balance requires the surface to
drop.

Requiring the pressure at the depth of the original crustal base to be unchanged
gives the **instantaneous subsidence**

$$S_i = t_c\left(1 - \frac{1}{\beta}\right)\frac{\rho_m - \rho_c}{\rho_m -
\rho_L}. \tag{1}$$

Two things about equation (1) are worth extracting. The factor
$(1 - 1/\beta)$ says that **the thinning fraction is the whole driver**: no
thinning, no basin. And the density contrast $(\rho_m - \rho_c)/(\rho_m - \rho_L)$
is a small number — of order 0.25 for a water load with $\rho_c = 2800$ and
$\rho_m = 3300$ kg m$^{-3}$ — so the surface drops by only a quarter of the
thickness removed. Isostasy is a very efficient damper.

Thinning also brings hot mantle rock closer to the surface, so the geotherm
steepens and the lithosphere is hotter, and therefore lighter, than before. As it
cools back towards its pre-rift conductive profile, the column contracts and the
basin subsides further. That is **thermal subsidence**, and it is what gives a
rifted margin its long, slow, exponentially decaying post-rift record.

## 2. The thermal subsidence, and the closed form that is not exact

Model the cooling as one-dimensional heat conduction in a column of thickness $a$
with a thermal diffusivity $\kappa$, a surface held at $0\,^\circ$C and a base
held at the asthenospheric temperature $T_m$. Immediately after stretching, the
geotherm is stretched with the lithosphere:

$$T(z, 0) = \begin{cases} T_m \,\beta z / a, & z \le a/\beta,\\ T_m, & z >
a/\beta, \end{cases} \tag{2}$$

with $z$ measured downwards. The final steady profile is $T_\infty(z) = T_m z/a$.
The perturbation $\theta = T - T_\infty$ satisfies $\theta_t = \kappa\theta_{zz}$
with $\theta = 0$ at both ends, so it has a sine series in $z$ whose $n$-th mode
decays as $e^{-n^2 t/\tau}$ with

$$\tau = \frac{a^2}{\pi^2\kappa}. \tag{3}$$

The subsidence is proportional to the column integral of the temperature change,
because a column that has cooled by $\delta T$ has gained density
$\alpha\rho_m\delta T$ and therefore sinks by the integral of that divided by
$(\rho_m - \rho_L)$:

$$S(t) = \frac{\alpha\rho_m}{\rho_m - \rho_L}\int_0^a \left[\theta(0) -
\theta(t)\right]\mathrm{d}z. \tag{4}$$

Carrying out the integral for large $t$ gives the asymptotic thermal subsidence

$$E_0 = \frac{\alpha\rho_m T_m a}{2(\rho_m - \rho_L)}\left(1 -
\frac{1}{\beta}\right), \tag{5}$$

which contains the same $(1 - 1/\beta)$ as equation (1): **both terms scale with
the fraction of the lithosphere removed.**

Now the part that is usually glossed. It is common to write the whole thing as

$$S_{\text{thermal}}(t) = E_0\left(1 - e^{-t/\tau}\right), \tag{6}$$

and equation (6) is **not the solution**. It is the first-mode truncation of the
series, and it is a good approximation only because the higher modes decay much
faster. Equation (2) is not a single sine mode: it has a kink at $z = a/\beta$,
and a kink requires higher modes. The demo computes the odd-mode weights of the
expansion:

```text
  mode n   1/tau_n (Ma^-1)      weight   cumulative
       1           0.01993     1.03205      1.03205
       3           0.17940    -0.03822      0.99383
       5           0.49834     0.00826      1.00208
       7           0.97674    -0.00301      0.99907
       9           1.61461     0.00142      1.00049
      11           2.41195    -0.00078      0.99971
```

The weights alternate in sign and decay as $1/n^3$; the first mode carries slightly
more than the whole, the third mode subtracts about 4 per cent, and the fifth adds
about 0.8 per cent. Mode $n$ decays $n^2$ times faster than mode 1, so the
correction is transient. Quantitatively, for $\beta = 2$:

```text
   t (Ma)  numeric (m)   exact (m)  numeric-exact   1-mode law   law-exact
      0.0          0.0         0.0            0.0          0.0         0.0
      5.0        160.1       160.1            0.0        188.0        27.9
     10.0        318.6       318.6            0.0        358.2        39.6
     25.0        740.1       740.1            0.0        777.8        37.7
     50.0      1,226.9     1,226.9            0.0      1,250.3        23.4
    100.0      1,703.2     1,703.2            0.0      1,711.8         8.7
    200.0      1,943.9     1,943.9            0.0      1,945.0         1.2
  worst |numeric - exact|   : 5.416e-03 m (2.733e-06 of E0)
  worst |1-mode law - exact|: 39.6 m (2.00% of E0)
```

Two separate results live in that table, and they should be kept apart. The
numerical solution matches the exact sine-series solution to a part in $10^5$ of
$E_0$, which says the discretisation and the isostatic bookkeeping are both
correct. And equation (6), the form quoted in most textbooks, errs by up to 40 m
here — 2 per cent of the total — because it discards the modes that make the
first tens of millions of years of post-rift subsidence faster than a single
exponential. **Quote the closed form, but know it is a truncation**, and know the
size of the error before using the early part of the curve for anything.

## 3. Verification of the solver, which is where the confidence comes from

Before trusting any of §2, the same code is run on a case with a known solution. If
the perturbation is set to a single sine mode, $\theta = \Theta\sin(\pi z/a)$, then
equation (4) requires the fractional subsidence to be exactly
$1 - e^{-t/\tau}$:

```text
  n cells   dt (Ma)   t (Ma)     numeric   1-exp(-t/tau)       error
      100     0.020     25.0    0.392422        0.392387    3.49e-05
      400     0.001     25.0    0.392464        0.392462    2.18e-06
      400     0.001    100.0    0.863762        0.863760    1.95e-06
      400     0.001    200.0    0.981440        0.981439    5.33e-07
```

The error falls by a factor of about 16 when the time step falls by a factor of 20,
which is the signature of a first-order explicit scheme's time discretisation
error. A solver verified this way can then be used on the real problem, where the
answer is not known in advance — and *that* is the point of the check. The
verification is not that the numbers agree with a textbook; it is that the code
reproduces a solution derived independently of it.

## 4. Total subsidence, and inverting it

Adding equations (1) and (5) gives the total water-loaded subsidence of a
uniformly stretched lithosphere:

$$S_{\text{total}}(\beta) = \left(1 - \frac{1}{\beta}\right)
\left[t_c\frac{\rho_m - \rho_c}{\rho_m - \rho_L} + \frac{\alpha\rho_m T_m
a}{2(\rho_m - \rho_L)}\right]. \tag{7}$$

The demo evaluates it with a stated set of typical parameters:

```text
 beta   S_initial (m)   S_thermal(inf) (m)   S_total (m)  crustal thinning (km)
 1.25         1,541.9                792.7       2,334.6                   7.00
 1.50         2,569.8              1,321.2       3,891.0                  11.67
 2.00         3,854.6              1,981.8       5,836.4                  17.50
 5.00         6,167.4              3,170.9       9,338.3                  28.00
```

Inverting a single observed total subsidence gives

```text
    SYNTHETIC observed S_total = 3,000 m
    coefficient (per unit of 1 - 1/beta) = 11,673 m
    (1 - 1/beta) = 0.2570  ->  beta = 1.346
    crustal thinning implied = 9.00 km
```

and the inversion is legitimate only because $\beta$ is the single unknown in
equation (7). This is the model at its most useful and most vulnerable. Useful,
because one number and a set of physical parameters give a tectonic
interpretation. Vulnerable, because **one number does not determine a history**:
the same total subsidence can be produced by more thinning with less thermal
subsidence, or the reverse. The shape of the curve, not its endpoint, is the
measurement — which brings back the truncation error of §2, since the shape in the
first tens of millions of years is exactly what the single-exponential law gets
wrong.

For a real basin the parameters are also not known independently. The
lithospheric thickness $a$ is a modelling choice with a large uncertainty, the
thermal expansion coefficient $\alpha$ is a laboratory quantity that varies
between minerals and with temperature, and the loading density depends on what was
deposited. The rest of this lesson is about making those dependencies explicit.

## 5. Backstripping: removing the load and the compaction

The observed quantity is the thickness of sediment in the column today. To
recover the tectonic subsidence, three corrections are needed.

**Decompaction.** A unit that is now 1200 m thick with 15 per cent porosity was
thinner when deposited, because it had more porosity then. Conserving solid
volume, with a porosity–depth law $\phi(z) = \phi_0 e^{-z/c}$, gives the
deposited thickness

$$\Delta z_{\text{dep}} = \frac{\Delta z_{\text{now}}\left[1 -
\phi(\bar z)\right]}{1 - \phi_0}, \tag{8}$$

with $\bar z$ the unit's present mid-depth.

**Load removal.** The sediment above a unit has weight, and removing it lets the
basement rise. The water-loaded subsidence is the load of everything above,
converted to an equivalent thickness of water:

$$Y = \frac{\rho_s^{\text{solid}}\,\text{solid thickness} + \rho_w\,
\text{porosity volume}}{(\rho_m - \rho_w)}, \tag{9}$$

and in practice the correction is applied unit by unit from the top down, because
each unit's own decompacted thickness is only defined once the ones above it have
been restored.

**Paleo-water-depth.** The depth of water in which the unit was deposited is a
facies interpretation, and it is added directly to the tectonic subsidence. It is
often the largest single uncertainty in a backstripped curve, because it comes
from the sedimentology rather than from the physics.

The demo backstrips a synthetic column:

```text
  age (Ma)  thickness now (m)  phi now  decompacted (m)  tectonic subs. (m)
        40                400    0.498              447                 346
        30                700    0.378              968               1,105
        20                900    0.253            1,493               2,283
        10              1,200    0.150            2,267               4,053
```

and reports the rate, which is the quantity of geological interest:

```text
  mean tectonic subsidence rate over the 30 Myr of record: 0.1351 m/ka
```

The rate, not the thickness, is the tectonic signal: a basin filled in 10 Myr and
one filled in 100 Myr have different histories behind the same column.

## 6. What each assumption is worth

This is the section that most basin analyses omit, and it is the one that decides
whether the result means anything. The same column is backstripped with the
porosity and density parameters varied over defensible ranges:

```text
  parameter                          variant    S_tectonic (m)    change (m)
  surface porosity phi0               0.45             3,873          -180
  surface porosity phi0               0.65             4,403          +349
  porosity decay length            1,500 m             4,319          +266
  porosity decay length            3,000 m             3,693          -360
  grain density               2,650 kg/m^3             4,009           -44
  grain density               2,850 kg/m^3             4,215          +161
```

The porosity assumptions alone move the answer by 710 m and the grain density by
205 m, against a total tectonic subsidence of about 4000 m. **The spread produced
by the porosity model is of the same order as the tectonic signal being
measured.** A backstripped curve without a sensitivity table therefore has an
unstated error bar, and the error bar belongs to the method rather than to the
measurement.

The correct response is not to abandon backstripping. It is to report the
sensitivity, to prefer porosity and density parameters measured on the actual
lithologies where they exist, and to be suspicious of any tectonic conclusion that
depends on a difference smaller than the spread of the sensitivity table.

## 7. Accommodation, supply and water depth

The subsidence history is the *accommodation* — the space available. What fills
it depends on sediment supply, and the record that results is a competition
between the two. Three regimes, in the standard vocabulary:

- **Supply exceeds accommodation.** The basin fills to sea level, the shoreline
  progrades, and the record is a regression with shallow-water facies
  progressively further basinward.
- **Accommodation exceeds supply.** Water deepens, the shoreline retreats, and
  the record is a transgression with a condensed section offshore.
- **They match.** A balance is maintained and a thick package of shallow-water
  facies accumulates — which is the condition for the thick shelf-carbonate and
  deltaic successions that make up a large part of the stratigraphic record, and
  which requires the two rates to track each other over millions of years.

Water depth is a separate quantity again: it is the difference between the
subsidence and the accumulated sediment thickness, and it is what the
paleontological and sedimentological evidence actually constrains. Confusing
total subsidence with tectonic subsidence, or sediment thickness with
accommodation, are the two commonest errors in reading a basin history.

## 8. Assumptions and regime of validity

- **Instantaneous stretching.** The model assumes the thinning happened quickly
  compared with the thermal time constant $\tau$. For $\tau$ of order 50 Ma this
  is a good approximation for a rift that lasted a few million years and a poor
  one for a wide rift that extended over tens of millions of years, where
  syn-rift thermal effects must be integrated during rifting.
- **Uniform stretching with depth.** The lithosphere is assumed to thin by the
  same factor at every depth. Real rifts often show depth-dependent stretching,
  which the model cannot represent.
- **Local (Airy) isostasy.** The model assumes that the load is supported
  locally. For loads with a wavelength much greater than the elastic thickness of
  the lithosphere this is inadequate, and a flexural model is needed.
- **A steady asthenospheric temperature and a fixed lithospheric thickness.**
  Both are modelling choices with uncertainties larger than the differences often
  being interpreted.
- **The ocean is water-filled in these calculations.** A sediment-filled or
  air-filled basin gives different numbers, which is why the load density appears
  explicitly in every equation above.
- **Backstripping assumes the porosity law and the grain densities are known and
  laterally uniform**, and that no unit has been removed by erosion. Where an
  unconformity is present, the removed section is a missing term that must be
  estimated by other means.

## 9. Python demonstration

[`code/04-basins_subsidence_demo.py`](./code/04-basins_subsidence_demo.py) runs
the finite-difference heat solver, verifies it against a single-mode exact
solution, computes the modal weights of the post-rift geotherm, compares the
numerical solution with both the exact series and the single-exponential law,
evaluates and inverts the total-subsidence relation, backstrips a synthetic
column, and tabulates the sensitivity of the result.

Its output is quoted in §2, §3, §4, §5 and §6 above. Run it as:

```bash
cd 04-earth-science-geology/03-geologic-time-and-stratigraphy/code
.venv/bin/python 04-basins_subsidence_demo.py
```

Every physical parameter in the script is labelled TABULATED or TYPICAL, and the
script prints that label. Replace them with province-specific values and a
reference, and the numbers move: that is the lesson and not a defect.

## 10. Common mistakes

1. **Reading the total subsidence as the tectonic signal.** The load and
   compaction contributions are not small.
2. **Using the single-exponential law over the first tens of millions of years**
   without knowing its error, which is of order a few per cent of the total.
3. **Inverting one number for two parameters.** Total subsidence alone cannot
   separate the crustal-thinning and thermal contributions.
4. **Quoting a backstripped curve without a sensitivity table.** The porosity
   model alone can move the answer by hundreds of metres.
5. **Forgetting paleo-water-depth.** It enters the tectonic subsidence directly
   and is often the largest single uncertainty.
6. **Confusing accommodation with sediment thickness.** The difference between
   them is the water depth.
7. **Using a fixed lithospheric thickness and a fixed $\alpha$ across provinces.**
   Both vary, and the subsidence scale is proportional to their product.
8. **Applying local isostasy to a wide basin.** At basin widths of hundreds of
   kilometres, flexure matters.
9. **Ignoring erosion at an unconformity.** The missing section is a real term in
   the balance, not a gap to be interpolated through.
10. **Reporting a subsidence rate over an interval chosen after seeing the
    curve.** The interval is part of the result.

## 11. Real-world applications

- **Rifted-margin evolution and passive-margin stratigraphy.** The thermal
  subsidence of §2 is the reason post-rift successions on passive margins thicken
  and deepen basinward.
- **Hydrocarbon exploration.** Source-rock maturity, reservoir distribution and
  trap timing all depend on a subsidence and thermal history, and the burial
  history that a basin model supplies is a backstripped curve
  ([04-06-01](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Geothermal resource assessment.** The same thermal model, run for longer and
  with a higher heat flow, is the basis of a geothermal prospect evaluation
  ([04-06-03](../06-petroleum-and-mineral-systems/03-geothermal-systems.md)).
- **Groundwater and aquifer geometry.** The architecture of a sedimentary basin
  sets aquifer continuity and the position of confining units
  ([04-06-04](../06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)).
- **Subsidence hazard.** Where the mechanism is anthropogenic rather than
  tectonic, the same decomposition is used in reverse to identify what is
  compacting ([04-07-04](../07-geologic-hazards/04-subsidence-sinkholes.md)).
- **Sea-level reconstruction.** A backstripped tectonic subsidence curve is the
  quantity that must be removed from a stratigraphic record before a eustatic
  sea-level signal can be extracted
  ([04-05-04](../05-geomorphology-and-quaternary/04-quaternary-climate.md)).

## 12. Further reading

- **Allen, P. A., & Allen, J. R. *Basin Analysis: Principles and Application to
  Petroleum Play Assessment* (Wiley-Blackwell).** The standard reference for
  everything in this lesson and the stratigraphic interpretation that follows it.
  Level: intermediate to advanced.
- **McKenzie, D. (1978). Some remarks on the development of sedimentary basins.
  *Earth and Planetary Science Letters* 40, 25–32.** The paper that introduced
  the uniform-stretching model used in §1–§4, including the thermal subsidence
  calculation. Level: advanced.
- **Turcotte, D. L., & Schubert, G. *Geodynamics* (Cambridge University Press).**
  The heat-conduction and isostasy background, derived from first principles.
  Level: advanced.
- **Watts, A. B. *Isostasy and Flexure of the Lithosphere* (Cambridge University
  Press).** The flexural treatment that this lesson's Airy assumption
  deliberately avoids, and the reason it matters at basin scale. Level:
  graduate.
- **Selley, R. C., & Morrill, A. *Applied Sedimentology* (Academic Press).** The
  porosity, compaction and diagenesis that §5 reduces to a single exponential
  law. Level: intermediate.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 13. Related lessons

- [01 The Geologic Time Scale and Deep Time](./01-geologic-time-scale.md) — the
  durations over which the thermal subsidence of §2 accumulates.
- [02 Stratigraphic Principles and Relative Dating](./02-stratigraphic-principles.md)
  — the column that is decompacted in §5.
- [03 Radiometric Dating Methods and Their Assumptions](./03-radiometric-dating.md)
  — how the ages on the horizons of that column are obtained.
- [04-01-02 Lithosphere, Asthenosphere and the Rheological Definition](../01-earth-structure/02-lithosphere-asthenosphere.md)
  — what the thickness $a$ in §2 actually means.
- [04-02-02 Divergent, Convergent and Transform Boundaries](../02-plate-tectonics/02-plate-boundaries.md)
  — where each basin-forming mechanism occurs.
- [06-09-09 Structural and Stratigraphic Interpretation](../../06-seismology/09-reflection-seismology/09-interpretation-reflection.md)
  — how the subsurface geometry that a basin model predicts is imaged.
- [26-02-04 Dimensional Analysis Quick Reference](../../26-reference-library/02-symbols-and-units/04-dimensional-analysis-reference.md)
  — for checking equations (1), (5) and (7) before using them.

Exercises:
[`exercises/04-sedimentary-basins-exercises.md`](./exercises/04-sedimentary-basins-exercises.md)
and
[`exercises/04-sedimentary-basins-solutions.md`](./exercises/04-sedimentary-basins-solutions.md).

## Self-assessment checklist

- [ ] I can derive the instantaneous subsidence of equation (1) from isostatic
      balance and explain the $(1 - 1/\beta)$ factor. (§1)
- [ ] I can set up the stretched-geotherm initial condition and explain why it is
      not a single sine mode. (§2)
- [ ] I can verify a heat-conduction solver against a single-mode exact solution
      and say what the residual convergence rate implies. (§3)
- [ ] I can state the asymptotic thermal subsidence and identify every parameter
      in it. (§2)
- [ ] I can explain why the single-exponential law is a truncation and quote the
      size of its error for a stated case. (§2)
- [ ] I can invert a total subsidence for $\beta$ and say why one number does not
      determine a history. (§4)
- [ ] I can backstrip a column: decompact, remove the load, and separate tectonic
      subsidence from water depth. (§5)
- [ ] I can construct a sensitivity table for a backstripped curve and say which
      parameter dominates. (§6)
- [ ] I can distinguish accommodation, supply and water depth, and name the
      stratigraphic signature of each regime. (§7)
- [ ] I can list the assumptions of the stretching model and the regime in which
      each fails. (§8)
