# Solutions — 23-02-01 Seismometers: Broadband, Short-Period, Geophones, MEMS

> Read after attempting. Lesson:
> [01 Seismometers](../01-seismometers.md). All values are **SYNTHETIC**.

---

## ★1 — Response at 0.5 Hz

With $f_0 = 2.0\ \mathrm{Hz}$, $h = 0.6$ and $f = 0.5\ \mathrm{Hz}$:
$r = 0.5/2.0 = 0.25$, so $r^{2} = 0.0625$ and

$$(1-r^{2})^{2} = (0.9375)^{2} = 0.878906, \qquad
(2hr)^{2} = (0.30)^{2} = 0.090000 .$$

$$\sqrt{0.878906 + 0.090000} = \sqrt{0.968906} = 0.984329, \qquad
|H| = \frac{0.0625}{0.984329} = 0.063495 .$$

In decibels: $20\log_{10}(0.063495) = -23.945\ \mathrm{dB}$.

**Meaning.** At 0.5 Hz the sensor's output is 0.0635 of what the same ground
velocity would produce above the corner. Since the response below the corner is
proportional to $f^{2}$ for a velocity transducer, a signal at 0.5 Hz is recorded
about $15.7\times$ smaller than the same signal at 10 Hz — before any noise
consideration.

---

## ★2 — The −3 dB corner and the resonance peak

Solve $r^{2}/\sqrt{(1-r^{2})^{2} + (2hr)^{2}} = 1/\sqrt{2}$ numerically on
$0 < r < 1$. Trial values:

| $r$ | $f$ (Hz) | $|H|$ |
|---|---|---|
| 0.70 | 1.400 | 0.4986 |
| 0.80 | 1.600 | 0.6240 |
| 0.85 | 1.700 | 0.6913 |
| 0.87 | 1.740 | 0.7126 |
| 0.8690 | 1.7379 | 0.7070 |

So $f_{-3\,\mathrm{dB}} \approx 1.742\ \mathrm{Hz}$, i.e. $r \approx 0.871$. The
corner sits *below* the natural frequency because the damping term contributes to
the denominator there.

**At $f = f_0$**: $r = 1$, the first term of the denominator vanishes and

$$|H| = \frac{1}{2h} = \frac{1}{1.2} = 0.833333 \;\Rightarrow\;
20\log_{10} 0.833333 = -1.584\ \mathrm{dB}.$$

This is a **notch**, not a peak: the *velocity* response magnitude of an inertial
sensor is monotonically increasing in $r$ and approaches 1, so the only feature
near the natural frequency is this dip of depth $1/(2h)$. The classic resonance
peak belongs to the displacement response
$|H_d| = |H|/r^{2} = 1/\sqrt{(1-r^{2})^{2}+(2hr)^{2}}$, which peaks at
$r = \sqrt{1-2h^{2}}$ when $h < 1/\sqrt{2}$ — for $h = 0.6$ that is
$r = 0.5292$, with $|H_d|_{\max} = 1/(2h\sqrt{1-h^{2}}) = 1/(1.2 \times 0.8)
= 1.0417$, an overshoot of only **0.354 dB**. Damping near $1/\sqrt{2}$
flattens that overshoot entirely, which is why feedback sensors are damped there.

---

## ★★3 — Input-referred self-noise and the crossover

$$n_{\text{in}}(0.5\ \mathrm{Hz})
= \frac{n_{\text{out}}}{G\,|H(0.5)|}
= \frac{2.0\times10^{-7}}{100 \times 0.063495}
= \frac{2.0\times10^{-9}}{0.063495}
= 3.150\times10^{-8}\ \mathrm{m/s/\sqrt{Hz}} .$$

Note the units: $\mathrm{(V/\sqrt{Hz}) / (V/(m/s))} = \mathrm{m/s/\sqrt{Hz}}$;
the response $|H|$ is dimensionless.

**Crossover.** Require $n_{\text{in}}(f) = 1.0\times10^{-7}$, i.e.

$$|H(f)| = \frac{n_{\text{out}}}{G \times 1.0\times10^{-7}}
= \frac{2.0\times10^{-9}}{1.0\times10^{-7}} = 0.020 .$$

Solving $r^{2}/\sqrt{(1-r^{2})^{2} + (2hr)^{2}} = 0.020$ gives $r = 0.1410$ and

$$f = 0.1410 \times 2.0 = 0.282\ \mathrm{Hz}.$$

**Meaning.** Below 0.282 Hz this sensor's own noise exceeds an ambient ground
motion of $1.0\times10^{-7}\ \mathrm{m/s/\sqrt{Hz}}$; above it, the sensor can see
the site. The sensor's *specified* corner is 2 Hz, so its usable band extends
about $7\times$ below its corner at this noise level — and would extend further
at a noisier site, where the crossover moves to a lower frequency.

---

## ★★4 — Clip level and electronic dynamic range

$$v_{\text{clip}} = \frac{V_{\text{FS}}}{G} = \frac{5.0}{200} = 0.0250\ \mathrm{m/s}.$$

$$\text{LSB} = \frac{2 \times 5.0}{2^{24}} = \frac{10.0}{16\,777\,216}
= 5.9605\times10^{-7}\ \mathrm{V},$$

$$q = \frac{\text{LSB}}{\sqrt{12}} = \frac{5.9605\times10^{-7}}{3.4641}
= 1.7206\times10^{-7}\ \mathrm{V}.$$

Referred to ground velocity through $G$:

$$v_{q} = \frac{q}{G} = \frac{1.7206\times10^{-7}}{200}
= 8.603\times10^{-10}\ \mathrm{m/s}.$$

$$\text{range} = 20\log_{10}\frac{v_{\text{clip}}}{v_{q}}
= 20\log_{10}\frac{0.0250}{8.603\times10^{-10}} = 20\log_{10}(2.906\times10^{7})
= 149.27\ \mathrm{dB}.$$

**Why this is not the usable range for ground motion.** The range computed here is
between the converter's full scale and the converter's own quantisation noise, both
measured through the same gain, so the gain cancels: 149.27 dB is essentially the
converter's 146.24 dB plus the 3.03 dB difference between a peak full-scale
sinusoid and an rms quantisation floor. The *usable* range for ground motion is
much narrower at both ends: at the top it stops where the sensor behaves linearly
(often well below the converter's clip), and at the bottom it stops where the
sensor's self-noise and the site's ambient noise exceed the quantisation floor. A
number like 149 dB describes the electronics, not the measurement.

---

## ★★★5 — A MEMS accelerometer at long periods

For a flat acceleration response, the equivalent ground-velocity noise is the
acceleration noise divided by $\omega = 2\pi f$:

$$v_{\text{eq}}(f) = \frac{a_n}{2\pi f} .$$

At $f = 0.01\ \mathrm{Hz}$: $\omega = 0.062832\ \mathrm{rad/s}$,

$$v_{\text{eq}} = \frac{1.0\times10^{-4}}{0.062832}
= 1.592\times10^{-3}\ \mathrm{m/s/\sqrt{Hz}},$$

which is $1.592\times10^{-3}/2.236\times10^{-5} = 71.2$ times the ambient model.

At $f = 1\ \mathrm{Hz}$: $\omega = 6.28319\ \mathrm{rad/s}$,

$$v_{\text{eq}} = \frac{1.0\times10^{-4}}{6.28319}
= 1.592\times10^{-5}\ \mathrm{m/s/\sqrt{Hz}},$$

which is $1.592\times10^{-5}/5.958\times10^{-8} = 267$ times the ambient model.

**Conclusion.** This accelerometer cannot resolve ambient ground motion in either
band: it is between two and nearly three orders of magnitude above the ambient
noise. Its useful regime is the opposite one — strong motion, where the ground
acceleration is many orders of magnitude above the ambient level and the
requirements are a large linear range, a flat response in acceleration and no
clipping. The same arithmetic applied in reverse explains why a broadband sensor
is useless for strong motion: its suspended mass hits its stops, and after that
the record is an artefact.

---

## ★★★6 — A field verification test for a deployed sensor

**Measurement.** Two independent checks, both done on site:

1. **Cross-sensor comparison.** Deploy the station sensor and a second sensor of a
   different type (or a known-good reference) side by side on the same pad, record
   simultaneously for at least a few hours, and compute the ratio of their
   amplitude spectra (and their cross-phase) after removing each sensor's nominal
   response.
2. **Ambient-noise self-consistency.** For a three-component sensor, compare the
   horizontal components rotated into radial/transverse; a well-installed sensor
   on a quiet site gives comparable horizontal noise levels, while a tilted or
   poorly coupled one shows a tilt-induced long-period signal that is coherent
   with the vertical component.

**Reference.** For (1), the second sensor with its own manufacturer calibration or
a field calibration performed with a calibrated coil or a portable shaker table.
For a purely relative check, the *ratio* between two sensors is the reference:
whatever the true ground motion, it is common to both.

**Metric and units.** The frequency-dependent amplitude ratio
$A(f) = |X_{\text{test}}(f)|/|X_{\text{ref}}(f)|$ (dimensionless, expected to be
flat and equal to 1 after correction), reported in dB, and the cross-phase
$\phi(f)$ in degrees, expected to be 0.

**Acceptance threshold.** Flag the sensor when $|20\log_{10}A(f)|$ exceeds a
stated tolerance (commonly about 1 dB in the passband) or when $|\phi(f)|$ exceeds
a few degrees in the passband, over a band that spans at least a decade.

**Failure modes detected.** A wrong generator constant, a wrong damping constant,
a damaged spring (changed natural frequency), a saturated or drifting output, a
tilted sensor, a mis-wired component, and a response file that does not describe
the deployed unit.

**What it cannot test.** (i) The **absolute** response at long periods, because
neither the ambient noise nor the reference sensor is known absolutely at those
frequencies — the test is relative, and a common-mode error cancels. (ii) The
**level accuracy** at large amplitudes: a comparison at ambient level cannot see a
nonlinearity or a clip that only occurs in strong motion. An absolute check needs
a calibrated stimulus, which is a laboratory exercise
([23-05-04 Calibration, Testing and Traceability](../../05-instrumentation-and-electronics/04-calibration-and-testing.md)).
