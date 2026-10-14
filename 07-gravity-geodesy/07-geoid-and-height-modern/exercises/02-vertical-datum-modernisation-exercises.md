# Exercises — 07-07-02 Vertical Datum Modernisation and National Height Systems

Attempt these before reading the
[solutions](./02-vertical-datum-modernisation-solutions.md). The lesson is
[02 Vertical Datum Modernisation](../02-vertical-datum-modernisation.md). **All
models and data in this module are SYNTHETIC.**

Constants: $\gamma_{45} = 9.806199\ \mathrm{m\,s^{-2}}$, normal free-air
gradient $0.3086\times10^{-5}\ \mathrm{m\,s^{-2}\,m^{-1}}$, Poincaré–Prey mean
gravity gradient $0.0424\ \mathrm{mGal\,m^{-1}}$.

## ★ Foundational

**★1.** Compute $H_{\text{dyn}}$ for $C = 5000\ \mathrm{m^{2}\,s^{-2}}$, stating
the gravity used and why that particular value is chosen by convention.

**★2.** A 100 km levelling line climbs 500 m. Estimate the orthometric correction
from the product of the fractional gravity change and the height gain, and state
the two quantities it depends on.

**★3.** Show algebraically that a constant offset $\delta$ added to every
orthometric height leaves every height *difference* unchanged.

## ★★ Applied

**★★4.** Compute $H_{\text{dyn}}$, $H_{\text{ortho}}$ (with
$\bar g = 9.8070$) and $H_{\text{norm}}$ (with $\bar\gamma = 9.8085$) for
$C = 6000\ \mathrm{m^{2}\,s^{-2}}$, and state the kind of quantity each
difference between them is.

**★★5.** For a levelling standard of $2\ \mathrm{mm\,\sqrt{km}^{-1}}$ and a
GNSS+geoid error of $3.0\ \mathrm{cm}$ at a point, compute the crossover length
for absolute heights. Then repeat for the error in a difference, using a geoid
error that is $90\%$ correlated in a difference and a GNSS error that is white.

**★★6.** A modernised datum replaces levelling with GNSS+geoid. State two
applications where the *absolute* height matters and two where only differences
matter, and for each say which error term dominates.

## ★★★ Research-oriented

**★★★7.** Design the publication set that would make a national datum change
*verifiable* rather than merely documented. For each item, state the diagnostic
that would detect an error in it, and the independent data that would resolve the
disagreement.

**★★★8.** Design a synthetic experiment that measures how much a wrong
mean-gravity hypothesis ($\bar g$) biases an orthometric height, and how the same
error appears in normal heights. State which of the two is affected and why.
