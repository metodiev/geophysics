---
id: 19-04-02
title: "Pseudospectral Methods, Transforms and Aliasing"
level: research
prereqs: ["19-04-01", "01-10-04", "01-10-05"]
tags: [numerical-modelling, pseudospectral, aliasing, fft, de-aliasing, numerical-modelling]
---

# Pseudospectral Methods, Transforms and Aliasing

**All models and data in this module are SYNTHETIC.** The signals are chosen
teaching models; the reference values are exact identities (the alias frequency,
the exact transform of a product), and every number is printed by
[`code/pseudospectral_demo.py`](./code/pseudospectral_demo.py).

## Learning objectives

By the end of this lesson you will be able to:

1. **Compute** the alias frequency of a sampled sinusoid and **verify** it
   against the exact folding identity $f_{\rm alias} = |f - \mathrm{round}(f/f_s)f_s|$.
2. **Explain** why a sampled sinusoid above the Nyquist limit is *indistinguishable*
   from its alias rather than merely inaccurately measured.
3. **State** the resolution limit of a pseudospectral scheme on a grid of $N$
   points and **measure** the error at and above it.
4. **Derive** the aliasing of a quadratic nonlinearity, **predict** the fold
   index, and **measure** the folded amplitude.
5. **Implement** and **compare** two de-aliasing rules — the 2/3 rule and 3/2
   zero padding — and **state** the condition each requires.
6. **Quantify** the error that an un-de-aliased nonlinear term injects into the
   modes a time integration will carry forward.
7. **State** which nonlinearities need which de-aliasing, and why de-aliasing is
   a property of the discretisation rather than of the implementation.

## Prerequisites

- [19-04-01 Spectral Methods: Basis Choice and Exponential Convergence](01-spectral-methods.md) —
  the transform-based derivative used throughout.
- [01-10-04 Discrete Fourier Transform and the FFT](../../01-mathematics/10-fourier-analysis/04-discrete-fourier.md) —
  the transform being applied.
- [01-10-05 Sampling, Aliasing, Leakage and Windowings](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md) —
  the one-dimensional aliasing result extended here.

## 1. Sampling relabels frequency; it does not lose it

A real sinusoid of frequency $f$ sampled at rate $f_s$ produces exactly the same
samples as a sinusoid of frequency

$$f_{\rm alias} = \left| f - \mathrm{round}\!\left(\frac{f}{f_s}\right) f_s \right|,
\qquad f_{\rm alias} \in \left[0, \tfrac{f_s}{2}\right] . \tag{1.1}$$

This is an identity, not an approximation: two frequencies differing by an
integer multiple of $f_s$ give identical samples, and no processing can separate
them. The demonstration measures the peak of the periodogram of a sampled cosine
at $f_s = 100$ samples/s:

| $f$ (Hz) | measured peak (Hz) | predicted $|f - \mathrm{round}(f/f_s)f_s|$ (Hz) |
|---|---|---|
| 10.0 | 10.00 | 10.00 |
| 45.0 | 45.00 | 45.00 |
| 60.0 | 40.00 | 40.00 |
| 110.0 | 10.00 | 10.00 |
| 210.0 | 10.00 | 10.00 |

110 Hz and 10 Hz are the same signal on this grid, to the last bit. The
consequence for modelling is direct: a scheme whose state carries a mode above
the Nyquist limit is not "slightly wrong about that mode"; it is *exactly right
about a different one*.

## 2. The resolution limit of a pseudospectral derivative

Applying (2.1) of lesson [01](01-spectral-methods.md) to a single mode
$e^{\mathrm{i}2\pi m x}$ sampled on $N$ points:

| $N$ | $m$ | $m/(N/2)$ | max error in $f'$ |
|---|---|---|---|
| 32 | 3 | 0.188 | $8.884\times10^{-14}$ |
| 32 | 12 | 0.750 | $5.695\times10^{-13}$ |
| 32 | 15 | 0.938 | $1.214\times10^{-12}$ |
| 32 | 16 | 1.000 | $2.011\times10^{2}$ |
| 32 | 17 | 1.062 | $2.011\times10^{2}$ |
| 32 | 21 | 1.312 | $2.011\times10^{2}$ |

Below the Nyquist mode the derivative is exact to round-off. At $m = N/2 = 16$
the mode is its own alias: only the cosine part is representable, the sine part
collapses, and the error jumps to $201.1$ — nine orders of magnitude, in one step
of $m$. Above it the error is the same $201.1$, because every one of those modes
aliases onto a lower one.

There is no gradual degradation to extrapolate from. That is why mesh design for
a pseudospectral code is a *statement about the solution's spectrum* — a
resolution criterion — and not a convergence study.

## 3. A quadratic nonlinearity, and the fold index measured

Take $u = \sin(2\pi kx)$ on $N = 32$ points with $k = 9$. Then

$$u^2 = \tfrac12 - \tfrac12\cos(4\pi kx) \tag{3.1}$$

needs mode $2k = 18$, which the grid cannot represent. Sampling (3.1) on the grid
folds mode 18 to $N - 18 = 14$. The demonstration measures the product's
transform and finds

| quantity | measured | exact |
|---|---|---|
| $\|c_{14}\|$ (folded) | 0.500000 | 0 |
| $\|c_0\|$ (mean) | 0.500000 | 0.5 |
| $\|c_{18}\|$ | not representable | 0.5 |

The folded amplitude is **exactly** 0.5 — the full amplitude of the mode that was
lost. The error is $O(1)$, not a small perturbation, and it lands in a *low* mode
that every subsequent operation will treat as physical.

## 4. Two de-aliasing rules, measured against the exact product

The reference is the exact product coefficients: zero-pad $u$ to $3N/2 = 48$
points, where mode 18 is representable, multiply there, and read the spectrum
back. The demonstration then compares three recipes on the band the 2/3 rule
promises to keep (modes $0\dots N/3 = 0\dots10$) and on all representable modes:

| $k$ | method | max error, modes 0–10 | max error, all modes |
|---|---|---|---|
| 9 | naive grid product | $4.720\times10^{-16}$ | $2.500\times10^{-1}$ |
| 9 | 2/3 rule | $3.755\times10^{-16}$ | $2.500\times10^{-1}$ |
| 9 | 3/2 zero padding | $4.321\times10^{-16}$ | $2.500\times10^{-1}$ |
| 12 | naive grid product | $2.500\times10^{-1}$ | $5.000\times10^{-1}$ |
| 12 | 2/3 rule | $5.000\times10^{-1}$ | $5.000\times10^{-1}$ |
| 12 | 3/2 zero padding | $4.589\times10^{-16}$ | $5.000\times10^{-1}$ |

The two blocks are the lesson.

**With $k = 9$** (which satisfies the 2/3 premise $k \le N/3$): the alias lands at
mode 14, *above* the retained band, so the naive product is already exact in
modes 0–10 and the 2/3 rule costs nothing there. No method is better than another
inside the band, and all three are equally wrong in the full spectrum — because
the full spectrum contains mode 18, which the coarse grid cannot hold at all.
That last column is not an error of the method; it is the grid's resolution
limit, and no de-aliasing can move it.

**With $k = 12$** (which violates the premise): the alias lands at mode 8, *inside*
the band the 2/3 rule claims. The naive error in the band is $0.25$; the 2/3
rule's is $0.50$, because its screening removed the legitimate mode 12 as well,
and the "exactness" it reports in that band is the exactness of having discarded
the signal. Only 3/2 padding is exact in the band in both cases — $4.6\times10^{-16}$.

The measured statement of the 2/3 rule is therefore: *it is exact in the modes it
keeps, provided the input obeys $k \le N/3$*. The condition is not optional, and
the table above is what happens when it is violated.

### 4.1 Deriving the 2/3 premise

For a quadratic nonlinearity, two input modes $m_1, m_2$ produce $m_1 + m_2$. If
all inputs satisfy $|m| \le N/3$ then all products satisfy
$|m_1+m_2| \le 2N/3$, and the alias map sends any $m > N/2$ to $N - m \ge N/3$.
So **every** aliased contribution lands in modes at or above $N/3$, exactly the
band the rule discards. Modes below $N/3$ are therefore computed exactly — which
is why the $k=9$ row shows round-off in the retained band. Discarding is the
mechanism; the premise is what makes the discarding harmless. The cost of the
rule is that it throws away a third of the spectrum *before* every product.

3/2 zero padding pays a larger transform instead. The general requirement is
easy to state: a real transform on $M$ points carries modes up to $M/2$, and a
quadratic product of input modes band-limited to $K$ reaches $2K$, so the padded
grid must satisfy $M/2 \ge 2K$, i.e. $M \ge 4K$. For the $2/3$ band $K = N/3$
this reads $M \ge 4N/3$, and the conventional choice $M = 3N/2$ satisfies it with
room to spare. The demonstration forms the product on $3N/2$ points,
where $2k$ is representable, then truncates — nothing legitimate is discarded
before the product, and the measured error is round-off in every representable
mode.

For comparison, an input band of the *full* grid, $K = N/2$, would need
$M \ge 2N$: doubling, not 1.5x. That is the arithmetic behind both rules, and it
also says what to do if neither is acceptable: keep the band below $N/3$ and pad
by $3/2$, or keep the full band and pad by $2$.

One boundary case is worth flagging. In the $k = 12$ row of the table the product
mode is $2k = 24$, exactly the padded grid's Nyquist limit (48 points). The
padded result there is exact because the product is a cosine plus a constant, and
a cosine at the Nyquist is representable. A sine at the Nyquist is not, so being
*exactly* at the limit is not a safe policy in general; the rule above is
expressed as an inequality for that reason.

## 5. What the defect costs a time integration

The right-hand side of Burgers' equation, $u_t + (u^2/2)_x = 0$, is now evaluated
on a 32-point grid for two-mode signals. Because a mode $2k > N/2$ is not
representable at all, the well-defined reference is the de-aliased flux truncated
to the resolved band — that is, what a padded code computes:

| $k_1$ | $k_2$ | $k_1+k_2$ | $\max|\mathrm{RHS}|$ (1/s) | naive relative error | 3/2 padded |
|---|---|---|---|---|---|
| 10 | 12 | 22 | 6.2832 | 8.7407 | $0.0\times10^{0}$ |
| 9 | 13 | 22 | 12.5664 | 3.6723 | $0.0\times10^{0}$ |
| 6 | 7 | 13 | 73.3338 | 0.0000 | $0.0\times10^{0}$ |

The first two rows fold the sum mode 22 onto $32-22 = 10$, inside the resolved
band, and the naive nonlinear term is wrong by **874%** and **367%** of the
signal itself. The third row has $k_1 + k_2 = 13 < 16$: no fold occurs and the
naive evaluation is exact, as it must be. **Aliasing is a property of the
spectrum, not of the scheme**, and that is why a code cannot be certified by a
test whose spectrum happens to be safe.

The error is not damped away by the time step. It is injected into low modes that
the integrator then carries forward, so a conservative pseudospectral code without
de-aliasing has an energy error whose *size* is set by the spectrum and whose
*growth* is set by the integration time — not by $\Delta t$. Reducing the step
changes how finely the error is accumulated; it does not change the error.

## 6. A fully worked de-aliasing decision

A pseudospectral code integrates a quadratic nonlinearity on $N = 256$ uniform
periodic points. The solution's spectrum currently has power up to mode 90.
Decide the de-aliasing policy, using the requirement of Section 4.1:
$M \ge 4K$ for a padded grid of $M$ points and an input band $K$.

1. **Representable band.** $N = 256$ points carry modes $|m| \le 128$.
2. **What the naive product does.** Products of modes up to 90 reach 180, which
   exceeds the Nyquist 128. The alias map sends $m > 128$ to $256 - m$: mode 180
   folds to 76, mode 128 is its own alias, and the contamination lands inside the
   physically meaningful band. The naive evaluation is not usable.
3. **Option A: the 2/3 rule.** Zero all modes with $|m| > \lfloor N/3\rfloor =
   85$ before each product, giving $K = 85$. Products reach 170, whose aliases
   land at $256 - m \ge 86$ — all above the retained band, so modes
   $\le 85$ are exact. Cost: the effective resolution drops from 128 to 85 modes,
   a 34% loss of bandwidth, paid at every nonlinear evaluation.
4. **Option B: 3/2 zero padding.** Keep $K = 85$ (the same input restriction),
   transform to $M = 384$ points where the Nyquist is 192 and $4K = 340 \le$
   $2M = 768$; more directly, $2K = 170 \le M/2 = 192$, so every product is
   representable. Multiply there, then truncate to the coarse grid. The product
   is exact up to mode 170 and can be kept up to the coarse Nyquist 128, so the
   full grid bandwidth is recovered at the cost of one larger transform pair.
5. **Option C: 2x padding.** If the input band must stay at the full 128 modes,
   no 3/2 scheme is exact: $2K = 256$ requires $M \ge 4K = 512$ points.
   Doubling is then the price of exactness.
6. **Decision.** With power currently at mode 90 the spectrum does *not* satisfy
   the $K = N/3 = 85$ premise (90 exceeds it), so Option A as usually written
   would silently discard physical signal — exactly the failure measured in
   Section 4 for $k=12$. The safe choices are Option C (2x padding, exact for the
   full band), or filtering the solution to $K \le 85$ first and recording that
   filtering as part of the model. The code must state which of these it does,
   because the difference between them is a $10^{-1}$ error in a low mode versus
   round-off, as Section 4 measured.

## 7. Assumptions and regime of validity

1. **Periodicity, uniform sampling.** The folding identity (1.1) and the fold
   index $N-2k$ are for a uniform periodic grid. On a Chebyshev grid the aliasing
   pattern is different (there is no simple fold), and de-aliasing is normally
   done by filtering or by over-integration with the exact rule.
2. **Quadratic nonlinearity for the 2/3 rule.** The premise $k \le N/3$
   is derived for products of two factors. A cubic term needs a stricter band
   ($k \le N/4$), and a general nonlinearity needs the band computed from its
   polynomial degree; using the 2/3 rule for a cubic term is a silent error.
3. **Exact arithmetic for the identity checks.** The measured
   $|G_{\rm num} - G_{\rm closed}|$ of order $10^{-17}$ is a statement about
   double precision.
4. **The reference is itself a padded computation.** In Section 5 the reference
   is the de-aliased result, which is the best available definition when the true
   product is unrepresentable. Where an analytic reference exists (Sections 1–3)
   it is used instead; the distinction is stated rather than glossed.
5. **No claim about stability.** De-aliasing removes a consistency error; it does
   not by itself make an explicit pseudospectral time integration stable, and it
   does not make it conservative for a general nonlinearity.
6. **Signals, not fields.** Everything above is one-dimensional and scalar; the
   two- and three-dimensional cases are the same statement applied along each
   transform axis, with the same $N/3$ and $3N/2$ arithmetic.

## 8. Mastery checkpoint

Complete this without notes.

> A pseudospectral code integrates $u_t + \tfrac12(u^2)_x = 0$ on $N = 64$ uniform
> periodic points, and the solution's spectrum is currently significant up to
> mode 28.
>
> **(a)** Compute the highest mode the product can produce and decide whether the
> naive product aliases.
> **(b)** State the fold index for a product mode of 40.
> **(c)** State the largest input mode the 2/3 rule permits at this $N$, and
> whether the present solution satisfies it.
> **(d)** Give the padded grid size for the 3/2 rule and the reason that size is
> sufficient for a quadratic term.
> **(e)** The code doubles $N$ to 128 while the physical spectrum is unchanged.
> State whether the aliasing gets better, worse or neither, and why.
> **(f)** A run is reported as "converged" because halving $\Delta t$ changed the
> answer by less than $10^{-6}$. State what that demonstrates and what it does
> not.

A worked version appears with the
[exercises](exercises/02-pseudospectral-exercises.md).

## 9. Common pitfalls

1. **Believing a mode above Nyquist is merely inaccurate.** It is exactly equal
   to another mode; the demonstration measures 110 Hz appearing at 10 Hz.
2. **Extrapolating a derivative error through the Nyquist limit.** The error goes
   from $1.2\times10^{-12}$ at $m=15$ to $2.0\times10^{2}$ at $m=16$ on a
   32-point grid — nine orders in one step of $m$.
3. **Applying the 2/3 rule without its premise.** Measured: with $k=12 > N/3$ the
   rule's error in its own "trusted" band is $0.50$, worse than the naive $0.25$.
4. **Reading the "all modes" column as a method error.** The unrepresentable
   mode $2k$ cannot be held by the grid; only padding with truncation or a finer
   grid addresses it.
5. **Assuming a smaller timestep fixes aliasing.** The aliased contribution is
   injected into low modes and integrated; the step size does not change its
   size.
6. **Using the 2/3 rule for a higher-degree nonlinearity.** The band depends on
   the polynomial degree of the term.
7. **Testing a solver on a spectrum that happens to be safe.** The third row of
   Section 5's table is exact with *no* de-aliasing; a test suite built only on
   such cases certifies nothing.

## 10. Related modules

- [19-04-03 Spectral Element Methods and Their Geophysical Use](03-spectral-elements.md) —
  the same nonlinear term inside an element-based code, where over-integration
  replaces padding.
- [19-01-03 Consistency, Stability and the Lax Equivalence Theorem](../01-numerical-foundations/03-consistency-stability.md) —
  why a consistency error of this size is a correctness problem, not a small one.
- [19-08-01 Simulating a 2-D/3-D Seismic Wavefield](../08-geophysical-simulation-case-studies/01-simulate-seismic-wavefield.md) —
  a production problem whose nonlinearity (if any) and resolution criterion must
  be stated explicitly.
- [01-10-05 Sampling, Aliasing, Leakage and Windowing](../../01-mathematics/10-fourier-analysis/05-windowing-aliasing.md) —
  the data-analysis side of the same phenomenon.
- [20-signal-processing](../../20-signal-processing/README.md) — where sampling
  limits are set by instruments rather than by a grid choice.

## Materials

- Demonstration: [`code/pseudospectral_demo.py`](./code/pseudospectral_demo.py).
- Exercises: [`exercises/02-pseudospectral-exercises.md`](./exercises/02-pseudospectral-exercises.md)
  with worked [solutions](./exercises/02-pseudospectral-solutions.md).
