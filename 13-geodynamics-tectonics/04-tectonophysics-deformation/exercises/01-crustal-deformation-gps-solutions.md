# Solutions — 13-04-01 Crustal Deformation from GNSS and Strain Rates

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [01 Crustal Deformation from GNSS and Strain Rates](../01-crustal-deformation-gps.md).

---

## ★1 — Unit conversions

$25\ \mathrm{nstrain\,yr^{-1}} = 25\times10^{-9}\ \mathrm{yr^{-1}}
= 2.5\times10^{-8}\ \mathrm{yr^{-1}}$.

From $10^{3}\ \mathrm{nstrain\,yr^{-1}} =
1\ \mathrm{mm\,yr^{-1}\,km^{-1}}$, we get
$25\ \mathrm{nstrain\,yr^{-1}} = 0.025\
\mathrm{mm\,yr^{-1}\,km^{-1}}$.

Velocity difference across $80\ \mathrm{km}$:
$2.5\times10^{-8}\ \mathrm{yr^{-1}}\times80\ \mathrm{km} =
2.0\times10^{-6}\ \mathrm{km\,yr^{-1}} = 2.0\ \mathrm{mm\,yr^{-1}}$
(using $1\ \mathrm{km\,Myr^{-1}} = 1\ \mathrm{mm\,yr^{-1}}$, and
$1\ \mathrm{km\,yr^{-1}} = 10^{6}\ \mathrm{mm\,yr^{-1}}$, so
$2.0\times10^{-6}\ \mathrm{km\,yr^{-1}} = 2.0\ \mathrm{mm\,yr^{-1}}$ ✔).

---

## ★2 — Decomposition

$$
E = \tfrac12(L + L^{\mathsf T}) = \begin{pmatrix}
20 & \tfrac12(-8+28) \\ \tfrac12(28-8) & -14\end{pmatrix}\times10^{-9}
= \begin{pmatrix} 20 & 10 \\ 10 & -14\end{pmatrix}\times10^{-9}\
\mathrm{yr^{-1}},
$$

$$
W = \tfrac12(L - L^{\mathsf T}) = \begin{pmatrix}
0 & \tfrac12(-8-28) \\ \tfrac12(28+8) & 0\end{pmatrix}\times10^{-9}
= \begin{pmatrix} 0 & -18 \\ 18 & 0\end{pmatrix}\times10^{-9},
$$

so $w = 18\times10^{-9}\ \mathrm{yr^{-1}}$ (positive = counter-clockwise) and
$\mathrm{tr}\,E = (20-14)\times10^{-9} = 6\times10^{-9}\ \mathrm{yr^{-1}}$.

Check: $\mathrm{tr}\,E = \mathrm{tr}\,L$ ✔ (the antisymmetric part is traceless).

---

## ★3 — Principal strain rates and azimuth

$\mathrm{tr}\,E = 6\times10^{-9}$, so $\mathrm{tr}/2 = 3\times10^{-9}$.
$\det E = (20)(-14) - (10)(10) = -280-100 = -380$ (in units of $10^{-18}$).

$$
\lambda = 3 \pm \sqrt{9 + 380} = 3 \pm 19.723
\quad\Longrightarrow\quad
e_1 = 22.723\times10^{-9},\quad e_2 = -16.723\times10^{-9}\ \mathrm{yr^{-1}} .
$$

Check: $e_1 + e_2 = 6\times10^{-9} = \mathrm{tr}\,E$ ✔.

Azimuth of $e_1$: solve $(E - e_1I)v = 0$. First row:
$(20-22.723)v_x + 10v_y = 0 \Rightarrow v_y = 0.2723v_x$, so with
$v = (\cos\theta, \sin\theta)$ in (east, north) components,
$\tan\theta = 0.2723$ and $\theta = 15.23^\circ$ from east. Measured clockwise
from north, the azimuth is $90^\circ - 15.23^\circ = 74.77^\circ$.

---

## ★4 — Is the recovery consistent?

Difference: $29.941 - 30.000 = -0.059\times10^{-9}\ \mathrm{yr^{-1}}$.
Significance: $-0.059/3.080 = -0.019\sigma$. **Entirely consistent** with zero —
better than one-fiftieth of a standard deviation, which happens roughly two
times in a hundred realisations by chance and is unremarkable for a single
noise draw.

The residual variance check is separate: the residual rms is
$0.417\ \mathrm{mm\,yr^{-1}}$ against $0.5\ \mathrm{mm\,yr^{-1}}$ input noise.
That is *below* the input value, as expected, because the residuals are computed
after subtracting six fitted parameters from $48$ observations, so the expected
residual variance is
$\sigma^{2}(2N-6)/(2N) = 0.5^{2}\times42/48 = 0.219$, giving an expected rms of
$0.468\ \mathrm{mm\,yr^{-1}}$. The measured $0.417$ is $11\%$ low, well within
the sampling variability of a variance estimate with $42$ degrees of freedom
($\sim15\%$).

**The important point:** a component recovered to $0.02\sigma$ is not evidence
that the method is accurate — it is one noise realisation. The meaningful
statement is the *ensemble* one: over 200 realisations the rms error is
$0.136\times10^{-9}\ \mathrm{yr^{-1}}$ for the global Euclidean case, matching
the formal $\sigma$.

---

## ★5 — Adding a rigid rotation

Velocity change: $\Delta v = \omega \times r$ with
$\lvert\Delta v\rvert = \omega\times\text{aperture}$ for a site at the network
edge. With $\omega = 10\times10^{-9}\ \mathrm{yr^{-1}}$ and
$L = 140\ \mathrm{km}$: $\Delta v = 1.4\times10^{-6}\ \mathrm{km\,yr^{-1}}
= 1.4\ \mathrm{mm\,yr^{-1}}$ at the edge (and zero at the network centre).

- The **strain rate** is unchanged. In the lesson's experiment the maximum change
  in any component of $E$ was $6\times10^{-17}\ \mathrm{yr^{-1}}$, i.e.
  numerical zero.
- The **rotation rate** shifts by exactly the added amount: $+10.000\times10^{-9}
  \ \mathrm{yr^{-1}}$.

**Why the two cannot be separated:** a rigid rotation of the frame and a rigid
rotation of the rock produce identical velocity changes at every station, so no
function of the velocities can distinguish them. The rotation rate is therefore
only meaningful *relative to a stated frame*. This is why coupling and
strain-rate studies fix a frame (a plate-fixed frame, or a frame defined by the
far-field stations) and say so; the choice propagates directly into any quoted
rotation rate.

---

## ★6 — Aperture for a $10\%$ target

Target: $\delta e_1 = 0.10\times20 = 2.0\times10^{-9}\ \mathrm{yr^{-1}}$ at
$0.5\ \mathrm{mm\,yr^{-1}}$ noise.

$$
L = \frac{386}{2.0} = 193\ \mathrm{km}.
$$

(The rule is fitted to the demonstration's table, where
$19.299\times20 = 386$ and $1.147\times320 = 367$; the coefficient is constant to
about $5\%$ over the range.)

For $1.0\ \mathrm{mm\,yr^{-1}}$ noise the error doubles, so the required
aperture doubles: $L = 386\ \mathrm{km}$.

**Scaling used:** the aperture rule is linear in the noise (a velocity
*gradient* is a velocity difference divided by a length, so
$\delta(\text{strain rate}) \propto \sigma/L$), hence
$L \propto \sigma$ at fixed target — verified in the demonstration by the
factor-of-two change between the $1\ \mathrm{mm\,yr^{-1}}$ and
$0.5\ \mathrm{mm\,yr^{-1}}$ runs.

---

## ★7 — One suspect station

**Two actions.**
1. **Re-estimate without the station** and compare the recovered tensor (and,
   more importantly, the principal rates and azimuth) with the full solution. If
   nothing material changes, report both and keep the station.
2. **Interrogate the station's history** — antenna change, monument type, local
   subsidence, seasonal signal, coseismic step — because a $20\times$-median
   residual has a mechanical or attributional cause far more often than a
   geophysical one.

**Effect of removing it.** The demonstration's $19.2\ \mathrm{mm\,yr^{-1}}$
blunder at one of $24$ stations moved $e_1$ by $6\%$ of the signal. Removing the
offending station should reduce that to the level of the formal uncertainty
($\sim2$–$3\%$ here). The scaling is roughly the blunder's weight in the least
squares, so with fewer stations the same blunder does proportionally more damage:
a $12$-station network would see an effect of order $2\times$ larger, i.e.
$\sim12\%$. **That is why blunder screening matters more in small networks, which
are exactly the networks that need every station.**

---

## ★8 — Design matrix and centring

For station $i$ with offsets $(\Delta x_i, \Delta y_i)$ from a chosen origin:

$$
A = \begin{pmatrix}
1 & 0 & \Delta x_1 & \Delta y_1 & 0 & 0 \\
0 & 1 & 0 & 0 & \Delta x_1 & \Delta y_1 \\
\vdots & & & & & \\
1 & 0 & \Delta x_N & \Delta y_N & 0 & 0 \\
0 & 1 & 0 & 0 & \Delta x_N & \Delta y_N
\end{pmatrix},
\qquad
m = \begin{pmatrix} v_{E0} \\ v_{N0} \\ L_{EE} \\ L_{EN} \\ L_{NE} \\ L_{NN}
\end{pmatrix} .
$$

The translation columns are orthogonal to the gradient columns if and only if
$\sum_i \Delta x_i = \sum_i \Delta y_i = 0$, i.e. the offsets are measured from
the **station centroid**. Then $A^{\mathsf T}A$ is block diagonal:

$$
A^{\mathsf T}A = \begin{pmatrix}
2N\,I_2 & 0 \\ 0 & B\end{pmatrix},
$$

with $B$ depending only on the centred coordinates.

**Why it matters.** With block diagonality the translation and gradient
estimates are *uncorrelated*, so $C_m$ is also block diagonal and the
six-parameter covariance factors into a clean translation part
$\sigma^{2}/(2N)I$ and a gradient part $\sigma^{2}B^{-1}$. If the origin is
placed anywhere else (for example at a reference station), the two blocks are
correlated: the reported uncertainties on the tensor components then depend on
the arbitrary choice of origin, and the correlation between the tensor
components and the reference velocity makes the covariance hard to interpret.
Centring is a one-line change that removes an artefact — and it is the reason the
demonstration subtracts $\bar x$ before building the design matrix.

---

## ★9 — Uncertainty versus geometry and noise correlation (specification)

**Metric.** $\varepsilon = \operatorname{rms}$ over realisations of the error in
$e_1$ (equivalently, the mean of the formal $\sigma(e_1)$), plus $\mathrm{cond}(A)$
and the mean formal $\sigma$ for comparison.

**Design.** Three one-at-a-time families with 200 realisations each at
$0.5\ \mathrm{mm\,yr^{-1}}$ marginal noise:
(i) aperture $L = 20$–$640\ \mathrm{km}$, $N = 20$ fixed;
(ii) $N = 5$–$80$ within $L = 160\ \mathrm{km}$ fixed;
(iii) two spatial correlation models, an exponential kernel with correlation
length $\ell = 0, 10, 50, 200\ \mathrm{km}$, at $L = 160\ \mathrm{km}$,
$N = 20$.

**Predictions.**
(i) $\varepsilon \propto 1/L$, as measured ($19.3 \to 1.15$ over a $16\times$
aperture change).
(ii) $\varepsilon \propto 1/\sqrt N$ until the sampling of the aperture
saturates, beyond which it flattens (a fixed aperture carries finite independent
gradient information).
(iii) $\varepsilon$ grows with $\ell$ and, for $\ell \gtrsim L$, approaches the
level expected if the effective number of independent stations were
$N_{\text{eff}} \sim (L/\ell)^{2}$ rather than $N$. The predicted
$\varepsilon(\ell \gg L)/\varepsilon(\ell=0)$ is therefore of order
$\sqrt{N/N_{\text{eff}}} = \sqrt N\,\ell/L$.

**Falsification.** Family (iii) failing to inflate the error by more than a
factor $\sim2$ for $\ell = 200\ \mathrm{km}$ would indicate that the correlated
component is being absorbed by the translation parameters (it is exactly a
translation for $\ell \to \infty$), which is itself a useful result: it would mean
that large-scale common-mode error is harmless while intermediate-scale error is
the dangerous one.
