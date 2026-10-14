# Exercises — 04-05-01 Landform Processes and Shapes

Attempt these **closed-book** before opening the
[solutions](./01-landforms-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/landforms_demo.py`](../code/landforms_demo.py)
require you to run it and report its actual output. **Every answer that is a rate
must name the coefficient it depends on, and every coefficient you supply is a
model input unless the problem says it is measured.**

Values to use, where a problem does not give them:
$g = 9.81$ m s⁻²; $1$ mm yr⁻¹ $= 10^{-3}$ m yr⁻¹.

---

## ★ Foundational

**★1.** A soil-mantled ridge crest has hillslope diffusivity $\kappa = 2\times10^{-3}$
m² yr⁻¹ and is subject to a rock uplift rate $U = 1\times10^{-4}$ m yr⁻¹.

(a) Compute the steady-state crest curvature $\partial^{2}z/\partial x^{2}$ in
m⁻¹.
(b) Compute the corresponding radius of curvature.
(c) Compute the diffusion (relaxation) time $\tau = L^{2}/\kappa$ for a ridge of
horizontal half-width $L = 50$ m, in years and in Myr.
(d) State what happens to $\tau$ if $\kappa$ doubles, and what happens if $L$
doubles.

---

**★2.** A fault scarp is $h = 8$ m high and its maximum slope magnitude is
measured as $s_{\max} = 0.5$.

(a) Using $\kappa = 1\times10^{-3}$ m² yr⁻¹, compute the age from
$t = h^{2}/(4\pi\kappa s_{\max}^{2})$.
(b) Compute the diffusion length $\sqrt{4\kappa t}$ at that age.
(c) Verify by substituting back that the formula returns
$s_{\max} = 0.5$.
(d) Recompute the age for $\kappa = 5\times10^{-4}$ m² yr⁻¹ and state the ratio
to (a).

---

**★3.** A channel obeys $S = k_s A^{-\theta}$ with $\theta = 0.5$ and
$k_s = 30$ m$^{2\theta}$ yr⁻¹ (i.e. m yr⁻¹ for this $\theta$).

(a) Compute $S$ at $A = 1\times10^{6}$ m².
(b) Compute $S$ at $A = 1\times10^{7}$ m².
(c) Compute $S$ at $A = 1\times10^{8}$ m².
(d) Compute the product $S A^{\theta}$ at each of the three areas, and state what
it is.

---

## ★★ Applied

**★★4.** The same channel has erosion coefficient $K = 1\times10^{-5}$
m$^{1-2m}$ yr⁻¹ and slope exponent $n = 1$.

(a) Compute the uplift rate implied by $k_s = 30$ m yr⁻¹ from
$k_s = (U/K)^{1/n}$.
(b) If instead $n = 2$ with the same $k_s$ and $K$, compute the implied $U$ from
$k_s = (U/K)^{1/n}$.
(c) Explain in two sentences why the same steepness index can correspond to
uplift rates that differ by orders of magnitude, and what a study must report
before $k_s$ can be compared with another study.

---

**★★5.** In a tributary the drainage area grows downstream as
$A(x) = A_0(1 + x/x_0)^{2}$ with $A_0 = 1\times10^{5}$ m² and $x_0 = 1000$ m.
$U = 1\times10^{-4}$ m yr⁻¹, $K = 1\times10^{-5}$ yr⁻¹, $m/n = 0.5$, $n = 1$.

(a) Show that $\chi(x) = \int_{0}^{x}(A_0/A)^{m/n}\,\mathrm{d}x$ evaluates to
$x_0\ln(1 + x/x_0)$, and compute $\chi$ at $x = 5000$ m.
(b) Compute the slope of $z$ against $\chi$ for a steady-state profile.
(c) Compute the total elevation drop over the $\chi$ of part (a).
(d) State what a *kink* in a $z$–$\chi$ plot would indicate.

---

**★★6.** A basin has area $A = 250$ km². Hack's law applies with
$k = 1.4$ km$^{1-2h}$ and $h = 0.6$.

(a) Compute the main-stem length $L$ in km.
(b) If the total mapped channel length is $4.5L$, compute the drainage density
$D_d$ in km⁻¹.
(c) Using the geometric approximation that the mean distance from a point to the
nearest channel is $1/(2D_d)$, compute that distance in km.
(d) State the units of $k$ and why a Hack coefficient quoted without units cannot
be compared with another study.

---

## ★★★ Research-oriented

**★★★7.** Run [`../code/landforms_demo.py`](../code/landforms_demo.py) and
report:

(a) the analytic and the numerical maximum slope, and the observed convergence
order of the profile error on the three grids;
(b) the slope error at the finest grid, as a percentage;
(c) the recovered concavity index from the slope–area regression and the value
of $k_s$ at the two ends of the area range;
(d) the relative difference between the fitted and the analytic $z$-on-$\chi$
slope;
(e) the knickpoint celerity at $A = 10^{6}$ m² and $10^{7}$ m², and the time for
100 km of retreat at each.

(f) In three sentences, explain why the recovery of $\theta$ to six decimal
places is a check of the code and *not* evidence that real channels obey
$\theta = 0.45$.

---

**★★★8.** Interpretation and its limits.

(a) Two fault scarps of the same height in the same region give ages that differ
by a factor of 3 when a single $\kappa$ is assumed. Give two entirely different
geological explanations and say which is testable with an independent dataset.
(b) The linear diffusion law is known to under-predict transport on steep slopes,
where landsliding dominates. State the direction of the bias this introduces in a
scarp age derived from $s_{\max}$, and justify it with the sign of the
relationship between $\kappa$ and $t$.
(c) A ridge crest is mapped with a 1 m lidar DEM and its curvature is computed as
$-5.1\times10^{-2}$ m⁻¹. Using $\kappa$ from ★1, compute the implied soil
production rate and state the two largest sources of uncertainty in that number.
(d) A buried palaeo-channel is found 12 m below a floodplain surface. List the
property contrasts that would make it detectable, and name one method for each
contrast.
