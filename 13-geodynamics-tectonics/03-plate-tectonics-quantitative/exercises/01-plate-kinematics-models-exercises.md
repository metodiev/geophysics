# Exercises — 13-03-01 Plate Kinematic Models and Euler Pole Inversion

Attempt these before reading the
[solutions](01-plate-kinematics-models-solutions.md). The lesson is
[01 Plate Kinematic Models and Euler Pole Inversion](../01-plate-kinematics-models.md).
All models and data in this module are **SYNTHETIC**.

## ★ Foundational

**★1.** A SYNTHETIC Euler vector is
$\omega = (0.006,\, -0.003,\, 0.008)\ \mathrm{rad\,Myr^{-1}}$. Compute
$|\omega|$ in $\mathrm{rad\,Myr^{-1}}$ and in
$\mathrm{deg\,Myr^{-1}}$, and state the latitude and longitude of the pole.

**★2.** A site sits at $(0^\circ, 0^\circ)$ on a SYNTHETIC plate with the Euler
vector of ★1. Compute $r$ for $R = 6371\ \mathrm{km}$, evaluate
$v = \omega \times r$, and resolve it onto east and north. State each answer in
$\mathrm{mm\,yr^{-1}}$.

**★3.** Using the site of ★2, write down the $3\times3$ matrix
$[n]_\times$ for its unit vector and verify that
$-R[n]_\times \omega$ reproduces the velocity you computed.

## ★★ Applied

**★★4.** The demonstration's one-cap network gives a pole latitude error of
$3.599^\circ$ at $445\ \mathrm{km}$ aperture, and its two-cap network gives
$0.218^\circ$ at $70^\circ$ separation. The velocity noise is the same. Estimate
the aperture ratio implied by the $1/L$ scaling and compare with the geometric
ratio of the two network spans. Is the agreement acceptable?

**★★5.** Reproduce the aperture argument from scratch for a network of aperture
$L$ and $N$ sites: show that the standard error of the angular rate estimated
from the velocity difference across the network scales as
$\sigma/(L\sqrt{N})$, taking care to state what is being averaged. Explain why
the demonstration's measured error at fixed $N$ falls as $1/L$ rather than
$1/(L\sqrt{N})$.

**★★6.** The demonstration reports a formal $\sigma$ of $3.475^\circ$ for the
one-cap network and a realised rms error of $3.599^\circ$ over 200 realisations.
Show that the ratio is consistent with a $\chi$ distribution with 200
independent samples and state the expected standard deviation of the realised
rms around the formal value.

**★★7.** A closure test gives
$\lVert \mathcal R_{AB}\mathcal R_{BC}\mathcal R_{CA} - \mathcal I\rVert =
3\times10^{-8}$. Is this a physical signal or a numerical error? Support the
answer with the demonstration's measured closure misfits.

## ★★★ Research-oriented

**★★★8.** Design a SYNTHETIC experiment that separates two effects on the
recovered pole: (i) the aperture of the network, and (ii) the number of sites
inside a fixed aperture. State the metric, the realisation count, the noise
model, and the expected outcome, including the scaling you predict for each
effect. A specification that could not be executed is a failed answer.

**★★★9.** The demonstration adds equal noise to every component. Real GNSS
velocity fields have spatially correlated noise, so that two stations 100 km
apart share a common error. Explain qualitatively how such a correlation changes
the formal uncertainty of the pole for (a) a global network and (b) a single
cluster, and propose a test on the residuals that would reveal the correlation.
