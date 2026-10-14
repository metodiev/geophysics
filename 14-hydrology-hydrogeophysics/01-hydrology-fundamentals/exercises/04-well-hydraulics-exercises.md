# Exercises — 14-01-04 Well Hydraulics, Pumping Tests and Aquifer Parameters

Attempt these before reading the
[solutions](./04-well-hydraulics-solutions.md). The lesson is
[04 Well Hydraulics, Pumping Tests and Aquifer Parameters](../04-well-hydraulics.md).
All tests and aquifers are **SYNTHETIC**.

Use the Theis solution $s = \dfrac{Q}{4\pi T}W(u)$ with
$u = \dfrac{r^{2}S}{4Tt}$ and the Cooper-Jacob form
$s = \dfrac{2.3026\,Q}{4\pi T}\log_{10}\dfrac{2.25\,Tt}{r^{2}S}$.

## ★ Foundational

**★1.** A constant-rate test pumps $Q = 500\ \mathrm{m^3\,d^{-1}}$. The
$s$-versus-$\log_{10}t$ line has a slope of $1.20\ \mathrm{m}$ per decade. Compute
$T$, showing the units.

**★2.** For the aquifer of ★1, the line's intercept at $s = 0$ is
$t_0 = 0.0025$ d, and the observation well is at $r = 30$ m. Compute $S$.

**★3.** For the same parameters, compute the dimensionless time $u$ at
$t = 1$ d and $r = 30$ m, and state whether the straight-line fit window is valid
at that time.

## ★★ Applied

**★★4.** A synthetic confined aquifer has $T = 250\ \mathrm{m^2\,d^{-1}}$,
$S = 1.0 \times 10^{-4}$. With $Q = 1000\ \mathrm{m^3\,d^{-1}}$ and
$r = 100$ m, compute $u$, $W(u)$ and the drawdown at $t = 2$ d, and compare with
the Cooper-Jacob value. Report the percentage difference and comment.

**★★5.** For a recovery test in the same aquifer, pumping stops after
$t_p = 2$ d. Compute the residual drawdown at $t = 4$ d (using
$s' = \frac{Q}{4\pi T}[W(u) - W(u')]$ with $t - t_p = 2$ d), and verify it against
the logarithmic form. Then, given a measured recovery slope of $0.60\ \mathrm{m}$
per decade, compute $T$ and state what assumption about $S$ the recovery analysis
required.

**★★6.** A synthetic step-drawdown test gives
$(300\ \mathrm{m^3\,d^{-1}},\ 1.035\ \mathrm{m})$,
$(900,\ 3.915)$ and $(1800,\ 10.260)$. Fit $s_w/Q = B + CQ$ to obtain $B$ and $C$,
then compute the well efficiency at each of the four rates 300, 900, 1800 and
$2700\ \mathrm{m^3\,d^{-1}}$.

## ★★★ Research-oriented

**★★★7.** Design a constant-rate pumping test that recovers $T$ to 10% and $S$ to
25% in a synthetic confined aquifer with true $T = 150\
\mathrm{m^2\,d^{-1}}$, $S = 2 \times 10^{-4}$. Choose $Q$, $r$, the observation-well
placement, the sampling schedule and the duration; show the arithmetic that each
choice satisfies (drawdown above noise, $u < 0.01$ within the test, no boundary
encountered, no dewatering of the screen). Then state the one measurement you would
add that does not rely on the Theis model at all.

**★★★8.** An unconfined aquifer has $S_y = 0.15$ and a saturated thickness of
20 m with $S_s = 1.5 \times 10^{-5}\ \mathrm{m^{-1}}$, so the confined-like early
response has $S = S_s b = 3.0 \times 10^{-4}$. Explain, with numbers, how a Theis
fit restricted to the first hour of a test would report a storativity wrong by a
factor of 500, how the error would appear on an $s$-versus-$\log t$ plot, and what
fitting strategy recovers $S_y$. State one additional diagnostic that separates
delayed yield from leakage.
