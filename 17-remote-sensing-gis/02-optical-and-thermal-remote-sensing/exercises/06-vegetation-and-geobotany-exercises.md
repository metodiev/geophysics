# Exercises — 17-02-06 Vegetation Indices, Geobotany and Mineral Alteration Mapping

Attempt these before reading the
[solutions](./06-vegetation-and-geobotany-solutions.md). The lesson is
[06 Vegetation Indices, Geobotany and Mineral Alteration Mapping](../06-vegetation-and-geobotany.md).
All relations and spectra are **SYNTHETIC** teaching values.

Reference values from the lesson: $I(P) = 0.90 - 0.80\,e^{-0.70P}$;
soil line $a = 1.15$, $b = 0.06$; features at $2.20\ \mathrm{\mu m}$ (clay-like)
and $2.33\ \mathrm{\mu m}$ (carbonate-like); depth ratio at reference
$D(2.20)/D(2.33) = 6.3361$.

## ★ Foundational

**★1.** Compute the index $I$ for $\mathrm{LAI} = 3$ from the synthetic relation,
and the sensitivity $\mathrm{d}I/\mathrm{d}\mathrm{LAI}$ at that point.

**★2.** A feature has $\rho(2.20) = 0.24$ and a continuum value
$C(2.20) = 0.30$. Compute the continuum-removed value and the band depth.

**★3.** State the soil-adjustment tuning condition $L = 2b/(a-1)$ and compute it
for a soil line with $a = 1.25$, $b = 0.05$.

## ★★ Applied

**★★4.** Compute the LAI retrieval uncertainty at $\mathrm{LAI} = 3$ for an index
uncertainty $\sigma_I = 0.015$, and state the relative uncertainty.

**★★5.** Compute the continuum value at $2.20\ \mathrm{\mu m}$ for the endpoint
pair $(2.05, 0.27)$ and $(2.45, 0.63)$, then the depth for
$\rho(2.20) = 0.24$. Compare with the depth obtained from the pair
$(2.00, 0.20)$ and $(2.50, 0.70)$, whose continuum at $2.20\ \mathrm{\mu m}$ is
$0.35$.

**★★6.** Show algebraically that a common brightness factor $b$ leaves
$D_1/D_2$ invariant. Then compute the residual change if the two continuum values
scale by $1/b$ and $1.1/b$ respectively instead, and state what surface property
would produce such a difference.

**★★7.** Two alteration estimators are compared at equal false-alarm rate: the
single band depth detects $0.3801$ of the patch at FAR $0.01$; the depth ratio
detects $0.7826$. Compute the ratio of detections and state, in two sentences, why
an uncorrected comparison at a fixed threshold would have been misleading.

## ★★★ Research-oriented

**★★★8.** Design an alteration-mapping product that reports a single-depth layer,
a depth-ratio layer and a slope-indicator layer. State what each layer is for, the
order in which an interpreter should use them, and the decision rule that rejects a
depth-ratio anomaly when the denominator feature is absent. A specification that
could not be executed is a failed answer.

**★★★9.** A geobotanical study reports a vegetation-stress anomaly over a
$20\ \mathrm{km^{2}}$ area and claims it indicates a buried mineralised body. Using
the lesson's synthetic stress model, state the quantitative false-alarm budget the
claim requires, list the three most plausible non-mineral causes of the same
signal, and specify the evidence that would distinguish them. Conclude with the
strongest statement the available data could support.
