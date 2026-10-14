# Exercises — 06-02-03 The tau-p Transform and Intercept Time

Attempt these before reading the
[solutions](./03-tau-p-solutions.md). The lesson is
[03 The tau-p Transform and Intercept Time](../03-tau-p.md). All models are
**SYNTHETIC** teaching values. Numbers marked "from the demo" are printed by
`code/tau_p_demo.py`.

## ★ Foundational

**★1.** An arrival has $X = 40.0$ km at $p = 1.30\times10^{-4}\
\mathrm{s\,m^{-1}}$ and $T = 6.400$ s. Compute $\tau$ at that point, with units,
and state what $\tau$ measures physically.

**★2.** A single layer of thickness $h = 5.00$ km and
$v_1 = 6.00\ \mathrm{km\,s^{-1}}$ overlies a half space of
$v_2 = 6.50\ \mathrm{km\,s^{-1}}$. Compute $\tau(p)$ at $p = 0$ and at
$p = 1/v_2$, and give the offset at the second point. State the name of each of
the two resulting numbers in the language of Lesson 02.

**★3.** From the demo table, one row is $p = 1.858782\times10^{-4}\
\mathrm{s\,m^{-1}}$, $X = 22.3288$ km, $T = 5.9421$ s, $\tau = 1.7916$ s. Verify
the relation $\tau = T - pX$ numerically and state the unit of $pX$.

## ★★ Applied

**★★4.** Derive Benndorf's relation $\mathrm{d}\tau/\mathrm{d}p = -X$ from
$\tau = T - pX$ and $\mathrm{d}T/\mathrm{d}X = p$. Then explain in words why the
same algebra shows that $(T, X)$ and $(\tau, -p)$ are a Legendre-transform pair.

**★★5.** The demonstration measures a mean offset error of 4473.411 m for
$\sigma_T = 10.0$ ms and ray-parameter spacing $\mathrm{d}p = 1.250\times10^{-6}\
\mathrm{s\,m^{-1}}$, against a prediction of 5656.854 m. State the prediction
formula, evaluate it, and compute the spacing that would keep the offset error
below 1.0 km with the same pick uncertainty.

**★★6.** In a sphere, $p = r\sin i/v$. At $r = 6371$ km, $i = 30^\circ$ and
$v = 8.00\ \mathrm{km\,s^{-1}}$, compute $p$ in $\mathrm{s\,rad^{-1}}$ and in
$\mathrm{s\,deg^{-1}}$. State the conversion factor you used.

## ★★★ Research-oriented

**★★★7.** A study needs offsets determined to 0.5 km from a $\tau(p)$ curve.
Specify the pick uncertainty and ray-parameter spacing that would achieve it,
using the central-difference error relation, and state what the specification
implies about how many traces the array must supply across the relevant slowness
band. Say which of the two inputs (pick quality or trace spacing) you would
invest in first, and why.

**★★★8.** At a triplication, $\mathrm{d}^{2}\tau/\mathrm{d}p^{2}$ changes sign.
Explain why, describe what the $\tau(p)$ curve looks like on either side, and
specify a numerical diagnostic you could run on a synthetic model to detect the
fold *before* attempting an inversion. State the outcome that would show the
diagnostic had failed.
