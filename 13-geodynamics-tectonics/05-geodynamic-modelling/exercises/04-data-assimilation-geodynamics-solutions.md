# Solutions — 13-05-04 Data Assimilation and Adjoint Geodynamics

> **Read after attempting the exercises.** Numbers were computed from the same
> model as the lesson's demonstration.

Lesson: [04 Data Assimilation and Adjoint Geodynamics](../04-data-assimilation-geodynamics.md).

---

## ★1 — The adjoint of one diffusion step

With $A = I + \nu L$ (and $L$ symmetric), one step is $\theta^{n+1} = A\theta^n$
and the transpose application is $A^{\mathsf{T}}\lambda = (I+\nu L)\lambda$ — the
*same* matrix for a symmetric operator, applied in reverse order along the time
sequence: the adjoint state at step $n$ is obtained from the adjoint state at step
$n+1$. The backward direction is not an algebraic accident: the adjoint of a
product is the product of the adjoints in reverse order,
$(A_1A_2\cdots A_N)^{\mathsf{T}} = A_N^{\mathsf{T}}\cdots A_2^{\mathsf{T}}A_1^{\mathsf{T}}$,
and the temporal ordering of the forward run is exactly what is reversed. For a
non-symmetric advection step the transpose is genuinely a different matrix, and
the adjoint integration must use it.

---

## ★2 — Mode-9 survival

$$\frac{9.229\times10^{-5}}{8.939\times10^{-1}} = 1.032\times10^{-4} .$$

A mode-9 initial amplitude of 1 produces an observable of $9.2\times10^{-5}$. A
noise level of $0.1\% = 10^{-3}$ is an order of magnitude larger than that
signal, so mode 9 is **not recoverable**: only about the first seven modes carry
singular values above $10^{-3}$ (the demonstration counts 7 of 64). In digits:
the mode-9 amplitude would have to be recovered from a measurement whose noise is
$10\times$ the signal, which is impossible regardless of the inversion method.

---

## ★3 — The gradient

$$J(m) = \tfrac12\|Mm-d\|^2 \quad\Longrightarrow\quad
\nabla J(m) = M^{\mathsf{T}}(Mm-d).$$

The transpose is all that is needed because $J$ is quadratic and the derivative
of a linear map $Mm$ with respect to $m$ is $M$ itself: the chain rule produces
$M^{\mathsf{T}}$ acting on the residual, and no second derivatives appear. The
practical consequence is that the gradient costs one forward application (to form
the residual) and one transposed application, independent of the number of
parameters.

---

## ★4 — What the gradient test proves

A central difference with step $\epsilon$ has a truncation error
$O(\epsilon^2)$ and a round-off error $O(\varepsilon_{\text{mach}}/\epsilon)$;
their sum is minimised at $\epsilon \sim \varepsilon_{\text{mach}}^{1/3}$,
giving a best achievable relative accuracy of order
$\varepsilon_{\text{mach}}^{2/3} = (2.2\times10^{-16})^{2/3} = 3.6\times10^{-11}$
in exact arithmetic, and in practice nearer $2\times10^{-5}$ for this problem's
scaling. The measured agreement of $5.7\times10^{-9}$ is therefore *better* than
the quoted practical resolution of the difference quotient.

**What it proves:** the adjoint implementation is consistent with the forward
implementation to the accuracy of the test. **What it does not prove:** that
either is correct (they could share a modelling error), nor anything about the
inverse problem's conditioning.

---

## ★5 — How many modes each noise level admits

From the measured spectrum (indices 0, 1, 2, 4, 8, 16 with values
$8.939\times10^{-1}$, $6.383\times10^{-1}$, $3.636\times10^{-1}$,
$5.946\times10^{-2}$, $9.229\times10^{-5}$, $4.367\times10^{-16}$) and the
counts printed by the demonstration:

| noise level | singular-value threshold | modes admitted |
|---|---|---|
| $10^{-2}$ | 0.01 | about 5 (indices 0–4; index 5 is already below) |
| $10^{-3}$ | 0.001 | 7 of 64 (measured) |
| $10^{-4}$ | $10^{-4}$ | 9 of 64 |
| $10^{-6}$ | $10^{-6}$ | 10 of 64 (measured) |

Increasing the number of grid points adds *high-wavenumber* modes, and the
diffusion damps them exponentially: their singular values are smaller than the
smallest double-precision number for $\kappa k^2 T \gtrsim 40$. So refining the
grid adds modes whose singular values are far below the noise, and the number of
recoverable modes — set by the noise level and the elapsed diffusion time — does
not change.

---

## ★6 — Finite-difference versus adjoint cost

One-sided differences: $p+1$ forward runs; central differences: $2p$. For $p = 25$:

$$\text{central: } 50\times0.0027\ \mathrm{ms} = 0.135\ \mathrm{ms},$$

against the adjoint's 0.0116 ms — a factor of 11.6. For $p = 5000$:
$10\,001\times0.0027 = 27.0$ ms against 0.0116 ms, a factor of 2330.

**Break-even:** the adjoint costs one forward plus one transposed application,
which is equivalent to about $0.0116/0.0027 = 4.3$ forward runs, so the adjoint
wins as soon as $p \gtrsim 2$ (one-sided differences, $p+1$ runs). The break-even
is therefore at a *handful* of parameters, and the adjoint's advantage grows
linearly from there. The caveat is engineering, not mathematics: for $p = 2$ the
extra code and the risk of a coding error usually outweigh a factor of 2.

---

## ★7 — Why a 16.7% difference is invisible

The direction of the difference is the trailing singular vector of the forward
map — the mode the diffusion damps hardest. Because the map is linear, the
observable difference is exactly $\sigma_{\min}$ times the state difference:

$$\frac{\|\Delta d\|}{\|d\|} = \frac{\sigma_{\min}\|\Delta m\|}{\|d\|}
\approx 2.4\times10^{-20}\times0.167 \approx 10^{-20},$$

which is below the resolution of a double-precision observable (the measured
$1.3\times10^{-16}$ is the round-off floor of the arithmetic, not a physical
signal). This is a property of the **forward map**, not of the inversion: an
algorithm cannot invent information that the forward operator destroyed, and no
regularisation, prior or optimiser changes the spectrum. The null-space component
must instead be *chosen* (by a prior or a regularisation), and the choice must be
reported.

---

## ★8 — Uncertainty of an uncertainty

The fractional sampling error of a standard deviation estimated from $N$
independent members is approximately $1/\sqrt{2N}$. For $N = 25$:
$1/\sqrt{50} = 0.141$, so the reported $\sigma = 0.2\times10^{21}$ carries about
**14% of its own uncertainty**, i.e. $0.2\pm0.03\times10^{21}$ Pa s *from
sampling alone*, before any model error.

**Report instead:** the value with its sampling uncertainty stated, the ensemble
size, the observation-error assumption used, and — the decisive extra — an
estimate of model error (for example from an ensemble with perturbed parameters,
or from a synthetic recovery test in which the truth is known). With 25 members
the sampling uncertainty is already comparable to the parameter's physical
uncertainty, so the honest conclusion is usually that the ensemble is too small
to support a strong statement.

---

## ★9 — Removing one unrecoverable mode

**Observable.** A measurement of the *initial* state itself at a time close to
the start of the interval, or an integral of the state over the interval, rather
than only the final state.

**Why it changes the spectrum.** The singular values are the amplification
factors $\exp(-\kappa k^2 T)$ for a single observation at time $T$. A second
observation at time $T_1 < T$ adds a row block with amplification
$\exp(-\kappa k^2 T_1) > \exp(-\kappa k^2 T)$ for every mode, which raises the
smallest singular value of the stacked operator and therefore admits more modes.
Equivalently, the *shortest* observation interval sets the highest recoverable
wavenumber: the information content is governed by the total elapsed diffusion
time, so splitting the interval into several observation times beats one long
interval.

**Cost.** Each additional observation time multiplies the data vector and the
storage of the forward state (for a time-stepping model, the adjoint needs the
stored trajectory anyway); for a large 3-D model the storage, not the arithmetic,
is the limiting cost. In geodynamics this is the argument for combining
present-day geodesy with a *history* of sea-level or palaeo-thermal markers rather
than measuring the present state more precisely.

---

## ★10 — Questions for a grid-scale "recovery"

1. **What is the resolution of the recovered structure, and how does it compare
   with the singular-value cut-off of the forward map?** *Defensible answer:* the
   structure is at scales whose singular values exceed the noise level, and the
   figure is annotated with the cut-off wavenumber; the grid-scale appearance is
   an artefact of plotting a low-pass field on a fine grid.
2. **What was the prior or regularisation, and how much of the reported
   structure is it?** *Defensible answer:* a stated smoothness or minimum-norm
   prior, with a synthetic test showing the recovered field from a *known* truth
   and reporting the error, not only the fit.
3. **Is the quoted misfit consistent with the data uncertainty, and is the
   recovered field stable under a change of regularisation weight?** *Defensible
   answer:* the misfit is within the noise level $\chi^2$ band, and the
   large-scale features are unchanged when the weight is varied over a stated
   range — with the small-scale ones reported as unresolved.

A figure that cannot answer all three is a picture of the prior, not a
measurement.
