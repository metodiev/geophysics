# Exercises — 17-08-03 Soil Moisture Remote Sensing and Its Validation

Attempt these before reading the
[solutions](./03-soil-moisture-rs-solutions.md). The lesson is
[03 Soil Moisture Remote Sensing and Its Validation](../03-soil-moisture-rs.md).
All models and values are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** State whether brightness temperature rises or falls as soil moisture
rises, and why. Quote two values from the lesson's table to support the answer.

**★2.** A retrieval has sensitivity $\partial T_B/\partial m_v = -200\
\mathrm{K}$ per $(\mathrm{m^3\,m^{-3}})$ and radiometric noise
$0.6\ \mathrm{K}$. Compute the moisture precision.

**★3.** Define *footprint* and *heterogeneity*, and state why they matter for
validation.

## ★★ Applied

**★★4.** At $m_v = 0.20$ an ignored canopy biases the retrieval by
$-0.0447\ \mathrm{m^3\,m^{-3}}$. The retrieval precision is
$0.0018\ \mathrm{m^3\,m^{-3}}$. Compute the ratio of bias to precision and state
what it says about the claim "the retrieval is accurate to $0.002$".

**★★5.** In the validation table the regression slope falls from $1.003$ to
$0.723$ as heterogeneity grows. Compute the fraction by which the slope is
attenuated, and name the statistical effect. State whether the product is
over-sensitive or the comparison is noisy.

**★★6.** A validation target is RMSD $\le 0.04$. With heterogeneity sd $0.04$
giving RMSD $0.0391$ and the retrieval adding $0.0018$, compute the combined RMSD
(in quadrature) and state which term dominates.

## ★★★ Research-oriented

**★★★7.** Design a validation that can separate a genuine product error from a
footprint-scale mismatch. State the reference network you would deploy, the
up-scaling method, the metric, and why the design can attribute error to the
product rather than the comparison. A specification that could not be executed
is a failed answer.

**★★★8.** Explain why a single point probe cannot validate a footprint product,
and describe (conceptually) how *three* independent, mutually imperfect
measurements — a satellite product, a land model, and an in-situ network — can
be combined to estimate each one's error without a perfect reference.
