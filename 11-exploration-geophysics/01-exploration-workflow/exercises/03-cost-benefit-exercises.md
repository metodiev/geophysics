# Exercises — 11-01-03 Cost, Risk and Value of Information in Exploration

Attempt these before reading the
[solutions](./03-cost-benefit-solutions.md). The lesson is
[03 Cost, Risk and Value of Information](../03-cost-benefit.md). All payoffs,
probabilities, test qualities and prices are **SYNTHETIC** teaching values.

Throughout, keep the payoff convention: $W$ is the value of a discovery **net of
all costs**, $K$ is the loss on a program that fails, and the value function is
$V(p) = \max\bigl(0,\;pW-(1-p)K\bigr)$.

## ★ Foundational

**★1.** With $W = 400$ MUSD and $K = 80$ MUSD, compute the indifference
probability $p^{*}$ and the EMV of drilling at $p = 0.10$, $0.20$ and $0.40$.
State the decision at each prior.

**★2.** For the same payoffs, compute the EVPI at $p = 0.10$, $0.1667$ (the
indifference point), and $0.60$, using $\mathrm{EVPI} = \min(pW,(1-p)K)$, and
state where it is largest and why.

**★3.** A test has $\mathrm{TPR} = 0.75$ and $\mathrm{FPR} = 0.25$ and the prior is
$p = 0.20$. Compute $\mathbb{P}(+)$, $p_{+}$ and $p_{-}$, and state the decisions
at the posterior probabilities for $W = 400$, $K = 80$.

**★4.** State in one sentence why a test with $\mathrm{TPR} = \mathrm{FPR}$ has
EVSI = 0, and verify it algebraically by substituting into the posterior formula.

## ★★ Applied

**★★5.** For the prospect of ★3, compute EVSI, the maximum price worth paying, and
the net expected gain if the test costs $4$ MUSD. Then compute EVPI and the
fraction of EVPI the test captures.

**★★6.** The same prospect, but the prior moves to $p = 0.1667$ (the indifference
probability of ★1) and then to $p = 0.02$. Compute EVSI at both priors with the
same test and the same $W$, $K$. Explain, with the numbers, why EVSI is larger at
one of the two and what that implies for the ordering of survey programs.

**★★7.** A test has $\mathrm{FPR} = 0.15$ and you may choose
$\mathrm{TPR} = 0.70$, $0.85$ or $0.95$, at prices of $2$, $4$ and $14$ MUSD
respectively. Using the prior and payoffs of ★3, compute the net expected gain of
each option and state which you would buy. State which quantity changed the
ranking relative to buying on EVSI alone.

**★★8.** Derive and evaluate the Jensen gap for $p \sim \mathrm{Beta}(2,8)$
(mean $0.20$) with $W = 400$ and $K = 80$: compute $V(\mathbb{E}[p])$,
$\mathbb{E}[V(p)]$ by quadrature, and state the sign and size of the error made by
using the mean.

## ★★★ Research-oriented

**★★★9.** An exploration manager argues that because
$\mathrm{EVPI}$ is only $\min(pW,(1-p)K)$, and because $K \ll W$ always, EVPI ≈
$(1-p)K \le K$ is *small* compared with $W$, so "information is never worth much
in exploration". Rebut or support this argument quantitatively, including the case
where many prospects share the same decision, and state the assumption that makes
the argument true.

**★★★10.** Extend the two-action payoff table with a third action, **delay**,
which pays $0$ now and keeps the option alive at a cost $D$. Derive the new value
function, show how $p^{*}$ changes, and construct a numerical example in which the
value of a survey is *higher* in the three-action problem than in the two-action
one even though the survey is the same. Explain the mechanism.

**★★★11.** A value-of-information study is itself a model. Write a specification
for auditing one: state the four inputs whose uncertainty you would propagate
($p$, $W$, $K$ and the test's operating characteristics), the quantity you would
report (not a single dollar figure), and how you would detect the case where the
VOI conclusion is driven by the payoff table rather than by the geophysics.
Include the check that distinguishes a genuinely negative EVSI from a
mis-specified action set.
