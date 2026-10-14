# Exercises — 15-02-06 Ocean-Bottom Seismology and OBS Networks

Attempt these before reading the
[solutions](./06-obn-ocean-bottom-seismology-solutions.md). The lesson is
[06 Ocean-Bottom Seismology](../06-obn-ocean-bottom-seismology.md). All models are
**SYNTHETIC** teaching values.

Use $c = 1500\ \mathrm{m\,s^{-1}}$ unless told otherwise.

## ★ Foundational

**★1.** Compute $T_w$ and the first spectral notch frequency for a water depth of
$2500\ \mathrm{m}$, and convert $T_w$ back to a depth as a check.

**★2.** A record shows repeated seabed arrivals at $5.33$, $10.67$ and
$16.00\ \mathrm{s}$. Compute the water depth, and state the error introduced if the
true sound speed is $1530\ \mathrm{m\,s^{-1}}$ instead of $1500$.

**★3.** Convert a tilt of $2^\circ$ into the fraction of horizontal motion that
leaks onto the vertical channel, and state the units of the number.

## ★★ Applied

**★★4.** Compute the Ps delay for a $3\ \mathrm{km}$ layer with
$v_p = 2500\ \mathrm{m\,s^{-1}}$, $v_s = 1400\ \mathrm{m\,s^{-1}}$ and
$p = 0.055\ \mathrm{s\,km^{-1}}$. Then compute the ratio of that delay to $T_w$ for
water depths of $3000\ \mathrm{m}$ and $150\ \mathrm{m}$, and state in which case
the record becomes an unresolvable comb.

**★★5.** Compute the leaked horizontal amplitude on the vertical channel for tilts
of $0.3^\circ$, $1.0^\circ$ and $3.0^\circ$, and state the tilt required to keep
the leakage below $0.5\,\%$ of the horizontal amplitude.

**★★6.** An OBS records for 250 days with a clock drifting at
$0.005\ \mathrm{s\,day^{-1}}$. Compute the accumulated timing error, and the
location error it implies at apparent velocities of $8\ \mathrm{km\,s^{-1}}$ and
$3.5\ \mathrm{km\,s^{-1}}$. State which phase is more sensitive and why.

**★★7.** The demonstration measures a compliance correction that reduces the
vertical variance by a factor 410 with a residual equal to the instrument noise.
(a) State the two diagnostics that establish that the correction was correct.
(b) Explain why a single scalar transfer leaves a residual eight times larger.

## ★★★ Research-oriented

**★★★8.** Design an OBS deployment to determine a $1\ \mathrm{mm\,s^{-1}}$
anomaly in mantle shear velocity, stating the instrument requirements (clock,
tilt, pressure, coupling), the array geometry, the noise budget, and the one
requirement you cannot verify until after recovery. A specification that could not
be executed is a failed answer.

**★★★9.** The water-layer multiple comb is a nuisance in receiver-function work
and a measurement in bathymetric work. Design a single processing step that
exploits it rather than suppressing it, and state the assumption about the
seafloor reflection coefficient that the step requires.
