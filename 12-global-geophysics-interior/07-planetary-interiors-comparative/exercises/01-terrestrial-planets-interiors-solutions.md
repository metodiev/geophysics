# Solutions — 12-07-01 Interiors of Mars, Venus, Mercury and the Moon

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [01 Interiors of Mars, Venus, Mercury and the Moon](../01-terrestrial-planets-interiors.md).

---

## ★1 — Uniform body

$$
M = \tfrac43\pi\rho R^{3}
= \tfrac43\pi(3500)(2.5\times10^{6})^{3}
= 2.2907\times10^{23}\ \mathrm{kg},
$$

$$
P_{c} = \tfrac23\pi G\rho^{2}R^{2}
= \tfrac23\pi(6.67430\times10^{-11})(3500)^{2}(2.5\times10^{6})^{2}
= 1.0702\times10^{10}\ \mathrm{Pa}.
$$

$$
\Pi = \frac{P_{c}R^{4}}{GM^{2}}
= \frac{(1.0702\times10^{10})(2.5\times10^{6})^{4}}
{(6.67430\times10^{-11})(2.2907\times10^{23})^{2}}
= 0.119366 .
$$

This is $3/(8\pi)$ exactly, to five digits: the identity is an algebraic
consequence of $P_{c} = \tfrac23\pi G\rho^{2}R^{2}$ and
$M = \tfrac43\pi\rho R^{3}$, not an approximation.

---

## ★2 — Scaling two bodies

$$
\frac{P_{c,2}}{P_{c,1}} = \left(\frac{M_{2}}{M_{1}}\right)^{2}
\left(\frac{R_{2}}{R_{1}}\right)^{-4}
= 2^{2}\times1.5^{-4} = \frac{4}{5.0625} = 0.7901 .
$$

The heavier body has the *lower* central pressure, because the radius grows faster
than the pressure does. Compression is governed by $P_{c}/K$ if the modulus is
similar, so the **smaller** body is the more compressed one — the counter-intuitive
scaling that makes "bigger means more compressed" a false rule of thumb.

---

## ★3 — Surface-to-volume ratio

$$
\left.\frac{S}{V}\right|_{1.8\times10^{6}} = \frac{3}{1.8\times10^{6}}
= 1.6667\times10^{-6}\ \mathrm{m^{-1}},
\qquad
\left.\frac{S}{V}\right|_{6.4\times10^{6}} = 4.6875\times10^{-7}\ \mathrm{m^{-1}},
$$

$$
\text{ratio} = \frac{1.6667\times10^{-6}}{4.6875\times10^{-7}} = 3.556 .
$$

For the same heat production per unit mass the smaller body loses heat about 3.6
times faster per unit mass: it cools and stiffens sooner. The statement holds
"all else equal", and all else — radiogenic inventory, insulation, tidal heating —
is generally *not* equal between two real bodies.

---

## ★4 — Core densities on the ridge

$$
\tfrac43\pi R^{3} = 1.1310\times10^{20}\ \mathrm{m^{3}},
\qquad
\rho_{\text{mean}} = \frac{4.0\times10^{23}}{1.1310\times10^{20}}
= 3.5368\times10^{3}\ \mathrm{kg\,m^{-3}},
$$

with $f_{c} = 0.30^{3} = 0.027$ and $f_{m} = 0.973$:

$$
\rho_{m} = \frac{3536.8}{0.973 + 0.027\times9.0515}
= \frac{3536.8}{1.21739} = 2905.2\ \mathrm{kg\,m^{-3}},
\qquad
\rho_{c} = 9.0515\times2905.2 = 2.6297\times10^{4}\ \mathrm{kg\,m^{-3}} .
$$

The demonstration prints $26296.6\ \mathrm{kg\,m^{-3}}$; the small difference is
rounding in the intermediate steps. The density contrast of 9 is large: for rocky
material, plausible contrasts are a few, so this row is at the edge of what
mineral physics permits, and rows with smaller $\alpha$ (larger cores) are more
comfortable. Once again the *physical* bound, not the data, does the narrowing.

---

## ★5 — The fluid Love number

$$
k_{f} = \frac{3J_{2}}{q} = 3\times0.4979 = 1.4937 .
$$

The exact small-rotation value is $1.5$, so the demonstration's solver is low by
$0.42\%$. This is **not** a solver error: the solver is run at the finite
$q = 4\times10^{-3}$, where the exact Maclaurin relation gives $J_{2}/q = 0.4968$
(lesson [01](../../06-geodesy-constraints-interior/01-moment-of-inertia.md), §5), i.e.
$k_{f} = 1.4904$. The residual against the exact finite-$q$ value is then
$0.2\%$, which is the solver's discretisation. The lesson: compare like with
like, and always state the $q$ at which a figure observable is evaluated.

---

## ★6 — Central pressure from $\Pi$

$$
P_{c} = \Pi\frac{GM^{2}}{R^{4}}
= 0.1888\times\frac{(6.67430\times10^{-11})(8.0\times10^{23})^{2}}
{(4.5\times10^{6})^{4}}
= 0.1888\times\frac{4.2716\times10^{37}}{4.1006\times10^{26}}
= 1.9667\times10^{10}\ \mathrm{Pa}.
$$

If instead the body were uniform, the same mass and radius would give

$$
P_{c}^{\text{uniform}} = \frac{3}{8\pi}\frac{GM^{2}}{R^{4}}
= 0.119366\times1.0417\times10^{11} = 1.2434\times10^{10}\ \mathrm{Pa},
$$

i.e. **36.8% lower**. The difference is not bookkeeping: it is the equation of
state. $\Pi = 0.1888$ says the mass is centrally concentrated; a uniform body of
the same $M$ and $R$ cannot be. So an inference of central pressure from mass and
radius alone carries an *assumption* about the density distribution, and the
assumption is worth tens of percent. That is why the comparison of two bodies
must fix the structure class before comparing $P_{c}$, and why $\Pi$ itself is
the quantity to compare.

## ★7 — Precision specification (no unique answer)

**What is available.** Along the ridge the four figure values span
$k_{f} = 0.9922$ (at $x = 0.20$) to $0.9607$ (at $x = 0.60$): a total range of
$0.0315$, or about 3.2% of $k_{f}$. A distinguishing measurement must therefore
resolve a fraction of that range, so $k_{f}$ needs about 1% accuracy to place
$x$ to better than half its range, and $C/MR^{2}$ needs comparable accuracy to
select the ridge in the first place.

**What that buys.** With $(C/MR^{2}, k_{f})$ both at 1%, the two-layer family is
determined to roughly the row spacing in the lesson's table, i.e. $\Delta x
\sim 0.05$ over the range considered. That is a real result.

**What remains.** The family is still assumed: two uniform layers plus the
homogeneity and hydrostaticity assumptions. A graded density profile or a
chemically distinct layer in the envelope is a different family and can fit the
same two numbers. The residual uncertainty is the *parameterisation*, and no
increase in precision removes it; only an independent observation (a seismic
discontinuity, or an equation of state that forbids a candidate layer) does.

---

## ★8 — The exact uniform-sphere relation, and condensation

Hydrostatic equilibrium with uniform density:

$$
\frac{\mathrm{d}P}{\mathrm{d}r} = -\rho\frac{GM(r)}{r^{2}},
\qquad
M(r) = \tfrac43\pi\rho r^{3}
\;\Longrightarrow\;
\frac{\mathrm{d}P}{\mathrm{d}r} = -\frac{4\pi G\rho^{2}}{3}r .
$$

Integrating inwards from $P(R) = 0$:

$$
P_{c} = \frac{4\pi G\rho^{2}}{3}\int_{0}^{R}r\,\mathrm{d}r
= \frac{2\pi G\rho^{2}R^{2}}{3}.
$$

Substituting $\rho = M/(\tfrac43\pi R^{3})$:

$$
P_{c} = \frac{2\pi G R^{2}}{3}\cdot\frac{M^{2}}{(\tfrac43\pi)^{2}R^{6}}
= \frac{2\pi}{3}\cdot\frac{9}{16\pi^{2}}\frac{GM^{2}}{R^{4}}
= \frac{3}{8\pi}\frac{GM^{2}}{R^{4}} .
$$

**Central condensation.** $\Pi = P_{c}R^{4}/(GM^{2})$ *rises* with central
condensation: the demonstration's table gives $0.1195$ for a uniform body,
$0.3927$ for $n = 1$, $0.7701$ for $n = 1.5$ and $11.05$ for $n = 3$. The reason
is that concentrating mass increases the gravitational field in the interior while
decreasing it in the outer parts, and the pressure is the integral of $\rho g$ —
both factors rise where the mass is. A compressible body therefore runs a much
higher central pressure for the same $M$ and $R$, which is why $\Pi$ is
diagnostic of the equation of state and not only of the mass distribution.
