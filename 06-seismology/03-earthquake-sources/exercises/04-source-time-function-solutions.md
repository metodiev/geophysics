# Solutions — 06-03-04 Source Time Functions, Rupture Kinematics and Directivity

> **Read after attempting the exercises.** All values are SYNTHETIC. Arithmetic
> is shown; hand values from the continuum formulas are compared with the demo's
> discrete measurements, and the small differences are explained.

Lesson: [04 Source Time Functions, Rupture Kinematics and Directivity](../04-source-time-function.md).

Baseline model: $\beta = 3500\ \mathrm{m\,s^{-1}}$, $L = 30\ \mathrm{km}$,
$v_r = 2800\ \mathrm{m\,s^{-1}}$, $\tau_r = 1.00\ \mathrm{s}$.

---

## ★1 — Spans

$$\frac{L}{v_r} = \frac{30\,000}{2800} = 10.714\ \mathrm{s},\qquad
\frac{L}{\beta} = \frac{30\,000}{3500} = 8.571\ \mathrm{s}.$$

$$D(0^\circ) = 10.714-8.571 = 2.143\ \mathrm{s},$$
$$D(90^\circ) = 10.714\ \mathrm{s},$$
$$D(180^\circ) = 10.714+8.571 = 19.286\ \mathrm{s}.$$

**Unit:** $(L/v_r - L\cos\theta/\beta)$ has units
$\mathrm{m}/(\mathrm{m\,s^{-1}}) = \mathrm{s}$, as required. ✔

---

## ★2 — Apparent durations and the span ratio

Adding $\tau_r = 1.00\ \mathrm{s}$:

$$0^\circ:\ 3.143\ \mathrm{s},\qquad 90^\circ:\ 11.714\ \mathrm{s},\qquad
180^\circ:\ 20.286\ \mathrm{s}.$$

$$\text{ratio}_{\text{with }\tau_r}
= \frac{20.286}{3.143} = 6.4545.$$

Without the rise time:

$$\text{ratio}_{\text{without }\tau_r} = \frac{19.286}{2.143} = 9.0000.$$

The rise time reduces the contrast by

$$\frac{9.0000-6.4545}{9.0000} = 0.283 \approx 28\%.$$

A longer local pulse is a larger constant added to both ends, so it dilutes the
directivity.

---

## ★3 — Delay widths

$$\sigma_{\text{delay}} = \frac{L}{\sqrt{12}}\left|\frac{1}{v_r}
- \frac{\cos\theta}{\beta}\right|,\qquad \frac{L}{\sqrt{12}} = 8660.25\ \mathrm{s\cdot m\,s^{-1}}.$$

- $0^\circ$: $|1/2800 - 1/3500| = 3.5714\times10^{-4}-2.8571\times10^{-4}
  = 7.1429\times10^{-5}$;
  $\sigma = 8660.25\times7.1429\times10^{-5} = 0.6186\ \mathrm{s}$.
- $90^\circ$: $|1/2800| = 3.5714\times10^{-4}$;
  $\sigma = 3.0929\ \mathrm{s}$.
- $180^\circ$: $3.5714\times10^{-4}+2.8571\times10^{-4} = 6.4286\times10^{-4}$;
  $\sigma = 5.5672\ \mathrm{s}$.

Comparison with the demo ($0.6201$, $3.1007$, $5.5812\ \mathrm{s}$): the hand
values are $0.23\%$, $0.25\%$ and $0.25\%$ lower. The continuum $1/\sqrt{12}$
factor is the limit of the discrete factor $\sqrt{(n^{2}-1)/12}/(n-1)$ for
$n$ evenly spaced delays, so a finite $n$ gives a slightly larger width; with
$n = 400$ the difference is a fraction of a per cent.

---

## ★4 — Predicted incoherent width at $90^\circ$

$$\sigma_{\text{total}} = \sqrt{\sigma_{\text{delay}}^{2}
+ \sigma_{\text{wavelet}}^{2}} = \sqrt{3.1007^{2}+0.8660^{2}}
= \sqrt{9.6143+0.7500} = 3.2194\ \mathrm{s}.$$

Demo: predicted $3.2194\ \mathrm{s}$, measured $2.9039\ \mathrm{s}$.

$$\text{discrepancy} = \frac{2.9039-3.2194}{3.2194} = -0.098 = -9.8\%.$$

**Reason and sign.** The quadrature rule is exact only when the pulses do not
overlap, in which case the energy density is the sum of the individual energies.
Here consecutive pulses overlap heavily, so the cross terms
$2w(t-d_i)w(t-d_j)$ in $|u|^{2}$ are present; summed over the signal they are
negative on average, which removes energy from the wings and pulls the
energy-weighted second moment **inwards**. Hence the measured width is always
**smaller** than the incoherent prediction — as the demo's table shows at every
azimuth, and as the shrinking-wavelet test confirms.

---

## ★5 — The wavelet's energy width

With $w(t) = (t/\tau_r)e^{-t/\tau_r}$ for $t>0$, substitute $x = t/\tau_r$:

$$\int_0^\infty w^{2}\,\mathrm{d}t
= \tau_r\int_0^\infty x^{2}e^{-2x}\,\mathrm{d}x
= \tau_r\cdot\frac{2!}{2^{3}} = \frac{\tau_r}{4}.$$

First moment of the energy density:

$$\langle t\rangle = \frac{\int t\,w^{2}\,\mathrm{d}t}{\int w^{2}\,\mathrm{d}t}
= \frac{\tau_r^{2}\int_0^\infty x^{3}e^{-2x}\mathrm{d}x}{\tau_r/4}
= \frac{\tau_r^{2}\cdot(3!/2^{4})}{\tau_r/4}
= \frac{\tau_r\cdot(6/16)}{1/4} = \frac{3\tau_r}{2}.$$

Second moment:

$$\langle t^{2}\rangle
= \frac{\tau_r^{3}\int_0^\infty x^{4}e^{-2x}\mathrm{d}x}{\tau_r/4}
= \frac{\tau_r^{2}\cdot(4!/2^{5})}{1/4} = \frac{\tau_r^{2}\cdot(24/32)}{1/4}
= 3\tau_r^{2}.$$

Therefore

$$\sigma_{\text{wavelet}}^{2} = \langle t^{2}\rangle-\langle t\rangle^{2}
= 3\tau_r^{2}-\tfrac94\tau_r^{2} = \tfrac34\tau_r^{2}
\;\Rightarrow\; \sigma_{\text{wavelet}} = \frac{\sqrt3}{2}\tau_r = 0.8660\tau_r. ☑$$

At $\tau_r = 1.00\ \mathrm{s}$ this is the demo's $0.8660\ \mathrm{s}$.

---

## ★6 — Three ratios, three functionals

The **closed-form $6.4545$** is the ratio of the emission-time *supports*
(spans, Section 3.1): it uses only the extremes of the delay distribution and the
constant rise time, so it is a statement about the width of the interval over
which pulses arrive.

The **rms ratio $5.4171$** replaces the span with the second moment of the
measured signal's energy density. The second moment of a distribution with an
exponential-like decay toward the receding end is smaller relative to its span
than a rectangular distribution's, and the overlapping pulses shift weight
inwards, so the rms ratio is *smaller* than the span ratio.

The **peak-amplitude ratio $0.1671$** is a point value of the signal, not a
moment; it satisfies the fixed-area scaling $\text{peak}\propto1/\sigma$ only
approximately, because the *shape* of the composite pulse also changes with
azimuth.

The quantity that is a property of the emission-time support is the **span
ratio $6.4545$**; the other two are properties of the realised waveform.

---

## ★7 — Stress-drop error factors

Because $\Delta\sigma\propto M_0f_c^{3}$ and $M_0$ is azimuth-independent, the
error factor from ignoring directivity is $(f_c/f_c(90^\circ))^{3}$:

| azimuth | $f_c/f_c(90^\circ)$ | cube | error factor |
|---|---|---|---|
| $0^\circ$ | 2.9792 | $2.9792^{3}$ | $26.44$ |
| $135^\circ$ | 0.6349 | $0.6349^{3}=0.2559$ | $1/0.2559 = 3.91$ |
| $180^\circ$ | 0.5500 | $0.5500^{3}=0.1664$ | $1/0.1664 = 6.01$ |

Ratio of the largest to the smallest: $26.44/3.91 = 6.76$. So the *same event*
yields point-source stress drops that differ by nearly a factor $7$ between
$0^\circ$ and $135^\circ$ — and the extremes span $26.44/6.01 = 4.40$ between
$0^\circ$ and $180^\circ$.

---

## ★8 — Inverting duration versus azimuth (specification)

**Forward relation.** With $D(\theta) = L(1/v_r-\cos\theta/\beta)$ and
$\tau_r$ fixed, the apparent duration is
$T_{\text{app}}(\theta) = \tau_r + D(\theta)$. Equivalently, for an inverse
problem, define the *delay coefficient*
$c(\theta) = 1/v_r - \cos\theta/\beta$, so
$D(\theta) = L\,c(\theta)$.

**Data.** Apparent rms durations $\hat T_i$ at $N$ stations with known azimuths
$\theta_i$ (azimuths relative to the *unknown* rupture direction $\phi$), so
$\cos(\theta_i-\phi)$ enters.

**Parameters.** $\{L, v_r, \tau_r, \phi\}$ — four, with $L$ and $v_r$ entering
only through the products $L/v_r$ and $L/\beta$, and $\beta$ assumed known.

**Non-uniqueness.** Fit on a grid of $(L, v_r, \tau_r, \phi)$ and map $\chi^{2}$.
Degenerate directions: (i) $\tau_r$ trades off against $L/v_r$ — a longer rise
time and a shorter fault give the same durations; (ii) since
$D(\theta)$ depends on $L(1/v_r - \cos(\theta-\phi)/\beta)$, a solution with
$(L, v_r, \phi)$ is nearly reproduced by $(L', v_r', \phi)$ with
$L'(1/v_r'-1/\beta) = L(1/v_r-1/\beta)$ and $L'/v_r' = L/v_r$, i.e.
$L' = L(v_r'/v_r)$ along a ridge. The two conditions together fix $v_r$ only
through the *contrast* between azimuths; hence **a single azimuth cannot
separate $L$ from $v_r$**, and $\phi$ needs stations spread far from the presumed
rupture direction.

**How many stations.** At least three azimuths sampling the directivity curve
(near $0^\circ$, near $90^\circ$, near $180^\circ$ relative to $\phi$), and
$N\ge6$–$10$ in practice to average out the unknown local rise time and the
medium broadening. The number is set by the need to fit four parameters *and* to
detect the non-rectangularity of the delay distribution; a two-station dataset
lies on the ridge and cannot resolve it.

---

## ★9 — Effect of finite down-dip width (specification)

**Argument.** For a line source the emission times are spread by the along-strike
delay $\xi(1/v_r-\cos\theta/\beta)$, which vanishes at $\cos\theta = \beta/v_r$
(never realised, since $v_r<\beta$), and is maximised at $\theta=0^\circ$ or
$180^\circ$. Adding a second dimension of width $W$ means the source is no longer
a straight line; the pulses emitted by different strike lines of the same fault
arrive over an extra spread of order $(W/\beta)$ in the direction normal to the
fault, and along the strike direction the effective dimension is reduced toward
$\min(L,W)$ for the *far-field* corner. The net effect is to **reduce** the
forward/backward duration contrast, because the finite width adds a
direction-independent spread that dilutes the along-strike directivity — the
same dilution mechanism as a long rise time.

**Prediction.** The forward/backward rms ratio $R(W/L)$ decreases monotonically
from the $W/L\to0$ value ($5.4171$) toward $1$ as $W/L$ grows past $\sim1$.

**Experiment.** Reuse the demo's superposition: place $N$ elements on the
rectangle $[0,L]\times[-W/2,W/2]$, each emitting $w(t-\xi/v_r)$ with
$\xi$ the along-strike coordinate and a fixed $v_r$, and compute the received
signal as the sum of element pulses with the far-field travel time relative to
the centroid, $(x\cos\theta + y\sin\theta)/\beta$. Measure the rms width at
$\theta=0^\circ$ and $180^\circ$ and their ratio $R$ for
$W/L\in\{0.1,0.25,0.5,1,2,4\}$. Plot $R$ versus $W/L$ and report the half-width
at which $R$ has fallen to half its line-source value; that number is the
measurement the specification produces.

---

## ★10 — Separating source duration from attenuation (specification)

**Observable.** The far-field displacement spectrum $U(f)$ from a set of events
of varying magnitude at a common station, and the same events at several stations.

**Model.** $U(f) = S(f;M_0,f_c)\,\exp(-\pi f t^{*})\,I(f)$, with $S$ the
$\omega^{-2}$ source model (lesson [05](../05-source-spectra.md)), $t^{*} =
\int \mathrm{d}s/(Q\beta)$ the attenuation operator, and $I(f)$ the instrument.
$S(f)$'s corner $f_c$ and $t^{*}$ both broaden the pulse, so they trade off in a
single spectrum: a higher $f_c$ with more $t^{*}$ fits as well as a lower $f_c$
with less.

**Separation strategy.** (i) Fix $t^{*}$ from a *stack* over many events: because
$f_c$ varies with $M_0$ (self-similarity gives $f_c\propto M_0^{-1/3}$) while
$t^{*}$ is a property of the path, the high-frequency decay common to all events
constrains $t^{*}$ and the *difference* between events constrains $f_c$.
(ii) Use the linearity of $\log U = \log S - \pi f t^{*} + \log I$: regress
$\log U$ on $f$ at high frequency across events to get the common slope
$-\pi t^{*}$, then subtract it.

**Best band.** The separation is best where the source spectrum's slope and the
attenuation slope differ most, i.e. **above** $f_c$ for the smallest events and
**well below** $f_{\text{max}}$ of the instrument. For the demo's synthetic
family ($f_c$ from $0.246\ \mathrm{Hz}$ at $M_0 = 10^{18}$ to
$0.0114\ \mathrm{Hz}$ at $M_0 = 10^{22}$), the band $0.5$–$5\ \mathrm{Hz}$ sits
above $f_c$ for the small events, where the source term is falling as $f^{-2}$
and the attenuation term as $e^{-\pi f t^{*}}$ — a difference in functional form
that is separable by the multi-event regression above.
