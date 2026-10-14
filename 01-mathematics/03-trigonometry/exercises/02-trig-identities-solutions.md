# Solutions — 01-03-02 Trigonometric Identities and Their Uses

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed, not estimated by hand; decimals are given to the
> precision stated. Where a question admits more than one defensible form, the
> alternatives are shown.

---

## ★1 — Exact values from the addition formulas

All three follow from writing each angle as a sum or difference of $45°$ and
$30°$, whose sines and cosines are known exactly.

**(a)** $75° = 45° + 30°$, so with
$\sin(\theta+\phi) = \sin\theta\cos\phi + \cos\theta\sin\phi$:

$$\sin 75° = \frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}
+ \frac{\sqrt2}{2}\cdot\frac12
= \frac{\sqrt6 + \sqrt2}{4} = \boxed{0.965925826289068}.$$

**(b)** $15° = 45° - 30°$, so with
$\cos(\theta-\phi) = \cos\theta\cos\phi + \sin\theta\sin\phi$:

$$\cos 15° = \frac{\sqrt2}{2}\cdot\frac{\sqrt3}{2}
+ \frac{\sqrt2}{2}\cdot\frac12 = \frac{\sqrt6+\sqrt2}{4}
= \boxed{0.965925826289068}.$$

The equality of (a) and (b) is not a coincidence: $\sin 75° = \cos 15°$ because
$75° + 15° = 90°$, the complementary-angle identity. Two different derivations
agreeing is a check on both.

**(c)** $\tan 75° = \tan(45° + 30°)$. Rather than use the tangent addition
formula, divide (a) by the corresponding cosine:

$$\tan 75° = \frac{\sin 75°}{\cos 75°}
= \frac{0.965925826289068}{0.258819045102521} = 3.732050807568878,$$

and the closed form is $2 + \sqrt3 = 3.732050807568877$ ✓.

The computed difference between the decimal quotient and the exact surd is
$1.1\times10^{-15}$, i.e. one round-off unit in the last place. **This is the best
a double-precision computation can do**, and it is the standard against which to
judge any trigonometric routine you write.

---

## ★2 — Amplitude–phase form

Use $a\cos\omega t + b\sin\omega t = A\cos(\omega t - \varphi)$ with
$A = \sqrt{a^{2}+b^{2}}$ and $\varphi = \operatorname{atan2}(b, a)$.

| | $a$ | $b$ | $A$ | $\varphi$ (rad) | $\varphi$ (deg) |
|---|---|---|---|---|---|
| (a) | 3 | $-4$ | $5$ | $-0.9272952$ | $-53.1301°$ |
| (b) | 5 | 12 | $13$ | $1.1760052$ | $67.3801°$ |
| (c) | $-2$ | 2 | $2\sqrt2 = 2.8284271$ | $2.3561945$ | $135.0000°$ |

**On the signs.** In (a) the amplitude is positive by construction and the
negative phase says the response *leads*: the peak occurs at
$t = \varphi/\omega = -0.9273/\omega$, i.e. before $t = 0$ in the convention
$\cos(\omega t - \varphi)$. Reporting $A = -5$ with $\varphi$ shifted by $\pi$
is arithmetically equivalent and is the kind of inconsistency that makes two
processing codes disagree about the polarity of an event. Pick the convention
"amplitude non-negative" and keep it.

**On (c).** Both coefficients are equal in magnitude with opposite signs, so the
result must be a sinusoid of amplitude $2\sqrt2$ phased exactly $135°$: the
components are at $180°$ and $90°$, and their vector sum is at $135°$. Any
calculation that returns a phase outside $(90°, 180°)$ for this input is wrong,
and you can tell without computing anything.

---

## ★3 — The Pythagorean family

**Proof.** Divide $\cos^{2}\theta + \sin^{2}\theta = 1$ by $\cos^{2}\theta$:

$$\frac{\cos^{2}\theta}{\cos^{2}\theta}
+ \frac{\sin^{2}\theta}{\cos^{2}\theta} = \frac{1}{\cos^{2}\theta}
\ \Longrightarrow\ 1 + \tan^{2}\theta = \sec^{2}\theta .$$

The division is invalid exactly where $\cos\theta = 0$, that is at
$\theta = \pi/2 + k\pi$ for integer $k$. There the tangent and the secant are both
undefined, and the identity is not a statement about those points. **The proof
does not fail; its domain excludes them.** This is worth noticing explicitly,
because an algebra step that divides by something is a step that changes the
domain.

**Numerical check at $\theta = 0.9$ rad:**

$$1 + \tan^{2}0.9 = 2.5879987332596475, \qquad
\sec^{2}0.9 = 2.5879987332596484 .$$

Agreement to $9\times10^{-16}$, which is four round-off units. The residual comes
from evaluating $\tan$ and $\cos$ by different internal routes; it is not
evidence of anything physical.

---

## ★4 — Triple angle

**Derivation.** Write $3\theta = 2\theta + \theta$ and apply the addition formula:

$$\sin 3\theta = \sin 2\theta\cos\theta + \cos 2\theta\sin\theta .$$

Substitute $\sin 2\theta = 2\sin\theta\cos\theta$ and
$\cos 2\theta = 1 - 2\sin^{2}\theta$:

$$\sin 3\theta = 2\sin\theta\cos^{2}\theta
+ \left(1 - 2\sin^{2}\theta\right)\sin\theta .$$

Replace $\cos^{2}\theta = 1 - \sin^{2}\theta$:

$$\sin 3\theta = 2\sin\theta\left(1-\sin^{2}\theta\right) + \sin\theta
- 2\sin^{3}\theta = 3\sin\theta - 4\sin^{3}\theta .$$

**Note the choice.** Using $\cos 2\theta = 1 - 2\sin^{2}\theta$ rather than
$\cos^{2}\theta - \sin^{2}\theta$ is what makes the result a polynomial in
$\sin\theta$ alone. The identity is the same either way; the *form* is chosen for
the purpose.

**Numerical check at $\theta = 0.4$ rad:**

$$\sin 1.2 = 0.9320390859672264, \qquad
3\sin 0.4 - 4\sin^{3}0.4 = 0.9320390859672263 .$$

Agreement to $1.1\times10^{-16}$, the last bit of the mantissa.

---

## ★★5 — Beats

**(a)** Carrier $= (0.25 + 0.30)/2 = 0.275$ Hz. Beat period
$= 1/|0.30 - 0.25| = 1/0.05 = \boxed{20\ \text{s}}$.

**(b)** The envelope is $2\cos(\pi(f_1-f_2)t)$ up to sign, which vanishes when
$\pi(f_1-f_2)t = \pi/2$, i.e. $t = 1/(2\times0.05) = \boxed{10\ \text{s}}$.
The envelope has zeros every 10 s and its maxima every 20 s.

**(c)** The envelope is $|2\cos(\pi \times 0.05 \times t)|$: it starts at its
maximum of 2, falls to zero at 10 s, rises back to 2 at 20 s, and repeats. Over
three beat periods (60 s) it completes three full lobes. The maximum value is
$\boxed{2}$, the sum of the two amplitudes — as it must be, since the envelope
cannot exceed the sum of the amplitudes and is attained when the two oscillations
are in phase.

**(d)** The factor of 2 is the difference between the *envelope* and the
*carrier*. With $\cos\omega_1 t + \cos\omega_2 t = 2\cos(\Delta\omega t/2)
\cos(\bar\omega t)$, the slow factor oscillates at
$|\omega_1-\omega_2|/2$, i.e. at a frequency of $|f_1-f_2|/2 = 0.025$ Hz. One full
cycle of that factor takes $1/0.025 = 40$ s, and within one cycle the envelope
passes through zero twice — at maximum, zero, minimum, zero — giving a
zero-to-zero spacing of 20 s. The colleague's 2 s is out by a factor of ten,
which suggests they inverted 0.05 without noticing the units: $1/0.05$ is 20, not
2.

**Cross-check.** Tap two tuning forks a semitone apart and count: the loudness
cycle is slow compared with the pitch, and it is twice as slow as the "frequency
difference" computed in hertz would suggest if you treated the difference as a
frequency of the envelope rather than of its squared magnitude.

---

## ★★6 — Product of two signals

The identity is

$$\cos\alpha\cos\beta = \tfrac12\left[\cos(\alpha-\beta)
+ \cos(\alpha+\beta)\right].$$

With $\alpha = 2\pi(13)t$ and $\beta = 2\pi(12)t$:

$$\cos(2\pi\cdot13t)\cos(2\pi\cdot12t)
= \tfrac12\left[\cos(2\pi\cdot1t) + \cos(2\pi\cdot25t)\right].$$

So the output contains exactly two components: **1 Hz and 25 Hz, each of amplitude
one half** the product's amplitude scale.

An analyst who assumed the sensor measured the sum rather than the product would
report the 1 Hz component as an unexplained low-frequency source and the 25 Hz
component as a high-frequency one, and would find no plausible physical
candidate for either. The tell is that both appear together, in equal amplitudes,
and are symmetric about the mean of the two input frequencies: 1 and 25 straddle
13. **Looking for that symmetry pattern before interpreting is a habit worth
building**, because the same pattern appears in nonlinear instrument responses,
in mixing, and in the amplitude-modulation sidebands of climate proxy records.

---

## ★★7 — Half angle with a quadrant

**Given** $\cos\theta = -0.6$, $\theta \in (90°, 180°)$.

**Step 1 — $\sin\theta$.** From $\sin^{2}\theta = 1 - 0.36 = 0.64$, so
$|\sin\theta| = 0.8$. In the second quadrant the sine is positive, hence
$\sin\theta = +0.8$. The sign comes from geometry, not from algebra: the equation
cannot supply it.

**Step 2 — the quadrant of $\theta/2$.** Since
$90° < \theta < 180°$, we have $45° < \theta/2 < 90°$: the first quadrant, where
**both** sine and cosine are positive. This is the step that determines both
signs at once.

**Step 3 — the values.**

$$\sin\frac{\theta}{2} = +\sqrt{\frac{1-\cos\theta}{2}}
= \sqrt{\frac{1.6}{2}} = \sqrt{0.8} = \boxed{0.894427190999916},$$

$$\cos\frac{\theta}{2} = +\sqrt{\frac{1+\cos\theta}{2}}
= \sqrt{\frac{0.4}{2}} = \sqrt{0.2} = \boxed{0.447213595499958},$$

$$\tan\frac{\theta}{2} = \frac{0.894427190999916}{0.447213595499958} = \boxed{2.000000000000000}.$$

**Check.** The exact half-angle formula for the tangent avoids both the square
root and the sign ambiguity when the quadrant is known:

$$\tan\frac{\theta}{2} = \frac{\sin\theta}{1+\cos\theta}
= \frac{0.8}{1-0.6} = \frac{0.8}{0.4} = 2 \quad\text{exactly.}$$

Two routes, exact agreement, and $\tan(\theta/2) = 2$ implies
$\theta/2 = 63.4349°$, hence $\theta = 126.8699°$, whose cosine is indeed
$-0.6$ ✓. **Whenever a formula exists that determines $\tan(\theta/2)$ without a
square root, prefer it** — the sign problem disappears because the tangent's
period is $\pi$, and the quadrant of $\theta/2$ is then only needed to choose
which of two antipodal angles you want.

---

## ★★8 — Adding two sinusoids

**(a)** Expand each with the addition formula.

$x_1$: $a_1 = 3\cos 0.4 = 2.76318298$, $b_1 = 3\sin 0.4 = 1.16825503$.

$x_2$: $a_2 = 2\cos 1.9 = -0.64657913$, $b_2 = 2\sin 1.9 = 1.89260018$.

**(b)** Add the components (this is where superposition acts, in the quadrature
representation):

$$a = 2.11660385, \qquad b = 3.06085520 .$$

Convert back:

$$A = \sqrt{2.11660385^{2} + 3.06085520^{2}} = \boxed{3.721403824},$$

$$\varphi = \operatorname{atan2}(3.06085520,\ 2.11660385) = \boxed{0.965792902}
\ \text{rad} = 55.3359° .$$

**(c)** The amplitudes are 3 and 2, so the resultant must satisfy
$1 \le A \le 5$; here $A = 3.7214$ ✓. The phase lies between the two input phases
$0.4$ and $1.9$ rad ✓ — also as it must, since a weighted sum of two vectors
cannot point outside the angular span they define when the weights are positive.

**Why component addition is the right move.** Adding in amplitude–phase form
requires expanding the phases anyway; adding in quadrature form is componentwise
and therefore exact and loopable. For $N$ sinusoids this is the difference between
a two-line loop and an error-prone special case, and it is the reason every
processing library represents a monochromatic response as a complex number rather
than as an amplitude and a phase.

---

## ★★★9 — An identity-verification harness

**(a)–(c)** A representative table, from the module's own demonstration
(`code/trig_foundations_demo.py`, Section 3, $10^{4}$ random angle pairs):

| Identity | Worst absolute discrepancy |
|---|---|
| $\sin^{2}+\cos^{2} = 1$ | $2.220\times10^{-16}$ |
| addition formula for sine | $4.441\times10^{-16}$ |
| $\cos 2x = 1-2\sin^{2}x$ | $3.331\times10^{-16}$ |
| half-angle for sine | $4.154\times10^{-14}$ |
| product-to-sum | $2.359\times10^{-16}$ |
| sum-to-product | $6.661\times10^{-16}$ |

Your own numbers will differ in the last digit or two — they depend on the
random generator, the seed and the range of arguments — but the *pattern* should
not: everything at the level of a few round-off units, except the half-angle.

**(d)** The half-angle row is about twenty times larger than the rest. It is
larger for a specific reason, and "round-off" is not an explanation:

- it forms $1 - \cos x$, a subtraction of two quantities that agree to fifteen
  digits when $x$ is small, so the absolute error of the numerator is inherited
  from $\cos x$ and the *relative* error of the numerator is
  $\sim 10^{-16}/(1-\cos x)$, which grows as $x \to 0$;
- it then takes a square root, which halves the relative error — a helpful
  operation;
- and it applies a sign derived from the quadrant of $x/2$, which is a
  *discrete* branch choice and can be wrong even when the magnitude is perfect.

So the observed $4\times10^{-14}$ is the round-off of $1-\cos x$ amplified by the
division and then halved by the square root. A more accurate form for small $x$
is $\sin(x/2) = \sqrt{(1-\cos x)/2}$ rewritten with the half-angle identity in
the reverse direction, or better, $|\sin(x/2)| = \sin|x|/2 \cdot \ldots$ — the
general lesson is that the *form* determines the accuracy.

**(e)** What the harness cannot do:

- It cannot prove an identity. A finite test misses all points except the ones
  sampled, and an identity that fails at exactly one argument — say
  $\theta = 0$ for a formula dividing by $\sin\theta$ — passes a random sweep
  with probability 1. Include the degenerate arguments by hand.
- It cannot distinguish a correct identity from a pair of compensating errors
  if the same algebra appears in the reference.
- It says nothing about domain restrictions. Every one of these identities has
  points where it is undefined, and `nan` propagating through a test is easy to
  mistake for a pass if the comparison is written carelessly. Always count the
  `nan`s.

---

## ★★★10 — Precision loss in the addition formula

**(a)–(b)** With $\theta = 2.0$ and $\varphi = \pi - 2.0 + \delta$, the exact value
is $\sin(\theta+\varphi) = \sin(\pi+\delta) = -\sin\delta$. Measured results:

| $\delta$ | direct | via addition formula | exact $-\sin\delta$ |
|---|---|---|---|
| $10^{-6}$ | $-1.0000000000171467\times10^{-6}$ | $-9.9999999980671106\times10^{-7}$ | $-9.9999999983333334\times10^{-7}$ |
| $10^{-9}$ | $-9.9999996027569112\times10^{-10}$ | $-9.9999997171806854\times10^{-10}$ | $-9.9999999983333334\times10^{-10}$ |
| $10^{-12}$ | $-9.9996643590242625\times10^{-13}$ | $-9.9992236712864724\times10^{-13}$ | $-9.9999999983333333\times10^{-13}$ |
| $10^{-15}$ | $-7.6571373978538989\times10^{-16}$ | $-1.0547118733938987\times10^{-15}$ | $-1.0000000000000000\times10^{-15}$ |
| $10^{-16}$ | $+1.2246467991473532\times10^{-16}$ | $+1.6653345369377348\times10^{-16}$ | $-1.0000000000000000\times10^{-16}$ |

The corresponding **relative** errors, against the exact $-\sin\delta$:

| $\delta$ | direct | addition formula |
|---|---|---|
| $10^{-6}$ | $1.8\times10^{-10}$ | $2.7\times10^{-11}$ |
| $10^{-9}$ | $4.0\times10^{-8}$ | $2.8\times10^{-8}$ |
| $10^{-12}$ | $3.4\times10^{-5}$ | $7.8\times10^{-5}$ |
| $10^{-15}$ | $0.23$ | $0.055$ |
| $10^{-16}$ | $2.2$ | $2.7$ |

**(c)** Both routes lose relative accuracy roughly as $1/\delta$, but for
different reasons, and that is the point of the exercise:

- **Direct.** The argument $\theta+\varphi$ is formed by floating-point addition.
  Representing $\pi + \delta$ costs an absolute error of order $10^{-16}$, so
  $\sin(\text{that})$ has absolute error $\sim10^{-16}$ while its magnitude is
  $\delta$; the relative error is therefore $\sim10^{-16}/\delta$.
- **Addition formula.** The two terms $\sin\theta\cos\varphi$ and
  $\cos\theta\sin\varphi$ are each of order 1, and they nearly cancel to give
  $\sim\delta$. Each product's round-off is $\sim10^{-16}$ in absolute terms, so
  again the relative error of the difference is $\sim10^{-16}/\delta$.

Note that neither route is *reliably* better: at $\delta = 10^{-6}$ and
$10^{-12}$ the formula is worse, at $10^{-15}$ it is better, and the ordering
depends on how the rounding happens to fall. Do not conclude that one form is
"more accurate"; conclude that **near-cancellation costs digits whichever way you
compute it**.

**(d)** Avoid the cancellation by restructuring, not by computing harder. Here
that is immediate, because the relation $\sin(\pi+\delta) = -\sin\delta$ is exact.
In general:

- write the expression as a function of the *small* quantity and evaluate that;
- use a series in the small quantity when no closed form exists —
  $-\sin\delta \approx -\delta + \delta^{3}/6$, accurate to 1 part in $10^{18}$ for
  $\delta = 10^{-6}$ and to working precision for smaller $\delta$;
- where the cancellation is inherent to a physical problem — a residual, a
  baseline difference, a perturbation — compute the small quantity from the
  physics rather than by subtracting two large numbers (this is why codes store
  residuals rather than recomputing them from solutions).

Note that the $\delta = 10^{-16}$ row is not a rounding failure at all: the two
representable numbers $\pi$ and $\pi + 10^{-16}$ may be the *same* double, so the
question "what is $\sin(\pi+10^{-16})$" has no answer in double precision. That is
a representation limit, and no algorithm removes it.
