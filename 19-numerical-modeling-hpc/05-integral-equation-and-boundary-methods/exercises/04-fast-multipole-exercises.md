# Exercises — 19-05-04 Fast Multipole and Hierarchical Acceleration

Attempt these before reading the
[solutions](./04-fast-multipole-solutions.md). The lesson is
[04 Fast Multipole and Hierarchical Acceleration](../04-fast-multipole.md). All
models are **SYNTHETIC** teaching values.

## ★ Foundational

**★1.** A node holds $400$ sources with total strength
$M_0 = 4.04726574\times10^{2}$. Compute the monopole potential at a target
$2.001436$ km from the node centre and state its unit for a kernel $1/r$ with
$r$ in km.

**★2.** State the admissibility criterion and explain what quantity $s/d$ bounds.

**★3.** A node spans $0.988$ km and its centre is $1.998564$ km from a target on
the other side. State whether the target is to the left or the right of the node
and whether the far-field series alternates.

## ★★ Applied

**★★4.** From the single-node error table ($p = 3$: $5.571\times10^{-4}$;
$p = 8$: $1.743\times10^{-6}$) estimate the ratio per added term and predict the
error at $p = 12$.

**★★5.** In the count table at $n = 3200$ the direct sum needs
$1.024\times10^{7}$ pairs while the tree uses $33\,636$ far-field nodes and
$55\,066$ direct particles. Compute the interaction ratio and explain why the
measured time ratio is $0.16$ rather than about $100$.

**★★6.** The opening-angle sweep gives direct-particle counts $4699$, $6820$,
$9063$, $13494$, $22054$ for $\theta = 1.0, 1.5, 2.0, 3.0, 5.0$. Compute the
growth per unit of $\log\theta$ and state what it implies for the optimum.

## ★★★ Research-oriented

**★★★7.** A tree code with $\theta = 2$, $p = 6$ gives an error of
$8.973\times10^{-4}$; with $\theta = 5$, $p = 6$ it gives $1.975\times10^{-6}$.
Explain why raising $\theta$ improves accuracy, and state what it costs at
$n = 400$.

**★★★8.** Design a test that decides whether an $O(1)$ error in a tree code comes
from the sign convention or from a wrong admissibility test, and state the
observable that separates the two.
