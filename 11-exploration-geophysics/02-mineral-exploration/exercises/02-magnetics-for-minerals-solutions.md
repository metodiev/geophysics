# Solutions — 11-02-02 Magnetics for IOCG, Porphyry and Magmatic Sulphides

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All properties, directions and geometries are **SYNTHETIC**.

Lesson: [02 Magnetics for Minerals](../02-magnetics-for-minerals.md).

---

## ★1 — Induced magnetisation of a sphere

$$H_0 = \frac{B_0}{\mu_0} = \frac{52\times10^{-6}}{4\pi\times10^{-7}}
= 41.380\ \mathrm{A\,m^{-1}}, \qquad
V = \frac{4}{3}\pi(100)^{3} = 4.18879\times10^{6}\ \mathrm{m^{3}}.$$

Linear: $M = \kappa H_0 = 0.05(41.380) = 2.0690\ \mathrm{A\,m^{-1}}$.

Demagnetised (sphere, $N = 1/3$):
$$M = \frac{\kappa H_0}{1+\kappa/3} = \frac{2.0690}{1.016667}
= 2.0351\ \mathrm{A\,m^{-1}}\quad(-1.6\%).$$

$$m = MV = 2.0351 \times 4.18879\times10^{6} = 8.5246\times10^{6}\ \mathrm{A\,m^{2}}.$$

At $z = 400\ \mathrm{m}$, on the axis:

$$\Delta B = 10^{-7}\frac{2m}{z^{3}} = 10^{-7}
\frac{2(8.5246\times10^{6})}{6.4\times10^{7}} = 2.6640\times10^{-8}\ \mathrm{T}
= 26.64\ \mathrm{nT}.$$

At $\kappa = 0.05$ the self-demagnetisation correction is only $1.6\%$, which is why
it is safely neglected for weakly magnetic rocks and unsafe for magnetite-rich ones
(★4).

---

## ★2 — Total dipole moment

$Q = 3$ means $|\mathbf{m}_r| = 3|\mathbf{m}_i|$. With
$|\mathbf{m}_i| = MV$ from ★1's demagnetised value:

$$|\mathbf{m}_i| = 8.5246\times10^{6}, \qquad
|\mathbf{m}_r| = 2.5574\times10^{7}\ \mathrm{A\,m^{2}}.$$

Resolving with $D = 0$ for both so the profiles lie in the $x$–$z$ plane:

$$\mathbf{m}_i = 8.5246\times10^{6}(\cos 55°, 0, \sin 55°)
= (4.8895, 0, 6.9831)\times10^{6},$$
$$\mathbf{m}_r = 2.5574\times10^{7}(\cos(-50°), 0, \sin(-50°))
= (1.6438, 0, -1.9590)\times10^{7},$$
$$\mathbf{m}_{\text{tot}} = (2.1328, 0, -1.2607)\times10^{7}\ \mathrm{A\,m^{2}},$$

$$|\mathbf{m}_{\text{tot}}| = 2.4776\times10^{7}\ \mathrm{A\,m^{2}},\qquad
I_{\text{tot}} = \arctan\!\left(\frac{-1.2607}{2.1328}\right) = -30.6° .$$

The total magnetisation inclination is $-30.6°$ even though the field is at
$+55°$: with $Q = 3$ the remanence has taken control, and any interpretation that
assumes an induced magnetisation will misplace the body and mis-sign the anomaly.

---

## ★3 — Vertical-component anomaly and its zero

$$Z(x) = \frac{\mu_0 m}{4\pi}\frac{2h^{2}-x^{2}}{(x^{2}+h^{2})^{5/2}}.$$

$Z = 0$ where $2h^{2} = x^{2}$, i.e. $x = \pm\sqrt{2}\,h = \pm1.4142\,h$. The zero
crossings therefore scale with depth exactly, which is the basis of several
"inflection-point" depth rules: their depth estimate is proportional to a measured
width, and therefore inherits the magnetisation-direction bias measured in the
lesson.

---

## ★4 — Self-demagnetisation factor at $\kappa = 2$

$$\frac{\kappa H_0}{\kappa H_0/(1+\kappa/3)} = 1+\frac{\kappa}{3}
= 1 + 0.6667 = 1.667 .$$

The linear formula over-predicts the magnetisation (and therefore the anomaly) by
$66.7\%$. Limiting value:

$$M \to \frac{\kappa H_0}{N\kappa} = \frac{H_0}{N} = 3H_0
= 3(41.380) = 124.14\ \mathrm{A\,m^{-1}}$$

for a sphere. **A rock cannot be magnetised beyond $3H_0$ in this model however
large its susceptibility**, because its own field cancels the applied one. This is
the reason a susceptibility map is not proportional to an anomaly map.

---

## ★5 — Classifying a profile by its peak/trough ratio

$$\text{ratio} = \frac{820}{1450} = 0.566 .$$

Against the lesson's model values: induced-dominated $5.53$, mixed ($Q = 1.5$)
$0.80$, remanence-dominated $0.188$. The observation lies between the mixed and
remanence-dominated cases, and nearer the top of that interval: **the total
magnetisation is significantly rotated by remanence, though not dominated by it.**

The ratio is the right diagnostic because it is dimensionless and independent of the
body's size and depth: it depends only on the *directions* of the total
magnetisation and the ambient field. The peak displacement ($180\ \mathrm{m}$,
comparable to the depth) reinforces the conclusion and provides a second,
independent measurement of the same direction. Note what the ratio cannot do: it
cannot say whether the remanence is carried by magnetite, pyrrhotite or hematite,
nor what the grade is.

---

## ★6 — Half-width and depth

Half-maximum condition with $u = x^{2}/h^{2}$:

$$\frac{2-u}{(1+u)^{5/2}} = 1 \;\Longrightarrow\; u = 0.250683
\;\Longrightarrow\; \frac{x_{1/2}}{h} = 0.500683 .$$

At $h = 250\ \mathrm{m}$: $x_{1/2} = 0.500683(250) = 125.17\ \mathrm{m}$.

Inverting a measured $x_{1/2} = 130\ \mathrm{m}$:

$$h = \frac{130}{0.500683} = 259.65\ \mathrm{m}.$$

**Sign of the error if the profile were bipolar:** there is no error to sign — the
rule is *undefined*. The half-maximum condition presumes a single dominant
positive peak; on a bipolar profile the "half-maximum" level is crossed on a
descending limb that has nothing to do with the depth, and the numerical answer
becomes arbitrarily large (the demonstration reports $1.3\times10^{6}\ \mathrm{m}$
when the rule is applied blindly to a bipolar profile). The detection test is
mechanical: require peak $> 3\times|\text{trough}|$ before applying the rule.

---

## ★7 — Scale invariance

The dipole anomaly depends on the body only through $(R/z)^{3}$, so equal peak
amplitude means equal $R/z$:

- $R = 200\ \mathrm{m}$ at $z = 320\ \mathrm{m}$ gives $R/z = 0.625$. A body of
  $R = 400\ \mathrm{m}$ therefore requires
  $$z = \frac{R}{0.625} = \frac{400}{0.625} = 640\ \mathrm{m}.$$
- A body at $z = 160\ \mathrm{m}$ requires
  $$R = 0.625(160) = 100\ \mathrm{m}.$$

**Both bodies produce an identical anomaly.** This is an exact ambiguity of the
dipole field: with $\kappa$, $Q$ and the direction fixed, the amplitude constrains
only $R/z$. The width of the profile is the sole depth information, and it is
distorted by the magnetisation direction — the two effects are entangled, which is
why a magnetic depth estimate should always be quoted as a range and with the
direction assumption stated.

---

## ★8 — Amplitude at $x = 0$ with and without remanence

Using the lesson's SYNTHETIC body ($R = 200\ \mathrm{m}$, $z = 300\ \mathrm{m}$,
$\kappa = 0.20$, $Q = 1.5$, field at $60°$, remanence at $-30°$):

**(a) induced only** ($\mathbf{m}$ parallel to the field):
$$\Delta T(0) = +1157.4\ \mathrm{nT}.$$

**(b) total magnetisation** (induced plus remanence):
$$\Delta T(0) = -646.8\ \mathrm{nT}.$$

**Ratio:** $-0.559$; the *sign* has reversed and the magnitude has fallen by
$44\%$.

**Which is the correct prediction?** Neither, without evidence: (a) is the
prediction of the assumption "the rock carries no remanence", which is a statement
about the rock, not about the method. For a **survey specification** the defensible
practice is to predict *both* and to size the survey so that the weaker
(remanence-rotated) amplitude is still detectable — here $647\ \mathrm{nT}$ against
$1157\ \mathrm{nT}$, a factor of $1.8$ in amplitude and therefore a factor of
$1.8^{1/3} = 1.22$ in the depth at which the same signal-to-noise is reached. A
specification that used (a) alone would overstate the depth of detection by
$\sim\!20\%$ in this example, and by much more where $Q$ is larger and the
rotation is closer to anti-parallel.

---

## ★9 — Fitting the magnetisation direction (specification)

**Parameters.** With a fixed body shape and a *unit* magnetisation direction
$\hat{\mathbf{u}}$, the anomaly is *linear* in the amplitude $\alpha$:
$\Delta T = \alpha f(\hat{\mathbf{u}}; x)$ where $f$ is the unit-moment profile.
So the unknowns are $(\alpha, \hat{\mathbf{u}}, \text{geometry})$ — for a sphere,
$(\alpha, I, D, x_0, y_0, z)$: seven parameters, but the amplitude and direction
interact with the depth, which is the identifiability problem.

**Penalty function.** Weighted least squares on the profile,
$\chi^{2} = \sum_i w_i [\Delta T_i - \alpha f_i(\hat{\mathbf{u}}; \theta)]^{2}$
with $w_i = 1/\sigma^{2}$. For a fixed direction, $\alpha$ is solved linearly
($\hat{\alpha} = \sum w f \Delta T / \sum w f^{2}$), so the search is over the
direction and geometry only.

**Numerical experiment on the lesson's body.** Fix $R = 200\ \mathrm{m}$ and
$z = 300\ \mathrm{m}$ (known), fix the field at $60°$, and vary the assumed
magnetisation inclination $I$ and declination $D$ on a $5°$ grid from $-90°$ to
$90°$, computing the residual against the *mixed* profile. What is found is that
the minimum is a **valley, not a point**: to first order the anomaly depends on the
dipole moment mainly through its projection onto the ambient field direction and
through the transverse component that controls asymmetry, so $I$ and the ratio
$\alpha/z^{3}$ trade off. The residual along the valley varies by less than the
noise for a wide range of $\alpha$, which is the degeneracy.

**Diagnostics.** (1) The condition number of the Jacobian at the minimum; (2) the
profile of $\chi^{2}$ along the valley's flat direction, reported as the range of
directions within $\Delta\chi^{2} = 1$; (3) a bootstrap over profile subsets to see
whether $I$ and $\alpha$ move together (they do). **If the direction's
one-sigma range spans more than about $30°$, the data do not constrain the
magnetisation direction and any RTP or half-width depth derived from an assumed
direction must be reported as conditional.**

---

## ★10 — Terrain and draped sensor height

The half-width rule assumes a constant sensor height $h$. With a draped survey the
sensor is $60\ \mathrm{m}$ above ground, and ground elevation varies by up to
$80\ \mathrm{m}$ across the anomaly, so $h$ varies between roughly
$h_{\min}$ and $h_{\min}+80\ \mathrm{m}$ in aircraft-referenced terms — equivalently
the *depth to the body* as seen by the rule varies by up to $80\ \mathrm{m}$.

Quantitatively, for a body at $300\ \mathrm{m}$ below the highest ground on the
profile and $380\ \mathrm{m}$ below the lowest, the apparent half-widths are
$0.500683(300) = 150.2\ \mathrm{m}$ and $0.500683(380) = 190.3\ \mathrm{m}$ — a
$27\%$ range in apparent depth for the same body.

**Systematic or random?** Systematic with respect to the *sensor-to-body* geometry,
not with respect to slope direction alone: the error follows the terrain profile,
so it is *reproducible* and correlatable with topography, which means it can be, and
must be, corrected by levelling the anomaly to a constant datum using the measured
radar/laser altimeter height. Because the error is systematic, it does not average
out with more flight lines: adjacent lines flown over the same terrain share it.
The diagnostic is a plot of the residual against terrain elevation after
interpretation — a correlation there is the signature of an uncorrected height.

---

## ★11 — Internal field of a magnetised sphere (numerical experiment)

**Experiment.** Discretise a sphere of radius $R = 200\ \mathrm{m}$ on a
$40^{3}$ grid of cubic cells with volume $V_c$; assign each cell the uniform
magnetisation $\mathbf{M}$; sum the dipole fields at a probe point inside the
sphere, at its centre, and divide by $\mu_0$ to obtain $H_{\text{int}}$; compare
with the ellipsoid prediction $H_{\text{int}} = H_0 - NM$ with $N = 1/3$.

**Result and interpretation.** At the exact centre the summation converges slowly
(the field of a dipole shell is conditionally convergent at the origin, and a
finite grid leaves a residual of order the cell size over $R$), so the comparison
must be made with cells *excluded* from a small region around the probe, and the
result extrapolated in cell size. What the experiment shows is:

1. For a **sphere** the extrapolated value agrees with $H_0 - M/3$ to within the
   discretisation error, confirming both the demagnetising factor and the dipole
   superposition used throughout the lesson.
2. For a **non-ellipsoidal** body (repeat with a cube of the same volume) the
   ratio $H_{\text{int}}/H_0$ **depends on the probe position inside the body**:
   there is no single $N$ that reproduces the internal field everywhere.

That second result is why "the" demagnetising factor of a real orebody is a
convention rather than a measurement: it is shape-, orientation- and
position-dependent, so any quoted $N$ must come with the ellipsoid it belongs to.
The consequence for practice is that self-demagnetisation corrections should be
reported as a range, and that the linear formula $M = \kappa H_0$ is an upper bound
rather than an estimate whenever $\kappa$ is large.
