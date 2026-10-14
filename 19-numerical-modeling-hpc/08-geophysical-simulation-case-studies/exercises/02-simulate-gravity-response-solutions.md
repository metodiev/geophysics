# Solutions — 19-08-02 Simulating Gravity and Magnetic Responses

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [02 Simulating Gravity and Magnetic Responses](../02-simulate-gravity-response.md).

---

## ★1 — The infinite-slab limit

$$g_z = 2\pi G\Delta\rho t
= 2\pi\times6.67430\times10^{-11}\times500\times100
= 2.0968\times10^{-5}\ \mathrm{m\,s^{-2}} = 2.0968\ \mathrm{mGal}.$$

The result is independent of depth because, for an infinite sheet, the solid angle
subtended by the sheet at the station is $2\pi$ at every depth: increasing $z$
reduces the contribution of each element by $1/r^{2}$ but increases the area seen
within a given angular element by $r^{2}$. The two effects cancel exactly, which is
why this limit is the standard far-field benchmark.

---

## ★2 — A point mass at two offsets

Directly above:

$$g_z(0) = \frac{GM}{z_c^{2}} = \frac{6.67430\times10^{-11}\times2.0\times10^{9}}{250^{2}}
= \frac{0.13349}{6.25\times10^{4}} = 2.1358\times10^{-6}\ \mathrm{m\,s^{-2}}
= 0.2136\ \mathrm{mGal}.$$

At $500$ m offset:

$$g_z(500) = \frac{GMz_c}{(500^{2}+250^{2})^{3/2}}
= \frac{0.13349\times250}{(3.12500\times10^{5})^{3/2}}
= \frac{33.372}{1.7469\times10^{8}} = 1.9104\times10^{-7}\ \mathrm{m\,s^{-2}}
= 0.01910\ \mathrm{mGal}.$$

Ratio: $0.01910/0.21358 = 0.0894$, i.e. $8.9$ per cent. The decay is not $1/r^{2}$
(which would give $0.25$ at $r = 2z_c$) because the anomaly depends on the
*vertical* component, which decays as $z_c^{3}/r^{3}$ in the far field.

---

## ★3 — Dipole moment and field

$$m = \frac{4}{3}\pi a^{3}M = \frac{4}{3}\pi(150)^{3}(2.0) = 2.8274\times10^{7}\ \mathrm{A\,m^{2}},$$

$$B_z(0) = \frac{\mu_0}{4\pi}\frac{2m}{z_c^{3}}
= 10^{-7}\times\frac{2\times2.8274\times10^{7}}{6.4\times10^{7}}
= 10^{-7}\times0.88357 = 8.8357\times10^{-8}\ \mathrm{T} = 88.36\ \mathrm{nT}.$$

A field of this size is measured routinely, which is why compact magnetised bodies
are standard exploration and UXO targets.

---

## ★4 — Where the point mass becomes acceptable

From the table: at $0$ m offset the error is $-5.70$ per cent, at $100$ m
$-0.33$ per cent, at $200$ m $+0.28$ per cent, at $400$ m $-0.33$ per cent, at
$800$ m $-0.06$ per cent. The smallest offset beyond which the error stays below
$0.5$ per cent is therefore $100$ m for this geometry.

The non-monotonicity is real and worth understanding: the error is the sum of the
body's multipole corrections, and different multipoles dominate at different
offsets with different signs. Directly above the centre the quadrupole term is
largest and negative; at $200$ m the octupole contributes with the opposite sign,
so the error crosses zero. **A rule of thumb like "the point mass is fine beyond
one body-width" is a statement about a specific body, and the honest procedure is to
compute the error for the body at hand rather than to assume a monotone decay.**

---

## ★5 — Discriminating three equal-mass bodies

Offsets above about $1$ km are useless: at $800$ m all three bodies agree to two
significant figures ($0.0057$ mGal) and at $2$ km the sheet is $0.0057$ while the
compact bodies are at $0.0004$ — a factor of $14$, but at the level of $0.4$ per cent
of the peak anomaly, easily lost in noise.

The discriminating offsets are therefore (i) close in — $0$ to $400$ m, where the
sheet is $66$ times weaker at the centre than the compact bodies — and (ii) far
out, beyond $2$ km, where the compact bodies have decayed and the sheet has not.
The discriminating **signal** is the *shape* of the profile: the sheet's anomaly is
nearly independent of offset, while a compact body's falls off steeply. Plotting
$g_z$ against log-offset makes the difference a slope, which is far more legible
than a difference of two similar numbers, and plotting the ratio to an equal-mass
point mass turns it into a signed curve whose shape identifies the body.

---

## ★6 — A magnetised cube as a dipole

$$m = (200)^{3}\times0.5 = 4.0\times10^{6}\ \mathrm{A\,m^{2}}, \qquad
B_z(0) = 10^{-7}\frac{2\times4.0\times10^{6}}{300^{3}} = 2.963\times10^{-8}\ \mathrm{T}
= 29.6\ \mathrm{nT}.$$

The real anomaly differs for two reasons: (i) a cube is **not** a dipole — its
external field has higher multipoles that matter at offsets comparable to its size,
exactly as for gravity; and (ii) a real body's magnetisation is rarely uniform: it
may be induced (along the ambient field) with demagnetising effects, or carry
remanence at an unrelated direction, in which case the moment direction is unknown
and the anomaly's *shape* depends on it as much as on the geometry.

---

## ★7 — Survey design for a sheet versus a compact body

**Assumed noise.** $\sigma = 0.01$ mGal, stated as a synthetic value; the design
must be re-run if the real repeatability is different.

**Station spacing and coverage.** $25$ m spacing from $0$ to $2$ km along two
crossing profiles: $25$ m resolves the shape of a $200$ m body (about $8$ stations
across it) and $2$ km reaches the region where the sheet's flat response differs
from the compact body's decay.

**Model-form signature.** Plot the ratio of the observed anomaly to the best-fitting
equal-mass point mass, against offset. For a compact body this curve is
$O((a/r)^{2})$ and decays; for a sheet it approaches a constant at large offset
because the field does not decay. Also plot the *residual* of each model against
offset: a sheet's misfit is a trend, a compact body's is a curvature.

**Decision rule.** Fit both models with the same number of free parameters, use half
the stations for calibration and half for validation, and report the reduced
chi-square of both on the validation half. With $100$ stations and this noise the
two models are separated at many sigma wherever the offset exceeds about one body
width, and the pipeline is the one of
[19-07-03](../../07-verification-validation-uncertainty/03-model-validation.md).

---

## ★8 — Quadrature requirements for an elongated body

**Test.** Gauss-Legendre in each axis, doubling $n$ from $8$ to $32$, and a
convergence curve of the maximum relative field error against an $n = 64$ reference
(or against an independent implementation, e.g. a boundary-element solution). Report
the measured convergence and the $n$ at which the error falls below $10^{-6}$.

**Why the sphere's table cannot be used.** The sphere's integrand is analytic and
nearly isotropic, so it converges fastest of all bodies; an elongated body with a
$10{:}1$ aspect ratio has a much more anisotropic kernel, and the convergence rate
is limited by the *shortest* dimension relative to the station distance. The
required node count scales with the aspect ratio, and the only reliable statement is
a measured one for the geometry at hand.

**If the test fails to converge.** Do not report the field. The failure carries
information: it usually means the quadrature is under-resolving a corner or an edge
where the integrand has a near-singularity. Options are to subdivide the body into
cells and integrate each with its own quadrature (the standard remedy, and the
reason production codes are built around a discretised body rather than one
integral), to transform the coordinates, or to replace the volume integral with a
boundary integral
([19-05-02 Boundary Element Methods for Potential Fields](../../05-integral-equation-and-boundary-methods/02-boundary-element.md)).
