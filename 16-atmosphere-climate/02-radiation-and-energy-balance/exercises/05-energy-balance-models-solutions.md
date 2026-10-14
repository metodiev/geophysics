# Solutions — 16-02-05 Zero- and One-Dimensional Energy Balance Models

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [05 Energy Balance Models](../05-energy-balance-models.md).

---

## ★1 — Equilibrium temperature versus albedo

$$F = \frac{S(1-a)}{4}, \qquad T_{\text{eq}} = \left(\frac{F}{\sigma}\right)^{1/4}.$$

| $a$ | $F$ (W m⁻²) | $T_{\text{eq}}$ (K) |
|---|---|---|
| 0.20 | 272.20 | 263.220 |
| 0.40 | 204.15 | 244.954 |

$$\frac{\mathrm{d}T}{\mathrm{d}a} \approx \frac{244.954 - 263.220}{0.20}
= -91.3\ \mathrm{K\ per\ unit\ albedo}.$$

**Statement to include.** That is the *sensitivity of a blackbody to albedo*,
computed for a $0.2$ change; the function is nonlinear, so a derivative evaluated
over such a large interval is an average slope, not a local one. The local value at
$a = 0.30$ is (from the fourth-root structure)
$\mathrm{d}T/\mathrm{d}a = -T_{\text{eq}}/[4(1-a)] = -254.578/(4\times0.70) =
-90.9\ \mathrm{K}$ per unit albedo — consistent to $0.5\%$, which is why the
average slope is a fair approximation over this range.

---

## ★2 — Heat capacity and relaxation time

$$C = \rho c_p h.$$

| $h$ (m) | $C$ (J m⁻² K⁻¹) | $\tau = C/B$ (s) | $\tau$ (yr) |
|---|---|---|---|
| 30 | $1.200\times10^{8}$ | $3.2066\times10^{7}$ | 1.016 |
| 80 | $3.200\times10^{8}$ | $8.5509\times10^{7}$ | 2.710 |
| 100 | $4.000\times10^{8}$ | $1.0689\times10^{8}$ | 3.387 |

**What changes:** only the *time* to reach equilibrium, in direct proportion to
$h$.

**What does not:** the equilibrium temperature, which is set by $\sigma T^4 = F$ and
has no $C$ in it. This is the single most useful fact about the zero-dimensional
model, and the reason a "forcing" is not a "temperature": a deeper mixed layer means
a slower approach to the same destination.

---

## ★3 — Linearisation about $270\ \mathrm{K}$

$$B = 4\sigma T_0^3 = 4\times5.670374419\times10^{-8}\times270^3 = 4.4644\
\mathrm{W\,m^{-2}\,K^{-1}},$$

$$A = \sigma T_0^4 - B\,T_0 = 301.347 - 1205.388 = -904.041\ \mathrm{W\,m^{-2}},$$

$$T_{\text{eq,lin}} = \frac{F - A}{B}
= \frac{238.175 + 904.041}{4.4644} = 255.850\ \mathrm{K}.$$

**Comparison.** The exact result is $254.578\ \mathrm{K}$; the linearised result is
$1.27\ \mathrm{K}$ **warmer**. The sign is the interesting part: the Taylor
expansion of $\sigma T^4$ about $270\ \mathrm{K}$ is a straight line tangent below
the curve at the evaluation point, and since the equilibrium lies *below*
$T_0 = 270\ \mathrm{K}$, a chord-to-curve comparison shows the tangent
overestimates $\sigma T^4$ for $T<T_0$... more precisely, $\sigma T^4$ is convex,
so its tangent lies *below* the curve on both sides, hence the tangent under-
estimates the emitted flux, hence the temperature needed to emit $F$ is
*over*-estimated. **A convex function linearised gives a biased answer in the
direction of convexity, and the bias scales with the square of the distance from
$T_0$** — $1.27\ \mathrm{K}$ for a distance of $15\ \mathrm{K}$ here.

---

## ★4 — Response to a step forcing

$$\Delta T(\infty) = \frac{\Delta F}{B} = \frac{4.0}{4.4644} = 0.896\ \mathrm{K}.$$

$$\Delta T(t) = \Delta T(\infty)\left(1 - e^{-t/\tau}\right), \qquad
\tau = \frac{C}{B} = \frac{3.200\times10^{8}}{4.4644} = 7.168\times10^{7}\
\mathrm{s} = 2.27\ \mathrm{yr}.$$

| $t$ | $1-e^{-t/\tau}$ | $\Delta T$ (K) |
|---|---|---|
| $1\tau$ (2.27 yr) | 0.6321 | 0.566 |
| $3\tau$ (6.82 yr) | 0.9502 | 0.851 |

After three relaxation times $95\%$ of the equilibrium response has been realised
— the standard working rule for "how long a climate experiment must run". Note
that this is the *idealised* timescale of a single mixed layer; a real ocean has a
spectrum of timescales, which is why the approach to equilibrium in a coupled model
takes centuries rather than years.

---

## ★5 — Relaxation time and the sign of the nonlinear residual

$$C\frac{\mathrm{d}T}{\mathrm{d}t} = F - (A + BT)
\;\Longrightarrow\;
\frac{\mathrm{d}T}{\mathrm{d}t} + \frac{B}{C}T = \frac{F-A}{C}.$$

This is a first-order linear ODE with solution

$$T(t) = T_\infty + \left(T_0 - T_\infty\right)e^{-t/\tau},
\qquad T_\infty = \frac{F-A}{B}, \qquad \tau = \frac{C}{B}. \;\checkmark$$

**$T_\infty$ is independent of $C$**: $C$ cancels from the equilibrium condition
$F = A + BT_\infty$. ✔

**Why the measured e-folding time exceeds $C/B$.** The linearised $\tau$ uses
$B = 4\sigma T_{\text{eq}}^3$ evaluated *at the equilibrium*. Along a trajectory
starting **colder** than equilibrium, the true local slope $4\sigma T^3$ is
*smaller* than $4\sigma T_{\text{eq}}^3$, so the restoring force is weaker and the
approach is slower — hence a longer measured e-folding time. The demonstration
measures exactly this: $5.4364\times10^{7}\ \mathrm{s}$ against
$5.3444\times10^{7}\ \mathrm{s}$, i.e. $+1.72\%$, for a start $4.6\ \mathrm{K}$
below equilibrium. **The sign is predicted by the direction of approach**: a start
*above* equilibrium would relax *faster* than $\tau$, and the asymmetry is the
signature of the fourth-power nonlinearity.

---

## ★6 — Discretisation, boundary conditions and the mean identity

**Discretisation.** With $f(x) = 1-x^2$ and uniform $\Delta x$,

$$\left[\frac{\partial}{\partial x}\left(f\frac{\partial T}{\partial x}\right)
\right]_i \approx
\frac{f_{i+1/2}(T_{i+1}-T_i) - f_{i-1/2}(T_i-T_{i-1})}{\Delta x^2},
\qquad
f_{i\pm1/2} = 1 - \left(\frac{x_i + x_{i\pm1}}{2}\right)^2 .$$

**Boundary conditions.**

- At $i = 0$ (equator, $x = 0$): there is no grid point at $i = -1$. The physical
  statement is that $\partial T/\partial x = 0$ at the equator by symmetry, so the
  flux through the equator face is zero. In the discretisation this is *implemented*
  by setting $f_{-1/2} \equiv 0$, i.e. by removing the face term.
- At $i = n-1$ (pole, $x = 1$): $f_{n-1/2} = 1 - 1^2 = 0$ **automatically**, so the
  pole face carries no flux without any extra statement.

**So the pole condition is not imposed at all — it is a property of the operator**,
because the metric factor $(1-x^2)$ vanishes there. Imposing an extra condition
would double-count and introduce an error. This is a general feature of
finite-volume discretisations in coordinates where the metric degenerates at a
boundary.

**The mean identity.** Write the discrete steady-state equations and sum over $i$:

$$\sum_i\left[\frac{D}{\Delta x^2}\left(f_{i+1/2}(T_{i+1}-T_i)
- f_{i-1/2}(T_i-T_{i-1})\right) - BT_i - A + Q_i(1-a_i)\right] = 0 .$$

The diffusion part is a telescoping sum:

$$\sum_i\left[f_{i+1/2}(T_{i+1}-T_i) - f_{i-1/2}(T_i-T_{i-1})\right]
= f_{n-1/2}(T_{\text{virtual}} - T_{n-1}) - f_{-1/2}(T_0 - T_{\text{virtual}})
= 0,$$

because both end fluxes are zero. Hence

$$\sum_i\left(-BT_i - A + Q_i(1-a_i)\right) = 0
\;\Longrightarrow\;
\langle T\rangle = \frac{\langle Q(1-a)\rangle - A}{B} . \;\checkmark$$

**The crucial point.** The uniform sum over the $x = \sin\phi$ grid *is* the
area-weighted integral over the sphere, because $\mathrm{d}x = \cos\phi\,
\mathrm{d}\phi$. Using a mean over a grid uniform in $\phi$ would give a different
(and wrong) answer — that error was made and caught during the development of the
demonstration, and it is worth repeating because a grid choice that looks innocent
is a silent area-weighting error.

---

## ★7 — Albedos of the two branches

At $S/S_0 = 1.40$:

$$Q = \frac{1.40 \times 1361}{4} = 476.35\ \mathrm{W\,m^{-2}}.$$

Setting $\sigma T^4 = Q(1-a)$ for each branch's global mean:

| branch | global mean $T$ (K) | implied $a$ |
|---|---|---|
| ice-free | 271.67 | $1 - \sigma(271.67)^4/476.35 = 0.3516$ |
| frozen | 239.34 | $1 - \sigma(239.34)^4/476.35 = 0.6094$ |

**Why they must differ, and do.** The two branches are solutions of the *same*
forcing with *different* albedos; that is what makes them two branches rather than
one. The computation recovers $0.35$ and $0.61$, both between the model's warm
($0.30$) and icy ($0.62$) values, and each an *area-weighted blend* of the two,
because each state has some fraction of its area above and below the ice threshold.
The frozen branch's albedo is nearly the icy value because almost all of its area
is icy; the ice-free branch's albedo is slightly above $0.30$ because part of its
area is icy. **A consistency check on the model: an implied albedo outside
$[0.30, 0.62]$ would indicate an error.**

---

## ★8 — The non-radiative flux a radiative profile would need

$$\sigma T_s^4\big|_{330\,\mathrm{K}} = 5.670374419\times10^{-8}\times330^4
= 672.46\ \mathrm{W\,m^{-2}},$$
$$\sigma T_s^4\big|_{288\,\mathrm{K}} = 390.105\ \mathrm{W\,m^{-2}},$$

$$\text{required non-radiative export} = 672.46 - 390.105 = 282.36\
\mathrm{W\,m^{-2}},$$

$$\frac{282.36}{238.175} = 1.186,$$

i.e. **$119\%$ of the absorbed solar flux** — and, crucially, *more than the
absorbed solar flux reaches the surface at all* in any model in which the surface
receives a fraction $f_s \le 1$ of $F$. **It is not physically possible.** The
surface cannot export more energy non-radiatively than it receives radiatively plus
from the atmosphere; and it cannot receive more from the atmosphere than the
atmosphere has. The excess is the quantitative diagnostic that the radiative
profile must be convectively adjusted.

**Note the pattern across the three cases** (from the lesson's §3.5): the required
export grows with the total infrared optical depth, and it exceeds $100\%$ of $F$
once the radiative surface temperature passes about $324\ \mathrm{K}$. Beyond that
point the radiative-equilibrium model is not merely inaccurate; it has no solution
consistent with a real surface energy budget.

---

## ★9 — Estimating the transport from the contrast

$$H \approx 2\pi R_E^2\,D\,\frac{\Delta T}{\Delta x}
= 2\pi(6.371\times10^{6})^2\times0.6\times\frac{24.052}{1.0}
= 3.680\times10^{15}\ \mathrm{W} = 3.68\ \mathrm{PW},$$

against the model's $2.643\ \mathrm{PW}$ — an **overestimate of $39\%$**.

**Which approximation was made, and why it overestimates.** Two:

1. **The gradient is not uniform.** Replacing $\mathrm{d}T/\mathrm{d}x$ by
   $\Delta T/\Delta x$ over the *full* range $x\in[0,1]$ uses the average slope
   everywhere. The transport is $D(1-x^2)\,\mathrm{d}T/\mathrm{d}x$, and since
   $(1-x^2)$ decreases toward the pole, the true maximum of the product occurs
   where the *product* peaks, at a smaller $x$ than the maximum of the gradient
   alone. The demonstration finds the peak at $x = \sin 38.1^\circ = 0.617$, not at
   $x = 1$.
2. **The contrast is not the right $\Delta T$.** The maximum transport is not at the
   latitude of maximum temperature difference but at the latitude where
   $(1-x^2)\,\mathrm{d}T/\mathrm{d}x$ is largest.

The estimate is therefore a *scale* estimate, good to a factor of about $1.4$, and
its usefulness is in giving the order of magnitude (a few PW) without solving the
model. That is exactly the level at which such estimates should be used, and saying
so is part of the answer.

---

## ★10 — Specification for locating both bifurcation points

1. **Order parameter.** The ice edge latitude $\phi_{\text{ice}}$, defined as the
   first grid point (from the pole) at which the albedo takes the icy value; or,
   better and grid-independent, the *fraction of the surface area with icy albedo*,
   $A_{\text{ice}} = 1 - \sin\phi_{\text{ice}}$, which is continuous in the
   parameter even when $\phi_{\text{ice}}$ jumps between grid points.
2. **Method: pseudo-arclength continuation.** Treat $S/S_0$ as an unknown and
   continue the solution branch in arclength, which steps *through* folds rather
   than failing at them. The alternative — simple parameter sweeping with a
   sign-of-jump test — locates the fold only to the resolution of the sweep.
3. **Tolerance.** Bisect on $S/S_0$ within the bracketing interval until the two
   branches (warm-start and cold-start fixed points) differ by less than
   $10^{-3}$ in $S/S_0$. Report the values and the number of iterations.
4. **Expected failure mode.** Starting the fixed-point iteration *exactly* on a fold
   makes the iteration converge to neither branch: the map is marginally stable
   there, so the iteration either oscillates between the two albedo patterns or
   converges very slowly. The symptom is a residual that stops decreasing while
   still of order the width of the transition. **Diagnosing that symptom is the
   practical content of the exercise**, and the remedy is to step off the fold in
   arclength rather than to iterate harder.
5. **What would falsify "these are the ends of one loop".** If, starting from the
   intermediate state between the two fold points, the iteration converged to a
   *third* branch not connected to either — or if a branch were found that does not
   connect to the ice-free solution in the limit of large $S/S_0$ — then the
   structure would not be a simple hysteresis loop. Continuation along the branch
   from large $S/S_0$ downward and checking that it terminates at the upper fold is
   the check.

---

## ★11 — Where the mean-transport identity fails

**Design.** Run the one-dimensional EBM at fixed $D$ with two configurations:
(i) the linear model (fixed albedo), and (ii) the nonlinear model (step albedo).
For each, record the area fraction with icy albedo, $A_{\text{ice}}$, and the
area-weighted mean temperature $\langle T\rangle$.

**Prediction.** In (i), $\langle T\rangle$ is independent of $D$ to machine
precision (the lesson measures $1.1\times10^{-10}\ \mathrm{K}$ across a fourfold
change in $D$). In (ii), $\langle T\rangle$ is *not* independent of $D$, because
changing $D$ changes the ice edge, which changes the albedo, which changes the
mean forcing.

**Expected scaling.** Near a bifurcation the sensitivity
$\mathrm{d}\langle T\rangle/\mathrm{d}A_{\text{ice}}$ is largest, because a small
change in area changes the global albedo by
$\Delta a \approx (a_{\text{ice}} - a_{\text{warm}})\Delta A_{\text{ice}}$, and the
mean temperature responds as
$\Delta\langle T\rangle \approx -\langle T\rangle\,\Delta a/[4(1-a)]$ by the
fourth-root relation. The failure of the identity should therefore itself be
*linear* in the ice-area change and *divergent* in slope near the folds.

**One paragraph on the implication.** The statement "changing the ocean circulation
cannot change the global mean temperature" is **false** wherever the circulation
changes something that feeds back on the albedo or on any other nonlinearity. In a
linear model it is exactly true, and §3.3 proves it — which is precisely why the
linear model must not be used to argue the point. The honest statement is: *pure
redistribution of a fixed energy input cannot change the mean, but redistribution
that changes the reflective or radiative properties of the system can.* The
qualifier is not a detail; it is where the physics lives.

---

## ★12 — Validation protocol using the pattern

**Observables and what each constrains.**

1. **The latitudinal temperature profile** $T(\phi)$, or its first two moments (the
   mean and the equator–pole contrast). The mean constrains the global energy
   balance (the combination $\langle Q(1-a)\rangle$ and $B$); the *contrast*
   constrains $D$ almost independently, as the lesson's table shows (a fourfold
   change in $D$ moves the contrast by a factor of $3.2$ while leaving the mean
   untouched). So the pair (mean, contrast) breaks the $(B, D)$ degeneracy.
2. **The ice edge latitude**, which constrains the *threshold temperature* and the
   ice albedo jointly — and, near a bifurcation, is extremely sensitive to both.
   This is the observable that constrains the nonlinearity.
3. **The seasonal cycle of temperature**, whose *amplitude* is set by the heat
   capacity $C$ and by the seasonal cycle of insolation, and whose *phase lag*
   relative to the insolation constrains $C$ again by an independent route. That
   pair breaks the $C$ degeneracy that a single mean temperature cannot touch.

**Which single observable is most efficient.** The **ice edge latitude**. The
reason is structural rather than numerical: the model's parameters enter it through
*a threshold* crossed by a *gradient*, so the ice edge is a strong function of
nearly every parameter ($D$ through the contrast, $B$ through the mean, the
albedos directly, the threshold directly, and $Q$ through the insolation profile)
while the mean temperature is insensitive to $D$ by construction. **An observable
that depends strongly on every parameter rules out more parameter combinations per
measurement than one that depends on a subset** — and the ice edge's dependence on
$D$ is exactly the dependence the mean lacks. The caveat is that it is also the
hardest observable to define operationally (a diffuse margin, seasonal ice, and
a threshold that is a model construct), so a defensible protocol uses it as a
strong constraint *alongside* the profile and the seasonal cycle, and states that
its uncertainty is dominated by the definition rather than by the measurement.
