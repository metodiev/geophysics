# Solutions — 02-08-06 Uniqueness Theorems and Boundary Conditions

> **Read this after attempting the exercises, not before.** Convention:
> $V > 0$, $\mathbf{g} = \nabla V$, so the flux form of Gauss's law reads
> $\oint\mathbf{g}\cdot d\mathbf{A} = -4\pi G M_{\text{enc}}$ with the outward
> normal. Values attributed to the demonstration are its actual output.

---

## ★1 — The exterior Dirichlet problem

**(a)** Find $u$ with $\nabla^2u = 0$ in $\Omega = \{\lvert\mathbf{x}\rvert > a\}$ and
$u = f$ on $\lvert\mathbf{x}\rvert = a$, where $f$ is a prescribed function on the
sphere.

**(b)** $u = O(1/r)$ and $\lvert\nabla u\rvert = O(1/r^2)$ as $r\to\infty$. It excludes
harmonic functions that grow or stay bounded away from zero at infinity.

**(c)** $u = 1$, $u = x$, $u = z^2 - \tfrac12(x^2+y^2)$, $u = 1/r^2$ in the
appropriate sense — all harmonic in $\Omega$; $u = 1$ and $u = x$ do not decay.

**(d)** Because the difference of two solutions would then only have to be a harmonic
function satisfying the homogeneous boundary condition, and there are infinitely many
of those (any decaying-free harmonic function). The boundary condition alone cannot
pin down the behaviour at infinity, and the equation alone admits the whole space of
harmonic functions. Adding regularity at infinity restricts the class so that only the
zero function satisfies both conditions.

---

## ★2 — The exterior Neumann problem

**(a)** $\partial u/\partial n = g$ on $\lvert\mathbf{x}\rvert = a$, where $n$ is the
outward normal of the *domain* $\Omega$, i.e. the normal points inward toward the
source region.

**(b)** The solution is **unique**, with no free additive constant. In the
bounded-domain problem the constant is free because adding a constant to a harmonic
function leaves both the equation and the normal derivative unchanged. Here the
regularity condition $u\to0$ removes that freedom: a constant solution violates
$u = O(1/r)$ unless it is zero, so the constant must be zero.

**(c)** The proof is identical up to the boundary terms of Green's first identity: for
the Dirichlet case the term on $r = a$ vanishes because $w = 0$; for the Neumann case
it vanishes because $\partial w/\partial n = 0$. The term on $r = R$ vanishes in both
cases by the same bound $\lvert\oint_{r=R}w\,\partial w/\partial n\,dS\rvert
\le (A/R)(B/R^2)4\pi R^2 = 4\pi AB/R\to0$.

**(d)** The decay at infinity is exactly what pins the constant: a solution can only
be determined up to a constant if adding a constant keeps the solution in the
admissible class, and the class $u = O(1/r)$ excludes non-zero constants.

---

## ★3 — Gauss's law in flux form

**(a)** $\oint_S\mathbf{g}\cdot d\mathbf{A} = -4\pi G M_{\text{enc}}$, with the
outward normal and $\mathbf{g} = \nabla V$.

**(b)** For a sphere of radius $a$ enclosing mass $M$, with $V = GM/r$:
$\mathbf{g} = -GM\hat{\mathbf{r}}/r^2$, and with the outward normal of the *domain*
pointing inward ($-\hat{\mathbf{r}}$),

$$\oint_{r=a}\frac{\partial V}{\partial n}dS
= \oint_{r=a}\left(-\frac{\partial V}{\partial r}\right)dS
= \oint_{r=a}\frac{GM}{a^2}dS = 4\pi GM .$$

**(c)** In the far field $V = GM/r$; the coefficient $C$ in $V\sim C/r$ is $C = GM$.
So (b) reads $\oint_{r=a}\partial V/\partial n\,dS = 4\pi C$ — the prescribed normal
derivative determines the coefficient of $1/r$ at infinity, and hence (in a gravity
problem) the total mass.

**(d)** Because the divergence theorem applied to $\Omega_R$ gives
$0 = \oint_{r=a}\partial u/\partial n\,dS + \oint_{r=R}\partial u/\partial n\,dS$,
and the second integral does **not** vanish: with $u\sim C/r$,
$\oint_{r=R}\partial u/\partial n\,dS\to-4\pi C$. Requiring the total to be zero gives
$\oint_{r=a}\partial u/\partial n\,dS = 4\pi C \neq 0$. The vanishing-flux condition
$\oint g\,dS = 0$ is correct only for a domain with no boundary at infinity.

---

## ★4 — An annihilator by construction

**(a)** Their densities sum to zero everywhere, so their fields sum to zero. The pair
is an annihilator in the trivial sense of being identically nothing — not a useful
construction, because it is not a *difference between two distinct but equivalent*
sources.

**(b)** $(\rho, t) = (2670, 400)$ and $(5340, 200)$ kg m$^{-3}$/m: both give
$g_z = 4.478\,750\,242702\times10^{-4}$ m s$^{-2}$ (demonstration, to twelve
decimals).

**(c)** The "difference distribution" is $+2670$ kg m$^{-3}$ over a $400$ m slab
minus $+5340$ kg m$^{-3}$ over a $200$ m slab occupying the same space. If the two
slabs are made to coincide (both of thickness $400$ m, with the second counted only
over its top $200$ m), the net density is $+2670$ in the bottom $200$ m and $-2670$
in the top $200$ m. Its field is identically zero.

**(d)** An annihilator is any distribution whose *field* vanishes, regardless of the
sign of its density. Gravity masses are physically positive, which bounds the
*feasible set* but does not remove the annihilator from the *forward operator's*
kernel: the same exclusion statement can be made with a non-negative pair (the
equivalent strata of ★6, which are all positive), at the price of changing the
geometry rather than the sign.

---

## ★5 — Reading the demonstration

**(a)** Maximum $\lvert u_a-u_b\rvert$: $1.290\times10^{-1}$ (10 sweeps),
$7.168\times10^{-5}$ (100), $9.367\times10^{-13}$ (1000), $0$ (4000).

**(b)** Maximum error against the exact series solution: $7.188\times10^{-3}$.

**(c)**

| $h$ (m) | peak $\sigma_h$ (kg m$^{-2}$) | FWHM (m) |
|---|---|---|
| $500$ | $1.061\,033\times10^{5}$ | $3000.0$ |
| $1000$ | $1.591\,549\times10^{5}$ | $2000.0$ |
| $1500$ | $3.183\,099\times10^{5}$ | $1000.0$ |

**(d)** Worst relative difference over the stations and the three depths:
$3.091\times10^{-6}$. At the finest quadrature refinement ($800z_0$ half-width,
$320\,001$ points) the value at $x = 0$, $h = 1000$ m is $1.036\times10^{-10}$.

**(e)** The annihilator's field is at most $1.97\times10^{-12}$ of the peak; its
peak density at the origin is $2.122\,066\times10^{5}$ kg m$^{-2}$, which is $2.00$
times the peak of $\sigma_{500}$.

**(f)** Horizontal derivative relative difference: $4.784\times10^{-10}$.

**(g)** All four slabs give $4.478\,750\,242702\times10^{-4}$ m s$^{-2}$ with relative
deviation $0.0\times10^{0}$.

---

## ★6 — The equivalent stratum

**(a)** The vertical field of a line mass $\lambda$ at depth $z_0$ is
$g_z = 2G\lambda z_0/(x^2+z_0^2)$, whose Fourier transform is
$2\pi G\lambda e^{-\lvert k\rvert z_0}$. A sheet of areal density $\sigma$ at depth
$h$ gives $2Gh\int\sigma(x')/((x-x')^2+h^2)\,dx'$, whose transform is
$2\pi G e^{-\lvert k\rvert h}\tilde\sigma(k)$. Equating:
$\tilde\sigma(k) = \lambda e^{-\lvert k\rvert(z_0-h)}$. Inverting the transform (a
two-sided exponential) gives
$\sigma_h(x) = \tfrac{\lambda}{\pi}\tfrac{z_0-h}{x^2+(z_0-h)^2}$.

**(b)** $\int_{-\infty}^{\infty}\sigma_h\,dx
= \tfrac{\lambda(z_0-h)}{\pi}\cdot\tfrac{\pi}{z_0-h} = \lambda$. It must hold for
every $h$, because the far-field ($k\to0$) behaviour of the field is the monopole,
fixed by the total mass per unit length; a stratum that failed this would produce a
different $1/r$ term and would be distinguishable at large distance.

**(c)** With $h = 1900$ m, $z_0 = 2000$ m, $\lambda = 5.0\times10^8$ kg m$^{-1}$:
$a = z_0-h = 100$ m, so peak $\sigma = \lambda/(\pi a) = 1.591\,549\times10^{6}$
kg m$^{-2}$ and FWHM $= 2a = 200$ m.

**(d)** A peak areal density of $1.59\times10^{6}$ kg m$^{-2}$ over a $200$ m width
implies an effective density of $1.59\times10^{6}/200 = 7958$ kg m$^{-2}$/m
$= 7958$ kg m$^{-3}$ — above any crustal rock, approaching the density of iron-nickel
and well above the inner core's mean. **Pushing the source to within $100$ m of its
true depth demands a physically impossible density**, which is why a well-constrained
depth range for a body's *top* (from geology, or from a borehole) usually ends the
ambiguity in practice. The ambiguity is unbounded in principle and bounded by
geology in application.

---

## ★7 — Uniqueness is not stability

**(a)** Upward continuation by height $h$ multiplies the wavenumber spectrum by
$e^{-\lvert k\rvert h} \le 1$.

**(b)** Downward continuation by depth $h$ multiplies by $e^{+\lvert k\rvert h} \ge 1$.

**(c)** With $\lvert k\rvert = 10^{-2}$ m$^{-1}$ and $h = 1000$ m, $\lvert k\rvert h
= 10$: upward factor $e^{-10} = 4.540\times10^{-5}$; downward factor $e^{+10} =
2.2026\times10^{4}$.

**(d)** The upward operator is bounded by $1$ (indeed by any norm $\le1$, so the
problem is not just well posed but contractive). The downward operator is unbounded:
its operator norm over all wavenumbers is infinite. Both are injective — by the
uniqueness theorem — so both have a unique exact solution for exact data. But for
*inexact* data the downward problem has no continuous dependence on the data, and the
solution moves arbitrarily far for arbitrarily small data perturbations. Uniqueness is
a statement about the number of solutions; conditioning is a statement about how
much the solution moves when the data move. Only the second is destroyed here.

---

## ★8 — Applying the ambiguity

**(a)** The two questions concern different objects. "Is the field unique given
complete surface data?" asks about the harmonic region above the boundary: yes, by
the exterior Dirichlet theorem. "Is the density unique?" asks about the region
*below* the boundary, which the boundary condition never constrains: no. There is no
contradiction because no theorem is being applied to the density. The boundary data
determine everything above them and nothing below them.

**(b)** (i) What constraints were applied — bounds on density, a prescribed depth
range, positivity, a compact-support requirement — and are they geologically
justified? (ii) What regularisation was used, and what would a different one have
produced (the model is a representative, so its fine structure is not data)? (iii)
What is the resolution: over what depth and with what lateral resolution are the
reported density variations actually determined, as opposed to inferred from the
prior? A model reported without these three is not falsifiable.

**(c)** A borehole (or a well-log density) constrains the density at a point and hence
the absolute level of the model; seismic reflection or refraction constrains the depth
of interfaces, which collapses the depth–density trade-off. Gravity gradient data do
*not* help in principle (see (d)). Two other useful measurements: rock samples for
density, and a seismic velocity model for the density–velocity relation, both of
which break the ambiguity by supplying information of a different physical type.

**(d)** **No, in principle.** Gravity gradients are derivatives of a harmonic field
and are themselves harmonic. An annihilator's field vanishes identically above the
survey, and so do all its derivatives: the demonstration confirms this numerically,
with $dg_z/dx$ agreeing between two equivalent sources to $4.8\times10^{-10}$
relative. Gradients improve the *conditioning* (they are more sensitive to shallow,
short-wavelength structure) but leave the null space untouched. The rule of thumb:
the null space is removed only by information the data do not contain.

---

## ★★★9 — The equivalent stratum in the wavenumber domain

**(a)** With $\tilde g(k)$ the transform of the measured vertical field and
$\tilde\sigma(k)$ the transform of the areal density at depth $h$, the sheet's field
has transform $2\pi Ge^{-\lvert k\rvert h}\tilde\sigma(k)$, so

$$\tilde\sigma(k) = \frac{\tilde g(k)}{2\pi G e^{-\lvert k\rvert h}} .$$

**(b)** From (a) directly, dividing by the kernel.

**(c)** The denominator $2\pi Ge^{-\lvert k\rvert h}$ is strictly positive for every
finite $k$ and every $h$, so $\tilde\sigma(k)$ exists for every $k$: the construction
never fails. Since $h$ ranges over a continuum of values, the map
$h\mapsto\sigma_h$ is injective as a family (members differ), and every member is in
the same fibre of the forward operator. The fibre is therefore infinite-dimensional:
the difference of any two members is a non-zero annihilator, and the annihilators
form a linear space closed under multiplication by scalars. No finite parameterisation
can exhaust it.

**(d)** At large $\lvert k\rvert$, $\tilde\sigma(k)\propto e^{\lvert k\rvert h}$ times
the (decaying) field spectrum. Taking $\lvert k\rvert = 0.01$ m$^{-1}$ and a field
amplitude $\tilde g \sim 10^{-5}$ m s$^{-2}$ (a plausible anomaly amplitude spread
over its characteristic wavelength), the required density amplitude is

$$\lvert\tilde\sigma\rvert = \frac{10^{-5}}{2\pi G}e^{0.01h} .$$

At $h = 1000$ m this is $5.25\times10^{8}$ kg m$^{-2}$; at $h = 2000$ m it is
$1.16\times10^{13}$ kg m$^{-2}$; at $h = 5000$ m it is $1.24\times10^{26}$
kg m$^{-2}$ — larger than the mass of the Earth per unit area by many orders of
magnitude. The required density exceeds $10^{6}$ kg m$^{-2}$ (already absurd for a
thin layer) once $e^{0.01h} > 10^{6}\times2\pi G/10^{-5} = 4.19\times10^{6}$, i.e.
$h > 1525$ m. **A $1.5$ km stratum is the practical limit for this anomaly**; deeper
placements demand impossible densities, which is why a depth constraint is so
powerful despite the ambiguity being formally infinite.

---

## ★★★10 — What additional information chooses a model

**(a)** A positivity constraint restricts the feasible set to $\{\rho \ge 0\}$, a
convex cone. It removes any annihilator with negative parts, but annihilators with
purely non-negative density on a *different support* remain: the equivalent strata of
★5 are all non-negative, and each is a different source producing the same field. So
positivity prunes the null space without eliminating it. In practice positivity is
powerful because it removes the *most* absurd alternatives (including all the ones
with the deep, high-density spikes that the exponential amplification demands), and
because it interacts with the data to bound the model from below.

**(b)** In the two-dimensional line-mass case, two *non-negative* distributions can
still be equivalent: $\sigma_h$ and $\sigma_{h'}$ are both positive for every
$h<h'<z_0$ and produce identical fields, as displayed in the demonstration's table
(peaks $1.061\times10^{5}$, $1.592\times10^{5}$ and $3.183\times10^{5}$ kg m$^{-2}$
for $h = 500$, $1000$ and $1500$ m, all with the same field). Physically, positivity
of the density of a *body* in three dimensions does not conflict with equivalence
either, for the same reason: the equivalent stratum can be thickened into a
non-negative three-dimensional body. What positivity *does* forbid is a compact
non-negative body at arbitrary depth with bounded density, which is the practical
constraint.

**(c)** A seismic velocity model supplies a *petrophysical* relation
$\rho = \rho(v)$ (or a set of candidate relations) that constrains the density at
every point where the velocity is known, so the gravity data then determine a
correction to that relation rather than the density itself. This shrinks the feasible
set dramatically and, crucially, the resulting model's resolution follows from the
*seismic* resolution. The assumption it introduces is exactly the density–velocity
relation, which is empirical, lithology-dependent and uncertain; a wrong relation
biases the result systematically, and the bias is invisible in the gravity misfit.

**(d)** A defensible concluding paragraph reads: *The survey is consistent with a
mass excess of $X \pm Y$ kg concentrated between depths $z_1$ and $z_2$, with lateral
extent $L$. The depth range is constrained by [borehole/seismic/geological
evidence]; without it the data would admit an equivalent stratum at any shallower
depth. Inversion with [regularisation] and [positivity] bounds yields the density
contrast presented here, which is one representative of a feasible set; the resolution
analysis shows the density variation is determined at scales $\ge$ [value] and
inferred from the prior below that. Independent [measurement] would test the model by
constraining [parameter].* Every clause answers one of the questions in ★8(b), and
none of them claims more than the data support.
