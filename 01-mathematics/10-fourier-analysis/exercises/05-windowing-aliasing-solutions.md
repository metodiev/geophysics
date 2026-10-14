# Solutions — 01-10-05 Sampling, Aliasing, Leakage and Windowing

> **Read this after attempting the exercises, not before.**
>
> All values below were computed. Values quoted from the supplied script are the
> values it printed.

---

## ★1 — Nyquist frequencies and apparent frequencies

The fold formula is
$f_{\text{app}} = \big((f+f_N)\bmod f_s\big) - f_N$ with $f_N = f_s/2$.

| | $f$ | $f_s$ | $f_N$ | $f_{\text{app}}$ | aliased? |
|---|---|---|---|---|---|
| (a) | 12 Hz | 20 Hz | 10 Hz | $\big((12+10)\bmod20\big)-10 = 2-10 = \boxed{-8\ \mathrm{Hz}}$ | **yes** |
| (b) | 45 Hz | 100 Hz | 50 Hz | $\big((45+50)\bmod100\big)-50 = 95-50 = \boxed{+45\ \mathrm{Hz}}$ | no |
| (c) | 75 Hz | 100 Hz | 50 Hz | $\big((75+50)\bmod100\big)-50 = 25-50 = \boxed{-25\ \mathrm{Hz}}$ | **yes** |
| (d) | 5 Hz | 4 Hz | 2 Hz | $\big((5+2)\bmod4\big)-2 = 3-2 = \boxed{+1\ \mathrm{Hz}}$ | **yes** |

**Notes on the signs.** (a) and (c) fold to *negative* apparent frequencies, and
(b) — a tone between the first and second Nyquist zones — folds to a positive one.
The sign matters whenever the direction of a signal is being interpreted (a
Doppler shift, a slowness, an f-k quadrant), so the fold should be applied to the
signed frequency and the result reported as it comes out. (d) is deliberately
extreme: a 5 Hz tone sampled at 4 Hz — below Nyquist by a factor of 2.5 — appears
as a 1 Hz tone, indistinguishable from a genuine 1 Hz signal.

---

## ★2 — Receiver spacing from the spatial Nyquist relation

**(a)** $f_a = v/(2\,dx) = 800/(2\times20) = \boxed{20\ \mathrm{Hz}}$.

**(b)** $dx \le v/(2f_{\max}) = 800/(2\times60) = \boxed{6.67\ \mathrm{m}}$.

**(c)** The general form used above is

$$f_a = \frac{v_{\text{app}}}{2\,dx}
\qquad\text{equivalently}\qquad
dx \le \frac{v_{\min}}{2\,f_{\max}} ,$$

which is the temporal Nyquist relation $f_s \ge 2f_{\max}$ with $f_s = v/dx$:
the "sampling rate" along a receiver line is one trace per distance
$dx$ travelled by the wavefront, i.e. $v/dx$ traces per second.

**Note the 9× cost.** Moving from 20 m to 6.67 m spacing triples the number of
receivers in one direction (nine times in two dimensions). This is why the
difference between a 20 Hz and a 60 Hz target is an acquisition-scale decision,
not a processing one.

---

## ★3 — Resolution from record length

**(a)** $T = N\,dt = 512\times0.004 = 2.048$ s; $df = 1/T = 0.4883$ Hz; Nyquist
$= 1/(2\,dt) = 125$ Hz.

**(b)** 0.1 Hz is *below* $df = 0.4883$ Hz, and $1/T = 0.4883$ Hz is the
resolution, so **no** — the two tones cannot be separated. They will appear as a
single broadened lobe whose shape is dominated by their interference.

**(c)** 3 Hz is about 6.1 bins apart, comfortably more than the resolution, so
**yes** with any of the windows of the lesson (though a tapered window costs
about a factor 2 in width, 6 bins still exceeds the Hann threshold of 2.3 bins).

**(d)** Padding to 8192 gives
$df_{\text{pad}} = 1/(8192\times0.004) = 0.0305$ Hz. The bin spacing has fallen
by a factor of 16, but $1/T$ is unchanged: **the answers to (b) and (c) are
unchanged**. The padded spectrum draws the same continuous curve with 16 times as
many samples, so a peak or valley is located more precisely and a marginal split
may become *visible* — but a pair separated by 0.1 Hz remains a single lobe,
because 0.1 Hz is a fifth of one resolution width.

---

## ★4 — Scalloping loss

**(a)** The nearest bin reads $2/\pi = 0.6366$ of the true amplitude, i.e.

$$20\log_{10}(2/\pi) = \boxed{-3.92\ \mathrm{dB}}.$$

**(b)** **The total energy is unchanged.** The tone's energy in the record is the
same whether it happens to land on a bin or between two; what changes is where
that energy is stored. A four-bin-wide neighbourhood contains essentially all of
it, and Parseval summed over the whole spectrum is independent of the offset.

**(c)** Recover the amplitude by **interpolating the spectrum** — zero-padding
before the transform, or fitting a Dirichlet/sinc shape to the samples around the
peak. The script's own measurement shows the interpolated peak recovers the
amplitude to within 0.4% even at the worst offset.

What interpolation does **not** fix: the resolution. Two tones closer than $1/T$
produce one interpolated peak, however finely the spectrum is sampled, because
the underlying continuous spectrum genuinely has one maximum.

---

## ★★5 — A seismic acquisition question

**(a)** $f_N = 1/(2\times0.004) = \boxed{125\ \mathrm{Hz}}$.

**(b)** $f_a = v/(2\,dx) = 300/(2\times25) = \boxed{6\ \mathrm{Hz}}$.

**(c)** The ground roll occupies 5–15 Hz, and everything above 6 Hz is spatially
aliased at 25 m spacing. So **yes: all of the band above 6 Hz is aliased**, and
the recorded ground roll will have an apparent velocity that wraps — at 15 Hz the
apparent velocity reads $2\times25\times15 = 750$ m/s, not 300 m/s, and it will
appear on the section as a plausible slower-dipping event in the opposite
direction. (The formula $f_a = v/(2dx)$ gives the frequency at which the phase
step reaches $180^\circ$; above it the measured velocity is
$v_{\text{app}} = v\,f_a/f$ in magnitude with a sign flip.)

**(d)** At $dx = 10$ m: $f_a = 300/(2\times10) = \boxed{15\ \mathrm{Hz}}$, so the
ground-roll band 5–15 Hz now sits *at or below* the alias frequency and is
recorded without aliasing. This is the standard reason modern high-resolution
surveys use small receiver intervals: not to image shorter wavelengths directly,
but to record the surface wave unaliased so that it can be removed by velocity
filtering rather than merely smeared.

---

## ★★6 — Trend leakage

**(a)** A record is the true signal times a boxcar window, so the measured
spectrum is the true spectrum convolved with the window's transform — a sinc
whose sidelobes decay only as $1/f$. A linear trend is a discontinuous function
at the record's ends (the periodic extension jumps), and that discontinuity is
what a $1/f$ spectrum means: the transform of a step-like feature.

**(b)** The amplitude spectrum of a ramp decays as $f^{-1}$, i.e. an exponent of
$-1$. The script measures $-0.996$ for a synthetic ramp over bins 4–40 — $1/f$ to
three figures.

**(c)** The residual leakage after removing the best-fit straight line is at the
round-off level: the script's mean $\lvert X\rvert$ over bins 8–40 falls from
$8.482$ to $0.000\times10^{0}$. What else is removed: a little of any genuine
long-wavelength signal, because a sampled sinusoid is not exactly orthogonal to a
linear function over a finite record.

**(d)** The script measures the recovered amplitude of a 12-cycle periodic tone
in a record that also contains a ramp: 1.000000 for the tone alone, 0.947052 for
tone + ramp, and **0.995794** after detrending. So the residual bias from
detrending is 0.42%, and it falls as $1/N$ with record length.

---

## ★★7 — Coherent gain

**(a)** All amplitudes are too large by $1/0.5 = 2$ — that is, **too small by a
factor of 2** if the coherent gain is not divided out; the raw Hann-windowed
spectrum reads half the true amplitude.

**(b)** $20\log_{10}(0.5) = -6.02$ dB in amplitude, and since power goes as
amplitude squared, $-12.04$ dB in power.

**(c)** A unit-amplitude tone windowed by Hann gives a raw peak amplitude reading
of 0.5. **Yes, that is correct as a raw spectral value** — the window has scaled
the signal by its mean value of 0.5 — and it becomes the physical amplitude 1.0
only after dividing by the coherent gain. Both statements are true and the
distinction is the whole point: the number is right, its *interpretation*
requires the correction.

**(d)** For Blackman (coherent gain 0.42): the raw reading of a unit tone is 0.42
and the correction factor is $1/0.42 = 2.381$, i.e. $+7.52$ dB. Note that a
sequence of windows with different coherent gains applied to the same data will
produce amplitude spectra differing by up to 7.5 dB unless all are corrected —
one of the commonest sources of apparently inconsistent amplitudes between
processing vintages.

---

## ★★8 — Resolution at the threshold

**(a)** Separation $2/T$. From the lesson's measured thresholds — rectangular
1.2, Hann 2.3, Hamming 2.2, Blackman 2.5 (all in units of $1/T$) — only the
**rectangular** window meets its own criterion at $2.0/T$. Hann, Hamming and
Blackman have thresholds above 2.0 and so show a single merged lobe under the
stated criterion (two maxima with a valley at least 3 dB below the lower one). As
the lesson's zero-padding table shows, at exactly $2.0\,df$ the valley depth is
about $+0.1$ dB — the two peaks are not separated by a dip at all.

**(b)** At $3/T$ all four windows exceed their thresholds (rectangular 1.2, Hann
2.3, Hamming 2.2, Blackman 2.5), and the measured valley depth for Blackman is
$-4.2$ dB at its own threshold and $\approx -31.5$ dB for a Hann-windowed pair at
$3\,df$ in the zero-padding experiment. The reason is simply the main-lobe
widths: 2 bins for the rectangular window, 4 for Hann and Hamming, 6 for
Blackman, so the *separation at which a dip appears* scales with the lobe width.

**(c)** A Blackman window with a 1 s record gives a resolution threshold of
$2.5\times(1/1\,\mathrm{s}) = 2.5$ Hz, and the claimed 2 Hz is below it. So the
claim is **not supported**: two 2 Hz-separated tones would merge into a single
lobe under the lesson's criterion with that window and that record. The claim
would be defensible with the rectangular window (threshold 1.2 Hz), which is
exactly the trade: the Blackman window suppresses sidelobes by 58 dB and pays for
it with a 2.5× coarser resolution.

---

## ★★★9 — What a window is worth in practice

**(a)** Separation 3 bins:

| window | floor (relative to the strong tone's peak) | floor (dB) | weakest $a$ for $+6$ dB |
|---|---|---|---|
| rectangular | $2.122\times10^{-1}$ | $-13.5$ | $5.670\times10^{-1}$ |
| Hann | $1.081\times10^{-1}$ | $-19.3$ | $1.987\times10^{-1}$ |

**(b)** Separation 8 bins:

| window | floor (relative to peak) | floor (dB) | weakest $a$ for $+6$ dB |
|---|---|---|---|
| rectangular | $5.269\times10^{-2}$ | $-25.6$ | $1.234\times10^{-1}$ |
| Hann | $1.069\times10^{-3}$ | $-59.4$ | $1.539\times10^{-3}$ |

**(c)** Blackman at 3 bins gives a floor of $2.354\times10^{-1}$ (−12.6 dB),
*worse* than the rectangular window's $2.122\times10^{-1}$, while at 8 bins it
gives $3.902\times10^{-4}$ (−68.2 dB), the best of the four. The reason is that
the floor in the 3-bin test is not a sidelobe at all: Blackman's main lobe is 6
bins wide, so at 3 bins the "weak tone" sits *inside* the strong tone's main
lobe, and the local level there is set by the main-lobe skirt, not by the
sidelobe structure. At 8 bins the weak tone is outside every main lobe and the
sidelobe levels decide. **Whether windowing helps depends on how far the
interference is.**

**(d)** The three amplitude corrections, in order.

1. **Divide by the window's coherent gain** (0.5 for Hann) — otherwise every
   amplitude is too small by a factor of 2, i.e. $-6.02$ dB. The failure is
   silent because the spectrum still *looks* like a spectrum.
2. **Account for the deconvolution's regularisation** — the water level biases
   amplitudes low wherever $\lvert H\rvert$ is small (the top of the band and any
   notch), and the size of the bias depends on the noise level that was assumed.
   Omitting it gives correct amplitudes in the middle of the band and
   systematically low amplitudes at the edges, with nothing in the output to
   indicate which is which.
3. **Apply the one-sided factor of 2** on every bin except DC and Nyquist, if a
   one-sided amplitude spectrum is being reported — otherwise amplitudes are
   again too small by a factor of 2, another $-6.02$ dB.

Omitting (1) and (3) together produces amplitudes that are four times too small
while every peak is still in the right place — the classic "the processing made
my amplitudes smaller and nobody noticed" failure, and the reason amplitude
calibration should always be checked against a synthetic input of known amplitude.

---

## ★★★10 — Aliasing versus resolution, and the acquisition compromise

**(a)** The phase difference between neighbouring traces for an event of
frequency $f$ and apparent velocity $v$ is

$$\Delta\phi = k\,dx = \frac{2\pi f}{v}\,dx .$$

The samples can represent the event unambiguously only while
$\lvert\Delta\phi\rvert \le \pi$, since a phase of $\pi+\epsilon$ is
indistinguishable from $-(\pi-\epsilon)$:

$$\frac{2\pi f}{v}dx \le \pi
\qquad\Longrightarrow\qquad
f \le \frac{v}{2\,dx} = f_a .$$

Equality at $f = f_a$ is the degenerate case where the event looks horizontal
(one full cycle between neighbours reads as no phase change at all).

**(b)** With $dx = 25$ m and $v = 350$ m/s,

$$f_a = \frac{350}{2\times25} = 7\ \mathrm{Hz}.$$

The ground-roll band is 5–18 Hz, so the portion from 7 to 18 Hz is **aliased**:
about 11 Hz of the 13 Hz band. Above 7 Hz the phase step between neighbouring
traces passes $180^\circ$ and folds, so part of the ground-roll band appears as
steeply dipping energy with the *opposite* dip sign. On a shot gather this is
recognisable, but only because the dip reverses within the band — a diagnostic
that requires the unaliased low frequencies to remain present.

**(c)** For reflections at 40 Hz with apparent velocity 2500 m/s,

$$f_a = \frac{2500}{2\times25} = 50\ \mathrm{Hz} \ge 40\ \mathrm{Hz},$$

so 25 m spacing is **adequate** for those reflections, with a comfortable margin.

**(d)** The conflict is generic: the reflection requirement calls for large
spacing and the ground-roll requirement for small. The three standard
resolutions.

1. **Reduce $dx$.** Sampling fine enough for the slowest, highest-frequency
   surface wave (here 18 Hz at 350 m/s would need $dx \le 9.7$ m) makes
   everything unaliased. *Cost:* roughly 2.6× more channels in one direction,
   hence more recorders, more cable and more data — the most expensive option,
   and the one that actually solves the problem.
2. **Accept the aliasing and remove the ground roll in another domain.** Aliased
   ground roll still has a coherent, high-amplitude signature; it can often be
   removed by f-k filtering
   ([01-10-07](../07-2d-fourier.md)), by adaptive subtraction, or by
   polarisation/velocity discrimination in a different transform. *Cost:* the
   aliased energy is genuinely ambiguous in the f-k plane — it shares quadrants
   with legitimate signal — so any filter that removes it also removes some
   signal, and the decision must be made with the interpretation in view.
3. **Band-limit the acquisition.** Record only the band in which the surface wave
   is unaliased (here, 5–7 Hz for the ground roll) or attenuate the surface wave
   at source (source arrays, deep burial, receivers with a low-frequency
   response designed to under-represent it). *Cost:* fewer frequencies available
   for deconvolution and for resolution of shallow targets, and often worse
   low-frequency signal-to-noise for the reflections themselves.

Real surveys use a weighted mixture: fine enough sampling for the high
frequencies that matter, source and receiver arrays to suppress the surface wave
in the field, and a processing step that removes the remainder — followed by an
explicit check that the aliased band has not contaminated the migrated image.
