# Solutions — 06-01-07 Scattering, Coda and Random Media

> **Read after attempting the exercises.** Numbers were computed; demonstration
> values are quoted directly.

Lesson: [07 Scattering, Coda and Random Media](../07-scattering-and-heterogeneity.md).

---

## ★1 — Impedance and a single interface

$$Z_0 = \rho_0v_0 = 2500 \times 3000 = 7.500\times10^{6}\
\mathrm{kg\,m^{-2}\,s^{-1}},$$

which matches the demonstration's `background Z0 = 7.500e+06`.

For $Z_1 = Z_0$, $Z_2 = 1.1Z_0$:

$$r = \frac{Z_1 - Z_2}{Z_1 + Z_2} = \frac{1 - 1.1}{1 + 1.1} = \frac{-0.1}{2.1}
= -0.047619 .$$

The magnitude is $|r| = 0.047619$, and
$r^2 = 2.268\times10^{-3}$. Note the linearisation: for a small contrast
$\delta = \Delta Z/Z$, $|r| \approx \delta/2 = 0.05$, so the *coefficient* is half
the fractional contrast and the *power* is a quarter of its square.

---

## ★2 — Impedance variance

$$Z_j = \rho_jv_j = \rho_0v_0(1+\sigma\xi_j)(1+\sigma\eta_j)
= Z_0\left[1 + \sigma(\xi_j+\eta_j) + \sigma^2\xi_j\eta_j\right].$$

To first order the quadratic term is dropped, so

$$\frac{\delta Z_j}{Z_0} \approx \sigma(\xi_j + \eta_j),$$

and since $\xi,\eta$ are independent standard normals,

$$\operatorname{Var}\!\left(\frac{\delta Z}{Z_0}\right)
= \sigma^2\left(\operatorname{Var}\xi + \operatorname{Var}\eta\right)
= 2\sigma^2 \equiv \sigma_Z^2 .$$

For $\sigma = 0.02$: $\sigma_Z^2 = 2(0.0004) = 8.0\times10^{-4}$, i.e. an r.m.s.
impedance fluctuation of $\sqrt{8\times10^{-4}} = 2.83\%$.

---

## ★3 — The single-interface check

The demonstration's second check is **one** 1 m layer of impedance $2Z_0$ over a
half space of impedance $Z_0$. Its recursion runs for a single interface, so no
multiple can be involved and the exact answer is the interface coefficient itself:

$$r = \frac{Z_{\text{above}} - Z_{\text{below}}}{Z_{\text{above}} + Z_{\text{below}}}
= \frac{2Z_0 - Z_0}{2Z_0 + Z_0} = \frac{1}{3} = +0.3333333333,$$

which is exactly the printed value, and the printed
`|difference| = 0.00e+00` confirms that the recursion and the closed form agree
bit-for-bit.

**What the check fixes.** It fixes the **normalisation and the sign convention** of
the recursion. A recursion that kept every multiple but used
$r = (Z_{\text{below}} - Z_{\text{above}})/(\cdot)$ would give $-1/3$ here, and
would then produce a reflectivity of the wrong sign for the whole random stack
while still satisfying the trivial uniform-stack check ($|R| = 0$). Having one
trivial and one non-trivial limit pinned is what makes the recursion safe to use
on a medium where no closed form exists.

---

## ★4 — The three limits at $\sigma = 0.01$

$$\sigma_Z^2 = 2(0.01)^2 = 2.0\times10^{-4}.$$

| Limit | Formula | Value |
|---|---|---|
| one interface | $\sigma_Z^2/2$ | $1.00\times10^{-4}$ |
| fully coherent stack | $\sigma_Z^2/4$ | $5.0\times10^{-5}$ |
| incoherent stack | $N\sigma_Z^2/2$ | $2000 \times 1.0\times10^{-4} = 2.00\times10^{-1}$ |

The measured $2\ \mathrm{Hz}$ value $6.124800\times10^{-5}$ is 1.22 times the
coherent value and a factor $3.3\times10^{3}$ below the incoherent value. It is
therefore in the **partially coherent** regime: some phase correlation survives
(the value sits nearer the coherent end), but not full coherence (it is above
$5.0\times10^{-5}$). The same conclusion appears in the fitted exponent for that
band, 0.58 rather than 0 or 2.

---

## ★★5 — Wrapped cycles

The two-way phase across the stack is $2(2\pi f/v)(Nh)$, and the number of wrapped
cycles is that divided by $2\pi$:

$$\text{cycles}(f) = \frac{2fNh}{v} = \frac{2f(2000)}{3000}
= 1.333f .$$

At $2\ \mathrm{Hz}$: $2.67$ cycles (the demonstration's printed value). At
$160\ \mathrm{Hz}$: $213.3$ cycles.

The small-phase expansion underlying $|R|^2\propto\omega^2$ requires the
accumulated phase to be much less than one **radian** — not one cycle. At 2 Hz the
phase is $2\pi \times 2.67 = 16.8\ \mathrm{rad}$, i.e. more than an order of
magnitude too large. The law therefore cannot apply anywhere in the
demonstration's band, which is why the measured exponent is 1.0356 rather than 2.

---

## ★★6 — Local exponents

Using the printed $\lvert R_{\text{Born}}\rvert^{2}$ values
($6.124800\times10^{-5}$, $1.043589\times10^{-4}$, $2.133667\times10^{-4}$,
$6.942457\times10^{-4}$):

$$\text{2–5 Hz: } \frac{\ln(1.043589/0.612480)}{\ln(5/2)}
= \frac{0.5329}{0.9163} = 0.58,$$

$$\text{5–10 Hz: } \frac{\ln(2.133667/1.043589)}{\ln 2}
= \frac{0.7151}{0.6931} = 1.03,$$

$$\text{10–20 Hz: } \frac{\ln(6.942457/2.133667)}{\ln 2}
= \frac{1.1806}{0.6931} = 1.70 .$$

The local exponent **increases** with frequency, from 0.58 to 1.70. A single
exponent fitted over 2–20 Hz (the demonstration's 1.0356) therefore averages a
steepening spectrum — which is why the fit range must always be quoted with the
exponent.

---

## ★★★7 — Correlation length experiment (specification)

**Generation.** Replace the independent layer perturbations by a stationary
Gaussian random field with exponential autocovariance
$C(d) = \sigma^2\exp(-d/\ell)$ along the stack. Generate it either by
convolving white noise with the corresponding kernel and renormalising to unit
variance, or by the circulant-embedding method; verify the realised
autocovariance at lags $0,\ \ell,\ 2\ell$ and report it.

**Parameters.** $\ell \in \{0.5, 1, 2, 5, 10, 20\}\ \mathrm{m}$ (the layer
thickness is 1 m, so the first value is below the discretisation and serves as a
control), $\sigma = 0.01$ fixed, $N = 2000$ layers, at least 200 realisations per
$\ell$.

**Fit.** Fit the exponent of the mean Born power in frequency over 2–20 Hz, once
per $\ell$, and report exponent versus $\ell$ with the fit range.

**Prediction.** At small $\ell$ the result must approach the independent-layer
value 1.0356 measured here (the control). As $\ell$ grows the medium becomes
smooth on the wavelength scale, the coherent plateau extends to higher frequency,
and the fitted exponent **decreases**: a smooth medium scatters less at low
frequency and its power grows more steeply higher up, which pushes the band-averaged
exponent down. The most sensitive regime is $\ell$ comparable to the wavelength,
i.e. $\ell \sim v/(2\pi f) \approx 24\ \mathrm{m}$ at 20 Hz — near the top of the
range, which is why the list extends to 20 m.

---

## ★★★8 — Born from the recursion (worked derivation)

Start from

$$R_j = \frac{r_j + \theta_jR_{j+1}}{1 + r_j\theta_jR_{j+1}},
\qquad \theta_j \equiv e^{2\mathrm{i}\omega h/v_j}.$$

**Step 1 — linearise the denominator.** For small coefficients,
$(1+x)^{-1} = 1 - x + O(x^2)$, so

$$R_j = \left(r_j + \theta_jR_{j+1}\right)\left(1 - r_j\theta_jR_{j+1}\right)
+ O(r^2) = r_j + \theta_jR_{j+1} + O(r^2).$$

*Discarded:* the term $-r_j\theta_j^2R_{j+1}^2$, which is second order in the
interface coefficients and corresponds to a wave that has scattered at two
interfaces — a multiple.

**Step 2 — iterate.** With $R_{N+1} = 0$,

$$R \approx r_1 + \theta_1\left(r_2 + \theta_2R_3\right) + \cdots
= \sum_{j=1}^{N} r_j\prod_{k<j}\theta_k .$$

**Step 3 — identify the phase.** Since
$\theta_k = e^{2\mathrm{i}\omega h/v_k}$ and $\tau_j = \sum_{k<j}h/v_k$ is the
one-way travel time to interface $j$,

$$\prod_{k<j}\theta_k = e^{2\mathrm{i}\omega\tau_j},
\qquad
R_{\text{Born}}(\omega) = \sum_{j=1}^{N}r_j\,e^{2\mathrm{i}\omega\tau_j}.$$

That is exactly the demonstration's `born_reflectivity`. It is a discrete Fourier
transform of the interface reflectivity sequence sampled at the two-way phase
$2\omega\tau_j$: **linear** in the medium parameters (so its inversion is a linear
inverse problem) and **blind to multiples** (the discarded term of Step 1).

---

## ★★★9 — Coherent limit and the factor of two

**Telescoping.** With $r_j \approx (\delta Z_j - \delta Z_{j+1})/(2Z_0)$ and all
phases equal,

$$\sum_{j=1}^{N}r_j = \frac{1}{2Z_0}\sum_{j=1}^{N}\left(\delta Z_j - \delta Z_{j+1}\right)
= \frac{\delta Z_1 - \delta Z_{N+1}}{2Z_0} = \frac{\delta Z_1}{2Z_0},$$

because the terminating half space is fixed ($\delta Z_{N+1} = 0$). Hence

$$\mathbb{E}\left\lvert\sum_j r_j\right\rvert^{2}
= \frac{\operatorname{Var}(\delta Z_1)}{4Z_0^2}
= \frac{\sigma_Z^2Z_0^2}{4Z_0^2} = \frac{\sigma_Z^2}{4},$$

which for $\sigma = 0.01$ is $5.0\times10^{-5}$.

**The factor of two.** Each interface coefficient involves the *difference* of two
independent impedances, so

$$\operatorname{Var}(r_j) = \frac{\operatorname{Var}(\delta Z_j - \delta Z_{j+1})}{4Z_0^2}
= \frac{2\sigma_Z^2Z_0^2}{4Z_0^2} = \frac{\sigma_Z^2}{2},$$

the single-interface value. But neighbouring coefficients share a layer, so
$\mathbb{E}[r_jr_{j+1}] = -\sigma_Z^2/4$; the $N-1$ anticorrelated neighbour pairs
cancel $(N-1)\sigma_Z^2/2$ of the $N\sigma_Z^2/2$ sum of variances, leaving
exactly $\sigma_Z^2/4$. A coherent stack is therefore **half as reflective as its
individual interfaces**, not $N$ times as reflective.

**Which number the measurement supports.** The measured $2\ \mathrm{Hz}$ power is
$6.124800\times10^{-5}$. The exact fully coherent value is
$\sigma_Z^2/4 = 5.0\times10^{-5}$; the value the demonstration prints as its
"coherent limit", $\sigma_Z^2/2 = 1.0\times10^{-4}$, is the single-interface
variance. The measurement sits 1.22× above the exact coherent value and 0.61×
below the single-interface value, which is the quantitative statement that the
phases at 2 Hz are partially — not fully — correlated. Reading the printed
$\sigma_Z^2/2$ as "the coherent limit of the stack" would place the theory 1.6×
above the measurement and force the wrong conclusion that the medium is
*anticorrelated*; the telescoping derivation shows that the correct coherent
reference is $5.0\times10^{-5}$.
