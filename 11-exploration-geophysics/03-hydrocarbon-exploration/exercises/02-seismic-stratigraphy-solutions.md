# Solutions — 11-03-02 Seismic Stratigraphy and Sequence Interpretation

> **Read after attempting the exercises.** Several problems have more than one
> defensible answer; where that is true it is said so.

Lesson: [02 Seismic Stratigraphy and Sequence Interpretation](../02-seismic-stratigraphy.md).

---

## ★1 — Interference factor

$$\Delta t = \frac{2h}{v} = \frac{2\times12}{3000} = 8.0\times10^{-3}\ \mathrm{s}
= 8.0\ \mathrm{ms}.$$

| $f$ (Hz) | $\pi f\Delta t$ | $2|\sin(\cdot)|$ |
|---|---|---|
| 15 | 0.3770 | 0.736 |
| 30 | 0.7540 | 1.371 |
| 60 | 1.5080 | 1.995 |

The factor grows with frequency for a fixed bed: a higher-frequency wavelet
"sees" the bed as thicker in periods, so the interference is more complete.
The maximum possible value is 2, reached when the two spike wavelets do not
overlap at all.

---

## ★2 — Tuning and readable thickness at 25 Hz

$$\lambda = \frac{3000}{25} = 120\ \mathrm{m}, \qquad \lambda/4 = 30.0\ \mathrm{m}.$$

Using the measured coefficients $0.195\,v/f_0$ and $0.17\,v/f_0$:

$$h_{\text{tune}} = 0.195\times\frac{3000}{25} = 23.4\ \mathrm{m}
= 0.78\,\lambda/4,$$
$$h_{\text{read}} = 0.17\times\frac{3000}{25} = 20.4\ \mathrm{m}
= 0.68\,\lambda/4.$$

$\lambda/4$ is conservative for both: the amplitude peaks and the thickness
becomes readable *below* it. Note the order: the amplitude maximum (23.4 m)
occurs at a greater thickness than the readable threshold (20.4 m), because the
amplitude carries thickness information down to where the read-off stops
tracking it.

---

## ★3 — Read-off of a 6 m bed

True: $\Delta t = 2\times6/3000 = 4.0$ ms.

Wavelet peak-to-trough: $1/(2f_0) = 1/50 = 20$ ms. The bed is far below the
readable threshold $0.17\times3000/25 = 20.4$ m, so the read-off saturates at
the wavelet's own scale — of order 20 ms, i.e. **five times the true value**.

The demonstration's 30 Hz equivalent measured 11.2 ms for a 5 m bed against a
true 3.3 ms (3.4×). The ratio is what matters: **the reported time is a property
of the wavelet, not of the bed**, and it changes when the acquisition frequency
changes.

---

## ★★4 — Amplitude 0.200: what it determines

For $R = 0.10$ the thick-bed composite amplitude is $2R = 0.200$, and the
demonstration's table reaches that asymptote by $h = 50$ m (0.200 at both 50 m
and 60 m).

So the measured 0.200 is consistent with **any thickness at or above the plateau
— roughly $h \ge 45$ m** — and it determines $R$, not $h$.

The general statement: **above the plateau amplitude measures the reflection
coefficient (an impedance contrast), not thickness**; between the tuning
thickness and the plateau it measures both, jointly; below tuning it measures
the product of the two in a way that cannot be separated without an assumption.
Three regimes, and only the middle one supports a thickness interpretation —
which is why a reported thickness from amplitude alone must state the
reflection coefficient it assumed.

---

## ★★5 — Accommodation rates and systems tracts

$$\frac{\mathrm{d}e}{\mathrm{d}t} = A\frac{2\pi}{T}\cos\left(\frac{2\pi t}{T}\right)
= 30\times\frac{2\pi}{0.4}\cos\left(\frac{2\pi t}{0.4}\right)
= 471.2\cos(2\pi t/0.4)\ \mathrm{m\,Myr^{-1}},$$

$$\text{rate} = 471.2\cos(2\pi t/0.4) + 50\ \mathrm{m\,Myr^{-1}}
\quad\Longrightarrow\quad \text{range } -421 \text{ to } +521
\ \mathrm{m\,Myr^{-1}}.$$

The range brackets zero, so **forced regression occurs** for part of each cycle.
At $t = 0.1$ Myr, $\cos(2\pi\times0.1/0.4) = \cos(\pi/2) = 0$, so the rate is
exactly the subsidence, $+50\ \mathrm{m\,Myr^{-1}}$; since
$50 < 80$ (sediment supply), the tract is **highstand / normal regression**.

Note the diagnostics: the rate balances subsidence alone at the sea-level
*inflexions*, not at the extremes, which is why the tract boundaries do not
coincide with the sea-level maxima and minima.

---

## ★★6 — Detection versus resolution

From the demonstration, with noise 5% of the thick-bed amplitude:

| $h$ (m) | amplitude/noise | read-off/true | detectable | resolvable |
|---|---|---|---|---|
| 2.0 | 4.9 | 8.4 | yes | **no** |
| 20.0 | 28.9 | 0.98 | yes | yes |

- The 2 m bed is **detected** (4.9× noise) and **not resolvable** (its apparent
  thickness is 8.4× the true value). The presence of a thin bed is established;
  its thickness is not.
- The 20 m bed is both detected and resolvable (read-off within 2% of truth).

The two properties fail at different thicknesses, and the reason is that they
are governed by different quantities: detection by **amplitude relative to
noise**, resolution by **bandwidth**. An acquisition upgrade (higher frequency
content) fixes resolution and can even hurt detection (more attenuation).

---

## ★★★7 — A wavelet-coefficient experiment

**Design.**

1. Choose three wavelets of the same dominant frequency but different
   fractional bandwidth: for example a Ricker (broad), a 3-term Ricker-like
   wavelet of narrower bandwidth, and a single-frequency (Gabor) wavelet of very
   narrow bandwidth. State each spectrum.
2. Build the wedge by convolving the two-spike reflectivity with each wavelet at
   the same $v$, and scan $\Delta t$ from 0.1 to 3.0 periods in steps of 0.01
   periods.
3. Metric for "readable": the smallest $\Delta t$ at which the measured
   peak-to-trough separation is within 10% of the true $\Delta t$ — the same
   criterion used in the lesson, so it is comparable.
4. Metric for "tuning": the $\Delta t$ of maximum peak-to-trough amplitude.
5. Report both as multiples of $v/f_0$ and as multiples of $\lambda/4$, for all
   three wavelets, from the same script and the same scan.

**Prediction.** The narrow-band wavelet should approach the analytic
$\Delta t = 1/(2f_0)$ (i.e. $0.25\,v/f_0 = \lambda/4$) for the tuning maximum,
since that is the single-frequency result; the Ricker should sit below it
(0.195 in the lesson). The readable threshold should follow the same ordering:
broader bandwidth reads thickness at smaller thicknesses relative to
$\lambda/4$...

**Failure mode.** If the three wavelets are not normalised to the same peak
amplitude (or the same energy), the amplitude comparison is meaningless, and if
the metric mixes "readable" and "tuning" definitions the numbers are not
comparable. The experiment also says nothing about a real wavelet, because
phase and bandwidth vary laterally; it characterises the *method*, not the Earth.

---

## ★★8 — Derivation

With $d(t) = R\left[w(t)-w(t-\Delta t)\right]$,

$$D(\omega) = R\,W(\omega)\left(1-e^{-i\omega\Delta t}\right)
= R\,W(\omega)e^{-i\omega\Delta t/2}\cdot 2i\sin\left(\frac{\omega\Delta t}{2}\right),$$

where the phasor has unit modulus, so

$$|D(\omega)| = 2R\,|W(\omega)|\,\left|\sin\left(\frac{\omega\Delta t}{2}\right)\right|.$$

**Narrow-band limit.** If $W$ is concentrated at $f_0$, the composite amplitude
is controlled by $|\sin(\pi f_0\Delta t)|$, whose first maximum is at
$\pi f_0\Delta t = \pi/2$, i.e.

$$\Delta t = \frac{1}{2f_0}
\qquad\Longrightarrow\qquad
h = \frac{v\Delta t}{2} = \frac{v}{4f_0} = \frac{\lambda}{4}.$$

**Broadband difference.** A Ricker of 30 Hz has significant energy from roughly
10 to 50 Hz. At a fixed $\Delta t$, the higher frequencies are already past their
own first interference maximum (their $\sin(\pi f\Delta t)$ has turned over), so
they contribute with reduced amplitude. The measured maximum is therefore at a
smaller $\Delta t$: $0.195\,v/f_0 = 0.78\,\lambda/4$.

**Which to use in a report.** Quote $\lambda/4$ as the rule of thumb because it
is the narrow-band convention everyone shares, and quote the *measured*
coefficient for the actual wavelet alongside it, because that is the number that
applies to the data. A report that gives only one of the two is either
irreproducible or inconsistent with the literature — and a bed interpreted at
20 m with a 30 Hz Ricker sits between the two, which is exactly the situation in
which the choice must be explicit.
