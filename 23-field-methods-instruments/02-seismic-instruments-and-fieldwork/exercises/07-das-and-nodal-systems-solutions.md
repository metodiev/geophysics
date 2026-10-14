# Solutions — 23-02-07 Nodal Systems and Distributed Acoustic Sensing in the Field

> Read after attempting. Lesson:
> [07 DAS and Nodal Systems](../07-das-and-nodal-systems.md). All values are
> **SYNTHETIC**.

---

## ★1 — Gauge notches at 5 m and 2000 m/s

$$f_{\text{notch}} = \frac{k v}{L} = \frac{k \times 2000}{5} = 400k\ \mathrm{Hz}.$$

So the first two notches are at **400 Hz** and **800 Hz**.

Response at 100 Hz, with $x = \pi f L/v = \pi \times 100 \times 5/2000 = 0.7854$:

$$|H| = \left|\frac{\sin 0.7854}{0.7854}\right| = \frac{0.70711}{0.7854}
= 0.9003 .$$

So the 5 m gauge attenuates 100 Hz by 0.90 — about 0.9 dB — and the first notch is
well above the band. Compare with the lesson's 10 m gauge on a 1500 m/s fibre,
which notched at 150 Hz: the gauge response scales with $L/v$, so a faster fibre or
a shorter gauge pushes the notches up.

---

## ★2 — Alias frequency and channel count

$$f_{\text{alias}} = \frac{v}{2\Delta x} = \frac{2000}{2 \times 2} = 500\ \mathrm{Hz},
\qquad
\text{channels per km} = \frac{1000}{2} = 500 .$$

**Which limits the band?** The gauge notches at 400 Hz; the spacing aliases at
500 Hz. The **gauge is the binding constraint** — and only just, so the design is
reasonably balanced. If the required band ended at 200 Hz both would be
comfortable; if it extended to 400 Hz, the gauge would have to be shortened *and*
the spacing kept at 2 m or finer. The general rule: compute both limits, take the
smaller, and if you must widen the band, widen both — shortening the gauge alone
would leave an aliased record, and reducing the spacing alone would produce more
channels of already-filtered data.

---

## ★★3 — Conversions for a 1 µm/s wave at 5 Hz

Angular frequency: $\omega = 2\pi \times 5 = 31.4159\ \mathrm{rad/s}$.
Wavenumber along the fibre: $k = \omega/v = 31.4159/1200 = 0.026180\ \mathrm{rad/m}$.

**Displacement amplitude** from the velocity amplitude
$A\dot u = \omega A$:

$$A = \frac{1.0\times10^{-6}}{31.4159} = 3.183\times10^{-8}\ \mathrm{m}
= 31.83\ \mathrm{nm}.$$

**Strain:**

$$\varepsilon = kA = 0.026180 \times 3.183\times10^{-8}
= 8.333\times10^{-10}\ \text{(dimensionless, 0.833 nanostrain)}.$$

**Strain rate:**

$$\dot\varepsilon = \omega k A = 31.4159 \times 8.333\times10^{-10}
= 2.618\times10^{-8}\ \mathrm{s^{-1}}.$$

**Acceleration:**

$$a = \omega^{2} A = (31.4159)^{2} \times 3.183\times10^{-8}
= 3.142\times10^{-5}\ \mathrm{m/s^{2}}.$$

**Check the constant factor.** Strain rate $= a/v$:
$3.142\times10^{-5}/1200 = 2.618\times10^{-8}\ \mathrm{s^{-1}}$ ✔. The factor is
$1/v$, frequency-independent: converting DAS strain rate to acceleration is a
single multiplication, which is why a DAS record and an accelerometer record have
the same spectral shape and differ only by scale.

Units: $A$ in m, $\varepsilon$ dimensionless, $\dot\varepsilon$ in s⁻¹, $a$ in
m/s².

---

## ★★4 — Nodal margins

**Continuous margin:**

$$\frac{40\ \text{days}}{15\ \text{days}} = 2.67\times .$$

**At 6 h/day:** the duty cycle is $6/24 = 0.25$, so the battery lifetime becomes

$$\frac{40}{0.25} = 160\ \text{days}, \qquad
\frac{160}{15} = 10.7\times .$$

**What the duty cycle costs.** It records 6 h per day, i.e. 25 % of the time, so
75 % of any event that is not predicted in advance is missed, and the record is
useless for ambient-noise or long-period work because the sampling is not
continuous. Any spectral or correlation analysis across the gaps is invalid.

**Unacceptable for:** earthquake or induced-seismicity monitoring, ambient-noise
interferometry, and any study whose target events are unpredictable. It is
acceptable for a controlled-source experiment, a scheduled injection, or a
survey in which the recording windows are known in advance and synchronised with
the source.

Note also that the battery is rarely the binding constraint: the planting and
harvesting labour, the data volume and the charging time all scale with the
channel count, and a survey that doubles its nodes doubles those costs even if the
battery margin is comfortable.

---

## ★★★5 — DAS design for 5–200 Hz borehole monitoring

**Gauge length.** The first notch is at $f_1 = v/L$, and the notch must lie above
the top of the band with margin — a factor of about 1.5 is a reasonable design
convention, so the gauge must satisfy $L \le v/(1.5 \times 200) = v/300$. For a
formation with $v = 2500\ \mathrm{m/s}$ this gives $L \le 8.3\ \mathrm{m}$; for a
soft formation with $v = 800\ \mathrm{m/s}$ it gives $L \le 2.7\ \mathrm{m}$. So
**the gauge cannot be chosen without the velocities** — a soft formation forces a
short gauge. Take $v = 2500\ \mathrm{m/s}$ and a **5 m gauge**, giving notches at
500, 1000, … Hz and a response at 200 Hz of
$\operatorname{sinc}(\pi \times 200 \times 5/2500) = \operatorname{sinc}(1.257) = 0.757$,
i.e. −2.4 dB — acceptable with the margin budget.

**Channel spacing.** The alias frequency must also exceed 200 Hz with margin:
$\Delta x \le v/(2 \times 1.5 \times 200) = v/600 = 4.2\ \mathrm{m}$ at
$v = 2500\ \mathrm{m/s}$. Take **2 m**, giving $f_{\text{alias}} = 625\ \mathrm{Hz}$
and 500 channels per kilometre. The spacing is comfortably finer than required,
which is the correct direction: an aliased record cannot be repaired, whereas the
extra channels cost only data volume.

**Channel count.** For a 1.5 km fibre at 2 m spacing:

$$N = \frac{1500}{2} = 750 \text{ channels}.$$

At a 10 kHz sample rate with 4-byte samples this is
$750 \times 10\,000 \times 4 = 3\times10^{7}\ \mathrm{B/s} = 30\ \mathrm{MB/s}$,
or about 2.6 TB per day — the reason spatial decimation and on-site reduction are
standard practice, and a constraint to plan before the campaign rather than after.

**Required sensitivity and its verification.** The requirement follows from the
target: the smallest event must produce a strain rate above the fibre's noise.
Using the lesson's conversion, a target particle velocity of $v_{\text{target}}$
gives a strain rate $k v_{\text{target}} = \omega v_{\text{target}}/v$. Require the
fibre's single-sample strain sensitivity (or, better, its noise spectral density)
to lie below that value across the band. Verify it in the field by
co-locating a broadband seismometer or an accelerometer at a known depth and
comparing the two records after converting the DAS strain rate to acceleration by
$v$; the ratio of the spectra is the product of the relative calibration and the
two installation responses, and its frequency dependence is the diagnostic. A
repeat of this comparison after the installation is complete is the acceptance
test.

**The two design choices that require the velocities.** (i) The gauge length,
through $f_1 = v/L$; (ii) the channel spacing, through $f_{\text{alias}} = v/(2\Delta x)$.
A third, subtler one also depends on the velocity structure: the interpretation
itself, because the conversion between strain rate and ground motion uses the
apparent velocity along the fibre, which for a borehole at an angle to the ray path
is not the formation velocity.

---

## ★★★6 — Measuring the installation transfer function of a trenched fibre

**Reference.** A co-located point sensor with a known response, installed in the
same trench at the same depth within a few metres of the fibre, so that both
experience the same ground motion. Ideal: a three-component geophone or
accelerometer grouted in the same backfill.

**Stimulus.** Two complementary sources, because neither alone covers the band:

1. **Controlled sources on the surface** — a hammer, a weight drop or a small
   vibrator at known offsets and azimuths — repeated many times and stacked. This
   gives a repeatable, broad-band stimulus with a known source position, and it can
   be moved along the line to sample the along-fibre variation.
2. **Ambient noise**, cross-correlated between the DAS channels and the reference
   sensor. This covers the band where ambient energy is available and is the only
   practical option where a controlled source is impossible (a producing well, a
   pipeline in service).

**Metric.** The frequency-domain ratio of the DAS strain rate (converted to
acceleration by multiplying by the apparent velocity $v$) to the reference
accelerometer, i.e. a dimensionless transfer function, reported in dB as a function
of frequency and of position along the fibre. The diagnostic is its *departure from
flat*: a flat ratio at all frequencies indicates a simple scaling (a calibration
factor), while a frequency-dependent ratio indicates an installation response. The
coherence between the two records is reported at the same time, because a ratio
computed where the coherence is low is noise.

**Frequency band it can constrain.** Downward, by the reference sensor's own noise
floor (below roughly 1 Hz a broadband sensor is required, and below its corner the
comparison fails); upward, by the stimulus bandwidth (a hammer or a small vibrator
rolls off in the hundreds of hertz) and by the gauge response, which must be
divided out. Realistically the measurement constrains roughly 1–200 Hz for a
broadband reference with an impulsive surface source.

**What it cannot determine.** (i) The transfer function at frequencies where
neither source provides energy — the gaps in the band are gaps in the knowledge,
not zero response. (ii) The *absolute* sensitivity of the fibre away from the
reference location, because the comparison constrains only the product of the
instrument calibration and the installation response, and separating the two
requires an independent calibration of the reference or of the fibre — the same
absolute-versus-relative distinction as in
[23-05-04 Calibration, Testing and Traceability](../../05-instrumentation-and-electronics/04-calibration-and-testing.md).
