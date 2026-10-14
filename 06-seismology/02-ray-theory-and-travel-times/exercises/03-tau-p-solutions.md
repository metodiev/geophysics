# Solutions — 06-02-03 The tau-p Transform and Intercept Time

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand; where a problem admits more than one defensible answer it is said so.

Lesson: [03 The tau-p Transform and Intercept Time](../03-tau-p.md).

---

## ★1 — Intercept time from one arrival

$$\tau = T - pX = 6.400 - (1.30\times10^{-4})(40.0\times10^{3})
= 6.400 - 5.200 = 1.200\ \mathrm{s}.$$

Units: $p$ is $\mathrm{s\,m^{-1}}$ and $X$ is m, so $pX$ is s; $\tau$ is a time.

Physically, $\tau$ is the time at zero offset of the plane wave that arrives at
offset $X$ with slowness $p$ — the intercept of the $(p, \tau)$ line on which this
arrival sits.

---

## ★2 — $\tau(p)$ for a single layer

$$\tau(p) = 2h\sqrt{v_1^{-2} - p^{2}}, \qquad 0 \le p \le 1/v_1 .$$

- $p = 0$: $\tau = 2(5.00)/6.00 = 1.666667$ s — the vertical two-way time.
- $p = 1/6.50 = 0.153846\ \mathrm{s\,km^{-1}}$:
  $\eta_1 = \sqrt{0.027778 - 0.023669} = 0.064104$, so
  $\tau = 10.00(0.064104) = 0.641026$ s — the **head-wave intercept time** of
  Lesson 02 — and
  $X = 2hp/\eta_1 = 1.538462/0.064104 = 24.000$ km — the **critical offset**.

So the two quantities Lesson 02 obtained by ray geometry are one evaluation of
$\tau(p)$ and its Benndorf derivative.

---

## ★3 — Verifying $\tau = T - pX$

$$pX = (1.858782\times10^{-4})(22.3288\times10^{3})
= 4.150437\ \mathrm{s},$$
$$\tau = 5.9421 - 4.150437 = 1.791663 \approx 1.7916\ \mathrm{s}.$$

The residual $6\times10^{-5}$ s is the rounding of the printed values to four
decimals ($T$ and $\tau$ are printed to $0.1$ ms, $p$ to six figures). Unit of
$pX$: $\mathrm{s\,m^{-1}}\times\mathrm{m} = \mathrm{s}$.

---

## ★4 — Benndorf's relation

Along a branch, $T$ depends on offset through $\mathrm{d}T/\mathrm{d}X = p$, so
$\mathrm{d}T = p\,\mathrm{d}X$ and

$$\mathrm{d}\tau = \mathrm{d}T - p\,\mathrm{d}X - X\,\mathrm{d}p
= p\,\mathrm{d}X - p\,\mathrm{d}X - X\,\mathrm{d}p
= -X\,\mathrm{d}p
\quad\Longrightarrow\quad
\frac{\mathrm{d}\tau}{\mathrm{d}p} = -X .$$

In words: differentiating the intercept function returns the offset. This is
exactly the defining property of a Legendre transform — the transform exchanges
the roles of a function and the derivative of its conjugate — so $T(X)$ and
$-\tau(p)$ carry the same information, related by
$T = \tau - p\,\mathrm{d}\tau/\mathrm{d}p$.

---

## ★5 — The noise scaling of the derivative

Prediction for a central difference of a quantity with noise $\sigma_T$ and
spacing $\mathrm{d}p$:

$$\sigma_X = \frac{\sigma_T}{\sqrt{2}\,\mathrm{d}p}
= \frac{0.010}{1.414214 \times 1.250\times10^{-6}}
= \frac{0.010}{1.767767\times10^{-6}} = 5656.9\ \mathrm{m}.$$

Measured: 4473.411 m mean, 5044.240 m worst — the prediction is an upper bound
consistent with the measurement to about 20 %.

For a 1.0 km target:

$$\mathrm{d}p = \frac{\sigma_T}{\sqrt{2}\,\sigma_X}
= \frac{0.010}{1.414214 \times 1000} = 7.071\times10^{-6}\ \mathrm{s\,m^{-1}}.$$

Note the direction of the trade: **coarser** spacing (larger $\mathrm{d}p$) is
what reduces the error. Refining the grid amplifies noise in inverse proportion.

---

## ★6 — The spherical ray parameter

$$p = \frac{r\sin i}{v} = \frac{6371 \times 0.5}{8.00}
= 398.1875\ \mathrm{s\,rad^{-1}}.$$

Conversion: multiply by $\pi/180$ to pass from $\mathrm{s\,rad^{-1}}$ to
$\mathrm{s\,deg^{-1}}$,

$$p = 398.1875 \times \frac{\pi}{180} = 6.949683\ \mathrm{s\,deg^{-1}},$$

so the factor is 0.0174533 $\mathrm{rad\,deg^{-1}}$ (equivalently, divide by
57.2958 $\mathrm{deg\,rad^{-1}}$).

---

## ★7 — Specifying an experiment for 0.5 km offsets

From the relation $\sigma_X = \sigma_T/(\sqrt{2}\,\mathrm{d}p)$, a 0.5 km target
requires

$$\mathrm{d}p = \frac{\sigma_T}{\sqrt{2}\,\sigma_X}
= \frac{0.010}{1.414214 \times 500} = 1.414\times10^{-5}\ \mathrm{s\,m^{-1}}$$

for $\sigma_T = 10$ ms. Across the slowness band used in the lesson,
$2\times10^{-4}\ \mathrm{s\,m^{-1}}$ wide, that is
$2\times10^{-4}/1.414\times10^{-5} \approx 14$ traces — a small, achievable
number.

Alternatively, with a 25-trace array ($\mathrm{d}p = 8\times10^{-6}\
\mathrm{s\,m^{-1}}$) the pick uncertainty must satisfy
$\sigma_T \le \sqrt{2}\,\mathrm{d}p\,\sigma_X = 1.414214 \times 8\times10^{-6}
\times 500 = 5.7$ ms.

**Which to invest in?** Improving picks is usually the better move, because both
the truncation error *and* the noise term scale with $\mathrm{d}p$, while a
better pick improves every arrival on every trace; but if the array cannot be laid
out more densely, the pick target of 5.7 ms is the specification that has to be
met. Note also the caveat: this assumes independent errors. A common-mode timing
error, or a mis-picked zero time, does not average down with more traces.

---

## ★8 — Detecting a fold before inverting

At a fold, $X(p)$ is not monotone, so $\tau(p)$ has a stationary point in
$\mathrm{d}\tau/\mathrm{d}p$; equivalently
$\mathrm{d}^{2}\tau/\mathrm{d}p^{2} = -\mathrm{d}X/\mathrm{d}p$ changes sign. On
one side of the fold the curve is concave (the normal branch), on the other it is
convex, and the two sides meet where $\mathrm{d}X/\mathrm{d}p = 0$ — the caustic,
where two branches are tangent in the $(\tau, p)$ plane.

**Diagnostic.** On a synthetic model: (i) compute $X(p)$ and $T(p)$ on a fine
$p$-grid; (ii) form $\tau = T - pX$ and its second derivative; (iii) look for a
sign change in $\mathrm{d}^{2}\tau/\mathrm{d}p^{2}$; and (iv) cross-check by
counting the roots of $X(p) = X^{\ast}$ at a few offsets, which must exceed one
inside the triplication range.

**Outcome that would show the diagnostic failed.** A second-derivative sign
change somewhere in the $p$-grid that does *not* coincide with any offset having
more than one arrival. That would indicate the sign change is numerical noise from
the differencing — the very effect quantified in Section 6 of the lesson — rather
than a physical fold, and the fix is to smooth $\tau(p)$ before differentiating
and to require the sign change to persist over a $p$ window wider than the noise
scale $\sigma_T/(\sqrt{2}\,\mathrm{d}p)$, expressed in offset units.
