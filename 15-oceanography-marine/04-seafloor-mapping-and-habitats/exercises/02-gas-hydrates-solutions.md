# Solutions — 15-04-02 Gas Hydrates: Occurrence, Geophysics and Resource Potential

> **Read after attempting the exercises.** Lesson:
> [02 Gas Hydrates](../02-gas-hydrates.md). All numbers are SYNTHETIC model
> values.

## ★ Foundational

## ★1 — Mass fraction and gas yield

$$f_{\mathrm{CH_4}}=\frac{8\times16.043}{8\times16.043+46\times18.015}
=\frac{128.344}{828.690+128.344}=\frac{128.344}{957.034}=0.13411 .$$

Note the mass fraction is **independent of the hydrate density** — it depends only
on the stoichiometry and occupancy.

$$Y=\frac{\rho_hf}{M_{\mathrm{CH_4}}}V_m
=\frac{920\times0.13411}{0.016043}\times0.022414
=7688.6\times0.022414=172.3\ \mathrm{m^3\,(STP)\,m^{-3}} .$$

Cross-check against the demonstration's sensitivity table: at
$\rho_h=900$ and occupancy 1.0 it gives 168.6 m³/m³, and at occupancy 0.8, 138.6;
our (920, 0.9) case sits between them, as it must.

## ★2 — Dissociation pressure and depth

$$p_{\text{eq}}=2.60\times10^{6}\exp\left[-6516\left(\frac{1}{280.15}-
\frac{1}{273.15}\right)\right]
=2.60\times10^{6}\exp(0.59593)=4.72\times10^{6}\ \mathrm{Pa}.$$

$$z=\frac{4.72\times10^{6}-101325}{1028\times9.81}
=\frac{4.6187\times10^{6}}{10084.7}=458\ \mathrm{m}.$$

Both agree with the demonstration's table.

## ★3 — Fluid modulus and density

$$K_{\text{fl}}=\left(\frac{0.30}{7.9\times10^{9}}+
\frac{0.70}{2.2\times10^{9}}\right)^{-1}
=\left(3.797\times10^{-11}+3.182\times10^{-10}\right)^{-1}
=\frac{1}{3.562\times10^{-10}}=2.808\times10^{9}\ \mathrm{Pa}.$$

$$\rho=(1-0.35)\times2650+0.35(0.30\times920+0.70\times1030)
=1722.5+0.35(989.0)=2068.7\ \mathrm{kg\,m^{-3}} .$$

## ★★ Applied

## ★4 — Gassmann velocity at $S_h=0.60$

$$K_{\text{fl}}=\left(\frac{0.60}{7.9\times10^{9}}+
\frac{0.40}{2.2\times10^{9}}\right)^{-1}
=\left(7.595\times10^{-11}+1.818\times10^{-10}\right)^{-1}
=3.879\times10^{9}\ \mathrm{Pa},$$

$$\text{denominator}=\frac{0.35}{3.879\times10^{9}}+\frac{0.65}{36\times10^{9}}
-\frac{1.0\times10^{9}}{(36\times10^{9})^{2}}
=9.023\times10^{-11}+1.806\times10^{-11}-7.72\times10^{-13}
=1.0752\times10^{-10},$$

$$\text{numerator}=(1-1/36)^{2}=0.94522,\qquad
K_{\text{sat}}=1.0\times10^{9}+\frac{0.94522}{1.0752\times10^{-10}}
=1.0\times10^{9}+8.791\times10^{9}=9.791\times10^{9}\ \mathrm{Pa},$$

$$\rho=(0.65\times2650)+0.35(0.60\times920+0.40\times1030)=1722.5+337.4
=2059.9\ \mathrm{kg\,m^{-3}},$$

$$v_p=\sqrt{\frac{9.791\times10^{9}+\tfrac43(0.6\times10^{9})}{2059.9}}
=\sqrt{\frac{1.0591\times10^{10}}{2059.9}}
=\sqrt{5.1415\times10^{6}}=2267.5\ \mathrm{m\,s^{-1}} .$$

Interpolating the lesson's table between $S_h=0.5$ (2172.9) and 0.7 (2379.7) at
0.6 gives 2276.3 m/s; the direct calculation gives 2267.5 m/s. The 9 m/s (0.4%)
difference is the curvature of the velocity–saturation relation, so the
interpolation is fine for an estimate and the arithmetic is what should be quoted.

## ★5 — Gas in place

$$V_{\text{hydrate}}=Ah\phi S_h=50\times10^{6}\times30\times0.30\times0.50
=2.25\times10^{8}\ \mathrm{m^3},$$

$$V_{\text{gas}}=2.25\times10^{8}\times168.6=3.793\times10^{10}\ \mathrm{m^3\ (STP)}
=37.9\times10^{9}\ \mathrm{m^3},$$

$$=3.793\times10^{10}\times35.3147=1.340\times10^{12}\ \mathrm{ft^3}
=1.34\times10^{12}\ \mathrm{ft^3}.$$

## ★6 — Base of the stability zone at 1500 m water depth

Seafloor pressure $=101325+1028\times9.81\times1500=1.5237\times10^{7}\
\mathrm{Pa}=15.24\ \mathrm{MPa}$.

| $z$ (m) | $T$ (°C) | $T$ (K) | $p$ (MPa) | $p_{\text{eq}}$ (MPa) | stable? |
|---|---|---|---|---|---|
| 500 | 20.5 | 293.65 | 20.28 | 13.74 | yes |
| 650 | 25.75 | 298.90 | 21.79 | 20.31 | yes |
| 675 | 26.63 | 299.78 | 22.05 | 21.65 | yes |
| 700 | 27.5 | 300.65 | 22.30 | 23.06 | **no** |
| 690 | 27.15 | 300.30 | 22.20 | 22.47 | no |

The base is between 675 m (stable) and 690 m (unstable): **about 685 m**, and the
bracketing interval is 15 m, so the answer within $\pm10$ m is
$685\ \mathrm{m}\pm8\ \mathrm{m}$ given the model.

The arithmetic for the two bracketing rows:
$p_{\text{eq}}(299.78)=2.60\exp[-6516(1/299.78-1/273.15)]
=2.60\exp(2.1193)=21.65$ MPa against a hydrostatic 22.05 MPa;
$p_{\text{eq}}(300.30)=2.60\exp(2.1571)=22.47$ MPa against 22.20 MPa.

## ★★★ Research-oriented

## ★7 — Which model does the shear velocity favour?

**(a)** $v_p/v_s=2300/560=4.11$; Poisson ratio

$$\nu=\frac{v_p^{2}-2v_s^{2}}{2(v_p^{2}-v_s^{2})}
=\frac{5.290\times10^{6}-6.272\times10^{5}}{2(5.290\times10^{6}-3.136\times10^{5})}
=\frac{4.6628\times10^{6}}{9.9528\times10^{6}}=0.469 .$$

**(b)** The lesson's pore-filling model gives $v_p/v_s=4.03$ at $S_h=0.5$ and
$4.41$ at 0.7 — bracketing the observed 4.11, with $v_s\approx540\ \mathrm{m/s}$.
The cementation model gives $v_p/v_s=2.10$ at $S_h=0.5$ and $2.04$ at 0.7, with
$v_s\approx1150$–$1230\ \mathrm{m/s}$. The observation matches **pore-filling**,
decisively: the observed $v_s=560\ \mathrm{m/s}$ is within 4% of the pore-filling
curves and half of the cementation values. Consistently, the observed $v_p=2300$
inverts to $S_h\approx0.63$ in the pore-filling model and 0.30 in the
cementation model, but only the pore-filling model also reproduces the shear
velocity.

**The structural reason** is that Gassmann's equation leaves the shear modulus
unchanged by fluid substitution, so the pore-filling model's $v_s$ can only change
through the density (a few per cent here), while the cementation model changes
$G_{\text{dry}}$ directly, by a factor of about two at $S_h=0.5$.

**(c)** The remaining model choice is the **dry-frame moduli and their porosity
dependence**. Both models were evaluated at $\phi=0.35$ with $K_{\text{dry}}=1.0$
and $G_{\text{dry}}=0.6\ \mathrm{GPa}$; a stiffer frame (a cemented or compacted
sand) would raise both $v_p$ and $v_s$ at every saturation, moving the inferred
$S_h$ and changing the $v_p/v_s$ baseline. The measurement that removes it is an
independent porosity and dry-frame calibration: a core measurement, or a
log-derived porosity with a velocity cross-plot from intervals known to be
hydrate-free in the same lithology. **A hydrate saturation is always a
difference from a hydrate-free reference, and that reference is a model too.**

## ★8 — A factor-of-three programme

| quantity | how to obtain it | measured or modelled? | contribution to the range |
|---|---|---|---|
| area | BSR and velocity-anomaly mapping of the seismic grid | measured (model-dependent edges) | factor 1.3–2 (mapping thresholds) |
| thickness | the same, plus amplitude-versus-offset; a log if available | measured | factor 1.5–3 |
| porosity | a log or core, or a velocity–porosity relation calibrated on hydrate-free intervals | measured if logged, otherwise modelled | factor 1.3–1.8 |
| saturation | $v_p$ and **$v_s$**, with a stated rock-physics model | modelled (the velocity is measured) | factor 2.1 (model choice) |
| yield | the unit cell | neither — a derived constant; the density and occupancy choices span 1.36× | a derived constant with a stated band |
| recovery factor | engineering, not geophysics | modelled | factor 2–5 if misused as a reserve |

**Dominating term:** saturation, through the rock-physics model choice
(2.1×), closely followed by the recovery factor if the question is a reserve
rather than in-place gas. Adding the five ranges in quadrature
($1.3\times1.5\times1.3\times2.1\times1.36$ for the in-place volume) already
exceeds a factor of 7 — which is why a factor-of-three target requires *fixing*
rather than measuring: pick one rock-physics model and justify it with a $v_s$
measurement, bound $\phi$ from logs, and define the area by a single stated
threshold.

**The honest statement:** "The in-place gas volume in this model interval is
$X\times10^{9}\ \mathrm{m^3}$ (STP) at the reference case $\phi=0.35$,
$S_h=0.63$; the 90% range from the porosity and saturation is
$0.4X$–$2.0X$, dominated by the choice of hydrate-occupancy model, which the
measured $v_p/v_s$ ratio favours toward pore-filling. **No geophysical
measurement determines the recovery factor**, so no reserve figure is quoted."

The quantity with no geophysical measurement is the recovery factor; the
quantity with no *direct* measurement at all is the thickness-integrated
saturation, which is always an inversion of a velocity anomaly.
