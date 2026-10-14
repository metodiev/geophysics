# Solutions — 16-02-02 Radiative Transfer in the Atmosphere

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [02 Radiative Transfer](../02-radiative-transfer-atmosphere.md).

---

## ★1 — Transmittance and emissivity

$$T = e^{-\tau}, \qquad \varepsilon = 1-e^{-\tau}.$$

| $\tau$ | $T$ | $\varepsilon$ | regime |
|---|---|---|---|
| 0.2 | 0.818731 | 0.181269 | optically thin |
| 0.7 | 0.496585 | 0.503415 | transitional |
| 3.0 | 0.049787 | 0.950213 | optically thick |

**Why the distinction is not just a factor in $\tau$.** The quantities are
*exponentials*: $\varepsilon$ saturates at 1 while $T$ decays to 0, and the
information about $\tau$ is carried by $T$, which changes by a factor of $16.4$
between $\tau = 0.2$ and $3.0$ while $\varepsilon$ changes by only a factor $5.2$.
Beyond $\tau \approx 3$ the medium is essentially opaque and the *sensitivity* to
further opacity is negligible — the saturation that dominates the physics of the
lesson.

---

## ★2 — Single grey layer versus emissivity

$$T_e = \left(\frac{238.175}{5.670374419\times10^{-8}}\right)^{1/4}
= 254.578\ \mathrm{K}, \qquad
T_s = \left(\frac{2F}{\sigma(2-\varepsilon)}\right)^{1/4}.$$

| $\varepsilon$ | $T_s$ (K) | $T_s - T_e$ (K) |
|---|---|---|
| 0.1 | 257.864 | 3.286 |
| 0.4 | 269.184 | 14.606 |
| 0.8 | 289.257 | 34.679 |
| 1.0 | 302.746 | 48.168 |

Note the increments: $\Delta T_s$ grows by $11.3\ \mathrm{K}$ from
$\varepsilon = 0.1 \to 0.4$ ($\Delta\varepsilon = 0.3$), by $20.1\ \mathrm{K}$ from
$0.4 \to 0.8$, and by $13.5\ \mathrm{K}$ from $0.8 \to 1.0$
($\Delta\varepsilon = 0.2$). The response per unit emissivity is *largest in the
middle* of the range and smallest at both ends — the signature of a saturating
function.

---

## ★3 — Where the optical depth reaches unity

$$\tau(z) = \tau_s e^{-z/H_\tau}
\;\Longrightarrow\;
z = H_\tau\ln\frac{\tau_s}{\tau(z)}.$$

With $\tau_s = 4$ and $H_\tau = 1.5\ \mathrm{km}$:

$$z(\tau = 1) = 1.5\ln 4 = 1.5\times1.386294 = 2.079\ \mathrm{km},$$

$$z(\tau = 0.1) = 1.5\ln 40 = 1.5\times3.688879 = 5.533\ \mathrm{km}.$$

So the "optically thick" part of this atmosphere is the lowest $2.1\ \mathrm{km}$
and the radiation that escapes comes from a layer several kilometres deep, with
the last interaction typically near $2\ \mathrm{km}$. Note the **logarithmic**
dependence: to raise the $\tau = 1$ level by a factor of two in height you need to
square the total optical depth.

---

## ★4 — The $(N+1)^{1/4}$ law

$$T_s = (N+1)^{1/4}\times254.578\ \mathrm{K}.$$

| $N$ | $T_s$ (K) |
|---|---|
| 1 | 302.746 |
| 4 | 380.683 |
| 20 | 544.974 |

**Why these must not be quoted as predictions.** The premise is that each layer is
opaque at *every* wavelength, so the model has infinite total optical depth for any
$N$; increasing $N$ also changes the total opacity rather than adding absorber to a
fixed atmosphere; and no convection removes the heat. A surface at $545\
\mathrm{K}$ ($272\ \mathrm{^\circ C}$) is a statement about an idealisation, not
about the Earth. What the law *does* establish is that the surface temperature is
not the planetary radiating temperature and that the offset grows with the number
of opaque layers between them.

---

## ★5 — Schwarzschild and its formal solution

$$\frac{\mathrm{d}I_\nu}{\mathrm{d}\tau} = I_\nu - B_\nu(T),$$

using $\mathrm{d}\tau = -\kappa_\nu\rho\,\mathrm{d}s$ with $\tau$ measured downward
from the top. This is a first-order linear ODE with integrating factor
$e^{-\tau}$:

$$\frac{\mathrm{d}}{\mathrm{d}\tau}\left(I_\nu e^{-\tau}\right) = -B_\nu e^{-\tau}.$$

Integrating from the top ($\tau = 0$, where $I_\nu^\uparrow = I_\nu^\uparrow(0)$)
down to the surface ($\tau = \tau_s$, where the upward intensity is
$B_\nu(T_s)$ for a black surface) and rearranging:

$$\boxed{\;I_\nu^\uparrow(0) = B_\nu(T_s)e^{-\tau_s}
+ \int_0^{\tau_s}B_\nu\!\left(T(\tau')\right)e^{-\tau'}\mathrm{d}\tau'\;}$$

**Limits.**

- $\tau_s \to 0$: the integral vanishes and
  $I_\nu^\uparrow(0) \to B_\nu(T_s)$ — the surface is seen directly.
- $\tau_s \to \infty$: the surface term vanishes and the integrand $B_\nu e^{-\tau}$
  is negligible outside $\tau \approx 1$, so
  $I_\nu^\uparrow(0) \approx B_\nu(T(z_e))$ with $z_e$ the level where $\tau = 1$.

**The sentence.** In the opaque limit the escaping radiation carries the
temperature of the level at $\tau \approx 1$ rather than the surface temperature,
so a planet whose emitting level lies in cold air must have a *warmer* surface to
radiate the same flux — which is the greenhouse effect stated as an emission-level
statement rather than as a "trapping" statement.

---

## ★6 — Exact single-layer solution

**Balances.**

$$\text{TOA: } (1-\varepsilon)\sigma T_s^4 + \varepsilon\sigma T_a^4 = F,
\qquad
\text{surface: } \sigma T_s^4 = F + \varepsilon\sigma T_a^4 .$$

**Elimination.** From the TOA equation,
$\varepsilon\sigma T_a^4 = F - (1-\varepsilon)\sigma T_s^4$. Substituting:

$$\sigma T_s^4 = F + F - (1-\varepsilon)\sigma T_s^4
\;\Longrightarrow\;
\sigma T_s^4\left[1 + (1-\varepsilon)\right] = 2F,$$

$$\boxed{\;\sigma T_s^4 = \frac{2F}{2-\varepsilon}\;}$$

**Layer temperature.** Substituting back:

$$\sigma T_a^4 = \frac{F}{\varepsilon} - \frac{1-\varepsilon}{\varepsilon}\sigma T_s^4
= \frac{F}{\varepsilon}\left[1 - \frac{2(1-\varepsilon)}{2-\varepsilon}\right]
= \frac{F}{\varepsilon}\cdot\frac{\varepsilon}{2-\varepsilon}
= \frac{F}{2-\varepsilon}.$$

$$\boxed{\;\sigma T_a^4 = \frac{F}{2-\varepsilon}\;}$$

**Numbers for $\varepsilon = 0.6$** with $F = 238.175\ \mathrm{W\,m^{-2}}$:

$$T_s = \left(\frac{2\times238.175}{5.670374419\times10^{-8}\times1.4}\right)^{1/4}
= (6.000486\times10^{9})^{1/4} = 278.321\ \mathrm{K},$$

$$T_a = \left(\frac{238.175}{5.670374419\times10^{-8}\times1.4}\right)^{1/4}
= (3.000243\times10^{9})^{1/4} = 234.039\ \mathrm{K}.$$

**Checks.** $\sigma T_s^4 = 340.250 = 2F/(2-\varepsilon)$ ✔ and
$\sigma T_a^4 = 170.125 = F/(2-\varepsilon)$ ✔. In ratio form the two results are
cleaner still:

$$\frac{T_s}{T_e} = \left(\frac{2}{2-\varepsilon}\right)^{1/4} = 1.0933,
\qquad
\frac{T_a}{T_e} = \left(\frac{1}{2-\varepsilon}\right)^{1/4} = 0.9193 .$$

**Why $T_a < T_e$ always.** $(2-\varepsilon)^{-1/4} < 1$ for every
$\varepsilon > 0$, so the layer is always colder than the effective radiating
temperature. **Physically:** the layer must radiate to space at $T_e$ while
receiving energy from a warmer surface below and losing part of it straight
through the window $(1-\varepsilon)$; the layer's own emission must therefore be
*less* than $\sigma T_e^4$, hence $T_a < T_e$. Equivalently, part of what leaves
the top of the atmosphere is surface radiation that never interacted with the layer.

---

## ★7 — Why refining converges while multiplying does not

**Layer emissivity as a function of $N$ at fixed $\tau_s$:**

$$\varepsilon_N = 1-e^{-\tau_s/N}
\;\xrightarrow[N\to\infty]{}\;
\frac{\tau_s}{N} \to 0,
\qquad\text{so}\qquad
N\varepsilon_N \to \tau_s \quad\text{(finite)}.$$

So each layer becomes *thin* and there are *many* of them: the total opacity is
finite and the discretisation is a consistent approximation of a finite-optical-depth
continuum. The surface temperature therefore converges, as the demonstration shows
(279.941, 281.615, 281.736, 281.737 K for $\tau_s = 1$ at $N = 1, 4, 40, 400$).

**The black-slab case is the opposite limit:** $\varepsilon = 1$ for every layer,
so $\varepsilon_N \to 1$ and $N\varepsilon_N \to \infty$ — the total optical depth
diverges with $N$. There is no continuum limit to converge to, and the solution
grows without bound as $(N+1)^{1/4}$.

**The one-line summary.** *Refining a discretisation holds the physics fixed;
adding layers changes it.* Confusing the two produces the unphysical
$(N+1)^{1/4}$ behaviour and is the reason the law must be presented as an
idealisation rather than as a physical sequence.

---

## ★8 — Emission level and the required opacity

$$z_e = \frac{T_s - T_e}{\Gamma} = \frac{290 - 254.578}{6.0\times10^{-3}}
= 5904\ \mathrm{m} = 5.904\ \mathrm{km}.$$

With $\tau(z) = \tau_s e^{-z/H_\tau}$ and $\tau(z_e) = 1$:

| $H_\tau$ | $\tau_s = e^{z_e/H_\tau}$ |
|---|---|
| 3.0 km | $e^{1.968} = 7.16$ |
| 1.5 km | $e^{3.936} = 51.2$ |

Ratio: $51.2/7.16 = 7.16$ — and note that this ratio equals the $H_\tau = 3\
\mathrm{km}$ value itself, because halving the scale height doubles the exponent
and the required opacity is its exponential.

**Lesson.** The *vertical distribution* of an absorber matters as much as its
column amount: concentrating the same total absorber into a shallower layer
requires a 7-fold larger optical depth to place the emission level at the same
height. This is why a greenhouse gas injected high in the atmosphere has a
different effect per molecule from the same gas added near the surface.

---

## ★9 — Saturation of the greenhouse response

| $\varepsilon$ | $T_s$ (K) |
|---|---|
| 0.00 | 254.578 |
| 0.10 | 257.864 |
| 0.90 | 295.618 |
| 1.00 | 302.746 |

$$\left.\frac{\mathrm{d}T_s}{\mathrm{d}\varepsilon}\right|_{0\to0.1}
\approx \frac{257.864-254.578}{0.1} = 32.86\ \mathrm{K\ per\ unit\ \varepsilon},$$

$$\left.\frac{\mathrm{d}T_s}{\mathrm{d}\varepsilon}\right|_{0.9\to1.0}
\approx \frac{302.746-295.618}{0.1} = 71.28\ \mathrm{K\ per\ unit\ \varepsilon}.$$

Ratio $32.86/71.28 = 0.46$: **the *marginal* response is roughly twice as large
near the opaque end as near the transparent end**, which at first sight contradicts
"the response saturates". It is not a contradiction: differentiation of
$\sigma T_s^4 = 2F/(2-\varepsilon)$ gives

$$\frac{\mathrm{d}T_s}{\mathrm{d}\varepsilon}
= \frac{T_s}{4(2-\varepsilon)},$$

which *increases* with $\varepsilon$ because $T_s$ increases faster than
$2-\varepsilon$ decreases. What saturates is the *fractional* response: from
$\varepsilon = 0.9$ to $1.0$, $T_s$ rises by $7.13\ \mathrm{K}$ or $2.4\%$, whereas
from $0$ to $0.1$ it rises by $3.29\ \mathrm{K}$ or $1.3\%$ — comparable
fractions — but the *emissivity* itself changed by $100\%$ and $10\%$ respectively.
**The right statement is therefore about the fractional change:** a $10\%$ increase
in absorptivity near the opaque end buys about $2.4\%$ of surface temperature,
whereas the same $10\%$ increase starting from transparency buys much less in
absolute terms, because there is little radiation for the layer to exchange. The
pedagogical point of the exercise is that "does it saturate?" depends on whether
the question is posed in absolute or relative terms, and a careful answer says
which.

---

## ★10 — Specification for a closure-error experiment

1. **Model.** The lesson's discrete grey atmosphere: fixed total optical depth
   $\tau_s$ split into $N$ layers of emissivity $1-e^{-\tau_s/N}$, each layer in
   radiative equilibrium, black surface. Assemble the linear system in
   $x_i = \sigma T_i^4$ and solve directly.
2. **Reference solution.** The Eddington two-stream analytic result
   $T_s = T_e(3\tau_s/4 + 1/2)^{1/4}$, which is itself an approximation but a
   *closed-form* one, so the comparison isolates the closure rather than the
   algebra. A better reference, if available without new assumptions, is the exact
   grey solution with the Hopf function, $T^4 = \tfrac34 T_e^4(\tau + q(\tau))$,
   $q(\infty) = 0.7104$.
3. **Metric.** The fractional difference in surface temperature,
   $(T_s^{\text{model}} - T_s^{\text{ref}})/T_s^{\text{ref}}$, as a function of
   $\tau_s$ at fixed and large $N$.
4. **Expected sign change.** The lesson measures $+4.66\%$ at $\tau_s = 1$,
   $-3.78\%$ at $\tau_s = 4$ and $-6.35\%$ at $\tau_s = 8$. The prediction is that
   the sign change occurs near $\tau_s \approx 2$: at small optical depth the
   single-flux model over-transmits (it treats all radiation as vertical, giving
   shorter paths than the true slanted geometry) and therefore needs a warmer
   surface to escape the same flux; at large optical depth the single-flux model
   under-estimates the amount of emission that escapes.
5. **Distinguishing closure from discretisation.** The decisive test: **hold $N$
   fixed and very large (so the discretisation is converged) and vary the closure**,
   for example by introducing a diffusivity factor $D$ multiplying $\tau$ in the
   layer emissivity, $1-e^{-D\tau_s/N}$. If the discrepancy is a closure error it
   must move systematically with $D$ and cannot be made to vanish at *all* $\tau_s$
   simultaneously. If it is a discretisation error it must shrink as $N$ grows at
   fixed $D$. Running both sweeps and reporting the two-dimensional table is the
   experiment.
6. **Falsification.** If the residual at $N = 10^4$ were still falling as
   $N^{-1}$ for every $\tau_s$, the "closure error" interpretation would be wrong
   and the observed behaviour would be a slow discretisation convergence.

---

## ★11 — Calibrating a grey model to a spectrum

**Why one parameter cannot do it.** A grey model has exactly one free parameter,
$\tau$. The spectral model has a function, $\varepsilon_\lambda$. Matching one
scalar (the broadband outgoing flux, or the broadband emissivity) fixes $\tau$ and
leaves the *derivative* with respect to absorber free — and §3.7 of the lesson
measures that the derivative then differs by a factor of about $2.4$. One equation
cannot constrain two independent observables.

**A calibration that fixes the sensitivity too.** Introduce a *second* grey
parameter. Two standard choices:

- **Two-band grey model:** split the spectrum into a "window" band and a "band"
  band, each with its own optical depth $(\tau_w, \tau_b)$. Two parameters, and
  one can be fitted to the outgoing flux while the other is fitted to
  $\mathrm{d}(\mathrm{OLR})/\mathrm{d}(\text{absorber})$. This is the minimum
  viable structure, and it is exactly what two-band energy balance models do.
- **Scaled-$\tau$ with a diffusivity factor:** fit $(\tau, D)$ to the same two
  observables. This works less well, because the two observables are both integrals
  of the same function evaluated at different absorber amounts, and a scale factor
  and a diffusivity shift them in similar ways.

**The general statement.** Because the sensitivity is a *different functional* of
the spectral emissivity from the flux, matching the flux determines nothing about
the sensitivity. A grey model can be made consistent with **one** observable; a
$k$-band model with **$k$** observables. That is the design principle behind
correlated-$k$ and line-by-line schemes.

**The distinguishing observable in a satellite record.** The *outgoing spectral
radiance* — the shape of the spectrum, in particular the depth and position of the
atmospheric absorption features. A grey model has no features at all: its outgoing
spectrum would be a Planck function at a single effective emission temperature, so
a measurement of the spectral contrast between a window channel and a band channel
distinguishes the two models immediately. The second observable is the *rate of
change* of the window-channel radiance with absorber amount, which is a direct
measurement of the sensitivity discussed above.

---

## ★12 — Radiative versus convective adjustment

**The criterion.** A layer is radiatively and convectively consistent when its
actual lapse rate equals whichever of the two is *smaller*:

$$\Gamma_{\text{actual}} = \min\left(\Gamma_{\text{rad}},
\Gamma_{\text{ad}}\right).$$

If the radiative-equilibrium lapse rate is steeper than adiabatic
($\Gamma_{\text{rad}} > \Gamma_{\text{ad}}$), a displaced parcel is unstable
([16-01-03](../../01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md))
and convection carries the excess heat, forcing the actual lapse rate down to the
adiabatic value. If $\Gamma_{\text{rad}} < \Gamma_{\text{ad}}$, radiation alone
can set the profile and convection does not occur.

**Why a radiative–convective model needs an adjustment.** The pure radiative
solution of the lesson reaches $380.7\ \mathrm{K}$ at $\tau_s = 8$ (relative to
$T_e = 254.58\ \mathrm{K}$), so its lapse rate over the troposphere is far steeper
than any realistic adiabat. Physically that is because the radiative solution
assumes every layer is in local radiative balance; in reality, once the radiative
gradient exceeds the adiabat, the layer overturns. The model therefore needs an
explicit step — the *convective adjustment* — that resets any superadiabatic layer
to the adiabatic lapse rate while conserving energy, and then the radiative
calculation is repeated. The result is a self-consistent
radiative–convective equilibrium profile: a convectively adjusted troposphere
capped by a radiatively controlled stratosphere.

**Observable difference.** In a radiative-only profile the outgoing spectrum is
set by the low-temperature upper layers of a very deep, very cold radiating region,
and the *surface* temperature is far above anything observed. Once convection is
included, the emission level sits near the top of the convectively adjusted layer
and the spectrum shows the characteristic signature of the tropopause: a sharp
change in the spectral slope where the emission weighting function transitions from
the convective troposphere to the radiative stratosphere. In a grey model the
convective adjustment shows up as a **discontinuous lapse rate** at the
tropopause, which is the grey proxy for that spectral signature.

**What is derivable here and what is not.** The *criterion*
$\Gamma = \min(\Gamma_{\text{rad}}, \Gamma_{\text{ad}})$ follows from this lesson's
radiative solution plus the parcel stability of
[16-01-03](../../01-atmospheric-structure-and-thermodynamics/03-thermodynamic-processes.md),
and the failure of the pure radiative profile is measured (§3.5). What is *not*
derivable without further assumptions is the *algorithm* for the adjustment
(which quantities are conserved, over what depth, and how a saturated troposphere
is treated), which requires the moist thermodynamics of
[16-01-04](../../01-atmospheric-structure-and-thermodynamics/04-moisture-and-clouds.md)
and the modelling choices quantified in
[05 Energy Balance Models](../05-energy-balance-models.md). **Stating that boundary is
the point of the exercise.**
