# Solutions — 06-07-04 Autocorrelation and Body-Wave Microseismics

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [04 Autocorrelation and Body-Wave Microseismics](../04-autocorrelation.md).

---

## ★1 — Reflection and transmission coefficients

$$R = \frac{Z_2 - Z_1}{Z_2 + Z_1}
= \frac{1.90 - 1.50}{1.90 + 1.50}\times10^{7}\ \text{over}\ 10^{7}
= \frac{0.40}{3.40} = +0.11765,$$
$$T = 1 + R = +1.11765 .$$

Both are **dimensionless**: the impedance units cancel. The sign is positive
because the impedance increases downward (a "hard" reflection), and the value
$|R| = 0.118$ means about $(0.118)^{2} = 1.4\%$ of the incident energy is
reflected — the rest is transmitted.

---

## ★2 — Two-way time

$$t = \frac{2h}{v_p} = \frac{2\times3.0}{6.00} = 1.0000\ \mathrm{s}.$$

Note the structure of the formula: the factor $2$ is the down-and-up path, and
the result is in seconds because kilometres divided by kilometres per second is
seconds.

---

## ★3 — Time to depth

$$h = \frac{v_p\,t}{2} = \frac{5.80 \times 1.7241}{2} = 5.000\ \mathrm{km},$$

which is the model's layer thickness. The exercise is a reminder of the
non-uniqueness: the same $1.7241\ \mathrm{s}$ would correspond to
$h = 5.0\ \mathrm{km}$ at $5.80\ \mathrm{km\,s^{-1}}$ but to
$h = 4.61\ \mathrm{km}$ at $5.35\ \mathrm{km\,s^{-1}}$, a $8\%$ difference for a
$8\%$ velocity error. **The time is the measurement; the depth is an
interpretation.**

---

## ★4 — Calibration ratio

$$\frac{A_{\text{peak}}/A(0)}{R} = \frac{0.077497}{0.069279} = 1.1186,$$

i.e. the measured peak amplitude is $11.9\%$ larger than $R$ times the zero-lag
value. The excess is the **tail of the zero-lag term**: the autocorrelation of
the band-limited source is not a delta function, and at the reflector's lag
($1.7241\ \mathrm{s}$) it still has a small but non-zero value that adds to the
desired peak. The proportionality $A_{\text{peak}} = R_iR_{ww}(0)$ holds for the
*peak of the wavelet*; what is measured is that peak plus the tail of the
zero-lag lobe. The excess diminishes as the first reflector is placed deeper or
as the bandwidth is reduced.

---

## ★5 — Tuning ratio

$$\frac{A(0.15)}{A(0.05)} = \frac{1.533}{0.769} = 1.994 .$$

The two separations give responses that differ by a factor of two, in the
direction opposite to naive intuition: the *larger* separation gives the larger
amplitude. The reason is the polarity. For two reflectors of opposite sign, the
two wavelet lobes add most constructively when their separation is close to half
the dominant period of the wavelet (here the passband is $1$-$5\ \mathrm{Hz}$, so
the dominant period is around $0.2$-$1\ \mathrm{s}$); at $\Delta = 0.05\
\mathrm{s}$, well below the HWHM of $0.100\ \mathrm{s}$, the two lobes largely
cancel and the response *shrinks* to $0.77$ of a single reflector. Both values
are far from the $2.0$ that a resolvable pair of a "sum" would give, which is
the point of the exercise: **below the wavelet width, amplitude is not a proxy
for reflection strength.**

---

## ★6 — Convergence exponent

$$\text{ratio} = \frac{7.456\times10^{-3}}{1.135\times10^{-3}} = 6.57,$$
$$\text{exponent} = \frac{\log_{10}6.57}{\log_{10}64}
= \frac{0.8176}{1.8062} = 0.453 .$$

The implied exponent is $0.453$, matching the fitted $-0.454$ (the fit uses all
seven points; the endpoint ratio gives the same answer to three decimals). The
theoretical value is $0.500$. The $9\%$ shortfall is the correlation between
windows: the same source wavelet is used for all of them, so the errors are not
independent.

---

## ★7 — A borehole sensor (specification)

**What changes.** At $1\ \mathrm{km}$ depth the sensor does not see the free
surface arrival in the same way: the strong surface reflection that provides the
zero-lag reference in a surface deployment arrives at the sensor as a
*separate* arrival at a non-zero lag (the two-way travel time from the surface to
the receiver), and it arrives with the polarity reversal of a free-surface
reflection. The record therefore no longer contains a unit arrival at $t=0$.

**What the autocorrelation then measures.** Differences of arrival times only:
the reflector times appear relative to the surface-reflection time, so the
retrieved reflectivity is *shifted* by the direct-arrival delay. With a known
receiver depth and velocity, the shift is computable and can be removed; with an
unknown one it is a systematic bias on every depth.

**Test for adequacy.** Compare the autocorrelation of the borehole record with a
synthetic one computed for the same depth and medium *including* the free
surface. If the measured autocorrelation is missing the peaks that the synthetic
record predicts at the reflector lags, the reference arrival is inadequate —
i.e. the noise field does not contain the down-going and up-going symmetric pair
the method assumes. A second, independent test is the reciprocity of the
retrieval: the autocorrelation of the *up-going* field at the borehole and of
the *down-going* field at the surface should be time-reversed copies if the
zero-lag reference exists.

---

## ★8 — Reducing the multiple contamination (specification)

**Processing step.** Predict the wanted peaks and the difference peaks
separately, then subtract the predicted difference peaks before measuring
amplitudes. In practice this is a **multiples model** built from the reflection
coefficients themselves: with the amplitudes of the wanted peaks measured
iteratively, the difference peaks $(i,j)$ have known lags
$t_j - t_i$ and amplitudes $R_iR_j$, so a linear least-squares fit of the
autocorrelation in terms of products $R_iR_j$ recovers the coefficients
self-consistently.

**Predicted effect.** The second and third difference peaks fall within one
wavelet of the primaries, so their coherent contribution is what biases the
measurement. Removing them leaves a residual error of second order
($\sim R^{2}\approx10^{-2}$ rather than $\sim R\approx 10^{-1}$). The measured
$-13.9\%$ and $-26.2\%$ should therefore shrink towards zero; a *specific*
prediction is that $A_3/A_1$ increases towards the model value $1.4436$, because
the difference peak at $1.690\ \mathrm{s}$ is the one closest to the primary at
$t_1 = 1.7241\ \mathrm{s}$ and its removal *reduces* the interface-1 amplitude
that $A_3$ is normalised by.

**Cost.** The multiples model requires the reflection coefficients it is trying
to measure (circularity), so it must be solved iteratively; convergence is not
guaranteed for strong reflectors, and the iterative scheme can absorb real
signal into a multiple if the wavelet estimate is biased. The cost is therefore
paid in *assumptions*: a fixed wavelet, a 1-D medium, and a weak-reflectivity
starting model.
