# Solutions — 15-02-05 Marine Gravity and Magnetic Surveys

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [05 Marine Gravity and Magnetics](../05-marine-gravity-magnetics.md).

---

## ★1 — Deriving the Eötvös coefficients

The platform's eastward speed is $u = V\sin\alpha$. It experiences an additional
radially outward acceleration $2\Omega\cos\phi\,u$ (this is the vertical component
of the Coriolis acceleration for eastward motion), and a curvature acceleration
$V^{2}/R$. Both reduce the measured $g$, so

$$\Delta g = -\left[2\Omega\cos\phi\,V\sin\alpha + \frac{V^{2}}{R}\right].$$

Converting to mGal and knots, with $V_{\mathrm{kn}} = V/0.514444$ and
multiplying each $\mathrm{m\,s^{-2}}$ by $10^{5}$:

$$C_{\text{lin}} = 2\Omega \times 10^{5} \times 0.514444
= 2(7.292115\times10^{-5})(10^{5})(0.514444) = 7.5028\
\mathrm{mGal\,kn^{-1}},$$

$$C_{\text{quad}} = \frac{10^{5}(0.514444)^{2}}{6.371\times10^{6}}
= \frac{10^{5}(0.264652)}{6.371\times10^{6}} = 0.0041540\
\mathrm{mGal\,kn^{-2}}. \ ✔$$

Both agree with the coefficients used in practice ($7.503$ and $0.004154$) to the
precision of the rounded constants here. The $C_{\text{lin}}$ value is quoted *per
unit $\cos\phi$*: the full linear term carries $\cos\phi\sin\alpha$.

---

## ★2 — Eötvös correction, 12 kn eastward at 35°N

$$C_{\text{lin}} V\cos\phi\sin\alpha = 7.5028(12)(0.81915)(1)
= 73.75\ \mathrm{mGal},$$

$$C_{\text{quad}} V^{2} = 0.004154(144) = 0.598\ \mathrm{mGal},$$

$$E = 73.75 + 0.598 = 74.35\ \mathrm{mGal}.$$

**Signs:** both terms enter as corrections to be **subtracted** from the measured
value, because both are radially outward. Their *contributions to $E$* as defined
here are positive; the correction applied to the reading is $-74.35$ mGal. The
linear term reverses on a westward heading; the quadratic term does not.

Note the size: $74\ \mathrm{mGal}$ is comparable to a strong crustal anomaly. **A
survey that ignored the Eötvös correction on an east–west line would produce a
"anomaly" that is an artefact of its own speed.**

---

## ★3 — Free-air gradient

$$\frac{\mathrm{d}g}{\mathrm{d}h} = -\frac{2g}{R}
= -\frac{2(9.80665)}{6.371\times10^{6}} = -3.0785\times10^{-6}\
\mathrm{m\,s^{-2}\,m^{-1}} = -0.30785\ \mathrm{mGal\,m^{-1}}.$$

For a station *below* the reference, $h_{\text{station}} < 0$ relative to the
datum, so $g$ rises: the correction $+0.30785\,|h|$ is **added** when reducing a
sub-seafloor measurement. (Conventions vary in how $h$ is signed; the physical
statement is unambiguous — being closer to the mass increases $g$, and the free-air
gradient is the rate at which it does so.)

---

## ★4 — Corrections at 2500 m depth

Free-air (depth is the only input):

$$\Delta g_{\text{FA}} = 0.30785 \times 2500 = 769.63\ \mathrm{mGal},$$

added to a reading taken 2500 m below the datum.

Bouguer (needs the **density contrast**):

$$\Delta g_B = 2\pi G \Delta\rho H
= 2\pi(6.674\times10^{-11})(770)(2500)
= 2\pi(6.674\times10^{-11})(1.925\times10^{6})$$

$$= 8.074\times10^{-4}\ \mathrm{m\,s^{-2}}
= 80.72\ \mathrm{mGal}.$$

**Which needs what:** the free-air correction needs only geometry (the depth); the
Bouguer correction needs the depth *and* a density contrast between the rock and
the water it displaces. The density is the quantity a gravity survey is usually
trying to determine, so the Bouguer anomaly is **conditional** on an assumed
sub-surface density — which is why both the free-air and the Bouguer anomaly are
routinely reported, and why a Bouguer anomaly is not a measurement of rock density.

---

## ★5 — Dipole field at 20° and 70°

$$B(\lambda) = \frac{\mu_0 m}{4\pi R^{3}}\sqrt{1+3\sin^{2}\lambda},$$

with $\mu_0 m/(4\pi R^{3}) = 30936.2$ nT:

| $\lambda$ | $\sin^{2}\lambda$ | $\sqrt{1+3\sin^{2}\lambda}$ | $B$ (nT) | $\tan I = 2\tan\lambda$ → $I$ (deg) |
|---|---|---|---|---|
| $0^\circ$ | 0 | 1.0000 | 30936.2 | 0.00 |
| $20^\circ$ | 0.11698 | 1.1623 | 35957.1 | 36.05 |
| $70^\circ$ | 0.88302 | 1.9104 | 59096.0 | 79.69 |
| $90^\circ$ | 1 | 2.0000 | 61872.4 | 90.00 |

Polar/equatorial ratio $= 61872.4/30936.2 = 2.0000$ exactly, as the factor
$\sqrt{1+3\sin^{2}90^\circ} = \sqrt{4} = 2$ requires. **Both the ratio and the
inclination relation are consequences of the dipole assumption**; they are the
properties that make a palaeolatitude recoverable, and they fail by tens of degrees
where the real field's non-dipole part is large.

---

## ★6 — Heading against speed error at 40°N, 9 kn

$C_{\text{lin}}V\cos 40^\circ = 7.5028(9)(0.76604) = 51.72$ mGal per unit
$\sin\alpha$.

**(a)** Heading $\alpha = 30^\circ$, error $\delta\alpha = 2^\circ =
0.034907$ rad:

$$\delta E = 51.72\cos 30^\circ \times 0.034907 = 51.72(0.86603)(0.034907)
= 1.564\ \mathrm{mGal}.$$

**(b)** Speed error $0.2$ kn:

$$\delta E = 7.5028(0.2)\cos 40^\circ\sin 30^\circ
+ 2(0.004154)(9)(0.2) = 0.5748 + 0.0150 = 0.590\ \mathrm{mGal}.$$

**The heading error dominates** — by a factor 2.7 here. This is the general rule for
a linear term with a $\cos$ derivative: for small angle errors the heading
sensitivity is $\propto V\delta\alpha$ while the speed sensitivity is $\propto
\delta V\sin\alpha$, and near a diagonal heading ($\alpha\approx45^\circ$) both
factors are order one, so the heading term wins whenever the heading is known less
precisely than the speed in the ratio $\delta V/(V\delta\alpha)$.

---

## ★7 — Depth from zero crossings, and the peak

**(a)** The anomaly of a vertical dipole crosses zero where $x^{2} = 2d^{2}$, so the
crossings are at $\pm\sqrt{2}\,d$ and their separation is $2\sqrt{2}\,d$:

$$d = \frac{4500}{2\sqrt{2}} = 1590.99\ \mathrm{m} \approx 1.59\ \mathrm{km}.$$

**(b)** The peak is at $x = 0$:

$$B_a(0) = \frac{\mu_0 m}{4\pi}\frac{2d^{2}}{d^{5}}
= \frac{\mu_0 m}{4\pi}\frac{2}{d^{3}}
= (10^{-7})(3.0\times10^{10})\frac{2}{(1590.99)^{3}}$$

$$= 3000 \times \frac{2}{4.0271\times10^{9}} = 1.490\times10^{-6}\ \mathrm{T}
= 1490\ \mathrm{nT}.$$

**The assumption worth stating:** this is a *depth scale*, exact only for a
vertical, induced, point dipole. For a body of finite extent the answer lies between
the top of the body and its centre of mass, so the number is a bound on the top
depth rather than a measurement of it.

---

## ★★★8 — A survey with a sub-0.5 mGal Eötvös budget

**The requirement.** From Exercise ★6 the heading sensitivity at 10 kn on a
diagonal heading is about $C_{\text{lin}}V\cos\phi\cos\alpha$ per radian, which at
$45^\circ$N and $\alpha = 45^\circ$ is $7.5028(10)(0.7071)(0.7071) = 37.52$ mGal
per radian. For a $0.5\ \mathrm{mGal}$ allowance:

$$\delta\alpha \le \frac{0.5}{37.52} = 1.333\times10^{-2}\ \mathrm{rad}
= 0.764^\circ.$$

Similarly the speed term: $7.5028\cos45^\circ\sin45^\circ = 3.751$ mGal per knot,
so $\delta V \le 0.5/3.751 \times$ (allowing half the budget) $= 0.067$ kn
$= 0.034\ \mathrm{m\,s^{-1}}$.

**How to achieve it.**

1. **Reciprocal headings.** Steam every line twice in opposite directions and
   average. The linear term is antisymmetric under reversal and cancels to first
   order, so the *residual* (dominated by the $V^2$ term, which is $0.415$ mGal at
   10 kn) is what remains. This alone meets the budget and is why the requirement
   on $\delta\alpha$ can then be relaxed by an order of magnitude.
2. **Heading from GNSS**, not from a gyrocompass, at a sampling rate higher than
   the swell period, so that the $\delta\alpha$ above is achievable in the average.
3. **Speed from GNSS**, since a log measures speed through water, not over ground,
   and the Eötvös term depends on the latter.
4. **Steer away from diagonals where possible.** The linear term vanishes on
   north–south lines, so a grid oriented north–south has a much smaller Eötvös
   error than one oriented diagonally, and for the same heading accuracy the budget
   is met with room to spare.

**The residual that geometry cannot remove.** The $V^{2}$ term. It is
heading-independent, always positive, and therefore does not cancel under
reciprocal-heading averaging. It is known to the accuracy of the speed, so its
residual is $2C_{\text{quad}}V\delta V = 2(0.004154)(10)(0.067) = 0.0056$ mGal — 
negligible — **but it is a bias rather than a noise**, and a survey that reports a
"regional trend" must be sure the trend is not a speed variation along the line.

---

## ★★★9 — Detecting a wrong magnetisation direction in an RTP grid

**Mathematical form of the distortion.** Let the true magnetisation direction have
declination $D$ and inclination $I$, and let the reduction assume $(D', I')$.
Reduction to the pole is a linear filter in the wavenumber domain, applied to the
observed total-field anomaly $F$:

$$\mathrm{RTP} = \mathcal{F}^{-1}\!\left[\frac{\left|\mathbf{k}\right|^{2}}
{\left(\hat{\mathbf{m}}\cdot\mathbf{k}\right)\left(\hat{\mathbf{f}}\cdot\mathbf{k}\right)}
\mathcal{F}[F]\right],$$

where $\hat{\mathbf{f}}$ is the direction of the inducing field and
$\hat{\mathbf{m}}$ that of the magnetisation. If the assumed $\hat{\mathbf{m}}'$
differs from the true $\hat{\mathbf{m}}$, the applied filter differs from the
required one by a factor that is **antisymmetric in the horizontal wavenumber
components**:

$$\frac{H'}{H} = \frac{\left(\hat{\mathbf{m}}\cdot\mathbf{k}\right)
\left(\hat{\mathbf{f}}\cdot\mathbf{k}\right)}
{\left(\hat{\mathbf{m}}'\cdot\mathbf{k}\right)\left(\hat{\mathbf{f}}\cdot\mathbf{k}\right)}
= \frac{\hat{\mathbf{m}}\cdot\mathbf{k}}{\hat{\mathbf{m}}'\cdot\mathbf{k}},$$

which has the form $\frac{a k_x + b k_y + c k_z}{a' k_x + b' k_y + c' k_z}$. A
wrong direction therefore applies a **skew** to the anomaly: the linear term
$k_x, k_y$ in the denominator multiplies the spectrum by a factor that is odd in
$k_x$ and $k_y$, which by the Fourier shift theorem **displaces the anomaly
horizontally** and makes it asymmetric, with a tail on one side.

**The observable that a wrong direction distorts.** The **centre of mass of the
anomaly relative to independent evidence for the body's position** — the
bathymetry, a seismic horizon, or the body's own gravity anomaly. A correct RTP
places a compact, symmetric anomaly over the body; a wrong assumed direction
displaces and skews it, and the displacement is proportional to the source depth,
which makes deep bodies the most sensitive test.

**A practical test.** Take a set of isolated anomalies whose bodies are located
independently (by bathymetry, say). Compute the horizontal offset between each
anomaly's centre of mass and its body for a range of assumed $(D', I')$, and choose
the direction that minimises the offsets across the set. Three or more isolated
bodies at different depths make the estimate well posed; one body cannot, because a
depth change and a direction change are partly degenerate. A complementary test is
**symmetry**: for a compact isolated source, a correct reduction makes the anomaly
radially symmetric to the first order, and a wrong direction makes it not.

**Why this matters.** Remanence is common in oceanic basalts, and the reduced grid
is used for structural interpretation and for estimating magnetisation intensity.
A skewed RTP grid puts anomalies in the wrong place and biases every depth estimate
made from it, with no internal signature that the direction was wrong.
