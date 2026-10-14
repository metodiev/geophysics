# Exercises — 25-01-04 Project: Reading and Describing a Real Seismogram

Attempt these before reading the
[solutions](./04-reading-a-seismogram-solutions.md). The project is
[04 Reading a Seismogram](../04-reading-a-seismogram.md). Values printed by
[`code/reading_seismogram_demo.py`](../code/reading_seismogram_demo.py):

| Quantity | Demonstration value |
|---|---|
| record | 6000 samples, $f_s = 100\ \mathrm{Hz}$, 60 s, Nyquist 50 Hz |
| pre-event noise RMS | $0.0500\ \mathrm{\mu m\,s^{-1}}$ |
| P pick / error | $9.91\ \mathrm{s}$ / $-0.09\ \mathrm{s}$ |
| S pick / error | $15.72\ \mathrm{s}$ / $-0.28\ \mathrm{s}$ |
| measured S−P | $5.81\ \mathrm{s}$ (true $6.00\ \mathrm{s}$) |
| distance factor at $V_p/V_s = 1.734$ | $8.17\ \mathrm{km\,s^{-1}}$ |
| hypocentral distance | $47.49\ \mathrm{km}$ ($48.53\ \mathrm{km}$ at 10 km depth) |
| PGV, S window | $1.785\ \mathrm{\mu m\,s^{-1}}$ |
| SNR of the S peak | $35.7$ |
| dominant frequency | $0.82\ \mathrm{Hz}$, resolution $0.118\ \mathrm{Hz}$ |
| coda duration | $6.69\ \mathrm{s}$ |

Everything is **SYNTHETIC**; no real event or instrument is used.

## ★ Foundational

**★1.** A record is sampled at $40\ \mathrm{Hz}$ for 300 s. State the number of
samples, the Nyquist frequency, and the shortest representable period.

**★2.** With $V_p = 6.20\ \mathrm{km\,s^{-1}}$ and
$V_s = 3.55\ \mathrm{km\,s^{-1}}$, compute the S−P distance factor and the
hypocentral distance for the demonstration's measured S−P of $5.81\ \mathrm{s}$.

**★3.** The demonstration measures a pre-event RMS of $0.0500\
\mathrm{\mu m\,s^{-1}}$ over 9 s at 100 Hz. Compute the relative standard error
of that RMS estimate from $N$ samples and give the value in
$\mathrm{\mu m\,s^{-1}}$.

## ★★ Applied

**★★4.** The measured S−P is $5.81\ \mathrm{s}$ and the true S−P is
$6.00\ \mathrm{s}$. Compute the distance at both times, the distance error, and
the distance uncertainty implied by the S pick's own $0.28\ \mathrm{s}$ error.
State which of the two is the systematic component.

**★★5.** The S window is 8.5 s long at 100 Hz. Compute the spectral resolution
$\Delta f = f_s/N$, and the window length needed to separate two spectral peaks
$0.1\ \mathrm{Hz}$ apart. State whether the demonstration could have resolved a
$1.0\ \mathrm{Hz}$ wavelet from a $1.1\ \mathrm{Hz}$ one.

**★★6.** One standard regional form of the local magnitude is
$M_L = \log_{10} A + 1.11\log_{10} D + 0.00189\,D - 2.09$ with $A$ the
Wood–Anderson displacement amplitude in millimetres and $D$ the distance in
kilometres (constants vary by region and network). Convert the demonstration's
PGV of $1.785\ \mathrm{\mu m\,s^{-1}}$ at a period of $1.216\ \mathrm{s}$ to a
displacement amplitude via $A = \mathrm{PGV}\cdot T/(2\pi)$, compute the resulting
$M_L$, and state why the number is not a defensible magnitude.

## ★★★ Research-oriented

**★★★7.** Build a pick-error budget for the S arrival: quantise the sources
(sampling quantisation, detector bias, clock error, three-component projection,
velocity-model error in the distance conversion), give each a size in seconds or
in kilometres with a justification, combine them into a total distance
uncertainty, and state which term dominates and what one additional observation
would remove it. A budget without a dominant term is a failed answer.
