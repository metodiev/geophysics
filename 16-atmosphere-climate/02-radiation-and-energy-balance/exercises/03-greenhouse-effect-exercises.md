# Exercises — 16-02-03 The Greenhouse Effect: Physics, Not Rhetoric

Attempt these before reading the
[solutions](./03-greenhouse-effect-solutions.md). The lesson is
[03 The Greenhouse Effect](../03-greenhouse-effect.md). Use
$\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$ and
$S = 1361\ \mathrm{W\,m^{-2}}$ unless stated otherwise. All models are
**SYNTHETIC**: albedos, surface temperatures and line parameters are chosen
teaching values, and no measured spectrum or published forcing is used.

## ★ Foundational

**★1.** For $a = 0.30$ compute $F = S(1-a)/4$, the effective radiating temperature
$T_e$, and $T_e$ in degrees Celsius. State in one sentence why $T_e$ is a model
output and not an observation.

**★2.** A surface is at $290\ \mathrm{K}$. Compute $\sigma T_s^4$, the downwelling
infrared flux it needs if it absorbs $238.175\ \mathrm{W\,m^{-2}}$ of sunlight, and
the ratio $\sigma T_s^4/F$.

**★3.** Compute the Planck response $4\sigma T^3$ at $250$, $255$, $280$ and
$300\ \mathrm{K}$. State in one sentence what quantity each number converts into
what.

**★4.** A change in composition produces an instantaneous forcing of
$+3.0\ \mathrm{W\,m^{-2}}$. Compute the no-feedback temperature change using the
Planck response at $T_e = 254.578\ \mathrm{K}$, and state what has been left out.

## ★★ Applied

**★★5.** Derive $\sigma T_s^4 = F + D$ for a black surface absorbing all incident
sunlight plus a downwelling infrared flux $D$. Then fit the one-layer emissivity
that reproduces $T_s = 290\ \mathrm{K}$ for $F = 238.175\ \mathrm{W\,m^{-2}}$ and
state, in two sentences, what the fit establishes and what it does not.

**★★6.** Derive $\mathrm{d}T_s/\mathrm{d}\varepsilon$ from the exact one-layer
result and evaluate it at $\varepsilon = 0.4$ and $\varepsilon = 0.9$. Compute the
*fractional* sensitivity at both and state whether the one-layer model saturates.
Then explain where the real saturation comes from and why a broadband emissivity
cannot represent it.

**★★7.** A Lorentz line has model half-width $\alpha = 3.0\times10^{2}\ \mathrm{m^{-1}}$
and a line-centre absorption coefficient of $1.2$ per unit reference column.
Explain, without computing, in which regime the absorption deficit scales linearly
with column amount and in which it scales as the square root, and state the
column amount in units of the reference column at which you expect the transition
(defined as the point where the line-centre optical depth is of order unity).
Justify the criterion.

**★★8.** A planet's atmosphere is modelled as a single layer whose effective
broadband emissivity is $0.60$ and whose surface is at $T_s$. The absorbed solar
flux is $200\ \mathrm{W\,m^{-2}}$. Compute (a) $T_e$, (b) $T_s$ from the exact
one-layer result, (c) the layer temperature $T_a$, and (d) the downwelling infrared
flux at the surface. Verify that your answers satisfy both balance equations.

## ★★★ Research-oriented

**★★★9.** Design a numerical experiment that measures the absorption deficit of a
synthetic Lorentz line as a function of column amount and of line half-width, and
extracts the local logarithmic slope over two decades in each variable. State the
metric, the expected scaling in the two limits, and — the important part — what
you expect the *product* of the two scalings to be. Then state what a failure of
that expectation would imply about the numerical integration or about the
definition of the deficit.

**★★★10.** The lesson's measured/modelled/inferred table classifies eight
statements. Add four more statements of your own choosing about the greenhouse
effect, classify each, and for each one name the specific measurement or
computation that would move it from *inferred* to *modelled* or from *modelled* to
*measured*. Then state one statement that cannot in principle be moved out of the
*inferred* column, and say why.

**★★★11.** "The greenhouse effect saturates, so adding more greenhouse gas cannot
warm the planet further." Identify every distinct error in that sentence, classify
each as a confusion of *physics*, *algebra* or *scaling of the forcing*, and write
the strongest version of the true statement that the sentence was reaching for. Be
explicit about which parts of your answer are derivable from this lesson and which
require results from outside it.

**★★★12.** A one-layer model can be fitted to a surface temperature with one free
parameter. Construct a falsification test for the *mechanism* (as opposed to the
fit) using only quantities that a single satellite instrument could measure, and
state the prediction the mechanism makes that a bare energy-balance fit does not.
Explain why the test must be spectral rather than broadband.
