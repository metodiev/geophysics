# Exercises — 03-10-05 Preprocessing: Detrend, Taper, Filter, Decimate

Attempt these **closed-book** before opening the
[solutions](./05-filtering-detrending-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Run the demonstration first; several answers require its printed values:

```
.venv/bin/python 03-scientific-computing/10-obspy-and-seismic-data/code/filtering_detrending_demo.py
```

The synthetic trace is 10 000 samples at 500 Hz (20 s) and contains a 4 Hz wave
packet, a 90 Hz hum, a linear trend of 2000 counts/s, a constant offset and
20 counts RMS of noise, from `np.random.default_rng(20240315)`.

---

## ★ Foundational

**★1.** State what `detrend("simple")`, `detrend("linear")` and
`detrend("polynomial", order=2)` remove. Give the measured residual mean after
`simple`.

**★2.** Compute the alias frequency of a 50 Hz hum decimated from 200 Hz by a
factor of 8. State the new sample rate and the new Nyquist frequency, and say
whether the alias lands in a 2–10 Hz band.

**★3.** For a narrow-band signal at 6 Hz, predict the factor by which
`differentiate()` and `integrate()` change its RMS amplitude.

**★4.** Give the measured peak-sample shift in samples and milliseconds for the
causal and zero-phase 2–6 Hz bandpass on a 500 Hz trace. State the sampling
interval used to convert.

**★5.** Why must an anti-alias filter be applied *before* decimation rather than
after? Answer in three sentences, using the word *ambiguous* once.

---

## ★★ Applied

**★★6.** The raw trace has a 39 777.17-count step between its first and last
samples. Explain its origin, predict its effect on a discrete Fourier
transform, and explain why the taper reduces the 0–1 Hz RMS by only 4 % while
detrending reduces it by a factor of $1.8\times10^4$.

**★★7.** From the measured 3–5 Hz RMS values with and without the anti-alias
filter (946.7407 and 884.7426 counts), compute the spurious RMS amplitude and
compare it with the true 90 Hz amplitude of 300 counts peak.

**★★8.** Design an anti-alias filter for decimating 500 Hz by 16. State the new
Nyquist, the passband you would preserve, and the stopband attenuation you
require. Then state which measured RMS column in the demo demonstrates that
your design works.

**★★9.** The differentiate measurement exceeds $2\pi f$ by 0.039 % and the
integrate measurement exceeds $1/(2\pi f)$ by 0.217 %. Explain both residuals
in terms of the finite bandwidth of the packet.

**★★10.** Two pipelines are compared: detrend→taper→filter and
filter→detrend. The measured 3–5 Hz RMS differs by 0.0030 counts. State
whether this shows the operations commute, and construct a case in which they
would not.

---

## ★★★ Research-oriented

**★★★11.** Measure the causal-filter latency as a function of order (2, 4, 6,
8 corners) for a 2–6 Hz bandpass at 500 Hz. Report the relationship you measure
between order and shift, and state whether a causal filter can be used for
arrival-time measurement and under what conditions.

**★★★12.** Construct a test in which a true high-frequency component folds
onto a frequency already occupied by signal after decimation. Report the two
frequencies, the decimation factor, and the resulting amplitude error. Then
design a test that detects the contamination without knowing the true signal,
and state the test's limitation.

**★★★13.** Choose a genuine preprocessing chain for a specific scientific
target — say, measuring Rayleigh-wave group velocity between 5 s and 20 s
period. State every step, its parameters, the frequency band it protects, and
the measurement that would reveal if the chain damaged the signal.
