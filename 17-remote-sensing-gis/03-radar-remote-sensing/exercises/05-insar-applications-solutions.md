# Solutions — 17-03-05 InSAR for Earthquakes, Volcanoes, Subsidence and Landslides

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [05 InSAR Applications](../05-insar-applications.md).

---

## ★1 — The strike-slip profile

Far-field offset (the total step across the fault):
$$u(\pm\infty) = \pm\frac{b}{2} = \pm0.750\ \mathrm{m}.$$

Peak surface shear strain at the trace:
$$\left.\frac{\mathrm{d}u}{\mathrm{d}x}\right|_{x=0}
= \frac{b}{\pi d} = \frac{1.5}{\pi \times 3000}
= 1.5915\times10^{-4}\ \text{(dimensionless, m/m)}.$$

Displacement at $x = d$:
$$u(d) = \frac{b}{\pi}\arctan(1) = \frac{b}{\pi}\cdot\frac{\pi}{4}
= \frac{b}{4} = 0.375\ \mathrm{m}.$$

**Units:** $b$ in m; $d$ in m; $u$ in m; $\mathrm{d}u/\mathrm{d}x$ is a strain,
dimensionless (m per m), and its reciprocal length scale is $d$.

---

## ★2 — Near-cancellation in the line of sight

$$d_{\text{LOS}} = \hat{u}\cdot\mathbf{d}
= 0.5680 \times 0.030 + 0.8192 \times (-0.020)$$
$$= 0.017040 - 0.016384 = +0.000656\ \mathrm{m}
= +0.656\ \mathrm{mm} \approx 0.02\ \text{fringes}.$$

**Comment:** eastward motion and subsidence partly *cancel* along this line of
sight, so a combination of two large displacements produces a nearly invisible
signal. The converse is the trap: an observed fringe pattern can be explained by
many different (east, up) combinations — the single-geometry ambiguity in its
most concrete form.

---

## ★3 — A Gaussian source

$$\Delta V = 2\pi\sigma^{2}A
= 2\pi \times (3000)^{2} \times 0.040 = 2.2619\times10^{6}\ \mathrm{m^{3}}
= 2.2619\ \mathrm{Mm^{3}}.$$

Peak LOS displacement at $\theta = 35^\circ$:
$$d_{\text{LOS}} = A\cos\theta = 0.040 \times 0.8192 = 0.032768\ \mathrm{m}
= 3.277\ \mathrm{cm}.$$

Fringes:
$$\frac{0.032768}{0.028282} = 1.159\ \text{fringes}.$$

A 4 cm uplift is a little over one fringe: measurable in a single pair if
coherence holds, and easy in a stack. The volume, however, is exact only for the
assumed Gaussian; a different source shape with the same surface peak and radius
gives a different volume.

---

## ★4 — Profile geometry

**(a)** Over $\pm 2d$:
$$u(+2d) - u(-2d) = 2\frac{b}{\pi}\arctan(2)
= 2 \times \frac{2.0}{\pi} \times 1.107149 = 1.4094\ \mathrm{m}.$$
As a fraction of $b$: $1.4094/2.0 = 70.5\%$.

**(b)** $u = 0.4b$ requires $\arctan(x/d) = 0.4\pi$, so
$$x = d\tan(0.4\pi) = 4000 \times \tan 72^\circ = 4000 \times 3.07768
= 12\,311\ \mathrm{m} = 12.31\ \mathrm{km}.$$

**(c)** It measures the **spatial scale of the elastic strain accumulation** — how
far from the trace the offset builds up. Since $u(d) = b/4$ by the profile's
geometry, the distance at which a given fraction of $b$ is reached is a direct
multiple of the locking depth. That is exactly why the locking depth is
recoverable from the shape of the fringe pattern: it is the only length scale in
the model.

---

## ★5 — Gradient budget with a halved locking depth

**(a)** Peak strain $b/(\pi d) = 2.0/(\pi\times2000) = 3.1831\times10^{-4}$. Per
$20\ \mathrm{m}$ pixel, projected with $\hat{u}_E = 0.5680$:
$$\Delta d_{\text{LOS}} = 0.5680 \times 3.1831\times10^{-4} \times 20
= 3.616\times10^{-3}\ \mathrm{m} = 3.616\ \mathrm{mm},$$
exactly twice the demonstration's $1.808$ mm for $d = 4$ km — the gradient scales
as $1/d$.

**(b)** Set the per-pixel change equal to $\lambda/4 = 0.014141$ m:
$$0.5680 \times \frac{2.0}{\pi d} \times 20 = 0.014141
\;\Longrightarrow\;
\frac{2.0}{\pi d} = 1.2449\times10^{-3}
\;\Longrightarrow\;
d = 511\ \mathrm{m}.$$

**(c)** For a $2\ \mathrm{m}$ slip the aliasing limit is reached only for a locking
depth of about half a kilometre. Shallower than that — very shallow ruptures,
mining-induced collapse, a lava dome growing fast — the fringes crowd below the
pixel scale and the near field becomes unmeasurable at this wavelength. The
remedies are a shorter wavelength? No: the *same* physical gradient subtends more
fringes at a shorter wavelength, so the remedy is a **longer** wavelength (L or P
band), a smaller pixel, or a shorter time between acquisitions (which reduces the
accumulated displacement but not a coseismic step). This is the standard argument
for L-band observation of heavily vegetated and rapidly deforming terrain.

---

## ★6 — Seasonal bias

**(a)** The bias arises because a sinusoid sampled over a non-integer number of
cycles projects onto the linear term of the design matrix. That projection is
**linear in the seasonal amplitude**, because the model is linear and the term is
additive, so doubling the amplitude to $12\ \mathrm{mm}$ doubles the bias to
approximately $+1.87\ \mathrm{mm\,yr^{-1}}$.

**(b)** Two sampling properties that change the bias at fixed amplitude:

1. **The phase of the season relative to the record ends.** A record that begins
   and ends near the same seasonal phase has a small projection; one that begins
   at a maximum and ends at a minimum has a large one. The bias can change sign
   with a different start date.
2. **The number of cycles spanned.** With many cycles the sinusoid is nearly
   orthogonal to the linear term and the bias falls; with one or two cycles the
   projection is large. A 3-year record with an annual term is the marginal case
   in which the demonstration's $0.94\ \mathrm{mm\,yr^{-1}}$ appears.

This is why a seasonal term must be *fitted*, not assumed away, and why the fitted
amplitude and phase belong in any report of a rate.

---

## ★7 — Separating volcanic source depth from volume (specification)

**The trade-off.** For a small source the surface displacement field scales with
the product of a source volume-like quantity and a function of depth: a shallow
small source and a deep large one produce nearly the same *pattern*. The
degeneracy is broken by any observable that depends on depth *independently* of
amplitude.

**Data that break it.**

1. **The shape of the near field.** A shallower source has a sharper, more
   strongly curved pattern within a few source radii; a deeper one is broader and
   flatter. Quantitatively, the ratio of the displacement at two radii is a
   function of depth alone. This requires good sampling of the near field, so a
   dense pixel spacing over the centre is essential.
2. **A second look geometry.** Ascending and descending views weight the vertical
   and horizontal components differently, so the *ratio* of the two LOS fields at
   the same location varies with depth.
3. **GNSS inside the deformation field.** One continuous station at a known
   horizontal distance provides an absolute amplitude at a known position,
   removing the amplitude–depth degeneracy with a single extra number.
4. **A time series.** If the source inflates, the pattern's evolution gives
   repeated constraints; a change in width with time distinguishes processes.

**Diagnostic.** Invert for source depth, volume and horizontal position with all
observables in one least-squares system, and inspect the **trade-off curve**
between depth and volume — the set of (depth, volume) pairs that fit to within
the data uncertainty. Report the curve, not a point.

**Acceptance criterion.** Claim a depth only if the trade-off curve excludes a
factor-of-two range in depth at the stated residual level. If the curve spans
0.5–5 km, the honest report is "the volume, for each assumed depth" — a one-line
answer, not a number with a spurious uncertainty.

---

## ★8 — Why north leaks into east, and how to break it

**(a)** Write the two equations with the east and north coefficients only:
$$d^{a} = \hat{u}^{a}_E d_E + \hat{u}^{a}_N d_N, \qquad
d^{d} = \hat{u}^{d}_E d_E + \hat{u}^{d}_N d_N.$$

If the second row is a multiple of the first — which happens when they share the
same ratio, $\hat{u}^{a}_N/\hat{u}^{a}_E = \hat{u}^{d}_N/\hat{u}^{d}_E$ — the
system is singular and $(d_E, d_N)$ cannot be separated at all. Then the solver
must assume one of them, and whichever is assumed absorbs the other. The vertical
equation is untouched because $d_U$ enters with a different coefficient, which is
why the vertical estimate stayed unbiased.

**(b)** For a right-looking geometry,
$$\frac{\hat{u}_N}{\hat{u}_E}
= \frac{-\sin\theta\sin\alpha}{\sin\theta\cos\alpha} = -\tan\alpha .$$

Ascending: $\alpha = 8^\circ \Rightarrow -\tan 8^\circ = -0.14054$. Descending:
$\alpha = 188^\circ \Rightarrow -\tan 188^\circ = -0.14054$ (tangent has period
$180^\circ$). The ratios are **identical**, so the two equations are parallel in
the $(d_E, d_N)$ plane and the degeneracy is exact — exactly as the demonstration
measured ($0.00$ mm of leakage into the vertical, $1.41$ mm into the east).

**(c)** The degeneracy is broken by making $-\tan\alpha$ differ between the two
observations, i.e. by combining passes with different **headings**, not merely
opposite directions. Concretely:

1. **A non-polar orbit pair**, or a same-sense pair from two satellites with
   different inclinations, giving $\tan\alpha$ values that differ by a worthwhile
   amount. The conditioning of the $2\times2$ system improves as
   $|\tan\alpha_a - \tan\alpha_d|$ grows.
2. **A left-looking acquisition**, which flips the sign of $\hat{u}_E$ and
   therefore the ratio, providing an independent equation for the north
   component.
3. **A GNSS station** measuring the north component directly at one point,
   which fixes $d_N$ and lets the geometry determine the rest — the cheapest
   honest solution when only one station is available.

Without one of these, a $10\ \mathrm{mm}$ north component appears as a $10/7.12
\approx 1.4\ \mathrm{mm}$ error in the east estimate, and no amount of processing
removes it: it is the geometry, and only new geometry or new data can break it.
