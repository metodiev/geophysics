# Solutions — 19-02-03 Boundary Conditions: Dirichlet, Neumann, Absorbing, PML

> **Read after attempting the exercises.** Demonstration values are quoted where
> they apply.

Lesson: [03 Boundary Conditions](../03-fd-boundary-conditions.md).

---

## ★1 — Two physical boundaries

**Pressure release (Dirichlet on pressure).** $p = 0$; the reflected pressure
has the opposite sign: $R = -1$. This is the sea surface in marine seismics.

**Rigid / free surface (Neumann).** Normal velocity zero,
$\partial p/\partial n = 0$; the reflected pressure has the same sign:
$R = +1$. This is the free surface of a solid Earth (the air is
negligible), with the "free" referring to the absence of traction.

Both are measured in the demonstration at $h = 1$ m and $0.5$ m to
$2\times10^{-5}$: $-0.99998028$ and $+0.99998028$.

---

## ★2 — Ghost node

At the left boundary, ${x_{-1} = x_0 - h}$ is fictitious. Centred differencing of
the Neumann condition at the boundary gives

$$\frac{u_{1} - u_{-1}}{2h} = q \qquad\Longrightarrow\qquad u_{-1} = u_1 - 2hq.$$

Substituting into the second-derivative operator at the boundary node,

$$\frac{u_{-1} - 2u_0 + u_1}{h^{2}} = f_0
\qquad\Longrightarrow\qquad
\frac{2(u_0 - u_1)}{h^{2}} = f_0 - \frac{2q}{h}.$$

For $q = 0$ this reduces to $2(u_0-u_1)/h^{2} = f_0$: a symmetric, second-order
boundary row.

---

## ★3 — Measured orders

Two-point one-sided: first order (measured $0.9939, 0.9970, 0.9985, 0.9992$).
Ghost node: second order (measured $2.0003, 2.0001, 2.0000, 2.0000$). At the
finest grid the one-sided error is $3.853\times10^{-3}$ against
$2.008\times10^{-6}$ for the ghost node: a factor $1919$.

---

## ★4 — Extrapolating the one-way reflection

The residual reflection is second order, so halving $h$ quarters it:

$$R(0.125) = \frac{8.64\times10^{-8}}{4} = 2.16\times10^{-8},
\qquad 20\log_{10}(2.16\times10^{-8}) = -153.3\ \mathrm{dB}.$$

The measured ratios in the demonstration ($4.0047$, $4.0016$, $4.0002$) confirm
the factor-of-four law.

---

## ★5 — The sponge optimum

**Optimum** in the scan: 40 cells with $\sigma_{\max} = 0.5$, where
$\lvert R\rvert = 0.6054$ — but note that the *global* best point of the full
scan is 80 cells with $\sigma_{\max} = 0.2$ ($0.4016$), and within the 40-cell
row the minimum is at $\sigma_{\max}=0.5$.

**Evidence of non-monotonicity:** within 40 cells the sequence is $0.8652$,
$0.6494$, $0.6054$, $0.6468$ — the reflection falls from $\sigma = 0.05$ to
$0.5$ and *rises again* at $\sigma = 1.0$. The same pattern appears within 80
cells: $0.5788, 0.4016, 0.4810, 0.5399$.

**Dimensionless group:** the wave spends $L_{\text{sp}}/c$ in the layer, so the
damping per crossing is $\sigma_{\max}L_{\text{sp}}/c$; the optimum is at that
group of order a few, and a stronger damping makes the entry ramp itself
reflective because the impedance changes by more than the wave can follow
adiabatically.

---

## ★6 — Physical versus numerical conditions in 2-D

**Physical:** the free surface ($R = +1$). **Numerical:** the absorbing edges
(and any sponge layers).

**Free surface — measurement:** place a source and a receiver, let the direct
wave hit the surface, and measure the polarity and amplitude of the reflected
arrival relative to the incident one; $+1$ means the implementation is correct.
**Absorbing edge — measurement:** send a wave at the edge at normal incidence,
record the field on a line in front of it, and compute the residual reflection as
the ratio of the returned to the outgoing amplitude; repeat with the wave
travelling parallel to the edge to check for grazing-incidence leakage.
**Corner:** the same test directed at the corner, since a one-dimensional
condition applied to each edge independently does not guarantee that the corner
is transparent — the classical failure of edge-only conditions.

---

## ★7 — A boundary-condition test suite

**(a) Free surface.** Geometry: a 1-D or narrow 2-D strip, a source at
$z = 200$ m, a receiver at $z = 300$ m. Observable: the surface-reflected
amplitude relative to the direct arrival, and its polarity. Acceptance:
$R = +1.00 \pm 0.01$ at $\mathrm{PPW}\ge10$. A **sign error** shows up
immediately as $-1$ — this is the experiment that catches it, and no interior
refinement study would.

**(b) Absorbing edge, normal and oblique.** Geometry: a homogeneous 2-D grid,
a point source at the centre of mass of the domain, receivers on a line
perpendicular to the edge. Observable: the amplitude arriving back after the
outgoing wave hits the edge. Acceptance: below $-40$ dB at normal incidence and
below $-30$ dB at $45^{\circ}$ for the chosen absorber (state the numbers with
the incidence angle).

**(c) Corners.** Geometry: the same grid, with the source near a corner.
Observable: the residual reflection measured along the diagonal from the source
to the corner. Acceptance: no arrival above the numerical noise of the absorber,
and specifically no artefact at $45^{\circ}$ from a one-dimensional condition
applied independently to the two edges.

---

## ★8 — Why a PML does better, and what it costs

**The mechanism.** A sponge adds *loss* to the same wave operator, so the
reflection is produced by the impedance mismatch between the damped and undamped
regions; that mismatch is set by the *variation per wavelength* of the damping,
which is why the reflection falls algebraically with the width (measured here as
roughly $1/W$). A PML instead *continues the wave analytically into a complex
coordinate*: it replaces $x$ by $x + \frac1{\mathrm i\omega}\sigma(x)$, which
makes the outgoing wave decay exponentially while leaving the phase and the
impedance unchanged when the stretching is smooth. The reflection is then
produced only by the *discretisation* of the stretch profile, so it falls
exponentially with layer thickness at fixed profile shape.

**Two PML-specific failure modes.** (i) *Grazing incidence and evanescent modes.*
A PML is derived for propagating waves at moderate angles; at grazing incidence
the stretched profiles of adjacent edges overlap and generate a growing
(late-time) instability in some formulations, which a sponge does not have.
(ii) *Anisotropic or heterogeneous media.* The stretch must be applied in the
correct material coordinates to remain matched; a PML applied along the grid axes
in a strongly anisotropic medium can reflect at the internal material contrasts
it was not designed for. Both are diagnosed the same way as the sponge: measure
the residual reflection on the actual geometry, and measure it late in time.
