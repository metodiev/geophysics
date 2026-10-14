# Solutions — 07-01-05 Units (Gal, mGal), Absolute vs Relative Measurement

> **Read after attempting the exercises.** Numbers were computed, not estimated.

Lesson: [05 Units (Gal, mGal), Absolute vs Relative Measurement](../05-gravity-units-and-instruments-relative.md).

---

## ★1 — Unit conversions

Conversions used throughout: multiply $\mathrm{m\,s^{-2}}$ by $10^{2}$ for Gal,
$10^{5}$ for mGal and $10^{8}$ for µGal.

| input | $\mathrm{m\,s^{-2}}$ | Gal | mGal | µGal |
|---|---|---|---|---|
| $9.820250$ | $9.820250$ | $9.820250\times10^{2}$ | $9.820250\times10^{5}$ | $9.820250\times10^{8}$ |
| $2.50\times10^{-7}$ | $2.50\times10^{-7}$ | $2.50\times10^{-5}$ | $2.50\times10^{-2}$ | $25.0$ |
| $0.00450$ Gal | $4.50\times10^{-5}$ | $4.50\times10^{-3}$ | $4.50$ | $4.50\times10^{3}$ |

**Which is a realistic survey signal?** (b): $25.0\ \mathrm{\mu Gal}$ is a
microgravity-scale signal (a small cavity, a subsidence change, or a very small
residual). (c) at $4.50\ \mathrm{mGal}$ is a strong local anomaly. (a) is the whole
field, not a signal. The lesson's working range is roughly $0.01$ to
$100\ \mathrm{mGal}$ for exploration and $1$ to $50\ \mathrm{\mu Gal}$ for
microgravity.

---

## ★2 — Mass, elevation and density equivalences

**(a) Mass at 1 m.** $g = GM/r^{2}$ with $r = 1$ m and $g = 10^{-5}\
\mathrm{m\,s^{-2}}$:

$$M = \frac{gr^{2}}{G} = \frac{10^{-5}\times1}{6.67430\times10^{-11}}
= 1.49828\times10^{5}\ \mathrm{kg} \approx 150\ \mathrm{tonnes}.$$

So a milligal is what a $150\ \mathrm{t}$ mass produces at one metre: an
instrument that resolves this is a metrological device, not a field toy.

**(b) Elevation.** With the model gradient $3.083\times10^{-6}\ \mathrm{s^{-2}}$,

$$h = \frac{10^{-8}}{3.083\times10^{-6}} = 3.2436\times10^{-3}\ \mathrm{m}
= 3.244\ \mathrm{mm}.$$

Note this is a *height* equivalence, independent of the 10 m in the question:
distance from a nearby mass and distance above the ellipsoid are different
geometries. The answer to the question as asked is $3.24\ \mathrm{mm}$ of
elevation, which equals a microgal.

**(c) Density through 50 m.** From $g = 2\pi G\Delta\rho\,h$,

$$\Delta\rho = \frac{10^{-8}}{2\pi G \times 50}
= 0.47692\ \mathrm{kg\,m^{-3}},$$

and the equivalent column mass per unit area is
$\Delta\rho\,h = 10^{-8}/(2\pi G) = 23.846\ \mathrm{kg\,m^{-2}}$. Over a
$1\ \mathrm{m^{2}}$ column the question asks for the mass, so
$23.85\ \mathrm{kg}$ — the same answer for any thickness, which is the point: the
observable is the surface density, not the density.

---

## ★3 — From readings to gravity, and a calibration error

With $c = 10^{-3}\ \mathrm{mGal\,count^{-1}}$, $g_{\text{base}} =
979\,500.0000$ mGal at $R_{0} = 12\,000.0$ counts:

$$g(14\,000) = 979\,500.0000 + 10^{-3}\times2000 = 979\,502.0000\
\mathrm{mGal},$$

$$g(18\,000) = 979\,500.0000 + 10^{-3}\times6000 = 979\,506.0000\
\mathrm{mGal}.$$

With the true calibration $0.9995\times10^{-3}$ the true values are
$979\,501.9990$ and $979\,505.9970$ mGal, so the errors are

$$+0.0010\ \mathrm{mGal} = +1.0\ \mathrm{\mu Gal}
\quad\text{and}\quad
+0.0030\ \mathrm{mGal} = +3.0\ \mathrm{\mu Gal}.$$

The error is proportional to the *span from the base*,
$\Delta c \times \left(R - R_{0}\right)$, not to the reading: the two stations
share the base and therefore share its value. This is why a base tie does not
correct a calibration error, and why the errors grow with distance from the base.

---

## ★★4 — Least-squares calibration on a noiseless six-station set

Design matrix rows $\left(R_{i}, 1\right)$; solving
$\widehat{\mathbf{p}} = \left(A^{T}A\right)^{-1}A^{T}\mathbf{g}$ gives

$$c = 1.000000\times10^{-3}\ \mathrm{mGal\,count^{-1}}, \qquad
b = 979\,490.0000\ \mathrm{mGal},$$

$$g_{i} = 1.000000\times10^{-3}R_{i} + 979\,490.0000.$$

**Residuals:** all six are below $6\times10^{-10}\ \mathrm{mGal}$, i.e.
round-off. A noiseless, exactly linear data set is reproduced exactly, so the
residuals here test the arithmetic, not the model. In a real calibration the
residuals are of the order of the reference-value uncertainty and their *pattern*
(a trend with reading) is the diagnostic of non-linearity.

**What $b$ means physically.** $b$ is the value the model assigns to a reading of
zero counts — an extrapolation far outside the observed range
$10\,000$–$20\,000$ counts. It is not a physical gravity value; it is the
intercept that makes the line fit. That is why it trades so strongly with the
slope: over a narrow span, a change in $c$ can be cancelled by a change in $b$ with
the fitted values barely moving. The lesson's measured correlation of $-0.9565$
quantifies exactly this.

**Check.** $g(15\,000) = 1.000000\times10^{-3}\times15\,000 + 979\,490.0000 =
979\,505.0000$, which is $979\,500 + 10^{-3}\times3000$: consistent with the base
form of the equation. The two forms are equivalent, as they must be, because
$g_{\text{base}} = cR_{0} + b$ with $R_{0} = 10\,000$ here.

---

## ★★5 — Two uncertainty contributions

$$\sigma_{\Delta g}^{2} = \left(\Delta R\right)^{2}\sigma_{c}^{2}
+ 2c^{2}\sigma_{R}^{2}.$$

**Calibration term:**

$$\Delta R\,\sigma_{c} = 4000 \times 4.0\times10^{-7}
= 1.600\times10^{-3}\ \mathrm{mGal} = 1.600\ \mathrm{\mu Gal}.$$

**Reading term:**

$$\sqrt{2}\,c\,\sigma_{R} = \sqrt{2}\times10^{-3}\times0.3
= 4.243\times10^{-4}\ \mathrm{mGal} = 0.4243\ \mathrm{\mu Gal}.$$

**Total:**

$$\sigma_{\Delta g} = \sqrt{1.600^{2} + 0.4243^{2}}
= 1.6553\ \mathrm{\mu Gal},$$

i.e. $0.0414\%$ of the measured difference
$\Delta g = 4000\times10^{-3} = 4.000\ \mathrm{mGal}$.

**Crossover span.** Setting the two terms equal,

$$\Delta R = \frac{\sqrt{2}\,c\,\sigma_{R}}{\sigma_{c}}
= \frac{0.4243\times10^{-3}}{4.0\times10^{-7}} = 1060.7\ \mathrm{counts}.$$

Below about $1060$ counts ($1.06\ \mathrm{mGal}$ of span) the readings limit the
difference; above it the calibration does. Most field surveys work well above the
crossover, which is the quantitative version of the statement that relative
gravimeters are calibration-limited.

---

## ★★6 — A 20 000-count survey, and why repeats would not help

$$\sigma_{c} = 0.02\% \times 10^{-3} = 2.0\times10^{-7}\
\mathrm{mGal\,count^{-1}}, \qquad \Delta R = 20\,000\ \mathrm{counts}.$$

**Calibration term:** $20\,000 \times 2.0\times10^{-7} = 4.000\times10^{-3}\
\mathrm{mGal} = 4.000\ \mathrm{\mu Gal}$.

**Reading term:** $\sqrt{2}\times10^{-3}\times0.3 = 0.4243\ \mathrm{\mu Gal}$.

**Total:** $\sqrt{4.000^{2} + 0.4243^{2}} = 4.0224\ \mathrm{\mu Gal}$.

**Repeats needed to make the reading term irrelevant:** the ratio of the
reading term to the calibration term is $0.4243/4.000 = 0.1061$, so reducing the
reading term by averaging $n$ repeats changes the total as
$\sqrt{16 + 0.180/n}$. Even for $n \to \infty$ the total falls only from
$4.0224$ to $4.0000\ \mathrm{\mu Gal}$ — **$0.6\%$**. Equivalently, the
"number of repeats needed to equalise the terms" is
$\left(0.4243/4.000\right)^{2} = 0.0113 < 1$: the reading term is *already* smaller
than the calibration term with a single reading.

**Conclusion.** No amount of repeating improves this survey. The only improvement
is a better calibration, which requires an independent reference. The general rule:
repeat to make the random term small compared with the systematic term, then stop —
and the systematic term, not the random one, sets what the survey can claim.

---

## ★★★7 — Calibration design for $0.01\%$ slope accuracy (specification)

**Target.** $\sigma_{c}/c \le 10^{-4}$.

**Relation to be used.** For a two-parameter fit with $N$ readings spread evenly
over a span $\Delta R$ and reference values of uncertainty $\sigma_{\text{ref}}$
(the weights being equal), the variance of the fitted slope is

$$\operatorname{var}\left(c\right) = \frac{12\,\sigma_{\text{ref}}^{2}}
{N\,\left(\Delta R\right)^{2}}
\qquad\Longrightarrow\qquad
\sigma_{c} = \frac{\sigma_{\text{ref}}}{\Delta R}\sqrt{\frac{12}{N}},$$

so the slope accuracy improves linearly with the span and only as $1/\sqrt{N}$ with
the number of stations. Rearranged for the design,

$$\Delta R \gtrsim \frac{\sigma_{\text{ref}}}{c\,\left(\sigma_{c}/c\right)}
\sqrt{\frac{12}{N}}.$$

**Design.** With an absolute datum of $\sigma_{\text{ref}} = 5\
\mathrm{\mu Gal} = 5\times10^{-3}\ \mathrm{mGal}$, $N = 12$ stations and a
target relative slope accuracy of $10^{-4}$:

$$\Delta R \gtrsim rac{5	imes10^{-3}}{10^{-3}	imes10^{-4}}
\sqrt{rac{12}{12}} = 5	imes10^{4}\ \mathrm{counts},$$

i.e. a span of at least $50\ \mathrm{mGal}$ of gravity difference. Using
$1\ \mathrm{mGal} = 3.24\ \mathrm{m}$ of elevation, that is a span of about
$160\ \mathrm{m}$ of elevation — comfortably realisable by occupying two stations
at very different heights, but not by a survey on a plain.

**Number of stations and placement.** At least 8–12 stations, distributed over the
span with several repeats at the ends (the ends carry the leverage on the slope),
and residuals checked for curvature. Repeats at intermediate stations mostly
improve the intercept and the residual level, not the slope.

**Predicted correlation.** The $c$–$b$ correlation is
$\rho \approx -\bar{R}/\sqrt{\bar{R}^{2} + \mathrm{var}(R)}$ when $b$ is evaluated
at $R = 0$: it becomes less negative as the span grows relative to the offset of the
readings from zero. The lesson measured $-0.9565$ for a $12\ \mathrm{mGal}$ span
around $12\,000$ counts, i.e. with the readings far from zero; increasing the span
and centring the readings both push $|\rho|$ down.

**Falsification.** Fit the model, then fit a quadratic; if the quadratic term is
significant at the stated uncertainty the linear calibration model is rejected and
the experiment must be redesigned (or the non-linearity modelled). A calibration
report that does not include a curvature test has not tested the assumption it
depends on.

---

## ★★★8 — Network design to $15\ \mathrm{\mu Gal}$ at 20 km (specification)

**Budget.** From the lesson,
$\sigma_{\text{total}} = \sqrt{N\sigma_{\ell}^{2} + \sigma_{\text{abs}}^{2}}$.

**Choose the meter.** For $N = 6$ links, a target of $15\ \mathrm{\mu Gal}$ and a
datum of $\sigma_{\text{abs}} = 5\ \mathrm{\mu Gal}$:

$$N\sigma_{\ell}^{2} = 15^{2} - 5^{2} = 200, \qquad
\sigma_{\ell} = \sqrt{200/6} = 5.77\ \mathrm{\mu Gal}.$$

So a meter with $6\ \mathrm{\mu Gal}$ repeatability suffices, provided the network
is built as six links from the base.

**Placement.** The uncertainty grows as $\sqrt{N}$, so the *number of traverses*
matters, not the distance. The design should therefore tie the 20 km station
directly to the base (one long traverse, $N = 1$, contributing
$6\ \mathrm{\mu Gal}$), rather than stepping through intermediate stations
($N = 6$, contributing $14.7\ \mathrm{\mu Gal}$). If intermediate stations are
required for their own sake, tie each of them back to the base rather than
chaining.

**Number and placement of ties.** One absolute datum at the base, re-occupied
between traverses. Re-occupying the base converts a growing error into a
correlated one: the base value's $\pm 5\ \mathrm{\mu Gal}$ applies to the whole
network, and the random part resets at each re-occupation, so a survey split into
$m$ traverses has $\sigma_{\text{random}} = \sqrt{N/m}\,\sigma_{\ell}$.

**Dominant term.** With the design above, the random term is
$\sqrt{200} = 14.1\ \mathrm{\mu Gal}$ and the datum $5\ \mathrm{\mu Gal}$: the
survey is random-error limited, so the priority is repeats and short traverses, not
a better absolute instrument. With a quieter meter ($2\ \mathrm{\mu Gal}$), the
random term at $N = 1$ is $2\ \mathrm{\mu Gal}$ and the datum dominates — the
priority reverses. The budget decides which, and it must be computed before the
survey, not after.

---

## ★★★9 — Manufacturer claims: $1\ \mathrm{\mu Gal}$ repeatability, $0.01\%$ calibration

**Contributions to a $10\,000$-count difference** with
$c = 10^{-3}\ \mathrm{mGal\,count^{-1}}$:

$$\text{calibration term} = 10\,000 \times \left(0.0001\times10^{-3}\right)
= 1.0\times10^{-3}\ \mathrm{mGal} = 1.0\ \mathrm{\mu Gal},$$

$$\text{reading term} = \sqrt{2}\times10^{-3}\times1\ \mathrm{\mu Gal}
= 1.41\times10^{-3}\ \mathrm{\mu Gal} = 0.0014\ \mathrm{\mu Gal}.$$

**Non-specialist explanation.** The instrument is spectacularly good at repeating
the same number, and that is what the first figure advertises. But a survey is not
a repetition: to compare two places, the instrument's scale must be right, and the
scale is known only through calibration. An error in the scale grows in proportion
to the gravity difference measured: over a $10\ \mathrm{mGal}$ span, $0.01\%$ is
$1\ \mathrm{\mu Gal}$; over a $100\ \mathrm{mGal}$ span it is $10\
\mathrm{\mu Gal}$; over the $5000\ \mathrm{mGal}$ range of the globe it is
$500\ \mathrm{\mu Gal}$. The repeatability figure is therefore a statement about
noise, and the survey's accuracy is set by the scale, i.e. by the second number —
and it degrades with the size of the survey, which is exactly the opposite of what
a user expects from a "better" instrument. The noise can be beaten by repeating
and averaging; the scale error cannot, because repeating the same instrument with
the same wrong scale gives the same wrong answer every time.

**The one experiment that verifies the claim.** Occupy a set of stations whose
gravity differences are known independently — for example, a calibration line
between two absolute stations, tied by both instruments — spanning a range as wide
as the instrument will see in service. Fit $g = cR + b$ to that data, and report:
(i) the residual scatter about the fitted line (this tests the repeatability claim,
once the readings are separated in time and transport); (ii) the fitted slope's
deviation from the nominal value and its uncertainty (this tests the calibration
claim); (iii) the curvature test (a quadratic term) to test linearity. A claim of
$1\ \mathrm{\mu Gal}$ repeatability is verified by (i); a claim of $0.01\%$
calibration can only be verified by (ii) over a span wide enough that $0.01\%$ is
larger than the residual scatter — with $1\ \mathrm{\mu Gal}$ scatter, the span must
exceed $1\ \mathrm{\mu Gal}/(0.0001\times10^{-3}\ \mathrm{mGal\,count^{-1}})
= 10^{4}$ counts, i.e. $10\ \mathrm{mGal}$ of difference or more. If the test span
is narrower than that, the experiment cannot distinguish $0.01\%$ from $0.1\%$, and
the claim is untested.
