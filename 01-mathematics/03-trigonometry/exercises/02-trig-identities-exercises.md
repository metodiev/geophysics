# Exercises — 01-03-02 Trigonometric Identities and Their Uses

Attempt these **closed-book**. Solutions are in
[`02-trig-identities-solutions.md`](./02-trig-identities-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

Unless stated otherwise, arguments are in radians.

---

## ★ Foundational

**★1.** Use the addition formulas to obtain exact values for

(a) $\sin 75°$  (b) $\cos 15°$  (c) $\tan 75°$

Give each in closed form (with surds) and as a decimal, and state which
identities you used.

---

**★2.** Write each expression in amplitude–phase form $A\cos(\omega t - \varphi)$.
Give $A$ exactly and $\varphi$ in both radians and degrees, to four decimal
places.

(a) $3\cos\omega t - 4\sin\omega t$
(b) $5\cos\omega t + 12\sin\omega t$
(c) $-2\cos\omega t + 2\sin\omega t$

---

**★3.** Prove from $\cos^{2}\theta + \sin^{2}\theta = 1$ that
$1 + \tan^{2}\theta = \sec^{2}\theta$, stating the one value of $\theta$ at which
the proof is invalid. Then verify the result numerically at $\theta = 0.9$ rad.

---

**★4.** Derive the triple-angle identity $\sin 3\theta = 3\sin\theta -
4\sin^{3}\theta$ from the addition and double-angle formulas, and verify it
numerically at $\theta = 0.4$ rad.

---

## ★★ Applied

**★★5.** Two oscillations of unit amplitude have frequencies 0.25 Hz and 0.30 Hz.

(a) Give the carrier frequency and the beat period.
(b) Give the time at which the envelope first vanishes.
(c) Sketch, in words, the envelope over three beat periods, and state the
maximum value the envelope attains.
(d) A colleague claims the beat period is 2 s because "the frequencies differ by
0.05 Hz, so the period is 1/0.05". Where does the factor of 2 come from in the
correct answer?

---

**★★6.** A sensor multiplies two signals, at 12 Hz and 13 Hz, together and reports
the product. Using the product-to-sum identity, list the frequencies present in
the output and their relative amplitudes. Explain why an analyst who did not know
about the multiplication would report two spurious "sources".

---

**★★7.** Given $\cos\theta = -0.6$ with $\theta$ in the second quadrant, find
$\sin(\theta/2)$, $\cos(\theta/2)$ and $\tan(\theta/2)$, with correct signs and
justifications for each sign.

---

**★★8.** Two sinusoids of the same frequency are added:
$x(t) = 3\cos(\omega t - 0.4) + 2\cos(\omega t - 1.9)$.

(a) Convert each to the form $a\cos\omega t + b\sin\omega t$.
(b) Add the components and convert back to amplitude–phase form.
(c) State the resultant amplitude and phase, and verify that the resultant
amplitude lies between $|3 - 2|$ and $3 + 2$ as it must.

---

## ★★★ Research-oriented

**★★★9.** Build an identity-verification harness.

(a) Implement numerical checks for at least eight identities from this lesson,
including the Pythagorean, addition, double-angle, half-angle, product-to-sum and
sum-to-product families.
(b) Evaluate each at $10^{4}$ or more random arguments and record the worst
absolute discrepancy for each identity.
(c) Report the table and identify any identity whose discrepancy is more than an
order of magnitude above the others.
(d) For each outlier, explain the mechanism in terms of the operations it
performs — not "round-off" but *which* subtraction, square root, or argument
construction loses digits.
(e) State clearly what your harness would fail to detect.

---

**★★★10.** Loss of precision in the addition formula.

Fix $\theta = 2.0$ rad and take $\varphi = \pi - 2.0 + \delta$, so that
$\theta + \varphi = \pi + \delta$ and $\sin(\theta+\varphi) = -\sin\delta$ is known
in closed form.

(a) For $\delta \in \{10^{-6}, 10^{-9}, 10^{-12}, 10^{-15}, 10^{-16}\}$, compute
$\sin(\theta+\varphi)$ two ways: directly, and with the addition formula
$\sin\theta\cos\varphi + \cos\theta\sin\varphi$.
(b) For each $\delta$, report the relative error of each route against the exact
value $-\sin\delta$.
(c) Explain the observed growth of the error with $1/\delta$ in each route
separately. The two routes fail for *different* reasons; say which mechanism
dominates in each.
(d) Propose a computation that avoids the loss entirely, and explain why it works.
This is the same restructuring discipline as
[01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation](../../01-arithmetic/04-floating-point.md).

---

## Extension ideas

- Repeat ★2 for a sum of three sinusoids and show that the result depends on the
  order of pairing — that is, that combining amplitudes and phases is not
  associative in the naive sense when phases wrap.
- For ★8, compute the resultant amplitude and phase as a function of the phase
  difference with the amplitudes held fixed, and describe the shape of the curve.
  This is a first look at the interference pattern that becomes the array response
  in [20-signal-processing](../../../20-signal-processing/README.md).
