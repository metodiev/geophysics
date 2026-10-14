# Solutions — 11-02-05 Radiometrics and Alteration Mapping

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All concentrations, sensitivities and stripping ratios are
> **SYNTHETIC**; the air density and the air mass attenuation coefficients are the
> standard constants stated in the lesson.

Lesson: [05 Radiometrics and Alteration Mapping](../05-radiometrics-for-minerals.md).

---

## ★1 — Soil attenuation

$$\mu = \left(\frac{\mu}{\rho}\right)\rho = 0.06 \times 1.9 = 0.114\
\mathrm{cm^{-1}}, \qquad
\mathrm{HVL} = \frac{\ln 2}{0.114} = 6.08\ \mathrm{cm},$$

transmitted through $25\ \mathrm{cm}$:
$$e^{-0.114(25)} = e^{-2.85} = 0.0578\quad(5.8\%).$$

**94.2% of the bedrock flux is lost through a quarter of a metre of soil.** The
same coverage over rock at $\rho = 2.7$ would lose more still, because the linear
coefficient scales with density. This one number is why radiometrics is described
as a surface method.

---

## ★2 — Height response of the K window

$$R(h) = E_2(\mu_K h), \qquad \mu_K = 6.49\times10^{-3}\ \mathrm{m^{-1}}.$$

| $h$ (m) | $\mu_Kh$ | $E_2(\mu_Kh)$ |
|---|---|---|
| 0 | 0.000 | 1.00000 |
| 50 | 0.325 | 0.44754 |
| 100 | 0.649 | 0.25487 |
| 200 | 1.299 | 0.09665 |

At $100\ \mathrm{m}$ the count rate is **25.5%** of the ground-level rate — a
factor of $3.92$. Note that a pure exponential with the same coefficient would give
$e^{-0.649} = 0.5226$, more than twice as large: **the plane-source geometry
attenuates faster than a beam**, because the flux is dominated by paths from a
region of radius $\sim2/\mu$ rather than by the vertical path alone.

---

## ★3 — Stripping round trip

Sensitivities $\mathbf{s} = (95.0, 4.2, 2.4)$ counts s⁻¹ per unit;
$\mathbf{S}$ as in the lesson. The concentrations first become "source strengths"

$$\mathbf{s}\odot\mathbf{c} = (285.0,\ 16.8,\ 19.2),$$

then the window count rates

$$\mathbf{w} = \mathbf{S}(\mathbf{s}\odot\mathbf{c}) =
(285.0 + 5.04 + 1.92,\ 14.25 + 16.8 + 5.76,\ 0 + 0.84 + 19.2)
= (291.96,\ 36.81,\ 19.20)\ \mathrm{counts\,s^{-1}}.$$

Inverting: $\mathbf{S}^{-1}\mathbf{w} = (285.0, 16.8, 19.2)$, dividing by the
sensitivities gives $K = 3.000\%$, $eU = 4.000$ ppm, $eTh = 8.000$ ppm. The
round trip is exact to machine precision (worst error $1.8\times10^{-15}$ over four
rock types in the demonstration) because a $3\times3$ solve is well conditioned
here, with $\kappa = 1.588$.

---

## ★4 — Counting statistics

$$\frac{\sigma_N}{N} = \frac{1}{\sqrt{NT}}, \qquad N = 250\ \mathrm{counts\,s^{-1}}:$$

| $T$ (s) | counts $NT$ | $\sigma/N$ |
|---|---|---|
| 30 | 7 500 | 0.011547 |
| 300 | 75 000 | 0.003651 |
| 3000 | 750 000 | 0.001155 |

**Ratio of the 30 s to the 3000 s uncertainty = 10.0**, exactly
$\sqrt{3000/30} = 10$: the uncertainty falls as $T^{-1/2}$, so a hundredfold
increase in counting time buys one decade of precision. This is the arithmetic
behind "fly fast and wide": precision is expensive and coverage is cheap, and the
signal-to-noise ratio is usually already enormous.

---

## ★5 — The Th/K height bias

Ground ratio 4.30. Measured ratio at height $h$:

$$\left(\frac{\mathrm{Th}}{\mathrm{K}}\right)_{h}
= 4.30\,\frac{E_2(\mu_{\text{Th}}h)}{E_2(\mu_K h)} .$$

| $h$ (m) | $R_{\text{Th}}/R_K$ | measured Th/K |
|---|---|---|
| 80 | 1.3433 | 5.776 |
| 160 | 1.6603 | 7.139 |

$$\text{difference} = \frac{7.139 - 5.776}{5.776} = +23.6\% .$$

**Implication for a draped survey over $80\ \mathrm{m}$ of relief:** if the aircraft
holds a constant altitude above ground, the *terrain-following* height is
constant and no drift appears; if instead the survey is flown at constant
barometric altitude, the terrain height changes by $80\ \mathrm{m}$ and the
apparent Th/K changes by order $10\%$ **across the map with no ground change**. The
$23.6\%$ computed here for a $80\ \mathrm{m}$ height change is that effect at
larger amplitude. The mapping consequence is unambiguous: height correction must be
applied before ratios are computed, and the height must be the *above-ground*
height, not the barometric altitude.

---

## ★6 — Which ratio is the better discriminator

| quantity | host | altered | change |
|---|---|---|---|
| Th/K | $9.0/2.0 = 4.500$ | $7.0/4.2 = 1.667$ | $-63.0\%$ |
| K/(K+U+Th) | $2.0/12.8 = 0.15625$ | $4.2/13.6 = 0.30882$ | $+97.6\%$ |

**Both are strong; the ratio index is the better discriminator here** (a $98\%$
change against $63\%$), because it normalises all three channels at once and is
therefore insensitive to a locally high or low overall radioelement level.

**Counting uncertainty at $T = 120\ \mathrm{s}$.** Window count rates at the
demonstration's sensitivities:

| rock | K (c/s) | U (c/s) | Th (c/s) |
|---|---|---|---|
| host | 194.43 | 23.54 | 21.60 |
| altered | 403.70 | 35.07 | 16.80 |

Relative uncertainties $1/\sqrt{NT}$: host $(0.00655, 0.01882, 0.01964)$; altered
$(0.00454, 0.01541, 0.02227)$.

$$\sigma_{\text{Th/K}} = \frac{\mathrm{Th}}{\mathrm{K}}
\sqrt{\left(\frac{\sigma_{\mathrm{Th}}}{\mathrm{Th}}\right)^{2}
+ \left(\frac{\sigma_{\mathrm{K}}}{\mathrm{K}}\right)^{2}}
= 4.5\sqrt{0.01964^{2} + 0.00655^{2}} = 0.0932$$

for the host, and $1.667\sqrt{0.02227^{2}+0.00454^{2}} = 0.0379$ for the altered
zone. The separation between them is

$$\frac{4.500 - 1.667}{\sqrt{0.0932^{2}+0.0379^{2}}} = \frac{2.833}{0.1006}
= 28.2\sigma .$$

**The discrimination is not counting-noise limited** at all: even at a
$120\ \mathrm{s}$ integration and with a modest count rate, a $63\%$ ratio contrast
is a $28\sigma$ effect. The limits on this method are cover, calibration and
disequilibrium — never counting statistics.

---

## ★7 — Conditioning and error amplification

$$\mathbf{S} = \begin{pmatrix}1&0.4&0.2\\0.1&1&0.4\\0&0.05&1\end{pmatrix},
\qquad \sigma = (1.41217,\ 0.93001,\ 0.71650), \qquad \kappa = 1.9709 .$$

Forward model for $\mathbf{c} = (3, 3, 8)$:
$\mathbf{w} = (293.88,\ 48.78,\ 19.83)$ counts s⁻¹. Perturbing the U window by
$+1\%$ and inverting:

| matrix | $\kappa$ | $\Delta$K (%) | $\Delta$eU (%) | $\Delta$eTh (%) |
|---|---|---|---|---|
| lesson matrix | 1.588 | −0.035 | **+2.63** | 0.00 |
| this matrix | 1.971 | −0.071 | **+4.11** | −0.135 |

**A $24\%$ increase in the condition number raises the error amplification in eU
from $2.6\times$ to $4.1\times$.** Note that the amplification *exceeds* $\kappa$
for the eU component: the condition number bounds the worst-case amplification of
the vector norm, whereas the per-component relative error also depends on how much
of a window's counts come from the element of interest. Here K contributes
$95\ \mathrm{c/s}$ per %K while eU contributes only $4.2$ per ppm, so a
$1\%$ error in a U window that is mostly fed by Th (the $0.30$ stripping term) is
a large relative error in a small quantity.

**Practical consequence.** Stripping amplifies errors in proportion to its
conditioning, and the amplification is worst for the *weakest* signal. A stripping
matrix must be verified — by pads, by a test range, or by the closure of the
round trip within the survey — because a wrong matrix produces not noise but
*correlated bias*, with negative concentrations as its visible symptom.

---

## ★8 — Drift with a different Th coefficient

Take $\mu_{\text{Th}} = 1.2\mu_K = 7.79\times10^{-3}\ \mathrm{m^{-1}}$:

| $h$ (m) | $R_{\text{Th}}/R_K$ |
|---|---|
| 60 | 0.8708 |
| 120 | 0.7885 |
| 180 | 0.7196 |

The ratio now **decreases** with height by about $17\%$ over $180\ \mathrm{m}$,
the opposite sign to the physical case.

**Why the sign is fixed by physics.** Gamma attenuation in the photopeak region is
a decreasing function of photon energy: higher-energy photons interact less, so
$\mu_{\text{Th}} < \mu_K$ because Th's window sits at $2.61\ \mathrm{MeV}$ against
K's $1.46\ \mathrm{MeV}$. It follows that $E_2(\mu_{\text{Th}}h) > E_2(\mu_K h)$
for every $h > 0$, and therefore the Th/K ratio **must increase with height** —
the sign does not depend on the exact coefficients, only on their ordering. That
is why height correction of Th/K is not a modelling choice but a physical
necessity with a known direction: uncorrected Th/K over-estimates Th in high
terrain and under-estimates it in valleys.

---

## ★9 — Survey design for a $40\%$ Th/K halo

**Requirement.** Host Th/K $= 5.0$; halo contrast $40\%$, i.e.
$\Delta(\mathrm{Th/K}) = 2.0$. Require $\ge3\sigma$ per pixel, so
$\sigma_{\text{Th/K}} \le 0.667$.

**Counting.** With $N_K = 200\ \mathrm{counts\,s^{-1}}$ at $60\ \mathrm{m}$ and a
Th/K ratio of 5, the Th count rate is of order $N_{\mathrm{Th}} \approx 24\
\mathrm{counts\,s^{-1}}$ for the host (using the demonstration's proportions). The
ratio uncertainty is

$$\sigma_{\text{Th/K}} \approx 5\sqrt{\frac{1}{N_{\mathrm{Th}}T}
+ \frac{1}{N_KT}} = 5\sqrt{\frac{1}{T}\left(\frac{1}{24} + \frac{1}{200}\right)}
= 5\sqrt{\frac{0.04667}{T}} .$$

Setting this to $0.667$ gives $T = 5^{2}(0.04667)/0.667^{2} = 2.62\ \mathrm{s}$ of
counting per pixel — *two and a half seconds*.

**Geometry.** At a ground speed of $70\ \mathrm{m\,s^{-1}}$ ($250\ \mathrm{km\,h^{-1}}$)
a $2.62\ \mathrm{s}$ integration gives a pixel of $183\ \mathrm{m}$ along line; a
detector footprint at $60\ \mathrm{m}$ height is of order $120$–$200\
\mathrm{m}$ across, so the pixel and the footprint are comparable and line spacing
of $200\ \mathrm{m}$ gives contiguous coverage.

**Cost driver.** Line kilometres, not counting time: halving the line spacing
doubles the cost, while halving the integration time is free in this design.

**The assumption that would invalidate it.** That the halo's *surface* expression
exists — i.e. that the alteration reaches the soil or outcrops. If transported
cover of $20\ \mathrm{cm}$ intervenes, the transmitted fraction is
$\exp(-0.06\times1.7\times20) = 0.130$, the count rate falls by a factor of
$7.7$, and the required integration time rises by that factor to $20\
\mathrm{s}$ per pixel, i.e. a $1400\ \mathrm{m}$ pixel at
$70\ \mathrm{m\,s^{-1}}$ —
which no longer resolves the halo. **The design is coupling-limited, not
photon-limited, and the coupling assumption is the one to test first** — by soil
sampling or a ground radiometric traverse.

---

## ★10 — Disequilibrium and the U channel

Model $D = {}^{214}\mathrm{Bi}/{}^{238}\mathrm{U}$ with $0.6 \le D \le 1.4$; the
reported eU is $D\times$ the true uranium equivalent, because the window measures
the daughter.

Take a host with U $= 2.0$ ppm, K $= 2.0\%$, Th $= 10.0$ ppm, so ground
Th/K $= 5.00$.

| quantity | true | at $D = 1.4$ | at $D = 0.6$ |
|---|---|---|---|
| reported eU (ppm) | 2.0 | 2.8 | 1.2 |
| Th/K | 5.00 | 5.00 | 5.00 |
| K/(K+U+Th) | $2/14 = 0.1429$ | $2/14.8 = 0.1351$ | $2/13.2 = 0.1515$ |

**(a) reported eU:** biased by $\pm40\%$, directly.
**(b) Th/K:** **unchanged**, because neither Th nor K appears in the U channel
(except through the stripping corrections, which are fractions of a window and
therefore second order).
**(c) K/(K+U+Th):** biased by $-5.4\%$ to $+6.0\%$.

**Most robust:** Th/K, and by construction — it contains no U at all. The
K/(K+U+Th) index is the *worst*, because it puts the disequilibrium-affected
channel in the denominator with a weight that is large when U is a substantial
fraction of the total.

**How to detect it in a survey's own data.** Three tests, all using only the
survey: (i) compare the airborne eU map with a **ground gamma-spectrometer**
traverse or with soil geochemistry at sample points — a systematic offset that is
spatially coherent indicates disequilibrium rather than noise; (ii) look for an
**anti-correlation between eU and the local relief or soil moisture**, the
signature of radon migration; (iii) check the **eU/eTh ratio's spatial structure**:
disequilibrium produces a smooth, regional gradient in eU that does not follow the
geology. The diagnostic to avoid is treating a radon anomaly as uranium
enrichment, which is the classic false positive of the method.

---

## ★11 — Transported cover as an explanation

$$\mu = (0.06)(1.7) = 0.102\ \mathrm{cm^{-1}},
\qquad e^{-0.102(20)} = e^{-2.04} = 0.130 .$$

**A $20\ \mathrm{cm}$ cover transmits $13\%$ of the bedrock flux** — a suppression
by a factor of $7.7$, which is more than enough to remove an anomaly of a few tens
of per cent. The cover thickness that reduces the signal by $90\%$:

$$e^{-\mu d} = 0.1 \;\Longrightarrow\; d = \frac{\ln 10}{0.102} = 22.6\
\mathrm{cm}.$$

**Twenty-three centimetres of soil is all it takes.** This is why "no anomaly" and
"no target" are different statements.

**Two measurements to test the hypothesis.**

1. **A soil profile or auger traverse** recording cover thickness and radioelement
   content at the surface. *Failure looks like:* uniform thickness and soil
   radioelement contents that track the bedrock pattern — in which case the cover
   is transmitting the pattern and the suppression explanation fails.
2. **A ground gamma-spectrometer traverse** with the detector at $0$ and $1\
   \mathrm{m}$ (or with the source exposed by scraping a shallow pit). *Failure
   looks like:* the count rate increasing steeply with a small increase in
   exposure time-height product, which indicates that the signal is coming from
   *within* the soil, not from bedrock beneath it.

The two measurements answer different questions: (1) asks whether the cover is
thick, (2) asks whether the observed flux originates below the cover. A cover can
be thick and still transmit a pattern if its own radioelement content is
inherited from the bedrock; it can be thin and still mask the bedrock if its
content is unrelated. Reporting "cover" as an explanation therefore requires both,
and the second is the one usually omitted.
