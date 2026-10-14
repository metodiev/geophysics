# Solutions — 03-03-02 scipy.integrate: Quadrature and ODE Integration

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values marked *measured* were obtained by
> running a modified copy of the demo, and the modification is stated.

---

## ★1 — Convergence orders

**(a)** Trapezoid: error $\propto n^{-2}$. Simpson: error $\propto n^{-6}$
*for this integrand*. The trapezoid errors fall by a factor of 100 for a factor
of 9.18 in $n$ ($9.18^2 = 84$); the Simpson errors fall by a factor of $10^6$
for the same change, and $9.18^6 = 5.9\times10^5$, so the observed Simpson order
is 6, not 4.

**(b)** The leading trapezoid term is analytic. Euler–Maclaurin gives
$I - T_n \approx -\frac{h^2}{12}\left[f'(b)-f'(a)\right]$ with $h = 1/n$. Here
$f' = -8x/(1+x^2)^2$, so $f'(0) = 0$ and $f'(1) = -2$, and
$I - T_n \approx \frac{1}{6n^2}$, i.e. $C = 1/6 = 0.16667$. At $n = 201$:
$1/(6\times40401) = 4.125\times10^{-6}$; *measured* $4.1667\times10^{-6}$. At
$n = 401$: $1/(6\times160801) = 1.0364\times10^{-6}$; *measured*
$1.0417\times10^{-6}$. The measured values are 1.0% above the leading term,
which is the size of the next term in the series. The fit from $n = 11$ gives
$C = 0.202$, which shows that $n = 11$ is not yet asymptotic.

**(c)** Simpson's leading error term is
$-\frac{h^4}{180}\left[f'''(b)-f'''(a)\right]$, and for this integrand
$f'''(x) = 96x(1-x^2)(1+x^2)^{-4}$, so $f'''(0) = f'''(1) = 0$ and the leading
term vanishes identically. The error falls as $n^{-6}$ instead. The constant
follows from $n = 11$: $C_6 = 3.965\times10^{-8}\times11^6 = 0.0702$, so the
prediction at $n = 21$ is $0.0702/21^6 = 8.2\times10^{-10}$; *measured*
$6.20\times10^{-10}$. Same order, and the residual difference is the next term.

**(d)** There is no round-off floor at $n = 101$: the error
$3.95\times10^{-14}$ is genuine and follows from the $n^{-6}$ behaviour, since
$n = 101$ is only 9.18 times $n = 11$ and $9.18^6 = 5.9\times10^5$. The reason
the Simpson error is so far below a naive $n^{-4}$ extrapolation is not
convergence to the asymptotic regime but the **cancellation of the $n^{-4}$
term**, which happens because $f'''$ vanishes at both endpoints. The same rule
on $[0,2]$, where $f'''(2) \ne 0$, would show the classical $n^{-4}$ and the
extrapolation from $n = 11$ would work.

---

## ★2 — The slab limit

**(a)** $g_z = 2\pi G\rho t = 2\pi \times 6.6743\times10^{-11} \times 300
\times 1000 = 1.2580759\times10^{-4}\ \mathrm{m\,s^{-2}} = 12.580759$ mGal,
which is the demo's `exact` column to the printed precision.

**(b)** $g_z = 2\pi G\rho t = 2\pi \times 6.6743\times10^{-11} \times 400
\times 500 = 8.3872\times10^{-5}\ \mathrm{m\,s^{-2}} = \mathbf{8.387}$ mGal
(measured 8.387172739).

**(c)** The residual is the field of the two missing tails. The reduced
integrand behaves as $(z_2^2-z_1^2)/(2x^2)$ for large $x$, so the tail integral
converges as $1/W$ and the relative error halves when $W$ doubles:
at 400 km the prediction is $1.11\times10^{-2}/2 = 5.55\times10^{-3}$.

**(d)** The error is the field of the material the model does *not* contain —
the truncated tails beyond $\pm W$. The quadrature itself is exact to round-off
at every $W$, as the round-off-level quadrature errors in the $n$-gon table
confirm.

---

## ★3 — The decay solution

**(a)** `rtol=1e-10` is a *local* per-step tolerance on the scaled error
estimate; the global error accumulates over 95 steps but with strong damping,
so a final maximum relative error of $5.8\times10^{-11}$ — better than the
request — is the expected outcome for a smooth, dissipative problem. A
tolerance is not a guaranteed bound on the global error.

**(b)** $\lambda = \ln 2/(10^9 \times 3.15576\times10^7) =
2.1972\times10^{-17}\ \mathrm{s^{-1}}$. The Julian year of
$3.15576\times10^7$ s is the conversion used throughout this module.

**(c)** $e^{-\ln 2} = 0.5$ **exactly**, and at $t = t_{1/2}$ the solution is
0.5; the value $0.707106781187$ in the table is at $t = t_{1/2}/2$, where
$e^{-\ln 2/2} = 1/\sqrt2 = 0.7071067811865$. The table's last digit differs by
$7\times10^{-13}$, which is the solver's error at that point.

**(d)** The local error per step is controlled to `rtol` by step-size
adaptation, and because the problem is linear with a negative eigenvalue
$-\lambda$, errors decay rather than amplify: the solution is contracting (the
variational equation is $\delta' = -\lambda\delta$). The absolute error shrinks
along with the solution, so the *relative* error stays at the tolerance.

---

## ★4 — The $n$-gon geometry error

**(a)** $p = \ln(2.55\times10^{-2}/6.27\times10^{-6})/\ln(1024/16)
= \ln(4067)/\ln(64) = 8.311/4.159 = 2.00$.

**(b)** Prediction: $6.27\times10^{-6}/16 = 3.92\times10^{-7}$.

**(c)** With $u = 2\pi/n$,
$\frac{n}{2}\sin(2\pi/n)/\pi = \frac{\sin u}{u} = 1 - \frac{u^2}{6} +
\frac{u^4}{120} - \cdots$, so the deficit is
$\frac{u^2}{6} - \frac{u^4}{120} + \cdots = \frac{2\pi^2}{3n^2}
- \frac{2\pi^4}{15n^4} + \cdots$.

**(d)** The external field of a 2-D body at distances large compared with its
size is dominated by the line-mass (monopole) term $\lambda = \rho A$; the
*relative* field error is therefore the relative mass error, i.e. the area
deficit itself. Substituting the expansion into the table:
$2\pi^2/(3\cdot16^2) = 2.570\times10^{-2}$ against a measured
$2.55\times10^{-2}$ (0.8% low, because the $u^4$ term is not yet negligible at
$n = 16$); $2\pi^2/(3\cdot256^2) = 1.004\times10^{-4}$ against
$1.00\times10^{-4}$; $2\pi^2/(3\cdot1024^2) = 6.275\times10^{-6}$ against
$6.27\times10^{-6}$. **The field error equals the area deficit to three
digits**, and the residual difference is the quadrupole correction, which is
of second order in the deficit.
At $n = 4096$ the prediction is $2\pi^2/(3\cdot4096^2) =
3.92\times10^{-7}$.

---

## ★5 — Stiffness and method choice

**(a)** Stiff: `BDF` or `Radau`, because their step is limited by accuracy
rather than by stability, so they need 166 and 306 evaluations where `RK45`
needs 13 190. Non-stiff and smooth: `RK45`, because it needs no Jacobian and
its higher order wins whenever the step is accuracy-limited.

**(b)** $13\,190/166 = 79.5$ — a factor of nearly 80 in favour of `BDF`, for the
same final accuracy (4.30, 7.85 and $7.69\times10^{-9}$ for the three methods).

**(c)** `Radau` is an implicit Runge–Kutta method of order 5 with an embedded
error estimate; its stage structure means more function evaluations per step
(306/41 ≈ 7.5 per step) than BDF's multistep formula (166/81 ≈ 2 per step), so
it takes fewer, more expensive steps. Both are implicit; the trade between
them is between a higher order and a cheaper step.

**(d)** Raising the coefficient from 1000 to 10 000 stiffens the equation:
`RK45`'s stability limit forces a step smaller by a factor of 10, so its `nfev`
grows roughly tenfold (to of order $10^5$) while `BDF`'s and `Radau`'s change
little. The **error stays the same** because the solution is still
$y = \cos t$: stiffness is a property of the *equation's dynamics*, not of the
solution, and no method's accuracy is affected by it — only the cost.

---

## ★6 — Integrand structure and `points=`

**(a)** `quad` samples where its error estimator says the error is largest. The
spike is 10⁻⁴ wide in a unit interval, so on the first 21-point rule it is
essentially measure zero: every sample the rule takes sees the function equal
to 0, the estimate is 0, and the rule comparison agrees that the integral is 0,
so the reported error is 0 as well. `quad` cannot distinguish "the integrand is
zero" from "I have not looked where the integrand is not zero".

**(b)** `points=[0.37]` — the kink makes the *second* derivative singular, so
each subinterval on either side is smooth; splitting there restores the
assumption. Expect convergence to resume at the smooth rate.

**(c)** `points=[0.25, 0.75]`. A jump discontinuity inside an interval breaks
the Gauss–Kronrod assumption entirely, and the two subintervals are each
smooth. Verify by comparing the sum of two `quad` calls on
$[0,0.25]$, $[0.25,0.75]$, $[0.75,1]$ with the single call using `points=`:
they should agree to round-off.

**(d)** The diagnosis is wrong because changing the tolerance cannot help if
the *sampling* cannot see the feature: the boundary is a curve across which the
integrand's derivative (or the density) jumps, and `quad` will keep subdividing
around it without ever placing a node on it. The fix is to hand the geometry to
the integral — split the $x$ range at the boundary crossings, exactly as the
demo's `gz_profile` does at the vertex abscissae, or use `points=` for a
one-dimensional slicing where the boundary crossing is known analytically. A
further consequence: the reported `abserr` may stay small while the answer is
wrong, so the only reliable check is against an independent reference.

---

## ★7 — The sphere, outside and inside

**(a)** $M = \rho \frac{4}{3}\pi R^3 = 2700\times5.2360\times10^{11} =
1.4137\times10^{15}$ kg. Then
$GM/d^2 = 6.6743\times10^{-11}\times1.4137\times10^{15}/10^{8} =
9.4356\times10^{-4}\ \mathrm{m\,s^{-2}} = 94.356$ mGal, matching
`94.355693`.

**(b)** $1.4137\times10^{15}$ kg (measured 1.413716694115407 × 10¹⁵).

**(c)** Newton's shell theorem: outside a spherically symmetric body the field
is exactly that of a point mass at the centre, for *any* radial density
profile. The quadrature is therefore not approximating — it is reproducing a
theorem, and the measured relative difference of $1.15\times10^{-16}$ is
round-off.

**(d)** Inside the sphere the field is $g = GMr/R^3$ (again the shell theorem,
with the outer shells contributing nothing), and the volume integral still
reproduces it — but the integrand is now singular at the observation point
itself, which is *inside* the integration domain. *Measured* with the same
integrand and $d = 3$ km from the centre: quadrature
$226.453893$ mGal against the analytic $GMr/R^3 = 226.453664$ mGal, a relative
difference of $10^{-6}$, with an `IntegrationWarning` and a reported error of
$0.011$ mGal — eleven orders of magnitude worse than the outside case. **The
same code, the same theorem, a different regime, and the routine now tells you
it is struggling.** This is why the outside case is the one worth using as a
verification: the answer is at round-off and the routine is silent for the
right reason.

---

## ★8 — The reduction, and the convexity assumption

**(a)** With $u = (x-x_0)^2 + z^2$, $du = 2z\,dz$, so
$\int z\,dz/u = \tfrac12\ln u$ and the result follows.

**(b)** On an interval where $z_1(x)$ and $z_2(x)$ are each linear (which is
exactly what a polygon gives between two consecutive vertex abscissae), the
integrand is a sum of logs and arctangents of smooth functions and $z_{1,2}$ do
not vanish. At a vertex abscissa one of $z_1'$ or $z_2'$ jumps, so the
integrand has a kink — not a singularity, so `quad` would converge, but only at
the reduced rate of a kinked integrand. Splitting at the vertices restores the
smooth-interior assumption and lets each subinterval converge at the full rate.
The demo's `xs = sorted({p[0] for p in poly})` is exactly this split.

**(c)** `min(zs), max(zs)` fills the *vertical interval between the lowest and
highest crossing* at each $x$. For a convex polygon there are exactly two
crossings and the interval is the body. For a non-convex polygon there can be
four (an "S"-shaped or "C"-shaped body), and the code then adds the empty
region between the two separate lobes. Counterexample: an "L"-shaped body whose
vertical arm has a notch; at an $x$ crossing the notch, the crossings are at
$z = 0.2, 0.4, 0.6, 0.8$ and the correct integral covers $[0.2,0.4]$ and
$[0.6,0.8]$ while `min/max` covers $[0.2,0.8]$ — an overestimate of the
attraction of the missing notch region.

**(d)** Handle the crossings in pairs: sort the intersections and integrate over
$[z_1,z_2], [z_3,z_4], \dots$, which is exact for any simple polygon (it is the
standard "even–odd" rule) and costs one extra logarithm per pair. For a
$k$-lobed body the cost grows linearly in the number of lobes, and the
quadrature must be split at *every* vertex abscissa plus every $x$ at which two
edges cross in the vertical sense (for a self-intersecting outline).

---

## ★9 — A third independent verification

**(a)** The **mass–integral identity**: for a 2-D body of unlimited strike with
mass per unit length $\lambda = \rho A$, the vertical attraction satisfies

$$\int_{-\infty}^{\infty} g_z(x)\,dx = 2\pi G \lambda .$$

This is the 2-D form of Gauss's theorem applied to the potential: the flux of
the field through a closed surface enclosing the body equals $2\pi G$ times the
enclosed mass per unit length. It shares no code with the quadrature, needs no
special shape, and constrains the *integral* of the whole profile with a single
closed-form number.

**(b)** With $\lambda = 300 \times 3.8370\times10^{7} = 1.1511\times10^{10}$
kg m⁻¹, the reference is $2\pi G\lambda = 4.827237\ \mathrm{m^2\,s^{-2}}$.
*Measured*, integrating the demo's profile with Simpson's rule on a
4001-point grid:

| profile half-width | measured $\int g_z\,dx$ | relative difference |
|---|---|---|
| 300 km | 4.792057 | $7.29\times10^{-3}$ |
| 1000 km | 4.816685 | $2.19\times10^{-3}$ |
| 3000 km | 4.823238 | $8.28\times10^{-4}$ |

The difference falls roughly as $1/X$, which is itself a verification: the
truncation error is the field of the excluded tails, and the tail decays as
$x^{-2}$, so its integral decays as $X^{-1}$. (Pushing $X$ to 10 000 km
*without* refining the grid makes the answer worse — $1.5\times10^{-2}$ —
because a 5 km sample spacing no longer resolves the anomaly.)

**(c)** The strongest single verification is the **line-mass check of the
circular cross-section**, because it is an exact closed form evaluated at five
stations with no truncation, no discretisation of a boundary and no modelled
error term, and it agrees to $6\times10^{-16}$ — round-off. The
mass–integral identity is the strongest *global* test (one number constrains
the entire profile, and it is a theorem rather than a limit), but it requires
a truncation whose own error must be modelled, which is exactly the kind of
extra assumption the line-mass check avoids. Use both: the pointwise check
against a closed form for accuracy, the identity for a mistake in the overall
scaling — a factor-of-two error in the density or the strike-length convention
would pass the first test and fail the second.
