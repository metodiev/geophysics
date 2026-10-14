# Solutions — 20-02-01 Practical DFT/FFT: Normalisation, Units and Pitfalls

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All models are **SYNTHETIC**.

Lesson: [01 Practical DFT/FFT](../01-dft-fft-practice.md).

---

## ★1 — The convention

$$X[k] = \sum_{n=0}^{N-1} x[n]\,e^{-2\pi ikn/N},
\qquad
x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k]\,e^{+2\pi ikn/N}.$$

- The **forward** transform carries **no** normalisation.
- The **inverse** carries the factor $1/N$.
- The forward exponent is **negative**, the inverse **positive**.
- The negative frequencies are stored in the *second half* of the output array,
  in the order $k = N/2,\dots,N-1$.

A useful sanity statement: $\sum_k \lvert X[k]\rvert^{2} = N\sum_n\lvert x[n]\rvert^{2}$,
so a transform that is not divided by $N$ scales its energy with record length.

---

## ★2 — Reading a spectrum

$$N = 2048,\quad f_s = 512\ \mathrm{Hz}
\;\Longrightarrow\;
\Delta f = \frac{f_s}{N} = \frac{512}{2048} = 0.25\ \mathrm{Hz},$$

and $64\ \mathrm{Hz} = 0.25\times256$ is exactly bin 256, so

$$\lvert X[256]\rvert = \frac{AN}{2} = \frac{1\times2048}{2} = 1024.000,$$

$$\text{amplitude spectrum} = \frac{2\lvert X\rvert}{N}
= \frac{2\times1024}{2048} = 1.000000\ \mathrm{V},$$

$$\text{one-sided PSD} = \frac{2\lvert X\rvert^{2}}{N^{2}\Delta f}
= \frac{2\times1024^{2}}{2048^{2}\times0.25} = 2.000000\ \mathrm{V^{2}\,Hz^{-1}}.$$

**Integral check.** With $\Delta f = 0.25\ \mathrm{Hz}$ the single bin
integrates to $2.0\times0.25 = 0.5\ \mathrm{V^{2}}$, and the sine's mean square
is $A^{2}/2 = 0.5\ \mathrm{V^{2}}$. ✔ The check is exact because the sine is
exactly on a bin.

---

## ★3 — Exact zeros of a pulse's transform

For $L = 40$ in $N = 1000$, $X[k] = 0$ exactly when $kL/N$ is a non-zero
integer, i.e. at multiples of $N/L = 25$:

$$k = 25,\ 50,\ 75,\ 100,\ 125,\ \dots$$

**Rule.** The DFT of a length-$L$ rectangular pulse in an $N$-sample record is the
Dirichlet kernel $\sin(\pi kL/N)/\sin(\pi k/N)$ (up to a linear phase); its
numerator vanishes whenever $kL/N$ is a non-zero integer.

**Why it matters.** A source that repeats at $f_s/25$ has its fundamental and all
harmonics exactly on those zeros. The pulse is then absent from the spectrum
altogether, with no warning sign — the transform is not degraded, it is zero.

---

## ★4 — Scalloping loss at $64.1\ \mathrm{Hz}$

$$\text{bin position} = \frac{64.1}{0.25} = 256.4
\;\Longrightarrow\; \delta = 0.4\ \text{bins from the nearest bin.}$$

$$G(\delta) = \left\lvert\frac{\sin(\pi\delta)}{N\sin(\pi\delta/N)}\right\rvert
= \left\lvert\frac{\sin(0.4\pi)}{2048\sin(0.4\pi/2048)}\right\rvert
= \frac{0.951057}{2048\times6.136\times10^{-4}} = 0.756827 .$$

So the amplitude spectrum would read

$$0.756827\times1.000000 = 0.756827\ \mathrm{V},$$

an under-report of $20\log_{10}(0.756827) = -2.42\ \mathrm{dB}$.

**If you read the peak naively** you would report $0.757\ \mathrm{V}$ for a
$1\ \mathrm{V}$ tone — a $24\%$ amplitude error that is entirely systematic and
repeats exactly. Three-point parabolic interpolation of the log-magnitude peak
reduces this to a few hundredths of a dB; zero-padding the record before the
transform interpolates the same curve and gives the same improvement in the
*estimate*, but not in the resolution (the kernel width in hertz does not
change).

Note the contrast between the two offsets: at $\delta = 0.5$ the loss is
$-3.92\ \mathrm{dB}$ (the worst case, factor $2/\pi$); at $\delta = 0.4$ it is
$-2.42\ \mathrm{dB}$. The loss is minimised (zero) exactly on bin.

---

## ★5 — Testing a reported PSD with Parseval

**What the data imply.** rms $= 1.0\times10^{-4}$, so the mean square is
$1.0\times10^{-8}$ in signal units squared. For a flat spectrum over the
one-sided band $0 \le f \le f_s/2 = 100\ \mathrm{Hz}$,

$$\text{PSD}_{\text{flat}} = \frac{\text{mean square}}{f_s/2}
= \frac{1.0\times10^{-8}}{100} = 1.0\times10^{-10}\ \text{per Hz}.$$

**Verdict.** The reported $1.0\times10^{-9}$ is a factor of **10** too large. It
is not a one-sided density over this band.

**The likely error, ranked.** The candidates and their factors are:

| hypothesis | factor by which it changes the number |
|---|---|
| reported as a **two-sided** density (whose integral over $0..f_s/2$ is half the power) | 2 |
| reported as **power per bin** (multiply by $\Delta f = 1/(N\Delta t)$) | $\Delta f = 0.005$ for a 100 s, 200 Hz record |
| reported with a $\Delta f$ based on the wrong record length | arbitrary |
| reported from a **different** record than the rms quoted | arbitrary |

The factor 10 is not reproduced by the two-sided/one-sided mix-up (factor 2), so
the most likely explanation is that the number is a **power per bin** divided by
the wrong bandwidth, or that it came from a different record. Concretely: a
100 s record at 200 Hz has $N = 20000$ samples and $\Delta f = 0.01\ \mathrm{Hz}$;
a *two-sided* periodogram bin value in signal² is
$\lvert X\rvert^{2}/N^{2} = $ PSD$\times\Delta f$ = $1.0\times10^{-10}\times0.01 =
1.0\times10^{-12}$ per bin. To reach $10^{-9}$ from a correct PSD one would have
to divide by $\Delta f = 0.1\ \mathrm{Hz}$, which corresponds to a 2 s record —
ten times shorter than stated. That is the diagnosis to put back to the
colleague: check the record length used in the normalisation.

**The lesson.** A PSD without its units, its scaling convention (`density` versus
`spectrum`) and its record length is not verifiable. With those three things,
Parseval verifies it in one line.

---

## ★6 — A pure on-bin exponential

With $N = 128$, $k_0 = 3$:

$$X[3] = \sum_{n=0}^{127}e^{+2\pi i\cdot3n/128}e^{-2\pi i\cdot3n/128}
= \sum_{n=0}^{127}1 = 128,$$

$$X[4] = \sum_{n=0}^{127}e^{-2\pi i n/128}
= \frac{1-e^{-2\pi i}}{1-e^{-2\pi i/128}} = 0,$$

because the 128th roots of unity sum to zero. So the transform is
$128$ at the single bin $k_0$ and zero elsewhere — the identity quoted in the
lesson (measured as $\lvert X[9]\rvert = 64.000000$ with $N = 64$ and all other
bins at the $10^{-14}$ rounding level).

**The $k_0 = 131$ case.** Since $e^{+2\pi i\cdot131n/128}
= e^{+2\pi i\cdot3n/128}e^{+2\pi i\cdot128n/128} = e^{+2\pi i\cdot3n/128}$, the
*same* samples are produced and the DFT is again $128$ at bin 3. Nothing aliases
*inside the DFT*: the transform is a bijection on $\mathbb{C}^{N}$, and any
integer $k_0$ maps to the same vector of samples modulo $N$, so the transform
correctly returns bin $3$. The physical statement — that a continuous-time
$131\ \mathrm{Hz}$ tone sampled at $128\ \mathrm{Hz}$ is indistinguishable from a
$3\ \mathrm{Hz}$ tone — is a statement about *sampling*, not about the transform,
and it is settled by
[20-01-05](../../01-signals-and-systems/05-sampling-theory.md)'s fold map, not by any
property of the DFT. Keeping these two facts separate prevents a common
misattribution: the DFT does not alias, samplers do.

---

## ★7 — A DFT test suite

| bug | test that fails | expected residual when correct |
|---|---|---|
| normalisation ($1/N$ missing or doubled) | Parseval: $\lvert\sum x^{2} - \frac1N\sum\lvert X\rvert^{2}\rvert$ | $\lesssim10^{-13}$ relative, $\sim N\epsilon$ |
| bin off-by-one | $\mathrm{DFT}$ of $e^{2\pi ik_0n/N}$ must have $\lvert X[k_0]\rvert = N$ and zeros elsewhere | zeros at $\sim10^{-14}N$ |
| missing $2/N$ in the amplitude spectrum | amplitude of a unit on-bin sine must be $1.000000$ for every $N$ | $10^{-14}$ |
| Nyquist bin doubled | one-sided sum used in Parseval must equal $\sum x^{2}$ exactly | $0$ to $10^{-13}$ |
| leakage assumed | the DFT of a boxcar must match $D(2\pi k/N,L)$ analytically | $10^{-13}$ |

**Tolerance policy.** Compare against exact identities with a relative tolerance
of $10^{-12}$ (double precision loses about $\log_{10}N$ digits to accumulation,
so $10^{-13}$ is a realistic floor for $N\lesssim10^{4}$), and never demand
bit-equality between two FFT implementations.

**The bug no spectral test can catch: undersampling.** If the record was
collected below Nyquist, the spectrum of the samples is a perfectly valid
spectrum of the samples; it is simply a spectrum of a *different* signal than the
one you believe you recorded. Every test in the table passes. The only detection
is external — a second record at a different rate, a known source spectrum, or
the anti-alias filter's documented response.

---

## ★8 — Detecting a weak monochromatic signal (specification)

**Record and window.** Search band $0.05$–$2\ \mathrm{Hz}$, so the required
resolution is well below the band edges: use $N$ such that
$\Delta f \lesssim 0.005\ \mathrm{Hz}$, i.e. a record of $200\ \mathrm{s}$ at
$f_s = 1\ \mathrm{Hz}$ ($N = 200$; $\Delta f = 0.005\ \mathrm{Hz}$) or longer for
a finer grid. Use a **Hann** window so that a strong low-frequency noise peak
does not leak across the band ([20-02-03](../03-windowing-advanced.md)); accept
its $1.5$-bin ENBW cost.

**Estimator.** Welch-averaged PSD with $K$ segments of half-overlap, or a
multitaper estimate with $K$ DPSS tapers — either gives a $\chi^{2}_{2K}$-like
distribution. The relevant result from lesson 20-02-02: a single periodogram
ordinate has a standard deviation equal to its mean (100 % uncertainty), while
averaging $K$ independent estimates reduces that to $1/\sqrt{K}$.

**Threshold.** For a search over $M$ independent frequency bins, set the
detection threshold at the level where the probability of any false alarm is
$\alpha$:

$$P_{\text{fa, per bin}} = 1-e^{-P_{\text{th}}/P_{\text{noise}}},$$

so $P_{\text{th}} \approx P_{\text{noise}}\ln(M/\alpha)$ for small $\alpha$ — an
exponential-distribution result, valid for a single periodogram ordinate.

**Smallest detectable amplitude.** With $M \approx 400$ independent bins in
$0.05$–$2\ \mathrm{Hz}$ at a $0.005\ \mathrm{Hz}$ grid and $\alpha = 0.01$,

$$\ln(M/\alpha) = \ln(400/0.01) = \ln 40000 = 10.60,$$

so the threshold is $10.6\times$ the mean noise power, and a tone must have a
power-spectral peak at least that large. For a coherent sinusoid of amplitude $A$
in white noise of amplitude spectral density $S^{1/2}$, the peak signal power in
a bin after windowing depends on the window's ENBW; with a Hann window the
matched-filter argument gives a detectable $A$ of order

$$A \gtrsim \sqrt{8\,P_{\text{th}}\,\Delta f}\ \text{in amplitude units},$$

which for the threshold above and $\Delta f = 0.005$ is about
$\sqrt{0.42\,P_{\text{noise}}}$ — i.e. roughly $0.65$ of the *per-bin* noise
amplitude, or a factor $1/\sqrt{N_{\text{eff}}}$ better than the
single-sample level because the coherent sum over the record averages the noise.

**Bound versus estimate.** The probability calculation is an **exact** statement
for independent periodogram ordinates with exponential statistics. Everything
about the amplitude is an **estimate**: the conversion from threshold power to
detectable amplitude depends on the window's ENBW, on whether the tone is exactly
on-bin (scalloping loss up to $3.9\ \mathrm{dB}$), and on the searched bandwidth
in the exact way the multiple-comparison factor $\ln(M/\alpha)$ encodes. State
the window, the number of independent bins and the assumed noise model beside the
number, or the number means nothing.

**The reported claim to a colleague:** "a tone 100 times weaker in amplitude than
the broadband rms is detectable with 99 % confidence in a 200 s record, given a
Hann taper, $K = 8$ averaged segments and independent bins over
$0.05$–$2\ \mathrm{Hz}$" — and with the honest caveat that a *drift* in the
instrument or a *coloured* noise floor invalidates the white-noise assumption
before it invalidates the threshold.


---

## Mastery checkpoint answers

**(b)** $N = 2048$, $f_s = 512\ \mathrm{Hz}$:
$\Delta f = 512/2048 = 0.25\ \mathrm{Hz}$; $64\ \mathrm{Hz} = $ bin 256;
raw peak $\lvert X\rvert = AN/2 = 1024.000$; amplitude spectrum
$2\lvert X\rvert/N = 1.000000\ \mathrm{V}$; one-sided PSD
$2\lvert X\rvert^{2}/(N^{2}\Delta f) = 2.000000\ \mathrm{V^{2}\,Hz^{-1}}$.

**(c)** $64.1/0.25 = 256.4$, so the tone is $0.4$ bin from the nearest bin and the
Dirichlet factor is
$\lvert\sin(0.4\pi)/(2048\sin(0.4\pi/2048))\rvert = 0.756827$: the amplitude
spectrum reads $0.756827\ \mathrm{V}$ and the shortfall is
$20\log_{10}0.756827 = -2.42\ \mathrm{dB}$.

**(e)** A 40-sample pulse in a 1000-sample record has exact zeros at multiples of
$N/L = 25$: $k = 25, 50, 75, 100, 125$ (and so on).
