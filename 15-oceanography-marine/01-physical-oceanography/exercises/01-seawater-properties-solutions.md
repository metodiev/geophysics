# Solutions — 15-01-01 Seawater Properties: Temperature, Salinity, Density

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed, not estimated by hand
> from memory.

Lesson: [01 Seawater Properties](../01-seawater-properties.md).

Constants: $\rho_0 = 1027.0\ \mathrm{kg\,m^{-3}}$, $T_0 = 10\ ^\circ$C,
$S_0 = 35.0\ \mathrm{g\,kg^{-1}}$, $\alpha = 1.70\times10^{-4}\
{}^\circ\mathrm{C}^{-1}$, $\beta = 7.60\times10^{-4}\
\mathrm{(g\,kg^{-1})^{-1}}$, $\kappa = 4.40\times10^{-6}\ \mathrm{dbar^{-1}}$,
$\Delta_\alpha = 1.50\times10^{-5}\ {}^\circ\mathrm{C}^{-2}$,
$g = 9.81\ \mathrm{m\,s^{-2}}$.

---

## ★1 — $\sigma_t$ for $(5\ ^\circ\mathrm{C}, 34.5\ \mathrm{g\,kg^{-1}})$

$$\rho = 1027.0\left[1 - 1.70\times10^{-4}(5-10) + 7.60\times10^{-4}(34.5-35.0)\right]$$

$T - T_0 = -5\ ^\circ$C, so $-1.70\times10^{-4}(-5) = +8.50\times10^{-4}$.
$S - S_0 = -0.5\ \mathrm{g\,kg^{-1}}$, so $7.60\times10^{-4}(-0.5) =
-3.80\times10^{-4}$. The bracket is $1 + 8.50\times10^{-4} - 3.80\times10^{-4}
= 1.00047$.

$$\rho = 1027.0 \times 1.00047 = 1027.4827\ \mathrm{kg\,m^{-3}},
\qquad \sigma_t = 27.4827 \approx 27.48 .$$

Cold and fresh partly cancel: the cold anomaly alone would add
$0.873\ \mathrm{kg\,m^{-3}}$, the fresh anomaly removes $0.390$, leaving
$+0.483$.

**Units:** each of $\alpha(T-T_0)$, $\beta(S-S_0)$, $\kappa p$ is dimensionless,
so the bracket is dimensionless and $\rho$ carries the unit of $\rho_0$.

---

## ★2 — Units

| coefficient | unit | check |
|---|---|---|
| $\alpha$ | $^\circ\mathrm{C}^{-1}$ | $\alpha \times^\circ\mathrm{C}$ dimensionless |
| $\beta$ | $(\mathrm{g\,kg^{-1}})^{-1}$ | $\beta \times \mathrm{g\,kg^{-1}}$ dimensionless |
| $\kappa$ | $\mathrm{dbar^{-1}}$ | $\kappa \times \mathrm{dbar}$ dimensionless |

$$\alpha(T-T_0) + \beta(S-S_0) + \kappa p
= [^\circ\mathrm{C}^{-1}][^\circ\mathrm{C}]
+ [(\mathrm{g\,kg^{-1}})^{-1}][\mathrm{g\,kg^{-1}}]
+ [\mathrm{dbar^{-1}}][\mathrm{dbar}] = 1 + 1 + 1 = \text{dimensionless}. \ ✔$$

This is why the three terms may be added, and it is the check that catches a
coefficient quoted in $\mathrm{m^{-1}}$, $\mathrm{kg^{-1}}$ or
$\mathrm{Pa^{-1}}$.

---

## ★3 — Pressure and compression at 3000 m

$$p = \frac{\rho_0 g z}{10^{4}} = \frac{1027.0 \times 9.81 \times 3000}{10^{4}}
= \frac{3.0225\times10^{7}}{10^{4}} = 3022.5\ \mathrm{dbar}.$$

$$\kappa p = 4.40\times10^{-6} \times 3022.5 = 1.3299\times10^{-2},
\qquad \kappa p \rho_0 = 1.3299\times10^{-2}\times1027.0 = 13.658\
\mathrm{kg\,m^{-3}} .$$

As a fraction of $\rho_0$: $13.658/1027.0 = 1.330\,\%$. Expressed as an
equivalent temperature change, $1.330\times10^{-2}/\alpha = 78.2\ ^\circ$C.

---

## ★4 — Two-layer column: stability with and without potential density

**(a)** Surface $T = 22.0\ ^\circ$C, $S = 35.80$:
$T - T_0 = 12$, $S - S_0 = 0.80$;
bracket $= 1 - 1.70\times10^{-4}(12) + 7.60\times10^{-4}(0.80)
= 1 - 2.040\times10^{-3} + 6.080\times10^{-4} = 0.998568$.
$\rho = 1025.529\ \mathrm{kg\,m^{-3}}$, $\sigma_t = 25.529$.

1000 m: $T = 6.0\ ^\circ$C, $S = 35.00$: bracket $= 1 + 6.80\times10^{-4}
= 1.000680$. $\rho_\theta = 1027.698\ \mathrm{kg\,m^{-3}}$,
$\sigma_t = 27.698$.

**(b)** With $z$ positive **downward**, $N^{2} = (g/\rho_0)\,
\Delta\rho_\theta/\Delta z$:

$$\Delta\rho_\theta = 1027.698 - 1025.529 = 2.169\ \mathrm{kg\,m^{-3}},
\qquad \Delta z = 1000\ \mathrm{m},$$

$$N^{2} = \frac{9.81}{1027.0}\cdot\frac{2.169}{1000}
= 9.552\times10^{-3}\times 2.169\times10^{-3}
= 2.072\times10^{-5}\ \mathrm{s^{-2}}.$$

$N = \sqrt{2.072\times10^{-5}} = 4.552\times10^{-3}\ \mathrm{rad\,s^{-1}}$;
buoyancy period $2\pi/N = 1380\ \mathrm{s} = 23.0$ min.

**(c)** In situ at 1000 m, adding $\kappa p$ with $p = 1007$ dbar:
$\kappa p = 4.4308\times10^{-3}$, bracket $= 1.000680 + 0.0044308 = 1.005111$,
$\rho = 1032.249\ \mathrm{kg\,m^{-3}}$.

$$\Delta\rho = 1032.249 - 1025.529 = 6.720\ \mathrm{kg\,m^{-3}}
\qquad\Rightarrow\qquad
N^{2}_{\text{spurious}} = 9.552\times10^{-3}\times 6.720\times10^{-3}
= 6.419\times10^{-5}\ \mathrm{s^{-2}}.$$

Ratio: $6.419\times10^{-5}/2.072\times10^{-5} = 3.10$. **The column appears 3.1
times more stable than it is.** Every bit of the excess is compression, and none
of it is stratification.

---

## ★5 — Cabbeling

**(a)** Water A, $\Delta T = 4$, $\Delta S = 0.500$:

$$\text{therm} = -\left[1.70\times10^{-4}(4) + \tfrac12(1.50\times10^{-5})(16)\right]
= -(6.80\times10^{-4} + 1.20\times10^{-4}) = -8.00\times10^{-4},$$
$$\text{haline} = 7.60\times10^{-4}(0.500) = 3.80\times10^{-4},$$
$$\text{bracket} = 1 - 8.00\times10^{-4} + 3.80\times10^{-4} = 0.999580
\;\Rightarrow\; \rho_A = 1026.5687 .$$

Water B, $\Delta T = -8$, $\Delta S = -1.711$:

$$\text{therm} = -\left[1.70\times10^{-4}(-8) + \tfrac12(1.50\times10^{-5})(64)\right]
= -(-1.360\times10^{-3} + 4.80\times10^{-4}) = +8.80\times10^{-4},$$
$$\text{haline} = 7.60\times10^{-4}(-1.711) = -1.30036\times10^{-3},$$
$$\text{bracket} = 1 + 8.80\times10^{-4} - 1.30036\times10^{-3} = 0.999580
\;\Rightarrow\; \rho_B = 1026.5687 .$$

The densities agree to more decimal places than the inputs justify — the
salinity of B was *chosen* to make them agree.

**(b)** Mixture: $T_m = 8.00\ ^\circ$C, $S_m = 34.3945\ \mathrm{g\,kg^{-1}}$,
$\Delta T_m = -2$, $\Delta S_m = -0.6055$.

$$\text{therm} = -\left[1.70\times10^{-4}(-2) + \tfrac12(1.50\times10^{-5})(4)\right]
= -(-3.40\times10^{-4} + 3.00\times10^{-5}) = +3.10\times10^{-4},$$
$$\text{haline} = 7.60\times10^{-4}(-0.6055) = -4.6018\times10^{-4},$$
$$\rho_m = 1027.0(1 + 3.10\times10^{-4} - 4.6018\times10^{-4})
= 1027.0(0.99984982) = 1026.8458 .$$

Mean of the two densities: $\tfrac12(1026.5687 + 1026.5687) = 1026.5687$.

**(c)** Cabbeling anomaly:

$$\rho_m - \bar\rho = 1026.8458 - 1026.5687 = +0.2771\ \mathrm{kg\,m^{-3}}
= 277.1\ \mathrm{g\,m^{-3}} .$$

Sign convention: positive means **the mixture is denser than the mean of its
constituents**. The demonstration prints $277.29\ \mathrm{g\,m^{-3}}$; the
difference of $0.2\ \mathrm{g\,m^{-3}}$ comes from rounding $S_B$ to three
decimals here.

**(d)** With $\Delta_\alpha = 0$ the bracket is linear in $T$ and $S$:

$$\rho(T,S) = \rho_0\left[1 - \alpha_0(T-T_0) + \beta(S-S_0) + \kappa p\right]
= \rho_0\left[1 - \alpha_0 T + \beta S\right] + \text{const}.$$

For any two parcels and any mixing fraction $f$,

$$\rho(fT_A + (1-f)T_B,\ fS_A + (1-f)S_B)
= f\rho(T_A,S_A) + (1-f)\rho(T_B,S_B)$$

identically, because both $\rho(T,S)$ and the mixture map are affine. The
anomaly is zero for *every* pair, not just this one — which is why cabbeling
cannot be produced by any choice of numbers inside a linear equation of state.

---

## ★6 — Sound-speed depth error

The instrument measures a two-way time $t$ and reports $z_{\text{rep}} =
c_{\text{assumed}} t/2$. The true depth is $z_{\text{true}} =
c_{\text{true}} t/2$, so

$$\frac{z_{\text{rep}}}{z_{\text{true}}} = \frac{c_{\text{assumed}}}{c_{\text{true}}}.$$

**(a)** Reported $4000\ \mathrm{m}$ at $c_{\text{assumed}} = 1500$ gives
$t = 2\times4000/1500 = 5.3333\ \mathrm{s}$. With
$c_{\text{true}} = 1540$:
$z_{\text{true}} = 1540\times5.3333/2 = 4106.7\ \mathrm{m}$.

**(b)** With $c_{\text{true}} = 1460$:
$z_{\text{true}} = 1460\times5.3333/2 = 3893.3\ \mathrm{m}$.

**(c)** Fractional errors relative to the *true* depth:

$$\text{(a)}\quad \frac{4000 - 4106.7}{4106.7} = -0.0260 = -2.60\,\%,
\qquad
\text{(b)}\quad \frac{4000 - 3893.3}{3893.3} = +0.0274 = +2.74\,\%.$$

Both equal $(c_{\text{assumed}} - c_{\text{true}})/c_{\text{true}}$:
$-40/1540 = -2.60\,\%$ and $+40/1460 = +2.74\,\%$. The magnitudes differ for the
same $|40\ \mathrm{m\,s^{-1}}|$ offset because the reference speed differs.
**The mapping is one-for-one in the fractional sense, with no attenuation** — a
$2.6\,\%$ speed error is a $2.6\,\%$ depth error, roughly $100\ \mathrm{m}$ at
this depth.

---

## ★7 — Distinguishing static from adiabatic stability

**Quantity.** The discriminator is the sign of
$N^{2} = (g/\rho_0)\partial\rho_\theta/\partial z$. Static stability alone is
$\partial\rho_{\text{in situ}}/\partial z > 0$, which is satisfied almost
everywhere including in columns that are unstable to adiabatic displacement.

**Instruments.** A CTD (conductivity–temperature–depth) package sampling at
least every $1\ \mathrm{m}$, plus a pressure sensor good to a few dbar. Salinity
must be reported on a stated scale and temperature as *potential* temperature at
the surface reference pressure.

**Sampling.** Full-depth profiles, repeated, with at least two casts to estimate
noise. Resolution matters: the effect is a difference between two nearly equal
numbers, so $1\ \mathrm{m}$ sampling is the minimum for a $10\ \mathrm{m}$
transition.

**Size of the effect to resolve.** From the lesson, compression contributes
$1.77\,\%$ of density at 4000 m, equivalent to $18.2\ \mathrm{kg\,m^{-3}}$;
an interesting $N^{2}$ corresponds to $\Delta\rho_\theta$ of order
$0.01\ \mathrm{kg\,m^{-3}}$ over a few metres. The *difference* between the two
estimates of $N^{2}$ is therefore of order $10^{3}$ times the signal. This is not
a delicate measurement; it is a measurement that is wrong by a factor if done
naively.

**Statement.** The report is "the profile is stable with respect to adiabatic
displacement over the depth range $a$–$b$, with $N^{2}$ between $x$ and $y$",
not "the water column is stable".

---

## ★8 — The linear-versus-curved discrepancy

**(a)** The curved and linear brackets differ by
$\tfrac12\Delta_\alpha(\Delta T)^{2}$ with $\Delta T = T - T_0$. On the box
$T \in [0,30]\ ^\circ$C with $T_0 = 10\ ^\circ$C, the largest
$|\Delta T|$ is $20\ ^\circ$C:

$$\tfrac12(1.50\times10^{-5})(20)^{2} = \tfrac12(1.50\times10^{-5})(400)
= 3.00\times10^{-3},$$

$$\Delta\rho_{\max} = 1027.0 \times 3.00\times10^{-3}
= 3.081\ \mathrm{kg\,m^{-3}} .$$

This matches the measured $3.0810\ \mathrm{kg\,m^{-3}}$ exactly, because the
difference of the two equations of state is *only* this quadratic term —
$S$ and $p$ cannot contribute, since both forms are linear in them. The
agreement is therefore a consistency check on the arithmetic rather than an
independent validation.

**(b)** Require $1027.0\times\tfrac12(1.50\times10^{-5})(\Delta T)^{2} \le 0.01$:

$$(\Delta T)^{2} \le \frac{0.01}{1027.0\times7.5\times10^{-6}}
= \frac{0.01}{7.7025\times10^{-3}} = 1.2983
\;\Rightarrow\; |\Delta T| \le 1.14\ ^\circ\mathrm{C}.$$

So this linear equation of state is good to $0.01\ \mathrm{kg\,m^{-3}}$ only
within about $\pm1\ ^\circ$C of the reference temperature — a small window, and
the reason the deep ocean and the cold high latitudes are exactly where a linear
equation of state fails first.

**(c)** The cabbeling result is structural because it follows from *convexity* of
$\rho(T,S)$ alone: an affine map commutes with averaging, and any non-affine
$\rho$ does not. The existence and sign of the anomaly (mixing two equal-density
waters gives denser water) therefore transfer to real seawater. Its magnitude
does not, because the magnitude is set by the curvature
$\partial^{2}\rho/\partial T^{2}$, i.e. by $\Delta_\alpha$, which is a property of
the particular equation of state and not of the argument. Reporting
"$277\ \mathrm{g\,m^{-3}}$" as a property of the ocean would be a category error;
reporting the mechanism is not.
