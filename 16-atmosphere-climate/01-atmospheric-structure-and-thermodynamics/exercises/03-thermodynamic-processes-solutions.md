# Solutions — 16-01-03 Adiabatic Processes, Lapse Rates and Stability

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [03 Adiabatic Processes](../03-thermodynamic-processes.md).

---

## ★1 — Constants

$$\Gamma_d = \frac{g}{c_p} = \frac{9.80665}{1004.64} = 9.7614\times10^{-3}\
\mathrm{K\,m^{-1}} = \mathbf{9.7614\ K\,km^{-1}},$$

$$\kappa = \frac{R_d}{c_p} = \frac{287.041}{1004.64} = 0.285715 .$$

$$\theta = 300\left(\frac{1000}{900}\right)^{0.285715}
= 300 \times 1.111111^{0.285715}.$$

$\ln 1.111111 = 0.105361$; $\times 0.285715 = 0.030103$; $e^{0.030103} = 1.030561$.

$$\theta = 300 \times 1.030561 = \mathbf{309.17\ K}.$$

So air at $900\ \mathrm{hPa}$ is $9.17\ \mathrm{K}$ warmer than its potential
temperature suggests: real temperature falls with height, $\theta$ rises.

---

## ★2 — Gradient of $\theta$ and $N^2$

$$\frac{\mathrm{d}\theta}{\mathrm{d}z} = \frac{\theta}{T}(\Gamma_d-\Gamma)
= \frac{300}{285}(9.7614 - 7.0)\times10^{-3}
= 1.052632 \times 2.7614\times10^{-3} = 2.9067\times10^{-3}\
\mathrm{K\,m^{-1}}.$$

So $\mathrm{d}\theta/\mathrm{d}z = +2.91\ \mathrm{K\,km^{-1}}$: $\theta$
**increases** with height, which is the signature of stability.

$$N^2 = \frac{g}{T}\left(\Gamma_d-\Gamma\right)
= \frac{9.80665}{285}\times 2.7614\times10^{-3}
= 3.44100\times10^{-2}\times2.7614\times10^{-3} = 9.5016\times10^{-5}\
\mathrm{s^{-2}} > 0 .$$

**Classification: stable** (and note the consistency check
$N^2 = (g/\theta)(\mathrm{d}\theta/\mathrm{d}z)$:
$(9.80665/300)\times2.9067\times10^{-3} = 9.5016\times10^{-5}$ ✔).

---

## ★3 — Period, and its weak temperature dependence

At $T = 285\ \mathrm{K}$:
$N = \sqrt{9.5016\times10^{-5}} = 9.748\times10^{-3}\ \mathrm{s^{-1}}$,
$2\pi/N = \mathbf{644.6\ s}$.

At $T = 255\ \mathrm{K}$:
$N^2 = (9.80665/255)\times2.7614\times10^{-3} = 1.0620\times10^{-4}\
\mathrm{s^{-2}}$, $N = 1.0305\times10^{-2}\ \mathrm{s^{-1}}$,
$2\pi/N = \mathbf{609.7\ s}$.

**Why they differ.** $N^2$ depends on $T$ through the prefactor $g/T$, not only
through $\Gamma$: cold air is denser, so a given fractional temperature excess
produces a smaller acceleration *per unit* — but the restoring force per unit
displacement also involves $g/T$, and the net effect is that $N \propto T^{-1/2}$,
so colder layers oscillate faster. The $5.6\%$ change here comes entirely from
$285 \to 255\ \mathrm{K}$.

---

## ★4 — An isothermal layer

$$\Gamma = 0 \;\Longrightarrow\; N^2 = \frac{9.80665}{255}\times 9.7614\times10^{-3}
= 3.7541\times10^{-4}\ \mathrm{s^{-2}} > 0,$$

$$N = 1.9375\times10^{-2}\ \mathrm{s^{-1}}, \qquad 2\pi/N = \mathbf{324.3\ s}.$$

**Stable** — and this is the counter-intuitive case worth remembering: an
isothermal layer has $T$ *not* falling at all, which is much less steep than
adiabatic, so it is strongly stable. Temperature falling with height is not the
criterion; falling *fast enough* is.

---

## ★5 — Deriving the $\theta$ gradient

Start from $\theta = T(p_0/p)^{\kappa}$ with $\kappa = R_d/c_p$; take logarithms:

$$\ln\theta = \ln T + \kappa\ln p_0 - \kappa\ln p .$$

Differentiate with respect to $z$, holding $p_0$ fixed:

$$\frac{1}{\theta}\frac{\mathrm{d}\theta}{\mathrm{d}z}
= \frac{1}{T}\frac{\mathrm{d}T}{\mathrm{d}z} - \frac{\kappa}{p}\frac{\mathrm{d}p}{\mathrm{d}z}.$$

**This is where hydrostatic balance enters**: substitute
$\mathrm{d}p/\mathrm{d}z = -\rho g$ and the ideal-gas law $\rho = p/(R_dT)$, so
that $(1/p)\,\mathrm{d}p/\mathrm{d}z = -g/(R_dT)$:

$$\frac{1}{\theta}\frac{\mathrm{d}\theta}{\mathrm{d}z}
= \frac{1}{T}\left(-\Gamma\right) + \frac{\kappa g}{R_d T}
= \frac{1}{T}\left(-\Gamma + \frac{R_d}{c_p}\frac{g}{R_d}\right)
= \frac{\Gamma_d - \Gamma}{T},$$

because $\kappa g/R_d = g/c_p = \Gamma_d$. Multiplying by $\theta$ gives the
stated result. ✔

**Evaluation.** $\Gamma_d - \Gamma = 9.7614 - 10.0 = -0.2386\ \mathrm{K\,km^{-1}}$,
so

$$\frac{\mathrm{d}\theta}{\mathrm{d}z} = \frac{300}{280}(-0.2386\times10^{-3})
= -2.556\times10^{-4}\ \mathrm{K\,m^{-1}} = -0.256\ \mathrm{K\,km^{-1}}.$$

**Sign.** Negative $\mathrm{d}\theta/\mathrm{d}z$ means $\theta$ *decreases* with
height and therefore that a displaced parcel is positively buoyant:
$N^2 = (g/T)(\Gamma_d-\Gamma) = -8.358\times10^{-6}\ \mathrm{s^{-2}} < 0$ —
**convectively unstable**, growing with an e-folding time
$1/|N| = 1/2.891\times10^{-3} = 346\ \mathrm{s}$.

---

## ★6 — A dry parcel lifted from 900 to 700 hPa

(a) $\theta = 290\left(\frac{1000}{900}\right)^{0.285715}
= 290 \times 1.030561 = \mathbf{298.86\ K}$.

(b) Invert: $T_2 = \theta\left(\frac{700}{1000}\right)^{0.285715}
= 298.86 \times 0.7^{0.285715}$. $\ln 0.7 = -0.356675$;
$\times 0.285715 = -0.101908$; $e^{-0.101908} = 0.903103$.

$$T_2 = 298.86 \times 0.903103 = \mathbf{269.91\ K}.$$

(c) $\Delta T = 269.91 - 290 = \mathbf{-20.09\ K}$.

(d) At $700\ \mathrm{hPa}$ the environment is at $280\ \mathrm{K}$:

$$a = g\frac{T_p - T_e}{T_e} = 9.80665\times\frac{269.91-280}{280}
= 9.80665\times(-0.036044) = \mathbf{-0.354\ m\,s^{-2}}.$$

**Negative, so the parcel is decelerated and sinks back**: it does not rise
spontaneously. The environment at $700\ \mathrm{hPa}$ is warmer than the dry
adiabat passing through the parcel's starting state.

**Why the path does not matter.** For an adiabatic process $\theta$ is conserved,
so the state $T_2$ depends only on the initial $\theta$ and the final pressure —
not on how the parcel got there. The same conclusion follows from
$s = c_p\ln\theta$ being constant, which makes the process path-independent by
definition.

---

## ★7 — Dry static energy

(a) $c_p T + gz = 1004.64 \times 290 + 0 = 291346\ \mathrm{J\,kg^{-1}}
= \mathbf{291.35\ kJ\,kg^{-1}}$.

(b) $c_p T + gz = 1004.64 \times 250 + 9.80665 \times 5400
= 251160 + 52956 = \mathbf{304.12\ kJ\,kg^{-1}}$.

**The air at $5400\ \mathrm{m}$ has the larger dry static energy**, by
$12.8\ \mathrm{kJ\,kg^{-1}}$. Lifting surface air to that level adiabatically
leaves its DSE unchanged (the demonstration verifies conservation to
$10^{-7}\ \mathrm{J\,kg^{-1}}$), so reaching the state in (b) requires
$12.8\ \mathrm{kJ\,kg^{-1}}$ of energy input — or an equivalent amount of kinetic
energy converted from elsewhere. Ascent is therefore *not* free in a stable
atmosphere.

**Caveat on the comparison.** The two parcels in (a) and (b) are not the same air,
so the difference is not the energy that a single parcel would need unless the two
states lie on the same adiabat. The physically meaningful statement is about one
air mass: "a parcel of DSE $291.35\ \mathrm{kJ\,kg^{-1}}$ cannot reach a level
whose DSE is $304.12\ \mathrm{kJ\,kg^{-1}}$ adiabatically". Comparing two
unrelated air masses measures the stratification, which is a different (also
useful) quantity.

---

## ★8 — Entropy change by two routes

$$\Delta s = c_p\ln\frac{\theta_1}{\theta_0}
= 1004.64 \times \ln\frac{305}{300} = 1004.64 \times 0.016529 = \mathbf{16.61\
J\,kg^{-1}\,K^{-1}}.$$

Direct heat input: $\Delta q/T = 2000/280 = \mathbf{7.14\ J\,kg^{-1}\,K^{-1}}$.

**They are not supposed to agree**, and the reason is instructive. The first
calculation is the *definition* of the entropy change corresponding to a specified
change in $\theta$; the second specifies a heat input and asks what $\theta$ change
it produces. They are related by
$\mathrm{d}\theta/\theta = \mathrm{d}q/(c_p T)$, so a heat input of
$2000\ \mathrm{J\,kg^{-1}}$ produces

$$\Delta\theta = \theta\,\frac{\Delta q}{c_p T}
= 300 \times \frac{2000}{1004.64 \times 280} = 300 \times
7.1098\times10^{-3} = 2.13\ \mathrm{K},$$

i.e. $\theta_1 = 302.13\ \mathrm{K}$, not $305\ \mathrm{K}$; the corresponding
entropy change is $c_p\ln(302.13/300) = 7.14\ \mathrm{J\,kg^{-1}\,K^{-1}}$,
**equal** to $\Delta q/T$. To obtain $\Delta\theta = 5\ \mathrm{K}$ at this
temperature requires $\Delta q = c_p T\,\Delta\theta/\theta = 1004.64 \times 280
\times 5/300 = 4688\ \mathrm{J\,kg^{-1}}$.

The lesson to take away: $\Delta s = \Delta q/T$ holds for a reversible heat
input, and $\Delta s = c_p\ln(\theta_1/\theta_0)$ holds always. Using the first
with a $\theta$ change, or the second with a heat input, is the error.

---

## ★9 — Specification for an amplitude study

1. **Integrator.** The lesson's RK4 on $\ddot\zeta = g[\theta_p - \theta_e(z)]/
   \theta_e(z)$ with $\theta_p$ conserved and $\theta_e$ from a linear
   $\Gamma = 6.5\ \mathrm{K\,km^{-1}}$ environment. Step $\mathrm{d}t = 0.25\
   \mathrm{s}$; integrate $20$ periods. Justify the step by halving it and
   confirming the period changes by less than $10^{-4}$.
2. **Period estimator.** Upward zero crossings of $\zeta$, taking the mean interval
   over many cycles (a single interval has discretisation noise of order
   $\mathrm{d}t/T \sim 4\times10^{-4}$).
3. **Nonlinearity metric.** Two candidates, and report both: (i) the fractional
   period shift $\Delta T/T_0$ against the linear value $2\pi/N$ evaluated at the
   *mean* height of the oscillation; (ii) the drift of the oscillation's centre
   (a nonlinear oscillator with asymmetric restoring force shifts its mean).
4. **Predicted scaling.** Expanding the exact buoyancy
   $g(\theta_p-\theta_e)/\theta_e$ to second order in $\zeta$ gives a quadratic
   term whose coefficient is set by $\mathrm{d}^2\theta_e/\mathrm{d}z^2$, which is
   *zero* for a strictly linear environment. In that case the leading nonlinearity
   comes from the $1/\theta_e$ factor and scales as
   $(\Gamma\,\zeta/\theta)$; the period shift should then be **second order in
   amplitude**, $\Delta T/T_0 \propto A^2$.
5. **The $1\%$ forecast.** From $(1/2)(\Gamma A/\theta)^2 \sim 0.01$ with
   $\Gamma = 6.5\times10^{-3}$, $\theta = 287\ \mathrm{K}$:
   $A \sim \sqrt{2\times0.01}\times 287/6.5\times10^{-3} = 0.1414 \times 4.4\times
   10^{4}\ \mathrm{m} \approx 6\ \mathrm{km}$.
   So a $1\%$ shift is predicted only at **kilometre** amplitudes — far larger
   than the $200\ \mathrm{m}$ used in the lesson, where the measured shift was
   $0.002\%$ (consistent with the $A^2$ scaling:
   $(200/6000)^2 \times 1\% = 1.1\times10^{-3}\% \approx 2\times10^{-3}\%$ ✔).
6. **If the prediction failed.** A period shift growing linearly in amplitude, or
   appearing at small amplitude, would indicate either an integration error
   (check by step refinement) or that the oscillation centre drifts out of the
   region where the environment is linear — in which case the experiment has
   measured $\mathrm{d}^2\theta_e/\mathrm{d}z^2$, not nonlinearity. Distinguishing
   these is the point of the experiment.

---

## ★10 — What "the lapse rate" must specify

| # | Choice | Classification |
|---|---|---|
| 1 | Depth interval over which the difference is taken | Physical *and* definitional: the atmosphere's $\Gamma$ genuinely varies, so quoting "the" lapse rate over a deep layer is an average |
| 2 | Vertical coordinate: $z$, geopotential $Z$, or pressure $p$ | Definitional for small differences ($\Delta\Gamma/\Gamma \sim 10^{-3}$), physical if a pressure-coordinate lapse rate is wanted because it enters the hydrostatic relation differently |
| 3 | Layer-mean convention: arithmetic mean of $T$, or $\ln p$-weighted | Definitional; measured in [lesson 02](../02-hydrostatic-balance.md) as $0.145\%$ of the thickness for the $1000\text{–}500\ \mathrm{hPa}$ layer |
| 4 | Endpoint difference versus least-squares fit over many levels | Definitional, but it changes the sensitivity to noise: an endpoint difference weights the noisiest samples fully, a fit does not |
| 5 | Moisture: does $T$ mean temperature or virtual temperature? | Physical, with a definitional fix: virtual temperature gives the *dynamically* correct stability, temperature does not, and a $10\ \mathrm{g\,kg^{-1}}$ humidity excess is worth $1.75\ \mathrm{K}$ |
| 6 | Whether an inversion is included in the average | Physical: averaging across an inversion produces a lapse rate that describes no layer present in the sounding |

**How a stability diagnostic can flip sign on a definitional choice.** A layer
with a sharp low-level inversion sitting on a superadiabatic surface layer has a
*mean* lapse rate between the two extremes. Depending on which levels are
included, that mean can be above or below $\Gamma_d$; so the same sounding can be
declared stable or unstable without any physical ambiguity being resolved.
The remedy is to define stability *locally*, by $\mathrm{d}\theta/\mathrm{d}z$ on a
stated vertical scale, rather than by a layer-mean lapse rate.

---

## ★11 — Locating the transition from a sounding

**What is measured.** Below the lifting condensation level (LCL) the parcel is
unsaturated and its $T$–$z$ path is the dry adiabat; above it, condensation heats
the parcel and the path is the moist adiabat. From the *sounding alone* the
transition is detectable as a **change in the slope** of the parcel path, and the
robust way to find it without a formula is:

1. **Fix the parcel's initial state** (lowest $100\ \mathrm{hPa}$ mean of $T$ and
   dewpoint — a definitional choice to state).
2. **Compute $\theta$ at every level** and test the *constancy* of $\theta$ as a
   function of height. In the dry layer $\theta$ is (by construction) the parcel's
   constant $\theta_p$. Above the LCL the parcel's $\theta$ is *no longer
   conserved* — condensation reduces the parcel's entropy relative to
   $\theta$ — so the parcel's effective $\theta_p(z)$ rises above the dry
   value. **The breakpoint in the curve $\theta_p(z)$ is the LCL**, and it can be
   found by a piecewise-constant-plus-linear fit without ever writing a moist
   adiabat.
3. **Cross-check by temperature:** the LCL is also where the parcel's temperature
   reaches its dewpoint, i.e. where $e_s(T_p)$ computed from the parcel's
   conserved mixing ratio equals the saturation value. That check needs a
   saturation-vapour-pressure relation, which is the constant the second method
   requires.

**What is modelled.** The assumption that the parcel is undiluted (no
entrainment) and that the only non-adiabatic process is condensation. Both are
approximations: real parcels entrain, so the observed breakpoint is smoother and
lower than the ideal one.

**Largest unresolved uncertainty.** The **height of the breakpoint** is uncertain
because it depends on the vertical interpolation used between sounding levels
(typically $\gtrsim100\ \mathrm{m}$ apart) and on the chosen reference
temperature, which is the mean of the lowest layer. A change of $0.5\ \mathrm{K}$
in the reference temperature moves the LCL by tens of metres; the interpolation
scheme moves it by a comparable amount. Neither is reducible from the same
sounding: they require a finer measurement or an independent humidity profile.
