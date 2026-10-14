# Solutions — 13-02-01 Rayleigh-Benard Convection Applied to the Mantle

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. $g = 9.81\ \mathrm{m\,s^{-2}}$ is standard;
> $Ra_c = 27\pi^{4}/4 = 657.5114$ is exact for free-slip boundaries.

Lesson:
[01 Rayleigh-Benard Convection](../01-rayleigh-benard-mantle.md).

---

## ★1 — Rayleigh number for the upper mantle

$$Ra = \frac{\rho_0 g\alpha\Delta T d^{3}}{\kappa\eta}
= \frac{(3300)(9.81)(3\times10^{-5})(1300)(7\times10^{5})^{3}}
{(10^{-6})(10^{21})} .$$

Numerator: $(3300)(9.81) = 3.2373\times10^{4}$;
$\times3\times10^{-5} = 0.97119$; $\times1300 = 1262.5$;
$(7\times10^{5})^{3} = 3.43\times10^{17}$;
$1262.5\times3.43\times10^{17} = 4.330\times10^{20}$.
Denominator: $10^{-6}\times10^{21} = 10^{15}$.

$$Ra = 4.330\times10^{5},$$

matching the lesson's tabulated $4.331\times10^{5}$ (rounding in the powers of
ten). The supercriticality is $Ra/Ra_c = 659$: convecting, not marginal.

---

## ★2 — Critical values

$$Ra_c = \frac{27\pi^{4}}{4} = \frac{27(97.4091)}{4}
= \frac{2629.045}{4} = 657.5114 .$$

$$k_c = \frac{\pi}{\sqrt{2}} = 2.2214,
\qquad
\lambda_c = \frac{2\pi}{k_c} = \frac{6.2832}{2.2214} = 2.8284\,d .$$

So the critical convection cell is $2.83$ times as wide as the layer is deep —
the classic aspect ratio of marginal Rayleigh–Bénard convection. For a 2900 km
mantle that is 8200 km, of the same order as the width of the Pacific.

---

## ★3 — Boundary-layer scalings at $Ra = 10^{6}$

$$\frac{\delta}{d} = \left(\frac{Ra_c}{Ra}\right)^{1/3}
= \left(\frac{657.5}{10^{6}}\right)^{1/3}
= (6.575\times10^{-4})^{1/3} = 0.08696,$$

$$Nu = \left(\frac{Ra}{Ra_c}\right)^{1/3}
= \left(1.521\times10^{3}\right)^{1/3} = 11.50 .$$

**Why only an order of magnitude.** The scaling fixes the *exponent* of the
$Ra$ dependence but leaves the prefactor as an undetermined $O(1)$ function of the
boundary conditions; the numerical model of
[13-02-02](../02-convection-numerical.md) measures that prefactor as 1.9 rather
than 1 for free-slip convection in a critical-wavelength box. In addition the
formula assumes bottom heating with two equal boundary layers, whereas a real
mantle has distributed internal heating.

---

## ★★4 — Deriving $k_c$ and $Ra_c$

With $a = \pi^{2}$ and $s = k^{2}$,

$$Ra(s) = \frac{(a+s)^{3}}{s} = a^{3}s^{-1} + 3a^{2} + 3as + s^{2},$$

$$\frac{\mathrm{d}Ra}{\mathrm{d}s} = -a^{3}s^{-2} + 3a + 2s = 0 .$$

Multiplying by $s^{2}$:

$$-a^{3} + 3as^{2} + 2s^{3} = 0 .$$

Substituting the claimed solution $s = a/2$:
$-a^{3} + 3a(a^{2}/4) + 2(a^{3}/8) = -a^{3} + 0.75a^{3} + 0.25a^{3} = 0$ ✔ — so
$s = a/2$ is a stationary point, and it is the global minimum because the cubic
$-a^{3} + 3as^{2} + 2s^{3}$ is increasing for $s>0$ (its derivative
$6as + 6s^{2} > 0$), so there is exactly one positive root.

Hence $k_c^{2} = \pi^{2}/2$ and

$$Ra_c = \frac{\left(\pi^{2} + \pi^{2}/2\right)^{3}}{\pi^{2}/2}
= \frac{\left(\tfrac{3}{2}\pi^{2}\right)^{3}}{\tfrac{1}{2}\pi^{2}}
= \frac{\tfrac{27}{8}\pi^{6}}{\tfrac{1}{2}\pi^{2}}
= \frac{27}{4}\pi^{4} = 657.5114 . \qquad\checkmark$$

---

## ★★5 — No-slip versus free-slip boundaries

$$\frac{Ra_c^{\text{rigid}}}{Ra_c^{\text{free}}}
= \frac{1707.8}{657.51} = 2.598,$$

and the critical wavelengths are $2.027\,d$ (measured) against $2.828\,d$: no-slip
cells are *narrower* by 28%.

Two physical consequences for mantle convection:

1. **A rigid lid raises the threshold and organises the flow at smaller
   horizontal scale.** More buoyancy is needed to initiate convection, and the
   planform acquires more, narrower upwellings — the pattern a code with a stiff
   surface finds, and the reason the choice of surface boundary condition changes
   the *style* of the solution even at fixed $Ra$.
2. **Heat transport is organised differently at the surface.** With a no-slip lid
   the surface is a conductive, immobile boundary layer; with free slip the
   surface participates in the horizontal flow. The Nusselt number and its
   prefactor therefore differ between the two cases; the exponents do not.

---

## ★★6 — Viscosity contrast and effective Rayleigh number

$$\Delta\ln\eta \approx \frac{E\,\Delta T}{R\,T_0^{2}}
= \frac{(3\times10^{5})(150)}{(8.314)(1550)^{2}}
= \frac{4.5\times10^{7}}{1.998\times10^{7}} = 2.252,$$

so the contrast is $e^{2.252} = 9.52$ — the cold edge of the boundary layer is
about ten times stiffer than the interior.

**Effect on the effective $Ra$:** the relevant viscosity for the boundary layer is
the stiff one, so $Ra_{\text{eff}} \approx Ra \times e^{-2.252} = 0.105\,Ra$ — a
tenfold reduction. That is not enough to stop convection, but it is enough to make
the surface layer conduct heat much less efficiently than a free-slip surface
would, which is the beginning of the stagnant-lid regime. A 350 kJ/mol activation
energy with a 200 K drop gives a factor of 27, and larger contrasts rapidly
suppress lid participation altogether.

---

## ★★★7 — The velocity scaling

**Derivation.** Inside the thermal boundary layer the buoyancy and viscous terms
of the momentum balance are comparable. Buoyancy force per unit volume is
$\rho_0 g\alpha\Delta T$; viscous force per unit volume is $\eta u/\delta^{2}$.
Equating:

$$u \sim \frac{\rho_0 g\alpha\Delta T\,\delta^{2}}{\eta} .$$

Substituting $Ra = \rho_0 g\alpha\Delta T d^{3}/(\kappa\eta)$, i.e.
$\rho_0 g\alpha\Delta T/\eta = Ra\,\kappa/d^{3}$:

$$u \sim \frac{\kappa}{d}\,Ra\left(\frac{\delta}{d}\right)^{2}
= \frac{\kappa}{d}\,Ra\left(\frac{Ra_c}{Ra}\right)^{2/3}
= \frac{\kappa}{d}\,Ra_c^{2/3}Ra^{1/3}
= \frac{\kappa}{d}\,Ra^{1/3}Ra_c^{2/3} .$$

**Evaluation** for the whole-mantle set ($\kappa/d = 3.448\times10^{-10}$
m s$^{-1}$, $Ra = 3.079\times10^{7}$, $\delta/d = 0.02774$):

$$\frac{\kappa}{d}Ra\left(\frac{\delta}{d}\right)^{2}
= (3.448\times10^{-10})(3.079\times10^{7})(7.695\times10^{-4})
= 8.17\times10^{-9}\ \mathrm{m\,s^{-1}},$$

$$u = 8.17\times10^{-9}\times3.1557\times10^{7}
= 0.258\ \mathrm{m\,yr^{-1}} .$$

**What the discrepancy says.** The measured $0.26\ \mathrm{m\,yr^{-1}}$ is 8.6
times the synthetic reference plate speed of $0.030\ \mathrm{m\,yr^{-1}}$. This
does *not* falsify the scaling: the derivation never determined the $O(1)$
coefficient, and the drag law used here (a single viscosity, a boundary layer
obeying a critical local Rayleigh number) is a caricature. What it *does* say is
that the velocity scale is $(\kappa/d)Ra^{1/3}Ra_c^{2/3}$ multiplied by an unknown
$O(10)$ — so the correct conclusion is "the mantle's convective velocity is set by
boundary-layer dynamics at the tens-of-centimetres-per-year level", with the
coefficient left to a numerical model or an independent viscosity constraint.
Deciding that the scaling is "wrong" and abandoning it would discard the
information that the exponent is right.

---

## ★★★8 — Distinguishing bottom from internal heating

**Configuration.** Two runs at the same $Ra$ in the same box, same boundary
conditions, same resolution and time step. (a) Bottom-heated: $T = 1$ at
$z = 0$, $T = 0$ at $z = 1$, no internal source. (b) Internally heated: zero flux
at both boundaries (or $T = 0$ at the top and zero flux at the bottom) with a
uniform source $H$ chosen so that the total heat flux through the top matches
case (a).

**Diagnostic.** The horizontally averaged temperature profile
$\langle T\rangle(z)$ and the *ratio* of the top to bottom boundary-layer
thicknesses, together with the Nusselt number.

**Expected signatures.** In case (a) the layer is symmetric: two boundary layers
of similar thickness, and $\langle T\rangle\approx 1/2$ in the interior. In case
(b) heat enters everywhere and leaves only through the top, so the bottom is
insulating and no bottom boundary layer forms:
$\langle T\rangle$ has a conductive $z^{2}$-like shape with the maximum at the
bottom, and the top boundary layer is thicker and hotter than in case (a). The
Nusselt-number *exponent* also differs: the bottom-heated case approaches
$Nu\propto Ra^{1/3}$, while in a strongly internally heated layer the scaling
arguments give a smaller exponent, because the heat to be transported is
generated at depth rather than supplied through a boundary.

**Run length.** At least three overturn times so that the mean profile is
stationary, with the profile averaged over the last overturn to reduce noise;
convergence judged by the drift of $Nu$ between successive halves of that window.

**What would convince me.** The two mean profiles at matched $Nu$ should
*visibly* differ: an interior that is nearly isothermal at 1/2 and symmetric in
(a), versus a bottom-warm, monotone profile with no basal boundary layer in (b).
If they do not differ, the diagnostic is not sensitive enough and the test has
failed rather than the hypothesis being rejected.
