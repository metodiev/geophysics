# Exercises — 02-08-04 Poisson's Equation and Source Distributions

Attempt these **closed-book** before opening the
[solutions](./04-poisson-equation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/poisson_sources_demo.py`](../code/poisson_sources_demo.py)
require you to run it and report its actual output. Use
$G = 6.674\,30\times10^{-11}$ m$^3$ kg$^{-1}$ s$^{-2}$, $z$ positive downward, and
report anomalies in mGal as well as m s$^{-2}$.

---

## ★ Foundational

**★1.** An infinite slab has $\rho = 2600$ kg m$^{-3}$ and thickness $t = 150$ m.

(a) Compute $g_z$ from $2\pi G\rho t$.
(b) Express it in mGal.
(c) Compute the result for $(\rho,t) = (5200, 75)$ and state the relation between
the two answers.
(d) State what a single measurement of $g_z$ determines about the slab.

---

**★2.** A right rectangular prism has horizontal extent
$1600\times1200$ m, top at $600$ m depth, thickness $300$ m and
$\rho = 2700$ kg m$^{-3}$.

(a) Sketch the anomaly profile and state where it is maximal.
(b) State qualitatively how the profile changes if the prism is moved to $1800$ m
depth with the same density and dimensions, and whether the peak decreases.
(c) State whether the half-width of the profile is closer to the depth to the top,
the centre or the bottom of the prism, and why.
(d) State what additional information the *shape* of the profile gives beyond its
amplitude.

---

**★3.** Superposition.

(a) Two prisms of the same dimensions sit side by side, both
$2700$ kg m$^{-3}$. State the relation between the anomaly of the pair and the
anomalies of the individual prisms.
(b) State whether the relation is exact or approximate.
(c) The demonstration reports the first prism at $1.0348993416\times10^{-4}$ m s$^{-2}$
at the origin and the second at $7.4728566602\times10^{-6}$ m s$^{-2}$. Compute the
sum and the second prism's contribution to the total at that station.
(d) State the property of Poisson's equation that makes (a) true.

---

**★4.** A sphere of radius $a = 1000$ m is uniformly magnetised with
$M = 1$ A m$^{-1}$ along $z$.

(a) Write the fictitious surface charge $\sigma_m(\theta')$.
(b) Compute the total magnetic moment $m = \tfrac43\pi a^3M$.
(c) Write the exterior scalar potential of the equivalent dipole and evaluate it at
$r = 2000$ m, $\theta = 45^\circ$.
(d) State why the surface-charge description is *exact* here and not an
approximation.

---

## ★★ Applied

**★★5.** Run [`../code/poisson_sources_demo.py`](../code/poisson_sources_demo.py).

(a) Report the split-prism superposition relative difference.
(b) Report the composite-body relative differences at $n = 40$, $80$ and $160$, and
the ratio between successive values.
(c) Report the prism closed form against quadrature at $x = 0$ for $n = 80$, and
the worst relative difference over the four stations.
(d) Report $g_z/$slab for half-widths $2000$ and $10^6$ m.
(e) Report the worst relative difference between the magnetic surface integral and
the dipole potential.
(f) Report the successive ratios of the thin-body/surface-layer discrepancy.

---

**★★6.** The slab ambiguity.

(a) Find four different $(\rho, t)$ pairs, with $t$ decreasing, whose $g_z$ is
$4.478750242702\times10^{-4}$ m s$^{-2}$.
(b) State what quantity the anomaly actually determines.
(c) Explain why this is not a numerical coincidence.
(d) A Bouguer anomaly of $20$ mGal is interpreted with $\rho = 2400$
kg m$^{-3}$ instead of the correct $2670$ kg m$^{-3}$. Compute the resulting error in
the inferred slab thickness at $500$ m depth, and state whether the error is a
percentage or an absolute quantity.

---

**★★7.** The thin-body equivalence.

(a) Hold $\rho t = 540000$ kg m$^{-2}$ fixed and compute $\rho$ for
$t = 200$, $100$, $50$ and $25$ m.
(b) State the limiting areal density the body approaches as $t\to0$.
(c) Using the demonstration's discrepancy values, estimate the exponent $p$ in
"discrepancy $\propto t^p$" from the ratio at successive halvings.
(d) State the geophysical implication for modelling a thin sedimentary layer.

---

**★★8.** The prism formula near a face.

(a) In equation (3) of the lesson, identify the terms that become singular when the
observation point lies on the plane $z = z_1$.
(b) State why the *sum* of the corner terms nevertheless has a finite limit.
(c) Describe the numerical symptom you would see in an implementation that used
$\arctan$ instead of $\operatorname{atan2}$.
(d) State one operational consequence for modelling a body whose top touches the
surface of the Earth.

---

## ★★★ Research-oriented

**★★★9.** Derive the vertical gravity of a two-dimensional polygon.

(a) Show that the field of a uniform polygon can be written as a line integral over
its boundary using the divergence theorem or Green's theorem in the plane.
(b) Show that for a polygon the integral reduces to a sum over the edges, with each
edge contributing terms involving the distance to the edge and the angles subtended.
(c) Apply your formula to an infinite horizontal strip and recover the slab result.
(d) Apply it to a horizontal cylinder by taking the limit of a regular $N$-gon and
show you recover $2G\lambda h/(x^2+h^2)$. State which terms vanish in the limit.

---

**★★★10.** The potential of a uniformly magnetised sphere, by direct integration.

(a) Write $V_m(\mathbf{r}) = \frac{1}{4\pi}\oint
\sigma_m/\lvert\mathbf{r}-\mathbf{r}'\rvert\,dA'$ with
$\sigma_m = M\cos\theta'$ and expand $1/\lvert\mathbf{r}-\mathbf{r}'\rvert$ in
Legendre functions.
(b) Use the orthogonality of the Legendre polynomials to show that only the $l=1$
term survives, and evaluate it.
(c) Show the result equals $m\cos\theta/(4\pi r^2)$ with
$m = \tfrac43\pi a^3M$.
(d) Explain what changes if the sphere is magnetised along $x$ instead of $z$, and
state the general statement about the surface-charge pattern and the multipole
order.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
