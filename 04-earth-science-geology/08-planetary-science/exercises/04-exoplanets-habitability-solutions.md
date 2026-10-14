# Solutions — 04-08-04 Exoplanets, Habitability and Observational Constraints

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Transit depth

**(a)** $\delta = (0.02)^2 = 4.00\times10^{-4} = 400$ ppm.

**(b)** $(0.1)^2 = 0.01 = 10\,000$ ppm, i.e. 1 per cent.

**(c)** The depth depends only on the *ratio* of the planet's radius to the star's.
It does not depend on the orbital distance, the period, the mass, the inclination
(for a full transit) or any property of the planet other than its size. That is
why a transit is such a clean measurement and why it is only half of what is
needed: it gives a size in units of the star, and the star's own size is an
inference.

**(d)** Because 84 ppm is smaller than the variability of most stars on the
timescale of a transit, so the limiting noise is astrophysical rather than
instrumental. From the ground, atmospheric scintillation and the day–night cycle
also enter; from space, the detector and the pointing are better than the star.
The measurement is therefore limited by the source, not by the instrument — a
situation worth recognising, because it means that improving the instrument does
not help.

---

## ★2 — Probability and duration

**(a)** $a = 1.496\times10^{10}$ m, so

$$P = 2\pi\sqrt{\frac{a^3}{GM}}
= 2\pi\sqrt{\frac{3.348\times10^{30}}{1.327\,1244\times10^{20}}}
= 9.980\times10^5\ \mathrm{s} = 11.55\ \mathrm{days}.$$

**(b)** $p = R_*/a = 6.957\times10^8/1.496\times10^{10} = 0.0465$, i.e.
**4.65 per cent**.

**(c)** $t = \dfrac{P}{\pi}\arcsin(R_*/a)
= \dfrac{9.980\times10^5}{\pi}\arcsin(0.0465) = 1.478\times10^4$ s $= 4.10$ h.

**(d)** At small $a$ both effects push the same way, but they have different
powers: the probability grows as $1/a$ while the number of transits per unit time
grows as $1/P \propto a^{-3/2}$. So the *period* contributes more steeply at
small $a$, and the detection yield per star rises faster than the geometric
probability alone would suggest. That compounding is why the first decade of
transit surveys found hot Jupiters and why an Earth at 1 au requires a long
stare.

---

## ★3 — Radial velocity

**(a)** $P = 11.55$ days $= 9.980\times10^5$ s, so
$P/P_{1\,\mathrm{yr}} = 9.980\times10^5/3.156\times10^7 = 0.03162$ and

$$K = 0.0894 \times 5 \times (0.03162)^{-1/3}
= 0.0894\times5\times3.163 = 1.414\ \mathrm{m\,s^{-1}}.$$

**(b)** $1.414/1 = \mathbf{1.4}$, so the signal is comparable with the stellar
jitter: a real detection would need many observations and careful modelling of
the stellar activity, and this is why even a 5 Earth-mass planet at 0.1 au is
near the limit for a Sun-like star.

**(c)** It is a **minimum mass** ($m_p\sin i$). The radial velocity measures only
the line-of-sight component of the star's reflex motion, so a planet seen
pole-on ($i = 0$) produces no signal at all and the true mass is unbounded above
for a given $K$ as $i \to 0$.

**(d)** A **transit**, which requires $i \approx 90^\circ$ and therefore fixes
$\sin i \approx 1$. Combined with the transit's measurement of the orbit
inclination and the star's density, the mass becomes a mass rather than a
minimum. This is the reason that systems with both a transit and an RV are the
productive ones.

---

## ★4 — Inclination statistics

**(a)** For isotropic orientations, $\cos i$ is uniform on $[0,1]$, so the density
of $i$ on $[0,\pi/2]$ is $\sin i$ and

$$\mathrm{E}[\sin i] = \int_0^{\pi/2}\sin i\cdot\sin i\,\mathrm{d}i
= \int_0^{\pi/2}\sin^2i\,\mathrm{d}i = \frac{\pi}{4} = 0.7854 .$$

**(b)**

$$\mathrm{E}\!\left[\frac{1}{\sin i}\right]
= \int_0^{\pi/2}\sin i\cdot\frac{1}{\sin i}\,\mathrm{d}i
= \int_0^{\pi/2}\mathrm{d}i = \frac{\pi}{2} = 1.5708 .$$

**(c)** $P(\sin i < 0.3) = P(\cos i > \sqrt{1-0.09}) = 1-\sqrt{0.91}
= 1-0.9539 = 0.0461$: **4.6 per cent** of randomly oriented systems have a
minimum mass more than a factor of 3.3 below the true mass.

**(d)** $m_\mathrm{true} = m_\mathrm{min}/\sin i$, so the mean true mass is
$\mathrm{E}[1/\sin i] = \pi/2$ times the mean minimum mass:

$$\langle m_\mathrm{true}\rangle = 3\times1.5708 = 4.71\ M_\oplus .$$

The assumption is that the sample is **isotropically oriented** — which holds for
an RV-only sample and fails for a transit-selected one, whose inclinations are
near $90^\circ$ by construction. Note also that $1/\mathrm{E}[\sin i] = 1.273$
would give 3.82 instead of 4.71, a 23 per cent error, and that is Jensen's
inequality: the mean of a reciprocal is not the reciprocal of a mean.

---

## ★★5 — Running the transit and RV sections

**(a)** 83.86 ppm, 335.45 ppm, 1341.81 ppm and 10 519.79 ppm for
$R_p/R_\oplus = 1$, 2, 4 and 11.2.

**(b)** 9.3009 per cent at 0.05 au, 2.3252 per cent at 0.2 au and 0.4650 per cent
at 1 au — one in 10.8, one in 43 and one in 215.

**(c)** $K = 0.0894$ m s⁻¹ at 1 au and 0.4000 m s⁻¹ at 0.05 au. The mass
required for $K = 1$ m s⁻¹ is 11.18 $M_\oplus$ at 1 au and 2.50 $M_\oplus$ at
0.05 au.

**(d)** Because the geometric probability grows as $1/a$ and the number of
transits per unit time grows as $a^{-3/2}$, the detection yield per star rises
steeply toward small orbits, so close-in planets are over-represented in the
catalogue relative to their true abundance — the observed distribution is the
true one multiplied by the weighting, and inverting the weighting is what
occurrence-rate work does.

---

## ★★6 — Running the inclination, zone and mass–radius sections

**(a)** Monte Carlo: $\mathrm{E}[\sin i] = 0.78575$ against $\pi/4 = 0.78540$, and
$\mathrm{E}[1/\sin i] = 1.57304$ against $\pi/2 = 1.57080$. The residuals are
$4\times10^{-4}$ and $1.4\times10^{-3}$, i.e. the Monte Carlo error for two
million samples, which is the correct way to read a random-sampling check.

**(b)** 0.13359 against the analytic $1-\sqrt3/2 = 0.13397$ — agreement to
0.3 per cent.

**(c)** Naive zone: 0.870 au (freezing) and 0.466 au (boiling). With 33 K of
greenhouse warming: 1.125 au and 0.561 au. The freezing boundary moves outward by
29 per cent.

**(d)** The measured exponent is $R \propto M^{0.294}$, between the uncompressed
limit of 0.333 and the strongly compressed limit of 0.250. It is evidence that the
model is behaving sensibly for two reasons: the exponent is not fitted — it
emerges from the integration — and it lies between two independently derived
limits, so the model has moved from one regime to the other as the mass rose, as
it should.

---

## ★★7 — Error propagation

**(a)** $\delta R_p/R_p = \delta R_*/R_* = 8$ per cent.

**(b)** $\dfrac{\delta\rho}{\rho}
= \sqrt{(0.02)^2 + 9(0.08)^2} = \sqrt{0.0004+0.0576} = \sqrt{0.058}
= 0.241$, i.e. **24 per cent** — dominated entirely by the stellar radius term,
which contributes 0.240 of the 0.241.

**(c)** Setting $\delta M/M = 0.02$ and requiring
$\sqrt{(0.02)^2 + 9x^2} = 0.10$:

$$9x^2 = 0.01-0.0004 = 0.0096
\quad\Longrightarrow\quad
x = \sqrt{1.067\times10^{-3}} = 0.0327 .$$

So the stellar radius must be known to **3.3 per cent** for the density to reach
10 per cent — a demanding requirement, and a reason that precise stellar
characterisation is a planet-characterisation activity.

**(d)** The **stellar radius** and its uncertainty, or equivalently the planet's
radius and its uncertainty, because the density error is dominated by it and the
measurement that constrains it is a different observation from the one that
produced the transit. An abstract that quotes a density to two significant
figures with no stellar error has hidden its dominant systematic.

---

## ★★★8 — What the habitable zone depends on

**(a)** $T_\mathrm{eq}(1\ \mathrm{au}) = [(1-A)L/(16\pi\sigma a^2)]^{1/4}$:
271.1 K at $A = 0.1$, 254.6 K at $A = 0.3$ and 239.6 K at $A = 0.5$.

**(b)** Since $a \propto \sqrt{1-A}$ at fixed temperature, the 273 K distance is

$$a_{273}(A) = \sqrt{\frac{(1-A)L}{16\pi\sigma(273)^4}} ,$$

giving 0.986 au ($A = 0.1$), 0.870 au ($A = 0.3$) and 0.735 au ($A = 0.5$). The
range 0.735 to 0.986 au is $\pm14$ per cent about the middle value — from the
albedo alone, before any atmosphere is considered.

**(c)** With $T_\mathrm{eq} = 255$ K and 33 K of warming, the surface temperature
is 288 K at 1 au. A bare body reaching 273 K sits at
$a = \sqrt{(1-A)L/(16\pi\sigma(273)^4)} = 0.870$ au, so adding greenhouse warming
is equivalent to moving the freezing line outward by
$1.125/0.870 = 1.29$ — outward by 29 per cent. The conventional inner edge of the
habitable zone is set by where a runaway greenhouse begins, not by where the
freezing point falls, and it is computed by climate models rather than by this
arithmetic; but the exercise shows the size of the effect that makes the zone a
model output.

**(d)** The measurement that would reduce the uncertainty most is an **atmospheric
spectrum** — transmission or emission spectroscopy that detects molecular
absorption — because it is the only observation that constrains the presence and
composition of an atmosphere, and the entire habitability-zone apparatus is an
atmosphere model. It would establish whether there is an atmosphere at all, and
roughly what it is made of, which converts an assumption (the albedo and the
greenhouse) into a constraint. What it would still leave unconstrained is
everything below the atmosphere: whether there is surface liquid water, what the
surface pressure and temperature actually are, the volatile inventory and its
delivery history, the presence or absence of a magnetic field and of plate
tectonics, and the long-term stability of the climate. That list is why the
honest formulation is "consistent with" rather than "is habitable": each further
claim requires a different measurement, and some of them — the surface — are
beyond any single observation.

---

## ★★★9 — Two compositions at one mass

**(a)** With $M = 5\times5.9722\times10^{24} = 2.9861\times10^{25}$ kg:

- Silicate, $\rho = 3500$ kg m⁻³:
  $R = (3M/4\pi\rho)^{1/3} = (8.958\times10^{25}/4.398\times10^4)^{1/3}
  = (2.037\times10^{21})^{1/3} = 1.268\times10^7$ m $= 12\,680$ km.
- Ice-rich mixture, $\rho = 1556$ kg m⁻³:
  $R = (8.958\times10^{25}/1.955\times10^4)^{1/3}
  = (4.581\times10^{21})^{1/3} = 1.661\times10^7$ m $= 16\,610$ km.

**(b)** Ignoring compression makes the computed radius too **large**, because
compression raises the density and therefore shrinks the body at fixed mass. The
direction matters: an uncompressed estimate is an upper bound, and comparing it
with a measured radius biases the inferred composition toward *less* rock than is
actually present (a dense compressed rocky planet looks like a larger, lighter
one).

**(c)** The uncompressed radii differ by
$(16\,610-12\,680)/12\,680 = \mathbf{31}$ per cent. Self-compression shrinks the
silicate body to 11 287 km (the demo's value), which would widen the difference
to 47 per cent if the ice body did not compress as well — but it does, so the
truth lies between. Even so, the two compositions differ by tens of per cent in
radius at fixed mass, so a radius measured to about 5 per cent combined with a
mass to about 5 per cent is enough to separate them. That is why "bulk density"
is a useful diagnostic, and it is also the reason it is not a composition: 31 per
cent is the difference between the extremes, and a partially differentiated body
lies anywhere in between.

**(d)** A radius and a mass give a *mean* density, and a mean density is one
number: it can be produced by an iron core with a thin mantle, by a rock–iron
mixture with a thick atmosphere, by a rock body with a deep ocean, or by several
intermediate cases, and the interior models that convert one to the other are
themselves uncertain (equation of state, temperature, core fraction). An
atmospheric spectrum adds the composition and the scale height of the *outer*
layer, which is where the distinction between "rocky" and "rocky with a
substantial volatile envelope" is made. It still does not give the interior
structure, so the honest report is a *set* of interior models consistent with all
the data, with the spectrum having removed the models with the wrong atmosphere.
That is why exoplanet characterisation is described as ruling out hypotheses
rather than as measuring properties: a measurement that excludes a family of
models is a real and publishable result, and it is the result that a single
number cannot deliver.
