# Solutions — 08-03-03 Reduction to the Pole and Equator

> **Read after attempting the exercises.** The lesson is
> [03 Reduction to the Pole and Equator](../03-reduction-to-pole.md).

---

## ★1 — The filter and its singularity

$$\mathrm{RTP}(\mathbf{k}) = \frac{k^{2}}
{\hat{\mathcal{O}}_{\hat m}(\mathbf{k})\,\hat{\mathcal{O}}_{\hat f}(\mathbf{k})},
\qquad \hat{\mathcal{O}}_d = i\left(k_xd_x+k_yd_y\right) + k\,d_z .$$

At the equator with $\hat m = \hat f = \hat x$,
$\hat{\mathcal{O}} = ik_x$, so
$\mathrm{RTP} = k^{2}/\left(ik_x\right)^{2} = -k^{2}/k_x^{2}$. It is singular on
the line $k_x = 0$, i.e. along the $k_y$ axis, and it grows without bound as that
line is approached. Physically, the component of the anomaly that RTP must
amplify corresponds to structure whose wavevector is perpendicular to the
magnetisation.

---

## ★2 — The Poisson form

$$\Delta T = C\,m\left(\hat m\!\cdot\!\nabla\right)\left(\hat f\!\cdot\!\nabla\right)\frac{1}{r}.$$

The **depth** enters only through $r = \sqrt{x^{2}+y^{2}+z_0^{2}}$ (and hence
through the spectrum's $e^{-kz_0}$ factor); the **directions** enter only through
the two unit vectors $\hat m$ and $\hat f$. RTP removes the second without
touching the first, which is why it can move and rescale an anomaly but cannot
change its depth content.

---

## ★3 — The pole-equivalent anomaly

$$\Delta T = \frac{\mu_0}{4\pi}\frac{2m}{z^{3}}
= 1.0\times10^{-7}\times\frac{2\times2.00\times10^{9}}{(3.0\times10^{3})^{3}}
= 1.0\times10^{-7}\times\frac{4.00\times10^{9}}{2.70\times10^{10}}
= 1.4815\times10^{-8}\ \mathrm{T} = 14.815\ \mathrm{nT},$$

in agreement with the demonstration's printed $14.815$ nT.

---

## ★4 — Displacement with inclination

| $I$ | Displacement (km) |
|---|---|
| $45^\circ$ | 1.2 |
| $30^\circ$ | 2.0 |
| $15^\circ$ | 2.8 |

The displacement grows monotonically as the inclination falls. The explanation is
that the anomaly's phase — the part of $\mathrm{RTP}$ that is not a pure
amplitude — scales with the horizontal direction cosines of $\hat m$ and
$\hat f$, which vanish as $I\to0$; in the space domain that phase corresponds to
a spatial shift of the anomaly pattern away from the source. The shift is
bounded: for a dipole it never exceeds roughly one body depth.

---

## ★5 — Where RTP stops being usable

| $I$ | Gain | Noise in the RTP product (nT) | Peak/noise for a 5 nT target |
|---|---|---|---|
| $45^\circ$ | 1.44 | 0.288 | 17.4 |
| $20^\circ$ | 3.48 | 0.696 | 7.2 |
| $10^\circ$ | 8.93 | 1.786 | 2.8 |

With a $3\sigma$ detection convention the last row is unacceptable (peak
$<3\times$ the noise). The honest threshold for this survey is between $10^\circ$
and $20^\circ$: below about $15^\circ$ the RTP product at this noise level is no
longer interpretable without stabilisation. Note the arithmetic: the noise in the
product grows *linearly* with the gain, while the anomaly does not change, so the
signal-to-noise falls as $1/\text{gain}$.

---

## ★6 — What is preserved and what is not

RTP is a **linear, deterministic** operation: it converts one data set into
another deterministically, so the *position* and the *amplitude* of the
transformed anomaly are reproducible and correct — hence the $-0.09\%$ agreement.

What it does to noise is a different matter. The filter's RMS gain on white noise
is 1.44 at $I = 45^\circ$, so the noise power in the product is about twice the
noise power in the input, and the peak-to-background ratio falls from 91 to 12.9.
Both statements are true at once because RTP does not create or destroy
information: it redistributes the *signal* correctly and the *noise* unfavourably.
A map that looks like the geology and a signal-to-noise ratio that has fallen by
a factor of seven are the same transformation.

---

## ★★7 — Order of convergence

$$\frac{2.96\times10^{-2}}{8.66\times10^{-3}} = 3.42, \qquad
\frac{8.66\times10^{-3}}{2.37\times10^{-3}} = 3.65, \qquad
\frac{2.37\times10^{-3}}{6.21\times10^{-4}} = 3.82 .$$

Halving $h$ divides the error by a factor approaching 4, so the error is
$O\left(h^{2}\right)$: second-order convergence. This is the expected order for
central differences of a smooth function, and it is evidence that the identity is
correct rather than approximately self-consistent — a wrongly-stated identity
would converge to a *non-zero* residual.

---

## ★★8 — Experiment design (specification)

**Reference.** The pole-equivalent anomaly computed analytically for the true
induced magnetisation direction, on the same grid.

**Data.** The anomaly of that body, tapered and transformed with RTP using a
direction rotated by $30^\circ$ (keeping the *field* direction correct and
changing only the assumed magnetisation).

**Metric.** Two numbers: the maximum absolute difference between the
mis-reduced anomaly and the reference, as a fraction of the reference peak; and
the displacement of the peak from the source.

**Expected result.** The amplitude error is small (the projection factors are
similar) but the position error is large and *systematic*: the artefact is a
displaced, elongated anomaly. This is the signature of a wrong RTP assumption in
practice — not noise, but structure that should not be there.

---

## ★★9 — Why the taper

The 2-D spectrum of $1/r$ is $2\pi e^{-kz_0}/k$: it decays only as $1/k$, so the
sampled field has significant amplitude at the edges of any finite grid, and the
periodic extension that a discrete Fourier transform imposes has a
**discontinuity** there. A discontinuity produces broadband leakage — energy at
all wavenumbers, including the high ones where RTP amplifies — and the result is
a cross-shaped artefact pattern aligned with the grid axes.

A flat-top (Tukey) window removes the discontinuity while leaving the central
half of the grid untouched, so the answer is exact where it matters. The cost is
that the window convolves the spectrum with its own transform, so the long
wavelengths are slightly attenuated and the deepest structure is the first to be
affected. Both effects are measurable: the demonstration reports a composite
reconstruction error of $9.0\times10^{-3}$ of the peak, dominated by this finite
aperture.
