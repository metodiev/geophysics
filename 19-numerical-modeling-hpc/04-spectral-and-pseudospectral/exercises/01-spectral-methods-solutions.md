# Solutions — 19-04-01 Spectral Methods: Basis Choice and Exponential Convergence

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [01 Spectral Methods: Basis Choice and Exponential Convergence](../01-spectral-methods.md).

---

## ★1 — The exact derivative of a mode

For $u = e^{\mathrm{i}2\pi mx}$ sampled on $N = 64$ points, the Fourier
derivative is $\widehat{u'}_k = \mathrm{i}k\widehat{u}_k$ with
$k = 2\pi j/N$, and the single non-zero coefficient sits at $j = m$. So the
derivative is exact whenever $m$ is representable, i.e. for
$|m| \le N/2 - 1 = 31$; at $m = 32 = N/2$ the mode is its own alias and only the
cosine part survives.

The measured 32-point table in the lesson is the evidence: the maximum error is
$5.7\times10^{-13}$ at $m = 12$, $1.2\times10^{-12}$ at $m = 15$, and jumps to
$2.011\times10^{2}$ at $m = 16$ — nine orders of magnitude in one step of $m$,
with nothing gradual in between.

---

## ★2 — Two error models

$$E_{\rm spectral} = C\rho^{-N} \quad (\rho > 1),
\qquad E_{\rm order\ p} = C N^{-p} \quad\text{(equivalently } Ch^{p}) .$$

The order-$p$ model is a power law: $\log E$ is linear in $\log N$, and each
doubling of $N$ reduces the error by a fixed factor $2^{p}$. The spectral model
is *geometric*: $\log E$ is linear in $N$, and the reduction factor per doubling
grows with $N$ without bound. The lesson's measured table shows the difference
directly — three doublings of $N$ carried nine decades of error, which no power
law of moderate $p$ can do.

---

## ★3 — The round-off floor

The floor is the product of the **operator norm** and the **machine epsilon**:
$\|D\|\,\epsilon_{\rm mach}$. The measured Fourier operator has
$\|D\|_2/N \to \pi$, so $\|D\|_2 \approx \pi N$ and the floor is about
$N\epsilon_{\rm mach}$ times the field's scale.

A convergence table that continues past the floor reports noise: in the lesson's
measured table the error rises from $6.3\times10^{-14}$ at $N=64$ to
$1.4\times10^{-13}$ at $N=128$. The honest report ends the table where the
improvement stops and says *why* it stops.

---

## ★4 — Finite differences to $10^{-10}$

Second order:

$$N = \sqrt{\frac{167.6}{10^{-10}}} = 1.2946\times10^{6}.$$

Fourth order:

$$N = \left(\frac{8.00\times10^{3}}{10^{-10}}\right)^{1/4}
= 2.9908\times10^{3}.$$

For comparison, the spectral method reached $10^{-6}$ with 19–24 modes, and the
extrapolation from that constant (in the lesson's §3) gave $5.28\times10^{6}$ and
$6.04\times10^{3}$ for $10^{-12}$. Both finite-difference orders require
$10^{4}$–$10^{7}$ more points than the spectral method at comparable accuracy —
which is the quantitative content of "exponential convergence".

Note also the *relative* gain: raising the order from 2 to 4 reduces $N$ by a
factor $433$; raising it from 1 to 2 would reduce it by $10^{3}$ relative to
second order but still leave $10^{6}$ points. Order matters, but only the
geometric law removes the power law.

---

## ★5 — The kink rate

If the coefficients decay like $k^{-2}$, the derivative series has coefficients
like $k\cdot k^{-2} = k^{-1}$, so the truncated tail satisfies

$$\|u' - u'_N\|_{L^2}^2 \sim \sum_{k>N}k^{-2} \sim \frac{1}{N}
\Longrightarrow \|u' - u'_N\|_{L^2} \sim N^{-1/2}.$$

The predicted rms order is therefore **0.5**, and the measured sequence
0.401, 0.452, 0.476, 0.488, 0.494 approaches it from below — the usual
pre-asymptotic transient as the sum $\sum_{k>N}k^{-2}$ converges to its
$1/N$ asymptote. The maximum error over the same runs stays at $1.21$ rad/m
because it is dominated by the two kink nodes, where the derivative does not
exist in the classical sense.

---

## ★6 — What the stagnation does and does not mean

The colleague's conclusion is wrong on two counts.

1. **The solution is converging** — just not in the norm they used. The measured
   rms error falls from $5.3\times10^{-1}$ to $1.1\times10^{-1}$ over the same
   range, at order 0.494. A sequence whose rms error falls monotonically is not
   "converging to the wrong answer"; it is converging slowly, at the rate the
   function's regularity permits.
2. **The maximum error is not expected to fall.** At a kink the derivative of the
   interpolant has an $O(1)$ error in a fixed neighbourhood of the kink, for
   every $N$ (the Gibbs effect). Stagnation of a maximum error localised at two
   points is the *signature* of a kink, not evidence of a bug.

**The norm to use** depends on the question. For a convergence claim about the
function as a whole, the rms or $\mathrm{L}^2$ norm is appropriate, and its order
should be quoted together with the coefficient-decay exponent that predicts it.
If the maximum error is the physically relevant quantity — a peak ground motion,
a shock position — then the honest statement is that the maximum error does not
converge, and a different discretisation (a limiter, a front-tracking method, or
an adaptive mesh) is required to control it.

---

## ★7 — Distinguishing a kink from a coarse grid

**Two runs.**

- **Run A — same function, different regularity.** Take a smooth periodic
  function (for example $e^{\sin(2\pi x)}$) and refine. The maximum error must
  fall geometrically to the round-off floor.
- **Run B — same function, kink removed.** Take the function with the kink,
  $|\sin(\pi x)|$, and apply the *same* differentiation operator, but measure the
  error only at the nodes of smooth subintervals that exclude the kink (or on a
  shifted grid on which the kink never coincides with a node).

**Metric.** Two curves against $N$: the maximum error over all nodes, and the
maximum error over the smooth region only.

**Predictions.**

| cause | max error over all nodes | max error over the smooth region |
|---|---|---|
| kink | stagnates at the jump size (measured $1.21$) | falls to round-off |
| too coarse | falls like a power law, and faster at higher $N$ | falls similarly |
| a bug in the operator | stagnates at a level unrelated to the data | stagnates or grows |

The decisive column is the second: a kink gives a *local* obstruction, so
removing the immediate neighbourhood of the kink restores fast convergence. Coarse
resolution affects the whole domain uniformly, so excluding a few nodes does not
change the picture.

The stagnation level is itself a diagnosis, and it can be predicted exactly. For
the Fourier case of the lesson the measured stagnation was
$1.107266\times10^{-1}$, which equals $32/289$ — the size of the *derivative jump*
of the periodic extension of $1/(1+16x^2)$ at the join. For the kinked function
$|\sin(\pi x)|$ the maximum derivative error stagnated at $1.21$ rad/m, i.e. at
$\pi$ to within a few per cent: the jump of the second derivative of the exact
function is what the interpolant's derivative error approaches. In both cases the
floor is a property of the *data*, computable before any run, so a stagnation
level that matches a predicted jump is confirmation, and one that does not is a
bug.

---

## ★8 — Modes for a $\rho = 2$ spectrum

Model: coefficient magnitude $|\hat{u}_m| \le \rho^{-m}$ and derivative error
dominated by the first omitted mode, $E \approx m\rho^{-m}$.

For $\rho = 2$, $\varepsilon = 10^{-8}$: solving $m\,2^{-m} = 10^{-8}$ gives
$m = 31.56$, so $m_{\max} = 32$ modes are needed, and a real function on $N$
uniform points carries modes up to $N/2$, hence

$$N \ge 2m_{\max} = 63.1 \Longrightarrow N = 64 .$$

For $\varepsilon = 10^{-12}$: solving $m\,2^{-m} = 10^{-12}$ gives $m = 45.37$,
so $m_{\max} = 46$ and $N \ge 90.7$, i.e. $N = 96$ (a multiple of 2; spectral
codes also prefer $N$ with small prime factors for the FFT).

**How the answer changes.** Twelve decades of accuracy — a factor $10^{4}$ — cost
a factor $1.5$ in $N$ (64 to 96). Compare $\log_2(1/\varepsilon)$, which grew by
a factor 1.5 as well (26.6 to 39.9): the requirement tracks the *logarithm* of the
target accuracy, not the accuracy itself. For a fourth-order scheme the same
factor $10^{4}$ in accuracy would cost a factor $10$ in $N$; for a second-order
scheme, a factor $100$.
