# Solutions — 01-08-04 Systems of ODEs, Phase Portraits and Stability

> **Read this after attempting the exercises, not before.** Every eigenvalue,
> eigenvector, timescale and equilibrium below was computed; the classification
> rules are applied from $T$ and $D$, not read off a picture.

---

## ★1 — Classification of five matrices

Throughout, $T = \operatorname{tr}A$, $D = \det A$, and
$\lambda = \tfrac12\left(T\pm\sqrt{T^{2}-4D}\right)$.

| Matrix | $T$ | $D$ | $T^{2}-4D$ | Eigenvalues | Portrait | Stability |
|---|---|---|---|---|---|---|
| (a) | $-2$ | $0.75$ | $1$ | $-0.5,\ -1.5$ | node | asymptotically stable |
| (b) | $-3$ | $6$ | $-15$ | $-1.5\pm1.936492i$ | spiral | asymptotically stable |
| (c) | $1$ | $-0.75$ | $4$ | $1.5,\ -0.5$ | saddle | unstable |
| (d) | $0$ | $4$ | $-16$ | $\pm2i$ | centre | stable, not asymptotically |
| (e) | $1$ | $-6$ | $25$ | $3,\ -2$ | saddle | unstable |

Details worth checking by hand:

**(b)** $T^{2}-4D = 9-24 = -15<0$, so complex; the real part is $T/2 = -1.5<0$,
so the spiral is stable. Note the ratio
$|\operatorname{Im}\lambda|/|\operatorname{Re}\lambda| = 1.936/1.5 = 1.29$: a
little more than one oscillation per e-folding, i.e. a low-$Q$ spiral, quite
unlike the near-circular case $T = -0.2$, $D = 1.01$ in the lesson.

**(c)** $D = 0.25-1 = -0.75<0$ is enough on its own: **$D<0$ is a saddle,
always**, and no inspection of $T$ is needed. The unstable direction is slow
($\lambda = +1.5$) and the stable direction fast ($\lambda = -0.5$).

**(d)** $T = 0$ and $D>0$ with $T^{2}-4D<0$ gives a **centre**: the motion is
oscillatory and bounded but does not decay. This is the one case with a
meaningful distinction between "stable" and "asymptotically stable", and it is
precisely the case where a linearisation is not conclusive.

**(e)** Diagonal, so the eigenvalues are the diagonal entries and the coordinate
axes are the eigenvectors: a saddle with an unstable $x$-direction and a stable
$y$-direction.

---

## ★2 — Reduction to a first-order system

Set $x_1 = x$, $x_2 = x'$. Then $x_1' = x_2$ and, from the ODE,
$x_2' = -\omega_0^{2}x_1 - 2\zeta\omega_0x_2$. In matrix form

$$\frac{d}{dt}\begin{pmatrix}x_1\\x_2\end{pmatrix}
= \begin{pmatrix}0 & 1\\ -\omega_0^{2} & -2\zeta\omega_0\end{pmatrix}
\begin{pmatrix}x_1\\x_2\end{pmatrix}.$$

The characteristic polynomial of the matrix is

$$\det\begin{pmatrix}-\lambda & 1\\ -\omega_0^{2} & -2\zeta\omega_0-\lambda
\end{pmatrix}
= (-\lambda)(-2\zeta\omega_0-\lambda)+\omega_0^{2}
= \lambda^{2}+2\zeta\omega_0\lambda+\omega_0^{2},$$

which is exactly the characteristic equation of
[02 Second-Order Linear ODEs](../02-second-order-linear.md). **The two lessons
are the same lesson**: the discriminant $\omega_0^{2}(\zeta^{2}-1)$ of the scalar
equation is $T^{2}-4D$ of the matrix, since here
$T^{2}-4D = 4\zeta^{2}\omega_0^{2}-4\omega_0^{2}$.

---

## ★3 — Lotka–Volterra equilibrium and linearisation

**(a)** Setting the right-hand sides to zero and discarding the trivial
equilibria (which lie on the axes), $ax = bxy$ and $cy = dxy$ give

$$y^{*} = \frac{a}{b} = \frac{1}{0.5} = 2, \qquad
x^{*} = \frac{c}{d} = \frac{0.8}{0.4} = 2 .$$

*Verify by substitution:* $1(2)-0.5(2)(2) = 2-2 = 0$ ✓ and
$-0.8(2)+0.4(2)(2) = -1.6+1.6 = 0$ ✓.

**(b)** The Jacobian is

$$J = \begin{pmatrix}a-by & -bx\\ dy & -c+dx\end{pmatrix}
\;\xrightarrow{(2,2)}\;
\begin{pmatrix}1-1 & -1\\ 0.8 & -0.8+0.8\end{pmatrix}
= \begin{pmatrix}0 & -1\\ 0.8 & 0\end{pmatrix},$$

so $T = 0$, $D = 0.8$, $T^{2}-4D = -3.2$ and

$$\lambda = \pm\sqrt{-0.8} = \pm 0.894427i .$$

**(c)** $T = 0$, $D>0$, complex: a **centre**. The linearisation therefore says
the equilibrium is stable but not asymptotically stable — it does *not* say that
nearby trajectories are periodic, and the theorem that licenses reading
qualitative behaviour off a linearisation (Hartman–Grobman) **does not apply
here**, because a centre is not hyperbolic. The demonstration in the lesson
settles the question a different way: it integrates the non-linear system and
measures the drift of the invariant $H$, finding $-1.5\times10^{-14}$ over 100
time units, so the orbits really are closed. **The linearisation raised the
question; only the invariant answered it.**

---

## ★★4 — A two-box model with unequal heat capacities

**(a)** Dividing each equation by its heat capacity,

$$\dot T_1 = -(\lambda+\gamma)T_1 + \gamma T_2 = -1.5T_1 + 0.5T_2, \qquad
\dot T_2 = \frac{\gamma}{C_2}(T_1-T_2) = 0.25T_1 - 0.25T_2 .$$

So $A = \begin{pmatrix}-1.5 & 0.5\\ 0.25 & -0.25\end{pmatrix}$, with
$T = -1.75$, $D = (-1.5)(-0.25)-(0.5)(0.25) = 0.375-0.125 = 0.25$ and
$T^{2}-4D = 3.0625-1 = 2.0625>0$: a **stable node** with eigenvalues

$$\lambda_{1,2} = \frac{-1.75\pm1.436141}{2} = -0.156930,\ -1.593070 .$$

**(b)** The relaxation times are $\tau = -1/\lambda$:

$$\tau_{\text{slow}} = \frac{1}{0.156930} = 6.372\ , \qquad
\tau_{\text{fast}} = \frac{1}{1.593070} = 0.628\ .$$

(Time units are arbitrary here; with $C$ in $\mathrm{J\,K^{-1}\,m^{-2}}$ and
$\lambda$ in $\mathrm{W\,m^{-2}\,K^{-1}}$ they are months and weeks
respectively.) **The fast mode is the surface equilibrating with the deep box,
and the slow mode is the two boxes returning together to radiative balance** —
the same structure as the equal-capacity case of the lesson, with the timescales
shifted by the unequal heat capacities.

**(c)** The slow eigenvector satisfies $(A-\lambda_1I)\mathbf{v} = \mathbf{0}$.
Taking the first row, $(-1.5+0.156930)v_1 + 0.5v_2 = 0$, so
$v_2/v_1 = 1.343140/0.5 = 2.686280$; normalising,

$$\mathbf{v}_{\text{slow}} = (0.348889,\ 0.937164) .$$

**Both components have the same sign**, so in the slow mode the surface and the
deep ocean warm and cool *together*, in the ratio 0.349 : 0.937 — the deep box
moves about 2.7 times as far as the surface. Physically: the slow mode is the
whole system charging and discharging, and because the deep box has the larger
heat capacity, most of the extra heat in that mode goes into it. By contrast the
fast eigenvector is $(0.983113,\ -0.182997)$: the two boxes move in **opposite**
directions, which is the signature of a redistribution of heat *between* them at
fixed total. **Reading the sign pattern of an eigenvector is the fastest way to
identify which physical process a mode represents.**

---

## ★★5 — A saddle, fully analysed

**(a)** $T = 0.2$, $D = -0.07$, $T^{2}-4D = 0.04+0.28 = 0.32$, so

$$\lambda_{1,2} = \frac{0.2\pm0.565685}{2} = +0.382843,\ -0.182843 .$$

For each root take $\mathbf{v} = (b,\ \lambda-a) = (0.2,\ \lambda-0.3)$, then
normalise:

$$\mathbf{v}_{u} = \frac{(0.2,\ 0.082843)}{\sqrt{0.04+0.006863}}
= (0.923880,\ 0.382683),$$

$$\mathbf{v}_{s} = \frac{(0.2,\ -0.482843)}{\sqrt{0.04+0.233137}}
= (0.382683,\ -0.923880).$$

(These two are orthogonal, as they must be for a symmetric matrix — here
$A$ is symmetric, which is a useful check.)

**(b)** Write the initial condition in the eigenbasis,
$\mathbf{x}_0 = c_u\mathbf{v}_u + c_s\mathbf{v}_s$. Applying the inverse of the
matrix $[\mathbf{v}_u\ \mathbf{v}_s]$ to $(0.01,0)$ gives
$c_u = 0.01\times0.923880 = 0.0092388$, $c_s = 0.01\times0.382683 = 0.0038268$.
As $t\to\infty$ the term $c_se^{-0.1828t}\mathbf{v}_s$ decays and only
$c_ue^{+0.3828t}\mathbf{v}_u$ remains:

$$\mathbf{x}(t) \propto \mathbf{v}_u = (0.923880,\ 0.382683)
\quad\text{for } \mathbf{x}_0 = (0.01,0).$$

For $\mathbf{x}_0 = (-0.01,0)$ both coefficients flip sign, so
$\mathbf{x}(t)\propto-\mathbf{v}_u = (-0.923880,\ -0.382683)$. **Both endpoints
lie on the same line, in opposite directions.** This is the point made in the
lesson: the surviving direction is the same for every start except those exactly
on the stable line, and the *sign* is inherited from the initial condition.

**(c)** The stable eigenvector $\mathbf{v}_s$ is the direction along which
perturbations are attracted toward the equilibrium; the line it spans is the
**stable manifold**, or in the planar terminology the **separatrix**, because it
separates trajectories that end in one out-direction from those that end in the
other. Physically, it is the threshold: a perturbation that starts on one side
of it ends in one state, and one that starts on the other side ends in the
opposite state. **Threshold behaviour in a dynamical model is always a manifold
statement, never a single-number test.**

---

## ★★6 — A Lyapunov function

**(a)** With $A = \begin{pmatrix}-2 & 0.8\\ 0.8 & -0.8\end{pmatrix}$ (since
$\lambda+\gamma = 2$) and $V = \tfrac12(T_1^{2}+T_2^{2})$,

$$\dot V = T_1\dot T_1 + T_2\dot T_2
= T_1(-2T_1+0.8T_2) + T_2(0.8T_1-0.8T_2)
= -2T_1^{2} + 1.6T_1T_2 - 0.8T_2^{2},$$

so, symmetrising,

$$\dot V = -\mathbf{T}^{\top}Q\mathbf{T}, \qquad
Q = \begin{pmatrix}2 & -0.8\\ -0.8 & 0.8\end{pmatrix}.$$

**(b)** Sylvester's criterion: $Q_{11} = 2>0$ and
$\det Q = 1.6-0.64 = 0.96>0$. Both leading principal minors are positive, so
$Q$ is **positive definite**, hence $\dot V<0$ for every $\mathbf{T}\neq
\mathbf{0}$ and $V$ decreases monotonically along every trajectory. (The
criterion is stated for symmetric matrices, and $Q$ is symmetric by
construction; $Q_{12}$ must be symmetrised as $-(A_{12}+A_{21})/2 = -0.8$.)

**(c)** The eigenvalue calculation gave *local* asymptotic stability: it
describes trajectories that start sufficiently close. The Lyapunov function
gives **global** asymptotic stability — every trajectory, from any initial
condition, converges to the origin — because $V$ is radially unbounded and
$\dot V<0$ everywhere except at the origin. For a linear system the two
conclusions happen to coincide, but the Lyapunov argument extends to non-linear
systems where the linearisation says nothing beyond a neighbourhood, and to
systems where the linearisation is inconclusive.

---

## ★★★7 — The trace, the Hopf bifurcation, and model choice

**(a)** At the interior equilibrium, $dx^{*} = c$, so
$J_{22} = -c+dx^{*} = 0$, and $ax^{*}(1-x^{*}/K) = bx^{*}y^{*}$, i.e.
$by^{*} = a(1-x^{*}/K)$. Then

$$J_{11} = a\left(1-\frac{2x^{*}}{K}\right) - by^{*}
= a\left(1-\frac{2x^{*}}{K}\right) - a\left(1-\frac{x^{*}}{K}\right)
= -\frac{ax^{*}}{K},$$

and with $x^{*} = c/d$,

$$T = J_{11}+J_{22} = -\frac{ac}{dK} < 0 \quad\text{for all } a,c,d,K>0.$$

A Hopf bifurcation requires $T$ to pass through zero with $D>0$, so **no such
bifurcation can occur from this equilibrium.** (It is worth noting what the sign
of $T$ does *not* say: it does not exclude limit cycles from other mechanisms,
e.g. a homoclinic or a saddle-node-of-cycles bifurcation, only the local one.)

**(b)** With the saturating response $bxy/(1+hx)$, the interior equilibrium
satisfies $dx^{*}/(1+hx^{*}) = c$ and $a(1-x^{*}/K) = by^{*}/(1+hx^{*})$, so
$J_{22} = -c+dx^{*}/(1+hx^{*}) = 0$ still, and now

$$J_{11} = a\left(1-\frac{2x^{*}}{K}\right)
- \frac{by^{*}}{1+hx^{*}} + \frac{bhx^{*}y^{*}}{(1+hx^{*})^{2}},$$

so, replacing $by^{*}/(1+hx^{*})$ by $a(1-x^{*}/K)$,

$$T = a\left(1-\frac{2x^{*}}{K}\right) - a\left(1-\frac{x^{*}}{K}\right)
+ \frac{bhx^{*}y^{*}}{(1+hx^{*})^{2}}
= x^{*}\left[-\frac{a}{K} + \frac{bh\,y^{*}}{(1+hx^{*})^{2}}\right].$$

**The extra term is positive**, so it can balance the negative one: the trace
can change sign.

**(c)** With $a = b = d = 1$, $c = 0.4$, $h = 0.5$:
$x^{*} = c/(d-ch) = 0.4/(1-0.2) = 0.5$ and
$y^{*} = a(1-x^{*}/K)(1+hx^{*})/b = 1.25(1-0.5/K)$. Setting $T = 0$:

$$\frac{1}{K} = \frac{bhy^{*}}{(1+hx^{*})^{2}} = \frac{0.5\times1.25(1-0.5/K)}{1.5625}
= 0.4 - \frac{0.2}{K}
\;\Longrightarrow\; \frac{1.2}{K} = 0.4
\;\Longrightarrow\; K = 3 .$$

**So the Hopf bifurcation occurs exactly at $K = 3$.** At $K = 5$,
$y^{*} = 1.25(0.9) = 1.125$ and

$$T = 0.5\left[-\frac{1}{5} + \frac{0.5\times1.125}{1.5625}\right]
= 0.5\left[-0.2+0.36\right] = +0.080000 > 0,$$

so the equilibrium has become an **unstable spiral** and trajectories approach a
limit cycle around it. This is the "paradox of enrichment": making the
environment more productive destroys the stable coexistence.

**(d)** The two results differ **only in the form of one term of the model** —
$bxy$ versus $bxy/(1+hx)$ — yet the qualitative conclusion is opposite: an
equilibrium that is unconditionally attracting in one model becomes capable of
oscillating indefinitely in the other, for the same parameter ranges. The
algebra is not the issue; **the warning is that a modelling choice made for
convenience (linear mass-action predation, which is the default in many coupled
reservoir analogues) can silently rule out the behaviour the model was built to
study.** Before trusting a stability conclusion, state which functional forms
were assumed and check whether the conclusion survives replacing them with the
next-most-plausible alternatives.

---

## ★★★8 — Adding a constant forcing

**(a)** Setting $\dot{\mathbf{T}} = \mathbf{0}$ gives
$A\mathbf{T}^{*}+\mathbf{F} = \mathbf{0}$, so

$$\mathbf{T}^{*} = -A^{-1}\mathbf{F}.$$

With $A = \begin{pmatrix}-1.5 & 0.5\\ 0.25 & -0.25\end{pmatrix}$ its inverse is

$$A^{-1} = \frac{1}{D}\begin{pmatrix}-0.25 & -0.5\\ -0.25 & -1.5\end{pmatrix}
= \frac{1}{0.25}\begin{pmatrix}-0.25 & -0.5\\ -0.25 & -1.5\end{pmatrix}
= \begin{pmatrix}-1 & -2\\ -1 & -6\end{pmatrix},$$

so for $\mathbf{F} = (1,0)$,

$$\mathbf{T}^{*} = -\begin{pmatrix}-1\\ -1\end{pmatrix}
= \begin{pmatrix}1\\ 1\end{pmatrix}$$

— in these units the forced equilibrium has both boxes one unit warmer, which is
the expected sign for a positive energy input.

**(b)** The Jacobian of $\dot{\mathbf{T}} = A\mathbf{T}+\mathbf{F}$ is
$A$ itself, because $\partial\mathbf{F}/\partial\mathbf{T} = 0$ for constant
$\mathbf{F}$. **A constant forcing shifts the equilibrium but does not touch its
stability.** This is the general principle: for an autonomous system, adding a
constant term translates the vector field without changing its derivative
structure, so every stability conclusion from the unforced problem carries over
verbatim. It is why a model can be analysed at the origin and then applied with
forcing, and it is also why a *time-dependent* forcing is qualitatively different
— a time-dependent term appears as an explicit $t$ in the Jacobian's argument and
can move an equilibrium, create a periodic orbit, or sweep a system through a
bifurcation.

**(c)** Write the initial departure from the forced equilibrium in the
eigenbasis: with $\mathbf{T}(0) = \mathbf{0}$ and
$\mathbf{T}^{*} = (1,1)$,

$$\mathbf{T}(0)-\mathbf{T}^{*} = (-1,-1) = a\,\mathbf{v}_{\text{slow}}
+ b\,\mathbf{v}_{\text{fast}},
\qquad a = -1.183647, \quad b = -0.597122 .$$

Since $\mathbf{v}_{\text{slow}} = (0.348889,\,0.937164)$ and
$\mathbf{v}_{\text{fast}} = (0.983113,\,-0.182997)$, the surface temperature
follows

$$T_1(t) = 1 - 0.412966\,e^{-0.156930t} - 0.587035\,e^{-1.593070t},$$

so the *deficit* of the surface splits into a slow part of weight 0.413 and a
fast part of weight 0.587. Numerically:

| $t$ | $T_1(t)$ | fraction of the change | $T_2(t)$ |
|---|---|---|---|
| 0.628 | 0.409933 | 41.0 % | 0.035016 |
| 1.593 | 0.631981 | 63.2 % | 0.144726 |
| 2.000 | 0.674019 | 67.4 % | 0.194058 |
| 6.372 | 0.848050 | 84.8 % | 0.591908 |
| 20.000 | 0.982101 | 98.2 % | 0.951920 |

**The surface covers 63 % of its change at $t = 1.593$, not at
$\tau_{\text{slow}} = 6.372$.** The naive expectation fails because the forcing
projects more strongly onto the *fast* mode on the surface (weight 0.587) than
onto the slow mode (0.413), even though the fast mode decays ten times faster.
What *is* true is that after about $t = 2$ the fast contribution is negligible
and the remaining approach is slow-mode controlled: at $t = 1.593$ the slow mode
already accounts for 87.4 % of the remaining deficit, and the deep box has moved
only 14.5 % of the way to its equilibrium, a visible lag. **The long-time
response is always governed by the slowest mode — but the *time to 63 %* is
governed by whichever modes the forcing excites, and that requires the
coefficients, not just the eigenvalues.**

**(d)** Reversing which component the forcing enters changes $A^{-1}\mathbf{F}$,
hence the equilibrium, but leaves $A$ unchanged, so the *stability* and the
*timescales* are identical. The magnitude of $\mathbf{T}^{*}$ changes because
$A^{-1}$ is not diagonal; the sign changes only if the relevant column of
$-A^{-1}$ has a sign opposite to that for $\mathbf{F} = (1,0)$, which here it
does not for the first component ($-A^{-1}_{11} = 1$) but does for the second
($-A^{-1}_{12} = 2$ versus $-A^{-1}_{22} = 6$, both positive). **The general
lesson: the response of a coupled system to a forcing in one compartment is
distributed according to the columns of $A^{-1}$, which is why a perturbation
applied in one place shows up somewhere else.**
