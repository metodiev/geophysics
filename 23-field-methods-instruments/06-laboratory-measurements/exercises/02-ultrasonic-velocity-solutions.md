# Solutions — 23-06-02 Ultrasonic Velocity Measurement and Pressure Dependence

The lesson is [02 Ultrasonic Velocity](../02-ultrasonic-velocity.md). All values are
**SYNTHETIC**.

## ★1

$$\text{naive } v = \frac{0.0300}{9.20\times10^{-6}} = 3261\ \mathrm{m/s},$$

$$v = \frac{L_2 - L_1}{t_2 - t_1} = \frac{0.0200}{4.20\times10^{-6}}
= 4761.9\ \mathrm{m/s},$$

$$t_0 = \frac{t_1L_2 - t_2L_1}{L_2 - L_1}
= \frac{(9.20)(50.0) - (13.40)(30.0)}{20.0} = \frac{460.0 - 402.0}{20.0}
= 2.90\ \mathrm{\mu s} .$$

The naive velocity is 31.5 % low — the same failure as in the lesson, and it is worth
noticing *how* it fails: the naive value is closer to the true one for the longer
specimen (3789 m/s versus 3512 m/s in the lesson's pair), so a series of specimens of
different lengths would show an apparent velocity that increases with length. That pattern
is a delay signature, not heterogeneity, and it is the reason the two-length check is
performed before a series rather than after it.

## ★2

$$f_{\min} = \frac{5v}{L} = \frac{5 \times 3800}{0.025} = 760\,000\ \mathrm{Hz}
= 0.760\ \mathrm{MHz},$$

$$\lambda = \frac{v}{f} = \frac{3800}{760\,000} = 5.0\ \mathrm{mm} = \frac{L}{5} .$$

The criterion is satisfied *exactly* at $0.760$ MHz and more comfortably above it, so the
frequency choice is driven upward by this rule and downward by attenuation and beam
spread. A 25 mm plug is short, so the usable window is narrow: at 2.25 MHz the wavelength
is 1.69 mm and attenuation in a tight sandstone may already remove the first arrival's
amplitude.

## ★3

$$M = \rho V_P^{2} = 2400 \times 3800^{2} = 34.66\ \mathrm{GPa},$$

$$G = \rho V_S^{2} = 2400 \times 2100^{2} = 10.58\ \mathrm{GPa},$$

$$K = \rho\left(V_P^{2} - \tfrac{4}{3}V_S^{2}\right)
= 2400\left(1.444\times10^{7} - 5.880\times10^{6}\right) = 20.54\ \mathrm{GPa},$$

$$\nu = \frac{V_P^{2} - 2V_S^{2}}{2\left(V_P^{2} - V_S^{2}\right)}
= \frac{1.444\times10^{7} - 8.820\times10^{6}}{2(1.003\times10^{7})} = 0.2802,$$

$$E = 2G(1+\nu) = 2(10.584\times10^{9})(1.2802) = 27.10\ \mathrm{GPa}, \qquad
\frac{V_P}{V_S} = 1.8095 .$$

Sensitivity to 1 % in $V_S$ (26.25 m/s here), using $\partial K/\partial V_S = -\frac83\rho V_S$:

$$\delta K = \frac{8}{3}(2400)(2100)(0.01 \times 2100) = 2.822\times10^{8}\ \mathrm{Pa}
= 0.282\ \mathrm{GPa} \;\Rightarrow\; 1.37\ \% .$$

So $K$ and $\nu$ carry the largest amplification of a $V_S$ error, which is why a dataset
that quotes $K$ from an S-wave velocity measured with one transducer and one coupling has
to state the $V_S$ uncertainty explicitly rather than leaving it implicit.

## ★4

$$V_P(P) = 4500 + 1000\left(5.0\times10^{-3}P - 1.2\times10^{-5}P^{2}\right)
\ \mathrm{m/s}, \qquad
\frac{\mathrm{d}V_P}{\mathrm{d}P} = 1000\left(5.0\times10^{-3} - 2.4\times10^{-5}P\right)$$

| $P$ (MPa) | $V_P$ (m/s) | $\mathrm{d}V_P/\mathrm{d}P$ (m/s/MPa) |
|---|---|---|
| 0 | 4500.0 | 5.00 |
| 75 | 4807.5 | 3.20 |
| 150 | 4980.0 | 1.40 |

Physically, the **falling slope is crack closure**: the compliant, crack-like part of the
void space closes first and contributes most of $\mathrm{d}V/\mathrm{d}P$, so the rock
stiffens fastest when it is most compliant. Above roughly 100 MPa here the response is
dominated by the stiff pores and the solid frame, the slope tends to a smaller value, and
the velocity approaches an asymptote well below the mineral velocity. The same mechanism
produces hysteresis on unloading, because crack closure is partly irreversible.

## ★5

With $v = L/t = 0.0400/10.53\times10^{-6} = 3798.7$ m/s:

$$\frac{\delta L}{L} = \frac{0.01}{40.0} = 0.0250\ \%, \qquad
\frac{\delta t}{t} = \frac{0.01}{10.53} = 0.0950\ \%,$$

$$\frac{\delta v}{v} = \sqrt{0.0250^{2} + 0.0950^{2}} = 0.0982\ \%, \qquad
\delta v = 3.73\ \mathrm{m/s} .$$

The timing term is 3.8× the length term, so a better micrometer is not the improvement to
make; a faster timing card or cross-correlation arrival picking is. (Note that here the
net time is used directly, so this budget excludes the delay term — a delay error is a
separate systematic contribution.)

A 0.15 µs delay error gives

$$\frac{\delta v}{v} = -\frac{\delta t_0}{t} = -\frac{0.15}{10.53} = -1.42\ \%$$

— **fourteen times the timing resolution's contribution**, and it is systematic: it shifts
every specimen measured in that session that way. That asymmetry is the reason the delay is
re-measured at the end of a session: only a repeated calibration can reveal a change, and
no amount of within-session averaging can remove it.

## ★6

A model answer.

**Geometry.** Plugs of 38.1 mm diameter and 80–90 mm length ($L/D \approx 2.2$–2.4), cut
with parallel ends to 0.02 mm, dried by the mass criterion of
[01](../01-sample-preparation.md) and saturated under a verified vacuum. L/D of 2.5 would be
better for the end effect but consumes core; the choice is justified by the 0.5 % target,
since the synthetic end effect of $0.10\,D$ gives 4–5 % at L/D = 2 — so the **end effect
must be corrected** by the two-length method (each plug measured at two lengths, or a pair
of 40 mm and 80 mm plugs), not assumed away.

**Frequencies.** 1 MHz for $V_P$ and 0.5 MHz for $V_S$ as a starting point: at 1 MHz
$\lambda = 3.8$ mm and $L \ge 5\lambda$ needs $L \ge 19$ mm, comfortably satisfied, while
attenuation in a tight sandstone at 1 MHz is usually tolerable. The frequencies are
justified by measuring one plug at 0.5 and 1 MHz and reporting the dispersion, which is
also the check that the first arrival is the direct wave.

**Delay calibration.** The two-length method, on a reference specimen (not a rock plug)
measured at the **start and end of every session**, with the delay recorded. A change of
more than 0.05 µs between the two ends invalidates the session's data unless the pair is
re-measured.

**Pressure sequence.** Constant confining pressure, pore pressure stepped to give the
effective pressures $P_e = P_c - P_p$ required (5, 20, 50, 100 MPa), pore fluid and
temperature held constant and recorded, and the sequence run loading then unloading. The
temperature of the vessel matters because the delay and the fluid properties both drift;
the same fluid must be used for all four plugs so the comparison is not a fluid
comparison.

**Repeats.** Three repeats per pressure step per plug; the four plugs give the
between-specimen variability, which is the quantity the report needs.

**Uncertainty budget.** Length 0.0250 %, timing 0.010 µs on a ~10 µs net time = 0.10 %,
delay drift 0.05 µs = 0.48 %, repeatability (estimated from the three repeats) ~0.15 %.
Combined, without the delay drift, $\sqrt{0.025^2 + 0.10^2 + 0.15^2} = 0.182$ %, so the
0.5 % target is met with margin; **including** the delay drift the result is
$\sqrt{0.025^2+0.10^2+0.48^2+0.15^2} = 0.513$ %, i.e. exactly at the target. The
conclusion is that the delay calibration, not the timing card, is what the 0.5 % target
depends on.

**$K$ uncertainty.** From $\delta K/K$ for 1 % in $V_S$ being 1.37 % and for 1 % in $V_P$
about 3.6 % (measured relative to $K$), a 0.5 % $V_P$ and 0.5 % $V_S$ dataset gives
$\delta K/K \approx \sqrt{(0.5\times3.6)^2 + (0.5\times1.37)^2} = \sqrt{1.8^2+0.685^2}
= 1.93$ %, which just meets the 2 % target. So the $V_S$ target can be relaxed to 0.7 %
and $K$ still meets 2 % — the kind of trade a budget exists to expose.

**Checks.** (i) $V_P/V_S$ should be consistent with the porosity and saturation of
[01](../01-sample-preparation.md) and should not vary between plugs by more than the
between-specimen variability; (ii) the unloading curve should lie above the loading curve
and return to a value no lower than the initial one; (iii) $V_P$ at the highest effective
pressure should approach a stable value (a flattening slope) rather than continue rising
linearly; (iv) the delay check at the end of each session; (v) a reference plug measured
at the start, middle and end of the programme, which detects instrument drift and
operator drift separately.

**What cannot be defended.** The *in-situ* effective pressure and fluid state: the
laboratory uses a controlled pore pressure and a specified fluid, while the reservoir has
a different saturation history, and the translation to in-situ conditions depends on
assumptions (uniform saturation, no chemical reaction with the plug) that the
measurement cannot test. That limitation belongs in the methods section.
