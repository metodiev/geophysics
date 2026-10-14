---
id: 03-12-01
title: "A 1-D Finite-Difference Solver from Scratch"
level: intermediate
prereqs: ["03-02-04", "01-12-01"]
tags: [numerical-simulation, finite-difference, wave-equation, convergence]
---

# A 1-D Finite-Difference Solver from Scratch

A numerical solver is a short piece of code surrounded by a long argument
about whether it is right. This lesson writes the short piece — thirty lines
that solve the 1-D wave equation — and then does the long part properly:
measures the order of accuracy, finds where the scheme is exact, measures the
numerical dispersion, checks energy conservation, and finds the grid spacing at
which round-off replaces discretisation error.

Run the demonstration before reading on; every number below is its output.

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/finite_difference_1d_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the centred second-difference approximation of $u_{xx}$ and
   **measure** its order of accuracy.
2. **Implement** the explicit three-level scheme for $u_{tt} = c^2u_{xx}$ and
   state its two initial conditions.
3. **Measure** the order of convergence and explain why the norm and the
   sampling time must be stated with it.
4. **Explain** why the scheme is exact at Courant number 1 and identify the
   degenerate case where it is not.
5. **Measure** the numerical dispersion relation and state the practical
   resolution rule that follows.
6. **Verify** energy conservation with the correctly staggered discrete energy,
   and explain why the naive energy decays.
7. **Identify** the grid spacing at which round-off error replaces
   discretisation error.

## Prerequisites

- [03-02-04 ufuncs, Reductions, Broadcasting and Vectorisation](../02-numpy/04-ufuncs-reductions.md)
  — `np.roll` and array arithmetic.
- [01-12-01 Root Finding](../../01-mathematics/12-numerical-methods/01-root-finding.md)
  — what a numerical method's error and order mean.

## 1. Intuition: the domain of dependence

The wave equation says something local: the value at $(x, t+\Delta t)$ depends
on values at $x$ and its neighbours at $t$ and $t-\Delta t$. Discretise space
and time and you get a stencil; the stencil's **domain of dependence** is the
set of earlier grid points that can influence a given point. If the physical
wave can travel further in one time step than the stencil reaches, the scheme
is being asked to produce a solution from information it never saw, and it will
produce a diverging one instead. That is the Courant–Friedrichs–Lewy condition,
and for this scheme it is

$$r = \frac{c\,\Delta t}{\Delta x} \le 1,$$

which says: in one time step, the wave must not travel more than one grid cell.
The full analysis is in lesson
[02](./02-stability-and-cfl.md); this lesson builds the solver and measures it.

## 2. Precise definitions

### 2.1 The centred second difference

Expand $u(x \pm \Delta x)$ in Taylor series about $x$ and add:

$$u(x+\Delta x) + u(x-\Delta x) = 2u(x) + \Delta x^2 u''(x)
+ \frac{\Delta x^4}{12}u''''(x) + O(\Delta x^6),$$

so

$$u''(x) = \frac{u(x+\Delta x) - 2u(x) + u(x-\Delta x)}{\Delta x^2}
+ O(\Delta x^2).$$

The leading error term is $\frac{\Delta x^2}{12}u''''$, which is why the
approximation is second order.

### 2.2 The scheme

With $u_i^n = u(i\Delta x, n\Delta t)$ and $r = c\Delta t/\Delta x$:

$$u_i^{n+1} = 2u_i^n - u_i^{n-1} + r^2\left(u_{i+1}^n - 2u_i^n + u_{i-1}^n\right).$$

It is **explicit** (each new value is a formula, not the solution of an
equation), **three-level** (it needs two time levels to start), and
**second-order accurate** in both $\Delta x$ and $\Delta t$.

Units: $r$ is dimensionless; $c\Delta t/\Delta x$ has units
$\mathrm{(m\,s^{-1})(s)/(m)} = 1$. Every term in the update has the units of
$u$: the bracket is a difference of $u$'s and $r^2(u_{i+1}-2u_i+u_{i-1})$ is
proportional to $\Delta t^2 c^2 u_{xx}$, i.e. a displacement.

### 2.3 Two initial conditions

A second-order equation in time needs two. The demonstration launches a
**travelling** wave with the exact solution at $t = 0$ and $t = \Delta t$,
which excites one direction; and a **standing** mode with $u_t = 0$ at $t = 0$,
using the consistent first step

$$u_i^1 = u_i^0 + \tfrac{1}{2}r^2\left(u_{i+1}^0 - 2u_i^0 + u_{i-1}^0\right).$$

Using $u^{-1} = 0$ instead (a common mistake) injects a spurious initial
velocity equal to $u^0/\Delta t$ and makes the $k = 0$ mode grow linearly
without limit — measured in lesson [02](./02-stability-and-cfl.md) as the
difference between a stable run and a diverging one.

## 3. Derivations and worked reasoning

### 3.1 The convergence measurement, and the two ways to get it wrong

The demonstration solves a travelling sine wave (4 wavelengths on $L = 1$,
$c = 1$, $r = 0.5$ fixed) and measures the error as the **RMS over space and
over the whole time history**:

| nx | $\Delta x$ | steps | space–time RMS | observed order |
|---|---|---|---|---|
| 100 | 1.000e−02 | 140 | 2.516176e−02 | — |
| 200 | 5.000e−03 | 280 | 6.269440e−03 | 2.0048 |
| 400 | 2.500e−03 | 560 | 1.564829e−03 | 2.0023 |
| 800 | 1.250e−03 | 1120 | 3.908972e−04 | 2.0011 |
| 1600 | 6.250e−04 | 2240 | 9.768592e−05 | 2.0006 |
| 3200 | 3.125e−04 | 4480 | 2.441670e−05 | 2.0003 |
| 6400 | 1.563e−04 | 8960 | 6.103580e−06 | 2.0001 |

**Order 2.0000 over six refinements.** Now the trap, which the demonstration
also performs. Solve the *standing* mode, keep $r = 0.5$ fixed, and read the
error at $t = 1.0$ s only:

| nx | RMS error | observed order |
|---|---|---|
| 100 | 1.5503e−04 | — |
| 200 | 9.6819e−06 | 4.0011 |
| 400 | 6.0500e−07 | 4.0003 |
| 800 | 3.7810e−08 | 4.0001 |
| 1600 | 2.3631e−09 | 4.0000 |

**Order 4 for a second-order scheme.** The scheme is not fourth order. The
leading error is a *phase* error, $\delta\phi = O(\Delta x^2)$, and at the
instant where the mode sits at a maximum the amplitude error is
$\cos(\delta\phi) - 1 = -\delta\phi^2/2 = O(\Delta x^4)$. Sampling one instant,
or one point, or one phase can report an order the solver does not have.

The lesson to carry into every convergence study: **state the norm, the time
window and the sampling, and if you can, use a solution whose error does not
cancel.** A travelling wave does not cancel; a standing wave at an extremum
does.

### 3.2 Why $r = 1$ is exact

At $r = 1$ the update becomes
$u_i^{n+1} = u_{i+1}^n + u_{i-1}^n - u_i^{n-1}$, which is the d'Alembert shift
for a wave sampled at exactly one cell per time step. Measured, for the
travelling wave:

| nx | $r$ | max RMS error over the run |
|---|---|---|
| 50 | 1.000000 | 3.120e−15 |
| 100 | 1.000000 | 2.704e−15 |
| 200 | 1.000000 | 2.170e−15 |
| 400 | 1.000000 | 1.254e−14 |

Errors of $10^{-15}$ against a round-off level of $2.2\times10^{-16}$: the
scheme is exact to accumulated round-off. The *numerical* domain of dependence
and the physical one coincide exactly, so no interpolation error is possible.

### 3.3 The degenerate exception at $r = 1$

The same scheme, at $r = 1$, on the *shortest wave the grid can carry* —
$u_i = (-1)^i$, wavelength $2\Delta x$ — with $u_t = 0$:

| step | max $\lvert u\rvert$ | $2n - 1$ |
|---|---|---|
| 1 | 3.0 | 3 |
| 2 | 5.0 | 5 |
| 3 | 7.0 | 7 |
| 5 | 11.0 | 11 |
| 9 | 19.0 | 19 |
| 40 | 81.0 | 81 |

The amplitude grows **linearly**, $\lvert u\rvert = 2n-1$, although the exact
solution is bounded by 1. The stability polynomial has a double root at $-1$:
the frequency is exact, but the amplification matrix is *defective*, so the
exact initial condition (zero velocity) cannot be represented and the
difference grows without bound. It is a measure-zero pathology — one
wavenumber out of a continuum, and only at exactly $r = 1$ — and it is the
reason "stable" and "accurate at the grid's shortest wavelength" are different
properties. The full von Neumann analysis is in lesson
[02](./02-stability-and-cfl.md).

### 3.4 Numerical dispersion

The discrete dispersion relation, obtained by inserting
$u_i^n = G^n\mathrm{e}^{\mathrm{i}ki\Delta x}$, is

$$\omega\Delta t = 2\arcsin\!\left(r\sin\frac{k\Delta x}{2}\right),
\qquad c_{\text{num}} = \frac{\omega}{k}.$$

The demonstration launches a single complex Fourier mode and measures its
phase advance over $N$ steps:

| $k\Delta x$ | points/wavelength | $c_{\text{num}}/c$ measured | theory | difference |
|---|---|---|---|---|
| 0.0491 | 128.00 | 0.999924 | 0.999925 | −1.2e−06 |
| 0.1963 | 32.00 | 0.998721 | 0.998794 | −7.4e−05 |
| 0.3927 | 16.00 | 0.994590 | 0.995169 | −5.8e−04 |
| 0.7854 | 8.00 | 0.976087 | 0.980542 | −4.5e−03 |
| 1.5708 | 4.00 | 0.887541 | 0.920214 | −3.3e−02 |

Every discrete phase speed is below $c$, and the deficit grows as
$(k\Delta x)^2$: 0.0001 % at 128 points per wavelength, 2.4 % at 8, 11 % at 4.

The residual difference between the measurement and the theory is *not* a
theory error: it is contamination of the tracked Fourier coefficient by the
counter-propagating discrete root. Launching a genuinely one-way wave on a grid
with a second time level is not possible without knowing the answer in advance,
and saying so is more honest than quoting the theory as if it were measured.

At $k\Delta x = \pi$ the group velocity is zero: the $2\Delta x$ wave does not
propagate, it stands and oscillates. **Five to ten points per wavelength is the
practical minimum for waveform modelling**, and that number comes from the
table above.

### 3.5 Energy

The leapfrog scheme conserves a discrete energy, but only if the kinetic and
potential halves are staggered consistently:

$$E^n = \frac{1}{2}\sum_i\left(\frac{u_i^{n+1}-u_i^n}{\Delta t}\right)^2\Delta x
+ \frac{C^2}{2}\sum_i
\frac{u_{i+1}^{n+1}-u_i^{n+1}}{\Delta x}\,
\frac{u_{i+1}^{n}-u_i^{n}}{\Delta x}\,\Delta x .$$

Measured over 2000 steps:

```
steps                         : 2000
initial energy                : 1.252531e+01
final energy                  : 1.252531e+01
relative drift                : +4.219e-15
max relative excursion        : 8.216e-15
```

A drift of $4\times10^{-15}$ against a machine epsilon of $2.2\times10^{-16}$
is exact conservation to accumulated round-off. Using the gradient at a single
time level instead makes the energy decay at $O(\Delta x^2)$ — a numerical
damping that is not in the scheme, and a diagnostic that will send you hunting
for a bug in the wrong place.

### 3.6 Where round-off takes over

Using the standing-mode metric (whose error is $O(\Delta x^4)$ and therefore
reaches the floor sooner):

| nx | $\Delta x$ | steps | RMS error | order |
|---|---|---|---|---|
| 1600 | 6.250e−04 | 3200 | 2.3631e−09 | — |
| 3200 | 3.125e−04 | 6400 | 1.4770e−10 | 4.0000 |
| 6400 | 1.563e−04 | 12800 | 9.2473e−12 | 3.9975 |
| 12800 | 7.813e−05 | 25600 | 6.2027e−13 | 3.8981 |
| 25600 | 3.906e−05 | 51200 | 4.1569e−13 | 0.5774 |
| 51200 | 1.953e−05 | 102400 | 1.9805e−12 | −2.2523 |

The error falls as $\Delta x^4$ until $\Delta x \approx 8\times10^{-5}$, stops,
and then *rises*: doubling the grid doubles the number of operations and
therefore the accumulated round-off, while the discretisation error is already
below the floor. **Discretisation error is a property of the method and
decreases with refinement; round-off error is a property of the arithmetic and
grows with the number of operations.** The optimum grid is where the two cross,
and refining past it costs memory and time and buys nothing.

## 3b. Worked examples

### 3b.1 Sizing a simulation from the resolution rule

**Problem.** Model a 1 Hz Rayleigh wave crossing a 100 km basin with
$v = 3$ km/s, using 10 points per wavelength and CFL 0.5. Give the grid, the time
step, and the number of steps.

$$\lambda = \frac{v}{f} = 3\ \mathrm{km}, \qquad
\Delta x = \frac{\lambda}{10} = 0.3\ \mathrm{km},$$

$$N = \frac{100}{0.3} = 334 \ \text{cells (plus boundary region)}, \qquad
\Delta t = \frac{0.5 \times 0.3}{3} = 0.05\ \mathrm{s}.$$

The wave takes $100/3 = 33.3$ s to cross, so the run needs $33.3/0.05 = 667$
steps for the crossing plus the source's duration. Measured memory: three
arrays of 400 `float64` is 9.6 kB; operations: $667 \times 400 \times 5$ flops
$\approx 1.3\times10^{6}$ — a fraction of a second on any machine.

Now change one assumption: the target is a 0.05 Hz surface wave
($\lambda = 60$ km, $\Delta x = 6$ km — coarser, cheaper) *in a basin with a
0.3 km deep structure*. The structure is now under-resolved, and the resolution
must come from the *structure*, not the wavelength: $\Delta x = 0.1$ km, 1000
cells, $\Delta t = 0.017$ s, 6000 steps, $3\times10^{7}$ flops. **The grid is
set by the smallest feature you must resolve, which is often not the dominant
wavelength** — and that is the calculation that decides whether a simulation is
feasible.

### 3b.2 What a measured order buys you

**Problem.** A solver measures order 2.0000. Its error at 100 cells is
$2.5\times10^{-2}$. What grid is needed for an error of $10^{-3}$?

For a second-order scheme, $\text{err} = E\Delta x^2$, so reducing the error by
a factor 25 requires $\Delta x$ smaller by $\sqrt{25} = 5$:

$$nx = 100 \times 5 = 500 .$$

That is the whole value of knowing the order: **it converts a required accuracy
into a required grid without running anything.** If the measured order were 1
instead, the factor would be 25 — 2500 cells, a 25-fold increase in work and a
125-fold increase in the time-stepping cost (since $\Delta t \propto \Delta x$).

Two caveats the measurement supplies:

- **The extrapolation is valid only until the round-off floor.** Measured: the
  $\Delta x^4$ metric stops improving at about $5\times10^{-13}$, so asking for
  $10^{-14}$ is asking for something the arithmetic cannot deliver.
- **The constant $E$ is problem-specific.** A different source wavelet, a
  different boundary condition or a different norm changes $E$ while leaving the
  order at 2. Reusing a grid derived for one problem on another is an assumption,
  not a calculation.

### 3b.3 Diagnosing a solver that will not converge

**Problem.** A solver's error does not decrease under refinement. List the causes
in the order a measurement can distinguish them.

| cause | measurement that identifies it |
|---|---|
| round-off floor reached | the error *stops* falling and then rises with $1/\Delta x$; the measured floor is $\sim10^{-13}$ for the standing-mode metric |
| the time step is not refined with the grid | refine $\Delta x$ at fixed $\Delta t$ and the temporal error stops improving: the observed order falls to 0 |
| a wrong implementation (a sign, an index, a coefficient) | the error is constant and large, and the growth rate matches a *predicted* wrong-scheme rate (measured: 2.618 per step for a flipped Laplacian) |
| the metric is measuring the wrong thing | the order is *larger* than the scheme's (measured: 4.0000 for a second-order scheme when the error is sampled at a phase extremum) |
| an unstable scheme | the amplitude grows without bound; the rate matches the von Neumann prediction to machine precision |

The discriminator between the last two is direction: a wrong metric reports a
*higher* order than expected, a wrong implementation reports a lower one or a
constant. **Neither is diagnosable from a single run**: the refinement sequence
is the diagnostic.

### 3b.4 A specification written so that it can be checked

**Problem.** Write the specification for a 1-D elastic simulation so that a
reader can reproduce it and check it.

1. **Equation:** $u_{tt} = c^2u_{xx} + s(x,t)$, displacement formulation, with
   $s$ a Ricker body force of dominant frequency $f_0$.
2. **Grid:** $nx$ cells, $\Delta x = L/nx$; state $L$ and $nx$ separately.
3. **Time step:** $\Delta t = 0.5\Delta x/c_{\max}$ — state the Courant number,
   not the time step, because the Courant number transfers to another machine.
4. **Boundary:** Reynolds first order at both ends, $b = (r-1)/(r+1)$, with the
   measured reflection 0.0012 at $r = 0.5$. If a sponge is used, state its width
   and strength and its measured reflection.
5. **Initial condition:** zero displacement, zero velocity, with the consistent
   first step $u^1 = u^0 + \tfrac12r^2\mathcal{L}u^0$ (**not** $u^{-1} = 0$).
6. **Order of accuracy:** measured, with the norm and the time window, and the
   refinement sequence used to obtain it.
7. **Validation:** which analytic or independent result the solver reproduces,
   and to what accuracy.
8. **Cost:** cell count, step count, and the operation count — not the elapsed
   time.

Eight lines, each checkable by a reader with the code and one run. Compare with
the typical methods section ("we solved the wave equation on a 1000-cell grid
with a time step of 0.01 s"), which is reproducible only by accident.

## 4. Physical and computational interpretation

Three lessons the solver teaches that generalise to every finite-difference
code:

1. **Measure the order; never assert it.** The difference between "second-order
   accurate" and "here is the table, order 2.0000" is the difference between a
   claim and a result.
2. **The norm determines the answer.** A space–time RMS gives order 2; a single
   instant at a phase extremum gives order 4 for the same code.
3. **Every diagnostic has a correct form.** The energy is conserved exactly if
   it is defined with staggering; the same name used naively measures a
   non-existent damping.

## 5. Python demonstration

[`code/finite_difference_1d_demo.py`](./code/finite_difference_1d_demo.py)
contains the 12-line update plus the measurements above. It prints no
wall-clock timings: grid sizes, step counts, errors and measured orders are
machine-independent; seconds are not.

## 6. Exercises

Full solutions:
[`exercises/01-finite-difference-1d-solutions.md`](./exercises/01-finite-difference-1d-solutions.md).

### ★ Foundational

**★1.** Derive $u''(x) = (u_{i+1}-2u_i+u_{i-1})/\Delta x^2 + O(\Delta x^2)$ by
adding the Taylor expansions at $x \pm \Delta x$, and state the leading error
term.

**★2.** Show that $r = c\Delta t/\Delta x$ is dimensionless, and state the value
of $r$ used throughout the demonstration.

**★3.** Write the consistent first step for a standing mode with $u_t = 0$ at
$t = 0$, and explain what goes wrong if $u^{-1} = 0$ is used instead.

**★4.** Give the measured order of convergence for the travelling-wave test and
for the standing-mode test at $t = 1$ s, and state which one is the scheme's
true order.

### ★★ Applied

**★★5.** The standing-mode test reports order 4.0000. Derive that result: show
that the leading error is a phase error $\delta\phi = O(\Delta x^2)$ and that
the amplitude error at a phase extremum is $O(\delta\phi^2)$.

**★★6.** At $r = 1$ the travelling-wave error is $10^{-15}$ and the
$2\Delta x$ standing mode grows as $2n-1$. Reconcile the two statements, and
state precisely which initial condition produces the growth.

**★★7.** From the dispersion table, state the phase-speed deficit at 5 points
per wavelength by interpolation, and state the practical rule that follows.

**★★8.** Write the discretely conserved energy and verify the measured drift of
$4.2\times10^{-15}$ by rerunning the demonstration. Then compute the energy with
the gradient taken at a single time level and report the resulting apparent
damping.

### ★★★ Research-oriented

**★★★9.** Refine the travelling-wave test to 8 points per wavelength and
beyond, measuring the phase speed with the Fourier-phase estimator. Report the
contamination by the counter-propagating root as a function of wavenumber, and
state whether the estimator is usable above $k\Delta x = 1$.

**★★★10.** Replace the centred second difference with the fourth-order
five-point stencil $(-1, 16, -30, 16, -1)/(12\Delta x^2)$ and repeat the
convergence study. Report the measured order, the stability limit (it is not 1),
and the number of points per wavelength at which the two schemes give the same
error.
