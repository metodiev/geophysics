# Exercises — Ice Sheet Marine Margins and Stability

Use the relations of
[`../03-ice-sheet-marine-margins.md`](../03-ice-sheet-marine-margins.md) and
`code/ice_sheet_marine_margins_demo.py`. **All models and data are SYNTHETIC.**

$h_g=1.1210\,d$, freeboard $=0.1079\,h$,
$q(h)=22032\ (h/1000)^5\ \mathrm{m^2\,yr^{-1}}$,
$h=\rho_ih_g\ldots$ — and the pivot formula
$h_{\text{eq}}=1000\,(aW/22032)^{0.2}$.

## ★ Foundational

**1.1 — Flotation.** An ice sheet is grounded in 700 m of water. Compute the
grounding-line thickness and the freeboard. State which of the two numbers a
bathymetric survey can measure directly.

**1.2 — Flux law.** Using the pivot formula, compute the discharge per unit width for
thicknesses of 900 m and 1100 m. What percentage change in discharge results from a
10% thickness change, and does it equal the exponent?

**1.3 — Back stress versus driving stress.** For a 400 m thick ice shelf, compute the
unconfined back stress and the driving stress (surface slope 0.01) and give their
ratio.

## ★★ Applied

**2.1 — Equilibrium thickness.** A catchment 150 km wide delivers a surface mass
balance of 0.25 m/yr. Compute the equilibrium thickness, the corresponding water
depth, and how much the thickness changes if the accumulation is halved.

**2.2 — Disequilibrium on a retrograde bed.** The grounding line retreats 6 km on a
bed that deepens inland at 15 m/km, starting from $d=1090$ m,
$q=60000\ \mathrm{m^2\,yr^{-1}}$. (a) Compute the new depth, thickness and flux.
(b) Compute $\mathrm{d}q/\mathrm{d}x$ and the disequilibrium distance.
(c) State whether an equilibrium exists.

**2.3 — Buttressing loss.** Losing half of the extra resistance of a shelf is
represented by $\beta=0.5$. Compute the required equilibrium thickness, the
corresponding water depth, and the inland shift on a 10 m/km retrograde bed.

## ★★★ Research-oriented

**3.1 — Two competing clocks.** A 80 km wide shelf 500 m thick is melted at
25 m/yr while accumulating 0.25 m/yr over a 200 km catchment. (a) Compare the melt
flux with the supply flux. (b) Compute the time to remove the shelf's cross-section
per unit width with no inflow. (c) Explain why the answer is not a prediction of
collapse, and what would have to be added to make it one.

**3.2 — Why the model gives no rate.** The static balance gives an excess flux of
about $3\times10^4\ \mathrm{m^2\,yr^{-1}}$ at 10 km of retreat. (a) Show that
dividing this by a thickness gives a velocity of order
$10^2\ \mathrm{m\,yr^{-1}}$… or does it? Perform the division by $h=1334$ m, state
the units of the result, and explain why it is not a retreat rate.
(b) State which additional physical ingredient converts an excess flux into a
retreat rate.

**3.3 — Stability criterion.** (a) Show, from $q\propto h^5$ and $h\propto d$, that
$\mathrm{d}q/\mathrm{d}x>0$ inland implies the instability, and that
$\mathrm{d}d/\mathrm{d}x<0$ (a prograde bed) reverses it. (b) Explain why a prograde
bed does not guarantee stability if the catchment shrinks or the shelf is removed.
