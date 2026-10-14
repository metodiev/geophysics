# Exercises — 02-01-03 Scaling Laws, Similarity and Dimensional Reasoning

Attempt these **closed-book** before opening the
[solutions](./03-scaling-laws-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Unless stated otherwise use $g = 9.81\ \mathrm{m\,s^{-2}}$ (nominal),
$\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ (nominal crustal thermal diffusivity),
$\rho_{\text{mantle}} = 3300\ \mathrm{kg\,m^{-3}}$ and
$\eta_{\text{mantle}} = 10^{21}$ Pa s (both nominal, order-of-magnitude anchors),
and take $1\ \mathrm{yr} = 3.1557\times10^{7}$ s.

---

## ★ Foundational

**★1.** Identify the dimensionless group and say what physical competition it
measures: (a) $\rho u L/\eta$; (b) $\kappa t/L^{2}$; (c) $uL/\kappa$;
(d) $\tau_{\text{relax}}/\tau_{\text{obs}}$; (e) the ratio of a root depth to a
topographic height in Airy isostasy.

---

**★2.** A pendulum has $l = 1$ m. (a) Compute $T_0 = 2\pi\sqrt{l/g}$.
(b) Compute the exact period at $\theta_0 = 30°$ by the series
$T = T_0(1+\theta_0^{2}/16 + 11\theta_0^{4}/3072)$ and state the error of the
small-angle form as a percentage. (c) At what angle does the small-angle error
reach 1%?

---

**★3.** Using $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$: (a) compute
$\sqrt{\kappa t}$ at $t = 1$ Ma and $t = 10$ Ma, in km; (b) compute the time for
the diffusive length to reach 50 km; (c) by what factor must $t$ increase for the
diffusive length to double?

---

**★4.** Compute $\mathrm{Re} = \rho u L/\eta$ for (a) mantle convection with
$u = 1\ \mathrm{cm\,yr^{-1}}$, $L = 10^{6}$ m; (b) an ocean current with
$\rho = 1025\ \mathrm{kg\,m^{-3}}$, $u = 0.1\ \mathrm{m\,s^{-1}}$,
$L = 100$ m, $\eta = 10^{-3}$ Pa s. State the ratio of the two.

---

## ★★ Applied

**★★5.** Evaluate the Rayleigh number
$\mathrm{Ra} = \rho g\alpha\Delta T L^{3}/(\kappa\eta)$ with
$\alpha = 3\times10^{-5}\ \mathrm{K^{-1}}$ and $\Delta T = 3000$ K **assumed**,
$L = 2.89\times10^{6}$ m. (a) Compute $\mathrm{Ra}$. (b) Recompute for
$\eta = 10^{19}, 10^{20}, 10^{22}$ Pa s. (c) State which digits of the answer are
defensible and why.

---

**★★6.** Airy isostasy gives a root $r = \rho_c h/(\rho_m-\rho_c)$.
(a) Compute the coefficient for $\rho_c = 2700$, $\rho_m = 3300\
\mathrm{kg\,m^{-3}}$, and the root for a 3 km plateau. (b) If the density
contrast is $600 \pm 50\ \mathrm{kg\,m^{-3}}$, what is the uncertainty in the
root? (c) State the two assumptions that make the linear law fail.

---

**★★7.** A laboratory tank has $L = 0.3$ m and holds water at
$\rho = 1000\ \mathrm{kg\,m^{-3}}$. (a) With $u = 0.1\ \mathrm{m\,s^{-1}}$,
compute its Reynolds number. (b) To match the mantle's
$\mathrm{Re} = 1.046\times10^{-21}$ by changing the **fluid only**, what dynamic
viscosity would be required? (c) Alternatively, holding $\eta = 10^{-3}$ Pa s,
what flow speed would be required? (d) Comment on whether either is realisable.

---

**★★8.** A structure is modelled at 1:100 scale. (a) By what factor do weight,
load-bearing area and stress scale? (b) If the model's rock is the same
material as the prototype's, by what factor does the safety margin change?
(c) Give one geophysical situation where gravity-driven scaling compensates,
and say what is adjusted.

---

## ★★★ Research-oriented

**★★★9.** For a sphere of radius $a$ and density contrast $\Delta\rho$ sinking
slowly in a fluid of viscosity $\eta$, the variables are
$(v, \Delta\rho, g, a, \eta)$.

(a) Write the four dimension vectors in $(M,L,T)$ and compute the rank of the
exponent matrix.
(b) How many independent π groups are there? Produce them.
(c) Show that the group usually written $v\eta/(\Delta\rho g a^{2})$ is a
combination of yours.
(d) Stokes' law says $v\eta/(\Delta\rho g a^{2}) = 2/9$ — a *constant*. What does
that imply about the second group, and what is the regime of validity of that
statement?

---

**★★★10.** A centrifuge is proposed to model a buoyancy-driven instability at
1:1000 geometric scale.

(a) Write the Rayleigh number in terms of a buoyancy stress. If the model has
the same $\rho$, $\alpha$, $\Delta T$, $\kappa$ and $\eta$ as the prototype, by
what factor must $g$ be increased to match $\mathrm{Ra}$?
(b) Express the required rotation rate ratio if $g_{\text{eff}} = \omega^{2}R$
and the two radii are in a stated ratio of your choosing.
(c) State two other similarity conditions that must hold simultaneously, and
explain which is most likely to fail in practice.
