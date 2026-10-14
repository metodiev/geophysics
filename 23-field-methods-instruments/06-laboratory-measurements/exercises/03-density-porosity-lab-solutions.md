# Solutions — 23-06-03 Laboratory Density, Porosity and Permeability Measurement

The lesson is [03 Density, Porosity and Permeability](../03-density-porosity-lab.md). All
values are **SYNTHETIC**.

## ★1

$$V_{\text{film}} = \frac{145.65 - 145.20}{0.900} = 0.5000\ \mathrm{cm^{3}},$$

$$V_{\text{coated}} = \frac{145.65 - 83.10}{0.998} = 62.6754\ \mathrm{cm^{3}},$$

$$V_{\text{bulk}} = 62.6754 - 0.5000 = 62.1754\ \mathrm{cm^{3}},$$

$$\rho_b = \frac{145.20}{62.1754} = 2.3353\ \mathrm{g/cm^{3}}, \qquad
\rho_{b,\text{no film}} = \frac{145.20}{62.6754} = 2.3167\ \mathrm{g/cm^{3}} ,$$

a −0.80 % error if the film is ignored. The error is larger than in the lesson (0.45 %)
because this specimen is smaller while the film volume is the same 0.50 cm³, so the film
is 0.80 % of the volume. **The film error scales as the surface-to-volume ratio**, which is
the practical rule: the smaller the specimen, the more the coating matters, and below about
20 cm³ the coating route must be corrected or abandoned.

## ★2

$$V_{\text{solid}} = V_c - V_e\left(\frac{p_1}{p_2} - 1\right)
= 80.00 - 40.00\left(\frac{120.0}{75.0} - 1\right) = 80.00 - 40.00(0.6000)
= 56.000\ \mathrm{cm^{3}},$$

$$\frac{\mathrm{d}V}{\mathrm{d}p_2} = \frac{V_e p_1}{p_2^{2}}
= \frac{40.00 \times 120.0}{75.0^{2}} = \frac{4800}{5625} = 0.8533\ \mathrm{cm^{3}/kPa} .$$

So a 0.5 kPa transducer error is $0.5 \times 0.8533 = 0.4267$ cm³, i.e. **0.762 %** of the
56 cm³ solid volume — about the same resolution as the lesson's example, obtained with a
smaller cell and a smaller pressure drop. If the target were 0.3 %, the transducer would
have to be three times better, or the expansion ratio larger.

## ★3

$$\rho_g = \frac{137.8}{52.0} = 2.6500\ \mathrm{g/cm^{3}}, \qquad
\rho_b = \frac{137.8}{65.0} = 2.1200\ \mathrm{g/cm^{3}},$$

$$\phi = 1 - \frac{52.0}{65.0} = 0.2000 = 20.00\ \%, \qquad
1 - \frac{2.1200}{2.6500} = 0.2000 = 20.00\ \% ,$$

$$m_{\text{water}} = 0.2000 \times 65.0 \times 0.998 = 12.974\ \mathrm{g} .$$

The two porosity forms agree exactly, as they must — they are one statement. The 12.97 g
of water is the number to check a saturation experiment against: a saturated mass more than
about 0.2 g away from $137.8 + 12.97 = 150.77$ g means a protocol failure, and the *sign*
tells you which one (too little water → residual air or an incomplete saturation; too much
→ surface film still adhering to the specimen when it was weighed).

## ★4

With $K_{\text{gas}} = K_L + K_L b\,(1/\bar p)$:

| $\bar p$ (MPa) | $K$ (mD) | $1/\bar p$ (1/MPa) |
|---|---|---|
| 0.4 | 3.2 | 2.50 |
| 1.6 | 1.6 | 0.625 |

$$K_L b = \frac{3.2 - 1.6}{2.50 - 0.625} = \frac{1.6}{1.875} = 0.8533 ,$$

$$K_L = 3.2 - 0.8533(2.50) = 3.2 - 2.1333 = 1.0667\ \mathrm{mD}, \qquad
b = \frac{0.8533}{1.0667} = 0.8000\ \mathrm{MPa} .$$

So the liquid-equivalent permeability is **1.07 mD** and the low-pressure measurement
overstates it by a factor of 3.0.

Two points are **not** enough for this extrapolation: the fit has no degrees of freedom,
so the linearity cannot be tested, and the whole result depends on the accuracy of the two
pressures. A slip in either measurement produces a plausible intercept from a wrong slope,
and there is no way to detect it from the data. The lesson's rule — four or more mean
pressures spanning a decade, with the linearity checked — is the minimum defensible
practice; with two points, the honest report is "1.07 mD assuming the Klinkenberg relation
holds, from two measurements at 0.4 and 1.6 MPa", which is a much weaker claim.

## ★5

$$K = \frac{Q\mu L}{A\Delta p}
= \frac{(1.20\times10^{-9})(1.0\times10^{-3})(0.060)}
{(9.50\times10^{-4})(3.5\times10^{5})} ,$$

numerator $= 1.20\times10^{-9} \times 1.0\times10^{-3} \times 0.060 = 7.20\times10^{-14}$,
denominator $= 9.50\times10^{-4} \times 3.5\times10^{5} = 3.325\times10^{2}$, so

$$K = 2.1654\times10^{-16}\ \mathrm{m^{2}} = 0.2195\ \mathrm{mD} .$$

Note the conversion carefully: $1\ \mathrm{mD} = 9.869233\times10^{-16}$ m², so
$K = 2.1654\times10^{-16}/9.869233\times10^{-16} = 0.2195$ mD.

Uncertainty, in quadrature:

$$\frac{\delta K}{K} = \sqrt{0.5^{2} + 0.1^{2} + 0.2^{2} + 3.0^{2} + 0.5^{2}}\ \%
= \sqrt{0.25+0.01+0.04+9.00+0.25}\ \% = 3.090\ \% .$$

The **differential pressure dominates**: its variance share is $9.00/9.55 = 94.2$ % of the
total. The combined 3.090 % corresponds to a 95 % half-width of $2 \times 3.090 = 6.2$ %
($k = 2$), so this test does **not** meet the lesson's ±5 % target — the pressure
measurement would have to improve to about 2 % to get there. That is the kind of conclusion
a budget exists to produce before the programme is funded rather than after.

## ★6

A model answer.

**Bulk volume.** Use the **helium pycnometry grain volume plus an independent bulk volume
from caliper** on right cylinders: the bulk volume is where the geometry error lives, and
the caliper route makes that error visible (parallelism, diameter, length) rather than
hiding it. For friable plugs, add the coated-immersion route as a cross-check and *report
both*, using the difference as a contribution to the porosity uncertainty.

**Pycnometer operating point.** Choose the expansion ratio so that the pressure drop is
large but $p_2$ is well above the transducer's noise, e.g. $V_c = 100$, $V_e = 50$ cm³,
$p_1 = 100$ kPa, $p_2 \approx 60$ kPa, where
$\mathrm{d}V/\mathrm{d}p_2 = 1.3889$ cm³/kPa. For a ±0.3 porosity point target on a 65 cm³
specimen, the pore volume is about 13 cm³, so 0.3 points is 0.195 cm³ of pore volume — and
0.195/1.3889 = **0.14 kPa** required transducer resolution, which is demanding and must be
verified with a calibrated reference. This is the calculation that decides the instrument.

**Klinkenberg plan.** Six mean pressures spanning at least a decade — for a tight gas, for
example 0.2, 0.4, 0.8, 1.5, 3.0 and 6.0 MPa — with the linearity of $K$ against $1/\bar p$
checked ($R^2$ is not enough: inspect the residual pattern for curvature) and the
intercept's standard error reported. Two pressures are never enough.

**Steady-state or transient.** For a tight rock the steady-state rate at 0.2 mD,
$\Delta p = 0.35$ MPa is
$Q = K A \Delta p/(\mu L) = (2.165\times10^{-16})(9.50\times10^{-4})(3.5\times10^{5})
/ (10^{-3} \times 0.060) = 1.20\times10^{-9}$ m³/s $= 1.2$ mm³/s, which is measurable but
slow to reach equilibrium, and the long service time means fines migration and clay
swelling have time to change the specimen. The better choice for a tight gas is a
**transient (pulse-decay) measurement** at several pore pressures, which also gives the
Klinkenberg dataset in the same runs, with a steady-state measurement on two plugs as a
cross-check.

**Uncertainty budget.** Porosity: pycnometry 0.76 %, geometry 0.15 %, specimen variability
(the dominant term) about 1.5 points — with $n = 12$ from 12 plugs the standard error is
$1.5/\sqrt{12} = 0.43$ points, so a ±0.3 point 95 % target is **not** met by 12 plugs from
a formation with 1.5 points of variability; it needs 96 plugs, or the target must be
relaxed, or the specimens must be pooled within a single lithofacies to reduce the
variability. Best to say that plainly in the plan. Permeability: with the transient method
the flow-rate term drops out and the budget is dominated by the pressure transducer and the
gas-property terms, so ±5 % is achievable with a 1 % pressure measurement and a temperature
controlled to 0.5 °C (viscosity and gas compressibility both depend on it).

**Standard checks.** Two known-volume pycnometer standards before and after every batch;
a reference plug measured monthly; caliper measurements repeated in two orientations;
the non-Darcy check ($K$ versus $Q$) at the highest rate; the saturation mass check
(the 12.97 g style calculation of ★3); and the temperature logged with every measurement.

**What cannot be defended.** The **in-situ** permeability and the connected porosity: the
laboratory measures an intact plug at a controlled stress and a clean fluid, whereas the
formation has a different stress state, a different clay and fines content and possibly a
different fluid — and neither the pore-scale connection nor the stress sensitivity is
revealed by a room-temperature, unconfined measurement. That statement belongs in the
report, together with the *direction* of the expected correction where it is known.
