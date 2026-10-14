# Solutions — 25-01-03 Project: Computing Gravity Through a Layered Earth

> Read after attempting. Lesson:
> [03 Gravity of Earth's Layers](../03-gravity-of-earths-layers.md). All values
> are **SYNTHETIC** teaching numbers printed by
> [`code/layered_earth_gravity_demo.py`](../code/layered_earth_gravity_demo.py).

---

## ★1 — A shell mass

$$V = \frac{4\pi}{3}\left(r_\text{out}^{3} - r_\text{in}^{3}\right)
= \frac{4\pi}{3}\left((6.0\times10^{6})^{3} - (5.0\times10^{6})^{3}\right)
= \frac{4\pi}{3}\left(9.1\times10^{19}\right) = 3.8118\times10^{20}\ \mathrm{m^{3}},$$

$$M = \rho V = 4000 \times 3.8118\times10^{20}
= 1.5247\times10^{24}\ \mathrm{kg}.$$

Unit: kg; the radius must be in metres for the volume to come out in m³, which is
failure mode §8(1) of the lesson.

---

## ★2 — Uniform sphere at the surface

$$g = \frac{4\pi G}{3}\rho R
= \frac{4\pi \times 6.67430\times10^{-11}}{3} \times 5504.0 \times 6.371\times10^{6}
= 9.8035\ \mathrm{m\,s^{-2}}.$$

It agrees exactly with the model's surface value. This is not a coincidence and
not a validation: $g = GM/R^{2}$ depends only on the total mass and the radius,
so **any** model with the same $M$ and $R$ matches at the surface. The agreement
carries no information about the interior.

---

## ★3 — Uniform versus layered interior

Uniform sphere at $r = 1000\ \mathrm{km}$:

$$g = \frac{4\pi G}{3}\rho r
= 1.53876\times10^{-6} \times 1.0\times10^{6}
= 1.5388\ \mathrm{m\,s^{-2}}.$$

Ratio to the layered value:

$$\frac{3.6596}{1.5388} = 2.378.$$

The layered Earth's gravity at 1000 km is **2.38 times** the uniform-sphere
value, because the real core is much denser than the mean density, so the
enclosed mass at 1000 km is much larger than the uniform model predicts.

---

## ★4 — Verifying the CMB value

$$g = \frac{G M}{r^{2}}
= \frac{6.67430\times10^{-11} \times 1.9578\times10^{24}}{(3.48\times10^{6})^{2}}
= \frac{1.30672\times10^{14}}{1.21104\times10^{13}}
= 10.7900\ \mathrm{m\,s^{-2}}.$$

Enclosed mass fraction:

$$\frac{1.9578\times10^{24}}{5.9620\times10^{24}} = 32.8\%.$$

So one third of the Earth's mass lies inside the core-mantle boundary, at 55% of
the radius — the density contrast, not the geometry, is what produces the gravity
maximum there.

---

## ★5 — Analytic and Monte Carlo density sensitivity

**Analytic.** Adding $\Delta\rho$ uniformly to the crust adds
$\Delta M = \Delta\rho \times V_\text{crust}$ to the enclosed mass, and only
$M(R)$ matters at the surface:

$$\Delta g = \frac{G\,\Delta M}{R^{2}}
= \frac{6.67430\times10^{-11} \times (200 \times 1.2399\times10^{19})}
        {(6.371\times10^{6})^{2}}
= \frac{1.65515\times10^{11}}{4.05896\times10^{13}}
= 4.078\times10^{-3}\ \mathrm{m\,s^{-2}}.$$

In mGal: $4.078\times10^{-3}/10^{-5} = 407.8\ \mathrm{mGal}$. This is the same
number the demonstration prints as $415.90$ ppm; converting
$415.90\ \mathrm{ppm} \times 9.8035\ \mathrm{m\,s^{-2}} = 4.077\times10^{-3}\
\mathrm{m\,s^{-2}}$ gives the identical result, so the ppm and mGal columns are
two readings of one change — a unit lesson in itself.

**Slope.** $\mathrm{d}g/\mathrm{d}\rho = 407.8/200 = 2.039\ \mathrm{mGal}$ per
kg m⁻³, so $\pm100\ \mathrm{kg\,m^{-3}}$ predicts a scatter of
$203.9\ \mathrm{mGal}$. The Monte Carlo measures $200.51\ \mathrm{mGal}$, which
is $1.7\%$ lower. That deficit is consistent with sampling error: the standard
deviation of a sample standard deviation from $M = 400$ draws has relative error
$1/\sqrt{2M} = 3.5\%$, so a $1.7\%$ deviation is well within one standard error.

---

## ★6 — Why the uniform sphere fails at the CMB

$$\frac{g_\text{layered}}{g_\text{uniform}} = \frac{10.7900}{5.3563} = 2.014.$$

The responsible feature is the **concentration of mass toward the centre**: the
core holds 32.8% of the mass inside 55% of the radius, so the enclosed mass at
3480 km is twice what a uniform distribution would put there. The density
*profile*, not the total mass, sets the interior field.

---

## ★★★7 — Inverting the gravity profile for layer densities

**Parametrisation.** Five layer densities
$\mathbf{m} = (\rho_1,\dots,\rho_5)$; radii fixed from seismology (this is the
standard split — gravity determines density, seismology determines geometry).

**Sensitivity matrix.** For datum $j$ at radius $r_j$,
$g_j = G M(r_j)/r_j^{2}$, so

$$A_{ji} = \frac{\partial g_j}{\partial \rho_i}
= \frac{G}{r_j^{2}}\cdot\frac{\partial M(r_j)}{\partial \rho_i}
= \frac{G}{r_j^{2}}\cdot\frac{4\pi}{3}
\left(\min(r_j,r_{\text{out},i})^{3} - r_{\text{in},i}^{3}\right)$$


for $r_j > r_{\text{in},i}$, and zero otherwise. **Size:** $40 \times 5$ — an
over-determined problem, 40 data for 5 parameters.

**Null space.** The null space is trivial for this parametrisation *only* if the
five sensitivity vectors are independent, which they are: each layer's column is
zero for data inside it, so the columns are linearly independent and the problem
has a unique least-squares solution. What is *not* determined is the
**fine-scale structure within each shell**, because the parametrisation cannot
represent it; and the useful diagnostic is the model resolution matrix, not the
null space of a deliberately coarse model.

**A second observation.** Adding the **free-air gradient measured at the
surface** constrains the mass near the surface and is almost degenerate with
$\rho_5$ alone. A far better second observation is a **normal-mode or
surface-wave dispersion** measurement, which samples depth with a different
kernel; gravity's kernels are all of the form $1/r_j^{2}$, so gravity alone
cannot distinguish a dense deep shell from a less dense shallower one when the
two produce the same enclosed mass.
