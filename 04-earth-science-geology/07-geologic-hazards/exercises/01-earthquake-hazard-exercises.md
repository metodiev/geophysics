# Exercises — 04-07-01 Earthquake Hazard and Ground Motion

Attempt these **closed-book** before opening the
[solutions](./01-earthquake-hazard-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/earthquake_hazard_demo.py`](../code/earthquake_hazard_demo.py) require
you to run it and report its actual output.

---

## ★ Foundational

**★1.** A rupture is 40 km long and 15 km wide, with a mean slip of 1.5 m in
rock of shear modulus 30 GPa.

(a) Compute the seismic moment in N m and in dyn cm.
(b) Compute the moment magnitude with the dyn cm relation (2), with the
converted offset $-6.0333$ and with the usual $-6.07$. State the difference.
(c) Compute the radiated energy from the empirical relation
$\log_{10}E[\mathrm{J}] = 1.5M + 4.8$.
(d) State the energy ratio between this event and one 1.0 magnitude unit larger.

---

**★2.** A 30 m layer of soil with $v_S = 180$ m s⁻¹ and $\rho = 1700$ kg m⁻³
overlies rock with $v_S = 900$ m s⁻¹ and $\rho = 2600$ kg m⁻³.

(a) Compute the two impedances and their ratio.
(b) Compute the fundamental resonance frequency.
(c) State the peak amplification of the soil surface relative to the rock
outcrop motion, and justify the absence of a factor of 2 in your answer.
(d) State the amplification of the soil surface relative to the *incident wave*
in the rock, and say why this differs from (c).

---

**★3.** A body wave with $f = 2$ Hz travels through rock with $Q = 250$ and
$v = 3400$ m s⁻¹, from a reference distance of 10 km to 60 km.

(a) Compute the anelastic exponent $\pi f/(Qv)$.
(b) Compute the anelastic amplitude factor over the 50 km of path.
(c) Compute the total amplitude factor at 60 km for a body wave and for a
surface wave, relative to 10 km.
(d) State the ratio of the two answers to (c) and show that it equals
$\sqrt{6}$.

---

**★4.** An oscillator has damping ratio $\zeta = 0.05$.

(a) Compute its steady-state dynamic amplification at resonance.
(b) A design ground motion has a return period of 475 years. Compute the mean
annual rate and the probability of at least one exceedance in 50 years.
(c) Repeat (b) for a return period of 2475 years.
(d) State which of the numbers in (a) and (b) is computed and which is a model
input.

---

## ★★ Applied

**★★5.** Run the demo's sections 3 and 4.

(a) Report the numerical maximum of $|T|$ and its location, and the closed form
$Z_2/Z_1$, with the relative difference.
(b) Explain why the scan grid is deliberately offset from the exact
resonances.
(c) Report the value of $|T|$ at $f = 2f_0$ and explain it physically.
(d) Modify the half-space velocity to 1600 m s⁻¹, keeping everything else, and
report the new peak amplification and the new $f_0$. State which of the two
changed and why.

---

**★★6.** Run the demo's section 5.

(a) Report the relative difference between the numerically integrated
$\omega_0^2|x|_\mathrm{max}$ and $1/(2\zeta)$ for the three periods.
(b) Report the peak spectral acceleration and the ratio $\mathrm{Sa}/\mathrm{PGA}$
for the pulse.
(c) Explain why the ratio is about 2.4 rather than $1/(2\zeta) = 10$.
(d) Predict what happens to the peak $\mathrm{Sa}$ if $\zeta$ is halved, then
run it and compare. Explain why the change is much smaller than the factor of 2
that the steady-state formula would suggest.

---

**★★7.** A catalogue is fitted by $N(\ge M) = 10^{a - bM}$ with $a = 4$ and
$b = 1$ in a region, so that $N(\ge 4) = 1$ per year.

(a) Compute the annual rate of $M \ge 6$ and the probability of at least one
$M \ge 6$ in 50 years.
(b) Tabulate the rate in each 0.5-magnitude bin from 4.0 to 8.0.
(c) Assume the ground-motion amplitude at a fixed frequency scales as the
square root of the radiated energy, so $A \propto 10^{0.75M}$. Compute the
contribution of each bin to the sum $\sum_i N_i A_i$ and state which bin
dominates.
(d) Repeat (c) with $A \propto 10^{0.5M}$ and state whether the conclusion
changes.
(e) State which assumption in (c) is known to be wrong and in what direction.

---

## ★★★ Research-oriented

**★★★8.** A site is characterised as a single layer with $H = 30$ m,
$\rho_1 = 1700$ kg m⁻³, over rock with $v_S = 900$ m s⁻¹ and
$\rho_2 = 2600$ kg m⁻³. The measured $v_S$ of the layer is $180$ m s⁻¹
with an uncertainty of $\pm20$ per cent.

(a) Compute $|T|$ at $f = 2$ Hz for $v_S = 144$, $180$ and $216$ m s⁻¹,
updating the impedance ratio consistently.
(b) Express the three answers as a range and state, in one sentence, why a site
amplification quoted without a $v_S$ uncertainty is not a result.
(c) A building has a fixed period of 0.5 s. State which of the three site models
puts the building closest to a resonance with $f_0$, and compute the ratio of
$|T|$ at the building's frequency to $|T|$ at 2 Hz for that model.
(d) Discuss, in no more than five sentences, what a two-dimensional basin model
would add that this one-dimensional calculation cannot represent.

---

**★★★9.** The 1-D transfer function (7) assumes vertical incidence and a single
layer. A real sedimentary column has a velocity that increases with depth
because of compaction.

(a) Argue from $|T|_\mathrm{max} = Z_2/Z_1$ and $f_0 = v/(4H)$ why a smooth
velocity gradient gives a LOWER peak amplification and a BROADER resonance than
a sharp two-layer model with the same average velocity.
(b) A stacked column of ten layers each 3 m thick has $v_S$ increasing linearly
from 120 m s⁻¹ at the surface to 300 m s⁻¹ at 30 m. Compute the two-way
vertical travel time through the column and hence the fundamental frequency
defined as $f_0 = 1/(4\tau)$ where $\tau$ is the one-way travel time.
(c) Compare your answer in (b) with $v_\mathrm{avg}/(4H)$ using the arithmetic
mean velocity, and state the direction and size of the difference.
(d) Explain how a measured microtremor horizontal-to-vertical spectral ratio
could be used to test (b), and what it cannot test.
