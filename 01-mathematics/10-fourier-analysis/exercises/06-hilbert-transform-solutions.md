# Solutions — 01-10-06 Hilbert Transform, Analytic Signal and Instantaneous Phase

> **Read this after attempting the exercises, not before.**
>
> Values quoted from the supplied script are the values it printed.

---

## ★1 — Four transforms

The transfer function is $-i\,\mathrm{sgn}(f)$, i.e. every positive frequency is
rotated by $-90^\circ$ and every negative frequency by $+90^\circ$.

**(a)** $\cos(2\pi f_0t) = \frac12(e^{2\pi if_0t} + e^{-2\pi if_0t})$. The two
components are rotated by $-90^\circ$ and $+90^\circ$ respectively, giving
$\frac12(-i e^{2\pi if_0t} + i e^{-2\pi if_0t}) = \sin(2\pi f_0t)$. So

$$H\{\cos(2\pi f_0t)\} = \boxed{\sin(2\pi f_0t)} .$$

**(b)** Similarly $H\{\sin(2\pi f_0t)\} = \boxed{-\cos(2\pi f_0t)}$.

**(c)** A constant is a zero-frequency signal, and $\mathrm{sgn}(0) = 0$, so
$H\{3\} = \boxed{0}$. This is the statement that the transform has no DC
response: **a constant offset produces no quadrature signal**, which is why the
analytic signal of a record with a large DC offset is not distorted by it.

**(d)** Linearity:

$$H\{\cos + 2\sin\} = \sin - 2\cos .$$

A useful check on (a) and (b) together: $H\{H\{\cos\}\} = H\{\sin\} = -\cos$ ✓,
which is $-\cos$ as required. The pair $(\cos,\sin)$ is a **quadrature pair**, and
the four results (a)–(c) are the whole of the transform's action on a single
tone.

---

## ★2 — The analytic signal of a band-limited signal

**(a)** $Z(f) = 2\hat x(f)$ for $f>0$, $Z(0) = \hat x(0)$, $Z(f) = 0$ for $f<0$.
Explicitly, $Z(f) = 2$ for $0 < f < 5$ Hz, $Z(0) = 1$, and zero elsewhere.

**(b)** Parseval: $\int\lvert Z\rvert^{2}df = 4\int_0^5 1\,df = 20$ against
$\int\lvert \hat x\rvert^{2}df = 2\int_0^5 1\,df = 10$. So the analytic signal
carries **twice** the energy of the original — because the negative-frequency half
has been folded onto the positive half rather than discarded. The factor is
exactly 2 for a signal with no DC and no Nyquist content; it is *not* 2 in
general, which is why energy comparisons between a real trace and its analytic
signal must be made carefully.

**(c)** $x(t) = \mathrm{Re}\,z(t)$, one line.

---

## ★3 — Envelope and phase of a complex number

$$A = \lvert 3+4i\rvert = \sqrt{9+16} = \boxed{5}, \qquad
\theta = \arctan_2(4,3) = \boxed{53.130^\circ} .$$

If the same value occurs at $t = 0$ and $t = 0.01$ s, then $\theta$ is unchanged
over that interval and

$$f_{\text{inst}} = \frac{1}{2\pi}\frac{\Delta\theta}{\Delta t} = 0 .$$

A constant complex value is a stationary phasor: constant envelope, constant
phase, zero instantaneous frequency. This is the correct answer and it is a
useful reminder that the instantaneous frequency is the *rate of change* of the
phase, not the phase itself — a common slip when reading attribute sections,
where a bright envelope does not imply any particular instantaneous frequency.

---

## ★4 — Amplitude modulation

**(a)** The envelope is $\lvert 1 + 0.5\cos(2\pi\cdot2t)\rvert$, i.e. the
modulation itself, because the carrier's own quadrature component is
$a(t)\cos\theta$ shifted to $a(t)\sin\theta$, whose modulus is $\lvert a(t)\rvert$.
**No low-pass filter of $x$ can recover the modulation**, because $x$ has zero
mean: averaging $x$ over any window of a few carrier periods gives zero, not the
modulation. The modulation information lives in the *amplitude* of the carrier,
which is invisible in the raw signal's mean but explicit in the envelope.

**(b)** The envelope of $a(t)\cos(2\pi f_ct)$ equals $\lvert a(t)\rvert$ exactly
when $a$ has no spectral content at or above the carrier frequency — the
**Bedrosian condition**. Here the modulation is 2 Hz and the carrier 60 Hz, so
the condition is satisfied with a wide margin, and the demo measures an envelope
error of $2.1\times10^{-13}$ (maximum) against the exact modulation.

---

## ★★5 — Proof that $H\{H\{x\}\} = -x$

In the frequency domain, applying the transform twice multiplies by

$$\left(-i\,\mathrm{sgn}(f)\right)\times\left(-i\,\mathrm{sgn}(f)\right)
= (-i)^2\,\mathrm{sgn}^2(f) = -1 ,$$

since $\mathrm{sgn}^2 = 1$ away from $f = 0$ and the value at $f = 0$ is measure
zero and contributes nothing. Therefore
$\widehat{H\{H\{x\}\}}(f) = -\hat x(f)$ and, by uniqueness of the transform,
$H\{H\{x\}\} = -x$.

The demo measures a maximum discrepancy of $5.4\times10^{-14}$ on a periodic test
signal.

**Two consequences.** First, the analytic signal $z = x + iH\{x\}$ satisfies
$H\{z\} = H\{x\} + iH\{H\{x\}\} = H\{x\} - ix = -i(x + iH\{x\}) = -iz$: the
analytic signal is an eigenfunction of the transform with eigenvalue $-i$, which
is the compact way of saying "its spectrum is one-sided". Second, the transform is
invertible, so it loses no information, even though $H\{x\}$ looks like a
derivative and feels lossy.

---

## ★★6 — A chirp

**(a)** $f_{\text{inst}} = \frac{1}{2\pi}\frac{d\theta}{dt}
= \frac{1}{2\pi}\cdot2\pi(5 + 8t) = 5 + 8t$ Hz.

**(b)** $f(0) = 5$ Hz, $f(0.5) = 9$ Hz, $f(1.0) = 13$ Hz.

**(c)** If the phase is defined only up to $t = 1$ s the band is 5–13 Hz, and the
sampling rate must exceed 26 Hz to represent the instantaneous frequency
unambiguously — with a comfortable margin in practice, because phase increments
are noisy. If the signal continues past 1 s, the sweep continues upwards without
limit, and the required rate grows with the record length.

**(d)** A signal whose instantaneous frequency exceeds the Nyquist frequency is
still sampled without error *as a waveform*: the samples are correct values of
the continuous signal. What fails is the *interpretation* of the phase
increments: unwrapping assumes the increment between consecutive samples is less
than $\pi$, so a larger true increment is interpreted as its folded counterpart,
and the recovered instantaneous frequency appears to jump to a low value — the
same fold as in [01-10-05](../05-windowing-aliasing.md), now applied to the phase
derivative rather than to the signal itself. The visible symptom is a
discontinuous jump in the instantaneous-frequency section, not an obvious
distortion of the waveform.

---

## ★★7 — The Nyquist bin

**(a)** $x[n] = \cos(\pi n) = (-1)^n$ for $n = 0,\ldots,7$. The DFT is

$$X[k] = \sum_{n=0}^{7}(-1)^ne^{-2\pi ikn/8} .$$

With $k = 4$: $e^{-2\pi i\cdot4n/8} = e^{-i\pi n} = (-1)^n$, so
$X[4] = \sum_n(-1)^n(-1)^n = \sum_n 1 = \boxed{8}$. For every other $k$ the sum
is a geometric series with ratio $-e^{-2\pi ik/8} \ne 1$, and it vanishes. So the
signal lives entirely in bin $k = 4 = N/2$, the Nyquist bin.

**(b)** The correct amplitude recovery for this bin is

$$A = \frac{\lvert X[N/2]\rvert}{N} = \frac{8}{8} = 1 ,$$

with **no factor of 2**. Applying the "double every bin except DC" rule gives
$2\times8/8 = 2$ — a factor-of-2 overestimate.

**(c)** The Nyquist bin is exceptional because at exactly $f = f_N$ the positive
and negative frequencies coincide: $+f_N$ and $-f_N$ are the same bin, so there is
no discarded twin to compensate for. The general rule is therefore "double every
bin except $k = 0$ and, for even $N$, $k = N/2$" — and the demo's implementation
follows it, keeping $Z[N/2] = X[N/2]$ un-doubled.

---

## ★★8 — Two Ricker wavelets 20 ms apart

**(a)** Dominant frequency 25 Hz means a dominant period of 40 ms, so 20 ms is
**half a period**.

- *Opposite signs*: at the position of the second wavelet's peak, the first
  wavelet (half a period away) is at its minimum, and its value there is opposite
  in sign to the second's peak — the two reinforce in a way that produces *one*
  broadened maximum of increased amplitude. Prediction: **one** envelope maximum.
- *Equal signs*: at each wavelet's peak the other contributes a value of the
  opposite sign to the peak (since a Ricker's value half a period away is on the
  opposite side), so the two peaks are *reduced* and a notch appears between
  them. Prediction: **two** maxima, each smaller than a single unit wavelet, if
  the notch is deep enough to be sampled.

**(b)** The script reports exactly this structure:

| configuration | separation | maxima | peak envelope |
|---|---|---|---|
| opposite signs | 20 ms | 1 | 1.4930 |
| equal signs | 20 ms | 2 | 0.7443 |
| equal signs | 40 ms | 2 | 0.9996 |
| opposite signs | 10 ms | 1 | 1.4362 |

So at half-period separation the opposite-sign pair merges into a single
*enhanced* event (1.4930 against 1.0000 for a unit wavelet), while the equal-sign
pair splits into two *diminished* lobes (0.7443). At 40 ms — a full dominant
period — the equal-sign pair is resolved with the peak back to approximately
1.0000.

**(c)** The implication for thin-bed work is stark: at half-period separation the
envelope amplitude of a *negative* reflection coefficient next to a positive one
is 1.49 — larger than either coefficient, and unrelated to their sum of 0. Any
attempt to read reflection coefficients off envelope amplitudes in a
thin-bedded sequence will confuse constructive and destructive interference
with changes in rock properties. What the envelope safely provides is *event
location*; what it does not provide is *amplitude* whenever two events are closer
than about one dominant period.

---

## ★★★9 — The two-tone signal

**(a)** The script reports an envelope range of $0.0876$ to $1.9115$ and an
instantaneous-frequency range of $-118.03$ to $38.85$ Hz for a signal composed of
30 Hz and 46 Hz tones.

**(b)** The analytic signal is a *model* of the data as one amplitude-modulated
phasor, $z = A(t)e^{i\theta(t)}$, and a two-tone signal is not that model. With
two equal-ish components the model must choose a single phase, so the recovered
instantaneous frequency oscillates around the *mean* of the two input
frequencies (38 Hz) — the sampled values 33.5–37.6 Hz bracket the mean of 38 Hz.
The extremes are diagnostic of what is happening. The negative extreme
($-118.03$ Hz) occurs at sample 188, where the envelope has its global minimum
($0.0876$ at sample 187): where the two components nearly cancel, a small change
in their relative phase moves $\arg z$ through a large angle, and for a short
interval the phasor's rotation *reverses*, giving a negative instantaneous
frequency. The positive extreme ($38.85$ Hz) occurs at sample 4016 of 4096 —
three dozen samples from the end of the record, where the transform's edge effect
is largest and the value is not interpretable at all. So the range printed by the
script mixes a genuine interference effect with an edge artefact, and both are
worth recognising: over the interior of the record the instantaneous frequency
stays near the mean of the two tones.

**(c)** Two unit-amplitude tones can add to at most 2 and can cancel to as little
as 0. The measured range 0.0876 to 1.9115 is consistent with that: the maximum is
below 2 because the two tones are not exactly in phase anywhere in the sampled
record (they are at 30 and 46 Hz, so their relative phase drifts continuously),
and the minimum is above 0 for the same reason. So the envelope is behaving
exactly as the sum of two tones must.

**(d)** Before computing instantaneous frequency on real data: **band-pass the
record** to a band narrow relative to its centre frequency (a fractional
bandwidth of an octave or less is a reasonable starting point), and taper the
ends. Alongside any instantaneous-frequency or envelope result, report the band
it was computed in and the taper or end-sample rejection used. Without those two
facts the numbers cannot be compared with anything, because a different band
gives different attributes from the same data.

---

## ★★★10 — Edge effects

**(a)** The transform is non-local: $H\{x\}(t)$ depends on $x$ at every other
time, weighting distant samples as $1/(t-\tau)$. On a finite record the
convolution can only use the samples that exist, so near the ends the operator is
effectively truncated and the quadrature signal is wrong. A spectral
implementation has the same difficulty expressed differently: it assumes the
record is periodic, so the signal actually transformed is the record with its
far end glued to its beginning — a discontinuity at the wrap point, which is a
large-amplitude, broadband artefact. In the middle half of a smooth chirp neither
effect has much influence, so the error is 0.079 Hz; over the whole record the
ends dominate and the error reaches 4.515 Hz, nearly two orders of magnitude
larger.

**(b)** The envelope of a constant-amplitude chirp should be 1 everywhere. In the
middle half the script measures 0.997648 to 1.002117 — within 0.24%. Near the
ends the departure is much larger: the script's own measurement over the *whole*
record gives an envelope range of 0.5438 to 1.3814, i.e. departures of $-46\%$
and $+38\%$ from the true constant amplitude, concentrated in the first and last
few hundred samples. That is the truncation artefact of (a), and its size is the
reason attributes near a record's ends are discarded rather than interpreted.

**(c)** The test: build a synthetic trace of known constant amplitude, compute the
envelope, and plot or tabulate the maximum absolute deviation from 1.0 as a
function of the number of samples discarded from each end, for several wavelet
lengths. The quantity to report is the smallest number of discarded samples at
which the deviation falls below the noise level you care about — expressed, for
convenience, as a multiple of the dominant wavelet length rather than in samples,
so that the number transfers to other datasets. The demo's own practice (64
samples on a 2048-sample trace at 2 ms, i.e. about 1.5 dominant periods of the
18 Hz pulse) is a concrete example of the answer.

**(d)** The spectral implementation is *algebraically* non-local, because the
split of "positive frequencies doubled, negative frequencies zeroed" cannot be
written as a short convolution. Its edge effects come from the periodic
assumption: the discrete spectrum describes a record that repeats end-to-end, so
if the record does not actually do that — and it never does — the effective
signal contains a jump at the wrap point. The transform then produces the ringing
that a jump always produces (the Gibbs phenomenon of
[01-10-01](../01-fourier-series.md)), which appears as an edge artefact. The cure
is the same as in every other spectral application: taper the ends, or pad them
symmetrically so that the periodic extension is continuous to first order, or
discard the ends.
