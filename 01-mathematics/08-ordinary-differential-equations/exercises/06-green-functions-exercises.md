# Exercises — 01-08-06 Green's Functions and Impulse Response

Attempt these **closed-book** before opening the
[solutions](./06-green-functions-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Companion lesson: [06 Green's Functions](../06-green-functions.md).

---

## ★ Foundational

**★1.** Find the Green's function of $-\dfrac{d^{2}}{dx^{2}}$ on $(0,1)$ with
$u(0) = 0$ and $u'(1) = 0$.

(a) Write the general solution on each side of the source, impose the boundary
conditions, the continuity at $\xi$, and the jump condition on the derivative.
(b) Compare your result with the case $u(0) = u(1) = 0$ from the lesson, and
state the physical difference between the two kernels.
(c) Verify the jump condition by differentiating your answer at $x = \xi \pm
\epsilon$.

---

**★2.** For the first-order operator $L = d/dt + a$ with $a = 2$ and
$y(0) = 0$:

(a) Show that $G(t) = e^{-2t}H(t)$ satisfies $LG = \delta$.
(b) Compute the response to $f(t) = e^{-t}$ in closed form.
(c) Evaluate the response at $t = 0.5$, $1$ and $2$, and state the value that
would be obtained by convolving numerically with 20 000 Simpson panels.

---

**★3.** A damped oscillator with $\omega_0 = 1$ and $\zeta = 0.1$ is driven by a
unit step, $x(0) = x'(0) = 0$.

(a) Write the step response as the convolution of $G$ with the unit step and
evaluate the integral.
(b) Give the steady-state value and the value at $t = 1$, $5$ and $20$.
(c) State what happens to the response if $\zeta = 0$ and the driving frequency
equals $\omega_0$, and quote the growth law.

---

## ★★ Applied

**★★4.** A finite-width pulse is used as a numerical impulse. The measured error
in reproducing $G(t)$ is

| $\epsilon$ | 0.4 | 0.2 | 0.1 | 0.05 | 0.025 |
|---|---|---|---|---|---|
| error | $3.99\times10^{-2}$ | $3.10\times10^{-2}$ | $1.81\times10^{-2}$ | $9.56\times10^{-3}$ | $4.73\times10^{-3}$ |

(a) Compute the error ratios and state the order of convergence.
(b) Derive analytically why the error is first order in $\epsilon$.
(c) Explain why the ratios approach the asymptotic value only slowly, and what
this implies for a convergence study that uses only two pulse widths.

---

**★★5.** For the operator $-\dfrac{d^{2}}{dx^{2}}$ on $(0,1)$ with
$u(0) = u(1) = 0$, the Green's function is the tent
$G(x,\xi) = x(1-\xi)$ for $x\le\xi$ and $\xi(1-x)$ for $x\ge\xi$.

(a) Prove reciprocity, $G(x,\xi) = G(\xi,x)$ directly from the formula, for each
of the two cases.
(b) Derive the reciprocity property in one line from the Lagrange identity of
[05 Sturm–Liouville Theory](../05-sturm-liouville.md), stating the boundary
assumption you used.
(c) State the observational consequence of reciprocity for a seismic survey.

---

**★★6.** A linear system with impulse response $G(t)$ is driven by
$f(t) = 1 - e^{-t}$.

(a) Write the convolution integral and evaluate it for a first-order operator
with $a = 2$.
(b) Verify that the result satisfies the ODE and the initial condition by
substitution.
(c) State the superposition property you used, and give one measurement
procedure where it is the working assumption.

---

## ★★★ Research-oriented

**★★★7.** The transfer function of a damped oscillator with $\omega_0 = 1$,
$\zeta = 0.1$ is
$\hat G(\omega) = \left[1-\omega^{2}+0.2i\omega\right]^{-1}$.

(a) Find the poles and state which half plane they lie in.
(b) Explain, using Jordan's lemma, why a pole in the lower half plane would
produce a non-zero response for $t<0$.
(c) A model is fitted to a *measured amplitude* response and gives a good match
but places a pole in the lower half plane. State what measurement would expose
the error and why.

---

**★★★8.** The three-point stencil for $-u'' = f$ on $(0,1)$ with $u(0) = u(1) = 0$
uses source weights such that a unit impulse at $\xi$ is distributed over the
two neighbouring nodes with weights $(1-\alpha)/h$ and $\alpha/h$, where
$\xi = (k+1+\alpha)h$.

(a) Show that placing the whole weight on the nearest node (that is, using
$\alpha \in \{0,1\}$) gives an error that is first order in $h$, while the
distributed version is exact for this operator. Use the tabulated result
"max error $1.474\times10^{-2}$ at 20 nodes with ratio 1.91 per halving" as your
evidence for the first-order claim.
(b) Derive the exactness of the distributed version by showing that the exact
piecewise-linear $G$ satisfies the discrete equations identically.
(c) State the general rule this illustrates about discretising a source term,
and name one geophysical modelling context where misplacing the source would
matter.

---

## Extension ideas

- Derive the Green's function of the diffusion equation on the whole line,
  $G(x,t) = (4\pi\kappa t)^{-1/2}e^{-x^{2}/4\kappa t}$, and show that
  $\int G\,dx = 1$ for every $t>0$ and that $\sigma = \sqrt{2\kappa t}$.
- Show that the convolution of two Green's functions corresponds to the
  composition of two operators, e.g. that $G_{L_2L_1} = G_{L_2}\ast G_{L_1}$,
  and give a physical example.
- Deconvolve a synthetic trace by an impulse response with a small
  high-frequency $\lvert\hat G\rvert$, with and without a water-level
  stabilisation, and describe what the unstabilised version does to the noise.
