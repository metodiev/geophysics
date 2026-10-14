---
id: 05-03-04
title: "Numerical Forward Modelling and Discretisation"
level: graduate
prereqs: ["05-03-01", "05-03-03"]
tags: [discretisation, finite-difference, convergence, manufactured-solution, numerics]
---

# Numerical Forward Modelling and Discretisation

## Learning objectives

1. **Distinguish** the three sources of error in a numerical forward model:
   modelling, discretisation and round-off.
2. **Derive** the second-order truncation error of the 5-point Laplacian and
   **measure** the convergence order of a solver.
3. **Use** the method of manufactured solutions to validate a PDE solver.
4. **Choose** a discretisation and state its cost and its error budget.
5. **Report** a numerical result so that another person can reproduce and
   falsify it.

## Prerequisites

- [05-03-01 The Forward Problem](./01-forward-problem.md)
- [01-09-04 Laplace and Poisson Equations](../../01-mathematics/09-partial-differential-equations/04-laplace-poisson.md)

## 1. Intuition

Analytical solutions exist for a handful of shapes. Everything else is
numerical, and every numerical answer contains an error that you chose. The
skill is not writing the solver; it is knowing which of the three error sources
dominates, and demonstrating that it is small compared with the physical
question.

## 2. Precise definitions

**Modelling error.** The difference between the physical system and its
mathematical statement (e.g. assuming a homogeneous half-space when the Earth is
layered). You cannot reduce it by refining a grid.

**Discretisation error.** The difference between the exact solution of the
mathematical statement and the computed solution. Reduced by refinement.

**Round-off error.** The difference caused by finite-precision arithmetic.
Increases as the grid is refined past a crossover point, because more
operations accumulate more error.

**Convergence order $p$.** If the error behaves as $E(h) = Ch^p$ for grid
spacing $h$, then $p = \log(E_1/E_2)/\log(h_1/h_2)$ measured between two
refinements.

## 3. Derivations

### 3.1 Truncation error of the 5-point Laplacian

Taylor expand $u$ about $(x_i,y_j)$:

$$u_{i\pm1,j} = u \pm h u_x + \frac{h^2}{2}u_{xx} \pm \frac{h^3}{6}u_{xxx}
+ \frac{h^4}{24}u_{xxxx} + O(h^5).$$

Adding the four neighbours and subtracting $4u$:

$$u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u = h^2\nabla^2u
+ \frac{h^4}{12}\left(u_{xxxx}+u_{yyyy}\right) + O(h^6),$$

so

$$\nabla^2u = \frac{u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u}{h^2}
- \frac{h^2}{12}\left(u_{xxxx}+u_{yyyy}\right) + O(h^4).$$

The scheme is **second order**: the local truncation error is $O(h^2)$.

### 3.2 Measuring the order

Halving $h$ multiplies a second-order error by 4. So the *order* is measurable:

$$p = \frac{\log(E(h_1)/E(h_2))}{\log(h_1/h_2)}.$$

This is the single most useful diagnostic in numerical geophysics: it tells you
whether your implementation matches your intention.

### 3.3 Method of manufactured solutions

Choose a solution $u$ with the properties you need (here
$u = \sin\pi x\sin\pi y$, which vanishes on the unit-square boundary). Compute
the source term $b = -\nabla^2u$ analytically. Solve the discrete problem with
$b$ and the exact boundary data, and compare with $u$. Any defect in the
implementation — a wrong coefficient, a wrong stencil, an assembly bug — shows
up as an error that does not converge at the expected order.

### 3.4 What the discretisation does to a wave: the modified wavenumber

Section 3.1 gave the truncation error of the 5-point Laplacian. A sharper
statement is available: exactly what the discrete operator does to a Fourier
mode, which is what determines whether a modelled wave travels at the right
speed.

Substitute a plane wave $u_{ij} = e^{i(k_x x_i + k_y y_j)}$ into the stencil and
divide by $h^2$:

$$\frac{u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{i,j}}{h^2}
= -\frac{4}{h^2}\left[\sin^2\!\left(\frac{k_xh}{2}\right)
+ \sin^2\!\left(\frac{k_yh}{2}\right)\right]u_{ij} .$$

Compare with the exact result $-\left(k_x^2+k_y^2\right)u_{ij}$. The discrete
operator acts like an exact operator with a **modified wavenumber**
$k^2 \to \frac{4}{h^2}\sin^2(kh/2)$ per direction. Expanding for small $kh$,

$$\frac{4}{h^2}\sin^2\!\left(\frac{kh}{2}\right)
= k^2\left(1 - \frac{(kh)^2}{12} + O(kh)^4\right),$$

so the relative error in the effective wavenumber is $-(kh)^2/12$. **Measured**
(one direction, $kh = 2\pi/\text{ppw}$ where ppw is points per wavelength):

| points per wavelength | $kh$ | measured $k_\text{disc}^2/k_\text{exact}^2-1$ | $(kh)^2/12$ |
|---|---|---|---|
| 5 | 1.2566 | $-1.249\times10^{-1}$ | $1.316\times10^{-1}$ |
| 10 | 0.6283 | $-3.247\times10^{-2}$ | $3.290\times10^{-2}$ |
| 20 | 0.3142 | $-8.198\times10^{-3}$ | $8.225\times10^{-3}$ |
| 40 | 0.1571 | $-2.054\times10^{-3}$ | $2.056\times10^{-3}$ |

The agreement between measurement and the derived $(kh)^2/12$ is better than 1%
for 10 points per wavelength and better than 0.5% beyond.

**Physical interpretation.** The stencil makes waves travel slightly too slowly:
$k_\text{disc} < k_\text{exact}$ means a *larger* wavelength, i.e. a
*lower* phase velocity. The error is second order in $h$ and grows quadratically
with frequency, so a simulation calibrated at long wavelength will be wrong at
short wavelength — the standard numerical-dispersion artefact. It is the discrete
analogue of physical dispersion discussed in
[05-04-06](../04-rock-physics/06-attenuation-dispersion-rock.md), and it is
*wrong physics introduced by the grid*.

### 3.5 The points-per-wavelength rule, derived

Set the derived relative error equal to a target:

$$\frac{(kh)^2}{12} = \epsilon
\qquad\Longrightarrow\qquad
kh = \sqrt{12\epsilon}, \qquad
\text{ppw} = \frac{2\pi}{kh} = \frac{2\pi}{\sqrt{12\epsilon}} .$$

| target relative error $\epsilon$ | ppw required |
|---|---|
| 10% | 5.7 |
| 1% | 18.1 |
| 0.1% | 57.4 |

So the widely repeated "use 10 points per wavelength" corresponds to a 3.2%
error, not 1% — a useful correction to folklore. **The rule scales as
$\epsilon^{-1/2}$:** halving the target error costs a factor
$\sqrt{2}$ in grid points per direction, and hence a factor $2\sqrt{2}$ in cost
in two dimensions.

### 3.6 Round-off: when refinement stops helping

The truncation error falls with $h$; round-off grows. For a sum of $N$ terms in
double precision, random rounding accumulates as

$$\text{error}_\text{round-off} \sim \sqrt{N}\,\epsilon_\text{mach}\,
\lVert\text{terms}\rVert, \qquad \epsilon_\text{mach} = 2.2\times10^{-16} .$$

**Numbers.** A million-term sum has $\sqrt{N}\,\epsilon_\text{mach} =
10^{3}\cdot2.2\times10^{-16} = 2.2\times10^{-13}$ relative — so for a
million-node assembly a tolerance of $10^{-12}$ is already at the edge of what
the arithmetic can deliver, while $10^{-14}$ is unreachable regardless of how
correct the algorithm is.

**The crossover.** Combining the two laws, total error
$\approx C h^p + \sqrt{N(h)}\,\epsilon_\text{mach}$ is minimised at some
$h_*$, beyond which refinement makes things worse. In practice one stops when
the truncation error reaches the round-off floor, which is exactly what the
measured quadrature table of
[05-01-01](../01-what-geophysics-measures/01-physical-property-contrast.md)
shows: errors falling by a factor $2.4\times10^{4}$ per refinement until
$3.98\times10^{-15}$, then flat.

### 3.7 Sparsity and cost, derived

The stencil's structure determines the cost of a solve, and the numbers are worth
knowing because they decide how fine a grid is affordable.

The 5-point Laplacian has **one unknown per interior node and five nonzeros per
row**: the diagonal and the four neighbours. For an $m\times m$ interior grid
($m = n-2$ interior nodes per side), the number of unknowns is $N = m^2$ and the
number of nonzeros is about $5N$.

| $n$ | unknowns $N$ | dense entries $N^2$ | nonzeros $\approx5N$ | ratio |
|---|---|---|---|---|
| 41 | 1 521 | 2.31×10⁶ | 7.6×10³ | 304 |
| 81 | 6 241 | 3.90×10⁷ | 3.1×10⁴ | 1 248 |
| 161 | 25 281 | 6.39×10⁸ | 1.3×10⁵ | **5 056** |

**The measured ratio grows as $N/5$**, so the storage advantage of sparsity
improves with resolution — from a factor 304 at $n = 41$ to 5056 at $n = 161$.
That is why the demonstration's manufactured-solution study can afford $n = 161$
in half a second with a sparse direct solve, while a dense solve of the same
problem would need 5 GB of memory for the matrix alone.

**Cost scaling, derived.** For a banded or sparse 2-D problem:

- dense direct solve: $O(N^3) = O(m^6)$ — doubling the resolution multiplies cost
  by 64;
- sparse (nested-dissection) direct solve: $O(N^{3/2}) = O(m^3)$ — a factor 8 per
  doubling;
- iterative (multigrid) solve: $O(N)$ per iteration, $O(\log N)$ iterations —
  nearly linear, which is why large 3-D problems are solved iteratively.

**The practical rule.** Before refining a grid, estimate the cost exponent for the
solver you are actually using. The difference between $m^6$ and $m$ per
doubling — factors of 64 versus 2 — is the difference between a study that is
feasible on a laptop and one that is not. **Report the grid, the solver type and
the measured accuracy together**, because the three are coupled through exactly
these scalings.

### 3.8 A second stability condition: the wave equation

Section 3.6 of
[05-01-03](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md)
derived $\Delta t \le \Delta z^2/(2D)$ for the diffusion equation. The wave
equation gives a *different* condition, and the comparison is instructive.

Discretise $u_{tt} = c^2u_{zz}$ with second-order centred differences in both
variables:

$$\frac{u_j^{n+1}-2u_j^n+u_j^{n-1}}{\Delta t^2}
= c^2\frac{u_{j+1}^n-2u_j^n+u_{j-1}^n}{\Delta z^2} .$$

Substitute $u_j^n = \xi^n e^{ikj\Delta z}$ and define the Courant number
$r \equiv c\Delta t/\Delta z$:

$$\xi^2 - 2\xi + 1 = -4r^2\sin^2\!\left(\frac{k\Delta z}{2}\right)
\qquad\Longrightarrow\qquad
\xi = 1 - 2r^2\sin^2\!\left(\frac{k\Delta z}{2}\right)
\pm\sqrt{\left[1-2r^2\sin^2\!\left(\frac{k\Delta z}{2}\right)\right]^2-1} .$$

Stability requires $|\xi|\le1$ for all $k$. The worst case is
$\sin^2(k\Delta z/2) = 1$; there the discriminant is non-negative only if
$r^2 \le 1$, giving the **Courant–Friedrichs–Lewy condition**

$$\boxed{\;r = \frac{c\,\Delta t}{\Delta z} \le 1\;}
\qquad\Longrightarrow\qquad
\Delta t \le \frac{\Delta z}{c} .$$

**Compare the two conditions, and note the physics.**

| equation | condition | character |
|---|---|---|
| diffusion | $\Delta t \le \Delta z^2/2D$ | *quadratic* in $\Delta z$; a diffusion length limit |
| wave | $\Delta t \le \Delta z/c$ | *linear* in $\Delta z$; a travel-time limit |

The CFL condition has a clean physical reading: **in one time step the wave must
not travel more than one cell.** The diffusion condition says the field must not
diffuse more than about one cell. Because one is linear and the other quadratic
in $\Delta z$, refining a wave simulation is far cheaper than refining a diffusion
simulation: at half the spacing, a wave code needs half the time step while a
diffusion code needs a quarter, and in two or three dimensions the gap widens
further. **Knowing which equation you are solving tells you which cost law
applies**, and this is the kind of estimate that should precede any modelling
budget.

## 4. Units and dimensional analysis

| Symbol | Meaning | Unit |
|---|---|---|
| $h$ | grid spacing | m |
| $u$ | field being solved for | m² s⁻² (potential) |
| $b$ | source term | m² s⁻² m⁻² = s⁻² |
| $E$ | error norm | depends on $u$ |
| $p$ | convergence order | dimensionless |

A useful sanity check on a Poisson solver for gravity: $b = 4\pi G\rho$ has
units $\mathrm{m^3kg^{-1}s^{-2}\cdot kg\,m^{-3}} = \mathrm{s^{-2}}$, matching
$\nabla^2\Phi$ with $[\Phi] = \mathrm{m^2s^{-2}}$ divided by $\mathrm{m^2}$. ✓

## 5. Assumptions

1. **Sufficient regularity** of the solution for the Taylor expansion. A
   discontinuous density field reduces the local order.
2. **Convergence to the correct solution**, not merely to *a* solution. The
   manufactured-solution test confirms this; refinemente alone does not (a
   consistent but wrongly-scaled scheme can converge to the wrong answer).
3. **Stability.** For time-dependent schemes, the time step must satisfy the
   stability limit (e.g. $dt \le h^2/(2D)$ for explicit diffusion).
4. **Round-off is below the discretisation error** for the grids used.

## 6. Worked examples (measured)

From `code/validation_benchmarks.py`, manufactured solution
$u = \sin\pi x\sin\pi y$ on the unit square with a sparse direct solve:

| $n$ | $h$ | $\max\lvert u_\text{num}-u_\text{exact}\rvert$ | measured order |
|---|---|---|---|
| 21 | 0.05 | $2.0587\times10^{-3}$ | — |
| 41 | 0.025 | $5.1420\times10^{-4}$ | 2.0013 |
| 81 | 0.0125 | $1.2852\times10^{-4}$ | 2.0003 |
| 161 | 0.00625 | $3.2128\times10^{-5}$ | 2.0001 |

Fitted log–log slope over all four grids: **2.000559**. The implementation is
second order, as intended, and the measurement says so.

**A test that cannot fail is not a test.** In Section 4 of the demo a deliberate
2% scaling error is injected into the prism kernel: the correct code passes a
$10^{-6}$ tolerance with a relative error of $3.98\times10^{-15}$, while the
buggy code fails with $2.000\times10^{-2}$. Inject a known error and confirm the
test rejects it.

**Round-off floor.** Gauss-Legendre quadrature of the prism integral gives
relative errors of $1.19\times10^{-2}$ at $n=4$, $1.51\times10^{-4}$ at 8,
$3.55\times10^{-8}$ at 16, then $8.5\times10^{-15}$ and $4.0\times10^{-15}$ at
32 and 64: it has hit the round-off floor near $10^{-15}$, and further refinement
buys nothing. **Set tolerances above the measured floor.**

### 6.1 Worked arithmetic: choosing a grid from the error budget

**The question.** An EM diffusion simulation must reproduce the skin-depth decay
to 1% at a dominant wavelength of 5 km. What grid spacing is needed?

**Step 1 — the requirement in $kh$.** From Section 3.5, $\epsilon = 0.01$ needs
$kh = \sqrt{12\cdot0.01} = 0.3464$ and ppw $= 18.1$.

**Step 2 — the spacing.** $h = \lambda/\text{ppw} = 5000/18.1 = 276$ m. In the
demonstration's units ($\delta = 5032.9$ m, and $\lambda$ of the same order as
$\delta$) that is $h/\delta \approx 0.055$ — close to the finest grid the
demonstration used ($h/\delta = 0.05$), which measured a 1% error
($6.99\times10^{-4}$ in decay length, 1.4% in phase). **The derived requirement
and the measured performance agree**, which is the point of doing the derivation.

**Step 3 — the cost.** Halving $h$ in two dimensions quadruples the node count,
and in an explicit diffusion scheme the time step falls as $h^2$, so total cost
scales as $h^{-4}$. Going from a 1% to a 0.1% target ($\epsilon^{-1/2}$ in $h$,
i.e. $h$ down by $\sqrt{10}$) multiplies cost by $10^{2} = 100$.

**Step 4 — the honest question: is 1% needed?** If the conductivity is known only
to 20%, a 1% numerical error is a fifth of the input uncertainty and is fine; a
0.01% target would be pure decoration. **Tolerance must be chosen from the
physical problem, not from what the computer can do.** This is the single most
common waste of compute in modelling, and it is a reasoning error rather than a
coding one.

### 6.2 A shortcut that fails: reaching for a higher-order stencil

**The shortcut.** The 5-point stencil has $(kh)^2/12$ error, so use a 9-point
fourth-order stencil and get $(kh)^4$ error at the same spacing.

**Why it can fail.** Three reasons, all real:

1. **The solution may not be smooth enough.** A fourth-order stencil achieves
   fourth-order convergence only if the fourth derivatives are bounded. Across a
   conductivity or density discontinuity the local order collapses to first
   order, and the *global* order with it. The gain over a second-order scheme can
   then be negligible or negative (a wider stencil smears the discontinuity over
   more nodes).
2. **Boundary conditions dominate.** A wide stencil needs more boundary closures,
   and the boundary scheme's order frequently becomes the global order. Reporting
   a fourth-order interior stencil with a first-order boundary closure is a
   measured misrepresentation.
3. **Stability can tighten.** Wider explicit stencils often reduce the allowable
   time step, erasing the accuracy gain in cost terms.

**What to do instead.** Measure the order with a manufactured solution
(Section 3.3) *after* adding the boundary conditions, and compare the measured
order at the resolutions you will actually use — not in the asymptotic limit you
will never reach. Then choose the scheme whose *measured* error per unit cost is
lowest, and report the grid, the order and the error together.

### 6.3 Extended worked example: a second convergence study, in a different equation

The manufactured-solution test exercises an elliptic solver. A second study, on
the parabolic diffusion equation, confirms that the same discipline transfers to
time-dependent problems — and it exposes a different failure mode.

The problem is $\partial B/\partial t = D\,\partial^2B/\partial z^2$ on a
semi-infinite domain, forced by $B(0,t) = B_0\cos\omega t$, with the closed-form
solution $B(z,t) = B_0e^{-z/\delta}\cos(\omega t - z/\delta)$ and
$\delta = \sqrt{2D/\omega}$. Take $D = 7.9577\times10^{5}$ m²/s (equivalent to
$\sigma = 1$ S/m), $T = 100$ s, so $\delta = 5032.9$ m.

An explicit scheme requires $dt \le dz^2/(2D)$ for stability. The demonstration
uses the conservative $dt = 0.4\,dz^2/D$ and marches five periods, recording the
last period for analysis. Measured decay length against grid refinement:

| $n_z$ | $dz/\delta$ | measured $\delta$ (m) | relative error | measured phase lag (rad) | predicted $z/\delta$ |
|---|---|---|---|---|---|
| 31 | 0.200 | 5057.4 | $4.87\times10^{-3}$ | 0.832 | 0.800 |
| 61 | 0.100 | 5040.6 | $1.53\times10^{-3}$ | 0.696 | 0.700 |
| 121 | 0.050 | 5036.4 | $6.99\times10^{-4}$ | 0.749 | 0.750 |

Both amplitude and phase converge toward the closed-form values, and the error
falls monotonically with refinement — the signature of discretisation error, not
modelling error. The observed error ratio per halving of $dz$ is about 3.2 then
2.2, i.e. between first and second order, which is what mixed time (first-order,
Euler) and space (second-order, centred) errors produce.

**An earlier version of this demonstration was wrong, and the way it was wrong is
instructive.** The first attempt used a domain extending only to $3\delta$ and
fitted the decay over $[0.2\delta, 1.5\delta]$. The measured decay length
settled at 4830–4841 m, a *systematic* 3.8% error that did not vanish with
refinement. The cause was not the scheme: it was the artificial zero-flux
boundary at $3\delta$, where the field has only decayed to $e^{-3} = 5\%$, so
that boundary reflects. The profile matched $e^{-z/\delta}$ to better than 0.5%
inside $z<\delta$ but diverged beyond it. Extending the domain to $6\delta$
(where $e^{-6} = 0.25\%$) and fitting within $1.2\delta$ reduced the error to
$4.9\times10^{-3}$ and made it converge.

**The lesson generalises.** A residual that does not shrink with refinement is
not a discretisation error — it is either a modelling error (a boundary
condition, a truncated domain, an inconsistent scheme) or a round-off floor.
Distinguishing them is done by the log-log slope: round-off is flat, a domain or
boundary error plateaus at a value set by the geometry, and a genuine
discretisation error decreases at the scheme's order. Report the slope, not just
the error.

## 7. Python demonstration

Run `code/validation_benchmarks.py`. It performs all three checks above (order
measurement, quadrature convergence, closed-form versus independent integral),
plus the deliberate-bug test, and prints the measured numbers. Predict the order
before running, then break the stencil (change the coefficient 4 to 4.01) and
confirm that the measured order collapses.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/04-numerical-forward-modelling-exercises.md`](./exercises/04-numerical-forward-modelling-exercises.md).

**Common mistakes.** (1) Refining the grid and calling the change "convergence"
without measuring an order. (2) Attributing discretisation error to the physics.
(3) Using a tolerance below the round-off floor. (4) Forgetting that an
inconsistent scheme converges to the wrong answer. (5) Reporting a result with
no grid, no tolerance and no measured error.

**Applications.** Finite-difference and finite-element gravity/magnetic
modelling in complex 3-D geometry; finite-difference seismic wave propagation;
finite-element EM; all share this error taxonomy.

## 9. Further reading

- **LeVeque, R. J. *Finite Difference Methods for Ordinary and Partial
  Differential Equations*.** Level: graduate. The canonical treatment of
  truncation error, stability and convergence.
- **Roache, P. J. *Verification and Validation in Computational Science and
  Engineering*.** Level: graduate. Manufactured solutions and grid-convergence
  indices.
- **Salari, K. & Knupp, P. (2000).** Code verification by the method of
  manufactured solutions. Sandia Report SAND2000-1444. Level: graduate.

## 10. Related lessons

- [05-03-05 Validating Forward Codes Against Analytic Benchmarks](./05-forward-model-validation.md)
- [03-03-02 scipy.integrate](../../03-scientific-computing/03-scipy/02-integrate.md)
- [19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md)

## Self-assessment checklist

- [ ] I can derive the second-order truncation error of the 5-point Laplacian.
- [ ] I can measure a convergence order from two grid refinements.
- [ ] I can set up a manufactured solution for a solver I use.
- [ ] I can identify the round-off floor in a refinement study.
- [ ] I can state the grid, the tolerance and the measured error for any
      numerical result I report.
