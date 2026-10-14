# Exercises — 13-07-01 Erosion, Uplift and Thermochronology

Attempt these before reading the
[solutions](./01-erosion-and-uplift-solutions.md). The lesson is
[01 Erosion, Uplift and Thermochronology](../01-erosion-and-uplift.md) and its
numbers come from
[`code/erosion_and_uplift_demo.py`](../code/erosion_and_uplift_demo.py). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the Péclet number $Pe = EL/\kappa$ for $E = 0.3$ mm/yr,
$L = 35$ km and $\kappa = 1.0\times10^{-6}$ m²/s (convert $E$ to m/yr first).

**★2.** Evaluate $T(z) = T_s + (T_m-T_s)(1-e^{-Pe z/L})/(1-e^{-Pe})$ at
$z = L/2$ for $Pe = 1$ with $T_s = 10$ °C and $T_m = 1350$ °C.

**★3.** Define rock uplift, surface uplift and exhumation in one sentence each,
and state which one a thermochronometer measures.

## ★★ Applied

**★★4.** A steady exhumation state has a closure depth of 4.0 km and an apparent
age of 8.0 Ma. Compute the exhumation rate in mm/yr.

**★★5.** For the same state, a second sample 1.5 km higher in elevation gives an
age of 2.0 Ma. Compute the age–elevation slope and the rate, and state why the
answer is identical to ★4.

**★★6.** The lesson measures the closure depth as 4.35 km at $E = 0.5$ mm/yr and
2.21 km at $E = 2.0$ mm/yr. Compute the ratio of the apparent ages these imply
for a sample at the closure isotherm and compare with the ratio of the rates.

**★★7.** A two-stage history exhumes at 0.2 mm/yr for 15 Myr and then at
1.0 mm/yr. Compute the depth of the break in the age–elevation plot and the two
slopes.

## ★★★ Research-oriented

**★★★8.** For $\lambda = 30$ km, $A = 1.5$ km, $\Gamma = 6$ °C/km and the
lesson's closure depth of 4.35 km with a local gradient of 42.22 °C/km, compute
the closure-depth shift and the age shift, and state whether this bias is
detectable against a typical analytical uncertainty of 5%.

**★★★9.** Design a sampling strategy that would measure both the present
exhumation rate and the rate 10 Myr ago, stating the elevations, the number of
samples and the quantity plotted.

**★★★10.** A study reports "3 km of surface uplift since 5 Ma" from an
age–elevation slope. Write the three questions you would ask, and state the
additional observation needed to convert an exhumation rate into surface uplift.
