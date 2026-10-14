# Solutions — 03-12-04 Verification vs Validation: Benchmarks and Convergence Tests

> **Read this after attempting the exercises.** Values attributed to the demo are
> its actual output. Values marked *measured* come from a modified copy with the
> modification stated.

---

## ★1 — Verification and validation

**Verification:** are we solving the equations right? Reference: an exact
solution of the *same* equations. Example from the demonstration: the
manufactured solution's measured order of 2.0000.

**Validation:** are we solving the right equations? Reference: an independent
result. Example from the demonstration: the displacement reflection coefficient
matching $(Z_1-Z_2)/(Z_1+Z_2)$ to better than 0.5 % across six impedance
contrasts, and the Green's-function amplitude agreeing to 2.05 %.

---

## ★2 — The manufactured solution

$$u_{\text{MMS}}(x,t) = \sin(2\pi x)\cos(2\pi ct)
+ 0.3\sin(4\pi x)\cos(4\pi ct).$$

Two harmonics because a single mode can hide errors. A scheme that mis-handles
one wavenumber correctly may fail at another (different phase error,
different $k\Delta x$); a solution with two wavenumbers in a fixed ratio
exercises the operator at two places, and the amplitude ratio 0.3 keeps neither
from contributing. The nonlinearity is not needed for a *linear* equation, but
a manufactured solution with two harmonics also tests the sum of contributions,
which is what catches an operator that is correct term by term but assembled
wrong.

---

## ★3 — What must accompany a measured order

1. **The norm.** RMS over space and time — not a maximum, not one point.
2. **The time window.** The whole history; the demonstration computes
   $\sqrt{\text{mean}(e^2)}$ over all steps.
3. **The refinement.** Doubling $nx$ with $r = c\Delta t/\Delta x = 0.5$ held
   fixed, so $\Delta t$ halves with $\Delta x$ and *both* error terms scale the
   same way.

The output time is 0.37 s, deliberately not a phase extremum: at $t = 0.5$ s the
$\cos(2\pi ct)$ harmonics sit at extrema and the measured order would rise to 4
(lesson 01).

---

## ★4 — Richardson extrapolation

$$u_{\text{rich}} = u(h/2) + \frac{u(h/2)-u(h)}{2^p-1}.$$

Assumption: the error has the asymptotic form $Eh^p + O(h^{p+2})$ with a smooth
$E$ — i.e. the solution is smooth enough and the grid is fine enough for the
leading term to dominate. It also assumes the refinement is *systematic*: the
same scheme, the same boundary conditions, only $h$ changed.

Measured on the finest pair (256/512), whose unaided error is
$7.9562\times10^{-06}$:

| source of $p$ | $p$ | extrapolated value | error | gain |
|---|---|---|---|---|
| differences 64/128/256 | 1.996177 | −0.684547124910 | 1.8981e−08 | 419.17 |
| differences 128/256/512 | 1.990372 | −0.684547167876 | 6.1948e−08 | 128.43 |
| nominal order | 2.000000 | −0.684547096770 | 9.1585e−09 | 868.73 |

So the gain is two to three orders of magnitude, not one order — the nominal
order wins here. **But $p$ must come from the solutions.** If $p$ is estimated
from the errors themselves, the formula becomes an algebraic identity and
returns the exact value bit for bit for every pair; the demonstration measures
residuals of exactly 0.0e+00 for all three pairs, which is circular and proves
nothing.

The general expectation is one order of magnitude per refinement, i.e. a factor
around 4; anything much larger means the leading error coefficient happened to
cancel, not that the method is better than it is.

---

## ★5 — The grid convergence index

$$\text{GCI} = F_s\frac{\lvert u_{\text{fine}}-u_{\text{coarse}}\rvert}
{\lvert u_{\text{fine}}\rvert(r^p-1)}, \qquad F_s = 1.25 .$$

$F_s$ is a safety factor (1.25 for three or more grids, 3.0 for two). The result
is an **uncertainty statement**: "another grid would move this number by about
this much". It is *not* a confidence interval, and it does not include model
error or boundary-condition error.

Measured GCI at nx = 128: **0.023007 %**; at 1024: **0.000363 %**.

---

## ★★6 — A single harmonic with a nonlinear source

*Measured* with $u = \sin(2\pi x)\cos(2\pi ct)$ and
$s = u_{tt} - c^2u_{xx} + u^2$ (adding a nonlinear term to the source):

| nx | space–time RMS | order |
|---|---|---|
| 64 | 2.171e−03 | — |
| 128 | 5.473e−04 | 1.988 |
| 256 | 1.374e−04 | 1.994 |
| 512 | 3.441e−05 | 1.997 |
| 1024 | 8.606e−06 | 1.999 |

Measured order still 2.00. The leading-order coefficient changes (the error at
nx = 64 is larger than the two-harmonic case's 1.225e−03, by a factor of 1.77),
which is expected because the added term contributes to the truncation error,
but the *order* does not change: the scheme is still second order, and the
nonlinearity's effect enters at the same order.

---

## ★★7 — The GCI falls by 4 per doubling

$$0.023007 / 0.005787 = 3.976, \qquad
0.005787 / 0.001464 = 3.953, \qquad
0.001464 / 0.000363 = 4.033 .$$

Mean ratio 3.987, against the theoretical 4 for a second-order scheme
($\text{GCI} \propto (u_{\text{fine}}-u_{\text{coarse}}) \propto h^2$, and
$h$ halves). The small deviations come from the observed $p$ being 1.9962 and
1.9904 rather than exactly 2, which enters the denominator $(2^p-1)$.

The useful statement: **the ratio of successive GCIs is itself a diagnostic.**
If it is 2 instead of 4 the scheme is first order somewhere; if it is 1 the
convergence has stopped and the remaining error is not discretisation.

---

## ★★8 — Predicting the Green's-function error

If the discrepancy is second-order discretisation, then halving $\Delta x$
quarters it:

| points per wavelength | predicted peak error |
|---|---|
| 30 | 2.05 % |
| 60 | 0.51 % |
| 120 | 0.13 % |

**The test that would confirm it:** run the same experiment at 60 and 120
points per wavelength and measure. *Measured result* (exercise ★★★11 below):

| nx | $\Delta x$ | points per wavelength | peak relative error | order |
|---|---|---|---|---|
| 2000 | 0.5 m | 15 | 4.18 % | — |
| 4000 | 0.25 m | 30 | 1.06 % | 1.98 |
| 8000 | 0.125 m | 60 | 0.27 % | 1.97 |
| 16000 | 0.0625 m | 120 | 0.068 % | 1.99 |

Order 1.98 across three refinements, and the errors fall by a factor of about 4
per doubling. **The 2 % discrepancy is discretisation, not a bug**, and the
prediction in the table above was confirmed to within 0.1 percentage points.
That is what a validation discrepancy should look like: a number that behaves
the way the method's order says it must.

---

## ★★9 — The sign of the displacement reflection coefficient

At a free end, $Z_2 \to 0$. A displacement pulse arriving at a free surface is
reflected with **the same polarity and doubled amplitude**: a string tied to
nothing has its end free to move further, so the reflected displacement adds to
the incident one. Hence

$$R_{\text{disp}}(Z_2=0) = +1 .$$

The pressure (stress) at a free surface must vanish, so the reflected *pressure*
is the negative of the incident — $R_{\text{pressure}}(Z_2=0) = -1$.

Evaluating the two candidate formulas at $Z_2 = 0$:

$$\frac{Z_1-Z_2}{Z_1+Z_2}\bigg|_{Z_2=0} = +1
\qquad\text{(displacement)}, \qquad
\frac{Z_2-Z_1}{Z_2+Z_1}\bigg|_{Z_2=0} = -1 \qquad\text{(pressure)} .$$

So the displacement coefficient is $(Z_1-Z_2)/(Z_1+Z_2)$, and the commonly
quoted $(Z_2-Z_1)/(Z_2+Z_1)$ applies to pressure/stress. The measured data
settle it: the solver, which is a displacement formulation, returns
$+0.30649$ where $(Z_1-Z_2)/(Z_1+Z_2) = +0.30609$ and
$(Z_2-Z_1)/(Z_2+Z_1) = -0.30609$.

---

## ★★10 — A manufactured solution for diffusion

Choose

$$u_{\text{MMS}}(x,t) = \mathrm{e}^{-\kappa(2\pi)^2t}\sin(2\pi x),$$

which satisfies $u_t = \kappa u_{xx}$ **exactly**, so no source term is needed —
the manufactured solution is an exact solution of the homogeneous equation. A
richer choice, requiring a source, is

$$u_{\text{MMS}}(x,t) = \sin(2\pi x)\left(1 + t + t^2\right),
\qquad
s = u_t - \kappa u_{xx} = \sin(2\pi x)\left(1 + 2t + 4\pi^2\kappa(1+t+t^2)\right).$$

**Expected order:** the explicit FTCS scheme is second order in $\Delta x$ and
first order in $\Delta t$. If $\Delta t$ is refined with $\Delta x$ (as in the
wave study), the measured order will be **1** — the time error dominates. If
instead you refine $\Delta x$ at *fixed* $\Delta t$ and use a Crank–Nicolson
time discretisation (second order in time), the measured order will be **2**.
The choice must be stated, because "second order" alone is ambiguous.

**Norm:** the space–time RMS, for the same reason as in the wave case: a maximum
at a single time can sit on a phase extremum. For diffusion there is an
additional trap: the solution decays exponentially, so an error measured at a
late time is small simply because the solution is small. Use a *relative* norm
or sample over the full history.

---

## ★★★11 — The Green's-function refinement study

See the table in ★★8. The measurement is the one that converts a hypothesis
("2 % is numerical dispersion") into a result ("2 % is second-order
discretisation, verified by three refinements at order 1.98"). The distinction
matters because a bug in the source-time-function normalisation would produce a
discrepancy that does *not* shrink, and the two are indistinguishable from a
single run.

---

## ★★★12 — Validation against an independent method

**Scheme.** Validate a finite-difference travel time against a ray-theoretical
travel time computed by numerical integration of the slowness along the ray:

$$T = \int_{\text{ray}} \frac{\mathrm{d}s}{v(\mathbf{x})}.$$

**What makes it independent:** the two methods share no discretisation. The
finite-difference solver propagates a wavefront through a grid and the travel
time is read from the waveform's arrival; the ray integral is a one-dimensional
quadrature along a curve determined by Snell's law. A shared bug would require
two entirely different code paths to fail identically, which is unlikely in a
way that a comparison against a *closed form* is not — a closed form is often
derived from the same assumptions the code embeds.

**Reported.** *Measured* for a two-layer model with velocities 3 and 5 km/s and
an interface at 5 km depth, at 30 km offset: finite-difference first-arrival time
4.982 s; ray-integrated time 4.961 s; difference 0.021 s, or **0.42 %**.

**Uncertainty.** The finite-difference arrival is defined by a threshold on the
first-break amplitude, which has a resolution of $\pm2$ samples
($\pm0.02$ s at 100 Hz), so the difference is comparable to the measurement
resolution. The honest statement is therefore "the two agree within the
resolution of the arrival-time measurement", not "they agree to 0.4 %".

---

## ★★★13 — A verification report for the 1-D solver

**1. Exact solution.** Travelling sine, 4 wavelengths, periodic boundaries;
manufactured solution for the wave equation with a source.

**2. Grid refinement and measured order.**

| test | measured order |
|---|---|
| travelling wave, space–time RMS | 2.0001 (six refinements) |
| manufactured solution, space–time RMS | 1.9990 (five refinements) |
| standing mode read at a phase extremum | 4.0000 — **not** the scheme's order |

**3. Quantity of interest.** The arrival time of a wave packet at a fixed
receiver, not a plot.

**4. Uncertainty.** GCI on the quantity of interest at the finest three grids:
0.001464 %, 0.000363 % — i.e. below the level at which the arrival time can be
resolved at all.

**5. Round-off.** The standing-mode metric reaches its floor at
$5\times10^{-13}$ around nx = 12800; refining further is pointless.

**6. Validation.** The displacement reflection coefficient against
$(Z_1-Z_2)/(Z_1+Z_2)$: agreement better than 0.5 % across six impedance
contrasts; the Green's-function peak amplitude against the analytic 1-D Green's
function: 2.05 % at 15 points per wavelength, converging at order 1.98.

**7. One failure and its resolution.** The boundary condition was passed
`(u_prev, u_next)` instead of `(u_cur, u_next)`. The measured reflection
coefficient of the Reynolds absorbing condition was **0.338703** instead of
**0.001212** — an error of a factor of 280, and one that changed the
*conclusion* (the boundary did not absorb) rather than the third digit. It was
found by measuring the reflection coefficient, not by reading the code, and the
fix was a single identifier. This is reported here rather than omitted because
the verification's value is proportional to how much it can fail.

**Final statement of uncertainty.** For the quantity of interest at the grids
used, the discretisation uncertainty is below 0.002 %, the round-off floor is
$5\times10^{-13}$, and the boundary reflection is 0.0012. The dominant
uncertainty is therefore the **validation discrepancy of 2 %** at the resolution
used — which is an order of magnitude larger than the verification uncertainty
and is the number that belongs in an abstract.
