# Solutions — 09-04-02 SP for Seepage, Dams, Landfills and Mineralisation

> **Read after attempting the exercises.** Lesson:
> [02 SP Applications](../02-sp-applications.md). All models **SYNTHETIC**.

---

## ★1 — Two depths from one width

$$\text{point electrode: } h = \frac{80.0}{3.4641} = 23.1\ \mathrm{m},
\qquad
\text{compact dipole: } h = \frac{80.0}{1.5328} = 52.2\ \mathrm{m}.$$

The ratio is $2.26$, the same factor as in lesson 01, because it is the ratio of
the two geometry constants and not a property of this particular anomaly.

---

## ★2 — A detection moment

From the measured table at $160$ m depth:
$IL = 1.131\times10^{-3}$ A m, and the corresponding peak anomaly is
$0.704\ \mu$V. Note that the required peak anomaly is *below* the per-station
noise of $1\ \mu$V: detection is possible because the matched filter integrates
the anomaly over $41$ stations, adding the signal coherently
($\propto$ number of stations) and the noise incoherently
($\propto \sqrt{\text{number of stations}}$). The template's width — which grows
with depth — is what makes the filter efficient, and that is why the required
peak anomaly *falls* with depth even though the required moment rises.

---

## ★3 — Which metric does what

- **Depth:** the full width at half maximum (for a single-lobe anomaly), or more
  generally the shape of the profile.
- **Strength:** the amplitude, i.e. the scale factor, of the anomaly.

Neither alone suffices because the two are coupled through the unknown source
geometry: the amplitude carries the moment divided by the depth squared (and
carries the unknown conductivity $\rho$), while the width carries the depth
multiplied by a geometry constant that differs by a factor $2.26$ between the
point-source and compact-dipole families. Interpreting either number requires the
other *and* a stated geometry.

---

## ★4 — The template norm and the $3/2$ exponent

Take the compact dipole surface field

$$v(x) \approx \frac{\rho IL}{2\pi}\cdot
\frac{h}{\left(x^{2}+h^{2}\right)^{3/2}} .$$

Then, writing $v = (\rho IL/2\pi)\,g(x)$ with
$g = h/\left(x^{2}+h^{2}\right)^{3/2}$,

$$\left\langle \mathbf{v},\mathbf{v}\right\rangle
= \left(\frac{\rho IL}{2\pi}\right)^{2}\sum_i g(x_i)^{2}\Delta x\,/\Delta x
\;\approx\; \left(\frac{\rho IL}{2\pi}\right)^{2}
\frac{1}{\Delta x}\int_{-\infty}^{\infty} g(x)^{2}\,\mathrm{d}x .$$

The integral is elementary: with $x = h\tan u$,

$$\int_{-\infty}^{\infty}\frac{h^{2}\,\mathrm{d}x}
{\left(x^{2}+h^{2}\right)^{3}} = \frac{1}{h^{4}}
\int_{-\pi/2}^{\pi/2}\cos^{4}u\,\mathrm{d}u = \frac{3\pi}{8h^{4}},$$

so $\int g^{2}\,\mathrm{d}x \propto h^{-4}\cdot h^{0}$? — the substitution removes
the $h$ dependence except through $\mathrm{d}x = h\sec^{2}u\,\mathrm{d}u$, and
the exact evaluation gives
$\int g^{2}\mathrm{d}x = 3\pi/\left(8h^{3}\right)$. Hence

$$\lVert\mathbf{v}\rVert \propto \frac{IL}{h^{3/2}} .$$

**The two approximations**: (i) the profile is much longer than the anomaly, so
the integral extends to $\pm\infty$; (ii) the stations sample the profile finely
enough that the sum approximates the integral (station spacing $\ll h$).

The measured exponent is $1.542$, i.e. $2.8\%$ above $1.5$. At the shallowest
depth ($10$ m) the $400$ m profile is only $20h$ wide with a station spacing of
$10$ m equal to $h$, so both approximations are marginal there; the excess
reflects the finite aperture and the finite density of stations, which matter
most exactly where the template is narrowest.

---

## ★5 — The missing number

At $20\%$ noise the demonstration measures a 16–84% depth spread of **$14$ m** on
a $40$ m source (a $35\%$ uncertainty), against $2$ m at $2\%$ noise.

The median alone is not the answer because the estimator's *distribution* is what
a reader needs to judge a claim: two surveys with the same median depth can differ
by an order of magnitude in reliability, and the spread is the only quantity that
distinguishes them. The spread also enters the interpretation directly — a
$14$ m uncertainty on a $40$ m source means a second, shallower body within
$14$ m of the first cannot be separated from it.

---

## ★6 — A linear ramp and an orthogonal template

The fitted current changes from $0.1002$ A to $0.1002$ A — i.e. by less than the
printed resolution, and the recovered depth is unchanged at $40.0$ m.

The reason is orthogonality. The template for a symmetric single-lobe anomaly is
an **even** function of $x$, and a linear ramp is **odd** about the profile
centre, so

$$\left\langle \mathbf{b}, \mathbf{x}\right\rangle = \sum_i b(x_i)\,x_i = 0$$

by symmetry (terms at $+x_i$ and $-x_i$ cancel exactly). A trend with no
projection on the template cannot move the least-squares estimate of the
template's scale, and the depth — which enters through the *shape* of
$\mathbf{b}$ — is likewise unaffected. The demonstration's quadratic trend
(symmetric) changes the current by $0.2\%$ because a quadratic is even but is not
orthogonal to the template's breadth.

---

## ★7 — Survey design for a small anomaly in a trending field

**Anomaly parameters.** $5$ mV amplitude, $150$ m width.

**Station spacing.** At least eight to ten stations across the anomaly:
$\Delta x = 15$ m. This resolves the width to about $\pm15$ m, which
corresponds to a depth uncertainty of $\pm15/3.4641 = \pm4.3$ m under the
point-electrode rule — better than the noise-limited depth spread at any
realistic noise level, so spacing is not the limiting factor.

**Profile length.** At least five times the FWHM on each side of the anomaly, so
$750$–$1000$ m, to make the aperture approximations valid and to give the
levelling function data where the anomaly is absent.

**Repeat policy.** Occupy a base station every ten stations (i.e. every
$150$ m) and repeat the first and last stations at the end of each day. This
gives a direct measure of the reference drift in time and lets it be removed as a
time function rather than absorbed into the space function.

**Levelling.** Fit and remove a **low-order polynomial in position with the
anomaly region excluded**, then interpolate the trend across the anomaly. Report
the polynomial order and the residual of the fit. With a regional trend of
$0.01$ mV/m over a $1000$ m profile, the trend is $10$ mV — twice the anomaly —
so the levelling is the dominant term in the whole analysis, and the choice of
order matters more than the instrument.

**Statistic that confirms the anomaly is not an artefact.** Two checks:
(i) the anomaly's width must be consistent with a plausible depth
($150$ m width $\to$ $43$ m depth for a point electrode, $98$ m for a compact
dipole, and a distributed source must have its own extent), whereas a levelling
artefact has a width set by the polynomial order and the profile length;
(ii) repeat the profile one day later with a *different* levelling order. An
anomaly that survives both with the same amplitude and position is real; one
whose depth moves by more than the noise-limited spread is a levelling artefact.
A quantitative version: refit with levelling polynomials of order 1 and 2 and
require the recovered source parameters to agree within the Monte Carlo spread of
Section 3.3 for the survey's own noise level.

**Budget.** $1000/15 \approx 67$ stations per profile, three profiles (one plus
two repeats or cross-lines) and base stations gives about $250$ occupations — a
comfortable two-day survey for a two-person crew.

---

## ★8 — Why the sheet is separable and the line is not

**The sheet is separable** because it produces a *qualitatively different
shape*: its source is distributed over $120$ m at only $10$ m depth, so its
anomaly is broad and flat-topped with slowly decaying flanks — a different
functional form from a single compact lobe. Over a $400$ m aperture with
$10$ m spacing that difference is large compared with the $2\%$ noise: the
residual is $6.93$ noise units, i.e. the misfit exceeds the noise by a factor
seven, and it is *systematic* (a coherent shape difference), not random.

**The line is not separable** because a compact dipole and a short vertical line
have almost the same *far-field* potential. Both are, to first order, a vertical
current dipole: the surface potential depends on the total moment and the
centroid depth, and the internal distribution of current along the axis changes
the field only in the near zone, by an amount that decays faster than the leading
term. Over an aperture of a few anomaly widths with $2\%$ noise, that near-zone
difference is below the detection threshold ($1.45$ versus $1.04$ noise units).

**What would separate them.** The near-zone difference lives at *small offsets*
(within about one source dimension) and at *high spatial frequencies* in the
profile. Two options:

1. **Closer station spacing near the anomaly axis** — $2$ m rather than $10$ m
   over the central $\pm40$ m — to sample the near-zone curvature, together with
   the same or better noise control so the smaller difference is resolvable.
2. **A measurement that is not a surface potential at all**: a borehole
   measurement (an SP log, a mise-à-la-masse sounding, or a resistivity log)
   that intersects the source and fixes its vertical extent directly.

The general principle is the one lesson 01 §3.6 states: surface potential data
constrain the *family* and the *centroid*, and only near-field or in-hole
measurements constrain the internal distribution.
