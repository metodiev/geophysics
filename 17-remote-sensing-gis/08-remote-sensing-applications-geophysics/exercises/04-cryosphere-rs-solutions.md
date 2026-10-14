# Solutions — 17-08-04 Cryosphere Remote Sensing: Ice, Snow and Permafrost

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All values are **SYNTHETIC** teaching numbers.

Lesson: [04 Cryosphere Remote Sensing](../04-cryosphere-rs.md).

---

## ★1 — Albedo

$$
\alpha(200) = 0.99 - 0.22\left(1 - e^{-200/250}\right)
= 0.99 - 0.22(1 - 0.4493) = 0.869,
$$
$$
\alpha(1000) = 0.99 - 0.22\left(1 - e^{-4}\right)
= 0.99 - 0.22(0.9817) = 0.774.
$$

Difference: $0.869 - 0.774 = 0.095$.

---

## ★2 — Speed

Displacement $= 4 \times 15\ \mathrm{m} = 60\ \mathrm{m}$ over $24$ days.

$$
v = \frac{60}{24} \times 365.25 = 2.5 \times 365.25 = 913.1\ \mathrm{m\,yr^{-1}}.
$$

---

## ★3 — Signs of the snow-depth bias

(i) Saturation: the signal grows sub-linearly, so the fixed-coefficient retrieval
**underestimates** depth (negative bias). (ii) Forest: the canopy attenuates the
signal, so the retrieval **underestimates** depth (negative bias). Both are
negative and therefore confusable.

---

## ★4 — Saturated and forested depth

No forest:

$$
\Delta T_B = 6.0\left(1 - e^{-60/45}\right) = 6.0(1 - 0.2636) = 4.418\ \mathrm{K},
$$
$$
\mathrm{SD}_{\text{ret}} = 7.5 \times 4.418 = 33.1\ \mathrm{cm},
\qquad \text{bias} = 33.1 - 60 = -26.9\ \mathrm{cm}.
$$

With forest fraction $0.25$ the signal is scaled by $(1 - 0.6 \times 0.25) = 0.85$:

$$
\Delta T_B = 4.418 \times 0.85 = 3.756\ \mathrm{K}, \qquad
\mathrm{SD}_{\text{ret}} = 7.5 \times 3.756 = 28.2\ \mathrm{cm},
$$

an additional bias of $-5.0\ \mathrm{cm}$ (total $-31.8\ \mathrm{cm}$). The two
model errors act in the same direction.

---

## ★5 — Uncertainty on the speed

$$
\delta v = \frac{0.5 \times 15}{24} \times 365.25 = 0.3125 \times 365.25
= 114.1\ \mathrm{m\,yr^{-1}}.
$$

As a percentage: $114.1 / 913.1 = 12.5\%$. The measurement is exact for the
displacement it finds; the *resolution* of the image sets the uncertainty floor.

---

## ★6 — Seasonal versus secular

Total secular displacement over five years: $1.0 \times 5 = 5.0\ \mathrm{cm}$.
The seasonal amplitude is $5.00\ \mathrm{cm}$ — equal to the *entire* secular
signal, and its peak-to-peak swing is $10\ \mathrm{cm}$. A single displacement
map records the surface at one instant; an $8\ \mathrm{cm}$ drop could be
mid-thaw or mid-freeze, so it cannot be attributed to settlement. Only fitting a
seasonal term and a trend together (or differencing maps at the same season)
separates the two.

---

## ★7 — Velocity validation (specification)

- **Reference.** Independent positions from a repeated survey (GNSS on the ice,
  or a higher-resolution image pair) at a stated set of points.
- **Matching.** Compare the product velocity averaged over the feature-tracking
  patch footprint and interval to the reference over the same interval; do not
  compare instantaneous to averaged.
- **Metric.** Bias and RMSD of the velocity vector, and the *angle* difference,
  which often matters more than magnitude for flow-line studies.
- **Physical mismatch.** Glacier flow is not rigid translation: it accelerates,
  shears and rotates, so a patch that deforms between the two images produces a
  genuine mismatch that is not measurement error. The design must sample
  sufficiently short intervals that the deformation across a patch is small.

---

## ★8 — Why wet snow destroys the retrieval

The passive-microwave depth signal arises from **volume scattering** of the
snowpack at microwave wavelengths: dry snow scatters, so the difference between
two frequencies grows with depth. When liquid water appears (melt onset), water
strongly absorbs microwaves, extinguishing the volume scattering and making the
snowpack emit nearly as a blackbody at a single temperature. The
brightness-temperature *difference* collapses toward zero regardless of depth,
so the retrieval returns a near-zero depth — which looks exactly like "no snow".
A careful product flags melt (often from a diurnal or cross-polarised signal),
suspends the depth retrieval during melt, and reports depth as undefined rather
than as a small number.
