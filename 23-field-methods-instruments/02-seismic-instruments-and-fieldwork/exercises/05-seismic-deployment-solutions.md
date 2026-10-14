# Solutions — 23-02-05 Deployment, Orientation, Timing and Metadata

> Read after attempting. Lesson:
> [05 Seismic Deployment](../05-seismic-deployment.md). All values are
> **SYNTHETIC**.

---

## ★1 — Orientation leakage at 8°

$$\sin(8^\circ) = 0.13917, \qquad
20\log_{10}(0.13917) = -17.13\ \mathrm{dB}.$$

So 13.9 % of the radial amplitude appears in the transverse component, at
−17.1 dB relative to the radial.

**Could it be mistaken for anisotropy?** Yes, easily. Shear-wave splitting
measurements on many real datasets report transverse amplitudes at the −20 dB
level and use them to infer a fast direction. An 8° orientation error therefore
produces a *spurious* transverse signal of the same order as the real one, and —
worse — it is coherent and looks physical, because it is produced by the geometry
rather than by noise. A dataset that claims fast directions to better than about
5° must have orientations known to better than about 5°, measured by a stated
method and recorded with their uncertainty.

---

## ★2 — Lock loss over a 60-day deployment

**Station-days with a loss:**

$$\mathbb{E}[\text{station-days}] = N \times D \times p
= 40 \times 60 \times 0.02 = 48.0 .$$

**Stations affected at least once:**

$$P(\text{affected}) = 1 - (1-p)^{D} = 1 - 0.98^{60} .$$

$\ln 0.98 = -0.020203$ and $60 \times (-0.020203) = -1.21218$, so
$0.98^{60} = e^{-1.21218} = 0.29755$ and

$$P(\text{affected}) = 0.70245, \qquad
\mathbb{E}[\text{stations}] = 40 \times 0.70245 = 28.10 \text{ stations}.$$

Note the disproportion: 48 station-days of lost lock (out of 2400 station-days,
i.e. 2 % of the deployment) affects **70 % of the stations**. A station that has
one bad day is a station whose absolute timing must be treated carefully for that
day; the arithmetic is dominated by the number of stations, not by the fraction of
time.

---

## ★★3 — Clock drift

$$\delta t = \epsilon\,t = 2.0\times10^{-6} \times 36 \times 3600\ \mathrm{s}
= 2.0\times10^{-6} \times 129\,600\ \mathrm{s} = 0.2592\ \mathrm{s}.$$

In samples at 200 sps:

$$n = 0.2592 \times 200 = 51.84 \text{ samples}.$$

**Whole deployment without re-acquisition** (60 days):

$$\delta t = 2.0\times10^{-6} \times 60 \times 86\,400
= 2.0\times10^{-6} \times 5\,184\,000 = 10.368\ \mathrm{s}.$$

**Usability.** No. A 10.4 s absolute timing error is tens of kilometres of
apparent mislocation for a regional event and hundreds of kilometres for a
teleseismic one, and it is *not* a constant offset that can be corrected by
aligning waveforms: it drifts, so relative arrival times within the deployment are
also wrong. Such a station can be used only for quantities that do not depend on
absolute time over the affected interval (envelope shapes, spectral content,
relative amplitudes), and the metadata must record the affected interval
explicitly rather than leave a later analyst to discover it.

---

## ★★4 — Coupling resonance at 15 Hz

With $f = 5\ \mathrm{Hz}$, $f_c = 15\ \mathrm{Hz}$, $r = 1/3$ and $h_c = 0.6$:

$$r^{2} = 0.111111, \quad (1-r^{2})^{2} = (0.888889)^{2} = 0.790123,
\quad (2h_c r)^{2} = (0.4)^{2} = 0.160000,$$

$$\sqrt{0.790123 + 0.160000} = \sqrt{0.950123} = 0.974744, \qquad
|H_c| = \frac{0.111111}{0.974744} = 0.113990 .$$

$$20\log_{10}(0.113990) = -18.86\ \mathrm{dB}.$$

So at 5 Hz the installation attenuates the ground motion by a factor of 8.8
relative to the sensor's own specification — a −18.9 dB error that would be
interpreted as a site effect if the installation were assumed ideal.

**Frequency below which the deviation is under 1 dB.** Solve
$|H_c| = 10^{-1/20} = 0.89125$ for $r$ on the low-frequency flank: with $h_c = 0.6$,
try $r = 0.85$: $r^2 = 0.7225$; $(1-0.7225)^2 = 0.077006$;
$(2 \times 0.6 \times 0.85)^2 = (1.02)^2 = 1.0404$;
$\sqrt{1.117406} = 1.05707$; $|H_c| = 0.7225/1.05707 = 0.6835$ (too low).
Try $r = 0.95$: $r^2 = 0.9025$; $(0.0975)^2 = 0.009506$; $(1.14)^2 = 1.2996$;
$\sqrt{1.309106} = 1.14416$; $|H_c| = 0.9025/1.14416 = 0.7888$ (still too low).
Try $r = 0.99$: $r^2 = 0.9801$; $(0.0199)^2 = 0.000396$; $(1.188)^2 = 1.411344$;
$\sqrt{1.411740} = 1.18817$; $|H_c| = 0.9801/1.18817 = 0.8249$.
Try $r = 1.05$: $r^2 = 1.1025$; $( -0.1025)^2 = 0.010506$; $(1.26)^2 = 1.5876$;
$\sqrt{1.598106} = 1.26416$; $|H_c| = 1.1025/1.26416 = 0.8721$.
Try $r = 1.10$: $r^2 = 1.21$; $(0.21)^2 = 0.0441$; $(1.32)^2 = 1.7424$;
$\sqrt{1.7865} = 1.33660$; $|H_c| = 1.21/1.3366 = 0.9053$ (just above 0.89125).
So the −1 dB point is at $r \approx 1.06$, i.e. $f \approx 16\ \mathrm{Hz}$: the
band where the installation is within 1 dB starts essentially *at and above* the
coupling resonance. This is why the design goal is to push $f_c$ far above the band
of interest: with the coupling resonance at 15 Hz and a band of interest ending at
10 Hz, the whole band is compromised.

---

## ★★★5 — Installing a broadband station on soft ground

**Installation.** A concrete or sand-and-gravel pad with the sensor buried at the
base of a shallow pit, or a pier taken to competent ground if the soil is
unconsolidated. The decision is quantitative: from ★★4, the coupling resonance
must lie above the top of the band of interest by a factor that keeps the deviation
inside the tolerance. If the band ends at 1 Hz (broadband work) then a coupling
resonance at even 5 Hz gives, with $h_c = 0.6$ and $r = 0.2$:
$r^2 = 0.04$, $(0.96)^2 = 0.9216$, $(0.24)^2 = 0.0576$,
$\sqrt{0.9792} = 0.98955$, $|H_c| = 0.0404$ → −27.9 dB. So the installation must be
*stiff*: a buried sensor on compacted material, ideally on a concrete pad tied into
a competent layer, with the pit backfilled and compacted in layers and the cable
protected from pulling on the sensor.

**Orientation.** Measure it with a method whose uncertainty is stated and better
than the required anisotropy resolution. From ★1, an 8° error is −17.1 dB of
spurious transverse energy, so if the science target is a fast direction to 5° the
orientation must be known to about 1–2°. Use a gyrocompass or a GNSS heading
system where available, otherwise a magnetic compass with the local declination
applied and its uncertainty recorded. Record: the angle of the north component,
the reference (true north), the method, the instrument used, the declination
applied, and the estimated uncertainty in degrees.

**Clock protocol.** Log the lock state, the satellites or the disciplining source
in use, and the clock offset against a reference (a portable GNSS receiver or the
station's own disciplined time) at power-up, at every site visit, and at
power-down. The log interval is set by the drift budget: from ★★3, a free-running
clock at $2\times10^{-6}$ accumulates 0.26 s in 36 h, so a visit at least every
few days with a reference comparison keeps the interpolation interval short enough
that the residual error stays below a millisecond. Record the affected intervals in
the metadata rather than correcting them silently.

**Levelling tolerance.** From the lesson's inversion, a tilt of 2.1 arcsec
imitates $10^{-5}\ \mathrm{m/s^{2}}$ and 21 arcsec imitates
$10^{-4}\ \mathrm{m/s^{2}}$. For broadband work the tolerance should therefore be
set in arcseconds, not in "bubble centred": state the target, for example
"horizontal components levelled to better than 10 arcsec, measured with a
precision level and recorded".

**Acceptance test.** Record at least several hours and check, in this order:
(i) all three components show the expected ambient noise with no clipping and no
constant channels; (ii) the horizontal noise levels are comparable and are not
dominated by a signal coherent with the vertical component (which would indicate
tilt or a badly coupled sensor); (iii) the clock has held lock with a recorded
offset; (iv) the observed noise in the 0.05–0.5 Hz band is no worse than a
pre-deployment estimate for the site, and if it is, the installation is revisited
before the station is accepted. A station that fails (ii) is usually a coupling or
levelling problem, and it is far cheaper to fix now than to explain later.

---

## ★★★6 — Auditing the metadata of 20 deployed stations

**Items to check, and how to verify each.**

| Item | Verification |
|---|---|
| Station code, position, elevation | Re-measure with a GNSS receiver during the visit; compare with the database |
| Sensor and logger serial numbers | Read the physical labels; compare with the database |
| Orientation | Re-measure with the same method, or check against a polarisation estimate from a known event |
| Levelling | Read the bubble or level; compare with the recorded value |
| Coupling method and burial depth | Photograph and inspect the pit, or note the state if buried |
| Clock state and offset | Compare the station clock with a reference at the visit; read the logger log |
| Gain, filter, sample rate | Read the configuration; compare with the metadata |
| Health of the power and cable | Inspect; this is where most future failures start |

The distinction that matters: **items checked by measurement** (position,
orientation, levelling, clock) versus **items checked by document** (serial
numbers, gain settings). A document check confirms that the record matches what is
written down; only a measurement confirms that it matches the world.

**Scoring rule.** For each station, classify each item as *correct*,
*missing*, or *wrong* (present but contradicting the measurement). Report the
counts per item; do not average them into a single percentage unless the weights
are stated, because a wrong orientation and a missing operator initial are not
equivalent errors.

**Metrics to report.**

1. **Item-level error rates** — for each item, the fraction of stations for which
   it is wrong, and separately missing (dimensionless).
2. **Station-level usability** — the number of stations whose errors affect an
   identifiable class of measurement (absolute timing, horizontal components,
   amplitude calibration), in stations.
3. **Correction effort** — the estimated person-hours to re-measure the wrong
   items (hours).
4. The **uncertainty of the audit itself**: an orientation check that uses the same
   method that produced the original error will reproduce it. Where possible,
   verify with an independent method, and say which checks were independent.

**Two classes of error the audit cannot detect.**

1. **Errors that are consistent between the record and the world.** If the sensor
   was installed 180° from the recorded direction *and* the record was written from
   the same wrong assumption, the document check passes and the re-measurement
   during the visit may repeat the mistake. Detecting this needs an independent
   physical reference (a polarisation analysis of a known event, or an invasive
   check of the installation).
2. **Errors that developed after the visit.** A sensor can be moved by frost heave,
   livestock, or a subsequent maintenance visit that changed the levelling without
   updating the metadata. The audit is a point-in-time measurement, and
   between-visit changes are invisible to it; only continuous monitoring (tilt
   sensors, repeated polarisation checks) would catch them.
