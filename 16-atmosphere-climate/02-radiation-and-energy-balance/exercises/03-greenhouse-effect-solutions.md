# Solutions — 16-02-03 The Greenhouse Effect: Physics, Not Rhetoric

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [03 The Greenhouse Effect](../03-greenhouse-effect.md).

---

## ★1 — The effective radiating temperature

$$F = \frac{S(1-a)}{4} = \frac{1361\times0.70}{4} = \frac{952.70}{4}
= 238.175\ \mathrm{W\,m^{-2}},$$

$$T_e = \left(\frac{238.175}{5.670374419\times10^{-8}}\right)^{1/4}
= (4.200357\times10^{9})^{1/4} = 254.578\ \mathrm{K} = -18.57\
\mathrm{^\circ C}.$$

**Why it is a model output.** It follows from the blackbody laws applied to an
albedo *that was chosen*, not measured here. Change the albedo to $0.60$ and $T_e$
becomes $221.34\ \mathrm{K}$ — a $13\%$ change from a parameter nobody measured.
An observation of outgoing radiation at the top of the atmosphere would give an
*actual* flux, which is a different (and better) quantity than this idealisation.

---

## ★2 — Downwelling infrared at a $290\ \mathrm{K}$ surface

$$\sigma T_s^4 = 5.670374419\times10^{-8}\times290^4
= 5.670374419\times10^{-8}\times7.07281\times10^{9}
= 401.055\ \mathrm{W\,m^{-2}},$$

$$D = 401.055 - 238.175 = 162.880\ \mathrm{W\,m^{-2}}, \qquad
\frac{\sigma T_s^4}{F} = \frac{401.055}{238.175} = 1.68387 .$$

So a surface at $290\ \mathrm{K}$ radiates $68\%$ more than the planet absorbs, and
the whole of the excess must come back from the sky as infrared.

---

## ★3 — The Planck response

$$\lambda_0 = 4\sigma T^3.$$

| $T$ (K) | $\lambda_0$ (W m⁻² K⁻¹) |
|---|---|
| 250 | 3.544 |
| 255 | 3.761 |
| 280 | 4.979 |
| 300 | 6.124 |

**One sentence:** each number converts an imposed radiative flux change
($\mathrm{W\,m^{-2}}$) into the temperature change ($\mathrm{K}$) of a blackbody in
radiative balance at that temperature, in the absence of all other feedbacks — so
it is a *reference sensitivity*, not a climate sensitivity.

---

## ★4 — No-feedback response to a forcing

$$\Delta T_0 = \frac{\Delta F}{4\sigma T_e^3}
= \frac{3.0}{3.7423} = 0.802\ \mathrm{K}.$$

**Left out:** every feedback. Water-vapour, lapse-rate, cloud, surface-albedo and
carbon-cycle responses all change the final temperature, in both directions; the
Planck response is included by construction and *only* it is. The number is
therefore a reference against which feedbacks are measured, not a prediction.

---

## ★5 — Surface budget and a one-parameter fit

**Derivation.** The surface receives $F$ (absorbed sunlight) and $D$ (downwelling
infrared) and loses $\sigma T_s^4$ by emission (and nothing by convection or
evaporation in this model). Steady state:

$$\sigma T_s^4 = F + D \qquad\Longrightarrow\qquad D = \sigma T_s^4 - F. \qquad\checkmark$$

**Fit.** With $T_s = 290\ \mathrm{K}$, $\sigma T_s^4 = 401.055\ \mathrm{W\,m^{-2}}$
and the one-layer result $\sigma T_s^4 = 2F/(2-\varepsilon)$:

$$\varepsilon = 2 - \frac{2F}{\sigma T_s^4}
= 2 - \frac{2\times238.175}{401.055} = 2 - 1.18774 = 0.81226 .$$

**Two sentences.** The fit shows that a single-layer model *can* be tuned to
reproduce a prescribed surface temperature, with a physically plausible emissivity.
It does **not** show that the real atmosphere behaves like one grey layer, because
the same tuning leaves the outgoing spectrum, its sensitivity to composition
change, and the vertical temperature structure unconstrained — and
[lesson 02](../02-radiative-transfer-atmosphere.md) measured the resulting
sensitivity error as a factor of about $2.4$.

---

## ★6 — Sensitivity, and the absence of saturation in the one-layer model

From $\sigma T_s^4 = 2F/(2-\varepsilon)$, take logarithms and differentiate:

$$4\ln T_s = \ln(2F/\sigma) - \ln(2-\varepsilon)
\;\Longrightarrow\;
\frac{4}{T_s}\frac{\mathrm{d}T_s}{\mathrm{d}\varepsilon}
= \frac{1}{2-\varepsilon},$$

$$\boxed{\;\frac{\mathrm{d}T_s}{\mathrm{d}\varepsilon}
= \frac{T_s}{4(2-\varepsilon)}\;}$$

| $\varepsilon$ | $T_s$ (K) | $\mathrm{d}T_s/\mathrm{d}\varepsilon$ (K) | fractional |
|---|---|---|---|
| 0.4 | 269.184 | 42.060 | 0.15625 |
| 0.9 | 295.618 | 67.186 | 0.22727 |

The fractional sensitivity is $1/[4(2-\varepsilon)]$, which *increases* with
$\varepsilon$: **the one-layer model does not saturate.** The reason is structural —
with one layer there is no partially transparent regime; the layer's transmittance
goes from $1$ to $0$ as $\varepsilon$ goes from $0$ to $1$, and the response is
monotone throughout.

**Where the real saturation comes from.** From the *line shapes*: a strong
absorption line saturates in its core, where adding absorber adds nothing, and
grows only in its wings, whose area scales as the square root of the amount
(§3.4 of the lesson measures the logarithmic slope of the absorption deficit moving
from $1.00$ to $0.54$ to $0.40$). A broadband emissivity is a single number and
therefore has no core and no wings: it cannot represent partial saturation, and
that is precisely why matching a grey model to a broadband flux leaves the
sensitivity wrong.

---

## ★7 — Regimes of a Lorentz line

For a Lorentz line the line-centre absorption coefficient is
$k_0 = k(\nu_0) = S/(\pi\alpha)$, and the optical depth at line centre for column
amount $W$ is $\tau_0 = k_0 W$.

**Linear regime** ($\tau_0 \ll 1$): $1-e^{-k W} \approx kW$ everywhere in the
line, so

$$D(W) \approx W\int k(\nu)B_\nu\,\mathrm{d}\nu \;\propto\; W ,
\qquad \frac{\mathrm{d}\ln D}{\mathrm{d}\ln W} = 1 .$$

**Square-root regime** ($\tau_0 \gg 1$): the core is black and contributes a
constant; only the wings contribute, and their integrated absorption grows as
$\sqrt{W}$:

$$D(W) \approx \text{const} + c\sqrt{W} .$$

With the model parameters given ($\alpha = 3.0\times10^{2}\ \mathrm{m^{-1}}$,
line-centre absorption coefficient $1.2$ per unit reference column), the
line-centre optical depth is $\tau_0 = 1.2\,W_{\text{ref}}$, so the transition is
at

$$W_{\text{trans}} \approx \frac{1}{\text{(line-centre coefficient)}}
= \frac{1}{1.2} = 0.83\ \text{reference columns}.$$

**Justification of the criterion.** The transition is where the line centre goes
from transmitting to absorbing, i.e. where $\tau_0 = O(1)$; that is the same
criterion that defines the visible depth in
[lesson 02 §2.2](../02-radiative-transfer-atmosphere.md). Below it the whole line
contributes proportionally to the amount; above it the core is saturated and only
the wings respond.

**Caveat to state.** The transition is *not* sharp, and the observed slope is an
average over the line profile weighted by the Planck function, so the measured
slope crosses $1/2$ rather than jumping to it — as the lesson's table shows
($0.9946$, $0.9515$, $0.7684$, $0.5420$, $0.3951$).

---

## ★8 — A single-layer planet with $F = 200\ \mathrm{W\,m^{-2}}$

**(a)** $T_e = (200/\sigma)^{1/4} = (3.527124\times10^{9})^{1/4} = 243.700\
\mathrm{K}$.

**(b)** $\sigma T_s^4 = 2F/(2-\varepsilon) = 400/1.4 = 285.714\
\mathrm{W\,m^{-2}}$, so

$$T_s = (285.714/\sigma)^{1/4} = (5.038748\times10^{9})^{1/4} = 266.428\
\mathrm{K}.$$

**(c)** $\sigma T_a^4 = F/(2-\varepsilon) = 200/1.4 = 142.857\
\mathrm{W\,m^{-2}}$, so $T_a = (142.857/\sigma)^{1/4} = 224.038\ \mathrm{K}$.

**(d)** The downwelling infrared at the surface is the layer's downward emission,
$\varepsilon\sigma T_a^4 = 0.6\times142.857 = 85.714\ \mathrm{W\,m^{-2}}$.

**Verifications.**

$$\text{surface: } \sigma T_s^4 = 285.714 = F + \varepsilon\sigma T_a^4
= 200 + 85.714 = 285.714 \;\checkmark$$

$$\text{TOA: } (1-\varepsilon)\sigma T_s^4 + \varepsilon\sigma T_a^4
= 0.4\times285.714 + 85.714 = 114.286 + 85.714 = 200.000 = F \;\checkmark$$

Both balances close exactly, which is what the two equations were solved for; the
check is on the algebra, not on the physics. Note the structure: the layer is at
$224.04\ \mathrm{K}$, *below* $T_e = 243.70\ \mathrm{K}$, and it is the sum of the
leaked surface radiation ($114.29\ \mathrm{W\,m^{-2}}$) and the layer's own upward
emission ($85.71\ \mathrm{W\,m^{-2}}$) that balances the absorbed sunlight.

---

## ★9 — Specification for a line-saturation experiment

1. **Model.** Lorentz lines, $k(\nu) = S\alpha/[\pi((\nu-\nu_0)^2+\alpha^2)]$, with
   $S$ and $\alpha$ stated in model units. Deficit
   $D(W) = \int[1-e^{-k(\nu)W}]B_\nu(T_s)\,\mathrm{d}\nu$, evaluated on a
   wavelength grid fine enough that halving the step changes $D$ by less than
   $10^{-4}$ relative (state the verified number).
2. **Scans.** $W$ over six decades and $\alpha$ over two decades, both
   logarithmically spaced, with $S$ rescaled so that $k_0 = S/(\pi\alpha)$ is held
   *fixed* across the $\alpha$ scan — otherwise the $\alpha$ scan changes the
   optical depth as well and confounds the two effects.
3. **Metric.** The local slope $p(W,\alpha) = \partial\ln D/\partial\ln W$,
   computed by a central difference in $\ln W$.
4. **Expected scaling.** $p \to 1$ for $\tau_0 = k_0 W \ll 1$ and $p \to 1/2$ for
   $\tau_0 \gg 1$. The transition occurs at $\tau_0 \approx 1$.
5. **The predicted product — the interesting part.** Because $D$ depends on $(S,
   \alpha, W)$ only through the combination $k_0 W$ *in the saturation criterion*
   but through $\alpha$ separately in the *wing* contribution, the two scans are
   **not** independent: rescaling $\alpha$ at fixed $k_0$ changes the total
   equivalent width of the line (a broader line absorbs more in its wings). The
   sharp prediction is that $p$ is a function of $\tau_0$ *alone*, i.e. the
   $\alpha$ scan must collapse onto the $W$ scan when plotted against $k_0W$.
   **A failure of that collapse** would mean (i) the numerical integration is
   under-resolved in the wings — the expected failure mode, since the wings are
   where the grid is coarsest in wavenumber — or (ii) the deficit is not being
   measured over a band wide enough to contain the wings, so the integral is
   truncated. Both are diagnosable: (i) improves with a finer grid and (ii) is
   cured by widening the band, and running those two controls is what makes the
   experiment decisive rather than merely suggestive.

---

## ★10 — Four more statements, classified

| statement | status | what would move it |
|---|---|---|
| The atmospheric window transmits some surface radiation directly to space | **modelled + measured**: window position is spectroscopic, the transmitted fraction is computed | already has measured inputs; to move fully to *measured*, a spectrally resolved outgoing radiance would be needed (which exists as a measurement but is not reproduced here) |
| Doubling a greenhouse gas raises the tropopause | **inferred**: requires a model of the stratosphere and of the convective adjustment | a *modelled* calculation in a radiative–convective or GCM framework; it becomes *measurable* in principle as a long-term tropopause-height record with stable sampling |
| The surface warms more at night than by day when greenhouse gases increase | **inferred and conditional**: depends on boundary-layer and cloud behaviour | a *modelled* diurnal-cycle study; measurable with a homogenised surface network with adequate night-time sampling |
| Downwelling infrared increases as a greenhouse gas increases | **measured in principle** (a pyrgeometer plus a composition measurement), **modelled** if the composition is only assumed | an actual paired time series of both quantities; the confounders are cloud and water-vapour variability, not the instrument |

**The statement that cannot leave the *inferred* column.** "The greenhouse effect
is responsible for keeping the surface $X$ kelvin warmer than it would otherwise
be." The reason is *not* instrumental and not computational: it requires a
counterfactual — a world with the composition changed and everything else,
including the albedo and the cloud field, held fixed. No observation of the actual
Earth contains that counterfactual, and any attempt to construct it necessarily
uses a model that assumes the answer at some level. The number $X$ can be
*computed*, and it can be *bounded*, but it cannot be observed.

---

## ★11 — Critiquing "it saturates, so it cannot warm further"

Four distinct errors, of three different kinds:

1. **"Saturates" conflated between two different quantities.** The *per-molecule
   forcing* declines as the amount already present grows (a statement about the
   scaling of the absorption deficit, §3.4 — this is where the word is correct).
   The *temperature response to a given forcing* does not saturate at all in this
   model (it is $1/[4\sigma T^3]$, §3.3). The sentence silently substitutes the
   second for the first. **Physics/algebra.**
2. **A declining marginal effect treated as a vanishing one.** The measured
   logarithmic slopes are $1.00$, $0.95$, $0.77$, $0.54$ and $0.40$ — always
   positive. A positive derivative is a warming, however small. **Algebra.**
3. **The word "so" assumed to run in one direction only.** Even with a saturated
   forcing, the temperature response *per unit forcing* is not constant once
   feedbacks are included, and feedback strengths change with temperature.
   **Scaling of the forcing — not derivable in this lesson.**
4. **A single gas treated as the whole composition.** Adding one absorber changes
   temperature, which changes water vapour (Clausius–Clapeyron), which changes the
   absorption. The "saturated" gas is embedded in a system whose other components
   are not saturated. **Requires material from
   [16-04-02](../../04-climate-system-and-feedbacks/02-climate-feedbacks.md).**

**Strongest defensible version of the intended statement.**

> For an absorption band that is already optically thick at its line centres, the
> marginal radiative forcing per unit of added absorber declines with the amount
> already present, approaching a dependence closer to logarithmic than linear
> because the absorption grows only in the line wings. The effect therefore
> diminishes, but its derivative with respect to absorber amount remains positive
> wherever the band is not entirely black across the whole spectrum, and the
> temperature change per unit forcing is governed by feedbacks that this
> statement does not address.

The first clause is this lesson's §3.4; the second is this lesson's §3.3; the third
requires another module, and the sentence says so.

---

## ★12 — A spectral falsification test for the mechanism

**What the mechanism predicts that a bare energy-balance fit does not.** The
emission-level picture predicts a *specific spectral signature*: the outgoing
radiance should show absorption features whose depth corresponds to emission from
atmospheric layers at the temperatures those layers have, so that

- the *depth* of a strong band corresponds to the temperature of the layer around
  $\tau \approx 1$ in that band, not the surface temperature;
- two bands with different opacities therefore originate from *different heights*
  and therefore show *different brightness temperatures* in the same atmosphere.

A single-layer energy-balance fit that reproduces the broadband flux predicts no
such ordering: it has one temperature and one emissivity, so all bands share a
brightness temperature.

**The test.** With one spectrometer measuring the outgoing spectrum:

1. Identify (from the spectrum's own structure, without external spectroscopy) a
   set of channels spanning a range of apparent optical depth, from a window
   channel to a strongly absorbing channel.
2. Retrieve the brightness temperature in each.
3. Test the prediction that brightness temperature **decreases** monotonically from
   the window channel toward the most opaque channel, and that the decrease is
   consistent with the vertical temperature profile measured independently by,
   say, radiosondes.

**Why it must be spectral.** A broadband instrument sees the integral of this
structure, and any single-layer model can be tuned to reproduce that integral —
that is §3.2 of the lesson. The *ordering* across channels is not a single number
and cannot be reproduced by a one-parameter fit: it is a prediction of the
mechanism, and it is falsifiable. A demonstration that all channels shared the same
brightness temperature would contradict the emission-level picture while remaining
entirely compatible with a broadband energy-balance fit — which is exactly what
makes the spectral test informative.
