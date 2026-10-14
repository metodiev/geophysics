# Solutions — 25-01-04 Project: Reading and Describing a Real Seismogram

> Read after attempting. Lesson:
> [04 Reading a Seismogram](../04-reading-a-seismogram.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/reading_seismogram_demo.py`](../code/reading_seismogram_demo.py).

---

## ★1 — Sampling arithmetic

$$N = f_s T = 40 \times 300 = 12\,000\ \text{samples},
\qquad f_\text{Nyq} = \frac{f_s}{2} = 20\ \mathrm{Hz},
\qquad T_\text{min} = \frac{1}{20} = 0.050\ \mathrm{s} = 50\ \mathrm{ms}.$$

Any energy above 20 Hz is aliased into the band and cannot be recovered. The
Nyquist frequency is a property of the *recording*, not of the earthquake.

---

## ★2 — The S−P factor

$$\frac{V_p V_s}{V_p - V_s} = \frac{6.20 \times 3.55}{6.20 - 3.55}
= \frac{22.01}{2.65} = 8.306\ \mathrm{km\,s^{-1}},$$

$$D = 5.81 \times 8.306 = 48.26\ \mathrm{km}.$$

Unit check: $\mathrm{s} \times \mathrm{km\,s^{-1}} = \mathrm{km}$ ✔. Compared
with the demonstration's $47.49\ \mathrm{km}$ at $V_p = 6.00\ \mathrm{km\,s^{-1}}$
and $V_s = 3.46\ \mathrm{km\,s^{-1}}$, changing the model by a few percent
changed the distance by $0.77\ \mathrm{km}$ ($1.6\%$).

---

## ★3 — Uncertainty of a noise estimate

For $N$ samples the sample standard deviation has relative standard error

$$\frac{1}{\sqrt{2N}} = \frac{1}{\sqrt{2 \times 900}} = \frac{1}{42.43} = 2.36\%,$$

so

$$\sigma_\text{noise} = 0.0500 \times 0.0236 = 0.0012\ \mathrm{\mu m\,s^{-1}}.$$

Reported: **RMS $= 0.0500 \pm 0.0012\ \mathrm{\mu m\,s^{-1}}$** over the 9 s
pre-event window. The measurement is not a property of the station: a different
window (night versus day, before versus after a train) gives a different number,
which is why the window belongs in the report.

---

## ★4 — Distance error versus pick uncertainty

At the measured S−P of $5.81\ \mathrm{s}$:

$$D_\text{measured} = 5.81 \times 8.17 = 47.49\ \mathrm{km}.$$

At the true S−P of $6.00\ \mathrm{s}$:

$$D_\text{true} = 6.00 \times 8.17 = 49.04\ \mathrm{km}.$$

$$\text{distance error} = 47.49 - 49.04 = -1.55\ \mathrm{km}\ (-3.2\%).$$

The distance **uncertainty** from the S pick's own error is

$$\delta D = 0.28 \times 8.17 = 2.29\ \mathrm{km},$$

which is **larger** than the actual error of $1.55\ \mathrm{km}$ — the error is
consistent with the stated pick uncertainty, so the number to quote is
$47.5 \pm 2.3\ \mathrm{km}$.

**Systematic versus random.** The $1.55\ \mathrm{km}$ error is the *systematic*
component: the STA/LTA detector picks early for every arrival, so repeating the
measurement does not average it away. The $2.29\ \mathrm{km}$ is the *random*
component associated with one realisation of the pick. Reducing the systematic
part needs a different detector; reducing the random part needs a better SNR or
more stations.

---

## ★5 — Spectral resolution

$$N = 8.5\ \mathrm{s} \times 100\ \mathrm{Hz} = 850\ \text{samples},
\qquad
\Delta f = \frac{f_s}{N} = \frac{100}{850} = 0.1176\ \mathrm{Hz},$$

matching the demonstration's $0.118\ \mathrm{Hz}$.

To separate two peaks $\delta f = 0.1\ \mathrm{Hz}$ apart the Rayleigh criterion
requires

$$T = \frac{1}{\delta f} = 10\ \mathrm{s}.$$

The 8.5 s window is **just short** of that: it could not reliably resolve a
1.0 Hz wavelet from a 1.1 Hz one, and indeed the demonstration's measured peak
of $0.82\ \mathrm{Hz}$ is a broad lobe, not a resolved line. The remedy is a
longer window (or a parametric estimate), not a finer frequency grid — zero
padding interpolates the spectrum without adding resolution.

---

## ★6 — Why the computed magnitude is not a magnitude

Displacement amplitude from PGV and period:

$$A = \frac{\mathrm{PGV}\cdot T}{2\pi}
= \frac{1.785 \times 1.216}{6.2832}
= 0.3455\ \mathrm{\mu m} = 3.455\times10^{-4}\ \mathrm{mm}.$$

$$M_L = \log_{10}(3.455\times10^{-4}) + 1.11\log_{10}(47.49)
+ 0.00189 \times 47.49 - 2.09$$

$$= -3.4616 + 1.8610 + 0.0898 - 2.09 = -3.60.$$

A local magnitude of $-3.6$ is far below the smallest events local networks
routinely record, and the value is not physically defensible. Three reasons:

1. **The channel is not a Wood–Anderson instrument.** The relation is defined for
   the Wood–Anderson response, and this synthetic channel has a flat velocity
   response.
2. **No site term.** The relation absorbs a station correction into its constants
   for a specific network; this record has no station.
3. **A velocity-to-displacement conversion assumes a single frequency.** A real
   broadband signal has no single $T$.

The honest reporting of this record is
$\log_{10}(\mathrm{PGV}/1\ \mathrm{\mu m\,s^{-1}}) = 0.252$ with the unit and the
period attached, plus the statement that a magnitude needs the calibration that
was not measured.

---

## ★★★7 — A pick-error budget for the S arrival

| Source | Size | Routed to | Justification |
|---|---|---|---|
| Sampling quantisation | $1/f_s = 0.010\ \mathrm{s}$ → $0.082\ \mathrm{km}$ | distance | a pick cannot be better than one sample |
| Detector bias (STA/LTA) | $-0.28\ \mathrm{s}$ → $-2.29\ \mathrm{km}$ | distance | measured against the known arrival |
| Clock error | $0.005\ \mathrm{s}$ → $0.041\ \mathrm{km}$ | distance | typical GPS-disciplined station clock |
| Orientation / projection | $0.05\ \mathrm{s}$ → $0.41\ \mathrm{km}$ | distance | a few degrees of off-vertical on a three-component sensor |
| Velocity-model error | $\pm1.2\%$ in $V_s$ → $\pm2.8\%$ in $D$ = $\pm1.33\ \mathrm{km}$ | distance | §6 of the lesson |

**Combination** (in quadrature, treating them as independent):

$$\sigma_D = \sqrt{0.082^{2} + 2.29^{2} + 0.041^{2} + 0.41^{2} + 1.33^{2}}
= \sqrt{0.0067 + 5.244 + 0.0017 + 0.168 + 1.769} = \sqrt{7.19}
= 2.68\ \mathrm{km}.$$

**Dominant term.** The detector bias, at $2.29\ \mathrm{km}$, contributes
$73\%$ of the variance. The velocity-model term is second at $25\%$; the
sampling and clock terms together contribute under $0.2\%$ and are irrelevant
at this precision.

**What removes the dominant term.** Not a better clock and not a finer sampling
rate, but a **second station**: two picks at different distances give a
location in which the *relative* travel times, not the absolute detector bias,
control the answer — the common bias largely cancels. Failing that, a matched
filter or a higher-order (AIC, higher-order statistics) picker replaces the
systematic early bias with a smaller, differently-signed one. And the
velocity-model term is removed only by using the observed travel times
themselves, which is the inversion of
[25-02-01](../../02-intermediate-projects/01-travel-time-curves.md).
