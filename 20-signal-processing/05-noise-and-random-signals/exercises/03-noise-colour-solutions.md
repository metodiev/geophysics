# Solutions — 20-05-03 Colour of Noise: White, Pink, Red and Geophysical Examples

> Read after attempting. Numbers computed. Lesson:
> [03 Colour of Noise](../03-noise-colour.md).

---

## ★1 — Reading the octave ratio

Use $2^{1-\alpha}$ and $\alpha = 2H+1$.

| ratio $2^{1-\alpha}$ | $1-\alpha$ | $\alpha$ | $H = (\alpha-1)/2$ | colour |
|---|---|---|---|---|
| 2.0 | $+1$ | 0 | $-0.5$ | white (the $H$ formula applies to fBm, $\alpha \ge 1$; a white record has no $H$) |
| 1.0 | $0$ | 1 | $0$ | pink / flicker |
| 0.5 | $-1$ | 2 | $0.5$ | red / Brownian |

The white case is the boundary: white noise is not a fractional Brownian motion,
so $H$ is undefined rather than negative.

---

## ★2 — From the structure slope to the spectrum

$\log D$ versus $\log T$ has slope $2H$, so $2H = 0.6 \Rightarrow H = 0.3$.
Then

$$\alpha = 2H + 1 = 1.6 ,$$

and the PSD slope on a log–log plot is $-\alpha = -1.6$. The process is
persistent ($H > 0$ means the increments are positively correlated in this
band), and its structure function grows sub-linearly.

---

## ★3 — Correcting the standard error

$$\text{SE}_{\text{correct}} = \text{SE}_{\text{naive}}\times
\sqrt{\tau_{\text{int}}/\Delta t}
= 0.02\times\sqrt{400} = 0.02\times20 = 0.40 .$$

The naive value was wrong by a factor of 20. (Equivalently,
$N_{\text{eff}} = 4000/400 = 10$, so the standard error is $\sigma/\sqrt{10}$,
twenty times the value of $\sigma/\sqrt{4000}$.)

---

## ★★4 — The $f^{-1}$ scaling of a mean

$$\operatorname{Var}(\bar x_T) = \frac{1}{T^{2}}\int_{-T}^{T}
C(\tau)\left(1-\frac{|\tau|}{T}\right)\mathrm{d}\tau
\;\sim\; \frac{1}{T}\int_{1/T}^{f_N} S(f)\,\mathrm{d}f ,$$

because the window's transfer function is $\approx T$ for $f \ll 1/T$ and passes
the rest. With $S \propto f^{-1}$ the remaining integral is
$\int_{1/T} f^{-1}\mathrm{d}f = \ln(f_N T)$, so

$$\operatorname{Var}(\bar x_T) \;\propto\; \frac{\ln T}{T},
\qquad
N_{\text{eff}} \;\propto\; \frac{T}{\ln T} .$$

This is *between* the white case ($1/T$) and the red case (constant or growing):
the mean still converges, but slower than $1/T$, and the effective sample count
grows slower than linearly. The logarithmic factor is why the relevant fractional
slope in the structure function is small: the demonstration measured $+0.183$ for
$\alpha = 1$ over slightly more than two decades.

---

## ★★5 — Classifying by octave power alone

**Procedure.** Compute the power in $K$ successive octave bands
$[f_0 2^{k}, f_0 2^{k+1})$. Form the $K-1$ ratios
$r_k = P_{k+1}/P_k$. Take the median ratio. Classify:

- median $r \approx 2 \Rightarrow \alpha \approx 0$ (white);
- median $r \approx 1 \Rightarrow \alpha \approx 1$ (pink);
- median $r \approx 0.5 \Rightarrow \alpha \approx 2$ (red).

Then refine with $\alpha = 1 - \log_2 r$ on the median.

**Minimum bands.** Three bands give two ratios, enough for a robust median with
one outlier tolerated. Five bands (four ratios) are better; the demonstration
uses five.

**Minimum dynamic range.** At least one decade of frequency and enough signal to
above the estimator noise; the demonstration's ratios scatter by about 5% for
pink and white and about 6% for red, so a $2\times$ classification is safe but a
$10\%$ difference is not.

**Failure mode.** A spectrum that is not a single power law — a corner frequency,
a roll-off, or a strong line inside one band — makes the median ratio describe
nothing. Adding a *fitted slope over a stated band* as a cross-check, or
reporting the individual ratios rather than only the median, exposes it.

---

## ★★6 — What stacking reduces for $f^{-2}$ noise

For $\alpha = 2$, the structure function grows linearly
($D(T) \propto T$), so over the length of one record the low-frequency wander is
the largest contribution to the error. Averaging $M$ records whose **random**
parts are independent reduces that part by $1/\sqrt{M}$; but the low-frequency
excursion common to the records has the same sign in all of them and is
reproduced by the average exactly.

**Quantitatively**, from the demonstration's table the red-noise structure
function grows by a factor

$$\frac{D(1024)}{D(4)} = \frac{1.42\times10^{-4}}{5.59\times10^{-7}}
\approx 254 ,$$

i.e. the energy at the longest lag studied is about $2.5\times10^{2}$ times that
at the shortest — against a factor of 1 for white noise. Averaging therefore
reduces the *high-frequency* residual by $\sqrt{M} = 10$ while leaving the
long-timescale excursion untouched. The defensible claim is "a factor of 10
reduction in the random component over the observing band", with the band and the
record length named; the indefensible claim is a factor of 10 reduction in the
total error.

---

## ★★★7 — Slope versus fitting band

**Design.** Generate $M = 200$ pink-noise realisations of length $2^{16}$ at a
fixed sampling rate. For each, compute a Welch PSD (fixed $N_{\text{seg}}$) and
fit a straight line to $\log_{10}S$ versus $\log_{10}f$ over several bands:
$[f_1, f_2]$, $[2f_1, f_2]$, $[4f_1, f_2]$, $[f_1, f_2/2]$, $[f_1, f_2/4]$.

**Metric.** Report, for each band, the ensemble-mean fitted slope and its scatter
over the 200 realisations, plus the band's decade width.

**Prediction.** For a pure power law the fitted slope is band-independent to
within the scatter. Any *systematic* drift with the band (a slope that steepens
as the low-frequency end is raised) is evidence of a corner or a second regime,
and the drift magnitude, compared with the scatter, is what makes the claim
testable. The scatter grows as the band narrows, because fewer decades carry the
fit; a band narrower than about one decade will report a slope with an
uncertainty comparable to the difference between white and pink. A single fitted
number without its band and scatter cannot be checked against any model.

---

## ★★★8 — Defending a Hurst exponent

**Check 1 — stationarity of the increments.** $H$ is defined for a process whose
increment statistics do not drift. Split the record into three parts and estimate
$D(T)$ on each; if the three curves do not overlay within their scatter, a change
of regime is present and a single $H$ is an average over regimes, not a property.
A change-point test or a time-frequency decomposition is the standard companion
analysis.

**Check 2 — scaling over at least two decades, in more than one estimator.**
Estimate $H$ independently from (i) the structure function slope, (ii) the PSD
slope via $\alpha = 2H+1$, and (iii) a rescaled-range (R/S) or detrended
fluctuation analysis. The three must agree within their stated uncertainties. A
single estimator on a single band is one number, not a demonstration.

**Falsification.** If the structure function is not a straight line in log–log
over the claimed range (e.g. it saturates at long lags because the record is
finite), or if a surrogate test on phase-randomised data of the same PSD
reproduces the reported $H$ (which it will for any linear Gaussian process), the
claim of a *particular persistence mechanism* fails even if the number is
reproduced. For a Gaussian process the PSD alone fixes every second-order
property, so $H = 0.8$ describes the spectrum, not the dynamics; a claim about
the dynamics needs a test that distinguishes linear from nonlinear origin.
