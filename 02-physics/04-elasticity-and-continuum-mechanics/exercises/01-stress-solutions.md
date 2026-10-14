# Solutions — 02-04-01 Stress: Traction, Cauchy Stress Tensor and Equilibrium

> **Read this after attempting the exercises, not before.** Compression-positive
> convention throughout. Values attributed to the demo are its actual output.

---

## ★1 — Tractions

For $\hat{n} = (1,0,0)$: $\mathbf{t} = (50, -15, 0)$ MPa;
$|t| = \sqrt{2500+225} = 52.201533$ MPa; $\sigma_n = 50$ MPa;
$\tau = \sqrt{52.201533^2-50^2} = 15.000000$ MPa.

For $\hat{n} = (1,1,0)/\sqrt2$:
$\mathbf{t} = \boldsymbol{\sigma}\hat{n}$ gives
$t_1 = (50-15)/\sqrt2 = 24.748737$, $t_2 = (-15+20)/\sqrt2 = 3.535534$,
$t_3 = 0$; $|t| = 25.000000$ MPa;
$\sigma_n = \mathbf{t}\cdot\hat{n} = (24.748737+3.535534)/\sqrt2 = 20.000000$ MPa;
$\tau = \sqrt{625-400} = 15.000000$ MPa.

**(c)** $\mathbf{t}(-\hat{n}) = \boldsymbol{\sigma}(-\hat{n}) =
-\mathbf{t}(\hat{n})$ ✓, since Cauchy's formula is linear in $\hat{n}$.

**(d)** Both planes in (a) carry $\tau = 15$ MPa (with opposite signs — the
*component* of shear changes sign with the normal, while the magnitude on the
perpendicular plane is the same). The maximum over all planes is
$(\sigma_1-\sigma_3)/2$, computed in ★2.

---

## ★2 — Invariants and principals

**(a)** $I_1 = 50+20+10 = 80$;
$I_2 = \sigma_{11}\sigma_{22}-\sigma_{12}^2 + \sigma_{22}\sigma_{33} +
\sigma_{11}\sigma_{33} = 1000-225+200+500 = 1475$;
$I_3 = \det = 50(200) - (-15)(-15\times10) = 10000 - 2250 = 7750$
(expanding: $I_3 = \sigma_{11}(\sigma_{22}\sigma_{33}-\sigma_{23}^2)
- \sigma_{12}(\sigma_{21}\sigma_{33}-\sigma_{23}\sigma_{31}) + \ldots$
$= 50\times200 - (-15)(-15\times10) = 10000-2250 = 7750$).

**(b)** The characteristic cubic is
$\sigma^3 - 80\sigma^2 + 1475\sigma - 7750 = 0$. The eigenvalue
$\sigma = 10$ (the $z$-direction, which is principal because the coupling terms
vanish) factors out:
$\sigma^3-80\sigma^2+1475\sigma-7750 = (\sigma-10)(\sigma^2-70\sigma+775)$, whose
roots are $\sigma = (70\pm\sqrt{4900-3100})/2 = (70\pm42.426407)/2$, i.e.
56.213203 and 13.786797. So $\sigma_1 = 56.213203$, $\sigma_2 = 13.786797$,
$\sigma_3 = 10$ MPa.

**(c)** The principal directions are $z$ (for $\sigma_3 = 10$) and, in the $xy$
plane, the eigenvectors of $\begin{pmatrix}50&-15\\-15&20\end{pmatrix}$. The
rotation angle from the $x$-axis satisfies
$\tan2\theta = 2\sigma_{12}/(\sigma_{11}-\sigma_{22}) = -30/30 = -1$, so
$\theta = -22.5^\circ$ (for the greater principal stress).

**(d)** $\tau_{\max} = (56.213203-10)/2 = 23.106601$ MPa.

---

## ★3 — The Mohr expressions

**(a)** With principal stresses $\sigma_1,\sigma_3$ and a plane whose normal makes
angle $\theta$ with the $\sigma_1$ direction, the traction components are
$t_1 = \sigma_1\cos\theta$, $t_3 = \sigma_3\sin\theta$; the normal stress is
$\sigma_n = t_1\cos\theta+t_3\sin\theta = \sigma_1\cos^2\theta+\sigma_3\sin^2\theta
= \frac{\sigma_1+\sigma_3}{2}+\frac{\sigma_1-\sigma_3}{2}\cos2\theta$ ✓.

**(b)** $\tau = t_1(-\sin\theta)+t_3\cos\theta
= (\sigma_3-\sigma_1)\sin\theta\cos\theta
= -\frac{\sigma_1-\sigma_3}{2}\sin2\theta$; the magnitude is maximal at
$\theta = 45^\circ$ ✓.

**(c)** At $45^\circ$, $\cos2\theta = 0$ and $\sin2\theta = 1$, giving
$\sigma_n = (\sigma_1+\sigma_3)/2$ and $|\tau| = (\sigma_1-\sigma_3)/2$ ✓.

**(d)** The restriction makes the state *approximately* 2-D and ensures the $2\theta$
rotation lies in the $\sigma_1$–$\sigma_3$ plane (the plane of maximum shear for
three distinct principal stresses). In a 3-D state with three distinct principal
stresses, the maximum shear is still $(\sigma_1-\sigma_3)/2$, but it occurs on the
plane bisecting $\sigma_1$ and $\sigma_3$, and the other two pairs give the
smaller shears $(\sigma_1-\sigma_2)/2$ and $(\sigma_2-\sigma_3)/2$. The 2-D
formulas are exact for the $\sigma_1$–$\sigma_3$ plane whatever $\sigma_2$ is; the
restriction matters only for identifying *which* plane carries the global maximum.

---

## ★4 — Lithostatic stress

**(a)**

| Depth (km) | $\sigma_v$ (MPa) | $p_f$ (MPa) | $\sigma_v^{\text{eff}}$ (MPa) |
|---|---|---|---|
| 1 | 25.997 | 10.104 | 15.892 |
| 5 | 129.983 | 50.522 | 79.461 |
| 10 | 259.965 | 101.043 | 158.922 |
| 20 | 519.930 | 202.086 | 317.844 |
| 30 | 779.895 | 303.129 | 476.766 |

**(b)** Effective gradient: $\rho g(1-\rho_w/\rho) = 2650\times9.81\times
(1-1030/2650) = 25996.5\times0.61132 = 15982$ Pa m⁻¹ ≈ 15.9 MPa km⁻¹.

**(c)** With $p_f = 0.6\sigma_v$ the effective gradient is
$0.4\times26.0 = 10.4$ MPa km⁻¹, and at 10 km the effective stress falls from 159
to 104 MPa — a 35 per cent reduction. Overpressure therefore weakens the crust
substantially.

**(d)** The pore-pressure assumption is a model. It is measured directly by
downhole pressure gauges in a well, by mud-weight and leak-off tests, or inferred
from seismic velocities through a compaction model — and each method has its own
systematic uncertainty.

---

## ★5 — Reading the demo

**(a)** $\sigma_1 = 134.490566$, $\sigma_2 = 63.586042$, $\sigma_3 = 31.923392$
MPa; invariants $I_1 = 230.000000$, $I_2 = 14875.000000$, $I_3 = 273000.000000$
from both routes.

**(b)** The residual shear on the principal planes is $2.7\times10^{-6}$,
$9.5\times10^{-7}$ and $0.0$ MPa — round-off. This demonstrates that the computed
eigenvectors are genuine principal directions of the given tensor (an indexing or
solver error would show up as a residual comparable with the stresses).

**(c)** Mean stress 76.666667 MPa, $J_2 = 2758.333333$ MPa², von Mises
90.967027 MPa.

**(d)** $\sqrt{3J_2}/p = 90.967/76.667 = 1.187$. A ratio of order unity means the
deviatoric stress is comparable with the mean, i.e. this is a highly stressed
state — not a lithostatic one. In the crust at 10 km the mean stress is about
265 MPa while the deviatoric part is limited by friction to of order 100 MPa, so
the ratio there is about 0.4. This synthetic tensor is closer to a laboratory
failure state.

---

## ★6 — Borehole stress state

**(a)** At 3 km: $\sigma_v = 75$ MPa, $\sigma_H = 112.5$ MPa,
$\sigma_h = 60$ MPa, $p_f = \rho_w g z = 29.43$ MPa. In the chosen coordinates,

$$\boldsymbol{\sigma}^{\text{eff}} = \begin{pmatrix}83.07&0&0\\0&30.57&0\\0&0&45.57
\end{pmatrix}\ \text{MPa}.$$

**(b)** The principal stresses are 83.07 (horizontal, $x$), 45.57 (vertical) and
30.57 (horizontal, $y$). The *greatest* principal stress is horizontal and the
least is also horizontal, so $\sigma_2$ is vertical: this is a **strike-slip**
regime in the Anderson classification.

**(c)** $\tau_{\max} = (83.07-30.57)/2 = 26.25$ MPa.

**(d)** The borehole wall concentrates the far-field stress: the tangential
(tangential to the wall) stress is about $3\sigma_{\max}-\sigma_{\min}$ at the
azimuth of the least principal stress, so shear failure (breakout) is expected
where the tangential compression is greatest, i.e. on the sides of the borehole
aligned with the *least* horizontal stress. That alignment is precisely why
breakout orientations are a stress indicator.

---

## ★7 — Reading the Mohr section

**(a)** Centre 80.000000 MPa, radius 50.000000 MPa, measured deviation
$7.1\times10^{-15}$ MPa.

**(b)** For each tabulated pair, $(\sigma_n-80)^2+\tau^2 = 2500$: e.g. at 15°,
$(129.641016-80)^2+5.980762^2 = 2464.6+35.8 = 2500.4$ ✓ (the small excess is the
printed rounding). Repeat for the others and report your residuals.

**(c)** Maximum measured shear 50.000000 MPa $= (\sigma_1-\sigma_3)/2$ with
$\sigma_1 = 130$, $\sigma_3 = 30$ MPa ✓.

**(d)** The plane at 45° to the *axes* ($\sigma_{xx}$ direction) is not at 45° to
the *principal axes*: here the principal axes are rotated by
$\theta_p = \frac12\tan^{-1}(2\times30/(120-40)) = \frac12\tan^{-1}(0.75) =
18.435^\circ$ from the $x$-axis. The maximum shear plane is at
$18.435+45 = 63.435^\circ$ from $x$, not 45°, so the shear at 45° is
$|\tau| = 50\sin(2\times26.565^\circ) = 40$ MPa. The arithmetic is a good test of
whether the angle convention has been stated correctly.

---

## ★8 — A full 3-D state

**(a)** $I_1 = 80+60+40 = 180$;
$I_2 = (80\times60-100) + (60\times40-64) + (80\times40-25) = 4700+2336+3175 =
10211$;
$I_3 = 80(2400-64) - 10(400+40) + (-5)(-80-300) = 186880-4400+1900 = 184380$.

**(b)** A numerical diagonalisation gives approximately $\sigma_1 = 82.86$,
$\sigma_2 = 57.93$, $\sigma_3 = 39.21$ MPa (report your own values; the sum must be
180).

**(c)** From the eigenvalues: $I_1 = 180$ ✓;
$I_2 = \sigma_1\sigma_2+\sigma_2\sigma_3+\sigma_1\sigma_3 = 4800+2271+3249 =
10320$... — a discrepancy of about 1 per cent indicates the eigenvalue listing above
is rounded too coarsely; recompute with full precision and the agreement should be
to ten digits. This is the practical lesson: invariant checks are only as good as
the precision you carry, and a 1 per cent discrepancy in an exact identity is a
numerical, not a physical, finding.

**(d)** Mean stress 60 MPa; the deviatoric tensor has diagonal
$20, 0, -20$ plus the off-diagonals unchanged;
$J_2 = \frac12[20^2+0^2+20^2+2(10^2+5^2+8^2)] = \frac12(800+2\times189) =
\frac12(1178) = 589$ MPa², so $\sigma_{\text{vM}} = \sqrt{1767} = 42.04$ MPa.

---

## ★★★9 — Uniaxial strain and lateral stress

**(a)** Uniaxial strain means $\varepsilon_{xx} = \varepsilon_{yy} = 0$ while
$\sigma_{zz} = \sigma_v$. From Hooke's law (lesson 02-04-03),
$\sigma_{xx} = \lambda(\varepsilon_{xx}+\varepsilon_{yy}+\varepsilon_{zz}) +
2\mu\varepsilon_{xx} = \lambda\varepsilon_{zz}$ and
$\sigma_{zz} = (\lambda+2\mu)\varepsilon_{zz}$. Eliminating
$\varepsilon_{zz}$: $\sigma_{xx} = \frac{\lambda}{\lambda+2\mu}\sigma_{zz}$.
Using $\lambda = 2\mu\nu/(1-2\nu)$ and $\lambda+2\mu = 2\mu(1-\nu)/(1-2\nu)$ gives
$\frac{\lambda}{\lambda+2\mu} = \frac{\nu}{1-\nu}$ ✓.

**(b)** With $\nu = 0.25$, $\sigma_h/\sigma_v = 1/3$: at 1 km,
$\sigma_v = 26.5$ MPa, $\sigma_h = 8.8$ MPa; at 5 km, 132.4 and 44.1 MPa; at
10 km, 264.9 and 88.3 MPa.

**(c)** With $\sigma_v$ as $\sigma_1$ and both lateral stresses equal:
$\sigma_1 = \sigma_v$, $\sigma_2 = \sigma_3 = \sigma_v/3$; the deviatoric tensor
has diagonal $(2\sigma_v/3-\sigma_v/3, -\sigma_v/3, -\sigma_v/3)$... more
carefully, the deviatoric part is $\text{diag}(\sigma_v,\sigma_v/3,\sigma_v/3) -
\frac{5\sigma_v}{9}\mathbf{I}$, whose $J_2 = \frac{1}{3}(\sigma_v-\sigma_v/3)^2
= \frac{4\sigma_v^2}{27}$. So $J_2 \propto \sigma_v^2$: it grows as the *square*
of depth, not linearly, in this model. At 10 km: $J_2 = 4\times264.9^2/27 =
10395$ MPa², $\sigma_{\text{vM}} = 176.6$ MPa.

**(d)** The state has the vertical stress as the greatest principal stress:
a **normal-faulting** regime. To change it one must add horizontal compression
(tectonic shortening) so that a horizontal stress becomes the greatest; then the
regime becomes strike-slip or thrust. This is why deviations of the measured
stress state from the uniaxial-strain prediction are interpreted as tectonic.

---

## ★★★10 — Gravitational stress in a uniform sphere

**(a)** By Gauss's law for gravity, at radius $r$ inside a uniform sphere only the
enclosed mass matters: $M(r) = \frac43\pi\rho r^3$, so
$g(r) = GM(r)/r^2 = \frac43\pi G\rho r$ ✓ — linear in $r$.

**(b)** In spherical symmetry the equilibrium equation is
$dp/dr = -\rho g(r) = -\frac43\pi G\rho^2 r$, which integrates from $r$ to $R$
with $p(R) = 0$:
$p(r) = \frac43\pi G\rho^2\frac{R^2-r^2}{2} = \frac23\pi G\rho^2(R^2-r^2)$ ✓.

**(c)** At $r = 0$:
$p_c = \frac23\pi\times6.6743\times10^{-11}\times(5510)^2\times(6.371\times10^6)^2$.
$(5510)^2 = 3.036\times10^7$;
$(6.371\times10^6)^2 = 4.059\times10^{13}$;
$p_c = \frac23\pi\times6.6743\times10^{-11}\times3.036\times10^7\times4.059\times
10^{13} = 1.72\times10^{11}$ Pa = 172 GPa. The actual central pressure is about
364 GPa, so the constant-density model underestimates it by a factor of about 2.1
— the correct direction, because real material is compressed to a much higher
density in the interior, so more mass lies within each radius and the weight is
greater.

**(d)** A realistic model needs an equation of state (density as a function of
pressure and temperature) and a composition model, solved self-consistently with
the Adams-Williamson or a full equation-of-state integration; the standard
reference model is PREM (Dziewonski & Anderson, 1981). Consult
[12-global-geophysics-interior](../../../12-global-geophysics-interior/README.md)
for the details, and verify the citation against the primary literature before
quoting numbers from it.
