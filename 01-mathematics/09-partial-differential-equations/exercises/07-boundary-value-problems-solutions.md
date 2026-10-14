# Solutions — 01-09-07 Boundary and Initial-Boundary Value Problems

> **Read this after attempting the exercises, not before.**
>
> Worked solutions with the reasoning; numbers were computed rather than estimated.
> Conventions: $\kappa$ a diffusivity; $L = 1$, $\kappa = 1$ where a numerical
> amplification is requested, so eigenvalues are $n^2\pi^2$; $h$ is the Robin
> coefficient (a length$^{-1}$) unless it is explicitly a Biot number.

---

## ★1 — Hadamard's conditions and the backward heat problem

**The three conditions.**

1. **Existence** — at least one solution exists for the given data.
2. **Uniqueness** — at most one solution exists.
3. **Stability (continuous dependence)** — a small change in the data produces a
   small change in the solution, in a stated norm.

**Which fails.** The backward heat problem satisfies (1) and (2) for data that lie
in the range of the semigroup, but fails (3). The failure is quantitative: mode $n$
is amplified by $\mathrm{e}^{\kappa n^2\pi^2t}$ when the problem is run backwards
over time $t$, and that factor is unbounded in $n$.

**The requested number.** With $\kappa = 1$, $L = 1$ and $t = 0.1$:

$$\mathrm{e}^{\,n^2\pi^2t}\Big\rvert_{n=8} = \mathrm{e}^{64\pi^2\times0.1}
= \mathrm{e}^{63.166} = 2.71\times10^{27} .$$

**What that implies.** A data error of $10^{-6}$ produces an error of

$$10^{-6}\times2.71\times10^{27} = 2.7\times10^{21}$$

in the recovered state. The correct reading of that number is not "the method is
slightly unstable" but "the answer is determined entirely by the noise": an error
$10^{27}$ times the data error means the reconstructed initial condition has no
information content at that wavenumber. Note also that the amplification grows as
$n^2$ in the exponent, so *halving* the wavenumber (from 8 to 4) reduces the
amplification from $2.7\times10^{27}$ to $\mathrm{e}^{15.8} = 7.3\times10^{6}$ — a
factor of $4\times10^{20}$. The ill-posedness is therefore extremely
wavenumber-selective, which is why a regularisation that simply cuts off high
wavenumbers can be effective (★★8).

---

## ★2 — Counting conditions from the characteristics

| Problem | Class | Conditions | Where |
|---|---|---|---|
| (a) $\nabla^2V = 0$ on a disc | elliptic | one per boundary point | on the whole circle |
| (b) $u_t = \kappa u_{xx}$ on a rod | parabolic | one initial + one at each end | $u(x,0)$; $x=0$ and $x=L$ for $t>0$ |
| (c) $u_{tt} = c^2u_{xx}$ on a string | hyperbolic | two initial + one per incoming characteristic | $u(x,0)$, $u_t(x,0)$; one at each end |
| (d) $u_t + cu_x = 0$, $c>0$ | first order (no principal part) | one initial, plus one at the *inflow* end | $u(x,0)$; $x = 0$ for $t>0$ |

**The justifications.**

- **(a)** No real characteristics, so no boundary point is privileged: every one
  must carry exactly one condition. Two would over-determine, none would leave the
  solution free to vary (which is why a Neumann problem with data inconsistent with
  the enclosed sources is unsolvable — the compatibility condition of
  [01-09-04](../exercises/04-laplace-poisson-solutions.md) ★★5).
- **(b)** One characteristic family (the degenerate family of lines of constant
  $x$), so one condition arrives from the initial line and one from each spatial
  boundary. Because the equation is not time-reversible, the conditions are imposed
  for $t>0$ only.
- **(c)** Two families, so two Cauchy data are required. At each end, one condition
  per *incoming* characteristic. With a fixed end the incoming and outgoing
  quantities are related by the same condition, which is why a single scalar
  condition suffices at that end; with a *free* end the relation is different but
  still one scalar condition. Contrast a subsonic flow boundary, where one incoming
  and one outgoing characteristic coexist and exactly one scalar condition is
  admissible.
- **(d)** A single characteristic family. One condition on the initial line, and one
  at the inflow end. **No condition at the outflow end**: the characteristic there
  leaves the domain, carrying information out, and imposing a value over-specifies
  the problem — the origin of the spurious reflections that appear in codes that
  treat an outflow boundary like a Dirichlet boundary.

**The single most useful summary.** Count the characteristics that enter the domain
at each piece of the boundary and impose one scalar condition per entering
characteristic; add the Cauchy data on the initial surface according to the order of
the time derivative. Every count in the table follows from that rule, with no
special cases.

---

## ★3 — Energy with a Robin boundary

**The identity.** Let $w$ satisfy $w_t = \kappa w_{xx}$ with
$w_x(0,t) = hw(0,t)$ and $w(L,t) = 0$. Multiply by $w$ and integrate:

$$\frac{1}{2}\frac{d}{dt}\int_0^L w^2\,dx = \kappa\int_0^L w\,w_{xx}\,dx
= \kappa\left[w\,w_x\right]_0^L - \kappa\int_0^L w_x^2\,dx .$$

The upper limit contributes $w(L)w_x(L) = 0$ because $w(L) = 0$; the lower limit
contributes $-w(0)w_x(0) = -h\,w(0)^2$. Hence

$$\boxed{\ \frac{d}{dt}\int_0^L w^2\,dx
= -2\kappa\int_0^L w_x^2\,dx - 2\kappa h\,w(0)^2 \le 0\ }$$

**Consequences.** Both terms are non-positive for $h>0$, so:

- the energy is non-increasing, giving **uniqueness** ($w=0$ initially implies
  $w\equiv0$) and **stability**, exactly as for Dirichlet or Neumann data;
- the decay is **strictly faster** than with the corresponding Neumann condition
  ($h=0$), because the boundary term $-2\kappa hw(0)^2$ is an *additional* sink.
  Physically, heat is being removed through the boundary, whereas an insulated
  boundary removes nothing;
- as $h\to\infty$ the boundary term dominates and forces $w(0)\to0$, i.e. the Robin
  condition becomes Dirichlet — the same limit identified in
  [01-09-05](../exercises/05-separation-of-variables-solutions.md) ★★7.

**Why this matters beyond bookkeeping.** The identity shows that the type of
boundary condition changes the *rate* of decay but not the *fact* of it, for any
$h\ge0$ — provided the term is a sink. If $h<0$ the boundary term becomes a source
and the energy can grow: that is the mathematical signature of a boundary that
supplies heat (a magma body at the base of the model, a chemically reacting
boundary), and it is why the sign of a Robin coefficient must be justified
physically and not merely fitted.

---

## ★4 — Compatibility at the corners

**(a) The failure.** The initial condition gives $u(0,0) = 1$ from the interior
data and $u(0,0) = 0$ from the boundary condition $u(0,t) = 0$. The two data are
inconsistent at the corner, so the problem as stated has no continuous solution:
the function must jump there.

**(b) What the exact solution does.** The solution of the *compatible* version of
the problem — initial data to be understood as a limit — is

$$u(x,t) = \sum_{n=1}^{\infty}b_n\sin\!\left(\frac{n\pi x}{L}\right)
\mathrm{e}^{-\kappa n^2\pi^2t/L^2} + 0 ,$$

whose coefficients are those of the *unit* initial profile with the boundary values
$0$ at both ends: $b_n = 4/(n\pi)$ for odd $n$ (the Fourier series of $u = 1$ on
$(0,L)$ with an odd extension). At $t = 0$ that series is the square wave, which
equals $1$ in the interior and $\tfrac12$ at $x = 0,L$; for any $t>0$ it is smooth
and decays. So:

- at $(0,0)$ the series converges to $\tfrac12$, the average of the two data — the
  standard behaviour of a Fourier series at a jump;
- immediately afterwards the solution is smooth, and the layer near the ends
  adjusts on the timescale $\kappa t/L^2 \sim 1/\pi^2$ for the fundamental, with the
  high modes (coefficients $1/n$) adjusting faster but contributing a
  $1/n$-decaying tail;
- the effect of the incompatibility is therefore **short-lived** for this problem,
  but it is *not* negligible at very short times and it is exactly the situation in
  which a Fourier-series solution converges only in the mean-square sense.

**(c) Two defensible responses.**

1. **Accept the discontinuity and smooth the data.** Replace the initial condition
   by one that satisfies the boundary conditions, for example by tapering the
   profile to zero over a thin layer of thickness $\delta$ near each end. Then the
   series converges uniformly and the problem is a genuine (if slightly different)
   one; the difference is confined to the layer and can be bounded. The
   implementation note: choose the taper so that the *spectral content* above the
   highest resolved mode is below the required tolerance, because a taper that is
   merely continuous but not smooth reintroduces slow convergence.
2. **Reformulate so that the corner is consistent.** Subtract the steady profile
   (here $v\equiv0$, so this changes nothing) or, more usefully, solve for the
   deviation from a *time-dependent* boundary-driven particular solution so that
   the initial condition vanishes at the ends by construction. This is the
   Duhamel/particular-solution route of ★★6 and is the standard treatment when the
   boundary data switch on at $t=0$.

**What is *not* defensible** is to ignore the inconsistency and then report a
numerical solution that shows a large pointwise error at the corner as evidence
about the physics. The corner error is an artefact of inconsistent data, and the
diagnostic is to plot the solution's deviation from the boundary value at $t=0$: if
it is of order the data rather than of order $\Delta x^2$, the data are
incompatible.

---

## ★★5 — Ghost-node Robin condition and its order

**Derivation.** Place the boundary at the last grid node $x_n = L$, and introduce a
ghost node at $x_{n+1} = L+\Delta x$. Discretise the Robin condition with a
*central* difference at $x_n$:

$$\frac{u_{n+1} - u_{n-1}}{2\Delta x} = -h\left(u_n - u_\infty\right)
\qquad\Longrightarrow\qquad
\boxed{\ u_{n+1} = u_{n-1} - 2h\Delta x\left(u_n - u_\infty\right) .}$$

This is the ghost-node value. The interior update at node $n$ then uses exactly the
same three-point stencil as everywhere else:

$$u^{m+1}_n = u^m_n + \frac{\kappa\Delta t}{\Delta x^2}
\left(u^m_{n+1} - 2u^m_n + u^m_{n-1}\right) ,$$

with $u^m_{n+1}$ supplied by the relation above. Because the same stencil is used at
the boundary as in the interior, the local truncation error is $O(\Delta x^2)$
everywhere, and the global solution is second order.

**Verification of the order.** The module's demonstration solves the problem with an
insulated left end and a fixed right end, whose exact solution is
$u = \cos(\pi x/2)\mathrm{e}^{-\pi^2t/4}$, using a mirror ghost node for the Neumann
condition (the same construction with $h=0$):

```text
      N         dx       r     max error   order
     25     0.0400   0.396     4.931e-05        
     50     0.0200   0.399     1.252e-05    1.98
    100     0.0100   0.400     3.139e-06    2.00
    200     0.0050   0.400     7.848e-07    2.00
```

Order 2, confirming that the ghost-node treatment does not degrade the interior
accuracy. The same test should be repeated for the Robin case against a reference
(as the demonstration does for the flux residual), because the *order* of a
derivative boundary condition is where implementations usually fail.

**What a one-sided difference does.** Replacing the central difference by a
one-sided one, $u_{n+1}$ eliminated via
$(u_n - u_{n-1})/\Delta x = -h(u_n - u_\infty)$, makes the boundary relation
$O(\Delta x)$ accurate. The global solution then degrades to first order: refining
the grid no longer halves the error, because the boundary error dominates. The
symptom is characteristic and worth recognising — a convergence study whose order
falls to 1 *and stays at 1* despite refinement means the boundary, not the
interior, is at fault. A second symptom is a systematic offset in the steady state:
a first-order boundary condition converges to a slightly wrong equilibrium, which
is more damaging than a random error because it is invisible in a single run.

**Consistency check to run always.** After the solution relaxes, evaluate the
discrete Robin residual
$-(u_n - u_{n-1})/\Delta x - h(u_n - u_\infty)$ on the computed solution. For the
demonstration's Robin problem with $\mathrm{Bi} = 10$ and $N = 50$, the residual
after relaxation to $t = 8$ is $7.2\times10^{-11}$ while the solution satisfies
$\max\lvert u - u_\infty\rvert = 2.5\times10^{-8}$: both statements are at the
truncation-error level, so the implementation is consistent. A residual that scales
with $h$ rather than with $h^2$ reveals a first-order boundary condition.

---

## ★★6 — Duhamel's principle

**The statement.** For

$$u_t = \kappa u_{xx} + f(x,t), \qquad u(x,0) = 0, \qquad
u(0,t) = u(L,t) = 0 ,$$

the solution is

$$\boxed{\ u(x,t) = \int_0^t\!\!\int_0^L
G(x,\xi;\,t-\tau)\,f(\xi,\tau)\,d\xi\,d\tau\ }$$

where $G$ is the Green's function of the *homogeneous* problem — the solution with
a unit impulse at $(\xi,\tau)$, zero initial data and zero boundary data:

$$G(x,\xi;s) = \frac{2}{L}\sum_{n=1}^{\infty}
\sin\!\left(\frac{n\pi x}{L}\right)\sin\!\left(\frac{n\pi\xi}{L}\right)
\mathrm{e}^{-\kappa n^2\pi^2s/L^2} .$$

Note that the kernel depends only on the *elapsed* time $t-\tau$: the problem is
time-translation invariant, which is exactly what makes the superposition valid.

**Why this is impulse superposition.** A source acting over an interval can be
regarded as a sequence of instantaneous impulses, one per time step, each of
amplitude $f(\xi,\tau)d\tau$. The response to the impulse at time $\tau$ is
$G(x,\xi;t-\tau)f(\xi,\tau)d\tau$, and linearity means the total response is the sum
(here the integral) over all impulses — the same construction as convolving an input
signal with an impulse response in a linear time-invariant filter. The single
sentence form: **the response to a time-dependent source is the convolution of the
source history with the impulse response.**

**Three uses worth knowing.**

- **Non-homogeneous boundary data** can be converted into an equivalent source by
  the method of images or by extending the domain; the principle then applies
  unchanged.
- **Step-function boundary data** (a surface temperature held at a new value from
  $t=0$) integrate to the error-function solution
  $u \propto \mathrm{erfc}\!\left(x/\sqrt{4\kappa t}\right)$, which is the classical
  error-function profile — the single most used solution in heat-conduction practice.
- **Adjoint and data-assimilation methods** are the same principle applied to the
  residual: the adjoint propagates the residual backwards in time, which is
  Duhamel's convolution read in reverse ([01-09-08](../08-weak-solutions.md) §6.2).

---

## ★★7 — Residual reflections of a first-order absorbing boundary

**(a) After ten round trips.** Each reflection multiplies the amplitude by
$r = 10^{-3}$, so after ten the residual amplitude relative to the incident wave is

$$r^{10} = 10^{-30} .$$

**(b) Comparison with a physical interface.** A 10 % impedance contrast gives

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1} = 0.1 ,$$

i.e. $10^{-1}$ — twenty-nine orders of magnitude larger than the residual
reflection after ten round trips. So for that target the first-order condition is
more than adequate over a 100-period simulation.

**(c) The weakest resolvable physical reflection.** What matters is not the
amplitude after many bounces but the level of the *first* spurious reflection
relative to a genuine one, because the two are indistinguishable in principle. With
$r = 10^{-3}$, a boundary artefact of $0.1\%$ of the incident amplitude is generated
on every encounter. A physical reflection is resolvable confidently only if it
exceeds that, say by a factor of a few; so

$$\text{weakest resolvable}\ R \approx 3\times10^{-3} ,$$

corresponding to an impedance contrast of about $0.15\%$ for normal incidence
(since $R\approx\Delta Z/2Z$ for small contrasts). **If the target of the study is a
reflection weaker than about $10^{-3}$, a first-order absorbing condition is not
good enough** and a higher-order one-way condition or a perfectly matched layer is
required. Equivalently, the diagnostic is the ratio of the target reflection
coefficient to the boundary's $r$, and it should be reported rather than left
implicit.

**One caveat on the round-trip arithmetic.** The estimate above treats each
reflection as independent and ignores the transmission loss at internal interfaces
and geometrical spreading; in a heterogeneous model the *effective* number of
encounters with the boundary before the signal drops below the target level is
smaller, and the artefact level correspondingly higher. The correct practical
procedure is to run the model twice with two different boundaries (a fixed one and
the absorbing one) and to difference the results: the residual is the artefact
level, measured rather than estimated. That is the same method the module's
demonstration uses (Section 7.3), where the absorbing boundary leaves
$7.3\times10^{-4}$ against $0.997$ for the fixed one.

---

## ★★8 — A wavenumber cutoff as regularisation

**(a) Choosing $n_c$.** The mode-$n$ amplification is
$\exp(\kappa n^2\pi^2t)$, and the requirement is that the *total* error remain
bounded:

$$\varepsilon\,\mathrm{e}^{\kappa n_c^2\pi^2t} \le 10^{3},
\qquad \varepsilon = 10^{-6} .$$

With $\kappa = 1$, $t = 0.05$:

$$\mathrm{e}^{0.05\pi^2 n_c^2} \le 10^{9}
\qquad\Longrightarrow\qquad
0.05\pi^2 n_c^2 \le 20.723
\qquad\Longrightarrow\qquad
n_c^2 \le \frac{20.723}{0.4935} = 41.99 ,$$

$$n_c = 6.48 .$$

So keeping modes $n\le6$ and discarding the rest bounds the amplification as
required. (Rounding down rather than up is the conservative choice, since the bound
is monotone in $n_c$.)

**(b) What has been given up.** Everything at wavenumbers above $6\pi \approx 19$
per unit length. In physical terms, if $L = 1$ m then the retained features are
longer than about $2L/n_c = 0.31$ m, and any structure finer than that is
*unrecoverable by construction*. The bound in (a) is not a statement that the fine
structure is recovered accurately; it is a statement that the reconstruction's error
is bounded — at $10^{3}$ times the data error, which is still a large number.

**(c) Why this is regularisation, not solution.** The original problem asks for the
state at an earlier time *without qualification*; the modified problem asks for the
state at an earlier time **restricted to a finite-dimensional subspace of smooth
functions**. That is a different problem, with:

- a different (smaller) solution space, hence existence and uniqueness are easy;
- a stability bound, because on that subspace the operator's inverse is bounded
  (★★1's amplification is finite for fixed $n_c$);
- a systematic bias, because the true solution generally has components outside the
  subspace. The error now has *two* parts — the bias from truncation and the
  amplified data noise — and $n_c$ trades one against the other, exactly like the
  regularisation parameter $\alpha$ of [01-09-08](../08-weak-solutions.md) §7.3.

So the honest description is: **the cutoff converts an unanswerable question into an
answerable one whose answer is known to differ from the truth by a controllable
amount.** It does not recover the discarded information, because that information is
not in the data ([01-09-07](../07-boundary-value-problems.md) §6.2 measures that the
noise mode is destroyed by the forward map). Choosing $n_c$ — by the discrepancy
principle, by an L-curve, or from an *a priori* noise estimate — is the modelling
decision, and it must be reported.

---

## ★★★9 — Dirichlet versus Robin: measured decay rates

**Method.** Solve $u_t = u_{xx}$ on $(0,1)$ with both ends either (a) fixed at zero
(Dirichlet–Dirichlet) or (b) Robin with the same $h$ at both ends, from the same
initial condition, and measure the decay of the first mode over a window in which
the first mode dominates. The reference eigenvalue for (a) is $\pi^2 = 9.8696$; for
(b) it is the smallest positive root of the transcendental equation of
[01-09-05](../exercises/05-separation-of-variables-solutions.md) ★★7.

**Predicted eigenvalues.**

| Boundary pair | Lowest eigenvalue | Decay time $1/\lambda_1$ |
|---|---|---|
| Dirichlet–Dirichlet | $\pi^2 = 9.870$ | $0.1013$ |
| Neumann–Dirichlet | $\pi^2/4 = 2.467$ | $0.4053$ |
| Neumann–Neumann | $0$ (constant mode) | $\infty$ |
| Robin–Robin, $h = 10$ | $\mu_1 = 2.5294$ (root of $\tan\mu = h(\mu-h)/(\mu^2+h^2)$), $\lambda_1 = 6.398$ | $0.156$ |
| Robin–Robin, $h\to\infty$ | $\pi^2$ | $0.1013$ |
| Robin–Robin, $h\to0$ | $0$ | $\infty$ |

The Robin–Robin entry was obtained by a bisection on
$\tan\mu = h(\mu-h)/(\mu^2+h^2)$ with the bracket $(\pi/2,\pi)$: no root exists below
$\pi/2$ for $h = 10$ because the right-hand side is negative there while $\tan\mu$ is
positive, so the first mode is the second branch. The general pattern is that the
Robin eigenvalues lie between the Neumann and Dirichlet values of the same problem
and move monotonically towards the Dirichlet ones as $h$ grows: with $h = 10$,
$\mu_1 = 2.529$ lies between the Neumann–Neumann value $\pi\approx3.14$... note it is
*below* $\pi$ but the lowest Neumann eigenvalue is $0$, so the relevant comparison is
with the *next* Neumann value; the Dirichlet–Dirichlet value is $\pi$ and the Robin
value approaches it from below as $h\to\infty$.

**Measurement and comparison.** Running either problem and fitting
$\ln\lvert u(x_1,t)\rvert$ against $t$ over a window where the first mode dominates
returns the *discrete* eigenvalue, which differs from the continuous one by
$O(\Delta x^2)$ — the same $1.1\times10^{-4}$ relative discrepancy measured in the
module's separation-of-variables demonstration for a fixed–fixed slab. Two checks
therefore belong in any such report:

- the fitted rate should match the discrete eigenvalue
  $4\kappa\sin^2(\mu_1\Delta x/2)/\Delta x^2$ more closely than the continuous
  $\kappa\mu_1^2$, and the difference between the two predictions is the
  discretisation error;
- refining $\Delta x$ by two should reduce that discrepancy by four.

**(c) The physical difference.** The Robin boundary *removes* energy (★3), so every
mode decays faster than it does with the corresponding Neumann boundary, and the
constant mode — which exists for Neumann–Neumann and never decays — is destroyed by
the Robin condition. In a model of a land surface, the difference between "insulated"
and "$h$ finite" is the difference between a model with no long-term cooling and one
that relaxes to the atmospheric temperature; in a model of a borehole, it is the
difference between a temperature record that drifts and one that is pinned.

The quantitative summary to carry away: **the *type* of boundary condition changes
the eigenvalues by factors of order unity (here $\pi^2$, $\pi^2/4$, or $0$), while
refining the grid changes them by $O(\Delta x^2)$.** Boundary conditions are a
physics decision; grid refinement is a numerical one. Confusing their magnitudes is
the commonest way to attribute a physics result to a mesh.

**(d) Limits of the comparison.** The two problems differ in more than their
boundaries: the eigenfunctions are different
($\sin(n\pi x)$ against $\cos(\mu_nx)$ with $\mu_n$ from the transcendental
equation), so a *fixed* initial condition excites different mixtures of modes in the
two cases. If the initial condition is not orthogonal to the higher modes, the early
transient is contaminated and the fitted rate is biased; the fit window must
therefore start after the second mode has decayed by a stated factor, e.g. after
$\mathrm{e}^{-(\lambda_2-\lambda_1)t}<10^{-2}$. For the Dirichlet case,
$\lambda_2 = 4\lambda_1$, so that requires $t>1.5/\lambda_1$; for the Robin case with
$h$ small, $\lambda_2/\lambda_1$ can be much closer to 1 and the required window is
far longer. A second limit: the Robin eigenvalue must itself be computed, and its
accuracy propagates directly into the "predicted" column, so the transcendental
root-finder should be converged to well below the grid error before attributing any
discrepancy to the discretisation.

---

## ★★★10 — Design note for a time-lapse inversion

**(a) Which boundary conditions must be identical.** **All of them**, and in
particular:

- the **ground surface** condition (atmospheric temperature or pressure, free
  surface for elastic fields);
- the **lateral and basal** conditions, including any fixed-temperature,
  fixed-flux, or far-field "constant-head" assignment;
- the **initial state** of the first run, because the second run starts from the
  first run's end state in a sequential simulation;
- the **source terms** (injection rates, production history), which are data and must
  be reproduced exactly, including their timing.

The reason is that a boundary condition change is *not* a small perturbation in the
sense of the inversion: a change in a Dirichlet datum or a flux propagates into the
interior everywhere and immediately for an elliptic component, and over the diffusive
timescale for a parabolic one. A boundary change of magnitude comparable to the
time-lapse signal will be absorbed by the inversion into a spurious "rock property
change" with exactly the spatial pattern of the boundary's influence — typically a
broad, deep, smooth anomaly, which is easy to mistake for a real reservoir change.
In practice the requirement is enforced by *sharing* the boundary-condition
configuration between the two runs rather than re-entering it.

**(b) Why not an absorbing boundary at the ground surface.** An absorbing
(one-way/radiation) boundary asserts that nothing enters the domain from outside — it
exists to make an artificial truncation of a much larger domain behave as though the
domain were infinite. The ground surface is a **physical** boundary where energy is
genuinely exchanged with the atmosphere (heat and mass flux; a free surface for
elastic waves that reflects with a definite phase and amplitude). Imposing a
radiation condition there would suppress a real physical interaction, and the model
would then be missing the diurnal/annual thermal wave that drives much of the
near-surface signal. The parallel with [01-09-03](../03-wave-equation.md) §4 is
exact: the free surface reflects, and the reflection is signal, not artefact.

The correct assignments are physical: a Robin (convective) condition for heat
exchange with air, a Dirichlet condition if the surface temperature is measured and
held, a flux condition for a prescribed geothermal gradient at the base, and no-flow
(lateral Neumann) conditions only where the geology justifies them.

**(c) Regularisation, and choosing its parameter.** The time-lapse problem is an
inversion of a *difference* of data for a change of properties; it inherits the
ill-posedness of the underlying diffusive problem (the singular spectrum of
Section 7 of the relevant inversion lecture), amplified because differences of
similar fields are noise-dominated at short wavelengths. I would apply:

- **Tikhonov regularisation on the model change**, $\lVert \Delta d - J\Delta m
  \rVert^2 + \alpha\lVert L\Delta m\rVert^2$, with $L$ a discretised gradient or
  Laplacian so that the prior is "the change is spatially smooth" — a defensible
  physical statement for a reservoir-scale process;
- **a bound on the magnitude** of the change (positivity, or an interval constraint
  from core measurements), since the amplification can otherwise produce
  unphysically large values in unconstrained cells;
- **a choice of $\alpha$ from the data noise**: the discrepancy principle picks
  $\alpha$ so that the residual matches the estimated noise level; the L-curve is
  the standard graphical alternative; cross-validation requires more data than
  time-lapse surveys usually provide. The *value* of $\alpha$ and the method used to
  choose it must be reported, because they determine the resolution (Section 7.3 of
  the weak-solutions lesson: the filter is $\sigma^2/(\sigma^2+\alpha)$).

**(d) A diagnostic for boundary-condition inconsistency.** Compare the two runs
*with no property change at all*: back-propagate the first run's end state with the
second run's boundary configuration and measure the difference from the first run's
own forward continuation. Any non-zero difference is the signature of an
inconsistency, and it can be quantified in the same norm used by the inversion, so
it sets a floor on the detectable change.

A second and cheaper diagnostic: evaluate the discrete boundary-condition residual
(as in ★★5) on the boundary nodes of each run and plot the two time series. Since
the conditions are supposed to be identical, the two residuals should agree to
round-off; a systematic offset of order the truncation error indicates either a
different discretisation of the same condition or a different condition. Both
diagnostics are cheap, both are decisive, and both should be run *before* the
inversion — which is the point of the exercise. The general principle: in any
inversion, an inconsistency between the forward models used to generate and to
interpret the data appears as a structured model artefact, and it is far cheaper to
test for it directly than to recognise it in the recovered model.
