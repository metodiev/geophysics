# Solutions — 01-09-03 The Wave Equation and Its Physical Content

> **Read this after attempting the exercises, not before.**
>
> Worked solutions with the reasoning; numbers were computed rather than estimated.
> Conventions: $u_{tt} = c^2u_{xx}$; $\sigma = c\,\Delta t/\Delta x$;
> $\alpha^2 = (\lambda+2\mu)/\rho$, $\beta^2 = \mu/\rho$; $g = 9.81\
> \mathrm{m\,s^{-2}}$.

---

## ★1 — String speed and travel time

$$c = \sqrt{\frac{T}{\rho_l}} = \sqrt{\frac{250}{0.02}}
= \sqrt{1.25\times10^{4}} = 111.80\ \mathrm{m\,s^{-1}} ,$$

$$t = \frac{15}{111.80} = 0.1342\ \mathrm{s} .$$

**If the tension is halved**, $c \propto \sqrt{T}$, so
$c = 111.80/\sqrt{2} = 79.06\ \mathrm{m\,s^{-1}}$ and the travel time rises by
$\sqrt{2}$ to $0.1897$ s. Note the asymmetry: to *double* the speed the tension
must be *quadrupled*. This square-root dependence on the restoring force is the
same dependence that appears in $c = \sqrt{k/\rho}$ for solids and
$\sqrt{gh}$ for shallow water, and it is the reason velocity is a poor discriminator
of stiffness in inversion: a factor of two in speed needs a factor of four in the
modulus.

**Why the amplitude does not appear.** The derivation of $c$ used only the
linearised (small-angle) restoring force and the inertia, neither of which involves
the amplitude. The linearity is an assumption: at large amplitude the tension
changes with displacement and the equation becomes nonlinear, the speed becomes
amplitude-dependent, and the disturbance steepens — the mechanism of
[01-09-06](../06-characteristics.md).

---

## ★2 — Mode verification and what fixes what

**Verification.** With $u = \sin(kx)\cos(\omega t)$,

$$u_{tt} = -\omega^2u, \qquad u_{xx} = -k^2u, \qquad
u_{tt} - c^2u_{xx} = \left(-\omega^2 + c^2k^2\right)u .$$

This vanishes for all $x,t$ if and only if

$$\omega^2 = c^2k^2 \qquad\Longrightarrow\qquad
\omega = ck \quad (\omega,k>0).$$

The boundary conditions $u(0,t) = u(L,t) = 0$ require $\sin(kL) = 0$, so
$k = n\pi/L$ and

$$\boxed{\ \omega_n = \frac{n\pi c}{L}, \qquad
f_n = \frac{nc}{2L}\ }\qquad n = 1,2,3,\dots$$

**Which part fixes which quantity.**

| Quantity | Fixed by |
|---|---|
| Wavenumber $k = n\pi/L$ | the boundary conditions and the length |
| Frequency $\omega_n = n\pi c/L$ | the wavenumber and the medium speed — the *eigenvalue* problem |
| Amplitude and phase of each mode | the initial conditions — a projection, not an eigenvalue |
| Which modes are present at all | the symmetry of the initial condition |

So the mode *frequencies* are properties of the problem and the mode *amplitudes*
are properties of the data. A string plucked at its centre excites only the odd
modes, however hard it is plucked; the frequencies of the odd modes are unchanged
by how it was plucked. The same separation in a three-dimensional Earth makes
normal-mode frequencies a constraint on structure and the excitation a separate
problem, which is why source and structure can be inverted from the same record.

---

## ★3 — P and S speeds, and Poisson's ratio

$$\alpha = \sqrt{\frac{2.0\times10^{10} + 2\times1.5\times10^{10}}{2600}}
= \sqrt{\frac{5.0\times10^{10}}{2600}} = 4385.3\ \mathrm{m\,s^{-1}} ,$$

$$\beta = \sqrt{\frac{1.5\times10^{10}}{2600}} = 2401.9\ \mathrm{m\,s^{-1}} ,$$

$$\alpha^2 = 1.9231\times10^{7}, \quad \beta^2 = 5.7692\times10^{6} ,$$

$$\nu = \frac{\alpha^2 - 2\beta^2}{2(\alpha^2 - \beta^2)}
= \frac{1.9231\times10^{7} - 1.1538\times10^{7}}
       {2(1.9231\times10^{7} - 5.7692\times10^{6})}
= \frac{7.6923\times10^{6}}{2.6923\times10^{7}} = 0.2857 .$$

**Comment.** The value is $2/7 \approx 0.2857$, close to the $\nu = 0.25$ that
corresponds to $\lambda = \mu$ and to a Poisson solid, and consistent with the range
usually quoted for crustal rocks (roughly 0.2 to 0.3, rising towards 0.5 in
near-surface, water-saturated or partially molten material). Two cautions:

- **$\nu$ is a *derived* quantity here.** It was computed from assumed $\lambda$ and
  $\mu$, so it tests the consistency of the assumptions, not the Earth.
- **In field data the direction is reversed.** $\alpha/\beta$ is measured from
  arrival times; $\nu$ follows from it. The relation
  $\alpha/\beta = \sqrt{2(1-\nu)/(1-2\nu)}$ shows the sensitivity: near
  $\nu = 0.5$ the ratio diverges, so $\nu$ is poorly constrained in saturated
  material even when the arrival times are excellent. This is a good example of
  why derived parameters must be reported with propagated uncertainty rather than
  as exact transformations of measured ones.

---

## ★4 — Tsunami travel time

$$c = \sqrt{gh} = \sqrt{9.81\times4000} = 198.1\ \mathrm{m\,s^{-1}} ,$$

$$t = \frac{10^{6}}{198.1} = 5048\ \mathrm{s} = 1.402\ \mathrm{h} .$$

At this speed a trans-Pacific crossing of 8000 km takes about 11 hours, which is
why tsunami warning is a matter of hours and why the ocean's depth, not the wave's
height, sets the timescale.

**Assumptions of the shallow-water approximation.**

1. The water depth $h$ is small compared with the wavelength $\lambda$, so the
   vertical acceleration is negligible and the pressure is hydrostatic.
2. The amplitude is small compared with $h$, so the equations can be linearised.
3. The flow is irrotational and the bed is rigid and impermeable.
4. The wavelength is long compared with the depth variation, so $h$ may be treated
   as slowly varying along the path (and the WKB-type approximation used for
   refraction is valid).

**Does $\lambda = 200$ km in $h = 4$ km satisfy them?** The ratio
$h/\lambda = 4/200 = 0.02$ is small, so assumption 1 is satisfied comfortably: the
shallow-water regime is precisely the long-wave regime. Typical deep-ocean tsunami
wavelengths are of order $10^{2}$ km with amplitudes of order 0.1–1 m, so
assumption 2 holds as well. What fails in practice is not the wave approximation
but the geometry: real bathymetry is not uniform, so the speed varies along the ray
and the wave refracts, which is the physical content of tsunami ray tracing.

---

## ★★5 — Von Neumann analysis of the leapfrog scheme

**Substitution.** Put $u^n_j = g^n\mathrm{e}^{\mathrm{i}j\theta}$ in

$$u^{n+1}_j = 2u^n_j - u^{n-1}_j + \sigma^2\left(u^n_{j+1} - 2u^n_j +
u^n_{j-1}\right).$$

The neighbour terms give
$u^n_{j\pm1} = g^n\mathrm{e}^{\mathrm{i}j\theta}\mathrm{e}^{\pm\mathrm{i}\theta}$,
so dividing through by $g^{n-1}\mathrm{e}^{\mathrm{i}j\theta}$:

$$g^2 = 2g - 1 + \sigma^2g\left(\mathrm{e}^{\mathrm{i}\theta} - 2 +
\mathrm{e}^{-\mathrm{i}\theta}\right).$$

Using $\mathrm{e}^{\mathrm{i}\theta} + \mathrm{e}^{-\mathrm{i}\theta} =
2\cos\theta$ and $2\cos\theta - 2 = -4\sin^2(\theta/2)$:

$$g^2 - 2\left(1 - 2\sigma^2\sin^2\frac{\theta}{2}\right)g + 1 = 0 .$$

**The roots.** Write $b = 2(1 - 2\sigma^2\sin^2(\theta/2))$. The product of the
roots is $1$ (the constant term), so the two roots are reciprocal. Therefore

$$\lvert g \rvert = 1 \text{ for both roots}
\quad\Longleftrightarrow\quad
\lvert b \rvert \le 2
\quad\Longleftrightarrow\quad
\left\lvert 1 - 2\sigma^2\sin^2\frac{\theta}{2}\right\rvert \le 1 .$$

The left inequality gives $1 - 2\sigma^2\sin^2(\theta/2) \le 1$, i.e.
$\sigma^2\sin^2(\theta/2) \ge 0$, always true. The right inequality gives
$-1 \le 1 - 2\sigma^2\sin^2(\theta/2)$, i.e.
$\sigma^2\sin^2(\theta/2) \le 1$. Since $\sin^2(\theta/2) \le 1$ with equality at
$\theta = \pi$, the condition that must hold for *all* $\theta$ is

$$\boxed{\ \sigma \le 1\ }$$

the CFL condition, obtained here purely from the scheme and independently of any
argument about characteristics.

**The alternating mode and $\sigma = 1$.** At $\theta = \pi$ the coefficient is
$b = 2(1 - 2\sigma^2)$, so the quadratic is $g^2 - 2(1-2\sigma^2)g + 1 = 0$:

| $\sigma$ | $b$ | Roots | Behaviour |
|---|---|---|---|
| $0.5$ | $+1$ | $\mathrm{e}^{\pm\mathrm{i}\pi/3}$ | neutral, modulus 1 |
| $1.0$ | $-2$ | $g = -1$ (double) | degenerate; a linearly growing parasitic solution is possible |
| $1.01$ | $-2.0804$ | $g = -0.7539,\ -1.3270$ | one root exceeds 1 in modulus: unstable |
| $1.05$ | $-2.41$ | modulus $1.8774$ | strongly unstable |

This last point is worth stating explicitly because it corrects a common
misreading: at exactly $\sigma = 1$ the alternating mode has a *double* root at
$g = -1$, so the general solution of the recurrence for that mode contains a term
proportional to $n(-1)^n$ — a linear growth in time. The scheme is marginally
stable for smooth data (it is exact for the PDE, as ★★7 shows) but the Nyquist mode
is not damped, and an initialisation or a boundary condition that excites it will
produce a slowly growing oscillation. This is why production codes use
$\sigma \approx 0.5$ rather than the theoretically exact $1$, and why the
demonstration of the lesson measured, for the alternating mode at $\sigma = 1$,
linear growth rather than a constant amplitude.

---

## ★★6 — Growth rate at $\sigma = 1.02$

**(a) The amplification factor.** With $\sigma = 1.02$,

$$2 - 4\sigma^2 = 2 - 4(1.0404) = -2.1616, \qquad \lvert \cdot \rvert = 2.1616 ,$$

$$(2-4\sigma^2)^2 - 4 = 4.6725 - 4 = 0.6725, \qquad \sqrt{0.6725} = 0.8201 ,$$

$$\lvert g \rvert = \frac{2.1616 + 0.8201}{2} = 1.4908 .$$

**(b) Growth in 500 steps.**

$$\lvert g \rvert^{500} = 1.4908^{500}
= 10^{500\log_{10}(1.4908)} = 10^{500\times0.17342} = 10^{86.7} .$$

An initial error of $10^{-12}$ therefore reaches $10^{-12}\times10^{86.7} =
10^{74.7}$.

**(c) Single precision.** No: a single-precision variable holds about 7
significant decimal digits, so the largest representable magnitude is near
$10^{38}$ (IEEE 754 binary32). The computation would overflow to infinity after
roughly $38/0.1734 = 219$ steps, long before the 500 requested. In double
precision (about $10^{308}$) the overflow occurs near $1776$ steps, so a 500-step
run completes and returns a number — which is exactly why an unstable run is
dangerous: it can produce plausible-looking output, of magnitude $10^{75}$ times the
data, without any error message.

**The practical lesson.** Instability is not detected by looking for a crash. The
diagnostics are (i) monitoring the maximum amplitude against the expected energy,
(ii) checking that $\sigma$ computed from the *largest velocity in the model* is
$\le 1$ at every step, and (iii) a convergence test: an unstable scheme does not
converge under refinement, so comparing two grids exposes it immediately.

---

## ★★7 — Exactness at $\sigma = 1$

**Reduction.** Setting $\sigma = 1$ in the scheme,

$$u^{n+1}_j = 2u^n_j - u^{n-1}_j + \left(u^n_{j+1} - 2u^n_j + u^n_{j-1}\right)
= u^n_{j+1} + u^n_{j-1} - u^{n-1}_j .$$

**Verification for a travelling wave.** Suppose $u^n_j = f(x_j - c\,n\Delta t)$
with $\Delta x = c\,\Delta t$, so $x_j = j\Delta x$ and
$x_j - cn\Delta t = (j - n)\Delta x$. Define $m = j-n$, so
$u^n_j = f(m\Delta x)$, $u^n_{j+1} = f((m+1)\Delta x)$,
$u^n_{j-1} = f((m-1)\Delta x)$ and $u^{n-1}_j = f((m-1)\Delta x)$. Substituting:

$$u^{n+1}_j = f((m+1)\Delta x) + f((m-1)\Delta x) - f((m-1)\Delta x)
= f((m+1)\Delta x) = f(x_j - c(n+1)\Delta t) ,$$

which is exactly $u^{n+1}_j$. So the right-moving solution is reproduced *exactly*,
for arbitrary $f$. The same computation with $m = j+n$ verifies the left-moving
solution. The scheme is exact at $\sigma = 1$ because the stencil's two spatial
points at level $n$ coincide with the two characteristic footpoints of level
$n+1$ — the numerical domain of dependence equals the physical one.

**The initialisation condition.** The second-order start for $u_t(x,0) = 0$ is

$$u^{-1}_j = u^0_j + \tfrac12\sigma^2\left(u^0_{j+1} - 2u^0_j +
u^0_{j-1}\right) = u^0_j + \tfrac12\left(u^0_{j+1} - 2u^0_j + u^0_{j-1}\right)
\quad (\sigma = 1).$$

This is the value the exact solution would have at $t = -\Delta t$ only to
$O(\Delta t^2)$ in general; for the *pure one-way* initial condition
$u(x,0) = f(x)$, $u_t(x,0) = -cf'(x)$, the exact value at $t = -\Delta t$ is
$f(x + c\Delta t) = f(x + \Delta x)$, and the correct start is
$u^{-1}_j = f(x_j + \Delta x)$ — a shift, not a second difference. If the scheme is
initialised with the second difference instead, the resulting solution is exact
*following* the first step for the part of the data that the initialisation
represented correctly, but the error introduced at step one is $O(\Delta t)$ and
then propagates and persists.

**What the error becomes when the condition is violated.** Initialising with
$u^{-1}_j = u^0_j$ (the naive choice, implying $u_t = 0$) makes the scheme first
order. Measured on the standing-wave test of the lesson's Section 5, in the maximum
norm:

| $N$ | second-order start | naive start $u^{-1}_j = u^0_j$ | ratio |
|---|---|---|---|
| $20$ | $5.425\times10^{-4}$ | $2.868\times10^{-2}$ | $53$ |
| $80$ | $3.603\times10^{-5}$ | $7.743\times10^{-3}$ | $215$ |
| $320$ | $2.285\times10^{-6}$ | $1.973\times10^{-3}$ | $863$ |

The naive error falls by only a factor of about two when the grid is halved (from
$2.87\times10^{-2}$ to $1.51\times10^{-2}$ to $7.74\times10^{-3}$): first order,
not second. The ratio therefore grows without bound as the grid is refined, which
is the diagnostic to look for — a *constant* ratio would indicate a
prefactor error, whereas a *growing* ratio indicates the wrong order. The lesson generalises: **whenever a two-time-level
scheme needs a second data value, it must be constructed to the same order as the
interior stencil, or the whole calculation drops to the lower order.**

---

## ★★8 — Energy, dissipation and its absence

**(a) Derivation.** Multiply $u_{tt} = c^2u_{xx}$ by $u_t$ and integrate over
$(0,L)$:

$$\int_0^L u_tu_{tt}\,dx = c^2\int_0^L u_tu_{xx}\,dx
= c^2\left[u_tu_x\right]_0^L - c^2\int_0^L u_{xt}u_x\,dx .$$

The boundary term vanishes for fixed ends (where $u_t = 0$ at $x = 0,L$ for all
$t$) and for free ends (where $u_x = 0$). Both integrals are now total time
derivatives:

$$\frac{d}{dt}\int_0^L\frac12u_t^2\,dx
= -c^2\frac{d}{dt}\int_0^L\frac12u_x^2\,dx
\qquad\Longrightarrow\qquad
\frac{d}{dt}\int_0^L\left(\tfrac12u_t^2 +
\tfrac12c^2u_x^2\right)dx = 0 ,$$

which is the conservation statement. The two terms are the kinetic and the elastic
energy densities, and their sum is constant.

**(b) Why non-dissipative is desirable, and the risk.** A long seismic record
integrates the equation for thousands of wavelengths. A dissipative scheme would
damp the amplitude, and — worse — would damp the high frequencies preferentially,
producing an apparent attenuation that is purely numerical. Since measured
attenuation is a physical observable from which $Q$ is inferred, a scheme that
invents attenuation corrupts the very quantity being measured. The leapfrog scheme
is therefore preferred for wave propagation, and the standard practice is to
verify non-dissipation by running a homogeneous problem for many periods and
checking that the amplitude is unchanged.

The risk of a neutrally stable scheme is the counterpart: it neither damps physical
modes nor spurious ones. Any energy injected by a mis-specified boundary, by a
parasitic mode (such as the degenerate Nyquist mode at $\sigma = 1$), or by
round-off in a marginally stable configuration grows slowly and is never removed.
In practice this is managed with $\sigma$ comfortably below 1, with a small amount
of numerical damping (or a filter applied to the solution, not the operator), and
by monitoring the total energy over the run.

**(c) Contrast with the diffusion equation.** For $u_t = \kappa u_{xx}$ the same
manipulation gives

$$\frac{d}{dt}\int_0^L u^2\,dx = -2\kappa\int_0^L u_x^2\,dx \le 0 ,$$

with *strict* inequality unless $u$ is constant. Diffusion is genuinely
dissipative: errors are damped and the long-time integration is self-correcting,
so a slightly inaccurate diffusive scheme is safe. Wave propagation is
conservative: errors persist, and a slightly inaccurate scheme accumulates them.
For long-time integration this inverts the usual intuition — **the wave equation
is the harder problem to integrate reliably**, even though its solutions are
smoother in appearance.

---

## ★★★9 — Variable velocity: order 2 survives, exactness does not

**Method.** Discretise $u_{tt} = c(x)^2u_{xx}$ with the leapfrog scheme using the
local coefficient at each node, with $c(x) = 1 + 0.5\sin(2\pi x)$, fixed ends,
$u(x,0) = \sin(\pi x)$, $u_t(x,0) = 0$ and a second-order start. Because
$c_{\max} = 1.5$, the time step is $\Delta t = 0.5\,\Delta x/c_{\max}$: the
*largest* velocity sets it, and using the mean velocity instead would give
$\sigma_{\max} = 1.5$ and immediate instability. The final time is $t = 0.3$.
There is no closed-form solution, so the reference is the same scheme on a
3200-node grid, interpolated linearly to each coarse grid.

**Measured convergence** (this is Section 6 of `code/wave_equation_cfl.py`, so the
numbers can be reproduced by running the module's code):

```text
       N         dx     max error   order
      50   1.96e-02     2.407e-04        
     100   9.90e-03     6.149e-05    1.97
     200   4.98e-03     1.561e-05    1.98
     400   2.49e-03     4.022e-06    1.96
     800   1.25e-03     1.005e-06    2.00
```

**The observed order is 2.** This is worth stating carefully because the opposite
is often supposed:

- the **stencil** is second-order accurate in $\Delta x$ and $\Delta t$, so it
  remains second order when the coefficient varies;
- the **coefficient** is sampled at the nodes rather than averaged over the cell,
  which is a second-order-consistent approximation because $c$ is *smooth* — the
  midpoint and node values of a smooth function differ by $O(\Delta x^2)$;
- the **time step** is set by $c_{\max}$, so the effective Courant number in the
  slow parts of the model is below 0.5. That costs accuracy relative to a
  locally optimal step but does not reduce the order.

**Why the $\sigma = 1$ exactness does not survive.** At $\sigma = 1$ with constant
$c$, the two spatial samples at level $n$ coincide *exactly* with the two
characteristic footpoints of level $n+1$, at every node simultaneously. With
variable $c$ the characteristics have different slopes at different nodes, so
exactness would require $\Delta t = \Delta x/c(x_j)$ to hold at every $j$ — a set
of simultaneous equations with no solution unless $c$ is constant. The stencil can
lie on the characteristics at one point, never along the whole grid. The exactness
of ★★7 is therefore a property of *constant-velocity* one-dimensional propagation
only.

**Where verification by refinement is delicate.** The order estimate depends on
the reference being much more accurate than the grids being tested. The
3200-node reference differs from a 1600-node solve by $3.8\times10^{-7}$ in the
maximum norm, two orders below the coarse-grid errors reported, so the reference is
adequate here. It is not adequate for an asymptotic-constant claim: the tabulated
error at $N = 800$ ($1.0\times10^{-6}$) is within a factor of three of the
reference's own error, so the last row could be optimistic. Two methodological
lessons follow, and both generalise:

- **Report the reference's accuracy** alongside the errors measured against it, or
  the convergence table is not interpretable;
- **an interpolated reference introduces an interpolation error** of order
  $\Delta x^2$ in the comparison. In this problem that is below the scheme's own
  error, but an interpolant of a rough solution would dominate.

**A caution that this exercise cannot settle.** For a *discontinuous* $c(x)$ the
same node-sampling is not second-order consistent, and the equation must be written
in conservation form, $u_{tt} = (c^2u_x)_x$ with interface conditions, or the order
degrades near the discontinuity. That is a separate experiment, and claiming a
number for it without running it would be exactly the kind of unverified statement
this module avoids.

## ★★★10 — A time-step budget

**(a) The proposal.** With $\Delta x = 10$ m and $c_{\max} = 6000\
\mathrm{m\,s^{-1}}$,

$$\sigma = \frac{c_{\max}\Delta t}{\Delta x} = \frac{6000\times2\times10^{-3}}{10}
= 1.20 .$$

Since $\sigma > 1$, the run is **unstable** — the alternating mode grows by
$\lvert g\rvert = (\lvert 2-4(1.44)\rvert + \sqrt{( -3.76)^2-4})/2
= (3.76 + 3.189)/2 = 3.47$ per step, i.e. a factor $10^{0.54}$ per step. After only
100 steps an initial error of $10^{-12}$ reaches $10^{42}$.

**(b) A usable time step and its cost.** The limit is
$\Delta t_{\max} = \Delta x/c_{\max} = 1.667\times10^{-3}$ s, and for accuracy one
takes about half that: $\Delta t = 8.333\times10^{-4}$ s at $\sigma = 0.5$. Relative
to the proposed 2 ms, the number of steps increases by a factor
$2\times10^{-3}/8.333\times10^{-4} = 2.4$. So the cost penalty is 2.4 times the run
time — modest, and far cheaper than an unstable run that has to be diagnosed and
repeated. (There is no stable alternative "fix" at 2 ms: the condition is a
property of the discretisation, not of the hardware.)

**(c) The dispersion requirement.** The wavelength at 40 Hz in a
$6000\ \mathrm{m\,s^{-1}}$ medium is

$$\lambda = \frac{c_{\max}}{f} = \frac{6000}{40} = 150\ \mathrm{m} ,$$

and 8 points per wavelength requires

$$\Delta x = \frac{\lambda}{8} = 18.75\ \mathrm{m} .$$

So the proposed 10 m grid is *finer* than necessary for dispersion accuracy — the
proposal was not saving anything there. Redrawing the budget for
$\Delta x = 18.75$ m:

| Quantity | 10 m grid | 18.75 m grid |
|---|---|---|
| $\Delta x$ | 10 m | 18.75 m |
| Points per wavelength at 40 Hz | 15 | 8 |
| $\Delta t$ at $\sigma = 0.5$ | $8.33\times10^{-4}$ s | $1.562\times10^{-3}$ s |
| $\Delta t$ at $\sigma = 1$ | $1.667\times10^{-3}$ s | $3.125\times10^{-3}$ s |

For a fixed physical duration, the coarser grid needs fewer steps *and* fewer
points per step: the cost per unit time falls as $\Delta x^{-2}$, so moving from 10
to 18.75 m is a factor $(18.75/10)^2 = 3.5$ saving. In three dimensions the saving
is a factor $(18.75/10)^4 = 12.4$, which is the reason dispersion criteria are
taken seriously in production modelling.

**(d) Which constraint binds.** In this example the *dispersion* requirement sets
the grid, and the *CFL* condition then sets the time step once the grid is fixed;
the two are linked because $\Delta t$ scales with $\Delta x$. The binding
constraint is whichever of (i) resolving the shortest wavelength in the model,
(ii) resolving the smallest velocity contrast, or (iii) representing the
high-velocity layer without the largest velocity forcing an uncomfortably small time
step, is most restrictive for the particular model. A high-velocity layer (salt,
basement, ice) is the usual culprit, and the standard mitigations are variable time
steps, subgridding or implicit time integration — all of which trade accuracy or
complexity for the time step. The honest report states which constraint was binding
and how the time step was chosen, since a reader cannot infer it from the grid
spacing alone.
