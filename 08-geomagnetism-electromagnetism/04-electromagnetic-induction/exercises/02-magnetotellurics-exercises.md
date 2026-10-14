# Exercises — 08-04-02 Magnetotellurics: Impedance Tensor, Apparent Resistivity, Phase

Attempt these before reading the
[solutions](./02-magnetotellurics-solutions.md). The lesson is
[02 Magnetotellurics](../02-magnetotellurics.md). All models are **SYNTHETIC**.

## ★ Foundational

**★1.** Compute $Z$ for a uniform $50\ \Omega$m half-space at $T = 20$ s:
$\left|Z\right| = \sqrt{\omega\mu_0\rho}$. Then compute $\rho_a$ and the phase.

**★2.** For a two-layer model with $\rho_1 = 50\ \Omega$m over a
$500\ \Omega$m half-space, state whether the phase at short periods is above or
below $45^\circ$, and give the one-sentence rule that decides it.

**★3.** A tensor (in $10^{-3}\ \Omega$) has $Z_{xx} = 3+2i$,
$Z_{xy} = 40+30i$, $Z_{yx} = -20-15i$, $Z_{yy} = -1-1i$. Compute the skew
$\left|Z_{xx}+Z_{yy}\right|/\left|Z_{xy}-Z_{yx}\right|$ and state the
dimensionality it indicates.

## ★★ Applied

**★★4.** A measured impedance is multiplied by $s = 2.5$ by a near-surface
galvanic body. Compute the new apparent resistivity as a multiple of the old, and
state what happens to the phase.

**★★5.** For the demonstration's synthetic 2-D tensor the invariants are
$\left|Z_{xy}+Z_{yx}\right| = 0.005845$ and
$\left|Z_{xy}-Z_{yx}\right| = 0.026904$. At a rotation of $45^\circ$ the table
gives $\left|Z_{xy}+Z_{yx}\right| = 0.000000$. Explain why the invariant is
allowed to be zero at one rotation while remaining constant, and state what is
happening to $\left|Z_{xy}\right|$ and $\left|Z_{yx}\right|$ at that angle.

**★★6.** A 2-D tensor is rotated by $40^\circ$ from strike. State the rotation
angle that minimises $\left|Z_{xx}\right|^{2}+\left|Z_{yy}\right|^{2}$ and the
ambiguity in the answer.

## ★★★ Research-oriented

**★★★7.** Design a field experiment to determine whether an MT site is 1-D, 2-D
or 3-D. State which quantities you would measure, over what period range, with
what array geometry, and the decision rule for each conclusion. Include the one
case in which the measurement will mislead you.

**★★★8.** The phase is invariant under a static shift while $\rho_a$ is not.
Show algebraically that this is a consequence of $s$ being real and positive, and
state what happens if $s$ is complex (a galvanic distortion with a phase).
