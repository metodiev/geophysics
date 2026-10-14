# Solutions — 08-06-02 Environmental Magnetism and Pollution Mapping

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [02 Environmental Magnetism](../02-environmental-magnetics.md).

---

## ★1 — Anomaly of a sphere

**Moment.** $V=\frac{4}{3}\pi a^3=\frac{4}{3}\pi(4)^3=268.08\ \mathrm{m^3}$;
$m=\chi H V=0.02\times48\times268.08=257.36\ \mathrm{A\,m^2}$.

**Anomaly.** $B=\mu_0 m/(2\pi d^3)$:

$$B=\frac{4\pi\times10^{-7}\times257.36}{2\pi\times1728}
=\frac{3.2335\times10^{-4}}{1.0857\times10^4}=2.978\times10^{-8}\ \mathrm{T}
=29.78\ \mathrm{nT}.$$

**Cross-check with the closed form.** $(a/d)^3=(4/12)^3=0.33333^3=0.037037$, so

$$B=\frac{2}{3}(0.02)(48)(0.037037)(1.2566\times10^{-6})
=2.978\times10^{-8}\ \mathrm{T}=29.78\ \mathrm{nT},$$

the same value by the two routes. ✔

---

## ★2 — Scalings

- (a) radius tripled: anomaly $\times27$.
- (b) depth halved: anomaly $\times8$.
- (c) susceptibility divided by five: anomaly $\div5$ (to $0.2\times$).

**The asymmetry is the point.** A body of the same mass but twice as far away is
eight times harder to see; there is nothing the surveyor can do about (b), whereas
(c) is the ground's own property. This is why magnetic surveys are described as
"detectors with poor quantifiers".

---

## ★3 — Signal-to-noise and one depth-multiple

Signal-to-noise $=10$. Moving the body one depth-multiple deeper means
$d\to2d$, so the anomaly falls by $2^3=8$ to $1.25\ \mathrm{nT}$, i.e. a
signal-to-noise of $1.25$.

**Answer:** still formally above the $1\ \mathrm{nT}$ noise floor, but no longer
*detectable* in any useful sense — a $1.25\sigma$ peak is indistinguishable from a
noise excursion, and would not survive a threshold at $3\sigma$. The honest
statement is that the body is at the edge of detection at its current depth and
would be lost at the next depth multiple.

---

## ★4 — Maximum detection depth

Set the anomaly equal to the noise floor and solve for $d$:

$$\frac{2}{3}\chi H\mu_0\left(\frac{a}{d}\right)^3=B_N
\quad\Longrightarrow\quad
\left(\frac{a}{d}\right)^3=\frac{3B_N}{2\chi H\mu_0}
\quad\Longrightarrow\quad
d_{\max}=a\left(\frac{2\chi H\mu_0}{3B_N}\right)^{1/3}.$$

Evaluating with $a=3\ \mathrm{m}$, $\chi=0.01$, $H=48\ \mathrm{A\,m^{-1}}$,
$B_N=1\times10^{-9}\ \mathrm{T}$:

$$\frac{2\chi H\mu_0}{3B_N}
=\frac{2\times0.01\times48\times1.2566\times10^{-6}}{3\times10^{-9}}
=\frac{1.2064\times10^{-6}}{3\times10^{-9}}=402.1,$$

$$d_{\max}=3\times(402.1)^{1/3}=3\times7.381=22.14\ \mathrm{m}.$$

**The cube root is the design statement:** a tenfold larger susceptibility gives
$d_{\max}\times10^{1/3}=2.15$; a tenfold better instrument gives the same. A
hundredfold improvement in either gives $4.64$.

---

## ★5 — Settling the depth

With $a/d=0.37$, the required size scales with depth: $a=0.37d$. An auger to
$5\ \mathrm{m}$ could reach a body of radius $0.37\times5=1.85\ \mathrm{m}$ if the
body were actually at $5\ \mathrm{m}$; a trial pit to $10\ \mathrm{m}$ reaches
$3.7\ \mathrm{m}$. **Which settles it depends on the body's actual size**, which is
what is unknown — the trap of the ambiguity in one line.

What to do if neither reaches the body:

1. **Increase the resolution of the map**: a shallower body has a sharper, more
   short-wavelength anomaly with stronger negative flanks. This is a *relative*
   discriminator, not an absolute measurement, and it requires the anomaly to be
   sampled at a spacing much smaller than the depth (the map in the lesson used
   $2\ \mathrm{m}$ for bodies at $5$–$15\ \mathrm{m}$).
2. **Use a second method with a different depth sensitivity**: resistivity or
   electromagnetic profiling responds to the conductivity of the same body; a
   gravity or seismic measurement responds to its density and geometry.
3. **Model with a shape constraint**: if the body is known to be a buried object
   with a fixed geometry (a drum, a pipe), the shape fixes the moment-to-size
   relation and the depth follows. Euler deconvolution does the same thing by
   assuming a structural index, and the assumption must be reported.
4. **Report the ambiguity**: "a body of $a/d=0.37$ at unknown depth; if it is a
   $1\ \mathrm{m}$ object it is at $2.7\ \mathrm{m}$, if it is $3\ \mathrm{m}$ it is
   at $8.1\ \mathrm{m}$".

---

## ★6 — Concentration or grain size?

$\chi$ fell by $1.25\times$ while SIRM per unit mass is unchanged. $\chi$ and SIRM
are both concentration-like, but they weight magnetic grain size differently:
$\chi$ is dominated by the larger (multi-domain) grains, SIRM by the smaller
(single-domain) ones. An unchanged SIRM with a lower $\chi$ therefore indicates a
**shift toward finer magnetic grains** (or the loss of a coarse-grained fraction),
not a lower concentration.

**What to measure next:** SIRM/$\chi$ (which rises as the grain size falls), plus
hysteresis parameters (the ratio of saturation remanence to saturation
magnetisation, and the coercivity of remanence) to place the sample on a
Day-plot-type diagram, and if possible a low-temperature or frequency-dependent
susceptibility measurement to detect the superparamagnetic fraction — which is
magnetic in SIRM terms and nearly invisible in $\chi$.

---

## ★7 — Designing a susceptibility-based pollution map

**Normalisation.** Report mass-specific susceptibility $\chi$ on a dry-mass basis
(and, for cross-lithology comparison, also normalise to iron or aluminium content).
Pair it with SIRM on the same samples so that a concentration change and a grain-size
change can be separated; report the pair, not $\chi$ alone.

**Sampling design.** A regular grid at a spacing shorter than the expected anomaly
width (topsoil, $0$–$10\ \mathrm{cm}$, with a fixed protocol for vegetation, moisture
and compaction), plus a background profile upwind and away from the site to
establish the natural variability — the background is required to define an anomaly
at all.

**Chemical analyses.** Enough to fit the proxy: at least $20$–$30$ samples spanning
the full range of $\chi$ at each site, analysed for the pollutant of interest and
for a conservative lithological indicator (Fe, Al, or Zr), with the sampling design
stratified so that the calibration is not driven by a single high-value point.

**Acceptance statistic.** Fit $c=a\chi+b$ (or a log-log form) and require
(i) a stated $r^2$, (ii) a slope whose confidence interval excludes zero,
(iii) residuals that show no spatial trend (a Moran's I or variogram check) — a
proxy whose residuals are spatially structured is mapping geology, not contamination.

**Reporting a failure.** Cells where the proxy fails (the ratio SIRM/$\chi$ outside
the calibration range, or the lithology indicator outside its range) are marked as
"proxy not applicable" with the reason, rather than interpolated from their
neighbours. A map with a stated fraction of undefined cells is more useful than a
complete map with an unknown error.

---

## ★8 — A non-induced shape

Three explanations, in order of likelihood, with the distinguishing measurement:

1. **Remanent magnetisation dominates** ($Q=M_r/(\chi H)$ of order one or more).
   The direction is fixed at the time of cooling or deposition, not parallel to
   today's field, so the anomaly's asymmetry is real. *Distinguishing measurement:*
   laboratory determination of the Koenigsberger ratio and of the direction of
   natural remanent magnetisation on oriented samples; in the field, a comparison
   between the anomaly and the induced model.
2. **A multi-body or shaped source.** Two nearby bodies, or a dipping sheet, produce
   a composite anomaly that a single dipole does not reproduce. *Distinguishing
   measurement:* forward modelling of candidate shapes and a comparison of the
   modelled gradients with the measured profile at several orientations; a
   gradiometer or a dense grid to resolve the individual lobes.
3. **A non-dipole ambient field / measurement geometry artefact.** A total-field
   sensor records the projection of the anomaly onto the field direction, so a
   strongly non-vertical ambient field rotates the apparent pattern; an incorrect
   sensor orientation or a levelling error produces a similar distortion.
   *Distinguishing measurement:* repeat the profile in the opposite direction (a
   geometry artefact reverses or stays the same, depending on its origin), and
   compare the anomaly with the expected projection direction computed from the
   ambient field and the body's inferred orientation.
