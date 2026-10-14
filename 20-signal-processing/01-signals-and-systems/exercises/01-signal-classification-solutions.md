# Solutions — 20-01-01 Signal Classification: Continuous/Discrete, Deterministic/Random

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All models are **SYNTHETIC** teaching choices.

Lesson: [01 Signal Classification](../01-signal-classification.md).

---

## ★1 — Four-axis classification

| | independent var. | dependent var. | predictability | quadratic size |
|---|---|---|---|---|
| (a) 100 Hz velocity record, 60 s | discrete (6000 samples) | real, quantised | random (one realisation of the noise field) | finite duration ⇒ finite energy; treated as power for its statistics |
| (b) gravimeter calibration curve | discrete (dial readings) | real, quantised | deterministic (fixed by the instrument) | finite, one-valued ⇒ neither energy nor power in the time-series sense |
| (c) $1.5\cos(2\pi\cdot0.25t)$ | continuous | real | deterministic | infinite energy, finite power |
| (d) hourly tidal water level | discrete (8760 samples) | real, quantised | deterministic in the tidal band, random in the weather band | finite duration; power statistics over the record |

Units: (a) $\mathrm{m\,s^{-1}}$; (b) mGal, with
$1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$ by definition; (c)
$\mathrm{m\,s^{-1}}$; (d) m.

**Point of (b):** not every "signal" is a time series. The four axes apply to
the mathematical object, not to the physical quantity, and a transfer function is
a perfectly good signal whose independent variable is a dial reading.

---

## ★2 — Energy, power, rms, crest factor

$x(t) = 5.0\sin(2\pi\cdot0.5t)\ \mathrm{m\,s^{-1}}$ over
$T = 20\ \mathrm{s}$ = 10 whole periods.

$$E = \int_{0}^{T} x^{2}\mathrm dt = \frac{A^{2}T}{2}
= \frac{25\cdot20}{2} = 250\ \mathrm{(m\,s^{-1})^{2}\,s},$$
$$P = \frac{E}{T} = \frac{A^{2}}{2} = 12.5\ \mathrm{(m\,s^{-1})^{2}},$$
$$x_{\mathrm{rms}} = \sqrt{P} = \frac{5}{\sqrt2}
= 3.535534\ \mathrm{m\,s^{-1}}, \qquad
\text{crest} = \frac{5}{3.535534} = \sqrt2 = 1.414214.$$

The exactness is a consequence of averaging over a whole number of periods; had
$T = 10.5\ \mathrm{s}$ been chosen, $P$ would differ by the residual
$\sin(4\pi f_0 T)/(4\pi f_0 T)$ term, of order $1/(4\pi\cdot5.25) \approx 1.5\%$.

---

## ★3 — Triangle and square, same peak amplitude

$$x_{\mathrm{rms,triangle}} = \frac{4}{\sqrt3}
= 2.309401\ \mathrm{mGal}, \qquad
x_{\mathrm{rms,square}} = 4.000000\ \mathrm{mGal}.$$

Power ratio (square / triangle) $= \dfrac{A^{2}}{A^{2}/3} = 3$ exactly. Carrying
units: mGal² for both powers, so the ratio is dimensionless as it must be.

---

## ★4 — Orthogonality of the even and odd parts

$$\int_{-T/2}^{T/2} x_e x_o\,\mathrm dt
= \frac14\int_{-T/2}^{T/2}\bigl[x(t)+x(-t)\bigr]\bigl[x(t)-x(-t)\bigr]\mathrm dt
= \frac14\int_{-T/2}^{T/2}\bigl[x^{2}(t)-x^{2}(-t)\bigr]\mathrm dt.$$

Substitute $t \to -t$ in the second term: it equals
$\int_{-T/2}^{T/2} x^{2}(t)\,\mathrm dt$ on a symmetric interval (the interval
maps onto itself). So the integrand integrates to zero and the parts are
orthogonal; expanding $\int (x_e+x_o)^{2}$ then gives
$\int x^{2} = \int x_e^{2} + \int x_o^{2}$.

**Causal discrete record.** For $x[0..N-1]$ the reflection is only defined after
you choose an origin and an extension. With the "reflect about $n=0$" convention
the record must be extended to negative indices, which invents data. The
decomposition therefore requires either a symmetric extension (odd-length,
centre-defined record), a periodic extension, or a stated convention such as
$n_0 = (N-1)/2$. Without a stated convention the split is not defined, and the
numerical check in the lesson is done on a 17-sample (odd) record for exactly
this reason.

---

## ★5 — Uncertainty of an rms from a single realisation

$$\delta x_{\mathrm{rms}} = \frac{\sigma}{\sqrt{2N}}
= \frac{2.40}{\sqrt{2048}} = 0.053033\ \mathrm{m\,s^{-1}},$$

a relative uncertainty of $1/\sqrt{2048} = 2.2097\%$.

For $0.5\%$:

$$\frac{1}{\sqrt{2N}} = 0.005 \implies 2N = 4\times10^{4}
\implies N = 20\,000\ \text{samples}.$$

**Provisional $\sigma$.** The formula uses the unknown $\sigma$, which you
replaced by the measurement $2.40$. The resulting interval is an estimate of an
interval; the quantity $\sqrt2\,N^{1/2} s^{2}/\sigma^{2}$ is
$\chi^{2}$-distributed with $N$ degrees of freedom, and for $N = 1024$ the
relative uncertainty *of the uncertainty* is $1/\sqrt{2N} = 2.2\%$ — the same
number. Quote it, or use a $\chi^{2}$ interval as in
[01-13-07](../../../01-mathematics/13-probability-and-statistics-foundations/07-confidence-intervals.md).

---

## ★6 — The "periodicity test" that tested the record length

For a signal that is genuinely periodic with period exactly $\ell$ samples,
$\sum_{n=0}^{N-\ell-1} x[n]x[n+\ell] = \sum_{n=0}^{N-\ell-1}x^{2}[n]$, while
$\sum_{n=0}^{N-1}x^{2}[n]$ is larger. The biased estimator therefore returns

$$\frac{N-\ell}{N} = 1 - \frac{200}{2000} = 0.90.$$

The measured $0.90$ is *exactly* what a perfectly periodic signal produces at
this lag and record length. The conclusion is unsound. Either use the unbiased
normalisation

$$r_{\text{unbiased}}(\ell) = \frac{1}{N-\ell}\sum_{n=0}^{N-\ell-1}x[n]x[n+\ell],$$

which returns $1.000$ for this case, or divide out the triangular factor
$1-\ell/N$ before applying a threshold. Note the trade: the unbiased estimator
has larger variance for large $\ell$, so quoting $N_{\text{eff}} = N-\ell$ beside
it is part of the answer.

---

## ★7 — Stationarity test for a dispersive train (specification)

**Statistic.** Windowed spectral centroid, or windowed group delay from the phase
of a cross-spectrum between two nearby receivers. The rms is *not* the statistic:
a dispersive train has constant amplitude and time-varying frequency.

**Windows.** Non-overlapping windows of $W$ samples, with $W$ chosen so the
window spans at least 5 cycles at the lowest frequency of interest and the
frequency resolution $\Delta f = f_s/W$ is smaller than the mode spacing you
must resolve. State both numbers; they are the resolution limit of the test.

**Null distribution.** Under the null that the record is stationary, successive
window centroids differ only by estimation scatter, whose variance you estimate
from the scatter itself (bootstrap over windows) or from the Cramér–Rao bound for
a spectral centroid. Report a 95% band.

**Falsification.** The null is falsified if a systematic monotone trend in the
centroids exceeds the 95% band. State in advance the trend slope that would count
as a detection, and how a trend in *amplitude* alone (which this test ignores)
would be handled separately.

**Honest limitation.** A trend in the centroid can also be produced by a
time-varying instrument response or by non-stationary noise. The test detects
non-stationarity, not its cause.

---

## ★8 — Effective sample count for correlated records

Starting from

$$\operatorname{Var}(s^{2}) \approx \frac{2\sigma^{4}}{N}
\sum_{k=-\infty}^{\infty}\rho^{2}(k),$$

with $\rho(k) = \phi^{|k|}$ and
$\sum_{k=-\infty}^{\infty}\phi^{2|k|} = 1 + 2\sum_{k\ge1}\phi^{2k}
= \dfrac{1+\phi^{2}}{1-\phi^{2}}$,

$$\operatorname{Var}(s^{2}) = \frac{2\sigma^{4}}{N}\cdot\frac{1+\phi^{2}}{1-\phi^{2}}
= \frac{2\sigma^{4}}{N_{\text{eff}}},
\qquad
N_{\text{eff}} = N\,\frac{1-\phi^{2}}{1+\phi^{2}}.$$

For $\phi = 0.9$, $N = 4096$:
$N_{\text{eff}} = 4096\times(1-0.81)/(1+0.81) = 4096\times0.10497 = 429.9$.

$$\text{relative uncertainty of the rms} \approx
\frac{1}{\sqrt{2N_{\text{eff}}}} = \frac{1}{\sqrt{859.9}} = 3.41\%,$$

against the i.i.d. value $1/\sqrt{2\cdot4096} = 1.10\%$: a factor $3.08$
inflation. (Direct evaluation of the exact finite-$N$ sum
$\frac{2}{N^{2}}\sum_{k=-(N-1)}^{N-1}(N-|k|)\rho^{2}(k)$ gives
$3.41\%$ as well, and a simulation of 800 realisations gives
$3.43\%$ — the asymptotic formula is already accurate at $N = 4096$.)

**Geophysical case.** Any red-noise record: magnetotelluric time series,
long-period gravity or GNSS position residuals, seismic ambient-noise amplitude
records. The honest error bar gets *bigger*, typically by a factor of $2$–$3$,
and a treatment that ignores correlation will report an uncertainty that is too
small by exactly that factor. The systematic treatment is in
[20-05-01](../../05-noise-and-random-signals/01-stochastic-processes.md).


---

## Mastery checkpoint answers

**(a)** $x(t) = 3.0\sin(2\pi\cdot2.0t)\ \mathrm{m\,s^{-1}}$ for
$2.0\ \mathrm{s}$ at $100\ \mathrm{Hz}$: discrete in time (200 samples), real
(and quantised in any real instrument), **deterministic**, and — because the
underlying signal is periodic rather than transient — a **power** signal. Its
finite record has finite energy, but the *signal* has infinite energy and finite
power.

$$E = rac{A^{2}T}{2} = rac{9	imes2}{2} = 9\ \mathrm{(m\,s^{-1})^{2}\,s},
\qquad P = rac{A^{2}}{2} = 4.5\ \mathrm{(m\,s^{-1})^{2}},$$
$$x_{\mathrm{rms}} = rac{3}{\sqrt2} = 2.121320\ \mathrm{m\,s^{-1}},
\qquad 	ext{crest factor} = \sqrt2 = 1.414214 .$$

**(b)** A triangle wave of the same peak amplitude has
$x_{\mathrm{rms}} = 3/\sqrt3 = 1.732051\ \mathrm{m\,s^{-1}}$ and power
$A^{2}/3 = 3.0$, so the **power ratio to the sine is
$(1/3)/(1/2) = 2/3 = 0.666667$**: the triangle carries two thirds of the sine's
power at the same peak.

**(e)** *Detects the chirp:* a windowed frequency estimate — the measured
zero-crossing frequency rose monotonically from $0.80$ to $7.40\ \mathrm{Hz}$
across the record. *Fails:* the windowed rms, which stayed within
$0.697$–$0.712$ (a spread of $1.022$) for the same record. A stationarity test on
the second moment alone would certify a constant-amplitude chirp as stationary.
