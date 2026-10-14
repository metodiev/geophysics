# Exercises — 01-09-03 The Wave Equation and Its Physical Content

Attempt these **closed-book** before opening the
[solutions](./03-wave-equation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: the wave equation is $u_{tt} = c^2u_{xx}$; the Courant number is
$\sigma = c\,\Delta t/\Delta x$; elastic wave speeds are
$\alpha^2 = (\lambda+2\mu)/\rho$ and $\beta^2 = \mu/\rho$; the shallow-water speed
is $\sqrt{gh}$ with $g = 9.81\ \mathrm{m\,s^{-2}}$. State any convention you add.

---

## ★ Foundational

**★1.** For a string with tension $T = 250$ N and linear density
$\rho_l = 0.02\ \mathrm{kg\,m^{-1}}$, compute the wave speed and the time for a
pulse to travel 15 m. State how the answer changes if the tension is halved.

---

**★2.** Verify by substitution that $u = \sin(kx)\cos(\omega t)$ solves
$u_{tt} = c^2u_{xx}$ provided $\omega = ck$. Then state the frequencies of a
string of length $L$ pinned at both ends, and explain which part of the
calculation fixes which quantity: the frequency, the wavenumber, or the amplitude.

---

**★3.** Compute the P and S speeds from
$\rho = 2600\ \mathrm{kg\,m^{-3}}$, $\lambda = 2.0\times10^{10}$ Pa,
$\mu = 1.5\times10^{10}$ Pa. Then compute Poisson's ratio from
$\nu = (\alpha^2 - 2\beta^2)/(2(\alpha^2 - \beta^2))$ and comment on the value.

---

**★4.** A tsunami crosses 1000 km of ocean of depth 4 km. Compute the travel time.
State the assumptions of the shallow-water approximation and say whether they hold
for a 200 km wavelength in 4 km of water.

---

## ★★ Applied

**★★5.** Carry out the von Neumann stability analysis of the leapfrog scheme
completely: substitute $u^n_j = g^n\mathrm{e}^{\mathrm{i}j\theta}$, obtain the
quadratic for $g$, identify the product of its roots, and determine the condition
on $\sigma$ under which both roots have modulus 1. State where the alternating mode
$\theta = \pi$ enters and what happens to it when $\sigma = 1$.

---

**★★6.** For $\sigma = 1.02$:

(a) compute the modulus of the amplification factor of the alternating mode from
$\lvert g\rvert = (\lvert 2-4\sigma^2\rvert + \sqrt{(2-4\sigma^2)^2-4})/2$;
(b) predict the factor by which an initial error of $10^{-12}$ grows in 500 steps;
(c) state whether a single-precision calculation (about 7 significant decimal
digits) could complete the 500 steps at all, and justify your answer.

---

**★★7.** Show that the leapfrog scheme with $\sigma = 1$ reduces to
$u^{n+1}_j = u^n_{j+1} + u^n_{j-1} - u^{n-1}_j$, and verify by substitution that
$u^n_j = f(j\Delta x - n\Delta t)$ satisfies it for any $f$. Then state the
condition on the initialisation (the value chosen for $u^{-1}_j$) for the scheme to
be *exact*, and what the error becomes when that condition is violated.

---

**★★8.** The energy
$\int_0^L(\tfrac12u_t^2 + \tfrac12c^2u_x^2)dx$ is conserved for the wave equation
with fixed ends.

(a) Derive the conservation statement by multiplying the equation by $u_t$ and
integrating.
(b) An explicit scheme that is *non-dissipative* neither gains nor loses energy.
Explain why that is desirable for a long seismic record and what risk it carries.
(c) How does this differ from the diffusion equation's energy
$\int u^2\,dx$, and why does the difference matter for long-time integration?

---

## ★★★ Research-oriented

**★★★9.** Implement the leapfrog scheme for $u_{tt} = c^2u_{xx}$ with a
variable velocity $c(x) = 1 + 0.5\sin(2\pi x)$ on $(0,1)$ with fixed ends.
Measure the convergence order against a grid-refinement reference at a fixed final
time, report the observed order, explain why the $\sigma = 1$ exactness of the
constant-velocity case does not survive, and state exactly how you chose the time
step (including which velocity sets it). Report the method, the numbers and the
limits of the conclusion.

---

**★★★10.** A modelling code uses a uniform grid with $\Delta x = 10$ m and a
maximum velocity $c_{\max} = 6000\ \mathrm{m\,s^{-1}}$.

(a) A colleague proposes $\Delta t = 2$ ms. Compute $\sigma$ and state whether the
run will be stable.
(b) If not, propose a time step and state the cost penalty in number of steps
relative to the proposal.
(c) The target data have a dominant frequency of 40 Hz and the code requires
8 points per wavelength for acceptable numerical dispersion accuracy. Compute the
required $\Delta x$ for $c_{\max}$, and redraw the time-step budget for that grid.
(d) Discuss the tension between the CFL limit, the dispersion requirement and the
run time, and state which constraint binds in your answer.
