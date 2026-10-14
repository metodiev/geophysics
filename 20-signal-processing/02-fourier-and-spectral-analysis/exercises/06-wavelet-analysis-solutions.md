# Solutions — 20-02-06 Wavelet Transforms and Multiresolution Analysis

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [06 Wavelet Transforms and Multiresolution Analysis](../06-wavelet-analysis.md).

---

## ★1 — The four orthonormality conditions

$$\sum_n h[n] = \sqrt2, \qquad
\sum_n h^{2}[n] = 1, \qquad
\sum_n h[n]h[n+2k] = \delta_{k0}, \qquad
\sum_n h[n]g[n+2k] = 0,$$

with $g[n] = (-1)^{n}h[L-1-n]$.

**What fails without the $1/\sqrt2$:** the first and second conditions together.
The unnormalised "sum = 2" form (sine/cosine-like filters scaled by 1 instead of
$1/\sqrt2$) still satisfies the *shift* orthogonality conditions — those depend on
ratios, not scale — but gives $\sum h^{2} = 2$ instead of 1, so the transform is
not orthonormal: analysis followed by synthesis scales the signal by 2, the
energy test $\sum x^{2} = \sum cA^{2}+\sum cD^{2}$ fails by a factor 2, and the
transform is a *biorthogonal* one that needs different synthesis filters.
Checking $\sum h = \sqrt2$ and $\sum h^{2} = 1$ separately catches the error, which
is why the demonstration prints both.

---

## ★2 — Daubechies-4 from the algebraic form

$$h = \frac{1}{4\sqrt2}\Bigl[1+\sqrt3,\;\; 3+\sqrt3,\;\; 3-\sqrt3,\;\; 1-\sqrt3
\Bigr].$$

**Sum, by hand.** The $\sqrt3$ terms cancel:

$$\sum h = \frac{1}{4\sqrt2}\bigl[(1+3+3+1) + \sqrt3(1+1-1-1)\bigr]
= \frac{8}{4\sqrt2} = \frac{2}{\sqrt2} = \sqrt2 .$$

**Sum of squares, by hand.** Write $s = \sqrt3$. The four numerators are
$(1+s), (3+s), (3-s), (1-s)$, and

$$(1+s)^{2} + (1-s)^{2} = 2 + 2s^{2} = 2+6 = 8,$$
$$(3+s)^{2} + (3-s)^{2} = 2\cdot 9 + 2s^{2} = 18+6 = 24,$$
$$\sum (\text{numerators})^{2} = 8 + 24 = 32,$$

with denominator $(4\sqrt2)^{2} = 32$, so

$$\sum h^{2} = \frac{32}{32} = 1 .$$

Numerically: $h = [0.4829629131,\ 0.8365163037,\ 0.2241438680,\
-0.1294095226]$, $\sum h = 1.4142135624 = \sqrt2$ ✔ and $\sum h^{2} = 1.0000000000$
✔, as the demonstration prints.

---

## ★3 — Band edges for $f_s = 500\ \mathrm{Hz}$, $J = 4$

With $d_j = [f_s/2^{j+1}, f_s/2^{j})$ and $a_J = [0, f_s/2^{J+1})$:

| level | band (Hz) |
|---|---|
| $d_1$ | 125.000–250.000 |
| $d_2$ | 62.500–125.000 |
| $d_3$ | 31.250–62.500 |
| $d_4$ | 15.625–31.250 |
| $a_4$ | 0.000–15.625 |

Each detail band has the same relative width ($Q = 1$ between its edges) and the
bands tile the Nyquist interval exactly: the five bands above cover
$[0, 250)\ \mathrm{Hz}$ with no overlap and no gap, which is the multiresolution
property. Note that the *lower* levels have the *higher* frequencies, which is the
opposite of the numbering intuition; state the convention.

---

## ★4 — Scales and uncertainties with $\omega_0 = 6$

$$a = \frac{\omega_0}{2\pi f\Delta t} = \frac{6}{2\pi\times0.01}f^{-1}
= \frac{95.493}{f}:$$

| $f$ (Hz) | scale $a$ | measured bandwidth from $Q \approx 3.7$ (Hz) |
|---|---|---|
| 1 | 95.493 | 0.2703 |
| 5 | 19.099 | 1.3514 |
| 25 | 3.820 | 6.757 |

**Can a neighbour 0.2 Hz away be separated?**

- At 1 Hz: bandwidth 0.27 Hz > 0.2 Hz → **not separable**.
- At 5 Hz: bandwidth 1.35 Hz ≫ 0.2 Hz → **not separable**.
- At 25 Hz: bandwidth 6.76 Hz ≫ 0.2 Hz → **not separable**.

None of the three. The constant-$Q$ property means the absolute bandwidth grows
with frequency, so a fixed absolute separation becomes *harder* to resolve as
frequency rises — the inverse of the STFT's behaviour. To separate tones 0.2 Hz
apart at 25 Hz requires $Q = 125$; a Morlet wavelet with $\omega_0 = 6$ gives
$Q \approx 3.7$, so a larger $\omega_0$ (roughly $125/3.7 \approx 34$, with the
corresponding loss of time resolution) or a narrow-band method (a long STFT, or a
sinusoidal fit) is needed.

---

## ★5 — Cycles per analysis and the resolution limit at low frequency

$$\text{samples spanned} = \sigma_t f_s = \frac{0.6752}{f}f_s :$$

- at $f = 2\ \mathrm{Hz}$, $f_s = 100\ \mathrm{Hz}$:
  $0.6752\times100/2 = 33.76$ samples $= 0.338\ \mathrm{s}$;
- at $f = 20\ \mathrm{Hz}$: $0.6752\times100/20 = 3.376$ samples
  $= 0.0338\ \mathrm{s}$.

The *wavelet* is ten times shorter at 20 Hz than at 2 Hz, which is the scaling
$\psi_{a,b}(t) = a^{-1/2}\psi((t-b)/a)$ doing its job. The number of cycles is
constant: $\sigma_t f = 0.6752$ in both cases (in energy-RMS terms, about
two-thirds of a cycle), because the product $\sigma_t f$ is scale-invariant.

**Why 0.01 Hz cannot be resolved at 0.05 Hz.** At 0.05 Hz the same product gives
$\sigma_t = 0.6752/0.05 = 13.5\ \mathrm{s}$ and, from the measured $Q \approx 3.7$,
a bandwidth of $0.05/3.7 = 0.0135\ \mathrm{Hz}$ — larger than the 0.01 Hz
separation. A longer record does not help: the transform's bandwidth at a given
frequency is set by the *wavelet parameters* ($\omega_0$ and shape), not by the
record length. Only a different analysis (a longer wavelet, i.e. larger
$\omega_0$, or a full-record spectral method) changes it. This is the cleanest
illustration of the difference between *observation length* (which sets the
resolution of a transform of the whole record) and *analysing wavelet length*
(which sets the resolution of a time-frequency transform).

---

## ★6 — Energy fractions and spectral slope

Total energy $= 4.0 + 25.0 + 100.0 + 871.0 = 1000.0$.

Band edges at $f_s = 200\ \mathrm{Hz}$: $d_1 = [100, 200)$, $d_2 = [50, 100)$,
$d_3 = [25, 50)$, $a_3 = [0, 25)$.

| band | frequency range (Hz) | energy | fraction |
|---|---|---|---|
| $d_1$ | 100–200 | 4.0 | 0.004 |
| $d_2$ | 50–100 | 25.0 | 0.025 |
| $d_3$ | 25–50 | 100.0 | 0.100 |
| $a_3$ | 0–25 | 871.0 | 0.871 |

**Slope between adjacent detail bands** (each band is one octave wide):

$$10\log_{10}\frac{25}{4} = 7.96\ \mathrm{dB}, \qquad
10\log_{10}\frac{100}{25} = 6.02\ \mathrm{dB}.$$

So the energy falls at roughly $6$–$8\ \mathrm{dB}$ per octave as frequency
rises: a red spectrum.

**Why it could be misleading.** (i) The bands are octave-wide, so this is an
*octave-band* power spectrum (a constant-$Q$ representation), and its slope cannot
be compared directly with a $1/f^{\alpha}$ slope fitted to a fixed-bandwidth PSD
without converting the band widths. (ii) The approximation band $a_3$ covers
$[0,25)\ \mathrm{Hz}$ — four octaves — so its $87\%$ fraction is not evidence of a
peak below 25 Hz; it is what a wide band collects from any red spectrum. (iii) A
single trend or offset in the record lands entirely in $a_3$ and would produce a
slope that has nothing to do with the processes of interest.

---

## ★7 — Multiresolution denoising for three features (specification)

**Setup.** $f_s = 100\ \mathrm{Hz}$, $N = 16384$ ($163.84\ \mathrm{s}$). The three
features and their bands:

| feature | frequency | level at $f_s = 100\ \mathrm{Hz}$ |
|---|---|---|
| 0.5 Hz sinusoid, amplitude 2 | 0.5 Hz | $d_8$ = [0.391, 0.781) |
| 4 Hz dispersive arrival, amplitude 0.5 | near 4 Hz | $d_5$ = [3.125, 6.25) |
| noise | white | all bands |

Band arithmetic: $d_j = [100/2^{j+1}, 100/2^{j})$, so $d_5 = [3.125, 6.25)$ and
$d_6 = [1.5625, 3.125)$, $d_7 = [0.781, 1.5625)$, $d_8 = [0.39, 0.78)$ — a
$0.5\ \mathrm{Hz}$ component sits in **$d_8$**, and a $4\ \mathrm{Hz}$ arrival in
**$d_5$**.

**Transform and depth.** db4, periodic boundaries, and a decomposition deep enough
to isolate both features but not so deep that the threshold bites the signal:
**$J = 8$**. Rationale, calibrated on the lesson's measurement: the improvement
rose to a maximum at 3 of 5 levels and fell for deeper transforms, so choose the
depth at which both features have their own band and stop — here that is 8 levels,
with $d_8$ (the sinusoid), $d_5$ (the arrival) and $a_8 = [0,0.195)$ Hz carrying
little except trend.

**Threshold rule and estimator.**

$$\hat\sigma = \frac{\operatorname{median}(\lvert cD_1\rvert)}{0.6745},
\qquad \lambda = \hat\sigma\sqrt{2\ln N}, \qquad
T_{\text{soft}}(c) = \operatorname{sign}(c)\max(\lvert c\rvert - \lambda, 0).$$

Apply the shrinkage **to all detail bands except $d_5$ and $d_8$, and to
$a_8$ if a trend is expected there**, or apply it everywhere and accept the
attenuation of the two features — state which. The lesson's measured improvement
was about $5\ \mathrm{dB}$ overall at a comparable SNR, so the honest expectation
is "a few dB", not an order of magnitude.

**Expected improvement per band.** White noise of $\sigma = 1$ spread over 16384
samples contributes $\sigma^{2}\times$ (band width fraction) to each band:
$d_1$ (the top octave, half the band) holds about half the noise energy
($\approx 8192$), each successive band about half of the remainder. The
$0.5\ \mathrm{Hz}$ sinusoid of amplitude 2 has energy $2^{2}/2 \times N =
32768$ concentrated in one band, so its band SNR is far above the threshold and it
survives; the $4\ \mathrm{Hz}$ arrival of amplitude 0.5 is a *transient*, so its
energy is spread over $d_4$–$d_6$ (as the lesson's impulse measurement showed),
and the threshold will attenuate it.

**The feature at risk: the dispersive arrival.** Its energy is spread across
several detail bands, so a per-band threshold removes a fraction of it in each.
The diagnostic to compute: **the peak amplitude of the arrival in the
reconstructed record versus in the clean synthetic record**, before and after
denoising. If the ratio falls below, say, 0.9, the scheme is changing a
measurement that a later arrival-time analysis depends on — and the honest fix is
to exclude the bands the arrival occupies from the shrinkage, not to lower the
global threshold.

---

## ★8 — Diagnosing a $3\times10^{-3}$ reconstruction error

Order the tests so that each one isolates a hypothesis.

| # | hypothesis | test | expected signature |
|---|---|---|---|
| 1 | **single-precision accumulation** | repeat in `float64` and compare; also compute the condition of the transform (it is orthogonal, so its condition number is 1) | error falls to $\sim10^{-15}$ in double precision. **If it does, the cause is rounding and nothing else** — the fastest discriminator |
| 2 | **wrong filter coefficient** | check the four orthonormality identities: $\sum h$, $\sum h^{2}$, $\sum h[n]h[n+2]$, $\sum h[n]g[n+2]$ | a mistyped coefficient breaks $\sum h^{2} = 1$ and the orthogonality sums by $\sim10^{-2}$–$10^{-1}$, far larger than the reconstruction error itself |
| 3 | **wrong synthesis alignment** | reconstruct a *single* impulse; compare with the impulse | an alignment error produces a *shifted or mirrored* reconstruction, so the error appears as a displaced spike with the same total energy — and it appears even for Haar, where no coefficient can be wrong |
| 4 | **boundary or buffer-length error** | reconstruct a signal that is zero except near one end; also vary $N$ (non-power-of-two, odd) | errors concentrated at the record ends, or an error that changes discontinuously as $N$ crosses a multiple of $2^{J}$ |

**Which is invisible in the energy-partition test.** The **alignments of the two
filters relative to each other** can be wrong in a way that preserves energy:
if $g$ is replaced by a shift of itself, the pair may remain orthonormal in the
sense of the four identities (energy still conserved, hence
$\sum x^{2} = \sum cA^{2}+\sum cD^{2}$ holds to rounding) while reconstruction
places the highpass content at the wrong times. The energy test cannot see it; the
impulse test in row 3 catches it immediately, which is why an implementation
should be validated with **both** a random signal (energy and reconstruction) and
an impulse (time alignment). Adding a *known* signal with a known answer — a sine
that must land in exactly one band — is the third test, and it checks the band
assignment numerics rather than the algebra.


---

## Mastery checkpoint answers

**(b)** $h = [1+\sqrt3,\,3+\sqrt3,\,3-\sqrt3,\,1-\sqrt3]/(4\sqrt2)$; the
$\sqrt3$ terms cancel in $\sum h$, giving $8/(4\sqrt2) = \sqrt2$, and
$\sum h^{2} = 32/(4\sqrt2)^{2} = 1$ exactly (the arithmetic is worked in ★2).

**(d)** $a = 10$, $\Delta t = 0.01\ \mathrm{s}$, $\omega_0 = 6$:

$$f = \frac{\omega_0}{2\pi a\Delta t} = \frac{6}{2\pi\times10\times0.01}
= 9.549\ \mathrm{Hz}.$$

With the measured $Q \approx 3.7$ the bandwidth is
$9.549/3.7 = 2.58\ \mathrm{Hz}$ — so "9.5 Hz" must be reported as
$9.5\pm2.6\ \mathrm{Hz}$ (in the sense of a $-3\ \mathrm{dB}$ band), not as a
frequency to three figures.

**(f)** For $f_s = 1\ \mathrm{Hz}$ the sixth-level approximation band is
$a_6 = [0,\,1/2^{7}) = [0,\,0.0078)\ \mathrm{Hz}$, which does not contain
$0.03\ \mathrm{Hz}$: the quoted level and the quoted frequency are inconsistent.
$0.03\ \mathrm{Hz}$ lies in $d_5 = [1/2^{6},\,1/2^{5}) =
[0.0156,\,0.0313)\ \mathrm{Hz}$. The correct statement is "the energy in the
$0.0156$–$0.0313\ \mathrm{Hz}$ band is $X$", which is testable, rather than a
frequency without a width.
