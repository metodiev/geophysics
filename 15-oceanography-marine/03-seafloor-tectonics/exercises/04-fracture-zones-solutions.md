# Solutions — 15-03-04 Fracture Zones, Transform Faults and Oceanic Anomalies

> **Read after attempting the exercises.** Lesson:
> [04 Fracture Zones, Transform Faults and Oceanic Anomalies](../04-fracture-zones.md).
> All numbers are SYNTHETIC model values.

## ★ Foundational

## ★1 — Velocity from the pole

$\omega=1.00\ ^\circ\mathrm{Myr^{-1}}=0.0174533\ \mathrm{rad\,Myr^{-1}}$,
$\sin45^\circ=0.707107$:

$$|v|=0.0174533\times6371\times0.707107
=1.11196\times10^{2}\times0.707107=78.63\ \mathrm{km\,Myr^{-1}}
=78.63\ \mathrm{mm\,yr^{-1}}.$$

The conversion is exact: $1\ \mathrm{km\,Myr^{-1}}=1\ \mathrm{mm\,yr^{-1}}$.

## ★2 — Exact and linear age

$$\text{age}(70^\circ)=\frac{1}{0.0174533}
\ln\frac{\tan35^\circ}{\tan30^\circ}
=\frac{\ln(0.700208/0.577350)}{0.0174533}
=\frac{0.192925}{0.0174533}=11.0539\ \mathrm{Myr}.$$

Linear rule: $(70-60)/1.00=10.0000\ \mathrm{Myr}$. Difference
$=(10.0000-11.0539)/11.0539=-9.5\%$, i.e. the linear rule underestimates the age
by 9.5% at this distance. (The demonstration reports 11.0539 Myr for the same
case, confirming the arithmetic.)

## ★3 — Rate conversion and age offset

$30\ \mathrm{mm\,yr^{-1}}=30\ \mathrm{km\,Myr^{-1}}$.

$$\Delta t=L/u_{\text{half}}=150\ \mathrm{km}/30\ \mathrm{km\,Myr^{-1}}
=5.00\ \mathrm{Myr}.$$

## ★★ Applied

## ★4 — Amplitude arithmetic

$$\frac{\mu_0J}{2\pi}=\frac{4\pi\times10^{-7}\times3.0}{2\pi}
=2\times10^{-7}\times3.0=6.0\times10^{-7}\ \mathrm{T}
=600\ \mathrm{nT}\ \text{per unit geometric factor}.$$

With a geometric factor of $0.4$: $0.4\times600=240\ \mathrm{nT}$ — the same
order as the demonstration's $228.7\ \mathrm{nT}$ peak-to-peak for the same
$J=3.0\ \mathrm{A\,m^{-1}}$. For $J=1.0\ \mathrm{A\,m^{-1}}$ the peak is
$0.4\times200=80\ \mathrm{nT}$, exactly one third.

**Why the rate inversion is immune:** the zero crossings — and therefore the
spacings — are positions of *zero* field. Scaling $J$ scales the whole profile
and moves no crossing. An amplitude inversion, by contrast, is linear in $J$ and
in the geometric factor, and the geometric factor depends on source depth,
thickness and skew: a factor-of-two error in any of them is invisible to the
spacing but fatal to the amplitude.

## ★5 — Age at 2224 km

(a) The angular distance is $2224/6371=0.34907\ \mathrm{rad}=20.000^\circ$, so
$\phi=80^\circ$ and the exact age is $21.4218\ \mathrm{Myr}$ (the lesson's value).

(b) The rate at the far end is
$\omega R\sin80^\circ=0.0174533\times6371\times0.98481=109.51\
\mathrm{km\,Myr^{-1}}$, so $2224/109.51=20.31\ \mathrm{Myr}$ — an *underestimate*
of 5.2%, because the point moved more slowly earlier in its history.

(c) Linear angular rule: $(80-60)/1.00=20.0000\ \mathrm{Myr}$.

(d) Errors: (b) $-5.2\%$, (c) $-6.6\%$. Both are systematically low; the error
grows as the pole is approached, reaching $-12.8\%$ at $\phi=65^\circ$ in the
lesson's table.

## ★6 — Depth steps

$\Delta t=300/40=7.50\ \mathrm{Myr}$.

- On 5 Myr crust: $373.2(\sqrt{12.5}-\sqrt{5})=373.2(3.53553-2.23607)
  =373.2\times1.29946=485\ \mathrm{m}$.
- On 30 Myr crust: $373.2(\sqrt{37.5}-\sqrt{30})=373.2(6.12372-5.47723)
  =373.2\times0.64649=241\ \mathrm{m}$.

Both age offsets are the same, but the depth step is halved on older crust
because $\mathrm{d}(\sqrt{t})/\mathrm{d}t=1/(2\sqrt{t})$: the subsidence curve
flattens, so equal age offsets produce smaller depth differences. **Fracture
zones are most prominent near the ridge** — a prediction that bathymetric
compilations confirm and that is a genuine test of the $\sqrt{t}$ law rather than
of a fitted curve.

## ★★★ Research-oriented

## ★7 — Age offset or temperature anomaly?

| observation | what it measures | precision needed | age-offset hypothesis | temperature hypothesis |
|---|---|---|---|---|
| magnetic lineation pattern across the fracture zone | the age offset directly, via stripe correlation | one identified reversal (the timescale calibration dominates) | the $396\ \mathrm{km}$ offset requires $\approx2\times$ the stripe spacing on the two sides | offsets are unchanged; the magnetisation pattern is unaffected by mantle temperature |
| bathymetric depth on both sides | the depth step | $\pm20\ \mathrm{m}$ (to resolve 184 m against 42 K) | predict $400\ \mathrm{m}$ from the offset alone | predict $216\ \mathrm{m}$ from the known offset plus a warm anomaly |
| free-air gravity / geoid across the fracture zone | the *density* structure, i.e. whether the depth anomaly is compensated by temperature | $\pm0.5\ \mathrm{mGal}$ at the anomaly wavelength | no geoid anomaly (age alone) | a geoid anomaly consistent with thermal expansion |
| heat flow on both sides | the thermal state at depth | $\pm5\ \mathrm{mW\,m^{-2}}$ | no heat-flow contrast once sediment and the $\sqrt{t}$ trend are removed | a contrast of order ${\sim}10$–$20\ \mathrm{mW\,m^{-2}}$ |
| crustal thickness from seismic refraction | whether the depth difference is crustal or mantle | $\pm0.3\ \mathrm{km}$ | thickness is the same on both sides | also the same (thermal anomalies are not crustal) |

**Discriminating logic:** the magnetic lineations settle the *age* question
definitively and cheaply. If they confirm a $200\ \mathrm{km}$ offset, the
$184\ \mathrm{m}$ residual must come from temperature, crustal thickness or
dynamic support, and the geoid and heat flow then separate temperature from
thickness.

**Remains degenerate:** the *vertical distribution* of the thermal anomaly. A
$42\ \mathrm{K}$ anomaly confined to the upper 100 km and a smaller anomaly
distributed over 300 km produce identical surface depth and geoid to first
order; separating them requires the heat flow *and* an assumption about the
conductivity structure, which is a model.

## ★8 — A skew-correction procedure

**Model.** The observed total-field anomaly is the projection of a 2-D body's
field onto the ambient field direction. For a fixed source geometry, changing the
magnetisation/magnetisation-to-field angle mixes the anomaly with a fixed
auxiliary function of the same geometry. The practical statement: the anomaly
$\Delta T(\theta)$ for skew angle $\theta$ is a linear combination of the
reduced-to-pole (RTP) anomaly $k_0(x)$ and a companion function $k_{90}(x)$:

$$\Delta T(x;\theta)=k_0(x)\cos\theta+k_{90}(x)\sin\theta ,$$

with $k_{90}$ determined by the same geometry (in the classic Fourier treatment,
$k_{90}$ is the Hilbert transform of $k_0$, so the pair is a quadrature pair).

**Parameter estimated:** the skew angle $\theta$ (equivalently the direction of
the magnetisation relative to the profile), which is what the interpreter does
not know because the palaeofield and the magnetisation direction are both
inferences.

**Objective function:** maximise the antisymmetry of the corrected profile,
$\rho(\theta)=-\sum k(x)k(-x)/\sum k(x)^2$ using the lesson's metric, over the
window containing one or a few boundaries. Equivalently, minimise
$\sum[k(x)+k(-x)]^2$, which is the $L_2$ statement of the same thing.
At the true $\theta$ the boundary response should be antisymmetric and
$\rho\to1$; the lesson's un-corrected values ($0.9765$ at $90^\circ$ down to
$0.5644$ at $30^\circ$) show the metric is sensitive enough to be a fitting
target.

**How noise enters:** the metric is quadratic in the profile, so its peak value
degrades as roughly $1/(1+\sigma_n^2/\sigma_s^2)$ and the *location* of the
maximum is unbiased only if the noise is symmetric about the boundary. With
signal-to-noise of 3 the fit typically recovers $\theta$ to a few degrees;
below signal-to-noise of about 1 the maximum is unconstrained and the correction
should not be applied.

**Independent validation:** a survey line crossing the same boundary at a
different azimuth. Both lines must give the *same* RTP anomaly after their
respective corrections; if they do not, the assumed source geometry (infinite
2-D, vertical sides) is wrong, not the angle.

**What the correction cannot fix:** the source geometry. Reducing to the pole
makes an oblique line look like a vertical-magnetisation line, but it cannot
recover resolution lost to depth, remove the finite width of a transition zone,
or correct an amplitude that has already been biased by a 2-D approximation on a
3-D body. After correction the anomaly is interpretable *shape-wise*; its
amplitude still carries the geometric factor, which is why rate inversions use
spacing and not amplitude.
