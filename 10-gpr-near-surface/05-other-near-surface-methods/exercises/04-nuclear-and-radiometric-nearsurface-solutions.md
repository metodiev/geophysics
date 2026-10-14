# Solutions — 10-05-04 Nuclear and Radiometric Near-Surface Methods

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. $k = 1.6449$ (one-sided 95%), $\gamma = 0.5772$.

Lesson: [04 Nuclear and Radiometric Methods](../04-nuclear-and-radiometric-nearsurface.md).

---

## ★1 — A single count rate

$$N = 900 \text{ counts in } t = 60\ \mathrm{s} \;\Longrightarrow\;
r = 15.0\ \mathrm{s^{-1}},$$
$$\sigma_N = \sqrt{900} = 30 \text{ counts}, \qquad
\sigma_r = \frac{30}{60} = 0.50\ \mathrm{s^{-1}},$$
$$\frac{\sigma_r}{r} = \frac{0.50}{15.0} = 3.33\% = \frac{1}{\sqrt{900}} .$$

The uncertainty is *one number*, derived from the measured count alone: no
repeat measurement is needed to know it. That is the practical value of the
Poisson law.

---

## ★2 — Counting time for 1% precision

$$N \ge \frac{1}{\epsilon^{2}} = \frac{1}{0.01^{2}} = 10000 \text{ counts},
\qquad t = \frac{N}{r} = \frac{10000}{12} = 833.3\ \mathrm{s} = 13.9\
\mathrm{min}.$$

The general relation is $\sigma_r/r = 1/\sqrt{rt}$, so $t = 1/(r\epsilon^2)$. Note
the quadratic penalty: 1% precision needs 25 times the time of 5% precision, and
a source ten times weaker needs ten times the time of this one for the same
precision.

---

## ★3 — Units

| Quantity | Unit | Note |
|---|---|---|
| activity | $\mathrm{Bq} = \mathrm{s^{-1}}$ | decays per second |
| count rate | $\mathrm{s^{-1}}$ | detected events per second |
| mass attenuation coefficient $\mu/\rho$ | $\mathrm{m^{2}\,kg^{-1}}$ | often quoted as $\mathrm{cm^{2}\,g^{-1}}$ |
| linear attenuation coefficient $\mu$ | $\mathrm{m^{-1}}$ | $=(\mu/\rho)\rho$ |
| depth $z$ | m | |

$\mu z$ has units $\mathrm{m^{-1}}\cdot\mathrm{m}$, dimensionless ✔. **Check
conversions explicitly**: $1\ \mathrm{cm^{2}\,g^{-1}} = 10\ \mathrm{m^{2}\,kg^{-1}}$,
so $0.055\ \mathrm{cm^{2}\,g^{-1}} = 0.0055\ \mathrm{m^{2}\,kg^{-1}}$, which is the
teaching value used throughout. Treating the two as the same changes every depth
by a factor of ten.

---

## ★★4 — Critical level and detection limit

$$L_C = k\sqrt{2N_B} = 1.6449\sqrt{5000} = 1.6449(70.711) = 116.31 \text{ counts},$$
$$L_D = L_C + k\sqrt{2N_B + L_D}
= 116.31 + 1.6449\sqrt{5000 + 235.32} = 235.32 \text{ counts},$$
$$L_D\ \text{as a rate} = \frac{235.32}{60} = 3.92\ \mathrm{s^{-1}}.$$

**Difference.** $L_C$ answers *"what is the smallest net count that would be
called a detection?"* — a decision rule about a single measurement. $L_D$ answers
*"what true signal is found 95% of the time?"* — a performance figure for the
measurement. They differ by a factor of about two because the variance of the net
signal grows with the signal itself. Reporting one when the other is meant is the
commonest error in detection claims.

---

## ★★5 — 75% depth against the mean depth

$$\mu = (0.0055)(1600) = 8.80\ \mathrm{m^{-1}},$$
$$f(z) = \mu z\,E_1(\mu z) + 1 - e^{-\mu z} = 0.75
\;\Longrightarrow\; z = 7.51\ \mathrm{cm},$$
$$\bar z = \frac{1}{2\mu} = \frac{1}{17.60} = 5.68\ \mathrm{cm}.$$

The 75% depth is **$32\%$ larger** than the mean depth of origin, and the 90% depth
is $14.48\ \mathrm{cm}$ — nearly three times the mean. The two differ because the
layer response $E_1(\mu z)$ is *not* exponential: it diverges logarithmically at
the surface (so the shallowest centimetres dominate the mean) and decays only as
$e^{-\mu z}/(\mu z)$ at depth (so it contributes a long tail to the cumulative).
Quoting a single "depth of investigation" for gamma spectrometry therefore hides
which question is being answered — the same point the thermal and EMI lessons
make about their own depth scales.

---

## ★★6 — Is 160 net counts a detection?

$$N_{\text{net}} = 1760 - 1600 = 160 \text{ counts}, \qquad
\sigma_{\text{net}} = \sqrt{1760 + 1600} = \sqrt{3360} = 57.97 \text{ counts},$$
$$L_C = 1.6449\sqrt{2(1600)} = 1.6449(56.569) = 93.05 \text{ counts}.$$

Since $160 > 93.05$, the excess **is a detection at 95% confidence**. It is
$160/57.97 = 2.76$ standard deviations — a real but not overwhelming detection;
roughly one station in fifty of pure background would give $2.76\sigma$.

**To halve the detectable rate** the detection limit must fall by a factor of two,
which requires $L_D/t$ to halve. Since $L_D/t \propto 1/\sqrt{t}$,
$t$ must increase by **four times** (to $240\ \mathrm{s}$), consistent with the
demonstration's table ($2.37 \to 1.17\ \mathrm{s^{-1}}$ from $60$ to
$240\ \mathrm{s}$).

---

## ★★★7 — A 10% error in a stripping factor (specification)

**Prediction.** Let $A$ be the true sensitivity matrix and $A'$ the matrix with one
factor 10% high. A ground of true activity $\mathbf a_{\text{true}}$ produces
$\mathbf c = A\mathbf a_{\text{true}}$, and the analyst inverts with the wrong
matrix:

$$\mathbf a_{\text{recovered}} = A'^{-1}A\,\mathbf a_{\text{true}}
= (I + A^{-1}\Delta A)\,\mathbf a_{\text{true}},$$

so the error appears in the row of $A^{-1}$ that multiplies the perturbed factor.
For the lesson's matrix, perturbing $A_{KU}$ by 10% (i.e. $0.20 \to 0.22$) gives a
K activity that is too low by roughly

$$|(A^{-1})_{KU}|\,\delta c_U \approx 0.2017 \times (0.02\,a_U)$$

per unit activity of U, i.e. of order $0.4\%$ of the U activity — small for an
equal-activity ground, but **first-order in the U activity**, so a uranium-rich
ground translates the error into a large absolute potassium error. The prediction
to test is therefore not a percentage on the recovered activity but the
*proportionality*: the error in K must scale linearly with the U activity of the
sample.

**Measurement that detects it.** Count a set of samples with *known* activities
(standards) spanning a range of U/K ratios. A wrong stripping factor produces a
straight line of non-zero slope when the recovered K is plotted against the U
activity; a correct matrix produces slope zero. This is a calibration-curve test,
not a field test, and it is the only way to separate a wrong factor from real
geochemistry.

---

## ★★★8 — Designing a natural-gamma soil map (specification)

**Precision target.** State it in activity, not in counts: e.g. "distinguish two
soils whose K-40 activities differ by 25%". A 25% discrimination at 95% confidence
needs the one-sigma relative uncertainty on the difference to be about
$25\%/2.77 \approx 9\%$, and the difference of two measurements of $\epsilon$ each
has $1.41\epsilon$, so $\epsilon \approx 6.4\%$ per station — about $250$ counts
in the K window, or a few tens of seconds per station at typical count rates.

**Station spacing.** Set by the geological target, not by the instrument: if the
soil boundary is metres wide, spacing must be a fraction of that, and the
radiometric footprint ($\sim$ the 90% depth scale laterally, a few metres) sets
the smoothing. State both, and check that the spacing is smaller than the
smoothing or the map is aliased.

**Detection limit claimed.** Report $L_D$ from the *measured background* of the
survey area, per window, converted to activity through the calibration. Reporting
a single number for the whole survey is wrong where the background varies.

**Calibration.** A daily count on a sealed standard source of known activity, plus
the stripping factors measured on the same standards. Both must be recorded in the
archive: an activity map without the calibration is a count map.

**Falsification test.** Repeat a subset of stations at the *end* of the survey and
compare. If the repeat differences are comparable to the mapped pattern, the map
is (partly) instrument drift and time-of-day effects; if they are far smaller, the
pattern is real. A survey whose repeats were never taken cannot support a
geochemical interpretation, whatever its statistical error bars say.
