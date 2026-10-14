# Exercises — 15-04-02 Gas Hydrates: Occurrence, Geophysics and Resource Potential

Attempt these before the [solutions](./02-gas-hydrates-solutions.md). The lesson
is [02 Gas Hydrates](../02-gas-hydrates.md). All models and data are **SYNTHETIC**
teaching values; the model constants are those printed by
`code/gas_hydrates_demo.py`.

## ★ Foundational

**★1.** Compute the methane mass fraction and the gas yield $Y$ for a hydrate of
density $920\ \mathrm{kg\,m^{-3}}$ at 90% cage occupancy, using the structure-I
cell of 46 water molecules and 8 guest sites, $M_{\mathrm{CH_4}}=16.043\
\mathrm{g\,mol^{-1}}$, $M_{\mathrm{H_2O}}=18.015\ \mathrm{g\,mol^{-1}}$ and
$V_m=22.414\ \mathrm{L\,mol^{-1}}$.

**★2.** Compute the dissociation pressure at $280.15\ \mathrm{K}$ from the
lesson's Clausius–Clapeyron model, and the hydrostatic depth at which that
pressure occurs (use $\rho_w=1028\ \mathrm{kg\,m^{-3}}$, $g=9.81\
\mathrm{m\,s^{-2}}$ and $p_{\text{atm}}=101325\ \mathrm{Pa}$).

**★3.** Compute the Reuss-average pore-fluid modulus and the saturated density for
$S_h=0.30$, $\phi=0.35$, with water $K_w=2.2\ \mathrm{GPa}$, hydrate
$K_h=7.9\ \mathrm{GPa}$, $\rho_w=1030$, $\rho_h=920$, $\rho_s=2650\
\mathrm{kg\,m^{-3}}$.

## ★★ Applied

**★★4.** Using the lesson's Gassmann parameters ($K_{\text{dry}}=1.0\
\mathrm{GPa}$, $G_{\text{dry}}=0.6\ \mathrm{GPa}$, $K_s=36\ \mathrm{GPa}$,
$\phi=0.35$) and your answer to ★3, compute $K_{\text{sat}}$ and $v_p$ for
$S_h=0.60$ in the pore-filling model. Compare with the interpolation of the
lesson's table between 0.5 and 0.7 and state the agreement.

**★★5.** Compute the gas in place for a model accumulation with $A=50\
\mathrm{km^2}$, $h=30\ \mathrm{m}$, $\phi=0.30$, $S_h=0.50$ and
$Y=168.6\ \mathrm{m^3\,m^{-3}}$, in both $\mathrm{m^3}$ (STP) and
$10^{9}\ \mathrm{ft^3}$.

**★★6.** For 1500 m water depth, a seafloor temperature of $3\
^\circ\mathrm{C}$ and a gradient of $35\ \mathrm{^\circ C\,km^{-1}}$, find the
base of the stability zone to within $\pm10\ \mathrm{m}$ by testing depths
against the phase-boundary model. Show the two bracketing depths and the
comparison at each.

## ★★★ Research-oriented

**★★★7.** A hydrate-bearing interval has $v_p=2300\ \mathrm{m\,s^{-1}}$ and
$v_s=560\ \mathrm{m\,s^{-1}}$ from an ocean-bottom survey at $\phi=0.35$.
**(a)** Compute $v_p/v_s$ and the Poisson ratio. **(b)** State which of the
lesson's two rock-physics models this is consistent with, with the arithmetic
that decides it. **(c)** State the one remaining model choice that could still
mislead you, and the measurement that removes it.

**★★★8.** Design a programme to estimate a gas-in-place volume with a stated
uncertainty of a factor of three. For each required quantity (area, thickness,
porosity, saturation, yield, recovery) state how you would measure or bound it,
whether it is measured or modelled, and which one dominates the final range.
Conclude with the honest statement you would publish, including the one quantity
for which no geophysical measurement exists.
