# Solutions — 23-05-03 Timing, GNSS Disciplining and Clock Accuracy

> Read after attempting. Lesson:
> [03 Timing and GNSS Instruments](../03-timing-and-gnss-instruments.md). All values
> are **SYNTHETIC**.

---

## ★1 — Accumulated time and apparent distance

$$\delta t = \epsilon T .$$

**6 h** ($T = 21\,600$ s):

$$\delta t = 2.5\times10^{-7} \times 21\,600 = 5.4\times10^{-3}\ \mathrm{s}
= 5.4\ \mathrm{ms}.$$

**15 days** ($T = 1\,296\,000$ s):

$$\delta t = 2.5\times10^{-7} \times 1.296\times10^{6} = 0.324\ \mathrm{s}.$$

**Apparent distance after 6 h** at 2.5 km/s:

$$\delta R = V\,\delta t = 2500 \times 5.4\times10^{-3} = 13.5\ \mathrm{m}.$$

A 13.5 m apparent mislocation after six hours, growing to 810 m after fifteen days
($2500 \times 0.324$), makes the point: this clock is usable only with a lock, or
with a much shorter deployment, or with a post-hoc correction from the locked
period. Note also that 5.4 ms at 100 sps is 540 samples — the timing error is not a
rounding artefact, it is 540 samples of apparent misalignment.

---

## ★2 — Holdover and budget

$$\text{drift per day} = 5\times10^{-8} \times 86\,400 = 4.32\times10^{-3}\ \mathrm{s}
= 4.32\ \mathrm{ms\ per\ day}.$$

$$T_{\text{holdover}} = \frac{0.5\ \mathrm{ms}}{4.32\ \mathrm{ms/day}}
= 0.1157\ \mathrm{days} = 2.78\ \mathrm{h}.$$

**Under three hours.** With this holdover, the station must re-acquire its lock
every few hours, or the science requirement must be relaxed, or a better oscillator
used. The arithmetic is the whole of the planning question: the holdover rate and the
budget fix the re-visit interval, and the re-visit interval is usually far shorter
than the battery life — a fact that surprises teams who plan by power budget alone.

---

## ★★3 — Averaging jitter

$$\sigma_{\text{eff}} = \frac{30}{\sqrt{400}} = \frac{30}{20}
= 1.5\ \mathrm{ns}.$$

**What averaging cannot reduce.** The **constant offset** between the PPS output and
the true second: the receiver's internal delay, the antenna and cable delays, and
any asymmetry in the detection of the pulse edge. These are systematic, they are the
same on every pulse, and averaging $N$ identical offsets leaves the offset unchanged
while reducing the scatter about it. The remedy is calibration against a reference
(a time-transfer service, a co-trace of a common event with a calibrated receiver, or
a round-trip measurement), and the offset must be recorded with its uncertainty. At a
100 m/s apparent velocity even 30 ns is 3 µm, but at the 10⁵ m/s of a regional
seismic phase, 30 ns is 3 mm — still small; the real concern is the *absolute*
accuracy of the reference time used to define the picks, which is a different and
larger error.

---

## ★★4 — Allan deviation and the two error accumulations

$$\sigma_y(1000\ \mathrm{s}) = \frac{5\times10^{-12}}{\sqrt{1000}}
= \frac{5\times10^{-12}}{31.623} = 1.581\times10^{-13}.$$

**Random accumulation over one day** ($T = 86\,400$ s):

$$\sigma_x(T) = \sigma_y(1\ \mathrm{s})\sqrt{T \cdot 1\ \mathrm{s}}
= 5\times10^{-12} \times 293.94 = 1.470\times10^{-9}\ \mathrm{s}
= 1.47\ \mathrm{ns}.$$

**Systematic offset over the same day:**

$$\epsilon T = 5\times10^{-12} \times 86\,400 = 4.32\times10^{-7}\ \mathrm{s}
= 432\ \mathrm{ns}.$$

So the systematic part is $432/1.47 = 294$ times the random part: the offset
dominates by nearly two and a half orders of magnitude. The practical consequence is
that a *clock comparison* — measuring the time offset between two sites that record a
common event — is limited by the two clocks' offsets and not by their noise, and the
comparison's accuracy is improved by correcting the offsets (disciplining), not by
averaging longer.

---

## ★★★5 — A timing plan for a 30-station array at 0.5 ms

**Reference and disciplining.** Every station carries a GNSS receiver disciplined to
GNSS time, with the receiver's PPS and a local oscillator (a temperature-compensated
or oven-controlled crystal) in a phase-locked or frequency-locked loop. The lock
state, the offset and the loop's tuning are logged continuously.

**Required holdover.** From the budget of 0.5 ms and the planned re-visit interval
$T_{\text{visit}}$ (days), the holdover rate must satisfy

$$\epsilon_{\text{holdover}} \le \frac{0.5\ \mathrm{ms}}{T_{\text{visit}} \times 86\,400\ \mathrm{s}} .$$

For a weekly visit ($T_{\text{visit}} = 7$):

$$\epsilon_{\text{holdover}} \le \frac{5\times10^{-4}}{6.048\times10^{5}}
= 8.27\times10^{-10}\ \mathrm{per\ day}.$$

For a monthly visit: $1.93\times10^{-10}$ per day. Both are in the range a
disciplined oscillator achieves during holdover, but each must be **verified**, not
assumed, because the specification is quoted at a nominal temperature.

**Verification.** (i) Before deployment, subject one station to an extended lock
loss in its enclosure and measure the accumulated offset against a reference over
several days — that is a direct measurement of the holdover rate under the actual
thermal conditions. (ii) In the field, record the clock offset at every visit and
compare with the previous visit's value; the slope is the realised holdover, and it
should be reported per station. (iii) Where two stations are close enough to record a
common event, compare their clock offsets directly.

**Maintenance interval.** With $\epsilon = 8.27\times10^{-10}$ per day and a 0.5 ms
budget the interval is seven days; but the *measured* holdover replaces the assumed
one, so the interval is recomputed after the first visit. The planning number to
carry is 7 days at 8.3e−10, and it should be checked against the battery, the data
storage and the access constraints — all of which may be longer, in which case the
timing is the binding constraint.

**Logging.** Per station and per day: the lock state and the fraction of the day
locked, the measured clock offset against the reference, the oscillator's control
voltage or tuning word, the temperature of the enclosure, the receiver's satellite
count and signal quality, and the antenna cable delay calibration. The offset series
is what allows a post-hoc correction of the unlocked intervals, and it cannot be
reconstructed later.

**Check at a site visit.** Compare the station clock with a portable reference
(a portable GNSS receiver or a disciplined counter), record the difference and its
time, and verify that the difference is consistent with the holdover rate measured at
the previous visit. A difference that is *smaller* than expected is as suspicious as
one that is larger: it can mean the lock was re-acquired without being logged, or
that the oscillator has a temperature coefficient that the enclosure is masking on
that particular day.

---

## ★★★6 — Testing the absolute timing offset of a recording system

**Equipment.** (i) A reference time source traceable to a national time scale — a
GNSS-disciplined clock with a *calibrated* cable and receiver delay, or a portable
time-transfer receiver. (ii) A pulse or step generator whose output can be injected
into the recording system's channel (through a capacitive or a transformer coupling,
so the injection does not disturb the input's DC conditions). (iii) A time-interval
counter, itself referenced to the same source, to measure the injected pulse's time
against the reference's PPS.

**Method.** Inject the same event into the recorder and the counter simultaneously
(or with a measured split), digitise it, and locate the event in the record by the
same method used in the science analysis (a first-break pick, a cross-correlation, or
a threshold crossing). The offset is the difference between the pick's time in the
record and the reference time of the pulse. Repeat it at several times of day and at
both edges of the sampling clock to expose a phase-dependent error.

**Metric.** The offset in microseconds, with its repeatability (the standard
deviation over repeats) and its stability over a day (the drift of the offset). The
*absolute* accuracy is the offset plus the uncertainty of the reference's own trace.

**Repeatability required.** The repeatability must be much better than the science
requirement: to claim a 0.5 ms accuracy, demonstrate a repeatability of a few tens of
microseconds — at least ten times better — and report both numbers. A test that
repeats to 1 ms cannot establish a 0.5 ms requirement.

**Two systematic effects the test cannot distinguish.**

1. **The injected pulse's own delay versus a real signal's delay through the
   input's analogue chain.** Injection at the input connector measures the digital
   and sampling delays but not the sensor, the cable and the input filter, whose
   delays are part of the system's timing. A test that does not include the full
   chain will report an offset that is too small, and the missing part must be
   measured or bounded separately (for example with a known travel-time path or a
   co-located reference sensor).
2. **A common offset between the recorder and the reference.** If both use the same
   GNSS receiver or the same antenna, a receiver-delay error or a cable-delay error
   is present in both and cancels in the comparison, leaving the test blind to it.
   Only a *different* reference — another receiver with an independently calibrated
   delay, or a time-transfer service — reveals the common part.
