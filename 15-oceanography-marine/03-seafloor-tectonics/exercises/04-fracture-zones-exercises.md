# Exercises — 15-03-04 Fracture Zones, Transform Faults and Oceanic Anomalies

Attempt these before the
[solutions](./04-fracture-zones-solutions.md). The lesson is
[04 Fracture Zones, Transform Faults and Oceanic Anomalies](../04-fracture-zones.md).
All models and data are **SYNTHETIC** teaching values; the model constants are
those printed by `code/fracture_zones_demo.py`.

## ★ Foundational

**★1.** For the model pole ($60\ ^\circ\mathrm{N}$, $30\ ^\circ\mathrm{W}$) and
$\omega=1.00\ ^\circ\mathrm{Myr^{-1}}$, compute $|v|$ at a point $45.0^\circ$
from the pole using $|v|=\omega R\sin\delta$ with $R=6371\ \mathrm{km}$, and give
the answer in both $\mathrm{km\,Myr^{-1}}$ and $\mathrm{mm\,yr^{-1}}$.

**★2.** With a ridge at $\phi_0=60^\circ$ and $\omega=1.00\
^\circ\mathrm{Myr^{-1}}$, compute the crustal age at $\phi=70^\circ$ from the
exact logarithmic relation and from the linear rule, and give the percentage
difference.

**★3.** A half-spreading rate is $30\ \mathrm{mm\,yr^{-1}}$. Express it in
$\mathrm{km\,Myr^{-1}}$ and compute the age offset across a $150\ \mathrm{km}$
ridge offset.

## ★★ Applied

**★★4.** Compute $\mu_0J/2\pi$ for $J=3.0\ \mathrm{A\,m^{-1}}$ and state the
anomaly amplitude in nT for a geometric factor of $0.4$. Then compute the peak
amplitude for $J=1.0\ \mathrm{A\,m^{-1}}$ and explain why a factor-of-two error in
$J$ is invisible in a spreading-rate inversion but fatal in an amplitude
inversion.

**★★5.** A magnetic profile runs from the ridge axis to $2224\ \mathrm{km}$
away, with the pole $60^\circ$ from the ridge and $\omega=1.00\
^\circ\mathrm{Myr^{-1}}$. Compute (a) the exact age at the far end, (b) the age
obtained by dividing the distance by the rate at the far end, (c) the age
obtained by the linear angular rule, and (d) the error of the linear rule in
per cent.

**★★6.** Compute the fracture-zone depth step for a $300\ \mathrm{km}$ ridge
offset at $40\ \mathrm{mm\,yr^{-1}}$ on crust of 5 Myr and of 30 Myr, using
$a=373.2\ \mathrm{m\,(Myr)^{-1/2}}$. State in one sentence why the step changes
with age.

## ★★★ Research-oriented

**★★★7.** A ridge-offset study must decide whether an observed $400\ \mathrm{m}$
depth step on 10 Myr crust is a $396\ \mathrm{km}$ ridge offset or a $42\
\mathrm{K}$ mantle temperature anomaly. Design the measurement programme: name
each observation, state what it measures and the precision required, give the
prediction of each hypothesis for each observation, and identify one quantity
that remains degenerate even after all your measurements.

**★★★8.** The lesson measures the skewness of a reversal-boundary response as an
antisymmetry metric falling from $0.9765$ at a profile azimuth of $90^\circ$ to
$0.5644$ at $30^\circ$, with the peak amplitude rising from $49.1$ to
$78.3\ \mathrm{nT}$. Specify a skew-correction procedure that uses only the
observed profile: state the model it assumes, the parameter it estimates, the
objective function it maximises, how a noise level enters, and the measurement
that would independently validate the correction. State what the correction
cannot fix.
