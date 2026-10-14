# Exercises — 01-09-02 The Diffusion/Heat Equation and Diffusive Timescales

Attempt these **closed-book** before opening the
[solutions](./02-heat-equation-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions for the whole set: the diffusion equation is written
$u_t = \kappa\nabla^2u$ with $\kappa$ the **diffusivity** in
$\mathrm{m^2\,s^{-1}}$; $\tau \sim L^2/\kappa$ always means the diffusive
timescale computed with exactly that expression (not with $\sqrt{\kappa t}$ and
not with $4\kappa t$), and every answer must state the convention it used. Use
$k$ for thermal conductivity ($\mathrm{W\,m^{-1}K^{-1}}$), $\rho c$ for volumetric
heat capacity, $k$ for permeability only where stated explicitly, and
$\mu_0 = 4\pi\times10^{-7}\ \mathrm{T\,m\,A^{-1}}$. One year is taken as
$3.156\times10^{7}$ s.

---

## ★ Foundational

**★1.** Compute $\kappa = k/(\rho c)$ for

(a) granite with $k = 2.5\ \mathrm{W\,m^{-1}K^{-1}}$,
$\rho = 2650\ \mathrm{kg\,m^{-3}}$,
$c = 800\ \mathrm{J\,kg^{-1}K^{-1}}$;
(b) water-saturated sand with $k = 1.8\ \mathrm{W\,m^{-1}K^{-1}}$,
$\rho = 2100\ \mathrm{kg\,m^{-3}}$,
$c = 1400\ \mathrm{J\,kg^{-1}K^{-1}}$.

Which material transmits a thermal disturbance faster, and by what factor? State
whether your answer would change if $c$ were uncertain by 20 %.

---

**★2.** Using $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$, compute the time for a
surface temperature perturbation to reach (a) 50 m, (b) 500 m and (c) 2 km.
Express each answer in years, and say which of them is relevant to (i) a borehole
palaeoclimate study and (ii) a lithospheric thermal model.

---

**★3.** Verify by substitution that
$u(x,t) = \mathrm{e}^{-\kappa n^2\pi^2t/L^2}\sin(n\pi x/L)$ solves
$u_t = \kappa u_{xx}$ on $0<x<L$ and satisfies $u(0,t) = u(L,t) = 0$. State the
decay rate and the half-life of the $n = 1$ mode for $\kappa = 10^{-6}$ and
$L = 1$ km.

---

**★4.** Derive the skin depth $\delta$ from $k^2 = \mathrm{i}\omega\mu\sigma$ by
writing $k = \alpha + \mathrm{i}\beta$ and solving for $\alpha$ and $\beta$. Show
that $\delta = 1/\beta$ and confirm the identity $\mu\sigma\delta^2 = 1/(\pi f)$.
State which physical assumption of the parabolic approximation the derivation
relies on.

---

## ★★ Applied

**★★5.** A confined aquifer has $T = 0.02\ \mathrm{m^2\,s^{-1}}$ and
$S = 2\times10^{-4}$.

(a) Compute the aquifer diffusivity $D = T/S$.
(b) How long until a pressure change 20 km away is observable?
(c) State two reasons why your answer is an order-of-magnitude statement rather
than a prediction.

---

**★★6.** A dyke of thickness $b$ is sometimes said to cool on the timescale
$b^2/\kappa$. For $b = 500$ m and $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$:

(a) compute $b^2/\kappa$ in years;
(b) compute the decay time of the slowest mode of a slab of thickness $b$ with
both faces held at a fixed temperature;
(c) explain why the two differ by a modest factor rather than orders of magnitude,
and identify the factor.

---

**★★7.** An injection well produces a pore-pressure front. Using
$D = 0.5\ \mathrm{m^2\,s^{-1}}$:

(a) compute the distance reached in 30 days and in 365 days;
(b) compute the ratio of those distances and compare it with the ratio of the
times;
(c) explain why the two ratios are different, and what would have to be true of a
front for them to be equal.

---

**★★8.** Show that the fundamental solution
$\Phi(x,t) = (4\pi\kappa t)^{-1/2}\mathrm{e}^{-x^2/(4\kappa t)}$ satisfies
$\int_{-\infty}^{\infty}\Phi\,dx = 1$ for all $t>0$. State what this conservation
means physically, and which behaviour at infinity the derivation requires.
Comment on whether the integral is conserved by a finite-difference scheme on a
bounded domain.

---

## ★★★ Research-oriented

**★★★9.** Take $u_t = \kappa u_{xx}$ on $(0,1)$ with $u(0,t) = 1$,
$u(1,t) = 0$ and the step initial condition $u = 1$ for $x<0.5$, $u = 0$ for
$x>0.5$. Subtract the steady profile $1-x$ so that the boundary data for the
remainder are homogeneous, and use its Fourier sine series (with enough terms) as
the reference solution.

Measure the observed convergence order in the maximum norm at $t = 10^{-2}$,
$10^{-3}$ and $10^{-4}$ on a sequence of grids. Report the orders, state whether
they are stable, and identify the dimensionless quantity that controls when the
order degrades. Explain the finding physically: the operator smooths instantly, so
what is it that the grid still has to resolve? This is a genuine numerical
experiment; state the method, the result and the limits of your conclusion.

---

**★★★10.** Write a short critical note on the following sentence, as if
reviewing a paper:

> "The 5 km migration of seismicity in 12 months implies a hydraulic diffusivity
> of $0.7\ \mathrm{m^2\,s^{-1}}$, hence a permeability of about
> $10^{-9}\ \mathrm{m^2}$, consistent with a fractured reservoir."

Your note must:

- list every assumption the inference requires, distinguishing assumptions about
  the physics from assumptions about the numbers;
- give the storage value the inference implies if the permeability is
  $10^{-9}\ \mathrm{m^2}$ with $\mu = 10^{-3}\ \mathrm{Pa\,s}$, and say whether
  that value is realistic for the rock described;
- state one independent measurement that would test the inference;
- rewrite the sentence so that it is defensible at the paper's own level of
  evidence.
