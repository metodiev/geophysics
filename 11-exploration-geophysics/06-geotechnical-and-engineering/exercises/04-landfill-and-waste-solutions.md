# Solutions — 11-06-04 Landfill, Waste and Brownfield Site Assessment

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand.

Lesson: [04 Landfill, Waste and Brownfield Site Assessment](../04-landfill-and-waste.md).

---

## ★1 — Normalisation and the uniform half-space

$$ \sigma_a = \int_0^{\infty}\sigma(z)\,K(z)\,\mathrm{d}z,
\qquad \int_0^{\infty}K(z)\,\mathrm{d}z = 1. $$

If $\sigma(z) = \sigma_0$ for all $z$, then

$$ \sigma_a = \sigma_0\int_0^{\infty}K(z)\,\mathrm{d}z = \sigma_0 \times 1
= \sigma_0.\qquad\checkmark $$

This is why the LIN apparent conductivity is *calibrated*: it returns the true
conductivity for uniform ground and a weighted average otherwise.

---

## ★2 — Conductances

**(a):** $S = 0.04 \times 12 = 0.48\ \mathrm{S}$.
**(b):** $S = 0.16 \times 3 = 0.48\ \mathrm{S}$.

They are identical. A 12 m plume at weakly elevated conductivity and a 3 m seam
at high conductivity are the same measurement to a system whose window is wider
than 3 m. The 3 m case is more likely to be a concentrated leachate channel and
the 12 m case a diffuse plume, but the conductance alone does not say which —
only the product is measured. A narrow-window system (see the lesson's table) or a
second method (ERT, which can resolve the depth of the top) is needed.

---

## ★3 — Magnetic anomaly

$$ B_z = 2\times10^{-7}\frac{m}{z^{3}}: $$

$$ z = 2\ \mathrm{m}: B_z = 2\times10^{-7}\frac{100}{8} = 2.5\times10^{-6}\ \mathrm{T}
= 2500\ \mathrm{nT}, $$
$$ z = 4\ \mathrm{m}: B_z = 2\times10^{-7}\frac{100}{64} = 3.125\times10^{-7}\ \mathrm{T}
= 312.5\ \mathrm{nT}. $$

A factor of 8 between 2 m and 4 m: the $z^{-3}$ dipole falloff.

---

## ★4 — Which model gives the larger reading?

**(a) Kernel peaking at 2.5 m.** The peak sits inside B (2 to 4.5 m) and mostly
*above* A (2 to 12 m). B's weight fraction in the kernel is larger than A's, so
**B gives the larger $\sigma_a$** — which is exactly what the lesson's table
shows for the 6 m peak (B larger by 91%): the system responds to *where* the
conductivity sits, not just how much conductance there is.

**(b) Kernel peaking at 15 m.** The window spans both models almost uniformly, so
both weight fractions approach the same value and **the two readings converge**
(2.5% apart in the lesson's table). Only the conductance $S$ is resolved.

The difference is the width of the kernel relative to the layer: a narrow window
resolves the layer's top; a broad window resolves only its conductance.

---

## ★5 — Posterior and false-discovery rate

$$ \mathrm{PPV} = \frac{p\,\mathrm{TPR}}{p\,\mathrm{TPR}+(1-p)\mathrm{FPR}}
= \frac{0.05(0.90)}{0.05(0.90)+0.95(0.50)}
= \frac{0.045}{0.045+0.475} = 0.0865. $$

$$ \mathrm{FDR} = 1-0.0865 = 0.9135. $$

Of 40 flagged anomalies, $40 \times 0.0865 = 3.5$, i.e. about **3 to 4** are
expected to be real contamination and about 36 to 37 are natural conductors. At
this prior the anomaly flag carries very little information, and the correct
action is to raise the prior (site history) or add a cheaper discriminator before
investigating.

---

## ★6 — Cap thickness in a DC sounding

With $\rho_1 = 150$, $\rho_2 = 5\ \Omega\,\mathrm{m}$, $AB/2 = 20\ \mathrm{m}$:

| Cap thickness (m) | $\rho_a$ at $AB/2 = 20$ m ($\Omega$m) |
|---|---|
| 1 | 5.04 |
| 3 | 5.69 |
| 8 | 45.59 |

The thickness information lives in the **intermediate** part of the curve: with a
1 m cap the array at 20 m already sees the conductive waste ($\rho_a \approx 5$,
the waste value); with an 8 m cap the same array is still inside the resistive
cap ($\rho_a \approx 46$, well above the waste value). At $AB/2 = 50$ m all three
have converged ($5.01$, $5.06$, $5.95\ \Omega\,\mathrm{m}$) because the current
reaches the waste regardless.

**Practical rule.** Use the *spacing range* in which the curve is transition —
roughly one to a few times the cap thickness — to constrain the cap; at much
larger spacing only the deep conductor is seen, and at much smaller spacing only
the cap resistivity.

---

## ★7 — Two-method survey for an unengineered waste site (specification)

| Question | Method | Expected contrast | False-negative mode |
|---|---|---|---|
| (i) Waste boundary | EM (FDEM) conductivity mapping, lines 20-25 m apart | Made ground and waste usually more conductive than natural soil | A **dry, inert** waste (rubble, plastic) has little or no conductivity contrast: the boundary is then invisible to EM |
| (ii) Depth to the base | ERT, plus GPR where the ground is resistive and shallow | Conductivity and dielectric contrasts at the base | A conductive *natural* substrate beneath the waste (clay) is indistinguishable from a conductive waste base by conductivity alone |
| (iii) Leachate presence | SP (flow) and ERT (conductance), with a shallow soil-gas or water sample at the top-ranked targets | Conductive plume, SP from flow | A leachate plume within a conductive waste body produces no *additional* contrast: the plume is hidden inside the anomaly |

**Line spacing.** Chosen so that at least two lines cross the smallest expected
feature; for EM, 20-25 m is typical for reconnaissance and 5-10 m for target
definition. State that a line spacing larger than the target width guarantees
aliasing.

**Decision rule, stated in advance.** Rank all anomalies by conductance (EM) and
plume index (ERT/SP); drill the top-ranked targets in order until the marginal
expected value of the next borehole falls below its cost, using the site-specific
prior. Report the rank, the admitted ranges and the expected hit rate — not a
single map with "contamination" written on it.

---

## ★8 — An empirical POD test

**Design.** Flag a *pre-specified* set of anomalies at a threshold fixed before
the data are analysed, and excavate a **random sample** of them — including a
sample of *non-flagged* locations (the crucial control). At each excavated
location record whether waste/contamination was present. Then

$$ \widehat{\mathrm{POD}} = \frac{\text{flagged locations with contamination}}
{\text{random sample of locations with contamination}}, $$

estimating the numerator and denominator from the two samples separately.

**Avoiding circularity.** (i) The threshold must be fixed on the basis of a
physics-based detection model (as in the lesson), not tuned to the excavation
results; (ii) the random non-flagged sample must be genuinely random over the
whole site, not chosen near anomalies; (iii) the sampling density must be
independent of the survey's own output, or the estimate measures the survey's
opinion of itself.

**Effect on a clearance-style claim.** A measured POD replaces the assumed one in
$\mathrm{POD}^{n}$, and the site-specific object density $n$ replaces the
assumed one. If the measured POD is lower than assumed — the usual outcome, because
detection models are optimistic at the tails — the residual probability of an
undetected feature rises sharply and the clearance claim must be weakened. The
report should carry both the *measured* POD and the *assumed* density with their
sample sizes and confidence intervals, so a reviewer can recompute
$\mathrm{POD}^{n}$ with their own numbers.

---

## Worked mastery checkpoint

**(a) Shallow or deep body?** The observed anomaly is $0.12\
\mathrm{S\,m^{-1}}$ over a $0.03\ \mathrm{S\,m^{-1}}$ background, a contrast of
$0.09\ \mathrm{S\,m^{-1}}$. If the body's conductivity is $0.30\
\mathrm{S\,m^{-1}}$ (contrast $0.27$), the required kernel fraction is

$$ f = \frac{0.09}{0.27} = 0.33. $$

Comparing with the demonstration's fraction table ($0.905$ for a top at 0.5 m,
$0.380$ at 1.5 m, $0.020$ at 3 m), a fraction of 0.33 corresponds to a body whose
top is **near 1.5 m** — shallower, not deeper, than the 3 m case. What would
change the answer: the body's true conductivity. A deeper body with a *higher*
conductivity (or a thicker one) produces the same reading, which is precisely the
amplitude-versus-depth ambiguity the lesson derives.

**(b) Depth from the $1500\ \mathrm{nT}$ anomaly.**

$$ \text{drum } (m = 200\ \mathrm{A\,m^{2}}): \quad
z^{3} = \frac{2\times10^{-7}(200)}{1500\times10^{-9}} = 26.67
\;\Longrightarrow\; z = 2.99\ \mathrm{m}, $$
$$ \text{soil } (m = 5\ \mathrm{A\,m^{2}}): \quad
z^{3} = \frac{2\times10^{-7}(5)}{1500\times10^{-9}} = 0.667
\;\Longrightarrow\; z = 0.87\ \mathrm{m}. $$

Both are consistent with the measurement. On a brownfield with made ground, a
shallow magnetised soil or slag feature at $\approx0.9\ \mathrm{m}$ is at least
as plausible as a drum at 3 m — and the two require different responses. The
discriminator is the **shape of the anomaly over a grid**: a compact dipole
produces a tight, symmetric anomaly, while a distributed magnetic body produces a
broad one.

**(c) Posterior.**

$$ \mathrm{PPV} = \frac{0.12(0.85)}{0.12(0.85)+0.88(0.35)}
= \frac{0.102}{0.102+0.308} = 0.249. $$

**(d) The measurement that settles (c):** a piezometer with pore-water
sampling (and, for the magnetic anomaly, a targeted excavation or a
downhole magnetometer). Conductivity correlates with contamination; a chemical
analysis establishes or refutes it. The geophysics cannot, because many natural
materials are as conductive as the target.
