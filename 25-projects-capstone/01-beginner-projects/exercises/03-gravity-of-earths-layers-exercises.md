# Exercises — 25-01-03 Project: Computing Gravity Through a Layered Earth

Attempt these before reading the
[solutions](./03-gravity-of-earths-layers-solutions.md). The project is
[03 Gravity of Earth's Layers](../03-gravity-of-earths-layers.md). Values printed
by [`code/layered_earth_gravity_demo.py`](../code/layered_earth_gravity_demo.py):

| Quantity | Demonstration value |
|---|---|
| model mass | $5.9620\times10^{24}\ \mathrm{kg}$ |
| mean density | $5504.0\ \mathrm{kg\,m^{-3}}$ |
| surface $g$ | $9.8035\ \mathrm{m\,s^{-2}}$ |
| CMB (3480 km) $g$ | $10.7900\ \mathrm{m\,s^{-2}}$ |
| max $g$ | $10.7881\ \mathrm{m\,s^{-2}}$ at $r = 3480.9\ \mathrm{km}$ |
| $g$ at 1000 km | $3.6596\ \mathrm{m\,s^{-2}}$ |
| uniform-sphere $g$ at CMB | $5.3563\ \mathrm{m\,s^{-2}}$ |
| crust 2800→3000 kg m⁻³ | $+415.90$ ppm = $+4.078\ \mathrm{mGal}$ |
| Monte Carlo $\rho_c = 2800\pm100$ | $9.803301 \pm 0.002005\ \mathrm{m\,s^{-2}}$ ($200.51\ \mathrm{mGal}$) |

All model values are **SYNTHETIC** teaching numbers.

## ★ Foundational

**★1.** Compute the mass of a uniform shell with
$\rho = 4000\ \mathrm{kg\,m^{-3}}$, $r_\text{in} = 5000\ \mathrm{km}$ and
$r_\text{out} = 6000\ \mathrm{km}$. State the unit and the volume used.

**★2.** Use the demonstration's mean density and radius to compute the surface
$g$ of a uniform sphere, and state whether it agrees with the model's
$9.8035\ \mathrm{m\,s^{-2}}$.

**★3.** Compute $g$ at $r = 1000\ \mathrm{km}$ for a *uniform* sphere of density
$5504.0\ \mathrm{kg\,m^{-3}}$, and compare it with the demonstration's layered
value of $3.6596\ \mathrm{m\,s^{-2}}$ by forming the ratio.

## ★★ Applied

**★★4.** Verify the demonstration's CMB entry: show that
$M = 1.9578\times10^{24}\ \mathrm{kg}$ at $r = 3480\ \mathrm{km}$ gives
$g = 10.7900\ \mathrm{m\,s^{-2}}$, and compute the enclosed mass fraction at that
radius.

**★★5.** Derive analytically the change in surface gravity produced by
$+200\ \mathrm{kg\,m^{-3}}$ in the crust, using the crustal volume of
$1.2399\times10^{19}\ \mathrm{m^{3}}$, and compare with the demonstration's
$+4.078\ \mathrm{mGal}$. Then compare the per-kg m⁻³ slope with the Monte Carlo
scatter of $200.51\ \mathrm{mGal}$ for $\pm100\ \mathrm{kg\,m^{-3}}$.

**★★6.** The uniform-sphere value at the CMB is $5.3563\ \mathrm{m\,s^{-2}}$ and
the layered value is $10.7900\ \mathrm{m\,s^{-2}}$. Compute the ratio and state
which single feature of the model is responsible for the difference.

## ★★★ Research-oriented

**★★★7.** Design an inversion of the gravity profile: suppose $g(r)$ is measured
at 40 radii between the CMB and the surface with $0.5\%$ relative uncertainty,
and you wish to recover the five layer densities. State the model
parametrisation, the sensitivity matrix and its size, whether the problem is
over- or under-determined, what the null space contains for this parametrisation,
and one independent observation that would reduce it. A design that could not be
executed is a failed answer.
