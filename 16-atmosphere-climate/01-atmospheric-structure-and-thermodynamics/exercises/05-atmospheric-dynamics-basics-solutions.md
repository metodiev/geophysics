# Solutions — 16-01-05 Atmospheric Dynamics: Coriolis, Geostrophic and Thermal Wind

> **Read after attempting.** Numbers were computed, not estimated by hand. All
> models are **SYNTHETIC** teaching values. Lesson:
> [05 Atmospheric Dynamics](../05-atmospheric-dynamics-basics.md).

---

## ★1 — The Coriolis parameter and its timescales

$$f = 2\Omega\sin\phi, \qquad \Omega = 7.2921150\times10^{-5}\ \mathrm{rad\,s^{-1}}.$$

| $\phi$ | $\sin\phi$ | $f$ (s⁻¹) | $1/f$ (h) | $2\pi/f$ (h) |
|---|---|---|---|---|
| 20° | 0.342020 | $4.9881\times10^{-5}$ | 5.569 | 34.99 |
| 45° | 0.707107 | $1.0313\times10^{-4}$ | 2.694 | 16.924 |
| 60° | 0.866025 | $1.2630\times10^{-4}$ | 2.199 | 13.819 |

**One sentence.** $1/f$ is the time in which the Coriolis acceleration turns a wind
by of order one radian (the *adjustment* time), while $2\pi/f$ is the period of a
complete inertial circle (the *oscillation* period); they differ by the factor
$2\pi$ and must not be used interchangeably.

---

## ★2 — Geostrophic wind

Pressure **rising** to the north means $\partial p/\partial y = +2\ \mathrm{hPa}$
per $200\ \mathrm{km}$ (with $y$ northward):

$$\frac{\partial p}{\partial y} = \frac{200\ \mathrm{Pa}}{2\times10^{5}\ \mathrm{m}}
= +1.0\times10^{-3}\ \mathrm{Pa\,m^{-1}},$$

$$u_g = -\frac{1}{\rho f}\frac{\partial p}{\partial y}
= -\frac{1.0\times10^{-3}}{1.2\times1.0313\times10^{-4}}
= -\frac{1.0\times10^{-3}}{1.23756\times10^{-4}} = -8.081\ \mathrm{m\,s^{-1}}.$$

**$u_g$ is negative: the wind is an *easterly*** (blowing toward the west, i.e.
from the east). This is the correct sense — with pressure rising northward the
geostrophic wind has low pressure on its left, and the low pressure lies to the
south.

*Check on the sign convention.* If pressure had *fallen* to the north, the same
magnitude would be a westerly. The pair is worth doing once with numbers to fix the
convention permanently.

---

## ★3 — Rossby number

$$\mathrm{Ro} = \frac{U}{fL} = \frac{15}{f\times8\times10^{5}}.$$

| $\phi$ | $f$ (s⁻¹) | $\mathrm{Ro}$ | verdict |
|---|---|---|---|
| 45° | $1.0313\times10^{-4}$ | 0.1818 | quasi-geostrophic; adequate to about 20% |
| 15° | $3.7747\times10^{-5}$ | 0.4967 | marginal; the acceleration is half the Coriolis term |

So **the same flow is geostrophic at $45^\circ$ and not at $15^\circ$.** That is the
practical reason tropical meteorology is a separate subject: the balance that
organises mid-latitude weather is absent near the equator.

---

## ★4 — Thermal-wind shear in the tropics

$$\frac{\partial u_g}{\partial z}
= -\frac{g}{fT}\frac{\partial T}{\partial y}
= -\frac{9.80665}{7.2921\times10^{-5}\times290}(+2\times10^{-5})
= -9.2747\times10^{-3}\ \mathrm{s^{-1}}
= -9.27\ \mathrm{m\,s^{-1}\,km^{-1}}.$$

The westerly **decreases** with height (a negative shear), so the wind at altitude
is more easterly than at the surface.

**Why the tropics differ.** In the tropics temperature *increases* toward the pole
up to the tropopause and then decreases, so the sign of $\partial T/\partial y$
reverses with height; and $f$ is small, which both weakens the balance and
magnifies the shear implied by any given gradient. The mid-latitude sign — cold
toward the pole, so westerly increasing with height — is a property of the
mid-latitude baroclinic zone, not a universal rule.

---

## ★5 — Scale analysis, and the gradient wind

**Scale analysis.** With $U$ a wind scale and $L$ a length scale:

acceleration $\sim U^2/L$; Coriolis $\sim fU$;

$$\frac{\text{acceleration}}{\text{Coriolis}} \sim \frac{U^2/L}{fU} = \frac{U}{fL}
= \mathrm{Ro}.$$

For $\mathrm{Ro} \ll 1$ the acceleration is negligible against both the Coriolis
term and the pressure gradient, and the balance is
$\mathbf{u}_g = (1/\rho f)\mathbf{k}\times\nabla_h p$ with a relative error
$O(\mathrm{Ro})$.

**Gradient wind.** For a circular vortex the radial momentum balance adds the
centrifugal term:

$$\frac{u^2}{R} + fu = fu_g .$$

This is a quadratic in $u$; taking the physical root,

$$u = \frac{-fR + \sqrt{f^2R^2 + 4fRu_g}}{2} .$$

*Numbers:* $u_g = 10\ \mathrm{m\,s^{-1}}$, $\phi = 45^\circ$
($f = 1.0313\times10^{-4}$), $\mathrm{Ro} = 0.2$ gives
$R = u_g/(f\,\mathrm{Ro}) = 4.848\times10^{5}\ \mathrm{m} = 484.8\ \mathrm{km}$.
Then $fR = 50.0\ \mathrm{m\,s^{-1}}$,
$\sqrt{f^2R^2 + 4fRu_g} = \sqrt{2500 + 2000} = 67.08$, and

$$u = \frac{-50 + 67.08}{2} = 8.541\ \mathrm{m\,s^{-1}} .$$

**The exact wind is $8.54\ \mathrm{m\,s^{-1}}$, i.e. $14.6\%$ sub-geostrophic**, and
$0.146/0.2 = 0.73$ of $\mathrm{Ro}$. Tight cyclones have slower winds than
geostrophy would give; the centrifugal term takes up part of the pressure-gradient
force.

---

## ★6 — Thermal-wind derivation and the identity

**Pressure coordinates.** $u_g = -(1/f)\partial\Phi/\partial y$. Then

$$\frac{\partial u_g}{\partial p}
= -\frac{1}{f}\frac{\partial}{\partial y}\!\left(\frac{\partial\Phi}{\partial p}\right).$$

*Assumption 1: hydrostatic balance*, $\partial\Phi/\partial p = -1/\rho$. Hence

$$\frac{\partial u_g}{\partial p}
= \frac{1}{f}\frac{\partial}{\partial y}\!\left(\frac{1}{\rho}\right).$$

*Assumption 2: ideal gas*, $1/\rho = R_dT/p$, so

$$\boxed{\frac{\partial u_g}{\partial p} = \frac{R_d}{fp}\frac{\partial T}{\partial y}.}$$

**Height coordinates.** *Assumption 3: hydrostatic balance to substitute
$\partial p/\partial z = -pg/(R_dT)$:*

$$\frac{\partial u_g}{\partial z}
= \frac{\partial u_g}{\partial p}\frac{\partial p}{\partial z}
= \frac{R_d}{fp}\frac{\partial T}{\partial y}\left(-\frac{pg}{R_dT}\right)
= -\frac{g}{fT}\frac{\partial T}{\partial y}. \qquad\checkmark$$

*Assumption 4* for both forms: $f$ constant (f-plane), so $f$ can be moved through
$\partial/\partial y$.

**The identity.** With $\mathrm{d}\ln p = \mathrm{d}p/p$ and the ideal-gas
hydrostatic relation,

$$(g/T)\,\mathrm{d}z = \frac{g}{T}\cdot\left(-\frac{R_dT}{g}\mathrm{d}\ln p\right)
= -R_d\,\mathrm{d}\ln p .$$

**Implication.** Any integral of the thermal-wind shear over height collapses onto
$-R_d\ln p$ times the temperature gradient. So integrating the thermal wind and
comparing with the difference of two geostrophic winds tests *arithmetic
bookkeeping*, not physics: both sides are built from the same two balances. A
genuine test must use an independently measured shear or an independent constraint
(see ★10).

---

## ★7 — The inertial oscillation

$$\frac{\mathrm{d}u}{\mathrm{d}t} = fv, \qquad \frac{\mathrm{d}v}{\mathrm{d}t} = -fu
\;\Longrightarrow\; \ddot u = -f^2u,
\qquad T = \frac{2\pi}{f}.$$

At $45^\circ$, $f = 1.0313\times10^{-4}\ \mathrm{s^{-1}}$:

$$T = 6.0927\times10^{4}\ \mathrm{s} = 16.924\ \mathrm{h}.$$

The hodograph radius is $U/f = 10/1.0313\times10^{-4} = 9.697\times10^{4}\ \mathrm{m}
= 96.97\ \mathrm{km}$, and the distance travelled in one period is
$U T = 10\times6.0927\times10^{4} = 609.3\ \mathrm{km}$.

**Why constant speed and a circle.** The Coriolis acceleration $\mathbf{a} = -f
\mathbf{k}\times\mathbf{u}$ is perpendicular to $\mathbf{u}$, so
$\mathbf{u}\cdot\mathbf{a} = 0$ and
$\frac{\mathrm{d}}{\mathrm{d}t}(\tfrac{1}{2}|\mathbf{u}|^2) = 0$: the speed cannot
change. The trajectory is therefore a circle rather than a spiral — an ellipse or
spiral would require a component of force along the motion, and there is none. In a
spiral the *wind vector* would rotate while shrinking; here only its direction
changes.

---

## ★8 — Inferring a temperature gradient from a jet

Mean shear over the layer:

$$\frac{\partial u_g}{\partial z} \approx
\frac{45-10}{7.71\times10^{3}} = 4.542\times10^{-3}\ \mathrm{s^{-1}}.$$

Inverting $\partial u_g/\partial z = -(g/(fT))\partial T/\partial y$ at
$45^\circ$ with $T = 265\ \mathrm{K}$:

$$\frac{\partial T}{\partial y}
= -\frac{fT}{g}\frac{\partial u_g}{\partial z}
= -\frac{1.0313\times10^{-4}\times265}{9.80665}\times4.542\times10^{-3}
= -1.2656\times10^{-5}\ \mathrm{K\,m^{-1}}
= -1.27\ \mathrm{K\ per\ 100\ km}.$$

**Sign: temperature falls northward**, as it must in the mid-latitude baroclinic
zone for the westerly to strengthen with height.

**Dominant assumptions.** (i) That the two winds really are geostrophic; along a
jet core the flow is strongly ageostrophic and the curvature correction of ★5
applies. (ii) That the layer-mean $T$ ($265\ \mathrm{K}$) represents the layer in
the coefficient $g/(fT)$; a $5\ \mathrm{K}$ error in $T$ is a $1.9\%$ error in the
inferred gradient, so this assumption is minor compared with (i). A third
assumption, implicitly made, is that the shear is entirely baroclinic and not partly
due to curvature or to a change in $\partial T/\partial y$ within the layer.

---

## ★9 — Specification for an observational test of geostrophic balance

1. **Wind measurement.** Use a wind *profilers/radiosonde* network (or a Doppler
   lidar/radar) rather than an assimilation product, because assimilated winds are
   already constrained to be close to geostrophic and would make the test
   circular. This is the crucial design decision.
2. **Pressure/geopotential field.** An independent analysis, constructed from
   pressure and temperature observations, with its own stated error.
3. **Metric.** Two numbers, both reported: (i) the root-mean-square *vector*
   difference $|\mathbf{u}_{obs} - \mathbf{u}_g|$ normalised by the rms
   $|\mathbf{u}_g|$; and (ii) the mean angle between the observed and geostrophic
   winds, since a small vector error can hide a large rotation. A sign convention
   is needed for (ii).
4. **Expected departures.** In the *free troposphere* at $\mathrm{Ro} \ll 1$ the
   balance should hold to $O(\mathrm{Ro})$ — of order $10\%$ and $10^\circ$–$20^\circ$
   for a well-resolved synoptic flow. In the *boundary layer* the frictional,
   ageostrophic flow crosses the isobars toward low pressure by $20$–$30^\circ$
   and is systematically weaker, so a boundary-layer test should fail and its
   failure is a *confirmation* of the physics.
5. **Confounders.** (a) Mismatch of scales: geostrophic balance is a statement
   about a *length scale*, so comparing a point wind with a pressure gradient
   smoothed over a different scale manufactures an error. (b) Instrumental and
   representativeness error, which is largest exactly where the gradients are
   sharpest. Both must be quantified or the test measures the data processing.
6. **Falsification.** If the normalised rms vector difference, in a well-resolved
   flow with $\mathrm{Ro} \le 0.1$, came out above (say) the theoretical $O(
   \mathrm{Ro})$ by a large factor *after* the confounders were budgeted, the
   approximation would be in question for that regime — the honest conclusion would
   be a statement about that regime, not a blanket rejection.

---

## ★10 — A genuinely independent test of the thermal wind

The consistency check differentiates an analysed geopotential, so it inherits the
balance assumptions. Three routes that do not:

**(a) Measured shear plus measured temperature gradient.** Measure
$\partial u/\partial z$ with a wind profiler (independent of any pressure analysis)
and $\partial T/\partial y$ with a radiosonde network (independent of any wind
measurement). The test is whether the *measured* shear equals
$-(g/(fT))\,\partial T/\partial y$ within the two error bars. This is a real test:
neither quantity is derived from the other, and a systematic disagreement would
indicate either non-geostrophic flow or a failure of hydrostatic/ideal-gas
reasoning.

**(b) Mass continuity.** For a flow in geostrophic balance the horizontal
divergence vanishes at leading order, $\nabla_h\cdot\mathbf{u}_g = 0$ (a direct
consequence of the stream-function form of the geostrophic wind). A measured wind
field with non-zero horizontal divergence therefore requires ageostrophic motion —
and that is not a test of the thermal wind directly, but it *bounds* the
ageostrophic part and hence how much slack the thermal wind has.

**(c) Independent buoyancy constraint.** The thermal wind's time evolution is tied
to the temperature tendency by the thermodynamic equation. Measuring both the
shear *change* and the *temperature change* over the same interval, with the
advection computed from independent winds, tests the closed set of relations rather
than any single one.

**What the independent test can detect that the consistency check cannot.** The
consistency check would pass even if geostrophic balance were violated in the real
atmosphere, because both sides are computed *assuming* it. Route (a) would fail: it
compares two independently measured quantities, so it can detect a real
non-geostrophic balance. That is the difference between verifying code and testing
physics.

---

## ★11 — Specification for the inertial-period numerical experiment

**Pipeline.** Integrate $\dot u = fv$, $\dot v = -fu$ with classical fourth-order
Runge–Kutta at fixed steps $\Delta t \in \{1, 2, 5, 10, 20, 50\}\ \mathrm{s}$,
starting from $(u,v) = (7,0)\ \mathrm{m\,s^{-1}}$, for exactly four periods at each
latitude; estimate the period from upward zero crossings of $u$; compare with
$2\pi/f$.

**Predicted scaling.** For a fourth-order scheme the local truncation error per
step is $O(\Delta t^5)$ and the global error per *period*, over $N =
T/\Delta t$ steps, is $O(\Delta t^4)$. So

$$\frac{\Delta T_{\text{measured}} - 2\pi/f}{2\pi/f} = C\,(\Delta t)^4 .$$

On a log–log plot of the fractional period error against $\Delta t$, the slope
should be $4.0$. With $\Delta t = 1\ \mathrm{s}$ at $45^\circ$ the demonstration
found a fractional error of $+1.9\times10^{-6}$; the prediction is then $1.9\%
$ at $\Delta t = 10\ \mathrm{s}$ and $O(10^{3})\%$ at $50\ \mathrm{s}$. The second
of those is nonsense, which is itself the useful information: **the $(\Delta t)^4$
law must break down** once the global error reaches a few per cent, at which point
the period estimator's own discretisation error (locating a zero crossing to within
one step) takes over. Reporting the break-down point is part of the experiment.

**Latitude dependence.** The *absolute* period changes with latitude through
$1/f$, but the *fractional* error should not depend on latitude at all in this
scaling: the equations are linear with a single coefficient $f$, and a rescaling of
time removes $f$ entirely. **That is the sharp prediction.** The dimensionless
error is a function of $\Delta t\,f$ alone, so plotting
$(\Delta T/T)$ against $f\,\Delta t$ should collapse all latitudes onto one curve.
A failure of the collapse would mean the integration is not capturing the dynamics
(e.g. a step-size or index bug), and finding that is much more useful than
confirming that a fourth-order scheme is fourth order.

**What the experiment is for.** The measured quantity is a pure numerical artefact:
the atmosphere's inertial period is $2\pi/f$ exactly. So the experiment is *not* a
test of the physics — it is a test of the integrator and of the period estimator,
and it belongs in the same category as the RK4 and hypsometric checks in
[02 §8](../02-hydrostatic-balance.md). Stating that plainly is the point: a
verification exercise must not be dressed up as a discovery.
