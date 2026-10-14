# Solutions — 01-05-02 Derivatives and Rates of Change

> **Read this after attempting the exercises, not before.** Numerical values were
> computed, not estimated by hand. Where a value depends on floating-point
> arithmetic, the mechanism is named.

---

## ★1 — From first principles

**(a)** $\displaystyle\frac{f(x+h)-f(x)}{h}
= \frac{3(x+h)^{2}-5(x+h)-3x^{2}+5x}{h}
= \frac{6xh + 3h^{2} - 5h}{h} = 6x + 3h - 5$.

Letting $h\to0$: $f'(x) = \boxed{6x - 5}$.

**(b)** $\displaystyle\frac{1}{h}\left(\frac{1}{x+h+2}-\frac{1}{x+2}\right)
= \frac{(x+2)-(x+h+2)}{h(x+h+2)(x+2)}
= \frac{-1}{(x+h+2)(x+2)}$.

Letting $h\to0$: $f'(x) = \boxed{-\dfrac{1}{(x+2)^{2}}}$.

**(c)** Rationalise the numerator:

$$\frac{\sqrt{t+h}-\sqrt{t}}{h}
= \frac{(t+h)-t}{h\left(\sqrt{t+h}+\sqrt{t}\right)}
= \frac{1}{\sqrt{t+h}+\sqrt{t}}
\xrightarrow[h\to0]{}\frac{1}{2\sqrt t}.$$

So $f'(t) = \boxed{\dfrac{1}{2\sqrt t}}$ for $t>0$.

Note the pattern in all three: the algebra removes $h$ from the denominator. Only
then may $h\to0$ be taken.

---

## ★2 — Units of derivatives

| | Derivative | Units | Meaning |
|---|---|---|---|
| (a) | $dv/dz$ | $(\mathrm{km\,s^{-1}})/\mathrm{km} = \mathrm{s^{-1}}$ | how quickly speed changes with depth |
| (b) | $dT/dz$ | $\mathrm{K\,m^{-1}}$ | geothermal gradient |
| (c) | $dg/dz$ | $(\mathrm{m\,s^{-2}})/\mathrm{m} = \mathrm{s^{-2}}$ | gravity gradient, the free-air coefficient |
| (d) | $dP/dt$ | $\mathrm{Pa\,yr^{-1}}$ | loading or unloading rate |

**Dimensional check.** In Fourier's law $q = k\,dT/dz$ the right-hand side has
units $\mathrm{W\,m^{-1}K^{-1}} \times \mathrm{K\,m^{-1}} = \mathrm{W\,m^{-2}}$: the
kelvin cancel and the two inverse metres combine into $\mathrm{m^{-2}}$, leaving a
flux. Had the conductivity been quoted per unit *temperature difference* rather
than per unit gradient, the same product would have produced a
$\mathrm{W\,m^{-3}}$ — a volumetric heating rate, which is $\nabla\cdot\mathbf{q}$
and requires differentiating the flux once more. That is the step taken in
[01-06-04 Divergence, Curl and Physical Meaning](../../06-multivariable-calculus/04-divergence-and-curl.md) when the heat
equation is derived, and it is the reason the units of $k$ are worth writing down
every time.

---

## ★3 — Finite differences

Forward: $f'(x) \approx \dfrac{f(x+h)-f(x)}{h}$, truncation error
$-\dfrac{h}{2}f''(\xi) = O(h)$.

Central: $f'(x) \approx \dfrac{f(x+h)-f(x-h)}{2h}$, truncation error
$-\dfrac{h^{2}}{6}f'''(\xi) = O(h^{2})$.

Both need two function evaluations, so when evaluations are expensive the central
form is the better buy: same cost, one extra order. The exception is at a boundary
of the domain, where $f(x-h)$ may not exist and the forward (or backward) form is
the only option.

---

## ★★4 — Velocity gradient

**(a)** $dv/dz = 0.5\ \mathrm{s^{-1}}$ exactly.

**(b)** Because $v$ is linear, the central difference is exact up to round-off at
both steps. The demonstration prints `0.500000000000000` for $h = 100$ m and
`0.500000000000000` for $h = 1$ m.

**(c)** For small $h$ the numerator $v(z+h)-v(z-h) = h$ becomes a difference of two
nearly equal numbers, each of magnitude $\approx 3\times10^{3}$ m/s. The spacing of
representable doubles near 3000 is about
$\varepsilon\cdot 3000 \approx 6.7\times10^{-13}$, so the numerator carries an
absolute error of that order. Dividing by $2h = 2\times10^{-5}$ amplifies it to
about $3\times10^{-8}$ — which is the scale of the reported `1.26e-08`. This is
**loss of significance in the numerator**, the same mechanism as catastrophic
cancellation; the error grows as $h$ shrinks, exactly opposite to the truncation
error, which vanishes because the function is linear.

**(d)** With data known to $\sigma = 0.1$ m/s, the difference carries noise
$\approx\sigma\sqrt2$, so the noise in the quotient is $\sigma/(\sqrt2\,h)$. To keep
the gradient accurate to $10^{-3}$ of $0.5\ \mathrm{s^{-1}}$, that is
$5\times10^{-4}$:

$$\frac{0.1}{\sqrt2\,h} = 5\times10^{-4}
\;\Longrightarrow\; h = \frac{0.1}{\sqrt2\times5\times10^{-4}} \approx 141\ \mathrm{m}.$$

So $h \approx 100$–$200$ m is the right scale, and refining below about 140 m makes
the answer *worse*. There is no truncation error to trade against, because the model
is linear: the only error is the data noise.

---

## ★★5 — Borehole geotherm

**(a)** $(91.0-22.0)/2.0 = 34.5\ \mathrm{K\,km^{-1}} = 3.45\times10^{-2}\ \mathrm{K\,m^{-1}}$.

**(b)** $q = k\,dT/dz = 2.4 \times 0.0345 = 0.0828\ \mathrm{W\,m^{-2}} = 82.8\ \mathrm{mW\,m^{-2}}$.

Dimensional check: $\mathrm{W\,m^{-1}K^{-1}}\times\mathrm{K\,m^{-1}}$; the metre
cancel and the answer is in $\mathrm{W\,m^{-2}}$.

**(c)** Any two of the following, and they are physically distinct:

1. **Transient response to surface temperature history.** The upper few hundred
   metres carry a thermal memory of past climate (the Holocene and later changes);
   in that zone the measured gradient is not the steady-state value.
2. **Advective transport.** Groundwater flow moves heat, so the local gradient is
   not proportional to the conductive flux.
3. **Conductivity variation with lithology.** The calculation used a single $k$;
   a layered sequence has several, and the apparent gradient is a harmonic-type
   average rather than a physical property of one rock.
4. **Erosion or sedimentation.** A moving surface boundary means the profile has not
   reached steady state.

---

## ★★6 — Strain rate

**(a)** $\dot\varepsilon = \dfrac{0.035\ \mathrm{m\,yr^{-1}}}{6.0\times10^{4}\ \mathrm{m}}
= 5.833\times10^{-7}\ \mathrm{yr^{-1}}$, and dividing by
$3.156\times10^{7}\ \mathrm{s\,yr^{-1}}$,

$$\dot\varepsilon = 1.848\times10^{-14}\ \mathrm{s^{-1}} .$$

**(b)** $t = 1/\dot\varepsilon = 1.714\times10^{6}$ yr $= \boxed{1.71}$ Myr. Equivalently
$t = W/v = 6.0\times10^{4}\,\mathrm{m} / 0.035\,\mathrm{m\,yr^{-1}}$.

**(c)** The time to unit strain is $W/v$, which depends on both numbers. A study
reporting "35 mm/yr across the zone" gives a velocity; a study reporting
$1.8\times10^{-14}\ \mathrm{s^{-1}}$ gives a strain rate. They are related only
through the zone width, which is itself a modelling choice (does the shear zone
extend 60 km or 6 km?). Comparing "deformation rates" between two regions without
stating how the zone was defined is one of the most common apples-to-oranges
comparisons in tectonics.

---

## ★★★7 — Noise in a second difference

**(a)** With $f(x) = x + \eta(x)$ and the second difference

$$D_{2} = \frac{f(x+h)-2f(x)+f(x-h)}{h^{2}},$$

the signal part of a linear function contributes nothing. The noise part is
$[\eta(x+h)-2\eta(x)+\eta(x-h)]/h^{2}$. The three samples are independent, each with
standard deviation $\sigma$, so

$$\mathrm{Var}(D_{2}) = \frac{\sigma^{2}\left(1^{2}+2^{2}+1^{2}\right)}{h^{4}}
= \frac{6\sigma^{2}}{h^{4}}
\;\Longrightarrow\;
\mathrm{sd}(D_{2}) = \frac{\sigma\sqrt6}{h^{2}} .$$

The fourfold weight on the central sample is what makes the constant $\sqrt6$
rather than $\sqrt2$. For a normal error, $E\lvert D_2\rvert = \mathrm{sd}(D_2)\sqrt{2/\pi}
= 0.798\,\mathrm{sd}(D_2)$.

**(b)** Predicted mean absolute values for $\sigma = 10$ m/s:
$0.798\times 10\sqrt6/h^{2}$.

| $h$ (m) | predicted mean | observed mean | ratio |
|---|---|---|---|
| 500 | $7.82\times10^{-5}$ | $7.40\times10^{-5}$ | 0.95 |
| 100 | $1.95\times10^{-3}$ | $1.87\times10^{-3}$ | 0.95 |
| 20 | $4.89\times10^{-2}$ | $5.10\times10^{-2}$ | 1.04 |

Empirical exponent: from $h = 500$ to $h = 20$ the mean grows by a factor
$5.10\times10^{-2}/7.40\times10^{-5} = 690$, while $h$ falls by a factor 25. Hence
the exponent is $\ln 690/\ln 25 = 2.03$, against the predicted 2. (Run-to-run
scatter of a few percent is expected from the finite sample; the fit was made with
200 samples per step.)

The practical statement: **a second difference amplifies noise as $h^{-2}$, worse
than a first difference's $h^{-1}$.** Computing curvature — gravity gradients,
flexural curvature, second derivatives of any gridded field — from noisy data is
correspondingly harder, and the standard remedy is to fit a smooth model rather
than to difference.

**(c)** Limits of the conclusion. The exponent depends only on the differencing
*weights* $(1,-2,1)$ and the $h^{-2}$ scaling, so it is robust to the noise
distribution. The *magnitude*, and in particular the constant $\sqrt6$, requires
the noise to be independent and identically distributed; correlated noise (a
systematic tilt, a drifting instrument) invalidates the $\sqrt6$ and can produce
errors that grow even faster, or that do not average down with more samples at all.
Nothing here identifies the true second derivative — the model is linear, so the
true value is zero and the entire signal in the table is noise.

---

## ★★★8 — Elevation error and survey design

The free-air gradient from the lesson is

$$\frac{dg}{dz} = -\frac{2g}{R} = -3.0826\times10^{-6}\ \mathrm{m\,s^{-2}\,m^{-1}}
= -308.6\ \mu\mathrm{Gal\,m^{-1}} .$$

An elevation uncertainty of $\pm3$ mm therefore produces

$$\lvert\delta g\rvert = 308.6\ \mu\mathrm{Gal\,m^{-1}} \times 3\times10^{-3}\ \mathrm{m}
= \boxed{0.93\ \mu\mathrm{Gal}} .$$

With a repeatability of 5 µGal, the elevation error contributes about 0.9 µGal in
quadrature with the instrument noise — well below the instrument's own limit
($\sqrt{5^{2}+0.93^{2}} = 5.09$ µGal, i.e. a 1.8 % inflation of the error). So at
5 µGal repeatability, millimetre-level height control is *adequate* and the survey
design should spend its effort elsewhere (network geometry, drift control, tidal
corrections, repeated occupations).

The comparison also tells you where the design must change: the elevation
contribution reaches 1 µGal at 3.2 mm and reaches 5 µGal at 16 mm. A survey aiming
at 1 µGal repeatability (heap gravimeters, or superconducting instruments) needs
heights known to better than a few millimetres, which in practice means
GNSS-levelled stations occupied concurrently. This is the design trade-off that
microgravity monitoring lives or dies by, and it is pure chain rule.
