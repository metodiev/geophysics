---
id: 01-08-04
title: "Systems of ODEs, Phase Portraits and Stability"
level: advanced
prereqs: ["01-08-02", "01-07-06"]
estimated_minutes: 90
tags: [ordinary-differential-equations, systems, phase-portrait, stability, eigenvalues]
---

# Systems of ODEs, Phase Portraits and Stability

## Learning objectives

By the end of this lesson you will be able to:

1. **Reduce** an $n$-th order scalar ODE to a first-order system in $n$
   variables, and explain why that is the standard form for both theory and
   computation.
2. **Solve** a linear system $\dot{\mathbf{x}} = A\mathbf{x}$ by eigen-
   decomposition, and write the general solution as a sum of modes with
   timescales $-1/\lambda_i$.
3. **Classify** a plane system completely from its trace $T$ and determinant
   $D$, and say what each class means physically.
4. **Linearise** a non-linear system about a fixed point and decide its
   stability from the Jacobian's eigenvalues, stating exactly where the
   linearisation is and is not trustworthy.
5. **Use** a Lyapunov function to prove global stability when a linearisation
   only gives local information, and give a conserved quantity for a system with
   closed orbits.
6. **Model** a coupled two-box climate system, a coupled-reservoir
   predator–prey analogue, and a bistable feedback with a saddle, and read the
   qualitative behaviour off the phase portrait.

## Prerequisites

- [02 Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) —
  the characteristic equation, which becomes the eigenvalue problem here.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md) —
  eigenvalues, eigenvectors and the diagonal form $\Lambda = S^{-1}AS$.
- [01-05-04 Taylor Series, Linearisation and Small-Angle Approximations](../05-single-variable-calculus/04-taylor-series.md) —
  the multi-variable linearisation that produces the Jacobian.

## 1. Intuition: a system is a picture, not a formula

A scalar ODE gives a curve; a two-dimensional system gives a *picture*. Plot
the state $(x,y)$ as a point and let the equations tell you the velocity at
every point: the result is a vector field whose integral curves are the
solutions. That picture is called a **phase portrait**, and it is the single
most informative object in the theory of ODEs, because it displays *all*
initial conditions at once rather than one solution at a time.

Three examples, each developed below, show why geophysicists care:

| System | Portrait | Geophysical reading |
|---|---|---|
| Coupled two-box climate | stable node | a perturbation decays on two timescales |
| Predator–prey (conservative) | centre, closed orbits | two coupled reservoirs trade a conserved quantity forever |
| Ice-albedo-like feedback | saddle | bistability: the fate of a perturbation depends on which side of a separatrix it starts |

The mathematics also delivers a payoff that is unique to two dimensions: in the
plane, a bounded trajectory that never settles down must approach a closed
orbit. There is no chaotic motion in a plane, and the shape of that statement is
what makes planar portraits readable.

## 2. Definitions and the classification theorem

### 2.1 Reduction to first-order form

Any scalar ODE of order $n$ can be written as a system of $n$ first-order
equations by introducing the lower derivatives as new variables. For
$x'' + 2\zeta\omega_0x' + \omega_0^2x = 0$, set $x_1 = x$ and $x_2 = x'$. Then

$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix}
= \begin{pmatrix}0 & 1\\ -\omega_0^2 & -2\zeta\omega_0\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix}.$$

The eigenvalues of that matrix are the roots of the characteristic equation of
[02](./02-second-order-linear.md), which is why the two lessons are the same
lesson. **This is the standard form for computation**: every general-purpose
ODE solver expects $\dot{\mathbf{x}} = \mathbf{f}(t,\mathbf{x})$, and every
numerical method in
[07 Stiff Systems](./07-stiff-systems.md) is stated that way.

### 2.2 Linear systems

For $\dot{\mathbf{x}} = A\mathbf{x}$ with $\mathbf{x}\in\mathbb{R}^n$ and $A$
constant, the general solution is a superposition of **modes**:

$$\mathbf{x}(t) = \sum_{i=1}^{n} c_i\,e^{\lambda_it}\mathbf{v}_i,$$

where $\lambda_i$ and $\mathbf{v}_i$ are eigenvalues and eigenvectors of $A$ and
the $c_i$ are fixed by $\mathbf{x}(0)$. Each mode has a **timescale**
$\tau_i = -1/\operatorname{Re}\lambda_i$ when $\operatorname{Re}\lambda_i<0$: the
time for that mode to decay by a factor $e$.

In the plane, write

$$A = \begin{pmatrix}a&b\\c&d\end{pmatrix}, \qquad
T = \operatorname{tr}A = a+d, \qquad D = \det A = ad-bc,$$

and note the two identities that make the classification possible:

$$\lambda_{1,2} = \tfrac12\left(T \pm \sqrt{T^2-4D}\right), \qquad
\lambda_1+\lambda_2 = T, \qquad \lambda_1\lambda_2 = D .$$

The pair $(T,D)$ therefore determines the eigenvalues completely, and the
following classification is exhaustive.

| Condition | Eigenvalues | Portrait | Stability |
|---|---|---|---|
| $D<0$ | real, opposite signs | **saddle** | unstable |
| $D>0$, $T^2>4D$, $T<0$ | real, both negative | **stable node** | asymptotically stable |
| $D>0$, $T^2>4D$, $T>0$ | real, both positive | **unstable node** | unstable |
| $D>0$, $T^2<4D$, $T<0$ | complex, negative real part | **stable spiral** | asymptotically stable |
| $D>0$, $T^2<4D$, $T>0$ | complex, positive real part | **unstable spiral** | unstable |
| $D>0$, $T=0$ | purely imaginary | **centre** | stable, not asymptotically |
| $D>0$, $T^2=4D$, $T<0$ | one repeated negative root | **degenerate node** | asymptotically stable |
| $D=0$ | at least one zero root | degenerate | linear test inconclusive |

### 2.3 Stability, precisely

The **origin is stable** if trajectories that start close stay close:
$\|\mathbf{x}(0)\|<\delta \Rightarrow \|\mathbf{x}(t)\|<\varepsilon$ for all
$t\ge 0$. It is **asymptotically stable** if in addition $\mathbf{x}(t)\to
\mathbf{0}$. It is **unstable** if it is not stable. A **centre** is stable but
not asymptotically stable — this distinction matters and is exactly the
predator–prey case below.

An equilibrium is **hyperbolic** if no eigenvalue has zero real part. The
**Hartman–Grobman theorem** states that near a hyperbolic equilibrium a
non-linear system is topologically equivalent to its linearisation: the
classification by $(T,D)$ carries over, it is not merely a linear
approximation. **Non-hyperbolic equilibria are where linearisation fails**, and
the predator–prey centre is the standard example: its linearisation is a centre
and the true system is also a centre, but that agreement is a coincidence of
symmetry, not a theorem, and a different non-linear perturbation of the same
linear system gives a spiral.

## 3. Derivations, step by step

### 3.1 The five portraits, computed

The demonstration builds each of the following matrices, computes $T$, $D$ and
the eigenvalues, and names the result. Reproducing the table by hand is the
best way to make the classification automatic:

| Matrix | $T$ | $D$ | $T^2-4D$ | Eigenvalues | Class |
|---|---|---|---|---|---|
| $\begin{pmatrix}-0.3&0.1\\0.05&-0.2\end{pmatrix}$ | $-0.5$ | $0.055$ | $0.03$ | $-0.163397,\ -0.336603$ | stable node |
| $\begin{pmatrix}-0.1&1\\-1&-0.1\end{pmatrix}$ | $-0.2$ | $1.01$ | $-4$ | $-0.1\pm1.0i$ | stable spiral |
| $\begin{pmatrix}0.2&0.5\\0.5&-0.1\end{pmatrix}$ | $0.1$ | $-0.27$ | $1.09$ | $+0.572015,\ -0.472015$ | saddle |
| $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ | $0$ | $1$ | $-4$ | $\pm1.0i$ | centre |
| $\begin{pmatrix}-0.5&0\\0&-0.5\end{pmatrix}$ | $-1$ | $0.25$ | $0$ | $-0.5,\ -0.5$ | degenerate node |

Two entries deserve comment. The second has $T^2-4D = -4$, far below zero,
which is what makes it a *circular* spiral: a small $|\operatorname{Re}\lambda|$
with a large $|\operatorname{Im}\lambda|$ means many oscillations per e-folding,
i.e. high $Q$. The third is the only one with $D<0$, so it is the only saddle,
and the sign of $D$ alone settles it.

### 3.2 A coupled two-box climate model

Split the climate system into a surface box (temperature $T_1$, heat capacity
$C_1$) and a deep box ($T_2$, $C_2$). The surface loses heat to space through a
feedback $\lambda$ and exchanges heat with the deep box through a coupling
$\gamma$:

$$C_1\dot T_1 = F - \lambda T_1 + \gamma(T_2-T_1), \qquad
C_2\dot T_2 = \gamma(T_1-T_2).$$

Setting $C_1=C_2=1$ for the homogeneous (perturbation) problem gives the matrix
of the demonstration:

$$A = \begin{pmatrix}-(\lambda+\gamma) & \gamma\\ \gamma & -\gamma\end{pmatrix}
= \begin{pmatrix}-2 & 0.8\\ 0.8 & -0.8\end{pmatrix},$$

with $T = -2.8$, $D = 0.96$, $T^2-4D = 4$ and eigenvalues $-0.4$ and $-2.4$.
Both are real and negative, so this is a **stable node**, and the two
relaxation times are

$$\tau_{\text{slow}} = \frac{1}{0.4} = 2.5, \qquad
\tau_{\text{fast}} = \frac{1}{2.4} = 0.4167 .$$

**Read the physics off the eigenvalues.** The fast mode is the surface
equilibrating with the deep ocean; the slow mode is the two boxes jointly
returning to radiative balance. A forcing pulse applied to the surface decays
quickly to a state that is *not* equilibrium and then decays slowly — which is
why a volcanic aerosol perturbation produces both a sharp and a lingering
surface-temperature response. The demonstration integrates $(T_1,T_2)=(1,0)$ to
$t=50$ and obtains $(4.08\times10^{-10},\,8.16\times10^{-10})$, both modes
decayed by a factor of $10^{10}$.

**What the model assumes:** two well-mixed boxes, a linear feedback $\lambda$,
and no transport. Everything that makes climate interesting — a spatially
varying feedback, ocean circulation, ice — is outside it. Its value is that it
shows how a two-timescale response arises from a *coupling*, without any
non-linearity.

### 3.3 A conservative coupling: predator–prey as two coupled reservoirs

The Lotka–Volterra equations

$$\dot x = ax - bxy, \qquad \dot y = -cy + dxy$$

describe a prey $x$ and a predator $y$, with $a$ the prey growth rate, $b$ the
predation rate, $c$ the predator death rate and $d$ the conversion efficiency.
The non-trivial equilibrium has $x^* = c/d$ and $y^* = a/b$; with
$a=1$, $b=0.5$, $c=0.8$, $d=0.4$ both equal 2. The Jacobian there is

$$J = \begin{pmatrix}a - by^* & -bx^*\\ dy^* & -c + dx^*\end{pmatrix}
= \begin{pmatrix}0 & -1\\ 0.8 & 0\end{pmatrix},$$

which has $T=0$, $D=0.8$ and eigenvalues $\pm0.894427i$: a **centre**. The
demonstration confirms that the motion is genuinely periodic, not an artefact
of the linearisation, by tracking the conserved quantity

$$H = dx - c\ln x + by - a\ln y$$

along a numerically integrated orbit (fourth-order Runge–Kutta, step 0.001).
Starting from $H(1,1)=0.9$ the drift over 100 time units is
$-1.5\times10^{-14}$: **the orbits are closed to machine precision**, so the
centre is real.

Two warnings. First, the demonstration deliberately uses RK4 and *not* Euler:
forward Euler on a conservative system spirals outward, and the drift would be
numerical rather than physical. Integrators have qualitative properties, and
choosing one that respects the geometry matters — the same point is made in
[19-numerical-modeling-hpc](../../19-numerical-modeling-hpc/README.md).
Second, the conserved quantity exists only because the model has no
self-limiting term; adding a logistic term for the prey destroys $H$ and turns
the centre into a spiral.

### 3.4 Adding a carrying capacity: the trace becomes a formula

Replace the prey growth with logistic growth:

$$\dot x = ax\left(1-\frac{x}{K}\right) - bxy, \qquad \dot y = -cy + dxy .$$

With $a=1$, $K=3$, $b=0.6$, $c=0.7$, $d=0.5$ the equilibrium is $x^* = c/d =
1.4$, $y^* = (a/b)(1-x^*/K) = 0.888889$, and the Jacobian there is

$$J = \begin{pmatrix}-0.466667 & -0.84\\ 0.444444 & 0\end{pmatrix},$$

with $T = -0.466667$, $D = 0.373333$, $T^2-4D = -1.27556$ and eigenvalues
$-0.233333 \pm 0.564702i$. This is a **stable spiral**: trajectories wind in
towards the equilibrium. The demonstration integrates from $(1,1)$ and records
the distance to the fixed point: $4.151\times10^{-1}$ at $t=0$,
$4.325\times10^{-6}$ at $t=50$, $3.717\times10^{-11}$ at $t=100$, and
$1.394\times10^{-13}$ thereafter, where the residual is integration error.

Now do the algebra instead of trusting the example, because this is where a
superficial reading goes wrong. At the interior equilibrium
$dx^* = c$ so $J_{22} = -c+dx^* = 0$, and $by^* = a(1-x^*/K)$, hence

$$T = J_{11}+J_{22} = a\left(1-\frac{2x^*}{K}\right) - by^*
= a\left(1-\frac{2x^*}{K}\right) - a\left(1-\frac{x^*}{K}\right)
= -\frac{ax^*}{K} = -\frac{ac}{dK} \;<\;0 .$$

**The trace is negative for every positive parameter set.** With a mass-action
(bilinear) predation term and logistic prey the interior equilibrium is
*always* attracting, so no limit cycle can bifurcate from it, regardless of how
large a carrying capacity you choose. The demonstration verifies the closed
form at $K = 3$, $1.5$ and $20$, obtaining $T = -0.466667$, $-0.933333$ and
$-0.070000$ against the predicted values to six decimals.

**Destabilisation requires a different model term.** If the functional response
saturates — the predator cannot eat faster than some maximum — replace $bxy$ by
$bxy/(1+hx)$. The equilibrium then has a non-zero $J_{22}$ contribution and

$$T = x^*\left[-\frac{a}{K} + \frac{b\,h\,y^*}{(1+hx^*)^2}\right],$$

which **can** change sign as $K$ grows. With $a=b=d=1$, $c=0.4$, $h=0.5$ the
demonstration computes $T = +0.000000$ at $K = 3$ and $T = +0.080000$ at
$K = 5$, so the equilibrium loses stability at $K = 3$: a Hopf bifurcation,
and the "paradox of enrichment" in which a richer environment destabilises the
community. **The point is not the ecology; it is that the sign of a trace is a
computed consequence of a model, and a different model term with the same
dimensions gives the opposite answer.** Substituting a plausible-looking term
changes the qualitative conclusion.

**The classification also tells you what the orbit cannot tell you.** A limit
cycle and a slowly converging spiral look similar on a short numerical run. The
discriminator is the sign of $T$: $T<0$ means the equilibrium attracts, so any
nearby closed orbit must be lost; $T>0$ means it repels, which is the necessary
condition for a limit cycle to exist nearby. **The sign of the trace, not the
appearance of the trajectory, decides.**

### 3.5 A saddle, and why bistability is a statement about a line

Take $A = \begin{pmatrix}0.3&0.2\\0.2&-0.1\end{pmatrix}$: $T=0.2$, $D=-0.07$,
eigenvalues $+0.382843$ and $-0.182843$. The unstable eigenvector is
$(0.923880,\ 0.382683)$. The demonstration integrates five different initial
conditions for 20 time units and reports both the endpoint and its direction:

| Start | Endpoint | Direction |
|---|---|---|
| $(+0.01, 0)$ | $(+18.027055,\ +7.466944)$ | $(+0.92388,\ +0.38268)$ |
| $(-0.01, 0)$ | $(-18.027055,\ -7.466944)$ | $(-0.92388,\ -0.38268)$ |
| $(0, +0.01)$ | $(+7.466944,\ +3.093167)$ | $(+0.92387,\ +0.38271)$ |
| $(0, -0.01)$ | $(-7.466944,\ -3.093167)$ | $(-0.92387,\ -0.38271)$ |
| $(+0.01, +0.01)$ | $(+25.493998,\ +10.560111)$ | $(+0.92388,\ +0.38269)$ |

All five directions coincide, up to sign, with the unstable eigenvector. The
stable direction has been annihilated and what survives is the one growing
direction. **A saddle is not merely "unstable": it is an amplifier with a
preferred direction.** Two trajectories that start on opposite sides of the
stable line end up in opposite quadrants, and the stable line (its stable
manifold) is the **separatrix** that separates them. That line is the reason
the phrase "the system tipped over a threshold" is meaningful in a dynamical
model, and it is why thresholds in climate and geodynamics are described by
manifolds rather than by single numbers.

### 3.6 Global stability from a Lyapunov function

A linearisation tells you about a neighbourhood. To prove stability over a
whole domain you need a function that decreases along every trajectory. For the
two-box model, take

$$V = \tfrac12\left(T_1^2+T_2^2\right), \qquad
\dot V = T_1\dot T_1 + T_2\dot T_2 = -\mathbf{T}^{\!\top}Q\,\mathbf{T}, \qquad
Q = \begin{pmatrix}2 & -0.8\\ -0.8 & 0.8\end{pmatrix}.$$

The demonstration computes $\det Q = 0.96 > 0$ and $Q_{11} = 2 > 0$. By the
Sylvester criterion $Q$ is positive definite, so $\dot V<0$ for every non-zero
state: **the origin is globally asymptotically stable**, not merely locally.
The criterion is the $2\times2$ case of the general statement that a symmetric
matrix is positive definite precisely when all its leading principal minors are
positive.

## 4. Physical interpretation

**The trace is the average decay rate; the determinant is the product of the
rates.** $T = \lambda_1+\lambda_2$ and $D = \lambda_1\lambda_2$. So $D>0$ means
the two modes decay or grow *together* (a node or spiral), and $D<0$ means one
decays while the other grows (a saddle). $T$ then decides whether the pair
decays or grows. Every classification rule follows from those two sentences,
and no memorisation is required.

**Eigenvectors are the directions in which the coupling is diagonal.** In the
two-box model the eigenvectors are combinations of surface and deep
temperature, not either alone. Physically: the fast mode is "surface changes,
deep does not", and the slow mode is "both move together". Recognising modes
matters because a forcing that projects onto one mode excites one timescale
only, and because observations that do not resolve the modes cannot separate
the processes.

**Oscillation requires complexity, and complexity requires a rotation.**
$\lambda$ complex means the coupling transfers the state back and forth between
the variables — a restorative rather than a dissipative interaction. In the
predator–prey system the rotation is the abundance cycle; in a coupled
two-reservoir geochemical model it is the back-and-forth of mass between
reservoirs.

**Stability is a property of the equilibrium, not of the system.** A system can
have two stable equilibria and one unstable one, which is what a saddle between
them means. Multistability in geodynamics — an ice-covered and an ice-free
Earth, a stagnant-lid and a mobile-lid mantle — is the same structure: several
attracting states and a separating manifold between them.

**What breaks the classification.** It is only complete for *hyperbolic*
equilibria of *autonomous* systems. A time-dependent forcing (seasonal,
tidal, orbital) makes the system non-autonomous and the fixed point disappears
into a periodic orbit; a non-hyperbolic equilibrium needs the non-linear terms
to decide; and a non-smooth right-hand side (stick–slip friction, a threshold
law) is not covered at all.

## 5. Python demonstration

The companion script is
[`code/systems_of_odes_demo.py`](./code/systems_of_odes_demo.py), standard
library only.

| Section | Claim being tested | Observed result |
|---|---|---|
| 1 | $(T,D)$ classifies the portrait | five matrices classified correctly, including the boundary case $T^2-4D=0$ |
| 2 | The two-box model is a stable node | $\lambda = -0.4,\ -2.4$; $(1,0)\to(4.1\times10^{-10},8.2\times10^{-10})$ at $t=50$ |
| 3 | Lotka–Volterra conserves $H$ | $H(1,1)=0.9$; drift $-1.5\times10^{-14}$ over 100 time units |
| 4 | The logistic version spirals in, and $T = -ac/(dK)$ | closed form matched at $K = 3, 1.5, 20$; distance $4.15\times10^{-1}\to1.39\times10^{-13}$ |
| 4 | A saturating response changes the sign of $T$ | Holling type II: $T = 0.000000$ at $K=3$, $T = +0.080000$ at $K=5$ |
| 5 | A saddle amplifies one direction | all five endpoints lie along $(0.92388,0.38268)$ |
| 6 | A Lyapunov function proves global stability | $\det Q = 0.96>0$, $Q_{11}=2>0$ |

Section 3 is the methodological lesson. Two integrators were available for the
conservative system — Euler and RK4 — and only one of them is admissible.
Rather than asserting that RK4 is better, the script *measures* the drift of
the conserved quantity, which is a property Euler cannot have at any step size.
When a system has a conserved quantity, the first thing to do with a numerical
method is check conservation, not convergence.

> **Breaking exercise.** In Section 4, replace the predation term $bxy$ with
> the saturating form $bxy/(1+hx)$ and predict, before running, whether $T$
> changes sign as $K$ grows, and at what $K$ it does. Compare with the values
> the script prints for $K = 3$ and $K = 5$.

## 6. Exercises

Attempt these closed-book. See
[`exercises/04-systems-of-odes-exercises.md`](./exercises/04-systems-of-odes-exercises.md)
and the worked
[`exercises/04-systems-of-odes-solutions.md`](./exercises/04-systems-of-odes-solutions.md).

## 7. Common mistakes

1. **Sign errors in the determinant.** $D = ad-bc$, not $ad+bc$; getting this
   wrong converts every saddle into a node.
2. **Reading stability off the trace alone.** $T>0$ with $D<0$ is still a
   saddle, and $T=0$ with $D>0$ is not asymptotically stable even though it
   does not grow.
3. **Assuming complex eigenvalues always mean a stable spiral.** Complex with
   $T>0$ is an unstable spiral; the oscillation is growing.
4. **Trusting a linearisation at a non-hyperbolic point.** The predator–prey
   centre has $\operatorname{Re}\lambda = 0$, and the linearisation cannot
   distinguish a centre from a very slow spiral.
5. **Confusing a centre with a limit cycle.** A centre has a continuum of
   nested closed orbits with a period set by the initial condition; a limit
   cycle is isolated and has a period set by the dynamics. Numerically they
   look similar on a short run.
6. **Euler on a conservative system.** The energy drifts systematically; the
   resulting "instability" is in the method. Use a method that respects the
   structure, or a small enough step that you can demonstrate the drift is
   negligible.
7. **Treating a saddle as "unstable everywhere".** It is attracting along one
   direction and repelling along another; the geometry is the useful part.
8. **Forgetting that the fixed point itself moves when forcing is added.** The
   forcing changes the equilibrium, not usually its stability; the two
   questions are separate.

## 8. Real-world applications

- **Climate and energy-balance models.** Two-box and multi-box models are the
  standard tool for separating fast (atmosphere/ocean-skin) from slow (deep
  ocean, ice) responses to forcing.
- **Coupled geochemical reservoirs.** Mantle–crust, ocean–atmosphere and
  sediment–water couplings are written as systems whose eigenvalues give the
  residence times of the coupled system, which differ from the individual
  residence times.
- **Ice-albedo and weathering feedbacks.** Bistability is a saddle-node
  structure; the separatrix is the threshold.
- **Geodynamics.** Thermal convection onset is an eigenvalue problem; the sign
  of the growth rate decides whether the conductive state is stable. See
  [02-06-06 Mantle Convection and Rayleigh–Bénard Instability](../../02-physics/06-fluid-mechanics/06-mantle-convection.md).
- **Epidemic and ecological analogues.** Predator–prey, SIR and coupled
  reservoir models share these portraits; the mathematics transfers even when
  the physics does not.
- **Control of instruments and experiments.** Any feedback loop is a system of
  ODEs, and its stability is decided by the eigenvalues of the loop matrix.

## 9. Further reading

- **Strogatz, S. H. *Nonlinear Dynamics and Chaos.* Westview/CRC.** Chapters 5–8
  are the definitive introductory treatment of phase portraits, linearisation,
  the trace–determinant classification and limit cycles. Level: intermediate to
  advanced. If you read one book from this lesson, read this one.
- **Coddington, E. A., & Levinson, N. *Theory of Ordinary Differential
  Equations.* McGraw-Hill.** The chapters on linear systems and on stability
  give the rigorous versions of the theorems quoted here. Level: advanced.
- **Hirsch, M. W., Smale, S., & Devaney, R. L. *Differential Equations,
  Dynamical Systems, and an Introduction to Chaos.* Academic Press.** The
  Hartman–Grobman theorem and the Jordan form arguments in full. Level:
  advanced.
- **Boyce, W. E., & DiPrima, R. C. *Elementary Differential Equations and
  Boundary Value Problems.* Wiley.** The linear-systems chapter, with many
  worked phase portraits and a careful treatment of the degenerate cases.
- **Turcotte, D. L., & Schubert, G. *Geodynamics.* Cambridge University
  Press.** Chapter on stability and convection, where an eigenvalue problem
  decides whether a physical state persists.
- **Khalil, H. K. *Nonlinear Systems.* Prentice Hall.** Lyapunov theory done
  properly, including the positive-definite criteria used in Section 3.6.
  Level: advanced.
- **Saltzman, B. *Dynamical Paleoclimatology.* Academic Press.** Low-order
  climate models built from exactly these systems, including their bistability.

> Note on citations: bibliographic details above are given so that you can
> locate the works. This repository does not host or reproduce copyrighted
> text, and you should confirm current editions and availability through your
> library before citing them yourself.

## 10. Related lessons

- [02 Second-Order Linear ODEs and Characteristic Equations](./02-second-order-linear.md) —
  the same eigenvalues, computed from a scalar equation.
- [05 Sturm–Liouville Theory and Eigenfunction Expansions](./05-sturm-liouville.md) —
  the infinite-dimensional version, where the "matrix" is a differential
  operator.
- [07 Stiff Systems and Numerical Stability Challenges](./07-stiff-systems.md) —
  what $\lambda_1/\lambda_2 \gg 1$ does to a numerical method.
- [01-07-06 Eigenvalues, Eigenvectors and Diagonalisation](../07-linear-algebra/06-eigenvalues.md) —
  the linear algebra used throughout.
- [13-geodynamics-tectonics](../../13-geodynamics-tectonics/README.md) and
  [16-atmosphere-climate](../../16-atmosphere-climate/README.md) — where these
  portraits are fitted to data.
- [01-14 Optimization and Variational Methods](../14-optimization/README.md) —
  the local theory of minima, which is the same Hessian/eigenvalue question.

## Self-assessment checklist

- [ ] I can reduce an $n$-th order equation to a first-order system. (2.1)
- [ ] I can solve $\dot{\mathbf{x}} = A\mathbf{x}$ as a sum of eigenmodes and
      give each mode's timescale. (2.2)
- [ ] I can classify any $2\times2$ matrix from $(T,D)$ and name the portrait.
      (2.2, 3.1)
- [ ] I can distinguish stability from asymptotic stability and give an
      example of each. (2.3)
- [ ] I can compute a Jacobian, evaluate it at a fixed point and decide local
      stability. (3.3, 3.4)
- [ ] I can state when linearisation is trustworthy and when it is not. (2.3,
      Section 7.4)
- [ ] I can construct a Lyapunov function for a symmetric linear system and
      use Sylvester's criterion. (3.6)
- [ ] I can explain why a saddle is an amplifier with a preferred direction and
      what the separatrix means physically. (3.5)
