# Solutions — 19-08-04 Simulating Mantle Convection

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [04 Simulating Mantle Convection](../04-simulate-mantle-convection.md).

---

## ★1 — The critical Rayleigh number

$\pi^{2} = 9.869604$, $\pi^{4} = 97.409091$, so

$$\mathrm{Ra}_c = \frac{27\times97.409091}{4} = \frac{2630.0455}{4} = 657.5114 .$$

The critical wavenumber is $k_c = \pi/\sqrt{2} = 2.221441$ per layer depth, and the
critical wavelength is

$$\lambda_c = \frac{2\pi}{k_c} = 2\sqrt{2} = 2.828427\ \text{layer depths}.$$

Both are exact. Note the check $\mathrm{Ra}_c = 6.75\pi^{4}$: the factor $6.75$ is
$(3/2)^{3}/(1/2) = 27/4$, which is where the $27$ comes from.

---

## ★2 — The conductive profile

$$T(z) = T_0 + (T_1 - T_0)\frac{z}{d}.$$

It is linear in $z$, and the three-point stencil is **exact** for linear functions
(indeed for all polynomials up to degree $3$): its local truncation error is
$(h^{2}/12)T''''$, which vanishes identically. A linear benchmark therefore tests
that the code can produce a linear profile with the right boundary values — useful,
but it cannot measure an order of accuracy. That is why the demonstration adds
internal heating with a *quartic* contribution, which is the lowest-degree exact
solution that the stencil does not reproduce exactly.

---

## ★3 — A mantle-like Rayleigh number

$$\nu = \eta/\rho = 10^{21}/3300 = 3.03\times10^{17}\ \mathrm{m^{2}s^{-1}},$$

$$\mathrm{Ra} = \frac{\alpha g\Delta T d^{3}}{\kappa\nu}
= \frac{3\times10^{-5}\times9.81\times1000\times(2.9\times10^{6})^{3}}
{10^{-6}\times3.03\times10^{17}} .$$

Numerator: $3\times10^{-5}\times9.81\times1000 = 0.2943$;
$(2.9\times10^{6})^{3} = 2.4389\times10^{19}$; product $= 7.178\times10^{18}$.
Denominator: $3.03\times10^{11}$. So $\mathrm{Ra} = 2.37\times10^{7}$.

**Dominant uncertainty.** The viscosity enters inverted and spans many orders of
magnitude between the lithosphere and the lower mantle; a factor of $10$ in $\eta$
is a factor of $10$ in $\mathrm{Ra}$, whereas $\Delta T$ and $\kappa$ are uncertain
by factors of a few at most. Any statement about a mantle Rayleigh number is
therefore first a statement about the viscosity profile assumed.

---

## ★4 — The unstable band at four times critical

Solve $(\pi^{2}+k^{2})^{3}/k^{2} = 4\times657.5114 = 2630.05$. Testing values:

| $k$ | $(\pi^{2}+k^{2})^{3}/k^{2}$ |
|---:|---:|
| 0.63 | 2729 |
| 0.64 | 2666 |
| **0.65** | **2578** |
| 5.90 | 2562 |
| 5.95 | 2621 |
| **5.97** | **2645** |

So the band is approximately $k \in [0.64,\ 5.96]$. In wavelengths,
$\lambda = 2\pi/k$ gives $\lambda \in [1.05,\ 9.82]$ layer depths: the simulation
must represent cells from about one to about ten layer depths wide. At
$10\,\mathrm{Ra}_c$ the demonstration measures $k \in [0.39,\ 8.11]$, i.e.
$\lambda \in [0.77,\ 16]$ — the band widens by about a factor of $20$ in width.

---

## ★5 — Growth rate at Ra = 5000

Box of aspect ratio $2\sqrt{2}$, so the fundamental horizontal wavenumber is
$k_x = 2\pi/L_x = 2\pi/2.8284 = 2.2214$ ✓ (the critical one), and the vertical mode
is $\sin(\pi z)$ so $k_z = \pi$. Then

$$\lambda = k_x^{2} + k_z^{2} = 4.935 + 9.870 = 14.805,$$

$$\sigma = -\lambda + k_x\sqrt{\mathrm{Ra}/\lambda}
= -14.805 + 2.2214\sqrt{5000/14.805}
= -14.805 + 2.2214\times18.377 = -14.805 + 40.823 = 26.02 .$$

The e-folding time is $1/\sigma = 0.0384$ diffusion times: the perturbation grows by
$e$ every $3.8$ per cent of a diffusion time, and by $e^{10} = 22026$ in one
diffusion time. **A convection run is in the nonlinear regime very quickly**, which
is why a short run can look converged while its mean state is still adjusting.

---

## ★6 — Resolution of the thermal boundary layer

A boundary layer of $0.01$ layer depths covered by four points needs
$\Delta z = 0.01/4 = 0.0025$, i.e. $N_z = 400$. For a $10^{3}$ horizontal mesh
($1000\times1000$ in the horizontal directions) the node count is
$1000\times1000\times400 = 4\times10^{8}$, and with seven field arrays at eight bytes
that is $4\times10^{8}\times56 = 2.2\times10^{10}$ bytes, about $22$ GB per field
pass — before any consideration of the many time steps needed to reach a
statistically steady state. **The boundary layer, not the interior, sets the cost,
and it is why geodynamics is a supercomputing discipline.**

---

## ★7 — A defensible Nusselt number at Ra = 10^5

**Grids.** A resolution ladder in *both* directions, for example
$96\times48$, $192\times96$, $384\times192$ (aspect ratio chosen so the box contains
several critical wavelengths), with the boundary layer covered by at least four
points at the finest resolution.

**Run length.** Several diffusion times after the initial transient, with the
*inspection* of $\mathrm{Nu}(t)$ used to decide when the statistically steady state
begins. Nusselt numbers are then averaged over a window of at least one diffusion
time and reported with the standard deviation of that average.

**Convergence criterion.** The Richardson-extrapolated $\mathrm{Nu}$ changes by less
than the stated tolerance between the two finest grids, and the observed order from
the three grids is consistent (a clean $O(h^{2})$ for a second-order scheme). Report
$\mathrm{Nu}$ with the grid, the average, the window and the estimated discretisation
error ([19-07-02](../../07-verification-validation-uncertainty/02-solution-verification.md)).

**Failure mode.** If the three grids give $\mathrm{Nu}$ values that do not converge
at any consistent rate, the boundary layer is not resolved at any of them and the
sequence is measuring the grid, not the flow. The response is to refine until the
rate appears, not to average the three values and quote the mean as a result with an
"uncertainty" that is really a grid artefact.

---

## ★8 — Invariants

**What $\max\lvert\theta\rvert \le 1$ encodes.** $\theta$ is the deviation of the
temperature from the conduction profile, whose endpoints are $1$ (bottom) and $0$
(top). The physical solution obeys $0 \le T \le 1$ — the temperature equation has a
maximum principle, so no interior point can exceed the boundary extremes in the
absence of internal heating. Therefore $\lvert\theta\rvert \le 1$, with equality only
in a perfectly mixed limit. A growing violation means the discretisation is
producing values the continuous equation cannot, i.e. the run is diverging from the
physics; it is the earliest and cheapest signal of an under-resolved run, and it
costs nothing to monitor.

**A second invariant for horizontal under-resolution.** Total energy (or the mean
temperature of the interior) must be conserved to the accuracy of the time
integration, since the boundaries are fixed: monitor
$\langle T\rangle - \langle T\rangle_{\text{initial}}$ and require it to stay below
a stated bound. A horizontal-grid-scale instability typically pumps energy into the
smallest resolved scales first, so a complementary diagnostic is the fraction of
kinetic energy in the highest horizontal wavenumber band: a smooth, resolved flow
keeps that fraction small and decaying, while an under-resolved run shows it growing
towards the grid scale. Monitoring both — a pointwise physical bound and a
spectral-scale diagnostic — catches failures that either one alone can miss.
