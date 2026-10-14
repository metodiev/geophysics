# Exercises — 02-07-02 Magnetostatics, Biot–Savart and Ampère's Law

Attempt these **closed-book** before opening the
[solutions](./02-magnetostatics-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/magnetostatics_demo.py`](../code/magnetostatics_demo.py) require you to
run it and report its actual output. Use
$\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N/A² throughout, and use the nominal
geomagnetic equatorial field of 30 000 nT where a nominal value is called for —
saying so in your answer.

---

## ★ Foundational

**★1.** A straight wire of half-length $L = 0.5$ m carries $I = 5$ A.

(a) Compute the field at perpendicular distance $s = 0.1$ m from the midpoint
using the finite-wire formula, and the infinite-wire value.
(b) Compute the ratio and compare it with $L/\sqrt{L^2+s^2}$.
(c) Find the aspect ratio $L/s$ at which the finite and infinite models agree to
1 %.
(d) State why the infinite-wire model is nevertheless the standard one for a
borehole sonde.

---

**★2.** Using Ampère's law:

(a) Compute $B$ inside a long solenoid of 1000 turns per metre carrying 2 A, and
express it as a multiple of the nominal geomagnetic field.
(b) Compute $B$ inside a toroid of 500 turns carrying 1 A at radius 0.05 m.
(c) Compute $B$ at 0.05 m from a long straight wire carrying 5 A.
(d) State the three conditions that must hold for Ampère's law to give these
results in one line, with no integral.

---

**★3.** A circular loop of radius $a = 0.2$ m carries $I = 10$ A.

(a) Derive the on-axis field $B_z(z)$ from Biot–Savart.
(b) Evaluate it at $z = 0$, $z = a$ and $z = 10a$.
(c) Compute the magnetic dipole moment.
(d) State the two limits of (b) in words, and the physical reason the far-field
falls off faster than the near field.

---

**★4.** The magnetic flux density satisfies $\nabla\cdot\mathbf B = 0$.

(a) Show by direct differentiation that the dipole field of equation (8) of the
lesson has zero divergence everywhere except possibly at the origin.
(b) Explain how the demo distinguishes a truncation error from a quadrature error
in its divergence table, and what the observed scaling is.
(c) State what $\nabla\cdot\mathbf B = 0$ permits (a vector potential, a scalar
potential where $\mathbf J = 0$) and what it forbids (a magnetic monopole).
(d) If a magnetic monopole of charge $q_m$ existed, write down the equation that
would replace $\nabla\cdot\mathbf B = 0$ and name one consequence for the design of
EM instruments.

---

## ★★ Applied

**★5.** A loop of radius $a = 0.2$ m carries $I = 10$ A, so
$m = 1.2566$ A m².

(a) Compute the axial and equatorial fields at $r = 1$, 2 and 5 m from the dipole
formula.
(b) Compare with the exact loop field at $r = 2a$ and $r = 5a$ (from the demo's
table, or by quadrature) and state at what $r/a$ the dipole approximation is good
to 1 %.
(c) Explain why the *equatorial* field is negative (anti-parallel to $\mathbf m$)
and what error a missing sign would cause in a modelled anomaly.
(d) State the ratio of the axial to equatorial amplitudes and derive it.

---

**★6.** A transmitter coil is to double its depth of investigation, all else being
equal.

(a) By what factor must its magnetic moment increase?
(b) A single-turn 1 m² loop is replaced by a 100-turn coil of the same area. What
current ratio achieves the same moment?
(c) A coil of 100 turns and 0.1 m radius carries 5 A. Compute its moment and the
on-axis field at 1 m, 10 m and 100 m.
(d) Compare the field at 100 m with the nominal geomagnetic field and explain why
EM systems measure the time-varying, coil-referenced component.

---

**★7.** Ampère's law for a finite wire.

(a) Derive the line integral of $\mathbf B$ around a circle of radius $s$ in the
midplane of a finite wire of half-length $L$, and show that it equals
$\mu_0IL/\sqrt{s^2+L^2}$.
(b) Evaluate the shortfall from $\mu_0I$ for $L = 500$ m, $s = 0.05$ m, $I = 10$ A,
and express it as a percentage.
(c) Explain why Ampère's law in the form $\oint\mathbf B\cdot\mathrm d\boldsymbol\ell
= \mu_0I_{\text{enc}}$ requires current conservation.
(d) The demo reports a non-linking path giving $-3.0\times10^{-21}$ T m where
$\mu_0I = 1.2566\times10^{-5}$ T m. Interpret the number relative to the linking
path and to double precision.

---

**★8.** The Earth's dipole.

(a) Compute the dipole moment from a nominal equatorial surface field of 30 000 nT
and the mean Earth radius $6.371\times10^6$ m.
(b) Compute the axial (polar) surface field implied by the same moment, and
compare with the nominal polar value of about 60 000 nT.
(c) Explain what quantity you must consult to obtain the *current* dipole moment,
and why quoting a fixed value is wrong.
(d) The moment is inferred, not measured. State precisely what is measured, what is
assumed, and what the assumption's first-order error is.

---

## ★★★ Research-oriented

**★9.** Vector potential.

(a) Show that for the dipole field of equation (8),
$\mathbf A = \frac{\mu_0}{4\pi}\frac{\mathbf m\times\hat{\mathbf r}}{r^2}$
satisfies $\mathbf B = \nabla\times\mathbf A$ and $\nabla\cdot\mathbf A = 0$.
(b) For an infinite straight wire along $z$ carrying $I$, show that
$A_z = -(\mu_0I/2\pi)\ln(s/s_0)$ reproduces $B_\phi = \mu_0I/(2\pi s)$, and comment
on the role of the arbitrary constant $s_0$.
(c) Explain why the vector potential, not $\mathbf B$, is the natural unknown in
many EM modelling codes and in the derivation of the induction equation.
(d) The scalar magnetic potential $\Phi_m$ satisfies $\mathbf B = -\mu_0\nabla\Phi_m$
where $\mathbf J = 0$. State one situation in geophysics where each potential is the
right choice, and why the scalar potential fails near a current-carrying coil.

---

**★10.** Units, dimensions and a design calculation.

(a) Show dimensionally that $\mathbf B = \mu_0(\mathbf H+\mathbf M)$ is consistent,
and state the SI unit of each term.
(b) Convert a field of 50 000 nT to $\mathbf H$ in A/m.
(c) A coil is required to produce 50 000 nT on axis at a distance of 1 m from its
centre. Compute the required magnetic moment.
(d) Using (c), compute the current needed for a single-turn 1 m² loop, for a
100-turn 1 m² coil, and for a 100-turn coil of 0.1 m radius. Comment on which
design is practical and what limits it.
(e) A coil is placed 0.5 m above a conducting ground. Explain qualitatively (no
calculation) why the field it produces is not the free-space field of (c)–(d), and
which lesson quantifies the discrepancy.
