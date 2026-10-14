# Solutions — 23-07-04 Case Study: A Marine Geophysical Cruise

The lesson is [04 Case Study: A Marine Geophysical Cruise](../04-case-study-marine-cruise.md).
All values are **SYNTHETIC**.

## ★1

$$t_{\text{two-way}} = \frac{2 \times 3000}{2200} = 2.7273\ \mathrm{s},$$

$$t_{\text{record}} = 2.7273 + 0.8 = \mathbf{3.5273}\ \mathrm{s},$$

$$\text{far offset} = 1.4 \times 3000 = \mathbf{4200}\ \mathrm{m} .$$

So this target needs a record of at least 3.53 s and a cable of about 4.2 km. Note how much
shorter the whole design becomes if the target is only 1.5 km deep (1.36 + 0.8 = 2.16 s, 2.1 km
cable): the depth enters the specification linearly, and it is the reason a survey that must
cover *two* targets is specified for the deeper one even when the shallow target is the
priority.

## ★2

$$\text{cable} = 360 \times 12.5 = 4500\ \mathrm{m} = 4.5\ \mathrm{km},$$

$$F = \frac{N\Delta g}{2\Delta s} = \frac{360 \times 12.5}{2 \times 20} = 112.5, \qquad
\text{bin} = \frac{\Delta g}{2} = 6.25\ \mathrm{m} .$$

A 112.5-fold section with a 6.25 m bin is a high-quality specification: the fold is nearly
double the lesson's 60, which buys a $\sqrt{112.5/60} = 1.37$ improvement in signal-to-noise
over the lesson's design — and *nothing* in resolution. The 20 m shot interval also means a shot
cycle of 8.6 s at 4.5 knots, which is demanding for the source and for the navigation, so the
specification has a schedule cost that must appear in the plan.

## ★3

$$v = 5.0 \times 0.514444 = 2.572\ \mathrm{m/s} = 9.26\ \mathrm{km/h},$$

$$\text{per line} = \frac{45}{9.26} + 0.4 = 4.860 + 0.4 = 5.260\ \mathrm{h},$$

$$\text{survey} = 30 \times 5.260 = 157.8\ \mathrm{h} = 6.57\ \mathrm{days},$$

$$\text{with 25 % weather} = 157.8 \times 1.25 = 197.2\ \mathrm{h} = 8.22\ \mathrm{days},$$

$$\text{plus 100 h transit} = 297.2\ \mathrm{h} = \mathbf{12.38\ days} .$$

The two terms most often omitted are the **turns** (30 × 0.4 = 12.0 h = 7.6 % of the steaming
time) and the **transit** (100 h = 63 % of the steaming time, or half the planned survey). Here
the transit is the dominant line in the schedule, which is exactly the situation in which a port
choice — or a multi-purpose cruise that acquires data on the transit — changes the science that
fits in the window.

## ★4

$$360 \times 800 \times 4 = 1\,152\,000\ \mathrm{B\ per\ shot} = 1.152\ \mathrm{MB},$$

$$70\,000 \times 1.152 = 80\,640\ \mathrm{MB} = \mathbf{80.64\ GB} .$$

The vessel cost is $35 \times 150 = 5250$ k units for the same campaign. So the archive is
**80.64 GB** — under two hours of a modern disk's write time — against a vessel budget of
thousands of units.

What that implies at sea: **never trade data for storage**. Keep the record long, the trace
density full, the navigation logs verbose and the raw data raw; the entire dataset costs less
than the vessel's fuel for a day. The only legitimate reasons to reduce data volume at sea are
the telemetry bandwidth (if any data are sent ashore) and the *processing* time later — and even
then the reduction should be a decimation kept alongside the raw data, not a replacement for it.

## ★5

$$\Delta y = x\sin\alpha :$$

| Feather | Displacement at 2400 m |
|---|---|
| 3° | 125.6 m |
| 7° | 292.5 m |
| 12° | 499.0 m |

So a 12° feather sweeps a 2400 m offset nearly 500 m off the line — a quarter of the cable
length in cross-line displacement, and a clear violation of a 2-D assumption at the far offsets.

The tolerance trade, using the lesson's synthetic distribution (mean 3.97°, sd 1.99°):

| Tolerance | Shots rejected | Cost |
|---|---|---|
| 6° | 15.58 % | about 0.9 days of the lesson's schedule |
| 8° | 1.79 % | negligible |
| 10° | 0.12 % | negligible |
| 12° | 0.00 % | none, but ~500 m of far-offset smear |

The engineering choice is usually **8–10°**: it rejects almost nothing (so the schedule is
untouched) while keeping the far-offset displacement near 300–400 m — and, crucially, the
processing can bin by midpoint and handle a few hundred metres of cross-line offset in a *3-D*
sense if the survey is dense enough in the cross-line direction. A 6° tolerance is a statement
that the survey is strictly 2-D, and it costs a day: that is a legitimate choice, but it must be
made deliberately in the plan rather than discovered as a coverage gap at the end.

## ★6

A model answer.

**Record and cable.** For a 2.5 km target at a synthetic 2400 m/s:

$$t_{\text{two-way}} = \frac{2 \times 2500}{2400} = 2.083\ \mathrm{s}, \qquad
t_{\text{record}} = 2.083 + 1.0 = \mathbf{3.08\ s} \Rightarrow 3.1\ \mathrm{s},$$

$$\text{far offset} \approx 1.4 \times 2500 = 3500\ \mathrm{m} .$$

So: a **3.2 s record** (a small extra margin for a slower velocity than the assumed 2400 m/s) and
a **3.6 km cable**. If the vessel's standard spread is 3.0 km, the far offset is 3000 m — 86 % of
the rule — which is acceptable for the target depth but weakens the velocity inversion *below*
it; that limitation should be stated rather than discovered in processing.

**Intervals, bin and fold.** A 20 m resolution requires a bin no larger than half of that,
i.e. **≤ 10 m**; choose a 12.5 m group interval → **6.25 m bin**. With a 25 m shot interval and
360 channels (4.5 km cable, or 288 channels for 3.6 km): $F = 288 \times 12.5/(2 \times 25) =
72$. The fold is set by the noise level expected at the target: 72-fold is a reasonable
specification for a 2.5 km target in a moderate-noise environment, and if the target is below a
hard seafloor (multiples, scattering) the plan should specify a higher fold at the cost of a
slower line rate, because **fold is the only lever that buys signal-to-noise without changing
the wavelet**.

**Line direction and spacing.** The lines run *dip* to the target structure (perpendicular to
the expected strike, taken from the reconnaissance or from a regional map) with line spacing set
by the cross-line resolution requirement — for a structure 1 km wide, a 1 km spacing with 50 %
overlap (0.5 km) is a reasonable 3-D-quality specification; for a strictly 2-D reconnaissance
programme, 2 km spacing along the strike tie lines. The reason to state this: the line direction
is the one geometry decision that cannot be corrected in processing when the target is 3-D.

**Schedule and the 25 % downtime.** For 1500 line km at 4.5 knots (8.33 km/h):

$$t_{\text{steam}} = \frac{1500}{8.33} = 180.1\ \mathrm{h},$$

and with a typical 60 km line (25 lines, 0.5 h turn each):

$$t_{\text{survey}} = 180.1 + 12.5 = 192.6\ \mathrm{h} = 8.03\ \mathrm{days},$$

so with **25 % weather downtime** the *acquired* time is 8.03 × 1.25 = 10.03 days of vessel days
plus transit (say 4 days of the 30) = about 14 days — comfortably inside the window. That leaves
room for a **repeat line** (a 30 km line acquired twice, 0.9 days) and for a contingency
go-around. The honest warning is that a 30-day window does **not** mean 30 days of acquisition:
transit, mob/demob, port days and weather consume a large fraction, and a plan that spends the
whole window at sea has no reserve for a re-acquisition.

**Feather tolerance.** Specify **8°** with the arithmetic above (1.79 % rejected at the synthetic
distribution, ~290 m of far-offset displacement at a 2400 m offset), i.e. a tolerance that costs
almost no schedule but keeps the geometry within what midpoint binning can handle. Acquire the
navigation and cable-shape data at full rate: they are a rounding error in volume and the only
record of the true geometry.

**At-sea QC and the repeat line.** Daily checks of (i) navigation and feathering per shot against
tolerance, (ii) far-field source signature and streamer noise spectra, (iii) bin and fold
coverage with gaps flagged immediately, and (iv) a repeat line acquired once mid-cruise on the
same heading, giving a direct measure of repeatability (the number a 4-D or time-lapse claim
rests on, and the marine analogue of a reciprocal check).

**What cannot be supported.**

1. **The velocity model below the target depth.** With a far offset shorter than the 1.4× rule,
   the moveout at the deepest reflector is small, so the depth conversion's velocity is
   extrapolated — and the *depth* of the target is then uncertain by more than its *shape*. The
   report must quantify this: a velocity error of 5 % is a depth error of 125 m at 2.5 km, larger
   than the 20 m resolution that the acquisition specification was built around. **Resolution is
   not accuracy**, and the cruise's headline claim should be a vertical *resolution*, with a
   separate, larger *depth uncertainty*.
2. **Any genuinely 3-D target geometry from a set of parallel 2-D lines.** A compact body is
   imaged as a smeared, enlarged feature whose apparent width depends on the line spacing and the
   migration aperture — the same limitation as the ERT case study, and the reason a 3-D
   specification should be argued from the target's expected dimensions rather than assumed.
