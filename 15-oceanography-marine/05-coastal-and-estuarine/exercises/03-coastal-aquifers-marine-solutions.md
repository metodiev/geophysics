# Solutions — 15-05-03 Coastal Aquifers and Submarine Groundwater Discharge

> **Read after attempting the exercises.** Lesson:
> [03 Coastal Aquifers and Submarine Groundwater Discharge](../03-coastal-aquifers-marine.md).
> Numbers are SYNTHETIC model values.

## ★ Foundational

## ★1 — Ghyben–Herzberg

$$\frac{\rho_f}{\rho_s-\rho_f}=\frac{1000}{24}=41.67,\qquad
z=41.67\times1.5=62.5\ \mathrm{m}.$$

The factor is larger than the lesson's 40.0 because $\Delta\rho$ is smaller: the
amplification is inversely proportional to the density difference, so a fresher
sea (or a colder one) deepens the interface for the same head.

## ★2 — Island lens

$$w=\frac{0.8}{3.15576\times10^{7}}=2.535\times10^{-8}\ \mathrm{m\,s^{-1}},\qquad
K=\frac{20}{86400}=2.315\times10^{-4}\ \mathrm{m\,s^{-1}},$$

$$\frac{w\Delta\rho}{K\rho_s}=\frac{2.535\times10^{-8}\times24}
{2.315\times10^{-4}\times1024}=\frac{6.084\times10^{-7}}{0.23706}
=2.567\times10^{-6}\ \mathrm{m^{-1}},$$

$$h(0)=\frac{L}{2}\sqrt{2.567\times10^{-6}}
=1000\times1.6021\times10^{-3}=1.602\ \mathrm{m},$$

$$z(0)=\frac{1000}{24}\times1.602=66.75\ \mathrm{m},\qquad
\text{lens thickness}=1.602\times\frac{1024}{24}=68.4\ \mathrm{m}.$$

The thickness is $1.602+66.75=68.35$ m, and the two expressions agree to the
rounding. ✔

## ★3 — Bulk resistivity

$$\sigma_f=0.114\times10=1.14\ \mathrm{S\,m^{-1}},\qquad
\rho_f=\frac{1}{1.14}=0.877\ \Omega\,\mathrm{m},$$

$$\rho_b=\rho_f\phi^{-m}=0.877\times0.30^{-2.0}=0.877\times11.111
=9.75\ \Omega\,\mathrm{m}.$$

For comparison, the lesson's $\phi=0.35$, $m=1.8$ case gives
$\phi^{-m}=6.62$; the porosity and the cementation exponent together move the
answer by nearly a factor of two.

## ★★ Applied

## ★4 — Upconing-limited pumping

$$s_{\max}=\frac{30}{40}=0.750\ \mathrm{m},$$

$$Q_{\max}=\frac{2\pi Ts_{\max}}{\ln(R/r_w)}
=\frac{2\pi\times0.02\times0.750}{7.5}
=\frac{0.09425}{7.5}=0.01257\ \mathrm{m^3\,s^{-1}}=1086\ \mathrm{m^3\,day^{-1}}.$$

Note that the interface was deeper (60 m) than in the lesson's example (40 m) so
the screen could be 30 m above it rather than 20 m, giving a larger allowable
drawdown and a larger well — **but the pumping rate still scales with the
available drawdown, not with $T$ alone.**

## ★5 — Tidal decay length

$$\omega=\frac{2\pi}{12.42\times3600}=1.405\times10^{-4}\ \mathrm{rad\,s^{-1}},$$

$$\lambda=\sqrt{\frac{2T}{S\omega}}
=\sqrt{\frac{2\times0.01}{0.1\times1.405\times10^{-4}}}
=\sqrt{\frac{0.02}{1.405\times10^{-5}}}=\sqrt{1423.5}=37.73\ \mathrm{m}.$$

The signal is $e^{-1}=0.37$ of the beachface amplitude at 37.7 m inland. With
$T=0.01\ \mathrm{m^2\,s^{-1}}$ (a tenth of the lesson's value) the decay length
falls only to 37.7 m from 40.6 m, because $\lambda\propto\sqrt{T}$: **the tidal
influence penetrates a few tens of metres regardless of plausible $T$, which is
why it is a shallow-but-universal process near every coast.**

## ★6 — Residence time

$$t=\frac{V}{Q}=\frac{5\times10^{5}}{4000}=125\ \mathrm{yr}.$$

If the island width doubles with the same recharge rate and $K$:

- the lens volume scales as $L^2$, so $V\to2.0\times10^{6}\ \mathrm{m^3}$ (×4);
- the rechage over the wider island scales as $L$, so $Q\to8000\
  \mathrm{m^3\,yr^{-1}}$ (×2);

$$t\to\frac{2.0\times10^{6}}{8000}=250\ \mathrm{yr}\quad(\times2).$$

The rule is $t\propto L$: doubling the island doubles the flushing time, which is
why large islands (and wide coastal plains) hold old water and are slow to
recover from contamination.

## ★★★ Research-oriented

## ★7 — Survey design for a lens with the interface at 40 m

| component | configuration | measured | modelled |
|---|---|---|---|
| land ERT | Wenner or dipole–dipole, electrode spacing $a=80$ m for a 42 m median depth of investigation, array length ≥240 m, at least three profiles across the island | bulk apparent resistivity | true resistivity section (inversion); salinity via Archie |
| towed marine EM | 20–50 m altitude over the seabed, frequency 1–10 Hz, along-shore lines | the secondary magnetic field | conductivity structure; offshore extent of the fresh water |
| boreholes and water levels | 2–3 holes to the interface, with nested piezometers; monthly water-level readings plus continuous loggers | head, hydraulic conductivity from slug tests, salinity profile from samples | the interface position between holes; the recharge rate from water-table fluctuation analysis |
| recharge | raingauges plus chloride mass balance or water-table fluctuation | rainfall; chloride deposition | recharge $w$, the single most uncertain input to the lens model |
| geophysics cross-check | seismic refraction (the bedrock depth) and gravity if the island is volcanic | bedrock geometry | the aquifer's base, which sets the transmissivity |

**Two model assumptions that most bias the salinity map:**

1. **Archie's law without surface conduction.** In a clay-bearing or volcanic
   coastal sediment, the bulk conductivity includes a surface-conduction path
   that Archie ignores, so an Archie inversion overestimates salinity.
   *Test:* laboratory resistivity measurements on cores at known pore-fluid
   salinity, i.e. a site-specific calibration of $\phi$, $m$ and the surface
   conductivity.
2. **The pore-fluid conductivity–salinity relation.** $\sigma_f=a_\sigma S$ is a
   model with a single coefficient and no temperature dependence.
   *Test:* measured pore-fluid samples from the boreholes with their electrical
   conductivity and their salinity, which gives the local $a_\sigma$ and reveals
   the temperature effect directly.

**The third bias worth naming:** the *inversion* of the ERT data itself
(smoothness constraints and a starting model). It is testable by comparing
inversions with different regularisation strengths against the borehole
observations — which is why the boreholes are not optional.

## ★8 — Partitioning SGD

**(a)** Recirculated fraction:

$$\frac{10000-2000}{10000}=0.80,$$

i.e. **80% of the discharge is recirculated seawater**, with a recirculated-to-fresh
ratio of 4.0 — the same order as the lesson's model ratio of 4.6.

**(b)** What each estimate measures:

| estimate | what it measures | uncertainty |
|---|---|---|
| radon budget | the total water flux through the sediment surface, weighted by the radon source (sediment–water exchange), including recirculated seawater | order of magnitude: it depends on the radon source term, the gas-exchange velocity and the mixing model, none of which is measured directly |
| water balance | the fresh component, via recharge minus evapotranspiration and abstraction over the catchment | factor of 2: recharge is a residual of several large terms |

**The water balance is more uncertain per unit effort, but the radon budget's
uncertainty is structural**: it measures a flux in units of the tracer's source,
so a factor-of-two error in the source is a factor-of-two error in the flux.
Neither is a direct measurement of discharge.

**(c)** Separating a larger fresh discharge from a larger recirculation:

- **A conservative, salinity-based mixing budget** (salinity plus a
  terrestrial tracer such as silica or a radiometric pair) decomposes the total
  into an end-member mixing term and a net terrestrial input: the fresh component
  is the one that changes the salinity of the coastal water over a full tidal
  cycle, while the recirculated water returns the same seawater it took in.
- **A time series** resolves the two: recirculation follows the tide (it is
  proportional to $A\lambda S$ per cycle, §3.5), while the fresh discharge follows
  the seasonal water table. Measuring the discharge over a spring–neap cycle and
  over a seasonal cycle separates them by their *time signature* rather than by
  their magnitude.

**The quantity that neither constrains:** the *age* of the water. A recirculated
parcel and a fresh parcel both leave the aquifer as water; neither the radon budget
nor the water balance distinguishes water that entered 3 days ago from water that
entered 30 years ago, and that distinction is what matters for contaminant
transport. It requires a transient tracer (tritium, CFCs, helium isotopes) and an
age model — a model again.
