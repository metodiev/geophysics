# Exercises — 06-03-07 Discriminating Explosions from Earthquakes

Attempt these before reading the
[solutions](./07-nuclear-explosion-sources-solutions.md). The lesson is
[07 Discriminating Explosions from Earthquakes](../07-nuclear-explosion-sources.md)
and the demonstration is
[`../code/nuclear_explosion_demo.py`](../code/nuclear_explosion_demo.py). All
sources are **SYNTHETIC**; no real yield, magnitude, catalogue or calibration
constant is used. Take $\beta = 3500\ \mathrm{m\,s^{-1}}$, $k = 0.37$, and

$$M_0 = \frac{16}{7}\Delta\sigma a^{3},\qquad f_c = \frac{k\beta}{a},\qquad
A(\hat r) = (\hat r\cdot\hat n)(\hat r\cdot\hat s).$$

## ★ Foundational

**★1.** For a purely isotropic source, evaluate
$\hat r^{\mathsf T}M\hat r$ for three arbitrary unit vectors and state the
measured compression fraction. Explain in one sentence why the pattern has no
nodal planes.

**★2.** Compute $2^{-N}$ for $N = 6$, $N = 12$ and $N = 20$, and give each as
$-\log_{10}p$. State which of these is the source-level probability that $N$
independent stations all read compression for a double couple.

**★3.** Compute $a$ and $f_c$ for $M_0 = 1.0\times10^{15}\ \mathrm{N\,m}$ with
(a) $\Delta\sigma = 3.0\ \mathrm{MPa}$ and (b) $\Delta\sigma_{\text{eff}} = 300\
\mathrm{MPa}$. Report the ratio of the two corner frequencies and compare it with
$100^{1/3}$.

## ★★ Applied

**★★4.** Explain, using the model spectrum, why the long-period amplitude
(0.02–0.1 Hz) is nearly independent of the source dimension while the
short-period amplitude (0.5–2 Hz) is not. Support the argument with the two
corner frequencies from ★3 and the band edges.

**★★5.** The demo's $M_0 = 10^{17}\ \mathrm{N\,m}$ row gives
$m_{\text{short}}^{\text{eq}} = 16.991$ and
$m_{\text{short}}^{\text{exp}} = 17.596$ at matched long-period amplitude. Convert
the offset to an amplitude ratio and state what it means physically.

**★★6.** A discriminating analyst reports "the source-level probability is
$9.8\times10^{-4}$". State which station count that corresponds to, what
assumption it rests on, and one mechanism by which the real false-positive rate
could be larger by an order of magnitude.

**★★7.** A third source class is an implosive collapse, modelled as
$M = -M_{\text{iso}}I$ with $M_{\text{iso}}>0$. State the sign of $\mathrm{tr}(M)$
and the first-motion signature, and explain in two sentences how it is separated
from both an earthquake and an explosion.

## ★★★ Research-oriented

**★★★8.** Design a discriminant that combines three independent observables you
could in principle measure, and specify how you would **calibrate** its
false-positive rate (which you cannot compute from the model, and why). State the
observables, the decision rule, the calibration data you would need, and the
assumption each observable rests on.

**★★★9.** The $2^{-N}$ argument assumes independent stations. Design an experiment
using the demo's random-direction machinery to measure how a *spatial
correlation* in station position degrades the effective $N$. Specify the model for
the correlation, the statistic, and the prediction for the effective number of
independent stations as a function of the correlation length.

**★★★10.** The demo's grid search finds an acceptable set spanning $1.25$ decades
in stress drop and one grid step in moment. Write down which combinations of
$(M_0,\Delta\sigma)$ leave the two band amplitudes invariant to first order, and
explain why this degeneracy is unavoidable for *any* two-band discriminant. State
what a third independent observation would have to measure to break it.
