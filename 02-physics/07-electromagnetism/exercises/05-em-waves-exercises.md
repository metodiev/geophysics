# Exercises — 02-07-05 Electromagnetic Waves, Impedance and Polarisation

Attempt these **closed-book** before opening the
[solutions](./05-em-waves-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/em_waves_demo.py`](../code/em_waves_demo.py)
require you to run it and report its actual output. **State your time convention in
every answer** — this module uses $e^{+i\omega t}$, and several standard references
use the opposite one.

---

## ★ Foundational

**★1.** A plane wave in vacuum has $\mathbf E = E_0\hat{\mathbf x}
e^{i(kz-\omega t)}$ with $E_0 = 10$ V/m and $f = 100$ MHz.

(a) Compute $k$ and $\lambda$.
(b) Write down $\mathbf B$ completely (magnitude, direction, phase).
(c) Verify $E/B = c$ and state the units of that ratio.
(d) State which of $\mathbf E$, $\mathbf B$, $\hat{\mathbf k}$ are parallel and
which are perpendicular, and what the right-handedness implies.

---

**★2.** The wave impedance.

(a) Compute $\eta = \sqrt{\mu_0/\varepsilon_0}$ and verify it equals $\mu_0c$.
(b) Compute $\eta$ for $\varepsilon_r = 1$, 4, 20 and 81, and state the trend.
(c) For a wave with $E_0 = 1$ V/m in each medium, compute $H_0$ (in A/m).
(d) Show dimensionally that $E/H$ is an ohm, and that $E/B$ is a speed.

---

**★3.** A uniform half-space of 100 Ω·m is sounded with magnetotellurics.

(a) Compute $\delta$ at $T = 1$, 10 and 100 s.
(b) Compute $|Z| = \sqrt{\omega\mu_0\rho}$ and the phase at each period.
(c) Compute $\rho_a = |Z|^2/(\omega\mu_0)$ and verify it returns 100 Ω·m.
(d) State what information a half-space sounding carries about depth, and why any
departure from a constant $\rho_a$ and a $45°$ phase is the *only* information.

---

**★4.** Normal-incidence reflection.

(a) Derive $r = (\eta_2-\eta_1)/(\eta_2+\eta_1)$ and show it becomes
$(\sqrt{\varepsilon_1}-\sqrt{\varepsilon_2})/(\sqrt{\varepsilon_1}+\sqrt{\varepsilon_2})$
for lossless dielectrics.
(b) Compute $r$, $R = |r|^2$ and the phase for $\varepsilon_r$ going from 4 to 25
(dry soil to saturated soil).
(c) Repeat for 4 to 1 (soil to air).
(d) Which of the two reflections dominates a GPR section, and why?

---

## ★★ Applied

**★5.** Polarisation. For $\mathbf E = (a_x\cos\omega t,\,
a_y\cos(\omega t+\phi))$ with $a_x = 1$ V/m, $a_y = 0.5$ V/m,
$\phi = 45°$:

(a) Compute all four Stokes parameters.
(b) Verify $S_1^2+S_2^2+S_3^2 = S_0^2$.
(c) Classify the polarisation state and compute the polarisation angle and the
ellipticity angle.
(d) State what additional information the polarisation of the *response* carries in
an MT survey, compared with the polarisation of the incident field.

---

**★6.** The two-layer MT response (use the demo's table for the 100 Ω·m / 5 km /
1000 Ω·m model).

(a) Report $\rho_a$ and $\phi$ at $T = 0.01$, 1, 10, 100 and 1000 s from the run.
(b) Compute the crossover period $T \approx \pi\mu_0d^2/\rho_1$ and compare with
where the transition actually begins.
(c) Explain why the phase *dips below* 45° in the transition and returns toward 45°
at long period.
(d) State why the phase is a more diagnostic quantity than $\rho_a$ for locating
the interface.

---

**★7.** Impedance in a lossy medium: $\sigma = 0.01$ S/m, $\varepsilon_r = 20$,
$\mu = \mu_0$.

(a) Compute $\eta = \sqrt{i\omega\mu/(\sigma+i\omega\varepsilon)}$ (magnitude and
phase) at $f = 10^{3}$, $8.99\times10^{6}$ and $10^{8}$ Hz.
(b) For each frequency compute $|\eta|$ and compare with the lossless
$\eta_0/\sqrt{\varepsilon_r}$.
(c) State which limit each frequency corresponds to and show that the phase passes
from 45° to 0° through 22.5° at the crossover.
(d) Explain why the *phase* of the impedance is a direct diagnostic of which
regime you are in.

---

**★8.** Source cancellation.

(a) Show algebraically why $Z = E/H$ is independent of the strength of a uniform
plane-wave source.
(b) Report what happens to $\rho_a$ if $|Z|$ is measured 10 % too high, and state
the sensitivity $\mathrm d\ln\rho_a/\mathrm d\ln|Z|$.
(c) Explain why a 10 % error in $\mathbf E$ and an *uncorrelated* 10 % error in
$\mathbf H$ are worse than a correlated 10 % error in both.
(d) Name two geophysical situations where the uniform-plane-wave assumption fails
systematically, and state the sign of the expected bias if you ignore it.

---

## ★★★ Research-oriented

**★9.** The impedance recursion.

(a) Derive the recursion
$Z_j = \eta_j(Z_{j+1}+\eta_j\tanh(\gamma_jh_j))/(\eta_j+Z_{j+1}\tanh(\gamma_jh_j))$
for a stack of layers over a half-space, stating the boundary conditions used at
each interface.
(b) For the 100 Ω·m / 5 km / 1000 Ω·m model at $T = 10$ s, compute
$\gamma_1h_1$, $\tanh(\gamma_1h_1)$, $\eta_1$, $\eta_2$ and the resulting surface
impedance. Compare with the demo's $\rho_a = 242.7250$ Ω·m and
$\phi = 25.5616°$.
(c) Explain what happens to the recursion when the first layer becomes very
resistive or very conductive, and in which limit it reduces to the half-space
result.
(d) Explain why this recursion, and not an analytic inversion, is the standard tool
for interpreting MT data, and what the non-uniqueness of the result implies.

---

**★10.** Three-dimensional structure and the impedance tensor.

(a) Write the tensor relation $E_i = Z_{ij}H_j$ and state what each of the four
elements is called.
(b) For a 1-D Earth, show that $Z_{xx} = Z_{yy} = 0$ and $Z_{xy} = -Z_{yx}$, and
explain physically why the response is independent of the polarisation of the
incident field.
(c) For a 2-D structure with strike along $y$, state which of the two modes
(E-polarisation and B-polarisation) is measured by which tensor elements, and why
they respond differently to the same conductivity structure.
(d) Define the tipper and the skew, state what each diagnoses, and explain why a
*vertical* magnetic field measurement adds information that the four-tensor
elements cannot.
