# Solutions — 07-02-05 Airborne and Marine Gravity: Platforms and Eotvos Corrections

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [05 Airborne and Marine Gravity: Platforms and Eotvos Corrections](../05-airborne-marine-gravity.md).

---

## ★1 — Deriving the knots coefficient

The Eötvös correction's Coriolis term is

$$a_{E} = 2\,\Omega\,V\cos\varphi\,\sin\alpha .$$

Converting to mGal and expressing the speed in knots
($V = 0.514444\,v_{\text{kn}}$):

$$2\Omega\times0.514444\times10^{5}
= 2\times7.292115\times10^{-5}\times0.514444\times10^{5}
= 7.50277\ \mathrm{mGal\ per\ knot}.$$

**At the equator, due east** ($\varphi = 0$, $\alpha = 90^\circ$) both
trigonometric factors are unity, so the correction is exactly
$7.503\ \mathrm{mGal}$ per knot. The familiar number is therefore not a constant of
nature but the product of three things: the Earth's rotation rate, the unit
conversion between knots and SI, and the unit conversion between SI and Gal. Quoting
it without deriving it hides all three, and it explains why the coefficient changes
if speeds are given in $\mathrm{km\,h^{-1}}$ or $\mathrm{m\,s^{-1}}$.

---

## ★2 — A ship at $60^\circ$ latitude, heading $135^\circ$

$$a_{E} = 2\times7.292115\times10^{-5}\times8\times\cos60^\circ\times\sin135^\circ
\ \mathrm{m\,s^{-2}}.$$

$$\cos60^\circ = 0.5, \qquad \sin135^\circ = \frac{\sqrt{2}}{2} = 0.70711,$$

$$a_{E} = 1.458423\times10^{-4}\times8\times0.5\times0.70711
= 4.12504\times10^{-4}\ \mathrm{m\,s^{-2}} = 41.250\ \mathrm{mGal}.$$

**Reciprocal heading ($315^\circ$):**
$\sin315^\circ = -0.70711$, so $a_{E} = -41.250\ \mathrm{mGal}$.

**Comment.** Two lines on the same track but in opposite directions differ by
$82.50\ \mathrm{mGal}$ at only $8\ \mathrm{m\,s^{-1}}$. For a target anomaly of a few
milligal, the Eötvös correction must be applied to every line, and a
"two-way" survey along the same track therefore doubles the information available:
the sum of the two directions cancels the Eötvös term to first order, while their
difference measures it — a useful internal check when the navigation is suspect.

---

## ★3 — The centrifugal term in a turn

$$\frac{V^{2}}{R} = \frac{6^{2}}{3000} = 1.2\times10^{-2}\ \mathrm{m\,s^{-2}}
= 1200\ \mathrm{mGal}.$$

**Why turns are avoided.** $1200\ \mathrm{mGal}$ is three orders of magnitude larger
than a typical marine target anomaly, and the direction of the centrifugal
acceleration changes continuously through the turn, so the correction requires the
full attitude and turn-rate history rather than a speed and a heading. The
alternatives are: (i) discard the turn data and rely on cross-overs for continuity,
(ii) sail straight through the turn line and re-run the line, or (iii) model the turn
with a full inertial solution when a gyro-stabilised platform and its feedback record
are available. Everything in the survey's design — line spacing, turn timing, target
accuracy — must account for the fraction of data discarded.

---

## ★★4 — GNSS differentiation noise and the position it demands

$$\sigma_{a} = \sigma_{z}\left(2\pi f\right)^{2}
= 0.02\times\left(2\pi\times0.004\right)^{2}
= 0.02\times2.527\times10^{-3}
= 5.0531\times10^{-5}\ \mathrm{m\,s^{-2}} = 5.053\ \mathrm{mGal}.$$

**Position accuracy for a $1\ \mathrm{mGal}$ contribution:**

$$\sigma_{z} = \frac{1\times10^{-5}}{\left(2\pi\times0.004\right)^{2}}
= \frac{10^{-5}}{2.527\times10^{-3}} = 3.957\times10^{-3}\ \mathrm{m}
\approx 4\ \mathrm{mm}.$$

**Interpretation.** With a 4 mHz hand-off the GNSS must be good to 4 mm to keep its
contribution at a milligal: this is the arithmetic behind "centimetre-level GNSS is
not enough; the hand-off frequency must be lower, or the acceleration measured
directly". Lowering the hand-off to $0.002\ \mathrm{Hz}$ quarters the amplification
(and therefore allows $16\ \mathrm{mm}$ for the same $1\ \mathrm{mGal}$), at the cost
of requiring the accelerometer — or the platform — to cover a wider band. **The
hand-off frequency is the central design parameter of a moving-platform gravity
system**, and it is set by comparing exactly this expression with the accelerometer's
own bias and noise.

---

## ★★5 — Heading sensitivity at $30^\circ$ and $60^\circ$

With $A = 721.88\ \mathrm{mGal}$ at the cardinal east-west heading,

$$\frac{\partial a_{E}}{\partial\alpha} = A\cos\alpha
\ \left[\mathrm{mGal\ per\ radian}\right]
\times\frac{\pi}{180}\ \left[\mathrm{mGal\ per\ degree}\right].$$

| heading | $\cos\alpha$ | sensitivity (mGal/deg) | error for $0.05^\circ$ (mGal) |
|---|---|---|---|
| $30^\circ$ | 0.86603 | $A\times0.86603\times\pi/180 = 10.911$ | 0.546 |
| $60^\circ$ | 0.50000 | $A\times0.5\times\pi/180 = 6.300$ | 0.315 |

**Comment.** The sensitivity falls with the cosine of the heading and is *largest on
the north-south lines*, where the correction itself is zero (the lesson's
counter-intuitive result). A survey that sets a single heading requirement will
either over-specify the east-west lines (where the sensitivity vanishes) or
under-specify the north-south ones. The requirement is per line direction, and it is
computed, not negotiated.

---

## ★★6 — Cross-over count and degrees of freedom

**Cross-over count.** Every east-west line crosses every north-south line once, so

$$N_{\text{cross}} = 8\times6 = 48.$$

**Degrees of freedom.** The model has one bias per line, $8 + 6 = 14$ parameters, and
cross-overs constrain only differences, so the model has a one-parameter gauge
freedom. Fixing one line's bias leaves

$$\text{d.o.f.} = 48 - \left(14 - 1\right) = 48 - 13 = 35.$$

**Why the residual cannot fall below the cross-over noise.** The adjustment
minimises $\sum\left(\Delta_{ij} - b_{i} + b_{j}\right)^{2}$ with $b$ estimated from
the same data, so the expected post-fit residual is
$\sigma\sqrt{\text{d.o.f.}/N} = 0.4\sqrt{35/48} = 0.34\ \mathrm{mGal}$ — *below* the
cross-over noise $\sigma$, because fitting 13 parameters to 48 observations absorbs
part of the scatter. A residual materially *above* $\sigma$ is the signal that the
model is wrong (drift, heading-dependent errors, or an Eötvös error on some lines);
a residual far *below* the prediction indicates over-fitting or an underestimated
noise.

---

## ★★★7 — A $2\ \mathrm{mGal}$ airborne survey design (specification)

**Geometry.** Target a line spacing that samples the anomaly's wavelength: for
crustal-scale targets a 5–10 km spacing is usual; take 5 km. Flight altitude: as low
as turbulence and safety allow, because altitude enters through the free-air term and
because deeper flight means broader anomalies — take 150 m above ground. Airspeed
$70\ \mathrm{m\,s^{-1}}$ ($136\ \mathrm{kn}$) as a compromise between the Eötvös term
(∝ speed) and productivity.

**Line direction.** Fly the *tie lines* perpendicular to the main lines. For the
Eötvös sensitivity, note that the correction's *magnitude* is largest on east-west
lines and its *sensitivity to heading* is largest on north-south lines; this argues
for collecting both directions and using the sum/difference structure, rather than
optimising one.

**Turn policy.** All turns between lines, outside the survey area, and the turn data
discarded; the aircraft must be straight and level for at least 10 s before the line
starts. With $70\ \mathrm{m\,s^{-1}}$ and a 5 km turn radius, the turn takes about
$450\ \mathrm{s}$ and covers a large area, so turn placement sets the usable survey
area.

**Tie lines.** One tie line per 5 main lines, giving cross-overs at every tie. The
cross-over adjustment then determines relative line biases.

**Budget (SYNTHETIC, at $70\ \mathrm{m\,s^{-1}}$, $45^\circ$ latitude).**

| term | mGal | control |
|---|---|---|
| gravimeter noise (0.1 after averaging) | 0.10 | instrument |
| Eötvös, speed error $0.2\ \mathrm{m\,s^{-1}}$ | 2.06 | GNSS velocity |
| Eötvös, heading error $0.1^\circ$ (worst line) | 1.26 | attitude/heading |
| GNSS vertical acceleration, 5 cm at 5 mHz | 4.94 | **raise the hand-off requirement or improve GNSS** |
| accelerometer bias, calibrated to $1\ \mathrm{mGal}$ | 1.00 | calibration |
| terrain/density reduction at 150 m altitude | $<0.5$ | DEM and density |
| **total in quadrature** | $\approx 5.7$ | |

**The design as stated does not meet a $2\ \mathrm{mGal}$ target**, and the dominant
term is the GNSS differentiation noise. Two changes close the gap: (i) lower the
hand-off frequency to $0.002\ \mathrm{Hz}$ and let a calibrated accelerometer cover
more of the band (GNSS term falls to $1.24\ \mathrm{mGal}$); and (ii) improve the
velocity solution to $0.05\ \mathrm{m\,s^{-1}}$, which reduces the Eötvös speed term
to $0.52\ \mathrm{mGal}$. With those, the total is about $1.9\ \mathrm{mGal}$.

**Which single change most improves the result?** Lowering the hand-off frequency:
it attacks the largest term and costs nothing but analysis, provided the
accelerometer's low-frequency bias is calibrated by the cross-over and tie-line
structure.

**Falsification.** Fly a repeat line in the opposite direction: the two lines should
agree to within the budget *after* the Eötvös corrections (the difference of the two
directions doubles the Eötvös error and cancels the gravity signal). A systematic
difference larger than the budget falsifies the navigation error model.

---

## ★★★8 — Choosing the GNSS/accelerometer hand-off (specification)

**Criterion.** The hand-off frequency $f_{h}$ is where the two sensors contribute
equally to the gravity estimate:

$$\sigma_{\text{GNSS}}\left(f_{h}\right) = \sigma_{\text{acc}},$$

with $\sigma_{\text{GNSS}} = \sigma_{z}\left(2\pi f_{h}\right)^{2}$ for the
doubly-differentiated position and $\sigma_{\text{acc}}$ the accelerometer's
short-wavelength noise (including its bias, which is *not* white and therefore must
be assessed in the band above $f_{h}$ only). Rearranged,

$$f_{h} = \frac{1}{2\pi}\sqrt{\frac{\sigma_{\text{acc}}}{\sigma_{z}}}.$$

With the lesson's numbers ($\sigma_{z} = 0.05\ \mathrm{m}$) and a synthetic
accelerometer noise of $1\times10^{-4}\ \mathrm{m\,s^{-2}}$
($10\ \mathrm{mGal}$):

$$f_{h} = \frac{1}{2\pi}\sqrt{\frac{10^{-4}}{0.05}} = \frac{1}{2\pi}\times0.04472
= 7.12\times10^{-3}\ \mathrm{Hz},$$

i.e. a 140 s hand-off. Note how the square root weakens the dependence: a fourfold
improvement in the accelerometer noise only halves the hand-off frequency.

**Test that reveals a wrong hand-off.** Process the same data with two different
$f_{h}$ values (say a factor of two apart) and compare the resulting gravity
profiles. The difference spectrum should be negligible in both sensors' good bands
and should *peak near $f_{h}$*. A systematic bump near the hand-off indicates that
one sensor's error at that frequency is underestimated — the classic signature of a
mis-specified hand-off.

**Expected error spectrum shapes.**

- **Hand-off too high** (the accelerometer is asked to cover frequencies where it is
  worse than GNSS): a *high-frequency* excess of noise in the gravity profile,
  appearing as a rough line whose noise grows with frequency up to the accelerometer
  cut-off.
- **Hand-off too low** (GNSS is asked to cover frequencies where its double
  differentiation is noisy): a *mid-frequency* ramp of noise, growing as $f^{2}$,
  visible as long-wavelength undulations along each line — and, because the GNSS
  solution's error is correlated in time, as a line-to-line *bias* pattern rather
  than white noise.

**Practical statement.** The hand-off must be reported with the survey, because it
determines which sensor's errors dominate which band, and because a reader cannot
assess an airborne gravity map without it.

---

## ★★★9 — A cross-over residual five times the noise (specification)

**Possible causes, and how each appears in the cross-over residuals.**

1. **Line-dependent drift (time-correlated accelerometer or gravimeter bias).** A
   constant-bias model is inadequate, so the residual grows with the *time* between
   the two lines crossing at that point. Signature: residual versus the time
   difference between the two occupations, monotonic; and residuals larger at the
   ends of long lines. Test: add a linear-in-time term per line to the adjustment and
   check whether the residual falls to the noise level.
2. **A heading-dependent error (Eötvös error, or an attitude misalignment).**
   Signature: residual correlated with the *heading of the line*, i.e. opposite signs
   on the eastbound and westbound legs. Test: fit the residual against $\sin\alpha$
   and $V$; a significant coefficient is an Eötvös-scale error, and its size compared
   with the budget identifies the culprit (speed, heading or latitude).
3. **A platform-attitude or levelling error.** Signature: correlated with the
   aircraft's roll/pitch or with turbulence intensity; appears as noise-like
   high-frequency residual that is worse on the noisier lines. Test: regress the
   residual on the measured vertical acceleration variance.
4. **The reduction (terrain or density model).** Signature: spatially coherent with
   topography, identical at all cross-overs in the same area, and shared with any
   ground data in the region. Test: correlate the residual with elevation and with
   the terrain-correction magnitude.
5. **A genuine signal (a short-wavelength anomaly incompletely sampled).** Signature:
   residuals of opposite sign on either side of a suspected source, coherent between
   nearby cross-overs. Test: the residual pattern should follow the anomaly's
   geometry, not the survey's line structure; and it should persist when the
   adjustment model is improved.

**Ranking.** On a moving-platform survey the ordering is almost always (1) and (2)
first — because both are navigation-related and both have the right amplitude to
explain a factor of five — then (3), then (4), then (5) last, because genuine
geological structure rarely correlates with the survey's line geometry.

**The analysis.** Add the candidate terms to the model one at a time and compare the
post-adjustment residual with the model's degrees of freedom:

$$\chi^{2}/\text{d.o.f.} = \frac{1}{\sigma^{2}\left(N - p\right)}
\sum\left(\Delta - \text{model}\right)^{2},$$

accepting or rejecting each extension by the change in $\chi^{2}$ per added
parameter. Stop when $\chi^{2}/\text{d.o.f.} \approx 1$; the terms retained are the
diagnosis, and their magnitudes are the survey's real error budget — which is why
this exercise is not a bookkeeping detail but the step that converts a residual into
an error statement.
