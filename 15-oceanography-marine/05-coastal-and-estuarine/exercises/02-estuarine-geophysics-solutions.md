# Solutions — 15-05-02 Estuarine and Delta Geophysics

> **Read after attempting the exercises.** Lesson:
> [02 Estuarine and Delta Geophysics](../02-estuarine-geophysics.md). Numbers are
> SYNTHETIC model values.

## ★ Foundational

## ★1 — Density and sound speed

$$\rho=1028\left[1-2.0\times10^{-4}(15-10)+7.8\times10^{-4}(20-35)\right]
=1028\left[1-0.0010-0.0117\right]=1028\times0.9873=1014.9\
\mathrm{kg\,m^{-3}},$$

$$c=\sqrt{\frac{2.34\times10^{9}}{1014.9}}=\sqrt{2.3057\times10^{6}}
=1518.5\ \mathrm{m\,s^{-1}} .$$

Cross-check against the lesson's table: $c(10,35)=1508.7$ and $c(0,0)=1528.2$;
the value here sits between them, as it must for intermediate $T$ and $S$.

## ★2 — Classification

$$u_r=\frac{150}{700\times7}=0.03061\ \mathrm{m\,s^{-1}},\qquad
g'=\frac{9.80665\times8}{1028}=0.07632\ \mathrm{m\,s^{-2}},$$

$$\sqrt{g'h}=\sqrt{0.07632\times7}=\sqrt{0.5343}=0.7309\ \mathrm{m\,s^{-1}},
\qquad \mathrm{Fr}_d=\frac{0.03061}{0.7309}=0.0419 .$$

$0.02<\mathrm{Fr}_d<0.2$: **partially mixed** under the lesson's model thresholds.
The classification is a model statement: a different threshold scheme would call
the same estuary "weakly stratified", and the physics (a river flow well below the
internal wave speed, with tidal mixing comparable to the river flow) is the part
that does not depend on the scheme.

## ★3 — Intrusion length

$$L_d=\frac{K_x}{u_r}=\frac{150}{0.03}=5000\ \mathrm{m}=5.0\ \mathrm{km},$$

$$x_{1\,\mathrm{g/kg}}=L_d\ln\frac{30}{1}=5.0\times3.4012=17.0\ \mathrm{km}.$$

## ★★ Applied

## ★4 — Sounding error at two depths

$$e(z)=-\frac{a z^{2}}{2}.$$

- At 20 m: $e=-3.0\times10^{-4}\times400/2=-0.060$ m ($-0.30\%$).
- At 60 m: $e=-3.0\times10^{-4}\times3600/2=-0.540$ m ($-0.90\%$).

The error grows as $z^2$ because the *relative* velocity error accumulates
proportionally to depth while the error in travel time — which is what the depth
is computed from — accumulates proportionally to $z^2/2$: a fractional error $az$
in speed converts into a fractional depth error $az/2$, so the absolute error is
$a z^2/2$. **At 60 m the error (0.54 m) is already larger than the 0.1–0.2 m of
change that many monitoring programmes are trying to detect.**

## ★5 — Accommodation, equilibrium and fill time

$$\text{accommodation}=A_0k=50\times10^{6}\times0.005=2.5\times10^{5}\
\mathrm{m^3\,yr^{-1}},$$

$$\text{net initial rate}=Q_s-A_0k=3.0\times10^{5}-2.5\times10^{5}
=5.0\times10^{4}\ \mathrm{m^3\,yr^{-1}},$$

$$A_{\text{eq}}=\frac{Q_s}{k}=\frac{3.0\times10^{5}}{0.005}=60\ \mathrm{km^2}
\quad(>50\ \mathrm{km^2}\text{, so the basin fills}),$$

$$t_{\text{with}}=\frac{d}{k}\ln\frac{A_{\text{eq}}}{A_{\text{eq}}-A_0}
=\frac{5}{0.005}\ln\frac{60}{10}=1000\times1.7918=1792\ \mathrm{yr},$$

$$t_{\text{without}}=\frac{A_0d}{Q_s}=\frac{50\times10^{6}\times5}{3.0\times10^{5}}
=833\ \mathrm{yr}.$$

The rise lengthens the fill by 115%. A constant-net-rate estimate,
$A_0/(\text{net}/d)=50\times10^{6}/10^{4}=5000$ yr, **overestimates** the fill
time by 2.8× because it holds the accommodation at its initial value while the
accommodation in fact shrinks as the basin fills.

## ★6 — Adding subsidence

The accommodation rate becomes $(k+w)A_0$ with $w=2\ \mathrm{mm\,yr^{-1}}$, so
$k_{\text{total}}=7\ \mathrm{mm\,yr^{-1}}$:

$$A_{\text{eq}}=\frac{Q_s}{k_{\text{total}}}=\frac{3.0\times10^{5}}{0.007}
=42.9\ \mathrm{km^2}\quad(<50\ \mathrm{km^2}).$$

**The change is qualitative, not quantitative**: the equilibrium area is now
smaller than the present basin, so the basin does *not* fill — it shrinks toward
42.9 km² and then stays there, with the supply exactly balancing the
accommodation. The 2 mm/yr of subsidence, which is 40% of the sea-level term and
is invisible to a tide gauge that shares the motion, converts a filling basin into
a permanent embayment. This is the arithmetic that underlies every "is the delta
keeping up?" assessment.

## ★★★ Research-oriented

## ★7 — Survey design for a 12 km estuary

| component | what | where and how often | measured | modelled |
|---|---|---|---|---|
| sound-speed profiling | CTD casts (temperature, salinity) to the bed | at 500 m spacing along the channel (25 casts), plus one repeat at the spring and neap tides | $T$, $S$, hence $\rho$ and $c(z)$ | the depth-error correction and the refraction correction |
| sub-bottom | chirp, 2–8 kHz, 0.25 m vertical resolution | same tracklines, tied to the CTD stations for velocity control | acoustic impedance contrasts and reflector geometry | the geological interpretation (channel fill, tidal flats, drape) and the depth conversion |
| resistivity or EM | floating or towed array, 20–100 m electrode/spacing dependent | three transects across the channel plus one along it | bulk conductivity and its spatial pattern | the salinity of the pore fluid via a porosity–saturation model |
| water-column salinity | the CTD grid | as above | salinity | the intrusion length via $K_x$ |

**The two assumptions that most affect the intrusion length:**

1. **$K_x$ constant.** The lesson's model gives $L\propto1/Q$; real estuaries
   weaken that scaling because $K_x$ grows with tidal energy and flow. *Test:* run
   the CTD grid at two very different river discharges (a dry spell and a flood)
   and fit $L$ against $Q$; the fitted exponent is the empirical answer, and it
   will not be −1.
2. **The isohaline chosen for the "intrusion length".** $L_d$ and the 1 g/kg
   distance differ by the factor $\ln(S_0/S_{\text{threshold}})$, i.e. 3.4 for the
   lesson's numbers. *Test:* it is not testable — it is a definition, so it must be
   stated and reported consistently.

A third assumption that affects the *stratigraphy* rather than the intrusion is the
depth conversion of the sub-bottom data: it uses the sound-speed profile from the
CTD stations, interpolated between them, and a 1% velocity error at 20 m of
penetration is a 0.2 m depth error — comparable to the thickness of the drape
being mapped.

## ★8 — Is the delta drowning?

| term | size (model scale) | how measured | comment |
|---|---|---|---|
| eustatic sea-level rise | 2–5 mm/yr | satellite altimetry plus tide gauges, with the vertical-land-motion correction | the global term; well determined at the global scale, not locally |
| compaction (natural) | 1–10 mm/yr | repeat levelling, benchmark networks, sediment geotechnical tests | fastest in the first decades after deposition; decays |
| tectonic subsidence | 0–10 mm/yr | GNSS on bedrock, repeated levelling tied to stable marks | regional and steady |
| anthropogenic subsidence (fluid extraction, drainage) | 0–100 mm/yr | InSAR time series over the delta, GNSS, extensometers | the term that dominates in many deltas and the one most easily misattributed |
| sediment supply | 10⁵–10⁶ m³/yr | river gauging plus load sampling, and a reservoir trap-efficiency correction | the term most changed by upstream dams |

**What a tide gauge alone cannot separate:** it measures *relative* sea level, i.e.
the sum of eustatic rise, compaction, tectonic subsidence and anthropogenic
subsidence. A gauge reading 8 mm/yr cannot tell whether the region is rising
slowly with fast subsidence or the reverse.

**Distinguishing a supply deficit from a subsidence excess.** Both produce a
retreating shoreline and a deepening basin, but they differ in what happens to the
*area* and the *sedimentology*:

- a supply deficit reduces the volume delivered, and the basin's *deposition rate*
  falls everywhere it used to be fed (fine-grained deposits thin, progradation
  slows);
- a subsidence excess leaves the supply unchanged, so deposition continues at the
  same rate while the basin deepens, producing thicker but more widespread
  deposition and a *change in accommodation distribution*, not in the delivered
  volume.

The discriminating observation is therefore a **sediment budget with an
independent supply measurement** (gauging above the delta) combined with a **spatial
pattern of subsidence** from InSAR or a GNSS network: if the measured supply is
unchanged and the basin still deepens, the deficit is subsidence. Neither a
shoreline trend nor a single tide gauge can do it.

**The observation that neither can distinguish** is the split between *natural
compaction* and *anthropogenic extraction*, once the total subsidence is known.
Both act on the same ground, both change over time, and separating them requires
either a pre-development baseline (which rarely exists) or a physical model of
compaction — a model, not a measurement.
