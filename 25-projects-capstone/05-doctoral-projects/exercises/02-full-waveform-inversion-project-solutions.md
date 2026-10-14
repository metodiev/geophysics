# Solutions — 25-05-02 Project: A Small-Scale Full-Waveform Inversion

Reference solutions. Every number is printed by
[`code/full_waveform_inversion_demo.py`](../code/full_waveform_inversion_demo.py);
all data are **SYNTHETIC**.

## ★1. The discrete scheme, the CFL number and the gradient factor

$$p^{n+1}_i = 2p^n_i - p^{n-1}_i + A_i\bigl(p^n_{i+1} - 2p^n_i + p^n_{i-1}\bigr)
+ \Delta t^2 s^n \delta_{i,i_s},\qquad A_i = \frac{\Delta t^2}{m_i \Delta z^2}.$$

Since $m_i = 1/c_i^2$,

$$A_i = \frac{\Delta t^2 c_i^2}{\Delta z^2} = \Bigl(\frac{c_i\Delta t}{\Delta z}\Bigr)^2
= \mathrm{CFL}_i^2 .$$

So the stability condition $A \le 1$ is exactly the CFL condition. For
$c = 1900\ \mathrm{m\,s^{-1}}$, $\Delta z = 10$ m, $\Delta t = 1$ ms:

$$\mathrm{CFL} = \frac{1900 \times 0.001}{10} = 0.19,\qquad
A = 0.19^2 = 0.0361,\qquad
m = \frac{1}{1900^2} = 2.7701\times10^{-7}\ \mathrm{s^2\,m^{-2}},$$

$$\frac{A}{m} = \frac{0.0361}{2.7701\times10^{-7}} = 1.3032\times10^{5}
\quad\Longrightarrow\quad
\frac{\partial J}{\partial m_j}\Big|_n = -1.3032\times10^{5}\;\lambda^{n+1}_j
\bigl[Lp^n\bigr]_j .$$

The large factor is why the parameters are scaled in the demo: raw gradients of order
$8.3\times10^{7}$ against parameters of order $10^{-7}$ make an unmodified
quasi-Newton line search fail on its first step.

## ★2. The gradient test, its scope, and stability

**Test.** Perturb one parameter at a time by $\pm\epsilon$, form the central
difference of the misfit, and compare the resulting vector with the adjoint gradient:
report the cosine of the angle between them and the magnitude ratio. The demo uses
$\epsilon = 10^{-9}\max(m)$ and obtains $\lVert g_\text{adj}\rVert = \lVert
g_\text{FD}\rVert = 8.3310\times10^{7}$, cosine $1.0000000000$ and ratio
$1.0000009$; the $9\times10^{-7}$ magnitude difference is the truncation error of the
central difference, not an adjoint error.

**What it does not verify.** (i) It is a *consistency* test between two
implementations, so a forward code with a wrong equation has a perfectly consistent
adjoint — the physics must be validated separately (analytic solutions, a convergence
test, or a comparison with a known arrival time). (ii) It tests one point in model
space, so errors that vanish there (a mis-scaled boundary term, a wrong sign in a
term that is zero for a constant model, an error that only appears when the source is
inside a heterogeneous region) are invisible. (iii) It says nothing about the misfit
function being the right one to measure.

**Stability.** $\Delta t \le \Delta z/c_{\max} = 10/2100 = 4.76$ ms. The demo uses
$1$ ms, a safety factor of $4.8$ (CFL $0.21$ against the $1.00$ limit), which is
comfortable for the second-order scheme and leaves room for the frequency-dependent
phase error that a larger time step would introduce.

## ★3. Period, half-period limit and the convergence window

$$T = \frac{1}{12\ \mathrm{Hz}} = 83.33\ \mathrm{ms},\qquad \frac{T}{2} = 41.67\ \mathrm{ms}.$$

Two-way time to the 400 m reflector for a constant-velocity start, $t = 0.800/c_0$,
against the true $0.422$ s:

| $c_0$ (m/s) | $t$ (s) | error (ms) | error / 41.67 ms | converged in the demo? |
|---|---|---|---|---|
| 1900 | 0.4211 | 1 | 0.02 | yes (recovered) |
| 1750 | 0.4571 | 35 | 0.84 | would converge, marginally |
| 1700 | 0.4706 | 49 | 1.17 | no |
| 2300 | 0.3478 | 74 | 1.78 | no (cycle skipped) |

Solving $|0.800/c_0 - 0.4225| = 0.04167$ gives the convergence window

$$c_0 \in [1725,\ 2104]\ \mathrm{m\,s^{-1}},$$

i.e. about $-9\%$ to $+11\%$ of the true average velocity of 1900 m/s over that
interval. **That window, not the optimiser, decides success**, and it is the reason
the demo's 1900 m/s start converges while the 1650 and 2300 m/s starts do not.

## ★★4. Is the successful inversion overfitting?

With $\sigma = 0.0309$, $\sigma^2 = 9.548\times10^{-4}$, and the standard
$\chi^2$ expectation $J = \tfrac{1}{2}(N - p)\sigma^2$:

| model | degrees of freedom | expected $J$ | observed $J$ |
|---|---|---|---|
| true model | 701 | 0.3347 | 0.3301 |
| best-fitting model | $701 - 20 = 681$ | 0.3251 | 0.3228 |

The expected reduction from fitting 20 parameters is
$0.3347 - 0.3251 = 0.0096$ ($2.9\%$); the observed reduction is
$0.3301 - 0.3228 = 0.0073$ ($2.2\%$). Both observations lie within one sampling
fluctuation of their expectations (the relative standard deviation of $\chi^2$ with
701 degrees of freedom is $\sqrt{2/701} = 5.3\%$). **The difference between the
successful inversion and the truth is the ordinary degrees-of-freedom effect of
fitting 20 parameters to 701 noisy data — not overfitting.** The corollary is more
important than the arithmetic: a model that fits *better* than the truth is expected,
so residuals cannot rank models.

## ★★5. The error in the deepest layer

$$\frac{1898}{2100} = 0.904 \quad\Longrightarrow\quad 9.6\%\ \text{too low}.$$

The 12 Hz Ricker's central lobe ends at its first zero crossing, which for
$(1 - 2a)e^{-a}$ with $a = (\pi f t')^2$ is at $a = 0.5$, i.e.

$$t' = \frac{\sqrt{0.5}}{\pi \times 12} = 18.8\ \mathrm{ms},$$

so the central lobe spans $\pm 18.8$ ms and the whole wavelet roughly $\pm 40$ ms
about its arrival. The 600 m reflector arrives at $0.658$ s and the record ends at
$0.700$ s: only $42$ ms of the wavelet is recorded. The central lobe is captured, so
the reflector's *position* is roughly determined, but the tail is truncated, so the
waveform cannot be matched — and the layer velocity, which is constrained by how the
waveform below the reflector behaves, is effectively free. The recovered $1898$
against $2100$ is that freedom showing, and it is an **illumination** limitation, not
an inversion failure: no optimiser can recover a velocity whose reflection is not in
the record.

## ★★6. Resolution limit versus parameterisation

$$\frac{\lambda}{2} = \frac{1}{2}\frac{2100\ \mathrm{m\,s^{-1}}}{12\ \mathrm{Hz}}
= \frac{175\ \mathrm{m}}{2} = 87.5 \approx 88\ \mathrm{m}.$$

The inversion parameterisation uses 20 layers of 50 m, each **1.75 times finer than
the resolution limit**. Consequences: (i) about half of the 20 parameters are not
independently determined, so the problem has a large null space; (ii) the model can
accommodate structure at the 50 m scale that the data cannot verify, which is where
apparent "high-resolution layering" in an FWI image normally comes from; (iii) the
slight over-fit in ★★4 is the mild symptom of the same thing. The disciplined choices
are a coarser parameterisation (about 8 layers of 125 m), an explicit
Tikhonov/smoothing term with the correlation length set to the resolution limit, or
reporting the model with its resolution stated — the last being the only option if
the client wants the fine parameterisation.

## ★★7. The frequency below which the 2300 start is inside the basin

Largest travel-time error for the 2300 m/s start: the 600 m reflector, true
$0.658$ s against $1.200/2.300 = 0.5217$ s, an error of $136$ ms. Satisfying the
half-period criterion requires

$$\frac{T}{2} \ge 0.136\ \mathrm{s} \quad\Longrightarrow\quad
T \ge 0.272\ \mathrm{s} \quad\Longrightarrow\quad f \le 3.68\ \mathrm{Hz}.$$

So the data must be low-pass filtered to about $3.5$ Hz before this starting model is
inside the basin of attraction at *any* frequency band, and 12 Hz data cannot be
inverted directly from it — precisely what the demo shows.

## ★★★8. A multiscale workflow that makes the 2300 m/s start converge

**1. Starting model: remove the long-wavelength error first.** The travel-time error
comes from a wrong *average* velocity, and average velocity is exactly what the
earliest arrivals and the reflection times measure. In a co-located 1-D experiment
the direct arrival and the reflection move-out give the average velocity to each
reflector to a few percent, which shrinks the 74 ms error at 400 m to about 10 ms —
inside the criterion at 12 Hz. In a real survey the standard route is first-arrival
refraction tomography with offsets, which is linear-ish, well conditioned and
independent of the deeper waveform shape. **Do this before any waveform inversion**:
it is cheaper and it is what determines whether the waveform stage succeeds.

**2. Frequency schedule fixed by the criterion.** Start where the *current* model's
largest travel-time error satisfies $\text{error} < 1/(2f)$, then step up by a factor
of about $\sqrt{2}$, re-evaluating the criterion after each stage (the error falls as
the long wavelengths are corrected, so higher bands become admissible):

| stage | band (Hz) | $\lambda$ at 1900 m/s (m) | $\lambda/2$ (m) | criterion allows an error of (ms) |
|---|---|---|---|---|
| 1 | 3.5 | 543 | 272 | 143 |
| 2 | 5 | 380 | 190 | 100 |
| 3 | 7 | 271 | 136 | 71 |
| 4 | 10 | 190 | 95 | 50 |
| 5 | 14 | 136 | 68 | 36 |
| 6 | 20 | 95 | 48 | 25 |

**3. Objective function by stage.** Stage 1: low-pass waveform $L_2$ with strong
smoothing (the data are few and the null space is huge). Stages 2–4: a
**cross-correlation time-shift** misfit, which is convex for time shifts up to half a
period and therefore removes cycle skipping at exactly the stage where it is most
likely. Stages 5–6: the full waveform $L_2$, now that the model is close. This
combination — smoothing plus a shift-based objective plus frequency continuation — is
the standard cure for the failure in §5 of the project.

**4. Resolution claimed per stage.** From the table: about 270 m after stage 1,
95 m after stage 4, and 48 m after stage 6 — *if* the source has energy in the 20 Hz
band. A 12 Hz Ricker has almost none above 20 Hz, so the honest claim for this
dataset is about 70–90 m (stages 5–6), consistent with the $\lambda/2 = 88$ m
computed in ★★6. Claiming finer structure from a frequency-continuation run is
claiming the artefact of the parameterisation.

**5. Tests that the multiscale run reached the global minimum.**

1. **Multi-start convergence.** Run all three starting models (1650, 1900, 2300 m/s)
   through the same schedule. If they converge to the same model within the claimed
   uncertainty, the basin structure has been removed; if two converge to different
   models with equal final misfit, the schedule has merely moved the local minimum.
2. **Per-band discrepancy test.** Require the final residual *in each frequency band*
   to fall to the noise level in that band. A run that fits the low frequencies but
   not the high ones has converged to a smooth local minimum; a run that fits all
   bands has not left the data unexplained anywhere.
3. **Fitted-versus-held-out test.** Withhold one frequency band or one source
   position during the inversion, then predict it. A model that has genuinely found
   the long-wavelength structure predicts the withheld band; a model that has
   absorbed the ambiguity into the low frequencies does not.
4. **Alternative-truth test.** Repeat the whole workflow on a *different* synthetic
   truth (a smooth velocity gradient rather than the layered model) and confirm the
   same schedule and parameterisation recover it. A workflow tuned so that its only
   demonstrated success is the layered model of this project is not yet evidence of
   generality.
5. **Gradient test at every stage**, since the objective function changes between
   stages and a mis-scaled shift-based misfit fails silently.
