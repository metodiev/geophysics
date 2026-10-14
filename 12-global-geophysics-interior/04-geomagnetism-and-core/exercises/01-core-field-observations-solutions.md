# Solutions — 12-04-01 Observations of the Core Field and Secular Variation

> Read after attempting the [exercises](./01-core-field-observations-exercises.md).
> Lesson: [01 Observations of the Core Field and Secular Variation](../01-core-field-observations.md).
> Numbers computed, not estimated. All models **SYNTHETIC**.

---

## ★1 — Dipole moment and tilt

$$M = \frac{4\pi a^3}{\mu_0}\sqrt{(g_1^0)^2 + (g_1^1)^2 + (h_1^1)^2},
\qquad \frac{4\pi a^3}{\mu_0} = 10^{7}\times(6.371\times10^6)^3
= 2.586\times10^{27}.$$

With $g_1^0 = -3.0\times10^{-5}\ \mathrm{T}$ and
$h_1^1 = +5.0\times10^{-6}\ \mathrm{T}$ in the root,

$$M = 2.586\times10^{27}\times\sqrt{9.00\times10^{-10} + 2.5\times10^{-11}}
= 2.586\times10^{27}\times3.0414\times10^{-5} = 7.865\times10^{22}\
\mathrm{A\,m^2}.$$

$$\theta_{\text{tilt}} = \arctan\frac{5.0\times10^{-6}}{3.0\times10^{-5}}
= \arctan(0.1667) = 9.46°.$$

Both are *derived* from the coefficients; the uncertainty of each is the
uncertainty of the degree-1 coefficients alone.

---

## ★2 — A pure axial dipole, and what a tilt does

For a pure axial dipole $B_r = 2g_1^0\cos\theta$ and
$B_\theta = g_1^0\sin\theta$ (with $a/r = 1$ at the surface).

- $\theta = 45°$: $B_r = 2(-30\,000)(0.7071) = -42\,426\ \mathrm{nT}$,
  $B_\theta = -21\,213\ \mathrm{nT}$. Down $= +42\,426$, north $= +21\,213$, so
  $F = 47\,434\ \mathrm{nT}$ and $I = \arctan(2) = 63.43°$ — the classic
  $\tan I = 2\tan\lambda$.
- $\theta = 90°$: $B_r = 0$, $B_\theta = -30\,000\ \mathrm{nT}$; down $= 0$,
  north $= +30\,000$, so $I = 0$ exactly.

With a tilt of 9.5°, the equator *of the dipole* is no longer the geographic
equator; moving 9.5° of latitude changes $\tan I = 2\tan\lambda$ from 0 to
$2\tan(9.5°) = 0.335$, i.e. $I \approx 18.5°$. A single site therefore cannot
locate the dipole axis without assuming the dipole is axial.

---

## ★3 — Decay time and its scaling

$$\eta = \frac{1}{\mu_0\sigma} = \frac{1}{4\pi\times10^{-7}\times5\times10^{5}}
= 1.5915\ \mathrm{m^2\,s^{-1}},$$

$$\tau = \frac{R^2}{\pi^2\eta} = \frac{(3.48\times10^6)^2}{9.8696\times1.5915}
= 7.707\times10^{11}\ \mathrm{s} = 24.4\ \mathrm{kyr}.$$

Scaling: $\tau \propto \sigma$ exactly (since $\eta \propto 1/\sigma$). Halving
the conductivity halves the decay time; this is why a decay time is a
conductivity measurement in disguise.

---

## ★★4 — Deriving the eigenvalue condition

Inside, $\mathbf{B} = \nabla\times\nabla\times(S\hat{\mathbf{r}})$ with
$S_{\text{in}} \propto j_l(kr)$; outside there is no current, so $\nabla^2 S = 0$
and $S_{\text{out}} \propto r^{-(l+1)}$ (the decaying solution; the growing
$r^{l}$ solution is rejected because it is not produced by the interior source).

Continuity of the normal component of $\mathbf{B}$ requires $S$ continuous;
continuity of the tangential $\mathbf{H}$ requires $\partial S/\partial r$
continuous. Writing $S_{\text{out}} = C r^{-(l+1)}$ and applying both at $r = R$:

$$C = B\,j_l(kR)\,R^{l+1},\qquad
C\left[-(l+1)\right]R^{-(l+2)} = B\,k\,j_l'(kR),$$

and eliminating $C/B$,

$$kR\,j_l'(kR) + (l+1)j_l(kR) = 0 .$$

With the recurrence $x j_l'(x) = l j_l(x) - x j_{l+1}(x)$,

$$l j_l(x) - x j_{l+1}(x) + (l+1)j_l(x) = 0
\;\Longrightarrow\;
(2l+1)j_l(x) = x j_{l+1}(x).$$

For $l = 2$ with $x = 4.49341$:

$$\tau = \frac{R^2}{\eta x^2} = \frac{1.211\times10^{13}}{0.7958\times20.191}
= 7.54\times10^{11}\ \mathrm{s} = 23.9\ \mathrm{kyr},$$

against 48.9 kyr for $l = 1$: a higher-degree mode decays twice as fast, because
the same sphere accommodates a shorter wavelength.

---

## ★★5 — Magnetic Reynolds number, twice

$\eta = 0.7958\ \mathrm{m^2\,s^{-1}}$ at $\sigma = 10^6\ \mathrm{S\,m^{-1}}$:

$$Rm = \frac{uR}{\eta} = \frac{10^{-3}\times3.48\times10^6}{0.7958} = 4373 .$$

At $\sigma = 10^5\ \mathrm{S\,m^{-1}}$, $\eta$ is ten times larger and
$Rm = 437$.

**Conclusion in both cases:** $Rm \gg 1$, so advection dominates diffusion and the
field is being carried by the flow faster than it can decay; neither conductivity
weakens the dynamo requirement.

Which is more sensitive to the conductivity? **Both scale as $\sigma$** —
$Rm \propto \sigma$ and $\tau \propto \sigma$ — so the sensitivities are identical
in relative terms. The *absolute* statement differs: at
$\sigma = 10^5\ \mathrm{S\,m^{-1}}$ the decay time is 244 kyr, still four orders
of magnitude shorter than the age of the field, so the conclusion is unchanged.

---

## ★★6 — The residual, and what it is a fraction of

$$\frac{2\,899}{42\,000} = 0.069 = 6.9\%.$$

The denominator is the rms field **of the full synthetic model**, evaluated on the
same grid — not the rms field of the Earth. The fraction is therefore a statement
about how much of that model's structure lies in the omitted degrees.

If the omitted degrees were crustal rather than core field, the fraction would be
larger at the same degree limit (crustal spectra are flatter, so more power sits
at high $l$), and — more importantly — it would not be reducible by better
measurements, because the crustal field is real signal, not noise. Separating the
two is a modelling decision based on their spatial and temporal statistics.

---

## ★★★7 — Inclination at the equator for a tilted dipole

Write the dipole with $g_1^1 = 0$ and $h_1^1 = M_{h}$, $g_1^0 = M_{0}$. At the
equator ($\theta = 90°$), $P_1^0 = \cos\theta = 0$ and $P_1^1 = \sin\theta = 1$, so

$$B_r = 2\left[g_1^0\cos\theta + h_1^1\sin\theta\,\sin\lambda\right]_{\theta =
90°} = 2h_1^1\sin\lambda,$$

$$B_\theta = -\left[g_1^0(-\sin\theta) + h_1^1\cos\theta\sin\lambda\right]
= g_1^0,\qquad B_\lambda = h_1^1\cos\lambda .$$

Hence down $= -B_r = -2h_1^1\sin\lambda$, north $= -B_\theta = -g_1^0$,
east $= B_\lambda = h_1^1\cos\lambda$, and

$$\tan I = \frac{-2h_1^1\sin\lambda}{-g_1^0} = 2\frac{h_1^1}{g_1^0}\sin\lambda .$$

With $h_1^1/g_1^0 = -1/6$ (a 9.46° tilt) the inclination runs from
$\arctan(0.333)$ to $\arctan(-0.333)$, i.e. **±18.4° around the equator**.

So a single equatorial site cannot measure the tilt: it measures one value of
$\tan I$ along a sinusoid whose amplitude and phase are two unknowns. At least
three well-distributed equatorial sites are needed to separate the tilt from the
longitude of the dipole axis.

---

## ★★★8 — Measuring the drift-recovery bias

**Synthetic data.** A Gauss-coefficient set with a chosen spectrum; impose a pure
rotation of the non-dipole coefficients by $\omega\Delta t$ (so the drift is exact
by construction); evaluate $B_\lambda$ on a latitude–longitude grid at two epochs.

**Estimator.** The shift $s$ minimising
$\sum_{i,j}\left[B_\lambda^{(2)}(\lambda_i) - B_\lambda^{(1)}(\lambda_i - s)\right]^2$
with periodic interpolation, converted to a rate $s/\Delta t$; repeat with a finer
latitude sampling and a finer shift grid to show the estimator itself has
converged.

**Quantity to report.** The *relative* bias
$\left(\hat\omega - \omega\right)/\omega$ as a function of the ratio of
non-dipole to dipole power. Prediction: the bias goes to zero as the dipole is
removed from the field, and grows as the dipole's share grows, because the
stationary part pulls the fitted shift toward zero. Reporting the bias curve, not
a single bias value, is what makes the result transferable to a real analysis in
which that ratio is uncertain.

---

## What a good answer looks like

Every part separated what is measured (a vector at a site), what is fitted (the
coefficients), and what is derived (the moment, the tilt, the decay time). No
decay time was quoted without its conductivity and no residual without its
denominator.
