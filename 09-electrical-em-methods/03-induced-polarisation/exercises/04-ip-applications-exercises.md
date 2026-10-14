# Exercises — 09-03-04 IP for Sulphides, Clays, Contaminants and Permafrost

Attempt these before reading the
[solutions](./04-ip-applications-solutions.md). The lesson is
[04 IP Applications](../04-ip-applications.md). All models are **SYNTHETIC**
teaching values throughout: no end-member, scenario or number is a measurement
of a real rock, ore body, soil or site.

## ★ Foundational

**★1.** With formation factor $F = 6.617$, surface conductance
$B = 0.0020$ S/m and intrinsic pathway chargeability $m_0 = 0.30$, compute the
electrolyte conductance $A$, the bulk conductivity, the resistivity and
$m_{\text{eff}}$ for a pore fluid with $\sigma_w = 0.010$ S/m.

**★2.** From the lesson's end-member table, which end-member has the largest peak
phase and which the largest peak frequency? Give both factors of the ratios
between the extremes, and state why the peak frequency is the more informative
of the two for separating frozen ground from clean sand.

**★3.** Using the lesson's scenario table,
(a) identify the scenario that matches
$\rho = 6.53\ \Omega\,\mathrm{m}$ with a peak phase of $1.156$ mrad;
(b) identify the scenario that matches $\rho = 23.24\ \Omega\,\mathrm{m}$ with
$69.268$ mrad; (c) state which of the two measurements alone would have confused
the two answers, and why.

## ★★ Applied

**★★4.** Derive $m_{\text{eff}} = m_0B/\left[A(1-m_0) + B\right]$ from the two
parallel pathways, and verify the limits $A = 0$ and $A \gg B$.

**★★5.** The confusion matrix computed from phase alone puts clay-rich soil
against frozen ground at $1.39$ noise units (with $2$ mrad noise), while the
matrix that also uses $\lvert\rho\rvert$ puts the same pair at $305.9$ units.
Explain the change with reference to the physical difference between the two
end-members, and state which measurement is doing the work.

**★★6.** For the frozen scenario the bulk conductivity is
$4.1511\times10^{-5}$ S/m against the base case's $0.009556$ S/m. Compute the
fraction retained and the resistivity change, and check both against the
lesson's printed percentage changes.

## ★★★ Research-oriented

**★★★7.** The synthetic surface conductance $B$ is halved by a change in surface
chemistry while the pore fluid is unchanged ($\sigma_w = 0.05$ S/m,
$F = 6.617$, $m_0 = 0.30$). Compute the new bulk conductivity, resistivity,
$m_{\text{eff}}$ and peak phase, and decide whether the change is detectable by
resistivity alone, by phase alone, or only by both, using the lesson's stated
thresholds of $1\%$ and $2$ mrad. State the interpretation you would report and
the alternative interpretations you cannot exclude.

**★★★8.** Design the measurement that would separate the single Cole-Cole fit
($\rho_0 = 61.52\ \Omega\,\mathrm{m}$, $m = 0.2936$, $c = 0.3112$,
$\tau = 0.204$ s) from the two-component mixture fit
($\tau = 0.021$ s and $2.257$ s, weights $0.511/0.489$), given that they differ
by up to $6.6$ mrad outside the fitted band. State the band, the noise level, the
decision criterion, and what you would report if the budget did not allow it.
