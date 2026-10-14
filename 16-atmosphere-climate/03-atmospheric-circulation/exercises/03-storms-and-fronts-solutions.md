# Solutions — 16-03-03 Cyclones, Fronts and Severe Weather Dynamics

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand; where an answer depends on a modelling choice it is stated.

Lesson: [03 Cyclones, Fronts and Severe Weather Dynamics](../03-storms-and-fronts.md).

---

## ★1 — The Eady growth criterion

$$\chi(\mu) = \frac{\coth\mu}{\mu} - \frac{1}{\mu^2}.$$

- $\mu = 1.0$: $\coth 1 = 1.313035$, so
  $\chi = 1.313035 - 1 = 0.313035 > 1/4$ → **unstable**.
- $\mu = 2.5$: $\coth 2.5 = 1.013590$, so
  $\chi = 1.013590/2.5 - 1/6.25 = 0.405436 - 0.16 = 0.245436 < 1/4$ →
  **stable**.

**Why each end is stable.** Long waves (small $\mu$): the two rigid lids couple
only through the interior PV, which is zero in Eady's problem, so as the
wavelength grows the boundary waves decouple and the instability switches off.
Short waves (large $\mu$): the wave is shorter than it is deep, so it cannot
sense the shear coherently and the boundary waves fall out of phase; formally
$\chi\to1/4$ at $\mu = 2.399$ and declines thereafter.

---

## ★2 — Preferred wavelength

$$L_d = \frac{NH}{f} = \frac{10^{-2}\times10^4}{1.03126\times10^{-4}}
= 9.697\times10^5\ \mathrm{m} = 970\ \mathrm{km},$$

$$\lambda_{\max} = \frac{2\pi NH}{1.606\,f}
= \frac{6.2832\times10^4}{1.606\times1.03126\times10^{-4}}
= 3.794\times10^6\ \mathrm{m} = 3794\ \mathrm{km}.$$

Units: $N$ is s⁻¹, $H$ is m, so $NH/f$ is m; multiplying by the dimensionless
factor $2\pi/1.606$ keeps it a length.

---

## ★3 — Frontogenesis doubling time

$$t_2 = \frac{\ln 2}{D} = \frac{0.69315}{10^{-5}} = 6.93\times10^4\ \mathrm{s}
= 0.80\ \mathrm{d}.$$

After $t = 2.0$ d the factor is
$\mathrm{e}^{Dt} = \mathrm{e}^{10^{-5}\times1.728\times10^5} = \mathrm{e}^{1.728}
= 5.63$, so

$$|\nabla_h\theta| = 2\times10^{-5}\times5.63 = 1.13\times10^{-4}\
\mathrm{K\,m^{-1}},$$

a factor of 5.63 larger, i.e. about 2.5 doubling times
($2^{2.5}=5.66$ ✔).

---

## ★4 — Growth rate from the characteristic equation

$$\hat c = \tfrac12\left[1 \pm \sqrt{1-4\chi}\right].$$

For $\chi>1/4$, write $1-4\chi = -(4\chi-1)$, so

$$\sqrt{1-4\chi} = \mathrm{i}\sqrt{4\chi-1},
\qquad
\mathrm{Im}(\hat c) = \tfrac12\sqrt{4\chi-1} = \sqrt{\chi-\tfrac14}.$$

Since $c = U_s\hat c$ and $\sigma = k\,c_i$ with $k = \mu f/(NH)$,

$$\sigma = \frac{\mu f}{NH}\,U_s\sqrt{\chi-\tfrac14}.$$

The standard form follows because the maximum of
$\mu\sqrt{\chi-1/4}$ over $\mu$ is $0.31$ (at $\mu = 1.606$), and
$fU_s/(NH) = f\,\mathrm{Ri}^{-1/2}$ with
$\mathrm{Ri} = (NH/U_s)^2$. Hence
$\sigma_{\max} = 0.31\,f\,\mathrm{Ri}^{-1/2}$. Note that this is a *numerical*
constant: it is the maximum of a one-variable function, not a property of the
atmosphere.

---

## ★5 — A different mean state

At $55^\circ$: $f = 2(7.292115\times10^{-5})\sin55^\circ
= 2(7.292115\times10^{-5})(0.819152) = 1.19467\times10^{-4}\ \mathrm{s^{-1}}$.

$$L_d = \frac{NH}{f} = \frac{8\times10^{-3}\times9\times10^3}{1.19467\times10^{-4}}
= \frac{72}{1.19467\times10^{-4}} = 6.027\times10^5\ \mathrm{m} = 603\ \mathrm{km},$$

$$\lambda_{\max} = \frac{2\pi L_d}{1.606} = \frac{6.2832\times6.027\times10^5}
{1.606} = 2.358\times10^6\ \mathrm{m} = 2358\ \mathrm{km},$$

$$\mathrm{Ri} = \left(\frac{NH}{U_s}\right)^2
= \left(\frac{72}{25}\right)^2 = 8.29,$$

$$\sigma_{\max} = \frac{0.31 f U_s}{NH}
= \frac{0.31\times1.19467\times10^{-4}\times25}{72}
= 1.286\times10^{-5}\ \mathrm{s^{-1}}
\;\Rightarrow\; \tau = 0.90\ \mathrm{d}.$$

**Comparison with the reference case.** The wavelength is 38% shorter —
$N$ and $H$ are both smaller ($\lambda\propto NH/f$) and the larger $f$ at
$55^\circ$ shortens it further. The growth is 2.0× faster, because
$\mathrm{Ri}$ fell from 25 to 8.3 and $\sigma\propto \mathrm{Ri}^{-1/2}$,
partly offset by the larger $f$ acting in the same direction
($\sigma\propto f$). Both changes are consequences of the two scaling laws, not
independent facts.

---

## ★6 — CAPE and updrafts

**(a)**

$$w_{\max} = \sqrt{2\,\text{CAPE}} =
\begin{cases}
\sqrt{2\times2152.6} = 65.6\ \mathrm{m\,s^{-1}}, & T_\text{surf}=296\ \mathrm{K},\\
\sqrt{2\times7894.6} = 125.7\ \mathrm{m\,s^{-1}}, & T_\text{surf}=308\ \mathrm{K}.
\end{cases}$$

**(b)** Two reasons the real updraft is smaller: (i) **entrainment** of
environmental air dilutes the parcel and reduces its buoyancy at every level
above cloud base; (ii) **water loading** — the weight of condensed water the
parcel carries — reduces the effective buoyancy. (A third is the reduction of
buoyancy by the dynamic pressure perturbation; any two of the three is a
complete answer.)

**(c)** Holding the environment fixed removes the compensation that operates in
reality: as the surface warms, the troposphere above it also warms (and
moistens), which shrinks the parcel–environment difference and hence CAPE. The
fixed-environment experiment therefore exaggerates the response and should be
read as an upper bound.

---

## ★7 — Convergence versus physical saturation (specification)

**Diagnostic to plot.** The fitted gradient growth rate $\hat D$ (from a linear
fit of $\ln|\nabla\theta|_{\max}$ against $t$, taken while the front is wider
than ten grid cells) against grid spacing $\Delta x$, on a logarithmic
abscissa. Overlay the line $\hat D = D$.

**Grid spacings.** A decade or more: $\Delta x = 4, 2, 1, 0.5, 0.25, 0.125$ km,
holding the domain fixed. Keep the time step at fixed CFL
($\Delta t \propto \Delta x$) so that temporal and spatial errors are not
confounded, then repeat one case at half the time step to confirm the time
discretisation is not the limit.

**Result demonstrating convergence.** A decaying, straight-line trend of
$|\hat D - D|$ against $\Delta x$ — sloped like $\Delta x^2$ for a
second-order scheme — with $\hat D\to D$ from below. Ideally the *time* to a
given front width would be the plotted quantity, since it is a cumulative
measure and amplifies errors.

**What physical saturation would look like instead.** The curves for different
$\Delta x$ would converge to a common $\hat D < D$ for *all* sufficiently fine
grids, and the extra physics would have to be added explicitly (a secondary
circulation or a mixing term). An answer that does not distinguish "the curves
keep moving with $\Delta x$" from "they stop moving, below $D$" has not
separated the two mechanisms.

---

## ★8 — Where cyclostrophic balance fails

For a Rankine vortex outside the core, $v = v_{\max}r_0/r$, so the two terms at
radius $r$ are

$$fv = \frac{f v_{\max} r_0}{r},
\qquad
\frac{v^2}{r} = \frac{v_{\max}^2 r_0^2}{r^3}.$$

They are equal when $r^2 = v_{\max}r_0/f$, i.e.

$$r_* = \sqrt{\frac{v_{\max}r_0}{f}}
= \sqrt{\frac{60\times1000}{8.365\times10^{-5}}}
= \sqrt{7.17\times10^{8}}
= 2.68\times10^4\ \mathrm{m} = 26.8\ \mathrm{km},$$

with $f(35^\circ) = 2\Omega\sin35^\circ = 8.365\times10^{-5}\ \mathrm{s^{-1}}$.

**Assumptions.** Steady, purely tangential flow; cyclostrophic-plus-Coriolis
balance with no radial inflow; the Rankine profile continues to hold at 27 km,
which is generous — a real vortex does not. The answer does **depend** on the
core model: an exponential or Bessel-type core has a different $v(r)$ and hence
a different $r_*$, and a vortex embedded in a larger-scale flow would feel an
environmental pressure gradient as well. The number is therefore an
order-of-magnitude statement: cyclostrophic balance is excellent within a few
core radii (tens of metres to a few kilometres) and must be replaced by
gradient-wind balance at radii of tens of kilometres, where the tangential wind
has already decayed to a few m s⁻¹.
