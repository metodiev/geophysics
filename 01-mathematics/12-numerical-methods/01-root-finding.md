---
id: 01-12-01
title: "Root Finding: Bisection, Newton, Secant and Robust Hybrids"
level: intermediate
prereqs: ["01-01-04", "01-02-02", "01-05-02"]
estimated_minutes: 90
tags: [numerical-methods, root-finding, newton-method, convergence-order]
---

# Root Finding: Bisection, Newton, Secant and Robust Hybrids

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** the order of convergence of an iteration and measure it from a
   sequence of errors rather than assuming it.
2. **Derive** the convergence rate of bisection ($\tfrac12$ per step) and of
   Newton's method (quadratic) from first principles, and the golden-ratio order
   of the secant method.
3. **Choose** a method from the information actually available: a bracket, an
   analytic derivative, or neither.
4. **Recognise** and repair the three standard failures of Newton's method —
   a vanishing derivative, an overshoot out of the physical range, and a cycle.
5. **Formulate** a geophysical inverse problem as a root-finding problem in
   several unknowns, and solve it by Newton's method on the normal equations.
6. **State** the assumptions each method needs, and what happens when they fail.

## Prerequisites

[01-01-04 Floating-Point Representation, Round-Off and Catastrophic
Cancellation](../01-arithmetic/04-floating-point.md) — the error floor that every
iteration eventually meets. [01-02-02 Functions and Graphs](../02-algebra/02-functions-and-graphs.md)
— what a root is, and how to see whether one is bracketed. [01-05-02
Derivatives](../05-single-variable-calculus/02-derivatives.md) — the Taylor
expansion, which is the whole engine of the convergence analysis below.

## 1. Intuition: one question, three currencies

Every root-finding problem is the same question: find $x$ with $f(x)=0$. What
differs is what you are willing to assume and what you are willing to pay.

- If you can **bracket** the root — find $a<b$ with $f(a)$ and $f(b)$ of opposite
  sign — then a root exists in between, and you can locate it by halving. The
  cost is one function evaluation per binary digit, and the guarantee is total.
- If you can compute a **derivative**, you can extrapolate along the tangent and
  the number of correct digits doubles per step. The cost is a local guarantee
  only: Newton's method can overshoot, cycle, or run away.
- If you have **neither**, you can replace the derivative by a chord between two
  points. You give up a little order and keep most of the speed.

Gauss described the situation in terms of "the astronomer's dilemma": the fastest
method is the one that assumes the most about the function, and the assumptions
are exactly what a real problem does not guarantee.

The geophysical content is immediate. A travel-time curve is a relation between
hypocentre coordinates and arrival times; locating an earthquake is finding the
root of the residual vector "predicted minus observed". A mineral's volume at a
given pressure is the root of an equation of state. A liquidus temperature is the
root of an equilibrium relation. Each of these is a root-finding problem, and
each arrives with a different amount of usable information.

## 2. Precise definitions

### 2.1 Order of convergence

Let $x_k$ be a sequence converging to $x^\*$, and let $e_k = x_k - x^\*$. The
sequence has **order of convergence** $p$ and asymptotic constant $C$ if

$$|e_{k+1}| \le C\,|e_k|^{p}, \qquad C>0 ,$$

eventually, with $p=1$ called **linear** (and requiring $C<1$), $1<p<2$
**superlinear**, $p=2$ **quadratic**, and $p=3$ **cubic**.

From a computed error sequence the order can be estimated as

$$p \approx \frac{\log(e_{k+1}/e_k)}{\log(e_k/e_{k-1})},$$

which is the estimator used everywhere in this lesson. It needs three errors,
so it is useless for a method that converges in two steps — a point taken up in
[01-12-08](./08-matrix-eigen-solvers.md).

### 2.2 Why order matters more than the constant

Doubling the number of correct digits per iteration is not a small improvement.
If a linear method reduces the error by 10 per step and a quadratic method
converges, both eventually succeed; but the linear method needs one step per
digit, so twelve digits take twelve steps, while a quadratic method takes four.
With a cubic method it takes three. For an inversion whose forward solve costs a
CPU-hour, that is the difference between a working algorithm and an impossible
one.

### 2.3 A bracket is a promise

A **bracket** is an interval $[a,b]$ on which $f$ is continuous and
$f(a)f(b)<0$. The intermediate value theorem then guarantees at least one root
inside, and no amount of bad luck can make the search leave it. That guarantee is
the single reason bracketing methods survive: they are the only algorithms here
whose convergence does not depend on the function being well behaved.

## 3. Derivations

### 3.1 Bisection: exactly one binary digit per step

With the bracket $[a_k,b_k]$ and $m_k = \tfrac12(a_k+b_k)$, the new bracket is one
half of the old one:

$$b_{k+1}-a_{k+1} = \tfrac12\,(b_k-a_k).$$

Hence the interval width after $k$ steps is $(b_0-a_0)/2^k$, and the error bound
is

$$|x_k - x^\*| \le \frac{b_0-a_0}{2^{k+1}} .$$

Bisection is order 1 with constant $\tfrac12$: **one bit per evaluation, always**.
To go from an initial interval of width 1 to machine precision $u \approx
2.2\times10^{-16}$ requires $k \approx \log_2(1/u) \approx 52$ halvings. The
demonstration below measures 50 iterations to reach $7\times10^{-16}$ on
$\cos x - x$, and the interval-width ratio is exactly 0.500 at every step.

The order cannot be improved without more information: bisection uses only the
*sign* of $f$, which carries one bit. That observation is the key to everything
that follows.

### 3.2 Newton's method: quadratic, from one Taylor term

Expand $f$ about the current iterate and keep the linear term:

$$f(x^\*) \approx f(x_k) + f'(x_k)(x^\*-x_k) = 0
\quad\Longrightarrow\quad
x^\* \approx x_k - \frac{f(x_k)}{f'(x_k)} .$$

That is the Newton step. To get the order, expand $f(x^\*)$ to second order,
$0 = f(x_k) + f'(x_k)e_k + \tfrac12 f''(\xi)e_k^2$, and substitute:

$$e_{k+1} = x_{k+1}-x^\* = e_k - \frac{f(x_k)}{f'(x_k)}
= \frac{f''(\xi)}{2f'(x_k)}\,e_k^2 .$$

So $p=2$ with $C = |f''/(2f')|$, provided $f'(x^\*) \neq 0$ — that is, provided
the root is **simple**. The demonstration measures orders 3.02 (a transient),
1.91 and 2.00 on $\cos x - x$; the transient is expected, because the asymptotic
constant only governs behaviour once $e_k$ is small.

The requirement $f'(x^\*)\ne0$ is not a technicality. At a **multiple** root,
$f(x) = (x-x^\*)^m g(x)$ with $m>1$, the same expansion gives

$$e_{k+1} = \frac{m-1}{m}\,e_k + O(e_k^2),$$

so Newton degrades to linear with constant $(m-1)/m$ — a loss of the entire
advantage. The fix is to iterate on $f/f'$ instead of $f$, which restores
quadratic convergence at the cost of a second derivative.

### 3.3 The secant method and the golden ratio

Replacing $f'(x_k)$ by the chord slope over the last two points,

$$f'(x_k) \approx \frac{f(x_k)-f(x_{k-1})}{x_k-x_{k-1}},$$

gives the secant iteration. Its error analysis proceeds by writing the chord
slope as $f'(x_k) (1 + O(e_k))$ and using that approximation in the Newton
expansion; the result is a recursion

$$e_{k+1} = C\,e_k e_{k-1},$$

whose solutions behave as $e_k \propto C'^{\,p^k}$ with $p$ satisfying
$p^2 = p+1$, so

$$p = \frac{1+\sqrt{5}}{2} = 1.618034\ldots$$

The secant method is superlinear with the golden-ratio order, and it needs one
function evaluation per step against Newton's two (function plus derivative).
When the derivative is expensive — a numerical derivative costs a function
evaluation, and an analytic one may not exist — secant is often the fastest
method per unit cost. The demonstration measures orders 1.88, 1.48, 1.68 and 1.60
scattering about 1.62, which is what a single-step estimator does on a short
sequence.

### 3.4 Robustness: a safeguarded Newton

The hybrid used in the demonstration keeps a bracket and accepts a Newton step
only if it lands strictly inside it:

```text
given bracket [a, b] and a start x
repeat:
    try xn = x - f(x)/f'(x)
    if xn is outside (a, b) or f'(x) = 0:  xn = (a+b)/2     # bisection
    update the bracket with the sign of f(x)
    x = xn
```

The result has the guaranteed progress of bisection and the local speed of
Newton: on $x^3-2x+2$ started at $x_0=0$ — the exact point from which pure
Newton cycles forever — the hybrid takes one bisection step and then five Newton
steps, and the step record printed by the demonstration is `BNNNNN`. On the
equation of state, started at a physically absurd volume, the record is
`BNNNNNNNB`. Production codes (Brent's method, and the root finders in every
scientific library) are refinements of exactly this idea: inverse quadratic
interpolation inside a bracket, with bisection as the fallback.

## 4. Physical interpretation and the geophysical problems

### 4.1 Hypocentre location is root finding in three unknowns

Let station $i$ sit at $(x_i,y_i)$, let the hypocentre be $(\hat x,\hat y)$ with
origin time $t_0$, and let the medium have speed $v$. The predicted arrival is

$$T_i^{\text{pred}} = t_0 + \frac{1}{v}\sqrt{(\hat x-x_i)^2 + (\hat y-y_i)^2},$$

and the residuals $r_i = T_i^{\text{pred}} - T_i^{\text{obs}}$ vanish at the
correct hypocentre. Stacking the residuals into a vector $\mathbf r \in
\mathbb{R}^4$ and the unknowns into $\mathbf m = (x,y,t_0)$ gives a
**root-finding problem in three unknowns with four equations** — over-determined,
solved by minimising $\tfrac12\|\mathbf r\|^2$, whose stationarity condition is

$$\mathbf J^\mathsf{T}\mathbf J\,\Delta\mathbf m = -\mathbf J^\mathsf{T}\mathbf r,
\qquad \mathbf J = \frac{\partial r_i}{\partial m_j}.$$

For the constant-velocity case the Jacobian entries are elementary:

$$\frac{\partial r_i}{\partial x} = \frac{x-x_i}{v\,d_i}, \qquad
\frac{\partial r_i}{\partial y} = \frac{y-y_i}{v\,d_i}, \qquad
\frac{\partial r_i}{\partial t_0} = 1, \qquad d_i = \sqrt{(x-x_i)^2+(y-y_i)^2}.$$

The demonstration solves this system by Newton's method with a Gaussian
elimination on the $3\times3$ normal equations, from a deliberately poor start.
The measured location error falls $6.9\times10^{-1} \to 6.4\times10^{-3} \to
5.0\times10^{-7} \to 2.5\times10^{-15}$ km, which is the signature of
superlinear convergence.

Two things about this example generalise. First, the residual is a *smooth*
function of the unknowns, which is what makes Newton work at all; a residual
built from picked arrivals has kinks wherever a phase is misidentified, and the
method then fails to converge. Second, the Jacobian is singular at any station
($d_i = 0$ gives division by zero), so a first guess placed exactly on a station
is not merely bad, it is undefined. Real location codes multiply this structure
by a layered or three-dimensional velocity model, and the resulting problem is
the same one: a nonlinear root find wrapped around a linear solve, which is the
subject of [14 Optimization](../14-optimization/README.md) and
[18 Inverse Problems](../../18-inverse-problems/README.md).

### 4.2 An equation of state is a root find

The Murnaghan equation of state relates pressure to volume through

$$P(V) = \frac{K_0}{K_0'}\left[\left(\frac{V_0}{V}\right)^{K_0'}-1\right],$$

with $K_0$ the bulk modulus and $K_0'$ its pressure derivative. Given a target
pressure, the volume is the root of $P(V)-P_{\text{target}}=0$, and the equation
is exactly invertible:

$$V = V_0\left(1+\frac{K_0' P}{K_0}\right)^{-1/K_0'}.$$

That makes it the ideal test case: the answer is known, so the iteration can be
scored. With $K_0 = 130$ GPa, $K_0' = 4$ and $P = 20$ GPa — illustrative values,
not a mineral — the volume is $0.887015$ of $V_0$, a change of 11.2985%. Bisection
needs 53 iterations; Newton needs 5 and reports order 2.005 and 2.000.

### 4.3 Physical interpretation of the failure modes

Each Newton failure has a physical reading, and that reading is the reason to
take it seriously:

- **A vanishing derivative** is a flat region of the response: a gravity anomaly
  that does not change when the body's depth changes. Nothing is learned about
  the parameter, and the iteration says so by dividing by zero.
- **An overshoot out of range** is an unphysical model: a negative volume, a
  negative density, a negative depth. The line tangent to the curve at a bad
  point extrapolates far outside the region where the physics is defined. Newton
  from $V=2.0$ in the Murnaghan case takes a step of $-12.42$ and lands at
  $-10.42$.
- **A cycle** is the worst case because it looks like convergence in a table of
  residuals that has not yet stalled: the residual returns to the same value
  forever.

## 5. Assumptions and regime of validity

| Method | Requires | Order | Fails when |
|---|---|---|---|
| Bisection | continuity and a sign change on $[a,b]$ | 1, rate $\tfrac12$ | $f$ is discontinuous across the root, or no sign change exists (a double root) |
| Newton | $f'$ exists and is computed, $f'(x^\*)\neq0$, a good start | 2 | multiple root, vanishing derivative, overshoot, cycle |
| Secant | two starting points, $f$ smooth near the root | 1.618 | the chord slope is near zero; round-off in the difference |
| Hybrid (bracketed Newton) | a bracket plus $f'$ | safe, locally 2 | a non-smooth or non-continuous $f$ |

Three conditions deserve to be stated explicitly.

1. **Simple root.** Everything except bisection relies on $f'(x^\*)\neq0$. A
   double root is the standard failure case in geophysics: a misfit function
   minimised along a valley rather than at a point.
2. **Smoothness of the residual.** Newton's derivation integrates a second-order
   Taylor term, which requires $f\in C^2$ in a neighbourhood of the root. Picked
   arrivals, tabulated measurements and interpolated look-up tables are not $C^2$;
   the derivative estimated from a table is only as smooth as the table.
3. **A local basin of attraction.** Newton's quadratic convergence is a *local*
   statement. Nothing in the analysis says the first step lands anywhere useful.
   This is why production codes bracket first and iterate second.

Scale involution deserves a fourth note, because it is a practical trap rather
than a mathematical one: the residual of an equation of state is measured in
pascals, and the residual of a travel-time problem in seconds. A convergence test
written as `abs(f(x)) < 1e-8` therefore means something completely different in
the two cases. The demonstration's `newton` routine tests the *relative step
size* instead, $\lvert x_{k+1}-x_k\rvert \le \text{tol}\,(1+\lvert x_{k+1}\rvert)$,
which is scale-free.

## 6. Python demonstration

The script `code/root_finding.py` implements bisection, Newton, secant and a
safeguarded hybrid from scratch and measures every order it quotes. A section of
its output:

```text
Bisection on [0, 1]: interval width halves exactly at every step
  iterations = 50,  final error = 6.661e-16
  width ratio (should be 0.5): 0.500 0.500 0.500 0.500 0.500 0.500 0.500

Newton from x0 = 0.0:
  iterations = 5,  final error = 0.000e+00
    k= 1  x=1.0000000000000000  |x-root|=2.609e-01
    k= 2  x=0.7503638678402439  |x-root|=1.128e-02
    k= 3  x=0.7391128909113617  |x-root|=2.776e-05
    k= 4  x=0.7390851333852840  |x-root|=1.701e-10
    k= 5  x=0.7390851332151607  |x-root|=0.000e+00
  observed order p from consecutive error triples:
    k= 1  p=3.017
    k= 2  p=1.912
    k= 3  p=1.998

Secant from x0 = 0.0, x1 = 1.0 (no derivative used):
  iterations = 7,  final error = 0.000e+00
  observed order p:
    k= 2  p=1.882      k= 3  p=1.484
    k= 4  p=1.680      k= 5  p=1.595
```

Newton's cycle, and its repair:

```text
  x -> x - f/f':  0 -> 1 -> 0 -> 1 -> ...  forever
  A bracketing safeguard (hybrid) started at the SAME x0 = 0.0,
  with the bracket [-3, 0], finds it:
    hybrid root = -1.7692923542386314,  error = 0.000e+00,  steps = 6
  step kinds (N=Newton, B=bisection): BNNNNN
```

The equation of state and the hypocentre location:

```text
  analytic volume      = 0.887015102729059
  bisection: V = 0.8870151027290589,  error = 1.110e-16,  iterations = 53
  Newton:    V = 0.8870151027290589,  error = 1.110e-16,  iterations = 5
    observed order at k=1: p=2.005
    observed order at k=2: p=2.000
  relative volume change = 11.298490% at 20.0 GPa

  start guess = [1.0, 1.0, 1.0]
   it      x (km)      y (km)      t0 (s)   |error| (km)   ||r|| (s)
    0    6.313045    8.951026    0.145528      6.887e-01   3.557e-01
    1    7.006343    8.999244    0.001693      6.388e-03   3.484e-03
    2    7.000000    9.000000    0.000000      4.966e-07   2.878e-07
    3    7.000000    9.000000    0.000000      2.512e-15   1.998e-15
  located hypocentre = (7.000000, 9.000000) km
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| Bisection width ratio is exactly 0.500 | order 1 means one *binary* digit per step — 52 steps for double precision |
| Newton order 3.02 then 1.91, 2.00 | the order estimator is only valid asymptotically; a single triple is noisy |
| Secant orders scatter about 1.6 | superlinear is real but needs several steps to see |
| Hybrid takes one `B` step then five `N` | robustness costs one evaluation and saves the solve |
| EOS: 53 bisections vs 5 Newtons | the derivative is worth about ten bisection steps here |
| Hypocentre error $6.9\times10^{-1}\to5.0\times10^{-7}$ | a smooth residual makes the multi-dimensional Newton superlinearly convergent |

> **Breaking exercise.** Change `report_orders` to start Newton at $x_0 = 0.5$
> and predict, before running, whether the order sequence will look cleaner or
> noisier. Then change the secant start to $(0.9, 1.0)$ and see whether the
> measured order moves closer to the asymptotic value.

## 7. Common mistakes

1. **Using a residual tolerance with the wrong units.** `abs(f(x)) < 1e-8` is a
   different request in pascals, seconds and kilometres. Prefer a test on the
   relative step, or scale the tolerance by a characteristic magnitude of $f$.
2. **Starting Newton inside a flat region.** If $f'$ is tiny, the first step is
   enormous. Check $\lvert f'(x_k)\rvert$ against a scale, and fall back to
   bisection when it is small.
3. **Assuming quadratic convergence at a multiple root.** A double root gives
   linear convergence and a residual that falls by exactly half per step, which
   looks like progress but is not.
4. **Reading a stalled residual as convergence.** In a cycle the residual is
   constant, not small. Always test the *step*, and if the step fails to shrink,
   stop and report.
5. **Differentiating a tabulated function by finite differences and calling it a
   derivative.** The resulting Newton iteration has a noise floor set by the
   difference step (see [01-12-03](./03-numerical-differentiation.md)), and near
   the root the computed derivative can have the wrong sign.
6. **Forgetting that the Jacobian may be singular at a station.** In hypocentre
   location the derivative with respect to position is undefined when the trial
   source sits on a station. Guard against it rather than hoping.
7. **Converging to the wrong root because the start was in the wrong basin.**
   Newton finds *a* root. Bracketing, or a physics-based initial guess, is what
   selects the right one.

## 8. Real-world applications

- **Earthquake location.** Every seismic network solves the residual system of
  §4.1 with a layered or 3-D velocity model, and the arrival times come from
  catalogues such as the [USGS FDSN event service](https://earthquake.usgs.gov/fdsnws/event/1/).
  The iterative structure — nonlinear root find around a linear solve — is
  identical to the constant-velocity example, and so are the failure modes.
- **Mineral physics and geobarometry.** Equations of state, fugacity relations
  and liquidus curves are inverted for pressure, temperature or composition
  hundreds of thousands of times in a single thermobarometry study. The
  difference between a 5-step and a 50-step inversion is the difference between
  a table computed in a minute and one computed overnight.
- **Well-log and petrophysical interpretation.** Shaly-sand models, fluid
  substitution and saturation equations are implicit in the unknowns; the
  standard solver is a bracketed Newton, precisely because the physical range of
  each variable is known and a runaway step must be refused.
- **Inverse theory.** Every nonlinear inversion is a root find on the gradient of
  a misfit, and the Gauss–Newton iteration is Newton's method with $f'$ replaced
  by the Jacobian. The convergence orders derived here are the convergence orders
  of inversion. See [18 Inverse Problems](../../18-inverse-problems/README.md).
- **Model calibration in hydrogeology and geothermics.** Matching a modelled
  drawdown or temperature profile to observations is a root find in a few
  parameters, and the sign-change structure of the residual is what makes a
  bracketing method admissible at all.

## 9. Further reading

- **Burden, R. L., & Faires, J. D. (2010). *Numerical Analysis* (9th ed.).
  Brooks/Cole.** Level: undergraduate. Chapters 2–3 are the standard treatment
  of bisection, Newton, secant and Brent's method, with the error proofs given
  in the same form derived above.
- **Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (2007).
  *Numerical Recipes: The Art of Scientific Computing* (3rd ed.). Cambridge
  University Press.** Level: advanced undergraduate to graduate. The most
  practical discussion available of *why* Brent's method is built the way it is,
  and of the round-off limits of the secant method.
- **Ortega, J. M., & Rheinboldt, W. C. (1970). *Iterative Solution of Nonlinear
  Equations in Several Variables*. Academic Press.** Level: graduate. The
  classical reference for the multi-dimensional theory used in §4.1, including
  the Kantorovich conditions for convergence from an initial guess.
- **Dennis, J. E., & Schnabel, R. B. (1996). *Numerical Methods for
  Unconstrained Optimization and Nonlinear Equations*. SIAM.** Level: graduate.
  Where the root-finding and the optimisation views of the same problem are
  finally reconciled.
- **Trefethen, L. N., & Bau, D. (1997). *Numerical Linear Algebra*. SIAM.**
  Level: graduate. Not about roots, but the source of the conditioning language
  used throughout this module.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library before citing.

## 10. Exercises

Attempt them closed-book. Full statements and difficulty grading are in
[`exercises/01-root-finding-exercises.md`](./exercises/01-root-finding-exercises.md),
with worked solutions in
[`exercises/01-root-finding-solutions.md`](./exercises/01-root-finding-solutions.md).

**★1.** How many bisection steps reduce an initial bracket of width 2 to a width
below $10^{-6}$? Below $u = 2.2\times10^{-16}$?

**★2.** Derive the Newton iteration for $f(x)=x^2-c$ and show that it is the
Babylonian square-root algorithm. Give the error recursion and the order.

**★3.** Apply one Newton step to $f(x)=x^3-2x+2$ from $x_0=0$ and from $x_1=1$,
and show that the orbit is a 2-cycle.

**★4.** A rock's density is given by $P(V)$ of §4.2 with $K_0=130$ GPa,
$K_0'=4$ and $V_0=1$. Estimate (by two bisection steps, with a bracket) the
volume at $P=5$ GPa, then compare with the closed form.

**★★5.** Show that Newton's method at a root of multiplicity $m$ has the linear
constant $(m-1)/m$, and compute the constant for $m=2,3,4$. At what rate does
the residual fall in each case?

**★★6.** Derive the secant order equation $p^2=p+1$ from the recursion
$e_{k+1}=Ce_ke_{k-1}$, stating clearly where the assumption $e_k\ll1$ is used.

**★★7.** A four-station array with $v = 5.8$ km/s records arrivals of 1.85,
2.61, 2.81 and 2.15 s from stations at the corners of a 20 km square. Set up the
residual vector and its Jacobian at the trial hypocentre $(5,5,0.0)$ and take one
Newton step by hand (normal equations, 3×3). State what the step does.

**★★8.** The equation of state is replaced by one with a numerical factor
$K_0' = 4.0$ but a *tabulated* $P(V)$ available only at 25 volumes. Describe how
you would bracket the root and what order you would expect from the secant
method applied to the table. What breaks first?

**★★★9.** Design and run an experiment that measures the order of convergence of
the safeguarded hybrid on a function where Newton and bisection *alternate* for
many steps. Report the measured order, explain why it lies between 1 and 2, and
state how the answer depends on the function.

**★★★10.** A colleague reports a hypocentre located 40 km from every station of
a regional network, with a residual that "converged". Using only the structure of
§4.1, list the three most likely explanations and the diagnostic that would
distinguish them with data you already have.

## 11. Self-assessment checklist

- [ ] I can define the order of convergence and estimate it from an error
      sequence, and I know that a three-term estimate is noisy.
- [ ] I can derive the bisection rate and the Newton order without notes.
- [ ] I can state the golden-ratio order of the secant method and why it arises.
- [ ] I can describe a Newton cycle, a vanishing derivative and an overshoot from
      memory, and say what a bracketed hybrid does about each.
- [ ] I can write the residual vector and Jacobian for a constant-velocity
      hypocentre problem and say where the Jacobian is singular.
- [ ] I can explain why a tolerance on $\lvert f\rvert$ is not scale-free and
      what to use instead.
- [ ] I can explain why a multiple root destroys quadratic convergence and how
      to restore it.

## Related lessons

- [01-12-02 Interpolation, Splines and Approximation Theory](./02-interpolation.md)
  — the other way of representing a function you cannot write down, and the
  source of the tabulated derivatives this lesson warns about.
- [01-12-03 Numerical Differentiation and Finite-Difference Stencils](./03-numerical-differentiation.md)
  — what happens when the derivative in Newton's method has to be approximated,
  including the round-off floor.
- [01-12-05 Direct vs Iterative Linear Solvers and Convergence](./05-linear-solvers.md)
  — the linear solve at the centre of the multi-dimensional iteration.
- [01-05-04 Taylor Series](../05-single-variable-calculus/04-taylor-series.md) —
  the prerequisite tool used in every derivation here.
- [14 Optimization](../14-optimization/README.md) — the same iteration applied to
  a misfit function instead of a residual.
- [18 Inverse Problems](../../18-inverse-problems/README.md) — hypocentre
  location generalised into full inverse theory, with a velocity model as the
  unknowns.
