# Exercises — 07-04-03 GNSS Positioning: Pseudorange, Carrier Phase and Ambiguity Resolution

Attempt these before reading the
[solutions](./03-gnss-positioning-solutions.md). The lesson is
[03 GNSS Positioning](../03-gnss-positioning.md). The speed of light
($299792458\ \mathrm{m\,s^{-1}}$) and the L1 carrier frequency
($1575.42\ \mathrm{MHz}$) are defining constants; all geometry, noise and delays
are **SYNTHETIC**.

## ★ Foundational

**★1.** Write the pseudorange and carrier-phase observation equations in metres,
then list which terms cancel in a single difference, a double difference and a
triple difference.

**★2.** Convert $f = 1575.42\ \mathrm{MHz}$ to a wavelength, and convert an
ambiguity scatter of $0.05\ \mathrm{m}$ to cycles.

**★3.** Explain in two sentences why VDOP is larger than HDOP for any realistic
constellation.

## ★★ Applied

**★★4.** A survey has $\sigma = 4\ \mathrm{mm}$ phase noise, VDOP $= 2.5$ and
HDOP $= 1.1$. Give the vertical and horizontal uncertainties, and state the
coordinate pair $(\sigma_H,\sigma_V)$ you would expect from the formal covariance.

**★★5.** A constellation gives GDOP $= 1.8$, PDOP $= 1.6$, VDOP $= 1.4$ and
HDOP $= 0.8$. With $0.6\ \mathrm{m}$ code noise, compute the expected position
errors, verify the relation between PDOP, HDOP and VDOP, and explain why the 3-D
error is not the arithmetic sum of the components.

**★★6.** Explain why the design matrix in a double-difference ambiguity solution
loses rank if the constellation does not move between epochs, and what physical
observation strategy restores it.

## ★★★ Research-oriented

**★★★7.** A $12\ \mathrm{km}$ baseline has $40$ double differences over $8$ epochs
and a float ambiguity scatter of $0.04\ \mathrm{m}$. Decide whether to fix, estimate
the resulting baseline uncertainty, and state the tests you would apply before
accepting the fix.

**★★★8.** A low-elevation satellite carries an unmodelled $3\ \mathrm{m}$ path
delay. Predict, with reasoning, whether the resulting error appears mostly in the
height or horizontally, and design a processing step that would detect and
attribute it.
