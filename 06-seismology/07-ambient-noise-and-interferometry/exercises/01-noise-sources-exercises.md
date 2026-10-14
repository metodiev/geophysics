# Exercises — 06-07-01 Sources of Ambient Seismic Noise

Attempt these before reading the
[solutions](./01-noise-sources-solutions.md). The lesson is
[01 Sources of Ambient Seismic Noise](../01-noise-sources.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A station pair is separated by $d = 40\ \mathrm{km}$ in a medium with
$c = 3.20\ \mathrm{km\,s^{-1}}$. Compute the Bessel argument $kd$ at
$T = 12\ \mathrm{s}$. State the units of $k$ and of $kd$.

**★2.** Ocean swell contains two wave trains of periods $9.5\ \mathrm{s}$ and
$11.5\ \mathrm{s}$. Compute their frequencies, the sum frequency and the
**secondary** microseism period; then compute the **beat** period of the
difference frequency.

**★3.** A colleague quotes the primary microseism period as exactly
$14\ \mathrm{s}$ from a month of data. State two reasons why a periodogram peak
is not a constant, using the demonstration's own measurement error.

## ★★ Applied

**★★4.** Using the demonstration's model ($d = 60\ \mathrm{km}$,
$c = 3.20\ \mathrm{km\,s^{-1}}$), find the period at which the coherence of two
stations first vanishes, and compare it with the first zero of $J_0$,
$kd = 2.4048$.

**★★5.** A pair of stations shows a coherence magnitude of $0.93$ at
$T = 7\ \mathrm{s}$. Using the sector table of §6 of the lesson, state which
illumination width is consistent with this value, and give the caveat that makes
the inference weak.

**★★6.** A Gaussian series of $10\,000$ samples contains a single sample equal
to $5\sigma$; all others are Gaussian. Estimate the excess kurtosis. Compare with
the demonstration's impulsive case, $+35.277$, and state what the comparison
shows about how many transients are needed to produce that value.

## ★★★ Research-oriented

**★★★7.** Design a measurement that would distinguish a directional source
field from lateral structure beneath a pair of stations, using only
single-station and two-station noise data. State the observable, the prediction
for each hypothesis, and the discriminating test. You do not need to run it, but
a specification that could not be executed is a failed answer.

**★★★8.** The derivation of $C(f) = S(f)J_0(kd)$ assumed (i) uncorrelated
sources, (ii) far field, (iii) one wave speed. For each assumption, give an
observation that violates it in a real deployment, a signature of that violation
in the coherence, and one way to reduce or detect it.
