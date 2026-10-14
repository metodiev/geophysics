# Solutions — Observing Modern Sea Level Rise: Altimetry, Tide Gauges, GRACE

Worked arithmetic for
[`02-sea-level-rise-observation-exercises.md`](02-sea-level-rise-observation-exercises.md).
**All models and data are SYNTHETIC.**

## ★ Foundational

**1.1** $\sigma_b=(8/25)\sqrt{12/300}=0.32\times0.200=\mathbf{0.064\ mm/yr}$. Doubling
$T$ at the same sampling halves it to 0.032 mm/yr (the $n$ in the square root doubles
and $T$ doubles, so the whole expression halves) — **duration is the lever**.

**1.2** $\bar t=15$ yr, so bias $=0.08\times15=\mathbf{1.20\ mm/yr}$, which is
$1.20/3.4=\mathbf{35.3\%}$ of the trend.

**1.3** The gauge reports $3.4+2.0=\mathbf{5.4\ mm/yr}$; the bias is
$\mathbf{+2.0\ mm/yr}$, i.e. **59%** of the true rise.

## ★★ Applied

**2.1** (a) A 20% error on 2.0 mm/yr is **0.4 mm/yr** of residual bias. (b) The
correction error is $0.4/3.4=\mathbf{11.8\%}$ of the signal — and note that this is
larger than the random trend error of a quarter-century of data, which is why gauge
networks invest in co-located GNSS.

**2.2** Residual $=3.20-1.70-1.60=\mathbf{-0.10\ mm/yr}$;
$\sigma=\sqrt{0.40^2+0.25^2+0.20^2}=\sqrt{0.2625}=\mathbf{0.51\ mm/yr}$. The residual
is $0.2\sigma$, consistent with zero. Mass rate:
$1.70\times361=\mathbf{614\ Gt/yr}$.

**2.3** (a) inflation $=\sqrt{1.6/0.4}=2.00$, so
$\sigma=0.064\times2.00=\mathbf{0.128\ mm/yr}$. (b) The drift bias of 1.20 mm/yr is
**9.4 times** the inflated random term. Reduce the **drift** — more data or denser
sampling cannot remove a systematic trend bias.

## ★★★ Research-oriented

**3.1** (a) $SL=2\times10^{18}/(1025\times3.61\times10^{14})=\mathbf{5.41\ m}$.
(b) $GM=g\,r\,h\Rightarrow r=GM/(gh)
=6.674\times10^{-11}\times2\times10^{18}/(9.81\times5.41)=2.52\times10^{6}$ m, i.e.
**≈2500 km**. (c) Ocean self-attraction and loading deformation (both of which
redistribute the meltwater and reduce the net attraction at moderate distance, moving
the crossover outward somewhat) and rotational feedback (which shifts mass toward the
equator and adds its own pattern). The point-mass value therefore brackets the result
rather than predicting it.

**3.2** (a) Over the half-record mean time $\bar t=7.5$ yr, a 0.10 mm/yr²
acceleration changes the mean rate by $c\bar t=0.10\times7.5=\mathbf{0.75\ mm/yr}$,
which exceeds the 0.5 mm/yr drift uncertainty and is therefore detectable *in
principle*. But it has exactly the same time signature as a linear instrument drift,
so it is not distinguishable from one by these data alone.
(b) A longer record does not break the degeneracy because the drift model and the
acceleration both scale with $\bar t$; only independent instrument validation (or a
mission overlap with a differently drifting instrument) separates them.

**3.3** (a) If two systems share an error source $\delta$, the variance of their
difference includes $2\delta^2$ only if the errors are independent; with correlation
$\rho=1$ the errors add linearly instead of in quadrature, so
$\sigma_{\text{budget}}=\sum\sigma_i$ rather than $\sqrt{\sum\sigma_i^2}$ — up to a
factor of 1.7 larger for three comparable terms.
(b) Recomputed the budget after removing the shared term (e.g. use an alternative
ocean mask or a different correction set) and check whether the residual's variance
falls with the number of systems; a residual that does not shrink as systems are
added is the signature of a common systematic.
