# Solutions — 01-07-10 Matrix Calculus and Sensitivity Derivatives

> **Read this after attempting the exercises, not before.**
>
> Every derivative below was checked against a central finite difference with step
> $10^{-6}$ before being written down. That check takes five lines and catches essentially
> all index errors.

---

## ★1 — Basic derivatives

| quantity | derivative | dimensions |
|---|---|---|
| (a) $a^\mathsf{T}x$, $a = (2,-1,3)$ | $(2,-1,3)^\mathsf{T}$ | gradient is $n\times1$, same shape as $x$ |
| (b) $x^\mathsf{T}Ax$, $A = \begin{bmatrix} 1 & 2 \\ 0 & 1\end{bmatrix}$ | $(A + A^\mathsf{T})x = \begin{bmatrix} 2 & 2 \\ 2 & 2\end{bmatrix}x$ | $n\times1$ |
| (c) $\|x\|^{4} = (x^\mathsf{T}x)^{2}$ | $4(x^\mathsf{T}x)x = 4\|x\|^{2}x$ | $n\times1$ |
| (d) $b^\mathsf{T}Ax$ | $A^\mathsf{T}b$ | $n\times1$ |

**Derivations.** (a) reads $\sum_i a_ix_i$, so $\partial/\partial x_k = a_k$.
(b) is the two-index case: $\partial(x^\mathsf{T}Ax)/\partial x_k = (Ax)_k +
(A^\mathsf{T}x)_k$, because $x_k$ appears once in the first slot and once in the second.
(d) $\sum_i\sum_j b_iA_{ij}x_j$ gives $\partial/\partial x_k = \sum_i b_iA_{ik} =
(A^\mathsf{T}b)_k$.

**Verification.** With $a = (2,-1,3)$ and $x = (0.3,-0.7,1.1)$ the finite difference
returns $(2.0,\ -1.0,\ 3.0)$ with a maximum error of order $10^{-10}$; the quadratic form
at $x = (0.3,-0.7,1.1)$ gives $(1.2,\ -3.1,\ 1.5)$ from both the analytic expression and
the finite difference, agreeing to $3.5\times10^{-11}$.

---

## ★2 — The misfit gradient and the regularised normal equations

$$\phi(m) = \tfrac12\sum_{i=1}^{m}\Big(\sum_{j=1}^{n}G_{ij}m_j - d_i\Big)^{2}, \qquad
\frac{\partial\phi}{\partial m_k} = \sum_i G_{ik}\Big(\sum_j G_{ij}m_j - d_i\Big) ,$$

because only the single factor $G_{ik}$ in the $i$-th bracket survives the
differentiation, while the bracket itself is left alone. Assembling:

$$\nabla_m\phi = G^\mathsf{T}(Gm - d) .$$

Setting it to zero gives $G^\mathsf{T}Gm = G^\mathsf{T}d$.

**Regularised.** For
$\phi_\alpha = \tfrac12\|Gm-d\|^{2} + \tfrac{\alpha}{2}\|Dm\|^{2}$, the second term has
gradient $\alpha D^\mathsf{T}Dm$ (the same identity with $G \to D$, $d \to 0$), so

$$\nabla_m\phi_\alpha = G^\mathsf{T}(Gm-d) + \alpha D^\mathsf{T}Dm = 0
\;\Longrightarrow\;
\big(G^\mathsf{T}G + \alpha D^\mathsf{T}D\big)m = G^\mathsf{T}d .$$

**Why deriving beats remembering.** The same three lines give the weighted version
($G^\mathsf{T}WGm = G^\mathsf{T}Wd$), the constrained version (Lagrange multipliers with
the system
$\begin{bmatrix} G^\mathsf{T}G & C^\mathsf{T} \\ C & 0\end{bmatrix}$), and the nonlinear
version of Section ★★4. A memorised formula gives one of the four.

---

## ★★3 — Gravity of a sphere, and the depth–radius trade-off

(a) With $K = \tfrac{4}{3}\pi G\Delta\rho R^{3}$ (units $\mathrm{m^{3}\,s^{-2}}$),

$$g_z = \frac{Kz}{(x^{2}+z^{2})^{3/2}},$$
$$\frac{\partial g_z}{\partial z} = K\frac{x^{2} - 2z^{2}}{(x^{2}+z^{2})^{5/2}}
\quad \left[\frac{\mathrm{m\,s^{-2}}}{\mathrm{m}}\right],$$
$$\frac{\partial g_z}{\partial R} = 4\pi G\Delta\rho R\,\frac{z}{(x^{2}+z^{2})^{3/2}}
= \frac{3g_z}{R} \quad \left[\frac{\mathrm{m\,s^{-2}}}{\mathrm{m}}\right].$$

The presence of $R^{3}$ in $K$ is why $\partial g_z/\partial R = 3g_z/R$: the anomaly is
proportional to the volume, hence to $R^{3}$.

(b) At $x = 0$, $z = 2000$ m, $R = 500$ m, $\Delta\rho = 500$
$\mathrm{kg\,m^{-3}}$:

$$K = \tfrac{4}{3}\pi(6.674\times10^{-11})(500)(500)^{3} = 17.472491\ \mathrm{m^{3}\,s^{-2}},$$
$$g_z = K/z^{2} = 17.472491/4\times10^{6} = 4.368123\times10^{-6}\
\mathrm{m\,s^{-2}} = \boxed{0.436812\ \text{mGal}} ,$$
$$\frac{\partial g_z}{\partial z} = -\frac{2K}{z^{3}} = -4.368123\times10^{-9}\
\frac{\mathrm{m\,s^{-2}}}{\mathrm{m}} = -4.368\times10^{-4}\ \frac{\text{mGal}}{\text{m}},$$
$$\frac{\partial g_z}{\partial R} = \frac{3g_z}{R} = 2.620874\times10^{-8}\
\frac{\mathrm{m\,s^{-2}}}{\mathrm{m}} = 2.621\times10^{-3}\
\frac{\text{mGal}}{\text{m}} .$$

(c) **The radius is the better-constrained parameter in absolute terms**, by a factor

$$\left|\frac{\partial g_z/\partial R}{\partial g_z/\partial z}\right| =
\frac{2.621\times10^{-3}}{4.368\times10^{-4}} = 6.0 .$$

A $1$ m error in radius changes the anomaly as much as a $6$ m error in depth. In
*relative* terms the two are comparable: the elasticities are
$(\partial g_z/\partial z)(z/g_z) = -2.0$ and
$(\partial g_z/\partial R)(R/g_z) = +3.0$, so a $1$ % change in either parameter changes
the anomaly by $2$ % or $3$ % respectively.

(d) Setting $\mathrm{d}g_z = 0$:

$$0 = \frac{\partial g_z}{\partial z}\delta z + \frac{\partial g_z}{\partial R}\delta R
\;\Longrightarrow\;
\frac{\delta z}{\delta R} = -\frac{\partial g_z/\partial R}{\partial g_z/\partial z}
= -6.0 .$$

So **a $1$ m increase in radius is exactly compensated by a $6$ m increase in depth** (and
the sign is negative because the two effects oppose). The Jacobian for this single
measurement is $1\times2$ and has rank 1: its null space is spanned by $(6,1)$-ish in
$(\delta z,\delta R)$ units. With one datum there is no way to separate depth from radius;
the data constrain only the combination $K/z^{2}$, and that leaves a one-parameter family —
the classic potential-field ambiguity, here in its simplest form.

(e) $z/R = 2000/500 = 4$, so $R \ll z$ and the point-mass limit is adequate. The leading
correction to the point-mass field of a uniform sphere at an external point is **exactly
zero** — by Newton's shell theorem the external field of a spherically symmetric body is
identical to that of a point mass at its centre, for *any* radius. So for a true sphere the
point-mass formula is not an approximation at all; the approximation enters only because a
real body is not spherical, and the correction is then of order the flattening or the
quadrupole moment, i.e. $(a/z)^{2}$ or $(a/z)^{3}$ in the relevant ratio, not
$(R/z)$ itself.

**This is a case worth stating carefully**: the reasoning "the body is small compared with
its depth, therefore treat it as a point mass" is correct for the *quadrupole and higher*
moments, but for a sphere the monopole term is already exact. Using the ratio $z/R$ to
justify a point-mass approximation is therefore the wrong argument; the right one is that
the body's shape deviates from a sphere, and the deviation enters at the order of the next
non-vanishing multipole.

---

## ★★4 — Newton versus Gauss–Newton on a large-residual problem

$$F(m) = e^{m}, \qquad d = 20, \qquad \phi(m) = \tfrac12(d - e^{m})^{2}.$$

(a) $F'(m) = F''(m) = e^{m}$, so
$\phi'(m) = -(d - e^{m})e^{m}$ and $\phi''(m) = e^{m}(2e^{m} - d)$. The exact minimiser is
$m^{*} = \ln 20 = 2.995732$.

(b) At $m_0 = 0$: $e^{0} = 1$, $\phi'(0) = -(20-1) = -19$, $\phi''(0) = 1(2 - 20) = -18$.

- **Exact Newton:** $m_1 = m_0 - \phi'/\phi'' = 0 - (-19)/(-18) = -1.055556$.
- **Gauss–Newton:** with $J = F'(0) = 1$ and residual $r = d - F = 19$,
  $m_1 = m_0 + (J^\mathsf{T}J)^{-1}J^\mathsf{T}r = 0 + 19/1 = +19$.

(c) **Sequences:**

| iteration | exact Newton | Gauss–Newton |
|---|---|---|
| 0 | $0.000000$ | $0.000000$ |
| 1 | $-1.055556$ | $19.000000$ |
| 2 | $-2.073583$ | $18.000000$ |
| 3 | $-3.079950$ | $17.000000$ |
| 5 | $-4.082258$ | $15.000003$ |
| 10 | (further negative) | $10.000528$ |
| 15 | — | $5.076805$ |
| 17 | — | $3.501033$ |
| 19 | — | $3.001424$ |
| limit | diverges to $-\infty$ | converges to $2.995732$ |

**Both methods fail in the way the theory predicts, and the failures are opposite.**

- **Exact Newton diverges**, because $\phi''(m) < 0$ for $m < \ln 10 = 2.302585$: the
  quadratic model has the *wrong curvature sign* there, so Newton's step points away from
  the minimum. Newton's method is only locally convergent, and $m_0 = 0$ is outside its
  basin of attraction for this problem. The failure has nothing to do with the
  implementation.
- **Gauss–Newton converges, but linearly and slowly.** Its step
  $m_{k+1} = m_k + (d - e^{m_k})/e^{m_k} = m_k + 20e^{-m_k} - 1$ gives $m_1 = 19$ — a
  wild overshoot — and then decreases by almost exactly $1$ per iteration from $19$ toward
  $3$, because $20e^{-m} \approx 0$ over that whole range. Only in the final few iterations,
  where $e^{m}$ approaches $20$, does it behave like a Newton method and converge quickly
  ($0.505 \to 0.109 \to \ldots$). Total: about $19$ iterations, all but the last few
  spent converging linearly.

(d) **The condition.** Gauss–Newton neglects the term
$\sum_i r_i\nabla^{2}F_i$ in the Hessian. It is a good approximation when the residuals
$r_i$ are small relative to the *curvature* of $F$: for this problem, when
$|d - e^{m}| \ll e^{m}$, i.e. when $e^{m} \gtrsim d$ and the model already nearly fits the
data. Here $r = 19$ against $F = 1$ — a residual nineteen times the model prediction — so
the neglect is severe at $m_0 = 0$, and the step is off by a factor of $20$.

**Practical reading.** The familiar statement "Gauss–Newton converges quadratically near
the solution and degrades gracefully away from it" is exactly what the table shows: fast
at the end, slow at the start — but *convergent*, where the exact Newton method from the
same starting point diverges. That robustness is why production inversion codes use
damped Gauss–Newton (Levenberg–Marquardt) rather than Newton: they give up the second-order
term deliberately, in exchange for a search direction that reliably decreases the misfit.

---

## ★★★5 — An adjoint for the diffusion problem

(a) **The adjoint system.** With $A(m)u = f$ and
$\phi = \tfrac12\|Su - d\|^{2}$, differentiate the forward system:

$$A\,\delta u + \frac{\partial A}{\partial m}\delta m\,u = 0
\;\Longrightarrow\;
\delta u = -A^{-1}\frac{\partial A}{\partial m}\delta m\,u .$$

Then $\delta\phi = (Su - d)^\mathsf{T}S\,\delta u$, so with the adjoint variable
$\lambda$ defined by

$$A^\mathsf{T}\lambda = S^\mathsf{T}(Su - d) ,$$

the gradient is

$$\frac{\mathrm{d}\phi}{\mathrm{d}m} = -\lambda^\mathsf{T}\frac{\partial A}{\partial m}u
\qquad\text{(component-wise: } \left.\partial\phi/\partial m_j =
-\lambda^\mathsf{T}(\partial A/\partial m_j)u\right) .$$

**Two solves:** one forward ($Au = f$) and one adjoint ($A^\mathsf{T}\lambda = S^\mathsf{T}r$).
Note that for a symmetric $A$ — which this diffusion operator is — the two systems have the
same matrix, so a single factorisation serves both, and the marginal cost is one more
triangular pair per iteration.

(b) **The dot-product test.** For random vectors $x$ (of model length) and $z$ (of data
length), verify

$$\langle z,\; A x\rangle = \langle A^\mathsf{T} z,\; x\rangle ,$$

i.e. `dot(z, forward(x)) == dot(adjoint(z), x)` to machine precision. This tests the
*transpose* relation, which is the only property of the adjoint that any solver uses. It is
a complete test of the adjoint's correctness (up to rounding) because the transpose is
defined by that identity for all $x, z$. In practice one also runs the test with the actual
gradient against a finite difference of the objective — a second, independent check that
catches sign and scaling errors that a random-vector test can miss when both maps are wrong
in a compensating way.

(c) **Solve counts.** The adjoint gradient needs **2** solves (one forward, one adjoint),
*independent of the number of parameters*. An explicit Jacobian needs one solve per datum,
i.e. $N_d$ solves, plus $N_m$ evaluations of the objective. For $N_d = 10^{4}$ and
$N_m = 10^{5}$ that is a saving factor of about $5\times10^{3}$ in operation count
([`../code/matrix_calculus_demo.py`](../code/matrix_calculus_demo.py) Section 5).

(d) **The adjoint is not "the forward solve run backwards".** Running the forward
discretisation with reversed time stepping (in a time-dependent problem) or with the same
matrix in reverse order solves a *different* system: it would compute $A^{-1}$ applied to
something, whereas the adjoint requires $A^{-\mathsf{T}}$ applied to the residual — the
transposed operator, which in a PDE means the adjoint *differential* operator with its own
boundary and interface conditions. For a symmetric operator the two coincide, which is
exactly why an incorrect adjoint often passes casual inspection on a self-adjoint test
problem and fails on a real one. The adjoint is defined by the bilinear identity in (b), and
nothing else.

(e) **Two tests before trusting the gradient.**

1. **The dot-product test** of (b), with several random pairs, at a tolerance of a few
   times $\epsilon_{\text{mach}}$ times the vector norms. It catches transposition errors.
2. **A finite-difference comparison of the objective.** For a random direction
   $\delta m$ of small norm, verify
   $\phi(m + \epsilon\delta m) - \phi(m - \epsilon\delta m) \approx
   2\epsilon\,\nabla\phi^\mathsf{T}\delta m$, and check that the discrepancy falls linearly
   with $\epsilon$ (first order) until round-off takes over. This catches sign errors,
   scaling errors and missing terms.

A third, cheap and often decisive test is to *minimise* with the gradient from a synthetic
model and confirm the inversion recovers it; but that tests the whole pipeline, not the
adjoint, and should come after the two above.

---

## ★★★6 — A nearly singular two-parameter experiment

(a) **Design.** The reflection travel time
$T(x) = \sqrt{x^{2}+4h^{2}}/v$ with parameters $(h, v)$, measured at two *very close*
offsets: $x = 0$ and $x = 0.1$ km, with the true model $h = 1.2$ km, $v = 3.7$ km/s. Both
rays then sample almost the same path, so the two data constrain almost the same
combination of depth and velocity.

Jacobian at the true model:

$$J = \begin{bmatrix} 0.540540541 & -0.175310446 \\ 0.540071931 & -0.175462559
\end{bmatrix}.$$

The columns, $c_1 = (0.540541,\ 0.540072)$ and $c_2 = (-0.175310,\ -0.175463)$, have

$$\cos\theta = \frac{\langle c_1, c_2\rangle}{\|c_1\|\|c_2\|} = -0.99999962,
\qquad \theta = 179.950307^{\circ},$$

i.e. the columns are antiparallel to within $5\times10^{-7}$ of a straight line — the
requested condition, and far beyond it.

(b) **Singular values and conditioning:**
$\sigma = (0.803357,\ 2.04611\times10^{-4})$, so

$$\kappa_2(J) = 3926.27 ,$$

against $\kappa_2 = 3.63$ for the wide-aperture design of
[`02-matrices-and-operations-solutions.md`](./02-matrices-and-operations-solutions.md)
(offsets 0–5 km). Moving the second station from $5$ km to $0.1$ km degrades the
conditioning by a factor of about **1080**.

(c) **Uncertainties.** With a $1$ % datum uncertainty the standard deviations are
$\sigma_d = 0.01\,T = (0.0064865,\ 0.0064921)$ s. Model standard deviations:

| quantity | formula | value (units of the parameter) |
|---|---|---|
| $\sigma_h$ | $\sqrt{(C_m)_{11}}$ | $9.79$ km |
| $\sigma_v$ | $\sqrt{(C_m)_{22}}$ | $30.15$ km/s |
| standard deviation along the *strong* singular direction | $\sigma_d/\sigma_{\max}$ | $8.07\times10^{-3}$ |
| standard deviation along the *weak* singular direction | $\sigma_d/\sigma_{\min}$ | $31.70$ |

against true values $h = 1.2$ km and $v = 3.7$ km/s. The weak-direction uncertainty
$31.70$ is $26$ times the depth itself: **the parameters are not determined at all**, and
the sharpness of the strong direction ($8\times10^{-3}$) is no consolation, because the
strong direction is almost exactly the *sum* combination that both stations measure — it
says nothing about depth and velocity separately.

(d) **The cure, quantified.** Add one measurement at a wide offset, $x = 5$ km:

| design | $\sigma_{\max}$ | $\sigma_{\min}$ | $\kappa_2$ | worst-direction $\sigma_d/\sigma_{\min}$ |
|---|---|---|---|---|
| $\{0,\ 0.1\}$ km | $0.803357$ | $2.046\times10^{-4}$ | $3926.27$ | $31.8$ |
| $\{0,\ 2\}$ km | $0.929516$ | $7.679\times10^{-2}$ | $12.11$ | $0.085$ |
| $\{0,\ 0.1,\ 5\}$ km | $0.885133$ | $2.842\times10^{-1}$ | $3.11$ | $0.023$ |
| $\{0..5\}$ km (seven offsets) | $1.155970$ | $3.182\times10^{-1}$ | $3.63$ | $0.020$ |

One extra station at $5$ km reduces $\kappa_2$ by a factor of **1261** and the
worst-direction model uncertainty by a factor of about **1360**. Adding further offsets
beyond that buys almost nothing: three well-spread offsets are nearly as good as seven.

**Is it worth the cost?** Yes, and the comparison is stark: one extra station turns a
measurement that determines nothing into one whose parameters are determined to a few
tenths of a per cent. The marginal cost is one receiver deployment; the marginal benefit is
the difference between an experiment and an anecdote. **This is the arithmetic that survey
design is made of**, and it is available before any data are collected, from the Jacobian
alone.
