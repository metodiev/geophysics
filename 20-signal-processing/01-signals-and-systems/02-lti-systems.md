---
id: 20-01-02
title: "Linear Time-Invariant Systems and Impulse Response"
level: advanced
prereqs: ["20-01-01", "01-10-03", "03-03-05"]
tags: [signal-processing, lti, impulse-response, convolution, stability, systems]
---

# Linear Time-Invariant Systems and Impulse Response

Most of what a geophysical instrument does to a signal is a **linear
time-invariant operation**, and the reason this matters is not mathematical
elegance but measurement economy: an LTI system is completely described by one
response, so a calibration done once applies forever. This lesson derives that
statement, states exactly which two assumptions it rests on, and then measures
each of them so the failure modes of a nonlinear or time-varying system are
visible rather than hypothetical.

**All models and data in this module are SYNTHETIC.** The systems used below are
one- and two-parameter teaching models with known closed forms, chosen so that
every measured number has an exact value to compare against.

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the two axioms (superposition and time-invariance) precisely, and
   **test** them numerically on a given system.
2. **Derive** the convolution sum $y[n] = \sum_k h[k]x[n-k]$ from the axioms by
   decomposing the input into shifted impulses.
3. **Identify** a system's impulse response from data and **reconstruct** the
   output by superposition, reporting the residual error.
4. **Classify** systems as causal or acausal, FIR or IIR, and **prove** the
   BIBO stability criterion $\sum_n \lvert h[n]\rvert < \infty$ for causal
   systems.
5. **Compute** the step response and the DC gain $\sum_n h[n]$, and explain the
   relation $h[n] = s[n]-s[n-1]$.
6. **Derive** the eigenfunction property
   $e^{i\omega n} \mapsto H(e^{i\omega})e^{i\omega n}$ and verify it against
   `scipy.signal.freqz`.
7. **Quantify** the delay a causal symmetric FIR imposes, from both the group
   delay and the centroid of an impulse response.

## Prerequisites

- [20-01-01 Signal Classification](01-signal-classification.md) — what the input
  and output objects are.
- [01-10-03 Convolution, Filtering and the Convolution Theorem](../../01-mathematics/10-fourier-analysis/03-convolution.md) —
  convolution in the transform domain.
- [03-03-05 scipy.signal: Filters, Windows and Spectral Estimation](../../03-scientific-computing/03-scipy/05-signal.md) —
  the library calls used in the demonstration.

## 1. Intuition: why one response describes a whole system

A seismometer, a geophone coil, a decimation stage, a stacking loop — each is a
**system**: a rule that maps an input sequence to an output sequence. If the rule
is linear, then responses to separate inputs add. If it is also time-invariant,
then delaying the input merely delays the output. Put the two together and you
can predict the response to *any* input from the response to *one* input,
because every input is a weighted sum of shifted unit impulses.

That is the whole content of the theorem. Its practical meaning for geophysics
is that an instrument response measured once with a pulse test characterises
every future recording; its practical danger is that instruments are only
approximately linear and only approximately time-invariant, and the
approximation fails exactly when the signal is largest.

## 2. Precise definitions

### 2.1 System, linearity, time-invariance

A **system** $\mathcal H$ maps an input sequence $x[n]$ to an output sequence
$y[n] = \mathcal H\{x\}[n]$. It is **linear** if for all inputs $x_1, x_2$ and
all scalars $a, b$,

$$\mathcal H\{a\,x_1 + b\,x_2\} = a\,\mathcal H\{x_1\} + b\,\mathcal H\{x_2\},
\tag{L}$$

and **time-invariant** if for every integer shift $m$

$$\mathcal H\{x[\cdot - m]\}[n] = y[n-m], \qquad y = \mathcal H\{x\}.
\tag{TI}$$

A system satisfying both is **LTI**. Note that (L) already forces
$\mathcal H\{0\} = 0$: a system with an offset (a DC bias, a dark current) is not
linear, it is *affine*, and must be linearised by removing the offset first.

### 2.2 The unit impulse and the impulse response

The **unit impulse** is $\delta[n] = 1$ at $n = 0$ and $0$ elsewhere. The
**impulse response** of a system is

$$h[n] = \mathcal H\{\delta\}[n].$$

For an LTI system, $h$ is the complete description: no other measurement is
needed. This is a strong claim, and Section 3 proves it.

### 2.3 Causality, memory, FIR and IIR

- **Causal**: $h[n] = 0$ for $n<0$ — the output cannot precede the input. Every
  real-time system is causal; recorded data can be filtered acausally (that is
  what zero-phase filtering does, see
  [20-01-04](04-transfer-functions.md)).
- **Memoryless**: $h[n] = c\,\delta[n]$ — the output depends only on the present
  input.
- **FIR** (finite impulse response): $h$ has finite support, so the system is
  always stable. **IIR**: $h$ has infinite support and must be checked.

## 3. Derivation: the convolution sum

Every sequence can be written as a sum of shifted impulses,
$x[n] = \sum_k x[k]\,\delta[n-k]$. Apply the system:

1. the input is the sum $\sum_k x[k]\,\delta[\cdot - k]$ with scalar weights
   $x[k]$;
2. by linearity (L), the output is $\sum_k x[k]\,\mathcal H\{\delta[\cdot-k]\}$;
3. by time-invariance (TI), $\mathcal H\{\delta[\cdot-k]\}[n] = h[n-k]$;
4. therefore

$$\boxed{\;y[n] = \sum_{k=-\infty}^{\infty} x[k]\,h[n-k]
= \sum_{k=-\infty}^{\infty} h[k]\,x[n-k] = (h * x)[n].\;}$$

The two sums are equal by the substitution $k \to n-k$, which is the
**commutativity** of convolution. Two consequences used constantly:

- **Associativity**: $(h_1 * h_2) * x = h_1 * (h_2 * x)$ — cascaded LTI systems
  combine by convolving their impulse responses.
- **Distributivity**: $(h_1 + h_2) * x = h_1*x + h_2*x$ — parallel paths add.

*Numerical check of (L) and (TI).* For the system
$h = [1,\ 0.5,\ 0.25]$ driven by two random inputs with $a = 2.5$,
$b = -1.25$, the demonstration measures

$$\max_n\bigl\lvert \mathcal H\{ax_1+bx_2\}[n] - a\mathcal H\{x_1\}[n]
- b\mathcal H\{x_2\}[n]\bigr\rvert = 1.78\times10^{-15},$$

and a time-invariance residual of exactly $0.000\times10^{0}$ for a
$7$-sample shift. Measured in double precision, $10^{-15}$ *is* zero: the
residual is the rounding of the additions, not a violation.

## 4. Causality and stability

**BIBO stability** (bounded input, bounded output) means
$\lvert x[n]\rvert \le M < \infty \Rightarrow \lvert y[n]\rvert < \infty$. For a
causal LTI system,

$$
\lvert y[n]\rvert = \Bigl\lvert\sum_{k=0}^{\infty} h[k]\,x[n-k]\Bigr\rvert
\le M\sum_{k=0}^{\infty}\lvert h[k]\rvert,
$$

so $\sum_k \lvert h[k]\rvert < \infty$ is *sufficient*. It is also *necessary*:
choose $x[n-k] = \operatorname{sign}(h[k])$, which is bounded by $1$, and the
output at $n$ equals $\sum_k\lvert h[k]\rvert$. Hence

$$\text{causal LTI is BIBO-stable} \iff
\sum_{n=0}^{\infty}\lvert h[n]\rvert < \infty .$$

*Numerical check.* The one-pole recursion $y[n] = a\,y[n-1] + x[n]$ has
$h[n] = a^{n}u[n]$, so $\sum\lvert h\rvert = 1/(1-a)$ for $\lvert a\rvert < 1$.
The demonstration measures $10.000000$ for $a = 0.9$ (exact $1/(1-0.9) = 10$)
and, for $a = 1.1$, a partial sum of $3034.82$ over just 60 samples — the sum
diverges, and the truncation is the only reason a finite number appears at all.
The impulse response is confirmed to be $a^{n}u[n]$ to a maximum error of
$1.11\times10^{-16}$.

## 5. Step response and DC gain

The **unit step** is $u[n] = 1$ for $n\ge0$. Because
$u[n] = \sum_{m\le n}\delta[m]$, linearity gives

$$s[n] = \sum_{m=0}^{n} h[m], \qquad h[n] = s[n] - s[n-1],$$

and, when the system is stable, $\lim_{n\to\infty}s[n] = \sum_{n}h[n] = H(e^{i0})$,
the **DC gain**. The step response is the measurement geophysicists actually
make (a calibration pulse, a step in a tiltmeter), and its limit is the number
that converts counts to physical units.

*Numerical check.* For $a = 0.9$ the demonstration prints
$s[10] = 6.861894$ and $s[63] = 9.988210$, against the closed form

$$s[n] = \frac{1-a^{n+1}}{1-a}: \quad
\frac{1-0.9^{11}}{0.1} = 6.861894, \quad
\frac{1-0.9^{64}}{0.1} = 9.988210 .$$

For the 5-point moving average the step response reaches $s[3] = 0.800000 = 4/5$
and $s[20] = 1.000000$, matching its DC gain $\sum h = 1$.

## 6. Derivation: complex exponentials are eigenfunctions

Let $x[n] = e^{i\omega n}$ with $\omega$ in radians per sample. Then

$$
y[n] = \sum_{k} h[k]\,e^{i\omega(n-k)}
= e^{i\omega n}\underbrace{\sum_{k} h[k]\,e^{-i\omega k}}
_{\displaystyle H(e^{i\omega})},
$$

so the output is the same exponential multiplied by the complex number
$H(e^{i\omega})$. That is the **eigenfunction property**, and the function
$H(e^{i\omega})$ — the discrete-time Fourier transform of $h$ — is the system's
**frequency response**. Its magnitude is the gain, its argument the phase shift;
both are functions of frequency, and neither is a property of the input.

*Numerical check.* For the moving average at $\omega = 0.7\ \mathrm{rad/sample}$
the demonstration obtains $H = +0.0975481770 - 0.5655729868i$ three ways: from
$y[40]/x[40]$, by summing $h[k]e^{-i\omega k}$, and from `scipy.signal.freqz`,
which agree to all printed digits; the maximum deviation of
$y[n] - H(e^{i\omega})x[n]$ over the whole record is $2.18\times10^{-15}$. The
analytic Dirichlet form for a length-5 average,

$$H(e^{i\omega}) = \frac1M e^{-i\omega(M-1)/2}
\frac{\sin(M\omega/2)}{\sin(\omega/2)},$$

gives $\frac15 \cdot \frac{\sin(1.75)}{\sin(0.35)} = 0.574$ in magnitude, which is
$\lvert H\rvert$ above.

## 7. Delay: group delay and the centroid

For a causal symmetric FIR of odd length $M$, the phase is exactly linear,
$\arg H(e^{i\omega}) = -\omega(M-1)/2$, so every frequency is delayed by the same
$ (M-1)/2$ samples. The **group delay**

$$\tau_g(\omega) = -\frac{\mathrm d\,\arg H(e^{i\omega})}{\mathrm d\omega}$$

is then flat, and the impulse response is delayed rather than distorted.

*Numerical check.* The demonstration sends an impulse through the length-5
average: the output begins at the input sample and its **centroid** is
$2.000000$ samples later, while the phase slope of $H$ over
$0.05 \le \omega \le 1.15\ \mathrm{rad}$ gives
$\tau_g = 2.000000$ samples with a maximum deviation of
$4.83\times10^{-13}$. The value $(M-1)/2 = 2.0$ is exact. Note the two distinct
statements: the *onset* of the output is not delayed, the *centre of mass* is.
Reporting "the filter delays by 2 samples" without saying which is a classic
source of half-sample errors in arrival-time picking.

## 8. Worked examples

### Example 1 — convolution by hand, checked against the exact result

$x = [1, 2, 3]$ (support $0..2$), $h = [1, 1, 1]$ (support $0..2$):

$$
y[0] = 1,\quad y[1] = 1+2 = 3,\quad y[2] = 1+2+3 = 6,\quad
y[3] = 2+3 = 5,\quad y[4] = 3,
$$

so $y = [1,3,6,5,3]$ and the length is $N_x + N_h - 1 = 3+3-1 = 5$. Sum check:
$\sum y = 18 = (\sum x)(\sum h) = 6\times3$, which must hold for every
convolution of finite sequences and is a useful one-line test.

The demonstration performs the same kind of check in two dimensions of
difficulty: $\text{boxcar}(4) * \text{boxcar}(4) = [1,2,3,4,3,2,1]$ exactly
(maximum difference $0.000\times10^{0}$ from the triangular result), with length
$4+4-1 = 7$.

### Example 2 — step response of a one-pole system, by hand and by recursion

For $y[n] = 0.9\,y[n-1] + x[n]$ with $x = u$ and $y[-1] = 0$:

$$y[n] = \sum_{m=0}^{n}0.9^{m} = \frac{1-0.9^{\,n+1}}{1-0.9}.$$

At $n = 10$: $0.9^{11} = 0.313810596$, so
$y[10] = (1-0.313810596)/0.1 = 6.861894$.
At $n = 63$: $0.9^{64} = 0.001179$, so $y[63] = 9.988210$. Both match the
direct recursion printed by the demonstration. The limit
$1/(1-0.9) = 10$ is the DC gain that converts input counts to output units.

### Example 3 — what a nonlinear system costs

If the "system" squares its input, superposition fails by an amount that grows
with signal amplitude. For the demonstration's two random inputs with
$a = 2.5$, $b = -1.25$:

$$\text{rms}\bigl(\mathcal Q\{ax_1+bx_2\} - a\mathcal Q\{x_1\}
- b\mathcal Q\{x_2\}\bigr) = 11.3831,$$

against an output rms of $13.5118$ — a relative violation of $0.8425$. The
number is not small and does not shrink with better arithmetic: it is $2ab\,
\langle x_1 x_2\rangle$, i.e. proportional to the signal *product*, so it is a
statement about the system, not about precision. A linear-model
instrument-response correction applied to a nonlinear instrument produces an
error of this order, and no amount of averaging removes it.

## 9. Units and dimensional analysis

| Quantity | Symbol | Unit | Note |
|---|---|---|---|
| input, output | $x, y$ | e.g. counts, V, m/s | may differ |
| impulse response | $h$ | output unit per input unit | a response, not a gain |
| frequency response | $H(e^{i\omega})$ | output unit per input unit | dimensionless only if $x, y$ share units |
| DC gain | $H(e^{i0})$ | output unit per input unit | equals $\sum h$, so it carries $h$'s units |
| group delay | $\tau_g$ | samples (or s if multiplied by $\Delta t$) | a time-like quantity |

For an ideal differentiator with step $\Delta t$, $h[0] = 1/\Delta t$,
$h[1] = -1/\Delta t$, so $h$ carries units of per second and the output of a
position input is a velocity. If a computed $h$ comes out dimensionless for a
system that changes units, a $\Delta t$ has been dropped.

## 10. Python demonstration

`code/lti_systems_demo.py` is print-only, single-process, uses `numpy` and
`scipy.signal`, and runs in about a second. It:

1. measures the superposition and time-invariance residuals of an FIR system;
2. recovers the impulse response and rebuilds the output by superposition;
3. measures the failure of superposition for a squaring system;
4. compares $\sum\lvert h\rvert$ with $1/(1-a)$ for a stable and an unstable
   one-pole system;
5. computes step responses and DC gains, and checks $s[n] = (1-a^{n+1})/(1-a)$;
6. verifies the eigenfunction property three ways, including `freqz`;
7. measures the group delay of a causal moving average by two independent
   methods;
8. convolves two boxcars and compares with the exact triangle.

```bash
cd 20-signal-processing/01-signals-and-systems/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python lti_systems_demo.py
```

## 11. Assumptions and regime of validity

1. **Linearity holds over a stated amplitude range, not in general.** Real
   sensors saturate, real coils have eddy-current and hysteresis terms, and real
   amplifiers clip. The demonstration's factor of $0.84$ relative violation for a
   squaring system is the size of the error when the assumption fails outright.
2. **Time-invariance fails when the instrument changes.** Thermal drift,
   ageing, clock drift and a changed gain state are time-varying. An LTI
   correction is invalid across a gain change; split the record instead.
3. **Convolution assumes zero initial conditions.** A recursive system with a
   non-zero initial state adds a *zero-input response* that is not described by
   $h$. The one-pole results above assume $y[-1] = 0$.
4. **Causality is a statement about the system, not the software.** Applying a
   symmetric FIR to a stored record is acausal; the same operator implemented in
   real time must be truncated, which costs a phase error
   ([20-01-04](04-transfer-functions.md)).
5. **$H(e^{i\omega})$ is only defined where the sums converge.** For an unstable
   system the frequency response still exists as a formal function of
   $z = e^{i\omega}$, but it does not describe a bounded output; the demonstration
   prints the divergent absolute sum precisely to keep that distinction visible.
6. **Everything here is discrete-time.** The continuous-time convolution
   $y(t) = \int h(\tau)x(t-\tau)\,\mathrm d\tau$ has the same properties; the
   bridge and its sampling conditions are in
   [20-01-05](05-sampling-theory.md).

## 12. Exercises

- [`exercises/02-lti-systems-exercises.md`](./exercises/02-lti-systems-exercises.md)
- [`exercises/02-lti-systems-solutions.md`](./exercises/02-lti-systems-solutions.md)

## 13. Common pitfalls

1. **Testing linearity with a single input.** Superposition must be checked with
   two independent inputs and non-trivial $a, b$; one input can pass by accident.
2. **Forgetting the offset.** An affine system $y = \mathcal H\{x\} + c$ fails
   (L) immediately. Remove and record the offset before claiming LTI.
3. **Reading $\lvert H\rvert = 1$ as "no effect".** A pure delay has
   $\lvert H\rvert = 1$ and a large phase; the waveform is unchanged in shape but
   displaced in time.
4. **Confusing the onset of a response with its centre.** The 5-point average
   starts at 0 samples and centres at 2.
5. **Applying a stability test only to FIR filters.** Every FIR with finite
   coefficients is BIBO-stable; the work is in IIR, where a single pole outside
   the unit circle destroys the output.
6. **Assuming superposition when the input is large.** The violation scales with
   the signal amplitude, so a calibration performed with a small pulse
   systematically underestimates the error on a large one.

## 14. Mastery checkpoint

Without notes:

**(a)** State the two LTI axioms and give one geophysical example of a system
that violates each.
**(b)** Derive $y[n] = \sum_k h[k]x[n-k]$ from the axioms in four steps.
**(c)** Convolve $x = [2, -1, 3]$ with $h = [1, 0.5]$ by hand and check the
result with $\sum y = (\sum x)(\sum h)$.
**(d)** For $y[n] = 0.8\,y[n-1] + x[n]$: give $h[n]$, $\sum\lvert h\rvert$, the
DC gain and the $10\%$-to-$90\%$ rise time of the step response in samples.
**(e)** Explain why a causal system cannot have $\arg H$ linear with zero slope.
**(f)** A geophone's step response reaches $0.632$ of its final value in $2\ \mathrm{ms}$.
What does that say about $a$, and what is the DC gain if $h$ is normalised so
that the final value is $1$?

Answers for (c)–(d) are in the
[solutions](./exercises/02-lti-systems-solutions.md).

## 15. Related modules

- [20-01-03 Convolution, Correlation and Filtering](03-convolution-and-filters.md) —
  convolution as a computation, and its correlation twin.
- [20-01-04 Transfer Functions, Poles and Zeros](04-transfer-functions.md) — the
  $z$-domain view of $H$.
- [20-01-05 Sampling, Nyquist and Reconstruction](05-sampling-theory.md) — what
  discretisation does to all of this.
- [20-03 Digital Filtering](../03-digital-filtering/README.md) — designing $h$ to
  meet a specification.
- [01-10 Fourier Analysis and Spectral Methods](../../01-mathematics/10-fourier-analysis/README.md) —
  the transform theory behind $H(e^{i\omega})$.
- [03-03 SciPy for Scientific Computing](../../03-scientific-computing/03-scipy/README.md) —
  `freqz`, `lfilter` and `lsim`.
