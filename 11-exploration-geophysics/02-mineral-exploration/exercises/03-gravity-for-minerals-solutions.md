# Solutions — 11-02-03 Gravity for Chromite, Massive Sulphide and Iron Ore

> **Read after attempting the exercises.** Numbers below were computed, not
> estimated. All contrasts, geometries and reduction densities are **SYNTHETIC**.

Lesson: [03 Gravity for Minerals](../03-gravity-for-minerals.md).

---

## ★1 — Sphere versus cylinder, same geometry

$$V = \frac{4}{3}\pi(90)^{3} = 3.0536\times10^{6}\ \mathrm{m^{3}},$$

sphere:
$$\Delta g = \frac{4}{3}\pi G\Delta\rho\frac{R^{3}}{z^{2}}
= \frac{4}{3}\pi(6.67430\times10^{-11})(450)
\frac{7.29\times10^{5}}{3.24\times10^{4}} = 2.8307\times10^{-6}\ \mathrm{m\,s^{-2}}
= 0.2831\ \mathrm{mGal}.$$

cylinder:
$$\Delta g = \frac{2\pi G\Delta\rho R^{2}}{z}
= \frac{2\pi(6.67430\times10^{-11})(450)(8100)}{180}
= 8.4920\times10^{-6}\ \mathrm{m\,s^{-2}} = 0.8492\ \mathrm{mGal}.$$

$$\text{ratio} = \frac{0.8492}{0.2831} = 3.00 .$$

The factor of exactly three at $z = 2R$ is the geometry of this example, not a
universal constant: the ratio is $\tfrac{3z}{2R}$ for a sphere and cylinder of
equal radius, so it grows without bound with depth.

---

## ★2 — Excess mass and the cross-check

$$\lambda = \pi R^{2}\Delta\rho = \pi(90)^{2}(450) = 1.14511\times10^{7}
\ \mathrm{kg\,m^{-1}},$$

$$\frac{2G\lambda}{z} = \frac{2(6.67430\times10^{-11})(1.14511\times10^{7})}{180}
= 8.4920\times10^{-6}\ \mathrm{m\,s^{-2}} = 0.8492\ \mathrm{mGal}.\ \checkmark$$

The two routes agree by construction, which is the point: the amplitude and the
mass are two views of the same quantity, and neither contains the depth
independently of the shape.

---

## ★3 — The two depth rules

**Cylinder rule (exact):** $x_{1/2} = z$, so a measured $180\ \mathrm{m}$ gives
$z = 180\ \mathrm{m}$.

**Sphere rule (calibrated):**
$$z = \frac{x_{1/2}}{\sqrt{2^{2/3}-1}} = \frac{180}{0.766421}
= 234.86\ \mathrm{m}.$$

The two rules disagree by $30.5\%$ on identical data. Nothing in the profile
distinguishes them **unless the strike extent is known or measured**: that is the
shape problem, and it is why a real program flies or walks perpendicular profiles.

---

## ★4 — Corrections from standard constants

Free-air:
$$\frac{2g}{a} = \frac{2(9.80665)}{6.371\times10^{6}} = 3.078528\times10^{-6}
\ \mathrm{s^{-2}} = 0.3079\ \mathrm{mGal\,m^{-1}}.$$

Bouguer slab at $\rho = 2400$:
$$2\pi G\rho = 2\pi(6.67430\times10^{-11})(2400) = 1.00646\times10^{-6}
\ \mathrm{s^{-2}} = 0.1006\ \mathrm{mGal\,m^{-1}}.$$

For $200\ \mathrm{m}$ of relief:
free-air $= +0.3079(200) = +61.57\ \mathrm{mGal}$;
slab $= -0.1006(200) = -20.13\ \mathrm{mGal}$; **net $= +41.44\ \mathrm{mGal}$**.

The net is larger than either the target anomaly in ★1 or the one in ★5 by two
orders of magnitude: the corrections are not refinements, they are the dominant
terms, and the target is what remains after two large numbers cancel.

---

## ★5 — What a peak and a half-width can and cannot determine

Cylinder rule: $z = x_{1/2} = 300\ \mathrm{m}$.

$$\lambda = \frac{\Delta g(0)\,z}{2G}
= \frac{(2.400\times10^{-5})(300)}{2(6.67430\times10^{-11})}
= 5.3938\times10^{7}\ \mathrm{kg\,m^{-1}},$$

$$R = \sqrt{\frac{\lambda}{\pi\Delta\rho}} = \sqrt{\frac{5.3938\times10^{7}}
{\pi(750)}} = 151.3\ \mathrm{m}\quad(\Delta\rho = 750\ \mathrm{kg\,m^{-3}}).$$

**A sphere fitting the same two numbers:** the sphere rule gives
$z = 300/0.766421 = 391.4\ \mathrm{m}$, and matching the peak
$2.400\ \mathrm{mGal}$ requires

$$R^{3} = \frac{2.400\times10^{-5}(391.4)^{2}}
{\frac{4}{3}\pi(6.67430\times10^{-11})(750)} \Longrightarrow R = 259.8\ \mathrm{m}.$$

**The data cannot exclude either model.** Both reproduce the peak and the
half-width exactly, and they differ in depth by **$30\%$** and in shape entirely.
The two models are not equally plausible *geologically* — a 2-D chromite
stratiform body is nothing like a sphere — and that geological prior is what a
working interpreter actually uses. It is a prior, not a measurement, and it must be
stated.

---

## ★6 — Window required for a stated mass recovery

$$\frac{\lambda_{\text{rec}}}{\lambda} = \frac{2}{\pi}\arctan\!\left(\frac{X}{z}\right)
\;\Longrightarrow\; X = z\tan\!\left(\frac{\pi}{2}\frac{\lambda_{\text{rec}}}{\lambda}\right).$$

At $z = 400\ \mathrm{m}$:

- $90\%$: $X = 400\tan(0.45\pi) = 400(6.3138) = 2.53\times10^{3}\ \mathrm{m}$.
- $95\%$: $X = 400\tan(0.475\pi) = 400(12.7062) = 5.08\times10^{3}\ \mathrm{m}$.

**Practical consequence.** A survey whose stations cover $\pm3\ \mathrm{km}$ at
$z = 400\ \mathrm{m}$ achieves
$(2/\pi)\arctan(3000/400) = (2/\pi)(1.4382) = 0.9155$, i.e. **91.6% of the mass**.
Reporting the raw integral as the mass understates it by $8.4\%$; dividing by the
formula's efficiency gives an unbiased estimate *provided the regional has been
removed correctly*, because the tail of the anomaly is exactly where a fitted
regional contaminates the integral most.

---

## ★7 — Height accuracy and the error budget

At $\rho = 2670\ \mathrm{kg\,m^{-3}}$: free-air $0.3079\ \mathrm{mGal\,m^{-1}}$,
slab $0.1120\ \mathrm{mGal\,m^{-1}}$.

For $80\ \mathrm{m}$ of relief: free-air $= +24.63\ \mathrm{mGal}$, slab
$= -8.96\ \mathrm{mGal}$, net $= +15.67\ \mathrm{mGal}$.

**A $0.5\ \mathrm{m}$ height error:** free-air $= 0.154\ \mathrm{mGal}$, slab
$= 0.056\ \mathrm{mGal}$, net $= 0.098\ \mathrm{mGal}$ — a fifth of the
$0.5\ \mathrm{mGal}$ target from height error alone, on every station.

**For a $0.02\ \mathrm{mGal}$ budget:** with only the free-air term,
$\delta h = 0.02/0.3079 = 0.065\ \mathrm{m}$; with the slab included so that the
two partially cancel, $\delta h = 0.02/(0.3079-0.1120) = 0.102\ \mathrm{m}$.

**Interpretation and caveat.** Both numbers say the same thing: differential GNSS
heights good to a few centimetres are a *prerequisite*, not a refinement, for
microgal-level work. The cancellation in the second number is not a free lunch —
it holds only if the slab is computed with the **same** density used in the
reduction, and the difference $(0.3079-0.1120)$ is itself the quantity that must be
correct. An error of $100\ \mathrm{kg\,m^{-3}}$ in the reduction density contributes
$2\pi G(100)t = 4.19\times10^{-3}\ \mathrm{mGal}$ per metre of slab thickness —
$0.335\ \mathrm{mGal}$ over the $80\ \mathrm{m}$ of relief here, i.e. $67\%$ of the
$0.5\ \mathrm{mGal}$ target.

---

## ★8 — How much the regional choice moves the answer

Linear to quadratic: residual peak
$(1.3315-1.1792)/1.3315 = 11.4\%$; implied depth
$(199.7-191.5)/199.7 = 4.1\%$.

Quadratic to cubic: residual peak $0\%$; implied depth $0\%$ — the two fits are
identical to four decimals, which is what one expects when the true field contains
no cubic term.

**What the second comparison tells you.** The agreement is *evidence that the
regional model is sufficient*, but only weak evidence: adding a polynomial term
that the data do not require cannot change a least-squares fit much, so a plateau
between orders 2 and 3 is the expected behaviour whether or not the true regional
is quadratic. It does **not** license the claim that the residual is correct. The
stronger test is the independent one: require the residual to be flat outside the
anomalous area, or compare against a regional derived from a wider survey. A depth
quoted from a polynomial regional is conditional on that polynomial, and the
$4\%$–$11\%$ spread measured here is the *lower bound* on that conditionality.

---

## ★9 — An explicit exact non-uniqueness (the sheet annihilator)

**Construction.** An infinite horizontal sheet of surface density
$\sigma = \rho t$ produces the vertical attraction

$$\Delta g_{\text{sheet}} = 2\pi G\sigma,$$

**independent of the observer's height** — the standard result derived in the
lesson's §4.2. It follows immediately that two sheets of equal $\sigma$ at
*different* depths are indistinguishable, and that the composite model

$$\text{model} \;+\; \bigl[+\sigma \text{ at depth } z_1\bigr]
\;+\;\bigl[-\sigma \text{ at depth } z_2\bigr]$$

produces **exactly** the same vertical attraction as the original model, for any
$z_1 \ne z_2$.

**Numerical verification.** For $\sigma = 500\ \mathrm{kg\,m^{-2}}$,
$2\pi G\sigma = 2\pi(6.67430\times10^{-11})(500) = 2.0968\times10^{-5}
\ \mathrm{m\,s^{-2}} = 0.020968\ \mathrm{mGal}$ at **every** height — the
demonstration's §4.2 table is the same computation with $t = 1\ \mathrm{m}$. The
composite therefore contributes $0.020968 - 0.020968 = 0$ to machine precision
(the difference computes to exactly $0$ in double precision), for $z_1 = 1\
\mathrm{km}$ and $z_2 = 5\ \mathrm{km}$ alike.

**What this implies.** A gravity map constrains only the **excess mass** (and,
through shape-dependent features, the depth of the *centre of mass*). It cannot
determine how that mass is distributed in depth: a thick low-density layer and a
thin high-density layer at different depths can be *exactly* equivalent. This is
not a practical limitation of instruments or coverage — it is a property of the
field equations, and it is the same structure that makes the excess-mass integral
of §6.1 the only exact shape-free invariant available. **Consequence for practice:**
a gravity-only model of a layered target (a chromite seam, a stratified iron
formation) has an unresolvable density–thickness trade-off; drill holes or
petrophysics must supply the split.

---

## ★10 — Distinguishing a cylinder from a sphere with few measurements

**Geometry.** Two perpendicular profiles through the anomaly maximum, plus a
short crossing profile at one end of the strike extent. A 2-D body shows a
*constant* anomaly along strike over distances comparable to the depth, whereas a
3-D body decays in every horizontal direction.

**Discriminating quantity.** The **ratio of the anomaly at the centre to the
anomaly at $N$ depths along strike**, at a fixed separation $d$: for an infinite
cylinder the ratio is $1$ (no decay), for a sphere it is
$\left(1+d^{2}/z^{2}\right)^{-3/2}$ at the same separation in the strike direction.
A more sensitive second quantity is the $x_{1/2}$ ratio between the two
perpendicular profiles.

**Number of stations.** Let the target depth be $z$ and the required discrimination
be between $x_{1/2}$ ratios of $1.00$ (cylinder) and $0.766$ (sphere). With a
per-station noise of $0.02\ \mathrm{mGal}$ and a peak of $0.85\ \mathrm{mGal}$
(solution ★1), the anomaly at $d = z$ has amplitude $2^{-3/2} = 0.35$ of the peak,
i.e. $0.30\ \mathrm{mGal}$, which is $15\sigma$. Ten stations at separations of
$z/2$ along strike are therefore ample to detect the along-strike decay; the
limiting factor is not noise but the *geological* deviation from both models, so
the design should specify an acceptable misfit rather than a station count.

**Testing the design.** Before committing, build a synthetic benchmark: forward
model a *finite* cylinder ($L/z = 3$, the worst case a program will meet) with a
taper, add the survey noise, and run both interpretations. Report the success rate
of the correct classification over ~100 noise realisations, and the fraction of
cases in which the 2-D model fits within the stated misfit. If that fraction is
high, the design cannot achieve its purpose whatever the station count — which is
exactly the information a design study exists to produce.

---

## ★11 — Propagating an uncertain density contrast

Target geometry: cylinder of $R = 120\ \mathrm{m}$ at $z = 250\ \mathrm{m}$;
$\Delta\rho$ between $300$ and $900\ \mathrm{kg\,m^{-3}}$ (a factor of three).

**(a) Peak amplitude** $\Delta g(0) = 2\pi G\Delta\rho R^{2}/z$: proportional to
$\Delta\rho$, so it ranges from
$$\frac{2\pi(6.6743\times10^{-11})(300)(14400)}{250}
= 7.25\times10^{-6}\ \mathrm{m\,s^{-2}} = 0.725\ \mathrm{mGal}$$
to $2.175\ \mathrm{mGal}$. **Strongly dependent** — a factor of three.

**(b) Depth from the half-width:** $z = x_{1/2}$ exactly, and no density term
appears in the derivation. The depth is **independent of $\Delta\rho$** for a 2-D
body — the single most valuable property of the cylinder rule.

**(c) Mass from the excess-mass integral:**
$\lambda = \pi R^{2}\Delta\rho$ ranges from
$\pi(120)^{2}(300) = 1.357\times10^{7}$ to
$4.072\times10^{7}\ \mathrm{kg\,m^{-1}}$ — **strongly dependent**, in fact exactly
proportional, because the recovered quantity is the mass, and the mass is what the
density contrast scales.

**Summary.** The **depth is robust and the amplitude and mass are not**. This is
the correct way to report a gravity result on a target of uncertain density: state
the depth (with its shape caveat), and state the mass *per unit assumed density
contrast*, e.g.
$\lambda/\Delta\rho = \pi R^{2} = 4.52\times10^{4}\ \mathrm{m^{2}}$ — a quantity
that requires no density assumption at all, and from which a reader can recover the
mass for any density they prefer. Reporting a mass without its density assumption
is the gravity equivalent of reporting a reserve without a price.
