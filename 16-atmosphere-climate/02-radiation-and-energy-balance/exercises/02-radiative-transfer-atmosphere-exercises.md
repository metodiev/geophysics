# Exercises — 16-02-02 Radiative Transfer in the Atmosphere

Attempt these before reading the
[solutions](./02-radiative-transfer-atmosphere-solutions.md). The lesson is
[02 Radiative Transfer](../02-radiative-transfer-atmosphere.md). Use
$\sigma = 5.670374419\times10^{-8}\ \mathrm{W\,m^{-2}\,K^{-4}}$,
$S = 1361\ \mathrm{W\,m^{-2}}$ and, unless stated otherwise, planetary albedo
$a = 0.30$. All models are **SYNTHETIC**: optical depths, layer temperatures and
band shapes are chosen teaching values.

## ★ Foundational

**★1.** Compute the transmittance and the emissivity of a homogeneous layer with
optical depths $\tau = 0.2$, $0.7$ and $3.0$. State which is "optically thin" and
which is "optically thick" and why the distinction is not simply a factor of two
in $\tau$.

**★2.** For absorbed solar flux $F = 238.175\ \mathrm{W\,m^{-2}}$, compute $T_e$
and then the surface temperature of a single grey layer for
$\varepsilon = 0.1$, $0.4$, $0.8$ and $1.0$ using
$\sigma T_s^4 = 2F/(2-\varepsilon)$. Tabulate the greenhouse increment.

**★3.** A layer has optical depth $\tau = 4$ at the surface and the opacity falls
off with scale height $H_\tau = 1.5\ \mathrm{km}$. Compute the height at which
$\tau = 1$ and the height at which $\tau = 0.1$.

**★4.** Compute $T_s = (N+1)^{1/4}T_e$ for $N = 1$, $4$ and $20$ with
$T_e = 254.578\ \mathrm{K}$, and state why these numbers must not be quoted as
predictions of the Earth's temperature.

## ★★ Applied

**★★5.** Write the Schwarzschild equation and derive its formal solution for the
upward intensity at the top of the atmosphere. Identify which term dominates in
the limits $\tau_s \to 0$ and $\tau_s \to \infty$, and explain in one sentence why
the second limit is the origin of the greenhouse effect.

**★★6.** Derive the exact single-grey-layer result
$\sigma T_s^4 = 2F/(2-\varepsilon)$ from the two balance equations (top of
atmosphere and surface), showing the elimination of $T_a$. Then derive the layer
temperature $T_a$ and evaluate both for $\varepsilon = 0.6$. Verify that the layer
temperature is always below $T_e$ for $0 < \varepsilon \le 1$ and explain what that
means physically.

**★★7.** A grey atmosphere with a fixed total optical depth $\tau_s$ is
discretised into $N$ layers each of emissivity $1-e^{-\tau_s/N}$. Explain why the
surface temperature converges as $N$ grows, whereas it diverges for $N$ perfectly
black layers. Support your answer with the two limits of the layer emissivity as
$N \to \infty$.

**★★8.** A surface is at $290\ \mathrm{K}$ with a lapse rate of
$6.0\ \mathrm{K\,km^{-1}}$ above it and $T_e = 254.578\ \mathrm{K}$. Compute the
emission level $z_e$ and the total optical depth implied if the absorber's scale
height is $3\ \mathrm{km}$. Then repeat for a scale height of $1.5\ \mathrm{km}$
and state the ratio of the two required opacities.

**★★9.** For the single-layer model with $F = 238.175\ \mathrm{W\,m^{-2}}$,
compute $T_s$ at $\varepsilon = 0.90$ and at $\varepsilon = 1.00$ and compare the
increment with that obtained between $0.00$ and $0.10$. Compute the ratio of
$(\Delta T_s)/(\Delta\varepsilon)$ for the two intervals and state the lesson.

## ★★★ Research-oriented

**★★★10.** Design a numerical experiment that measures the angular-closure error
of a two-stream radiative transfer scheme as a function of total optical depth.
Specify the model, the reference solution, the metric, and the expected sign change
of the error with optical depth (the lesson measures a sign change between
$\tau_s = 1$ and $\tau_s = 8$). State what would falsify the claim that the
discrepancy is a closure error rather than a discretisation error, and how you
would distinguish them experimentally.

**★★★11.** The lesson shows that a grey model matched to a spectral model's
broadband emissivity gets the sensitivity to added absorber wrong by a factor of
about $2.4$. Design a calibration procedure that would let a grey model reproduce
the *sensitivity* as well as the flux, state the number of free parameters it needs,
and explain why a single grey optical depth can never do this. Then state which
observable would distinguish a grey model from a full spectral model in a satellite
record.

**★★★12.** Thermal radiation from the surface is carried upward partly by radiation
and partly by convection, and the two cannot both set the lapse rate. Formulate the
criterion that decides which wins (write it in terms of the radiative-equilibrium
lapse rate and the adiabatic lapse rate), explain why a *radiative–convective*
equilibrium model must impose a convective adjustment, and state what observable
difference the presence of convection makes to the outgoing spectrum. Note
explicitly which parts of your answer are derivable from this lesson and which
require assumptions you must state.
