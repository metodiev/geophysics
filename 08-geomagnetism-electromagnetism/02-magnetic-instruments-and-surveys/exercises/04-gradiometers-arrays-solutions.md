# Solutions — 08-02-04 Gradiometers, Arrays and Noise Rejection

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [04 Gradiometers, Arrays and Noise Rejection](../04-gradiometers-arrays.md).

---

## ★1 — Rejection factors

$$\sigma_{\text{diff}} = \sqrt{2(1-\rho)}\,\sigma.$$

| $\rho$ | $\sqrt{2(1-\rho)}$ | rejection factor |
|---|---|---|
| 0.95 | $\sqrt{0.10} = 0.31623$ | 3.162 |
| 0.99 | $\sqrt{0.02} = 0.14142$ | 7.071 |
| 0.9999 | $\sqrt{2\times10^{-4}} = 1.4142\times10^{-2}$ | 70.71 |

Note the square root: to double the rejection factor, $\rho$ must move four times
closer to 1 in $(1-\rho)$. This is why a gradiometer specification is a statement
about matching, and why "high correlation" is not a useful phrase without a
number.

---

## ★2 — Dipole field and gradient at 8 m

On the axis of a dipole with moment $m$ along $z$:

$$|B| = \frac{\mu_0}{4\pi}\frac{2m}{z^{3}}
= 1.0\times10^{-7}\times\frac{2\times25}{8.0^{3}}
= 1.0\times10^{-7}\times\frac{50}{512}
= 9.7656\times10^{-9}\ \mathrm{T} = 9.7656\ \mathrm{nT}.$$

$$\left|\frac{\partial B}{\partial z}\right| = \frac{3}{z}|B|
= \frac{3\times9.7656}{8.0} = 3.6621\ \mathrm{nT\,m^{-1}}.$$

The ratio is $z/3 = 2.667\ \mathrm{m}$, as §2 of the lesson guarantees.

---

## ★3 — The two tensor properties

- $\nabla\cdot\mathbf{B} = 0$ gives
  $\partial B_x/\partial x + \partial B_y/\partial y + \partial B_z/\partial z
  = G_{xx}+G_{yy}+G_{zz} = \operatorname{tr}G = 0$: the **zero trace**.
- $\nabla\times\mathbf{B} = 0$ (no current density at the sensor) gives
  $\partial B_i/\partial x_j = \partial B_j/\partial x_i$, i.e. the tensor is
  **symmetric**.

A symmetric traceless $3\times3$ matrix has $6-1 = 5$ independent components,
down from nine. That is what makes tensor gradiometry practical: five channels of
information rather than nine, with four relations available as consistency checks.

---

## ★4 — Signal-to-noise and the instrument choice

From ★2: $|B| = 9.7656\ \mathrm{nT}$, $|\text{grad}| = 3.6621\ \mathrm{nT\,m^{-1}}$.

$$\mathrm{S/N}_{B} = \frac{9.7656}{0.05} = 195.3, \qquad
\mathrm{S/N}_{g} = \frac{3.6621}{0.005} = 732.4.$$

Both are far above the $3\sigma$ threshold of 3, so **either instrument detects
the target**; the gradient has 3.75 times the signal-to-noise ratio. The ratio
$732.4/195.3 = 3.75$ equals the ratio of the two floors' scaling:
$(3/z)\times(0.05/0.005) = (3/8)\times10 = 3.75$. ✔

**Generalisation.** The gradient's advantage factor is
$(3/z)\times(\sigma_B/\sigma_g)$. With the floors of the lesson
($\sigma_B = 0.1\ \mathrm{nT}$, $\sigma_g = 0.01\ \mathrm{nT\,m^{-1}}$) the factor
is $30/z$, so the gradient wins while $z < 30\ \mathrm{m}$ — which is exactly the
crossover the lesson's detection table shows between 20 m and 40 m.

---

## ★5 — Wavelength response

$$R(L/\lambda) = 2\sin\!\left(\pi\frac{L}{\lambda}\right),
\qquad \text{fraction} = \frac{R}{2} = \sin\!\left(\pi\frac{L}{\lambda}\right).$$

| $L/\lambda$ | $R$ | fraction |
|---|---|---|
| 0.02 | $2\sin(0.0628319) = 0.125581$ | 6.279% |
| 0.20 | $2\sin(0.628319) = 1.175570$ | 58.779% |

**Half response:** $\sin(\pi L/\lambda) = 0.5$ gives
$\pi L/\lambda = \pi/6$, so $L/\lambda = 1/6 = 0.16667$.

So a gradiometer recovers half the true gradient amplitude for an anomaly whose
wavelength is six baselines long, and only 6.3% for one fifty baselines long. Any
gradient map must therefore be accompanied by the baseline, because the number
quoted is a filtered version of the quantity the reader is imagining.

---

## ★6 — Sensitivity mismatch

A 1% higher sensitivity on sensor A turns a common field $B$ into an apparent
difference

$$\Delta = 0.01\times50000\ \mathrm{nT} = 500\ \mathrm{nT}.$$

That is **500 times** a $1\ \mathrm{nT}$ target anomaly: the mismatch does not
merely add noise, it destroys the measurement. Note how the arithmetic scales: the
leak is proportional to the *common field*, not to the target, so it is worse at
high latitude and worse for larger sensitivity errors.

**Tolerance for a 0.1 nT target.** Require the leak to be below, say, one tenth of
the target, i.e. $0.01\ \mathrm{nT}$:

$$\frac{\delta s}{s} \le \frac{0.01}{50000} = 2.0\times10^{-7}.$$

A relative sensitivity match of **2 parts in $10^{7}$** between the two sensors.
That is not achievable by selecting components; it is achieved by calibrating the
pair *as a difference channel* against a known field, which absorbs the mismatch
into a single scale factor. This is the practical meaning of "a gradiometer is a
single instrument with two heads".

---

## ★7 — A shallow-target gradiometer (specification)

**Baseline.** For a target at $3\ \mathrm{m}$ depth, the anomaly's wavelength is
of order a few times the depth, so take $L \approx 1\ \mathrm{m}$: then
$L/\lambda \approx 0.1$–$0.3$ and the transfer function of ★5 costs only
30–50%. A longer baseline would reject more of the regional field but would also
attenuate the target; a shorter one would improve the transfer function but
approach the sensor-size limit and raise the orientation sensitivity.

**Sensor matching.** From ★6, a 0.1 nT target in a 50000 nT field needs the pair
calibrated as a difference channel; the sensors themselves need only to be
*stable* to about $10^{-4}$ relative, with the residual absorbed by a
difference-channel calibration against a known field gradient (a coil pair or a
measured step in a quiet place).

**Orientation tolerance.** A tilt $\alpha$ of the baseline from the intended
direction converts the main field's horizontal component into an apparent
vertical gradient: the error is of order $H\alpha/L$. For $H = 20000\ \mathrm{nT}$,
$L = 1\ \mathrm{m}$ and a target gradient of a few nT/m, an error below
$0.1\ \mathrm{nT\,m^{-1}}$ requires $\alpha < 5\times10^{-6}\ \mathrm{rad}
= 1$ arcsecond. Achievable only with a rigid, surveyed mount and an attitude
sensor; the design must include both.

**Noise floor.** With matched sensors and $\rho \ge 0.999$, ★1 gives a rejection
of 22.5, so two 0.05 nT sensors give $0.05\times\sqrt{2\times10^{-3}}
= 0.0022\ \mathrm{nT}$ on a $1\ \mathrm{m}$ baseline, i.e.
$0.0022\ \mathrm{nT\,m^{-1}}$ — an order of magnitude below the target's few
nT/m.

**Instrument-level baseline test.** Move the gradiometer over a *known* uniform
gradient (a calibrated coil pair, or a long traverse across a region whose field
is known from a scalar survey) and check that the difference channel reproduces
the known gradient. A baseline error appears as a *scale* error, an orientation
error as a *constant offset* that changes sign when the instrument is reversed —
which is exactly the test that distinguishes them.

---

## ★8 — Depth from a field/gradient ratio

**(a) Point dipole.** From §2 of the lesson,
$|\text{grad}|/|B| = 3/z$, so

$$z = \frac{3\,|B|}{|\text{grad}|}.$$

**Assumption:** the target is a point dipole on the sensor axis, and the
measurement is of the vertical derivative of the total field.

**(b) Horizontal cylinder (2D line source).** For a line of dipoles with moment
per unit length $\lambda_m$, the axial field falls as $r^{-2}$:

$$|B| = \frac{\mu_0}{2\pi}\frac{\lambda_m}{z^{2}}, \qquad
\left|\frac{\partial B}{\partial z}\right|
= \frac{\mu_0}{2\pi}\frac{2\lambda_m}{z^{3}}
= \frac{2}{z}|B|
\;\Longrightarrow\;
z = \frac{2\,|B|}{|\text{grad}|}.$$

**Assumption:** the source is two-dimensional (striking well beyond both ends of
the profile), so that the field falls as $r^{-2}$ rather than $r^{-3}$.

**Error propagation.** Write the ratio estimator as $z = k|B|/|\text{grad}|$ with
$k = 3$ or 2. A fractional error in the ratio measurement propagates directly:
$\delta z/z = \delta(\text{ratio})/(\text{ratio})$, so a 5% error in either
measurement gives a 5% depth error in the ideal case. The *systematic* error is
the more serious one:

- **Wrong model:** using $k = 3$ for a cylindrical target overestimates the depth
  by 50%, and no measurement precision can fix it. This is the dominant
  uncertainty and it is a *model* choice, not a data problem.
- **Off-axis position:** both formulas assume the sensor is directly above the
  source. A horizontal offset $x$ changes the geometry, and the recovered $z$
  becomes an apparent depth that is larger than the true one. The remedy is a
  profile, not a single station: the anomaly's *shape* across a profile is what
  identifies the model, and the ratio is only a first estimate.
- **Interference from other sources:** a regional gradient adds to $|B|$ and
  changes the ratio; this is exactly what a gradiometer's high-pass
  characteristic suppresses, which is why the ratio method is applied to gradient
  data rather than to raw profiles.

**The honest statement of the result:** a field/gradient ratio gives a *model
depth* in one number, and its error is dominated by whether the source is
two-dimensional or three-dimensional — a question the ratio itself cannot answer.
