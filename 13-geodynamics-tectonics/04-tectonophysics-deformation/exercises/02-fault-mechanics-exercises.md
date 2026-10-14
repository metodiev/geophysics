# Exercises — 13-04-02 Fault Mechanics, Coulomb Stress and Stress Transfer

Attempt these before reading the
[solutions](02-fault-mechanics-solutions.md). The lesson is
[02 Fault Mechanics, Coulomb Stress and Stress Transfer](../02-fault-mechanics.md).
All models and data in this module are **SYNTHETIC**.

Unless stated otherwise use $\mu = 0.75$, $\mu_e = 30\ \mathrm{GPa}$,
$\rho = 2800\ \mathrm{kg\,m^{-3}}$ and $g = 9.81\ \mathrm{m\,s^{-2}}$.

## ★ Foundational

**★1.** For $\sigma_1 = 150$ and $\sigma_3 = 50\ \mathrm{MPa}$ with zero pore
pressure, compute $\sigma_n$ and $\tau$ on planes whose **normals** lie at
$\theta = 20^\circ$, $30^\circ$ and $45^\circ$ from $\sigma_1$, and state which is
closest to failure for $\mu = 0.75$. Then compute the failure function at the
true optimum $\theta = 45^\circ+\phi/2$ and explain why it exceeds all three.

**★2.** Compute the friction angle for $\mu = 0.6$ and $\mu = 0.85$, and the
corresponding optimal angles $\theta_{\text{opt}}$.

**★3.** With $\lambda = 0.4$, $\rho = 2800\ \mathrm{kg\,m^{-3}}$ and
$\mu = 0.75$, compute the failure differential stress at $8\ \mathrm{km}$ depth
and state the units of every factor.

## ★★ Applied

**★★4.** A SYNTHETIC vertical strike-slip fault slipped $1\ \mathrm{m}$ to a
depth of $d = 10\ \mathrm{km}$ in a medium with $\mu_e = 30\ \mathrm{GPa}$.
Compute $\sigma_{xy}$ on the surface at $x = 0$, $5$, $20$ and $100\
\mathrm{km}$, and show that the last two follow the asymptotic form
$2\mu_e s d/(\pi x^{2})$ to better than $5\%$.

**★★5.** At $x = 20\ \mathrm{km}$, $z = 4\ \mathrm{km}$ compute $\Delta
\mathrm{CFS}$ for receiver strikes of $0^\circ$, $18.4^\circ$, $45^\circ$ and
$90^\circ$ from the main fault, and state which of them is promoted and which is
inhibited.

**★★6.** Show analytically that $\Delta\sigma_n$ on a vertical receiver plane is
$\sigma_{xy}\sin 2\phi$ and $\Delta\tau = \sigma_{xy}\cos 2\phi$, given that only
$\sigma_{xy}$ changes. Then explain why $\Delta\mathrm{CFS}(\phi)$ is unchanged
under $\phi \to \phi + 90^\circ$ except for its sign.

**★★7.** The demonstration reports that $82.8\%$ of the sampled
$(x, z)$ area has positive $\Delta\mathrm{CFS}$ on the parallel mechanism.
Predict the fraction for the whole half-space $z>0$, $-\infty<x<\infty$, arguing
from the zero crossing $z = \sqrt{x^{2}+d^{2}}$, and compare with the
grid value.

**★★8.** A fault is already $2\ \mathrm{MPa}$ from failure. Using the worked
example's $\Delta\mathrm{CFS} = 1.31\ \mathrm{MPa}$ on the most promoted strike,
state whether the calculation predicts failure and, in two sentences, what else
would be needed to turn it into a probability.

## ★★★ Research-oriented

**★★★9.** The parallel-fault result $\Delta\sigma_n = 0$ is a feature of
anti-plane strain. Write down the stress-change tensor for a full 3-D
strike-slip dislocation in the far field (you may use the static moment-tensor
representation and state the radiation pattern), identify which components add a
normal-stress term on a parallel vertical plane, and explain the sign of the
correction near the fault ends.

**★★★10.** Design a SYNTHETIC test of whether aftershocks of a modelled main
shock correlate with $\Delta\mathrm{CFS}$, specifying: the synthetic catalogue
generation, the noise model for event locations and mechanisms, the metric and
its null distribution, and the result that would falsify the correlation. A
specification that could not be executed is a failed answer.
