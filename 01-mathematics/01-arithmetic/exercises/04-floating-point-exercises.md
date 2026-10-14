# Exercises — 01-01-04 Floating-Point Representation, Round-Off and Catastrophic Cancellation

Attempt these **closed-book**, on paper, before opening the
[solutions](./04-floating-point-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Where an exercise asks for a computer check, write down your prediction first.
The predictions you get wrong are the ones that teach you something.

---

## ★ Foundational

**★1.** For IEEE 754 binary64, state:

(a) the value of machine epsilon $\varepsilon_{\text{mach}}$;
(b) the unit roundoff $u$;
(c) how many decimal significant digits are guaranteed.

Then decide, **without computing**, whether each of the following differs from
$1.0$ in binary64, and give the reason:

1. `1.0 + 1e-17`
2. `1.0 + 1e-16`
3. `1.0 + 2.3e-16`

---

**★2.** Complete the table of ulp (the gap to the next representable double).

| $x$ | `math.ulp(x)` |
|---|---|
| $1$ | |
| $1000$ | |
| $10^{6}$ | |
| $10^{16}$ | |

State the rule that relates the ulp to the magnitude of $x$. Then decide whether
the difference `x - 0.4` is represented exactly when $x = 1.0$.

---

**★3.** Which of these numbers are **exactly** representable in binary64?

(a) $0.5$  (b) $0.25$  (c) $0.75$  (d) $3/8$  (e) $0.1$  (f) $0.2$
(g) $1/3$

Give the general criterion (in terms of the denominator in lowest terms), and
explain in one sentence why the criterion arises from the binary point.

---

**★4.** (a) Predict the value of `0.1 + 0.2 == 0.3` and then check it.

(b) `Decimal(0.1 + 0.2)` prints the exact stored value of the sum. Write it out
to the printed precision and compare it with `Decimal(0.3)`.

(c) Is the computed sum larger or smaller than the true $0.3$? By what relative
amount? Report the relative error to one significant figure.

---

## ★★ Applied

**★★5.** The quantity $f(x) = \dfrac{1-\cos x}{x^{2}}$ has the limit $1/2$ as
$x \to 0$.

(a) Compute $f$ naively in binary64 at $x = 10^{-4}, 10^{-6}, 10^{-8}$ and
report both the value and the relative error against $0.5$.

(b) Derive the identity $1 - \cos x = 2\sin^{2}(x/2)$ and use it to compute $f$
at the same three points.

(c) At which $x$ does the naive evaluation return exactly $0.0$? Explain the
mechanism in one sentence.

(d) Which of the two forms would you ship in a geophysical code that computes
attenuation or gravity corrections involving $1-\cos\theta$? Justify the answer
in terms of *relative* error, not absolute error.

---

**★★6.** Summing $n$ copies of $0.1$ deliberately in an accumulation loop gives
these absolute errors against the exact value $n/10$:

| $n$ | naive absolute error |
|---|---|
| $10^{4}$ | $1.588\times10^{-10}$ |
| $10^{5}$ | $1.885\times10^{-8}$ |
| $10^{6}$ | $1.333\times10^{-6}$ |
| $10^{7}$ | $1.610\times10^{-4}$ |

(a) Compute `error / n**2` for each row. What does the near-constant result
imply about how the error grows?

(b) Predict the naive error at $n = 10^{8}$ from your fitted coefficient, and
state the two assumptions your prediction makes.

(c) For $n = 10^{6}$, compare the plain loop with Kahan compensated summation and
with `math.fsum`. Report all three results.

(d) The standard bound for naive summation is
$(n-1)u\sum|x_k|$. Compute it for $n=10^{6}$ and $x_k = 0.1$ and compare with the
observed error. Is the bound tight, loose, or wildly loose?

---

**★★7.** Consider the list `[1e16, 1.0, -1e16]`.

(a) Accumulate it with an explicit `for` loop starting from `0.0`. Predict the
result, then check it.

(b) Compute it with `math.fsum`. Predict, then check.

(c) Do the same with the built-in `sum()`. Explain why it agrees with
`math.fsum` here, and state what that implies about which construct is "naive"
in modern Python.

(d) Rewrite the list in an order that makes the explicit loop exact, and explain
why that order works.

---

**★★8.** A gravity survey gives an observed value of 979 812.37 mGal and a
computed theoretical value of 979 802.15 mGal at the same station.

(a) Compute the anomaly.

(b) Estimate how many decimal digits of the two data are "common" and therefore
do not constrain the anomaly. Use the ratio of the datum to the anomaly.

(c) If each datum carries a relative representation error of order $u$, what
absolute error does each datum carry in mGal? What relative error does that
impose on the anomaly?

(d) Compare your answer in (c) with the instrument resolution of a typical
modern relative gravimeter, which is of order $0.01$ mGal. Which dominates the
error budget at this station?

---

**★★9.** The quadratic $x^{2} - 10^{8}x + 1 = 0$ has roots approximately
$10^{8}$ and $10^{-8}$.

(a) Compute both roots with the naive formula
$x = \left(-b \pm \sqrt{b^{2}-4ac}\right)/(2a)$.

(b) Compute the small root again using $x_2 = c/(a x_1)$ with $x_1$ the large
root.

(c) Use the 50-digit decimal module to get an exact small root, and report the
absolute error of both routes.

(d) Explain why the large root is fine and the small root is not, referring to
the *relative* error of the subtraction.

---

## ★★★ Research-oriented

**★★★10.** Binary32 (single precision) is not available in the Python standard
library, but it can be emulated, because reading a value written as a 32-bit
float rounds it to binary32:

```python
import struct

def to_float32(x: float) -> float:
    return struct.unpack("f", struct.pack("f", x))[0]
```

(a) Measure $\varepsilon_{\text{mach}}$ for binary32 by bisection: find the
smallest power of two $2^{-k}$ such that `to_float32(1.0 + 2**-k) != 1.0`.
Report the exponent $k$ and the decimal value, and confirm
$\varepsilon_{\text{mach}} = 2^{-(p-1)}$ with the correct $p$.

(b) Compute `to_float32(0.1)` and `Decimal(to_float32(0.1))`. How large is the
relative representation error compared with binary64?

(c) Repeat the naive evaluation of $(1-\cos x)/x^{2}$ from ★★5, but round every
intermediate result through `to_float32`. At which $x$ does it collapse to zero?
Compare with the binary64 crossover.

(d) Write a four- or five-sentence report: method, measurements, the practical
precision of binary32 for this kind of calculation, and the limits of your
conclusion (which does not extend to other functions, other argument ranges, or
to code compiled with different optimisation settings).

---

**★★★11.** The **central** difference approximates a derivative better than the
forward difference:

$$f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}.$$

(a) Using Taylor's theorem, show that the truncation error is
$\dfrac{h^{2}}{6}|f'''(x)|$ to leading order, and that the round-off error is
about $\dfrac{2u|f(x)|}{h}$.

(b) Add the two and minimise over $h$ to show that the optimal step is
$h^{*} = \left(\dfrac{6u|f|}{|f'''|}\right)^{1/3}$, so that
$h^{*} \propto u^{1/3}$ and the achievable error is
$\mathcal{O}(u^{2/3})$.

(c) Evaluate $f(x)=\sin x$ at $x=1$ for $h \in \{10^{-1}, 10^{-2}, \dots,
10^{-13}\}$ and tabulate the absolute error. Report the observed best $h$ and
the observed minimum error.

(d) Compare the observed best $h$ and minimum error with the prediction from
(b). Do the two agree to within a factor of two?

(e) Contrast this with the forward difference of Section 5.6 of the lesson
($h^{*} \propto u^{1/2}$, error $\mathcal{O}(u^{1/2})$) and state which scheme
you would use for a numerical derivative in an inversion code, and at which
step size.

---

## Extension ideas

- Derive the error of the **trapezoidal rule** as a function of the number of
  intervals for a smooth function, and find the point at which round-off
  dominates the $\mathcal{O}(h^{2})$ convergence. This is the practical reason
  quadrature libraries stop refining.
- Implement Kahan summation and compare its error with naive summation over a
  synthetic seismogram of $10^{7}$ samples whose values vary by six orders of
  magnitude. Report the empirical growth exponent of each.
- Use `math.nextafter` to walk from $1.0$ towards $+\infty$ and count the number
  of representable doubles in $[1, 2)$. Confirm that it equals $2^{52}$.
- Take a formula from your own work that subtracts two nearly equal quantities
  and reformulate it algebraically. Show, with measurements, that the
  reformulation reduces the relative error.
