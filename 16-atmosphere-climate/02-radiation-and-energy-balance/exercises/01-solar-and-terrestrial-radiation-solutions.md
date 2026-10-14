# Solutions — 16-02-01 Solar and Terrestrial Radiation, Blackbody Laws

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [01 Solar and Terrestrial Radiation](../01-solar-and-terrestrial-radiation.md).

---

## ★1 — Insolation and effective temperature versus albedo

$$T_e = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4}, \qquad \frac{S}{4} = 340.25\
\mathrm{W\,m^{-2}}.$$

| $a$ | absorbed $S(1-a)/4$ (W m⁻²) | $T_e$ (K) | $\lambda_{\max}$ (µm) |
|---|---|---|---|
| 0.00 | 340.25 | 278.32 | 10.41 |
| 0.30 | 238.17 | 254.58 | 11.38 |
| 0.60 | 136.10 | 221.34 | 13.09 |

**Trend.** A higher albedo reflects more sunlight, so a lower temperature is
needed to balance the energy budget — a *reflective* planet is a colder planet, and
because $F \propto T^4$ the temperature moves only as the fourth root of the
albedo change ($a: 0\to0.3$ lowers $T_e$ by $8.5\%$ but lowers the absorbed flux
by $30\%$).

---

## ★2 — Peak wavelengths

$$\lambda_{\max} = \frac{2.897771955\times10^{-3}}{T}.$$

| $T$ (K) | $\lambda_{\max}$ (µm) | region |
|---|---|---|
| 200 | 14.489 | thermal infrared |
| 255 | 11.364 | thermal infrared |
| 300 | 9.659 | thermal infrared |
| 1000 | 2.898 | near/mid infrared |
| 5772 | 0.502 | visible (green) |

---

## ★3 — Blackbody flux densities

$$F(300) = 5.670374419\times10^{-8}\times300^4 = 459.30\ \mathrm{W\,m^{-2}},$$
$$F(255) = 5.670374419\times10^{-8}\times255^4 = 239.76\ \mathrm{W\,m^{-2}}.$$

Ratio: $459.30/239.76 = 1.9157 = (300/255)^4 = 1.17549^4$. ✔

**Why the fourth power.** The Planck function has the temperature entering through
the argument $hc/(\lambda k_BT)$, so scaling $T$ scales the whole spectrum in
amplitude by $T^4$ and in wavelength by $1/T$; the total flux therefore scales as
$T^4$. Equivalently, both the peak height and the width of the spectrum grow with
$T$, and the product goes as $T^4$.

---

## ★4 — Brightness temperatures

$$T_B = \left(\frac{F}{\sigma}\right)^{1/4}.$$

| $F$ (W m⁻²) | $T_B$ (K) |
|---|---|
| 100 | 204.93 |
| 238.17 | 254.58 |
| 400 | 289.81 |

Note that $F = 238.17\ \mathrm{W\,m^{-2}}$ recovers exactly the lesson's
$T_e = 254.58\ \mathrm{K}$: the brightness temperature and the effective
temperature are the same quantity when the emitting surface is black and
unobstructed.

---

## ★5 — Derivation of Wien's law

Write $x = hc/(\lambda k_BT)$, so $\lambda = hc/(xk_BT)$ and
$\mathrm{d}\lambda = -(hc/(k_BT))x^{-2}\mathrm{d}x$. Then

$$B_\lambda = \frac{2hc^2}{\lambda^5}\frac{1}{e^x-1}
= \frac{2hc^2}{(hc/(xk_BT))^5}\frac{1}{e^x-1}
= \frac{2k_B^5T^5}{h^4c^3}\frac{x^5}{e^x-1}
\equiv C\,\frac{x^5}{e^x-1}.$$

Maximising with respect to $x$:

$$\frac{\mathrm{d}}{\mathrm{d}x}\frac{x^5}{e^x-1} = 0
\;\Longrightarrow\;
\frac{5x^4(e^x-1)-x^5e^x}{(e^x-1)^2} = 0
\;\Longrightarrow\;
5(e^x-1) = xe^x,$$

$$5e^x - 5 = xe^x \;\Longrightarrow\; e^x(5-x) = 5
\;\Longrightarrow\; x = 5(1-e^{-x}). \qquad\checkmark$$

**Numerical solution.** Newton's method on $g(x) = x - 5(1-e^{-x})$,
$g'(x) = 1 - 5e^{-x}$, from $x_0 = 5$:

| iteration | $x$ |
|---|---|
| 0 | 5.000000000 |
| 1 | 4.965162753 |
| 2 | 4.965114232 |
| 3 | 4.965114232 |

$$b = \frac{hc}{xk_B} = \frac{6.62607015\times10^{-34}\times2.99792458\times10^{8}}
{4.965114232\times1.380649\times10^{-23}}
= 2.897771955\times10^{-3}\ \mathrm{m\,K}.$$

The tabulated value is $2.897772\times10^{-3}\ \mathrm{m\,K}$: agreement to
$6.4\times10^{-11}$ relative — the small residual is the tabulation's own rounding.

---

## ★6 — Derivation of the Stefan–Boltzmann constant

From ★5's substitution (the same one, since the integral is over all
wavelengths):

$$\int_0^\infty B_\lambda\,\mathrm{d}\lambda
= \frac{2k_B^4T^4}{h^3c^2}\int_0^\infty\frac{x^3}{e^x-1}\mathrm{d}x .$$

Using $\int_0^\infty x^3/(e^x-1)\,\mathrm{d}x = \Gamma(4)\zeta(4) = 6\cdot
\frac{\pi^4}{90} = \frac{\pi^4}{15} = 6.493939402$ (verified numerically in the
demonstration to $2.0\times10^{-11}$):

$$\int_0^\infty B_\lambda\,\mathrm{d}\lambda = \frac{2\pi^4k_B^4}{15h^3c^2}T^4
= 1.804936236\times10^{-8}\,T^4 \ \mathrm{W\,m^{-2}\,sr^{-1}}.$$

**Where the extra $\pi$ comes from.** $B_\lambda$ is a *radiance*, per unit solid
angle. The flux leaving a flat Lambertian surface integrates the radiance over the
outgoing hemisphere with a $\cos\theta$ weighting:
$\int\cos\theta\,\mathrm{d}\Omega = 2\pi\int_0^{\pi/2}\cos\theta\sin\theta\,
\mathrm{d}\theta = \pi$. So

$$\sigma = \pi\times\frac{2\pi^4k_B^4}{15h^3c^2} = \frac{2\pi^5k_B^4}{15h^3c^2}.$$

**Numerical evaluation.**

$$\sigma = \frac{2\times(3.14159265)^5\times(1.380649\times10^{-23})^4}
{15\times(6.62607015\times10^{-34})^3\times(2.99792458\times10^{8})^2}
= 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}},$$

agreeing with the tabulated constant to $3.3\times10^{-11}$ (rounding in the
tabulation).

---

## ★7 — The Sun, and a second planet

$$L_\odot = S\times4\pi(1\ \mathrm{AU})^2
= 1361 \times 4\pi \times (1.495978707\times10^{11})^2 = 3.82753\times10^{26}\
\mathrm{W},$$

$$T_{\text{eff}} = \left(\frac{L_\odot}{4\pi R_\odot^2\sigma}\right)^{1/4}
= \left(\frac{3.82753\times10^{26}}
{4\pi(6.957\times10^{8})^2\times5.670374419\times10^{-8}}\right)^{1/4}
= 5771.8\ \mathrm{K}.$$

**At Mars** ($d = 1.524\ \mathrm{AU}$), the inverse-square law gives

$$S_{\text{Mars}} = \frac{1361}{1.524^2} = \frac{1361}{2.322576}
= 585.99\ \mathrm{W\,m^{-2}},$$

$$T_e = \left(\frac{585.99\times(1-0.25)}{4\times5.670374419\times10^{-8}}
\right)^{1/4}
= \left(\frac{439.49}{2.26815\times10^{-7}}\right)^{1/4}
= (1.93737\times10^{9})^{1/4} = 209.81\ \mathrm{K}.$$

**Statement to include:** this is the equilibrium temperature of a blackbody with
albedo $0.25$ and no atmosphere, and it is *not* a claim about any measured
surface temperature. The step from a modelled $T_e$ to an observed surface
temperature requires the atmospheric radiative transfer of
[02](../02-radiative-transfer-atmosphere.md).

---

## ★8 — Daily-mean insolation at $60^\circ$N

$$h_0 = \arccos(-\tan\phi\tan\delta), \qquad
\bar F = \frac{S}{\pi}\left[h_0\sin\phi\sin\delta
+ \cos\phi\cos\delta\sin h_0\right].$$

| $\delta$ | $h_0$ (rad) | half-day (h) | $\bar F$ (W m⁻²) |
|---|---|---|---|
| $0^\circ$ | 1.5708 | 6.00 | 216.6 |
| $+23.44^\circ$ | 2.4194 | 9.24 | 492.4 |
| $-23.44^\circ$ | 0.7237 | 2.76 | 23.6 |

**Implication.** The daily-mean insolation at $60^\circ$N varies by a factor of
**21** between the solstices ($492.4/23.6 = 20.9$) while the equator's varies by
only $1.09$ ($433.2/397.5$). Whatever the atmosphere does, it must transport heat
poleward in winter and the pole-to-equator gradient must reverse sign in summer —
and through the thermal wind of
[16-01-05](../../01-atmospheric-structure-and-thermodynamics/05-atmospheric-dynamics-basics.md)
a reversed temperature gradient means a reversed zonal wind. This one table is
the arithmetic origin of the seasonal reversal of the stratospheric circulation.

---

## ★9 — Emissivity, brightness temperature and the ratio

For a grey surface at $T = 300\ \mathrm{K}$, $\varepsilon = 0.90$:

$$F = \varepsilon\sigma T^4 = 0.90\times5.670374419\times10^{-8}\times300^4
= 0.90\times459.30 = 413.4\ \mathrm{W\,m^{-2}}.$$

The *brightness temperature* of a scene radiating
$F = 400\ \mathrm{W\,m^{-2}}$ is $T_B = (400/\sigma)^{1/4} = 289.81\ \mathrm{K}$.

**Why $T_B < T$.** For a grey body, $F = \varepsilon\sigma T^4$, so
$T_B = (F/\sigma)^{1/4} = \varepsilon^{1/4}T$. With $\varepsilon = 0.90$,

$$\frac{T_B}{T} = 0.90^{1/4} = 0.97400, \qquad
T_B = 0.97400\times300 = 292.20\ \mathrm{K}.$$

The measured $289.81\ \mathrm{K}$ is *lower still*, so a second effect is present
beyond the surface emissivity: the scene is radiating
$400\ \mathrm{W\,m^{-2}}$ rather than the $413.4\ \mathrm{W\,m^{-2}}$ a
$\varepsilon=0.90$ surface at $300\ \mathrm{K}$ would emit. A ratio
$400/413.4 = 0.9676$ corresponds to $T = 300\times0.9676^{1/4} = 297.6\
\mathrm{K}$, i.e. the surface is slightly cooler than $300\ \mathrm{K}$, or partly
obscured. **The point of the exercise** is that brightness temperature folds three
different things together — kinetic temperature, emissivity and intervening
absorption — and cannot be inverted for temperature alone without an independent
constraint.

---

## ★10 — Specification for an albedo measurement

1. **Band.** The *reflected shortwave* band, roughly $0.3$–$4\ \mu\mathrm{m}$, and
   not the total, because the terrestrial emission in that band is
   $<1\%$ (lesson §5) and can be neglected. The albedo is a *ratio* of reflected to
   incident shortwave flux, so both must be measured in the same band.
2. **Geometry.** Albedo depends strongly on the illumination and viewing geometry
   (the *bidirectional reflectance*). A single viewing angle gives a
   bidirectional reflectance, **not** an albedo. A valid albedo measurement requires
   either (i) sampling enough angles to integrate over the viewing hemisphere at
   each illumination condition, or (ii) a stated angular model with its own
   uncertainty, or (iii) a broadband radiometer whose field of view is wide enough
   to average the angular structure — and then that averaging must be justified.
3. **Metric.** The ratio of the hemispherically integrated reflected flux to the
   incident flux density, as a function of latitude and time; the *global annual
   mean* is then an average of that field weighted by incident flux, not a simple
   spatial mean.
4. **Confounders.** *Instrumental:* a change in the sensor's calibration or
   spectral response between epochs mimics an albedo change; the standard defence
   is overlapping observations and a common reference. *Physical:* a change in
   cloud amount and a change in surface type can produce the same broadband albedo
   change, and separating them requires the spectral information that a single
   broadband channel destroys.
5. **Falsification.** A claim that the albedo changed between two epochs is
   falsified by showing that the difference disappears when both records are
   reprocessed with a single calibration, or that the difference is present in a
   band where the alleged physical cause could not act. Both are checkable, and
   neither requires new measurements.

---

## ★11 — The peak in frequency space, and why there is no contradiction

The frequency form of the Planck function is derived from
$B_\nu = B_\lambda\,\left|\mathrm{d}\lambda/\mathrm{d}\nu\right|$ with
$\nu = c/\lambda$:

$$B_\nu(T) = \frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/(k_BT)}-1}.$$

Maximising $\nu^3/(e^{y}-1)$ with $y = h\nu/(k_BT)$ gives
$3(1-e^{-y}) = y$, whose root is $y = 2.821439$. So

$$\nu_{\max} = 2.821439\,\frac{k_B}{h}\,T
= 5.87892\times10^{10}\,T\ \mathrm{Hz\,K^{-1}}
\quad (= 58.789\ \mathrm{GHz\,K^{-1}}).$$

At $T = 5772\ \mathrm{K}$: $\nu_{\max} = 3.3933\times10^{14}\ \mathrm{Hz}$,
corresponding to $\lambda = c/\nu = 0.884\ \mu\mathrm{m}$ — while the
wavelength-space peak is at $0.502\ \mu\mathrm{m}$. The two differ by
$4.965114/2.821439 = 1.7597$.

**No contradiction.** $B_\lambda$ and $B_\nu$ are *densities*, and a density's
maximum moves when the coordinate is transformed because the transformation
compresses one axis and stretches the other. The energy in a fixed interval
$[\lambda, \lambda+\mathrm{d}\lambda]$ is the same computed either way; only the
location of the peak of the density is coordinate-dependent. "The peak of the
solar spectrum" is therefore an incomplete statement without the variable.

**Practical consequence.** Two published solar or terrestrial spectra plotted
against different variables will disagree about the peak wavelength by up to a
factor $1.76$ without either being wrong. When comparing, always check (i) which
variable is on the abscissa, (ii) whether the ordinate is radiance, radiance per
unit wavenumber, or flux, and (iii) whether a logarithmic scale hides the fact
that the peak is a very weak maximum (the Planck function around its peak is
nearly flat, so a $76\%$ shift in the peak position changes the local ordinate by
only a few per cent).

---

## ★12 — Uncertainty budget for $T_e = 254.58\ \mathrm{K}$

$$T_e = \left(\frac{S(1-a)}{4\sigma}\right)^{1/4}
\;\Longrightarrow\;
\frac{\delta T_e}{T_e} = \frac{1}{4}\left(\frac{\delta S}{S}
+ \frac{\delta a}{1-a}\right).$$

| term | source | how it propagates | relative size |
|---|---|---|---|
| (i) solar constant | measurement; also the annual orbit eccentricity ($\pm3.4\%$ in $S$ over the year, which the mean value averages out) | $\frac{1}{4}\frac{\delta S}{S}$ | smallest of the four, but not zero |
| (ii) albedo | clouds, ice, surface; the albedo also *responds* to temperature, so it is not an independent parameter | $\frac{1}{4}\frac{\delta a}{1-a} = 0.357\,\delta a$ | large: $\delta a = 0.03$ gives $\delta T_e = 2.7\ \mathrm{K}$, twice the size of a $1\%$ solar-constant error |
| (iii) the blackbody, no-atmosphere model | physical, not instrumental — the real planet has an atmosphere, an emissivity below 1, and an internal heat source | not a small perturbation: this is the whole greenhouse effect | dominant; it is why $254.6\ \mathrm{K}$ is a reference and not a prediction |
| (iv) uniform absorption of sunlight | geometry — absorption is strongly latitude-dependent | not a perturbation to $T_e$ but to the *pattern*; it does not change the global mean by more than the albedo's latitude dependence already accounts for | moderate, and it is absorbed into (ii) if the albedo is taken as an annual global mean |

**Dominant term: (iii).** The reason is structural rather than numerical. Terms (i)
and (iv) are perturbations about a physical model that is at least approximately
right; term (ii) is a real uncertainty in a real parameter; but term (iii) is the
statement that the model has *omitted the phenomenon of interest*. A budget that
lists the first three and omits the fourth would report an uncertainty an order of
magnitude too small — and that is exactly the error this lesson's "climate-claim
discipline" paragraph is written to prevent. The honest statement is:
"$254.58\ \mathrm{K}$ is the equilibrium temperature of a blackbody with albedo
$0.30$, computed from standard constants; it is a reference for measuring the
greenhouse effect, with the modelling error dominated by the absence of an
atmosphere."
