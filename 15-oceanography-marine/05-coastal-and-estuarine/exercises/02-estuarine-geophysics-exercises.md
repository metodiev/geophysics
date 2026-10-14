# Exercises — 15-05-02 Estuarine and Delta Geophysics

Attempt these before the
[solutions](./02-estuarine-geophysics-solutions.md). The lesson is
[02 Estuarine and Delta Geophysics](../02-estuarine-geophysics.md). All models
and data are **SYNTHETIC** teaching values; the model constants are those printed
by `code/estuarine_geophysics_demo.py`.

## ★ Foundational

**★1.** Using the lesson's model
$\rho=1028[1-2.0\times10^{-4}(T-10)+7.8\times10^{-4}(S-35)]$ and
$c=\sqrt{K/\rho}$ with $K=2.34\ \mathrm{GPa}$, compute $\rho$ and $c$ for
$T=15\ ^\circ\mathrm{C}$, $S=20\ \mathrm{g\,kg^{-1}}$.

**★2.** Compute the densimetric Froude number for $Q=150\ \mathrm{m^3\,s^{-1}}$,
$b=700$ m, $h=7$ m and $\Delta\rho=8\ \mathrm{kg\,m^{-3}}$, and classify the
estuary against the lesson's thresholds.

**★3.** For $K_x=150\ \mathrm{m^2\,s^{-1}}$ and $u_r=0.03\ \mathrm{m\,s^{-1}}$,
compute the e-folding intrusion length and the distance from the mouth to the
1 g/kg isohaline with an oceanic salinity of $30\ \mathrm{g\,kg^{-1}}$.

## ★★ Applied

**★★4.** A stratified estuary has a relative sound-speed gradient of
$a=3.0\times10^{-4}\ \mathrm{m^{-1}}$. Compute the depth error of a constant-speed
sounding at 20 m and at 60 m, and the percentage error at each. State why the
error grows faster than the depth.

**★★5.** A basin of area $50\ \mathrm{km^2}$ and mean depth 5 m receives
$3.0\times10^{5}\ \mathrm{m^3\,yr^{-1}}$ of bulk sediment with a relative
sea-level rise of $5\ \mathrm{mm\,yr^{-1}}$. Compute the accommodation, the
initial net rate, the equilibrium area, and the fill time with and without the
rise. State which estimate is an overestimate and why.

**★★6.** Repeat ★5 with an added subsidence of $2\ \mathrm{mm\,yr^{-1}}$. State
what has changed qualitatively about the basin's fate and compute the equilibrium
area.

## ★★★ Research-oriented

**★★★7.** An estuary 12 km long, 600 m wide and 8 m deep must be surveyed to map
the salinity intrusion and its stratigraphic record. Design the programme:
specify the sound-speed profiling strategy (what, where, how often), the
sub-bottom configuration, the resistivity or EM component, and for each the
parameter you measure and the quantity you model. State the two assumptions that
most affect the intrusion-length result and how you would test each.

**★★★8.** A delta is reported to be "drowning". Enumerate the terms of its
accommodation budget (eustatic rise, compaction, tectonic subsidence, sediment
supply), state for each how it would be measured, its likely size, and the
quantity that a tide gauge alone cannot separate. Then state the observation that
would distinguish a supply deficit from a subsidence excess, and the one that
neither can distinguish.
