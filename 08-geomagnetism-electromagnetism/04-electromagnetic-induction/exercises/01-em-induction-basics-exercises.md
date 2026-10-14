# Exercises — 08-04-01 Induction, Skin Depth, Diffusion and Conductivity Structure

Attempt these before reading the
[solutions](./01-em-induction-basics-solutions.md). The lesson is
[01 Induction, Skin Depth and Diffusion](../01-em-induction-basics.md). All models
are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the skin depth for $\rho = 25\ \Omega$m at $T = 4$ s, using
$\delta = \sqrt{\rho T/(\pi\mu_0)}$ with $\mu_0 = 4\pi\times10^{-7}$ H m$^{-1}$.
Check the answer against the demonstration's table entry for
$\rho = 100\ \Omega$m at $T = 100$ s by scaling.

**★2.** State the units of $\omega\mu_0\sigma$ and show that $\delta$ has units of
length.

**★3.** At $2\delta$ depth, compute the fraction of the surface amplitude
remaining and the phase lag in radians and in degrees.

## ★★ Applied

**★★4.** The demonstration verifies the plane-wave solution with a Crank–Nicolson
solution that has $r = D\,\mathrm{d}t/(2\,\mathrm{d}z^{2}) = 9.82$. State what
$r$ is, what value an explicit scheme would require, and why this is not a
problem for Crank–Nicolson.

**★★5.** Compute the diffusion time $\tau = \mu_0\sigma L^{2}$ for $L = 200$ km
and $\sigma = 0.05$ S m$^{-1}$, and the period at which $\delta = L$.

**★★6.** Compute $z/\delta$ at the top and bottom of a 5 km thick sediment layer
with $\rho = 10\ \Omega$m in a field of period 100 s. State whether the layer is
thin or thick compared with the skin depth.

## ★★★ Research-oriented

**★★★7.** Compute $\omega\epsilon_0/\sigma$ for $\sigma = 0.01$ S m$^{-1}$ at
$T = 1$ s and at $T = 10^{-3}$ s, with $\epsilon_0 = 8.854\times10^{-12}$
F m$^{-1}$. State the period at which the ratio reaches $10^{-2}$, and what that
implies for the highest frequency at which the quasi-static approximation is
comfortable in such rock.

**★★★8.** Design the Crank–Nicolson verification for a two-layer structure and
state why the analytic comparison is no longer available. Say what you would
compare against instead, and what that tests.

**★★★9.** The demonstration measures a numerically determined amplitude of
0.04966 at $z/\delta = 3$ against an analytic 0.04979. State the relative error,
and give two plausible sources of it that are *not* errors in the physics.
