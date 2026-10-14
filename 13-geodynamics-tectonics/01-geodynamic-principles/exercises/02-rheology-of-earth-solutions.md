# Solutions — 13-01-02 Rheology: Elastic, Viscous, Plastic and Power-Law Creep

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Units are carried through; $R = 8.314\ \mathrm{J\,mol^{-1}\,K^{-1}}$ and
> $g = 9.81\ \mathrm{m\,s^{-2}}$.

Lesson: [02 Rheology](../02-rheology-of-earth.md).

---

## ★1 — Maxwell time and Deborah number

$$t_M = \frac{\eta}{\mu} = \frac{5\times10^{20}}{7\times10^{10}}
= 7.143\times10^{9}\ \mathrm{s}
= \frac{7.143\times10^{9}}{3.1557\times10^{7}} = 226.3\ \mathrm{yr} .$$

$$De = \frac{t_M}{t_{\text{obs}}} = \frac{226.3}{10^{6}} = 2.26\times10^{-4} .$$

$De\ll1$: over a million years the material has relaxed its elastic strain many
thousands of times over, so it responds as a viscous fluid even though a seismic
wave crossing it in a second sees an elastic solid.

---

## ★2 — Effective viscosity at 50 MPa

$$e^{E/RT} = \exp\!\left(\frac{350\times10^{3}}{8.314\times1600}\right)
= e^{26.31} = 2.674\times10^{11},$$

$$\eta_{\text{eff}} = \frac{e^{E/RT}}{2A\sigma^{\,n-1}}
= \frac{2.674\times10^{11}}{2(2\times10^{-28})(5\times10^{7})^{2.5}} .$$

$(5\times10^{7})^{2.5} = 5^{2.5}\times10^{17.5} = 55.90\times3.162\times10^{17}
= 1.768\times10^{19}$, so the denominator is
$4\times10^{-28}\times1.768\times10^{19} = 7.072\times10^{-9}$ and

$$\eta_{\text{eff}} = 3.78\times10^{19}\ \mathrm{Pa\,s} .$$

Compare the lesson's value at 10 MPa, $2.11\times10^{21}$ Pa s: a fivefold
increase in stress lowers the viscosity by a factor of 56, the $\sigma^{-2.5}$
dependence in action.

---

## ★3 — Brittle strength at 15 km

$$\sigma_b = \mu_f(1-\lambda_p)\rho g z
= (0.60)(0.60)(2750)(9.81)(1.5\times10^{4})
= 1.4568\times10^{8}\ \mathrm{Pa} = 145.7\ \mathrm{MPa} .$$

Pore pressure reduces the *effective* normal stress that friction acts on: only
the difference between lithostatic and pore pressure is clamped by the friction
law, so a pore factor of 0.40 removes 40% of the strength and does so at every
depth.

---

## ★★4 — Interpolating the brittle–ductile transition

**Assumption:** the transition depth varies smoothly with the geotherm, so linear
interpolation between the two tabulated geotherms is adequate over a 5 K/km
step. Using the crust values (21.63 km at 10 K/km, 11.76 km at 20 K/km):

$$z(15) \approx \frac{21.63 + 11.76}{2} = 16.70\ \mathrm{km}
\quad\text{(crust)},$$

$$z(15) \approx \frac{69.45 + 37.28}{2} = 53.37\ \mathrm{km}
\quad\text{(mantle)} .$$

**Is the interpolation accurate?** Probably to about a kilometre, and the reason
is structural rather than empirical. The transition is where a
linearly-growing function ($\sigma_b\propto z$) meets an exponentially decaying
one ($\sigma_d\propto e^{E/nRT}$), so $z$ varies smoothly with the temperature
gradient; but the exponential makes the local slope of $z(\gamma)$ largest at
small $\gamma$, so linear interpolation over a 10 K/km interval *overestimates*
$z$ at the midpoint. The check is cheap: run the bisection at 15 K/km. Note also
that the two branches are governed by different flow laws, so the crustal and
mantle transitions do not scale identically.

---

## ★★5 — The two slopes, applied to two shear zones

**(a)** At constant strain rate and at constant stress:

$$\frac{\mathrm{d}\log\eta_{\text{eff}}}{\mathrm{d}\log\sigma} = 1-n = -2.5,
\qquad
\frac{\mathrm{d}\log\eta_{\text{eff}}}{\mathrm{d}\log\dot\varepsilon}
= \frac{1-n}{n} = \frac{-2.5}{3.5} = -0.7143 .$$

They differ because the two experiments change different things. Holding stress
fixed and doubling strain rate means the material must be *weaker*; holding
strain rate fixed and doubling stress means the material must be *stronger*. The
same physical law produces two different partial derivatives, and quoting "the
stress exponent of viscosity" without saying which variable is held fixed is
ambiguous by a factor of $n = 3.5$.

**(b)** $u = 30\ \mathrm{mm\,yr^{-1}} = 9.507\times10^{-10}\ \mathrm{m\,s^{-1}}$.

| zone | $\dot\varepsilon = u/d$ (s$^{-1}$) | $\eta_{\text{eff}}$ (Pa s) | $\tau = 2\eta\dot\varepsilon$ |
|---|---|---|---|
| 5 km | $1.9013\times10^{-13}$ | $1.2201\times10^{20}$ | 46.40 MPa |
| 50 km | $1.9013\times10^{-14}$ | $6.3194\times10^{20}$ | 24.03 MPa |

The thin zone is *weaker* (viscosity lower by a factor of
$10^{-0.7143} = 0.193$) and yet carries the *larger stress* (higher by
$10^{0.2857} = 1.93$). The resolution is that stress is not viscosity: with
$\eta\propto\dot\varepsilon^{-0.714}$ the product
$\tau = 2\eta\dot\varepsilon \propto \dot\varepsilon^{1/n} =
\dot\varepsilon^{0.286}$ still increases with strain rate. Shear-thinning softens
the material, but not fast enough to offset the imposed increase in strain rate —
which is exactly why localized shear zones are hot places rather than weak ones.

---

## ★★6 — Viscosity from a postseismic relaxation

Half relaxed after 5 yr means $1 - e^{-t/t_M} = 0.5$, so
$t_M = t/\ln 2 = 5/0.6931 = 7.213\ \mathrm{yr}$:

$$\eta = \mu t_M = (7\times10^{10})(7.213\times3.1557\times10^{7})
= 1.593\times10^{19}\ \mathrm{Pa\,s} .$$

**Why it could be wrong by an order of magnitude.** The Maxwell model has a
single relaxation time, but a real postseismic signal is a superposition of
modes with different decay rates set by the *geometry* of the viscoelastic body —
a low-viscosity channel at depth, a finite-thickness plate, a depth-varying
viscosity. Fitting one exponential to such a superposition recovers an
"effective" time that can differ from any physical relaxation time by a factor of
several, and the amplitude is contaminated by afterslip, poroelastic rebound and
the unknown fault slip distribution.

---

## ★★★7 — A laboratory design

**Stress range.** At least two decades, e.g. $50$–$5000$ MPa in simple shear or
axial compression, so that the curvature of $\log\dot\varepsilon$ versus
$\log\sigma$ is measurable rather than assumed.

**Temperature range.** At least 200 K, e.g. 1473–1673 K, with the range chosen so
the strain rate stays measurable (roughly $10^{-7}$ to $10^{-4}\ \mathrm{s^{-1}}$)
at every condition.

**Design.** A full factorial grid of $5$ stresses $\times$ $4$ temperatures
$= 20$ conditions, each replicated three times; 60 experiments.

**Noise model.** Multiplicative log-normal noise on $\dot\varepsilon$ at 10%,
plus a systematic 5 K uncertainty in temperature and a 3% uncertainty in the
measured stress; the temperature error is the one that matters, because
$\partial\ln\dot\varepsilon/\partial T = E/(RT^{2})$ is large.

**Metrics.** (i) the posterior standard deviation of $n$, which should be below
0.1 for a useful flow law; (ii) the correlation coefficient between $A$ and $E$;
(iii) the residual rms in $\log\dot\varepsilon$, which should match the imposed
noise.

**Why $A$ and $E$ are always correlated.** The measured quantity is
$A\,e^{-E/RT}$, which depends on $A$ and $E$ only through the combination
$\ln A - E/RT$. Over a finite temperature range the two parameters shift the
strain rate in nearly the same direction, so the data determine the *combination*
well and the split poorly; the correlation is a property of the model
parameterisation, not of the apparatus.

---

## ★★★8 — Why $\eta_{\text{eff}}$ must be re-evaluated every iteration

The Stokes problem is nonlinear: the viscosity depends on the stress, and the
stress depends on the velocity, which depends on the viscosity. The standard
treatment is a Picard (fixed-point) or Newton iteration in which each sweep solves
a *linear* Stokes problem with the viscosity frozen at the previous estimate, then
updates $\eta_{\text{eff}}$ from the new stress. Because
$\eta_{\text{eff}} = \sigma/(2\dot\varepsilon)$ is itself a function of both the
stress and strain rate, computing it once at the start is equivalent to assuming
the flow field does not change — that is, to solving a constant-viscosity problem
with a misleading label.

**Failure mode if not updated.** The converged solution is that of a
constant-viscosity fluid with the *initial* viscosity structure, so a
strain-weakening shear zone never forms and the solution remains artificially
diffuse: heat flux and velocity are wrong by tens of per cent, and the code can
appear to converge beautifully to the wrong answer. A diagnostic that catches
this: verify that the final solution satisfies $\eta_{\text{eff}} =
\sigma/(2\dot\varepsilon)$ *pointwise* to the iteration tolerance. A code that
never updates cannot pass that check.

---

## ★★★9 — Making "no single mantle viscosity" precise

*Model answer.* What is well defined is a constitutive *law*: a relation between
stress, strain rate, temperature, pressure, grain size and chemistry. Given those
arguments, $\eta_{\text{eff}}$ is unambiguous and reproducible. What does not
exist is a single number that describes the mantle, for three reasons. (i) The
stress dependence: a power law with $n = 3.5$ means $\eta$ falls as
$\sigma^{-2.5}$, so the same rock at the same temperature is
$10^{2.5}\approx300$ times weaker at 100 MPa than at 10 MPa. (ii) The
temperature dependence: measured here as a factor of $6.4\times10^{3}$ between
1200 K and 1600 K, so a 400 K variation spans nearly four decades. (iii) The
mechanism: diffusion creep (Newtonian) and dislocation creep (power law) dominate
on either side of a crossover stress of about 15 MPa, and the crossover moves with
grain size.

An observational consequence follows directly: because viscosity is
temperature-dependent, a convecting mantle cannot have a uniform viscosity. The
cold surface boundary layer must be orders of magnitude stiffer than the
interior, which is why the surface does not participate in the overturning and why
a *lid* — on Earth, a broken one that subducts — exists at all. Reported
"viscosities" are therefore effective values averaged over a depth range, a
mechanism, and a stress level, and any such value must be quoted with those
three qualifiers attached.
