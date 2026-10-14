# Solutions — 08-05-04 EM Inversion and Dimensionality

> **Read after attempting the exercises.** Numbers were computed, not estimated.
> Lesson: [04 EM Inversion and Dimensionality](../04-em-inversion.md).

---

## ★1 — Standard deviation of one datum

$$|d|=\sqrt{70^2+1440^2}=\sqrt{4900+2073600}=\sqrt{2078500}
=1441.7\ \mathrm{ppm}.$$

Relative contribution: $0.02\times1441.7=28.83\ \mathrm{ppm}$.
Floor: $2\ \mathrm{ppm}$.
Combined in quadrature:

$$w=\sqrt{28.83^2+2^2}=\sqrt{831.2+4.0}=28.90\ \mathrm{ppm}.$$

The floor changes the answer by $0.2\%$ here: at $70$–$1440\ \mathrm{ppm}$ the
relative term dominates, and the floor matters only below about
$100\ \mathrm{ppm}$ of amplitude. **Stating both contributions is what makes the
weight reproducible.**

---

## ★2 — Misfit contribution

Residual: $(72-70)+i(1450-1440)\ \mathrm{ppm}=2+10i\ \mathrm{ppm}$,
$|\text{res}|=\sqrt{4+100}=10.20\ \mathrm{ppm}$. Weighted:

$$\frac{|\text{res}|^2}{w^2}=\frac{10.20^2}{28.90^2}=\frac{104.0}{835.2}=0.1245.$$

For a single complex datum the expected value of $\chi^2_i$ is $2$ (two real
degrees of freedom), so this datum contributes $0.12$, i.e. it is
$\sqrt{2/0.1245}=4.0$ times *better* than expected. One such datum is not
suspicious; a whole data set like it is — either the weights are too large or the
model is fitting noise. Note the arithmetic trap: the misfit is the *sum* of the
squared real and imaginary residuals divided by $w^2$, so $2$ and $10\ \mathrm{ppm}$
produce mostly the $10$: the quadrature channel dominates the fit here, as it does
in most FDEM practice.

---

## ★3 — Target misfit

With weights equal to the true standard deviations,
$\mathbb{E}[\chi^2]=1$. A value of $0.4$ means the model reproduces the *noise
fluctuations* better than chance — it has fitted a particular realisation rather
than the signal — so it indicates that the weights are too large (or the model is
too flexible), and it carries no information advantage.

The demonstration's data illustrate the subtlety: the true model scores
$0.7468$ on its own realisation, so the target there is $0.75$, not $1.00$. With a
single realisation the expected value has a spread of $\sqrt{2/N_{\text{ind}}}$
in the reduced misfit; with 12 real data points that spread is about $0.4$, so
$0.6$ is unremarkable and $0.4$ is at the edge but not impossible. The honest
statement is "consistent with the noise model", not "better than the noise model".

---

## ★4 — Occam normal equations

Let $\mathbf{r}(\mathbf{m})=W(\mathbf{d}^{\text{pred}}(\mathbf{m})
-\mathbf{d}^{\text{obs}})$ and linearise
$\mathbf{r}(\mathbf{m}+\Delta\mathbf{m})\approx\mathbf{r}+J\Delta\mathbf{m}$ with
$J=\partial\mathbf{r}/\partial\mathbf{m}$. Then

$$\Phi\approx\lVert\mathbf{r}+J\Delta\mathbf{m}\rVert^2
+\mu\lVert R\mathbf{m}+R\Delta\mathbf{m}\rVert^2.$$

Expanding and differentiating with respect to $\Delta\mathbf{m}$:

$$\frac{\partial\Phi}{\partial\Delta\mathbf{m}}
=2J^{\mathsf{T}}\left(\mathbf{r}+J\Delta\mathbf{m}\right)
+2\mu R^{\mathsf{T}}R\left(\mathbf{m}+\Delta\mathbf{m}\right)=0,$$

hence

$$\left(J^{\mathsf{T}}J+\mu R^{\mathsf{T}}R\right)\Delta\mathbf{m}
=-J^{\mathsf{T}}\mathbf{r}-\mu R^{\mathsf{T}}R\,\mathbf{m}.$$

**Reading the terms:** $J^{\mathsf{T}}\mathbf{r}$ is the data-driven direction
(steepest descent on the misfit); $J^{\mathsf{T}}J$ measures how strongly the data
constrain each parameter combination; $R^{\mathsf{T}}R$ penalises differences
between neighbouring layers, so it is the term that produces smoothness; and
$\mu$ sets the ratio between them. If $\mu=0$ the system is $J^{\mathsf{T}}J
\Delta\mathbf{m}=-J^{\mathsf{T}}\mathbf{r}$ and the solution is the (possibly
unstable) least-squares step; if $J$ has a null direction, only the $\mu$ term
keeps the system invertible, which is the mathematical reason regularisation is
not optional.

---

## ★5 — Formal uncertainty per direction

$$\delta m_k=\frac{\sqrt{\chi^2}}{s_k},\qquad \sqrt{0.591}=0.7688.$$

Best direction: $\delta m_1=0.7688/145.7011=0.00528$ in $\log_{10}$ units, i.e. a
factor $10^{0.00528}=1.0122$ — about $1.2\%$ in conductivity.

Worst direction: $\delta m_6=0.7688/1.0397=0.7394$ in $\log_{10}$ units, i.e. a
factor $10^{0.7394}=5.49$ — the conductivity along that combination is uncertain
by more than a factor of five.

**Interpretation.** These are uncertainties on *combinations* of layer
conductivities, not on individual layers: the singular vectors mix adjacent
layers. Reporting "$\sigma_6 = 0.019\ \mathrm{S\,m^{-1}}$" without the fact that
its direction is a factor-of-five uncertainty is the commonest overclaim in
published 1-D EM models. The demonstration prints the same numbers, computed from
the same Jacobian.

---

## ★6 — Choosing between two inversions

The two models have $\chi^2$ of $0.5906$ and $0.4033$ against a target of $0.7468$:
both fit at least as well as the truth, and **the data cannot choose between
them** — that is exactly what "non-uniqueness" means when it is demonstrated
rather than asserted. What chooses is information from outside the data:

1. geology or a borehole that fixes the depth of a formation boundary;
2. a nearby sounding with a different geometry (another separation, another
   frequency band) whose misfit would separate the two models;
3. an explicit smoothness prior, stated as such (this is choosing model A, and the
   report should say so);
4. other methods (seismic reflection for structure, well logs for conductivity).

The correct practice is to report the family of models with acceptable misfit and
the resolution analysis, and to state which external information was used to
prefer one member.

---

## ★7 — Resolving layer 6 to a factor of two

**The obstacle, quantified.** The goal is $\delta m_6\lesssim\log_{10}2=0.301$.
With $\delta m=\sqrt{\chi^2}/s$, the required smallest singular value is
$s_{\min}\gtrsim0.769/0.301=2.56$, i.e. about $2.5$ times the current $1.04$.
Since the sensitivity of a sounding to a layer at depth $d$ grows roughly as the
diffusion length $\delta=\sqrt{2/(\omega\mu_0\sigma)}$ approaches $d$, the
frequency spectrum must be extended downward (longer periods) and the geometry
enlarged.

**Concrete specification.** For the host conductivity $0.02\ \mathrm{S\,m^{-1}}$
and a target depth of $360\ \mathrm{m}$, the skin depth must be comparable with the
depth. Solving $\delta=\sqrt{2/(2\pi f\mu_0\sigma)}$ for the frequency at
$\delta=300\ \mathrm{m}$:

$$f=\frac{2}{2\pi\mu_0\sigma\delta^2}
=\frac{2}{2\pi\times1.2566\times10^{-6}\times0.02\times9\times10^{4}}
=141\ \mathrm{Hz}.$$

So the band must extend *below* $\sim100\ \mathrm{Hz}$, where the current survey already starts, and the
long-period channels carry the new information. In practice: frequencies
$0.5$–$100\ \mathrm{Hz}$ (three decades below the current band), separations of
$100$–$400\ \mathrm{m}$ (so that the induction number stays in the resolved
range), and the same layered parametrisation *extended* in depth.

**Evidence of success.** The $s_{\min}$ of the new Jacobian exceeding $2.5$, with
the layer-6 kernel peak rising above about $0.3$ and its width falling below
$\sim100\ \mathrm{m}$ — the same diagnostics computed in the lesson, recomputed
for the new design.

**Cost.** Two things: a transmitter capable of long periods and long separations —
a physically larger and heavier system — and an insensitivity to source drift over
the longer integration times. The single-frequency, $40\ \mathrm{m}$ survey cannot
be pushed to this target by more iterations or a better algorithm: the information
is not in the data.

**Honest alternative.** If the target layer's conductivity is not resolvable within
the budget, report the *conductance* of the resolved part of the section and state
that deeper structure is not determined, rather than publishing a layer-6 value
that the roughness penalty placed there.

---

## ★8 — Why amplitude is absorbed and phase is not

**Mechanism.** In the low-induction regime the response is proportional to
$\omega\mu_0\sigma_{\text{eff}}r^2$ (Section 5.3 of
[08-05-01](../01-frequency-domain-em.md)); conductivity and an amplitude factor
enter the response *multiplicatively and identically*, so the inversion cannot
distinguish "a conductor $15\%$ more conductive" from "a system reading $15\%$
high". A change of conductivity also shifts the phase, but only through the
$\theta$-dependent part of the response, which is weak at small induction number:
so the amplitude factor is absorbed by a conductivity change with a near-perfect
fit. A frequency-independent *phase* rotation, by contrast, cannot be produced by
any conductivity distribution in the diffusive regime, where the phase of the
response varies with frequency in a prescribed way; a constant rotation is
therefore orthogonal to everything the model can do, and it appears as misfit.

**Prediction for $1+a\ln(f/f_0)$.** This factor is frequency dependent, so it is
neither purely absorbed nor purely visible: it has a shape that a
*conductivity-versus-depth* change can partly mimic (a graded conductivity profile
produces a slowly varying response), because a log-frequency dependence is exactly
the form that the diffusion-weighted sensitivity kernel can approximate by
smearing a conductivity change over depth. The prediction is therefore **both**:
part of it is absorbed into a spurious gradient in the upper few hundred metres,
and the remainder appears as a misfit that grows with the curvature of the factor
across the band. The diagnostic is to invert for a *calibration factor per
frequency* and inspect whether the recovered factor is smooth in $\ln f$ — if it
is, suspect a graded conductivity or a dimensional effect rather than
miscalibration.
