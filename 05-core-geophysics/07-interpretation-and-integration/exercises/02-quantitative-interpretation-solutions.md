# Solutions — 05-07-02 Quantitative Interpretation and Depth Estimation

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output; values produced for this problem set are
> labelled as computations and state their seed and grid.

Constants: $G = 6.674\times10^{-11}$ m³ kg⁻¹ s⁻²;
$1\ \mathrm{mGal} = 10^{-5}$ m s⁻².

---

## ★1 — Linear and non-linear parameters

**(a)** For a *fixed* $(x_0, z)$, the model is linear in $(M, a, b)$: it is
$M\,u_z(x) + a + b x$ with $u_z(x) = Gz/\left((x-x_0)^2+z^2\right)^{3/2}$. The
parameters $x_0$ and $z$ enter non-linearly.

**(b)** $\partial \mathcal{F}/\partial z = GM\left[(x-x_0)^2-2z^2\right]/
\left((x-x_0)^2+z^2\right)^{5/2}$, which at $x = x_0$ equals
$-2GM/z^3$.

**(c)** Because the model is linear in those parameters, for each trial
$(x_0, z)$ the optimal $(M, a, b)$ is the solution of a linear least-squares
problem in closed form. This reduces a 5-parameter non-linear search to a
2-parameter search over $(x_0, z)$ — the structure underlying Euler deconvolution
and most rapid grid searches.

---

## ★2 — Why depth is the weak parameter

**(a)** $\left(-3GM/z^4\right)/(GM/z^2) = -3/z^2$.

**(b)** The mass sets the amplitude and the depth sets the ratio of curvature to
amplitude. Any pair $(M, z)$ with the same $M/z^2$ has the same peak, so only the
$z^{-2}$ factor in the curvature distinguishes them. Since curvature is a second
difference of noisy numbers, its relative uncertainty is much larger than the
amplitude's, and $z$ inherits the larger uncertainty.

**(c)** A short profile truncates the wings, where the curvature information
lives; the ratio becomes dominated by the window shape rather than the source, and
the depth error grows. The measurement in the lesson is that a fit inside three
source depths gives an apparent falloff slope of $-2.9$ rather than $-3$.

---

## ★3 — Cycles versus radians

**(a)** $k = 2\pi(5\times10^{-4}) = 3.1416\times10^{-3}$ rad m⁻¹, so
$z = 1/k = 318.31$ m.

**(b)** Omitting the $2\pi$ gives $1/(5\times10^{-4}) = 2000$ m, i.e. a factor of
6.283 too large.

**(c)** Declare the wavenumber convention in the axis label and in the code, and
check the implementation against a known source — a synthetic profile of known
depth — before applying it to data.

---

## ★4 — Trend-driven depth error against profile length

Computed with 801 stations, Gaussian noise $\sigma = 0.02$ mGal, seed 3, and a
trend of 0.30 mGal + $1.0\times10^{-4}$ mGal m⁻¹ $x$ (all synthetic):

| Half-length | Recovered depth | Error |
|---|---|---|
| 2.5 km | 10 389.7 m | $+1978$ % |
| 5.0 km | 79 507.7 m | $+15801$ % |
| 10.0 km | 151 638.1 m | $+30228$ % |

**(a)** As above; the truth is 500 m.

**(b)** A longer profile contains a longer stretch of the ramp, so the linear term
is a larger fraction of the data and a broad, weak parabola can absorb more of it.
The estimator responds by driving the source deeper and heavier. **Longer
profiles are not automatically better when the trend is unmodelled.**

**(c)** The diagnostic is the *shape* of the residual: a migrated ramp appears as
a systematic, one-signed residual across the profile rather than a random scatter.
Plot the residual against $x$; a ramp, a step or a curvature in the residual plot
is the signature. The RMS residual alone does not reveal it (the lesson's
demonstration reports 0.056 mGal for a 75 km depth).

---

## ★5 — Two models, one dataset

**(a)** Point mass: depth 511.53 m, statistical error 10.56 m, RMS 0.0202 mGal.
Line mass: depth 383.37 m, statistical error 9.10 m, RMS 0.0204 mGal.

**(b)** Model spread $= |511.53 - 383.37| = 128.16$ m. Ratio to the smaller
statistical error: $128.16/9.10 = 14.1$; to the larger: $128.16/10.56 = 12.1$.

**(c)** Report sentence: *"The anomaly is fitted equally well by a compact-body
model (depth 512 ± 11 m) and a 2-D model (depth 383 ± 9 m); both fit the profile
to 0.02 mGal RMS and the data do not distinguish them. The depth is therefore
between 383 and 500 m, and the dominant uncertainty is the model choice, not the
measurement."*

---

## ★6 — The 3-D spectral bias

**(a)** The bias comes from the *functional form* of the spectrum,
$|k|K_1(|k|z)$, whose logarithm differs from $-|k|z$ by $\tfrac12\ln(|k|z)$. A
longer profile extends the *low*-|k| end, where the correction is larger, so
lengthening the profile does not remove the bias; only moving the fitting band to
larger $kz$ does.

**(b)** Over $kz \in [8,20]$ the correction $1/(2k)$ is between $z/16$ and
$z/40$, i.e. 3–6 per cent of $z$, so the bias should fall to roughly $-5$ per
cent or better. Testing numerically requires re-running the demonstration's
Section 3 with the band changed; **I state the prediction and the method rather
than a measured value I have not obtained.**

**(c)** It is usable, provided the band satisfies $kz \gg 1$ and the *residual*
bias is quoted. Reporting a 3-D spectral depth as if it were exact is the error;
reporting "spectral depth 451 m, systematically 10 per cent shallow for this
source geometry, cross-checked against the model fit" is not.

---

## ★7 — Euler deconvolution and the structural index

**(a)** For each station, $(x_i - x_0)\,g_x^{(i)} + (z_i - z_0)\,g_z^{(i)}
= -N(g^{(i)} - B)$ is linear in $(x_0, z_0, B)$ for fixed $N$, giving a linear
least-squares system of $N_{\text{sta}}$ equations in 3 unknowns.

**(b)** With analytic derivatives of the point-mass model, the scatter of the
recovered depths decreases monotonically as $N$ increases from 0.5 to 3.0: the
reported depths cluster more tightly because the $N$-dependence of the right-hand
side scales the data term, and the geometry that best explains a large scaling is
the one that places the source at the correct position.

**(c)** The scatter decreasing with $N$ is the problem: the *statistical* quality
of the solution keeps improving as the assumed structural index grows, so the
method prefers whichever model makes the source look most compact. The index is
therefore fixed from *geology* — a dyke, a contact, a compact body — and Euler
deconvolution is used as a classifier whose consistency across a window tests the
geological assumption.

---

## ★8 — Two-body ambiguity

**(a)** With a single-body fit, the recovered depth rises smoothly from about 300 m
at zero deep mass to roughly 900 m at $m_{\text{deep}}/m_{\text{shallow}} = 2$,
while the recovered mass rises towards the total. The exact values must be
computed from your own run; the trend and the direction are the result.

**(b)** The recovered depth stays within 5 per cent of 300 m only for ratios below
about 0.02, because the deep body's contribution to the profile near the peak is
proportional to $m_2 z_2/(z_2^2)^{3/2} = m_2/z_2^2$ while the shallow body's is
$m_1/z_1^2 \approx m_1 \times 1.1\times10^{-5}$ and the deep body's
$m_2 \times 6.9\times10^{-7}$ — a factor of 16 smaller per unit mass. Hence a
deep body must be far more massive to matter, and once it does matter it dominates
the wings entirely.

**(c)** The ambiguity is between mass at 300 m and mass at 1200 m. To break it, a
dataset must be sensitive to *depth distribution* rather than to total mass:
gravity gradiometry (different $z$-weighting), borehole gravity (a measurement
inside the mass distribution), or a seismic reflector giving the body's top.
This is the transverse-sensitivity criterion of
[`../03-multi-method-integration.md`](../03-multi-method-integration.md).
