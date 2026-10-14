# Exercises — 02-01-01 Physical Quantities, SI Units and Dimensional Homogeneity

Attempt these **closed-book** before opening the
[solutions](./01-physical-quantities-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Unless a problem says otherwise, use $G = 6.674\,30\times10^{-11}\ \mathrm{m^3\,kg^{-1}\,s^{-2}}$,
$GM_\oplus = 3.986\,004\,418\times10^{14}\ \mathrm{m^3\,s^{-2}}$ (defining),
$a = 6\,378\,137$ m (defining), $\omega = 7.292\,115\times10^{-5}$ rad/s
(defining), and $g_n = 9.806\,65\ \mathrm{m\,s^{-2}}$ (exact).

---

## ★ Foundational

**★1.** Convert to coherent SI units, showing the exact conversion factor you
use: (a) $3.2$ mGal; (b) $250$ nT; (c) $3.5$ km/s in km/h; (d) $45\ \mu\mathrm{W\,m^{-3}}$;
(e) $0.15$ m/s in mm/yr (use $1\ \mathrm{yr} = 3.1557\times10^{7}$ s).

---

**★2.** How many significant figures does each value carry, and is the value
exact or measured? (a) `6371 km`; (b) `6.674 30 × 10⁻¹¹ m³ kg⁻¹ s⁻²`;
(c) `1 mGal = 10⁻⁵ m s⁻²`; (d) `9.806 65 m/s²`; (e) `3 300 kg/m³`.

---

**★3.** Decide whether each equation is dimensionally homogeneous by writing
the dimensions of both sides:

(a) $v^{2} = 2gh$; (b) $p = \rho g h$; (c) $q = -k\,\dfrac{dT}{dz}$;
(d) $E = \tfrac12 m v^{2}$; (e) $\omega = \sqrt{g/L}$;
(f) $v_p = \sqrt{\mu/\rho}$.

---

**★4.** Derive the dimensions of these quantities from their defining
equations, not from memory:

(a) seismic moment, $M_0 = \mu A D$, with $\mu$ in Pa, $A$ an area, $D$ a slip;
(b) hydraulic conductivity, from $\mathbf{v} = -K\,\nabla h$ with $h$ a head in
metres and $\mathbf{v}$ a velocity — and explain why $K$ has the same dimension
as a velocity;
(c) the Eötvös unit, defined as $10^{-9}\ \mathrm{s^{-2}}$; (d) surface heat
flow; (e) magnetic dipole moment, from the far-field $B \propto \mu_0 m/r^{3}$.

---

## ★★ Applied

**★★5.** Using $g = GM_\oplus/R^{2}$: (a) evaluate $g$ at
$R = 6\,371$ km and at $R = 6\,375$ km; (b) compute the difference and compare it
with the vertical gradient $2GM/R^{3}$ multiplied by the 4 km change; (c) explain
in one sentence why the two answers in (b) agree only approximately.

---

**★★6.** A relative gravimeter resolves 0.01 mGal. (a) Compute the vertical
gravity gradient $2GM_\oplus/R^{3}$ at $R = 6\,371$ km in mGal m⁻¹. (b) What
elevation error produces a 0.01 mGal error? (c) A station is levelled to 3 cm.
What gravity error does that imply? (d) State one other term that must appear in
the budget before the instrument resolution is the limiting factor.

---

**★★7.** The Bouguer slab correction is $\Delta g = 2\pi G\rho t$.
(a) Evaluate $2\pi G\rho$ for $\rho = 2670\ \mathrm{kg\,m^{-3}}$ and express the
result in mGal per metre. (b) Confirm the practitioners' rule
$\Delta g\,[\mathrm{mGal}] \approx 0.04193\,\rho\,[\mathrm{g\,cm^{-3}}]\,
t\,[\mathrm{m}]$. (c) Compute $\Delta g$ for a 500 m slab of that density.
(d) If $\rho$ is uncertain by $50\ \mathrm{kg\,m^{-3}}$, what uncertainty in
$\Delta g$ does that produce?

---

**★★8.** A quantity is $g = GM_\oplus/R^{2}$, with $GM_\oplus$ known to a
relative uncertainty of $10^{-9}$ and $R$ to 0.1 m. (a) Compute the relative
uncertainty in $g$ from the quadrature rule. (b) Which term dominates?
(c) A student reports $g$ to 12 significant figures. Critique the report.

---

## ★★★ Research-oriented

**★★★9.** Construct a dimensionless group for each of these problems by
supplying the variable list yourself, then verify with a rank argument (write the
exponent matrix and compute its rank):

(a) the period of a pendulum;
(b) the depth of penetration of a magnetic field into a conductor (variables:
conductivity, permeability, angular frequency, depth — note the combination
$\delta = \sqrt{2/(\mu_0\sigma\omega)}$);
(c) the escape velocity from a planet, from $(G, M, R)$.

For each, state which variable dropped out and why that is physically correct.

---

**★★★10.** The dimensions of the seismic moment $M_0$ and of an energy are
identical. (a) Verify this. (b) Compute $M_0$ for a synthetic source with
$\mu = 30$ GPa, a fault $10\ \mathrm{km}\times5\ \mathrm{km}$ and 1 m of slip.
(c) Using the relation $E_s \approx (\Delta\sigma/2\mu) M_0$ with an **assumed**
stress drop $\Delta\sigma = 3$ MPa, compute the fraction $E_s/M_0$.
(d) Explain, in three sentences, why the two quantities can share a dimension and
still be physically different, and say what measurement would distinguish them.
