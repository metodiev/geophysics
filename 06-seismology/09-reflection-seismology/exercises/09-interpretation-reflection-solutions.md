# Solutions — 06-09-09 Structural and Stratigraphic Interpretation

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [09 Interpretation](../09-interpretation-reflection.md).

---

## ★1 — Throw in metres versus resolution

A two-way time throw $\Delta t$ corresponds to a vertical displacement

$$\Delta z = \frac{v\,\Delta t}{2} = \frac{3200\times0.015}{2}
= 24.0\ \mathrm{m}.$$

The vertical resolution scale is

$$\lambda = \frac{v}{f_0} = \frac{3200}{30} = 106.7\ \mathrm{m}, \qquad
\frac{\lambda}{4} = 26.7\ \mathrm{m}.$$

So the throw ($24.0\ \mathrm{m}$) is just **below** $\lambda/4$: the marker is
offset by less than the resolution scale, which means the throw is detectable
(a lateral discontinuity exists) but its magnitude is at the resolution limit and
must be quoted with that scale.

---

## ★2 — Two-way time of the marker

$$t = \frac{2h}{v} = \frac{2\times500}{3000} = 0.333333\ \mathrm{s}
= 333.3\ \mathrm{ms},$$

which is the printed value. Unit check: $\mathrm{m}/(\mathrm{m\,s^{-1}}) =
\mathrm{s}$.

---

## ★3 — Lateral uncertainty from the coherency window

A 5-trace window centred on a trace spans $2$ traces on each side, i.e.

$$\pm 2\,dx = \pm 2\times25 = \pm 50\ \mathrm{m}.$$

The demonstration reports the minimum-coherency trace exactly at
$x = 1500\ \mathrm{m}$ (the true fault), and its ±50 m window is the finest
lateral localisation the attribute can claim. Compared with the *vertical*
resolution $\lambda/4 = 25.0\ \mathrm{m}$, the lateral localisation is **$2\times$
coarser** — a useful reminder that an attribute's lateral resolution is set by
its aperture, while the vertical scale is set by the wavelength.

---

## ★4 — Why half the window width

A similarity/coherency value at trace $i$ is a *summary over the window*, so it
reports "the traces in this window are dissimilar" rather than "the
discontinuity is at this trace". If the fault is at the edge of the window the
statistic is still reduced, and as the window slides across the fault the
minimum of the attribute is reached when the fault is *centred* — but the
attribute's value changes only gradually over the window, so the position of the
minimum is defined only to about the half-width.

**Reduction without changing $dx$:** use a *smaller* window (fewer traces) at the
cost of a noisier attribute, or replace the window statistic with a
**discontinuity attribute** that fits a local planar model and reports the
lateral gradient's location (a "discontinuity/fault-enhancement" attribute), whose
resolution is not set by the aperture but by the local fit. A third option is to
combine several windows of different sizes and report the *intersection* of their
minima, which typically reduces the uncertainty by a factor of about
$\sqrt{2}$ for two independent window sizes.

---

## ★5 — Depth and its uncertainty

$$\text{depth} = \frac{v\,t_0}{2} = \frac{3000\times2.4}{2} = 3600\ \mathrm{m}.$$

**(i) Velocity uncertainty of $4\%$:** depth is *linear* in $v$, so

$$\delta z_v = 0.04\times3600 = \pm144\ \mathrm{m}.$$

**(ii) Time-picking uncertainty of $\pm2\ \mathrm{ms}$:** depth is *linear* in
$t_0$, so

$$\delta z_t = \frac{v\,\delta t}{2} = \frac{3000\times0.002}{2}
= \pm3.0\ \mathrm{m}.$$

**The velocity term dominates by a factor of $48$.** The defensible statement is
that a time-picked depth is only as good as the velocity used to convert it, and
that chasing timing precision (finer sampling, better picking) is wasted effort
until the velocity uncertainty is reduced.

---

## ★6 — The full uncertainty statement

Adding the independent contributions in quadrature (the standard convention for
independent errors):

$$\delta z = \sqrt{\delta z_v^{2} + \delta z_t^{2} + \delta z_{\text{quant}}^{2}} .$$

**Quantisation** with a $4\ \mathrm{ms}$ two-way sample interval: the picked time
is uncertain by half a sample, $\pm2\ \mathrm{ms}$, which is *the same* as the
picking term of ★5 — so the sampling, not the picker, sets that floor at

$$\delta z_{\text{quant}} = \frac{3000\times0.004/2}{2} = \pm3.0\ \mathrm{m}.$$

Combining:

$$\delta z = \sqrt{144^{2} + 3.0^{2} + 3.0^{2}} = \sqrt{20\,736 + 9 + 9}
= \pm144.06\ \mathrm{m}.$$

**Statement:** "reservoir top at $3600 \pm 144\ \mathrm{m}$ (1σ), where the
uncertainty is dominated by the $\pm4\%$ velocity conversion; time-picking and
sampling contribute $\pm4.2\ \mathrm{m}$ and are negligible."

**What would reduce it:** an independent velocity measurement tied to the
reservoir (a well with a check-shot or a sonic log, or a tomographic velocity
update with migration-flattening QC). Reducing the time uncertainty below 2 ms
would change nothing.

---

## ★7 — QC for a phase error (specification)

**Observable.** The polarity and the phase rotation of the wavelet as measured at
**tie points**: (a) wells with a synthetic seismogram, and (b) a
statistically-derived wavelet from the data itself (e.g. the autocorrelation of
a clean, isolated reflector, or a deterministic source signature for
controlled-source data).

**Diagnostic.** (i) The correlation coefficient between the synthetic trace from
the well reflectivity and the seismic trace at the well: the demonstration
measures $1.0000$ for a correct wavelet and time–depth relation, so a marked drop
is the signal. (ii) The *sign* of the strongest reflection at a known
impedance contrast (a hard water bottom, or a known unconformity): a phase error
flips it. (iii) For a rotated (not flipped) wavelet, the ratio of the peak to the
sidelobes of the extracted wavelet, and the asymmetry of its zero crossings.

**Threshold.** Fail the interpretation if (a) the well-tie correlation falls
below the level expected for the local signal-to-noise ratio (for clean data,
$<0.7$ would be suspicious against the demonstration's $1.0000$), or (b) the
polarity at any of two independent tie points is inconsistent with the other, or
(c) the extracted wavelet requires a rotation of more than about $30^\circ$ to
match the well synthetics.

**Distinguishing a phase error from genuine structural complexity.** A phase
error is **global**: it flips or rotates *every* event in the section, so the
mismatch cannot be fixed by adjusting structure, and the tie residual is
systematic in depth. Genuine complexity (tuning, interference, steep dips) is
**local**: the mismatch appears on some events and not others, and it correlates
with the geology (a channel edge, a bed below tuning thickness). The decisive
test is to apply the candidate phase correction and re-tie: a correct phase
correction improves the tie at **every** tie point simultaneously; a structural
re-interpretation cannot.

---

## ★8 — Making the throw uncertainty visible (protocol)

**Picking protocol.**

1. Pick the marker's two-way time on **both** sides of the fault, on every
   interpreted line, using the same picking criterion (e.g. the extremum of the
   envelope, or the zero crossing of the same phase) — the criterion must be
   stated, because a peak and a zero-crossing pick differ by a phase-dependent
   amount.
2. Quote the throw as a **depth** throw and as a **time** throw, with the
   conversion velocity and its uncertainty.
3. Report, for each fault, the throw **and** the picking uncertainty computed
   from (i) the sample interval, (ii) the amplitude-to-noise ratio at the
   marker, and (iii) the difference between two independent pickers (or two
   picking criteria) on a subset of lines.
4. Publish the throw distribution with the **resolution scale** ($\lambda/4$)
   drawn on it, so that throws below the scale are visibly marked.

**From the demonstration's numbers:** with no noise the picked throw is
$40.0\ \mathrm{m}$ (correct), and the quantisation alone (depth sample
$5\ \mathrm{m}$) sets a floor; with a noise rms of $0.10$ the pick is
$55\ \mathrm{m}$ against a true $40\ \mathrm{m}$ — an error of $+15\ \mathrm{m}$
($38\%$). The true throw is $1.60\times\lambda/4$, so it is *resolvable but not
precisely measurable*.

**Threshold for refusing to publish.** Refuse to publish a throw value when the
picking-plus-quantisation uncertainty exceeds **one third** of the throw itself
(the usual "signal-to-uncertainty of 3" convention): here $40/3 = 13.3\ \mathrm{m}$,
and the noisy case's error of $15\ \mathrm{m}$ exceeds it. Below $\lambda/4$ the
throw should be reported as "$\lesssim$ resolution scale" rather than as a
number, because at that level the measurement cannot distinguish a small throw
from a sharp lateral change in impedance.
