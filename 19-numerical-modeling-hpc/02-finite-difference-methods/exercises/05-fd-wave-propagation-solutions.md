# Solutions — 19-02-05 Finite-Difference Acoustic and Elastic Wave Propagation

> **Read after attempting the exercises.** Demonstration values are quoted where
> they apply.

Lesson: [05 Wave Propagation](../05-fd-wave-propagation.md).

---

## ★1 — Fourth-order Laplacian

$$\mathsf L_4u = \frac{-u_{i+2}+16u_{i+1}-30u_i+16u_{i-1}-u_{i-2}}{12h^{2}},
\qquad
S(\theta_x,\theta_y) = \frac{30-32\cos\theta_x+2\cos2\theta_x}{12}
+ \frac{30-32\cos\theta_y+2\cos2\theta_y}{12}.$$

The symbol approximates $\theta_x^{2}+\theta_y^{2}$ with an $O(\theta^{6})$
error per axis, and its maximum is at the Nyquist corner: $S_{\max} = 10.666667$.

---

## ★2 — Discrete dispersion relation

$$\cos(\omega\,dt) = 1 - \tfrac12 C^{2}S
\qquad\Longrightarrow\qquad
\omega = \frac{\arccos\!\left(1-\tfrac12 C^{2}S\right)}{dt}.$$

For small $\theta$, $S \approx \theta^{2}$ and
$\arccos(1-C^{2}\theta^{2}/2) \approx C\theta$, giving
$\omega \approx C\theta/dt = ck$: the continuum relation, as consistency
requires.

---

## ★3 — Below four points per wavelength

At PPW $=4$ the measured phase speed is $0.98989$ on the axis *and* $1.01615$ on
the diagonal — a $2.65\,\%$ anisotropy, and the axis and diagonal errors have
opposite signs. The physical meaning is that at this resolution the wave samples
the grid's square symmetry rather than the medium; the phase speed depends on
propagation direction, and a travel time measured on the diagonal is not
comparable with one measured on the axis.

---

## ★4 — The exact limit

$$S_{\max} = 2\times\frac{30-32(-1)+2(1)}{12} = 2\times5.333333 = 10.666667,
\qquad
C_{\max} = \frac{2}{\sqrt{10.666667}} = 0.612372.$$

The five-point scheme has $S_{\max} = 8$ and $C_{\max} = 0.707107$. The
fourth-order stencil's limit is $(0.612372/0.707107) = 0.866$ of the
second-order one, i.e. $13.4\,\%$ **stricter**.

**Consequence.** A time step chosen for a five-point code at $C = 0.7$ becomes
$C = 0.7$ against a limit of $0.612$ — unstable, with a measured growth of
$2.01$ per step at $C = 0.65$. The demonstration measures $1.00000000$ at
$C = 0.60$ and $1.01915738$ at $C = 0.6124$: the boundary is sharp.

---

## ★5 — Interface coefficients

$$Z_1 = 2000\times2500 = 5.0\times10^{6},\qquad
Z_2 = 2200\times3200 = 7.04\times10^{6}\ \mathrm{kg\,m^{-2}\,s^{-1}},$$

$$R = \frac{7.04-5.0}{7.04+5.0} = \frac{2.04}{12.04} = 0.169435,
\qquad
T = \frac{2(7.04)}{12.04} = 1.169435.$$

**At eight cells per wavelength** the one-dimensional staggered test measured an
$R$ *deficit* of about $28\,\%$ (measured $0.204728$ against an exact
$0.285714$). Applying the same proportional deficit:

$$R_{\text{measured}} \approx 0.169435\times(1-0.283) = 0.1215.$$

The honest statement to attach: the amplitude at this resolution is not usable
without the calibration, and the calibration must be done on the actual scheme
(which is exactly what the demonstration provides).

---

## ★6 — Anisotropy over 3 km

Measured at PPW $= 10$, interpolating linearly between the tabulated $8$ and
$16$ rows: axis $\approx1.0015$ (a phase error of $+0.15\,\%$), diagonal
$\approx1.0031$ ($+0.31\,\%$), i.e. a relative difference of about
$0.16\,\%$ between the two directions.

Travel time over 3 km at $c = 3000\ \mathrm{m\,s^{-1}}$: $1.0$ s nominally. The
numerical arrival shifts *early* by $0.15\,\%$ on the axis and by $0.31\,\%$ on
the diagonal, so the difference between the two paths is about
$1.6\times10^{-3}$ s.

**Consequence for interpretation.** A $1.8$ ms differential over $3$ km cannot
be turned into velocity structure without knowing the anisotropy of the grid;
and because the sign is fixed (the diagonal is faster), the effect mimics a
systematic azimuthal velocity variation. Reporting the number is the only way a
reader can separate it from geology.

---

## ★7 — A verification suite for a 3-D elastic staggered solver

Ordered so that early failures localise the fault:

**1. Homogeneous point-source arrival times.** Reference: the analytic travel
time $r/v_p$ and $r/v_s$. Acceptance: error below the dispersion prediction of
the discrete relation (measured, in 2-D, as $0.2\,\%$ at PPW $=8$). Catches:
wrong velocities, wrong staggering (a P arrival appearing at the S speed), sign
errors in the stencil.

**2. Normal-incidence reflection coefficient.** Reference:
$R = (Z_2-Z_1)/(Z_2+Z_1)$, as measured in the lesson's 1-D test. Acceptance:
within $0.5\,\%$ at 64 cells per wavelength. Catches: wrong material placement
(density averaged onto the wrong node set), wrong source amplitude scaling,
interface handling errors. This is the amplitude check that the travel-time test
cannot make.

**3. Free-surface reflection.** Reference: $R = +1$ with the correct polarity for
a traction-free surface. Acceptance: $\pm2\,\%$ and correct sign. Catches: the
free-surface implementation, including the common error of applying a
pressure-release condition to a solid.

**4. Absorbing-edge residual.** Reference: none analytic — measure the returned
amplitude against the outgoing one, and compare with the design target (say
$-40$ dB at normal incidence). Catches: sponge/PML misconfiguration, corner
leakage, and any periodicity left in the grid.

**5. Dispersion and anisotropy.** Reference: the symbol-derived phase speed
along the axis and the diagonal. Acceptance: agreement within the measurement
uncertainty of the run. Catches: a stencil with the wrong coefficients that
passed tests 1 and 2 because those used too few points to expose it.

---

## ★8 — A 2 % dip that might be numerical

**Measured facts.** At PPW $= 8$ the axis phase speed is $+0.206\,\%$ and the
diagonal is $+0.361\,\%$ (both fast); the anisotropy difference is
$0.154\,\%$. At PPW $=4$ the anisotropy is $2.65\,\%$ — the same order as the
claimed $2\,\%$ dip.

**Assessment.** At eight points per wavelength the numerical anisotropy is
$0.15\,\%$, an order of magnitude smaller than the claimed $2\,\%$, so the
claim is *not* explained by anisotropy at that resolution. But the claim becomes
fragile if the effective resolution of the *shortest* wavelengths in the data is
lower than eight points per wavelength — the anisotropy scales as
$\mathrm{PPW}^{-2}$ (measured: $2.65\,\%$ at 4, $0.154\,\%$ at 8), so a
$2\,\%$ effect requires about $\mathrm{PPW} = 4.6$.

**Additional measurement that settles it.** Re-run the same model at two
resolutions (e.g. PPW $=8$ and $12$) and migrate both. A numerical dip changes
with resolution roughly as $\mathrm{PPW}^{-2}$; a structural dip does not move.
If the dip persists identically at both resolutions, it is not the grid.

**What the numerical explanation would look like.** A systematic, azimuth-
dependent velocity error leaves a *consistent* apparent dip that trails the true
structure, varies smoothly with azimuth, and disappears when the migration
velocity is adjusted by the measured phase error. A structural dip instead
correlates with the geology, is consistent between independent source lines, and
does not correlate with the wavepath azimuth relative to the grid axes.
