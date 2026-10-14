# Solutions — 01-05-04 Taylor Series, Linearisation and Small-Angle Approximations

> **Read this after attempting the exercises, not before.** All numerical values
> were computed; the expansions are derived rather than quoted.

---

## ★1 — Maclaurin series and radii

**(a)** $e^{-x} = 1 - x + \dfrac{x^{2}}{2} - \dfrac{x^{3}}{6} + \cdots$, radius
$R = \infty$ (the exponential is entire: no singularity anywhere in the finite
plane).

**(b)** Substitute $2x$ into $\cos y = 1 - y^{2}/2! + y^{4}/4! - y^{6}/6! + \cdots$:

$$\cos(2x) = 1 - 2x^{2} + \frac{16x^{4}}{24} - \frac{64x^{6}}{720} + \cdots
= 1 - 2x^{2} + \frac{2}{3}x^{4} - \frac{4}{45}x^{6} + \cdots, \qquad R = \infty .$$

**(c)** $\ln(1+x) = x - \dfrac{x^{2}}{2} + \dfrac{x^{3}}{3} - \dfrac{x^{4}}{4} + \cdots$,
radius $R = 1$. The singularity of $\ln(1+x)$ is at $x = -1$, at the boundary of the
disc.

**(d)** Geometric: $(1+x)^{-1} = 1 - x + x^{2} - x^{3} + \cdots$, radius $R = 1$,
singular at $x = -1$.

---

## ★2 — Two linearisations with bounds

**(i)** $f(x) = \sqrt{1+x}$, $f(0) = 1$, $f'(x) = \frac{1}{2}(1+x)^{-1/2}$,
$f'(0) = \frac12$, so the linearisation is $1 + x/2$ and at $x = 0.02$:

$$\sqrt{1.02} \approx 1 + 0.01 = 1.01, \qquad \text{exact } = 1.0099504938362078 .$$

True error: $4.95\times10^{-5}$.

Bound: $\lvert R_1\rvert = \left\lvert\frac{f''(\xi)}{2}x^{2}\right\rvert$ with
$f''(x) = -\frac14(1+x)^{-3/2}$, whose magnitude is largest at $x=0$:
$\lvert f''\rvert \le 0.25$. Hence

$$\lvert R_1\rvert \le \frac{0.25}{2}(0.02)^{2} = 5.0\times10^{-5} .$$

The bound is $5.0\times10^{-5}$ against a true error of $4.95\times10^{-5}$ — tight
to 1 %.

**(ii)** $\sin x \approx x$, so $\sin(0.05) \approx 0.05$; exact
$= 0.04997916927067833$. True error: $2.083\times10^{-5}$.

Bound: the first omitted term is $x^{3}/3!$ with remainder
$R_3 = \dfrac{f^{(4)}(\xi)}{4!}x^{4}$, but for an alternating series the *first
omitted term* already bounds the error: $\frac{0.05^{3}}{6} = 2.0833\times10^{-5}$,
matching the true error to four figures.

**Reading.** Two lectures' worth of theory in two lines: the Lagrange remainder is an
exact statement about an unknown point $\xi$, and it converts into a usable bound by
maximising the derivative on the interval.

---

## ★3 — Thresholds for 1 % error

| Approximation | Relative error | $\theta$ or $x$ for 1 % |
|---|---|---|
| $\sin\theta \approx \theta$ | $\theta^{2}/6$ | $\theta = \sqrt{6\times10^{-2}} = 0.245$ rad $= 14.0°$ |
| $\cos\theta \approx 1-\theta^{2}/2$ | $\theta^{4}/24$ | $\theta = (24\times10^{-2})^{1/4} = 0.699$ rad $= 40.1°$ |
| $e^{-x} \approx 1-x$ | $x^{2}/2$ | $x = \sqrt{2\times10^{-2}} = 0.141$ |
| $(1+u)^{-2} \approx 1-2u$ | $3u^{2}$ | $u = \sqrt{10^{-2}/3} = 0.0577$ |

The third row is a good reminder that $e^{-x} \approx 1-x$ is the *worst* of the four
approximations in its range: it fails at $x = 0.141$, whereas the same expansion
carried to order $x^{2}$ is accurate to 0.1 % over the same interval.

The $\cos$ threshold is much larger than for $\sin$ because the leading error is
$\theta^{4}$ rather than $\theta^{2}$: for the second-order approximation to $\cos$,
accuracy improves twice as fast in the exponent. (The cruder $\cos\theta \approx 1$
has relative error $\theta^{2}/2$ and fails at $\theta = \sqrt{2\times10^{-2}} = 0.141$
rad $= 8.1°$.)

---

## ★★4 — Data precision versus model perturbation

**(a)** From $\delta g/g = 2\delta d/d$ (the linearised sensitivity), a relative data
precision of $10^{-3}$ corresponds to

$$\frac{\delta d}{d} = \frac{10^{-3}}{2} = 5\times10^{-4}
\;\Longrightarrow\; \delta d = 0.25\ \mathrm{m} \text{ at } d = 500\ \mathrm{m}.$$

**(b)** For a perturbation $u$, the linearisation error is $3u^{2}$. Setting
$3u^{2} = 10^{-3}$ gives $u = \sqrt{3.33\times10^{-4}} = 0.0183$, i.e.
$\delta d \approx 9.1$ m at $d = 500$ m.

**(c)** The two numbers differ by a factor of about 36, and the *smaller* one is the
model perturbation. A linearised inversion using $u = 0.05$ makes a
$3u^{2} = 7.5\times10^{-3}$ error — **7.5 times the data precision**, so the
linearisation error dominates and the fine data precision is wasted. A perturbation
of 1.8 % is the largest the linearisation supports at this precision.

The sentence: **the validity of a linearisation is limited by the size of the model
perturbation, not by the precision of the data.** Buying a better instrument does not
extend the range over which a linearisation is honest; it makes the failure more
visible.

---

## ★★5 — Travel-time perturbation

**(a)** With $v(s) = v_0 + \alpha s = v_0(1 + \alpha s/v_0)$,

$$t = \int_0^{L}\frac{ds}{v_0\left(1+\frac{\alpha s}{v_0}\right)}
= \frac{1}{v_0}\int_0^{L}\left(1 - \frac{\alpha s}{v_0} + \left(\frac{\alpha s}{v_0}\right)^{2} - \cdots\right)ds .$$

**(b)** To first order,

$$t \approx \frac{L}{v_0} - \frac{\alpha L^{2}}{2v_0^{2}}
= \frac{L}{v_0}\left(1 - \frac{\alpha L}{2v_0}\right).$$

The correction is $\dfrac{\alpha L^{2}}{2v_0^{2}}$, and it is *negative*: a faster
medium along the path reduces the travel time, as it must.

**(c)** The expansion parameter is $\varepsilon = \dfrac{\alpha L}{v_0}$: the fractional
speed change along the whole path. The first-order result is accurate to 1 % when the
neglected term, of order $\varepsilon^{2}$, is below $10^{-2}$, i.e.
$\varepsilon < 0.1$. Note the assumption that the path is straight: this is a
travel-time perturbation, not a ray-perturbation, and converting it into an
inversion requires a linearised ray-bending term as well. That is the step taken in
tomographic formulations, and it is the reason first-order tomography is stated as an
integral along the *reference* ray.

---

## ★★★6 — The $x^{4}$ term and the 1 % offset

**(a)** With $u = (x/(vt_0))^{2}$ and
$\sqrt{1+u} = 1 + \frac{u}{2} - \frac{u^{2}}{8} + \cdots$,

$$t(x) = t_0\left(1 + \frac{u}{2} - \frac{u^{2}}{8} + \cdots\right)
= t_0 + \frac{x^{2}}{2v^{2}t_0} - \frac{x^{4}}{8v^{4}t_0^{3}} + \cdots .$$

**(b)** The *relative* error of the parabolic truncation is approximately
$(u^{2}/8)/\sqrt{1+u}$, whose leading term is $u^{2}/8$. Setting $u^{2}/8 = 10^{-2}$:

$$u = \sqrt{0.08} = 0.2828
\;\Longrightarrow\;
x = vt_0\sqrt u = 2000\times0.5318 = 1063.7\ \mathrm{m}.$$

**(c)** The lesson's table gives a relative error of `6.231e-03` at $x = 1000$ m and
`1.0217e-02` at $x = 1150$ m (both computed directly from the exact hyperbola), so
the 1 % crossover lies between them — the prediction $x = 1064$ m is inside that
bracket. The table's $x = 1000$ m entry is slightly *better* than the leading-term
estimate because the next term in the series, $-u^{3}/16$, partially cancels the
$u^{2}/8$ term at $u = 0.25$.

**(d)** The 1 % condition depends on $u = (x/(vt_0))^{2}$, so the critical offset
scales with the product $vt_0$. That product has units of length and is exactly twice
the reflector depth, since $t_0 = 2h/v$ gives $vt_0 = 2h$. **Small-offset means
"offset small compared with reflector depth"** — the dimensionless quantity is
$x/h$, not $x$ alone and not $v$ or $t_0$ separately. A 2 km-offset survey over a 500
m reflector is a wide-angle survey; the same offsets over a 5 km reflector are not.

---

## ★★★7 — Thermal expansion

**(a)** Take the linear relation to be the first-order truncation of an exponential
equation of state, a common idealisation for a narrow temperature range: if
$\rho(T) = \rho_0\exp[-\alpha(T-T_0)]$, then

$$\rho = \rho_0\left(1 - \alpha\Delta T + \frac{\alpha^{2}\Delta T^{2}}{2} - \cdots\right),
\qquad \Delta T = T - T_0 .$$

With $\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$ and $\Delta T = 100$ K, the
dimensionless expansion parameter is $\alpha\Delta T = 3\times10^{-3}$, so the
second-order term is smaller than the first by a factor $\alpha\Delta T/2 = 1.5\times10^{-3}$.

**(b)** First order: $\Delta\rho = -\rho_0\alpha\Delta T
= -2700\times3\times10^{-5}\times100 = -8.10\ \mathrm{kg\,m^{-3}}$.

Second order: $\Delta\rho = -8.10 + 2700\times(3\times10^{-5})^{2}\times10^{4}/2
= -8.10 + 0.01215\ \mathrm{kg\,m^{-3}}$.

So the second-order correction is $+0.0122\ \mathrm{kg\,m^{-3}}$, i.e. a relative
change of $1.5\times10^{-3}$ in the density change itself and
$4.5\times10^{-6}$ in the density. Negligible at this temperature range.

**(c)** Two independent physical failures, well before 1000 K:

1. **Phase changes.** Rock that melts, or minerals that transform (quartz → coesite,
   olivine → wadsleyite), do not follow any smooth equation of state across the
   transition; the density jumps rather than drifting.
2. **The coefficient itself varies.** $\alpha$ is not a constant: it depends on
   temperature (and pressure), typically increasing with $T$; over 1000 K the change
   in $\alpha$ is comparable to $\alpha$ itself, so the linear relation is not even a
   good local model.
3. **Pressure effects.** Thermal expansion at depth is partially offset by
   compression; a relation in $T$ alone ignores the pressure dependence.

The numerical point stands: the *arithmetic* of a second-order truncation is fine at
100 K, and the failure at 1000 K is a failure of the model, not of the expansion.

---

## Extension notes

- **$\tan x$ series.** Dividing the series gives
  $\tan x = x + x^{3}/3 + 2x^{5}/15 + \cdots$, so the relative error of
  $\tan x \approx x$ is $x^{2}/3$, matching the threshold
  $\sqrt{3\varepsilon} = 2.58\times10^{-8}$ used in the previous lesson's exercise.
- **Radii check.** For $\ln(1+x)$ the coefficients are $a_k = (-1)^{k+1}/k$, giving
  $\lvert a_{k+1}/a_k\rvert = k/(k+1) \to 1$, so $R = 1$; for $(1+x)^{-1}$ all
  coefficients have modulus 1 and $R = 1$. The ratio test is decisive for both,
  although it says nothing about the endpoints, which need the alternating or
  harmonic arguments of [01-05-07](../07-sequences-and-series.md).
