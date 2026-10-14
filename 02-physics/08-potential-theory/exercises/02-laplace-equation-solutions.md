# Solutions — 02-08-02 Laplace's Equation and Harmonic Functions

> **Read this after attempting the exercises, not before.** Values attributed to the
> demonstration are its actual output.

---

## ★1 — Which functions are harmonic

**(a)** $u = x^2+y^2-2z^2$: $\nabla^2u = 2+2-4 = 0$ — **harmonic everywhere**.

**(b)** $u = x^2-y^2$: $\nabla^2u = 2-2 = 0$ — **harmonic everywhere**. (It is the
real part of $(x+iy)^2$, as any harmonic function in two dimensions is the real or
imaginary part of an analytic function — the connection between Laplace's equation
in 2-D and complex analysis.)

**(c)** $u = 1/r$: $\nabla^2(1/r) = -4\pi\delta^3(\mathbf{r})$ in the
distributional sense, so it is harmonic everywhere **except at the origin**; at the
origin it is not even finite. This is the potential of a point mass up to the factor
$G M$, and the delta function is the whole content of Poisson's equation.

**(d)** $u = e^{-(x^2+y^2+z^2)}$: $\nabla^2u = (4r^2-6)u \neq 0$ — **nowhere
harmonic**. This is the archetype of the trap: infinitely smooth, radially
symmetric, bell-shaped, and emphatically not harmonic. Smoothness is necessary and
nowhere near sufficient.

**(e)** $u = \ln\sqrt{x^2+y^2}$: $\nabla^2u = 0$ for
$\rho = \sqrt{x^2+y^2}\neq0$ — **harmonic away from the $z$ axis**. This is the
two-dimensional Green's function, the potential of a line mass (lesson 01), and the
reason two-dimensional potential theory has a logarithmic kernel.

---

## ★2 — The mean value expansion

**(a)** $\nabla^2f = \partial_x^2(x^2) + \partial_y^2(2y^2) = 2+4 = 6$.

**(b)** $\overline{f} = f(\mathbf{p}) + \frac{R^2}{6}\times6 = f(\mathbf{p}) + R^2$.
With $f(3,-1,0) = 9+2 = 11$ and $R = 1$, $\overline{f} = 12$.

**(c)** Exactly: the sphere mean of $x^2$ about $\mathbf{p}$ is $p_x^2 + R^2/3
= 9 + 1/3$, and of $2y^2$ is $2(p_y^2+R^2/3) = 2(1+1/3) = 2+2/3$. Sum
$= 12$. ✓ The expansion in (b) is exact here to all orders because $f$ is quadratic
and the $O(R^4)$ term vanishes for a quadratic.

**(d)** The mean exceeds the centre value because $f$ is *convex* in the
$x$ and $y$ directions (positive second derivatives), so the average over a sphere
of finite radius samples higher values than the centre. The correction is
proportional to $\nabla^2f$ — exactly the statement that the mean value property
holds if and only if the Laplacian vanishes.

---

## ★3 — $u = x^2-y^2$ on the unit disk

**(a)** $\nabla^2u = 2-2 = 0$ identically.

**(b)** On the boundary $x^2+y^2=1$: write $u = 2x^2-1$ (using $y^2 = 1-x^2$), so
$u$ increases monotonically with $x^2$: maximum $+1$ at $(\pm1,0)$, minimum $-1$ at
$(0,\pm1)$. Both extremes are **on the boundary**, as the maximum principle
requires, and they are attained at two points each.

**(c)** At the centre, the mean over the unit circle is
$\frac{1}{2\pi}\int_0^{2\pi}(\cos^2\theta-\sin^2\theta)d\theta = 0 = u(0,0)$. ✓

**(d)** The disk centred at $(0.5,0)$ with $R = 0.4$ lies in
$x\in[0.1,0.9]$, $y\in[-0.4,0.4]$, where $u$ is harmonic (no singularity anywhere),
so the mean equals the centre value $u(0.5,0) = 0.25$.

---

## ★4 — A mis-levelled line

**(a)** No. A constant offset applied along a finite line is not the boundary value
of any harmonic field above the grid: it is a *discontinuity* in the surface data of
the type the exterior Neumann existence condition (lesson 06, equation 11) excludes.

**(b)** The finite-difference Laplacian of the grid would be large and
*alternating* along and across the line: a positive spike where the line begins, a
long run of near-zero residual inside the line (the offset is locally a constant, so
its second differences vanish there), and a negative spike at the end. A levelling
error therefore shows up as two glitches at the ends of the line rather than as a
uniform error along it, which is why line-end behaviour is examined closely in
quality control.

**(c)** Because the discrete mean value property holds for any harmonic grid and
fails in a measurable, localised way for a mis-levelled one. The test is
dimensionless (it compares a value with a mean of the same kind), needs no
knowledge of the sources, and localises the error. It is the practical face of the
theoretical statement that harmonicity is equivalent to "each value is the average
of its neighbours".

---

## ★5 — Reading the demonstration

**(a)** Source-free sphere, $R = 1000$ m: relative difference $1.0\times10^{-13}$.
Sphere enclosing the source, $R = 200$ m: relative difference **$0.7500$**.

**(b)** Interior maximum $1.337535070140\times10^{-1}$, boundary maximum
$1.337535070140\times10^{-1}$, relative difference $0$. The location is
$(\pm1, 0, 0)$ m — on the boundary, $21$ km from the source at $(500,0,0)$ m.

**(c)** Harmonic function at $h = 100$ m: $-6.920844\times10^{-12}$ s$^{-2}$; at
$h = 12.5$ m: $-1.081524\times10^{-13}$ s$^{-2}$. Ratio $64.0$ over three halvings,
i.e. exactly $4.000$ per halving — second order.

**(d)** $f = x^2$ gives $2.0000000000$ at $h = 100$, $50$ and $25$ m — the exact
Laplacian, because the seven-point stencil is exact for quadratics.

**(e)** (a) mean value property; (b) maximum principle; (c) the finite-difference
test for harmonicity and its second-order accuracy; (d) the contrast between
harmonic and non-harmonic, expressed through the source content
$\nabla^2f = -4\pi G\rho$ (with $\rho\to0$ for the harmonic case).

---

## ★6 — Downward continuation and noise

**(a)** $k = 2\pi/\lambda$ and the amplification is $e^{kd}$ with $d = 1000$ m:

| $\lambda$ | $k$ (m$^{-1}$) | $e^{kd}$ |
|---|---|---|
| $60$ km | $1.0472\times10^{-4}$ | $1.1104$ |
| $6$ km | $1.0472\times10^{-3}$ | $2.8497$ |
| $600$ m | $1.0472\times10^{-2}$ | $3.5312\times10^{4}$ |

**(b)** With $1$ per cent initial noise: $1.110$ per cent, $2.850$ per cent and
$353$ per cent respectively.

**(c)** Set $0.01e^{kd} = 1$: $kd = \ln100 = 4.6052$, so
$k = 4.6052\times10^{-3}$ m$^{-1}$ and $\lambda = 2\pi/k = 1364$ m. At wavelengths
shorter than about $1.4$ km the noise dominates after a $1$ km continuation.

**(d)** The problem remains unique because the operator
$e^{+kd}$ is injective: for every noise-free field above there is exactly one
harmonic field below, and the theorem of lesson 06 guarantees it. But the operator is
*unbounded*, so a small perturbation in the data produces an arbitrarily large change
in the solution. Uniqueness constrains the number of solutions; it says nothing about
whether the solution can be found from imperfect data. The practical fix is
regularisation (truncating high wavenumbers), and the price is that the answer then
depends on the truncation — which is a different kind of non-uniqueness, induced by
the method rather than by the physics.

---

## ★7 — Sharpening of an anomaly with depth

**(a)** $g_z(0) = GM/h^2$. Differentiating twice,
$d^2g_z/dx^2 = GMh\cdot\frac{d^2}{dx^2}(x^2+h^2)^{-3/2}
= -3GMh(x^2+h^2)^{-5/2} + 15GMh\,x^2(x^2+h^2)^{-7/2}$, and at $x=0$ the second term
vanishes, leaving $-3GM/h^4$.

**(b)** For $M = 1.0\times10^{12}$ kg and $h = 1000$ m: peak
$= 6.674\,30\times10^{-5}$ m s$^{-2}$, curvature
$= -2.002\,29\times10^{-10}$ s$^{-2}$ — matching the demonstration's table rows for
$h = 1000$ m exactly.

**(c)** $d^2g_z/dx^2 \propto h^{-4}$, so a factor $2$ reduction in depth multiplies
the curvature by $16$ (the table shows $1.251\times10^{-11}\to2.002\times10^{-10}$
for $2000\to1000$ m, a factor $16.0$). Double differentiation therefore amplifies
both the depth-dependent signal and the noise by the same factor, and the ratio of
signal to noise after differentiating a *finite-precision* field falls as $h^{-4}$.
Estimating depth by numerical differentiation is thus a badly conditioned version of
a question that fitting answers well.

**(d)** The potential is harmonic above the source, so it has **no interior
extremum** (maximum principle) — there is no peak to sharpen. The field's sharpening
comes from differentiating the potential, and each derivative multiplies the
wavenumber-$k$ content by $k$. The potential itself remains smooth; it is the
*derivatives* that concentrate at shallow depths.

---

## ★8 — Testing a grid for harmonicity

**(a)** $4\pi G\rho = 4\pi\times6.674\,30\times10^{-11}\times2700
= 2.2645\times10^{-6}$ s$^{-2}$. Ratio
$= 5\times10^{-11}/2.2645\times10^{-6} = 2.208\times10^{-5}$.

**(b)** Yes, the grid may be treated as harmonic at the level of the data: the
residual is $2.2\times10^{-5}$ of the Laplacian that even a modest density would
produce, and the density that would be inferred from the residual alone is
$\rho_{\text{eff}} = \lvert\nabla^2V\rvert/(4\pi G) = 5\times10^{-11}/8.386\times10^{-10}
= 0.06$ kg m$^{-3}$ — four to five orders of magnitude below any plausible rock.
The correct statement is quantitative: the residual corresponds to a spurious density
of $0.06$ kg m$^{-3}$.

**(c)** Second order in $h$ means the residual should fall by a factor of about $4$
when $h$ is halved, to about $1.3\times10^{-11}$ s$^{-2}$.
**(d)** If the residual did not fall with refinement it would mean the departure from
harmonicity is *real*, not numerical: there is source content inside the region at
the sampling scale — a shallow density contrast between the stations, or a systematic
data error that mimics one. Since the stencil's truncation error is the only
numerical source and it is known to be second order, persistence is diagnostic.
This is *the* practical harmonicity test.

---

## ★★★9 — Mean value property implies harmonicity

**(a)** Let $u$ be continuous on a connected open set $\Omega$ and suppose the mean
value property holds for every closed ball inside $\Omega$.

*Step 1: $u$ is smooth.* The volume form of the property,
$u(\mathbf{p}) = \frac{3}{4\pi R^3}\iiint_{B(\mathbf{p},R)}u\,dV$, expresses $u$ as a
volume average. Changing variables to centre the ball on $\mathbf{p}$ and
differentiating in $\mathbf{p}$ (the integrand is only Lipschitz, so the standard
argument smooths first by convolving with a radial mollifier and then differentiates)
shows $u$ is $C^\infty$. A cleaner route: fix a small $a$ and write
$u(\mathbf{p}) = \frac{3}{4\pi a^3}\int_{B(0,a)}u(\mathbf{p}+\mathbf{y})\,d\mathbf{y}$,
which is a convolution with the indicator of a ball, hence smooth. This is the one
place where the argument needs care.

*Step 2: the Laplacian vanishes.* With $A(R)$ the surface mean,
$A'(R) = \frac{1}{4\pi R^2}\oint_{r=R}\partial u/\partial n\,dS
= \frac{1}{4\pi R^2}\iiint_{B}\nabla^2u\,dV$. Since $A(R) = u(\mathbf{p})$ is
constant, $A'(R) = 0$, so $\iiint_{B(\mathbf{p},R)}\nabla^2u\,dV = 0$ for every $R$.
Dividing by the volume and letting $R\to0$, continuity of $\nabla^2u$ (from Step 1)
gives $\nabla^2u(\mathbf{p}) = 0$.

*Step 3: connectedness* is used only in the maximum-principle corollary (the set
where $u$ attains its maximum is open and closed, hence all of $\Omega$). The
direct argument in Step 2 needs no connectivity.

**(b)** On a disconnected domain, take $\Omega = B(0,1)\cup B(3,1)$ and let $u = 0$
on the first ball and $u = 1$ on the second. $u$ is harmonic on each component and
satisfies the mean value property everywhere in $\Omega$, yet it is not constant —
and no contradiction arises, because the maximum principle's connectedness step fails.
"Non-constant" in the statement of the maximum principle means non-constant on each
connected component.

**(c)** On a punctured ball $\Omega = B(0,1)\setminus\{\mathbf{0}\}$, the function
$u = 1/r$ is harmonic and bounded below, but not constant. Nothing is contradicted:
the maximum principle requires the domain to be bounded and $u$ to be continuous on
it (or at least bounded above), and $u = 1/r$ is unbounded *at the puncture* and the
puncture is part of the closure of the domain, so the supremum is not attained in
$\Omega$ at all. More simply, $u = 1/r$ is not harmonic at the removed point, and the
theorem's hypothesis "$\Omega$ is open and $u\in C^2(\Omega)$" holds — so the real
reason must be that the domain is not bounded in the relevant sense: the maximum of
$1/r$ over the punctured ball is unbounded, so there is no maximum to be attained on
the boundary. The lesson is that the maximum principle is a statement about
attainment, and an unbounded function need not attain anything.

---

## ★★★10 — The maximum principle for $\nabla\cdot(k\nabla u) = 0$

**(a)** **Statement.** If $k>0$ and $u$ satisfies
$\nabla\cdot(k\nabla u) = 0$ in a bounded region $V$, then $\max_V u = \max_{\partial V}u$.
**Proof.** Multiply the equation by $u$ and integrate:
$0 = \iiint u\nabla\cdot(k\nabla u)\,dV
= \oint u\,k\frac{\partial u}{\partial n}\,dS - \iiint k\lvert\nabla u\rvert^2\,dV$,
the second line by the divergence theorem. Rearranging,
$\iiint k\lvert\nabla u\rvert^2\,dV = \oint ku\partial u/\partial n\,dS$. Now
consider a perturbation $u_\epsilon = u + \epsilon$ and note that if $u$ had a strict
interior maximum then $\nabla\cdot(k\nabla u)$ would have to be negative there; a
rigorous proof uses the *weak* form and a comparison argument with
$u_\epsilon = u + \epsilon\lvert\mathbf{x}\rvert^2$, whose
$\nabla\cdot(k\nabla u_\epsilon) > 0$ unless $k$ degenerates, forcing the maximum of
$u_\epsilon$ onto the boundary, and then letting $\epsilon\to0$.

**(b)** Steady heat conduction: $\nabla\cdot(k\nabla T) = 0$ with no internal heat
sources. The principle says the maximum temperature is on the boundary, so you cannot
have an isolated hot spot in the interior of a source-free conducting body. A hot
spot implies a heat source, in precise analogy with a gravity "hot spot" implying a
mass.

**(c)** DC resistivity: $\nabla\cdot(\sigma\nabla\phi) = 0$ with injection only at
the electrodes. The potential cannot have a strict interior maximum in a
source-free region of constant or variable conductivity; the equipotentials behave
like level surfaces of a gravity potential, and the geometric factors of resistivity
arrays are computed as solutions of this equation.

**(d)** The maximum is interior wherever there is a source: a resistive body
dissipating power, a chemical reaction releasing heat, or a current injection point.
Each corresponds to a non-zero right-hand side or a singular $k$ (a perfect insulator
or conductor), i.e. to a failure of the hypothesis $k>0$ finite and
$\nabla\cdot(k\nabla u) = 0$ everywhere.

**(e)** With $\nabla\cdot(k\nabla u) = f$ and $f$ of both signs, the sign argument
fails: the equation no longer says "$u$ is the average of its neighbours with a
positive weight". A positive region of $f$ can support an interior maximum (a source)
just as a positive mass supports an interior potential maximum. The maximum principle
is a *maximum* principle, and sources are precisely what remove it.
