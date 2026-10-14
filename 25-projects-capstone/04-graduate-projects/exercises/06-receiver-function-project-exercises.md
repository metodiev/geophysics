# Exercises — 25-04-06 Project: Crustal Structure from Receiver Functions

Attempt these before reading the
[solutions](./06-receiver-function-project-solutions.md). The project is
[06 Receiver Functions](../06-receiver-function-project.md). Values printed by
[`code/receiver_function_demo.py`](../code/receiver_function_demo.py):

| Quantity | Value |
|---|---|
| true model | $H = 35.0$ km, $V_p = 6.30$ km/s, $V_p/V_s = 1.75$, $V_s = 3.600$ km/s |
| ray parameter | $p = 0.060$ s/km |
| phase times | Ps 4.3493 s, PpPs 14.6361 s, PpSs+PsPs 18.9854 s |
| grid | $161 \times 81$, $H$ 20–60 km, $k$ 1.60–2.00 |
| joint peak | 0.729 at $H = 35.00$ km, $k = 1.750$ |
| half-maximum region | $H$ 24.75–46.75 km, $k$ 1.60–2.00 |
| Ps only | 28.50 km, 1.925 |
| PpPs only | 36.75 km, 1.630 |
| PpSs+PsPs only | 23.50 km, 2.000 |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Write the three delay-time expressions and state the physical content of
each. Verify the demonstration's Ps time for the stated model.

**★2.** Compute the three delay times for $H = 30\ \mathrm{km}$,
$V_p = 6.00\ \mathrm{km\,s^{-1}}$, $V_p/V_s = 1.80$ and
$p = 0.060\ \mathrm{s\,km^{-1}}$.

**★3.** State why the three expressions are linearly independent in $(H, k)$, and
what a stack of two of them would leave undetermined.

## ★★ Applied

**★★4.** The half-maximum region spans $H = 24.75$–$46.75$ km. Compute its width,
compare it with the grid step (0.25 km), and state which of the two is the honest
resolution.

**★★5.** The joint stack recovers $H$ and $k$ exactly while each single-phase stack
does not. Explain in two sentences why an exact recovery on synthetic data is not
evidence that the method is accurate on real data, and state what the demonstration
*does* establish.

**★★6.** $H$ scales almost linearly with the assumed $V_p$. Compute the recovered
$H$ if the true $V_p$ were $5\%$ lower than assumed, holding the observed phase
times fixed, and state which of $H$ and $k$ absorbs the error.

## ★★★ Research-oriented

**★★★7.** Design a study that determines crustal thickness and $V_p/V_s$ without
assuming $V_p$: state the additional observations, what each measures, why the
combination removes the ambiguity, the resolution you would report for each
parameter, and the test that would demonstrate the ambiguity is gone rather than
merely hidden. A design that still contains an assumed $V_p$ is a failed answer.
