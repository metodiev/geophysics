# Solutions — 19-02-01 Deriving Finite-Difference Operators via Taylor Expansion

> **Read after attempting the exercises.** The weights below were solved and
> checked numerically during preparation.

Lesson: [01 FD Derivation](../01-fd-derivation.md).

---

## ★1 — Forward difference

Offsets $[0, 1]$. Moment equations for $d = 1$:
$w_0 + w_1 = 0$ and $0\,w_0 + 1\,w_1 = 1$. Hence $w_1 = 1$, $w_0 = -1$: the
stencil is $(f_{i+1}-f_i)/h$, first order, leading term $+\frac{h}{2}f''$.

---

## ★2 — Centred second derivative

Offsets $[-1,0,1]$, $d = 2$: $w_{-1}+w_0+w_1 = 0$;
$-w_{-1}+w_1 = 0$; $w_{-1}+w_1 = 2$. Solution $w_{-1} = w_1 = 1$,
$w_0 = -2$, i.e. $(u_{i+1}-2u_i+u_{i-1})/h^{2}$.

First surviving moment: $m = 4$, $\sum w_i\xi_i^{4} = 1+1 = 2$, so the order is
$4-2 = 2$ and the leading error is
$\frac{h^{2}}{4!}\cdot2\cdot f'''' = \frac{h^{2}}{12}f''''$, i.e.
$+\frac{h^{2}}{12}f''''$.

---

## ★3 — Order of the five-point stencil

Moment $m=0$: $(1-8+0+8-1)/12 = 0$ ✔.
Moment $m=1$: $(1(-2) - 8(-1) + 0 + 8(1) - 1(2))/12 = (-2+8+8-2)/12 = 1$ ✔
equals $1!$.
Moment $m=2$: $(1(4) - 8(1) + 0 + 8(1) - 1(4))/12 = 0$ ✔.
Moment $m=3$: $(1(-8) - 8(-1) + 8(1) - 1(8))/12 = 0$ ✔.
Moment $m=4$: $(16 - 8 + 8 - 16)/12 = 0$ ✔.
Moment $m=5$: $(1(-32) - 8(-1) + 8(1) - 1(32))/12 = (-32+8+8-32)/12
= -48/12 = -4 \ne 0$.

Order $= 5-1 = 4$, constant $= -4/5! = -1/30$, matching the demonstration's
$h^{4}$ coefficient $-0.03333333$.

---

## ★4 — Non-symmetric three-point stencil

Offsets $[-1, 0, 0.5]$, $d=1$:

$$w_{-1}+w_0+w_{1/2} = 0,\quad -w_{-1}+0.5w_{1/2} = 1,\quad
w_{-1}+0.25w_{1/2} = 0.$$

From the third, $w_{-1} = -0.25w_{1/2}$; substituting in the second,
$0.25w_{1/2}+0.5w_{1/2} = 0.75w_{1/2} = 1$, so $w_{1/2} = 4/3 = 1.33333333$,
$w_{-1} = -1/3 = -0.33333333$ and $w_0 = -(w_{-1}+w_{1/2}) = -1$.

Order: the first surviving moment is $m = 3$,
$\sum w_i\xi_i^{3} = (-1/3)(-1) + (4/3)(0.125) = 0.3333333+0.1666667
= 0.5$, so the order is 2 and the leading constant is $0.5/3! = 1/12 = 0.08333$,
i.e. error $\approx +0.0833\,h^{2}f'''$.

---

## ★5 — A 5 % node-position error

With $\delta = 0.05$ the weights no longer sum to zero, and the leading residual
is

$$\text{error} \to \frac{\delta}{2}f'(x_0) = 0.025\,f'(x_0),$$

i.e. $2.5\,\%$ of the derivative itself. **Refinement does not remove it**: the
error is $O(1)$, not $O(h^{p})$, because the operator is inconsistent (it is
approximating $f' + 0.025f' + O(h)$ rather than $f'$). The demonstration measures
exactly this behaviour with $\delta = 0.1$: the error converges to
$0.04776682 = 0.05f'(0.3)$ and stops falling.

---

## ★6 — Why the forward difference is off by 0.6 %

The measured error is the sum of the leading term and the next:

$$e = \frac{h}{2}f'' + \frac{h^{2}}{6}f''' + O(h^{3}).$$

At $x_0 = 0.5$, $f = \sin$: $f'' = -0.47942554$, $f''' = -0.87758256$,
$h = 0.01$:

$$e = -0.002397128 - 0.000014626 + \cdots = -0.002411754.$$

Divided by $h$: $-0.2411754$; the demonstration measures $-0.2411734$. The
residual difference of $0.6\,\%$ is exactly the $h f'''/6$ term, so **halving
$h$ halves the discrepancy** — the estimate will approach $-0.2397128$ linearly,
not quadratically. That is why a first-order scheme's measured "constant"
converges slowly and should not be quoted at coarse $h$.

---

## ★7 — A stretched boundary stencil

Offsets $[0, 0.3, 0.9, 2.0]$, $d = 1$. Four unknowns, four conditions:

$$w_1+w_2+w_3+w_4 = 0,\quad
0.3w_2+0.9w_3+2w_4 = 1,$$
$$0.09w_2+0.81w_3+4w_4 = 0,\quad
0.027w_2+0.729w_3+8w_4 = 0.$$

Solving the system numerically (as the demonstration does) gives

$$w_1 = -4.94444444,\quad w_2 = +5.88235294,\quad
w_3 = -1.01010101,\quad w_4 = +0.07219251,$$

and the residual moment $\sum w_i\xi_i^{4} = 0.540000$ does not vanish, so the
first surviving moment is $m = 4$ and the **order is $4-1 = 3$**, not 2: four
nodes buy one more order than three.

**Leading constant.** $\dfrac{0.540000}{4!} = 0.0225$, so the error is
$\approx 0.0225\,h^{3}f''''$. **Verified numerically during preparation:** on
$\sin$ at $x = 0.7$, the measured error$/h^{3}$ is $0.01556$ at $h = 0.1$ and
$0.01504$ at $h = 0.05$, approaching the predicted
$0.0225\sin(0.7) = 0.014495$ from above as the $O(h^{4})$ term decays — the
stencil behaves as an order-3 operator. For scale, at $h = 0.05$ its error is
$0.0225\,h^{3}|f''''| = 1.8\times10^{-6}$, against
$\frac{h^{2}}{6}|f'''| = 3.7\times10^{-4}$ for the uniform three-point stencil
on the same function: a factor of about $200$, which is what the extra node and
the extra order buy.

**Polynomial exactness.** Applying the weights to $x^{1}$, $x^{2}$, $x^{3}$
reproduces $1$, $2x$, $3x^{2}$ to round-off; $x^{4}$ is the first failure, which
is the same statement as the moment count above.

---

## ★8 — Is the reported order credible?

**Analysis.** A transform error of $10^{-6}$ relative displaces nodes by
$10^{-6}h$. That is a *node-position* error of $\delta \sim 10^{-6}$, whose
leading effect on a first-derivative stencil is
$\frac{\delta}{2}f' \approx 5\times10^{-7}f'$ — an $O(1)$ inconsistency, but a
tiny one. The stencil's truncation error at $h$ is $\sim c\,h^{p}f^{(p+1)}$; for
$p = 2$ and $h = 10^{-2}$, that is $\sim10^{-4}$ — much larger than
$5\times10^{-7}$. So the transform error is irrelevant until $h$ is small enough
that $c\,h^{2}\lesssim5\times10^{-7}$, i.e. $h\lesssim2\times10^{-3}$: at that
point the reported order collapses to zero.

**Diagnostic.** Run a refinement sequence past $h\approx2\times10^{-3}$ and watch
the error: if it stops falling and settles at $\sim5\times10^{-7}f'$, the
transform, not the scheme, is what is being measured. The fix is to compute the
stencil weights from the *actual* node positions (or to generate both the grid and
the weights from the same exact transform), exactly as §3.4 of the lesson shows.
