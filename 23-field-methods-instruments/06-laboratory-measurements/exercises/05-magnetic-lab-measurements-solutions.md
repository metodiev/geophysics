# Solutions — 23-06-05 Laboratory Magnetic Susceptibility and Remanence

The lesson is [05 Magnetic Laboratory Measurements](../05-magnetic-lab-measurements.md). All
values are **SYNTHETIC**.

## ★1

$$\chi_{\text{mass}} = \frac{\kappa}{\rho} = \frac{2.5\times10^{-3}}{2700}
= 9.2593\times10^{-7}\ \mathrm{m^{3}/kg},$$

$$\kappa_{\text{cgs}} = \frac{\kappa_{\text{SI}}}{4\pi}
= \frac{2.5\times10^{-3}}{12.5664} = 1.9894\times10^{-4}\ \mathrm{emu/cm^{3}},$$

$$\chi_{\text{cgs,mass}} = \frac{1.9894\times10^{-4}}{2.700}
= 7.3683\times10^{-5}\ \mathrm{cm^{3}/g} .$$

Omitting the $4\pi$ gives a value $12.5664\times$ too large — the single most common
magnetic-unit error, and the reason the lesson's rule is to state both the system and the
normalization. Note also that the mass-specific conversions differ by 1000 between the SI
and cgs columns ($9.2593\times10^{-7}$ m³/kg and $7.3683\times10^{-5}$ cm³/g are the same
number once the $4\pi$ is removed), because 1 m³ = 10⁶ cm³ and 1 kg = 1000 g.

## ★2

$$\frac{\kappa_{\text{app}}}{\kappa_0} = \frac{1}{1 + H/H_s} :$$

| $H$ (A/m) | Ratio |
|---|---|
| 25 | 0.8000 |
| 100 | 0.5000 |
| 400 | 0.2000 |

A factor of four in the measuring amplitude changes the reported susceptibility by a factor
of four at the top of this range. This is why the lesson insists that the amplitude is part
of the result: two laboratories can both be correct and disagree by a factor of four.

## ★3

$$\frac{\text{IRM}(H)}{\text{SIRM}} = \frac12\left[1 +
\mathrm{erf}\left(\frac{\ln(H/100)}{1.6282}\right)\right] :$$

| $H$ (mT) | IRM/SIRM |
|---|---|
| 30 | 0.1478 |
| 100 | 0.5000 |
| 300 | 0.8300 |
| 1000 | 0.9772 |

A value of 0.5 at 300 mT instead of 0.8300 would mean the coercivity distribution is
**shifted to higher fields by a factor of three** — i.e. the same *shape* of curve (the same
$\sigma$) centred at 300 mT rather than 100 mT. Physically that is a more
high-coercivity assemblage: hematite-like rather than magnetite-like. Note the important
distinction: the mid-point field tells you *which* mineral, and the slope through the
mid-point tells you the *spread* of coercivities. The lesson's parameters give a spread of
one decade in $H$ ($\sigma = \ln(10)/2$, so roughly a factor of 10 of coercivity range),
and both the mid-point and the slope should be reported, because either alone is ambiguous.

## ★4

$$\frac{\text{ARM}}{\text{SIRM}} = \frac{0.11}{1.10} = 0.1000
\quad\text{and}\quad \frac{0.022}{1.10} = 0.0200 .$$

The **first specimen** (0.1000) is the finer-grained. The ARM is acquired only by grains
whose coercivity can respond to the alternating field but which are small enough to be
single-domain-like; a coarse multi-domain assemblage is efficient at acquiring a large
SIRM (more material, and domain walls move easily) but poor at acquiring an ARM. So a high
ARM/SIRM at equal SIRM means a larger *fraction* of the magnetic material is in the fine
size range.

The **first** specimen would dominate a palaeomagnetic signal, because the fine
single-domain-like grains are the stable remanence carriers, while the coarse multi-domain
grains acquire a large but unstable and easily reset remanence. This is why the ARM/SIRM
ratio is a proxy for the *palaeomagnetic reliability* of a specimen, and why a specimen
with a high SIRM but a low ARM/SIRM is a poor palaeomagnetic recorder no matter how
strongly magnetic it is.

## ★5

$$\frac{\kappa_{\text{app}}}{\kappa} = 1 + \frac{V_{\text{holder}}}{V_{\text{sample}}} :$$

| $V_{\text{sample}}$ | Ratio |
|---|---|
| 1.0 cm³ | 1.3000 |
| 5.0 cm³ | 1.0600 |
| 20.0 cm³ | 1.0150 |

For a 2 % tolerance, $0.30/V \le 0.02 \Rightarrow V \ge 15.0$ cm³. The lesson's specimen-size
conclusion is therefore general: with a fixed holder, the tolerance *sets* the minimum
specimen volume, and the smallest specimens carry the largest systematic error — which must
be reported rather than corrected, unless the holder is measured empty in the same session
and position.

## ★6

A model answer.

**Measurements, in order.** (1) Mass and volume of each chip by the same method used for the
bulk (see [01](../01-sample-preparation.md)); (2) low-field susceptibility at a stated
amplitude, with the holder measured empty immediately before and after; (3) ARM with a
stated bias field and AF peak, after AF demagnetization at a peak high enough to remove the
natural remanence; (4) stepwise IRM acquisition to 1 T, giving $H_{1/2}$, SIRM and the
curve shape; (5) back-field demagnetization to −300 mT for the S-ratio. Temperature
dependence (Curie or low-temperature) would be the next step for mineral identification, and
is the only measurement here that identifies a mineral rather than classifying it.

**Corrections.** Holder background subtracted using the empty measurement; mass normalization
per measured chip (not per bulk specimen); the demagnetization (shape) correction for the
chips' geometry, which is larger for an elongated chip than for a cylinder and should be
bounded; the ARM protocol recorded because the ratio is protocol-dependent.

**The tolerances cannot be met, and here is the arithmetic.** A chip of 0.4 cm³ with a holder
equivalent volume of 0.30 cm³ has $\kappa_{\text{app}}/\kappa = 1 + 0.30/0.4 = 1.75$, a
**+75 %** error; at 1.5 cm³ it is +20 %. Even with a perfect empty-holder subtraction, the
residual (positioning, packing, chip irregularity) is of order 1–2 % of the *holder* term,
i.e. $\sim 0.30/0.4 \times 0.02 = 1.5$ % on the smallest chips — so the **1 % target fails
by about a factor of two on reproducibility alone**, and the achievable tolerance is roughly
±3 % for the small chips and ±1.5 % for the largest. The remanence tolerances are less
affected by volume (a moment measurement is not a volume ratio) but the chips' irregular
shape and their orientation in the holder give ±3–5 % rather than 2 %.

**What the ratios still deliver.** This is the point that saves the programme: the
ARM/SIRM ratio, the S-ratio, the median coercivity $H_{1/2}$ and the shape of the IRM curve
are all **ratios or shape parameters**, so a common volume error cancels, and the
amplitude-dependent errors largely cancel too. With ±3 % on each of two measurements the
ratio's uncertainty is ±4.2 %, enough to separate fine from coarse grain-size populations by
a factor of two or more (the synthetic examples differ by factors of 5–10), and enough to
distinguish a low-coercivity from a high-coercivity assemblage (a factor of three in
$H_{1/2}$). So the deliverable is: relative mineral proportions and grain-size
classification across the 20 chips — *not* absolute susceptibilities.

**What cannot be supported.** Absolute magnetite or hematite *percentages*, or absolute
susceptibilities of the chips. Mineral quantification needs the concentration of each phase,
which requires either a saturation-magnetization calibration per mineral (with its own
uncertainty) or an independent mineralogical measurement. The programme measures magnetic
*response* ratios and cannot convert them into mineral percentages without that extra
information — and with 0.4 cm³ chips at ±3 % it cannot even compare absolute susceptibilities
between chips reliably.
