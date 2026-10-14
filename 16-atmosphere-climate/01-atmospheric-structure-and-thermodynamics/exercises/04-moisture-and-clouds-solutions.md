# Solutions — 16-01-04 Moisture, Humidity Variables and Cloud Formation

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [04 Moisture and Clouds](../04-moisture-and-clouds.md).

---

## ★1 — Saturation vapour pressure and its sensitivity

$$e_s(283.15) = 611.2\exp\left[\frac{2.501\times10^{6}}{461.5}
\left(\frac{1}{273.15}-\frac{1}{283.15}\right)\right].$$

Exponent: $\dfrac{2.501\times10^{6}}{461.5} = 5419.3$;
$\dfrac{1}{273.15}-\dfrac{1}{283.15} = 3.66099\times10^{-3}-3.53170\times10^{-3}
= 1.29290\times10^{-4}$; product $0.70065$; $e^{0.70065} = 2.01504$.

$$e_s(283.15) = 611.2\times2.01504 = 1231.65\ \mathrm{Pa} = 12.3165\ \mathrm{hPa}.$$

$$e_s(293.15) = 611.2\exp\left[5419.3\times(3.66099\times10^{-3}
-3.41122\times10^{-3})\right] = 611.2\,e^{1.35321} = 2366.09\ \mathrm{Pa}.$$

| $T$ (K) | $e_s$ (hPa) | $L_v/(R_vT^2)$ (%/K) |
|---|---|---|
| 283.15 | 12.3165 | 6.759 |
| 293.15 | 23.6609 | 6.306 |

**One sentence.** Because saturation vapour pressure rises by about $6.5\%$ per
kelvin, holding relative humidity fixed as the atmosphere warms implies that its
water-vapour content rises at the same rate — a *thermodynamic* capacity
statement, which says nothing on its own about whether relative humidity stays
fixed.

---

## ★2 — A full conversion at $290\ \mathrm{K}$, $950\ \mathrm{hPa}$

$$\frac{2.501\times10^{6}}{461.5}\left(\frac{1}{273.15}-\frac{1}{290}\right)
= 5419.3\times(3.66099\times10^{-3}-3.44828\times10^{-3}) = 1.15263,$$

$$e_s(290) = 611.2\,e^{1.15263} = 1935.64\ \mathrm{Pa}, \qquad
e = 0.70\times1935.64 = 1354.95\ \mathrm{Pa}.$$

$$w = \frac{0.622 \times 1354.95}{95000-1354.95} = \frac{842.78}{93645.05}
= 8.9993\times10^{-3}\ \mathrm{kg\,kg^{-1}},$$

$$q = \frac{0.0089993}{1.0089993} = 8.9191\times10^{-3}\ \mathrm{kg\,kg^{-1}},$$

$$T_d = \left[\frac{1}{273.15}-\frac{461.5}{2.501\times10^{6}}
\ln\frac{1354.95}{611.2}\right]^{-1}.$$

$\ln(1354.95/611.2) = \ln 2.21698 = 0.79612$;
$\frac{461.5}{2.501\times10^6} = 1.84526\times10^{-4}$;
product $1.46913\times10^{-4}$.

$$T_d = \left[3.66099\times10^{-3}-1.46913\times10^{-4}\right]^{-1}
= (3.51408\times10^{-3})^{-1} = 284.5686\ \mathrm{K}.$$

**Verification:** $e_s(284.5686) = 1354.95\ \mathrm{Pa} = e$ ✔

---

## ★3 — Rule of thumb

Dewpoint depression $= 290 - 284.5686 = 5.4314\ \mathrm{K}$.

$$z_L \approx 125\,\mathrm{m\,K^{-1}} \times 5.4314\ \mathrm{K}
= \mathbf{678.9\ m}.$$

---

## ★4 — Saturated lapse rate at $280\ \mathrm{K}$, $900\ \mathrm{hPa}$

$e_s(280) = 611.2\exp[5419.3(3.66099\times10^{-3}-3.57143\times10^{-3})]
= 611.2\,e^{0.48530} = 991.0\ \mathrm{Pa}$.

$$w_s = \frac{0.622\times991.0}{90000-991.0} = \frac{616.4}{89009} = 6.939\times10^{-3}
\ \mathrm{kg\,kg^{-1}},$$

$$A = \frac{L_vw_s}{R_dT} = \frac{2.501\times10^{6}\times6.939\times10^{-3}}
{287.041\times280} = \frac{17354}{80371} = 0.21594,$$

$$B = \frac{L_v^2w_s}{c_pR_vT^2} =
\frac{6.255\times10^{12}\times6.939\times10^{-3}}
{1004.64\times461.5\times78400} = \frac{4.3404\times10^{10}}{3.6354\times10^{10}}
= 1.19414,$$

$$\Gamma_m = \frac{9.80665}{1004.64}\times\frac{1.21594}{2.19414}
= 9.7614\times10^{-3}\times0.55418 = 5.4095\times10^{-3}\ \mathrm{K\,m^{-1}}
= \mathbf{5.410\ K\,km^{-1}},$$

$$\frac{\Gamma_m}{\Gamma_d} = 0.5542 .$$

**Warmer or colder?** A saturated parcel cools at $5.41\ \mathrm{K\,km^{-1}}$
against the dry $9.76$: **it is warmer than a dry parcel lifted the same
distance**, because condensation has replaced some of the expansion cooling with
latent heat. That temperature advantage is what makes moisture the fuel of
convection.

---

## ★5 — Derivation of Clausius–Clapeyron

Start from the Clapeyron equation for equilibrium between two phases,
$\mathrm{d}p/\mathrm{d}T = L/(T\Delta v)$, with $L$ the latent heat and
$\Delta v$ the specific-volume change.

**Approximation 1.** The specific volume of the condensed phase is negligible
against the vapour: $\Delta v \approx v_v$.

**Approximation 2.** The vapour is an ideal gas, so $v_v = R_vT/e_s$.

Then

$$\frac{\mathrm{d}e_s}{\mathrm{d}T} = \frac{L_v}{T v_v}
= \frac{L_v e_s}{R_vT^2}
\qquad\Longrightarrow\qquad
\frac{\mathrm{d}\ln e_s}{\mathrm{d}T} = \frac{L_v}{R_vT^2}.$$

**Approximation 3.** $L_v$ independent of $T$, so the right-hand side integrates
to $\frac{L_v}{R_v}\left(\frac{1}{T_0}-\frac{1}{T}\right)$.

$$\boxed{\;e_s(T) = e_{s0}\exp\left[\frac{L_v}{R_v}
\left(\frac{1}{T_0}-\frac{1}{T}\right)\right].}$$

**Numerical check at $288.15\ \mathrm{K}$:** exponent
$= 5419.3\times(3.66099\times10^{-3}-3.47041\times10^{-3})
= 5419.3\times1.90577\times10^{-4} = 1.03281$; $e^{1.03281} = 2.80895$;
$e_s = 611.2\times2.80895 = \mathbf{1716.80\ Pa}$ ✔, as tabulated in the lesson.

---

## ★6 — Exact LCL for the ★2 state

Parcel: $\theta_p = 290\left(\frac{100000}{95000}\right)^{0.285715}
= 290\times1.014763 = 294.281\ \mathrm{K}$, and $w = 8.9993\
\mathrm{g\,kg^{-1}}$.

Environment: $p_e(z) = 95000(1-6.5\times10^{-3}z/290)^{5.2561}$,
$T_e(z) = 290 - 6.5\times10^{-3}z$.

Solve $w_s\bigl(\theta_p(p_e/100000)^{0.285715},\,p_e\bigr) = w$ by bisection on
$z$:

| $z$ (m) | $p_e$ (hPa) | $T_p$ (K) | $w_s$ (g kg⁻¹) |
|---|---|---|---|
| 0 | 950.000 | 290.000 | 12.936 |
| 300 | 916.901 | 287.077 | 11.048 |
| 600 | 884.743 | 284.163 | 9.410 |
| **682.57** | 876.054 | **283.363** | **8.999** |


$$z_L = \mathbf{682.6\ m}, \qquad T_L = 283.363\ \mathrm{K}.$$

Rule of thumb: $678.9\ \mathrm{m}$. Difference $+3.6\ \mathrm{m}$, i.e.
$\mathbf{+0.53\%}$.

**Why the sign?** The rule linearises the *difference* between the dry-adiabatic
cooling rate and the dewpoint's fall rate. Both rates change with height: the dry
adiabat is exactly linear, but the dewpoint falls slightly faster than linearly
because $e_s$ is convex in $T$. The linearisation therefore underestimates the
height at which the two curves meet, and the exact LCL comes out *above* the
estimate. The discrepancy is small here because the depression is only
$5.4\ \mathrm{K}$; it grows with the depression (for the mastery-checkpoint state
with a $6.8\ \mathrm{K}$ depression the rule is $11\%$ low).

---

## ★7 — Derivation of the saturated adiabatic lapse rate

**(a) The parcel's first law.** For a saturated parcel in pressure equilibrium with
an environment of density $\rho_e$ (so $\mathrm{d}p/\mathrm{d}z = -\rho_e g$),
condensing $\mathrm{d}w_s$ per unit mass:

$$c_p\,\mathrm{d}T - \frac{1}{\rho_p}\mathrm{d}p = -L_v\,\mathrm{d}w_s
\;\Longrightarrow\;
c_p\frac{\mathrm{d}T}{\mathrm{d}z} + \frac{\rho_e}{\rho_p}g
= -L_v\frac{\mathrm{d}w_s}{\mathrm{d}z}.$$

**(b) The derivative of $w_s$.** With $w_s = \varepsilon e_s/p$ (the approximation
under test),

$$\frac{\mathrm{d}\ln w_s}{\mathrm{d}z}
= \frac{1}{e_s}\frac{\mathrm{d}e_s}{\mathrm{d}z} - \frac{1}{p}\frac{\mathrm{d}p}{\mathrm{d}z}
= \frac{L_v}{R_vT^2}\frac{\mathrm{d}T}{\mathrm{d}z} + \frac{g}{R_dT_e},$$

using Clausius–Clapeyron and the hydrostatic relation for the environment.

**(c) Combine**, and for clarity set $\rho_e = \rho_p$ (equivalently
$T_e = T$), and write $A = L_vw_s/(R_dT)$, $B = L_v^2w_s/(c_pR_vT^2)$:

$$c_p\frac{\mathrm{d}T}{\mathrm{d}z} + g
= -L_vw_s\left[\frac{L_v}{R_vT^2}\frac{\mathrm{d}T}{\mathrm{d}z}
+ \frac{g}{R_dT}\right],$$

$$\frac{\mathrm{d}T}{\mathrm{d}z}\left(c_p + \frac{L_v^2w_s}{R_vT^2}\right)
= -g\left(1 + \frac{L_vw_s}{R_dT}\right)
= -g(1+A),$$

$$\Gamma_m = -\frac{\mathrm{d}T}{\mathrm{d}z}
= \frac{g}{c_p}\frac{1+A}{1+B}. \qquad \checkmark$$

**(d) The limit.** As $w_s \to 0$ both $A$ and $B$ vanish, so
$\Gamma_m \to g/c_p = \Gamma_d$. Physically: **when there is no condensable water,
saturation is irrelevant and the parcel behaves as a dry parcel.** The
demonstration measures $\Gamma_m/\Gamma_d = 0.9968$ at $193.15\ \mathrm{K}$,
$100\ \mathrm{hPa}$, where $w_s = 10.3\ \mathrm{mg\,kg^{-1}}$.

---

## ★8 — A lifted parcel at $3\ \mathrm{km}$

(a) Below the LCL ($600\ \mathrm{m}$) the parcel follows the dry adiabat:

$$T(600\ \mathrm{m}) = 292 - 9.7614\times0.6 = 292 - 5.857 = 286.143\ \mathrm{K}.$$

Above it, with an average saturated lapse rate of $5.5\ \mathrm{K\,km^{-1}}$ over
the remaining $2.4\ \mathrm{km}$:

$$T_p(3\ \mathrm{km}) = 286.143 - 5.5\times2.4 = 286.143 - 13.200
= \mathbf{272.943\ K}.$$

(b)

$$a = g\frac{T_p - T_e}{T_e} = 9.80665\times\frac{272.943-268}{268}
= 9.80665\times0.018444 = \mathbf{+0.1809\ m\,s^{-2}},$$

about $1.8\%$ of $g$.

(c) The buoyancy is **positive**, so the parcel is **accelerating** upward at that
level; if the environment stayed like this up to the level of neutral buoyancy the
parcel would keep rising.

**Largest assumption.** That the saturated lapse rate is constant at
$5.5\ \mathrm{K\,km^{-1}}$ between the LCL and $3\ \mathrm{km}$. The real
$\Gamma_m$ *increases* with height as $w_s$ falls (from §3.4 of the lesson: $5.04\
\mathrm{K\,km^{-1}}$ at $283\ \mathrm{K}$, $6.03$ at $273\ \mathrm{K}$,
$7.98$ at $253\ \mathrm{K}$), so a constant-$5.5$ model **overestimates** the
parcel's warmth at $3\ \mathrm{km}$ and hence the buoyancy. The second-largest
assumption is the absence of entrainment.

---

## ★9 — Specification for the $\Gamma_m$ residual experiment

1. **Configurations.** A grid over surface temperature
   $T_0 \in \{280, 285, 290, 295, 300, 305\}\ \mathrm{K}$ and relative humidity
   $\mathrm{RH} \in \{0.5, 0.7, 0.9\}$, with the environment a polytropic profile
   of stated lapse rate so that the LCL is well defined.
2. **Measurement at each level.** Use the same three quantities as §3.6 of the
   lesson: the first-law left-hand side
   $c_p\,\mathrm{d}T_p/\mathrm{d}z + (\rho_e/\rho_p)g$ with
   $\mathrm{d}T_p/\mathrm{d}z$ from the analytic saturated formula; the right-hand
   side with the **approximate** $w_s$ derivative
   $w_s(\mathrm{d}\ln e_s/\mathrm{d}z - \mathrm{d}\ln p/\mathrm{d}z)$; and the
   right-hand side with the **exact** total derivative of $\varepsilon e_s/(p-e_s)$
   along the trajectory. Never evaluate a derivative *at* the kink at the LCL.
3. **Metric.** $R(z) = |\text{LHS} - \text{RHS}_{\text{exact}}|/\text{LHS}$, and the
   companion quantity $e_s/p$ at the same level.
4. **Prediction, stated before running.** Because the only difference between
   $\mathrm{d}\ln(p-e_s)$ and $\mathrm{d}\ln p$ is a factor
   $(1-e_s/p)^{-1}$, and because the two terms being differentiated nearly cancel,
   the residual should scale as
   $R(z) \approx C\,e_s(T_p(z))/p_e(z)$ with $C$ of order unity. Since both
   $e_s$ and $p$ fall with height but $e_s$ falls much faster, $R$ should
   **decrease** with height, roughly exponentially with a scale height of about
   $2\ \mathrm{km}$ at surface temperatures near $290\ \mathrm{K}$.
5. **Falsification.** If $R$ were found to be independent of $e_s/p$ — for
   example if $R$ came out the same at $280\ \mathrm{K}$ and $305\ \mathrm{K}$
   configurations chosen to have equal $e_s/p$ — then the residual is not the
   $w_s$ approximation and something else (most likely the constant-$L_v$
   approximation or a discretisation error) is responsible. That test, more than
   the magnitude itself, is what makes the experiment informative.

---

## ★10 — Dilution (entrainment) specification

**Entrainment equation.** Relax the parcel's conserved properties toward the
environment at a fractional rate $\mu$ per unit height:

$$\frac{\mathrm{d}\theta_p}{\mathrm{d}z} = -\mu\,(\theta_p - \theta_e),
\qquad
\frac{\mathrm{d}w_p}{\mathrm{d}z} = -\mu\,(w_p - w_e),$$

with the temperature recovered from $T_p = \theta_p(p_e/p_0)^{R_d/c_p}$ and the
condition $w_{\text{condensed}} = \max(0, w_p - w_s(T_p,p_e))$ defining saturation.
(These are the standard "bulk-plume" equations; the closure is that $\mu$ is
constant, which is itself an assumption.)

**Numerical scheme.** RK4 in $z$ with a stated step, halved to confirm convergence;
buoyancy $g(T_p-T_e)/T_e$ evaluated with the *diluted* $T_p$; LFC and LNB found by
sign change; CAPE by the trapezoid rule on the same grid.

**Metric.** $\mathrm{CAPE}(\mu)/\mathrm{CAPE}(0)$, reported as a function of $\mu$.

**Predictions.**

- $\mathrm{CAPE}(\mu)$ falls monotonically with $\mu$, and the ratio should fall
  faster for *deeper* clouds, because a parcel that has travelled further has
  entrained more and its $\theta_p$ and $w_p$ are closer to the environment.
  Quantitatively the leading behaviour is exponential in $\mu$ times the
  penetration depth, $\mathrm{CAPE}(\mu)/\mathrm{CAPE}(0) \sim
  e^{-k\mu\,\Delta z}$ for some $k$ of order unity.
- LFC rises and LNB falls with $\mu$: dilution both delays the onset of buoyancy
  and removes it sooner.
- The metric should be more sensitive to $\mu$ when the environment is *dry*,
  because then entrainment removes more buoyancy per unit mass mixed in.

**Falsification.** If the ratio were found to be *insensitive* to cloud depth,
either the entrainment term is being applied inconsistently with the saturation
condition (a bookkeeping bug), or the environment's humidity profile makes the
diluted parcel nearly identical to the environment — which is a statement about
the *environment*, not about entrainment. Both are checkable, and distinguishing
them is the experiment.

---

## ★11 — Critique of "precipitation must rise $6.5\%$ per kelvin"

The argument makes four steps, of which only the first is thermodynamics.

1. **Saturation vapour pressure rises $6.5\%\ \mathrm{K^{-1}}$.** *Physical.*
   Clausius–Clapeyron, with the constant-$L_v$ and ideal-vapour approximations.
2. **Water-vapour content therefore rises $6.5\%\ \mathrm{K^{-1}}$.** *Requires a
   modelling assumption*: that relative humidity stays constant. If RH fell, the
   vapour content would rise less; if it rose, more. This is the step where the
   argument stops being thermodynamics. It is supported by *evidence* (models and
   observations agree to within a few per cent of constant RH in the lower
   troposphere) but it is not a law, and it is not exact.
3. **Precipitation rises in proportion to water-vapour content.** *Physical in
   part, and wrong as stated.* Precipitation equals condensation, and condensation
   equals the *convergence of the vapour flux*, not the vapour content. A warmer
   atmosphere can hold more vapour without raining more, if the circulation does
   not import more moisture into the storm. The relevant statement involves the
   moisture budget of a storm, i.e. the larger-scale dynamics.
4. **The $6.5\%$ applies globally.** *Modelling.* Global-mean precipitation is
   constrained as much by the atmospheric energy budget (how fast the atmosphere
   can radiate away the latent heat released) as by the water supply, and standard
   estimates of that constraint give a rate of change of global precipitation
   nearer $2$–$3\%\ \mathrm{K^{-1}}$ than $6.5$. Extreme *local* precipitation
   scales closer to the Clausius–Clapeyron value than the global mean does — a
   distinction the original sentence erases. The numbers here are *qualitative*
   statements about which physical constraint binds; any specific rate must be
   sourced from the literature or computed by
   [16-05](../../05-climate-models/README.md), and this repository does not assert one.

**Strongest defensible version.**

> Because saturation vapour pressure rises about $6.5\%\ \mathrm{K^{-1}}$ and
> lower-tropospheric relative humidity is observed and modelled to remain nearly
> constant as the atmosphere warms, the atmospheric water-vapour content rises at
> a rate close to $6.5\%\ \mathrm{K^{-1}}$. Whether precipitation rises at the
> same rate depends on the moisture *convergence* and on the atmospheric energy
> budget, so the water-vapour scaling is an upper bound on the response of
> *extreme local* rainfall intensity and not a prediction of the change in
> global-mean precipitation, which is constrained by energy rather than by water.

Every clause of that version names its own evidential basis, and the two claims
that are *not* thermodynamics are labelled as such.
