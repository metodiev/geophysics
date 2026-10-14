# Solutions — 17-08-01 Mineral and Alteration Mapping from Space

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> All values are **SYNTHETIC** teaching numbers.

Lesson: [01 Mineral and Alteration Mapping from Space](../01-mineral-mapping-rs.md).

---

## ★1 — Continuum and band depth

$$
R_{\text{cont}}(2.20) = 0.50 + (0.55 - 0.50)\frac{2.20 - 2.10}{2.40 - 2.10}
= 0.50 + 0.05 \times \frac{0.10}{0.30} = 0.51667.
$$

$$
\mathrm{BD} = 1 - \frac{0.42}{0.51667} = 1 - 0.8129 = 0.1871.
$$

---

## ★2 — Endmember and constraints

An endmember is a pure reference spectrum of a single surface component. In a
linear mixture model the abundances must satisfy **non-negativity** ($a_i \ge 0$)
and **sum-to-one** ($\sum_i a_i = 1$).

---

## ★3 — Continuum removal

It divides the spectrum by a smooth background (the continuum), normalising it to
a flat continuum at one so that absorption features can be measured as depths
independent of the overall brightness. It does **not** remove an atmospheric
error that is *curved*: a linear error is absorbed by the continuum, a curved
one is not.

---

## ★4 — Interpolating the degeneracy

Between $(0.18, 1.39)$ and $(0.25, 1.00)$ the grain factor falls with abundance
at a rate

$$
\frac{1.00 - 1.39}{0.25 - 0.18} = \frac{-0.39}{0.07} = -5.571\ \text{per unit } a.
$$

At $a = 0.20$:

$$
g \approx 1.39 + (-5.571)(0.20 - 0.18) = 1.39 - 0.111 = 1.28.
$$

So $a = 0.20, g \approx 1.28$ reproduces the same depth of $0.0724$ as
$a = 0.25, g = 1.00$. A map reporting only the depth cannot tell these apart.

---

## ★5 — Conditioning and RMSE

Condition-number ratio: $130.2 / 53.6 = 2.43$.

RMSE ratio (component 1): $0.0229 / 0.0087 = 2.63$.

The RMSE grows a little faster than the condition number. Conditioning limits the
*amplification* of input error and sets the order of magnitude; the residual gap
is the usual difference between a worst-case bound ($\kappa$) and the realised
error for a particular noise realisation and geometry. The conclusion — nearly
collinear endmembers make the abundance error several times worse on identical
data — stands, and the library must always be reported with its conditioning.

---

## ★6 — False apparent abundance

$$
a_{\text{apparent}} = \frac{0.0288}{0.30} = 0.096 \approx 10\%.
$$

The controlling quantity is the **ratio** of the artefact's curvature to the
reference depth: the artefact biases the depth by an amount proportional to its
amplitude, and the mapping to abundance divides by the reference depth. So a
$10\%$ curvature on a spectrum whose real feature is $0.30$ deep appears as a
$10\%$ abundance anomaly. The lesson is that the *false positive rate* of a
mineral map depends on the ratio of the atmospheric curvature to the target's
own feature depth — a number the map never reports.

---

## ★7 — Breaking the degeneracy with a second feature (specification)

- **Data.** Reflectance over a spectral range containing at least two absorption
  features of the *same* mineral whose relative depths respond differently to
  grain size (grain growth deepens all features, but the ratio of depths at two
  wavelengths also depends on grain size and on the mineral).
- **Model.** Fit a radiative-transfer or Hapke-type mixing model with abundance
  and grain size as free parameters, using both features simultaneously.
- **Separating quantity.** The **ratio of the two band depths** changes with
  grain size but is nearly fixed by mineralogy, so it can pin the grain size and
  free the abundance.
- **Failure mode.** If the two features are close enough that the same grain-size
  change moves both in proportion, the ratio is degenerate again and the two
  causes remain entangled; the design must choose spectrally *separated*
  features.

---

## ★8 — Shape versus depth

Continuum removal divides by a **straight line** between two shoulders, so any
error that is itself a straight line (a constant slope) is divided out exactly
and leaves the depth unchanged — that is why the *linear* error cancels. A curve
is not a straight line, so it survives the division and appears as a distortion
of the feature. To distinguish a real absorption from a curved artefact, use the
**shape**: an artefact tends to vary smoothly and slowly across the spectrum and
is shared among the shoulders, whereas a mineral absorption is centred at a
characteristic wavelength and affects the local shape (symmetry, width,
shoulder slopes). Fitting a parametric absorption model (centre, width, depth)
and checking whether the shoulders themselves are distorted separates a real
feature (shoulders clean) from a curved artefact (shoulders distorted).
