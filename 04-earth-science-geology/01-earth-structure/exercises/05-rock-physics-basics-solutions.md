# Solutions — 04-01-05 Density, Porosity, Permeability and Elastic Properties

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — Bulk density

**(a)** $\rho_\text{dry} = 0.85\times2650 = 2252.5$ kg/m³.

**(b)** $\rho_\text{sat} = 0.85\times2650 + 0.15\times1000 = 2402.5$ kg/m³.

**(c)** With gas at 100 kg/m³:
$\rho_\text{gas} = 2252.5 + 15 = 2267.5$ kg/m³.

**(d)** The contrast is $2402.5 - 2267.5 = 135$ kg/m³, which is 5.6 per cent of
the water-saturated density. That is the size of the signal a time-lapse gravity
or seismic survey is asked to detect when a gas cap replaces brine.

---

## ★2 — Voigt, Reuss and Hill

**(a)** $K_V = 0.30\times37 + 0.70\times21 = 11.1 + 14.7 = 25.8$ GPa.

**(b)** $1/K_R = 0.30/37 + 0.70/21 = 0.008108 + 0.033333 = 0.041441$, so
$K_R = 24.13$ GPa.

**(c)** $K_H = (25.8+24.13)/2 = 24.97$ GPa.

**(d)** The bound is 6.7 per cent wide. Physically, it is the range of effective
moduli consistent with the mineral fractions alone: the *geometry* of the
mixture — which mineral forms the load-bearing framework, how the grains are
packed, how much pore space is present — decides where inside the bound the true
value lies, and that information is not in the volume fractions.

---

## ★3 — Kozeny–Carman

**(a)** With $d = 1.5\times10^{-4}$ m and $\phi = 0.20$:
$$k = \frac{(1.5\times10^{-4})^2 \times 0.008}{180\times0.64}
= \frac{2.25\times10^{-8}\times0.008}{115.2} = 1.5625\times10^{-12}\ \text{m}^2.$$

**(b)** $1.5625\times10^{-12}/9.869\times10^{-13} = 1.58$ darcy.

**(c)** At $d = 1.5$ mm the diameter is ten times larger, so $k$ is 100 times
larger: $1.5625\times10^{-10}$ m² = 158 darcy. The dependence is quadratic in the
grain size.

**(d)** It assumes a bundle of straight capillary tubes of uniform radius. A real
rock violates it in several ways at once: the pore throats are narrower than the
pores and control the flow; clay lines the pores and blocks the throats; and
compaction and stress change the geometry. Each violation makes the real
permeability lower than the prediction, often by orders of magnitude.

---

## ★★4 — Gassmann at 15 per cent porosity

**(a)** The denominator is
$0.15/2.2 + 0.85/37 - 9.92/1369 = 0.068182 + 0.022973 - 0.007246 = 0.083909$.
The numerator is $(1-9.92/37)^2 = (0.73189)^2 = 0.53566$. So
$K_\text{sat} = 9.92 + 0.53566/0.083909 = 9.92 + 6.384 = 16.30$ GPa.

**(b)** With gas, the denominator becomes
$0.15/0.02 + 0.022973 - 0.007246 = 7.5 + 0.015727 = 7.515727$, so
$K_\text{sat} = 9.92 + 0.53566/7.515727 = 9.92 + 0.0713 = 9.99$ GPa.

**(c)** Brine: $\rho = 0.85\times2650 + 0.15\times1000 = 2402.5$ kg/m³, and
$v_p = \sqrt{(16.30 + \frac43\times6.87)\times10^9/2402.5} = 3256$ m/s,
$v_s = \sqrt{6.87\times10^9/2402.5} = 1691$ m/s. Gas:
$\rho = 2267.5$ kg/m³, $v_p = 2906$ m/s, $v_s = 1741$ m/s.

**(d)** $v_p$ falls by 10.7 per cent and $v_s$ rises by 2.9 per cent. The demo,
at $\phi = 0.20$, gives $-7.4$ and $+4.1$ per cent. The trend is that the *P*
velocity effect is larger at lower porosity, because a given fluid change acts on
a stiffer framework where the fluid's compressibility matters relatively more;
and the *S* velocity effect is smaller, because the density change is a smaller
fraction of the total when there is less pore volume.

---

## ★★5 — Archie's law

**(a)** $S_w = (1\times0.05/(0.22^2\times10))^{1/2} = (0.05/0.484)^{1/2}
= (0.10331)^{1/2} = 0.321$.

**(b)** For $R_t = 40$: $(0.05/1.936)^{1/2} = (0.025826)^{1/2} = 0.161$.

**(c)** $S_w \propto R_t^{-1/n} = R_t^{-1/2}$, so quadrupling the resistivity
halves the saturation. The reason is that the rock's conductivity is carried by
the brine, so the resistivity of a rock with a fixed geometry is inversely
proportional to the water saturation; squaring the relation (for $n = 2$) inverts
it.

**(d)** $S_w = 1$ requires $\phi^2 R_t = R_w$, so
$\phi = \sqrt{0.05/10} = 0.071$. Below 7.1 per cent porosity this rock cannot be
fully brine-saturated and still have a resistivity of 10 Ω·m; the formula would
return $S_w > 1$, which is impossible. That is the domain limit of the model, and
a printed value above 1 is a warning rather than a result.

---

## ★★6 — Error propagation

**(a)** $G = 2300\times2000^2 = 9.20\times10^9$ Pa $= 9.20$ GPa. And
$K = 2300(3500^2 - \frac43\times2000^2) = 2300(1.225\times10^7 - 5.3333\times10^6)
= 2300\times6.9167\times10^6 = 1.591\times10^{10}$ Pa $= 15.91$ GPa.

**(b)** With $v_s \to 2020$ m/s:
$K = 2300(1.225\times10^7 - \frac43\times4.0804\times10^6) = 2300\times6.8093\times10^6
= 1.566\times10^{10}$ Pa $= 15.66$ GPa.

**(c)** The change is $-1.55$ per cent, which is exactly the demo's
`dK/K for 1% in Vs` row for this case (`-1.55%`).

**(d)** A 1 per cent error in $v_s$ is a 2 per cent error in $v_s^2$, and
$\frac43v_s^2$ is a substantial fraction of $v_p^2$, so the changed term is a
non-trivial part of a difference of two comparable terms. The amplification
factor is $2\times(\frac43v_s^2)/(v_p^2 - \frac43v_s^2)$, which is why it grows as
$v_s/v_p$ grows — and why a rock with a low Poisson's ratio is the *most*
sensitive to a shear-velocity error.

---

## ★★★7 — Two porosity models disagree

**(a)** $1/v_p = 0.20/1500 + 0.80/5500 = 1.3333\times10^{-4} + 1.4545\times10^{-4}
= 2.7879\times10^{-4}$, so $v_p = 3587$ m/s.

**(b)** The time average gives 3587 m/s and Gassmann (with the demo's dry-rock
moduli) gives 3228 m/s, a difference of 359 m/s or 11 per cent.

**(c)** Inverting both models from the same measured velocity into a porosity is
ambiguous: a $v_p$ of 3400 m/s corresponds to about 0.24 porosity on the time
average and about 0.16 on the Gassmann model. Two models, one velocity, two
porosities differing by half — and nothing in the velocity says which is right.

**(d)** Because they are not measuring the same quantity. Archie's law reports
the **connected, brine-filled** pore fraction, which is what carries the current.
The time average responds to however much soft material the rock contains —
including isolated pores, microcracks and soft grains — because a compressional
wave is slowed by anything that makes the rock more compressible. A rock with
10 per cent of its volume as isolated vugs has an Archie porosity 10 points lower
and a velocity porosity that sees all of it.

---

## ★★★8 — The demo's output

**(a)** Brine 2320 kg/m³, gas 2140 kg/m³; the contrast moves from $-12.5$ to
$-19.2$ per cent against the grain density, a change of 180 kg/m³.

**(b)** At a 50/50 quartz–calcite mix the bound is 12 per cent wide in $K$ and
3.6 per cent wide in $G$ (from $K_V = 56.0$, $K_R = 49.6$, $G_V = 37.0$,
$G_R = 35.7$ GPa).

**(c)** Brine: $K_\text{sat} = 15.01$ GPa, $v_p = 3228$, $v_s = 1721$ m/s. Oil:
12.42 GPa, 3076, 1736. Gas: 9.98 GPa, 2990, 1792.

**(d)** $v_p$ changes by $-7.4$ per cent from brine to gas and $v_s$ by
$+4.1$ per cent. The signs are opposite, and that opposition is the diagnostic
that separates a fluid change from a rock change.

**(e)** $d = 0.20$ mm: $\phi = 0.15$ gives `1.05 D`, 0.25 gives `6.25 D`, 0.35
gives `22.85 D`.

**(f)** From 0.25 to 0.20 the loss is 55 per cent; from 0.15 to 0.10 it is
74 per cent.

**(g)** The row $\phi = 0.15$, $R_t = 1.0$ Ω·m returns $S_w = 2.108$. A
saturation above 1 is impossible, so the assumed $R_w$, $m$ or $n$ do not
describe that rock; a real interpretation revises the parameters rather than
reporting the number.

**(h)** The mineral moduli, fluid moduli, densities and the Archie exponents are
`TABULATED` inputs. The bulk densities, the Voigt–Reuss–Hill moduli, the Gassmann
$K_\text{sat}$, the velocities, the permeabilities and the saturations are all
computed from them, and the demo prints each computed value next to an
independent check.

---

## ★★★9 — Sensitivity to the dry-rock moduli

**(a)** With $\phi = 0.20$ and brine: $K_\text{dry} = 5$ GPa gives
$K_\text{sat} = 11.87$ GPa; 10 GPa gives 15.06 GPa; 20 GPa gives 22.16 GPa.

**(b)** Brine-to-gas changes: 5 GPa → $11.87 - 5.07 = 6.80$ GPa; 10 GPa →
$15.06 - 10.05 = 5.01$ GPa; 20 GPa → $22.16 - 20.02 = 2.13$ GPa.

**(c)** The fluid effect is 6.80, 5.01 and 2.13 GPa for dry moduli of 5, 10 and
20 GPa — it shrinks as the rock gets stiffer. The reason is that Gassmann's
correction is driven by the *contrast* between the fluid's compressibility and
the rock's: in a compliant rock the fluid carries much of the load, so changing
the fluid changes the rock's stiffness substantially; in a stiff rock the
framework carries the load and the fluid barely matters.

**(d)** A time-lapse survey can monitor **soft, high-porosity, poorly cemented**
reservoirs, where the dry-rock modulus is low and the fluid effect is large. It
will struggle with **stiff, low-porosity, well-cemented** rocks, where the same
fluid change barely moves the velocity. That dependency is why a feasibility
study — inserting the expected saturation change into Gassmann and computing the
velocity change — is the first step of any 4-D seismic project, and why a null
result is sometimes a statement about the rock rather than about the survey.
