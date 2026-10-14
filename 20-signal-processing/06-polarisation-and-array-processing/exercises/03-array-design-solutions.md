# Solutions — 20-06-03 Seismic Array Design and Resolution

> Read after attempting. Numbers computed. Lesson:
> [03 Array Design](../03-array-design.md).

---

## ★1 — The four numbers at 3 Hz

$$L = (N-1)d = 23 \times 2 = 46\ \mathrm{km},$$
$$\text{resolution} = \frac{1}{fL} = \frac{1}{3\times46}
= 0.00725\ \mathrm{s\,km^{-1}},$$
$$\text{aliasing-free} = \pm\frac{1}{2fd} = \pm\frac{1}{2\times3\times2}
= \pm0.0833\ \mathrm{s\,km^{-1}},$$
peak sidelobe $\approx -13\ \mathrm{dB}$ for uniform weighting (the lesson's
16-sensor measurement was $-13.15\ \mathrm{dB}$, the asymptotic value
$-13.26\ \mathrm{dB}$).

---

## ★2 — Hann tapering and what it costs

From the lesson's taper table: peak sidelobe $-31.5\ \mathrm{dB}$ (the asymptotic
Hann value, measured as an exact match), and the half-power width grows by a
factor of **1.75**.

New resolution: $1.75 \times 0.00725 = 0.01269\ \mathrm{s\,km^{-1}}$ — a 75%
loss.

To restore $0.00725$ at the same 2 km spacing, keep $f = 3\ \mathrm{Hz}$ and
increase the aperture by 1.75:

$$L' = 1.75 \times 46 = 80.5\ \mathrm{km}
\;\Longrightarrow\;
N' = \frac{80.5}{2} + 1 \approx 41\ \text{sensors}.$$

So buying $-31.5\ \mathrm{dB}$ sidelobes costs either 75% of the resolution or
about 70% more sensors.

---

## ★3 — Removing a grating lobe

**Change:** reduce the sensor spacing (make the array denser) so that
$1/(2fd) > |s|_{\max}$, or replace the regular layout with an irregular one.

**Costs:** (i) more sensors for the same aperture, hence more hardware and more
data — doubling the density roughly doubles the count; (ii) an irregular layout
raises the average sidelobe floor (the lesson measured $-10.86 \pm 1.68\ \mathrm{dB}$
for random layouts against $-13.15\ \mathrm{dB}$ uniform) and its sidelobes vary
between realisations.

---

## ★★4 — Distrusting a single-layout sidelobe number

1. **Single realisation.** Random layouts scatter; the lesson's 50-layout
   ensemble had a peak-sidelobe standard deviation of $\pm1.68\ \mathrm{dB}$.
   A $-30\ \mathrm{dB}$ report could easily be a $1.7\sigma$ lucky draw from a
   distribution whose mean is $-25.7\ \mathrm{dB}$.
2. **Asymptotic versus finite $N$.** The lesson measured Hamming at 16 sensors
   as $-39.37\ \mathrm{dB}$ against its asymptotic $-42.7\ \mathrm{dB}$: quoted
   window numbers are limits that small arrays do not reach. A $-30\ \mathrm{dB}$
   claim should be accompanied by the sensor count and the frequency.

**Measurement that settles it:** report the peak sidelobe over an ensemble of
layouts (or over the frequency band and slowness scan actually used), with its
mean and scatter, and state the exclusion window for the main lobe. A single
number without its ensemble and its scan range is not a measurement.

---

## ★★5 — Designing for resolution and aliasing

**Resolution.** $L = 1/(f\Delta s) = 1/(4 \times 0.004) = 62.5\ \mathrm{km}$.

**Aliasing.** $1/(2fd) > 0.05 \Rightarrow d < 1/(2 \times 4 \times 0.05) =
2.5\ \mathrm{km}$.

**Sensor count.** With $d = 2.5\ \mathrm{km}$,
$N = 62.5/2.5 + 1 = 26$ sensors.

**Design.** 26 sensors, 2.5 km spacing, 62.5 km aperture. Achieved: resolution
$0.004\ \mathrm{s\,km^{-1}}$, aliasing-free range
$\pm1/(2\times4\times2.5) = \pm0.05\ \mathrm{s\,km^{-1}}$. Both requirements are
met exactly, so add margin: $d = 2\ \mathrm{km}$, $N = 32$ sensors gives
$\pm0.0625\ \mathrm{s\,km^{-1}}$ aliasing-free and the same resolution.

---

## ★★6 — Choosing a taper for a nearby strong source

The strong coherent source sits $0.02\ \mathrm{s\,km^{-1}}$ from the target. The
main lobe of a uniform 30-km array at 5 Hz has its first null at
$1/(fL) = 0.0067$ and its first sidelobe at about $1.43/(fL) = 0.0095$ — so a
source at $0.02$ is at roughly the third sidelobe of a uniform array, where the
level is about $-17\ \mathrm{dB}$ to $-18\ \mathrm{dB}$. That leakage can
dominate a weak target.

From the table:

| taper | peak sidelobe | width ratio |
|---|---|---|
| uniform | $-13.15$ dB | 1.00 |
| triangular | $-27.05$ dB | 1.43 |
| Hann | $-31.50$ dB | 1.75 |

**Choice: triangular.** At $0.02$ from the target the sidelobe envelope of a
triangular taper is far below $-27\ \mathrm{dB}$ (the peak sidelobe is only the
*first* one; the envelope decays), which suppresses the source more than
adequately, while the 1.43 width penalty is the smallest of the three tapers.
Hann would suppress more but costs 1.75 — 22% more resolution loss than
triangular for suppression this study does not need. The decision rule is to buy
only as much suppression as the interfering amplitude requires.

---

## ★★★7 — A design that cannot be met

**Requirement A (resolution).** $L = 1/(f\Delta s) = 1/(3 \times 0.003) =
111.1\ \mathrm{km}$.

**Requirement B (aliasing).** $d < 1/(2 \times 3 \times 0.15) = 1.111\ \mathrm{km}$.

**Requirement D (sensor cap).** $N = L/d + 1 > 111.1/1.111 + 1 = 101$ sensors.

**Conclusion.** A and B together force at least 101 sensors against a cap of 40.
**The requirements cannot be met simultaneously.** Note also that the uniform
array of (A)+(B) would have $-13\ \mathrm{dB}$ sidelobes, violating the
$-25\ \mathrm{dB}$ requirement, so a taper is needed on top — which widens the
main lobe by $1.43$–$1.75$ and pushes $L$ to 159–194 km, and $N$ past 140.

**What to relax, and by how much.** The cheapest relaxation is the resolution
requirement, which is the one with the steepest cost. Holding $N = 40$ and
$d = 1.111\ \mathrm{km}$ gives $L = 43.3$ km, hence

$$\Delta s = \frac{1}{3 \times 43.3} = 0.0077\ \mathrm{s\,km^{-1}}$$

— a factor of 2.6 worse than requested. With a triangular taper ($1.43$) the
achievable resolution is $0.0110\ \mathrm{s\,km^{-1}}$, or a factor of 3.7 worse.
The alternative is to relax the aliasing requirement: keeping 40 sensors over
$L = 111$ km needs $d = 2.85\ \mathrm{km}$, giving an aliasing-free range of only
$\pm0.058\ \mathrm{s\,km^{-1}}$ against the requested $\pm0.15$ — so
slownesses beyond $\pm0.058$ cannot be trusted.

**The honest answer** states all three relaxations, their costs, and asks which
the science case can afford; it does not quietly drop one requirement and report
the design as meeting the specification.

---

## ★★★8 — Why more sensors at fixed aperture do not help

The array response depends on the spacings $x_j = jd$ only through the product
$f \Delta s\, d$ for a uniform array, and the main-lobe width in $\Delta s$ is

$$\Delta s_{\text{null}} = \frac{1}{N f d} = \frac{1}{fL},$$

which contains $N$ only through $L = Nd$. Fixing $L$ fixes the width, and
increasing $N$ at that $L$ requires *decreasing* $d$ so that the two effects
cancel.

**Numbers, going from 16 to 64 sensors at a 30-km aperture (5 Hz).**

| | 16 sensors | 64 sensors |
|---|---|---|
| spacing | $30/15 = 2.0\ \mathrm{km}$ | $30/63 = 0.476\ \mathrm{km}$ |
| resolution $1/(fL)$ | $0.00667\ \mathrm{s\,km^{-1}}$ | $0.00667\ \mathrm{s\,km^{-1}}$ |
| aliasing-free $\pm1/(2fd)$ | $\pm0.050\ \mathrm{s\,km^{-1}}$ | $\pm0.210\ \mathrm{s\,km^{-1}}$ |
| array gain (incoherent) | $12.0\ \mathrm{dB}$ | $18.1\ \mathrm{dB}$ |

So what improves is (i) the **aliasing-free range**, by a factor of 4.2, and
(ii) the **array gain**, by $10\log_{10}(64/16) = 6.0\ \mathrm{dB}$, hence the
ability to detect a weaker coherent signal against incoherent noise. The lesson's
measured half-power width was constant at $0.83/(fL)$ across all apertures, which
is the same statement measured rather than derived. Resolution is geometry; the
sensor count is redundancy.
