# Solutions — 06-07-01 Sources of Ambient Seismic Noise

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. Everything is SYNTHETIC. Lesson:
> [01 Sources of Ambient Seismic Noise](../01-noise-sources.md).

---

## ★1 — Bessel argument

$$f = \frac{1}{T} = \frac{1}{12} = 0.083333\ \mathrm{Hz},$$
$$k = \frac{2\pi f}{c} = \frac{2\pi \times 0.083333}{3.20}
= 0.163625\ \mathrm{rad\,km^{-1}},$$
$$kd = 0.163625 \times 40 = 6.545 .$$

$k$ has units of radians per kilometre (equivalently $\mathrm{km^{-1}}$,
since radians are dimensionless) and $kd$ is **dimensionless** — a requirement,
because it is an argument of the Bessel function.

---

## ★2 — Two swell trains

$$f_1 = 1/9.5 = 0.105263\ \mathrm{Hz}, \qquad
f_2 = 1/11.5 = 0.086957\ \mathrm{Hz},$$
$$f_{\text{sum}} = f_1 + f_2 = 0.192220\ \mathrm{Hz}
\;\Longrightarrow\;
T_{\text{secondary}} = \frac{1}{0.192220} = 5.202\ \mathrm{s},$$
$$f_{\text{beat}} = |f_1 - f_2| = 0.018306\ \mathrm{Hz}
\;\Longrightarrow\;
T_{\text{beat}} = 54.6\ \mathrm{s}.$$

The secondary microseism sits near $5.2\ \mathrm{s}$, and it is **not stationary**
in amplitude: the beat period of $54.6\ \mathrm{s}$ modulates it. That
modulation is why a microseism band is a band and why its peak wanders between
analysis windows.

---

## ★3 — Why a periodogram peak is not a constant

Two reasons, both measured in the demonstration.

1. **Spectral resolution.** The demonstration's periodogram has
   $df = 1.53\times10^{-4}\ \mathrm{Hz}$, which at $14\ \mathrm{s}$ is a period
   bin of $|dT/df|\,df = df/f^{2} = 1.53\times10^{-4}/(0.0714)^{2} =
   0.030\ \mathrm{s}$. The measurement cannot be quoted to better than a bin.
2. **A broad source spectrum.** The demonstration measures a peak at
   $15.87\ \mathrm{s}$ for an input centre of $16.0\ \mathrm{s}$ — an error of
   $0.13\ \mathrm{s}$, four bin widths — because the source bump is broad and
   the peak of a finite-length estimate wanders inside it. Its secondary peak is
   measured at $7.04\ \mathrm{s}$ against an input of $7.0\ \mathrm{s}$.

The honest quotation is a **band and a peak with an uncertainty**, not a
constant.

---

## ★4 — Where the coherence first vanishes

Set $kd = 2.4048$:

$$k = \frac{2.4048}{d} = \frac{2.4048}{60} = 0.040080\ \mathrm{rad\,km^{-1}},$$
$$f = \frac{kc}{2\pi} = \frac{0.040080 \times 3.20}{2\pi} = 0.020413\ \mathrm{Hz},$$
$$T = \frac{1}{f} = 48.99\ \mathrm{s}.$$

So the pair is first incoherent at about $49\ \mathrm{s}$. That period is
**outside** the lesson's table, whose slowest row is 20 s and therefore already
past that first zero: the tabulated rows span the intervals between the later
zeros of $J_0$, which fall at

$$T = \frac{2\pi d}{c\,kd_j} \quad\text{gives}\quad
21.34,\ 13.61,\ 9.99,\ 7.89,\ 6.52\ \mathrm{s}, \dots$$

for the successive zeros $kd_j$. This is why the sign of the tabulated coherence
changes between rows ($+0.1192$ at 20 s, $-0.0025$ at 10 s, $-0.1840$ at 7 s,
$+0.0159$ at 3.5 s): each row lies in a different inter-zero interval.

---

## ★5 — Coherence 0.93 at 7 s

The demonstration's table at $T = 7\ \mathrm{s}$ ($J_0 = -0.1840$) gives

| sector | $|C|$ |
|---|---|
| 360° | 0.1840 |
| 180° | 0.1857 |
| 90° | 0.3120 |
| 45° | 0.9287 |
| 20° | 0.9971 |

A measured magnitude of $0.93$ is consistent with a sector of about $45^\circ$,
interpolating between the $45^\circ$ ($0.9287$) and $20^\circ$ ($0.9971$)
entries.

**Caveat.** The magnitude alone cannot separate a source-sector effect from a
laterally varying structure, which changes the effective $kd$ (hence $J_0$) in
the same direction. The discriminating measurement is the **phase**: the
isotropic value is real ($179.99^\circ$ in the table, i.e. exactly out of
phase), whereas the $45^\circ$ sector has phase $-139.96^\circ$. A structure
anomaly changes the magnitude with a phase that tracks the travel-time
perturbation, and the two must be modelled together.

---

## ★6 — Excess kurtosis from one spike

With $z = x/\sigma$, the Gaussian samples have $\mathbb{E}[z^{4}] = 3$
exactly. Averaging,

$$\mathbb{E}[z^{4}] = \frac{9999 \times 3 + 5^{4}}{10\,000}
= \frac{29\,997 + 625}{10\,000} = 3.0622,$$
$$K = \mathbb{E}[z^{4}] - 3 = +0.0622 .$$

The demonstration's impulsive case has $K = +35.277$. The ratio
$35.277/0.0622 = 567$ shows that a kurtosis of tens requires *many* transients
or *larger* ones: 400 boosts of $8$-$20\sigma$ in $400\,000$ samples give a
$z^4$ contribution of order $400\times10^{4}/400\,000 = 10$, and the observed
35 means the largest boosts reach $20\sigma$ each, contributing
$20^{4}=1.6\times10^{5}$ per event. **Kurtosis is a fourth-moment statistic: it
is dominated by the largest few samples, so it is a sensitive but unstable
detector of transients.**

---

## ★7 — Directional sources versus structure (specification)

**Observable 1: causal/acausal ratio.** Invert the noise-to-Green's-function
retrieval for a pair and measure the amplitude ratio of the two branches
(lesson 02, §5, measures 0.75 for a full ring and 21.04 for a $45^\circ$
sector). *Directional sources:* the ratio departs from 1. *Structure:* a
structure anomaly between the stations shifts both branches nearly equally and
changes the ratio only through the weak asymmetry of the anomaly's position
along the path. **Test:** the ratio should be independent of the season and
stable on a medium without real change.

**Observable 2: the phase of the coherence as a function of azimuth.** With
three or more stations, compute the pairwise coherence phase and invert for the
apparent arrival direction. *Directional sources:* the apparent direction is
stable in time and points to the dominant source region. *Structure:*
the apparent direction depends on the pair's azimuth relative to the anomaly.
**Test:** repeat with a source-independent measurement (an earthquake) on the
same pairs; structure must be consistent between the two, a source bias is not.

A study that measures only one of the two observables cannot separate the
hypotheses; this is the honest statement of the problem.

---

## ★8 — The three assumptions, their violations and their signatures

**(i) Uncorrelated sources.** Violated by two nearby coherent sources (a
resonating structure, a ship's engine, a wind turbine). *Signature:* the
coherence magnitude shows narrow-band spikes that repeat between epochs and
survive longer stacking than the $\sqrt{N}$ law allows (a measured exponent well
below 0.5). *Detection:* split the record in time and test the exponent, or
compute the coherence between stations that share no path.

**(ii) Far field.** Violated when a source sits inside or near the array, so
the incident wavefront is curved. *Signature:* the measured coherence depends on
the assumed source distance; $J_0(kd)$ fits poorly and the misfit has a
range dependence. *Detection:* add a near-field term to the model and test
whether the fit improves; or use pairs with the same $d$ but different azimuths
and check that they agree.

**(iii) One wave speed.** Violated where two modes with different speeds carry
comparable energy (fundamental and first higher mode; Rayleigh and Love on the
same component; body waves and surface waves in the same band). *Signature:* the
retrieved phase velocity is not a smooth function of period, and the retrieved
waveform has extra branches that no 1-D model explains. *Detection:* measure the
dispersion curve and test whether a single mode can fit it; if not, both modes
must be modelled and their relative amplitudes measured.
