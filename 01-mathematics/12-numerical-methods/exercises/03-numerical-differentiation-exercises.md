# Exercises — 01-12-03 Numerical Differentiation and Finite-Difference Stencils

Attempt these **closed-book** before opening the
[solutions](./03-numerical-differentiation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: $u$ is the double-precision unit roundoff, $u \approx
2.2\times10^{-16}$; a uniform grid with spacing $h$; $f_i=f(x_i)$; a centred
second difference is written $D^0_2$; noise has standard deviation $\sigma$ and is
independent between samples. State any convention you add.

---

## ★ Foundational

**★1.** Derive the leading truncation term of the forward difference $D^+$ and of
the backward difference $D^-$, and show that the two terms differ in sign.

---

**★2.** Show that $D^0_2 f_i$ is exact for cubic polynomials and find its leading
error term.

---

**★3.** For $u=2.2\times10^{-16}$, $\lvert f\rvert=1$, $\lvert f''\rvert=2$ and
$\lvert f'''\rvert=6$, compute the optimal step for the forward and for the centred
stencil, and the resulting minimum total error for each.

---

**★4.** A gravity profile is sampled at 20 m and read to 0.01 mGal. Estimate the
spacing at which a centred difference of the gradient stops improving, and say
which error source sets that spacing.

---

## ★★ Applied

**★★5.** Construct the five-point centred first-derivative stencil from the moment
conditions and verify its $O(h^4)$ error on $\sin x$ at $x=1$.

---

**★★6.** Derive the one-sided third-order stencil for $f'_0$ using
$f_0,f_1,f_2,f_3$, and state its truncation term.

---

**★★7.** Show that step doubling applied to $D^+$ gives an $O(h^2)$ stencil for any
smooth $f$. Then apply the same idea once more and show that the order becomes 3.
Explain why the first argument does not transfer to $D^0$.

---

**★★8.** A strain rate is estimated from two GNSS stations 12 km apart, each
providing horizontal position to 1.5 mm per day. Compute the strain-rate noise for
a single day and for a mean over one year, and state the assumption you make about
the daily errors.

---

## ★★★ Research-oriented

**★★★9.** Design and run a numerical experiment that distinguishes round-off from
data noise in the differentiation error of a centred stencil. Specify the
diagnostic, the predicted scaling of the error under each hypothesis, and report
the result of your experiment with numbers.

---

**★★★10.** A colleague reports a gravity-gradient map computed on a 250 m grid
from readings with 0.02 mGal repeatability and asks whether a finer grid would
improve the map. Answer with numbers, and state the single most useful additional
measurement you would request.
