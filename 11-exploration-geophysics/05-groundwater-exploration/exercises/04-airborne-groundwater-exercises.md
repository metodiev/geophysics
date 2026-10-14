# Exercises — 11-05-04 Airborne EM for Regional Aquifer Mapping

Attempt these before reading the
[solutions](./04-airborne-groundwater-solutions.md). The lesson is
[04 Airborne EM for Regional Aquifer Mapping](../04-airborne-groundwater.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the diffusion depth at $t = 0.1\ \mathrm{ms}$, $1\ \mathrm{ms}$
and $10\ \mathrm{ms}$ for $\rho = 30\ \Omega\,\mathrm{m}$, using
$d = 1261.6\sqrt{\rho t}$. State the units of every factor.

**★2.** For the kernel $K(z,t) = \dfrac{z}{2Dt}e^{-z^{2}/(4Dt)}$, show by
substitution that $\int_0^{\infty}K\,\mathrm{d}z = 1$ and that its maximum is at
$z = \sqrt{2Dt}$.

**★3.** A conductance anomaly is $S = 2.5\ \mathrm{S}$. Compute the thickness of
an equivalent layer for $\sigma = 0.05$, $0.25$ and $1.0\
\mathrm{S\,m^{-1}}$, and state which of the three is physically plausible as an
aquifer.

## ★★ Applied

**★★4.** A target lies at $80\ \mathrm{m}$ depth in $50\ \Omega\,\mathrm{m}$
ground. Compute the gate time whose diffusion depth is $80\ \mathrm{m}$, and the
DOI at that time using the $30\%$ level $z_{\text{DOI}} = 1.55\,d$.

**★★5.** Using the lesson's altitude/coupling table, estimate the depth limit of
a survey flown at $50\ \mathrm{m}$ altitude with a $2\%$ noise floor and a
$3\times$ detection threshold. State the assumption you made.

**★★6.** An AEM anomaly has prior probability $p = 0.12$ of being a usable
aquifer. The signature appears in $70\%$ of aquifers and in $40\%$ of clays.
Compute the positive predictive value, and state how many of 50 such anomalies
you expect to be worth drilling.

## ★★★ Research-oriented

**★★★7.** Design a two-stage survey for an arid basin: an AEM regional block plus
ground follow-up. Specify the flight altitude, the moment rationale, the gates,
the line spacing, the follow-up method and the decision rule that converts an AEM
anomaly into a drilling recommendation with a stated error rate. Justify every
number with a relation from the lesson.

**★★★8.** A colleague reports that a deeper AEM gate "images the aquifer at
150 m". Using the kernel, show numerically why the claim is unsafe: compute the
fraction of the kernel's weight lying above 100 m at the gate in question, and
state what the observation does and does not constrain.
