# Solutions — 04-08-01 Solar System Architecture and Formation

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Kepler's third law

**(a)** $a = 2.5\times1.495\,978\,707\times10^{11} = 3.7399\times10^{11}$ m, so
$a^3 = 5.2306\times10^{34}$ m³ and

$$T = 2\pi\sqrt{\frac{a^3}{GM}}
= 2\pi\sqrt{\frac{5.2306\times10^{34}}{1.327\,1244\times10^{20}}}
= 1.2475\times10^8\ \mathrm{s} = 3.952\ \mathrm{yr}.$$

**(b)** $v = 2\pi a/T = 2\pi(3.7399\times10^{11})/1.2475\times10^8
= 1.883\times10^4$ m s⁻¹ $= 18.84$ km s⁻¹.

**(c)** $29.79/\sqrt{2.5} = 18.84$ km s⁻¹ ✓. The scaling is exact for circular
orbits, because $v = \sqrt{GM/a}$ and $T \propto a^{3/2}$ are the same relation.

**(d)** The astronomical unit is **defined** — its value in metres is exact by
convention — and the sidereal year is **measured**. $GM_\odot$ is therefore
measured by this calculation, and that is why the gravitational parameter rather
than the mass is the tabulated quantity.

---

## ★2 — Equilibrium temperature

**(a)** 407.7 K at 0.39 au, 254.6 K at 1.0 au and 111.6 K at 5.2 au.

**(b)** A body intercepts sunlight over its cross section $\pi R^2$ and radiates
from its whole surface $4\pi R^2$. The ratio is 4, and it is the reason the
equilibrium temperature is lower than a naive "solar constant" temperature by
$4^{1/4} = 1.414$.

**(c)** $288 - 254.6 = 33.4$ K.

**(d)** The calculation knows about the Sun, the distance and the albedo, and
nothing else. Every departure of the real surface temperature from $T_\mathrm{eq}$
must come from something inside or around the planet, and the atmosphere is the
only candidate. So the difference is a measurement of the atmosphere's radiative
effect, obtained by subtracting two quantities that are independently known.

---

## ★3 — The ice line

**(a)** $a = \sqrt{(1-A)L/(16\pi\sigma T^4)}
= \sqrt{0.7(3.828\times10^{26})/(16\pi(5.670\,374\times10^{-8})(170)^4)}
= 3.355\times10^{11}$ m $= 2.243$ au.

**(b)** 200 K gives 1.620 au and 273 K gives 0.870 au.

**(c)** All four giant planets orbit beyond 5 au, well outside even the 2.243 au
of part (a). Beyond the ice line, water is not merely present but *abundant*, so
a growing core has far more condensable mass available and reaches the size at
which it can capture hydrogen and helium from the disk before the gas disperses.
The temperature therefore determines where a planet *can* grow large *quickly*,
which is what the giant planets require.

**(d)** The star's luminosity (which sets the flux), and the disk's own thermal
structure (opacity, internal heating and radial temperature profile). The albedo
matters too, and for a disk of grains the effective albedo is not a single
number.

---

## ★4 — Escape and retention

**(a)** $v_\mathrm{esc} = \sqrt{2(4.9\times10^{12})/1.5\times10^6}
= \sqrt{6533} = 2.558\times10^3$ m s⁻¹.

**(b)** $v_\mathrm{th} = \sqrt{3kT/m}
= \sqrt{3(1.380\,649\times10^{-23})(300)/(44.009\times1.6605\times10^{-27})}
= \sqrt{1.7008\times10^5} = 412.4$ m s⁻¹.

**(c)** $\lambda = (v_\mathrm{esc}/v_\mathrm{th})^2 = (2558/412.4)^2 = 38.5$,
above 25, so CO₂ is retained.

**(d)** $\lambda$ halves, because $\lambda \propto 1/T$: the escape parameter
compares an escape energy with a thermal energy, and raising the temperature
raises the thermal energy proportionally. Note that the *escape rate* falls much
faster than $1/T$ — the fraction of molecules above the escape speed is
$\propto e^{-\lambda}$ — which is why a modest change in exospheric temperature
changes atmospheric loss by orders of magnitude, and why $\lambda$ is only as
good as the temperature you put into it.

---

## ★★5 — Running the Kepler section

**(a)** Derived $GM = 1.327\,128\times10^{20}$ m³ s⁻²; tabulated
$1.327\,124\times10^{20}$; relative difference $2.931\times10^{-6}$.

**(b)** $GM_\text{Earth} + GM_\text{Moon} = 4.0351\times10^{14}$ m³ s⁻², which is
$3.040\times10^{-6}$ of $GM_\odot$ — the same 3 parts per million as the
residual. The coincidence is not a coincidence: the orbit whose period and
distance were used is the Earth–Moon barycentre's, and it responds to the Sun
plus the Earth–Moon system, so the derived value contains both masses. The
calculation has measured the Earth as a by-product, and the demo demonstrates the
residual rather than asserting it.

**(c)** $a = 3\times1.496\times10^{11} = 4.488\times10^{11}$ m, so

$$T = 2\pi\sqrt{\frac{(4.488\times10^{11})^3}{1.327\,1244\times10^{20}}}
= 1.640\times10^8\ \mathrm{s} = 5.196\ \mathrm{yr},$$

and $v = 2\pi a/T = 17.20$ km s⁻¹, which also follows from
$29.79/\sqrt3 = 17.20$ km s⁻¹.

**(d)** The sidereal year is the period of the Earth's orbit against the fixed
stars, which is what Kepler's law refers to; the tropical year is defined against
the equinox and is shorter by about 20 minutes because of precession, which
would introduce a spurious 4 part in 10⁵ error into (3).

---

## ★★6 — The escape parameter and its limits

**(a)** H₂: $\lambda = 10.1$, not retained. He: 20.1, not retained. N₂: 140.5,
retained. CO₂: 220.8, retained.

**(b)** Setting $\lambda = 25$ and solving for $T$:

$$T = \frac{2GMm}{3kR\lambda}
= \frac{2(3.986\times10^{14})(2.016\times1.6605\times10^{-27})}
{3(1.380\,649\times10^{-23})(6.371\times10^6)(25)} = 404.5\ \mathrm{K}.$$

The Earth's exosphere is of order 1000 K, well above 404 K, so hydrogen escapes —
which is the observed behaviour and the reason the Earth is not a gas giant.

**(c)** For water on Mars at an assumed 250 K the criterion gives
$\lambda = 73$, i.e. "retained", yet Mars has lost most of its water. The
criterion is wrong for water because water does not escape as H₂O: it is
photodissociated in the upper atmosphere by ultraviolet light, and the hydrogen
atoms produced escape individually — a chemical and non-thermal process that a
thermal escape parameter does not describe at all.

**(d)** It is useful for *ordering* gases on a body — which of hydrogen, helium,
nitrogen and carbon dioxide a given body can hold — and hence for explaining the
broad compositional difference between the terrestrial and giant planets. It is
not useful as a quantitative statement about how much of a species remains,
because it says nothing about photochemistry, ion pickup, sputtering or the
supply of the gas in the first place.

---

## ★★7 — The angular-momentum budget

**(a)** Total planetary orbital angular momentum
$3.1342\times10^{43}$ kg m² s⁻¹; Jupiter holds 61.49 per cent and Saturn 24.97
per cent; the Sun's mass share is 99.8661 per cent.

**(b)** With $I = 0.40MR^2$ the Sun's rotational angular momentum is
$1.1033\times10^{42}$ kg m² s⁻¹, or 3.400 per cent of the system total; with
$I = 0.06MR^2$ it is $1.6550\times10^{41}$, or 0.525 per cent.

**(c)** $L = m\sqrt{GMa(1-e^2)}$. For $m = 5.9722\times10^{24}$ kg at
$a = 30.05$ au (the value used for Neptune's semimajor axis) and $e \approx 0$:
$L = 5.9722\times10^{24}\sqrt{1.327\,1244\times10^{20}\times4.495\times10^{12}}
= 5.9722\times10^{24}\times2.4427\times10^{16} = 1.459\times10^{41}$ kg m² s⁻¹.
Neptune's is $2.501\times10^{42}$, about **17 times larger**, and the reason is
simply that Neptune is 17 times more massive: at the same distance the angular
momentum is proportional to the mass, and the distance is what it is.

**(d)** The problem: the Sun holds 99.87 per cent of the mass and the planets
hold 96.6 per cent or more of the angular momentum, whereas a collapsing cloud
that conserves angular momentum should have produced a rapidly rotating Sun, so
something must have transported angular momentum outward. The robust part of (b)
is the conclusion: 3.4 per cent is an upper bound from an over-estimate of the
Sun's moment of inertia, so the Sun holds a few per cent of the angular momentum
at most, and no plausible interior rotation profile can change that. The digits
are model-dependent; the ordering is not.

---

## ★★★8 — Density, composition and compression

**(a)** $\dfrac{1}{\rho} = \dfrac{0.40}{1000} + \dfrac{0.60}{3500}
= 4.0000\times10^{-4} + 1.7143\times10^{-4} = 5.7143\times10^{-4}$, so
$\rho = 1750.0$ kg m⁻³. The demo's table brackets this between 2000.0 kg m⁻³ at
$f = 0.30$ and 1555.6 kg m⁻³ at $f = 0.50$.

**(b)** A 20 per cent compression gives a measured $\rho = 2100$ kg m⁻³.
Inverting the *uncompressed* relation:

$$f = \frac{1/2100 - 1/3500}{1/1000 - 1/3500}
= \frac{4.762\times10^{-4} - 2.857\times10^{-4}}{7.143\times10^{-4}}
= 0.267 .$$

The true ice fraction is 0.40 and the inferred one is 0.27: the body looks
substantially rockier than it is, because compression raises the density the way
extra rock would.

**(c)** A 10 per cent compression (measured 1925 kg m⁻³) gives
$f = (5.195\times10^{-4} - 2.857\times10^{-4})/7.143\times10^{-4} = 0.327$ —
still an 18 per cent under-estimate of the ice fraction.

**(d)** A mean density is a compressed density, and removing the compression
requires a pressure–density relation, which requires knowing the composition —
a circularity. The result is that one measured number constrains a *curve* in
the composition–structure plane rather than a point, and bodies with different
rock fractions and different internal temperatures can share a measured density.
A mission narrows it with independent information: the moment of inertia from a
rotational and gravitational figure (which measures how centrally condensed the
body is), the radius at high precision from repeated stellar occultations or
limb imaging, and composition from spectroscopy or from a lander. Radius alone
is not composition.

---

## ★★★9 — The ice line and the star

**(a)** From (4), $T_\mathrm{eq}^4 \propto L/a^2$, so at fixed temperature
$a \propto \sqrt L$. The ice line scales as the **square root** of the star's
luminosity.

**(b)** At $T_\mathrm{eq} = 170$ K: 0.709 au for $0.1L_\odot$, 2.243 au for
$L_\odot$ and 7.092 au for $10L_\odot$ — each a factor of $\sqrt{10}$ from the
last, as (a) requires.

**(c)** At fixed $a$, $T_\mathrm{eq} \propto L^{1/4}$. A star a hundred times
fainter than the Sun therefore has an equilibrium temperature at the same
distance lower by a factor $100^{1/4} = 3.2$, so its habitable zone sits about a
tenth of an au from the star rather than one au. For a low-mass star — which is
also much fainter, and whose habitable zone is therefore very close in — the
consequences are that the planet is likely to be tidally locked, that stellar
flares and the ultraviolet environment are harsher, and that the transit
probability $R_*/a$ is much larger, which is an observational advantage that
happens to offset the physical difficulty
([04-08-04 Exoplanets, Habitability and Observational Constraints](../04-exoplanets-habitability.md)).

**(d)** Because the condensation temperature depends on the *local gas pressure*
as well as on the temperature, and because the disk's temperature profile is set
by its own opacity and internal heating rather than by stellar irradiation alone:
a disk is optically thick, its surface is not at the same temperature as its
midplane, and the midplane — where condensation actually happens — is hotter than
a simple irradiated-body calculation predicts. The ice line is therefore a
consequence of disk structure, and the simple estimate in (4) gives the right
order of magnitude for the wrong reason.
