# Solutions — 06-04-04 Magnitude Scales: Local, Body, Surface, Duration, Moment

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [04 Magnitude Scales](../04-magnitude-scales.md).

---

## ★1 — Moment magnitude

$$
M_w = \tfrac{2}{3}(\log_{10}M_0 - 9.1).
$$

For $M_0 = 3.0\times10^{16}$: $\log_{10}M_0 = 16.4771$, so
$M_w = \tfrac{2}{3}(7.3771) = 4.918$.

For $M_0 = 10^{19}$: $\log_{10}M_0 = 19$, so
$M_w = \tfrac{2}{3}(9.9) = 6.600$.

---

## ★2 — Plateau

$$
\Omega_0 = \frac{M_0\,a}{4\pi\rho\beta^{3}R}
= \frac{10^{19}\times0.6325}{1.4547\times10^{20}}
= 4.348\times10^{-2}\ \mathrm{m\,s}.
$$

The plateau scales linearly with $M_0$, as Section 3.1 states.

---

## ★3 — Corner frequency

$$
f_c = 0.6\times\left(\frac{10^{20}}{10^{15}}\right)^{-1/3}
= 0.6\times(10^{5})^{-1/3}
= 0.6\times10^{-1.667}
= 0.6\times0.02154 = 0.01293\ \mathrm{Hz},
$$

which is the printed $0.0129\ \mathrm{Hz}$.

---

## ★4 — The two slopes

On the flat branch, $f_b \ll f_c$ and $A \approx \Omega_0 \propto M_0$; with
$\log_{10}M_0 = \tfrac{3}{2}M_w + 9.1$,
$M = \log_{10}A + c = \log_{10}M_0 + c' = \tfrac{3}{2}M_w + c''$, so the slope is
$3/2$.

On the $f^{-2}$ branch, $f_b \gg f_c$ and
$A \approx \Omega_0(f_c/f_b)^{2} \propto M_0 M_0^{-2/3} = M_0^{1/3}$, so
$M = \tfrac{1}{3}\log_{10}M_0 + c = \tfrac{1}{2}M_w + c'$, and the slope is
$1/2$.

---

## ★5 — A band amplitude

For $M_0 = 10^{20}\ \mathrm{N\,m}$ the plateau is
$\Omega_0 = 4.348\times10^{-1}\ \mathrm{m\,s}$ (one decade above the $10^{19}$
value of ★2, since the plateau is proportional to $M_0$). Then

$$
A = \frac{4.348\times10^{-1}}{1 + (1/0.01293)^{2}}\times e^{-0.2244}
= \frac{4.348\times10^{-1}}{1 + 5983.6}\times0.7990
= 7.265\times10^{-5}\times0.7990
= 5.805\times10^{-5}\ \mathrm{m} = 58.05\ \mathrm{\mu m},
$$

which is the printed $5.804\times10^{1}\ \mathrm{\mu m}$. The band sits on the
$f^{-2}$ branch — the denominator is 5984 — so this is the regime in which the
amplitude grows as $M_0^{1/3}$ rather than as $M_0$.

---

## ★6 — A secant slope

$$
\frac{3.37 - 1.64}{3.27 - 1.93} = \frac{1.73}{1.34} = 1.291
$$

against the least-squares value 1.299 for the same third. The difference is
curvature: the scale's slope is not constant over a third of the range, so the
secant and the fit differ in the third decimal, not the first.

---

## ★7 — Saturation versus non-self-similarity

**Test:** for each event with a measured $M_0$ and $f_c$, compute the predicted
$M_s$ from the spectrum *using the same $f_c$*, then compare the predicted and
reported $M_s$. If the reported $M_s$ falls below the prediction as size grows,
the scale is compressed relative to the spectrum; if instead the measured $f_c$
itself fails to follow $M_0^{-1/3}$, the spectrum is not self-similar.

**Deciding observation:** a measured exponent in $r \propto M_0^{p}$ differing
from $1/3$, with the $M_s$ values still following the prediction, indicts
self-similarity rather than the scale.

---

## ★8 — Calibrating a real scale

**Experiment:** for a set of reference events with independently known $M_0$
(well-determined from moment tensors), record the band amplitude at each
station, regress $\log_{10}A$ against distance for each event to obtain the
distance correction, then difference the result from $M_w$ to obtain the additive
constant.

**Inputs:** an instrument response, polarities/mechanisms for the radiation
correction, hypocentres, an attenuation model, and a set of events spanning the
size range.

**Reporting:** quote the constant with the standard error of the regression at a
reference distance, and quote the magnitude with an uncertainty that includes the
residual scatter of the calibration, not only the reading error of the single
amplitude.
