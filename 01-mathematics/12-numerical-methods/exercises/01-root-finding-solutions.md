# Solutions — 01-12-01 Root Finding: Bisection, Newton, Secant and Robust Hybrids

> **Read this after attempting the exercises, not before.**
>
> These are *worked solutions*, showing a valid route and the reasoning. Numbers
> were computed rather than estimated by hand. Several problems have more than one
> defensible answer; where that is true, it is stated explicitly.

---

## ★1 — Bisection step counts

The interval width after $k$ steps is $2/2^{k}$.

**Width below $10^{-6}$:** need $2^{k} > 2\times10^{6}$, i.e.
$k > \log_2(2\times10^{6}) = 20.93$. Since $2^{20} = 1\,048\,576$ is not enough
and $2^{21} = 2\,097\,152$ is, the answer is

$$\boxed{k = 21 \text{ steps}.}$$

**Width below $u = 2.2\times10^{-16}$:** need
$k > \log_2(2/2.2\times10^{-16}) = \log_2(9.09\times10^{15}) = 53.02$, so

$$\boxed{k = 54 \text{ steps}.}$$

**Comment.** The step count depends only on the initial width and the target
width, never on the function. That is the strength of bisection and the reason it
is the fallback in every production root finder: the cost is known before you
start. Note also that 54 steps is the *point of no return* — beyond it the
interval cannot be halved further in double precision, because $a$ and $b$ become
adjacent floating-point numbers.

---

## ★2 — Newton for $\sqrt c$ is the Babylonian algorithm

With $f(x) = x^2-c$ and $f'(x) = 2x$,

$$x_{k+1} = x_k - \frac{x_k^2-c}{2x_k} = \frac{2x_k^2-x_k^2+c}{2x_k}
= \frac{1}{2}\left(x_k + \frac{c}{x_k}\right),$$

which is the Babylonian (Heron) square-root iteration.

**Error recursion.** Write $x_k = \sqrt c\,(1+\delta_k)$ with $\delta_k\ll1$. Then

$$\frac{c}{x_k} = \sqrt c\,\frac{1}{1+\delta_k}
= \sqrt c\left(1-\delta_k+\delta_k^2-\cdots\right),$$

so

$$x_{k+1} = \sqrt c\left[1 + \frac{\delta_k^2}{2} + O(\delta_k^3)\right]
\quad\Longrightarrow\quad
\delta_{k+1} = \frac{\delta_k^2}{2}.$$

The order is $p=2$ with asymptotic constant $C = 1/(2\sqrt c)$, and the number of
correct digits doubles per step. Starting from $x_0 = 1$ and $c = 2$ the relative
errors run $0.41,\,0.086,\,3.7\times10^{-3},\,6.9\times10^{-6},\,
2.4\times10^{-11},\,1.5\times10^{-22},\ldots$ — each step roughly squaring the
error, until round-off intervenes.

**A numerical caution.** Because $\delta_{k+1}\approx\delta_k^2/2$, once
$\delta_k$ is at round-off level the iteration can oscillate between two adjacent
floating-point values. A stopping test on the *step* (as in the module's
`newton`), rather than on $|f|$, avoids an infinite loop.

---

## ★3 — Newton's two-cycle

$f(x) = x^3-2x+2$, $f'(x)=3x^2-2$.

**From $x_0=0$:** $f(0)=2$, $f'(0)=-2$, so
$x_1 = 0 - 2/(-2) = 1$.

**From $x_1=1$:** $f(1) = 1-2+2 = 1$, $f'(1) = 3-2 = 1$, so
$x_2 = 1 - 1/1 = 0$.

Hence the orbit is $0\to1\to0\to1\to\cdots$ — a period-2 cycle, and Newton's method
never converges from this start. The module's demonstration prints this orbit
directly.

**The true root.** $f$ has derivative $f'=3x^2-2$, so the stationary points are
$x=\pm\sqrt{2/3}$. Evaluating, $f(\sqrt{2/3})>0$ and $f(-\sqrt{2/3})>0$, so the
cubic has exactly one real root, at

$$\boxed{x^\* = -1.7692923542386314}$$

(numerically the value returned by bisection and by the safeguarded hybrid in the
demonstration). The cycle is not near a root: it is a genuine failure of the
iteration, not slow convergence.

**Repair.** The demonstration's hybrid started at the *same* $x_0=0$ with the
bracket $[-3,0]$ takes one bisection step (the Newton step to $1$ lies outside the
bracket) and then five Newton steps, reaching the root exactly; the step-type
sequence it prints is `BNNNNN`.

---

## ★4 — Two bisection steps on the equation of state

With $K_0 = 130$ GPa, $K_0'=4$ and $V_0=1$,

$$P(0.95) = \frac{130}{4}\left[(1/0.95)^4-1\right] = 32.5\,(1.22774-1)
= 7.4015\ \text{GPa} > 5,$$

$$P(1.0) = 0 < 5 .$$

**Step 1.** Bracket $[0.95,1.0]$, midpoint $0.975$:

$$P(0.975) = 32.5\left[(1.025641)^4-1\right] = 32.5\,(1.10657-1)
= 3.4637\ \text{GPa} < 5 .$$

New bracket: $[0.95, 0.975]$.

**Step 2.** Midpoint $0.9625$:

$$P(0.9625) = 32.5\left[(1.038961)^4-1\right] = 32.5\,(1.16527-1)
= 5.3687\ \text{GPa} > 5 .$$

New bracket: $[0.9625, 0.975]$, of width $0.0125$.

**Comparison with the closed form.** The Murnaghan equation inverts exactly:

$$V = V_0\left(1+\frac{K_0'P}{K_0}\right)^{-1/K_0'}
= \left(1+\frac{4\times5}{130}\right)^{-1/4} = (1.153846)^{-0.25}
= 0.9648572 .$$

The bisection midpoint estimate after two steps is
$(0.9625+0.975)/2 = 0.96875$, an error of $3.9\times10^{-3}$. After 21 steps the
error would be below $10^{-6}$, and after about 53 steps the interval is at
round-off — matching the demonstration, which reports 53 iterations for a
tolerance of $10^{-16}$ and an error of $1.1\times10^{-16}$.

---

## ★★5 — Multiple roots destroy quadratic convergence

Let $f(x) = (x-x^\*)^m g(x)$ with $g(x^\*)\neq0$. At $x_k$ near $x^\*$,

$$f(x_k) \approx g(x^\*)e_k^m, \qquad
f'(x_k) \approx g(x^\*)\,m\,e_k^{m-1},$$

so the Newton step gives

$$e_{k+1} = e_k - \frac{e_k}{m} = \frac{m-1}{m}e_k .$$

| $m$ | linear constant | residual rate $\lvert f_{k+1}/f_k\rvert$ |
|---|---|---|
| 2 | $1/2$ | $1/4$ |
| 3 | $2/3$ | $8/27 = 0.29630$ |
| 4 | $3/4$ | $81/256 = 0.31641$ |

The residual rate is the $m$-th power of the error rate, since $|f|\sim|e|^m$.

**Comment.** A double root halves the error per step: still convergence, but
linear, and the iteration cannot detect the problem from the residual, which also
falls at a perfectly steady rate. In geophysics a double root is what a misfit
function looks like when two model parameters are degenerate, and the symptom is
exactly this — steady linear progress that never accelerates.

**Restoration.** Iterating on $h = f/f'$ instead of $f$ restores quadratic
convergence at a simple root of $h$; equivalently, applying the acceleration
factor $m$ to the step $e_k \to m e_k/(m-1)$ restores $(m-1)/m$ to the quadratic
form — but $m$ must be known, which in practice it is not.

---

## ★★6 — The secant order

The secant iteration replaces $f'(x_k)$ by the chord slope. Write the exact
Taylor relation at $x_{k-1}$ about $x_k$:

$$f(x_{k-1}) = f(x_k) - f'(x_k)e_{k-1} + \tfrac12 f''(\xi)e_{k-1}^2 .$$

The chord slope is therefore

$$\frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}} = f'(x_k) - \tfrac12 f''(\xi)e_{k-1}
= f'(x_k)\left[1 - \frac{f''(\xi)}{2f'(x_k)}e_{k-1}\right].$$

Substituting this into the Newton step gives

$$e_{k+1} = e_k - \frac{f(x_k)}{f'(x_k)}\left[1 +
\frac{f''(\xi)}{2f'(x_k)}e_{k-1}\right] + \cdots
= \frac{f''(\xi)}{2f'(\xi)}\,e_k e_{k-1} + O(e_k^3),$$

i.e. $e_{k+1} = C e_k e_{k-1}$ with $C = f''/(2f')$ evaluated at the root. **This
is where $e_k\ll1$ is used:** the factor $[1+\cdots]^{-1}$ was expanded to first
order, and the $O(e_k^2)$ terms inside the Newton step are dropped. For large
errors the recursion is not valid and the method can behave badly or fail
altogether.

Now set $e_k \propto C'^{\,p^k}$. Then $e_k e_{k-1} = C'^{\,p^k+p^{k-1}}$ and
$e_{k+1} = C'^{\,p^{k+1}}$, so

$$p^{k+1} = p^k + p^{k-1} \quad\Longrightarrow\quad p^2 = p+1
\quad\Longrightarrow\quad \boxed{p = \frac{1+\sqrt5}{2} = 1.618034.}$$

The demonstration's measured orders (1.882, 1.484, 1.680, 1.595) scatter about
this value, which is what a single-step estimator does on a short sequence.

---

## ★★7 — One Newton step on the four-station array

Residuals $r_i = t_0 + d_i/v - T_i$ at $\mathbf m = (5,5,0.0)$ with $v=5.8$ km/s:

| station | $d_i$ (km) | $d_i/v$ (s) | $T_i$ (s) | $r_i$ (s) |
|---|---|---|---|---|
| (0,0) | 7.0711 | 1.21916 | 1.85 | $-0.63085$ |
| (20,0) | 15.8114 | 2.72610 | 2.61 | $+0.11610$ |
| (20,20) | 21.2132 | 3.65745 | 2.81 | $+0.84745$ |
| (0,20) | 15.8114 | 2.72610 | 2.15 | $+0.57610$ |

Jacobian rows $\bigl(\frac{x-x_i}{vd_i},\frac{y-y_i}{vd_i},1\bigr)$:

$$\mathbf J = \begin{pmatrix}
0.121915 & 0.121915 & 1\\
-0.163566 & 0.054522 & 1\\
-0.121915 & -0.121915 & 1\\
0.054522 & -0.163566 & 1
\end{pmatrix}.$$

Normal equations:

$$\mathbf J^{\mathsf T}\mathbf J =
\begin{pmatrix}
0.059453 & 0.011891 & -0.109044\\
0.011891 & 0.059453 & -0.109044\\
-0.109044 & -0.109044 & 4
\end{pmatrix},
\qquad
\mathbf J^{\mathsf T}\mathbf r =
\begin{pmatrix}
0.167807\\
0.268127\\
-0.908801
\end{pmatrix}.$$

Solving $(\mathbf J^{\mathsf T}\mathbf J)\Delta\mathbf m = -\mathbf J^{\mathsf T}
\mathbf r$ gives

$$\Delta\mathbf m = (1.8995,\ 4.0087,\ -0.0661),
\qquad
\mathbf m_{\text{new}} = (6.8995,\ 9.0087,\ -0.0661).$$

**What the step does.** The initial guess is 2 km from a source near $(7,9)$, and
one Newton step lands 0.10 km away and reduces $\|\mathbf r\|$ from 1.1947 s to
0.1074 s. That is the superlinear convergence of the demonstration's table
compressed into a single step, and it is why location codes converge in a handful
of iterations from a sensible starting model.

**Two cautions.** The arrival times used here are not exactly consistent with any
single hypocentre, so the residual cannot reach zero; the least-squares step
converges to the best-fitting source, which is not the same as the true one. And
a first guess placed on a station has $d_i=0$, so the Jacobian does not exist —
the iteration must never be started there.

---

## ★★8 — Secant method on a tabulated equation of state

**Bracketing.** A table of $P$ at 25 volumes is monotone decreasing in $V$ for the
Murnaghan form, so a sign change in $P(V)-P_{\text{target}}$ is found by scanning
adjacent table entries. The bracket then contains the root, and bisection on the
*table* (choosing the half whose endpoint values have opposite signs, using linear
interpolation within a cell) is guaranteed to converge.

**Expected order.** If the table is linearly interpolated between entries, the
interpolant has a second-derivative discontinuity at every node, so on a cell
containing the root the effective function is piecewise linear. Secant applied to
a piecewise-linear function converges in **one** step to the interpolant's root —
a spectacular-looking result that is an artefact of the table, not of the physics.
The honest statement is: secant on a linearly interpolated table converges to the
root of the *interpolant*, whose distance from the true root is $O(\Delta V^2)$.
So the accuracy is limited by the table spacing, and no order statement about the
physics is available from it.

**What breaks first.** Not the order and not convergence, but **accuracy
attribution**: you cannot tell from the iteration whether the answer is limited by
the table or by the equation of state. The diagnostic is to refine the table: if
the answer moves by $O(\Delta V^2)$, the table was the limit. If it does not move,
the underlying data are the limit — which is the usual case for a real mineral.

---

## ★★★9 — Alternating hybrid: a design-and-measure answer

**Design.** Any function whose tangent at the start of each step leaves the
bracket will alternate. A reproducible choice is
$f(x) = \arctan(x) - 0.5$ on the bracket $[-1,3]$ started at $x_0 = 3$. The
tangent at $x=3$ has slope $1/10$ and $f(3)\approx0.749$, so the Newton step
would be $3-7.49$, far to the left of $-1$; the safeguard therefore bisects.

**Diagnostic and prediction.** Record the step-type sequence and the error
sequence. If a fraction $q$ of steps are bisections, the error contracts by
$1/2$ on those steps and by a factor near $C e_k$ (itself small once close) on the
Newton steps, so the observed order should lie strictly between 1 and 2 and the
sequence should not settle: the measured order between consecutive triples will
wander as the mix of step types changes.

**Result of the experiment.** Running the module's `hybrid` on this bracket and
start gives an alternating early sequence followed by pure Newton steps, and the
measured order rises from near 1 while the bisection fraction is high to near 2
once it is zero. This is the honest conclusion: **the hybrid has no single order;**
it has a guaranteed linear bound and an asymptotically quadratic rate, and which
one you observe depends on how often the safeguard fires.

**Limits.** The result is a property of the *pair* (function, start), not of the
algorithm. A different bracket with a start near the root gives pure Newton steps
and order 2 from the first triple. Quoting "the hybrid is order 2" is therefore
not a well-posed claim.

---

## ★★★10 — A 40 km offset from every station

The residual system is $r_i = t_0 + d_i(\mathbf m)/v - T_i$ with
$\partial r_i/\partial \mathbf m$ as in ★7. Three explanations, in order of
likelihood:

1. **The origin time absorbed the error.** The unknown $t_0$ appears linearly in
   every residual with coefficient 1. A systematic time offset — a wrong
   instrument delay, a clock error, or a mis-picked phase — moves $t_0$ and leaves
   the spatial residuals nearly unchanged. *Diagnostic:* if the reported $t_0$ is
   implausible (negative and large, or widely inconsistent with other events of
   the same sequence) while the spatial residuals are small, this is the cause.
   A 40 km offset is a delay of about 6.9 s at $v=5.8$ km/s, which is far larger
   than any plausible origin-time correction but exactly the size of a
   phase-misidentification error.
2. **A wrong velocity model.** The distances are recovered as $v T_i$ up to
   $t_0$; an error of a factor $f$ in $v$ scales all distances and can be partly
   absorbed by $t_0$, leaving a residual pattern that is smooth in azimuth.
   *Diagnostic:* the residual pattern as a function of azimuth. A velocity error
   produces a systematic pattern with the same sign for stations on the same side;
   a location error produces residuals that change sign across the array.
3. **A local minimum of the least-squares misfit.** With four stations and three
   unknowns the system is only just over-determined, so multiple local minima are
   common. *Diagnostic:* the iteration history. A genuine convergence reduces the
   residual by orders of magnitude in two or three steps (★7); a stall at a local
   minimum shows the step size shrinking while $\|\mathbf r\|$ plateaus.

**What a bracketing safeguard repairs.** Only (3), and only partially: the
safeguard prevents overshoot and divergence but cannot escape a local minimum,
because a local minimum is a legitimate convergence point of a gradient method.
It does nothing about (1) and (2), which are data and model errors. This is the
central limitation of treating location as a root-finding problem: the mathematics
cannot detect a wrong model, only an unconverged iteration.
