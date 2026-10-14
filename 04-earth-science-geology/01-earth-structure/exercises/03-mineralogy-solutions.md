# Solutions — 04-01-03 Rock-Forming Minerals and Their Physical Properties

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — Density from a unit cell

**(a)** With $V = 664.5\times10^{-24}$ cm³,
$$\rho = \frac{ZM}{N_A V} = \frac{4\times262.223}{6.02214076\times10^{23}\times664.5\times10^{-24}}
= \frac{1048.89}{400.17} = 2.621\ \text{g/cm}^3 .$$

**(b)** The measured value is 2.62 g/cm³, so the calculation is right to
0.05 per cent.

**(c)** It verifies that the **structural input is self-consistent**: the cell
contents $Z$, the cell volume and the formula mass agree with each other and
with the measured density. It does not verify that the mineral is albite — an
X-ray diffraction pattern or a chemical analysis does that. A density is a
*consequence* of a structure, and checking it is a way of catching a wrong
structure, not a way of identifying a mineral.

---

## ★2 — Moduli from measured velocities

**(a)** $G = 2750 \times (3900)^2 = 4.183\times10^{10}$ Pa $= 41.8$ GPa.

**(b)** $v_p^2 = 5.184\times10^7$, $\frac43v_s^2 = 2.028\times10^7$, so
$K = 2750 \times 3.156\times10^7 = 8.679\times10^{10}$ Pa $= 86.8$ GPa.

**(c)** $\nu = (3\times86.8 - 2\times41.8)/(2(3\times86.8 + 41.8))
= 176.8/688.4 = 0.292$.

**(d)** 0.29 is at the high end of typical for a silicate — the usual range is
0.2 to 0.3 — which is consistent with a slightly compressible mineral. Values
above 0.33 in a rock suggest a soft or fluid-saturated framework rather than a
different mineralogy.

---

## ★3 — Mean atomic number

**(a)** $\bar Z = (20 + 2\times13 + 2\times14 + 8\times8)/13 = 138/13 = 10.615$.

**(b)** $\bar Z = (20 + 12 + 2\times6 + 6\times8)/10 = 92/10 = 9.20$.

**(c)** Anorthite is separated least well from quartz and calcite: its mean
atomic number is 10.62 against 10.00, a ratio of $(10.615/10)^3 = 1.20$ in the
photoelectric cross section. Dolomite, at 9.20, is *lower* than calcite and
quartz, so it is separated from them by 20 per cent in the opposite direction —
and it is separated from calcite much better on a photoelectric log than on
density, where the two differ by only 6 per cent.

---

## ★★4 — Error propagation in a modulus

**(a)** $G = 5010\times4700^2 = 1.107\times10^{11}$ Pa $= 110.7$ GPa;
$K = 5010(8100^2 - \frac43\times4700^2) = 5010\times3.616\times10^7
= 1.811\times10^{11}$ Pa $= 181.1$ GPa; $\nu = 0.246$.

**(b)** With $v_s \to 4935$ m/s (5 per cent higher) and $v_p$ unchanged,
$K = 5010(6.561\times10^7 - 3.247\times10^7) = 5010\times3.314\times10^7
= 1.660\times10^{11}$ Pa $= 166.0$ GPa.

**(c)** $K$ falls by 8.35 per cent for a 5 per cent velocity error. The reason is
that $K = \rho(v_p^2 - \frac43v_s^2)$ is a **difference of two comparable
terms** — here $6.561\times10^7$ and $3.247\times10^7$ — so a 10 per cent change
in the smaller term changes the difference by about 20 per cent of it, i.e. by
about 8 per cent of $K$. (The 10 per cent is the *squared* velocity change; a
5 per cent velocity error is 10.25 per cent in $v_s^2$.) Cancellation amplifies
relative errors, and this is why $K$ is the least well determined modulus of the
three.

---

## ★★5 — Porosity and saturation

**(a)** $\phi = 1 - \rho_b/\rho_g = 1 - 2.35/2.68 = 0.123$, i.e. 12.3 per cent.

**(b)** Water-saturated:
$\rho = (1-0.123)\times2.68 + 0.123\times1.00 = 2.35 + 0.123 = 2.47$ g/cm³.

**(c)** Gas-saturated with $\rho_\text{gas} = 0.10$ g/cm³:
$\rho = 2.35 + 0.123\times0.10 = 2.362$ g/cm³.

**(d)** The contrast between (b) and (c) is 0.111 g/cm³ = 111 kg/m³, or
4.7 per cent of the saturated density. A time-lapse gravity survey designed to
detect a depleted or gas-filled reservoir is looking for a signal of that size,
which is why the survey must resolve a few microgal and why the pore geometry
and the fluid density both have to be modelled.

---

## ★★6 — One log cannot do it

**(a)** $(2.71-2.65)/2.65 = 2.3$ per cent.

**(b)** $(3.22-2.65)/2.65 = 21.5$ per cent.

**(c)** A photoelectric log can separate forsterite from quartz (both have
$\bar Z = 10.00$, so in fact it **cannot** separate them — see below) — the
resolution is in the *density* contrast. Restated correctly: the photoelectric
log cannot separate any of the three, because quartz, calcite and forsterite all
have $\bar Z = 10.00$ and their $(Z/10)^3$ ratios are all exactly 1. Density
separates forsterite from the other two by 21 per cent, but separates quartz
from calcite by only 2.3 per cent.

**(d)** The ambiguity matters wherever a quartz-rich rock must be distinguished
from a carbonate one — a sandstone reservoir next to a limestone, or a
carbonate-hosted ore body in a siliceous host. Neither the photoelectric log nor
the density log alone will do it, and the practical solution is to use a
velocity or a $v_p/v_s$ measurement, which responds to the elastic contrast
rather than to the atomic or the mass contrast.

---

## ★★★7 — Density error propagation

**(a)** $\rho = 4\times140.693/(6.02214076\times10^{23}\times290.30\times10^{-24})
= 562.77/174.82 = 3.219$ g/cm³.

**(b)** $Z = 3$: 2.414 g/cm³. $Z = 5$: 4.024 g/cm³.

**(c)** $Z = 3$ gives $-25.0$ per cent and $Z = 5$ gives $+25.0$ per cent against
the measured 3.22. A 25 per cent error in a computed density is the signature of
a **wrong cell content**, not of a rounding or an experimental error: the
formula is so nearly exact that only a wrong $Z$ or a wrong formula mass can move
the answer by tens of per cent.

**(d)** Increasing $V$ by 2 per cent gives 3.156 g/cm³, a decrease of 2.0 per
cent. At 100 km depth the pressure is about 3 GPa, and mantle minerals are
compressed by several per cent at that pressure even before any phase change, so
a laboratory cell volume **cannot** be used directly: the density at depth is
larger, and an equation of state is required to extrapolate it. That is the
subject of [02-11-02 Equations of State](../../../02-physics/11-physics-of-earths-interior-and-atmosphere/02-equations-of-state.md).

---

## ★★★8 — The demo's output

**(a)** quartz 2.649 against 2.65 (−0.0 per cent); forsterite 3.219 against 3.22
(−0.0); calcite 2.710 against 2.71 (0.0); halite 2.164 against 2.17 (−0.3);
pyrite 5.011 against 5.01 (0.0); hematite 5.256 against 5.26 (−0.1).

**(b)** Quartz: $G = 44.3$, $K = 37.9$ GPa, $\nu = 0.079$. Calcite:
$G = 29.5$, $K = 75.1$ GPa, $\nu = 0.326$. The contrast is that calcite is twice
as stiff in compression and 50 per cent softer in shear, so the two have very
different $v_p/v_s$ ratios — 1.48 for quartz against 1.97 for calcite.

**(c)** quartz 10.00, forsterite 10.00, calcite 10.00, halite 14.00, pyrite
19.33, hematite 15.20.

**(d)** Electron densities: quartz 0.80, calcite 0.82, halite 0.63, forsterite
0.96, pyrite 1.46, hematite 1.51, in units of $10^{24}$ e/cm³. The range is a
factor of 2.4, while the density range is a factor of 2.4 as well — but the
*orderings* differ: halite has the lowest electron density and the lowest mass
density, pyrite and hematite the highest of both, while forsterite is second in
electron density but third in mass density.

**(e)** At $\phi = 0.30$: dry 1.855 g/cm³, water-saturated 2.155 g/cm³, a
contrast of 0.30 g/cm³.

**(f)** The cell volumes, formula masses, atomic numbers, measured densities and
measured velocities are all `TABULATED` inputs. Every density, modulus, mean
atomic number, electron density and bulk density above is computed from them.
The density table prints the computed value next to the measured one precisely so
that the reader can see which is which.

---

## ★★★9 — Designing a discrimination

**(a)** At the same porosity, a quartz sandstone has grain density 2.65 and a
limestone 2.71 g/cm³, so:

| Measurement | Quartz sandstone | Limestone | Separates? |
|---|---|---|---|
| Bulk density | $0.8\times2.65 + 0.2\times1.0 = 2.32$ | $0.8\times2.71+0.2 = 2.37$ | Weakly: 2 per cent |
| $v_p$ | about 3.6 km/s | about 4.3 km/s | Yes, and strongly |
| $v_p/v_s$ | about 1.6 | about 1.9 | Yes, very strongly |
| Photoelectric $\bar Z$ | 10.00 | 10.00 | Not at all |

**(b)** Ranking, best first: $v_p/v_s$, then $v_p$, then bulk density, then the
photoelectric log.

**(c)** The best pair is **$v_p$ and $v_s$**, because the two measurements
separate the rocks through *different* elastic contrasts: calcite's bulk modulus
is twice quartz's while its shear modulus is only two-thirds, so it raises $v_p$
and lowers $v_s$ simultaneously. Using the ratio $v_p/v_s$ exploits both at once
and removes the common dependence on porosity, which is the quantity that would
otherwise confound the comparison. The physical reason the pair works is that
carbonate and silicate stiffnesses differ in *opposite directions* for the two
moduli, whereas their densities differ in the same direction and only slightly.
