# Solutions — 16-02-04 Earth Energy Balance and Global Mean Temperature

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [04 Earth Energy Balance](../04-earth-energy-balance.md).

---

## ★1 — The top-of-atmosphere budget versus albedo

$$F = \frac{S(1-a)}{4}, \qquad T_e = \left(\frac{F}{\sigma}\right)^{1/4},
\qquad \text{reflected} = \frac{Sa}{4}.$$

| $a$ | reflected (W m⁻²) | $F$ (W m⁻²) | $T_e$ (K) |
|---|---|---|---|
| 0.30 | 102.08 | 238.175 | 254.578 |
| 0.15 | 51.04 | 289.210 | 267.240 |

Ratio of temperatures:
$267.240/254.578 = 1.04974$ — and indeed
$((1-0.15)/(1-0.30))^{1/4} = (1.21429)^{1/4} = 1.04974$ ✔.

**The point.** Halving the albedo, which doubles the *reflected* flux, raises the
effective temperature by only $5\%$ ($12.7\ \mathrm{K}$), because the temperature
depends on the flux to the *fourth root*. That insensitivity is reassuring for the
radiative budget and alarming for the reverse direction: a $1\ \mathrm{K}$
temperature change is a $1.6\%$ flux change, which is why absolute radiometry is
the hard part of this subject.

---

## ★2 — A surface budget term by term

$$\sigma T_s^4 = 5.670374419\times10^{-8}\times290^4 = 401.055\ \mathrm{W\,m^{-2}},$$

$$\frac{\sigma T_s^4}{F} = \frac{401.055}{238.175} = 1.68387,$$

$$H + LE = F + D - \sigma T_s^4 = 238.175 + 200 - 401.055
= 37.120\ \mathrm{W\,m^{-2}}.$$

**Sign convention:** fluxes *into* the surface are positive, so the surface budget
reads

$$\underbrace{F + D}_{\text{gains}} = \underbrace{\sigma T_s^4}_{\text{radiative loss}}
+ \underbrace{(H+LE)}_{\text{non-radiative loss}} .$$

The non-radiative term is therefore **$+37.120\ \mathrm{W\,m^{-2}}$ exported** —
convection and evaporation cool this surface. A negative value would mean the model
required a non-radiative *heating*, which is unphysical at a planetary surface and
is the diagnostic used in ★6.

---

## ★3 — Transport for $N = 30 - 90\sin^2\phi$

**Global balance.**

$$\int_0^1 (30 - 90u^2)\,\mathrm{d}u = 30 - 90/3 = 30 - 30 = 0 . \;\checkmark$$

(The area-weighted mean is $\int_0^{\pi/2}N\cos\phi\,\mathrm{d}\phi /
\int_0^{\pi/2}\cos\phi\,\mathrm{d}\phi$; since the numerator is this integral and
the denominator is 1, the mean is zero.)

**Analytic transport.** With $u = \sin\phi'$,

$$H(\phi) = -2\pi R_E^2\int_u^1(30 - 90u'^2)\,\mathrm{d}u'
= -2\pi R_E^2\left[30u' - 30u'^3\right]_u^1 .$$

At $u' = 1$ the bracket is $30 - 30 = 0$, so

$$H(\phi) = -2\pi R_E^2\left(0 - 30u + 30u^3\right)
= 60\pi R_E^2\,u\left(1 - u^2\right)
= 60\pi R_E^2\sin\phi\left(1-\sin^2\phi\right).$$

**Maximum.** $\mathrm{d}/\mathrm{d}u\,[u - u^3] = 1 - 3u^2 = 0 \Rightarrow
u = 1/\sqrt3$, i.e. $\phi = 35.26^\circ$. Then

$$H_{\max} = 60\pi R_E^2\cdot\frac{2}{3\sqrt3}
= 60\pi\times4.05896\times10^{13}\times0.384900
= 9.8720\times10^{14}\times 3.84900 .$$

$$H_{\max} = 2.9449\times10^{15}\ \mathrm{W} = \mathbf{2.94\ PW}.$$

**Structure check.** $H(0) = 0$ ✔ (no transport across the equator in a symmetric
state) and $H(90^\circ) = 0$ ✔ (nothing beyond the pole).

---

## ★4 — Planck response for $F = 227.5\ \mathrm{W\,m^{-2}}$

$$T_e = (227.5/\sigma)^{1/4} = 251.676\ \mathrm{K},$$

$$\lambda_0 = 4\sigma T_e^3 = \frac{4F}{T_e}
= \frac{4\times227.5}{251.676} = 3.6158\ \mathrm{W\,m^{-2}\,K^{-1}},$$

$$\Delta T_0 = \frac{2.0}{3.6158} = 0.553\ \mathrm{K}.$$

The identity $\lambda_0 = 4F/T_e$ is the fastest route and doubles as an arithmetic
check: it uses $\sigma T_e^4 = F$ and nothing else.

---

## ★5 — Deriving the two-box relation

Equations (all per unit area, surface temperature $T_s$, layer temperature $T_a$ and
emissivity $\varepsilon$; the grey layer emits $\varepsilon\sigma T_a^4$ both
upward and downward):

$$\text{TOA: } (1-\varepsilon)\sigma T_s^4 + \varepsilon\sigma T_a^4 = F,
\tag{1}$$

$$\text{surface: } f_sF + \varepsilon\sigma T_a^4
= \sigma T_s^4 + (H+LE), \tag{2}$$

$$\text{layer: } f_aF + \varepsilon\sigma T_s^4 + (H+LE)
= 2\varepsilon\sigma T_a^4, \qquad f_a = 1 - f_s . \tag{3}$$

**Step 1.** From (1):
$\varepsilon\sigma T_a^4 = F - (1-\varepsilon)\sigma T_s^4$.

**Step 2.** Substitute into (2):

$$f_sF + F - (1-\varepsilon)\sigma T_s^4
= \sigma T_s^4 + (H+LE),$$

$$F(1+f_s) - (H+LE) = \sigma T_s^4 + (1-\varepsilon)\sigma T_s^4
= \sigma T_s^4(2-\varepsilon).$$

$$\boxed{\;\sigma T_s^4(2-\varepsilon) = F(1+f_s) - (H+LE)\;}\;\checkmark$$

**Step 3 (the equations are not independent).** Now derive $H+LE$ from (3) instead,
using $\varepsilon\sigma T_a^4 = F - (1-\varepsilon)\sigma T_s^4$ from (1):

$$f_aF + \varepsilon\sigma T_s^4 + (H+LE)
= 2F - 2(1-\varepsilon)\sigma T_s^4,$$

$$H+LE = F(2-f_a) - \sigma T_s^4\left[2 - 2\varepsilon + \varepsilon\right]
= F(2-f_a) - \sigma T_s^4(2-\varepsilon).$$

Setting this equal to the Step-2 expression
$F(1+f_s) - \sigma T_s^4(2-\varepsilon)$ gives

$$2 - f_a = 1 + f_s \qquad\Longleftrightarrow\qquad f_s + f_a = 1,$$

**which is true by definition.** So equation (3) is *not* an independent constraint:
the system has rank two, and once $\varepsilon$ and $f_s$ are given, there is one
degree of freedom among $(T_s, T_a, H+LE)$.

**That is the degeneracy of §3.3 in algebraic form, and it is the point of the
exercise.** A surface energy budget cannot determine the opacity and the
non-radiative flux separately; specifying one determines the other. Breaking the
degeneracy requires an extra *physical* relation — a lapse rate, or a convective
adjustment — which is exactly what the radiative–convective models of
[05 Energy Balance Models](../05-energy-balance-models.md) supply.

**Check of the limit.** With $f_s = 1$ and $H+LE = 0$:
$\sigma T_s^4(2-\varepsilon) = 2F$, i.e. $\sigma T_s^4 = 2F/(2-\varepsilon)$ — the
lesson-02 result ✔.

---

## ★6 — Required non-radiative flux versus opacity

Inputs: $F = 1300(1-0.30)/4 = 227.5\ \mathrm{W\,m^{-2}}$,
$\sigma T_s^4 = 390.105\ \mathrm{W\,m^{-2}}$ at $288\ \mathrm{K}$, $f_s = 0.80$.

$$H + LE = F(1+f_s) - \sigma T_s^4(2-\varepsilon)
= 409.50 - 390.105(2-\varepsilon).$$

| $\varepsilon$ | $2-\varepsilon$ | $H+LE$ (W m⁻²) |
|---|---|---|
| 0.50 | 1.50 | $-175.66$ |
| 0.70 | 1.30 | $-97.64$ |
| 0.85 | 1.15 | $-39.12$ |
| 0.95 | 1.05 | $-0.11$ |
| 1.00 | 1.00 | $+19.40$ |

**Zero at** $\varepsilon = 2 - 409.50/390.105 = 2 - 1.04971 = \mathbf{0.95028}$.

**What that value means.** It is the atmospheric emissivity at which this
particular planet's radiative balance *alone* produces a $288\ \mathrm{K}$ surface,
so that convection and evaporation need carry nothing. Below it the radiative model
is too cold (and no physical mechanism could warm the surface non-radiatively);
above it the radiative model is too warm and the surface must export the excess.
**The fit that reproduces a surface temperature is exactly the assumption that
convection and evaporation do not exist.**

---

## ★7 — Transport for a general balanced profile

$$N(\phi) = A + Bu^2, \qquad u = \sin\phi .$$

**Global balance.** $\int_0^1(A + Bu^2)\,\mathrm{d}u = A + B/3 = 0
\Rightarrow A = -B/3$.

**Transport.**

$$H(\phi) = -2\pi R_E^2\int_u^1\left(A + Bu'^2\right)\mathrm{d}u'
= -2\pi R_E^2\left[A(1-u) + \frac{B}{3}(1-u^3)\right].$$

Substituting $A = -B/3$:

$$H(\phi) = -2\pi R_E^2\frac{B}{3}\left[-(1-u) + (1-u^3)\right]
= -2\pi R_E^2\frac{B}{3}(u^3 - u)
= -\frac{2\pi R_E^2B}{3}\,u\left(1-u^2\right).$$

$$\boxed{\;H(\phi) = -\frac{2\pi R_E^2B}{3}\sin\phi\left(1-\sin^2\phi\right)\;}$$

**Checks.**

- $B = -120$: $H = \frac{2\pi R_E^2\times120}{3}u(1-u^2) = 80\pi R_E^2u(1-u^2)$ ✔
  (the lesson).
- $B = -90$: $H = 60\pi R_E^2u(1-u^2)$ ✔ (★3).

**What is a model choice and what is geometric.** The *functional form*
$\propto\sin\phi(1-\sin^2\phi)$ — vanishing at both ends with a single interior
maximum at $\sin^2\phi = 1/3$ — follows from the *requirement* of global balance
plus the *assumption* that $N$ is a function of $\sin^2\phi$ alone. Choose a
different functional form for $N$ (say a polynomial in $\phi$ rather than in
$\sin^2\phi$) and the shape of $H$ changes, though the vanishing at both ends does
not. **The magnitude is proportional to $B$, which is entirely a model choice, and
the vanishing at both ends is geometric and unbreakable.**

---

## ★8 — Bowen ratio changes the partition, not the total

With $F = 238.175\ \mathrm{W\,m^{-2}}$, $f_s = 1$, $\varepsilon = 1$ and
$T_s = 288\ \mathrm{K}$:

$$H + LE = F(1+1) - \sigma T_s^4(2-1) = 476.35 - 390.105
= 86.245\ \mathrm{W\,m^{-2}}.$$

| $B$ | $LE = (H+LE)/(1+B)$ | $H = B\cdot LE$ | total |
|---|---|---|---|
| 0.25 | 68.996 | 17.249 | 86.245 |
| 0.80 | 47.914 | 38.331 | 86.245 |

**Fraction of absorbed solar flux leaving non-radiatively:**
$86.245/238.175 = 0.36216$, i.e. $36.2\%$ — **the same for both Bowen ratios.**

**Which quantity changed and which did not.** The *partition* changed (latent heat
fell from $69.0$ to $47.9\ \mathrm{W\,m^{-2}}$, sensible heat rose from $17.2$ to
$38.3\ \mathrm{W\,m^{-2}}$) and the *total* did not. That is exactly what the
surface energy budget requires: the Bowen ratio is a diagnostic of how the
non-radiative flux is divided, and the budget determines only its sum. **A change in
the Bowen ratio is a change in how the surface cools, not in how much it must
cool** — and that distinction matters, because the two components have very
different effects on the atmosphere (latent heat is deposited where condensation
occurs, sensible heat where it is transferred).

---

## ★9 — Measuring the transport without an assumed profile

1. **Measurement.** The net top-of-atmosphere flux $N$ as a function of latitude,
   obtained from the difference between measured reflected shortwave and measured
   emitted longwave, each from a broadband radiometer with a stated absolute
   calibration. This is an *observed* field; no model profile is assumed.
2. **Sampling.** The integral
   $H(\phi) = -2\pi R^2\int_\phi^{\pi/2}N(\phi')\cos\phi'\,\mathrm{d}\phi'$ requires
   that $N$ be averaged over *longitude and over a full annual cycle* before the
   integral is taken, because the transport requirement is a statement about the
   time-mean state. Diurnal sampling matters: a polar-orbiting instrument samples
   each latitude at fixed local times, so a diurnal bias in cloudiness aliases into
   a spurious zonal gradient. State the drift and the local-time coverage of the
   constellation, not just the number of instruments.
3. **Metric.** The transport profile in PW against latitude, with a stated
   uncertainty band propagated from the flux uncertainties; plus the *closure
   residual*, i.e. $H$ evaluated at the pole, which must be zero and is therefore a
   direct test of the measurement rather than of the physics.
4. **Two error sources that would make closure fail without a physical violation.**
   (i) **Angular and spectral sampling error**: converting a radiance measured at
   one viewing angle to a hemispheric flux requires an angular model, and cloud
   anisotropy is the largest source of error. (ii) **Absolute calibration drift**:
   a constant multiplicative error in the shortwave channel produces an error in
   $N$ that is *proportional to the incident flux*, i.e. largest in the tropics, and
   therefore an error in $H$ that grows poleward — a systematic, not random,
   failure of closure.
5. **What would falsify "the transport must vanish at the equator".** Nothing
   physical can: in a state with no net interhemispheric energy exchange the
   transport across the equator is zero by symmetry. What *could* be measured is a
   nonzero transport, and its existence would demonstrate that the two hemispheres
   are **not** energetically symmetric — that is a statement about the climate
   state (a strong interhemispheric asymmetry in absorbed solar flux caused by the
   land-ocean distribution), not a violation of the requirement. So the honest
   falsifier is: "the hemispherically symmetric assumption is false", not
   "the requirement is false".

---

## ★10 — Breaking the opacity/non-radiative degeneracy

**The degeneracy.** From ★6, the surface temperature fixes only the combination
$F(1+f_s) - \sigma T_s^4(2-\varepsilon) = H+LE$. One equation, two unknowns.

**A programme using surface and column measurements.**

1. **Measure $H + LE$ directly** rather than inferring it. Eddy covariance at the
   surface gives $H$ and $LE$ from the covariance of vertical wind with temperature
   and humidity. That immediately determines one of the two unknowns, and the
   surface budget then *determines* $\varepsilon$ — the atmospheric effective
   emissivity relevant to the downwelling flux. **This is the measurement that does
   the breaking.**
2. **Independent assumption still required.** Eddy covariance measures a flux over a
   *footprint* whose size depends on wind, stability and height; attributing it to
   the same area as the downwelling infrared measurement requires that the two
   footprints coincide and that advection is negligible. Neither is guaranteed, and
   both must be stated.
3. **Cross-check with the vertical profile.** A radiosonde gives $T(z)$ and humidity,
   hence the downwelling infrared from a radiative transfer calculation; comparing
   that with the radiometer's value tests whether the "$\varepsilon$" implied above
   is consistent with the profile. It is a consistency check, not an independent
   measurement, since the transfer calculation assumes the profile.

**The measurement that would break it with no assumption.** Measure the outgoing
spectral radiance, which constrains the *emissivity as a function of wavelength*
rather than a single broadband number, and add the surface fluxes. With
$\varepsilon_\lambda$ measured and $H+LE$ measured, the surface budget is
over-determined and the degeneracy is gone. **Feasibility:** it is feasible in
principle (spectrometers exist), but the *inversion* from radiance to emissivity
still requires a temperature profile and an assumed line-by-line model, so a
residual assumption remains — the honest statement is that the degeneracy can be
reduced to the level of the spectroscopic and profile assumptions, not eliminated.

---

## ★11 — "The global mean surface temperature rose by $X$ kelvin"

**What must be specified.**

| choice | classification |
|---|---|
| Spatial weighting: area-weighted mean over the globe, or a simple mean over stations? | **Definitional**; the two differ systematically because station density is not proportional to area |
| Temporal window: monthly, annual, or a 30-year normal? | **Definitional** at the small end, **physical** at the large end, because natural variability has a spectrum and a short window can be dominated by it |
| Definition of "surface": $2\ \mathrm{m}$ air temperature over land, sea-surface temperature over ocean, or something else? | **Definitional**, and the land/ocean blend is a *choice about which physical quantity* is being averaged; they are not the same variable |
| Treatment of missing regions, historically the polar regions and the oceans | **Definitional** for the interpolation, **physical** for what is actually there |
| Treatment of changing station networks and instrumentation | **Physical** (the networks changed) with a **definitional** fix (homogenisation, which requires choices) |
| Reference period for the baseline | **Definitional**, and it changes the quoted anomaly entirely (not the trend) |

**Reducible with more stations: the sampling variance.** Adding stations reduces
the random component of the spatial-sampling uncertainty.

**Not reducible with more stations: the definitional and structural components.**
Adding stations does not resolve the land-versus-ocean variable definition, the
inhomogeneities of the *existing* long records (which set the trend), or the fact
that a "global mean" of a field with a strongly non-uniform observation network is
an interpolation. The residual uncertainty from homogenisation is a *structural*
uncertainty, not a variance, and it can only be reduced by independent data (e.g. a
different variable or platform that shares no errors), not by station count.

**The lesson's relevance.** This lesson's budget was a *global annual mean*. Every
one of the choices above is also a choice in the budget: $S/4$ is an
area-weighted, annually averaged geometric quantity, and the moment it is compared
with an observed flux the comparison inherits the same definitional questions.

---

## ★12 — A nonzero residual, and the heat capacity

**Constructing a positive residual.** Take a planet with
$F = 238.175\ \mathrm{W\,m^{-2}}$ absorbed and an outgoing longwave flux 2%
smaller, $\mathrm{OLR} = 233.41\ \mathrm{W\,m^{-2}}$. Then

$$N = \text{absorbed} - \mathrm{OLR} = +4.76\ \mathrm{W\,m^{-2}} .$$

**The planet must be warming**, because the top of the atmosphere is gaining energy
and the only place for it to go is into the internal energy of the system.

**Rate of warming.** For a system with a heat-capacity per unit area $C$
($\mathrm{J\,m^{-2}\,K^{-1}}$),

$$C\frac{\mathrm{d}T}{\mathrm{d}t} = N .$$

**Which component dominates $C$.** The ocean, by a very large margin: water's
volumetric heat capacity is a few megajoules per cubic metre per kelvin and the
mixed layer is tens of metres deep, whereas the atmosphere's heat capacity is
equivalent to a layer of water a few metres deep — roughly two orders of magnitude
smaller. **The additional measurement required** to convert $N$ into a rate is an
estimate of the ocean's effective heat capacity, which requires knowing the depth
over which the energy is mixed — an *oceanographic* measurement, not a radiative
one.

**Why equilibrium must be abandoned, and what changes.** The lesson's whole
structure rests on $N = 0$: it is that equality which fixes $\mathrm{OLR}$, which
fixes $T_e$, and which makes the budgets determinate. With $N \ne 0$:

- the balance is a *rate* statement, not a constraint, so one more unknown enters;
- the surface and atmosphere budgets each acquire a storage term, so the
  degeneracy of §3.3 becomes worse rather than better;
- the *time* dimension appears, and with it the distinction between the
  equilibrium response and the transient response — the subject of
  [16-04](../../04-climate-system-and-feedbacks/README.md).

What does *not* change: the geometry of the transport requirement (§3.4), which is
a statement about the time mean of $N$, but which would itself acquire a storage
term if the transport were changing.
