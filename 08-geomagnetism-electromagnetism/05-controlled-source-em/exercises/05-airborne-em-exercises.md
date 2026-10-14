# Exercises — 08-05-05 Airborne EM for Conductivity Mapping

Attempt these before reading the
[solutions](./05-airborne-em-solutions.md). The lesson is
[05 Airborne EM](../05-airborne-em.md). All models are **SYNTHETIC** teaching
values.

## ★ Foundational

**★1.** Compute the weak-induction height factor
$r/\sqrt{r^2+4h^2}$ for $r=8\ \mathrm{m}$ and $h=25\ \mathrm{m}$. Express the
signal loss in decibels and in per cent.

**★2.** Using the lesson's table of the height–conductivity trade-off at
$1.6\ \mathrm{kHz}$, state the conductivity error produced by a $1\ \mathrm{m}$
height error at $20$, $40$ and $60\ \mathrm{m}$ flight height, and say in one
sentence how the three compare.

**★3.** A cover of conductance $8\ \mathrm{S}$ sits over a target. Using the
lesson's masking table, state the fraction of the target's anomaly that survives,
and say in one sentence what increasing the stacking by a factor of ten would do
for it.

## ★★ Applied

**★4.** Derive the height factor from the kernel of the layered response, using
$\int_0^\infty e^{-a\lambda}J_0(\lambda r)\,\mathrm{d}\lambda
=1/\sqrt{a^2+r^2}$ and the weak-induction limit
$R(\lambda)\to-k^2/(4\lambda^2)$ for large $\lambda$.

**★5.** The altimeter on a survey is good to $0.5\ \mathrm{m}$. At which
frequencies (from $400\ \mathrm{Hz}$, $1.6$, $6.4$ and $25.6\ \mathrm{kHz}$) can
the conductivity be quoted to better than $5\%$, at flight heights of $20$ and
$60\ \mathrm{m}$? Use the lesson's trade-off table and interpolate where
necessary.

**★6.** A target is a sheet of conductance $2\ \mathrm{S}$ at $120\ \mathrm{m}$
depth. From the lesson's depth-of-investigation table, state the best channel and
the relative anomaly, and decide whether a system whose lowest channel is
$400\ \mathrm{Hz}$ can see it at all.

## ★★★ Research-oriented

**★7.** Design a levelling and quality-control procedure that would detect a
height-correlated bias in a delivered conductivity map. Specify the flight-line
and tie-line geometry, the statistic you will monitor, the null result that would
give you confidence, and the alternative explanations for a positive result.

**★8.** A client asks for a conductivity map that distinguishes $0.05$ from
$0.02\ \mathrm{S\,m^{-1}}$ at $80\ \mathrm{m}$ depth over terrain with a
$20\ \mathrm{S}$-conductance cover. Using the scalings measured in this lesson,
state which of the requested specifications is plausible, which is not, and what
the cheapest change to the survey would be that improves the one that is
marginal.
