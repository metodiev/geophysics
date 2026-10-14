# Solutions — 02-05-04 Heat Conduction, Fourier's Law and Thermal Diffusivity

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Every answer below names the constant it used. If you used $k$ anywhere a $\kappa$
was required, or vice versa, the error is a factor of $(\rho c_p)$ or its square
root — about 1500 or 39 for crustal rock.

---

## ★1 — The two constants

**(a)** $\kappa = k/(\rho c_p) = 2.4/(2650\times850) = 2.4/2.2525\times10^6
= 1.0655\times10^{-6}$ m² s⁻¹.

**(b)** $k$: **watts per metre per kelvin** (W m⁻¹ K⁻¹), the flux carried per unit
gradient. $\kappa$: **square metres per second** (m² s⁻¹), the rate at which a
temperature disturbance spreads.

**(c)** $\kappa$ appears in the evolution equation, because the equation balances
the *rate of change of stored energy* ($\rho c_p\partial T/\partial t$) against a
divergence of flux, and the $\rho c_p$ cancels into $\kappa$. $k$ appears in the
constitutive relation, because it is what converts a gradient into a flux.

**(d)** A thermal diffusivity of 2.4 m² s⁻¹ is about $2.3\times10^6$ times too
large; 2.4 is the value of $k$, not $\kappa$. The two are confused because both are
"thermal" something with plausible rock values, and the only reliable
discriminator is the unit.

---

## ★2 — Diffusion times

**(a)** $\tau = L^2/\kappa$ with $\kappa = 1.0655\times10^{-6}$ m² s⁻¹:
$L = 30$ m → $9\times10^2/1.0655\times10^{-6} = 8.447\times10^8$ s
$= 26.77$ yr. $L = 300$ m → $2.677\times10^3$ yr. $L = 3$ km →
$2.677\times10^5$ yr.

**(b)** $t_{10} = L^2/(4x^2\kappa)$ with $x = 0.906\,1938$
(so $4x^2 = 3.2847$): 8.15 yr, 814.9 yr, $8.149\times10^4$ yr.

**(c)** The ratio is $1/3.2847 = 0.3044$; the characteristic time is 3.28 times
the 10 per cent time. Both are used because they answer different questions: the
characteristic time is the timescale over which the profile is *rearranged*, while
the 10 per cent time is when a change becomes *locally detectable*. Quoting one
without naming it is the error.

**(d)** 2.7 × 10⁵ yr. A 3 km column needs a quarter of a million years to reach
its steady geotherm, so any thermal event younger than that requires a transient
model no matter how well the boundary conditions are known.

---

## ★3 — The step change

**(a)** $T(z,t)/\Delta T = \mathrm{erfc}\!\left(z/(2\sqrt{\kappa t})\right)$.

**(b)** $2\sqrt{\kappa t} = 2\sqrt{1.0655\times10^{-6}\times7.8894\times10^{10}}
= 2\sqrt{8.406\times10^4} = 579.86$ m. At $z = 579.86$ m the argument is 1, so
$T/\Delta T = \mathrm{erfc}(1) = 0.157\,299$.

**(c)** At $z = \sqrt{\kappa t} = 289.93$ m the argument is $1/2$, so
$T/\Delta T = \mathrm{erfc}(0.5) = 0.479\,500$.

**(d)** $q = k\Delta T/\sqrt{\pi\kappa t}
= 2.4\times12/\sqrt{\pi\times1.0655\times10^{-6}\times7.8894\times10^{10}}
= 28.8/514.9 = 5.60\times10^{-2}$ W m⁻² $= 56.0$ mW m⁻².

---

## ★4 — Stability of the explicit scheme

**(a)** $r = \kappa\Delta t/\Delta z^2 \le 1/2$.

**(b)** $\Delta t_{\max} = 0.5\Delta z^2/\kappa
= 0.5\times25/1.0655\times10^{-6} = 1.1732\times10^7$ s $= 135.8$ days.

**(c)** $500\times3.155\,76\times10^7/1.1732\times10^7 = 1345$ steps.

**(d)** The solution oscillates with growing amplitude and diverges to
$\pm\infty$ within a few dozen steps. The failure is not a small error because the
scheme is *unconditionally unstable* above the limit — the amplification factor
for the highest resolved wavenumber exceeds 1, and error grows geometrically.
Halving $\Delta t$ fixes it; refining $\Delta z$ while holding $\Delta t$ makes it
worse.

---

## ★★5 — Reading the demo

**(a)** Rock $1.157\,407\times10^{-6}$, oceanic $7.757\,576\times10^{-7}$, water
$1.433\,349\times10^{-7}$, air $2.111\,890\times10^{-5}$ m² s⁻¹. Ratio of largest
to smallest (air to water) $= 1.47\times10^2$.

**(b)** $L = 100$ m: $\tau = 273.8$ yr, $t_{10} = 83.4$ yr. $L = 1$ km:
$\tau = 27\,378.5$ yr, $t_{10} = 8335.0$ yr.

**(c)** Analytic 0.046 677 W m⁻²; finite difference 0.046 674 W m⁻²; relative
difference $5.8\times10^{-5}$.

**(d)** Because 46.7 mW m⁻² is **72 per cent** of a 65 mW m⁻² province mean. A
heat-flow value quoted without a palaeoclimate correction can therefore be wrong
by more than the signal being mapped, which is why the correction is a
requirement rather than an option.

---

## ★★6 — A palaeoclimate log

**(a)** With $\rho c_p = 2.512\times10^6$ J m⁻³ K⁻¹ (lesson 02-05-01 ★2(b)) and
$k = 2.6$ W m⁻¹ K⁻¹: $\kappa = 2.6/2.512\times10^6 = 1.0350\times10^{-6}$ m² s⁻¹.

**(b)** $t = 200$ yr $= 6.3115\times10^9$ s, so
$2\sqrt{\kappa t} = 2\sqrt{1.0350\times10^{-6}\times6.3115\times10^9}
= 2\sqrt{6532.6} = 161.65$ m. At $z = 50$ m, $\eta = 0.3093$ and
$\mathrm{erfc}(0.3093) = 0.6618$, so the anomaly is
$5\times0.6618 = 3.31$ K.

**(c)** The 10 per cent depth is $\eta = 0.9062$, i.e.
$z = 0.9062\times161.65 = 146.5$ m.

**(d)** 0.02 K against 5 K is a fraction $4\times10^{-3}$, so solve
$\mathrm{erfc}(\eta) = 0.004$: $\eta = 2.0352$, giving
$z = 2.0352\times161.65 = 329.0$ m. The approximation is that the surface change
was a step in time and uniform in space; a real 200-year surface history is a
ramp, is spatially variable, and is overprinted by later changes.

---

## ★★7 — Reading the demo's convergence table

**(a)** $4.3946\times10^{-3}$, $1.1212\times10^{-3}$, $2.7988\times10^{-4}$,
$7.0127\times10^{-5}$ (all in units of $\Delta T$).

**(b)** 3.92, 4.01, 3.99 — all close to the expected factor of 4 for a scheme whose
error is second-order in the grid spacing when $r$ is held fixed.

**(c)** Because holding $r = \kappa\Delta t/\Delta z^2$ fixed forces
$\Delta t \propto \Delta z^2$, so a finer grid automatically takes finer time steps
and the temporal truncation error falls with the same power.

**(d)** Halving $r$ halves $\Delta t$ at fixed $\Delta z$, so the error falls by
about a factor of 2 at every grid level while the ratios between successive
refinements stay near 4 — the errors scale as $O(\Delta t)$ but the *convergence
rate in $\Delta z$* is unchanged, because $r$ is still fixed from level to level.
Verify by running: the absolute errors should roughly halve.

---

## ★★8 — Permafrost

**(a)** $q = k\Delta T/L = 2.0\times5/100 = 0.1$ W m⁻² $= 100$ mW m⁻².

**(b)** The gradient is $5/100 = 0.05$ K m⁻¹ $= 50$ K km⁻¹ — a high value, and
that is the point: a cold surface with a thick frozen column requires a large
gradient to carry the Earth's heat out through a low-conductivity medium.

**(c)** $\kappa = k/(\rho c_p) = 2.0/2.8\times10^6 = 7.143\times10^{-7}$ m² s⁻¹.
$\tau = 400/7.143\times10^{-7} = 5.60\times10^8$ s $= 17.7$ yr; the 10 per cent
time is $0.3044\times17.7 = 5.40$ yr.

**(d)** Not a step change, because (i) atmospheric warming is a trend rather than
a step, and (ii) the surface temperature has an annual cycle of several kelvin
superimposed. Not constant-conductivity, because (i) the thermal conductivity of
frozen soil depends strongly on ice content and therefore on temperature, and
(ii) the ice–water phase change absorbs latent heat, adding an effective heat
capacity that is enormous inside the transition interval.

---

## ★★9 — Advection versus conduction

**(a)** $\mathrm{Pe} = vL/\kappa$.

**(b)** $v = \kappa/L = 1.0655\times10^{-6}/500 = 2.13\times10^{-9}$ m s⁻¹
$= 0.0672$ m yr⁻¹ $= 6.7$ cm yr⁻¹.

**(c)** $\mathrm{Pe} = (1/3.155\,76\times10^7)\times500/1.0655\times10^{-6}
= 1.585\times10^{-8}\times500/1.0655\times10^{-6} = \mathbf{14.9}$. Advection
dominates: the temperature field is controlled by the fluid flow, and a conductive
geotherm fitted to a well in such a basin is wrong.

**(d)** An advection term,
$\rho c_p\left(\partial T/\partial t + \mathbf v\cdot\nabla T\right)
= \nabla\cdot(k\nabla T) + A$. The equation is no longer a pure diffusion equation
because it is no longer *parabolic in the same sense*: information now travels
with the flow as well as spreading, the solution depends on the upstream
direction, and boundary conditions are required only at the inflow. Steady
advection–diffusion problems with $\mathrm{Pe} \gg 1$ also need upwinding or
artificial diffusion in a numerical scheme, precisely because the centred
discretisation of §4 is no longer stable.

---

## ★★★10 — Cooling of intrusive bodies

**(a)** Sill of thickness $L = 200$ m:
$\tau = 4\times10^4/1.065\times10^{-6} = 3.756\times10^{10}$ s $= 1190$ yr.
Sphere of radius $a = 100$ m:
$\tau = a^2/(\pi^2\kappa) = 10^4/(9.8696\times1.065\times10^{-6})
= 9.513\times10^8$ s $= 30.1$ yr.

**(b)** Ratio $= 39.5$. The $\pi^2$ comes from the eigenvalue of the lowest
spatial mode of the Laplacian in a sphere with a fixed surface temperature: the
eigenfunctions are $\sin(kr)/r$ with $k = \pi/a$, so the decay rate is
$\kappa k^2 = \pi^2\kappa/a^2$. A slab's lowest mode has $k = \pi/L$ as well, but
the relevant comparison here uses the slab *thickness* against the sphere
*radius*, i.e. a factor of 2 in the length, which gives $2^2\pi^2 = 39.5$.

**(c)** With $a = 2500$ m: $\tau = 6.25\times10^6/(9.8696\times1.065\times10^{-6})
= 5.946\times10^{11}$ s $= 1.884\times10^4$ yr. For the duration of an orogenic
cycle, **declined to quote a value**: the range in the literature is broad and
this repository has not verified a specific figure, so the comparison must be made
by the reader against a source they have checked. What can be said without a
number is that $1.9\times10^4$ yr is *much shorter* than the tectonic timescales
usually associated with orogeny, so a pluton's conductive cooling is a
geologically brief event and must be treated as a thermal pulse on top of a
tectonic history.

**(d)** The characteristic time is the time for the *temperature* profile to relax
to the ambient, which is set by the geometry, $\kappa$ and the boundary condition.
The *crystallisation* time is set in addition by the latent heat (which lengthens
the time spent near the solidus by the plateau factor of lesson 02-05-01 §3.3),
by the crystallisation interval, and by the fact that as the outer shell solidifies
its low conductivity insulates the interior. It also depends on whether the body is
losing heat purely by conduction or is being cooled by circulating hydrothermal
fluid, which is faster and is not described by the diffusion equation at all.

---

## ★★★11 — Verification of a numerical solution

**(a)** Domain $0 \le z \le L_{\max}$ with $L_{\max}$ several times the diffusion
length; initial condition $T(z,0) = 0$; boundary conditions $T(0,t) = \Delta T$
and $T(L_{\max},t) = 0$ with $L_{\max}$ large enough that the second condition is
exact to machine precision. Measure the $L_\infty$ norm of the difference from
$\Delta T\,\mathrm{erfc}(z/2\sqrt{\kappa t})$ over the grid at a fixed final time,
and separately measure the error in the surface flux
$k(T_0 - T_1)/\Delta z$ against $k\Delta T/\sqrt{\pi\kappa t}$.

**(b)** Dividing by $\Delta T$ makes the error a *fraction of the signal*, which
is the quantity that matters: an absolute error of $10^{-4}$ K is excellent when
$\Delta T = 10$ K and useless when $\Delta T = 10^{-3}$ K. A dimensioned error also
hides the fact that the truncation error scales with the amplitude of the solution,
so two runs with different $\Delta T$ would appear to disagree when they do not.

**(c)** Spatial truncation (the second-derivative operator is $O(\Delta z^2)$) and
temporal truncation (the forward Euler step is $O(\Delta t)$). Holding
$r = \kappa\Delta t/\Delta z^2$ fixed makes $\Delta t = r\Delta z^2/\kappa$, so
$O(\Delta t) = O(\Delta z^2)$: the two error sources then have the same scaling and
the observed ratio of 4 per halving of $\Delta z$ tests the combined scheme. To
isolate the temporal error, vary $\Delta t$ at fixed $\Delta z$.

**(d)** Three candidates. (i) The domain is too short, so the far-field condition
$T(L_{\max}) = 0$ is not satisfied and the error is dominated by a boundary
artefact — distinguish by doubling $L_{\max}$ and seeing whether the error falls.
(ii) The time integration is being terminated at a non-integer number of steps or
with a mismatched $t$, so the comparison is at the wrong time — distinguish by
printing the actual elapsed time. (iii) The spatial difference operator is
inconsistent at the boundaries (a one-sided or first-order stencil), so refining
$\Delta z$ refines the interior while the boundary error grows in relative
importance — distinguish by computing the error only on the interior nodes.

---

## ★★★12 — Inverting a borehole profile

**(a)** For a surface temperature history $\Delta T_s(t')$ relative to the initial
state, the temperature anomaly at depth $z$ and time $t$ is

$$T(z,t) - T_\infty(z) = \int_0^t \Delta T_s(t')\,\frac{\partial}{\partial t}
\mathrm{erfc}\!\left(\frac{z}{2\sqrt{\kappa(t-t')}}\right)\mathrm{d}t'
= \int_0^t \Delta T_s(t')\,G(z,t-t')\,\mathrm{d}t' ,$$

with the impulse response

$$G(z,\tau) = \frac{z}{2\sqrt{\pi\kappa\tau^3}}\exp\!\left(-\frac{z^2}{4\kappa\tau}\right) .$$

**(b)** Because $G$ is exponentially small in $z^2/\kappa\tau$, the deep
measurements are almost insensitive to recent history and the shallow ones are
almost insensitive to the distant past; the kernel's singular values decay
geometrically, so many different histories reproduce the same profile to within
the measurement noise. The exponential attenuation demonstrated in lesson §3.5 is
exactly the statement that the forward operator is rank-deficient in practice.

**(c)** $\Phi(\Delta T_s) = \|\mathbf d - \mathbf G\,\Delta T_s\|_2^2
+ \lambda\|\mathbf L\,\Delta T_s\|_2^2$: the first term measures the misfit to the
data and the second penalises roughness (or magnitude, if $\mathbf L = \mathbf I$)
of the recovered history; $\lambda$ sets the trade-off and is chosen so that the
misfit is commensurate with the noise level.

**(d)** The forward problem is a well-posed integral of a known kernel against a
known $\kappa$; it has a unique, stable answer and requires no regularisation. The
inverse problem asks for the history given finite, noisy, band-limited data, and
is ill-posed because the kernel is smoothing: fine structure in $T_s$ is
invisible at depth. The distinction matters because a forward model can be
reported with its assumptions, whereas an inverse result is one of many consistent
histories and must be reported with the regularisation, the noise model, and a
resolution or uncertainty estimate. Reporting an inverted borehole history as
"the" temperature history is the error this exercise is designed to prevent.
