# Solutions — 23-06-01 Sample Preparation, Coring and Drying Protocols

The lesson is [01 Sample Preparation](../01-sample-preparation.md). All values are
**SYNTHETIC**.

## ★1

The excess length is $0.10\,D$, so the fractional bias is
$\varepsilon = 0.10\,D/L = 0.10/(L/D)$:

| L/D | Bias | At 4.5 km/s |
|---|---|---|
| 2.0 | 5.00 % | 225.0 m/s |
| 3.0 | 3.33 % | 150.0 m/s |

For a 1 % velocity target, $0.10/(L/D) \le 0.01 \Rightarrow L/D \ge 10$, i.e. a
250 mm plug from a 25 mm core — usually impossible. The honest resolution is that the
end effect must be **measured and corrected**, not removed by geometry: cut two lengths
of the same material, difference them to obtain the excess length, and apply the
correction to the main series. That is why a pilot pair is cut before the main series,
and it is the reason a 1 % velocity target is achievable at L/D = 2.5 with a correction
and not at all without one.

## ★2

$$m_{\text{water}} = 118.40 - 110.20 = 8.20\ \mathrm{g},$$

$$\text{of wet mass} = \frac{8.20}{118.40} = 6.93\ \%, \qquad
\text{of dry mass} = \frac{8.20}{110.20} = 7.44\ \% .$$

The distinction is not pedantic: porosity, saturation and gravimetric water content are
all quoted against different bases, and a 6.93/7.44 pair quoted as "about 7 %" has lost
the information needed to reproduce the calculation.

## ★3

$$V_{\text{pore}} = \frac{120.05 - 110.20}{0.998} = 9.8697\ \mathrm{cm^{3}},$$

$$V_{\text{bulk}} = \frac{120.05 - 68.30}{0.998} = 51.8537\ \mathrm{cm^{3}},$$

$$\rho_b = \frac{110.20}{51.8537} = 2.1252\ \mathrm{g/cm^{3}}, \qquad
\phi = \frac{9.8697}{51.8537} = 0.1903 = 19.03\ \% .$$

Cross-check by the grain-density route:

$$\rho_g = \frac{110.20}{51.8537 - 9.8697} = \frac{110.20}{41.9840}
= 2.6248\ \mathrm{g/cm^{3}},$$

$$\phi = 1 - \frac{2.1252}{2.6248} = 0.1905 = 19.05\ \% ,$$

agreeing with the direct route to 0.02 points. The agreement is *not* independent
evidence — the second route uses the same masses — but it does confirm the algebra, and
it shows that $2.62$ g/cm³ is the grain density the immersion route implies. If the
mineralogy implies a different grain density, the discrepancy is a measurement error in
the masses, not a mineralogical surprise.

## ★4

$$S_{\text{air}} = \frac{p_{\text{vac}}}{p_{\text{atm}}} = \frac{2000}{101\,325}
= 0.01974 = 1.97\ \% .$$

On a 20 % porosity that is $0.20 \times 0.01974 = 0.0039$, i.e. **0.39 porosity
points** — larger than the 0.34 points that separated the three routes of the lesson, and
therefore not negligible.

A gravimetric check on a second specimen *would* detect it, and only because it is a
different measurement: if the second specimen is saturated by a method that displaces the
air completely (or if the saturation is verified by comparing the mass gain with the
expected pore volume), the two porosities differ by the residual air fraction. The point
of the exercise is that the error is **systematic**: every vacuum-saturated specimen is
low by the same 0.39 points, so the reproducibility is perfect and the bias is invisible
in the dataset.

## ★5

The mass above the dry asymptote decays as $e^{-t/\tau}$, so the fractional mass change
over a 24 h window beginning at $t$ is

$$\Delta(t) = \frac{m_{\text{water}}}{m_{\text{dry}}}
\left(e^{-t/\tau} - e^{-(t+24)/\tau}\right)
= 0.07441 \times e^{-t/12}\left(1 - e^{-2}\right)
= 0.06434\,e^{-t/12} ,$$

| $t$ (h) | $\Delta$ (% per 24 h) |
|---|---|
| 24 | 0.00871 |
| 48 | 0.00117 |
| 72 | 0.00016 |
| 77.6 | 0.0001 |

Setting $\Delta = 0.0001$ (0.01 %) gives

$$e^{-t/12} = \frac{0.0001}{0.06434} = 1.554\times10^{-3}
\;\Rightarrow\; t = 12\ln(643.4) = 77.6\ \mathrm{h} .$$

So the same criterion that was met at 72 h for a 6 h time constant is met at 77.6 h for a
12 h constant — a small difference here because both are far into the tail, and the
reason the criterion is stated per 24 h rather than as a fixed time. Note also the
practical trap: $\Delta$ at 24 h is 0.0087 %, which is *below* a 0.01 % criterion, so a
protocol that started counting at 24 h would declare this sample dry — wrongly, since the
criterion must be applied to *successive* 24 h windows, not the first one.

## ★6

$$n = \left(\frac{1.96\,s}{h}\right)^{2} = \left(\frac{1.96 \times 1.5}{0.4}\right)^{2}
= (7.35)^{2} = 54.0 \;\Rightarrow\; \textbf{55 specimens} .$$

The cost statement follows immediately: to move from a 0.4-point to a 0.2-point
half-width would take 216 specimens — four times as much rock, cutting time and
measurement time for a two-fold improvement. The number to put in a plan is therefore the
one the *inversion* needs, not the smallest one that is technically attainable.

With only 10 plugs:

$$\mathrm{se} = \frac{1.5}{\sqrt{10}} = 0.4743, \qquad
h = 1.96 \times 0.4743 = 0.93 \text{ porosity points},$$

so the reportable statement is:

> "The mean porosity of the 10 plugs is 22.0 % ± 0.9 % (95 % confidence, $k = 2$,
> $n = 10$, between-specimen standard deviation 1.5 points). The uncertainty is dominated
> by between-specimen variability and is larger than the measurement repeatability,
> which is 0.1 points."

That sentence is honest, quantitatively complete and reproducible. What must **not** be
reported is "22.0 %", or "22.0 % ± 0.1 %" using the repeatability, which is the error the
lesson exists to prevent.
