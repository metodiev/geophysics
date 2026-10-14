# Solutions — 08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase

> **Read after attempting the exercises.** The lesson is
> [02 Magnetotellurics](../02-magnetotellurics.md).

---

## ★1 — The half-space impedance

$$\omega = \frac{2\pi}{20} = 0.31416\ \mathrm{rad\,s^{-1}}, \qquad
\omega\mu_0 = 0.31416\times1.256637\times10^{-6} = 3.9478\times10^{-7},$$

$$\left|Z\right| = \sqrt{\omega\mu_0\rho}
= \sqrt{3.9478\times10^{-7}\times50} = \sqrt{1.9739\times10^{-5}}
= 4.443\times10^{-3}\ \Omega,$$

$$\rho_a = \frac{\left|Z\right|^{2}}{\omega\mu_0}
= \frac{1.9739\times10^{-5}}{3.9478\times10^{-7}} = 50.0\ \Omega\mathrm{m}, \qquad
\phi = 45.000^\circ .$$

The half-space returns its own resistivity at every period, and the phase is
exactly $45^\circ$ — the demonstration's check, reproduced by hand.

---

## ★2 — The direction of the phase departure

The phase is **below** $45^\circ$, because resistivity increases with depth: the
currents in the resistive basement are weaker than they would be in a uniform
medium, the impedance becomes more inductive in the sense of a decreasing phase,
and the response moves towards the resistive limit. The rule:
$\phi < 45^\circ$ means conductivity **decreasing** with depth;
$\phi > 45^\circ$ means conductivity increasing with depth.

---

## ★3 — The skew

$$Z_{xx}+Z_{yy} = \left(3-1\right)+\left(2-1\right)i = 2+i, \qquad
\left|Z_{xx}+Z_{yy}\right| = \sqrt{5} = 2.236,$$
$$Z_{xy}-Z_{yx} = \left(40+20\right)+\left(30+15\right)i = 60+45i, \qquad
\left|Z_{xy}-Z_{yx}\right| = 75.0,$$
$$\text{skew} = \frac{2.236}{75.0} = 0.0298 .$$

A skew of 0.03 is small. With $\left|Z_{xx}+Z_{yy}\right|$ not exactly zero, the
data are not exactly 2-D, but the departure is of the order of the noise of a
good site: the structure is consistent with 2-D, and a 1-D interpretation would
be rejected by the inequality of $\rho_{xy}$ and $\rho_{yx}$
($\rho_{xy}/\rho_{yx} = \left|60+45i\right|^{2}/\left|20+15i\right|^{2} =
5625/625 = 9$, a factor of 9 in apparent resistivity — strongly 2-D).

---

## ★4 — A factor of 2.5

$$\rho_a^{\text{obs}} = s^{2}\rho_a^{\text{true}} = 6.25\,\rho_a^{\text{true}},
\qquad \phi^{\text{obs}} = \phi^{\text{true}} .$$

The apparent resistivity is multiplied by 6.25 and the phase is untouched. Note
the practical consequence: a station whose true structure is $100\ \Omega$m can
report $625\ \Omega$m and look entirely reasonable, with a phase curve that is
perfectly consistent with a *deeper* or *more resistive* structure other than the
real one.

---

## ★5 — An invariant that passes through zero

$\left|Z_{xy}+Z_{yx}\right|$ is invariant in *magnitude*: its value is the same at
every rotation, and it happens to be the amplitude of a complex quantity that
rotates through zero. At $45^\circ$ from strike the two off-diagonal elements
become equal in magnitude and opposite in sign, so their sum vanishes while their
difference is unchanged:

$$\left|Z_{xy}\right| = \left|Z_{yx}\right| \quad\text{and}\quad
Z_{xy} \approx -Z_{yx} \quad\text{at }45^\circ .$$

At that rotation the tensor looks like a 1-D tensor in its off-diagonal elements,
which is why a *1-D test that looks only at whether $Z_{xy} = -Z_{yx}$* can be
fooled: the diagnostic must be the **rotation-invariant** quantities
$\left|Z_{xy}\pm Z_{yx}\right|$ (or equivalently the Mohr-circle parameters), not
the appearance at one orientation.

---

## ★6 — Strike recovery

The minimum of $\left|Z_{xx}\right|^{2}+\left|Z_{yy}\right|^{2}$ occurs at a
rotation of $40^\circ$ (or $-40^\circ$, depending on the sign convention of the
rotation matrix), which returns the tensor to strike coordinates. The
**ambiguity**: a 2-D tensor is unchanged in its $\left|Z_{xx}\right|$,
$\left|Z_{yy}\right|$ structure by a $90^\circ$ rotation combined with a sign
change of the off-diagonal elements, so the strike is determined only up to
$90^\circ$; and because a rotation by $\theta$ and by $-\theta$ both zero the
diagonal to first order, the *sign* is also ambiguous. A tensor cannot distinguish
a strike from its perpendicular, and this is a property of the data, not of the
estimator.

---

## ★★7 — Dimensionality experiment (specification)

**Quantities.** The full four-component impedance tensor and the two tipper
components at each site, plus the phase tensor if a 3-D assessment is wanted.

**Period range.** Two decades centred on the periods that sample the target depth
range, chosen from $\delta = \sqrt{\rho T/(\pi\mu_0)}$; if the target is 10 km
deep in $100\ \Omega$m rock, that is periods around $10$–$300$ s.

**Geometry.** An L-shaped or grid array of 5–10 sites within a few tens of
kilometres: enough to distinguish a coherent strike direction from the effects of
one anomalous body, and to estimate the tipper over a baseline comparable to the
skin depth.

**Decision rule.**

| Observation | Conclusion |
|---|---|
| $\rho_{xy} = \rho_{yx}$, skew $\approx 0$, tipper $\approx 0$ at all sites | 1-D (or at least interpretable as 1-D at this location) |
| $\rho_{xy} \ne \rho_{yx}$, skew $\approx 0$, coherent strike direction across the array, tipper perpendicular to it | 2-D, strike known |
| Non-zero skew, incoherent strike between sites, tipper varying with position | 3-D; a 2-D inversion must be justified, not assumed |

**Where it misleads.** A 2-D structure sampled at a site on or near its own axis
of symmetry can give a small skew and a tipper that vanishes, and a *superposition
of two* 2-D structures with different strikes can mimic 3-D. The remedy is
redundancy: several sites, several periods, and a check that the inferred strike
is stable in both.

---

## ★★8 — Why the phase is invariant

Write $Z = \left|Z\right|e^{i\phi}$. Then

$$Z_{\text{obs}} = sZ = s\left|Z\right|e^{i\phi}
\ \Longrightarrow\ \arg Z_{\text{obs}} = \arg s + \phi .$$

For **real, positive** $s$, $\arg s = 0$, so the phase is exactly unchanged, while
$\left|Z_{\text{obs}}\right| = s\left|Z\right|$ and
$\rho_a^{\text{obs}} = s^{2}\rho_a$. For **complex** $s = \left|s\right|e^{i\psi}$
the phase is shifted by $\psi$ as well: a phase-rotating distortion is *not*
removable by a static-shift parameter, it changes the phase curve, and
distinguishing it from structure is a genuinely harder problem (it is the subject
of galvanic-distortion decomposition, which requires assumptions about the
distortion's frequency independence and dimensionality).
