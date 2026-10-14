# Solutions — 01-12-04 Numerical Integration: Trapezoid, Simpson, Gauss Quadrature

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed. Where an entry is quoted from the module's Romberg table
> it is identified.

---

## ★1 — Trapezoid and Simpson with four panels

$h = 0.25$; nodal values $\mathrm e^{0}=1$, $\mathrm e^{0.25}=1.284025$,
$\mathrm e^{0.5}=1.648721$, $\mathrm e^{0.75}=2.117000$, $\mathrm e^{1}=2.718282$.

**Trapezoid:**

$$T_4 = 0.25\left[\tfrac12(1) + 1.284025 + 1.648721 + 2.117000
+ \tfrac12(2.718282)\right] = 0.25(6.908887) = 1.7272219,$$

error $|1.7272219 - 1.7182818| = \boxed{8.940\times10^{-3}}$.

**Simpson (even $n$, Simpson applies directly):**

$$S_4 = \frac{0.25}{3}\left[1 + 4(1.284025) + 2(1.648721) + 4(2.117000)
+ 2.718282\right] = \frac{0.25}{3}(20.619825) = 1.7183188,$$

error $\boxed{3.701\times10^{-5}}$.

Simpson is 240 times more accurate with the same five function values. The reason
is the order: $T_4$ is $O(h^2)$ and $S_4$ is $O(h^4)$.

---

## ★2 — Degree of exactness of the 3-point Gauss rule

An $n$-point Gauss–Legendre rule is exact to degree $2n-1$, so for $n=3$ the
degree is $\boxed{5}$.

$$\int_{-1}^{1}x^4\,dx = \frac{2}{5} = 0.4 \quad\text{(computed: }0.4000000000)$$

$$\int_{-1}^{1}x^6\,dx = \frac{2}{7} = 0.2857142857
\quad\text{(computed: }0.2400000000)$$

The $x^4$ integral is exact; the $x^6$ integral is not, and the error is
$4.571\times10^{-2}$ — the same value the demonstration's exactness table shows at
$p=2n=6$ for $n=3$. The first failure occurring exactly at $p=2n$ is the
definition of the rule, so this verifies the *node generation*, not the theory.

---

## ★3 — Simpson's rule and its error term

Interpolate $f$ at three equispaced nodes $a$, $m=(a+b)/2$, $b$ with Lagrange
polynomials of $h=(b-a)/2$ and integrate:

$$\int_a^b p_2\,dx = \frac{h}{3}\left[f(a)+4f(m)+f(b)\right].$$

This is exact for quadratics (it is an interpolatory rule with three nodes) and,
by symmetry, also exact for cubics: the cubic term $c_3(x-m)^3$ is odd about the
midpoint and integrates to zero. So the degree of exactness is 3.

**Error.** Expand about the midpoint with $x = m+sh$:

$$\int_{-1}^{1}\left[f(m)+sh\,f'(m)+\frac{s^2h^2}{2}f''(m)
+\frac{s^3h^3}{6}f'''(m)+\frac{s^4h^4}{24}f''''(m)+\cdots\right]h\,\mathrm ds$$

The odd terms vanish. The rule is exact for the constant, $s^2$ and $s^3$ terms,
so the residual comes from $s^4$ and higher:

$$\text{error} = h^5f''''(m)\left[\int_{-1}^{1}\frac{s^4}{24}\mathrm ds
- \frac{1}{3}\left(0+4\left(\tfrac12\right)^4\text{ contribution}\right)\right].$$

Carrying out the arithmetic ($\int_{-1}^{1}s^4\mathrm ds = 2/5$, and the rule's
reproduction of $s^4$ is $4(1/16)/3 = 1/12$ per unit $h^5$):

$$I - S_2 = h^5f''''(m)\left(\frac{1}{12}-\frac{1}{12}\right)
- \frac{h^5}{90}\cdot\frac{2}{2}f''''(\xi) + \cdots
= -\frac{h^5}{90}f''''(\xi) = -\frac{(b-a)^4}{2880}f''''(\xi),$$

which is the standard $-h^4f''''/180$ per panel written with $h=(b-a)/2$ for a
composite panel of width $2h$. **The mechanism to remember:** the rule is exact to
degree 3, so the leading error is proportional to the fourth derivative and to
$h^5$ per panel, i.e. $O(h^4)$ per panel and $O(h^4)$ in the composite error.

---

## ★4 — The Bouguer slab

$$g_z = 2\pi G\rho t = 2\pi(6.674\times10^{-11})(2670)(200)
= 2.2393\times10^{-4}\ \mathrm{m\,s^{-2}} = \boxed{22.3927\ \text{mGal}}.$$

**Which limit it is.** The slab is the $L\to\infty$ limit of a quadrature over a
plate of half-width $L$. The quadrature result is always *less* than the infinite
slab value, and the deficit falls as $t/L$ for a thin plate (and slowly, as
$\ln$ for very thin ones), which is why a Bouguer correction applied without a
finite-extent check systematically over-corrects. The limit is not merely an
analytic curiosity: it is the reference against which the quadrature is scored,
exactly as the point-mass limit is used for the ellipsoid in the lesson.

---

## ★★5 — Only even powers of $h$ appear

Write $f$ as a Taylor series about $b$ and integrate panel by panel: for a panel
$[b-h,b]$,

$$\int_{b-h}^{b}f\,\mathrm dx = hf(b) - \frac{h^2}{2}f'(b) + \frac{h^3}{6}f''(b)
- \frac{h^4}{24}f'''(b) + \cdots,$$

while the trapezoid estimate of that panel is

$$T = \frac{h}{2}\left[f(b-h)+f(b)\right] = hf(b) - \frac{h^2}{2}f'(b)
+ \frac{h^3}{4}f''(b) - \frac{h^4}{12}f'''(b)+\cdots$$

Subtracting, the panel error is

$$I_{\text{panel}} - T_{\text{panel}} = h^3\left(\frac16-\frac14\right)f''(b)
+ h^4\left(-\frac{1}{24}+\frac{1}{12}\right)f'''(b)+\cdots
= -\frac{h^3}{12}f''(b) + \frac{h^4}{24}f'''(b)+\cdots$$

The $h^3$ term is the leading panel error. Summing over $n$ panels and using
$\sum_i h^3 f''(x_i) \to h^2\int f''\,dx = h^2[f'(b)-f'(a)]$, the leading term
becomes $-\frac{h^2}{12}[f'(b)-f'(a)]$, which is $O(h^2)$ with no $O(h)$ term —
the odd-order terms cancel pairwise because each panel contributes with the
opposite sign to its neighbour. The next contribution is $O(h^4)$, and the pattern
continues: **only even powers appear**. That is exactly the property Romberg
extrapolation exploits, and it is why one Richardson level buys *two* orders
rather than one.

---

## ★★6 — Eight digits from the Romberg table

The lesson's table of errors is

| level $j$ | entries (errors) |
|---|---|
| 0 | $1.409\times10^{-1}$, $3.565\times10^{-2}$, $8.940\times10^{-3}$, $2.237\times10^{-3}$, $5.593\times10^{-4}$, $1.398\times10^{-4}$ |
| 1 | $5.793\times10^{-4}$, $3.701\times10^{-5}$, $2.326\times10^{-6}$, $1.456\times10^{-7}$, $9.103\times10^{-9}$ |
| 2 | $8.595\times10^{-7}$, $1.376\times10^{-8}$, $2.163\times10^{-10}$, $3.384\times10^{-12}$ |
| 3 | $3.355\times10^{-10}$, $1.344\times10^{-12}$, $4.663\times10^{-15}$ |
| 4 | $3.375\times10^{-14}$, $6.661\times10^{-16}$ |

Eight digits means an error below $5\times10^{-9}$. The first entry that achieves
it is $j=2$, $k=3$ with an error of $3.384\times10^{-12}$ — comfortably better, so
the answer to eight digits is

$$\int_0^1\mathrm e^x\,dx = 1.71828183 \quad (\pm 4\times10^{-9} \text{ from the nearest worse entry } 8.595\times10^{-7}\cdot),$$

i.e. the 8-digit value is $1.71828183$.

**Why the next level does not help.** Level 4's entries are $3.375\times10^{-14}$
and $6.661\times10^{-16}$: the second is at the round-off floor of double
precision for a value of order 1.7 (the unit roundoff is $2.2\times10^{-16}$, and
the accumulated cancellation in the extrapolation amplifies it). Refining further
produces numbers that scatter rather than converge, and the measured orders in the
lesson (7.96 at level 3, then nothing usable) show the boundary. This is the
general rule for extrapolation methods: **they buy orders until they hit the
arithmetic's floor, and then they stop.**

---

## ★★7 — An improper integral three ways

$I = \int_0^1x^{-1/2}\,dx = \left[2x^{1/2}\right]_0^1 = 2$ exactly.

**(a) Trapezoid with the endpoint value omitted** (taking $f(0)=0$): with
$n = 10^5$ the computed value is $1.9953819536$, an error of
$\boxed{4.618\times10^{-3}}$. The convergence is poor — $O(h^{1/2})$ rather than
$O(h^2)$ — because the integrand's derivative is unbounded at $x=0$, so the panel
error near the endpoint is not $O(h^3)$ but $O(h^{3/2})$.

**(b) Substitution** $x=t^2$, $\mathrm dx = 2t\,\mathrm dt$, so

$$\int_0^1x^{-1/2}\mathrm dx = \int_0^12\,\mathrm dt = 2,$$

and Simpson on a constant integrand is exact with any even panel count: the
computed value is $\boxed{2.0000000000}$, error exactly 0. For comparison, applying
Simpson directly in $x$ with 8 panels and $f(0)=0$ gives $1.5549722281$, an error
of 0.445. **The substitution is not a numerical trick; it is a change of variable
that removes the singularity**, and it converts a problem with algebraic
convergence into one solved exactly.

**(c) Gauss–Legendre directly on $[0,1]$:** with 4 nodes the computed value is
$1.8063425404$ (error $1.937\times10^{-1}$, 9.7%) and with 8 nodes
$1.8975409492$ (error $1.025\times10^{-1}$, 5.1%).

**Ranking and explanation.** substitution (exact) $>$ trapezoid with endpoint
omitted ($4.6\times10^{-3}$) $>$ Gauss-8 ($1.0\times10^{-1}$) $>$ Gauss-4
($1.9\times10^{-1}$). The Gauss rules are **the worst of the three**, defying the
usual ranking, and the reason is structural: the Gauss error theory requires
analyticity on the closed interval, whereas this integrand has an infinite
derivative at an endpoint. Quadrupling the node count only halves the error —
algebraic convergence, not geometric. The trapezoid rule, which at least has a
node structure that can be refined toward the singularity, does better; and the
substitution does best of all because it removes the difficulty rather than
fighting it.

*(The numeric values here were computed with the module's own quadrature routines,
so the comparison is internal to one implementation.)*

---

## ★★8 — Node counts from the measured error table

The lesson's relative errors are $1.021\times10^{-4}$ at $n_r=n_\mu=4$,
$1.252\times10^{-8}$ at 8, $1.632\times10^{-12}$ at 12 and
$1.634\times10^{-16}$ at 16. Each increment of 4 in the node count multiplies the
error by roughly $10^{-4}$, i.e. the convergence is **geometric** in $n$:

$$\log_{10}\text{error} \approx -4 - 1.05(n-4).$$

For a relative error of $0.01\% = 10^{-4}$ the measured table already reaches
$1.02\times10^{-4}$ at $n=4$ — so $n_r = n_\mu = 4$ is sufficient at that level,
and the answer to "$\pm1\%$ needs the next refinement" is a misreading: the 1%-low
result quoted in the question must have come from a different integrand or a
different (unconverged) implementation, not from geometric convergence at $n=4$.

Taking the question at face value and using the measured sequence: to move from
$10^{-2}$ (1%) to $10^{-4}$ (0.01%) requires **one** increment of the node count,
i.e. $n_r=n_\mu=8$, which the table places at $1.25\times10^{-8}$ — comfortably
inside the target with margin.

**The assumption.** That the integrand is analytic on the closed region of
integration, so that Gauss convergence is geometric. That assumption is precisely
what fails when the observation point approaches the body: the kernel
$1/\lvert\mathbf r-\mathbf r'\rvert^2$ becomes singular, the convergence degrades
to algebraic, and no measured table can be extrapolated to a new geometry. This is
why the lesson insists that an error table is a statement about one integrand, not
about the method.

---

## ★★★9 — Finite-plate Bouguer quadrature

**Setup.** Observation at the centre of the top surface of a plate occupying
$x,y\in[-L,L]$, $z\in[-t,0]$:

$$g_z = G\rho\int_{-t}^{0}\!\!\int_{-L}^{L}\!\!\int_{-L}^{L}
\frac{-z'}{\left(x'^2+y'^2+z'^2\right)^{3/2}}\,\mathrm dx'\,\mathrm dy'\,\mathrm dz' .$$

The limit $L\to\infty$ is $2\pi G\rho t$ exactly, and the ratio
$g_z/(2\pi G\rho t)$ measures the fraction of the infinite slab captured by a
finite plate. For $t=100$ m:

| $L/t$ | behaviour of the ratio | comment |
|---|---|---|
| 1 | well below 1 | a cube-like body: most of the slab is missing |
| 10 | within a few per cent of 1 | the usual working rule of thumb for a "slab" |
| 100 | above 0.999 | the finite-extent correction is negligible |

The approach is slow — the deficit falls roughly as $t/L$ for small $t/L$ (and
logarithmically for very thin plates) — which is the quantitative reason a
regional gravity survey at 10 km scale must correct for the finite extent of a
"regionally compensated" slab, while a 100 km survey generally need not.

**The corner singularity.** The observation point $(0,0,0)$ is a corner of the
integration domain, and the integrand behaves like $1/z'^2$ as $z'\to0$ along the
axis $x'=y'=0$. The integral converges (the volume element supplies enough
powers), but the integrand is *not* analytic on the closed domain, so a single
Gauss–Legendre rule in $z$ converges only algebraically — the same failure
documented in ★★7. The practical remedies are to subdivide the $z$ range and use
composite Gauss, to use a substitution in $z$ that removes the singularity, or to
split the plate into a small disc around the observation point (treated
analytically by the standard thin-disc formula) plus the remainder (treated by
Gauss). In production potential-field code the last route is the standard one.

---

## ★★★10 — Critique of a verification by node count

**What the check does establish.** Increasing 20 nodes to 24 and finding the same
four figures shows that the *quadrature* has converged for the integrand as
implemented. That is necessary and useful: it excludes a mis-transcribed weight,
an integration bound error, and a gross node-generation bug, all of which change
the answer when $n$ changes.

**Why it is not sufficient.** Two reasons, and they are different.

1. **A shared error is invisible to it.** Both runs use the same geometry
  parameterisation, the same density model and the same Jacobian. A missing
  Jacobian factor, a dyke strike measured from the wrong axis, or a dip sign
  convention error appears identically in both runs. The lesson's own ellipsoid
  example is the proof: a missing $r^2$ factor in the Jacobian made the far-field
  ratio approach 3 instead of 1, and *no* change of node count would have revealed
  it — the quadrature was converged and consistently wrong.
2. **Four figures says nothing about the model.** Agreement between two
  discretisations of the same integral establishes the *arithmetic*, not the
  *physics*. A dyke has a closed-form anomaly for the simpler geometries
  (infinite strike, uniform magnetisation, vertical sides), and the honest
  validation is against one of those.

**The two independent checks I would require.**

1. **A closed-form or limit check.** Evaluate the same code on a geometry where
  the answer is known exactly: a sphere (point mass), a semi-infinite slab
  (Bouguer limit), or the far-field multipole limit $g\,d^2/GM\to1$ used in the
  lesson. This tests the kernel, the Jacobian, the units and the sign conventions
  at once. For a dyke specifically, the classic checks are the thick-dyke
  far-field limit (which must reproduce the line-mass field $2G\lambda z/(x^2+z^2)$
  per unit strike length) and the thin-sheet limit.
2. **A convergence study with an order, not a repetition.** Halve the node count
  in a sequence (20, 40, 80, 160) and report the measured order of convergence
  against the expected one for an analytic integrand (geometric for Gauss). Two
  points cannot show a trend; a sequence can, and a *wrong* order immediately
  signals either a singular integrand or a bug. If the expected order is not
  observed, the integrand is not as smooth as assumed — which for a dyke corner is
  exactly the case worth knowing about.
