# Solutions — 16-06-04 Pleistocene Glacial Cycles and Orbital Forcing

> Read after attempting the exercises. Lesson:
> [04 Pleistocene Glacial Cycles and Orbital Forcing](../04-pleistocene-cycles.md).

---

## ★1 — Summing the forcing shares

$$0.2723 + 0.6831 + 0.0026 = 0.9580.$$

The remainder, $0.0420$, lies in bands outside the three named ones: the long
$(>200\ \mathrm{ka})$ band ($0.0017$), and the intervening frequencies between
the bands — the sidebands produced by the amplitude modulation, and any power
between about 25 and 40 ka and between 50 and 80 ka not captured by the named
windows. The shares are a partition of the spectrum into the analyst's chosen
bands, not of a physical decomposition.

---

## ★2 — Required amplification

Power ratio:

$$\frac{0.3073}{0.0026} = 118.2.$$

Amplitude ratio:

$$\sqrt{118.2} = 10.87.$$

A linear transfer function would need to amplify the $100\ \mathrm{ka}$ component
by a factor of nearly eleven while leaving the other bands largely untouched
(★5). That is a narrow resonance, and its required sharpness is the quantitative
statement of the "100-kyr problem".

---

## ★3 — E-folding and growth time

With $g = 1/60\ \mathrm{ka^{-1}}$, the e-folding time is $1/g = 60\
\mathrm{ka}$. With melting off, $1-V = (1-V_0)e^{-gt}$, so from $V_0 = 0$:

$$V(t) = 1 - e^{-t/60}.$$

Setting $V = 0.633$: $1-0.633 = 0.367 = e^{-t/60}$, so
$t = 60\ln(1/0.367) = 60 \times 1.0024 = 60.1\ \mathrm{ka}$. The maximum volume
in the demonstration's run ($0.6329$) is therefore about one e-folding of growth
— the ice never approaches its nominal maximum, because the melt threshold
intervenes first.

---

## ★4 — Spectral resolution

Frequency spacing: $\Delta f = 1/T = 1/2400 = 4.17\times10^{-4}\
\mathrm{ka^{-1}}$. At $P = 100\ \mathrm{ka}$, $f = 0.01\ \mathrm{ka^{-1}}$, and

$$\Delta P = \frac{\Delta f}{f^{2}} = P^{2}\Delta f = \frac{100^{2}}{2400}
= 4.17\ \mathrm{ka},$$

i.e. $4.2\%$ of the period. A quoted dominant period of $100.0\ \mathrm{ka}$
should therefore be read as $100 \pm 4\ \mathrm{ka}$ given the record length
alone, before any consideration of aliasing or of the spectral estimator's
windowing. Quoting more digits than the resolution justifies is a common
overclaim.

---

## ★5 — Band-by-band ratios

| band | forcing share | response share | ratio |
|---|---|---|---|
| obliquity (41 ka) | 0.2723 | 0.2042 | $0.750$ |
| precession (19–23 ka) | 0.6831 | 0.1536 | $0.225$ |
| eccentricity (100 ka) | 0.0026 | 0.3073 | $118.2$ |

The obliquity and precession bands are attenuated (ratios $<1$): the ice model
does not follow the fast insolation changes directly. The eccentricity band is
amplified by two orders of magnitude. No single linear transfer function can do
both, because a linear $|H(f)|^{2}$ would have to be tiny at 23 ka and huge at
100 ka, with a rapid transition between — which is what Section 7 of the lesson
means by "a strained explanation".

---

## ★6 — Sensitivity to the melt threshold

Long-period share:

$$\frac{0.5066-0.3598}{0.80-0.60} = \frac{0.1468}{0.20} = 0.734\ \text{per unit threshold}.$$

Mean volume:

$$\frac{0.3103-0.2182}{0.20} = 0.4605\ \text{per unit threshold}.$$

Both are positive: raising the threshold makes melting harder, so the ice stays
larger on average, and more of the response's variance is pushed into the long
period because melt events become rarer and more concentrated at the extreme
forcing maxima. The *period* is unchanged at $100.0\ \mathrm{ka}$ across the
range, which is the robust feature; the amplitude distribution is not robust, and
a model that fixes the period while missing the amplitude distribution has
reproduced only part of the record.

---

## ★7 — Distinguishing a threshold from an internal oscillation (specification)

**Diagnostic.** Compare the response in the period bands with the forcing. A
threshold-driven response is *phase-locked* to the forcing: its long-period
maxima occur at times set by the forcing envelope, and its period changes
coherently when the forcing's modulation changes. An internally oscillating ice
sheet has an intrinsic period set by its own dynamics (accumulation rate, basal
conditions, isostatic response), which persists — and can be detected — even when
the forcing is held constant.

**Expected signatures.** (i) Threshold: period shifts with the threshold and with
the forcing amplitude; spectral power at the forcing's modulation frequency and
its sidebands. (ii) Internal oscillation: a period that is stable under changes
to the forcing but shifts with ice-sheet parameters (accumulation, ablation
gradient); a self-sustained oscillation in a run with constant forcing.

**Remaining ambiguity.** The two mechanisms interact: an ice sheet near its own
oscillation threshold can be nudged into a different limit cycle by the orbital
forcing, in which case the observed period is neither the forcing's nor the
ice sheet's. A test that varies only one of the two cannot separate that case,
and the separation requires joint modelling of both.

---

## ★8 — Critique of "orbital forcing explains the 100-kyr cycles"

**What the demonstration establishes.** That a nonlinear model with a melt
threshold, driven by an amplitude-modulated precession signal, concentrates
variance at a long period that the forcing's own spectrum barely contains
(forcing share $0.0026$ versus response share $0.3073$ in that band), and produces
an asymmetric sawtooth response ($79.7\%$ of the time growing, skewness
$+0.3026$). It shows a *possible* mechanism and quantifies what it does.

**What it does not establish.**

1. That the synthetic forcing resembles the real insolation history. It uses the
   standard periods but chosen amplitudes and phases, and a dimensionless proxy
   rather than an actual insolation computation.
2. That the model's threshold and time constants are physical rather than chosen;
   the demonstration shows the output changing materially when one threshold is
   changed by $0.2$ (long-period share $0.3598 \to 0.5066$).
3. That the response matches the reconstructed ice volume in detail — no real
   record is used, and no comparison is made.
4. That competing mechanisms (carbon-cycle changes, dust and albedo feedbacks,
   ice-sheet internal dynamics, ocean circulation reorganisation) are excluded.
5. That the model is falsifiable in its present form: with free threshold and
   amplitude parameters it can be tuned to many records.

**What would be required.** A forcing computed from the full orbital solution, a
physically constrained ice model validated against independent observables, a
quantitative fit to a dated record including its uncertainty, and a demonstration
that alternative mechanisms cannot reproduce the same features. Until then the
honest statement is: the demonstration exhibits a mechanism capable of producing
the observed spectral signature, and there is no reason to prefer it to the
alternatives on the evidence presented.
