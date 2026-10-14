# Solutions — 20-03-03 Filter Selection for Geophysical Data

> **Read after attempting the exercises.** Lesson:
> [03 Filter Selection](../03-filter-applications.md).

---

## ★1 — Alias of a 220 Hz tone

Decimating 1000 → 200 Hz gives $f_s' = 200$ Hz and Nyquist 100 Hz. The tone is
above Nyquist, so

$$f_{\text{alias}} = \left|220 - 1 \times 200\right| = 20\ \text{Hz}.$$

The 220 Hz tone reappears as a 20 Hz tone and is indistinguishable from genuine
20 Hz signal. An anti-alias lowpass at $0.8 \times 100 = 80$ Hz would have removed
it.

---

## ★2 — Notch bandwidth

$$B = \frac{f_0}{Q} = \frac{60}{40} = 1.5\ \text{Hz}.$$

The notch spans roughly 59.25–60.75 Hz at $-3$ dB.

---

## ★3 — Ordered chain

1. **Notch** the power line at $f_0$ with a narrow $Q$. The line lies inside the
   signal band, so no band-pass can remove it without removing signal; only a
   narrow notch can.
2. **Band-pass** to keep the signal band and reject the broadband ground roll
   below it and the high-frequency noise above it.
3. **Anti-alias lowpass** at $0.8\,f_s'/2$ before any decimation, to prevent
   folding.
4. **Decimate** by the chosen integer factor.

The order is forced by where each contaminant lives: narrowband-in-band needs a
notch; broadband-out-of-band needs a band-pass; anything above the new Nyquist
needs the anti-alias stage last, immediately before decimation.

---

## ★4 — Why one band-pass is not enough

The signal is at 45 Hz, the ground roll at 8 Hz, and the line at 50 Hz. A
band-pass that keeps 30–60 Hz keeps the 50 Hz line along with the signal. A
band-pass that keeps 30–45 Hz loses part of the signal's own band. Since the line
*overlaps the signal band*, no single frequency-selective filter can separate them:
the choice is between losing signal and keeping interference. A notch exploits the
line's narrow bandwidth (1.67 Hz at $Q = 30$) to remove it while leaving 30–45 Hz
and 55–60 Hz of signal intact, which is why the notch is a separate, earlier stage.

---

## ★5 — How a metric can get worse while the data improve

The metric is

$$\mathrm{SNR} = 10\log_{10}\frac{P_{30\text{--}60}}{P_{0\text{--}20}+P_{80\text{--}250}}.$$

The 50 Hz line lies **inside** the numerator band. Before notching, it contributed
a large amount of power to $P_{30\text{--}60}$, inflating the numerator. Removing
the line removes that inflation, so the ratio falls from $-3.36$ to $-15.57$ dB
even though the record improved. The metric was partly measuring the interference
it was supposed to penalise.

A metric without this defect must place the line in the denominator, not the
numerator. Two options:

- exclude the line from the signal band by defining the numerator as 30–45 Hz plus
  55–60 Hz (a notch-aware band), or
- define the metric on the *residual*: measure the power of
  (filtered record − clean synthetic signal) and compare with the power of the
  signal.

The honest summary of the demo is the raw-versus-final comparison, $-3.36 \to
+21.65$ dB, which does not pass through the ambiguous intermediate stage.

---

## ★6 — Alias bands for a decimation by 4

$f_s = 1000$ Hz → $f_s' = 250$ Hz, Nyquist 125 Hz. Content at $f$ folds to
$|f - k\,250|$ for the integer $k$ that lands it in $[0,125]$.

- 125–250 Hz folds directly onto 125–0 Hz (i.e. onto 0–125 Hz).
- 250–375 Hz folds to 0–125 Hz after subtracting 250.
- 375–500 Hz folds to 0–125 Hz.

The band that lands on 0–60 Hz is everything in $[125, 250] \cup [250,375] \cup
[375,500] \supset [125, 500]$ Hz, restricted to those offsets: a component at
$125 + x$ aliases to $|125 - x|$... more carefully, a component at $250 - x$
aliases to $x$ for $x \in [0,125]$, so the band 125–250 Hz maps onto 125–0 Hz;
the band 375–500 Hz maps to $|f - 500|$ = 0–125 Hz. So **everything above 125 Hz**
must be removed.

The anti-alias filter must therefore reach 60 dB by **125 Hz** (and stay above
60 dB to Nyquist, 500 Hz). Using the $0.8$ rule, a cutoff of $0.8\times125 =
100$ Hz leaves 25 Hz of transition to reach 60 dB, which the demo's 8th-order
Butterworth achieves.

---

## ★7 — A drifting line

A fixed 1.67 Hz notch ($Q = 30$) does not cover a $\pm0.2$ Hz drift if the first
record's null is exactly on 50 Hz and the line later sits at 50.2 Hz, where the
notch has only partial attenuation. Options:

1. **Widen the notch**: $Q = 20$ gives $B = 2.5$ Hz, spanning 48.75–51.25 Hz,
   covering the drift with margin. Cost: 2.5 Hz of the signal band removed, which
   matters if signal exists at 49–51 Hz.
2. **Time-varying notch**: estimate the instantaneous line frequency per window
   (from the spectrum of a quiet segment) and apply a per-window notch. Cost: the
   high resolution required to estimate 0.2 Hz needs a window of about
   $1/0.2 = 5$ s, so the notch can only be updated every several seconds.
3. **Adaptive cancellation** (lesson 05): if a reference channel at the line
   frequency is available, an NLMS canceller tracks the drift continuously with no
   signal-band hole.

The resolution cost is the honest currency: a wider fixed notch costs signal
band; a time-varying notch costs temporal resolution in the estimate.

---

## ★8 — Two-stage decimation

500 → 250 Hz (stage 1) → 125 Hz (stage 2).

- **Stage 1** must anti-alias to 125 Hz (Nyquist of 250 Hz). The 150 Hz tone is
  above 125 Hz and is removed here. The required attenuation at 150 Hz depends on
  how much the tone may leak: after stage 1, a residual at 150 Hz would be above
  the *new* Nyquist (125 Hz) and would fold at stage 2 to
  $|150 - 250| = 100$ Hz — not onto 25 Hz, but onto 100 Hz, still in-band. So
  stage 1 must suppress it below the noise floor; 60 dB is a reasonable target.
- **Stage 2** anti-aliases to 62.5 Hz. Nothing at 150 Hz survives stage 1, so
  stage 2 has no 150 Hz work to do; it only needs to suppress 62.5–125 Hz content
  that stage 1 passed.

Compare with the single-stage case: there, the 150 Hz tone folds all the way to
25 Hz. The two-stage chain is safer because each stage has a wider transition band
relative to its own sample rate, so a lower-order filter suffices — but only
because the **first** stage does the hard work. Skipping stage 1's anti-alias
filter reintroduces the 25 Hz alias exactly as in the single-stage case.