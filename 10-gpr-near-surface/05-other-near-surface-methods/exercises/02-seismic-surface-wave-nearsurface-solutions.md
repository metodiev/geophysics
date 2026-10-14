# Solutions — 10-05-02 Surface-Wave Methods for Shallow Layers

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Reference values come from `code/surface_wave_demo.py`; the teaching model
> is $h = 5\ \mathrm{m}$, $\beta_1 = 180\ \mathrm{m\,s^{-1}}$,
> $\rho_1 = 1800\ \mathrm{kg\,m^{-3}}$ over $\beta_2 = 400\ \mathrm{m\,s^{-1}}$,
> $\rho_2 = 2000\ \mathrm{kg\,m^{-3}}$.

Lesson: [02 Surface-Wave Methods](../02-seismic-surface-wave-nearsurface.md).

---

## ★1 — Rayleigh speed at $\nu = 1/3$

$$\frac{\alpha}{\beta} = \sqrt{\frac{2(1-1/3)}{1-2/3}} = \sqrt{2} = 1.41421,$$

so $\eta^2 = 0.5$ and the sextic is
$\zeta^6 - 8\zeta^4 + 8(3-1)\zeta^2 - 16(0.5) = 0$. Its root in $(0,1)$ is

$$\zeta = 0.93252591, \qquad
c_R = 0.932526\times250 = 233.13\ \mathrm{m\,s^{-1}} .$$

The demonstration reports $\zeta = 0.93252591$ from both the determinant equation
and the sextic, and $c_R/\beta = 0.932526$. Note the ratio moves by only $2.3\%$
between $\nu = 0.20$ ($0.910996$) and $\nu = 0.40$ ($0.942195$): **the Rayleigh
speed is a weak function of Poisson's ratio**, which is why interpreting a
Rayleigh measurement as an S-wave velocity is a modest approximation rather than
a blunder.

---

## ★2 — Cut-off frequencies

$$\sqrt{\frac{1}{\beta_1^2}-\frac{1}{\beta_2^2}}
= \sqrt{4.4444\times10^{-5} - 8.1633\times10^{-6}}
= \sqrt{3.6281\times10^{-5}} = 6.0234\times10^{-3}\ \mathrm{s\,m^{-1}},$$

$$h\sqrt{\frac{1}{\beta_1^2}-\frac{1}{\beta_2^2}} = 3(6.0234\times10^{-3})
= 1.8070\times10^{-2}\ \mathrm{s},$$

$$f_{c,n} = \frac{n\pi}{1.8070\times10^{-2}} = n(173.86)\ \mathrm{Hz}:$$

| $n$ | $f_{c,n}$ (Hz) |
|---|---|
| 1 | 173.86 |
| 2 | 347.71 |
| 3 | 521.57 |

At $200\ \mathrm{Hz}$: $f_{c,1} < 200 < f_{c,2}$, so **two modes** propagate
(the fundamental and mode 1). At $400\ \mathrm{Hz}$: $f_{c,2} < 400 < f_{c,3}$, so
**three modes** propagate.

---

## ★3 — Why Rayleigh but not Love in a uniform half-space

The Rayleigh wave is the free-surface solution of the P–SV system: the two
evanescent potentials $\phi \propto e^{-qkz}$ and $\psi \propto e^{-skz}$ satisfy
the traction-free boundary conditions at one frequency-independent speed $c_R$.
The Love wave is an SH mode of a *layered* system: it exists only because total
internal reflection at the layer–half-space interface traps the motion, which
requires a slower layer above a faster half-space. With no interface there is
nothing to trap the motion.

---

## ★★4 — A root checked by hand at $32\ \mathrm{Hz}$

$$\omega = 2\pi(32) = 201.062\ \mathrm{rad\,s^{-1}},$$
$$k_1 = \omega\sqrt{\frac{1}{180^2}-\frac{1}{186.991^2}}
= 201.062\sqrt{3.08642\times10^{-5} - 2.86013\times10^{-5}}
= 201.062\,(1.50428\times10^{-3}) = 0.30257\ \mathrm{rad\,m^{-1}},$$
$$k_1h = 1.51285\ \mathrm{rad} = 86.68^\circ \in (0^\circ, 90^\circ)
\;\Rightarrow\; n = 0 \text{ (fundamental)},$$
$$k_2 = 201.062\sqrt{\frac{1}{186.991^2}-\frac{1}{400^2}}
= 201.062\sqrt{2.86013\times10^{-5}-6.25000\times10^{-6}} = 0.95053\ \mathrm{rad\,m^{-1}},$$
$$B = \frac{\mu_2k_2}{\mu_1k_1}
= \frac{(2000)(400^2)(0.95053)}{(1800)(180^2)(0.30257)}
= \frac{3.0417\times10^{8}}{1.7641\times10^{7}} = 17.237,$$
$$\tan(k_1h) = \tan(1.51285) = 17.237 .\;✔$$

The agreement is exact to the printed digits, which is why the demonstration's
residual for this root is $\sim10^{-11}$. Note $k_1h$ is close to $\pi/2$: the
$32\ \mathrm{Hz}$ point sits near the top of the fundamental branch, which is why
$c$ is already within $4\%$ of $\beta_1$.

---

## ★★5 — A 2% velocity change in the top metre

The measured fraction of the fixed-frequency kernel lying in the top 1 m is
$0.263$ at $16\ \mathrm{Hz}$ and $0.373$ at $64\ \mathrm{Hz}$ (from the
demonstration's table), and $\int K\,\mathrm dz = 0.6607$ and $0.5095$. Then

$$\frac{\delta c}{c}\bigg|_{16} = 2(0.02)\,(0.263)(0.6607) = 0.00694
= 0.69\%,$$
$$\frac{\delta c}{c}\bigg|_{64} = 2(0.02)\,(0.373)(0.5095) = 0.00761
= 0.76\%.$$

The two differ by only $10\%$ — far less than the factor of four in frequency —
because the two effects compete: the *relative* share of the kernel in the top
metre grows with frequency ($0.263 \to 0.373$) while the *total* sensitivity
$\int K\,\mathrm dz$ falls ($0.6607 \to 0.5095$). That cancellation is why a
narrow top layer is nearly equally visible across the band, and why detecting it
does not require the highest frequency available.

---

## ★★6 — A 5% velocity error and the thickness

From the measured table:

| assumed $\beta_1$ (m/s) | fitted $h$ (m), 4–16 Hz | fitted $h$ (m), 4–128 Hz |
|---|---|---|
| 171.00 ($-5\%$) | 4.576 ($-8.5\%$) | 4.534 ($-9.3\%$) |
| 189.00 ($+5\%$) | 5.469 ($+9.4\%$) | 5.515 ($+10.3\%$) |

A 5% velocity error becomes a $9$–$10\%$ thickness error, and the wide band
changes it by about one percentage point.

**Implication.** Widening the band does **not** fix a velocity/thickness
trade-off: the trade-off is between two parameters of the model, so it can only be
broken by measuring one of them independently (a borehole, a cross-hole
measurement, or a refraction $v_p$ with a density estimate). Bandwidth buys depth
resolution, not parameter separation.

---

## ★★★7 — Testing the ridge (specification)

**Data.** A phase-velocity dispersion curve with stated uncertainties, ideally
with two modes. The synthetic control is a dispersion curve generated from a
*known* two-layer model with the same frequency sampling and the same noise
statistics as the real data.

**Inversion.** A layer-over-half-space parameterisation, with a fixed-density
assumption stated explicitly, inverted by a global search (a grid over $h$ and
$\beta_1$ is sufficient in two dimensions) rather than a local gradient method —
otherwise the width of the valley is set by the optimiser, not by the data.

**Metric.** The admissible set: all $(h,\beta_1)$ whose RMS misfit is below the
level implied by the data uncertainties. Report its extent in $h$ (in metres) and
its correlation (or the slope of the ridge in the $(h,\beta_1)$ plane), not a
single best model.

**Control.** Run the identical pipeline on the synthetic control curve. If the
inversion does not recover the known model of the control to within the
predicted admissible set, the pipeline — not the prediction — is wrong.

**Falsification.** The prediction "the ridge is wide in the long-wavelength band"
is falsified if the admissible set for data dominated by long wavelengths is
narrower than that for data spanning the confining regime. Because the metric is
a *set width*, the test can fail in either direction, which is what makes it a
test rather than a demonstration.

---

## ★★★8 — A soft pocket at 2 m depth

**Estimate.** The perturbation is $\beta_1 \to 80\ \mathrm{m\,s^{-1}}$ over
$0.5\ \mathrm{m}$ inside an otherwise uniform $180\ \mathrm{m\,s^{-1}}$ layer, so
at constant density

$$\frac{\delta\mu}{\mu} = \frac{80^2-180^2}{180^2} = -0.8025\ \mathrm{(a\ 80\%
reduction)},$$

and $\delta c/c = \int(\delta\mu/\mu)K\,\mathrm dz \approx -0.8025
\int_{2.0}^{2.5} K\,\mathrm dz$. The kernel of the *reference* model is
concentrated near the surface: only $0.263$ of it lies in the top metre at
$16\ \mathrm{Hz}$ and the per-metre share falls with depth, so the $2.0$–$2.5\ \mathrm{m}$
interval carries a modest fraction. Taking the measured layer fraction
$0.994$ at $32\ \mathrm{Hz}$ as an upper bound over 0–5 m and distributing it
evenly gives an upper bound of roughly $0.10$ of the kernel in that half-metre,
hence $|\delta c/c| \lesssim 0.08$ — but the *correct* estimate requires the
kernel evaluated at the perturbed model, because a buried low-velocity zone
traps energy and concentrates the kernel on itself. The honest answer to a
point-perturbation question is therefore: evaluate $\int_{2.0}^{2.5}K\,\mathrm dz$
for the *perturbed* model numerically; the first-order estimate above is a lower
bound.

**Detectability.** A $1\%$ phase-velocity measurement would see a perturbation of
this size; the physics does not prevent it. What limits detection in practice is
that (i) the pocket changes $c$ by an amount comparable to the picking error of a
single trace, (ii) the inversion trade-off absorbs much of the perturbation into a
slightly faster layer above, and (iii) a $0.5\ \mathrm{m}$ feature at $2\ \mathrm{m}$
depth requires short wavelengths ($\lambda \lesssim 2\ \mathrm{m}$) and therefore
high frequencies, where attenuation and source coupling reduce the usable
signal. The practical limit is signal-to-noise at high frequency, not the kernel.
