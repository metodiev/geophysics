# Exercises — 15-01-05 Sea Level, Tides and Harmonic Analysis

Attempt these before reading the
[solutions](./05-sea-level-and-tides-solutions.md). The lesson is
[05 Sea Level and Tides](../05-sea-level-and-tides.md). All records are
**SYNTHETIC**; the astronomical constants are standard values.

Constants: $G = 6.674\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$R = 6.371\times10^{6}\ \mathrm{m}$, $g = 9.81\ \mathrm{m\,s^{-2}}$,
$M_{\text{Moon}} = 7.342\times10^{22}\ \mathrm{kg}$,
$d_{\text{Moon}} = 3.844\times10^{8}\ \mathrm{m}$; constituent periods M2
$12.4206012$ h, S2 $12.0000000$ h, K1 $23.9344721$ h, O1 $25.8193417$ h.

## ★ Foundational

**★1.** Compute $\zeta_{\max}$ for a body of twice the Moon's mass at the Moon's
distance. State the scaling law you used and the unit.

**★2.** Show that the tide-generating potential's leading term falls off as
$d^{-3}$ while the direct gravitational attraction falls off as $d^{-2}$, and
state in one sentence why this makes the Moon's tide dominate the Sun's.

**★3.** Write the harmonic model for three constituents as a matrix equation
$\mathbf{d} = \mathbf{G}\mathbf{m}$, and state the dimensions of
$\mathbf{G}$ for a 30-day record sampled every hour.

## ★★ Applied

**★★4.** (a) Compute the Rayleigh period for separating K1 from O1, in hours and
days. (b) State whether a 20-day record can separate them. (c) Repeat the
calculation for the pair M2 and N2, given that a hypothetical N2 period is
$12.6583\ \mathrm{h}$.

**★★5.** A constituent of true period $12.66\ \mathrm{h}$ is sampled (a) every
6 h and (b) every 12.4 h. Compute the alias frequency and period in each case and
state which sampling resolves the constituent.

**★★6.** A 20-year synthetic record of monthly means is fitted with a datum, a
linear trend and an annual cycle. The noise is Gaussian with
$\sigma = 25\ \mathrm{mm}$. (a) Compute $\mathrm{Var}(\hat b)$ from
$\sigma^{2}/\sum(t_k-\bar t)^{2}$ using $\sum(t_k-\bar t)^{2} = N(N^{2}-1)/(12^{3})$
with $t_k$ in years. (b) Predict the trend uncertainty for a 10-year record with
the same noise. (c) State the scaling with record length.

**★★7.** The demonstration's 60-day fit has a condition number of 1.466 and all
four constituents carry the same formal $\sigma = 0.0013\ \mathrm{m}$. (a) Explain
why the errors are equal despite the amplitudes differing by a factor 12. (b)
Compute the relative error on O1 and on M2 and state which constituent is
better determined *in relative terms*. (c) State what you would change in the
design to improve the O1 estimate.

## ★★★ Research-oriented

**★★★8.** Design a tide-gauge deployment and analysis that would determine a
$2\ \mathrm{mm\,yr^{-1}}$ sea-level trend to $\pm1\ \mathrm{mm\,yr^{-1}}$. State
(a) the sampling, (b) the record length implied by your error budget, (c) the
terms you can control, and (d) the terms you cannot control and therefore cannot
remove. A specification that could not be executed is a failed answer.

**★★★9.** Two colleagues disagree. One reports "the tide at this site is
semidiurnal, M2 amplitude $1.20\ \mathrm{m}$" from a 60-day record. The other
reports "M2 amplitude $1.31\ \mathrm{m}$, S2 $0.28\ \mathrm{m}$" from a 10-day
record. Using the demonstration's own condition numbers and errors, adjudicate:
state which report is defensible, what number quantifies the problem, and what
single additional piece of information would settle it.
