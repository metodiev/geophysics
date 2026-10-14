# Exercises — 06-11-02 Aftershock Sequences: Omori, ETAS and Triggering

Attempt these before reading the
[solutions](./02-aftershocks-solutions.md). The lesson is
[02 Aftershocks](../02-aftershocks.md). All models and data in this module are
**SYNTHETIC**.

## ★ Foundational

**★1.** An ETAS model has $K = 0.050$, $\alpha = 0.85$ and $b = 1.00$ (with
$\alpha < b$ required). Compute the branching ratio $\bar n = Kb/(b-\alpha)$ and
state whether the process is subcritical. If it were not, what would break in the
model?

**★2.** With $K = 0.020$, $\alpha = 0.90$ and $M_c = 1.0$, compute the expected
total number of direct offspring of a $M5.5$ mainshock.

**★3.** For $p = 1.2$ and $c = 0.1$ d, compute the fraction of offspring expected
inside the first 2 days and inside the first 60 days.

## ★★ Applied

**★★4.** The demonstration fits Omori-Utsu with the window normalisation both
correctly and naively at $\hat p = 1.085$, $\hat c = 0.0578$ d. Compute
$\Lambda = \int_{0}^{200}(t+c)^{-p}\,\mathrm{d}t$ and
$\Lambda_w = \int_{1}^{200}(t+c)^{-p}\,\mathrm{d}t$ for $p = 1.1$, $c = 0.05$, and
state the factor by which a naive fit understates the sequence's productivity
$K_{seq} = N/\Lambda$.

**★★5.** Using $K = 0.020$, $\alpha = 0.90$, $p = 1.10$, $c = 0.05$ d and
$M_c = 1.0$, compute the expected number of aftershocks of a $M6.5$ mainshock
within 30 days, and separately the expected number of those with $M \ge 4$.

**★★6.** With the same parameters, compute the probability that a $M6.0$ mainshock
is exceeded by at least one of its own offspring. State whether the result
contradicts the demonstration's measured mean
$\Delta M = M_\text{main} - M_\text{largest aftershock}$ of about 2.1.

## ★★★ Research-oriented

**★★★7.** Design an experiment to measure the bias in $(\hat p, \hat c)$ as a
function of the fraction of the sequence that is discarded. State the metric, the
bootstrap-permitting design, the prediction with its derivation, and the control
that separates bias from scatter.

**★★★8.** Derive $\bar n = Kb/(b-\alpha)$ and state exactly what fails when
$\alpha \ge b$. Then propose a physically motivated truncation of the magnitude
distribution that restores a finite branching ratio, and predict how it changes the
number of large aftershocks relative to the untruncated model.
