# Exercises — 01-10-04 Discrete Fourier Transform and the FFT

Attempt these **closed-book** before opening the
[solutions](./04-discrete-fourier-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Convention throughout:

$$X[k] = \sum_{n=0}^{N-1}x[n]e^{-2\pi ikn/N}, \qquad
x[n] = \frac{1}{N}\sum_{k=0}^{N-1}X[k]e^{+2\pi ikn/N}, \qquad
df = \frac{1}{N\,dt}.$$

---

## ★ Foundational

**★1.** Compute the full DFT of each 4-sample sequence by hand.

(a) $x = [1,0,0,0]$
(b) $x = [1,1,1,1]$
(c) $x = [1,-1,1,-1]$

---

**★2.** For $x = [1,2,3,4]$, compute $X[0]$, $X[1]$ and $X[2]$ and write down
$X[3]$ using Hermitian symmetry.

---

**★3.** A record has $N = 8$ samples at $dt = 0.5$ s.

(a) State the record length $T$, the bin spacing $df$, and the Nyquist frequency.
(b) State the physical frequency of bins $k = 0, 1, 3$ and $k = 7$.
(c) A tone at 0.75 Hz is present. Which bin carries it, and what would you do to
present a one-sided amplitude spectrum?

---

**★4.** A cosine of amplitude 2.0 is sampled at $N = 64$ samples with the tone
exactly on bin $k_0$.

(a) State $\lvert X[k_0]\rvert$ and $\lvert X[N-k_0]\rvert$.
(b) Give the two correct expressions for recovering the amplitude, and one wrong
one that is off by a factor of 2.
(c) How do the answers change if the signal were replaced by its mean value only
(i.e. $x[n] = 2$ for all $n$)?

---

## ★★ Applied

**★★5.** Show that the DFT is linear, and that shifting a sequence in time
multiplies its spectrum by a linear phase:

$$x[n] \to x[n-n_0] \quad\Longrightarrow\quad X[k] \to X[k]e^{-2\pi ikn_0/N}.$$

Demonstrate the shift property on $x = [1,0,0,0]$ with $n_0 = 1$ in a
4-point transform: compute both spectra explicitly and verify the phase relation.

---

**★★6.** Verify Parseval's relation on $x = [1,1,1,1]$.

(a) Compute $\sum_n\lvert x[n]\rvert^{2}$.
(b) Compute $\sum_k\lvert X[k]\rvert^{2}$ and $\frac1N\sum_k\lvert X[k]\rvert^{2}$.
(c) State the relation and which factor is the common error.

---

**★★7.** A 64-sample record is zero-padded to 256 samples and transformed.

(a) Show that the 256-point spectrum equals the 64-point spectrum at every fourth
bin, i.e. $X_{256}[4k] = X_{64}[k]$.
(b) State the bin spacing before and after padding, for $dt = 1$ s.
(c) Two tones are 0.004 Hz apart. The record is 64 s long. Can padding to 65536
samples separate them? Justify with numbers.

---

**★★8.** Operation counts.

(a) For $N = 1024$, compute $N^{2}$ and $(N/2)\log_2N$, and their ratio.
(b) Repeat for $N = 2^{20}$.
(c) At roughly what $N$ does the direct DFT exceed $10^{12}$ operations, i.e.
become expensive even on a fast machine?
(d) State in one sentence why a factor of 100 matters more than it appears.

---

## ★★★ Research-oriented

**★★★9.** Using [`code/dft_fft_demo.py`](../code/dft_fft_demo.py):

(a) Report the measured times for the direct DFT and the FFT at $N = 256, 512$
and $1024$, and the fitted power-law exponent for each.
(b) The measured FFT exponent is about 1.1 rather than 1.0. Give two reasons.
(c) Show that $\text{time}/(N\log_2N)$ is approximately constant for the FFT,
using your three measurements.
(d) The script reports a maximum absolute difference of about $10^{-10}$ between
the direct DFT and the FFT on a 1024-sample signal, with a relative difference of
about $2\times10^{-13}$. Explain why the direct sum is the less accurate of the
two, and what a relative difference of $10^{-3}$ would indicate.

---

**★★★10.** Sign conventions and the derivative property.

(a) Derive the derivative property for the forward kernel $e^{-2\pi ift}$, and
state what it becomes if the kernel is $e^{+2\pi ift}$.
(b) A 2-D transform uses the kernel
$e^{-2\pi i(k_x x + k_t t)}$. A plane wave has arrival time
$t = t_0 + p\,x$ with $p > 0$. Show that its positive-frequency energy sits at
$k_x = -p\,f$, and explain how this fixes which half-plane of the $f$-$k_x$
plane contains events travelling in the $+x$ direction.
(c) Two processors disagree: one filters "positive $k_x$" for a downgoing wave,
the other filters "negative $k_x$". Explain how they could both be right, and
what document would settle it.
(d) State one observable consequence of mixing the two conventions in an f-k
filter, and one in a migration.
