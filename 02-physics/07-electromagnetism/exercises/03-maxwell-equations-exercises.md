# Exercises — 02-07-03 Maxwell's Equations and Their Physical Meaning

Attempt these **closed-book** before opening the
[solutions](./03-maxwell-equations-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/maxwell_demo.py`](../code/maxwell_demo.py) require you to run it and
report its actual output. State the time convention ($e^{+i\omega t}$ or
$e^{-i\omega t}$) in every answer that involves complex amplitudes.

---

## ★ Foundational

**★1.** Write all four Maxwell equations in differential and integral form, and
give the physical meaning of each in one sentence. Then state, for each of the
four, the version that survives in the static limit and the name of that version.

---

**★2.** Derive the continuity equation $\nabla\cdot\mathbf J +
\partial\rho/\partial t = 0$ from Ampère–Maxwell's law and Gauss's law.

(a) Show that without the displacement current the same manipulation forces
$\nabla\cdot\mathbf J = 0$.
(b) Explain why that is unacceptable, with a specific physical example.
(c) A parallel-plate capacitor with plates of area $0.01$ m² separated by 1 mm is
charged by a current of 1 mA. Compute the displacement current between the plates
and show that it equals the conduction current.

---

**★3.** Derive the electromagnetic wave equation in a charge-free, non-conducting
medium.

(a) Show $\nabla^2\mathbf E = \mu\varepsilon\,\partial^2\mathbf E/\partial t^2$,
stating each identity you use.
(b) Compute the speed for $\varepsilon_r = 6$, $\mu = \mu_0$, and express it as a
fraction of $c$.
(c) Compute the wavelength at 100 MHz in that medium.
(d) State what the numerical agreement of $1/\sqrt{\mu_0\varepsilon_0}$ with the
measured speed of light establishes about the nature of light.

---

**★4.** Derive the diffusion equation in a conductor.

(a) Show $\nabla^2\mathbf E = \mu\sigma\,\partial\mathbf E/\partial t$, stating
exactly which term was dropped from Ampère's law and why.
(b) Identify the diffusivity $D$ and compute it for $\rho = 100$ Ω·m.
(c) Using $z_{1/2}\approx0.954\sqrt{Dt}$ for a step applied at the surface, compute
the half-amplitude depth at $t = 1$, 10 and 100 s.
(d) Explain why the phrase "the EM pulse arrives at depth $z$ at time $t$" is
meaningless in this regime, and give the correct statement.

---

## ★★ Applied

**★5.** Evaluate the ratio $\sigma/(\omega\varepsilon)$ and decide the regime.

(a) For $\rho = 1000$ Ω·m, $\varepsilon_r = 6$, compute $\sigma/(\omega\varepsilon)$
at $f = 10^{-3}$, 1, $10^{6}$ and $10^{8}$ Hz.
(b) Compute the crossover frequency $f_c = \sigma/(2\pi\varepsilon)$ for the same
medium and explain why the answer depends on $\varepsilon_r$ as well as $\sigma$.
(c) For a wet soil with $\rho = 100$ Ω·m and $\varepsilon_r = 20$, repeat (a) and
(b).
(d) For each of the eight entries, say whether you would use the wave equation, the
diffusion equation, or neither, and why.

---

**★6.** The exact Helmholtz equation.

(a) Show that for $e^{+i\omega t}$ the field satisfies
$\nabla^2\mathbf E = (i\omega\mu\sigma - \omega^2\mu\varepsilon)\mathbf E$ and hence
$k^2 = \omega^2\mu\varepsilon - i\omega\mu\sigma$.
(b) With $k = \beta - i\alpha$, derive the expressions for $\alpha$ and $\beta$.
(c) Evaluate $\alpha$, $\beta$, $\alpha/\beta$ and the phase velocity
$\omega/\beta$ at the crossover $\sigma/(\omega\varepsilon) = 1$ for a non-magnetic
medium, and compare the phase velocity with the lossless $c/\sqrt{\varepsilon_r}$.
(d) Compare $\alpha$ with the low-loss approximation
$(\sigma/2)\sqrt{\mu/\varepsilon}$ and with $1/\delta$ at the same frequency, and
state which (if either) is acceptable.

---

**★7.** Poynting's theorem.

(a) Derive $-\partial u/\partial t - \nabla\cdot\mathbf S = \mathbf J\cdot\mathbf E$
from the field equations, starting from
$\nabla\cdot(\mathbf E\times\mathbf H) = \mathbf H\cdot(\nabla\times\mathbf E)
- \mathbf E\cdot(\nabla\times\mathbf H)$.
(b) Identify $u$ and $\mathbf S$ and give their SI units.
(c) Compute the Poynting flux for $E = 1$ V/m in vacuum and in a medium with
$\varepsilon_r = 6$ ($\eta = 153.8$ Ω) and explain the difference.
(d) Identify the ohmic dissipation term and explain why it is the loss mechanism
that limits EM penetration.

---

**★8.** Numerical verification of the four equations (demo).

(a) Run the demo and report the Faraday and Ampère residuals for the exact vacuum
plane wave at three step sizes, and the observed convergence order.
(b) Explain why the Ampère residual is about nine orders of magnitude smaller than
the Faraday residual at the same step size, and what that demonstrates about the
displacement current.
(c) Report what the demo finds for $\nabla\cdot\mathbf E$ and $\nabla\cdot\mathbf B$
and explain why those are identically zero for a plane wave varying only in $z$.
(d) State the two independent curl equations' roles in fixing the amplitude ratio
and the wave speed.

---

## ★★★ Research-oriented

**★9.** Numerical dispersion of the 1-D Yee (FDTD) scheme.

(a) Starting from the exact staggered-grid dispersion relation
$\sin(\omega\Delta t/2) = (c\Delta t/\Delta x)\sin(k\Delta x/2)$, derive

$$\frac{c_{\text{num}}}{c} = \frac{\arcsin\!\left[\,\mathrm{cfl}\,
\sin(k\Delta x/2)\right]}{\mathrm{cfl}\,k\Delta x/2} , \qquad
\mathrm{cfl} = \frac{c\Delta t}{\Delta x} .$$

(b) Expand to leading order and show
$c_{\text{num}}/c = 1 - \frac{(k\Delta x)^2}{24}(1-\mathrm{cfl}^2) + O((k\Delta x)^4)$.
(c) Show that at $\mathrm{cfl} = 1$ the scheme is exact, and explain why this
"magic time step" is a one-dimensional accident.
(d) Check your formula against the demo's table: with 15 points per wavelength
$\mathrm{cfl} = 0.5$ the demo reports a relative error of $-5.498\times10^{-3}$;
verify that your leading-order result predicts $-5.483\times10^{-3}$ and state the
origin of the residual difference.

---

**★10.** Charge relaxation and the reason EM methods measure conductivity.

(a) Show that a free charge density in a homogeneous conductor decays as
$\rho(t) = \rho_0e^{-t/\tau_e}$ with $\tau_e = \varepsilon/\sigma$.
(b) Compute $\tau_e$ for rock ($\varepsilon_r = 6$, $\rho = 100$ Ω·m) and for
copper ($\sigma = 5.96\times10^{7}$ S/m, $\varepsilon\approx\varepsilon_0$).
(c) Explain what (a) means for the statement "electrostatics is useless for deep
exploration", and reconcile it with the fact that the *self-potential* method
measures steady potentials at the surface.
(d) Show that with $\rho = 0$ in the bulk the steady-current field obeys Laplace's
equation, and explain why this makes every EM method an inference about
*conductivity* rather than about charge.
