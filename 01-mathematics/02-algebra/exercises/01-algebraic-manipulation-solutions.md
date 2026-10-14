# Solutions — 01-02-01 Algebraic Manipulation and Solving Equations

> **Read this after attempting the exercises, not before.**
>
> These are worked solutions showing one valid route and the reasoning behind it.
> Numeric values were computed with the standard library rather than estimated by
> hand. Where a problem has more than one defensible answer, that is stated.

---

## ★1 — Solving a reciprocal relation for $v$

Multiply both sides by $v v_1 v_2$:

$$v_1v_2 = v v_2 + v v_1 = v(v_1 + v_2),$$

so

$$\boxed{\;v = \frac{v_1v_2}{v_1 + v_2}\;}$$

**Conditions.** $v_1 \ne 0$, $v_2 \ne 0$ (otherwise the original reciprocals are
undefined), and $v_1 + v_2 \ne 0$ (otherwise the division producing $v$ is
undefined). For physical velocities all three hold automatically, but they are
part of the answer: an algebra solution without its domain is incomplete.

**Check.** With $v_1 = 3$, $v_2 = 6$: $v = 18/9 = 2$. Then
$1/v = 0.5$ and $1/v_1 + 1/v_2 = 1/3 + 1/6 = 0.5$. ✓

**Limiting cases.** If $v_2 \to \infty$ then $v \to v_1$: an infinitely fast
second medium contributes nothing to the resistance-like sum, which is the
expected behaviour.

---

## ★2 — The geothermal relation

**(a)** $T = T_0 + \gamma z \;\Longrightarrow\; z = \dfrac{T - T_0}{\gamma}$,
valid for $\gamma \ne 0$.

**(b)** $\gamma = \dfrac{T - T_0}{z}$, valid for $z \ne 0$.

**(c)** $z = (135.0 - 10.0)/25.0 = \mathbf{5.00}$ **km**. Check:
$T(5.00) = 10.0 + 25.0 \times 5.00 = 135.0\,^\circ$C. ✓

**(d)** $\gamma = (95.0 - 10.0)/3.5 = \mathbf{24.29\ ^\circ C\,km^{-1}}$.

**Physical comment.** $24.3\ ^\circ$C/km is close to the canonical continental
average of about $25\ ^\circ$C/km, so the number is plausible — but the exercise
does not establish that this is a *measured* gradient. It is a gradient implied by
one temperature and one depth, and it inherits all the uncertainty of both, plus
the assumption that the profile is linear. Stated arithmetic is not stated
geology.

**Units.** $\mathrm{K\,km^{-1}}$ in (b), $\mathrm{km}$ in (a); the temperature
difference cancels the choice of kelvin or Celsius because it is a difference.

---

## ★3 — Quadratics

**(a)** $x^{2}-3x+2 = (x-1)(x-2) = 0$, so $x = 1$ or $x = 2$.

By the formula: $a=1$, $b=-3$, $c=2$, $\Delta = 9-8 = 1$,
$x = (3 \pm 1)/2 \in \{1, 2\}$. ✓

**(b)** $x^{2}-6x+9 = (x-3)^{2} = 0$, so $x = 3$ (twice).

By the formula: $\Delta = 36-36 = 0$, $x = 6/2 = 3$.

**(c)** The discriminant is $0$: there is one **repeated** real root. Geometrically
the parabola touches the $x$-axis at a single point. Numerically this matters:
near a repeated root the function is flat, so a small error in the coefficients
moves the root a large distance — the same sensitivity demonstrated numerically in
★★★9 below and analysed in
[01-01-05](../../01-arithmetic/05-error-and-conditioning.md).

---

## ★4 — Hydrostatic pressure

**(a)** $h = \dfrac{P}{\rho g}$, valid for $\rho \ne 0$ and $g \ne 0$.

**(b)** $h = \dfrac{1.0\times10^{7}}{1000 \times 9.81} = \mathbf{1019.37}$ **m**.

Check by substitution: $\rho g h = 1000 \times 9.81 \times 1019.368 = 1.0\times10^{7}$
Pa. ✓

**(c)** Dimensions: $[P] = \mathrm{kg\,m^{-1}\,s^{-2}}$,
$[\rho g] = \mathrm{kg\,m^{-3}}\cdot\mathrm{m\,s^{-2}} =
\mathrm{kg\,m^{-2}\,s^{-2}}$, so

$$\left[\frac{P}{\rho g}\right] = \frac{\mathrm{kg\,m^{-1}\,s^{-2}}}
{\mathrm{kg\,m^{-2}\,s^{-2}}} = \mathrm{m}. ✓$$

**(d)** As $\rho \to 0$ the expression diverges: an ever-thicker column of
weightless fluid is needed to produce any pressure. The limit is a mathematically
correct statement about the formula and physically meaningless as a description of
a fluid, which is exactly why the *conditions* on rearrangements matter. Note also
that the formula is a hydrostatic approximation: it assumes the fluid is at rest
and of uniform density, neither of which holds in a real borehole over a kilometre.

---

## ★★5 — Solving an equation with a square root

Start from $\sqrt{2x+3} = x$.

**Domain.** The square root requires $2x + 3 \ge 0$; the right-hand side is a
square root, so it must be non-negative, hence $x \ge 0$.

**Square.** $2x + 3 = x^{2}$, i.e. $x^{2} - 2x - 3 = 0$, i.e.
$(x-3)(x+1) = 0$, so $x = 3$ or $x = -1$.

**Check in the original equation:**

| candidate | $\sqrt{2x+3}$ | $x$ | valid? |
|---|---|---|---|
| $x = 3$ | $3.000000$ | $3.000000$ | **yes** |
| $x = -1$ | $1.000000$ | $-1.000000$ | **no** |

**Answer:** $x = 3$, uniquely. The candidate $x=-1$ is extraneous — it satisfied
the squared equation because $(-1)^{2} = 1^{2}$, and it is excluded both by the
domain argument ($x \ge 0$) and by direct substitution.

---

## ★★6 — Radiometric age by inversion

**(a)** $N/N_0 = e^{-\lambda t}$, so

$$\ln(N/N_0) = -\lambda t
\qquad\Longrightarrow\qquad
t = -\frac{1}{\lambda}\ln\frac{N}{N_0} = \frac{\ln(N_0/N)}{\lambda}.$$

Valid for $N_0 > 0$, $N > 0$, $\lambda \ne 0$.

**(b)** With $N_0/N = 4$, $\lambda = \ln 2/5730 = 1.209681\times10^{-4}\ \mathrm{yr^{-1}}$:

$$t = \frac{\ln 4}{1.209681\times10^{-4}} = 11460.0\ \mathrm{yr}.$$

**(c)** $N_0/N = 4 = 2^{2}$, so the sample has decayed for exactly **two
half-lives** — which is why the answer is exactly $2 \times 5730 = 11460$ yr.
The logarithm makes this explicit: $\ln 4 = 2\ln 2$, and dividing by
$\lambda = \ln2/T_{1/2}$ cancels the $\ln 2$ and leaves $2T_{1/2}$.

**Scope note.** This is a *conventional* age from a simple parent–daughter model
with no initial daughter and no reservoir effect. Converting it to a calendar age,
or to a date from a real sample, requires the additional corrections of
[01-02-03](../03-exponentials-logarithms.md) — the arithmetic here is only the
first step.

---

## ★★7 — Refraction crossover

**(a)** Square both sides and rearrange:

$$\frac{x_c^{2}}{4H^{2}} = \frac{v_2+v_1}{v_2-v_1}
\;\Longrightarrow\;
H^{2} = \frac{x_c^{2}}{4}\cdot\frac{v_2-v_1}{v_2+v_1}
\;\Longrightarrow\;
H = \frac{x_c}{2}\sqrt{\frac{v_2 - v_1}{v_2 + v_1}}.$$

The positive root is the physical one. Conditions: $v_2 > v_1 > 0$ (a head wave
requires the lower layer to be faster).

**(b)** $H = \frac{120}{2}\sqrt{\frac{2500}{5500}} = 60 \times 0.674200 =
\mathbf{40.452}$ **m**.

Verification by substitution into the original form:
$2(40.452)\sqrt{5500/2500} = 80.904 \times 1.48324 = 120.00$ m. ✓

**(c)** Let $k = x_c^{2}/(4H^{2})$. Then

$$k = \frac{v_2+v_1}{v_2-v_1}
\;\Longrightarrow\;
k v_2 - k v_1 = v_2 + v_1
\;\Longrightarrow\;
v_2(k-1) = v_1(k+1)
\;\Longrightarrow\;
\frac{v_2}{v_1} = \frac{k+1}{k-1}.$$

The condition is $k > 1$, i.e. $x_c > 2H$. That is not an algebraic technicality:
the crossover distance must exceed twice the layer thickness, otherwise even the
vertical raypath switch is impossible before the receiver.

**(d)** $\theta_c = \arcsin(1500/4000) = \arcsin(0.375) = \mathbf{21.7156^\circ}$.

---

## ★★8 — Two picks, two unknowns

**(a)** The equations are

$$0.100 = a + 100b, \qquad 0.180 = a + 400b.$$

Subtracting the first from the second: $0.080 = 300b$, so

$$b = 2.666667\times10^{-4}\ \mathrm{s\,m^{-1}}, \qquad
a = 0.100 - 100b = 0.0733333\ \mathrm{s}.$$

**(b)** In $t = a + bx$, the slope $b$ is the **inverse velocity** of the
refracting medium, so $v_2 = 1/b = 3750.0$ m/s. The intercept $a$ is the
travel-time delay accumulated in the overlying layer at zero offset; for a
horizontal two-layer case it equals $2H\cos\theta_c/v_1$, so it is the key to the
thickness once $v_1$ is known.

**(c)** $a$ has units of seconds; $b$ has units of
$\mathrm{s\,m^{-1}} = \mathrm{m^{-1}\,s}$, so $bx$ is
$\mathrm{m^{-1}\,s}\cdot\mathrm{m} = \mathrm{s}$, matching $t$ and $a$. ✓

**Comment.** $v_2 = 3750$ m/s is a plausible refractor velocity, but note that
only two picks were used: there is no redundancy, no check on the straight-line
assumption, and any pick error propagates directly into both $a$ and $b$. A real
survey fits many picks, and the residuals are part of the result — see
[01-13 Probability and Statistics Foundations](../../13-probability-and-statistics-foundations/README.md).

---

## ★★★9 — How a quadratic root collapses

**(a)** Expand $(x-1)(x-(1-\delta)) $:

$$x^{2} - (2-\delta)x + (1-\delta),$$

which matches the given polynomial. So the roots are exactly $x=1$ and
$x = 1-\delta$.

**(b)** Naive smaller root $x = (-b-\sqrt{b^{2}-4ac})/2$ with
$b = -(2-\delta)$, $c = 1-\delta$, measured in binary64:

| $\delta$ | computed $b^{2}-4c$ (exact $\delta^{2}$) | naive root | relative error |
|---|---|---|---|
| $10^{-3}$ | $1.000000\times10^{-6}$ | $0.9989999999998541$ | $1.46\times10^{-13}$ |
| $10^{-6}$ | $1.000533\times10^{-12}$ | $0.9999989998667703$ | $1.33\times10^{-10}$ |
| $10^{-7}$ | $9.769963\times10^{-15}$ | $0.9999999005784393$ | $5.78\times10^{-10}$ |
| $10^{-8}$ | $4.440892\times10^{-16}$ | $0.9999999844632879$ | $5.54\times10^{-9}$ |
| $10^{-9}$ | $-4.440892\times10^{-16}$ | — | *fails* |

**(c)** At $\delta = 10^{-9}$ the computed discriminant is
$-4.44\times10^{-16}$, so $\sqrt{\cdot}$ is not even defined and the naive route
throws an error. The exact discriminant is $\delta^{2} = 10^{-18}$, but it is
formed as the difference of two numbers near 4: the rounding error in each term is
of order $u \times 4 \approx 4.4\times10^{-16}$, which is 400 times larger than
the true discriminant. **Catastrophic cancellation** has destroyed the quantity
completely — and here the cancellation is so severe that even the *sign* is wrong.

**(d)** The product of the roots gives the same root exactly:

$$x_1x_2 = \frac{c}{a} \;\Longrightarrow\; x_2 = \frac{c}{a x_1} = \frac{1-\delta}{1}
= 1-\delta,$$

with measured error $0.0$ at every $\delta$ in the table (the large root
$x_1 = (-b+\sqrt{\cdot})/2$ is computed as exactly $1$ because it involves only
additions of like-signed quantities).

**(e) Threshold and report.**

*Method.* Naive quadratic formula against the known exact roots, at five values
of $\delta$ spanning four decades, in binary64.

*Results.* The relative error of the naive root grows like $u/\delta$ while the
discriminant is still meaningful: the model predicts
$2u/\delta = \{2.2\times10^{-13},\ 2.2\times10^{-10},\ 2.2\times10^{-9},\
2.2\times10^{-8}\}$ for the first four rows, against measured values a factor of
1.5 to 4 smaller — good order-of-magnitude agreement. The discriminant is dominated by
round-off once $\delta^{2} \lesssim 4u$, i.e.

$$\delta \lesssim 2\sqrt{u} \approx 3\times10^{-8},$$

and the method fails outright at $\delta = 10^{-9}$ (measured, not estimated). The
product-of-roots route is exact at every $\delta$ tested, because it contains no
subtraction of nearly equal quantities.

*Limits.* These numbers are for one quadratic, one binary64 implementation and one
set of coefficients; the *scaling* ($u/\delta$ degradation, failure near
$\sqrt{u}$) is general to the naive formula, but the exact crossover differs
between formats (in binary32 it would move to $\delta \sim 10^{-4}$) and between
different coefficient magnitudes. The conclusion does not extend to quartics,
where no simple closed form is usable and one switches to a companion-matrix
eigenvalue method — see [01-07 Linear Algebra](../../07-linear-algebra/README.md).

---

## ★★★10 — Solving for a temperature inside an exponential

**(a)** With $D = D_0e^{-E_a/(RT)}$,

$$T = \frac{E_a}{R\ln(D_0/D)}.$$

For $D_0 = 1.0\times10^{-6}$, $D = 1.0\times10^{-18}$,
$\ln(D_0/D) = \ln(10^{12}) = 27.6310$, $E_a = 2.0\times10^{5}$ J/mol,
$R = 8.31446261815324$ J/(mol K):

$$T = \frac{2.0\times10^{5}}{8.31446261815324 \times 27.6310}
= 870.560\ \mathrm{K} = 597.4\,^\circ\mathrm{C}.$$

**(b)** With $g(T) = \ln D(T) - \ln D_{\text{target}} = \ln D_0 - E_a/(RT)
- \ln D_{\text{target}}$:

$$g(300) = -52.55 < 0, \qquad g(2000) = +15.60 > 0,$$

so the bracket $[300, 2000]$ is valid (continuous $g$, sign change). Bisection
halving an interval of width $1700$ K until the half-width is below $10^{-9}$ K
needs

$$\lceil \log_2(1700/10^{-9}) \rceil = \lceil 40.63 \rceil = 41$$

iterations; the measured run converged in **40 iterations** to
$T = 870.5603353425886$ K, differing from the closed form by
$-1.6\times10^{-10}$ K — i.e. at the level of the stopping criterion, as it must
be.

**(c)** Prefer the numerical route when the equation is *not* analytically
invertible. Here it is invertible, so the closed form is better: it is exact
(up to one rounding), needs no bracket, and gives no false impression of
generality. The numerical route is the general tool — it works equally well for
$D(T) = D_0 e^{-E_a/(RT)}\left(1 + \beta T\right)$ or any other modification,
whereas the closed form has to be re-derived for every change of model. In a
modelling code one therefore solves numerically, and validates the solver against
a closed form wherever one exists.

**(d)** Dependence on the constants: the answer scales **linearly** with $E_a$ at
fixed $\ln(D_0/D)$ — doubling $E_a$ to $4.0\times10^{5}$ J/mol gives
$T = 1741.121$ K, exactly twice 870.560 K. The answer is *insensitive* to how the
ratio $D_0/D$ is achieved: only the logarithm of the ratio enters, so
$D_0 = 10^{-6}, D = 10^{-18}$ and $D_0 = 10^{-9}, D = 10^{-21}$ give the same
temperature. That is a real and useful invariance, because $D_0$ is usually the
worst-constrained parameter in a diffusion experiment.

---

## Notes on what these solutions do not settle

- The diffusion constants in ★★★10 are explicitly **ILLUSTRATIVE**. No value
  quoted here should be used to date, thermal-model or interpret a real rock; real
  Arrhenius parameters for any mineral require the source and its uncertainty.
- The radiocarbon half-life used in ★★6 is the conventional $5730 \pm 40$ yr.
  Real radiocarbon dating also requires calibration and a reservoir correction,
  neither of which is part of an algebra exercise.
- The quadratic-collapse threshold in ★★★9 was measured on one machine and one
  interpreter; the mechanism is general, the exact crossover is not.
