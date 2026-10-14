# Solutions — 02-02-03 Work, Energy, Power and Conservative Forces

> **Read this after attempting the exercises, not before.**
>
> All arithmetic was computed. $g = 9.82025\ \mathrm{m\,s^{-2}}$,
> $GM_\oplus = 3.986\,004\,418\times10^{14}$ m³ s⁻², $R = 6\,371$ km.

---

## ★1 — Work of constant and variable forces

**(a)** $W = Fd\cos\alpha$:
$\alpha = 0°$: $W = 40\times5 = \mathbf{200\ J}$;
$\alpha = 60°$: $W = 200\times0.5 = \mathbf{100\ J}$;
$\alpha = 90°$: $W = \mathbf{0\ J}$.

**(b)** $W = \int_0^{0.2}500x\,dx = \tfrac12(500)(0.2)^{2} = \mathbf{10.0\ J}$.

**(c)** The spring force is **conservative**: its work over any closed path is
zero, and a potential energy $\tfrac12kx^{2}$ exists. The constant force is
conservative too. Neither depends on the speed or on the history of the motion —
which is the operational test. By contrast, friction and drag are not
conservative: their work depends on the path and on the speed, and no potential
function exists.

---

## ★2 — The near-surface approximation

**(a)** For a conservative force, $W = \int\mathbf{F}\cdot d\mathbf{r}
= -\int\nabla U\cdot d\mathbf{r} = -\Delta U$ by the fundamental theorem for line
integrals. The result is path-independent, which is what makes $U$ a function of
position alone.

**(b)** The exact work is
$$W_{\text{exact}} = GMm\left(\frac{1}{R}-\frac{1}{R+h}\right)
= mgh\frac{1}{1+h/R},$$
so the relative error of $mgh$ is $h/R$ to leading order. For $h = 5$ km:
$5/6371 = 7.848\times10^{-4}$, i.e. **0.078%**.

**(c)** $h/R = 0.01$ gives $h = \mathbf{63.7\ km}$. So $mgh$ is a 1% approximation
up to 64 km — far beyond any borehole, mine or mountain, and far short of any
orbital application.

---

## ★3 — Escape speed

**(a)** Set the total specific energy to zero at $r = R$:
$\tfrac12v^{2} - GM/R = 0 \Rightarrow v_{\text{esc}} = \sqrt{2GM/R}$. Equivalently,
the work against gravity from $R$ to infinity is $GMm/R$, and the kinetic energy
must match it.

**(b)** $v_{\text{esc}} = \sqrt{2\times3.986\,004\,418\times10^{14}/6.371\times10^{6}}
= \mathbf{11\,186.14\ m\,s^{-1}} = 11.19$ km/s.

**(c)** The specific energy required is $GM/R = \mathbf{6.2565\times10^{7}\ J\,kg^{-1}}$.
For a bound (elliptical) orbit the total specific energy is **negative**;
$\varepsilon = 0$ is parabolic escape and $\varepsilon > 0$ hyperbolic. The sign
of one scalar classifies the trajectory.

---

## ★4 — Pumping water

**(a)** $2\ \mathrm{m^{3}\,min^{-1}} = 0.033333\ \mathrm{m^3\,s^{-1}}$, so
$\dot m = \rho\dot V = 1000\times0.033333 = \mathbf{33.333\ kg\,s^{-1}}$
(nominal fresh-water density).

**(b)** $P = \dot mgh = 33.333\times9.82025\times50 = \mathbf{1.6367\times10^{4}\ W}
= 16.37$ kW.

**(c)** Efficiency $= 16.37/25 = \mathbf{65.5\%}$. The remaining 34.5% is lost to
friction in the pump and pipe, turbulence and motor losses — a power balance, not
an energy one. Note that a "pump efficiency" quoted without saying whether it is
the *wire-to-water* or the *hydraulic* efficiency is not a well-defined number.

---

## ★★5 — Sliding block

**(a)** Friction: $W_f = -\mu_kN d = -\mu_kmgd = -0.4\times5\times9.82025\times3
= \mathbf{-58.92\ J}$. Gravity: the displacement is horizontal, so
$W_g = \mathbf{0\ J}$.

**(b)** Initial kinetic energy $= \tfrac12\times5\times16 = 40$ J. After the
slide, $K = 40 - 58.92 = -18.92$ J — **a negative kinetic energy, which is
impossible**. The conclusion is physical, not arithmetic: the block cannot slide
3 m at $\mu_k = 0.4$ from 4 m/s; it stops after
$d_{\text{stop}} = K_0/(\mu_kmg) = 40/19.64 = 2.037$ m. The lesson: when the
computed kinetic energy goes negative, the *model* has been applied outside its
range (the friction law applies only while sliding).

---

## ★★6 — Spring launcher

**(a)** $E = \tfrac12kx^{2} = \tfrac12\times500\times0.04 = \mathbf{10.0\ J}$;
launch speed $v = \sqrt{2E/m} = \sqrt{40} = \mathbf{6.3246\ m\,s^{-1}}$.

**(b)** With $mgh$: $h = E/(mg) = 10/(0.5\times9.82025) = \mathbf{2.0366\ m}$.
The limiting approximation is $mgh$ itself (and the neglect of air resistance,
which is not negligible at 6 m/s for a light projectile with any appreciable
cross-section).

**(c)** At the height reached, $h = 2.04$ m, the relative error of $mgh$ is
$h/R = 2.04/6.371\times10^{6} = \mathbf{3.2\times10^{-7}}$, i.e. 0.000032%. The
near-surface approximation is not the limiting factor at all here; if this
experiment needs accuracy, the limiting factor is air resistance (and the
projectile's cross-section), not gravity's variation.

---

## ★★7 — Uplift energy and power

**(a)** $W = \rho A g h^{2}/2 = 2700\times10^{6}\times9.82025\times10^{6}/2
= \mathbf{1.3257\times10^{16}\ J}$. (The centre of mass rises $h/2$.)

**(b)** At $10^{6}$ W: $1.326\times10^{10}$ s $= \mathbf{420\ yr}$.
At $10^{9}$ W: $\mathbf{0.42\ yr}$ (about 5 months).

**(c)** Both powers are *assumed* levels for comparison, not measurements of any
real process. The point is structural: $1.33\times10^{16}$ J is the annual output
of an ordinary power station, so the *energy* is unremarkable. What makes uplift
slow is that the power available to a buoyancy-driven process is limited by
viscous dissipation and by the rate at which mass can be moved — a transport
problem, not an energy-supply problem. This is why geodynamics is written in
terms of viscosities and Rayleigh numbers rather than energies.

---

## ★★8 — Seismic moment and radiated energy

**(a)** $M_0 = \mu AD = 3\times10^{10}\times2\times10^{7}\times0.5
= \mathbf{3.0\times10^{17}\ N\,m}$.

**(b)** $E_s = (\Delta\sigma/2\mu)M_0 = (3\times10^{6}/6\times10^{10})
\times3.0\times10^{17} = \mathbf{1.5\times10^{13}\ J}$.

**(c)** $1.5\times10^{13}/4.184\times10^{12} = \mathbf{3.6\ kt}$ of TNT
equivalent. **Assumed inputs:** the shear modulus (a nominal 30 GPa for crustal
rock), the stress drop (a measured quantity with a large spread, here assumed at
3 MPa), and the uniform-stress-drop source model behind
$E_s = (\Delta\sigma/2\mu)M_0$. $M_0$ itself is a source parameter, not an energy:
the two share a dimension and differ here by a factor of
$1.5\times10^{13}/3.0\times10^{17} = 5\times10^{-5}$.

---

## ★★★9 — Geothermal resource lifetime

**(a)** $E_{\text{thermal}} = V\rho c\,\Delta T
= 10^{9}\times2.16\times10^{6}\times200 = \mathbf{4.32\times10^{17}\ J}$.

**(b)** At 100 MW thermal: $4.32\times10^{17}/10^{8} = 4.32\times10^{9}$ s
$= \mathbf{137\ yr}$. At 1 GW thermal: $13.7$ yr. (For the stated 10 MW of
*electrical* output, the thermal draw would be higher by the conversion
efficiency, which is typically 10–20% for a low-enthalpy doublet — so the
electric lifetime would be roughly 14–27 years if the whole reservoir were
accessible at $\Delta T = 200$ K.)

**(c)** Reality departs from $E/P$ for at least three reasons: (i) the produced
fluid cools the rock near the well long before the whole reservoir is depleted,
so the outlet temperature — and hence the power — declines with time; (ii) only a
fraction of the reservoir volume is hydraulically connected to the well pair
(recoverable fraction); and (iii) reinjection short-circuits along high-
permeability paths, bypassing most of the rock. The first is a diffusion limit
(§3.2 of [02-01-03](../../01-measurement-and-physical-reasoning/03-scaling-laws.md)),
the second a geometry problem, the third a heterogeneity problem.

**(d)** The measurement that would most change the answer is the **effective
permeability distribution** (from a well test and from tracers), because it
controls the connected volume and the thermal drawdown rate. $\rho c$ and
$\Delta T$ are comparatively well constrained; the connectivity is not.

---

## ★★★10 — Conservation tests

**(a)** For $\mathbf{F} = -kx\hat{\mathbf{x}}$, take the rectangle
$0\le x\le a$, $0\le y\le b$. The vertical legs contribute nothing
($\mathbf{F}\cdot d\mathbf{r} = 0$ since $\mathbf{F}$ has no $y$-component).
The horizontal legs: $\int_0^{a}(-kx)\,dx$ at $y = b$, and the return leg
$\int_a^{0}(-kx)\,dx$ at $y = 0$. These are equal and opposite, so the sum is
**exactly zero** — the force is conservative and $\nabla\times\mathbf{F}
= \mathbf{0}$.

**(b)** For $\mathbf{F} = -c|\mathbf{v}|\mathbf{v}$, traverse a loop in such a way
that the speed is different on the two legs (e.g. a rectangle traversed faster
along one side). Then the two horizontal contributions are
$-c|v_1|v_1a$ and $+c|v_2|v_2a$ with $v_1\ne v_2$, and the sum is
$-ca(|v_1|v_1 - |v_2|v_2) \ne 0$: **the work around a closed path does not
vanish**, so drag is not conservative. Note also that $\mathbf{F}$ here depends on
$\mathbf{v}$, not on position alone, so the curl test as usually stated does not
even apply — a reminder that the test presumes a velocity-independent force field.

**(c)** $\nabla\times\mathbf{F} = \mathbf{0}$ guarantees path independence on a
**simply connected** domain — one where every closed loop can be shrunk to a point
without leaving the domain. On a domain with a hole (a borehole, a long
conductor, an excluded cylinder), a field can be curl-free yet have non-zero
circulation around the hole, and no single-valued potential exists. The physical
example is the magnetic field of a current-carrying wire, which is curl-free in
the region around the wire but whose circulation is non-zero. The condition is
therefore sufficient only under the domain assumption — which is exactly the
caveat attached to "a curl-free field has a potential" in
[01-06-04](../../../01-mathematics/06-multivariable-calculus/04-divergence-and-curl.md).
