# Exercises — 01-11-01 Complex Numbers, Polar Form and Argand Diagrams

Attempt these **closed-book**, on paper, before opening the
[solutions](./01-complex-arithmetic-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

A calculator that handles complex numbers is allowed only to check an answer you
have already obtained by hand.

---

## ★ Foundational

**★1.** Convert to polar form, giving the modulus exactly where possible and the
principal argument in degrees to three decimals. State the interval you are
using for the argument.

(a) $2 - 2i$
(b) $-3 + 4i$
(c) $-1 - i\sqrt{3}$
(d) $5i$

---

**★2.** Without converting to rectangular form, compute
$\bigl(3e^{i40^{\circ}}\bigr)\bigl(2e^{-i25^{\circ}}\bigr)$ and confirm the
result against the rectangular product. State which of the two routes is quicker
and why.

---

**★3.** Compute $\dfrac{4+3i}{1-2i}$ by rationalising, and verify that the
modulus of the result equals the ratio of the moduli.

---

**★4.** Use De Moivre's theorem to compute $(1+i)^{8}$ exactly, then find all
three cube roots of $8i$ and verify that their sum is zero.

---

## ★★ Applied

**★★5.** Three sinusoidal ground-velocity components of the same frequency are
recorded on a three-component sensor:

$$v_{1} = 3\cos\omega t, \qquad
v_{2} = 4\cos(\omega t + 60^{\circ}), \qquad
v_{3} = 2\cos(\omega t - 45^{\circ}).$$

(a) Write each as a phasor and compute the phasor sum.
(b) State the amplitude and phase of the sum, in degrees.
(c) Explain, in one sentence, why the answer does **not** depend on $\omega$.

---

**★★6.** A series $R$–$C$ network has $R = 1000\ \Omega$ and
$C = 100\ \mathrm{nF}$.

(a) Write the impedance $Z(\omega)$ and find $|Z|$ and $\arg Z$ at
$f = 1000\ \mathrm{Hz}$.
(b) Find the corner frequency $1/(2\pi RC)$ and state the values of $|Z|$ and
$\arg Z$ there.
(c) Find the frequency at which $|Z| = 1500\ \Omega$, and give the phase there.
(d) A colleague writes $i = v/R$ and concludes that the current is "in phase with
the voltage at all frequencies". Identify the error and give the correct
statement.

---

**★★7.** A damped driven oscillator has $m = 1.0\ \mathrm{kg}$,
$c = 2.0\ \mathrm{N\,s\,m^{-1}}$ and $k = 100\ \mathrm{N\,m^{-1}}$, driven by
$F_{0}\cos\omega t$.

(a) Write the impedance $Z(\omega)$ and compute the steady-state amplitude at
$\omega = 8$, $10$ and $12\ \mathrm{rad\,s^{-1}}$.
(b) Find the frequency of the amplitude peak and compare it with
$\omega_{0} = \sqrt{k/m}$.
(c) Sketch (or describe precisely) the phase of the response at
$\omega \ll \omega_{0}$, $\omega = \omega_{0}$ and $\omega \gg \omega_{0}$.

---

**★★8.** State whether each set describes a circle, a line, or neither, and give
its centre and radius where applicable.

(a) $|z - 3 + 2i| = 4$
(b) $|z - 1| = |z + i|$
(c) $\operatorname{Re} z > 2$
(d) $|z|^{2} = z + \bar z$

---

## ★★★ Research-oriented

**★★★9.** Two sinusoids of *slightly* different frequencies,
$\cos(\omega_{1}t)$ and $\cos(\omega_{2}t)$ with
$\Delta\omega = \omega_{2}-\omega_{1} \ll \omega_{1}$, are added.

(a) Explain why a single phasor cannot represent the sum.
(b) Derive the beat envelope, and give the envelope period and the carrier
frequency.
(c) A seismic trace contains two arrivals of the same wavelet with a $20$
ms time lag and a dominant frequency of $25\ \mathrm{Hz}$. Estimate the
period of the amplitude modulation you would see in the trace and say why
this is used to detect multiples.
(d) State the condition under which a phasor description of a **filter** still
applies even though the input is a sum of two frequencies.

---

**★★★10.** In a magnetotelluric sounding the horizontal-field impedance at one
period ($T = 100$ s) is measured, after rotation to principal axes, as
$Z = 2.80\times10^{-3} + 1.20\times10^{-3}i$ in SI units
($\mathrm{V\,m^{-1}}$ per $\mathrm{A\,m^{-1}}$).

(a) Compute the apparent resistivity $\rho_{a} = |Z|^{2}/(\mu_{0}\omega)$ with
$\mu_{0} = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$ and $\omega = 2\pi/100$
rad s⁻¹, and the impedance phase $\phi = \arg Z$ in degrees.
(b) Standard practice reports the phase in $(0^{\circ}, 90^{\circ})$ for a
resistive half-space. Is this value consistent with that expectation, and what
does a negative phase mean physically?
(c) The same quantity is quoted by another author as
$\phi = 23.2^{\circ}$ after a $180^{\circ}$ rotation of the axes. Explain the
relationship between the two conventions and why the sign has to be stated.
(d) Two stations differ by a $2\pi$ offset in their numerically unwrapped
impedance phase. Give two independent checks that would decide which is correct.

---

## Self-assessment before the solutions

- [ ] I converted every quantity in ★1 without a calculator and stated my
      argument interval.
- [ ] I used the polar route for ★2 and understood why it is faster.
- [ ] I did ★6(a) without first computing the current.
- [ ] I can write down the resonance condition from memory in ★7(b).
- [ ] I stated a physical meaning, not only a number, in ★10(b).
