# Solutions — 25-02-02 Project: Gravity Anomaly of Simple Bodies

> Read after attempting. Lesson:
> [02 Simple Gravity Model](../02-simple-gravity-model.md). All values are
> **SYNTHETIC** teaching numbers; the demonstration is
> [`code/simple_gravity_model_demo.py`](../code/simple_gravity_model_demo.py).

---

## ★1 — Sphere peak

$$g_\text{max} = \frac{4}{3}\pi G \Delta\rho \frac{R^{3}}{z^{2}}
= \frac{4}{3}\pi \times 6.67430\times10^{-11} \times 300
\times \frac{(1.5\times10^{3})^{3}}{(4.0\times10^{3})^{2}}.$$

Numerator factor: $\frac{4}{3}\pi G\Delta\rho = 4.18879 \times 6.67430\times10^{-11}
\times 300 = 8.3871\times10^{-8}\ \mathrm{s^{-2}}$.
Then $R^{3} = 3.375\times10^{9}\ \mathrm{m^{3}}$ and $z^{2} = 1.6\times10^{7}\
\mathrm{m^{2}}$:

$$g_\text{max} = 8.3871\times10^{-8} \times \frac{3.375\times10^{9}}{1.6\times10^{7}}
= 8.3871\times10^{-8} \times 210.94 = 1.7692\times10^{-5}\ \mathrm{m\,s^{-2}}
= 1.769\ \mathrm{mGal}.$$

---

## ★2 — Two depth rules from one half-width

Sphere: $z = 1.3048 \times 3.0 = 3.914\ \mathrm{km}$.

Cylinder: $z = 1.0000 \times 3.0 = 3.000\ \mathrm{km}$.

Percentage difference, taking the sphere value as reference:

$$\frac{3.914 - 3.000}{3.914} = 23.4\%.$$

The two rules differ by $30.5\%$ in the *inverse* direction
($1.3048/1.0000$); quoting the depth without the shape assumption leaves a
$23$–$30\%$ ambiguity that no measurement precision removes.

---

## ★3 — Cylinder peak and the ratio

$$g_\text{max}^\text{cyl} = 2\pi G \Delta\rho \frac{R^{2}}{z}
= 2\pi \times 6.67430\times10^{-11} \times 300 \times \frac{(1.5\times10^{3})^{2}}
{4.0\times10^{3}}.$$

With $2\pi G\Delta\rho = 4.19370\times10^{-10} \times 300 = 1.25811\times10^{-7}$:

$$g_\text{max}^\text{cyl} = 1.25811\times10^{-7} \times \frac{2.25\times10^{6}}{4.0\times10^{3}}
= 1.25811\times10^{-7} \times 562.5 = 7.0769\times10^{-5}\ \mathrm{m\,s^{-2}}
= 7.077\ \mathrm{mGal}.$$

Ratio check:

$$\frac{g_\text{max}^\text{cyl}}{g_\text{max}^\text{sphere}}
= \frac{2\pi G\Delta\rho R^{2}/z}{\frac{4}{3}\pi G\Delta\rho R^{3}/z^{2}}
= \frac{3}{2}\cdot\frac{z}{R} = 1.5 \times \frac{4.0}{1.5} = 4.00,$$

and $7.077/1.769 = 4.00$ ✔. A 2-D body is *not* slightly bigger than a 3-D one at
equal parameters; it is a factor of four bigger here.

---

## ★4 — The degeneracy table

From $R^{3} = g_\text{max} z^{2}/\left(\frac{4}{3}\pi G\Delta\rho\right)$ with
$g_\text{max} = 1.7692\times10^{-5}\ \mathrm{m\,s^{-2}}$ and
$\frac{4}{3}\pi G\Delta\rho = 8.3871\times10^{-8}\ \mathrm{s^{-2}}$:

$$k = \frac{g_\text{max}}{\frac{4}{3}\pi G\Delta\rho} = \frac{1.7692\times10^{-5}}
{8.3871\times10^{-8}} = 210.94\ \mathrm{m}.$$

| $z$ (km) | $R = (k z^{2})^{1/3}$ (km) | $x_{1/2} = 0.7664 z$ (km) |
|---|---|---|
| 2.0 | 0.945 | 1.533 |
| 4.0 | 1.500 | 3.066 |
| 6.0 | 1.965 | 4.598 |

The **peak** column is identical in all three rows (that is the point of the
table); the **$R$** column is degenerate with the assumed $z$; the
**$x_{1/2}$** column is not. The peak determines only the group
$\Delta\rho R^{3}/z^{2}$, and the half-width determines $z$, so the pair
(half-width, peak) determines $z$ and $\Delta\rho R^{3}$ — and a density estimate
from elsewhere closes the problem.

---

## ★5 — The slab

$$g = 2\pi G \Delta\rho t = 4.19370\times10^{-10} \times 400 \times 300
= 5.0324\times10^{-5}\ \mathrm{m\,s^{-2}} = 5.032\ \mathrm{mGal}.$$

Inverting for the thickness that gives $5.0\ \mathrm{mGal}$:

$$t = \frac{g}{2\pi G \Delta\rho}
= \frac{5.0\times10^{-5}}{4.19370\times10^{-10} \times 400}
= \frac{5.0\times10^{-5}}{1.67748\times10^{-7}} = 298.1\ \mathrm{m}.$$

Note what the second answer is *not*: there is no depth in it. A $298\ \mathrm{m}$
slab at 1 km and at 20 km produce the same $5.0\ \mathrm{mGal}$, so the slab
model must never be used to infer depth.

---

## ★6 — Two interpretations of one profile

**As a sphere.** Depth from the width, radius from the amplitude:

$$z = 1.3048 \times 4.0 = 5.219\ \mathrm{km},$$

$$R = \left(\frac{g_\text{max} z^{2}}{\frac{4}{3}\pi G\Delta\rho}\right)^{1/3}
= \left(\frac{6.0\times10^{-5} \times (5.219\times10^{3})^{2}}
{1.39786\times10^{-7}}\right)^{1/3}
= (1.1691\times10^{10})^{1/3} = 2.269\ \mathrm{km}.$$

**As a cylinder.**

$$z = 4.000\ \mathrm{km},$$

$$R = \left(\frac{g_\text{max} z}{2\pi G\Delta\rho}\right)^{1/2}
= \left(\frac{6.0\times10^{-5} \times 4.0\times10^{3}}{2.09685\times10^{-7}}
\right)^{1/2}
= (1.1446\times10^{6})^{1/2} = 1.070\ \mathrm{km}.$$

**Which is more conservative for the radius.** The **cylinder** interpretation:
it returns a smaller radius ($1.07$ versus $2.27\ \mathrm{km}$), so the sphere
model would report a body four times the volume of the cylinder model. For a
resource or hazard statement, quoting the smaller radius is the safer default
until the strike length is measured — and the along-strike extent is exactly the
observation that distinguishes the two cases.

---

## ★★★7 — A shape-independent depth measurement

**Quantity to measure.** The **vertical gravity gradient** $\partial g_z /
\partial z$ at the anomaly's centre, in addition to the anomaly itself.
Equivalently, the difference in $g$ between two heights separated by a known
vertical distance $\Delta z$ (a tower, a borehole, or a moving-platform
gradiometer).

**Instrument class.** A relative gravimeter measured at two heights (the
classical tower or borehole gradient), or an airborne/spaceborne gravity
gradiometer that measures $\partial g_z/\partial z$ directly.

**The relation.** For a point mass $M$ at depth $z$ directly beneath the station,

$$g_z = \frac{GM}{z^{2}},
\qquad
\frac{\partial g_z}{\partial z} = -\frac{2GM}{z^{3}},$$

so the ratio

$$\boxed{\;z = \frac{2\,g_z}{\left|\partial g_z/\partial z\right|}\;}$$

depends **only on $z$** — the mass cancels. That is what makes the measurement
shape-independent for a point mass: it delivers the depth with no assumption about
$\Delta\rho$ or $R$, which is exactly what §6's degeneracy denied to the
amplitude-and-width method.

**Error budget.** $\sigma_z/z = \sqrt{(\sigma_g/g)^{2} +
(\sigma_{\partial g}/\partial g)^{2}}$; the gradient term dominates because
$\partial g/\partial z$ is small — for $g = 1.77\ \mathrm{mGal}$ at $z = 4\
\mathrm{km}$, $\partial g/\partial z = 2g/z = 8.85\times10^{-4}\ \mathrm{mGal\,m^{-1}}$,
so a $0.01\ \mathrm{mGal}$ instrument gives
$\sigma_{z}/z \approx 0.005/0.885 = 0.6\%$ — but only if the two levels are
separated by enough to make the difference resolvable, which requires
$\Delta z \gtrsim 10\ \mathrm{m}$ for this instrument.

**What breaks it first.** The point-mass idealisation. A finite body of radius
$R$ comparable to $z$ makes the gradient depend on the shape as well, and the
measured ratio gives a *moment* of the body rather than its depth. The
next-order correction is the second vertical derivative, which is why
gradiometry is used in practice: the tensor components separate the depth from the
shape for bodies that are not point-like.
