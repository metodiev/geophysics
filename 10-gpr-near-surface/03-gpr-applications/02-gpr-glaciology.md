---
id: 10-03-02
title: "GPR for Glacier Thickness and Internal Stratigraphy"
level: doctoral
prereqs: ["10-01-01", "10-01-02", "10-01-03", "04-05-02"]
tags: [gpr, near-surface, geotechnical, glaciology, radio-echo-sounding, ice-thickness, firn]
---

# GPR for Glacier Thickness and Internal Stratigraphy

**All models and data in this module are SYNTHETIC.** No glacier, radar system or
survey is described here from measurement. The ice thickness, firn profile,
absorption coefficients and ages are chosen teaching values. Physical constants
and the standard permittivity and density of ice are labelled as such.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the low-loss depth relation $z = c t / (2\sqrt{\varepsilon_r})$ and
   the exact sensitivity $\mathrm{d}H/H = -\mathrm{d}\varepsilon_r/(2\varepsilon_r)$,
   and **compute** how a permittivity error maps into an ice thickness error.
2. **Compute** the permittivity and speed of firn from its density with a
   volumetric mixing model, and **explain** why a firn layer makes the shallow
   part of a radar section faster than the deep part.
3. **Show** that a constant firn correction cancels in a difference of two
   horizon depths but not in an absolute depth, and **state** the condition under
   which that cancellation fails.
4. **Compute** bed reflection coefficients, and **use** the air/ice surface echo
   as an amplitude reference to turn "bright" into a reflection coefficient.
5. **Compute** the quarter-wavelength resolution in a medium and **explain** why
   resolution improves as $1/\sqrt{\varepsilon_r}$ while penetration does not.
6. **Derive** the temperature dependence of englacial absorption from an
   Arrhenius form, and **estimate** the depth of investigation of a sounding at a
   stated ice temperature.
7. **Fit** a diffraction hyperbola to a two-layer (firn + ice) travel time and
   **quantify** the velocity bias and the non-hyperbolic residual it produces.

## Prerequisites

- [10-01-01 GPR Physics: EM Pulses, Dielectric Permittivity and Reflection](../01-gpr-principles/01-gpr-physics.md)
  — the low-loss speed and the reflection coefficient.
- [10-01-02 Velocity Estimation and Depth Conversion](../01-gpr-principles/02-gpr-velocity-and-depth.md)
  — the two-way time, the velocity model and the depth conversion.
- [10-01-03 Attenuation, Penetration Depth and Frequency Trade-Offs](../01-gpr-principles/03-gpr-attenuation-penetration.md)
  — absorption, the dynamic range and the depth of investigation.
- [04-05-02 Glacial Landforms](../../04-earth-science-geology/05-geomorphology-and-quaternary/02-glacial-landforms.md)
  — ice masses, firn and the landforms a thickness survey is used to explain.

## 1. Intuition: the one material through which radar sees for kilometres

Ice is almost the ideal radar medium. It is a solid, so it does not scatter the
way a granular rock does; it is chemically pure, so it has no conduction current
worth the name; and its permittivity is low and tightly constrained by density
and temperature. Radio-echo sounding of ice is therefore the oldest and the most
successful application of the method: the bed of a glacier can be mapped through
a kilometre of ice with an instrument that would see a few metres of wet soil.

Three measurements come out of the same profile, and they are different kinds of
claim:

- the **bed echo**, which gives a thickness *conditional on a permittivity*, and,
  through its amplitude, a *contrast* conditional on a calibration;
- the **internal reflections**, which are usually not material boundaries but
  density and chemistry changes, and whose value is that they are isochrones —
  surfaces of equal age;
- the **surface echo**, which is not clutter but the reference amplitude that
  makes the other two quantitative.

The honest difficulty of the subject is that all three are expressed in
two-way time, and time converts to depth only through a permittivity that is
assigned, not measured. The bed of a glacier is the one place in near-surface
geophysics where the assigned permittivity is genuinely well known
($\varepsilon_r = 3.17$ for cold ice) — and even there the firn at the top of the
column, whose density is *not* known, biases the shallow section.

## 2. Precise definitions

### 2.1 The ice column

| Quantity | Symbol | Value used here | Status |
|---|---|---|---|
| relative permittivity of cold ice | $\varepsilon_{\mathrm{ice}}$ | $3.17$ | standard value |
| density of ice | $\rho_{\mathrm{ice}}$ | $917\ \mathrm{kg\,m^{-3}}$ | standard value |
| relative permittivity of liquid water | $\varepsilon_w$ | $80.1$ | standard value, $20\ ^\circ\mathrm{C}$ |
| speed of light | $c$ | $0.299792458\ \mathrm{m\,ns^{-1}}$ | exact |

The **firn** column is snow that has densified but not yet closed off into ice. It
is a mixture of ice and air with density between roughly
$400$ and $900\ \mathrm{kg\,m^{-3}}$, and that is a chosen teaching range, not a
site measurement.

### 2.2 Two-way time and depth

For a uniform medium,

$$t = \frac{2z}{v}, \qquad v = \frac{c}{\sqrt{\varepsilon_r}},$$

so

$$z = \frac{c\,t}{2\sqrt{\varepsilon_r}}.$$

$t$ is in ns, $z$ in m, $v$ in $\mathrm{m\,ns^{-1}}$.

### 2.3 Resolution and the recorded band

The conventional **vertical resolution** of a sounding is $\lambda/4$ in the
medium, with $\lambda = v/f$. The **bandwidth** $B$ sets the limit
$\Delta z = c/(2B\sqrt{\varepsilon_r})$, which is the same statement expressed in
the time domain; the two are consistent to the factor that relates a Ricker
wavelet's bandwidth to its centre frequency.

### 2.4 The absorption coefficient

Absorption in ice is quoted as a one-way attenuation $\alpha$ in
$\mathrm{dB\,m^{-1}}$. A **dynamic range** of $D$ dB is spent at a depth
$D/(2\alpha)$: the factor $2$ is the two-way path. Absorption increases strongly
with temperature, and the standard form for a thermally activated process is

$$\alpha(T) = \alpha_0\exp\!\left[-\frac{E_a}{R}\left(\frac{1}{T}-\frac{1}{T_0}\right)\right],$$

with $T$ in kelvin, $R = 8.314462618\ \mathrm{J\,mol^{-1}K^{-1}}$ (exact) and a
reference temperature $T_0$. In this lesson both $\alpha_0$ and $E_a$ are
**chosen teaching values** ($0.020\ \mathrm{dB\,m^{-1}}$ at
$-20\ ^\circ\mathrm{C}$ and $6.0\times10^{4}\ \mathrm{J\,mol^{-1}}$); the
exponential *form* is the standard one.

## 3. Derivations

### 3.1 Depth and its exact sensitivity to permittivity

Differentiate $z = ct/(2\sqrt{\varepsilon_r})$ at fixed $t$:

$$\frac{\mathrm{d}z}{z} = -\frac{1}{2}\frac{\mathrm{d}\varepsilon_r}{\varepsilon_r}.$$

*Numerical check.* A $+1\%$ error in $\varepsilon_r$ gives
$1/\sqrt{1.01}-1 = -0.4988\%$, i.e. $-0.50\%$. For the demonstration's
$800\ \mathrm{m}$ bed that is $-3.97\ \mathrm{m}$. The demonstration's table
confirms the halving independently: its $\varepsilon_r = 3.30$ entry is a
$+4.10\%$ permittivity error and a $-15.92\ \mathrm{m}$ ($-1.99\%$) depth error,
a ratio of $-0.485$ that differs from $-0.5$ only by the second-order
curvature the linearisation drops.

The full table from the demonstration, for $t = 9502.30\ \mathrm{ns}$:

| assumed $\varepsilon_r$ | $v$ (m/ns) | depth (m) | error (m) |
|---|---|---|---|
| $3.00$ | $0.1731$ | $822.35$ | $+22.35$ |
| $3.10$ | $0.1703$ | $808.98$ | $+8.98$ |
| $3.17$ | $0.1684$ | $800.00$ | $0.00$ |
| $3.30$ | $0.1650$ | $784.08$ | $-15.92$ |
| $3.40$ | $0.1626$ | $772.47$ | $-27.53$ |

A $7\%$ range of assumed permittivity spans $50\ \mathrm{m}$ of thickness. That is
why a radar thickness is always quoted *with* its permittivity, and why an
independent constraint on $\varepsilon_{\mathrm{ice}}$ (a known thickness, a
borehole, or a radar sounding in a place where the bed is exposed) is worth the
trouble.

### 3.2 Firn: a density mixing problem, and a constant time offset

Firn is an ice/air mixture. Apply CRIM with a pore fraction
$\phi = 1-\rho/\rho_{\mathrm{ice}}$:

$$\sqrt{\varepsilon_{\mathrm{firn}}} = (1-\phi)\sqrt{\varepsilon_{\mathrm{ice}}} + \phi\sqrt{\varepsilon_{\mathrm{air}}}.$$

*Worked value (SYNTHETIC).* $\rho = 500\ \mathrm{kg\,m^{-3}}$:
$\phi = 1-500/917 = 0.4547$,

$$\sqrt{\varepsilon} = 0.5453(1.78045) + 0.4547(1) = 0.97088 + 0.45470 = 1.42558,
\qquad \varepsilon = 2.032,$$

$$v = \frac{0.299792458}{1.42558} = 0.21029\ \mathrm{m\,ns^{-1}}.$$

The demonstration prints $\varepsilon = 2.032$ and
$v = 0.2103\ \mathrm{m\,ns^{-1}}$: firn is $1.249$ times **faster** than ice.
This is the counter-intuitive result of the whole subject — the *less* dense
material is the *faster* one, because adding air raises the speed
($\sqrt{\varepsilon}$ closer to $1$) and the density plays no direct role in the
electromagnetic speed.

Now the important structural point. For a two-layer column, firn of thickness
$h$ over ice, the two-way time to a horizon at depth $z > h$ is

$$t(z) = \frac{2h}{v_{\mathrm{firn}}} + \frac{2(z-h)}{v_{\mathrm{ice}}}.$$

The firn's contribution is the *constant* $2h(1/v_{\mathrm{firn}} -
1/v_{\mathrm{ice}})$, independent of $z$. Converting $t$ with $v_{\mathrm{ice}}$
alone therefore returns

$$z_{\mathrm{rep}} = \frac{v_{\mathrm{ice}}t}{2}
= z + h\left(\frac{v_{\mathrm{ice}}}{v_{\mathrm{firn}}} - 1\right)
= z - h\left(1 - \frac{v_{\mathrm{ice}}}{v_{\mathrm{firn}}}\right),$$

a **depth shift that does not grow with depth**. The demonstration's $100\
\mathrm{m}$ column ($20\ \mathrm{m}$ of firn at $500\ \mathrm{kg\,m^{-3}}$ over
$80\ \mathrm{m}$ of ice) has two-way time $1140.4\ \mathrm{ns}$ against
$1187.8\ \mathrm{ns}$ for pure ice, and converting the former as pure ice gives
$96.01\ \mathrm{m}$: $-3.99\ \mathrm{m}$, exactly the offset
$-20(1 - 0.1684/0.2103) = -3.99\ \mathrm{m}$.

Two consequences, and they are the practical content of this section:

- **An absolute depth is firn-sensitive; a thickness between two horizons below
  the firn is not.** The demonstration converts two picked times ($3000$ and
  $6000\ \mathrm{ns}$) with a uniform-ice model and with a firn + ice model: the
  depths differ ($252.6$ and $505.1\ \mathrm{m}$ against $256.6$ and
  $509.1\ \mathrm{m}$) but the thickness is $252.6\ \mathrm{m}$ in both cases, a
  difference of $0.000\ \mathrm{m}$.
- **The cancellation fails if the firn thickness differs between the two
  horizon positions** (which it does across an accumulation gradient), or if one
  of the horizons lies *inside* the firn. Both are survey-geometry questions, not
  radar questions.

### 3.3 Reflection coefficients, and the surface echo as a reference

$$R = \frac{\eta_2-\eta_1}{\eta_2+\eta_1}
= \frac{\sqrt{\varepsilon_1}-\sqrt{\varepsilon_2}}{\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2}}.$$

The demonstration computes, for ice over five beds:

| bed material | $\varepsilon_r$ | $R$ | $|R|/|R_{\mathrm{surface}}|$ | dB vs surface |
|---|---|---|---|---|
| subglacial water | $80.1$ | $-0.6681$ | $2.38$ | $+7.5$ |
| water-saturated till | $25.0$ | $-0.4748$ | $1.69$ | $+4.6$ |
| frozen sediment | $6.0$ | $-0.1582$ | $0.56$ | $-5.0$ |
| crystalline rock | $5.0$ | $-0.1134$ | $0.40$ | $-7.9$ |
| very dry sediment | $2.5$ | $+0.0593$ | $0.21$ | $-13.5$ |

The air/ice surface coefficient is $R = -0.2807$, i.e. $-11.0\ \mathrm{dB}$.

Read the signs before the sizes. **Ice has a lower permittivity than almost every
bed material**, so almost every bed coefficient has the same sign as the surface
coefficient; only a bed drier than ice (snow or air) reverses it. A "polarity
reversal" is therefore a poor water indicator in ground-based radar, and the
discriminator used in practice is the **calibrated amplitude**: a subglacial water
bed returns $+7.5\ \mathrm{dB}$ more than the surface echo, saturated till
$+4.6\ \mathrm{dB}$, rock $-7.9\ \mathrm{dB}$. Because
$R_{\mathrm{surface}} = -0.2807$ is fixed by $\varepsilon_{\mathrm{ice}}$, which is
known to a few per cent, the surface echo is a free in-situ amplitude reference.
That is what turns "a bright reflector" into "a reflection coefficient of
$0.67$, consistent with water".

### 3.4 Resolution in a medium

$$\lambda = \frac{v}{f} = \frac{c}{f\sqrt{\varepsilon_r}},
\qquad \Delta z = \frac{\lambda}{4} = \frac{c}{4f\sqrt{\varepsilon_r}}.$$

The demonstration's table:

| $f$ (MHz) | $\lambda$ in ice (m) | $\lambda/4$ (m) | two-way time of $\lambda/4$ (ns) |
|---|---|---|---|
| $5$ | $33.68$ | $8.42$ | $100.0$ |
| $20$ | $8.42$ | $2.10$ | $25.0$ |
| $100$ | $1.68$ | $0.42$ | $5.0$ |

Note that $\lambda/4$ at $5\ \mathrm{MHz}$ in ice equals $\lambda$ at
$20\ \mathrm{MHz}$ in ice: the resolution improves *in depth* as
$1/\sqrt{\varepsilon_r}$ while the *time* resolution improves with $f$ alone. A
layer thinner than $\lambda/4$ is still detectable — as an amplitude change — but
it is no longer two echoes, and calling it a thickness is an inversion, not a
pick.

### 3.5 Absorption and the depth of investigation

The demonstration's Arrhenius model gives

| $T$ ($^\circ$C) | $\alpha$ (dB/m) | 60 dB two-way depth (m) |
|---|---|---|
| $-40$ | $0.0017$ | $17\,301$ |
| $-30$ | $0.0062$ | $4\,844$ |
| $-20$ | $0.0200$ | $1\,500$ |
| $-10$ | $0.0591$ | $508$ |
| $-5$ | $0.0985$ | $304$ |

A factor of $56.8$ in absorption between $-40$ and $-5\ ^\circ\mathrm{C}$: the
same instrument sees $17\ \mathrm{km}$ of cold ice and $300\ \mathrm{m}$ of
temperate ice. The mechanism is that the loss is thermally activated, so it
depends exponentially on temperature, not linearly. This is why a cold-based ice
sheet and a temperate glacier are different survey problems even when their
geometry is identical, and why the *temperature* of the ice is part of the
interpretation of any penetration claim.

### 3.6 A two-layer hyperbola is not a hyperbola

For a point diffractor at depth $z$ in a uniform medium the travel time at offset
$x$ is the hyperbola

$$t(x) = \frac{2\sqrt{x^2+z^2}}{v}.$$

With a firn layer present, Snell's law at the firn/ice contact bends the ray and
the exact time is

$$t(x) = 2\left[\frac{h}{v_1\cos i_1} + \frac{z-h}{v_2\cos i_2}\right],
\qquad \frac{\sin i_1}{v_1} = \frac{\sin i_2}{v_2} = p,$$

i.e. the same slowness $p$ in both layers. The demonstration evaluates this by
scanning $p$ and fits the best single-velocity hyperbola to the result:

| diffractor depth (m) | fitted $v$ (m/ns) | bias vs ice | max residual (ns) | depth from the fit (m) |
|---|---|---|---|---|
| $100$ | $0.1879$ | $+11.57\%$ | $107.52$ | $107.1$ |
| $400$ | $0.1703$ | $+1.16\%$ | $11.57$ | $400.6$ |
| $800$ | $0.1692$ | $+0.51\%$ | $1.61$ | $800.1$ |

The bias is a **near-surface** problem: $20\ \mathrm{m}$ of firn is a fifth of the
path to a $100\ \mathrm{m}$ horizon and a fortieth of the path to the bed. The
residual is the signature of the misfit: $107.52\ \mathrm{ns}$ at $100\ \mathrm{m}$
means the two-layer times are not hyperbolas, and a single-velocity fit absorbs
the difference into a biased velocity.

## 4. Physical interpretation

- Everything measured is a **two-way time**. Everything reported is a depth or a
  thickness, which needs a permittivity. The sensitivity is exactly
  $-1/2$ in the fractional sense, and it is the dominant term in the error budget
  ($7.98\ \mathrm{m}$ of the demonstration's $\sigma_z = 7.98\ \mathrm{m}$ budget
  at $800\ \mathrm{m}$, against $0.08\ \mathrm{m}$ from a $1\ \mathrm{ns}$ pick
  error).
- **Firn is the shallow-section problem**; ice is the deep-section convenience.
  The constant-offset property of Section 3.2 means thicknesses are robust where
  absolute depths are not, which is why glaciologists report both.
- **Absorption is a temperature measurement in disguise.** A penetration claim
  that does not state an ice temperature is not a claim about the instrument.
- **Internal reflections are usually not interfaces.** They are density,
  chemistry and fabric changes, and their value is that they are dated: an
  isochrone pair with an independently dated age gap turns a thickness into an
  accumulation rate. The demonstration computes $0.5051\ \mathrm{m\,a^{-1}}$ from
  a $252.6\ \mathrm{m}$ thickness over $500\ \mathrm{a}$, and shows that a $2\%$
  error in $\varepsilon_{\mathrm{ice}}$ moves it by $1\%$ — an error that the
  firn cancellation does *not* remove, because the ice permittivity sets the
  conversion factor for the whole thickness.

## 5. Worked examples

### Example 1 — depth and its permittivity error

A cold glacier, a bed echo at $t = 9502.30\ \mathrm{ns}$, assumed
$\varepsilon_r = 3.17$.

1. $v = 0.299792458/\sqrt{3.17} = 0.168380\ \mathrm{m\,ns^{-1}}$.
2. $z = 0.168380 \times 9502.30/2 = 800.00\ \mathrm{m}$.
3. Suppose the ice is actually $2\%$ denser in impurity content and
   $\varepsilon_r = 3.2334$. Then $v = 0.299792458/\sqrt{3.2334} =
   0.166721\ \mathrm{m\,ns^{-1}}$ and $z = 792.12\ \mathrm{m}$: a $7.9\ \mathrm{m}$
   error from a $2\%$ permittivity error, as
   $\mathrm{d}H/H = -\mathrm{d}\varepsilon_r/(2\varepsilon_r)$ predicts
   ($-1\%$).

### Example 2 — is the bed wet?

The surface echo has amplitude $A_s$ and the bed echo $A_b$ after the geometric
spreading and absorption correction. With $R_{\mathrm{surface}} = -0.2807$:

1. A bed echo $7.5\ \mathrm{dB}$ above the surface echo gives
   $|R_{\mathrm{bed}}| = 0.2807 \times 10^{7.5/20} = 0.668$, which matches
   $\varepsilon_{\mathrm{bed}} = 80.1$: **subglacial water**.
2. A bed echo $4.6\ \mathrm{dB}$ above gives $0.475$, matching
   $\varepsilon_{\mathrm{bed}} = 25$: **water-saturated till**.
3. A bed echo $7.9\ \mathrm{dB}$ *below* gives $0.113$: **rock**.
4. The three are separated by $12\ \mathrm{dB}$ in amplitude, which is well inside
   the dynamic range of a sounder — so the discrimination is a calibration
   question, not a sensitivity question. The calibration requires the geometric
   spreading, the absorption, the antenna pattern and the interface roughness to
   be accounted for; each is a model, and roughness alone can move the estimate by
   several dB in the direction of *under*-estimating the contrast.

### Example 3 — accumulation rate from isochrones

SYNTHETIC picks: $t_1 = 3000\ \mathrm{ns}$, $t_2 = 6000\ \mathrm{ns}$, age gap
$500\ \mathrm{a}$, $\varepsilon_r = 3.17$.

1. Uniform-ice conversion: $z_1 = 0.168380(3000)/2 = 252.57\ \mathrm{m}$;
   $z_2 = 505.14\ \mathrm{m}$ (the demonstration prints $252.6$ and $505.1$).
2. Thickness $= 505.14-252.57 = 252.57\ \mathrm{m}$. The two-layer model gives
   $252.6$ and $509.1\ \mathrm{m}$, the same thickness.
3. Accumulation $= 252.57/500 = 0.5051\ \mathrm{m\,a^{-1}}$ of ice equivalent.
4. With $\varepsilon_r = 3.2334$ ($+2\%$), $v = 0.166721$, thickness
   $= 250.08\ \mathrm{m}$ and accumulation $0.50016\ \mathrm{m\,a^{-1}}$: $-1.0\%$.
   The demonstration prints $250.1$ and $0.5002\ \mathrm{m\,a^{-1}}$.

Note what the arithmetic does *not* include: the conversion of ice-equivalent
accumulation to snow accumulation needs a density profile, and the assumption
that both horizons are true isochrones needs a dated core. The radar supplies
one number and inherits two assumptions.

## 6. Assumptions and regime of validity

1. **Low loss, non-magnetic ice.** $\tan\delta$ in cold ice is small
   enough that $v = c/\sqrt{\varepsilon_r}$ is accurate to a fraction of a per
   cent; in temperate ice with a water content of a few per cent it is not, and
   the speed is both lower and frequency-dependent.
2. **A known permittivity, or a known thickness.** The depth conversion is exact
   *given* $\varepsilon_r$; $\varepsilon_r$ is the assumption, and its uncertainty
   enters at half weight.
3. **CRIM for firn.** Valid where the air and ice are mixed at a scale small
   compared with the wavelength; in a $20\ \mathrm{m}$ firn column sounded at
   $5\ \mathrm{MHz}$ ($\lambda = 34\ \mathrm{m}$) that is satisfied, in a
   $1\ \mathrm{GHz}$ survey of a snowpack it is not.
4. **The Arrhenius absorption model.** The exponential form is standard; the
   coefficients used here are teaching values. A real penetration estimate
   requires an absorption measurement or a temperature profile.
5. **A flat, specular bed for amplitudes.** Roughness reduces the coherent echo,
   and the reduction depends on the roughness spectrum at the scale of the
   Fresnel zone. All the amplitudes in this lesson are for smooth interfaces.
6. **Two-way times without migration.** Section 3.6 shows that a dipping or
   curved bed shifts the apparent time; migration requires the very velocity
   model that is in question, so the conversion and the migration are coupled.

## 7. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| permittivity | $\varepsilon_r$ | dimensionless | — |
| density | $\rho$ | $\mathrm{kg\,m^{-3}}$ | — |
| speed | $v$ | $\mathrm{m\,ns^{-1}}$ | $c/\sqrt{\varepsilon_r}$ |
| two-way time | $t$ | ns | $2z/v$ |
| absorption | $\alpha$ | $\mathrm{dB\,m^{-1}}$ | $-10\log_{10}(P/P_0)$ per metre |
| activation energy | $E_a$ | $\mathrm{J\,mol^{-1}}$ | $E_a/R$ in K |
| accumulation | $\dot a$ | $\mathrm{m\,a^{-1}}$ | thickness / age gap |

In the Arrhenius exponent, $E_a/R$ has units of kelvin and $(1/T-1/T_0)$ of
$\mathrm{K^{-1}}$, so the exponent is dimensionless — the only way the
exponential can be evaluated at all.

## 8. Python demonstration

[`code/gpr_glaciology_demo.py`](code/gpr_glaciology_demo.py) prints every number
quoted above:

1. firn density to permittivity and speed, the $1.249$ factor, and the
   $-3.99\ \mathrm{m}$ error of converting a firn column as pure ice;
2. the two-way time to an $800\ \mathrm{m}$ bed and the depth error for five
   assumed permittivities, plus a Monte Carlo depth budget
   ($7.98\ \mathrm{m}$, of which $7.98\ \mathrm{m}$ is permittivity and
   $0.08\ \mathrm{m}$ is picking);
3. bed reflection coefficients referenced to the air/ice surface echo, and the
   statement that all bed signs coincide with it;
4. the $\lambda/4$ resolution at three frequencies;
5. the Arrhenius absorption table and the $56.8\times$ range between
   $-40$ and $-5\ ^\circ\mathrm{C}$;
6. exact two-layer hyperbola times fitted with a single velocity, at three
   diffractor depths, showing the near-surface bias ($+11.57\%$ at
   $100\ \mathrm{m}$) and the residual that betrays it ($107.52\ \mathrm{ns}$);
7. isochrone thicknesses, the firn cancellation ($0.000\ \mathrm{m}$), and the
   $1\%$ accumulation error from a $2\%$ ice-permittivity error.

The ray times are computed by scanning the ray parameter, not by calling a
ray-tracing library, so the check is independent of any package. The demo is
print-only, uses the fixed seed `20261014`, and exits $0$.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/02-gpr-glaciology-exercises.md`](exercises/02-gpr-glaciology-exercises.md)
and
[`exercises/02-gpr-glaciology-solutions.md`](exercises/02-gpr-glaciology-solutions.md).

- **★** Compute $\varepsilon_r$ and $v$ for firn of $600\ \mathrm{kg\,m^{-3}}$,
  and the two-way time through $30\ \mathrm{m}$ of it.
- **★★** A $1200\ \mathrm{m}$ bed echo is converted with $\varepsilon_r = 3.17$
  and with $\varepsilon_r = 3.40$. Give both depths and the difference, and
  compare with the linear estimate.
- **★★★** Design a survey that determines the accumulation rate over a
  $500\ \mathrm{a}$ isochrone pair to $5\%$, stating the frequency, the firn
  correction, the independent constraints, and what remains untestable.

## 10. Further reading

- **Bogorodsky, V. V., Bentley, C. R., & Gudmandsen, P. E. (1985).
  *Radioglaciology.* D. Reidel.** Level: graduate textbook. The founding text of
  radio-echo sounding; the firn and absorption sections are the ancestors of
  everything in this lesson.
- **Plewes, L. A., & Hubbard, B. (2001). A review of the use of radio-echo
  sounding in glaciology. *Progress in Physical Geography*, 25(2).** Level:
  research. A survey of what has and has not worked, including the amplitude
  methods.
- **Cuffey, K. M., & Paterson, W. S. B. (2010). *The Physics of Glaciers*
  (4th ed.). Elsevier.** Level: graduate textbook. The density, temperature and
  flow context that makes a thickness measurement useful.
- Instrument practice: ground-based ice sounders operate from a few MHz to a few
  hundred MHz, and airborne ice sounders are conventionally built around tens of
  MHz to trade resolution for penetration at aircraft altitude. These are
  standard design bands for the class of instrument, not properties of any
  particular model.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## Mastery checkpoint

Complete this without notes. All values are SYNTHETIC.

> A cold glacier has $25\ \mathrm{m}$ of firn at $520\ \mathrm{kg\,m^{-3}}$ over
> ice of $\varepsilon_r = 3.17$. A $20\ \mathrm{MHz}$ sounder records the bed at
> $12\,000\ \mathrm{ns}$ and an internal horizon at $4000\ \mathrm{ns}$.
> **(a)** Compute the firn permittivity, the firn speed and the ice speed.
> **(b)** Convert both times using a two-layer model, and again using ice alone;
> give the depth error of the ice-only conversion for each. **(c)** Explain in one
> sentence why the internal horizon's depth error equals the bed's, and what that
> implies for a thickness between them. **(d)** Compute $\lambda/4$ in ice at
> $20\ \mathrm{MHz}$ and state whether the $4000\ \mathrm{ns}$ horizon could be
> resolved if it were two horizons $3\ \mathrm{m}$ apart. **(e)** The bed echo is
> $6\ \mathrm{dB}$ stronger than the surface echo. Compute
> $|R_{\mathrm{bed}}|$ and name the two bed materials consistent with it.
> **(e)** The bed echo is $4.6\ \mathrm{dB}$ stronger than the surface echo.
> Compute $|R_{\mathrm{bed}}|$, the implied bed permittivity, and state which
> material of the lesson's table it matches and what would have to be true
> instead for subglacial water.
> **(f)** State which single measurement would most reduce the thickness error.

A worked version of (a)–(b) appears in the
[solutions](exercises/02-gpr-glaciology-solutions.md).

## Common pitfalls

1. **Quoting a thickness without the permittivity.** At $800\ \mathrm{m}$ a $7\%$
   permittivity range spans $50\ \mathrm{m}$.
2. **Assuming firn is slow.** It is faster than ice
   ($0.2103$ against $0.1684\ \mathrm{m\,ns^{-1}}$ in the demonstration), which is
   why an uncorrected shallow section reads too shallow.
3. **Applying a firn correction to a thickness.** It is a constant time offset and
   cancels in a difference — but only if both horizons are below the firn.
4. **Using polarity as a water indicator.** Ice has the lowest permittivity of
   almost all bed materials, so almost every bed reflection shares the surface
   echo's sign; the calibrated amplitude is the measurement.
5. **Citing a penetration depth without a temperature.** The same ice at
   $-40$ and $-5\ ^\circ\mathrm{C}$ differs by $57\times$ in absorption.
6. **Fitting one velocity to a diffraction hyperbola.** With a firn layer the
   times are not hyperbolas; the fit hides the firn in a biased velocity
   ($+11.6\%$ at $100\ \mathrm{m}$).

## Related modules

- [10-01 GPR Principles](../01-gpr-principles/README.md) — the physics of the
  speed, the reflection and the resolution used throughout.
- [10-02 GPR Acquisition and Processing](../02-gpr-acquisition-and-processing/README.md)
  — the acquisition geometry, the migration and the velocity analysis that turn
  these profiles into sections.
- [10-03 GPR Applications](./README.md) — the companion applications in
  hydrogeology, archaeology, infrastructure and planetary sounding.
- [10-06 Near-Surface Monitoring and Time-Lapse](../06-nearsurface-monitoring/README.md)
  — repeating an ice sounding to detect change.
- [04-05 Geomorphology and Quaternary](../../04-earth-science-geology/05-geomorphology-and-quaternary/README.md)
  — what the thickness and the internal stratigraphy are used to explain.

## Code and exercises

| Path | Contents |
|---|---|
| [`code/gpr_glaciology_demo.py`](code/gpr_glaciology_demo.py) | The seven computations of Section 8 |
| [`exercises/02-gpr-glaciology-exercises.md`](exercises/02-gpr-glaciology-exercises.md) | Graded problems |
| [`exercises/02-gpr-glaciology-solutions.md`](exercises/02-gpr-glaciology-solutions.md) | Worked solutions |

```bash
cd 10-gpr-near-surface/03-gpr-applications/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python gpr_glaciology_demo.py
```
