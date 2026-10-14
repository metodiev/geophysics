# Solutions — 02-10-03 Radiative Transfer, Blackbody Radiation and Kirchhoff's Law

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Planck at 10 µm

**(a)** With $c_1 = 1.191\,043\times10^{-16}$ W m² and
$x = c_2/(\lambda T) = 1.438\,777\times10^{-2}/(10^{-5}T)$:

| $T$ (K) | $x$ | $B_\lambda$ (W m⁻² sr⁻¹ µm⁻¹) |
|---|---|---|
| 300 | 4.796 | **9.924** |
| 500 | 2.878 | **71.019** |
| 1000 | 1.439 | **370.403** |

**(b)** $370.403/9.924 = \mathbf{37.3}$. The flux ratio is
$56703.7/459.3 = 123.5$. The two differ because $B_\lambda$ is the *spectral*
radiance at one wavelength while $\sigma T^4$ is the integral over all
wavelengths, and the shape of the spectrum changes with $T$: raising the
temperature moves the peak toward shorter wavelengths and away from 10 µm, so
the spectral radiance at 10 µm grows more slowly than the total.

**(c)** $\sigma T^4 = 459.300$, 3543.984 and 56 703.744 W m⁻² for 300, 500 and
1000 K.

**(d)** 300 K is a typical terrestrial surface (the demo's 288–300 K range); the
1000 K value is a hot geological surface, of the order of a lava crust or a
high-temperature geothermal vent.

---

## ★2 — Flux, coefficient and peak

**(a)** $F = \sigma T^4 = \mathbf{459.300}$, $\mathbf{3543.984}$ and
$\mathbf{56\,703.744}$ W m⁻².

**(b)** $4\sigma T^3 = \mathbf{6.124}$, $\mathbf{28.352}$ and
$\mathbf{226.815}$ W m⁻² K⁻¹.

**(c)** $\lambda_{\max} = 2.897\,772\times10^{-3}/T$:
**9.6592 µm**, **5.7955 µm** and **2.8978 µm**.

**(d)** $56\,703.7/459.3 = \mathbf{123.5}$. A 1000 K target against a 300 K
background has a contrast of two orders of magnitude in flux — which is why lava
and hot springs are trivially detectable in the thermal infrared, and why the
hard problem in thermal remote sensing is separating surfaces of *similar*
temperature (a 1 K difference at 300 K is a 1.3 per cent flux change) rather
than finding the hot ones.

---

## ★3 — Wien's law

**(a)** $\lambda_{\max} = 2.897\,772\times10^{-3}/400 = 7.244\times10^{-6}$ m
$= \mathbf{7.244}$ µm (thermal infrared).

**(b)** $T = 2.897\,772\times10^{-3}/4.0\times10^{-6} = \mathbf{724.4}$ **K**.

**(c)** $\lambda_{\max} = 2.897\,772\times10^{-3}/5772 = 5.020\times10^{-7}$ m
$= \mathbf{502}$ **nm**, in the **visible** (green).

**(d)** **No.** The frequency form $B_\nu$ peaks where
$h\nu/k_BT = 2.821\,439\ldots$, giving
$\nu_{\max} = 5.878\,9\times10^{10}\,T$ Hz, whereas
$c/\lambda_{\max} = 1.0346\times10^{11}\,T$ Hz. The two differ by a factor
$5.8789/10.346 = 0.568$, i.e. the peak in frequency is at a wavelength longer
than $\lambda_{\max}$ by a factor 1.76. The reason is that "the peak" is defined
with respect to an integration variable, and $B_\lambda$ and $B_\nu$ are
different functions related by the Jacobian $c/\lambda^2$; a peak of a function
is not preserved by a change of variable.

---

## ★4 — Brightness temperature

**(a)** $x = \ln\!\left(1+\dfrac{c_1}{\lambda^5I}\right)
= \ln\!\left(1+\dfrac{1.191043\times10^{-16}}{(11\times10^{-6})^5\times8.0\times10^{6}}
\right)$

$\lambda^5 = 1.610\,51\times10^{-25}$ m⁵, so
$\lambda^5I = 1.288\,41\times10^{-18}$ W m² and
$c_1/(\lambda^5I) = 92.44$. Then $x = \ln(93.44) = 4.5374$ and

$$T_B = \frac{c_2}{\lambda x} = \frac{1.438\,777\times10^{-2}}
{1.1\times10^{-5}\times4.5374} = \mathbf{288.27\ K} .$$

**(b)** The brightness temperature is **below** the true kinetic temperature. A
surface with $\epsilon<1$ emits less than a blackbody at the same temperature,
and the inverse Planck function maps a smaller radiance to a smaller
temperature monotonically; the retrieved value is therefore a lower bound.

**(c)** With a greybody relation $T_B \approx \epsilon^{1/4}T$ (the broadband
limit of lesson equation (16)),
$T \approx T_B/\epsilon^{1/4} = 288.27/0.95^{1/4} = 288.27/0.98726
= \mathbf{292.0}$ **K**. The emissivity correction raises the retrieved
temperature by 3.7 K. (A real retrieval does the correction in radiance, band by
band, rather than with the fourth-root approximation.)

**(d)** Two reasons at least: (i) the atmosphere between the surface and the
sensor adds its own emission and absorbs some of the surface's, so the measured
radiance is not the surface radiance; (ii) the surface may not be isothermal over
the pixel or opaque at that wavelength, and it may be a mixture of materials at
different temperatures and emissivities. A third, which is really a
specification error, is that the emissivity used may not be the emissivity at
that wavelength and viewing angle.

---

## ★5 — Reading the demo

**(a)** The numerically integrated value is **6.493939402266** and
$\pi^4/15 = 6.493939402267$: a relative difference of **1.372 × 10⁻¹³**.
This is the quadrature converging to the analytic value to the limit of the
arithmetic.

**(b)** $\sigma$ from the numerically integrated Planck function is
**5.670374419184 × 10⁻⁸** W m⁻² K⁻⁴, against the exact
5.670374419 × 10⁻⁸: a relative difference of **3.239 × 10⁻¹¹**, which is the
10-digit truncation of the exact value plus the quadrature error, not a physical
discrepancy.

**(c)** $x = \mathbf{4.965114231744}$ and
$b = c_2/x = \mathbf{2.897\,771\,955\,2\times10^{-3}}$ **m K**, against a
published 2.897 771 955 × 10⁻³ m K — a relative difference of 6.4 × 10⁻¹¹.

**(d)** Because $\sigma$ is *derived* from $h$, $c$ and $k_B$, all of which have
exact values fixed by the 2019 SI, so $\sigma$ itself is exact and its digits are
definitions rather than measurements. An emissivity is a *nominal* property of a
particular surface at a particular wavelength, viewing angle, grain size,
roughness and moisture content; it varies continuously and must be given as a
range with a source, or as a measurement with an uncertainty.

---

## ★6 — Emissivity error

**(a)** $F = \epsilon\sigma T^4 = 0.96\times5.670\,374\,419\times10^{-8}
\times320^4 = \mathbf{570.80}$ **W m⁻²**.

**(b)** The greybody brightness temperature with $\epsilon$ assumed 1 is
$T_B = \epsilon^{1/4}T = 0.96^{0.25}\times320 = \mathbf{316.75}$ **K**.

**(c)** Error $= 316.75-320 = \mathbf{-3.25}$ **K**: the retrieval is too cold
by 3.25 K.

**(d)** With $\epsilon = 0.90$, $T_B = 0.90^{1/4}\times320 = 311.68$ K, an error
of **−8.32 K**. The general rule: for the broadband greybody relation the error
is $-T(1-\epsilon^{1/4})$, so it grows (i) as the emissivity departs from 1, and
(ii) in proportion to the true temperature — a 10 per cent emissivity error at
320 K costs about 8 K, and at 600 K it would cost about 16 K. The error is always
in the direction of *underestimating* temperature, because
$\epsilon^{1/4} < 1$.

---

## ★7 — A layer over a surface

**(a)** $B(11\ \mu\mathrm m, 300\ \mathrm K)$ and $B(11\ \mu\mathrm m,
265\ \mathrm K)$ from the Planck function, then

$$I = B_a(1-e^{-0.5}) + B_se^{-0.5} .$$

Numerically, $I = \mathbf{7.9123}$ **W m⁻² sr⁻¹ µm⁻¹**.

**(b)** Inverting the Planck function, $T_B = \mathbf{287.58}$ **K**.

**(c)** $\epsilon = 1-e^{-\tau} = 1-e^{-0.5} = \mathbf{0.3935}$.

**(d)** The measurement is much closer to the surface than to the layer: 287.58 K
against a surface of 300 K and a layer of 265 K. The surface dominates because at
$\tau = 0.5$ only 39.35 per cent of the observed radiance originates in the
layer; 60.65 per cent is transmitted surface radiance. At $\tau = 5$ the same
calculation gives $I = 5.3805$ W m⁻² sr⁻¹ µm⁻¹ and $T_B = 265.28$ **K** — the
layer, with the surface completely hidden. The transition happens over $\tau$ of
order unity, which is the quantitative statement of "the atmosphere is opaque
here".

---

## ★8 — Planetary balance

**(a)** $F = S(1-a)/4 = 1361\times0.75/4 = 255.1875$ W m⁻², so

$$T_e = (255.1875/\sigma)^{1/4} = \mathbf{259.01}\ \mathbf K .$$

**(b)** $\dfrac{\mathrm dT_e}{\mathrm dS} = \dfrac{T_e}{4S}
= \dfrac{259.007}{4\times1361} = \mathbf{0.04758}$ **K per W m⁻²**.

**(c)** A 1 per cent change in $S$ is 13.61 W m⁻², so
$\Delta T_e = 0.04758\times13.61 = \mathbf{0.648}$ **K**.

**(d)** $T_s = 2^{1/4}T_e = 1.189\,21\times259.007 = \mathbf{308.01}$ **K**. A
grey single-layer atmosphere is **not** adequate: it predicts 308 K against an
observed 288 K for the Earth at these parameters, an error of 20 K in the
direction of too much warming. The failure is that a grey atmosphere absorbs all
infrared, whereas the real one is transparent in the 8–14 µm window, where
36.6 per cent of the terrestrial emission at 288 K escapes directly from the
surface. The greenhouse effect is a *spectral* phenomenon, and a grey model
cannot represent it.

---

## ★★★9 — Radiative transfer and Kirchhoff for a slab

**(a)** Over a path element $\mathrm ds$ containing $N$ absorbers per unit volume
with absorption cross-section $\sigma_a$, the fraction of the beam removed is
$N\sigma_a\,\mathrm ds = \mathrm d\tau$. The element also emits, and in local
thermodynamic equilibrium at temperature $T$ its emission coefficient is
$\mathrm d\tau\,B(T)$ by the Einstein relations. Hence

$$\mathrm dI = -I\,\mathrm d\tau + B(T)\,\mathrm d\tau
\qquad\Longrightarrow\qquad
\frac{\mathrm dI}{\mathrm d\tau} = -I + B(T) ,$$

with $\tau$ increasing along the direction of propagation into the medium from
the observer, so that the observed intensity decreases with increasing $\tau$.
Here $I$ is the spectral radiance in W m⁻² sr⁻¹ per unit wavelength,
$B(T)$ the Planck function in the same units, and $\tau$ dimensionless.

**(b)** Multiply by $e^{\tau}$:

$$\frac{\mathrm d}{\mathrm d\tau}\left(Ie^{\tau}\right) = B(T)e^{\tau}
\qquad\Longrightarrow\qquad
I(\tau) = e^{-\tau}I(0) + \int_0^{\tau}B(T(\tau'))e^{-(\tau-\tau')}
\mathrm d\tau' .$$

For an isothermal layer, $B$ is constant and the integral is
$B(1-e^{-\tau})$, so $I = B(1-e^{-\tau}) + I_se^{-\tau}$ with
$I_s = I(0)$ the radiance entering from below.

**(c)** Set the surface radiance to zero (nothing behind the slab) and divide by
$B$: the emergent radiance is $B(1-e^{-\tau})$. Comparing with the definition of
emissivity for a slab, $I = \epsilon B$, gives $\epsilon = 1-e^{-\tau}$
exactly. This is Kirchhoff's law and not a definition: what was used is that the
emission coefficient of the element equals its absorption coefficient, which is
the Einstein relation between $A$ and $B$ coefficients and hence the second law
of thermodynamics. A medium that absorbed more than it emitted at a given
temperature would produce a net radiative energy transfer from cold to hot.

**(d)** With scattering, extinction (the $-I$ term) is the sum of absorption and
scattering, but the source function acquires an additional term from radiation
scattered *into* the beam from other directions. The equation becomes
integro-differential, and one must specify the phase function
$p(\cos\Theta)$ describing the angular distribution of a scattering event, the
single-scattering albedo (the fraction of extinction that scatters), and the
boundary conditions at the surface, whose reflectance itself depends on the
illumination geometry. That is the content of the scattering chapter of any
radiative transfer text (§13).

---

## ★★★10 — Fitting a single-layer emissivity

**(a)** Let $F = S(1-a)/4$ be the absorbed solar flux per unit area. The
surface radiates $\sigma T_s^4$ upward and absorbs $\epsilon_a\sigma T_a^4$ from
the layer below it:

$$\sigma T_s^4 = F + \epsilon_a\sigma T_a^4 . \tag{i}$$

At the top of the atmosphere the outgoing flux is the layer's upward emission
plus the surface radiation transmitted through the layer, and it must balance the
absorbed solar flux:

$$\epsilon_a\sigma T_a^4 + (1-\epsilon_a)\sigma T_s^4 = F . \tag{ii}$$

From (i), $\epsilon_a\sigma T_a^4 = \sigma T_s^4 - F$; substituting into (ii):

$$\sigma T_s^4 - F + (1-\epsilon_a)\sigma T_s^4 = F
\qquad\Longrightarrow\qquad
\sigma T_s^4(2-\epsilon_a) = 2F .$$

With $F = \sigma T_e^4$,

$$T_s = T_e\left(\frac{2}{2-\epsilon_a}\right)^{1/4} .$$

**(b)** $\epsilon_a = 1$ gives $T_s = 2^{1/4}T_e = 302.75$ K, so to obtain
288 K the factor must be smaller:
$\left(\dfrac{288}{T_e}\right)^4 = \dfrac{2}{2-\epsilon_a}$ with
$T_e = 254.578$ K. Numerically
$(288/254.578)^4 = 1.6374$, so $2-\epsilon_a = 1.2214$ and
$\epsilon_a = \mathbf{0.779}$.

**(c)** For $\epsilon_a = 1$, $T_s = \mathbf{302.75}$ **K** — 14.8 K hotter than
the value fitted in (b) and 14.7 K above the observed 288 K.

**(d)** The fitted $\epsilon_a = 0.779$ says that the atmosphere absorbs (and
therefore emits) only about 78 per cent of the infrared radiation reaching it,
leaving 22 per cent to escape directly to space. That is exactly what a
*spectral* window does: the demo's band calculation shows that **36.6 per cent**
of the terrestrial emission at 288 K lies between 8 and 14 µm, where the
atmosphere is largely transparent, so a large fraction of the surface radiance
never interacts with the absorbing gases at all. A single grey emissivity cannot
describe this because it must be applied to every wavelength simultaneously: the
same number must represent both the opaque 15 µm CO₂ band and the transparent
11 µm window. Reproducing the observed surface temperature therefore requires
wavelength-dependent absorption, and the grey model's fitted $\epsilon_a$ is a
compromise that gets the *total* right while getting every individual band wrong.

---

## ★★★11 — Calibration error and the split window

**(a)** Using the demo's computed fractional sensitivities at 300 K:

| $\lambda$ (µm) | $\mathrm dL/L$ per K | temperature error for 1 per cent (K) |
|---|---|---|
| 8 | 0.020168 | **0.496** |
| 10 | 0.016197 | **0.617** |
| 12 | 0.013620 | **0.734** |
| 14 | 0.011835 | **0.845** |

**(b)** The sensitivity $\mathrm dL/L\,\mathrm dT \approx c_2/(\lambda T^2)$
*rises* as the wavelength shortens, so the shortest wavelength tested (8 µm) is
the most sensitive to a temperature change and the least sensitive to a radiance
error. Sensitivity to *emissivity* is a different question: an emissivity error
enters as a multiplicative factor on the radiance, so a band in which the
emissivity varies strongly with wavelength and mineralogy (8–9 µm, the
reststrahlen region of silicates) is much more affected by an emissivity error
than a band in the 11–12 µm region where most rock emissivities are close to 1
and vary slowly. That is why operational retrievals use the 11–12 µm window for
temperature and the 8–9 µm region for emissivity and mineralogy.

**(c)** The radiance difference between the two bands carries information about
the atmosphere: water vapour absorbs slightly more at 12 µm than at 11 µm, so
the *difference* between the two brightness temperatures is a measure of the
column water vapour and of the atmospheric temperature profile between the
surface and the sensor. That is the whole content of the split-window technique:
the atmosphere's differential absorption is measured by the two-band difference
and used to correct the surface temperature derived from either band alone.

**(d)** A split-window algorithm does not remove: (i) an error in the surface
emissivity, which enters both bands and is not separable from temperature without
independent information; and (ii) an error in the radiometric calibration, which
is common to both bands and therefore cancels in the *difference* but not in the
absolute temperature. A third, which is really a specification error, is a
scene that is not horizontally uniform within the field of view, so that the two
bands do not see the same surface.
