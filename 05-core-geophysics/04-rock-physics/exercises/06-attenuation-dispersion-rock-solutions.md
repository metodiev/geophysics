# Solutions — 05-04-06 Attenuation and Velocity Dispersion in Rocks

> Numbers marked *verified* were computed.

---

## ★1

$Q = 2\pi\,(\text{energy stored})/(\text{energy lost per cycle})$,
dimensionless. In the weak-attenuation limit
$\alpha = \pi f/(VQ)$, so $\mathrm{m^{-1}} = \mathrm{s^{-1}}/(\mathrm{m\,s^{-1}})$. ✓

---

## ★2

$Q^{-1}(\omega)$ and $V(\omega)$ are Hilbert transforms of one another, a
consequence of linearity and causality. Practical consequence: attenuation and
dispersion cannot be chosen independently; any operator that changes one changes
the other.

---

## ★3

$1/Q = \Delta\,\omega\tau/(1+\omega^2\tau^2)$, peaking at $\omega\tau = 1$, i.e.
$f = 1/(2\pi\tau)$, with value $\Delta/2$.

---

## ★★4 *(verified)*

$\alpha = \pi f/(VQ) = \pi(30)/(3000\cdot80) = 94.248/240000
= 3.927\times10^{-4}$ np/m. Over 1000 m the amplitude factor is
$e^{-\alpha x} = e^{-0.3927} = 0.6753$: about **32% of the amplitude is lost**
over 1 km at 30 Hz.

---

## ★★5 *(verified)*

$2\pi/Q = 2\pi/80 = 0.0785$, i.e. **7.85% of the energy is lost per
wavelength**. This is a useful scale-free measure: amplitude falls by
$e^{-\pi/Q}\approx0.961$ per wavelength for amplitude (or by
$e^{-2\pi/Q}$ for energy), independent of velocity and frequency.

---

## ★★6 *(verified)*

Peak at $f = 1/(2\pi\tau) = 1/(2\pi\cdot2\times10^{-3}) = 79.577$ Hz.
$1/Q$ at the peak $= \Delta/2 = 0.03$, so $Q = 33.3$.
Total dispersion $= \sqrt{1+\Delta}-1 = \sqrt{1.06}-1 = 2.957\%$.

---

## ★★7

Because causality requires the real and imaginary parts of the modulus (velocity
and attenuation) to be Hilbert-transform pairs. Applying one without the other
implies a non-causal operator: the output would contain energy before the input
arrives. In practice the artefact is a small timing error, but it is a
systematic one and it grows with the strength of the attenuation applied.

---

## ★★★8

Method: evaluate $1/Q(\omega)$ on $\ge4$ decades of frequency, take the Hilbert
transform by FFT with the frequency axis extended to zero, and compare the
resulting $\Delta V(\omega)/V$ with the analytic form for the Zener element.

Expected: agreement of order 1% or better over the central decades, degrading
near the edges of the computed band because the Hilbert transform is non-local —
truncating the frequency range introduces errors that decay slowly. Report the
range used and confirm convergence by halving the low-frequency limit. The
sensitivity to integration limits is the honest answer to "how accurate is my
numerical Kramers–Kronig check?"

---

## ★★★9

With $\alpha = \pi f/(VQ)$, the amplitude at depth $z$ is
$e^{-\pi f z/(VQ)}$. Requiring a factor of $e^{-1}$ (a generous criterion) gives
$f_\text{max} = VQ/(\pi z)$. With $V = 3000$ m/s and $Q = 80$:

| depth | $f_\text{max}$ (Hz) | resolution $V/(4B)$ (m) |
|---|---|---|
| 500 m | 153 | 4.9 |
| 1 km | 76 | 9.8 |
| 2 km | 38 | 19.6 |
| 4 km | 19 | 39.2 |

Resolution degrades linearly with depth, exactly as the $r^{-1}$ information
argument for diffusive fields suggested and as the constant-$Q$ model predicts
for waves. The assumption that would most change the conclusion is the value of
$Q$: halving it halves the maximum frequency at every depth and doubles the
resolution length. A second assumption worth flagging is the "factor of $e^{-1}$
survives" criterion, which is arbitrary; using $e^{-3}$ (a stricter
signal-to-noise case) moves every resolution number by a factor of about 1.7.
---

## ★★★10

**Derivation.** The peak of $1/Q = \Delta\omega\tau/(1+\omega^2\tau^2)$ is
$\Delta/2$ at $\omega\tau = 1$. Setting $1/Q$ equal to half the peak,

$$\Delta\frac{\omega\tau}{1+\omega^2\tau^2} = \frac{\Delta}{4}
\qquad\Longrightarrow\qquad
4x = 1+x^2, \quad x \equiv \omega\tau ,$$

a quadratic with roots $x = 2\pm\sqrt3 = 3.7321$ and $0.2679$.

**The result.** The half-maximum points are separated by
$3.7321/0.2679 = 13.9282$, i.e.

$$\log_{10} 13.9282 = \mathbf{1.144\ \text{decades}} ,$$

**independent of $\Delta$** — because $\Delta$ multiplies $1/Q$ uniformly and so
cancels from the half-maximum condition. The relaxation strength sets the *height*
of the absorption peak ($\Delta/2$), never its width in frequency.

**The falsifiable test.** A measured $Q^{-1}$ spectrum whose half-maximum width
differs materially from 1.14 decades is **not** a single relaxation, and this
requires no fitting, no assumed $\Delta$ and no assumed mechanism — only the
measured spectrum. A single-mechanism fit forced onto such data will produce
systematic residuals whose shape is the diagnostic.

**A flat spectrum over three decades.** $Q$ nearly constant over three decades
(1.14 decades is the width of one element) cannot be produced by any single
relaxation; it requires a **distribution of relaxation times** spanning the band.
Two standard formulations that can represent it are (i) the **Cole–Cole** model,
which replaces the single relaxation time by a distribution parameterised by an
exponent, and (ii) **Kjartansson's constant-$Q$** model, which posits $Q$
independent of frequency by construction and derives the corresponding dispersion
from Kramers–Kronig.

**What would distinguish them.** The *phase* of the modulus, or equivalently the
velocity dispersion's frequency dependence: the Cole–Cole model gives a dispersion
that flattens at high frequency, whereas constant-$Q$ gives a strictly logarithmic
dispersion across all frequencies. Measuring velocity (not just attenuation) at
three or more well-separated frequencies, and comparing the slope of $V$ against
$\ln f$, therefore separates the two — a good illustration of the lesson's theme
that attenuation and dispersion are two views of one mechanism, so each
constrains the other.
