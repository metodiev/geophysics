# Solutions — 20-02-03 Window Functions and Spectral Leakage Control

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [03 Window Functions and Spectral Leakage Control](../03-windowing-advanced.md).

---

## ★1 — The four metrics

| metric | one-sentence meaning | what it costs |
|---|---|---|
| **coherent gain** | the mean of the window, i.e. the factor by which an on-bin tone's amplitude is scaled | an amplitude bias unless divided out |
| **ENBW** | the width, in bins, of a rectangular filter passing the same white-noise power | variance: $\operatorname{Var}\propto\text{ENBW}$ |
| **highest sidelobe level** | the largest sidelobe of the window's transform, in dB below the main lobe | dynamic range: how strong a nearby tone can contaminate a weak bin |
| **scalloping loss** | the worst-case amplitude a bin reading under-reports for an off-bin tone | a systematic amplitude error up to $-3.92\ \mathrm{dB}$ |

Two more that a complete report includes: the **sidelobe decay rate** (a single
sidelobe number does not describe leakage at a distance — Hamming versus Hann),
and the **worst-case process loss** = coherent gain × scalloping.

---

## ★2 — Resolution and ENBW for a Blackman window

$N = 8192$, $f_s = 512\ \mathrm{Hz}$:

$$\Delta f = \frac{f_s}{N} = \frac{512}{8192} = 0.0625\ \mathrm{Hz}.$$

Blackman: 3-dB bandwidth $0.828$ bins, ENBW $1.7268$ bins.

$$\text{3 dB resolution} = 0.828\times0.0625 = 0.05175\ \mathrm{Hz},$$

$$\text{ENBW} = 1.7268\times0.0625 = 0.107925\ \mathrm{Hz}.$$

Hann: 3-dB bandwidth $0.719$ bins $= 0.04494\ \mathrm{Hz}$, ENBW
$1.5\times0.0625 = 0.09375\ \mathrm{Hz}$.

**Which for a $5\ \mathrm{Hz}$ requirement?** Both are about a factor of 100
better than needed — the requirement is met with enormous margin, so the
resolution is not the binding constraint. Hann is the better choice *on the
numbers*: narrower main lobe ($0.045$ against $0.052\ \mathrm{Hz}$) and lower
ENBW ($0.094$ against $0.108\ \mathrm{Hz}$, i.e. $13\%$ less variance). Blackman
would only be preferred if leakage mattered, and at 10 bins Blackman measured
$-76.4\ \mathrm{dB}$ against Hann's $-68.5\ \mathrm{dB}$: $8\ \mathrm{dB}$ of
extra dynamic range for $35\%$ more variance and a wider lobe. That is the trade
to state.

---

## ★3 — Correcting a Hann-windowed amplitude

Measured peak $= 0.42\ \mathrm{V}$.

**On-bin correction:** divide by the coherent gain,
$0.42/0.5 = 0.84\ \mathrm{V}$.

**Range admitted by scalloping.** The Hann window's worst-case scalloping loss is
$-1.42\ \mathrm{dB}$, i.e. a factor $10^{-1.42/20} = 0.8488$ (the measured
value at a half-bin offset). If the tone is half a bin off, the true amplitude is

$$\frac{0.42}{0.5\times0.8488} = 0.9896\ \mathrm{V}.$$

So the reading $0.42\ \mathrm{V}$ is consistent with a true amplitude between
$0.84$ and $0.99\ \mathrm{V}$ — a $45\%$ range — purely from the unknown bin
offset. **If an amplitude to better than that is needed: use a flat-top window,
whose measured scalloping loss is $-0.01\ \mathrm{dB}$ (a $0.1\%$ range), or
interpolate the peak with a three-point parabola.** Both cost resolution.

---

## ★4 — Deriving the ENBW

**Definition.** For a window $w[n]$ of length $N$,

$$\mathrm{ENBW} = \frac{N\sum_n w^{2}[n]}{\left(\sum_n w[n]\right)^{2}}
\ \text{(in bins)} .$$

It is the width of the rectangular band that passes the same white-noise power as
the window, and it is the factor by which the windowed estimate's variance exceeds
the unwindowed one.

**Hann, from the definition.** With $w[n] = 0.5 - 0.5\cos(2\pi n/N)$:

$$\sum_{n=0}^{N-1}w[n] = 0.5N - 0.5\underbrace{\sum_{n=0}^{N-1}\cos\frac{2\pi n}{N}}_{0}
= \frac{N}{2},$$

$$\sum_{n=0}^{N-1}w^{2}[n] = \sum_n\left(\frac14 - \frac12\cos\frac{2\pi n}{N}
+ \frac14\cos^{2}\frac{2\pi n}{N}\right)
= \frac{N}{4} + 0 + \frac{N}{8} = \frac{3N}{8},$$

using $\sum\cos = 0$ and $\sum\cos^{2}(2\pi n/N) = N/2$ for $N \ge 3$. Hence

$$\mathrm{ENBW} = N\frac{3N/8}{(N/2)^{2}} = \frac{3N^{2}/8}{N^{2}/4} = 1.5\ \text{exact}$$

(the measured $1.500000$).

**General cosine-sum window** $w[n] = a_0 - a_1\cos(2\pi n/N)
+ a_2\cos(4\pi n/N)$: the cross terms average to zero over a whole number of
periods, and each $\cos^{2}(2\pi kn/N)$ averages to $1/2$, so

$$\sum_n w = a_0N, \qquad
\sum_n w^{2} = \left(a_0^{2} + \frac{a_1^{2}}{2}
+ \frac{a_2^{2}}{2}\right)N,$$

$$\boxed{\ \mathrm{ENBW} = \frac{a_0^{2} + \frac12 a_1^{2}
+ \frac12 a_2^{2}}{a_0^{2}}\ }.$$

**Check against the measurements.**

| window | $(a_0, a_1, a_2)$ | formula | measured |
|---|---|---|---|
| Hann | $(0.5, 0.5, 0)$ | $\dfrac{0.25+0.125}{0.25} = 1.5$ | 1.500000 |
| Hamming | $(0.54, 0.46, 0)$ | $\dfrac{0.2916+0.1058}{0.2916} = 1.36283$ | 1.362826 |
| Blackman | $(0.42, 0.5, 0.08)$ | $\dfrac{0.1764+0.125+0.0032}{0.1764} = 1.72676$ | 1.726757 |

The formula is exact for a periodic window; the residuals ($10^{-5}$) are the
one-sample difference between the symmetric and periodic conventions
(`sym=True` against `sym=False`).

**Note on units.** The result is in bins of $1/N$; in hertz it is
$\mathrm{ENBW}\times f_s/N$. A noise level quoted per bin and one quoted per hertz
differ by exactly this factor, which is why reporting the window without its ENBW
leaves a noise level unverifiable.

---

## ★5 — Separating two tones 3 bins apart

Using the exact phase-averaged construction
$\lvert W(f-f_1)\rvert^{2} + \lvert W(f-f_2)\rvert^{2}$, the dip between the peaks
at a 3-bin separation is:

| window | dip at 3 bins (dB) | meets $-10\ \mathrm{dB}$? |
|---|---|---|
| rectangular | deep (below the numerical floor) | yes |
| Hamming | $-31.81$ | yes |
| Hann | $-24.78$ | yes |
| Kaiser $\beta = 8.6$ | $-15.30$ | yes |
| Blackman | $-15.22$ | yes |
| flat-top | $-0.47$ | **no** |

So every window except the flat-top separates the pair at the required depth.

**Why the ordering is not the ordering by 3-dB bandwidth.** The 3-dB bandwidth
ranks rectangular (0.438) < Hamming (0.656) < Hann (0.719) < Kaiser (0.812) <
Blackman (0.828) < flat-top (1.859). At a 3-bin separation the dip also depends on
the *shape of the sidelobes*: Hamming's first sidelobe is higher than Hann's but
its main lobe is narrower, and the dip is set by the sum of the two main lobes
plus the contribution of the first sidelobes of the opposite tone. Hamming's
narrower main lobe wins at this separation, which is why the ordering differs from
the bandwidth ordering between the two cosine windows.

**The general lesson.** A resolution number is only meaningful together with the
criterion (dip depth, Rayleigh half-width, 3-dB width) and the two-tone phase
convention. State all three.

---

## ★6 — Detecting a weak tone at $-60\ \mathrm{dB}$

Weak/strong amplitude ratio $= 1\times10^{-3}$, so the weak tone's peak power is
$10^{-6}$ of the strong tone's. A 3 dB detection margin requires

$$10^{-6} \ge 2\times10^{\text{floor}/10}
\;\Longrightarrow\;
\text{floor} \le -63.0\ \mathrm{dB}.$$

| window | floor at 20 bins (dB) | detectable? |
|---|---|---|
| rectangular | $-35.9$ | no |
| Hamming | $-53.3$ | no |
| Kaiser $\beta = 8.6$ | $-85.0$ | yes |
| Hann | $-88.9$ | yes |
| flat-top | $-94.3$ | yes |
| Blackman | $-96.5$ | yes |

**Detection limit for the best window (Blackman, $-96.5\ \mathrm{dB}$).** The
weakest detectable amplitude ratio is

$$\sqrt{2\times10^{-9.65}} = \sqrt{4.47\times10^{-10}} = 2.11\times10^{-5},$$

i.e. $-93.5\ \mathrm{dB}$ in amplitude — about two orders of magnitude weaker than
the Hann case and nearly three than the rectangular case at the same frequency.
Blackman's advantage is not its first sidelobe ($-58.1\ \mathrm{dB}$, worse than
Kaiser's $-63.3$) but its decay: at 20 bins it holds $-96.5\ \mathrm{dB}$ where
Kaiser holds $-85.0\ \mathrm{dB}$.

**Caveat to state.** These are single-tone floors. With several strong
components, leakage adds incoherently and the effective floor rises by roughly
$10\log_{10}M$ for $M$ comparable strong tones; the honest answer quotes the
assumed number of strong components.

---

## ★7 — Three requirements, one recipe (specification)

Requirements: (i) resolve two tones $0.4\%$ apart; (ii) detect a tone
$-70\ \mathrm{dB}$ below a strong neighbour 10 bins away; (iii) measure an
isolated tone's amplitude to $2\%$.

**Requirement (i) fixes the record length.** A $0.4\%$ separation at frequency
$f$ is $0.004f$. To resolve it, the 3-dB resolution must be smaller, say by a
factor 2: $\text{BW}_{3\,\mathrm{dB}}/\text{bin}\times\Delta f \le 0.002f$. With
Hann ($0.719$ bins), $\Delta f \le 0.00278f$, so $N \ge f_s/(0.00278f) = 360\,f_s/f$
samples. At $f = 10\ \mathrm{Hz}$ and $f_s = 100\ \mathrm{Hz}$, $N \ge 3600$.

**Requirement (ii) fixes the window.** $-70\ \mathrm{dB}$ of leakage suppression
at 10 bins: from the measured table, Hann gives $-68.5\ \mathrm{dB}$ (marginally
short), Blackman and Kaiser 8.6 give $-76$ to $-79\ \mathrm{dB}$ (comfortable).
Choose **Blackman** (or Kaiser $\beta = 8.6$). This contradicts requirement (i)'s
preference for Hann and requirement (iii)'s preference for flat-top.

**Requirement (iii) fixes the window again, and conflicts.** A $2\%$ amplitude
accuracy from a single bin read requires scalloping loss $\le 2\%$: the
rectangular window ($-3.92\ \mathrm{dB} = 36\%$) and Hann
($-1.42\ \mathrm{dB} = 15\%$) fail; Blackman ($-1.10\ \mathrm{dB} = 11\%$) fails;
Kaiser $\beta = 8.6$ ($-1.11\ \mathrm{dB}$) fails; only a flat-top
($-0.01\ \mathrm{dB}$) passes — or a Blackman spectrum whose peak is *interpolated*
rather than read at a bin.

**Verdict: the three requirements cannot all be met with one window.**
Requirement (ii) needs a low-sidelobe decaying window; (iii) needs a flat-top or a
peak interpolation; (i) merely needs enough record. The two viable designs are:

1. **Two passes.** Produce the detection spectrum with Blackman (requirement ii)
   and the amplitude spectrum with a flat-top plus a peak interpolation
   (requirement iii); state both windows and both ENBWs. Cost: two analyses, two
   variance figures.
2. **One pass with interpolation.** Use Blackman (satisfying ii), interpolate the
   peak with a three-point parabola using Blackman's own scalloping curve, which
   reduces the worst-case amplitude error from $11\%$ to about $1\%$ when the SNR
   is high (satisfying iii in practice, not by construction). Cost: the $1\%$
   guarantee becomes SNR-dependent, and the honest report says so.

**Which requirement dominates?** (ii), because it is the only one that cannot be
recovered by a longer record: resolution and amplitude accuracy both improve with
more data or with post-processing, while a leakage floor is a property of the
window alone.

---

## ★8 — Windowing a segment too short for the lowest frequency

**The setup.** Hann window on 64-sample segments at $f_s = 100\ \mathrm{Hz}$, so
each segment is $0.64\ \mathrm{s}$ long, $\Delta f = f_s/N = 1.5625\ \mathrm{Hz}$,
and the claim is a spectrum down to $0.5\ \mathrm{Hz}$.

**What happens to a $0.5\ \mathrm{Hz}$ component.** It sits at
$0.5/1.5625 = 0.32$ bins — *inside the main lobe of the DC bin*. Measured for a
unit-amplitude $0.5\ \mathrm{Hz}$ cosine windowed by Hann over 64 samples
(amplitudes normalised by $\sum_n w[n] = 0.5N$):

| bin | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| level | 0.5014 | 0.3332 | 0.0509 | 0.0105 |

The component's energy is smeared across the low bins, and the value at bin 0 is
$0.5014$ — the coherent gain ($0.5000$) to within $0.3\%$. In other words **the
component is indistinguishable from a DC offset of $0.5$** in this estimate. Its
frequency cannot be measured (it is below the resolution by a factor of 3), and
its amplitude appears in the DC bin where a real offset would also appear.

**How much of it a detrending step would remove.** The mean of the 64 samples of
$\cos(2\pi\cdot0.5t)$ is $0.461125$ (only $0.32$ of a cycle fits), and removing
the mean reduces the bin-0 reading from $0.5014$ to $0.0402$ — that is, $92\%$ of
the apparent level was the *trend*, not the oscillation. Any pipeline that
detrends will therefore delete this component before the analysis.

**Minimum segment length.** To make the window transparent to a component of
frequency $f_{\min}$, the segment must contain several periods:

$$L \ge m\,\frac{f_s}{f_{\min}}, \qquad m \approx 5\text{–}10 .$$

For $f_{\min} = 0.5\ \mathrm{Hz}$, $f_s = 100\ \mathrm{Hz}$: $L \ge 5\times100/0.5
= 1000$ samples ($10\ \mathrm{s}$) at $m = 5$, or $2000$ samples ($20\ \mathrm{s}$)
at $m = 10$. The corresponding $\Delta f$ is $0.1\ \mathrm{Hz}$ (or
$0.05\ \mathrm{Hz}$), which resolves $0.5\ \mathrm{Hz}$ by 5 (or 10) bins.

**The general rule.** *The segment, not the record, must be long compared with the
lowest period of interest.* Segmentation buys variance at the cost of the lowest
frequency the estimator can see, and that cost must be computed before the
analysis — a 64-sample segment at $100\ \mathrm{Hz}$ cannot report anything about
$0.5\ \mathrm{Hz}$, no matter how many segments are averaged.


---

## Mastery checkpoint answers

**(b)** $N = 8192$, $f_s = 512\ \mathrm{Hz}$: $\Delta f = 0.0625\ \mathrm{Hz}$.
Blackman's measured 3-dB bandwidth is $0.828$ bins, so the resolution is
$0.828\times0.0625 = 0.05175\ \mathrm{Hz}$, and its ENBW is
$1.7268\times0.0625 = 0.107925\ \mathrm{Hz}$.

**(d)** With a 3-bin separation the measured phase-averaged dips are: rectangular
deep, Hamming $-31.8\ \mathrm{dB}$, Hann $-24.8\ \mathrm{dB}$, Kaiser $8.6$
$-15.3\ \mathrm{dB}$, Blackman $-15.2\ \mathrm{dB}$, flat-top
$-0.5\ \mathrm{dB}$. The criterion is "dip $\le -10\ \mathrm{dB}$ relative to
the taller peak, averaged over the two tones' relative phase": every window
qualifies **except the flat-top**.

**(f)** For $1\%$ amplitude accuracy at an unknown bin offset, only the flat-top
qualifies (measured scalloping $-0.01\ \mathrm{dB}$; Hann is $-1.42\ \mathrm{dB}$
and rectangular $-3.92\ \mathrm{dB}$). Its cost: ENBW $3.77$ bins
($3.77\times$ the rectangular window's variance) and a two-tone resolution worse
than 4 bins, versus 1.10 bins for the rectangular window.
