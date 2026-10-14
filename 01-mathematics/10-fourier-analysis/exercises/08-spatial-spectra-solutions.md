# Solutions — 01-10-08 Power Spectra, Admittance and Coherence of Geophysical Fields

> **Read this after attempting the exercises, not before.**
>
> All values below were computed. Values quoted from the supplied script are the
> values it printed.

---

## ★1 — Scatter of a spectral estimate

**(a)** $5.57$ dB, usually quoted as **5.6 dB**. It is independent of the record
length and of the shape of the spectrum, because each periodogram ordinate is a
$\chi^2_2$ variable whose standard deviation equals its mean.

**(b)** Using $\sigma = 4.3429\sqrt{\psi'(K)}$:

| $K$ | $\psi'(K)$ | exact (dB) | $5.6/\sqrt{K}$ (dB) |
|---|---|---|---|
| 4 | 0.2838 | 2.314 | 2.80 |
| 100 | $\approx 0.0100$ | $\approx 0.435$ | 0.56 |

(For $K = 100$, $\psi'(100) = \sum_{n\ge0}(100+n)^{-2} \approx 0.01$ to three
figures.)

The approximation is accurate at $K = 1$ and increasingly pessimistic as $K$
grows: it overestimates the scatter by 21% at $K = 4$ and by about 30% at
$K = 100$. Use the exact expression when the number matters.

**(c)** **Resolution.** Averaging $K$ segments gives a record of length
$T/K$ each, so the frequency resolution of the averaged estimate is $K/T$ rather
than $1/T$: a factor $K$ coarser, and it cannot be recovered by padding
([01-10-04](../04-discrete-fourier.md)).

---

## ★2 — A PSD and its integral

**(a)** $P = 2\lvert X\rvert^{2}dt/N = 2\times400\times1/1000 = \boxed{0.8}$ in
units of (signal)²/Hz — for a dimensionless signal, 0.8 per second.

**(b)** $df = 1/(N\,dt) = 1/1000 = \boxed{1.0\times10^{-3}}$ Hz.

**(c)** If only that one bin were non-zero, the series would be a sinusoid at
$f = k\,df$ with mean square $= \frac12 A^2$, where
$\lvert X\rvert = A\,N/2$ gives $A = 2\times20/1000 = 0.04$ and so the variance is
$0.04^{2}/2 = 8.0\times10^{-4}$.

The PSD integral gives $P\,df = 0.8\times10^{-3} = 8.0\times10^{-4}$ ✓. The two
agree exactly, which is the check that the $1/N$, the $dt$ and the factor 2 have
all been placed correctly. **This check takes one line and catches the three
classic errors at once.**

---

## ★3 — Definitions

With $x$ and $y$ the two real zero-mean fields on the same grid, $X$ and $Y$
their transforms over a band,

$$Z(f) = \frac{S_{xy}}{S_{xx}}
= \frac{Y\overline{X}}{\lvert X\rvert^{2}}
\qquad\text{[units of }y\text{ per unit }x\text{]},$$

$$\gamma^2(f) = \frac{\lvert S_{xy}\rvert^{2}}{S_{xx}S_{yy}}
\qquad\text{[dimensionless, }0\le\gamma^2\le1\text{]}.$$

For gravity in m s$^{-2}$ and topography in metres, $Z$ has units of
**m s$^{-2}$ per metre**, i.e. acceleration per unit height. It is convenient to
convert to the conventional gravity unit: with
$1\ \mathrm{mGal} = 10^{-5}$ m s$^{-2}$,

$$Z\ \text{in mGal/m} = Z\ \text{in (m s}^{-2}\text{)/m} \times 10^{5}.$$

The classic long-wavelength limit $2\pi G\rho = 1.12\times10^{-6}$ (m s$^{-2}$)/m
is therefore $0.112$ mGal/m — a useful number to carry in your head, because it is
the Bouguer-slab admittance.

---

## ★4 — Uncompensated admittance at three wavelengths

$Z(k) = 2\pi G\rho e^{-kd}$ with $2\pi G\rho = 1.1196\times10^{-6}$
(m s$^{-2}$)/m and $d = 4000$ m:

| wavelength (km) | $k = 2\pi/\lambda$ (rad/m) | $kd$ | $e^{-kd}$ | $Z$ ((m s$^{-2}$)/m) | $Z$ (mGal/m) |
|---|---|---|---|---|---|
| 100 | $6.283\times10^{-5}$ | 0.2513 | 0.7777 | $8.71\times10^{-7}$ | 0.0871 |
| 20 | $3.142\times10^{-4}$ | 1.2566 | 0.2846 | $3.19\times10^{-7}$ | 0.0319 |
| 10 | $6.283\times10^{-4}$ | 2.5133 | 0.0810 | $9.07\times10^{-8}$ | 0.0091 |

**Read the trend.** The admittance falls by a factor of 2.7 going from 100 km to
20 km and by a further 3.5 going to 10 km. This exponential attenuation with
wavelength is why the short-wavelength end of any real admittance estimate is
unreliable: the gravity signal there is small, while the measurement noise is not.

---

## ★★5 — Two estimators and the coherence

**(a)**

$$Z = \frac{\lvert S_{xy}\rvert}{S_{xx}} = \frac{1.6\times10^{-3}}{4.0\times10^{4}}
= \boxed{4.0\times10^{-8}\ \text{(m\,s}^{-2}\text{)/m}},$$

$$A = \sqrt{\frac{S_{yy}}{S_{xx}}}
= \sqrt{\frac{1.6\times10^{-7}}{4.0\times10^{4}}}
= \sqrt{4.0\times10^{-12}} = \boxed{2.0\times10^{-6}\ \text{(m\,s}^{-2}\text{)/m}} .$$

**(b)**

$$\gamma^2 = \frac{\lvert S_{xy}\rvert^{2}}{S_{xx}S_{yy}}
= \frac{(1.6\times10^{-3})^{2}}{4.0\times10^{4}\times1.6\times10^{-7}}
= \frac{2.56\times10^{-6}}{6.4\times10^{-3}} = \boxed{4.0\times10^{-4}} .$$

**(c)** A coherence of $4\times10^{-4}$ says the two fields are essentially
unrelated in this band, so **neither estimator should be reported as a measurement
of a transfer function**. The one to quote is the least-squares form
$\lvert S_{xy}\rvert/S_{xx}$, together with the coherence and the band. Note also
the inequality of ★★8: with $\gamma^2 \ll 1$ the amplitude ratio is expected to be
far larger than the least-squares estimate, and indeed
$2.0\times10^{-6}/4.0\times10^{-8} = 50$, i.e.
$1/\sqrt{\gamma^2} = 50$ — exactly the factor the Cauchy–Schwarz relation
predicts. **A ratio of 50 between the two estimators is not a discrepancy; it is a
coherence measurement.**

---

## ★★6 — Why a per-bin coherence is 1

A single frequency bin contains one complex number for each field. Its coherence
is $\lvert Y\overline X\rvert^{2}/(\lvert X\rvert^{2}\lvert Y\rvert^{2})$, which is
algebraically equal to 1 for any non-zero $X$ and $Y$: with one complex degree of
freedom the two fields can always be related by a single complex constant, so the
"fit" is exact and the coherence is 1 — it carries *no information at all* about
the relationship.

For 36 *independent* bins of unrelated data, each bin still has coherence 1 and
the average of 36 ones is 1 — the naive answer. But if the 36 complex cross-
products are *summed first* (which is what band averaging means), the sum of 36
independent random vectors has a magnitude of order $\sqrt{36} = 6$ times the
magnitude of a single one, while the auto-spectra sum to 36 terms. So

$$\gamma^2 \sim \frac{36}{36\times36} = \frac{1}{36} = 0.028,$$

i.e. the expected coherence of unrelated data over $M$ bins is approximately
$1/M$, not zero. That is the upward bias referred to in the lesson: with one or
two bins per band, even unrelated fields appear coherent. The practical rule
follows: **use bands with enough bins that $1/M$ is well below the coherence you
intend to interpret** — a band of 9 bins can never demonstrate a coherence below
about 0.11.

---

## ★★7 — Segment averaging

**(a)** Each segment is $4096/16 = 256$ samples = **256 s** long, so the averaged
estimate has a resolution of $1/256 = 3.91\times10^{-3}$ Hz.

**(b)** Without averaging the resolution would have been
$1/4096 = 2.44\times10^{-4}$ Hz — sixteen times finer.

**(c)** From the exact expression with $K = 16$, $\psi'(16) = 0.0640$, so

$$\sigma = 4.3429\sqrt{0.0640} = \boxed{1.10\ \mathrm{dB}} per bin.$$

**(d)** A peak narrower than the averaged resolution is **smeared**: it will
appear as a single broad bump of width $\approx 3.9\times10^{-3}$ Hz centred on the
true frequency, with its peak *height* reduced (by roughly the ratio of the true
width to the resolution width, when the true feature is a resolved line). The
frequency of the peak is still located correctly to within the resolution, and the
total power in the bump is preserved — which is why a line that appears in a
fine-resolution spectrum and vanishes when segments are averaged has not been
"removed", only diluted, and why the resolution of any reported spectrum must
accompany it.

---

## ★★8 — The Cauchy–Schwarz inequality

By Cauchy–Schwarz applied to the averaged spectra,

$$\lvert S_{xy}\rvert^{2} \le S_{xx}S_{yy}
\qquad\Longrightarrow\qquad
\frac{\lvert S_{xy}\rvert}{S_{xx}} \le \frac{\sqrt{S_{xx}S_{yy}}}{S_{xx}}
= \sqrt{\frac{S_{yy}}{S_{xx}}} ,$$

which is the stated inequality. Equality holds precisely when
$\lvert S_{xy}\rvert^{2} = S_{xx}S_{yy}$, i.e. when the coherence is 1: the two
fields are related by a single complex constant in that band, so the least-squares
fit is perfect and the amplitude ratio (which ignores phase) agrees with it.

**Consequence in practice.** The ratio of the two estimators is a direct measure of
the coherence:

$$\frac{\sqrt{S_{yy}/S_{xx}}}{\lvert S_{xy}\rvert/S_{xx}}
= \frac{\sqrt{S_{xx}S_{yy}}}{\lvert S_{xy}\rvert} = \frac{1}{\gamma} .$$

So a factor of 2 between the two estimators means $\gamma^2 = 0.25$: the
amplitude-ratio admittance is $1/\gamma$ times too large, which is the bias
referred to throughout the lesson. This identity is worth remembering: it means
that the two estimators' disagreement *is* the coherence, and it converts the
"which estimator" question into the "what is the coherence" question.

---

## ★★★9 — Reading the demo's tables

**(a)** Geometric-mean error factors over the bands whose coherence reaches 0.5:

| noise / signal | bands used | error of $\lvert S_{xy}\rvert/S_{xx}$ | error of amplitude ratio |
|---|---|---|---|
| 0.00 | 12 | 1.138× | 1.186× |
| 0.25 | 6 | 1.324× | 1.406× |
| 1.00 | 5 | 1.720× | 1.727× |

Both estimators degenerate as the noise grows, and the amplitude ratio is
consistently the worse of the two — the bias of ★★8, now visible as a systematic
error factor.

**(b)** The threshold restricts the reported statistics to bands with
$\gamma^2 \ge 0.5$. Raising the noise lowers the coherence in *every* band, so
bands drop out of the selection from the short-wavelength end, where the gravity
has been attenuated most. Hence the count falls 12 → 6 → 5 as the noise rises.
This is not a defect of the analysis; it is the analysis telling you which parts
of the spectrum the data actually determine.

**(c)** At noise/signal $= 0.25$:

| wavelength (km) | coherence | $\lvert S_{xy}\rvert/S_{xx}$ | amplitude ratio | true $Z$ | ratio to true |
|---|---|---|---|---|---|
| 25.6 | 1.0000 | $5.067\times10^{-7}$ | $5.067\times10^{-7}$ | $4.195\times10^{-7}$ | 1.208 |
| 14.2 | 0.3887 | $2.162\times10^{-7}$ | $3.468\times10^{-7}$ | $1.913\times10^{-7}$ | 1.130 |
| 5.6 | 0.2081 | $4.988\times10^{-7}$ | $1.093\times10^{-6}$ | $1.224\times10^{-8}$ | 40.749 |

- **25.6 km:** coherence 1, the two estimators identical, and the measured
  admittance within 21% of the truth. This row is determined by the data, and the
  21% is the finite-band scatter of a single realisation.
- **14.2 km:** coherence 0.39 — the two estimators differ by a factor of 1.6,
  which by ★★8 corresponds to $\gamma = 1/1.6 = 0.62$, consistent with
  $\gamma^2 = 0.39$ ✓. The least-squares estimate is still within 13% of the truth,
  while the amplitude ratio is 81% high. **The least-squares estimator is
  doing its job; the amplitude ratio is failing.**
- **5.6 km:** coherence 0.21, and the least-squares estimate is a factor of 41 from
  the truth — the gravity there is
  $e^{-2\pi(0.178)(4)} = 0.011$ of the long-wavelength value, i.e. below the noise.
  Neither number is a measurement of a transfer function.

**(d)** Two reasons the true uncertainty on a coherence of 0.9 is larger than the
36-bin count suggests.

1. **The bins are not independent.** A 128 km profile at any reasonable sampling
   has a *correlation length* set by the band and by the window, so the effective
   number of independent estimates is the number of *resolution widths* in the
   band, not the number of transform bins. A 4-bin band of a 128 km profile may
   contain only one independent estimate, in which case the bias is $1/M \approx 1$
   and the "coherence" is meaningless. The rule of thumb is that the effective
   count is the band width divided by the resolution $1/T$, summed over
   independent *segments*.
2. **There is only one realisation.** A single 128 km profile provides one draw of
   the field, so any spectral quantity is a single-sample estimate of a random
   variable. The scatter is not reduced by finer binning or by zero padding, only
   by averaging over independent pieces of the field — which requires either a
   larger area or a longer record.

**How to improve it:** use several overlapping segments of a larger area (or of a
set of parallel profiles), average the *spectra* over both segments and bands
before forming the ratios, and report the number of degrees of freedom (the total
effective number of independent spectral estimates) with the result. A multitaper
estimate is the standard refinement: several orthogonal tapers applied to the same
record give several nearly independent spectral estimates without shortening the
record, which is precisely the trade that plain segmentation cannot avoid.

---

## ★★★10 — Designing an admittance study

**(a)** Conventionally **$x$ = bathymetry (or topography)** as the independent
variable and **$y$ = gravity** as the dependent one, because the estimator
$Z = S_{xy}/S_{xx}$ is the regression of $y$ on $x$: it minimises the misfit in
*gravity* for a given topography. The choice matters because the two regressions
give different answers whenever there is noise: regressing gravity on topography
is the right choice when the errors are (mostly) in the gravity, which for
satellite-derived gravity over well-surveyed bathymetry is the usual situation.
If the bathymetry were the noisy one, the roles should be reversed or a total
least-squares estimator used — and the choice must be stated, because it changes
the numbers.

**(b)** The area is 1000 km across, so the fundamental wavenumber is
$1/1000\ \text{km}^{-1}$ and the wavelength range 200–20 km corresponds to
harmonic numbers 5 to 50 — about **46 independent bins** in the radial sense, but
far fewer in *bands*: with logarithmic bands four bins wide, on the order of
$46/4 \approx 11$ bands, and if the useful range narrows to 100–20 km, only about
5. So the achievable scatter on $Z$ is set by a small number of bands, not by the
size of the grid: **the stability of the estimate is limited by the area, not by
the resolution of the grid.** This is the two-dimensional version of the
resolution/averaging trade of Section 2.2.

**(c)**
- **Detrending:** remove a best-fit plane (and, for a large area, a low-order
  polynomial or the long-wavelength part of the gravity already removed by the
  satellite model). Reason: a trend leaks as $1/f$ across the spectrum
  ([01-10-05](../05-windowing-aliasing.md) Section 3.3), which would dominate the
  longest wavelengths in the useful band.
- **Window:** a Hann or a multitaper sequence. Reason: the field is not periodic
  over the area, so a hard edge leaks into the entire band; a taper cuts the edge
  amplitude by roughly the factor the lesson measured (about 40% in the 1-D
  example) and confines the residual ringing to the taper zone.
- **Padding:** zero-pad to the next convenient length if using an FFT. Reason: the
  bin spacing becomes $1/(N_{\text{pad}}dx)$ so peaks are located precisely, with
  the caveat that padding does not improve the resolution — which remains
  $1/L$ from the window length.

**(d)** Expect the coherence to fall below 0.5 at the **short-wavelength end**, in
the range where the gravity has been attenuated by $e^{-kd}$ below the noise of
the satellite-derived field, typically some tens of kilometres for a
several-kilometre-deep load. Because the coherence is the fraction of gravity
power explained by the load, once it falls below the chosen threshold the
admittance is no longer a measurement of a transfer function and the reported
result must stop there. The threshold therefore *defines* the short-wavelength
limit of the reported result, and the threshold, the band edges and the coherence
values must all be stated.

**(e)** In the order a reader would want them:

1. The admittance $Z(f)$ with its uncertainties, plotted or tabulated against
   wavelength or wavenumber.
2. The coherence $\gamma^2(f)$ on the same axis.
3. The band edges (or band centres and widths) used, and the coherence threshold
   applied.
4. The window(s) used, the detrending applied, the number of independent segments
   or tapers, and hence the number of degrees of freedom.
5. The wavenumber range over which the estimate is reported as a result, with the
   explicit statement that outside it the coherence is too low for the transfer
   function to be determined.
6. The intercept or long-wavelength limit of the model fitted to $Z$ (for
   example the best-fitting $2\pi G\rho$ and $d$, or the flexural parameters), and
   the range over which the model was fitted.
7. Any residual systematics the authors are aware of — an unmodelled density
   contrast, sediment thickness, or a regional gravity field not removed — because
   these dominate the systematic error budget even when the random error is small.
