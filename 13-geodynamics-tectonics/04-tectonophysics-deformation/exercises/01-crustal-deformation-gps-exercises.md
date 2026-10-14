# Exercises — 13-04-01 Crustal Deformation from GNSS and Strain Rates

Attempt these before reading the
[solutions](01-crustal-deformation-gps-solutions.md). The lesson is
[01 Crustal Deformation from GNSS and Strain Rates](../01-crustal-deformation-gps.md).
All models and data in this module are **SYNTHETIC**.

Useful identity throughout: $1\ \mathrm{mm\,yr^{-1}\,km^{-1}} =
10^{3}\ \mathrm{nstrain\,yr^{-1}} = 10^{-6}\ \mathrm{yr^{-1}}$.

## ★ Foundational

**★1.** Convert $25\ \mathrm{nstrain\,yr^{-1}}$ into $\mathrm{yr^{-1}}$ and into
$\mathrm{mm\,yr^{-1}\,km^{-1}}$. Then state how much velocity difference
$25\ \mathrm{nstrain\,yr^{-1}}$ produces across $80\ \mathrm{km}$.

**★2.** A velocity-gradient tensor is
$L = \begin{pmatrix} 20 & -8 \\ 28 & -14\end{pmatrix}\times10^{-9}
\ \mathrm{yr^{-1}}$. Compute its symmetric part $E$, its antisymmetric part
$W$, the rotation rate $w$, and the dilatation rate $\mathrm{tr}\,E$.

**★3.** For the $E$ of ★2, compute the principal strain rates
$e_1, e_2$ (eigenvalues of a $2\times2$ symmetric matrix:
$\lambda = \frac{\mathrm{tr}}{2} \pm \sqrt{(\frac{\mathrm{tr}}{2})^{2} -
\det}$), and state the azimuth of $e_1$ measured clockwise from north.

## ★★ Applied

**★★4.** Using the lesson's SYNTHETIC network result — $E_{xx}$ recovered as
$29.941 \pm 3.080$ against a true $30.000\times10^{-9}\ \mathrm{yr^{-1}}$ —
compute the significance of the difference and state whether the residual
variance estimate is consistent with the input noise of
$0.5\ \mathrm{mm\,yr^{-1}}$.

**★★5.** A rigid rotation of $10\times10^{-9}\ \mathrm{yr^{-1}}$ is added to
every velocity of a network of aperture $140\ \mathrm{km}$. Compute the maximum
velocity change, state what happens to the recovered strain rate and to the
recovered rotation rate, and explain why an analyst cannot separate the added
rotation from a real one.

**★★6.** Using the measured aperture rule
$\delta e_1 \approx 386/L$ in units of $10^{-9}\ \mathrm{yr^{-1}}$ per km at
$0.5\ \mathrm{mm\,yr^{-1}}$ noise, compute the aperture needed to resolve
$e_1 = 20\times10^{-9}\ \mathrm{yr^{-1}}$ to $10\%$. Then repeat for
$1.0\ \mathrm{mm\,yr^{-1}}$ noise and state the scaling you used.

**★★7.** A network of 12 stations has one station whose residual is 20 times the
median of the rest. State two actions to take and estimate the effect of
removing it, given the demonstration's measurement that a $19.2\
\mathrm{mm\,yr^{-1}}$ blunder moved $e_1$ by $6\%$ with 24 stations.

## ★★★ Research-oriented

**★★★8.** Write out the design matrix for the six-parameter fit explicitly (two
reference velocities, four tensor components) for $N$ stations, and show that
the normal matrix $A^{\mathsf T}A$ is block-diagonal between the translation and
gradient blocks **only if** the station coordinates are centred on their mean.
Explain why that matters for interpreting the covariance.

**★★★9.** Design a SYNTHETIC experiment to determine how the strain-rate
uncertainty depends on (i) the aperture, (ii) the station count and (iii) the
spatial correlation length of the velocity errors. Specify the metric, the
noise model, the realisation count and the scaling you predict for each factor.
A specification that could not be executed is a failed answer.
