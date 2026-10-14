# Solutions — Palaeo Sea Level Reconstruction from Marine Records

Worked arithmetic for
[`01-paleo-sea-level-exercises.md`](01-paleo-sea-level-exercises.md). **All models
and data are SYNTHETIC.**

## ★ Foundational

**1.1** $\delta^{18}\mathrm{O}_{\text{sw}}=0.010\times60=0.600$‰. Temperature term
$=0.22\times(15-11)=0.880$‰. Carbonate value
$=0.600+0.880=1.480$‰. The temperature contribution is
$0.880/0.600=1.47$, i.e. **147% of the ice-volume term** — at a 4 K cooling the
temperature term already dominates.

**1.2** With $T=10\ ^\circ\mathrm{C}$:
$SL=-(2.20-0.22\times5)/0.010=-110.0$ m. With $T=13\ ^\circ\mathrm{C}$:
$SL=-(2.20-0.22\times2)/0.010=-176.0$ m. The difference is 66 m over 3 K, i.e.
**22 m K⁻¹**, which equals $0.22/0.010$ exactly as expected.

**1.3 (a)** $SL=2.478\times10^{-15}\times8\times10^{15}=\mathbf{19.8\ m}$ (from
$SL=\rho_iV/(\rho_{\text{sw}}A)$ with $\rho_{\text{sw}}=1025$).
**(b)** $1\ \mathrm{mm}=361$ Gt, so $1.5\ \mathrm{mm/yr}=1.5\times361=\mathbf{542\ Gt/yr}$.

## ★★ Applied

**2.1** Rate $=45\ \mathrm{m}/8\ \mathrm{ka}=5.625$ mm/yr. Age uncertainty
$\sigma_{\Delta t}=\sqrt2\times0.8=1.131$ ka, so
$\sigma_{\text{rate}}=5.625\times1.131/8=0.795$ mm/yr, a relative error of
$0.795/5.625=14.1\%$. The depth error of a few centimetres is ~4 orders of magnitude
smaller in relative terms, so the **chronology dominates**.

**2.2** (a) $SL=-22+9=-13$ m relative to present.
(b) $\sigma=\sqrt{1.5^2+2^2+(\text{age term})^2}$. The age term alone converts
$0.6$ ka into a rate error, not a level error, so for a level comparison
$\sigma=\sqrt{1.5^2+2^2}=2.5$ m, and the datum term is the largest contributor.
(c) A 5 m difference is $2\sigma$ of a single terrace reconstruction, so it is
**not** a meaningful discrepancy on its own; several terraces with independent GIA
corrections would be needed.

**2.3** The two disagree at
$\sigma_{\text{diff}}=\sqrt{5^2+8^2}=9.4$ m, and the difference is 22 m, i.e.
$2.3\sigma$: marginally significant. In this framework the most likely explanations
are (i) a different temperature assumption, worth 22 m per kelvin, and (ii) a
different GIA correction, worth up to tens of metres; the isotope estimate also
carries the ice-volume coefficient's own calibration error.

## ★★★ Research-oriented

**3.1** (a) $1.5\times22=33$ m, and adding the $\pm1\ ^\circ\mathrm{C}$ calibration
error in quadrature gives $\sqrt{1.5^2+1^2}\times22=39.6$ m.
(b) $\pm5/22=\pm0.23$ K — better than the calibration accuracy of any current
proxy. (c) No stated proxy achieves 0.2 K absolute accuracy, so a sea level derived
from isotopes alone cannot resolve 5 m: published curves that quote metre-level
resolution must be relying on independent constraints (GIA-invariant sites,
corals/terraces, speleothems) rather than on the isotope value alone.

**3.2** (a) $0.10\times60=6$ m — comparable to the change being studied.
(b) If the ice history is tuned to fit the same sea-level records that the GIA model
is then used to correct, the correction absorbs the signal.
Break it by using data the ice history was not tuned to (far-field records, or
independent ice-margin chronologies), or by jointly inverting the Earth structure
with data that are insensitive to sea level.

**3.3** The isotope route alone gives a 1 K temperature error of 22 m and a GIA error
of 6 m: $\sqrt{22^2+6^2}=22.8$ m, far worse than the 10 m target.
Required: (i) an independent temperature proxy accurate to better than 0.3 K,
(ii) a GIA model validated at a far-field, tectonically stable site, and (iii) at
least one non-isotopic sea-level marker (a dated terrace, or a radiometrically dated
speleothem with a known growth position) to anchor the level. Only the combination
can reach 10 m.
