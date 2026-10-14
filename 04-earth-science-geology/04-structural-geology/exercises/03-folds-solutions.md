# Solutions — 04-04-03 Fold Geometry, Mechanisms and Interpretation

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Geometry of a sinusoid

**(a)** The slope is $\mathrm{d}z/\mathrm{d}x = -Ak\sin(kx)$ with
$k = 2\pi/\lambda$, so its maximum magnitude is $Ak = 200 \times 2\pi/2000 =
0.6283$ and the maximum limb dip is $\arctan 0.6283 = 32.14^\circ$. It occurs at
the inflection points, where $\mathrm{d}^2z/\mathrm{d}x^2 = 0$ — the two rows of
the demo's table labelled `inflection (max dip)`.

**(b)** At the crest $\mathrm{d}z/\mathrm{d}x = 0$, so the curvature is just
$|z''| = Ak^2 = 200 \times (2\pi/2000)^2 = 1.9739 \times 10^{-3}$ m$^{-1}$, the
demo's `1.9739e-03`.

**(c)** At the inflection points. Structurally this is where the layer is planar
in profile and where the sense of the layer-parallel shear reverses; it is also
where a fold is least likely to develop an axial-plane cleavage, because there is
no curvature to localise it.

**(d)** The amplitude and the wavelength. The limb dip is a consequence of those
two and does not determine them: the demo's fold and a fold of half the amplitude
at a quarter of the wavelength have the same maximum dip and different
shortenings.

---

## ★2 — Thickness ratios

**(a)** $t' = \cos 10^\circ = 0.9848$; $\cos 50^\circ = 0.6428$;
$\cos 70^\circ = 0.3420$. These are the demo's `parallel t-prime` column.

**(b)** $t' = 1$ — constant vertical thickness.

**(c)** $1.0000/0.6428 = 1.56$.

**(d)** Because $t'$ is measured directly: pick a marker pair, measure the
perpendicular distance between them at the hinge and on the limb. The ratio of
1.56 at 50° of limb dip is far outside a field measurement error, so the
measurement discriminates the mechanisms rather than merely classifying the fold.

---

## ★3 — Flexural-slip shear

$\gamma = 2\tan(\alpha/2)$ is the layer-parallel shear strain accumulated across a
limb folded by flexural slip; it is the strain that produces the layer-parallel
slickenlines seen on bedding surfaces in folded sequences.

**(a)** At 30°: $2\tan 15^\circ = 0.5359$. At 60°: $2\tan 30^\circ = 1.1547$.
Both are the demo's printed values.

**(b)** $\tan 30^\circ = 0.5774$; $\tan 60^\circ = 1.7321$.

**(c)** The first pair corresponds to flexural slip, the second to homogeneous
simple shear of the whole limb. They differ because flexural slip distributes the
rotation between the two limbs through layer-parallel movement, so the strain
accumulated at any point is smaller than the strain a uniformly sheared block
would carry for the same limb dip. The difference is 8 per cent at 30° and 50 per
cent at 60°.

**(d)** A finite-strain measurement across the limb — deformed ooids, reduction
spots, belemnite guards, or any strain marker — giving the strain ellipse rather
than just the dip. Flexural slip predicts the smaller value and, importantly, a
strain that varies systematically across the limb.

---

## ★4 — The demo

**(a)** `over four wavelengths: chord = 8,000.0 m, arc length = 8,739.1 m` and
`excess length (shortening) = 739.1 m = 8.4575% of the arc length`.

**(b)** `Maximum limb dip occurs at the inflection points and is 32.14 deg`.

**(c)** `recovered amplitude = |c| lambda/(2 pi) = 153.2 m against a true 150.0 m`
with `error +3.2 m (+2.16%)` and `rms residual 0.03019 in slope units = 1.729 deg
in dip`, consistent with the 1.5° of synthetic noise.

**(d)** The fit assumed the wavelength. Fitting frequency and amplitude together
from the dips of one surface is ill-conditioned, which is why field studies
report dip *and* wavelength and why a short traverse supports only a rough fold
shape.

---

## ★5 — Buckling

**(a)** $\lambda_d/d = 2\pi(10/6)^{1/3} = 2\pi \times 1.1856 = 7.45$;
for $G = 100$, $16.05$; for $G = 1000$, $34.58$. The demo prints
`7.4495`, `16.0495`, `34.5777`.

**(b)** The exponent is $1/3$. From $G = 10$ to $G = 1000$ the ratio of
wavelengths is $34.5777/7.4495 = 4.642$, and $100^{1/3} = 4.642$. The demo
verifies the exponent directly by finite difference and prints
`fitted exponent 0.333333 against the predicted 1/3 = 0.333333`.

**(c)** A wavelength ratio of 2 implies $G$ a factor of $2^3 = 8$ larger — but any
$G$ can be multiplied by 8 and give the same wavelength ratio, so the wavelength
does not determine $G$, only its **ratio** between two layers, and that only as a
cube. A 10 per cent error in wavelength is a 33 per cent error in the inferred
viscosity ratio from a quantity that is itself difficult to estimate
independently.

**(d)** As a consistency check on a viscosity ratio obtained independently (from
creep-law parameters and temperature, say), and as an explanation of why
competent layers in a range of settings buckle at wavelengths of a few to a few
tens of layer thicknesses. It is not a measurement of viscosity.

---

## ★6 — Excess area

**(a)** `predicted h = 4,052.8 m` from the closed form, and the numerical
inversion gives `4,329.8` — a difference of `6.83%`.

**(b)** The closed form uses the second-order arc-length approximation
$\sqrt{1+w'^2} \approx 1 + w'^2/2$, and at a maximum limb dip of 51.5° that
expansion is inadequate. The approximation **understates the shortening and hence
understates the depth**; the exact quadrature gives the larger, correct value.

**(c)** `the two perturbed columns change h by -8.0% and +19.7% respectively`:
$-8.0$ per cent for a 10 per cent increase in amplitude, $+19.7$ per cent for a
10 per cent increase in wavelength.

**(d)** The wavelength, because $h \propto \lambda^2$ but $h \propto 1/A$. And
the wavelength of a fold belt is exactly the quantity most sensitive to how much
of the belt is exposed and to where the section is drawn.

---

## ★7 — Deriving the closed form

**(a)** With $w(x) = A[1 - \cos(2\pi x/\lambda)]/2$ over $n$ wavelengths,

$$A_{\text{excess}} = \int_0^{n\lambda} w\,\mathrm{d}x = \frac{A}{2}
\left[n\lambda - 0\right] = \frac{n\lambda A}{2},$$

because the cosine integrates to zero over complete periods.

**(b)** The arc length is
$\int\sqrt{1 + w'^2}\,\mathrm{d}x$ with $w'(x) = (A\pi/\lambda)\sin(2\pi x/\lambda)$.
To second order, $\sqrt{1+w'^2} \approx 1 + w'^2/2$, and
$\int_0^{n\lambda}w'^2\mathrm{d}x = (A^2\pi^2/\lambda^2)(n\lambda/2) =
nA^2\pi^2/(2\lambda)$. Hence

$$S \approx \frac{1}{2} \times \frac{nA^2\pi^2}{2\lambda} =
\frac{n\pi^2A^2}{4\lambda}.$$

The factor of 4 comes from two places: the $\tfrac12$ in the second-order
expansion of $\sqrt{1+w'^2}$, and the factor $\tfrac12$ from the mean square of
$\sin^2$ over complete periods.

**(c)** Dividing (a) by (b):

$$h = \frac{n\lambda A/2}{n\pi^2A^2/(4\lambda)} = \frac{2\lambda^2}{\pi^2A}.$$

**(d)** The number of waves cancels because both the excess area and the
shortening are *extensive* quantities: doubling the number of waves doubles both,
so their ratio is an intensive property of the fold train. That is the content of
the result — **the depth to detachment is a property of the fold wavelength and
amplitude, not of how long the belt is** — and the kinematic assumption that makes
it true is that the shortening is accommodated entirely at the detachment with a
balanced section. A single ramp with no flat gives $A = hS/2$ and therefore $h =
2A/S$, a factor of two, which is larger than any of the measurement errors
involved.

---

## ★8 — A limb that is neither parallel nor similar

**(a)** Parallel folding predicts $t' = \cos 50^\circ = 0.643$; similar folding
predicts $t' = 1$. A measured 0.75 lies between them, so neither end member fits
and the fold is **not** explained by either mechanism alone.

**(b)** The standard explanation is a **parallel fold that was subsequently
flattened**: layer-parallel shortening superimposed on the flexural-slip fold
reduces the thickness on the limbs relative to the hinge. A fold that began
parallel and was then flattened in the shortening direction moves $t'$ from
$\cos\alpha$ towards 1.

**(c)** Take a simple model: homogeneous flattening by a factor $R$ along the
axial trace combined with the flexural-slip shape. For small flattening, the
thickness on the limb is reduced by the component of shortening normal to the
layer, and the ratio moves towards 1; a first estimate is
$1 - R(x) \approx$ the fractional reduction required, i.e.
$0.75/0.643 = 1.167$, so about 17 per cent of the original limb thickness has been
added — which a pure flattening cannot do, so the correct reading is that the fold
started somewhat less parallel than a pure flexural-slip fold, or that the
thickness ratio was measured across a shortened marker pair. **This is the point
of the exercise**: an intermediate $t'$ does not by itself identify a mechanism,
and the model must be stated before the number means anything.

**(d)** The decisive measurement is a **finite-strain estimate from strain
markers on the same limb**. A parallel-then-flattened fold predicts a strain
ellipse with its short axis normal to the layer near the hinge and rotating on the
limbs, and with a measurable flattening component; a pure flexural-slip fold
predicts no such flattening. Reporting the strain ellipse, not just $t'$, is what
turns the classification into a test.
