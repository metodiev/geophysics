# Exercises — 02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity

Attempt these **closed-book** before opening the
[solutions](./04-heat-conduction-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/heat_conduction_demo.py`](../code/heat_conduction_demo.py) require you
to run it and report its actual output. This is the module's mastery lesson:
**every problem below that asks for a time or a length requires you to say which
of $k$ and $\kappa$ you used, and in what unit, before you compute it.**

---

## ★ Foundational

**★1.** A rock has $k = 2.4$ W m⁻¹ K⁻¹, $\rho = 2650$ kg m⁻³ and
$c_p = 850$ J kg⁻¹ K⁻¹.

(a) Compute its thermal diffusivity, with its unit.
(b) Write the unit of $k$ and of $\kappa$ in words.
(c) State which of the two appears in $\partial T/\partial t = \kappa\nabla^2T$ and
which in $\mathbf q = -k\nabla T$, and why.
(d) A colleague reports "a thermal diffusivity of 2.4 in SI units" for this rock.
Identify the error.

---

**★2.** For the rock of ★1:

(a) Compute the diffusion time $\tau = L^2/\kappa$ for $L = 30$ m, 300 m and 3 km,
in years.
(b) Compute the 10 per cent arrival time for the same three lengths.
(c) Compute the ratio between the two conventions and state why both are used.
(d) Convert the 3 km answer into a statement about the steady state: how long does
a 3 km column take to reach its steady geotherm?

---

**★3.** A step change of 12 K in surface temperature occurs at $t = 0$ on a
half-space of the rock of ★1.

(a) Write the temperature profile $T(z,t)/\Delta T$.
(b) Evaluate it at $z = 2\sqrt{\kappa t}$ for $t = 2500$ yr and state the value of
$\mathrm{erfc}(1)$ you used.
(c) Evaluate it at $z = \sqrt{\kappa t}$.
(d) Compute the surface heat-flow perturbation at $t = 2500$ yr from
$q = k\Delta T/\sqrt{\pi\kappa t}$, in mW m⁻².

---

**★4.** State the von Neumann stability condition for the explicit
finite-difference scheme

$$T_i^{n+1} = T_i^n + r\left(T_{i-1}^n - 2T_i^n + T_{i+1}^n\right)$$

(a) Give the condition on $r = \kappa\Delta t/\Delta z^2$.
(b) For $\kappa = 1.065\times10^{-6}$ m² s⁻¹, $\Delta z = 5$ m, compute the largest
stable $\Delta t$.
(c) Compute the number of time steps needed to reach 500 years at that limit.
(d) State what happens numerically if the condition is violated, and why the
failure is not a small error.

---

## ★★ Applied

**★★5.** Run the demo, Section 2 and Section 3.

(a) Report $\kappa$ for rock, oceanic rock, water and air, and compute the ratio
of the largest to the smallest.
(b) Report $\tau$ and $t_{10}$ for $L = 100$ m and $L = 1$ km.
(c) Report the analytic and finite-difference surface fluxes at $t = 2500$ yr and
their relative difference.
(d) Explain why a 46.7 mW m⁻² perturbation is a serious problem for a heat-flow
measurement whose province mean is 65 mW m⁻².

---

**★★6.** A borehole palaeoclimate inversion is being attempted at a site where
the rock is the sandstone of lesson 02-05-01 ★2 ($k$ property given there as a
volumetric heat capacity; adopt $k = 2.6$ W m⁻¹ K⁻¹).

(a) Compute $\kappa$.
(b) A 5 K surface step occurred 200 years ago. Compute the temperature anomaly at
50 m, using the erfc solution.
(c) Compute the depth at which the anomaly is 10 per cent of 5 K.
(d) The log's temperature resolution is 0.02 K. Compute the maximum depth at which
the 200-year-old event is detectable, and state the approximation made.

---

**★★7.** Run the demo, Section 4.

(a) Report the $L_\infty$ error for $\Delta z = 40, 20, 10, 5$ m.
(b) Report the error ratios and compare with the theoretically expected factor.
(c) Explain, in one sentence, why refining $\Delta z$ refines $\Delta t$ at fixed
$r$.
(d) State what happens to the ratio column if $r$ is halved instead, and predict
the new errors before running.

---

**★★8.** A permafrost column. The ground surface is at $-5$ °C and the base of the
permafrost at 100 m is at 0 °C, in steady state with $k = 2.0$ W m⁻¹ K⁻¹. Adopt a
frozen-ground volumetric heat capacity of
$2.8\times10^6$ J m⁻³ K⁻¹ (nominal).

(a) Compute the heat flux.
(b) Compute the geothermal gradient in K km⁻¹.
(c) A warming of the surface by 3 K is imposed as a step. Compute the time for the
disturbance to reach 20 m by both conventions.
(d) State two reasons the real situation is not a step change, and two reasons the
thermal conductivity is not constant.

---

**★★9.** Advection versus conduction.

(a) Write the Péclet number.
(b) For $\kappa = 1.065\times10^{-6}$ m² s⁻¹ and $L = 500$ m, compute the velocity
at which $\mathrm{Pe} = 1$, in m yr⁻¹.
(c) A basin has groundwater moving at 1 m yr⁻¹. Compute Pe and state what controls
the temperature field.
(d) State what additional term would have to be added to equation (5) of the
lesson to describe this, and why the resulting equation is no longer a pure
diffusion equation.

---

## ★★★ Research-oriented

**★★★10.** Cooling of a magmatic intrusion.

(a) For a 200 m thick sill and a spherical body of radius 100 m, compute the
respective characteristic cooling times from $\tau_{\text{slab}} = L^2/\kappa$ and
$\tau_{\text{sphere}} = a^2/(\pi^2\kappa)$, using $\kappa = 1.065\times10^{-6}$
m² s⁻¹.
(b) State the ratio and explain the origin of the $\pi^2$.
(c) For a 5 km pluton, compute $\tau_{\text{sphere}}$ and compare it with the
duration of a typical orogenic cycle. State your source for the latter or say that
you declined to quote one.
(d) Explain why the characteristic time is a *cooling* time and not a
*crystallisation* time, and what additional physics must be added to obtain the
latter.

**★★★11.** Verification of a numerical solution. You have written a
finite-difference diffusion solver and it gives a profile that "looks right".

(a) Design a verification test using the exact solution, specifying the
initial condition, both boundary conditions, and the quantity you will measure.
(b) Explain why measuring the error in units of the step amplitude is the correct
normalisation, and what a dimensioned error would hide.
(c) State the two independent error sources (temporal and spatial truncation) and
explain why holding $r$ fixed makes the observed order a test of the temporal
discretisation alone.
(d) A student reports an error that *increases* as $\Delta z$ is refined. Give
three possible causes and say how each would be distinguished.

**★★★12.** Inversion of a borehole profile. A temperature log $T(z)$ at
$z_1, \dots, z_N$ is to be inverted for the surface temperature history $T_s(t)$.

(a) Write the forward relation as a convolution integral of $T_s$ with the
half-space impulse response, and give the impulse response.
(b) Explain why the inverse problem is non-unique, in terms of the exponential
attenuation of the skin-depth filter.
(c) State the Tikhonov-regularised objective function that would be minimised and
say what each term does.
(d) Explain why the *forward* physics of this problem is exact while the *inverse*
problem is ill-posed, and why that distinction matters for how results should be
reported.
