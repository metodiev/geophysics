# Solutions — 13-05-01 Finite Element and Finite Volume Methods in Geodynamics

> **Read after attempting the exercises.** Numbers were computed, not estimated;
> where a problem admits more than one defensible answer it is said so.

Lesson: [01 Finite Element and Finite Volume Methods](../01-finite-element-geodynamics.md).

---

## ★1 — Element stiffness

$$k_e = \frac{1}{0.1}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
= \begin{pmatrix}10&-10\\-10&10\end{pmatrix}\ \mathrm{N\,m^{-1}}.$$

Row sums: $10 + (-10) = 0$ for both rows. **Physically:** a rigid-body translation
$u = c$ on both nodes must produce no strain energy and no nodal force, and
translations are the null space of the strain operator.

---

## ★2 — Cell Péclet number and numerical diffusivity

(a) $Pe_h = |u|h/D = 0.1\times0.01/2\times10^{-3} = 0.5$.

(b) $D_{\text{num}} = |u|h/2 = 0.1\times0.01/2 = 5.0\times10^{-4}$ m²/s.

$D_{\text{eff}} = D + D_{\text{num}} = 2.5\times10^{-3}$ m²/s, so
$D_{\text{eff}}/D = 1.25$: the upwind scheme conducts heat 25% too fast here.
Because $Pe_h = 0.5 < 2$ the central scheme is monotone and preferable.

---

## ★3 — Decay of the inf-sup constant

$$\frac{\beta_h(4)}{\beta_h(12)} = \frac{0.191180}{0.0746240} = 2.562,
\qquad \frac{h_4}{h_{12}} = \frac{0.25}{0.083333} = 3.000 .$$

The constant fell by 2.56 while the mesh coarsened by 3, so
$\beta_h \sim h^{0.86}$ (the demonstration's fit) — **not bounded away from
zero**. The pair fails the inf-sup condition in the limit even though each mesh
gives an invertible system.

---

## ★4 — Deriving the $Pe_h = 2$ threshold

Write the interior equation for the central scheme in the form
"coefficient of $T_{i}$ times $T_i$ equals a combination of neighbours". With
$u > 0$, the face fluxes are
$F_{i+1/2} = u(T_i+T_{i+1})/2 - D(T_{i+1}-T_i)/h$ and
$F_{i-1/2} = u(T_{i-1}+T_i)/2 - D(T_i-T_{i-1})/h$; the steady balance
$(F_{i+1/2}-F_{i-1/2})/h = 0$ gives

$$\left(2\frac{D}{h^2}\right)T_i
+ \left(\frac{u}{2h} - \frac{D}{h^2}\right)T_{i+1}
+ \left(-\frac{u}{2h} - \frac{D}{h^2}\right)T_{i-1} = 0 .$$

Rearranging for $T_i$: the coefficient of the *upwind* neighbour $T_{i-1}$ is
$\left(\frac{D}{h^2} + \frac{u}{2h}\right)$, which is always positive; the
coefficient of the *downwind* neighbour is
$\left(\frac{D}{h^2} - \frac{u}{2h}\right) = \frac{D}{h^2}\left(1 - \frac{Pe_h}{2}\right)$.
Requiring it to be non-negative gives

$$1 - \frac{Pe_h}{2} \ge 0 \qquad\Longleftrightarrow\qquad Pe_h \le 2 .$$

For $Pe_h > 2$ the discrete matrix is no longer an M-matrix, the maximum
principle fails, and the solution overshoots. This is exactly the threshold the
demonstration measures by bisection: **2.000**.

---

## ★5 — Observed orders

$$p_{32/16} = \frac{\ln(5.661\times10^{-3}/1.419\times10^{-3})}{\ln 2}
= \frac{1.3835}{0.6931} = 1.996, \qquad
p_{64/32} = \frac{\ln(1.419\times10^{-3}/3.549\times10^{-4})}{\ln 2} = 2.000 .$$

**Implies:** the scheme is behaving as a second-order method over this range, and
the observed order is stable from mesh to mesh. **Does not imply:** that the
*absolute* error is small (it is $5.3\times10^{-5}$ in $L^2$ at $n=128$), that
the order holds on other problems, or anything about the accuracy of the
coefficients in a real model. An order is a rate, not a size.

---

## ★6 — Is either elementary scheme usable?

$|u| = 4\ \mathrm{cm/yr} = 0.04/3.1557\times10^{7}
= 1.268\times10^{-9}$ m/s, $h = 2.5\times10^{4}$ m:

$$Pe_h = \frac{|u|h}{\kappa} = \frac{1.268\times10^{-9}\times2.5\times10^{4}}
{1.0\times10^{-6}} = 31.7, \qquad
\frac{D_{\text{num}}}{\kappa} = \frac{|u|h/2}{\kappa} = 15.8 .$$

$Pe_h = 31.7 \gg 2$, so the central scheme is non-monotone at this resolution;
and the upwind scheme's numerical diffusivity is 16 times the physical
diffusivity, which would destroy the thermal structure being computed. **Neither
elementary scheme is acceptable.** The options are refinement until
$Pe_h \lesssim 2$ ($h \lesssim 1.6$ km, a 16-fold refinement in each direction)
or a higher-order advection scheme.

---

## ★7 — A second assembly check

A good choice: verify the *divergence theorem* on the discrete operator. Pick a
smooth velocity field $\boldsymbol{u}$ whose divergence is known analytically
(e.g. $\boldsymbol{u} = (\sin\pi x\cos\pi y,\ \cos\pi x\sin\pi y)$, for which
$\nabla\!\cdot\!\boldsymbol{u} = 0$), interpolate it into the discrete velocity
space, apply $B$, and compare with the interpolated analytic divergence on a
sequence of meshes. That test fails if the element geometry, the quadrature or
the boundary elimination is wrong — none of which the constant-pressure check
touches, because the constant-pressure check tests only that
$\nabla\!\cdot\!\boldsymbol{v}$ integrates to zero against a constant, a
property that survives many bugs. A third check would be the convergence order
of $\|B\boldsymbol{u}_h - \Pi_h(\nabla\!\cdot\!\boldsymbol{u})\|$ under
refinement.

---

## ★8 — Scaling of the stabilisation parameter

**Design.** Fix a problem with a known solution (the analytic Stokes solution, or
a manufactured solution), and measure two things as $h$ is reduced with the
stabilised Q1-Q1 pair: (i) $\beta_h$ and the count of near-zero pressure modes,
and (ii) the $L^2$ error in the pressure field. Repeat for $\varepsilon$ scaled
as $h^2$, $h$ and $h^0$.

**Metric.** The pressure error's convergence order, with the exact solution
known; $\beta_h$ is the constraint, not the objective.

**Predicted outcome from the measured behaviour.** With $\varepsilon$ fixed the
measured $\beta_h$ is 1.004, 0.716 and 0.636 at $n = 4, 8, 12$ — decreasing but
far from zero, so the pair is stable at every mesh; the pressure error, however,
is polluted by the $O(\varepsilon h^2)$ term, so a constant $\varepsilon$ gives a
pressure error that does not converge to the exact answer. The $h^2$ scaling
makes the perturbation vanish at the same rate as the discretisation error,
which is the standard choice; $h$ over-damps and slows convergence without
improving stability. The experiment that would settle it is a three-mesh
pressure-error convergence study for each scaling.

---

## ★9 — Detecting a loss of conservation

**Experiment.** Advect a passive tracer in a divergence-free but spatially
variable velocity field on a closed domain, with the scheme under test, for many
time steps.

**Quantities to monitor.** (i) the total tracer, $\sum_i T_i V_i$; (ii) the
*flux-balance residual* per cell, $R_i = \sum_{\text{faces}}F \cdot n$ evaluated
after the update, $R_i = (T_i^{n+1}-T_i^n)V_i/\Delta t + \sum F$; (iii) the
maximum of $|R_i|$ normalised by the flux scale.

**Tolerance.** The total should drift by less than $10^{-12}$ relative over
$10^{4}$ steps; a conservative scheme written in flux form gives round-off,
while a non-conservative reconstruction drifts by orders of magnitude more (the
demonstration measures 22% in 4000 steps for a deliberately non-conservative
form).

**Why the residual is the stronger test.** A global budget can be preserved by
cancelling errors: matter lost in one region and gained in another cancels in the
sum but is a real error, and it is exactly the error that a non-conservative
limiter produces at a discontinuity. The per-cell residual localises the failure
and therefore diagnoses it.

---

## ★10 — One scheme or two?

**For one scheme.** Simplicity, and the fact that both laws are advection with
the same velocity field, so the same upwind direction and the same limiter logic
apply; consistency between them avoids a spurious differential transport.

**Against.** The two laws have different conservation requirements. Temperature
is not conserved — it is diffused, and its total is set by boundary fluxes — so a
scheme for it should minimise *numerical diffusion* (favouring high-order
central-like schemes). A chemical tracer's total *is* conserved when the
chemistry is absent, so its scheme must be exactly conservative (favouring flux
form with consistent faces). A limiter chosen to keep temperature monotone at a
sharp thermal boundary layer necessarily adds diffusion that a tracer budget will
not forgive, and a tracer scheme that preserves sharp compositional contrasts can
overshoot the temperature.

**Case where they conflict.** A propagating compositional front across a thermal
boundary layer: the tracer needs a monotone, non-oscillatory interface
reconstruction (which is diffusive), while the temperature field needs a
non-diffusive scheme (which oscillates at the front). The defensible resolution
is two schemes, with the choice stated and its effect on each diagnostic
measured — which is exactly the kind of statement the lesson asks for.
