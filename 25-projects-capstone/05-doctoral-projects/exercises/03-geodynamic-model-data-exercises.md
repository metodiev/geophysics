# Exercises — 25-05-03 Project: Geodynamic Model-Data Comparison

Attempt these before reading the
[solutions](./03-geodynamic-model-data-solutions.md). The project is
[03 Geodynamic Model-Data Comparison](../03-geodynamic-model-data.md); all numbers
below are **SYNTHETIC** and printed by
[`code/geodynamic_model_demo.py`](../code/geodynamic_model_demo.py):

| Quantity | Value |
|---|---|
| constants | $\kappa = 10^{-6}$ m²/s, $\alpha = 3.0\times10^{-5}$ K⁻¹, $T_m = 1300$ °C, $\rho_m = 3300$, $\rho_w = 1030$ kg/m³, $k = 3.2$ W/m/K |
| half-space law | $d = d_\text{ridge} + a\sqrt t$, $a_\text{theory} = 359.4$ m/Myr^0.5 |
| heat-flow law | $q = C/\sqrt t$, $C = 417.8$ mW/m²/Myr^0.5 |
| plate model | base $T = T_m$ at $L = 95$ km; saturation subsidence 2693 m |
| synthetic data | 60 ages 2–160 Myr; depth 2961–5284 m with 100 m rms noise; heat flow 279.7–40.4 mW/m² with 5% noise |
| half-space fit, 2–160 Myr | $d_\text{ridge} = 3426 \pm 39$ m, $a = 161.7 \pm 4.4$, residual rms 236.5 m, $\chi^2/\text{dof} = 5.59$ |
| plate fit, 2–160 Myr | $L = 94.0$ km, $d_\text{ridge} = 2485$ m, $d_\text{sat} = 2695$ m, residual rms 102.0 m, $\chi^2/\text{dof} = 1.04$ |
| half-space fit, 2–39 Myr | noisy $a = 323.8 \pm 18.1$, noiseless $a = 336.8 \pm 18.1$ |
| heat flow fit | $C = 420.7$, residual 5.45 mW/m², $\chi^2/\text{dof} = 5.44$; plate model with $L$ free gives $L = 94.0$ km, $\chi^2/\text{dof} = 0.76$ |
| parameter correlation | $d_\text{ridge}$–$a$: $-0.94$ (full range), $-0.95$ (2–39 Myr) |

## ★ Foundational

**★1.** Derive $a = 359.4$ m/Myr^0.5 from $T(z,t) = T_m\,\mathrm{erf}(z/2\sqrt{\kappa t})$
and check it against the printed value. State which physical constants appear only as
a product.

**★2.** Derive the saturation subsidence of the plate model,
$d_\text{sat} = \rho_m\alpha T_m(L/2)/(\rho_m - \rho_w)$, and evaluate it for
$L = 95$ km.

**★3.** Derive $C = kT_m/\sqrt{\pi\kappa t_\text{Myr}}$ for the heat flow and check
it against the printed 417.8 mW/m²/Myr^0.5. Explain why $C$ and $a$ are related by
$a/C = 2\alpha\rho_m\sqrt{\kappa t_\text{Myr}}/(k(\rho_m-\rho_w))\cdot$something —
that is, work out the ratio and say what it depends on.

## ★★ Applied

**★★4.** The half-space fit over 2–160 Myr gives $a = 161.7$ against a theoretical
359.4. Compute the ratio, and compute how much of the difference is explained by
fitting over a range in which the model saturates: at 160 Myr the half-space
prediction is $359.4\sqrt{160} = 4546$ m while the plate model gives 2684 m; compute
the two curves at 40 and 160 Myr and explain the sign of the fit's bias.

**★★5.** The half-space depth residuals average $-192$, $+205$ and $-233$ m over the
youngest, middle and oldest thirds of the age range. Sketch the sign pattern this
implies, and state what physical feature of the plate model produces it.

**★★6.** Using the noisy and noiseless 2–39 Myr fits ($a = 323.8 \pm 18.1$ and
$336.8 \pm 18.1$), split the total discrepancy from the theoretical 359.4 into a model
component and a noise component. Which is larger, and what does the answer imply for
the conclusion "the half-space model is valid to 40 Myr"?

**★★7.** Both the bathymetry and the heat flow give $L = 94.0$ km at a 1 km grid
resolution. Compute the saturation subsidence for $L = 94$ and $L = 95$ km and state
whether the 1 km difference is detectable at this noise level. Then state what
actually determines the precision of $L$ (it is not the grid step).

**★★8.** Compute $q$ from the half-space law and from the plate model at 10, 50 and
150 Myr, compare with the printed observed values 124.5, 64.1 and 47.7 mW/m², and
state at which age the two models diverge beyond the 5% noise.

## ★★★ Research-oriented

**★★★9.** The half-space coefficient fixes only the product $\alpha T_m$. Design a
study that determines $\alpha$ and $T_m$ separately using geophysical observables,
naming for each observable which combination it measures, why the Jacobians are not
parallel, the resolution you would claim for each parameter, and the synthetic test
that would demonstrate the separation is real rather than an artefact of an assumed
value. A design that fixes $\alpha$ at a laboratory value and then calls $T_m$
"measured" is a failed answer.
