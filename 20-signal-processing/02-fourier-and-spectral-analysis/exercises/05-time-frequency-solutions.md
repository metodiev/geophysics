# Solutions — 20-02-05 Time-Frequency Analysis: STFT, Wavelets, Spectrograms

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [05 Time-Frequency Analysis](../05-time-frequency.md).

---

## ★1 — The STFT and the spectrogram

$$\mathrm{STFT}\{x\}(t,f) = \int x(\tau)w(\tau - t)e^{-i2\pi f\tau}\,\mathrm d\tau,
\qquad S(t,f) = \lvert\mathrm{STFT}\{x\}(t,f)\rvert^{2}.$$

- The **time axis** is the window's centre: each column is the spectrum of the
  signal seen through a window of duration set by $w$, so a feature is localised
  in time only to the window's width.
- The **frequency axis** is the transform variable within that window: each row is
  the power in a band whose width is the window's bandwidth, so a frequency is
  localised only to that bandwidth.

Both resolutions are properties of the window and cannot be chosen independently.

---

## ★2 — The uncertainty relation

$$\sigma_t\,\sigma_\omega \ge \frac12,
\qquad
\sigma_t\,\sigma_f \ge \frac{1}{4\pi} = 0.079577\ \mathrm{s\,Hz},$$

where $\sigma_t$ and $\sigma_f$ are energy-RMS widths and $\omega = 2\pi f$. The
factor between the two forms is exactly $2\pi$, and getting it wrong is the most
common error in quoting the bound.

**Attained by:** a Gaussian window, and only by a Gaussian — the equality case of
the Cauchy–Schwarz argument behind the proof. Measured in the lesson: the Gaussian
product is $0.0796$ at every window length (ratio $1.000$ to the bound), while the
Hann window gives $0.081665$, i.e. $1.0262\times$ the bound.

---

## ★3 — A 512-sample Hann spectrogram at $f_s = 2000\ \mathrm{Hz}$

**(a) Bin spacing.**

$$\Delta f = \frac{f_s}{N_{\text{seg}}} = \frac{2000}{512} = 3.90625\ \mathrm{Hz}.$$

**(b) $-3\ \mathrm{dB}$ two-tone resolution.** The measured rule is $2.4$ bins for
Hann:

$$2.4\times3.90625 = 9.375\ \mathrm{Hz}.$$

**(c) Energy-RMS time width.** Measured coefficient for Hann: $\sigma_t =
0.141\,N_{\text{seg}}\Delta t$:

$$\sigma_t = 0.141\times\frac{512}{2000} = 0.036096\ \mathrm{s} = 36.1\ \mathrm{ms}.$$

**Cross-check with the bound.** $\sigma_f = 0.081665/0.036096 = 2.262\ \mathrm{Hz}$,
so the *resolution* is $9.375/2.262 = 4.14$ times the RMS bandwidth. The two are
different quantities — a resolution is a dip criterion, a bandwidth is a second
moment — and quoting one where the other is meant over-states or under-states by
roughly a factor of 4. State which you are reporting.

---

## ★4 — Minimum segment length for a 4 Hz separation

The criterion is

$$2.4\,\frac{f_s}{N_{\text{seg}}} \le 4\ \mathrm{Hz}
\;\Longrightarrow\;
N_{\text{seg}} \ge \frac{2.4\times1000}{4} = 600\ \text{samples}.$$

**Cost in time localisation.** $\sigma_t = 0.141\times600/1000 = 84.6\
\mathrm{ms}$: a transient is localised to about $85\ \mathrm{ms}$, and the first and
last half-window ($\approx 300\ \mathrm{ms}$) of the record carry edge artefacts.
So resolving two components $4\ \mathrm{Hz}$ apart costs the ability to timestamp
anything to better than about a tenth of a second — and this is a *hard* trade, not
a matter of tuning, because the two numbers are the two ends of the product
measured in Section 2 of the lesson.

**If both are needed:** a multi-resolution (constant-Q) analysis uses a short window
at high frequency (where the components are far apart in relative terms) and a long
one at low frequency; the requirement then has to be restated as a *relative*
frequency resolution
([20-02-06](../06-wavelet-analysis.md)).

---

## ★5 — Uncertainty on a ridge slope

**Two-endpoint argument.** The frequency error of each ridge point is about one bin,
$\Delta f = f_s/N_{\text{seg}} = 1000/256 = 3.906\ \mathrm{Hz}$, and the time stamp
of each endpoint is uncertain by about $\sigma_t = 0.141\times256/1000 = 36.1\
\mathrm{ms}$. Combining the two endpoints of a $0.4\ \mathrm{s}$ baseline:

$$\delta\left(\frac{\mathrm df}{\mathrm dt}\right)
\approx \sqrt{2}\,\frac{\Delta f}{\Delta t}
= 1.414\times\frac{3.906}{0.4} = 13.8\ \mathrm{Hz\,s^{-1}},$$

so the measured $20\ \mathrm{Hz\,s^{-1}}$ has a $69\%$ relative uncertainty. The
number "20" without the error bar is not a measurement.

**Two ways to reduce it.**

1. **Fit over the whole ridge, not two endpoints.** Using a baseline of
   $2.0\ \mathrm{s}$ instead of $0.4\ \mathrm{s}$ (for a synthetic chirp spanning
   the record) reduces the slope uncertainty to $1.414\times3.906/2.0 = 2.75\
   \mathrm{Hz\,s^{-1}}$, a factor of $5$ — and the factor is exactly the ratio of
   baselines, so state the baseline.
2. **Lengthen the window** — but only if the signal stays locally stationary over
   it. Doubling $N_{\text{seg}}$ halves $\Delta f$ and doubles the baseline
   available for a *fitted* model, so the slope uncertainty can fall by up to
   $2\sqrt2$; the cost is that the ridge is no longer a local measurement, and a
   curved (dispersive) ridge is then mis-fitted by a straight line. Report the
   residual of the fit, not just the slope.

---

## ★6 — What "summing a spectrogram over time" gives

For an STFT with window $w$,

$$\int S(t,f)\,\mathrm dt
= \lvert X(f)\rvert^{2} * \lvert W(f)\rvert^{2},$$

i.e. the *full-record power spectrum convolved with the window's power spectrum*.
So the colleague has computed **a smoothed power spectrum**, not the power
spectrum. Two consequences:

1. **The resolution is the window's, not the record's.** With $N_{\text{seg}} =
   256$ at $f_s = 1000\ \mathrm{Hz}$, the smoothing kernel has an energy-RMS width
   of $2.262\ \mathrm{Hz}$ (Section ★3's cross-check) and a $-3\ \mathrm{dB}$
   two-tone resolution equivalent of $2.4\times3.906 = 9.4\ \mathrm{Hz}$. The full
   8192-sample record, by contrast, has $\Delta f = 0.122\ \mathrm{Hz}$, so the
   marginal is about $77$ times coarser in bin spacing than the transform of the
   whole record — and its *resolution* is worse by the same order.
2. **The level is biased for a spectrum with structure.** Convolution with the
   window's kernel lowers resolved peaks and fills nulls; for a red spectrum the
   low-frequency end is additionally affected by the one-sided DC convention
   ([20-02-02 §3](../02-spectral-estimation.md)).

**The correct summary** of a spectrogram over time, if an average spectrum is
wanted, is either (a) the full-record Welch or multitaper estimate with its own
stated resolution and dof, or (b) the *average of the per-frame PSDs* with the
window's kernel explicitly stated as the resolution, and its ENBW reported
([20-02-03](../03-windowing-advanced.md)). Both are defensible; "the power spectrum"
as a bare label is not.

---

## ★7 — Dispersive train at 0.3–3 Hz: can one window do it?

**Requirements.** $f_s = 20\ \mathrm{Hz}$ (Nyquist 10 Hz, so the band 0.3–3 Hz is
comfortably inside). Group velocity to $2\%$ and arrival time to $50\ \mathrm{ms}$.

**Time requirement.** A $50\ \mathrm{ms}$ arrival-time accuracy is far finer than
any window appropriate to $0.3\ \mathrm{Hz}$: with Hann,
$\sigma_t = 0.141 N_{\text{seg}}\Delta t$, so $50\ \mathrm{ms}$ forces
$N_{\text{seg}} \le 0.05/0.141\times20 = 7$ samples — which cannot represent a
$0.3\ \mathrm{Hz}$ component at all (a $0.3\ \mathrm{Hz}$ period is $67$ samples).
So the "arrival time to $50\ \mathrm{ms}$" requirement cannot be about the
*wavelet* arrival through a spectrogram; it must be a *pick* on the onset, which is
a different estimator (Section 5 of the lesson and ★★★8 of
[20-01-02](../../01-signals-and-systems/exercises/02-lti-systems-solutions.md)).

**Frequency requirement at the low end.** To measure a group velocity to $2\%$ at
$0.3\ \mathrm{Hz}$ you need the frequency to about $0.006\ \mathrm{Hz}$, i.e. a
window of at least $2.4/(0.006\times20) = 20\,000$ samples ($1000\ \mathrm{s}$) for
a Hann window's $-3\ \mathrm{dB}$ criterion. That is a long window, and it is
legitimate here because a $0.3\ \mathrm{Hz}$ wave is nearly stationary over
$1000\ \mathrm{s}$.

**At the high end.** The same *relative* accuracy at $3\ \mathrm{Hz}$ needs
$0.06\ \mathrm{Hz}$, i.e. at least $2000$ samples ($100$ s) — a window $10\times$
shorter.

**Verdict.** A single window cannot serve both ends: $20\,000$ samples at
$3\ \mathrm{Hz}$ would smear the whole arrival into one bin (the arrival's
duration is likely much shorter than $1000\ \mathrm{s}$), while $2000$ samples at
$0.3\ \mathrm{Hz}$ is only $30$ periods — usable but marginal. **A
constant-Q/multi-resolution analysis is the right tool**, with the scale factor
between the shortest and longest windows set by the band ratio
$3/0.3 = 10$: a factor of 10 in window length covers both ends at constant
*relative* resolution. That is precisely the design of the wavelet transform in the
next lesson, and the number to quote is the factor $Q = f/\Delta f$, constant
across the band.

**The honest caveat.** Group velocity derived from a time-frequency ridge is a
ridge-motion measurement, and dispersion within the window biases it. Report the
group delay at each frequency with the window's $\sigma_t$ as the resolution, and
check that halving the window changes the answer by less than the stated
uncertainty.

---

## ★8 — Detecting a $5\%$ excess in the time-bandwidth product

**Target.** Distinguish a window with $\sigma_t\sigma_f = 1.05/(4\pi) = 0.083556$
from one attaining the bound, $0.079577$ — a difference of $0.003979\ \mathrm{s\,Hz}$.

**Statistic.** Measure $\sigma_t$ from the window's own second moment and
$\sigma_f$ from the second moment of its squared transform:

$$\sigma_t = \sqrt{\frac{\sum_n (n-\bar n)^{2}w^{2}[n]}{\sum_n w^{2}[n]}}\,\Delta t,
\qquad
\sigma_f = \sqrt{\frac{\int(f-\bar f)^{2}\lvert W(f)\rvert^{2}\mathrm df}
{\int\lvert W(f)\rvert^{2}\mathrm df}} .$$

**Precision required.** A $5\%$ error in the product can come from a $2.5\%$ error
in each width (they enter as a product), which means each width must be measured to
about $2.5\%$ — i.e. the discretisation must not disturb the second moments by more
than a few parts in a hundred.

**Discretisation effects that masquerade as an excess.**

1. **Truncation of the window.** A Gaussian truncated at $\pm k\sigma$ loses tails
   and *reduces* $\sigma_t$; at $\pm4\sigma$ the missing energy is
   $2\Phi(-4) \approx 6.3\times10^{-5}$ of the total, so the second-moment error is
   of order $10^{-4}$ relative — negligible. At $\pm2\sigma$, however, $4.6\%$ of
   the energy is missing and the error is of order several per cent: **the first
   control is to state the truncation and keep it at $\pm4\sigma$ or wider.**
2. **Coarse sampling of the time axis.** If the window has only a few samples per
   standard deviation, the discrete second moment is quantised: with $m$ samples
   per $\sigma$, the error in $\sigma_t$ is of order $1/(12m^{2})$ relative plus
   the effect of the trapezoidal approximation to the integral. The lesson's
   measurement used $8$ samples per $\sigma$ ($N_{\text{seg}}/8$), which is enough;
   at $2$ samples per $\sigma$ the discretisation error is of order $1\%$–$2\%$ and
   would look like part of the effect.
3. **The frequency grid.** $\sigma_f$ is computed on a grid that must extend well
   beyond the spectral tails and be fine enough to resolve them: an under-resolved
   grid truncates the tails and biases $\sigma_f$ low, exactly as (1) does in time.
   Use at least $8$ samples per $\sigma_f$ and a range of $\pm6\sigma_f$.
4. **Normalisation.** A window that is not normalised (or is normalised
   differently) affects $\bar f$ and hence $\sigma_f$ if the window has a non-zero
   mean; remove the mean or verify that the second moment is invariant under it.

**Which control fails for a poorly sampled window.** The time-axis control: with
few samples per $\sigma$ the discrete $\sigma_t$ is itself a coarse approximation,
so an apparent $5\%$ excess cannot be distinguished from sampling error. The test
is to *upsample the window analytically* (evaluate the same functional form on a
finer grid) and recompute — if the product moves by more than $1\%$, the
discretisation, not the window, is what was measured. Report the product for two
grid densities; a genuine excess is stable under that change, and then the
comparison against $1/(4\pi)$ is a statement about the window.


---

## Mastery checkpoint answers

**(c)** $N_{\text{seg}} = 512$, $f_s = 2000\ \mathrm{Hz}$:
$\Delta f = 3.90625\ \mathrm{Hz}$; the measured two-tone resolution is
$2.4$ bins $= 9.375\ \mathrm{Hz}$; the energy-RMS time width is
$\sigma_t = 0.141\times512/2000 = 36.1\ \mathrm{ms}$.

**(d)** $2.4\,f_s/N_{\text{seg}} \le 4\ \mathrm{Hz}$ gives
$N_{\text{seg}} \ge 2.4\times1000/4 = 600$ samples.

**(f)** *Right tool:* a mono-component chirp, where the analytic signal gave an rms
frequency error of $0.135\ \mathrm{Hz}$ against $1.157\ \mathrm{Hz}$ for the
STFT ridge with a 256-sample window — a factor $8.6$ better, because there is
exactly one component for the phase derivative to describe. *Wrong tool:* two
simultaneous components, where the analytic signal's phase is the vector sum of
the two and the "instantaneous frequency" swings between them; there the
spectrogram's separability (measured resolution $9.5\ \mathrm{Hz}$ at that window
length) is the quantity that matters.
