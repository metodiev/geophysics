# Solutions — 12-01-02 Crustal Structure and Continental vs Oceanic Crust

Worked solutions for
[02-crustal-structure-exercises.md](./02-crustal-structure-exercises.md). The
lesson is
[02 Crustal Structure and Continental vs Oceanic Crust](../02-crustal-structure.md).
All models are **SYNTHETIC**.

---

## ★ Foundational

### ★1 — A two-layer refraction, computed

With $v_1 = 6.20$, $v_2 = 8.10\ \mathrm{km\,s^{-1}}$, $H = 32.0\ \mathrm{km}$:

$$\sqrt{v_2^2 - v_1^2} = \sqrt{65.61 - 38.44} = \sqrt{27.17}
= 5.2125\ \mathrm{km\,s^{-1}}.$$

**(a)** $t_i = \dfrac{2H\sqrt{v_2^2-v_1^2}}{v_1v_2}
= \dfrac{64.0 \times 5.2125}{6.20 \times 8.10} = \dfrac{333.60}{50.22}
= 6.643\ \mathrm{s}.$

**(b)** $x_c = \dfrac{2Hv_1}{\sqrt{v_2^2-v_1^2}}
= \dfrac{64.0 \times 6.20}{5.2125} = 76.12\ \mathrm{km}.$

**(c)** $x_\times = \dfrac{t_i}{1/v_1 - 1/v_2}
= \dfrac{6.643}{0.161290 - 0.123457} = \dfrac{6.643}{0.037833}
= 175.58\ \mathrm{km}.$

**(d)** $H = \dfrac{t_i v_1 v_2}{2\sqrt{v_2^2-v_1^2}}
= \dfrac{6.90 \times 50.22}{10.425} = 33.24\ \mathrm{km}.$

The reported thickness is 1.24 km too large (3.9 %) for a 3.9 % long intercept:
as the lesson stresses, $H \propto t_i$ at fixed velocities, so an intercept error
passes through one-for-one.

### ★2 — Poisson's ratio and its sensitivity

$$\nu = \frac{k^2-2}{2(k^2-1)}:$$

| $k$ | $k^2$ | $k^2-2$ | $2(k^2-1)$ | $\nu$ |
|---|---|---|---|---|
| 1.70 | 2.8900 | 0.8900 | 3.7800 | 0.23545 |
| 1.73 | 2.9929 | 0.9929 | 3.9858 | 0.24911 |
| 1.80 | 3.2400 | 1.2400 | 4.4800 | 0.27679 |

At $k = 1.73$, a 1 % change in $k$ (to 1.7473) gives
$\nu = 0.25646$, so

$$\Delta\nu = 0.25646 - 0.24911 = 0.00735 \quad \text{per 1 % of } k.$$

**Blunt, not sensitive.** A change of 0.03 in $\nu$ — about the resolution of a
careful study — needs a 4 % change in $k$, which is comparable to the whole
anisotropy signal in the crust. $\nu$ is therefore useful for a coarse
porosity/saturation split and for consistency checks, not for identifying a rock
type from a single value.

### ★3 — A three-layer column and a wrong depth conversion

| layer | $h$ (km) | $v_p$ (km s$^{-1}$) | $h/v_p$ (s) |
|---|---|---|---|
| sediment | 1.5 | 2.50 | 0.600 |
| upper crust | 14.0 | 6.00 | 2.333 |
| lower crust | 16.0 | 6.70 | 2.388 |
| **total** | **31.5** | — | **5.321** |

Harmonic-mean velocity $= 31.5/5.321 = 5.9195\ \mathrm{km\,s^{-1}}$ — *lower*
than the arithmetic mean of 5.067? Then check: the arithmetic mean is
$(2.50+6.00+6.70)/3 = 5.067$, which is *smaller* than the harmonic mean of the
*thickness-weighted* column. This is the point to be careful about: the relevant
comparison is not between the harmonic mean and the unweighted arithmetic mean of
three numbers, but between $1/\langle 1/v\rangle$ and $\langle v\rangle$ **weighted
by thickness**:

$$\langle v\rangle_h = \frac{1.5\times 2.50 + 14\times 6.00 + 16\times 6.70}{31.5}
= \frac{3.75 + 84.0 + 107.2}{31.5} = \frac{194.95}{31.5}
= 6.189\ \mathrm{km\,s^{-1}},$$

which is indeed larger than the harmonic mean 5.9195. The rule holds: for a
fixed thickness weighting, the harmonic mean is always the smaller, and it is the
one that gives the right travel time.

Depth from a $6.00\ \mathrm{km\,s^{-1}}$ conversion:

$$z = v t = 6.00 \times 5.321 = 31.93\ \mathrm{km},$$

i.e. **+0.43 km** (1.4 %) on the true 31.5 km. Small here, because the sediment
carries only 11 % of the time; compare the lesson's oceanic column, where the
water carries 66 % and the same kind of mistake costs 14 km.

---

## ★★ Applied

### ★★4 — Propagating a 30 ms intercept error

At fixed velocities, $H = t_i v_1 v_2/(2\sqrt{v_2^2-v_1^2})$, so

$$\sigma_H = \sigma_{t_i}\frac{v_1 v_2}{2\sqrt{v_2^2-v_1^2}}
= 0.030 \times \frac{50.22}{10.425} = 0.030 \times 4.817
= 0.145\ \mathrm{km}.$$

The lesson's Monte Carlo gives 0.201 km — **1.39 times larger**. The extra
contributes because the Monte Carlo does *not* fix the velocities: it fits $v_1$
from the direct branch and $v_2$ from the head branch, and each fitted velocity
carries its own error into $H$. That propagation is not independent: Section 3.1
of the lesson measures $\mathrm{corr}(H,v_1) = +0.915$, so the two errors add
nearly coherently rather than in quadrature. The moral is the usual one — a
partial-derivative error estimate is exact only for the parameter set you held
fixed, and it understates the answer whenever the fit adjusts other parameters.

### ★★5 — Airy compensation of a plateau and of an ocean

Take $\rho_c = 2.85$, $\rho_m = 3.32$, $\rho_w = 1.03\ \mathrm{g\,cm^{-3}}$,
$T_0 = 30\ \mathrm{km}$.

**(a)** Plateau, $h = 2\ \mathrm{km}$:

$$r = h\frac{\rho_c}{\rho_m - \rho_c} = 2 \times \frac{2.85}{0.47}
= 2 \times 6.0638 = 12.13\ \mathrm{km},$$

so the crust there is $T_0 + h + r = 30 + 2 + 12.13 = 44.13\ \mathrm{km}$.

**(b)** Ocean, $d = 3.5\ \mathrm{km}$:

$$\delta T = d\frac{\rho_m-\rho_w}{\rho_m-\rho_c} = 3.5 \times
\frac{2.29}{0.47} = 3.5 \times 4.8723 = 17.05\ \mathrm{km},$$

leaving $30 - 17.05 = 12.95\ \mathrm{km}$ of crust. Note the asymmetry: 2 km of
*positive* relief needs 12.1 km of root, while 3.5 km of *negative* relief needs
17.1 km of thinning, because water is much lighter than rock and therefore
removes less load per kilometre than rock adds.

### ★★6 — Equivalent gravity sources

Use $g = \frac{4}{3}\pi G \Delta\rho\, a^3/d^2$ with
$g = 20\ \mathrm{mGal} = 2.0\times10^{-4}\ \mathrm{m\,s^{-2}}$, $G = 6.674\times
10^{-11}$ SI.

**(a)** A sphere of $a = 4\ \mathrm{km} = 4\times10^{3}$ m at $d = 8\ \mathrm{km}$:

$$\Delta\rho = \frac{g\,d^2}{\frac{4}{3}\pi G a^3}
= \frac{2.0\times10^{-4} \times (8.0\times10^{3})^2}
{\frac{4}{3}\pi \times 6.674\times10^{-11} \times (4.0\times10^{3})^3}
= \frac{1.28\times10^{4}}{1.790\times10^{-1}}
= 7.154\times10^{4}\ \mathrm{kg\,m^{-3}} = 0.715\ \mathrm{g\,cm^{-3}}.$$

**(b)** The same size at $d = 16\ \mathrm{km}$: since
$\Delta\rho \propto d^2$ at fixed $a$ and $g$,

$$\Delta\rho = 0.715 \times \left(\frac{16}{8}\right)^2
= 0.715 \times 4 = 2.862\ \mathrm{g\,cm^{-3}}.$$

That is larger than any plausible rock contrast (and larger than the density of
the mantle rocks involved), so this equivalent source is **physically
inadmissible**: the arithmetic of equivalence allows it, the geology does not.
This is the practical use of non-uniqueness — it prunes the family.

**(c)** Keeping $a/d = 1/2$ fixed, so $a = 8\ \mathrm{km}$ at $d = 16\ \mathrm{km}$:
now $\Delta\rho \propto d^2/a^3 \propto 1/d$, so

$$\Delta\rho = 0.715/2 = 0.358\ \mathrm{g\,cm^{-3}},$$

which is perfectly admissible. **The data cannot tell (a) from (c)**: both produce
exactly 20 mGal at every station on the profile, because gravity measures only the
single combination $\Delta\rho\,a^3/d^2$. Additional data with a different
geometric weighting — a seismic reflection from the top of the body, a density
log, or a higher derivative of the field — are required, and that is the subject
of ★★★10.

### ★★7 — Ps delay inverted with the wrong $k$

With $H = 32.0\ \mathrm{km}$, $v_p = 6.20\ \mathrm{km\,s^{-1}}$,
$v_s = 3.60\ \mathrm{km\,s^{-1}}$, $p = 0.060\ \mathrm{s\,km^{-1}}$
(so the true $k = 6.20/3.60 = 1.7222$):

$$q_p = \sqrt{1/6.20^2 - 0.060^2} = \sqrt{0.026015 - 0.003600}
= \sqrt{0.022415} = 0.149717,$$
$$q_s = \sqrt{1/3.60^2 - 0.060^2} = \sqrt{0.077160 - 0.003600}
= \sqrt{0.073560} = 0.271220,$$
$$\Delta t_{Ps} = 32.0 \times (0.271220 - 0.149717) = 32.0 \times 0.121503
= 3.888\ \mathrm{s}.$$

Inverting with the correct $k$ returns $H = 32.0\ \mathrm{km}$, as it must.
With wrong assumptions:

| assumed $k$ | implied $v_s$ (km s$^{-1}$) | $H$ (km) | error |
|---|---|---|---|
| 1.65 | 3.758 | 35.49 | +3.49 |
| 1.7222 (correct) | 3.600 | 32.00 | 0.00 |
| 1.78 | 3.483 | 29.67 | −2.33 |

**Direction of the bias.** A $k$ that is assumed *too small* forces $v_s$ too
large, which shrinks $(q_s - q_p)$ and requires a *larger* $H$: the depth is
biased **up**. In the refraction case a velocity assumed *too large* also biases
the depth **up** (lesson Section 3.2). So the signs agree for these two particular
mistakes, and a survey that made both would push its depth estimate high by
several kilometres while every internal consistency check still passed. Biases
in the same direction are the most dangerous kind, because they do not show up as
scatter.

---

## ★★★ Research-oriented

### ★★★8 — The exact $H$–$v_1$ trade-off

From $t_i = 2H\sqrt{v_2^2-v_1^2}/(v_1v_2)$, hold $v_2$ and $t_i$ fixed and
differentiate logarithmically:

$$\ln t_i = \ln 2 + \ln H + \tfrac{1}{2}\ln(v_2^2-v_1^2) - \ln v_1 - \ln v_2,$$
$$0 = \frac{\delta H}{H} + \frac{1}{2}\frac{-2v_1\,\delta v_1}{v_2^2-v_1^2}
- \frac{\delta v_1}{v_1},$$
$$\frac{\delta H}{\delta v_1} = H\left[\frac{v_1}{v_2^2-v_1^2} + \frac{1}{v_1}\right]
= \frac{H v_2^2}{v_1\left(v_2^2-v_1^2\right)}.$$

For $H = 32.0$, $v_1 = 6.20$, $v_2 = 8.10$:

$$\frac{\delta H}{\delta v_1} = \frac{32.0 \times 65.61}{6.20 \times 27.17}
= \frac{2099.5}{168.45} = 12.46\ \mathrm{km\ per\ km\,s^{-1}}.$$

So a 3 % error in $v_1$ (0.186 km s$^{-1}$) is traded against
$0.186 \times 12.46 = 2.32\ \mathrm{km}$ of depth with **no change in any arrival
time** — 7 % of the layer thickness, from a 3 % velocity mistake. This is why a
refraction line that never records the direct branch cannot be inverted for
thickness at all: it measures $t_i$ and $v_2$ but has no handle on $v_1$.

**Effect of a 5 km borehole.** A borehole that logs $v_1$ to ±1 % (i.e. ±0.062
km s$^{-1}$) reduces the depth ambiguity to
$0.062 \times 12.46 = 0.77\ \mathrm{km}$, a factor of 3 improvement over the 3 %
case. Boreholes do not remove the trade-off — they *shrink* it to the size of the
logging error times 12.5 km per km s$^{-1}$. The trade-off factor is the thing to
report.

### ★★★9 — A survey that measures a Moho depth without assuming a velocity

The requirement "to better than 2 %" and "without assuming a velocity" cannot be
met by travel times alone, because $H \propto 1/\sqrt{v_2^2-v_1^2}$ and $v_1$,
$v_2$ are themselves fitted from the same times. The design must therefore
include an observable that measures a **velocity** independently of a travel
time, or a **depth** independently of a velocity.

**Design.** A 120 km refraction profile with 100 m receiver spacing (an array,
not a single line of 10 km-spaced shots), shots at 0, 20, 60 and 120 km, plus a
small-aperture array at the far end to measure **apparent velocities across the
array**. The apparent-velocity measurement gives $v_1$ and $v_2$ from *moveout
across the array*, which is a local differential measurement and therefore far
less sensitive to the absolute time origin and to shallow statics than a slope
fitted to the whole branch.

**Forward model:** the two-layer head-wave equations of the lesson, plus a
linear velocity gradient in the basement, fitted by least squares to (i) the
direct-time branch, (ii) the head-time branch, and (iii) the two array
apparent-velocity curves.

**Well determined:** $v_2$ (from the head-branch slope and from array moveout,
two independent estimates) and $t_i$; expected $v_2$ error below 0.5 %.

**Trades off:** $H$ against $v_1$, with the trade factor
$\delta H/\delta v_1 = 12.5\ \mathrm{km}$ per km s$^{-1}$ from ★8. If the array
apparent velocity pins $v_1$ to 1 % (±0.062 km s$^{-1}$), the depth error from the
trade-off is 0.77 km on 32 km = **2.4 %**, marginally short of the 2 % target;
adding a coincident converted-phase measurement (a Ps delay, which constrains
$H(q_s-q_p)$ with a different dependence on the velocities) brings it under 1.5 %
by breaking the trade-off in a second direction.

**Quantitative prediction:** depth uncertainty $\approx$
$\sqrt{(0.045\ \mathrm{km})^2 + (0.77\ \mathrm{km})^2} = 0.77\ \mathrm{km}$
(2.4 %) with refraction alone, and about 0.4 km (1.3 %) with the converted phase
added, dominated in both cases by the velocity term — which is the design
conclusion: **spend the budget on velocity, not on more offsets.**

### ★★★10 — Resolving the depth ambiguity with derivatives

Let the anomaly be that of a point mass $m$ at depth $d$:

$$g(x) = G m\,\frac{d}{\left(x^2+d^2\right)^{3/2}}.$$

Hold the **peak amplitude** fixed at $g(0) = Gm/d^2$, since both candidate bodies
were fitted to the same anomaly. Then $m \propto d^2$, and

- the maximum horizontal gradient,
  $\left|\partial g/\partial x\right|_\text{max} \propto m/d^{3}
  \propto 1/d$;
- the second horizontal derivative at the anomaly centre,
  $\left|\partial^2 g/\partial x^2\right|_{x=0} = 3Gm/d^{4} \propto 1/d^{2}$.

So the power of $d$ is **−1 for the first derivative and −2 for the second**, at
fixed amplitude. (If instead the mass is held fixed, the powers become $d^{-3}$
and $d^{-4}$; the difference between the two conventions is exactly the
amplitude normalisation, and quoting a power without saying which quantity is
held fixed is a common source of confusion.)

**Factors for $d = 15\ \mathrm{km}$ against $d = 5\ \mathrm{km}$:** the
first-derivative signal is 3 times smaller, the second-derivative signal 9 times
smaller. Working it out explicitly with $g(0) = 10^{-4}\ \mathrm{m\,s^{-2}}$:

| quantity | $d = 5$ km | $d = 15$ km | ratio |
|---|---|---|---|
| mass $m$ (kg) | $3.75\times10^{13}$ | $3.37\times10^{14}$ | 9.0 |
| $\max\lvert g'\rvert$ (s$^{-2}$) | $1.72\times10^{-8}$ | $5.72\times10^{-9}$ | 3.0 |
| $\lvert g''(0)\rvert$ (m$^{-1}$s$^{-2}$) | $1.20\times10^{-11}$ | $1.33\times10^{-12}$ | 9.0 |

**The measurement to propose:** a high-resolution horizontal-gradient or
gravity-gradiometry survey. The horizontal gradient must be measured to about
$6\times10^{-9}\ \mathrm{s^{-2}}$ (5.7 Eötvös, since
$1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$) to detect the deeper body, and the
*ratio* of the second derivative to the peak amplitude distinguishes the two
cases by a factor of 9 — a comfortable margin if the near-surface noise permits
differentiation, which is precisely what gradiometers exist for. The lesson's
non-uniqueness is exact for potential fields sampled at a single level; it is
weakened, not broken, by measuring the field's shape.

---

## Mastery checkpoint — worked version of parts (a)–(c)

> Direct branch slope $0.1580\ \mathrm{s\,km^{-1}}$; head branch slope
> $0.1235\ \mathrm{s\,km^{-1}}$; intercept $2.05\ \mathrm{s}$.

**(a) Velocities and thickness.**
$v_1 = 1/0.1580 = 6.329\ \mathrm{km\,s^{-1}}$ and
$v_2 = 1/0.1235 = 8.097\ \mathrm{km\,s^{-1}}$. Then

$$\sqrt{v_2^2-v_1^2} = \sqrt{65.564 - 40.058} = \sqrt{25.507}
= 5.0505\ \mathrm{km\,s^{-1}},$$
$$H = \frac{2.05 \times 6.329 \times 8.097}{2 \times 5.0505}
= \frac{105.05}{10.101} = 10.40\ \mathrm{km}.$$

**(b) Crossover and first arrival at 60 km.**

$$x_\times = \frac{t_i}{1/v_1 - 1/v_2} = \frac{2.05}{0.1580 - 0.1235}
= \frac{2.05}{0.0345} = 59.42\ \mathrm{km}.$$

At 60 km the offset is just past the crossover, so the **head wave** is the first
arrival — but only by 0.02 s, so the two arrivals interfere and amplitude, not
time, determines what can be picked. The critical distance is
$x_c = 2 \times 10.40 \times 6.329/5.0505 = 26.07\ \mathrm{km}$, where the head
wave first exists.

**(c) Ps delay for $k = 1.72$.** $v_s = 6.329/1.72 = 3.680\ \mathrm{km\,s^{-1}}$,
$p = 0.060\ \mathrm{s\,km^{-1}}$:

$$q_p = \sqrt{1/6.329^2 - 0.060^2} = \sqrt{0.024964 - 0.003600} = 0.146164,$$
$$q_s = \sqrt{1/3.680^2 - 0.060^2} = \sqrt{0.073854 - 0.003600} = 0.265054,$$
$$\Delta t_{Ps} = 10.40 \times (0.265054 - 0.146164) = 10.40 \times 0.118890
= 1.237\ \mathrm{s}.$$

**(d)** A systematic error that biases *every* depth the same way is any error in
the common time base — a sample-rate error, an unresolved instrument delay, or a
datum/elevation error — because all three methods convert a *time* to a *depth*
with a velocity: a common timing stretch makes each measured time longer and each
depth larger. An error that does *not* act in a common direction is a wrong
assumed $k$ (it touches only the converted-phase depth), a wrong density contrast
(only the gravity/root interpretation), or a wrong near-surface velocity (only the
method whose raypath traverses that layer).
