# Exercises — 25-02-02 Project: Gravity Anomaly of Simple Bodies

Attempt these before reading the
[solutions](./02-simple-gravity-model-solutions.md). The project is
[02 Simple Gravity Model](../02-simple-gravity-model.md). Values printed by
[`code/simple_gravity_model_demo.py`](../code/simple_gravity_model_demo.py):

| Quantity | Demonstration value |
|---|---|
| sphere peak ($\Delta\rho = 500$, $R = 2.0$ km, $z = 5.0$ km) | $4.4732\ \mathrm{mGal}$ |
| cylinder peak (same parameters) | $16.7743\ \mathrm{mGal}$ |
| cylinder / sphere | $3.75$ |
| slab ($t = 500$ m) | $10.4840\ \mathrm{mGal}$ at every depth |
| sphere $x_{1/2}$ | $3.832\ \mathrm{km}$ → $z = 5.000\ \mathrm{km}$ |
| cylinder $x_{1/2}$ | $5.000\ \mathrm{km}$ → $z = 5.000\ \mathrm{km}$ |
| degeneracy, $z = 3 \to 7$ km | $R = 1.423 \to 2.503\ \mathrm{km}$, same peak |

Constants: $G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$. All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the peak anomaly of a buried sphere with
$\Delta\rho = 300\ \mathrm{kg\,m^{-3}}$, $R = 1.5\ \mathrm{km}$ and
$z = 4.0\ \mathrm{km}$. State the unit and the formula used.

**★2.** A profile's half-width is $3.0\ \mathrm{km}$. Give the inferred depth
under the sphere rule and under the cylinder rule, and state the percentage
difference between them.

**★3.** Compute the peak anomaly of an infinite horizontal cylinder with the same
$\Delta\rho$, $R$ and $z$ as ★1, and show that the cylinder/sphere ratio equals
$\frac{3}{2}\,z/R$.

## ★★ Applied

**★★4.** Fix the sphere's peak at the value from ★1 and tabulate the ($z$, $R$)
pairs that reproduce it for $z = 2.0$, $4.0$ and $6.0\ \mathrm{km}$, together with
the sphere half-width $x_{1/2} = 0.7664\,z$ for each. State which column is
degenerate.

**★★5.** A Bouguer slab of $\Delta\rho = 400\ \mathrm{kg\,m^{-3}}$ and
$t = 300\ \mathrm{m}$ produces an anomaly of how many mGal? Conversely, what
thickness of that slab would be needed to explain a $5.0\ \mathrm{mGal}$ anomaly?

**★★6.** A profile has a peak of $6.0\ \mathrm{mGal}$ and a half-width of
$4.0\ \mathrm{km}$. Interpret it twice — once as a sphere and once as a cylinder
— using $\Delta\rho = 500\ \mathrm{kg\,m^{-3}}$ in both cases, and report (depth,
radius) for each interpretation. State which interpretation is more conservative
for the radius and why.

## ★★★ Research-oriented

**★★★7.** Design a measurement campaign that determines the depth of a compact
mass anomaly *without* assuming a shape, given that only the peak anomaly and the
half-width are currently available. State the quantity to be measured, the
instrument class that measures it, the relation that yields depth from the two
quantities measured, and the error budget. Show that the relation is
shape-independent for a point mass, and state the first thing that breaks it.
