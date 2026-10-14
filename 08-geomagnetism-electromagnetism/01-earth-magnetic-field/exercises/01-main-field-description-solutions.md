# Solutions — 08-01-01 Describing the Main Field: Declination, Inclination, Intensity

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [01 Describing the Main Field](../01-main-field-description.md).

---

## ★1 — Components to elements

$$H = \sqrt{21000^2 + (-4200)^2} = \sqrt{4.41\times10^{8} + 1.764\times10^{7}}
= \sqrt{4.5864\times10^{8}} = 21416.82\ \mathrm{nT}.$$

$$F = \sqrt{H^2 + Z^2} = \sqrt{4.5864\times10^{8} + 1.48225\times10^{9}}
= \sqrt{1.94089\times10^{9}} = 44055.53\ \mathrm{nT}.$$

$$D = \arctan\!\left(\frac{-4200}{21000}\right) = \arctan(-0.2000)
= -11.3099^{\circ} = 348.6901^{\circ},$$

i.e. $11.31^{\circ}$ **west**. The four-quadrant form matters: with
$X>0$ the answer is in the fourth quadrant, not the second.

$$I = \arctan\!\left(\frac{38500}{21416.82}\right) = \arctan(1.79766)
= 60.9050^{\circ}.$$

$Z > 0$ (down) and $I = 60.9^{\circ}$: the site is in the **northern
hemisphere**. The axial dipole relation $\tan I = 2\tan\lambda$ of the next
lesson inverts to

$$\lambda = \arctan\!\left(\frac{\tan I}{2}\right)
= \arctan(0.89883) = 41.94^{\circ},$$

so an axial dipole reaching $I = 60.9^{\circ}$ at this site would put it at
geomagnetic latitude $41.9^{\circ}$.

---

## ★2 — Units of one intensity

$$48000\ \mathrm{nT} = 48000\times10^{-9}\ \mathrm{T}
= 4.8\times10^{-5}\ \mathrm{T} = 48.0\ \mu\mathrm{T},$$
$$48000\ \mathrm{nT} = 48000\ \gamma \quad(\text{gamma} \equiv \text{nT}),$$
$$H_{\text{equiv}} = \frac{4.8\times10^{-5}}{4\pi\times10^{-7}}
= \frac{4.8\times10^{-5}}{1.256637\times10^{-6}}
= 38.1972\ \mathrm{A\,m^{-1}}.$$

Equivalently, $1\ \mathrm{A\,m^{-1}} \leftrightarrow 1256.64\ \mathrm{nT}$.

---

## ★3 — Dimensional check

$X$, $Y$, $Z$, $H$, $F$ are all in nT (tesla for SI purists); $D$ and $I$ are in
degrees (or radians). $H^2+Z^2$ has units $\mathrm{nT^2}$, and
$F^2 = \left(\sqrt{X^2+Y^2+Z^2}\right)^2$ also has units $\mathrm{nT^2}$. ✔

An angle is dimensionless, which is why $\tan D = Y/X$ is a legal equation: a
ratio of two intensities is a pure number.

---

## ★4 — Linearised versus exact sensitivity

**Mid-latitude site.** The differential of $\tan D = Y/X$ at constant $X$ is
$\mathrm{d}D = \cos D\,\mathrm{d}Y/H$, and the cruder form $\mathrm{d}Y/H$ holds
only when $D$ is small. At site A, $D = 4.2892^{\circ}$ and $\cos D = 0.99720$:

$$\mathrm{d}D = \frac{\cos D}{H}\mathrm{d}Y = \frac{0.99720}{20056.171}\times5
= 2.4860\times10^{-4}\ \mathrm{rad} = 0.014244^{\circ} = 0.855\ \mathrm{arcmin},$$
$$\mathrm{d}D \approx \frac{5}{20056.171} = 0.014284^{\circ}
= 0.857\ \mathrm{arcmin}\ \text{(crude form)}.$$

Exact, with $X = 20000\ \mathrm{nT}$, $Y = 1500\ \mathrm{nT}$:

$$D = \arctan(1500/20000) = 4.28915^{\circ}, \quad
D' = \arctan(1505/20000) = 4.30343^{\circ},$$
$$\mathrm{d}D = 0.014284^{\circ} = 0.857\ \mathrm{arcmin}.$$

The correct differential reproduces this to 0.3%; the crude form agrees here
only by accident of the small declination.

**Near-pole site.** $H = 471.699\ \mathrm{nT}$, $D = 32.00538^{\circ}$,
$\cos D = 0.84805$:

$$\mathrm{d}D = \frac{0.84805}{471.699}\times5 = 8.9883\times10^{-3}\ \mathrm{rad}
= 0.51495^{\circ} = 30.90\ \mathrm{arcmin},$$
$$\mathrm{d}D \approx \frac{5}{471.699} = 0.60734^{\circ}
= 36.44\ \mathrm{arcmin}\ \text{(crude form)}.$$

Exact, with $X = 400\ \mathrm{nT}$, $Y = 250\ \mathrm{nT}$:

$$D = \arctan(250/400) = 32.00538^{\circ}, \quad
D' = \arctan(255/400) = 32.51716^{\circ},$$
$$\mathrm{d}D = 0.51178^{\circ} = 30.71\ \mathrm{arcmin}.$$

The correct differential is 0.6% high; the crude $1/H$ form is **19% high**.
The lesson: near a pole where $D$ is large, use the differential
$\cos D\,\mathrm{d}Y/H$, not $\mathrm{d}Y/H$.

---

## ★5 — A heading error is a declination error of the same size

Rotate the reported frame by $\varepsilon$ clockwise. The reported components of
the true vector $\mathbf{B} = (X, Y)$ are

$$X' = X\cos\varepsilon + Y\sin\varepsilon, \qquad
Y' = -X\sin\varepsilon + Y\cos\varepsilon.$$

Then

$$\tan D' = \frac{Y'}{X'} = \frac{-X\sin\varepsilon + Y\cos\varepsilon}
{X\cos\varepsilon + Y\sin\varepsilon}.$$

Divide numerator and denominator by $H$ and recall $X/H = \cos D$,
$Y/H = \sin D$:

$$\tan D' = \frac{-\cos D\sin\varepsilon + \sin D\cos\varepsilon}
{\cos D\cos\varepsilon + \sin D\sin\varepsilon}
= \frac{\sin(D-\varepsilon)}{\cos(D-\varepsilon)}
= \tan(D - \varepsilon).$$

So $D' = D - \varepsilon$, and a heading error of $\varepsilon = 0.2^{\circ}$
produces exactly a $0.2^{\circ}$ declination error. This is why a declination
survey is only as good as its north reference: the heading error passes straight
through with unit gain, whatever the field strength. Note also that $I$ is
unaffected, because a rotation about the vertical leaves $Z$ and $|H|$ alone.

---

## ★6 — How large an error can declination tolerate?

Use the differential $\mathrm{d}D = \cos D\,\mathrm{d}Y/H$, so
$\mathrm{d}Y \le H\,\mathrm{d}D/\cos D$, with
$\mathrm{d}D = 1^{\circ} = 0.0174533\ \mathrm{rad}$:

$$\text{near-pole site } (H = 471.699,\ \cos D = 0.84805):\quad
\mathrm{d}Y \le \frac{471.699\times0.0174533}{0.84805} = 9.707\ \mathrm{nT},$$
$$\text{site A } (H = 20056.171,\ D = 4.2892^{\circ},\ \cos D = 0.99720):\quad
\mathrm{d}Y \le \frac{20056.171\times0.0174533}{0.99720} = 351.02\ \mathrm{nT}.$$

The near-pole site tolerates **36 times less** component error for the same
angular accuracy. Practical conclusion: at high magnetic latitude, declination is
a demanding measurement, and inclination — limited by $F$ rather than by $H$ — is
the cheaper datum to quote.

---

## ★7 — Recovering $I$ from total-field readings (specification)

**Setup.** The instrument measures $F$ only. Add a known bias field
$\mathbf{b}$ with magnitude $b \ll F$ along a known direction relative to the
sensor, in $k$ different orientations $\hat{u}_i$. Each reading is

$$F_i = \left|\mathbf{B} + b\,\hat{u}_i\right|
\approx F + b\,\hat{u}_i\cdot\hat{\mathbf{B}},$$

so the differences $F_i - F$ are linear in the unknown unit vector
$\hat{\mathbf{B}} = (X, Y, Z)/F$. With $k = 3$ non-coplanar bias directions and
one measurement of $F$ itself, the three components follow from a $3\times3$
linear solve; then $I = \arctan(Z/\sqrt{X^2+Y^2})$.

**Number of readings.** Four in total, or five with one degree of freedom for a
consistency check. In practice one uses more and solves in least squares.

**Algebra.** Let $A$ be the $k\times3$ matrix with rows $\hat{u}_i$. Then
$(F_i - F)/b = A\,\hat{\mathbf{B}}$, so
$\hat{\mathbf{B}} = (A^{\mathsf T}A)^{-1}A^{\mathsf T}\mathbf{d}$ where
$\mathbf{d}$ is the vector of differences divided by $b$.

**The assumption that could invalidate it.** The *first-order expansion* assumes
$b \ll F$, and it also assumes that $b$ is known in the sensor frame and
constant, and that $F$ does not drift between readings. If the field drifts by
more than the signal $b\,(\hat u\cdot\hat B)$ — which for reasonable
orientations can be small — the components are not recoverable. That is the
practical reason this method needs a fast sequence of readings or a reference
station: the drift must be small compared with $b$, not with $F$.

---

## ★8 — The volume element in $(H, D, I)$

Use the frame $(x,y,z) = (X,Y,Z)$ with $z$ down. Then

$$X = H\cos I\cos D, \qquad Y = H\cos I\sin D, \qquad Z = H\sin I,$$

which is exactly the spherical-coordinate map with radius $H$ and polar angle
$\pi/2 - I$. The Jacobian of the map $(H, D, I)\mapsto(x,y,z)$ is therefore the
usual spherical one with $\rho = H$ and colatitude $\theta = \pi/2 - I$:

$$\left|\frac{\partial(x,y,z)}{\partial(H,D,I)}\right|
= H^2\sin\theta = H^2\sin\!\left(\tfrac{\pi}{2}-I\right) = H^2\cos I.$$

So $\mathrm{d}V = H^2\cos I\,\mathrm{d}H\,\mathrm{d}D\,\mathrm{d}I$, and the
single volume element is $H^2\cos I$ — small at the poles, where $I\to\pm90^{\circ}$
and $\cos I \to 0$. **Why the cosine appears:** $D$ and $I$ are *angles*, and an
angular increment corresponds to an arc length proportional to the radius $H$
times the sine of the angle between the increment's direction and the radial
direction. For $D$ that factor is $\cos I$ (the horizontal projection), and for
$I$ it is $1$. If $I$ were measured as a colatitude from the pole instead of as a
declination-like angle from the equator, the map would be the standard spherical
one and the cosine would reappear as the sine of that colatitude — same geometry,
different bookkeeping.
