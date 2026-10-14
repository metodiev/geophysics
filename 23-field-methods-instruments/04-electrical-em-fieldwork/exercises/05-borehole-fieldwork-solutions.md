# Solutions — 23-04-05 Borehole Logging Operations and Tool Calibration

> Read after attempting. Lesson:
> [05 Borehole Logging](../05-borehole-fieldwork.md). All values are
> **SYNTHETIC**.

---

## ★1 — Stretch of a 750 N tool at 3000 m

$$A = 12\ \mathrm{mm^2} = 1.2\times10^{-5}\ \mathrm{m^2},$$

$$\Delta L = \frac{WL}{AE} = \frac{750 \times 3000}{1.2\times10^{-5}
\times 1.1\times10^{11}} = \frac{2.25\times10^{6}}{1.32\times10^{6}}
= 1.7045\ \mathrm{m}.$$

In sampling intervals of 0.05 m:

$$\frac{1.7045}{0.05} = 34.1 \text{ intervals}.$$

So the tool is 1.70 m deeper than the cable payout indicates, or 34 depth samples
— more than the thickness of the thin beds the log is meant to resolve. The
correction is systematic and computable, but only if the tool weight, cable section
and depth are recorded. Note that the cable's own weight adds a term of order
$wL^{2}/(2AE)$; with a 0.5 kg/m cable ($w \approx 4.9$ N/m) that term is
$4.9 \times 9\times10^{6}/(2 \times 1.32\times10^{6}) = 16.7$ m — which dominates
the tool's own weight! This is why real depth corrections use the *tension at the
surface* logged by the winch rather than a nominal tool weight: the cable's own
weight is the larger term and it is measured directly.

---

## ★2 — A 0.15 m bed with a 0.60 m detector

$$R_{\text{peak}} = \frac{b}{L} = \frac{0.15}{0.60} = 0.250,$$

apparent thickness $= L = 0.60$ m.

**Which carries the information.** The **amplitude** (the peak response) is
proportional to the true thickness, so the thickness is recovered as
$b = R_{\text{peak}} \times L$ *if* the bed's contrast with its surroundings is
known. The **apparent thickness** is the detector length for every thin bed and
carries no information about the bed at all. The practical procedure is therefore:
quantify the bed by its amplitude, quote the detector length, and treat the
apparent extent as a constant of the tool. A deconvolution can separate two closely
spaced thin beds whose combined response differs from that of one thicker bed, but
with a single bed and no independent constraint the thickness–amplitude ambiguity is
irreducible.

---

## ★★3 — Logging speed and rig time

$$v_{\text{log}} = \Delta z \times f_s = 0.02 \times 50 = 1.00\ \mathrm{m/s}
= 3600\ \mathrm{m/h}.$$

$$\text{time for 1500 m} = \frac{1500}{1.00} = 1500\ \mathrm{s}
= 25.0\ \mathrm{min}.$$

Add the rig time outside the logging interval — rigging up and down, tool changes,
the calibration, and the repeats — which for a single tool is typically comparable
to the logging time itself and for a multi-tool programme dominates it. The
engineering question is whether the 0.02 m sampling is justified: if the tools have
0.15–0.60 m detectors, sampling at 0.02 m records the same information five to
thirty times more often. The rule is to sample at about a quarter of the shortest
detector length — 0.04–0.15 m here — which would halve or third the logging time.

---

## ★★4 — Two-point calibration

$$g = \frac{45.0 - 5.0}{4500 - 500} = \frac{40.0}{4000} = 0.010000
\ \text{value units per count},$$

$$o = 5.0 - 0.010000 \times 500 = 0.0000\ \text{value units},$$

$$V(2000) = 0.010000 \times 2000 + 0.0000 = 20.0 \ \text{value units}.$$

Check: $V(500) = 5.0$ ✔, $V(4500) = 45.0$ ✔.

**What it assumes.** Linearity between the two points, and (implicitly) that the two
reference values are exact. Neither is guaranteed: a detector whose response
saturates at high count rates is non-linear in the middle of its range and the
two-point calibration cannot see it, and a reference value known to ±2 % makes the
gain uncertain by about ±3 % (the two errors combining in quadrature). A third
reference point is what tests the linearity assumption, and the uncertainty of the
references is what the log's scale uncertainty should be quoted from.

---

## ★★5 — Depth-shift significance

$$\mathrm{se}(\text{shift}) = \frac{s}{\sqrt{n}} = \frac{0.12}{\sqrt{15}}
= \frac{0.12}{3.8730} = 0.030984\ \mathrm{m} \approx 0.031\ \mathrm{m}.$$

**Significance of a 0.25 m shift:**

$$\frac{0.25}{0.031} = 8.07 \text{ standard errors}.$$

So a 0.25 m shift is highly significant — far beyond three standard errors
(0.093 m) — and cannot be explained by picking scatter: it is a real depth
difference between the runs (a stretch difference, a different tool, or a different
logging direction). Conversely, a reported shift of 0.05 m would be
$1.6$ standard errors, indistinguishable from zero at the three-sigma level, and
should be reported as "no significant shift" rather than applied as a correction.

---

## ★★★6 — A logging programme for a 1200 m well with 0.3 m pay zones

**Tool order.** Run the tools in the order that puts the *largest* tool first and the
highest-resolution tools last, because each run may leave the hole in a slightly
different state and the high-resolution data are the most sensitive to it:

1. **Natural gamma** — cheap, robust, high resolution (a scintillation detector of
   0.1–0.3 m), and the workhorse for correlation. Run first and last, so the two
   passes give the depth-matching markers for every other tool.
2. **Resistivity** — the deepest-reading tool and the least sensitive to near-borehole
   conditions; it also anchors the formation evaluation.
3. **Density** — the shallowest-reading petrophysical tool; run after the others so
   that mud-cake and invasion effects are as they will be.
4. **Sonic** — the highest-resolution and the most sensitive to tool centralisation;
   run last, slowly, with centralisers, and repeat a section.

**Logging speeds from the detector lengths.** Take the detector lengths as
0.20 m (gamma), 0.60 m (density), 1.00 m (sonic) and 0.50 m (resistivity array).
Sampling at a quarter of the shortest detector gives, per tool:

| Tool | Detector (m) | Sampling (m) | Speed at 20 samples/s (m/h) | Time for 1200 m (min) |
|---|---|---|---|---|
| gamma | 0.20 | 0.05 | 3600 | 20.0 |
| resistivity | 0.50 | 0.125 | 9000 | 8.0 |
| density | 0.60 | 0.15 | 10 800 | 6.7 |
| sonic | 1.00 | 0.25 | 18 000 | 4.0 |

Total logging time ≈ 39 minutes; with rig-up, tool changes, calibration and repeats
budget **4–6 hours** of rig time. The arithmetic of the speeds is
$v = \Delta z \cdot f_s$ and the time is $L/v$.

**Depth control.** (i) Log **up** for all tools, with the gamma run repeated down
and up to measure the direction-dependent stretch. (ii) Record the cable tension at
the winch continuously, and compute the elastic stretch
$\Delta L = \int T(z)\,\mathrm{d}z/(AE)$ using the *logged* tension rather than a
nominal tool weight. (iii) Match the runs using casing collars and the gamma
shoulder beds, fitting a single shift per run (Section 6 of the lesson) and
reporting the residual scatter. (iv) Verify against the drill-string depth of any
core or test data.

**Calibration.** Each tool calibrated against its reference: gamma against a
calibration facility or a portable source, density against an aluminium-and-water
jig, sonic against a known travel-time standard, resistivity against a test
resistor. Record for each: the reference, its stated uncertainty, the date, the
temperature, and the before-and-after readings so that drift during the run is
visible.

**Repeat checks.** A repeat of at least 50 m in each run, at the same speed and
direction, compared interval by interval; and a repeat of one full pass at the end
of the programme to detect a change in hole conditions. Report the repeat difference
per curve in physical units, not as a percentage.

**Two limitations the programme cannot remove.**

1. **The vertical resolution limit set by the detectors.** Thin pay zones of 0.3 m
   logged with a 0.6 m density detector are seen as amplitude anomalies of the
   detector's width, and their thickness is recoverable only through the known
   contrast — the detector length cannot be undone. The programme should therefore
   include an independent constraint on bed thickness (core, image logs, or a
   high-resolution tool).
2. **Borehole and invasion effects.** The near-borehole region is altered by
   drilling, and the shallow-reading tools measure the altered rock; no calibration
   and no depth control can remove it. The mitigation is to run the shallow tools as
   late as possible (so the invasion has stabilised), to record the drilling and
   mud history, and to interpret with an invasion model — and to state the
   remaining uncertainty.
