# Solutions — 06-07-03 Ambient-Noise Tomography and Monitoring

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Everything is SYNTHETIC. Lesson:
> [03 Ambient-Noise Tomography and Monitoring](../03-noise-tomography.md).

---

## ★1 — A diagonal ray through the grid

The ray direction is $(120,120)$, so its length is

$$L = \sqrt{120^{2}+120^{2}} = 120\sqrt{2} = 169.71\ \mathrm{km}.$$

It crosses one cell per row and column, entering cell $(0,0)$ and leaving at
$(120,120)$: the six crossed cells are the diagonal ones. The path inside each
is

$$\frac{120\sqrt{2}}{6} = 28.28\ \mathrm{km}.$$

The matrix row is therefore

$$G_{i} = \frac{\ell_{ij}}{L_i} = \frac{28.28}{169.71} = \frac{1}{6}
\quad\text{for each of the six diagonal cells, } 0 \text{ elsewhere.}$$

The row sums to $1$, as it must: the data are a *path average*.

---

## ★2 — Phase and phase velocity at 20 s

$$f = \frac{1}{20} = 0.050\ \mathrm{Hz},$$
$$\phi = \frac{2\pi f d}{c} = \frac{2\pi \times 0.050 \times 60}{2.2500}
= \frac{18.8496}{2.2500} = 8.3776\ \mathrm{rad},$$
$$c_{\text{meas}} = \frac{2\pi f d}{\phi} = \frac{18.8496}{8.3776}
= 2.2500\ \mathrm{km\,s^{-1}},$$

which agrees with the lesson's table row ($c$ from phase $2.2506$, error
$+0.0005\ \mathrm{km\,s^{-1}}$). The small positive error in the demonstration is
the finite-difference effect of reading the phase on a discrete frequency grid,
not a physical discrepancy.

---

## ★3 — Frequency step for unambiguous unwrapping

$$\Delta f < \frac{c}{2d} = \frac{3.00}{2\times80} = 0.018750\ \mathrm{Hz}.$$

The demonstration uses $\Delta f = 3.8\times10^{-4}\ \mathrm{Hz}$, i.e. **49
times smaller** than the limit:

$$\frac{0.018750}{3.8\times10^{-4}} = 49.3 .$$

The margin is generous because the demonstration's band is narrow
($0.02$-$0.25\ \mathrm{Hz}$ over 600 samples). For a wide band and a long path
the margin disappears and the measurement must be unwrapped with an
external constraint on the phase velocity — a common and under-reported
pitfall.

---

## ★4 — Misfit against the input noise

The data noise is $0.1\%$ relative slowness, i.e. an rms of
$1.0\times10^{-3}$ in the same units as the data.

$$\text{ratio}(\lambda = 0.003) = \frac{7.76\times10^{-4}}{1.0\times10^{-3}}
= 0.78,$$
$$\text{ratio}(\lambda = 1.0) = \frac{2.47\times10^{-3}}{1.0\times10^{-3}}
= 2.47 .$$

At $\lambda = 0.003$ the model fits **below** the noise level — the misfit is
smaller than the noise, which means the inversion is fitting noise
(over-fitting) and the solution is being shaped by it. At $\lambda = 1.0$ the
misfit is $2.5\times$ the noise: the model is no longer able to reproduce the
data even to the noise level, and the recovered anomaly has lost $45\%$ of its
amplitude ($1.66\%$ against $3.0\%$). The defensible choice sits where the
misfit equals the noise — between $\lambda = 0.03$ and $\lambda = 0.3$ in this
table — and that choice, not the minimum misfit, is what must be justified.

---

## ★5 — Group velocity at 30 s

$$U = \frac{c}{1 + \dfrac{T}{c}\dfrac{dc}{dT}}
= \frac{2.6046}{1 + \dfrac{30.0}{2.6046}\times0.04430}
= \frac{2.6046}{1 + 0.51027} = \frac{2.6046}{1.51027}
= 1.7246\ \mathrm{km\,s^{-1}},$$

which is the tabulated value $1.7246\ \mathrm{km\,s^{-1}}$. The difference from
the phase velocity is

$$\frac{c - U}{c} = \frac{2.6046-1.7246}{2.6046} = 33.8\%.$$

**Reading a phase velocity from an envelope arrival would be wrong by a third at
this period.** This is the most common quantitative error in casual use of
ambient-noise dispersion.

---

## ★6 — Is a reported 2.5% consistent with a true 3.0%?

With the resolution of the demonstration's checkerboard test, the recovered norm
is $93.5\%$ of the true norm, and the recovered *peak* was $2.92\%$ for a true
$3.0\%$ — i.e. a peak ratio of $0.973$ at $\lambda = 0.03$.

Predicted reported amplitude for a true $3.0\%$ anomaly:

$$3.0\% \times 0.935 \approx 2.81\%\quad\text{(norm scaling)}, \qquad
3.0\% \times 0.973 \approx 2.92\%\quad\text{(peak scaling)}.$$

A reported $2.5\%$ is below both predictions: it is $2.5/2.92 = 0.86$ of the
expected peak. **It is not consistent with a $3.0\%$ true anomaly at the same
resolution** unless the damping used in the second study is stronger. From the
lesson's table a peak ratio near $0.86$ requires damping between
$\lambda = 0.3$ (ratio $0.891$) and $\lambda = 1.0$ (ratio $0.552$); linear
interpolation in $\log_{10}\lambda$ gives

$$\log_{10}\lambda = -0.523 + \frac{0.891-0.860}{0.891-0.552}\times 0.523
= -0.475 \quad\Longrightarrow\quad \lambda \approx 0.34 .$$

The right response is to report both studies' damping values and recompute one at
the other's damping, not to average the two amplitudes.

---

## ★7 — Bringing four uncovered cells into the model (specification)

**Diagnosis first.** The four cells have zero path count, and the worst diagonal
of the resolution matrix is exactly $0.000$. The relevant diagnostic is the
**path-count map** and the **diagonal of $\mathbf{R}$**, computed before any
change.

**Deployment change.** Two options.

- *Add stations inside the gap.* Add 3-4 stations inside the ray-poor region
  (the cells with the lowest path counts). With $n$ stations the number of pairs
  is $n(n-1)/2$, so going from 13 to 17 stations raises the pair count from 78
  to 136 ($+74\%$), and the new pairs cross the gap.
- *Use earthquakes as sources.* Adding teleseismic events provides crossing
  paths at no instrument cost, at the price of a different (and harder to
  control) source geometry.

**Expected benefit, quantified.** The quantity to predict is the diagonal of
$\mathbf{R}$: the change should raise the worst diagonal from $0.000$ to a value
reported explicitly, and raise the mean diagonal above the measured $0.884$. A
reasonable target is that every cell has at least two crossing paths and a
resolution diagonal above $0.2$, which makes the map's amplitudes interpretable
instead of being pure leakage.

**Cost.** Four more stations is an installation and maintenance cost, and the
new pairs add data noise: the inversion's variance grows with the number of
parameters (here the grid is fixed, so the variance grows only through the noise
in the new paths). The honest cost statement is the *increase in the posterior
variance* of every cell, not the installation alone.

**Diagnostic after.** Recompute the path-count map, the resolution diagonal and
the checkerboard norm ratio; report all three before/after so the benefit is
measurable rather than asserted.

---

## ★8 — Error budget for monthly monitoring (specification)

| error channel | effect of the tomographic inversion |
|---|---|
| Path-measurement noise (per pair) | **Reduced** by the averaging over many paths, roughly as $1/\sqrt{(\text{number of paths crossing the cell})}$ |
| Null-space leakage from uncovered cells | **Unchanged or amplified**: the inversion spreads it into neighbouring cells; it is not a noise and does not average down |
| Damping bias | **Unchanged**: it scales every recovered amplitude by the same factor, so it cancels in an epoch *difference* only if the damping is identical at both epochs (state this explicitly) |
| Source-direction change between epochs | **Unchanged**: it enters as a travel-time perturbation, i.e. as data, and the inversion cannot separate it from structure |
| Reference-model error | **Unchanged and multiplied**: errors in the reference slowness propagate into every cell of every epoch, and differencing epochs cancels only the *stationary* part |
| Common-mode environmental forcing | **Unchanged** by the inversion; must be handled by differencing epochs or by regression against independent records |

**The single most valuable measurement.** A continuously recorded, independent
high-sample-rate station pair (or pairs) whose source field is known to be
stable — used to measure the common-mode $\delta v/v$ at the same epochs as the
map. Removing a common seasonal cycle from the tomographic time series is worth
more than doubling the station count, because it attacks the two channels
(source change and environmental forcing) that the inversion provably cannot
reduce.
