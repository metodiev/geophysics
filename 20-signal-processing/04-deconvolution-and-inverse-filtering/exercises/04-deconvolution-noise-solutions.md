# Solutions — 20-04-04 Deconvolution in the Presence of Noise

> **Read after attempting the exercises.** Lesson:
> [04 Deconvolution in the Presence of Noise](../04-deconvolution-noise.md).

---

## ★1 — Output noise spectrum

With input noise spectrum $S_{ee}(f)$ and inverse filter $H = 1/W$,

$$S_{\text{out}}(f) = \frac{S_{ee}(f)}{\left|W(f)\right|^{2}}.$$

At $|W| = 0.01$, the gain is $1/0.01 = 100$ in amplitude, i.e. $100^2 = 10^{4}$
in power ($+40$ dB). A white noise floor of $\sigma = 10^{-3}$ contributes
$10^{-3} \times 100 = 0.1$ in amplitude at that frequency — larger than typical
reflectivity amplitudes, so the noise dominates the answer there.

---

## ★2 — Water level and prewhitening

They are the same operation. Prewhitening replaces $|W|^2$ with
$|W|^2 + \varepsilon\max|W|^2$ before inverting; the water-level inverse divides by
$|W|^2 + \varepsilon\max|W|^2$. "Add white noise to the wavelet" and "damp the
inverse" are two descriptions of one modification.

---

## ★3 — Why the naive inverse error is stubborn

Its error is $E/W$, amplified by $1/|W|$ at the frequency where $|W|$ is smallest.
That amplification factor does not depend on the noise level: reducing the noise by
20 dB reduces the output error by 20 dB *in that bin*, but the bin's contribution
was already $10^{13}$ times the target, so the answer stays useless. The limitation
is the operator's conditioning, not the noise.

---

## ★★4 — Frequency where the gain exceeds 1000

The peak gain equals $1/\min|W|$ over the usable band, and the condition number is
$K = \max|W|/\min|W| = 2000$. Normalising to the wavelet's peak,
$1/\max|W|$ is the gain where the wavelet is strongest, and the gain reaches 1000
when

$$\frac{\max|W|}{|W(f)|} = 1000
\quad\Longrightarrow\quad
|W(f)| = \frac{\max|W|}{1000} = 10^{-3}\max|W|.$$

So the gain exceeds 1000 wherever the wavelet spectrum falls below $10^{-3}$ of its
peak — which is exactly the usable-band threshold used in the lesson. For the
demo's Ricker this is above about 144 Hz; for the resonator-type wavelets in the
module the threshold sits near the band edge.

**The statement to remember**: the gain exceeds a specified $G$ wherever
$|W| < \max|W|/G$, so the *fraction of the band* affected is read directly off the
wavelet's amplitude spectrum.

---

## ★★5 — Benefit of improving the record SNR

| record SNR | naive inverse error | NSR-rule error |
|---|---|---|
| 10 dB | $4.633\times10^{13}$ | 0.694 |
| 30 dB | $1.764\times10^{13}$ | 0.439 |

- **Naive inverse**: improves by a factor $4.633/1.764 = 2.6$ — about 4 dB.
- **NSR rule**: improves from 0.694 to 0.439, a factor $1.58$ — about 4 dB as well,
  but starting from a *usable* value.

The striking feature is not the size of either improvement but the **starting
level**: at 10 dB the naive inverse's error is $10^{13}$ while the NSR rule's is
0.69. Twenty decibels of record SNR buys a factor of ~2 either way; the stabilised
inversion was already four orders of magnitude (in the $\log_{10}$ sense, thirteen!)
closer to usable. The conclusion is that *choosing the regulariser correctly is worth
far more than improving the data by 20 dB*.

---

## ★★6 — Why prewhitening is cheap here

The inverse filter's output noise power at frequency $f$ is proportional to
$1/|W(f)|^2$. For the demo's 45 Hz Ricker, $|W|$ falls from its peak at 45 Hz to
$6.6\times10^{-7}$ of the peak at 200 Hz, so essentially all the output noise power
is concentrated above 100 Hz — measured as 100.00% of it. Meanwhile the wavelet
carries only 0.14% of its energy above 100 Hz. Suppressing that band therefore
removes ~all of the noise and ~none of the signal.

It would be expensive for a wavelet with **broadband or high-frequency energy** —
for example a source with a strong high-frequency component (a dynamite-like
spike), or a wavelet whose spectrum decays slowly (a low-order Butterworth pulse).
For such a wavelet the high-frequency band that the inverse amplifies is also a
band the signal occupies, and prewhitening would trade real resolution for
stability at a visible cost.

---

## ★★★7 — Frequency-dependent water level

Minimise the misfit plus a frequency-dependent penalty, or equivalently apply the
Wiener form with a frequency-dependent noise-to-signal ratio:

$$R(f) = \frac{\overline{W(f)}\,D(f)}
{\left|W(f)\right|^{2} + \lambda(f)},
\qquad \lambda(f) = \frac{S_{ee}(f)}{S_{rr}(f)}.$$

This is the per-frequency optimal regulariser. With $S_{ee}$ and $S_{rr}$ the noise
and reflectivity spectra, the derivation of the single-frequency optimum from
lesson 01 carries through unchanged at each frequency, giving the same result
$\varepsilon^{*}(f) = S_{ee}(f)/S_{rr}(f)$.

**When the noise is white** ($S_{ee}$ constant) and the reflectivity is white
($S_{rr}$ constant), $\lambda(f)$ is a constant and the frequency-dependent form
reduces to the single water level used throughout the module. The reduction is
exactly why the NSR rule works on records where both are approximately white — and
why it fails on records where the noise is coloured (monochromatic lines, 1/f
drift) or the reflectivity is not white (a strong isolated reflector).

---

## ★★★8 — White-in-band, high-out-of-band noise

The signal band has NSR $= 10^{-4}$; outside it, NSR $= 10^{-2}$.

**Wrong approach**: a single water level. Choosing $\varepsilon = 10^{-4}$ (right
for the signal band) leaves the out-of-band noise amplified by up to
$1/\varepsilon = 10^{4}$ relative to the signal; choosing $\varepsilon = 10^{-2}$
matters over-damps the signal band, broadening the pulse for no benefit.

**Right approach**: a frequency-dependent regulariser

$$\lambda(f) = \frac{S_{ee}(f)}{S_{rr}(f)} = \begin{cases} 10^{-4}, & f
\in\text{signal band},\\ 10^{-2}, & \text{otherwise,}\end{cases}$$

implemented by estimating the noise spectrum in each band from a quiet window (or
from the pre-first-break part of the trace) and dividing by an assumed flat
reflectivity spectrum. The result damps where the noise is, and only there.

This is also why **band-pass filtering before deconvolution is a form of
regularisation**: it removes the out-of-band band where the single water level
would otherwise have to compromise. That is the practical bridge back to
[20-03-03](../../03-digital-filtering/03-filter-applications.md).