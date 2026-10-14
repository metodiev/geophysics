# Exercises — 10-05-04 Nuclear and Radiometric Near-Surface Methods

Attempt these before reading the
[solutions](./04-nuclear-and-radiometric-nearsurface-solutions.md). The lesson is
[04 Nuclear and Radiometric Methods](../04-nuclear-and-radiometric-nearsurface.md).
All models are **SYNTHETIC** teaching values; reference numbers come from
`code/nuclear_radiometric_demo.py`. Use $k = 1.6449$ for one-sided 95% confidence
and $\gamma = 0.5772$.

## ★ Foundational

**★1.** A detector window records $900$ counts in $60\ \mathrm{s}$. Compute the
count rate, its one-sigma uncertainty in counts and in $\mathrm{s^{-1}}$, and the
relative precision of the measurement.

**★2.** A source gives $12\ \mathrm{s^{-1}}$. How long must it be counted to reach
1% relative precision? State the general relation you used.

**★3.** State the SI units of activity, count rate, the mass attenuation
coefficient and the linear attenuation coefficient, and verify that $\mu z$ is
dimensionless.

## ★★ Applied

**★★4.** A uranium window has a background of $2500$ counts per $60\ \mathrm{s}$
measurement. Compute the critical level $L_C$ and the detection limit $L_D$, and
express $L_D$ as a count rate. Explain in one sentence the difference between the
two quantities.

**★★5.** For the teaching soil ($\mu/\rho = 0.0055\ \mathrm{m^{2}\,kg^{-1}}$,
$\rho = 1600\ \mathrm{kg\,m^{-3}}$), compute the depth above which 75% of the
gamma-ray signal originates, and compare it with the mean depth of origin
$1/(2\mu)$. Explain why the two answers differ.

**★★6.** A station records $1760$ counts in $60\ \mathrm{s}$ against a background
of $1600$. Decide whether this is a detection at 95% confidence, compute the
one-sigma uncertainty of the net count, and state how much longer the count would
have to be to halve the detectable rate.

## ★★★ Research-oriented

**★★★7.** A stripping factor used in a K/U/Th analysis is wrong by 10%. Using the
inverse-matrix relation $\delta\mathbf a = A^{-1}\delta\mathbf c$, predict the
error this introduces in each activity when the true ground has equal activities,
and state the field measurement that would detect the mistake. A specification
that could not be executed is a failed answer.

**★★★8.** Design a natural-gamma survey that must map soil type to a stated
precision. Specify the station spacing, the counting time per station, the
detection limit you will claim, the calibration procedure, and the falsification
test that would show the map is measuring instrument drift rather than soil.
