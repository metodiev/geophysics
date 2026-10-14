# Solutions — 17-08-03 Soil Moisture Remote Sensing and Its Validation

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All values are **SYNTHETIC** teaching numbers.

Lesson: [03 Soil Moisture Remote Sensing and Its Validation](../03-soil-moisture-rs.md).

---

## ★1 — Direction of the response

Brightness temperature **falls** as moisture rises, because wetter soil has a
higher dielectric constant and therefore a higher reflectivity (lower
emissivity), so it emits less. From the table, $T_B = 245.32\ \mathrm{K}$ at
$m_v = 0.10$ and $T_B = 184.60\ \mathrm{K}$ at $m_v = 0.40$ — a drop of
$60.72\ \mathrm{K}$ for a rise of $0.30\ \mathrm{m^3\,m^{-3}}$.

---

## ★2 — Precision

$$
\sigma_{m_v} = \frac{0.6}{200} = 0.0030\ \mathrm{m^3\,m^{-3}}.
$$

---

## ★3 — Footprint and heterogeneity

The *footprint* is the ground area a retrieval averages (large for a microwave
sounder). *Heterogeneity* is the spatial variance of moisture inside that area.
They matter because the product estimates the footprint mean while a ground probe
measures a point, so the difference between them — heterogeneity, not product
error — appears in every validation statistic.

---

## ★4 — Bias versus precision

$$
\frac{|\text{bias}|}{\text{precision}} = \frac{0.0447}{0.0018} = 24.8.
$$

The retrieval is *precise* to $0.002$ but *biased* by $0.045$, twenty-five times
larger. The claim "accurate to $0.002$" is false: precision describes scatter,
not agreement. With an unmodelled canopy, the correct statement is "scatter
$0.002$, bias up to $0.045$".

---

## ★5 — Slope attenuation

$$
1 - 0.723 = 0.277, \quad\text{i.e. } 27.7\%\ \text{attenuation}.
$$

The effect is **errors-in-variables** attenuation: noise in the predictor
(here, the point reference sampling a heterogeneous footprint) shrinks the fitted
slope toward zero. The product is not over-sensitive; the *comparison* carries
noise that deflates the slope. Reading a sub-unit slope as a product defect is
the error this problem is designed to expose.

---

## ★6 — RMSD budget

$$
\text{RMSD}_{\text{total}} = \sqrt{0.0391^{2} + 0.0018^{2}}
= \sqrt{1.5288\times10^{-3} + 3.24\times10^{-6}} = 0.03914\
\mathrm{m^3\,m^{-3}}.
$$

The heterogeneity term dominates ($0.0391$ against $0.0018$): the comparison, not
the retrieval, consumes the budget.

---

## ★7 — Separating product error from scale mismatch (specification)

- **Reference network.** A dense cluster of probes within each footprint (many
  points) whose *average* estimates the footprint mean, rather than one probe.
- **Up-scaling.** Compute the footprint mean by spatial averaging or by a
  regression/kriging up-scaling calibrated on the cluster.
- **Metric.** Compare the product to the *up-scaled* footprint mean (bias, RMSD,
  slope), and separately report the within-footprint variance as the scale term.
- **Attribution.** If the product matches the up-scaled mean to within its
  retrieval precision, the remaining error is scale, not product. The design
  attributes error by making the reference estimate the *same* spatial quantity
  the product estimates.

---

## ★8 — Point probes and triple collocation

A point probe and a footprint product measure different physical quantities
(point value versus areal mean); their difference includes the sub-footprint
variance, which is a property of the *site*, so a single point cannot certify or
refute the product's accuracy.

**Triple collocation.** With three independent estimates of the same quantity —
a satellite product, a land-surface model, and an in-situ network — each with
uncorrelated errors, the pairwise covariances between them contain enough
information to solve for each estimate's error variance without any of them
being a perfect reference. The requirement is that the three errors are mutually
independent, which is itself an assumption to state and test; its violation
(e.g. the model and product sharing a forcing) invalidates the estimate.
