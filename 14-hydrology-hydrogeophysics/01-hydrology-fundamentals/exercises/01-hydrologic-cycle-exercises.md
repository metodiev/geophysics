# Exercises — 14-01-01 The Hydrologic Cycle and Water Balance

Attempt these before reading the
[solutions](./01-hydrologic-cycle-solutions.md). The lesson is
[01 The Hydrologic Cycle and Water Balance](../01-hydrologic-cycle.md). All
catchments and series below are **SYNTHETIC** teaching values.

Use $1\ \mathrm{mm}$ over $1\ \mathrm{km^2} = 1000\ \mathrm{m^3}$ and
1 Julian year $= 365.25 \times 86400\ \mathrm{s} = 3.15576 \times 10^{7}\
\mathrm{s}$ throughout.

## ★ Foundational

**★1.** Convert each of the following to cubic metres.

  (a) $25\ \mathrm{mm}$ of rain over $12\ \mathrm{km^2}$.
  (b) $1\ \mathrm{mm}$ of rain over $1\ \mathrm{km^2}$.
  (c) $320\ \mathrm{mm\,yr^{-1}}$ over $250\ \mathrm{km^2}$, as a volume per year.

**★2.** A synthetic catchment has $P = 1000\ \mathrm{mm\,yr^{-1}}$,
$ET = 600\ \mathrm{mm\,yr^{-1}}$ and $Q = 350\ \mathrm{mm\,yr^{-1}}$. Compute
$\Delta S$, the runoff coefficient $Q/P$ and the evaporative index $ET/P$, and
verify that the three ratios sum to 1.

**★3.** A synthetic aquifer holds $V = 2.4 \times 10^{8}\ \mathrm{m^3}$ of
mobile water and discharges $3.0 \times 10^{7}\ \mathrm{m^3\,yr^{-1}}$. Compute
the mean residence time in years and in days.

## ★★ Applied

**★★4.** A synthetic basin of $400\ \mathrm{km^2}$ has
$Q = 350\ \mathrm{mm\,yr^{-1}}$. Convert this to a mean discharge in
$\mathrm{m^3\,s^{-1}}$ and in $\mathrm{L\,s^{-1}}$, showing the unit cancellation.

**★★5.** A synthetic catchment has $P = 1200\ \mathrm{mm\,yr^{-1}}$,
$ET = 800\ \mathrm{mm\,yr^{-1}}$, $Q = 380\ \mathrm{mm\,yr^{-1}}$, so
$\Delta S = 20\ \mathrm{mm\,yr^{-1}}$. Assuming errors of 5% on $P$, 10% on $ET$
and 5% on $Q$, compute each term's contribution as a percentage of $\Delta S$.
To what accuracy would $Q$ have to be measured for the $Q$ error to contribute
only 10% of $\Delta S$?

**★★6.** The synthetic daily hydrograph of the lesson has an annual total of
$574.8\ \mathrm{mm}$ over $250\ \mathrm{km^2}$. With a filter time constant of
$30\ \mathrm{d}$ the baseflow is $434.7\ \mathrm{mm}$ and the stormflow
$140.0\ \mathrm{mm}$. Convert all three to $\mathrm{m^3\,s^{-1}}$ and check that
the parts sum to the total.

**★★7.** A recession follows $Q(t) = 12.0\exp(-t/45)\ \mathrm{mm\,d^{-1}}$.
Compute $Q$ at $t = 0, 30, 60, 90\ \mathrm{d}$. Then, given only the two pairs
$Q(0) = 6.00$ and $Q(20) = 3.00\ \mathrm{mm\,d^{-1}}$, recover the recession
constant.

## ★★★ Research-oriented

**★★★8.** A stakeholder asks whether a synthetic basin's groundwater storage is
declining. The candidate measurements are: (i) repeat water-level surveys,
(ii) repeat microgravity, (iii) satellite gravimetry, (iv) the water balance of
this lesson. For each, state the quantity it measures directly, an order-of-
magnitude detection threshold in mm of water, and one systematic error that could
masquerade as a trend. Then design a 10-year monitoring plan that could detect a
$5\ \mathrm{mm\,yr^{-1}}$ decline, with a short arithmetic error budget showing
why a single year of water-balance data cannot do the job.
