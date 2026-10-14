# Solutions — 04-01-04 Igneous, Sedimentary and Metamorphic Rocks

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — QAPF

**(a)** $Q + A + P = 80$, so $Q_n = 25.0$, $A_n = 31.25$, $P_n = 43.75$ per cent.

**(b)** $A/(A+P) = 31.25/(31.25+43.75) = 31.25/75.0 = 41.7$ per cent.

**(c)** $Q_n = 25$ lies between 20 and 60, and $A/(A+P) = 41.7$ lies between 35
and 65, so the rock is a **monzogranite**. The demo's classification of the same
analysis prints `monzogranite` and the check prints `OK`.

**(d)** The colour index is 20 per cent — the mafic mineral content. It matters
more than the name because density and velocity follow the mafic content:
quartz and feldspar are all near 2.6 to 2.7 g/cm³ with low velocities, while
olivine, pyroxene and amphibole are 3.0 to 3.4 g/cm³ with high velocities. A
name tells a geophysicist nothing; a colour index bounds the properties.

---

## ★2 — Grain size

**(a)** $\phi(0.5) = -\log_2 0.5 = +1.00$; $\phi(0.0625) = -\log_2 0.0625 = +4.00$.

**(b)** 0.5 mm is coarse sand; 0.0625 mm is the very fine sand / silt boundary.

**(c)** $\phi(2) = -\log_2 2 = -1.00$, which is a granule.

**(d)** The reference unit is the **millimetre**. Substituting a size in
micrometres gives a phi larger by $\log_2 1000 = 9.97$, which turns a medium sand
into something that looks like a clay — a plausible value rather than an obvious
error, which is why the reference unit has to be written down.

---

## ★3 — Facies

**(a)** $P = 0.80 < 1.2$, so not eclogite. $P \ge 0.6$ but $T = 600 \ge 350$, so
not blueschist. $T = 600$ is under 700, so **amphibolite**.

**(b)** $P = 0.45 < 0.6$, so no blueschist test. $T = 250$ is between 200 and
300, so **prehnite-pumpellyite**.

**(c)** $P = 1.30 \ge 1.2$ and $T = 500 < 1000$, so **eclogite**.

**(d)** $P = 0.70 \ge 0.6$ and $T = 300 < 350$, so **blueschist**.

---

## ★★4 — Folk and Ward

**(a)** $M_z = (1.462 + 2.318 + 3.388)/3 = 7.168/3 = 2.389$.

**(b)** $\sigma_I = (3.388-1.462)/4 + (3.954-1.024)/6.6 = 0.4815 + 0.4439 = 0.925$.

**(c)** 0.925 falls in 0.71 to 1.00, so the sample is **moderately sorted**.

**(d)** $d = 2^{-2.389} = 0.1909$ mm, which is **fine sand** (0.125 to 0.25 mm).

---

## ★★5 — Depth from pressure

**(a)** $z = 0.8\times10^9/(2900\times9.81) = 28.1$ km.

**(b)** $z = 0.8\times10^9/(2500\times9.81) = 32.6$ km.

**(c)** $P = 2750\times9.81\times3.5\times10^4 = 9.44\times10^8$ Pa $= 0.94$ GPa.

**(d)** Because the density changes with depth — from about 2500 kg/m³ in
sediments to 3300 at the base of the crust, 4400 at 660 km and 5570 at the base
of the mantle — so the pressure gradient itself varies by more than a factor of
two across the mantle. A single conversion factor accumulates an error
proportional to the depth over which it is applied, and in the mantle the error
reaches tens of kilometres.

---

## ★★6 — Two contrasts, two mechanisms

**(a)** Granite: $\rho_b = 0.99\times2.65 = 2.624$ g/cm³. Sandstone:
$\rho_b = 0.75\times2.68 = 2.010$ g/cm³. Contrast = 0.614 g/cm³, or 23 per cent
of the granite value.

**(b)** Gabbro: $0.98\times3.00 = 2.940$ g/cm³. Peridotite:
$0.995\times3.30 = 3.284$ g/cm³. Contrast = 0.344 g/cm³, or 12 per cent.

**(c)** The granite–sandstone contrast is **porosity-driven**: the grain
densities are within 1 per cent of each other and the difference is entirely in
$\phi$. The gabbro–peridotite contrast is **mineralogical**: both have
essentially zero porosity and the difference is in the grain density. The test
in the field is a second measurement that responds to porosity rather than to
mass density — a resistivity or a neutron log, or a seismic velocity, which drops
strongly with porosity and much less strongly with mineralogy.

---

## ★★★7 — Moving a classification boundary

**(a)** At $T = 300$ °C the standard geotherm's 25 km point becomes
**prehnite-pumpellyite**, not blueschist.

**(b)** At 360 °C the cold subduction 35 km point stays **greenschist**, since
it was already at 360 °C and neither boundary applies.

**(c)** Two rows change: the standard continental 25 km row and the cold
subduction 25 km row (0.69 GPa, 260 °C), which was blueschist and becomes
prehnite-pumpellyite. The extended geotherm's rows are unaffected.

**(d)** Moving one boundary by 50 °C reclassifies whole rows of the table, so a
box classification is a *communication* device and not a measurement. A
petrologist works from the actual mineral reactions — the appearance or
disappearance of a specific phase in a specific bulk composition — and reports
the assemblage and the reaction, not the box the point falls in.

---

## ★★★8 — The demo's output

**(a)** `a granite → monzogranite OK`; `a granodiorite → granodiorite OK`;
`a tonalite → tonalite OK`; `a gabbro → diorite / gabbro OK`;
`a syenite → syenite OK`. All five checks print `OK`.

**(b)** `Sorting value 0.925 -> moderately sorted (Folk and Ward classes)`;
`Median grain size in mm: 0.2005 mm (fine sand)`.

**(c)** At 35 km: cold subduction → `greenschist` at 360 °C; standard continental
→ `amphibolite` at 549 °C; extended → `granulite / partial melt` at 1042 °C.

**(d)** Sandstone 1.85 to 2.43 g/cm³; granite 2.55 to 2.69 g/cm³ — a 27 per cent
contrast at the extremes of both ranges.

**(e)** At 45 km the extended geotherm gives 1562 °C, which is above the
granulite field's upper temperature bound, so the demo labels it
`granulite / partial melt`. At that temperature a real rock would be partly
molten, and calling it a metamorphic rock would be wrong.

**(f)** The QAPF field boundaries, the Wentworth boundaries, the Folk and Ward
samples and the property ranges are all `TABULATED` or `NOMINAL` inputs; the
classifications, the statistics and the bulk densities are computed. The demo
prints `OK` or `expected <name>` next to each classification so that a wrong
implementation would be visible rather than plausible.

---

## ★★★9 — A bimodal sample

**(a)** A 60/40 mixture of a sand mode near $\phi = 2$ and a gravel mode near
$\phi = -2.5$ gives percentiles near $\phi_5 = -3.0$, $\phi_{16} = -2.0$,
$\phi_{50} = 1.5$ (between the modes), $\phi_{84} = 2.6$, $\phi_{95} = 3.0$. Then
$M_z = (-2.0 + 1.5 + 2.6)/3 = 0.70$, which lies between the two modes, in a range
of grain size where almost no grains are present.

**(b)** $\sigma_I = (2.6-(-2.0))/4 + (3.0-(-3.0))/6.6 = 1.15 + 0.91 = 2.06$, which
is "very poorly sorted". The value describes the *mixture*, not a depositional
process: the current that deposited the gravel and the current that deposited
the sand were different, and the statistic has averaged them.

**(c)** A sedimentologist reports the two populations separately — a gravel mode
and a sand mode, each with its own percentage, mean and sorting.

**(d)** A geophysicist predicting permeability from the mean grain size would
smooth over the bimodality and get both ends wrong: the mean grain size implies
a permeability intermediate between a gravel and a sand, while the real rock's
permeability is controlled by the sand-sized pore throats that the gravel
framework leaves, which are much smaller than the gravel's own grain size. The
predictions from a unimodal model can be orders of magnitude off.
