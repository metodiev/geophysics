# Exercises — 01-09-01 Classification of PDEs: Elliptic, Parabolic, Hyperbolic

Attempt these **closed-book** before opening the
[solutions](./01-classification-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Convention for the whole set: the principal part of a second-order equation is
written $A\,u_{xx} + 2B\,u_{xy} + C\,u_{yy}$ and the class is read from
$\Delta = B^2 - AC$. When an equation involves $u_t$, treat $(x,t)$ as the two
independent variables for the purpose of the test, and say which variable plays
the role of the second one. State your conventions.

---

## ★ Foundational

**★1.** Classify each equation. In every case write down the principal part, the
coefficient triple $(A,B,C)$ and the discriminant, and say which of the three
classes follows:

(a) $u_{xx} + 4u_{xy} + 4u_{yy} = 0$;
(b) $u_{xx} + u_{xy} + u_{yy} = 0$;
(c) $u_{xx} - 4u_{yy} = 0$;
(d) $3u_{xx} + 2u_{xy} + 3u_{yy} = 0$.

Watch the factor of two on the mixed term.

---

**★2.** For each problem, state exactly which data are required — a boundary
condition, an initial condition, or both, and *where* — and justify the count from
the class rather than from convention:

(a) $u_t = \kappa u_{xx}$ on $0 < x < 1$, $t > 0$;
(b) $\nabla^2V = 0$ in a bounded region $\Omega$;
(c) $u_{tt} = c^2u_{xx}$ on $0 < x < 1$, $t > 0$.

---

**★3.** The convection–diffusion equation is
$u_t + v\,u_x = \kappa\,u_{xx}$ with $v$ a constant velocity. Classify it when

(a) $\kappa = 0$ and $v \ne 0$;
(b) $v = 0$ and $\kappa > 0$;
(c) both $v > 0$ and $\kappa > 0$.

Name a geophysical process described by each case.

---

**★4.** Show that $u_{xx} + 2u_{xy} + u_{yy} = 0$ has the single characteristic
family $y - x = \text{const}$, and find its general solution by the change of
variables $\xi = y - x$, $\eta = y$. Verify your general solution by substitution.

---

## ★★ Applied

**★★5.** Derive the characteristic equation
$A\,(dy/dx)^2 - 2B\,(dy/dx) + C = 0$ by the argument of Section 3.1 of the
lesson: parametrise a curve, write the second derivatives of $u$ along it in terms
of data on the curve, and identify the condition under which they cannot be
determined from that data.

---

**★★6.** The skin depth for diffusive electromagnetic fields in a conductor is
$\delta = \sqrt{2/(\omega\mu\sigma)}$ with $\mu = \mu_0 = 4\pi\times10^{-7}$
(the units of $\mu_0$ are $\mathrm{T\,m\,A^{-1}}$).

(a) For $\sigma = 0.01\ \mathrm{S\,m^{-1}}$ at $f = 1$ Hz, compute $\delta$ in
metres and in kilometres.
(b) For a 100 MHz ground-penetrating radar pulse in the same rock with
$\epsilon_r = 6$, compute the loss tangent $\sigma/(\omega\epsilon)$ and decide
whether the wave equation or the diffusion equation is the better description.
(c) State the criterion you used and give the approximate value of the loss
tangent at which the two descriptions cross over.

---

**★★7.** An equation has principal part $A\,u_{xx} + 2B\,u_{xy} + C\,u_{yy}$ with
$A = 1$, $B = x$, $C = 1 - y$. Find the regions of the $(x,y)$ plane in which it
is elliptic, parabolic and hyperbolic, and describe the dividing curve. State what
"mixed type" means physically for a flow problem.

---

**★★8.** Adding a relaxation term to the diffusion equation gives
$u_t + \tau\,u_{tt} = \kappa\,u_{xx}$ with $\tau \ge 0$. Compute the discriminant
of the principal part in the variables $(x,t)$ and determine for which $\tau$ the
equation is parabolic and for which it is hyperbolic. Identify the physical process
described by the hyperbolic case, and explain why the value $\tau = 0$ is special.

---

## ★★★ Research-oriented

**★★★9.** Design a numerical experiment that distinguishes elliptic, parabolic
and hyperbolic behaviour using **only** the response to a localised disturbance at
a single interior point of the domain. Specify:

- the diagnostic quantity you would measure;
- the expected scaling of that diagnostic with grid spacing and with time for each
  of the three classes;
- how you would falsify a classification that was wrong.

Then run your experiment (you may reuse the scripts in this module's `code/`
directory as a starting point), report the observed numbers, and state the limits
of your conclusion. A genuine numerical-experiment report states the method, the
result and the uncertainty.

---

**★★★10.** A paper reports that a magnetic anomaly can be explained either by a
magnetised body at 4 km depth or by a larger, less strongly magnetised body at
8 km.

Using only (i) the classification of the governing equation and (ii) the
properties of harmonic functions, write a critique of the claim that one of the two
models must be "wrong". Your answer should:

- name the class and the equation;
- state which properties of harmonic functions bear on the question;
- explain what kind of additional data would break the tie;
- state what the paper would have to report for its claim to be defensible.

You do not need to model the anomaly; argue from the equation.
