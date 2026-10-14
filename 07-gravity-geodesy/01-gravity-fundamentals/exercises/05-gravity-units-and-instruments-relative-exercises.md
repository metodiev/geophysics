# Exercises — 07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement

Attempt these before reading the
[solutions](./05-gravity-units-and-instruments-relative-solutions.md). The lesson
is [05 Units (Gal, mGal), Absolute vs Relative Measurement](../05-gravity-units-and-instruments-relative.md).
All models are **SYNTHETIC**. Use
$1\ \mathrm{Gal} = 10^{-2}\ \mathrm{m\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$,
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$,
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$ and the model
free-air gradient $3.083\times10^{-6}\ \mathrm{s^{-2}}$.

## ★ Foundational

**★1.** Convert each of the following into all four units
($\mathrm{m\,s^{-2}}$, Gal, mGal, µGal): (a) the model surface field
$9.820250\ \mathrm{m\,s^{-2}}$; (b) $2.50\times10^{-7}\ \mathrm{m\,s^{-2}}$;
(c) $0.00450\ \mathrm{Gal}$. State which of the three is a realistic survey
signal.

**★2.** Using $r = \sqrt{GM/g}$: (a) what mass produces $1\ \mathrm{mGal}$ at a
distance of $1\ \mathrm{m}$? (b) What is $1\ \mathrm{\mu Gal}$ at $10\ \mathrm{m}$
distance equivalent to, in metres of elevation? (c) How many kilograms of rock
(density unchanged) correspond to $1\ \mathrm{\mu Gal}$ through $50\ \mathrm{m}$ of
thickness over a $1\ \mathrm{m^{2}}$ column?

**★3.** A relative meter has calibration
$c = 1.0000\times10^{-3}\ \mathrm{mGal\,count^{-1}}$ and a base value
$g_{\text{base}} = 979\,500.0000\ \mathrm{mGal}$ read at $12\,000.0$ counts.
Compute $g$ at stations reading $14\,000.0$ and $18\,000.0$ counts, and compute the
error introduced at those stations if the true calibration is $0.9995\times10^{-3}$
instead.

## ★★ Applied

**★★4.** A SYNTHETIC calibration occupies six stations with readings (counts)
$10\,000$, $12\,000$, $14\,000$, $16\,000$, $18\,000$, $20\,000$ and reference
values $979\,500.000$, $979\,502.000$, $979\,504.000$, $979\,506.000$,
$979\,508.000$, $979\,510.000\ \mathrm{mGal}$. Fit $g = cR + b$ by least squares,
report $c$ and $b$, state what $b$ means physically, and compute the residual at
each station.

**★★5.** For the same meter, a field span of $4000$ counts is measured with
$\sigma_{c} = 4.0\times10^{-7}\ \mathrm{mGal\,count^{-1}}$ and reading
repeatability $\sigma_{R} = 0.3$ counts. Compute the two uncertainty contributions
and the total, and state the count span at which the reading term becomes equal to
the calibration term.

**★★6.** A survey spans $20\,000$ counts. The meter's calibration is known to
$0.02\%$ and its readings repeat to $0.3$ counts ($c = 10^{-3}\
\mathrm{mGal\,count^{-1}}$). Compute the total difference uncertainty in
microgal, then compute how many repeat readings would be needed to make the
reading term irrelevant — and state whether that would improve the result at all.

## ★★★ Research-oriented

**★★★7.** Design a calibration experiment that determines $c$ to $0.01\%$ (1σ),
using only relative measurements, one absolute datum with uncertainty
$\sigma_{\text{abs}}$, and a set of stations whose gravity differences you may
choose. Specify the span needed, the number of stations, the reference
uncertainty required, and predict the residual $c$–$b$ correlation as a function of
the span. State what would falsify the design.

**★★★8.** Design a 20-station network, tied to a single absolute base, that must
deliver $15\ \mathrm{\mu Gal}$ (1σ) at the furthest station. Using the lesson's
accumulation rule, choose the meter repeatability, the number and placement of
ties, and the datum accuracy. State the dominant term in your budget.

**★★★9.** An instrument manufacturer claims $1\ \mathrm{\mu Gal}$ repeatability and
$0.01\%$ calibration accuracy. Compute the two contributions to the uncertainty of
a $10\,000$-count difference, then write a paragraph explaining to a
non-specialist why the second number, not the first, limits a regional survey —
and construct the one experiment that would verify the claim.
