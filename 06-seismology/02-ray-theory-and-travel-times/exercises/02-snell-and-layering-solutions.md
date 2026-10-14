# Solutions — 06-02-02 Snell's Law, Layered Media and the Travel-Time Curve

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand; where a problem admits more than one defensible answer it is said so.

Lesson: [02 Snell's Law, Layered Media and the Travel-Time Curve](../02-snell-and-layering.md).

---

## ★1 — Critical angle

$$\sin i_c = \frac{v_1}{v_2} = \frac{5.60}{6.20} = 0.903226
\quad\Longrightarrow\quad i_c = 64.5854^\circ .$$

Because $v_1 < v_2$, $\sin i_c = 0.903226 < 1$: a real critical angle exists and
the head wave does exist.

---

## ★2 — Intercept time

$$\tau = 2h_1\frac{\cos i_c}{v_1}, \qquad
\cos i_c = \sqrt{1 - 0.903226^{2}} = 0.429166 .$$

$$\tau = 2(2.00)\frac{0.429166}{5.60} = 4.00 \times 0.076637 = 0.306547\ \mathrm{s}.$$

Units: $\mathrm{km}\times\mathrm{s\,km^{-1}} = \mathrm{s}$.

---

## ★3 — Crossover distance

Direct: $X/v_1$; head wave: $X/v_2 + \tau$. Setting them equal,

$$X = \frac{\tau}{v_1^{-1} - v_2^{-1}}
= \frac{0.306547}{0.178571 - 0.161290}
= \frac{0.306547}{0.017281} = 17.7388\ \mathrm{km}.$$

Closed form: $X = 2h_1\sqrt{(v_2+v_1)/(v_2-v_1)}
= 4.00\sqrt{11.80/0.60} = 4.00(4.434712) = 17.7388$ km. ✔

---

## ★4 — Interface 3 of the demonstration model, from scratch

1. $p = 1/v_3 = 1/7.00 = 0.142857\ \mathrm{s\,km^{-1}}$; here the interface is
   the top of the $8.00\ \mathrm{km\,s^{-1}}$ half space, so
   $p = 1/8.00 = 0.125000\ \mathrm{s\,km^{-1}}$.
2. Angles: $\sin\theta_i = p\,v_i$, so

| layer | $v$ (km s⁻¹) | $\sin\theta$ | $\theta$ (°) | $\cos\theta$ |
|---|---|---|---|---|
| 1 | 6.00 | 0.750000 | 48.5904 | 0.661438 |
| 2 | 6.50 | 0.812500 | 54.3409 | 0.582961 |
| 3 | 7.00 | 0.875000 | 61.0450 | 0.484123 |

3. One-way horizontal legs $h_i\tan\theta_i$: $5.00 \times 1.133893 = 5.6695$ km;
   $10.00 \times 1.393746 = 13.9375$ km; $10.00 \times 1.807392 = 18.0739$ km.
4. $X_c = 2(5.6695 + 13.9375 + 18.0739) = 75.3617$ km ✔ matches the demo.
5. $\tau = 2\sum h_i\cos\theta_i/v_i
   = 2[5.00(0.661438)/6.00 + 10.00(0.582961)/6.50 + 10.00(0.484123)/7.00]
   = 2[0.551198 + 0.896863 + 0.691604] = 2(2.139666) = 4.279331$ s ✔.

The two demonstrations of the same geometry — one from $\tan\theta$, one from
$\cos\theta$ — are consistent to every printed digit.

---

## ★5 — Which interfaces produce head waves

| interface | $v$ above (km s⁻¹) | $v$ below (km s⁻¹) | $\sin i_c = v_{\text{above}}/v_{\text{below}}$ | exists? |
|---|---|---|---|---|
| 1 (at 4.0 km) | 6.20 | 5.80 | 1.0690 | no — exceeds 1 |
| 2 (at 8.0 km) | 5.80 | 6.80 | 0.8529 | yes |

The criterion is $\sin i_c = v_{\text{above}}/v_{\text{below}} \le 1$, i.e. a
velocity *increase* with depth. Interface 1 sits above a slower medium, so it is
hidden and produces no arrival at any offset.

For interface 2, $p = 1/6.80 = 0.147059\ \mathrm{s\,km^{-1}}$:

$$\eta_1 = \sqrt{6.20^{-2} - 0.147059^{2}} = \sqrt{0.026015 - 0.021626}
= 0.066244,$$
$$\eta_2 = \sqrt{5.80^{-2} - 0.147059^{2}} = \sqrt{0.029727 - 0.021626}
= 0.090001,$$
$$\tau = 2(4.0)(0.066244) + 2(4.0)(0.090001) = 0.529952 + 0.720008
= 1.249962\ \mathrm{s},$$
$$X_c = 2\left[\frac{4.0(0.147059)}{0.066244} + \frac{4.0(0.147059)}{0.090001}\right]
= 2[8.879825 + 6.535860] = 30.8314\ \mathrm{km}.$$

Note that the hidden interface still contributes to the *intercept* of the branch
below it: $\eta_1$ uses the 6.20 layer, and nothing in the fit can tell an analyst
whether the 4.0 km between the two interfaces is one layer or two.

---

## ★6 — Reading a fitted branch

- **Slope.** $1/v = 1/6.95\ \mathrm{s\,km^{-1}}$, so the branch runs along a
  medium with $v = 6.95\ \mathrm{km\,s^{-1}}$. The slope measures the refractor's
  velocity, not the velocity at the receiver.
- **Intercept.** $\tau = 2\sum_{i<k} h_i\cos\theta_i/v_i$. With $p = 1/6.95$, the
  angles $\theta_i$ depend on the velocities above, and the thicknesses enter only
  as that weighted sum. One equation, $k-1$ unknowns.
- **What is needed.** The velocities of all shallower layers, from the slopes of
  the shallower branches (or from independent information such as a well or a
  borehole measurement).
- **Why it is one-directional.** Each branch supplies one velocity (its own) and
  one weighted thickness sum. Inverting interface $k$ therefore requires the
  velocities from interfaces $1$ to $k-1$; an error in the shallowest velocity
  biases every depth below it, while an error in a deep velocity affects nothing
  above.

---

## ★7 — What the depth target demands

From the run, the velocity error of $\sigma_v = 0.10\ \mathrm{km\,s^{-1}}$
moves the inverted depth by 0.584 km, giving a sensitivity of about
$5.84\ \mathrm{km}/(\mathrm{km\,s^{-1}})$. The thickness error contributes
$\sigma_h = 0.25$ km on its own. In quadrature:

$$\sigma_H = \sqrt{\sigma_h^{2} + \left(5.84\,\sigma_v\right)^{2}} .$$

A 0.10 km target needs *both* terms below 0.10 km:

- velocity term $\le 0.10$ km gives
  $\sigma_v \le 0.10/5.84 = 0.0171\ \mathrm{km\,s^{-1}}$, i.e. 0.29 % of
  $6.00\ \mathrm{km\,s^{-1}}$ — three times better than assumed;
- thickness term $\le 0.10$ km requires $\sigma_h \le 0.10$ km, 2.5 times better
  than assumed.

The **velocity term binds**: it is the one whose relative accuracy is hardest to
achieve and the one that scales with the depth itself. The survey-design
consequence is that effort spent measuring velocities (a longer array, reversed
shots, a borehole check) buys depth accuracy, while effort spent picking
thicknesses more precisely does not.

---

## ★8 — Designing the survey

- **Shallowest useful offset.** The interface-1 head wave (if $v$ above is 5.60)
  is first arrival beyond the crossover
  $X = 2h_1\sqrt{(v_2+v_1)/(v_2-v_1)}$ with $h_1 = 8.0$ km, $v_1 = 5.60$,
  $v_2 = 6.20\ \mathrm{km\,s^{-1}}$:
  $X = 16.0\sqrt{11.80/0.60} = 16.0(4.434712) = 70.955$ km. Only beyond about
  71 km does the branch from 8 km depth become the first arrival.
- **Longest correlatable offset.** Set by the signal-to-noise ratio and by
  interference from later reflections and from the deeper branch; in practice the
  array must be several times the crossover distance so that the branch's slope
  can be fitted over a long baseline.
- **Contradicting observable.** The interface does not exist if no straight branch
  of slope $1/6.20\ \mathrm{s\,km^{-1}}$ appears at offsets beyond 71 km, with
  zero amplitude at all offsets (as opposed to a branch with a small amplitude,
  which is a thin or gradational refractor).
- **Failure when the refractor is 1.5 km thick.** A 1.5 km thick layer under a
  5.60 layer produces a head-wave-like arrival only over a limited offset range;
  beyond the crossover with the next interface, and once the layer thickness is
  comparable to a wavelength, the "branch" becomes a curved transfer rather than a
  straight line, and the straight-line inversion returns a velocity and a depth
  that correspond to no single layer.
