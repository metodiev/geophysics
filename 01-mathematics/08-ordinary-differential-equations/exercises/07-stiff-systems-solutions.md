# Solutions — 01-08-07 Stiff Systems and Numerical Stability Challenges

> **Read this after attempting the exercises, not before.** Every rate, ratio,
> step limit and iteration count below was computed; where a number depends on a
> modelling assumption (such as a machine speed) the assumption is stated where
> it is used.

---

## ★1 — Stiffness of a one-dimensional diffusion problem

$\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, $L = 1$ m, so
$\lambda_{\min} = \kappa\pi^{2}/L^{2} = 9.869604\times10^{-6}\ \mathrm{s^{-1}}$
and the physical decay time is $1/\lambda_{\min} = 1.0132\times10^{5}$ s
$= 1.17$ d.

| $N$ | $\Delta x$ (m) | $\lambda_{\max}$ (s⁻¹) | $S$ | $2/\lambda_{\max}$ (s) | steps per decay time |
|---|---|---|---|---|---|
| 100 | $9.9010\times10^{-3}$ | $4.0804\times10^{-2}$ | $4.134\times10^{3}$ | 49.015 | 2067 |
| 400 | $2.4938\times10^{-3}$ | $6.4320\times10^{-1}$ | $6.517\times10^{4}$ | 3.109 | 32 585 |
| 1000 | $9.9900\times10^{-4}$ | $4.0080\times10^{0}$ | $4.061\times10^{5}$ | 0.499 | 203 048 |

**(b)** The scaling is quadratic in $N$ in both factors: $\lambda_{\max}\propto
\Delta x^{-2}\propto N^{2}$ (so the step limit falls as $N^{-2}$), and
$\lambda_{\min}$ is *independent* of $N$ for a fixed domain (so the number of
steps per physical decay time, $S$, grows as $N^{2}$). The table bears it out:
from $N = 100$ to $N = 400$ the ratio $S$ grows by $16.0$ against
$4^{2} = 16$ ✓, and from 400 to 1000 by $6.23$ against $2.5^{2} = 6.25$ ✓. **Every
factor-of-two refinement of a diffusion grid quadruples the cost of an explicit
integration over a fixed physical time — before any accuracy requirement is
considered.**

---

## ★2 — Amplification factors

| $z$ | $\exp(z)$ | explicit Euler | implicit Euler | trapezoidal |
|---|---|---|---|---|
| $-0.5$ | $0.606531$ | $0.500000$ | $0.666667$ | $0.600000$ |
| $-1$ | $0.367879$ | $0.000000$ | $0.500000$ | $0.333333$ |
| $-2$ | $0.135335$ | $-1.000000$ | $0.333333$ | $0.000000$ |
| $-5$ | $0.006738$ | $-4.000000$ | $0.166667$ | $-0.428571$ |
| $-100$ | $3.720\times10^{-44}$ | $-99.000000$ | $0.009901$ | $-0.960784$ |

**(a)** Explicit Euler is stable while $|1+z|\le1$, i.e. on the disc of radius
1 centred at $z = -1$: $-2\le z\le0$ on the negative real axis. The table shows
$|R| = 1$ at $z = -2$ (the boundary), $|R| = 4$ at $z = -5$ and $|R| = 99$ at
$z = -100$.

**(b)** **Implicit Euler is A-stable**: $|R(z)| = |1/(1-z)|<1$ for every $z$
with $\operatorname{Re}z<0$, because $|1-z|\ge1$ there — and the table shows
$|R|$ decreasing monotonically ($0.667$, $0.5$, $0.333$, $0.167$, $0.0099$).
**The trapezoidal rule is also A-stable**:
$|R| = |(1+z/2)/(1-z/2)| = 1$ on the imaginary axis and less than 1 in the open
left half plane.

**(c)** **Only implicit Euler is L-stable.** As $z\to-\infty$,
$R_{\text{imp}}\to0$ like $1/|z|$ (table: $0.0099$ at $z = -100$), while
$R_{\text{trap}}\to-1$ (table: $-0.960784$ at $z = -100$). The trapezoidal rule
therefore does not damp a very fast mode; it preserves it with alternating sign.
**The table's last column is the whole distinction in one row.**

---

## ★3 — Is the problem stiff?

Stiffness is a statement about the ratio of timescales *present* against the
timescales *of interest*, so the same system can be stiff for one run and not for
another.

**(a)** $S = 200/0.1 = 2000$. **Yes, stiff**: the fast mode is three decades
faster than the slow one, and resolving it explicitly is not worth it.
**(b)** Over one month the slow mode is barely started; the run has to cover
$10$ fast decay times and $0.005$ slow ones. **Not stiff for this run**: the
interval is of the same order as the fast timescale, so an explicit method must
resolve it anyway and pays no penalty.
**(c)** $S = 10^{6}$. **Yes, stiff**: the interval is $10^{7}$ fast timescales and
10 slow ones.
**(d)** $S = 10^{6}$ still, but the interval is $10^{-5}$ s $= 10$ fast
timescales. **Not stiff for this run**: the fast modes are the physics of
interest. The *system* is stiff; the *problem* is not.

**The lesson of (b) and (d): stiffness is not a property of a system alone, but
of a system together with the interval you need to integrate over.** A code that
switches to an implicit method purely because the rate constants span many
decades will waste time on a short run.

---

## ★★4 — Cost scaling for a two-dimensional aquifer

$D = T/S = 10\ \mathrm{m^{2}\,s^{-1}}$, $L = 4000$ m, so
$\lambda_{\min} = 2D\pi^{2}/L^{2} = 1.233701\times10^{-5}\ \mathrm{s^{-1}}$ and
the physical decay time is $8.1057\times10^{4}$ s $= 0.938$ d.

**(a)**

| $\Delta x$ (m) | $N$ | nodes | $\lambda_{\max}$ (s⁻¹) | $S$ | $2/\lambda_{\max}$ (s) | steps per decay time | node-updates |
|---|---|---|---|---|---|---|---|
| 100 | 40 | 1 600 | $4.00\times10^{-3}$ | $3.242\times10^{2}$ | 500.0 | 162 | $2.59\times10^{5}$ |
| 25 | 160 | 25 600 | $6.40\times10^{-2}$ | $5.188\times10^{3}$ | 31.25 | 2594 | $6.64\times10^{7}$ |
| 6.25 | 640 | 409 600 | $1.024\times10^{0}$ | $8.300\times10^{4}$ | 1.953 | 41 501 | $1.70\times10^{10}$ |

**(b)** Both factors scale as $\Delta x^{-2}$: the explicit step limit is
$2/\lambda_{\max}\propto\Delta x^{2}$, so the number of *steps* per fixed
physical time grows as $\Delta x^{-2}$; and the number of *nodes* for a fixed
domain grows as $\Delta x^{-2}$. Their product therefore grows as
$\Delta x^{-4}$. The table confirms it: reducing $\Delta x$ by a factor of 4
multiplies the step count by $16.0$ and the update count by $256 = 4^{4}$ ✓.

**(c)** An implicit scheme with $\Delta t = 0.1$ d $= 8640$ s takes
$8.1057\times10^{4}/8640 = 9.4\approx10$ steps per decay time. Multiplying by the
node counts and by a generous $10^{2}$–$10^{3}$ node-operations per unknown for
the solve gives

| $\Delta x$ | implicit node-operations (lower–upper) | explicit node-updates | winner |
|---|---|---|---|
| 100 m | $1.6\times10^{6}$ – $1.6\times10^{7}$ | $2.59\times10^{5}$ | explicit |
| 25 m | $2.6\times10^{7}$ – $2.6\times10^{8}$ | $6.64\times10^{7}$ | comparable |
| 6.25 m | $4.1\times10^{8}$ – $4.1\times10^{9}$ | $1.70\times10^{10}$ | implicit, by 4–40× |

**The crossover is between 100 m and 25 m.** On a coarse grid the explicit
scheme is genuinely cheaper — a solve per step is real work — and on a fine grid
the implicit scheme wins by more than an order of magnitude, with the margin
growing as $\Delta x^{-4}$ divided by the (much weaker) growth of the solve cost.

**(d)** Stability is not accuracy. The implicit run used $\Delta t = 8640$ s,
which is $2.8\times10^{4}$ times larger than the explicit limit at
$\Delta x = 25$ m; backward Euler is unconditionally stable but only first-order
accurate, so the answer is trustworthy only if the solution varies little over
one step. **The check is a convergence study in $\Delta t$** — run with
$\Delta t$ and $\Delta t/2$ (or with backward Euler and Crank–Nicolson) and
confirm that the difference is below the required tolerance. Nothing about
stability tells you the answer is right.

---

## ★★5 — Trapezoidal versus implicit Euler on a very fast mode

$\lambda = 1000$, $h = 1$, so $z = -1000$; $\exp(-1000) = 0$ to every double
precision digit.

**(a)** $R_{\text{trap}} = (1+z/2)/(1-z/2) = (1-500)/(1+500) = -0.996008$ and
$R_{\text{imp}} = 1/(1-z) = 1/1001 = 9.99001\times10^{-4}$.

**(b)**

| $n$ | $t$ | trapezoidal | implicit Euler | exact |
|---|---|---|---|---|
| 1 | 1 | $-9.96008\times10^{-1}$ | $9.99001\times10^{-4}$ | $0$ |
| 10 | 10 | $9.60789\times10^{-1}$ | $9.90055\times10^{-31}$ | $0$ |
| 50 | 50 | $8.18731\times10^{-1}$ | $9.51253\times10^{-151}$ | $0$ |
| 100 | 100 | $6.70320\times10^{-1}$ | $9.04883\times10^{-301}$ | $0$ |

**(c)** Recommend **implicit Euler**, despite its lower order. The deciding
property is **L-stability**: $R_{\text{imp}}(z)\to0$ as $z\to-\infty$, so the
fast mode is annihilated in one step, whereas
$R_{\text{trap}}\to-1$ leaves it oscillating with almost undiminished
magnitude — after 100 steps the trapezoidal solution is still at $0.67$ while
the exact answer is $10^{-434}$. **Order is an accuracy statement about the
asymptotic regime $z\to0$, and here $|z| = 1000$: the regime is not asymptotic,
and the order comparison is irrelevant.** Had the fast mode been the physics of
interest, the conclusion would reverse; it is the fact that the fast mode is
*irrelevant* (and must be damped away) that makes the L-stable first-order method
the right tool.

---

## ★★6 — A non-linear stiff problem

**(a)** Separating $dy/y^{3} = -10\,dt$ and integrating,
$-1/(2y^{2}) = -10t+C$. With $y(0) = 1$, $C = -1/2$, so
$1/(2y^{2}) = 10t+1/2$ and

$$y(t) = \frac{1}{\sqrt{20t+1}}, \qquad
y(1) = \frac{1}{\sqrt{21}} = 0.218217890 .$$

**(b)** Backward Euler is
$y_{n+1} = y_n + h\left(-10y_{n+1}^{3}\right)$, i.e.

$$y_{n+1}^{3}+y_{n+1}-y_n = 0 \qquad (h\lambda = 1),$$

a **cubic** in $y_{n+1}$ — and a cubic can be solved in closed form, but Newton is
what a general code does.

**(c)** With $y_0 = 1$ the first step solves $y^{3}+y-1 = 0$, whose root is
$y_1 = 0.682327804$ (Newton from $y_0 = 1$: $F = 1$, $F' = 4$, step $-0.25$;
then $F(0.75) = 0.171875$, $F' = 2.6875$, step $-0.06395$; …). The full
sequence over $[0,1]$ with $h = 0.1$:

| $n$ | $y_n$ |
|---|---|
| 0 | 1.000000 |
| 1 | 0.682328 |
| 2 | 0.531870 |
| 3 | 0.444214 |
| 4 | 0.386485 |
| 5 | 0.345310 |
| 6 | 0.314271 |
| 7 | 0.289906 |
| 8 | 0.270183 |
| 9 | 0.253829 |
| 10 | 0.240004 |

Newton converged to a $10^{-14}$ relative tolerance in an average of **4.8
iterations** (worst case 6) per step. The final value $0.240004$ is 10.0 % above
the exact $0.218218$ — the expected first-order error for $h = 0.1$ on a solution
that varies on a timescale of order $1/(3\lambda y^{2})\approx0.03$ at early
times.

**(d)** Explicit Euler with $h = 0.1$ gives $y_1 = 1 + 0.1(-10) = 0$, and the
iteration then stays at zero for ever: **the scheme collapses to the trivial
solution in a single step.** For smaller steps it behaves properly but slowly:

| $h$ | $y(1)$ from explicit Euler | error |
|---|---|---|
| 0.10 | 0.000000 | 100 % |
| 0.05 | 0.202297 | 7.3 % |
| 0.02 | 0.213244 | 2.3 % |
| 0.01 | 0.215798 | 1.1 % |

The linearised stability limit is $h<2/(3\lambda y^{2})$, which at $y = 1$ is
$h<0.0667$ — and $h = 0.1$ exceeds it. **The failure mode is different from the
linear test problem: instead of blow-up with alternating sign, the scheme
collapses to the spurious-looking value zero.** The reason is that the
non-linearity is *stabilising*: once $y$ is too small, the right-hand side
$(-10y^{3})$ is tiny and the iteration freezes. **A stiff solver's diagnostics
based on "is the solution growing?" will not detect this failure at all** — the
solution is bounded, smooth and wrong by 100 %.

---

## ★★★7 — The fast timescale of the Robertson system

**(a)** The Jacobian is

$$\frac{\partial\mathbf{f}}{\partial\mathbf{y}} =
\begin{pmatrix}
-k_1 & k_3y_3 & k_3y_2\\
k_1 & -k_3y_3-2k_2y_2 & -k_3y_2\\
0 & 2k_2y_2 & 0
\end{pmatrix}.$$

The fast timescale comes from $J_{22}$, specifically the term $-2k_2y_2$ (from
$-k_2y_2^{2}$) and the term $-k_3y_3$ (from the reversible step). Their sum sets
the rate.

**(b)** At $t = 40$ with $y_2 = 9.2\times10^{-6}$ and $y_3 = 0.284$:

$$k_3y_3 = 10^{4}\times0.284 = 2.84\times10^{3}, \qquad
2k_2y_2 = 2\times3\times10^{7}\times9.2\times10^{-6} = 5.52\times10^{2},$$

so $J_{22} = -3.392\times10^{3}$ and the trace is
$-0.04-3392-0 = -3392.04$. **Since the trace equals the sum of the eigenvalues,
one eigenvalue of magnitude $\approx3.4\times10^{3}$ accounts for essentially the
entire trace**, leaving the other two of order $10^{-2}$ and smaller. A
power-iteration estimate on the full matrix gives the dominant eigenvalue as
$-3392.02$, consistent with that reasoning. The stiffness ratio against the slow
rate $k_1 = 0.04$ is therefore

$$S \approx \frac{3392}{0.04} = 8.5\times10^{4} .$$

**(c)** The explicit step limit is $h<2/3392 = 5.9\times10^{-4}$ s. The lesson's
run used $h = 0.01$ s, which is **17 times over the limit** — which is exactly
why explicit Euler fails at both $h = 0.01$ and $h = 0.1$ while the implicit
method succeeds. Note also that the estimate is at $t = 40$: at $t = 0$ both
$y_2$ and $y_3$ vanish, the fast eigenvalue is absent, and an explicit method
starts off perfectly happy. **The stiffness appears as the solution evolves, so
a stability estimate must be made along the trajectory, not only at the initial
condition.**

**(d)** Both methods are first order, so their *asymptotic* accuracy is
identical; the difference is where their stability limits sit. Implicit Euler's
limit is empty — it has none — so $h = 0.1$ is permitted and the error is the
ordinary $O(h)$ truncation error (which is why halving $h$ halves the error, as
the lesson's table shows). Explicit Euler's limit is $h<5.9\times10^{-4}$, so
$h = 0.1$ is not merely inaccurate but outside the region where the scheme
converges at all: the fast eigenvalue makes the iteration diverge. **Stiffness
is the gap between the step the method needs for stability and the step its
accuracy needs; when the gap is 10² or more, only a method without a stability
limit can exploit the accuracy requirement.**

---

## ★★★8 — Choosing a scheme for a three-dimensional diffusion problem

**(a)** $L = 1000$ m, $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, so

$$\lambda_{\min} = \frac{3\kappa\pi^{2}}{L^{2}} = 2.9609\times10^{-11}\ \mathrm{s^{-1}},
\qquad \tau = 1/\lambda_{\min} = 3.378\times10^{10}\ \mathrm{s}.$$

For $N = 100$ ($\Delta x = 10$ m):
$\lambda_{\max} = 12\kappa/\Delta x^{2} = 1.2\times10^{-7}\ \mathrm{s^{-1}}$,
$\Delta t_{\max} = 2/\lambda_{\max} = 1.6667\times10^{7}$ s, steps per $\tau$ =
$3.378\times10^{10}/1.6667\times10^{7} = 2026$, nodes $= 10^{6}$, node-updates
$= 2.03\times10^{9}$. For $N = 400$ ($\Delta x = 2.5$ m):
$\lambda_{\max} = 1.92\times10^{-6}$, $\Delta t_{\max} = 1.0417\times10^{6}$ s,
steps per $\tau = 32\,423$, nodes $= 6.4\times10^{7}$, updates
$= 2.08\times10^{12}$. Both agree with the table.

**(b)** Steps per decay time $\propto\Delta t_{\max}^{-1}\propto\Delta x^{-2}$, and
nodes $\propto\Delta x^{-3}$; the product goes as $\Delta x^{-5}$. Check:
halving $\Delta x$ multiplies the update count by $2^{5} = 32$; from
$6.33\times10^{7}$ to $2.03\times10^{9}$ is a factor $32.0$ ✓, and from
$6.49\times10^{10}$ to $2.08\times10^{12}$ is $32.0$ ✓. **In three dimensions
the cost of an explicit diffusion integration per physical decay time grows as
the fifth power of the refinement ratio** — one of the strongest arguments for
implicit methods in geophysical modelling.

**(c)** With the stipulated $10^{8}$ node-updates per second:

| $\Delta x$ (m) | node-updates per $\tau$ | run time per $\tau$ |
|---|---|---|
| 20 | $6.3\times10^{7}$ | 0.63 s |
| 10 | $2.0\times10^{9}$ | 20 s |
| 5 | $6.5\times10^{10}$ | 11 min |
| 2.5 | $2.1\times10^{12}$ | 5.8 h |

The finest grid inside a one-hour budget is $\Delta x = 5$ m; $\Delta x = 2.5$ m
misses by a factor of six. **The assumption is stated rather than measured**: a
real code's throughput depends on its memory access pattern, vectorisation and
parallelism, so treat these as order-of-magnitude figures.

**(d)** Reasoning, one scheme at a time:

- **(i) Explicit Euler — reject.** Its step limit at $\Delta x = 5$ m is
  $4.17\times10^{6}$ s and the run needs 8106 steps, consuming 11 minutes per
  decay time of the *fastest* mode; if the physical time of interest is many
  decay times of the *domain*, the cost multiplies accordingly, and the
  $\Delta x^{-5}$ scaling means any refinement is fatal. It is also only
  first-order accurate, so its error is the largest of the four.
- **(ii) Backward Euler with a multigrid solve — accept.** It is
  unconditionally stable and L-stable, so the grid-scale modes are damped
  rather than resolved; the step can be chosen from accuracy alone, e.g.
  $\Delta t\sim\tau/50 = 6.8\times10^{8}$ s, which is 160 times larger than the
  explicit limit at $\Delta x = 5$ m. The cost is one multigrid solve per step
  (a few hundreds of node-operations per unknown), which for 8000 steps of
  $8\times10^{6}$ nodes is $O(10^{12})$ operations — large, but reducible
  further because the *first-order* accuracy may permit an even larger step.
- **(iii) Crank–Nicolson — accept with care.** It is second-order accurate and
  A-stable, so it gives far better accuracy per step; but it is **not
  L-stable**, and on a diffusion problem with a sharp initial condition it can
  produce negative values (Section 3.4 of the lesson). The usual practice is to
  start with a few backward-Euler steps to smooth the initial data and then
  switch to Crank–Nicolson.
- **(iv) IMEX — accept if the problem has a non-stiff part.** Splitting the
  linear diffusion implicitly and an advective or reactive term explicitly is
  efficient *provided* the explicit term is not the stiff one; putting a stiff
  reaction on the explicit side reimposes exactly the limit the split was meant
  to remove.

**(e)** **Explicit Euler should be rejected on accuracy grounds as well as
stability grounds**, and the distinction matters: even if a machine were fast
enough to take the 8106 steps, the method is first order, so the error falls
only linearly with the step. Crank–Nicolson is the one to prefer for accuracy;
backward Euler is the safe default. Rejecting explicit Euler for stability alone
would understate the problem.

**(f)** The one calculation to do first is **the eigenvalue estimate**: compute
$\lambda_{\max}\approx12\kappa/\Delta x^{2}$ and
$\lambda_{\min}\approx3\kappa\pi^{2}/L^{2}$, take their ratio, and compare the
implied explicit step limit with the physical time of interest. It takes five
minutes, requires no code, and it decides the entire architecture of the solver.
Had this been done before the first line of code, the 5.8-hour explicit run at
$\Delta x = 2.5$ m would never have been attempted.
