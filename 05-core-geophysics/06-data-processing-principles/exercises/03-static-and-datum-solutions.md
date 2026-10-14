# Solutions — 05-06-03 Static Corrections, Datum and Elevation Effects

> **Read this after attempting the exercises, not before.**

---

## ★1 — Deriving the weathering static

A vertical ray traverses the weathering layer twice (down and up), taking $2h/v_w$.
If the same thickness were replaced by substrate material it would take $2h/v_r$.
The static is the difference:

$$\Delta t = \frac{2h}{v_w} - \frac{2h}{v_r} = 2h\left(\frac{1}{v_w}-\frac{1}{v_r}\right).
\ \boxed{}$$

The factor 2 is the two-way path: reflection seismics measures two-way time.

---

## ★2 — A thickness evaluation

$$\Delta t = 2 \times 8 \times \left(\frac{1}{500}-\frac{1}{3000}\right)
= 16 \times (2.0000\times10^{-3} - 3.3333\times10^{-4})
= 16 \times 1.66667\times10^{-3} = \boxed{26.67\ \mathrm{ms}}.$$

At 4 ms sampling that is $26.67/4 = \boxed{6.67\ \text{samples}}$ — more than six
samples of shift, far beyond what any stacking will tolerate without correction.

---

## ★3 — The three statics

| static | source of values |
|---|---|
| elevation | measured elevations plus a **replacement velocity** (a model-based input) |
| weathering | a refraction survey, uphole shots, or first-arrival tomography — i.e. a measured near-surface model |
| residual | the data itself (cross-correlation, surface-consistent decomposition) |

---

## ★4 — Elevation to time error

$$\Delta t = \frac{2\Delta z}{v_r} = \frac{2 \times 15}{2400} = \boxed{12.5\ \mathrm{ms}}.$$

---

## ★5 — Why the long wavelength is invisible

A static shift that is common to every trace within a spread does not change the
*alignment* of those traces, so it does not change the stack and cannot be detected by
any criterion based on the stack — hence the datum must supply it.

---

## ★★6 — A 70 Hz bandwidth specification

**(a)** Requiring $\exp(-2\pi^{2}f^{2}\sigma_t^{2}) \ge 0.97$:

$$2\pi^{2}f^{2}\sigma_t^{2} \le -\ln 0.97 = 0.030459$$
$$\sigma_t \le \frac{\sqrt{0.030459}}{2\pi \times 70} = \frac{0.17453}{439.82}
= \boxed{0.397\ \mathrm{ms}}.$$

**(b)** With $h = \Delta t / \left[2(1/v_w - 1/v_r)\right]$ and
$2(1/700 - 1/2800) = 2(1.42857\times10^{-3}-3.57143\times10^{-4})
= 2.14286\times10^{-3}$ s/m:

$$h_{\max} = \frac{0.397\times10^{-3}}{2.14286\times10^{-3}}
= \boxed{0.185\ \mathrm{m}} .$$

**(c)** A refraction survey cannot resolve the weathering thickness to 18 cm
everywhere across a survey. This is the quantitative reason residual-statics
algorithms exist and are applied *in addition* to the model-based statics: the
specification implied by a high-frequency bandwidth exceeds what any independent
near-surface measurement delivers, and the remainder must be estimated from the data
— with the long-wavelength part still supplied by the datum.

---

## ★★7 — Elevation statics across a spread

**(a)** Two-way time to a datum at 100 m, i.e. using the height above the datum:

$$\Delta t(175) = \frac{2\times75}{2200} = \boxed{68.18\ \mathrm{ms}}, \qquad
\Delta t(120) = \frac{2\times20}{2200} = \boxed{18.18\ \mathrm{ms}}.$$

**(b)** Range $= 68.18 - 18.18 = \boxed{50.00\ \mathrm{ms}}$.

**(c)** With $v_r$ 10 % too high (2420 instead of 2200):
$\Delta t = 2\times75/2420 = 61.98$ ms, an error of 6.20 ms at the highest receiver.
At 40 Hz the lesson's table (which is at 30 Hz) scaled by the frequency squared
gives, for a residual of 6.2 ms at 40 Hz,
$\exp(-2\pi^{2}\cdot1600\cdot(0.0062)^{2}) = \exp(-0.486) = 0.615$. Even allowing for
the formula's optimism at large $\sigma_t$ (measured implied frequency falling), the
consequence is a **25–40 % loss of stack amplitude** from the replacement velocity
alone. The velocity must be measured.

---

## ★★8 — A residual-statics solution

**(a)** The lesson's partial-correction table gives, for a fraction removed of 1.00,
0.90, 0.75, 0.50, 0.00, the retained amplitudes 1.001039, 0.984514, 0.903591,
0.682146, 0.306183 with an *input* $\sigma_t = 8$ ms. Before correction therefore
about 0.31; a 50 %-accurate solution about 0.68; a 75 %-accurate solution about 0.90.

**(b)** The reported $\sigma_t = 4$ ms is the *pointwise* scatter of the estimated
statics. If the algorithm resolves only short wavelengths, the residual seen by the
stack is not that pointwise value: the unresolved long-wavelength part is common to
nearby traces and is therefore *not* removed by the algorithm, yet it does not appear
in the reported scatter either. The stack's attenuation is set by the residual's
*correlation structure* as well as its amplitude — correlated residuals attenuate more
than uncorrelated ones of the same standard deviation, which is question ★★★10.

---

## ★★9 — Merging two lines with different datums

The mismatch at the junction is the difference in datum-level statics. From the
lesson's measurement, the difference between a flat and a floating datum was a
**44.8 ms** spread in a synthetic example with about 70 m of relief and
$v_r = 2500$ m/s. Two lines with datums 60 m apart in elevation and a replacement
velocity of 2200 m/s differ by

$$\Delta t = \frac{2\times60}{2200} = 54.5\ \mathrm{ms} .$$

That is a *constant* time shift at the junction plus a spatially varying component
wherever the surface relief differs. The consequence is a discontinuity in the
migrated section at the tie — which, if not recognised, is interpreted as a fault.

**What must be reported** for a future merge: the datum elevation and its definition;
the replacement velocity used above it; and which corrections were applied relative
to it. Without these three, the dataset cannot be tied to any other.

---

## ★★★10 — Correlated statics

A satisfactory experiment:

1. Generate the static field as a random walk (or an exponentially correlated field)
   along the spread, with a chosen correlation length $\ell$, and rescale it to a
   fixed pointwise $\sigma_t$.
2. Stack 400 traces with the *same* static applied to traces within a correlation
   length (because the surface position varies slowly), and measure the retained peak.
3. **Expected result:** for $\ell$ much smaller than the spread, the attenuation
   approaches the uncorrelated prediction; as $\ell$ grows comparable to the spread,
   the attenuation becomes much stronger than the Gaussian prediction *for the same
   $\sigma_t$*.
4. **Why:** the Gaussian formula is the expectation of the *complex* exponential
   under independent Gaussian phases, i.e.
   $\operatorname{E}[e^{i\omega\delta}] = e^{-\omega^{2}\sigma^{2}/2}$. With
   correlated statics, all traces in a neighbourhood share the same $\delta$, so the
   sum does not average that component down: the effective number of independent
   statics is not $N$ but the number of independent correlation patches, which can be
   one or two.
5. **The practical lesson:** a residual-statics solution's *reported* standard
   deviation is not a sufficient statistic for the stack's attenuation; the
   correlation length must be measured too.

---

## ★★★11 — Recovering the long wavelengths from stack power

A satisfactory experiment:

1. Take the true static field (long-wavelength dominated) and construct a family of
   corrections that pass wavelengths longer than a cutoff $\Lambda$ (i.e. remove
   everything shorter).
2. For each $\Lambda$, correct and stack, and measure the stack power (or peak
   amplitude).
3. **Expected shape:** the power rises as $\Lambda$ *increases* (more of the static is
   removed) and then saturates or falls when the correction itself starts removing
   real signal — for example when the solution is allowed to absorb the structure's
   own moveout.
4. **The saturation cutoff is a measurement of the longest wavelength recoverable
   from the data**, which is set by the spread length: a static longer than the
   spread appears as a constant shift of the whole gather, which the stack cannot
   detect. So the physical content of the measured cutoff is the *spread length*.
5. **Corollary:** the remaining long-wavelength component is unrecoverable, which is
   the lesson's justification for a datum.

---

## ★★★12 — Exact attenuation of a Ricker wavelet under Gaussian jitter

**Derivation.** Let the wavelet have spectrum $W(\omega)$ and let each trace be
shifted by an independent $\delta \sim \mathcal{N}(0,\sigma_t^{2})$. The stack in the
frequency domain is

$$S(\omega) = W(\omega)\cdot\frac{1}{N}\sum_{i=1}^{N} e^{-i\omega\delta_i},
\qquad
\operatorname{E}[S(\omega)] = W(\omega)\operatorname{E}[e^{-i\omega\delta}]
= W(\omega)\,e^{-\omega^{2}\sigma_t^{2}/2}.$$

For a real wavelet the same factor applies to the negative frequencies, so the
*expected stack spectrum* is $W(\omega)e^{-\omega^{2}\sigma_t^{2}/2}$, and the
expected stacked wavelet is the inverse transform of that. With
$\omega = 2\pi f$:

$$A(\sigma_t) = \int W(\omega)\,e^{-2\pi^{2}f^{2}\sigma_t^{2}}e^{i\omega t}\,
\mathrm{d}\omega .$$

The Gaussian factor is a *frequency-dependent attenuation*: it multiplies the
spectrum by a factor that falls faster at high frequency. Two consequences follow
immediately and jointly explain the measurement:

- the *peak* of the resulting wavelet is reduced by a factor close to the Gaussian
  evaluated at the wavelet's spectral centroid — which for a Ricker is *above* its
  peak frequency, giving an implied frequency of about 36 Hz at small $\sigma_t$;
- as $\sigma_t$ grows, the surviving spectrum is progressively concentrated at low
  frequency, so the centroid falls and the implied frequency falls with it — measured
  from 36.06 Hz at 1 ms to 23.60 Hz at 16 ms.

**Numerical verification.** Evaluating $\int W(\omega)e^{-\omega^{2}\sigma_t^{2}/2}
e^{i\omega t}\,\mathrm{d}\omega$ numerically for the lesson's 30 Hz Ricker and taking
the maximum over $t$ reproduces the measured column: the ratio of the numerical peak
to the uncorrected peak should equal the printed attenuation, and the frequency
computed by inverting $A = e^{-2\pi^{2}f^{2}\sigma_t^{2}}$ should equal the printed
effective frequency. A successful answer reports the two columns agreeing to better
than 1 %. This is the analytic basis for the lesson's warning: **equation (2) of the
lesson is a scaling law derived from the Gaussian character of the jitter, and its
apparent "frequency" is only the wavelet's dominant frequency at vanishing jitter.**
