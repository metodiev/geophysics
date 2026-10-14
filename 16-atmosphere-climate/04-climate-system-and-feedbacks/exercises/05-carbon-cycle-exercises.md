# Exercises — 16-04-05 The Carbon Cycle: Reservoirs, Fluxes and Perturbations

Attempt these before reading the
[solutions](./05-carbon-cycle-solutions.md). The lesson is
[05 The Carbon Cycle](../05-carbon-cycle.md). All models are **SYNTHETIC**
teaching values. Use $p_s = 1.013\times10^5$ Pa, $g = 9.81\ \mathrm{m\,s^{-2}}$,
$a = 6.371\times10^6$ m, $M_C/M_\text{air} = 0.4146$, and the demonstration's
impulse response

$$a(t) = 0.20 + 0.30\mathrm{e}^{-t/3.5} + 0.30\mathrm{e}^{-t/30}
+ 0.20\mathrm{e}^{-t/400}.$$

## ★ Foundational

**★1.** Compute the atmospheric mass per unit area $p_s/g$ and the total
atmospheric mass over $4\pi a^2$. Hence compute the GtC equivalent of 1 ppm of
CO₂ in this model, with units.

**★2.** Using $a(t)$, compute the fraction of a pulse remaining in the
atmosphere at 30 years and at 400 years. State which term dominates at each
time.

**★3.** For a 2000 GtC pulse, compute the atmospheric excess at 10 years and
state how much is in the sinks. Verify that the two add to the total.

## ★★ Applied

**★★4.** For a 3000 GtC pulse, compute the atmospheric excess and the sink
content at 10, 100 and 1000 years, and state the trend in the fraction airborne.

**★★5.** Using $\Delta C = (E-\gamma\Delta T)/(1+\beta)$ with
$|\lambda| = 4.0\ \mathrm{W\,m^{-2}K^{-1}}$, $F_{2\times} = 3.7\
\mathrm{W\,m^{-2}}$, $C_0 = 800$ GtC, $E = 2000$ GtC, $\beta = 1.5$ and
$\gamma = 150\ \mathrm{GtC\,K^{-1}}$, compute the equilibrium airborne fraction
and temperature change (iterate twice and state your convergence check).

**★★6.** Recompute ★★5 with $\gamma = 0$ and state the difference the
climate–carbon feedback makes to both the airborne fraction and the temperature.

## ★★★ Research-oriented

**★★★7.** The demonstration's increment per 1000 GtC falls from 0.723 K to
0.408 K across its range. Design a calculation that separates the contribution
of the logarithmic forcing from that of the $\gamma$ term to this curvature.
State the two runs, the diagnostic and how you would attribute the total
curvature to each source.

**★★★8.** A study reports that "about half of emitted CO₂ remains in the
atmosphere". Using the lesson, construct the complete list of what a reader must
know to interpret that claim numerically, and state whether the claim is true,
false or incomplete.
