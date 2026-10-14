# Solutions — 20-05-04 Noise Reduction Strategies in Practice

> Read after attempting. Numbers computed. Lesson:
> [04 Noise Reduction](../04-noise-reduction.md).

---

## ★1 — The stacking gain

$$G = \sqrt{M} = \sqrt{64} = 8 \;\Longrightarrow\;
20\log_{10}8 = 18.06\ \mathrm{dB},
\quad\text{equivalently } 10\log_{10}64 = 18.06\ \mathrm{dB}.$$

The condition is that the **noise is incoherent between records** (independent,
zero-mean) while the signal is common to all of them. Coherent noise gains
nothing from averaging.

---

## ★2 — SNR in dB

$$\mathrm{SNR} = 20\log_{10}\frac{0.20}{0.05} = 20\log_{10}4 = 12.04\ \mathrm{dB}.$$

Halving the signal rms divides the ratio by 2, which is
$20\log_{10}(1/2) = -6.02\ \mathrm{dB}$. The new SNR is $6.02\ \mathrm{dB}$.

---

## ★3 — Coherent noise in a stack

The harmonic is **reproduced exactly** by the average (its amplitude is
unchanged, while the incoherent part falls as $1/\sqrt{M}$), so the stack
converges to signal plus harmonic. In the demonstration the $M = 100$ stack
gained $7.98\ \mathrm{dB}$ instead of the expected $20.00\ \mathrm{dB}$.

Remedies: notch-filter or model-and-subtract the harmonic before stacking;
remove it with a coherency-based multichannel filter; or record with an
instrument and layout that suppresses the common-mode coupling in the first
place.

---

## ★★4 — Choosing a passband on the $D$ column

From the table, the bands with $D < 0.2$ are:

| passband | output SNR | $D$ | FWHM |
|---|---|---|---|
| 5–100 Hz | $+6.14$ dB | 0.0345 | 40.0 ms |
| 5–40 Hz | $+10.40$ dB | 0.0836 | 40.0 ms |
| 10–30 Hz | $+11.91$ dB | 0.3313 | 56.0 ms (exceeds $D<0.2$) |

The best compromise satisfying $D < 0.2$ is the **5–40 Hz** band:
$+10.40\ \mathrm{dB}$ at $D = 0.084$, with the pulse width unchanged at 40 ms.
It delivers $+10.4 - 6.02 = 4.4\ \mathrm{dB}$ of net improvement over the input.

A study needing $D < 0.05$ is restricted to the widest band tested,
5–100 Hz, which gives only $+6.14\ \mathrm{dB}$ — an improvement of just
$0.12\ \mathrm{dB}$ over the input. In that regime filtering is not the lever to
use; stacking is.

---

## ★★5 — The Wiener weight

$$H(f) = \frac{S_{ss}}{S_{ss}+S_{nn}}
= \frac{4S_{nn}}{4S_{nn}+S_{nn}} = \frac{4}{5} = 0.8 .$$

Attenuation $= 20\log_{10}0.8 = -1.94\ \mathrm{dB}$. The filter passes 80% of the
amplitude where the signal power dominates 4:1 — it never passes 100% unless the
noise is zero, which is why the Wiener filter always leaves a small bias.

---

## ★★6 — The price of the median

For Gaussian noise,
$\operatorname{Var}(\text{median})/\operatorname{Var}(\text{mean}) = \pi/2$,
so

$$\frac{\operatorname{sd}(\text{median})}{\operatorname{sd}(\text{mean})}
= \sqrt{\pi/2} = 1.2533 .$$

The SNR penalty is $20\log_{10}(1/1.2533) = -1.96\ \mathrm{dB}$ — a loss of
about $2\ \mathrm{dB}$ in SNR, or equivalently the median of 25 records is only
as good as the mean of $25/(\pi/2) = 15.9$ records.

**What pays for it.** Bounded influence: in the demonstration, a single-sample
spike in 30% of the records raised the mean's peak error to $0.0267$ against the
clean-record floor of $0.0114$ (a factor of $2.3$), while the median stayed at
$0.0175$ and a 10% trimmed mean at $0.0135$. Two decibels is a small price for
that protection.

---

## ★★★7 — A noise-reduction budget

**Target.** $+20\ \mathrm{dB}$ from an input of $0\ \mathrm{dB}$.

**Lever 1 — stacking.** $M$ records with incoherent noise give
$10\log_{10}M$ dB. Choose $M = 64$: $+18.06\ \mathrm{dB}$.

**Lever 2 — filtering.** The remaining $1.94\ \mathrm{dB}$ is to come from a
band-pass. From the table the 5–40 Hz band gives $+10.4\ \mathrm{dB}$ of SNR at
$D = 0.084$ — comfortably more than needed, so choose a wider, gentler band:
5–60 Hz would give roughly $+7\ \mathrm{dB}$ at $D \approx 0.05$, more than the
shortfall and less distorting.

**Budget.**

| step | contribution | cumulative |
|---|---|---|
| input | — | $0.00$ dB |
| filter (5–60 Hz, $D\approx0.05$) | $+7.0$ dB | $+7.0$ dB |
| stack 64 records | $+18.06$ dB | $+25.1$ dB |

**Estimator.** Mean (the noise is band-limited Gaussian, no outliers expected).
If spikes are possible, a 10% trimmed mean costs about $1\ \mathrm{dB}$ and is
worth it.

**Assumptions to state.** The signal is repeatable and aligned across the 64
records; the noise is incoherent between them; the noise is not strongly
coloured below the passband (otherwise
[03 Colour of Noise](../03-noise-colour.md) adds a surviving low-frequency
term); the distortion $D \approx 0.05$ is acceptable for the science target.

**Result.** $+25.1\ \mathrm{dB}$ against a $+20\ \mathrm{dB}$ target, with
$5\ \mathrm{dB}$ of margin that can be spent on a wider passband (less
distortion) or fewer records.

---

## ★★★8 — Why tuning on the test record over-smooths

**Mechanism.** Maximising SNR alone rewards suppressing every sample that is not
the signal, including the signal's own low-amplitude samples — a filter that
approximates the signal itself scores best. With a *known* true signal, the
optimum of SNR alone is the filter that best reproduces the signal's shape, and
as the search space widens this approaches a filter matched to that particular
realisation rather than to the class of signals. When applied to new data the
filter is too narrow and the waveform is broadened and biased. This is the
over-fitting failure in a filtering guise; the demonstration shows its signature
directly: as the noise scale is over-estimated, the output SNR *falls* while the
residual bias grows.

**Protocol that prevents it.**

1. Split the test data into a **tuning set** and a **held-out set** before any
   filter is chosen.
2. Choose the filter on the tuning set, but by the objective that includes both
   terms — e.g. minimise $D$ subject to a target SNR, or maximise
   $\text{SNR} - \lambda D$.
3. **Detect over-smoothing** on the held-out set with the second number the
   lesson insists on: the distortion $D$ and the retained signal rms. If the
   held-out SNR is much lower than the tuning SNR, or the retained rms drops
   below about 0.9 while the SNR does not improve, the filter has over-fit.
4. Report the tuning and held-out numbers side by side, and the number of
   parameters that were tuned. A filter with a hand-chosen band has one
   parameter; a Wiener filter estimated from the data has as many as it has
   frequency bins, and needs a correspondingly more careful protocol.
