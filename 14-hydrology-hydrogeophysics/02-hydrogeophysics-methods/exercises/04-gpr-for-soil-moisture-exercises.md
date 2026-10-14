# Exercises — 14-02-04 GPR for Soil Moisture and Water Table

Attempt these before reading the
[solutions](./04-gpr-for-soil-moisture-solutions.md). The lesson is
[04 GPR for Soil Moisture and Water Table](../04-gpr-for-soil-moisture.md). All
soils are **SYNTHETIC**.

Use
$\sqrt{\varepsilon_{\text{eff}}} = (1-\phi)\sqrt{4.5} + \theta\sqrt{81}
+ (\phi-\theta)$, $v = c/\sqrt{\varepsilon}$ with $c = 0.299792458\
\mathrm{m\,ns^{-1}}$, $R = (\sqrt{\varepsilon_1} - \sqrt{\varepsilon_2})/
(\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2})$, $t^2 = t_0^2 + x^2/v^2$, and
$\alpha = (\sigma/2)\sqrt{\mu_0/\varepsilon}$ with $1\ \mathrm{Np} = 8.686\
\mathrm{dB}$ in the low-loss regime.

## ★ Foundational

**★1.** A soil has $\phi = 0.42$ and $\theta = 0.18$. Compute
$\varepsilon_{\text{eff}}$, the radar velocity, and the two-way travel time over a
1.2 m layer.

**★2.** For the same soil, compute the reflection coefficient at a boundary where
the water content falls to $\theta = 0.08$. State the polarity in words.

**★3.** State which of the following a single-offset GPR profile determines and
which it does not: (a) water content, (b) layer thickness, (c) pore-water salinity,
(d) clay-bound water.

## ★★ Applied

**★★4.** A CMP gather gives, at separations 0.5, 1.0, 1.5 and 2.0 m, two-way
times of 41.2, 43.0, 46.4 and 51.4 ns. Fit $t^2 = t_0^2 + x^2/v^2$, report $v$ and
$t_0$, and compute the reflector depth for both $v$ and $1.3v$. State the
percentage error in depth.

**★★5.** A soil has $\sigma = 0.04\ \mathrm{S\,m^{-1}}$ and
$\theta = 0.25$ at $\phi = 0.40$. Compute the loss tangent at 100 and 250 MHz,
decide which regime applies, and compute the attenuation and the 60 dB depth in
each case. State whether lowering the frequency from 250 to 100 MHz improves
penetration here.

**★★6.** A gravimetric calibration gives $\theta = 0.22$ where CRIM inverts to
0.17 at the same location, and $\theta = 0.09$ where CRIM gives 0.05. State the
form of the bias (constant or proportional), compute both for a third point where
CRIM returns 0.13, and explain why the relative error is worse at low water
content.

## ★★★ Research-oriented

**★★★7.** Design a GPR survey to map soil moisture to $\pm 0.02$ over a 2 m
profile in a soil whose clay fraction raises $\sigma$ to
$0.03\ \mathrm{S\,m^{-1}}$. Specify the antenna frequency, the survey geometry
(CMP or fixed-offset, and why), the calibration programme, and the error budget.
Then state one site condition that would make the survey impossible and the
alternative method you would choose instead, with the arithmetic that supports the
choice.

**★★★8.** A time-lapse GPR survey over a 1.5 m profile shows the two-way travel
time to a shallow reflector increasing by 8% between spring and autumn, with no
change in the reflection amplitude.
(a) Compute the water-content change implied, using a two-layer model.
(b) Show that a temperature change cannot explain it, while a salinity change of
the pore water can explain the amplitude behaviour but not the travel time.
(c) State the additional measurement that fixes the interpretation, and give the
arithmetic that would confirm it.
