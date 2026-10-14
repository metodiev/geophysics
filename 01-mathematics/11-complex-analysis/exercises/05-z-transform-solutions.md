# Solutions — 01-11-05 The z-Transform and Discrete Linear Systems

> **Read this after attempting the exercises, not before.**
>
> Values quoted as "measured" come from the companion script in
> [`../code/`](../code/ztransform_demo.py).

---

## ★1 — Transforms and regions

**(a)** $X(z) = 1$ for all $z$: a single impulse has no memory, and its transform
converges everywhere.

**(b)** $X(z) = 1 + 2z^{-1} + 3z^{-2}$, which converges for all
$z \neq 0$ — the only "convergence" condition for a finite sequence, since the sum
has three terms.

**(c)** $X(z) = \sum_{n\ge0}z^{-n} = 1/(1-z^{-1})$, convergent for $|z|>1$. The
pole is on the unit circle, at $z=1$.

**(d)** $X(z) = 1/(1-0.5z^{-1})$, convergent for $|z|>0.5$: outside the circle
through the pole.

**Why the region matters.** (c) and (d) are the same *form* with the pole
radius playing the role of a parameter; the region is what tells you the sequence
is right-sided. For a finite sequence the region is the whole plane except
possibly $z = 0$ or $z = \infty$, which is why FIR filters have no stability
question.

---

## ★2 — Two inverses of one formula

**(a) $|z| > 0.5$ (causal).** Expand in powers of $z^{-1}$:

$$\frac{1}{1-0.5z^{-1}} = \sum_{n=0}^{\infty}0.5^{n}z^{-n}
\qquad\Longrightarrow\qquad x[n] = 0.5^{n}u[n].$$

**(b) $|z| < 0.5$ (anti-causal).** Now expand in powers of $z$:

$$\frac{1}{1-0.5z^{-1}} = \frac{-z/0.5}{1-z/0.5}
= -\sum_{n=1}^{\infty}0.5^{-n}z^{n}
\qquad\Longrightarrow\qquad x[n] = -0.5^{n}u[-n-1].$$

**What changes.** Only the region. The algebraic expression $1/(1-0.5z^{-1})$
does not determine the sequence; it determines *two* sequences, one of which
grows to the left of the origin and one of which decays to the right. This is the
discrete version of the same ambiguity in the Laplace transform, and it is why a
stated region is part of a transform rather than a footnote to it.

---

## ★3 — A first-order recursive filter

**(a)** Transforming with zero initial conditions (so
$\mathcal{L}$-style shift terms vanish and $z^{-1}$ is the delay):

$$Y(z) = 0.8z^{-1}Y(z) + X(z) - 0.5z^{-1}X(z),$$

$$H(z) = \frac{1-0.5z^{-1}}{1-0.8z^{-1}}
= \frac{z-0.5}{z-0.8}\cdot\frac{z}{z} = \frac{z-0.5}{z-0.8}\ \text{(after clearing } z^{-1}\text{)}.$$

Carefully: multiplying numerator and denominator by $z$ gives
$H(z) = (z-0.5)/(z-0.8)$, so the finite zero is at $z = 0.5$ and the finite pole
at $z = 0.8$.

**(b)** Pole $z = 0.8$, zero $z = 0.5$. Stable: the single pole has
$|0.8| < 1$, and the system is causal. (The zero's position affects the amplitude
response but not stability.)

**(c)** Run $h[n] = 0.8h[n-1] + \delta[n] - 0.5\delta[n-1]$ with $h[-1]=0$:

| $n$ | computation | $h[n]$ |
|---|---|---|
| 0 | $0 + 1 - 0$ | 1.000000 |
| 1 | $0.8(1) + 0 - 0.5$ | 0.300000 |
| 2 | $0.8(0.3) + 0$ | 0.240000 |
| 3 | $0.8(0.24)$ | 0.192000 |

From $n\ge2$ the response is purely $h[n] = 0.3\cdot0.8^{\,n-1}$, i.e. a
geometric decay with ratio $0.8$: the pole radius, as expected.

---

## ★4 — A two-tap differencing filter

$H(z) = 1 - 0.5z^{-1}$, so $h[0] = 1$, $h[1] = -0.5$ and $h[n]=0$ thereafter: an
FIR filter with two coefficients.

$$|H(e^{i\omega})| = |1-0.5e^{-i\omega}|
= \sqrt{(1-0.5\cos\omega)^{2} + 0.25\sin^{2}\omega}
= \sqrt{1.25-\cos\omega}.$$

| $\omega$ | $\vert H\vert$ |
|---|---|
| $0$ (DC) | $\sqrt{0.25} = 0.500000$ |
| $\pi/2$ | $\sqrt{1.25} = 1.118034$ |
| $\pi$ (Nyquist) | $\sqrt{2.25} = 1.500000$ |

**Description:** a gentle **high-pass** (or "differencing" or "derivative-like")
filter: it attenuates low frequencies, peaks at Nyquist, and its phase response is
linear in frequency because the impulse response is symmetric about a
half-sample — so it introduces no waveform distortion, only a half-sample shift.
Note that the maximum gain exceeds unity ($1.5$), so the filter *amplifies* as
well as shapes; that must be accounted for when chaining filters.

---

## ★★5 — The two-point moving average

**(a)**

$$H(e^{i\omega}) = \frac{1+e^{-i\omega}}{2}
= e^{-i\omega/2}\frac{e^{i\omega/2}+e^{-i\omega/2}}{2}
= e^{-i\omega/2}\cos\frac{\omega}{2},$$

so $|H| = |\cos(\omega/2)|$ and the phase is $-\omega/2$: linear phase, i.e. a
pure half-sample delay with no distortion.

**(b)** Nulls where $\cos(\omega/2) = 0$, i.e. $\omega = \pi$ — only the Nyquist
frequency. (And at $\omega = 3\pi$, outside the principal interval.) A two-point
average therefore kills the Nyquist component exactly, which is why it is used as
a cheap anti-alias pre-filter before decimation by two.

**(c)** Applying it twice multiplies the transfer functions:

$$H^{2}(z) = \left(\frac{1+z^{-1}}{2}\right)^{2}
= \frac{1+2z^{-1}+z^{-2}}{4},$$

a three-coefficient FIR. Its zeros are at $z = -1$ **twice**: a double zero, so
the magnitude has a *second-order* null at Nyquist,
$|H|^{2} = \cos^{2}(\omega/2)$.

**(d)** **Prefer longer:** a longer average has a narrower main lobe, so it
attenuates a wider band before Nyquist rather than only at Nyquist. **Avoid:** its
magnitude response has side lobes (the Dirichlet kernel), so a strong event at a
frequency near a side-lobe peak passes with little attenuation while the passband
is unnecessarily attenuated; and every extra tap costs resolution, since the
averaging length sets the shortest resolvable feature. The usual compromise is a
tapered (windowed) average, which trades side-lobe level against main-lobe width
([01-10-05 Window
leakage](../../10-fourier-analysis/05-windowing-aliasing.md)).

---

## ★★6 — A narrow-band resonator

**(a)** With poles at $re^{\pm i\omega_{0}}$,

$$H(z) = \frac{1}{1-2r\cos\omega_{0}z^{-1}+r^{2}z^{-2}},
\qquad r = 0.98,\ \omega_{0} = \pi/4 .$$

The resonance frequency is $f_{0} = \omega_{0}/(2\pi)$ cycles per sample; with one
sample per second, $f_{0} = 0.125$ Hz.

**(b)** $1/[(1-r)2\sin\omega_{0}] = 1/[0.02\times2\times0.707107] = 35.355339$. The
exact peak (measured by a fine scan) is $35.712464$ at
$\omega = 0.785193960$ rad, so the approximation is **low by $1.0\%$**. The bias
is always in that direction for a resonator with a pole angle not near
$\omega = 0$: the approximation drops the contribution of the conjugate pole.

**(c)** The measured $-3$ dB crossings are at $0.764776749$ and $0.805204334$ rad,
so

$$\text{bandwidth} = 0.040427585\ \mathrm{rad},
\qquad Q = \frac{\omega_{0}}{\text{bandwidth}} = 19.427284 .$$

The scaling $Q\approx\omega_{0}/[2(1-r)] = 0.785398/0.04 = 19.634954$ is high by
about $1.1\%$ — the same order of error as the peak height, and for the same
reason. Note that the bandwidth in rad is $0.040427585$ against $2(1-r) = 0.04$:
the estimate $2(1-r)$ is a *good* first approximation, and better than the peak
height estimate because it involves a ratio in which the approximations partly
cancel.

**(d)** With $r = 0.9$: the peak height collapses from about $35.7$ to about
$1/[0.1\times2\times0.707107] = 7.07$ (an inverse-proportionality in $(1-r)$), and
$Q$ halves to about $9.8$. The pole angle is unchanged, so the *frequency* of the
resonance is unchanged — moving the pole radially changes sharpness only. That is
the design rule: angle sets frequency, radius sets sharpness.

---

## ★★7 — Removing DC and Nyquist

**(a)** Place zeros at $z = 1$ (DC) and $z = -1$ (Nyquist):

$$H(z) = \frac{(1-z^{-1})(1+z^{-1})}{4} = \frac{1-z^{-2}}{4},$$

and indeed $H(1) = 0$ and $H(-1) = (1-1)/4 = 0$. The impulse response is
$h[0] = 1/4$, $h[1] = 0$, $h[2] = -1/4$: a three-tap filter whose central tap is
zero (the $1/4$ normalisation is conventional — choose any scale you like).

**(b)**

$$|H(e^{i\omega})| = \left|\frac{1-e^{-2i\omega}}{4}\right|
= \frac{|2\sin\omega|}{4} = \frac{|\sin\omega|}{2},$$

using $1-e^{-2i\omega} = e^{-i\omega}(e^{i\omega}-e^{-i\omega}) = 2ie^{-i\omega}
\sin\omega$.

**(c)** $|\sin\omega|$ peaks at $\omega = \pi/2$, where $|H| = 1/2$. That is the
**Nyquist-rate** frequency — one quarter of the sampling rate — and the filter
passes it with gain exactly one half.

**(d)** **DC null mandatory:** any processing of a record with an unknown
constant offset, a drifting instrument, or a trend that would otherwise leak into
every low-frequency estimate (a DC component makes the spectrum's lowest bins
meaningless and biases autocorrelation-based deconvolution). **Nyquist null
destructive:** broadband seismic data with usable energy up to Nyquist — for
example, a high-resolution shallow survey in which the interesting reflections sit
at $60$–$90\%$ of Nyquist. Nulling Nyquist also nulls a band around it (the null
is only exact at $\omega = \pi$, but the attenuation nearby is strong), and in a
migrated section that shows up as a loss of resolution rather than as a visible
artefact.

---

## ★★8 — Linear versus circular convolution by hand

**(a) Linear convolution** (length $4+2-1 = 5$):

$$(x*h)[n] = \sum_{k}x[k]h[n-k]
= \begin{cases}
1 & n=0\\
1 & n=1\\
1 & n=2\\
1 & n=3\\
-4 & n=4
\end{cases}
\qquad\text{i.e. } \{1,1,1,1,-4\}.$$

**(b) 4-point circular convolution** uses $k$ modulo 4:

$$\begin{aligned}
y[0] &= x[0]h[0] + x[3]h[1] = 1 - 4 = -3,\\
y[1] &= x[1]h[0] + x[0]h[1] = 2 - 1 = 1,\\
y[2] &= x[2]h[0] + x[1]h[1] = 3 - 2 = 1,\\
y[3] &= x[3]h[0] + x[2]h[1] = 4 - 3 = 1 .
\end{aligned}$$

So $y = \{-3, 1, 1, 1\}$.

**(c)** Comparing: the linear result is $\{1,1,1,1,-4\}$ and the circular one is
$\{-3,1,1,1\}$. The sample $n = 4$ of the linear result has **wrapped** onto
$n = 0$: $1 + (-4) = -3$ ✓. So the wrapped value is exactly the fifth linear
sample added to the first.

**(d)** The linear result requires a transform length of at least
$n_{x}+n_{h}-1 = 5$. Here 4 is not enough; 5 is the minimum, and practical codes
use a power of two, i.e. 8. **The rule is not "pad to the input length"**; it is
"pad to the length of the *output*".

---

## ★★★9 — Poles just outside the unit circle

**(a)** $r^{5000} = 1.01^{5000} = 4.04\times10^{21}$. The impulse response has
grown by more than twenty-one orders of magnitude; the filter is unusable for any
purpose and will overflow double precision long before the record ends.

**(b)** Require $r^{5000} \le 100$, so

$$r \le 100^{1/5000} = e^{\ln(100)/5000} = e^{0.000921034} = 1.000921458 .$$

The pole may be at most $0.0921\%$ outside the unit circle — a tolerance of one
part in a thousand, which is *below* the accuracy with which a pole is usually
estimated from a finite record. The practical conclusion is the important one:
any pole you cannot locate to better than $0.1\%$ in radius must be assumed to be
at or outside the circle unless you have a physical reason to know otherwise.

**(c)** Two diagnostics, both using only the impulse response:

1. **Growth versus decay over the record.** Fit $\ln|h[n]|$ against $n$ over the
   *last* half of the record. A radius of $0.99$ gives a slope of
   $\ln 0.99 = -0.010050$ per sample; $1.01$ gives $+0.009950$. The sign of the
   slope is decisive and requires no absolute calibration — the two differ by a
   factor of the order of the reciprocal of the record length divided by the
   e-folding time, which is easily resolved.
2. **Energy growth.** Compare the summed energy in successive halves of the
   record: $\sum|h|^{2}$ over $n = 2500..5000$ versus $0..2500$. It grows by a
   factor of about $e^{2\times5000\times0.00995}\approx e^{99}$ for $r=1.01$ and
   decays for $0.99$. This is the same test with better conditioning against
   additive noise, because the noise floor does not grow.

**(d)** At exactly $|p| = 1$ the impulse response neither decays nor grows: it is
a **marginally stable** system, and its response to a bounded input is bounded
only if the input's component at the pole frequency is zero. Any input with energy
at that frequency produces an output that grows linearly (for a simple pole) or
faster (for a repeated pole). Examples: a perfect integrator or accumulator
($H(z) = 1/(1-z^{-1})$, pole at $z = 1$) — a permanent offset in the input
produces an output that ramps forever; and an undamped oscillator with poles on
the unit circle, whose response to a resonance-frequency input grows without
bound. **A geophysical example:** a recursive scheme for a decaying quantity that
is tuned to be exactly non-dissipative (a leapfrog scheme at its stability limit,
or a "perfect integrator" written to conserve a quantity exactly) sits on the unit
circle and will drift linearly in the presence of any bias.

---

## ★★★10 — The bilinear transform and pre-warping

**(a)** With $z = (1+sT/2)/(1-sT/2)$ and $s = i\Omega$,

$$z = e^{i\omega}, \qquad \omega = 2\arctan\left(\frac{\Omega T}{2}\right) .$$

The mapping is monotone, odd, and **compressive**: $\omega \approx \Omega T$ for
$\Omega T \ll 1$, while $\omega \to \pi$ as $\Omega T\to\infty$. The whole
infinite analogue axis is squeezed into $(-\pi,\pi)$ — that is, into the Nyquist
band. It also maps $\operatorname{Re}s<0$ onto $|z|<1$ exactly, which is why it is
the discretisation of choice for filter design.

**(b)** Pre-warping means choosing the analogue frequency whose image is the
wanted digital frequency:

$$\Omega_{c} = \frac{2}{T}\tan\left(\frac{\omega_{c}}{2}\right)
= \frac{2}{0.01}\tan\left(\frac{2\pi\times10\times0.01}{2}\right)
= 200\tan(0.1\pi) = 64.983939\ \mathrm{rad\,s^{-1}} .$$

Substituting back: $\omega = 2\arctan(64.983939\times0.01/2) = 0.628318531$ rad,
and since $\omega = 2\pi f T$ with $T = 0.01$,
$f = 0.628318531/(2\pi\times0.01) = 10.000000$ Hz exactly ✓.

**(c)** Without pre-warping, $\Omega_{c} = 2\pi f_{c} = 62.831853$ and

$$\omega = 2\arctan\left(\frac{62.831853\times0.01}{2}\right) = 0.608791595
\ \mathrm{rad}, \qquad f = \frac{\omega}{2\pi T} = 9.689219\ \mathrm{Hz} .$$

**(d)** The error is $0.310781$ Hz, i.e. $3.1\%$ of $f_{c}$, and it is **always
towards lower frequency** — the warping compresses, so an unwarped design puts the
corner too low. For an anti-alias filter ahead of decimation this matters: the
stopband edge is also misplaced, and a 3% early roll-off attenuates the top of the
passband that you intended to keep. It is small enough that many processing
systems tolerate it, and large enough that a filter specified and verified
numerically should be checked rather than assumed. The error grows as $(f_{c}T)^{2}$,
so at $f_{c}T = 0.3$ it is about $9\%$, which is no longer tolerable.

**(e)** The impulse-invariant method samples the analogue impulse response:
$h[n] = T\,h_{a}(nT)$. It preserves the impulse response exactly at the sample
instants, and therefore preserves the pole positions through $z = e^{sT}$ — but it
**aliases** the frequency response, because the sampled response's spectrum is the
sum of the analogue spectrum repeated at multiples of $f_{s}$. The output is
correct for a band-limited input and wrong for anything above Nyquist,
which is precisely the content of sampling theory
([01-10-05](../../10-fourier-analysis/05-windowing-aliasing.md)). Frequency
warping is *not* the relevant question there: the map $z = e^{sT}$ is
multiplicative along the imaginary axis ($\omega = \Omega T$) with no compression,
so there is no corner displacement to pre-warp — the only issue is that the
analogue response beyond Nyquist folds back into the band. Its virtue is that the
poles map exactly and the transient behaviour matches; its vice is that the
magnitude response of a low-pass filter has aliased high-frequency tails, so a
sharp analogue filter becomes a poor digital one.

---

## Self-assessment: have you actually learned this?

You can, without notes:

- write a transform with its region of convergence and say why the region is part
  of the answer;
- convert a difference equation into $H(z)$, list poles and zeros, and decide
  stability;
- get an impulse response by recursion and explain its decay rate from the pole
  radius;
- explain why a resonator's peak is not at its pole angle, and estimate both the
  peak and the bandwidth;
- compute a circular convolution by hand and say where the wrapped samples went;
- state the padding rule for a linear convolution;
- state the bilinear warping formula and pre-warp a corner frequency;
- explain why a pole at exactly unity is marginal, not stable.
