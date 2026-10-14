# Solutions — 01-10-02 The Fourier Transform and Its Properties

> **Read this after attempting the exercises, not before.**
>
> All numbers below were computed, and the values quoted from the supplied
> script are the ones it printed.

---

## ★1 — The kernel and three Gaussians

The forward kernel is $e^{-2\pi i f t}$, i.e. the forward transform is

$$X(f) = \int x(t)e^{-2\pi i f t}\,dt .$$

Since $\mathcal F\{e^{-\pi t^2}\} = e^{-\pi f^2}$:

| signal | transform | which rule |
|---|---|---|
| $e^{-\pi t^2}$ | $e^{-\pi f^2}$ | self-reciprocal Gaussian |
| $e^{-\pi(t-3)^2}$ | $e^{-\pi f^{2}}e^{-2\pi i f\cdot3}$ | shift by $t_0 = 3$ |
| $e^{-\pi(2t)^2}$ | $\frac{1}{2}e^{-\pi(f/2)^2}$ | scaling with $a = 2$ |

**Check the scaling entry** by substituting $u = 2t$:
$\int e^{-\pi(2t)^2}e^{-2\pi ift}dt = \frac{1}{2}\int e^{-\pi u^2}e^{-2\pi i(f/2)u}du
= \frac12 e^{-\pi(f/2)^2}$ ✓.

**Note the pattern** worth remembering: a shift changes only the phase, a scaling
changes only the width and height, and neither changes the shape of a Gaussian's
magnitude spectrum. That is why a Gaussian is the ideal test pulse.

---

## ★2 — Boxcar of width 2 s

**(a)** $T = 2$ s and

$$X(f) = \int_{-1}^{1}e^{-2\pi ift}dt = \frac{\sin(2\pi f)}{\pi f}
= 2\,\mathrm{sinc}(2f).$$

**(b)**

| $f$ (Hz) | $X(f)$ |
|---|---|
| 0.00 | 2.00 |
| 0.25 | 1.27 |
| 0.50 | 0.00 |
| 0.75 | $-0.424$ |
| 1.00 | 0.00 |

Check the values: $X(0.25) = 2\sin(\pi/2)/(\pi/2) = 2\times0.63662 = 1.27324$;
$X(0.75) = 2\sin(3\pi/2)/(3\pi/2) = 2\times(-1)/4.71239 = -0.424413$ ✓. Note the
sign change: the sinc is negative between $f = 0.5$ and $1.0$ Hz, so the
transform is real but not positive.

**(c)** The zeros are at $f = n/T = 0.5n$ Hz: 0.5, 1.0, 1.5, … They occur because
the integral of a full cycle of a complex exponential over a period is zero:
when the boxcar contains an integer number of cycles of $e^{-2\pi ift}$, the
positive and negative halves of each cycle cancel exactly. This is the same
orthogonality that extracts Fourier coefficients in
[01-10-01](../01-fourier-series.md) — the boxcar's zeros are orthogonality seen
from the other side.

---

## ★3 — Properties applied to a Gaussian

**(a)** Linearity: $\mathcal F\{5e^{-\pi t^2}\} = 5e^{-\pi f^2}$.

**(b)** Modulation: $\frac12\left[e^{-\pi(f-5)^2} + e^{-\pi(f+5)^2}\right]$. The
spectrum is now two Gaussian bumps centred at $\pm5$ Hz.

**(c)** Shift: $e^{-\pi f^2}e^{-2\pi i f(0.25)} = e^{-\pi f^2}e^{-i\pi f/2}$. The
magnitude is unchanged; the phase is the linear ramp $-(\pi/2)f$, which at
$f = 4$ Hz is $-2\pi$, i.e. a full turn and no visible change — the classic
aliasing of phase information when a delay is an exact multiple of the period at
that frequency.

**(d)** Scaling with $a = 10$:
$\frac{1}{10}e^{-\pi(f/10)^2}$. The pulse is 10 times shorter in time and its
spectrum is 10 times wider and 10 times lower.

**Check (d) by area.** $\int X df$ equals $x(0)$ (the inverse transform at
$t = 0$), which is unchanged by scaling: $x(0) = 1$ either way. The transform
got wider and lower in exactly compensating proportion.

---

## ★4 — Derivatives in the transform domain

$$\mathcal F\left\{\frac{dx}{dt}\right\} = 2\pi i f\,X(f), \qquad
\mathcal F\left\{\frac{d^2x}{dt^2}\right\} = (2\pi i f)^2X(f) = -4\pi^2f^2X(f).$$

For a spatial field $g(x)$ with wavenumber $k$ in radians per metre
($k = 2\pi f$),

$$\frac{\partial g}{\partial x}\;\longleftrightarrow\; ik\,G(k), \qquad
\frac{\partial^2 g}{\partial x^2}\;\longleftrightarrow\; -k^2 G(k).$$

**Two consequences worth stating explicitly.**

1. The sign flip on the second derivative, $-k^2$, is why the Laplace equation
   $\nabla^2 g = 0$ becomes $-k^2G(k) = 0$ in the transform domain: a harmonic
   field has spectrum only at $k = 0$, i.e. it is a constant plus, in two
   dimensions, terms that are non-zero only where the horizontal and vertical
   wavenumbers cancel.
2. The factor $k^2$ is why second derivatives amplify short-wavelength noise so
   brutally: at a wavelength of 1 km, $k^2 = (2\pi/1000)^2 = 3.9\times10^{-5}$
   m$^{-2}$, while at 100 m it is $3.9\times10^{-3}$ — two orders of magnitude
   more amplification of whatever noise lives there.

---

## ★★5 — The central difference as a filter

**(a)** Sampling the operator on a continuum with step $h$,

$$\mathcal F\{(x(t+h)-x(t-h))/(2h)\}
= \frac{e^{2\pi ifh} - e^{-2\pi ifh}}{2h}X(f)
= \frac{i\sin(2\pi f h)}{h}X(f),$$

using $\sin\theta = (e^{i\theta}-e^{-i\theta})/(2i)$.

**(b)** The response vanishes where $\sin(2\pi f h) = 0$, i.e. at
$f = n/(2h)$. The first such frequency is

$$f_{\text{blind}} = \frac{1}{2h},$$

which is exactly the Nyquist frequency of a grid with spacing $h$. The stencil
is blind at its own Nyquist wavenumber — a fact worth remembering before
differentiating any gridded field.

**(c)** The ratio is $\sin(2\pi fh)/(2\pi fh)$:

| $f$ | $h$ | $2\pi fh$ | ratio | amplitude error |
|---|---|---|---|---|
| 30 Hz | 2 ms | 0.3770 | 0.976481 | 2.35% |
| 30 Hz | 4 ms | 0.7540 | 0.907909 | 9.21% |
| 60 Hz | 2 ms | 0.7540 | 0.907909 | 9.21% |

Notice the pattern: it is the product $fh$ that matters, not either factor alone
— 30 Hz with $h = 4$ ms is as bad as 60 Hz with $h = 2$ ms. This is why
differentiating a fine grid is preferred to differentiating a coarse one, and why
a "vertical derivative" map computed with a coarse stencil is systematically
deficient at short wavelengths.

**(d)** With $h = 100$ m, the blind frequency is $f = 1/(2\times100)$
= 0.005 cycles/m, i.e. a wavelength of 200 m. So at 1 Hz the operator is not
0.005 cycles/m — 1 Hz is not a spatial frequency at all — the relevant check is
the *product* $f h$ expressed in the correct units. If the "1 Hz" refers to
frequency in time and $h$ is a distance in metres, the two are not comparable and
the colleague has conflated temporal frequency with spatial frequency. The
substantive point: with $h = 100$ m the operator attenuates wavenumbers above
about 0.001 cycles/m (1 km wavelength) by more than 1%, and everything above
0.0025 cycles/m (400 m) by more than 3%. **Quote the stencil spacing next to any
derivative map.**

---

## ★★6 — Parseval with an exponential

**(a)**
$$\int_{-\infty}^{\infty}e^{-2\lvert t\rvert}dt = 2\int_0^{\infty}e^{-2t}dt = 1.$$

**(b)** Substituting $u = 2\pi f$, $df = du/(2\pi)$:

$$\int_{-\infty}^{\infty}\frac{4}{(1+(2\pi f)^2)^2}df
= \frac{4}{2\pi}\int_{-\infty}^{\infty}\frac{du}{(1+u^2)^2}
= \frac{2}{\pi}\cdot\frac{\pi}{2} = 1 .$$

**(c)** Parseval's relation, $\int\lvert x\rvert^2dt = \int\lvert X\rvert^2df$ —
verified here exactly rather than numerically, which is the useful way to check a
normalisation convention: pick a pair whose integrals are elementary and confirm
the two sides agree to the last digit. If they differ by $2\pi$, the convention
is not the one you think it is.

---

## ★★7 — Reading a DFT's zeroth bin

**(a)** $X_{\text{DFT}}[0] = \sum_n x_n = 12345.0$. The mean is

$$\bar x = \frac{12345.0}{24} = 514.375 .$$

**(b)** The integral over the record, by the rectangle rule, is

$$\int x\,dt \approx dt\sum_n x_n = 3600 \times 12345.0 = 4.4442\times10^{7}.$$

**(c)** $X(0) = \int_{-\infty}^{\infty}x(t)dt$; over a single 24-hour record it is
the same as (b) *provided the signal is negligible outside the record*:
$X(0) \approx 4.4442\times10^{7}$.

**(d)** The colleague has reported the **sum** of the samples and called it the
**transform at zero frequency**. The three quantities are

$$\underbrace{\sum_n x_n}_{\text{sum}} = 12345, \qquad
\underbrace{\frac{1}{N}\sum_n x_n}_{\text{mean}} = 514.375, \qquad
\underbrace{dt\sum_n x_n}_{\text{integral}} = 4.4442\times10^{7}.$$

They differ by $N = 24$ and by $dt = 3600$ respectively. Both factors are pure
bookkeeping and neither is physics; both are silent in a plot.

---

## ★★8 — The forward difference

**(a)**
$$\left\lvert\frac{e^{i\omega h}-1}{h}\right\rvert
= \frac{\lvert e^{i\omega h/2}\rvert}{h}\left\lvert e^{i\omega h/2}-e^{-i\omega h/2}\right\rvert
= \frac{2\lvert\sin(\omega h/2)\rvert}{h}.$$

**(b)** Since $\lvert\sin u\rvert < \lvert u\rvert$ for all $u \ne 0$, putting
$u = \omega h/2$ gives $2\lvert\sin(\omega h/2)\rvert/h < 2(\omega h/2)/h
= \omega$. Equality holds only at $\omega = 0$. So the forward difference always
*under*-estimates the derivative amplitude — it is a low-pass filter with no
frequency at which it is exact except DC.

**(c)** At $\omega h = \pi/2$: ratio $=2\sin(\pi/4)/(\pi/2) = 2(0.707107)/1.570796
= 0.900316$. At $\omega h = \pi$: ratio $= 2\sin(\pi/2)/\pi = 2/\pi = 0.636620$.
These are the values the supplied script prints for the forward difference at
$f = 1$ Hz and $f = 5$ Hz with $h = 0.1$ s.

**(d)** Write $e^{i\omega h}-1 = 2i\sin(\omega h/2)e^{i\omega h/2}$, so

$$\frac{e^{i\omega h}-1}{h} = \frac{2\sin(\omega h/2)}{h}\,e^{i\omega h/2},$$

which is $i\omega$ times
$\left[\frac{2\sin(\omega h/2)}{\omega h}\right]e^{i\omega h/2}$. The phase error
is therefore $\omega h/2$, growing linearly with frequency.

It matters more than the amplitude error for dipping events because a
frequency-dependent phase is a **time shift that varies with frequency**: the
operator delays high frequencies more than low ones, which is precisely the
definition of dispersion. Applying a one-sided difference to a dipping reflector
in a wavefield extrapolation therefore smears and rotates it, whereas an
amplitude-only error would merely dim it. This is the standard argument for
centred stencils (phase error zero, at the cost of a blind frequency) over
one-sided ones in migration.

---

## ★★★9 — Upward and downward continuation

**(a)** Above the observation plane the field is harmonic, so in the transform
domain each horizontal wavenumber $k$ must satisfy

$$\frac{d^2G}{dz^2} - k^2G = 0
\qquad\Longrightarrow\qquad G(k,z) = A(k)e^{-kz} + B(k)e^{+kz}$$

(the $z$ axis pointing up, $k = \lvert 2\pi f\rvert \ge 0$). Boundedness as
$z \to \infty$ forces $B = 0$, and matching $G(k,0) = G_0(k)$ gives

$$G(k,z) = G_0(k)e^{-kz}.$$

With $k = 2\pi f$ this is the stated factor $e^{-2\pi f z}$ for upward
continuation by $z$ ($f$ in cycles per metre). Note the physics in the choice of
sign: only the decaying solution is allowed, so upward continuation is always
stable.

**(b)** With $h = 1$ km, the factor is $e^{-2\pi/\lambda}$ where $\lambda$ is the
wavelength in kilometres:

| wavelength (km) | upward factor | downward factor (reciprocal) | 5 km downward |
|---|---|---|---|
| 100 | 0.9391 | 1.0648 | 1.3691 |
| 20 | 0.7304 | 1.3691 | 4.8105 |
| 10 | 0.5335 | 1.8745 | 23.1407 |
| 5 | 0.2846 | 3.5136 | 535.4917 |

**(c)** At 5 km wavelength, downward continuation by 5 km multiplies the spectrum
by $(3.5136)^{5} = 535.49$.

**(d)** Noise is amplified by the same factor as signal at the same wavelength,
so the ratio of noise to signal changes only through the *different* wavelength
content. Take the noise as white (constant spectral density) and the signal at
20 km wavelength with amplitude 2 mGal against noise of 0.02 mGal at that
wavelength — that is a signal-to-noise ratio of 100 at 20 km. Downward
continuation by 5 km amplifies everything at 20 km by 4.81, so the ratio there is
unchanged. The ratio *degrades* at shorter wavelengths, where the amplification
is larger: it falls by the factor
$e^{2\pi(5)(1/\lambda_{short} - 1/20)}$. Setting the ratio to 1 (noise equal to
signal at 20 km) gives

$$\frac{\text{amp}(\lambda)}{\text{amp}(20\ \mathrm{km})} = 100
\qquad\Longrightarrow\qquad
e^{2\pi\cdot5(1/\lambda - 1/20)} = 100,$$

$$2\pi\cdot5\left(\frac{1}{\lambda}-\frac{1}{20}\right) = \ln 100 = 4.6052
\;\Longrightarrow\;
\frac{1}{\lambda} - 0.05 = 0.14658
\;\Longrightarrow\; \lambda = \frac{1}{0.19658} = 5.09\ \mathrm{km}.$$

So after continuing down 5 km the noise reaches the level of the 2 mGal signal at
about 5 km wavelength; below that, the map is noise. Interpretation must be
restricted to wavelengths longer than roughly 5 km, and that limit must be stated
in the report.

**(e)** The two standard devices:

1. **A low-pass or band-limiting filter** applied before the continuation, with a
   cutoff chosen from the noise level and the depth exactly as in (d). This
   discards the wavelengths you could not interpret anyway.
2. **Regularised (stabilised) downward continuation**, in which the division by
   $e^{-kz}$ is replaced by $e^{-kz}/(e^{-2kz} + \epsilon^2)$ or an equivalent
   Wiener-style filter, so that the amplification saturates at $1/(2\epsilon)$
   instead of growing exponentially. This is the same water-level regularisation
   that [01-10-03](../03-convolution.md) applies to deconvolution, and it carries
   the same cost: a bias at the shortest retained wavelengths in exchange for a
   bounded noise gain.

---

## ★★★10 — The uncertainty relation for a Gaussian

**(a)** With $x(t) = e^{-\pi t^2}$, $\lvert x\rvert^2 = e^{-2\pi t^2}$, and

$$\int_{-\infty}^{\infty}e^{-2\pi t^2}dt = \frac{1}{\sqrt{2}},
\qquad
\int_{-\infty}^{\infty}t^2e^{-2\pi t^2}dt
= \frac{1}{4\pi}\sqrt{\frac{\pi}{2\pi}} = \frac{1}{4\pi\sqrt{2}} .$$

Therefore

$$\sigma_t^2 = \frac{1/(4\pi\sqrt{2})}{1/\sqrt{2}} = \frac{1}{4\pi},
\qquad \sigma_t = \frac{1}{2\sqrt{\pi}} = 0.2820948 .$$

The transform is $e^{-\pi f^2}$, the same functional form, so
$\sigma_f = 0.2820948$ as well and

$$\sigma_t\sigma_f = \frac{1}{4\pi} = 0.07957747 .$$

**(b)** For $x(t) = e^{-\pi(at)^2}$, scaling gives
$X(f) = \frac1a e^{-\pi(f/a)^2}$. Both widths scale as $1/a$ (one inversely, one
directly), so the product is invariant:

$$\sigma_t = \frac{1}{2a\sqrt{\pi}}, \qquad
\sigma_f = \frac{a}{2\sqrt{\pi}}, \qquad
\sigma_t\sigma_f = \frac{1}{4\pi} .$$

**(c)** The script reports:

| $a$ | $\sigma_t$ | $\sigma_f$ | product |
|---|---|---|---|
| 0.5 | 0.564190 | 0.141047 | 0.07957747 |
| 1.0 | 0.282095 | 0.282095 | 0.07957747 |
| 2.0 | 0.141047 | 0.564190 | 0.07957747 |
| 4.0 | 0.070524 | 1.128379 | 0.07957747 |

Every product equals $1/(4\pi) = 0.07957747$ to all printed figures, and the
individual widths match $0.2820948/a$ and $0.2820948a$ exactly. The Gaussian
attains the bound with equality — the only signal that does so.

**(d)** If widths are defined in *angular* frequency, $\sigma_\omega = 2\pi\sigma_f$,
so

$$\sigma_t\sigma_\omega = 2\pi\cdot\frac{1}{4\pi} = \frac12 .$$

So "$\Delta t\Delta f \ge 1/2$" is the *same* statement with the $\omega$
convention and angular-frequency widths. A statement of the form
"$\Delta t\Delta f = \text{constant}$" is incomplete without both the transform
convention and the definition of width, and this is the cleanest example in the
module of why convention statements are not pedantry.
