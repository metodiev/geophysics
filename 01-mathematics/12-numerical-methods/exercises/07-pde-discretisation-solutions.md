# Solutions — 01-12-07 Discretising PDEs: Consistency, Stability, Convergence

> **Read this after attempting the exercises, not before.** Every amplification
> factor below was computed; the tabulated orders attributed to the demonstration
> are the output of [`../code/pde_discretisation.py`](../code/pde_discretisation.py).

---

## ★1 — Consistency of FTCS

**(a)** With $u_i^n = u(t_n,x_i)$,

$$\frac{u^{n+1}_i - u^n_i}{\Delta t} = u_t + \frac{\Delta t}{2}u_{tt}
+ O(\Delta t^{2}), \qquad
\frac{u^n_{i+1} - 2u^n_i + u^n_{i-1}}{\Delta x^{2}} = u_{xx}
+ \frac{\Delta x^{2}}{12}u_{xxxx} + O(\Delta x^{4}).$$

Subtracting the second from the first and using $u_t = \kappa u_{xx}$:

$$\text{LTE} = \frac{\Delta t}{2}u_{tt} - \frac{\kappa\Delta x^{2}}{12}u_{xxxx}
+ O(\Delta t^{2}, \Delta x^{4}).$$

**(b)** First order in $\Delta t$, second order in $\Delta x$.

**(c)** For a solution of the heat equation $u_{tt} = \kappa u_{xxxx}$, so the two
terms read $\tfrac{\kappa\Delta t}{2}u_{xxxx}$ and
$\tfrac{\kappa\Delta x^{2}}{12}u_{xxxx}$: equal whenever
$\Delta t = \Delta x^{2}/6$. If instead $\Delta t$ is held fixed, the
$\Delta t$ term dominates for every small enough $\Delta x$ and the observed order
under refinement of $\Delta x$ alone falls to **0** — the scheme converges to the
solution of the wrong equation, since the first term then acts as an $O(1)$
perturbation.

**(d)** Consistency means $\text{LTE}\to0$ as the grid is refined: the scheme
reproduces the differential operator to at least first order in each variable.
It is a local, algebraic property and says nothing about whether the error grows
or decays during the integration — that is stability, and convergence needs both
(the Lax equivalence theorem).

---

## ★2 — Consistency of the leapfrog wave scheme

**(a)** Writing $u^{n\pm1}_i = u \pm \Delta t\,u_t +
\tfrac{\Delta t^{2}}{2}u_{tt} \pm \tfrac{\Delta t^{3}}{6}u_{ttt} + O(\Delta t^{4})$,

$$u^{n+1}_i - 2u^n_i + u^{n-1}_i = \Delta t^{2}u_{tt}
+ \frac{\Delta t^{4}}{12}u_{tttt} + O(\Delta t^{6}).$$

**(b)** The spatial stencil is
$u_{i-1} - 2u_i + u_{i+1} = \Delta x^{2}u_{xx} +
\tfrac{\Delta x^{4}}{12}u_{xxxx} + O(\Delta x^{6})$.

**(c)** Dividing by $\Delta t^{2}$ and using $u_{tt} = c^{2}u_{xx}$,

$$\text{LTE} = \frac{\Delta t^{2}}{12}u_{tttt}
- \frac{c^{2}\Delta x^{2}}{12}u_{xxxx} + \dots = O(\Delta t^{2}) + O(\Delta x^{2}),
$$

so the scheme is consistent and second order in both variables. $\square$

**(d)** Consistency says the scheme solves the right equation to second order
*locally*. If the amplification factor exceeds 1 anywhere, those local errors — and
round-off, which is unavoidable — are amplified without bound, and the computed
solution diverges from the exact one however small the truncation error is. The
lesson's measured growth $1.32658443$ per step at $\sigma = 1.01$ is exactly that:
a consistent scheme whose solution is worthless.

---

## ★3 — The explicit diffusion step

**(a)** $r = \kappa\Delta t/\Delta x^{2}\le\tfrac12$ gives

$$\Delta t \le \frac{\Delta x^{2}}{2\kappa}
= \frac{100}{2\times10^{-6}} = 5\times10^{7}\ \text{s}.$$

**(b)** $5\times10^{7}/86400 = \boxed{578.70}$ days.

**(c)** $\Delta t \propto \Delta x^{2}$, so halving $\Delta x$ to 5 m requires
$\Delta t \le 25/(2\times10^{-6}) = 1.25\times10^{7}$ s $= 144.68$ days — a factor
of **4** smaller for a factor of 2 in resolution.

**(d)** In two dimensions the five-point Laplacian has four neighbours instead of
two, so $r \le \tfrac14$: the step is halved again, and in three dimensions
$r\le\tfrac16$. Refining a $d$-dimensional explicit diffusion grid by a factor 2
thus costs $2^{d+1}$ times as many steps *and* twice as many unknowns per
direction, which is why reservoir simulators solve the diffusive part implicitly.

---

## ★4 — von Neumann analysis of upwind advection

**(a)** Substituting $u_i^n = G^n\mathrm{e}^{\mathrm{i}\theta i}$ and dividing
through by $G^n\mathrm{e}^{\mathrm{i}\theta i}$,

$$G = 1 - \sigma\left(1 - \mathrm{e}^{-\mathrm{i}\theta}\right).$$

**(b)** With $\mathrm{e}^{-\mathrm{i}\theta} = \cos\theta - \mathrm{i}\sin\theta$,
write $G = 1 - \sigma(1-\cos\theta) + \mathrm{i}\sigma\sin\theta$, so

$$|G|^{2} = \left[1 - \sigma(1-\cos\theta)\right]^{2} + \sigma^{2}\sin^{2}\theta
= 1 - 2\sigma(1-\sigma)(1-\cos\theta),$$

where the last step uses $\sin^{2}\theta = (1-\cos\theta)(1+\cos\theta)$. $\square$

**(c)** Since $1-\cos\theta\ge0$, the condition $|G|^{2}\le1$ is
$2\sigma(1-\sigma)(1-\cos\theta)\ge0$, i.e.

$$0 \le \sigma \le 1 \qquad\text{for all }\theta,$$

which is the CFL condition. Because $|G|^{2}$ is *decreasing* in
$1-\cos\theta$, the smallest value is at $\theta = \pi$ (the Nyquist mode), where
$|G|^{2} = 1 - 4\sigma(1-\sigma)$; the worst case for the *growth* is
$\theta = \pi$, and the worst case for *accuracy* is the smallest resolved
$\theta$.

**(d)** Upwind is **first order** in space (the one-sided difference has an
$O(\Delta x)$ truncation term), against second order for the centred difference
that is unconditionally unstable. The price of a stable scheme is therefore order
plus numerical diffusion: expanding $|G|$ for small $\theta$ gives an effective
diffusion coefficient $\tfrac{1}{2}c\Delta x(1-\sigma)$, so refining the grid is
the only way to reduce it.

---

## ★★5 — Why centred advection cannot be saved

**(a)** $G = 1 - \tfrac{\sigma}{2}(\mathrm{e}^{\mathrm{i}\theta} -
\mathrm{e}^{-\mathrm{i}\theta}) = 1 - \mathrm{i}\sigma\sin\theta$.

**(b)** $|G|^{2} = 1 + \sigma^{2}\sin^{2}\theta$, which exceeds 1 whenever
$\sigma>0$ and $\theta\ne0,\pi$. There is no pair $(\sigma,\theta)$ in the
unstable regime that can be repaired by changing the step.

**(c)** At $\sigma = 0.5$, $\theta = \pi/2$: $|G| = \sqrt{1 + 0.25} =
\boxed{1.1180340}$. At $\sigma = 1.0$: $|G| = \sqrt{2} = \boxed{1.4142136}$ —
reducing the step to the CFL limit of the *upwind* scheme makes the centred
scheme worse, not better.

**(d)** Halving $\Delta t$ halves $\sigma$, which halves $\sigma\sin\theta$ and
therefore slows the divergence to half the rate per step — while doubling the
number of steps, so the total growth over a fixed time interval is unchanged.
Adding an artificial diffusion term $\epsilon u_{xx}$ makes $G = 1 -
\mathrm{i}\sigma\sin\theta + \epsilon r(1-\cos\theta)$-like with a damping term
proportional to $\epsilon r$; stability then requires the damping to dominate at
every $\theta$, which is possible but converts the scheme back to (at best) first
order and introduces a physical-looking diffusivity that must be chosen and
justified.

---

## ★★6 — Crank–Nicolson

**(a)** Averaging the operator between the old and new levels,

$$u^{n+1}_i - \frac{r}{2}\left(u^{n+1}_{i-1} - 2u^{n+1}_i + u^{n+1}_{i+1}\right)
= u^n_i + \frac{r}{2}\left(u^n_{i-1} - 2u^n_i + u^n_{i+1}\right),$$

and with the mode substitution the spatial difference becomes
$-4\sin^{2}(\theta/2)$ times the mode, so

$$G(\theta) = \frac{1 - r\left(1-\cos\theta\right)}
{1 + r\left(1-\cos\theta\right)}
= \frac{1 - 2r\sin^{2}(\theta/2)}{1 + 2r\sin^{2}(\theta/2)}.$$

**(b)** Write $a = 2r\sin^{2}(\theta/2)\ge0$. Then $G = (1-a)/(1+a)$, and

$$|G|\le1 \iff (1-a)^{2}\le(1+a)^{2} \iff -4a\le0,$$

which holds for every $a\ge0$, i.e. for every $r>0$ and every $\theta$. As
$r\to\infty$ at fixed $\theta\ne0$, $a\to\infty$ and $G\to-1$. $\square$

**(c)**

| $r$ | $G(\pi)$ | $G(\pi/2)$ |
|---|---|---|
| 0.5 | $0.000000$ | $0.333333$ |
| 5 | $-0.818182$ | $-0.666667$ |

At $r = 0.5$ and $\theta = \pi$ the factor is *exactly* zero — the worst mode is
annihilated rather than preserved. That is the mirror image of FTCS at $r = 0.5$,
where the same mode gives $G = -1$ and a permanent sawtooth.

**(d)** $r = 5$ is ten times the explicit limit, and Crank–Nicolson is stable
there (part (b)); the lesson measures an error of $1.31\times10^{-4}$ where FTCS
blows up to $1.08\times10^{4}$. The step is legitimate because the scheme is
implicit, and it costs a tridiagonal solve per step — $O(N)$ work instead of
$O(N)$ per step for FTCS, so the advantage is not the work per step but the number
of steps: at $r=5$ the implicit scheme takes a step five times larger than the
explicit stability limit (ten times if one compares with $r = 0.5$). Note that
this does *not* make the large step accurate: Crank–Nicolson is second order in
$\Delta t$, so at $\Delta t$ ten times larger the error is $100$ times the
error of the small step, and it rings on a sharp transient because it is not
L-stable (§5 of the lesson).

---

## ★★7 — Lax–Wendroff

**(a)** Expanding in time about $t_n$:
$u^{n+1} = u^n + \Delta t\,u_t + \tfrac{\Delta t^{2}}{2}u_{tt} + O(\Delta t^{3})$.
From $u_t = -cu_x$ we get $u_{tt} = -cu_{xt} = -c(u_t)_x = c^{2}u_{xx}$, so

$$u^{n+1} = u^n - c\Delta t\,u_x + \frac{c^{2}\Delta t^{2}}{2}u_{xx}
+ O(\Delta t^{3}).$$

**(b)** Discretising $u_x$ centrally and $u_{xx}$ with the three-point stencil, and
using $\sigma = c\Delta t/\Delta x$:

$$u_i^{n+1} = u_i^n - \frac{\sigma}{2}\left(u^n_{i+1} - u^n_{i-1}\right)
+ \frac{\sigma^{2}}{2}\left(u^n_{i+1} - 2u^n_i + u^n_{i-1}\right). \qquad\square$$

**(c)** $G = 1 - \mathrm{i}\sigma\sin\theta + \sigma^{2}(\cos\theta - 1)
= 1 - 2\sigma^{2}\sin^{2}(\theta/2) - \mathrm{i}\sigma\sin\theta$. With
$s = \sin^{2}(\theta/2)$ and $\sin^{2}\theta = 4s(1-s)$,

$$|G|^{2} = \left(1-2\sigma^{2}s\right)^{2} + 4\sigma^{2}s(1-s)
= 1 - 4\sigma^{2}s + 4\sigma^{4}s^{2} + 4\sigma^{2}s - 4\sigma^{2}s^{2}
= 1 - 4\sigma^{2}(1-\sigma^{2})s^{2}. \qquad\square$$

**(d)** $|G|^{2}\le1$ for all $\theta$ requires $1-\sigma^{2}\ge0$, i.e.
$\sigma\le1$ — the same CFL condition as upwind, at **second order** instead of
first. The cost is the wider stencil (three spatial points and the extra term) plus
a genuinely oscillatory error near a discontinuity: because
$|G|<1$ everywhere except the endpoints, Lax–Wendroff damps less than upwind and
produces dispersive ripples behind fronts, which is why limiters exist.

---

## ★★8 — A step that is stable until the grid is refined

**(a)** $r = \kappa\Delta t/\Delta x^{2} = 10^{-7}\times10^{6}/0.25 =
\boxed{0.4}$: stable, with margin ($r\le0.5$).

**(b)** $\Delta t_{\max} = \Delta x^{2}/(2\kappa) = 0.25/(2\times10^{-7}) =
1.25\times10^{6}$ s $= \boxed{14.47}$ days.

**(c)** On the finer grid $r = 10^{-7}\times10^{6}/0.0625 = \boxed{1.6}$: above
the limit of $\tfrac12$, so the highest Fourier mode grows by
$4r - 1 = 5.4$ per step and the run is destroyed. The largest stable step is
$\Delta x^{2}/(2\kappa) = 0.0625/2\times10^{-7} = 3.125\times10^{5}$ s
$= 3.617$ days: the step must be **4 times smaller** for the same $\Delta t$ — a
factor of 4 in step count for a factor of 2 in resolution, compounded by twice as
many unknowns.

**(d)** Assert at every time step that $r = \kappa\Delta t/\Delta x^{2}$ — computed
from the *current* grid spacing and the largest $\kappa$ on the grid — is at most
$\tfrac12$, and fail loudly rather than continuing. A Courant-number check on a
separate advection term computes $\sigma = c\Delta t/\Delta x$ and is a completely
different number: here $\sigma$ would equal 0.4 too, and it shrinks when
$\Delta x$ is halved, so a code that checks only $\sigma$ would report an
*improving* situation while the diffusive term became unstable. A diffusion term
must be checked with its own dimensionless group.

---

## ★★★9 — Leapfrog with a travelling initial condition

**(a)** Periodic unit domain, $c = 1$, $u(x,0) = \sin 2\pi x$,
$u_t(x,0) = -2\pi\cos 2\pi x$, $\sigma = 0.4$, $n$ steps to $t = 0.4$, and the
second-order Taylor startup $u^{1} = u^{0} + \Delta t\,g +
\tfrac{\Delta t^{2}}{2}c^{2}u^{0}_{xx}$:

| $n$ | $\Delta x$ | max error at $t = 0.4$ | measured order |
|---|---|---|---|
| 20 | 0.0500 | $1.1698\times10^{-2}$ | — |
| 40 | 0.0250 | $2.9432\times10^{-3}$ | 1.991 |
| 80 | 0.0125 | $7.3531\times10^{-4}$ | 2.001 |
| 160 | 0.00625 | $1.8382\times10^{-4}$ | 2.000 |
| 320 | 0.003125 | $4.5959\times10^{-5}$ | 2.000 |

The order is **2**, as the truncation analysis of ★2 predicts, and the errors fall
by almost exactly a factor of 4 per refinement.

**(b)** With the naive startup $u^{1} = u^{0} + \Delta t\,g$:

| $n$ | max error at $t = 0.4$ | measured order | discrepancy in $u^{1}$ between the two startups |
|---|---|---|---|
| 20 | $4.3636\times10^{-2}$ | — | $7.8310\times10^{-3}$ |
| 40 | $1.9960\times10^{-2}$ | 1.128 | $1.9699\times10^{-3}$ |
| 80 | $9.5802\times10^{-3}$ | 1.059 | $4.9323\times10^{-4}$ |
| 160 | $4.6998\times10^{-3}$ | 1.027 | $1.2335\times10^{-4}$ |
| 320 | $2.3286\times10^{-3}$ | 1.013 | $3.0842\times10^{-5}$ |

The measured order degrades to **1**, even though the interior scheme is second
order. The startup error is $O(\Delta t^{2}) = O(\Delta x^{2})$ in the *first time
level* — the discrepancy column falls by a factor 3.98 per refinement — and that
initial defect propagates undamped, so it contributes an error of the same order
as the truncation error of a first-order scheme. At $n = 20$ the naive run is
$3.73$ times worse than the properly started one.

**(c)** The spurious-mode amplitude $\left|\sum_i u_i(-1)^{i}\right|2/n$ is at
round-off in **both** runs at every $n$ ($\sim10^{-17}$), so the naive startup did
not excite the computational mode. The reason is that its error is a smooth
function of $x$ (proportional to the initial mode shape), and a smooth error
projects onto the physical root; the computational mode needs a checkerboard-like
error to be excited. The lesson's §5 warning still stands — what the startup
damaged here is accuracy, not the spurious mode.

**(d)** Perturbing the second time level by a checkerboard of amplitude
$10^{-3}$ in a 40-step run:

| $\sigma$ | final Nyquist amplitude, unperturbed | final Nyquist amplitude, perturbed |
|---|---|---|
| 0.5 | $3.6\times10^{-17}$ | $2.000\times10^{-3}$ |
| 1.0 | $1.7\times10^{-15}$ | $8.00\times10^{-2}$ |

At $\sigma = 0.5$ the checkerboard is **undamped**: a $10^{-3}$ perturbation in
$u^{1}$ appears as $2\times10^{-3}$ at the end (both time levels carry it) and has
not decayed at all — the computational mode is neutral. At $\sigma = 1.0$ it grows
*linearly* in the step count, from $2\times10^{-3}$ to $8\times10^{-2}$ over
40 steps, a factor of exactly 40. $\sigma = 1$ is the point where the two roots of
$G^{2} - 2aG + 1$ coalesce at $-1$; a double root at $|G| = 1$ produces secular
growth rather than exponential growth. That is why $\sigma = 1$ is "neutral" in the
stability analysis and unusable in practice: any asymmetry, boundary reflection or
round-off supplies the checkerboard, and it grows in proportion to the run length.

---

## ★★★10 — A reported Courant number of 0.85 that still violates a limit

**(a)** In order of likelihood:

1. **The reported number is a nominal or interior value, not the maximum over the
   grid.** Diagnostic: recompute $\max_i c_i\Delta t/\Delta x_i$ from the velocity
   model actually in use, including any sharp low-velocity or high-velocity layer,
   and compare with the reported figure.
2. **A second, different stability limit is being violated** — typically an
   explicit diffusive term, a source/sink term integrated explicitly, or an
   attenuation term with a relaxation time shorter than $\Delta t$. Diagnostic:
   print every dimensionless group the scheme contains ($r$ for diffusion,
   $\lambda_{\text{relax}}\Delta t$ for relaxation, $\sigma$ for advection) and
   check each against its own limit.
3. **The boundary treatment is unstable even though the interior is stable.**
   Diagnostic: rerun with the interior scheme unchanged but the boundary driven
   from an analytic solution; if the growth persists, it is the boundary.

The order can be inverted by evidence: a growth rate matching a predicted
amplification factor points at 2, an error field concentrated at the domain edges
points at 3, and a growth that appears only after the wavefront has crossed the
fastest cell points at 1.

**(b)** A single Courant number presupposes a single velocity. With variable
velocity the condition is $\max_i c_i\Delta t/\Delta x_i\le1$, so the binding cell
is the one with the largest $c/\Delta x$ — which is not necessarily the cell the
user had in mind (a shallow, low-velocity cell on a coarse grid can be the
offender, and so can a single high-velocity cell inserted by an interpolation
artefact). The quantity to compute and report is that maximum, together with the
index of the cell that attains it.

**(c)** Growth of $1.327$ per step from round-off $10^{-16}$ reaches order 1 after

$$k = \frac{16\ln 10}{\ln 1.327} = \frac{36.84}{0.28305}
= \boxed{130.2}\ \text{steps},$$

and after 400 steps the amplification is $1.327^{400} =
1.41\times10^{49}$, i.e. the run is already $10^{49}$ times above its initial
noise. A crash (or a saturation to NaN/infinity) at step 400 is entirely
consistent with a violation of a few per cent: the observable blow-up begins at
roughly step 130, which leaves 270 steps for the overflow to become fatal.

**(d)** The two conditions are independent: $\sigma = 0.85$ says nothing about
$r = \kappa\Delta t/\Delta x^{2}$, whose limit is $\tfrac12$ for FTCS in 1-D
($\tfrac14$ in 2-D). So the reported Courant number is entirely consistent with a
diffusive term being unstable, and the diagnosis should be revisited: the most
likely cause is cause (2) of part (a) — a dimensionless group that was never
printed — rather than a subtlety in the advective CFL condition itself.
