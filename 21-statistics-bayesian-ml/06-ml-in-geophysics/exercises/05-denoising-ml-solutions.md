# Solutions — 21-06-05 ML-Based Denoising of Geophysical Signals

> Read after attempting. Lesson:
> [05 Denoising](../05-denoising-ml.md). Decibels are **SYNTHETIC** values
> printed by [`code/denoising_ml_demo.py`](../code/denoising_ml_demo.py).

---

## ★1 — Change in SNR, and the error-energy factor

Subtract the input SNR from each output SNR:

| method | noise 0.3 | noise 0.6 |
|---|---|---|
| BP 30 Hz | $2.45 - 10.18 = -7.73$ dB | $1.92 - 4.15 = -2.23$ dB |
| BP 40 Hz | $-4.01$ dB | $+0.57$ dB |
| BP 60 Hz | $+2.54$ dB | $+3.02$ dB |
| BP 80 Hz | $+1.96$ dB | $+1.92$ dB |
| learned dictionary | $+1.89$ dB | $+1.81$ dB |

For the 30 Hz band-pass at noise 0.3, $\Delta\mathrm{SNR} = -7.73$ dB means the
error energy grew by

$$\frac{E_{\text{after}}}{E_{\text{before}}} = 10^{7.73/10} = 5.9 .$$

Processing made the trace **5.9 times worse in error energy** than not processing
it, while the SNR "improvement" column of a naive report would have been +2.45 dB
against a nominal input of 0 dB. This is the single most useful number in the
lesson: a filter that is not tuned is not a neutral baseline.

---

## ★2 — Predicting the band-pass result from energy fractions

Let $\sigma_s^2$ be the clean signal power and $r = 0.3$ the noise ratio, so
$\sigma_n^2 = r^2\sigma_s^2 = 0.09\,\sigma_s^2$. The band-pass error is

$$E = \underbrace{(1 - g_s)\,\sigma_s^2}_{\text{signal deleted}}
+ \underbrace{g_n\,\sigma_n^2}_{\text{noise kept}},$$

where $g_s$ is the retained signal fraction and $g_n = f/f_N$ for white noise.

**40 Hz:** $g_s = 0.797$, $g_n = 40/125 = 0.320$:

$$E = 0.203\,\sigma_s^2 + 0.320\times0.09\,\sigma_s^2 = 0.2318\,\sigma_s^2,
\qquad \mathrm{SNR} = 10\log_{10}\frac{1}{0.2318} = +6.35\ \text{dB},$$

against the measured $+6.17$ dB.

**60 Hz:** $g_s = 0.993$, $g_n = 60/125 = 0.480$:

$$E = 0.007\,\sigma_s^2 + 0.480\times0.09\,\sigma_s^2 = 0.0502\,\sigma_s^2,
\qquad \mathrm{SNR} = +12.99\ \text{dB},$$

against the measured $+12.72$ dB.

The residual $0.2$–$0.3$ dB is the difference between the ensemble-average energy
fractions quoted here (measured over 20 traces) and the per-realisation values,
plus the finite-record effect of a rectangular frequency cut (spectral leakage
spreads a little noise back into the pass band and takes a little signal out).
The mechanism is confirmed: **a band-pass improves the SNR only when the signal
fraction it keeps exceeds the noise fraction it keeps**, and at a corner near the
wavelet's own frequency it does not.

---

## ★3 — Mean and spread across noise levels

Learned dictionary: mean $= (12.07 + 5.96)/2 = +9.02$ dB, spread
$12.07 - 5.96 = 6.11$ dB.
Best band-pass (60 Hz): mean $= (12.72 + 7.17)/2 = +9.95$ dB, spread
$12.72 - 7.17 = 5.55$ dB.

The band-pass has both the higher mean and the smaller spread. The lesson is not
that filters win; it is that the noise level sets the answer, and a single-level
comparison is a statement about that level. A denoising claim needs the curve of
SNR improvement against input SNR, with the filter's parameter tuned at each
level.

---

## ★4 — What a rank-16 projector should deliver

If the dictionary were an orthonormal basis of rank $K = 16$ on patches of length
$L = 32$, and if it captured the signal exactly, the projection would keep the
signal and retain only the fraction $K/L$ of white-noise variance:

$$E = 0 + \frac{16}{32}\times0.09\,\sigma_s^2 = 0.045\,\sigma_s^2,
\qquad \mathrm{SNR} = 10\log_{10}\frac{1}{0.045} = +13.47\ \text{dB}.$$

The measured value is $+12.07$ dB, $1.4$ dB lower. Three mechanisms account for
it:

1. **The dictionary is not an exact rank-16 basis of the signal space.** The
   residual $0.000181$ of signal variance is not located in the discarded
   dimensions only, so a small part of the deleted energy is signal.
2. **The ridge penalty.** $\lambda = 10^{-3}$ shrinks the coefficients, which
   biases the reconstruction towards zero and removes a little more signal than
   the pure projector would.
3. **Patches overlap with stride 8 and are Hann-tapered.** Overlap–add changes the
   effective rank of the operator applied to the trace: a sample is reconstructed
   from several overlapping patch projections, so the noise reduction in the
   sample domain is not exactly $K/L$, and the taper weights the edges of each
   patch less.

The order of magnitude is right, which is the point: **the noise reduction of a
dictionary denoiser is set by its rank relative to the patch dimension**, and the
signal loss is what the training distribution buys or costs.

---

## ★★★5 — The mismatch sweep

**Design.** Train five dictionaries, one per training wavelet frequency
$f_{\text{tr}} \in \{20, 25, 30, 35, 40\}$ Hz, from 200 clean training traces each,
and apply all five to the same 40 clean test traces built from 30 Hz wavelets at
the same two noise ratios. Nothing else changes: same patch length and stride,
same rank, same ridge, same seeds.

**Metric.** Mean SNR over the 40 test traces for each $(f_{\text{tr}}, r)$ pair,
reported together with the *matched* value ($f_{\text{tr}} = 30$ Hz) as the
reference, and hence the penalty $\Delta(f_{\text{tr}}) = \mathrm{SNR}_{\text{matched}}
- \mathrm{SNR}(f_{\text{tr}})$.

**Plot.** $\Delta$ against $|f_{\text{tr}} - 30|$ Hz, one curve per noise level.
Predicted shape: a minimum at zero mismatch, rising monotonically with
$|f_{\text{tr}} - 30|$, with a steeper rise for *lower* frequencies than higher
ones because a 20 Hz dictionary spans a narrower band and therefore misses more
of the 30 Hz wavelet than a 40 Hz dictionary does.

**The single number to quote.** The penalty at the largest plausible mismatch,
$\Delta(20\ \text{Hz})$ — here $1.61$ dB at noise 0.3 — because it is the
worst-case number that a reader applying the method to a different area needs.
A sweep that reports only the matched case is not a robustness statement.

---

## ★★6 — Two sources of sampling error in the mean SNR

1. **Across traces.** The 40 test traces have different reflectivity
   realisations, so each has its own SNR; the mean has standard error
   $\mathrm{sd}/\sqrt{40}$. This is the ordinary trace-to-trace error.
2. **Across patches within a trace.** Each trace contributes
   $(1000 - 32)/8 + 1 = 122$ patches, but consecutive patches overlap by 24 of 32
   samples, so they share most of their samples and their noise. The effective
   number of independent patches is roughly the trace length divided by the patch
   length, $1000/32 \approx 31$, not 122 — a factor of about $4$ fewer.

**Resampling unit.** A bootstrap over the *40 traces* (resample traces with
replacement, recompute the mean SNR) captures source 1 and, because each resample
carries all of that trace's correlated patches, it also carries source 2 into the
spread. A bootstrap that resampled *patches* would understate the error by
roughly $\sqrt{4} = 2$: it would treat overlapping patches as independent
observations of the same trace's noise. The rule is the usual one: resample the
unit that was independently drawn — the trace, or the event or station above
it — not the derived, overlapping sub-units.

---

## ★★★7 — Does the denoiser help the picker?

**Design.** Two denoisers (the tuned 60 Hz band-pass and the learned dictionary),
one noise level (or a sweep of two), and one picker applied identically to each
input: the raw trace, the band-passed trace and the dictionary-denoised trace.
Everything else — records, seeds, picker, thresholds — is held fixed so that the
comparison is paired per record.

**Metric pair.** (i) SNR in dB, to show what the denoiser did to the waveform;
(ii) pick bias and pick MAE in samples (or seconds), plus the fraction inside the
tolerance the downstream task needs, per
[21-06-02](./02-phase-picking-ml-solutions.md).

**Control.** The *matched* denoiser applied to *matched* data, plus an
inverse-filter or pure-noise null: denoise a trace whose signal has been set to
zero and confirm that the picker finds nothing.

**Sizing.** Paired over records; to resolve a pick-MAE change of 0.05 s with a
per-record difference scatter of 0.30 s you need
$n \ge (0.30/(0.05/3))^2 = 324$ records. Quote the paired interval, not two
independent intervals.

**The result pattern that condemns the denoiser.** SNR improves (step (i)
positive) while the pick bias moves *and the MAE outside the tolerance grows* —
that is, the denoiser removed noise at the cost of a wavelet distortion that
displaces the onset. A denoiser that shifts the pick is worse than no denoiser
for every downstream consumer, however flattering its decibel.

---

## ★★★8 — Substitutes for the clean reference

1. **Repeat shots or repeat passes.** Two acquisitions over the same target with
   independent noise. *Can* establish noise suppression and stability; *cannot*
   establish signal fidelity, because the underlying signal is unknown and both
   repeats may share the same systematic error. Acceptable for noise claims only.
2. **Synthetic truth inserted into a real noise field.** Add a modelled (or
   well-log-derived) reflection response to recorded noise. *Can* establish bias
   and amplitude fidelity, because the truth is known; *cannot* establish
   behaviour on real signal that the model does not represent, and the answer
   depends on the model chosen — so the model and its provenance must be
   reported.
3. **Cross-validation against an independent measurement** (a well log, another
   survey with different resolution, or an inversion of a different data type).
   *Can* establish that the processed data agree with independent information at
   the scale the independent measurement resolves; *cannot* establish fidelity at
   scales finer than that.

**For an amplitude-fidelity claim** I would accept **(2)**: it is the only
substitute in which the true amplitude of each reflection is known, so the
question "did the denoiser change relative amplitudes?" is answerable rather than
inferred. Repeat shots answer a noise question, and independent measurements
answer a scale-limited consistency question; neither pins an amplitude ratio.

---

## ★★★9 — Detecting amplitude distortion

**Metric.** Per-reflection amplitude ratio
$\rho_i = A_i^{\text{out}} / A_i^{\text{in}}$ measured on the *clean* synthetic
contribution, with the truth known. Report the denominator-normalised distortion
$D = \mathrm{sd}(\rho_i)$ (a scale-free measure of whether different reflections
are treated differently), together with the mean $\bar\rho$ (a bulk amplitude
bias) and the amplitude-versus-offset gradient of $\rho$: a denoiser that
compresses strong reflections more than weak ones turns an AVP trend into a
flatter one, which is the failure that matters for reservoir work.

**Synthetic truth needed.** Reflections whose amplitudes span the range of
interest, placed on the same grid as the noise, with a known amplitude trend in
the offset direction. The model must be stated, because the measured distortion
is a property of the pair (denoiser, reflection ensemble).

**Confound with noise removal.** Any measurement of $\rho_i$ on a *noisy* trace is
contaminated by the noise's own contribution to the peak amplitude, which biases
$\rho_i$ towards 1 as the noise rises. The experiment must therefore separate the
two: (i) apply the denoiser to the clean trace alone — the pure distortion,
independent of noise; (ii) apply it to clean + noise and report the difference,
which is the noise-removal part. A claim about amplitude fidelity is only
meaningful when the two are reported separately.

**Sizing.** Each reflection contributes one $\rho_i$; with $n$ reflections the
standard error of $D$ is approximately
$D/\sqrt{2(n-1)}$. To resolve a distortion of $D = 0.05$ with a $3\sigma$ margin
you need $n \ge 1 + 2(0.05/0.0167)^2 \approx 19$ reflections per amplitude bin —
and the bins matter, because the whole question is whether $\rho$ depends on
amplitude. Size each bin, not the pooled set.
