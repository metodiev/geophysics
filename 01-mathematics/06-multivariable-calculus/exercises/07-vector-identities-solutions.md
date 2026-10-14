# Solutions — 01-06-07 Vector Identities and Their Role in Geophysics

> **Read this after attempting the exercises, not before.**
>
> Throughout, $\mu_0 = 4\pi\times10^{-7}$ H/m and $G = 6.674\times10^{-11}$.

---

## ★1 — Product rules verified by direct differentiation

With $f = x^2y$, $\mathbf{F} = (yz, xz, xy)$ and $g = z^2$:

**(a)** $f\mathbf{F} = (x^2y^2z,\ x^3yz,\ x^3y^2)$. Then

$$\nabla\cdot(f\mathbf{F}) = 2xy^2z + x^3z + 0 = 2xy^2z + x^3z .$$

Right-hand side: $\nabla\cdot\mathbf{F} = 0$ (from
[01-06-04](./04-divergence-and-curl-solutions.md), ★1(b)), and
$\nabla f = (2xy, x^2, 0)$, so

$$\nabla f\cdot\mathbf{F} = 2xy\cdot yz + x^2\cdot xz + 0 = 2xy^2z + x^3z . \checkmark$$

**(b)** $f\mathbf{F} = (x^2y^2z,\ x^3yz,\ x^3y^2)$, so

$$\nabla\times(f\mathbf{F}) = \left(\frac{\partial(x^3y^2)}{\partial y}
- \frac{\partial(x^3yz)}{\partial z},\
\frac{\partial(x^2y^2z)}{\partial z} - \frac{\partial(x^3y^2)}{\partial x},\
\frac{\partial(x^3yz)}{\partial x} - \frac{\partial(x^2y^2z)}{\partial y}\right)$$

$$= \left(2x^3y - x^3y,\ x^2y^2 - 3x^2y^2,\ 3x^2yz - 2x^2yz\right)
= \left(x^3y,\ -2x^2y^2,\ x^2yz\right).$$

Right-hand side: $f\nabla\times\mathbf{F} = \mathbf{0}$ because
$\nabla\times\mathbf{F} = \mathbf{0}$, and

$$\nabla f\times\mathbf{F} = (2xy,\ x^2,\ 0)\times(yz,\ xz,\ xy)
= \left(x^2\cdot xy - 0,\ 0 - 2xy\cdot xy,\ 2xy\cdot xz - x^2\cdot yz\right)$$

$$= \left(x^3y,\ -2x^2y^2,\ x^2yz\right) . \checkmark$$

**(c)** With $g = z^2$, $fg = x^2yz^2$, so

$$\nabla^2(fg) = 2yz^2 + 0 + 2x^2y = 2yz^2 + 2x^2y .$$

Right-hand side:

$$f\nabla^2g = x^2y \cdot 2 = 2x^2y, \qquad
2\nabla f\cdot\nabla g = 2(2xy, x^2, 0)\cdot(0,0,2z) = 0, \qquad
g\nabla^2f = z^2 \cdot 2y = 2yz^2 .$$

Sum: $2x^2y + 2yz^2$ ✓.

**Note.** In (a) and (b) the entire right-hand side came from the $\nabla f$ term,
because $\mathbf{F}$ happens to be curl-free and divergence-free. **A test field
with both of those properties is a weak test**: it cannot distinguish a correct
identity from one missing a term. This is why the module's demonstration used
$\mathbf{F} = (xy+z^2, yz+x^2, zx+y^2)$, for which $\nabla\cdot\mathbf{F} = 1.400$
and $\lvert\nabla\times\mathbf{F}\rvert = 1.364$ are both nonzero.

---

## ★2 — $\nabla\cdot(\nabla\times\mathbf{F}) = 0$

In index notation, with $\partial_i = \partial/\partial x_i$:

$$\nabla\cdot(\nabla\times\mathbf{F})
= \partial_i\varepsilon_{ijk}\partial_jF_k
= \varepsilon_{ijk}\partial_i\partial_jF_k .$$

Now interchange the names of the dummy indices $i$ and $j$:

$$\varepsilon_{ijk}\partial_i\partial_jF_k
= \varepsilon_{jik}\partial_j\partial_iF_k
= -\varepsilon_{ijk}\partial_i\partial_jF_k ,$$

using $\varepsilon_{jik} = -\varepsilon_{ijk}$ (an odd permutation) and
$\partial_j\partial_i = \partial_i\partial_j$ (Clairaut–Schwarz, which needs
$\mathbf{F}$ to be $C^2$). A quantity equal to its own negative is zero:

$$\varepsilon_{ijk}\partial_i\partial_jF_k = 0 . \qquad\square$$

**The two ingredients are exactly the two hypotheses**: antisymmetry of
$\varepsilon_{ijk}$, which is algebra, and symmetry of the mixed second
derivatives, which is a smoothness assumption. Where one of them fails — at a
singularity, or for a field with only one derivative — the identity can fail too.
It does not fail at a singularity in this case, because the cancellation is
algebraic; but the same interchange argument applied to $\nabla\cdot(\hat{r}/r^2)$
is not available, because that field is not $C^2$ at the origin, and the result is
$4\pi\delta^3$ rather than zero.

---

## ★3 — $\nabla\times\nabla f = \mathbf{0}$

$$(\nabla\times\nabla f)_i = \varepsilon_{ijk}\partial_j\partial_kf .$$

Interchanging $j$ and $k$ gives
$\varepsilon_{ikj}\partial_k\partial_jf = -\varepsilon_{ijk}\partial_j\partial_kf$,
so the quantity equals its own negative and therefore vanishes. $\square$

**Hypothesis.** $f \in C^2$, so that $\partial_j\partial_kf =
\partial_k\partial_jf$. This is the Clairaut–Schwarz theorem stated in
[01-06-01](../01-partial-derivatives.md) Section 2.2, and it is not a formality: for
a function whose second partials exist but are discontinuous, the mixed partials
can differ, and the identity fails pointwise. All the potentials of this
curriculum are $C^2$ away from their sources.

---

## ★4 — The Laplacian of a radial function

**(a)** In spherical coordinates, for $F = F(r)$ with no angular dependence, the
Laplacian reduces to the radial part:

$$\nabla^2F = \frac{1}{r^2}\frac{d}{dr}\left(r^2\frac{dF}{dr}\right)
= \frac{1}{r^2}\left(2rF' + r^2F''\right) = F''(r) + \frac{2}{r}F'(r) .$$

**Verification that this is not a different formula from the Cartesian one.**
Apply it to $F = x^2$ considered as a function on the $x$ axis: at the point
$(x,0,0)$, $r = x$ and $F(r) = r^2$, so $F'' + 2F'/r = 2 + 2(2r)/r = 6$. The
Cartesian Laplacian of $x^2$ is $2$ — **not 6** — because $F(r) = r^2$ is a
*different function* from $x^2$; it equals $x^2+y^2+z^2$. Consistently,
$\nabla^2(x^2+y^2+z^2) = 6$ ✓. The apparent discrepancy is a reminder that
"radial function" means a function of $r$, not a function of $x$.

**(b)** For $F = r^n$: $F' = nr^{n-1}$, $F'' = n(n-1)r^{n-2}$, so

$$\nabla^2r^n = n(n-1)r^{n-2} + 2nr^{n-2}
= n(n+1)r^{n-2} .$$

This vanishes for $n = 0$ (the constant) and $n = -1$.

**(c)** $n = -1$ means $F = 1/r$ is harmonic for every $r > 0$. Since the
gravitational potential of a point mass is $V = GM/r$, it satisfies Laplace's
equation wherever there is no mass — which is the whole of potential theory in one
sentence. The fact that $n = -1$ and not some other power is **forced** by the
three-dimensional Laplacian: in $d$ dimensions the harmonic power would be
$2-d$. The inverse-square force law is a consequence of living in three spatial
dimensions.

---

## ★★5 — The curl–curl identity, step by step

Write $\mathbf{G} = \nabla\times\mathbf{F}$, so $G_k = \varepsilon_{klm}
\partial_lF_m$. Then

$$(\nabla\times\mathbf{G})_i = \varepsilon_{ijk}\partial_jG_k
\ \ \text{(definition of the curl)}$$

$$= \varepsilon_{ijk}\partial_j\left(\varepsilon_{klm}\partial_lF_m\right)
\ \ \text{(substituting } G_k\text{)}$$

$$= \varepsilon_{ijk}\varepsilon_{klm}\,\partial_j\partial_lF_m
\ \ \text{(}\varepsilon\text{ is constant in Cartesian coordinates)}$$

$$= \varepsilon_{kij}\varepsilon_{klm}\,\partial_j\partial_lF_m
\ \ \text{(cyclic permutation of the first symbol)}$$

$$= \left(\delta_{il}\delta_{jm} - \delta_{im}\delta_{jl}\right)
\partial_j\partial_lF_m
\ \ \text{(the Levi-Civita contraction)}$$

$$= \partial_j\partial_iF_j - \partial_j\partial_jF_i
\ \ \text{(sifting by the deltas)}$$

$$= \partial_i\left(\partial_jF_j\right) - \partial_j\partial_jF_i
\ \ \text{(Clairaut--Schwarz)}$$

$$= \left[\nabla(\nabla\cdot\mathbf{F})\right]_i -
\left[\nabla^2\mathbf{F}\right]_i .$$

Hence $\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) -
\nabla^2\mathbf{F}$ ✓.

**Two notes.** (i) The cyclic permutation $\varepsilon_{ijk} = \varepsilon_{kij}$
is legitimate because the Levi-Civita symbol is unchanged by an even permutation.
Using $\varepsilon_{ijk} = \varepsilon_{jki}$ would be equally valid; using an odd
one would flip the sign and give the wrong identity. (ii) The step from
$\partial_j\partial_iF_j$ to $\partial_i\partial_jF_j$ is Clairaut–Schwarz, so the
identity again requires $C^2$ smoothness.

---

## ★★6 — Separating the elastic wave equations

**(a)** Substitute $\nabla^2\mathbf{u} = \nabla(\nabla\cdot\mathbf{u}) -
\nabla\times(\nabla\times\mathbf{u})$ into

$$\mu\nabla^2\mathbf{u} + (\lambda+\mu)\nabla(\nabla\cdot\mathbf{u})
= \rho\,\partial_t^2\mathbf{u}:$$

$$\left(\lambda + 2\mu\right)\nabla(\nabla\cdot\mathbf{u})
- \mu\,\nabla\times(\nabla\times\mathbf{u})
= \rho\,\partial_t^2\mathbf{u} . \tag{$\ast$}$$

**Divergence of ($\ast$).** Since $\nabla\cdot\nabla(\nabla\cdot\mathbf{u}) =
\nabla^2(\nabla\cdot\mathbf{u})$ and $\nabla\cdot(\nabla\times\mathbf{w}) = 0$ for
any $\mathbf{w}$ (Section ★2),

$$\left(\lambda+2\mu\right)\nabla^2\left(\nabla\cdot\mathbf{u}\right)
= \rho\,\partial_t^2\left(\nabla\cdot\mathbf{u}\right)
\qquad\Longrightarrow\qquad
v_p = \sqrt{\frac{\lambda+2\mu}{\rho}} .$$

**Curl of ($\ast$).** The gradient term vanishes on curl, and with
$\mathbf{w} = \nabla\times\mathbf{u}$ (which is divergence-free, so
$\nabla\times(\nabla\times\mathbf{w}) = -\nabla^2\mathbf{w}$),

$$\mu\nabla^2\mathbf{w} = \rho\,\partial_t^2\mathbf{w}
\qquad\Longrightarrow\qquad
v_s = \sqrt{\frac{\mu}{\rho}} .$$

**(b)** $v_p = \sqrt{(\lambda+2\mu)/\rho}$ and $v_s = \sqrt{\mu/\rho}$.

**(c)** With $\lambda = \mu = 3.0\times10^{10}$ Pa and
$\rho = 2700\ \mathrm{kg\,m^{-3}}$:

$$v_p = \sqrt{\frac{(3.0 + 6.0)\times10^{10}}{2700}} = \sqrt{1.1111\times10^{7}}
= 5773.5\ \mathrm{m\,s^{-1}},$$

$$v_s = \sqrt{\frac{3.0\times10^{10}}{2700}} = \sqrt{1.1111\times10^{7}}
= 3333.3\ \mathrm{m\,s^{-1}} .$$

**(d)**

$$\frac{v_p}{v_s} = \sqrt{\frac{\lambda+2\mu}{\mu}} = \sqrt{3} = 1.73205
\quad\text{when } \lambda = \mu,$$

and

$$\nu = \frac{(v_p/v_s)^2 - 2}{2\left[(v_p/v_s)^2-1\right]}
= \frac{3-2}{2(3-1)} = \frac{1}{4} = 0.25 .$$

**Poisson's ratio $= 0.25$ is the value expected when $\lambda = \mu$**, which is
what "Poisson solid" means. The agreement confirms self-consistency: the formula
for $\nu$ was not used to derive $\sqrt{3}$, so the two matching is a genuine
check.

**Why this matters.** The separation is not a numerical convenience; it is an
algebraic decoupling. P energy has $\nabla\times\mathbf{u} = \mathbf{0}$ and S
energy has $\nabla\cdot\mathbf{u} = 0$, so the two attributes measure the two
modes directly in an isotropic medium — and only there (see Section 4 of the
lesson on anisotropy).

---

## ★★7 — The electromagnetic diffusion and wave equations

**(a)** Taking the curl of Faraday's law, substituting Ampère's law and using
$\nabla\cdot\mathbf{E} = 0$ (as in the lesson, Section 3.4):

$$\nabla^2\mathbf{E} = \mu\sigma\,\partial_t\mathbf{E}
+ \mu\varepsilon\,\partial_t^2\mathbf{E} .$$

The ratio of the second term to the first is $\varepsilon\omega/\sigma$.
**Low frequency (or high conductivity): the first term dominates and the equation
is diffusive.** **High frequency (or low conductivity): the second term dominates
and the equation is a wave equation.** The crossover is

$$\varepsilon\omega/\sigma = 1
\qquad\Longrightarrow\qquad
f_c = \frac{\sigma}{2\pi\varepsilon} .$$

For a rock with $\sigma = 0.01\ \mathrm{S\,m^{-1}}$ and relative permittivity
$10$, $\varepsilon = 8.854\times10^{-11}$ F/m and

$$f_c = \frac{0.01}{2\pi(8.854\times10^{-11})} = 1.8\times10^{7}\ \mathrm{Hz},$$

far above the $10^{-3}$–$10^{3}$ Hz band used by EM exploration methods. Hence
**EM fields in the Earth diffuse**, and treating them as waves is a serious
misinterpretation; GPR, operating at $10^{7}$–$10^{9}$ Hz, is genuinely in the
wave regime and needs the second term.

**(b)** For $\mathbf{E}\propto e^{i(kz-\omega t)}$, $\nabla^2\mathbf{E} = -k^2\mathbf{E}$
and $\partial_t\mathbf{E} = -i\omega\mathbf{E}$. Retaining only the diffusive term,

$$-k^2 = \mu\sigma(-i\omega)
\qquad\Longrightarrow\qquad
k^2 = i\omega\mu\sigma .$$

Then

$$k = \sqrt{i\omega\mu\sigma} = (1+i)\sqrt{\frac{\omega\mu\sigma}{2}}
= \frac{1+i}{\delta}, \qquad
\delta = \sqrt{\frac{2}{\omega\mu\sigma}} .$$

The equality $\sqrt{i} = (1+i)/\sqrt{2}$ is worth checking once: squaring
$(1+i)/\sqrt2$ gives $(1 + 2i + i^2)/2 = i$ ✓.

**(c)** With $\mu = \mu_0$:

| $T$ (s) | $\sigma$ (S/m) | $\omega$ (rad/s) | $\delta$ (m) |
|---|---|---|---|
| 100 | 0.02 | 0.0628319 | 35588 |
| 10 | 0.5 | 0.628319 | 2251 |

$$\delta(100\ \mathrm{s}, 0.02\ \mathrm{S/m}) = \sqrt{\frac{2}{(0.0628319)
(1.25664\times10^{-6})(0.02)}} = 3.5588\times10^{4}\ \mathrm{m} = 35.6\ \mathrm{km},$$

$$\delta(10\ \mathrm{s}, 0.5\ \mathrm{S/m}) = \sqrt{\frac{2}{(0.628319)
(1.25664\times10^{-6})(0.5)}} = 2.2508\times10^{3}\ \mathrm{m} = 2.25\ \mathrm{km}.$$

**(d)** Long-period MT sounds deeper because $\delta \propto 1/\sqrt{\omega}$: the
depth to which the field penetrates grows without bound as the period lengthens,
so the period band chosen for a sounding **is** the depth range being probed. This
single scaling is the operational basis of magnetotellurics.

---

## ★★8 — Poisson's equation from the delta function

Start with

$$V(\mathbf{r}) = G\iiint\frac{\rho(\mathbf{r}')}{\lvert\mathbf{r}-\mathbf{r}'\rvert}\,dV'$$

and apply the Laplacian in $\mathbf{r}$, moving it inside the integral (legitimate
for a density that is integrable and bounded):

$$\nabla^2V(\mathbf{r}) = G\iiint\rho(\mathbf{r}')\,
\nabla^2\left(\frac{1}{\lvert\mathbf{r}-\mathbf{r}'\rvert}\right)dV' .$$

Using the identity of Section 3.7 of the lesson,

$$\nabla^2\left(\frac{1}{\lvert\mathbf{r}-\mathbf{r}'\rvert}\right)
= -4\pi\delta^3(\mathbf{r}-\mathbf{r}'),$$

and then the **sifting property** of the delta function,
$\iiint f(\mathbf{r}')\delta^3(\mathbf{r}-\mathbf{r}')\,dV' = f(\mathbf{r})$,

$$\nabla^2V(\mathbf{r}) = -4\pi G\iiint\rho(\mathbf{r}')
\delta^3(\mathbf{r}-\mathbf{r}')\,dV'
= -4\pi G\rho(\mathbf{r}) .$$

**The two ingredients** are (i) the delta identity, which encodes why the
inverse-distance kernel is the Green's function of the Laplacian in three
dimensions, and (ii) the sifting property, which is the definition of the delta.
No symmetry, shape or approximation entered — which is why the result holds for any
density distribution whatsoever.

---

## ★★★9 — Numerical verification of the identities

**Method.** Test fields $f = x^2y+y^2z+z^2x$, $\mathbf{F} = (xy+z^2, yz+x^2, zx+y^2)$,
evaluated at $(0.7,-0.4,1.1)$ with central differences at step $H$. The residual
is the norm of the difference between the two sides of the identity, and the
reference scale is the norm of the computed left-hand side.

**(a)** At $H = 10^{-3}$:

| identity | residual | reference scale | ratio |
|---|---|---|---|
| $\nabla\times(\nabla\times\mathbf{F}) = \nabla(\nabla\cdot\mathbf{F}) - \nabla^2\mathbf{F}$ | $1.755\times10^{-10}$ | $1.732$ | $1.013\times10^{-10}$ |
| $\nabla\times\nabla f = \mathbf{0}$ | $0.000$ | — | $0$ |

**(b)** The residual against step, over a wider sweep than the four values the
exercise asked for:

| $H$ (m) | curl–curl residual | $\lvert\nabla\times\nabla f\rvert$ |
|---|---|---|
| $10^{0}$ | $8.006\times10^{-16}$ | $0.0$ |
| $3\times10^{-1}$ | $1.570\times10^{-15}$ | $2.22\times10^{-16}$ |
| $10^{-1}$ | $1.072\times10^{-14}$ | $5.55\times10^{-16}$ |
| $3\times10^{-2}$ | $1.436\times10^{-13}$ | $2.09\times10^{-15}$ |
| $10^{-2}$ | $2.238\times10^{-12}$ | $0.0$ |
| $3\times10^{-3}$ | $1.883\times10^{-11}$ | $2.07\times10^{-14}$ |
| $10^{-3}$ | $1.755\times10^{-10}$ | $0.0$ |
| $3\times10^{-4}$ | $1.981\times10^{-9}$ | $2.78\times10^{-13}$ |
| $10^{-4}$ | $8.886\times10^{-9}$ | $0.0$ |
| $10^{-5}$ | $2.737\times10^{-6}$ | $0.0$ |

**The residual does not converge as $H\to0$; it grows**, by a factor of roughly 10
to 300 per decade in $H$. The smallest residual in the whole sweep is at the
*largest* step. The explanation is round-off, not truncation: the identity is
built from nested second-order operators, so evaluating it involves differences of
numbers of size $\sim1$ divided by $H^2$ (and by $H^3$ in the inner operator), and
the round-off term scales as $\epsilon_m/H^{2}$ to $\epsilon_m/H^{3}$. At
$H = 10^{-3}$ that is $10^{-10}$ to $10^{-7}$; at $H = 10^{-5}$, $10^{-6}$ to
$10^{-1}$. The measured values sit in those ranges.

The growth is not a clean power law because several cancellation terms of
different magnitudes contribute, so a fitted exponent would be an artefact. **What
the table establishes is which of the two error sources dominates**, and the
answer is unambiguous: round-off, at every step accessible.

**(c)** $\lvert\nabla\times\nabla f\rvert$ is **zero at several steps and at
round-off level at others** — $2.8\times10^{-13}$ at the worst, in a field of
scale 1.7. It never approaches truncation-error size, and no convergence rate
applies or exists.

Why: in exact arithmetic the cancellation is *algebraic*. The $z$ component of
$\nabla\times\nabla f$ is built from two nested differences that contain the same
four function values, so the two expressions are identical sums; in floating point
the additions happen in a different order, and the difference between the two
orders is a few units in the last place. **The residual is therefore a statement
about floating-point addition, not about the identity.**

**(d)** The two cases show what a numerical check of an identity can and cannot
establish.

- When the identity is a **cancellation between different stencils** (case b), the
  residual is a genuine measure of how well the discretisation approximates the
  continuum statement, and its behaviour with $H$ is informative — but the measured
  residual is a property of the *scheme*, not of the identity, and here it is
  dominated by round-off rather than truncation.
- When the identity is **exact for the discrete operator** (case c), the zero
  residual is evidence that the stencils are mutually consistent — a code whose
  discrete $\nabla\times\nabla f$ is not zero has a bug — but it is *no evidence at
  all* about the identity itself, because it cancels term by term.

Neither case is worthless. Consistency checks (c) catch implementation errors;
convergence checks (b) test the approximation. What is illegitimate is to present
a zero residual from a case-(c) identity as confirmation that the field is smooth
or that the identity holds — and that is precisely the trap demonstrated in
[01-06-07](../07-vector-identities.md), Section 5.4.

---

## ★★★10 — The delta function is not a pointwise statement

**(a)** With $\mathbf{F} = \hat{r}/r^2$,

$$\nabla\cdot\mathbf{F}
= \frac{1}{r^2}\frac{\partial}{\partial r}\left(r^2\cdot\frac{1}{r^2}\right)
= \frac{1}{r^2}\frac{\partial}{\partial r}(1) = 0
\qquad\text{for every } r > 0 .$$

**(b)** On a sphere of radius $R$, $\mathbf{F}\cdot\hat{r} = 1/R^2$ and
$dA = R^2\sin\theta\,d\theta\,d\phi$, so

$$\oint\mathbf{F}\cdot d\mathbf{A}
= \frac{1}{R^2}\cdot R^2\oint\sin\theta\,d\theta\,d\phi
= 4\pi,$$

**independent of $R$** — the value $4\pi$ does not even contain $R$.

**Measured confirmation** (from the module demonstration, midpoint rule with
$n = 400$ in each angle): the flux was $12.566402913$ for $R = 0.5$, $2$ and $10$
m, against $4\pi = 12.566370614$ — a relative residual of
$2.57\times10^{-6}$, the same for all three radii. **The identical value at three
radii is the point:** a quadrature artefact would vary with $R$; the physics does
not.

**(c)** A central-difference divergence at $\mathbf{r} = (0.7,-0.4,1.1)$ returned
$3.709\times10^{-7}$ — the $O(H^2)$ truncation error of the stencil at $H = 10^{-3}$
for a field whose natural scale is $1/r^3$ at $r \approx 1.4$, i.e. about $0.4$.
So the measured value is $10^{-6}$ of the scale, a numerical zero.

**Why this does not contradict (b).** The divergence is zero *pointwise* — at
every point where it can be evaluated — and its **integral over any volume
containing the origin is $4\pi$**. A function that vanishes everywhere except at a
single point, yet has a nonzero integral, is a delta function. The pointwise value
and the integral are both correct, and they are different statements. Concretely,

$$\nabla\cdot\left(\frac{\hat{r}}{r^2}\right) = 4\pi\delta^3(\mathbf{r})$$

holds in the sense of distributions, and the correct way to verify it is to
integrate, not to differentiate.

**(d)** Measured Laplacian of $1/r$ by central differences with $H = 10^{-3}$:

| $r$ (m) | measured $\nabla^2(1/r)$ | analytic value |
|---|---|---|
| 0.500 | $1.120\times10^{-4}$ | 0 |
| 0.050 | $1.120\times10^{1}$ | 0 |
| 0.005 | $1.131\times10^{6}$ | 0 |

The analytic value is zero at every one of those points, yet the computed value
grows by a factor of $10^{5}$ for each factor of 10 in $r$, i.e. as $r^{-5}$.

**Why.** With $H$ fixed at $10^{-3}$ m and the field varying on the scale $r$, the
stencil spans a relative interval $2H/r$. When $r \gg H$ the finite difference is
an accurate approximation to a zero second derivative plus a truncation error of
order $H^2 f'''' \sim H^2/r^5$. At $r = 0.5$: $10^{-6}/0.03125 \approx
3\times10^{-5}$, the size measured. At $r = 0.005$: $10^{-6}/(0.005)^5 =
3.2\times10^{5}$, the size measured. **The polynomial growth is exactly the
predicted truncation error, so nothing pathological is happening — the stencil is
simply being asked to resolve a function that varies on a scale 200 times smaller
than its own step.**

**What it demonstrates about finite differences.** A finite-difference operator
evaluated at a point where the field is analytic can differ arbitrarily from the
analytic value, and the failure becomes unbounded as the length scale of the field
decreases towards the step size. A numerical test of an identity involving
derivatives of a singular field therefore verifies nothing unless the step is
chosen relative to the smallest length scale present — and for $1/r$ near the
origin, no fixed step can be.

**The one thing that *is* verified.** The flux result in (b) is an *integral*
statement, and integral statements are insensitive to how badly the integrand is
resolved locally, provided the quadrature captures the total. That is why the
integral form of Gauss's law is the one to compute with, and the differential form
the one to be careful with.
