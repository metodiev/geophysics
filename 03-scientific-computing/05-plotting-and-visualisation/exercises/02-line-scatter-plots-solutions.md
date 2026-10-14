# Solutions — 03-05-02 Line, Scatter and Error-Bar Plots with Correct Uncertainty

> **Read this after attempting the exercises, not before.** Values attributed to
> the demonstration are its actual output.

---

## ★1 — What ± means

**(a)** The three common meanings, with their coverages:

| Written as | Meaning | Coverage |
|---|---|---|
| $5.00 \pm 0.30$ | one standard deviation of the measurement | 68.3 % |
| $5.00 \pm 0.30$ | standard error of the mean of $n$ measurements | 68.3 % for the mean |
| $5.00 \pm 0.30$ | half-width of a 95 % interval | 95.4 % |

**(b)** If the interval is one standard deviation, $\sigma = 0.30$. If it is a
standard error of the mean, $\sigma_{\text{mean}} = 0.30$ and the individual
measurement scatter is $\sigma = 0.30\sqrt{n}$. If it is a 95 % interval,
$\sigma = 0.30/1.96 = 0.153$.

**(c)** The three interpretations differ by a factor of up to $1.96\sqrt{n}$, so
without the coverage the number cannot be compared with anything — not with another
measurement, not with a model prediction, and not with the same quantity measured
by another group.

---

## ★2 — Reduced chi-square

**(a)** $\nu = n - p = 12 - 2 = 10$.

**(b)** $\chi^2/\nu = 4.2/10 = 0.42$. The residuals are far smaller than the stated
uncertainties, which means either the uncertainties are overstated (by about a
factor $\sqrt{1/0.42} = 1.54$ in $\sigma$) or the errors are correlated in a way
that reduces the effective scatter.

**(c)** $\chi^2/\nu = 240/10 = 24$. Two causes: the quoted uncertainties are too
small (by a factor $\sqrt{24} = 4.9$), or the model is wrong — a straight line
fitted to curved data leaves systematic residuals that no error bar can absorb.
The two are distinguished by plotting the residuals against $x$: random-looking
residuals of the wrong size point to (i), structured residuals point to (ii).

---

## ★3 — Weights

**(a)** $\sigma(10)/\sigma(0) = 1.0812/0.1868 = 5.788$.

**(b)** $w = 1/\sigma^2$, so
$w(0)/w(10) = (1.0812/0.1868)^2 = 33.50$.

**(c)** The point at $x = 0$ is preferred by a factor of 33.5 in the least-squares
sum. Equivalently, moving the fitted line by one standard deviation at $x=0$ costs
33.5 times as much $\chi^2$ as the same normalised displacement at $x = 10$.

---

## ★4 — Marks and legibility

**(a)** The continuous series takes a **line** because the ordering of the samples
is information and the model asserts continuity between them. The sample with
error bars takes **markers with bars** because the samples are independent: a
segment drawn between two of them would assert values that were never measured.

**(b)** Three changes that keep all the data: (i) encode the series with a second
channel — line style and marker shape — instead of colour alone; (ii) plot the
difference between each series and a common reference, so the panels separate; and
(iii) split into a small multiple of aligned panels sharing an axis. Removing data
is not on the list, because the overlap usually *is* the result.

---

## ★5 — Running the demonstration

**(a)** From the script:

```text
  intercept a = 3.0019 +/- 0.0781  (true 3.0)
  slope     b = 1.4808 +/- 0.0239  (true 1.5)
  chi^2 = 54.482 for 58 degrees of freedom  ->  chi^2/dof = 0.939
```

**(b)** Measured against expected:

```text
    within 1 sigma: 41/60 =  0.683   (expected 0.683 for Gaussian noise)
    within 2 sigma: 59/60 =  0.983   (expected 0.954 for Gaussian noise)
    within 3 sigma: 59/60 =  0.983   (expected 0.997 for Gaussian noise)
```

**(c)** Under the Gaussian model the count inside $1\sigma$ is binomial with
$p = 0.683$ and $n = 60$, so
$\sigma_p = \sqrt{p(1-p)/n} = \sqrt{0.683 \times 0.317/60} = 0.0601$. The measured
$41/60 = 0.6833$ differs from 0.683 by 0.0003, i.e. by $0.005\sigma_p$: exactly
consistent. The
$2\sigma$ count of 0.983 exceeds 0.954 by 0.029, or $0.49\sigma_p$ — also
consistent. Neither count rejects the error model.

**(d)** $\chi^2/\nu = 0.939$ is within about $1/\sqrt{2\nu} = 0.093$ of unity, so the
scatter is consistent with the stated $\sigma_i$. The bars are correctly calibrated
for the noise that generated the data, which is the strongest statement available
here.

---

## ★6 — Weighted versus unweighted

**(a)** With the script's seed and generating model, unweighted least squares gives
$y = 2.8313 + 1.5217x$, against the weighted $y = 3.0019 + 1.4808x$. The slopes
differ by 0.041, which is 1.7 times the weighted fit's standard error of 0.0239.

**(b)** The weighted fit is correct. The generating model gives each point an
independent Gaussian error with $\sigma_i^2 = (0.06(3 + 1.5x_i))^2 + 0.05^2$, and
maximum-likelihood estimation for that model is the weighted normal equations. The
unweighted fit ignores the model: it lets the high-$x$ points, whose $\sigma$ is
33.5 times larger in weight terms, drive the slope. Its steeper value is the
expected consequence of that, not evidence about the data.

**(c)** Unweighted least squares is the more efficient estimator — it is the
maximum-likelihood estimator — when all $\sigma_i$ are equal, i.e. the data are
homoscedastic. In that case the weights are a constant and drop out of the normal
equations.

---

## ★7 — Power-law fitting

**(a)** For $y = Ax^{-p}$, $\ln y = \ln A - p\ln x$. Propagating a relative
uncertainty: $\sigma_{\ln y} = \sigma_y/y$, and converting to base 10,
$\sigma_{\log_{10} y} = \sigma_y/(y\ln 10)$. With $\sigma_y/y = 0.10$,
$\sigma_{\log_{10} y} = 0.10/2.3026 = 0.0434$. The weights are
$w_i = 1/\sigma_{\log_{10}y_i}^2 = (y_i \ln 10/\sigma_{y_i})^2$, which for a
constant relative error are all equal: with multiplicative noise, log-space fitting
is automatically homoscedastic.

**(b)** $1.4073 \pm 1.96 \times 0.0077 = 1.4073 \pm 0.0151$, i.e. the interval
$[1.3922, 1.4224]$. The true value 1.4 lies inside it.

**(c)** The straightness of the log-log plot establishes that the data are
*consistent with* a power law over the fitted range. It does not establish that the
relationship is a power law outside that range, and it does not establish
causation: many different physical models produce a power law with a similar
exponent over two decades.

---

## ★8 — Two-dimensional uncertainty

**(a)** $1.5/0.4 = 3.75$.

**(b)** A bar's length on the page is the uncertainty divided by the number of data
units per inch on that axis. Each axis has its own scale, chosen by the author, so
the ratio of the drawn lengths is the ratio of the numbers times the ratio of the
two axis scales. Compressing the distance axis by a factor of ten makes the
horizontal bar ten times shorter while the number is unchanged.

**(c)** The caption sentence must state the magnitude explicitly: "horizontal
uncertainty $\pm 1.5$ km is smaller than the marker and is not drawn". A reader
who cannot see a bar will otherwise assume it is zero, which is a stronger claim
than any measurement supports.

---

## ★9 — Confidence bands

**(a)** For a straight-line model with parameter covariance $\mathrm{Cov}$ and
design row $A_x = (1,\ x)$,

$$\sigma^2_{\hat y(x)} = A_x\,\mathrm{Cov}\,A_x^{\mathsf T}
 = \sigma^2_a + 2x\,\mathrm{Cov}(a,b) + x^2\sigma^2_b .$$

**(b)** The fitted line pivots about the centroid $(\bar x, \bar y)$: a change in
slope can be compensated by a change in intercept with no effect on the value at
$\bar x$. So the uncertainty of $\hat y$ is stationary — actually minimal — at
$\bar x$, and grows quadratically away from it. This is a property of the design
matrix, not of the physics.

**(c)** No: a band narrower than the bars does not mean the fit is better than the
data. The band is the uncertainty of the *mean line*, which averages over $n$
points and is therefore smaller than the scatter of a single point; the bars show
the scatter of single points. Comparing them is comparing two different quantities.
The statistic that tests the model is $\chi^2/\nu$, together with the structure of
the residuals — a band that stays narrow beyond the last datum is over-claiming,
because the formula assumed the model holds there.

---

## ★10 — Errors in both variables

**(a)** Weighted least squares in $y$ attributes all the misfit to the dependent
variable. If $x$ also carries error, part of each residual is due to $x$, and the
estimator systematically attenuates the slope: the noise in $x$ is treated as noise
in $y$, which pulls an estimated slope toward zero. The effect grows with the ratio
of the $x$ variance to the spread of the $x$ values.

**(b)** Total least squares minimises the sum of squared *orthogonal* distances
from the data points to the fitted line, which is the maximum-likelihood estimator
when the two variables' errors have comparable variance (and equals the first
principal component of the centred data). Weighted least squares minimises the sum
of squared *vertical* distances, weighted by $1/\sigma_y^2$. The two agree only
when the $x$ errors vanish.

**(c)** Defensible: fitting gravity anomaly against *depth* where depth comes from a
drilled well collar, so the depth error is metres against a kilometre-scale axis —
negligible. Not defensible: fitting anomaly against a *distance to a geological
contact* digitised from a map, where both variables come from the same
interpretation and their errors are of comparable size and correlated.
