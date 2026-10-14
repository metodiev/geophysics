# Solutions — 08-02-05 Airborne Magnetic Surveys and Compensation

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [05 Airborne Magnetic Surveys and Compensation](../05-airborne-magnetic-surveys.md).

---

## ★1 — The three interference terms

$$I(t) = \sum_k a_k u_k \;+\; \sum_{i\le j} b_{ij}u_iu_j
\;+\; \sum_{i,j} c_{ij}u_i\dot u_j,$$

with $\mathbf{u}$ the ambient field direction in the aircraft frame.

| term | physical origin | coefficients |
|---|---|---|
| permanent | fixed remanent magnetisation of the airframe, projected on the sensor | 3 |
| induced | airframe magnetisation $\mathbf{M} = \kappa\mathbf{H}$, quadratic in the field direction | 6 |
| eddy | currents driven by $\mathrm{d}\Phi/\mathrm{d}t$ in conducting structure | 9 |
| **total** | | **18** |

All three scale with the ambient field, so the coefficients are aircraft
properties rather than properties of the flight latitude.

---

## ★2 — Anomaly at two altitudes

$$|B| = \frac{\mu_0}{4\pi}\frac{2m}{r^{3}}
= 1.0\times10^{-7}\times\frac{2\times800}{r^{3}}.$$

At the surface, $r = 25$ m:

$$|B| = 1.6\times10^{-4}/25^{3} = 1.6\times10^{-4}/1.5625\times10^{4}
= 1.024\times10^{-8}\ \mathrm{T} = 10.240\ \mathrm{nT}.$$

At 50 m altitude, $r = 25+50 = 75$ m:

$$|B| = 1.6\times10^{-4}/75^{3} = 1.6\times10^{-4}/4.21875\times10^{5}
= 3.793\times10^{-10}\ \mathrm{T} = 0.3793\ \mathrm{nT}.$$

$$\text{fraction retained} = \frac{0.3793}{10.240} = 0.03704 = 3.704\%.$$

Check: $(25/75)^{3} = 1/27 = 0.03704$ ✔ — the cube law is all that is happening.

---

## ★3 — Line spacing

**Quarter-wavelength rule:** $s = \lambda/4 = 250/4 = 62.5\ \mathrm{m}$.

**Nyquist minimum:** $s = \lambda/2 = 125\ \mathrm{m}$.

The Nyquist value is the point beyond which the anomaly is aliased; it is the
failure threshold, not a target. Designing at Nyquist leaves the amplitude at
$2\sin(\pi/2)/2 = 100\%$ in the best phase and **0%** in the worst phase
(lesson 04, ★5), which is why the quarter-wavelength rule exists.

---

## ★4 — Choosing a model order

| model | residual (nT) | compared with the $0.35$ nT floor |
|---|---|---|
| 3 coefficients | 2.10 | 6.0× above — inadequate |
| 9 coefficients | 0.41 | 1.17× above — indistinguishable from the floor |
| 18 coefficients | 0.39 | 1.11× above — indistinguishable from the floor |

**Adopt the 9-coefficient model.** The 18-coefficient residual is not
distinguishable from the 9-coefficient residual given a $0.35\ \mathrm{nT}$ noise
floor, so the nine extra coefficients buy nothing on this flight and will amplify
noise when applied to another one. This is a parsimony decision made *against*
the better-fitting model, and it is only defensible because the noise floor is
stated.

A quantitative statement of the comparison: the residual reduction from 9 to 18
terms is $0.41 \to 0.39\ \mathrm{nT}$, i.e. a variance reduction of
$1 - (0.39/0.41)^{2} = 9.5\%$, against an expected reduction of order
$9/18 = 50\%$ if the extra nine coefficients were measuring real signal. As a
rough $F$-test guide, nine coefficients would need to reduce the residual variance
by appreciably more than the noise's own fluctuation to be justified.

---

## ★5 — A stale solution

If the interference were entirely permanent, the interference is
$\mathbf{a}\cdot\mathbf{u}$ with $|\mathbf{a}|$ of the order of the rms value
divided by the rms of $\mathbf{u}$'s components. A 25% change in the permanent
coefficients leaves a residual of order

$$0.25\times4.0\ \mathrm{nT} = 1.0\ \mathrm{nT}\ \text{rms}.$$

The demonstration's equivalent experiment (a 20% change) measured
$0.522\ \mathrm{nT}$ rms, consistent with this scaling given the different
$\mathbf{u}$ statistics.

**Processing consequence.** The residual is **correlated with attitude**, so it
repeats consistently along each flight line and appears as a smooth anomaly with
the anomaly's own spatial wavelength. Levelling cannot remove it, because it is
different on each line; the only fixes are to re-solve the compensation, or to
discard the affected line. This is why the figure of merit is computed per
flight, not per survey.

---

## ★6 — Design numbers

**(a) Line spacing.** $s = \lambda_{\min}/4 = 350/4 = 87.5\ \mathrm{m}$.

**(b) Along-line sample interval.** The same rule applies along track:
$\Delta x = 87.5\ \mathrm{m}$ would be the *minimum* to satisfy the rule with the
same wavelength; surveys normally take it finer, typically by using the sensor's
natural rate. With the rule applied identically in both directions,
$\Delta x = 87.5\ \mathrm{m}$; the constraint that usually binds is the sensor's
reading rate, since a $70\ \mathrm{m\,s^{-1}}$ aircraft covers $87.5\ \mathrm{m}$
in 1.25 s and a pulsed sensor may not deliver a reading that fast.

**(c) Retention at 700 m wavelength with $s = 87.5$ m.** The worst-case retention
over the anomaly's phase is $\cos(\pi s/\lambda) = \cos(\pi\times87.5/700)
= \cos(0.3927) = 0.9239$: 92.4%. Equivalently, $s/\lambda = 0.125$, which is the
$7.6\%$ loss case of the lesson's table. ✔ Note the transfer-function point: the
*spacing* passed the 700 m anomaly with $92\%$ of its amplitude, and the
$2\sin(\pi s/\lambda)$ factor of a *difference* would be the relevant one only for
a gradiometer, not for a total-field survey.

---

## ★7 — Testing a linear compensation model (specification)

**Manoeuvres.** Fly at least three manoeuvre types, each repeated at two headings
$90^{\circ}$ apart and at two field magnitudes if the survey covers a wide
latitude range: (i) a pitch oscillation, (ii) a roll oscillation, (iii) a yaw
oscillation, each of several cycles at differing amplitudes, over magnetically
quiet ground. Repeat at high and low altitude if the field direction at the sensor
differs appreciably.

**Models.** Fit (a) the 18-term linear Tolles–Lawson model, and (b) an extended
model that adds terms quadratic in $|\mathbf{B}|$ and third-order products
$u_iu_ju_k$. The extended model is the *alternative hypothesis*: it exists to be
rejected.

**Metric.** The **figure of merit**: fit on one manoeuvre and predict on a
held-out manoeuvre, reporting
$\mathrm{FOM} = \mathrm{rms}(\text{prediction residual})/\mathrm{rms}(\text{noise
floor})$, with the noise floor measured separately in a quiet, level interval.

**Falsification of the linear model.** The linear model is falsified if the
extended model reduces the held-out residual by more than the noise's own
fluctuation, *and* the improvement is reproducible across flights. A cruise flight
(level, no manoeuvre, over quiet ground) is the decisive test: any residual there
that exceeds the noise floor and correlates with heading or with the field
magnitude cannot be explained by the linear model at all, because $\mathbf{u}$ is
nearly constant during cruise.

---

## ★8 — Altitude, apparent depth, and the drape

**Forward model.** For a dipole at depth $d$ observed at height $h$ on the axis,

$$|B(h)| = \frac{\mu_0}{4\pi}\frac{2m}{(d+h)^{3}}.$$

An inversion that assumes $h = 0$ and matches the amplitude returns a depth
$\hat d$ satisfying $(d+h)^{3} = \hat d^{3}$, i.e. $\hat d = d + h$ **for the
on-axis amplitude alone**. Off axis the relation is not a simple shift, because
the anomaly's shape as well as its amplitude changes with height: a deeper or
higher body has a broader, smoother anomaly, so amplitude and width together carry
the height information only if one of them is independently known. That is the
classic depth–height trade-off, and it is the reason aeromagnetic depth estimates
are always quoted with an assumed flight height.

**Why a varying drape imposes an apparent gradient.** If $h$ varies along a line
by $\Delta h$ over a distance $\Delta x$, then even over a uniform target the
measured field varies, because the anomaly is a function of $d + h$. The apparent
gradient is approximately

$$\frac{\partial B}{\partial x} \approx \frac{\partial B}{\partial h}
\frac{\mathrm{d}h}{\mathrm{d}x}
= -3\frac{B}{d+h}\frac{\mathrm{d}h}{\mathrm{d}x}.$$

For an anomaly of $20\ \mathrm{nT}$ at $d+h = 100\ \mathrm{m}$ with a drape
changing by $1\ \mathrm{m}$ per $100\ \mathrm{m}$ of track
($\mathrm{d}h/\mathrm{d}x = 0.01$), this gives
$-3\times20/100\times0.01 = -0.006\ \mathrm{nT\,m^{-1}}$ over the anomaly's own
extent — small in absolute terms but shaped exactly like the anomaly, so it biases
its apparent width.

**The test that distinguishes it from geology.** A drape-induced gradient is a
function of the **flight height**, so it changes when the same line is re-flown at
a different (deliberately offset) altitude, while a geological gradient does not.
Re-flying a subset of lines at a second height is therefore the standard
discrimination test, and it also provides the data needed to *invert* for height
rather than assume it.
