# Exercises — 14-03-03 Seismic Velocity vs Saturation and Gassmann

Attempt before the [solutions](./03-seismic-velocity-saturation-solutions.md).
Lesson:
[03 Seismic Velocity vs Saturation and Gassmann](../03-seismic-velocity-saturation.md).
All models are **SYNTHETIC** teaching values. Standard fluid and mineral
constants: $K_w = 2.20\ \mathrm{GPa}$, $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$,
$K_g = 1.0\times10^{-4}\ \mathrm{GPa}$, $\rho_g = 1.2\ \mathrm{kg\,m^{-3}}$.

## ★ Foundational

**★1.** A synthetic sandstone has $\phi = 0.25$,
$K_\text{dry} = 9.00\ \mathrm{GPa}$, $\mu_\text{dry} = 8.00\ \mathrm{GPa}$,
$K_\text{min} = 36.00\ \mathrm{GPa}$, $\rho_\text{min} = 2650\ \mathrm{kg\,m^{-3}}$.
Compute $K_\text{sat}$, $\rho$, $V_p$ and $V_s$ at $S_w = 1$ (uniform
saturation).

**★2.** Compute the Wood fluid modulus for $S_w = 0.5$, $0.9$ and $1.0$ and
comment on why the value at $S_w = 0.9$ is still so far below $K_w$.

**★3.** State Gassmann's prediction for the shear modulus and explain in one
sentence why the fluid does not affect shear stiffness. Then compute $V_s$ for
the model of ★1 at $S_w = 0$ and $S_w = 1$ and give the change in
$\mathrm{m\,s^{-1}}$.

## ★★ Applied

**★★4.** For the lesson's model ($\phi = 0.30$, $K_\text{dry} = 8.00\ \mathrm{GPa}$,
$\mu_\text{dry} = 7.00\ \mathrm{GPa}$), compute $K_\text{sat}$ at $S_w = 1$ and at
$S_w = 0$, then compute the **patchy** $K_\text{sat}$ at $S_w = 0.5$ and the
resulting $V_p$.

**★★5.** Using the same model, compute $V_p$ at $S_w = 0.5$ under uniform and
patchy mixing and state the difference in $\mathrm{m\,s^{-1}}$. Which assumption
is the safer default when nothing else is known, and why?

**★★6.** Using the same model, find the water saturation at which the
uniform-saturation $V_p$ has fallen $100\ \mathrm{m\,s^{-1}}$ below the dry
value, and find the saturation at which it returns to the dry value. Comment on
the asymmetry.

**★★7.** Verify the analytic limit $K_\text{sat} = K_\text{min}$ when
$K_\text{fl} = K_\text{min}$, by substituting into the Gassmann denominator
rather than by appeal to the demonstration.

## ★★★ Research-oriented

**★★★8.** A field $V_p$ of $2.90\ \mathrm{km\,s^{-1}}$ is reported in the lesson's
model as $\phi = 0.30$ (uniform). **(a)** Show that the patchy curve cannot
produce this value at any saturation. **(b)** Find a pair $(K_\text{dry},
S_w)$ with uniform saturation that does reproduce it. **(c)** State the
additional measurement that resolves the ambiguity and the quantity it must
constrain. **(d)** Explain why the ambiguity would *not* be resolved by a more
accurate $V_p$.

**★★★9.** Design a laboratory programme to test whether a sandstone's fluid
sensitivity follows uniform or patchy mixing. **(a)** State the saturation
protocol that produces each geometry and why it does. **(b)** State the
frequency band of the measurement and why the Gassmann limit requires it.
**(c)** Specify the plot and the expected signature of each model. **(d)** State
one way the experiment could produce an intermediate answer and what that would
imply.
