# Exercises — 15-03-02 Oceanic Crust Structure and Ophiolites

Attempt these before the [solutions](./02-oceanic-crust-structure-solutions.md).
The lesson is [02 Oceanic Crust Structure and Ophiolites](../02-oceanic-crust-structure.md).
All models and data are **SYNTHETIC** teaching values, and the model constants are
those printed by `code/oceanic_crust_structure_demo.py`.

## ★ Foundational

**★1.** For a two-layer case with $v_0=2.95\ \mathrm{km\,s^{-1}}$,
$v_1=5.10\ \mathrm{km\,s^{-1}}$ and $h_0=0.40$ km, compute $\sin\theta_0$,
$\cos\theta_0$ and the intercept time $t_i$, then give the travel time at an
offset of 15 km. State the unit of every quantity.

**★2.** Two first-arrival branches have intercepts $0.30\ \mathrm{s}$ and
$0.62\ \mathrm{s}$ and velocities $4.00$ and $6.50\ \mathrm{km\,s^{-1}}$. Compute
their crossover distance, and state in one sentence what a spread shorter than
that distance would fail to detect.

**★3.** Name the petrological unit corresponding to seismic layer 2B and explain
in two sentences why its velocity is higher than that of layer 2A, referring to
porosity rather than to depth.

## ★★ Applied

**★★4.** Using the lesson's model (Moho at 5.55 km, mantle intercept
$1.2423\ \mathrm{s}$, mantle velocity $8.10\ \mathrm{km\,s^{-1}}$), compute the
travel time of the mantle refraction at 40 km and at 100 km. State the smallest
spread length that sees the mantle branch and the ratio of that length to the
Moho depth.

**★★5.** Derive the two-layer trade-off coefficient
$\dfrac{\mathrm{d}h/h}{\mathrm{d}v/v}=\dfrac{v_1^2}{v_1^2-v_0^2}$ and evaluate it
for $v_0=3.00$, $v_1=6.00\ \mathrm{km\,s^{-1}}$. If the top-layer velocity is
known to 5% and the true thickness is 0.50 km, what is the thickness uncertainty?

**★★6.** For the lesson's end-members (peridotite $v_p=8.10\ \mathrm{km\,s^{-1}}$,
$\rho=3.30\ \mathrm{g\,cm^{-3}}$; serpentinite $v_p=5.10$, $\rho=2.55$), compute
the Voigt, Reuss and geometric-mean $v_p$ and the Voigt and Reuss density at 30%
serpentine. State which of the three $v_p$ values is a rigorous bound and which is
a model choice.

## ★★★ Research-oriented

**★★★7.** A survey must determine the thickness of layer 2A to 5% for a layer
0.45 km thick. The lesson's Monte Carlo gives a thickness standard deviation of
0.048 km for a 10 ms pick error with the offset ranges used there. Using the
scaling of the estimate's variance with pick error and offset range, specify the
pick accuracy (or the offset range) required, state the assumption that makes the
scaling valid, and say which of the two changes you would choose in practice and
why.

**★★★8.** A refraction line reports a velocity step at 5.5 km below the seafloor,
from $6.8$ to $7.5\ \mathrm{km\,s^{-1}}$. Enumerate the models that explain it —
including a serpentinised mantle, a thick gabbro-to-peridotite transition, and an
underplated body — and for each state the observable that would distinguish it,
the measurement precision required, and the one model that remains untestable
with the measurements you listed. Use the mixing numbers of §3.5 of the lesson
where they apply.
