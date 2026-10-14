# Solutions — 05-01-04 Non-Uniqueness of Geophysical Models

> Numbers marked *verified* were computed.

---

## ★1

The forward operator is a smoothing integral, so it has a null space: distinct
source distributions exist that produce identical fields, and a finite data set
contains fewer numbers than a continuous model has degrees of freedom.

---

## ★2

$\{\mathbf{n} : \mathbf{G}\mathbf{n} = \mathbf{0}\}$. A null vector can be
added to any model without changing the data at all, so the data cannot
distinguish the two models. Interpretation must therefore be built on priors
and regularisation, not on the data fit alone.

---

## ★3

$\hat{g}_z(k) = 2\pi G\,e^{-|k|d}\,\hat\sigma(k)$. The depth enters only through
$e^{-|k|d}$; $|k|d$ is dimensionless.

---

## ★★4 *(verified)*

$\hat\sigma_2(k) = \hat\sigma_1(k)\,e^{-|k|(d_1-d_2)}$, so with
$\Delta d = 300$ m and $\lambda = 1000$ m, $|k| = 2\pi/1000 = 6.283\times10^{-3}$
rad/m and

$$e^{-|k|\Delta d} = e^{-6.283\times10^{-3}\cdot300} = e^{-1.885} = 0.1519.$$

The shallower sheet ($d_2 = 100$ m) has the smaller high-wavenumber content, so
**the shallower equivalent is broader**.

---

## ★★5

Null-space dimension $\ge 600 - 150 = 450$. It is only a bound because the rank
could be less than 150 if rows are dependent.

---

## ★★6

Going deeper needs the inverse filter $e^{+|k|\Delta d}$, which amplifies high
wavenumbers without bound. Any noise or round-off at high $k$ is amplified by
this factor, so the deeper model oscillates with enormous amplitudes while
still fitting the data. Only the downward direction is unstable; upward
(shallower) continuation is stable.

---

## ★★7

Any three of: (i) independent information on depth (drill hole, seismic
horizon, magnetic depth estimate); (ii) a bound on the density contrast from
petrophysics or a cited range; (iii) the regularisation and its parameter
choice; (iv) the resolution matrix or a checkerboard test showing which cells
are constrained; (v) an estimate of geological noise; (vi) equivalent-source
tests at other depths. "It fits the data" is not on the list.

---

## ★★★8 *(verified)*

With 120 observations and 400 cells, all 120 singular values exceeded
$10^{-12}\sigma_\text{max}$, so the null-space dimension is at least 280. The
smallest-singular-value right vector gave

$$\frac{\lVert\mathbf{G}\mathbf{n}\rVert}{\sigma_\text{max}\lVert\mathbf{n}\rVert}
= 8.286\times10^{-17},$$

and adding $0.6\,\lVert m_\text{true}\rVert/\lVert n\rVert\cdot\mathbf{n}$
changed the computed field by a relative $1.311\times10^{-16}$ (machine
precision) while changing total mass by 0.002%. Conclusion: the data constrain
the *field*, and only through it a heavily smoothed functional of the source.
A large part of the model is invisible.

---

## ★★★9 *(verified)*

| depth (m) | $\mathrm{cond}(\mathbf{G})$ | model RMS (kg/m²) | data misfit |
|---|---|---|---|
| 50 | $3.33$ | $1.80\times10^{6}$ | $1.2\times10^{-15}$ |
| 100 | $1.56\times10^{1}$ | $1.90\times10^{6}$ | $1.2\times10^{-15}$ |
| 300 | $7.62\times10^{3}$ | $2.64\times10^{6}$ | $1.3\times10^{-15}$ |
| 600 | $8.11\times10^{7}$ | $6.83\times10^{9}$ | $2.1\times10^{-13}$ |
| 1200 | $8.27\times10^{15}$ | $5.66\times10^{14}$ | $1.0\times10^{-4}$ |

Round-off begins to degrade the fit around 1200 m, where the condition number
($10^{15}$) approaches the reciprocal of double-precision epsilon
($\approx 2\times10^{16}$): the high-wavenumber amplification can no longer be
represented. Prior information that would make a model defensible includes a
depth constraint from drilling, a density bound, a smoothness or compactness
prior, and a reported resolution matrix.

---

## ★★★10

A strong critique states: the inversion reproduces a *smoothed, band-limited
functional* of the subsurface, not the subsurface. Unconstrained are (at least)
absolute depth, the high-wavenumber content below the resolved band, and any
component in the null space. The regularisation — its norm, its weight, and the
criterion used to choose the weight — selected this particular member of the
equivalence class, so the answer is a statement about *model plus prior*, not
about the earth. Meaningful tests include: does the model change materially
when the regularisation weight is varied within the range that keeps the misfit
acceptable? Does an independent data set (seismic, drilling) agree? Does the
model predict a quantity that was not used in the inversion? A model that fails
the last test is a fit, not an interpretation.
---

## ★★★11

**The contour.** For $k>0$ the factor $e^{-ikx}$ decays as $\mathrm{Im}\,x\to
-\infty$, so close in the **lower** half-plane, clockwise, enclosing the simple
pole at $x = -id$. Writing the integrand as
$d/[(x-id)(x+id)]$, the residue at $x=-id$ is

$$\operatorname*{Res}_{x=-id}\frac{d}{(x-id)(x+id)}
= \frac{d}{-id-id} = \frac{i}{2},$$

and the exponential at the pole is $e^{-ik(-id)} = e^{-kd}$. Closing clockwise
contributes $-2\pi i$ times the residue, so
$I(k) = -2\pi i\cdot(i/2)e^{-kd} = \pi e^{-kd}$. For $k<0$ the same argument in
the upper half-plane gives $\pi e^{+kd}$, and the two combine to
$I(k) = \pi e^{-|k|d}$. With the factor $2G$:

$$\hat h(k) = 2\pi G\,e^{-|k|d}.$$

*Reasoning note: the sign of the closing direction and the sign of the
exponential must be checked together. A common error is to close in the upper
half-plane for $k>0$, which gives the wrong exponential and would predict
amplification instead of attenuation.*

**The tenth-amplitude wavelength.** Set $e^{-2\pi d/\lambda} = 0.1$:
$2\pi d/\lambda = \ln 10 = 2.3026$, so $\lambda_{10} = (2\pi/\ln 10)d = 2.7288\,d$.

**The comparison.** $w_{1/2} = 1.532842\,d$, so

$$\frac{\lambda_{10}}{w_{1/2}} = \frac{2.7288}{1.5328} = 1.780 .$$

**Why the ratio is more robust.** Both constants follow from the same kernel, so
their *ratio* is independent of $d$, of the source strength and of any amplitude
calibration — it depends only on the shape of the operator. A single constant,
by contrast, can be corrupted by an error in the assumed body shape (the half-width
constant is 1.533 for a sphere and 2.000 for a 2-D line), whereas the transfer
function's $2\pi/\ln 10$ is fixed by the Fourier transform alone. So the ratio
tests the *physics of the kernel*, and the individual constants test the *assumed
geometry* — different questions, and worth keeping apart.
