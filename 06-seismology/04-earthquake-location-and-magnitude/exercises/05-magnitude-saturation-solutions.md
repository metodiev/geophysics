# Solutions — 06-04-05 Magnitude Saturation and Why Moment Magnitude Is Preferred

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [05 Magnitude Saturation](../05-magnitude-saturation.md).

---

## ★1 — Crossing size

$$
M_0^{\text{cross}} = M_{0,\text{ref}}
\left(\frac{f_{c,\text{ref}}}{f_b}\right)^{3}
= 10^{15}\left(\frac{0.6}{0.5}\right)^{3}
= 10^{15}\times1.728 = 1.728\times10^{15}\ \mathrm{N\,m},
$$

$$
M_w^{\text{cross}} = \tfrac{2}{3}\left(\log_{10}(1.728\times10^{15}) - 9.1\right)
= \tfrac{2}{3}(15.2375 - 9.1) = \tfrac{2}{3}(6.1375) = 4.09 .
$$

The band lies below the reference corner frequency, so the crossing happens
*above* the reference event — a lower-frequency band saturates at a larger size.

---

## ★2 — Asymptotic slopes

On the $f^{-2}$ branch the amplitude grows as $M_0^{1/3}$, so

$$
\frac{\mathrm{d}M}{\mathrm{d}M_w} = \frac{1}{2},
\qquad
\frac{\mathrm{d}M}{\mathrm{d}\log_{10}M_0} = \frac{1}{3} .
$$

A saturated scale still grows; it grows at half the rate in $M_w$.

---

## ★3 — A magnitude difference as a moment factor

$$
10^{1.5\times0.5} = 10^{0.75} = 5.62 .
$$

Half a magnitude unit is a factor of 5.6 in moment, since
$\log_{10}M_0 = 1.5M_w + 9.1$.

---

## ★4 — A b-value, inverted

$$
\bar{M} = M_{\min} + \frac{\log_{10}e}{\hat{b}}
= 3.98 + \frac{0.4343}{1.609} = 3.98 + 0.270 = 4.25 .
$$

The corresponding $M_w$ sample has
$\bar{M}_w = 4.00 + 0.4343/1.012 = 4.00 + 0.429 = 4.43$. The two samples
describe the same earthquakes with means that differ by 0.18 in their own units —
which is precisely why the magnitude type must be quoted with the b-value.

---

## ★5 — The cost of a linear conversion

$$
M_w^{\text{est}} = 1.261\times6.10 - 0.935 = 7.692 - 0.935 = 6.76 .
$$

A true $M_w = 8.0$ event is reported as 6.76: a bias of $-1.24$ magnitude units,
or a moment factor

$$
10^{1.5\times1.24} = 10^{1.86} = 72 .
$$

The tabulated value for $M_w = 8.0$ in the lesson is exactly this row.

---

## ★6 — Why the $M_s$ crossing is larger

The crossing condition is $f_c(M_0) = f_b$, and $f_c \propto M_0^{-1/3}$. A lower
band frequency therefore requires a *smaller* $f_c$ and hence a *larger* $M_0$:

$$
\frac{M_0^{\text{cross}}(M_s)}{M_0^{\text{cross}}(m_b)}
= \left(\frac{f_b^{m_b}}{f_b^{M_s}}\right)^{3}
= \left(\frac{1.0}{0.05}\right)^{3} = 8000 ,
$$

which is $\log_{10}(8000) = 3.90$ decades of moment, or
$\tfrac{2}{3}(3.90) = 2.6$ magnitude units — the difference between the printed
crossings of 3.49 and 6.09.

---

## ★7 — Recovering the b-value of the seismicity

**Data needed:** the $m_b$ values; the $m_b(M_w)$ curve with its saturation
parameters for the network that produced them (or enough events with independently
measured $M_w$ to fit it); completeness magnitude as a function of time; the
focal mechanism subset needed for the radiation correction.

**Form:** invert the curve event by event and fit the GR law to the recovered
$M_w$ by maximum likelihood with a completeness threshold; alternatively fit a
GR law convolved with the (nonlinear) $m_b$ mapping directly to the $m_b$
sample, which propagates the saturation properly.

**Expected bias with a single linear term:** the linear calibration is fitted at
small sizes where the slope is $3/2$; applying it at large sizes where the slope
is $1/2$ under-reports large events, which compresses the upper end of the
distribution and steepens the fitted line, biasing the recovered b-value upward
— the same sign as the inflation measured in the lesson's catalogue.

---

## ★8 — The missing finite-fault effect

A point-source spectrum has one corner and no length scale other than $f_c$. A
finite fault has a *duration* set by rupture propagation, so the observed
surface wave of a great earthquake is the integral over a moving source. The
spectrum gains a second, lower corner and a steeper decay in the intermediate
band, and the 20 s wave may sample only part of the source.

**Prediction:** the real $M_s$ curve departs from the synthetic one *sooner* and
*flatter*, i.e. real $M_s$ saturates at a smaller $M_w$ and with a smaller
asymptotic slope than the 0.50 measured here. The synthetic curve is therefore a
*lower bound* on the saturation of real catalogues.
