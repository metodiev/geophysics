# Exercises — 07-04-01 Geodetic Datums, Ellipsoids and Coordinate Frames

Attempt these before reading the
[solutions](./01-geodetic-datums-solutions.md). The lesson is
[01 Geodetic Datums](../01-geodetic-datums.md). WGS 84 parameters are standard
constants: $a = 6378137.0\ \mathrm{m}$,
$f = 1/298.257223563$; everything else is **SYNTHETIC**.

## ★ Foundational

**★1.** For the synthetic ellipsoid $a = 6378000\ \mathrm{m}$,
$f = 1/297$, compute $b$, $e^{2}$ and $e'^{2}$, and compare with WGS 84.

**★2.** Compute $N(\varphi)$ and $M(\varphi)$ on WGS 84 at
$\varphi = 0^{\circ}, 45^{\circ}, 60^{\circ}, 90^{\circ}$ and state in which
direction their difference grows.

**★3.** State the relation between geodetic and geocentric latitude and give the
maximum separation in arcminutes and in kilometres on the surface.

## ★★ Applied

**★★4.** A station is at $\varphi = 50^{\circ}$, $\lambda = 10^{\circ}$,
$h = 500\ \mathrm{m}$ on WGS 84. Compute its Cartesian coordinates, then verify
the inverse conversion returns the original latitude, longitude and height.

**★★5.** A seven-parameter transformation has
$\mathbf{T} = (120,-80,200)\ \mathrm{m}$,
rotations $(0.5,-0.3,1.2)\ \mathrm{arcsec}$ and $s = 2.0\times10^{-6}$. Compute
the total displacement of a point at $\varphi = 45^{\circ}$, and state which term
dominates.

**★★6.** A $40\ \mathrm{km}$ levelling line has heights $H$ rising $45\ \mathrm{m}$
and a synthetic geoid slope of $30\ \mathrm{mm\,km^{-1}}$. Compute the ellipsoidal
rise and the error introduced by using a single mean undulation.

## ★★★ Research-oriented

**★★★7.** Coordinates are given in a datum whose ellipsoid differs from WGS 84 by
$137\ \mathrm{m}$ in $a$ and by $2\times10^{-3}$ in flattening, and no
transformation is supplied. Estimate the resulting horizontal and vertical errors
at latitude $60^{\circ}$ and say whether the error is a rigid offset (removable by
a translation) or a distortion.

**★★★8.** A $10\ \mathrm{km}$ GNSS baseline is computed in a datum whose scale
parameter is unknown at the $1\ \mathrm{ppm}$ level. Estimate the baseline error,
and decide whether it is detectable with a horizontal precision of
$5\ \mathrm{mm} + 1\ \mathrm{ppm}$.
