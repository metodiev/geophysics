# Exercises — 01-06-07 Vector Identities and Their Role in Geophysics

Attempt these **closed-book** before opening the
[solutions](./07-vector-identities-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Use $\mu_0 = 4\pi\times10^{-7}$ H/m and $G = 6.674\times10^{-11}$.

---

## ★ Foundational

**★1.** Verify each product rule by direct differentiation for
$f = x^2y$, $\mathbf{F} = (y z,\ x z,\ x y)$.

(a) $\nabla\cdot(f\mathbf{F}) = f\nabla\cdot\mathbf{F} + \nabla f\cdot\mathbf{F}$
(b) $\nabla\times(f\mathbf{F}) = f\nabla\times\mathbf{F} + \nabla f\times\mathbf{F}$
(c) $\nabla^2(fg) = f\nabla^2g + 2\nabla f\cdot\nabla g + g\nabla^2f$ with
$g = z^2$

---

**★2.** Prove in index notation that
$\nabla\cdot(\nabla\times\mathbf{F}) = 0$ for any $C^2$ field $\mathbf{F}$.

---

**★3.** Prove in index notation that $\nabla\times\nabla f = \mathbf{0}$ for any
$C^2$ scalar $f$, and state the smoothness hypothesis that the proof uses.

---

**★4.** For the radial function $F(r)$:

(a) derive $\nabla^2F = F''(r) + \frac{2}{r}F'(r)$;
(b) apply it to $F = r^n$ and state the values of $n$ for which the result
vanishes;
(c) explain what part (b) implies about the gravitational potential of a point
mass.

---

## ★★ Applied

**★★5.** Derive the curl–curl identity
$\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F}$
in full, naming each step of the Levi-Civita manipulation.

---

**★★6.** The equations of linear isotropic elastodynamics are

$$\mu\nabla^2\mathbf{u} + (\lambda+\mu)\nabla(\nabla\cdot\mathbf{u})
= \rho\,\partial_t^2\mathbf{u}.$$

(a) Derive the two separated wave equations for $\nabla\cdot\mathbf{u}$ and
$\nabla\times\mathbf{u}$.
(b) State $v_p$ and $v_s$ in terms of $\lambda$, $\mu$ and $\rho$.
(c) Compute both speeds for granite-like values
$\lambda = 3.0\times10^{10}$ Pa, $\mu = 3.0\times10^{10}$ Pa,
$\rho = 2700\ \mathrm{kg\,m^{-3}}$.
(d) Compute Poisson's ratio from $v_p/v_s$ and state whether the value is
consistent with $\lambda = \mu$.

---

**★★7.** Starting from Maxwell's equations in a homogeneous, isotropic,
charge-free medium, derive

$$\nabla^2\mathbf{E} = \mu\sigma\,\partial_t\mathbf{E}
+ \mu\varepsilon\,\partial_t^2\mathbf{E}.$$

(a) Identify which term is dominant at low frequency and which at high frequency,
and give the crossover condition in terms of $\omega$, $\sigma$ and $\varepsilon$.
(b) For a plane wave $\mathbf{E} \propto e^{i(kz-\omega t)}$, derive
$k^2 = i\omega\mu\sigma$ in the quasi-static limit and hence
$\delta = \sqrt{2/(\omega\mu\sigma)}$.
(c) Compute $\delta$ for $T = 100$ s and $\sigma = 0.02$ S/m, and for $T = 10$ s
and $\sigma = 0.5$ S/m.
(d) State in one sentence why long-period MT sounds deeper.

---

**★★8.** Starting from the identity
$\nabla\cdot(\hat{r}/r^2) = 4\pi\delta^3(\mathbf{r})$, derive Poisson's equation
$\nabla^2V = -4\pi G\rho$ for $V = G\int\rho/D\,dV'$, naming the property of the
delta function you use.

---

## ★★★ Research-oriented

**★★★9.** Numerical verification of the identities.

Using the test fields $f = x^2y + y^2z + z^2x$ and
$\mathbf{F} = (xy+z^2,\ yz+x^2,\ zx+y^2)$ at the point $(0.7,-0.4,1.1)$:

(a) verify $\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) -
\nabla^2\mathbf{F}$ with central differences at $H = 10^{-3}$, and report the
residual and the reference scale.
(b) repeat for $H = 10^{-2}, 10^{-3}, 10^{-4}, 10^{-5}$ and report the empirical
order of convergence of the residual.
(c) verify that the residual for $\nabla\times\nabla(f)$ is *exactly* zero at
every $H$, and explain why no convergence rate applies.
(d) discuss the difference between (b) and (c) in terms of what a numerical check
of an identity can establish.

---

**★★★10.** The delta function is not a pointwise statement.

(a) Compute $\nabla\cdot(\hat{r}/r^2)$ symbolically and show it vanishes for
$r>0$.
(b) Compute the flux of $\hat{r}/r^2$ through a sphere of radius $R$ and show it is
$4\pi$ for every $R$.
(c) Explain why a finite-difference divergence evaluated at
$\mathbf{r} = (0.7,-0.4,1.1)$ returns zero, and why that zero does not contradict
(b).
(d) Now evaluate the *Laplacian* of $1/r$ numerically with central differences at
$r = 0.5$, $r = 0.05$ and $r = 0.005$ with $H = 10^{-3}$ and report the three
values. The analytic value is zero everywhere for $r>0$. Explain the growth and
state what it demonstrates about the limits of finite differences.

Report measured numbers as measured; do not adjust them to match theory.
