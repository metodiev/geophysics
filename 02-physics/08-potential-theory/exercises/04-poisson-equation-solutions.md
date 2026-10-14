# Solutions — 02-08-04 Poisson's Equation and Source Distributions

> **Read this after attempting the exercises, not before.** $z$ is positive
> downward, so the "vertical field" is the downward component.
> $G = 6.674\,30\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$. Values attributed to the
> demonstration are its actual output.

---

## ★1 — An infinite slab

**(a)** $g_z = 2\pi G\rho t = 2\pi\times6.674\,30\times10^{-11}\times2600\times150
= 1.635\,498\,7\times10^{-4}$ m s$^{-2}$.

**(b)** $16.355$ mGal.

**(c)** $2\pi G\times5200\times75 = 1.635\,498\,7\times10^{-4}$ m s$^{-2}$ — the same
number to all displayed digits, because $\rho t$ is unchanged.

**(d)** It determines the **mass per unit area** $\rho t$
$(= 390\,000$ kg m$^{-2}$ here$)$, and nothing else. The density and the thickness are
individually unconstrained: any pair with that product fits.

---

## ★2 — A right rectangular prism

**(a)** The profile is bell-shaped, asymmetric only in that a prism has straight
edges; it is maximal **above the centre of the prism's top face** (that is, at the
surface point with the smallest distance to the body's mass), and falls off
monotonically outward. Unlike the sphere's profile it has no closed-form half-width
rule; it is broader than a sphere of equal mass at the same centre depth because the
mass is spread laterally.

**(b)** Moving the prism deeper with the same density and dimensions: the peak
decreases (roughly as depth$^{-2}$ in the far field), and the profile becomes broader
and smoother. Concretely, the anomaly's curvature at the peak decreases.

**(c)** The half-width is closest to the depth to the **centre** of the prism. That is
the general rule for compact bodies: the anomaly's width is set by the depth to the
centre of mass, not to the top or the bottom. For a prism of thickness $t$ centred at
$h_c$, the characterising depth is $h_c$ to within a fraction of $t$.

**(d)** The shape (width, curvature, and the decay rate away from the peak) constrains
the **depth and the geometry**; the amplitude constrains the **mass**. That separation
is the depth–amplitude trade-off, and it is the reason both a shallow small body and a
deep large one can fit a given anomaly (lesson 06).

---

## ★3 — Superposition

**(a)** The pair's anomaly equals the sum of the individual anomalies, at every
station.

**(b)** **Exact.** It follows from the linearity of the integral
$V = G\int\rho/D\,dV'$ and of Poisson's equation; it is not an approximation about
geometry or magnitude.

**(c)** The second prism contributes
$1.109\,627\,9082\times10^{-4} - 1.034\,899\,3416\times10^{-4}
= 7.472\,856\,6600\times10^{-6}$ m s$^{-2}$ — the demonstration's value for the
second prism's closed form, $7.472\,856\,6602\times10^{-6}$ m s$^{-2}$. ✓

**(d)** The linearity of the forward operator: $\mathcal{F}(\rho_1+\rho_2)
= \mathcal{F}(\rho_1)+\mathcal{F}(\rho_2)$.

---

## ★4 — A magnetised sphere

**(a)** $\sigma_m(\theta') = \mathbf{M}\cdot\hat{\mathbf{n}} = M\cos\theta'$, positive
in the northern hemisphere (where $\mathbf{M}$ points outward) and negative in the
south.

**(b)** $m = \tfrac43\pi a^3M = \tfrac43\pi\times10^9\times1
= 4.188\,790\,205\times10^9$ A m$^2$.

**(c)** $V_m = m\cos\theta/(4\pi r^2)$. At $r = 2000$ m, $\theta = 45^\circ$:
$V_m = 4.188\,790\,205\times10^9\times0.707\,106\,8/(4\pi\times4\times10^6)
= 58.9256$ A. (The demonstration prints $58.925\,565\,099$ for the surface integral
at the same station.)

**(d)** Because the volume source $\nabla\cdot\mathbf{M}$ vanishes *identically* for
uniform $\mathbf{M}$: the divergence of a constant vector field is zero. Apply the
divergence theorem and only the boundary term survives, exactly. Uniform
magnetisation is the one case where the surface description is not an approximation
but an identity.

---

## ★5 — Reading the demonstration

**(a)** Split-prism superposition relative difference: $0.0\times10^{0}$ (exact).

**(b)** Composite body: $4.598\times10^{-4}$ at $n = 40$, $1.150\times10^{-4}$ at
$n = 80$, $2.875\times10^{-5}$ at $n = 160$. Successive ratios $4.00$ and $4.00$ —
second-order convergence of the midpoint quadrature.

**(c)** Prism closed form $1.034\,899\,3416\times10^{-4}$ m s$^{-2}$ against
quadrature $1.034\,935\,4278\times10^{-4}$ m s$^{-2}$ at $x = 0$, $n = 80$: relative
difference $3.49\times10^{-5}$. Worst over the four stations: $4.18\times10^{-5}$
(at $x = 1600$ m).

**(d)** Half-width $2000$ m: $g_z/$slab $= 0.739\,715\,39$. Half-width $10^6$ m:
$0.999\,459\,81$.

**(e)** Worst relative difference between the magnetic surface integral and the dipole
potential: $3.2\times10^{-13}$.

**(f)** Thin-body/surface-layer discrepancy ratios per halving of $t$: $1.811$,
$1.888$, $1.937$, $1.966$ — increasing toward $2$, consistent with a leading $O(t)$
error.

---

## ★6 — The slab ambiguity

**(a)** $4.478\,750\,242702\times10^{-4} = 2\pi G\rho t$ gives
$\rho t = 1\,068\,000$ kg m$^{-2}$, so for example $(2670, 400)$, $(5340, 200)$,
$(10680, 100)$ and $(42720, 25)$ — in kg m$^{-3}$ and m respectively.

**(b)** The product $\rho t$, i.e. the mass per unit area.

**(c)** It is an algebraic identity, not a coincidence: the slab field is
$2\pi G\rho t$ with $\rho$ and $t$ appearing only as a product, so the level set of
the forward operator is the hyperbola $\rho t = \text{const}$. The demonstration shows
all four pairs giving $4.478\,750\,242702\times10^{-4}$ m s$^{-2}$ with a relative
deviation of $0.0\times10^{0}$.

**(d)** The correct density is $2670$ instead of $2400$, so the inferred thickness is
too large by the factor $2670/2400 = 1.1125$, i.e. $11.25$ per cent: $500$ m becomes
$556.25$ m — an error of $56$ m. The error is a **percentage** of the thickness (and
of the anomaly), not an absolute quantity, so it grows with the target size. This is
why an assumed Bouguer density is a systematic error that propagates into every
derived thickness and every model built on the corrected anomaly.

---

## ★7 — The thin-body equivalence

**(a)** $\rho = 540\,000/t$: $2700$, $5400$, $10\,800$ and $21\,600$ kg m$^{-3}$ for
$t = 200$, $100$, $50$ and $25$ m.

**(b)** $\sigma = 540\,000$ kg m$^{-2}$, the surface layer of the same areal density.

**(c)** The discrepancy values are $1.878\times10^{-1}$, $1.037\times10^{-1}$,
$5.492\times10^{-2}$, $2.835\times10^{-2}$ and $1.442\times10^{-2}$. Taking
$\log_2$ of successive ratios gives $0.857$, $0.917$, $0.954$, $0.975$ — approaching
$1$, so $p\to1$: the discrepancy is $O(t)$, linear in the thickness. (The
logarithmic ratios are slightly below $1$ because of the next-order term, which has
the opposite sign.)

**(d)** A layer thinner than about a tenth of its depth can be modelled as a surface
density to better than a per cent, which justifies the widespread use of
"equivalent-layer" and "thin-sheet" representations for sedimentary fill, and — read
in reverse — justifies the claim in lesson 06 that a thin sheet and a body can be
made indistinguishable by choosing the depth appropriately.

---

## ★8 — The prism formula near a face

**(a)** The terms $\ln(y+r)$ and $\ln(x+r)$ become singular where $y+r\to0$ or
$x+r\to0$, and the arctangent term where $zr\to0$. These occur when the observation
point lies in the plane of a face (so $z=0$ for that face) or on an edge.

**(b)** The singularities are logarithmic (integrable) and the arctangent terms come
in pairs with opposite signs from opposite faces; the alternating sum
$\Delta_x\Delta_y\Delta_z$ of the eight corners cancels the leading divergent pieces,
leaving a finite limit. This is why the closed form extends by continuity to the
faces, but not without care.

**(c)** Using $\arctan$ instead of $\operatorname{atan2}$ returns a principal value in
$(-\pi/2,\pi/2)$, so where the correct quadrant is III or IV the term is off by
$\pi$. The symptom is a *discontinuous offset* in the computed field as the
observation point crosses a horizontal line through the body's edge, or an anomalous
$\pi$-sized jump in the arctangent term — a step of plausible magnitude in the wrong
direction, which is worse than an obvious bug.

**(d)** A body whose top touches the surface (a topographic mass, or a target at zero
depth) puts the observation point exactly on a face, and a careless implementation
then produces a spurious offset along the outcrop. The practical fix is either the
$\operatorname{atan2}$ form with an explicit limiting branch, or evaluating the body
as the difference of two bodies whose faces do not contain the station.

---

## ★★★9 — The vertical gravity of a two-dimensional polygon

**(a)** For a 2-D body of uniform density with cross-section $S$, the vertical field
at a point is the area integral $g_z = 2G\rho\iint_S
(z-z')/((x-x')^2+(z-z')^2)\,dA'$. The integrand is a divergence (in the primed
variables) of the vector field
$\mathbf{F} = (0,-\ln R)$ with $R = \sqrt{(x-x')^2+(z-z')^2}$, since
$\partial_{z'}(-\ln R) = (z-z')/R^2$. Green's theorem in the plane converts the area
integral to the line integral $\oint_{\partial S}\mathbf{F}\cdot\hat{\mathbf{n}}\,ds$
around the perimeter.

**(b)** On an edge between vertices $i$ and $i+1$, parametrise by arclength $s$. With
$\theta$ the angle from the station to the edge point, $\hat{\mathbf{n}}\cdot\mathbf{F}$
collapses to a term proportional to $(\theta_{i+1}-\theta_i)$ plus a logarithmic term
in the distances to the two vertices. The result for a polygon is a sum over edges
$\sum_i[\,z_i(\theta_{i+1}-\theta_i) + \ldots\,]$, which is why polygon
implementations are short and why they are the workhorse of 2-D modelling. (The
demonstration does not evaluate this formula, so no numerical value is quoted here;
the derivation is the exercise's content.)

**(c)** An infinite horizontal strip between depths $z_1$ and $z_2$ has two
horizontal boundaries. Each contributes a term independent of the observation height
(the angles subtended are constant in the infinite limit), and the sum telescopes to
$g_z = 2\pi G\rho(z_2-z_1) = 2\pi G\rho t$ — the slab result.

**(d)** Take a regular $N$-gon of radius $a$ centred at $(0,h)$, and let $N\to\infty$
with $a$ fixed: the angular sum $\sum_i(\theta_{i+1}-\theta_i)\to2\pi$ exactly, and
the logarithmic terms, which involve the distances to the vertices, average to the
logarithm of the distance to the axis. The limiting result is
$g_z = 2G\lambda h/(x^2+h^2)$ with $\lambda = \rho\pi a^2$. The terms that vanish in
the limit are the individual vertex logarithms, which sum to a $\ln$ of the centroid
distance; the terms that survive are the $2\pi$ angular sum, which carries the total
mass, and the geometric factor $h/(x^2+h^2)$.

---

## ★★★10 — The potential of a uniformly magnetised sphere

**(a)** With $\sigma_m = M\cos\theta'$ and $r > a$,

$$\frac{1}{\lvert\mathbf{r}-\mathbf{r}'\rvert}
= \sum_{l}\frac{a^l}{r^{l+1}}P_l(\cos\gamma), \qquad
P_l(\cos\gamma) = P_l(\cos\theta)P_l(\cos\theta')
+ 2\sum_{m\ge1}\frac{(l-m)!}{(l+m)!}P_l^m(\cos\theta)P_l^m(\cos\theta')\cos m(\phi-\phi') .$$

**(b)** The $\phi'$ integral kills every $m\neq0$ term (each contains
$\cos m(\phi-\phi')$, whose mean over $\phi'$ is zero). Of the remaining terms the
$\theta'$ integral is $\int_0^\pi\cos\theta'P_l(\cos\theta')\sin\theta'd\theta'$,
which vanishes for every $l\neq1$ by orthogonality (it is the projection of
$P_1 = \cos\theta'$ onto $P_l$). Only $l=1$ survives, and
$\int_0^\pi\cos^2\theta'\sin\theta'd\theta' = 2/3$, so

$$V_m = \frac{M a^2}{4\pi}\cdot\frac{1}{r^2}\cdot\frac{2}{3}\cdot2\pi\cdot
P_1(\cos\theta)\times\ldots
= \frac{M a^3\cos\theta}{3r^2} .$$

**(c)** With $m = \tfrac43\pi a^3M$, the dipole potential is
$\frac{m\cos\theta}{4\pi r^2} = \frac{4\pi a^3M/3\times\cos\theta}{4\pi r^2}
= \frac{Ma^3\cos\theta}{3r^2}$ ✓ — identical to (b). The demonstration confirms it
numerically at four stations with a worst relative difference of $3.2\times10^{-13}$.

**(d)** Magnetising along $x$ rotates the surface-charge pattern by $90^\circ$; the
integral then involves $P_1^1$ rather than $P_1^0$ and gives a dipole potential
proportional to $\sin\theta\cos\phi$, i.e. the $x$-oriented dipole. The general
statement: **the multipole order of the exterior field is determined by the angular
pattern of the surface charge, not by the body's shape.** A uniform magnetisation
gives a pure dipole for any shape that is inversion-symmetric; a two-domain
magnetisation (opposite signs on opposing faces) gives a quadrupole for a sphere of
the same size. That is why the pattern of a magnetic anomaly's peaks is used to infer
the magnetisation direction, and why remanence makes magnetic interpretation harder
than gravity.
