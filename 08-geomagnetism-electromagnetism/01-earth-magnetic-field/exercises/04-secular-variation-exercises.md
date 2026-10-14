# Exercises — 08-01-04 Secular Variation, Jerks and Core Dynamics

Attempt these before reading the
[solutions](./04-secular-variation-solutions.md). The lesson is
[04 Secular Variation, Jerks and Core Dynamics](../04-secular-variation.md). All
values are **SYNTHETIC** teaching values.

Use $a = 6371\ \mathrm{km}$ and $1\ \mathrm{yr} = 3.1557\times10^{7}\
\mathrm{s}$ (365.25 days).

## ★ Foundational

**★1.** A synthetic coefficient has $g_1^0 = -30120\ \mathrm{nT}$ in 1960 and
$-30132\ \mathrm{nT}$ in 1961. Compute the secular variation in
$\mathrm{nT\,yr^{-1}}$ and in $\mathrm{nT\,s^{-1}}$.

**★2.** For a synthetic $g_1^0 = 28000\ \mathrm{nT}$ with
$\dot{g}_1^0 = -35\ \mathrm{nT\,yr^{-1}}$, compute the characteristic timescale
$\tau = |g_1^0|/|\dot{g}_1^0|$, in years.

**★3.** Convert a westward drift of $0.20\ \mathrm{deg\,yr^{-1}}$ into a speed in
$\mathrm{m\,s^{-1}}$ at the equator, showing the unit chain from degrees of
longitude to metres.

## ★★ Applied

**★★4.** A pattern has the form $p(\phi) = \cos m(\phi-\Delta)$ with $m = 2$ and
$\Delta = 1.2^{\circ}$. Show that the argument of
$\sum_k p_k e^{-im\phi_k}$ equals $m\Delta$ and recover $\Delta$ from a synthetic
sum. Then state the largest shift the method can measure unambiguously, and the
aliasing rate if the pattern is reused after 8 yr.

**★★5.** Derive the variance of the centred SV estimator
$\hat{E}'_i = (E_{i+1}-E_{i-1})/2\Delta t$ for white noise of variance
$\sigma^2$ on the samples, and verify the ratio $\sqrt{1/2}$ quoted in the
lesson. Repeat for the acceleration estimator
$(E_{i+2}-2E_i+E_{i-2})/4$ and compare with $\sqrt{6}/4$.

**★★6.** A main-field model is fitted at 1995 with a secular-variation term of
$-30\ \mathrm{nT\,yr^{-1}}$ for $g_1^0$, but the true rate changes to
$-45\ \mathrm{nT\,yr^{-1}}$ in 2000. Derive the expression for the model error as
a function of time and evaluate it for 2010 and 2025.

## ★★★ Research-oriented

**★★★7.** Design a jerk-detection experiment from a synthetic observatory series
with a stated noise level and a stated sampling interval. State the metric, the
window length, the trade-off between the aliasing limit of a drift estimate and
the noise gain of the third derivative, and one prediction that would falsify a
claimed jerk epoch. A specification that could not be executed is a failed
answer.

**★★★8.** Construct an explicit element of the null space of the frozen-flux
inversion. Start from
$\partial B_r/\partial t = -\nabla_h\cdot(\mathbf{u}B_r)$ and show that a
divergence-free horizontal flow $\mathbf{u}$ that runs along the contours of
$B_r$ produces no secular variation at all, so no data can constrain it. State
which two assumptions about the flow your construction uses.
