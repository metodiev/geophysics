# Solutions — 07-04-03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [03 GNSS Positioning](../03-gnss-positioning.md).

---

## ★1 — The observation equations and what differences cancel

$$P = \rho + c(\delta t - \delta t^{s}) + I + T + M_P + \epsilon_P,$$
$$\Phi = \rho + c(\delta t - \delta t^{s}) - I + T + \lambda N + M_\Phi + \epsilon_\Phi .$$

| difference | cancels |
|---|---|
| single (between satellites) | satellite clock $\delta t^{s}$ (exactly), receiver clock kept |
| single (between receivers) | receiver clock $\delta t$ (exactly), satellite clock kept |
| double (two receivers, two satellites) | both clocks |
| triple (double difference, differenced in time) | the integer ambiguity, provided there is no cycle slip |

The ionosphere and troposphere are **reduced, not cancelled**, except in the
special case of a very short baseline where the paths are nearly identical. The
$\lambda N$ term survives single and double differences because it belongs to the
satellite–receiver pair, and it is destroyed by the triple difference because it is
constant in time.

---

## ★2 — Wavelength and cycles

$$\lambda = \frac{c}{f} = \frac{299792458}{1575.42\times10^{6}}
= \mathbf{0.190294\ m} = 19.03\ \mathrm{cm}.$$

An ambiguity scatter of $0.05\ \mathrm{m}$ is

$$\frac{0.05}{0.190294} = 0.263\ \mathrm{cycles},$$

comfortably under half a cycle, so rounding would succeed most of the time *for a
single difference* — but the decision must be made on the full estimator's
scatter, not on one difference's.

---

## ★3 — Why VDOP > HDOP

Every satellite is above the receiver, so the set of unit line-of-sight vectors
spans only a hemisphere (and less, given elevation masks). The vertical direction
is therefore constrained from one side only: a change in the receiver's height
moves all ranges in the same sense, which is nearly the same signature as a clock
error. Horizontal directions are constrained from many azimuths at once. The
consequence is geometric and unavoidable — VDOP is larger than HDOP for any
constellation confined to the upper half-space.

---

## ★4 — Phase-based uncertainties

$$\sigma_V = \sigma\cdot\mathrm{VDOP} = 4\ \mathrm{mm}\times2.5
= \mathbf{10.0\ mm},$$

$$\sigma_H = \sigma\cdot\mathrm{HDOP} = 4\ \mathrm{mm}\times1.1
= \mathbf{4.4\ mm}.$$

Formal covariance: with
$\mathrm{cov}(\mathbf{b}) = \sigma^{2}(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}$, the
horizontal uncertainty is the rms of the two horizontal standard deviations and
the vertical is the third diagonal element — so the pair
$(\sigma_H,\sigma_V) = (4.4,\ 10.0)\ \mathrm{mm}$ is the correct statement. Note
that the horizontal figure is a *radial* (2-D) quantity if quoted as a single
number; the lesson reports rms of the components and says so.

---

## ★5 — Code-based position errors

$$\sigma_H = 0.6\times0.8 = \mathbf{0.48\ m},\qquad
\sigma_V = 0.6\times1.4 = \mathbf{0.84\ m},\qquad
\mathrm{3\text{-}D} = 0.6\times1.6 = \mathbf{0.96\ m}.$$

**Relation check.** With $\mathrm{HDOP}^{2} = Q_{xx}+Q_{yy}$ and
$\mathrm{VDOP}^{2} = Q_{zz}$ drawn from the same
$3\times3$ block of $(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}$,

$$\mathrm{PDOP} = \sqrt{\mathrm{HDOP}^{2}+\mathrm{VDOP}^{2}}
= \sqrt{0.8^{2}+1.4^{2}} = 1.61 \approx 1.6 ✔,$$

and the rms 3-D error is
$\sqrt{0.48^{2}+0.84^{2}} = 0.97\ \mathrm{m}$, matching
$0.6\times1.6 = 0.96\ \mathrm{m}$ to rounding.

**Why it is not the sum.** The three components are correlated through the
off-diagonal terms of $(\mathbf{A}^{\mathsf{T}}\mathbf{A})^{-1}$, so the 3-D error
is the Euclidean length of a correlated random vector. The arithmetic sum
$0.48+0.84 = 1.32\ \mathrm{m}$ would overstate it by $37\%$, and the correct
combination rule is the quadratic one — components can only be combined through
the covariance matrix, not by adding standard deviations.

---

## ★6 — Rank loss with a static constellation

If the satellite geometry does not change, the mapping from the baseline $\mathbf{b}$
to the double differences is the same at every epoch, so the stacked design matrix
has identical blocks. The integer ambiguity contributes a *constant* offset to each
difference across epochs, and a constant offset in the observations is exactly
absorbed by a change in $\mathbf{b}$ in the direction that produces a constant
double-difference pattern (for the demonstration's geometry, the vertical
component when the constellation rotates only in azimuth). The two effects are
then perfectly collinear: the design matrix is rank-deficient and the ambiguities
are not separable from the baseline.

Likewise the physical statement: the ambiguities are only observable because the
*geometry* changes while the *integers* do not. Practically, one to a few minutes
of observation is enough for satellite motion to break the collinearity; a
snapshot solution cannot fix ambiguities, which is why instantaneous
centimetre positioning relies on a known integer set transferred from a
nearby reference station.

---

## ★7 — Fixing a $12\ \mathrm{km}$ baseline with $0.04\ \mathrm{m}$ scatter

$$\text{scatter in cycles} = \frac{0.04}{0.190294} = 0.210\ \mathrm{cycles}.$$

Well under half a cycle, so **fix**. From the lesson's table, at $0.060\ \mathrm{m}$
noise the float solution gave $0.0830\ \mathrm{m}$ and the fixed solution
$0.0472\ \mathrm{m}$ — a ratio of $1.76$. Scaling the lesson's $8$-epoch,
$40$-observation geometry to the same problem, expect the fixed baseline
uncertainty to be roughly

$$\sigma_{\text{fixed}} \approx \frac{0.04}{\sqrt{40}}\times\text{(geometry factor)}
\approx 6.3\ \mathrm{mm}\times 1.8 \approx 1.1\ \mathrm{cm},$$

i.e. of order $1\ \mathrm{cm}$ for a $12\ \mathrm{km}$ baseline with a strong
geometry — consistent with the demonstration's ratio of float to fixed errors.

**Tests before accepting the fix:**

1. **Ratio test.** Compare the squared residual norm of the best integer candidate
   with the second-best; a ratio above a stated threshold (commonly around $3$) is
   evidence the best candidate is unambiguous.
2. **Residual test.** The fixed solution's residuals must be consistent with the
   noise; a systematic pattern indicates a wrongly fixed ambiguity.
3. **Repeatability.** Independent solutions (different observation windows,
   different reference satellites) must agree within the formal uncertainty.
4. **Float fallback.** If the tests fail, report the float solution with its larger
   uncertainty — never a fix accepted on rounding alone, because one wrong integer
   costs $19\ \mathrm{cm}$.

---

## ★8 — Where a low-elevation delay appears

From the demonstration's table for a $3.0\ \mathrm{m}$ extra path:

| satellite azimuth / elevation | horizontal error (cm) | vertical error (cm) |
|---|---|---|
| 0 / 75 | 66.7 | $-216.7$ |
| 120 / 30 | 150.1 | 83.7 |

The reasoning is geometric. A delay adds a bias to one range; the least-squares
solution distributes that bias among the four unknowns (three coordinates and the
clock) in proportion to the geometry matrix's inverse. An **overhead** satellite
has a line of sight nearly aligned with the vertical, and the vertical coordinate
is the only one it discriminates — hence the bias lands almost entirely in the
height ($-2.17\ \mathrm{m}$). A **low-elevation** satellite's line of sight is
nearly horizontal, so the bias is distributed into both horizontals and the clock,
and the height is only weakly affected ($+0.84\ \mathrm{m}$, and mixed in sign
with the horizontal $1.50\ \mathrm{m}$).

**Processing step to detect and attribute it.** Compare the residual of each
satellite against elevation: an unmodelled delay produces residuals whose
magnitude increases with decreasing sine of elevation (the standard mapping
function shape). Fitting residuals against $\mathrm{cosec}(e)$ and testing whether
the fitted coefficient is significant — and whether removing it changes the
height by more than its formal error — attributes the bias to atmosphere rather
than to the geometry. A single-frequency solution cannot separate the ionosphere
from the troposphere, which is why the standard remedy is dual-frequency
combination plus a tropospheric model, with the residuals monitored as the
diagnostic.
