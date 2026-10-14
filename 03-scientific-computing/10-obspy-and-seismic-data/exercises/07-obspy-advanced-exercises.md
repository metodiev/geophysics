# Exercises — 03-10-07 Cross-Correlation, Polarisation and Array Processing

Attempt these **closed-book** before opening the
[solutions](./07-obspy-advanced-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first:

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/obspy_advanced_demo.py
```

---

## ★ Foundational

**★1.** State ObsPy's cross-correlation sign convention using the measured
25-sample case, then state what a *positive* lag means in words.

**★2.** Give the measured correlation coefficients at 0.05, 0.20 and 0.50
counts RMS of noise, and state the noise level at which the lag itself becomes
wrong.

**★3.** Name the four outputs of `polarization_analysis` and give the measured
value of each for the synthetic P arrival (azimuth, incidence, rectilinearity
range, and the azimuth in the noise windows).

**★4.** Give the measured `array_processing` azimuth and slowness for an injected
propagation azimuth of 60.0° and slowness 0.2500 s/km, with units.

**★5.** State the measured max STA/LTA and trigger time for signal amplitudes
×1.00, ×0.20 and ×0.05, and the true wavelet centre.

---

## ★★ Applied

**★★6.** Show that the azimuth column is the back-azimuth by computing
$-120.2564 + 360$ and comparing with the injected propagation azimuth. Then
state what a regional focal-mechanism calculation would get wrong if the
convention were assumed to be the propagation azimuth.

**★★7.** Show by arithmetic that the slowness column cannot be in s/deg:
convert 0.25006 with 111.195 km/deg and compare with the injected 0.2500 s/km.

**★★8.** Find the noise level at which the correlation coefficient falls below
0.5 by interpolating the measured table; then state a one-sentence rule of
thumb for deciding whether a lag is trustworthy.

**★★9.** Write down two $(\theta, p)$ pairs that describe the same slowness
vector, and explain why a beamformer that searches over $(\theta, p)$ with
$p$ allowed to be negative is redundant.

**★★10.** The demonstration's independent beamformer agrees with
`array_processing` in back-azimuth to 0.08°. Compute the theoretical resolution
$\lambda/(2D)$ for a 6 Hz signal on a 2 km-radius array with wavespeed 4 km/s,
and state whether the agreement is at that level.

---

## ★★★ Research-oriented

**★★★11.** Measure the azimuth resolution of the seven-element, 2 km array as a
function of frequency (2, 4, 8, 12 Hz), report the error versus frequency, and
compare with the $\lambda/(2D)$ estimate. State where the comparison fails and
why.

**★★★12.** Introduce a 1 km horizontal coordinate error at one array element
and measure the resulting back-azimuth bias as a function of the error's
direction. Report the worst-case bias, and state why array-geometry errors
dominate the practical error budget.

**★★★13.** Design a picking algorithm that turns the STA/LTA detection into an
arrival time, measure its bias and scatter on 100 synthetic traces at three
signal-to-noise ratios, and compare it with the cross-correlation lag of the
same arrivals. State which is better and for which signal-to-noise range.
