# Solutions — 17-04-02 GNSS Processing: Networks, PPP and Error Sources

> **Read after attempting the exercises.** Numbers were computed with the
> lesson's constants, not estimated by hand.

Lesson: [02 GNSS Processing](../02-gnss-processing.md).

---

## ★1 — What the differences remove

**Single difference** between two receivers for one satellite:
$$\Delta P = P_A^k - P_B^k
= \left(\rho_A^k-\rho_B^k\right) + c\left(\delta t_A-\delta t_B\right)
+ \left(I_A^k-I_B^k\right) + \left(T_A^k-T_B^k\right) + \varepsilon .$$

- **cancels:** the satellite clock $\delta t^k$, because both receivers observe
  the same satellite.
- **does not cancel:** the receiver clock difference $c(\delta t_A-\delta t_B)$ —
  measured in the lesson's demonstration as a $68\,952\ \mathrm{m}$ common offset.

**Double difference** against a reference satellite:
$$\nabla\Delta P = \Delta P^k - \Delta P^{0}.$$
- **cancels:** the receiver clock difference as well.
- **does not cancel:** the differential *geometry* (which is the signal), the
  differential atmosphere, and the noise. The lesson measures residuals of
  $-0.010$, $+1.181$ and $+1.559\ \mathrm{m}$ against a noise-only expectation of
  $0.600\ \mathrm{m}$ rms.

---

## ★2 — Differential troposphere

At equal zenith angles the two rays traverse the same atmosphere, so the
differential delay is small to first order and cancels almost entirely in the
difference — this is the physical basis for short-baseline relative positioning.
The residual is the part of the atmosphere that differs between the two paths,
which for a $100\ \mathrm{km}$ baseline is millimetres to centimetres depending on
the weather gradient.

With $z_A = 5^\circ$ and $z_B = 70^\circ$ the mapping functions differ enormously
($m \approx 1.004$ against $m \approx 3.4$), so the *same* zenith delay produces
very different slant delays at the two stations:
$$\Delta T = ZTD\left(m(70^\circ) - m(5^\circ)\right)
\approx 2.6 \times (3.4 - 1.0) \approx 6.2\ \mathrm{m}.$$
The difference no longer cancels; it must be modelled with an elevation-dependent
mapping and, in practice, by estimating a residual zenith delay per station. This
is why mixing very low and very high elevations within one difference is avoided
where possible, and why low-elevation data are down-weighted.

---

## ★3 — Mapping functions at $40^\circ$

$$\frac{1}{\cos 40^\circ} = \frac{1}{0.766044} = 1.305407.$$
$$m_{\text{curved}} = \left[1-\left(\frac{6371}{6379}\right)^{2}\sin^{2}40^\circ
\right]^{-1/2}
= \left[1-\left(0.998746\right)^{2}\times0.413176\right]^{-1/2}.$$
$$(0.998746)^{2} = 0.997494, \quad
0.997494\times0.413176 = 0.412140, \quad
1-0.412140 = 0.587860,$$
$$m_{\text{curved}} = \frac{1}{\sqrt{0.587860}} = 1.304561.$$

Difference: $1.305407 - 1.304561 = 0.000846$, i.e. **$+0.065\%$** of the mapping
factor. At $40^\circ$ the two forms are almost indistinguishable; the divergence
appears only below about $20^\circ$ of elevation, reaching $15.2\%$ at $z =
85^\circ$ (lesson table).

---

## ★4 — Height error at $65^\circ$

**(a)** The curved mapping at $z = 65^\circ$:
$$m = \left[1-0.997494\sin^{2}65^\circ\right]^{-1/2}
= \left[1-0.997494\times0.821394\right]^{-1/2}
= \left[1-0.819336\right]^{-1/2} = \frac{1}{\sqrt{0.180664}} = 2.352713.$$
$$\text{height error} = 1.5\ \mathrm{cm}\times2.3527 = 3.53\ \mathrm{cm}.$$

**(b)** Geometry term: $\text{VDOP}\times\sigma_{\text{phase}} = 2.0\times4\
\mathrm{mm} = 8\ \mathrm{mm} = 0.8\ \mathrm{cm}$.

**The wet-delay term dominates**, $3.53\ \mathrm{cm}$ against $0.8\ \mathrm{cm}$ —
a factor of 4.4. Even though VDOP is only moderate, the zenith wet delay is a
poorly known quantity amplified by the mapping function, and it is the term to
attack (better troposphere model, independent water-vapour data, longer session).

---

## ★5 — Ambiguity fixing at $\sigma = 0.30$ cycles

**(a)** From the table: $\sigma = 0.20$ gives 0.0115 and $\sigma = 0.40$ gives
0.2167. Interpolating roughly linearly in $\sigma$ (or, better, from the normal
probability of $|e| > 0.5$):
$$P\left(|e|>0.5\right) = 2\Phi\!\left(-\frac{0.5}{0.30}\right)
= 2\Phi(-1.667) \approx 2\times0.0478 = 0.0956 \approx 9.6\%.$$

(The interpolation between the table entries, 0.0115 and 0.2167, gives about
$0.11$ — the normal-probability value is the honest one, and the two agree in
magnitude.)

**(b)** If every wrong fix were excluded, the rms error would be that of a
*fractional* estimate, i.e. the float error, about
$0.30\ \lambda/2$ scale, so a few centimetres rather than tens. That number is
**not achievable** because you cannot exclude wrong fixes without a validation
test, and the test has its own false-accept rate. A fix that fails validation is
discarded (returning the float solution), which means the practical output is a
*mixture*: float where validation failed, fixed where it passed. Its rms lies
between the two rows of the table, and the mixture fraction must be reported.

---

## ★6 — Bias from an omitted annual term

**(a)** Scaling from the lesson: the $1.2$-year record gave $-2.343\
\mathrm{mm\,yr^{-1}}$ and the $3.0$-year record $-0.814\ \mathrm{mm\,yr^{-1}}$
for an annual amplitude of $4\ \mathrm{mm}$. The bias is roughly inversely
proportional to the record length (the sinusoid becomes more nearly orthogonal to
the linear term as more cycles are covered), so for a $2.5$-year record expect
about
$$-0.814\times\frac{3.0}{2.5} = -0.98\ \mathrm{mm\,yr^{-1}},$$
and scaling the amplitude from 4 to $5\ \mathrm{mm}$ multiplies it:
$$\approx -0.98\times\frac{5}{4} = -1.22\ \mathrm{mm\,yr^{-1}}.$$

Note that this bias is comparable to the $1\ \mathrm{mm\,yr^{-1}}$ signal of a
★★★-type study — larger, in fact. The seasonal term must therefore be fitted, not
assumed away.

**(b)** The two record properties that change the bias:

1. **The number of seasonal cycles covered.** A record spanning 3.0 cycles has a
   nearly orthogonal sinusoid and a small projection onto the linear trend; a
   record spanning 1.2 cycles has a large one, and the bias is of order $1/N_{\text{cyc}}$.
2. **The phase of the season at the record ends.** A record starting at a
   seasonal maximum and ending at a minimum has a large projection; one starting
   and ending near the same phase has a much smaller one. This can change the bias
   by a factor of two or more, and even its sign, without altering anything else.

---

## ★7 — A 1 mm/yr uplift network (specification)

**Observation strategy.** Continuous or near-continuous daily solutions at all ten
stations for the full five years, dual frequency for the ionosphere, with a
session length long enough that the geometry changes (a full day is standard). The
target is $1\ \mathrm{mm\,yr^{-1}}$ over 5 years, i.e. $5\ \mathrm{mm}$ of total
signal — so the *rate*, not the position, is the deliverable, and the noise model
and the seasonal model dominate the error budget.

**Difference or PPP.** Use both. Double differences over the short baselines give
the best relative accuracy between neighbouring stations (the atmosphere largely
cancels); PPP with precise products gives an independent absolute check and is
insensitive to network geometry. Comparing the two is itself the strongest
validation, because their error structures differ.

**Noise model.** Assume a combination of white, flicker and random-walk noise and
*estimate* the components from the data (e.g. by fitting the power spectrum or the
Allan variance of the residuals). Do not assume white: the lesson measures a
factor of **7.3** in the velocity scatter between white and flicker noise of equal
variance, so a white-noise error bar would be optimistic by an order of magnitude
in the variance.

**Seasonal and discontinuity terms.** Fit a linear rate, an annual sine and
cosine, a semiannual term if the record supports it, and offsets at every known
equipment change, earthquake or monument repair. Omitting the annual term alone
cost the lesson $0.81\ \mathrm{mm\,yr^{-1}}$ over 3 years and
$2.34\ \mathrm{mm\,yr^{-1}}$ over 1.2 years — larger than the signal.

**External comparison.** Compare against an independent technique with a different
error budget: absolute gravity if the uplift has a mass component, InSAR where
coherence allows, or the tide-gauge and satellite-altimetry record if the question
is sea level. The comparison tests the *rate*, which is the quantity of interest,
and it is the only way to detect a common-mode error shared by the whole network.

---

## ★8 — Why equal variance is not equal information

**(a)** A trend estimate weights the data by their *low-frequency* content. White
noise has a flat spectrum, so a longer record adds new independent information at
all frequencies and the trend variance falls roughly as $1/(N\,T^{2})$. Flicker
noise has power concentrated at the lowest frequencies — precisely where the trend
lives — so successive samples are correlated and the effective number of
independent observations saturates at $T/\tau$ where $\tau$ is the correlation
time, not at $N$. Equal *variance* therefore corresponds to unequal *information*:
the correlated series has much less independent low-frequency content, and the
trend is far less well determined.

**(b)** With ten times the record length, the white-noise case improves by about a
factor $\sqrt{10}$ in the velocity scatter. The flicker case improves much less:
the flicker trend uncertainty falls roughly as $T^{-1}$ (or slower) rather than
$T^{-3/2}$, because the new data continue to be correlated with the old. So the
*ratio* between the two increases with record length: the gap widens, and long
records are where choosing the right noise model matters most.

**(c) Diagnostic.** Compute the power spectral density of the residual positions
after removing the deterministic model, and fit a power law in log-log space: a
slope near 0 indicates white noise, near $-1$ flicker, near $-2$ random walk. Two
complementary checks: (i) the Allan variance (or the scatter of rates estimated
from nested sub-intervals), whose slope distinguishes the regimes; (ii) empirical
repeatability, by splitting the record into independent halves and comparing the
two velocities against the formal errors. The empirical check is the decisive one,
because it uses the data's own correlation structure rather than a parametric
assumption.
