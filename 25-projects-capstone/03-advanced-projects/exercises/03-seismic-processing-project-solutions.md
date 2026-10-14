# Solutions — 25-03-03 Project: Seismic Reflection Processing Flow

> Read after attempting. Lesson:
> [03 Seismic Processing](../03-seismic-processing-project.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/seismic_processing_demo.py`](../code/seismic_processing_demo.py).

---

## ★1 — Moveout and stretch at 1500 m

$$t(1500) = \sqrt{1.2^{2} + \frac{1500^{2}}{2800^{2}}}
= \sqrt{1.44 + 0.28699} = \sqrt{1.72699} = 1.31415\ \mathrm{s}.$$

$$\text{stretch} = 1 - \frac{t_0}{t} = 1 - \frac{1.2}{1.31415} = 0.0869
= 8.69\%.$$

Below the usual $20$–$30\%$ mute threshold, so this offset would be kept.
Moveout is $0.11415\ \mathrm{s} = 114.15\ \mathrm{ms}$.

---

## ★2 — Residual moveout for a $2\%$ velocity error

$v_* = 0.98 \times 2500 = 2450\ \mathrm{m\,s^{-1}}$:

$$t(2000; 2450) = \sqrt{1 + \frac{4\times10^{6}}{6.0025\times10^{6}}}
= \sqrt{1.666389} = 1.290888\ \mathrm{s},$$

against the true $t(2000; 2500) = 1.280625\ \mathrm{s}$:

$$\Delta t = 1.290888 - 1.280625 = +10.26\ \mathrm{ms}.$$

In wavelet periods, with $1/30\ \mathrm{Hz} = 33.3\ \mathrm{ms}$:

$$\frac{10.26}{33.3} = 0.31\ \mathrm{period}.$$

A third of a period of mis-registration is the point at which the stack begins to
lose amplitude and the wavelet begins to change shape, which is the standard
working tolerance for velocity-pick accuracy. The demonstration's $5\%$ error
gives $0.70$ of a period and collapses the far-trace amplitude from $1.0071$ to
$-0.1338$.

---

## ★3 — Semblance values

Semblance is the ratio of the stacked energy to the summed individual energy:

$$S = \frac{\sum_j \big(\sum_i a_{ij}\big)^{2}}{N\sum_j\sum_i a_{ij}^{2}}.$$

**Perfectly coherent event.** All $N = 81$ traces carry the same value at each
sample: $\big(\sum_i a_{ij}\big)^{2} = N^{2}a^{2}$ and
$N\sum_i a_{ij}^{2} = N \cdot N a^{2}$, so

$$S = \frac{N^{2}a^{2}}{N^{2}a^{2}} = 1.$$

**Pure incoherent noise.** The cross-terms average to zero, so
$\big(\sum_i a_{ij}\big)^{2} \approx N\langle a^{2}\rangle$ while
$N\sum_i a_{ij}^{2} = N^{2}\langle a^{2}\rangle$, giving

$$S \to \frac{1}{N} = \frac{1}{81} = 0.0123.$$

The demonstration's peak values, $0.0306$ and $0.0287$, sit between the two bounds
— as they must, because $30\ \mathrm{Hz}$ data sampled at $2\ \mathrm{ms}$ gives
only about 16 samples per period and the trial hyperbola is rarely exactly right.
Semblance is a *relative* measure; its absolute value is not a quality metric, but
its **bandwidth** is a resolution metric.

---

## ★★4 — Why the deeper pick is broader

Moveout at 2000 m:

- first primary: $1.280625 - 1.000 = 0.2806\ \mathrm{s}$;
- second primary: $2.095430 - 2.000 = 0.0954\ \mathrm{s}$.

Moveout ratio: $0.2806/0.0954 = 2.94$.

Measured bandwidth ratio: $240/60 = 4.00$.

The controlling quantity is not moveout but the **sensitivity of moveout to
velocity**:

$$\frac{\partial \Delta t}{\partial v}
= -\frac{x^{2}}{v^{3}}\cdot\frac{1}{t}.$$

| reflector | $x^{2}/v^{3}/t$ ($\mathrm{s}$ per m s⁻¹) | ratio |
|---|---|---|
| $t_0 = 1.0$ s, $v = 2500$ | $1.999\times10^{-4}$ | — |
| $t_0 = 2.0$ s, $v = 3200$ | $5.826\times10^{-5}$ | $3.43$ |

The derivative ratio $3.43$ is within $17\%$ of the measured bandwidth ratio
$4.00$; the pure-moveout ratio $2.94$ is $26\%$ off. So the pick's precision
scales approximately as the inverse of $\partial\Delta t/\partial v$, and the
residual difference is the fixed window length in samples and the fact that
semblance is not exactly a quadratic function of the velocity error near the peak.
The practical statement holds: **the deeper the reflector, the worse the velocity
pick, for the same spread.**

---

## ★★5 — Choosing and tightening the mute

Setting the stretch to exactly $20\%$:

$$1 - \frac{t_0}{t} = 0.20 \;\Longrightarrow\; t = \frac{1.000}{0.80}
= 1.250\ \mathrm{s}
\;\Longrightarrow\; x^{2} = v^{2}(t^{2}-t_0^{2}) = 2500^{2}(1.5625-1),$$

$$x = \sqrt{3.5156\times10^{6}} = 1875\ \mathrm{m}.$$

The stretch is *strictly* greater than $20\%$ only beyond 1875 m, so on a 25 m
grid the muted traces are those from 1900 to 2000 m: **5 of 81**, matching the
demonstration.

Tightening the threshold to $15\%$: $t = 1.000/0.85 = 1.17647\ \mathrm{s}$, so
$x^{2} = 6.25\times10^{6}(1.38408 - 1) = 2.4005\times10^{6}$ and
$x = 1549.4\ \mathrm{m}$; the muted traces run from 1550 to 2000 m, i.e.
$(2000-1550)/25 + 1 = 19$ of $81$.

**Trade-off.** A tighter mute removes more stretched, low-frequency-biased data
and loses more far-offset coverage — and the far offsets are exactly where the
velocity information lives, so a tighter mute degrades the velocity analysis on
the *next* pass. Use the unmuted gather for velocity analysis and the muted one
for the stack.

---

## ★★6 — Two gains and why they differ

$$\text{simple average gain} = \frac{0.07836}{0.00882} = 8.885
\qquad (\sqrt{81} = 9.000,\ \text{agreement to } 1.3\%),$$

$$\text{NMO stack gain} = \frac{0.07836}{0.00702} = 11.163.$$

The simple average behaves exactly as the $\sqrt{N}$ law predicts, because
averaging independent traces reduces a white-noise variance by $N$ while
preserving the coherent signal. The NMO stack's gain is **$26\%$ higher** than
the prediction, and the excess is not signal: the moveout correction resamples
each trace at shifted times by linear interpolation, which is a low-pass filter.
The coherent signal (well below the sampling Nyquist) passes almost unchanged
while the white noise, which has power up to Nyquist, is attenuated. The stack's
noise is therefore reduced by more than $1/\sqrt{N}$, and quoting $11.16$ as "the
stacking gain" credits the processing with a gain that belongs to the
interpolation.

The general lesson: any processing step that resamples, interpolates or filters
will change the noise statistics as well as the signal, and a measured
signal-to-noise gain is a measurement *of that step*, not of a physical principle.

---

## ★★★7 — Resolving $v_\text{rms}$ to $\pm 1\%$ at $t_0 = 2.5$ s

**Available moveout.** With a maximum offset of 3000 m and a plausible
$v_\text{rms} = 3500\ \mathrm{m\,s^{-1}}$:

$$t(3000) = \sqrt{2.5^{2} + \frac{9\times10^{6}}{1.225\times10^{7}}}
= \sqrt{6.25 + 0.7347} = 2.64286\ \mathrm{s},
\qquad
\text{moveout} = 0.14286\ \mathrm{s}.$$

**Implied resolution.** The sensitivity is

$$\frac{\partial\Delta t}{\partial v}
= \frac{x^{2}}{v^{3}t} = \frac{9\times10^{6}}{4.2875\times10^{10}\times2.64286}
= 7.94\times10^{-5}\ \mathrm{s\ per\ m\,s^{-1}},$$

so a $\pm 1\%$ ($\pm 35\ \mathrm{m\,s^{-1}}$) velocity error moves the far-offset
arrival by only

$$\Delta\Delta t = 7.94\times10^{-5} \times 35 = 2.78\ \mathrm{ms},$$

which is $0.08$ of a $33\ \mathrm{ms}$ wavelet period. The semblance band for the
deeper reflector in the demonstration was already $\pm 240\ \mathrm{m\,s^{-1}}$
at $t_0 = 2$ s with a similar geometry, so the requirement **cannot** be met with
a 3000 m maximum offset: the pick's resolution is several times coarser than
$\pm 1\%$.

**What delivers it.** Three levers, in increasing cost:

1. **Offset range.** The sensitivity scales roughly as $x^{2}/t$, so going from
   3000 to 5200 m multiplies it by about 3 — enough to bring $2.78$ ms to
   $8.3\ \mathrm{ms} = 0.25$ period. Doubling the spread is the standard remedy
   and the standard cost (more channels, more shots, more processing).
2. **Wavelet bandwidth.** A $60\ \mathrm{Hz}$ source halves the period, so the
   same $2.78$ ms becomes $0.17$ period. A higher-frequency source is cheaper
   than a longer spread but penetrates less and is absorbed more over the
   overburden.
3. **Trace count and window design.** Increasing fold reduces the *statistical*
   part of the pick error but not the systematic bias from residual
   non-hyperbolic moveout; it is the weakest of the three levers at depth.

**The test that must be run before reporting.** Report the semblance
**half-maximum band** for the target at $t_0 = 2.5$ s in $\mathrm{m\,s^{-1}}$.
If it is wider than $\pm 35\ \mathrm{m\,s^{-1}}$ (i.e. $\pm 1\%$), the requirement
is unmet, and the honest deliverable is the measured band rather than a number.
A second, complementary test is a synthetic recovery: model the same geometry and
noise, invert for the velocity, and measure the recovered width — if the synthetic
width exceeds the requirement, no field result can be better. Both tests are
cheap and both belong in the report.
