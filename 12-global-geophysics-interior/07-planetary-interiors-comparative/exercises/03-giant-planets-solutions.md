# Solutions — 12-07-03 Giant Planet Interiors and Magnetic Fields

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [03 Giant Planet Interiors and Magnetic Fields](../03-giant-planets.md).

---

## ★1 — The $n = 1$ solution

The Lane-Emden equation for $n = 1$ is

$$
\theta'' + \frac{2}{\xi}\theta' + \theta = 0 .
$$

With $\theta = \sin\xi/\xi$:

$$
\theta' = \frac{\xi\cos\xi - \sin\xi}{\xi^{2}},
\qquad
\theta'' = \frac{-\xi^{2}\sin\xi - 2\xi\cos\xi + 2\sin\xi}{\xi^{3}} .
$$

Substituting:

$$
\theta'' + \frac{2}{\xi}\theta' + \theta
= \frac{-\xi^{2}\sin\xi - 2\xi\cos\xi + 2\sin\xi}{\xi^{3}}
+ \frac{2\xi\cos\xi - 2\sin\xi}{\xi^{3}}
+ \frac{\xi^{2}\sin\xi}{\xi^{3}} = 0 .\ \checkmark
$$

The boundary conditions hold because $\sin\xi/\xi\to1$ and its derivative
$\to0$ as $\xi\to0$ (both are the leading terms of the expansions
$\sin\xi = \xi - \xi^{3}/6 + \dots$). The first zero is at $\xi_{1} = \pi$, where
$\sin\xi = 0$ and the function is regular. The dimensionless mass is

$$
\omega_{1} = -\xi_{1}^{2}\theta'(\xi_{1}) = -\pi^{2}\times\frac{\pi\cos\pi - \sin\pi}{\pi^{2}}
= -\pi^{2}\times\frac{-\pi}{\pi^{2}} = \pi ,
$$

matching the demonstration's $3.141593$ to seven digits.

---

## ★2 — Radius and mass for $n = 1$

$$
\alpha^{2} = \frac{(n+1)K\rho_{c}^{1/n-1}}{4\pi G}
= \frac{2\times10^{7}\times\rho_{c}^{0}}{4\pi(6.67430\times10^{-11})}
= \frac{2\times10^{7}}{8.3860\times10^{-10}} = 2.3850\times10^{16},
$$

$$
\alpha = 1.5442\times10^{8}\ \mathrm{m},
\qquad
R = \alpha\xi_{1} = 1.5442\times10^{8}\times3.14159
= 4.8513\times10^{8}\ \mathrm{m},
$$

$$
M = 4\pi\rho_{c}\alpha^{3}\omega_{1}
= 4\pi(10^{4})(1.5442\times10^{8})^{3}(\pi)
= 1.4537\times10^{30}\ \mathrm{kg}.
$$

The mass is absurd as a planet — $\rho_{c}$ and $K$ here are arbitrary teaching
values, and the point of the exercise is the algebra and the *scaling*, not the
numbers. Note the important feature: $\alpha$ does not depend on $\rho_{c}$ at all
for $n = 1$, so $R$ is fixed by $K$ alone. Changing $\rho_{c}$ changes $M$ by the
explicit factor $\rho_{c}$ but leaves $R$ untouched.

---

## ★3 — Mass–radius exponents

| $n$ | exponent $(3-n)/(1-n)$ | meaning |
|---|---|---|
| 1 | infinite | $R$ independent of $M$: the radius is set by the equation of state |
| 1.5 | $-3$ | adding mass makes the body *smaller*: self-compression wins |
| 3 | 0 | $M$ independent of $R$: the mass is fixed by $K$ alone |

**The giant-planet case is $n\approx1$**: a body supported by the pressure of a
self-gravitating gas behaves nearly like an $n = 1$ polytrope, so its radius is
nearly independent of its mass and is instead a measure of its internal entropy
(which sets $K$) and of the heavy-element mass fraction (which changes $K$
indirectly through the mean molecular weight). This is why observations of giant
planets are interpreted through *radius as a function of composition and
entropy*, not radius as a function of mass.

---

## ★4 — Why compressibility lowers $C/MR^{2}$

$$
\frac{0.20460}{0.40000} = 0.5115 .
$$

The inertia integral weights each mass element by $r^{4}/R^{4}$. In a
compressible body the density rises steeply towards the centre; the mass is
therefore concentrated where the weight is small. Concretely, the polytropic
profile has a central density far above the mean, so the effective radius of
gyration $k$ with $I = Mk^{2}$ is only $k = R\sqrt{0.2046} = 0.452R$ instead of
$R\sqrt{0.4} = 0.632R$. The ratio of gyration radii, $0.452/0.632 = 0.716$, is the
whole content of the difference.

**Is $C/MR^{2} = 0.21$ evidence for a core?** No — not by itself. The lesson's
$n = 1.5$ polytrope reaches $0.2046$ with *no* core, purely through
compressibility. A low inertia factor is evidence of central condensation, and
central condensation can be produced by compression, by a core, or by both. What
distinguishes them is a second observable, such as the figure response.

---

## ★5 — Elsasser balance and the Reynolds number

$$
B = \sqrt{\frac{\rho\Omega}{\sigma}}
= \sqrt{\frac{(10^{3})(1.75\times10^{-4})}{10^{4}}}
= \sqrt{1.75\times10^{-5}} = 4.183\times10^{-3}\ \mathrm{T}.
$$

$$
m = B R_{c}^{3}\frac{4\pi}{3\mu_{0}}
= (4.183\times10^{-3})(5\times10^{7})^{3}
\frac{4\pi}{3(4\pi\times10^{-7})}
= (4.183\times10^{-3})(1.25\times10^{23})(3.3333\times10^{6})
= 1.743\times10^{27}\ \mathrm{A\,m^{2}} .
$$

The demonstration prints exactly $1.7430\times10^{27}$ for this row. ✔

$$
\mathrm{Rm} = \mu_{0}\sigma U L
= (4\pi\times10^{-7})(10^{4})(10^{-3})(10^{6}) = 1.257\times10^{1} = 12.6 .
$$

Since $\mathrm{Rm}\approx13$ exceeds the usual threshold of order 10, a dynamo is
*plausible* — which is the strongest statement the scaling can make. It does not
prove convection, does not give the geometry of the field, and does not determine
the moment: it shows that the material properties assumed would permit a dynamo.

---

## ★6 — What the degeneracy does and does not say

The core model that matches the $p = 2$ spread profile has a core of **0.8%** of
the body's mass, while the spread model places **10%** of the mass in heavy
elements distributed through the envelope. The two models therefore have *completely
different compositions* in the sense that matters to formation: one has a
distinct dense core and a nearly hydrogen–helium envelope, the other has a
uniformly enriched envelope and practically no core.

**What is degenerate:** the observable pair (mass, radius, $C/MR^{2}$) — and, at
the level of these numbers, anything else that depends only on the radial density
profile to low order. The two structures produce the same inertia factor and the
same shape response to within the precision discussed in §5 of the lesson.

**What is not degenerate:** the composition. A formation model that predicts a
core mass, or a thermal evolution model that depends on the envelope's opacity,
distinguishes them completely. This is the reason giant-planet interior work
proceeds by *forward modelling* — choosing a composition and computing the
observables — rather than by inverting the observables into a profile.

---

## ★7 — Specification (no unique answer)

**The observable difference.** From the lesson: the four spread profiles give
$C/MR^{2}$ from $0.21538$ ($p = 0.5$) to $0.19610$ ($p = 4$), and a core model
with the same 10% heavy-element mass gives $0.18778$. The largest separation
between "core" and "spread" is about $0.022$ in $C/MR^{2}$, i.e. **10%**.

**Precision needed.** To resolve the core/spread question, $C/MR^{2}$ must be
measured to about 1 to 2%, i.e. an order of magnitude better than the separation.
$C/MR^{2}$ is not directly observable for a giant planet, but it is inferred from
$J_{2}$ and the rotation (with an assumed hydrostatic figure), so the practical
requirement is a $J_{2}$ measured to about 1% *and* a reliable statement that the
figure is hydrostatic. That is the weak link: a non-hydrostatic contribution to
$J_{2}$ of a few percent would swamp the 10% signal.

**The assumption that remains.** The equation of state. Even a perfect
$C/MR^{2}$ selects a *family* of (core mass, envelope enrichment) pairs, because
the heavy elements could be rock, ice or helium and each choice changes the
envelope's density profile. Only an assumed EOS, or an additional observable
sensitive to the *depth* of the enrichment (for example a high-degree gravity
coefficient or a normal-mode period), closes the inference.

---

## ★8 — Deriving the $n = 1$ radius independence

$$
\alpha^{2} = \frac{(n+1)K\rho_{c}^{1/n-1}}{4\pi G},
\qquad
R = \alpha\xi_{1} .
$$

For $n = 1$ the exponent $1/n - 1 = 0$, so $\rho_{c}^{0} = 1$ and

$$
\alpha^{2} = \frac{2K}{4\pi G} = \frac{K}{2\pi G}
\qquad\Longrightarrow\qquad
\alpha = \sqrt{\frac{K}{2\pi G}},
$$

which contains no $\rho_{c}$. Hence

$$
R = \xi_{1}\sqrt{\frac{K}{2\pi G}} = \pi\sqrt{\frac{K}{2\pi G}} ,
$$

a function of the equation of state alone. The mass, by contrast, is
$M = 4\pi\rho_{c}\alpha^{3}\pi \propto \rho_{c}$: adding mass (at fixed $K$) raises
the central density and leaves the radius where it was.

**Physical reason.** For an $n = 1$ polytrope the pressure scales as
$\rho^{2}$, so the pressure support grows as fast as the weight that the extra
mass adds. Adding mass compresses the interior exactly as much as it adds
material, and the two effects cancel in the radius. For a gas giant this is the
statement that the radius is set by the *entropy* of the interior (through $K$,
which depends on temperature and composition), not by the mass. That is why
radius measurements of giant planets are interpreted as constraints on
composition, thermal state and atmospheric structure — and why a body of twice
the mass can have the same radius.
