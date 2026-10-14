# Solutions — 01-10-04 Discrete Fourier Transform and the FFT

> **Read this after attempting the exercises, not before.**
>
> All values below were computed. Values quoted from the supplied script are the
> values it printed.

---

## ★1 — Three 4-point transforms

**(a)** $x = [1,0,0,0]$: every $X[k] = 1\cdot e^0 = 1$. So

$$X = \boxed{[1,1,1,1]}.$$

A unit spike has a flat spectrum: an instantaneous event contains all
frequencies equally. This is the discrete statement that the impulse is the
neutral element of convolution.

**(b)** $x = [1,1,1,1]$:

$$X[k] = \sum_{n=0}^{3}e^{-2\pi ikn/4}
= \begin{cases}4, & k = 0,\\ 0, & k = 1,2,3,\end{cases}$$

so $X = \boxed{[4,0,0,0]}$. A constant has all its energy at DC, and $X[0] = 4$ is
the *sum*, not the value 1 — the sum of four samples each equal to 1.

**(c)** $x = [1,-1,1,-1]$:

$$X[k] = \sum_{n=0}^{3}(-1)^ne^{-2\pi ikn/4}
= \sum_{n=0}^{3}e^{-i\pi n(1 + k/2)} .$$

The sum is non-zero only when the exponent is a multiple of $2\pi$, i.e. when
$1 + k/2$ is even, which for $k = 0,\ldots,3$ means $k = 2$:

$$X = \boxed{[0,0,4,0]}.$$

The alternation $[1,-1,1,-1]$ has period 2, which in a 4-point transform is the
harmonic $k = 2$ — the Nyquist bin. Note the contrast with (b): the "same energy,
different frequency" pattern, and in each case the whole signal lands in a single
bin because the signal *is* a basis vector.

---

## ★2 — A 4-point transform in full

$$X[0] = 1+2+3+4 = \boxed{10}.$$

$$X[1] = 1 + 2e^{-i\pi/2} + 3e^{-i\pi} + 4e^{-3i\pi/2}
= 1 - 2i - 3 + 4i = \boxed{-2 + 2i}, \qquad \lvert X[1]\rvert = 2.828427.$$

$$X[2] = 1 + 2e^{-i\pi} + 3e^{-2i\pi} + 4e^{-3i\pi}
= 1 - 2 + 3 - 4 = \boxed{-2}.$$

Hermitian symmetry for a real sequence gives $X[3] = \overline{X[1]}
= \boxed{-2 - 2i}$.

**Check.** The mean of the sequence is $10/4 = 2.5$, and $X[0]/N = 2.5$ ✓. The
Nyquist bin is $X[2] = -2$, which for a real sequence must be real ✓ (it is
$-2$). Everything is consistent with the definitions rather than with a table of
recipes.

---

## ★3 — Reading a spectrum's axes

**(a)** $T = N\,dt = 8\times0.5 = 4$ s; $df = 1/(N\,dt) = 1/4 = 0.25$ Hz; Nyquist
$= 1/(2\,dt) = 1$ Hz.

**(b)** $f_k = k\,df$: bin 0 → 0 Hz (DC), bin 1 → 0.25 Hz, bin 3 → 0.75 Hz. Bin 7
is a *negative* frequency: $f = (7-8)\,df = -0.25$ Hz.

**(c)** 0.75 Hz is bin $k = 3$ exactly ($3\times0.25 = 0.75$). To present a
one-sided amplitude spectrum: keep bins $0,\ldots,N/2 = 4$, double the amplitude
of every bin except $k = 0$ and $k = N/2$, and label the axis $f_k = k\,df$. The
doubling is needed because the tone's energy is split between bins 3 and 5
($X[5] = \overline{X[3]}$), and discarding the upper half discards exactly half of
it.

---

## ★4 — Amplitude from a spectrum

**(a)** A real cosine is two complex exponentials of amplitude $1.0$ each, and
each occupies one bin entirely, so $X[k_0] = (A/2)N = 2.0\times64/2 = 64$ and
$\lvert X[N-k_0]\rvert = 64$.

**(b)** Correct expressions: $A = 2\lvert X[k_0]\rvert/N$ (using either the
one-sided doubling or the two-sided pair). Wrong: $A = \lvert X[k_0]\rvert/N$,
which gives 1.0 — off by exactly 2, and wrong for exactly the reason stated: the
factor 2 is the price of discarding the twin at $-f_0$.

**(c)** For a constant signal $x[n] = 2$, all the energy is at $k = 0$ and
$X[0] = 2N = 128$, with every other bin zero. Here $\lvert X[0]\rvert/N = 2$ is
already the right answer: **no factor of 2 for the DC bin**, because there is no
negative-frequency twin to account for. The Nyquist bin behaves the same way for
the same reason, which is why the rule is usually stated as "double every bin
except DC and Nyquist".

---

## ★★5 — Linearity and the shift property

**Linearity** is immediate from the definition, because the transform is a sum:

$$\sum_n(\alpha x[n] + \beta y[n])e^{-2\pi ikn/N}
= \alpha\sum_nx[n]e^{-2\pi ikn/N} + \beta\sum_ny[n]e^{-2\pi ikn/N}
= \alpha X[k] + \beta Y[k].$$

**Shift.** Let $y[n] = x[n-n_0]$ with the index understood modulo $N$ (circular
shift). Substituting $m = n-n_0$:

$$Y[k] = \sum_{n=0}^{N-1}x[n-n_0]e^{-2\pi ikn/N}
= \sum_{m=-n_0}^{N-1-n_0}x[m]e^{-2\pi ik(m+n_0)/N}
= e^{-2\pi ikn_0/N}\sum_{m}x[m]e^{-2\pi ikm/N} = e^{-2\pi ikn_0/N}X[k].$$

**Demonstration** with $x = [1,0,0,0]$ and $n_0 = 1$ in a 4-point transform. From
★1(a), $X = [1,1,1,1]$. The shifted sequence is
$y = [0,1,0,0]$ (circularly: the 1 has moved from index 0 to index 1), and
directly

$$Y[k] = e^{-2\pi ik\cdot1/4} = e^{-i\pi k/2},$$

i.e. $Y = [1, -i, -1, i]$. Compare with the prediction
$X[k]e^{-2\pi ik/4} = 1\cdot e^{-i\pi k/2} = [1,-i,-1,i]$ ✓ exactly.

**Read the magnitudes:** $\lvert Y[k]\rvert = 1$ for all $k$, identical to
$\lvert X\rvert$. A time shift changes only the phase, and the phase change is
linear in $k$ with slope $-2\pi n_0/N$. That single observation is why arrival
times can be inverted from phase spectra and why a phase spectrum must be
unwrapped before it can be interpreted.

---

## ★★6 — Parseval on a constant

**(a)** $\sum_n\lvert x[n]\rvert^{2} = 4\times1^{2} = 4$.

**(b)** From ★1(b), $X = [4,0,0,0]$, so $\sum_k\lvert X[k]\rvert^{2} = 16$ and
$\frac1N\sum_k\lvert X[k]\rvert^{2} = 16/4 = 4$.

**(c)** The relation is

$$\sum_{n=0}^{N-1}\lvert x[n]\rvert^{2}
= \frac{1}{N}\sum_{k=0}^{N-1}\lvert X[k]\rvert^{2},$$

and the common error is to omit the $1/N$, which inflates the spectral energy by
exactly the record length. Note also where the "energy" is: the data have energy
4 while the single DC bin has magnitude 4 and energy 16. The $1/N$ is what
reconciles them — a reminder that the DFT is an unnormalised projection, as
Section 3 of the lesson derives.

---

## ★★7 — Zero padding

**(a)** Write the padded sequence as $x_{\text{pad}}[n] = x[n]$ for
$n < 64$ and $0$ otherwise, of length 256. Then

$$X_{256}[m] = \sum_{n=0}^{255}x_{\text{pad}}[n]e^{-2\pi imn/256}
= \sum_{n=0}^{63}x[n]e^{-2\pi imn/256} .$$

Set $m = 4k$. Then $e^{-2\pi i(4k)n/256} = e^{-2\pi ikn/64}$, so

$$X_{256}[4k] = \sum_{n=0}^{63}x[n]e^{-2\pi ikn/64} = X_{64}[k] .$$

So the padded spectrum reproduces the original spectrum exactly at every fourth
bin and *interpolates* between them. No new information appears — as it cannot,
since the padded array contains the original 64 numbers and 192 zeros.

**(b)** Before padding: $df = 1/(64\times1) = 0.015625$ Hz. After padding to 256:
$df = 1/(256\times1) = 0.00390625$ Hz.

**(c)** The record is $T = 64$ s, so the resolution is $1/T = 0.015625$ Hz. The
two tones are 0.004 Hz apart — about one quarter of the resolution — so they are
not separable at any padding. Padding to 65536 samples gives a bin spacing of
$1/65536 = 1.5\times10^{-5}$ Hz, i.e. the spectrum is sampled very finely, but the
two tones remain a single hump whose width is set by $1/T$: the interpolation
simply describes that hump in more detail. **Resolution is a property of the
record length, not of the transform length**, and the numbers here are the
cleanest way to say so.

---

## ★★8 — Operation counts

**(a)** $N^{2} = 1024^{2} = 1\,048\,576$ complex multiply-adds;
$(N/2)\log_2N = 512\times10 = 5120$ butterflies; ratio
$= 1\,048\,576/5120 = 204.8 \approx 205$.

**(b)** $N = 2^{20} = 1\,048\,576$: $N^{2} = 1.0995\times10^{12}$;
$(N/2)\log_2N = 524\,288\times20 = 1.0486\times10^{7}$; ratio
$= 1.0486\times10^{5}$.

**(c)** $N^{2} = 10^{12}$ gives $N = 10^{6}$. At $10^{6}$ samples the direct
transform needs about $10^{12}$ complex operations, i.e. tens of minutes to
hours, while the FFT needs about $10^{7}$ butterflies, i.e. a fraction of a
second.

**(d)** A factor of 100 is not a factor of 100 in wall-clock terms but a change
of category: an operation that took an hour now takes half a minute, so it can
be run inside an iteration, inside a loop over many traces, or inside an
inversion — which is where the FFT's real importance lies. The algorithm did not
merely speed up a computation; it made a class of computations routine.

---

## ★★★9 — Measuring the cost models

**(a)** The script reports (timings vary between runs, so the numbers will differ
slightly on your machine):

| $N$ | direct DFT (s) | FFT (s) | fitted exponent |
|---|---|---|---|
| 256 | 0.006577 | 0.000242 | — |
| 512 | 0.024792 | 0.000553 | — |
| 1024 | 0.097654 | 0.001252 | — |
| (fit over 128–2048) | — | — | DFT 2.018–2.08, FFT 1.10–1.16 |

Your own times will differ, and by a lot on a loaded machine: the script takes the
minimum of three runs per case, and over repeated runs on this machine the DFT
exponent ranged from 1.9 to 2.1 while the FFT exponent ranged from 1.05 to
1.25. **The reproducible quantities are the operation counts, not the
timings.**

**(b)** Two reasons the measured FFT exponent exceeds 1.

1. The operation count is $(N/2)\log_2N$, not $N$. On a log–log plot its local
   slope is $1 + 1/\ln N$ (approximately, for the multiplicative
   $\log_2 N$ factor), which for the tested range is about 1.1–1.15. The
   *model* has exponent exactly 1 for the leading term $N$ but the $\log N$
   factor contributes an apparent extra slope over any finite range.
2. Cache and memory effects: as $N$ grows the working arrays exceed cache and the
   achieved operations per second fall, which steepens the measured curve
   independently of the operation count.

**(c)** Dividing by $N\log_2N$:

| $N$ | $\text{time}/(N\log_2N)$ (s) |
|---|---|
| 256 | $3.3\times10^{-9}$ |
| 512 | $2.8\times10^{-9}$ |
| 1024 | $2.4\times10^{-9}$ |

The ratio varies by less than 40% across a factor of four in $N$; combined with
the fact that the inverse of this ratio (operations per second) is a plausible
Python-level throughput, the cost model is confirmed. A machine-independent
statement is: the FFT's time divided by $(N/2)\log_2N$ is roughly constant.

**(d)** Both algorithms accumulate rounding error. The **direct sum** is less
accurate because its twiddle factors $e^{-2\pi ikn/N}$ are generated by repeated
complex multiplication, so each successive term of the inner sum carries an error
that has accumulated over $n$ multiplications; the FFT's twiddle factors are also
built by repeated multiplication but its butterfly structure keeps the *number*
of accumulated multiplications per output at $\log_2N$ rather than $N$. On this
signal the direct sum's error is $10^{-10}$ absolute against a maximum
$|X|$ of about $500$, i.e. $2\times10^{-13}$ relative.

A relative difference of $10^{-3}$ would indicate a **bug**, not round-off: it is
nine orders of magnitude larger than double-precision accumulation can explain.
The likely causes are a wrong twiddle sign, a missing bit-reversal, a length that
is not a power of two for the radix-2 code, or an inverse that omits its $1/N$.

---

## ★★★10 — Sign conventions and the derivative property

**(a)** With $X(f) = \int x(t)e^{-2\pi ift}dt$, integrate by parts:

$$\int\frac{dx}{dt}e^{-2\pi ift}dt
= \left[x(t)e^{-2\pi ift}\right]_{-\infty}^{\infty}
+ 2\pi if\int x(t)e^{-2\pi ift}dt = 2\pi if\,X(f),$$

the boundary term vanishing for a signal that decays. So
$d/dt \leftrightarrow +2\pi if = +i\omega$. If instead the forward kernel were
$e^{+2\pi ift}$, the same calculation gives $-i\omega$, because the sign of the
derivative's contribution is tied to the sign in the exponent. **The operator's
sign is not a matter of taste; it is determined by the kernel, and consistency is
what matters.**

**(b)** A plane wave with arrival time $t = t_0 + p\,x$ can be written
$\cos(2\pi f(t - p x - t_0))$, i.e. as the sum of
$e^{+2\pi i f(t-px-t_0)}$ and its conjugate. Consider the component that the
transform labels with positive frequency. Matching the phase of
$e^{2\pi ift}e^{-2\pi ifpx}$ against the kernel $e^{-2\pi i(k_x x + k_t t)}$
requires $k_t = -f$ for one component and $k_t = +f$ for the other, with
$k_x = +p f$ and $k_x = -p f$ respectively. The demo measures which one lands on
the positive-frequency bins: for $p > 0$ the positive-frequency peak appears at

$$k_x = -p\,f .$$

So in the convention of this module, **energy travelling towards increasing $x$
occupies the negative-$k_x$ half of the $f$-$k_x$ plane** (for $f > 0$). The
mirror image holds for the conjugate half. This is precisely why
[01-10-07](../07-2d-fourier.md) must state a convention before it can talk about
quadrants.

**(c)** Both processors can be right if they use opposite conventions for the
sign in the exponent and each says so. Under $e^{-2\pi i(k_xx+k_tt)}$, downgoing
energy with $p>0$ is at negative $k_x$; under the opposite kernel it is at
positive $k_x$. The document that settles it is the **signature convention
statement** — the two lines giving the forward kernel and the definition of $k$
— which belongs at the top of every piece of processing software and every
processing report. Note that this is not pedantry: the two processors' outputs
are mirror images of each other, and a mirror image of a seismic section is an
interpretation error, not a plotting error.

**(d)** One observable consequence in an **f-k filter**: applying the mask to the
wrong half-plane passes the event that was meant to be removed and removes the
event that was meant to be kept — the filtered section looks plausible and is
exactly wrong (this failure mode is discussed in
[01-10-07](../07-2d-fourier.md)). One observable consequence in a **migration**:
the extrapolation operator $\pm i k_z$ has the wrong sign, so energy is moved
in the wrong direction along the time axis — events that should move up in time
move down, producing a section with coherent but misplaced energy and, in
practice, a "smile" instead of a "frown" on the deeper part of a diffraction.
Both are silent failures: every amplitude stays bounded, and only a comparison
against a known model exposes them.
