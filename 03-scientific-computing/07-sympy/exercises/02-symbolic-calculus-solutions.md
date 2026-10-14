# Solutions — 03-07-02 Symbolic Differentiation, Integration and Limits

> **Read this after attempting the exercises.** Values marked as measured are the
> demonstration's output, produced with sympy 1.14.0, NumPy 2.5.4 and
> SciPy 1.18.1 on Python 3.14.4.

---

## ★1 — Derivatives

(a) $12x^3 - 2$. (b) $e^{-ax}\left(k\cos kx - a\sin kx\right)$.
(c) $\dfrac{2x}{x^2 + a^2}$. (d) $\dfrac{2}{\sqrt{\pi}}e^{-x^2/4}\cdot\frac12
= \dfrac{e^{-x^2/4}}{\sqrt{\pi}}$.

Check (d) with `sp.diff(sp.erf(x/2), x)` — the chain rule factor of $\frac12$
combined with the $\frac{2}{\sqrt\pi}$ prefactor is exactly where a factor of 2 is
lost by hand.

---

## ★2 — Three integrals

(a) $\frac13$. (b) 1. (c) $\frac{\pi}{2}$.

The demonstration's measured quadrature agreements on comparable integrals:

```
  Gaussian tail (0, inf)   exact = sqrt(pi)/2 = 0.886226925452758
                           quad  = 0.886226925452758   |difference| = 1.110e-16
  arctan integral (0, 1)   exact = pi/4 = 0.785398163397448
                           quad  = 0.785398163397448   |difference| = 0.000e+00
```

---

## ★3 — Two limits

$$\lim_{x\to0}\frac{\sin x}{x} = 1, \qquad
\lim_{x\to0}\frac{e^x - 1 - x}{x^2} = \frac12.$$

By series: $\sin x/x = 1 - x^2/6 + O(x^4)$ and
$(e^x - 1 - x)/x^2 = \frac12 + \frac{x}{6} + O(x^2)$.

The second is the same structure as the demonstration's measured case:

```
  lim_(u->0) (1 - cos u)/u^2 = 1/2
  series form of the same ratio: 1/2 - u**2/24 + O(u^4)
      float evaluation at u = 1e-08: 0.000000000000000   relative error vs 1/2 = 1.000e+00
  cos(1e-8) in binary64: np.float64(1.0)  (so 1 - cos(1e-8) is exactly 0.0)
```

---

## ★4 — The two error terms of a central difference

Truncation: $\frac{h^2}{6}f'''(x)$, falling as $h^2$. Round-off: of order
$\epsilon|f|/h$, growing as $1/h$. The optimum balances them at
$h \approx (\epsilon|f|/|f'''|)^{1/3}$. Measured in the demonstration:

```
  best h in the scan: 1e-06 m, relative error 6.493e-12
```

with the truncation regime visible from $h = 2\times10^{-2}$ (relative error
`7.488e-04`) down to $h = 10^{-6}$ (`6.493e-12`) and round-off taking over by
$h = 10^{-8}$ (`8.898e-10`).

---

## ★5 — Ricker side lobe

Measured: the extrema are at $t = 0$ (value 1) and
$t = \pm\sqrt6/(2\pi f)$ (value $-2e^{-3/2}$):

```
      t = -sqrt(6)/(2*pi*f)  ->  w = -2*exp(-3/2) = -0.44626032
```

So the side lobe is **44.626 %** of the peak, inverting phase. In decibels,
$20\log_{10}(0.44626032) = -7.01$ dB.

---

## ★6 — Maximum horizontal gradient of a point mass

For $g_z = GMz/(x^2+z^2)^{3/2}$ at depth $z = d$, the horizontal derivative is
$F = \partial g_z/\partial x$, and $\partial F/\partial x = 0$ gives the extrema. The
classical result for the horizontal derivative's maximum is

$$x = \frac{d}{\sqrt{2}} \approx 0.7071\,d,$$

so for $d = 1000$ m the maximum horizontal gradient occurs at $x = 707.1$ m.
Symbolic solution of the stationarity condition returns $x = \pm d/\sqrt2$ and
$x = 0$; the last is the minimum of the derivative, not the maximum.

---

## ★7 — Verifying the flux against the heat equation

```python
T = T0 + dT * sp.erfc(z / (2 * sp.sqrt(kappa * t)))
residual = sp.simplify(sp.diff(T, t) - kappa * sp.diff(T, z, 2))
```

The residual simplifies to **0** for $\kappa > 0$, $t > 0$. Note that `dsolve`
cannot produce this solution from the heat equation as easily as it produces the
steady-state geotherm of the next lesson; the similarity solution is verified by
substitution, which is what the demonstration does for the flux:

```
  check against the closed form -dT exp(-z^2/(4 kappa t))/sqrt(pi kappa t): difference simplifies to 0
```

---

## ★8 — $\int_0^1 dx/(1+x^2)$

Exact: $\arctan 1 - \arctan 0 = \pi/4 = 0.7853981633974483$.

Measured against `quad`: `exact = pi/4 = 0.785398163397448`,
`quad = 0.785398163397448   |difference| = 0.000e+00`. The two agree bit for bit
here, so the difference is *below* the printed precision rather than exactly zero
— a subtlety worth stating: `0.000e+00` at 15 decimals means $<5\times10^{-16}$.

You would quote the exact value with a tolerance because the *inputs* are what
limit the claim, and because any consumer will compare it with a float.

---

## ★9 — Ricker extrema and side-lobe ratio

See ★5. The ratio is $2e^{-3/2} = 0.44626032$, i.e. 44.63 %, or −7.01 dB.

---

## ★10 — Laplacian of $V = -GM/r$

Measured:

```
  |grad V| - GM/(x^2+y^2+z^2) simplifies to: 0
  Laplacian of V, symbolic: 0
  number of operations in the Laplacian: 0
```

The identity holds on $\{(x,y,z) \ne 0\}$: the expression's domain excludes the
source, so "the Laplacian is zero" means zero everywhere the field is defined,
which is what harmonicity means.

---

## ★11 — A vertical cylinder

The kernel is $\dfrac{z-\zeta}{((x-\xi)^2+(y-\eta)^2+(z-\zeta)^2)^{3/2}}$
integrated over a disc in $(\xi,\eta)$ and $[z_1,z_2]$ in $\zeta$. In cylindrical
coordinates the angular integral is elementary and the radial one gives closed-form
terms; SymPy can complete the $\zeta$ integral and leave the radial one to be
tabulated.

For a survey of 10 000 stations: **use the closed form** if it exists, and a
numerical double integral only as the verification, because 10 000 stations times a
2-D quadrature is 10 000 quadratures. The decision is arithmetic on the evaluation
count, exactly as in the lesson's §10.3.

---

## ★12 — The finite-difference optimum

Measured table (relative error 7.488e-04 at $h = 2\times10^{-2}$ down to
`6.493e-12` at $h = 10^{-6}$, then rising to `8.898e-10` at $h = 10^{-8}$) gives
a truncation-regime exponent near 2: the ratio between $h = 0.02$ and $h = 0.005$
errors is $7.488\times10^{-4}/4.683\times10^{-5} = 15.99$, against
$(0.02/0.005)^2 = 16$ — a match to 0.1 %.

The classical estimate $h_{\text{opt}} \approx (\epsilon|f|/|f'''|)^{1/3}$ with
$\epsilon = 2.22\times10^{-16}$, $|f| = 26.75$ and a third derivative of order
$10^3$ gives $h_{\text{opt}}$ of order $10^{-6}$ m, agreeing with the measured
optimum. The comparison fails in the sense that the constant in the estimate is
not universal; the *scaling* is what transfers.
