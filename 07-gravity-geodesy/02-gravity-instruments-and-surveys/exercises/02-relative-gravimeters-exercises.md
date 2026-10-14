# Exercises — 07-02-02 Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex

Attempt these before reading the
[solutions](./02-relative-gravimeters-solutions.md). The lesson is
[02 Relative Gravimeters: Springs, LaCoste-Romberg, Scintrex](../02-relative-gravimeters.md).
All models are **SYNTHETIC**. Use $1\ \mathrm{\mu Gal} = 10^{-8}\
\mathrm{m\,s^{-2}}$, $g = 9.820250\ \mathrm{m\,s^{-2}}$ where a scale is needed, and
the lesson's measured relations where they apply.

## ★ Foundational

**★1.** A SYNTHETIC proof mass of $0.10\ \mathrm{kg}$ hangs on a spring of stiffness
$k = 3.948\ \mathrm{N\,m^{-1}}$. Compute the natural frequency, the static
extension, and the displacement corresponding to $1\ \mathrm{\mu Gal}$.

**★2.** For the spring of ★1, compute the displacement corresponding to the readout
noise of $5\ \mathrm{nm}$, and express it in microgal.

**★3.** A sensor response is $R(g) = c_{1}g + c_{2}g^{2}$ with
$c_{1} = 2\times10^{-3}$ counts/µGal and $c_{2} = 4\times10^{-12}$
counts/µGal². Compute the residual of a linear calibration at the ends of a span of
$\pm40\,000\ \mathrm{\mu Gal}$, using $\max\left|\text{residual}\right| =
\tfrac23 c_{2}L^{2}$ reduced to microgal through $c_{1}$.

## ★★ Applied

**★★4.** A sensor has $\eta = 0.995$. Compute the amplification factor $A$, the
effective stiffness relative to a $1\ \mathrm{Hz}$ spring, the natural period, and
the displacement per microgal for a $0.05\ \mathrm{kg}$ mass.

**★★5.** For the sensor of ★★4 with $l = 0.30\ \mathrm{m}$, compute
$\delta g_{\text{equiv}}$ for a geometric change of $10^{-10}\ \mathrm{m}$ and for
$10^{-7}\ \mathrm{m}$, and compute the length stability required to keep the effect
below $0.2\ \mathrm{\mu Gal}$.

**★★6.** Using the lesson's temperature sensitivity scaling, compute the temperature
stability required to hold the geometry of ★★5 to the value you found, assuming an
effective geometry coefficient of $5\times10^{-9}\ \mathrm{m\,K^{-1}}$. State
whether that is achievable with a simple enclosure and what it implies for a field
survey.

## ★★★ Research-oriented

**★★★7.** Design a relative survey that claims $5\ \mathrm{\mu Gal}$ (1σ) per
station over a $20\ \mathrm{km^{2}}$ area, using a sensor with $0.4\
\mathrm{\mu Gal}$ readout noise per sample and $25\ \mathrm{\mu Gal\,h^{-1}}$ drift.
Specify the loop structure, the base-occupation interval, the number of samples per
station, and show by arithmetic which term dominates. State what would falsify your
design.

**★★★8.** Two relative meters of different design families (a long-period spring
sensor and a nulled force-balance sensor) are used on the same survey. Design the
measurement and analysis that would show which instrument's error is limiting, and
how you would estimate the drift of each without assuming a functional form.

**★★★9.** A relative meter's drift is usually modelled as a linear ramp. Construct a
SYNTHETIC record in which that model fails (a step, a curvature, or a temperature
correlated with time) and specify the test that would detect the failure from
survey data alone, including the false-alarm rate you are willing to accept.
