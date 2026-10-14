# Solutions — 04-05-03 Fluvial, Coastal and Aeolian Systems

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values computed here are labelled as such.

Empirical coefficients used below: the Schiller–Naumann drag correlation, Shields
$\tau^{*}_c = 0.045$, Manning $n$, Bagnold $A$ and $C$, and the breaker index
$\gamma$. None of them is derived, and each is stated with its value.

---

## ★1 — Settling velocity

**(a)** The drag balance
$\frac{\pi}{6}d^{3}(\rho_s-\rho_f)g = \frac{\pi}{8}C_D\rho_f d^{2}v_s^{2}$
is implicit in $v_s$ because $C_D = C_D(\mathrm{Re})$. Iterating gives
$v_s = 0.07839$ m s⁻¹ and $\mathrm{Re} = \rho_w v_s d/\mu = 39.12$.

**(b)** $C_D = \frac{24}{39.12}(1 + 0.15 \times 39.12^{0.687}) = 0.6135 \times
(1 + 0.15 \times 12.42) = 0.6135 \times 2.8624 = 1.756$. The demo reports
$C_D = 1.756$ for the same case.

**(c)** Stokes: $v_s = (\rho_s-\rho_w)gd^{2}/(18\mu) =
(1650)(9.81)(5\times10^{-4})^{2}/(18 \times 1.002\times10^{-3}) = 0.22436$
m s⁻¹. The error is
$100(0.22436 - 0.07839)/0.07839 = +186.2$ per cent.

**(d)** Stokes' law is the $\mathrm{Re} \ll 1$ limit of the drag law
($C_D = 24/\mathrm{Re}$), and a 0.5 mm grain at $v_s \approx 0.08$ m s⁻¹ is at
$\mathrm{Re} \approx 39$, so the inertial term in the drag is dominant and the
linear law is invalid.

---

## ★2 — Shields threshold and mobility

**(a)** $\tau_c = 0.045(1650)(9.81)(2\times10^{-3}) = 1.4568$ Pa.

**(b)** $\tau_b = 1000 \times 9.81 \times 1.5 \times 2\times10^{-4} = 2.943$ Pa.

**(c)** $\tau_b/\tau_c = 2.943/1.4568 = 2.020$, so the bed is **mobile** (the ratio
exceeds one).

**(d)** With $\tau_c = 728.4\,d$ for $d$ in metres:
$d = 0.5$ mm gives $\tau_c = 0.3642$ Pa; $d = 2$ mm gives $1.4568$ Pa;
$d = 5$ mm gives $\tau_c = 3.642$ Pa. At $\tau_b = 2.943$ Pa the 0.5 mm and 2 mm
fractions move (ratios 8.08 and 2.02) and the 5 mm fraction does not
(ratio 0.808). That is grain-size sorting, and it is why a deposit formed at one
flow stage is graded.

---

## ★3 — Manning flow

**(a)** $A = 30 \times 1.2 = 36$ m²; $P = 30 + 2(1.2) = 32.4$ m;
$R_h = 36/32.4 = 1.1111$ m.

**(b)** $V = \frac{1}{0.030}(1.1111)^{2/3}(8\times10^{-4})^{1/2}
= 33.333 \times 1.0725 \times 2.8284\times10^{-2} = 1.0114$ m s⁻¹.

**(c)** $Q = VA = 1.0114 \times 36 = 36.41$ m³ s⁻¹.

**(d)** $\mathrm{Fr} = V/\sqrt{gD} = 1.0114/\sqrt{9.81 \times 1.2}
= 1.0114/3.4304 = 0.2948$. Subcritical (tranquil) flow; bedforms are dunes, not
antidunes.

---

## ★★4 — Wave dispersion and breaking

**(a)** $c_0 = gT/2\pi = 9.81 \times 10/6.28319 = 15.613$ m s⁻¹;
$L_0 = c_0 T = 156.13$ m.

**(b)** $\sqrt{gh} = 3.132$ m s⁻¹ at $h = 1$ m and $5.425$ m s⁻¹ at $h = 3$ m,
against $15.613$ m s⁻¹ in deep water: shallow water slows the wave by a factor of
five.

**(c)** In the shallow limit $kh \approx \omega\sqrt{h/g}$, so at fixed period
$kh \propto \sqrt{h}$. Scaling: $kh = 0.3$ requires
$h = 5(0.3/0.474)^{2} \approx 2.0$ m, where $0.474$ is the $T = 10$ s value at
$h = 5$ m obtained from the $T = 8$ s entry ($0.592 \times 0.6283/0.7854$). The
estimate is approximate — applying it to the demo's $T = 12$ s entry predicts
$0.395$ against the computed $0.383$, a 4 per cent discrepancy — because the
scaling itself assumes the limit it is being used to locate.

**(d)** $c_{g0} = c_0/2 = 7.8065$ m s⁻¹. Then
$h_b^{5/2} = \frac{9 \times 7.8065}{0.78^{2}\sqrt{9.81}}
= \frac{70.26}{1.9056} = 36.87$, so $h_b = 36.87^{0.4} = 4.233$ m and
$H_b = 0.78 \times 4.233 = 3.302$ m. The wave has grown from 3 m in deep water to
3.30 m in 4.2 m of water and breaks there.

---

## ★★5 — Suspension and wind transport

**(a)** $P = v_s/(\kappa u_{*}) = 0.05/(0.40 \times 0.08) = 1.5625$, which is in
the conventional **mixed** band (1.2–2.5): roughly half the load travels in
suspension.

**(b)** $P = 0.05/(0.40 \times 0.16) = 0.781$, below 0.8, so the material is
**wash load** at that shear velocity: essentially all of it is in suspension, and
the bed itself is barely engaged.

**(c)** $u_{*t} = 0.10\sqrt{(2650-1.225)(9.81)(3\times10^{-4})/1.225}
= 0.10\sqrt{6.3633} = 0.2523$ m s⁻¹.

**(d)** $q = C(\rho_a/g)u_{*}^{3} = 1.75 \times 1.225/9.81 \times 0.45^{3}
= 0.21853 \times 0.091125 = 1.991\times10^{-2}$ kg m⁻¹ s⁻¹. Multiplying by
$3.15576\times10^{7}$ s yr⁻¹ gives $6.284\times10^{5}$ kg m⁻¹ yr⁻¹
$= 628.4$ t m⁻¹ yr⁻¹.

It is an upper bound because it is the **saturated** flux for dry, loose,
unbounded sand: any moisture, vegetation, armour layer or limited supply reduces
the actual flux below it.

---

## ★★6 — The Bruun rule

**(a)** $R = (4\times10^{-3})(8000)/(1.5 + 18) = 32/19.5 = 1.641$ m yr⁻¹.

**(b)** $R = 64/19.5 = 3.282$ m yr⁻¹, exactly twice (a).

**(c)** Assumptions and failures:

1. **The shoreface profile translates landward without changing shape.** Fails
   where the profile is armoured by rock, reef or a seawall, because it cannot
   translate.
2. **Sand is conserved on the profile.** Fails where longshore drift removes or
   delivers sand — which is the normal case on a real open coast.
3. **Two-dimensional, with a fixed closure depth.** Fails where the seabed is
   muddy, where the sediment supply is river-dominated, or where the closure
   depth itself changes with the wave climate.

**(d)** If $h^{*}$ is taken as a multiple of the breaking wave height, then
$h^{*}$ (and usually $L^{*}$, through the shoreface slope) changes with the wave
climate. The formula is still written with $S$ as an independent variable, but
$R$ then depends on storminess and on wave period as well, so a shoreline
retreat computed from sea level alone hides a dependence on the wave forcing.

---

## ★★★7 — Reading the demonstration

Quoted output from `fluvial_coastal_demo.py`:

**(a)** $d = 0.0625$ mm: $v_s = 0.00334$ m s⁻¹, $\mathrm{Re} = 0.21$, Stokes error
$+5.10$ per cent. $d = 0.25$ mm: $0.03397$ m s⁻¹, $\mathrm{Re} = 8.48$,
$+65.12$ per cent. $d = 1.0$ mm: $0.15502$ m s⁻¹, $\mathrm{Re} = 154.71$,
$+478.94$ per cent.

**(b)** $\tau_c$: silt 0.03 mm 0.0219 Pa; fine sand 0.15 mm 0.1093 Pa; medium
sand 0.35 mm 0.2549 Pa; coarse sand 1 mm 0.7284 Pa; gravel 10 mm 7.2839 Pa;
cobble 100 mm 72.839 Pa. For $h = 2$ m and $S = 3\times10^{-4}$
($\tau_b = 5.8860$ Pa), the ratios are 53.87, 23.09, 8.08 and 0.81: gravel
10 mm and coarser are immobile, everything finer moves.

**(c)** $W = 10$ m, $D = 1.0$ m: $V = 0.933$, $Q = 9.33$, $\mathrm{Fr} = 0.298$;
$W = 100$ m, $D = 3.0$ m: $V = 0.943$, $Q = 282.96$, $\mathrm{Fr} = 0.174$.
Hydraulic geometry: $b + f + m = 0.50 + 0.40 + 0.10 = 1.00$, and the
$Q = 1$ m³ s⁻¹ ratios are 0.316, 0.398 and 0.794, which multiply to
$0.316 \times 0.398 \times 0.794 = 0.0998$, i.e. $0.1 = 1/10$ as continuity
requires.

**(d)** $T = 8$ s, $h = 100$ m: $k = 0.06288$ m⁻¹, $L = 99.92$ m, $c = 12.490$
m s⁻¹ ($=gT/2\pi$, the deep-water value); $T = 8$ s, $h = 5$ m: $k = 0.11837$,
$L = 53.08$ m, $c = 6.635$ m s⁻¹, $kh = 0.592$. Breaking depths: 1.43 m for
$H_0 = 1$ m, $T = 6$ s; 2.80 m for 2 m, 8 s; 4.23 m for 3 m, 10 s; 5.73 m for 4 m,
12 s.

**(e)** At $u_{*} = 0.05$ m s⁻¹: fine sand 0.15 mm $P = 0.794$ (wash load);
medium sand 0.35 mm $P = 2.613$ (bedload dominated); coarse sand 1 mm
$P = 7.751$; gravel 10 mm $P = 51.699$.

**(f)** $u_{*t}$: 0.1151, 0.1628, 0.2303, 0.3257 and 0.4606 m s⁻¹ for 0.0625,
0.125, 0.25, 0.5 and 1.0 mm. Potential flux: 67.3 m³ m⁻¹ yr⁻¹ at
$u_{*} = 0.25$ m s⁻¹, 184.8 at 0.35 and 538.8 at 0.50.

**(g)** Bruun retreat: 0.6250 m yr⁻¹, 2.5000 m yr⁻¹ and 2.2727 m yr⁻¹ for the
three cases.

**(h)** The settling velocity, the Shields thresholds and mobility ratios, the
Manning velocities and discharges, the dispersion relation, the breaking depth,
the Rouse number and the Bruun retreat are **computed from derived relations**.
The drag coefficient, the Shields critical value, the Manning roughness, the
Bagnold coefficients and the breaker index are **empirical coefficients** with
stated nominal values. The Rouse thresholds and the "potential flux" label are
**conventions**: the first are conventional band edges rather than physical
boundaries, and the second is an explicitly labelled upper bound, not a
prediction.

---

## ★★★8 — Interpretation and its limits

**(a)** The two strongest contrasts for an 8 m sand body in silty clay:

1. **Electrical resistivity** — clean sand holds fresh water in large pores and
   is one to two orders of magnitude more resistive than clay. Method: electrical
   resistivity tomography (ERT) or electromagnetic induction.
2. **Permittivity / dielectric loss** — dry or fresh-water-saturated sand is
   radar-transparent and low-loss compared with clay. Method: ground-penetrating
   radar.

The sand *fraction* of a floodplain is a poor predictor of yield because a
floodplain made of 40 per cent isolated sand lenses yields little, while one made
of 20 per cent sand in connected ribbons yields a great deal: the yield is set by
**connectivity and by the presence or absence of a clay seal**, not by the
proportion of permeable material.

**(b)** The observed migration corresponds to a small fraction of the potential
flux because the potential flux is the saturated value for dry, loose, unbounded
sand. Three processes that reduce the actual transport:

1. **Moisture** — a small water content raises the threshold friction velocity
   sharply and can suppress transport entirely.
2. **Vegetation and surface crusts** — roots, litter and biological crusts raise
   the threshold and trap grains.
3. **Supply limitation and armouring** — once the available loose sand is
   removed, the surface coarsens and the transport falls, regardless of the wind.

**(c)** From $R = S L^{*}/(B + h^{*})$:
$L^{*}/(B + h^{*}) = R/S = 1.6/0.004 = 400$. With $B + h^{*} \approx 20$ m, that
gives $L^{*} \approx 8000$ m, which is a plausible shoreface width to closure —
which is exactly the problem with the rule: it can always be fitted by choosing
$L^{*}$.

Two independent observations that would test a Bruun-type explanation:

1. **A sediment budget from a dated profile.** If the volume of sand eroded from
   the upper shoreface matches the volume that appears in the landward profile,
   the assumption of conservative translation is supported; a mismatch means the
   sand went elsewhere (or was supplied from elsewhere).
2. **A profile that translates without changing shape.** Repeated surveys of the
   same profile, with the sea-level rise removed, should show a landward
   translation of the *same* curve. A profile that steepens, flattens or moves
   only at its landward end is not Bruun-type.

**(d)** $b + f + m = 0.5 + 0.4 + 0.2 = 1.1 \ne 1$. The exponents violate
**continuity**: $Q = WDV$ demands that a fractional change in discharge be
distributed exactly among the three powers, so the exponents must sum to one. A
set summing to 1.1 implies a 10 per cent error in discharge for a doubling of
discharge — a large systematic error, and a strong indication that the paper
mixed measurements at different stations or defined width or depth differently.
