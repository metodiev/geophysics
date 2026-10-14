# Solutions — 14-04-02 Landfill Investigation and Leachate Mapping

> Read after attempting. Lesson:
> [02 Landfill Investigation and Leachate Mapping](../02-landfill-investigation.md).
> All models **SYNTHETIC**.

---

## ★1 — Dupuit mound

$$\Delta h_\text{max} = \frac{w b^{2}}{2T}
= \frac{1.0\times10^{-3}\times75^{2}}{2\times15}
= \frac{5.625}{30} = 0.1875\ \mathrm{m} .$$

**Assumptions.** (i) Steady state. (ii) Uniform recharge over a strip of uniform
transmissivity. (iii) The Dupuit approximation — horizontal flow and hydrostatic
pressure, which fails near the edges. (iv) No leakage through the base and no
regional flow gradient.

---

## ★2 — Apparent resistivity at three spacings

From the series with $\rho_1 = 50$, $\rho_2 = 500$,
$k = 450/550 = 0.81818$, $h = 10\ \mathrm{m}$:

| $a$ (m) | 1 | 10 | 100 |
|---|---|---|---|
| $\rho_a$ ($\Omega$ m) | 50.03 | 69.02 | 315.13 |

At $a = 1\ \mathrm{m}$ ($a/h = 0.1$) the array samples only the top layer and
returns $\rho_1$ to three figures. At $a = 10\ \mathrm{m}$ ($a/h = 1$) the array
is beginning to sense the boundary. At $a = 100\ \mathrm{m}$ ($a/h = 10$) the
current penetrates the layer and the value has moved most of the way toward the
half-space.

---

## ★3 — Bulk resistivity of clean and leachate-affected water

Clean: $\sigma_w = 0.050\ \mathrm{S\,m^{-1}}$,
$\sigma_b = \phi^{m}\sigma_w/a = 0.09\times0.050 = 0.00450\
\mathrm{S\,m^{-1}}$, $\rho_b = 222.2\ \Omega\,\mathrm{m}$.

At $C = 400$ CU: $\sigma_w = 0.050 + 1.0\times10^{-4}\times400 = 0.090\
\mathrm{S\,m^{-1}}$, $\sigma_b = 0.00810\ \mathrm{S\,m^{-1}}$,
$\rho_b = 123.5\ \Omega\,\mathrm{m}$.

The contrast is a factor $1.80$ — smaller than the factor of $2.50$ at $750$ CU
in the lesson, because the synthetic relation is linear in the *conductivity*,
so the resistivity contrast depends on where on the curve you are.

---

## ★★4 — Limit verification

At $a = 10^{-3}\ \mathrm{m}$ the series returns
$\rho_a = 50.00000000003507\ \Omega\,\mathrm{m}$, i.e. $\rho_1$ to eleven
figures. At $a = 10^{5}\ \mathrm{m}$ it returns
$\rho_a = 499.9991337585739\ \Omega\,\mathrm{m}$, i.e. $\rho_2$ to six figures.

**Why this check comes first.** The series is an infinite sum of terms
$k^n/\sqrt{a^2+4n^2h^2}$ whose cancellation structure is delicate at both ends:
for small $a$ every bracket is a difference of two nearly equal large numbers,
and for large $a$ the sum converges slowly and must be truncated with a
convergence argument. A sign error in the reflection coefficient, a missing
factor of $4a$, or a truncated sum can all produce *plausible-looking* curves
that no visual inspection would catch. The two limits are the only exact
statements available, they cost nothing to evaluate, and a forward model that
fails them cannot be used in an inversion: an inversion will happily fit the
error.

---

## ★★5 — Where the thickness information is

**(a)** From the lesson's sensitivity table for $\rho_1 = 60$,
$\rho_2 = 400\ \Omega\,\mathrm{m}$, $h = 8\ \mathrm{m}$, the largest fractional
change for a $10\%$ thickness error is at $a/h = 2.00$: $-0.0638$, i.e. a
$6.4\%$ change in $\rho_a$ for a $10\%$ change in $h$.

**(b)** At $a/h = 0.1$ the current barely penetrates the layer, so almost all of
the measured potential difference is controlled by $\rho_1$ and the thickness
enters only at second order ($-0.0022$ for a $10\%$ change, i.e. $0.2\%$, well
below the noise of any field survey). A small spacing measures the *cover's*
resistivity, not its thickness. The information about thickness is carried by
spacings of one to a few times $h$.

---

## ★★6 — Are the interpretations supported?

| interpretation | verdict | reason |
|---|---|---|
| "a conductive layer $8\ \mathrm{m}$ thick" | **supported** | $8\ \mathrm{m}$ lies inside the admitted $[7.5, 9.0]\ \mathrm{m}$ at $5\%$ noise |
| "exactly $12\ \mathrm{m}$ thick" | **not supported** | $12\ \mathrm{m}$ is outside the admitted set at either $5\%$ or $10\%$ noise, and "exactly" grants a precision the data do not have |
| "thinner than $6\ \mathrm{m}$" | **not supported** | the admitted set at $10\%$ noise already excludes $h < 6.0\ \mathrm{m}$, and at $5\%$ noise it excludes $h < 7.5\ \mathrm{m}$ |

The general rule: an interpretation is supported when it lies inside the admitted
set at the survey's own noise level, and the set must be quoted alongside the
number.

---

## ★★★7 — Testing for a third layer (model answer)

**(a) The forward model.** Fit a three-layer model ($\rho_1, h_1$; $\rho_2, h_2$;
$\rho_3$ half-space), because the two-layer fit attributes to a single conductive
layer whatever the current senses from both the cover and any intermediate
layer. The trap is that a two-layer model *always* returns an answer: the
inversion has no way to report "one of my layers should be two", and the fitted
$\rho_1$ and $h$ absorb the intermediate layer as a systematic bias. This is why
the two-layer curve looks well determined (Section 6 of the lesson) while being
wrong.

**(b) Discriminating spacings and plot.** Acquire over a wide range of $a$, at
least $0.3h$ to $20h$ where $h$ is the target depth, with several points per
decade, and plot $\rho_a$ against $a$ on log–log axes. A two-layer curve is
smooth and monotone in $\log a$ when $\rho_2 > \rho_1$; a three-layer curve with
an intermediate conductive layer shows an inflection, and a model with an
intermediate *resistive* layer shows a local maximum followed by a decrease.

**(c) Null hypothesis and criterion.** Null hypothesis: the data are drawn from a
two-layer model plus the stated noise. Reject it if the rms residual of the
best-fitting two-layer model exceeds the noise level (e.g. an rms of $8\%$ in
$\log\rho_a$ against a $5\%$ repeatability), **or** if the residuals are
structured — a systematic run of positive residuals at intermediate spacings
followed by negative ones is the signature of a missing layer and cannot be
explained by random noise however small the rms. The criterion must combine the
size and the structure of the residuals, because a model with the wrong number of
layers usually fails on structure first.

---

## ★★★8 — The self-potential degeneracy

**(a) Non-separability.** The model is

$$V(x) = \frac{\rho I}{2\pi\sqrt{x^{2}+d^{2}}} .$$

The two parameters $\rho$ and $I$ appear only in the product $\rho I$: replacing
$(\rho, I)$ by $(\lambda\rho, I/\lambda)$ leaves $V$ unchanged for every $x$.
The data therefore determine one number, $\rho I$, and the anomaly's *shape*
determines $d$ but not the pair. This is a one-dimensional null space, and no
amount of extra potential data along the same profile removes it.

**(b) Breaking it with resistivity.** A co-located resistivity survey measures
$\rho$ independently (via the layering of the shallow subsurface, not the buried
source). With $\rho$ known, $I = 2\pi V(0)\,d/\rho$ from the peak, so the source
strength is determined. **The remaining assumption** is that the buried source
is a compact current source in an otherwise *uniform* half-space of that
resistivity: a layered or heterogeneous subsurface distorts the potential, and
that distortion is not distinguishable from a change in $I$. The honest output is
then a range of $I$ consistent with the admitted range of $\rho$.

**(c) Half-width and depth location.** Setting $V(x) = V_\text{peak}/2$:

$$\frac{1}{\sqrt{1+(x/d)^{2}}} = \frac{1}{2}
\;\;\Longrightarrow\;\;
1 + \left(\frac{x}{d}\right)^{2} = 4
\;\;\Longrightarrow\;\;
x_{1/2} = \sqrt{3}\,d = 1.732\,d .$$

For the lesson's synthetic example ($d = 6\ \mathrm{m}$) the half-width is
$10.39\ \mathrm{m}$, consistent with the printed values ($68.237\
\mathrm{mV}$ at $x = 10\ \mathrm{m}$ against a half-peak of $66.31\
\mathrm{mV}$). **Use:** measure the half-width, divide by $\sqrt3$, and quote a
source depth. Two cautions: the relation assumes a single compact source, and a
distributed redox zone produces a *broader* hump that would be misread as a
deeper source; and the depth inferred is a depth to an equivalent point source,
not to the top of the reacting body.
