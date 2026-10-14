# Solutions — 11-02-04 EM for Conductors, Massive Sulphides and Graphite

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All resistivities, sizes and conductances are **SYNTHETIC**.

Lesson: [04 EM for Minerals](../04-em-for-minerals.md).

---

## ★1 — Skin depths

$$\delta = \sqrt{\frac{2}{\omega\mu_0\sigma}}.$$

Body, $\rho = 2\ \Omega\,\mathrm{m}$ ($\sigma = 0.5\ \mathrm{S\,m^{-1}}$):
at $50\ \mathrm{Hz}$, $\omega\mu_0\sigma = 314.159(1.25664\times10^{-6})(0.5)
= 1.9739\times10^{-4}$, so $\delta = \sqrt{1.0132\times10^{4}} = 100.7\
\mathrm{m}$. At $500\ \mathrm{Hz}$: $\delta = 100.7/\sqrt{10} = 31.8\ \mathrm{m}$.

Host, $\rho = 400\ \Omega\,\mathrm{m}$ ($\sigma = 2.5\times10^{-3}$): at $50\
\mathrm{Hz}$, $\delta = 100.7\times\sqrt{200} = 1424.0\ \mathrm{m}$; at $500\
\mathrm{Hz}$, $\delta = 450.3\ \mathrm{m}$.

**Ratio host : body** $= \sqrt{400/2} = \sqrt{200} = 14.1$ at every frequency,
because $\delta \propto \sqrt{\rho}$. The frequency cancels in the ratio, which is
why the *contrast* controls whether a conductor stands out, and the *frequency*
controls at what depth you look.

---

## ★2 — Time constant and corner frequency

$$\tau = \frac{\mu_0\sigma a^{2}}{\pi^{2}}
= \frac{(1.25664\times10^{-6})(1/1.5)(80)^{2}}{\pi^{2}}
= \frac{5.3617\times10^{-3}}{9.8696} = 5.4325\times10^{-4}\ \mathrm{s}
= 0.543\ \mathrm{ms}.$$

$$\omega\tau = 1 \;\Longrightarrow\; f = \frac{1}{2\pi\tau}
= \frac{1}{2\pi(5.4325\times10^{-4})} = 292.9\ \mathrm{Hz}.$$

Below this frequency the induction response grows as $\omega\tau$; above it the
response saturates at 1 while the host attenuation keeps growing as $e^{-2z/\delta}$,
so there is an optimum, and it sits near the corner.

---

## ★3 — Conductance

$$S = \sigma t = (4)(15) = 60\ \mathrm{S}.$$

A $3\ \mathrm{m}$ sheet with the same response needs
$\sigma = 60/3 = 20\ \mathrm{S\,m^{-1}}$, i.e. **five times** the conductivity for
one fifth of the thickness. In general $\sigma_{2} = \sigma_{1}t_{1}/t_{2}$: the
exchange rate is exactly inverse in thickness, so a factor of $100$ in thickness is
a factor of $100$ in the conductivity required — and real rocks span about
$10^{-5}$ to $10^{5}\ \Omega\,\mathrm{m}$, which is wide enough that the degeneracy
is nearly always live.

---

## ★4 — Screening factor

$$1 + \frac{\mu_0\omega Sz}{2}
= 1 + \frac{(1.25664\times10^{-6})(2\pi)(200)(8)(150)}{2}.$$

$\mu_0\omega = 1.25664\times10^{-6}(1256.64) = 1.5791\times10^{-3}$; times
$S z/2 = 8(150)/2 = 600$ gives $0.9475$. So

$$\text{screen} = 1.95 .$$

The target response is roughly halved. Note the linearity in $S$, $f$ and $z$:
doubling any one of them nearly doubles the screening, which is why deep targets
under conductive cover are the hardest EM problem in the method.

---

## ★5 — The radius–conductivity trade-off

$$\sigma = \frac{\pi^{2}\tau}{\mu_0 a^{2}}
= \frac{9.8696(2.5\times10^{-3})}{(1.25664\times10^{-6})a^{2}}
= \frac{1.9635\times10^{4}}{a^{2}}\ \mathrm{S\,m^{-1}}.$$

| $a$ (m) | $\sigma$ (S m⁻¹) | $\rho$ (Ω m) |
|---|---|---|
| 70 | 4.0072 | 0.250 |
| 100 | 1.9635 | 0.509 |
| 140 | 1.0018 | 0.998 |

**The inferred conductivity changes by a factor of $4$** (0.25 → 1.00 Ω m) across
a factor of two in radius, exactly as $\rho \propto a^{2}$. A decay curve gives
$\tau$; a conductivity requires a size, and the size is usually the least-known
parameter in the model. The defensible report is $\sigma a^{2} = \pi^{2}\tau/\mu_0
= 1.9635\times10^{4}\ \mathrm{m^{2}\,s^{-1}}$ — a quantity with no size assumption
in it, from which a reader can compute a conductivity for whatever size they
prefer.

---

## ★6 — What a short window actually measures

From the lesson's table, a quarter-decade window ($0.92$–$1.63\ \mathrm{ms}$)
yields a fitted time constant of $0.496\ \mathrm{ms}$ for the host's power law,
while the target's true $\tau$ is $1.833\ \mathrm{ms}$.

**The specific error:** over a quarter-decade window an exponential fits a
power-law decay to $3\%$, so the fit is *statistically excellent*, and the fitted
$\tau$ is $27\%$ of the target's. Reporting it as "the target's time constant"
therefore reports a number that is neither the target's nor the host's, with no
diagnostic that anything is wrong — the fit residual looks like noise. The
quantified lesson is that a time constant is only interpretable together with
(a) the window it was fitted over and (b) evidence that the decay is exponential
rather than a power law, which requires at least a decade of clean decay.

---

## ★7 — Frequency choice without an overburden

$$a = 100\ \mathrm{m},\ z = 200\ \mathrm{m},\ \rho_t = 1\ \Omega\,\mathrm{m},\
\rho_{\text{host}} = 200\ \Omega\,\mathrm{m},\ S = 0 .$$

$\tau = \mu_0\sigma a^{2}/\pi^{2} = 1.25664\times10^{-6}(1)(10^{4})/9.8696
= 1.2732\times10^{-3}\ \mathrm{s}$, corner $1/(2\pi\tau) = 125.1\ \mathrm{Hz}$.

| $f$ (Hz) | $\delta_{\text{host}}$ (m) | $e^{-2z/\delta}$ | $\omega\tau/\sqrt{1+(\omega\tau)^{2}}$ | index |
|---|---|---|---|---|
| 100 | 711.8 | 0.5702 | 0.6247 | **0.044515** |
| 1000 | 225.1 | 0.1691 | 0.9923 | 0.020977 |

**$100\ \mathrm{Hz}$ wins by a factor of 2.1**, even though its induction term is
smaller, because the host attenuation at $1000\ \mathrm{Hz}$ costs a factor of
$3.4$. The optimum sits near the target's corner frequency, where the induction
term has nearly saturated before the attenuation has become severe.

---

## ★8 — The same choice under a conductive overburden

With $S = 15\ \mathrm{S}$:

| $f$ (Hz) | screen $1+\mu_0\omega Sz/2$ | index |
|---|---|---|
| 100 | 2.184 | 0.020379 |
| 1000 | 12.844 | 0.001633 |

**The ranking does not change** — $100\ \mathrm{Hz}$ still wins, now by a factor of
12.5 — but the *reason* has changed: at $1000\ \mathrm{Hz}$ the screen alone costs
a factor of 12.8.

**The competition in one sentence:** higher frequency strengthens the target's
induction response toward saturation while shrinking the host skin depth and
raising the overburden screen, so the optimum frequency is where the marginal gain
in induction equals the marginal loss to attenuation and screening — a property of
the target *and* its cover together.

---

## ★9 — Measuring $\sigma$ and $t$ separately

**(a) Physical principle.** The conductance degeneracy holds only when the induced
current crosses the body in a *single* mode whose geometry is fixed by the receiver
coupling. It breaks when the measurement resolves the current *distribution*
inside the body, which requires either a frequency/delay short enough that the
internal diffusion is incomplete (so the response depends on the internal geometry,
not only on $\sigma t$), or a receiver placement that samples different parts of the
return current.

**(b) Geometry.** Three options, in increasing cost: (i) a **multi-offset,
multi-component** ground system at two widely separated delays; (ii) a
**borehole** (downhole EM) survey with the transmitter on the surface and the
receiver inside or beneath the conductor, which samples the internal field
directly; (iii) **surface-to-surface separated loops** with the receiver over the
body and a distant, small transmitter, giving a *current-channeling* response that
depends on $\sigma$ rather than on $S$.

**(c) Quantity to fit.** The ratio of responses at two widely separated delays
where the target's internal diffusion is *not* complete — equivalently, the
*departure from a single exponential* in the early-time part of the decay.

**(d) Precision.** The separation scales as the ratio of the internal diffusion
time across the thickness, $\tau_t \approx \mu_0\sigma t^{2}/\pi^{2}$, to the
body's overall $\tau = \mu_0\sigma a^{2}/\pi^{2}$: their ratio is $(t/a)^{2}$.
Resolving $t$ to $20\%$ therefore needs the early-time deviation measured to about
$0.04$ of the total response, i.e. an amplitude precision of a few per cent with
sub-microsecond sampling — feasible in a borehole, rarely feasible from the air.

**Conclusion:** for an airborne conductor, the honest output is the conductance
and the time constant, never a conductivity; a downhole measurement is the
cheapest route to the missing thickness.

---

## ★10 — The thin-sheet time constant by dimensional analysis

**Why the sphere result does not transfer.** For a compact body the diffusivity is
$D = 1/(\mu_0\sigma)$ with units $\mathrm{m^{2}\,s^{-1}}$, so
$\tau \sim a^{2}/D = \mu_0\sigma a^{2}$ times an eigenvalue constant. For a *thin
sheet* the current is confined to the sheet and the relevant (areal) current is
driven by the sheet's conductance; the combination that plays the role of a
diffusivity is $1/(\mu_0 S)$, whose units are

$$\left[\mu_0 S\right] = \frac{\mathrm{H\,m^{-1}}\cdot\mathrm{S}}{1}
= \frac{\mathrm{s}}{\mathrm{m}},
\qquad
\left[\frac{1}{\mu_0 S}\right] = \mathrm{m\,s^{-1}} ,$$

a **velocity**, not a diffusivity. The only time that can be built from a length
$L$ and this velocity is

$$\tau = c\,\mu_0 S L ,$$

with $c$ a dimensionless constant fixed by the sheet's *shape* and by the
eigenvalue of the corresponding boundary-value problem — not by its conductivity.

**Numerical procedure to find $c$.** Solve the thin-sheet diffusion equation for
the sheet's magnetic field with zero field on the sheet's edge (for a disk of
radius $L$: $\partial B/\partial t = (1/(\mu_0 S))\,\nabla^{2}_{\text{sheet}}
(\cdot)$ in the appropriate gauge), initialise with the primary field, and measure
the late-time decay rate; $c = 1/(\text{measured rate}\times\mu_0 S L)$. Repeat for
a square and a rectangle to show that $c$ is shape-dependent.

**Why this matters.** $\tau \propto S L$ means a *large, moderately conducting*
sheet and a *small, highly conducting* one can share a time constant through a
*different* trade-off than the sphere's $\sigma a^{2}$ — and now even a perfectly
known $\tau$ provides no size–conductivity separation, because the size appears
linearly and the conductance linearly, with a shape coefficient in between.

---

## ★11 — Two conductors in one footprint

**Composite decay.** Take two compact bodies with
$\tau_1 = 1.8\ \mathrm{ms}$ and $\tau_2 = 8.0\ \mathrm{ms}$ contributing
amplitudes $0.6$ and $0.4$ (SYNTHETIC), so

$$V(t) = 0.6e^{-t/1.8\,\mathrm{ms}} + 0.4e^{-t/8.0\,\mathrm{ms}} .$$

Fitting a single exponential $Ae^{-t/\tau}$ by least squares over
$0.5$–$20\ \mathrm{ms}$ gives

$$\tau_{\text{fit}} = 6.62\ \mathrm{ms}, \qquad
\text{relative rms misfit} = 11.2\% .$$

**Why this is dangerous.** The fitted value lies between the two true constants and
is closer to the *longer* one because that is what the fit optimises over the
window; the misfit is only $11\%$, which is the size of the levelling and
geological noise in a real survey. An interpreter would report a single body with
$\tau = 6.6\ \mathrm{ms}$ — which, via $\sigma \propto 1/a^{2}$, is a perfectly
plausible conductivity for a plausible size — and would have no way to know that
two bodies are present.

**Measurement that reveals the second body.** Two candidates, in order of cost:
(i) an **early-time window** where the two exponentials are clearly separated (at
$t = 1\ \mathrm{ms}$ the amplitudes are $0.35$ and $0.35$, i.e. the decay has a
kink); (ii) a **profile** across the anomaly: the two bodies are $120\ \mathrm{m}$
apart, so a moving-loop profile shows a bimodal or flattened anomaly, whereas a
single body gives a single peak. The diagnostic is the *spatial* first
derivative, not the temporal one — which is why a single sounding, however
precise, cannot substitute for a profile.
