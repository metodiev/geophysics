# Solutions — 17-08-05 Remote Sensing for Disaster Response

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All values are **SYNTHETIC** teaching numbers.

Lesson: [05 Remote Sensing for Disaster Response](../05-disaster-response-rs.md).

---

## ★1 — Precision, recall, $F_1$

$$
P = \frac{2806}{2806 + 1035} = \frac{2806}{3841} = 0.731,
$$
$$
R = \frac{2806}{2806 + 3} = \frac{2806}{2809} = 0.999,
$$
$$
F_1 = \frac{2 \times 0.731 \times 0.999}{0.731 + 0.999} = 0.844.
$$

---

## ★2 — Latency

$$
\mathbb{E}[\text{days}] = \frac{r}{p} = \frac{6}{0.6} = 10\ \text{days}.
$$

---

## ★3 — What the two errors cost

A *false positive* sends resources to dry ground: wasted effort, and if the
product is used for a pixel-count total, an overestimate. A *false negative*
leaves a flooded area unmapped: a missed rescue, the more serious error in a
response. Precision speaks to the cost of false alarms; recall to the cost of
misses. In a response, recall usually matters more, which is exactly what the
cost-weighted threshold encodes.

---

## ★4 — Cost with $c_{\text{miss}} = 10$, $c_{\text{fa}} = 1$

(i) $10 \times 3 + 1 \times 1035 = 30 + 1035 = 1065$.

(ii) $10 \times 20 + 1 \times 365 = 200 + 365 = 565$.

Choose (ii), the lower cost ($565$): a much lower miss count at the price of
more false alarms is worth it when a miss costs ten times a false alarm.

---

## ★5 — Cost with $c_{\text{miss}} = 100$, $c_{\text{fa}} = 1$

- $(80, 126)$: $100 \times 126 + 80 = 12\,680$.
- $(365, 20)$: $100 \times 20 + 365 = 2\,365$.
- $(1035, 3)$: $100 \times 3 + 1035 = 1\,335$.

The optimum moves to the $(1035, 3)$ operating point — the highest recall
(lowest misses) — because a miss now costs a hundred times a false alarm. The
detector did not change; the *cost structure* did, and the chosen threshold moved
with it. This is why a threshold is uninterpretable without its cost
assumption.

---

## ★6 — False-alarm fraction of the change map

$$
\frac{1329}{4154} = 0.320, \quad\text{i.e. } 32.0\%.
$$

Nearly a third of the flagged pixels are saturated soil, not water. A
pixel-count damage total built from this map would overestimate the affected
area by about a third; the map is usable for *targeting* but not for an
unqualified area statistic.

---

## ★7 — Validating a fresh-event flood map (specification)

- **Reference.** No perfect truth exists, so build the best available: a
  higher-resolution or differently-timed acquisition interpreted by analysts, or
  an independent sensor (optical where cloud permits), with an explicit
  confidence layer.
- **Reference uncertainty.** Treat the reference as fallible: report the
  agreement *and* the reference's own estimated error, and avoid reporting
  precision/recall to more digits than the reference supports.
- **Metric.** Precision and recall (or a cost-weighted score) over stratified
  land covers, since error rates differ between open water, urban and vegetated
  areas; a single global number hides the strata that matter.
- **Timeliness.** State the latency achieved and the decision it informed.
  A validation that ignores latency certifies accuracy but not usefulness.

---

## ★8 — Water beneath emergent vegetation

Emergent vegetation (reeds, mangroves, floating mats) scatters the radar pulse
back to the sensor, so the surface is *not* smooth and the backscatter is high —
indistinguishable from dry vegetated land. The water is physically present but
radiometrically hidden, so the miss is a limit of the measurement geometry, not
of the classifier; no threshold recovers it.

Recovery options include a longer wavelength or cross-polarised channel (which
penetrates or interacts differently with the canopy, so flooded and
non-flooded vegetation differ), an incidence-angle or polarimetric contrast, or
fusing an optical index sensitive to water beneath canopy. Each is a *different
physical measurement*, which is why the fix is a configuration change, not a
better algorithm.
