---
id: 01-03-02
title: "Trigonometric Identities and Their Uses"
level: beginner
prereqs: ["01-03-01"]
estimated_minutes: 75
tags: [trigonometry, identities, superposition, phasors]
---

# Trigonometric Identities and Their Uses

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Pythagorean, addition, double-angle, half-angle and
   product-to-sum identities from the unit circle rather than recalling them.
2. **Choose** the identity that removes work from a calculation, and say what
   the calculation became easier to interpret.
3. **Combine** a cosine and a sine of the same frequency into a single sinusoid
   with an amplitude and a phase, and recover both.
4. **Explain** beats as a consequence of the sum-to-product identity, and
   predict the beat period for two given frequencies.
5. **Verify** an identity numerically, and state what such a verification does
   and does not prove.
6. **Recognise** the identities that recur in geophysics: the ray parameter
   identity, the apparent-dip relation, and the harmonic decomposition of a
   periodic signal.

## Prerequisites

[01-03-01 Angles, Triangles and the Unit Circle](./01-angles-and-triangles.md)
for the unit-circle definitions and the two triangle laws.

## 1. What an identity is, and why you want one

An **identity** is an equation true for every value of its variables. You do not
solve it; you use it to replace one expression with another that is easier to
compute, easier to differentiate, or easier to interpret physically.

That last clause is the point. In geophysics a change of form is usually a
change of meaning. Writing

$$A\cos(\omega t) + B\sin(\omega t) = C\cos(\omega t - \phi)$$

is not algebra for its own sake: the left side is what a model computes as two
summed responses, and the right side is what an instrument reports as an
amplitude and a phase. The identity is the bridge between a computation and a
measurement.

## 2. The Pythagorean family

Everything starts with one fact from the unit circle:

$$\boxed{\cos^{2}\theta + \sin^{2}\theta = 1}.$$

Dividing by $\cos^{2}\theta$ and by $\sin^{2}\theta$ in turn, wherever those are
non-zero, gives the other two members of the family:

$$1 + \tan^{2}\theta = \sec^{2}\theta, \qquad
1 + \cot^{2}\theta = \csc^{2}\theta .$$

**Where you will meet these.** Every time you eliminate a square root in an
inverse problem — solving for an angle from two components, or converting
between a slowness and a direction cosine — you are using
$\cos^{2} + \sin^{2} = 1$ to trade a square root for a subtraction. In the
direction-cosine parameterisation of a ray, the three components $(l, m, n)$
satisfy $l^{2} + m^{2} + n^{2} = 1$; that constraint is why specifying two of
them fixes the third up to a sign, and the sign is a branch question, not an
algebraic one.

## 3. The addition formulas, derived by rotation

Let $R(\theta)$ be the rotation of the plane anti-clockwise by $\theta$:

$$R(\theta) =
\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$

Rotation by $\theta$ followed by rotation by $\phi$ is rotation by $\theta+\phi$,
because angles add:

$$R(\theta)\,R(\phi) = R(\theta + \phi).$$

Multiply the matrices and read off the entries:

$$\begin{pmatrix}
\cos\theta\cos\phi - \sin\theta\sin\phi & -\cos\theta\sin\phi - \sin\theta\cos\phi \\
\sin\theta\cos\phi + \cos\theta\sin\phi & -\sin\theta\sin\phi + \cos\theta\cos\phi
\end{pmatrix}
=
\begin{pmatrix} \cos(\theta+\phi) & -\sin(\theta+\phi) \\
\sin(\theta+\phi) & \cos(\theta+\phi) \end{pmatrix}.$$

Equating the upper-left and lower-left entries gives the two addition formulas:

$$\boxed{\cos(\theta+\phi) = \cos\theta\cos\phi - \sin\theta\sin\phi}, \qquad
\boxed{\sin(\theta+\phi) = \sin\theta\cos\phi + \cos\theta\sin\phi}.$$

Two remarks on this derivation.

**It requires no diagram.** The rotation-matrix argument is the cleanest route
from the unit circle to the addition formulas, and it is worth remembering as a
*derivation* rather than a proof-by-picture that you must reconstruct from
scratch each time.

**It is the same algebra as the two-slit problem.** Anything that composes
angles multiplicatively — rotations, phasors, transmission through a stack of
layers — carries this structure. The composition law of angles *is* the addition
formula.

## 4. Consequences you will actually use

### 4.1 Double angle

Set $\phi = \theta$:

$$\sin 2\theta = 2\sin\theta\cos\theta, \qquad
\cos 2\theta = \cos^{2}\theta - \sin^{2}\theta = 1 - 2\sin^{2}\theta = 2\cos^{2}\theta - 1 .$$

The three forms of $\cos 2\theta$ are not equivalent in practice. Which you pick
is decided by which quantity you know: use $1 - 2\sin^{2}$ when the sine is given,
$2\cos^{2} - 1$ when the cosine is.

### 4.2 Half angle

Invert the last two forms:

$$\sin^{2}\frac{\theta}{2} = \frac{1 - \cos\theta}{2}, \qquad
\cos^{2}\frac{\theta}{2} = \frac{1 + \cos\theta}{2}.$$

These give $\left|\sin(\theta/2)\right|$, not $\sin(\theta/2)$. The sign must be
supplied from the quadrant of $\theta/2$ — the first appearance in this module of
the branch problem that dominates
[01-03-03](./03-inverse-trig.md).

### 4.3 Product to sum and sum to product

Adding and subtracting the two addition formulas, with $\theta = (u+v)/2$ and
$\phi = (u-v)/2$ in one case and simple substitution in the other, yields

$$\sin u + \sin v = 2\sin\!\left(\frac{u+v}{2}\right)\cos\!\left(\frac{u-v}{2}\right),$$

$$\cos u + \cos v = 2\cos\!\left(\frac{u+v}{2}\right)\cos\!\left(\frac{u-v}{2}\right),$$

$$\sin u \cos v = \tfrac12\left[\sin(u+v) + \sin(u-v)\right].$$

The **sum-to-product** pair is the one that explains interference and beats.
The **product-to-sum** pair is what turns a nonlinear product of oscillations
into a sum of frequencies — which is why a multiplicative process such as
mixing in a seismometer, or amplitude modulation in a climate proxy record,
manufactures a difference-tone at $u - v$ that was not present in either input.

### 4.4 The phasor (quadrature) form

For constants $a$, $b$ define

$$A = \sqrt{a^{2} + b^{2}}, \qquad \phi = \operatorname{atan2}(b, a).$$

Then

$$a\cos\omega t + b\sin\omega t = A\cos(\omega t - \phi).$$

*Proof.* Expand the right side with the addition formula:

$$A\cos(\omega t - \phi) = A\cos\omega t\cos\phi + A\sin\omega t\sin\phi.$$

Matching coefficients requires $a = A\cos\phi$ and $b = A\sin\phi$. Squaring and
adding gives $A^{2} = a^{2}+b^{2}$, and the ratio gives $\tan\phi = b/a$ with the
correction supplied by `atan2`.

This is the identity that converts a computed waveform into a reported amplitude
and phase. The demonstration checks it numerically with $A = 2.5$, $\phi = 0.7$:

```text
A cos(phi) = 1.9121054682   (in-phase amplitude)
A sin(phi) = 1.6105442181   (quadrature amplitude)
hypot(a, b) = 2.5000000000   (recovers A)
atan2(b, a) = 0.7000000000   (recovers phi)
```

and then confirms that the two forms agree at each sample:

```text
   t (s)    A cos(wt-phi)    a cos(wt)+b sin(wt)
    0.00     1.9121054682           1.9121054682
    0.25     2.4935799584           2.4935799584
    0.50     2.1225916581           2.1225916581
    0.75     0.9408454887           0.9408454887
    1.00    -0.6002716793          -0.6002716793
```

The recovery of $A$ and $\phi$ from $(a, b)$ is exact here, which is the whole
content of the identity: the pair $(a, b)$ and the pair $(A, \phi)$ carry
identical information.

## 5. Worked derivations

### 5.1 Beats, derived rather than asserted

**Problem.** Two oscillations of equal amplitude and slightly different
frequencies are added. Describe the result, and find the period of the slow
envelope.

**Solution.** Use sum-to-product on the sum of two cosines:

$$\cos\omega_1 t + \cos\omega_2 t
= 2\cos\!\left(\frac{\omega_1-\omega_2}{2}t\right)
   \cos\!\left(\frac{\omega_1+\omega_2}{2}t\right).$$

The second factor oscillates at the *mean* frequency
$(\omega_1+\omega_2)/2$ — the carrier. The first factor oscillates at the
*difference* frequency $|\omega_1-\omega_2|/2$ — the envelope. The envelope
reaches its extremes when

$$\frac{|\omega_1-\omega_2|}{2}\,t = n\pi, \qquad
t = \frac{2\pi n}{|\omega_1-\omega_2|},$$

so the interval between successive maxima is $1/|f_1 - f_2|$. For $f_1 = 1.0$ Hz
and $f_2 = 1.1$ Hz that is 10.000000 s. The demonstration also confirms that the
envelope is respected at every sample, for example at $t = 0.5$ s the sum is
$-1.951057$ while the envelope is $1.975377$: the sum never escapes its
envelope, which is a useful check on any beating calculation.

**Interpretation.** Beats are not a property of either oscillation. They are an
artefact of adding two of them, and they exist only in the sum. This matters
because a "beat" in a record is often *evidence* that two distinct physical
sources are present — two closely spaced spectral lines, two tidal
constituents, two nearby scatterers.

### 5.2 The spring–neap cycle as a beat

The two largest semidiurnal tidal constituents are M2, of period 12.4206012
hours, and S2, whose period is exactly 12 hours. Their frequencies in cycles per
hour are

$$f_{M2} = 0.0805114007, \qquad f_{S2} = 0.0833333333,$$

so the difference frequency is $0.0028219326$ cycles per hour, and the beat
period is

$$\frac{1}{0.0028219326} = 354.3671\ \text{h} = 14.7653\ \text{days}.$$

That is the spring–neap cycle: the interval over which the lunar and solar
semidiurnal tides drift into and out of phase, adding to give spring tides and
partly cancelling to give neaps.

> **State the model, not the world.** The 14.77 days is what a two-constituent
> model predicts. A real tide gauge also records K1, O1 and P1, and the observed
> neap-to-spring interval varies. Quote the model result as a model result.

### 5.3 The apparent-dip relation, revisited as an identity

Section 4.4 of [01-03-01](./01-angles-and-triangles.md) used

$$\tan\alpha = \tan\delta\,|\sin(\varphi - \theta)| .$$

Rewriting it with the identity
$\tan\theta = \sin\theta/\cos\theta$ is what makes the elimination work when you
square and add the north–south and east–west equations. The algebra is short, but
it only goes through because the tangent converts a ratio of lengths into a
ratio of sines and cosines. Identities are not decoration: they are the reason
one route through a problem exists and another does not.

### 5.4 When not to use an identity

Consider evaluating $\sin(\theta+\phi)$ for $\theta = 1.2$ rad and
$\phi = 0.9$ rad. The addition formula is available, but evaluating
$\sin(2.1)$ directly is more accurate and about as fast. The formula
$\sin(\theta+\phi) = \sin\theta\cos\phi + \cos\theta\sin\phi$ loses precision
whenever the two terms nearly cancel — that is, when $\theta+\phi$ is close to a
multiple of $\pi$, where $\sin(\theta+\phi) \approx 0$ while the two terms on the
right are individually of order 1. If your input angles are near such a
cancellation point, expand the sum argument first, then take the sine once.

This is the same numerical theme as
[01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../01-arithmetic/04-floating-point.md):
an identity that is exact in exact arithmetic can still be a worse algorithm.

## 6. Numerical verification of the identities

A numerical check does one useful thing: it catches errors of sign, of argument
order, and of degree/radian confusion, which together account for most identity
mistakes. It does nothing else — an identity that is wrong at a single point is
not an identity, and a numerical test can miss that point. Use it as a smoke
test, and prove the algebra.

The demonstration evaluates six identities at 10 000 random angle arguments and
reports the worst absolute discrepancy:

```text
  pythagorean      2.220e-16
  addition         4.441e-16
  double-angle     3.331e-16
  half-angle       4.154e-14
  product-to-sum   2.359e-16
  sum-to-product   6.661e-16
```

All six are at or near double-precision round-off,
$\varepsilon = 2.2\times10^{-16}$. The half-angle row is twenty times larger than
the others and that is expected: the formula as coded takes a square root of
$1-\cos\theta$, which for small $\theta$ is the difference of two nearly equal
numbers, and then applies a sign chosen from the quadrant of $\theta/2$. Two
extra operations, two extra chances to lose digits — and still the answer is
right to fourteen decimal places.

## 7. Common mistakes

1. **Wrong sign in $\cos(\theta+\phi)$.** It is a minus: $\cos$ of a sum has a
   minus. The sine of a sum has a plus. If you remember one and derive the other,
   you will not get this wrong.
2. **Losing the sign of the half-angle.** $\sin^{2}(\theta/2)$ determines only
   the magnitude. The quadrant of $\theta/2$ decides the sign, and no algebraic
   manipulation will supply it.
3. **Using `atan` where `atan2` is needed.** $\tan\phi = b/a$ has two solutions in
   $[0, 2\pi)$; only the signs of $a$ and $b$ separately distinguish them.
4. **Cancelling terms of order 1 to get a result of order $10^{-16}$.** Adding
   two large trigonometric terms that nearly cancel throws away every significant
   figure. Restructure the computation instead.
5. **Assuming a beat implies two sources.** It usually does, but a nonlinear
   instrument response produces difference tones too, through the
   product-to-sum identity, with no second source present.
6. **Applying an identity outside its domain.** $\tan\theta = \sin\theta/\cos\theta$
   is undefined at $\theta = \pi/2$; an algebra step that "simplifies" there has
   removed a singularity rather than resolved it.
7. **Forgetting that radians are assumed.** Every identity above is written for
   radian arguments. The addition formula is true for degrees as well, but its
   derivations and its derivatives are not.

## 8. Real-world applications

- **Travel-time curves and the ray parameter.** Snell's law is treated with the
  identities in Section 4.4 whenever a ray parameter is converted between an
  angle and a slowness, and the branch of the inverse is chosen from the geometry
  of the ray, not from the algebra.
- **Tides and long-period signals.** The spring–neap cycle of Section 5.2 is a
  beat, and tidal analysis is a least-squares fit of sinusoids whose frequencies
  are known — an application of the same $a\cos + b\sin$ decomposition.
- **Magnetotellurics and impedance phase.** The impedance of the Earth is
  reported as an amplitude and a phase; the phase is meaningful only because the
  quadrature form of Section 4.4 lets you represent a linear response by one
  complex number per frequency.
- **Interferometry and phase unwrapping.** Radar and seismic interferometry
  measure phase differences, and combining them requires the sum-to-product
  identities in the form used for a two-source interference pattern.
- **Instrument and sensor response.** A geophone or seismometer response is a
  product of second-order factors; converting amplitude and phase between the
  product form and the sum form is exactly Section 4.4 applied repeatedly.

## 9. Further reading

- **Gelfand, I. M. and Saul, M. (2001). *Trigonometry*. Birkhäuser.** Level:
  beginner. Derives the addition formulas and the sum-to-product family
  geometrically and with rotations; the treatment is closer to Section 3 than
  most school books.
- **Bronshtein, I. N. and Semendyayev, K. A. *Handbook of Mathematics*.**
  Level: reference. A compact list of the identities, useful as a check when you
  have derived something and want to confirm its form.
- **Hamming, R. W. (1989). *Digital Filters* (3rd ed.). Dover.** Level:
  intermediate. Chapter 2 on the running-sum and harmonic viewpoint is a brisk
  reminder that a sum of sinusoids is a filter, and that identities are the
  arithmetic of filters.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted text,
> and you should confirm current availability and editions through your library
> before relying on them.

## 10. Related lessons

- [01-03-01 Angles, Triangles and the Unit Circle](./01-angles-and-triangles.md) —
  the unit circle these identities come from.
- [01-03-03 Inverse Trigonometric Functions and Branch Ambiguity](./03-inverse-trig.md) —
  the sign problems that the half-angle formula introduces.
- [01-03-05 Phase, Harmonics and Superposition of Oscillations](./05-phase-and-harmonics.md) —
  this lesson's algebra applied to signals.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../05-single-variable-calculus/04-taylor-series.md) —
  the approximation that every identity here can be expanded into.
- [01-10-01 Fourier Series and Periodic Decomposition](../10-fourier-analysis/01-fourier-series.md) —
  where the sum of sinusoids becomes a basis.

## Exercises and self-assessment

Exercises are in
[`exercises/02-trig-identities-exercises.md`](./exercises/02-trig-identities-exercises.md),
with solutions in
[`exercises/02-trig-identities-solutions.md`](./exercises/02-trig-identities-solutions.md).

Before moving on, you should be able to:

- [ ] Derive the addition formulas from the rotation matrices without notes.
- [ ] Convert $3\cos\omega t - 4\sin\omega t$ to amplitude-phase form in your head
      (amplitude 5, phase $\operatorname{atan2}(-4, 3)$).
- [ ] State the beat period for frequencies 0.25 Hz and 0.30 Hz.
- [ ] Explain why the half-angle identity needs a sign but the double-angle
      identity does not.
- [ ] Say what a numerical identity check proves, and what it does not.
