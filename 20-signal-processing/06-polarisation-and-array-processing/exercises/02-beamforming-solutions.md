# Solutions — 20-06-02 Beamforming, Slowness Estimation and f-k Analysis

> Read after attempting. Numbers computed. Lesson:
> [02 Beamforming](../02-beamforming.md).

---

## ★1 — The four design numbers at 4 Hz

Aperture: $L = (N-1)d = 19 \times 1.5 = 28.5\ \mathrm{km}$.

$$\text{first null} = \frac{1}{fL} = \frac{1}{4\times28.5}
= 0.00877\ \mathrm{s\,km^{-1}},$$
$$\text{grating spacing} = \frac{1}{fd} = \frac{1}{4\times1.5}
= 0.1667\ \mathrm{s\,km^{-1}},$$
$$\text{aliasing-free range} = \pm\frac{1}{2fd} = \pm0.0833\ \mathrm{s\,km^{-1}}.$$

---

## ★2 — The same array at 12 Hz

$L$ and $d$ are geometry and do not change. Every *slowness* scale does:

$$\text{first null} = \frac{1}{12\times28.5} = 0.00292\ \mathrm{s\,km^{-1}},$$
$$\text{grating spacing} = \frac{1}{12\times1.5} = 0.0556\ \mathrm{s\,km^{-1}},$$
$$\text{aliasing-free range} = \pm0.0278\ \mathrm{s\,km^{-1}}.$$

Higher frequency buys resolution by a factor of three and costs aliasing-free
range by the same factor. This is the single most important operational fact
about arrays: **you cannot choose a frequency that is good for both.**

---

## ★3 — Resolving two arrivals

The Rayleigh limit at 4 Hz is
$\Delta s_{\min} \approx 1/(fL) = 0.00877\ \mathrm{s\,km^{-1}}$. The separation is
$0.02\ \mathrm{s\,km^{-1}} = 2.3\times$ the limit, so **yes**, the array resolves
them (with the qualification that the demonstration's equal-amplitude pair was
still partly separable slightly below the limit, $0.556$ valley/peak at
$0.008$).

At 12 Hz the limit would be $0.00292$ and the margin would be $6.8\times$; at
2 Hz the limit would be $0.0175$ and the separation would be only $1.1\times$ the
limit — marginal.

---

## ★★4 — An impossible array gain

For incoherent noise, $G = 10\log_{10}N = 10\log_{10}10 = 10.00\ \mathrm{dB}$.
Reaching $20\ \mathrm{dB}$ in power needs $N = 100$ sensors.

Two likely errors:

1. **Power/amplitude confusion.** An amplitude ratio of 10 between the beam and a
   single sensor is $20\log_{10}10 = 20\ \mathrm{dB}$, but the *power* ratio is
   only 10 dB. The array gain is a power ratio: $G = N$, not $\sqrt{N}$.
2. **Coherent noise.** If part of the noise is coherent across sensors (a
   pressure signal, a common-mode instrument artefact), the beam does not reduce
   it, and the apparent gain measured on a *mixed* noise field can be anything —
   including larger than $N$ if the reported "noise" was actually signal-like.

A third possibility is a mis-stated sensor count or an unstated "gain" relative
to the noisiest single sensor rather than the mean. The measurement that exposes
the error is the comparison of the beam noise rms with the single-sensor noise
rms: the ratio must be $\sqrt{N}$ (the demonstration measured $3.151$ for
$N = 10$, against $\sqrt{10} = 3.162$).

---

## ★★5 — Deriving the gain

With $x_j = A + n_j$, $n_j$ independent with variance $\sigma_n^{2}$,

$$b = \frac{1}{N}\sum_j x_j = A + \frac{1}{N}\sum_j n_j,
\qquad
\operatorname{Var}\!\left(\frac{1}{N}\sum_j n_j\right)
= \frac{\sigma_n^{2}}{N}.$$

So $\mathrm{SNR}_{\text{beam}}/\mathrm{SNR}_{\text{single}} =
\sigma_n^{2}/(\sigma_n^{2}/N) = N$. For $N = 36$:

$$G = 10\log_{10}36 = 15.56\ \mathrm{dB}.$$

**Condition:** the noise must be **incoherent** between sensors. Any part of the
noise field that is coherent across sensors is summed coherently and gains
nothing.

---

## ★★6 — Grating lobes at 4 km spacing, 5 Hz

$$\frac{1}{fd} = \frac{1}{5\times4} = 0.0500\ \mathrm{s\,km^{-1}},
\qquad
\frac{1}{2fd} = 0.0250\ \mathrm{s\,km^{-1}}.$$

With a true slowness of $0.10$, the grating lobes fall at
$0.10 \pm 0.05 = 0.05$ and $0.15\ \mathrm{s\,km^{-1}}$ (and further multiples).
The proposed search range is $0.10 \pm 0.06 = [0.04, 0.16]$, which **contains both
grating lobes** — a wave genuinely at $0.05$ would be reported at $0.10$ with full
amplitude, and vice versa.

**Verdict:** not safe. Halve the spacing to 2 km (grating spacing
$0.1\ \mathrm{s\,km^{-1}}$, lobes at $0.0$ and $0.2$, outside the range), or
restrict the search to $|s - 0.10| < 0.05$ and accept that slownesses beyond it
are aliased. The demonstration measured exactly this for $d = 4$ km: grating
offsets at $\pm0.050$.

---

## ★★★7 — Designing the array

**Resolution.** $\Delta s = 1/(fL) \Rightarrow L = 1/(2 \times 0.005) =
100\ \mathrm{km}$.

**Aliasing.** No grating lobe within $|s| < 0.1$ requires
$1/(2fd) > 0.1$, i.e. $d < 1/(2 \times 2 \times 0.1) = 2.5\ \mathrm{km}$. This
also satisfies the stated cap of $2.5\ \mathrm{km}$.

**Sensor count.** With $d = 2.5\ \mathrm{km}$ (the widest allowed, hence the
fewest sensors),

$$N = \frac{L}{d} + 1 = \frac{100}{2.5} + 1 = 41\ \text{sensors}.$$

**Achieved numbers.** $L = 40 \times 2.5 = 100\ \mathrm{km}$,
$\Delta s = 1/(2\times100) = 0.005\ \mathrm{s\,km^{-1}}$,
$1/(fd) = 1/(2\times2.5) = 0.20\ \mathrm{s\,km^{-1}}$,
aliasing-free range $\pm0.10\ \mathrm{s\,km^{-1}}$ — exactly the requirement, with
no margin.

**Recommendation.** Add margin by using $d = 2.0\ \mathrm{km}$ and
$N = 51$ sensors: aliasing-free range $\pm0.125\ \mathrm{s\,km^{-1}}$ and the same
resolution. A design that exactly meets every bound has no tolerance for a
position error or a frequency excursion, and the demonstration's random-array
ensemble (sidelobe scatter $\pm1.68\ \mathrm{dB}$) shows how much a single
realisation can drift.

---

## ★★★8 — Why the threshold is hard

The array response to a single monochromatic wave is
$\operatorname{sinc}^{2}$-shaped with its first nulls at $\pm1/(fL)$ — about
$\pm0.0111\ \mathrm{s\,km^{-1}}$ for the demonstration's 18-km aperture at 5 Hz.
Two equal waves separated by $\Delta s$ produce a total response that is the sum
of two shifted $\operatorname{sinc}^{2}$ functions.

- If $\Delta s$ exceeds the null-to-null half-width, the first wave's main lobe
  falls in the second's sidelobe region and a **dip between two peaks** exists.
  The dip is a real feature of the total response and its depth grows quickly as
  $\Delta s$ grows (the demonstration: valley/peak $0.556$ at $0.0096$, $0.097$ at
  $0.0158$, $0.038$ at $0.0304$);
- as $\Delta s$ falls below the half-width, the two main lobes overlap and the sum
  becomes a **single broader peak**. There is no dip to find, and the sum of two
  overlapping $\operatorname{sinc}^{2}$ lobes is mathematically indistinguishable
  from one wave of intermediate slowness with a slightly broader spectrum.

**Why post-processing cannot help.** The beam power is a deterministic function
of the slownesses and amplitudes present. Once the map from (two waves at
$\Delta s$) to (beam power) is not injective — and for $\Delta s$ below the
threshold it is not — no algorithm can invert it, because two different truths
give the same data. A sparsity prior can pick one of the two, but it is choosing
on the basis of an assumption about the Earth, not extracting information from the
array. The demonstration's merged case is the honest statement: the information
is not in the data.
