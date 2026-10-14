# Solutions — 02-07-04 Faraday's Law, Induction and Eddy Currents

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

---

## ★1 — Transformer EMF

**(a)** Flux $\Phi_B = \pi a^2B_0\cos\omega t$, so

$$\mathcal E = -\frac{\mathrm d\Phi_B}{\mathrm dt} = \pi a^2B_0\omega\sin\omega t .$$

**(b)** With $a = 0.05$ m, $\pi a^2 = 7.854\times10^{-3}$ m². At $f = 1$ kHz:
$\mathcal E_{\text{peak}} = 7.854\times10^{-3}\times10^{-4}\times2\pi\times10^{3}
= 4.935\times10^{-3}$ V, i.e. 4.93 mV. At 50 Hz it is 50 times smaller:
$9.87\times10^{-5}$ V, i.e. 0.099 mV. The demo's version (a 10 cm loop in 50 µT at
50 Hz) gives 0.4935 mV, larger both because the area is 4× and the field 500×.

**(c)** The EMF scales with the number of turns, $\mathcal E = N\pi a^2B_0\omega$,
for a tightly wound coil (ignoring self-capacitance and the inductive phase shift).

**(d)** The loop is fixed and the field changes, so the EMF comes from
$-\partial\mathbf B/\partial t$ alone; no material is moving relative to the field.
The motional EMF of ★2 comes from $\mathbf u\times\mathbf B$ with
$\partial\mathbf B/\partial t$ possibly zero.

---

## ★2 — Motional EMF

**(a)** $\mathcal E = vB_\perp L = 2\times5\times10^{-5}\times10 = 1.000\times10^{-3}$ V
= 1 mV.

**(b)** At 20 m/s, 10 mV. The demo reports the same linear scaling for its table of
rod lengths and speeds.

**(c)** A magnetometer reading is meant to be a measurement of the ambient field,
but the sensor's own motion through that field generates an EMF in its cables,
coils and electronics that is indistinguishable from signal unless it is either
negligible or measured. It is reduced by orienting the tow cable (or the sensor
axis) parallel to the field, by twisting signal pairs so that opposing segments
cancel, and by recording motion and correcting — which is why airborne and
shipborne magnetic data have a characteristic "heading error" to be calibrated
out.

**(d)** The motional EMF vanishes when the conductor's velocity is parallel to
$\mathbf B$ (then $\mathbf u\times\mathbf B = \mathbf 0$), or when the conductor is
oriented parallel to $\mathbf u\times\mathbf B$ so that no length of it spans the
induced field. The first condition is used deliberately in some borehole
instruments.

---

## ★3 — Diffusion

**(a)** $D = 1/(\mu_0\sigma) = \rho/\mu_0 = 100/1.2566\times10^{-6}
= 7.9577\times10^{7}$ m²/s.

**(b)** $\tau = \mu_0\sigma L^2 = (1.2566\times10^{-6})(0.01)(10^{4})^2
= 1.2566$ s.

**(c)** $z_{1/2} = 0.954\sqrt{Dt}$: at 1 s, **8508 m**; at 10 s, **26 906 m**; at
100 s, **85 085 m**. (These follow directly from the demo's verified
$z_{1/2}/\sqrt{Dt} = 0.9538$.)

**(d)** $z_{1/2}\propto t^{1/2}$. It is not a speed because the ratio $z/t$ is not
constant: it decreases with time. There is no front; the field amplitude at depth
$z$ is nonzero for every $t>0$.

---

## ★4 — Eddy currents

**(a)** Lenz's law: the induced EMF drives currents whose magnetic effect opposes
the change in flux that produced them. The energy statement: the work done against
that opposition is exactly the energy dissipated as heat in the conductor. A
positive sign would imply the induced current *enhances* the change, which would
extract energy from nothing, so the sign is fixed by conservation of energy.

**(b)** The induced currents are proportional to $\mathrm dB/\mathrm dt$, so for a
static field they vanish and the sheet is transparent to it. For a changing field
they are largest near the surface, they oppose the change, and the field is
progressively excluded — a perfect conductor in the limit $\omega\to\infty$.

**(c)** $J = \sigma E = 0.05\times2 = 0.1$ A/m²; dissipation
$J\cdot E = \sigma E^2 = 0.05\times4 = 0.2$ W/m³.

**(d)** The dissipated energy is extracted from the magnetic field, whose energy
density is $B^2/(2\mu_0)$. Hence the field amplitude must decrease with depth — the
skin effect. The observed decay length is $\delta$ and the decay is exponential, so
signal amplitude falls off by a factor of about 500 per $2\pi\delta$; that is the
whole basis of depth limitation in EM methods.

---

## ★5 — The induction equation

**(a)** Faraday: $\nabla\times\mathbf E = -\partial\mathbf B/\partial t$. Ampère
(quasi-static): $\nabla\times\mathbf H = \mathbf J$, so
$\nabla\times\mathbf B = \mu\mathbf J$. Ohm in the moving frame:
$\mathbf J = \sigma(\mathbf E + \mathbf u\times\mathbf B)$, so
$\mathbf E = \mathbf J/\sigma - \mathbf u\times\mathbf B$. Substituting into
Faraday:

$$\nabla\times\left(\frac{\mathbf J}{\sigma}\right)
- \nabla\times(\mathbf u\times\mathbf B) = -\frac{\partial\mathbf B}{\partial t}
\ \Longrightarrow\
\frac{\partial\mathbf B}{\partial t} = \nabla\times(\mathbf u\times\mathbf B)
+ \frac{1}{\mu\sigma}\nabla^2\mathbf B ,$$

using $\nabla\times\mathbf J = \nabla\times(\nabla\times\mathbf B/\mu) =
-\nabla^2\mathbf B/\mu$ (valid since $\nabla\cdot\mathbf B = 0$).

**(b)** $R_m = \mu_0\sigma uL$:

| case | $\sigma$ (S/m) | $u$ (m/s) | $L$ (m) | $R_m$ |
|---|---|---|---|---|
| laboratory, copper | $5.96\times10^{7}$ | 1 | 0.1 | 7.49 |
| crustal shear zone | 0.01 | $10^{-9}$ | $10^{4}$ | $1.26\times10^{-13}$ |
| core (nominal) | $10^{6}$ | $10^{-3}$ | $3.5\times10^{6}$ | $4.40\times10^{3}$ |

**(c)** Laboratory: $R_m = 7.5$ — advection and diffusion both matter; this is the
regime of liquid-metal dynamo experiments, which are calibrated to be just above
$R_m\sim10$. Crustal: $R_m\sim10^{-13}$ — diffusion wins by thirteen orders of
magnitude, so the field in the crust is entirely controlled by the conductivity
distribution and the external source; nothing about crustal motion appears.
Core: $R_m\sim4400$ — advection wins, field lines are carried and stretched by the
flow, and a dynamo is possible.

**(d)** A shear zone moving at $10^{-9}$ m/s (about 3 cm per year) over 10 km
produces $R_m\sim10^{-13}$: the motional term is negligible by thirteen orders of
magnitude. Every exploration EM method may therefore treat conductivity as a static
property of the ground and solve a purely diffusive, source-driven problem. Without
this numerical check the assumption would be a hope; with it, it is a fact.

---

## ★6 — Step diffusion

**(a)** Let $u = z/(2\sqrt{Dt})$. Then
$B_t = B_0\mathrm{erfc}'(u)\cdot(-z/(4\sqrt D\,t^{3/2}))$ and
$B_{zz} = B_0\mathrm{erfc}''(u)/(4Dt)$. Using
$\mathrm{erfc}'(u) = -(2/\sqrt\pi)e^{-u^2}$ gives
$\mathrm{erfc}''(u) = (4u/\sqrt\pi)e^{-u^2}$, so
$DB_{zz} = B_0(4u/\sqrt\pi)e^{-u^2}/(4t) = B_0(u/(\sqrt\pi t))e^{-u^2}$, while
$B_t = B_0(2/\sqrt\pi)e^{-u^2}\cdot z/(4\sqrt D t^{3/2})
= B_0(2/\sqrt\pi)e^{-u^2}\cdot u/(2t) = B_0(u/(\sqrt\pi t))e^{-u^2}$ ✓. Identical.

**(b)** At $z = 0$, $u = 0$ and $\operatorname{erfc}(0) = 1$, so $B = B_0$
(the imposed step). As $z\to\infty$, $u\to\infty$ and
$\operatorname{erfc}\to0$: the field has not yet reached there. The solution is
also the correct one for the initial condition $B(z,0) = 0$ for $z>0$ ✓.

**(c)** $D = 1/(\mu_0\sigma) = 7.9577\times10^{5}$ m²/s (for $\sigma = 1$ S/m), so
$u = 0.02/(2\sqrt{7.9577\times10^{5}\times4\times10^{-8}})
= 0.02/0.356\,822 = 0.056\,050$, giving
$\operatorname{erfc}(u) = 0.936\,821$. The demo's numerical scheme gives
0.936 819: a difference of $2\times10^{-6}$, which is the $O(\Delta z^2)$ truncation
error of the explicit scheme plus the influence of the far-field boundary
condition. Both numbers agree with the PDE residual check, which the demo reports as
$5.6\times10^{-7}$ relative.

**(d)** Half amplitude where $\operatorname{erfc}(u) = 0.5$, i.e.
$u = 0.476\,936$, so $z_{1/2} = 2\times0.476\,936\sqrt{Dt} = 0.953\,872\sqrt{Dt}$.
The demo's values are 0.085 082, 0.120 333 and 0.170 178 m at 10, 20 and 40 ns: the
ratios of consecutive values are $\sqrt2$ to five figures, and
$z/\sqrt{Dt}$ is 0.9538 in all three cases ✓.

---

## ★7 — Diffusion times and the age of the Earth

**(a)** $\mu_0\sigma L^2 = (1.2566\times10^{-6})(5.96\times10^{7})(1)^2 = 74.90$ s;
the fundamental mode is $\mu_0\sigma L^2/\pi^2 = 7.589$ s. A metre of copper holds
(or loses) its internal field on a timescale of seconds.

**(b)** For the core: $\mu_0\sigma R^2 = (1.2566\times10^{-6})(10^{6})
(3.48\times10^{6})^2 = 1.522\times10^{13}$ s $= 4.82\times10^{5}$ yr; the
fundamental mode is $1.542\times10^{12}$ s $= \mathbf{4.89\times10^{4}}$ yr.

**(c)** $4.89\times10^{4}/4.5\times10^{9} = 1.09\times10^{-5}$.

**(d)** Conclusion: diffusion alone cannot sustain the geomagnetic field for the age
of the Earth; it must be maintained, i.e. a dynamo must operate. Assumptions: (i)
Ohm's law with a real, uniform, scalar conductivity (ignores anisotropy, melting
and the exact iron-alloy composition); (ii) the nominal $\sigma = 10^{6}$ S/m,
whose published estimates differ by a factor of a few; (iii) that the observed
surface field is representative of the core field's magnitude history — the
palaeomagnetic record shows the field has existed for billions of years with
roughly comparable strength; (iv) a diffusion time is the right comparison with the
age of the Earth. The weakest assumption is (ii): the core conductivity is genuinely
uncertain, and it appears as a *linear* factor, so a factor of three in $\sigma$ is
a factor of three in the decay time — but three orders of magnitude of argument
mean that even this weakest assumption does not change the conclusion.

---

## ★8 — The geodynamo argument

**(a)** **Measured**: the magnetic field at and above the Earth's surface, its
spatial structure, and its time variation (secular variation) from observatories
and satellites; and remanent magnetisation in rocks, which records the field's
direction in the past. **Inferred**: that the source is inside the Earth (the field
correlates with the core's position, not with the crust), and that it is
predominantly dipolar at the surface. **Assumed**: that the core is a
well-conducting fluid in convective motion, that the induction equation applies,
and that the observed timescales (decades for secular variation) reflect core
dynamics rather than mantle or crustal diffusion — which the crustal diffusion time
of ★3b supports.

**(b)** $R_m = 4.40\times10^{3}$. It is necessary because with $R_m<1$ diffusion
would dominate over the entire core and no amount of advection could regenerate
what diffusion destroys. It is not sufficient because the flow must also have the
right topology: flows can be found that satisfy $R_m\gg1$ and still decay, and the
anti-dynamo theorems show that no axisymmetric flow sustains a dynamo at all. The
sufficiency question is a research subject.

**(c)** The decay time scales linearly with the assumed core conductivity, which
is uncertain by a factor of a few, and with the square of an assumed length scale;
"$\sim10^{4}$–$10^{5}$ years" is the range spanned by plausible choices, not a
prediction from a measurement. A sharper statement requires an independent
determination of core conductivity — from laboratory measurements of iron alloys at
core temperature and pressure, or from the observation of core waves
(magnetohydrodynamic modes) whose periods depend on it.

**(d)** Secular variation on decadal timescales (a diffusive origin would give
changes on the $10^{5}$-year timescale); the westward drift of field features; the
existence of geomagnetic reversals recorded in magnetised rocks; and the
near-axial dipole persisting through reversal. All four require an active,
evolving fluid source; none is compatible with a frozen or purely decaying field.

---

## ★9 — Frozen flux and amplification

**(a)** Setting $\eta\to0$ in the induction equation gives the frozen-flux form.
With the identity
$\nabla\times(\mathbf u\times\mathbf B) = \mathbf u(\nabla\cdot\mathbf B) -
\mathbf B(\nabla\cdot\mathbf u) + (\mathbf B\cdot\nabla)\mathbf u -
(\mathbf u\cdot\nabla)\mathbf B$ and $\nabla\cdot\mathbf B = 0$, this becomes
$\partial\mathbf B/\partial t = -\mathbf u\cdot\nabla\mathbf B +
(\mathbf B\cdot\nabla)\mathbf u - \mathbf B(\nabla\cdot\mathbf u)$, i.e.

$$\frac{\mathrm d\mathbf B}{\mathrm dt} = (\mathbf B\cdot\nabla)\mathbf u
- \mathbf B(\nabla\cdot\mathbf u) .$$

**(b)** For an incompressible flow $\nabla\cdot\mathbf u = 0$, so the only term
that changes $|\mathbf B|$ along the motion is $(\mathbf B\cdot\nabla)\mathbf u$,
which measures how the velocity varies *along* the field direction. A velocity that
increases along a field line stretches the line — the same stretching that a
stretched rubber band suggests — and by flux conservation through a material
surface the field strength must rise with the stretching.

**(c)** For a uniform stretch by factor $\alpha$ along the field in an
incompressible flow, the transverse dimensions contract by $\alpha^{-1/2}$ each,
the cross-section falls by $1/\alpha$, and flux conservation through a material
surface gives $|\mathbf B|\propto\alpha$. (Equivalently, $B/\rho$ scales as
$\alpha$.) The process cannot continue indefinitely: as $B$ grows, the current
density grows, the field lines become increasingly tangled, and eventually
opposite-polarity field regions touch and annihilate through **diffusion** —
magnetic reconnection — which is the only way to dispose of the magnetic energy.
A working dynamo needs both: advection to generate and amplify, diffusion to
reorganise and to prevent unbounded accumulation.

**(d)** Saturation is set by the back-reaction: the Lorentz force
$\mathbf J\times\mathbf B$ opposes the flow that generated the field, extracting
kinetic energy and converting it to magnetic energy and then into heat. A steady
dynamo balances the rate of magnetic-energy generation by buoyancy-driven convection
against ohmic and viscous dissipation, so the field strength is set by the
available power in the convective engine — a thermodynamic, not a kinematic,
statement. Estimating it requires the heat flow, the efficiency and the geometry,
which is why dynamo field strengths are model outputs rather than predictions.

**(e)** Exploration EM is linear (with $\sigma$ fixed, the response is
proportional to the source, so superposition holds — as it does in the whole of
this module). The dynamo is nonlinear: the field modifies the flow that makes it,
through the Lorentz force, and the equations must be solved as a coupled system.
Superposition of dynamo solutions is therefore invalid, and one cannot add two
dynamo models to get a third — a structural difference worth remembering when
reading dynamo literature.

---

## ★10 — Diffusion as a filter

**(a)** The half-space problem is linear in the boundary datum, so the response to
an arbitrary history $B_0(t)$ is the convolution of that history with the impulse
response (equivalently, its derivative the step response). The step response is
$S(z,t) = \operatorname{erfc}(z/2\sqrt{Dt})$ for $t>0$, so the field is

$$B(z,t) = \int_0^t B_0(t-\tau)\,\frac{\partial S}{\partial\tau}(z,\tau)\,
\mathrm d\tau
\qquad\text{with}\qquad
\frac{\partial S}{\partial\tau} = \frac{z}{2\sqrt{\pi D}\,\tau^{3/2}}
e^{-z^2/(4D\tau)} ,$$

a kernel depending only on $z/\sqrt D$. Diffusion is a causal, linear filter whose
memory grows with depth and with $1/\sqrt D$.

**(b)** Substituting $\tilde B = B_0e^{-(1+i)z/\delta}$ into
$\tilde B'' = i\omega\mu\sigma\tilde B$: the left side is
$\tilde B\times(1+i)^2/\delta^2 = 2i\tilde B/\delta^2$, and the right side is
$i\omega\mu\sigma\tilde B$; equality requires
$\delta^2 = 2/(\omega\mu\sigma)$ ✓. Taking the real part at frequency $\omega$ and
using $e^{-z/\delta}e^{-iz/\delta}$ gives
$B_0e^{-z/\delta}\cos(\omega t - z/\delta)$.

**(c)** At any depth the amplitude exponent is $z/\delta$ (natural logarithms) and
the phase lag is $z/\delta$ radians: the same number. Hence the complex response
has equal real and imaginary parts — a 45° phase for the half-space — and neither
amplitude nor phase alone determines the conductivity. This is the mathematical
root of the MT convention of reporting $(\rho_a,\phi)$ rather than a single
number, and of the standard practice of displaying both curves.

**(d)** A transfer function is a linear map between input and output *in the
frequency domain*; a wave has, in addition, a well-defined travel time in the time
domain because its group velocity is bounded and its impulse response has a
recognisable front. In a diffusive medium the impulse response is a
$\tau^{-3/2}$-weighted exponential with an infinitely long tail and no front, so
the natural description is entirely in the frequency domain (or as a decay curve),
and the natural inverse problem is to fit a causal, minimum-phase, complex
response rather than to pick times. That is precisely how MT data are inverted, and
why the "arrival time" language of seismology has no counterpart in EM.
