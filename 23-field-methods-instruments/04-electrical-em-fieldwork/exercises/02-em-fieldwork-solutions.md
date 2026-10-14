# Solutions — 23-04-02 EM Fieldwork: Loop, Coil and Grounded-Source Configurations

> Read after attempting. Lesson:
> [02 EM Fieldwork](../02-em-fieldwork.md). All values are **SYNTHETIC**.

---

## ★1 — Skin depth at 5 kHz

$$\delta = 503.3\sqrt{\frac{\rho}{f}} = 503.3\sqrt{\frac{30}{5000}}
= 503.3\sqrt{0.006} = 503.3 \times 0.077460 = 38.99\ \mathrm{m}.$$

**Frequency for $\delta = 25$ m.** Invert the relation:

$$\sqrt{\frac{\rho}{f}} = \frac{25}{503.3} = 0.049672
\;\Rightarrow\; \frac{\rho}{f} = 0.0024673
\;\Rightarrow\; f = \frac{30}{0.0024673} = 12\,159\ \mathrm{Hz}.$$

So a 30 Ω·m ground requires **about 12.2 kHz** for a 25 m skin depth. Units: $\rho$
in Ω·m, $f$ in Hz, $\delta$ in m. The intermediate
$\sqrt{\rho/f} = 0.04967\ \mathrm{m}$ at the second part, and
$\sqrt{30/5000} = 0.07746$ at the first.

Note the square-root dependence: to halve the skin depth you must *quadruple* the
frequency, which is why high-resolution shallow EMI systems use very high
frequencies and why their depth of exploration saturates quickly.

---

## ★2 — Induction number at 40 m separation

$$\delta(20\ \Omega\,\mathrm{m}, 3\ \mathrm{kHz})
= 503.3\sqrt{\frac{20}{3000}} = 503.3 \times 0.081650 = 41.09\ \mathrm{m}.$$

$$B = \frac{s}{\delta} = \frac{40}{41.09} = 0.973 .$$

**Threshold used:** $B < 0.3$, from the lesson's working rule. Since $0.973 > 0.3$,
the **LIN approximation does not apply** at this geometry and frequency: the
response is non-linear in conductivity, and an apparent conductivity computed with
a LIN calibration would be wrong — by tens of per cent at this induction number, and
in a way that depends on the conductivity itself, so it cannot be corrected by a
single factor.

What to do: reduce the separation (a 20 m pair at 3 kHz gives $B = 0.487$, still
above 0.3), reduce the frequency (at 1 kHz, $B = 0.487/1.732 = 0.281$, inside the
regime), or accept the non-linearity and interpret the data with a full forward
model rather than with a conductivity calibration. The third option is what
mineral-exploration systems do deliberately.

---

## ★★3 — TDEM diffusion times

$$t = \frac{\mu_0 \sigma d^{2}}{2} .$$

With $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H/m}$, $\sigma = 0.2\ \mathrm{S/m}$ and
$d = 300\ \mathrm{m}$:

$$t = \frac{4\pi\times10^{-7} \times 0.2 \times 90\,000}{2}
= \frac{2.26195\times10^{-2}}{2} = 1.1310\times10^{-2}\ \mathrm{s}
= 11.31\ \mathrm{ms}.$$

For $\sigma = 0.05\ \mathrm{S/m}$:

$$t = \frac{4\pi\times10^{-7} \times 0.05 \times 90\,000}{2}
= 2.8274\times10^{-3}\ \mathrm{s} = 2.83\ \mathrm{ms}.$$

**Factor:** the times are proportional to $\sigma$, so the resistive ground needs a
window **four times shorter** (11.31/2.83 = 4.00), and the conductive ground needs
the longer one. The window must extend to at least these times *and* the late
channels must remain above the noise floor; otherwise the sounding is depth-limited.

---

## ★★4 — Coupling distance

Coupling falls as $1/r^{2}$, so a reduction by a factor $F$ in amplitude requires
the distance to increase by $\sqrt{F}$.

Current situation: 15 m, coupling 40 dB above target, i.e. an amplitude ratio of
$10^{40/20} = 100$.

Target: 10 dB above the target signal, i.e. a ratio of $10^{10/20} = 3.162$.

Required additional reduction: $100/3.162 = 31.62$, so the distance must increase by
$\sqrt{31.62} = 5.623$:

$$r_{\text{new}} = 15 \times 5.623 = 84.3\ \mathrm{m}.$$

**Two alternatives to moving.** (i) **Change the time of day**: many cultural
sources (irrigation pumps, industrial load, trains) have a pronounced daily
rhythm, and a survey at a quieter time can gain 10–20 dB without moving; record the
time and the source's operating schedule so the choice is defensible. (ii) **Change
the configuration**: orient the receiver to minimise the intercepted flux, use a
different coil separation or orientation, or — for a TDEM system — use a later
window where the cultural response has decayed faster than the target response.
Note that *stacking does not help* against a coherent interferer: it reduces only
the random part of the noise.

---

## ★★★5 — Design for a 150 m target in 20–100 Ω·m ground

**Method.** A 150 m target in a 20–100 Ω·m ground is a classic **time-domain**
(inductive) target depth. Check the alternatives with the skin depth:

- At 20 Ω·m and 100 Hz, $\delta = 503.3\sqrt{0.2} = 225$ m; at 1 kHz,
  $\delta = 71$ m. So a frequency-domain sounding spanning roughly 100 Hz–10 kHz
  would bridge the target depth, with the low frequencies carrying the deep
  information.
- At 100 Ω·m and 100 Hz, $\delta = 503$ m — the target is well inside the
  diffusive volume even at the low end, so the same frequency range works with
  more sensitivity margin.
- A **grounded-source** configuration (a long wire or a pair of electrodes with
  magnetic and electric receivers) improves the deep signal-to-noise relative to a
  small coil pair, at the cost of requiring ground contact and of a more complex
  geometry to model.

Recommendation: a **grounded-source or large-loop TDEM** survey, with frequencies
interpreted through the time window rather than directly.

**Time window.** With an assumed $\sigma = 0.02\ \mathrm{S/m}$ (50 Ω·m):

$$t = \frac{\mu_0 \sigma d^{2}}{2}
= \frac{4\pi\times10^{-7} \times 0.02 \times 22\,500}{2}
= 2.83\times10^{-4}\ \mathrm{s} = 0.283\ \mathrm{ms}$$

for 150 m. For the conductive end of the range ($\sigma = 0.05\ \mathrm{S/m}$,
20 Ω·m) the same depth takes 0.707 ms. So the window must extend to **at least
0.7 ms**, and in practice several times that, so that the late channels sample the
half-space below the target and the sounder can distinguish the target from it. A
practical window of 0.05–20 ms covers it with margin.

**Geometry.** For a large loop, the depth of exploration scales with the loop
side length: a 100 m × 100 m loop reaches of order 100–200 m with adequate signal,
so the loop is sized for the target rather than the target for the loop. For a
coil pair, the depth-of-exploration conventions of Section 4 give
$s \approx d/1.5 \approx 100$ m for the horizontal coplanar orientation — a large
separation with a correspondingly weak signal, which is why the loop or grounded
source is preferred at this depth.

**Stacking budget.** Require the *latest* channel to be above the noise. If the
late-time signal-to-noise at a single stack is 0 dB and the required detection is
10 dB, the required number of stacks is

$$N = 10^{10/5} = 100 \quad (\text{since the amplitude gain is } \sqrt{N}),$$

i.e. **about 100 stacks**, which at 1 s per stack is under two minutes per
sounding — acceptable, and the number should be verified by watching the stack
error rather than assumed.

**Coupling distances.** From ★★4's arithmetic, use the survey's own source map:
distances of order 100 m from power lines, pipelines and railways, with the actual
coupling measured at a test site before the survey rather than assumed.

**The quantity to measure first.** The **site resistivity**, because every depth
scale depends on it: the skin depth as $\sqrt{\rho}$, the diffusion time as
$\sigma = 1/\rho$. Measure it with a small ERT or a short TEM sounding at one or two
representative sites before designing the loop size and the window; an order of
magnitude error in $\rho$ is a factor of 10 in the diffusion time and a factor of
3 in the skin depth, which is the difference between a design that works and one
that is depth-limited.

---

## ★★★6 — Verifying the LIN regime in the field

**Measurement.** Two or three measurements at the same site with the same
instrument but *different coil separations* (where the system allows it), or the
same separation at different frequencies. The physical quantity (the ground
conductivity) is unchanged, so any variation in the reported apparent conductivity
is a measure of the departure from linearity.

**Analysis.** Compute the ratio of the apparent conductivities measured at the two
geometries, and the induction number for each from
$B = s/\delta$ using the *reported* conductivity for $\delta$. If the reported
conductivities agree within the instrument's repeatability, the measurements are in
the linear regime at both geometries; if they differ systematically with $B$, the
system is outside it at the larger $B$.

**Metric.** The ratio $\sigma_a(s_1)/\sigma_a(s_2)$ (dimensionless) against the
ratio $B_1/B_2$, together with the instrument's own repeatability in the same units
(for example, if the repeatability is 1 % and the measured ratio is 1.15, the
non-linearity is 15 % — 15 times the repeatability, and not explainable by noise).

**Number of sites.** At least **three** sites spanning the conductivity range
expected in the survey, each with two geometries: three is the minimum that
distinguishes a systematic trend with $B$ from a site-specific anomaly, and the
conductivity range is what matters, because $B$ depends on both $s$ and
$\delta \propto \sqrt{\rho}$.

**Why the test is conservative.** It compares two measurements on *different*
geometries, so it also includes any genuine lateral variation between the two
measurement positions: a real conductivity change with position mimics a
non-linearity, and therefore the test over-reports non-linearity rather than
under-reporting it. A test that shows linearity is therefore good evidence, and a
test that shows a difference needs the two geometries to be co-located (nested
coils, or a repeat at the same station) before the non-linearity is blamed.
