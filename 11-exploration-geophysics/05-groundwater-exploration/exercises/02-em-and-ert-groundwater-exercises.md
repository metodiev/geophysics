# Exercises — 11-05-02 EM and ERT for Groundwater Mapping

Attempt these before reading the
[solutions](./02-em-and-ert-groundwater-solutions.md). The lesson is
[02 EM and ERT for Groundwater Mapping](../02-em-and-ert-groundwater.md).
All models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the geometric factor $K$ of (a) a Wenner array with spacing
$a = 5\ \mathrm{m}$ and (b) a Schlumberger array with $AB/2 = 30\ \mathrm{m}$ and
$MN = 5\ \mathrm{m}$. For the Schlumberger array, compute $\rho_a$ if the
measured resistance is $R = 0.42\ \Omega$.

**★2.** Compute the skin depth for $\rho = 50\ \Omega\,\mathrm{m}$ at
$f = 1$, $10$ and $100\ \mathrm{Hz}$, and state the units of every factor.

**★3.** For a two-layer earth with $\rho_1 = 50$, $\rho_2 = 10\
\Omega\,\mathrm{m}$ and $h_1 = 8\ \mathrm{m}$, evaluate the Schlumberger series
at $L = 10\ \mathrm{m}$ using the first three terms ($n = 1,2,3$), then with
$n = 6$, and state how much the truncation moves the answer.

## ★★ Applied

**★★4.** A $5\ \mathrm{m}$-thick conductive layer with conductivity
$0.2\ \mathrm{S\,m^{-1}}$ sits in a resistive background. Compute its conductance
$S$. What thickness of a $0.5\ \mathrm{S\,m^{-1}}$ layer has the same
conductance, and why can a sounding not distinguish the two?

**★★5.** In the lesson's admitted-set table, the wide spacing range gives
$h_1 = 7.8$-$8.0\ \mathrm{m}$ and the short range gives $7.4$-$9.5\
\mathrm{m}$ for the same model and noise. Explain, using the form of the
two-layer series, why the long spacings are the ones that fix the depth.

**★★6.** A survey reports $\rho_2 = 12\ \Omega\,\mathrm{m}$ and
$h_1 = 7\ \mathrm{m}$ from a two-layer fit. Using the least-determined direction
$(+0.449, -0.894)$ in log units, compute the alternative model that fits the data
equally well if $\rho_2$ is increased by $10\%$, and state its $h_1$.

## ★★★ Research-oriented

**★★★7.** You must site a borehole that will screen an aquifer at about
$60\ \mathrm{m}$ depth beneath $20\ \mathrm{m}$ of resistive dry sand, using a
Schlumberger sounding. Specify the largest $AB/2$, the $MN$ values, the noise
target, and the number of soundings, and justify each with a number from the
lesson's sensitivity analysis. State what you would report if the inversion is
ambiguous.

**★★★8.** An ERT section and an FDEM survey over the same line give apparent
resistivities that differ by a factor of two. List three physical causes and
three processing causes, and describe a measurement that would separate the
leading candidate from the others.
