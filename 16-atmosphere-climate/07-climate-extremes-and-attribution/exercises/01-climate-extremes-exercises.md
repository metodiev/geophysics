# Exercises — 16-07-01 Extreme Events: Statistics and Physical Drivers

Attempt these before reading the
[solutions](./01-climate-extremes-solutions.md). The lesson is
[01 Extreme Events](../01-climate-extremes.md). All models and numbers are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A GEV has $\mu = 100.0$, $\sigma = 15.0$ and $\xi = 0.20$ (rainfall in
mm/day). Compute the 10-year and 50-year return levels and state the units of
each term.

**★2.** For the same GEV, compute the return level in the limit $\xi \to 0$ and
state whether the positive shape raises or lowers the far-tail level relative to
the Gumbel case.

**★3.** A POT analysis has threshold $u = 90.0\ \mathrm{mm\,day^{-1}}$,
generalised-Pareto scale $\tilde\sigma = 16.0\ \mathrm{mm\,day^{-1}}$, shape
$\xi = 0.12$ and $\lambda = 2.5$ exceedances per year. Compute the 20-year
return level.

## ★★ Applied

**★★4.** Show algebraically that $\tilde\sigma = \sigma + \xi(u-\mu)$ makes the
GEV and POT expressions for $z_T$ identical at the threshold, and verify the
identity numerically by mapping the demonstration's block-maxima parameters
($\hat\mu = 111.67$, $\hat\sigma = 17.51$, $\hat\xi = 0.111$) to the POT scale at
$u = 90.21\ \mathrm{mm\,day^{-1}}$.

**★★5.** In the demonstration, the 100-year level from a 50-year record has a
5–95% interval width of $106.1\ \mathrm{mm\,day^{-1}}$, and from a 1000-year
record $19.7\ \mathrm{mm\,day^{-1}}$. By what factor should the width change
between the two if it scaled exactly as $1/\sqrt{n}$, and by what factor does it
actually change? What does the difference tell you?

**★★6.** A reviewer asks for the 100-year rainfall "for the year 2050" from a
record with a significant linear trend in the location parameter. Write the two
or three sentences you would put in the report, naming the reference climate and
the assumption you are making.

## ★★★ Research-oriented

**★★★7.** Design an experiment, specifying the code you would write and the
metric you would report, to measure how a *mixture* of two GEV populations in one
series biases a single-population block-maxima fit. State the prediction you
would test and what result would falsify the single-population model.

**★★★8.** The Clausius–Clapeyron relation gives about $7\%/\mathrm{K}$ for
moisture. Suppose a synthetic study reports that wet-day 3-day rainfall maxima
rose by $10\%/\mathrm{K}$. List three distinct physical mechanisms that could
produce a scaling above the thermodynamic value, and for each state one
observable that would distinguish it from a change in the moisture supply alone.
