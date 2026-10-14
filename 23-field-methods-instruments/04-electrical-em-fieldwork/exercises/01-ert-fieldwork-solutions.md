# Solutions — 23-04-01 ERT Fieldwork: Electrode Layouts, Contact Resistance, Reciprocity

> Read after attempting. Lesson:
> [01 ERT Fieldwork](../01-ert-fieldwork.md). All values are **SYNTHETIC**.

---

## ★1 — Geometric factor of a Wenner array at 10 m

Closed form:

$$K = 2\pi a = 2\pi \times 10 = 62.8319\ \mathrm{m}.$$

Exact formula with $A = 0$, $M = 10$, $N = 20$, $B = 30$ m, so
$AM = 10$, $BM = 20$, $AN = 20$, $BN = 10$ m:

$$K = \frac{2\pi}{\dfrac{1}{10} - \dfrac{1}{20} - \dfrac{1}{20} + \dfrac{1}{10}}
= \frac{2\pi}{0.1 - 0.05 - 0.05 + 0.1} = \frac{2\pi}{0.1}
= 62.8319\ \mathrm{m}.$$

The two agree exactly, which is the check the lesson recommends: the electrode
*order* matters, and a wrong denominator (using $BM = 30$ instead of 20, which
happens when the electrode numbering is misread) would give
$2\pi/0.116667 = 53.86$ m — a 14 % error in $K$ and therefore in every resistivity
derived from it, with no field symptom.

Units: $K$ in metres, since each $1/r$ term has units of m⁻¹.

---

## ★2 — Apparent resistivity and error

$$K = \frac{\rho_a I}{\Delta V}
= \frac{120 \times 4\times10^{-3}}{20\times10^{-3}}
= \frac{0.480}{0.020} = 24.0\ \mathrm{m}.$$

Check the round trip: $K\Delta V/I = 24 \times 0.020/0.004 = 120.0\
\Omega\,\mathrm{m}$ ✔.

Relative error:

$$\frac{\delta\rho_a}{\rho_a} = \sqrt{0.03^{2} + 0.01^{2}}
= \sqrt{0.0009 + 0.0001} = \sqrt{0.001} = 0.031623 \;(3.162\ \%).$$

Absolute error:

$$\delta\rho_a = 0.031623 \times 120 = 3.795\ \Omega\,\mathrm{m}.$$

So the result is $120 \pm 4\ \Omega\,\mathrm{m}$ (one standard error). Note that
the current error contributes only 10 % of the variance here, so improving the
current measurement further would not help: the voltage error dominates, and the
field effort should go into signal quality (contacts, stacking, cable routing)
rather than into a more precise ammeter.

---

## ★★3 — Injected current and signal ratio

$V_{\max} = 200$ V, $R_{\text{ground}} = 30$ Ω, and
$R_{\text{loop}} = 2R_{\text{contact}} + R_{\text{ground}}$.

**500 Ω contacts:**

$$R_{\text{loop}} = 2(500) + 30 = 1030\ \Omega, \qquad
I = \frac{200}{1030} = 0.19417\ \mathrm{A} = 194.17\ \mathrm{mA}.$$

**50 kΩ contacts:**

$$R_{\text{loop}} = 2(50\,000) + 30 = 100\,030\ \Omega, \qquad
I = \frac{200}{100\,030} = 1.9994\times10^{-3}\ \mathrm{A} = 2.00\ \mathrm{mA}.$$

**Signal ratio.** The measured potential is proportional to the injected current, so

$$20\log_{10}\!\left(\frac{194.17}{2.00}\right)
= 20\log_{10}(97.1) = 39.75\ \mathrm{dB}.$$

So the poor contact costs about **40 dB** — a factor of nearly 100 in signal
amplitude, which for a fixed receiver noise floor is a factor of 100 in
signal-to-noise and, in practice, the difference between a usable reading and no
reading at all. Improving the contact is the cheapest available improvement in ERT
data quality, and it is done with water, deeper stakes or bentonite, not with a
larger transmitter: a transmitter with double the compliance would recover only
6 dB of the 40.

---

## ★★4 — Reciprocity tolerance

$$\frac{\delta\rho_a}{\rho_a}\bigg|_{\text{reciprocal}}
= \sqrt{2} \times 0.04 = 0.05657 \;(5.66\ \%).$$

A difference of 25 % is

$$\frac{25}{5.66} = 4.4 \text{ times the tolerance},$$

which is far outside noise. Candidate defects, in the order a field crew would
check them:

1. **A geometry error** — an electrode not where it is recorded, or a cable
   connected to the wrong take-out. This is the most common cause, and it is
   detectable immediately because the reciprocal measurement uses the *same four*
   electrodes; a position error changes $K$ in one direction only.
2. **A cable or take-out fault** — a high resistance in a potential-electrode
   circuit, which loads the measurement differently in the two configurations.
3. **A non-linear coupling at an electrode** — a corroded stake, an electrode in
   contact with buried metal, or an electrode in a very dry hole that breaks down
   under current. The two configurations inject current through different
   electrodes, so a contact that behaves non-linearly shows up here and nowhere
   else.

---

## ★★★5 — Design for a 40 m target over a 300 m line

**Electrode spacing and count.** The largest current–potential separation sets the
deepest information. With the conventional Wenner median depth of about $0.5a$ for
spacing $a$, a 40 m target needs $a$ of order 80 m, i.e. a total array length of
$3a = 240$ m. A 300 m line therefore accommodates the required array with margin.
Choose a **10 m electrode spacing** and **31 electrodes** (0 to 300 m in 10 m
steps), which gives:

- maximum Wenner spacing $a_{\max} = 30 \times 10/3 = 100$ m (limited by the need
  for four electrodes at $0, a, 2a, 3a$ inside the line), i.e. a nominal maximum
  depth of about 50 m — comfortably deeper than the target;
- the same electrodes support dipole-dipole with separations up to $n = 29$, whose
  larger $K$ values probe deeper but with weaker signal.

**Configurations.** Use a standard multi-array protocol containing:

1. **Wenner $\alpha$** — the best signal-to-noise and the most reliable shallow
   coverage;
2. **Dipole-dipole** — the best lateral resolution and the largest depth range, at
   the cost of signal ($K$ rises by a factor of 56 from $n=1$ to $n=6$);
3. **Schlumberger** with a fixed small potential dipole — efficient sounding of the
   deeper section.

A typical protocol on 31 electrodes measures of order 600–900 configurations,
covering the depth range 5–50 m. Since the array has $\binom{31}{4} = 31\,465$
possible configurations, the protocol is a deliberate choice of under 3 % of them.

**Checks and tolerances.**

- **Contact resistance at every electrode**, measured before acquisition. Reject or
  improve any electrode whose resistance is above a stated value — for example
  5 kΩ on a 100 V transmitter, which costs 27 dB relative to a 200 Ω contact — and
  record every value.
- **Reciprocity on a subset** (a few per cent of the measurements). Tolerance
  $\sqrt{2}\,\delta V/V$: for a typical 2 % voltage noise this is 2.83 %, and it
  should be calculated from the *measured* noise, not quoted as a constant.
- **Repeat one configuration** at the start and end of each day, to detect a
  systematic change (a drying electrode, a temperature effect in the receiver).
- **Record the layout** — electrode positions measured with a tape or a GNSS, the
  line azimuth, the terrain, and the contact resistances.

**Acquisition time.** Each configuration requires the transmitter to switch, the
current to stabilise and the receiver to stack. If a configuration takes 8 s
(including the stacking and the switching), 800 configurations take 6400 s, or
1.8 h of pure acquisition — but with electrode moving, cable checks and access the
realistic field rate is often nearer 2–3 s per configuration of *contact time*, so
the day's productivity is set by the protocol size and the crew's speed, not by the
physics. Doubling the protocol doubles the field time: this is the trade the design
loop must close against the inversion's requirements.

**The assumption that needs a synthetic model.** The relation between the *nominal*
maximum depth (about 0.5 times the largest spacing) and the depth at which the
inversion actually resolves a layer depends on the resistivity structure and on the
error bars. With a conductive layer over a resistive half-space the depth of
investigation is larger than in the reverse case, because the current penetrates
the conductor. The only way to know the resolved depth for this target is to run a
synthetic forward model with the planned protocol and error levels, invert the
synthetic data, and measure how much of the true model is recovered — the standard
resolution test of
[18-08-02 Synthetic Testing, Checkerboards and Recovery Tests](../../../18-inverse-problems/08-practical-inversion-workflow/02-synthetic-testing.md).

---

## ★★★6 — Field quality-control procedure

**Before acquisition, at every electrode.**

| Check | How | Tolerance / action |
|---|---|---|
| Electrode position | Tape or GNSS, recorded in the notebook and in the instrument file | Position error ≤ 1 % of the spacing; re-measure if larger |
| Contact resistance | Instrument's own contact check, per electrode | Record all values; improve any above the stated limit (watering, deeper stake, parallel stakes) |
| Cable continuity and take-out integrity | Continuity check on both current and potential cables | Any open or intermittent take-out replaced before acquisition |
| Ground coupling at the start of the line | One test measurement at a known configuration | Measured $\rho_a$ compared with the previous day's value on the same line |

**During the day.**

| Check | Frequency | Tolerance |
|---|---|---|
| Repeat of one configuration | Start and end of the day | Within the reciprocal tolerance derived from the day's measured noise |
| Reciprocal measurements | A few per cent, spread through the protocol | $\sqrt{2}\,\delta V/V$, derived from the measured voltage noise |
| Contact resistance drift | Every few hundred configurations, or after rain | Re-check any electrode that has changed by more than a factor of 2 |
| Stacked voltage quality | Every configuration (the instrument reports the stack error) | Reject and re-measure configurations above the error limit |
| Current stability | Every configuration | Reject if the current varied during the measurement |

**Acceptance tolerances and their derivation.**

- **Reciprocity**: $\sqrt{2}\,\delta V/V$ with $\delta V/V$ measured, not assumed.
  For a 2 % voltage noise, 2.83 %.
- **Repeat configuration**: the same tolerance, applied to a repeat of the *same*
  configuration, which additionally detects temporal changes (drying, temperature).
- **Contact resistance**: derived from the transmitter's compliance and the
  required signal level; with a 100 V transmitter, a 5 kΩ contact costs 27 dB
  relative to a 200 Ω contact, so 5 kΩ is a reasonable field limit below which
  improvement is not worth the delay.
- **Stack error**: a stated percentage of the measured voltage, above which the
  configuration is re-measured rather than averaged.

**Actions.** A reciprocity failure → stop, check the geometry and the cables for
that configuration, and re-measure; if it persists with the geometry confirmed,
inspect the electrodes involved. A contact above the limit → improve the electrode
before continuing. A repeat-configuration drift → investigate (rain, drying, a
cable being moved by traffic) and, if it cannot be explained, record the change and
process the day's data separately. A stack error above the limit → re-measure
immediately, because a rejected configuration leaves a hole in a depth interval.

**Metadata archived with the data.** The electrode positions (measured, with the
method and the coordinate reference system), the line identification and azimuth,
the array types and the full configuration list, the contact resistance per
electrode, the injected current and measured voltage per configuration with their
errors, the reciprocal and repeat measurements with the computed differences, the
instrument settings (stacking, gain, current waveform), the operator and date, and
the terrain notes. The inversion's error model is derived from these numbers, so a
dataset without them can be inverted but not assessed.
