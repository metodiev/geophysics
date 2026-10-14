# Exercises — 06-03-02 The Double-Couple Source and Radiation Patterns

Attempt these before reading the
[solutions](./02-double-couple-solutions.md). The lesson is
[02 The Double-Couple Source and Radiation Patterns](../02-double-couple.md) and
the demonstration is
[`../code/double_couple_demo.py`](../code/double_couple_demo.py). All mechanisms
and amplitudes are **SYNTHETIC**. Frame: $x$ North, $y$ East, $z$ Down;
$\hat n$ = fault normal, $\hat s$ = hanging-wall slip vector;
rakes $+90^\circ$ = thrust, $-90^\circ$ = normal, $0$ = left-lateral.

Useful construction:

$$\hat n = \left(-\sin\delta\sin\phi,\ \sin\delta\cos\phi,\ -\cos\delta\right),$$
$$\hat s = \left(\cos\lambda\cos\phi + \cos\delta\sin\lambda\sin\phi,\
\cos\lambda\sin\phi - \cos\delta\sin\lambda\cos\phi,\ -\sin\lambda\sin\delta\right).$$

## ★ Foundational

**★1.** For a vertical strike-slip fault with $\phi = 90^\circ$,
$\delta = 90^\circ$, $\lambda = 0^\circ$, compute $\hat n$ and $\hat s$ and write
out the full $3\times3$ matrix $M/M_0$.

**★2.** For your ★1 tensor, compute the trace and verify symmetry
($M = M^{\mathsf T}$). State in one sentence what each of the two results means
physically.

**★3.** For the same mechanism, evaluate the P amplitude factor
$A(\hat r) = (\hat r\cdot\hat n)(\hat r\cdot\hat s)$ for the three ray directions
$\hat r = (1,0,0)$, $\hat r = (0,1,0)$ and $\hat r = (1,1,0)/\sqrt2$. Which are
nodal?

## ★★ Applied

**★★4.** Derive, for arbitrary orthogonal unit vectors $\hat n$ and $\hat s$,
that $\hat r^{\mathsf T}M\hat r = 2M_0(\hat r\cdot\hat n)(\hat r\cdot\hat s)$.
State clearly which property of $\hat n$ and $\hat s$ you used.

**★★5.** For a **thrust** ($\lambda = +90^\circ$, $\phi = 0^\circ$) compute the
vertical-ray amplitude as a function of dip $\delta$, and evaluate it at
$\delta = 30^\circ$. Then repeat for a **normal** fault at $\delta = 45^\circ$.
State the polarity in each case.

**★★6.** Using the plunge relation $90^\circ - |\delta - 45^\circ|$, compute the
plunge of the compressional axis for thrust dips $10^\circ$, $35^\circ$,
$55^\circ$ and $80^\circ$, and comment on the pattern.

**★★7.** The demo reports a worst absolute difference of
$2.048\times10^{3}\ \mathrm{N\,m}$ between the $(\hat n,\hat s)$ construction and
the closed-form components, on components of size $1.0\times10^{19}\ \mathrm{N\,m}$.
Compute the relative difference and explain why a value near $10^{-16}$ is the
expected outcome of a double-precision comparison.

## ★★★ Research-oriented

**★★★8.** Show algebraically that $M$ is invariant under
$(\hat n,\hat s)\to(-\hat n,-\hat s)$ but changes sign under
$\hat s\to-\hat s$ alone, and connect the second fact to the $P$/$T$ labelling
trap. Then state the physical operation on a fault that each algebraic change
corresponds to.

**★★★9.** Design a procedure to decide which of the two nodal planes of a
SYNTHETIC mechanism is the fault plane, using only the *spatial distribution* of
aftershocks you generate yourself. Specify the model you would use to place the
hypocentres, the statistic that discriminates the two candidates, and the false
decision rate you would accept. A specification that could not be executed is a
failed answer.

**★★★10.** A regional network has $N$ three-component stations with reliable
first-motion polarities. A double couple radiates compression over half the focal
sphere, so the probability that a *given* station reads compression is $1/2$. Using
the binomial argument that underlies the demo's $2^{-N}$ table, compute the number
of stations needed for the probability of an all-compressional false positive to
fall below $10^{-3}$, and state two reasons why the real network is *not* as
decisive as that number suggests.
