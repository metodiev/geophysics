# Exercises — 01-11-06 Dispersion Relations and Causality in Wave Physics

Attempt these **closed-book**, then open the
[solutions](./06-dispersion-relations-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

**State the sign convention in every answer.** Answers in this set are graded on
the convention being declared as much as on the result, because the two standard
conventions differ in the sign of every imaginary part.

---

## ★ Foundational

**★1.** The convention in this module is $e^{-i\omega t}$.

(a) Write the Kramers–Kronig relation for $\operatorname{Re}H(\omega)$ in both the
whole-line and the folded (positive-frequency) form.
(b) State which half plane $H$ is analytic in, and derive that statement in three
lines from $H(\omega) = \int_{0}^{\infty}h(t)e^{-i\omega t}\mathrm{d}t$.
(c) A paper writes the relation with the opposite overall sign. What convention
does the paper use, and what is the first thing you would check in its equations?

---

**★2.** For each response, state whether it can be the transfer function of a real
causal system under the $e^{-i\omega t}$ convention, and name the analyticity
region.

(a) $H(\omega) = \dfrac{1}{1+i\omega\tau}$
(b) $H(\omega) = \dfrac{1}{1-i\omega\tau}$
(c) $H(\omega) = e^{-a\omega^{2}}$ with $a>0$
(d) $H(\omega) = e^{i\omega t_{0}}$ with $t_{0}>0$

---

**★3.** A model has $\operatorname{Im}M(\omega) = -\dfrac{\Delta M\,\omega\tau}
{1+\omega^{2}\tau^{2}}$, growing linearly at low frequency and decaying as
$1/\omega$ at high frequency.

(a) Show that this is consistent with a modulus that vanishes at high frequency
(the "susceptibility" part of a relaxation).
(b) Use the Kramers–Kronig relation for the modulus to find
$\operatorname{Re}M(\omega)$ by partial fractions.
(c) Evaluate $\operatorname{Re}M$ at $\omega\tau = 1$ and compare with the direct
evaluation of your answer.

---

**★4.** A sinusoidal strain $\varepsilon = \varepsilon_{0}\cos\omega t$ produces a
stress $\sigma = \sigma_{0}\cos(\omega t - \phi)$ with $\phi = 30^{\circ}$.

(a) Write the complex modulus, including its phase.
(b) Compute the dissipated energy per cycle, $W = \oint\sigma\,\mathrm{d}\varepsilon$,
for $\varepsilon_{0} = 5\times10^{-4}$ and $\sigma_{0} = 20$ MPa.
(c) State the sign of $\operatorname{Im}M$ and check it against the requirement
$W>0$.

---

## ★★ Applied

**★★5.** A standard linear solid has $\tau_{\sigma} = 0.25$ s and
$\tau_{\varepsilon} = 1.0$ s.

(a) State $M_{R}$, $M_{U}$ and the ratio, taking $M_{R} = 10$ GPa.
(b) Give $\omega$ at which $1/Q$ peaks, the value of $1/Q$ there, and the peak's
dependence on the two time constants.
(c) State the low- and high-frequency limits of the wave velocity and the total
dispersion between them, with $\rho = 2600\ \mathrm{kg\,m^{-3}}$.
(d) Explain why this model cannot describe a medium with a $Q$ that is constant
over a decade.

---

**★★6.** A laboratory sample is driven at 10 Hz with
$\varepsilon_{0} = 10^{-3}$ and the measured stress amplitude is 30 MPa with a
phase lag of $\phi = 0.02$ rad.

(a) Compute $|M|$, $\operatorname{Re}M$, $\operatorname{Im}M$ and the sign of
$\operatorname{Im}M$.
(b) Compute the dissipated energy per unit volume per cycle from
$W = \pi\varepsilon_{0}^{2}\operatorname{Re}M\tan\phi$ and identify this with
$\pi\varepsilon_{0}^{2}|M|\sin\phi$.
(c) Give $1/Q$ and the attenuation $\alpha$ for a wave of speed
$3500\ \mathrm{m\,s^{-1}}$ in the same material, using
$\alpha = \omega/(2vQ)$.
(d) Over what distance is the amplitude reduced by a factor of $e$?

---

**★★7.** A model is proposed with $\operatorname{Re}H(\omega) = 1 - 0.3\omega^{2}\tau^{2}/(1+\omega^{2}\tau^{2})$
and $\operatorname{Im}H(\omega) = 0$, with $\tau = 0.1$ s.

(a) Is it causal? Give the Kramers–Kronig argument, with the value of the implied
$\operatorname{Im}H$ at $\omega\tau = 1$.
(b) Give the time-domain support of the impulse response predicted by the
Kramers–Kronig inconsistency.
(c) State what a measured response would have to show for this model to be
falsified *directly*, without any dispersion-relation argument.
(d) Is the model acceptable as a description of a *static* (frequency-independent)
elastic modulus? Explain.

---

**★★8.** For the Debye response with $\tau = 1$, the log-amplitude/phase relation
gives the numerical residuals in the table below (the companion script's output):

| $\omega$ | nodes | $\arg H$ exact | $\omega = 1$: P.V. | difference |
|---|---|---|---|---|
| 1.00 | $10^{5}$ | $-0.785398163397$ | $-0.785477295028$ | $7.9\times10^{-5}$ |
| 1.00 | $10^{6}$ | $-0.785398163397$ | $-0.785405309032$ | $7.2\times10^{-6}$ |

(a) What convergence rate in the node spacing does this demonstrate?
(b) Explain the mechanism, naming the property of $\ln|H|$ responsible.
(c) Estimate the number of nodes needed for a residual of $10^{-8}$, and comment
on whether the relation is *practically* useful at that accuracy.
(d) The conjugate Kramers–Kronig relation reaches $10^{-12}$ with the same code
and the same node count. Explain the contrast.

---

## ★★★ Research-oriented

**★★★9.** Consider a medium with a *single* relaxation and a peak
$1/Q_{\max} = 0.01$ — a value representative of a low-loss rock — and a seismic
band from 1 Hz to 100 Hz.

(a) Using the single-relaxation relation $1/Q_{\max} = (\rho-1)/(2\sqrt\rho)$ with
$\rho = M_{U}/M_{R}$, find $\rho$ and hence the total velocity dispersion
$v(\infty)/v(0)$ between the relaxed and unrelaxed limits.
(b) The band 1–100 Hz is centred two decades from the relaxation frequency in the
low-loss limit. Estimate the *fractional* velocity change across the band by
scaling (a), and state the assumption you made.
(c) Compare your estimate with the near-constant-$Q$ logarithmic law
$\Delta v/v = (1/\pi Q)\ln(\omega_{2}/\omega_{1})$ with $Q = 100$, and state which
assumptions that law requires that your single relaxation does not satisfy.
(d) Explain why the answer to (c) is a *model-selection* statement rather than a
statement about the Earth, and what measurement would settle it.

---

**★★★10.** You are asked to test whether a laboratory or field measurement is
consistent with causality, using a digitised amplitude and phase at 200
frequencies spanning two decades.

(a) Describe the numerical procedure: what you fit, what you integrate, and how
you handle the principal value.
(b) What is the *diagnostic quantity*, and what is its expected distribution if
the data are causal and the noise is Gaussian?
(c) State the two ways the test can give a false alarm, and how you would control
each.
(d) A colleague reports that the phase residuals pass the test but the attenuation
integral does not converge under refinement. What are the three most likely
explanations?

---

## Self-assessment before the solutions

- [ ] I stated the convention before writing any imaginary part.
- [ ] I distinguished the transfer-function form of Kramers–Kronig from the
      modulus form, including the sign.
- [ ] I derived the sign of $\operatorname{Im}M$ from the loop integral rather
      than from memory.
- [ ] I said explicitly which assumptions the near-constant-$Q$ law needs.
