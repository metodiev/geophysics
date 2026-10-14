# Solutions — 01-11-03 Contour Integration, Residues and Real Integrals

> **Read this after attempting the exercises, not before.**
>
> Numerical values quoted as "measured" are the values printed by the companion
> script in [`../code/`](../code/contour_residues_demo.py).

---

## ★1 — A quadratic denominator

Complete the square: $x^{2}+2x+10 = (x+1)^{2}+9$. Set $z_{0} = -1+3i$, the upper
pole of $1/(z^{2}+2z+10)$ (the other is at $-1-3i$). At a simple pole of
$1/h(z)$ the residue is $1/h'(z_{0}) = 1/(2z_{0}+2) = 1/(6i)$.

Close in the upper half plane: denominator degree 2, numerator degree 0, so the
degree gap is 2 and the arc contributes $O(1/R)$. Hence

$$\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^{2}+2x+10}
= 2\pi i\cdot\frac{1}{6i} = \frac{\pi}{3} = 1.0471975511965976 .$$

**Check by real substitution.** With $u = x+1$,
$\int\mathrm{d}u/(u^{2}+9) = (1/3)\arctan(u/3)\big|_{-\infty}^{\infty}
= \pi/3$ ✓.

---

## ★2 — Two routes to $\pi/6$

**Real route.** Partial fractions:

$$\frac{1}{(x^{2}+1)(x^{2}+4)} = \frac{1}{3}\left(\frac{1}{x^{2}+1} -
\frac{1}{x^{2}+4}\right),$$

so the integral is $\frac13(\pi - \pi/2) = \pi/6 = 0.5235987755982988$.

**Residue route.** Upper poles at $i$ and $2i$. With $h = (z^{2}+1)(z^{2}+4)$,
$h'(z) = 2z(z^{2}+4) + 2z(z^{2}+1)$:

| pole | $h'(z)$ | residue |
|---|---|---|
| $i$ | $2i(3) = 6i$ | $1/(6i)$ |
| $2i$ | $4i(-3) = -12i$ | $-1/(12i)$ |

Sum $= \frac{1}{6i}-\frac{1}{12i} = \frac{1}{12i}$, so the integral is
$2\pi i/(12i) = \pi/6$ ✓. The two routes agree to the last digit, as they must —
the residue route is a *proof*, and the partial-fraction route is an independent
check that the poles were enumerated correctly.

---

## ★3 — Residues

**(a) $e^{z}/(z^{2}+1)$ at $z=i$.** Simple pole;
$h'(i) = 2i$, so

$$\operatorname{Res}_{i} = \frac{e^{i}}{2i} = \frac{e^{i}}{2i}\cdot\frac{-i}{-i}
= -\frac{i}{2}e^{i} = \frac{\sin 1 - i\cos 1}{2} \approx 0.420735 - 0.270151i .$$

**(b) $z^{2}/(z-1)^{3}$ at $z = 1$.** Pole of order 3. Use
$\operatorname{Res} = \frac{1}{(m-1)!}\lim_{z\to z_{0}}
\frac{\mathrm{d}^{m-1}}{\mathrm{d}z^{m-1}}\bigl[(z-z_{0})^{m}f(z)\bigr]$ with
$m = 3$ and $(z-1)^{3}f = z^{2}$:

$$\operatorname{Res}_{1} = \frac{1}{2!}\frac{\mathrm{d}^{2}}{\mathrm{d}z^{2}}
z^{2}\bigg|_{z=1} = \frac{1}{2}\cdot 2 = 1 .$$

Alternative: expand $z^{2} = [(z-1)+1]^{2} = (z-1)^{2}+2(z-1)+1$, so
$f = (z-1)^{-1} + 2(z-1)^{-2} + (z-1)^{-3}$ and the coefficient of
$(z-1)^{-1}$, the residue, is $1$ ✓. The expansion is quicker and shows why the
derivative formula works.

**(c) $1/(z\sin z)$ at $z = 0$.** Here $\sin z = z - z^{3}/6+\cdots$, so
$z\sin z = z^{2}(1 - z^{2}/6+\cdots)$ and

$$f = \frac{1}{z^{2}}\cdot\frac{1}{1-z^{2}/6+\cdots}
= \frac{1}{z^{2}}\left(1 + \frac{z^{2}}{6}+\cdots\right)
= \frac{1}{z^{2}} + \frac{1}{6}+\cdots,$$

so there is no $z^{-1}$ term: the residue is **0**. The function has a
double pole at the origin, and its residue vanishes — a reminder that "pole"
does not imply "non-zero residue".

**(d) $\cos z/z^{4}$ at $z=0$.** $\cos z = 1 - z^{2}/2 + z^{4}/24-\cdots$, so
$f = z^{-4} - \frac12 z^{-2} + \frac{1}{24}+\cdots$ and the coefficient of
$z^{-1}$ is **0**. A pole of even order with an even numerator function has
residue zero; the same computation for $\sin z/z^{4}$ would give residue
$-1/6$.

---

## ★4 — Cauchy's integral formula directly

For the first, $f(z) = e^{z}$ is entire and $z_{0} = 2$ lies inside $|z| = 3$:

$$\oint_{|z|=3}\frac{e^{z}}{z-2}\,\mathrm{d}z = 2\pi i\,e^{2}
= 2\pi i\times 7.389056 = 46.426768i .$$

For the second, $f(z) = \cos z/(z^{2}+1)$ is holomorphic on and inside
$|z-2| = 1$ (its poles are at $\pm i$, and $|i-2| = \sqrt5 \approx 2.236 > 1$, so
both are outside). The integrand $(z-1)$-free, there is no enclosing
singularity, so by Cauchy's theorem

$$\oint_{|z-2|=1}\frac{\cos z}{z^{2}+1}\,\mathrm{d}z = 0 .$$

**The check that is easy to forget.** Before applying any formula, verify which
singularities the contour encloses. Here the pole of the *numerator* (there is
none) and the poles of the denominator are both outside, and the answer is zero.

---

## ★★5 — $\int_{0}^{\infty}\mathrm{d}x/(x^{4}+1)$

The integrand is even, so

$$\int_{0}^{\infty}\frac{\mathrm{d}x}{x^{4}+1} =
\frac12\int_{-\infty}^{\infty}\frac{\mathrm{d}x}{x^{4}+1},$$

and the whole-line integral is half the residue sum of ★4-type because the
*halving* is a symmetry argument, not a contour argument. (This is the point of
the "why": the evenness of the integrand is what relates the two, and it must be
stated; the contour does not know about it.)

Poles: $z^{4} = -1$ gives $z_{k} = e^{i(\pi+2\pi k)/4}$, i.e.
$e^{i\pi/4}, e^{3i\pi/4}, e^{5i\pi/4}, e^{7i\pi/4}$. Two are in the upper half
plane. With $h = z^{4}+1$, $h'(z_{k}) = 4z_{k}^{3}$, and since
$z_{k}^{4} = -1$, $z_{k}^{3} = -1/z_{k}$, so
$\operatorname{Res} = -z_{k}/4$.

$$\sum_{\text{upper}}\operatorname{Res}
= -\frac14\left(e^{i\pi/4}+e^{3i\pi/4}\right)
= -\frac14\left(\frac{\sqrt2}{2}(1+i) + \frac{\sqrt2}{2}(-1+i)\right)
= -\frac{i\sqrt2}{4}.$$

Hence the whole-line integral is
$2\pi i(-i\sqrt2/4) = \pi\sqrt2/2 = \pi/\sqrt2 = 2.2214414690791$ and

$$\int_{0}^{\infty}\frac{\mathrm{d}x}{x^{4}+1} = \frac{\pi}{2\sqrt2}
= 1.1107207345396 .$$

The companion script's quadrature of the whole-line integral gives
$2.221441469079$, matching to $1.1\times10^{-14}$.

---

## ★★6 — $\int \cos 2x/(x^{2}+1)\mathrm{d}x$

Write $\cos 2x = \operatorname{Re}e^{2ix}$ and consider
$f(z) = e^{2iz}/(z^{2}+1)$, whose poles are at $\pm i$.

**Jordan's lemma** decides the contour: on the upper arc,
$|e^{2iz}| = e^{-2\operatorname{Im}z}\le1$, and the factor decays for
$\operatorname{Im}z>0$; for $\omega = 2 > 0$ the upper arc contributes nothing as
$R\to\infty$, whereas the lower arc would grow. So close **in the upper half
plane**; only the pole at $z = i$ is enclosed, with

$$\operatorname{Res}_{i}\frac{e^{2iz}}{z^{2}+1}
= \frac{e^{2i\cdot i}}{2i} = \frac{e^{-2}}{2i} = -\frac{i}{2}e^{-2}.$$

Therefore

$$\int_{-\infty}^{\infty}\frac{e^{2ix}}{x^{2}+1}\,\mathrm{d}x
= 2\pi i\left(-\frac{i}{2}e^{-2}\right) = \pi e^{-2},$$

and taking real parts,

$$\int_{-\infty}^{\infty}\frac{\cos 2x}{x^{2}+1}\,\mathrm{d}x = \frac{\pi}{e^{2}}
= 0.4251683315876 .$$

**Consistency check.** At $\omega = 0$ this must reduce to
$\int\mathrm{d}x/(1+x^{2}) = \pi$ ✓, which is a one-line test of the formula
$\pi e^{-a\omega}$ with $a = 1$ — and it is the reason the sign of $\omega$ must
be stated: for $\omega<0$ the same algebra with the lower contour gives the same
answer, because $\cos$ is even and only $|\omega|$ can appear.

---

## ★★7 — The indentation lemma

**(a)** Parametrise the semicircle as $z = x_{0}+\epsilon e^{i\theta}$ with
$\mathrm{d}z = i\epsilon e^{i\theta}\mathrm{d}\theta$. Near a simple pole,
$f(z) = r/(z-x_{0}) + g(z)$ with $g$ analytic, so

$$\int_{\gamma}f\,\mathrm{d}z
= \int_{\theta_{1}}^{\theta_{2}}\left(\frac{r}{\epsilon e^{i\theta}}+g\right)
i\epsilon e^{i\theta}\,\mathrm{d}\theta
= ir(\theta_{2}-\theta_{1}) + O(\epsilon) .$$

- A semicircle in the **upper** half plane traversed **from right to left**
  ($\theta$ from $0$ to $\pi$) gives $i\pi r$.
- A semicircle in the **upper** half plane traversed **from left to right**
  ($\theta$ from $\pi$ to $0$) gives $-i\pi r$, i.e. an indentation that dips
  *below* the pole gives $-i\pi r$.

So the sign is fixed by the direction of travel, and the convention to remember is
the one used in the derivation of the Kramers-Kronig relations: an indentation
*below* a real pole traversed left to right contributes $-i\pi r$ (equivalently, it
is the half of an encircling loop that is missed).

**(b)** Take $f(z) = e^{iz}/(z-a)$ and close in the upper half plane (Jordan's
lemma, $\omega = 1>0$). The contour consists of the real axis with an indentation
below $z = a$, plus the upper arc. Its interior contains **no** singularity, so
the closed integral is zero. The large arc contributes nothing, so

$$\mathrm{P.V.}\int_{-\infty}^{\infty}\frac{e^{ix}}{x-a}\,\mathrm{d}x
+ \bigl(-i\pi\operatorname{Res}_{a}\bigr) = 0 .$$

The residue of $e^{iz}/(z-a)$ at $z=a$ is $e^{ia}$, so

$$\mathrm{P.V.}\int_{-\infty}^{\infty}\frac{e^{ix}}{x-a}\,\mathrm{d}x
= i\pi e^{ia} .$$

As a consistency check, the real part gives
$\mathrm{P.V.}\int\cos x/(x-a)\mathrm{d}x = -\pi\sin a$ and the imaginary part
gives $\mathrm{P.V.}\int\sin x/(x-a)\mathrm{d}x = \pi\cos a$; setting $a=0$
recovers the Dirichlet integral $\int\sin x/x = \pi$ over the whole line, i.e.
$\pi/2$ over $(0,\infty)$ ✓.

**(c)** Without the oscillatory factor, $\int f$ with $f \sim r/(x-a)$ behaves
like $r\ln|x-a|$, which **diverges logarithmically at both edges** of the
puncture; the two divergences are equal and opposite only for the *symmetric*
limit, so the Cauchy principal value exists while the improper integral does not.
The lemma, applied blindly, would still return $\pm i\pi r$ — which is the value
of the principal value of $1/(x-a)$ *times* the residue — but the intermediate
step where the arc contribution was discarded relied on the $e^{iz}$ decay and
would be unjustified. **The lemma tells you the contribution of the indentation;
it does not by itself tell you that the rest of the contour is under control.**

---

## ★★8 — Summing $\sum 1/(n^{2}+1)$

From the identity
$\sum_{n=-\infty}^{\infty}1/(n^{2}+a^{2}) = (\pi/a)\coth(\pi a)$, split off
$n = 0$:

$$\sum_{n=1}^{\infty}\frac{1}{n^{2}+1}
= \frac12\left[\frac{\pi}{1}\coth\pi - 1\right]
= \frac{\pi\coth\pi - 1}{2} = 1.0766740474686 .$$

**Numerical verification.** Summing $n = 1,\dots,2\times10^{5}$ gives
$1.0766690474811$; the analytic tail is
$\sum_{n>N}1/n^{2}\approx1/N = 5\times10^{-6}$, and adding it gives
$1.0766740474811$, agreeing with the closed form to $1.3\times10^{-11}$. The
comparison is meaningful only *after* the tail correction: the raw partial sum is
wrong by $10^{-5}$ of its own value, and quoting that as a discrepancy would have
been an error of the check rather than of the identity.

---

## ★★★9 — Inverting the Kramers-Kronig integral

**(a)** With $\operatorname{Im}H(\omega') = -\omega'\tau/(1+\omega'^{2}\tau^{2})$,

$$-\frac{2}{\pi}\,\mathrm{P.V.}\int_{0}^{\infty}
\frac{\omega'\operatorname{Im}H(\omega')}{\omega'^{2}-\omega^{2}}
\,\mathrm{d}\omega'
= \frac{2\tau}{\pi}\,\mathrm{P.V.}\int_{0}^{\infty}
\frac{\omega'^{2}}{(1+\omega'^{2}\tau^{2})(\omega'^{2}-\omega^{2})}
\,\mathrm{d}\omega' .$$

Partial fractions:

$$\frac{\omega'^{2}}{(1+\omega'^{2}\tau^{2})(\omega'^{2}-\omega^{2})}
= \frac{A}{1+\omega'^{2}\tau^{2}} + \frac{B}{\omega'^{2}-\omega^{2}},$$

with $A = 1/(1+\omega^{2}\tau^{2})$ and $B = \omega^{2}/(1+\omega^{2}\tau^{2})$
(obtained by comparing the coefficient of $\omega'^{2}$ and the constant term).

**(b)** The term with $B$ is a constant multiple of
$\mathrm{P.V.}\int_{0}^{\infty}\mathrm{d}\omega'/(\omega'^{2}-\omega^{2})$,
which is **zero** — that is the definition of the principal value here, and it is
the same identity that justifies subtracting the singularity in a numerical
quadrature. What remains is elementary:

$$\int_{0}^{\infty}\frac{\mathrm{d}\omega'}{1+\omega'^{2}\tau^{2}}
= \frac{\pi}{2\tau} .$$

Hence

$$-\frac{2}{\pi}\cdot\frac{\tau\pi}{2}\cdot\frac{1}{1+\omega^{2}\tau^{2}}
= \frac{1}{1+\omega^{2}\tau^{2}} = \operatorname{Re}H(\omega) .$$

**(c)** At $\omega\tau = 1$ the formula gives $1/(1+1) = 1/2$, which is the exact
value of $\operatorname{Re}H = 1/(1+\omega^{2}\tau^{2})$ there, and the companion
script's numerical evaluation of the same principal value at $\omega = 1$ with
$\tau = 1$ gives $0.50000000000000$ (difference $8.9\times10^{-16}$).

What the check **does** establish: the algebra of the partial fractions and the
identification of the vanishing term are correct, and the sign of the relation is
right for the $e^{-i\omega t}$ convention. What it **does not** establish: that
the Debye model is a correct model of a real medium, or that the relation holds
for any other response. It is a proof about a mathematical identity, and it must
be paired with a physical question (does this medium attenuate?) before it says
anything about the Earth.

---

## ★★★10 — Inverting $Y(s) = (s+3)/[(s+1)(s+2)]$

**(a)** Partial fractions:

$$\frac{s+3}{(s+1)(s+2)} = \frac{2}{s+1} - \frac{1}{s+2},$$

checked by combining over the common denominator:
$2(s+2)-(s+1) = s+3$ ✓. Poles at $s = -1$ and $s = -2$, both with
$\operatorname{Re}s<0$, so the response is stable.

**(b)** Using $\mathcal{L}\{e^{-at}\} = 1/(s+a)$,

$$y(t) = 2e^{-t} - e^{-2t}, \qquad t>0 .$$

**(c)** **Initial value:** $\lim_{s\to\infty}sY(s) =
\lim s(s+3)/((s+1)(s+2)) = 1$, and $y(0^{+}) = 2-1 = 1$ ✓.
**Final value:** $\lim_{s\to0}sY(s) = 0$, and
$y(\infty) = 0$ ✓ (both poles in the left half plane, so the hypothesis of the
final-value theorem holds). One further check worth making: $y$ is positive for
all $t>0$ ($2e^{-t} > e^{-2t}$ always), which is what a step-like response of a
passive system must be.

**(d)** With $c = 0$ the vertical contour passes **through both poles**, and the
integral is not defined as an ordinary improper integral: the integrand has a
$1/(s+1)$ and a $1/(s+2)$ singularity on the path. Numerically, the quadrature
would produce a large, oscillating, grid-dependent value — it would *not* be
merely inaccurate. Convergence would not improve as the node count increased, and
the result would change by large amounts if the node positions were shifted. The
diagnostic is that behaviour, not the magnitude of the number: **a contour
integral that does not converge under refinement is a contour in the wrong
place**, and the cure is to move $c$ to the right of every singularity (or to take
principal values deliberately, with the indentations accounted for as in ★★7).

---

## Self-assessment: have you actually learned this?

You can, without notes:

- state the contour, the enclosed poles and the arc argument for a rational
  integral, and get the answer to a numerical check;
- compute a residue of a simple pole, a pole of order $m$, and a double pole with
  an even numerator (residue zero);
- choose the closing half plane from the sign of $\omega$ and justify it with
  Jordan's lemma;
- apply the indentation lemma with the correct sign and explain what it does not
  prove;
- explain why principal values exist when improper integrals do not;
- check a Bromwich contour by asking where its singularities are.
