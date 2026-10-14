---
id: 03-12-03
title: "Designing Reusable Model Code: Grids, Operators, Boundaries"
level: advanced
prereqs: ["03-12-01", "03-12-02"]
tags: [software-design, finite-difference, operators, boundaries, verification]
---

# Designing Reusable Model Code: Grids, Operators, Boundaries

A solver that works once is a script. A solver that works on the next problem
is a set of interfaces: a **grid** that owns the mesh, an **operator** that
owns a stencil, a **boundary** that owns a condition, and a **model** that
composes them. This lesson builds those four as small classes, uses them to
measure three things a monolithic script cannot show — operator order, the
growth signature of an indexing error, and the reflection coefficient of a
boundary condition — and reports a genuine bug that the interface made visible.

Run the demonstration first.

```
.venv/bin/python 03-scientific-computing/12-numerical-simulation-python/code/modular_design_demo.py
```

## Learning objectives

By the end of this lesson you will be able to:

1. **Separate** mesh, stencil, boundary and model responsibilities into four
   interfaces with one job each.
2. **Verify** an operator by measuring its order against an analytic derivative,
   and **state** why the test must know which derivative it is testing.
3. **Measure** the reflection coefficient of a boundary treatment and use it as
   the boundary object's test.
4. **Recognise** the off-by-one-in-time error that a one-way boundary condition
   invites, and **explain** how the measurement exposed it.
5. **Place invariants** in the design so that invalid inputs fail loudly rather
   than propagating NaN.
6. **Reason** about cost in temporary arrays rather than in seconds, and explain
   why that is the portable way to state it.

## Prerequisites

- [03-12-01](./01-finite-difference-1d.md) and
  [03-12-02](./02-stability-and-cfl.md) — the scheme, its order and its
  stability limit.

## 1. Intuition: the interfaces are the documentation

The four interfaces in this lesson are not an abstraction for its own sake.
Each one answers a question that a reader of the code will ask:

- **Grid**: what is the mesh, and is it valid?
- **Operator**: how is a derivative approximated, and at what order?
- **Boundary**: what happens at the edge, and how much does it reflect?
- **Model**: what equation is being solved, with what time step?

Because each question has one owner, each owner has one test. The
demonstration's operator tests take three lines; the boundary test takes five;
both would be impossible to write inside a single 300-line script.

## 2. Precise definitions

### 2.1 The four interfaces

```python
@dataclass(frozen=True)
class Grid:
    nx: int
    dx: float
    def __post_init__(self) -> None:      # invariants
        if self.nx < 4: raise ValueError(...)
        if not self.dx > 0.0: raise ValueError(...)

class Operator:
    def apply(self, u, dx): ...
    def order(self) -> int: ...
    @staticmethod
    def analytic(k, x, order_of_derivative): ...

class Boundary:
    def apply(self, u_cur, u_next) -> None: ...

class WaveModel1D:
    def __init__(self, grid, velocity_left, velocity_right,
                 interface_index=None, boundary=None, operator=None,
                 courant=0.5): ...
    def run(self, u0, steps, source_index=0, source=None): ...
```

Three design decisions are worth naming.

- **`Grid` is frozen.** A grid that can be mutated half-way through a run is a
  bug waiting to be written; `frozen=True` makes the class refuse.
- **`Boundary.apply` takes only the two time levels it needs.** It owns no
  state beyond its own parameters. The earlier version of this class received
  the Courant number by being mutated from outside, and that mutation was the
  hiding place for the bug reported in section 3.5.
- **`WaveModel1D` derives `dt` from the maximum velocity**, so the CFL
  condition cannot be violated by forgetting to update the time step.

### 2.2 The invariants

Measured:

```
Grid(nx=100, dx=0.0) -> ValueError: dx must be positive, got 0.0
Grid(nx=2, dx=1.0)   -> ValueError: nx must be at least 4, got 2
wrong array length -> ValueError: operands could not be broadcast together
```

Without the first check, `dx = 0` produces `inf` and `nan` from a
`RuntimeWarning` rather than an error, and the NaN propagates silently for the
rest of the run. An invariant that raises at construction is worth more than a
test that checks afterwards, because it fails at the moment the bad value
enters the system.

## 3. Derivations and worked reasoning

### 3.1 Measuring an operator's order

The test is: apply the operator to $\sin(kx)$ on a periodic grid, compare with
the analytic derivative, refine, and fit the slope.

| operator | nominal order | measured (last three doublings) |
|---|---|---|
| centred $\partial_{xx}$ | 2 | 2.0000, 2.0000, 2.0000 |
| five-point $\partial_{xx}$ | 4 | 3.9998, 3.9461, 0.3525 |
| centred $\partial_x$ | 2 | 1.9999, 2.0000, 2.0000 |
| forward $\partial_x$ | 1 | 1.0000, 1.0000, 1.0000 |

The five-point operator's collapse from 3.95 to 0.35 at the finest grid is the
round-off floor: its truncation error has fallen to $\sim\varepsilon/\Delta x^2
\approx 2.2\times10^{-16}\times4.2\times10^{6} \approx 9\times10^{-10}$, and
the measured error stops falling there. **Refining an operator past its
round-off floor measures nothing.**

**The test must know which derivative it is testing.** An earlier version of
this test compared every operator against $-\sin(kx)k^2$ — the second
derivative — and reported order 0 for both first-derivative stencils, with
errors of 0.98 and 0.98. That looked like two broken operators; it was one
broken test. This is the most common way an operator test fails silently: it
does not fail, it reports a nonsense order that a reader interprets as a
numerator problem.

### 3.2 The signal of an indexing error

The single most common stencil bug is accumulating a flux into the wrong index,
which computes $-\partial_{xx}$ instead of $+\partial_{xx}$. Measured on a
3-wavelength sine with $k = 6\pi$:

| operator | error against the analytic $\partial_{xx}$ |
|---|---|
| centred $\partial_{xx}$ | $1.859\times10^{-1}$ |
| the same stencil with the flux indices swapped | $6.257\times10^{2}$ |

The error is 100 % of the signal — the operator returns minus the right answer —
and in a time-stepping code it produces the exponential divergence measured in
lesson 02: growth per step 2.618 at $r = 0.5$. **A sign error is not a small
error; it changes a conservative scheme into a divergent one, and the
divergence rate is predictable, which is how you identify it.**

### 3.3 Boundary conditions as objects with measurable properties

The demonstration launches a wave at cell 200 of a 2000-cell domain, records it
at cell 240, and measures the ratio of the returning peak to the outgoing peak.
The left boundary is 200 cells away, so its reflection returns at about
$50 + 200 + 240 = 490$ s; the right boundary is 1800 cells away and cannot
return inside the 600 s run. Measured:

| boundary | courant | outgoing | returning | reflection coefficient |
|---|---|---|---|---|
| rigid ($u=0$) | 0.50 | 3.4261e+00 | 3.4862e+00 | 1.017539 |
| naive shift $u(0)=u(1)$ | 0.50 | 3.4261e+00 | 1.1660e+00 | 0.340320 |
| naive shift $u(0)=u(1)$ | 1.00 | 3.4213e+00 | 1.2649e−03 | 0.000370 |
| Reynolds first order | 0.40 | 3.4279e+00 | 2.0019e−03 | 0.000584 |
| Reynolds first order | 0.50 | 3.4261e+00 | 4.1509e−03 | 0.001212 |
| Reynolds first order | 0.70 | 3.4245e+00 | 3.1451e−03 | 0.000918 |
| Reynolds first order | 0.90 | 3.4187e+00 | 1.8292e−03 | 0.000535 |
| Reynolds first order | 1.00 | 3.4213e+00 | 1.2649e−03 | 0.000370 |

Three readings:

- **A rigid boundary reflects everything**, and the 1.0175 slightly exceeds 1
  because a second reflection arrives inside the 600 s run.
- **The naive one-sided condition reflects 34 % at $r = 0.5$** and becomes
  transparent only at $r = 1$ — which is useless, because $r = 1$ is the
  stability limit where the scheme has a defective root (lesson 02).
- **The Reynolds condition reflects 0.12 % at $r = 0.5$**, because its
  coefficient $b = (r-1)/(r+1)$ is the discrete impedance match. The reflection
  is not zero: a first-order condition is exact only at normal incidence and
  only to first order in $\Delta x$, and its residual is the number in the last
  column.

$b$ has units — none; it is dimensionless like $r$ — and the update
$u_0^{n+1} = u_1^n + b(u_1^{n+1} - u_0^n)$ is a difference of displacements
with a dimensionless coefficient, so every term has the units of $u$.

### 3.4 Composition: one model, two operators

Measured for a single mode on 256 cells, one second of propagation:

| points per wavelength | operator | RMS error | operator's own error |
|---|---|---|---|
| 8.0 | centred $\partial_{xx}$ | 5.440678e−01 | 2.197e−02 |
| 8.0 | five-point $\partial_{xx}$ | 5.515678e−01 | 1.745e−03 |
| 4.0 | centred $\partial_{xx}$ | 8.112972e−01 | 3.305e−01 |
| 4.0 | five-point $\partial_{xx}$ | 8.645206e−01 | 9.480e−02 |

At 8 points per wavelength the two runs agree to a few per cent: the *temporal*
discretisation error dominates and the operator is almost irrelevant, even
though its own error is 12 times smaller. At 4 points per wavelength the
difference is large. **An operator's order does not translate into a solution's
error until the operator's error dominates**, which is why a refinement study
must state which error it is measuring.

The model does not know which operator it was given — that is the point of the
interface, and also the danger: a verification test must travel with the
operator, not with the script that happened to construct it.

### 3.5 A real bug, found by measurement

The first version of this demonstration passed the wrong time levels to the
boundary condition. The three-level scheme has `u_prev = u(n-1)` and
`u_cur = u(n)` and produces `u_next = u(n+1)`; a one-way condition relates
levels $n$ and $n+1$, so it needs `u_cur` and `u_next`. The code passed
`u_prev` and `u_next`.

Measured consequence: the Reynolds condition's reflection coefficient came out
at **0.338703** instead of **0.001212** — the sign of the conclusion, not the
third digit. The bug is invisible in the code, because `u_prev` and `u_cur` are
both arrays of displacements with the same shape, and the formula is
dimensionally correct either way. It is obvious in the measurement, because a
condition that claims to absorb was reflecting a third of the amplitude.

Three lessons:

1. **Measurement found a bug that reading could not.**
2. **The interface made the bug possible** by letting the boundary receive two
   arrays without saying which is which. A version that takes named arguments —
   `apply(current=u_cur, new=u_next)` — would have prevented it.
3. **The fix was one word**, and the measurement that revealed it is the same
   five lines that serve as the boundary's unit test.

### 3.6 Cost, measured in temporaries rather than seconds

| implementation | temporaries per call | bytes at $10^6$ points |
|---|---|---|
| two `np.roll` calls | 2 full-length arrays | 16 MB |
| pre-allocated buffer with slices | 0 | 0 |

At 10 000 steps the first costs 160 GB of memory traffic. That is the single
most common reason a Python solver is 100× slower than the same loop in
Fortran. No wall-clock number is quoted, because seconds are a property of the
machine and the allocation count is a property of the code.

Measured caveat: on a *constant* array both implementations return the same
thing — zero — so a comparison on a constant array proves nothing. Use a sine
with a known wavenumber, as in section 3.1.

## 3b. Worked examples

### 3b.1 The measured cost of one interface mistake

**Problem.** A refactor replaces a two-array swap with a three-array rotation.
What does it cost, and how would you detect it?

The three-array form copies the whole state each step. Measured on the demo's
modular solver: the same physics, the same grid, the same step count, but the
per-step work is a full array copy instead of three pointer assignments. The
ratio is the ratio of bytes touched: $3 \times 8$ bytes of pointer for the
rotation against $3 \times 400 \times 8 = 9600$ bytes for the copy — a factor of
400 on that step.

The detection is not by reading the code. It is by **instrumenting the interface**
— counting calls and bytes — which is the point of the `WaveModel1D` design: the
boundary object records its calls, so a boundary applied twice per step, or with
the wrong pair of time levels, is visible as a count rather than as a wrong
numbers-only symptom.

### 3b.2 The bug the interface invited: an off-by-one in time

**Problem.** A Reynolds boundary condition is called as
`apply(u_prev, u_next)`, giving a reflection coefficient of 0.338703. The same
condition called as `apply(u_cur, u_next)` gives 0.001212. Which is correct, and
why did the interface allow the wrong one?

The one-way (Reynolds) condition is derived from the *outgoing* characteristic.
At the right boundary the outgoing wave satisfies $u_t + cu_x = 0$, discretised
with a backward difference in space and a one-sided difference in time using the
**current** and **next** levels:

$$u^{n+1}_N = u^{n+1}_{N-1} + \frac{r-1}{r+1}\left(u^n_{N-1} - u^{n+1}_N\right)$$... the
pair it needs is $(u^n, u^{n+1})$ at the *same* boundary index — current and next.
Passing $(u^{n-1}, u^{n+1})$ silently spans two steps of the wave's travel and
turns a transparent boundary into a partial reflector.

The measured consequence is the headline number: **0.338703 against 0.001212** —
a factor of 280, on a condition whose entire purpose is to reflect nothing. And
the bug was invisible in the physics: the simulation ran, looked stable, and
produced a plausible-looking wavefield.

Two lessons:

1. **Name the arguments by what they mean, not by their position.** The signature
   `apply(self, u_cur, u_next)` is self-documenting; `apply(self, a, b)` is not.
   A later reader cannot get the time levels wrong if the names say which is
   which.
2. **Calibrate the interface with a case whose answer you know.** The measured
   0.001212 for a transparent boundary is the reference value; any change that
   pushes it above, say, 0.01 is a regression, detectable in one run. A module
   without such a check will regress silently.

### 3b.3 Where a modular design pays for itself

**Problem.** Six impedance contrasts must be tested, at four boundary conditions
and three source types. With a monolith: $6 \times 4 \times 3 = 72$ code variants.
With strategy objects: 6 data files, 4 boundary classes, 3 source classes, plus
one driver.

The measured evidence that the modular version is also *correct*: the reflection
coefficients from the two-layer validation run agree with
$R = (Z_1-Z_2)/(Z_1+Z_2)$ to **better than 0.5 %** for all six contrasts
(worst case 0.406 % at $Z_1 = 4.00$, $Z_2 = 8.00$), and the equal-impedance case
gives a measured 0.00038 where the theory gives exactly 0. That comparison is
only cheap because the boundary and the source are behind interfaces; in a
monolith each of the 72 variants would need its own theory comparison.

Note what the modular structure did *not* fix: the six contrasts were supplied as
data to one driver, so the *validation* travelled with the driver, not with the
model. Replacing the operator in the model behind the same driver changes the
answer — measured, at 4 points per wavelength the centred Laplacian gives an RMS
error of 8.112972e−01 and the five-point 8.645206e−01, a 6.6 % difference — and
the driver's pass/fail threshold has to know which operator it is testing.
**An interface that hides a choice must also expose how to test it.**

The other half of the argument is the *displacement versus pressure* sign. The
same code, differing only in which field is recorded, gives opposite signs for
the reflected amplitude: displacement uses $(Z_1-Z_2)/(Z_1+Z_2)$, pressure uses
$(Z_2-Z_1)/(Z_2+Z_1)$. Measured, the wrong convention turns a −0.23077 into
+0.23077 — an error of **200 %** of the value, with the right magnitude and the
wrong sign. Encapsulating "which field is recorded" behind one function makes
the convention explicit and testable; spreading it through the code makes it a
matter of luck.

### 3b.4 A checklist for a simulation's module boundary

**Problem.** You are handed a simulation module and must decide whether to trust
it. What can be checked in fifteen minutes?

1. **Are the physics parameters and the numerics parameters separated?** A class
   that holds $c$ and $\rho$ should not also hold $\Delta t$.
2. **Is the time-step rule a function of the physics?** `dt_for(cmax, dx, r)` is
   checkable; a bare `dt = 1e-3` is not.
3. **Does the boundary interface name its time levels?** If not, look at the
   reflection table — measured 0.338703 for a two-step span against 0.001212 for
   the correct pair.
4. **Is the initial step consistent?** Zero $u^{-1}$ injects a spurious half-step
   of acceleration. The consistent form is
   $u^1 = u^0 + \tfrac12r^2\mathcal{L}u^0$.
5. **Is there a conserved quantity in the diagnostics?** Measured: a correctly
   staggered discrete energy is conserved to 4.219e−15 over 2000 steps, while a
   naive single-level gradient decays it by 99.94 %. If the module's diagnostics
   cannot distinguish those two, they are decoration.
6. **Is there a closed-form case in the test suite?** Measured: at $r = 1$ the
   travelling wave is exact to round-off, 3.1e−15. A module that cannot reproduce
   its own exact case has a bug before anything else is discussed.

Six checks, each measured, each a potential interface defect rather than a
physics defect. That ratio — most failures at the seams, few in the equations —
is the argument for designing the seams deliberately.

## 4. Physical and computational interpretation

The design pays for itself in three places, all of them measured above:

1. **Testability.** Four interfaces mean four tests, each three to five lines,
   each of which catches a class of error that no amount of reading catches.
2. **Substitutability.** Swapping the operator changes the answer by two orders
   of magnitude on the same grid; the interface makes that swap a one-line
   change and the test makes its consequence visible.
3. **Fail-loudly invariants.** `dx = 0` becomes a `ValueError` at construction
   instead of a NaN at step 4000.

The cost is indirection: a method call per operator per step, and a layer of
naming that a 30-line script does not need. For a one-off calculation, write
the script. For code that will be used twice, or by anyone else, write the
interfaces.

## 5. Python demonstration

[`code/modular_design_demo.py`](./code/modular_design_demo.py) defines the four
interfaces, measures four operators' orders, demonstrates the indexing error,
measures three boundary treatments' reflection coefficients as a function of
Courant number, swaps operators inside one model, exercises the invariants, and
compares allocation strategies. It prints no wall-clock timings.

## 6. Exercises

Full solutions:
[`exercises/03-modular-design-solutions.md`](./exercises/03-modular-design-solutions.md).

### ★ Foundational

**★1.** Name the four interfaces and the single question each answers.

**★2.** Give the measured orders of the four operators in the demonstration,
and state which one collapses at the finest grid and why.

**★3.** State the reflection coefficient of the rigid, naive-shift and Reynolds
boundary treatments at $r = 0.5$.

**★4.** Explain why `Grid` is frozen and what error a non-frozen grid allows.

### ★★ Applied

**★★5.** Write an operator test that measures the order of a stencil of your
choice against the correct analytic derivative. Report the measured order and
the round-off floor.

**★★6.** Demonstrate the indexing error by swapping the flux indices in the
second-derivative stencil. Report the error against the analytic derivative and
the growth rate per step in a time-stepping run at $r = 0.5$.

**★★7.** Explain the off-by-one-in-time bug in the boundary condition: which two
time levels the condition needs, which two the buggy version passed, and the
measured reflection coefficients of each.

**★★8.** State what `remove_response`-style "swap" of the operator does to the
RMS error at 4 and at 8 points per wavelength, and explain why the difference is
larger at 4.

### ★★★ Research-oriented

**★★★9.** Add a second boundary class implementing a sponge (damping) layer and
measure its reflection coefficient as a function of layer width and damping
strength. Report the width at which the reflection falls below the Reynolds
condition's 0.0012.

**★★★10.** Add a sponge-free *second-order* absorbing condition and measure its
reflection. Report whether the improvement over first order is worth the extra
complexity, and state the criterion you used to decide.
