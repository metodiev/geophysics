# Solutions — 06-10-01 Refraction Survey Geometry and Travel-Time Interpretation

**Read after attempting the exercises.** Numbers were computed, not estimated.
Lesson: [01 Refraction Survey Geometry and Travel-Time Interpretation](../01-refraction-basics.md).
All models are SYNTHETIC.

---

## ★1 — Critical angle and ray parameter

$$\sin i_c = \frac{v_1}{v_2} = \frac{800}{2400} = 0.333333
\quad (\text{dimensionless}),$$
$$i_c = \arcsin 0.333333 = 19.4712^\circ = 0.339837\ \mathrm{rad},$$
$$\cos i_c = \sqrt{1 - 0.111111} = 0.942809,$$
$$p = \frac{\sin i_c}{v_1} = \frac{0.333333}{800}
= 4.16667\times10^{-4}\ \mathrm{s\,m^{-1}}
= \frac{1}{v_2}.$$

The unit of $p$ is seconds per metre, the same as $1/v$, because
$\sin i_c$ is dimensionless.

---

## ★2 — Intercept time and crossover

$$t_i = \frac{2h\cos i_c}{v_1}
= \frac{2 \times 15 \times 0.942809}{800}
= \frac{28.28427}{800} = 0.0353553\ \mathrm{s} = 35.3553\ \mathrm{ms},$$
$$x_c = 2h\sqrt{\frac{v_2+v_1}{v_2-v_1}}
= 30\sqrt{\frac{3200}{1600}} = 30\sqrt{2} = 42.4264\ \mathrm{m}.$$

Units: $\mathrm{km} \times \mathrm{s\,km^{-1}}$ would be seconds; here
$\mathrm{m} \times \mathrm{s\,m^{-1}}$ is seconds. Dimensional check:
$2h\cos i_c/v_1$ is $\mathrm{m}/(\mathrm{m\,s^{-1}}) = \mathrm{s}$. ✔

---

## ★3 — The two algebraic routes agree

$$t_i = \frac{2h\sqrt{v_2^{2}-v_1^{2}}}{v_1 v_2}
= \frac{2 \times 15 \times \sqrt{5.76\times10^{6} - 6.40\times10^{5}}}{800 \times 2400}
= \frac{30 \times 2262.74}{1.92\times10^{6}} = 0.0353553\ \mathrm{s}.$$

They must agree because substituting $\cos i_c =
\sqrt{v_2^{2}-v_1^{2}}/v_2$ into the first form gives the second identically —
the identity $\cos i_c = \sqrt{1-\sin^{2}i_c}$ with $\sin i_c = v_1/v_2$. A
disagreement would indicate that $i_c$ was computed from the wrong velocity ratio.

---

## ★4 — A three-layer curve read as two layers

**Intercept time of the true model.**

$$\theta_1 = \arcsin\frac{1000}{2500} = 23.5782^\circ, \quad
\cos\theta_1 = 0.916515,$$
$$\theta_2 = \arcsin\frac{400}{2500} = 9.2061^\circ, \quad
\cos\theta_2 = 0.987097,$$
$$t_i = 2\left[\frac{6 \times 0.916515}{1000}
+ \frac{5 \times 0.987097}{400}\right]
= 2\left[0.00549909 + 0.01233871\right]
= 0.0356761\ \mathrm{s} = 35.6761\ \mathrm{ms}.$$

**Two-layer interpretation of that intercept.**

$$h_{\text{eq}} = \frac{t_i v_1 v_2}{2\sqrt{v_2^{2}-v_1^{2}}}
= \frac{0.0356761 \times 1000 \times 2500}{2\sqrt{6.25\times10^{6}-1.0\times10^{6}}}
= \frac{89190.3}{4582.58} = 19.4629\ \mathrm{m}.$$

**Error.** The true depth to the $2500\ \mathrm{m\,s^{-1}}$ layer is
$6 + 5 = 11\ \mathrm{m}$, so the error is

$$19.4629 - 11 = +8.4629\ \mathrm{m}, \qquad \frac{8.4629}{11} = +76.9\%.$$

The $400\ \mathrm{m\,s^{-1}}$ layer is never entered by a first-arrival ray, so the
fit is exact — the residual is zero to numerical precision — and the depth is
wrong by three quarters. The crossover of the true curve is
$2 \times 11\sqrt{3500/1500} = 33.6056\ \mathrm{m}$; the two-layer interpretation
invented a crossover at $2 \times 19.4629\sqrt{3500/1500} = 59.46\ \mathrm{m}$,
which a short spread would not even reach.

---

## ★5 — Why the eikonal residual plateaus

A shortest-path solver lets a path continue only in the directions present in its
search set. A ray inclined at $73.87^\circ$ from the horizontal cannot be
represented exactly by a set containing only $71.57^\circ$ and $75.96^\circ$, so
the path is built from those two neighbouring directions and the resulting time
error is the angular quantisation. Between 48 and 96 directions the *same* two
directions bracket the ray, so enriching the set changes nothing and the residual
is constant at $0.0275\ \mathrm{ms}$. At 144 directions a new direction
(consistent with a step of $(2,7)$ grid cells) becomes available, the bracket
tightens, and the residual falls by a factor of about $2.6$ to
$0.0104\ \mathrm{ms}$.

**The refinement parameter is the number of directions, not the grid spacing.**
Reducing $\Delta x$ at fixed directions refines the geometry of each segment but
does not remove the quantisation of its direction, and this is the single most
common misreading of such a convergence table.

---

## ★6 — A spread shorter than the crossover

For $h = 10\ \mathrm{m}$, $x_c = 26.6025\ \mathrm{m}$ (Section 3.2 of the lesson).
A $20\ \mathrm{m}$ spread has its farthest offset at $20\ \mathrm{m} < x_c$, so the
refractor is **not seen at all**: every first arrival is a direct wave and the
record is one straight line of slope $1/v_1 = 2\ \mathrm{ms\,m^{-1}}$. The
interpretation returns $v_1 = 500\ \mathrm{m\,s^{-1}}$ and nothing else.

For $h = 6\ \mathrm{m}$,

$$x_c = 2 \times 6\sqrt{\frac{2300}{1300}} = 12 \times 1.330124
= 15.9615\ \mathrm{m},$$

which is inside the spread, so the refractor *is* seen. But the far branch runs
only from $15.96$ to $20\ \mathrm{m}$ — a $4.04\ \mathrm{m}$ baseline across about
eight receivers at $0.5\ \mathrm{m}$ spacing. That branch determines the slope
$1/v_2$, and its length sets the slope's precision: a $1\ \mathrm{ms}$ pick scatter
over a $4\ \mathrm{m}$ baseline gives a velocity uncertainty of order
$1\ \mathrm{ms}/4\ \mathrm{m} \approx 25\%$ in $v_2$. The depth is therefore
"seen" but barely constrained, which is the practical meaning of the design rule
that the far branch should be about as long as the crossover distance.

---

## ★★★7 — Survey design

$$x_c = 2 \times 25\sqrt{\frac{2700+900}{2700-900}}
= 50\sqrt{2} = 70.7107\ \mathrm{m}.$$

With the crossover at one third of the line, the spread is
$L = 3 \times 70.7107 = 212.13\ \mathrm{m}$, say $210\ \mathrm{m}$ of cable.

**Receiver spacing.** The near branch must resolve $v_1$ and the far branch
$v_2$, and every depth in a delay-time interpretation (Lesson 02) belongs to one
receiver. A $1\ \mathrm{m}$ spacing gives about $70$ near-branch picks and $140$
far-branch picks over $210\ \mathrm{m}$; that is a comfortable design. A $5\
\mathrm{m}$ spacing would give $14$ far-branch picks and would make the depth
profile coarser than the structure being mapped.

**Two checks before reporting a depth.**

1. **Internal consistency of $v_1$.** Fit the direct branch over the near offsets
   and compare with the $v_1$ assumed in the depth conversion. The demonstration's
   sensitivity is $+1.0667$ in logarithmic terms, so a $10\%$ discrepancy in $v_1$
   is a $10.7\%$ depth error — larger than any plausible picking error and
   therefore attributable to structure (a weathered layer with a velocity
   gradient), not to noise.
2. **Reciprocity and residual.** Shoot the line from both ends; the two picks at
   the shot points must agree within the picking error (Lesson 02 uses this as a
   free noise estimate). Then check the two-layer residual against that noise: a
   residual above the noise floor means the model class, not the fit, is the
   problem — the blind-zone situation of ★4.

A depth quoted from a two-layer interpretation without a $v_1$ check is
conditional on a number that was never measured on that line.

---

## ★★★8 — Demonstrating that a perfect fit is not evidence

**Forward model.** A three-layer model with a low-velocity middle layer, e.g.
$800\ \mathrm{m\,s^{-1}}$ from $0$ to $7\ \mathrm{m}$, $300\ \mathrm{m\,s^{-1}}$
from $7$ to $12\ \mathrm{m}$, $2200\ \mathrm{m\,s^{-1}}$ below, with first-arrival
times computed exactly from the delay-time sum of the two overlying layers.

**Metric.** The maximum absolute residual, in seconds, of the best-fitting
two-layer model fitted to all first arrivals between $10$ and $300\ \mathrm{m}$;
and, separately, the depth error of that fit against the true depth to the
$2200\ \mathrm{m\,s^{-1}}$ layer.

**Control.** The same two-layer fit applied to a genuine two-layer model with the
same end-member velocities. This is necessary: without it, a zero residual could be
attributed to a bug.

**Expected outcome.** The residual of the three-layer data is at the numerical
floor (the module demonstration obtains exactly $0.000\ \mathrm{s}$ and
$0.000\ \mathrm{s}$ RMS over 91 traces), identical to the control, while the
depth error is tens of per cent ($+53.1\%$ in the lesson's model and $+76.9\%$ in
★4). The demonstration is complete when a reader can say which single number
changed and which did not: the residual did not, and the depth did.
