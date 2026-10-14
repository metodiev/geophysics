# Solutions — 05-04-01 Porosity, Density and Velocity Relationships

> Numbers marked *verified* were computed.

---

## ★1

Mass $= (1-\phi)V\rho_m + \phi V\rho_f$; divide by $V$:
$\rho_b = (1-\phi)\rho_m+\phi\rho_f$. Both terms kg m⁻³. ✓

---

## ★2

Porosity: $10^{-3}$ to 0.5. Grain density: a factor of ~1.5. $V_p$: a factor of
2–4. $V_s$: a factor of 2–5. A single "typical" value misrepresents the spread
as certainty and destroys the information that matters most — the possibility of
an end-member.

---

## ★3

$V_s^\text{sat}/V_s^\text{dry} = \sqrt{\rho_\text{dry}/\rho_\text{sat}}$. A
violation means one of Gassmann's assumptions fails: patchy saturation, a
softening clay, high frequency, or an inaccurate dry-frame modulus.

---

## ★★4 *(verified)*

Dry-ish: $\rho_b = 0.82(2650)+0.18(1020) = 2173+183.6 = 2356.6$ kg/m³.
With $S_w = 0.3$: $\rho_f = 0.3(1020)+0.7(250) = 306+175 = 481$ kg/m³, so
$\rho_b = 2173+0.18(481) = 2173+86.6 = 2259.6$ kg/m³. The partial-saturation
change is $-97$ kg/m³, a 4.1% density reduction.

---

## ★★5 *(verified)*

$\Delta\rho_b = 0.25(180-1050) = -217.5$ kg/m³. Since $G$ is unchanged,
$V_s \propto \rho^{-1/2}$, so $V_s$ **increases** by
$\sqrt{\rho_\text{dry}/\rho_\text{sat}}$; the lighter fluid raises $V_s$.

---

## ★★6

Porosity and frame stiffness. A rock with high porosity and a stiff mineral
assemblage can have the same bulk density as a low-porosity rock with dense
minerals, while the two frames differ greatly in $K$ and $G$. Density is
arithmetic; velocity is not a function of density.

---

## ★★7

Predicted 0.96 against measured 0.93: the measured $V_s$ is
$(0.96-0.93)/0.96 = 3.1\%$ lower than the density-only prediction. Candidate
mechanisms: (i) softening of the frame by compliant clay or by chemical
interaction with the fluid; (ii) patchy saturation, which produces a stiffer
effective fluid and therefore a *higher* $V_p$ while the frame — and hence the
$V_s$ discrepancy — reflects something else, or (iii) high-frequency squirt
effects. The sign of the discrepancy (measured lower) points to frame softening
rather than to an effective-fluid effect.

---

## ★★★8

Expected structure: $\rho_b$ uncertainty from $\phi$ dominates unless $\phi$ is
measured precisely; fluid-density uncertainty matters at high porosity; grain
density uncertainty contributes a few tens of kg/m³. For impedance
$Z = \rho V_p$, $\sigma_Z/Z = \sqrt{(\sigma_\rho/\rho)^2 + (\sigma_{V_p}/V_p)^2}$.
If $V_p$ is uncertain by 2% and $\rho$ by 1%, $Z$ is uncertain by 2.2%. A
saturation change producing a 1% impedance change is then **not detectable** —
the honest conclusion may be that 4-D is infeasible with the available
constraints, which is itself a valuable result.

---

## ★★★9

With a *fixed* frame (e.g. $K_\text{dry} = 12$ GPa at every $\phi$), the fluid
substitution effect is nearly independent of porosity and can even be largest at
low $\phi$ because the modulus contrast dominates. With a *porosity-dependent*
frame (e.g. $K_\text{dry} = K_\text{min}(1-\phi/\phi_c)$), the effect grows
monotonically with $\phi$ and the sign of $\Delta V_p$ can flip. The second is
physically meaningful: comparing rocks at different porosities means comparing
different frames, so the frame must change with the porosity. Holding it fixed
compares a rock with a rock that does not exist.
