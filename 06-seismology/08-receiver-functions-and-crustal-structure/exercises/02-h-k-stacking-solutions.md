# Solutions — 06-08-02 H-K Stacking and Crustal Thickness Estimation

> Read after attempting. Numbers computed, not hand-waved. Lesson:
> [02 H-K Stacking](../02-h-k-stacking.md).

---

## ★1 — The triplet

$v_s = v_p/k = 3.647\ \mathrm{km\,s^{-1}}$.
$q_p = \sqrt{0.026015-0.003600} = \sqrt{0.022415} = 0.149716$.
$q_s = \sqrt{0.075191-0.003600} = \sqrt{0.071591} = 0.267565$.

$$t_{Ps} = 35(0.117849) = 4.1247\ \mathrm{s},$$
$$t_{PpPs} = 35(0.417281) = 14.6048\ \mathrm{s},$$
$$t_{PpSs} = 2(35)(0.267565) = 18.7296\ \mathrm{s}.$$

Check: $t_{PpSs} = t_{Ps} + t_{PpPs}$ → $4.1247+14.6048 = 18.7295$ ✔ (rounding).

---

## ★2 — Why $t_{PpPs} = t_{Ps} + 2Hq_p$

PpPs has one more down-and-up P reverberation inside the layer than Ps, and that
extra loop costs $2Hq_p$ of vertical travel time.

---

## ★3 — Multiple moveout

$$t_{PpPs} = H(q_s+q_p), \qquad
\frac{\partial t_{PpPs}}{\partial p^{2}}
= -\frac{H}{2}\left(\frac{1}{q_s}+\frac{1}{q_p}\right).$$

For ★1: $(1/0.267565 + 1/0.149716) = 3.7374 + 6.6793 = 10.4167$;
$-35(10.4167)/2 = -182.3\ \mathrm{s}$ per $(\mathrm{s\,km^{-1}})^{2}$.

**Sign.** Negative, because both vertical slownesses *decrease* with $p$ and there
is no difference of $1/q$ terms to reverse the trend — unlike $t_{Ps}$, where
$(1/q_s - 1/q_p)$ is negative and the overall slope is positive.

---

## ★4 — Reply to the referee

"The 95% admitted set for $H$ spans 1.50 km because the receiver function
constrains a combination of $H$ and $k$ (a ridge), not $H$ alone; a $\pm0.1\
\mathrm{km}$ depth claim would require an independent constraint on $v_p/v_s$,
which this data set does not provide. With the ridge reported, the result is as
precise as the data permit; quoting a single point would overstate the
information."

---

## ★5 — Is 13% decisive?

Ratio $8.445/9.708 = 0.870$, so the second is $13.0\%$ lower. For a single
receiver function this is **not** decisive: the score is a weighted sum of a few
amplitude samples with their own noise, and a 13% difference is comparable to
what one noise realisation produces. The defensible statement is "model A is
preferred, but model B fits only 13% worse; the ridge includes both."

---

## ★6 — Weight-sensitivity test

Rerun the grid search for at least three weight sets spanning a plausible range
of relative reliability, e.g. $(0.8,0.2,0.1)$, $(0.7,0.2,0.1)$, $(0.5,0.3,0.2)$,
identically for polarities. Report for each: the best $(H,k)$ and the 95%
admitted set. **Report** whether the best $H$ moves by more than the admitted
range. If it does not, state that the result is weight-robust; if it does, report
the spread as part of the uncertainty and say the data cannot decide.

---

## ★7 — What limits the answer, and when noise takes over

At 16% noise the ridge ($1.50\ \mathrm{km}$) dominates the noise scatter
($0.14\ \mathrm{km}$) by a factor of about 11. Noise and ridge become comparable
when the noise-induced scatter grows to $\sim1.5\ \mathrm{km}$. The demo's
Monte Carlo at 16% gave $0.14\ \mathrm{km}$; if the scatter scales roughly
linearly with noise level, comparable limits require about $16\%\times
(1.50/0.14) \approx 170\%$ relative noise — i.e. the trace would be dominated by
noise and the stack would fail long before that. **Conclusion: for this design the
ridge always limits $H$; more events at the same noise cannot break it.**
