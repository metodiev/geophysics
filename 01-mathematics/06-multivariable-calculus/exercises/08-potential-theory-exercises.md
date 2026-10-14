# Exercises — 01-06-08 Potential Fields, Laplace and Poisson Equations

Attempt these **closed-book** before opening the
[solutions](./08-potential-theory-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Convention for the whole set: $V = G\int\rho/D\,dV'$ is **positive**,
$\mathbf{g} = \nabla V$, and $\nabla^2V = -4\pi G\rho$. State the convention you
use whenever a sign is at stake. Use $G = 6.674\times10^{-11}$.

---

## ★ Foundational

**★1.** For a point mass $M = 5.0\times10^{11}$ kg at the origin:

(a) write $V$ and compute $\mathbf{g}$ at $\mathbf{r} = (2000, -1500, 3000)$ m;
(b) evaluate $\lvert\mathbf{g}\rvert$ in m/s² and in mGal;
(c) verify that $\nabla^2 V = 0$ at that point, analytically and by stating the
value the numerical Laplacian must converge to.

---

**★2.** State the mean value property, and compute the average of the harmonic
function $V = GM/r$ over the sphere of radius $R$ centred at the point
$\mathbf{c} = (5000, 0, 0)$ m, with the mass at the origin (so the source is
outside the sphere). State the value of $V$ at the centre and confirm agreement.

---

**★3.** A uniform ball has radius $a = 400$ m and density
$\rho = 2800\ \mathrm{kg\,m^{-3}}$.

(a) Compute its total mass.
(b) Compute the surface gravity.
(c) Use Gauss's law to compute the field at $r = 200$ m and $r = 100$ m inside.
(d) State the potential difference between the centre and the surface.
(e) State how many significant figures are defensible in (b) if the density is
known to 1 % and the radius to 5 m.

---

**★4.** A horizontal slab of infinite extent has density $\rho$ and thickness $t$.
Starting from the result for an infinite sheet, $g_z = 2\pi G\sigma$, derive
$g_z = 2\pi G\rho t$ and evaluate it for $\rho = 2500\ \mathrm{kg\,m^{-3}}$ and
$t = 200$ m. Express the answer in mGal and explain why the result is independent
of the observation height.

---

## ★★ Applied

**★★5.** Prove the uniqueness of the Dirichlet problem for Laplace's equation,
stating the identity you use and each step. Then state precisely what the theorem
does *not* say about the sources producing the boundary data.

---

**★★6.** Equivalent strata.

A gravity survey measures $g_z(x,y)$ on a horizontal plane. A modeller proposes to
represent the subsurface by an areal density on a plane at depth $h$.

(a) Write the relationship between the measured field and the density in the
two-dimensional wavenumber domain.
(b) Explain why a solution exists for every $h > 0$.
(c) For two depths $h_1 < h_2$, write the ratio of the required density spectra
and state which depth requires the smoother density.
(d) State what physical information, if any, distinguishes the two models.

---

**★★7.** Isostatic root.

An Airy isostatic model has a mountain of height $H$ above sea level supported by
a root of thickness $t$ below a reference depth, with crustal density
$\rho_c = 2800\ \mathrm{kg\,m^{-3}}$ and mantle density
$\rho_m = 3300\ \mathrm{kg\,m^{-3}}$.

(a) Derive the isostatic balance condition relating $H$ and $t$.
(b) For $H = 2000$ m, compute $t$.
(c) Compute the mass per unit area of the root deficiency, and hence the depth of
the compensating "root" in terms of an equivalent areal mass deficit.
(d) Explain in one sentence why the gravity anomaly over a perfectly compensated
mountain may be small even though the mountain is large.

---

**★★8.** A student reports a residual gravity anomaly with an isolated interior
maximum, 15 % higher than any value on the survey boundary. The survey is 40 km
across and the anomaly is assumed to arise from density structure at 3–5 km depth.

(a) State the result that makes an interior extremum of a harmonic function
impossible, with its hypothesis.
(b) Explain why the hypothesis is satisfied in the *measurement region* but not in
the region containing the sources, and why that distinction matters.
(c) Explain why an interior maximum is nevertheless expected over a dense body,
and reconcile this with (a) using the region in which the field is harmonic.
(d) State one measurement that would help distinguish a shallow compact source
from a deeper, broader one.

---

## ★★★ Research-oriented

**★★★9.** Reproduce the non-uniqueness numerically.

Using the demonstration
[`../code/potential_theory_demo.py`](../code/potential_theory_demo.py) or your own
code, compute the external potential and vertical field at
$(1200, 800, 1400)$ m for

(i) a point mass $M = 1.570796\times10^{12}$ kg at the origin;
(ii) a uniform ball of radius 500 m with that total mass;
(iii) a uniform ball of radius 300 m with that total mass;
(iv) a uniform shell with $400\ \mathrm{m} < r < 500$ m with that total mass.

(a) Report all four values of $V$ and $g_z$.
(b) Compute the relative differences from the point-mass values.
(c) Increase the numerical resolution until your answers stop changing, and report
the resolution at which that happens.
(d) State, with reference to your numbers, why no improvement in instrument
precision can separate (i) from (iv).

---

**★★★10.** Continuation and non-uniqueness.

A gravity field measured on the plane $z=0$ is continued upward by a height $h$
using the kernel $e^{-\lvert k\rvert h}$, where $k$ is the horizontal wavenumber.

(a) Explain why upward continuation is a smoothing operation and why it is stable.
(b) Explain why the inverse operation, downward continuation by a depth $d$, is
unstable and give the amplification factor for wavenumber $k$.
(c) For a survey whose shortest resolved wavelength is $\lambda_{\min}$, determine
the depth $d$ at which the amplification at $\lambda_{\min}$ reaches a factor of
$10^{3}$. Assume the noise level is $10^{-3}$ of the signal at that wavelength and
state at what depth the noise becomes comparable to the signal.
(d) Relate this to the equivalent-stratum result of ★★6 and explain why the
instability of downward continuation and the non-uniqueness of the inverse problem
are two faces of the same statement.
