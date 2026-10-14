# Exercises — 01-10-06 Hilbert Transform, Analytic Signal and Instantaneous Phase

Attempt these **closed-book** before opening the
[solutions](./06-hilbert-transform-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Convention: forward kernel $e^{-2\pi ift}$, so
$\widehat{H\{x\}}(f) = -i\,\mathrm{sgn}(f)\hat x(f)$.

---

## ★ Foundational

**★1.** Give $H\{x\}$ for each signal, and say which property of the transform
each answer illustrates.

(a) $x(t) = \cos(2\pi f_0t)$
(b) $x(t) = \sin(2\pi f_0t)$
(c) $x(t) = 3$ (a constant)
(d) $x(t) = \cos(2\pi f_0t) + 2\sin(2\pi f_0t)$

---

**★2.** A real signal has $\hat x(f) = 1$ for $0 < f < 5$ Hz and zero elsewhere
(take $\hat x(-f) = \hat x(f)$).

(a) Write $Z(f)$, the spectrum of the analytic signal.
(b) State the energy ratio between the analytic signal and the original signal.
(c) State how $x(t)$ is recovered from $z(t)$ in one line.

---

**★3.** For $z = 3 + 4i$, compute the envelope and the instantaneous phase at
that instant. If the same $z$ occurs at $t = 0$ and again at $t = 0.01$ s as
$z = 3 + 4i$, what is the instantaneous frequency between them?

---

**★4.** An amplitude-modulated carrier is
$x(t) = (1 + 0.5\cos(2\pi\cdot2t))\cos(2\pi\cdot60t)$.

(a) State the envelope, and why no low-pass filter of $x$ itself can recover it.
(b) State the condition on the modulation frequency for the envelope to be exact.

---

## ★★ Applied

**★★5.** Prove $H\{H\{x\}\} = -x$ from the transfer function, stating the
convention you use.

---

**★★6.** A chirp has analytic phase
$\theta(t) = 2\pi(5t + 4t^2)$ radians.

(a) Compute the instantaneous frequency as a function of time.
(b) Evaluate it at $t = 0$, 0.5 and 1 s.
(c) State the band the signal sweeps, and the sampling rate needed to avoid
aliasing the *instantaneous frequency*.
(d) Explain why a signal whose instantaneous frequency exceeds Nyquist does not
simply "lose" the high frequencies but folds them.

---

**★★7.** A 8-sample record contains a cosine at exactly the Nyquist frequency,
$x[n] = \cos(\pi n)$.

(a) Compute the DFT and state which bin carries the signal.
(b) State the correct amplitude-recovery factor for that bin, and what you get if
you apply the "double every bin except DC" rule instead.
(c) Explain in one sentence why the Nyquist bin is exceptional.

---

**★★8.** A synthetic trace contains two Ricker wavelets with dominant frequency
25 Hz (dominant period 40 ms), separated by 20 ms.

(a) Predict, for the two cases (equal signs, opposite signs), how many envelope
maxima there will be and roughly how large the peak will be relative to a single
unit wavelet. Justify physically.
(b) The supplied script gives: separation 20 ms with opposite signs $\to$ 1
maximum, peak 1.4930; with equal signs $\to$ 2 maxima, peak 0.7443; separation
40 ms with equal signs $\to$ 2 maxima, peak 0.9996. Compare with your prediction.
(c) State what the result implies for using envelope peaks to measure reflection
coefficients in a thin-bed sequence.

---

## ★★★ Research-oriented

**★★★9.** Using [`code/hilbert_demo.py`](../code/hilbert_demo.py):

(a) Report the envelope range and the instantaneous-frequency range that the
script measures for the two-tone signal (30 Hz and 46 Hz).
(b) Explain why the instantaneous frequency does not report either 30 or 46 Hz,
and why the range extends to negative values.
(c) The envelope of the two-tone signal ranges from about 0.09 to 1.91. Show that
these are consistent with the sum of two unit-amplitude tones.
(d) State what you would do to a real dataset before computing instantaneous
frequency, and what you would report alongside it.

---

**★★★10.** Edge effects and their scaling.

(a) In the script's chirp test, the maximum instantaneous-frequency error is
0.079 Hz over the middle half of the record and 4.515 Hz over the whole record.
Explain the difference in terms of the non-locality of the transform.
(b) The envelope of a constant-amplitude chirp should be 1. Report the script's
range in the middle half, and the departure near the ends.
(c) Design a test to decide how many samples at each end must be discarded as a
function of the wavelet length, and describe what you would plot.
(d) The transform is implemented spectrally, so it is not obviously non-local.
Explain why a spectral implementation nevertheless has edge effects.
