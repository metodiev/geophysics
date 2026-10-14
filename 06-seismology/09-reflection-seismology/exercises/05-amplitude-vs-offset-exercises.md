# Exercises — 06-09-05 AVO/AVA Analysis and Its Assumptions

Attempt these before reading the
[solutions](./05-amplitude-vs-offset-solutions.md). The lesson is
[05 Amplitude vs Offset](../05-amplitude-vs-offset.md). All models are
**SYNTHETIC** teaching values.

## ★ Foundational

**★1.** Compute the Aki–Richards intercept $A$ and gradient $B$ for
$\Delta v_p/\bar v_p = 0.10$, $\Delta v_s/\bar v_s = 0.15$,
$\Delta\rho/\bar\rho = 0.05$ and $\bar v_s/\bar v_p = 0.55$, and state what each
one physically measures.

**★2.** The demonstration reports an exact normal-incidence coefficient
$R = +0.093894$ and an Aki–Richards intercept $A = +0.094079$ for the same
interface. Compute the difference and explain, in one sentence, why $A$ is not
"the" reflection coefficient.

## ★★ Applied

**★★3.** Using the demonstration's interface ($v_{p1} = 3000$,
$v_{s1} = 1600$, $\rho_1 = 2300$; $v_{p2} = 3400$, $v_{s2} = 1900$,
$\rho_2 = 2450$ in SI), compute $\bar v_s/\bar v_p$, $A$ and $B$ from the
definitions, and compare with the printed $A = +0.09408$, $B = -0.18036$.

**★★4.** Show that $A = \tfrac12\left(\Delta v_p/\bar v_p +
\Delta\rho/\bar\rho\right)$ reduces to the exactly normal-incidence coefficient
to first order in the contrasts, and state the neglected terms.

**★★5.** Using the demonstration's fluid-substitution table, describe how
$R(0)$ changes from brine to oil to gas and explain why $v_s$ *increases* while
$v_p$ decreases when the pore fluid becomes lighter.

## ★★★ Research-oriented

**★★★7.** Verify numerically, from the printed (rounded) values, that the
demonstration's models A ($v_p = 3400$, $v_s = 1900$, $\rho = 2450$) and B
($v_p = 3026$, $v_s = 1705$, $\rho = 2754$) fit the same two-term AVO curve:
compute $A$ and $B$ for both and report the maximum two-term $|R_A - R_B|$ over
$0$-$40^\circ$. Explain why the demonstration reports an exact zero and this
calculation does not.

**★★★8.** Construct a *third* member of the equivalence family for the same
$(A,B)$, state the constraint you imposed, and name the two independent
measurements that would break the degeneracy — with the reason each must be
independent of the others.

**★★★9.** The demonstration shows that the three-term AVO model separates the
two models over $0$-$40^\circ$ at $3.39\sigma$ while the two-term model cannot.
Design the acquisition that would make this separation routine, and state the
cost in maximum offset for a target at $t_0 = 2.0\ \mathrm{s}$,
$v_{\text{rms}} = 2800\ \mathrm{m\,s^{-1}}$.
