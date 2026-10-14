# Solutions — 02-06-05 Flow in Porous Media: Darcy's Law and Permeability

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. All material labels are nominal permeability
> classes, not measurements of a specific formation.

---

## ★1 — Permeability and hydraulic conductivity

**(a)** $K = \dfrac{k\rho g}{\mu} = \dfrac{10^{-13}\times1000\times9.81}{10^{-3}}
= \mathbf{9.81\times10^{-7}\ m\,s^{-1}}$.

**(b)** $9.81\times10^{-7}\times86\,400 = \mathbf{0.0848\ m\,day^{-1}}$.

**(c)** $K = \dfrac{10^{-13}\times800\times9.81}{5\times10^{-3}} =
\mathbf{1.57\times10^{-7}\ m\,s^{-1}} = 0.0136$ m per day.

**(d)** $K_{\text{water}}/K_{\text{oil}} = 9.81\times10^{-7}/1.57\times10^{-7} =
\mathbf{6.25}$. The **permeability does not differ**: $k$ is a property of the
rock alone. Only $K$ changes, because it contains $\rho g/\mu$ — which is the
whole reason the intrinsic and hydraulic descriptions are kept separate.

---

## ★2 — Bundle of tubes

**(a)** $k = \phi r^2/8 = 0.2\times(10^{-5})^2/8 = \mathbf{2.5\times10^{-12}\
\mathrm{m^2}}$.

**(b)** $K = k\rho g/\mu = 2.5\times10^{-12}\times9810/10^{-3} = \mathbf{2.45\times
10^{-5}\ m\,s^{-1}} = 2.12$ m per day.

**(c)** Specific discharge $q = Ki = 2.45\times10^{-5}\times0.01 =
\mathbf{2.45\times10^{-7}\ m\,s^{-1}}$; pore velocity
$v = q/\phi = 2.45\times10^{-7}/0.2 = \mathbf{1.23\times10^{-6}\ m\,s^{-1}}$.

**(d)** (i) The tubes are straight, of one size, smooth and all aligned with the
flow; a real pore space is tortuous, of mixed sizes, rough and three-dimensional,
and the flow is dominated by the largest connected throats. (ii) The model
assumes the medium is fully saturated and that the fluid is Newtonian and
inertia-free in every tube — the last of which fails in the widest throats at high
discharge. The formula gives the *scaling* against $r$ and $\phi$, and nothing
more than that.

---

## ★3 — Fracture permeability and the cubic law

**(a)** $k = b^2/12 = (5\times10^{-4})^2/12 = 2.083\times10^{-8}$ m²
$= \mathbf{2.11\times10^{4}\ darcy}$.

**(b)** $K = k\rho g/\mu = 2.083\times10^{-8}\times9810/10^{-3} =
\mathbf{0.2044\ m\,s^{-1}}$.

**(c)** At unit hydraulic gradient $q = K = 0.2044$ m s⁻¹. From lesson 03, ★★2,
the cubic law with $G = 10^4$ Pa m⁻¹ and $b = 0.5$ mm gave
$u_{\text{mean}} = 0.2083$ m s⁻¹. A unit hydraulic gradient in water corresponds
to $G = \rho g = 9810$ Pa m⁻¹, so the two numbers are the same quantity computed
by two routes: $q = (b^2/12)(G/\mu) = 2.083\times10^{-8}\times9810/10^{-3} =
0.204$ m s⁻¹.

**(d)** Because Darcy's law with $k = b^2/12$ *is* the cubic law: equation (6) was
obtained by writing the Poiseuille result in Darcy's form. The agreement verifies
the algebra of the conversion, and that Darcy's specific discharge equals the
Poiseuille mean velocity for a slot. It does not verify that either applies to a
real fracture — for that, the hydraulic aperture must be measured (lesson 03,
★★8).

---

## ★4 — Confined aquifer

**(a)** $T = KD = 10^{-5}\times50 = \mathbf{5\times10^{-4}\ m^2\,s^{-1}}$.

**(b)** $q = Ki = 10^{-5}\times10^{-3} = \mathbf{10^{-8}\ m\,s^{-1}}$. Across a
10 km front: $Q = q\times10^4\ \mathrm{m}\times50\ \mathrm{m} =
10^{-8}\times10^4\times50 = \mathbf{5\times10^{-3}\ m^3\,s^{-1}}$. Pore
velocity $v = q/\phi = 10^{-8}/0.25 = \mathbf{4\times10^{-8}\ m\,s^{-1}}$.

**(c)** $t = 10^{3}/4\times10^{-8} = 2.5\times10^{10}$ s $= \mathbf{792\ years}$.

**(d)** The **pore velocity**, not the specific discharge: a contaminant is
carried by the fluid, which moves at $q/\phi$. Using $q$ would understate the
travel speed by a factor of 4 here and produce a 792-year error in the arrival
time — the kind of mistake that matters.

---

## ★★5 — The Thiem solution

**(a)** $Q = \dfrac{2\pi T(h_2-h_1)}{\ln(r_2/r_1)} =
\dfrac{2\pi\times10^{-3}\times10}{\ln(10^4)} =
\dfrac{6.283\times10^{-2}}{9.2103} = \mathbf{6.82\times10^{-3}\ m^3\,s^{-1}}$.

**(b)** $6.82\times10^{-3}\times86\,400 = \mathbf{589\ m^3\,day^{-1}}$.

**(c)** $\dfrac{\mathrm{d}h}{\mathrm{d}r} = -\dfrac{Q}{2\pi Tr}$:
at $r = 1$ m, $-6.82\times10^{-3}/(2\pi\times10^{-3}) = -1.086$ m m⁻¹;
at $r = 100$ m, $-1.086\times10^{-2}$ m m⁻¹. The gradient falls as $1/r$: steep
near the well, gentle far from it. This is why the largest head loss occurs in
the first metre around a well and why a well's "radius of influence" is a
modelling construct.

**(d)** (i) The solution is **steady**, and a confined aquifer does not reach
steady state; drawdown grows without bound (though slowly after some time).
(ii) The medium is assumed **homogeneous and isotropic**, whereas real aquifers
are layered and heterogeneous, so a single $T$ is an average that may be
representative of neither the near-well zone nor the far field. A third
approximation — that the well fully penetrates the aquifer — matters in practice
as well.

---

## ★★6 — Reading the demo

**(a)** $k$ from the summed flux $= 6.250000\times10^{-13}$ m²;
$k$ from $\phi r^2/8 = 6.250000\times10^{-13}$ m²; relative difference
$1.85\times10^{-10}$.

**(b)** Silty sand ($k = 10^{-13}$ m²): $K = 8.476\times10^{-2}$ m per day. A
1 mm open fracture ($k = 8.3\times10^{-8}$ m²): $K = 7.035\times10^{4}$ m per
day. Ratio $\approx \mathbf{8.3\times10^{5}}$, i.e. six orders of magnitude.

**(c)** $|Q| = 1.447379\times10^{-3}$ m³ s⁻¹ $= 125.05$ m³ per day; relative
difference from the numerical radial integration $5.08\times10^{-5}$.

**(d)** At $q = 10^{-2}$ m s⁻¹: sand aquifer ($d = 0.2$ mm) $Re_p = 2.0$
(darcy ok); gravel aquifer ($d = 10$ mm) $Re_p = 1.0\times10^{2}$ (Darcy
invalid); 1 mm fracture ($d = 1$ mm) $Re_p = 10$ (Darcy invalid, though for a
fracture the correct model is the cubic law, whose laminar range extends much
further).

---

## ★★7 — Pore-pressure diffusion

**(a)** $\kappa_h = \dfrac{k\rho g}{\mu S_s} =
\dfrac{10^{-15}\times1000\times9.81}{10^{-3}\times10^{-5}} =
\mathbf{9.81\times10^{-4}\ m^2\,s^{-1}}$.

**(b)** $L = \sqrt{\kappa_h t}$: for 1 day, $\sqrt{9.81\times10^{-4}\times86\,400}
= \mathbf{9.21\ m}$; for 1 year, $\sqrt{9.81\times10^{-4}\times3.156\times10^7} =
\mathbf{175.9\ m}$; for 100 years, $\sqrt{9.81\times10^{-4}\times3.156\times10^9}
= \mathbf{1759\ m}$.

**(c)** $t = L^2/\kappa_h = 10^{6}/9.81\times10^{-4} = 1.02\times10^{9}$ s
$= \mathbf{32.3\ years}$.

**(d)** For $k = 10^{-14}$ m², $\kappa_h = 9.81\times10^{-3}$ m² s⁻¹, so
$L(1\ \text{day}) = 29.1$ m, $L(1\ \text{yr}) = 556.4$ m and the 1 km time is
$\mathbf{3.23\ years}$. The ratio of the two 1 km times is $\mathbf{10}$,
exactly the ratio of the permeabilities: $t \propto 1/k$.

These numbers reproduce the demo's section 5 (`9.8100e-04`, `9.21`,
`175.9`), and they are the reason a triggered-seismicity study must state its
permeability and storage assumptions: a factor of ten in $k$ moves the
reachable distance by a factor of $\sqrt{10}$ in a fixed time, or the required
time by a factor of ten at fixed distance.

---

## ★★8 — Darcy validity thresholds

**(a)–(b)** $q^\ast = \mu/(\rho d)$:

| Medium | $d$ (m) | $q^\ast$ (m s⁻¹) | $q^\ast$ (m day⁻¹) |
|---|---|---|---|
| sand | $2\times10^{-4}$ | $5\times10^{-3}$ | 432 |
| gravel | $10^{-2}$ | $10^{-4}$ | 8.64 |
| karst conduit | $0.5$ | $2\times10^{-6}$ | 0.173 |

**(c)** With typical groundwater specific discharges of $10^{-6}$–$10^{-5}$
m s⁻¹ ($0.086$–$0.86$ m per day):

- **sand**: $Re_p = 0.002$–$0.02$, three orders inside the limit. Darcy's law is
  safe by a wide margin.
- **gravel**: $Re_p = 0.01$–$0.1$ at typical flows, but an order of magnitude
  higher discharge (which occurs near a well) crosses $Re_p = 1$ and then 10, so
  the quadratic correction becomes necessary.
- **karst conduit**: $Re_p = 0.5$–$5$ at *typical* flows and far above that in a
  flood. Flow in a karst conduit is not Darcy flow at all; it is conduit flow
  governed by the cubic law or by a pipe friction law, and the transition matters
  for how fast a contaminant travels.

**(d)** Because what controls the validity of the Stokes approximation is the
local flow around a *pore*: whether inertia matters for the fluid squeezing
through a throat of size $d$. The aquifer thickness is irrelevant to that
question. Using the formation scale in $Re_p$ gives a number smaller by many
orders of magnitude and would wrongly suggest Darcy's law always applies.

---

## ★★★9 — Deriving the diffusion equation

**(a)** Starting point:

$$\frac{\partial(\phi\rho)}{\partial t} + \nabla\cdot(\rho\mathbf{q}) = 0.$$

**(b)** Expand and use the linearised compressibilities. With
$\mathrm{d}\rho = \rho c_f\,\mathrm{d}p$ and $\mathrm{d}\phi = \phi c_m\,
\mathrm{d}p$,

$$\frac{\partial}{\partial t}\left[\phi\rho\right] = \rho(\phi c_m +
\phi c_f)\frac{\partial p}{\partial t} = \rho\phi(c_f+c_m)\frac{\partial
p}{\partial t}.$$

The flux divergence is $\rho\nabla\cdot\mathbf{q} + \mathbf{q}\cdot\nabla\rho$;
the second term is second order in the perturbations, so
$\nabla\cdot(\rho\mathbf{q}) \approx \rho\nabla\cdot\mathbf{q}$. Inserting
Darcy's law in the head form, $\mathbf{q} = -K\nabla h$ with
$h = p/(\rho g)$ for **constant density**, gives $\mathbf{q} =
-(k/\mu)\nabla p$ and hence

$$\nabla\cdot\mathbf{q} = -\frac{k}{\mu}\nabla^2 p .$$

Dividing the mass balance by $\rho$ and rearranging:

$$\phi(c_f+c_m)\frac{\partial p}{\partial t} = \frac{k}{\mu}\nabla^2 p
\;\Longrightarrow\;
\frac{\partial p}{\partial t} = \frac{k}{\mu\phi(c_f+c_m)}\nabla^2 p.$$

The approximation made explicitly is that the driving gradient is dominated by
the pressure perturbation, i.e. $\nabla p \gg \rho\mathbf{g}$ in the sense that
the *hydraulic* gradient is what drives the perturbation flux; for a
constant-density fluid at rest this is exact, because $\rho\mathbf{g}$ is
absorbed into the hydrostatic reference state. In a variable-density system it is
**not** exact and the full $\nabla p - \rho\mathbf{g}$ must be retained.

**(c)** Multiplying numerator and denominator by $\rho g$:
$\kappa_h = \dfrac{k\rho g}{\mu\phi(c_f+c_m)\rho g} =
\dfrac{k\rho g}{\mu S_s}$ with

$$S_s = \rho g\,\phi(c_f+c_m) + \rho g\,c_m^{\text{(solid)}} .$$

The classical definition of specific storage includes a third term from the
compressibility of the solid grains; for most rocks the pore and fluid terms
dominate if $\phi$ is not vanishingly small, but for a very low-porosity
crystalline rock the solid term can matter. Stating which terms were kept is part
of the derivation.

**(d)** $c_f$ is the **fluid compressibility**, $1/\rho\,\mathrm{d}\rho/\mathrm{d}p$
— about $4.5\times10^{-10}$ Pa⁻¹ for water. $c_m$ is the **pore (matrix)
compressibility**, the fractional change in pore volume per unit pressure change,
which for a stiff crystalline rock is of order $10^{-11}$–$10^{-10}$ Pa⁻¹ and for
a soft soil can reach $10^{-6}$ Pa⁻¹ or more. In a stiff rock the fluid
compressibility dominates (water is hard to compress but the rock is harder); in
a soft soil the matrix term dominates by orders of magnitude, which is why
$\kappa_h$ in a clay is small even if $k$ is not, and why the same permeability
gives different diffusion rates in different materials.

---

## ★★★10 — Triggering distance

**(a)** An increase $\Delta p$ in pore pressure reduces the effective normal
stress by $\Delta p$, so the Coulomb failure function changes by
$\Delta\mathrm{CFF} = \Delta\tau - \mu_f\Delta\sigma_n' \approx \mu_f\Delta p$ if
the shear traction is unchanged. With $\mu_f = 0.6$ and $\Delta p = 1$ MPa,
$\Delta\mathrm{CFF} = \mathbf{0.6\ MPa}$.

**(b)** Typical earthquake stress drops are of order 1–10 MPa, so 0.6 MPa may be
**10 to 60 per cent** of a stress drop. That is a substantial perturbation: it is
more than enough to advance the failure time of a fault already close to
failure, which is the accepted mechanism for injection-induced earthquakes. It
is *not* enough to break an intact, well-oriented fault that is far from
failure, which is why induced seismicity is strongly site- and stress-state
dependent.

**(c)** With $\kappa_h = 9.81\times10^{-4}$ m² s⁻¹ ($k = 10^{-15}$ m²),
$t = L^2/\kappa_h = 300^2/9.81\times10^{-4} = 9.17\times10^{7}$ s
$= \mathbf{2.9\ years}$. With $k = 10^{-14}$ m² ($\kappa_h = 9.81\times10^{-3}$),
$t = \mathbf{0.29\ year} = 106$ days.

**(d)** Because the travel time depends linearly on $1/k$ while the distance
depends on $\sqrt{t}$: a single order of magnitude in the permeability — routine
in the crust — moves the reachable distance in one year from 176 m to 556 m, and
the time to reach a fixed 300 m from about three years to about three months.
The two controlling quantities are the **permeability** $k$ (through
$\kappa_h$) and the **specific storage** $S_s$. Both are measured, both vary by
orders of magnitude, and therefore a triggering distance must be reported as a
range over the plausible values of both — which is exactly how the induced-
seismicity literature reports it. See
[06-seismology/12 Induced and Triggered Seismicity](../../../06-seismology/12-induced-and-triggered-seismicity/README.md)
and [14-hydrology-hydrogeophysics](../../../14-hydrology-hydrogeophysics/README.md).
