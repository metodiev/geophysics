# Solutions — 04-06-05 Unconventional Resources: Shale, Tight Gas, Hydrates

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values computed here are labelled as such.

Throughout: the saturated moduli, the velocities, the moduli from velocities, the
stability depth and the reflection coefficients are **physical calculations**. The
brittleness index's bounds are a **convention**. Recovery factors, estimated
ultimate recoveries and reserves are **not** computed, and none is stated.

---

## ★1 — Gassmann's equation

**(a)**

$$K_\mathrm{sat} = 10 + \frac{(1 - 10/37)^{2}}
{0.15/2.5 + 0.85/37 - 10/37^{2}}
= 10 + \frac{0.53251}{0.06 + 0.022973 - 0.007305}
= 10 + 7.037 = 17.04\ \mathrm{GPa}.$$

**(b)** $(17.04 - 10)/10 = 70.4$ per cent.

**(c)** Because the pore fluid resists volumetric compression: filling the pores
with a fluid of finite bulk modulus adds stiffness, whereas an empty (dry) frame
deforms under the same stress without that resistance.

**(d)** Gassmann's equation assumes the **shear modulus is independent of the
fluid**. That is exact for a homogeneous fluid at low frequency, and it is the
reason $v_S$ (proportional to $\sqrt{\mu/\rho}$) responds to the saturation
change only through the density while $v_P$ responds through the bulk modulus as
well.

---

## ★2 — Velocities and the discriminator

**(a)** Brine: $\rho = 0.30(1050) + 0.70(2650) = 315 + 1855 =
2170$ kg m⁻³. Gas: $\rho = 0.30(200) + 1855 = 1915$ kg m⁻³.

**(b)** With $\mu = 8$ GPa and the brine-saturated $K_\mathrm{sat} = 13.02$ GPa:

$$v_P = \sqrt{\frac{13.02 + (4/3)(8)}{2170}\times10^{9}} = 3304\ \mathrm{m\,s^{-1}},
\qquad
v_S = \sqrt{\frac{8\times10^{9}}{2170}} = 1920\ \mathrm{m\,s^{-1}}.$$

With $K_\mathrm{sat} = 8.10$ GPa and the gas density:

$$v_P = \sqrt{\frac{8.10 + 10.667}{1915}\times10^{9}} = 3130\ \mathrm{m\,s^{-1}},
\qquad
v_S = \sqrt{\frac{8\times10^{9}}{1915}} = 2044\ \mathrm{m\,s^{-1}}.$$

**(c)** $v_P/v_S = 1.721$ (brine) and 1.532 (gas).

**(d)** The **shear velocity** is the better lithology indicator, because the
shear modulus is fluid independent by assumption: a change in $v_S$ at constant
rock means a change in density or in the frame, not in the pore fluid. A change in
$v_P/v_S$ therefore separates a fluid effect from a lithology effect, which a
$v_P$ amplitude alone cannot do.

---

## ★3 — Moduli from velocities

**(a)** $v_P^{2} = 17.64\times10^{6}$, $v_S^{2} = 5.76\times10^{6}$, so

$$\nu = \frac{17.64 - 2(5.76)}{2(17.64 - 5.76)} = \frac{6.12}{23.76} = 0.2576 .$$

**(b)**

$$E = \rho v_S^{2}\frac{3v_P^{2} - 4v_S^{2}}{v_P^{2} - v_S^{2}}
= 2550(5.76\times10^{6})\frac{52.92 - 23.04}{11.88}
= 36.94\ \mathrm{GPa}.$$

**(c)** Poisson's ratio is more sensitive to $v_S$: it involves the ratio of
$v_S^{2}$ to the difference $v_P^{2} - v_S^{2}$, so an error in $v_S$ is amplified
twice, while $E$ is dominated by the larger $v_P^{2}$ terms.

**(d)** With $\nu = 0.258$ and $E = 36.9$ GPa the rock is relatively **stiff and
low-Poisson**, which is the signature of a quartz-rich (brittle) composition.
Clay-rich shales typically show $\nu$ above 0.30 and lower $E$.

---

## ★★4 — A brittleness index

**(a)** $\mathrm{BI}_E = (36.94 - 10)/50 = 0.539$;
$\mathrm{BI}_\nu = (0.40 - 0.2576)/0.20 = 0.712$; mean $= 0.626$.

**(b)** Clay-rich shale: $v_P^{2} = 9.61\times10^{6}$,
$v_S^{2} = 2.56\times10^{6}$, so

$$\nu = \frac{9.61 - 5.12}{2(9.61 - 2.56)} = 0.3184,
\qquad
E = 2500(2.56\times10^{6})\frac{28.83 - 10.24}{7.05} = 16.88\ \mathrm{GPa},$$

giving $\mathrm{BI}_E = 0.138$, $\mathrm{BI}_\nu = 0.408$ and a mean of 0.273.

**(c)** The ordering — quartz-rich 0.626 above clay-rich 0.273 — is robust,
because both component indices move in the same direction and by a wide margin.
The numerical values are not: different bounds give different numbers for the same
rock.

**(d)** Physical: $(E,\nu)$ and the velocities and density they come from.
Conventional: the bounds $10$ and $60$ GPa, and $0.40$ and $0.20$, which are
choices made by the analyst. The index is a monotone rescaling of a physical pair
onto a 0–1 scale, and it should always be reported together with its bounds.

---

## ★★5 — Hydrate stability

**(a)** $P_\mathrm{floor} = (1030)(9.81)(1000)/10^{6} = 10.104$ MPa;
$\mathrm{d}P/\mathrm{d}z = (1030)(9.81)/10^{6} = 0.010104$ MPa m⁻¹.

**(b)** The boundary rises at
$0.90 \times 0.010104 = 0.009094$ K m⁻¹ $= 9.09$ K km⁻¹. The geotherm rises at
35 K km⁻¹, so

$$h = \frac{12.5 - 3}{0.035 - 0.009094} = \frac{9.5}{0.025906} = 366.7\ \mathrm{m}$$

below the seafloor.

**(c)** With bottom water at 5 °C:
$h = (12.5 - 5)/0.025906 = 289.5$ m — a 21 per cent thinning from a 2 K change.

**(d)** The two constants are the **boundary temperature at the reference
pressure** (12.5 °C) and its **slope** (0.90 °C MPa⁻¹). A real assessment must
replace both with a current laboratory compilation of methane-hydrate
dissociation data, because the boundary depends on the gas composition (heavier
components stabilise the hydrate), on salinity (which depresses the stability
field) and on the water activity — none of which a two-constant linearisation can
represent.

---

## ★★6 — Klinkenberg and closure stress

**(a)** At 2 MPa: $k_g = 5\times10^{-17}(1 + 1.5\times10^{6}/2\times10^{6})
= 5\times10^{-17}(1.75) = 8.75\times10^{-17}$ m². At 15 MPa:
$k_g = 5\times10^{-17}(1.10) = 5.50\times10^{-17}$ m².

**(b)** Ratios 1.75 and 1.10.

**(c)** Because the *gas* is slipping along the pore walls: at low mean pressure
the molecular mean free path is a significant fraction of the pore-throat
diameter, so gas transport is enhanced beyond Darcy flow. Raising the pressure
suppresses the slip and the measurement approaches the liquid permeability. The
rock has not changed; the flow mechanism has.

**(d)**
$\sigma_h = \frac{0.28}{0.72}(45 - 0.75\times20) + 0.75\times20
= 0.3889(30) + 15 = 26.67$ MPa.

---

## ★★★7 — Reading the demonstration

Quoted output from `unconventional_resources_demo.py`:

**(a)** $S_w = 1.00$: $K_\mathrm{fl} = 2.8000$ GPa, $K_\mathrm{sat} = 13.0238$,
$\rho = 2170$, $v_P = 3113$, $v_S = 1663$, ratio 1.872, $\nu = 0.300$.
0.95: 0.7467, 9.4575, 2157, 2845, 1668, 1.706, 0.238.
0.90: 0.4308, 8.8524, 2144, 2803, 1673, 1.676, 0.224.
0.80: 0.2333, 8.4657, 2119, 2788, 1683, 1.657, 0.213.
0.60: 0.1217, 8.2442, 2068, 2803, 1703, 1.645, 0.207.
0.40: 0.0824, 8.1655, 2017, 2831, 1725, 1.641, 0.205.
0.20: 0.0622, 8.1251, 1966, 2864, 1747, 1.639, 0.204.
0.00: 0.0500, 8.1006, 1915, 2900, 1770, 1.638, 0.203.

**(b)** Brine: $v_P = 3113$, $v_S = 1663$ m s⁻¹. Ten per cent gas:
$v_P = 2803$ (−9.9 per cent), $v_S = 1673$ (+0.6 per cent). Full gas:
$v_P = 2900$ (−6.8 per cent), $v_S = 1770$ (+6.4 per cent).

**(c)** Quartz-rich: $E = 29.0$ GPa, $\nu = 0.242$, $\mathrm{BI}_E = 0.381$,
$\mathrm{BI}_\nu = 0.789$, $\mathrm{BI} = 0.585$. Clay-rich: $E = 16.9$ GPa,
$\nu = 0.318$, $\mathrm{BI} = 0.273$.

**(d)** $P_\mathrm{floor} = 15.156$ MPa, $\mathrm{d}P/\mathrm{d}z = 0.010104$
MPa m⁻¹, boundary slope 9.09 K km⁻¹, base of the stability zone 478.3 m.
Sensitivity, as bottom water and gradient change: 628.7 m at 25 K km⁻¹;
478.3 m at 30 K km⁻¹; 323.6 m at 40 K km⁻¹; 382.7 m for bottom water at 4 °C;
287.0 m at 6 °C (all with the other parameter held at its reference value).

**(e)** $R = -0.1304$: **negative**, so a trough, with the polarity reversed
relative to the seafloor.

**(f)** Klinkenberg ratios 3.000 (1 MPa), 2.000 (2), 1.400 (5), 1.200 (10),
1.100 (20). Closure stress 17.60, 19.60, 21.87, 24.46 and 27.45 MPa for
$\nu = 0.15$ to 0.35.

**(g)** The Gassmann saturated moduli and velocities, the moduli computed from
velocities, the hydrostatic pressure, the stability depth for a *given* boundary,
the reflection coefficient and the closure-stress relation are **physical
calculations**. The Arrhenius-like kinetic behaviour of maturity elsewhere in the
module, the brittleness index's bounds and the Klinkenberg slip factor are
**parameterisations or conventions**. In a real assessment the porosity,
saturation, mineral moduli, boundary position, stress state and slip factor are
**inputs from logs, laboratory measurements and well tests**, and the recovery
factor is an **engineering** input.

---

## ★★★8 — Interpretation and its limits

**(a)** The fizz-gas calculation shows that $v_P$ at 10 per cent gas saturation
(2803 m s⁻¹) is *lower* than at full gas saturation (2900 m s⁻¹), because the fluid
modulus collapses as soon as any free gas appears while the density is still
nearly that of brine. A given amplitude anomaly is therefore consistent with a
range of saturations spanning an order of magnitude. The measurement that
discriminates is the **shear-wave information** — a $v_P/v_S$ analysis or a
converted-wave survey — because $v_S$ changes by only 0.6 per cent at 10 per cent
gas against 6.4 per cent at full gas, and the *ratio* therefore separates them.

**(b)** Three separate assumptions in "a hydrate accumulation contains a large
volume of gas inferred from the areal extent of a BSR":

1. **That the BSR maps a hydrate accumulation at all.** It maps the base of the
   stability field, which is a temperature–pressure surface; hydrate may be absent
   above it.
2. **That hydrate occupies a known fraction of the pore space within the stability
   zone.** This is the hydrate saturation, and seismic data constrain it only
   weakly, because hydrate's elastic properties are close to those of the pore
   fluid it displaces.
3. **That the gas in the hydrate could be produced**, which is an engineering
   statement about dissociation, permeability and well design.

Assumptions 1 and 2 are the unphysical ones to assert from seismic data alone;
assumption 3 is an engineering claim that is outside geophysics altogether.

**(c)** Two reasons a brittleness map from inversion could mislead:

1. **The index's bounds are arbitrary**, so a map drawn with one convention is not
   comparable with another, and a "brittle" area on one map may be "ductile" on
   another with the same underlying velocities.
2. **The inversion's input is anisotropic rock.** Shales are strongly anisotropic,
   so a single $E$ and $\nu$ derived from an isotropic inversion do not describe
   the rock, and the anisotropy is often the very thing that controls how a
   fracture propagates.

A non-geophysical input that the selection also depends on: the **completion
design and cost** — fluid volume, proppant, stage spacing and the water available
— together with the land and regulatory position.

**(d)** Multiplying a heat in place by a recovery factor is not a geophysical
claim at all, because $Q$ is a physical quantity and $R$ is an engineering
assumption with no physical measurement behind it. Presenting the product as a
capacity implies that $R$ is a property of the reservoir, which it is not: it
depends on permeability, well pattern, flow rate, reinjection temperature,
lifetime, cost and regulation. To make the number defensible one would have to
(i) state $R$ as an explicit assumption with its basis, (ii) show the sensitivity
$\partial Q_\mathrm{rec}/\partial R = Q$, and (iii) present the result as a
*conditional* estimate whose condition is the engineering scenario — and then
acknowledge that the scenario, not the geophysics, dominates the uncertainty.
