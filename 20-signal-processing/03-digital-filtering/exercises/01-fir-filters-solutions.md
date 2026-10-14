# Solutions — 20-03-01 FIR Filter Design: Windows, Parks-McClellan, Least Squares

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [01 FIR Filter Design](../01-fir-filters.md).

---

## ★1 — Ideal lowpass samples

$$h_d[n] = \frac{2f_c}{f_s}\,\mathrm{sinc}\!\left(\frac{2f_c n}{f_s}\right)
= 0.4\,\mathrm{sinc}(0.4n),\qquad \mathrm{sinc}(x) = \frac{\sin \pi x}{\pi x}.$$

- $h_d[0] = 0.4\,\mathrm{sinc}(0) = 0.4$.
- $h_d[1] = 0.4\,\mathrm{sinc}(0.4) = 0.4 \times 0.75683 = 0.30273$.
- $h_d[2] = 0.4\,\mathrm{sinc}(0.8) = 0.4 \times 0.23387 = 0.09355$.
- $h_d[3] = 0.4\,\mathrm{sinc}(1.2) = 0.4 \times (-0.15591) = -0.06237$.
- $h_d[4] = 0.4\,\mathrm{sinc}(1.6) = 0.4 \times (-0.18921) = -0.07568$.

The response decays only as $1/n$, which is why a rectangular truncation cannot
give a deep stopband.

---

## ★2 — Linear phase

The coefficients must satisfy $b_k = b_{N-1-k}$ (symmetric) or
$b_k = -b_{N-1-k}$ (antisymmetric). Then

$$H(e^{i\omega}) = e^{-i\omega(N-1)/2}A(\omega),$$

and the group delay is exactly $\tau_g = (N-1)/2$ samples.

---

## ★3 — Gibbs

Truncation is multiplication by a rectangular window in time, which is convolution
with the Dirichlet kernel in frequency. The kernel's sidelobes decay slowly
($\sim1/\Delta\omega$), so the convolved response keeps oscillating near the band
edge. Increasing $N$ narrows the kernel but does not lower its sidelobes, so the
ripple amplitude stays at about 9% of the step (the Gibbs overshoot) and only its
width shrinks.

---

## ★4 — Hamming versus Blackman

From the demo's table at $N = 121$:

| window | attenuation (dB) | edge at $-60$ dB (Hz) |
|---|---|---|
| Hamming | 58.49 | 53.54 |
| Blackman | 79.11 | 55.21 |

**Blackman** meets the 60 dB requirement (79.11 dB); Hamming does not (58.49 dB is
1.5 dB short). The transition edge moves from 53.54 to 55.21 Hz — Blackman is
1.67 Hz wider. The trade is the standard one: a deeper stopband floor costs
transition width.

---

## ★5 — Kaiser design, 200 Hz specification

1. Transition width $\Delta f = 35 - 20 = 15$ Hz;
   $\Delta\omega = 2\pi(15)/200 = 0.47124$ rad/sample.
2. $\beta = 0.1102(A - 8.7) = 0.1102(55 - 8.7) = 5.102$.
3. Order: $N \approx \frac{A-8}{2.285\Delta\omega} + 1
   = \frac{47}{2.285 \times 0.47124} + 1 = \frac{47}{1.07681} + 1 = 43.65 + 1 = 44.65$.
4. Odd order nearest: $N = 45$. Group delay
   $= (45-1)/2 = 22$ samples $= 22/200\ \mathrm{s} = 110$ ms.
5. **Check the estimate**: the measured attenuation at 35 Hz for a 45-tap Kaiser
   filter with this $\beta$ is **54.58 dB** — 0.4 dB short of 55. A 47-tap design
   measures **56.07 dB** and meets it. The estimate is good to a fraction of a dB
   but rounding *down* to 45 is not safe here; round up when the margin matters.
6. A 31-tap design measures only **25.85 dB**, 30 dB short: at that order the
   window's own floor is unreachable, so the rule of thumb fails completely.

---

## ★6 — Equiripple versus window

The window method multiplies the ideal response by a window, so its error is the
window's sidelobe pattern scaled by the ideal response — concentrated near the
band edge and decaying away from it. It does not attempt to minimise anything.

Parks-McClellan minimises the **weighted Chebyshev norm** (the maximum error over
the bands), so it spreads the error *equally* across the stopband instead of
concentrating it near the edge. Every stopband ripple reaches the same depth, and
that depth is lower than the window's worst sidelobe at the same order. With the
stopband weighted 20:1 the algorithm chooses how to spend the available error, and
it spends it uniformly. Hence $+18.78$ dB at equal order.

---

## ★7 — Sensitivity of linear phase to a coefficient error

Breaking symmetry by perturbing one coefficient adds an antisymmetric component
to the coefficient vector. An $N$-tap filter splits into a symmetric (linear-phase)
part and an antisymmetric part; the antisymmetric part has its own linear phase but
$90^{\circ}$ away, so the sum has a phase that is no longer exactly linear. The
group-delay excursion is first order in the perturbation.

A 1% change in $b_{20}$ of a 61-tap Hamming filter changes the passband group
delay by a fraction of a sample, varying with frequency: the delay is no longer
constant, and the maximum deviation grows linearly with the perturbation size. The
practical statement is that **linear phase is exact only for exactly symmetric
coefficients**; quantisation to fixed point destroys it in proportion to the
coefficient error.

---

## ★8 — A specification where the estimate fails

The Kaiser estimate $A \approx 2.285(N-1)\Delta\omega + 8$ assumes the order is
large enough for the Kaiser window's own floor to be reached, and that the
transition width is the binding constraint. Both assumptions fail when the order is
too small for the chosen $\beta$.

Example: $f_s = 200$ Hz, $f_p = 20$ Hz, $f_s^{\text{stop}} = 22$ Hz (very narrow
transition, $\Delta\omega = 0.0628$ rad/sample), $A = 55$ dB.
The estimate gives $N \approx 47/(2.285\times0.0628)+1 \approx 328 + 1$, so a
300-tap design would be predicted at $A \approx 2.285\times299\times0.0628 + 8 =
42.9 + 8 = 50.9$ dB. But a 300-tap Kaiser window with $\beta = 5.102$ has a floor of
about 55 dB *only if the transition is wide enough relative to the grid*; at this
narrow transition the passband and stopband edges are 2 Hz apart, fewer than two
frequency samples at the natural resolution, and the realised attenuation
fluctuates around the prediction by several dB depending on where the edges land
relative to the DFT grid.

The analytic reason the rule fails at small order is different and simpler: for
$N$ below the order at which the window's own sidelobe floor is reached, the
attenuation is set by $N$ rather than by $\beta$, and the linear formula
over-predicts. The demo's own $N = 31$ row is the clean example: the estimate
would predict a much deeper stopband but the measurement is 25 dB.

**The lesson:** verify with `freqz`, not with the rule.