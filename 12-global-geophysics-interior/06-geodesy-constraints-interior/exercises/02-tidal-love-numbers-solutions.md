# Solutions — 12-06-02 Love Numbers and Theoretical Tides

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. Where a problem admits more than one defensible answer, that is said.

Lesson: [02 Love Numbers and Theoretical Tides](../02-tidal-love-numbers.md).

---

## ★1 — Induced potential of a displaced surface

$$
V_{2}(R) = -\frac{4\pi G\rho u R}{5}
= -\frac{4\pi\,(6.67430\times10^{-11})(3000)(1.0)(1.0\times10^{6})}{5}
= -5.032304\times10^{-1}\ \mathrm{J\,kg^{-1}} .
$$

The sign is negative: adding mass at the poles (where $P_{2} = 1$) lowers the
potential there, exactly as adding mass anywhere does. The number is the *degree-2
coefficient* at the surface, i.e. the value multiplying
$P_{2}(\cos\theta)$ in J/kg. Divided by $g u$ with
$g = \tfrac43\pi G\rho R = 0.8387\ \mathrm{m\,s^{-2}}$:

$$
\frac{|V_{2}(R)|}{g u} = \frac{0.5032304}{0.8387\times1.0} = 0.600000 = \frac{3}{5},
$$

which is the geometry-only identity $k_{2} = \tfrac35 h_{2}$.

---

## ★2 — Fluid limit and the observable factors

Equipotential condition on the deformed surface:

$$
V_{0} + gu - \tfrac35 gu = 0
\Longrightarrow u = \frac{5}{2}\frac{V_{0}}{g},
\qquad h_{2} = \frac{5}{2},
$$

$$
k_{2} = \frac{|V_{2}(R)|}{V_{0}} = \frac{\tfrac35 g u}{V_{0}}
= \frac{3}{5}\times\frac{5}{2} = \frac{3}{2},
\qquad h_{2} = 1 + k_{2} = 2.5 .
$$

Observables:

| body | $h_{2}$ | $k_{2}$ | $\delta = 1+h_{2}-\tfrac32 k_{2}$ | $\tau = 1+k_{2}-h_{2}$ |
|---|---|---|---|---|
| fluid | 2.5 | 1.5 | $1 + 2.5 - 2.25 = 1.25$ | $1+1.5-2.5 = 0$ |
| rigid | 0 | 0 | $1$ | $1$ |

A fluid body's surface *is* an equipotential, so there is no tilt relative to the
equilibrium tide: $\tau = 0$. A rigid body follows the geometry of the forcing
exactly in the sense that nothing moves: $\delta = \tau = 1$.

---

## ★3 — A moderately rigid body

$$
h_{2} = \frac{2.5}{1 + 9.5(0.5)} = \frac{2.5}{5.75} = 0.43478,
\qquad
k_{2} = 0.6\times0.43478 = 0.26087,
$$

$$
\frac{k_{2}}{h_{2}} = 0.6000,\qquad
\delta = 1 + 0.43478 - 1.5(0.26087) = 1.04348,
\qquad
\tau = 1 + 0.26087 - 0.43478 = 0.82609 .
$$

Compared with the endpoints ($\delta_{\text{fluid}} = 1.25$,
$\delta_{\text{rigid}} = 1$), the body is closer to rigid in $\delta$ but its
tilt factor is only 17% below the rigid value. A single number decides: **the
combination $\hat\mu = \mu/(\rho g R) = 0.5$**; every observable here is a
function of that one number, which is why none of them can separately constrain
$\mu$, $\rho$ or $R$.

---

## ★4 — Inverting a gravity-tide factor

With $k_{2} = 0.6h_{2}$,

$$
\delta = 1 + h_{2} - 1.5(0.6h_{2}) = 1 + 0.1h_{2}
\;\Longrightarrow\;
h_{2} = 10(\delta - 1) = 10(0.13) = 1.30 .
$$

$$
\hat\mu = \frac{1}{9.5}\left(\frac{2.5}{1.30} - 1\right)
= \frac{1.92308 - 1}{9.5} = \frac{0.92308}{9.5} = 0.097166 .
$$

$$
\mu = \hat\mu\,\rho g R = 0.097166\times3500\times10\times6.0\times10^{6}
= 2.04\times10^{10}\ \mathrm{Pa} .
$$

That is a fairly compliant body ($\sim2\times10^{10}$ Pa is well below a rocky
mantle's elastic modulus), consistent with the measured $\delta$ being well above
1. Note the fragility: $\mu\propto\rho g R$, so an error in the assumed density
or gravity passes straight through.

---

## ★5 — Maxwell body in the transition band

$$
\omega = \frac{2\pi}{10^{9}\times3600} = 1.7453\times10^{-12}\ \mathrm{s^{-1}},
\qquad
\omega\tau_{M} = 1.6493\times10^{-1} .
$$

$$
\mu(\omega) = \mu\frac{i\omega\tau_{M}}{1+i\omega\tau_{M}}
= 0.5\,\frac{i(0.16493)}{1+i(0.16493)} .
$$

$$
\frac{i x}{1+ix} = \frac{ix(1-ix)}{1+x^{2}} = \frac{x^{2} + ix}{1+x^{2}}
= \frac{0.027202 + i\,0.16493}{1.027202} = 0.026481 + i\,0.160563 .
$$

So $\mu(\omega) = 0.5(0.026481 + i\,0.160563) = 0.013241 + i\,0.080282$, and

$$
h_{2} = \frac{2.5}{1 + 9.5\mu(\omega)} = \frac{2.5}{1 + 0.12579 + i\,0.76268}
= \frac{2.5}{1.12579 + i\,0.76268}.
$$

$$
|h_{2}| = \frac{2.5}{\sqrt{1.12579^{2} + 0.76268^{2}}}
= \frac{2.5}{\sqrt{1.26740 + 0.58168}} = \frac{2.5}{1.36055} = 1.8385,
$$

matching the demonstration's $|h_{2}| = 1.8385$ and $|k_{2}| = 1.1031$. The phase
of $k_{2}$ is $-\arctan(0.76268/1.12579) = -34.12^{\circ}$, again matching. **The
body is in the relaxation band**: it is neither elastic nor fluid, its response is
a factor 4 above the elastic value, and the response lags the forcing by a third
of a radian.

---

## ★6 — Amplification, analytically

With $\hat\mu = (2.5/h_{2} - 1)/9.5$,

$$
\frac{\mathrm{d}\hat\mu}{\mathrm{d}h_{2}} = -\frac{2.5}{9.5\,h_{2}^{2}},
\qquad
\frac{\mathrm{d}\ln\hat\mu}{\mathrm{d}\ln h_{2}}
= \frac{h_{2}}{\hat\mu}\frac{\mathrm{d}\hat\mu}{\mathrm{d}h_{2}}
= -\frac{2.5}{9.5\,h_{2}\,\hat\mu} .
$$

At $h_{2} = 0.6$, $\hat\mu = 0.33333$:

$$
\left|\frac{\mathrm{d}\ln\hat\mu}{\mathrm{d}\ln h_{2}}\right|
= \frac{2.5}{9.5\times0.6\times0.33333} = \frac{2.5}{1.90000} = 1.3158 .
$$

The demonstration measures $1.316$ — agreement to four digits, which is a check on
both the algebra and the finite-difference step. Note that the amplification
*decreases* with $h_{2}$ (the denominator carries $h_{2}\hat\mu$), so a compliant
body's rigidity is better determined than a stiff body's from the same Love
number.

---

## ★7 — A two-band programme (specification)

**Observables.** The complex Love number at two well-separated tidal periods: one
diurnal ($\sim1$ day) and one long-period (a fortnight or longer). Each band
gives an amplitude and a phase: four numbers in total, of which the two phases
are the anelastic signal.

**Precision.** The phase lag is proportional to $1/Q$; to determine $Q$ to 20%
the phases must be measured to a few degrees. The amplitudes must be good to a
few percent to fix the elastic part against which the phases are referenced.

**What remains ambiguous.** Two complex numbers are four real numbers; a
single-Maxwell-time model has three parameters ($\mu$, $\tau_{M}$, and the
density structure). So one parameter is left over — realistically the elastic
rigidity, which must be taken from an assumed density and rheology. A real body
has a *spectrum* of Maxwell times, so even with four numbers the relaxation
spectrum is not determined; determining it requires a third band, and even then
the answer is an effective spectrum unless a mechanism is assumed.

**The honest conclusion.** A two-band programme measures *dissipation at two
frequencies*, and converts them to an effective relaxation model. That is a
legitimate result; it is not a profile.

---

## ★8 — The ratio, and what 0.40 would mean

Re-derivation with the assumptions made explicit:

1. The body is **homogeneous** near the surface, so the displaced mass forms a
   degree-2 shell of areal density $\sigma_{2} = \rho u$ where $u$ is the *same*
   amplitude that appears in $h_{2}$.
2. Self-gravity is described by the **spherically symmetric** part, so
   $g = GM/R^{2}$.
3. The response is **linear** in the deformation.

Then the shell potential at the shell is $V_{2}(R) = -\tfrac{4\pi G\rho uR}{5}$
and, using $g = \tfrac43\pi G\rho R$,

$$
k_{2} = \frac{|V_{2}(R)|}{V_{0}}\cdot\frac{V_{0}}{V_{0}}
= \frac{\tfrac{3}{5}gu}{V_{0}} = \frac{3}{5}h_{2} .
$$

**If a measurement gave $k_{2}/h_{2} = 0.40$**, then either (i) the body is not
homogeneous — a denser or lighter layer at the surface changes the effective
$\rho$ in the shell mass that moves — or (ii) the measurement is contaminated by
an ocean or atmosphere (whose surface is its own equipotential and whose
deformation is not the solid-body one), or (iii) there is an error. What the
ratio alone does **not** do is determine a profile: one number cannot invert for a
radial function, and the same ratio can be produced by many stratified structures.
It tells you *that* the body is stratified; locating the stratification requires
the mass, radius, inertia and figure together.
