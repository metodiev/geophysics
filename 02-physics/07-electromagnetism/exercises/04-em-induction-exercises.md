# Exercises — 02-07-04 Faraday's Law, Induction and Eddy Currents

Attempt these **closed-book** before opening the
[solutions](./04-em-induction-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/em_induction_demo.py`](../code/em_induction_demo.py) require you to run
it and report its actual output. Where a conductivity must be assumed, state that
it is a nominal value.

---

## ★ Foundational

**★1.** A single-turn circular loop of radius $a = 0.05$ m lies in a uniform field
$B(t) = B_0\cos\omega t$ with $B_0 = 10^{-4}$ T.

(a) Write the flux and the induced EMF.
(b) Compute the peak EMF at $f = 1$ kHz and at $f = 50$ Hz.
(c) State what changes if the loop has 100 turns.
(d) Explain why this is called the *transformer* EMF and not the motional EMF.

---

**★2.** A 10 m long cable is towed horizontally at 2 m/s through a region where the
vertical component of the geomagnetic field is 50 000 nT.

(a) Compute the EMF developed along the cable.
(b) Compute the EMF if the cable is towed at 20 m/s (a slow aircraft).
(c) Explain why this is a *noise* source for a towed magnetometer and how it can be
reduced.
(d) State the configuration in which the motional EMF vanishes identically.

---

**★3.** Magnetic diffusion.

(a) From $\nabla^2\mathbf B = \mu\sigma\,\partial\mathbf B/\partial t$, identify the
diffusivity $D$ and compute it for $\rho = 100$ Ω·m.
(b) Compute the diffusion time $\tau = \mu_0\sigma L^2$ for $L = 10$ km.
(c) Compute the half-amplitude depth $z_{1/2} = 0.954\sqrt{Dt}$ at $t = 1$, 10 and
100 s.
(d) State the exponent relating $z_{1/2}$ to $t$ and explain why this is *not* a
speed.

---

**★4.** Eddy currents.

(a) State Lenz's law and explain it as a statement about energy rather than signs.
(b) Explain why a copper sheet strongly attenuates a *changing* magnetic field but
transmits a static one unchanged.
(c) For a conductor in which the induced electric field has amplitude
$E_0 = 2$ V/m and $\sigma = 0.05$ S/m, compute the eddy-current density and the
ohmic dissipation per unit volume.
(d) Explain why the dissipation must come out of the magnetic field energy and what
that implies for signal amplitude with depth.

---

## ★★ Applied

**★5.** The magnetic induction equation.

(a) Derive $\partial\mathbf B/\partial t = \nabla\times(\mathbf u\times\mathbf B)
+ \eta\nabla^2\mathbf B$ from Faraday's law, Ampère's law (quasi-static) and Ohm's
law in the moving frame, with $\eta = 1/(\mu\sigma)$.
(b) Define the magnetic Reynolds number and compute it for: a laboratory
experiment ($u = 1$ m/s, $L = 0.1$ m, copper); a crustal shear zone
($u = 10^{-9}$ m/s, $L = 10$ km, $\sigma = 0.01$ S/m); and the core
($u = 10^{-3}$ m/s, $L = 3.5\times10^{6}$ m, $\sigma = 10^{6}$ S/m, nominal).
(c) For each, state whether advection or diffusion wins and what that means for the
field's behaviour.
(d) Explain why the crustal case is the one that justifies the static-conductivity
assumption of every exploration method.

---

**★6.** The step-diffusion solution.

(a) Show by substitution that $B(z,t) = B_0\operatorname{erfc}
\left(z/2\sqrt{Dt}\right)$ satisfies $B_t = DB_{zz}$ for $t>0$, using
$\frac{\mathrm d}{\mathrm du}\operatorname{erfc}(u) =
-\frac{2}{\sqrt\pi}e^{-u^2}$.
(b) Verify the boundary conditions at $z = 0$ and as $z\to\infty$.
(c) Evaluate $B/B_0$ at $z = 0.02$ m for $t = 40$ ns with $\sigma = 1$ S/m in the
demo and compare with the demo's value (0.936821). Explain the small discrepancy.
(d) State the depth at which the field has fallen to half, and confirm that its
growth with time is $\sqrt t$ using the demo's three values.

---

**★7.** Diffusion times, and the age of the Earth.

(a) Compute $\mu_0\sigma L^2$ for a 1 m copper sphere
($\sigma = 5.96\times10^{7}$ S/m) and compare with the fundamental-mode estimate
$\mu_0\sigma L^2/\pi^2$.
(b) Compute both for the core with $L = R_{\text{core}} = 3.48\times10^{6}$ m and
the nominal $\sigma = 10^{6}$ S/m, and express them in years.
(c) Compute the ratio of the fundamental-mode time to the age of the Earth
(4.5 Gyr).
(d) State the conclusion and *every* assumption it rests on, and say which
assumption is the weakest.

---

**★8.** The geodynamo argument.

(a) State precisely what is measured, what is inferred, and what is assumed in the
statement "the geomagnetic field is maintained by dynamo action".
(b) Compute $R_m$ for the core with the nominal parameters of ★5b and state why
$R_m\gg1$ is necessary but not sufficient.
(c) Explain why "the field would decay in $\sim10^{4}$–$10^{5}$ years" is an
order-of-magnitude statement rather than a prediction, and what measurement would
sharpen it.
(d) Name three observable consequences of the dynamo that a purely diffusive
origin could not produce.

---

## ★★★ Research-oriented

**★9.** Frozen flux and field amplification.

(a) Show that for a perfectly conducting fluid ($\sigma\to\infty$) the induction
equation becomes $\partial\mathbf B/\partial t = \nabla\times(\mathbf u\times\mathbf B)$
and that this is equivalent to
$\frac{\mathrm d\mathbf B}{\mathrm dt} = (\mathbf B\cdot\nabla)\mathbf u -
\mathbf B(\nabla\cdot\mathbf u)$ when written in the material derivative
$\mathrm d/\mathrm dt = \partial/\partial t + \mathbf u\cdot\nabla$.
(b) Show that for an incompressible flow the field magnitude changes only through
the term $(\mathbf B\cdot\nabla)\mathbf u$, and interpret it: field lines are
stretched and thereby amplified.
(c) For a uniform stretch along the field direction by a factor $\alpha > 1$ in an
incompressible flow, compute the resulting change in $|\mathbf B|$. Explain why the
process cannot continue indefinitely, and what must interrupt it.
(d) Explain what determines the *saturation* field strength of a dynamo, and why
the answer is not simply "as strong as the flow allows" (hint: consider the
back-reaction and the energy budget).
(e) Explain why the dynamo problem is a *dynamical* problem while the forward
problem of exploration EM is a *linear* one, and what that means for the validity
of the superposition used everywhere else in this module.

---

**★10.** Diffusion as a linear filter.

(a) Show that the surface response of a half-space to an arbitrary surface field
history $B_0(t)$ is given by a convolution with a kernel depending on $z/\sqrt{D}$,
and write the kernel explicitly for the step response.
(b) Using the periodic boundary condition $B(0,t) = B_0\cos\omega t$, show that the
steady-state solution is $B_0e^{-z/\delta}\cos(\omega t - z/\delta)$ with
$\delta = \sqrt{2/(\omega\mu\sigma)}$, by substituting a complex amplitude
$\tilde B = B_0e^{-(1+i)z/\delta}$.
(c) Confirm that the amplitude decay and the phase lag are the same number at every
depth, and state why this is the mathematical reason MT measurements are reported
as amplitude *and* phase.
(d) Explain why the diffusive response is not a wave but is still a *transfer
function*, and what that implies for inverting EM data (a frequency-domain,
causal, minimum-phase structure rather than an arrival time).
