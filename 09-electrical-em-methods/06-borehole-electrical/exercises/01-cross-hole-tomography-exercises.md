# Exercises — 09-06-01 Cross-Hole and Borehole-to-Surface Tomography

Attempt these before reading the
[solutions](./01-cross-hole-tomography-solutions.md). The lesson is
[01 Cross-Hole and Borehole-to-Surface Tomography](../01-cross-hole-tomography.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A whole-space cross-hole quadrupole has
$A=(0,0,4)$, $B=(0,0,6)$, $M=(12,0,4)$, $N=(12,0,6)$ in metres, in a medium of
$\rho_0 = 50\ \Omega\,\mathrm{m}$. Compute the four distances, the bracket
$[1/r_{AM}-1/r_{BM}-1/r_{AN}+1/r_{BN}]$, the geometric factor $K$, the transfer
resistance $\Delta V/I$, and verify that $K(\Delta V/I)$ returns $\rho_0$.

**★2.** Write down the pole-pole sensitivity kernel and state its units. Compute
it at the midpoint between $A=(0,0,0)$ and $M=(10,0,0)$ in a medium of
$\sigma_0 = 0.05\ \mathrm{S\,m^{-1}}$, and say whether a conductivity *increase*
there raises or lowers the measured potential.

**★3.** The demonstration reports a resolution diagonal of 0.787 in the cells
beside the electrodes and 0.168 in the cells between the holes. State in one
sentence what those two numbers mean for a reported anomaly amplitude.

## ★★ Applied

**★★4.** Using the kernel
$J = -\mathbf{u}_A\cdot\mathbf{u}_M/(16\pi^{2}\sigma_0^{2}r_A^{2}r_M^{2})$,
evaluate $J$ for the point pair $A=(0,0,0)$, $M=(10,0,0)$ at the three points
$(5,0,0)$, $(5,3,0)$ and $(5,0,3)$, and explain the ordering of the three values
geometrically.

**★★5.** The demonstration's Jacobian has a condition number of
$3.0\times10^{3}$ and singular values ranging from $5.93\times10^{-4}$ to
$1.96\times10^{-7}\ \Omega$. Estimate the number of independent model numbers the
survey measures, and state two different reasons why that number is not the
number of cells.

**★★6.** A uniform perturbation of $\delta\sigma/\sigma_0 = 1\%$ is applied
everywhere. Using the normalisation identity, compute the change in
$\Delta V/I$ for the quadrupole of ★1 without re-deriving anything, and state
which piece of information about the kernel you needed.

## ★★★ Research-oriented

**★★★7.** The demonstration constructs an alternative model that fits the data
to within a factor 1.0014 of the inversion result and is $7.8\times$ further from
the truth. Design a survey (electrode depths, bipole lengths, number of
quadrupoles, borehole separation) that you expect to reduce that factor to 2,
and state the criterion by which you would decide that your design succeeded.
You may not use more than two boreholes, and you must report the singular
spectrum you expect.

**★★★8.** The kernel grows as $1/r^{2}$ towards a current electrode, so the
region within a few tenths of a metre of an electrode carries most of the
sensitivity and is usually outside the parameterisation. Design a study that
measures the model error this exclusion causes, and specify the statistic that
would reveal it. A specification that could not be executed is a failed answer.
