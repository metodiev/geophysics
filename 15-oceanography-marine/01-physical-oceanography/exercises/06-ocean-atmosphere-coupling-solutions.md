# Solutions — 15-01-06 Ocean-Atmosphere Coupling and ENSO

> **Read after attempting the exercises.** Where more than one answer is
> defensible it is said so. All arithmetic was computed.

Lesson: [06 Ocean-Atmosphere Coupling](../06-ocean-atmosphere-coupling.md).

---

## ★1 — The three bulk fluxes

$$\tau = \rho_{\text{air}}C_D|U|U
= 1.225 \times 1.2\times10^{-3} \times 4.0 \times 4.0
= 2.352\times10^{-2}\ \mathrm{N\,m^{-2}},$$

$$H = \rho_{\text{air}}c_pC_H|U|(T_s-T_a)
= 1.225 \times 1005 \times 1.1\times10^{-3} \times 4.0 \times(-2.0)
= -10.834\ \mathrm{W\,m^{-2}},$$

$$LE = \rho_{\text{air}}L_vC_E|U|(q_s-q_a)
= 1.225 \times 2.501\times10^{6} \times 1.2\times10^{-3} \times 4.0
\times(-4.0\times10^{-3}) = -58.82\ \mathrm{W\,m^{-2}}.$$

Dimensional checks: $\mathrm{(kg\,m^{-3})(m\,s^{-1})^{2}} = \mathrm{kg\,m^{-1}\,s^{-2}}
= \mathrm{N\,m^{-2}}$ ✔; $\mathrm{(kg\,m^{-3})(J\,kg^{-1}\,K^{-1})(m\,s^{-1})(K)}
= \mathrm{J\,m^{-2}\,s^{-1}} = \mathrm{W\,m^{-2}}$ ✔. The negative signs mean the
ocean is losing heat and water to the atmosphere, which is the convention when
$T_s - T_a < 0$ and $q_s - q_a < 0$.

---

## ★2 — Quadratic against linear in wind speed

**Quadratic:** $\tau = \rho_{\text{air}}C_D|\mathbf{U}|\mathbf{U}$. **Linear:**
$H$ and $LE$ (each contains $|U|$ to the first power).

For a power law $y \propto U^{n}$, a fractional error $\delta U/U$ propagates as
$\delta y/y \approx n\,\delta U/U$ to first order. Hence:

$$\frac{\delta\tau}{\tau} \approx 2\frac{\delta U}{U}, \qquad
\frac{\delta H}{H} \approx \frac{\delta U}{U}, \qquad
\frac{\delta LE}{LE} \approx \frac{\delta U}{U}.$$

A $5\,\%$ wind error is therefore a $10\,\%$ **stress** error but only a $5\,\%$
heat-flux error. This asymmetry matters because stress drives the circulation
(Sverdrup balance, Ekman transport) while the heat fluxes drive the buoyancy —
the two halves of the problem do not inherit wind error equally.

---

## ★3 — The model

$$\frac{\mathrm{d}T}{\mathrm{d}t} = R\,T + \gamma\,h + \xi(t),
\qquad
\frac{\mathrm{d}h}{\mathrm{d}t} = -\epsilon\,T - r\,h .$$

| symbol | meaning |
|---|---|
| $R$ | Bjerknes feedback: a warm SST anomaly strengthens the winds that warm it further |
| $\gamma$ | thermocline-depth effect on SST: a deeper thermocline warms the eastern surface |
| $\epsilon$ | discharge: a warm anomaly drives a thermocline response that removes it |
| $r$ | damping of the thermocline-depth anomaly |
| $\xi$ | white noise standing in for unrepresented weather |

$T$ is an SST anomaly (K or $^\circ$C); $h$ is a thermocline-depth anomaly (m).

---

## ★★4 — Eigenvalues for $R = 0.8$, $r = 0.6$

$$\operatorname{tr}A = R - r = 0.8 - 0.6 = +0.200\ \mathrm{yr^{-1}},
\qquad
\det A = \gamma\epsilon - Rr = 2.9 - 0.48 = 2.420\ \mathrm{yr^{-2}},$$

$$\lambda = \frac{0.200 \pm \sqrt{0.0400 - 4(2.420)}}{2}
= \frac{0.200 \pm \sqrt{-9.640}}{2}
= \frac{0.200 \pm 3.1048\,\mathrm{i}}{2}$$

$$= +0.100 \pm 1.5524\,\mathrm{i}\ \mathrm{yr^{-1}} .$$

Period: $2\pi/1.5524 = 4.047$ yr. Growth rate: $+0.100\ \mathrm{yr^{-1}}$, so the
$e$-folding time is $1/0.100 = 10.0$ yr. The mode **grows** (positive real part)
**and oscillates** (nonzero imaginary part) — an unstable, growing oscillation.
In this regime the linear model is being used outside its regime of validity;
a real system would saturate.

---

## ★★5 — The critical coupling

The eigenvalues are $\lambda = (\operatorname{tr} \pm \sqrt{\operatorname{tr}^{2}
- 4\det})/2$, which form a complex pair when the discriminant is negative:
$\operatorname{tr}^{2} < 4\det$. The transition to two real eigenvalues occurs at

$$\operatorname{tr}^{2} = 4\det
\;\Longrightarrow\;
(R-r)^{2} = 4(\gamma\epsilon - Rr)
\;\Longrightarrow\;
\boxed{\gamma\epsilon = Rr + \frac{(R-r)^{2}}{4} .}$$

Expanding for $r = 0.8$, $\gamma = 1.0$, $\epsilon = 2.7174$:

$$2.7174 = 0.8R + \frac{(R-0.8)^{2}}{4}
= 0.8R + 0.25R^{2} - 0.4R + 0.16
= 0.25R^{2} + 0.4R + 0.16,$$

$$0.25R^{2} + 0.4R - 2.5574 = 0
\;\Longrightarrow\; R^{2} + 1.6R - 10.2296 = 0,$$

$$R = \frac{-1.6 \pm \sqrt{2.56 + 40.9184}}{2}
= \frac{-1.6 \pm \sqrt{43.4784}}{2} = \frac{-1.6 \pm 6.5938}{2},$$

taking the positive root: $R = 2.497\ \mathrm{yr^{-1}}$.

**Comparison.** For $r = 0.5$ the lesson found $R = 2.797$; for $r = 0.8$ we get
$2.497$. Increasing the damping of the thermocline reduces the coupling strength
needed to destroy the oscillation, because $r$ appears on the right-hand side of
the critical condition. Physically: stronger damping of $h$ makes the recharge
less able to store the anomaly, so the oscillation dies at weaker Bjerknes
feedback.

---

## ★★6 — Two models, one period, two thermocline responses

**(a)** $5.4348/2.1266 = 2.556$ — the neutral case's steady thermocline response
is **2.6 times larger** than the damped case's, for the same period.

**(b)** The period depends on $\omega_0^{2} = \gamma\epsilon - Rr
- (R-r)^{2}/4$, i.e. on a *combination* of $\epsilon$, $R$ and $r$; the steady
ratio depends on $\epsilon/r$ alone. Two parameter sets can therefore match by
trading $\epsilon$ against $r$ while keeping the combination in the period fixed —
and the neutral case does exactly that, with $\epsilon = 2.7174$, $r = 0.5$,
$R = 0.5$ against the damped case's $\epsilon = 3.1899$, $r = 1.5$,
$R = 0.2$. This is a **degeneracy**: the oscillation period does not determine the
response amplitude, and a dataset that measures only the period cannot break it.
An independent estimate of $\epsilon/r$ — from the observed relation between
thermocline depth and SST anomalies — is what would.

---

## ★★7 — Changing $R$ against changing $r$

Baseline: $R = 0.5$, $r = 0.5$, $\gamma = 1.0$, $\epsilon = 2.7174$;
$\operatorname{tr} = 0$, $\det = 2.7174 - 0.25 = 2.4674$,
$\lambda = \pm1.5708\mathrm{i}$ (period 4.000 yr, no growth).

**(a) Doubling $R$ to $1.0$** (with $r = 0.5$):

$$\operatorname{tr} = 0.5, \quad \det = 2.7174 - 0.5 = 2.2174,$$
$$\lambda = 0.25 \pm \frac{\sqrt{0.25 - 8.8696}}{2}
= 0.25 \pm 1.4680\,\mathrm{i}\ \mathrm{yr^{-1}},$$

period $2\pi/1.4680 = 4.280$ yr, growth $+0.250\ \mathrm{yr^{-1}}$
($e$-folding 4.0 yr). This matches the demonstration's $R = 1.0$ row exactly.

**(b) Halving $r$ to $0.25$** (with $R = 0.5$):

$$\operatorname{tr} = 0.25, \quad \det = 2.7174 - 0.125 = 2.5924,$$
$$\lambda = 0.125 \pm 1.6052\,\mathrm{i}\ \mathrm{yr^{-1}},$$

period $2\pi/1.6052 = 3.914$ yr, growth $+0.125\ \mathrm{yr^{-1}}$
($e$-folding 8.0 yr).

**Which changes the period more?** Doubling $R$ lengthens the period by
$+7.0\,\%$ (4.000 → 4.280); halving $r$ shortens it by $-2.2\,\%$
(4.000 → 3.914). **$R$ moves the period about three times as much per unit
fractional change** under these parameters, and — importantly — the growth rate
is exactly $(R-r)/2$ in both cases, so an observed growth rate constrains only the
*difference* $R - r$, never either one alone.

---

## ★★★8 — Damped oscillator against self-sustained oscillation

**The statistic.** The discriminating feature is **phase coherence across
successive cycles**. A self-sustained (limit-cycle) oscillation has a well-defined
amplitude and a phase that diffuses only slowly; a noise-driven damped oscillator
has an amplitude that fluctuates and a phase that decorrelates on the damping
timescale. Practical estimators: (i) the width of the spectral peak relative to
its centre, expressed as a quality factor $Q$; (ii) the lag at which the
autocorrelation envelope falls to $1/e$; (iii) the ratio of the amplitude's
standard deviation to its mean over independent segments.

**Record length.** The test needs many *independent* cycles: for a 4-year period,
at least $20$ cycles, i.e. **80 years**, to distinguish $Q \approx 1$ from
$Q \gg 1$ at useful confidence. Longer is better; the demonstration's own scatter
of $\pm11\,\%$ in the peak period from 100-year segments shows that a single
segment is nowhere near enough.

**Discriminating feature.** For a damped oscillator driven by white noise, the
peak width and the amplitude scatter are both set by the same damping rate, and
the *product* $Q^{-1}\times$(relative amplitude scatter) is fixed by the model.
For a self-sustained oscillator, $Q$ is large and the amplitude scatter is small —
the two statistics move together in a way the damped case cannot produce. The test
is therefore a joint test on two statistics, not a single threshold.

**The assumption it relies on.** That the forcing is white (or at least broad
compared with the resonance). If the atmosphere's noise has its own peak near the
oscillator's frequency, the measured $Q$ is inflated and the test loses its power —
this is exactly the ambiguity that makes the real ENSO system's dynamics a
long-running debate.

**What the demonstration's diagnostics can and cannot separate.** They **can**
reject the neutral, undamped linear model outright, because its response variance
is unbounded (Section 6.2 of the lesson: standard deviation growing from
$8.3\times10^{3}$ to $2.6\times10^{16}$ as the record lengthens). They **cannot**
distinguish a decay rate of $0.65\ \mathrm{yr^{-1}}$ from $0.3$ or $1.0$: the
response is broad ($Q = 1.21$) and the eight-segment peak scatter
($\pm11\,\%$) is far larger than the effect of such a change on the peak period
($\sim1.5\,\%$). And they **can** show that a linear model cannot reproduce
skewness — a rejection, not a confirmation.

---

## ★★★9 — Noise on both equations

Write the system as $\dot{\mathbf{x}} = A\mathbf{x} + B\boldsymbol{\xi}$ with
$\mathbf{x} = (T,h)^{\mathsf{T}}$, $\boldsymbol{\xi}$ a two-vector of independent
unit white noises, and $B = \operatorname{diag}(s_T, s_h)$ the two noise
amplitudes. The **transfer matrix** is
$H(\omega) = (\mathrm{i}\omega I - A)^{-1}B$, so the spectral matrix is

$$S(\omega) = \left(\mathrm{i}\omega I - A\right)^{-1} B B^{\mathsf{T}}
\left(\mathrm{i}\omega I - A\right)^{-\dagger},$$

and the spectrum of $T$ is the $(1,1)$ element:

$$S_{TT}(\omega) = \frac{s_T^{2}\,|\mathrm{i}\omega + r|^{2}
+ s_h^{2}\,\gamma^{2}}{\left|(\mathrm{i}\omega - R)(\mathrm{i}\omega + r)
+ \gamma\epsilon\right|^{2}} .$$

**What changes.** The **denominator is unchanged** — it is the characteristic
polynomial of $A$, so the *poles* of the response, and therefore the
eigenfrequencies, are identical whether or not the second equation is forced. That
is the precise sense in which "the eigenfrequencies are properties of the
deterministic system".

**What changes is the numerator**, and hence the shape of the spectrum. The new
term $s_h^{2}\gamma^{2}$ is *constant* in $\omega$, so it adds a white background
to the spectrum while the original term $s_T^{2}(\omega^{2}+r^{2})$ grows with
frequency as $\omega^{2}$. The practical consequences are that the peak becomes
**broader and lower**, and its position **shifts slightly upward in frequency**,
because the numerator now rises more slowly relative to the peaked denominator. If
the two noise sources were correlated — physically likely, since a single weather
system drives both — a cross term would appear and could shift the peak in either
direction. Recognising that the poles are robust while the peak is not is the
useful distinction: **the eigenfrequency is a property of the model, the spectral
peak is a property of the model AND its forcing.**
