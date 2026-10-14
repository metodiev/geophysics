# Exercises — 01-10-01 Fourier Series and Periodic Decomposition

Attempt these **closed-book**, on paper, before opening the
[solutions](./01-fourier-series-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Useful constants: $G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻² is **not** needed here.
The tidal speeds you need are:

| constituent | speed (deg/h) |
|---|---|
| M2 | 28.9841042 |
| S2 | 30.0000000 |
| N2 | 28.4397295 |
| K2 | 30.0821373 |
| K1 | 15.0410686 |
| O1 | 13.9430356 |
| P1 | 14.9589314 |

---

## ★ Foundational

**★1.** The square wave $f(t) = \mathrm{sign}(\sin t)$ has period $2\pi$ and
odd symmetry.

(a) Show that every $a_n$ (including $a_0$) vanishes.
(b) Compute $b_n$ for general $n$ and state which $n$ survive.
(c) State the decay rate of the coefficients as $n \to \infty$ and the
consequence for the smoothness of $f$.

---

**★2.** Convert each pair of coefficients to amplitude and phase lag, giving the
phase in $[0^\circ, 360^\circ)$.

(a) $a_1 = 3$, $b_1 = 4$
(b) $a_2 = 0$, $b_2 = -2$
(c) $a_3 = -1$, $b_3 = -1$
(d) $a_4 = 0.5$, $b_4 = 0$

---

**★3.** Evaluate, using orthogonality and stating which rule you used:

(a) $\displaystyle\int_0^{2\pi}\cos(2x)\cos(3x)\,dx$
(b) $\displaystyle\int_0^{2\pi}\sin^2(4x)\,dx$
(c) $\displaystyle\int_0^{2\pi}\cos(2x)\sin(2x)\,dx$
(d) $\displaystyle\int_0^{2\pi}\cos(0x)\cos(2x)\,dx$

---

**★4.** Two constituents have speeds 28.9841042 and 30.0000000 deg/h.

(a) Convert both to cycles per hour.
(b) Compute the beat period of their sum in hours and days.
(c) Repeat for the pair 15.0410686 and 14.9589314 deg/h and compare.

---

## ★★ Applied

**★★5.** The sawtooth wave $f(t) = t/\pi$ on $(-\pi, \pi)$, extended
periodically, has $b_n = 2(-1)^{n+1}/n$ and all $a_n = 0$.

(a) Write the partial sum with three terms.
(b) Evaluate it at $t = \pi/2$ and compare with $f(\pi/2)$.
(c) Evaluate it at $t = 0.1\pi$ and compare with $f(0.1\pi)$.
(d) Explain, using the two results, why the error is largest near the
discontinuity.

---

**★★6.** A tide gauge has recorded for 20 days.

(a) For which of the pairs M2–S2, M2–N2, K1–P1 and S2–K2 does the Rayleigh
criterion hold?
(b) For the pairs where it fails, state how much longer the record would have to
be.
(c) A colleague reports separate M2 and S2 amplitudes from the 20-day record
without quoting uncertainties. Write two sentences of review comment.

---

**★★7.** Parseval's relation for the square wave $\mathrm{sign}(\sin t)$ reads

$$\frac{1}{2\pi}\int_0^{2\pi}f(t)^2\,dt = \frac{1}{2}\sum_{n\ \mathrm{odd}} b_n^2 .$$

(a) Evaluate the left-hand side exactly.
(b) Show that the right-hand side reduces to $\dfrac{8}{\pi^2}\sum_{n\ \mathrm{odd}} \dfrac{1}{n^2}$.
(c) Deduce that $\sum_{n\ \mathrm{odd}} n^{-2} = \pi^2/8$ and evaluate it.
(d) Compute the partial sum $\sum_{n\ \mathrm{odd},\, n \le 9} n^{-2}$ and state
what fraction of $\pi^2/8$ it captures.

---

**★★8.** A constituent has amplitude $A = 1.5$ m and phase lag $\phi = 40^\circ$
referred to the epoch $t = 0$.

(a) Write its contribution as $a\cos\omega t + b\sin\omega t$.
(b) The whole record is shifted in time by a quarter of this constituent's
period. Give the new phase lag and the new coefficients.
(c) State in one sentence why the amplitude is unchanged.
(d) A second analyst quotes $\phi = 310^\circ$ for the same record. Are the two
analysts in conflict? Justify your answer.

---

## ★★★ Research-oriented

**★★★9.** A tide gauge has white measurement noise of standard deviation
$\sigma = 0.0200$ m, sampled hourly. The formal standard error of a fitted
constituent amplitude is

$$\sigma_A = \sigma\sqrt{\left[(A^{\mathsf T}A)^{-1}\right]_{11}
+ \left[(A^{\mathsf T}A)^{-1}\right]_{22}}$$

evaluated on the $(\cos,\sin)$ block of that constituent, where $A$ is the
design matrix with columns $1$, $\cos(\omega_i t)$ and $\sin(\omega_i t)$ for
each constituent $i$.

(a) Using the supplied script
[`code/fourier_series_demo.py`](../code/fourier_series_demo.py), obtain
$\sigma_A$ for K2 for records of 14, 20 and 30 days. Report the three numbers.
(b) Estimate the record length needed to bring $\sigma_A(\mathrm{K2})$ below
5 mm, and check your estimate against the script.
(c) Between 14 and 30 days the error falls by a factor of about 5. Between 182
and 365 days it falls by a factor of about 1.4. Explain both numbers in terms of
the Rayleigh criterion.
(d) K2 has an amplitude of 0.11 m at the synthetic station. At the record length
from (b), what fractional uncertainty does that represent? Is the K2 estimate
useful?

---

**★★★10.** Truncating the square-wave series produces the Gibbs overshoot, and
the script measures it:

| odd harmonics kept | overshoot as % of the jump |
|---|---|
| 9 | 9.116 |
| 25 | 8.974 |
| 99 | 8.951 |
| 199 | 8.949 |

(a) Estimate, from the table, the limiting overshoot as a fraction of the jump.
(b) Determine the smallest number of odd harmonics in the table (or a nearby
value you compute) whose overshoot is within $0.002$ percentage points of that
limit.
(c) The classical result is that the maximum of the partial sum tends to
$\frac{2}{\pi}\int_0^\pi \frac{\sin u}{u}\,du$, with
$\int_0^\pi \frac{\sin u}{u}\,du \approx 1.85193705$. Compute that maximum,
convert it to an overshoot as a fraction of the jump of 2, and compare with your
estimate from (a).
(d) Explain why the overshoot as a *fraction of the jump* is independent of the
number of terms in the limit, while the *width* of the overshoot region is not.
