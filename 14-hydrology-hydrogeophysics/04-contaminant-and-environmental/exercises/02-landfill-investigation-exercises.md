# Exercises — 14-04-02 Landfill Investigation and Leachate Mapping

Attempt before the [solutions](./02-landfill-investigation-solutions.md). Lesson:
[02 Landfill Investigation and Leachate Mapping](../02-landfill-investigation.md).
All models **SYNTHETIC**; the landfill and leachate are idealised archetypes.

Use the two-layer Wenner relation
$\rho_a = \rho_1[1 + 4a\sum_{n\ge1}k^n(1/\sqrt{a^2+4n^2h^2} - 1/\sqrt{4a^2+4n^2h^2})]$
with $k = (\rho_2-\rho_1)/(\rho_2+\rho_1)$, and
$\sigma_w = 0.050 + 1.0\times10^{-4}C$ with $C$ in CU, $\phi = 0.30$, $a = 1$,
$m = 2$.

## ★ Foundational

**★1.** A synthetic site has $w = 1.0\times10^{-3}\ \mathrm{m\,day^{-1}}$,
$b = 75\ \mathrm{m}$, $T = 15\ \mathrm{m^{2}\,day^{-1}}$. Compute the steady
Dupuit mound rise and state the four assumptions behind the formula.

**★2.** For $\rho_1 = 50$, $\rho_2 = 500\ \Omega\,\mathrm{m}$ and
$h = 10\ \mathrm{m}$, compute $\rho_a$ at $a = 1$, $10$ and $100\
\mathrm{m}$. State which electrode configuration dominates each value.

**★3.** Compute the bulk resistivity of clean pore water and of
leachate-affected water at $C = 400$ CU.

## ★★ Applied

**★★4.** Verify the two analytic limits of the Wenner series for
$\rho_1 = 50$, $\rho_2 = 500\ \Omega\,\mathrm{m}$, $h = 10\ \mathrm{m}$ at
$a = 10^{-3}$ and $10^{5}\ \mathrm{m}$. Explain why a forward model must be
tested this way before it is used in an inversion.

**★★5.** A sounding over a synthetic landfill returns a conductive layer of
$60\ \Omega\,\mathrm{m}$ and $8\ \mathrm{m}$ thick over a
$400\ \Omega\,\mathrm{m}$ half-space. **(a)** At which $a/h$ does a $10\%$
thickness error produce the largest fractional change in $\rho_a$?
**(b)** Explain why a spacing of $a/h = 0.1$ is useless for mapping the layer
thickness.

**★★6.** The survey has a $5\%$ repeatability. Using the lesson's admitted-set
result ($\rho_1$ pinned to the grid value, $h \in [7.5, 9.0]\ \mathrm{m}$),
state whether the following interpretations are supported: (i) "a conductive
layer $8\ \mathrm{m}$ thick"; (ii) "a conductive layer exactly
$12\ \mathrm{m}$ thick"; (iii) "a conductive layer thinner than $6\ \mathrm{m}$".
Justify each in one sentence.

## ★★★ Research-oriented

**★★★7.** A conductive anomaly lies at a depth where a two-layer inversion
returns $h = 8\ \mathrm{m}$. Design the programme that tests whether a third
layer is present. **(a)** State the forward model you would fit and why the
two-layer fit is a trap. **(b)** Specify the spacings that would discriminate and
the plot you would use. **(c)** State the null hypothesis and the quantitative
criterion for rejecting it.

**★★★8.** The self-potential model of the lesson is
$V(x) = \rho I/(2\pi\sqrt{x^2+d^2})$ for a compact source at depth $d$.
**(a)** Show that $\rho$ and $I$ are not separable from $V$ alone. **(b)** Show
how a co-located resistivity measurement breaks the degeneracy, and state the
remaining assumption. **(c)** Compute the half-width of the anomaly in terms of
$d$ (the value of $x$ at which $V$ has fallen to half its peak), and state how
you would use it to depth-locate the source.
