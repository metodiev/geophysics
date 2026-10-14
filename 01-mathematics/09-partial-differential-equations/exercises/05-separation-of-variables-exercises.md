# Exercises — 01-09-05 Separation of Variables and Boundary Conditions

Attempt these **closed-book** before opening the
[solutions](./05-separation-of-variables-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Conventions: separation is carried out by writing $u = X(x)T(t)$ and choosing the
separation constant $-\lambda$ so that $\lambda \ge 0$ for the problems below;
$\kappa$ is a diffusivity in $\mathrm{m^2\,s^{-1}}$; eigenvalues of a
diffusion problem are decay *rates*; state the boundary conditions in full before
starting each part.

---

## ★ Foundational

**★1.** Separate $u_t = \kappa u_{xx}$ on $0<x<L$ with $u_x(0,t) = 0$ and
$u(L,t) = 0$.

(a) Write the two ordinary differential equations.
(b) Find the eigenvalues and eigenfunctions, and say whether $\lambda = 0$ is
allowed.
(c) State the general solution and the formula for the coefficients.

---

**★2.** For the triangular initial profile
$f(x) = 2x$ for $x\le\tfrac12$, $f(x) = 2(1-x)$ for $x>\tfrac12$ on $(0,1)$:

(a) compute $b_1$ analytically from
$b_n = 2\int_0^1f(x)\sin(n\pi x)\,dx$;
(b) compute $b_3$ and $b_5$;
(c) compare with the numerical values reported in the lesson
($b_1 = 0.810569$, $b_3 = -0.090063$, $b_5 = +0.032423$);
(d) explain why every even coefficient vanishes, without computing one.

---

**★3.** Using $T(z) = T_s + (q_0/k)z - Az^2/(2k)$ with
$k = 2.5\ \mathrm{W\,m^{-1}K^{-1}}$, $q_0 = 0.065\ \mathrm{W\,m^{-2}}$,
$A = 10^{-6}\ \mathrm{W\,m^{-3}}$ and $T_s = 10\ ^\circ$C, compute $T$ at 15 km and
25 km, and state how much of each value is due to the radiogenic term.

---

**★4.** Verify that $u(x,t) = T_0 + (T_1-T_0)x/L$ satisfies $u'' = 0$ and the
boundary conditions $u(0) = T_0$, $u(L) = T_1$. Then write down the problem
satisfied by $w = u - v$ for the heat equation with these same boundary conditions,
including the modified initial condition.

---

## ★★ Applied

**★★5.** For a string with $u(0,t) = 0$ and $u_x(L,t) = 0$, find the mode
frequencies and compare them with the fixed–fixed case of the same length. Which is
lower, and why does that make physical sense? State the ratio of the fundamentals.

---

**★★6.** A 1 km thick layer has $\kappa = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and an
initial sinusoidal temperature perturbation of wavelength 200 km.

(a) Compute the decay rate and the decay time of the fundamental from the
wavenumber.
(b) Reconcile the answer with $\tau \sim L^2/\kappa$ using $L$ equal to a quarter of
the wavelength, stating the numerical factor by which the two differ.
(c) Explain why the answer does not depend on the layer thickness here.

---

**★★7.** For the Robin problem $u_t = \kappa u_{xx}$ with $u_x(0,t) = 0$ and
$-u_x(L,t) = h\,u(L,t)$ (the ambient value has been subtracted):

(a) derive the transcendental equation for the eigenvalues;
(b) show that as $h\to\infty$ the roots approach the Dirichlet–Neumann
eigenvalues;
(c) state the physical meaning of the limit and of the case $h\to0$.

---

**★★8.** For a sphere of radius $a$ with a fixed zero surface temperature and a
uniform initial temperature, the radial eigenfunctions are
$j_0(k_nr) = \sin(k_nr)/(k_nr)$ with $k_n = n\pi/a$.

(a) State the decay rates of the first two modes.
(b) Compute the ratio of the two rates and say what it implies for fitting a single
exponential to observed cooling.
(c) For granite with $\kappa = 1.18\times10^{-6}\ \mathrm{m^2\,s^{-1}}$ and
$a = 500$ m, compute the time constant of the fundamental.

---

## ★★★ Research-oriented

**★★★9.** Implement the eigenfunction solution for the slab problem with the
triangular initial profile and measure how many terms are required for a
$10^{-8}$ maximum-norm error at $t = 0.5$, $0.05$ and $0.005$.

(a) Report the three counts.
(b) Explain the trend with $t$ using the modal attenuation factors
$\mathrm{e}^{-n^2\pi^2t}$.
(c) State the practical rule you would adopt for choosing the number of terms, and
say how it depends on the required accuracy.
(d) State the limits of your conclusion.

---

**★★★10.** A borehole temperature profile is modelled with a layered thermal
conductivity and a steady heat flow.

(a) Write out the layer-matching conditions and explain how they give a
transcendental equation for the modal decay rates.
(b) Describe an algorithm that finds the slowest decay rate, and say what could
make it fail.
(c) State precisely what would have to change for the problem to become
non-separable, and name the numerical alternative you would use.
