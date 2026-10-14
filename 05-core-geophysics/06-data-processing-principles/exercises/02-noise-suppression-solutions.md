# Solutions — 05-06-02 Noise Suppression: Stacking, Filtering, Median, KL Transform

> **Read this after attempting the exercises, not before.**

---

## ★1 — The stacking law

Write each trace as $d_i(t) = s(t) + n_i(t)$ with $\operatorname{E}[n_i] = 0$,
$\operatorname{Var}[n_i] = \sigma^{2}$, and $n_i$ independent. The stack is
$S = \frac1N\sum_i d_i = s + \frac1N\sum_i n_i$. The expectation is
$\operatorname{E}[S] = s + \frac1N\sum \operatorname{E}[n_i] = s$ (zero-mean noise);
the variance, using independence so that all covariance terms vanish, is

$$\operatorname{Var}[S] = \frac{1}{N^{2}}\sum_i \operatorname{Var}[n_i]
= \frac{N\sigma^{2}}{N^{2}} = \frac{\sigma^{2}}{N}
\ \Longrightarrow\ \sigma_S = \frac{\sigma}{\sqrt N}. \ \boxed{}$$

Assumptions used: (i) the signal is common to all traces; (ii) the noises are
independent and zero-mean; (iii) no single trace dominates.

---

## ★2 — Matching method to structure

| method | noise structure |
|---|---|
| stacking | independent noise between traces (and needs alignment) |
| median filtering | sparse, large outliers |
| band-pass filtering | noise outside the signal's band |
| KL (SVD) filtering | incoherent noise on a gather of coherent, energetic events |

---

## ★3 — Single-trace noise

$\sigma = \sigma_S\sqrt{N} = 0.05\times\sqrt{36} = \boxed{0.30\ \mathrm{mGal}}$.

---

## ★4 — The Tikhonov operator

$$\hat h_\lambda(k) = \frac{\hat w^{*}(k)}{\lvert\hat w(k)\rvert^{2}+\lambda^{2}}.$$

For $\lvert\hat w\rvert \gg \lambda$, $\hat h \approx 1/\hat w$ — the exact inverse.
For $\lvert\hat w\rvert \ll \lambda$, $\hat h \approx \hat w^{*}/\lambda^{2}$ — strong
attenuation, i.e. the regularisation *replaces* the unavailable information at that
frequency with zero rather than with amplified noise.

---

## ★5 — Ill-posedness

Because the wavelet's spectrum can be *exactly zero* at some frequencies — the
measured example has 62 of 257 bins below the double-precision floor — the
information at those frequencies was multiplied by zero in the convolution and is
irrecoverably absent; an inverse problem whose solution does not exist for all data
is ill-posed, not merely ill-conditioned.

---

## ★★6 — Measuring leakage against the gain

**(a)** The naive prediction is $\sigma \times \text{gain}
= 0.00189 \times 10.7210 = 0.02026$ mGal-equivalent.

**(b)** The **measured** leakage at $\lambda = 0.01$ is 0.013232 — a factor 0.65 of
that prediction. The discrepancy is real and instructive: leakage measures *two*
contributions — the amplified noise *and* the smearing of the true spikes into the
quiet zone — and only the first scales with the operator gain. Across the sweep the
measured ratio leakage/($\sigma\times$gain) ranges from 0.65 to 13.17; at small
$\lambda$ the amplified noise dominates (ratio ≈ 1), and at large $\lambda$ the noise
has gone and the leakage is almost entirely smeared signal.

**(c)** The gain reaches about 1 (no amplification) at $\lambda \approx 0.1$, where
the measured leakage is 0.004376 — about 2.3 times the data noise of 0.00189, with
the excess being the smeared-signal contribution. At that $\lambda$ the spike
recovery is 31.80 %, against 46.23 % at $\lambda = 0.001$. So damping the noise to
the data's own level costs roughly a third of the recovered spike amplitude, and no
choice of $\lambda$ avoids the trade.

---

## ★★7 — Stacking coherent and incoherent noise

**(a)** Independent noise is reduced by $\sqrt{60} = 7.75$, giving an effective
amplitude noise of 0.129.

**(b)** Coherent ground roll identical on every trace is **not reduced at all**: the
stack of a constant is that constant. The S/N against the ground roll is unchanged.

**(c)** SVD filtering would **not** help here, and the measured numbers say why: the
ground roll is coherent, and so is the signal, so *both* occupy the leading
eigenimages. Truncating the rank removes the signal with the noise. The lesson's
measured experiment makes the point quantitatively: at input S/N 1.48 the best rank
(4) still leaves 29.74 % error, and at S/N 0.49 (noise-dominated) the best rank
leaves 75.17 %. KL filtering is a bet that the noise is incoherent — here it is not.
The correct tool for coherent noise is a velocity or f–k filter, or receiver arrays
during acquisition.

---

## ★★8 — Retained energy and lost peak

**(a)** Energy and peak amplitude are different statistics. A pass band removes
0.82 % of the *energy* (concentrated in the spectral tails) but the removal is
spectrally selective, and the wavelet's *peak* is affected by the coherent
reconstruction of all its components — an asymmetric perturbation can reduce the peak
more than the energy (and in other cases less).

**(b)** (i) Amplitude interpretation needs the **peak** (or an amplitude measure at
the event), so −5.53 % is the relevant number and must be corrected or reported.
(ii) Energy or power analysis needs the **retained energy**, 99.18 %.

**(c)** A rectangular pass band produces Gibbs ringing at its edges and passes the
frequencies just inside the corner with full amplitude while rejecting those just
outside with none; a tapered pass band trades a little more attenuation at the corner
for far less ringing and leakage. The lesson's example is a good outcome because the
signal band (5–40 Hz) lay *inside* the pass band (5–40 Hz) with the noise at 70 and
95 Hz well outside — the ideal case. If the signal band had overlapped the noise band,
no filter would have helped.

---

## ★★9 — Too wide a median window

**(a)** At window 11 the measured peak retention is 62.09 %, so the amplitude error is
about **−38 %** — nearly four times the survey's likely noise level, and systematic.

**(b)** Choose a window of 3 (measured 95.32 % retention, RMS 0.00221) — the narrowest
window that still rejects isolated spikes. The cost is that a two-sample spike may
survive, and that the spike discrimination is weaker (a 3-point median flags a sample
only if it lies outside the interval spanned by its two neighbours).

**(c)** Measure, on real data: (i) the number of samples flagged, compared with the
expected spike rate; (ii) the difference between the filtered and unfiltered amplitude
at a *known* event (a repeat of a control station, or a strong reflection whose
amplitude is stable along the line); (iii) the RMS of the residual (data minus
filtered) in a quiet window, which should match the noise estimate. The third is the
truth-independent check.

---

## ★★★10 — Wavelet distortion versus $\lambda$

A satisfactory experiment:

1. Recover the model $\hat m = \hat d\,\hat h_\lambda$ for a sweep of $\lambda$.
2. Re-convolve: $\hat d_{\text{model}} = \hat w\,\hat m$, so the "residual" of the
   inverse problem is $\hat d - \hat w\hat m = \hat d\,(1 - \hat w\hat h_\lambda)$.
3. Report $\lVert d - d_{\text{model}}\rVert/\lVert d\rVert$ as a function of
   $\lambda$.
4. **Expected shape:** monotonically *increasing* with $\lambda$, from ~0 (at tiny
   $\lambda$ the model explains the data including its noise) to ~1 (large $\lambda$
   gives $m \to 0$ and the residual tends to the data itself).
5. **Interpretation:** the re-convolved residual is a pure measure of *bias* — it
   contains none of the inverse problem's noise amplification, because the noise is
   passed through $\hat w\hat h_\lambda$ which is small out of band. This is the
   cleanest demonstration that the trade is bias against variance: the variance
   (leakage) falls with $\lambda$ while the bias (this residual) rises. Choose
   $\lambda$ where the two curves' *sum* is minimised, which is a concrete criterion.

---

## ★★★11 — Choosing the rank without the truth

Three candidate criteria and an assessment:

| criterion | how it works | trust? |
|---|---|---|
| **elbow on the singular-value spectrum** | plot $\log\sigma_j$ against $j$; choose where the curve's slope breaks | weak: the break is often absent for real gathers, and the choice is subjective |
| **cross-validation over traces** | reconstruct each trace from the others and measure the prediction error | **strongest**: it measures generalisation, the quantity that matters, and needs no truth |
| **noise-level criterion** | retain ranks whose components exceed the noise level estimated from a signal-free window | strong if a genuine noise estimate exists; fails when the noise is coherent |

The cross-validation approach is the most defensible: it holds out traces, reconstructs
them from the retained eigenimages, and selects the rank minimising the prediction
error. Its assumptions are that the held-out traces share the same signal as the
retained ones (true for a coherent event) and that the noise is stationary across the
gather. It fails when the gather contains a strong, spatially varying event, because
then the held-out trace is genuinely different from its neighbours and the criterion
penalises retaining the very signal it should keep.

---

## ★★★12 — A criterion for $\lambda$

The most defensible criterion for this problem is the **discrepancy principle**:
choose the largest $\lambda$ such that the data residual is still consistent with the
known noise level, i.e.

$$\lVert d - w m_\lambda\rVert \le \sqrt{N}\,\sigma_n .$$

Implementation on the lesson's data:

1. Estimate $\sigma_n$ from the noise added in the construction (0.00189) — on real
   data, from a quiet window using the robust scale of
   [05-06-01](../01-processing-pipeline-concept.md).
2. Sweep $\lambda$, computing the residual $\lVert d - w*m_\lambda\rVert$.
3. Take the largest $\lambda$ satisfying the inequality above.

From the measured table, the residual at $\lambda = 0.03$ is 0.06310 and at
$\lambda = 0.1$ is 0.06730, both far above a residual consistent with
$\sigma_n = 0.00189$; the tiny-$\lambda$ rows have residuals of 0.05102–0.00150. The
criterion therefore selects a $\lambda$ in the smallest few rows of the sweep, i.e. it
tolerates substantial leakage. That is *correct* behaviour for the discrepancy
principle — it does not attempt to control the model's noise, only to explain the data
to within their own accuracy.

**Assumptions:** the noise level is known and Gaussian, the wavelet is correct, and
the noise is white. **Failure mode:** if the wavelet is wrong, the residual includes a
modelling error that grows with $\lambda$ in a complicated way and the criterion
selects a $\lambda$ compensating for the wavelet error. On real data the honest
practice is to report $\lambda$, the wavelet, the noise estimate and the residual
together — so that a reader can see which of the three is doing the work.
