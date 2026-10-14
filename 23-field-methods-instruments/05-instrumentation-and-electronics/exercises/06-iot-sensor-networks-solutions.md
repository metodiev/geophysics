# Solutions — 23-05-06 IoT and Autonomous Sensor Networks for Earth Monitoring

The lesson is [06 IoT and Autonomous Sensor Networks](../06-iot-sensor-networks.md). All
values are **SYNTHETIC**.

## ★1

$$\text{rate} = 50 \times 1 \times 2 = 100\ \mathrm{B/s} = 0.8\ \mathrm{kbit/s},$$

$$\text{per node per day} = 100 \times 86\,400 = 8.64\ \mathrm{MB},$$

$$12 \times 90 \times 8.64\ \mathrm{MB} = 9331.2\ \mathrm{MB} = 9.33\ \mathrm{GB} .$$

The whole campaign is 9.33 GB — under two minutes of the raw three-component stream of
the lesson, and a reminder that the *volume* is rarely the problem.

## ★2

$$\text{airtime} = \frac{8.64 \times 10^{6} \times 8}{25\,000}
= 2764.8\ \mathrm{s/day} = 46.08\ \mathrm{min/day} = 3.20\ \% \text{ of the day},$$

$$\text{allowed at 1 \%} = 864\ \mathrm{s/day}
\;\Rightarrow\; \text{shortfall} = \frac{2764.8}{864} = 3.20\times ,$$

$$\text{deliverable} = \frac{864 \times 25\,000}{8} = 2.70\ \mathrm{MB/day} .$$

So even this modest node needs 3.2× more airtime than the limit allows. The lesson's
options apply in order: store and collect, or trigger and buffer, or decimate — and the
comparison that matters is between **46 minutes per day of radio** and a visit once per
quarter.

## ★3

$\tau = 1$ s, $w = 4$ s, so $P = \min(1, 5/\Delta)$:

| Wake interval | $P$ | Acquisition duty |
|---|---|---|
| 600 s | 0.0083 | 0.0067 |
| 120 s | 0.0417 | 0.0333 |
| 30 s | 0.1667 | 0.1333 |

For $P = 0.80$: $\Delta = 5/0.80 = 6.25$ s, i.e. a duty cycle of $4/6.25 = 0.64$, or
**64 %**. That is the same tension as in the lesson, and it is a proportional one: the
detection probability per unit of acquisition duty is
$(P/\text{duty}) = (\tau + w)/w = 1 + \tau/w$, so both shortening the wake interval and
lengthening the window cost duty, and the only genuinely free parameter is $\tau$,
which the physics sets. The cheap-and-honest alternative is to report the $P$ you
actually achieve.

## ★4

$$L_{\text{allowed}} = 10 + 0 + 0 - (-110) = 120\ \mathrm{dB} .$$

Free space at 868 MHz ($20\log_{10}(868\times10^{6}) = 178.77$ dB):

$$\log_{10} d = \frac{120 - 178.77 + 147.55}{20} = 4.439
\;\Rightarrow\; d = 27\,480\ \mathrm{m} = 27.5\ \mathrm{km} .$$

Empirical, $L(d) = 60 + 10(3.5)\log_{10}(d/10)$:

$$d = 10 \times 10^{(120-60)/35} = 10 \times 51.8 = 518\ \mathrm{m}
\quad\text{(no margin)},$$

$$d = 10 \times 10^{(100-60)/35} = 10 \times 13.9 = 139\ \mathrm{m}
\quad\text{(20 dB margin)} .$$

The 20 dB margin costs a factor of **3.73** in range, exactly as in the lesson, because
$10^{20/35} = 3.73$. Two things to carry into a field plan: the empirical range is 53×
smaller than the free-space one, and the number to plan with is the margined one,
because a link that works only in dry weather is a link that does not work.

## ★5

Independent failures, $X \sim \mathrm{Bin}(20, 0.9)$:

$$P(X \ge 16) = \sum_{k=16}^{20}\binom{20}{k}0.9^{k}0.1^{20-k} = 0.9568 .$$

With the common-cause branch, $q = 0.05$ removes four nodes and leaves
$\mathrm{Bin}(16, 0.9)$:

$$P(X_{16} \ge 12) = 0.9830 ,$$

$$P = 0.95(0.9568) + 0.05(0.9830) = 0.90896 + 0.04915 = 0.9581 .$$

So the common-cause event moves availability from 0.9568 to 0.9581 — **0.13 percentage
points** — because the four nodes of slack absorb it. The honest reading is not that
common causes are harmless but that **slack is what buys tolerance to them**: with the
demand raised to 18 nodes the independent figure is 0.6769 and the correlated figure is
$0.95(0.6769) + 0.05(0.7892) = 0.6825$, and the same absolute stress now matters far
more in a campaign, because there is no spare capacity to absorb it.

For a campaign the statement to make is therefore about **margin, not the point
estimate**: "the array meets its minimum count with 96 % probability under independent
failures, and the design keeps four nodes of slack so that a shared fault costing four
nodes does not breach it" is defensible; "availability is 96 %" alone is not.

## ★6

A model answer.

**Volumes.** Rate $= 100 \times 3 \times 4 = 1200$ B/s $= 9.6$ kbit/s. Per node per day
$= 103.68$ MB. Over 40 nodes and 120 days (4 months):

$$40 \times 120 \times 103.68\ \mathrm{MB} = 497.7\ \mathrm{GB} \text{ raw},$$

$$\frac{497.7}{3} = 165.9\ \mathrm{GB} \text{ at 3:1 lossless compression} .$$

**Airtime.** At 50 kbit/s effective the raw stream needs 16 589 s/day per node; the 1 %
limit allows 864 s/day, a shortfall of 19.2×. Even the compressed stream needs
$16\,589/3 = 5530$ s/day, i.e. 6.4× the limit — compression alone does not solve it.

**Options, and the choice.**

| Option | Cost | Science preserved |
|---|---|---|
| store and collect | one visit per node | all of it |
| trigger and buffer | firmware, airtime on events | all of it locally, summaries in near-real-time |
| decimate | agreed change of band or rate | only the decimated band continuously |
| change the medium | licensed link or wired gateways | all of it |

**The choice is trigger and buffer plus store and collect**: the full-rate waveform is
kept locally and collected at the single visit, while a daily report carries the health
telemetry and a triggered summary. This is the only option that both satisfies the 1 %
duty limit and preserves the raw data, and it requires no change to the science.

**Detection probability.** With a 2 s event and a 5 s window it is
$P = 7/\Delta$; at a 30 s wake interval $P = 0.233$, at 10 s $P = 0.70$. I would
configure a 10 s wake interval inside the triggered mode ($P = 0.70$, duty 0.50) *only*
while armed, and state $P = 0.70$ for randomly timed events in the methods section, with
the local continuous recording of the full stream as the device that makes the duty
figures honest.

**Health telemetry** in every report: battery voltage, internal temperature, clock offset
against the discipline reference, samples written, samples rejected, clipped-sample count,
trigger count, free storage, and a heartbeat with the firmware version.

**What the plan cannot deliver.** No real-time waveform (latency of one visit for raw
data), no guaranteed detection (70 % of randomly timed events, not 100 %), no absolute
timing without a discipline source at each node, and no protection against a common-cause
fault in the shared firmware — which is why the reports carry the firmware version and why
the firmware must be validated on a subset of nodes before the whole array is updated.
