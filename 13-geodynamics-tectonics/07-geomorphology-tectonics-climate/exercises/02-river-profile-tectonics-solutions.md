# Solutions — 13-07-02 River Profiles, Steepness Indices and Uplift Inference

> **Read after attempting the exercises.** Numbers were computed with the same
> formulas as the lesson's demonstration.

Lesson: [02 River Profiles, Steepness Indices and Uplift Inference](../02-river-profile-tectonics.md).

---

## ★1 — Deriving the steady profile

Setting $\mathrm{d}z/\mathrm{d}t = 0$:

$$U = KA^mS^n \quad\Longrightarrow\quad S^n = \frac{U}{K}A^{-m}
\quad\Longrightarrow\quad S = \left(\frac{U}{K}\right)^{1/n}A^{-m/n}
= k_sA^{-\theta}.$$

So $\theta = m/n$ and $k_s = (U/K)^{1/n}$.

**Dimensions.** $[A] = \mathrm{m^2}$, $[S] = 1$, $[U] = \mathrm{m\,s^{-1}}$. With
$m = 0.5$, $n = 1$: $[K] = \mathrm{m\,s^{-1}}/\mathrm{m} = \mathrm{s^{-1}}$, and
$[k_s] = \mathrm{m\,s^{-1}}/\mathrm{s^{-1}} = \mathrm{m}$ — a length. In the
lesson's units (metres, years) $K$ has units yr$^{-1}$ and $k_s$ metres.

---

## ★2 — Slope–area values

$$S(4\times10^{5}) = 20\times(4\times10^{5})^{-0.5}
= \frac{20}{632.5} = 3.162\times10^{-2},$$

$$S(10^{6}) = \frac{20}{1000} = 2.0\times10^{-2}.$$

In geomorphic units, 31.6 m/km and 20.0 m/km. A factor of 2.5 in drainage area
gives a factor of $\sqrt{2.5} = 1.58$ in slope — the mild dependence that makes
river profiles useful over large drainage areas.

---

## ★3 — What $\theta$ means

$\theta = m/n$ is the ratio of the drainage-area exponent (how the erosional
efficiency grows downstream with discharge) to the slope exponent (how incision
responds to steepness). A profile's *shape* is controlled by $\theta$ alone,
whereas $k_s$ also involves the physical magnitudes $U$ and $K$, neither of which
the shape constrains. Empirically $\theta$ is well determined by a long profile
because it is a curvature, while $k_s$ is a slope normalised by drainage area,
i.e. an amplitude.

---

## ★4 — A two-segment $\chi$ transform

The transform is additive:
$\chi(x) = \int_0^{x}(A_0/A)^{0.5}\mathrm{d}x'$ with $A_0 = 10^{6}$ m². The
integrand is $(10^{6}/10^{5})^{0.5} = \sqrt{10} = 3.162$ for $x<50$ km and 1 for
$x\ge50$ km.

First segment: $3.162\times50\ \mathrm{km} = 158.1$ km. Second segment:
$1\times50\ \mathrm{km} = 50$ km. Total:

$$\chi(\text{outlet}) = \chi_{\text{total}} = \mathbf{208.1\ km}.$$

---

## ★5 — Elevations on the steady profile

$\mathrm{d}z/\mathrm{d}\chi = -k_sA_0^{-\theta} = -10/\sqrt{10^{6}} = -10/1000
= -0.01$. With $z = 0$ at the outlet ($\chi = 208.1$ km, which lies *downstream*,
so elevations increase as $\chi$ decreases):

$$z(x) = 0.01\times(\chi_{\text{total}}-\chi(x)).$$

- At the point $x = 50$ km: $\chi = 158.1$ km, $z = 0.01\times50{,}000 = 500$ m.
- At the divide: $\chi = 0$, $z = 0.01\times208{,}100 = \mathbf{2081\ m}$.
- At the outlet: $z = 0$.

Note that the profile is *straight in $\chi$* but piecewise-linear in $x$: the
two segments have different slopes in $x$ (31.62 m/km for $x<50$ km and 10 m/km
beyond), yet the same slope in $\chi$. That is the practical reason the transform
is used.

---

## ★6 — Ratio of $U/K$ and what it does not give

$k_s = (U/K)^{1/n}$ with $n=1$, so $(U/K)_1/(U/K)_2 = 40/20 = 2$. The steeper
basin has twice the ratio of uplift to erodibility.

**Cannot be concluded:** whether the difference is twice the uplift, half the
erodibility, or any product of the two — the degeneracy derived in the lesson.
Nor can it be concluded that the *present* ratio applies: $k_s$ integrates the
history over the response time of the profile.

---

## ★7 — Knickpoint speed and erodibility

$$c = \frac{60\ \mathrm{km}}{6\ \mathrm{Myr}} = 10\ \mathrm{km/Myr}
= 1.0\times10^{4}\ \mathrm{m}/10^{6}\ \mathrm{yr}
= 1.0\times10^{-2}\ \mathrm{m/yr} = \mathbf{10\ mm/yr}.$$

With $m = 0.5$ and $A_0 = 10^{6}$ m² ($A_0^{m} = 1000$ m):

$$K = \frac{c}{A_0^{m}} = \frac{1.0\times10^{-2}\ \mathrm{m/yr}}{1000\ \mathrm{m}}
= \mathbf{1.0\times10^{-5}\ yr^{-1}},$$

and the unit check is that $KA^m$ must have units of velocity:
$\mathrm{yr^{-1}}\times\mathrm{m} = \mathrm{m/yr}$ ✓.

---

## ★8 — Bias from a wrong concavity

From the lesson's table, using $\theta_{\text{try}} = 0.55$ on a profile built
with $\theta = 0.50$ biases the inferred $U$ by $+87.28\%$ — nearly a factor of
two. **The sign is predictable in advance:** using a concavity that is too large
puts too much weight on the downstream part of the transform
($(A_0/A)^{\theta}$ grows faster as $A$ falls), which flattens the $\chi$-plot's
abscissa upstream and *steepens* the fitted slope; a steeper slope means a larger
$k_s$ and therefore a larger inferred $U$. So $\theta_{\text{try}} > \theta_{\text{true}}$
biases $U$ upward, exactly as measured ($\theta = 0.55 \to +87\%$,
$\theta = 0.60 \to +250\%$). A useful check: the bias is monotone in
$\theta_{\text{try}}$, so a study that reports only one $\theta$ cannot bound it.

---

## ★9 — Measuring $K$ rather than $U/K$

**Observable.** The migration of a knickpoint through a dated sequence of
profiles, or its present-day position together with the timing of the disturbance
(a dated terrace, a lava flow damming the profile, or a known sea-level fall).

**Time resolution.** The knickpoint speed is $c = KA_0^m$; to resolve $K$ to a
factor of two the speed must be known to a factor of two, so the *timing* of the
disturbance and the profile pair must bracket the migration within a factor of
two. For $c = 10$ km/Myr and a 60 km migration that means dating the disruption
to within $\pm3$ Myr — achievable with a dated volcanic or terrace record, not
with an undated knickpoint.

**Assumption that remains.** $m$ and $A_0$, and the assumption that the
knickpoint's migration is set by the stream-power law rather than by a sediment
flux or a lithological boundary — which is the same class of assumption as before,
now moved onto a different parameter.

---

## ★10 — Precipitation variability mistaken for tectonics

$K$ varies with precipitation (roughly as a power law above a threshold) and with
sediment cover; over a range where rainfall varies by a factor of two, $K$ can
vary by a factor of several. Since the observable is $U/K$, a wetter basin looks
like a basin with higher uplift.

**Distinguishing test.** Map the precipitation field and the lithology
independently, and compare the spatial pattern of $k_s$ with the pattern of each
control:

- if the $k_s$ pattern correlates with rainfall and not with structure, the
  signal is climatic;
- if it correlates with structure (a fault, a fold hinge, a basin boundary) and
  crosses rainfall contours without change, the signal is tectonic;
- the decisive version is a *gradient* test: across a rainfall gradient that
  crosses a structural trend, a tectonic signal varies along strike and a
  climatic one along the rainfall gradient.

**Quantitative check.** Regress $\ln k_s$ on the structural distance and on
$\ln P$ simultaneously and compare the coefficients with their uncertainties; a
tectonic inference must survive when the precipitation term is included, not
before.
