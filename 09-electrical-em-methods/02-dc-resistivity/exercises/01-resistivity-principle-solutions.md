# Solutions — 09-02-01 Resistivity Principle and the Four-Electrode Arrangement

> **Read after attempting the exercises.** Lesson:
> [01 Resistivity Principle and the Four-Electrode Arrangement](../01-resistivity-principle.md).

---

## ★1 — Point-source potential

$$V = \frac{\rho I}{2\pi r} = \frac{75\times0.2}{2\pi\times3}
= \frac{15}{18.8496} = 0.7958\ \mathrm{V}.$$

---

## ★2 — Wenner geometric factor

General formula with $r_{AM} = a$, $r_{AN} = 2a$, $r_{BM} = 2a$, $r_{BN} = a$:

$$k = \frac{2\pi}{\frac{1}{a}-\frac{1}{2a}-\frac{1}{2a}+\frac{1}{a}}
= \frac{2\pi}{1/a} = 2\pi a = 2\pi\times10 = 62.832\ \mathrm{m}.$$

---

## ★3 — Apparent resistivity

$$\rho_a = \frac{k\,\Delta V}{I} = \frac{62.832\times0.5}{0.2}
= 157.08\ \Omega\,\mathrm{m}.$$

Units: $\mathrm{m}\times\mathrm{V}/\mathrm{A} = \mathrm{m}\times\Omega
= \Omega\,\mathrm{m}$. ✔

---

## ★4 — Dipole-dipole

$r_{AM} = (n+1)a = 30$ m, $r_{AN} = 40$ m, $r_{BM} = 20$ m, $r_{BN} = 30$ m:

$$\frac{1}{k} = \frac{1}{2\pi}\left(\frac{1}{30}-\frac{1}{40}-\frac{1}{20}
+\frac{1}{30}\right) = \frac{1}{2\pi}(0.033333-0.025-0.05+0.033333)
= \frac{-0.008333}{6.2832},$$

$$k = -753.98\ \mathrm{m}, \qquad |k| = 753.98\ \mathrm{m}.$$

Over a half-space, $\Delta V = \rho I/|k| = 200\times0.5/753.98
= 0.1326\ \mathrm{V}$.

---

## ★5 — Positioning error

Uniform half-space: over a half-space $\rho_a$ is independent of geometry, so a
2 cm error changes the *reading* by 0.17% (for an inner electrode at $a = 20$ m:
$0.01/20 = 0.05\%$ per centimetre, so about 0.1% for 2 cm), but if the geometry
is measured and used honestly the error is **zero** — as the demonstration
prints ($99.750349$ vs $100.000000$ when the *nominal* geometry is used and
$100.000000$ when the true positions are used).

Layered ground: the response is *not* scale-invariant, so a geometric error is a
real error. At 0.26% per centimetre on an inner electrode, $\pm2$ cm gives
$\pm0.52\%$ in $\rho_a$ — five times what the same error would cost over a
half-space. The difference is the whole point: **over a uniform ground only the
geometry matters and it is self-consistent; over a varying ground the shape of
the sensitivity *function* matters too, and a misplaced electrode samples the
wrong part of it.**

---

## ★6 — Two electrodes

$$R_\text{geo} = \frac{60}{2\pi}\left(\frac{2}{0.04}\right)
= 9.5493\times50 = 477.46\ \Omega,$$

$$R_\text{measured} = 477.46 + 600 = 1077.46\ \Omega.$$

Apparent resistivity: the geometry implies $R = \rho/(2\pi)\times(2/a)$, so

$$\rho_\text{app} = \frac{R_\text{measured}\,2\pi a}{2}
= \frac{1077.46\times2\pi\times0.04}{2} = 135.4\ \Omega\,\mathrm{m}$$

against $60\ \Omega\,\mathrm{m}$: a factor **2.26**.

---

## ★7 — Reciprocity

The formula is symmetric in the pair
$(A,B)\leftrightarrow(M,N)$ because
$\Delta V_{MN}$ is a sum of four terms
$r_{ij}^{-1}$ with signs
$(+1,-1,-1,+1)$ that are unchanged when the two pairs are exchanged — the
mathematical statement that the matrix of $1/r$ terms is symmetric:

$$\left(\frac{1}{r_{AM}}-\frac{1}{r_{AN}}-\frac{1}{r_{BM}}
+\frac{1}{r_{BN}}\right)$$

is invariant under $A\leftrightarrow M$, $B\leftrightarrow N$. Physically, this
follows from the **self-adjointness of the conductivity operator**: for
$\nabla\cdot(\sigma\nabla u) = -I(\delta_A-\delta_B)$, the bilinear form
$\int\sigma\nabla u_1\cdot\nabla u_2$ is symmetric, which is Green's second
identity applied to the two source distributions.

A model that violates reciprocity is one with a non-symmetric constitutive
relation — for instance a *non-reciprocal* coupling such as a Hall effect
(magnetic field breaking time-reversal symmetry). In ordinary DC resistivity
there is no magnetic field in the constitutive law, so reciprocity is exact; a
solver that breaks it has a bug, not a physical effect.

---

## ★8 — Reducing geometric error

1. **Record every position to the best available accuracy** with an
   independent method (total station, RTK GNSS, or a tapeline between surveyed
   pegs) rather than a walking wheel along a curved line.
2. **Measure the array geometry thermally**: resistivity varies with expansion
   of the cable, and a tape drawn taut in one weather and slack in another gives
   different spacings. Record the measured value, not the nominal one.
3. **Use the measured positions in $k$**, and additionally **fit the positions**
   as nuisance parameters in the inversion: with many measurements and few
   positions, the geometry can be estimated from the data
   ($\pm$ a well-posedness analysis).
4. **Prefer array geometries whose sensitivity is least sensitive to position**:
   over a layered ground the outer electrodes matter less (0.13–0.17% per cm)
   than the inner ones (0.26–0.31%). A Schlumberger-style layout with the
   potential pair well inside the current pair inherits the second, worse,
   sensitivity — so place the potential pair accurately even though its spacing
   is small.
5. **Post-processing:** recompute $\rho_a$ with measured positions, and inflate
   the data errors by the geometric uncertainty
   $\partial\rho_a/\partial x \cdot \delta x$ so that the inversion does not
   treat a known geometric uncertainty as a data error.
