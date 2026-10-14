# Solutions — 06-09-03 Velocity Analysis and Moveout Interpretation

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [03 Velocity Analysis](../03-velocity-analysis.md).

---

## ★1 — Moveout at 2 km

$$t = \sqrt{1.5^{2} + \left(\frac{2000}{2800}\right)^{2}}
= \sqrt{2.25 + 0.510204} = \sqrt{2.760204} = 1.661386\ \mathrm{s},$$
$$\Delta t = 0.161386\ \mathrm{s} = 161.4\ \mathrm{ms}.$$

---

## ★2 — Relative resolution widths

With $v = 2500\ \mathrm{m\,s^{-1}}$:

| max offset (m) | 90%-width (m/s) | relative width | printed |
|---|---|---|---|
| 800 | 350 | $350/2500 = 14.0\%$ | 14.0% |
| 1200 | 160 | $6.4\%$ | 6.4% |
| 1600 | 90 | $3.6\%$ | 3.6% |
| 2400 | 50 | $2.0\%$ | 2.0% |
| 3200 | 40 | $1.6\%$ | 1.6% |

The relative width is the number that can be quoted across surveys; the absolute
width is not.

---

## ★3 — Sensitivity of moveout to velocity

$$\Delta t(v) = \sqrt{t_0^{2} + \frac{x^{2}}{v^{2}}} - t_0
= t_0\left[\left(1+\frac{x^{2}}{v^{2}t_0^{2}}\right)^{1/2} - 1\right].$$

Differentiating with respect to $v$,

$$\frac{\partial \Delta t}{\partial v}
= t_0 \cdot \frac{1}{2}\left(1+\frac{x^{2}}{v^{2}t_0^{2}}\right)^{-1/2}
\cdot\left(-\frac{2x^{2}}{v^{3}t_0^{2}}\right)
= -\frac{x^{2}}{v^{3}t_0}\left(1+\frac{x^{2}}{v^{2}t_0^{2}}\right)^{-1/2}.$$

For small offset the bracket is $\approx1$ and

$$\frac{\partial \Delta t}{\partial v} \approx -\frac{x^{2}}{v^{3}t_0},$$

so the moveout's sensitivity to velocity **grows as $x^{2}$**: a two-fold longer
cable doubles the velocity-dependent part of the moveout four times over. In
inversion language, the semblance width is

$$\delta v \approx \frac{\delta t}{\left|\partial \Delta t/\partial v\right|}
\approx \frac{\delta t\,v^{3}t_0}{x^{2}},$$

so the velocity resolution improves as $1/x^{2}$ at small offset — the
quantitative form of "longer cables measure velocity better". At long offset the
bracket in the exact derivative is less than one, the sensitivity grows more
slowly than $x^{2}$, and the improvement flattens (see ★5).

---

## ★4 — Dip bias

For a planar dipping reflector the moveout is still hyperbolic, with

$$v_{\text{NMO}} = \frac{v}{\cos\theta},$$

so

$$v_{\text{true}} = v_{\text{NMO}}\cos\theta
= 3200 \times \cos 30^\circ = 3200 \times 0.866025
= 2771.3\ \mathrm{m\,s^{-1}}.$$

**Bias in velocity:** if the dip is ignored, $v_{\text{stack}}$ is
$3200\ \mathrm{m\,s^{-1}}$, which is

$$\frac{3200-2771.3}{2771.3} = +15.47\%$$

above the true value — exactly the demonstration's $15.47\%$ at $30^\circ$.

**Depth error.** Converting $t_0 = 1.8\ \mathrm{s}$ with a single velocity
($z = vt_0/2$):

$$z_{\text{stack}} = \frac{3200\times1.8}{2} = 2880\ \mathrm{m}, \qquad
z_{\text{true}} = \frac{2771.3\times1.8}{2} = 2494.2\ \mathrm{m},$$

an error of $+385.8\ \mathrm{m} = +15.5\%$. Ignoring dip biases the velocity and
the depth by the *same* factor, which is why the two errors are so often
mistaken for each other.

---

## ★5 — Measured exponents of the width–offset relation

$$e_{ij} = -\frac{\log(w_j/w_i)}{\log(x_j/x_i)}:$$

| offset pair (m) | width ratio | offset ratio | exponent |
|---|---|---|---|
| 800 → 1200 | 2.188 | 1.500 | 1.93 |
| 1200 → 1600 | 1.778 | 1.333 | 2.00 |
| 1600 → 2400 | 1.800 | 1.500 | 1.45 |
| 2400 → 3200 | 1.250 | 1.333 | 0.78 |

The near-offset rows reproduce the $x^{-2}$ prediction of ★3 (exponents $1.93$
and $2.00$); the far-offset rows do not ($1.45$ and $0.78$). The reason is in the
derivation: the bracket $\left(1+x^{2}/(v^{2}t_0^{2})\right)^{-1/2}$ departs from
one as the offset approaches and exceeds $vt_0$, so the sensitivity stops growing
as $x^{2}$ and the resolution stops improving as $x^{-2}$. Quoting the
$x^{-2}$ law beyond the range where the bracket is near one is an extrapolation,
not a result.

---

## ★6 — Can a 3.2 km cable reach 1%?

The target width is $1\%$ of $2500\ \mathrm{m\,s^{-1}} = 25\ \mathrm{m\,s^{-1}}$.
The table's best entry at $3200\ \mathrm{m}$ is $40\ \mathrm{m\,s^{-1}}$ ($1.6\%$).
**No tabulated cable length reaches $1\%$.**

Extrapolate with the measured far-offset exponent. Using the last measured pair
($2400 \to 3200\ \mathrm{m}$, exponent $0.78$):

$$x_{\text{needed}} = 3200 \times \left(\frac{40}{25}\right)^{1/0.78}
= 3200 \times 1.6^{1.282} = 3200 \times 1.827 = 5846\ \mathrm{m}.$$

Using the more optimistic mid-range exponent ($1.45$, the $1600 \to 2400$ pair):

$$x_{\text{needed}} = 3200 \times \left(\frac{40}{25}\right)^{1/1.45}
= 3200 \times 1.6^{0.690} = 3200 \times 1.383 = 4425\ \mathrm{m}.$$

So a cable of roughly $4.4$-$5.8\ \mathrm{km}$, i.e. $1.4$-$1.8\times$ the
tabulated maximum, is required. **The alternative is bandwidth:** the
bandwidth table shows the width falling with wavelet frequency ($170$, $90$,
$40$, $20\ \mathrm{m\,s^{-1}}$ for $12$, $20$, $30$, $45\ \mathrm{Hz}$), so
raising $f_0$ from $30$ to $45\ \mathrm{Hz}$ at $3.2\ \mathrm{km}$ gives
$20\ \mathrm{m\,s^{-1}} = 0.8\%$ — below the target with *no* cable change,
provided the data actually contain the higher frequencies. In practice the
choice is made on what the geology transmits: a $45\ \mathrm{Hz}$ wavelet is
unlikely to survive a deep, attenuating overburden.

**Also note the demonstration's own caveat:** at $60\ \mathrm{Hz}$ with
$dt = 2\ \mathrm{ms}$ the measured width *degrades* to
$540\ \mathrm{m\,s^{-1}}$, because the wavelet spans about three samples and the
NMO interpolation aliases. Any bandwidth extrapolation must state the sampling
interval.

---

## ★7 — QC procedure for the dip bias (specification)

**Observable.** The difference between the stacking velocity at a common
midpoint analysed (i) along the dip direction and (ii) along the strike
direction, and between the stacking velocity and the *migration* velocity that
best focuses the same event.

**Diagnostic threshold.** A systematic increase of $v_{\text{stack}}$ over
$v_{\text{mig}}$ of the order of the predicted
$1/\cos\theta - 1$ for the mapped dip. At $20^\circ$ that is $+6.4\%$ and at
$30^\circ$ $+15.5\%$ (the demonstration's table). Call the bias present if the
measured excess exceeds the velocity-analysis precision of ★2 — e.g. $3.6\%$ at
a $1.6\ \mathrm{km}$ cable — *and* correlates with the mapped dip.

**Confirming measurement.** Apply dip moveout (DMO) before velocity analysis and
repeat the pick: if the bias is the $1/\cos\theta$ factor, the DMO-corrected
velocity for a dipping event must agree with the strike-direction velocity for
the same reflector. An independent confirmation is a well tie or a
migration-velocity scan (lesson 04), which is sensitive to the velocity in a
different way.
