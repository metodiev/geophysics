# Solutions — 14-01-04 Well Hydraulics, Pumping Tests and Aquifer Parameters

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All tests and aquifers are **SYNTHETIC**.

Lesson: [04 Well Hydraulics, Pumping Tests and Aquifer Parameters](../04-well-hydraulics.md).

---

## ★1 — Transmissivity from the slope

$$T = \frac{2.3026\,Q}{4\pi\,\Delta s}
= \frac{2.3026 \times 500}{4\pi \times 1.20}
= \frac{1151.3}{15.080} = 76.35\ \mathrm{m^2\,d^{-1}}.$$

Units: $(\mathrm{m^3\,d^{-1}})/\mathrm{m} = \mathrm{m^2\,d^{-1}}$ ✔. If $Q$ had
been given in $\mathrm{m^3\,s^{-1}}$, the answer would be in
$\mathrm{m^2\,s^{-1}}$ and numerically 86,400 times smaller.

---

## ★2 — Storativity from the intercept

$$S = \frac{2.25\,T\,t_0}{r^{2}}
= \frac{2.25 \times 76.35 \times 0.0025}{30^{2}}
= \frac{0.42946}{900} = 4.772 \times 10^{-4}.$$

The value is a plausible confined storativity. Note that $t_0$ is an
*extrapolation*: the line reaches $s = 0$ at a time long before the first
measurement, so $S$ inherits whatever curvature contaminated the fitted window.

---

## ★3 — Validity of the fit window

$$u = \frac{r^{2}S}{4Tt} = \frac{900 \times 4.772 \times 10^{-4}}
{4 \times 76.35 \times 1} = \frac{0.42946}{305.4} = 1.406 \times 10^{-3}.$$

$u = 1.4 \times 10^{-3} < 0.01$, so the Cooper-Jacob form is valid at $t = 1$ d
with an error of about 0.03% (from the lesson's error table, interpolating between
$u = 10^{-3}$ and $5 \times 10^{-3}$). The criterion
$u<0.01$ is met after
$$t_{\min} = \frac{25r^{2}S}{T} = \frac{25 \times 900 \times 4.772 \times 10^{-4}}
{76.35} = 0.1406\ \mathrm{d} = 3.37\ \mathrm{h},$$
so the first 3.4 hours of the test must be excluded from the straight-line fit.

---

## ★★4 — Theis versus Cooper-Jacob at $t = 2$ d

$$u = \frac{100^{2} \times 1.0 \times 10^{-4}}{4 \times 250 \times 2}
= \frac{1.00}{2000} = 5.00 \times 10^{-4}.$$

$$W(u) = E_1(5.00 \times 10^{-4}) = 7.0242,$$
$$s = \frac{Q}{4\pi T}W(u) = \frac{1000}{4\pi \times 250} \times 7.0242
= 0.31831 \times 7.0242 = 2.2359\ \mathrm{m}.$$

Cooper-Jacob:
$$s = \frac{2.3026 \times 1000}{4\pi \times 250}
\log_{10}\frac{2.25 \times 250 \times 2}{100^{2} \times 1.0 \times 10^{-4}}
= 0.73300 \times \log_{10}(1125) = 0.73300 \times 3.05115
= 2.2363\ \mathrm{m}.$$

Difference: $2.2363 - 2.2359 = 0.0004$ m, i.e. $+0.018\%$ — consistent with the
lesson's table ($+0.013\%$ at $u = 10^{-3}$). **Comment:** at $u = 5 \times 10^{-4}$
the two forms are numerically indistinguishable; the choice between them is about
convenience, not accuracy.

---

## ★★5 — Recovery test

$t_p = 2$ d, $t = 4$ d, so $t - t_p = 2$ d:
$$u = \frac{100^{2} \times 1.0 \times 10^{-4}}{4 \times 250 \times 4}
= 2.50 \times 10^{-4}, \qquad
u' = \frac{100^{2} \times 1.0 \times 10^{-4}}{4 \times 250 \times 2}
= 5.00 \times 10^{-4}.$$

$$W(u) = E_1(2.50 \times 10^{-4}) = 7.7171, \qquad
W(u') = E_1(5.00 \times 10^{-4}) = 7.0242,$$
$$s' = 0.31831 \times (7.7171 - 7.0242) = 0.31831 \times 0.6929
= 0.2206\ \mathrm{m}.$$

Logarithmic check:
$$s' = \frac{2.3026 \times 1000}{4\pi \times 250}\log_{10}\frac{4}{2}
= 0.73300 \times 0.30103 = 0.2207\ \mathrm{m} \ \checkmark$$

Transmissivity from a measured recovery slope of 0.60 m per decade:
$$T = \frac{2.3026 \times 1000}{4\pi \times 0.60} = \frac{2302.6}{7.5398}
= 305.4\ \mathrm{m^2\,d^{-1}}.$$

**What assumption about $S$?** None. The slope of $s'$ against
$\log_{10}[t/(t-t_p)]$ contains only $Q$ and $T$; $S$ cancels from the
superposition because it appears symmetrically in $u$ and $u'$ and, in the
logarithmic limit, $W(u) - W(u') \to \ln(u'/u) = \ln[t/(t-t_p)]$. That is why a
recovery test is the robust route to $T$.

---

## ★★6 — Step-drawdown analysis

| $Q$ (m$^3$ d$^{-1}$) | $s_w$ (m) | $s_w/Q$ (d m$^{-2}$) |
|---|---|---|
| 300 | 1.035 | 0.003450 |
| 900 | 3.915 | 0.004350 |
| 1800 | 10.260 | 0.005700 |

Linear regression of $s_w/Q$ on $Q$:
$$C = \text{slope} = \frac{\sum (Q_i-\bar Q)(y_i-\bar y)}{\sum (Q_i-\bar Q)^{2}}
= 1.50 \times 10^{-6}\ \mathrm{d^2\,m^{-5}},$$
$$B = \text{intercept} = \bar y - C\bar Q = 0.004500 - 1.50 \times 10^{-6} \times 1000
= 3.00 \times 10^{-3}\ \mathrm{d\,m^{-2}}.$$

(The data were generated from exactly these values, so the recovery is exact;
with 0.02 m of noise it would be good to about 1%.)

Efficiencies, $E = BQ/(BQ + CQ^{2})$:

| $Q$ | $BQ$ (m) | $CQ^{2}$ (m) | $E$ |
|---|---|---|---|
| 300 | 0.900 | 0.135 | 87.0% |
| 900 | 2.700 | 1.215 | 69.0% |
| 1800 | 5.400 | 4.860 | 52.6% |
| 2700 | 8.100 | 10.935 | 42.6% |

**Comment.** The aquifer's contribution ($BQ$) is exactly linear in $Q$; all of
the efficiency loss is the quadratic well term. Reporting "T decreased at higher
pumping rates" would be wrong — the *well* got less efficient, and the aquifer
never changed.

---

## ★★★7 — Designing a pumping test for $T$ (10%) and $S$ (25%)

Truth: $T = 150\ \mathrm{m^2\,d^{-1}}$, $S = 2.0 \times 10^{-4}$, confined,
saturated thickness $b = 20$ m (so dewatering is not a concern for a few metres of
drawdown), assumed transmissivity-to-noise-limited conditions.

**Step 1 — pick the rate so the drawdown is well above the noise.** Assume a
transducer with 5 mm resolution and a stated datum, so a usable signal is
$\gtrsim 10 \times$ the noise, i.e. $s \ge 0.05$ m at the observation well by the
end of the test. Using the logarithmic form at one day,
$$\Delta s \text{ per decade} = \frac{2.3026Q}{4\pi T} = 0.0012217\,Q\
[\mathrm{m\ per\ decade\ with\ } Q \mathrm{\ in\ m^3\,d^{-1}}].$$
With $Q = 400\ \mathrm{m^3\,d^{-1}}$, $\Delta s = 0.489\ \mathrm{m}$ per decade.
At $r = 60$ m, $t = 1$ d:
$$u = \frac{60^{2} \times 2.0 \times 10^{-4}}{4 \times 150 \times 1}
= 1.20 \times 10^{-3},$$
$$s \approx 0.489\log_{10}\frac{2.25 \times 150 \times 1}{3600 \times 2.0 \times 10^{-4}}
= 0.489\log_{10}(468.8) = 0.489 \times 2.671 = 1.306\ \mathrm{m},$$
which is 261 times the noise. Ample.

**Step 2 — choose $r$ so that $u<0.01$ early enough to fit.** The valid window
starts at
$$t_{\min} = \frac{25r^{2}S}{T}
= \frac{25 \times 3600 \times 2.0 \times 10^{-4}}{150} = 0.12\ \mathrm{d}
= 2.88\ \mathrm{h}.$$
A 2-day test therefore provides 1.88 days of valid data spanning
$\log_{10}(2/0.12) = 1.22$ decades — enough for a slope, and marginally enough for
the intercept. To gain a full decade instead, place a second observation well at
$r = 25$ m, where $t_{\min} = 25 \times 625 \times 2.0 \times 10^{-4}/150
= 0.021\ \mathrm{d} = 0.5$ h, giving 1.6 decades.

**Step 3 — check that no boundary is met and no dewatering occurs.** A boundary at
distance $L$ becomes visible when $\sqrt{4Dt} \sim L$ with
$D = T/S = 150/2.0 \times 10^{-4} = 7.5 \times 10^{5}\ \mathrm{m^2\,d^{-1}}$:
$$L \sim \sqrt{4 \times 7.5 \times 10^{5} \times 2} = 2450\ \mathrm{m}.$$
So no boundary within about 2.5 km is a design requirement — and if one is closer,
the test must be shortened or the boundary modelled explicitly. Dewatering: total
drawdown at the pumped well is larger than at $r = 60$ m; with $B$ of order
$3 \times 10^{-3}$ d m$^{-2}$, $s_w \approx 0.003 \times 400 = 1.2$ m plus well
loss, well below the 20 m saturated thickness ✔.

**Step 4 — sampling schedule.** Drawdown is logarithmic in time, so sample
logarithmically: every 10 s for the first 2 min, 30 s to 10 min, 2 min to 1 h,
15 min to 6 h, hourly to 48 h, then a recovery phase with the same schedule for
about 1–2 times $t_p$.

**Step 5 — precision arithmetic.** $T$ is set by the slope; with $N$ points spread
over $D$ decades of $\log_{10}t$ and a per-point noise $\sigma$,
$$\sigma_T/T \approx \frac{\sigma}{\Delta s_{\text{decade}}\,D\sqrt{N_{\text{eff}}}}.$$
With $\sigma = 5$ mm, $\Delta s = 0.489$ m per decade, $D = 1.22$ decades and
$N_{\text{eff}} \approx 12$ independent points (noise is correlated over adjacent
samples, so $N_{\text{eff}} < N$):
$$\sigma_T/T \approx \frac{0.005}{0.489 \times 1.22 \times 3.46} = 0.0024
= 0.24\%,$$
comfortably inside 10%. $S$ is set by the intercept, which is extrapolated far
outside the data; a rule of thumb from the lesson's measured behaviour is that
$\sigma_S/S$ is 5–20 times $\sigma_T/T$, giving 1–5% here — also inside 25%, but
only if the window is chosen correctly. Adding the second well at $r = 25$ m and
fitting both curves simultaneously for a common $(T, S)$ is the single most
effective improvement.

**Step 6 — the measurement that does not use Theis.** A **recovery test** after
shut-in: its slope gives $T$ with no assumption about $S$ and no reliance on the
early-time window. Agreement between the pumping-phase $T$ and the recovery-phase
$T$ within their stated uncertainties is the strongest internal check available
from one well, and it detects a variable pumping rate or a developing boundary.

---

## ★★★8 — Delayed yield and the factor of 500

**The numbers.** Take $T = 150\ \mathrm{m^2\,d^{-1}}$ (as in ★★★7). For the unconfined aquifer,
$$S_{\text{early}} = S_s b = 1.5 \times 10^{-5} \times 20 = 3.0 \times 10^{-4},
\qquad S_y = 0.15, \qquad \frac{S_y}{S_s b} = \frac{0.15}{3.0 \times 10^{-4}}
= 500.$$

Physically, the first hour of pumping only lowers the water table in the immediate
vicinity and the water released comes almost entirely from **elastic compression
and water expansion**, exactly as in a confined aquifer. Gravity drainage of pores
takes minutes to hours to deliver its water to the water table, so $S_y$ does not
enter the early response at all.

**Why a first-hour Theis fit reports the wrong number.** Over the first hour at
$r = 30$ m with $T = 150\ \mathrm{m^2\,d^{-1}}$:
$$u_{\text{early}} = \frac{900 \times 3.0 \times 10^{-4}}{4 \times 150 \times 0.0417}
= \frac{0.270}{25.0} = 0.0108,$$
so the early data *do* fall in the straight-line regime — but with the
confined-like storage. A fit using $S = 3.0 \times 10^{-4}$ reproduces them
beautifully. The same well measured at late time (say $t = 5$ d, by which point
the drainage has caught up) is described by $S = S_y = 0.15$. Fitting the first
hour and calling the result "the storativity" understates the drainable storage by
a factor of 500, and would understate the sustainable yield of the aquifer by the
same factor.

**How the error appears on an $s$-versus-$\log t$ plot.** Three straight-ish
segments instead of one:

1. an early segment with the **small** slope imposed by $S_s b$ (equivalently, the
   curve is displaced downward relative to the $S_y$ line by
   $\frac{2.3026Q}{4\pi T}\log_{10}(S_y/S_s b) =
   \frac{2.3026Q}{4\pi T} \times 2.70$);
2. a transitional **S-shaped** segment of decreasing slope as gravity drainage
   delivers water — drawdown actually levels off or even recovers briefly before
   resuming;
3. a late segment parallel to the first, offset upward, with $S = S_y$.

**Fitting strategy.** Fit the **late** straight-line segment for $S_y$; report the
early segment separately as $S_s b$; and fit the whole curve with a delayed-yield
model (or a numerical model) if an intermediate-time prediction is needed. Do not
fit a single Theis curve to all three segments: the residual pattern will be
systematic, and the recovered $S$ will be an artefact of the window.

**Diagnostic that separates delayed yield from leakage.** Leakage makes the
drawdown **flatten towards a steady value and stay there** (the response approaches
steady state and never resumes a logarithmic rise), whereas delayed yield produces
an **S-shaped return to a steeper, parallel logarithmic line** after the
transition. The test is the *late-time* slope: with delayed yield the late slope
equals the early slope; with leakage the late slope tends to zero. A second,
independent check is to observe the water table in a shallow observation well — it
responds late to delayed yield but shows a steady vertical gradient under leakage.

---

## Mastery checkpoint — worked

Synthetic test: $Q = 1200\ \mathrm{m^3\,d^{-1}}$, $r = 80$ m, fitted slope
$0.55$ m per decade, intercept $2.20$ m (at $s = 0$, i.e. the intercept is
$\log_{10} t_0$ in the form $s = \text{slope}\times\log_{10}t + \text{intercept}$).

**(a) Transmissivity.**
$$T = \frac{2.3026\,Q}{4\pi\,\Delta s}
= \frac{2.3026 \times 1200}{4\pi \times 0.55} = \frac{2763.1}{6.9115}
= 399.8\ \mathrm{m^2\,d^{-1}}.$$

**(b) Intercept time and storativity.**
$$t_0 = 10^{-\text{intercept}/\text{slope}} = 10^{-2.20/0.55} = 10^{-4.000}
= 1.000 \times 10^{-4}\ \mathrm{d} = 8.64\ \mathrm{s},$$
$$S = \frac{2.25\,T\,t_0}{r^{2}}
= \frac{2.25 \times 399.8 \times 1.000 \times 10^{-4}}{6400}
= \frac{0.08995}{6400} = 1.406 \times 10^{-5}.$$

**(c) Validity at $t = 1$ d.** $u = r^{2}S/(4Tt) = 6400 \times 1.406 \times 10^{-5}
/(4 \times 399.8) = 0.08995/1599.2 = 5.63 \times 10^{-5} \ll 0.01$, so the
Cooper-Jacob window is valid at 1 d. In fact
$t_{\min} = 25r^{2}S/T = 25 \times 6400 \times 1.406 \times 10^{-5}/399.8
= 0.00563$ d = 8.1 min: the test qualifies almost immediately, which is a warning
sign in itself — the fit window is very long relative to $t_0$, so the intercept is
a long extrapolation.

**(d) Is $S = 1.4 \times 10^{-5}$ physical?** For $b = 20$ m,
$$S_s = \frac{S}{b} = \frac{1.406 \times 10^{-5}}{20}
= 7.03 \times 10^{-7}\ \mathrm{m^{-1}}.$$
Inverting $S_s = \rho_w g(\alpha + n\beta_w)$ with $\rho_w g = 9810\
\mathrm{kg\,m^{-2}\,s^{-2}}$, $n = 0.25$ and $\beta_w = 4.4 \times 10^{-10}\
\mathrm{Pa^{-1}}$:
$$\alpha = \frac{S_s}{\rho_w g} - n\beta_w
= 7.16 \times 10^{-11} - 1.10 \times 10^{-10}
= -3.8 \times 10^{-11}\ \mathrm{Pa^{-1}} < 0.$$
A **negative** rock compressibility is impossible. The recovered $S$ is therefore
too small to be physically admissible for that thickness, and the intercept — not
the slope — is the suspect quantity. The likely causes, in order: leakage or a
boundary flattening the late-time curve (which biases the straight line), a
prolonged wellbore-storage segment at early time, or an incorrect (too large) $r$.
The correct response is not to report $1.4 \times 10^{-5}$ but to report that
$S$ is only bounded above, and to redesign the test with a closer observation well
so that $t_0$ falls inside the measured window.

**(e) What changed after rehabilitation?** The slope is set by $2.3026Q/(4\pi T)$
and is unchanged, so $T$ is unchanged — the aquifer was never the problem. The
drawdown at the same rate fell by 0.8 m, and since $s_w = BQ + CQ^{2}$ with $B$
fixed by the (unchanged) aquifer, the improvement is entirely in $C$:

$$C_{\text{before}} - C_{\text{after}} = \frac{0.8}{Q^{2}}
= \frac{0.8}{1200^{2}} = 5.6 \times 10^{-7}\ \mathrm{d^2\,m^{-5}}.$$

**Report it as** an increase in well efficiency,
$E = BQ/(BQ + CQ^{2})$, at the stated rate — not as an increase in transmissivity.
And re-run a step-drawdown test at several rates, because a single rate cannot
separate $B$ from $C$.
