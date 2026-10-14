# Exercises — 06-12-01 Causes of Induced Seismicity: Injection, Extraction, Reservoirs

Attempt these before reading the
[solutions](./01-induced-seismicity-causes-solutions.md). The lesson is
[01 Causes of Induced Seismicity](../01-induced-seismicity-causes.md); all numbers
are printed by
[`../code/coulomb_sign_flip_demo.py`](../code/coulomb_sign_flip_demo.py). All
models are **SYNTHETIC** teaching values; no real earthquake, well or field is
referred to.

## ★ Foundational

**★1.** State the dimensions of the Biot coefficient $\alpha$, the friction
coefficient $\mu_f$, the seismic moment $M_0$ and a Coulomb stress change
$\Delta CFS$, and show that $\mu_f\Delta p$ has stress dimensions.

**★2.** A fault has $\sigma_n = 40\ \mathrm{MPa}$ (compression positive),
$p = 15\ \mathrm{MPa}$ and $\mu_f = 0.6$. Compute
$CFS = \tau - \mu_f(\sigma_n - p)$ for $\tau = 12\ \mathrm{MPa}$ and state
whether the fault is closer to failure than one with $CFS = 0$.

**★3.** Compute $\alpha = 1 - K/K_s$ for $K = 20\ \mathrm{GPa}$,
$K_s = 40\ \mathrm{GPa}$, and again for $K = 4\ \mathrm{GPa}$,
$K_s = 40\ \mathrm{GPa}$. Say in one sentence why the second rock is more
sensitive to pore pressure.

## ★★ Applied

**★★4.** An injection raises $p$ by $3\ \mathrm{MPa}$ at a fault in a rock with
$K = 12\ \mathrm{GPa}$, $K_s = 45\ \mathrm{GPa}$, $\mu_f = 0.55$. Compute
$\Delta CFS$ using the pressure-only result, and compute the pressure change that
would produce $\Delta CFS = 0.1\ \mathrm{MPa}$. Comment on the size of the second
number relative to the first.

**★★5.** Using the demonstration's magnitude table, compute the peak
$\lvert\Delta\sigma\rvert$ at $5\ \mathrm{km}$ from an $M_w\,4.5$ source by scaling
the $r = 3\ \mathrm{km}$ value, and compare it with the pressure term for a
$0.5\ \mathrm{MPa}$ pressure change with $\mu_f = 0.6$. Which dominates, and by
what factor?

**★★6.** The demonstration measures sign-flip rates for a perturbed receiver plane
of $0.0694$ ($\pm5^\circ$), $0.1076$ ($\pm30^\circ$), $0.1736$ ($\pm45^\circ$) and
$0.2917$ ($\pm60^\circ$). Interpolate to find the perturbation angle at which
roughly a quarter of cases flip, and state why the flip rate is a property of the
source–receiver *pair*.

## ★★★ Research-oriented

**★★★7.** From the poroelastic constitutive law
$\sigma_{ij} = 2G\varepsilon_{ij} + \lambda\varepsilon_{kk}\delta_{ij} - \alpha
p\delta_{ij}$, derive the stress change produced by a spherical pressurised
inclusion of radius $a$ at distance $r \gg a$ in an infinite medium in the
undrained limit. Show that it decays as $1/r^3$, and state the undrained Poisson
ratio $\nu_u$ in terms of $\nu$, $\alpha$ and the Skempton coefficient $B$.

**★★★8.** The demonstration neglects the free surface, and it states that the
point-source approximation fails at $r$ of order the source dimension — for
$M_w\,5$ roughly $3\ \mathrm{km}$. Argue, using the $1/r^3$ decay and the method of
images, at what source-to-receiver distance a free surface at depth $z_s$ changes
the answer by more than 20%, and state which of the two limitations binds first for
a $M_w\,5$ source at $z_s = 5\ \mathrm{km}$.

**★★★9.** A colleague reports "the earthquake was induced: the Coulomb stress
change at the hypocentre was $+0.05\ \mathrm{MPa}$". Write the four questions you
must ask before accepting the claim, and state for each what the answer could do to
the sign or the magnitude of the result.
