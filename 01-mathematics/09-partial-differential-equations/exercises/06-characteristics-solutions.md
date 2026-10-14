# Solutions — 01-09-06 Method of Characteristics and First-Order PDEs

> **Read this after attempting the exercises, not before.**
>
> Worked solutions with the reasoning; numbers were computed (root-finding for the
> implicit characteristic maps was done numerically to $10^{-6}$ or better).
> Conventions: conservation form $u_t + f(u)_x = 0$; characteristics
> $dx/dt = f'(u)$; Rankine–Hugoniot speeds as derived in ★★8.

---

## ★1 — Constant-velocity transport

**Characteristic equations.** For $u_t + 3u_x = 0$ with $a = 3$, $b = 1$:

$$\frac{dx}{dt} = 3, \qquad \frac{du}{dt} = 0 ,$$

so the characteristics are $x = x_0 + 3t$ and $u$ is constant along each. Solving
for the label, $x_0 = x - 3t$, so

$$u(x,t) = f(x - 3t) = \mathrm{e}^{-(x-3t)^2} .$$

**At $x = 10$, $t = 2$:** $x - 3t = 10 - 6 = 4$, so

$$u(10,2) = \mathrm{e}^{-16} = 1.125\times10^{-7} .$$

**The characteristic through that point.** Backward in time from $(10,2)$, the line
$x = 10 + 3(t - 2)$ meets the initial line at $x_0 = 4$, $t = 0$: the disturbance
that is now at $x = 10$ started at $x = 4$ and travelled 6 m in 2 s at speed 3.
Every point on that line carries the same value $\mathrm{e}^{-16}$.

**Two remarks worth generalising.**

- The problem needs *one* initial condition and no boundary condition on an
  infinite domain. On a finite domain it needs one condition at the *inflow* end
  (here $x = 0$, where $u$ is prescribed by the data entering), and none at the
  outflow end.
- The result is a rigid translation with no change of shape, so the amplitude at
  $x = 10$ is exactly the initial amplitude at $x = 4$. Compare the diffusion
  equation, where the same feature would have decayed by
  $\exp(-4\kappa t \cdot(\text{curvature}))$ in addition to spreading.

---

## ★2 — Variable coefficient

**(a) Characteristic equations.** For $u_t + xu_x = 0$: $dx/dt = x$, $du/dt = 0$.
Integrating, $x = x_0\mathrm{e}^{t}$ and $u = u_0(x_0)$, so
$x_0 = x\mathrm{e}^{-t}$ and

$$u(x,t) = f\!\left(x\mathrm{e}^{-t}\right) = \sin\!\left(\pi x\mathrm{e}^{-t}\right) .$$

**(b) At $x = 1$, $t = 1$:** $x\mathrm{e}^{-t} = 1/\mathrm{e} = 0.367879$, so

$$u = \sin(\pi/\mathrm{e}) = \sin(1.155727) = 0.915089 .$$

**(c) At $x = 2$, $t = \ln 2$:** $x\mathrm{e}^{-t} = 2/2 = 1$, so

$$u = \sin(\pi) = 0 .$$

**(d) The feature at $x_0 = 0.5$ after $t = 1$:**

$$x = 0.5\,\mathrm{e}^{1} = 1.3591 .$$

So the feature has moved *outward* from 0.5 to 1.36 — it has been stretched in
space, while its amplitude is unchanged. This is a **rarefaction**: the
characteristics diverge, the profile flattens in the shifted coordinate, and an
observer stationed at fixed $x$ sees a slowly varying signal.

**The physical reading, in one paragraph.** The map $x = x_0\mathrm{e}^t$ is a
one-parameter dilation. Everything the model produces is the initial condition seen
through that dilation: to recover the source one must *un-stretch* by
$x_0 = x\mathrm{e}^{-t}$, which is not an inversion but a change of variable. Two
consequences follow. First, resolution is lost in the stretched coordinate —
features that were separated by $\Delta x_0$ are separated by
$\Delta x_0\mathrm{e}^t$ in the observation, so the information is spread out rather
than destroyed. Second, nothing crosses $x = 0$: the characteristic through the
origin is $x = 0$ for all time, so the two half-lines never exchange information.
That is the mathematical content of a divided-flow system in which the coefficient
vanishes at a stagnation point.

---

## ★3 — Verification and a jump

**Verification.** With $u = f(x-ct)$, write $s = x - ct$:

$$u_t = -cf'(s), \qquad u_x = f'(s)
\qquad\Longrightarrow\qquad
u_t + cu_x = -cf'(s) + cf'(s) = 0 .$$

The identity is exact for any differentiable $f$, and it holds *without* assuming
anything about the magnitude of $c$ (which may be negative, giving left-going
transport).

**A jump in $f$.** If $f$ has a jump at $s_0$, then $u$ has a jump across the line
$x - ct = s_0$, i.e. across the moving line $x = s_0 + ct$. The function is
**not differentiable** there, so it is **not a classical solution**: the PDE in its
differential form is not satisfied at the jump.

What remains true is the *integral* (conservation) form. Integrating
$u_t + (f(u))_x = 0$ across a thin box straddling the jump and letting its width
tend to zero gives

$$\frac{dx_s}{dt} = \frac{f(u_R) - f(u_L)}{u_R - u_L} = c ,$$

i.e. the jump moves at exactly $c$ — the same speed as the smooth parts. So the
"solution" is a **weak solution**: a function satisfying the conservation law in the
integral sense, piecewise smooth with a moving discontinuity. For the linear
advection equation a jump is a *contact discontinuity*: it moves at the characteristic
speed and is neither smoothed nor sharpened, because $f'(u) = c$ does not depend on
$u$.

**Why this matters in practice.** Real measured fronts are never true
discontinuities: some diffusion, dispersion or finite resolution smears them. The
weak-solution language is what allows a model to describe the front *without*
resolving its structure, and it is why the numerical schemes of ★★7 and Section 5 of
the lesson must be written in conservation form — a non-conservative scheme
converges to the wrong weak solution when a jump is present.

---

## ★4 — Breaking of a sine wave

**(a) Breaking time.** For $u_0 = \sin x$, $u_0'(x) = \cos x$ with minimum $-1$
attained at $x_0 = \pi$ (mod $2\pi$). Hence

$$t_s = -\frac{1}{\min u_0'} = -\frac{1}{-1} = 1 .$$

**(b) Location.** The characteristic that breaks first is the one for which
$1 + u_0'(x_0)t = 0$. Since $u_0'(\pi) = -1$, that is the characteristic through
$x_0 = \pi$, and it does not move, because

$$x = x_0 + u_0(x_0)t = \pi + \sin(\pi)t = \pi .$$

So the shock first forms at the *fixed* point $x = \pi$, for all times up to $t_s$.
Two independent checks: the same point carries the maximum slope (★★6), and it is the
point where the *compression* $\partial_x u$ is most negative — which is exactly what
"the characteristic breaks" means.

**A subtlety worth stating.** The condition for breaking involves the *derivative of
the initial velocity*, and the location of the break is where $u_0'$ is *minimum*,
not where $u_0$ is minimum or maximum. Students often look for the steepest part of
the visible profile, which is where $u_0'$ is largest in magnitude but not
necessarily most negative. Here the two coincide at $\pi$ because $\sin$ is odd
about $\pi$; for a general profile they do not, and a wrong location follows from a
wrong criterion.

**(c) Beyond $t_s$.** The map $x_0\mapsto x = x_0 + \sin(x_0)t$ ceases to be
invertible: for $t>1$ there are pairs $x_0^1<x_0^2$ with the same image $x$ and
different values of $u$, so the classical solution **does not exist**. The
conservation form still makes sense, and the physically correct answer is a weak
solution with a shock. For this problem the shock forms with left and right states
approaching $+1$ and $-1$ as $t\to1^+$ (the extreme values reached by the
characteristic family), and its speed follows the Rankine–Hugoniot condition
$$s = \tfrac12(u_L + u_R)$$ — see ★★8. The discontinuity then decays in amplitude as
the shock propagates into the unbroken parts of the wave, which is the standard
behaviour of a Burgers sawtooth.

---

## ★★5 — A steepening tanh profile

**(a) Breaking time.** For $u_0 = 1-\tanh x$, $u_0' = -\mathrm{sech}^2x$, whose
minimum is $-1$ at $x = 0$. Hence $t_s = 1$, and the first break occurs on the
characteristic through $x_0 = 0$, where
$x = 0 + u_0(0)t = 0$: the shock forms at $x = 0$.

**(b) The profile at $t = 0.4$.** The solution is implicit:
$u = u_0(x_0)$ with $x = x_0 + u_0(x_0)t$ and $t = 0.4$. Solving
$x_0 + 0.4(1-\tanh x_0) = x$ numerically (bisection to $10^{-9}$):

| $x$ | $x_0$ | $u = 1-\tanh x_0$ |
|---|---|---|
| $-1$ | $-1.777782$ | $1.944456$ |
| $0$ | $-0.620625$ | $1.551563$ |
| $1$ | $0.883209$ | $0.291977$ |

**(c) The asymmetry.** Reading down the table: at $x=-1$ the value is $1.944$; at
$x=0$ it is $1.552$; at $x=1$ it is $0.292$. The profile has a steep, nearly linear
segment between $x=-1$ and $x=1$ — the region of compression — and the initial
profile's shape (values near 2 on the left, near 0 on the right) is compressed into
a narrower interval. Quantitatively: the initial profile varies over $x\in(-2,2)$
roughly, whereas at $t = 0.4$ the same variation is concentrated into $x\in(-1,1)$,
about half the width. That is the steepening, and it is what terminates at
$t = t_s = 1$.

The asymmetry in the three values (1.94, 1.55, 0.29) is not an artefact: the
characteristics move at speed $u_0$, so the high-value (left) part of the profile
travels faster and catches up with the low-value part. The consequence is that at
any fixed time *before breaking*, the profile's steepest point is not at the
midpoint of the range.

**A check on the numerics.** The characteristic equation is monotone for $t<t_s$
($dx/dx_0 = 1 + u_0't \ge 1 - t > 0$), so the root is unique and bisection cannot
converge to a spurious branch. That check should always be made before trusting a
root-finder on an implicit characteristic map: after $t_s$ the same routine would
return one of several roots and give a meaningless "solution".

---

## ★★6 — The gradient formula

**Derivation.** The characteristic solution is given implicitly by

$$x = x_0 + u_0(x_0)t, \qquad u = u_0(x_0) .$$

Differentiate $u$ with respect to $x$ at fixed $t$:

$$u_x = \frac{du}{dx} = \frac{u_0'(x_0)}{dx/dx_0} = \frac{u_0'(x_0)}
{1 + u_0'(x_0)t} ,$$

using the chain rule and $dx/dx_0 = 1 + u_0'(x_0)t$ from the implicit relation. This
is the required formula; note that the denominator is *not* $1 + u_0''t$ — a
mis-statement seen often, and it gives the wrong breaking time.

**For $u_0 = \sin x$: $u_0' = \cos x$, so**

$$u_x = \frac{\cos x_0}{1 + t\cos x_0} ,$$

and the maximum of $\lvert u_x\rvert$ over $x_0$ is attained where $\cos x_0 = -1$
(any other value gives a smaller numerator and a larger denominator), i.e. at
$x_0 = \pi$, where the characteristic stays at $x = \pi$:

$$\boxed{\ \max\lvert u_x\rvert = \frac{1}{1-t}\ }$$

**Values.**

| $t$ | $\max\lvert u_x\rvert$ |
|---|---|
| $0.5$ | $2$ |
| $0.9$ | $10$ |
| $0.99$ | $100$ |

**Reading.** The gradient diverges as $1/(1-t)$, not as $1/\sqrt{1-t}$ or
$1/(1-t)^2$; the exponent is one because the denominator is linear in $t$. The
demonstration's upwind scheme reproduces this to within 0.1 % at $t = 0.2$ and
under-predicts by 20 % at $t = 0.95$, the shortfall being the scheme's own numerical
viscosity smoothing the peak over a few cells. **A verification of this kind must
therefore report both the exact and the measured numbers plus the ratio**, as the
demonstration does, rather than asserting agreement.

**A cross-check using the exact solution of the worked problem.** The same formula
appears in the well-known special case $u_0(x) = -x$ on an interval, where
$u_x = -1/(1-t)$ exactly, and the shock forms simultaneously everywhere at $t = 1$.
That degenerate case is a useful sanity check on any implementation of the implicit
map.

---

## ★★7 — Numerical diffusion of the upwind scheme

**(a) The coefficient.** With $c = 1$, $\Delta x = 0.01$ and $\nu = 0.6$,

$$D_{\text{num}} = \frac{c\,\Delta x}{2}(1-\nu) = \frac{1\times0.01}{2}\times0.4
= 2.0\times10^{-3} .$$

**(b) Variance growth rate.** For a diffusion term $D\,u_{xx}$ in one dimension,
the second central moment of a pulse grows at rate $2D$:

$$\frac{d\langle (x-\bar x)^2\rangle}{dt} = 2D_{\text{num}} = 4.0\times10^{-3}
\ \mathrm{m^2\,s^{-1}} .$$

So over a run of duration $t = 1$ (in units with $c = 1$) the variance added is
$4.0\times10^{-3}$, and the width added is
$\sqrt{2D_{\text{num}}t} = \sqrt{4.0\times10^{-3}} = 6.3\times10^{-2}$ m — i.e.
about 6 cells' worth of additional spreading. The *measured* value in the module's
demonstration, with $\Delta x = 0.01$ and $\nu = 0.8$, was
$2.005\times10^{-3}$ against the predicted $2.000\times10^{-3}$, a 0.26 % agreement,
which is the verification that the modified equation is being realised.

**(c) The error from omitting it.** If the numerical spreading is interpreted as
physical, the inferred diffusivity is $D_{\text{num}}$ instead of zero — an error of
100 % in a problem whose true diffusivity is zero, and an over-estimate of the
spreading (i.e. an under-estimate of the resolution) in any problem with a real
diffusivity. As a *percentage of the pulse width*: the width grows from the initial
width $w_0$ to $\sqrt{w_0^2 + 2D_{\text{num}}t}$; for an initial width of, say,
10 cells ($w_0 = 0.1$ m) the fractional width increase over $t = 1$ is

$$\frac{\sqrt{0.1^2 + 4.0\times10^{-3}} - 0.1}{0.1} = 0.19 ,$$

i.e. about 19 %. For a narrower pulse the same numerical diffusion is far more
damaging: with $w_0 = 0.02$ m (2 cells) the fractional increase is 68 %, and the
pulse is destroyed as a recognisable feature.

**The general lesson.** $D_{\text{num}}\propto\Delta x(1-\nu)$: refining the grid
reduces it linearly, and $\nu = 1$ eliminates it in the constant-velocity case only.
A first-order upwind scheme is therefore acceptable for a *conservative* tracer in a
coarse model but must not be used to argue that a physical front has broadened, or
that a measured amplitude decay is attenuation. Second-order or flux-limited schemes
exist for exactly this reason, and the diagnostic above (compute $D_{\text{num}}$,
compare with the physical $D$) takes one line.

---

## ★★8 — Rankine–Hugoniot

**Derivation.** Integrate $u_t + f(u)_x = 0$ over the box
$[x_s(t)-\varepsilon, x_s(t)+\varepsilon]\times[t_1,t_2]$ where $x_s(t)$ is the
discontinuity:

$$\int_{t_1}^{t_2}\!\!\int_{x_s-\varepsilon}^{x_s+\varepsilon}
u_t\,dx\,dt + \int_{t_1}^{t_2}\!\!\int_{x_s-\varepsilon}^{x_s+\varepsilon}
f(u)_x\,dx\,dt = 0 .$$

The second integral is evaluated exactly in $x$:
$\int[f(u)]_{x_s-\varepsilon}^{x_s+\varepsilon}dt
= \int_{t_1}^{t_2}\left[f(u_R) - f(u_L)\right]dt$ (the states just outside the
layer). The first integral is rewritten using the Leibniz rule, taking account of the
moving boundary:

$$\int_{x_s-\varepsilon}^{x_s+\varepsilon}u\,dx\bigg\rvert_{t_1}^{t_2}
- \int_{t_1}^{t_2}\left[u_R\dot x_s - u_L\dot x_s\right]dt = 0
\quad\text{to leading order as }\varepsilon\to0.$$

Letting $\varepsilon\to0$ with $t_2-t_1\to0$ and dividing by the time interval:

$$(u_R - u_L)\frac{dx_s}{dt} = f(u_R) - f(u_L)
\qquad\Longrightarrow\qquad
\boxed{\ s = \frac{f(u_R)-f(u_L)}{u_R-u_L}\ }$$

**Evaluation for Burgers.** $f(u) = \tfrac12u^2$, $u_L = 1$, $u_R = -0.5$:

$$s = \frac{\tfrac12(0.25) - \tfrac12(1)}{-0.5 - 1}
= \frac{0.125 - 0.5}{-1.5} = \frac{-0.375}{-1.5} = 0.25 .$$

So the shock moves to the right at speed $0.25$ — *slower* than the left state
(speed 1) and *faster* than the right state (speed $-0.5$), which is the
consistency condition that must hold for a compressive shock: the discontinuity
speed must lie between the characteristic speeds on either side, or characteristics
would emerge from the shock rather than enter it.

**The entropy condition.** For a convex flux ($f''>0$), the physically admissible
shock is the **compressive** one,

$$f'(u_L) > s > f'(u_R) \qquad\Longleftrightarrow\qquad u_L > u_R ,$$

which for Burgers reads $u_L > u_R$: the flow must converge onto the discontinuity.
The opposite configuration ($u_L<u_R$) is a **rarefaction** and must be resolved as a
continuous expansion fan, not as a shock. Without the entropy condition the weak
solution is not unique — both a shock and a rarefaction can satisfy the integral
statement — and the entropy condition is what selects the physically observed one.

**A check.** For $u_L = u_R$ the formula gives $0/0$; expanding shows
$s\to f'(u)$, recovering the characteristic speed. And for the special case
$f(u) = \tfrac12u^2$, $s = \tfrac12(u_L+u_R)$, which is the average of the states.

---

## ★★★9 — Measuring the gradient of a breaking wave

**Method.** The upwind (sign-dependent) scheme
$u^{n+1}_j = u^n_j - u^n_j(\Delta t/\Delta x)(u^n_j - u^n_{j-1})$ for $u\ge0$ and the
mirror form for $u<0$, with $\Delta t = 0.5\Delta x$ (so the local Courant number is
at most 0.5), on $[0,2\pi)$ periodic, $u_0 = \sin x$. The gradient is measured with
a central difference on the numerical solution, and the reference is the exact
$1/(1-t)$ from ★★6.

**(a) Measured gradients.** The module's `code/characteristics.py` reports, at
$N = 1200$ grid points:

| $t$ | exact $1/(1-t)$ | measured $\max\lvert u_x\rvert$ | ratio |
|---|---|---|---|
| $0.20$ | $1.250000$ | $1.249067$ | $0.9993$ |
| $0.40$ | $1.666667$ | $1.662893$ | $0.9977$ |
| $0.60$ | $2.500000$ | $2.484579$ | $0.9938$ |
| $0.80$ | $5.000000$ | $4.886867$ | $0.9774$ |
| $0.90$ | $10.000000$ | $9.290199$ | $0.9290$ |
| $0.95$ | $20.000000$ | $16.097461$ | $0.8049$ |

**(b) How the required grid scales with $t$.** The exact profile develops a layer of
thickness $\ell(t)$ containing the sharp feature; near the breaking point the
gradient is $1/(1-t)$ and the change of $u$ across the layer is of order unity, so

$$\ell(t) \sim \frac{\Delta u}{\max\lvert u_x\rvert} \sim (1-t) .$$

To resolve that layer with a fixed number of cells requires
$\Delta x\lesssim \ell(t)/n_{\text{cells}}$, i.e. the number of grid points must grow
as

$$N \gtrsim \frac{2\pi\,n_{\text{cells}}}{1-t} .$$

So refining in time by a factor two (halving $1-t$) doubles the required grid. This
is why the measured ratio degrades as $t\to1$ at *fixed* grid: the layer shrinks
below the cell size and the scheme's numerical viscosity takes over. It is also
why a fixed-tolerance study of a breaking wave cannot be done with a fixed grid —
either the grid is refined with time or the study stops before breaking. Note the
practical corollary: the *cost* of resolving a shock grows as $(1-t)^{-1}$ in one
dimension and as $(1-t)^{-d}$ in $d$ dimensions, which is the reason shock-resolving
schemes (high-order with limiters, or adaptive meshes) exist at all.

**(c) Which part is a numerical artefact.** The shortfall — everything by which the
measured value falls below $1/(1-t)$ — is numerical: it is the scheme's diffusion
smearing the peak over a few cells, and it is directly analogous to the
$D_{\text{num}}$ of ★★7. The evidence that it is numerical and not physical is that

- it shrinks as the grid is refined *at fixed $t$* (a convergence test), which no
  physical effect would do;
- its magnitude is predicted by the modified equation's diffusion acting on a
  feature of width $\ell(t)$;
- the *exact* solution of the PDE has no such shortfall by construction.

The *divergence* itself, however, is physical: the exact solution's gradient grows
without bound, and the scheme merely fails to follow it. Distinguishing "the scheme
under-resolves a real singularity" from "the scheme created a feature that is not
there" is the essential step, and the test is refinement at fixed physical time.

**(d) Limits.** The comparison presupposes that the exact solution exists at the
times measured — valid for $t<t_s = 1$ only. At and beyond $t_s$ the classical
solution does not exist, and the "exact $1/(1-t)$" formula is meaningless; the
scheme then converges to a *weak* solution whose shock speed is set by
Rankine–Hugoniot (★★8), and the correct comparison is against that weak solution,
not against the multivalued classical one. Additionally, the measured gradient
depends on the difference stencil used to compute it (central, one-sided, or a
spline derivative), all of which are $O(\Delta x^2)$ approximations of a quantity
that is itself divergent — so a reported "maximum gradient at $t=0.99$" is a
statement about the grid as much as about the wave and must be reported with the
grid.

---

## ★★★10 — Kinematic waves in a river reach

**(a) The kinematic wave speed.** With $q = Ku^{5/3}$,

$$c(u) = \frac{dq}{du} = \frac{5}{3}Ku^{2/3} = \frac{5}{3}\frac{q(u)}{u} ,$$

which is $\tfrac53$ times the mean velocity $q/u$ for this flux law. The flux is
**convex**, $q''(u) = \tfrac{10}{9}Ku^{-1/3} > 0$ for $u>0$, so the nonlinearity is
of the compressive type and the theory of ★4 applies.

Two checks on the algebra: the exponent $\tfrac53$ is the Manning-exponent
convention, and $c>q/u$ (the wave outruns the fluid) is the classical kinematic-wave
result — a flood wave travels faster than the water that carries it, which is why
flood peaks travel faster than the mean flow and why the peak arrives before the
bulk of the water.

**(b) Steepening or spreading?** For $u_t + c(u)u_x = 0$ with $c'(u)>0$,
characteristics diverging or converging is decided by the sign of
$\partial_x u$: where the profile *decreases* downstream
($\partial_x u<0$), the characteristics converge and the profile **steepens**;
where it increases, the profile spreads as a rarefaction.

For a flood hydrograph the *rising limb* has $\partial u/\partial x>0$ (discharge
increasing downstream in the direction of travel is the same as increasing in time
at a fixed station — but note the sign convention carefully: in the direction of
propagation the leading edge is where discharge is falling, and that is where
steepening occurs). The steepening therefore begins on the **falling limb** of the
hydrograph, i.e. at the front of the flood, not at the back. This is the observed
behaviour of kinematic river waves: the front sharpens and the recession is
stretched.

A practical consequence: the peak discharge is preserved (the equation conserves
$u$) but the *shape* changes, so a hydrograph measured upstream cannot be used
directly downstream without accounting for the steepening — the travel time of the
peak is the characteristic speed of the peak's own discharge, $c(u_{\text{peak}})$,
which is larger than the speed of the lower discharges, so the peak separates from
the body of the flood.

**(c) Two effects a kinematic wave cannot represent.**

1. **Momentum effects, hence backwater and upstream influence.** The kinematic
   reduction replaces the momentum equation by a local flux--storage relation
   $q = q(u)$, which contains no spatial derivative of the momentum. A kinematic
   model therefore cannot produce a backwater curve, a hydraulic jump, or any
   dependence of conditions at a point on what happens *downstream*. Real rivers
   have upstream influence through the free-surface gradient, and in low-slope or
   tidally forced reaches the kinematic approximation fails badly; the
   diffusive-wave or full dynamic-wave formulations are required.
2. **Looping rating curves and hysteresis.** Because $q = q(u)$ is single-valued by
   assumption, a kinematic model cannot reproduce the observed hysteresis of a
   flood — the same discharge occurring at a higher stage on the rising limb than
   on the falling limb. The hysteresis is a momentum (or diffusion) effect, and its
   absence is a *falsifiable* prediction of the kinematic model, not merely a
   limitation.

Two further candidates worth naming: lateral inflow and storage change (which break
the pure conservation form) and the friction law's dependence on unmodelled
quantities such as vegetation or bedform change.

**(d) A falsifying observation, and what to conclude.** The kinematic prediction is
that the flood peak travels at $c(u_{\text{peak}}) = \tfrac53\bar v$ (with $\bar v$
the mean velocity at peak discharge) and that the peak travels *faster* than the
body of the flood, with a hydrograph that steepens at the front and stretches at
the back.

A falsifying observation would be one of:

- **measured peak celerity less than or equal to the mean velocity**, or a peak that
  arrives *after* the bulk of the discharge — the kinematic model requires the
  opposite;
- **demonstrated upstream influence**, e.g. a downstream control (a weir, a tidal
  boundary, a confluence backwater) measurably affecting the hydrograph
  *upstream* of it — impossible in a kinematic model;
- **a measured rating curve that loops** while the model predicts a single-valued
  relation.

If the observation contradicted the prediction, the correct conclusion would be
that the flux--storage closure is insufficient, not that the data are wrong. The
diagnosis would proceed by measuring the free-surface slope (to quantify the
diffusive term), computing the dimensionless wave amplitude to slope ratio, and
testing a diffusive-wave model against the same data — the standard escalation in
flood-wave modelling. Note what the exercise does *not* license: concluding from a
single hydrograph that "the kinematic wave is wrong". The model fails in a specific
regime (low slope, strong downstream control, large amplitude), and locating the
regime boundary is the informative result.
