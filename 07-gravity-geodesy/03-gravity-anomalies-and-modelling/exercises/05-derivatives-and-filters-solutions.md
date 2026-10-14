# Solutions — 07-03-05 Derivatives, Upward/Downward Continuation and Euler Deconvolution

> **Read after attempting the exercises.** Numbers were computed. Lesson:
> [05 Derivatives and Filters](../05-derivatives-and-filters.md).

---

## ★1 — The operators

| operation | multiplier | units of the result for an input in mGal |
|---|---|---|
| $\partial/\partial x$ | $ik_x$ | $\mathrm{mGal\,m^{-1}}$ |
| $\partial/\partial z$ ( $z$ up) | $-k$ | $\mathrm{mGal\,m^{-1}}$ |
| upward continuation by $1\ \mathrm{km}$ | $e^{-k\times1000}$ | mGal |

For $k$ in $\mathrm{rad\,m^{-1}}$ — equivalently $2\pi/\lambda$ — the continuation
factor is dimensionless and the derivative gains one inverse length. Both are
illustrated in the demonstration, whose filter checks agree with the analytic
derivatives to $1.2\times10^{-16}$ (mGal/m) on a periodic grid.

---

## ★2 — Why the derivative filter is not compact

Multiplication by $|k|$ in the wavenumber domain corresponds, in space, to a
convolution kernel whose transform is $|k|$; that kernel is proportional to
$1/x^{3}$ (in 1-D) and decays only as a power, not exponentially. A filter with a
power-law tail has no finite support, so the derivative at a point depends on the
field at arbitrarily large distances. Practically, this is why derivative maps
have long-range edge effects and why the field must be padded and tapered before
an FFT.

---

## ★3 — Downward-continuation amplification

Station spacing $100\ \mathrm{m}$ gives a Nyquist wavelength $200\ \mathrm{m}$,
so $k_N = 2\pi/200 = 0.0314\ \mathrm{m^{-1}}$. Then

$$e^{k_N\Delta z} = e^{0.0314\times500} = e^{15.7} = 6.6\times10^{6}.$$

The reason is that the field decays upward as $e^{-kz}$, so recovering it at
depth means multiplying by the exact inverse $e^{+k\Delta z}$ — geometry, not a
numerical choice. The shortest wavelengths are attenuated most going up, so they
must be amplified most coming down.

---

## ★4 — Choosing a cutoff

Target wavelength $700\ \mathrm{m}$ gives $k = 2\pi/700 = 8.98\times10^{-3}
\ \mathrm{m^{-1}}$, well inside the Nyquist band. From the demonstration's table
(white noise $0.10\ \mathrm{mGal}$ on a $3.5\ \mathrm{mGal}$ field):

| cutoff (m) | total (mGal/m) | bias | noise |
|---|---|---|---|
| none | 0.002555 | 0.000000 | 0.002555 |
| 2000 | 0.005298 | 0.005297 | 0.000017 |
| 1000 | 0.000540 | 0.000533 | 0.000067 |
| 500 | 0.000276 | 0.000002 | 0.000275 |
| 300 | 0.000755 | 0.000000 | 0.000755 |

The signal wavelength ($700\ \mathrm{m}$) sits between the $500\ \mathrm{m}$ and
$1000\ \mathrm{m}$ cutoffs. **Choose $500\ \mathrm{m}$**: the bias at that cutoff
is $0.000002\ \mathrm{mGal/m}$ — negligible, because nothing in the *synthetic*
signal lives below $300\ \mathrm{m}$ — while the noise is
$0.000275\ \mathrm{mGal/m}$, a factor $9$ below the unfiltered value. A $1000\
\mathrm{m}$ cutoff would corrupt the $700\ \mathrm{m}$ signal
(bias $0.000533$, comparable to the signal's own short-wavelength content), and a
$300\ \mathrm{m}$ cutoff would pass essentially all the noise.

**Justification in one sentence:** choose the longest cutoff wavelength that is
still shorter than the shortest target wavelength, because the bias grows as real
content is removed while the noise falls only as the retained band.

---

## ★5 — Euler for a point mass

With $\Delta x = x-x_0$, $\Delta y = y-y_0$, $\Delta z = z_0$ (source below the
observer) the field $g = GM\Delta z\rho^{-3}$, with
$\rho^{2} = \Delta x^{2}+\Delta y^{2}+\Delta z^{2}$, is **homogeneous of degree
$-2$** in $(\Delta x,\Delta y,\Delta z)$: scaling all three by $\lambda$ gives
$\lambda^{-2}g$. Euler's theorem then gives

$$\Delta x\,g_x + \Delta y\,g_y + \Delta z\,\frac{\partial g}{\partial\Delta z}
= -2g .$$

Using $\partial g/\partial\Delta z = GM\left(\rho^{-3}
- 3\Delta z^{2}\rho^{-5}\right)$ and the gradients
$g_x = -3GM\Delta z\Delta x\rho^{-5}$,
$g_y = -3GM\Delta z\Delta y\rho^{-5}$:

$$\Delta x g_x + \Delta y g_y
= -3GM\Delta z\left(\rho^{2}-\Delta z^{2}\right)\rho^{-5},$$

and adding $\Delta z\,\partial g/\partial\Delta z$ gives
$GM\Delta z\rho^{-5}\left[-3\rho^{2}+3\Delta z^{2}+\rho^{2}-3\Delta z^{2}\right]
= -2GM\Delta z\rho^{-3} = -2g$ ✔.

Because the observer's vertical derivative is
$g_z = \partial g/\partial z = -\partial g/\partial\Delta z$, rearranging gives

$$x_0g_x + y_0g_y + z_0g_z + NB = xg_x + yg_y + Ng,$$

with $N = 2$ for a point mass and $B$ a background. Note the sign: in the final
equation the coefficient of $g_z$ is $+z_0$, which is what makes the recovered
depth positive. The demonstration verifies this by recovering
$(200,-300,800)\ \mathrm{m}$ with a residual of $4.5\times10^{-11}\ \mathrm{mGal}$.

---

## ★6 — The depth range from the structural index

From the lesson's table for the true depth $800\ \mathrm{m}$:

| $N$ | $z_0$ (m) |
|---|---|
| 0 | $-319.4$ (unphysical) |
| 1 | 442.4 |
| 2 | 800.0 |
| 3 | 1157.6 |

The *admissible* range, excluding the unphysical negative solution, is
$442$–$1158\ \mathrm{m}$ — a factor $2.6$. Reporting a single depth from a
guessed index is therefore an overclaim of that magnitude.

**Evidence to reject the wrong indices:**

1. **Residual.** $N = 2$ gives $4.5\times10^{-11}\ \mathrm{mGal}$; $N = 1$ and
   $N = 3$ give $9.1\times10^{-2}\ \mathrm{mGal}$ — nine orders of magnitude worse.
   The residual is the primary test.
2. **Consistency of $B$.** $N = 2$ returns $B = 0$ (no regional); the wrong
   indices require a background of $-0.51$ or $+0.17\ \mathrm{mGal}$, i.e. they
   absorb their misfit into a fictitious regional.
3. **Physical plausibility.** $N = 0$ returns a negative depth.
4. **Independent shape information.** The half-width rule
   ([01](../01-anomaly-interpretation.md)) gives an independent depth estimate
   once a body class is assumed, which either agrees with $N = 2$ or exposes a
   contradiction.

---

## ★7 — Maximum admissible continuation depth

Assume the noise is white with rms $\sigma_g = 0.03\ \mathrm{mGal}$ on a grid with
spacing $dx = 100\ \mathrm{m}$, so its spectrum is flat with variance per unit
wavenumber $\sigma_g^{2}/k_N$ over the band $0 \le k \le k_N$.

Downward continuation multiplies each wavenumber by $e^{k\Delta z}$; the amplified
noise rms is

$$\sigma_{\text{cont}} \approx \sigma_g
\sqrt{\frac{1}{k_N}\int_{0}^{k_N}e^{2k\Delta z}\,\mathrm{d}k}
= \sigma_g\frac{e^{k_N\Delta z}-1}{\sqrt{2\,k_N\,\Delta z}} .$$

Setting $\sigma_{\text{cont}} = 0.1\ \mathrm{mGal}$ (the stated tolerance) and
$\sigma_g = 0.03\ \mathrm{mGal}$ requires a noise gain of $3.33$, so

$$\frac{e^{k_N\Delta z}-1}{\sqrt{2k_N\Delta z}} = 3.33
\;\Longrightarrow\; k_N\Delta z \approx 2.4
\;\Longrightarrow\;
\Delta z = \frac{2.4}{0.0314} = \mathbf{76\ m}.$$

The maximum admissible continuation depth is therefore of order **$75\ \mathrm{m}$**
— much less than a naive "continue to the source depth" intuition suggests. The
result is governed by the *shortest* wavelength present, which is why the answer
depends on the grid spacing as much as on the noise: halving the spacing to
$50\ \mathrm{m}$ doubles $k_N$ and halves the admissible depth.

**Assumption stated:** white noise. If the noise is red — as gridded and levelled
data usually are — the amplification is smaller and the admissible depth larger;
a red-noise answer must therefore quote the measured spectrum, not a white-noise
formula.

---

## ★8 — Rejecting contaminated Euler windows

**Rejection criteria.**

1. **Residual threshold.** Accept a window only if the rms residual is below a
   stated multiple of the noise, e.g. $1.5\times$ the data noise ($\sim0.2\
   \mathrm{mGal}$ in the demonstration's units). The contaminated windows there
   have residuals of $0.17$–$0.41\ \mathrm{mGal}$ against $4.5\times10^{-11}$ for
   the isolated source — the separation is enormous.
2. **Background constraint.** Reject windows whose fitted $B$ exceeds a physically
   plausible regional range; a large $B$ is a symptom of multiple sources.
3. **Depth-sign and range check.** Reject negative or absurdly large $z_0$, and
   cross-check $z_0$ against the half-width estimate.
4. **Solution-cluster test.** Accept only windows whose estimated $(x_0,y_0,z_0)$
   agrees within a tolerance with the estimates from neighbouring windows;
   isolated outliers are window artefacts.

**Reporting.** Do not average the surviving estimates into one depth. Report a
**map**: for each accepted window, plot its estimated horizontal location with the
estimated depth as a symbol size or colour, and quote the modal depth and the
interquartile range of the accepted estimates as the answer. An alternative and
often clearer presentation is a histogram of $z_0$ over accepted windows with the
rejection threshold annotated, since the width of that distribution *is* the
achieved depth resolution — which, for the two-source example, is tens of metres
and contaminated towards the stronger body, exactly the honest result.
