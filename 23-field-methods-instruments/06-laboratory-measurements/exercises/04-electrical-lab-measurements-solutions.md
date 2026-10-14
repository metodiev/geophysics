# Solutions — 23-06-04 Laboratory Resistivity, IP and Dielectric Measurements

The lesson is [04 Electrical Laboratory Measurements](../04-electrical-lab-measurements.md).
All values are **SYNTHETIC**.

## ★1

$$R = \frac{\rho L}{A} = \frac{5 \times 0.050}{1.0\times10^{-3}} = 250\ \Omega,$$

$$\rho_{\text{app}} = \rho\left(1 + \frac{2R_c}{R}\right)
= 5\left(1 + \frac{400}{250}\right) = 5 \times 2.6 = 13.0\ \Omega\cdot\mathrm{m},$$

a **+160 %** error. This is the lesson's warning at its most extreme: the more conductive
the specimen, the smaller $R$ and the larger the contact error, so a two-electrode holder
is useless for a clay-rich or brine-saturated specimen — precisely the specimens whose
resistivity is most interesting for the clay and saturation questions.

## ★2

$$K = \frac{A}{L} = \frac{1.0\times10^{-3}}{0.050} = 0.0200\ \mathrm{m} = 20.0\ \mathrm{mm},$$

and since $\rho \propto L$, a 1 % error needs
$\delta L = 0.01 \times 50.0 = \mathbf{0.5}$ **mm**. That is a real tolerance: it is about
the width of a caliper's smallest division and easily exceeded by hand-placed electrodes, by
a specimen whose end is not square, or by a spacing recorded from a drawing. For the
lesson's 80 mm holder the equivalent tolerance was 0.8 mm.

## ★3

$$f_{\text{peak}} = \frac{1}{2\pi\tau} = \frac{1}{2\pi \times 0.5} = 0.3183\ \mathrm{Hz} .$$

With $c = 0.8$ (closer to a single relaxation than the lesson's 0.5) the imaginary part's
peak stays at $1/(2\pi\tau)$ to a very good approximation — the broadening exponent changes
the *width* of the spectrum, and shifts the peak only slightly. The frequency still has to
be inside the anomalous band to see anything.

The **phase** is the observable to report for three reasons: it is dimensionless, so it does
not require the geometric factor or an absolute calibration; it is unaffected by a
*resistive* contact in series with the specimen, which changes the magnitude but barely the
phase; and it is the quantity a field IP survey measures, so a laboratory phase is directly
comparable with field data. The magnitude at the anomalous frequency is 3 %–30 % below the
DC value in the lesson's example, which is a small number to defend with a 2 % measurement
uncertainty.

## ★4

$$f_{\varepsilon''} = \frac{1}{2\pi\tau} = \frac{1}{2\pi \times 2.0\times10^{-6}}
= 79.577\ \mathrm{kHz},$$

$$f_{\tan\delta} = \frac{1}{2\pi\tau}\sqrt{\frac{\varepsilon_s}{\varepsilon_\infty}}
= 79.577 \times \sqrt{\frac{30}{6}} = 79.577 \times 2.2361
= 177.94\ \mathrm{kHz},$$

$$\tan\delta_{\max} = \frac{\varepsilon_s - \varepsilon_\infty}
{2\sqrt{\varepsilon_s\varepsilon_\infty}} = \frac{24}{2\sqrt{180}}
= \frac{24}{26.833} = 0.8944 .$$

So the two peaks are separated by a factor of 2.24 — more than an octave — and a survey
that measures only at 100 kHz would report neither peak: it would sit between them and
conclude, wrongly, that the response is featureless. **The frequency grid must bracket the
expected relaxation time on both sides**, which for a 2 µs relaxation means a decade either
side, i.e. roughly 10 kHz to 1 MHz.

## ★5

$$\frac{\delta\rho}{\rho} = \sqrt{0.4^2+0.4^2+0.1^2+0.2^2+1.5^2+3.0^2}\ \%
= \sqrt{0.16+0.16+0.01+0.04+2.25+9.00}\ \% = \sqrt{11.62}\ \% = 3.409\ \% .$$

| Term | Relative | Variance share |
|---|---|---|
| voltage | 0.4 % | 1.38 % |
| current | 0.4 % | 1.38 % |
| length | 0.1 % | 0.09 % |
| area | 0.2 % | 0.34 % |
| temperature | 1.5 % | 19.36 % |
| **pore-fluid conductivity** | **3.0 %** | **77.45 %** |
| **combined** | **3.409 %** | 100 % |

The **fluid conductivity dominates at 77.45 %**. Improving the voltmeter from 0.4 % to
0.1 % would reduce the total from 3.409 % to $\sqrt{11.58} = 3.403$ % — a change of 0.006
percentage points, i.e. nothing. Improving the fluid conductivity from 3.0 % to 1.0 %
(by measuring the salinity and the temperature properly) reduces the total to
$\sqrt{11.62 - 9.00 + 1.00} = \sqrt{3.62} = 1.903$ %, a factor of 1.8. This is the
arithmetic that should decide where the programme's money and attention go.

## ★6

A model answer.

**Electrode configuration.** A **four-electrode holder with fixed sense electrodes**, with
the sense pair well inside the current path (or with a guard ring) so that the current
distribution is close to uniform; non-polarizing (reversible) electrode pairs, since steel
electrodes polarize and the polarization grows exactly where the IP signal lives. The
configuration is chosen because the two-electrode alternative would add tens of percent of
contact impedance to a saturated sandstone whose resistance is a few hundred to a few
thousand ohm.

**Frequency range.** Select it from the expected $\tau$: for a sandstone with clay, the IP
relaxation is commonly in the 0.1–100 Hz band; for a sulfide-bearing rock it can be higher.
Measure at least **six to eight frequencies per decade**, spanning at least three decades
around the expected peak, because the phase peak must be *bracketed* to be observed and
because $m$, $\tau$ and $c$ are correlated when the band is narrow. Report the phase and PFE
at the measured frequencies as the primary result; report the fitted parameters as secondary.

**Calibration and reference checks.** A reference specimen (a well-characterised resistor
plus capacitor network, not necessarily a rock) measured at the start, the middle and the
end of every session, at every frequency; the holder's own impedance measured empty
(open-circuit and short-circuit) so the stray capacitance can be removed; the electrode
polarization checked by reversing the current direction and repeating one measurement
(reversal must not change the result by more than the target uncertainty); and the fluid
conductivity and temperature logged with every specimen.

**Uncertainty budget.** Resistivity: fluid 3.0 % (unless the salinity is known to 0.5 %),
temperature 1.5 % (unless held to 0.5 °C), voltage 0.4 %, current 0.4 %, geometry 0.22 %,
giving $\sqrt{9.00+2.25+0.16+0.16+0.05} = 3.41$ % — **the 2 % (95 %) target is not met**.
With 0.5 % fluid and 0.3 % temperature the total is
$\sqrt{0.25+0.09+0.16+0.16+0.05} = 0.84$ %, and the 95 % half-width is 1.7 % — just inside
the target. So the *targets are met only if the fluid and temperature terms are brought
under control*, which is the honest message of the budget.

Phase: a 0.5 mrad target on a phase that peaks at 70 mrad is a relative uncertainty of
0.7 %, achieved if the voltage and current amplitude and phase uncertainties are ~0.5 %
each and the polarization check passes — but not achievable at the low-frequency end of the
band, where electrode polarization and drift dominate, so the phase should be reported with
a frequency-dependent uncertainty rather than one number.

**What the field comparison cannot support.** The laboratory measures a plug at room
temperature, full water saturation, a known salinity and a controlled stress; the field
measures a formation at a different saturation, a different salinity history and an
in-situ stress. So the laboratory values *bound* and *interpret* the field values but do not
predict them: the statement to make is "the field resistivity range is consistent with the
laboratory values at the recorded saturations", not "the field value equals the laboratory
value". The difference — surface conduction, anisotropy, and the saturation distribution —
is not measured by either alone.
