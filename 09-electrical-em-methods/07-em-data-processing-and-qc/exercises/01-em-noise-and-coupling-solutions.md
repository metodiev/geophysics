# Solutions — 09-07-01 EM Noise, Coupling and Cultural Effects

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All models are **SYNTHETIC**.

Lesson: [01 EM Noise, Coupling and Cultural Effects](../01-em-noise-and-coupling.md).

---

## ★1 — The error budget of a Wenner sounding

With $\sigma_{\rho_a} = 2\pi a\,\sigma_V$ and $\sigma_V$ fixed by the 1 m
requirement, $\sigma_V = 0.01\times25.0382/(2\pi\times1) = 0.039850$ (arbitrary
volt units). The synthetic model is $\rho_1 = 25$, $\rho_2 = 500\
\Omega\,\mathrm{m}$, $H = 8$ m.

| $a$ (m) | $\rho_a$ ($\Omega$ m) | $\sigma_{\rho_a}$ ($\Omega$ m) | relative error |
|---|---|---|---|
| 1 | 25.0382 | 0.25038 | 1.000% |
| 2 | 25.2943 | 0.50076 | 1.980% |
| 4 | 27.0529 | 1.00153 | 3.702% |
| 8 | 35.8857 | 2.00306 | 5.582% |
| 16 | 61.8999 | 4.00611 | 6.472% |
| 32 | 110.8966 | 8.01222 | 7.225% |

The **32 m spacing limits the sounding**: it carries the deepest information and
the worst relative error, and because the error grows as $a$ while the sensitivity
to the target grows much more slowly, the deepest datapoints are always the
weakest. The correct response is not to drop them but to weight them by
$1/\sigma^{2}$.

---

## ★2 — Classification

| case | kind | does stacking help? |
|---|---|---|
| (a) thermal noise in the receiver | incoherent | yes, as $1/\sqrt{N}$ |
| (b) 50 Hz line phase-locked to the clock | coherent | **no** — it is signal to the stack |
| (c) buried metal pipe | systematic (cultural) | no — it is not time-dependent |
| (d) telluric fluctuation of period minutes over a 30 s repeat | coherent (correlated between repeats) | **barely** — the effective $N$ is much smaller than the nominal $N$ |
| (e) drifting electrode contact resistance | systematic, slowly varying | no — it needs a drift correction, not averaging |

Case (d) is the subtle one: a slow telluric field is technically random
(so $1/\sqrt{N}$ is not *wrong*), but its correlation time exceeds the repeat
interval, so the samples are not independent and the nominal $N$ overstates the
available gain.

---

## ★3 — A line in apparent-resistivity units

Line amplitude in $\Omega\,\mathrm{m}$ is $K\times(\text{line voltage}) =
2\pi a \times 3\sigma_V$ with $\sigma_V = 0.04$:

- $a = 1$ m: $2\pi\times1\times0.12 = 0.7540\ \Omega\,\mathrm{m}$
- $a = 32$ m: $2\pi\times32\times0.12 = 24.127\ \Omega\,\mathrm{m}$

a factor of 32 between them, purely from the geometric factor. Stacking 100
repeats changes neither number: a phase-locked line is unchanged by averaging.
The demonstration measures this directly, as the rms error of the stacked
estimate at the widest spacing: 27.39 $\Omega\,\mathrm{m}$ at $N=1$ and
22.53 $\Omega\,\mathrm{m}$ at $N=256$ — no reduction at all, against
13.23 $\rightarrow$ 0.88 for the incoherent case.

---

## ★4 — The $1/\sqrt{N}$ law

Let $x_i$ be independent with mean $\mu$ and variance $\sigma^{2}$. Then
$\mathrm{Var}(\bar{x}) = \frac{1}{N^{2}}\sum_i \mathrm{Var}(x_i)
= \sigma^{2}/N$, so $\mathrm{sd}(\bar{x}) = \sigma/\sqrt{N}$. The assumptions
are (i) **independence** and (ii) **finite, identical variance**.

The demonstration's **drifting-phase** case violates **neither**: the phase
advances between repeats by more than a radian, so the coherent samples are
effectively independent draws and the measured error returns to
$\sigma/\sqrt{N}$ (3.6533 and 0.8856 at $N=16$ and $N=256$ against the
predicted 3.5053 and 0.8763). The case that *does* violate independence is the
**phase-locked** one, where every repeat draws the identical value
$A\sin(\varphi_0)$: the variance of the mean is then $A^{2}\sin^{2}\varphi_0$
regardless of $N$, which is why its measured error stays near 22.5
$\Omega\,\mathrm{m}$ from $N=4$ to $N=256$.

---

## ★5 — Choosing a stacker at 5% contamination

Clean-data rms for the mean: $\sigma/\sqrt{N} = 14.0214/8 = 1.7527\
\Omega\,\mathrm{m}$. Under Gaussian noise the median's variance is $\pi/2$
times the mean's, so its rms is

$$1.7527\times\sqrt{\pi/2} = 1.7527\times1.2533 = 2.1966\ \Omega\,\mathrm{m}.$$

That is within $0.7\%$ of the measured median rms on the *contaminated* data
(2.18092): the median is essentially untouched by the spikes and pays only the
Gaussian efficiency penalty.

Doubling the contamination to $5\%$ doubles the spike contribution to the mean's
variance: $15.524 \to 2\times15.524 - 3.072 = 27.98$, so the mean's rms becomes
$\sqrt{27.98} = 5.29\ \Omega\,\mathrm{m}$ against the median's ~2.20. **Choose
the median** (or a trimmed mean) for a 5% contamination rate: it is a factor 2.4
better, and the price on clean data would have been only 25%.

---

## ★6 — Why the notch makes it worse

With a constant phase the columns $\cos(2\pi f t_j)$, $\sin(2\pi f t_j)$ and
$\mathbf{1}$ are all proportional to $\mathbf{1}$: the design matrix has rank 1
and condition number $4.0\times10^{31}$. The normal equations are then singular,
and `lstsq` returns the *minimum-norm* solution, which splits the single
observable number (the mean level) arbitrarily among the three collinear
coefficients. The quantity returned as "the DC level" is therefore generally not
the mean, and its error (73.588) is larger than the plain average's (22.698). The
failure is one of *identifiability*, not of arithmetic: with a locked phase, the
model "DC + line" and the model "DC only" are the same model, so there is nothing
to estimate — and asking for three parameters from one number returns a
meaningless partition of it.

---

## ★7 — Guaranteeing a phase advance

Requirement: phase advance $\Delta\varphi = 0.4$ rad per repeat at $f_0 = 50$ Hz,
with a repeat period near 1 s. Since
$\Delta\varphi = 2\pi f_0 T \bmod 2\pi$, write $2\pi f_0 T = 2\pi n + 0.4$ and
solve with $n = 50$ (which places $T$ near 1 s):

$$T = \frac{2\pi\times50 + 0.4}{2\pi\times50} = 1.001273\ \mathrm{s}.$$

Check: $2\pi\times50\times1.001273 = 314.559$ rad, and $314.559 - 314.159 = 0.400$ rad
$\equiv 0.4$ rad. ✔

Residual coherent amplitude after $N = 64$ repeats is the Dirichlet factor

$$\left|\frac{1}{N}\sum_{j=0}^{N-1}\mathrm{e}^{\,\mathrm{i}j\Delta\varphi}\right|
= \left|\frac{\sin(N\Delta\varphi/2)}{N\sin(\Delta\varphi/2)}\right|
= \left|\frac{\sin(12.8)}{64\sin(0.2)}\right| = 0.0182,$$

i.e. a reduction by a factor **54.9**, far better than the incoherent
$1/\sqrt{64} = 0.125$. Two cautions belong in the design: the sampling rate must
not be an integer submultiple of the line frequency (1 kHz and 50 Hz are exactly
20:1, so every sample sits at the same phase — a synchronous sampler is just as
bad as a synchronous repeat), and the interval must be stable against clock drift
over the survey.

---

## ★8 — Why the coherent error lands on $\rho_2$

The sensitivity matrix of module 09-07-03 shows that $\partial\rho_a/\partial H$
grows by a factor 1250 between 1 m and 100 m of spacing, and
$\partial\rho_a/\partial\rho_2$ grows from $\approx0$ to $0.2066$. The line's
amplitude grows as $2\pi a$, i.e. as the same function of spacing that weights the
deep datapoints most — so the coherent term masquerades as "more half-space
signal", and the inversion answers with $\rho_2$ rather than with $H$: the two
are correlated at $+0.69$, and $\rho_2$ is the parameter that absorbs a change
common to all the long spacings without disturbing the short ones.

To move the bias onto a parameter you would rather sacrifice: shorten the
spacing range so the longest spacing never approaches the half-space; then the
same coherent term is absorbed by $H$ (and the fitted $H$ becomes meaningless,
which is the point). Alternatively record the line current and remove it by
reference, which removes the term rather than relocating it — always preferable
when the hardware allows.
