# Exercises — 25-03-01 Project: Magnetic Anomaly Modelling and Depth Estimation

Attempt these before reading the
[solutions](./01-mag-anomaly-modelling-solutions.md). The project is
[01 Magnetic Anomaly Modelling](../01-mag-anomaly-modelling.md). Values printed by
[`code/mag_anomaly_modelling_demo.py`](../code/mag_anomaly_modelling_demo.py):

| Quantity | Value |
|---|---|
| depth to both dipole lines | $4.0\ \mathrm{km}$ |
| strength $k$ | $1000\ \mathrm{nT\,km}$ |
| body A (skew $0°$) | peak $250.0\ \mathrm{nT}$ at $x = -8.00\ \mathrm{km}$, half-width $4.000\ \mathrm{km}$ |
| body B (skew $40°$) | peak $220.7\ \mathrm{nT}$ at $x = 9.40\ \mathrm{km}$, min $-29.2\ \mathrm{nT}$, half-width $4.594\ \mathrm{km}$ |
| $\max|\partial T/\partial x|$ / $\max|\partial T/\partial z|$ | $54.82$ / $57.04\ \mathrm{nT\,km^{-1}}$ |
| $|\mathrm{AS}|$ peak (body B) | $61.1388\ \mathrm{nT\,km^{-1}}$ at $x = 8.00\ \mathrm{km}$ |
| exact $|\mathrm{AS}|$ peak, $k/z^{2}$ | $62.5000\ \mathrm{nT\,km^{-1}}$ |
| $|\mathrm{AS}|$ half-width | $4.160\ \mathrm{km}$ ($+4.0\%$) |
| Lorentzian fit of body B | $x_0 = 7.944\ \mathrm{km}$, $z = 4.137\ \mathrm{km}$ |
| trend $1.5$ / $8.0\ \mathrm{nT\,km^{-1}}$ | raw $4.201$ / $4.515\ \mathrm{km}$; detrended $4.195\ \mathrm{km}$ |
| Monte Carlo (200 draws) | $z = 4.181 \pm 0.017\ \mathrm{km}$; $x_0 = -8.121 \pm 0.009\ \mathrm{km}$ |

Everything is **SYNTHETIC**.

## ★ Foundational

**★1.** Write the total-field anomaly of a 2-D dipole line and evaluate it at
$x = x_0$ for $\theta = 0$ and $\theta = 40°$ with $k = 1000\
\mathrm{nT\,km}$ and $z = 4.0\ \mathrm{km}$. State the unit.

**★2.** Show that the half-width of a symmetric ($\theta = 0$) line anomaly is
exactly $z$, and state the depth rule that follows.

**★3.** Verify the demonstration's gradient pair at $x = 8.00\ \mathrm{km}$ by
computing $|\mathrm{AS}| = \sqrt{(\partial T/\partial x)^{2}+
(\partial T/\partial z)^{2}}$ from the printed values $+40.0740$ and
$-47.3815\ \mathrm{nT\,km^{-1}}$.

## ★★ Applied

**★★4.** A $|\mathrm{AS}|$ profile is fitted by
$1/|\mathrm{AS}| = ax^{2}+bx+c$ with $a = 2.5\times10^{-2}\ (\mathrm{km\,nT})^{-1}$,
$b = -4.0\times10^{-1}\ \mathrm{nT^{-1}}$ and $c = 2.0\ \mathrm{km\,nT^{-1}}$.
Recover $k$, $x_0$ and $z$ with their units, and state which coefficient controls
which quantity.

**★★5.** The skewed anomaly's half-width is $4.594\ \mathrm{km}$ and the analytic
signal's is $4.160\ \mathrm{km}$, against a true depth of $4.0\ \mathrm{km}$; the
symmetric body's anomaly half-width is $4.000\ \mathrm{km}$. Compute all three
biases as percentages, and state which two are magnetisation-driven and which is
discretisation-driven.

**★★6.** At $8.0\ \mathrm{nT\,km^{-1}}$ the trend contributes a constant
$c = 8.0\ \mathrm{nT\,km^{-1}}$ to $\partial T/\partial x$. Compute $c$ as a
fraction of the skew-free anomaly's maximum horizontal derivative
($|\partial T/\partial x|_\text{max} = 54.82\ \mathrm{nT\,km^{-1}}$), and explain
in one sentence why a constant offset distorts a Lorentzian but a constant
*level* in $T$ does not.

## ★★★ Research-oriented

**★★★7.** Design an estimator that recovers **both** the depth and the
magnetisation direction of a compact 3-D source from a grid of total-field data.
State the data you would use, the parameterisation, the objective function, the
non-uniqueness you expect (and the specific trade-off between the two parameters),
and the independent observation that would break it. Then state the test that
would show your estimator is working. A design that cannot separate depth from
magnetisation direction is a failed answer.
