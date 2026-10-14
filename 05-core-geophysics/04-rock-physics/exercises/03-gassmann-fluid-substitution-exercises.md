# Exercises — 05-04-03 Gassmann Fluid Substitution

Difficulty: ★ · ★★ · ★★★.

---

## ★ Foundational

**★1.** Write Gassmann's equation and name every symbol with its unit.

**★2.** State the three exact limits and what each tests.

**★3.** Explain in one sentence why $G_\text{sat} = G_\text{dry}$.

---

## ★★ Applied

**★★4.** With $K_\text{min} = 37$ GPa, $K_\text{dry} = 18.5$ GPa,
$K_\text{fl} = 2.2$ GPa and $\phi = 0.20$, compute $K_\text{sat}$ by hand and
compare with the tabulated 21.0248 GPa.

**★★5.** With $\rho_\text{min} = 2650$, $\phi = 0.20$ and fluid density
1000 kg/m³, compute $\rho_\text{sat}$ and then $V_s$ for $G = 22$ GPa. Verify
$V_s^\text{sat}/V_s^\text{dry} = \sqrt{\rho_\text{dry}/\rho_\text{sat}}$.

**★★6.** Show that setting $K_\text{fl} = K_\text{min}$ in Gassmann gives
$K_\text{sat} = K_\text{min}$ algebraically.

**★★7.** State what happens physically at $K_\text{fl}\to\infty$ and why
$K_\text{sat}$ exceeds $K_\text{min}$.

---

## ★★★ Research-oriented

**★★★8.** Fluid substitution workflow. Given a *saturated* measurement
($K_\text{sat}$, $G$, $\rho$, $\phi$) and the mineral and fluid moduli,
(i) invert Gassmann for $K_\text{dry}$, (ii) substitute a new fluid, and (iii)
report the new $V_p$ and $V_s$. Then perturb all inputs by 5% and report which
one dominates the final $V_p$ uncertainty. State every assumption.

**★★★9.** Test Gassmann's domain of validity. For a stated rock, compute the
pore-fluid pressure diffusion time $t \sim L^2/D$ with $D = kK_f/(\mu\phi)$ for
a stated permeability, viscosity and patch length $L$, and compare it with the
seismic period. Report the frequency above which the equilibrated-fluid
assumption fails, and state what happens to the predicted velocities above it.
