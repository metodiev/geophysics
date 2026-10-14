# Solutions — 12-06-03 Nutation and Constraints on Core Properties

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [03 Nutation and Constraints on Core Properties](../03-nutation-constraints.md).

---

## ★1 — Free wobble periods

$$
T_{\text{inertial}} = \frac{1}{H} = 400\ \text{sidereal days},
\qquad
T_{\text{body}} = \frac{1-H}{H} = 399\ \text{sidereal days}.
$$

The station sits on the rotating body, so it sees the **body-frame** period:
399.0 sidereal days. The inertial period is what the mode looks like against the
stars. The two differ by the factor $1-H$; quoting one as the other is a 0.25%
error at $H = 1/400$, and it grows with $H$.

---

## ★2 — Free-core-nutation period

$$
A_{c} = 0.10\left(1 - \frac{1}{500}\right) = 0.0998,
\qquad
A_{\text{red}} = \frac{A_{m}A_{c}}{A_{m}+A_{c}}
= \frac{0.99\times0.0998}{0.99+0.0998} = \frac{0.098802}{1.0898}
= 0.0906607,
$$

$$
T_{\text{FCN}} = \frac{0.0906607}{(1/500)\times0.10}
= \frac{0.0906607}{2.0\times10^{-4}} = 453.3\ \text{sidereal days}.
$$

Note the structure: the period scales as $1/e_{c}$, so halving the core's
oblateness doubles the period. The inertia ratio enters only through
$A_{\text{red}}/(A_{m}+A_{c})$-type factors, which is the weak dependence the
lesson measures.

---

## ★3 — Which mode is which

The **free core nutation** is the slow, long-period mode, because it is the
*relative* motion of the two bodies: the restoring torque is proportional to the
core's oblateness (small) and the inertia to be overcome is the reduced inertia
(also small), but the oblateness is far smaller than order unity, so the mode is
slow. The whole-body Euler mode has the full moment of inertia and the full
obliquity $C-A$ and is therefore much faster (period $\sim1/H$ days).

An **oblate** core is required because a spherical core has no preferred axis: any
tilt of a spherical core is a neutral mode at zero frequency, and it exerts no
pressure torque on the mantle. Formally, $K = C_{c}-A_{c}\to0$ makes the relative
mode disappear, which the demonstration's limits confirm.

---

## ★4 — Inverting a period with an error bar

With the inertia ratios fixed at the lesson-02 values
($A_{m} = 0.99672$, $C_{c} = 0.11$, $A_{\text{red}} = 0.098844$):

$$
e_{c} = \frac{A_{\text{red}}}{T\,C_{c}}
= \frac{0.098844}{400\times0.11} = 2.2465\times10^{-3},
\qquad
\frac{1}{e_{c}} = 445.1 .
$$

Since $e_{c}\propto 1/T$, a $\pm2\%$ error in $T$ gives a $\mp2\%$ error in
$e_{c}$:

| $T$ (d) | $e_{c}$ | $1/e_{c}$ |
|---|---|---|
| 392 (2% low) | $2.2465\times10^{-3}\times(400/392) = 2.2923\times10^{-3}$ | 436.2 |
| 400 | $2.2465\times10^{-3}$ | 445.1 |
| 408 (2% high) | $2.2465\times10^{-3}\times(400/408) = 2.2024\times10^{-3}$ | 454.0 |

So the measurement constrains $1/e_{c}$ to a range $\pm2\%$ wide, i.e. $e_{c}$
between $2.20\times10^{-3}$ and $2.29\times10^{-3}$. Everything here scales
linearly: the period is a *linear* ruler on the core's oblateness, which is why
the lesson describes nutation as primarily an oblateness measurement.

---

## ★5 — Precession rate

$$
n = \frac{2\pi}{2\times365.25\times86164.0905} = 9.9813\times10^{-8}\ \mathrm{s^{-1}},
\qquad
\Omega = \frac{2\pi}{86164.0905} = 7.2921\times10^{-5}\ \mathrm{s^{-1}},
$$

$$
\dot\psi = \frac{3}{2}\frac{n^{2}}{\Omega}H\cos 45^{\circ}
= 1.5\times\frac{(9.9813\times10^{-8})^{2}}{7.2921\times10^{-5}}
\times\frac{1}{400}\times0.70711
= 3.6235\times10^{-13}\ \mathrm{rad\,s^{-1}} .
$$

$$
T_{\text{node}} = \frac{2\pi}{3.6235\times10^{-13}}
= 1.734\times10^{13}\ \mathrm{s} = 5.49\times10^{5}\ \mathrm{yr} .
$$

At $\varepsilon = 60^{\circ}$, $\cos\varepsilon = 0.5$ instead of $0.7071$: the
rate is smaller by the factor $0.5/0.7071 = 0.7071$, so the period is *longer* by
$1/0.7071 = 1.414$: $7.77\times10^{5}$ yr. The rate is exactly linear in
$\cos\varepsilon$ and in $H$, and inversely proportional to the spin rate — the
four scalings the lesson's §2 measures.

---

## ★6 — Error propagation along the chain

$$
T\propto\frac{1}{e_{c}}
\;\Longrightarrow\;
\frac{\delta e_{c}}{e_{c}} = -\frac{\delta T}{T} = \mp2\% ,
$$

$$
M_{c} = \frac{\omega^{2}r_{c}^{3}}{G(4/5)e_{c}}
\;\Longrightarrow\;
\frac{\delta M_{c}}{M_{c}} = 3\frac{\delta r_{c}}{r_{c}} - \frac{\delta e_{c}}{e_{c}}
= \pm15\% \mp 2\% ,
$$

$$
\rho_{c} = \frac{M_{c}}{\tfrac43\pi r_{c}^{3}}
\;\Longrightarrow\;
\frac{\delta\rho_{c}}{\rho_{c}}
= \frac{\delta M_{c}}{M_{c}} - 3\frac{\delta r_{c}}{r_{c}} = \mp2\% .
$$

Two things are worth stating. The mean density is *insensitive* to the assumed
core radius (the $r_{c}^{3}$ factors cancel), which makes it a better-determined
quantity than the core mass. The **core mass carries the whole $3\delta r_{c}/r_{c}$
term**, i.e. $\pm15\%$ from a 5% radius error, and that is the dominant
uncertainty in the chain.

---

## ★7 — Specification for a second observable (no unique answer)

**The degeneracy.** From §4 of the lesson,
$\mathrm{d}\ln T_{\text{FCN}}/\mathrm{d}\ln(C_{c}/C_{m}) = -0.0953$: a factor 4 in
the core's inertia share moves the period by only 25%. So $T$ alone determines
$e_{c}$ to a few percent at *any* assumed core size — the two parameters are
almost perfectly degenerate in this one number.

**A second observable.** The most natural partner is the **resonance strength**
(the amplitude magnification at the resonance, i.e. the product of the coupling
and the inertia ratios) rather than the resonance *position*. In the model of the
lesson the resonance strength scales with $A_{\text{red}}$, so a measurement of
the magnification at the few-percent level translates into
$A_{\text{red}}$ — and hence $C_{c}/C_{m}$ — to the few-percent level. Combined
with the period, that is two numbers for two parameters.

**Precision required.** To resolve a factor 2 in $C_{c}/C_{m}$, the magnification
must be measured to better than the 25% span that a factor 4 produces, i.e. to
about 10%. That is a demanding but not impossible nutation-amplitude requirement,
and it is the reason real analyses fit a *resonance model* to many nutation terms
simultaneously rather than to one.

**The assumption that remains.** The coupling constant is taken as
$K = C_{c}-A_{c}$ and the fluid core is treated as a rigidly rotating body.
Mantle deformation and core flow change the period by tens of percent, so the
recovered $e_{c}$ is an *effective* oblateness of a two-parameter model, not a
geometric property of a real core.

---

## ★8 — Deriving the reduced-inertia result

**Start from two equations of motion.** For tilts $m_{m}$, $m_{c}$ (complex,
measured in the frame rotating at $\Omega$) and a coupling torque proportional to
the difference,

$$
A_{m}\dot m_{m} = -i\Omega K\,(m_{m}-m_{c}),
\qquad
A_{c}\dot m_{c} = +i\Omega K\,(m_{m}-m_{c}).
$$

The torques are equal and opposite, so total angular momentum about the tilt axes
is conserved: the modes are (i) a "common" mode and (ii) a relative mode.

**Divide by the inertias.**

$$
\dot m_{m} = -\frac{i\Omega K}{A_{m}}(m_{m}-m_{c}),
\qquad
\dot m_{c} = +\frac{i\Omega K}{A_{c}}(m_{m}-m_{c}).
$$

**Subtract** the second from the first, with $\theta = m_{m}-m_{c}$:

$$
\dot\theta = -i\Omega K\left(\frac{1}{A_{m}}+\frac{1}{A_{c}}\right)\theta
= -i\Omega K\,\frac{A_{m}+A_{c}}{A_{m}A_{c}}\,\theta .
$$

**Identify**

$$
\frac{1}{A_{\text{red}}} \equiv \frac{1}{A_{m}}+\frac{1}{A_{c}}
= \frac{A_{m}+A_{c}}{A_{m}A_{c}}
\;\Longrightarrow\;
A_{\text{red}} = \frac{A_{m}A_{c}}{A_{m}+A_{c}} .
$$

Hence $A_{\text{red}}\dot\theta = -i\Omega K\theta$, with mode frequency
$\Omega K/A_{\text{red}}$ and period
$T = A_{\text{red}}/(e_{c}C_{c})$ sidereal days. ✔

**Check the spherical-core limit.** With $K = C_{c}-A_{c}\to0$ the relative mode
has zero frequency: $\dot\theta = 0$, i.e. an arbitrary (neutral) tilt. A
spherical core is not coupled to the mantle's figure, so there is no restoring
torque and no free core nutation. This is exactly the limit the demonstration
prints, and it is the physical content of the model rather than an algebraic
curiosity.
