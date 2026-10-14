# Solutions — 08-06-03 Magnetic Monitoring of Volcanoes and Faults

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [03 Magnetic Hazard Monitoring](../03-magnetic-hazard-monitoring.md).

---

## ★1 — Moment change at 800 m

$$\\Delta m=\\frac{2\\pi d^3\\Delta B}{\\mu_0}
=\\frac{2\\pi\\left(800\\right)^3\\left(2\\times10^{-9}\\right)}
{1.2566\\times10^{-6}}
=\\frac{6.2832\\times5.12\\times10^{8}\\times2\\times10^{-9}}
{1.2566\\times10^{-6}}.$$

Numerator: $6.2832\\times5.12\\times10^{8}=3.217\\times10^{9}$; times
$2\\times10^{-9}$ gives $6.434$; divided by $1.2566\\times10^{-6}$:

$$\\Delta m=5.12\\times10^{6}\\ \\mathrm{A\\,m^2}.$$

**Equivalent volume** at $M=1\\ \\mathrm{A\\,m^{-1}}$: $5.12\\times10^{6}\\ \\mathrm{m^3}$,
a cube of side $(5.12\\times10^{6})^{1/3}=172\\ \\mathrm{m}$. At
$M=100\\ \\mathrm{A\\,m^{-1}}$ the volume is $5.12\\times10^{4}\\ \\mathrm{m^3}$, a cube
of $37\\ \\mathrm{m}$.

Note the $d^3$: the same $2\\ \\mathrm{nT}$ at $1.6\\ \\mathrm{km}$ would require eight
times the moment change, $4.1\\times10^{7}\\ \\mathrm{A\\,m^2}$.

---

## ★2 — Ranking and coherence

By standard deviation: secular variation ($11\\ \\mathrm{nT}$) $>$ diurnal
($6\\ \\mathrm{nT}$) $>$ source transient ($2\\ \\mathrm{nT}$) $>$ noise
($0.5\\ \\mathrm{nT}$) $>$ drift ($0.3\\ \\mathrm{nT}$).

**Coherent between stations:** the secular variation (over hundreds of kilometres)
and the diurnal variation (to a few per cent over tens of kilometres). **Not
coherent:** the source transient, the noise and the drift (drift is coherent within
one instrument but not between instruments).

**Consequence:** the two largest terms are the two most coherent, which is what makes
differencing a reference station effective. The largest *incoherent* term is the
source itself; the second largest is the residual of the diurnal coherence, which is
the practical floor.

---

## ★3 — Noise of a difference and of an estimator

Two independent stations each with $\\sigma=0.5\\ \\mathrm{nT}$ give a difference with

$$\\sigma_{\\text{diff}}=\\sqrt{0.5^2+0.5^2}=0.707\\ \\mathrm{nT},$$

which matches the lesson's measured pre-transient scatter of $0.679\\ \\mathrm{nT}$
(the small difference is the realisation).

An estimator that compares the medians of two windows each containing $n$ samples
has a standard error of order $\\sigma_{\\text{diff}}\\sqrt{2/n_{\\text{eff}}}$,
which for $n\\sim2000$ is about $0.02\\ \\mathrm{nT}$ — thirty times smaller than the
single-sample scatter. The lesson's measured value is $0.039\\ \\mathrm{nT}$, larger
than the ideal because the diurnal residual is correlated between samples and
therefore reduces $n_{\\text{eff}}$. **This is exactly why the scatter must be
measured and not computed from the single-sample noise.**

---

## ★4 — Threshold, significance and false alarms

$$\\text{threshold}=3\\times0.04=0.12\\ \\mathrm{nT}.$$

A $0.3\\ \\mathrm{nT}$ change is $0.3/0.04=7.5\\sigma$: significant beyond any
reasonable doubt, *provided* the threshold and the scatter were computed on this
record (same window, same filtering).

**False-alarm rate to quote:** with one null realisation in 200 exceeding the
threshold, the empirical rate is $1/200=0.5\\%$, consistent with a Gaussian
$3\\sigma$ tail ($0.27\\%$) within the binomial uncertainty of 200 trials
($\\pm0.5\\%$). Publishing "$3\\sigma$, corresponding to about a $0.3\\%$ false-alarm
rate per independent window" is honest; publishing "significant" alone is not.

---

## ★5 — Off-axis reduction

At $\\rho=0$: $B\\propto 2d^2/d^5=2/d^3$. At $\\rho=2\\ \\mathrm{km}$,
$d=1\\ \\mathrm{km}$: $R=\\sqrt{\\rho^2+d^2}=\\sqrt{4+1}=2.236\\ \\mathrm{km}$,
$\\rho^2+d^2=5\\ \\mathrm{km^2}$, so

$$\\text{factor}=\\frac{2d^2-\\rho^2}{\\left(\\rho^2+d^2\\right)^{5/2}}\\cdot\\frac{d^3}{2}
=\\frac{2(1)-4}{5^{2.5}}\\cdot\\frac{1}{2}
=\\frac{-2}{55.90}\\cdot\\frac{1}{2}
=-0.01789.$$

**So the station sees $1.8\\%$ of the on-axis anomaly and with the opposite sign.**
At $\\rho=2\\ \\mathrm{km}$ with $d=1\\ \\mathrm{km}$ the station is well past the
sign reversal at $\\rho=d/\\sqrt2=0.71\\ \\mathrm{km}$, where the vertical component
is zero. A station placed at the wrong distance does not merely see a weaker
anomaly: it can see nothing at all, and this is the single commonest design error in
magnetic monitoring.

---

## ★6 — Required trend accuracy

The ambiguity from a trend error $e$ over a window of $T$ days is $eT/365$. Requiring
it below $\\Delta B/3$ with $\\Delta B=1\\ \\mathrm{nT}$ and $T=120$ days:

$$e<\\frac{365}{3}\\cdot\\frac{1}{120}=1.01\\ \\mathrm{nT\\,yr^{-1}}.$$

**Is that deliverable?** The lesson's SYNTHETIC instrument drift was
$0.5\\ \\mathrm{nT\\,yr^{-1}}$ over two years, so a *single* station with a good
calibration is marginally adequate at this level — but the requirement is not about
drift, it is about the *secular variation*, which is $10$–$100\\ \\mathrm{nT\\,yr^{-1}}$
and must be removed by a reference. A reference $10\\ \\mathrm{km}$ away shares the
core field to within the non-dipole difference, which over 120 days is typically a
few tenths of a nanotesla: adequate here, and not adequate for a $0.2\\ \\mathrm{nT}$
target (★7's design problem).

---

## ★7 — Monitoring network design for a $1\ \mathrm{km}$ hydrothermal system

**Station layout.** Array stations at $0.5$–$3\\ \\mathrm{km}$ from the expected
source centre, in at least four azimuths, at $0.3$–$0.5\\ \\mathrm{km}$ spacing near
the centre (so that the sign reversal at $\\rho=d/\\sqrt2\\approx0.71\\ \\mathrm{km}$
is bracketed — ★5 shows why a single badly placed station can be blind). Avoid
placing all stations inside the sign reversal.

**Reference.** Two references at $8$–$20\\ \\mathrm{km}$ in different directions,
outside the source's influence and inside the external field's coherence; the
difference between the two references measures the coherence floor directly, which
is the number that validates the design.

**Sampling.** $1\\ \\mathrm{Hz}$ or faster for piezomagnetic and lightning studies,
with $1$-minute means archived; continuous, with a stated clock and a GPS-disciplined
time base so that the diurnal variation can be removed by a common-mode model as
well as by differencing.

**Detection threshold and false-alarm rate.** Measure the estimator's scatter by
Monte Carlo on the actual residual series (not from the catalogue noise), set the
threshold at $3\\sigma$, and publish the empirical false-alarm rate per window
(typically $0.1$–$1\\%$). State the window length, because the rate is per window
and the number of windows per year multiplies it.

**Independent observables, and what each would establish.** Seismicity (brittle
failure and fluid movement), GNSS or tilt (deformation, hence pressure change),
gas flux and temperature (hydrothermal activity and heat), and electrical
resistivity or self-potential (fluid and alteration). A magnetic change accompanied
by a temperature change and a gas-flux change points to a thermal source; one
accompanied by microseismicity and strain points to a piezomagnetic or intrusive
source.

---

## ★8 — Three questions about a $0.5\ \mathrm{nT}$ change over six months

1. **What is the estimator's measured scatter on this record, and how was it
   computed?** A $0.5\ \mathrm{nT}$ change is $12\\sigma$ against the lesson's
   $0.04\ \\mathrm{nT}$ but only $1\\sigma$ against the single-sample noise
   ($0.5\\ \\mathrm{nT}$). The claim stands or falls on the former, and the
   Monte Carlo must be redone for the actual window, filtering and gap structure.
2. **What is the secular-variation trend error, and what ambiguity does it
   produce?** Using the design rule
   $e<122\\Delta B/T=122\\times0.5/180=0.34\\ \\mathrm{nT\\,yr^{-1}}$. If the
   reference pair's non-dipole difference over six months exceeds a third of
   $0.5\\ \\mathrm{nT}$, the change is indistinguishable from a trend error
   (Section 5 of the lesson), and the claim is not supported.
3. **Is the change coherent across the array with the geometry of a buried dipole,
   and does it have the sign pattern of a station inside or outside the sign
   reversal?** A real intrusive or thermal source produces a spatially structured
   signal with the $d^{-3}$ decay and the geometric sign change; a trend error is
   common-mode. Test: fit the array's amplitudes against the geometric factor of a
   common source depth, and check the residuals. A single-station claim cannot pass
   this test at all.

**Most direct test:** a second, independent observable that responds to the same
physical process — a temperature or gas-flux measurement at the fumarole field above
the inferred source. If the magnetic change is magmatic or hydrothermal, the thermal
and gas signals will be correlated in time with it; if no other observable moves, the
magnetic change is most likely an analytical artefact or a shallow, non-source
effect (soil moisture, frost, or a cultural source).
