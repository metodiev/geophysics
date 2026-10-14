# Solutions — 06-03-05 Source Spectra, Corner Frequency and Stress Drop

> **Read after attempting the exercises.** All values are SYNTHETIC. Arithmetic is
> shown; where a hand value is compared with the demo, the difference is
> explained.

Lesson: [05 Source Spectra, Corner Frequency and Stress Drop](../05-source-spectra.md).

Constants: $\beta = 3500\ \mathrm{m\,s^{-1}}$,
$\mu = 3.0\times10^{10}\ \mathrm{Pa}$, $k = 0.37$ (model choice), and
$k\beta = 1295\ \mathrm{m\,s^{-1}}$.

---

## ★1 — Radius and corner frequency

From $M_0 = \tfrac{16}{7}\Delta\sigma a^{3}$,

$$a^{3} = \frac{7}{16}\frac{M_0}{\Delta\sigma}
= 0.43750\times\frac{1.0\times10^{20}}{5.0\times10^{6}}
= 0.43750\times2.0\times10^{13} = 8.750\times10^{12},$$
$$a = \left(8.750\times10^{12}\right)^{1/3} = 2.06064\times10^{4}
= 20606.4\ \mathrm{m} \approx 20.6\ \mathrm{km}.$$

$$f_c = \frac{k\beta}{a} = \frac{0.37\times3500}{20606.4} = \frac{1295}{20606.4}
= 0.062844\ \mathrm{Hz}.$$

---

## ★2 — Asymptotes

$$\Omega(f_c/2) = \frac{\Omega_0}{1+0.25} = \frac{\Omega_0}{1.25}
= 0.8000\,\Omega_0,$$
$$\Omega(2f_c) = \frac{\Omega_0}{1+4} = \frac{\Omega_0}{5} = 0.2000\,\Omega_0.$$

At $f_c/2$ the value is still $80\%$ of the plateau; at $2f_c$ it has fallen to
$20\%$. The asymptotes are

- $f\ll f_c$: $\Omega\to\Omega_0$, a **flat** (zero-slope) plateau;
- $f\gg f_c$: $\Omega\to\Omega_0f_c^{2}f^{-2}$, a slope of $-2$ on a
  $\log\Omega$–$\log f$ plot.

The corner is where the two straight asymptote lines cross, which is how the demo
measures it.

---

## ★3 — Inverting back to stress drop

$$\Delta\sigma = \frac{7}{16}M_0\left(\frac{f_c}{k\beta}\right)^{3}
= 0.43750\times1.0\times10^{20}\left(\frac{0.062844}{1295}\right)^{3}.$$

$$\frac{0.062844}{1295} = 4.8528\times10^{-5}, \qquad
\left(4.8528\times10^{-5}\right)^{3} = 1.14282\times10^{-13},$$
$$\Delta\sigma = 0.43750\times10^{20}\times1.14282\times10^{-13}
= 0.43750\times1.14282\times10^{7}
= 5.000\times10^{6}\ \mathrm{Pa} = 5.00\ \mathrm{MPa}. ☑$$

The inversion is exact by construction: the two model relations were built with
the same $k$, so nothing is left over but rounding.

---

## ★4 — Inverting with a wrong $k$

$$\Delta\sigma(k') = \Delta\sigma(k)\left(\frac{k}{k'}\right)^{3}.$$

- $k' = 0.20$: $\left(0.37/0.20\right)^{3} = 1.85^{3} = 6.3316$, so
  $\Delta\sigma = 5.0\times6.3316 = 31.66\ \mathrm{MPa}$.
- $k' = 0.50$: $\left(0.37/0.50\right)^{3} = 0.74^{3} = 0.40522$, so
  $\Delta\sigma = 5.0\times0.40522 = 2.026\ \mathrm{MPa}$.

Ratio between them: $31.66/2.026 = 15.63$ — a factor of fifteen, from the choice
of one dimensionless constant. Both $0.20$ and $0.50$ are conventions in use.

**Does $M_0$ change?** No. $M_0$ comes from the low-frequency plateau,
$\Omega_0\propto M_0$, which does not involve $k$ at all. Only the derived
*length* and *stress drop* move: $a$ scales as $k$, so with $k' = 0.20$ the
inferred radius is $0.20/0.37 = 0.541$ of the true one.

---

## ★5 — Mean slip

$$\bar D = \frac{16}{7\pi}\frac{\Delta\sigma}{\mu}a
= 0.727575\times\frac{5.0\times10^{6}}{3.0\times10^{10}}\times20606.4.$$

$$\frac{\Delta\sigma}{\mu} = 1.66667\times10^{-4},\qquad
0.727575\times1.66667\times10^{-4} = 1.21263\times10^{-4},$$
$$\bar D = 1.21263\times10^{-4}\times20606.4 = 2.4988\ \mathrm{m}.$$

**Check** with $M_0 = \mu\pi a^{2}\bar D$:

$$\mu\pi a^{2} = 3.0\times10^{10}\times3.14159\times\left(2.06064\times10^{4}\right)^{2}
= 3.0\times10^{10}\times3.14159\times4.24624\times10^{8} = 4.0022\times10^{19},$$
$$\mu\pi a^{2}\bar D = 4.0022\times10^{19}\times2.4988 = 1.000\times10^{20}
= M_0. ☑$$

---

## ★6 — The $M_0$–$f_c$ exponent from two points

Point 1: $f_c = 25.9\ \mathrm{Hz}$, $M_0 = 8.5714\times10^{11}\ \mathrm{N\,m}$.
Point 2: $f_c = 0.259\ \mathrm{Hz}$, $M_0 = 8.5714\times10^{17}\ \mathrm{N\,m}$.

$$p = \frac{\log_{10}(M_{0,2}/M_{0,1})}{\log_{10}(f_{c,2}/f_{c,1})}
= \frac{\log_{10}(10^{6})}{\log_{10}(0.259/25.9)}
= \frac{6}{\log_{10}(0.01)} = \frac{6}{-2} = -3.000.$$

**Implication for the slip.** Since $M_0 = \mu\pi a^{2}\bar D$ and
$f_c\propto a^{-1}$, the constant exponent $-3$ together with constant stress
drop requires $\bar D\propto a$: the slip grows **linearly** with radius. The demo
tabularises it ($a = 50,\ 500,\ 5000\ \mathrm{m}\to\bar D = 0.0036,\ 0.0364,\
0.3638\ \mathrm{m}$). A ten-fold longer rupture slips ten times as far — which is
exactly what "the same stress drop at every size" means, and is why a single
exponent describes the population.

---

## ★7 — Saturation exponents

**(a) Band $10^{-4}$–$10^{-3}\ \mathrm{Hz}$.** This band lies **below** $f_c$ for
every row (the smallest $f_c$ is $0.00530\ \mathrm{Hz}$, still above
$10^{-3}\ \mathrm{Hz}$), so the amplitude is the plateau and scales as $M_0$.

$$\text{ratio} = \frac{9.8464\times10^{22}}{9.9744\times10^{17}}
= 9.8717\times10^{4},\qquad
p = \frac{\log_{10}(9.8717\times10^{4})}{5.000} = \frac{4.99439}{5.000}
= 0.99888.$$

**(b) Band $2$–$10\ \mathrm{Hz}$.** This band lies **above** $f_c$, where
$\Omega\propto\Omega_0f_c^{2}\propto M_0^{1/3}$.

$$\text{ratio} = \frac{1.4021\times10^{17}}{3.0021\times10^{15}} = 46.70,\qquad
p = \frac{\log_{10}(46.70)}{5.000} = \frac{1.66936}{5.000} = 0.33387.$$

**Comparison.** The demo's fitted values are $0.999089$ and $0.333771$; the
two-point estimates are $0.99888$ and $0.33387$, lower and higher by $0.02\%$ and
$0.03\%$ respectively. The two-point estimate is a chord slope between the
extreme rows, while the demo fits 60 sources across the whole family, so the
difference is the small curvature of the relation introduced by the finite band
edges moving relative to $f_c$. Both agree with the predictions $1$ and $1/3$ to
three decimals.

---

## ★8 — Does stress drop vary with depth? (specification)

**The obstacle.** Absolute stress drop requires $k$, which cannot be measured
independently from a single spectrum. Any absolute trend could be a trend in $k$
through the depth-dependent slip-velocity function.

**What to hold fixed.** (i) One spectral model ($\omega^{-2}$) and one inversion
code; (ii) one value of $k$ for the *whole* population, so that even if $k$ is
wrong it is wrong identically everywhere; (iii) one value of $\beta$ per depth,
taken from a measured velocity model, and reported.

**What to compare — a relative statistic.** Not $\Delta\sigma(z)$, but the
**ratio** of stress drops between two depth populations, or the slope of
$\log\Delta\sigma$ against $z$. Because
$\Delta\sigma_{\text{inferred}} = \Delta\sigma_{\text{true}}(k/k')^{3}$, a common
$k'$ cancels in every ratio: relative trends are $k$-independent (this is exercise
★★★10). The reportable result is
$\mathrm{d}\log\Delta\sigma/\mathrm{d}z$ with its confidence interval, not an
absolute value.

**Data needed.** Several hundred events with (a) well-constrained depths
(a relocated catalogue, not routine locations), (b) spectra covering $f_c$ at the
station used, (c) computed corner frequencies with quantified uncertainty, and (d)
an independent depth-controlled comparison of source-to-station paths so that a
$t^{*}$ difference does not masquerade as an $f_c$ difference.

**Residual model dependence.** The assumption that $k$ is depth-*independent* is
the load-bearing one. It fails if the slip-velocity function changes with depth —
for instance because of a change in normal stress or in the frictional regime —
and no amount of data can test it from spectra alone. A second, independent
constraint on source dimension (e.g. a well-located aftershock volume, or a
finite-fault inversion) is required to close the gap.

---

## ★9 — Testing the $\omega^{-2}$ assumption (specification)

**Observable.** The source spectrum $S(f) = U(f)/I(f)\cdot
\exp(+\pi ft^{*})$, i.e. the recorded spectrum corrected for instrument and
attenuation, for many events at one station. Because the correction needs
$t^{*}$, work with the *ratio* of spectra of events with similar paths.

**Competing models.** (i) the $\omega^{-2}$ model with a single corner;
(ii) a general decay exponent $\Omega\propto f^{-n}$ with $n$ free;
(iii) two-corner models with a second break at high frequency. Fit each by
least squares in $\log\Omega$ versus $\log f$ over a stated band.

**Fit statistic.** Residual rms in log space, with an $F$-test or an
information criterion for the extra parameters in (ii) and (iii); report the
distribution of the fitted $n$ over events, not a single value.

**The degeneracy to break.** A larger $t^{*}$ mimics a steeper source decay: at
high frequency both $e^{-\pi ft^{*}}$ and $f^{-n}$ remove energy, and over a
finite band they are nearly interchangeable. Break it by (a) using events of
*different* $f_c$ recorded at the *same* station, since $t^{*}$ is common and
$f_c$ differs; and (b) using the same event at several stations, since $f_c$ is
common and $t^{*}$ differs. Only the *intersection* of the two families separates
the source from the path.

---

## ★10 — Relative stress drops are $k$-independent

With $\Delta\sigma = \tfrac{7}{16}M_0\left(f_c/(k\beta)\right)^{3}$ and a common
$k$, the ratio of two inferred stress drops is

$$\frac{\Delta\sigma_2}{\Delta\sigma_1}
= \frac{M_{0,2}}{M_{0,1}}
\left(\frac{f_{c,2}}{f_{c,1}}\right)^{3}
\frac{(k_2/k_1)^{3}}{(k_2/k_1)^{3}}
= \frac{M_{0,2}}{M_{0,1}}\left(\frac{f_{c,2}}{f_{c,1}}\right)^{3}.$$

The factor $(1/k)^{3}$ cancels *identically*. So any statement of the form "stress
drops within this population differ by a factor $X$" is independent of the model
constant, whereas any statement of the form "the stress drop is $Y\ \mathrm{MPa}$"
is not.

**Observational requirement.** The two events must be analysed with the *same*
spectral model, the *same* inversion code, and — for the cancellation to be
physical rather than arithmetic — a $k$ that really is common. If $f_c$ is
measured in different bands for the two events, or corrected with different
$t^{*}$, the ratio is contaminated before $k$ ever enters.

**How it can fail.** If $k$ is *not* constant — for instance if it depends on the
source size (a genuine non-self-similarity) or on the assumed slip pulse that is
inferred per event — then the cancellation is only apparent: the two events are
being compared through two different model constants, and the ratio silently
carries the difference. The honest statement is then a ratio *given a fixed,
stated $k$*, with the $k$-dependence of the difference between $k$ values reported
as a systematic uncertainty.
