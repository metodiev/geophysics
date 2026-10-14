# Solutions — 25-04-01 Project: Finite-Difference Wave Propagation and Convergence Testing

> Read after attempting. Lesson:
> [01 FD Wave Propagation](../01-fd-wave-propagation-project.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/fd_wave_demo.py`](../code/fd_wave_demo.py).

---

## ★1 — The update and its truncation error

$$u^{n+1}_i = 2u^{n}_i - u^{n-1}_i
+ r^{2}\left(u^{n}_{i+1} - 2u^{n}_i + u^{n}_{i-1}\right),
\qquad r = \frac{c\,\Delta t}{\Delta x},$$

with modified equation

$$u_{tt} - c^{2}u_{xx}
= \frac{c^{2}\Delta x^{2}}{12}\left(r^{2}-1\right)u_{xxxx}
+ \mathcal O(\Delta x^{4}).$$

**Vanish point:** $r = 1$. **Instability point:** $r > 1$ (the CFL limit). The
scheme is therefore most accurate exactly at the boundary of its stability region,
which is why production acoustic codes run at $r \approx 0.9$ rather than at
$r = 0.3$.

---

## ★2 — An order from one pair

$$\text{order} = \frac{\log(e_{40}/e_{80})}{\log(80/40)}
= \frac{\log(2.161\times10^{-3}/5.421\times10^{-4})}{\log 2}
= \frac{\log 3.986}{0.6931} = \frac{1.3828}{0.6931} = 1.995 \approx 2.0.$$

One pair gives *a* number, but not a defensible order: the fitted value is
sensitive to which two grids are chosen, and a single pair cannot reveal whether
the error is in the asymptotic regime at all. **At least three, preferably four
grids spanning a factor of eight in $\Delta x$**, with the fitted orders compared
against each other — as the project's own table does, where the three successive
orders ($2.00$, $2.00$, $2.00$) are what makes the claim credible.

---

## ★3 — The stability condition

$$|g|^{2} = 1 - r^{2}\sin^{2}\theta \le 1
\;\Longleftrightarrow\;
r^{2}\sin^{2}\theta \ge 0 \;\text{is bounded}
\;\Longleftrightarrow\;
r \le 1 .$$

The worst case is $\theta = \pi/2$, i.e. $\sin^{2}\theta = 1$, where
$|g|^{2} = 1-r^{2}$: at $r = 1$ the amplification is exactly zero (the scheme is
non-dissipative but marginally stable, since $|g| = 1$ elsewhere), and for $r > 1$
there are wavenumbers with $|g| > 1$ and the solution grows exponentially. The
most dangerous mode is therefore the **shortest wavelength the grid can carry**,
$\theta = \pi/2$ — which is why grid noise grows fastest when the CFL limit is
violated, exactly as the sweep shows.

---

## ★★4 — Order and extrapolation

$$\text{order}(100 \to 200) = \frac{\log(8.692\times10^{-5}/2.174\times10^{-5})}{\log 2}
= \frac{\log 3.998}{0.6931} = 1.999,$$

$$\text{order}(200 \to 400) = \frac{\log(2.174\times10^{-5}/5.438\times10^{-6})}{\log 2}
= \frac{\log 3.998}{0.6931} = 1.999.$$

Mean order: **2.00**.

**Extrapolation.** At order 2, halving $\Delta x$ quarters the error:

$$e(800) \approx \frac{e(400)}{4} = \frac{5.438\times10^{-6}}{4}
= 1.360\times10^{-6}.$$

**Assumption.** The extrapolation assumes the solution is in the **asymptotic
regime**, i.e. that the $\mathcal O(\Delta x^{2})$ term already dominates and no
lower-order error source (a boundary, a source, a coefficient evaluation) takes
over on the finer grid. The three identical fitted orders are the evidence that it
is, and that evidence is what makes the extrapolation legitimate rather than
wishful.

---

## ★★5 — The initialisation's O(Δt) error

Eliminating $u^{-1}$ from the two equations

$$u^{1}_i = 2u^{0}_i - u^{-1}_i + r^{2}\left(u^{0}_{i+1}-2u^{0}_i+u^{0}_{i-1}\right),
\qquad
u^{-1}_i = u^{0}_i$$

gives the implied initial velocity

$$v^{0}_i \approx \frac{u^{1}_i - u^{-1}_i}{2\Delta t}
= \frac{r^{2}}{2\Delta t}\left(u^{0}_{i+1}-2u^{0}_i+u^{0}_{i-1}\right)
= \frac{\Delta t\,c^{2}}{2}u_{xx}(x_i,0) + \mathcal O(\Delta t^{3}).$$

The true initial velocity is zero, so the initialisation introduces a spurious
velocity of size $\tfrac{1}{2}\Delta t\,c^{2}u_{xx}$, i.e. **$\mathcal O(\Delta t)$**.
The wave equation propagates that error linearly in time, so the solution error at
fixed $T$ is also $\mathcal O(\Delta t)$.

At fixed $r$, $\Delta t = r\Delta x/c \propto \Delta x$, so the initialisation
error is $\mathcal O(\Delta x)$ — **one order worse than the stencil's
$\mathcal O(\Delta x^{2})$** — and it dominates once the grid is refined enough for
the truncation term to fall below it. That is exactly what the measurement shows:
the fitted order is $0.96$–$0.99$ with the naive start and $2.00$ with the exact
start, at a factor of $28$ lower absolute error.

The fix is to initialise the second time level to second-order accuracy, here by
taking it from the exact solution: $u^{-1}_i = u(x_i, -\Delta t)$.

---

## ★★6 — Growth rate at the CFL limit

$$\text{growth over the run} = \frac{3.0767}{0.35352} = 8.70,$$

and with $\Delta t = 4.04\ \mathrm{ms}$ and $T = 0.55\ \mathrm{s}$ the number of
steps is $0.55/0.00404 = 136$, so

$$\text{per-step factor} = 8.70^{1/136} = e^{2.1633/136} = e^{0.01591} = 1.0160,$$

i.e. **$+1.6\%$ per time step**.

**Why that is dangerous.** A $1.6\%$ per-step growth compounds as $1.016^{n}$:

| steps | amplitude factor |
|---|---|
| $136$ (this run) | $8.7$ |
| $10^{3}$ | $7.9\times10^{6}$ |
| $10^{4}$ | $1.7\times10^{69}$ |

A production run of $10^{4}$ steps — a few seconds of modelled time at a fine
grid — overflows long before it finishes. Worse, the growth is fastest for the
highest wavenumbers, so the symptom is grid-scale noise rather than a smoothly
blowing-up field: over the first few hundred steps the solution can look like a
plausible wavefield with a slightly rough background, which is how a marginal CFL
number reaches a published figure. **Run at $r \le 0.9$ and assert the norm.**

---

## ★★★7 — A verification suite for a heterogeneous elastic FDEM code

**Manufactured solutions and what each tests.**

| test | what it isolates |
|---|---|
| homogeneous full space, plane wave, periodic boundaries | the stencil's truncation order in space and time, with no boundary error and no heterogeneity error |
| layered medium, analytic reflection/transmission coefficients | the impedance and interface treatment: the reflection coefficient should match the exact value for a plane wave at normal incidence |
| heterogeneous smooth medium, **manufactured** solution ($u = \sin(kx)\sin(mz)\cos(\omega t)$ inserted as a body force) | the variable-coefficient discretisation, including whether $\rho$ and $\mu$ are averaged consistently with the stencil's order |
| free surface, Rayleigh-wave dispersion | the free-surface boundary condition: the dispersion curve has a closed-form solution and is a strong test of the traction-free condition |
| absorbing boundary, pulse exiting the domain | the reflection coefficient of the absorbing condition, measured as residual energy |
| energy conservation in a closed elastic domain | whether the scheme is conservative; drift in total energy indicates a flux error |

**Quantities to fit orders from.** For the homogeneous and manufactured tests, the
**discrete $L_{2}$ norm of the error at a fixed physical time**, fitted over four
grids. For the layered test, the **reflection coefficient** and the **travel time**,
each fitted against the analytic value. For the free surface, the **Rayleigh-wave
phase velocity**, fitted against the analytic dispersion curve. Fitting an order
from a norm alone is insufficient for boundary-dominated tests, where the error
scales differently.

**Separating boundary error from interior error.** Run the same physical problem
on a sequence of **domain sizes with the receiver and the source held at fixed
distance from the boundary**, so the boundary contribution is constant while the
interior grid is refined; then refine with a fixed domain so the boundary distance
grows. The two sequences separate the terms. A second technique is to compute the
error on an interior subdomain only, excluding a boundary layer several grid cells
wide.

**Tolerance.** Demand a fitted order within $0.1$ of the nominal order over at
least a factor of four in $\Delta x$, and a relative error below $10^{-4}$ at the
finest grid for the homogeneous test. For the boundary tests, demand agreement with
the analytic reflection coefficient to $1\%$ and with the Rayleigh dispersion curve
to $0.5\%$.

**The tests that can pass while the code is still wrong.** This is the point of the
exercise, and the honest answer has three entries:

1. **A homogeneous test passes with wrong interface physics.** A code that averages
   density incorrectly across an interface can be exactly right in a homogeneous
   medium; only the layered test detects it, and only if the reflection coefficient
   is checked rather than the wavefield's appearance.
2. **An interior-subdomain error norm passes with a wrong boundary.** Excluding the
   boundary layer removes the diagnostic along with the error.
3. **An order test passes with the wrong physics.** Any consistent
   second-order scheme has order 2; a plausible-looking dispersion relation for the
   wrong material parameters would also have order 2. Verification tests
   *implementation*, not *formulation*: a verified code can still be solving the
   wrong equation, which is what a **validation** test against a physical
   observation is for.
