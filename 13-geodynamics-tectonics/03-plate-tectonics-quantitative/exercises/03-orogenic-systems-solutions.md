# Solutions — 13-03-03 Orogenic Systems, Crustal Thickening and Collapse

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [03 Orogenic Systems, Crustal Thickening and Collapse](../03-orogenic-systems.md).

---

## ★1 — Elevation and Moho depth of a $52\ \mathrm{km}$ crust

$$
e = (52-35)\frac{3330-2800}{3330} = 17\times0.15916 = 2.706\ \mathrm{km},
$$
$$
\text{Moho depth} = e + t_c = 2.706 + 52 = 54.7\ \mathrm{km}.
$$

(The demonstration's table gives $2.387\ \mathrm{km}$ at $t_c = 50$ and
$3.979\ \mathrm{km}$ at $t_c = 60$, so $2.7\ \mathrm{km}$ at $52\ \mathrm{km}$
is consistent.)

---

## ★2 — Shortening

$$
\beta = \frac{52}{35} = 1.4857, \qquad
\text{shortening} = 1 - \frac{1}{1.4857} = 1 - 0.6731 = 0.3269 .
$$

So $32.7\%$, or $32.7\ \mathrm{km}$ of shortening per $100\ \mathrm{km}$ of
section. Check by the equivalent form $1 - t_{c0}/t_c = 1 - 35/52 = 0.3269$. ✔

---

## ★3 — Units and stress

$P$ is in $\mathrm{Pa} = \mathrm{N\,m^{-2}}$ and $\mathrm dz$ in
$\mathrm{m}$, so the integral is $\mathrm{N\,m^{-1}}$: a force per unit length,
i.e. a **force resultant**. ✔

$$
\bar\tau = \frac{\Gamma}{L} = \frac{2.2\times10^{13}}{1.5\times10^{5}}
= 1.47\times10^{8}\ \mathrm{Pa} = 0.15\ \mathrm{GPa}.
$$

---

## ★4 — The isostatic factor and its reciprocals

$$
\frac{\rho_m - \rho_c}{\rho_m} = \frac{530}{3330} = 0.15916, \qquad
\frac{\rho_m}{\rho_m - \rho_c} = 6.283 .
$$

So $1\ \mathrm{km}$ of elevation requires $6.283\ \mathrm{km}$ of crustal
thickening; equivalently, $1\ \mathrm{km}$ of thickening gives
$0.159\ \mathrm{km}$ of elevation.

---

## ★5 — Three ways to $3.0\ \mathrm{km}$

**(i) Crustal thickening.**
$t_c - t_{c0} = 3.0/0.15916 = 18.85\ \mathrm{km}$, so
$t_c = 53.85\ \mathrm{km}$.

**(ii) Cold-lid removal.** With $\rho_m\alpha(T_m/2)/(\rho_m-\rho_w)
= 0.028165\ \mathrm{m}$ of uplift per metre of lid,

$$
L_{\text{lid}} = \frac{3.0}{0.028165} = 106.5\ \mathrm{km}.
$$

**(iii) Half and half.** Thickening contributes $1.5\ \mathrm{km}$ of elevation,
so $\Delta t_c = 1.5/0.15916 = 9.42\ \mathrm{km}$
($t_c = 44.42\ \mathrm{km}$); the lid contributes the other $1.5\ \mathrm{km}$,
so $L_{\text{lid}} = 53.3\ \mathrm{km}$.

**Distinguishing quantity.** Crustal thickness (Moho depth), measured
seismologically, or the gravity anomaly computed with an assumed crust–mantle
density contrast. Elevation alone cannot separate the three cases: they are
identical by construction.

---

## ★6 — Buoyancy force at $t_c = 45\ \mathrm{km}$

Elevation: $e = 10\times0.15916 = 1.592\ \mathrm{km}$.

The exact integral has two parts. Using $\bar u = t_c - t_{c0} - E$ (the column's
crustal base lies at $t_c - E$, so the second interval extends from $t_{c0}$ to
$t_c - E$):

$$
\Gamma = \rho_c g E\,t_{c0}
+ g\left[\frac{(\rho_c-\rho_m)\bar u^{2}}{2}
+ \rho_c(t_{c0}+E)\,\bar u\right],
\qquad \bar u = (45-35-1.592)\times10^{3} = 8.408\times10^{3}\ \mathrm{m}.
$$

- first term: $2800\times9.81\times1592\times3.5\times10^{4}
  = 1.530\times10^{12}$;
- second term, first part:
  $9.81\times(-530)\times(8.408\times10^{3})^{2}/2
  = -1.837\times10^{11}$;
- second term, second part:
  $9.81\times2800\times36592\times8.408\times10^{3} = 8.451\times10^{12}$.

$$
\Gamma_{\text{exact}} = 1.530 - 0.184 + 8.451 = 9.798\times10^{12}
\ \mathrm{N\,m^{-1}} .
$$

The scale:
$\tfrac12 g\rho_c(t_c^{2}-t_{c0}^{2}) =
\tfrac12\times9.81\times2800\times800\times10^{6}
= 1.0987\times10^{13}\ \mathrm{N\,m^{-1}}$.

**Ratio $= 9.798/10.987 = 0.892$, so the scale OVERESTIMATES the buoyancy force
by $12.1\%$** at $\Delta t_c = 10\ \mathrm{km}$. Interpolating the lesson's table
between $0.942$ at $t_c = 40$ and $0.847$ at $t_c = 50$ predicts $0.892$ — the
hand calculation agrees with the demonstration, which is the check that the sign
convention for $\bar u$ has been applied correctly. (Getting the sign of $\bar u$
wrong changes the answer by about $20\%$; it is the single easiest mistake in
this calculation.)

---

## ★7 — Collapse times

$\rho_c g\,e\,H = 2800\times9.81\times4000\times6.5\times10^{4}
= 7.142\times10^{12}\ \mathrm{Pa\,m}$.

$$
\tau_c = \frac{\eta L}{\rho_c g\,e\,H} =
\frac{\eta\times3\times10^{5}}{7.142\times10^{12}}
= 4.20\times10^{-8}\,\eta \ \mathrm{s} .
$$

| $\eta$ (Pa s) | $\tau_c$ (s) | $\tau_c$ (Myr) |
|---|---|---|
| $10^{20}$ | $4.20\times10^{12}$ | 0.133 |
| $10^{21}$ | $4.20\times10^{13}$ | 1.33 |
| $10^{22}$ | $4.20\times10^{14}$ | 13.3 |

**Viscosity for $40\ \mathrm{Myr}$:** $40\ \mathrm{Myr}
= 1.262\times10^{15}\ \mathrm{s}$, so
$\eta = 1.262\times10^{15}/4.20\times10^{-8} = 3.0\times10^{22}\ \mathrm{Pa\,s}$.

Again the requirement is $10^{22}$–$10^{23}$: two to three orders of magnitude
above a crustal channel.

---

## ★8 — Erosion at $0.3\ \mathrm{mm\,yr^{-1}}$

$0.3\ \mathrm{mm\,yr^{-1}} = 0.3\ \mathrm{km\,Myr^{-1}}$, because
$1\ \mathrm{mm\,yr^{-1}} = 1\ \mathrm{km\,Myr^{-1}}$ exactly.

Surface lowering rate $= 0.1592\times0.3 = 0.048\ \mathrm{mm\,yr^{-1}}$;
the Moho rises at $(1+0.1592)\times0.3 = 0.348\ \mathrm{mm\,yr^{-1}}$ (the Moho
depth changes at $-(1+0.1592)\,h$).

Time to remove $5.0\ \mathrm{km}$ of topography with no tectonic input:
$h = 5.0/0.1592 = 31.4\ \mathrm{km}$ of erosion, which at
$0.3\ \mathrm{km\,Myr^{-1}}$ takes $105\ \mathrm{Myr}$.

**The number is the point.** Even a vigorous erosion rate of
$0.3\ \mathrm{mm\,yr^{-1}}$ needs over $100\ \mathrm{Myr}$ to level the plateau
by erosion alone, because $84\%$ of the removal is cancelled by rebound. Any
young, high orogen must therefore be actively supported; erosion alone cannot
explain its disappearance on a $10\ \mathrm{Myr}$ timescale.

---

## ★9 — Two-layer scaling (one defensible form)

Let an elastic upper crust of thickness $h_u$ (with a finite elastic thickness
$T_e$) overlie a viscous channel of thickness $h$ and viscosity $\eta_c$, above
a strong mantle lithosphere. Only the channel flows, and it flows because the
plateau's weight drives a pressure gradient

$$
\frac{\partial p}{\partial x} \sim \frac{\rho_c g\,\Delta e}{L},
$$

and the channel flux is $q \sim h^{3}\,\partial_x p/(12\eta_c)$, so the volume
flux (per unit strike length) is
$Q \sim h^{3}\rho_c g\,\Delta e/(12\eta_c L)$. Spreading consumes the
topography at a rate set by $Q$ and the plateau's width scale $L$:

$$
\frac{\mathrm d(\Delta e)}{\mathrm dt}
\sim \frac{Q}{L}
= \frac{h^{3}\rho_c g\,\Delta e}{12\eta_c L^{2}} .
$$

The decay is exponential with time constant

$$
\boxed{\;\tau_{\text{channel}} = \frac{12\,\eta_c L^{2}}
{\rho_c g\,h^{3}}\;}
$$

Compare with the single-viscosity result $\tau_c = \eta L/(\rho_c g\,\Delta e\,H)$.
The new scaling is qualitatively different: it depends on $L^{2}$ (long plateaux
collapse *faster*, not slower, because the pressure gradient is smaller but the
flux length is larger), on $h^{3}$ (a thin channel is enormously more resistant),
and not at all on the plateau height — because the driving stress and the
thickness to be removed are both proportional to $\Delta e$.

Numerically, with $\eta_c = 10^{19}\ \mathrm{Pa\,s}$, $L = 250\ \mathrm{km}$,
$\Delta e = 5.571\ \mathrm{km}$ and a channel of thickness $h$:

| $h$ (km) | 2 | 5 | 10 | 15 |
|---|---|---|---|---|
| $\tau_{\text{channel}}$ (Myr) | 1081 | 69.2 | 8.65 | 2.56 |

The $h^{3}$ dependence is brutal: a $5\ \mathrm{km}$ channel at
$10^{19}\ \mathrm{Pa\,s}$ gives a $69\ \mathrm{Myr}$ collapse, geologically
plausible, while a $15\ \mathrm{km}$ channel of the same viscosity collapses in
$2.6\ \mathrm{Myr}$. The single-viscosity model of the lesson gave
$0.07\ \mathrm{Myr}$ for the whole $70\ \mathrm{km}$ column at
$\eta = 10^{20}\ \mathrm{Pa\,s}$, which is the same order as
$\tau_{\text{channel}}$ with $h = 70\ \mathrm{km}$ — as it should be, since the
two models coincide when the channel fills the column.

**Separating observations.** The channel model predicts (i) a strong
dependence on channel thickness, testable with heat flow and magnetotellurics;
(ii) surface deformation concentrated in the plateau interior with little
deformation at its edges, testable with GNSS; and (iii) a timescale
*independent of elevation*, so a smaller plateau decays on the same timescale as
a larger one. The single-viscosity model predicts the opposite dependence on
$\Delta e$.

---

## ★10 — Crustal root versus lithospheric buoyancy (specification)

**Data.** (i) Receiver functions at $\ge 30$ stations across the plateau, to
estimate Moho depth with the $v_p/v_s$ trade-off admitted; (ii) a gravity or
satellite-derived Bouguer anomaly field; (iii) topography and, if available,
surface-wave $v_s$ structure to constrain lithospheric thickness.

**Forward models.** Model A: crustal thickness $t_c$ varying laterally, mantle
lithosphere of fixed density, local (Airy) compensation. Model B: fixed crustal
density but a laterally varying mantle-lithosphere thickness (density anomaly
$\rho_m\alpha\Delta T$ over a lid thickness $L_{\text{lid}}$). Model C: both, to
test whether the data need the second parameter at all.

**Noise model.** Moho depth errors of $\pm 2$–$4\ \mathrm{km}$ (dominated by the
$v_p/v_s$ trade-off, see
[06-08-01](../../../06-seismology/08-receiver-functions-and-crustal-structure/01-receiver-function-principle.md));
gravity errors dominated by the unknown density contrast; topography errors
negligible.

**Metric.** Joint misfit with a covariance-weighted $\chi^{2}$, plus the
trade-off between $L_{\text{lid}}$ and $\Delta t_c$ expressed as the correlation
coefficient and the marginal posterior width of each.

**Expected trade-off.** They are strongly anti-correlated: adding
$10\ \mathrm{km}$ of cold lid substitutes for roughly $3.2\ \mathrm{km}$ of
crustal thickening (from the two coefficients, $0.0282$ km uplift per km of lid
and $0.1592$ km uplift per km of thickening). The experiment is only decisive if
the seismological constraint on Moho depth is better than that exchange rate
allows — i.e. if $\sigma(\text{Moho}) \lesssim 3\ \mathrm{km}$, otherwise the
gravity data cannot break the trade-off no matter how good they are.
