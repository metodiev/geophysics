# Solutions — 07-04-01 Geodetic Datums, Ellipsoids and Coordinate Frames

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [01 Geodetic Datums](../01-geodetic-datums.md).

---

## ★1 — Constants of the synthetic ellipsoid

$$b = a(1-f) = 6378000\left(1-\tfrac{1}{297}\right) = \mathbf{6356525.2525\ m},$$

$$e^{2} = 2f-f^{2} = 6.722670\times10^{-3},\qquad
e'^{2} = \frac{e^{2}}{1-e^{2}} = 6.768170\times10^{-3}.$$

WGS 84 for comparison: $b = 6356752.3142\ \mathrm{m}$ ($227\ \mathrm{m}$ larger
than the synthetic datum), $e^{2} = 6.694379990\times10^{-3}$. The synthetic
ellipsoid is deliberately *not* a real one; what matters is that replacing one
ellipsoid by another changes every derived quantity systematically.

---

## ★2 — Radii of curvature on WGS 84

| $\varphi$ | $N$ (m) | $M$ (m) | $N-M$ (m) |
|---|---|---|---|
| 0 | 6378137.0000 | 6335439.3273 | 42697.67 |
| 45 | 6388838.2901 | 6367381.8156 | 21456.47 |
| 60 | 6394209.1738 | 6383453.8572 | 10755.32 |
| 90 | 6399593.6258 | 6399593.6258 | 0.00 |

$N > M$ everywhere below the pole, and the difference **shrinks towards the
pole**, vanishing there. At the equator $N$ is the semi-major axis and $M$ is
reduced by the $e^{2}$ factor; at the pole both equal $a/\sqrt{1-e^{2}}$.

---

## ★3 — Geodetic versus geocentric latitude

$$\tan\psi = \left(1-e^{2}\right)\tan\varphi .$$

The maximum separation is at $\varphi = 45^{\circ}$:

$$\varphi-\psi \approx \frac{e^{2}}{2} = \frac{6.6944\times10^{-3}}{2}
= 3.347\times10^{-3}\ \mathrm{rad} = 0.1918^{\circ} = \mathbf{11.51\ arcmin},$$

which on the surface is
$3.347\times10^{-3}\times6378101\ \mathrm{m} = \mathbf{21.35\ km}$. The
demonstration measures $11.545$ arcmin and $21.42\ \mathrm{km}$ at
$\varphi = 45^{\circ}$, the small difference being the next-order term in
$e^{2}$.

---

## ★4 — Cartesian coordinates and the inverse

With $N(50^{\circ}) = 6390702.0\ \mathrm{m}$ (computed from WGS 84),

$$X = (N+h)\cos\varphi\cos\lambda = \mathbf{4045772.916\ m},$$
$$Y = (N+h)\cos\varphi\sin\lambda = \mathbf{713378.923\ m},$$
$$Z = \left(N(1-e^{2})+h\right)\sin\varphi = \mathbf{4863172.060\ m}.$$

The demonstration's inverse iteration (eight steps, starting from
$\varphi_0 = \arctan\left[Z/(p(1-e^{2}))\right]$) returns
$\varphi = 50.000000^{\circ}$, $\lambda = 10.000000^{\circ}$,
$h = 500.00\ \mathrm{m}$, with round-trip errors of $0$ in latitude and height and
$1.4\times10^{-14}$ degrees in longitude at worst — i.e. exact to double
precision. **The round trip is the mandatory test**, because a quadrant error in
the inverse preserves $X$, $Y$, $Z$ perfectly while returning a wrong station.

---

## ★5 — Displacement from the seven parameters

For small angles,

$$\mathbf{X}'-\mathbf{X} = \mathbf{T} + s\mathbf{X}
+ \boldsymbol{\varepsilon}\times\mathbf{X}.$$

At $\varphi = 45^{\circ}$, $\lambda = 16^{\circ}$,
$h = 100\ \mathrm{m}$: $\mathbf{X} = (4342655.041, 1245236.295, 4487419.120)\
\mathrm{m}$ (computed from the ellipsoid), so

- translation contributes $\left|\mathbf{T}\right| =
  \sqrt{120^{2}+80^{2}+200^{2}} = 246.58\ \mathrm{m}$;
- scale contributes $s\left|\mathbf{X}\right| =
  2.0\times10^{-6}\times6.37\times10^{6} = 12.74\ \mathrm{m}$;
- rotation contributes
  $\left|\boldsymbol{\varepsilon}\times\mathbf{X}\right| = 21.99\ \mathrm{m}$,
  with $\left|\boldsymbol{\varepsilon}\right| = \sqrt{0.5^{2}+0.3^{2}+1.2^{2}}
  = 1.334\ \mathrm{arcsec} = 6.468\times10^{-6}\ \mathrm{rad}$.

Total displacement $\mathbf{254.65\ m}$ — the value the demonstration prints.
**The translation dominates** ($246.6\ \mathrm{m}$ of the $254.7\ \mathrm{m}$
result), the rotation contributes $22.0\ \mathrm{m}$ and the scale
$12.7\ \mathrm{m}$ (the three add as vectors, not scalars, so the total is
slightly less than their sum). Translation dominance is the usual ordering for
datum-to-datum transformations and the reason a translation-only fit is often good
to a few metres.

---

## ★6 — Ellipsoidal rise over $40\ \mathrm{km}$

With $N$ increasing at $30\ \mathrm{mm\,km^{-1}}$:

$$\Delta h = \Delta H + \Delta N = 45.20 + 1.200 = \mathbf{46.40\ m}.$$

Using a single mean $N$ (mean of $45.000$ and $46.200$, i.e. $45.600\ \mathrm{m}$)
gives an error at each end of

$$\max\left|N(x)-45.600\right| = \left|45.000-45.600\right| = 0.600\ \mathrm{m}
= \mathbf{600\ mm}.$$

That is two orders of magnitude more than the levelling itself, and ten times the
precision of a modern GNSS height. **The geoid gradient, not the measurement, is
the limit** whenever ellipsoidal and orthometric heights are mixed.

---

## ★7 — Reinterpretation across a $137\ \mathrm{m}$ ellipsoid change

The demonstration's synthetic case (datum B with $a$ smaller by $137\ \mathrm{m}$)
gives, at $\varphi = 60^{\circ}$:

- latitude shift $-78.26\ \mathrm{m}$;
- height change $-204.49\ \mathrm{m}$;
- longitude shift $3.6\times10^{-15}$ degrees (round-off).

The errors are **not** a rigid offset: the latitude shift is zero at the equator,
largest in the mid-latitudes ($-90.37\ \mathrm{m}$ at $45^{\circ}$) and smaller
again at high latitude, while the height change grows monotonically towards the
pole ($-137.00\ \mathrm{m}$ at the equator to $-224.34\ \mathrm{m}$ at
$80^{\circ}$). A single translation cannot reproduce a latitude-dependent
shift-plus-height-change pattern: the discrepancy is a **distortion**, which is
why a proper transformation needs scale and rotation as well as translation, and
why for large networks even seven parameters are insufficient. The practical
statement: without a transformation, coordinates differ by tens to hundreds of
metres in a pattern that no offset can absorb.

---

## ★8 — A $10\ \mathrm{km}$ baseline with a $1\ \mathrm{ppm}$ scale error

The scale term stretches every coordinate vector by $s$, so a baseline of length
$L$ changes by

$$\delta L = s\,L_{\text{from the origin, not the baseline}} .$$

Precisely: scaling *coordinates* by $s$ multiplies the vector between two points by
$(1+s)$ only if the scale is applied about the origin — then the baseline length
changes by $sL = 1\times10^{-6}\times10\ \mathrm{km} = \mathbf{10\ mm}$.

**Detectability:** the stated precision is $5\ \mathrm{mm} + 1$ ppm, i.e. for a
$10\ \mathrm{km}$ baseline $5 + 10 = 15\ \mathrm{mm}$. A $10\ \mathrm{mm}$ bias is
below that, so it is **not** detectable in a single baseline at that precision —
but it is at the edge, and over a network with redundant baselines the scale
parameter becomes estimable to well under $1\ \mathrm{ppm}$, at which point the
bias would be resolved. The lesson's general point: a scale error is a *linear*
function of position, so its effect grows with baseline length, and a
$1\ \mathrm{ppm}$ scale error on a $100\ \mathrm{km}$ baseline is $100\ \mathrm{mm}$
— easily detectable and easily mistaken for a tectonic signal.
