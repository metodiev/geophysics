# Solutions — 09-02-03 Apparent Resistivity and Geometric Factors

> **Read after attempting the exercises.** Lesson:
> [03 Apparent Resistivity and Geometric Factors](../03-apparent-resistivity.md).

---

## ★1 — Limits

$$\lim_{a\to0}\rho_a = \rho_1 = 150\ \Omega\,\mathrm{m}, \qquad
\lim_{a\to\infty}\rho_a = \rho_2 = 30\ \Omega\,\mathrm{m}.$$

At intermediate spacings $\rho_a$ is a weighted average between them, decreasing
monotonically with $a$ for a conductive basement.

---

## ★2 — Voltage

$k = 2\pi a = 188.50$ m:

$$\Delta V = \frac{\rho_a I}{k} = \frac{45\times0.2}{188.50}
= 0.04775\ \mathrm{V} = 47.7\ \mathrm{mV}.$$

---

## ★3 — Transverse resistance and conductance

$$T = h\rho = 3\times400 = 1200\ \Omega\,\mathrm{m^{2}}, \qquad
S = \frac{h}{\rho} = \frac{3}{400} = 7.5\times10^{-3}\ \mathrm{S}.$$

Note $T S = 1$? No: $T=h\rho$ and $S=h/\rho$ give $TS = h^{2}$, so
$1200\times7.5\times10^{-3} = 9.0\ \mathrm{m^{2}} = h^{2}$ ✔ (a useful
consistency check).

---

## ★4 — An equivalence family for $T$ fixed

Members of $\{\rho = T/h\}$:

| $h$ (m) | 1 | 3 | 6 | 12 |
|---|---|---|---|---|
| $\rho$ ($\Omega\,\mathrm{m}$) | 1200 | 400 | 200 | 100 |

From the lesson's demonstration, a factor 16 in $h$ (and 16 in $\rho$) produced
a maximum deviation of 4.0% (at $h_2 = 8$ m) and 14.0% (at $h_2 = 16$ m) at 2%
noise. So the range admitted **at 2% noise** is roughly $h$ from 1 to about 8 m
for this $T$ — a factor 8 — with the endpoints determined by whichever
thickness first exceeds $\chi^{2} = 1$.

---

## ★5 — Halfway point of the conductive curve

Halfway in log space between 100 and 10 is $10^{1.5} = 31.6\
\Omega\,\mathrm{m}$. Interpolating the table (12 m: 81.85, 20 m: 66.93, 30 m:
58.95, 50 m: 55.63, 200 m: 55.02): the value 31.6 is never reached — the curve
approaches 55 $\Omega\,\mathrm{m}$ at $a = 200$ m and is still falling. So the
asymptote itself is not reached within the measured range, and the "halfway"
question has no answer: **a conductive half-space with a 10:1 contrast is
approached far more slowly than a resistive one**, because the current is
attracted *into* the conductor and the array must grow very large before the
current is dominated by it. This asymmetry (resistive asymptotes are approached
quickly, conductive ones slowly) is a well-known practical asymmetry of the
method.

---

## ★6 — The geometric-mean rule

Rule of thumb: $\rho_a(a = h_1) = \sqrt{\rho_1\rho_2}$ gives
$\sqrt{100\times1000} = 316.2\ \Omega\,\mathrm{m}$.

From the lesson's table, $\rho_a$ reaches 316.2 at about $a = 75$ m (201 at
30 m, 266 at 50 m, 333 at 80 m), **not** at $a = h_1 = 10$ m, where the model
gives 120.3 $\Omega\,\mathrm{m}$.

So the rule overestimates the depth of investigation by a factor ~7.5 for this
contrast, or equivalently underestimates the spacing needed to sense the
half-space. The reliable procedure is to compute the forward model for candidate
models (as the demonstration does) and to invert, not to use a nomogram.

---

## ★7 — Small-spacing behaviour

The limit cannot be obtained by a short argument because the two-layer solution
is a Bessel integral, not an elementary function. What *can* be done: fit the
exponent numerically from the tabulated data. Take the resistive case
$\rho_2 = 1000\ \Omega\,\mathrm{m}$, $h_1 = 10$ m, and define
$y(a) = \rho_a(a)-\rho_1$:

- $a = 0.5$: $y = 0.00$ (below the printed precision)
- $a = 2$: $y = 0.27$
- $a = 5$: $y = 3.62$
- $a = 8$: $y = 11.67$

A log-log fit of $y$ against $a$ over the three non-degenerate points
($a = 2,5,8$; $y = 0.27,3.62,11.67$) gives a slope of about

$$\frac{\ln(11.67/0.27)}{\ln(8/2)} = \frac{3.766}{1.386} = 2.72.$$

So $\rho_a - \rho_1$ grows roughly as $a^{2.7}$ in this range — steeper than
the naïve $(a/h)^{2}$ guess, because the array's sensitivity grows with its
aperture as well as with the depth reached. The lesson's point stands: the
approach to the first-layer asymptote is a power law whose exponent must be
measured, not assumed.

---

## ★8 — Programme for $T$ and depth

1. **Spacings:** at least eight, geometrically spaced from $0.2h$ to $20h$, so
   the curve's rising limb, minimum and asymptote are all sampled.
2. **$T$:** the equivalence means only $T = h\rho$ is measurable; fit $T$ by
   requiring the curve's *amplitude* of deviation from the host resistivity to
   match. Expected precision: with 2% noise on $\Delta V$, $T$ is determined to
   roughly the noise level divided by the sensitivity of the deviation to $T$,
   empirically a few per cent for a thin layer.
3. **Depth:** determined by *where* the deviation occurs (the crossover
   spacing), which is controlled by $h$ alone and is therefore better
   determined than $\rho$ — the lesson's family shows that $h$ changes by
   factors with the same $T$ but shifts the crossover by a much smaller amount.
4. **What remains unresolved:** the pair $(\rho, h)$ individually. The programme
   must report $T$ and a *bound* on $h$ (equivalently on $\rho$), plus the
   covariance from an inversion, and state that any single $(\rho, h)$ pair is a
   choice within that bound.
