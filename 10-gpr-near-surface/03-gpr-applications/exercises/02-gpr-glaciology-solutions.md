# Solutions — 10-03-02 GPR for Glacier Thickness and Internal Stratigraphy

> **Read after attempting the exercises.** Numbers were computed with the project
> virtual environment, not estimated by hand. Where a problem has more than one
> defensible answer, that is said.

Lesson: [02 GPR for Glacier Thickness and Internal Stratigraphy](../02-gpr-glaciology.md).
Constants: $c = 0.299792458\ \mathrm{m\,ns^{-1}}$,
$\rho_{\mathrm{ice}} = 917\ \mathrm{kg\,m^{-3}}$,
$\varepsilon_{\mathrm{ice}} = 3.17$, $\varepsilon_w = 80.1$,
$R = 8.314462618\ \mathrm{J\,mol^{-1}K^{-1}}$.

---

## ★1 — Firn of $600\ \mathrm{kg\,m^{-3}}$

$$\phi = 1 - \frac{600}{917} = 0.34569.$$

$$\sqrt{\varepsilon} = (1-0.34569)\sqrt{3.17} + 0.34569(1)
= 0.65431(1.780449) + 0.34569 = 1.164977 + 0.345690 = 1.510667,$$

$$\varepsilon_r = 2.2821, \qquad
v = \frac{0.299792458}{1.510667} = 0.198452\ \mathrm{m\,ns^{-1}}.$$

$$t = \frac{2(30.0)}{0.198452} = 302.34\ \mathrm{ns},$$

$$\lambda = \frac{v}{f} = \frac{0.198452}{0.020} = 9.9226\ \mathrm{m}
\quad \mathrm{at}\ 20\ \mathrm{MHz}.$$

The demonstration prints $\varepsilon_r = 2.282$ and
$v = 0.1985\ \mathrm{m\,ns^{-1}}$ for the same density. Note the direction: denser
firn is *slower*, and ice ($0.1684\ \mathrm{m\,ns^{-1}}$) is slower still.

---

## ★2 — The same time, two permittivities

$$v(3.17) = \frac{0.299792458}{\sqrt{3.17}} = 0.168380\ \mathrm{m\,ns^{-1}}.$$

$$z = \frac{0.168380 \times 14\,253.46}{2} = 1200.00\ \mathrm{m}.$$

$$v(3.40) = \frac{0.299792458}{\sqrt{3.40}} = 0.162582\ \mathrm{m\,ns^{-1}},$$

$$z = \frac{0.162582 \times 14\,253.46}{2} = 1158.70\ \mathrm{m}.$$

Difference: $1158.70 - 1200.00 = -41.30\ \mathrm{m}$, i.e. $-3.44\%$.

The linear estimate is

$$\frac{\mathrm{d}z}{z} = -\frac{1}{2}\frac{0.23}{3.17} = -0.03628
\;\Rightarrow\; -43.53\ \mathrm{m}.$$

**Discussion.** The exact answer is $41.30\ \mathrm{m}$ and the linear
approximation gives $43.53\ \mathrm{m}$: $5\%$ too large, because a $7.3\%$
permittivity change is no longer small. The linear form is the right tool for
error *budgets* at the few per cent level, not for converting between two
material permittivities.

---

## ★3 — Dimensionless exponent

$E_a$ is in $\mathrm{J\,mol^{-1}}$ and $R$ in
$\mathrm{J\,mol^{-1}K^{-1}}$, so $E_a/R$ is in **kelvin**.
$(1/T - 1/T_0)$ is in $\mathrm{K^{-1}}$. The product is therefore
$\mathrm{K}\times\mathrm{K^{-1}}$, dimensionless, which is what an exponential
requires. Numerically, $E_a/R = 6.0\times10^{4}/8.314462618 =
7216.4\ \mathrm{K}$ — a large number, which is exactly why the absorption
changes by a factor of tens over a few tens of kelvin.

---

## ★4 — Depth budget

$z = 800\ \mathrm{m}$, $t = 9502.30\ \mathrm{ns}$,
$v = 0.168380\ \mathrm{m\,ns^{-1}}$.

**Permittivity term.** A $3\%$ permittivity error is a $1.5\%$ velocity error
(exactly half, from Section 3.1):

$$\sigma_z(\varepsilon) = 800 \times 0.015 = 12.00\ \mathrm{m}.$$

**Pick term.** A $2\ \mathrm{ns}$ error on a $9502.30\ \mathrm{ns}$ time is
$0.021\%$:

$$\sigma_z(t) = 800 \times \frac{2}{9502.30} = 800 \times 2.105\times10^{-4}
= 0.168\ \mathrm{m}.$$

**Total:**

$$\sigma_z = \sqrt{12.00^{2} + 0.168^{2}} = \sqrt{144.00 + 0.0283}
= 12.00\ \mathrm{m}.$$

The permittivity dominates by a factor of $71$ in standard deviation, so $99.97\%$
of the variance. **Improving the pick is worthless; the permittivity is the whole
budget.** This is the same conclusion the lesson's Monte Carlo reaches
($7.98$ against $0.08\ \mathrm{m}$ for $2\%$ and $1\ \mathrm{ns}$).

---

## ★5 — Bed coefficients and the reference

$$R_{\mathrm{water}} = \frac{\sqrt{3.17}-\sqrt{80.1}}{\sqrt{3.17}+\sqrt{80.1}}
= \frac{1.780449 - 8.950419}{1.780449 + 8.950419} = -0.6681,$$

$$R_{\mathrm{rock}} = \frac{1.780449 - 2.236068}{1.780449 + 2.236068} = -0.1134,$$

$$R_{\mathrm{surface}} = \frac{\sqrt{1}-\sqrt{3.17}}{\sqrt{1}+\sqrt{3.17}}
= -0.2807.$$

| comparison | arithmetic | dB |
|---|---|---|
| water vs surface | $20\log_{10}(0.6681/0.2807)$ | $+7.53$ |
| rock vs surface | $20\log_{10}(0.1134/0.2807)$ | $-7.87$ |
| water vs rock | $20\log_{10}(0.6681/0.1134)$ | $+15.40$ |

All three coefficients are **negative**: ice has the lowest permittivity of the
three materials, so every bed contact is a step *down* in impedance and the
reflected pulse keeps the polarity of the surface reflection. Only a bed drier
than ice reverses it.

**What the amplitude measurement must also account for.** Before either bed
number can be compared with the surface reference: the geometric spreading
difference between a $1\ \mathrm{km}$ range and a $0\ \mathrm{m}$ range; the
two-way absorption over the ice column, which needs a temperature model; the
antenna pattern (the bed echo arrives from a narrower or wider angular range than
the surface echo); the subglacial interface roughness, which reduces the coherent
echo; and the firn/ice internal multiples that add to the bed echo. Each is a
model with its own error, and roughness alone can bias the contrast by several dB
— always in the direction of under-estimating it.

---

## ★6 — Attenuation at $-25\ ^\circ\mathrm{C}$

$$\alpha(-25) = 0.020\exp\left[-\frac{6.0\times10^{4}}{8.314462618}
\left(\frac{1}{248.15}-\frac{1}{253.15}\right)\right].$$

Bracket: $1/248.15 = 4.02982\times10^{-3}$,
$1/253.15 = 3.95023\times10^{-3}$, difference $7.959\times10^{-5}$.

$$-\frac{E_a}{R}\Delta = -7216.4 \times 7.959\times10^{-5} = -0.57440,
\qquad e^{-0.57440} = 0.56300,$$

$$\alpha = 0.020 \times 0.56300 = 0.011261\ \mathrm{dB\,m^{-1}}.$$

$$\text{60 dB two-way depth} = \frac{60}{2(0.011261)} = 2664\ \mathrm{m},
\qquad
\text{100 dB} = \frac{100}{2(0.011261)} = 4440\ \mathrm{m}.$$

**Why not a linear interpolation?** The bracket contains $1/T$, not $T$: the
Arrhenius form is a straight line in $1/T$, and $1/T$ is curved in $T$. A linear
interpolation between the $-20\ ^\circ\mathrm{C}$ value ($0.0200$) and the
$-30\ ^\circ\mathrm{C}$ value ($0.0062$) would give $0.0131\
\mathrm{dB\,m^{-1}}$ at $-25\ ^\circ\mathrm{C}$ — $16\%$ above the correct
$0.0113$. The exponential guarantees that the midpoint of a temperature interval
is not the midpoint of the attenuation.

---

## ★7 — The firn cancellation, proved

Let the firn thickness be $h$ with speed $v_1$ and the ice speed be $v_2$. For a
horizon at true depth $z_k > h$,

$$t_k = \frac{2h}{v_1} + \frac{2(z_k-h)}{v_2}.$$

Converting with ice alone:

$$z_k^{\mathrm{rep}} = \frac{v_2 t_k}{2} = h\frac{v_2}{v_1} + z_k - h
= z_k - h\left(1 - \frac{v_2}{v_1}\right).$$

The correction is the same constant $C = h\left(1 - v_2/v_1\right)$ for **every**
horizon below the firn, so

$$z_2^{\mathrm{rep}} - z_1^{\mathrm{rep}} = (z_2 - C) - (z_1 - C) = z_2 - z_1.$$

**Conditions.**
1. Both horizons lie **below** the firn. If one lies inside it, its time is
   $2z/v_1$ and the shift is not $C$.
2. The firn thickness (and density) is the **same** at both horizon locations.
   Across an accumulation gradient this fails.

**Error if $h$ differs by $5\ \mathrm{m}$.** With $\rho = 500\
\mathrm{kg\,m^{-3}}$, $v_1 = 0.210300\ \mathrm{m\,ns^{-1}}$ and
$v_2 = 0.168380\ \mathrm{m\,ns^{-1}}$:

$$C = h\left(1 - \frac{0.168380}{0.210300}\right) = h(1 - 0.800665) = 0.199335\,h.$$

$$\Delta C = 0.199335 \times 5 = 0.9967\ \mathrm{m}.$$

For a $252\ \mathrm{m}$ thickness this is $0.40\%$ — small, but it is a
*systematic*, spatially correlated error, so it does not average out along the
profile and it appears as a false accumulation gradient. That is why the firn
correction is applied as a map (from a separate shallow sounding or from
measured density) rather than as one number.

---

## ★8 — Accumulation rate and what it assumes

$$v_2 = 0.168380\ \mathrm{m\,ns^{-1}}, \qquad
\Delta t = 3000\ \mathrm{ns}.$$

$$\Delta z = \frac{v_2 \Delta t}{2} = \frac{0.168380 \times 3000}{2}
= 252.57\ \mathrm{m}.$$

$$\dot a = \frac{252.57}{500} = 0.50514\ \mathrm{m\,a^{-1}}.$$

With $\varepsilon_r = 3.2334$: $v = 0.166721\ \mathrm{m\,ns^{-1}}$,
$\Delta z = 250.08\ \mathrm{m}$, $\dot a = 0.50016\ \mathrm{m\,a^{-1}}$, i.e.
$-0.99\%$ for a $+2\%$ permittivity error — the half-weight rule again.

**Three inherited assumptions and how to test each.** All models and data in this
module are SYNTHETIC; the tests named are the real ones.

1. **Both horizons are isochrones** (surfaces of equal age). A radar reflection is
   a change in density or chemistry, which is usually *along* an isochrone but
   need not be: a melt layer or an ash band follows a deposition surface, while a
   refrozen water table does not. *Test:* trace the horizons to a core or an
   ice-coring site and date them; continuity of the reflection over a
   large distance is weaker evidence but is the only check available away from
   the core.
2. **The ice between the horizons is uniform**, so that one $\varepsilon_r$
   converts the whole thickness. Fabric, impurity content and, above all,
   temperature change $\varepsilon_r$ at the $10^{-3}$ to $10^{-2}$ level, and a
   temperate layer with a per-cent water content changes it far more. *Test:* a
   common-midpoint (or wide-angle) sounding over the two horizons gives the
   interval velocity independently of the depth, which is the direct test.
3. **The age gap is known exactly**, i.e. the dating (and any correction for
   layer thinning between accumulation and the sampled depth) contributes no
   error. In practice this is often the largest term. *Test:* replicate dating at
   a second core, and report the age-gap uncertainty explicitly rather than
   folding it into the depth error.

The radar supplies one number — a two-way time difference — and inherits all
three.

---

## ★9 — A procedure that could be executed

**Objective:** classify the bed as water, saturated till or rock along a
$10\ \mathrm{km}$ profile, with stated uncertainty.

1. **Reference.** Use the air/ice surface echo on every trace as the amplitude
   reference: its coefficient is $R = -0.2807$, fixed by
   $\varepsilon_{\mathrm{ice}} = 3.17$ to a few per cent. Divide each bed echo
   amplitude by the surface amplitude of the **same** trace before any further
   correction, which removes antenna coupling, transmit power and receiver gain
   drift along the profile.
2. **Corrections.** Apply, with stated models: (i) geometric spreading, from the
   measured ice thickness and the antenna pattern; (ii) two-way absorption, from
   the absorption model with its temperature profile — and report the
   classification's sensitivity to that temperature, since a factor of $57$ in
   absorption is available over $35\ \mathrm{K}$; (iii) interface roughness, which
   can only *lower* the coherent amplitude and therefore biases the inferred
   contrast *down*; (iv) the internal-multiple contribution, removed by comparing
   the bed echo before and after predictive deconvolution.
3. **Discrimination bands**, from the lesson's table: water $\ge +7.5\
\mathrm{dB}$ over the surface, saturated till about $+4.6\ \mathrm{dB}$,
frozen sediment $-5.0\ \mathrm{dB}$, rock $-7.9\ \mathrm{dB}$. Water and rock are
$15.4\ \mathrm{dB}$ apart, which is far outside the likely correction error, so
the classification is meaningful. The till band is close to the sediment band,
which is where the honest difficulty lies.
4. **Spatial resolution.** The along-track Fresnel zone at $20\ \mathrm{MHz}$ is
   $r_f = \sqrt{\lambda z/2}$; for $z = 800\ \mathrm{m}$ and
   $\lambda = 8.42\ \mathrm{m}$ this is $58\ \mathrm{m}$. **Claim no resolution
   better than about $60\ \mathrm{m}$** regardless of the trace spacing.
5. **Reporting an intermediate bed.** Report the calibrated reflection
   coefficient **with its uncertainty band**, not a class label: e.g.
   "$\alpha = -0.48 \pm 0.06$, consistent with saturated till or with a
   transitional water content between $0.05$ and $0.15$ by volume in the basal
   layer". A single class label would hide the very case — a thin water film over
   a rough bed, or a partly drained dilatant till — that a geophysical survey is
   most often asked about, and the calibration cannot separate those from the
   amplitude alone. The additional measurement that would is a comparison with a
   borehole or a seismic reflection coefficient at one point, which anchors the
   absolute calibration for the whole profile.
