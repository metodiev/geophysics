# Exercises — 17-08-04 Cryosphere Remote Sensing: Ice, Snow and Permafrost

Attempt these before reading the
[solutions](./04-cryosphere-rs-solutions.md). The lesson is
[04 Cryosphere Remote Sensing](../04-cryosphere-rs.md). All models and values
are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** Using the synthetic albedo model, compute the albedo of clean snow at
grain size $200\ \mu\mathrm{m}$ and at $1000\ \mu\mathrm{m}$, and state the
difference.

**★2.** Two images taken $24$ days apart show a displacement of $4$ pixels with
a pixel size of $15\ \mathrm{m}$. Compute the surface speed in
$\mathrm{m\,yr^{-1}}$.

**★3.** State the sign of the snow-depth bias introduced by (i) saturation and
(ii) forest cover.

## ★★ Applied

**★★4.** Using the saturation relation $\Delta T_B = 6.0(1 - e^{-\mathrm{SD}/45})$
and coefficient $7.5\ \mathrm{cm\,K^{-1}}$, compute the retrieved depth for a
true depth of $60\ \mathrm{cm}$, and the bias. Repeat with a forest fraction of
$0.25$.

**★★5.** For the displacement of ★2, compute the uncertainty from $\pm 0.5$
pixel in $\mathrm{m\,yr^{-1}}$, and express it as a percentage of the speed.

**★★6.** A displacement series has a seasonal amplitude of $5.00\ \mathrm{cm}$
and a secular settlement of $1.0\ \mathrm{cm\,yr^{-1}}$. Over five years, compute
the total secular displacement and compare it with the seasonal amplitude; state
why one map cannot separate them.

## ★★★ Research-oriented

**★★★7.** Design a validation of a glacier-velocity product. State the reference
you would use, the spatial and temporal matching you would apply, the metric, and
the reason a mismatch may be a real physical signal rather than an error. A
specification that could not be executed is a failed answer.

**★★★8.** Explain why *wet* snow destroys the passive-microwave depth retrieval,
using the emission physics, and state what a careful product does at melt onset.
