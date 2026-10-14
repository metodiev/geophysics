# Solutions — 05-05-04 Positioning with GNSS/DGPS and Static Corrections

> **Read this after attempting the exercises, not before.**

---

## ★1 — The free-air gradient

$g(z) = GM/(a+z)^{2}$, so $\mathrm{d}g/\mathrm{d}z = -2GM/(a+z)^{3} = -2g/(a+z)
\approx -2g/a$ for $z \ll a$.

Numerically:

$$\frac{2 \times 9.80665}{6.371\times10^{6}} = 3.0785\times10^{-6}\ \mathrm{s^{-2}}
= \frac{3.0785\times10^{-6}}{10^{-5}} = \boxed{0.30785\ \mathrm{mGal\,m^{-1}}}.$$

This matches the lesson's printed value exactly, and confirms that the often-quoted
0.3086 mGal/m differs by about 0.25 % because it is evaluated with a different $g$
and radius.

---

## ★2 — Height error to gravity error

Using $\delta g = 0.30785\,\delta z$ mGal:

| $\delta z$ (m) | $\delta g$ (mGal) |
|---|---|
| 0.01 | 0.0031 |
| 0.5 | 0.1539 |
| 5.0 | 1.539 |

Note that 5 m of height error exceeds the total anomaly of most detailed surveys.

---

## ★3 — The three heights

$$h = H + N,$$

with $h$ the ellipsoidal height (measured directly by GNSS), $H$ the orthometric
height above the geoid, and $N$ the geoid undulation. **GNSS measures $h$.**

---

## ★4 — Maximum horizontal gradient

$\left|\partial g/\partial x\right|_{\max} = 0.8587\,g^{\max}/h
= 0.8587 \times 0.20/400 = \boxed{4.29\times10^{-4}\ \mathrm{mGal\,m^{-1}}}$, at
$x = h/2 = 200$ m from the centre.

---

## ★5 — Averaging out or not

- **Averages out:** GNSS random noise. It is zero-mean and independent between
  occupations, so the standard error of $N$ occupations falls as $1/\sqrt{N}$.
- **Does not average out:** a vertical datum (geoid model) error, or a mis-taped
  instrument pole. Both are the *same* bias at every occupation, so repeating
  measures the bias more precisely rather than removing it.

---

## ★★6 — Vertical and horizontal requirements

**(a)** $0.20 \times 0.08 = 0.016$ mGal allowed for positioning, so

$$\delta z \le \frac{0.016}{0.30785} = \boxed{0.052\ \mathrm{m}}\quad (\text{RTK class}).$$

**(b)** $4.29\times10^{-4}$ scaling to $h = 500$ and $g^{\max} = 0.08$:
$0.8587 \times 0.08/500 = 1.374\times10^{-4}$ mGal/m, so

$$\delta x \le \frac{0.016}{1.374\times10^{-4}} = \boxed{116\ \mathrm{m}}.$$

**(c)** The **vertical** requirement binds, by a factor of about
$116/0.052 \approx 2200$ in the accuracy needed. This is the lesson's central
practical result: for gravity, vertical positioning dominates by orders of
magnitude, because the free-air gradient is large while horizontal gradients of
gravity anomalies are gently sloped.

---

## ★★7 — A microgravity monitoring budget

**(a)** $\delta z = 0.002$ m → $0.002 \times 0.30785 = \boxed{0.000616\ \mathrm{mGal}}$.

**(b)** $\left|\partial g/\partial x\right|_{\max} = 0.8587 \times 0.5/100
= 4.29\times10^{-3}$ mGal/m; with $\delta x = 0.005$ m →
$\boxed{0.0000215\ \mathrm{mGal}}$.

**(c)** The **vertical** term dominates, by a factor $0.000616/0.0000215 = 28.6$.
Both are far below the 0.015 mGal 4-D signal, so this design is adequate; but the
implication is that re-occupation monument stability and height measurement, not
horizontal positioning, set the achievable 4-D resolution. A monument that settles by
1 cm produces a spurious 0.0031 mGal signal — 21 % of the target signal.

---

## ★★8 — A shallow magnetic dyke

**(a)** $2/50 = \boxed{0.04\ \mathrm{m}}$ — 4 cm horizontal.

**(b)** **RTK only.** DGPS at 0.5 m would contribute 25 nT, twelve times the allowed
2 nT.

**(c)** $\pm 1$ cm of pole height → $0.01 \times 0.30785 = 0.0031$ mGal. For a
*magnetic* survey this term does not apply at all: the magnetic field has no direct
dependence on height of that form, so the relevant height error is the *gradient*
term $\partial B/\partial z \cdot \delta z$, which is a different (and usually much
smaller) number. The lesson's table makes this explicit: the same 0.5 m error costs
0.154 mGal for gravity and nothing directly for magnetics; the magnetic requirement
comes from the horizontal gradient.

---

## ★★9 — A survey with 0.02 mGal repeatability and 3 m of height error

**(a)** Both can be true because they measure different things.
**Repeatability** measured from repeated occupations of *one* station cancels any
constant bias affecting that station — including a height error, if the same wrong
height is used every time. The survey's *accuracy* is limited by the (spatially
varying) height error across stations, which the repeat test does not probe.

**(b)** $\delta g = 3 \times 0.30785 = 0.9236$ mGal from height alone. In quadrature
with the 0.02 mGal repeatability (and any terrain term), the realistic threshold is
$3\sigma \approx$ 2.8 mGal if the height error is random, or 0.92 mGal if it is a
bias. Either way, two orders of magnitude worse than the quoted 0.02 mGal.

**(c)** A **repeat of a whole line, or of a set of stations spread across the survey
area, with the field heights re-measured independently** (for example by differential
levelling or by a separate GNSS occupation). The bias would appear as a reproducible
spatial pattern; a single-station repeat occupation cannot reveal it.

---

## ★★★10 — The quadratic term

Write the anomaly about the nominal position as
$g(x_0+\delta) = g(x_0) + g'(x_0)\delta + \tfrac12 g''(x_0)\delta^{2} + \dots$.

For the point-mass profile, at the location of the maximum horizontal gradient
($x = h/2$) we have $g'(h/2) = -0.8587\,g^{\max}/h$ (magnitude) and

$$g''(x) = \frac{3GMh\,(4x^{2}-h^{2})}{(x^{2}+h^{2})^{7/2}},$$

which at $x = h/2$ vanishes, so at the *steepest point* the quadratic term is zero to
leading order. The quadratic term is largest, relative to the linear term, at the
inflection-free locations where $g'$ is small — i.e. near the peak and near the tails.
Evaluating at $x = 0$: $g'(0) = 0$ and $g''(0) = -3GM/h^{4}$, so the error there is
purely quadratic, $-\tfrac32 GM\delta^{2}/h^{4}$, and the *linear* estimate is zero —
hence the linear estimate is not merely a lower bound, it is qualitatively wrong at
the peak.

**Where the quadratic reaches 10 % of the linear term:** at $x = h/4$,
$g'(h/4) = -0.6450\,GM/h^{3}$ and $g''(h/4) = -1.8188\,GM/h^{4}$, so the ratio of the
second-order to the first-order term is

$$\frac{\tfrac12 g''\delta^{2}}{g'\delta} = \frac{1.8188}{2 \times 0.6450}\cdot
\frac{\delta}{h} = 1.410\,\frac{\delta}{h} = 0.10
\ \Longrightarrow\ \delta = 0.071\,h .$$

For $h = 100$ m that is 7.1 m of mislocation — far beyond any realistic GNSS error.
**The linear estimate of equation (1) is therefore adequate for a deep body, and the
case to watch is the very shallow, steep-gradient anomaly where the peak error is
purely quadratic and the linear estimate simply fails to see it.**

---

## ★★★11 — Correlated positioning error

A satisfactory experiment samples a random walk for the horizontal error, converts it
to an anomaly error via the measured gradient profile, and reports:

- with a **short** correlation length the error looks like noise: it raises the
  misfit of any model but does not invent coherent structure;
- with a correlation length **comparable with the anomaly width** the error becomes a
  smooth, low-amplitude, spatially coherent perturbation — indistinguishable in
  character from a real anomaly;
- **why it is more dangerous:** coherent error survives averaging, survives
  smoothing, and is *attributed to geology*. The quantitative test for it is a
  *repeat* of the whole profile with independently determined positions; if the
  perturbation does not repeat, it is positioning; if it does, it may be either real
  or a systematic position error, and only independent positioning resolves the
  ambiguity.

---

## ★★★12 — Bias, random and tilt

A satisfactory answer constructs a synthetic height field
$z_i = z_{\text{true},i} + \delta z_0 + \eta_i + \alpha x_i$, converts each component
to an anomaly error with 0.30785 mGal/m, and reports three error maps:

| component | appearance in the anomaly map | detectable by repeating? |
|---|---|---|
| constant bias $\delta z_0$ | a constant offset over the whole survey | no |
| random $\eta_i$ | scatter, raised misfit | yes, reduced as $1/\sqrt{N}$ |
| tilt $\alpha x$ | a long-wavelength gradient, resembling a regional trend or a deep source | no |

The **bias and tilt cannot be detected by repeating**, because they are identical on
every occupation. A **base station** at a site with an independently known height
detects both: the residual after correcting to the base reveals the bias, and two
bases far apart reveal the tilt. This is the potential-field analogue of the loop
closure in [05-05-05](../05-quality-control.md).
