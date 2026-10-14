# Solutions — 21-01-06 Spatial and Directional Statistics in Earth Science

> Read after attempting. Lesson:
> [06 Spatial Statistics](../06-spatial-statistics-geo.md). Numbers quoted from
> the demonstration reproduce its output.

---

## ★1 — Null expectation of Moran's I

$$\mathbb E[I] = -\frac{1}{N-1} = -\frac{1}{899} = -0.001112 .$$

The measured white-noise value is $-0.0346$, which is $31$ times the magnitude of
the expectation. With $\operatorname{sd}(I) \approx 1/\sqrt{N}$ for a large
lattice, $\operatorname{sd}(I) \approx 1/\sqrt{900} = 0.0333$, so the value sits
$(-0.0346 + 0.0011)/0.0333 = -1.0$ standard deviations from the null — entirely
consistent with no spatial autocorrelation. The comparison with **zero** (which
would suggest a modest negative $I$) is the mistake the expectation exists to
prevent.

---

## ★2 — Semivariance of a short line

Values $\{4, 6, 7, 9\}$, mean $=\ 6.5$.

Centre and square: deviations $-2.5, -0.5, +0.5, +2.5$, squares $6.25, 0.25,
0.25, 6.25$; $\sum z_i^{2} = 13.0$.

**Lag 1** has $N(1) = 3$ pairs: $(4,6), (6,7), (7,9)$.

$$\hat\gamma(1) = \frac{(6-4)^{2} + (7-6)^{2} + (9-7)^{2}}{2\times3}
= \frac{4 + 1 + 4}{6} = 1.5\ \%.$$

**Lag 2** has $N(2) = 2$ pairs: $(4,7), (6,9)$.

$$\hat\gamma(2) = \frac{(7-4)^{2} + (9-6)^{2}}{2\times2}
= \frac{9 + 9}{4} = 4.5\ \%.$$

The semivariance is in squared per-cent units, like the variance. It has risen
from $1.5$ to $4.5$, three times as large at double the lag — the direction of
growth the variogram model formalises.

---

## ★3 — Circular mean and resultant length

Represent each bearing as $(\cos\theta, \sin\theta)$ in degrees.

**Two bearings $350^{\circ}, 10^{\circ}$:**

$$\bar C = \frac{\cos 350 + \cos 10}{2} = \frac{0.9848 + 0.9848}{2} = 0.9848,$$
$$\bar S = \frac{\sin 350 + \sin 10}{2} = \frac{-0.1736 + 0.1736}{2} = 0.0000 .$$

$$\bar\theta = \operatorname{atan2}(0, 0.9848) = 0^{\circ}, \qquad
R = \sqrt{0.9848^{2} + 0^{2}} = 0.9848 .$$

The circular mean is $0^{\circ}$ — the correct answer, midway between $350^{\circ}$
and $10^{\circ}$ across the branch cut. The arithmetic mean would have given
$180^{\circ}$.

**Add $30^{\circ}$:**

$$\bar C = \frac{0.9848 + 0.9848 + 0.8660}{3} = 0.9452, \qquad
\bar S = \frac{-0.1736 + 0.1736 + 0.5}{3} = 0.1667,$$

$$\bar\theta = \operatorname{atan2}(0.1667, 0.9452) = 10.0^{\circ}, \qquad
R = \sqrt{0.9452^{2} + 0.1667^{2}} = 0.9598 .$$

The mean direction moves $0^{\circ} \to 10^{\circ}$ and $R$ rises slightly
because the third bearing is close to the first two's centre.

---

## ★★4 — Relating semivariance to covariance

For a second-order stationary field, $\mathbb E[Z(x)] = \mu$ and
$C(h) = \operatorname{Cov}(Z(x), Z(x+h))$. Then

$$\mathbb E\big[(Z(x+h) - Z(x))^{2}\big]
= \operatorname{Var}\big(Z(x+h) - Z(x)\big)
= C(0) + C(0) - 2C(h) = 2\big(C(0) - C(h)\big),$$

using $\operatorname{Var}(A - B) = \operatorname{Var}A + \operatorname{Var}B -
2\operatorname{Cov}(A,B)$ and $C(-h) = C(h)$. Halving gives the claimed

$$\gamma(h) = C(0) - C(h).$$

If only the **increments** are stationary (the intrinsic hypothesis), $C(0)$ need
not exist — the variance of $Z$ itself can be infinite, as it is for a random
walk or a fractal field — but the left-hand side, the variance of an increment,
remains finite and well defined. The semivariogram is then
estimable even though the covariance is not, which is why it is the primary tool
in geostatistics.

---

## ★★5 — Rayleigh test arithmetic

$$Z = nR^{2}, \qquad p = e^{-Z}.$$

**Uniform sample**, $R = 0.1037$, $n = 60$:

$$Z = 60 \times 0.1037^{2} = 60 \times 0.010754 = 0.645, \qquad
p = e^{-0.645} = 0.525 .$$

Matches the printed $Z = 0.645$, $p = 5.25\times10^{-1}$.

**Concentrated sample**, $R = 0.7682$, $n = 60$:

$$Z = 60 \times 0.59013 = 35.408, \qquad p = e^{-35.408} = 4.2\times10^{-16}.$$

Matches the printed $35.404$ and $4.21\times10^{-16}$ (the last digit is rounding
of $R$).

**Threshold.** For $p = 0.05$, $Z = -\ln 0.05 = 2.996$, so

$$R_{\text{crit}} = \sqrt{\frac{2.996}{60}} = \sqrt{0.04993} = 0.2235 .$$

Any $R$ above $0.2235$ at $n = 60$ rejects the uniform null at $5\ \%$ — the
uneven sample's $R = 0.104$ is comfortably below it.

---

## ★★6 — Effective sample size

**From the range.** A semivariogram range of about five cells means values
roughly five cells apart are uncorrelated. The area over which values are
correlated is of order the range squared, $5^{2} = 25$ cells, so an upper bound
on the effective count is

$$N_{\text{eff}} \approx \frac{A}{(\text{range})^{2}} = \frac{900}{25} = 36 .$$

**From the Gaussian-covariance formula.** With $C(r) = \sigma^{2}e^{-r^{2}/(2\ell^{2})}$
and $\ell = 2$ cells,

$$\operatorname{Var}(\bar z) \approx \frac{\sigma^{2}}{A}\int_{\mathbb R^{2}}
C(r)\,\mathrm d^{2}r \cdot \frac{1}{\sigma^{2}}
= \frac{2\pi\ell^{2}}{A}\sigma^{2}
\;\Longrightarrow\;
N_{\text{eff}} = \frac{A}{2\pi\ell^{2}} = \frac{900}{2\pi\times4} = 35.8 .$$

Both estimates agree at about $36$, i.e. **$4\ \%$** of the $900$ cell values are
effectively independent. The standard error of the field mean is therefore
$\sigma/\sqrt{N_{\text{eff}}} = \sigma/5.99$ rather than $\sigma/30$ — **five
times** larger than the naive independent-sample value. Reporting the naive one
understates the uncertainty of a map mean by a factor of five.

---

## ★★★7 — Anisotropy test

**Field construction.** Generate a Gaussian random field by smoothing white noise
anisotropically: convolve with a Gaussian kernel of length $\ell_x = 3$ cells in
the $x$-direction and $\ell_y = 6$ cells in the $y$-direction on a
$128\times128$ grid with periodic boundaries, so the true range is $3$ cells
along $x$ and $6$ along $y$.

**Directional bins.** Estimate the semivariance in four directional bins:
azimuth $0^{\circ}-45^{\circ}$, $45^{\circ}-90^{\circ}$, $90^{\circ}-135^{\circ}$
and $135^{\circ}-180^{\circ}$, each with a lag tolerance of $\pm1$ cell.

**Statistic.** Fit a spherical model in each bin and read off the range
$\hat r_k$; the statistic is $\max_k \hat r_k / \min_k \hat r_k$.

**Replicates.** The range estimated from a $128\times128$ field by nonlinear
least squares has a relative standard error of roughly $5\ \%$–$10\ \%$. To
distinguish ranges of $3$ and $6$ cells — an absolute gap of $3$ cells, or about
$30\ \%$ of the larger — at $3\sigma$ needs a per-bin relative error below
$10\ \%$; with the usual $2$–$3\ \%$ per bin, that holds for the four bins of a
single field, and $M = 30$ realisations give the distribution of the ratio under
the null of isotropy. The prediction is a ratio near $1.0$ under isotropy and
near $2.0$ here; the test rejects when the observed ratio exceeds the
$95$th percentile of the simulated null distribution.

---

## ★★★8 — Standard error against sampling spacing

**Design.** Build a $256\times256$ Gaussian-covariance field with $\ell = 2$
cells. Sample it on grids with spacing $s \in \{1, 2, 3, 4, 6, 8, 12, 16\}$
cells, keeping the field fixed; compute the sample mean of each subsample.
Repeat over $M = 1000$ independent fields, recording the standard deviation of
the mean across fields for each spacing.

**Metric.** $\mathrm{sd}(\bar z)(s)$, and its ratio to the formula
$\sigma\sqrt{2\pi\ell^{2}/A_s}$ where $A_s$ is the sampled area.

**Predicted scaling.** As long as the sampled area is fixed and $s \ll \ell$, the
standard error is set by the **area** and the correlation length, not by the
number of samples: it is flat in $s$. Only when the spacing approaches $2\ell$
does the sample approach independence and the curve begin to fall as
$1/\sqrt{n}$. The study's headline is the spacing at which the curve departs from
flat, which is the survey design rule: sampling closer than the correlation
length buys almost no information.
