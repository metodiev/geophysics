# Exercises — 16-03-03 Cyclones, Fronts and Severe Weather Dynamics

Attempt these before reading the
[solutions](./03-storms-and-fronts-solutions.md). The lesson is
[03 Cyclones, Fronts and Severe Weather Dynamics](../03-storms-and-fronts.md).
All models are **SYNTHETIC** teaching values. Use
$\Omega = 7.292115\times10^{-5}\ \mathrm{rad\,s^{-1}}$, $g = 9.81\
\mathrm{m\,s^{-2}}$, and the Eady relations
$\chi(\mu) = \coth\mu/\mu - 1/\mu^2$, $\mu_{\max} = 1.606$,
$\sigma_{\max} = 0.31 f U_s/(NH)$.

## ★ Foundational

**★1.** Compute $\chi(\mu)$ for $\mu = 1.0$ and $\mu = 2.5$ and state, with the
criterion, which is unstable. Give the reason each end of the band is stable.

**★2.** For $N = 10^{-2}\ \mathrm{s^{-1}}$, $H = 10$ km and $f = 1.03126\times
10^{-4}\ \mathrm{s^{-1}}$, compute the internal Rossby radius $NH/f$ and the
most unstable zonal wavelength $2\pi NH/(1.606 f)$. State units.

**★3.** A front has $|\nabla_h\theta| = 2\times10^{-5}\ \mathrm{K\,m^{-1}}$ and
is being sharpened at $D = 10^{-5}\ \mathrm{s^{-1}}$. Compute the doubling time
of the gradient and the gradient after 2.0 days.

## ★★ Applied

**★★4.** Derive $\sigma = (\mu f/(NH))U_s\sqrt{\chi-1/4}$ starting from
$\hat c = \tfrac12[1\pm\sqrt{1-4\chi}]$, and show that the maximum over $\mu$
gives $\sigma_{\max} = 0.31 f \mathrm{Ri}^{-1/2}$ with
$\mathrm{Ri} = (NH/U_s)^2$.

**★★5.** A mean state has $N = 8\times10^{-3}\ \mathrm{s^{-1}}$, $H = 9$ km,
$U_s = 25\ \mathrm{m\,s^{-1}}$ at $55^\circ$. Compute $f$, the internal Rossby
radius, $\mathrm{Ri}$, $\lambda_{\max}$ and the e-folding time. Compare with the
lesson's reference case and explain the direction of each change.

**★★6.** A synthetic sounding gives CAPE $= 2152.6\ \mathrm{J\,kg^{-1}}$ at
$T_\text{surf} = 296$ K and $7894.6\ \mathrm{J\,kg^{-1}}$ at 308 K with the
environment held fixed.
**(a)** Compute $w_{\max}$ in both cases.
**(b)** State two reasons the real updraft is smaller.
**(c)** Explain in one sentence why holding the environment fixed makes the
sensitivity larger than it would be otherwise.

## ★★★ Research-oriented

**★★★7.** The frontogenesis experiment's measured growth rate falls behind
$\mathrm{e}^{Dt}$ after about four days. Design a convergence study that
separates numerical from physical saturation: state the grid spacings, the
diagnostic you would plot, the axes, and the result that would demonstrate
convergence to $D$. Then state what the same study would look like if the
saturation were physical.

**★★★8.** Building on Section 8, estimate the radius at which the cyclostrophic
approximation fails for a vortex with $v_{\max} = 60\ \mathrm{m\,s^{-1}}$ and a
1 km core radius at $35^\circ$, by finding where $fv$ becomes comparable to
$v^2/r$. State the assumptions in your estimate and whether the answer depends
on the core model.
