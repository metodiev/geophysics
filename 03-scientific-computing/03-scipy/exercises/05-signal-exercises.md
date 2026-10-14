# Exercises — 03-03-05 scipy.signal: Filters, Windows and Spectral Estimation

Attempt these **closed-book** before opening the
[solutions](./05-signal-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems that refer to
[`../code/signal_demo.py`](../code/signal_demo.py) require you to run it and
report its actual output:

```
.venv/bin/python 03-scientific-computing/03-scipy/code/signal_demo.py
```

The sampling rate in the demo is $f_s = 500$ Hz and the Ricker wavelet's
dominant frequency is 32 Hz.

---

## ★ Foundational

**★1.** The Ricker (Mexican-hat) wavelet is

$$w(t) = \left(1 - 2\pi^2 f^2 t^2\right) e^{-\pi^2 f^2 t^2}.$$

(a) Evaluate $w(0)$.
(b) Find its zero crossings and express them in milliseconds for $f = 32$ Hz,
and in samples at 500 Hz.
(c) Compute $\int_{-\infty}^{\infty}w(t)\,dt$ and state the geophysical
consequence of its value.
(d) The demo reports the trace amplitude at the 0.250 s pick as 0.8703 times
the peak, for a reflectivity of 0.80. Explain why it is not 0.80.

---

**★2.** For a fourth-order digital Butterworth low-pass with $f_c = 40$ Hz at
$f_s = 500$ Hz, the demo reports

```
         4           39.9933       0.707107              -36.14              -86.30
```

(a) Show that the bilinear transform maps $f = 100$ Hz to
$\tan(\pi f/f_s)/\tan(\pi f_c/f_s) = 2.829$ times the cut-off.
(b) Using $|H|^2 = 1/(1 + (f'/f_c')^{2N})$ with the warped ratio, compute
$|H|$ at 100 Hz in dB and check the tabulated value.
(c) Repeat for $N = 2$ and check $-18.14$ dB.
(d) Explain why $20N\log_{10}(100/40)$ predicts a smaller attenuation.

---

**★3.** The demo reports the group delay of a fourth-order 40 Hz low-pass:

```
    group delay at    5 Hz =  10.252 ms
    group delay at   32 Hz =  15.344 ms
    group delay at   40 Hz =  15.342 ms
```

and a cross-correlation latency of the whole trace of 12.000 ms.

(a) Convert the 15.344 ms delay to samples at 500 Hz.
(b) Explain why the measured 12.000 ms is neither the 10.252 nor the 15.344 ms
value.
(c) State how the delay in *seconds* changes if the same 40 Hz filter is applied
to a record sampled at 1000 Hz, and justify the answer from the phase response.
(d) A tomographic arrival is picked to 0.5 ms. By what factor must the filter's
delay be known before the pick is meaningful?

---

## ★★ Applied

**★4.** The window table is

```
    window           -6 dB width (bins) null-to-null (bins)  first sidelobe (dB)
    boxcar                        0.605               2.000               -13.26
    hann                          1.000               4.000               -31.47
    hamming                       0.906               4.000               -42.62
    blackman                      1.148               6.000               -58.11
    kaiser(beta=8)                1.109               5.469               -58.69
    kaiser(beta=14)               1.438               9.133              -105.95
```

and the monochromatic-signal test is

```
    window            on-bin amplitude     error  half-bin amplitude  loss (dB)
    boxcar                    1.000000  2.22e-16            0.645881     -3.797
    hann                      1.000000  4.44e-16            0.848835     -1.424
    hamming                   1.000000  4.44e-16            0.818752     -1.737
    blackman                  1.000000  4.44e-16            0.881166     -1.099
```

(a) Convert the boxcar's first-sidelobe level to a linear amplitude ratio.
(b) Compute the percentage amplitude error introduced by scalloping for the
boxcar and for Hann.
(c) State which window you would use to measure the amplitude of a monochromatic
tidal line to 1%, and why.
(d) Explain why Hamming's first sidelobe is lower than Hann's while its
null-to-null mainlobe width is the same.

---

**★5.** The causality test reports

```
    filter                        max |difference|  at sample  time (s)
    sosfilt (causal)                     0.000e+00          0    0.000
    sosfiltfilt (zero-phase)             8.416e-03        499    0.998
   ... the first sample where the two differ by more than 1e-9 is
  347 (0.694 s), 153 samples before the truncation.
```

(a) Explain why the causal filter's difference is *exactly* zero and not merely
small.
(b) Express the 153-sample look-ahead in seconds and in periods of the 20 Hz
cut-off.
(c) Predict, with a reason, the look-ahead for the same record filtered with a
10 Hz cut-off, then measure it by modifying the demo and report the value.
(d) An early-warning system must issue an alert within 3 s of the first P
arrival and filters with `sosfiltfilt` at 0.5 Hz. State whether this is
possible, with the numbers that decide it.

---

**★6.** The PSD check reports

```
    sum(Pxx) * df = 0.582609
    var(x)        = 0.565053   (mean of x = 1.882e-03)
    ratio         = 1.031069  (+3.11%)
    The same test on a stationary white record gives 0.989781 (-1.02%)
```

(a) Compute the absolute variance discrepancy in m² s⁻², and the implied RMS
discrepancy.
(b) Explain why the chirp's ratio differs from 1 while the white record's is
closer.
(c) A colleague computes a PSD with `scaling='spectrum'` and finds that
`Pxx.sum() * df` equals the variance divided by 2. Explain the factor of two.
(d) State the one-line test that would have caught the error in (c).

---

## ★★★ Research-oriented

**★7.** Design a low-pass filter with $f_s = 500$ Hz, $f_c = 40$ Hz and at
least 60 dB of attenuation at 100 Hz.

(a) Show that the digital Butterworth attenuation at 100 Hz for order $N$ is
$10\log_{10}\left(1 + 2.829^{2N}\right)$ dB.
(b) Compute the minimum order satisfying the specification.
(c) Verify your design with `sosfreqz`, report the measured attenuation, and
state the order of the resulting filter's group delay at 32 Hz.
(d) Compare your design with a 5th-order elliptic filter of the same edges and
state one specification in which the elliptic filter is preferable and one in
which it is not.

---

**★8.** A reflection-seismic processor applies a 20 Hz low-pass with
`sosfiltfilt` and then picks first breaks to 0.5 ms.

(a) Explain why the zero-phase choice is correct here and what it would cost in
a real-time system.
(b) The same filter applied causally has a group delay varying from 10.25 ms at
5 Hz to 15.34 ms at 40 Hz. Compute the differential delay across the band and
explain why it cannot be removed by subtracting a constant.
(c) Explain how the differential delay appears in a wavelet: name the effect and
describe the resulting change in the waveform.
(d) The processor rejects your suggestion to use `sosfilt` with a correction
because "the residual delay is only 12 ms and the survey tolerance is 20 ms".
Construct the quantitative reply, using the differential delay of (b) rather
than the mean.
