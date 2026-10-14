# Exercises — 11-02-02 Magnetics for IOCG, Porphyry and Magmatic Sulphides

Attempt these before reading the
[solutions](./02-magnetics-for-minerals-solutions.md). The lesson is
[02 Magnetics for Minerals](../02-magnetics-for-minerals.md). All properties,
directions, geometries and noise levels are **SYNTHETIC** teaching values.

Useful: $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$,
$\mu_0/4\pi = 10^{-7}$, $1\ \mathrm{nT} = 10^{-9}$ T,
$H_0 = B_0/\mu_0$.

## ★ Foundational

**★1.** A sphere of radius $100\ \mathrm{m}$ has $\kappa = 0.05$ SI in a field of
$52\ \mathrm{\mu T}$ and is centred at $z = 400\ \mathrm{m}$. Compute $H_0$, the
induced magnetisation (without and with self-demagnetisation), the dipole moment
and the axial magnetic anomaly in nT.

**★2.** For the same body, $Q = 3$ with the remanence at $-50°$ inclination while
the field is at $55°$. Compute the total dipole moment vector and its inclination.

**★3.** Write down the vertical-component anomaly $Z(x)$ of a vertically magnetised
dipole and state the value of $x/h$ at which $Z = 0$.

**★4.** A sphere has $\kappa = 2$ SI. Compute the factor by which the linear
formula $M = \kappa H_0$ over-predicts the magnetisation, and state the limiting
magnetisation as $\kappa\to\infty$.

## ★★ Applied

**★★5.** A profile over a SYNTHETIC body has a positive peak of $+820\ \mathrm{nT}$
and a trough of $-1450\ \mathrm{nT}$ with the peak displaced $180\ \mathrm{m}$
from the interpreted centre. Estimate the peak/trough ratio and state whether the
body is induced-dominated, remanence-dominated or mixed, using the lesson's values
($5.53$, $0.80$, $0.188$).

**★★6.** For a vertically magnetised dipole at $250\ \mathrm{m}$ depth, compute
the half-width of the RTP profile from the equation
$(2-u)/(1+u)^{5/2} = 1$ and hence the depth implied by a measured half-width of
$130\ \mathrm{m}$. State the sign of the error if the profile were actually
bipolar.

**★★7.** A body of radius $200\ \mathrm{m}$ at $z = 320\ \mathrm{m}$ gives an RTP
peak of $2500\ \mathrm{nT}$. Using the scale invariance of the dipole field,
compute the depth that a body of radius $400\ \mathrm{m}$ would require to give the
same peak, and the radius that a body at $z = 160\ \mathrm{m}$ would require.

**★★8.** For the lesson's SYNTHETIC body ($R = 200\ \mathrm{m}$, $z = 300\
\mathrm{m}$, $\kappa = 0.20$, $Q = 1.5$), compute the expected anomaly amplitude
at $x = 0$ (a) with the induced magnetisation only, (b) with the total
magnetisation. State the ratio and comment on which is the "correct" prediction
for a survey specification.

## ★★★ Research-oriented

**★★★9.** Design a procedure to solve for the total magnetisation direction as a
free parameter of a dipole fit, using only total-field data. State the penalty
function, the number of parameters, the identifiability problem you expect (which
parameter combinations are nearly degenerate), and the diagnostic you would use to
detect that degeneracy. Support your answer with a numerical experiment on the
lesson's SYNTHETIC body: vary the assumed direction over a grid and plot/print the
misfit, and report how flat the minimum is.

**★★★10.** A draped survey flies $60\ \mathrm{m}$ above ground over terrain that
varies by $80\ \mathrm{m}$ within one anomaly. Quantify the depth error this
introduces for a half-width depth rule, given that the rule assumes a constant
sensor height, and state whether the error is random or systematic with respect to
slope direction.

**★★★11.** Self-demagnetisation is exact only for an ellipsoid. Construct a
numerical experiment on a magnetised sphere (voxel sum) that measures the
*internal* field, and compare it with $H_0 - NM$; report the discrepancy and
explain why an irregular body has no single $N$.
