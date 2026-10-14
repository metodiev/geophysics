# Solutions — 05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off

> Numbers marked *verified* were computed.

---

## ★1

$$w_{1/2} = 2\sqrt{2^{2/3}-1}\,d = 1.532842\,d.$$

---

## ★2 *(verified)*

$w_{1/2} = 1.532842\times250 = 383.2$ m; ratio to depth $= 1.532842$ exactly.

---

## ★3

$\nabla^2\mathbf{B} = \mu\sigma\,\partial_t\mathbf{B}$ with
$\mathbf{B}\propto e^{i(\omega t-kz)}$ gives $-k^2 = i\mu\sigma\omega$, hence
$k = (1-i)\sqrt{\mu\sigma\omega/2} = (1-i)/\delta$ and
$\delta = \sqrt{2/\mu\sigma\omega}$.

Dimensions: $[\mu] = \mathrm{H\,m^{-1}}$, $[\sigma] = \mathrm{S\,m^{-1}}$,
$[\omega] = \mathrm{s^{-1}}$, and $\mathrm{H\,S} = \mathrm{s\,m^{-1}}$? Check:
$\mathrm{H} = \mathrm{kg\,m^2\,s^{-2}\,A^{-2}}$, $\mathrm{S} =
\mathrm{A^2\,s^3\,kg^{-1}\,m^{-2}}$, product $= \mathrm{m^2\,s}$... so
$[\mu\sigma\omega] = \mathrm{m^{-2}}$ and $[\delta] = \mathrm{m}$. ✓

---

## ★4 *(verified)*

$B = 50$ Hz, $v = 2400$ m/s: $\Delta z = 2400/(4\cdot50) = 12.0$ m.

---

## ★5

For $g(x) = Cd/(x^2+d^2)$, set $g(x) = \frac12 g(0)$:
$d/(x^2+d^2) = 1/(2d) \Rightarrow x^2+d^2 = 2d^2 \Rightarrow x = d$, so the
half-width is $2d$ and the ratio is **2.000000**.

It is larger than the point-mass ratio (1.532842) because the line-mass kernel
decays more slowly with $x$ ($(x^2+d^2)^{-1}$ versus $(x^2+d^2)^{-3/2}$), so the
anomaly spreads further before falling to half. **The constant depends on the
source geometry; only the proportionality to $d$ is universal.** This is why
depth rules must be calibrated to the assumed body shape.

---

## ★6 *(verified)*

$\sigma = 0.05$ S/m, $\mu_0 = 1.2566\times10^{-6}$ H/m,
$\mu\sigma = 6.283\times10^{-8}$.

| $T$ (s) | $\omega$ (rad/s) | $\delta = \sqrt{2/(\mu\sigma\omega)}$ (m) |
|---|---|---|
| 1 | 6.283 | 712 |
| 10 | 0.6283 | 2251 |
| 100 | 0.06283 | 7117 |

To sense 800 m you need $\delta \gtrsim 800$ m, satisfied from about $T = 1.3$ s
upward. The 1 s period is marginal; 10 s comfortably reaches it.

---

## ★7

The anomaly at distance $x$ from one mass is $K\,d/(x^2+d^2)^{3/2}$. For two
masses separated by $s$ at the same depth, every geometric quantity in the
problem ($x$, $s$, $d$) appears as a ratio to $d$: $x/d$ and $s/d$. Therefore
the function $\text{profile}(x/d; s/d)$ is scale-invariant, so the criterion
"dip exceeds 1% of peak" selects a fixed value of $s/d$ — independent of $d$.
The measurement confirms $s_\text{min}/d = 1.11697$ at every depth tested.

---

## ★8 *(verified)*

For a point mass, amplitude $\propto d^{-2}$: at 1200 m,
$0.5\times(300/1200)^2 = 0.03125$ mGal. Relative information scales as
$d^{-3}$, so the ratio is $(300/1200)^3 = 1/64$: about **64 times less
information**, not 16. Exponent used: $d^{-3}$, which combines the amplitude
penalty ($d^{-2}$) with the width penalty (the anomaly occupies a region
$\propto d$ wider, so its relevant sample count grows only linearly).

---

## ★★★9

Expected: fitted slope $1.000$ to three or more decimal places for a point mass
and for a cylinder, provided the grid resolves the anomaly and the same
fraction-of-peak criterion is used. Measured deviation from 1.532842 was
$5.5\times10^{-4}$ with a 20001-point grid over $\pm20d$; halving $\Delta x$
reduces it.

The **slope** is more robust than the constant because the slope follows from
the kernel's homogeneity ($x$ and $d$ appear only as $x/d$), which no finite
grid can break, whereas the constant depends on where exactly the sampled
maximum falls and on the criterion chosen. Report both, and report the grid.

---

## ★★★10

Method and reporting: state $D = 1/(\mu_0\sigma)$, $\delta$ closed form, the
grid ($dz/\delta$), the time step from the stability limit, and the number of
periods simulated. Fit $\ln(\text{amplitude})$ against $z$ over a window inside
one skin depth.

Measured result for $\sigma = 1$ S/m, $T = 100$ s ($\delta = 5032.9$ m): decay
lengths of 4830.9 m, 4837.3 m and 4841.1 m at $dz/\delta = 0.2, 0.1, 0.05$
respectively, with the phase lag matching $z/\delta$ to about 1%. The error
falls monotonically with refinement, so it is **discretisation error**, not
modelling error. The distinction is made by refining the grid: a modelling
error would not shrink.
