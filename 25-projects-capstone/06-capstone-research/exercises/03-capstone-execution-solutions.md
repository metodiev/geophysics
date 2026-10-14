# Solutions — 25-06-03 Capstone: Data, Modelling and Uncertainty Analysis

Reference solutions. Every number is printed by
[`code/capstone_execution_demo.py`](../code/capstone_execution_demo.py) or derived from
its printed values; the setting is **SYNTHETIC**.

## ★1. The estimator and its units

$$H = \frac{t}{\eta_s-\eta_p},\qquad
\eta_s = \sqrt{\frac{k^2}{V_p^2}-p^2},\qquad
\eta_p = \sqrt{\frac{1}{V_p^2}-p^2},$$

with $k = V_p/V_s$ dimensionless, $V_p$ in km/s, so both $\eta$ are in s/km; the
product $H(\eta_s-\eta_p)$ is in seconds, and $t$ is a time in seconds, so $H$ comes out
in kilometres. For $t = 4.3493$ s the exact inversion returns $H = 35.00$ km — the
analytic check of §2 of the lesson, and the first thing to verify, because a units error
here would produce a plausible-looking number in the wrong unit.

## ★2. The slowness difference

$$\eta_s = \sqrt{\frac{1.75^2}{6.30^2} - 0.06^2} = \sqrt{0.0771605 - 0.0036} = 0.271220,$$
$$\eta_p = \sqrt{\frac{1}{6.30^2} - 0.06^2} = \sqrt{0.0251953 - 0.0036} = 0.146954,$$
$$\eta_s - \eta_p = 0.124266\ \mathrm{s\,km^{-1}}
\quad\Longrightarrow\quad
H = \frac{4.3493}{0.124266} = 35.00\ \mathrm{km},$$

matching the printed value. The sensitivity of $H$ to the inputs follows immediately
from these two numbers: $H \propto t$ exactly, and
$\partial H/\partial k = -H/(\eta_s-\eta_p)\cdot\partial(\eta_s)/\partial k
\approx -H k/(V_p^2\eta_s(\eta_s-\eta_p)) = -0.1388\ \mathrm{km}$ per unit $k$, i.e.
about $46$ km per unit $k$, or $1.38$ km for $\sigma_k = 0.03$ — the budget's largest
term, obtained analytically.

## ★3. What the statistical interval is an interval for

The statistical-only standard deviation is $\sigma_H = H\,\sigma_t/t = 35.04 \times
0.15/4.3493 = 1.208$ km, so the 95% interval is

$$H = 35.04 \pm 1.96 \times 1.208 = 35.04 \pm 2.37\ \mathrm{km}.$$

It is an interval for *the depth that would be obtained if the assumed $V_p$, $V_p/V_s$
and $p$ were exactly right and the measurement were repeated*. It is not an interval for
the crustal thickness. For it to become one, $V_p/V_s$, $V_p$ and $p$ would have to be
known exactly — and the systematic term they contribute (1.600 km, 64% of the variance)
is larger than the statistical term, so the interval as quoted understates the
uncertainty of the scientific quantity by a factor
$2.001/1.198 = 1.67$ in standard deviation (it might be quoted as $2.37$ km when the
honest number is $3.92$ km).

## ★★4. Quadrature versus addition

$$\sqrt{1.198^2 + 1.600^2} = \sqrt{1.4352 + 2.5600} = \sqrt{3.9952} = 1.9988\
\mathrm{km},$$

matching the printed $1.998$ km against the sampled $2.001$ km — a $0.14\%$ agreement,
which is the quantitative evidence that the model is nearly linear over the input
ranges (an exactly linear model would give exact equality; interaction between inputs
would show as a difference). Adding instead of combining in quadrature gives
$1.198 + 1.600 = 2.798$ km, an overstatement of

$$\frac{2.798 - 2.001}{2.001} = 40\%,$$

and the overstatement grows with the number of comparable terms: for $n$ equal terms,
addition overstates by $\sqrt n$.

## ★★5. The effect of improving the dominant input

The contribution of an input scales linearly with its uncertainty, so halving
$\sigma_k$ from $0.03$ to $0.015$ gives $1.378/2 = 0.689$ km, and reducing it to
$0.01$ gives $1.378 \times (0.01/0.03) = 0.459$ km. With the other terms unchanged:

| $\sigma_k$ | $k$ contribution | total sd | improvement |
|---|---|---|---|
| 0.03 | 1.378 | 2.001 | — |
| 0.015 | 0.689 | $1.629$ | $19\%$ |
| 0.010 | 0.459 | $1.546$ | $23\%$ |

Compare with the value of measurement effort: halving the picking error buys $15\%$.
Reducing $\sigma_k$ by a factor of three — a joint $V_p/V_s$ determination from the same
waveforms, which costs processing time rather than field time — buys $23\%$. The
arithmetic of the budget, not the intuition, identifies the cheaper route.

## ★★6. What it takes to make the statistical term dominant

The statistical contribution is 1.208 km (the printed 1.198 km is the sampled value;
the analytic one is $H\sigma_t/t = 1.208$), and the systematic total is 1.600 km. For
the systematic to fall below the statistical:

$$0.756^2 + x_k^2 + 0.271^2 < 1.208^2
\quad\Longrightarrow\quad
x_k^2 < 1.4593 - 0.5715 - 0.0734 = 0.8144,$$

$$x_k < 0.902\ \mathrm{km}
\quad\Longrightarrow\quad
\sigma_k < 0.03 \times \frac{0.902}{1.378} = 0.0196 .$$

**A $V_p/V_s$ known to $\pm 0.02$ makes the statistical term dominant**, and that
precision is attainable by the same station's H-K analysis or a joint inversion — it
does not require a new survey. The opposite route is impossible: the statistical
contribution is $H\sigma_t/t$, so making it *dominant* would require
$\sigma_t > 1.600 \times 4.3493/35.04 = 0.199$ s — a *worse* measurement than the one
in hand. **Uncertainty budgets are reduced at the assumption end, not at the
measurement end, whenever the systematic term dominates.**

## ★★7. Coverage is not agreement with the truth

The coverage check answers: "if I repeat this measurement many times, how often does
the interval I compute contain the *known* value?" It says nothing about whether a
*single* interval contains the truth — that is a property of the interval, not of the
draw, and no single realization can verify it. What the interval delivers is a
**long-run frequency guarantee under stated assumptions**: (i) the measurement error is
Gaussian with the stated $\sigma_t$, (ii) the estimator is unbiased, and (iii) the
assumed parameters are correct. The demonstration's 95.1% holds under (i)–(iii)
simultaneously; in the real case, (iii) is false by construction, which is exactly why
the statistical interval is not the result's uncertainty (★★3).

## ★★8. The provenance log for this analysis

| content | concrete entry |
|---|---|
| query and filters | FDSN dataselect request, network/station list, channel, window 30 s before the P pick, 40 stations accepted of 52 requested, SHA-256 of the downloaded archive |
| environment | Python 3.14 in `.venv`, `numpy 2.x`, `scipy 1.x`, lock file commit `a1b2c3`, command line recorded in the workflow log |
| steps | `fetch_waveforms.py` → `rotate_and_deconvolve.py` (Gaussian half-width 0.5 s) → `hk_grid.py` (grid 20–60 km × 1.60–2.00) → `headline.py` → `figure_03.py`, each with its input and output hashes |
| decisions | Gaussian half-width 0.5 s chosen, tested at 0.3 and 0.8 s (±0.4 km in $H$); $V_p$ taken as $6.30 \pm 0.15$ from a published regional value; $p$ from the event distance; damping grid 161 × 81 |
| freeze point | commit `d4e5f6` at which `headline.py` first produced $H = 35.04$ km; the subsequent change of the filter width to 0.8 s is recorded as a delta with the before/after values ($35.04$ and $34.62$ km) |

The freeze-point entry is the one that converts the log from bookkeeping into
integrity: it makes every later change visible, including the ones made for
presentational reasons.

## ★★★9. A design whose dominant term is statistical

**Target.** Make $S_t$ the largest index, and specifically make the systematic
contribution smaller than the statistical one, so that additional data would genuinely
improve the result.

**1. Inputs to measure rather than assume.**

| input | current | target | observation that delivers it |
|---|---|---|---|
| $V_p/V_s$ | assumed $\pm 0.03$ | $\pm 0.015$ | joint H-K + receiver-function waveform inversion at the same stations, which returns $k$ and its uncertainty |
| $V_p$ | assumed $\pm 0.15$ km/s | $\pm 0.08$ km/s | regional refraction/wide-angle profile, or a nearby borehole check shot; if unavailable, a joint inversion with surface-wave dispersion constrains the $V_s$ path independently of the assumed $V_p$ |
| $p$ | assumed $\pm 0.005$ s/km | $\pm 0.002$ s/km | recompute from the event catalogue's own distance and depth uncertainties rather than a nominal value |

**2. Resulting budget.** With the contributions scaled linearly: $k$ from 1.378 to
$0.689$, $V_p$ from 0.756 to 0.403, $p$ from 0.271 to 0.108 km, and the statistical
term held at 1.208 km:

$$\sigma_\text{sys} = \sqrt{0.689^2 + 0.403^2 + 0.108^2} = 0.807\ \mathrm{km},\qquad
\sigma_\text{total} = \sqrt{1.208^2 + 0.807^2} = 1.453\ \mathrm{km},$$

so the statistical term now carries $1.208^2/1.453^2 = 69\%$ of the variance and
$S_t \approx 0.69$ dominates the budget. A further halving of $\sigma_t$ (better
picking and more stations, §3 of the lesson) would then bring the total to
$\sqrt{0.604^2+0.807^2} = 1.008$ km — a $31\%$ improvement that was **impossible
before** the assumptions were measured, which is the point of the redesign.

**3. Cost.** Processing time for the joint inversion (days, not weeks) and a literature
or field effort to obtain the regional $V_p$ (one to two weeks, with a fallback to a
published value with a stated uncertainty). No new seismic deployment is required —
which is why this is the redesign a capstone can actually execute.

**4. Verification.**

- *Analytic*: substitute the generating parameters into the joint estimator and check
  the recovery of $k$ to machine precision.
- *Recovery/coverage*: synthtic receiver functions from known $H$, $k$ and $V_p$; check
  that the joint inversion's $k$ is unbiased and that its 95% interval covers the truth
  in 95% of replicates. This is the verification that must pass *before* the reduced
  $\sigma_k$ is used.
- *End-to-end*: run the full pipeline on the synthetic dataset and require the final
  figure to recover the known $H$ within the quoted interval.

**5. The test that the systematic term is genuinely reduced.** Reduce the assumed
$\sigma_k$ by a factor of two in the budget while leaving the *data and the inversion
unchanged*, and confirm that the recovered $k$ and its interval do not move. If the
interval narrows only because the assumption was tightened, the budget has been edited
rather than improved — the failure mode this exercise is designed to catch.
