# Exercises — 05-02-04 Reduction of Observations to Anomalies

Difficulty: ★ · ★★ · ★★★. Use $G = 6.67430\times10^{-11}$ m³kg⁻¹s⁻²,
$R = 6378137$ m, $g = 9.8$ m/s².

---

## ★ Foundational

**★1.** Derive $dg/dh = -2g/R$ from $g = GM/r^2$ and evaluate it in mGal/m with
the stated constants. State why $M$ is not needed.

**★2.** Derive $g_\text{slab} = 2\pi G\rho t$ for an infinite slab and state its
assumptions.

**★3.** For a station 12 m above the datum, state the sign and magnitude of
(a) the free-air correction and (b) the Bouguer correction with
$\rho_B = 2400$ kg/m³.

**★4.** List the reductions in the order applied and say what each removes.

---

## ★★ Applied

**★★5.** A station sits 40 m above the datum in terrain with $\rho_B = 2670$
kg/m³. Compute both corrections in mGal and their ratio. Compare the ratio with
$\rho_B/(3\bar\rho_E)$ for $\bar\rho_E = 5515$ kg/m³.

**★★6.** A Bouguer anomaly of 15.0 mGal is computed with $\rho_B = 2400$
kg/m³. The same data are reprocessed with $\rho_B = 2670$ kg/m³ and the anomaly
becomes 15.42 mGal. Using the slab formula, verify this shift for 40 m of
relief.

**★★7.** A gravity survey covers 0.7° of latitude. Estimate the change in the
normal field across it, given that the latitude effect on $g$ is dominated by
the centrifugal term. Compute $\omega^2 R\sin 2\varphi$ per degree at
$\varphi = 45°$ with $\omega = 7.292115\times10^{-5}$ rad/s, and state whether
it can be ignored for a 0.1 mGal target.

**★★8.** Terrain corrections are omitted in hilly ground. State the sign of the
error and explain why the omission usually biases Bouguer anomalies negatively
near valleys.

---

## ★★★ Research-oriented

**★★★9.** Implement the full reduction chain on synthetic data: build a model
with a known target anomaly, a known relief, a known Bouguer density, and a
stated regional field; generate "observed" readings; apply every reduction; and
report the residual against truth. Then (a) misuse the Bouguer density by 10%
and report the resulting bias; (b) omit terrain correction in a synthetic valley
and report the error; (c) report which single step contributes the largest
uncertainty. All inputs labelled measured/derived/assumed.

**★★★10.** Nettleton method. Given two synthetic profiles over the same
geology at different elevations, grid-search the Bouguer density that minimises
the correlation between the Bouguer anomaly and topography. Report the recovered
density, the width of the minimum, and the range of densities consistent with
the data. State the method's assumptions and one situation in which it fails.
