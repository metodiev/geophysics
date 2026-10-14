# Solutions — 10-03-01 GPR for Soil Moisture, Water Table and Aquifer Structure

> **Read after attempting the exercises.** Several problems have more than one
> defensible answer; where that is true it is said so. Numbers were computed with
> the project virtual environment, not estimated by hand.

Lesson: [01 GPR for Soil Moisture, Water Table and Aquifer Structure](../01-gpr-hydrogeology.md).
Constants used: $c = 0.299792458\ \mathrm{m\,ns^{-1}}$,
$Z_0 = 376.730313668\ \Omega$,
$\varepsilon_0 = 8.8541878128\times10^{-12}\ \mathrm{F\,m^{-1}}$,
$\varepsilon_w = 80.1$ (water, $20\ ^\circ\mathrm{C}$). All soil values are
**SYNTHETIC** teaching values.

---

## ★1 — CRIM, saturation, speed, wavelength

$\phi = 0.40$, $\varepsilon_g = 5.0$ so $n_g = 2.23607$;
$\varepsilon_w = 80.1$ so $n_w = 8.95042$; $n_a = 1$; $\theta = 0.20$, so the
three volume fractions are $0.60$, $0.20$ and $0.20$.

$$\sqrt{\varepsilon} = 0.60(2.23607) + 0.20(8.95042) + 0.20(1)
= 1.34164 + 1.79008 + 0.20000 = 3.33172.$$

$$\varepsilon_r = 3.33172^{2} = 11.10 \quad (\text{dimensionless}).$$

$$S = \frac{\theta}{\phi} = \frac{0.20}{0.40} = 0.50.$$

$$v = \frac{c}{\sqrt{\varepsilon_r}} = \frac{0.299792458}{3.33172}
= 0.089984\ \mathrm{m\,ns^{-1}}.$$

$$\lambda = \frac{v}{f} = \frac{0.089984}{0.250} = 0.35994\ \mathrm{m}
\approx 0.360\ \mathrm{m}\ \mathrm{at}\ 250\ \mathrm{MHz}.$$

Units: $\varepsilon_r$ and $S$ dimensionless, $v$ in $\mathrm{m\,ns^{-1}}$
($=10^{9}\ \mathrm{m\,s^{-1}}$), $\lambda$ in m.

---

## ★2 — Porosity sensitivity

$$\frac{\partial\theta}{\partial\phi} = \frac{n_g - n_a}{n_w - n_a}
= \frac{2.23607 - 1}{8.95042 - 1} = \frac{1.23607}{7.95042} = 0.15548.$$

$$\delta\theta = 0.15548 \times 0.03 = 0.0047.$$

About half a percentage point of volumetric water content — comparable with the
difference between a dry and a slightly damp soil, which is the point of the
exercise.

---

## ★3 — Reflection coefficient

$$R = \frac{\sqrt{6.0} - \sqrt{21.0}}{\sqrt{6.0} + \sqrt{21.0}}
= \frac{2.44949 - 4.58258}{2.44949 + 4.58258} = \frac{-2.13309}{7.03207}
= -0.30334.$$

$$20\log_{10}|R| = 20\log_{10}(0.30334) = -10.36\ \mathrm{dB}.$$

$R < 0$: the reflection is **phase-reversed**. Physically the wave moves from the
higher-impedance medium (low $\varepsilon_r$, high $\eta = Z_0/\sqrt{\varepsilon_r}$)
into the lower-impedance one, and the sign of the reflection coefficient follows
from $R = (\eta_2-\eta_1)/(\eta_2+\eta_1)$ with $\eta_2<\eta_1$.

---

## ★4 — One velocity, one wrong depth

$$v_1 = \frac{0.299792458}{\sqrt{5.0}} = 0.134071\ \mathrm{m\,ns^{-1}},
\qquad v_2 = \frac{0.299792458}{\sqrt{16.0}} = 0.074948\ \mathrm{m\,ns^{-1}}.$$

True two-way time to $1.40\ \mathrm{m}$:

$$t = 2\left(\frac{0.60}{0.134071} + \frac{0.80}{0.074948}\right)
= 2(4.4753 + 10.6741) = 30.299\ \mathrm{ns}.$$

The measured $30.0\ \mathrm{ns}$ is therefore $0.3\ \mathrm{ns}$ shorter than the
model predicts, which is a pick-level discrepancy; it is quoted rather than
hidden because it matters below.

**Single-velocity conversion.** $z = 0.115 \times 30.0/2 = 1.725\ \mathrm{m}$.

$$\text{error} = 1.725 - 1.40 = +0.325\ \mathrm{m},\qquad +23.2\%.$$

**Two-layer conversion from the same $30.0\ \mathrm{ns}$.** The top layer costs
$2(0.60)/0.134071 = 8.950\ \mathrm{ns}$; the remaining $21.050\ \mathrm{ns}$ is in
the second layer, one-way $10.525\ \mathrm{ns}$:

$$z = 0.60 + 10.525(0.074948) = 0.60 + 0.7888 = 1.389\ \mathrm{m}.$$

Against the drilled $1.40\ \mathrm{m}$ this is $-0.011\ \mathrm{m}$ ($-0.8\%$),
i.e. entirely explained by the $0.3\ \mathrm{ns}$ pick difference.

**Which layer did the single velocity favour?** The true conversion velocity that
would return $1.40\ \mathrm{m}$ is $2(1.40)/30.0 = 0.09333\ \mathrm{m\,ns^{-1}}$.
The adopted $0.115\ \mathrm{m\,ns^{-1}}$ is $23\%$ higher, i.e. it is biased
toward the **shallow, faster layer** — which is what a shallow sounding measures.
The bias therefore makes every deeper reflector appear too deep, and the error
grows with depth.

---

## ★5 — The graded water table

$\tau = 2h/v$ with $v = 0.10\ \mathrm{m\,ns^{-1}}$, and
$\mathrm{sinc}(x) = \sin(\pi x)/(\pi x)$.

| fringe $h$ (m) | $\tau$ (ns) | $f\tau$ at $250\ \mathrm{MHz}$ | $\mathrm{sinc}(f\tau)$ | $|R| = 0.31|\mathrm{sinc}|$ |
|---|---|---|---|---|
| $0.05$ | $1.00$ | $0.250$ | $0.9003$ | $0.2791$ |
| $0.10$ | $2.00$ | $0.500$ | $0.6366$ | $0.1974$ |
| $0.20$ | $4.00$ | $1.000$ | $0.0000$ | $0.0000$ |

The $0.20\ \mathrm{m}$ case is the **first null**: the reflections from the top
and the bottom of the ramp cancel exactly at the antenna centre frequency, and
$250\ \mathrm{MHz}$ sees nothing at all even though the interface is real.

For the $0.10\ \mathrm{m}$ fringe an analyst who assumed a sharp contact would
report $|R_0| = 0.1974$ where the truth is $0.310$: a factor
$0.1974/0.310 = 0.637$, so the moisture contrast is under-estimated by about
$36\%$.

**Caveat, and it is the demonstration's own.** The sinc form is the
weak-contrast (single-scattering) result. The demonstration sums the Born series
for the *strong* water-table contrast and finds the $0.10\ \mathrm{m}$ fringe
retaining $0.567$ of the sharp amplitude rather than $0.637$. The two answers
differ by $11\%$ because $\sqrt{\varepsilon}$ is not linear across a
$5.95\rightarrow21.03$ ramp. Both are quoted: the analytic answer shows the
mechanism, the direct sum shows the size for the actual contrast.

---

## ★6 — Loss tangent and the exact attenuation

$$\tan\delta = \frac{\sigma}{2\pi f\varepsilon_0\varepsilon_r}.$$

At $100\ \mathrm{MHz}$:
$2\pi(10^{8}) = 6.28319\times10^{8}$,
$\varepsilon' = 8.8541878\times10^{-12}(9) = 7.96877\times10^{-11}$,

$$\tan\delta = \frac{0.02}{6.28319\times10^{8}\times7.96877\times10^{-11}}
= \frac{0.02}{5.00686\times10^{-2}} = 0.3994.$$

At $250\ \mathrm{MHz}$: $\tan\delta = 0.1598$ (scales as $1/f$).

**Threshold.** Adopt $\tan\delta < 0.1$ as "low-loss" (a stated convention, not a
law). $100\ \mathrm{MHz}$ fails outright ($0.399$); $250\ \mathrm{MHz}$ is
marginal ($0.160$).

**Exact attenuation at $250\ \mathrm{MHz}$:**

$$b = \sqrt{\frac{\sqrt{1+\tan^{2}\delta}-1}{2}}
= \sqrt{\frac{\sqrt{1.02554}-1}{2}} = \sqrt{0.006343} = 0.079643,$$

$$\alpha = \omega\sqrt{\mu_0\varepsilon'}\,b
= (1.5708\times10^{9})(1.00065\times10^{-8})(0.079643)
= 1.2518\ \mathrm{Np\,m^{-1}},$$

$$\alpha_{\mathrm{dB}} = 8.6858896 \times 1.2518 = 10.873\ \mathrm{dB\,m^{-1}},$$

$$\text{60 dB two-way depth} = \frac{60}{2(10.873)} = 2.759\ \mathrm{m}.$$

The low-loss formula gives $\sigma Z_0/(2\sqrt{\varepsilon_r}) = 1.2558\
\mathrm{Np\,m^{-1}}$, only $0.3\%$ higher — so at $\tan\delta = 0.16$ the
approximation is *numerically* fine, which is precisely why a rule of thumb
($\tan\delta<0.1$) is a convention and not a derivation. At $100\ \mathrm{MHz}$
the same approximation gives $1.2558$ against an exact $1.2323$: $1.9\%$ high,
and the discrepancy grows quadratically from there.

---

## ★7 — A procedure that could be executed

**Required result:** water-table depth to $\pm 0.10\ \mathrm{m}$ in sand, with a
stated porosity.

1. **Frequency.** $250\ \mathrm{MHz}$ gives $\lambda \approx 0.36\ \mathrm{m}$
   in this soil (Section ★1) and a quarter-wavelength limit of $0.09\ \mathrm{m}$,
   comfortably below the tolerance. Lower frequencies would trade resolution for
   penetration that sand does not need; higher ones lose depth in the capillary
   fringe's absorption.
2. **Velocity, two independent ways.**
   (a) A common-midpoint sounding over the site, which gives the interval
   velocity only over the depth the raypaths actually sample.
   (b) A diffraction hyperbola from a buried point target (a rod driven to a known
   depth, or a utility of known plan position) analysed at an aperture of at least
   $2\times$ the target depth: the lesson's aperture result says a short aperture
   leaves velocity and depth correlated at $+0.999$, so the aperture is part of
   the specification, not a detail.
3. **Porosity, measured not assumed.** A core or a downhole nuclear log gives
   $\phi$ at the site; without it the CRIM inversion carries
   $\partial\theta/\partial\phi = 0.155$, and the amplitude-derived moisture
   contrast is uninterpretable. Note the porosity does **not** affect the depth;
   it affects only the moisture inversion. Keeping those two error terms separate
   is part of the answer.
4. **Depth.** Convert the picked two-way time with the CMP velocity **and** with
   the hyperbola velocity, and report both depths. If they disagree by more than
   the $0.10\ \mathrm{m}$ tolerance, the profile is layered at the scale of the
   Fresnel zone and the answer must be a model, not a pick.
5. **Quoted result.** A depth $\pm$ a stated uncertainty, conditional on the
   velocity model, plus the moisture profile conditional on the porosity. Two
   numbers with two assumption sets — never one number.

**What would invalidate it:** a dispersion of salinity that raises $\tan\delta$
(Section ★6's $250\ \mathrm{MHz}$ case is already marginal at
$0.02\ \mathrm{S\,m^{-1}}$), or clay in the profile, which both raises the loss
and breaks CRIM.

---

## ★8 — Which term dominates the depth budget

$$\sigma_z = \sqrt{\sigma_v^{2} + \sigma_t^{2}}
= \sqrt{0.0475^{2} + 0.0306^{2}} = \sqrt{0.002256 + 0.000936}
= \sqrt{0.003192} = 0.0565\ \mathrm{m},$$

which reproduces the Monte Carlo's $0.0563\ \mathrm{m}$ to rounding — a check
that the two terms are the only ones the simulation varies.

For equal contributions the smaller term must rise to the larger:
$\sigma_t = 0.0475\ \mathrm{m}$, i.e. the picking error must **increase** by
$0.0475/0.0306 = 1.55$, a factor of $1.55$. Equivalently, the velocity
uncertainty must **fall** to $0.0306/0.0475 = 0.644$ of its present value.

With equal terms, $\sigma_z = \sqrt{2}(0.0475) = 0.0672\ \mathrm{m}$ using the
present velocity term, or $\sqrt{2}(0.0306) = 0.0433\ \mathrm{m}$ in the case
where the velocity term was reduced to match the picking term. Neither term
dominates in that state, by construction.

**Reading.** At present the velocity term is $1.55\times$ the picking term in
standard deviation, so it carries $0.0475^{2}/0.003192 = 71\%$ of the variance.
Improving the pick is worth little; the velocity is where the accuracy is bought.

---

## ★9 — Why CRIM and an empirical calibration differ

The two models disagree by $1.79$ percentage points of water content at
$\varepsilon_r = 9.0$. Two physical reasons, each with a detection measurement:

1. **Bound water and clay mineral surfaces.** Water adsorbed on clay surfaces
   does not rotate freely in the microwave field, so its effective permittivity is
   far below $80.1$ and depends on the surface area. CRIM, which assigns every
   water molecule $\varepsilon_w = 80.1$, must then over-predict
   $\varepsilon_r$ at a given $\theta$, and an inversion from a measured
   $\varepsilon_r$ under-predicts $\theta$ — the direction seen here.
   *Detection:* measure the specific surface area (or the cation exchange
   capacity) of the soil and correlate the residual against it; a nonzero slope
   is the signature. Dielectric spectroscopy of the same soil over frequency
   shows the bound-water relaxation directly.
2. **Structural heterogeneity at the scale of the wavelength.** CRIM is a
   volumetric average, valid when the inclusions are small compared with
   $\lambda/10$. In a soil with centimetre-scale stratification, or with
   water-filled pores clustered rather than dispersed, the effective permittivity
   departs from the average in a way that depends on the geometry.
   *Detection:* compare the permittivity measured on the same soil at two
   frequencies far apart (the geometric term is nearly frequency-independent while
   the relaxation terms are not), and compare a crushed, homogenised sample with an
   intact core: any difference is geometric, because the water content is identical.

A third, less physical reason is worth stating because it is common: the
empirical calibration was fitted on soils whose mineral permittivity differs from
the $5.0$ used here. Its $1.79$-point offset is an error of the *pair* of models,
not of either one alone. Nothing in a GPR trace identifies which model is right
for the site, which is why a gravimetric or neutron measurement at one point is
part of any honest moisture survey.
