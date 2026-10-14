# Solutions — 10-01-02 Velocity Estimation and Depth Conversion

> Read after attempting. Lesson:
> [02 Velocity Estimation and Depth Conversion](../02-gpr-velocity-and-depth.md).

---

## ★1 — Velocity and depth from a hyperbola fit

Slope $= 1/v^{2}$, so $v = 1/\sqrt{278.0} = 0.05998\ \mathrm{m\,ns^{-1}}$.

Intercept $= 4d^{2}/v^{2}$, so
$d = \frac{v\sqrt{t_0^{2}}}{2} = \frac{0.05998 \times 40.000}{2}
= 1.1996\ \mathrm{m} \approx 1.200\ \mathrm{m}$.

---

## ★2 — Air wave, ground wave

$t_{\mathrm{air}} = x/c = 0.25/0.299792458 = 0.834\ \mathrm{ns}$.

$t_{\mathrm{ground}} = 0.25/0.075 = 3.333\ \mathrm{ns}$.

Ratio $= 3.333/0.834 = 4.00 = \sqrt{\varepsilon_r}$, so
$\varepsilon_r = 16.0$ to the digits given — a direct permittivity measurement
from two arrival times.

---

## ★3 — Time-zero bias

$\delta d = (v/2)\,\delta t_0 = (0.075/2) \times 1.0
= 0.0375\ \mathrm{m} = 3.75\ \mathrm{cm}$, **too deep**.

---

## ★4 — Linear error propagation

$d = vt/2 \Rightarrow \partial d/\partial v = t/2$, so
$\delta d = (t/2)\delta v$ and
$\delta d/d = \delta v/v$ (no factor, no sign change).

Numerically: $d = 0.09 \times 60/2 = 2.700\ \mathrm{m}$,
$\delta d = (60/2)\times 0.005 = 0.150\ \mathrm{m}$,
and $0.150/2.700 = 0.0556 = 0.005/0.09$. Consistent.

---

## ★5 — Dix interval velocity

$$v_{2}^{2} = \frac{v_{\mathrm{nmo},2}^{2}t_{0,2}
- v_{\mathrm{nmo},1}^{2}t_{0,1}}{t_{0,2}-t_{0,1}}
= \frac{0.0740^{2}\times 66.7 - 0.0600^{2}\times 40.0}{66.7-40.0}
= \frac{0.3653 - 0.1440}{26.7} = 0.008287,$$

$v_2 = 0.0910\ \mathrm{m\,ns^{-1}}$.

Which pick dominates: the difference in the numerator ($0.2213$ of a total
$0.3653$, i.e. $61\%$) comes from the deeper event, but the denominator
$26.7\ \mathrm{ns}$ is also set by both. Perturbing $v_{\mathrm{nmo},2}$ by $+5\%$
changes the numerator by $+0.0365$ ($+16.5\%$ of it); perturbing
$t_{0,2}$ by $+5\%$ changes both terms and the denominator. The demonstration
shows the largest single amplification comes from the deeper event's NMO velocity
($+8.1\%$ for a $+5\%$ perturbation).

---

## ★6 — Exact two-layer times

At $x = 0$: the minimum is at $a = 0$ and

$$t = \frac{2h_1}{v_1} + \frac{2(d-h_1)}{v_2}
= \frac{2\times1.2}{0.060} + \frac{2\times1.2}{0.090} = 40.000 + 26.667
= 66.667\ \mathrm{ns}.$$

At $x = 3.0\ \mathrm{m}$: minimise
$t(a) = 2\sqrt{(a+1.5)^{2}+1.44}/0.060 + 2\sqrt{a^{2}+1.44}/0.090$.
The minimum lies at $a \approx -0.75\ \mathrm{m}$, i.e. **negative**: the ray
refracts on the transmitter side of the midpoint, shortening its path in the slow
layer. (Substituting $a = -0.75$: first term
$2\sqrt{0.5625+1.44}/0.060 = 2\times1.4158/0.060 = 47.19\ \mathrm{ns}$; second
term $2\sqrt{0.5625+1.44}/0.090 = 31.46\ \mathrm{ns}$; total
$78.65\ \mathrm{ns}$, against $a=0$: $2\sqrt{3.69}/0.060 + 26.667 = 63.99 +
26.67 = 90.65\ \mathrm{ns}$ — so the negative offset is indeed the minimum.)

---

## ★7 — Aperture and velocity precision

The curvature signal in $t^{2}$ vs $x^{2}$ is $x^{2}/v^{2}$, so over an aperture
$x_{\max}$ the signal scales as $x_{\max}^{2}$: from $1.0$ to $4.0\ \mathrm{m}$
that is a factor $16$. The picking noise enters $t^{2}$ as $2t\,\delta t$, growing
only as the time, so the velocity uncertainty falls by roughly the factor
$16$ in signal-to-noise — the demonstration measures this: the 0.9-of-peak
velocity width falls from $0.0750$ to $0.0020\ \mathrm{m\,ns^{-1}}$ (a factor
$37$) between $x_{\max} = 0.8\ \mathrm{m}$ and $4.0\ \mathrm{m}$.

---

## ★★★8 — Designing for a $2\%$ interval velocity

Requirement: $dv/v \le 0.02$ with $dt \approx 0.25\ \mathrm{ns}$ (a realistic
pick), from $dv = v^{3}t\,dt/x^{2}$:

$$x^{2} \ge \frac{v^{3}t\,dt}{0.02\,v}
= \frac{v^{2}t\,dt}{0.02}
= \frac{0.08^{2}\times t \times 0.25}{0.02}.$$

For a target at $2.5\ \mathrm{m}$, $t_0 = 2\times2.5/0.08 = 62.5\ \mathrm{ns}$;
at the far offset the time is larger, so take $t \approx 75\ \mathrm{ns}$:

$$x^{2} \ge \frac{0.0064\times 75\times0.25}{0.02} = 6.0\ \mathrm{m^{2}}
\Rightarrow x \ge 2.45\ \mathrm{m}.$$

So a maximum offset of about $2.5\ \mathrm{m}$ — one target depth — is the
minimum, and $3$–$4\ \mathrm{m}$ is comfortable. Offsets beyond that buy little,
because the hyperbolic approximation itself begins to fail.
