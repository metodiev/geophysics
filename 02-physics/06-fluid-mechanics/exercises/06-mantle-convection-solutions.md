# Solutions — 02-06-06 Mantle Convection and Rayleigh-Benard Instability

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output. Every physical input below is a nominal value
> with a stated range; the Rayleigh numbers computed from them are therefore
> nominal too, and are reported to the precision of the arithmetic, not of the
> Earth.

---

## ★1 — Rayleigh numbers

$Ra = \rho g\alpha\Delta T d^3/(\kappa\eta)$ in SI units throughout.

**(a) Mantle.** Numerator
$= 3300\times9.81\times3\times10^{-5}\times2500\times(2.891\times10^6)^3
= 5.8666\times10^{22}$; denominator $= 10^{-6}\times10^{21} = 10^{15}$;
$Ra = \mathbf{5.87\times10^{7}}$.

**(b) Water tank.** Numerator
$= 1000\times9.81\times2\times10^{-4}\times20\times1^3 = 39.24$; denominator
$= 1.4\times10^{-7}\times10^{-3} = 1.4\times10^{-10}$;
$Ra = \mathbf{2.80\times10^{11}}$.

**(c) Magma chamber.** Numerator
$= 2500\times9.81\times3\times10^{-5}\times100\times(10^3)^3 = 7.3575\times
10^{10}$; denominator $= 10^{-6}\times10^{3} = 10^{-3}$;
$Ra = \mathbf{7.36\times10^{13}}$.

**(d)** Supercriticality $Ra/Ra_c$: mantle $8.9\times10^{4}$; water tank
$4.3\times10^{8}$; magma chamber $1.1\times10^{11}$. The **magma chamber** is the
most supercritical, and by a wide margin. This is the answer that surprises:
the mantle is the *least* supercritical of the three, because although it is
enormous it is also extremely viscous. Laboratory tanks and magma chambers
convect far more violently relative to their thresholds, which is why
laboratory convection is a good test of planform and of $Nu$–$Ra$ scaling, and a
poor analogue of the mantle's dynamical regime.

---

## ★2 — Marginal stability with stress-free boundaries

**(a)** Stress-free boundaries have no tangential stress, which for
incompressible flow requires $W = \mathrm{d}^2W/\mathrm{d}z^2 = 0$ at $z = 0,1$.
With $W = \sin(n\pi z)$: $W(0) = W(1) = 0$, and
$\mathrm{d}^2W/\mathrm{d}z^2 = -n^2\pi^2\sin(n\pi z)$, which also vanishes at
both ends. Both conditions are satisfied for every integer $n$.

**(b)** Substituting $W = \sin(n\pi z)$ into
$(\mathrm{d}^2/\mathrm{d}z^2 - a^2)^3W = -Ra\,a^2W$ replaces each derivative by
its eigenvalue: $\mathrm{d}^2/\mathrm{d}z^2 \to -n^2\pi^2$, so

$$\left(-n^2\pi^2 - a^2\right)^3 W = -Ra\,a^2W
\;\Longrightarrow\; Ra = \frac{(n^2\pi^2+a^2)^3}{a^2}.$$

**(c)** For $n = 1$, write $f(a) = (\pi^2+a^2)^3/a^2$. Then

$$f'(a) = \frac{3(\pi^2+a^2)^2\cdot2a\cdot a^2 - (\pi^2+a^2)^3\cdot2a}{a^4}
= \frac{2(\pi^2+a^2)^2}{a^3}\left[3a^2 - (\pi^2+a^2)\right],$$

which vanishes when $3a^2 = \pi^2+a^2$, i.e. $a_c^2 = \pi^2/2$, so
$a_c = \pi/\sqrt2 \approx 2.2214$.

**(d)** $Ra_c = (3\pi^2/2)^3/(\pi^2/2) = 27\pi^4/4 = \mathbf{657.5114}$.

---

## ★3 — Aspect ratio

**(a)** $\lambda_c/d = 2\pi/a_c = 2\pi\sqrt2/\pi = 2\sqrt2 = \mathbf{2.828}$.

**(b)** At onset the cells are wider than they are deep, by a factor of about
2.8. Rolls or the equivalent hexagonal planforms are predicted, with a
wavelength set by the balance between the horizontal diffusion that limits the
cell width and the vertical convection that drives it.

**(c)** With $a_c \approx 3.117$ for rigid boundaries,
$\lambda_c/d = 2\pi/3.117 = \mathbf{2.016}$: about 2, i.e. cells almost square in
cross-section. Rigid boundaries pin the flow and allow narrower cells.

**(d)** The critical Rayleigh number answers a **yes/no** question — does the layer
convect? — and its value is a threshold. The aspect ratio is a **quantitative**
prediction of the linear theory at onset, and it can be measured directly in a
laboratory tank, which is why it is one of the classic confirmations of the
theory.

---

## ★4 — Boundary layers

**(a)** $Ra^{1/3} = (5.8666\times10^7)^{1/3} = 388.6$, so
$\delta = 2.891\times10^6/388.6 = \mathbf{7.44\times10^{3}\ m} = 7.4$ km.

**(b)** $Ra_\delta = Ra\,(\delta/d)^3 = Ra\cdot Ra^{-1} = \mathbf{1.000}$. The
definition was constructed to make it so: the local Rayleigh number of a layer of
thickness $d\,Ra^{-1/3}$ is exactly 1. This is an identity, and it carries no
independent physical information.

**(c)** $\delta_c = d(Ra_c/Ra)^{1/3} = 7.44\ \mathrm{km}\times(657.51)^{1/3} =
7.44\times8.70 = \mathbf{64.7\ km}$. It is larger by $Ra_c^{1/3} = 8.70$
because it is defined by a *different* physical requirement: that the layer be
locally marginal ($Ra_\delta = Ra_c$) rather than locally unit-Rayleigh.

**(d)** For comparison with a seismic estimate of lithospheric thickness, the
marginal-stability definition ($\delta_c \approx 65$ km) is the appropriate one,
because the lithosphere is the layer that is *just stable* against convection,
and the seismic lithosphere is defined by where the material is strong enough not
to creep on geological timescales. The $Ra^{-1/3}$ definition gives a much thinner
layer and corresponds instead to the temperature scale over which a conductive
profile would be perturbed. **State the definition**; the two answers differ by
a factor of nearly 9, and both are defensible.

---

## ★★5 — The mantle's Prandtl number

**(a)** $\nu = 10^{21}/3300 = \mathbf{3.03\times10^{17}\ m^2\,s^{-1}}$.

**(b)** $Pr = 3.03\times10^{17}/10^{-6} = \mathbf{3.03\times10^{23}}$.

**(c)** $t_\nu = d^2/\nu = 8.36\times10^{12}/3.03\times10^{17} = 2.76\times
10^{-5}$ s. $t_\kappa = d^2/\kappa = 8.36\times10^{12}/10^{-6} = 8.36\times
10^{18}$ s $= 2.65\times10^{11}$ yr.

**(d)** The Stokes approximation is safe because momentum diffuses across the
whole mantle in microseconds: no part of the flow can retain the memory of a
previous acceleration, so inertia never accumulates and the momentum equation
reduces to a local balance. The same fact implies there is no cascade: with
$Re \sim 10^{-20}$ the nonlinear advection term is utterly negligible, so the
mantle is a *laminar, time-dependent* flow. Chaos there is chaotic advection by a
laminar flow, not turbulence, and applying a Kolmogorov-scale or eddy-diffusivity
model to it is a category error.

---

## ★★6 — Reading the demo

**(a)** Numerator $5.866627\times10^{22}$; denominator $1.000000\times10^{15}$;
$Ra = 5.866627\times10^{7}$; $\log_{10}Ra = 7.7684$.

**(b)** Ternary-search minimum: $a_c = 2.221441$, $Ra_c = 657.511364$; analytic
$\pi/\sqrt2 = 2.221441$ and $27\pi^4/4 = 657.511364$. The agreement to six digits
demonstrates that the analytic minimum in ★2(c) is correctly located and
evaluated: the identity between the two routes is a check on the algebra, and its
exactness is expected because both compute the same closed-form function.

**(c)** Free-slip: $N = 20$ gives $Ra_c \approx 654.813$ (error $-2.698$);
$N = 40$ gives $656.836$ (error $-0.676$); $N = 80$ gives $657.342$ (error
$-0.169$). The error falls by roughly a factor of four for each doubling of $N$,
i.e. as $h^2$: second-order convergence for a sixth-order operator.

**(d)** Rigid: $N = 40$ gives $Ra_c \approx 1699.441$; $N = 60$ gives
$1704.046$. Both approach the classical value 1707.76, with $a_c \approx 3.116$
against the classical 3.117. The residual is the discretisation error.

**(e)** $Ra_\delta = 1.000000$. It is exactly 1 by construction, because
$\delta = d\,Ra^{-1/3}$ was chosen precisely so that the local Rayleigh number
($\propto \delta^3$) equals 1. The demo prints it to make the reader notice that
it is an identity; the meaningful version imposes the physical requirement
$Ra_\delta = Ra_c$ and gives $\delta_c = 64.7$ km.

---

## ★★7 — Nusselt number and heat flow

**(a)** $Nu = 0.1\,Ra^{1/3} = 0.1\times388.6 = \mathbf{38.9}$.

**(b)** $q = Nu\,k\Delta T/d = 38.9\times2.5\times2500/2.891\times10^6
= \mathbf{84\ mW\,m^{-2}}$.

**(c)** The handbook's nominal values are about 65 mW m⁻² for continental and
100 mW m⁻² for oceanic surface heat flow. The estimate is between them, i.e.
correct to within tens of per cent.

**(d)** The **exponent $1/3$** follows from the boundary-layer scaling and is a
scaling law; the **coefficient 0.1** is an empirical fit to laboratory and
numerical data and is not derived from the equations. Consequently, (b) is only
credible to the extent that the coefficient is appropriate for the geometry,
rheology and heating mode of the Earth's mantle — which it is not, since the fit
was obtained for constant-viscosity, bottom-heated convection. The honest
statement is that the *scaling* predicts a heat flow of the observed order,
while the precise value depends on physics (variable viscosity, internal heating)
that the simple model omits.

---

## ★★8 — Viscosity sensitivity

**(a)**

| $\eta$ (Pa s) | $Ra$ | $\delta = d Ra^{-1/3}$ (km) | $Nu = 0.1Ra^{1/3}$ | $u = (\kappa/d)Ra^{2/3}$ (cm yr⁻¹) |
|---|---|---|---|---|
| $10^{19}$ | $5.87\times10^{9}$ | 1.60 | 180.4 | 3551 |
| $10^{20}$ | $5.87\times10^{8}$ | 3.45 | 83.7 | 765 |
| $10^{21}$ | $5.87\times10^{7}$ | 7.44 | 38.9 | 164.8 |
| $10^{22}$ | $5.87\times10^{6}$ | 16.03 | 18.0 | 35.5 |

**(b)** $Ra \propto \eta^{-1}$; $\delta \propto \eta^{1/3}$;
$Nu \propto \eta^{-1/3}$; $u \propto \eta^{-2/3}$.

**(c)** The four values of $u$ are 3551, 765, 165 and 35.5 cm yr⁻¹, against
observed plate speeds of order 1–10 cm yr⁻¹.

**(d)** The **largest viscosity, $10^{22}$ Pa s, gives the best agreement** (a
factor of 3.5–35 too fast, against a factor of 16–350 for $10^{21}$ and worse for
lower viscosities). Taken at face value this suggests that the effective
viscosity governing plate-scale flow is nearer $10^{22}$ than $10^{21}$ Pa s —
but the inference must be stated cautiously: the scaling itself ignores the
lithosphere, internal heating and the temperature dependence of $\eta$, any of
which can shift the velocity by a factor of several independent of $\eta$. What
the exercise legitimately demonstrates is that a factor of ten in the viscosity
moves the predicted plate speed by a factor of $10^{2/3} \approx 4.6$, so a
velocity comparison constrains the viscosity only to within roughly a factor of
three.

---

## ★★★9 — The Rayleigh number as a ratio of timescales

**(a)** Take the diffusion time across the layer,
$\tau_{\text{diffusion}} = d^2/\kappa$, and the time for a buoyant parcel to
traverse the layer against viscous resistance. In a Stokes flow the velocity
scale from a balance of buoyancy against viscous stress is
$u \sim \rho g\alpha\Delta T\,d^2/\eta$, so the traversal time is
$\tau_{\text{buoyancy}} = d/u = \eta/(\rho g\alpha\Delta T\,d)$. Then

$$\frac{\tau_{\text{diffusion}}}{\tau_{\text{buoyancy}}} =
\frac{d^2}{\kappa}\cdot\frac{\rho g\alpha\Delta T\,d}{\eta} =
\frac{\rho g\alpha\Delta T\,d^3}{\kappa\eta} = Ra.$$

**(b)** $\tau_{\text{diffusion}} = 8.358\times10^{18}$ s
$= 2.65\times10^{11}$ yr. $\tau_{\text{buoyancy}} = 1.4246\times10^{11}$ s
$= 4515$ yr. Ratio $= 5.867\times10^{7}$, exactly the answer to ★1(a).

**(c)** $Ra_c \approx 657.5$ (free-slip) means that convection begins only when
the buoyancy timescale is $\tau_{\text{diffusion}}/Ra_c \approx 1/1000$ of the
diffusion timescale. Physically: for $Ra < Ra_c$ the parcel loses its
temperature anomaly to diffusion before it can traverse the layer and buoyancy is
neutralised. Convection requires the parcel to overtake diffusion by a factor of
about a thousand — a strongly stabilising, *cubed* geometry effect, which is why
$Ra_c$ is of order $10^3$ rather than of order 1.

**(d)** For a 1 m layer of the same material,
$Ra = 3300\times9.81\times3\times10^{-5}\times2500\times1/(10^{-6}\times10^{21})
= 2.4\times10^{-12}$, twelve orders of magnitude below the threshold. The layer
would **never** convect: the buoyancy timescale would exceed the diffusion
timescale by a factor of $4\times10^{11}$. This is why mantle convection is a
property of the *thickness* of the mantle and not of the rock: the same material
in a 1 m layer is a rigid solid for this purpose. It also explains why convection
in a thin layer such as the oceanic lithosphere requires a completely different
mechanism (small-scale convection beneath the plate, driven by the
temperature-dependent viscosity).

---

## ★★★10 — Temperature-dependent viscosity

**(a)** With $\eta(T) = \eta_0\exp[E_a/(R_gT)]$ and $\eta(1800) = 10^{21}$,

$$\frac{\eta(1500)}{\eta(2500)} = \exp\left[\frac{E_a}{R_g}\left(\frac{1}{1500}
-\frac{1}{2500}\right)\right] = \exp\left[\frac{3\times10^5}{8.314}\times
1.0667\times10^{-4}\right] \approx \mathbf{1.5\times10^{4}}.$$

(Explicitly: $\eta(1500) \approx 5.5\times10^{22}$ Pa s,
$\eta(2500) \approx 3.7\times10^{18}$ Pa s.)

**(b)** A viscosity varying by four orders of magnitude across a layer makes the
cold upper boundary rigid and the interior fluid. The result is a **stagnant lid**
or a highly asymmetric planform: narrow, fast downwellings where cold material is
advected into the interior, and broad, slow upwellings. The symmetric
Rayleigh–Bénard cells are destroyed by the simple fact that one half of the layer
is a thousand times stiffer than the other.

**(c)** Because the viscosity appearing in $Ra$ is now a function of the
temperature field, which is itself unknown: $Ra$ ceases to be a parameter external
to the problem and becomes a diagnostic of the solution. The controlling
quantities become (i) the **viscosity contrast** across the layer,
$\eta(T_{\text{cold}})/\eta(T_{\text{hot}})$, and (ii) the temperature dependence
of the viscosity through the Arrhenius parameters — together with the Rayleigh
number defined at a reference (usually interior) viscosity. Two models with the
same reference $Ra$ but different viscosity contrasts have entirely different
dynamics.

**(d)** Two observations that a constant-viscosity model cannot reproduce:
(i) the existence of **rigid, long-lived lithospheric plates** with narrow
boundaries — constant-viscosity convection produces broad, symmetric cells and a
freely deforming surface, not plates; and (ii) the **asymmetric thermal
structure** of the mantle inferred from tomography, with narrow, cold
downwellings (subducted slabs) and broad, hot upwellings, which is the signature
of a strongly temperature-dependent viscosity. A third, if wanted, is the
existence of a **low-viscosity asthenosphere**, which requires a mechanism that
reduces viscosity locally, not a uniform value.
