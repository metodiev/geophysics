# Solutions — 15-02-07 Marine CSEM and EM for Gas Hydrates

> **All models and data in this module are SYNTHETIC.** Where a problem has more
> than one defensible reading, that is said so. All arithmetic was computed.

Lesson: [07 Marine CSEM and EM](../07-marine-csem-em.md).

$$\delta = 503.3\sqrt{\frac{\rho}{f}}\ \mathrm{m}, \qquad
\text{one-way loss} = 8.686\,\frac{d}{\delta}\ \mathrm{dB}.$$

---

## ★1 — Skin depth, two frequencies

**(a) Seawater, $\rho = 0.30\ \Omega\,\mathrm{m}$:**

$$\delta(0.25) = 503.3\sqrt{\frac{0.30}{0.25}}
= 503.3\sqrt{1.20} = 503.3(1.0954) = 551.3\ \mathrm{m},$$

$$\delta(4) = 503.3\sqrt{\frac{0.30}{4}} = 503.3\sqrt{0.075}
= 503.3(0.27386) = 137.8\ \mathrm{m}.$$

**(b) Sediment, $\rho = 2.0\ \Omega\,\mathrm{m}$:**

$$\delta(0.25) = 503.3\sqrt{8} = 1423.5\ \mathrm{m}, \qquad
\delta(4) = 503.3\sqrt{0.5} = 355.9\ \mathrm{m}.$$

**(c)** The ratios are

$$\frac{1423.5}{551.3} = 2.583, \qquad
\frac{355.9}{137.8} = 2.583 .$$

The ratio is the same at both frequencies because $\delta \propto \sqrt{\rho}$
**only**: the frequency and $\mu_0$ cancel, so
$\delta_{\text{sed}}/\delta_{\text{sw}} = \sqrt{2.0/0.30} = \sqrt{6.667} = 2.582$
at every frequency. Units: $\sqrt{\Omega\,\mathrm{m}/\Omega\,\mathrm{m}}$,
dimensionless ✔.

---

## ★2 — Water-column attenuation and the usable band

**(a)** $d = 2000\ \mathrm{m}$.

| $f$ (Hz) | $\delta$ (m) | one-way (dB) | two-way (dB) |
|---|---|---|---|
| 0.1 | 871.7 | $8.686(2000)/871.7 = 19.93$ | 39.86 |
| 1.0 | 275.7 | $8.686(2000)/275.7 = 63.02$ | 126.04 |

**(b)** $110\ \mathrm{dB}$ of range, two-way propagation: at $0.1\ \mathrm{Hz}$
$39.86\ \mathrm{dB}$ is consumed, leaving $110 - 39.86 = 70.1\ \mathrm{dB}$ for the
sub-seafloor. At $1\ \mathrm{Hz}$ the two-way loss alone is $126.0\ \mathrm{dB}$,
**more than the entire dynamic range**, so that frequency is unusable.
**$0.1\ \mathrm{Hz}$ is the usable choice**; $64\,\%$ of the range remains.

**(c)** The two-way loss equals $110\ \mathrm{dB}$ when the one-way loss is
$55\ \mathrm{dB}$:

$$8.686\frac{2000}{\delta} = 55 \;\Longrightarrow\;
\delta = \frac{8.686(2000)}{55} = 315.9\ \mathrm{m},$$

$$f = \frac{\rho}{(\delta/503.3)^{2}}
= \frac{0.30}{(315.9/503.3)^{2}} = \frac{0.30}{0.3938} = 0.762\ \mathrm{Hz}.$$

**Consequence:** the survey's band must stay **below about $0.76\ \mathrm{Hz}$**,
whatever the target needs. The water column, not the target, sets the ceiling.

---

## ★3 — Choosing the band for a target

**(a)** Criterion $\delta \approx 2d$ with $d = 300\ \mathrm{m}$:

$$\delta = 600\ \mathrm{m} \;\Longrightarrow\;
f = \frac{\rho}{(\delta/503.3)^{2}} = \frac{1.5}{(600/503.3)^{2}}
= \frac{1.5}{1.4212} = 1.055\ \mathrm{Hz}.$$

Criterion $\delta \approx 3d$:

$$f = \frac{1.5}{(900/503.3)^{2}} = \frac{1.5}{3.1979} = 0.469\ \mathrm{Hz}.$$

**(b)** **Band: roughly $0.45$–$1.1\ \mathrm{Hz}$.** It is a band because the
sensitivity is a *resonance-like* trade: too high and the skin depth is smaller than
the target depth, so the fields never reach the layer (the demonstration shows the
anomaly falling to $1.5\,\%$ at $3\ \mathrm{Hz}$); too low and the layer is
electrically thin compared with the skin depth, so its contribution is diluted
exactly as $\omega\mu_0\delta h$ and eventually swamped by the water's screening.

**(c)** $T = \rho h = 20 \times 50 = 1000\ \Omega\,\mathrm{m^{2}}$, against the
host's resistance over the same $50\ \mathrm{m}$, $\rho_{\text{host}}h = 75\
\Omega\,\mathrm{m^{2}}$: a ratio of **13.3**, which sounds like a strong contrast.
But Section 5b shows that ratio is not what controls a plane-wave response. At
$0.9\ \mathrm{Hz}$ the host skin depth is $\delta = 503.3\sqrt{1.5/0.9} = 649.8\
\mathrm{m}$ and the layer's own skin depth is $503.3\sqrt{20/0.9} = 2372.6\
\mathrm{m}$, so

$$\frac{h}{\delta_{\text{host}}} = \frac{50}{649.8} = 0.077, \qquad
\frac{h}{\delta_{\text{layer}}} = \frac{50}{2372.6} = 0.021 .$$

**Both ratios are far below 1, so this is the thin-sheet regime**: the layer's
contribution is the inductive increment $\omega\mu_0h = 2\pi(0.9)(1.2566\times
10^{-6})(50) = 3.55\times10^{-4}\ \Omega$ against a host impedance of
$\omega\mu_0\delta/\sqrt{2} = 3.26\times10^{-3}\ \Omega$ — about $11\,\%$ before the
burial attenuation of $300\ \mathrm{m}$ of sediment, and less than that after it
(the demonstration measures $16\,\%$ for an analogous $100\ \Omega\,\mathrm{m}
\times 100\ \mathrm{m}$ layer at $300\ \mathrm{m}$ depth). **A 13-fold
transverse-resistance contrast is a marginal-to-moderate target** here, because the
signal scales with the layer's thickness rather than with $\rho h$.

---

## ★4 — Testing the transverse-resistance rule

**(a)** $\delta_{\text{layer}} = 503.3\sqrt{\rho/f}$ at each peak frequency:

| $\rho$ ($\Omega$ m) | $h$ (m) | peak $f$ (Hz) | $\delta_{\text{layer}}$ (m) | $h/\delta_{\text{layer}}$ | regime |
|---|---|---|---|---|---|
| 200 | 50 | 0.562 | 9495 | 0.0053 | thin |
| 100 | 100 | 0.422 | 7748 | 0.0129 | thin |
| 50 | 200 | 0.422 | 5478 | 0.0365 | thin |
| 25 | 400 | 0.316 | 4477 | 0.0893 | thin |
| 12.5 | 800 | 0.237 | 3655 | 0.2189 | thin |

**Every layer is thin compared with the skin depth *inside* it**, so the fields do
not attenuate within the layer: all five models are in the thin-sheet regime, not
the "thick layer" regime. Therefore a difference between them cannot be explained by
internal attenuation, and it is the *thickness* (and the buried depth, which fixes
$\delta_{\text{host}}$) that separates them. Taking
$\delta_{\text{host}} = 503.3/\sqrt{f}$ ($1.0\ \Omega\,\mathrm{m}$ host), the ratios
$h/\delta_{\text{host}}$ are $0.074$, $0.129$, $0.258$, $0.447$ and $0.774$ — rising
in the same order as the anomalies ($8.52 \to 114.34\,\%$), because the anomaly
scales with $h$.

**(b)** Compare the two controlled groups:

- **same $h = 100\ \mathrm{m}$, $\rho$ varying by 100×**: $\rho_a = 1.2588$ ($\rho =
  10$), $1.2882$ ($\rho = 100$), $1.2911\ \Omega\,\mathrm{m}$ ($\rho = 1000$) — a
  total spread of $(1.2911-1.2588)/1.2588 = 2.5\,\%$;
- **same $\rho h = 10\,000$, $h$ varying by 100×**: $1.2882$ ($h = 100$), $1.0261$
  ($h = 10$), $1.0026\ \Omega\,\mathrm{m}$ ($h = 1$) — the anomaly falls from $28.8$
  to $2.6$ to $0.26\,\%$, i.e. by a factor of 100.

**The response is a function of $h$, essentially not of $\rho h$ and only weakly of
$\rho$**, in the regime tested. Any statement of the form "CSEM measures the
transverse resistance" therefore needs the geometry to be stated as well.

**(c)** For $h \ll \delta_{\text{layer}}$, $kh \ll 1$ so
$\tanh(kh) \to kh$ and, since $k^{2} = \mathrm{i}\omega\mu_0/\rho$,

$$\rho k\tanh(kh) \to \rho k^{2}h = \mathrm{i}\omega\mu_0 h,$$

a purely **inductive** impedance increment that contains $h$ but not $\rho$. Adding it
to the half-space impedance $Z = (1+\mathrm{i})\omega\mu_0\delta/2$:

$$Z_{\text{tot}} = \omega\mu_0\left[\frac{\delta}{2} +
\mathrm{i}\left(\frac{\delta}{2} + h\right)\right], \qquad
|Z_{\text{tot}}|^{2} = (\omega\mu_0)^{2}\left[\frac{\delta^{2}}{2} + \delta h +
h^{2}\right],$$

$$\rho_a = \frac{|Z_{\text{tot}}|^{2}}{\omega\mu_0}
= \omega\mu_0\left(\frac{\delta^{2}}{2} + \delta h + h^{2}\right).$$

At $f = 0.422\ \mathrm{Hz}$, $\delta = 774.8\ \mathrm{m}$, $h = 100\ \mathrm{m}$:
$\omega\mu_0 = 2\pi(0.422)(1.2566\times10^{-6}) = 3.332\times10^{-6}\
\Omega\,\mathrm{m^{-1}}$ (units: $\mathrm{s^{-1}}\,\mathrm{H\,m^{-1}} = \Omega\,
\mathrm{m^{-1}}$), so

$$\rho_a = 3.332\times10^{-6}\left(\frac{774.8^{2}}{2} + 774.8(100) +
100^{2}\right) = 3.332\times10^{-6}(3.876\times10^{5}) = 1.2915\
\Omega\,\mathrm{m}.$$

**Check:** the recursion gives $1.2882$ ($\rho = 100$) and $1.2911$
($\rho = 1000$) — agreement to $0.3\,\%$ and $0.03\,\%$ respectively, with the
prediction slightly *high* because the expansion ignores the layer's finite
resistance.

**(d)** $h = \delta_{\text{layer}}$ means $\delta = 100\ \mathrm{m}$, i.e.

$$f = \frac{\rho}{\pi\mu_0 h^{2}} = \frac{100}{\pi(1.2566\times10^{-6})(100^{2})}
= \frac{100}{3.948\times10^{-2}} = 2533\ \mathrm{Hz}.$$

**Consequence:** a one-dimensional CSEM sounding at CSEM frequencies cannot resolve
the layer's resistivity, only its thickness; the resistivity enters only if the
survey geometry supplies vertical currents across the layer, which the
offset-dependent controlled source does and a plane-wave sounding does not.

---

## ★5 — Why the plane-wave response fails

**(a)** Conductance is thickness/resistivity:

$$S_{\text{water}} = \frac{1500}{0.30} = 5000\ \mathrm{S}, \qquad
S_{\text{sediment}} = \frac{900}{1.00} = 900\ \mathrm{S}, \qquad
\frac{S_{\text{water}}}{S_{\text{sediment}}} = 5.56 .$$

The target's contribution is $100\ \Omega\,\mathrm{m}$ over $100\ \mathrm{m}$:
$100/100 = 1\ \mathrm{S}$, i.e. $0.02\,\%$ of the water's conductance.

**(b)** Because the water column's conductance is **$5.6$ times** the sediment's and
it is the *first* conductor the plane-wave fields cross, the seafloor impedance is
controlled by the water: the parallel combination is dominated by the
lower-impedance branch, so the measured apparent resistivity
($0.116$–$0.198\ \Omega\,\mathrm{m}$) sits near the water's $0.30\ \Omega\,\mathrm{m}$
and never approaches the sediment's $1.00\ \Omega\,\mathrm{m}$.

**(c)** **Move the source and receivers to the seafloor.** A controlled source
close to the seafloor sends most of its field into the sediment after traversing
metres of water rather than kilometres: the *path* through the water is shortened by
four orders of magnitude ($\sim10\ \mathrm{m}$ instead of $1500\ \mathrm{m}$), so the
exponential attenuation $\exp(-d/\delta)$ of the water is negligible and the
response is controlled by the sediment. The geometry *avoids* the screening instead
of correcting for it.

---

## ★6 — Design a survey

**Model** (all synthetic): $200\ \mathrm{m}$ thick layer of
$50\ \Omega\,\mathrm{m}$ at $250\ \mathrm{m}$ below the seafloor; sediment
$1.0\ \Omega\,\mathrm{m}$; $1500\ \mathrm{m}$ of seawater at $0.30\ \Omega\,\mathrm{m}$.

**(a) Offsets.** The diffusive field from a source decays as
$\exp(-r/\delta_{\text{eff}})$, so offsets must be a few skin depths to be
sensitive to the sub-seafloor, but not so large that the signal falls below noise.
With $\delta_{\text{sed}} = 503.3\sqrt{1.0/0.5} = 711.8\ \mathrm{m}$ at
$0.5\ \mathrm{Hz}$, an offset range of roughly **$0.5$–$6\ \mathrm{km}$** (about one
to eight skin depths) covers the transition from the water-dominated near offset to
the sub-seafloor-dominated far offset. Long offsets help because they force the
currents deeper (the direct water-path arrival decays faster with offset than the
sub-seafloor return), which is exactly the *galvanic* geometry that makes
$\rho h$ matter.

**(b) Frequency band.** Target depth $250\ \mathrm{m}$; best response near
$\delta_{\text{sed}} \approx 2$–$3 \times 250 = 500$–$750\ \mathrm{m}$:

$$f(\delta = 500) = \frac{1.0}{(500/503.3)^{2}} = 1.013\ \mathrm{Hz}, \qquad
f(\delta = 750) = \frac{1.0}{(750/503.3)^{2}} = 0.450\ \mathrm{Hz}.$$

**Band $0.3$–$1.0\ \mathrm{Hz}$**, with the lower end justified by depth penetration
and the upper end by the increased target response (the anomaly grows as
$\omega\mu_0\delta h$ before the fields stop reaching the layer). Water loss at the
ends: at $0.3\ \mathrm{Hz}$, $8.686(1500)/503.3 = 25.9\ \mathrm{dB}$ one-way
($51.8\ \mathrm{dB}$ two-way); at $1\ \mathrm{Hz}$, $47.3\ \mathrm{dB}$ one-way
($94.5\ \mathrm{dB}$ two-way) — near the limit of a $110\ \mathrm{dB}$ system, so the
band is chosen together with the system's dynamic range.

**(c) Array.** The layer is laterally extensive in this 1-D model, so a single
sounding suffices for the layer's *properties*; the array is needed for the
**trend and the background resistivity**. Practical design: 10–20 seafloor receivers
at $500\ \mathrm{m}$–$2\ \mathrm{km}$ spacing along one or two tow lines, with at
least one line crossing to test 2-D/3-D effects. Non-uniqueness is addressed not by
more receivers but by more *independent information*: wide offsets (galvanic), a
second azimuth, and independent constraints on the water resistivity and the
background (logs or MT).

**(d) Error budget, ranked.**

1. **Water resistivity and depth** — the water dominates the response; a $5\,\%$
   error in $\rho_{\text{water}}$ shifts the whole curve. Fix by CTD measurement.
2. **Geometry** — source and receiver positions and the offset, which set the
   amplitude fall-off; a few metres of offset error is a per-cent amplitude error.
3. **Three-dimensional effects** — seafloor topography and lateral resistivity
   changes can mimic or mask a 1-D layer; this is the largest *interpretation*
   error.
4. **Instrument noise and drift** — a lower term because the anomaly sought is tens
   of per cent, but it sets the maximum usable offset.

**(e) Deliverables.**

- **The survey delivers:** a resistivity–depth image along the tow line with a
  stated resolution (here of order tens of metres in depth and tens of per cent in
  resistivity), and a statement of the depth extent of a resistive body.
- **It does not deliver:** a hydrate saturation, a hydrate thickness independent of
  an assumed resistivity, or a resource estimate. Saturation requires an
  Archie-type conversion with its own parameters, and thickness requires the
  resistivity–thickness trade-off to be broken by additional information.

---

## ★7 — When the anomaly is not the target

**(a)** Four physical causes of a band-limited positive apparent-resistivity
anomaly, other than a resistive layer:

1. **A conductive (not resistive) layer above the target** — removes the
   screening and *increases* the apparent resistivity at the frequencies where the
   layer matters.
2. **Seafloor topography or a 3-D resistivity body off the tow line** — changes the
   current paths and produces an offset-dependent amplitude/direction anomaly.
3. **Anisotropy**: a finely layered sediment with a high horizontal resistivity
   looks, to a 1-D isotropic inversion, like a deeper or thicker resistive layer.
4. **Acquisition or processing artefacts**: incorrect receiver orientation
   (rotation of the horizontal components), source waveform/positioning errors, or
   an airwave/mode not modelled by the 1-D response — all frequency-dependent.

**(b)** Independent information that discriminates each:

| cause | discriminating information |
|---|---|
| conductive layer above | its own expression in the higher-frequency band and in the *shape* of the phase curve; a seismic/bathymetric tie |
| topography / 3-D body | crossing tow lines and a 2-D/3-D inversion; bathymetry |
| anisotropy | anisotropy-sensitive offsets (vertical vs horizontal current geometry); core or log data |
| acquisition artefact | receiver compass/orientation record, source navigation, reciprocity check between crossings, record-quality metrics |

**(c)** Prior information to insist on before accepting a hydrate interpretation:

- **The water resistivity and depth**, measured independently — otherwise the
  background of the whole response is unknown.
- **A background resistivity model** from an independent measurement (well log, or a
  previous survey) — a hydrate anomaly is a *difference* from a background, and the
  background is not uniquely determined by the same data.
- **Confirmation that the anomaly is repeatable across independent tow lines** —
  a 1-D-looking anomaly that does not repeat is an artefact or a 3-D effect.
- **Bathymetry and seismic control of the layer's geometry** — hydrate stability,
  and therefore the plausible depth interval, is a pressure–temperature statement
  that comes from depth and temperature, not resistivity.
- **A stated petrophysical relation** before any saturation is quoted, with its
  parameters and uncertainty, since the conversion is an inference rather than a
  measurement.

Each item is necessary because each removes one of the alternative explanations in
(a) or one of the non-uniquenesses the sounding itself cannot break.

---

## Mastery checkpoint — worked answers

**Model:** $2000\ \mathrm{m}$ of seawater at $0.30\ \Omega\,\mathrm{m}$; a
$150\ \mathrm{m}$ layer of $80\ \Omega\,\mathrm{m}$ at $400\ \mathrm{m}$ below the
seafloor; sediment $1.2\ \Omega\,\mathrm{m}$.

**(a) Water column.**

| $f$ (Hz) | $\delta_{\text{sw}}$ (m) | one-way loss (dB) |
|---|---|---|
| 0.1 | $503.3\sqrt{0.3/0.1} = 871.7$ | $8.686(2000)/871.7 = 19.93$ |
| 0.5 | $503.3\sqrt{0.3/0.5} = 389.9$ | $8.686(2000)/389.9 = 44.56$ |
| 2.0 | $503.3\sqrt{0.3/2.0} = 194.9$ | $8.686(2000)/194.9 = 89.12$ |

**(b) Sediment skin depth.**

| $f$ (Hz) | $\delta_{\text{sed}}$ (m) | $2d$ with $d = 400\ \mathrm{m}$ |
|---|---|---|
| 0.1 | $503.3\sqrt{1.2/0.1} = 1743.5$ | too deep-penetrating (thin-layer dilution) |
| 0.5 | $503.3\sqrt{1.2/0.5} = 779.7$ | $\approx 2 \times 400 = 800$ ✔ |
| 2.0 | $503.3\sqrt{1.2/2.0} = 389.9$ | $\approx 400$: marginal, fields barely reach the layer |

**$0.5\ \mathrm{Hz}$ is best suited to a $400\ \mathrm{m}$ target**, because that is
where $\delta_{\text{sed}} \approx 2d$; comparing (a) and (b), it is also the highest
frequency whose two-way water loss ($89.1\ \mathrm{dB}$) still fits inside a
$110\ \mathrm{dB}$ system.

**(c)** The water's conductance is $2000/0.30 = 6667\ \mathrm{S}$, vastly larger than
that of any sediment interval beneath; the seafloor impedance is the parallel
combination of the up-looking (water) and down-looking (sediment) impedances, so the
lower-impedance branch dominates and the apparent resistivity returns the water's
value at every frequency in the band. **Fix: put the source and receivers at or near
the seafloor**, so the path through the water is metres instead of kilometres and the
sub-seafloor fields are no longer screened.

**(d)** The layer's own skin depth at $0.5\ \mathrm{Hz}$ is
$503.3\sqrt{80/0.5} = 6366\ \mathrm{m}$, so

$$\frac{h}{\delta_{\text{layer}}} = \frac{150}{6366} = 0.024, \qquad
\frac{h}{\delta_{\text{host}}} = \frac{150}{779.7} = 0.192 .$$

Both are much less than 1 — the **thin-sheet regime** — so the response is governed
by the *thickness* $150\ \mathrm{m}$ rather than by $\rho h = 80 \times 150 =
12\,000\ \Omega\,\mathrm{m^{2}}$. Applying the lesson's thin-sheet formula *at the
seafloor*, $\omega\mu_0(\delta h + h^{2}) = 2\pi(0.5)(1.2566\times10^{-6})(779.7
\times150 + 150^{2}) = 0.551$, would be a $+55\,\%$ anomaly; buried $400\ \mathrm{m}$
deep, the increment propagates up through the overburden and the demonstrated
analogue ($100\ \Omega\,\mathrm{m} \times 100\ \mathrm{m}$ at $300\ \mathrm{m}$ depth)
gives $16.15\,\%$. **So the statement is: the layer's thickness is measurable, its
resistivity is not, from this geometry** — and any quoted thickness is conditional on
the resistivity assumed for the conversion.
