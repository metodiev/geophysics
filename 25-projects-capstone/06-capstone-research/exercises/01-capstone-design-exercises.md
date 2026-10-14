# Exercises — 25-06-01 Capstone: Designing an Original Research Study

Attempt these before reading the
[solutions](./01-capstone-design-solutions.md). The lesson is
[01 Designing an Original Research Study](../01-capstone-design.md); all numbers are
**SYNTHETIC** planning figures printed by
[`code/capstone_design_demo.py`](../code/capstone_design_demo.py):

| Quantity | Value |
|---|---|
| power conventions | $z_{0.025} = 1.96$, $z_{0.20} = 0.84$, so $\Delta_\text{MDE} = 2.80\sigma/\sqrt N$ |
| time budget | 24 weeks |
| candidates (effect, $\sigma$, $N$) | H-K 1.500/4.00/20; InSAR 0.800/0.50/120; joint 0.015/0.04/30; ambient 0.400/0.30/200; $b$-value 0.150/0.12/60; MT 0.150/0.35/25 |
| SNR / MDE | 1.68/2.504; 17.53/0.128; 2.05/0.020; 18.86/0.059; 9.68/0.043; 2.14/0.196 |
| scores (0.40/0.25/0.20/0.15) | 0.890, 0.870, 0.833, 0.555, 0.484, 0.374 (ambient, $b$-value, InSAR, H-K, joint, MT) |
| rank stability (500 draws) | ambient wins 60.8%, $b$-value 39.2%, all others 0.0%; top-2: 99.6%, 67.0%, 33.0%, 0.4%, 0%, 0% |
| repairs needed | H-K $N > 56$, joint $N > 56$, MT $N > 43$; MT is 4 weeks over budget |

## ★ Foundational

**★1.** State the minimum detectable effect for a two-sided 5% test at 80% power, and
verify the H-K row of the table (effect 1.500 km, $\sigma = 4.00$ km, $N = 20$).

**★2.** Convert each candidate's SNR into a statistical power using
$\text{power} = \Phi(\text{SNR} - 1.96)$. State which candidates would have a better
than even chance of detecting their effect if it were real.

**★3.** State why the constant is $2.80$ and compute it for 90% power. By what factor
does the required sample size change?

## ★★ Applied

**★★4.** Compute the sample size each underpowered candidate needs, express it as a
multiple of the planned $N$, and state which of the three is cheapest to repair *among
those inside the time budget*. Justify the ranking of repairs.

**★★5.** The InSAR candidate has $N = 120$ and $\sigma = 0.50$ cm/yr. Compute the
effect it could detect at 80% power. Then compute the effect it could detect with
$\sigma = 0.25$ cm/yr (better processing) and with $N = 480$ (four times the data), and
state which buys more and by how much.

**★★6.** The top-ranked candidate wins $60.8\%$ of perturbed weightings while the
second wins $39.2\%$. Compute the score gap at the stated weights, and explain why a
gap of $0.020$ on a scale of $0$–$1$ is nonetheless the difference between two
essentially tied studies. Then state what the $0.0\%$ win rates of the bottom three
candidates *do* establish.

**★★7.** A candidate has $\Delta/\sigma = 0.4$. Compute the $N$ needed for 80% power,
and compare it with the $N$ needed if the same study used a measurement with twice the
scatter. State the general rule relating sample size and noise.

## ★★★ Research-oriented

**★★★8.** Design one capstone study of your own. Your answer must contain: the
question in one sentence with an effect size and expected sign; the data source and
the count of *independent* measurements with an effective-$N$ argument; the source of
the scatter estimate (measured, published or assumed, and which); the SNR and minimum
detectable effect at the planned $N$; the decision rule and the threshold; a falsifier;
the deliverable with its stated resolution or uncertainty; the screening weights you
used and the stability of your choice under perturbed weights; and the two risks with
a fallback for each. A design that omits the effective-$N$ argument or the falsifier is
a failed answer.
