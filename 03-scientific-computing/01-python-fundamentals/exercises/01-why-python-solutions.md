# Solutions — 03-01-01 Why Python for Geophysics: The Scientific Ecosystem

> **Read this after attempting the exercises, not before.** Every number
> attributed to a demo is its actual printed output.

---

## ★1 — Mass and peak anomaly

**(a)** $M = \frac{4}{3}\pi a^3 \Delta\rho
= \frac{4}{3}\pi (150)^3 \times 250$.

$(150)^3 = 3.375\times10^{6}$ m³. With $\frac{4}{3}\pi = 4.188790$ (six
significant figures, which is the precision we are carrying by hand):

$$M = 4.188790 \times 3.375\times10^{6} \times 250
= 4.188790 \times 8.4375\times10^{8} = 3.534292\times10^{9}\ \text{kg}.$$

**(b)** $g = GM/z^2 = 6.67430\times10^{-11} \times 3.534292\times10^{9} / 400^2$.

Numerator: $6.67430\times10^{-11} \times 3.534292\times10^{9}
= 2.358892\times10^{-1}$ m³ s⁻².
Divide by $1.6\times10^{5}$ m²: $g = 1.474308\times10^{-6}$ m s⁻².

In mGal: $1.474308\times10^{-6} / 10^{-5} = 0.1474308$ mGal.

Note the two-step unit conversion. $G$ carries m³ kg⁻¹ s⁻², so $M/z^2$ gives the
acceleration directly in SI; the mGal conversion is a *separate* factor of $10^{-5}$
applied last. Doing it in one expression without checking the intermediate SI value
is where sign and factor-of-ten errors enter.

**(c)** `print(sphere_mass(150.0, 250.0))` gives `3534291735.288517`, and
`print(sphere_anomaly_mgal(250.0, 150.0, 400.0, 0.0))` gives
`0.1474307708052259`.

The relative difference from the hand values is $4.9\times10^{-8}$ — five parts in
$10^{8}$ — and it comes entirely from rounding $\frac{4}{3}\pi$ to six digits in
(a). Reporting the discrepancy rather than hiding it is the point: **a hand
calculation is a calibration that is good to the precision you carry it.**

---

## ★2 — Scaling and the half-width

**(a)** For a **fixed mass** and the point-mass form $g = GM/z^2$, doubling $z$
divides the anomaly by four. Answer: $0.147431/4 = 0.036858$ mGal.

The reason in one sentence: the anomaly of a fixed mass falls off as the inverse
square of distance, because the solid angle the mass subtends at the station falls
as $z^{-2}$.

**(b)** `print(sphere_anomaly_mgal(250.0, 150.0, 800.0, 0.0))` gives
`0.036857692701306476`, which is 0.0368577 mGal — exactly one quarter of
0.1474308 mGal to every digit printed. The library keeps the mass fixed fractionally
because the mass is recomputed from $a$ and $\Delta\rho$, which are unchanged. Had
the script instead halved the *radius* as well, the mass would have fallen by a
factor of eight and the comparison would be meaningless.

**(c)** The half-width satisfies

$$(x^2+z^2)^{-3/2} z = \tfrac{1}{2} z^{-2}
\;\Longrightarrow\;
\left(\frac{x}{z}\right)^2 = 2^{2/3} - 1,$$

so $x = z\sqrt{2^{2/3}-1} = 400 \times 0.766279 = 306.57$ m.

The constant is $0.766$ for a sphere. The lesson's demo prints
`= 383.2 m` for its own $z = 500$ m, which is $500 \times 0.766 = 383.1$ m.

The property: **the anomaly profile's width scales with the depth**, so a single
profile determines $z$ once the shape is known. It does *not* determine the shape;
a cylinder of the same depth has a different half-width-to-depth ratio, which is
exercise ★★★9.

---

## ★3 — Layer selection

| Task | Layer | Why the neighbour is wrong |
|---|---|---|
| (a) 10⁸-element array subtraction | NumPy | A `list` of that size is a list of pointers to boxed floats, not a contiguous array; the arithmetic is elementwise and per-element Python overhead dominates |
| (b) Curve fit with uncertainties | SciPy (`scipy.optimize`) | NumPy can do a linear least-squares solve but not the general minimisation, bounds, or parameter covariance machinery |
| (c) miniSEED read and response removal | ObsPy | NumPy has no concept of a miniSEED block or a transfer function; SciPy would have to be told the file format |
| (d) Group-by and mean over a catalogue | pandas | A dict-of-lists can do the grouping (lesson 05) but not typed columns, missing-value semantics, or the fast compiled group-by |
| (e) Annotated anomaly map | PyGMT | Matplotlib can draw it, but projections, coastlines and shaded relief are what GMT exists for |

The rule is by problem *shape*: elementwise → NumPy; an algorithm → SciPy;
a labelled table → pandas; a grid with coordinates → xarray; a map → PyGMT;
a seismic file → ObsPy.

---

## ★4 — The demo's measurements and an extrapolation

**(a)** Mass contrast `M = 1.005310e+10 kg`, peak anomaly `g_z(0) = 0.268390 mGal`.

**(b)** `stations computed : 200,000`, `wall-clock time : 0.034 s`,
`per-station cost : 172 ns`.

**(c)** `Python version used: 3.14.4`.

Extrapolation: $10^{9} \times 172\times10^{-9}$ s $= 172$ s, which is
$172/3600 = 0.0478$ hours — about 2.9 minutes.

Two assumptions, both of which need stating:

1. **The per-station cost is constant.** It is not. The demo's timing is dominated
   by interpreter overhead relative to a small amount of arithmetic, and at 10⁹
   stations cache behaviour, memory traffic and the accumulation of a large float
   total would change the number. A 172 ns per-station figure is calibrated at
   2 × 10⁵, not at 10⁹.
2. **The machine and interpreter are the same.** Timings vary between machines,
   between CPython versions, and between runs on the same machine by tens of per
   cent. The figure is a calibration of *this* instrument, not a property of
   Python.

The honest conclusion: the standard library is adequate at 10⁵–10⁶ stations and
inadequate at 10⁹, and the fix is a vectorised library (module 03-02), not a faster
machine.

---

## ★5 — Station spacing and benchmark realism

**(a)** 200 000 stations over 4 000 m is 20 mm between stations. No survey places
stations 20 mm apart: the measurement is a *potential-field* quantity that varies
smoothly over tens to hundreds of metres, and a gravimeter occupies a station for
a minute. The spacing also implies a survey with 200 000 readings on one line,
which is more than a small commercial campaign.

**(b)** $4000 / (200000 - 1) = 0.020000$ m = 20.000 mm, which the demo prints as
`station spacing : 20.000 mm`. The $(n-1)$ is the number of intervals, the same
convention as a trace's duration in lesson 08.

**(c)** A realistic version:

```python
stations = int(PROFILE_LENGTH / STATION_SPACING) + 1        # 201
start = time.perf_counter()
for i in range(stations):
    x = -PROFILE_LENGTH / 2 + i * STATION_SPACING
    anomaly_mgal(x)
elapsed = time.perf_counter() - start
```

201 stations at roughly 170–200 ns each is about 40 µs — below the resolution of a
single `perf_counter` reading in a busy process, and entirely dominated by timer
noise and the loop setup.

Why it is a worse benchmark: **a measurement shorter than the timer's own
uncertainty measures the timer.** The 200 000-station version is not a realistic
survey, but it is a valid *calibration of per-station cost*, which is what a
benchmark is for. The lesson's rule applies: state the setup and say what the
number is a measurement *of*.

---

## ★6 — Detectability

**(a)** $1\ \mu\text{Gal} = 10^{-6}$ Gal $= 10^{-6} \times 10^{-2}$ mGal
$= 10^{-8}$ mGal. So $10\ \mu\text{Gal} = 10^{-7}$ mGal, and three times that is
$3\times10^{-7}$ mGal.

Careful with the Gal/Milligal/µGal ladder: 1 Gal $= 10^{-2}$ m s⁻², so
1 mGal $= 10^{-5}$ m s⁻² and 1 µGal $= 10^{-8}$ m s⁻².

**(b)** Set $g_{\text{peak}} = GM/z^2 = \frac{4}{3}\pi a^3 \Delta\rho\, G / z^2$.

Target $g = 30\ \mu\text{Gal} = 30 \times 10^{-8}$ m s⁻² $= 3\times10^{-7}$ m s⁻².
With $a = 500$ m and $z = 2000$ m:

$$\frac{4}{3}\pi a^3 = 4.188790 \times 1.25\times10^{8} = 5.235988\times10^{8}\ \text{m}^3,$$

$$\Delta\rho = \frac{g z^2}{G \cdot \frac{4}{3}\pi a^3}
= \frac{3\times10^{-7} \times 4\times10^{6}}
        {6.67430\times10^{-11} \times 5.235988\times10^{8}}
= \frac{1.2}{0.0349509}
= 34.33\ \text{kg m}^{-3}.$$

(Check: at $z = 1000$ m the same radius needs a contrast of
$2.8615$ kg m⁻³ for $0.01$ mGal, and the anomaly scales as
$\Delta\rho/z^2$, so $0.03$ mGal at $z = 2000$ m requires
$2.8615 \times 4 \times 3 = 34.34$ kg m⁻³, matching the value above.)

**(c)** 34 kg m⁻³ against a nominal crustal density of 2670 kg m⁻³ is a
**1.3 per cent contrast**. That is geologically plausible in the sense that such a
contrast exists (a slightly more porous or more mafic body), and *implausible* in
the sense that the interpreter can never be confident the body is there at all:
a 1 per cent density difference could equally be a weathering layer, an elevation
error of a few metres, or a terrain-correction deficiency. Iron is 7874 kg m⁻³, so
the contrast is two orders of magnitude below the physical ceiling — the physical
check passes and the *geological resolution* check fails.

---

## ★7 — Inversion sensitivity

**(a)** From $g = GM z^{-2}$,

$$\frac{\mathrm{d}g}{\mathrm{d}z} = -\frac{2GM}{z^3}
\quad\Longrightarrow\quad
\frac{\mathrm{d}z}{\mathrm{d}g} = -\frac{z^3}{2GM} = -\frac{z}{2g}.$$

Using $z = 400$ m and $g = 0.147431$ mGal:
$|\mathrm{d}z/\mathrm{d}g| = 400/(2 \times 0.147431) = 400/0.294862 = 1356.3$ m per
mGal.

**(b)** $0.5\ \mu\text{Gal} = 5\times10^{-4}$ mGal, so
$\Delta z = 1356.3 \times 5\times10^{-4} = 0.68$ m. Measurement uncertainty is a
sub-metre problem.

**(c)** $g \propto a^3 \Delta\rho / z^2$, so holding $g$ fixed:
$z \propto (a^3 \Delta\rho)^{1/2}$. Then

$$\frac{\Delta z}{z} = \tfrac{1}{2}\left(3\frac{\Delta a}{a} + \frac{\Delta\rho}{\rho}\right)
= \tfrac{1}{2}\left(3 \times 0.10 + 0.20\right) = 0.25.$$

At $z = 400$ m, $\Delta z = 100$ m.

**Conclusion:** the measurement uncertainty contributes 0.7 m and the
geometric/parameter uncertainty contributes 100 m. The parameter uncertainty
dominates by a factor of 150. **No improvement in the gravimeter helps**, which is
the standard reason potential-field depth estimates are quoted as ranges and
cross-checked with an independent method — a borehole, a seismic reflection, or a
joint inversion. This is the single most important number in the exercise set.

---

## ★8 — Instrument specification

A good answer contains, for each property, both a statement and a test. Model
answer in outline:

| Property | Statement | How it is tested |
|---|---|---|
| Specification | Vertical anomaly of a uniform sphere of excess density in a homogeneous half-space: inputs $a$, $\Delta\rho$, $z$, $x$; output in mGal | Dimensional analysis of (1); the docstring's parameter list |
| Calibration | The point-mass limit; a known mass gives a known anomaly | Compare with a hand value at $x = 0$; the library's self-test asserts `0.268 ± 0.002` for a known case |
| Precision | `float64` throughout; roughly 16 significant digits; the mGal output near 0.27 mGal has an ulp of about $6\times10^{-17}$ mGal | Print `math.ulp(g)`; compare two algebraically equivalent orderings of (1) |
| Failure mode | Not detected: zero or negative radius; zero or negative depth; zero or negative density; `x` with the wrong type; a complex input | Feed each and observe: **all are accepted silently except the type error** |
| Cost | 172 ns per station for one square root and four multiplications | `time.perf_counter` over $2\times10^{5}$ stations, repeated |

The three undetected input classes are the interesting column. A negative depth is
*algebraically* legal in (1) because only $z^2$ and a single $z$ appear — so the
code returns a *negative* anomaly for a source above the surface, which is
physically wrong (the body would be above the station; the vertical component
above a mass is positive and the formula's geometry no longer applies). A zero
density returns zero, which is legitimate. A zero radius returns zero, legitimate.
A negative radius returns a *negative* mass, which is not a body at all. The
proper fixes are the validation discipline of lesson 07: raise on non-physical
inputs, and do not attempt to be clever about the rest.

---

## ★★★9 — Sphere versus cylinder

**Prediction, before coding.** The cylinder's anomaly is

$$g_{\text{cyl}}(x) = 2\pi G a^2 \Delta\rho \frac{z}{x^2+z^2},$$

which falls off as $x^{-2}$ for large $x$, whereas the sphere's falls off as
$x^{-3}$. A *slower* decay means more of the anomaly survives far from the axis,
so the cylinder's mean over a fixed long line should be **larger** relative to its
peak than the sphere's. A two-dimensional body's anomaly is broader than a
three-dimensional body's at the same depth — the standard reason a 2-D model
over-estimates the depth needed to explain a given width.

**Test.** Implementing both over the same 4 km line with $a = 200$ m, $z = 500$ m
and $\Delta\rho = 300$ kg m⁻³ gives:

| Quantity | Sphere | Horizontal cylinder |
|---|---|---|
| Peak anomaly (mGal) | 0.268390 | 1.006461 |
| Mean over the 4 km line (mGal) | 0.065094 | 0.333594 |
| Mean / peak | 0.2426 | 0.3315 |

The cylinder's peak is about 3.75 times the sphere's — expected, since a horizontal
cylinder of 200 m radius holds far more mass per unit length than a sphere of the
same radius. The comparison that tests the prediction is the last row: the
cylinder's mean-to-peak ratio is 0.3315 against the sphere's 0.2426, so the
cylinder's anomaly is **broader relative to its peak**, exactly as predicted from
its slower $x^{-2}$ decay.

State the result as a ratio and say whether the prediction held. The method point
is the one to carry forward: **a prediction made before coding is a test; an
observation made after coding is a description.**
