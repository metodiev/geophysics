# Exercises — 01-11-04 The Laplace Transform and Transient Problems

Attempt these **closed-book**, then open the
[solutions](./04-laplace-transform-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

For every initial-value problem state the transform of the derivative you use,
including the initial condition. Several marks in this set are for stating the
region of convergence or the validity condition of a theorem.

---

## ★ Foundational

**★1.** Compute from the defining integral:

(a) $\mathcal{L}\{t^{2}\}$
(b) $\mathcal{L}\{e^{-3t}\cos 2t\}$
(c) $\mathcal{L}\{u(t-2)\}$, the unit step switched on at $t=2$.

State the region of convergence in each case.

---

**★2.** Solve $\dot y + 3y = e^{-t}$ with $y(0) = 2$ by transforming, and verify
your solution satisfies the differential equation and the initial condition.

---

**★3.** Solve $\ddot y + 4y = 0$ with $y(0) = 1$, $\dot y(0) = 0$, and say which
of the two initial conditions would have changed the answer had it been non-zero.

---

**★4.** Apply the initial- and final-value theorems to

$$F(s) = \frac{3s+5}{s(s^{2}+4s+5)}.$$

State whether each theorem's hypothesis holds, and give the limits (or say that
they do not exist).

---

## ★★ Applied

**★★5.** Solve $\ddot y + 3\dot y + 2y = 1$ with $y(0) = \dot y(0) = 0$.

(a) Find $Y(s)$ and its partial fractions.
(b) Invert by residues of $Y(s)e^{st}$, listing the residues.
(c) State the final value and the slowest time constant, and say which pole
supplies each.

---

**★★6.** A seismometer is modelled as a damped oscillator with a step input:
$\ddot x + 2\zeta\omega_{0}\dot x + \omega_{0}^{2}x = \omega_{0}^{2}$,
$x(0) = \dot x(0) = 0$, with $\omega_{0} = 20$ rad s⁻¹ and $\zeta = 0.5$.

(a) Find $X(s)$ and the poles.
(b) Invert and describe the transient qualitatively.
(c) At what time does the response first reach $90\%$ of its final value? Estimate
it from the dominant pole and say why your estimate is an over- or
under-estimate.

---

**★★7.** Invert

$$F(s) = \frac{s+5}{s^{2}+4s+13}$$

and verify your answer at $t = 0$ and as $t\to\infty$.

---

**★★8.** The diffusive response is $F(s) = e^{-a\sqrt s}/s$ with $a>0$.

(a) Where are the singularities, and what kind are they?
(b) Why can the inversion not be written as a sum of residues?
(c) State the inverse and check its two limits $t\to0^{+}$ and $t\to\infty$.
(d) A colleague inverts numerically and obtains a smooth curve with a kink at the
point where the branch cut would be crossed. What has gone wrong?

---

## ★★★ Research-oriented

**★★★9.** Invert $Y(s) = 1/[s(s+2)]$ by a numerical Bromwich integral and by
residues, and account for the difference.

(a) Choose $c$, state the singularities of $Y(s)e^{st}$ and hence the minimum
acceptable $c$.
(b) Explain why the vertical-line quadrature converges only as $1/\Omega$ while
the residue sum is exact at every $\Omega$.
(c) The measured difference between the truncated line integral and the residue
sum at $t=1$ is about $1.6\times10^{-4}$ for $\Omega = 200$ and
$1.4\times10^{-4}$ at $t=3$. Is that consistent with $1/\Omega$ convergence?
What would you check next?
(d) Give two independent checks on an inverted transient that do **not** use the
transform.

---

**★★★10.** A thermistor probe measures ground temperature. The surface
temperature is stepped from $T_{0}$ to $T_{1}$ at $t=0$ and held.

(a) Write the one-dimensional diffusion problem and its Laplace-domain solution
$T(x,s)$ for a semi-infinite conducting medium with diffusivity $\kappa$.
(b) Invert and state the result.
(c) At what depth is the temperature change half the surface step at $t = 30$
days, with $\kappa = 10^{-6}\ \mathrm{m^{2}\,s^{-1}}$?
(d) The probe has a first-order response with time constant $\tau_{p} = 1$ h.
Write the transfer function of the combined system and explain why the surface
step is *not* instantaneous as seen by the probe.
(e) A second probe at twice the depth records the half-amplitude time. How much
later does it lag the first, in the same units? State the scaling law you used.

---

## Self-assessment before the solutions

- [ ] I wrote the transform of the derivative correctly in every problem.
- [ ] I stated the region of convergence or the hypothesis of each theorem.
- [ ] I identified the branch point in ★★8 and did not try to compute a residue
      there.
- [ ] I distinguished the *split* between line and arc from the *value* of the
      integral in ★★★9.
