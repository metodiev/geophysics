# Exercises — 16-02-01 Solar and Terrestrial Radiation, Blackbody Laws

Attempt these before reading the
[solutions](./01-solar-and-terrestrial-radiation-solutions.md). The lesson is
[01 Solar and Terrestrial Radiation](../01-solar-and-terrestrial-radiation.md).
Use $h = 6.62607015\times10^{-34}\ \mathrm{J\,s}$,
$c = 2.99792458\times10^{8}\ \mathrm{m\,s^{-1}}$,
$k_B = 1.380649\times10^{-23}\ \mathrm{J\,K^{-1}}$,
$\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$,
$b = 2.897771955\times10^{-3}\ \mathrm{m\,K}$,
$S = 1361\ \mathrm{W\,m^{-2}}$,
$1\ \mathrm{AU} = 1.495978707\times10^{11}\ \mathrm{m}$ and
$R_\odot = 6.957\times10^{8}\ \mathrm{m}$. All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute the global-mean top-of-atmosphere insolation $S/4$ and the
effective radiating temperature for planetary albedos of $0.00$, $0.30$ and
$0.60$. State the trend and its physical meaning in one sentence.

**★2.** Compute the wavelength of peak emission for $T = 200$, $255$, $300$,
$1000$ and $5772\ \mathrm{K}$, and name the spectral region (ultraviolet, visible,
near infrared, thermal infrared) for each.

**★3.** Compute the flux density radiated by a blackbody at $300\ \mathrm{K}$ and
at $255\ \mathrm{K}$. In one sentence, explain why the ratio is $(300/255)^4$.

**★4.** A satellite measures a flux density of $100$, $238.17$ and
$400\ \mathrm{W\,m^{-2}}$ from three scenes. Compute the brightness temperature of
each.

## ★★ Applied

**★★5.** Derive Wien's displacement law completely: differentiate the Planck
function with respect to $\lambda$, show that the stationary point satisfies
$x = 5(1-e^{-x})$ with $x = hc/(\lambda k_BT)$, solve that equation numerically to
six decimal places, and compute $b = hc/(xk_B)$.

**★★6.** Derive $\sigma = 2\pi^5k_B^4/(15h^3c^2)$ from the Planck function,
showing the substitution and the value of $\int_0^\infty x^3/(e^x-1)\,\mathrm{d}x$.
Explain in one sentence where the extra factor of $\pi$ (relative to the radiance
integral) comes from, and evaluate $\sigma$ numerically.

**★★7.** Using only $S$, $1\ \mathrm{AU}$, $R_\odot$ and the blackbody laws,
compute the Sun's luminosity and effective temperature. Then compute the solar
constant and the equilibrium temperature at $\mathrm{Mars}$
($1.524\ \mathrm{AU}$, albedo $0.25$).

**★★8.** Use
$\bar F = (S/\pi)[h_0\sin\phi\sin\delta+\cos\phi\cos\delta\sin h_0]$ with
$h_0 = \arccos(-\tan\phi\tan\delta)$ to compute the daily-mean insolation at
$60^\circ\mathrm{N}$ for $\delta = 0$, $+23.44^\circ$ and $-23.44^\circ$, and the
half-day length in hours for each. State what the three numbers imply about the
seasonal cycle of the pole-to-equator temperature gradient.

**★★9.** A grey surface has emissivity $\varepsilon = 0.90$ at $300\ \mathrm{K}$.
Compute its emitted flux density. A satellite over it measures
$400\ \mathrm{W\,m^{-2}}$ and its instrument reports a brightness temperature of
$289.8\ \mathrm{K}$. Explain why the brightness temperature is lower than
$300\ \mathrm{K}$ and compute the ratio you expect.

## ★★★ Research-oriented

**★★★10.** Design a measurement of a planet's planetary albedo from orbit.
Specify: which spectral band and why, the geometry (which viewing and illumination
angles must be sampled and why), the metric, and two confounders that would bias
the answer (one instrumental, one physical). State what would falsify a claim that
the albedo has changed between two epochs.

**★★★11.** The peak of a blackbody spectrum occurs at a different wavelength when
the spectrum is plotted per unit frequency rather than per unit wavelength.
Derive the frequency-space analogue of Wien's law, compute both peaks for
$T = 5772\ \mathrm{K}$, and explain why no physical contradiction is involved. Then
state the practical consequence for anyone comparing two published spectra that do
not state which variable they are plotted against.

**★★★12.** The lesson derives $T_e = 254.58\ \mathrm{K}$ for $a = 0.30$ and calls
it a model, not a prediction. Construct a complete uncertainty budget for that
number that separates: (i) the uncertainty in the solar constant, (ii) the
uncertainty in the albedo, (iii) the error made by treating the planet as a
single-layer blackbody with no atmosphere, and (iv) the error made by assuming the
absorbed sunlight is uniformly distributed. State which term dominates, and give
your reasoning for the relative sizes rather than inventing figures.
