# Solutions — 06-05-01 Measuring Q: Spectral Ratio, Rise Time, Multiple Methods

The lesson is [01 Measuring Q](../01-attenuation-measurement.md). All models are
**SYNTHETIC**. Arithmetic is shown so that every number can be checked.

## ★ Foundational

**★1.** With $f = 2\ \mathrm{Hz}$, $v = 3500\ \mathrm{m\,s^{-1}}$,
$Q = 150$:

$$\alpha = \frac{\pi f}{Q v} = \frac{3.141593 \times 2}{150 \times 3500}
= \frac{6.283185}{5.25\times10^{5}} = 1.197\times10^{-5}\ \mathrm{m^{-1}},$$

$$1/\alpha = 8.354\times10^{4}\ \mathrm{m} = 83.5\ \mathrm{km}.$$

The wavelength is $\lambda = v/f = 3500/2 = 1750\ \mathrm{m} = 1.75\
\mathrm{km}$, some 48 times smaller. They are different quantities: $1/\alpha$ is
the distance over which the **amplitude** falls by $1/e$, while $\lambda$ is the
spatial period. The two are related exactly by
$\alpha = \pi/(Q\lambda)$, so $1/\alpha = Q\lambda/\pi = 150 \times 1750/\pi =
83\,500\ \mathrm{m}$, confirming the number above. Like $\lambda$, the decay
length scales inversely with frequency, because a fixed $Q$ loses the same
*fraction* of energy per cycle.

**★2.** In the ideal case with equal source and coupling,

$$\ln\frac{A_1}{A_2} = \ln\frac{x_2}{x_1} + \frac{\pi (x_2-x_1)}{Q v} f .$$

With $x_2/x_1 = 130/30 = 4.3333$, $\ln(x_2/x_1) = 1.46634$ and
$x_2-x_1 = 1.0\times10^{5}\ \mathrm{m}$:

$$m = \frac{\pi \times 10^{5}}{150 \times 3500} = \frac{3.141593\times10^{5}}
{5.25\times10^{5}} = 0.598398\ \mathrm{Hz^{-1}},$$

$$\ln\frac{A_1}{A_2}(5\ \mathrm{Hz}) = 1.46634 + 0.598398 \times 5
= 1.46634 + 2.99199 = 4.458 .$$

**★3.** Invert the same relation with $Q = 80$ in place of 150:

$$Q = \frac{\pi (x_2-x_1)}{v\,m} = \frac{3.141593\times10^{5}}
{3500 \times 0.1132} = \frac{3.141593\times10^{5}}{396.2}
= 792.9 \Rightarrow \mathbf{793}.$$

The slope $m$ has units of $\mathrm{Hz^{-1}}$ (dimensionless per hertz), because
it multiplies $f$ in an exponent: $\pi\Delta x/(Qv)$ is
$\mathrm{m}/(\mathrm{m\,s^{-1}}) = \mathrm{s}$, and $m f$ is dimensionless.

## ★★ Applied

**★★4.** For $N = 150$ uniformly spaced frequencies over $W = 7.5\ \mathrm{Hz}$
(lowest frequency $0.5\ \mathrm{Hz}$),

$$\sum_i (f_i-\bar f)^2 = \frac{N(N^2-1)}{12}\left(\frac{W}{N-1}\right)^{2}
= \frac{150 \times 22499}{12}\left(\frac{7.5}{149}\right)^{2}
= 281\,238 \times 2.534\times10^{-3} = 712.6,$$

so $\sqrt{\sum} = 26.69$ and

$$\sigma_m = \frac{\sigma_y}{\sqrt{\sum}} = \frac{1.414214}{26.69}
= 5.299\times10^{-2}\ \mathrm{Hz^{-1}}.$$

The true slope for $Q = 150$ is $m = 0.598398\ \mathrm{Hz^{-1}}$, so

$$\frac{\sigma_Q}{Q} = \frac{\sigma_m}{m} = \frac{0.05299}{0.598398}
= 8.86\%.$$

A $1.5\%$ answer is **not** possible in this band: no amount of stacking inside
the band helps, because the information is limited by the lever arm $W$. A
$1.5\%$ target needs $\sqrt{\sum} = \sigma_y/(m \times 0.015) = 1.414214/0.008976
= 157.6$, i.e. $\sum = 24\,840$, i.e. $W = \sqrt{12 \times 24840/150} =
44.6\ \mathrm{Hz}$ — more than the usable band of any real body-wave
measurement, which is why real studies average many paths.

**★★5.** The model is $\mathrm{FWHM}(\tau_r) = 2\tau_s + \tau_r/Q$; widths add
**linearly** for Lorentzian pulses.

Slope from the two points:
$$Q = \frac{\Delta\tau_r}{\Delta \mathrm{FWHM}} = \frac{30.0-12.0}{0.761-0.311}
= \frac{18.0}{0.450} = 40.0 .$$

Source width: $2\tau_s = \mathrm{FWHM} - \tau_r/Q = 0.311 - 12.0/40 = 0.311 -
0.300 = 0.011\ \mathrm{s}$, i.e. $\tau_s = 0.0055\ \mathrm{s}$ — consistent
between the two arrivals only if the model is right, which is the check to run:
predicted second width $= 0.011 + 30/40 = 0.761\ \mathrm{s}$, equal to the
measured value to three figures, so the model and the picks agree.

The slope is the measurement because the intercept *is* the source width (twice
it), and the source width is unknown. Only the change with travel time is
source-independent — the same reason the spectral-ratio method uses a slope.

**★★6.** For $f_0 = 1\ \mathrm{Hz}$, $D = 0.020$,

$$\frac{1}{Q(f)} = 0.020\,\frac{f}{1 + f^{2}} .$$

In the same convention as the demonstration (an arithmetic mean over linearly
spaced frequencies, as produced by fitting a straight line to the slope),

$$\langle 1/Q\rangle = \frac{0.020}{2-0.5}\int_{0.5}^{2}\frac{f}{1+f^{2}}\,
\mathrm{d}f = \frac{0.020}{1.5}\left[\frac{1}{2}\ln(1+f^{2})\right]_{0.5}^{2}
= 0.0133333 \times 0.693147 = 0.00923885,$$

so $\langle 1/Q\rangle = 9.24\times10^{-3}$ and the band-$Q$ is
$1/0.00923885 = \mathbf{108}$. (Averaging in $\ln f$ instead gives
$1/Q = 0.009281$, $Q = 107.8$ — the convention matters at the 1% level and must
be stated.)

The band-$Q$ is **108**, against $Q(f_0) = 100$: an 8% bias in $Q$ from the
band average alone, with no noise. The colleague's $Q = 90$ therefore cannot be
produced by this relaxation with this band; it needs either a lower-frequency
band (where $1/Q$ grows roughly as $f$ toward the peak) or a larger $D$. What the
claim needs to be reproducible is: **the band**, the estimator (slope of the log
spectral ratio), the assumed source, and whether the number is
$\langle 1/Q\rangle$ or $Q$ at a stated frequency. Compare the demonstration's
table, where the same synthetic Earth reports 121.91, 216.26, 472.79 or 1392.37
depending only on the band.

## ★★★ Research-oriented

**★★★7.** **Estimator.** Two-receiver (or two-distance) spectral ratio, fitted
in the log domain; $Q = \pi\Delta x/(v m)$.

**Band and precision.** Usable band $W = 6 - 0.8 = 5.2\ \mathrm{Hz}$,
$\sigma_y = \sqrt{2}\,\sigma = 0.0707$, and with $N$ frequencies uniformly spaced
$\sum_i(f_i-\bar f)^2 \approx NW^{2}/12$. The target is
$\sigma_Q/Q = \sigma_m/m \le 0.02$, with

$$m = \frac{\pi \Delta x}{Q v} = \frac{3.141593 \times 6\times10^{4}}
{Q \times 3200} .$$

For a working assumption $Q = 100$: $m = 1.8850\times10^{5}/3.2\times10^{5}
= 0.58905\ \mathrm{Hz^{-1}}$.

$$\sqrt{\textstyle\sum_i(f_i-\bar f)^2} = \frac{\sigma_y}{m \times 0.02}
= \frac{0.0707}{0.58905 \times 0.02} = 6.001,$$

so $\sum = 36.03$, and since $\sum = NW^{2}/12 = 2.2533N$,

$$N \ge \frac{36.03}{2.2533} = 16\ \text{frequencies in } [0.8, 6]\ \mathrm{Hz}.$$

**Plan.** Use $N = 30$ log-spaced frequencies in the band (giving
$\sum = 67.6$, i.e. $\sigma_Q/Q = 1.46\%$ per path), fit the slope in the log
domain with the geometric term fixed at $\ln(x_2/x_1)$, and repeat on $K = 4$
independent two-station pairs on the same structure, which brings the formal
error to $1.46\%/\sqrt{4} = 0.73\%$ and — more importantly — gives a scatter
between paths that can be compared with the formal error. Report: the band, $N$,
the fitted slope with its formal error, the inter-path scatter, and $Q$ with the
assumption $v = 3200\ \mathrm{m\,s^{-1}}$ stated (the velocity enters linearly,
so a $2\%$ velocity error is a $2\%$ $Q$ error and it is not reduced by
averaging paths).

**★★★8.** Dispersion measurement: $\Delta t/\tau_r = (1/(\pi Q))\ln(f_2/f_1)$.
With $\Delta t = 0.010\ \mathrm{s}$, $\tau_r = 24.0\ \mathrm{s}$,
$\ln(10/1) = 2.302585$:

$$\frac{1}{\pi Q} = \frac{\Delta t}{\tau_r \ln(f_2/f_1)}
= \frac{0.010}{24.0 \times 2.302585} = 1.8097\times10^{-4},
\qquad Q_{\text{disp}} = \frac{1}{\pi \times 1.8097\times10^{-4}} = 1759 .$$

The spectral-ratio measurement gave $Q = 200$; the dispersion measurement gives
$Q \approx 1759$. They are **inconsistent by a factor of about 9** — they cannot
both be right for the same path and band.

Interpretation: the dispersion relation is a *causality* statement and is
therefore the more robust of the two in form, but it is numerically vicious
here: the predicted delay for $Q = 200$ over one decade on a $24\ \mathrm{s}$
path is $\Delta t = \tau_r \ln 10/(\pi Q) = 24 \times 2.302585/(628.32)
= 0.0879\ \mathrm{s}$, which is 8.8 times the measured $0.010\ \mathrm{s}$. A
measured delay *smaller* than the attenuation-implied delay is a classic sign
that the two "frequencies" were not measured on the same phase, or that the band
used for $Q$ is not the band used for the dispersion (a low-frequency spectral
ratio is strongly biased by the source corner).

Trust for a $1\%$ velocity correction: the **dispersion** measurement, because it
is a travel-time difference between two frequencies of the same phase, and its
error is set by timing precision (sub-millisecond is achievable), whereas the
$Q$ from a spectral ratio over $[1,10]\ \mathrm{Hz}$ carries a bandwidth-limited
error of several per cent and a possible source-corner bias. But it must be
measured on the same phase, and the inconsistency above must be resolved before
either is used.
