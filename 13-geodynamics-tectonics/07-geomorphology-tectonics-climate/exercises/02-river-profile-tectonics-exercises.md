# Exercises — 13-07-02 River Profiles, Steepness Indices and Uplift Inference

Attempt these before reading the
[solutions](./02-river-profile-tectonics-solutions.md). The lesson is
[02 River Profiles, Steepness Indices and Uplift Inference](../02-river-profile-tectonics.md)
and its numbers come from
[`code/river_profile_tectonics_demo.py`](../code/river_profile_tectonics_demo.py).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Derive $S = k_sA^{-\theta}$ from
$\mathrm{d}z/\mathrm{d}t = U - KA^mS^n$, and state the dimensions of $K$ and $k_s$
for $m = 0.5$, $n = 1$ in SI units.

**★2.** For $k_s = 20$ m and $\theta = 0.5$, compute the slope $S$ at
$A = 4\times10^{5}$ m² and $A = 10^{6}$ m².

**★3.** State what $\theta = m/n$ represents physically and why it is better
constrained by a profile than $k_s$.

## ★★ Applied

**★★4.** Perform a $\chi$ transform with $\theta = 0.5$ for the two-segment
drainage area $A = 10^{5}$ m² for $x<50$ km and $A = 10^{6}$ m² for $x\ge50$ km
over a total length of 100 km, and state the $\chi$ value at the divide.

**★★5.** Using the $\chi$ from ★4 and a steady profile with $k_s = 10$ m, compute
the elevation at the outlet, the divide and the point $x = 50$ km.

**★★6.** Two basins have $k_s = 40$ m and $k_s = 20$ m at the same $\theta = 0.5$
with $n = 1$. Compute the ratio of $U/K$ and state what cannot be concluded from
it.

**★★7.** A knickpoint travels 60 km upstream in 6 Myr. Compute its speed in mm/yr
and, with $m = 0.5$ and $A_0 = 10^{6}$ m², the implied erodibility $K$ with its
units.

## ★★★ Research-oriented

**★★★8.** Using the lesson's bias table for a wrong concavity, estimate the bias
in $U$ if $\theta$ is taken as 0.55 when the true value is 0.50, and state whether
the sign of the bias is predictable in advance.

**★★★9.** Design a study that would measure $K$ rather than $U/K$. State the
observable, the time resolution of the knickpoint constraint, and the assumption
that would still have to be made.

**★★★10.** A landscape has a uniform $k_s$ but a spatially varying precipitation
rate. Explain how the resulting variability in $K$ could be mistaken for a
tectonic signal, and design the test that would distinguish them.
