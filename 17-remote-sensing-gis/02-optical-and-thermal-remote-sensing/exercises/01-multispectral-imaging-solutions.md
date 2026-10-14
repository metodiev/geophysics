# Solutions — 17-02-01 Multispectral Imaging, Band Ratios and Indices

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All spectra are **SYNTHETIC** teaching values.

Lesson: [01 Multispectral Imaging, Band Ratios and Indices](../01-multispectral-imaging.md).

Notation: $I = (\rho_{\rm NIR}-\rho_{\rm red})/(\rho_{\rm NIR}+\rho_{\rm red})$,
$S = \rho_{\rm red}+\rho_{\rm NIR}$.

---

## ★1 — Normalised difference index

$$I = \frac{0.35-0.10}{0.35+0.10} = \frac{0.25}{0.45} = 0.5556.$$

The index is bounded: $I\in[-1,+1]$, with $-1$ for a pure red reflector, $0$ for a
grey (flat) spectrum and $+1$ in the limit $\rho_{\rm red}\to0$.

---

## ★2 — Haze error

With $h = 0.03$ added to both bands:

$$I' = \frac{\rho_{\rm NIR}-\rho_{\rm red}}
{\rho_{\rm red}+\rho_{\rm NIR}+2h}
= \frac{0.25}{0.45+0.06} = \frac{0.25}{0.51} = 0.4902.$$

$$\Delta I = 0.4902 - 0.5556 = -0.0654,
\qquad
\frac{\Delta I}{I} = -11.8\%.$$

Equivalently $I' = I S/(S+2h) = 0.5556\times0.45/0.51$. Note the sign: the haze
compresses the index toward zero, because it adds equal amounts to a numerator
that is a difference and a denominator that is a sum.

---

## ★3 — Simple ratio and its instability

- vegetation-like: $R = 0.48/0.04 = 12.000$.
- water-like: $R = 0.02/0.04 = 0.500$.

$R$ is unstable for **small denominators**: an absolute error $\delta$ in the red
reflectance produces a relative error $\delta/\rho_{\rm red}$, so at
$\rho_{\rm red} = 0.04$ a $\pm0.004$ error (1% of full scale in reflectance units)
is a $\pm10\%$ error in $R$, i.e. $\pm1.2$ in the vegetation case. The water-like
spectrum has $\rho_{\rm red} = 0.04$ too, and equally unstable $R$, but its *index*
is bounded at $-0.333$. **Boundedness, not contrast, is what makes an index
robust for dark targets.**

---

## ★4 — Index change along a soil line

Along $\rho_{\rm NIR} = a\rho_{\rm red} + b$, with $x = \rho_{\rm red}$,

$$I(x) = \frac{(a-1)x+b}{(a+1)x+b},
\qquad
\frac{\mathrm{d}I}{\mathrm{d}x}
= \frac{(a-1)\left[(a+1)x+b\right] - (a+1)\left[(a-1)x+b\right]}
{\left[(a+1)x+b\right]^{2}} = -\frac{2b}{\left[(a+1)x+b\right]^{2}}.$$

For $a = 1.2$, $b = 0.08$, $x = 0.25$: $(a+1)x+b = 2.2\times0.25+0.08 = 0.63$,
$0.63^{2} = 0.3969$, so

$$\frac{\mathrm{d}I}{\mathrm{d}x} = -\frac{0.16}{0.3969} = -0.4031.$$

Over $\Delta x = 0.02$ (a modest brightness change), $\Delta I \approx -0.0081$.

**Where the confound comes from.** The derivative is proportional to $b$, the
*intercept* of the soil line: a line through the origin ($b=0$) projects to a
constant ratio, and any offset from the origin makes the projection vary. The
slope $a$ enters only through the denominator. To confirm the magnitudes, the
lesson's synthetic line ($a = 1.15$, $b = 0.06$) gives

$$\frac{\mathrm{d}I}{\mathrm{d}x}\bigg|_{x=0.12} = -1.1867,
\qquad
\frac{\mathrm{d}I}{\mathrm{d}x}\bigg|_{x=0.25} = -0.3361,
\qquad
\frac{\mathrm{d}I}{\mathrm{d}x}\bigg|_{x=0.28} = -0.2738,$$

so the confound is worst for **dark** soils, exactly as the haze and noise
arguments predict.

---

## ★5 — Propagating band noise

$$\frac{\partial I}{\partial \rho_{\rm red}} = -\frac{2\rho_{\rm NIR}}{S^{2}},
\qquad
\frac{\partial I}{\partial \rho_{\rm NIR}} = +\frac{2\rho_{\rm red}}{S^{2}},
\qquad
\sigma_I = \sigma\sqrt{\left(\partial_{\rho_{\rm red}}I\right)^{2}
+ \left(\partial_{\rho_{\rm NIR}}I\right)^{2}}.$$

**Soil-like** $(0.42, 0.45)$, $S = 0.87$, $S^{2} = 0.7569$:

$$\partial_{\rho_{\rm red}}I = -0.90/0.7569 = -1.1891,\qquad
\partial_{\rho_{\rm NIR}}I = 0.84/0.7569 = +1.1098,$$
$$\sigma_I = 0.015\sqrt{1.4140+1.2317} = 0.015\times1.6266 = 0.02440.$$

**Vegetation-like** $(0.04, 0.48)$, $S = 0.52$, $S^{2} = 0.2704$:

$$\partial_{\rho_{\rm red}}I = -3.5503,\qquad
\partial_{\rho_{\rm NIR}}I = +0.2959,$$
$$\sigma_I = 0.015\times3.5626 = 0.05344.$$

The vegetation-like spectrum gives a $2.19\times$ larger index uncertainty even
though its (absolute) contrast is similar. **Why contrast alone does not decide:**
$\sigma_I$ depends on the two partial derivatives *separately*, not on their
difference. A balanced pair of reflectances ($0.42$, $0.45$) puts both
derivatives near unity; an unbalanced pair ($0.04$, $0.48$) makes the derivative
with respect to the dark band large, and that one term dominates the quadrature.
The index's noise is set by the *darkest* band it uses.

---

## ★6 — Perpendicular vegetation index

$$\mathrm{PVI} = \frac{\rho_{\rm NIR} - a\rho_{\rm red} - b}{\sqrt{1+a^{2}}}
= \frac{0.40 - 1.15\times0.15 - 0.06}{\sqrt{1+1.3225}}
= \frac{0.40-0.1725-0.06}{1.5240} = \frac{0.1675}{1.5240} = 0.1099.$$

A soil pixel on the line has $\mathrm{PVI} = 0.0000$ by construction, and the
synthetic vegetation-like endmember has $\mathrm{PVI} = +0.2454$. The pixel's
$+0.1099$ is $45\%$ of the way from bare soil to dense vegetation-like cover in
this geometry — evidence of vegetation, not of soil brightness. Its
$I = (0.40-0.15)/(0.55) = 0.4545$ would *also* be consistent with a bright bare
soil: along the soil line with $a = 1.15$, $b = 0.06$, $x$ would have to be
$0.319$ (solving $\rho_{\rm NIR} = 1.15x+0.06 = 0.40$ gives $x = 0.2957$, whose
index is $(0.40-0.2957)/0.6957 = 0.1500$). The two indices disagree about the
interpretation, and PVI is the one designed for the question asked.

---

## ★7 — Inverting the alteration ratio

$$R = 1 + \frac{0.8A}{A+1.5}
\;\Longrightarrow\;
(R-1)(A+1.5) = 0.8A
\;\Longrightarrow\;
A = \frac{1.5(R-1)}{0.8-(R-1)}.$$

For $R = 1.40$: $R-1 = 0.40$, so $A = 1.5\times0.40/(0.80-0.40) = 0.60/0.40 = 1.50$.
Check: $R(1.5) = 1 + 0.8\times1.5/3.0 = 1.4000$. ✔

Sensitivity: $\mathrm{d}R/\mathrm{d}A = 1.2/(A+1.5)^{2}$, so

$$\frac{\mathrm{d}A}{\mathrm{d}R} = \frac{(A+1.5)^{2}}{1.2}
= \frac{3.0^{2}}{1.2} = 7.50\ \text{per unit }R.$$

An index error $\pm0.01$ therefore yields $\delta A = 7.5\times0.01 = \pm0.075$,
i.e. a $5\%$ abundance error at $A = 1.5$. At $A = 4$ the same calculation gives
$(5.5)^{2}/1.2 = 25.2$ per unit $R$, so the same index error becomes
$\delta A = \pm0.25$ — a $6\%$ error on a larger value, and the *relative* error
grows as $A$ does because the sensitivity is decaying.

---

## ★8 — Why an LAI claim fails over a dense canopy

**The argument.** With $I(P) = I_\infty - (I_\infty-I_0)e^{-kP}$,
$I_\infty = 0.90$, $I_0 = 0.10$, $k = 0.70$:

$$\frac{\mathrm{d}I}{\mathrm{d}P} = k(I_\infty-I_0)e^{-kP} = 0.56\,e^{-0.70P},$$

so the property uncertainty for index uncertainty $\sigma_I$ is

$$\sigma_P = \frac{\sigma_I}{0.56}e^{+0.70P}.$$

The demonstration's table quantifies it: at $\mathrm{LAI} = 4$ a
$\sigma_I = 0.02$ spans LAI $3.51$–$4.76$, a width of $1.25$ — a $\pm16\%$
retrieval. At $\mathrm{LAI} = 6$, $I + 0.02 = 0.9080$ exceeds the asymptote
$I_\infty = 0.90$, so **no LAI value is consistent with the upper bound**: the
interval is unbounded. A dense-canopy LAI claim from this index at this precision
is therefore unsupportable *for any confidence interval that includes the upper
tail*, and the claim "LAI $= 7$" is consistent with any LAI $\ge 6$.

**The two measurements that restore the claim.**

1. **An index with a slower saturation.** Red-edge indices saturate later because
   the red-edge reflectance continues to respond at higher biomass; this is a
   *choice of wavelengths*, not a statistical fix. Alternatively use a
   near-infrared and a shortwave-infrared band whose ratio responds to canopy
   water content, which keeps changing after the green-leaf signal has saturated.
2. **An independent measurement of a different physical quantity** — a
   microwave or lidar canopy-height/structure measurement, or a radiative-transfer
   inversion with several bands constrained simultaneously — which breaks the
   degeneracy rather than shrinking the noise. Averaging more pixels does **not**
   help once $\sigma_I$ has shrunk below the gap to the asymptote; the problem is
   then model bias, not random error.

---

## ★9 — Designing an index for mixed bright and dark soils

**Requirement.** Map a notional surface property $P$ in a scene containing bright
and dark bare soils, with (i) an error contribution from soil brightness below
$0.02$ in index units, and (ii) an index noise amplification below $3\times$ the
per-band noise.

**Band regions (notional, no real sensor).** Three reflectances: a visible red
band $\rho_{\rm R}$, a near-infrared band $\rho_{\rm N}$, and a shortwave-infrared
band $\rho_{\rm S}$ in which bare soils are bright and the target is dark.

**Algebra — the soil-adjusted form.** Because the confound is a line with a
non-zero intercept, use the adjusted index

$$I_{\rm adj} = (1+L)\,\frac{\rho_{\rm N}-\rho_{\rm R}}
{\rho_{\rm N}+\rho_{\rm R}+L}.$$

Along a soil line $\rho_{\rm N} = a\rho_{\rm R} + b$, differentiating with respect
to $x = \rho_{\rm R}$ gives

$$\frac{\mathrm{d}I_{\rm adj}}{\mathrm{d}x}
= \frac{(1+L)\left[(a-1)L - 2b\right]}
{\left[(a+1)x + b + L\right]^{2}},$$

which vanishes identically for

$$L = \frac{2b}{a-1}.$$

For the lesson's synthetic soil line ($a = 1.15$, $b = 0.06$) this gives
$L = 0.8000$, and the adjusted index is $0.1256$ at every point on the line
against a plain-index spread of $0.2453\to0.1541$.

**Expected soil-brightness error.** With $L$ tuned, the *first-order* residual is
zero by construction; the residual that remains is second-order in the departure
of the real soil line from the fitted one. For a pair of soils whose true
intercepts differ by $\pm0.01$ from the fitted $b$, the residual index change is
$\approx (1+L)\times2\times0.01/((a+1)x+b+L)^{2}$ evaluated at the scene's
brightness, which for the lesson's geometry is
$1.8\times0.02/(1.29)^{2} = 0.0216$ — right at the $0.02$ requirement, which is
the honest conclusion: **the adjustment removes the confound only as well as the
soil line is known**, and the soil line must therefore be fitted from the scene
itself, not taken from a textbook.

**Noise amplification accepted.** The adjusted index keeps the
normalised-difference structure, so the sensitivities are of the same order as
★5: amplification $\approx 1.6\times$ for a balanced band pair and
$\approx 3.6\times$ for an unbalanced one. To stay under $3\times$, choose the NIR
band so that the two reflectances of the target are within a factor of about $3$
of each other, or average pixels. Report the *measured* amplification from a Monte
Carlo on the scene's own band statistics rather than the analytic estimate,
because the amplification varies across the scene.

**Executability.** Every step above is computable from scene statistics and the
soil-line fit; nothing requires data outside the scene. The specification is
therefore falsifiable: if the measured soil-brightness residual exceeds $0.02$,
the index is rejected, not merely "improved".

**Noise amplification accepted.** The adjusted index keeps the normalised-difference
structure, so the sensitivities are of the same order as ★5: amplification
$\approx 1.6\times$ for a balanced band pair and $\approx 3.6\times$ for an
unbalanced one. To stay under $3\times$, choose the NIR band so that the two
reflectances of the target are within a factor of about $3$ of each other, or
average pixels. Report the *measured* amplification from a Monte Carlo on the
scene's own band statistics rather than the analytic estimate, because the
amplification varies across the scene.

**Executability.** Every step above is computable from scene statistics and the
soil-line fit; nothing requires data outside the scene. The specification is
therefore falsifiable: if the measured soil-brightness error exceeds $0.02$, the
index is rejected, not merely "improved".
