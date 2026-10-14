# Exercises — 03-05-02 Line, Scatter and Error-Bar Plots with Correct Uncertainty

Attempt these **closed-book** before opening the
[solutions](./02-line-scatter-plots-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/02_line_scatter_plots_demo.py`](../code/02_line_scatter_plots_demo.py)
require you to run it and report its **actual** output.

All uncertainties in these problems are **nominal** unless a problem states that a
measurement is given. Where a problem asks for a coverage, state the coverage you
are using.

---

## ★ Foundational

**★1.** A measurement is reported as $y = 5.00 \pm 0.30$ with no coverage stated.

(a) Write the three most likely meanings of $\pm 0.30$ and the coverage each
implies.
(b) For each, compute $\sigma$ if the underlying standard deviation is the
quantity of interest.
(c) State in one sentence why the figure caption must carry the coverage.

---

**★2.** A straight-line model is fitted to $n = 12$ points by weighted least
squares with $p = 2$ parameters.

(a) State the number of degrees of freedom.
(b) The fit returns $\chi^2 = 4.2$. Compute $\chi^2/\nu$ and interpret it.
(c) The fit returns $\chi^2 = 240$. Compute $\chi^2/\nu$ and interpret it,
naming two possible causes.

---

**★3.** The demonstration reports that the noise standard deviation grows from
0.1868 at $x = 0$ to 1.0812 at $x = 10$.

(a) Compute the ratio of the two standard deviations.
(b) Compute the ratio of the corresponding weights $w_i = 1/\sigma_i^2$.
(c) State which of the two points the weighted fit prefers and by how much.

---

**★4.** Two samples are plotted on the same axes, one as a continuous curve and one
as scattered points with error bars.

(a) State which mark is appropriate for each and why.
(b) A third sample is added and the plot becomes unreadable because the three
series overlap. Name three changes that improve legibility without removing data.

---

## ★★ Applied

**★★5.** Run [`../code/02_line_scatter_plots_demo.py`](../code/02_line_scatter_plots_demo.py).

(a) Report the fitted intercept, its standard error, the fitted slope, its standard
error and $\chi^2/\nu$.
(b) Report the measured coverage at 1, 2 and 3 $\sigma$, and the expected values
the script prints beside them.
(c) With $n = 60$, compute the standard error of the *fraction* covered at
$1\sigma$ assuming the Gaussian value 0.683, and state whether the measured value
is consistent with it.
(d) State whether the $\chi^2/\nu$ value is consistent with correctly calibrated
error bars.

---

**★★6.** A colleague fits the same data with unweighted least squares and obtains a
steeper slope, then argues that the weighted fit is "wrong" because it disagrees.

(a) Compute the unweighted fit for the demonstration's data using the script's
seed, and report the slope.
(b) Explain which fit is correct and why, using the ratio computed in ★3.
(c) State what would have to be true of the data for the unweighted fit to be the
more efficient estimator.

---

**★★7.** A power law $y = Ax^{-p}$ is fitted to 40 points spanning $x$ from 0.1 to
100 with 10 % relative uncertainty on each $y$.

(a) State the weights to use in log space and derive them from
$\sigma_{\log y} = \sigma_y/(y \ln 10)$.
(b) The fit returns $p = 1.4073 \pm 0.0077$. Compute the 95 % interval using the
Gaussian factor 1.96, and state whether the true value 1.4 lies inside.
(c) State what the straightness of the log-log plot establishes and what it does
not.

---

**★★8.** A vertical error bar of 0.4 mGal and a horizontal error bar of 1.5 km are
drawn on the same panel.

(a) Compute the ratio of the two numbers.
(b) Explain why the ratio of the *numbers* says nothing about the ratio of the
*bars* on the page.
(c) State the caption sentence that repairs the problem when the horizontal bar is
smaller than the marker.

---

## ★★★ Research-oriented

**★★★9.** A confidence band and the data error bars are both drawn on one figure.

(a) Write the expression for the variance of the fitted value at a point $x$ in
terms of the parameter covariance.
(b) Explain why the band is narrowest at the centroid of the data.
(c) A referee asks why the band is narrower than the error bars across most of the
range and whether that means the fit is better than the data. Answer, and name the
statistic that actually tests the model.

---

**★★★10.** An errors-in-variables problem: both $x$ and $y$ carry uncertainty of
comparable size.

(a) State why ordinary weighted least squares in $y$ is biased in this case.
(b) Describe the geometric quantity that an orthogonal-distance (total
least-squares) fit minimises, and contrast it with what weighted least squares
minimises.
(c) State one situation in geophysics where the asymmetry is defensible — that is,
where the $x$ uncertainty really is negligible — and one where it is not.
