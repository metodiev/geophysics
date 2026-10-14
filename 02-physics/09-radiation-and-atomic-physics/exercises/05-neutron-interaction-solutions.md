# Solutions — 02-09-05 Neutron Interactions and Borehole Nuclear Measurements

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Every cross section below is a **tabulated** 2200 m/s value from the evaluated
neutron-data compilations, so each use needs a citation and an edition. The
collision kinematics are exact; the tool responses are declared **model** inputs.
No answer below mixes the three.

---

## ★1 — Two thermal conventions

**(a)** $E = \tfrac12m_nv^2 = \tfrac12 \times 1.674\,927\,5 \times 10^{-27}
\times 2200^2 = 4.0533 \times 10^{-21}$ J. Dividing by
$e = 1.602\,176\,634 \times 10^{-19}$ C gives $\mathbf{0.0253}$ eV.

**(b)** $\tfrac32k_BT = 1.5 \times 1.380\,649 \times 10^{-23} \times 293.6 =
6.0804 \times 10^{-21}$ J = $\mathbf{0.0380}$ eV.

**(c)** The ratio is $1.500$. A tabulated "thermal" cross section is the value at
the **2200 m/s reference speed**, which is the most probable speed of a
Maxwellian gas near 20 °C; it is not the mean energy, which is 1.5 times larger.
The demo prints 0.025299 eV, 0.037951 eV and a ratio of 1.500097.

**(d)** A $1/v$ absorber has $\sigma \propto 1/v$, so the cross section is largest
for the slowest neutrons. Averaging $1/v$ over a Maxwellian distribution weights
the *slow* end more than the distribution of speeds weights it, and the resulting
effective cross section for a $1/v$ absorber is about 0.9 times the 2200 m/s
value. Equivalently: the tabulated value is defined at a speed, while the real
population is spread over speeds, and the average of a convex function of $v$ is
not its value at the most probable $v$.

---

## ★2 — Slowing down

**(a)** For $A = 1.008$:
$\frac{(A-1)^2}{2A}\ln\frac{A-1}{A+1} = \frac{6.4 \times 10^{-5}}{2.016}
\ln(0.007\,937) = 3.17 \times 10^{-5} \times (-4.836) = -1.53 \times 10^{-4}$,
so $\xi = \mathbf{0.99985}$. For $A = 12.011$:
$\frac{121.26}{24.022}\ln(0.846\,13) = 5.0478 \times (-0.167\,05) = -0.8432$,
so $\xi = \mathbf{0.1568}$.

**(b)** $4A/(1+A)^2$: hydrogen $\frac{4.032}{4.032} = \mathbf{0.999\,98}$;
carbon $\frac{48.044}{169.27} = \mathbf{0.2838}$.

**(c)** $\ln(4.5 \times 10^6/0.025) = \ln(1.8 \times 10^8) = \mathbf{19.008}$.

**(d)** Hydrogen: $19.008/0.99985 = \mathbf{19.0}$ collisions. Carbon:
$19.008/0.1568 = \mathbf{121}$ collisions. Hydrogen moderates far better per
collision — by a factor of 6.4 — because a head-on collision with an equal-mass
nucleus can remove all the neutron's energy. The demo prints 0.99982, 0.15763 and
19.0, 120.6 respectively; the small differences are from the molar masses used.

---

## ★3 — Water

**(a)** $\Sigma_a = N\sigma_a$:
hydrogen $6.6857 \times 10^{22} \times 0.332 \times 10^{-24} = 0.02220$ cm⁻¹;
oxygen $3.3429 \times 10^{22} \times 0.00019 \times 10^{-24} =
6.35 \times 10^{-6}$ cm⁻¹. Total $\mathbf{0.02220}$ cm⁻¹ — the oxygen
contribution is $3 \times 10^{-4}$ of it.

**(b)** $1/0.02220 = \mathbf{45.0}$ cm.

**(c)** $\Sigma_s$: hydrogen $6.6857 \times 10^{22} \times 20.4 \times 10^{-24} =
1.3639$ cm⁻¹; oxygen $3.3429 \times 10^{22} \times 4.232 \times 10^{-24} =
0.1415$ cm⁻¹. Total $\mathbf{1.5054}$ cm⁻¹, so the scattering mean free path is
$1/1.5054 = \mathbf{0.664}$ cm. The demo prints 45.0 cm and 0.66 cm.

**(d)** The scattering mean free path is 68 times shorter than the absorption mean
free path, so a thermal neutron in water is scattered tens of times before it is
captured. That is what makes a *diffusion* description workable: the neutron's
direction is randomised many times over before it disappears, so the population
can be described by a density and a flux rather than by tracking individual
trajectories. It is also why the thermal-neutron population spreads over tens of
centimetres, which is the geometric scale of a neutron log.

---

## ★★4 — Moderating ratio of graphite

**(a)** $N = 1.70 \times 6.022\,140\,76 \times 10^{23}/12.011 =
8.523 \times 10^{22}$ cm⁻³. Then
$\Sigma_a = 8.523 \times 10^{22} \times 0.0035 \times 10^{-24} =
2.983 \times 10^{-4}$ cm⁻¹ and
$\Sigma_s = 8.523 \times 10^{22} \times 4.74 \times 10^{-24} = 0.4040$ cm⁻¹.

**(b)** $\xi\Sigma_s/\Sigma_a = 0.1568 \times 0.4040/2.983 \times 10^{-4} =
\mathbf{213}$.

**(c)** The demo gives 213.5 for graphite, 62.2 for light water and 4476.6 for
heavy water. The ordering D₂O ≫ C > H₂O is the standard one; the absolute values
depend on the cross sections used, which is exactly why the compilation must be
cited.

**(d)** Hydrogen needs 19 collisions against deuterium's 26, so light water slows
a neutron faster per unit path length. But the absorption cross section of
hydrogen is 0.332 b against deuterium's 0.00051 b — a factor of 650 — and the
moderating ratio is dominated by that ratio in the denominator. A moderator's job
is to slow neutrons *before they are absorbed*, and on that criterion deuterium
wins by a factor of 70 despite needing more collisions. This is the quantitative
statement of why the "best moderator" is a different material depending on
whether the design is limited by volume or by neutron economy.

---

## ★★5 — The gas effect

**(a)** Hydrogen index of methane at $\rho = 0.10$ g cm⁻³:
$N_\mathrm{H} = 4 \times 0.10 \times 6.022\,140\,76 \times 10^{23}/16.043 =
1.5014 \times 10^{22}$ cm⁻³. For water:
$N_\mathrm{H} = 2 \times 1.00 \times 6.022\,140\,76 \times 10^{23}/18.015 =
6.6857 \times 10^{22}$ cm⁻³. So HI $= 1.5014/6.6857 = \mathbf{0.2246}$. The demo
prints 0.225.

**(b)** $\rho_b = (1 - \phi)\rho_\mathrm{ma} + \phi[S_g\rho_g + (1 - S_g)
\rho_w] = 0.75 \times 2.65 + 0.25 \times (0.5 \times 0.10 + 0.5 \times 1.00) =
1.9875 + 0.1375 = 2.1250$ g cm⁻³. Then
$\phi_D = (2.65 - 2.125)/(2.65 - 1.00) = 0.5250/1.65 = \mathbf{0.3182}$.

**(c)** $\phi_N = \phi[S_g\,\mathrm{HI}_g + (1 - S_g)\mathrm{HI}_w] =
0.25 \times (0.5 \times 0.2246 + 0.5 \times 1) = 0.25 \times 0.6123 =
\mathbf{0.1531}$. The separation is
$\phi_D - \phi_N = \mathbf{0.1651}$. The demo prints 0.3182, 0.1531 and 0.1651.

**(d)** Each reading alone could be wrong for several reasons — a wrong matrix in
$\phi_D$, a wrong salinity or shale correction in $\phi_N$ — and none of those
errors produces the *opposite* movement of the two readings. The physical reason
the two move oppositely is that gas is simultaneously *light* (raising $\phi_D$)
and *hydrogen-poor* (lowering $\phi_N$), and no single-cause error reproduces
both at once. That is why the diagnostic is the separation rather than either
value, and why the separation must be read together with a lithology indicator
(the Pe curve) before it is trusted.

---

## ★★6 — The photoelectric factor of calcite

**(a)** For $\mathrm{CaCO_3}$: $\sum n_iZ_i^4 = 20^4 + 6^4 + 3 \times 8^4 =
160\,000 + 1296 + 12\,288 = 173\,584$; $\sum n_iZ_i = 20 + 6 + 3 \times 8 = 50$.
Then $Z_\mathrm{eff} = (173\,584/50)^{1/3} = 3471.7^{1/3} =
\mathbf{15.14}$.

**(b)** $\mathrm{Pe} = (1.514)^{3.6} = e^{3.6\ln 1.514} = e^{1.4962} =
\mathbf{4.453}$.

**(c)** $2Z/A$: the electron count is 50 and the formula mass is
$40.078 + 12.011 + 3 \times 15.999 = 100.086$ g mol⁻¹, so
$2Z/A = 2 \times 50/100.086 = 0.9991$ and
$\rho_e = 0.9991 \times 2.71 = \mathbf{2.708}$ g cm⁻³.

**(d)** Against the published 5.08 the computed value is $-12.3$ per cent. The
computed values for water, quartz, calcite and dolomite are $-4.8$, $-6.3$,
$-12.3$ and $-15.3$ per cent from the published figures — a consistent bias
rather than a scatter. The ordering and the ratios are reproduced exactly:
quartz/calcite $= 1.697/4.453 = 0.381$ against $1.81/5.08 = 0.356$, and the
dolomite value falls between them as it must from the compositions. The
*ordering* is a stronger conclusion because it is forced by the $Z^{3.6}$ scaling
and by the formula units alone, whereas the absolute scale depends on which
definition of $Z_\mathrm{eff}$ (atom-, electron- or mass-weighted) and which
exponent a particular tool's calibration used. In a report, state the definition
and the exponent, and cite the tool's calibration.

---

## ★★★7 — Running the demo

**(a)** 2200 m s⁻¹ corresponds to 0.025299 eV; $\tfrac32k_BT$ at 293.6 K is
0.037951 eV; ratio 1.500097.

**(b)** Hydrogen: $\xi = 0.99982$, 19.0 collisions. Silicon: $\xi = 0.06955$,
273.3 collisions.

**(c)** Absorption mean free path 45.0 cm; scattering mean free path 0.66 cm.

**(d)** Light water 62.2, heavy water 4476.6, graphite 213.5, quartz rock 6.8.

**(e)** Gas at 0.20 g cm⁻³: HI = 0.449; liquid methane at 0.42 g cm⁻³:
HI = 0.943.

**(f)** Quartz: computed 1.697 against 1.81 published, $-6.3$ per cent. Dolomite:
computed 2.660 against 3.14 published, $-15.3$ per cent.

**(g)** At seawater salinity of about 35 g L⁻¹, about 35 per cent of
thermal-neutron captures are on chlorine.

**(h)** Exact: the collision kinematics ($\xi$, the maximum energy loss, the
number of collisions) and the arithmetic of $\Sigma = N\sigma$ and the hydrogen
index. Tabulated: every microscopic cross section and molar mass. Model: the
gas-effect proportionality between the neutron reading and the hydrogen index,
the neutron *porosity* response itself, and the Pe definition and exponent.

---

## ★★★8 — Interpretation

**(a)** Shales contain hydrogen in their clay mineral structures — hydroxyl
groups and interlayer water — so the hydrogen *number* density is high even
where the effective porosity is low. The neutron tool responds to hydrogen, so it
reads apparent porosity in proportion to total hydrogen, not to movable or
connected porosity. The independent measurement that corrects it is a **clay
indicator**: the natural gamma-ray log (clays carry potassium, uranium and
thorium), the Pe curve, or a density–neutron cross-plot whose shale point is
established from a local calibration. Without one of those, a shale interval's
apparent neutron porosity is not interpretable as a porosity at all.

**(b)** The **Pe** curve is least affected. It is a ratio of a low-energy to a
high-energy count rate, and both channels carry the same borehole attenuation
almost exactly, so the common part cancels. Barite changes the density log's
calibration because barite is heavy and photoelectrically active, and it changes
the neutron log through the fluid and the matrix; Pe survives because its
calibration is a ratio and because the photoelectric cross section, being a
strong function of $Z$, is dominated by the *formation* rather than by the mud
once the mud is a thin annulus. Naming the measurement that is robust to an
environmental effect, and saying *why* it is robust, is the standard way to
present a log interpretation.

**(c)** 1 g L⁻¹ of boron gives $\Sigma = (10^{-3} \times 6.022\,140\,76 \times
10^{23}/10.811) \times 767 \times 10^{-24} = \mathbf{0.0427}$ cm⁻¹, against
water's own 0.0222 cm⁻¹. So 1 g L⁻¹ of boron nearly doubles the absorption of the
fluid. Scaling linearly, 500 ppm gives 0.0214 cm⁻¹, which is 96 per cent of
water's own absorption — so a pore fluid containing 500 ppm of boron has twice
the capture cross section of pure water. That is why boron is used as a
neutron-absorbing tracer and why, conversely, a formation's neutron response can
be dominated by a trace constituent that no other log would notice.

**(d)** The porosity information in the count rate comes from the *contrast* in
moderating power between the pore fluid and the matrix. Water's moderating ratio
is 62 and a quartz matrix's is 6.8, so a change in water content changes the
thermal-neutron population measurably. But that contrast is with *quartz*: with a
matrix containing hydrogen (a shale) or a strong absorber (a boron- or
gadolinium-bearing mineral, or a chloride-rich fluid) the reference moderating
ratio and the absorption both change, so the same count rate corresponds to a
different porosity. The tool's calibration — to a limestone standard, in API
units — encodes one matrix and one fluid. Reading a porosity therefore requires
knowing that the matrix is the calibrated one, which is what the Pe measurement
is for, and that the fluid is the calibrated one, which is what the salinity
information is for.
