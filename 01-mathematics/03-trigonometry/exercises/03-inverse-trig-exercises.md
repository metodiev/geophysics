# Exercises — 01-03-03 Inverse Trigonometric Functions and Branch Ambiguity

Attempt these **closed-book**. Solutions are in
[`03-inverse-trig-solutions.md`](./03-inverse-trig-solutions.md).
Difficulty: ★ foundational · ★★ applied · ★★★ research-oriented.

Angles are in radians unless a question says otherwise. Where a problem involves
`atan2`, state the argument order you used and why.

---

## ★ Foundational

**★1.** Give **all** solutions in $[0, 2\pi)$.

(a) $\sin x = 0.3$
(b) $\cos x = -0.5$
(c) $\tan x = 1.5$

For (a), state the general solution for all real $x$ as well.

---

**★2.** Compute `atan2(y, x)` in degrees for the eight sign combinations
$y, x \in \{+1, -1\}$ together with the two axis cases $(0, 1)$ and $(1, 0)$.
Beside each, give `atan(y/x)` where it is defined. Then state in one sentence
which information `atan` discards.

---

**★3.** Write down $d(\arcsin x)/dx$, and evaluate it at $x = 0$, $0.5$, $0.9$ and
$0.99$. For what value of $|x|$ does the derivative reach 10?

---

## ★★ Applied

**★★4.** A survey reference station is at the origin. Four targets lie at
(east, north) = $(10, 10)$, $(10, -10)$, $(-10, -10)$ and $(-10, 10)$ km.

(a) Compute the azimuth to each, in degrees, using `atan2`.
(b) Compute the same four azimuths using `atan(y/x)` and explain the failure
pattern.
(c) A fifth target lies at $(0, -15)$ km. Compute its azimuth and state why
`atan(y/x)` cannot be used at all.

---

**★★5.** Inverse ray geometry. On a uniform sphere of radius $R$ and velocity
$v$, the take-off angle $i$ from the downward vertical and the epicentral
distance $\Delta$ are related by $\Delta = \pi - 2i$.

(a) Invert the relation and compute $i$ for $\Delta = 60°$, $90°$ and $120°$.
(b) For $R = 6371$ km and $v = 6$ km/s, compute the ray parameter
$p = R\sin i / v$ at each of the three angles.
(c) The inverse has an obvious limitation. State it, and say what happens to
your answer if $\Delta = 200°$.

---

**★★6.** Phase unwrapping. A phase series is measured in $(-\pi, \pi]$ at
$k = 0, 1, 2, \dots$ with samples, in radians,

$$0.00,\ 1.20,\ 2.40,\ 3.00,\ -2.80,\ -1.60,\ -0.40,\ 0.80 .$$

(a) Unwrap the series by adding multiples of $2\pi$ when consecutive samples
differ by more than $\pi$.
(b) State the assumed maximum phase step per sample.
(c) Construct a different sampled series — all samples inside $(-\pi,\pi]$ — that
unwraps wrongly, and explain why the algorithm cannot detect the error.

---

**★★7.** Inferring a velocity from a near-critical observation. The critical angle
at a sediment–rock interface is measured as $28.0° \pm 0.3°$, and the sediment
velocity is known exactly as $v_1 = 6.0$ km/s.

(a) Compute $v_2$ from $v_2 = v_1/\sin i_c$.
(b) Propagate the angular uncertainty into $v_2$.
(c) Repeat for a measurement at $i_c = 60.0° \pm 0.3°$. Compare the fractional
uncertainties and explain the difference in terms of the derivative of $\arcsin$.

---

**★★8.** For the station at $(38.00°\text{N}, 25.00°\text{E})$ and the receiver at
$(37.00°\text{N}, 23.50°\text{E})$:

(a) Compute the azimuth from the receiver to the station, and the azimuth from
the station to the receiver.
(b) By how much does the difference between them deviate from $180°$?
(c) Now do the same for two points on the same meridian. Explain the difference
between the two cases in one sentence.

---

## ★★★ Research-oriented

**★★★9.** Take-off angle, travel time and the ray parameter.

Using the uniform-sphere model $\Delta = \pi - 2i$, $T = 2R\cos i / v$ with
$R = 6371$ km and $v = 6$ km/s:

(a) Tabulate $\Delta(i)$, $T(i)$ and $p(i) = R\sin i/v$ for
$i = 0°, 10°, \dots, 90°$.
(b) Estimate $dT/d\Delta$ by finite differences at several midpoints, and compare
with $p$ at the same midpoints.
(c) Repeat with a step ten times smaller and report how the discrepancy scales.
State the expected exponent and whether your data support it.
(d) Explain why the identity $dT/d\Delta = p$ must hold exactly, using the chain
rule on the two relations above.
(e) State the limits of the model: which assumption, if removed, breaks the
closed-form relations you used?

---

**★★★10.** The conditioning of an inverse sine.

For the inversion $x = \arcsin c$, define the relative condition number

$$\kappa(c) = \left|\frac{c}{x}\frac{dx}{dc}\right|
= \left|\frac{c}{\arcsin c \sqrt{1-c^{2}}}\right| .$$

(a) Evaluate $\kappa$ at $c = 0.1, 0.5, 0.9, 0.99, 0.999$.
(b) Determine the range of $c$ in $(0, 1)$ for which $\kappa > 10$, and for which
$\kappa > 100$.
(c) Confirm (a) and (b) numerically by perturbing $c$ by a relative amount of
$10^{-6}$ and measuring the resulting relative error in $x$. Report the worst
discrepancy between the predicted and measured amplification.
(d) Interpret the result for a refraction survey: at what take-off angle does the
inversion become dangerous, and what would you do about it in practice?
(e) Show that $\kappa \to 1$ as $c \to 0^{+}$ and explain why that is the
best-conditioned limit — then explain why a refraction survey cannot exploit it,
and what that says about the trade-off between conditioning and information.
This is the conditioning framework of
[01-01-05 Absolute vs Relative Error, Conditioning and Stability](../../01-arithmetic/05-error-and-conditioning.md)
applied to a specific function.

---

## Extension ideas

- Implement `unwrap(series)` and test it on synthetic ramps of increasing slope.
  Find the slope at which it first fails, and compare with the theoretical limit of
  $\pi$ per sample.
- Implement an azimuth function that also returns an uncertainty, propagated from
  the uncertainties in the easting and northing, and show that the uncertainty
  diverges as the two components approach zero.
