# Solutions — 03-03-05 scipy.signal: Filters, Windows and Spectral Estimation

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked *measured* come from running a
> modified copy, with the modification stated.

---

## ★1 — The Ricker wavelet

**(a)** $w(0) = (1-0)e^{0} = 1$.

**(b)** $1 - 2\pi^2f^2t^2 = 0 \Rightarrow t = \pm 1/(\pi f\sqrt2)$. For
$f = 32$ Hz: $t = \pm1/(\pi\times32\times1.4142) = \pm7.03$ ms, i.e. $\pm3.52$
samples at $2$ ms sampling. The main lobe is therefore about 14 ms wide, or
7 samples.

**(c)** $\int_{-\infty}^{\infty}w\,dt = 0$ because the Ricker wavelet is the
second derivative of a Gaussian, and the integral of any derivative of a
decaying function over the whole line is zero. The consequence is that
convolving with it preserves the mean level of the data — no DC is introduced
and a trace's baseline is unchanged. This is why a zero-mean wavelet is
required for any processing that assumes the seismic trace has no DC.

**(d)** The demo's column is `trace[i] / np.abs(clean).max()`, i.e. normalised by
the *largest value anywhere in the trace*, not by the reflectivity. Adjacent
reflectors interfere: the 0.250 s and 0.412 s picks are 0.162 s apart, only
$5.2$ main-lobe widths, so their wavelets overlap and the leading lobe at
0.250 s carries a contribution from the following reflector. The quotient is
therefore a mixture, whereas the reflectivity itself is exactly 0.80. The
lesson: a trace *amplitude* is a reflectivity only after the wavelet's overlap
has been handled, which is deconvolution.

---

## ★2 — Verifying a Butterworth specification

**(a)** In the bilinear transform the digital frequency $f$ maps to
$\Omega = \tan(\pi f/f_s)$, so a ratio of digital frequencies becomes a ratio of
tangents:
$\tan(\pi\times100/500)/\tan(\pi\times40/500) = \tan(0.6283)/\tan(0.2513) =
0.72654/0.25676 = 2.829$.

**(b)** $|H|^2 = 1/(1 + 2.829^{8})$; $2.829^8 = 4.103\times10^{3}$, so
$|H| = 1/\sqrt{4104} = 1.561\times10^{-2}$ and
$20\log_{10}|H| = -36.13$ dB, matching the tabulated $-36.14$ dB.

**(c)** For $N = 2$: $2.829^4 = 64.05$, so $|H| = 1/\sqrt{65.05} = 0.1240$ and
$-18.13$ dB, matching the tabulated $-18.14$ dB.

**(d)** The unwarped prediction $20N\log_{10}(100/40)$ uses the ratio
$2.5$ instead of $2.829$: $20\times4\times\log_{10}(2.5) = 31.84$ dB against the
measured $36.14$. The bilinear transform pre-warps the frequency axis so that
the specified cut-off lands exactly on $-3$ dB, at the price of a *steeper*
stopband than the analogue prototype predicts when the digital frequencies are
compared by ratio rather than by tangent. Any digital filter design done in the
$z$ domain has this property, and it is why a specification is verified against
`sosfreqz` rather than against the analogue formula.

---

## ★3 — Group delay

**(a)** $15.344\ \mathrm{ms} \times 500\ \mathrm{Hz} = 7.67$ samples.

**(b)** Because the trace is broadband. The cross-correlation measures the delay
of the *dominant* energy, which sits near the Ricker's 32 Hz where the group
delay is 15.3 ms, but the trace also has energy at 5–10 Hz where the delay is
10.2–10.5 ms. The measured 12.00 ms is an amplitude-weighted average over the
signal's spectrum, which is why a cross-correlation lag must always be quoted
with the spectrum it was measured on.

**(c)** The delay in *seconds* is essentially unchanged. The phase response of
a digital Butterworth design with `fs=1000` approximates the same analogue
40 Hz prototype, whose group delay at low frequency is
$2.613/(2\pi f_c) = 10.4$ ms — the analogue value, independent of $f_s$. What
changes is the delay expressed in *samples*, which halves (7.67 → 3.83) because
each sample is half as long. The check is `sosfreqz` at 5 Hz for both designs.

**(d)** The delay must be known to a fraction $0.5/12\,000 = 4\times10^{-5}$,
i.e. 0.004% — or, equivalently, the delay must be *removed* using the measured
phase response of the actual instrument filter rather than assumed from the
nominal cut-off. A 4% error in the delay (0.5 ms) is exactly the pick
precision, so an assumed delay is not good enough.

---

## ★4 — Windows

**(a)** $10^{-13.26/20} = 0.2172$. A tone's leakage sidelobe is 21.7% of the
tone's amplitude, which is why a boxcar-windowed spectrum of a strong reflection
shows sidelobes across the whole record.

**(b)** Boxcar: $(1 - 0.645881) = 35.4\%$ low. Hann: $(1 - 0.848835) = 15.1\%$
low. (Hamming 18.1%, Blackman 11.9%.) Note that these are the *worst-case*
off-bin errors; on a bin every window is exact.

**(c)** A window with low scalloping and a mainlobe narrow enough to separate the
tidal constituents being studied. Blackman (1.099 dB worst-case, 11.9%) or a
flat-topped window; Hann (1.424 dB, 15.1%) is marginal for a 1% amplitude
specification. If the constituent frequencies are known, the better answer is
to *fit* the tidal harmonics in the time domain by least squares, which avoids
the windowing trade entirely — this is how tidal analysis is normally done.

**(d)** The mainlobe is set by the window's *length* and its smoothness at the
edges; both Hann and Hamming taper to small but nonzero values (Hamming ends at
0.08, Hann at 0), which gives the same 4-bin null-to-null width. The sidelobes
are set by how *smooth* the taper is across its interior and at the ends: the
Hamming window is designed by choosing the coefficients that cancel the first
sidelobe, at the cost of a slower falloff of the far sidelobes (about
$-20$ dB/decade against Hann's $-60$).

---

## ★5 — Causality and look-ahead

**(a)** Because a causal filter's output at time $t$ is a finite summation over
$x(t')$ with $t' \le t$ — the recursion never references a later sample, so
filtering a truncated record gives *bit-identical* results for the samples that
both runs share. The difference is not small, it is zero.

**(b)** $153$ samples $= 153/500 = 0.306$ s $= 6.1$ periods of a 20 Hz
sinusoid: the backward pass needs about six cycles of the cut-off frequency to
settle.

**(c)** The look-ahead scales roughly inversely with the cut-off, because a
lower cut-off means a longer impulse response. *Measured* with an independent
noise realisation and the same 1.0 s truncation, using the on-line threshold
$10^{-9}$:

| $f_c$ (Hz) | look-ahead (samples) | $\tau_g$ at 32 Hz (ms) |
|---|---|---|
| 40 | 77 | 15.34 |
| 20 | 137 (demo: 153) | 10.34 |
| 10 | 305 | 4.30 |
| 5 | $\ge 500$ (the whole shared record) | 2.08 |

The absolute counts depend on the noise realisation and on the threshold, so the
demo's 153 and the table's 137 at 20 Hz are the same measurement to within that
sensitivity. **The trend is the result**: the look-ahead grows from 0.15 s at
40 Hz to 0.61 s at 10 Hz, and at 5 Hz the filter's transient is longer than the
segment being compared.

**(d)** No — not with `sosfiltfilt`. A fourth-order 0.5 Hz low-pass has a
group delay at zero frequency of $2.613/(2\pi\times0.5) = 0.83$ s, and the
forward–backward scheme needs of order twice that of *look-ahead* (the backward
pass must settle over the same impulse response), so about 1.7 s at minimum and
more for the low-frequency content of a teleseismic P arrival. Extrapolating the
measured $1/f_c$ trend from 0.61 s at 10 Hz gives several seconds at 0.5 Hz —
longer than the 3 s budget and longer than the P coda. A causal filter with a
known, small group delay is the only admissible choice, and if 0.5 Hz is
required, the filter order must be reduced and the delay budgeted explicitly.

---

## ★6 — Parseval's theorem as a check

**(a)** $0.582609 - 0.565053 = 0.017556$ in the variance units of the record,
so the implied RMS discrepancy is $\sqrt{0.017556} = 0.1325$ — against a signal
RMS of $\sqrt{0.565053} = 0.7517$, i.e. 17.6% of the signal's RMS, or 3.1% of
the variance.

**(b)** Welch's estimator averages the periodograms of overlapping windowed
segments. For a stationary signal the segments are all draws from the same
distribution and the average is a consistent estimate whose normalisation is
exact in expectation. For a chirp the *spectrum changes within each segment*:
the windowed segment contains a swept signal whose leakage pattern is not that
of a stationary process, and the ensemble average over segments is a differently
weighted object. The residual is the price of applying a stationarity assumption
to a non-stationary record.

**(c)** `scaling='spectrum'` returns the power in each bin, whose sum is the
variance; `scaling='density'` (the default) returns power *per hertz*, whose
integral over frequency is the variance. Multiplying the density by the bin
width $df$ recovers the power, so `Pxx_spectrum.sum()` and
`Pxx_density.sum() * df` should agree. A factor of two rather than $df$ means
the one-sided/two-sided convention has been mixed: a two-sided density
integrates to the variance over $[-f_s/2, f_s/2]$, so a one-sided density
contains twice the power per bin except at DC and Nyquist.

**(d)** `abs(Pxx.sum() * df / np.var(x) - 1) < 0.05`, or simply printing the
ratio, as the demo does. The test catches a factor-of-two, a missing $df$, and
a wrong `scaling` in one line, and it costs nothing.

---

## ★7 — Designing a filter to specification

**(a)** From ★2(a) the warped ratio at 100 Hz is $r = 2.829$, and the digital
Butterworth magnitude is $|H|^2 = 1/(1+r^{2N})$, so the attenuation is
$10\log_{10}(1 + r^{2N}) = 10\log_{10}(1 + 2.829^{2N})$ dB. For large $N$ this
is $20N\log_{10}(2.829) = 9.03N$ dB.

**(b)** $9.03N \ge 60 \Rightarrow N \ge 6.64$, so **order 7** (the exact
expression gives $10\log_{10}(1+2.829^{14}) = 63.2$ dB, and order 6 gives
54.2 dB, which fails).

**(c)** `butter(7, 40.0, btype='low', fs=500, output='sos')` followed by
`sosfreqz` reports **−63.24 dB** at 100 Hz, meeting the specification with 3.2 dB
of margin. The group delay grows with order: *measured* at 32 Hz it is
**26.58 ms** against 15.34 ms for the fourth-order filter, a factor of 1.73,
because a steeper skirt requires a longer impulse response. (For reference the
measured attenuations at 100 Hz are −36.14, −54.21, −63.24 and −72.28 dB for
orders 4, 6, 7 and 8.) Note also that order 7 is odd, so the design has one
first-order section plus three biquads — with `output='sos'` this is handled
automatically, whereas a seventh-order transfer function in `b, a` form is
numerically fragile.

**(d)** A fifth-order elliptic filter reaches the same 60 dB with a much
narrower transition band, or reaches far more attenuation with the same
transition. It is preferable when the specification is a *narrow transition*
(e.g. 40 Hz passband and a 45 Hz stopband edge), because a Butterworth filter
would need a very high order. It is not preferable when the *passband must be
flat*: an elliptic filter has equiripple in the passband (typically 0.1–1 dB),
and it also has ripple in the stopband and a worse group-delay behaviour near
the cut-off. Quantitatively the same specification would be met by an elliptic
filter of order 3 with 0.1 dB passband ripple; the trade is the ripple for two
fewer poles.

---

## ★8 — Phase distortion and picks

**(a)** Zero-phase filtering is correct because the whole record is available:
there is no need to answer in real time, and the zero-phase result has no
delay to correct and no phase distortion to deconvolve. In a real-time system
it would be impossible: the backward pass requires future samples (measured in
★5: 77–305 samples, and far more at lower cut-offs), so the value at time $t$
cannot be produced at time $t$.

**(b)** $15.34 - 10.25 = 5.09$ ms of *differential* delay between 5 Hz and
40 Hz. It cannot be removed by a constant shift because the required shift
depends on frequency: shifting the whole trace by 12 ms would leave the 5 Hz
content 1.7 ms early and the 40 Hz content 3.3 ms late.

**(c)** The effect is a **frequency-dependent time shift**, which is *dispersion
of the wavelet*: a symmetric zero-phase wavelet becomes asymmetric and longer,
with the high-frequency content arriving before the low-frequency content (the
group delay is larger at higher frequency in this filter). In seismic terms the
wavelet is "chirped", and the peak of the envelope is no longer at the
reflector time.

**(d)** The reply: "The mean delay is 12 ms, which is inside your 20 ms
tolerance, but the *differential* delay across the passband is 5.09 ms, and that
is not a shift — it is a waveform distortion that no subsequent correction
removes. Your first break is picked at 0.5 ms, and at 5 Hz the filter will have
moved the arrival 10.25 ms while at 40 Hz it has moved it 15.34 ms, so the pick
must specify which frequency it is picking. The cheapest fix is a
zero-phase filter (this dataset is archived, not real-time) which reduces the
differential delay to zero; failing that, the constant-delay equivalent of
`sosfilt` with a full phase correction from the measured filter response."
