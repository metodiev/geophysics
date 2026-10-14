# Exercises — 25-02-01 Project: Travel-Time Curves and 1-D Velocity Structure

Attempt these before reading the
[solutions](./01-travel-time-curves-solutions.md). The project is
[01 Travel-Time Curves](../01-travel-time-curves.md). Values printed by
[`code/travel_time_curves_demo.py`](../code/travel_time_curves_demo.py):

| Quantity | Demonstration value |
|---|---|
| model | $V_1 = 5.90$, $V_2 = 8.05\ \mathrm{km\,s^{-1}}$, $H_1 = 32.0\ \mathrm{km}$ |
| critical angle | $47.13°$ ($\sin\theta_c = 0.7329$) |
| intercept time $t_i$ | $7.3797\ \mathrm{s}$ |
| $T_\text{direct}(100)$ / $T_\text{head}(100)$ | $16.9492$ / $19.8021\ \mathrm{s}$ |
| $T_\text{direct}(250)$ / $T_\text{head}(250)$ | $42.3729$ / $38.4356\ \mathrm{s}$ |
| crossover $X_c$ | $163.02\ \mathrm{km}$ at $27.6310\ \mathrm{s}$ |
| apparent velocity, 300–500 km | $8.0500\ \mathrm{km\,s^{-1}}$ |
| fitted intercept / slope | $7.4138\ \mathrm{s}$ / $0.124112\ \mathrm{s\,km^{-1}}$ |
| recovered $V_2$ | $8.0573 \pm 0.0114\ \mathrm{km\,s^{-1}}$ |
| recovered $H_1$ (at $V_1 = 5.90$) | $32.11\ \mathrm{km}$ |
| rms residual | $0.0648\ \mathrm{s}$ (input $0.05\ \mathrm{s}$) |
| $H_1$ for $V_1 = 5.60$ / $6.20$ | $28.87$ / $35.99\ \mathrm{km}$ |

All model values are **SYNTHETIC**.

## ★ Foundational

**★1.** For $V_1 = 6.00\ \mathrm{km\,s^{-1}}$, $V_2 = 8.10\ \mathrm{km\,s^{-1}}$
and $H_1 = 40.0\ \mathrm{km}$, compute the critical angle, the intercept time
$t_i$ and the crossover distance $X_c$.

**★2.** Compute $T_\text{direct}$ and $T_\text{head}$ at $X = 100\
\mathrm{km}$ and $X = 250\ \mathrm{km}$ for the demonstration's model, and state
which branch is the first arrival at each offset. Verify that the crossover
$163.02\ \mathrm{km}$ satisfies both branches equally.

**★3.** The fitted slope is $b = 0.124112\ \mathrm{s\,km^{-1}}$ with standard
error $\sigma_b = 1.756\times10^{-4}\ \mathrm{s\,km^{-1}}$. Confirm this
$\sigma_b$ from the quoted velocity uncertainty, and state the unit of
$\sigma_b$.

## ★★ Applied

**★★4.** Using $H_1 = a V_1 V_2/(2\sqrt{V_2^{2}-V_1^{2}})$ with
$a = 7.4138\ \mathrm{s}$ and $V_2 = 8.0573\ \mathrm{km\,s^{-1}}$, compute $H_1$
for $V_1 = 5.60$, $5.90$ and $6.20\ \mathrm{km\,s^{-1}}$, and form the ratio of
the extreme change to the statistical uncertainty $\pm 0.0114\ \mathrm{km}$ in
$V_2$ (propagated to a depth uncertainty).

**★★5.** The picks run from 200 to 500 km at 20 km spacing. If the crossover is
at $163.02\ \mathrm{km}$, state how many picks the head-wave branch has in that
set, and evaluate the effect of extending the selection down to $180\
\mathrm{km}$ (one additional pick). Argue from the conditioning of a
straight-line fit — lever arm, slope variance and the risk of including a
mis-picked direct arrival near the crossover — not by re-running the fit.

**★★6.** Show that subtracting the reduced travel time $X/V_2$ from the
head-wave branch leaves a constant, and identify that constant with $t_i$.
Compute $T_\text{head}(500) - 500/8.05$ and compare with $t_i$.

## ★★★ Research-oriented

**★★★7.** You must resolve a 5 km thick layer at 30 km depth beneath a
high-velocity lid, knowing the lid velocity only to $\pm5\%$. Specify the array
geometry (offsets, spacing), the branch-selection rule, the estimator, and the
quantity that decides whether the layer is resolved at all. State the predicted
crossover, the offset at which the target branch first becomes the first arrival,
and how the $\pm5\%$ lid velocity propagates into the recovered thickness. A
specification that omits the last item is a failed answer.
