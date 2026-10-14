# Solutions — 08-04-01 Induction, Skin Depth, Diffusion and Conductivity Structure

> **Read after attempting the exercises.** The lesson is
> [01 Induction, Skin Depth and Diffusion](../01-em-induction-basics.md).

---

## ★1 — Skin depth

$$\pi\mu_0 = \pi\times4\pi\times10^{-7} = 3.9478\times10^{-6},$$
$$\delta = \sqrt{\frac{\rho T}{\pi\mu_0}} = \sqrt{\frac{25\times4}{3.9478\times10^{-6}}}
= \sqrt{2.5330\times10^{7}} = 5033\ \mathrm{m} = 5.033\ \mathrm{km}.$$

**Scaling check.** The demonstration gives $\delta = 50.329$ km for
$\rho = 100\ \Omega$m and $T = 100$ s. The product $\rho T$ here is $100$ against
$10^{4}$ there, a ratio of $100$, so the skin depths should differ by
$\sqrt{100} = 10$: $50.329/10 = 5.033$ km. ✔ (The scaling works because
$\delta\propto\sqrt{\rho T}$ involves no other dimensional quantity.)

---

## ★2 — Units

$\omega\mu_0\sigma$ has units
$\left(\mathrm{s^{-1}}\right)\left(\mathrm{H\,m^{-1}}\right)\left(\mathrm{S\,m^{-1}}\right)
= \left(\mathrm{s^{-1}}\right)\left(\mathrm{H\,m^{-1}}\right)
\left(\mathrm{A\,V^{-1}\,m^{-1}}\right) = \mathrm{m^{-2}}$,
since $\mathrm{H} = \mathrm{V\,s\,A^{-1}}$. Its reciprocal has units
$\mathrm{m^{2}}$, and the square root is a length. ✔

---

## ★3 — At two skin depths

$$\text{amplitude} = e^{-2} = 0.13534 \quad (13.5\%), \qquad
\text{phase lag} = 2\ \mathrm{rad} = 2\times\frac{180}{\pi} = 114.6^\circ .$$

Eleven per cent of the surface amplitude at a depth where the phase has already
turned past a right angle: the two are locked together by the diffusion equation,
which is why in a 1-D Earth amplitude and phase are not independent measurements.

---

## ★4 — The Crank–Nicolson parameter

$r = D\,\mathrm{d}t/\left(2\,\mathrm{d}z^{2}\right)$ is the dimensionless ratio of
the diffusion length in one time step to the grid spacing. An **explicit**
finite-difference scheme requires $r \le \frac12$ for stability, which for
$\rho = 100\ \Omega$m and a grid fine enough to resolve $\delta$ would demand time
steps of microseconds and millions of iterations per period. **Crank–Nicolson is
unconditionally stable**: it averages the diffusion operator between the present
and future times, giving an implicit tridiagonal system whose solution is stable
for any $r$. That is why it is the standard choice for diffusion problems — the
stability is bought with a linear solve per step rather than with a small step.

---

## ★5 — Diffusion time

$$\tau = \mu_0\sigma L^{2} = 1.2566\times10^{-6}\times0.05\times\left(2.0\times10^{5}\right)^{2}
= 1.2566\times10^{-6}\times0.05\times4.0\times10^{10} = 2.513\times10^{3}\ \mathrm{s},$$
$$T_{\delta = L} = \pi\mu_0\sigma L^{2} = \pi\times2.513\times10^{3}
= 7.895\times10^{3}\ \mathrm{s} \approx 2.2\ \mathrm{hours}.$$

Interval-consistency: $7.9\times10^{3}$ s is also what one gets from
$\delta = L$ directly at $\sigma = 0.05$ S m$^{-1}$ and $L = 200$ km, since
$T = \pi\mu_0\sigma L^{2}$ *is* the definition of that condition.

---

## ★6 — Layer thickness against skin depth

$$\delta = \sqrt{\frac{\rho T}{\pi\mu_0}} = \sqrt{\frac{10\times100}{3.9478\times10^{-6}}}
= \sqrt{2.533\times10^{8}} = 15.92\ \mathrm{km}.$$

The 5 km layer spans $z/\delta$ from 0 to $5/15.92 = 0.314$: the *entire layer* lies
within a third of a skin depth, so the field hardly attenuates within it. The
layer is **thin against the skin depth**, and the response will depend on its
conductance rather than on its thickness — the equivalence demonstrated in
[05 MT Interpretation](../05-mt-interpretation.md).

---

## ★★7 — The displacement-current ratio

$$\frac{\omega\epsilon_0}{\sigma} = \frac{2\pi\epsilon_0}{\sigma T}
= \frac{2\pi\times8.854\times10^{-12}}{0.01\times T}
= \frac{5.563\times10^{-9}}{T} .$$

| $T$ | ratio |
|---|---|
| 1 s | $5.6\times10^{-9}$ |
| $10^{-3}$ s | $5.6\times10^{-6}$ |

The ratio reaches $10^{-2}$ at $T = 5.6\times10^{-7}$ s, i.e. a frequency of
about 1.8 MHz. So for resistivities of $100\ \Omega$m and frequencies up to
hundreds of kilohertz the quasi-static approximation is safe by at least three
orders of magnitude; the approximation fails only in very resistive media (ice,
dry rock) at radio frequencies — which is exactly where ground-penetrating radar
operates.

---

## ★★8 — Verification for a two-layer structure (specification)

**Why the analytic comparison is unavailable.** The plane-wave solution
$e^{-z/\delta}\cos(\omega t - z/\delta)$ is the solution for a **uniform**
half-space; with an interface there is a reflected wave and the field is a sum of
two exponentials whose ratio is set by the impedance matching condition. The
simple closed form does not exist.

**What to compare against.** The frequency-domain **layered recursion** of
[02 Magnetotellurics](../02-magnetotellurics.md), which is an independent route
(steady-state complex impedance) to the same transfer function, or the analytic
two-layer Sommerfeld solution expressed through the reflection coefficient at the
interface.

**What it tests.** Time-domain PDE solutions and frequency-domain impedance
recursions fail differently: the first in transient removal, boundary reflections
and time-stepping, the second in the arithmetic of $\tanh$ of complex arguments
and the recursion order. Agreement between them is evidence that both are right,
and the *phase* agreement is the more sensitive test because it is unaffected by
any amplitude scaling error.

---

## ★★9 — The residual at three skin depths

$$\frac{\left|0.04966 - 0.04979\right|}{0.04979} = 2.6\times10^{-3} = 0.26\% .$$

Two plausible sources that are not physics:

1. **Truncation of the domain.** The domain is $6\delta$ with an artificial
   $B=0$ boundary; the field at the far boundary is $e^{-6} = 2.5\times10^{-3}$ of
   the surface value, not zero, so the reflected residual contaminates the solution
   at the per-mille level. Extending the domain or using an absorbing (impedance)
   boundary reduces it.
2. **The complex demodulation window.** The steady-state amplitude is extracted by
   summing over exactly one period; the transient is not perfectly removed after
   five periods (it decays but does not vanish), and the finite window does not
   reject the residual. Averaging over more periods, after discarding more
   transients, reduces this term.

A third, smaller, source is the spatial truncation error of the second-order
difference stencil.
