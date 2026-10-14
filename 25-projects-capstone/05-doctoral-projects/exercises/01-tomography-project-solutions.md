# Solutions — 25-05-01 Project: Local Earthquake Tomography with Resolution Tests

Reference solutions. Every number is printed by
[`code/tomography_demo.py`](../code/tomography_demo.py); all data are
**SYNTHETIC**.

## ★1. The forward relation and units

$$t_i = t_i^{(0)} + \sum_j G_{ij}\,\delta s_j,\qquad G_{ij} = s_0\,l_{ij},$$

with $l_{ij}$ in km, $s_0 = 1/6.000 = 0.166667\ \mathrm{s\,km^{-1}}$, so
$G_{ij}$ is in **seconds**, $\delta s_j$ is a slowness perturbation in
$\mathrm{s\,km^{-1}}$ (or a dimensionless fraction of $s_0$, which is the unit used
throughout the demo) and $t_i$ is in seconds.

A ray spending $10.0$ km in a cell whose slowness is $5\%$ low:

$$\delta t = s_0\,(-0.05)(10.0) = \frac{-0.5}{6.000} = -0.08333\ \mathrm{s} = -83.3\ \mathrm{ms}.$$

The absolute travel time of a $19.14$ km ray in the background:

$$t^{(0)} = 19.14 \times 0.166667 = 3.190\ \mathrm{s}.$$

The demo's largest perturbation is $62.28$ ms, which corresponds to an effective
in-anomaly path of $0.06228 \times 6.000/0.05 = 7.47$ km — consistent with a
$5 \times 3.5$ km half-width anomaly crossed near its centre.

## ★2. The discrepancy principle

**Rule (as stated in the project):** choose the *largest* damping $\alpha$ whose rms
data residual does not exceed the estimated noise level. The largest residual that
qualifies is the noise level itself, so the rule is
$\alpha^\star = \max\{\alpha : \|Gm_\alpha - d\|_\text{rms} \le \sigma\}$.

- With $\sigma = 5.0$ ms: $\alpha = 0.500$ gives $3.92$ ms and $\alpha = 1.000$ gives
  $4.49$ ms, both below $5.0$; $\alpha = 5.000$ gives $18.98$ ms, far above. So
  $\alpha^\star = 1.000$ (the largest qualifying value).
- With $\sigma = 20$ ms: $\alpha = 5.000$ gives $18.98$ ms $\le 20$ and
  $\alpha = 20$ gives $34.64$ ms $> 20$, so $\alpha^\star = 5.000$. The selected
  model then has rms $0.511\%$ and a peak of only $1.44\%$ — a $29\%$ amplitude
  recovery. **A worse picking error buys a smoother, weaker image, and the rule
  moves the damping automatically in the right direction.** That behaviour is the
  test of whether a regularisation rule is sensible.

## ★3. Signal-to-noise and the detection floor

$$\mathrm{SNR} = \frac{36.16\ \mathrm{ms}}{5.0\ \mathrm{ms}} = 7.2,$$

which is the printed value. Because the perturbation is linear in the anomaly
amplitude, an anomaly of peak $A$ produces a signal of
$36.16 \times (A/5.00\%)$ ms; a nominal detection threshold at $\mathrm{SNR} = 1$
gives

$$A_\text{min} = 5.00\%\times\frac{5.0}{36.16} = 0.69\%.$$

Two caveats belong with that number: an extended anomaly is detected through its
whole travel-time signature rather than through its peak, so the real threshold is
lower for a smooth body and higher for a cell-scale one; and the threshold is not
$\mathrm{SNR}=1$ but whatever the chosen detection statistic requires (typically
SNR $\approx 3$–$5$ for a marginal detection in a formal test), i.e. a few percent.

## ★★4. Residual difference versus model difference

- Residual difference: $4.49 - 3.18 = 1.31$ ms from the rounded table, $1.30$ ms from
  the unrounded values the demo prints. As a fraction of the noise:
  $1.30/5.0 = 26\%$.
- Model norm ratio: $9.979/1.037 = 9.62$, i.e. the $\alpha = 0.001$ model is
  $9.6$ times larger in rms.

Why the first number decides nothing: (i) a $26\%$ reduction in residual is not
statistically significant when both residuals are *below* the estimated noise level,
so both models are consistent with the data at the $\sigma$ level; (ii) the extra fit
is achieved by adding cell-scale structure with amplitudes up to $-22\%$ where the
truth is $-5\%$, i.e. by fitting noise — the classic manifestation of fitting more
parameters than the data support; (iii) the choice between two equally acceptable
fits requires a prior or a complexity penalty, which is exactly what the damping
term supplies. **The data determine a set of acceptable models; the damping chooses
within that set.**

## ★★5. Model rms recovery versus peak recovery

$$\frac{\text{recovered rms}}{\text{true rms}} = \frac{1.037}{1.237} = 0.838
\quad\text{against}\quad \frac{\text{recovered peak}}{\text{true peak}} = 0.69 .$$

The two differ because they measure different things. The model rms is an $L_2$
quantity dominated by the amplitude of the anomaly and is insensitive to blurring —
smoothing redistributes a function's energy over neighbouring cells without removing
it, so it barely changes the rms. The peak is a *maximum*: smoothing lowers it
immediately, and the damping removes a further fraction. A recovery figure quoted
without saying which of the two it is therefore understates the problem, and the
honest pair to report is "image rms recovered to $84\%$, peak amplitude to $69\%$".

## ★★6. Why the checkerboard recovers less

The one-cell checkerboard alternates sign at the **highest spatial frequency the
grid can represent**. The damping term $\alpha^2\|\mathbf m\|^2$ penalises amplitude,
and for a fixed amplitude a sign-alternating model has the largest
neighbour-difference content; in singular-value terms the high-spatial-frequency
vectors have the smallest singular values and are filtered hardest. The smooth
Gaussian anomaly is dominated by low-spatial-frequency components and survives
better ($69\%$ against $54.9\%$).

The direction of the error is therefore **conservative**: the checkerboard is
attenuated, so if a checkerboard of that scale is recovered at $r = 0.888$ with
$54.9\%$ amplitude, then real structure of that scale would also be recovered.
The test can produce false negatives (structure that is real but invisible to this
geometry and noise level) but not false positives of that scale. A *failed*
checkerboard must not be reported as "the resolution is the cell size"; it means the
resolution is worse than the cell size and the next question is how much worse.

## ★★7. PSF, effective cells and the resolution length

At the spike cell the recovered amplitude is $63.5\%$ of the input. The row of the
resolution matrix sums to approximately unity (the signed PSF sum is
$-1.085 \times 0.05/0.05$, i.e. $|{\cdot}| \approx 1.08$), so the inversion preserves
the *local average* of the model to within about $8\%$. The absolute gain summed over
the grid is

$$\sum_j |R_{ij}| = 2.327, \qquad
\text{effective cells} = \frac{2.327}{0.635} = 3.66 \approx 3.7 .$$

Two complementary readings:

- *Peak-preservation measure*: $1/0.635 = 1.57$ cells — the spike keeps
  $63.5\%$ of its height, equivalent to being spread over about one and a half cells.
- *Magnitude-sum measure*: $3.7$ cells — the total magnitude recovered corresponds to
  a footprint of about $3.7$ cells.

The **conservative** one is the second, because a null-space direction can put
amplitude where the data do not see it while leaving a sharp peak. Converting to a
length: $3.7 \times (3\ \mathrm{km})^2 = 33\ \mathrm{km^2}$, an equivalent circular
diameter of $\sqrt{4 \times 33/\pi} = 6.5\ \mathrm{km}$. **Quote a resolution of
about $6$–$7$ km at $z = 7.5$ km, not the $3$ km cell.** The demo's own-cell
recoveries at $z = 1.5$, $7.5$ and $13.5$ km ($62.3\%$, $63.5\%$, $63.3\%$) are
nearly equal because coverage per cell is comparable everywhere here
($5.9$–$74.4$ km); with a real catalogue the deep cells are far less well lit and
the resolution length grows sharply with depth, which is why the resolution length
must be quoted *per depth*, never once for the whole model.

## ★★★8. Breaking the source-location–velocity coupling

**Statement of the coupling.** For a fixed set of arrival times, a velocity increase
along a ray path can be traded against moving the hypocentre closer to the station;
the two perturbations produce nearly the same datum. With all hypocentres and all
cell slownesses as free parameters, the problem has a near-null direction that mixes
the two fields, so *both* the velocity image and the catalogue inherit the ambiguity —
in the worst case the velocity model is biased towards the *starting* locations and
the locations are then biased towards the resulting model.

**Constraints that break it, and what each determines.**

1. **Sources with known location and origin time** (quarry blasts, calibration shots,
   explosions, induced events with known depth, repeating earthquake families whose
   geometry is fixed by differential times): these remove the location half of the
   coupling entirely in the volume they illuminate, so the velocity field there is
   determined by absolute times alone.
2. **Sources outside the network** (regional and teleseismic events): their
   hypocentres come from the global network and are essentially independent of the
   local model, so their arrival times constrain velocity with negligible location
   coupling — at the cost of a different ray geometry and hence different resolution.
3. **Double-difference / relative arrival times** for nearby event pairs: the path
   from the hypocentre to a common station is nearly identical for the pair, so
   velocity errors cancel and relative locations are obtained almost model-free.
   This determines the *relative* geometry, while absolute times from 1 or 2 determine
   the absolute velocity; the combination is well conditioned.
4. **Joint inversion with explicit location parameters and their priors**: write the
   posterior over $(\mathbf m, \mathbf x_\text{hypo})$; the coupling then appears as
   a non-zero posterior covariance and can be quantified rather than denied. The
   disciplined version of this is to report the velocity model marginalized over
   hypocentre uncertainty, and to report the hypocentre uncertainty marginalized over
   velocity — reporting both at their jointly optimal values is the standard error.
5. **Independent absolute constraints**: $V_p/V_s$ or $V_s$ from receiver functions
   ([25-04-06](../../04-graduate-projects/06-receiver-function-project.md)), density from
   gravity, or a borehole log, which fix the velocity scale that the arrival-time
   data alone can only determine up to the coupling.

**Resolution to claim for each field.**

- *Velocity*: a PSF-derived resolution length per depth (about $6$–$7$ km here),
  together with the amplitude recovery and the null-space direction that mixes
  velocity with source depth.
- *Hypocentres*: 95% confidence ellipsoids from the posterior or a bootstrap,
  reported with their horizontal and vertical semi-axes separately (the vertical is
  always the worse constrained and is the one coupled to velocity).

**Synthetic tests that show the coupling is gone rather than hidden.**

1. **Wrong-start convergence test.** Run the full joint inversion from velocity
   models biased by $\pm 5\%$ and from hypocentres displaced by $\pm 2$ km. If the
   coupling is broken, both runs converge to the same velocity field and to
   locations agreeing within the claimed ellipsoids. If they converge to two
   different (velocity, location) pairs with equal misfit, the coupling remains and
   the uncertainty has merely been moved into the starting model.
2. **Null test with a known velocity perturbation.** Add a synthetic velocity
   anomaly to the true model, generate data, invert, and check that the recovered
   hypocentres are unchanged (within the ellipsoids) while the velocity anomaly is
   recovered. The reverse test — perturb a hypocentre and check that the velocity
   field is unchanged — is equally necessary; a study that runs only one direction
   has not demonstrated decoupling.
3. **Held-out absolute constraints.** Exclude the calibration shots from the
   inversion, then predict their arrival times and compare with the observed. If the
   velocity field has absorbed the location ambiguity, these predictions will be
   biased in a distance-dependent way — the diagnostic for this particular pathology.
