# Solutions — 20-03-02 IIR Filter Design: Butterworth, Chebyshev, Elliptic

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [02 IIR Filter Design](../02-iir-filters.md).

---

## ★1 — Butterworth magnitude-squared

$$|H(\Omega)|^2 = \frac{1}{1 + (\Omega/\Omega_c)^{2M}}.$$

At $\Omega = \Omega_c$: $|H|^2 = 1/(1+1) = 1/2$, so
$|H| = 1/\sqrt{2} = 0.7071$, i.e. $-3.01$ dB — **for every order $M$**. This is
why $\Omega_c$ is called the $-3$ dB point, and why it is *not* the passband edge.

---

## ★2 — Stability from poles

$a(z) = 1 - 1.2z^{-1} + 0.5z^{-2}$, so $A(z) = z^2 - 1.2z + 0.5 = 0$ gives

$$z = \frac{1.2 \pm \sqrt{1.44 - 2.0}}{2} = 0.6 \pm 0.4\,i.$$

$|z| = \sqrt{0.36+0.16} = \sqrt{0.52} = 0.7211 < 1$ for both poles. **Stable.**

---

## ★3 — Bilinear transform

$$s = \frac{2}{T}\frac{1 - z^{-1}}{1 + z^{-1}}, \qquad
\Omega = \frac{2}{T}\tan\!\left(\frac{\omega}{2}\right).$$

The map takes the left half-plane to the unit disc (stability preserved) and the
imaginary axis to the unit circle (frequency axis maps onto itself), but the
frequency mapping is non-linear — the **warping** above. Design routines pre-warp
the requested edges internally.

---

## ★4 — Butterworth order

$R_p = 3$ dB, $R_s = 40$ dB, $\Omega_s/\Omega_p = 20/10 = 2$.

$$10^{R_s/10} - 1 = 10^4 - 1 = 9999, \qquad
10^{R_p/10} - 1 = 10^{0.3} - 1 = 0.99526.$$

Ratio $= 9999/0.99526 = 10046.6$.

$$M \ge \frac{\log_{10}(10046.6)}{2\log_{10}(2)}
= \frac{4.00201}{2 \times 0.30103} = \frac{4.00201}{0.60206} = 6.65.$$

So $M \ge 6.65$, i.e. **$M = 7$**. (The demo's analogous spec with the cutoff
placed optimally returns a lower order; here the cutoff is pinned at the passband
edge, which is the conservative reading.)

---

## ★5 — Elliptic order

An elliptic (Cauer) design ripples **both** bands, so it reaches the same
stopband attenuation with fewer orders. For this specification
`ellipord(10, 20, 3, 40, fs=100)` returns **4**, against 7 for Butterworth. The
direction is always the same — Butterworth $>$ Chebyshev $>$ elliptic — and the
reason is that each ripple added to the response is a degree of freedom spent on
the transition instead of on flatness.

---

## ★6 — Differential delay

Using the measured table endpoints from the lesson:

- $\tau_g(5\ \mathrm{Hz}) = 10.155$ samples;
- $\tau_g(55\ \mathrm{Hz}) = 17.395$ samples.

Differential delay $= 17.395 - 10.155 = 7.240$ samples. At $f_s = 1000$ Hz that
is $7.240/1000 = 7.24$ ms. A wavelet with energy at both frequencies is smeared
over about 7 ms by this filter, which is why a broadband pick made after causal
IIR filtering is unreliable. Taking the interior points instead —
$\tau_g(20\ \mathrm{Hz}) = 10.610$ and $\tau_g(40\ \mathrm{Hz}) = 12.915$ — gives
$2.305$ samples $= 2.31$ ms over that narrower band, showing that the dispersion
is concentrated near the cutoff.

---

## ★7 — $-3$ dB frequency versus passband edge

At the passband edge $\Omega_p$ the response must be $\ge -R_p$ dB, so

$$\left(\frac{\Omega_p}{\Omega_c}\right)^{2M} = 10^{R_p/10} - 1
\Longrightarrow
\Omega_p = \Omega_c\left(10^{R_p/10}-1\right)^{1/(2M)}.$$

For $R_p = 1$ dB and $M = 6$:
$(10^{0.1}-1)^{1/12} = (0.25893)^{1/12} = e^{-1.3516/12} = e^{-0.11263} = 0.8935$.

So a filter designed with $f_c = 40$ Hz has its 1 dB point at
$0.8935 \times 40 = 35.7$ Hz, i.e. 4.3 Hz *below* the nominal cutoff. This is
exactly the effect visible in the demo, where the 15th-order Butterworth measured
2.997 dB of "ripple" at the 40 Hz passband edge because `buttord` had placed the
$-3$ dB point beyond 40 Hz. **$\Omega_c$ is where the response is $-3$ dB, not
where the specification binds.**

---

## ★8 — Cascade versus direct form

Three identical 2nd-order sections have the same poles as the single 6th-order
direct form, so their *total* group delay is identical: cascading multiplies the
transfer functions, and multiplying magnitudes adds the decibel responses while
adding the phases — the group delays add. The dispersion is therefore the same.

What differs is numerical conditioning. The direct-form 6th-order denominator
polynomial is a product of three quadratics; near the unit circle, the roots of a
sum of powers are far more sensitive to coefficient rounding than the roots of the
factors. In double precision the difference is invisible; in single precision the
direct form can move a pole outside the unit circle and the filter becomes
unstable. That is why every serious implementation uses cascaded second-order
sections (`sos`), and why the demo's stability check on `np.roots(a)` is a
diagnostic for the *design*, not a guarantee for a fixed-point implementation.