# Solutions — 08-05-03 EM Forward Modelling: Integral Equation, FD, FE Methods

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [03 EM Forward Modelling](../03-em-modelling.md).

---

## ★1 — Wavenumbers at 100 Hz

$\omega=2\pi f=628.3185\ \mathrm{rad\,s^{-1}}$,
$\omega\mu_0=7.8957\times10^{-4}\ \mathrm{H\,m^{-1}\,s^{-1}}$ (numerically the
same as $\mathrm{\Omega\,m^{-1}}$ in SI), so
$\omega\mu_0\sigma$ is in $\mathrm{m^{-2}}$:

| $\sigma$ (S/m) | $k^2=i\omega\mu_0\sigma$ (m⁻²) | $u=\sqrt{\lambda^2+k^2}$ (m⁻¹) |
|---|---|---|
| 0.01 | $i\,7.8957\times10^{-6}$ | $0.0250005+0.0001579i$ |
| 0.002 | $i\,1.5791\times10^{-6}$ | $0.0250000+0.0000316i$ |
| 0.05 | $i\,3.9478\times10^{-5}$ | $0.0250125+0.0007892i$ |

**Units:** $\lambda$ and $u$ are $\mathrm{m^{-1}}$ (inverse length); $k$ is
$\mathrm{m^{-1}}$; $k^2$ is $\mathrm{m^{-2}}$. Note that at this small
$\lambda=0.025$ and these low conductivities, $u\approx\lambda$ to five digits:
the vertical wavenumber is dominated by the geometry, not the diffusion. That is
exactly the regime in which the response is nearly that of a halfspace.

---

## ★2 — One recursion step

$$q_j=u_j\frac{q_{j+1}+u_j\tanh\left(u_jh_j\right)}
{u_j+q_{j+1}\tanh\left(u_jh_j\right)}.$$

With $u_j=0.025+0.00016i$, $u_jh_j=(0.025+0.00016i)\times60
=1.5+0.0096i$, so
$\tanh(u_jh_j)=0.90515+0.00034i$ (computed). Then

$$q_{j+1}+u_j\tanh=0.025+6.9\times10^{-4}i+\left(0.025+0.00016i\right)
\left(0.90515+0.00034i\right).$$

The product is
$0.022629+0.0000085i+0.000145i\approx0.022629+0.000153i$, so the numerator is
$0.047629+0.000843i$ and the denominator is
$0.025+0.00016i+0.022629+0.000153i=0.047629+0.000313i$. The ratio is
$1.000+i\,0.01113$, and multiplying by $u_j$ gives

$$q_j\approx0.025000+0.000138i\ \mathrm{m^{-1}},$$

matching the lesson's worked example to its printed digits.

---

## ★3 — From $R$ back to $q$

$R=(\lambda-q)/(\lambda+q)$ inverts to $q=\lambda(1-R)/(1+R)$. With
$\lambda=0.025$ and $R=-1.8086\times10^{-5}-2.7626\times10^{-3}i$:

$$1-R=1.000018086+0.0027626i,\qquad
1+R=0.999981914-0.0027626i,$$

$$\frac{1-R}{1+R}=1.0000362+0.0055251i
\quad\Longrightarrow\quad
q=0.025\left(1.0000362+0.0055251i\right)
=0.0250009+0.0001381i,$$

which is the $q_1$ of the worked example ($0.0250005+0.0001381i$) to five
significant figures. The round trip $q\to R\to q$ is a check worth automating: it
costs one line and catches a mistake in the sign of the reflection convention,
which otherwise appears only as a wrong sign of the in-phase response at high
induction number.

---

## ★4 — The matched-layer identity

Set $q_{j+1}=u_j$ in the recursion:

$$q_j=u_j\frac{u_j+u_j t}{u_j+u_j t}=u_j\qquad\text{for any }t=\tanh(u_jh_j).$$

The identity is exact for every thickness, including $h_j\to0$ and
$h_j\to\infty$.

**Why it catches what the halfspace test misses.** The homogeneous-halfspace test
uses $N=1$: the recursion loop never executes, so an error *inside* the loop —
for example transposing $u_j$ and $q_{j+1}$ in the denominator — is invisible. The
matched-layer test executes the loop with a known answer for every thickness, so
it exercises exactly the code the halfspace test skips. The direct
interface-elimination test is stronger still, but it is an independent
implementation and cannot catch a bug *shared* by both; the matched-layer test is
the one that has an independent *answer*.

---

## ★5 — Finite-element matrices for linear elements

On a uniform mesh with $h$ the spacing, a hat function is $1-|z-z_i|/h$ locally,
so $\phi_i'=\pm1/h$ on its two elements. Then

$$K_{ij}=\int\phi_i'\phi_j'\,\mathrm{d}z
=\frac{1}{h}\begin{pmatrix}1&-1\\-1&1\end{pmatrix}
\quad\text{(element)}, \qquad
M_{ij}=\int\phi_i\phi_j\,\mathrm{d}z
=\frac{h}{6}\begin{pmatrix}2&1\\1&2\end{pmatrix}.$$

Assembling $K+\kappa^2M$ gives, for an interior node,
$\left(\frac{2}{h}+\frac{2\kappa^2h}{3}\right)u_i
+\left(-\frac{1}{h}+\frac{\kappa^2h}{6}\right)\left(u_{i-1}+u_{i+1}\right)=0$,
i.e. a tridiagonal matrix with constant coefficients under uniform meshing. The
Dirichlet value at $z=1$ enters only the last right-hand-side entry,
$-\left(-1/h+\kappa^2h/6\right)$. Dividing by $h$ recovers

$$-\frac{u_{i+1}-2u_i+u_{i-1}}{h^2}
+\kappa^2\left[u_i+\frac{h^2}{6}u''_i\right]=0,$$

which shows the FEM is *not* the same scheme as the finite difference: it solves a
modified equation in which the reaction term is weighted by
$(1+h^2\kappa^2/6)$ to leading order. Both are second order, which is why their
errors are so similar in the lesson's table — and why the similarity should not be
read as an identity.

---

## ★6 — Convergence ratio

$$\text{ratio}=\frac{9.181\times10^{-4}}{2.296\times10^{-4}}=3.999.$$

A ratio of about $4$ on halving $h$ means the error scales as $h^2$: second order.
If the next refinement gave, say, $3.0$ instead of $4.0$, the likely causes are
(in decreasing order of probability):

1. the mesh has left the asymptotic regime in another variable (here the time
   step, or, in a layered solver, the $\lambda$ range) and that other error now
   dominates;
2. the solution has a singularity or a boundary layer that the uniform mesh is
   resolving at only first order;
3. a bug that happens to be second order at coarse meshes.

The diagnostic is to refine the *other* error source alone (e.g. fix the mesh and
halve the time step, as the lesson does at $\lambda=0.1$) and see whether the
ratio returns to $4$. A convergence table that mixes two refinements cannot
attribute the error to either.

---

## ★7 — Resolution check for a 3-D FEM model

**Quantity to monitor:** the response at a fixed receiver, decomposed into
in-phase and quadrature, for a fixed frequency, plus a second quantity that is
sensitive to the direction in question — for instance the total current density
integrated across a plane normal to that direction.

**Refinement:** refine anisotropically — halve the node spacing in the $x$
direction only, keeping the others fixed, and repeat with the $y$ and $z$
directions. Track the change in the monitored quantities against the total number
of unknowns.

**Pattern that indicates a single-direction failure:** the responses change by
much more under the $x$ refinement than under the others, while the $y$ and $z$
refinements produce changes at the level of the solver tolerance. A global
resolution problem would show comparable changes under every refinement. The
remedy for a single-direction failure is not a globally finer mesh but an
anisotropic one (or a coordinate system aligned with the structure), which is
usually an order of magnitude cheaper.

**What makes this acceptable as a check:** it is quantitative (changes are
reported), directionally diagnostic, and it terminates — the refinement stops
when the change falls below the noise level of the intended comparison, which
should itself be stated.

---

## ★8 — Born validity for a larger-conductance target

**Experiment.** Rebuild the lesson's test with the layer conductance multiplied by
ten (e.g. $\sigma_{\text{layer}}$ from $0.011$ to $2\ \mathrm{S\,m^{-1}}$, keeping
the thickness and depth), compute the exact layered response for each contrast,
divide the response difference by the contrast, normalise at the smallest
contrast, and plot the ratio against contrast. The *only* thing that changes with
respect to the lesson is the target's conductance.

**Prediction: the linear regime will be narrower.** The Born approximation
neglects the field that the induced currents produce inside the anomaly itself.
That self-field is proportional to the anomalous current density integrated over
the anomaly — that is, to the anomaly's conductance — and it grows with the
induction number $\Delta\sigma\,\mu_0\omega L^2$ of the target. So a target with
ten times the conductance reaches a given fractional self-field at roughly a tenth
of the contrast. This reason does not depend on any number in the lesson: it is
the statement that the expansion parameter is the scattered field, and the
scattered field scales with conductance, not with the contrast ratio alone.

**Secondary prediction:** the shape of the curve will remain monotone and nearly
linear in contrast for small contrasts — the *criterion* moves, the *form* of the
failure does not.
