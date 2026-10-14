# Solutions — 07-03-06 Microgravity for Cavities, Tunnels and Archaeology

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [06 Microgravity](../06-microgravity-applications.md).

---

## ★1 — Unit conversion

$$25\ \mu\mathrm{Gal} = 25\times10^{-8}\ \mathrm{m\,s^{-2}}
= 2.5\times10^{-7}\ \mathrm{m\,s^{-2}} = 0.025\ \mathrm{mGal}.$$

Three units for the same number; the factor between $\mu$Gal and mGal is
$10^{3}$, and confusing them is a routine error in site reports.

---

## ★2 — A $1.5\ \mathrm{m}$ cavity at $4\ \mathrm{m}$

$$M = \tfrac{4}{3}\pi R^{3}\left|\Delta\rho\right|
= \tfrac{4}{3}\pi(1.5)^{3}(2000) = 2.827\times10^{4}\ \mathrm{kg},$$

$$g_z = \frac{GM}{z^{2}}
= \frac{(6.67430\times10^{-11})(2.827\times10^{4})}{16}
= 1.179\times10^{-7}\ \mathrm{m\,s^{-2}} = \mathbf{11.79\ \mu Gal}.$$

This is the demonstration's table row, and it is comfortably above the
$5\ \mu$Gal instrument resolution — but not above a typical $2$–$5\ \mu$Gal
*geological* noise, which is the number that decides detectability.

---

## ★3 — The two depth rules

- Sphere (cavity): $z = x_{1/2}/0.766421 = 1.3048\,x_{1/2}$.
- Horizontal cylinder (tunnel): $z = x_{1/2}$ exactly.

They differ because the sphere's kernel varies as
$z/(x^{2}+z^{2})^{3/2}$ while the cylinder's varies as $z/(x^{2}+z^{2})$. The
cylinder's Lorentzian shape is wider relative to its depth, so its depth is
"read off" directly; the sphere's profile is more peaked, so its half-width is
$76.6\%$ of its depth.

---

## ★4 — The tunnel with a $30\ \mu$Gal peak and a $6\ \mathrm{m}$ half-width

**Depth:** $z = x_{1/2} = \mathbf{6.0\ m}$ (axis depth).

**Line mass:** from $g_{\max} = 2G\lambda/z$,

$$\lambda = \frac{g_{\max}z}{2G}
= \frac{(30\times10^{-8})(6)}{2(6.67430\times10^{-11})}
= 1.348\times10^{4}\ \mathrm{kg\,m^{-1}}.$$

**Radius:** $\lambda = \pi R^{2}\left|\Delta\rho\right|$, so

$$R = \sqrt{\frac{\lambda}{\pi\left|\Delta\rho\right|}}
= \sqrt{\frac{1.348\times10^{4}}{\pi\times2000}} = \mathbf{1.46\ m}.$$

A $1.5\ \mathrm{m}$ radius tunnel with its axis $6\ \mathrm{m}$ down. Note the
internal consistency check: $R/z = 0.24 \ll 1$, so the line-mass approximation
behind the formula is comfortable.

---

## ★5 — A $1\ \mathrm{m}$ cavity under $4\ \mathrm{m}$ with $1\ \mu$Gal noise

Peak anomaly with $\left|\Delta\rho\right| = 2000\ \mathrm{kg\,m^{-3}}$:

$$M = \tfrac{4}{3}\pi(1)^{3}(2000) = 8378\ \mathrm{kg},\qquad
g = \frac{GM}{16} = \frac{(6.67430\times10^{-11})(8378)}{16}
= 3.49\times10^{-8}\ \mathrm{m\,s^{-2}} = \mathbf{3.49\ \mu Gal}.$$

That is $3.5\times$ the stated $1\ \mu$Gal noise, so **detection is possible in
principle** (signal-to-noise $3.5$), but only if the noise is genuinely
$1\ \mu$Gal — a quiet site with repeat readings and careful correction. If the
achievable noise were $3\ \mu$Gal, detection would be marginal.

**If detection fails at $1\ \mu$Gal** the required contrast would be

$$\left|\Delta\rho\right|_{\min} = 2000\times\frac{1}{3.49} = 573\
\mathrm{kg\,m^{-3}},$$

i.e. the anomaly would have to be $3.5$ times larger than an air-filled cavity of
that size can produce — impossible, which is the quantitative way of saying that a
$1\ \mathrm{m}$ cavity at $4\ \mathrm{m}$ is at the edge of what microgravity can
see.

---

## ★6 — Why the factor is exactly two

Both anomalies are linear in $\Delta\rho$, so an air-filled
($-2000\ \mathrm{kg\,m^{-3}}$) and a water-filled ($-1000\ \mathrm{kg\,m^{-3}}$)
cavity of identical geometry differ by exactly $\times2$: the demonstration prints
the ratio $0.500$ for both test cases. Nothing about the geometry enters.

**Implication for inversion:** a single anomaly amplitude cannot separate a
water-filled cavity at depth $z$ from an air-filled one at depth $z\sqrt{2}$ (since
$g \propto \Delta\rho R^{3}/z^{2}$ and $R$, $\Delta\rho$ trade off too). Only the
**profile width** adds independent information, which is why a single-station
reading is worthless and a profile with well-sampled flanks is not.

---

## ★7 — Water-filled at $3\ \mathrm{m}$ versus air-filled deeper

Matching amplitudes with the same radius:

$$\frac{\left|\Delta\rho_1\right|}{z_1^{2}} = \frac{\left|\Delta\rho_2\right|}{z_2^{2}}
\;\Longrightarrow\;
z_2 = z_1\sqrt{\frac{2000}{1000}} = 3\sqrt{2} = \mathbf{4.24\ m}.$$

So a water-filled void at $3\ \mathrm{m}$ is amplitude-degenerate with an
air-filled void at $4.24\ \mathrm{m}$. The degeneracy is broken by the **shape**:
the half-widths differ by the same factor, $x_{1/2} = 0.766421z$, i.e.
$2.30\ \mathrm{m}$ against $3.25\ \mathrm{m}$.

**Survey specification:**

- **Station spacing ≤ 0.5 m** on the flanks so that the half-width (a $\sim1\
  \mathrm{m}$ difference) is measured to better than $10\%$; the lesson's own
  $2\ \mathrm{m}$ spacing produced a $+19\%$ depth error, so $0.5$–$1\ \mathrm{m}$
  is the requirement.
- **Profile length** at least $3\times x_{1/2}$ on both sides of the peak
  ($\ge 10\ \mathrm{m}$ each way) so the flanks are measured, not extrapolated.
- **Repeat protocol:** each station read twice with a base re-occupation every
  $1$–$2$ hours to control drift, targeting $\le 1\ \mu$Gal repeatability — the
  depth discrimination depends on the flank amplitude difference, which is a few
  $\mu$Gal.
- **Corrections:** Earth tide computed (order $100\ \mu$Gal, an order of magnitude
  larger than the target), free-air and Bouguer applied with levelling to
  $\sim1\ \mathrm{cm}$.

---

## ★8 — Depth uncertainty at a $4\ \mathrm{m}$ spacing

The lesson's scatter was measured at a $2\ \mathrm{m}$ spacing; the depth
uncertainty from noise scales as $\sigma_z \approx \sigma_g x_{1/2}/g_0$, i.e. it
does not depend on the spacing at all — the spacing contributes a *bias*, not a
scatter. For a $2\ \mathrm{m}$ sphere at $3\ \mathrm{m}$ with a $49.7\ \mu$Gal
peak:

| noise ($\mu$Gal) | scatter (m) | scaled to a $4\ \mathrm{m}$ spacing |
|---|---|---|
| 0.5 | 0.07 | same, plus a larger sampling bias |
| 1.0 | 0.15 | same |
| 2.0 | 0.31 | same |

At a $4\ \mathrm{m}$ spacing, however, the *half-width itself* becomes poorly
sampled: with only one or two stations on each flank, the interpolated
half-amplitude point carries an error of order $dx/2 = 2\ \mathrm{m}$, far larger
than the noise term. **The dominant assumption/limitation is therefore the station
spacing (and, in a real survey, the geological noise and the regional field), not
the instrument noise.** That is why microgravity cavity surveys are run at
$0.5$–$2\ \mathrm{m}$ spacing when the target is metres deep.
