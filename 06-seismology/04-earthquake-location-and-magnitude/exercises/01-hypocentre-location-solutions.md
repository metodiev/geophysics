# Solutions — 06-04-01 Hypocentre Location: Arrival Times, Inversions and Error Ellipses

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand.

Lesson: [01 Hypocentre Location](../01-hypocentre-location.md).

---

## ★1 — One Jacobian row

$$
d = \sqrt{42^{2} + 60^{2} + 7.5^{2}}\ \mathrm{km}
= \sqrt{1764 + 3600 + 56.25} = \sqrt{5420.25} = 73.622\ \mathrm{km}.
$$

$$
\frac{\partial T}{\partial x}
= -\frac{\xi - x}{v\,d} = \frac{42\,000}{6000\times73\,622}
= 9.508\times10^{-5}\ \mathrm{s\,m^{-1}},
\qquad
\frac{\partial T}{\partial z} = \frac{7500}{6000\times73\,622}
= 1.698\times10^{-5}\ \mathrm{s\,m^{-1}}.
$$

Both are slowness-like quantities: seconds per metre.

---

## ★2 — The origin-time derivative

$T_i^{\text{pred}} = T_i(\mathbf{m}) + t_0$, and $t_0$ enters additively, so
$\partial T_i^{\text{pred}}/\partial t_0 = 1$ for every station. The unit is
dimensionless: seconds per second.

---

## ★3 — Rank of a single station

With one arrival the Jacobian is a single row with four entries, so its rank is
at most 1 and three parameter directions are unconstrained. Physically, that one
time can be matched by any point along the ray to the station by adjusting
$t_0$, so the data fix a family rather than a point.

---

## ★4 — Marginal versus principal

$$
1.96\sqrt{C_{zz}} = 1.96\times466.4 = 914.0\ \mathrm{m}.
$$

The joint 95 per cent ellipsoid uses $\chi^{2}_{4}(0.95) = 9.4877$ and its
semi-axes are $\sqrt{9.4877\lambda_k}$ with $\lambda_k$ the eigenvalues of $C$.
The largest eigenvalue is inflated by the correlation between the horizontal
coordinates and depth, so its semi-axis ($1488.2\ \mathrm{m}$) exceeds every
marginal value: a marginal interval pretends the other three parameters are
known, while a principal semi-axis allows them to move.

---

## ★5 — Two-parameter trade-off

| $z$ (km) | $T(z)$ (s) | $t_0$ to keep $T = 5.050$ s |
|---|---|---|
| 2.0 | 5.011 | $+0.039$ |
| 5.0 | 5.069 | $-0.019$ |
| 10.0 | 5.270 | $-0.220$ |
| 15.0 | 5.590 | $-0.540$ |
| 20.0 | 6.009 | $-0.959$ |

A 0.05 s error in $t_0$ is crossed between $z = 2$ and $z = 5$ km, i.e. a
**0.05 s timing error trades for roughly 3 km of depth** at this distance. This
is the exact trade-off that makes depth unresolvable from one station.

---

## ★6 — A tight array

A cosine of 0.9998 means the two columns differ by an angle of about 1.1°, so a
0.05 s change in origin time can be traded for a depth change at roughly the
$1/\sin\theta \approx 50$-fold rate. Qualitatively the inversion becomes an
extreme deconvolution, and the condition number of $J^{T}J$ is infinite because
the rank is 3: there is a direction (a combination of station positions and the
two parameters) along which the data are *exactly* insensitive.

---

## ★7 — A depth-resolving network

Take 8 stations at epicentral distances of 20, 40, 60, 80, 100, 120, 140 and
160 km, all along a line through the epicentre so that the ray angles vary as
widely as possible. For a homogeneous half-space,
$\partial T/\partial z = z/(v r)$ with $r = \sqrt{\Delta^{2} + z^{2}}$, which is
largest at small $\Delta$; spreading the distances over a factor of eight makes
the column vary strongly, which lowers the cosine with the constant column
$t_0$. The design fails in reality if the network is far from the event
(no near station means no depth sensitivity), if picks at large distances are
systematically late because the model is wrong, or if the phase changes along
the profile (Pn beyond the cross-over distance).

---

## ★8 — A local minimum

Put every station on one side of the source and start the iteration at a
shallower hypocentre. The depth and origin time then trade along the
near-null direction, and Gauss-Newton can stop where the gradient vanishes
without reaching the true depth. The observable symptom is a *small* residual
with a *large* discrepancy from an independently known depth (for example a
comparison with a quarry blast or a known focal depth), together with a long
principal semi-axis pointing along the trade-off direction.
