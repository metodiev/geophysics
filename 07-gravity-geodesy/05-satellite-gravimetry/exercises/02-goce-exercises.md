# Exercises — 07-05-02 GOCE, Gravity Gradients and the Static Field

Attempt these before reading the
[solutions](./02-goce-solutions.md). The lesson is
[02 GOCE, Gravity Gradients and the Static Field](../02-goce.md). **All models
and data in this module are SYNTHETIC**; altitudes, coefficients, spectra and
noise are teaching values.

Constants: $GM = 3.986004418\times10^{14}\ \mathrm{m^{3}\,s^{-2}}$,
$R = 6371\ \mathrm{km}$ (rounded), $1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$.

## ★ Foundational

**★1.** Compute the monopole gradient tensor at $h = 300\ \mathrm{km}$ in the
local orbital frame. Give $\Gamma_{rr}$ and the two tangential components in both
$\mathrm{s^{-2}}$ and E, and check the trace by hand.

**★2.** Show by direct differentiation of the point-mass potential
$\phi = -Gm/|\mathbf{r}-\mathbf{r}_m|$ that its Hessian has zero trace. State
where you use the fact that the mass is not at the evaluation point.

**★3.** For the synthetic zonal field of the demonstration
($C_{20} = 1.0\times10^{-4}$ at $250\ \mathrm{km}$, co-latitude $40^\circ$), the
numerical Hessian is

$$\begin{pmatrix} +8.5566 & 0 & +5.2020\\ 0 & -3.6890 & 0\\
+5.2020 & 0 & -4.8676\end{pmatrix}\times10^{-10}\ \mathrm{s^{-2}} .$$

Convert the largest component to E, compute the trace, and state what the
off-diagonal $G_{xz}$ tells you about the geometry.

## ★★ Applied

**★★4.** Derive the transfer function $T(l)$ from the radial degree scaling and
find its peak degree for $h = 400\ \mathrm{km}$, both exactly (solving
$1/(l+1)+1/(l+2) = \ln(a/R)$) and with the crude $2/\ln(a/R)$. State which is
high and by how much.

**★★5.** Using the lesson's synthetic surface radial-gradient spectrum
$A_s(l) = 1.0\times10^{-10}(2/l)^{1.5}\ \mathrm{s^{-2}}$ and a per-component
noise of $0.10\ \mathrm{E}$, find the highest degree with S/N $> 1$ at
$h = 350\ \mathrm{km}$ and give the corresponding half-wavelength $\pi R/l$.
Compare with the $250\ \mathrm{km}$ value of $167$ and state the physical reason
for the difference in one sentence.

**★★6.** A gradient solution is quoted to degree $200$. Using
$a/R = 1.03924$ and the transfer function with a *fixed* surface amplitude,
compute $T(50)$ and $T(200)$ and state by what factor degree $200$ is attenuated
relative to the peak. Then explain why a quoted high degree is not evidence of
information at that degree.

## ★★★ Research-oriented

**★★★7.** Design a numerical experiment that separates the effect of **altitude**
from the effect of **instrument noise** on the usable degree of a gradient
mission. Specify the grid of altitudes and noise levels, the metric that decides
"usable", and the prediction you would test. Then answer: what does a *single*
mission at one altitude and one noise level leave undetermined?

**★★★8.** The trace check detects a calibration error but does not diagnose its
cause. Propose a measurement or analysis that *would* separate an instrument
scale error from a mis-modelled non-gravitational acceleration, and state the
observation that distinguishes them. Your answer must be executable in principle
with mission data, not merely a wish.
