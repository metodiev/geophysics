# Solutions — 10-06-02 Monitoring Dams, Embankments and Foundations

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Line-electrode (2-D) conventions throughout: current per unit electrode
> length, $\rho_a = \pi\,\Delta V/(2I\ln 2)$.

Lesson: [02 Monitoring Dams, Embankments and Foundations](../02-geotechnical-monitoring.md).

---

## ★1 — The array factor from the analytic potential

$$\Delta V = \frac{2I\rho}{\pi}\ln 2
= \frac{2(0.05)(50)}{\pi}(0.693147) = 1.1032\ \mathrm{V},$$
$$\text{transfer resistance} = \frac{\Delta V}{I} = \frac{1.1032}{0.05}
= 22.064\ \Omega\,\mathrm{m},$$
$$\rho_a = \frac{\pi\,\Delta V}{2I\ln 2}
= \frac{\pi(1.1032)}{2(0.05)(0.693147)} = 50.00\ \Omega\,\mathrm{m} .$$

$\rho_a$ **must** equal the true resistivity because the array factor was derived
for the homogeneous half-space itself: substituting $V(r) = -(I\rho/\pi)\ln r$ into
the four-electrode difference and then into the formula leaves $\rho_a = \rho$
exactly, with the factors of $\pi$ and $\ln 2$ cancelling. That is the point of the exercise: the factor is not a
convention to be looked up, it is a consequence of the Green's function. The
demonstration confirms it numerically, printing $\rho_a = 50.000000$ against
$1/\sigma_0 = 50.000000$.

**Units note.** With $I$ per unit electrode length the transfer resistance has
units of $\Omega\,\mathrm{m}$; with a point electrode it would be $\Omega$. Mixing
the two conventions shifts the answer by $4a\ln 2 = 11.1$ at
$a = 4\ \mathrm{m}$.

---

## ★2 — The depth decay of the anomaly

$$\frac{-14.66}{-29.14} = 0.503, \qquad
\frac{-7.16}{-14.66} = 0.488 .$$

The anomaly **halves for each additional metre of front depth** over this range —
a decay of roughly $0.5$ per metre, i.e. an amplitude that falls by a factor of
about eight between $1$ and $4\ \mathrm{m}$. The rule of thumb it supports: for a
thin conductive layer at depth $z$ with a fixed spacing, the anomaly decays roughly
exponentially with a scale of order the spacing, so *every extra metre of depth
costs about a factor of two in detectability* — which is why the feasibility table
of the lesson is produced before installation.

---

## ★3 — Property versus decision

An ERT monitoring array measures a **transfer resistance** between electrode pairs
at each epoch, which inverts to a conductivity distribution and, through a
petrophysical relation, to a water-content change over a volume. The engineer's
question is whether the **factor of safety** of the asset is changing, which is a
question about effective stress, pore pressure and shear strength at a critical
surface. The two are connected by a mechanical model and a calibration — not by
geophysics, and not by an inversion alone.

---

## ★★4 — From resistivity change to water content

**Conductivity.** For a uniform relative change,
$\rho_a = \rho_0/(1+\Delta\sigma/\sigma)$, so

$$\frac{\Delta\sigma}{\sigma} = \frac{-\Delta\rho_a/\rho_a}{1+\Delta\rho_a/\rho_a}
= \frac{0.1466}{1-0.1466} = \frac{0.1466}{0.8534} = +17.18\%.$$

**Water content.** With $\sigma = \sigma_w\theta^{m}$, $m = 1.5$ and fixed
$\sigma_w$:

$$\frac{\Delta\theta}{\theta} = \frac{1}{m}\frac{\Delta\sigma}{\sigma}
= \frac{0.1718}{1.5} = +11.5\%,$$

so a water content of $0.200$ becomes $0.223$.

**Largest assumptions.** (i) **Uniformity**: the change is confined to a
$1\ \mathrm{m}$ layer, so the layer's own conductivity change is larger than the
apparent change by roughly $1/W$, where $W$ is that layer's share of the array's
sensitivity — with $W = 0.4$ the layer change would be $+43\%$ rather than
$+17\%$. (ii) **Unchanged pore-water conductivity**: a $17\%$ conductivity rise can
be produced by a much smaller water-content rise if the pore water also became
more saline (or by none at all if only the salinity changed). A third assumption,
smaller but real, is that $\phi$ and $m$ are unchanged by the wetting.

---

## ★★5 — Multiplicity for 400 measurements

**Per-test false alarm at $2\sigma$:**
$p = 2[1-\Phi(2)] = 4.55\%$.

**(a) Expected flags under the null:**
$400 \times 0.0455 = 18.2$ measurements.

**(b) Family-wise probability:**
$1-(1-0.0455)^{400} = 1 - 8.1\times10^{-9} \approx 100.0\%$.

**(c) Bonferroni threshold** for a 5% family-wise rate:
$z = \Phi^{-1}(1 - 0.05/(2\times400)) = 3.836$.

**(d) Amplitude penalty:** $3.836/2.000 = 1.918$, i.e. a change must be $92\%$
larger to reach the corrected threshold.

**Interpretation.** With 400 measurements, a report of "eighteen anomalies" at
$2\sigma$ is exactly what noise produces. The correction restores a 5% family-wise
rate but costs almost a factor of two in amplitude — which is why the *second*
defence matters as much: a real anomaly is spatially coherent and has the sign the
physics predicts, and combining the two criteria (threshold plus coherence)
recovers most of the lost power.

---

## ★★6 — Which spacing?

From the measured spacing table, for a front at $4\ \mathrm{m}$:

| spacing | anomaly for a front at 4 m |
|---|---|
| 1 m | $-1.14\%$ |
| 2 m | $-3.83\%$ |
| 4 m | $-8.70\%$ |
| 8 m | $-9.19\%$ |

**Deploy $4$–$8\ \mathrm{m}$ spacing**, expecting $-9\%$ rather than the $-1\%$ a
$1\ \mathrm{m}$ spacing would give — an eightfold difference in detectability for
the same target. The trade is resolution: the larger spacing cannot resolve a
$0.25\ \mathrm{m}$ feature near the surface (its near-surface sensitivity is
poorer), so if the same array must also watch the crest, use two interleaved
spacings rather than one compromise. Reviewing the whole table (Section 3.3 of the
lesson) shows the rule: match the spacing to the depth of the feature you are
defending, and if two depths matter, deploy two spacings.

---

## ★★★7 — A permanent array for a 6 m embankment (specification)

**Layout.** Two lines: one along the crest and one along the toe, each with
electrodes at $2\ \mathrm{m}$ spacing, plus a line up the downstream slope with the
same spacing, giving cross-slope coverage of the target zone. Interleave a second
spacing of $4$–$8\ \mathrm{m}$ on the same electrodes (larger spacings reuse the
same electrodes, so the cost is only in the switching), so that the $2$–$4\
\mathrm{m}$ target is covered by two independent depth weightings.

**Expected anomaly.** From the measured table, a $1\ \mathrm{m}$ thick front of
doubled conductivity at $2\ \mathrm{m}$ gives $-14.7\%$ at $2\ \mathrm{m}$ spacing
and about $-17.9\%$ at $4\ \mathrm{m}$ spacing; at $4\ \mathrm{m}$ depth expect
$-8.7\%$ and $-9.2\%$ respectively. A *modest* front ($+30\%$ conductivity over
$0.25\ \mathrm{m}$) gives only $-1.4\%$ at $2\ \mathrm{m}$ depth — below
detectability — so the design must state which class of target it can see.

**Threshold and multiplicity.** With $1\%$ noise and $N$ quadrupoles per epoch,
set the per-measurement threshold at the Bonferroni value
$z = \Phi^{-1}(1-0.05/(2N))$ and additionally require spatial coherence (at least
three adjacent quadrupoles with the physically expected sign). Report the
detectable change amplitude from the measured sensitivity table, not from a wish.

**Coupling-drift controls.** Buried, backfilled, corrosion-resistant electrodes;
a reciprocity check of a subset at every epoch; logging of injected current and
contact resistance per electrode; and a permanent temperature-and-moisture sensor
at two depths to separate seasonal effects from the target.

**Falsification test.** Before claiming any anomaly, (i) re-measure a *control*
line on the crest where the target cannot reach, (ii) verify that the anomaly
reproduces with a second, independent spacing, and (iii) confirm that the
reciprocity check is clean at that epoch. An anomaly that fails any of the three
is reported as unverified, with the test that failed.

---

## ★★★8 — One quadrupole, $-15\%$ change (specification)

**Test 1: hardware.** Repeat the measurement immediately, then repeat with the
current and potential pairs exchanged (reciprocity). *Expected outcome if
hardware:* the anomaly does not reproduce, or reciprocity fails by more than the
noise. Most single-quadrupole anomalies die here, because dry, frozen or corroded
electrodes change contact resistance directly.

**Test 2: neighbouring quadrupoles sharing the electrodes.** Any real change in the
ground must appear in every quadrupole whose sensitivity includes that volume.
*Expected outcome if real:* at least three adjacent quadrupoles show changes of the
same sign, consistent with each one's sensitivity to a common subsurface change.
*Expected outcome if a single electrode's contact resistance:* the anomaly appears
in every quadrupole containing that electrode, with a *pattern* that depends only
on the electrode, not on the ground — a diagnostic signature, because contact
resistance enters the transfer resistance linearly and independently of geometry.

**Test 3: statistical.** Re-run the epoch's full measurement set and count how many
quadrupoles exceed the *corrected* threshold (Section 5 of the lesson). *Expected
outcome if a fluctuation:* about $(1-0.05/N)$ of the time nothing exceeds it, and
the single outlier disappears or moves.

**Test 4: physics.** Compare the anomaly's *sign* and *magnitude* with the
prediction of a forward model of a plausible change in that cell. *Expected
outcome if real:* the sign matches the prediction for a wetting or a salinity
change, and the magnitude is reproducible with the second spacing.

The tests are ordered by cost: hardware first, because it is both the most likely
cause and the cheapest to test, and because a real change that survives tests 1–3
is one for which the *interpretation* — not the measurement — is the remaining
uncertainty.
