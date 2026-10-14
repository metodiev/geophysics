# Solutions — 19-02-06 FD for Diffusion, Laplace and Poisson Problems

> **Read after attempting the exercises.** Demonstration values are quoted where
> they apply.

Lesson: [06 Diffusion and Potential](../06-fd-diffusion-and-potential.md).

---

## ★1 — Five-point Laplacian

$$\nabla^{2}u \approx \frac{u_{i+1,j}+u_{i-1,j}+u_{i,j+1}+u_{i,j-1}-4u_{i,j}}{h^{2}}
+ \frac{h^{2}}{12}\left(u_{xxxx}+u_{yyyy}\right) + O(h^{4}).$$

---

## ★2 — Conditioning and iterations

For the Dirichlet five-point Laplacian, $\kappa = O(h^{-2})$; on a unit square
the smallest eigenvalue is $2\pi^{2}$ and the largest is $8h^{-2}$ to leading
order, so $\kappa \approx 4/(\pi^{2}h^{2})$.

For a Krylov method the iteration count to a fixed relative residual scales as
$O(\sqrt\kappa) = O(h^{-1})$: **halving $h$ doubles the iterations**. The
demonstration measures this exponent as $1.013$ for CG against $1.957$ for
Jacobi, which is driven by $\kappa$ itself.

---

## ★3 — Fundamental-mode decay

$$u = e^{-2\pi^{2}\alpha t}\sin(\pi x)\sin(\pi y), \qquad
\tau = \frac{1}{2\pi^{2}\alpha} = \frac{1}{2\pi^{2}} = 0.050661\ \mathrm{s}
\quad(\alpha = 1).$$

---

## ★4 — The exact constant

The smooth error satisfies $\mathsf L_h e \approx -2\pi^{2}e$ with
$\mathsf L_h e = (h^{2}\pi^{4}/6)u$, so

$$e \approx -\frac{h^{2}\pi^{4}/6}{2\pi^{2}}u = -\frac{h^{2}\pi^{2}}{12}u,
\qquad \frac{\pi^{2}}{12} = 0.822467.$$

At $h = 1/50$: predicted maximum error $0.822467/2500 = 3.290\times10^{-4}$,
i.e. $0.822467\,h^{2}$. The demonstration's measured $\max|e|/h^{2}$ is
$0.820977$ at $n = 32$ ($h = 1/33$), $0.822083$ at $n = 64$ and $0.822369$ at
$n = 128$ — approaching $0.822467$ from below as the $O(h^{4})$ term decays.

---

## ★5 — Iteration counts and cost

Measured: $n = 16 \to 28$, $n = 32 \to 54$, $n = 64 \to 109$ iterations, an
exponent of $1.013$. Extrapolating with a factor $2^{1.013} = 2.018$ per
doubling:

- $n = 128$: about $109\times2.018 = 220$ iterations;
- $n = 256$: about $444$ iterations.

Cost per iteration grows with the unknown count: from $128^{2}$ to $256^{2}$ is
$4\times$. Total time factor $= 2.018\times4 = 8.1$, against $4$ unknowns per
direction — i.e. the solve cost grows slightly faster than the problem size,
which is the practical form of the $O(h^{-1})$ iteration law.

---

## ★6 — The bias of backward Euler

Relative bias:

$$\frac{2.006603\times10^{-2} - 1.929630\times10^{-2}}{1.929630\times10^{-2}}
= \frac{7.6973\times10^{-4}}{1.92963\times10^{-2}} = 0.03989,$$

i.e. $3.99\,\%$ high at $t = 0.2$ s (four timescales).

**Sign.** Backward Euler's mode amplification is $1/(1+dt\lambda)$ against the
exact $e^{-dt\lambda}$. Since $1/(1+x) > e^{-x}$ for every $x>0$, the scheme
decays more slowly than the physics at every step. The bias therefore
**accumulates in the direction of too little damping**, i.e. the amplitude is too
large, and it grows linearly in $t$ for small $dt\lambda$ (measured:
$1.9\,\%$ at $t = 0.02$, $4.0\,\%$ at $t = 0.2$ — approximately linear in time,
as expected).

---

## ★7 — A Poisson benchmark for iterative solvers

**Discretisation order.** Exact solution $u = \sin(\pi x)\sin(\pi y)$, so the
right-hand side is $f = 2\pi^{2}u$ and the constant is known
($\pi^{2}/12 = 0.822467$). Grids $n = 16, 32, 64, 128$; metric $\max|e|$ and
its ratio to $h^{2}$; acceptance: the constant within $0.5\,\%$ of $0.822467$ at
the finest grid and the observed order within $3\,\%$ of two.

**Iteration scaling.** Right-hand side: a localised Gaussian bump plus a smooth
ramp (broad spectrum). Metric: iterations to a relative residual of $10^{-10}$;
grids as above; acceptance: measured exponent in $[0.9, 1.2]$ for CG and
$[1.7, 2.1]$ for Jacobi. Both are measured in the demonstration.

**Preconditioner effect.** Repeat with an incomplete-Cholesky or
algebraic-multigrid preconditioner; metric the same iteration count; acceptance:
a demonstrable reduction of the exponent (multigrid should approach an
$h$-independent count for this problem class).

**Why a single mode is forbidden as a right-hand side.** A single sine mode is an
*eigenvector* of the discrete Laplacian. For such a right-hand side CG converges
in one iteration in exact arithmetic (and two if two modes are present), so the
measured count says nothing about the method's behaviour on real data. The
demonstration shows this directly: with a single-mode right-hand side the count
collapses to 1; with a broadband bump it is 28, 54, 109.

---

## ★8 — Marching to steady state instead of a direct solve

**Setup.** $h = 100$ m, $\alpha = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$, so
$dt_{\max} = h^{2}/(2\alpha d) = 10^{4}/(4\times10^{-6}) = 2.5\times10^{9}$ s
in 2-D.

**Time to steady state.** The slowest mode of the problem decays with
$\tau \sim L^{2}/(\pi^{2}\alpha)$; for a $10$ km domain that is
$10^{8}/(9.87\times10^{-6}) = 1.01\times10^{13}$ s. To reach, say,
$99.9\,\%$ of steady state takes about $7\tau = 7.1\times10^{13}$ s.

**Step count.** $7.1\times10^{13}/2.5\times10^{9} = 2.8\times10^{4}$ steps
(and the explicit limit is not the binding constraint — the long diffusive
timescale is).

**Comparison.** Each explicit step is a matrix-vector-like stencil application
with no assembly and no factorisation; $2.8\times10^{4}$ steps on a
$10^{4}$-unknown grid is $2.8\times10^{8}$ point-updates — trivial. A direct
sparse solve needs one factorisation plus one solve, usually faster in wall-clock
time for a single right-hand side and *much* faster if the problem is nonlinear
or has many right-hand sides (a factorised operator is reused).

**Verdict.** Both are defensible; the deciding factors are (i) whether the
operator is reused, (ii) whether storage for the factor is available (fill-in can
exceed the matrix), and (iii) whether the transient itself is of interest. What
is *not* defensible is choosing explicit marching "because it avoids a solver"
while ignoring the $2.8\times10^{4}$-step requirement and the slowest-mode
timescale that sets it: the honest comparison states the step count and the
timescale, as above.
