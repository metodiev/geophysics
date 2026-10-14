# Exercises — 25-01-02 Project: Mapping Global Seismicity from a Real Catalogue

Attempt these before reading the
[solutions](./02-earthquake-map-solutions.md). The project is
[02 Earthquake Map](../02-earthquake-map.md). Values printed by
[`code/earthquake_map_demo.py`](../code/earthquake_map_demo.py) and used below:

| Quantity | Demonstration value |
|---|---|
| events | 3000 |
| true / generating $b$ | $1.00$ |
| $\overline{M}$ | $4.3841$ |
| mean magnitude step | $0.4341$ (exact $0.4343$) |
| $\hat b$ at $M_c = 4.0$ | $1.0005$ |
| $\sigma_b$ at $N = 3000$ | $0.0183$ |
| $\hat b$ at $M_c = 4.5$, $N = 920$ | $0.9672$ |
| events within 2° of the line | 2319 (77.3%) |
| density on the line | 16.1 per $10°\times10°$ box |

Everything is **SYNTHETIC**; no real catalogue and no real earthquake is used.

## ★ Foundational

**★1.** Compute the mean magnitude step $1/\beta = 1/(b\ln 10)$ for
$b = 1.00$ and for $b = 0.80$, state its unit, and say what a larger $b$ means
for the relative number of small and large events.

**★2.** A regional catalogue above its completeness magnitude has
$\overline{M} = 3.72$ with $M_c = 3.5$ and bin width $\Delta M = 0.1$. Compute
$\hat b$ and state the unit.

**★3.** Using $\sigma_b = b/\sqrt{N}$, compute $\sigma_b$ for the
demonstration's fits at $N = 3000$ and at $N = 920$, and state the number of
events discarded when $M_c$ was raised from $4.0$ to $4.5$.

## ★★ Applied

**★★4.** From the two fitted values, estimate $\mathrm{d}b/\mathrm{d}M_c$ in
per magnitude unit, and use it to predict $\hat b$ at $M_c = 5.0$. State one
reason the extrapolation is unsafe.

**★★5.** The demonstration reports $2319$ events within 2° of the synthetic plate
line and $16.1$ events per $10°\times10°$ box. Compute the density in events per
$5°\times5°$ box and per $1°\times1°$ box, and state which box size you would
choose to *show* the plate line on a map and why.

**★★6.** A colleague fits $b$ over a catalogue in which 40% of the events carry a
magnitude that is systematically $+0.2$ higher than the rest (two instruments on
different scales). Using the demonstration's $\overline{M}$ and $M_c$, compute
the biased $\hat b$ and the bias relative to $1.0005$.

## ★★★ Research-oriented

**★★★7.** Design a declustering experiment for the real ComCat catalogue:
state the declustering rule and its parameters, the two statistics you would
compare before and after (with the reason each is sensitive), how you would
separate the declustering effect from the $M_c$ effect of §6 of the lesson, and
what result would change your published $b$-value by more than its standard
error. A design that could not be executed is a failed answer.
