# Exercises — 07-02-04 Practical Correction Workflow and Processing Sequence

Attempt these before reading the
[solutions](./04-corrections-workflow-solutions.md). The lesson is
[04 Practical Correction Workflow and Processing Sequence](../04-corrections-workflow.md).
All models are **SYNTHETIC**. Use
$G = 6.67430\times10^{-11}\ \mathrm{m^{3}\,kg^{-1}\,s^{-2}}$,
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$,
$1\ \mathrm{\mu Gal} = 10^{-8}\ \mathrm{m\,s^{-2}}$, the free-air coefficient
$0.308555\ \mathrm{mGal\,m^{-1}}$ and the slab coefficient
$0.111969\ \mathrm{mGal\,m^{-1}}$ for $\rho = 2670\ \mathrm{kg\,m^{-3}}$.

## ★ Foundational

**★1.** List the eight steps of the processing sequence in order, and for each state
one input it requires and one diagnostic that would reveal an error in it.

**★2.** A station stands $400\ \mathrm{m}$ above the datum with a terrain term of
$0.5\ \mathrm{mGal}$ (convention: slab minus topography). Compute the free-air, slab
and terrain terms, and the net effect of the three on the anomaly.

**★3.** Compute the attraction of a rectangular prism of horizontal extent
$100\times100\ \mathrm{m}$ and thickness $20\ \mathrm{m}$ at a station $50\
\mathrm{m}$ away horizontally, in the plate approximation
($2\pi G\rho\times$ mean thickness), and compare with the exact prism value you would
expect to be smaller. State why the exact value is smaller.

## ★★ Applied

**★★4.** A SYNTHETIC survey has $900\ \mathrm{m}$ of relief and a target anomaly of
$1.0\ \mathrm{mGal}$. Using the lesson's measured sensitivity of the density error
(plate prediction $0.01132\ \mathrm{mGal\,m^{-1}}$ per
$270\ \mathrm{kg\,m^{-3}}$, realised slope $87\%$ of that), compute the anomaly error
at the maximum relief for a density error of (a) $100$ and (b) $400\
\mathrm{kg\,m^{-3}}$, and state whether the target is achievable without a density
constraint.

**★★5.** A terrain model is built with 100 m cells and the same topography with
200 m cells gives a difference of $200\ \mathrm{\mu Gal}$ at the worst station. If
the survey target is $100\ \mathrm{\mu Gal}$, what cell size would you need?
Justify the scaling you assume, and state the test that would confirm it.

**★★6.** A pipeline's residual against a known SYNTHETIC truth is
$3.5\ \mathrm{\mu Gal}$ rms, with reading noise $2.0\ \mathrm{\mu Gal}$, drift-model
residual $2.5\ \mathrm{\mu Gal}$ and terrain discretisation $1.5\ \mathrm{\mu Gal}$.
Compute the expected floor and decide whether the pipeline has an unexplained error.

## ★★★ Research-oriented

**★★★7.** Design the complete processing workflow for a SYNTHETIC $500$-station
survey targeting $50\ \mathrm{\mu Gal}$, specifying every input, its uncertainty, the
diagnostics at each stage and the acceptance thresholds. State which single input you
would improve first and justify it with the budget.

**★★★8.** Construct a *validation* plan for a terrain-correction code: list three
independent checks with their expected accuracy, and specify what you would conclude
if the code passed two and failed the third.

**★★★9.** A colleague delivers a Bouguer anomaly map and states only "the standard
corrections were applied". List what you must ask to be able to reproduce or even
interpret the map, and rank the questions by how much the answer could change the
map.
