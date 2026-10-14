# Solutions — 23-07-01 Case Study: Deploying a Temporary Seismic Array

The lesson is [01 Case Study: A Temporary Seismic Array](../01-case-study-seismic-array.md).
All values are **SYNTHETIC**.

## ★1

$$D = \frac{\lambda z}{R} = \frac{3000 \times 15\,000}{2000} = 22\,500\ \mathrm{m}
= 22.5\ \mathrm{km},$$

$$d_{\text{alias}} = \frac{\lambda}{2} = \frac{3000}{2} = 1500\ \mathrm{m} .$$

At half the aliasing limit ($d = 750$ m):

$$n = \frac{22\,500}{750} + 1 = 31 \text{ stations};$$

at the limit itself ($d = 1500$ m):

$$n = \frac{22\,500}{1500} + 1 = 16 \text{ stations} .$$

So the same resolution can be bought with 16 or 31 stations — **the aperture is the
requirement and the spacing is the insurance policy**. The 16-station design meets the
resolution on paper and fails it as soon as one station is lost (a 3000 m gap, twice the
aliasing limit), and it cannot measure the short-wavelength part of the wavefield at all. The
31-station design has a factor-of-two margin in spacing and therefore tolerates single
failures; its extra cost is 15 sites of installation, which is the price of the robustness.

## ★2

$$\text{station-hours} = 30 \times 4.0 = 120, \qquad
\text{person-days} = \frac{120 \times 4}{8} = 60,$$

$$\text{one crew: } \frac{30}{8/4.0} = 15 \text{ days}, \qquad
\text{two crews: } \frac{30}{16/4.0} = 7.5 \rightarrow 8 \text{ days} .$$

The labour is 60 person-days either way; the two-crew schedule halves the calendar and doubles
the vehicles, accommodation and supervision. The decision is made by the weather window and
the labour rate, and the *retrieval* visit costs the same again — so the campaign's total
labour is about 120 person-days, and a plan that counts only the installation is 50 % short.

## ★3

$$\text{rate} = 200 \times 3 \times 4 = 2400\ \mathrm{B/s},$$

$$\text{raw} = 2400 \times 86\,400 \times 45 \times 30 = 2.7994\times10^{11}
\ \mathrm{B} = 279.94\ \mathrm{GB},$$

$$\text{compressed} = \frac{279.94}{3} = 93.31\ \mathrm{GB}, \qquad
\text{repeats on 8 TB} = \frac{8000}{93.31} = 85.7 .$$

So one 8 TB disk holds **86 campaigns**. The constraint is therefore not storage at all — it is
the **download bench and the time to verify**: 30 stations' media, each holding 9.33 GB
compressed, at a realistic read-and-check rate of a few tens of MB/s per reader, is hours of
wall time per station. The plan should name the readers, the staging disks and the verification
step rather than the archive size.

## ★4

$$\bar I = 60\ \mathrm{\mu A} + 40\ \mathrm{mA}\,D_{\text{acq}}
+ \frac{200\ \mathrm{mA} \times 30}{86\,400} ,$$

| Duty | $\bar I$ | Life (30 Ah × 60 %) | Visits in 45 days |
|---|---|---|---|
| 1/4 | 10.129 mA | 74.04 days | 1 |
| 1/24 | 1.796 mA | 417.57 days | 1 |

Both duties cover the 45-day deployment with one visit, so the choice is **scientific, not
energetic**: 1/4 gives six times the recording time of 1/24 for the same visit schedule and
with 64 % of the battery life to spare. The 1/24 plan would be justified only if the storage or
the download volume were the constraint — and ★3 showed they are not. This is the pattern worth
remembering: once the power budget has margin, the duty cycle should be set by the *science*,
not by the battery.

## ★5

$$D_{\text{nominal}} = (30-1)(0.9) = 26.1\ \mathrm{km}, \qquad
R_{\text{nominal}} = \frac{\lambda z}{D} = \frac{45}{26.1} = 1.724\ \mathrm{km},$$

$$\text{expected alive} = 30 \times 0.85 = 25.5, \qquad
D_{\text{expected}} = (25.5-1)(0.9) = 22.05\ \mathrm{km},$$

$$R_{\text{expected}} = \frac{45}{22.05} = 2.041\ \mathrm{km}
\quad\text{(+18.3 % worse than designed)},$$

$$\text{two failures}: D = (28-1)(0.9) = 24.3\ \mathrm{km}, \quad
R = \frac{45}{24.3} = 1.852\ \mathrm{km},$$

$$\Delta R = 1.852 - 1.724 = 0.128\ \mathrm{km} = \mathbf{128\ m}
\quad\text{(+7.4 %)} .$$

Note the units and the structure: $\lambda z$ has units of km² only because both $\lambda$ and
$z$ are in km, so the aperture must be in km too; a mixed unit set is the standard way to get
this calculation wrong by 1000. Note also the *expected* loss (18.3 %) is larger than the
two-failure loss (7.4 %), because the expectation weights the cases with three, four and five
failures that also occur. A design requirement expressed as a mean is therefore a weak
requirement; it should be expressed as a probability (see ★6).

## ★6

A model answer.

**Geometry and margin.** With $\lambda = 3$ km at $z = 15$ km, the aperture needed for a
2 km target is $\lambda z/R = 45/2 = 22.5$ km, and the aliasing spacing is 1500 m. **Choose
1000 m** — two-thirds of the limit — which costs 24 stations for the bare aperture. But the
requirement is not the nominal resolution, it is *still meeting* the 2 km target after
failures: with 1000 m spacing, $R = 45/[(k-1)(1.0)]$ km for $k$ live stations, so $R \le 2$ km
needs $k \ge 24$ live stations. The design must therefore be built **around the failures**, not
around the nominal aperture:

| Stations deployed | Nominal $R$ | P(at least 24 live) at $p = 0.90$ |
|---|---|---|
| 24 | 1.957 km | 0.0798 |
| 27 | 1.731 km | 0.7179 |
| 28 | 1.667 km | 0.8579 |
| **29** | **1.607 km** | **0.9363** |
| 30 | 1.552 km | 0.9742 |

So **29 stations at 1000 m** is the smallest design meeting the 80 % requirement with margin
(0.9363), and it tolerates five simultaneous failures. The five extra stations beyond the bare
24 cost 20 station-hours — 10 person-days — which is the cheapest part of the whole plan.

**Installation schedule.** 29 stations at 4 h with a 4-person crew:

$$\text{station-hours} = 29 \times 4 = 116, \qquad
\text{person-days} = \frac{116 \times 4}{8} = 58, \qquad
\text{days to install (one crew)} = \frac{29}{4\times8/4} = 14.5 \rightarrow 15 .$$

Installation plus retrieval is therefore 30 of the 45 days with one crew, leaving 15 for
weather and re-visits — tight but feasible; a second crew shortens the calendar to about
8 + 8 days and is the correct choice if the access window is short. The **land-access budget is
the binding constraint**: 29 sites at 10 sites per week is 2.9 weeks = 20 days of permission
work, which must start long before the installation crew — a plan that begins access work at
mobilisation loses the campaign.

**Duty cycle and visits.** Using the lesson's currents, a 1/6 duty gives 5.06 mA and 230 days
of life, so one visit suffices energetically; the campaign should nevertheless plan **two
visits** — a health check and partial download at day 25, retrieval at day 45 — because a
single visit converts any station fault into a permanent data loss. The second visit costs
29 × 4 = 116 station-hours (58 person-days): the most expensive line in the plan, and still
cheaper than a failed requirement.

**Data volume and bench.** At 100 Hz, three components and four bytes: 9.6 kbit/s per station,
103.68 MB/station/day, so

$$29 \times 45 \times 103.68\ \mathrm{MB} = 135.30\ \mathrm{GB} \text{ raw},
\qquad 45.10\ \mathrm{GB} \text{ at } 3\!:\!1 .$$

Provision three 4 TB staging disks (raw, verified copy, off-site copy), two media readers and a
bench rate of four stations per day → 8 days of bench time, scheduled before the retrieval
visit ends. Storage is never the constraint; the bench and the verification are.

**QC during the campaign.** A daily health beacon (battery, temperature, clock offset, samples
written, clipped counts, free storage) from each station; a weekly automated check that the
station's noise spectrum is unchanged and its clock offset is within the holdover budget; and
an immediate re-visit criterion — for example, any clock offset above 1 ms or any station
silent for 48 h triggers a visit, because the data from that station are already degrading.

**Three risks and their mitigations.**

| Risk | Effect | Mitigation |
|---|---|---|
| Access permission delayed | installation window lost | start access before mobilisation; identify alternate sites |
| Cold-weather battery loss | stations die mid-deployment | derate capacity for the expected minimum temperature; second visit at day 25 |
| Clustered failure (a shared firmware bug) | aperture loss on one side | stage the firmware update on a subset; keep the previous version and a recovery procedure |

The mitigation column is the part of the plan that turns a list of worries into a design.
