# Solutions — 06-11-02 Aftershock Sequences: Omori, ETAS and Triggering

> Read after attempting the exercises. Numbers were computed with the formulas of
> the lesson, not estimated. All values are **SYNTHETIC**.

Lesson: [02 Aftershocks](../02-aftershocks.md).

---

## ★1 — branching ratio

$$\bar n = \frac{Kb}{b-\alpha} = \frac{0.050\times1.00}{1.00-0.85}
= \frac{0.050}{0.15} = 0.333.$$

$\bar n < 1$, so the process is subcritical and cascades die out; the expected
number of events per ancestor is $1/(1-\bar n) = 1.5$.

If $\bar n \ge 1$ the mean offspring count diverges and the model has no stationary
background solution: the expectation of the sum over the magnitude distribution
does not converge, so the "background rate $\mu$" no longer describes the long-run
rate of the catalogue.

---

## ★2 — expected direct offspring

$$n(M) = K\,10^{\alpha(M-M_c)} = 0.020\times10^{0.90\times4.5}
= 0.020\times10^{4.05}.$$

$10^{4.05} = 1.122\times10^{4}$, so

$$n = 0.020\times11\,220 = 224 \text{ offspring}.$$

---

## ★3 — fraction inside a window

$$F(t) = 1 - \left(\frac{t+c}{c}\right)^{1-p}.$$

At $t = 2$ d: $\dfrac{t+c}{c} = \dfrac{2.1}{0.1} = 21$;
$21^{-0.2} = e^{-0.2\ln 21} = e^{-0.2\times3.0445} = e^{-0.6089} = 0.5438$;
$F = 1 - 0.5438 = 0.456$.

At $t = 60$ d: $\dfrac{60.1}{0.1} = 601$;
$601^{-0.2} = e^{-0.2\times6.3987} = e^{-1.2797} = 0.2781$;
$F = 1 - 0.2781 = 0.722$.

So 46% of offspring arrive within 2 days and 72% within 60 days: the sequence's
bulk is early, but a quarter of it is still to come after two months.

---

## ★4 — the two normalisations

$$\Lambda = \int_{0}^{200}(t+c)^{-p}\,\mathrm{d}t
= \frac{(200.05)^{-0.1} - (0.05)^{-0.1}}{-0.1}.$$

$(0.05)^{-0.1} = e^{0.1\times2.9957} = 1.3495$;
$(200.05)^{-0.1} = e^{-0.1\times5.2986} = 0.5889$. Therefore

$$\Lambda = \frac{0.5889 - 1.3495}{-0.1} = 7.606.$$

$$\Lambda_w = \int_{1}^{200}(t+c)^{-p}\,\mathrm{d}t
= \frac{0.5889 - (1.05)^{-0.1}}{-0.1},\qquad
(1.05)^{-0.1} = e^{-0.1\times0.04879} = 0.99513,$$
$$\Lambda_w = \frac{0.5889 - 0.99513}{-0.1} = 4.062.$$

A naive fit (which deletes the first day of events but keeps the integral running
from $t=0$) divides $N$ by a normalisation that is too large by the factor

$$\frac{\Lambda}{\Lambda_w} = \frac{7.606}{4.062} = 1.87.$$

The apparent productivity $K_{seq}$ is therefore understated by 46%. Note that the
misfit is not confined to $K_{seq}$: the likelihood's shape in $(p,c)$ also
changes, which is why the demonstration's naive $\hat p$ moves from 1.085 to 1.360
on the same data.

---

## ★5 — expected aftershocks of a $M6.5$ mainshock

Total direct offspring over all time:

$$n(6.5) = 0.020\times10^{0.90\times5.5} = 0.020\times10^{4.95}
= 0.020\times89\,125 = 1783.$$

Fraction inside 30 days:

$$F(30) = 1 - \left(\frac{30.05}{0.05}\right)^{-0.1}
= 1 - 601^{-0.1} = 1 - e^{-0.63987} = 1 - 0.5273 = 0.473.$$

So the expected number of aftershocks of *any* magnitude in 30 days is
$1783\times0.473 = 843$.

For $M\ge4$, multiply by $10^{-b(4-M_c)} = 10^{-3}$:

$$843\times10^{-3} = 0.84 \text{ events}.$$

This is the point of the magnitude distribution: **843 aftershocks, and fewer than
one of them is above $M4$.** A forecast of "many aftershocks" is almost always a
forecast of small ones.

---

## ★6 — can an offspring exceed the mainshock?

For one offspring, $P(m_\text{off} > M_\text{main}) = 10^{-b(M_\text{main}-M_c)}$.
With $M = 6.0$, $b = 1.0$, $M_c = 1.0$: $10^{-5}$.

The number of direct offspring is $n(6.0) = 0.020\times10^{4.5} = 632.5$, so the
expected number of exceedances is $632.5\times10^{-5} = 6.3\times10^{-3}$, and

$$P(\text{at least one}) \approx 1 - e^{-6.3\times10^{-3}} = 0.63\%.$$

This does not contradict the measured $\Delta M \approx 2.1$: the model says such
events are rare but possible (and the demonstration does observe $\Delta M < 0$ in
about 1 case in 40–120), which is precisely why $\Delta M$ must be reported as a
distribution with a minimum, not as a bound.

---

## ★7 — experiment specification (window truncation bias)

**Metric:** $\hat p(t_1)$ and $\hat c(t_1)$ as functions of the discarded fraction,
together with the coverage of the true values by a bootstrap interval, plus the
Kullback-type misfit (or the mean log-likelihood per event) of the fitted law.

**Design:** simulate $B = 200$ independent sequences with the same parameters
($p_0 = 1.1$, $c_0 = 0.05$ d, $K_0 = 0.02$, $\alpha_0 = 0.9$, $b = 1$), each long
enough that a 100-day window still contains hundreds of offspring. For a grid of
$t_1 \in \{0, 0.1, 0.5, 1, 5, 10, 20\}$ days, fit $(\hat p, \hat c)$ in the window
$(t_1, 100]$ **twice**: once normalising the integral on $(t_1,100]$ and once on
$(0,100]$. Report the mean and the s.d. of each estimator over the 200 replicates,
and bootstrap each sequence to get an interval width for comparison.

**Prediction with derivation:** with the correct normalisation the estimator is
consistent, so the mean of $\hat p$ stays near 1.1 with a width that grows as the
window loses events; with the naive normalisation the likelihood is misspecified
because the observed rate is over the window but the expected count is computed
over a longer one, so the fit compensates by raising $\hat p$ (steeper decay) —
the demonstration measures $\hat p = 1.36$ at $t_1 = 1$ d and $1.535$ at
$t_1 = 1$, $t_2 = 20$ d, both above the true 1.1. Also predict that $\hat c$ rises
towards the top of its search range, which is what the demonstration's windowed
fits show.

**Control:** the $t_1 = 0$ case, where the two normalisations coincide and both
must recover the true parameters within their scatter. If they do not, the fit
routine or the sequence generator is wrong, and no conclusion about the windows is
supportable.

---

## ★8 — derivation of the branching ratio and the truncation question

$$\bar n = \int_{M_c}^{\infty} K 10^{\alpha(m-M_c)}\,b\ln 10\,10^{-b(m-M_c)}\,dm
= K b\ln 10 \int_{M_c}^{\infty} 10^{-(b-\alpha)(m-M_c)}\,dm.$$

Substituting $x = m - M_c$ and integrating,

$$\int_0^\infty 10^{-(b-\alpha)x}\,dx = \frac{1}{(b-\alpha)\ln 10}
\qquad \text{provided } b - \alpha > 0,$$

so $\bar n = Kb\ln 10 \times 1/[(b-\alpha)\ln 10] = Kb/(b-\alpha)$.

If $\alpha \ge b$ the integral diverges: the contribution from arbitrarily large
parents grows as fast as (or faster than) their scarcity falls, so the expected
offspring per event is infinite and the process is not stationary. Physically, it
means that in such a model the largest events in an infinite catalogue dominate the
total productivity.

**Truncation.** Imposing a maximum magnitude $M_\text{max}$ (a physical or
modelling upper bound) replaces the integral's upper limit with
$M_\text{max} - M_c$:

$$\bar n_\text{trunc} = Kb\ln 10\,
\frac{1 - 10^{-(b-\alpha)(M_\text{max}-M_c)}}{(b-\alpha)\ln 10}
= \frac{Kb}{b-\alpha}\Big[1 - 10^{-(b-\alpha)(M_\text{max}-M_c)}\Big].$$

For $b > \alpha$ the truncation only *reduces* $\bar n$ relative to the untruncated
value, and the number of large aftershocks is reduced more than the number of small
ones — because the truncation bites exactly where the untruncated integral was
converging most slowly. For $\alpha > b$ the truncated result is finite while the
untruncated one is not, so truncation is what makes an $\alpha \ge b$ model usable
at all; but the model's rate then depends strongly on $M_\text{max}$, which is the
least well constrained input in the whole formulation. That trade-off — a finite
branching ratio bought with an unmeasurable parameter — is the reason $\alpha < b$
is preferred in practice.
