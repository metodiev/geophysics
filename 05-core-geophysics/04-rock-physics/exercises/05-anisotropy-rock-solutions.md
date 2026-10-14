# Solutions — 05-04-05 Anisotropy in Rocks: Causes and Magnitudes

> Numbers marked *verified* were computed.

---

## ★1

Intrinsic (crystallographic or grain-shape alignment; shales). Structural (fine
layering of isotropic beds; thin-bedded sequences, via Backus averaging).
Stress-induced (aligned cracks opened by the stress field; fractured
reservoirs).

---

## ★2

$\varepsilon = (C_{11}-C_{33})/(2C_{33})$;
$\gamma = (C_{66}-C_{44})/(2C_{44})$;
$\delta = [(C_{13}+C_{44})^2-(C_{33}-C_{44})^2]/[2C_{33}(C_{33}-C_{44})]$.
All dimensionless.

---

## ★3

$V_p(90°)/V_p(0)-1 = \sqrt{1+2\varepsilon}-1$ and
$V_s(90°)/V_s(0)-1 = \sqrt{1+2\gamma}-1$. They check that the Thomsen
parameterisation is consistent with the axial velocities obtained from an
independent Christoffel eigen-solution — a benchmark for the implementation.

---

## ★★4 *(verified)*

$V_p(0) = \sqrt{55\times10^{9}/2500} = \sqrt{2.2\times10^{7}} = 4690.4$ m/s.
$V_p(90°) = \sqrt{66\times10^{9}/2500} = \sqrt{2.64\times10^{7}} = 5138.1$ m/s.
$\varepsilon = (66-55)/(2\cdot55) = 0.1000$.
$\sqrt{1+2\varepsilon}-1 = \sqrt{1.2}-1 = 0.095445$;
$5138.1/4690.4-1 = 0.095445$. ✓

---

## ★★5 *(verified)*

$\gamma = (23-20)/(2\cdot20) = 0.0750$. SH anisotropy
$= \sqrt{1+2\gamma}-1 = \sqrt{1.15}-1 = 0.072381$, i.e. 7.24%.

---

## ★★6

At $\theta = 45°$: $s^2 = c^2 = 0.5$, $sc = 0.5$. The matrix elements are
$\Gamma_{11} = 0.5(C_{11}+C_{44}) = 0.5(86) = 43$ GPa,
$\Gamma_{22} = 0.5(C_{66}+C_{44}) = 0.5(43) = 21.5$ GPa,
$\Gamma_{33} = 0.5(C_{44}+C_{33}) = 0.5(75) = 37.5$ GPa,
$\Gamma_{13} = 0.5(C_{13}+C_{44}) = 0.5(38) = 19$ GPa.

The 2×2 block in (1,3) has eigenvalues
$\frac{43+37.5}{2}\pm\sqrt{\left(\frac{43-37.5}{2}\right)^2+19^2}
= 40.25\pm\sqrt{7.5625+361} = 40.25\pm19.196$, giving 59.446 and 21.054 GPa.
Dividing by $\rho = 2500$ and taking square roots:
quasi-P $= \sqrt{2.3778\times10^{7}} = 4876.3$ m/s;
quasi-SV $= \sqrt{8.4216\times10^{6}} = 2902.0$ m/s;
SH $= \sqrt{21.5\times10^{9}/2500} = \sqrt{8.6\times10^{6}} = 2932.6$ m/s.

Both S velocities exceed $V_s(0) = 2828.4$ m/s, and quasi-P lies between
$V_p(0)$ and $V_p(90°)$.

---

## ★★7

Because the P-velocity depends on $\delta$ through a $\sin^2\theta\cos^2\theta$
term that vanishes at both $\theta = 0$ and $\theta = 90°$ but is maximal near
vertical-to-moderate angles. Depth ties and normal moveout use exactly that
angular range, so they sample $\delta$; axial velocities sample only $C_{33}$
and $C_{11}$, i.e. $\varepsilon$. Hence a model can match both axial velocities
perfectly and still tie depths wrongly.

---

## ★★★8

Backus averages for a two-component stack (fractions $f_1,f_2$):
$C_{33}^\text{eff} = \langle 1/C_{33}\rangle^{-1}$ (harmonic),
$C_{44}^\text{eff} = \langle 1/C_{44}\rangle^{-1}$,
$C_{11}^\text{eff} = \langle C_{11}-C_{13}^2/C_{33}\rangle +
\langle C_{13}/C_{33}\rangle^2/\langle 1/C_{33}\rangle$,
$C_{13}^\text{eff} = \langle C_{13}/C_{33}\rangle/\langle 1/C_{33}\rangle$,
$C_{66}^\text{eff} = \langle C_{66}\rangle$.

Expected: anisotropy grows roughly linearly with the modulus contrast and the
volume fraction of the softer component, and is zero at both limits. Validity
requires the layer thickness to be small compared with the dominant wavelength —
typically less than about a quarter wavelength.

A 5% depth tie error at 4 km depth corresponds to an effective velocity error of
5%, which for a moderate-contrast thin-bedded sequence can be produced by
anisotropy of order 0.05–0.10 — entirely plausible in a shale-prone basin, and
the reason anisotropic depth conversion is standard practice.

---

## ★★★9

From $V_p(0)$, $V_p(90°)$, $V_s(0)$, $V_s(90°)$ one obtains $C_{33}$,
$C_{11}$, $C_{44}$, $C_{66}$ directly. $C_{13}$ (and hence $\delta$) is *not*
determined: it influences velocities only at intermediate angles. Recovering it
requires travel times at non-axial incidence — offsets in a walkaway VSP, or
moveout from surface seismic.

Consequently $\varepsilon$ and $\gamma$ are well determined by axial
measurements, while $\delta$ is not, and any depth conversion that depends on
$\delta$ must state how $\delta$ was obtained (measured, assumed via an
$\varepsilon$–$\delta$ empirical relation, or left as an uncertainty). Reporting
a single $\delta$ without that provenance is the most common anisotropy-related
overstatement in practice.
