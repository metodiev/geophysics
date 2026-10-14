# Solutions — 06-09-07 Seismic Attributes and Quantitative Interpretation

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [07 Seismic Attributes](../07-seismic-attributes.md).

---

## ★1 — Resolution scales at 25 Hz

$$\lambda = \frac{v}{f_0} = \frac{2600}{25} = 104\ \mathrm{m}, \qquad
\frac{\lambda}{4} = 26.0\ \mathrm{m}, \qquad
\frac{\lambda}{8} = 13.0\ \mathrm{m}.$$

Units: $\mathrm{m\,s^{-1}}/\mathrm{Hz} = \mathrm{m\,s^{-1}\,s} =
\mathrm{m}$. $\lambda/4$ is the vertical resolution scale (the tuning
thickness); $\lambda/8$ is the Widess limit, below which the composite waveform
becomes the derivative of the wavelet and thickness can no longer be read from
the amplitude.

---

## ★2 — The demonstration's scales

$$\lambda = \frac{3000}{30} = 100.0\ \mathrm{m}, \qquad
\frac{\lambda}{4} = 25.0\ \mathrm{m}, \qquad
\frac{\lambda}{8} = 12.5\ \mathrm{m}. \quad\checkmark$$

All three match the printed values.

---

## ★3 — Tuning maximum and its two-way separation

For a thin bed of thickness $h$ between two interfaces, the two-way separation of
the top and bottom reflections is

$$\Delta\tau = \frac{2h}{v} = \frac{2\times20.0}{3000}
= 13.33\ \mathrm{ms},$$

printed as $13.3\ \mathrm{ms}$; and the measured tuning maximum is at
$h = 20.0\ \mathrm{m}$.

**Note the comparison the demonstration draws:** the conventional rule of thumb
puts the tuning thickness at $\lambda/4 = 25\ \mathrm{m}$, i.e. at
$\Delta\tau = 1/(2f_0) = 16.7\ \mathrm{ms}$, about $20\%$ larger than the
measured $20\ \mathrm{m}$. The rule assumes an idealised wavelet; a Ricker peaks
earlier. **Quote the rule as an order and the measurement for the number.**

---

## ★4 — Fresnel radius

The first Fresnel zone is the set of surface points whose two-way path differs
from the specular path by less than half a wavelength, $\lambda/2$. For a
zero-offset ray to a reflector at depth $z$ and a nearby reflection point at
horizontal offset $r$:

$$\text{path difference} \approx \frac{r^{2}}{2z}
\quad\text{(the standard small-angle geometry)},\qquad
\frac{r^{2}}{2z} = \frac{\lambda}{2}
\;\Longrightarrow\;
r_f = \sqrt{\frac{\lambda z}{2}} .$$

**Verification** with $\lambda = 100\ \mathrm{m}$:

$$z = 500\ \mathrm{m}:\; r_f = \sqrt{\frac{100\times500}{2}}
= \sqrt{25\,000} = 158.11\ \mathrm{m},$$
$$z = 4000\ \mathrm{m}:\; r_f = \sqrt{\frac{100\times4000}{2}}
= \sqrt{200\,000} = 447.21\ \mathrm{m}.$$

Both match the printed values ($158.1$ and $447.2\ \mathrm{m}$). The scaling
$r_f\propto\sqrt{z}$ is the reason **horizontal** resolution degrades with depth
while **vertical** resolution ($\lambda/4$) does not: the vertical scale is set
by the wavelength, the horizontal scale by the geometry.

---

## ★5 — Detection versus resolution at this noise level

The threshold is $3\sigma$ of the difference between two surveys, which for a
single survey's noise rms of $0.050$ and independent noise is
$3\times\sqrt{2}\times0.050 = 0.212$ (for a *single* survey comparison; the
demonstration quotes $0.212$ as "3 sigma of the difference").

| thickness (m) | contrast | composite amplitude | detected? |
|---|---|---|---|
| 10 | 0.15 | 0.1609 | no |
| 10 | 0.30 | 0.3218 | yes |
| 20 | 0.15 | 0.2150 | yes |
| 20 | 0.30 | 0.4299 | yes |

A $10\ \mathrm{m}$ bed at contrast $0.30$ is detected ($0.3218 > 0.212$) while a
$20\ \mathrm{m}$ bed at $0.15$ is only marginally detected ($0.2150$ vs
$0.212$). **Which has the better resolution?** The $20\ \mathrm{m}$ bed is
closer to the tuning thickness ($25\ \mathrm{m}$) and its thickness is better
constrained; the $10\ \mathrm{m}$ bed is below $\lambda/8$'s neighbourhood and
its *thickness* is unresolvable even though it is detectable. Detection is a
**contrast** question (signal against noise); resolution is a **wavelength**
question (can the two interfaces be separated). A thin high-contrast bed can be
detected long after its thickness has become unreadable, and a thick low-contrast
bed can be resolvable in principle while falling below the noise.

---

## ★6 — The two regimes

$$\frac{A(4)}{A(2)} = 1.97 \approx 2, \qquad
\frac{A(16)}{A(8)} = 1.53 .$$

- $2 \to 4\ \mathrm{m}$: doubling the thickness nearly doubles the composite
  amplitude. Both thicknesses are far below $\lambda/8 = 12.5\ \mathrm{m}$, in
  the **Widess regime** where the composite wavelet is the derivative of the
  source and its amplitude is *linear* in the thickness (hence the factor
  $1.97 \approx 2$).
- $8 \to 16\ \mathrm{m}$: the same doubling gives only $1.53$. The larger
  thickness is approaching $\lambda/4 = 25\ \mathrm{m}$, where the two lobes
  begin to separate and the composite peak amplitude **saturates** (the
  demonstration's tuning curve peaks at $20\ \mathrm{m}$ and falls thereafter).

**One sentence:** below $\lambda/8$ amplitude is proportional to thickness; above
it the two reflections interfere and the amplitude saturates towards the tuning
maximum, so the amplitude–thickness relation is not single-valued.

---

## ★7 — Thickness below $\lambda/4$ (specification)

**How thickness is estimated.** Not from the *time* separation (unresolvable) but
from the *amplitude* of the composite response, inverted through a calibration
curve: the tuning curve of amplitude versus thickness for the local wavelet, the
local velocity, and the local reflection coefficient. In practice:

1. Well-tie the seismic to a synthetic to obtain the wavelet and the
   time–depth relation.
2. Compute the synthetic tuning curve for the target's contrast.
3. Convert the mapped composite amplitude to thickness through the curve.
4. Report the thickness with the *double-valued* branch of the tuning curve
   resolved by an independent argument (a geological thickness trend, or a
   spectral-decomposition phase/thickness estimate).

**Assumptions required.**

- The wavelet is known and stationary; its phase is correct.
- The velocity and therefore $\lambda$ are known at the target.
- The **impedance contrast** of the bed is known — this is the critical one: the
  amplitude is a product of contrast and thickness, so a contrast error of
  factor $2$ is a thickness error of factor $2$.
- The bed is a single thin layer, not a thin-layer *stack* (two nearby thin beds
  produce the same amplitude).
- No tuning with neighbouring beds, no interference from multiples, and no
  lateral amplitude changes from acquisition or overburden transmission.

**Which assumption fails first, and the check.** The **contrast is unknown**,
because it is precisely what a thickness map would otherwise be interpreted
against; the amplitude–thickness inversion is degenerate along a
contrast–thickness ridge (the same geometry as the AVO ridge of lesson 05). The
quantitative check: compute the inversion at two extreme plausible contrasts
(e.g. from the well's log range) and map the *difference* in the resulting
thickness. If the two maps differ by more than the desired resolution, the
thickness map is not a measurement — it is a contrast assumption in disguise.

---

## ★8 — Why the instantaneous frequency at the peak is biased

The instantaneous frequency is the time derivative of the instantaneous phase of
the analytic trace, $\omega_i(t) = d\phi/dt$. For a *symmetric* zero-phase
wavelet the phase is constant (0 or $\pi$) at the peak, and the instantaneous
frequency there is dominated by the second derivative of the envelope, not by the
dominant frequency of the wavelet's spectrum. For a Ricker with $f_0 = 30\
\mathrm{Hz}$ the demonstration measures $33.81\ \mathrm{Hz}$ at the envelope
peak — $13\%$ high. **The attribute reports a local property of the analytic
trace, not the spectrum's peak.**

**Threshold rule.** The instantaneous frequency is undefined where the envelope
is zero (the phase has no derivative), and unstable where the envelope is small,
because $d\phi/dt$ then divides a noisy phase difference by a small amplitude. A
usable rule is to compute the instantaneous frequency only where the envelope
exceeds a stated fraction of the local maximum — for example where the envelope
is above $10\%$ of the trace's peak envelope — and to report that threshold
alongside the map. Averaging an unthresholded instantaneous-frequency map
produces numbers that depend on the noise level, which is the tell-tale sign that
the map is being read as an average of noise rather than of signal.
