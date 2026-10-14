# Solutions — 17-04-01 GNSS Principles and Signal Structure

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [01 GNSS Principles](../01-gnss-principles.md).

---

## ★1 — The observation equation

$$P = \rho + c\left(\delta t_r - \delta t^{s}\right) + I + T + M + \varepsilon,
\qquad \rho = \left|\mathbf{x}^{s} - \mathbf{x}_r\right|.$$

**(a) Solved for:** the receiver position $(x, y, z)$ and the receiver clock
offset $\delta t_r$ — four unknowns, hence four satellites.

**(b) Modelled or measured:** the ionospheric delay $I$, the tropospheric delay
$T$, and the satellite clock offset $\delta t^{s}$ (with the satellite position,
from the broadcast or precise ephemeris). Multipath $M$ and receiver noise
$\varepsilon$ are neither modelled nor solved for in the standard solution; they
are mitigated (elevation weighting, sidereal filtering) and left in the residuals.

---

## ★2 — Ionospheric delay at two frequencies

$$I = \frac{40.308\times\mathrm{TEC}}{f^{2}}, \qquad
\mathrm{TEC} = 45\ \mathrm{TECU} = 4.5\times10^{17}\ \mathrm{m^{-2}}.$$

$$I_1 = \frac{40.308 \times 4.5\times10^{17}}{(1.57542\times10^{9})^{2}}
= \frac{1.81386\times10^{19}}{2.481947\times10^{18}} = 7.3082\ \mathrm{m}.$$

$$I_2 = \frac{1.81386\times10^{19}}{(1.22760\times10^{9})^{2}}
= \frac{1.81386\times10^{19}}{1.506999\times10^{18}} = 12.0366\ \mathrm{m}.$$

$$\frac{I_1}{I_2} = \frac{7.3082}{12.0366} = 0.60717,
\qquad
\left(\frac{f_2}{f_1}\right)^{2} = \left(\frac{1.22760}{1.57542}\right)^{2}
= 0.60717. \;\checkmark$$

The ratio is frequency-only: it holds for every electron content, which is what
allows TEC to be estimated from the difference and removed from the sum.

---

## ★3 — From DOP to scatter

$$\sigma_{\text{hor}} = \text{HDOP}\times\sigma = 1.4\times0.25
= 0.35\ \mathrm{m}.$$

**Why VDOP exceeds HDOP:** the satellites are all *above* the receiver, so the
look vectors span a wide range of azimuths (good horizontal leverage) but only a
narrow range of elevation angles (poor vertical leverage). The vertical direction
can be traded against the clock offset almost one-for-one whenever the elevations
are similar, which inflates the vertical variance. This asymmetry — vertical
typically two to three times worse than horizontal — is why GNSS height is the
noisiest coordinate, and why a low-elevation satellite is valuable for height
even though its atmosphere errors are largest.

---

## ★4 — A singular geometry

**(a)** If two satellites share a direction, their unit vectors are equal,
$\mathbf{u}_1 = \mathbf{u}_2$, so the first three columns of the two rows are
identical and the fourth column (1 for both) is identical too:
$$G = \begin{pmatrix} -\mathbf{u}^{\mathsf T} & 1 \\ -\mathbf{u}^{\mathsf T} & 1 \\
\vdots & \vdots \end{pmatrix}.$$
The rows are linearly dependent, so $\operatorname{rank}(G) \le 3 < 4$ and the
normal matrix $G^{\mathsf T}G$ is singular.

**(b)** The DOP is then **infinite** — no finite noise level gives a finite
position — because the two measurements are the same measurement. Numerically, the
practical case is not exactly equal directions but *clustered* ones: the lesson
measures GDOP $= 247.09$ for a clustered constellation against $3.00$ for a
well-spread one, an 82-fold amplification.

**Practice:** a receiver applies an elevation mask (excluding the noisiest
low-elevation satellites), weights observations by elevation, and either waits for
better geometry or accepts a degraded solution — and reports the DOP so the user
can see which happened.

---

## ★5 — The ionosphere-free combination

**(a)** With $D = f_1^{2}-f_2^{2}$,
$$\frac{a}{f_1^{2}} + \frac{b}{f_2^{2}}
= \frac{1}{D}\left(\frac{f_1^{2}}{f_1^{2}} - \frac{f_2^{2}}{f_2^{2}}\right)
= \frac{1-1}{D} = 0. \;\checkmark$$
So an ionospheric delay $I = K/f^{2}$ contributes
$aK/f_1^{2} + bK/f_2^{2} = K\times0 = 0$ for any $K$, i.e. the combination is
ionosphere-free identically. Also $a + b = (f_1^{2}-f_2^{2})/D = 1$, so a common
range is preserved exactly.

**(b)**
$$\sigma_{\text{IF}} = \sqrt{a^{2}\sigma_1^{2} + b^{2}\sigma_2^{2}}
= \sqrt{(2.545728\times0.30)^{2} + (1.545728\times0.40)^{2}}$$
$$= \sqrt{0.583476 + 0.382113} = \sqrt{0.965589} = 0.9826\ \mathrm{m}.$$

Note that with unequal sigmas the penalty is smaller than the equal-sigma factor
of 2.9783 would suggest — but it is still a factor of about 2.5 over the better
single frequency.

---

## ★6 — Redundancy and scatter

**(a)** $6 - 4 = 2$ redundant observations. They buy (i) a *check*: the
post-fit residuals should be consistent with the assumed noise, and a
$\chi^{2}$ or residual test detects blunders and unmodelled biases; and (ii)
*reduction*: the estimate variance falls with the number and geometry of
observations through $(G^{\mathsf T}G)^{-1}$.

**(b)** $\sigma_{\text{3D}} = \text{GDOP}\times\sigma = 6\times0.5 = 3.0\ \mathrm{m}$.

---

## ★7 — A 1 cm horizontal, 3 cm vertical session (specification)

**Observation type and duration.** Carrier-phase observations on both frequencies
(determining why in a moment), with the integer ambiguities resolved. Duration:
long enough that the geometry changes appreciably — the satellites repeat their
geometry roughly every sidereal day, so a session of several hours is the minimum
that gives a genuinely changing DOP; a full day is the standard for
centimetre-level absolute work because it averages the multipath and
multipath-geometry coupling.

**Frequency combination.** Dual frequency, because the ionosphere at 45 TECU
reaches 7.3 m at $f_1$ (exercise ★2) — hundreds of times the target accuracy. The
ionosphere-free combination removes it at a cost of 2.98 times the noise, which is
irrelevant when the noise is millimetres.

**DOP requirement.** For a 1 cm horizontal goal with 5 mm phase noise, the
requirement $\text{HDOP}\times 0.005 \le 0.010$ gives HDOP $\le 2$. In practice
one requires PDOP $< 3$ and inspects the DOP *time series* rather than its
average, since a brief excursion dominates the formal covariance.

**Corrections.** Precise satellite orbits and clocks (not broadcast),
elevation-dependent weighting, the tropospheric delay with a mapping function and
an estimated residual (the lesson's Section 3 of the next lesson), ocean and
solid-Earth tide loading, antenna phase-centre offsets and variations, and the
reference-frame realisation.

**Validation.** (i) Residual rms consistent with the assumed noise — a larger
residual means an unmodelled effect, not a better solution. (ii) A repeatability
test: solutions from independent days must agree within their formal errors, and
that scatter — not the formal covariance — is the honest uncertainty. (iii)
Antenna swap or a local tie to an independent monument to test for a station
bias. The vertical target of 3 cm is set by the wet troposphere and by VDOP;
claiming 1 cm vertically would require a much longer session and a very good
troposphere model.

---

## ★8 — What is absorbed, and what moves the position

**(a)** A delay pattern $I_k$ contributes to the observations a vector
$\mathbf{I} = (I_1,\ldots,I_n)$. The estimator projects the observations onto the
column space of $G$. If $\mathbf{I}$ lies *within* that column space, it is
indistinguishable from a change in the parameters:

- a **constant** pattern $\mathbf{I} = I_0\mathbf{1}$ is exactly the fourth column
  of $G$ (the clock), so it is absorbed entirely by the clock;
- a pattern that varies with the *geometry* projects partly onto the position
  columns and moves the position.

**(b) Condition.** $\mathbf{I}$ is completely absorbed iff it lies in the column
space of $G$, i.e. iff it can be written as
$I_k = \mathbf{u}_k\cdot\mathbf{a} + b$ for some vector $\mathbf{a}$ and scalar
$b$ — a "linear in the look vector plus constant" pattern. Any delay pattern with
structure orthogonal to that subspace moves the solution. Since a real
ionosphere has azimuthal and elevation structure, part of it always moves the
position; that part is what the DOP amplifies.

**(c)** If $a + b \ne 1$ the combination would *scale* the geometric range, so
the estimated position would be biased by a factor of order $(a+b)$ times the
range — a kilometres-level error. The condition $a+b=1$ is therefore what makes
the combination a *range* measurement, and hence usable for positioning; without
it the combination could still estimate the ionosphere from the difference of the
two frequencies, but its sum could not be used to locate anything.
