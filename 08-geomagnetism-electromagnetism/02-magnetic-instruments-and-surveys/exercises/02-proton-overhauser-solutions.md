# Solutions — 08-02-02 Proton Precession and Overhauser Magnetometers

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [02 Proton Precession and Overhauser Magnetometers](../02-proton-overhauser.md).

---

## ★1 — Precession frequency at 45000 nT

$$\frac{\gamma_p}{2\pi} = \frac{2.6752218744\times10^{8}}{2\pi}
= 4.257749\times10^{7}\ \mathrm{Hz\,T^{-1}},$$

$$f_L = 4.257749\times10^{7}\times45000\times10^{-9}
= 1915.99\ \mathrm{Hz}.$$

Equivalently, $0.042577\ \mathrm{Hz\,nT^{-1}}\times45000\ \mathrm{nT}
= 1915.99\ \mathrm{Hz}$. ✔

---

## ★2 — Field resolution from a 1 mHz counter

$$\Delta B = \frac{\Delta f}{\gamma_p/2\pi}
= \frac{1.0\times10^{-3}}{4.257749\times10^{7}}
= 2.349\times10^{-11}\ \mathrm{T} = 0.02349\ \mathrm{nT}.$$

So a millilitre-class counter resolution corresponds to about $0.023\ \mathrm{nT}$
of field — **provided** the signal-to-noise ratio is high enough for the
interpolation to reach that resolution. Section 3 of the lesson shows it is the
SNR, not the counter, that normally limits a real instrument.

---

## ★3 — Amplitude retention

$$a(t) = a_0\,e^{-t/T_2^{*}}.$$

| $t$ (s) | $t/T_2^{*}$ | fraction retained |
|---|---|---|
| 1.0 | 0.5 | $e^{-0.5} = 0.606531$ |
| 2.0 | 1.0 | $e^{-1} = 0.367879$ |
| 6.0 | 3.0 | $e^{-3} = 0.049787$ |

After 6 s (three envelope times) only 5% of the amplitude is left, which is why a
pulsed instrument's acquisition window is a few $T_2^{*}$ and no more.

---

## ★4 — Verifying the $1/\mathrm{SNR}$ law

$$\frac{\sigma_f(1)}{\sigma_f(100)} = \frac{0.00552604}{0.00005598}
= 98.71.$$

The law predicts exactly 100 for a hundredfold SNR. The measured 98.71 is within
1.3% of the prediction, which is the Monte Carlo scatter of 400 realisations
(the standard error of a standard deviation with $N = 400$ is about
$1/\sqrt{2N} = 3.5\%$).

**SNR needed for 0.01 nT.** The target frequency error is

$$\sigma_f^{\text{target}} = 0.01\ \mathrm{nT}\times 0.042577\
\mathrm{Hz\,nT^{-1}} = 4.2577\times10^{-4}\ \mathrm{Hz}.$$

With $\sigma_f = 0.00552604\ \mathrm{Hz}$ at SNR $= 1$ and
$\sigma_f\propto 1/\mathrm{SNR}$:

$$\mathrm{SNR} = \frac{0.00552604}{4.2577\times10^{-4}} = 12.98.$$

So an SNR of about 13 at a 2.0 s counting time delivers 0.01 nT.

---

## ★5 — Duty cycle and reading rate

$$\text{cycle} = 5.0 + 1.0 + 0.3 = 6.3\ \mathrm{s}, \qquad
\text{duty cycle} = \frac{1.0}{6.3} = 15.87\%,$$

$$\text{readings per hour} = \frac{3600}{6.3} = 571.4\ \mathrm{hour^{-1}}
= 0.159\ \mathrm{s^{-1}}.$$

A continuous sensor sampled once per second gives
$3600/1.0 = 3600\ \mathrm{readings\,hour^{-1}}$, so the ratio is

$$\frac{3600}{571.4} = 6.30,$$

i.e. **the pulsed instrument delivers one reading for every 6.3 the continuous
one does**, exactly the ratio of the cycle times. The continuous instrument also
has no dead interval in which a transient can be missed — the qualitative
difference that matters for monitoring and for moving platforms.

---

## ★6 — Counting time for 0.01 nT

From the table at SNR $= 10$, $\sigma_B = 0.012856\ \mathrm{nT}$ at
$T_{\text{acq}} = 2.0\ \mathrm{s}$.

**Assuming $T^{-3/2}$:** to reduce the error by $0.012856/0.01 = 1.2856$ requires

$$T_{\text{acq}} = 2.0\times1.2856^{2/3} = 2.0\times1.1823
= 2.365\ \mathrm{s}.$$

**Reading the table:** 2.0 s gives 0.012856 nT and 4.0 s gives 0.007181 nT, so
the target lies between them; log-linear interpolation gives

$$T_{\text{acq}} \approx 2.0\times\left(\frac{0.012856}{0.01}\right)^{1/0.84}
\approx 2.0\times1.349 = 2.70\ \mathrm{s},$$

using the measured local slope of $-0.84$ instead of $-1.5$.

**The discrepancy is the point.** The $T^{-3/2}$ law assumes a signal of constant
amplitude, while the envelope decays with $T_2^{*} = 2.0\ \mathrm{s}$: beyond
about one envelope time the extra samples carry mostly noise, so the measured
local slope is milder than the ideal law and the required counting time is longer
than the naive estimate. A design based on the ideal law would under-specify the
count by about 14% (2.70/2.365 = 1.140).

---

## ★7 — A scalar sensor specification (executable version)

**Target.** $\sigma_B = 0.05\ \mathrm{nT}$ per reading, one reading every 2 s.

**Frequency requirement.** $0.05\ \mathrm{nT}\times0.042577\
\mathrm{Hz\,nT^{-1}} = 2.13\ \mathrm{mHz}$.

**Counting time.** From ★6, reaching 0.01 nT needs about 2.4–2.7 s. The required
precision is five times looser, so with the measured local slope of about $-1$
over the range 0.25–1 s, roughly 0.4–0.5 s of acquisition suffices at
comparable SNR. Take $T_{\text{acq}} = 0.6\ \mathrm{s}$ with margin.

**SNR.** Scale ★4: 0.01 nT needed SNR 13 at 2.0 s. At 0.6 s the record is shorter,
so more SNR is needed; using the measured $\sigma_f \propto T^{-1.2}$ in this
range, $\mathrm{SNR} \approx 13\times(2.0/0.6)^{1.2} \approx 55$. **This is the
hardest requirement**, and it is met by sensor amplitude, not by electronics:
the polarised magnetisation scales with sample volume and polarising field.

**Duty cycle.** With $T_{\text{pol}} = 1.4\ \mathrm{s}$ (about one $T_2^{*}$ of
build-up), $T_{\text{acq}} = 0.6\ \mathrm{s}$ and 0.05 s of overhead the cycle is
2.05 s, giving a duty cycle of 29% and 1756 readings per hour (0.49 s$^{-1}$).
For one reading per 2 s that is ample; for a continuously sampled recorder it is
not, which is the argument for Overhauser or alkali operation.

**How to test it.** (i) Measure $\sigma_f$ against counting time at fixed SNR and
check the saturation against $T_2^{*}$; (ii) measure $\sigma_B$ against SNR and
check the slope is $-1$; (iii) run a long repeat series in a magnetically quiet
place and verify the Allan deviation reaches the specified 0.05 nT at 2 s
without drift; (iv) deliberately introduce a field gradient across the sensor and
verify that the loss of precision appears as a shorter $T_2^{*}$, since that
distinguishes a gradient from noise.

---

## ★8 — The Cramér–Rao bound and its breakdown

**Model.** Samples $y_k = A\sin(\omega t_k) + n_k$, $k = 0\ldots N-1$, with
$t_k = k/f_s$ and $n_k$ white with variance $\sigma^2$. The Fisher information for
$\omega$ from a sinusoid of unknown amplitude and phase is the standard result

$$I(\omega) = \frac{2A^{2}}{\sigma^{2}}\sum_k t_k^{2}\cos^{2}(\omega t_k)
\approx \frac{A^{2}}{\sigma^{2}}\sum_k t_k^{2},$$

using $\left<\cos^2\right> = 1/2$. With $t_k = k/f_s$,

$$\sum_{k=0}^{N-1}t_k^{2} = \frac{1}{f_s^{2}}\frac{(N-1)N(2N-1)}{6}
\approx \frac{N^{3}}{3f_s^{2}},$$

so $I(\omega) \approx A^{2}N^{3}/(3\sigma^{2}f_s^{2})$, and the bound
$\mathrm{Var}(\hat\omega) \ge 1/I$ gives

$$\sigma_\omega \approx \frac{\sqrt{3}\,\sigma f_s}{A\,N^{3/2}}, \qquad
\sigma_f = \frac{\sigma_\omega}{2\pi}
= \frac{\sqrt{3}\,\sigma f_s}{2\pi A\,N^{3/2}}.$$

With $T = N/f_s$ and $N = T f_s$:

$$\boxed{\;\sigma_f \propto \frac{\sigma}{A}\,\frac{f_s}{N^{3/2}}
= \frac{\sigma}{A}\,\frac{1}{\sqrt{f_s}}\,\frac{1}{T^{3/2}}.\;}$$

Hence $\sigma_f \propto \sigma/(A T^{3/2})$: the amplitude enters to the first
power, the duration to the three-halves power, and the sampling rate weakly.

**Why a damped signal breaks it.** The derivation assumes every sample carries the
same signal amplitude. With $A(t) = A_0e^{-t/T_2^{*}}$, the Fisher information is
weighted by the squared amplitude, so

$$I(\omega) \propto \sum_k e^{-2t_k/T_2^{*}} t_k^{2}
\;\xrightarrow[T \gg T_2^{*}]{}\; \text{a constant,}$$

because the sum is dominated by the first few envelope times regardless of how
long the record is. Long records add only noise, so $\sigma_f$ flattens: the
measured local slopes ($-1.41$ early, $-0.20$ late) are the transition between
the two regimes. The practical rule follows directly: **the usable count is a few
$T_2^{*}$, and beyond that the only lever is amplitude.**
