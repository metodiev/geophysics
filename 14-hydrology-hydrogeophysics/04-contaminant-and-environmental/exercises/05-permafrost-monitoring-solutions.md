# Solutions — 14-04-05 Permafrost Monitoring with Geophysics

> Read after attempting. Lesson:
> [05 Permafrost Monitoring with Geophysics](../05-permafrost-monitoring.md).
> All models **SYNTHETIC**.

---

## ★1 — Stefan solution and a numerical value

**Derivation.** The conducted flux to a front at depth $X$ is
$q = k\Delta T/X$, so the energy supplied per unit area in $\mathrm{d}t$ is
$k\Delta T\,\mathrm{d}t/X$. It is absorbed as latent heat
$\mathrm{d}(L_vX) = L_v\,\mathrm{d}X$, with
$L_v = \theta\rho_wL_f$. Hence

$$k\frac{\Delta T}{X}\mathrm{d}t = L_v\mathrm{d}X
\;\;\Longrightarrow\;\;
X\,\mathrm{d}X = \frac{k\Delta T}{L_v}\mathrm{d}t
\;\;\Longrightarrow\;\;
X = \sqrt{\frac{2k\Delta T t}{\theta\rho_w L_f}} .$$

**Numerical.** $t = 90\times86400 = 7.776\times10^{6}\ \mathrm{s}$;

$$L_v = 0.35\times1000\times334\times10^{3} = 1.169\times10^{8}\
\mathrm{J\,m^{-3}},$$

$$X = \sqrt{\frac{2\times1.5\times8\times7.776\times10^{6}}{1.169\times10^{8}}}
= \sqrt{\frac{1.866\times10^{8}}{1.169\times10^{8}}} = \sqrt{1.5965}
= 1.2635\ \mathrm{m} .$$

---

## ★2 — Resistivity and the unfrozen fraction

$\sigma_b = \phi^{m}S_w^{n}\sigma_w$, $\rho_w = 25\ \Omega\,\mathrm{m}$ so
$\sigma_w = 0.0400\ \mathrm{S\,m^{-1}}$, and $\phi^{m} = 0.09$.

At $S_w = 1.00$: $\sigma_b = 0.09\times1.00\times0.0400 = 0.00360\
\mathrm{S\,m^{-1}}$, $\rho_b = 277.8\ \Omega\,\mathrm{m}$.

At $S_w = 0.10$: $S_w^{n} = 0.01$, $\sigma_b = 0.09\times0.01\times0.0400
= 3.60\times10^{-5}\ \mathrm{S\,m^{-1}}$, $\rho_b = 27\,778\
\Omega\,\mathrm{m}$.

Ratio: $100$ — exactly $1/S_w^{n}$, as the algebra requires. The ratio is a
property of the saturation change alone and is independent of $\sigma_w$, which is
the result that makes a frozen/thawed *ratio* robust to salinisation.

---

## ★3 — Degree-day form

$$X = \sqrt{\frac{2k\,\mathrm{DDT}\times86400}{\theta\rho_w L_f}},
\qquad \mathrm{DDT} = \sum_i \Delta T_i\,\Delta t_i .$$

For ★1 the forcing is $\mathrm{DDT} = 8\ \mathrm{K}\times90\ \mathrm{d}
= 720\ \mathrm{K\,day}$, so

$$X = \sqrt{\frac{2\times1.5\times720\times86400}{1.169\times10^{8}}}
= \sqrt{1.5965} = 1.2635\ \mathrm{m},$$

identical to ★1. The equivalence is exact because the solution depends on
$\Delta T$ and $t$ only through their product; it holds for any sequence of
temperatures whose degree-day sum is the same, which is the method's strength
(it needs only a temperature record) and its weakness (it cannot represent a
history whose *shape* matters).

---

## ★★4 — Sensitivity to water content

$X \propto 1/\sqrt{\theta}$, so doubling $\theta$ from $0.35$ to $0.70$ multiplies
the depth by $1/\sqrt2 = 0.7071$: from $1.2635\ \mathrm{m}$ to
$0.8934\ \mathrm{m}$.

**Why this is bad news for attribution.** A measured increase in thaw depth can
be produced by a warming surface ($X \propto \sqrt{\Delta T}$), a wetter soil
($X \propto 1/\sqrt{\theta}$), or a change in thermal conductivity through a
change in lithology or saturation. A $41\%$ increase in depth is produced by
*either* doubling $\Delta T$ *or* halving $\theta$ — and the second is a
plausible consequence of the first, since a warming Arctic tends to drain as well
as thaw. The geophysical survey measures the thawed/unfrozen state; it does not
apportion the change among the three controls. Attribution requires collocated
temperature and moisture measurements, and the honest geophysical deliverable is
the *distribution* of thaw, not its cause.

---

## ★★5 — A fixed sensor

**(a)** $X_\text{max}$ at $t = 150$ days with $\Delta T = 8\ \mathrm{K}$,
$k = 1.5$, $\theta = 0.35$: scaling ★1 by $\sqrt{150/90} = 1.291$,

$$X_\text{max} = 1.2635\times1.291 = 1.631\ \mathrm{m}.$$

**(b)** Set $X(t) = 1.5\ \mathrm{m}$ and invert:

$$t = \frac{X^{2}\,\theta\rho_w L_f}{2k\Delta T}
= \frac{2.25\times1.169\times10^{8}}{2\times1.5\times8}
= \frac{2.630\times10^{8}}{24} = 1.096\times10^{7}\ \mathrm{s}
= 126.8\ \mathrm{days}.$$

Since $126.8 < 150$ days, the front does cross the sensor within the season.

**(c)** Differentiating $X = a\sqrt t$ gives
$\mathrm{d}X/\mathrm{d}t = a/(2\sqrt t) = X/(2t)$:

$$\frac{\mathrm{d}X}{\mathrm{d}t} = \frac{1.5}{2\times126.8}
= 5.91\times10^{-3}\ \mathrm{m\,day^{-1}} = 5.9\
\mathrm{mm\,day^{-1}} .$$

A weekly survey therefore resolves the crossing to about
$5.91\times10^{-3}\times7 = 4.1\ \mathrm{cm}$, i.e. $2.8\%$ of the sensor depth.
The resistivity flip at the crossing is a factor of $100$ (★2), far above any
survey noise — so the *timing* is precise while the *depth* is only as good as the
survey interval, which is the sense in which a fixed sensor is a clock rather
than a profile.

---

## ★★6 — Gassmann's ice substitution and the missing term

Gassmann predicts $K_\text{sat}$ for ice as the pore phase
($K_\text{ice} = 9.0\ \mathrm{GPa}$) and sets $\mu_\text{sat} = \mu_\text{dry}$.
For the lesson's synthetic frame ($\phi = 0.30$, $K_\text{dry} = 5.0\
\mathrm{GPa}$, $\mu_\text{dry} = 4.0\ \mathrm{GPa}$) it gives
$K_\text{sat} = 20.1577\ \mathrm{GPa}$ against $9.8800\ \mathrm{GPa}$ for water,
and the predicted water-to-ice velocity shift is $802.4\ \mathrm{m\,s^{-1}}$.

The missing term is **cementation**: ice grows between grains and bonds them,
raising the *shear* modulus, which Gassmann cannot represent because it treats
the pore phase as a fluid. The lesson's illustrative bracket raises $\mu$ by
factors of one, two and four, giving $V_p$ values of $3.4593$, $3.8041$ and
$4.4134\ \mathrm{km\,s^{-1}}$ and $V_s$ values of $1.3703$, $1.9380$ and
$2.7407\ \mathrm{km\,s^{-1}}$. The bracket is wider than the substitution effect
itself: **the cementation term dominates.**

**The constraining measurement** is $V_s$ — or equivalently the
$V_p/V_s$ ratio, or a $V_s$-derived $\mu$ — measured in frozen and thawed states
on representative samples *in the seismic frequency band*, because $V_s$ responds
to $\mu$ and is nearly independent of the pore phase's bulk modulus. A
$V_p$-only survey cannot separate ice content from frame stiffness at all.

---

## ★★★7 — Detecting unfrozen-water change under changing salinity (model answer)

**(a) What the survey separates.** In a single resistivity survey the model
$\rho_b = a/(\phi^{m}S_w^{n}\sigma_w)$ has two unknowns that multiply into the
same observable: the unfrozen fraction $S_w$ and the pore-fluid conductivity
$\sigma_w$. A conductivity change can be entirely a salinity change at constant
unfrozen content, entirely a freezing change at constant salinity, or any
mixture. What the survey *does* separate is the time-lapse **ratio** at a fixed
site when only $S_w$ changes: the frozen/thawed ratio is $1/S_w^{n}$ and is
independent of $\sigma_w$ (★2). So the survey tracks freezing *if the salinity is
stable*, and tracks neither if both change.

**(b) Breaking the ambiguity.** Three measurements, in order of cost:

1. **Time-lapse at a fixed array with a collocated pore-water sample** to monitor
   $\sigma_w$ directly. This is the only method that separates the two terms
   unambiguously, and it is a water-chemistry measurement, not a geophysical one.
2. **A second, differently weighted measurement** of the same volume — for
   example a seismic $V_s$ measurement, which responds to cementation and density
   rather than to the conducting fluid, or a GPR measurement in a dry sandy soil
   (where the permittivity contrast between ice, water and air is large and the
   salinity dependence of the permittivity is weak at radar frequencies). The
   requirement is that the second observable's sensitivity vector not be parallel
   to the resistivity one.
3. **A repeating ratio measurement in a salinity-stable interval** of the same
   site, used as a control to bound the salinity drift before it is extrapolated
   to the interval of interest.

**(c) Repeatability requirement.** Differentiate
$\rho_b \propto S_w^{-n}$: $\partial\ln\rho_b/\partial S_w = -n/S_w$. For a target
resolution $\delta S_w = 0.02$ (two points of unfrozen fraction) at
$S_w = 0.20$ with $n = 2$:

$$\frac{\delta\rho_b}{\rho_b} = \frac{n\,\delta S_w}{S_w}
= \frac{2\times0.02}{0.20} = 0.20 .$$

**A $20\%$ repeatability suffices at $S_w = 0.20$** — easy. But at
$S_w = 0.80$ the same absolute resolution requires
$2\times0.02/0.80 = 5\%$, and at $S_w = 0.95$ it requires $4.2\%$. The
requirement is therefore a strong function of where on the curve the
measurement sits, and it is *most demanding in the warm, wet state* where the
permittivity and velocity contrasts are also weakest. A programme designed for
the frozen end of the range will quietly fail in the thawed state unless the
repeatability requirement is derived at the state of interest, as here.

---

## ★★★8 — Limits of the Stefan solution

**(a) Two effects that limit it in a coarse, permeable substrate.**

1. **Advective heat transport by groundwater.** Moving water carries heat far
   more efficiently than conduction, so the front penetrates deeper than Stefan
   predicts and the active layer is thicker. The error is *large and in one
   direction* — Stefan under-predicts the thaw depth — and it is not a correction
   that can be fitted by adjusting $k$, because the transport is a different
   mechanism with a different scaling (advective fronts move linearly in time,
   not as $\sqrt t$).
2. **A non-step surface temperature with snow cover.** Snow insulates with a
   conductivity an order of magnitude below the soil's, so the effective
   $\Delta T$ at the ground surface is much smaller than the air-temperature
   difference, and the timing of snowmelt sets a real starting date for the thaw
   season. Stefan over-predicts the depth if it uses air temperature directly,
   and the error is largest in the early season when $X$ is most sensitive.

**(b) The conductivity contrast.** Frozen water is a crystalline solid with
$k \approx 2.2\ \mathrm{W\,m^{-1}\,K^{-1}}$, while liquid water has
$k \approx 0.6\ \mathrm{W\,m^{-1}\,K^{-1}}$; a water-saturated soil therefore has
a higher thermal conductivity when frozen (often roughly a factor of two, with
the exact ratio depending on porosity and mineralogy). As the season progresses
the conducting path of the *thawed* zone above the front grows, so the series
conductance of the system falls and the front decelerates faster than
$\sqrt t$ — that is, the true $X(t)$ lies below the Stefan curve late in the
season even without advection. Empirically, the effective $k$ in the Stefan
formula must be chosen for the state you are modelling.

**(c) A field measurement that detects the failure without a temperature model.**
The **shape of the $X(t)$ curve**: Stefan predicts $X \propto \sqrt t$ exactly,
which is a straight line on a plot of $X^{2}$ against $t$. Repeated
thaw-depth measurements (a sensor array at several depths, or a repeated GPR or
resistivity transect) plotted as $X^{2}$ against $t$ will show a straight line if
Stefan holds and a concave-down curvature if a second mechanism is draining heat
efficiently — advection or a changing $k$. The test costs no temperature data and
is the cleanest available diagnostic, because it tests the *scaling* rather than
the constant.
