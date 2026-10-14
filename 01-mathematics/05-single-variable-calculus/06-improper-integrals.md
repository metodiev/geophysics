---
id: 01-05-06
title: "Improper Integrals, Singularities and Convergence"
level: intermediate
prereqs: ["01-05-05"]
estimated_minutes: 90
tags: [calculus, improper-integrals, singularities, convergence]
---

# Improper Integrals, Singularities and Convergence

## Learning objectives

By the end of this lesson you will be able to:

1. **Decide** whether an improper integral converges, using the $p$-tests at
   infinity and at zero, without evaluating it.
2. **Determine** whether a singularity is integrable by examining the weight
   attached to it, and explain why $\int r^{2}\cdot(1/r)\,dr$ is finite when
   $\int (1/r)\,dr$ is not.
3. **Derive** the Bouguer slab field $2\pi G\sigma$ from an improper integral and
   state how slowly that integral converges.
4. **Explain** what logarithmic divergence means physically for two-dimensional
   potential fields, and why it forces an arbitrary reference level.
5. **Remove** a singularity by substitution, and measure the improvement in
   quadrature convergence.
6. **Recognise** when a Fourier-type integral converges absolutely, and when it
   must be interpreted as a principal value or a distribution.

## Prerequisites

[01-05-05 Integration Techniques and Definite Integrals](./05-integration.md) for
the technique, and [01-05-01](./01-limits-and-continuity.md) for limits at
infinity and infinite discontinuities.

## 1. Intuition: "improper" is a misnomer

An integral is called improper if either the interval is unbounded or the
integrand is unbounded. In geophysics that is the normal case, not the exception:

- the gravitational potential of a body involves $1/r$, which is unbounded at the
  source;
- the gravitational field of an infinite slab involves an integral to infinity,
  and the answer is finite;
- Fourier transforms integrate over the whole real line;
- the potential of an infinite line (a two-dimensional model) *diverges*, and
  that divergence is physically meaningful.

So the question is never "is this integral improper?", it is "does it converge,
how fast, and what does the answer mean?" — and the second part is what decides
whether a numerical model is usable.

## 2. Precise definitions

### 2.1 Two kinds of improper integral

**Type I (unbounded interval):**

$$\int_a^{\infty} f(x)\,dx = \lim_{L\to\infty}\int_a^{L} f(x)\,dx ,$$

and similarly for $(-\infty, b]$ and the whole line, which must be split at any
interior point and the two pieces treated separately.

**Type II (unbounded integrand):** if $f$ is unbounded at $b$,

$$\int_a^{b} f(x)\,dx = \lim_{\epsilon\to0^{+}}\int_a^{b-\epsilon} f(x)\,dx .$$

The integral **converges** if the limit is a finite number, and **diverges**
otherwise. An integral is never "the area under the curve" in an improper case
until convergence has been established.

### 2.2 The $p$-tests

$$\int_1^{\infty}\frac{dx}{x^{p}} \ \text{converges} \iff p > 1, \qquad
\int_0^{1}\frac{dx}{x^{p}} \ \text{converges} \iff p < 1 .$$

The exponent 1 is the boundary in both cases, and the boundary is *logarithmic*:
no power of $x$ describes the growth of $\int^{L}dx/x = \ln L$. Memorising the two
inequalities is less useful than remembering that near infinity you need decay
faster than $1/x$, while near zero you need growth slower than $1/x$.

### 2.3 Comparison and absolute convergence

If $0 \le f(x) \le g(x)$ for all large $x$ and $\int g$ converges, then
$\int f$ converges (and is smaller). If $\int |f|$ converges, the integral
converges **absolutely**; absolute convergence is invariant under rearrangement,
conditional convergence is not.

### 2.4 The Cauchy principal value

When a symmetric integral diverges only by cancellation, one may define

$$\text{P.V.}\int_{-\infty}^{\infty} f(x)\,dx = \lim_{L\to\infty}\int_{-L}^{L} f(x)\,dx .$$

For an odd $f$ this can be finite when the improper integral is not. Principal
values appear whenever an observation point lies exactly on a surface of sources,
and in Hilbert transforms in signal processing.

### 2.5 Two useful bounds

$$\int_L^{\infty}e^{-x^{2}}dx \le \frac{e^{-L^{2}}}{2L},
\qquad\text{and hence}\qquad
\int_{-L}^{L}e^{-x^{2}}dx = \sqrt{\pi} + O\!\left(\frac{e^{-L^{2}}}{L}\right).$$

Exponentially decaying integrands are the easy case; algebraically decaying ones
are the hard case, and the whole difficulty of improper integration is in the
difference.

## 3. Step-by-step derivations

### 3.1 The $p$-tests, quantified

For $p \ne 1$,

$$\int_1^{L}\frac{dx}{x^{p}} = \frac{L^{1-p} - 1}{1-p}, \qquad
\int_{\epsilon}^{1}\frac{dx}{x^{p}} = \frac{1 - \epsilon^{1-p}}{1-p},$$

and for $p = 1$ the two integrals are $\ln L$ and $\ln(1/\epsilon)$. The script
evaluates these exactly:

| | $p = 0.5$ | $p = 1$ | $p = 2$ | $p = 3$ |
|---|---|---|---|---|
| $\int_1^{10^{4}}$ | `1.9800e+02` | `9.2103e+00` | `9.9990e-01` | `5.0000e-01` |
| $\int_1^{10^{8}}$ | `1.9998e+04` | `1.8421e+01` | `1.0000e+00` | `5.0000e-01` |
| $\int_{10^{-12}}^{1}$ | `2.0000e+00` | `2.7631e+01` | `1.0000e+12` | — |

Read the two directions off the table. At infinity, $p = 0.5$ grows without bound
like $2\sqrt L$, $p = 1$ like $\ln L$, and $p = 2$ converges to 1 with a tail of
$1/L$. At zero, $p = 0.5$ converges to exactly 2, $p = 1$ diverges like
$\ln(1/\epsilon)$, and $p = 2$ diverges like $1/\epsilon$. **The same exponent
behaves oppositely at the two ends of the axis**, which is why the two tests are
worth keeping separate in your head.

### 3.2 Why $1/r$ does not destroy a potential integral

The gravitational potential at a field point is $-G\int dM/s$, where $s$ is the
distance from the mass element to the field point. At the field point itself,
$s \to 0$ and the integrand is unbounded. Does the integral exist?

Consider the field point at the centre of a uniform sphere of density $\rho$.
Mass elements at distance $s$ occupy a shell of volume $4\pi s^{2}\,ds$, so

$$dM = 4\pi\rho s^{2}\,ds
\quad\Longrightarrow\quad
\left|\frac{dM}{s}\right| = 4\pi\rho\,s\,ds,$$

which is bounded and integrable on $[0,R]$:

$$\int_0^{R}4\pi\rho\,s\,ds = 2\pi\rho R^{2}.$$

The $1/s$ singularity is **integrable** because the volume element carries the
weight $s^{2}$, and $s^{2}/s = s \to 0$. The script makes the same point
numerically: multiplying $1/r$ by $4\pi r^{2}$ gives $4\pi r$, which is `1.257e-05`
m at $r = 10^{-6}$ m. The general statement is:

> A singularity of the form $s^{-\alpha}$ near a field point is integrable in
> three dimensions if and only if $\alpha < 3$, because the volume element
> contributes $s^{2}$.

This is why *extended* sources always give finite potentials, and why the
point-mass potential $-GM/r$ is an idealisation that is singular only because the
mass was pushed into a set of measure zero.

### 3.3 The Bouguer slab: an improper integral that converges

Model an infinite horizontal sheet of surface density $\sigma$ as a stack of
infinitely long lines. A line of mass per unit length $\lambda$ at horizontal
distance $x$ from the observation point, observed at height $z$, produces a
vertical field component

$$dg_z = \frac{2G\lambda z}{x^{2}+z^{2}} .$$

Write $\lambda = \sigma\,dx$ and integrate:

$$g_z = \int_{-\infty}^{\infty}\frac{2G\sigma z}{x^{2}+z^{2}}\,dx
= 2G\sigma z\left[\frac{1}{z}\arctan\frac{x}{z}\right]_{-\infty}^{\infty}
= 2G\sigma\,[\arctan\infty - \arctan(-\infty)] = 2\pi G\sigma .$$

With $\sigma = 2.67\times10^{6}\ \mathrm{kg\,m^{-2}}$ (2670 kg/m³ over 1000 m) the
script obtains

$$g_z = 2\pi(6.674\times10^{-11})(2.67\times10^{6}) = 1.119637\times10^{-3}\ \mathrm{m\,s^{-2}}
= 111.96372\ \mathrm{mGal}.$$

**But look at how slowly the integral converges.** The partial integral out to
$\pm L$ is $4G\sigma\arctan(L/z)$, so the relative error after truncating at $L$ is

$$1 - \frac{2}{\pi}\arctan\frac{L}{z} \approx \frac{2z}{\pi L} .$$

The script's column of relative errors is `-6.345e-02` at $L = 10^{4}$ m,
`-6.366e-03` at $10^{5}$ m, `-6.366e-04` at $10^{6}$ m and `-6.366e-05` at
$10^{7}$ m — a factor of ten per decade, exactly $2z/(\pi L)$. To reach six digits
you would have to integrate to $L \approx 6\times10^{8}$ m, sixty times the
observation height. **Convergent is not the same as converged**: the limit exists,
and the tail decays only algebraically.

This is the derivation of the Bouguer slab correction, and it explains two
practical facts: the correction is exact for an infinite slab, and every real
survey must apply a *terrain* correction because the Earth is not infinite and
flat.

### 3.4 An exponential case: a Fourier integral

$$\int_{-\infty}^{\infty}e^{-|x|}\cos(\omega x)\,dx
= 2\int_0^{\infty}e^{-x}\cos(\omega x)\,dx
= \frac{2}{1+\omega^{2}} .$$

Two points matter. First, the split at zero is necessary because $|x|$ is not
differentiable there and quadrature rules converge poorly across a kink. Second,
the convergence is *absolute* and fast, because the integrand decays
exponentially. The script verifies the formula at five frequencies:

| $\omega$ | numeric | $2/(1+\omega^{2})$ | difference |
|---|---|---|---|
| 0.0 | `2.000000000000` | `2.000000000000` | `-1.021e-13` |
| 1.0 | `1.000000000000` | `1.000000000000` | `-6.206e-14` |
| 5.0 | `0.076923076922` | `0.076923076923` | `-8.217e-13` |

The result — a smooth, even, positive function decaying like $2/\omega^{2}$ —
is the spectral signature of an exponential decay in the time or space domain,
which is why this particular transform appears so often in attenuation and
diffusion problems. A function whose transform decays only like $1/\omega$ would
have a discontinuity; the decay rate of a transform is a statement about the
smoothness of the original.

### 3.5 The Gaussian integral

$$\int_{-\infty}^{\infty}e^{-x^{2}}dx = \sqrt{\pi} = 1.7724538509055159 .$$

The standard derivation squares the integral and evaluates the resulting double
integral in polar coordinates, which requires the machinery of
[01-06-02](../06-multivariable-calculus/02-multiple-integrals.md). What matters
here is the convergence: truncating at $\pm L$ leaves a tail smaller than
$e^{-L^{2}}/L$. The script's errors are `-8.291e-03` at $L = 2$ (bound `9.158e-03`),
`-2.733e-08` at $L = 4$ (bound `2.813e-08`) and at the level of round-off by
$L = 6$. **Gaussian integrands are the easy case; power laws are the hard case.**
That contrast governs the convergence of every Fourier transform you will compute.

### 3.6 An integrable singularity at an endpoint: $\int_0^1\ln x\,dx = -1$

Integrate by parts with $u = \ln x$, $dv = dx$:

$$\int_0^{1}\ln x\,dx = \left[x\ln x - x\right]_0^{1} = (0 - 1) - \lim_{x\to0^{+}}\left(x\ln x - x\right) = -1,$$

using $\lim_{x\to0^{+}}x\ln x = 0$, which follows from l'Hôpital applied to
$\ln x/(1/x)$. The singularity at the endpoint is integrable, and the value is
finite.

Numerically this is awkward: the script's midpoint rule converges only as $O(h)$,
with errors `+3.424e-02`, `+3.462e-03`, `+3.465e-04`, `+3.466e-05` for
$n = 10, 10^{2}, 10^{3}, 10^{4}$ — a factor of ten per decade, so the practical
accuracy is poor. Substitute $x = e^{-t}$, so $dx = -e^{-t}dt$ and $x: 0 \to 1$
becomes $t: \infty \to 0$:

$$\int_0^{1}\ln x\,dx = \int_{\infty}^{0}(-t)(-e^{-t})\,dt
= -\int_0^{\infty}t\,e^{-t}\,dt = -1,$$

the minus sign coming from the orientation of the limits, not from the physics.
The integral in $t$ now truncates with an *explicit* tail bound
$e^{-T}(T+1)$. The script confirms it:

| $T$ | truncated value | error | tail bound |
|---|---|---|---|
| 10 | `0.999500600773` | `-4.994e-04` | `4.994e-04` |
| 20 | `0.999999956716` | `-4.328e-08` | `4.328e-08` |
| 30 | `0.999999999997` | `-2.984e-12` | `2.901e-12` |

The observed error and the bound agree to four figures. **A substitution turns a
singular, slowly convergent quadrature into a smooth, exponentially convergent
one, with a computable truncation budget.**

### 3.7 Removing an algebraic singularity: $x^{-1/2}$

$$\int_0^{1}\frac{e^{-x}}{\sqrt x}\,dx, \qquad\text{substitute } x = u^{2},\ dx = 2u\,du
\;\Longrightarrow\; 2\int_0^{1}e^{-u^{2}}du = \sqrt{\pi}\,\mathrm{erf}(1) = 1.49364826562485 .$$

The script compares the two routes:

| $n$ | midpoint, raw | error | Simpson after $x = u^{2}$ | error |
|---|---|---|---|---|
| 10 | `1.300693099` | `-1.930e-01` | `1.493649896509` | `1.631e-06` |
| 100 | `1.433099895` | `-6.055e-02` | `1.493648265788` | `1.635e-10` |
| 1000 | `1.474517789` | `-1.913e-02` | `1.493648265625` | `1.821e-14` |
| 100000 | `1.491735406` | `-1.913e-03` | `1.493648265625` | `1.998e-15` |

The raw errors fall by a factor of about 3.2 per decade — $O(h^{1/2})$, the
signature of a half-power singularity — while the substituted integral is at the
floating-point floor after a thousand panels. This is the single most useful
practical lesson in the chapter: **a slow quadrature is usually a singularity in
disguise, and a substitution is usually the fix.**

### 3.8 Where the argument genuinely diverges: the potential of a line

For an infinitely long line of mass $\lambda$ per unit length, the two-dimensional
potential is

$$V(r) = 2G\lambda\ln\frac{r}{r_0} .$$

Changing the reference radius $r_0$ changes $V$ by a constant, without bound: there
is no choice of $r_0$ that makes the potential vanish at infinity, because
$\int^{L} dr/r = \ln L$ diverges. The script tabulates the effect:

| $r/r_0$ | $2G\lambda\ln(r/r_0)$ (arbitrary units) |
|---|---|
| $10^{0}$ | `0.000000e+00` |
| $10^{3}$ | `9.220472e-04` |
| $10^{6}$ | `1.844094e-03` |
| $10^{9}$ | `2.766142e-03` |

The divergence is not a numerical artefact and not a mistake. It is the statement
that an infinite source distribution has no natural zero of potential. In
practice one chooses a reference (a distant station, a regional datum, the survey
boundary) and works with potential *differences*. **Whenever a physically
meaningful zero does not exist, the observable is a difference, and your model must
say what the difference is taken relative to.**

## 4. Physical interpretation

**Integrability is decided by the weight, not by the singularity.** Section 3.2 is
the general rule: what matters is $\int r^{2}\cdot r^{-\alpha}dr$, i.e. whether
$\alpha < 3$ in three dimensions (and $\alpha < 2$ in two, $\alpha < 1$ in one).
This is why a point mass is a convenient fiction, and why every real body gives a
finite potential.

**Convergence rate decides whether a truncation is legitimate.** An exponential
tail of $10^{-6}$ is reached at a modest cutoff; an algebraic tail of $1/L$ needs
$10^{6}$ units of length. When someone reports a numerically converged improper
integral, the honest question is "converged at what rate, and did you check the
tail?"

**Divergence is information about the model, not a defect of the mathematics.** A
logarithmic divergence in a potential means the model has structure at all length
scales, i.e. it is two-dimensional and infinite. Restore the missing physics — a
finite length, a curved Earth, a smaller region — and the divergence disappears
and is replaced by a logarithm of the ratio of scales, which is the physically
correct statement.

**Absolute versus conditional convergence has numerical consequences.** An
absolutely convergent integral can be summed in any order; a conditionally
convergent one cannot. In signal processing, filters that are only conditionally
convergent require care in their discrete implementation.

## 5. Python demonstration

The companion script is
[`code/improper_integrals_demo.py`](./code/improper_integrals_demo.py), with eight
sections. Three outputs are worth quoting because they are the ones that change how
you compute:

```
3. Integrating through a singularity: substitute it away
  exact value, sqrt(pi) erf(1) = 1.4936482656248538
       n       midpoint, raw         error       Simpson after u^2         error
      10         1.300693099    -1.930e-01          1.493649896509     1.631e-06
     100         1.433099895    -6.055e-02          1.493648265788     1.635e-10
    1000         1.474517789    -1.913e-02          1.493648265625     1.821e-14
  100000         1.491735406    -1.913e-03          1.493648265625     1.998e-15
```

```
7. The Bouguer slab: an improper integral with a finite answer
  exact 2 pi G sigma = 1.119637e-03 m/s^2 = 111.96372 mGal
 half-length L (m)    numeric g_z (mGal)    rel. error    2/(pi) * arctan(L/z)
             1e+03           55.98186162    -5.000e-01            0.5000000000
             1e+05          111.25096379    -6.366e-03            0.9936340145
             1e+07          111.95659540    -6.366e-05            0.9999363380
```

```
8. Where the same argument diverges: the potential of a line mass
       1e+00                      0.000000e+00
       1e+03                      9.220472e-04
       1e+09                      2.766142e-03
```

The remaining sections confirm the $p$-tests (Section 3.1), the Gaussian tail
(`[-2, 2]` gives error `-8.291e-03` against a bound of `9.158e-03`), the Fourier
transform of $e^{-|x|}$ (all five frequencies agree to about `1e-13`) and the
exponential truncation of $\int_0^{\infty}te^{-t}dt$ (error `-4.328e-08` at
$T = 20$ against a bound of `4.328e-08`).

> **Breaking exercise.** Section 7 uses $\sigma = 2.67\times10^{6}$ kg/m² at
> $z = 1000$ m. Predict the relative error of the truncated integral at
> $L = 10^{9}$ m and at $L = 10^{6}$ m before running the script, and then explain
> why halving the observation height to $z = 500$ m halves every relative error in
> the column.

## 6. Exercises

Full set and worked solutions:
[`exercises/06-improper-integrals-exercises.md`](./exercises/06-improper-integrals-exercises.md)
and
[`exercises/06-improper-integrals-solutions.md`](./exercises/06-improper-integrals-solutions.md).
Four to start with:

**★1.** Determine convergence or divergence, with a reason:
(a) $\int_1^{\infty}\frac{dx}{x^{3/2}}$, (b) $\int_1^{\infty}\frac{dx}{x+1}$,
(c) $\int_0^{1}\frac{dx}{\sqrt x}$, (d) $\int_0^{1}\frac{dx}{x^{0.9}}$,
(e) $\int_1^{\infty}\frac{e^{-x}}{x}\,dx$.

**★2.** Evaluate or show divergence:
(a) $\int_1^{\infty}\frac{dx}{x^{2}}$, (b) $\int_0^{\infty}e^{-2x}dx$,
(c) $\int_0^{1}\ln x\,dx$.

**★★3.** Show that $\int_0^{\infty}\frac{dr}{(r^{2}+a^{2})^{3/2}} = \frac{1}{a^{2}}$
and interpret the result as a field of a line mass. Which substitution makes the
integral elementary?

**★★4.** The gravitational potential of a uniform sphere at an internal radius
$r$ requires the integral $\int_0^{R}4\pi\rho\,s^{2}\,ds$ plus a shell correction.
Explain, using the criterion of Section 3.2, why neither integral has a
non-integrable singularity. Then state the value of $\alpha$ for which a
three-dimensional source would *not* have a finite potential, and say whether such
a source can be represented by a density.

**★★★5.** A two-dimensional gravity model uses line elements, whose potential
involves $\ln r$. Build the field of a semi-infinite line mass (a line from $x = 0$
to $x = \infty$) and show that the field at a point is finite even though the
potential is not. Report the method, the result, and what the result says about
which quantities are observable.

## 7. Common mistakes

1. **Assuming a bounded-looking region has finite area.** $\int_1^{\infty}dx/x$ is
   infinite; so is $\int_0^{1}dx/x$. A picture proves nothing.
2. **Splitting an integral at a singularity and treating the pieces as ordinary
   integrals.** Each piece must be a limit, and each must converge separately;
   cancellation between divergences is not convergence.
3. **Applying the fundamental theorem across a singularity.** Evaluating
   $[-1/x]_{-1}^{1}$ and reporting 0 ignores the non-integrable singularity at 0.
   Such symmetric cancellations are principal values, and must be labelled as such.
4. **Believing a slow computation indicates slow convergence.** An algebraic tail
   converges slowly; an exponential one converges fast. Identify which you have
   before investing in more panels.
5. **Treating divergence as "no answer".** Divergence usually means the model has a
   scale missing (an infinite sheet, a line source, a perfect insulator). Add the
   physics and the integral converges.
6. **Forgetting the tail bound.** When you truncate at $L$, you owe the reader a
   statement of what the omitted tail can contribute.
7. **Integrating $|x|$-like integrands with a smooth rule.** Split at the kink
   first; a $C^{0}$ integrand degrades Simpson's order.
8. **Confusing absolute with conditional convergence.** For a conditionally
   convergent integral, the numerical answer can depend on the summation order.

## 8. Real-world applications

- **Gravity and magnetic modelling.** The field of an arbitrary body is a volume
  integral over the source; codes that discretise it into prisms are evaluating an
  integral whose integrand is singular when the observation point lies on the
  body's surface. Recognising the integrable-singularity structure is what makes
  those codes behave near a contact. See
  [07-gravity-geodesy](../../07-gravity-geodesy/README.md).
- **Bouguer and terrain corrections.** The slab field $2\pi G\sigma$ is the exact
  infinite-slab limit; the terrain correction is the finite-extent remainder, and
  its convergence is algebraic, not exponential.
- **Fourier analysis and filtering.** Transform integrals over the whole
  frequency axis are improper; their convergence rate is the smoothness of the
  original signal, and this is why windowing exists. See
  [01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md)
  and [20-signal-processing](../../20-signal-processing/README.md).
- **Two-dimensional potential field methods.** In 2-D modelling the potential
  contains $\ln r$ and therefore carries an arbitrary reference. Comparisons of
  "potential" between different codes must state the reference. See
  [09-electrical-em-methods](../../09-electrical-em-methods/README.md).
- **Diffusion kernels.** Solutions of the heat equation involve
  $\int_0^{\infty}e^{-u^{2}}du = \sqrt\pi/2$, and their tails are Gaussian — the
  benign case. See [01-09 Partial Differential Equations](../09-partial-differential-equations/README.md).

## 9. Further reading

- **Spivak, M. (2008). *Calculus* (4th ed.). Publish or Perish.** Chapters 20–22.
  Level: beginner upward. Improper integrals and their convergence tests, proved.
- **Apostol, T. M. (1967). *Calculus, Vol. 1* (2nd ed.). Wiley.** Chapter 10.
  Level: beginner to intermediate. Rigorous treatment of limits of integrals and
  the comparison test.
- **Boas, M. L. (2006). *Mathematical Methods in the Physical Sciences* (3rd ed.).
  Wiley.** Chapters 11 and 12. Level: beginner. Fourier integrals and the
  conditions under which they exist.
- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapters 1–3. Level: intermediate.
  Integrals over source distributions, including the singularity structure near a
  contact.
- **Turcotte, D. L. & Schubert, G. (2014). *Geodynamics* (3rd ed.). Cambridge
  University Press.** Chapter 4. Level: intermediate. Diffusion solutions and their
  Gaussian kernels.
- **Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990). *Applied Geophysics*
  (2nd ed.). Cambridge University Press.** Level: intermediate. Practical use of
  slab and line-element formulas in gravity and magnetic interpretation.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not reproduce copyrighted text; confirm editions and
> availability through your library before citing them. Chapter references are
> indicative rather than authoritative: editions differ in numbering and content,
> so use each book's index to find the topic.

## 10. Self-assessment checklist

- [ ] I can state both $p$-tests from memory and apply them without integrating.
- [ ] I can decide whether a singularity is integrable from the weight attached to
      it, and quote the exponent criterion in one, two and three dimensions.
- [ ] I can derive $g_z = 2\pi G\sigma$ for an infinite slab and state the
      convergence rate of the truncated integral.
- [ ] I can explain what logarithmic divergence means physically and why it forces
      a reference level.
- [ ] I can remove an algebraic singularity by substitution and measure the
      improvement in the quadrature error.
- [ ] I can bound the tail of a truncated improper integral, for both exponential
      and algebraic decay.
- [ ] I can say when a principal value is the honest answer and label it as such.

## 11. Related lessons

- [01-05-05 Integration Techniques and Definite Integrals](./05-integration.md) —
  the techniques this lesson stretches to the limits.
- [01-05-01 Limits, Continuity and the Idea of Approximation](./01-limits-and-continuity.md) —
  the limit machinery that defines an improper integral.
- [01-05-07 Sequences, Series and Convergence Tests](./07-sequences-and-series.md) —
  the discrete counterpart: convergence of sums, and the tests that decide it.
- [01-06-02 Multiple Integrals and Change of Variables](../06-multivariable-calculus/02-multiple-integrals.md) —
  the double integral behind the Gaussian value and volume integration in general.
- [01-10 Fourier Analysis and Spectral Methods](../10-fourier-analysis/README.md) —
  where improper integrals over the whole axis become the working tool.
- [01-11 Complex Numbers and Analysis](../11-complex-analysis/README.md) —
  contour integration, residues and the systematic evaluation of improper
  integrals.
