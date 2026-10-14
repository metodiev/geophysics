# Solutions — 23-07-02 Case Study: An ERT Survey from Design to Report

The lesson is [02 Case Study: An ERT Survey](../02-case-study-ert-survey.md). All values are
**SYNTHETIC**.

## ★1

$$L_{\max} \ge 5 \times 30 = 150\ \mathrm{m} .$$

For 48 electrodes at 4 m:

$$\text{line} = 47 \times 4 = 188\ \mathrm{m}, \qquad
L_{\max} = 188\ \mathrm{m}, \qquad
\text{DOI} = \frac{188}{5} = 37.6\ \mathrm{m} .$$

So the line reaches **37.6 m**, 25 % deeper than the 30 m target — an acceptable margin, bought
by 38 m of extra line and four extra electrodes. If the line were shortened to reach exactly
30 m (150 m, i.e. about 38 electrodes at 4 m), one lost electrode would put the target at the
very edge of the model, which is why a margin of 20–30 % on the depth is the practical design
rule. Note also that the *lateral sampling* is 4 m here: the body must be wider than that to
be resolved.

## ★2

$$\binom{32}{4} = 35\,960 \text{ possible configurations},$$

and the skip-1 α/β/γ protocol with $n = 1\ldots10$ has $3(32-3n)$ configurations per level, so

$$N = 3\sum_{n=1}^{10}(32 - 3n) = 3\left(10 \times 32 - 3\frac{10 \times 11}{2}\right)
= 3(320 - 165) = 465 .$$

465/35 960 = 1.29 % of the space. Note the limit on $n$: the count $32-3n$ must stay positive,
so $n \le 10$ for a 32-electrode spread — the maximum skip level *and* the deepest reachable
level are set by the electrode count, exactly as in the demonstration.

## ★3

$$I = \frac{V_{\text{tx}}}{2R_c + R_{\text{ground}}} = \frac{200}{2(3000) + 1000}
= \frac{200}{7000} = 0.028571\ \mathrm{A} = 28.571\ \mathrm{mA},$$

$$V_{\text{pair}} = I\frac{\rho}{2\pi a}
= 0.028571 \times \frac{30}{2\pi \times 20} = 0.028571 \times 0.238732
= 6.8209\ \mathrm{mV},$$

$$\mathrm{SNR} = \frac{6.8209}{0.3} = 22.74 .$$

The signal-to-noise is comfortable at this configuration, but two things change along the
line: at the *largest* spread ($a$ three times larger) the transfer resistance falls by 3× and
the SNR with it, to about 7.6; and at the *smallest* spread it is that much better. So the
binding configuration is the deepest one, and the design should quote its SNR rather than the
mid-line value.

Which to change first: **the contacts**. Raising the transmitter voltage from 200 V to 400 V
doubles the SNR (a factor 2 for a hardware change and no extra field time); halving the
contact resistance from 3 kΩ to 1.5 kΩ raises the current from 28.571 mA to 50.0 mA, a factor
1.75, at the cost of better electrodes (water, bentonite, deeper rods). Stacking multiplies
the SNR only as $\sqrt{N}$ while costing time linearly, so it is the last resort — and the
contact improvement *also* reduces the risk of a level failing outright.

## ★4

$$\text{5 stacks}: \quad 2000 \times 5 \times 0.5\ \mathrm{s} = 5000\ \mathrm{s}
= 83.3\ \mathrm{min}, \qquad \text{noise factor } \frac{1}{\sqrt{5}} = 0.4472,$$

$$\text{20 stacks}: \quad 2000 \times 20 \times 0.5 = 20\,000\ \mathrm{s}
= 333.3\ \mathrm{min} = 5.6\ \mathrm{h}, \qquad \frac{1}{\sqrt{20}} = 0.2236 .$$

So four times the time buys a further factor of 2 — the same exchange rate as in the lesson,
and the reason the stack count is set by a *tolerance* (the inversion's error model and the
2× contrast requirement) rather than by "as many as possible". At 5.6 h of acquisition plus
electrode moves, the 20-stack survey is a two-day line; the 5-stack survey is most of one day.

## ★5

| Mesh cells | Data | Cells/data | Status | What the resolution claim can say |
|---|---|---|---|---|
| 200 | 2 000 | 0.10 | over-determined | each cell is constrained; resolution is set by the sensitivity pattern |
| 2 000 | 2 000 | 1.00 | at the limit | the inversion is exactly determined only with regularization; treat the claim as optimistic |
| 20 000 | 2 000 | 10.00 | under-determined | the mesh's smoothing *is* the resolution; a sharp interface claim is not supportable |

The practical rule that follows: **choose the mesh from the data count and the geometry, then
report the resolution as a property of that mesh** — for example by inverting a synthetic
model of the same mesh and reporting how well the target feature is recovered. A resolution
claim that does not state the mesh, the regularization and the error model is not a claim
about the ground.

## ★6

A model answer.

**Configuration.** For a 15 m target: $L_{\max} \ge 5 \times 15 = 75$ m, with a 25 % margin
$L_{\max} \approx 95$ m. A **64-electrode line at 2.5 m spacing gives a 157.5 m line** — twice
the requirement, and 2.5 m lateral sampling, which resolves a 10 m body comfortably (about four
samples across it). If the line must be 200 m, use 80 electrodes at 2.5 m (197.5 m) or 64 at
3 m (189 m). The electrode spacing is chosen from the *width* of the target (10 m), not from
the depth: 2.5 m sampling gives four independent samples across the body, which is the
conventional minimum for resolving a bounded body with an inversion.

**Protocol and data count.** Skip-1 α/β/γ with $n = 1\ldots15$ (the spread limit for a
64-electrode line with 2.5 m spacing), plus a few gradient arrays for near-surface coverage:
about 1 800 configurations, of which a 1 200-measurement subset is acquired. Recompute the
counts explicitly for the chosen electrode count and spacing, as in the demonstration's table,
and report the deepest level's count — that number, not the total, bounds the resolution at the
target depth.

**Contact requirement.** Specify a **contact resistance ≤ 2 kΩ per electrode** and verify it
during the electrode installation with a resistance check, because it is the term that limits
the deepest levels' signal. With a 200 V transmitter, 2 kΩ contacts and $R_{\text{ground}}
\approx 1$ kΩ, the current is about 40 mA, and at the largest $a$ (≈ 75 m) with
$\rho = 30$ Ω·m the pair voltage is $I\rho/2\pi a \approx 2.5\ \mathrm{mV}$ — against a 0.3 mV
noise level an SNR of about 8, which is the number to quote.

**Stacking and field time.** With the deepest level at SNR 8 and the requirement being a 2×
contrast detection, a factor 2 improvement is enough in the mean, so **8 stacks** (a factor
$\sqrt{8} = 2.83$ for the noise, at 0.4 s per stack = 3.2 s per measurement, i.e. 1200 × 3.2 =
64 min of acquisition) is the specification, with a check that the reciprocal error is below
1 %. One line is then about one day including electrode moves.

**Mesh and error model.** Mesh cells from the data count: 1 200 data with a 2.5 m spacing over
157 m suggests a model of about 1 500–2 500 cells (comparable to the data count), further
constrained by smoothness regularization; the error model is
$\varepsilon = 0.005\lvert V\rvert + 0.2$ mV, which the reciprocal measurements verify. The
*resolution demonstration* is an inversion of a synthetic model containing the expected target,
showing what fraction of the true contrast is recovered — that, not the picture, is the
resolution claim.

**Repeatability for time-lapse.** The requirement is that the *difference* between two surveys
resolve the change, so the repeatability must be stated per configuration, not per model: fix
the electrode positions permanently (buried and surveyed, markers left in place), the
acquisition protocol and the stack count; and require that the repeated measurements at a
fixed subset of configurations (say 10 % of the protocol, measured twice within each survey)
agree to better than 1 %. A 2× contrast change at the target is then detectable if the model's
cell-level uncertainty from the difference is under ~10 % of the background value — which the
resolution demonstration in the previous paragraph quantifies.

**What cannot be established.**

1. **The absolute resistivity of the plume, or its chemistry.** ERT measures a bulk
   resistivity, which depends on the pore fluid, the clay content and the porosity together;
   without borehole or laboratory control (see
   [23-06-04 Laboratory Resistivity, IP and Dielectric Measurements](../../06-laboratory-measurements/04-electrical-lab-measurements.md))
   the number cannot be converted into a concentration. The deliverable is a *resistivity
   distribution and its change*, and the interpretation must be calibrated by an independent
   measurement.
2. **The 3-D shape of the body from a single line.** A 2-D inversion of a line over a compact
   3-D body images a smeared, enlarged body, and its apparent lateral extent depends on the
   profile geometry rather than on the plume — a second crossing line or a 3-D survey is the
   only way to bound it.
