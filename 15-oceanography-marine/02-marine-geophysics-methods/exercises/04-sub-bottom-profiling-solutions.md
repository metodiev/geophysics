# Solutions — 15-02-04 Sub-Bottom Profiling and Chirp Systems

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [04 Sub-Bottom Profiling](../04-sub-bottom-profiling.md).

---

## ★1 — Chirp parameters and resolution

$$B = f_1 - f_0 = 8.0 - 1.0 = 7.0\ \mathrm{kHz}, \qquad
\frac{B}{T} = \frac{7000}{0.015} = 4.667\times10^{5}\ \mathrm{Hz\,s^{-1}},$$

$$BT = 7000 \times 0.015 = 105, \qquad
\Delta z = \frac{c}{2B} = \frac{1700}{2 \times 7000} = 0.1214\ \mathrm{m}.$$

A $12\ \mathrm{cm}$ resolution in a sediment — centimetric, and roughly a hundred
times finer than a marine reflection survey's at the same depth. **Note that the
duration does not appear in the resolution**: the sweep rate and 105-cycle product
set the gain, not the resolving power.

---

## ★2 — Samples and processing gain

$$N = T F_s = 0.015 \times 100000 = 1500\ \mathrm{samples},$$

$$G = 10\log_{10}N = 10\log_{10}(1500) = 31.76\ \mathrm{dB}.$$

Equivalently $10\log_{10}(BT) + 10\log_{10}[(F_s/2)/B] + 10\log_{10}2
= 20.21 + 8.54 + 3.01 = 31.76\ \mathrm{dB}$. ✔ The three terms must sum to the
same number, which is a useful arithmetic check on a system budget.

---

## ★3 — Which contribution is chirp-specific

**Only the first: the compression gain $10\log_{10}(BT)$.**

- $10\log_{10}[(F_s/2)/B]$, the rejection of noise outside the signal band, is
  available to **any** filter whose noise bandwidth is matched to a signal
  occupying a fraction of the sampled band. A narrow-band CW system gets it too.
- $10\log_{10}2$, the peak-to-rms factor of the compressed main lobe, is a
  **definitional** artefact of quoting the output as a peak while the input is
  quoted as an rms. Changing either definition removes it.

So of a quoted $31.8\ \mathrm{dB}$ of "chirp gain", $20.2\ \mathrm{dB}$ is the
chirp, $8.5\ \mathrm{dB}$ is filtering and $3.0\ \mathrm{dB}$ is bookkeeping.
Reporting the total as a chirp property over-states the method by $11.5\
\mathrm{dB}$.

---

## ★★4 — Derivation of $G = \sqrt{N}$

Let the replica be $s_k$, $k = 0\ldots N-1$, with $a^{2} = \frac{1}{N}\sum_k
s_k^{2}$ its mean square, and let the noise be white with standard deviation
$\sigma$.

**Signal peak.** At zero lag the correlator sums the products of the signal with
itself, sample by sample and all in phase:

$$C_{\text{sig}} = \sum_k s_k^{2} = N a^{2}.$$

**Noise standard deviation.** The correlator is linear, so the noise at one output
sample is $\sum_k n_k s_k$, a sum of $N$ independent zero-mean terms with
variances $\sigma^{2}s_k^{2}$. Hence

$$\sigma_C^{2} = \sigma^{2}\sum_k s_k^{2} = \sigma^{2} N a^{2}
\qquad\Longrightarrow\qquad
\sigma_C = \sigma\,a\sqrt{N}.$$

**Ratio.** With the lesson's definitions,

$$\mathrm{SNR}_{\text{out}} = \frac{C_{\text{sig}}}{\sigma_C}
= \frac{N a^{2}}{\sigma a \sqrt{N}}
= \sqrt{N}\,\frac{a}{\sigma}
= \sqrt{N}\,\mathrm{SNR}_{\text{in}} . \ ✔$$

**Consequences.** The gain depends only on the number of samples in the pulse,
i.e. on $T F_s$, and not on the amplitude $a$ or the noise level $\sigma$ — which
is why the demonstration's measured gain is constant across three noise levels.
It also means a longer duration at the same bandwidth gains more, with no cost in
resolution.

---

## ★★5 — Penetration at two frequencies

$$R = \frac{\mathrm{DR}}{2\alpha}, \qquad \alpha(f) = 0.10 f_{\mathrm{kHz}}.$$

| $f$ (kHz) | $\alpha$ (dB m$^{-1}$) | $R$ at DR $=60$ dB |
|---|---|---|
| 3 | 0.300 | $60/(0.6) = 100.0\ \mathrm{m}$ |
| 6 | 0.600 | $60/(1.2) = 50.0\ \mathrm{m}$ |

**The trade:** a factor 2 in frequency halves the penetration at fixed dynamic
range, while (through the bandwidth) it improves the resolution — so resolution
and penetration are bought with the same currency and the exchange rate is set by
the sediment's attenuation law.

---

## ★★6 — Taper choice

**(a)** $\Delta z = c\,\mathrm{FWHM}/2$ with $c = 1600\ \mathrm{m\,s^{-1}}$:

$$0.2900\ \mathrm{ms}: \quad \frac{1600 \times 2.900\times10^{-4}}{2}
= 0.2320\ \mathrm{m},$$

$$0.5500\ \mathrm{ms}: \quad \frac{1600 \times 5.500\times10^{-4}}{2}
= 0.4400\ \mathrm{m}.$$

**(b)** The reflectors are $0.35\ \mathrm{m}$ apart. The rectangular chirp's
resolution, $0.232\ \mathrm{m}$, is comfortably below the separation; the Hann
taper's, $0.440\ \mathrm{m}$, is above it. **Choose the rectangular chirp** — but
only if the two reflectors are of comparable amplitude. If one of them is much
weaker, the $-13.6\ \mathrm{dB}$ rectangular side lobes will produce false peaks
that the Hann taper would suppress, and the answer flips. The honest decision rule
is therefore two-part: resolve if $\Delta z < $ separation, and prefer the taper if
the amplitude contrast between the events shown exceeds about $15\ \mathrm{dB}$.

---

## ★★7 — Detectability

Unprocessed echo level after all losses:

$$\mathrm{EL}_0 = 45 - \underbrace{2(0.5)(35)}_{\text{attenuation}}
- \underbrace{22}_{\text{reflection}} = 45 - 35 - 22 = -12\ \mathrm{dB}.$$

After the matched filter:

$$\mathrm{EL} = -12 + 33 = +21\ \mathrm{dB}.$$

The required margin is $8\ \mathrm{dB}$, so the target is detectable with $13\
\mathrm{dB}$ to spare. **The chirp changes the answer from "impossible" to
"comfortable"**: a $\mathrm{CW}$ pulse of the same energy would carry no
processing gain in the compression term and would leave the target $12\ \mathrm{dB}$
*below* the noise.

---

## ★★★8 — Resolving a 0.3 m layer at 25 m

**Required bandwidth.** $\Delta z = c/(2B) < 0.3\ \mathrm{m}$ with
$c = 1700\ \mathrm{m\,s^{-1}}$:

$$B > \frac{c}{2\Delta z} = \frac{1700}{0.6} = 2833\ \mathrm{Hz}
\;\Longrightarrow\; B \gtrsim 2.9\ \mathrm{kHz}.$$

**Required frequency band.** To penetrate $25\ \mathrm{m}$ twice (down and up, so
$50\ \mathrm{m}$ of two-way path) within a dynamic range DR:

$$2\alpha(25) \le \mathrm{DR} - \mathrm{reflection\ loss}
\;\Longrightarrow\; \alpha \le \frac{\mathrm{DR} - 20}{50}$$
(with $20\ \mathrm{dB}$ reserved for the reflection coefficient and the margin). For
$\mathrm{DR} = 60\ \mathrm{dB}$: $\alpha \le 0.8\ \mathrm{dB\,m^{-1}}$, i.e.
$f \le 8\ \mathrm{kHz}$ under the lesson's linear law. For $\mathrm{DR} = 40\
\mathrm{dB}$: $\alpha \le 0.4\ \mathrm{dB\,m^{-1}}$, i.e. $f \le 4\ \mathrm{kHz}$.

**The implied band.** Combining, the band must fall in roughly
$2\ \mathrm{kHz}$–$5\ \mathrm{kHz}$ to get $2.9\ \mathrm{kHz}$ of bandwidth below
$4$–$8\ \mathrm{kHz}$: a $2.0$–$5.0\ \mathrm{kHz}$ sweep, $B = 3\ \mathrm{kHz}$,
$\Delta z = 0.283\ \mathrm{m}$, marginal.

**Which constraint binds.** **Bandwidth**, jointly with **attenuation**: the
bandwidth requirement pushes the upper frequency up, and the attenuation
requirement pushes it down, and they meet. Energy is the next constraint — the
marginal resolution needs a longer sweep, which costs nothing in resolution but
requires a source able to transmit it and a system able to handle the
time–bandwidth product. **Side lobes are the least binding** here: at $0.283\
\mathrm{m}$ of resolution against a $0.3\ \mathrm{m}$ target the margin is thin,
and a Hann taper's $1.9\times$ widening is unaffordable — so the answer is to use
a rectangular (or very lightly tapered) chirp and accept the side lobes.

**Executable specification.** A $2.0$–$5.0\ \mathrm{kHz}$ linear chirp of
$25\ \mathrm{ms}$ ($BT = 75$, $N = 2500$ at $100\ \mathrm{kHz}$,
gain $34.0\ \mathrm{dB}$), rectangular taper, towed so that the target lies within
$25\ \mathrm{m}$ of the seabed, with the record stacked over a few pings to recover
the remaining margin. The report should state that the resolution is
$0.283\ \mathrm{m}$ at the target depth, not at the seabed.

---

## ★★★9 — Measured FWHM against the half-power bandwidth

**The discrepancy.** At $30\ \mathrm{m}$ of path the half-power bandwidth of the
surviving spectrum is about $0.5\ \mathrm{kHz}$ (the high frequencies are
$24\ \mathrm{dB}$ down, so the $-3\ \mathrm{dB}$ point is reached quickly), which
predicts a resolution of about $1.6\ \mathrm{m}$ — a factor 8 worse than the
seabed value of $0.20\ \mathrm{m}$. The demonstration measures only a factor
$1.6$ (FWHM $0.2900 \to 0.4700\ \mathrm{ms}$).

**Why.** The half-power bandwidth discards a *great deal* of still-useful
information. The surviving spectrum has a steep exponential roll-off, so it
retains appreciable amplitude well above the half-power point: components
$20\ \mathrm{dB}$ down still contribute to the correlation peak, and it is the
*extent* of the spectrum rather than its half-power width that sets the main-lobe
width of an autocorrelation. Formally, the compressed main-lobe width is
approximately the reciprocal of the total extent of the passband, not of its
half-power width; for a spectrum that decays as $e^{-\gamma f}$ the effective
extent grows only logarithmically with attenuation, which is why the measured
degradation is so much milder than the half-power estimate.

A second, smaller contribution: the demonstration matches the replica to the
attenuated waveform, which is the optimistic case; a fixed replica would add a
mismatch loss and broaden the peak further.

**What to quote.** The **measured compressed FWHM** for the *expected* path —
converted to a resolution through $c\,\mathrm{FWHM}/2$ — together with the
processing actually used. The half-power bandwidth is a convenient way to *bound*
the degradation and to see the mechanism, but it is a lower bound on the
resolution, not an estimate of it. Quoting it as an estimate makes the method look
several times worse than it is, and quoting a single seabed resolution makes it
look several times better than it is.
