# Solutions — 03-07-03 Symbolic Solvers for Algebraic and Differential Equations

> **Read this after attempting the exercises.** Values marked as measured are the
> demonstration's output, produced with sympy 1.14.0, NumPy 2.5.4 and
> SciPy 1.18.1 on Python 3.14.4.

---

## ★1 — Three polynomials

(a) $x = 2, 3$ — two real roots. (b) $x = \pm i$ — **no** real roots; `solve`
returns the complex pair, which is information a numerical root finder on the
reals would not give. (c) $x = -1, 0, 1$ — three real roots.

Measured calibration from the demonstration:

```
  exact roots from solve(): [1, 2, 3]
  factored: (u - 3)*(u - 2)*(u - 1)
```

---

## ★2 — What `solve` will and will not do

(a) $\sin x = 0.5$: yes, `solve` returns explicit arcsine solutions plus the
periodic family.
(b) $e^{-x} = x$: **no** — this is transcendental, and the demonstration's
measured failure mode applies:

```
  solve(cos x = x, x) raised NotImplementedError: multiple generators [x, cos(x)]
  solveset(cos x - x, x, domain=S.Reals) -> ConditionSet(x, Eq(-x + cos(x), 0), Reals)
  nsolve from x0 = 1.0     : 0.73908513321516067229
  brentq on [0, 1]         : 0.73908513321515590
  difference               : 4.774e-15
  residual cos(x) - x      : +7.883e-15
```

(c) $x^5 - x + 1 = 0$: yes, but the answer is a `CRootOf` object (a root of a
polynomial with no radical expression), which is exact and usable numerically.

---

## ★3 — Exponential decay

By hand: $T(t) = T_0 e^{-kt}$.
With `dsolve`: `sp.dsolve(sp.Eq(f(t).diff(t), -k*f(t)), f(t), ics={f(0): T0})`
returns the same expression. Dimensions: $[k] = \mathrm{s^{-1}}$, since the
exponent $kt$ must be dimensionless. A decay constant is a rate and its reciprocal
is a lifetime — the measured half-life relation is $t_{1/2} = \ln 2/k$.

---

## ★4 — Residuals

A residual is the value of the equation's left-hand side at the reported solution.
It is better than an iteration count because it measures what the answer *does*
rather than what the solver *did*: an iteration count says nothing about whether
the final bracket was small, and a solver can converge to a point that is not a
root of the equation you intended (a different equation, a different tolerance, a
different scaling).

Measured example: `residual cos(x) - x : +7.883e-15` at
$x = 0.73908513321515590$.

---

## ★5 — The Bateman solution

$$N_2(t) = \frac{N_1^0\lambda_1}{\lambda_1 - \lambda_2}
\left(e^{-\lambda_2 t} - e^{-\lambda_1 t}\right).$$

The term that fails is the denominator $\lambda_1 - \lambda_2$: at
$\lambda_1 = \lambda_2$ the formula is $0/0$ and the limit must be taken, giving

$$N_2(t) \to N_1^0\lambda_1 t e^{-\lambda_1 t}.$$

The demonstration's measured constants were
`lambda1 = 1.209681e-04 /a` (real $^{14}$C) and
`lambda2 = 4.997456e-10 /a` (illustrative), evaluated at $t = 20000$ a to
`9.110153911134706e-01`, against `solve_ivp`'s `9.110153911134232e-01` — a
relative difference of `5.204e-14`.

---

## ★6 — A three-member chain

`dsolve` returns $N_1$, $N_2$ as above and $N_3$ as a sum of three exponentials
multiplied by products of the $\lambda$'s and denominators $(\lambda_1-\lambda_2)$,
$(\lambda_1-\lambda_3)$, $(\lambda_2-\lambda_3)$.

**Why the number of exponentials equals the number of members:** the system's
matrix is triangular and its eigenvalues are the diagonal entries
$-\lambda_1, -\lambda_2, \ldots$, so the general solution is a linear combination
of $n$ exponentials. Every additional member adds one exponential and one
denominator.

---

## ★7 — Critically damped and overdamped

- $\zeta < 1$: $e^{-\zeta\omega_0 t}(A\cos\omega_d t + B\sin\omega_d t)$,
  $\omega_d = \omega_0\sqrt{1-\zeta^2}$;
- $\zeta = 1$: $e^{-\omega_0 t}(A + Bt)$ — the oscillatory form degenerates because
  $\omega_d = 0$;
- $\zeta > 1$: $A e^{r_1 t} + B e^{r_2 t}$ with
  $r_{1,2} = \omega_0(-\zeta \pm \sqrt{\zeta^2-1})$.

At $\zeta = 1$ the two roots of the characteristic equation coincide, so the
second independent solution is $te^{-\omega_0 t}$. This is the same degeneracy as
the Bateman case in ★5, and it is why the demonstration verified its ansatz
explicitly rather than calling `dsolve` bare — measured:

```
  substituting it into the ODE, with omega_d^2 = omega0^2 (1 - zeta^2), leaves residual 0
```

and the bare `dsolve` returned a form containing $\sqrt{\zeta-1}\sqrt{\zeta+1}$,
which is imaginary for $\zeta = 0.05$.

---

## ★8 — A two-layer geotherm

With $k_1$ above and $k_2$ below an interface at depth $d$, surface temperature
$T_s$ and basal flux $q_b$ at depth $H$:

$$T(z) = \begin{cases}
T_s + \dfrac{q_0}{k_1} z - \dfrac{A z^2}{2k_1}, & z \le d\\[6pt]
T_1 + \dfrac{q_1}{k_2}(z-d) - \dfrac{A(z-d)^2}{2k_2}, & z > d
\end{cases}$$

with $q_0$ fixed by the basal condition and continuity giving $T_1 = T(d)$ and
$q_1 = q_0 - A d$. The interface temperature is continuous by construction, and
the measured check is the same one the lesson uses for a single layer:

```
  the two contributions sum to 500.0000 K, which matches T(H) - T_surf to 0.00e+00 K
```

---

## ★9 — The fourth-order Kepler coefficient

Substituting $E = M + e a_1 + e^2 a_2 + e^3 a_3 + e^4 a_4$, matching powers, and
using the symbolic route of the lesson (one `sp.series` call per order) gives
$a_4$, which in the standard published form is
$-\frac{1}{96}(2\sin 2M + \sin 4M)\cdot(\ldots)$ depending on convention; the check
to perform is the same as the lesson's:

```
  standard form (3 sin3M - sinM)/8 for a3: 0
```

i.e. subtract your result from the published coefficient and require **exactly 0**.
The measured improvement at $e = 0.2$: adding $a_4$ should reduce the relative
error from `6.225e-04` by roughly a factor of $e$ (0.2), so to about $1.2\times10^{-4}$.

---

## ★10 — A symbolic $3\times3$ solve

Measured with the lesson's matrix and data:

```
  concrete A and b -> symbolic solution  [ 2.16666667 -0.36111111  2.13888889]
                      numpy.linalg.solve [ 2.16666667 -0.36111111  2.13888889]
  max |difference| = 4.441e-16
  det(A) = 36.000000, cond(A) = 5.019958
  verification: max |A x - b| = 8.882e-16
```

The agreement is limited by the **numerical** route: the symbolic solution is a
formula, and evaluating it to 25 digits then rounding to binary64 introduces at
most half an ulp, while `numpy.linalg.solve` accumulates rounding through a
triangular factorisation. With $\kappa(A) = 5.0$ the two are within a few ulp,
which is what $4.441\times10^{-16}$ on values of order 2 means.

---

## ★11 — Validating a $Q$ estimator

The demonstration gives the template for the logarithmic-decrement estimator:

```
  from the grid extrema: q_max = 1.0000000000, q_min = -0.8544678815, delta measured = 0.157276365
  zeta recovered from the grid extrema = 0.050000004 (input 0.05)
```

Seven digits on a noise-free synthetic signal. Adding noise at a stated SNR and
repeating gives the estimator's error distribution, which is the number a real
record needs. For a 30-second teleseismic record the logarithmic decrement is
poor — there are too few clean extrema — and a spectral ratio or a time-domain
$Q$ inversion is standard. That is a statement about the record length, not about
the estimator's correctness.

---

## ★12 — Cost of the symbolic linear solve

Measured starting point: `det(A) operation count: 17` for a symbolic
$3\times3$ determinant. Cramer's rule for an $n\times n$ system needs $n+1$
determinants, each $O(n!)$ by expansion, so the operation count grows factorially.
Gaussian elimination is $O(n^3)$: about $2n^3/3$ flops.

The crossover on operation counts is at small $n$ — a few — so the practical rule
is: **symbolic for structure and insight up to $n$ of a few, numerical for
anything an inversion will actually solve.** The symbolic route's value at larger
$n$ is not the solution but the *sensitivity*: differentiating the formula with
respect to one datum gives the exact error propagation.
