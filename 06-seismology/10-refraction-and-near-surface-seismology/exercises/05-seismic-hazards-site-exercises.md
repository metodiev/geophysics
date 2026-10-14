# Exercises — 06-10-05 Site Characterisation: Vs30 and Site Response

**All values are SYNTHETIC.** Attempt these before reading the
[solutions](./05-seismic-hazards-site-solutions.md). The lesson is
[05 Site Characterisation: Vs30 and Site Response](../05-seismic-hazards-site.md).
The demonstration's half-space is $900\ \mathrm{m\,s^{-1}}$ at
$2200\ \mathrm{kg\,m^{-3}}$ with $Q = 100$, and the soil layers carry $Q = 20$.

## ★ Foundational

**★1.** For a profile of $5\ \mathrm{m}$ at $150\ \mathrm{m\,s^{-1}}$,
$10\ \mathrm{m}$ at $250\ \mathrm{m\,s^{-1}}$ and $15\ \mathrm{m}$ at
$500\ \mathrm{m\,s^{-1}}$, compute the vertical travel time to $30\ \mathrm{m}$,
$V_{S30}$, the site class against the standard boundaries
$1500/760/360/180\ \mathrm{m\,s^{-1}}$, and the thickness-weighted arithmetic mean
for comparison.

**★2.** Compute the three exact weights
$w_i = (h_i/V_{S,i})/\Delta t$ for the profile of ★1 and verify that they sum to
one.

**★3.** Compute $4H/V_{S30}$ for the profile of ★1 and state what the rule assumes
about the column.

## ★★ Applied

**★★4.** The top layer of ★1 is stiffened by $20\%$. Using $w_1$ only, compute the
change in $V_{S30}$ in percent and in $\mathrm{m\,s^{-1}}$, and state whether the
site class changed.

**★★5.** Every layer velocity of ★1 is uncertain by $10\%$, independently. Compute
$\sigma_{V_{S30}}$ from the weights, and then as a fraction of $V_{S30}$. Explain
why the fractional uncertainty is smaller than $10\%$.

**★★6.** For a half-space at $900\ \mathrm{m\,s^{-1}}$, $2200\ \mathrm{kg\,m^{-3}}$
over a soil of $200\ \mathrm{m\,s^{-1}}$, $1900\ \mathrm{kg\,m^{-3}}$, compute the
impedance ratio and the peak $|T|$ of the lossless single-layer response. State what
makes the peak finite in a real calculation.

## ★★★ Research-oriented

**★★★7.** The demonstration's profiles A and B both have
$V_{S30} = 200.00\ \mathrm{m\,s^{-1}}$. Construct two further profiles with
$V_{S30} = 290.32\ \mathrm{m\,s^{-1}}$ — the value of ★1 — one of them a gradual
stiffening and the other a two-layer contrast. Predict, before computing, whether
their fundamental periods and peak amplifications will agree, and state the metric
by which you will check the prediction.

**★★★8.** A colleague reports $V_{S30} = 370 \pm 25\ \mathrm{m\,s^{-1}}$ and
labels the site class C. Write the two-sentence correction that keeps the number and
the uncertainty, states both admitted classes, and explains why the label is a
convention rather than a measurement.
