# Solutions — 11-05-01 Geophysical Signatures of Aquifers and Saline Interfaces

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Several problems admit more than one defensible answer; where that is so
> it is said.

Lesson: [01 Geophysical Signatures of Aquifers and Saline Interfaces](../01-aquifer-signatures.md).

---

## ★1 — Sharp-interface depth

$$ z = h_f\frac{\rho_f}{\rho_s-\rho_f} = 2.0\times\frac{1000}{25}
= 80.0\ \mathrm{m}\ \text{below sea level}. $$

The ratio is $z/h_f = 40$.

---

## ★2 — Archie conductivity, saturated and partly saturated

Saturated ($S_w = 1$):

$$ \sigma_b = \sigma_w\phi^{m}S_w^{n} = 0.2\times 0.25^{2}\times 1
= 0.2\times 0.0625 = 0.0125\ \mathrm{S\,m^{-1}}. $$

Partly saturated ($S_w = 0.6$, $n = 2$):

$$ \sigma_b = 0.2\times 0.0625\times 0.36 = 0.0045\ \mathrm{S\,m^{-1}}. $$

**Note.** The partly saturated value ($0.0045$) is also consistent with a fully
saturated, *fresher* water at $\sigma_w = 0.072\
\mathrm{S\,m^{-1}}$. Saturation and salinity trade off in the same direction.

---

## ★3 — Density change on saturation

$$ \Delta\rho = \phi(\rho_w-\rho_{\text{air}}) = 0.28\times(1000-1.2)
= 279.7\ \mathrm{kg\,m^{-3}} = 0.2797\ \mathrm{g\,cm^{-3}}. $$

---

## ★4 — Minimum detectable saturated thickness

Convert the resolution to mGal: $8\ \mu\mathrm{Gal} = 0.008\
\mathrm{mGal}$.

$$ \Delta g = 0.04194\,\Delta\rho\,h
\quad\Longrightarrow\quad
h = \frac{\Delta g}{0.04194\,\Delta\rho}
= \frac{0.008}{0.04194\times 0.2497} = 0.764\ \mathrm{m}. $$

So the survey detects fully saturated thicknesses down to about $0.76\
\mathrm{m}$ — *provided* the anomaly is the slab and nothing else. In practice
the limit is set by how well the deeper and regional field is removed, not by
the instrument.

---

## ★5 — Gassmann substitution

Denominator of the fluid term (water):
$\phi/K_{\text{fl}} = 0.30/2.2\times10^{9} = 1.3636\times10^{-10}$;
$(1-\phi)/K_{\text{min}} = 0.70/37\times10^{9} = 1.8919\times10^{-11}$;
$K_{\text{dry}}/K_{\text{min}}^{2} = 1.0\times10^{9}/1.369\times10^{21}
= 7.305\times10^{-13}$. Sum: $1.5455\times10^{-10}$.

Numerator: $(1-1.0/37)^{2} = (0.97297)^{2} = 0.94667$.

$$ K_{\text{sat}}^{\text{water}} = 1.0\times10^{9}
+ \frac{0.94667}{1.5455\times10^{-10}} = 1.000\times10^{9}+6.126\times10^{9}
= 7.126\ \mathrm{GPa}, $$

which is the demonstration's printed $7.125\ \mathrm{GPa}$ (the last digit is
rounding in this hand calculation).

Densities: $\rho_{\text{dry}} = 0.7(2650)+0.3(1.2) = 1855.4\
\mathrm{kg\,m^{-3}}$; $\rho_{\text{sat}} = 0.7(2650)+0.3(1000) = 2155.0\
\mathrm{kg\,m^{-3}}$.

$$ v_p^{\text{dry}} = \sqrt{\frac{1.0\times10^{9}+\tfrac43(3.0\times10^{9})}{1855.4}}
= \sqrt{\frac{5.0\times10^{9}}{1855.4}} = 1642\ \mathrm{m\,s^{-1}}, $$
$$ v_s^{\text{dry}} = \sqrt{\frac{3.0\times10^{9}}{1855.4}}
= 1272\ \mathrm{m\,s^{-1}}, $$
$$ v_p^{\text{sat}} = \sqrt{\frac{7.125\times10^{9}+\tfrac43(3.0\times10^{9})}{2155.0}}
= 2272\ \mathrm{m\,s^{-1}}, $$
$$ v_s^{\text{sat}} = \sqrt{\frac{3.0\times10^{9}}{2155.0}}
= 1180\ \mathrm{m\,s^{-1}}. $$

**Why $v_s$ falls.** Gassmann leaves $\mu$ unchanged, so replacing air with
water raises the density from $1855.4$ to $2155.0\ \mathrm{kg\,m^{-3}}$ while
$\mu$ stays at $3.0\ \mathrm{GPa}$; $v_s = \sqrt{\mu/\rho}$ therefore decreases.

---

## ★6 — Depth and its velocity sensitivity

$$ z = \frac{x_c}{2}\sqrt{\frac{v_2-v_1}{v_2+v_1}}
= 18.5\sqrt{\frac{630}{3910}} = 18.5(0.40141) = 7.43\ \mathrm{m}. $$

With $v_1 = 1720\ \mathrm{m\,s^{-1}}$ and the same $x_c$:

$$ z = 18.5\sqrt{\frac{550}{3990}} = 18.5(0.37127) = 6.87\ \mathrm{m}. $$

Error: $-0.56\ \mathrm{m}$, i.e. $-7.5\%$. The depth is roughly twice as
sensitive to the velocity contrast as to $v_1$ itself; the lesson's table shows
this blowing up as the contrast approaches 1.

---

## ★7 — Separating salinity from clay (specification)

**Measurement 1:** bulk conductivity $\sigma_b$ from ERT or FDEM.
**Measurement 2:** either (a) seismic $v_p$ inverted for porosity through
Gassmann, or (b) a nuclear-magnetic-resonance free-fluid index, or (c) a
water sample from a piezometer.

**Forward relations.** Archie's law with a clay term,
$\sigma_b = \frac{1}{a}\sigma_w\phi^{m}S_w^{n} + \sigma_{\text{clay}}$, and the
Gassmann/porosity relation connecting $v_p$ to $\phi$ at a stated fluid and
mineral modulus.

**Assumptions.** The seismic porosity is independent of the clay surface
conduction; the clay term is calibrated from local samples; $S_w = 1$ below the
water table.

**Test.** Drill one control borehole: measure $\phi$ on core, $\sigma_w$ on a
water sample, and compare the forward-predicted conductivity with the measured
one. A residual larger than the measurement error in a clay-rich interval is
evidence the clay term must be fitted; agreement in a clean sand is evidence the
calibration transfers.

---

## ★8 — Drawdown and the interface

The Ghyben-Herzberg relation holds at every instant if the interface stays
hydrostatic. A drawdown of the head by $\delta h$ lowers $h$, so

$$ \delta z = -\frac{\rho_f}{\rho_s-\rho_f}\,\delta h = -40\,\delta h
\quad(\text{sea-water ratio}). $$

A $0.5\ \mathrm{m}$ drawdown raises the interface by about $20\ \mathrm{m}$
locally (up-coning). The response is a *rising* interface, and it is local to the
well, so the regional relation is unaffected far away.

**Signs the sharp-interface model is failing.** A well log or water sample that
shows a salinity transition tens of metres thick rather than a step; a brackish
lens above a deeper fresh zone; salinity that varies with pumping rate; or a
measured interface depth that does not scale with the head as $z = 40h$. Any of
these means the transition zone, dispersion or transient up-coning is controlling
the position, and the sharp-interface number is a model output rather than a
measurement.

---

## Worked mastery checkpoint

**(a) Interface depth.** $h = 1.0\ \mathrm{m}$,
$\rho_s = 1025\ \mathrm{kg\,m^{-3}}$:

$$ z = 1.0\times\frac{1000}{25} = 40\ \mathrm{m}. $$

It is a lower bound on the *toe* of a real transition zone because the
sharp-interface model puts all the fresh water above a single surface, whereas a
real interface is a dispersive transition tens of metres wide: the fresh water
extends deeper than $z$ above the transition, and brackish water exists below it.

**(b) Two interpretations of $\sigma_b = 0.02\ \mathrm{S\,m^{-1}}$** with
$m = n = 2$:

| Water | $\sigma_w$ (S/m) | Required $\phi$ |
|---|---|---|
| brackish | 0.5 | $\sqrt{0.02/0.5} = 0.200$ |
| saline | 4.0 | $\sqrt{0.02/4.0} = 0.071$ |

**(c) Crossover distance** with $v_1 = 1640$, $v_2 = 2270\
\mathrm{m\,s^{-1}}$, $z = 6\ \mathrm{m}$:

$$ x_c = 2(6)\sqrt{\frac{2270+1640}{2270-1640}}
= 12\sqrt{6.2063} = 12(2.4912) = 29.9\ \mathrm{m}. $$

**(d) The measurement that reduces the ambiguity most:** a borehole with a
porosity log (or a core measurement of $\phi$) plus a water sample for
$\sigma_w$. Archie's law has three unknowns in one equation; only an independent
measurement of one of them — the porosity or the salinity — breaks the tie, and
a water sample settles the salinity directly.
