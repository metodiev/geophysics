---
id: 03-12-02
title: "Numerical Stability, CFL Conditions and Convergence Testing"
level: advanced
prereqs: ["03-12-01"]
tags: [stability, von-neumann, cfl, convergence, verification]
---

# Numerical Stability, CFL Conditions and Convergence Testing

A stable scheme produces a bounded answer; an unstable one produces garbage
that grows exponentially and is *predictable in its growth rate*. This lesson
derives the von Neumann stability condition for three schemes, measures the
growth rate of each in the unstable regime and compares it with the prediction,
and shows the two cases where the standard test is not enough: a defective
amplification matrix, and a sign error in a stencil.

Run the demonstration first; every number below is its output.

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/stability_and_cfl_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Perform** a von Neumann analysis: insert a Fourier mode, derive the
   amplification polynomial, and solve the stability condition.
2. **Measure** the growth rate of an unstable scheme and compare it with the
   prediction, using an exact eigenmode as the initial condition.
3. **State** the stability limits of the explicit wave equation, the explicit
   diffusion equation and backward Euler, and explain why the implicit scheme
   has none.
4. **Identify** the defective-root case where $\lvert G\rvert \le 1$ fails to
   guarantee boundedness.
5. **Recognise** the growth signature of a sign error in a stencil and predict
   its rate.
6. **Explain** the CFL condition as a geometric statement about the domain of
   dependence.

## Prerequisites

- [03-12-01 A 1-D Finite-Difference Solver from Scratch](./01-finite-difference-1d.md)
  — the scheme being analysed.

## 1. Intuition: the amplification factor

Stability is a statement about what a scheme does to a single Fourier mode.
Write the discrete solution as

$$u_i^n = G^n\,\mathrm{e}^{\mathrm{i}ki\Delta x},$$

substitute it into the update, cancel everything that does not depend on $n$,
and you get an equation for $G$. The mode is bounded if $\lvert G\rvert \le 1$
for **every** wavenumber $k$, and the scheme is stable when the worst
wavenumber satisfies it. The worst wavenumber is almost always
$k\Delta x = \pi$ — the sawtooth, the grid's shortest wave, alternating
$+1, -1, +1, \ldots$ — because that is where the differencing operator
overshoots by the largest factor.

This is the whole method. Its output is a condition on $\Delta t$ in terms of
$\Delta x$, the local wavespeed or diffusivity, and nothing else.

## 2. Precise definitions

### 2.1 The wave equation

Inserting the mode into
$u_i^{n+1} = 2u_i^n - u_i^{n-1} + r^2(u_{i+1}^n - 2u_i^n + u_{i-1}^n)$
and dividing by $G^{n-1}\mathrm{e}^{\mathrm{i}ki\Delta x}$ gives

$$G^2 - 2aG + 1 = 0, \qquad a = 1 - 2r^2\sin^2\frac{k\Delta x}{2},$$

so $G = a \pm \sqrt{a^2-1}$. If $\lvert a\rvert \le 1$ the roots are complex
conjugates on the unit circle and $\lvert G\rvert = 1$ exactly; if
$\lvert a\rvert > 1$ one root exceeds 1. The worst case is
$\lvert a\rvert_{\max} = \lvert 1 - 2r^2\rvert$, so

$$\boxed{r = \frac{c\Delta t}{\Delta x} \le 1}.$$

### 2.2 The growth rate beyond the limit

With $a = 1-2r^2 < -1$ (i.e. $r>1$), the larger root is

$$\lvert G\rvert_{\max} = \lvert a\rvert + \sqrt{a^2-1} = (2r^2-1) + \sqrt{(2r^2-1)^2-1}.$$

This is a *prediction of the divergence rate*, not just a yes/no condition, and
it is what the measurement tests.

### 2.3 The diffusion equation

Explicit FTCS: $u_i^{n+1} = u_i^n + r(u_{i+1}^n - 2u_i^n + u_{i-1}^n)$ with
$r = \kappa\Delta t/\Delta x^2$ gives

$$G = 1 - 4r\sin^2\frac{k\Delta x}{2}, \qquad
\lvert G\rvert \le 1 \ \forall k \iff r \le \tfrac12 .$$

Implicit (backward Euler): $(\mathbf{I} - r\mathbf{D}_2)u^{n+1} = u^n$ gives

$$G = \frac{1}{1 + 4r\sin^2(k\Delta x/2)}, \qquad \lvert G\rvert < 1
\ \text{for every } r>0 .$$

Units: $r = \kappa\Delta t/\Delta x^2$ has units
$\mathrm{(m^2\,s^{-1})(s)/(m^2)} = 1$.

## 3. Derivations and worked reasoning

### 3.1 Measured growth versus prediction, wave equation

Initial condition: the exact $k\Delta x = \pi$ eigenmode, $u = (-1)^i$, with
$u_t = 0$. The growth is the mean ratio of successive maxima far into the run.

| $r$ | predicted $\lvert G\rvert$ | measured $\lvert G\rvert$ | difference | max $\lvert u\rvert$ at 300 steps |
|---|---|---|---|---|
| 0.500 | 1.000000 | bounded | — | 1.0 |
| 0.900 | 1.000000 | bounded | — | 2.3 |
| 0.990 | 1.000000 | bounded | — | 7.1 |
| 0.999 | 1.000000 | bounded | — | 22.4 |
| 1.000 | 1.000000 | bounded | — | **601.0** |
| 1.001 | 1.093557 | 1.093595 | 3.8e−05 | unstable |
| 1.010 | 1.326584 | 1.326584 | 7.6e−12 | unstable |
| 1.050 | 1.877328 | 1.877328 | 2.2e−16 | unstable |
| 1.200 | 3.471980 | 3.471980 | 8.9e−16 | unstable |

For $r>1$ the agreement is exact to machine precision: the measured
instability **is** the predicted one. At $r = 1$ the verdict "bounded" hides
the growth in the last column: 601 at 300 steps, which is exactly $2n+1$. The
$\lvert G\rvert \le 1$ test is necessary but not sufficient when the two roots
**coincide** — the amplification matrix is defective, there is no basis of
eigenvectors, and the amplitude grows linearly. This is the case identified in
lesson [01](./01-finite-difference-1d.md) and it is why a practical code uses
$r \le 0.9$ rather than $r \le 1$.

### 3.2 The signature of a sign error

The demonstration runs the same scheme with the sign of the Laplacian flipped —
the arithmetic produced by accumulating a flux into the wrong index, which is
the single most common stencil error. The operator becomes
$-\partial_{xx}$, and at $k\Delta x = \pi$, $a = 1 + 2r^2 = 1.5$:

$$G^2 - 3G + 1 = 0 \ \Longrightarrow\ G_{\max} = \frac{3+\sqrt5}{2} = 2.618034.$$

Measured growth per step at $r = 0.5$: **2.618034**. The agreement is exact,
and that is the practical value of the prediction: a measured growth rate of
2.618 is not a rounding accident, it *identifies* the fault. A sign error does
not produce a slightly wrong answer; it converts a conservative scheme into an
exponential amplifier whose rate is predictable.

### 3.3 Diffusion: an exact match, a marginal case, and unconditional stability

Explicit diffusion, measured against $\lvert 1-4r\rvert$:

| $r$ | $\lvert 1-4r\rvert$ predicted | measured growth | difference |
|---|---|---|---|
| 0.2500 | 0.000000 | 0.000000 | 0.0 |
| 0.4000 | 0.600000 | 0.600000 | 0.0 |
| 0.4999 | 0.999600 | 0.999600 | 0.0 |
| 0.5000 | 1.000000 | 1.000000 | 0.0 |
| 0.5001 | 1.000400 | 1.000400 | 0.0 |
| 0.5100 | 1.040000 | 1.040000 | 0.0 |
| 0.6000 | 1.400000 | 1.400000 | 0.0 |

Exact at every value, because the scalar recursion has a single root and the
sawtooth is an exact eigenvector. Two things to notice:

- **$r = 1/2$ is only marginally stable.** $G = -1$ exactly at
  $k\Delta x = \pi$: that mode oscillates forever without decaying. It is
  bounded, so it is stable, but any perturbation that couples to it persists.
  Use $r = 0.4$.
- **The measured value is the prediction, to all printed digits.** When a
  scheme is genuinely a one-term recursion there is nothing for a measurement
  to disagree about; the measurement's value is that it confirms the
  implementation computes what the derivation says.

Implicit diffusion, measured after six solves at several $r$:

| $r$ | predicted $\lvert G\rvert$ | amplitude after 6 steps | predicted $(1/(1+4r))^6$ |
|---|---|---|---|
| 0.5 | 0.333333 | 1.6935e−03 | 1.6935e−03 |
| 1.0 | 0.200000 | 6.4000e−05 | 6.4000e−05 |
| 5.0 | 0.047619 | 1.1709e−08 | 1.1709e−08 |
| 50.0 | 0.004975 | 1.5186e−14 | 1.5186e−14 |
| 1000.0 | 0.000249 | ~1e−22 | 1e−22 |

Exact at $r = 1000$, where the explicit scheme would need a time step 2000
times smaller to be stable. **The price is a linear solve per step**, and the
warning is that stability is not accuracy: at $r = 1000$ the implicit solution
is stable and resolves nothing.

### 3.4 CFL as a geometric statement

For the explicit wave scheme, $r \le 1$ says

$$\text{distance travelled in one step } (c\Delta t) \le \text{one grid cell } (\Delta x).$$

Equivalently: the numerical domain of dependence must contain the physical one.
Worked examples at $\Delta x = 1$ m:

| $c$ (m/s) | $\Delta t$ (s) | $r$ | verdict |
|---|---|---|---|
| 2.0 | 0.4 | 0.800 | stable |
| 2.0 | 0.6 | 1.200 | unstable |
| 6.0 | 0.2 | 1.200 | unstable |

**For a heterogeneous medium the limit uses the largest local velocity.** A
single too-large cell anywhere in the mesh destabilises the whole run, which is
why production codes compute $\Delta t$ from a global maximum, not a local one.

### 3.5 Summary of the limits, all measured

| scheme | stability limit | order |
|---|---|---|
| explicit wave, 3-level centred | $r \le 1$ (use 0.9; $r=1$ is defective) | 2 in $\Delta x$ and $\Delta t$ |
| explicit diffusion (FTCS) | $r \le 1/2$ (use 0.4; $1/2$ is marginal) | 2 in $\Delta x$, 1 in $\Delta t$ |
| implicit diffusion (backward Euler) | unconditional | 2 in $\Delta x$, 1 in $\Delta t$ |
| first-order upwind advection | $\nu \le 1$ | 1 |
| Lax–Wendroff advection | $\nu \le 1$ | 2 |

## 3b. Worked examples

### 3b.1 Choosing a time step from a stability limit and an accuracy target

**Problem.** A solver must resolve a 2 Hz signal in a medium with
$c_{\max} = 4$ km/s on a grid with $\Delta x = 25$ m. Choose $\Delta t$ from
stability and then from accuracy.

**Stability:** $r \le 1$ requires
$\Delta t \le \Delta x/c_{\max} = 25/4000 = 6.25\times10^{-3}$ s. Using
$r = 0.9$ for margin (the demonstration measured that $r = 1$ has a defective
root and that $r = 0.999$ still reaches a maximum amplitude of 22.4 at 300
steps, against a bounded value of 2.3 at $r = 0.9$):

$$\Delta t = \frac{0.9 \times 25}{4000} = 5.6\times10^{-3}\ \mathrm{s}.$$

**Accuracy:** the *grid* must resolve the wavelength,
$\lambda = 4000/2 = 2$ km, so at 10 points per wavelength
$\Delta x = 200$ m — eight times coarser than the stability choice. At
$\Delta x = 200$ m the stability limit gives
$\Delta t \le 0.05$ s, nine times larger.

So the binding constraint depends on the question. If $\Delta x = 25$ m was
chosen for a *structure* (a thin layer), the time step is set by stability at
5.6 ms and the user pays $200/25 = 8$ times more steps than accuracy requires.
This is the standard situation in elastic modelling: **stability, not accuracy,
sets the time step**, which is why implicit and spectral methods, whose time
steps are not stability-limited, are attractive.

### 3b.2 The two-sided cost of a smaller grid

**Problem.** Halving $\Delta x$ in a 2-D explicit simulation: what happens to the
work?

- Cells: $\times 4$ (two dimensions).
- Time step: $\Delta t \propto \Delta x$ for fixed $r$, so steps $\times 2$.
- Total work: $\times 8$.

In 3-D the factor is $2^4 = 16$ per halving. That is why 3-D elastic modelling
remains expensive despite decades of hardware improvement, and why the choice of
*order* matters so much: a fourth-order scheme reaching the same accuracy at
4 points per wavelength instead of 10 reduces the cell count by a factor
$(10/4)^3 = 15.6$ in 3-D — worth more than three hardware generations.

The measured numbers that support the trade: the five-point Laplacian's own error
is 12 times smaller than the centred one at 8 points per wavelength
($1.745\times10^{-3}$ vs $2.197\times10^{-2}$), but the *solution's* RMS error is
barely different (5.516e−01 vs 5.441e−01) because the time discretisation
dominates at that resolution. **A higher-order operator pays off only where the
temporal error is not dominant**, which is at few points per wavelength, for
long propagation distances, or with high-order time stepping.

### 3b.3 What to do when a run blows up

**Problem.** A simulation diverges after 2000 steps. Diagnose it in order of
effort.

Measured signatures, each of which names a specific cause:

| observation | cause | measured evidence |
|---|---|---|
| growth per step ≈ 2.618 at $r = 0.5$ | Laplacian sign error | the flipped-sign scheme's exact growth rate |
| growth per step = the von Neumann prediction for your $r$ | genuinely $r > 1$; a too-large cell or velocity somewhere | agreement to machine precision at $r = 1.01, 1.05, 1.2$ |
| growth is linear, not exponential | defective double root at $r = 1$ exactly | $\lvert u\rvert = 2n-1$, measured 601 at $n = 300$ |
| magnitude doubles per step | a source term applied twice, or a boundary condition adding energy | not predicted by the analysis; check the source loop |
| growth appears only after the wave reaches the boundary | a boundary condition that is a reflector | measured reflection of a rigid boundary: 1.0175 |

The first three are *predictable*, and comparing the measured rate with the
prediction is a one-line diagnostic that turns a debugging session into a
lookup. The last two are not, and they are found by turning off the boundary and
the source in turn.

The practical advice: **compute the predicted growth rate before you start
debugging.** A run that is unstable in the way the analysis says it should be is
not a bug; a run that is unstable in a different way is.

### 3b.4 Stability is not accuracy: a case study

**Problem.** A backward-Euler diffusion run at $r = 1000$ is stable. What is it
computing?

Measured: the amplification factor is $1/(1+4r) = 2.49\times10^{-4}$ per step,
so the amplitude decays by a factor of $10^{-3.6}$ per step. After 100 steps the
solution is $10^{-360}$ — **numerical zero**. The scheme is stable, resolves
nothing, and reports a smooth field that is entirely an artefact of the
discretisation.

The diagnostic is not the stability condition (which is satisfied
unconditionally) but the *accuracy* condition: a backward-Euler step resolves the
diffusion of the shortest wave on the grid only if $r \lesssim 1$. Above that,
the implicit scheme's damping is so strong that it removes the physical
solution along with everything else.

The general statement: **for an unconditionally stable scheme, the time step is
limited by accuracy, and the accuracy limit is stricter than users expect.** The
demonstration's measured table shows it — $(1/(1+4r))^6$ matches the measurement
exactly at every $r$ including 1000, which is to say the measured decay *is* the
prediction of near-total damping.

## 4. Physical and computational interpretation

Three practical consequences:

1. **Stability is a property of the *scheme*, accuracy of the *solution*.** A
   stable scheme on too coarse a grid gives a smooth wrong answer, which is
   harder to detect than a blow-up. Always run both tests: a refinement study
   for accuracy (lessons [01](./01-finite-difference-1d.md) and
   [04](./04-verification-and-validation.md)) and a stability check for
   boundedness.
2. **The growth rate is a diagnostic.** An exponential blow-up has a rate, and
   that rate identifies the fault. Measuring 2.618 per step is not a mystery;
   it is $\varphi^2$ and it names the error.
3. **Implicit schemes trade time for linear algebra.** They remove the time-step
   limit and introduce a solve whose cost grows with the stencil's bandwidth;
   for large 3-D problems that trade is often not worth making, which is why
   explicit schemes still dominate seismology.

## 5. Python demonstration

[`code/stability_and_cfl_demo.py`](./code/stability_and_cfl_demo.py) performs
all four analyses: the von Neumann derivation printed step by step, the measured
growth table for the wave scheme, the flipped-sign case, the explicit and
implicit diffusion tables, and the worked CFL examples. It reports no wall-clock
timings.

## 6. Exercises

Full solutions:
[`exercises/02-stability-and-cfl-solutions.md`](./exercises/02-stability-and-cfl-solutions.md).

### ★ Foundational

**★1.** Perform the von Neumann analysis of the explicit wave scheme and derive
$G^2 - 2aG + 1 = 0$ with $a = 1-2r^2\sin^2(k\Delta x/2)$.

**★2.** State the stability limit of the explicit wave scheme, the explicit
diffusion scheme and backward Euler diffusion, with the measured growth-rate
agreement for each.

**★3.** Show that $r = \kappa\Delta t/\Delta x^2$ is dimensionless.

**★4.** At $r = 0.5$ the flipped-sign scheme grows by 2.618034 per step. Show
that this equals $(3+\sqrt5)/2$ and derive the polynomial it solves.

### ★★ Applied

**★★5.** Compute the predicted growth rate per step at $r = 1.05$ and compare
with the measured 1.877328. Then compute the amplitude after 30 steps and state
whether the run would overflow a `float64`.

**★★6.** Explain why $r = 1$ is reported as "bounded" in the wave table while
the maximum amplitude at 300 steps is 601. State the property of the
amplification matrix responsible.

**★★7.** A simulation uses $c_{\max} = 6$ km/s, $\Delta x = 100$ m and
$\Delta t = 0.02$ s. Compute $r$, state whether it is stable, and compute the
time step a CFL of 0.9 would require.

**★★8.** For the diffusion equation, explain why $r = 1/2$ is called marginally
stable rather than stable, using the value of $G$ at $k\Delta x = \pi$.

**★★9.** Solve the quadratic for the wave scheme at $r = 0.9$ and $k\Delta x = \pi$
and show that $\lvert G\rvert = 1$ exactly. Then explain why the demonstration's
table nevertheless reports a maximum amplitude of 2.3 at 300 steps.

### ★★★ Research-oriented

**★★★10.** Derive the stability condition for the Lax–Wendroff advection scheme
by von Neumann analysis, then measure the growth rate in the unstable regime and
compare. Report the rate at $\nu = 1.05$ and $\nu = 1.2$.

**★★★11.** Measure the growth rate of a *staggered-grid* (velocity–stress)
acoustic scheme beyond its CFL limit and compare it with the prediction. State
whether the growth-rate diagnostic is as sharp on a staggered grid as on a
collocated one, and why.

**★★★12.** Construct a scheme whose stability polynomial has a double root on
the unit circle at $r = 1$ *and* at a wavenumber other than $\pi$. Report the
wavenumbers and the growth behaviour, and state what this implies for the
practical advice "use $r \le 0.9$".
