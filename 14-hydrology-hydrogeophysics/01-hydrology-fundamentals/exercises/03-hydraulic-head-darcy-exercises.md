# Exercises — 14-01-03 Hydraulic Head, Darcy's Law and Groundwater Flow

Attempt these before reading the
[solutions](./03-hydraulic-head-darcy-solutions.md). The lesson is
[03 Hydraulic Head, Darcy's Law and Groundwater Flow](../03-hydraulic-head-darcy.md).
All wells, heads and conductivities are **SYNTHETIC**.

Constants: $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$g = 9.81\ \mathrm{m\,s^{-2}}$, $\mu_w = 1.002 \times 10^{-3}\ \mathrm{Pa\,s}$.

## ★ Foundational

**★1.** A piezometer is screened at $z = -15.0\ \mathrm{m}$ and reads
$p = 2.50 \times 10^{5}\ \mathrm{Pa}$. Compute the pressure head and the hydraulic
head. Then compute the head at $z = -8.0\ \mathrm{m}$ where $p = 0$ (a water
table), and explain in one sentence why the answer is not "the depth".

**★2.** Two piezometers 300 m apart read $h_1 = 50.00\ \mathrm{m}$ and
$h_2 = 49.25\ \mathrm{m}$ in a unit with $K = 8.0 \times 10^{-6}\
\mathrm{m\,s^{-1}}$ and $n_e = 0.15$. Compute the gradient, the specific
discharge in $\mathrm{m\,s^{-1}}$ and $\mathrm{m\,d^{-1}}$, the average linear
velocity, and the travel time over the 300 m.

**★3.** For $q = 1.0 \times 10^{-6}\ \mathrm{m\,s^{-1}}$ and
$d = 0.50\ \mathrm{mm}$, compute the grain-scale Reynolds number and state whether
Darcy's law is valid.

## ★★ Applied

**★★4.** A synthetic confined unit has $T = 100\ \mathrm{m^2\,d^{-1}}$ and
$S = 2.0 \times 10^{-4}$. Compute the hydraulic diffusivity and the time for a head
disturbance to reach 2 km. Repeat for an unconfined unit with the same $T$ and
$S_y = 0.15$, and state the ratio of the two times.

**★★5.** For a $L = 2000$ m strip with $K = 1.0 \times 10^{-4}\
\mathrm{m\,s^{-1}}$, $h_1 = h(L) = 15.0\ \mathrm{m}$ and uniform recharge
$R = 0.50\ \mathrm{mm\,d^{-1}}$, compute the exact Dupuit rise at mid-span and the
small-rise approximation, and report the percentage difference. State one
assumption of the Dupuit solution that the comparison does **not** test.

**★★6.** Flow crosses from a gravel ($K_1 = 1.0 \times 10^{-3}\
\mathrm{m\,s^{-1}}$) into a clay ($K_2 = 1.0 \times 10^{-6}\ \mathrm{m\,s^{-1}}$)
at $\theta_1 = 30^\circ$ from the normal. Compute $\theta_2$. Then reverse the
direction (clay to gravel) with $\theta_1 = 1^\circ$ and comment on the physical
consequence for recharge focusing.

## ★★★ Research-oriented

**★★★7.** The $R/K$ non-uniqueness of the lesson means that four different
$(K, R)$ pairs reproduce one water table exactly. Design a field programme for a
$L = 5\ \mathrm{km}$, $W = 2\ \mathrm{km}$ synthetic basin that separates $R$ from
$K$. Specify the measurements, the arithmetic that converts each measurement into
$R$ or $K$, and the precision required to distinguish 1 mm yr$^{-1}$ of recharge.
Include one systematic error per measurement and one cross-check that does not
share that error.

**★★★8.** The demonstration's finite-difference Dupuit solution agrees with the
analytic parabola to $6.4 \times 10^{-14}\ \mathrm{m}$. Explain precisely what
that agreement proves and what it does not. Then specify a **grid-convergence
test**: state the refinement sequence, the order of accuracy you expect for the
chosen discretisation of $u'' = -2R/K$, and what observed order would tell you
that the scheme is implemented correctly. Finally, name one analytic solution that
tests a Dupuit assumption the parabola test cannot, and say what it would check.
