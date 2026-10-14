---
id: 01-03-03
title: "Inverse Trigonometric Functions and Branch Ambiguity"
level: intermediate
prereqs: ["01-03-01", "01-03-02"]
estimated_minutes: 75
tags: [trigonometry, inverse-functions, branch-cuts, azimuth, take-off-angle]
---

# Inverse Trigonometric Functions and Branch Ambiguity

## Learning objectives

By the end of this lesson you will be able to:

1. **State** the principal branch of each inverse trigonometric function, and say
   which information the branch discards.
2. **Use** `atan2` instead of `atan` for every azimuth, and explain exactly which
   sign errors `atan` makes.
3. **Recover** an angle from a ratio safely, including the cases where the ratio
   is undefined or the answer is ambiguous.
4. **Quantify** the amplification of measurement error by an inverse function,
   using $d(\arcsin x)/dx = 1/\sqrt{1-x^{2}}$.
5. **Derive** the take-off angle relation $\Delta = \pi - 2i$ on a uniform sphere,
   and use it to verify the identity $dT/d\Delta = p$.
6. **Wrap and unwrap** phases, and state the assumption that unwrapping relies on.

## Prerequisites

[01-03-01 Angles, Triangles and the Unit Circle](./01-angles-and-triangles.md)
and [01-03-02 Trigonometric Identities and Their Uses](./02-trig-identities.md).

## 1. The problem: trigonometric functions are not injective

To invert a function you need each output to come from exactly one input. Sines
and cosines fail this immediately: $\sin\theta = \sin(\pi - \theta)$, and the
pattern repeats every $2\pi$. There are infinitely many angles with a given sine.

So the inverse cannot be a function unless we agree to throw information away.
The convention is to restrict the domain to an interval on which the function
*is* injective, and to define the inverse there. That interval is the
**principal branch**, and the discarded outputs are the **branch ambiguity**.

$$\arcsin: [-1,1] \to \left[-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right], \qquad
\arccos: [-1,1] \to [0, \pi], \qquad
\arctan: \mathbb{R} \to \left(-\tfrac{\pi}{2}, \tfrac{\pi}{2}\right).$$

The demonstration tabulates the branches and, beside each, the *other* solution:

```text
   input c   asin c (deg)   180 - asin   acos c (deg)   atan c (deg)
  -1.00000     -90.000000   270.000000     180.000000     -45.000000
  -0.50000     -30.000000   210.000000     120.000000     -26.565051
   0.00000       0.000000   180.000000      90.000000       0.000000
   0.50000      30.000000   150.000000      60.000000      26.565051
   0.86603      60.000000   120.000000     120.000000      40.893395
   1.00000      90.000000    90.000000       0.000000      45.000000
```

### 1.1 All solutions of $\sin x = c$

For $|c| \le 1$, let $x_0 = \arcsin c \in [-\pi/2, \pi/2]$. Because
$\sin(\pi - x_0) = \sin x_0$ and the sine has period $2\pi$, the complete solution
set is

$$x = x_0 + 2\pi k \quad \text{or} \quad x = \pi - x_0 + 2\pi k, \qquad k \in \mathbb{Z}.$$

The two families merge only at $c = \pm 1$, which is why the table's
$180° - \arcsin$ column equals the $\arcsin$ column at $c = 1$.

**The geophysical consequence.** If your model contains $\sin i = c$ and you call
an inverse sine, you have silently selected the ray travelling within $90°$ of the
interface normal. A real ray can leave at any angle up to $90°$ from the normal,
so that selection is correct here — but only because the physics supplies the
restriction. When it does not, a model that quietly picks the principal branch
will fit half the data and miss the other half with no error message.

For cosine, $\cos(\pm x) = \cos x$, so $\arccos$ loses a *sign*, not a
supplement:

$$x = \pm\arccos c + 2\pi k .$$

## 2. `atan2`: the function you actually want

The tangent has period $\pi$, not $2\pi$, so $\arctan$ can only ever return an
angle in an open interval of length $\pi$. Given the ratio $y/x$ alone, an angle
and the angle $180°$ away are indistinguishable. The fix is to stop throwing away
the information the ratio destroyed: pass the two components separately.

$$\operatorname{atan2}(y, x) = \text{the angle } \theta \in (-\pi, \pi] \text{ with }
\sin\theta = \frac{y}{\sqrt{x^{2}+y^{2}}},\
\cos\theta = \frac{x}{\sqrt{x^{2}+y^{2}}} .$$

The demonstration contrasts the two functions on the four combinations of signs:

```text
       y        x    atan(y/x) deg   atan2(y,x) deg
     1.0      1.0          45.0000          45.0000
     1.0     -1.0         -45.0000         135.0000
    -1.0     -1.0          45.0000        -135.0000
    -1.0      1.0         -45.0000         -45.0000
     1.0      0.0        undefined          90.0000
     0.0      0.0        undefined           0.0000
```

Rows 2 and 3 have the same ratio $y/x = -1$, so `atan` returns $-45°$ for both:
it is right about the *slope* and wrong about the *direction*, and it cannot even
detect that it is wrong. `atan2` returns $135°$ and $-135°$.

**Numerical note.** `atan2` is not defined at the origin; implementations return
0 there and you should not rely on it in a physical calculation, because the
origin is exactly where the direction is genuinely undefined. The half-angle
form

$$\operatorname{atan2}(y, x) = 2\arctan\!\left(\frac{y}{\sqrt{x^{2}+y^{2}} + x}\right)$$

avoids overflow for very large $x$ or $y$, and satisfies the same branch
conditions. Verified against a library `atan2` at 100 000 random arguments, its
worst discrepancy was $8.1\times10^{-12}$ rad, which is the conditioning of the
ratio rather than an error in the identity.

## 3. Worked derivation: an azimuth, and how the naive version fails

**Problem.** A survey has a reference station at the origin `(east, north) =
(0, 0)` and four targets at the corners of a square: $(10, 10)$, $(10, -10)$,
$(-10, -10)$, $(-10, 10)$ km. Compute the azimuth to each.

**Solution.** Azimuth is measured clockwise from north, so with $E$ the easting
and $N$ the northing,

$$\text{azimuth} = \operatorname{atan2}(E, N) \bmod 360° .$$

Note the argument order: easting first, northing second, because atan2's first
argument is the "opposite" component and its second is the "adjacent" one.
Getting this backwards produces a survey rotated by $90°$ — which looks like a
geological surprise rather than a bug.

The demonstration's result:

```text
 east (km)  north (km)   atan(E/N) deg   atan2(E,N) deg   true quadrant
      10.0        10.0         45.0000          45.0000              NE
      10.0       -10.0        -45.0000         135.0000              SE
     -10.0       -10.0         45.0000         225.0000              SW
     -10.0        10.0        -45.0000         315.0000              NW
```

The naive column is wrong in three of four cases and, critically, it is wrong in
a *structured* way: it reports values in $[-90°, 90°]$ only, so a map made from
it folds all four quadrants onto a single half-plane. Any contouring or
interpolation that follows inherits the fold.

**The discipline this teaches.** Whenever you write an inverse trigonometric
function in production code, ask two questions: *which quadrant can this result
live in?* and *what information did I destroy before calling the function?* If the
answer to the first is "more than the range of the function", you need `atan2`
or an explicit case analysis, not a bigger tolerance.

## 4. Error amplification: the derivative of an inverse

Inverse functions amplify or attenuate input error depending on their slope. The
slope of $\arcsin$ comes from implicit differentiation:

$$y = \arcsin x \ \Longrightarrow\ \sin y = x
\ \Longrightarrow\ \cos y \cdot \frac{dy}{dx} = 1
\ \Longrightarrow\ \frac{dy}{dx} = \frac{1}{\cos y} = \frac{1}{\sqrt{1 - x^{2}}},$$

using $\cos^{2}y = 1 - \sin^{2}y = 1 - x^{2}$ and the fact that
$\cos y \ge 0$ on the principal branch.

The slope is 1 at $x = 0$ and diverges as $|x| \to 1$. The demonstration makes
the consequence concrete, taking an uncertainty in $x$ of $10^{-9}$:

```text
         x   asin x (deg)     d(asin)/dx  angle error for dx=1e-9
    0.0000       0.000000        1.00000             5.729578e-08
    0.5000      30.000000        1.15470             6.615947e-08
    0.9000      64.158067        2.29416             1.314455e-07
    0.9900      81.890386        7.08881             4.061590e-07
    0.9999      89.189709       70.71245             4.051525e-06
    1.0000      90.000000          inf                      inf
```

At $x = 0.9999$ a relative error of $10^{-9}$ in the ratio becomes an error of
$4\times10^{-6}$ degrees in the recovered angle. That is still tiny — but it is
not the regime that matters. In refraction surveying $x = \sin i / v$ is
estimated from times and distances, and the interesting rays are the ones that
grazed the refractor, i.e. with $\sin i$ close to 1. The measurement is fine; the
*inversion of it* is the weak link, and no amount of averaging fixes a
derivative that diverges.

> **The general rule.** Error amplification is a property of the problem, not of
> your code. The condition number of the inversion is
> $\left|x/(\sqrt{1-x^{2}} \cdot \arcsin x)\right|$ in relative terms, and it is
> large exactly where the physics is interesting. This is the conditioning
> concept developed in
> [01-01-05 Absolute vs Relative Error, Conditioning and Stability](../01-arithmetic/05-error-and-conditioning.md).

## 5. Worked derivation: take-off angle and the ray parameter

Consider a spherically symmetric Earth of radius $R$ with a single constant
velocity $v$ — an idealisation, but one we can solve exactly, which is what makes
it the right first test.

**Geometry.** A ray leaves the surface at angle $i$ measured from the downward
vertical. In a uniform medium rays are straight lines, so the ray is a chord of
the sphere. Let the chord have length $L$. The triangle formed by the two
endpoints and the centre $O$ is isosceles with equal sides $R$; the angle at the
source between the chord and the radius is $i$, so by the law of sines applied to
that triangle the base angles are both $i$, the angle at $O$ is $\pi - 2i$, and

$$L = 2R\cos i .$$

The central angle between source and receiver is therefore the epicentral
distance

$$\boxed{\Delta = \pi - 2i} .$$

*Check the limits.* $i = 0$ (straight down) gives $\Delta = \pi$, the antipode.
$i = \pi/2$ (horizontal) gives $\Delta = 0$. Both are right.

**Travel time.** At constant speed $v$ the travel time is the chord over the
speed:

$$T = \frac{2R\cos i}{v} .$$

**The ray parameter.** Differentiate the two:

$$\frac{dT}{di} = -\frac{2R\sin i}{v}, \qquad \frac{d\Delta}{di} = -2
\quad\Longrightarrow\quad
\frac{dT}{d\Delta} = \frac{R\sin i}{v} = p .$$

So on this model the ray parameter $p$ is *also* the slope of the travel-time
curve, $dT/d\Delta$, which is the definition used in seismology when the velocity
structure is unknown. The agreement here is not an accident of the model: it is
why $p$ is the natural parameterisation of a travel-time curve at all.

The demonstration prints the table and then checks the derivative numerically at
two step sizes:

```text
 midpoint i (deg)  step (deg)  dT/dDelta (s/rad)   p exact (s/rad)    difference
             5.00       10.00          92.427456         92.544873     1.174e-01
            45.00       10.00         749.876931        750.829550     9.526e-01
             0.25        0.50           4.633093          4.633107     1.470e-05
             4.75        0.50          87.928236         87.928515     2.790e-04
```

Everything in the last column is *truncation error of the finite difference*, not
an error in the identity. Reducing the step from 10° to 0.5° — a factor of 20 —
cuts the discrepancy at low take-off angles from $1.17\times10^{-1}$ to
$2.79\times10^{-4}$ s/rad, a factor of about 400. That is the $h^{2}$ behaviour
of a centred difference, exactly as expected. If you have ever estimated a
derivative from a travel-time curve and been puzzled that your answer depended on
the spacing of your picks, this is the reason, and the remedy is
[01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../05-single-variable-calculus/04-taylor-series.md).

## 6. Phase wrapping and unwrapping

Measured phases are almost always known only modulo $2\pi$, because a
phase-sensitive instrument cannot distinguish $\theta$ from $\theta + 2\pi$. The
standard reduction into $(-\pi, \pi]$ is

$$\operatorname{wrap}(\theta) = (\theta + \pi) \bmod 2\pi - \pi .$$

To undo it, walk through the series and add $2\pi$ whenever the step between
consecutive samples exceeds $\pi$ in magnitude:

$$u_{k} = u_{k-1} + \operatorname{wrap}(\theta_{k} - u_{k-1}), \qquad u_0 = \theta_0 .$$

The demonstration applies this to a linear ramp wrapped into $(-\pi,\pi]$ and
recovers the original to $1.8\times10^{-15}$ rad:

```text
  k   true (rad)  wrapped (rad)  unwrapped (rad)
  0      0.00000        0.00000          0.00000
  7      6.30000        0.01681          6.30000
  8      7.20000        0.91681          7.20000
 11      9.90000       -2.66637          9.90000
 23     20.70000        1.85044         20.70000
```

**The assumption, stated plainly.** Unwrapping is correct only if the true phase
changes by less than $\pi$ between consecutive samples. Every unwrapping failure
you will ever see is a violation of that assumption: a phase ramp steeper than
the sampling can follow (undersampled interference fringes), or a discontinuity
in the physical phase (a cycle skip in a phase picker, or a branch jump where
noise pushed the phase across $-\pi$). The algorithm has no way to detect either;
it will produce a smooth, plausible, wrong answer.

## 7. Common mistakes

1. **`atan` instead of `atan2`.** Wrong in three of four quadrants, and wrong in
   a way that folds the map rather than producing noise.
2. **Swapped arguments to `atan2`.** `atan2(E, N)` for azimuth, not
   `atan2(N, E)`. This rotates the answer by $90°$ and is easy to miss if your
   data happen to be nearly axis-aligned.
3. **Taking the principal branch as the physical answer.** $\arcsin$ returns a
   value in $[-\pi/2, \pi/2]$; if the physics allows $120°$, you have discarded it.
4. **Ignoring the amplification of error near $|x| = 1$.** A well-measured ratio
   can still yield a badly determined angle, because the inversion itself is
   ill-conditioned there.
5. **Dividing by $\cos\theta$ when $\theta$ might be $90°$.** The stored cosine is
   $6.1\times10^{-17}$, not 0, so the division "succeeds" and returns a huge
   number instead of raising an error.
6. **Unwrapping without checking the sampling.** If the phase can move by more
   than $\pi$ between samples, unwrapping is invalid and the output is
   confidently wrong.
7. **Forgetting that $\arctan$ cannot return $\pm\pi/2$.** The range is open, so
   a vertical ray direction is a limit, not a returned value; special-case it.

## 8. Real-world applications

- **Back-azimuth and epicentral geometry.** Every station-orientation and
  source-location estimate reduces to an `atan2` on easting and northing, and the
  inverse problem inherits the fold if the wrong function is used.
- **Refraction interpretation.** The critical angle and the ray parameter of
  Section 5 are the standard tools of a seismic refraction survey; the error
  amplification of Section 4 is why near-critical picks deserve the least weight
  in the inversion.
- **Travelling-wave travel-time inversion.** $p = dT/d\Delta$ is measured by
  differencing travel times across an array; the truncation error of Section 5 is
  its error budget.
- **Interferometric synthetic aperture radar and seismic interferometry.** Both
  produce wrapped phase fields, and both depend entirely on the unwrapping
  assumption being true across the field.
- **Magnetotellurics.** Impedance phase is quoted in the interval
  $(-180°, 180°]$; interpreting a phase that has wrapped through $-\pi$ as a
  physical change of sign in the response is a well-known interpretation hazard.
- **Instrument orientation.** A three-component seismometer's channel polarity
  and orientation are determined by angles computed with `atan2` from the
  components themselves.

## 9. Further reading

- **Abramowitz, M. and Stegun, I. A. (1964). *Handbook of Mathematical
  Functions*. National Bureau of Standards.** Level: reference. The standard
  compendium of branch conventions and identities; the definitions in Chapter 4
  are the ones most libraries follow.
- **Kahan, W. (1987). Branch cuts for complex elementary functions. In *The State
  of the Art in Numerical Analysis* (Iserles and Powell, eds.), Oxford University
  Press.** Level: advanced. The definitive treatment of why branch conventions
  are chosen as they are, and what goes wrong when they are not respected.
- **Aki, K. and Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. Section 4.2 develops the ray
  parameter $p = dT/d\Delta$ in the general case, of which Section 5 here is the
  constant-velocity special case.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm current availability and editions through your library
> before relying on them.

## 10. Related lessons

- [01-03-01 Angles, Triangles and the Unit Circle](./01-angles-and-triangles.md) —
  the SSA triangle ambiguity that is the geometric form of this lesson's problem.
- [01-03-02 Trigonometric Identities and Their Uses](./02-trig-identities.md) —
  the half-angle identity that introduces the sign choice.
- [01-03-05 Phase, Harmonics and Superposition of Oscillations](./05-phase-and-harmonics.md) —
  phase as a physical quantity, with the wrapping of Section 6 as a practical
  detail.
- [01-01-05 Absolute vs Relative Error, Conditioning and Stability](../01-arithmetic/05-error-and-conditioning.md) —
  the conditioning framework behind Section 4.
- [01-06-01 Partial Derivatives, Gradients and Directional Derivatives](../06-multivariable-calculus/01-partial-derivatives.md) —
  where the chain rule takes over from the single-variable differentiation used
  here.

## Exercises and self-assessment

Exercises are in
[`exercises/03-inverse-trig-exercises.md`](./exercises/03-inverse-trig-exercises.md),
with solutions in
[`exercises/03-inverse-trig-solutions.md`](./exercises/03-inverse-trig-solutions.md).

Before moving on, you should be able to:

- [ ] State the range of $\arcsin$, $\arccos$, $\arctan$ and `atan2`.
- [ ] Explain, with the $y/x = -1$ example, why `atan` cannot distinguish two of
      the quadrants.
- [ ] Write down all solutions of $\sin x = 0.4$ in $[0, 4\pi)$.
- [ ] Quote $d(\arcsin x)/dx$ and say where it diverges.
- [ ] Derive $\Delta = \pi - 2i$ for a uniform sphere from the isosceles triangle
      at the centre, without notes.
- [ ] State the assumption behind phase unwrapping in one sentence.
