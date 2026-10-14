# Solutions — 13-02-02 Numerical Modelling of Mantle Convection

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson:
[02 Numerical Modelling](../02-convection-numerical.md).

---

## ★1 — Time step and step count

$$\Delta t = \frac{\mathrm{CFL}\min(\Delta x, \Delta z)}{|u|_{\max}}
= \frac{0.7\times(1/48)}{30}
= \frac{0.7\times0.020833}{30}
= 4.861\times10^{-4} .$$

Note that $\Delta z = 1/48 = 0.020833$ is the smaller spacing (the box is
$2.8284$ long in $x$, so $\Delta x = 2.8284/48 = 0.058925$; with $N_z = 49$
points there are 48 intervals in $z$). Therefore

$$n_{\text{steps}} = \frac{0.5}{4.861\times10^{-4}} = 1028.6
\;\Longrightarrow\; 1029\ \text{steps} .$$

The CFL limit comes from the *vertical* spacing because the grid is equant in
index but not in length: $\Delta z$ is 2.83 times smaller than $\Delta x$.

---

## ★2 — Discrete versus continuum Laplacian eigenvalue

$$-\lambda_{\text{disc}} = -\frac{2(1-\cos\pi\Delta z)}{\Delta z^{2}} .$$

With $\Delta z = 1/48 = 0.0208333$: $\pi\Delta z = 0.0654498$;
$\cos(\pi\Delta z) = 0.9978589$; $1-\cos = 2.14108\times10^{-3}$;
$2(1-\cos) = 4.28216\times10^{-3}$; divided by $\Delta z^{2} =
4.34028\times10^{-4}$:

$$\lambda_{\text{disc}} = 9.86608, \qquad \lambda_{\text{exact}} = \pi^{2} = 9.86960,$$

a relative difference of $-3.57\times10^{-4}$ — the discrete operator has a
slightly *smaller* eigenvalue, meaning it is slightly *softer* than the continuum
one.

**Implication.** A Poisson solve cannot be more accurate than the operator it
represents, so the solution error is of this order (measured as
$1.38\times10^{-4}$ in the lesson's verification, the amplification of the
operator error). Reporting a "solver error" of $10^{-4}$ for a good transform
method is therefore meaningless unless the discretisation error is separated
from it: the right test compares against *discrete* eigenfunctions, not
continuum ones.

---

## ★3 — Modes and the mean-mode normalisation

For $N_x = 49$ real samples, `numpy.fft.rfft` returns $N_x/2 + 1 = 25$ modes: one
real mean (mode 0), 23 complex conjugate pairs, and one real Nyquist mode.

**Why the mean coefficient is $N_x$.** The unnormalised forward transform is a
*sum*, not an average: for $\mathbf{x} = (1,1,\dots,1)$, the mode-0 coefficient is
$\sum_j x_j = N_x = 49$. The inverse transform then divides by $N_x$, recovering
1.0. Every right-hand side, every boundary contribution and every physical
quantity expressed in mode space must therefore carry the same convention — if an
inhomogeneous boundary value of 1.0 is added in mode space as $1.0$ instead of
$N_x$, the interior sees an effective boundary condition $N_x$ times too small.

**What goes wrong.** In the convection code the bottom boundary is
$T = 1$. Mis-scaling it to $1/49$ produces a spreading cold anomaly that drives
the interior towards the *top* boundary temperature: the field relaxes to a
nearly linear profile between $0.02$ and $0$ rather than between $1$ and $0$. The
code still runs, still "conserves" energy, and reports a Nusselt number of 0.017
instead of about 1 — a physically absurd state that looks like a physical result
(boundary layers thinner than the grid) unless the heat balance is checked
against $Nu = 1$ in the conducting limit.

---

## ★★4 — Growth rate at $\Delta t = 0.01$

$$\lambda = \pi^{2} + k_c^{2} = 9.8696 + \frac{\pi^{2}}{2} = 9.8696 + 4.9348
= 14.8044,$$

$$C = \frac{Ra\,k_c^{2}}{\lambda^{2}} = \frac{800\times4.9348}{219.17}
= \frac{3947.8}{219.17} = 18.0127 .$$

$$\text{analytic } \sigma = -\lambda + C = -14.8044 + 18.0127 = +3.2082 .$$

Discrete amplification factor at $\Delta t = 0.01$:

$$\frac{1+\Delta t\,C}{1+\lambda\Delta t}
= \frac{1+0.180127}{1+0.148044} = \frac{1.180127}{1.148044} = 1.027945,$$

$$\sigma_{\text{discrete}} = \frac{\ln(1.027945)}{0.01} = 2.7562 .$$

**Why they differ.** The advection term — which contains the destabilising
coupling $C$ — is treated *explicitly*, so the scheme amplifies by
$1+\Delta t\,C$ rather than $e^{\Delta t C}$, while the diffusion is treated
*implicitly*, so it damps by $1/(1+\lambda\Delta t)$ rather than
$e^{-\lambda\Delta t}$. Both errors are $O(\Delta t)$ and they do not cancel:
here the discrete rate is 14% below the analytic value, and the lesson's measured
sequence (2.3486, 2.8831, 2.9967 at $\Delta t = 0.02$, $0.005$, $0.0025$) tends
to 3.088 at $\Delta t\to0$, i.e. to within 3.7% of 3.2082.

---

## ★★5 — Local logarithmic slopes

$$\text{1000}\to\text{3000}:\;
\frac{\ln(3.103/1.651)}{\ln 3} = \frac{0.6309}{1.0986} = 0.574,$$

$$\text{3000}\to\text{10000}:\;
\frac{\ln(4.741/3.103)}{\ln(10/3)} = \frac{0.4233}{1.2040} = 0.352,$$

$$\text{10000}\to\text{20000}:\;
\frac{\ln(5.862/4.741)}{\ln 2} = \frac{0.2122}{0.6931} = 0.306 .$$

The interval $10^{4}$–$2\times10^{4}$ is closest to the asymptotic $1/3$
(0.306 against 0.333). The $1000\to3000$ interval is nearly twice the asymptotic
value: near onset, the weakly nonlinear term
$Nu-1\propto(Ra-Ra_c)/Ra_c$ adds a contribution that is steep in $Ra$, so the
apparent exponent is inflated. **Fitting one power law across all four points**
gives 0.418, a number that describes the crossover and not the asymptote.

---

## ★★6 — Two residuals, two different statements

The **top-to-bottom** agreement compares two *horizontally averaged boundary
fluxes*, and it is a statement about conservation: the same energy that enters at
the base leaves at the top, once the transient term (which is small at steady
state) is accounted for. Any value near zero says the discretisation of the
advection–diffusion operator is globally conservative.

The **maximum deviation of the flux profile** compares the local
$-\langle\partial_z T\rangle + \langle wT\rangle$ at each depth with the average.
It is a statement about *local* accuracy: inside the boundary layers, where the
gradient is largest and the first-order upwind scheme's numerical diffusion is
strongest, the flux is not constant because the scheme is not solving the
equation exactly there. A 15% local deviation concentrated in a thin layer is
compatible with a 0.5% global balance, because the bad region carries only a
small fraction of the domain.

**What each tells you.** The global number bounds the size of an error that would
corrupt any heat-budget argument; the profile number tells you where the solution
is least trustworthy and, with a grid study, whether refining narrows that region.
Reporting only the first would be complacent; reporting only the second would
understate the model's usefulness. Both are needed.

---

## ★★★7 — A convergence study for the advection order

**Grids.** Four grids with uniform refinement factor 2 in both directions, e.g.
$25\times25$, $49\times49$, $97\times97$, $193\times193$, holding $Ra = 3000$,
the box, the initial condition and $\mathrm{CFL} = 0.7$ fixed.

**Quantity to converge.** The Nusselt number at statistical steady state, with the
same time-averaging window in convective time units on every grid; and, to avoid
the confound of time-averaging noise, also the *steady single-roll* solution at a
moderate $Ra$ where a stationary state exists.

**Order estimate.** Fit $\ln|Nu(\Delta z) - Nu_{\text{ext}}|$ against
$\ln\Delta z$, or use the three-grid formula

$$p = \frac{\ln\left(\frac{Nu_2 - Nu_1}{Nu_3 - Nu_2}\right)}{\ln r}$$

with refinement ratio $r = 2$, iterating with a Richardson extrapolation for
$Nu_{\text{ext}}$.

**What would show first order.** $p\approx1$ with a monotone increase of $Nu$ with
refinement (numerical diffusion is a positive diffusion, so a coarse grid
*under*-predicts the flux). The measured two-grid values in the lesson,
$Nu = 3.103$ at $\Delta z = 0.0208$ and $3.132$ at $0.0156$, are consistent with
first order: the change is 0.9% for a refinement factor of 1.33, i.e. a relative
change of about $0.9\%/33\% = 2.7\%$ per unit relative $\Delta z$ — an error that
would extrapolate to roughly 1% of the converged value. A second-order scheme
would show a change of about $(1.33)^{-2} = 0.56$ times as much.

---

## ★★★8 — The $1/N_x$ interior-cooling bug

**Mechanism.** The temperature equation was advanced with the diffusion operator
treated implicitly in Fourier space. The bottom boundary condition $T = 1$ is
uniform in $x$, so in mode space it is nonzero *only* in the mean mode, and its
coefficient is $N_x$ (the unnormalised forward transform is a sum). The code
added the boundary term as $+1$ instead of $+N_x$: every non-mean mode received a
spurious source at the first interior node, and the mean mode received a source
$N_x$ times too small. The result was an interior that cooled towards the *top*
boundary value and a field that relaxed to a linear profile between
$\approx1/N_x$ and $0$, with the last grid point at the boundary holding the
correct value — a kink of size $1 - 1/N_x$ in one grid cell.

**Diagnostic that revealed it.** Integrating a purely conducting initial state
($T = 1-z$, which is an exact steady solution of the continuous problem) and
measuring the mean-temperature drift per step. For a correct implementation the
drift is round-off; the buggy version dropped the second interior node from
0.984 to 0.142 in a single step at $N_x = 65$, i.e. by almost the whole
temperature range. The diagnostic is fast, exact, and unambiguous: **a good
Poisson/operator implementation preserves an analytic steady state bit for bit**.

**Unit test for the class of bug.** For any transform-based solver, assert that
(a) a constant field maps to a mode-space array whose only nonzero entry is the
mean mode with coefficient $N$; (b) applying the operator to a known
eigenfunction returns the *discrete* eigenvalue expected from the difference
stencil (for a sine basis, the odd extension of $2(1-\cos\pi\Delta z)/
\Delta z^{2}$); and (c) with inhomogeneous Dirichlet data set to a constant and
the source switched off, one time step returns the same constant field to
round-off. Test (c) is the one that catches the boundary-term scaling, because it
exercises the boundary and the operator together.
