# Solutions — 04-05-02 Glacial and Periglacial Landforms and Sediments

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Every velocity below carries its thickness and temperature, because with
$\bar u \propto A H^{n+1}$ neither can be omitted.

---

## ★1 — Driving stress and deformation velocity

**(a)**
$\tau_b = 917 \times 9.81 \times 800 \times \sin(0.5^\circ)
= 8995.8 \times 800 \times 8.7265\times10^{-3} = 6.280\times10^{4}$ Pa.

**(b)**
$\bar u_d = \frac{2(2.4\times10^{-24})}{4}(6.2802\times10^{4})^{3}(800)
= 1.2\times10^{-24} \times 2.4771\times10^{14} \times 800
= 2.378\times10^{-7}$ m s⁻¹.

Multiply by $3.15576\times10^{7}$ s yr⁻¹:
$\bar u_d = 7.504$ m yr⁻¹.

**(c)** $A(-20\,^\circ\mathrm{C}) = 2.4\times10^{-24}
\exp\!\left[\frac{6.0\times10^{4}}{8.314}\left(\frac{1}{273.15} -
\frac{1}{253.15}\right)\right] = 2.977\times10^{-25}$ Pa⁻³ s⁻¹, i.e. 12.4 per
cent of $A(0)$. Velocity is linear in $A$, so
$\bar u_d = 0.9307$ m yr⁻¹.

**(d)** Ratio $= 7.504/0.9307 = 8.06$. Equivalently
$A(0)/A(-20) = 100/12.4 = 8.06$: with $n = 3$ and a fixed geometry the velocity
ratio is *exactly* the ratio of the flow-law coefficients, which is why a 20 K
cooling matters so much and why an ice-temperature estimate is a required input
to any ice-flux calculation.

---

## ★2 — Perfect plasticity

**(a)** $\sin(0.3^\circ) = 5.2360\times10^{-3}$,
$H = 10^{5}/(8995.8 \times 5.2360\times10^{-3}) = 10^{5}/47.10 = 2.123\times10^{3}$
m.

**(b)** $\sin(1^\circ) = 1.74524\times10^{-2}$,
$H = 10^{5}/156.996 = 637.0$ m.

**(c)** $\sin(3^\circ) = 5.23360\times10^{-2}$,
$H = 10^{5}/470.83 = 212.4$ m.

**(d)** The model reproduces the inverse-sine dependence of thickness on surface
slope — kilometres thick on a plain, hundreds of metres on a steep flank — and it
ignores basal sliding, longitudinal stress gradients and the concentration of
shear near the margin, so it is an order-of-magnitude estimate rather than a
profile.

---

## ★3 — Isostasy and relaxation time

**(a)** $\Delta h = (917/3300)(1500) = 416.8$ m, i.e. 27.8 per cent of the ice
thickness.

**(b)** $k = 2\pi/5\times10^{5} = 1.2566\times10^{-5}$ m⁻¹, so
$\tau = \frac{2(10^{21})(1.2566\times10^{-5})}{3300 \times 9.81}
= \frac{2.5133\times10^{16}}{32373} = 7.763\times10^{11}$ s
$= 2.460\times10^{4}$ yr.

**(c)** $\tau = 1.230\times10^{4}$ yr.

**(d)** $\tau \propto \eta$ and $\tau \propto 1/\lambda$: relaxation is *faster*
for short wavelengths (a small load is supported and released quickly) and slower
for long ones. That wavelength dependence is what makes the spatial pattern of
present-day rebound a constraint on mantle viscosity rather than merely on its
magnitude.

---

## ★★4 — Reflection coefficients

**(a)** $Z_1 = 2000 \times 1700 = 3.400\times10^{6}$ kg m⁻² s⁻¹;
$Z_2 = 2650 \times 5500 = 1.4575\times10^{7}$ kg m⁻² s⁻¹.

$$R = \frac{1.4575\times10^{7} - 3.400\times10^{6}}
{1.4575\times10^{7} + 3.400\times10^{6}}
= \frac{1.1175\times10^{7}}{1.7975\times10^{7}} = 0.6217 .$$

**(b)** $R^{2} = 0.3865$, i.e. **38.65 per cent** of the incident energy is
reflected. For a deep crustal reflection with $R = 0.05$, $R^{2} = 2.5\times10^{-3}$
(0.25 per cent), so this shallow contact returns about 155 times more energy.
That is the quantitative reason shallow seismic surveys are "easy": the contrasts
are large and the geometric spreading is small.

**(c)** $Z_{\text{dry}} = 1900 \times 900 = 1.710\times10^{6}$;
$Z_{\text{sat}} = 3.400\times10^{6}$; so
$R = (3.400 - 1.710)/(3.400 + 1.710) = 1.690/5.110 = 0.3307$. (The demo reports
$0.3035$ for its own property pair; the difference is entirely in the assumed
velocities, which is the point of quoting them.) A water table inside one
lithology produces a reflection that is a substantial fraction of the
sediment–bedrock one.

**(d)** The acoustic-impedance contrast across an ice bed is very small (here
$R = 0.043$ in amplitude and $1.8\times10^{-3}$ in energy), so a reflection survey
would need a large source and long stacking to see it. Radar instead uses the
**dielectric** contrast: cold ice has $\varepsilon_r \approx 3.17$ while water,
wet till and most rock are far higher, so the reflection coefficient at the bed is
large at radio frequencies. The observable is different, and it is the dielectric
one that is large.

---

## ★★5 — The Stefan active-layer depth

**(a)** $t = 5\ \text{months} = \frac{5}{12}(3.15576\times10^{7})
= 1.3149\times10^{7}$ s.

$$X = \sqrt{\frac{2(1.8)(18)(1.3149\times10^{7})}{3.34\times10^{5}\times1000}}
= \sqrt{\frac{8.5206\times10^{8}}{3.34\times10^{8}}} = \sqrt{2.5511} = 1.597\ \mathrm{m}.$$

**(b)** $X \propto \sqrt{t}$, so
$X = 1.597\sqrt{8/5} = 1.597 \times 1.2649 = 2.020$ m.

**(c)** $X \propto \sqrt{\Delta T}$, so
$X = 1.597\sqrt{12/18} = 1.597 \times 0.8165 = 1.304$ m.

**(d)** $X \propto \sqrt{t}$ and $X \propto \sqrt{\Delta T}$: a 60 per cent longer
winter deepens the active layer by 26 per cent, not 60 per cent. Two assumptions
that a real soil violates: **constant thermal conductivity** (it changes sharply
between frozen and unfrozen states, and with moisture content) and **a step
surface temperature with latent heat dominant** (the real surface temperature
oscillates, and sensible heat is not negligible where the soil is dry).

---

## ★★6 — Radar in ice

**(a)** $v = c/\sqrt{\varepsilon_r} = 2.99792458\times10^{8}/\sqrt{3.17}
= 1.6838\times10^{8}$ m s⁻¹.

**(b)** Two-way travel time $= 2(250)/1.6838\times10^{8} = 2.967\times10^{-6}$ s
$= 2.967\ \mu$s.

**(c)** $\lambda = v/f = 1.6838\times10^{8}/5\times10^{7} = 3.368$ m, so the
quarter-wavelength resolution is $0.842$ m.

**(d)** Resolution improves as the wavelength falls (higher frequency) while
attenuation and scattering in ice grow with frequency, so penetration depth falls.
The trade-off is set by the **wavelength in (c)** — it determines the resolution —
while the *time window* in (b) sets how long a record must be and how the gains
must be applied. A 100 MHz survey resolves about a metre at a few hundred metres
depth; a 5 MHz survey penetrates kilometres at a resolution of tens of metres.

---

## ★★★7 — Reading the demonstration

Quoted output from `glacial_landforms_demo.py`, reference case $H = 1000$ m,
$\alpha = 1^\circ$:

**(a)** $\tau_b = 1.5700\times10^{5}$ Pa; $\bar u_d = 4.6437\times10^{-6}$ m s⁻¹
$= 146.54$ m yr⁻¹. At 0, $-10$, $-20$ and $-30\,^\circ$C:
146.543, 53.698, 18.176 and 5.628 m yr⁻¹.

**(b)** 2547.7 m at 0.25°, 1273.9 m at 0.5°, 637.0 m at 1°, 318.5 m at 2°,
127.5 m at 5°; $\tau_b = 1.0\times10^{5}$ Pa in every case, by construction.

**(c)** 277.88 m, 555.76 m, 833.64 m — 27.79 per cent of the load at every
thickness, because the ratio is density-only.

**(d)** 123.01 kyr at 100 km, 12.30 kyr at 1000 km, 4.10 kyr at 3000 km.

**(e)** Till over shale $R = +0.3701$; limestone $+0.5705$; granite $+0.6231$;
ice $+0.0426$ (all relative to the demo's till). Dry versus saturated till:
$R = +0.3035$.

**(f)** $v = 1.6838\times10^{8}$ m s⁻¹; travel times 1.188, 5.939 and
23.756 µs at 100, 500 and 2000 m; quarter-wavelength resolution 0.421 m at
100 MHz.

**(g)** Stefan depth 1.4580 m; frost-heave upper bounds 27.0, 54.0 and 108.0 mm
for 0.30, 0.60 and 1.20 m of water freezing in place.

**(h)** The driving stress, the deformation velocity, the perfect-plasticity
thickness, the Airy ratio, the relaxation time, the reflection coefficients, the
radar travel times and the Stefan depth are **computed from derived formulas**.
The Arrhenius temperature dependence of $A$ and the sliding multiplier are
**parameterisations** with declared coefficients. The densities, velocities,
permittivities, viscosities, yield stress and thermal conductivity are **nominal
literature values**, entered as inputs and not measured here. Any of the computed
numbers changes if any of the nominal ones changes, and the sensitivity is not
uniform: velocity is linear in $A$ and in $H^{4}$, so the thickness and
temperature inputs dominate.

---

## ★★★8 — Interpretation and its limits

**(a)** Three plausible origins for a 60 m deep, 400 m wide, elongate bedrock
depression beneath 30 m of till:

1. **Subglacial overdeepening / rock basin** scoured along a fast-flow corridor.
   Discriminating observation: striations or a roche moutonnée asymmetry on the
   flanks, with the long axis parallel to the regionally mapped ice-flow
   direction.
2. **Tunnel valley or meltwater channel** cut by subglacial water. Discriminating
   observation: a fill of sorted glaciofluvial sand and gravel, and a linear
   continuity with an esker or a larger tunnel valley up-ice.
3. **Pre-glacial fluvial valley exhumed or deepened by ice.** Discriminating
   observation: a fill with a weathering profile, or an orientation inherited
   from the pre-glacial drainage that is oblique to the glacial flow direction.

Any of the three also requires checking that the depression is not a bedrock
structure — a fault-bounded graben or a karst cavity — which is a fourth
hypothesis that a gravity and a seismic survey together can usually exclude.

**(b)** A sand-and-gravel unit under clay has similar density and similar P-wave
velocity to the clay (both are water-saturated granular or fine-grained
sediments, and the bulk modulus of the pore fluid sets much of $v_P$), so the
acoustic impedance contrast is small and the reflection may be below the noise.
Resistivity and electromagnetic methods instead use the **electrical
conductivity contrast**: the clean permeable sand has a much higher resistivity
(and lower clay content) than the clay, a difference of one to two orders of
magnitude, which no elastic method can match.

**(c)** Two reasons the internal architecture of a till sheet controls groundwater
more than its total thickness:

1. **Connectivity, not volume.** If the permeable sand and gravel lenses are
   isolated by till, there is no through-flow regardless of how much permeable
   material the sheet contains; a modest volume that forms a connected network
   yields much more water.
2. **Hydraulic gradient.** A till sheet with a laterally continuous
   low-permeability base changes where the head is directed and how recharge
   reaches the permeable unit; the boundary geometry, not the thickness, sets the
   flow path.

A method that can resolve the architecture: **ground-penetrating radar** with a
suitable centre frequency, or **multichannel surface-wave analysis**, both of
which respond to contrasts *within* the saturated sediment column rather than to
its overall thickness.

**(d)** The age is likely to be **too young**. A sand plain has a much larger
hillslope diffusivity than a boulder-rich moraine crest, so calibrating $\kappa$
on the sand plain overestimates the value that applies to the moraine. From
$t = h^{2}/(4\pi\kappa s_{\max}^{2})$ the age scales as $1/\kappa$, so an
over-estimated diffusivity gives an under-estimated age.
