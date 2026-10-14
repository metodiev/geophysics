# Exercises — 11-06-04 Landfill, Waste and Brownfield Site Assessment

Attempt these before reading the
[solutions](./04-landfill-and-waste-solutions.md). The lesson is
[04 Landfill, Waste and Brownfield Site Assessment](../04-landfill-and-waste.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** State the low-induction-number relation
$\sigma_a = \int\sigma(z)K(z)\,\mathrm{d}z$ with $\int K = 1$, and show that a
uniform half-space of conductivity $\sigma_0$ gives $\sigma_a = \sigma_0$ exactly.

**★2.** Compute the conductance $S = \sigma h$ of (a) a $12\ \mathrm{m}$ layer at
$0.04\ \mathrm{S\,m^{-1}}$ and (b) a $3\ \mathrm{m}$ layer at
$0.16\ \mathrm{S\,m^{-1}}$. State which is more plausible as a leachate plume and
why the two are hard to separate.

**★3.** Compute the magnetic anomaly at $2\ \mathrm{m}$ and $4\ \mathrm{m}$ depth
of a compact ferrous object with moment $100\ \mathrm{A\,m^{2}}$, in nT.

## ★★ Applied

**★★4.** Two layers have the same conductance $S = 0.5\ \mathrm{S}$: A is 10 m of
$0.05\ \mathrm{S\,m^{-1}}$ and B is 2.5 m of $0.20\ \mathrm{S\,m^{-1}}$, both
starting at 2 m. Using the lesson's kernel-fraction argument, state which model
gives the larger apparent conductivity for a system with a kernel peaking at
(a) 2.5 m and (b) 15 m, and explain the difference in one sentence.

**★★5.** A site has a prior $p = 0.05$ that a conductive anomaly is
contamination, with $\mathrm{TPR} = 0.90$ and $\mathrm{FPR} = 0.50$. Compute the
posterior probability and the false-discovery rate, and state how many of 40
flagged anomalies you expect to be real.

**★★6.** For a cap of $150\ \Omega\,\mathrm{m}$ over waste of
$5\ \Omega\,\mathrm{m}$, compute the Schlumberger apparent resistivity at
$AB/2 = 20\ \mathrm{m}$ for cap thicknesses of 1, 3 and 8 m, and state which part
of the sounding curve carries the thickness information.

## ★★★ Research-oriented

**★★★7.** Design a two-method survey for an unengineered waste site of unknown
extent, where the questions are (i) waste boundary, (ii) depth to the base,
(iii) leachate presence. Specify the methods, the line spacing, the expected
contrasts and, for each question, the false-negative mode. State the decision
rule that converts the results into a drilling plan.

**★★★8.** The lesson's PPV calculation uses fixed $\mathrm{TPR}$ and
$\mathrm{FPR}$. Design an empirical test of the true $\mathrm{POD}$ on a site
where some anomalies are excavated (ground truth is available), including how you
would avoid circularity, and state how the result should change a clearance-style
claim.
