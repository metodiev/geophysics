---
id: 15-05-03
title: "Coastal Aquifers and Submarine Groundwater Discharge"
level: doctoral
prereqs: ["15-05-02", "14-02-01", "09-02-05", "07-03-02"]
tags: [oceanography, marine-geophysics, coastal-and-estuarine, coastal-aquifers, submarine-groundwater, hydrogeophysics]
---

# Coastal Aquifers and Submarine Groundwater Discharge

> **All models and data in this module are SYNTHETIC.** The island, the aquifer
> properties and the conductivity model are teaching models with the stated model
> constants. No real island, aquifer, well, beach or survey is referenced, and no
> number is quoted from a published measurement.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Ghyben–Herzberg relation from hydrostatic equilibrium and
   **apply** the 40-fold amplification to a measured head.
2. **Derive** the Dupuit solution for an island freshwater lens, **verify** it
   against the steady Boussinesq equation, and **compute** the lens geometry,
   volume and residence time.
3. **Compute** the drawdown that induces upconing and the pumping rate it
   corresponds to, and **state** why the limit is set by the density contrast
   rather than by permeability.
4. **Convert** a pore-fluid salinity into a bulk resistivity through a fluid
   conductivity model and Archie's law, and **state** the two model assumptions
   that most bias the result.
5. **Choose** an electrode spacing for a target depth, given the depth-of-
   investigation model, and **state** that the model's coefficient is a choice.
6. **Compute** the tidal decay length and **show** with numbers that the
   recirculated discharge exceeds the fresh discharge.
7. **Separate** the terms of a coastal groundwater budget and **name** the term
   that no single measurement determines.

## Prerequisites

- [15-05-02 Estuarine and Delta Geophysics](02-estuarine-geophysics.md) —
  the salinity structure of the coastal water column.
- [14-02-01 ERT for Hydrology](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/01-ert-for-hydrology.md) —
  the resistivity method used to map the interface.
- [09-02-05 ERT Tomography](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md) —
  array geometry and depth of investigation.
- [07-03-02 Simple Body Formulas](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/02-simple-body-formulas.md) —
  the potential-field analogue of the density-contrast argument.

## 1. Intuition: a lens held up by a 2.5% density difference

Fresh water floats on seawater, and the density difference is small — about 2.5%.
That small number produces a dramatic result. Hydrostatic equilibrium at the
interface requires that the fresh-water column above balance the seawater column
beside it, so a metre of fresh head above sea level supports **forty metres** of
fresh water below it. The coastal aquifer is therefore a thin, deep lens whose
geometry is controlled by a density ratio, and whose response to pumping is
amplified by the same factor of forty.

Two consequences follow, and they organise this lesson.

**The interface is easy to move and easy to mismeasure.** A drawdown of half a
metre brings the interface up twenty metres. A well that looks comfortably
screened 20 m above the interface can therefore only pump a few hundred cubic
metres a day. And because the interface is a *transition zone* in reality rather
than a sharp surface, the sharp-interface model overstates the gradient and
understates the thickness — the model gives the scaling, not the operational
limit.

**The interface is a conductivity contrast, not a salinity measurement.**
Seawater-saturated sand has a bulk resistivity of order 1.5 Ω·m against 58 Ω·m for
brackish water in the model here — a factor of 35, which is why resistivity and EM
methods are the standard tool. But a resistivity section measures conductivity,
and clays conduct through their surfaces as well as their pores; an Archie
inversion of a clay-rich coastal sediment overestimates the salinity. **Every
mapping of a coastal interface is an inversion through a rock-physics model.**

Finally, the water that discharges offshore is not only the fresh water. Tidal
loading pumps seawater in and out of the aquifer every cycle, and the
demonstration shows the recirculated volume is **4.6 times the fresh discharge**
for its model parameters. A tracer survey measures both unless it separates them,
and the two have entirely different implications for nutrient budgets and for
contamination.

## 2. Precise definitions

**Ghyben–Herzberg relation**: $z=\dfrac{\rho_f}{\rho_s-\rho_f}h$, the interface
depth below sea level for a fresh head $h$ above it.

**Freshwater lens**: the body of fresh water floating on seawater beneath an
island or a coastal strip, bounded below by the interface and above by the water
table.

**Upconing**: the upward movement of the interface beneath a pumping well, caused
by the local drawdown and amplified by the density ratio.

**Hydraulic head** $h$ and **transmissivity** $T=Kb$: the drive and the
conductance of the aquifer.

**Archie's law**: $\rho_b=\rho_f\phi^{-m}S_w^{-n}$, an empirical relation between
the bulk resistivity, the pore-fluid resistivity, porosity and water saturation.
Valid for clean (clay-free) granular media.

**Submarine groundwater discharge (SGD)**: all water flowing from the aquifer
across the seafloor, fresh and recirculated. Only the fresh part represents
net terrestrial input.

**Tidal decay length** $\lambda=\sqrt{2T/(S\omega)}$: the distance over which a
tidal pore-pressure oscillation decays inland, with $S$ the storativity and
$\omega$ the tidal angular frequency.

## 3. Derivations and measurements

### 3.1 Ghyben–Herzberg from hydrostatics

At the interface, the pressure from the fresh column must equal the pressure from
the seawater column at the same depth. Taking the sea surface as datum and the
interface at depth $z$:

$$\rho_fg(h+z)=\rho_sg\,z
\;\Rightarrow\;
z(\rho_s-\rho_f)=\rho_fh
\;\Rightarrow\;
\boxed{\;z=\frac{\rho_f}{\rho_s-\rho_f}h\;}$$

With $\rho_f=1000$ and $\rho_s=1025\ \mathrm{kg\,m^{-3}}$ the factor is
**40.0**: a 2 m head holds the interface at 80 m below sea level. The relation is
*exact* hydrostatics; everything that makes it approximate is in the assumptions
(§5), not in the algebra.

### 3.2 The Dupuit island lens

Let a strip island of width $L$ receive recharge $w$ and be underlain by an
aquifer of constant $K$. With the Ghyben–Herzberg relation, the fresh-water
thickness is $b=h+z=h\rho_s/(\rho_s-\rho_f)$, and the Dupuit (horizontal-flow)
discharge per unit width is

$$q=-Kb\frac{\mathrm{d}h}{\mathrm{d}x}
=-K\frac{\rho_s}{\Delta\rho}h\frac{\mathrm{d}h}{\mathrm{d}x} .$$

Steady state requires $\mathrm{d}q/\mathrm{d}x=w$, and symmetry requires
$\mathrm{d}h/\mathrm{d}x=0$ at the centre, giving

$$h^2(x)=\frac{w\,\Delta\rho}{K\rho_s}\left(\frac{L^2}{4}-x^2\right),
\qquad
h(0)=\frac{L}{2}\sqrt{\frac{w\Delta\rho}{K\rho_s}} .$$

For the model island ($L=5000$ m, $w=0.5\ \mathrm{m\,yr^{-1}}$,
$K=50\ \mathrm{m\,day^{-1}}$, i.e. $w=1.584\times10^{-8}\ \mathrm{m\,s^{-1}}$ and
$K=5.787\times10^{-4}\ \mathrm{m\,s^{-1}}$):

$$\frac{w\Delta\rho}{K\rho_s}=6.678\times10^{-7}\ \mathrm{m^{-1}},\qquad
h(0)=2.043\ \mathrm{m},\qquad z(0)=81.7\ \mathrm{m},$$

and the lens thickness is $41.00\,h(0)=83.8$ m — exactly
$\rho_s/\Delta\rho$ times the head, as the algebra requires.

**Verification.** The demonstration evaluates the solution on a 2001-point grid,
forms $q=-Kbh'$ and checks $\mathrm{d}q/\mathrm{d}x=w$. The maximum relative
residual is $2.4\times10^{-4}$, which is the finite-difference error of
`np.gradient` on the steep flanks — the analytic solution satisfies the governing
equation. **This is the useful kind of check: it tests the algebra rather than
restating it.**

**Volume and residence time.** Integrating $\rho_s h/\Delta\rho$ over the width:

$$V=41.00\int_{-L/2}^{L/2}h\,\mathrm{d}x=41.00\times\frac{\pi L^2}{8}
\sqrt{\frac{w\Delta\rho}{K\rho_s}}
=3.289\times10^{5}\ \mathrm{m^3\ (per\ m\ of\ shoreline)}$$

(the integral of the semi-ellipse profile is $\pi L^2/8$ times the coefficient
$a=\sqrt{w\Delta\rho/(K\rho_s)}$). The recharge over the same width is
$wL=2500\ \mathrm{m^3\,yr^{-1}}$ per metre of shoreline, so the **residence time is
$3.289\times10^{5}/2500=132$ yr**.

Two orders of magnitude matter here. The residence time is the number that decides
how long a contaminant persists, and it is set by the lens volume — which depends
on $L^2$, $w^{1/2}$ and $K^{-1/2}$. **A doubling of the island width quadruples
the volume and doubles the residence time.**

### 3.3 Upconing and the pumping limit

Because the interface rises 40 m per metre of drawdown, a well whose screen sits
20 m above an interface at 40 m can only draw down

$$s_{\max}=\frac{40-20}{40}=0.500\ \mathrm{m} .$$

With $T=Kb=5.787\times10^{-4}\times40=0.0231\ \mathrm{m^2\,s^{-1}}$ and the Thiem
solution $s(r)=Q\ln(R/r_w)/(2\pi T)$:

$$Q_{\max}=\frac{2\pi Ts_{\max}}{\ln(R/r_w)}
=\frac{2\pi\times0.0231\times0.500}{7.824}=0.00929\ \mathrm{m^3\,s^{-1}}
=803\ \mathrm{m^3\,day^{-1}} .$$

**The limit is set by the density ratio, not by the permeability.** Multiply $K$
by ten and $Q_{\max}$ rises by ten — but the *drawdown* available to the well stays
at half a metre, so the well's specific capacity is unchanged and the constraint is
the head, not the flow. In practice, heterogeneous $K$, a transition zone of finite
thickness and time-dependent mixing all change this by factors; the model gives the
scale and the scaling law, which is what a management decision needs.

### 3.4 From salinity to conductivity to resistivity

A model for the pore-fluid conductivity, calibrated so that seawater salinity
gives a plausible value, is $\sigma_f=a_\sigma S$ with
$a_\sigma=0.114\ \mathrm{S\,m^{-1}\,(g\,kg^{-1})^{-1}}$. With Archie's law
($m=1.8$, $n=2.0$, $\phi=0.35$, so $\phi^{-m}=6.62$):

| $S$ (g/kg) | $\sigma_f$ (S/m) | $\rho_f$ (Ω·m) | $\rho_b$ (Ω·m) |
|---|---|---|---|
| 0.1 | 0.011 | 87.72 | 580.46 |
| 1.0 | 0.114 | 8.77 | 58.05 |
| 5.0 | 0.570 | 1.75 | 11.61 |
| 10.0 | 1.140 | 0.88 | 5.80 |
| 35.0 | 3.990 | 0.25 | 1.66 |

The contrast from 1 to 35 g/kg is **35×** — the physical reason resistivity and EM
methods are the standard interface tools. Three caveats, all of which bias the
answer in the same direction:

1. **Clays.** Surface conduction adds a parallel conductivity path that Archie's
   law does not represent, so the true bulk resistivity is *lower* than
   predicted and an Archie inversion *overestimates* the salinity. Coastal
   sediments are usually clay-bearing.
2. **$m$ and $n$ are fitted, not measured.** A change from $m=1.8$ to $m=2.2$
   changes $\phi^{-m}$ from 6.62 to 9.97, a 50% change in every resistivity.
3. **The pore-fluid model.** $a_\sigma$ is a model constant; different
   calibrations shift the salinity by tens of per cent at low salinity, exactly
   where the interface is.

**The honest statement is therefore the one in the lesson title of this
section: conductivity is not salinity.** A resistivity section maps a conductivity
distribution; the conversion to salinity carries a model, and the model's error
grows with clay content.

**Depth of investigation.** A Wenner array's median depth of investigation is
about $0.52a$ for an electrode spacing $a$ (a model value, stated so that it can
be checked):

| $a$ (m) | median depth (m) | minimum array length $3a$ (m) |
|---|---|---|
| 20 | 10 | 60 |
| 40 | 21 | 120 |
| 80 | 42 | 240 |

To see an interface at 40 m, $a=80$ m and a 240 m array are needed — which means
the lateral resolution is ~80 m and a channel 100 m wide cannot be resolved along
its axis with such an array.

### 3.5 Fresh versus recirculated discharge

Tidal loading drives an oscillatory pore pressure that decays inland with the
skin length $\lambda=\sqrt{2T/(S\omega)}$. With $T=0.0231\ \mathrm{m^2\,s^{-1}}$,
$S=0.2$ and $\omega=2\pi/(12.42\ \mathrm{h})=1.405\times10^{-4}\ \mathrm{rad\,s^{-1}}$:

$$\lambda=\sqrt{\frac{2\times0.0231}{0.2\times1.405\times10^{-4}}}=40.6\ \mathrm{m}.$$

An order-of-magnitude exchange volume per unit shoreline is
$2A\lambda S$ per tidal cycle ($A$ the tidal amplitude, a model estimate), which
for $A=1$ m and 1.93 cycles per day gives $31.4\ \mathrm{m^3\,day^{-1}}$ per metre
of shoreline, or $1.146\times10^{4}\ \mathrm{m^3\,yr^{-1}}$. Against the fresh
discharge of $2500\ \mathrm{m^3\,yr^{-1}}$ from §3.2:

$$\frac{\text{recirculated}}{\text{fresh}}=4.6 .$$

**The recirculated component is several times the fresh component** in this model.
Any tracer-based SGD estimate mixes the two, and only the fresh part is
terrestrial input. Separating them needs a conservative tracer pair (salinity for
the mixing, radium or radon isotopes for the water–sediment exchange) plus a mass
balance — a model, built on measurements.

## 4. Physical interpretation

- **A 2.5% density difference creates a 40-fold amplification.** Almost every
  surprising thing about coastal aquifers follows from that number.
- **The lens is thin, deep and slow.** $h/L=4\times10^{-4}$ for the model island,
  and a 132 yr residence time.
- **Pumping is limited by head, not by permeability.** The available drawdown is
  set by the interface depth and the density ratio.
- **The interface is a transition zone.** The sharp-interface models give
  scaling; dispersion, heterogeneity and transient mixing set the local position.
- **Resistivity maps conductivity, and conductivity is not salinity.** The
  inversion needs a rock-physics model whose error grows with clay content.
- **SGD is mostly recirculated seawater.** Reporting a total SGD flux as a
  freshwater flux is a category error, and it is common.

## 5. Assumptions and regime of validity

1. **Sharp interface.** The Ghyben–Herzberg relation treats the boundary as a
   surface; real coastal aquifers have a transition zone whose thickness grows with
   dispersion and with pumping.
2. **Hydrostatic equilibrium and no vertical flow.** The Dupuit assumption
   (horizontal flow, vertical equipotentials) fails near the coast and near
   pumping wells, which is exactly where the interesting questions are.
3. **Constant density in each fluid and a constant $K$.** Density varies with
   salinity through the transition zone, and coastal $K$ varies by orders of
   magnitude over metres.
4. **Steady state.** Recharge is seasonal; sea level and pumping change; the lens
   adjusts on the timescale of its residence time, i.e. decades.
5. **A uniform recharge rate and a symmetric strip island.** Real islands have
   spatial recharge patterns and a three-dimensional lens whose shape depends on
   the shoreline geometry.
6. **Archie's law without surface conduction.** Valid only for clean sands; the
   single largest error source in the salinity inversion.
7. **A linearised pore-fluid conductivity.** The salinity–conductivity relation is
   nonlinear at high salinity and strongly temperature-dependent.
8. **A constant tidal decay length.** It depends on $T$ and $S$, which vary
   spatially and with the tide itself.
9. **A model estimate of exchange volume.** $2A\lambda S$ is an
   order-of-magnitude construct, not a derived flux; the true recirculation depends
   on the beachface geometry, wave setup and the sediment's permeability.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| density | $\rho$ | $\mathrm{kg\,m^{-3}}$ | |
| head | $h$ | m | |
| interface depth | $z$ | m | $\rho_fh/\Delta\rho$ |
| recharge | $w$ | $\mathrm{m\,s^{-1}}$ | m/yr ÷ 3.15576×10⁷ |
| hydraulic conductivity | $K$ | $\mathrm{m\,s^{-1}}$ | m/day ÷ 86400 |
| transmissivity | $T$ | $\mathrm{m^2\,s^{-1}}$ | $Kb$ |
| pumping rate | $Q$ | $\mathrm{m^3\,s^{-1}}$ | ×86400 for m³/day |
| conductivity | $\sigma$ | $\mathrm{S\,m^{-1}}$ | |
| resistivity | $\rho_b$ | $\Omega\,\mathrm{m}$ | $1/\sigma$ |
| decay length | $\lambda$ | m | $\sqrt{T/(S\omega)}$ |
| discharge | — | $\mathrm{m^3\,yr^{-1}}$ | per metre of shoreline |

The check that catches most errors: $w$ and $K$ must both be in
$\mathrm{m\,s^{-1}}$ before they enter $h^2=\cdots w/K$. A recharge left in
$\mathrm{m\,yr^{-1}}$ and a $K$ in $\mathrm{m\,day^{-1}}$ differ by a factor of
365, and the head is wrong by $\sqrt{365}=19$. The second check: $Q$ in
$\mathrm{m^3\,day^{-1}}$ is the operational unit, and the conversion from
$\mathrm{m^3\,s^{-1}}$ is a factor of 86 400.

## 7. Worked examples

All numbers are printed by `code/coastal_aquifers_marine_demo.py`.

### Example 1 — the amplification

$z/h=1000/25=40.0$. A 2 m head holds the interface at 80 m; a 10 m head at 400 m.
The demonstration's table is exactly this linear relation.

### Example 2 — the model island's lens

$w\Delta\rho/(K\rho_s)=1.584\times10^{-8}\times25/(5.787\times10^{-4}\times1025)
=6.678\times10^{-7}\ \mathrm{m^{-1}}$,
$h(0)=(5000/2)\sqrt{6.678\times10^{-7}}=2.043$ m, $z(0)=81.7$ m, and
$V=3.289\times10^{5}\ \mathrm{m^3}$ per metre of shoreline, giving a residence time
of **132 yr** with a recharge of $2500\ \mathrm{m^3\,yr^{-1}}$ per metre.

### Example 3 — upconing

$s_{\max}=(40-20)/40=0.500$ m, and with $T=0.0231\ \mathrm{m^2\,s^{-1}}$ and
$\ln(500/0.2)=7.824$, $Q_{\max}=803\ \mathrm{m^3\,day^{-1}}$.

### Example 4 — the resistivity contrast

A 1 g/kg pore fluid gives $\rho_f=1/(0.114\times1)=8.77\ \Omega\,\mathrm{m}$ and
$\rho_b=8.77\times6.62=58.05\ \Omega\,\mathrm{m}$; a 35 g/kg fluid gives
$\rho_b=1.66\ \Omega\,\mathrm{m}$. The ratio 35.0 is the contrast a resistivity
section sees.

### Example 5 — the discharge partition

$\lambda=\sqrt{2\times0.0231/(0.2\times1.405\times10^{-4})}=40.6$ m; the exchange
is $31.4\ \mathrm{m^3\,day^{-1}}$ per metre of shoreline, or
$1.146\times10^{4}\ \mathrm{m^3\,yr^{-1}}$, against 2500 for the fresh discharge:
a ratio of **4.6**.

## 8. Python demonstration

`code/coastal_aquifers_marine_demo.py` prints, with units:

1. the Ghyben–Herzberg factor and table, the model island's lens profile, the
   Boussinesq residual check, the lens volume and the residence time;
2. the upconing calculation and the corresponding pumping limit;
3. the salinity–conductivity–resistivity table, the contrast, the clay caveat and
   the electrode-spacing table;
4. the tidal decay length and the fresh-versus-recirculated partition;
5. the worked-example values of Section 7.

```bash
cd 15-oceanography-marine/05-coastal-and-estuarine/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python coastal_aquifers_marine_demo.py
```

## 9. Exercises

[`exercises/03-coastal-aquifers-marine-exercises.md`](./exercises/03-coastal-aquifers-marine-exercises.md)
and
[`exercises/03-coastal-aquifers-marine-solutions.md`](./exercises/03-coastal-aquifers-marine-solutions.md).

## 10. Real-world applications

- **Water supply on small islands.** The lens is often the only resource, and the
  upconing limit sets the sustainable yield.
- **Seawater intrusion management.** Interface positions and their movement under
  pumping are regulatory quantities.
- **Coastal nutrient budgets.** SGD delivers nitrogen and phosphorus to coastal
  waters; the fresh fraction carries the terrestrial load, the recirculated
  fraction cycles seawater.
- **Contamination and remediation.** The residence time of the lens sets how long
  a spill persists.
- **Offshore freshened groundwater.** The same physics applies to palaeo-freshwater
  bodies on continental shelves, which are mapped with marine EM
  ([15-02-07 Marine CSEM and EM](../02-marine-geophysics-methods/07-marine-csem-em.md)).

## 11. Further reading

- **Bear, J., *Hydraulics of Groundwater*, McGraw-Hill (reprinted by Dover).**
  Level: graduate textbook. The Dupuit and Ghyben–Herzberg solutions in full.
- **Burnett, W. C., Bokuniewicz, H., Huettel, M., Moore, W. S., & Taniguchi, M.,
  "Groundwater and pore water inputs to the coastal zone", *Biogeochemistry*.**
  Level: research review. The SGD partition and its measurement.
- **Archie, G. E., "The electrical resistivity log as an aid in determining some
  reservoir characteristics", *Transactions of the AIME*.** Level: research. The
  original empirical law and its limitations.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint
- [ ] I can derive the Ghyben–Herzberg relation and use the amplification factor.
- [ ] I can derive the island-lens head profile and verify it.
- [ ] I can compute a lens volume and a residence time.
- [ ] I can compute the upconing-limited pumping rate.
- [ ] I can convert salinity to bulk resistivity through a stated model and name
      its two weakest assumptions.
- [ ] I can choose an electrode spacing for a target depth.
- [ ] I can compute a tidal decay length and the fresh/recirculated partition.
## Common pitfalls
1. **Forgetting the 40-fold amplification.** A head change of 10 cm moves the
   interface 4 m.
2. **Reporting a pumping limit from permeability alone.** The available drawdown
   is the binding constraint.
3. **Reading a resistivity section as a salinity map.** The conversion needs a
   rock-physics model, and clay conduction breaks it.
4. **Quoting $m$ and $n$ as measured.** They are fitted, and a 20% change moves
   every resistivity by 50%.
5. **Calling total SGD "fresh groundwater discharge".** The recirculated fraction
   can dominate.
6. **Using the Dupuit solution at the coast or at a well.** Vertical flow is
   largest exactly where the solution is quoted.
7. **Ignoring the transition zone.** A model interface sharpens as the grid is
   refined and as the pumping increases.
8. **Mixing recharge and conductivity units.** m/yr with m/day is a factor of 365,
   and the head responds as its square root.

## Related modules
- [15-05-02 Estuarine and Delta Geophysics](02-estuarine-geophysics.md) —
  the salinity structure of the water above this aquifer.
- [14-02-01 ERT for Hydrology](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/01-ert-for-hydrology.md) —
  the resistivity method in a hydrological setting.
- [14-02-02 EM for Hydrology](../../14-hydrology-hydrogeophysics/02-hydrogeophysics-methods/02-em-for-hydrology.md) —
  the induction counterpart, and the tool of choice offshore.
- [09-02-05 ERT Tomography](../../09-electrical-em-methods/02-dc-resistivity/05-ert-tomography.md) —
  array design and depth of investigation.
- [04-06-04 Groundwater Aquifers](../../04-earth-science-geology/06-petroleum-and-mineral-systems/04-groundwater-aquifers.md) —
  the geological setting.
- [15-06-02 Observing Modern Sea Level Rise](../06-sea-level-change-marine/02-sea-level-rise-observation.md) —
  why the coastal water table and the sea surface move together.
