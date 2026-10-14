# Solutions — 13-06-03 Glacial Isostatic Adjustment

> **Read after attempting the exercises.** Numbers were computed with the same
> formulas as the lesson's demonstration.

Lesson: [03 Glacial Isostatic Adjustment](../03-glacial-isostatic-adjustment.md).

---

## ★1 — Relaxation time

$$\tau = \frac{4\pi\eta}{\rho g\lambda}
= \frac{4\pi\times5.0\times10^{20}}{3300\times9.81\times2.5\times10^{6}}
= \frac{6.283\times10^{21}}{8.093\times10^{10}} = 7.764\times10^{10}\ \mathrm{s},$$

$$\tau = \frac{7.764\times10^{10}}{3.1557\times10^{7}} = \mathbf{2460\ yr}.$$

(Agreement check: the lesson's $\eta = 5\times10^{20}$ row at $\lambda = 3000$ km
gives 2051 yr; scaling as $1/\lambda$ gives $2051\times3000/2500 = 2461$ yr ✓.)

---

## ★2 — Equilibrium deflection

$$w_{\text{eq}} = \frac{917}{3300}\times2500 = 0.2779\times2500
= \mathbf{694.7\ m}.$$

This is the Airy value for a load on a fluid half-space: the ice displaces mantle
material whose density is 3.6 times the ice density, so the deflection is about
28% of the ice thickness.

---

## ★3 — Remaining fraction

$$\exp(-t/\tau) = \exp(-12000/4000) = e^{-3} = 0.0498 .$$

About 5% of the deflection remains 12 kyr after unloading — which, multiplied by
the ~700 m equilibrium deflection, is a few tens of metres, still rising at a
measurable rate.

---

## ★4 — Present-day uplift rate

Remaining deflection $= 0.0498\times694.7 = 34.6$ m. The present rate is that
deflection divided by the relaxation time, because the decay is exponential:

$$\text{rate} = \frac{34.6\ \mathrm{m}}{4000\ \mathrm{yr}}
= 8.65\times10^{-3}\ \mathrm{m/yr} = \mathbf{8.65\ mm/yr}.$$

Two factors are combined: **how much deflection is left** (which grows with
viscosity, because a stiffer mantle has responded less by the time the ice is
removed) and **how fast it decays** (which falls with viscosity). Their product
is maximised at an intermediate value.

---

## ★5 — Why the maximum is at an intermediate viscosity

A very low viscosity means the mantle finished relaxing long before the present
(little deflection left, so little current uplift); a very high viscosity means
the mantle has barely responded to the unloading (the deflection persists but
changes slowly, so again little current uplift). Between the two there is a
viscosity for which the residual deflection is large *and* the decay is fast
enough to produce a measurable rate. Measured at $\lambda = 3000$ km, the uplift
is 0.000, 0.057, 8.944, 12.453, 2.986 and 0.444 mm/yr for
$\eta = 10^{20}, 3\times10^{20}, 10^{21}, 3\times10^{21}, 10^{22}, 3\times10^{22}$
Pa s: the maximum lies near $3\times10^{21}$ Pa s, i.e. where
$\tau \approx 12$ kyr, comparable with the time since unloading.

---

## ★6 — Eustatic versus isostatic

Ice volume $= 10^{6}\ \mathrm{km^2}\times2\ \mathrm{km} = 2.0\times10^{6}\ \mathrm{km^3}
= 2.0\times10^{15}\ \mathrm{m^3}$.

$$\Delta\text{RSL}_{\text{eustatic}} = -\frac{\Delta V}{A_{\text{ocean}}}
= -\frac{2.0\times10^{15}}{3.6215\times10^{14}} = \mathbf{-5.52\ m} .$$

The measured isostatic deflection at the load centre reaches 526.7 m (at
$-12$ ka) and 36.2 m today. **The isostatic term is between 100 and 80 times
larger than the eustatic term** for this ice area: near a former ice sheet,
relative sea level is a measurement of the solid-Earth response, not of the ice
volume.

---

## ★7 — The centre-to-flank ratio

The ratio is exactly 2 because the model deflection is
$w(x) = w_0\cos(kx)$ and the flank site was defined by $\cos kx = 0.5$: the
deflection, and therefore the relative sea-level rate, is proportional to
$\cos kx$ at every time. The eustatic term is common to both sites and is
negligible here.

If the solid-Earth response were ignored, a worker would attribute the entire
relative sea-level fall to a eustatic rise (or fall) of the *opposite* sign: the
flank record falls at 4.47 mm/yr, which would be read as 4.47 mm/yr of sea-level
fall, i.e. about 0.45 m per century of apparent global sea-level change from an
ice sheet that no longer exists. The error is the whole signal.

---

## ★8 — Discriminating the two branches

**Observable.** The *spatial pattern* of the present-day gravity change or of the
geoid rate: the two branches differ in the ratio of their short-wavelength to
long-wavelength response because the deflection's spatial form differs (a
shallower, thinner ice sheet with a low-viscosity mantle produces a
more localised, faster-relaxing pattern than a thick load on a stiff mantle).

**Wavelength band.** Where the two branches differ most, i.e. at wavelengths
comparable with the load's own width (hundreds of kilometres) and shorter —
$\lambda \lesssim \lambda_c$, since at longer wavelengths both branches relax
quasi-uniformly and look alike. This is why GRACE-class gravity rates at
200–500 km wavelengths are the standard discriminator.

**Precision required.** The branch separation must exceed the gravity-rate
uncertainty (a few mm/yr in equivalent water height for a multi-year solution).
Since the two branches differ by a factor of several in the *rate of change* of
the gravity field, this is achievable in principle — which is exactly why
gravity-rate observations, and not uplift rates, are the standard tool.

---

## ★9 — A synthetic recovery test

**Truth.** A two-layer viscosity profile: a lithosphere with $\eta = 10^{25}$ Pa s
(the model's $\tau$ then depends on the mantle below), an upper mantle of
$10^{20}$ Pa s to 400 km and a lower mantle of $3\times10^{21}$ Pa s beneath.
Prescribed ice history: the synthetic two-step history of the lesson.

**Observables.** Synthetic (i) present-day uplift rates at 20 sites on a grid,
(ii) present-day gravity rates, (iii) three relative sea-level curves, each with
stated Gaussian noise of a realistic size (1 mm/yr, and 0.5 m on sea level).

**Metric.** The recovered profile plotted against the truth with its posterior
(or admitted) envelope; the misfit, and the *resolution* — how much the recovered
profile changes when a narrow perturbation of the truth is applied (the
resolution matrix, as in 18-02-05).

**What success looks like.** The upper-mantle viscosity recovered to within a
factor of two, the lower-mantle value much less well (a factor of three to five),
and the *transition depth* resolved to no better than a few hundred kilometres.
Those numbers would be the honest claim, not "the viscosity profile has been
determined".

---

## ★10 — The water load and self-gravitation

**(a) Relaxation time.** The water load is added to the ice load offshore, so the
effective surface load is larger and longer-lived than the ice alone; for the same
mantle it lengthens the time over which the load changes, and it also adds a
*direct* load on the ocean floor at the ice margin. Self-gravitation changes the
surface gravity field as mass is redistributed, which modifies the equilibrium
deflection by a few per cent and hence the effective $\tau$ at long wavelengths.
Both are small effects on $\tau$ at 3000 km; the dominant effect is the load
history, not the load type.

**(b) Relative sea level near the margin.** This is where the two dominate. The
water load is applied *where the sea is*, so it depresses the seafloor in the
peripheral region — producing the observed peripheral forebulge and, in the
records, a relative sea-level *rise* followed by a fall, which the ice-only model
does not reproduce. Self-gravitation adds a smaller, smooth contribution: as the
ice sheet grows, the sea surface near it is gravitationally attracted upward, so
the local sea level is higher than the global average during glaciation, and this
must be removed before a record can be compared with a eustatic curve.

**Which dominates at 3000 km.** The water load, because it acts directly on the
surface with a large mass distributed over exactly the region where the relative
sea-level records are measured. Self-gravitation matters most at long wavelengths
because its contribution decays slowly with distance; at 3000 km its effect is a
few per cent of the deflection, while the water load changes the deflection by a
larger fraction near the margin. Both must be included in a real inversion, but
the water load is the one whose omission produces a qualitative error (a missing
sign change in the sea-level curve) rather than a quantitative bias.
