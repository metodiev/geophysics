# Exercises — 14-02-01 ERT for Aquifer Characterisation and Salinity Mapping

Attempt these before reading the
[solutions](./01-ert-for-hydrology-solutions.md). The lesson is
[01 ERT for Aquifer Characterisation and Salinity Mapping](../01-ert-for-hydrology.md).
All sites and datasets are **SYNTHETIC**.

Use Archie $\rho_{\text{bulk}} = a\rho_w/(\phi^{m}S_w^{n})$ with $a = 1$, $m = 2$,
$n = 2$, and the synthetic calibration
$\sigma_w = 0.15\,\mathrm{TDS}$ [g L$^{-1}$] S m$^{-1}$. The Wenner two-layer
response of the lesson is
$\rho_a = \rho_1[1 + 4\sum k^{n}(\ldots)]$ with
$k = (\rho_2-\rho_1)/(\rho_2+\rho_1)$.

## ★ Foundational

**★1.** Compute the reflection coefficient for $\rho_1 = 100$ and
$\rho_2 = 25\ \Omega$ m. State what $\rho_a$ tends to as $a \to 0$ and what it
tends to as $h \to 0$.

**★2.** The lesson's strong-contrast curve falls to $\rho_a/\rho_1 = 0.705$ at
$a = 8$ m and $0.454$ at $a = 12$ m. Interpolate in $\log_{10}a$ to find the
spacing at which $\rho_a/\rho_1 = 0.5$, and use the empirical rule
$h \approx a_{50}/1.4$ to estimate the depth. Compare with the true 8 m.

**★3.** A bulk resistivity of $55\ \Omega$ m is measured in a sand of
$\phi = 0.30$ at $S_w = 1$. Compute $\rho_w$, $\sigma_w$ and the TDS.

## ★★ Applied

**★★4.** The same $60\ \Omega$ m measurement is interpreted at
$\phi = 0.25$, $0.30$ and $0.35$, and then at $\phi = 0.30$ with $m = 1.8$ and
$2.2$. Report the full range of TDS consistent with the measurement and state
which parameter dominates the ambiguity.

**★★5.** A synthetic aquifer has $\phi = 0.28$, TDS $= 800\
\mathrm{mg\,L^{-1}}$ at the first survey. Compute the bulk resistivity. A second
survey shows a $9.1\%$ drop. Compute the TDS that explains it, then compute the
temperature rise that would explain the same drop given a $2\%$ per $^\circ$C
dependence. Finally, work out whether a falling water table could explain it at all,
and justify the sign of your answer.

**★★6.** Design the Wenner spacing list for a saline aquifer at 12 m depth,
covering roughly $0.25h$ to $5h$, and state the expected spacing at which the
curve has fallen to half of $\rho_1$.

## ★★★ Research-oriented

**★★★7.** A 1 m thick saline layer of $2\ \Omega$ m lies at 20 m depth under a
$40\ \Omega$ m sand. Compute the conductance (thickness/resistivity) of the layer
and of the 20 m of sand above it, and use the ratio to argue whether the layer is
detectable by a surface Wenner survey. Then propose a measurement strategy that
could detect it, and one that definitely could not, with the arithmetic that
supports each claim.

**★★★8.** Five-per-cent noise on eight spacings gave errors of $+10.0\%$ in
$\rho_2$ and $-2.1\%$ in $h$. Specify a bootstrap uncertainty analysis (resampling
procedure, number of realisations, statistic reported) and predict, with reasoning
about the misfit curvature, how the ranges for $\rho_2$ and $h$ will compare with
each other and with the noise level. State the one thing the bootstrap will
*not* capture.
