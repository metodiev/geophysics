# Solutions — 19-07-02 Solution Verification and Discretisation Error Estimation

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Lesson: [02 Solution Verification](../02-solution-verification.md).

---

## ★1 — Order, estimate and GCI

Differences: $J_2 - J_1 = -2.55\times10^{-2}$,
$J_3 - J_2 = -6.4\times10^{-3}$; ratio $3.9844$;

$$p = \frac{\ln 3.9844}{\ln 2} = \frac{1.38237}{0.69315} = 1.9945 .$$

`r^p = 2^{1.9945} = 3.9848`, so `r^p - 1 = 2.9848` and

$$\hat{\delta}_3 = \frac{|J_3 - J_2|}{r^{p} - 1}
= \frac{6.4\times10^{-3}}{2.9848} = 2.144\times10^{-3},$$

$$\mathrm{GCI}_3 = 3\hat{\delta}_3 = 6.43\times10^{-3}.$$

**Reported:** $J = 1.2021 \pm 0.0064$ (GCI with $F_s = 3$, three grids
$h, h/2, h/4$, observed order $1.9945$), plus the solver tolerance.

---

## ★2 — Condition number versus discretisation error

$$\kappa = \frac{4N^{2}}{\pi^{2}} = \frac{4\times1024^{2}}{9.8696}
= 4.249\times10^{6}, \qquad
\epsilon\kappa = 2.2\times10^{-16}\times4.249\times10^{6}
= 9.3\times10^{-10}.$$

The measured discretisation error is $5.546\times10^{-7}$, about $600$ times
larger. **The discretisation error dominates**, so round-off is not yet a
limitation at $N = 1024$; from the lesson's table the floor appears between
$N = 65536$ and $N = 262144$, where the error rises from $7.7\times10^{-11}$ to
$6.2\times10^{-9}$.

---

## ★3 — Why the tolerance must be below the error

At $N = 1024$ the CG solve with relative tolerance $10^{-2}$ achieved
$\lVert u_{\text{CG}} - u_{\text{direct}}\rVert/\lVert u_{\text{direct}}\rVert =
8.771\times10^{-3}$ — larger than the discretisation error at that grid,
$5.5\times10^{-7}$, by four orders of magnitude. Refining the grid further would
not change the reported error at all: the study would measure the solver. The
tolerance must be at least an order of magnitude below the discretisation error you
intend to claim, so here below $10^{-8}$; the lesson's table shows the accuracy
reaching its own floor of $1.9\times10^{-13}$ for tolerances $\le10^{-4}$.

---

## ★4 — Resolution for a target accuracy

With $e = Ch^{2}$ and $e(64) = 10^{-3}$: to reach $10^{-6}$ the error must fall by
$10^{3}$, so $h$ must fall by $\sqrt{10^{3}} = 31.6$, giving
$N \approx 64\times31.6 = 2024$, i.e. $N = 2048$ on a power-of-two sequence.

For a 2-D problem the unknowns scale as $N^{2}$: from $64^{2} = 4096$ to
$2048^{2} = 4.19\times10^{6}$, a factor of $1024$ more unknowns (and, for an
explicit scheme, $2^{15}$ more work per time step, before the time step shrinks).

---

## ★5 — Choosing the asymptotic triple

The successive orders $2.6,\,2.15,\,2.03,\,1.99$ approach $2$ from above, which is
the signature of a solution whose higher-order term has the *opposite* sign and is
not yet negligible. The last two triples are in the asymptotic range
($p = 2.03 \pm 0.04$), and the finest triple should be used for the error estimate.
Using the first triple would report $p = 2.6$, hence
$r^{p} - 1 = 5.06$ instead of $3.0$ for $r = 2$: the estimated error would be
**under**-stated by a factor of $1.7$, and the extrapolated value would be biased.

---

## ★6 — The pair-mixing factor

With $r = 2$ and $p = 2$, $r^{p} - 1 = 3$. The error on the fine grid is estimated
from $J_{\text{fine}} - J_{\text{mid}}$, and the error on the mid grid from
$J_{\text{mid}} - J_{\text{coarse}}$. Since the error falls by $r^{p} = 4$ per
refinement, the coarse difference is $4$ times the fine difference, so mixing them
inflates the estimate by exactly $4$.

It is *conservative* in the sense that it does not under-state the error, but it is
still wrong: it describes the mid grid while claiming to describe the fine one, and
it makes the GCI look like a loose bound when the error model is in fact exact.
That is the failure mode the lesson's Example 2 warns about; the correct estimate
for $N = 128$ in the demonstration is $3.616\times10^{-4}$, not
$1.448\times10^{-3}$.

---

## ★7 — Separating a tolerance floor from a discretisation error

**Scan.** Two independent refinement axes: the grid, $N \in \{64, 128, 256, 512,
1024, 2048\}$, and the solver tolerance, $\tau \in \{10^{-3}, 10^{-5}, 10^{-7},
10^{-9}, 10^{-11}, 10^{-13}\}$. For each $(N, \tau)$ compute the functional $J$ and
record it in a two-dimensional table. Additionally record the *solver residual* and
the number of iterations, both of which cost nothing.

**Plot.** $\log|J(N,\tau) - J_{\text{ref}}|$ against $\log h$ for each fixed
$\tau$, where $J_{\text{ref}}$ is the most accurate value obtained on the whole
scan; or, if a reference is unavailable, plot
$|J(N,\tau) - J(N,\tau_{\min})|$, the difference from the tightest tolerance at the
same $N$.

**Patterns.** A pure discretisation error gives parallel straight lines of slope
$p$, all reaching the same floor at large $N$; a pure tolerance floor gives
horizontal lines whose level is set by $\tau$ and which are insensitive to $N$. The
diagnostic for a floor is that **the curves collapse when plotted against
$\tau$ instead of $h$**, i.e. the error depends on the tolerance and not the grid.

**Failure mode.** If the tolerance is *proportional* to a discretisation-scaled
quantity (a common choice is $\tau = c h^{2}$ so that the solver keeps pace with
refinement), the two effects are collinear in the scan and cannot be separated: an
apparent order of $2$ could be the grid, the tolerance, or a mixture. The fix is to
hold $\tau$ fixed while refining $h$, at least for the calibration runs.

---

## ★8 — Conservatism of the GCI, and when it fails

**Proof of exact conservatism.** With $J_i = J + Ch_i^{p}$ exactly (three grids,
$h_2 = h_1/r$, $h_3 = h_2/r$), and the error on the fine grid being
$e_3 = Ch_3^{p}$:

$$J_2 - J_3 = C\left(h_2^{p} - h_3^{p}\right) = Ch_3^{p}\left(r^{p} - 1\right)
\quad\Longrightarrow\quad
\frac{|J_2 - J_3|}{r^{p} - 1} = |Ch_3^{p}| = e_3,$$

so $\mathrm{GCI}_3 = F_s e_3$: the estimate is the true error multiplied by exactly
$F_s$, independent of $C$, $p$ and $r$. Numerically, the demonstration measures
GCI/true $= 3.0$ with $F_s = 3$ and total error $1.207\times10^{-4}$.

**Smallest departure that under-estimates.** Keep the geometry but let the error
model have a second term with the *same sign* and a *higher* order:
$J_h = J + Ch^{p} + Dh^{q}$ with $q > p$ and $CD > 0$ (the demonstration's own
orders $2.6, 2.15, 2.03$ come from a case near this regime). Then the observed $p$
is biased **high**, so $r^{p_{\text{obs}}} - 1 > r^{p} - 1$ and the estimate
$\lvert J_2 - J_3\rvert/(r^{p_{\text{obs}}} - 1)$ is too **small**; with
$p_{\text{obs}} = 2.6$ instead of $2$ it is smaller by a factor
$(2^{2.6} - 1)/(2^{2} - 1) = 5.06/3 = 1.7$. Adding noise to $J_3$ does the same
thing more cheaply: a perturbation of order the Richardson term in the wrong
direction shrinks the numerator directly. Both departures are detectable by the
sign test on $J_2 - J_3$ relative to $J_1 - J_2$ and by an order that drifts with
the choice of triple.
