# Solutions — 20-01-05 Sampling, Nyquist and Reconstruction

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [05 Sampling, Nyquist and Reconstruction](../05-sampling-theory.md).

---

## ★1 — A 62 Hz tone at 100 Hz

$$f_{\text{alias}} = \left\lvert\left(\left(62 + 50\right)\bmod 100\right) - 50
\right\rvert = \lvert 12 - 50\rvert = 38\ \mathrm{Hz}.$$

The sign is negative because $62\bmod100 = 62 > f_s/2 = 50$: the apparent
waveform is **time-reversed**.

**What the analyst sees.** A clean $38\ \mathrm{Hz}$ tone, with no harmonic
structure, no spectral smearing and no indication of a problem. This is the
central difficulty of aliasing: the record is not noisy or corrupted, it is
*wrong in a way that looks perfect*. Nothing in a spectral analysis of the record
can reveal it, because the record contains exactly a 38 Hz tone — the sampled
sequence is identical to what a true 38 Hz source would have produced. Only
information from outside the record (a known source spectrum, or a second
recording at a different rate) can detect the fold.

For the record: if the same source is also recorded at $f_s = 128\
\mathrm{Hz}$, the apparent frequency there would be
$\lvert((62+64)\bmod128)-64\rvert = 62\ \mathrm{Hz}$, and the *disagreement*
between the two records is the detection.

---

## ★2 — Fold map

| $f$ (Hz) | $f_s$ (Hz) | $f_{\text{alias}}$ (Hz) | above or below Nyquist |
|---|---|---|---|
| 45 | 100 | 45 | below ($45 < 50$) |
| 75 | 100 | 25 | above ($75 > 50$) |
| 140 | 250 | 110 | above |
| 270 | 500 | 230 | above |
| 11 | 20 | 9 | above ($11 > 10$) |

Signs: 45 → $+$; 75 → $-$; 140 → $-$; 270 → $-$; 11 → $-$. So four of the five
fold with a time reversal, and only the first is unaliased.

Note the second line: $75\ \mathrm{Hz}$ sampled at $100\ \mathrm{Hz}$ is
indistinguishable from $25\ \mathrm{Hz}$. An isolated 25 Hz peak in a 100 Hz
record is therefore ambiguous unless the anti-alias filter guarantees that
nothing above $50\ \mathrm{Hz}$ reached the sampler.

---

## ★3 — $q$, peak error and SNR

$$q = \frac{10\ \mathrm{V}}{2^{14}} = \frac{10}{16384}
= 6.103516\times10^{-4}\ \mathrm{V} = 0.610\ \mathrm{mV},$$

$$\text{peak rounding error} = \frac{q}{2} = 0.305\ \mathrm{mV},$$

$$\mathrm{SNR} = 6.02\times14 + 1.76 = 86.04\ \mathrm{dB}.$$

For a $1\ \mathrm{V}$ sine instead of full scale ($5\ \mathrm{V}$), the signal
power drops by $20\log_{10}(1/5) = -13.98\ \mathrm{dB}$, so

$$\mathrm{SNR} = 86.04 - 13.98 = 72.06\ \mathrm{dB}.$$

**The lesson.** The headline bit count is only realised by a signal that fills the
converter. Every dB of unused headroom on the analog side is paid for directly in
SNR: a $\pm5\ \mathrm{V}$ converter digitising $1\ \mathrm{V}$ signals is a
$11.7$-bit converter in practice. This is why amplifier gain is set so that the
expected maximum signal lands just inside full scale — and why the *statistics*
of the signal (crest factor) determine how much of the range you dare to use.

---

## ★4 — A 130 Hz tone on a 250 Hz system

**(a) Where it appears.** $\lvert((130 + 125)\bmod 250) - 125\rvert
= \lvert(255\bmod250) - 125\rvert = \lvert5-125\rvert = 120\ \mathrm{Hz}$, with a
negative sign (the fold reverses the time axis). So the tone appears as a clean
$120\ \mathrm{Hz}$ peak, $5\ \mathrm{Hz}$ inside the passband.

**(b) Above or below the floor?** A 12-bit converter has
$\mathrm{SNR} = 6.02\times12 + 1.76 = 74.0\ \mathrm{dB}$ for a full-scale sine, so
the quantisation floor is $74\ \mathrm{dB}$ below the band-of-interest level. The
aliased tone arrives $40\ \mathrm{dB}$ below that level, i.e.

$$74 - 40 = 34\ \mathrm{dB}\ \textbf{above the noise floor}.$$

It is a detectable, contaminating peak, not a buried one.

**(c) Required attenuation.** The anti-alias filter must attenuate the tone by at
least $34\ \mathrm{dB}$ to bring it to the floor — and the attenuation must be at
**130 Hz**, the tone's true frequency, not at 120 Hz where it lands. This is the
most frequently misread line in an anti-alias specification: stopband
requirements are stated at the *input* frequencies that could fold, and the
relevant band is $f_s - f_{\text{pass}}$ upward, i.e. for a passband to
$100\ \mathrm{Hz}$ at $f_s = 250\ \mathrm{Hz}$ the critical band starts at
$150\ \mathrm{Hz}$ (which folds to $100\ \mathrm{Hz}$) and extends upward without
limit.

**Assumptions to state.** (i) The converter's SNR is the binding noise floor —
analog noise could be higher, and then less attenuation is needed. (ii) The tone
is a pure sinusoid; a broadband source requires integrating the folded spectrum
against the filter response. (iii) "40 dB below the full-scale level" means below
the *band of interest's* level, not below the converter's full scale; the two
differ by however much the band of interest is attenuated.

---

## ★5 — Twelve bits from a ten-bit converter

**How much SNR is needed:** $12-10 = 2$ bits
$\Rightarrow 2\times6.02 = 12.04\ \mathrm{dB}$.

**Oversampling ratio:** $10\log_{10}\mathrm{OSR} \ge 12.04 \Rightarrow
\mathrm{OSR} \ge 10^{1.204} = 15.996 \Rightarrow \mathrm{OSR} = 16$.

**Sample rate:** to oversample a $0$–$20\ \mathrm{Hz}$ band by 16, the rate must
be at least $2\times20\times16 = 640\ \mathrm{Hz}$. The deciding constraint is
usually the anti-alias filter rather than the rate: at $640\ \mathrm{Hz}$ the
first alias band starts at $640-20 = 620\ \mathrm{Hz}$, so the filter must be flat
to $20\ \mathrm{Hz}$ and reach its stopband by about $620\ \mathrm{Hz}$ — a
transition band of a factor of 31 in frequency, which is easy. Compare
$40\ \mathrm{Hz}$ sampling (the bare Nyquist rate), where the filter must go from
passband at $20\ \mathrm{Hz}$ to full attenuation by $20\ \mathrm{Hz}$ later — a
nearly impossible analog specification. **Oversampling buys a cheap anti-alias
filter as much as it buys bits.**

**Decimation filter:** the averaging decimator is a boxcar, whose nulls sit at
multiples of $f_s/\mathrm{OSR} = 40\ \mathrm{Hz}$ — the first null falls exactly
on the top of the wanted band and the stopband attenuation is only about
$-13\ \mathrm{dB}$ ([20-01-03 §5.1](../03-convolution-and-filters.md)). A proper
decimation filter is a designed low-pass with a corner just above $20\
\mathrm{Hz}$, stopband attenuation at least equal to the converter's SNR, and
passband ripple inside the error budget; then take every 16th sample.

**Cost of dither at $\mathrm{OSR} = 1$:** measured $2.94\ \mathrm{dB}$
($49.810\ \mathrm{dB} \to 46.866\ \mathrm{dB}$ for the 8-bit case in the lesson).
At $\mathrm{OSR} = 16$ the same measurement gives an improvement of
$11.868\ \mathrm{dB}$ with dither — $0.17\ \mathrm{dB}$ short of the promised
$12.04$ — so the two bits arrive with a $0.03$-bit shortfall. Without dither the
gain stalls, and dither is cheaper than three extra bits.

---

## ★6 — Aperture loss from a one-sample hold

$$\lvert H(f)\rvert = \left\lvert\frac{\sin(\pi f/f_s)}{\pi f/f_s}\right\rvert .$$

The $-1\ \mathrm{dB}$ point solves $\lvert\operatorname{sinc}(u)\rvert =
10^{-1/20} = 0.891251$, giving

$$u = f/f_s = 0.261500 .$$

So the response is within $1\ \mathrm{dB}$ only up to **26.2 % of the sample
rate**. Measured table:

| $f/f_s$ | 0.25 | 0.5 (Nyquist) |
|---|---|---|
| $\lvert H\rvert$ | 0.900316 | 0.636620 |
| dB | $-0.912$ | $-3.922$ |

**Correction.** Yes — the aperture is a known, deterministic, minimum-phase
amplitude filter, so it can be divided out (with the usual care about noise
amplification at the band edge, exactly as in
[20-04 Deconvolution](../../04-deconvolution-and-inverse-filtering/README.md)). Two
practical notes: (i) many instrument-response files already include the
digitising aperture, so correcting twice is a real hazard — read the
documentation; (ii) if the aperture is an *anti-alias* filter's group delay plus a
hold, the phase must be handled as well, and the total delay is
$\Delta t/2$ for an ideal hold, i.e. half a sample.

---

## ★7 — Array design for microseismic monitoring

$$f_{\max} = \frac{v}{2\Delta x}:
\qquad
v = 2000\ \mathrm{m/s}: \frac{2000}{2(15)} = 66.7\ \mathrm{Hz},
\qquad
v = 5000\ \mathrm{m/s}: \frac{5000}{2(15)} = 166.7\ \mathrm{Hz}.$$

**Verdict:** the array fails the specification. At $\Delta x = 15\ \mathrm{m}$
the slow end of the required velocity range aliases everything above
$66.7\ \mathrm{Hz}$; the fast end is comfortable. Note the direction of the
tension: **slower apparent velocities alias sooner**, so the requirement is set
by the *smallest* expected apparent velocity, which is the opposite of the
intuition that "the array must be designed for the fastest wave"
(that intuition applies to the *sampling rate in time*, where the highest
frequency sets the rate — in space it is the largest wavenumber, i.e. the slowest
wave × the highest frequency).

**Redesign options.**

1. **Reduce spacing.** For $f_{\max} \ge 80\ \mathrm{Hz}$ at
   $v = 2000\ \mathrm{m/s}$:
   $\Delta x \le v/(2f_{\max}) = 2000/160 = 12.5\ \mathrm{m}$. That is a 17 %
   reduction — cheap if the survey is being planned, impossible if it is not.
2. **Spatial anti-alias by grouping.** Replace each single sensor with a
   *sub-array* (a "geophone group") whose length is about $\Delta x$; the group
   response sums incoherently-moving high-wavenumber energy and suppresses it,
   at the cost of attenuating steeply dipping but genuine signal.
3. **Accept and flag.** If the slow $2000\ \mathrm{m/s}$ arrivals above
   $66.7\ \mathrm{Hz}$ are not needed (often they are not: they are mostly
   near-surface or shallow-path energy), record the aliasing as a documented
   limitation with the band stated.

**The field measurement that tests the assumption.** Record a shot with a
*reference* small-aperture array (spacing a few metres) alongside the production
array, compute the f-k spectrum of each for the same event, and compare the
wavenumber content: if the production array's f-k spectrum has energy piling up
along the alias lines $k = {\pm}1/(2\Delta x)$, the assumed $f_{\max}$ was
optimistic.

**If it turns out to be optimistic.** Do not simply filter in time: the aliased
energy is now *inside* the unaliased band because it has folded to a
low wavenumber, where it overlaps the genuine signal. Options are to restrict
processing to sub-alias wavenumbers (accepting reduced resolution), to migrate
with an explicit aliasing-aware operator, or — the honest answer — to report the
band limitation in every result derived from the array.

---

## ★8 — Testing "16× oversampling gives us 4 bits"

**What 16× can deliver.** From the measured table in the lesson, 16×
oversampling gives

- **with dither:** $11.868\ \mathrm{dB} = 1.97$ effective bits;
- **without dither:** $10.446\ \mathrm{dB} = 1.74$ effective bits.

The claimed 4 bits would require $4\times6.02 = 24.1\ \mathrm{dB}$, i.e.
$\mathrm{OSR} = 10^{2.41} = 257$. The claim is wrong by a factor of
$\sim$16 in rate.

**The experiment that settles which regime the system is in.** Digitise a
*quiet* input — ideally a DC level, or a very slow ramp — with the production
antialias and decimation chain, and compute the amplitude histogram of the
output. Without dither the histogram is a comb of discrete spikes separated by
$q$ (the level stays on a few codes); with dither it becomes smooth and
continuous. A second, equivalent test: apply a tiny DC offset sweep and check
whether the output moves continuously or in steps of $q$; a system with adequate
dither moves continuously.

**Why 16× removes no aliased tone.** The fold map is
$f_{\text{alias}} = \lvert((f+f_s/2)\bmod f_s) - f_s/2\rvert$, a property of the
*relationship* between $f$ and $f_s$. Raising $f_s$ changes the fold only by
shifting which frequencies are above Nyquist: a tone at $f$ that aliased at
$f_s = 100\ \mathrm{Hz}$ may not alias at $f_s = 1600\ \mathrm{Hz}$ — but if there
is *any* energy above the new Nyquist, it folds just the same, and
oversampling plus decimation moves that energy back down into the recorded band
during the decimation step. Oversampling cannot create bandwidth; it buys
resolution within the band that the sampling rate already supports.

**The smallest modification that would help.** Put a genuine anti-alias filter
ahead of the sampler, specified with an attenuation at least equal to the
converter's SNR at every frequency above $f_s - f_{\text{pass}}$. If the analog
filter cannot be changed, *raise the sample rate* so that the offending tone falls
inside the unaliased band and can then be removed digitally — which is a change
to the acquisition, not to the processing.


---

## Mastery checkpoint answers

**(a)** $f_{\text{alias}} =
\lvert((62+50)\bmod 100) - 50\rvert = 38\ \mathrm{Hz}$, with a **negative**
apparent frequency $(62\bmod100 = 62 > 50)$: the waveform runs backwards in time.
A real cosine record cannot reveal it because $\cos(-2\pi f t) = \cos(2\pi f t)$:
the sampled sequence is *identical* to that of a genuine $38\ \mathrm{Hz}$
cosine, so no analysis of that record can tell the two apart. Only external
information (a second record at another rate, or a known source spectrum) can.

**(c)** $q = 10\,\mathrm{V}/2^{14} = 0.610352\ \mathrm{mV}$; the peak rounding
error is $q/2 = 0.305176\ \mathrm{mV}$; the SNR for a full-scale sine is
$6.02\times14+1.76 = 86.04\ \mathrm{dB}$. For a $1\ \mathrm{V}$ sine,
subtract $20\log_{10}(5) = 13.98\ \mathrm{dB}$: $72.06\ \mathrm{dB}$.

**(f)** $f_{\max} = v/(2\Delta x) = 1500/25 = 60\ \mathrm{Hz}$. A
$90\ \mathrm{Hz}$ component is therefore aliased: its true wavenumber is
$k = f p = 90/1500 = 0.06$ cycles/m against a spatial Nyquist wavenumber of
$1/(2\Delta x) = 0.04$ cycles/m, so it folds to
$k_{\text{alias}} = 0.06 - 0.08 = -0.02$ cycles/m. It appears as a
$90\ \mathrm{Hz}$ event with an **apparent velocity of
$-4500\ \mathrm{m\,s^{-1}}$** — the right speed and the wrong sign of dip — which
is the spatial analogue of the temporal fold measured above.
