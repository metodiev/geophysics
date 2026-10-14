# Solutions — 20-04-03 Wiener Filtering and Least-Squares Inverse Filters

> **Read after attempting the exercises.** Lesson:
> [03 Wiener Filtering](../03-wiener-filtering.md).

---

## ★1 — The cost and the desired signal

$$\xi(h) = \mathbb{E}\!\left[\left(d[n-\Delta] - h^{\top}\mathbf{x}[n]\right)^2\right].$$

In the deconvolution case the desired signal is the **reflectivity**
$d[n] = r[n]$, and the input is the trace $x = w * r + e$. The design delay
$\Delta$ accounts for the wavelet's causal spread.

---

## ★2 — Normal equations for $L = 2$

$$\begin{pmatrix} r_{xx}[0] & r_{xx}[1]\\ r_{xx}[1] & r_{xx}[0]\end{pmatrix}
\begin{pmatrix} h_0\\ h_1 \end{pmatrix}
= \begin{pmatrix} r_{dx}[\Delta]\\ r_{dx}[\Delta-1] \end{pmatrix}.$$

- $r_{xx}[0]$ — input power (variance).
- $r_{xx}[1]$ — input autocorrelation at lag 1 (the wavelet's own correlation).
- $r_{dx}[\Delta]$, $r_{dx}[\Delta-1]$ — cross-correlation between the desired
  signal and the input at the two lags the filter can reach. Because $x$ lags $d$
  by the wavelet, these are nonzero only over the wavelet's support.

---

## ★3 — Orthogonality

$$\mathbb{E}\!\left[e[n]\,x[n-j]\right] = 0 \quad \text{for } j = 0,\dots,L-1.$$

It is checkable because both $e$ and $x$ are *measured* quantities: you can compute
the cross-correlation of the error with the input without knowing the true answer.
If the residual is small the filter is optimal for its length; if it is large, the
filter is not the least-squares solution (wrong delay, too short, or a bug).

---

## ★★4 — Why the negative-lag residual is larger

The filter's span is causal: it can only use $x[n], x[n-1], \ldots, x[n-L+1]$, so
the orthogonality condition applies to lags $j = 0,\dots,L-1$ — the **non-negative**
lags here. The negative-lag correlations measure the error against *future* input
samples, which the filter cannot see and is not required to be orthogonal to. Those
lags are simply not constrained by the optimisation.

**The meaningful test is the non-negative-lag one**: $4.11\times10^{-4}$, which is
small, so the solution is optimal to three decimal places. The $1.29\times10^{-2}$
figure is a useful diagnostic in one respect: if it were *far* larger than the
positive-lag residual, it would suggest the design delay is misaligned so that the
desired correlation support falls partly outside the filter's span.

---

## ★★5 — When Wiener filtering is worth it

| record SNR (dB) | naive inverse SNR (dB) | Wiener SNR (dB) | gap (dB) |
|---|---|---|---|
| 10 | $-4.70$ | $0.17$ | 4.87 |
| 20 | $5.29$ | $6.61$ | 1.32 |
| 30 | $15.19$ | $15.48$ | 0.29 |
| 40 | $25.27$ | $25.45$ | 0.18 |

- **At 10 dB record SNR or below**, the Wiener filter wins by about 5 dB — a factor
  of three in amplitude error. Use it.
- **At 30 dB and above**, the naive inverse is within 0.3 dB; if you know the
  wavelet exactly and have a high-SNR record, the extra machinery buys almost
  nothing.
- **In between (20 dB)**, the gap is about 1.3 dB — worthwhile if the wavelet is
  imperfect, because the Wiener formulation degrades gracefully while the naive
  inverse does not.

The decisive factor is not the record SNR alone but the *usable-band condition
number*: a wavelet with a large dynamic range hurts the naive inverse at any SNR.

---

## ★★6 — What the extra coefficients do

The filter length sweep gains 5.81 → 6.36 dB over a 32-fold increase in length.
The first few coefficients model the wavelet inverse; once the filter spans the
wavelet (about 20–30 samples here) the inverse is essentially complete, and the
remaining coefficients can only reduce the error by fitting the *noise* in the
finite-record correlation estimates. That fitting is not a real improvement: it
will not generalise to another trace.

This is the finite-length face of regularisation. A short filter is a strong
regulariser (it cannot represent a wild inverse); a long filter is a weak one (it
can). The 0.55 dB gain from 161 coefficients is the benefit of a weaker
regulariser, and it comes with the risk of over-fitting the noise in $r_{xx}$ and
$r_{dx}$.

---

## ★★★7 — Excess error of a finite-length filter

Write the optimal infinite-length filter as $h_\infty$ with error
$\xi_\infty$. A length-$L$ filter is constrained to a subspace $S_L$ of the
filter space, so its minimum error is

$$\xi_L = \xi_\infty + \min_{h \in S_L}
\mathbb{E}\left[\left(h_\infty^{\top}\mathbf{x}[n] -
h^{\top}\mathbf{x}[n]\right)^2\right].$$

The excess is the energy of the component of $h_\infty$ orthogonal to $S_L$,
weighted by the input covariance: it vanishes as $S_L$ grows to contain
$h_\infty$. Because $h_\infty = 1/W$, the component outside a length-$L$ span
decays like the tail of the inverse filter, which for a minimum-phase wavelet with
a $z$ pole radius $a$ behaves as $a^{L}$. For the demo's wavelet
($a = 0.88$) and $L \approx 20$–$160$, the tail is $0.88^{20} \approx 0.077$ down to
$0.88^{160} \approx 2\times10^{-9}$, so the excess error energy falls by orders of
magnitude — which would predict a gain far larger than the measured 0.55 dB.

The measured gain is smaller because the error is already dominated by something
else: the target is a *band-limited* reflectivity, and the residual is set by the
noise in the passband, not by the filter's length. The model gives the right
qualitative shape (a saturating curve) but over-predicts the size because it
ignores the noise floor. This is a good illustration of why every prediction should
be checked against a measurement.

---

## ★★★8 — Matched versus Wiener

**Matched filter**: $h_{\text{mf}} = w$ reversed, output $y = (w \star w) * r +
n \star w$. The peak at a spike is $\sum_k w_k^2$ times the spike amplitude, with
output noise power $\sigma_n^2\sum_k w_k^2$, giving a peak signal-to-noise ratio of

$$\mathrm{SNR}_{\text{peak}} = \frac{\left(\sum_k w_k^2\right)^2\sigma_r^2}
{\sigma_n^2\sum_k w_k^2} = \frac{\sum_k w_k^2\,\sigma_r^2}{\sigma_n^2},$$

which is the largest achievable at a known epoch — this is the matched-filter
theorem.

**Wiener filter**: minimises $\mathbb{E}[(r - y)^2]$. Its output is the
band-limited reflectivity, and its error contains both noise and band-limiting.

**The two rank differently**: suppose candidate A is a spike train with energy
concentrated in the wavelet's passband, and candidate B is a spike train with much
of its energy outside the band. The matched filter ranks A above B because A's
in-band energy produces the larger peak. The Wiener filter *also* ranks A above B
here, but for a different reason (B's out-of-band energy is unrecoverable error).
Construct instead: candidate A a single large spike, candidate B two half-size
spikes at different times with equal in-band energy. The matched filter's *peak*
output is larger for A (one big peak beats two half peaks), while the Wiener
filter's mean squared error is the same for both, because total energy, not peak
height, sets the error. The metrics disagree on which is "better", which is exactly
why the criterion must be stated with the filter.