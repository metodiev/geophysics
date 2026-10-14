# Exercises — 06-11-07 Declustering, Completeness and Catalogue Physics

Attempt these before reading the
[solutions](./07-catalog-declustering-solutions.md). The lesson is
[07 Declustering](../07-catalog-declustering.md). All models and data in this
module are **SYNTHETIC**.

## ★ Foundational

**★1.** Explain in two sentences why a time-independent PSHA calculation needs a
declustered rate, and what question a declustered catalogue answers.

**★2.** For $\eta_0 = -4.0$ the demonstration removes 824 events with precision
0.982 and recall 0.605 from a catalogue with 1338 triggered events. Compute the
true positives, false positives and false negatives.

**★3.** A neighbour rule declares an aftershock when
$\log_{10}\eta < -3.5$. State the equivalent window offset $o$ in the rule
$w(M) = 10^{M-o}$ days, and evaluate $\log_{10}\eta$ for a $M4.5$ parent at a delay
of 0.5 days with $b = 1.0$, $M_c = 1.0$.

## ★★ Applied

**★★4.** The raw catalogue has 1864 events with $b = 0.9799$ and CV $= 1.894$. The
true background has 520 events with $b = 0.9940$ and CV $= 1.007$. Compute the
fraction of the catalogue that is background, and the fraction of the *b-value
difference* from the truth that the best declustering rule ($\eta_0 = -4$) removes.

**★★5.** The demonstration reports $b = 0.9803$ for the window offset $o = 4.0$ but
$b = 0.9537$ for $o = 5.0$, while $\eta_0 = -4$ also gives 0.9537. Explain both
observations — the change with the window, and the exact agreement of the two
rules — using the metric and the precision/recall numbers.

**★★6.** Estimate the standard error of the b-value for the residual catalogue of
$\eta_0 = -4$ ($N = 1040$) and for the true background ($N = 520$), and state
whether the difference between the two b-values (0.9537 and 0.9940) is resolved by
either sample.

## ★★★ Research-oriented

**★★★7.** Design a declustering study in which the rule is fitted to the data
rather than chosen a priori. State the objective function, the parameterisation,
the risk of overfitting, and the validation scheme that would detect it.

**★★★8.** A time-independent hazard calculation uses a declustered rate; a
time-dependent model of the same region uses the full catalogue and an ETAS
intensity. Design a comparison that determines, for a stated decision, which of the
two frameworks is preferable, and state the criterion you would pre-register.
Include what each framework makes impossible to answer.
