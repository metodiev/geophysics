# Solutions — 05-04-03 Gassmann Fluid Substitution

> Numbers marked *verified* were computed.

---

## ★1

$K_\text{sat} = K_\text{dry} + (1-K_\text{dry}/K_\text{min})^2/
[\phi/K_\text{fl} + (1-\phi)/K_\text{min} - K_\text{dry}/K_\text{min}^2]$,
all moduli in Pa, $\phi$ dimensionless; $G_\text{sat} = G_\text{dry}$.

---

## ★2

(a) $K_\text{fl} = K_\text{min}$ gives $K_\text{sat} = K_\text{min}$ exactly
(tests the algebra). (a′) $K_\text{fl}\to\infty$ gives a finite $K_\text{sat}$
*above* $K_\text{min}$ (tests the limit and reveals that a bulk modulus is not
bounded by its constituents). (b) $K_\text{fl}\to0$ gives
$K_\text{sat} = K_\text{dry}$ (tests the reference state). (c) $G$ unchanged
(tests the shear branch).

---

## ★3

At low frequency the fluid cannot sustain shear stress and its shear stiffness is
zero, so adding it to the pores cannot change the rock's shear response; only
volume changes involve the fluid.

---

## ★★4 *(verified)*

Numerator: $(1-18.5/37)^2 = (0.5)^2 = 0.25$.
Denominator: $0.2/2.2 + 0.8/37 - 18.5/37^2
= 0.0909091 + 0.0216216 - 0.0135135 = 0.0990172$.
$K_\text{sat} = 18.5 + 0.25/0.0990172 = 18.5 + 2.52481 = 21.0248$ GPa. ✓
Matches the tabulated value to five figures.

---

## ★★5 *(verified)*

$\rho_\text{dry} = 0.8(2650) = 2120$ kg/m³; $\rho_\text{sat} = 2120+0.2(1000)
= 2320$ kg/m³.
$V_s^\text{sat} = \sqrt{22\times10^{9}/2320} = \sqrt{9.4828\times10^{6}}
= 3079.4$ m/s.
$V_s^\text{dry} = \sqrt{22\times10^{9}/2120} = \sqrt{1.03774\times10^{7}}
= 3221.4$ m/s.
Ratio $= 3079.4/3221.4 = 0.955925$;
$\sqrt{2120/2320} = \sqrt{0.913793} = 0.955925$. ✓

---

## ★★6

Set $K_\text{fl} = K_\text{min}$:
denominator $= \phi/K_\text{min} + (1-\phi)/K_\text{min} - K_\text{dry}/K_\text{min}^2
= 1/K_\text{min} - K_\text{dry}/K_\text{min}^2
= (K_\text{min}-K_\text{dry})/K_\text{min}^2$.
Numerator $= (K_\text{min}-K_\text{dry})^2/K_\text{min}^2$.
Ratio $= K_\text{min}-K_\text{dry}$, so
$K_\text{sat} = K_\text{dry} + K_\text{min} - K_\text{dry} = K_\text{min}$. ✓

---

## ★★7

Physically, an incompressible pore fluid prevents volumetric compaction of the
pores, so the rock resists compression through the fluid. $K_\text{sat}$ exceeds
$K_\text{min}$ because the mineral itself is compressible: the *composite*
(mineral plus rigid fluid filling the pores) has a higher effective bulk modulus
than the mineral alone. This shows that a bulk modulus is not bounded by the
moduli of its constituents — the Voigt bound for a two-phase mixture with an
incompressible phase is itself infinite.

---

## ★★★8

Expected: invert
$K_\text{dry} = [K_\text{sat}(\phi K_\text{min}/K_\text{fl} + 1-\phi) - K_\text{min}]/
[\phi K_\text{min}/K_\text{fl} + K_\text{sat}/K_\text{min} - 1-\phi]$, then apply
Gassmann forward with the new fluid.

The dominant uncertainty is usually $K_\text{fl}$ for the *new* fluid (fluid
moduli are often estimated, not measured) and $\phi$ for the rock, followed by
$K_\text{min}$. A 5% error in $K_\text{fl}$ for a soft gas can shift $V_p$ by a
few percent, comparable to the effect being modelled. Assumptions to state: low
frequency, uniform saturation, homogeneous mineral, known $K_\text{dry}$.

---

## ★★★9

$D = kK_f/(\mu\phi)$ has units
$\mathrm{m^2\cdot Pa/(Pa\,s)} = \mathrm{m^2/s}$ ✓. With $k = 10^{-14}$ m²,
$K_f = 2.2$ GPa, $\mu = 10^{-3}$ Pa·s, $\phi = 0.2$:
$D = (10^{-14})(2.2\times10^{9})/(10^{-3}\cdot0.2) = 2.2\times10^{-5}/2\times
10^{-4} = 0.11$ m²/s. For a patch length $L = 0.1$ m,
$t \sim L^2/D = 0.01/0.11 = 0.091$ s. The Gassmann limit requires the seismic
period $\gg t$, i.e. $f \ll 1/t \approx 11$ Hz. Above that frequency the fluid
pressure is not equilibrated and velocities approach the *unrelaxed* (stiffer)
limit for $V_p$, which is *higher* than the Gassmann prediction — i.e. Gassmann
underestimates $V_p$ at high frequency, and the difference grows with frequency
until the unrelaxed limit is reached.
