# Exercises — 11-07-04 Case Study: Arid-Region Groundwater Exploration

Attempt these before reading the
[solutions](./04-case-study-groundwater-solutions.md). The lesson is
[04 Case Study: Arid-Region Groundwater Exploration](../04-case-study-groundwater.md).
All models are **SYNTHETIC** argument archetypes: no real basin, aquifer or
borehole is used, and no site-specific number is quoted.

## ★ Foundational

**★1.** An AEM indicator has $\mathrm{TPR} = 0.65$ and $\mathrm{FPR} = 0.20$.
Compute the posterior probability that a site is productive given an anomaly, for
a base rate of $0.10$.

**★2.** For the posterior of ★1, compute the expected number of holes drilled per
productive well and the dry-hole fraction.

**★3.** A region has $150\ \mathrm{mm\,yr^{-1}}$ of rainfall, a recharge
coefficient of $0.04$ and an area of $800\ \mathrm{km^{2}}$. Compute the annual
recharge in $\mathrm{m^{3}\,yr^{-1}}$.

## ★★ Applied

**★★4.** A programme has 200 candidate sites, a $10\%$ base rate, an AEM
indicator with $\mathrm{TPR} = 0.65$, $\mathrm{FPR} = 0.20$, and a TDEM follow-up
with $\mathrm{TPR} = 0.85$, $\mathrm{FPR} = 0.10$ (conditionally independent).
Compute the number of AEM anomalies and the number of sites retained by TDEM.

**★★5.** Using the costs of the lesson's demonstration (AEM $0.05$ per site,
TDEM $0.5$ per site, well $10$, productive well worth $80$), compute the net value
of (i) drilling all 200 sites, (ii) AEM then drilling anomalies, (iii) AEM + TDEM
then drilling. State which strategy you would recommend and why.

**★★6.** With the recharge of ★3 and an abstraction of
$0.4\times10^{6}\ \mathrm{m^{3}\,yr^{-1}}$ per well, compute the number of wells
supported at steady state. With a storage of $200\times10^{6}\ \mathrm{m^{3}}$ and
20 wells, compute the storage-depletion time.

## ★★★ Research-oriented

**★★★7.** Write an exploration recommendation for an arid-region programme:
state the target, the two-stage survey, the prior you would use and how you would
establish it, the decision rule, and the sustainability caveat. Quote no
site-specific numbers.

**★★★8.** The lesson assumes the two survey stages are conditionally
independent. Describe a geological situation in which they are not, show how the
correlation would change the staged strategy's cost per productive well, and
propose a design change that restores some independence.
