---
id: 01-11-05
title: "The z-Transform and Discrete Linear Systems"
level: graduate
prereqs: ["01-11-04", "01-10-04"]
estimated_minutes: 90
tags: [z-transform, digital-filters, difference-equations, transfer-function, stability]
---

# The z-Transform and Discrete Linear Systems

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the two-sided and one-sided $z$-transform, state the region of
   convergence as an annulus, and explain what the region decides.
2. **Derive** the transforms of the geometric, step and finite sequences, and
   apply the shift, scaling and convolution properties.
3. **Convert** a difference equation into a transfer function $H(z)$ and back,
   and obtain the impulse response by recursion, by partial fractions and by
   residues.
4. **Read** a pole-zero diagram: radius gives per-sample decay, argument gives
   frequency, and the unit circle decides stability.
5. **Explain** why the peak of a two-pole resonator is *not* at the pole angle,
   and compute where it is.
6. **Distinguish** circular from linear convolution, and pad to
   $n_{x}+n_{h}-1$ rather than to the length of the input.
7. **Relate** the $z$ plane to the $s$ plane through $z = e^{sT}$, and explain
   the frequency warping of the bilinear transform.

## Prerequisites

[01-11-04 The Laplace Transform and Transient
Problems](./04-laplace-transform.md) — poles, transfer functions and stability in
the continuous case, of which this lesson is the sampled version;
[01-10-04 Discrete Fourier Transform and the
FFT](../10-fourier-analysis/04-discrete-fourier.md) — the DFT as a transform on
the unit circle, and the sampling and normalisation conventions.

## 1. Intuition: every record is a sequence

Geophysical data arrive as samples. A seismogram is a list of numbers at a fixed
sampling interval; a tide gauge record is a list of hourly heights; a gravity
profile is a list of values at fixed station spacing. Any operation applied to
such a list — filtering, deconvolution, prediction, differencing, stacking — is
a **linear discrete system**, and the algebra of linear discrete systems is the
algebra of polynomials in a variable $z^{-1}$.

The $z$-transform is the bookkeeping device that makes this algebra work:

$$X(z) = \sum_{n=-\infty}^{\infty}x[n]\,z^{-n}.$$

Three things follow, and they are the whole lesson:

1. **A shift of the sequence is a multiplication by $z^{-1}$.** Delaying a
   signal by one sample multiplies its transform by $z^{-1}$, so a difference
   equation becomes a rational function and filtering becomes multiplication.
2. **The unit circle is the frequency axis.** Setting $z = e^{i\omega}$ turns
   the transform into the discrete-time Fourier transform, and the DFT is the
   same function evaluated at the $N$-th roots of unity
   ([01-10-04](../10-fourier-analysis/04-discrete-fourier.md)).
3. **The region of convergence, and hence stability, is decided by the radius of
   the poles.** A causal filter is stable exactly when every pole lies inside
   the unit circle. This is the discrete image of the left-half-plane criterion
   of [01-11-04](./04-laplace-transform.md) Section 2.2.

The last point is why the $z$-transform is not merely a notational convenience.
A recursive filter with a pole outside the unit circle does not merely distort a
record — its impulse response grows without bound and the output destroys the
data. The pole radius is an operational limit, and it is read off the complex
plane.

## 2. Definition, convergence and the shape of the $z$ plane

### 2.1 The transform and its region

For a two-sided sequence $x[n]$, $n \in \mathbb{Z}$, define

$$X(z) = \sum_{n=-\infty}^{\infty}x[n]z^{-n},$$

convergent in an **annulus** $r_{-} < |z| < r_{+}$ whose inner radius is set by
the causal part and whose outer radius by the anti-causal part. The **one-sided**
transform used for initial-value problems sums from $n=0$ only. As with the
Laplace transform, the algebraic expression does not determine the sequence: the
region of convergence is part of the answer. For $x[n] = a^{n}u[n]$ (causal),

$$X(z) = \sum_{n=0}^{\infty}\left(\frac{a}{z}\right)^{n}
= \frac{1}{1-a z^{-1}} = \frac{z}{z-a}, \qquad |z| > |a|,$$

and the same algebraic form with $|z| < |a|$ belongs to the anti-causal sequence
$-a^{n}u[-n-1]$.

The demo sums the causal series term by term and compares with the closed form
at $a = 0.85$:

| $z$ | $|z|$ | partial sum to $n=199$ | closed form | error |
|---|---|---|---|---|
| $2.000$ | 2.0000 | $1.739130434783$ | $1.739130434783$ | $2.2\times10^{-16}$ |
| $1.300+0.700i$ | 1.4765 | $1.552346570397-0.859205776173i$ | same | $6.3\times10^{-16}$ |
| $-1.500+1.500i$ | 2.1213 | $0.743004181409-0.164039884207i$ | same | $1.4\times10^{-16}$ |
| $1.200-0.900i$ | 1.5000 | $1.319034852547+0.820375335121i$ | same | $4.0\times10^{-16}$ |

Truncating at $n=199$ leaves a residual of order $|a/z|^{200} \approx 10^{-48}$,
so the agreement is round-off. **Inside** the radius of convergence the same sum
diverges: at $z = 0.5$ the ratio is $a/0.5 = 1.7$, and the partial sum to $n=59$
is already $9.5904\times10^{13}$. The closed form is not a representation of the
series there, and no amount of numerical care fixes that — the series genuinely
diverges.

### 2.2 The unit circle is the DFT

The demo checks the identity directly. For the filter
$H(z) = (0.5+0.5z^{-1})/(1-0.9z^{-1})$ it forms the impulse response on a finite
record, takes its DFT, and compares with $H(e^{i\omega})$ at the DFT bins:

| $k$ | $\omega$ (rad) | DFT of $h$ | $H(e^{i\omega})$ |
|---|---|---|---|
| 0 | 0.000000 | $9.987554805$ | $10.000000000$ |
| 4 | 0.392699 | $0.652879382-2.469925390i$ | $0.654305831-2.472840915i$ |
| 8 | 0.785398 | $0.158044667-1.248975615i$ | $0.158887008-1.250449919i$ |
| 16 | 1.570796 | $0.026936730-0.524243057i$ | $0.027624309-0.524861878i$ |
| 24 | 2.356194 | $0.004089842-0.217646662i$ | $0.004750453-0.217903575i$ |
| 32 | 3.141593 | $-0.000655010$ | $-0.000000000$ |

The two columns agree only approximately, and the reason is instructive. With
$N = 64$ samples the worst difference over the bins is $1.245\times10^{-2}$,
because the impulse response has not died away by $n = 63$ (its last value is
$1.383\times10^{-3}$). With $N = 1024$ the worst difference falls to
$1.389\times10^{-13}$ and the last value of the response is
$1.635\times10^{-47}$. **The DFT is not a different transform.** It is the
$z$-transform sampled at the $N$-th roots of unity, and the discrepancy is
truncation of the sequence — never a defect of the identity.

## 3. Properties and the transform table

| property | sequence | transform | region |
|---|---|---|---|
| linearity | $\alpha x + \beta y$ | $\alpha X + \beta Y$ | intersection |
| delay | $x[n-k]$ | $z^{-k}X(z)$ | shifted |
| advance | $x[n+k]$ | $z^{k}\bigl(X(z)-\sum_{j=0}^{k-1}x[j]z^{-j}\bigr)$ | shifted |
| scaling | $a^{n}x[n]$ | $X(z/a)$ | $\vert a\vert r_{-}<\vert z\vert<\vert a\vert r_{+}$ |
| convolution | $x * y$ | $X(z)Y(z)$ | intersection |
| accumulation | $\sum_{k\le n}x[k]$ | $X(z)/(1-z^{-1})$ | plus $\vert z\vert>1$ |
| difference | $x[n]-x[n-1]$ | $(1-z^{-1})X(z)$ | plus $\vert z\vert>1$ |

and the elementary pairs:

| $x[n]$ | $X(z)$ | region |
|---|---|---|
| $\delta[n]$ | $1$ | all $z$ |
| $u[n]$ | $1/(1-z^{-1})$ | $\vert z\vert>1$ |
| $a^{n}u[n]$ | $1/(1-az^{-1})$ | $\vert z\vert>\vert a\vert$ |
| $n a^{n}u[n]$ | $az^{-1}/(1-az^{-1})^{2}$ | $\vert z\vert>\vert a\vert$ |
| $\cos(\omega_{0}n)u[n]$ | $(1-z^{-1}\cos\omega_{0})/(1-2z^{-1}\cos\omega_{0}+z^{-2})$ | $\vert z\vert>1$ |
| $r^{n}\cos(\omega_{0}n)u[n]$ | $(1-rz^{-1}\cos\omega_{0})/(1-2rz^{-1}\cos\omega_{0}+r^{2}z^{-2})$ | $\vert z\vert>r$ |

The difference and accumulation entries are the discrete counterparts of
"differentiation becomes multiplication" and "integration becomes division" from
the Laplace lesson: they are why a difference equation turns into a rational
function of $z^{-1}$.

## 4. Difference equations, transfer functions and impulse responses

### 4.1 The conversion

A general linear difference equation with constant coefficients,

$$\sum_{k=0}^{N}a_{k}\,y[n-k] = \sum_{k=0}^{M}b_{k}\,x[n-k],$$

transforms, using the delay property and assuming zero initial conditions, into

$$H(z) = \frac{Y(z)}{X(z)}
= \frac{b_{0}+b_{1}z^{-1}+\cdots+b_{M}z^{-M}}{a_{0}+a_{1}z^{-1}+\cdots+a_{N}z^{-N}}
= \frac{z^{N-M}\,\prod_{k}(z-z_{k})}{\prod_{j}(z-p_{j})}.$$

The **zeros** $z_{k}$ and **poles** $p_{j}$ determine everything about the
system. The impulse response is the inverse transform of $H$, obtained by partial
fractions — equivalently by summing residues of $H(z)z^{n-1}$ at the poles.

### 4.2 A worked example, verified inside

Take

$$y[n] = 0.5\,x[n] + 0.5\,x[n-1] + 0.9\,y[n-1],$$

so that $H(z) = (0.5+0.5z^{-1})/(1-0.9z^{-1})$. The single pole is at
$z = 0.9$ and the single zero at $z = -1$; there is also a zero at the origin
from the numerator's $z^{-1}$. Partial fractions give

$$h[n] = 0.5\,\delta[n] + 0.95\,\cdot 0.9^{\,n-1}\,u[n-1],$$

that is, $h[0] = 0.5$ and $h[n] = 0.95\cdot0.9^{n-1}$ for $n\ge1$. The demo runs
the recursion and compares:

| $n$ | $h[n]$ from recursion | closed form | error |
|---|---|---|---|
| 0 | 0.500000000000 | 0.500000000000 | 0 |
| 1 | 0.950000000000 | 0.950000000000 | 0 |
| 2 | 0.855000000000 | 0.855000000000 | 0 |
| 5 | 0.623295000000 | 0.623295000000 | $1.1\times10^{-16}$ |
| 10 | 0.368049464550 | 0.368049464550 | $5.6\times10^{-17}$ |
| 30 | 0.044746222624 | 0.044746222624 | $1.4\times10^{-17}$ |
| 63 | 0.001382799426 | 0.001382799426 | $4.3\times10^{-19}$ |

The recursion and the transform are the same object; the transform just says so
in one line. Note the reading of $H$ before any inverse: one pole at radius
$0.9$ means a geometric decay with ratio $0.9$ per sample, and one zero at
$z = -1$ means exact rejection at the Nyquist frequency — the filter is a
low-pass, and both facts are visible in the pole-zero plot without computing a
single output value.

## 5. Poles: radius, angle, stability

### 5.1 Radius is decay, angle is frequency

A pole at $p = re^{i\omega_{0}}$ contributes a term proportional to
$r^{n}e^{i\omega_{0}n}$ to the impulse response. So:

- the **radius** $r$ is the per-sample decay factor;
- the **angle** $\omega_{0}$ is the oscillation frequency, in radians per sample,
  corresponding to $f = \omega_{0}/(2\pi)$ cycles per sample;
- stability requires $r<1$ for every pole, if the system is causal.

The demo measures the logarithmic slope of $|h[n]|$ against $\ln r$:

| pole | radius | measured $\mathrm{d}\ln|h|/\mathrm{d}n$ | $\ln r$ | verdict |
|---|---|---|---|---|
| $0.5$ | 0.5000 | $-0.693147$ | $-0.693147$ | stable |
| $0.9$ | 0.9000 | $-0.105361$ | $-0.105361$ | stable |
| $-0.9$ | 0.9000 | $-0.105361$ | $-0.105361$ | stable |
| $1.0$ | 1.0000 | — (no decay) | $0.000000$ | marginal |
| $1.02$ | 1.0200 | $+0.019803$ | $+0.019803$ | unstable |

Two rows deserve comment. The pole at $-0.9$ oscillates in sign at the Nyquist
frequency but decays at the same rate as $+0.9$: the *sign* of a pole carries
frequency information, the radius carries decay. The pole at $1.02$ has a
measured growth rate of $+0.019803$ per sample, which is $2\%$ per sample — over
a $10^{5}$-sample record that is $e^{1980}$, i.e. an overflow. Recursive filters
on field data are not a place for a pole outside the circle "by a little".

### 5.2 The resonator, and the peak that is not at the pole

A two-pole resonator is the workhorse of discrete spectral analysis:

$$H(z) = \frac{1}{1-2r\cos\omega_{0}\,z^{-1}+r^{2}z^{-2}},
\qquad\text{poles at } re^{\pm i\omega_{0}}.$$

It is tempting to say that the resonance is at $\omega_{0}$. It is not, and the
demo measures the difference with a brute-force scan of $|H(e^{i\omega})|$ over
two million points. With $r = 0.95$, $\omega_{0} = 2\pi\cdot10/100 = 0.628318531$
rad:

| quantity | value |
|---|---|
| pole angle $\omega_{0}$ | 0.628318531 rad (10.000000 Hz) |
| measured peak of $\lvert H\rvert$ | 0.626504261 rad (9.971125 Hz) |
| $\arccos\!\bigl((1+r^{2})\cos\omega_{0}/(2r)\bigr)$ | 0.626505238 rad (9.971141 Hz) |
| $\lvert H\rvert$ at the pole angle | 17.438391 |
| $\lvert H\rvert$ at the true peak | 17.449247 |
| $-3$ dB points | 0.573066 and 0.676267 rad |
| bandwidth | 1.642500 Hz (0.103201 rad) |
| measured $Q = f_{0}/\text{bandwidth}$ | 6.0883 |

and $Q \approx \omega_{0}/[2(1-r)] = 6.2832$. The peak is pulled **towards DC**
by $0.2886\%$ of $\omega_{0}$, the measured peak agrees with the closed form to
$9.8\times10^{-7}$ rad (which is the scan resolution, not a discrepancy), and the
simple approximation $1/[(1-r)2\sin\omega_{0}] = 17.0130$ for the peak height is
low by $2.5\%$ at this pole radius.

The practical consequence: quoting the pole angle as the resonance frequency
introduces an error proportional to $(1-r)$, so the sharper the resonator — the
more useful it is — the worse the error. For $r = 0.95$ it is $0.29\%$; for
$r = 0.999$ it is roughly $0.06\%$ in the angle but a far larger error in the
inferred frequency if the pole is extracted from a spectrum, because the peak
height $1/[(1-r)2\sin\omega_{0}]$ is then about $500$ and the peak is very
narrow.

## 6. Discrete convolution: circular, linear, and the padding rule

The convolution property says that $y = x * h$ has transform $X(z)H(z)$. For
finite sequences and a DFT, the product of transforms produces **circular**
convolution, which wraps the tail of the response onto the start of the record.
The demo demonstrates the wrap explicitly with a 12-sample wavelet and an
8-coefficient FIR filter:

| $n$ | linear convolution | circular, length 12 | circular, length 32 | wrap error |
|---|---|---|---|---|
| 0 | $-0.000317173$ | $-0.000260916$ | $-0.000317173$ | $5.6\times10^{-5}$ |
| 1 | $-0.010630586$ | $-0.014564964$ | $-0.010630586$ | $3.9\times10^{-3}$ |
| 2 | $-0.122894179$ | $-0.121205280$ | $-0.122894179$ | $1.7\times10^{-3}$ |
| 3 | $-0.370475827$ | $-0.369633078$ | $-0.370475827$ | $8.4\times10^{-4}$ |
| 15 | $0.000842749$ | $-0.369633078$ | $0.000842749$ | $3.7\times10^{-1}$ |

The transform length must be at least $n_{x}+n_{h}-1 = 19$ samples; the demo uses
32 and obtains a worst error of $5.9\times10^{-16}$. The 12-sample version is
wrong by $0.37$ at sample 15, where the true answer is essentially zero: the
wrapped tail of the filter response has been added to nothing.

The same trap appears for an infinite impulse response, in a milder form. With
$n = 256$ and a transform length of 512, the recursion and the transform product
agree to $9.8\times10^{-14}$, and the residual is set by the truncated tail
$|h[255]| = 2.3\times10^{-12}$ multiplied by the sum of the input. There is no
padding length that makes an IIR exact; there is only a length at which the tail
is below the noise.

## 7. From the $s$ plane to the $z$ plane

### 7.1 Sampling maps the planes

A continuous signal sampled every $T$ seconds has $z = e^{sT}$, so:

- the **left half** of the $s$ plane maps onto the **inside** of the unit circle,
  which is why stability looks different in the two planes and means the same
  thing;
- the **imaginary axis** maps onto the **unit circle**, with
  $\omega = \Omega T$ where $\Omega$ is the analogue angular frequency;
- the strip $|\operatorname{Im}s| < \pi/T$ maps onto the circle **without
  overlap**; frequencies outside the strip land on top of frequencies inside it,
  which is aliasing seen from the $z$ plane
  ([01-10-05](../10-fourier-analysis/05-windowing-aliasing.md)).

The demo evaluates $z = e^{sT}$ at $T = 0.01$ s:

| $s$ | $z = e^{sT}$ | $\vert z\vert$ |
|---|---|---|
| $-5$ | $0.951229424501$ | 0.951229425 |
| $-2+30i$ | $0.936419559202+0.289668514505i$ | 0.980198673 |
| $-1+100i$ | $0.534926208099+0.833098208614i$ | 0.990049834 |
| $1+2i$ | $1.009848163784+0.020199656635i$ | 1.010050167 |

The third row is the point: $\Omega = 100\ \mathrm{rad\,s^{-1}}$ with
$T = 0.01$ s gives $\Omega T = 1$, and $|z| = e^{-0.01} = 0.990049834$ — a decay
of only $1\%$ per sample, so the sampled system is barely damped even though the
analogue decay is substantial. Discretisation changes apparent damping rates, and
the mapping above is how to see it.

### 7.2 The bilinear transform, and why frequency warping is not optional

The bilinear transform

$$z = \frac{1+sT/2}{1-sT/2}$$

maps the entire left half plane into the unit disc, with no aliasing — the price
is that frequencies are warped. With $s = i\Omega$,

$$z = e^{i\omega}, \qquad \omega = 2\arctan\!\left(\frac{\Omega T}{2}\right),$$

so the infinite analogue frequency axis is compressed into $(-\pi,\pi)$. The demo
verifies the identity to machine precision:

| $\Omega T$ | $\vert z\vert$ | $\arg z$ | $2\arctan(\Omega T/2)$ |
|---|---|---|---|
| 0.5 | 1.0000000000 | 0.4899573263 | 0.4899573263 |
| 1.0 | 1.0000000000 | 0.9272952180 | 0.9272952180 |
| 2.0 | 1.0000000000 | 1.5707963268 | 1.5707963268 |
| 4.0 | 1.0000000000 | 2.2142974356 | 2.2142974356 |
| 8.0 | 1.0000000000 | 2.6516353273 | 2.6516353273 |

The practical rule is to **pre-warp**: if a filter is to have its corner at
$f_{c}$, choose the analogue $\Omega = (2/T)\tan(\pi f_{c}T)$ rather than
$2\pi f_{c}$. Omit the warp and at $f_{c}T = 0.25$ the corner lands at
$\arctan$ of the wrong argument — an error of some per cent, silent, and in the
wrong direction for a filter whose purpose is to control noise.

## Assumptions and regime of validity

| assumption | statement | where it fails or must be checked |
|---|---|---|
| **Linearity and time invariance** | superposition and the convolution theorem | adaptive filters, saturation, time-varying media |
| **Zero initial conditions** | the delay property gives $z^{-k}X(z)$, so a difference equation becomes a rational $H(z)$ | a recursion started mid-record: the initial state appears as extra terms |
| **A stated region of convergence** | $1/(1-az^{-1})$ is one formula for two sequences | quoting the formula without the annulus |
| **Causality for the stability criterion** | causal $\Rightarrow$ stable iff every pole satisfies $\vert p\vert<1$ | an anti-causal system is stable when every pole lies outside the unit circle |
| **Sampling and anti-aliasing** | $z = e^{sT}$ maps only the strip $\vert\operatorname{Im}s\vert<\pi/T$ without overlap | content above Nyquist folds; no filter recovers it |
| **Transform length $\geq n_{x}+n_{h}-1$** | for a linear convolution by transform product | shorter lengths give circular convolution, and the wrap can exceed the signal |
| **Impulse response negligible at the record end** | for an IIR, the transform product is exact only in the limit | a pole near the unit circle: no finite length suffices |

**Regime of validity of the pole reading.** "Radius is decay, angle is
frequency" is exact for a *single* pole. With several poles the response is a sum
of terms, and the apparent decay rate is the slowest one while the apparent
frequency is the strongest one — read the poles, not the envelope, unless you
have established which dominates. The peak formula
$\cos\omega_{\text{peak}} = [(1+r^{2})/(2r)]\cos\omega_{0}$ has its own
restriction: since $(1+r^{2})/(2r) \ge 1$, a solution exists only when
$\cos\omega_{0} \le 2r/(1+r^{2})$, i.e. when the pole angle exceeds
$\arccos[2r/(1+r^{2})]$. For $r = 0.95$ that threshold is $0.051271$ rad
($0.020201$ rad for $r = 0.98$, and $0.105166$ rad for $r = 0.9$), and for a
smaller pole angle the response is largest at DC and there is **no interior peak
at all**. The correction to the peak position is therefore invisible in
low-frequency, wide-band designs and glaring in narrow-band ones — but so is the
existence of the peak, so the formula must be used with its inequality checked.

**Discretisation is not a detail.** The bilinear transform preserves the
left-half-plane mapping exactly and warps frequency; the impulse-invariant method
preserves the pole map exactly and aliases the response. Neither is "the"
discretisation, and a filter specified in the analogue domain must state which
one produced the coefficients. The error from choosing the wrong one is silent:
the filter is stable, has plausible coefficients, and puts its corner in the wrong
place.

## 8. Python demonstration

[`code/ztransform_demo.py`](./code/ztransform_demo.py) prints all the tables
above in under a second:

```text
python3 code/ztransform_demo.py
```

Only the standard library is used (`cmath`, `math`), with a direct transform for
arbitrary lengths and a radix-2 FFT for the power-of-two cases. Points of method:

- **The transform is verified against a truncated sum, not against itself.** The
  $1024$-point check uses an impulse response whose tail is $10^{-47}$, so the
  residual $1.389\times10^{-13}$ is a statement about the identity; the
  $64$-point check is deliberately left in to show what truncation looks like
  when it is not negligible.
- **The resonator peak is found by brute force, not by a formula.** Two million
  scan points establish the peak location independently of the closed form it is
  compared with, and the residual is reported as the scan resolution.
- **Stability is measured, not asserted.** The logarithmic slope of the impulse
  response is computed and compared with $\ln r$ for five radii, including one
  outside the unit circle.
- **The padding rule is demonstrated at both lengths.** The same data are
  convolved at length 12 and length 32 so the wrap error can be read off rather
  than described.

## 9. Common mistakes

1. **Quoting $X(z)$ without the region of convergence.** $1/(1-az^{-1})$
   represents a causal sequence for $|z|>|a|$ and an anti-causal one for
   $|z|<|a|$.
2. **Padding to the length of the input.** Zero-pad to $n_{x}+n_{h}-1$ for a
   linear convolution; padding to $n_{x}$ produces circular convolution with a
   wrap error that can exceed the signal (Section 6).
3. **Assuming the pole angle is the resonance.** Section 5.2: the peak is pulled
   towards DC by an amount proportional to $(1-r)$.
4. **Designing a filter by its poles and forgetting the zeros.** A zero at
   $z = -1$ puts a null at Nyquist; a zero just outside the unit circle inverts a
   phase without changing amplitude, which is either the goal or an accident.
5. **Confusing the DFT bin spacing with resolution.** The $z$-transform on the
   unit circle gives values at any $\omega$; the DFT gives them at $N$ points,
   and the resolution is set by the record length, not by $N$
   ([01-10-04](../10-fourier-analysis/04-discrete-fourier.md)).
6. **Using the bilinear transform without pre-warping.** Section 7.2.
7. **Expecting a recursive filter to be invertible.** A pole inside the unit
   circle in $H(z)$ becomes a pole outside the unit circle in $1/H(z)$; direct
   deconvolution with a recursive filter that has small poles is an unstable
   inverse problem, which is the discrete face of the deconvolution problem in
   [01-10-03](../10-fourier-analysis/03-convolution.md).

## 10. Real-world applications

- **Digital filtering of seismic and potential-field data.** Every recursive and
  every FIR filter in a processing flow is a rational $H(z)$; its pole-zero plot
  is the design document
  ([20-signal-processing](../../20-signal-processing/README.md)).
- **Autoregressive models and spectral estimation.** An AR$(p)$ model is
  $H(z) = 1/A(z)$ with $A$ a polynomial whose roots are the poles; the
  estimated poles give the resonance frequencies, with exactly the bias of
  Section 5.2 ([01-10-08 Spatial
  Spectra](../10-fourier-analysis/08-spatial-spectra.md)).
- **Deconvolution and predictive filtering.** Wiener and spiking filters are
  designed by solving a Toeplitz system whose normal equations come from the
  discretised convolution property
  ([18-inverse-problems](../../18-inverse-problems/README.md)).
- **Tide and climate records.** Recurrence relations for ocean tides and for
  harmonic analysis of a sampled record are difference equations; their
  numerical stability is a $z$-plane question
  ([01-10-01 Fourier series](../10-fourier-analysis/01-fourier-series.md)).
- **Instrument response removal.** A recorded trace is a discrete convolution of
  ground motion with instrument response; removing the response is dividing by
  $H(z)$ on the unit circle, with the noise amplification analysed in
  [01-10-03](../10-fourier-analysis/03-convolution.md).
- **Numerical stability of explicit schemes.** The von Neumann condition for a
  finite-difference scheme is exactly the requirement that a certain $z$
  polynomial has no roots outside the unit circle
  ([19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)).

## 11. Further reading

- **Oppenheim, A. V. & Schafer, R. W. (2010). *Discrete-Time Signal
  Processing* (3rd ed.). Prentice Hall.** Chapters 3, 5 and 6. Level:
  intermediate. The $z$-transform, its region of convergence and filter design,
  with the pole-zero reading done properly.
- **Proakis, J. G. & Manolakis, D. G. (2007). *Digital Signal Processing:
  Principles, Algorithms and Applications* (4th ed.). Pearson.** Chapters 3–5.
  Level: intermediate. The same material with more design tables.
- **Kanasewich, E. R. (1981). *Time Sequence Analysis in Geophysics* (3rd ed.).
  University of Alberta Press.** Level: intermediate. Written for geophysics,
  with the recursive filters and deconvolution operators actually used in
  processing.
- **Claerbout, J. F. (1976). *Fundamentals of Geophysical Data Processing*.
  McGraw-Hill.** Level: advanced. Filter design and recursive operators treated
  as linear algebra; the source of much of the field's practical intuition.
- **Robinson, E. A. & Treitel, S. (1980). *Geophysical Signal Analysis*.
  Prentice Hall.** Level: advanced. Where the predictive deconvolution filters of
  seismic processing are derived in the $z$ domain.
- **Trefethen, L. N. & Bau, D. (1997). *Numerical Linear Algebra*, SIAM.**
  Lecture 29. Level: graduate. Stability of difference equations and why poles
  near the unit circle make numerical work delicate.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm editions
> and availability through your library before citing them.

## 12. Related lessons

- [04 The Laplace Transform and Transient
  Problems](./04-laplace-transform.md) — the continuous version of everything
  here, and the origin of the $z = e^{sT}$ mapping.
- [06 Dispersion Relations and Causality in Wave
  Physics](./06-dispersion-relations.md) — where the analytic structure of a
  transfer function becomes a physical constraint.
- [01-10-04 Discrete Fourier Transform and the
  FFT](../10-fourier-analysis/04-discrete-fourier.md) — the unit circle, and the
  $N$ and $\Delta t$ factors that this lesson's normalisation omits.
- [01-10-05 Sampling, Aliasing, Leakage and
  Windowing](../10-fourier-analysis/05-windowing-aliasing.md) — the overlap of
  the $z$ plane's frequency strip, and what it costs.
- [01-10-03 Convolution, Filtering and the Convolution
  Theorem](../10-fourier-analysis/03-convolution.md) — the filtering theory this
  lesson discretises.
- [20 Signal Processing](../../20-signal-processing/README.md) — where these
  filters are sequenced into a processing flow on real records.

## 13. Exercises

Ten graded exercises, with full worked solutions, are in
[`exercises/05-z-transform-exercises.md`](./exercises/05-z-transform-exercises.md).
Solutions:
[`exercises/05-z-transform-solutions.md`](./exercises/05-z-transform-solutions.md).

## Self-assessment checklist

- [ ] I can define the $z$-transform, state its region of convergence for a
      geometric sequence, and say what the region decides.
- [ ] I can convert a difference equation into $H(z)$, find its poles and zeros,
      and write the impulse response by partial fractions.
- [ ] I can read decay rate and frequency off a pole, and state the stability
      criterion for a causal system.
- [ ] I can explain why the peak of a two-pole resonator is not at the pole
      angle, and compute where it is.
- [ ] I can distinguish circular from linear convolution and state the padding
      rule.
- [ ] I can relate the $s$ plane to the $z$ plane and explain the frequency
      warping of the bilinear transform.
- [ ] I can verify a transform identity against a truncated sum whose tail is
      negligible, and say why the residual is then evidence.
