# Solutions — 25-01-01 Project: Units, Conversions and First Scientific Plots

> Read after attempting. Lesson:
> [01 Units and Plotting](../01-units-and-plotting.md). All values are
> **SYNTHETIC** teaching numbers printed by
> [`code/units_and_plotting_demo.py`](../code/units_and_plotting_demo.py).

---

## ★1 — Conversions with factors

| Value | Factor to SI | SI value | SI unit |
|---|---|---|---|
| $1.5\ \mathrm{mGal}$ | $\times 10^{-5}$ | $1.5\times10^{-5}$ | m s⁻² |
| $2.67\ \mathrm{g\,cm^{-3}}$ | $\times 10^{3}$ | $2670$ | kg m⁻³ |
| $5.80\ \mathrm{km\,s^{-1}}$ | $\times 10^{3}$ | $5800$ | m s⁻¹ |
| $2.4\ \mathrm{km}$ | $\times 10^{3}$ | $2400$ | m |
| $48\,000\ \mathrm{nT}$ | $\times 10^{-9}$ | $4.8\times10^{-5}$ | T |

Each factor is exact by the definition of the prefixed unit; no uncertainty is
attached to a conversion.

---

## ★2 — The two gradients

$$\frac{2g}{R} = \frac{2 \times 9.8203}{6.371\times10^{6}}
= 3.0828\times10^{-6}\ \mathrm{m\,s^{-2}\,m^{-1}}
= 0.3083\ \mathrm{mGal\,m^{-1}}.$$

Unit: acceleration per length; dividing by $10^{-5}\ \mathrm{m\,s^{-2}}$ per mGal
gives mGal m⁻¹.

For $\rho = 2900\ \mathrm{kg\,m^{-3}}$,

$$2\pi G\rho = 2\pi \times 6.67430\times10^{-11} \times 2900
= 1.2162\times10^{-6}\ \mathrm{m\,s^{-2}\,m^{-1}}
= 0.1216\ \mathrm{mGal\,m^{-1}}.$$

The Bouguer gradient scales linearly with density, so it is
$0.1120 \times (2900/2670) = 0.1216\ \mathrm{mGal\,m^{-1}}$ — a useful
cross-check between two routes to the same number.

---

## ★3 — Dimensional check

$$[2\pi G \rho h] = (\mathrm{m^{3}\,kg^{-1}\,s^{-2}})(\mathrm{kg\,m^{-3}})(\mathrm{m})
= \mathrm{m\,s^{-2}} = [\Delta g].$$

The two sides agree: the formula is dimensionally homogeneous. Note that the
check passes for *any* constant in front of $G\rho h$; dimensional analysis can
reject a wrong formula but never proves the coefficient.

---

## ★4 — A 250 m station correction

Free-air: a station 250 m higher reads *lower*, so the correction to bring it to
the reference level is

$$\Delta g_{\mathrm{FA}} = 0.3083 \times 250 = 77.08\ \mathrm{mGal},$$

added back (positive).

Bouguer: the rock between the two levels also pulls the station down, so the
slab term is

$$\Delta g_{\mathrm{B}} = 0.1120 \times 250 = 28.00\ \mathrm{mGal},$$

also added back, but partially cancelling the free-air term.

Combined correction $= 77.08 - 28.00 = 49.08\ \mathrm{mGal}$ (to be added to the
observed value), with the sign convention that both are *subtracted from* the
free-air-corrected value in the standard reduction chain. Reporting $49.08\
\mathrm{mGal}$ without the convention is the error this item is testing.

---

## ★5 — Caption arithmetic

(a) $119 \times 500\ \mathrm{m} = 59\,500\ \mathrm{m} = 59.5\ \mathrm{km}$.

(b) $\mathrm{SEM} = 57.1/\sqrt{30} = 57.1/5.477 = 10.43\ \mathrm{m}$ — twice the
demonstration's $5.21\ \mathrm{m}$, because the standard error falls as
$1/\sqrt{n}$ and $n$ fell by a factor of 4.

(c) The horizontal-extent line changes from "$0$ to $29.75\ \mathrm{km}$" to
"$0$ to $59.5\ \mathrm{km}$"; the SEM line changes from $5.21$ to $10.43\
\mathrm{m}$. The depth range and the spacing line are unaffected by (a); the
depth range is unaffected by (b) but quoted differently in the caption.

---

## ★6 — The factor of $10^{3}$

The colleague used $2.67\ \mathrm{kg\,m^{-3}}$ instead of
$2670\ \mathrm{kg\,m^{-3}}$, losing a factor of $10^{3}$. The correct gradient is
$1.1197\times10^{-6}\ \mathrm{m\,s^{-2}\,m^{-1}}$ (the demonstration's value),
$10^{3}$ times their $1.12\times10^{-9}$.

**Sanity check.** A rock density must be of order $10^{3}\ \mathrm{kg\,m^{-3}}$;
$2.67\ \mathrm{kg\,m^{-3}}$ is the density of air at altitude. Comparing the
converted value's order of magnitude with the expected physical range is a
one-line test that catches the whole family of lost-factor errors.

---

## ★★★7 — A unit-hygiene procedure

**Where conversion happens.** Convert **at ingestion**: the loader owns the
factor table and emits SI columns only. Storing field units and converting on
demand is the arrangement in which two scripts disagree, so it is rejected.

**How units are recorded.** Every stored column carries a unit string in a
machine-readable schema — a table of `(column, unit, si_unit)` rows checked into
the repository next to the data. The unit is data, not a comment.

**The automated test.** A validation step asserts, for every column, that a unit
is present and that it is one of the allowed strings. It fails the pipeline when
a column has no unit. A second test asserts that every *derived* column's unit
equals the unit obtained by substituting the input columns' units into the
formula — for a speed, $\mathrm{m}/\mathrm{s}$; for a gradient,
$\mathrm{m\,s^{-2}}/\mathrm{m}$. A third test compares a converted value's order
of magnitude against a declared physical range (density
$2\times10^{3}$–$3\times10^{3}\ \mathrm{kg\,m^{-3}}$, say) and warns when it
falls outside.

**Derived columns.** The schema stores units for inputs and for outputs. A
derived column's unit is computed from the formula, then compared with the
declared output unit; a mismatch fails the build. This is what makes the free-air
and Bouguer gradients safe: both are declared
$\mathrm{m\,s^{-2}\,m^{-1}}$, and any change to the formula that breaks that unit
is caught before it reaches a figure.
