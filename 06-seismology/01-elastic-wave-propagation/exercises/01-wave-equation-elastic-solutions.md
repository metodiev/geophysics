# Solutions — 06-01-01 From Hooke's Law and Newton to the Elastodynamic Equation

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand; where the demonstration prints a value it is quoted directly.

Lesson: [01 From Hooke's Law and Newton to the Elastodynamic
Equation](../01-wave-equation-elastic.md).

---

## ★1 — Speeds and a dimensional check

For $\lambda = 25\times10^{9}$, $\mu = 30\times10^{9}\ \mathrm{Pa}$,
$\rho = 2700\ \mathrm{kg\,m^{-3}}$:

$$v_p = \sqrt{\frac{\lambda + 2\mu}{\rho}}
= \sqrt{\frac{(25 + 60)\times10^{9}}{2700}}
= \sqrt{3.148148\times10^{7}} = 5610.8361\ \mathrm{m\,s^{-1}},$$

$$v_s = \sqrt{\frac{\mu}{\rho}} = \sqrt{\frac{30\times10^{9}}{2700}}
= \sqrt{1.111111\times10^{7}} = 3333.3333\ \mathrm{m\,s^{-1}}.$$

Both match the demonstration exactly.

Dimensional check: $[\rho][\ddot u] = \mathrm{kg\,m^{-3}}\cdot
\mathrm{m\,s^{-2}} = \mathrm{kg\,m^{-2}\,s^{-2}} = \mathrm{Pa\,m^{-1}}$, and
$[\mu][\nabla^2 u] = \mathrm{Pa}\cdot\mathrm{m^{-1}} = \mathrm{Pa\,m^{-1}}$. The
demonstration prints the same chain as `rho * d2u/dt2 -> kg m^-2 s^-2 = Pa m^-1`
and `(lam+mu) grad(div u) -> Pa m^-1`.

---

## ★2 — Which term does which job

For $\mathbf u = \nabla\phi$, the vector identity
$\nabla^2\nabla\phi = \nabla(\nabla\cdot\nabla\phi)$ collapses the equation to
$\rho\ddot{\mathbf u} = (\lambda+2\mu)\nabla(\nabla^2\phi)$, i.e. the $\mu\nabla^2$
term is *redundant*, not absent: it adds to the same gradient. The
$(\lambda+\mu)$ term supplies the extra stiffness. The result is
$v_p^2 = (\lambda+2\mu)/\rho$.

For $\mathbf u = \nabla\times\boldsymbol\psi$ with $\nabla\cdot\boldsymbol\psi = 0$,
$\nabla\cdot\mathbf u = 0$, so the $(\lambda+\mu)\nabla(\nabla\cdot\mathbf u)$
term vanishes identically and only $\mu\nabla^2\mathbf u$ survives, giving
$v_s^2 = \mu/\rho$. This is the same argument the lesson makes with
$\nabla\cdot$ and $\nabla\times$.

---

## ★3 — Poisson solid

$\lambda = \mu$ gives

$$\frac{v_p}{v_s} = \sqrt{\frac{\lambda+2\mu}{\mu}} = \sqrt{3} = 1.732051.$$

Check against the demonstration: $5883.48/3396.83 = 1.732051$. ✔ Both follow
from the same model, so no independent information is added — the check is that
the ratio column and the speed columns are consistent arithmetic.

---

## ★4 — Residual convergence

Central differences have $O(\Delta x^2)$ truncation error, and halving
$\Delta x$ (doubling $n$) should cut the residual by 4.

| $n$ | predicted residual |
|---|---|
| 192 | $6.866\times10^{-3}/4 = 1.717\times10^{-3}$ |
| 384 | $1.717\times10^{-3}/4 = 4.29\times10^{-4}$ |
| 768 | $4.29\times10^{-4}/4 = 1.07\times10^{-4}$ |

The demonstration confirms the mechanism: it reports $2.834\times10^{-2}$ at
$n=48$ and $6.866\times10^{-3}$ at $n=96$, a factor $4.13$ per halving, and its
own table annotates the further rows as `residual x4.04` and `residual x4.03`.

A measured order of 1 would mean the residual is dominated by a **first-order**
operator — a one-sided rather than centred difference, or a boundary node handled
with a lower-order stencil. Since the reported constant is close to 4 but not
exactly 4, the honest reading is "second order plus a small higher-order
contamination", and the fitted order should be reported rather than assumed.

---

## ★5 — Grid dispersion at two wavenumbers

$$\text{error}(k_0\Delta x = 0.6280) = 1 - \frac{5402.1965}{5610.8361}
= 3.7185\%,$$
$$\text{error}(k_0\Delta x = 0.0785) = 1 - \frac{5608.5971}{5610.8361}
= 0.0399\%.$$

Ratio of errors: $3.7185/0.0399 = 93.2$. Ratio of $k_0\Delta x$:
$0.6280/0.0785 = 8.0$. If the error went as $(k_0\Delta x)^m$,
$8^m = 93.2$, so $m = \ln(93.2)/\ln 8 = 2.18$. The demonstration's fitted
exponent over the whole sequence is $2.172$ — the same number, obtained the same
way. The agreement confirms that the only difference between measured and derived
speed is grid dispersion.

---

## ★6 — Timestep and grid spacing

CFL: $\Delta t = r\Delta x/c = 0.5(1000)/5610.8361
= 0.089113\ \mathrm{s}$.

Ten points per wavelength at $f = 20\ \mathrm{Hz}$ requires
$\Delta x \le \lambda/10 = c/(10f) = 5610.8361/200 = 28.05\ \mathrm{m}$.

That is a factor of about 36 finer than the demonstration's $1000\ \mathrm{m}$
grid, which is exactly why the demonstration measures dispersion *on purpose*: it
uses a coarse grid so the effect is visible and measurable rather than
negligible.

---

## ★★7 — Discrete dispersion and group velocity (worked derivation)

With the standard three-point spatial and time stencils, substituting
$u_j^n = e^{\mathrm{i}(kj\Delta x - \omega n\Delta t)}$ into the scheme gives

$$\sin\!\left(\frac{\omega\Delta t}{2}\right)
= r\sin\!\left(\frac{k\Delta x}{2}\right),
\qquad r = \frac{c\Delta t}{\Delta x},$$

hence $\omega = (2/\Delta t)\arcsin(r\sin(k\Delta x/2))$. Differentiating with
respect to $k$:

$$c_g = \frac{\mathrm{d}\omega}{\mathrm{d}k}
= \frac{2}{\Delta t}\cdot
\frac{r\cos(k\Delta x/2)\cdot(\Delta x/2)}
{\sqrt{1 - r^2\sin^2(k\Delta x/2)}}
= \frac{c\cos(k\Delta x/2)}{\sqrt{1 - r^2\sin^2(k\Delta x/2)}},$$

using $r\Delta x/\Delta t = c$. Both factors are $\le 1$ for real $k$, so
$c_g \le c$: the numerical scheme is **slower** than the medium. That is why
every measured speed in the demonstration lies below $5610.8361\ \mathrm{m\,s^{-1}}$
and approaches it only as $k\Delta x \to 0$. A scheme that measured *faster* than
the medium would indicate a sign or coefficient error, not dispersion.

---

## ★★8 — Heterogeneous medium (worked derivation)

Without assuming homogeneity, $\partial_j$ must act on both $C_{ijkl}$ and the
field. For an isotropic but depth-dependent medium,

$$\rho\,\ddot u_i = \partial_j\left[\lambda\,\varepsilon_{kk}\delta_{ij}
+ 2\mu\,\varepsilon_{ij}\right]
= (\lambda+\mu)\partial_i(\partial_k u_k) + \mu\,\partial_k\partial_k u_i
+ (\partial_i\lambda)(\partial_k u_k) + 2(\partial_j\mu)\,\varepsilon_{ij}.$$

- $(\partial_i\lambda)\,\nabla\cdot\mathbf u$ is a **dilatation** term: where the
  bulk modulus changes along the direction of the P motion, it acts like a body
  force proportional to the local volume change.
- $2(\partial_j\mu)\varepsilon_{ij}$ is a **shear-gradient** term, sourced by the
  strain field where the shear modulus varies.

The first of these is the one that couples the two modes at a *gradient*: a P
wave travelling through a region where $\lambda$ varies generates a
divergence-proportional forcing that does not have the P polarisation pattern,
which is the mathematical origin of P-to-S conversion without a discrete
interface. This is why a smooth gradient and a sharp interface can produce the
same converted amplitude — the observation that makes
[08 Anisotropic Propagation](../08-anisotropic-propagation.md) and
[04 Body-Wave Arrivals](../04-body-wave-arrivals.md) hard to separate in
practice.

---

## ★★★9 — A design that needs the seed (specification)

**Metric.** Measured phase speed $\hat c$ of the packet, obtained by fitting the
envelope peak time against distance, as the demonstration does.

**Design.** Replace the deterministic Gaussian-modulated packet by
$u_0(x) = A(x)\sum_{m=1}^{M}a_m\cos(k_mx + \varphi_m)$ with $a_m$ drawn from a
stated spectrum and $\varphi_m$ random, using `RNG = np.random.default_rng(20261014)`.
For each $\Delta x$ in the demonstration's list, run $R$ realisations and record
the mean and standard deviation of $\hat c$.

**Why a seed is needed.** The bias (grid dispersion) is deterministic, but its
*estimate* is not: the realisation noise in $\hat c$ is what determines how many
runs are needed. From the central limit theorem, the standard error of the mean
falls as $R^{-1/2}$, so to resolve a bias that is, for example, $1/5$ of the
realisation standard deviation, $R \gtrsim 25$; to resolve it at the $1/10$ level,
$R \gtrsim 100$.

**Expected result.** The mean should reproduce the deterministic dispersion curve
(the same numbers as the demonstration's `v measured` column) within its standard
error, with the spread growing as $k_0\Delta x$ grows. A mean that disagrees with
the deterministic curve beyond its error bar would mean the packet-fitting
estimator is biased, which is a different failure from grid dispersion.
