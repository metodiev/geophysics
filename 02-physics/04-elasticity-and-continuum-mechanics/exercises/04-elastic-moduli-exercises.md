# Exercises — 02-04-04 Young's Modulus, Poisson's Ratio and the Elastic Constants

Attempt these **closed-book** before opening the
[solutions](./04-elastic-moduli-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/elastic_moduli_demo.py`](../code/elastic_moduli_demo.py) require you to
run it and report its actual output.

---

## ★ Foundational

**★1.** A rock has $K = 40$ GPa and $\mu = 25$ GPa.

(a) Compute $\lambda$, $M$, $E$ and $\nu$.
(b) For $\rho = 2600\ \mathrm{kg\,m^{-3}}$, compute $v_p$ and $v_s$.
(c) Compute $v_p/v_s$ by three different formulas and verify agreement.
(d) State whether this material is closer to a Poisson solid or to a
high-$\nu$ rock.

---

**★2.** A material has $\nu = 0.30$ and $E = 50$ GPa.

(a) Compute $\mu$ and $K$.
(b) State why the $K$ computation is more sensitive to an error in $\nu$ than the
$\mu$ computation, and quantify it by recomputing $K$ for $\nu = 0.31$.
(c) Compute $v_p/v_s$.
(d) State the value of $\nu$ at which $v_p/v_s = \sqrt2$ and explain the physical
meaning of that point.

---

**★3.** Prove that $v_p > v_s$ for any stable isotropic elastic solid.

(a) Write $v_p^2-v_s^2$ in terms of $\lambda$, $\mu$ and $\rho$.
(b) Express it in terms of $K$ and $\mu$ and show it is positive.
(c) State the smallest possible value of the ratio and the condition for it.
(d) Repeat (c) under the additional assumption $\lambda\ge0$ and explain the
difference.

---

**★4.** A saturated sandstone has $v_p = 3300$ m s⁻¹, $v_s = 1900$ m s⁻¹ and
$\rho = 2250\ \mathrm{kg\,m^{-3}}$.

(a) Compute $M$, $\mu$, $K$ and $\nu$.
(b) Compute $E$.
(c) State which of the six constants is determined *directly* by the
measurement and which are derived.
(d) Compute the water-saturated $v_s$ you would predict if the porosity were
pore-filled with a fluid of density 1000 kg m⁻³ and the dry density were
2100 kg m⁻³, given $\mu$ unchanged.

---

## ★★ Applied

**★★5.** Run the demo and use its granite-like model.

(a) Report all six constants and both velocities.
(b) Report the uniaxial-test verification values and state which equations are
being tested.
(c) Report $v_p/v_s$ at $\nu = -0.9$, $0$, $0.25$ and $0.49$, and check each
against the two bounds.
(d) Compute the fractional error in $v_p$ that would result from using $K$ instead
of $M$ in $v_p = \sqrt{M/\rho}$, for this model.

---

**★★6.** A gas sand has $K_{\text{dry}} = 8$ GPa, $\mu = 6$ GPa,
$K_{\min} = 36$ GPa, $\phi = 0.25$, $\rho_{\min} = 2650\ \mathrm{kg\,m^{-3}}$,
and the pore fluid is either gas ($K_g = 0.02$ GPa, $\rho_g = 100$ kg m⁻³) or
water ($K_w = 2.2$ GPa, $\rho_w = 1000$ kg m⁻³).

(a) Compute $K_{\text{sat}}$, $\rho$, $v_p$ and $v_s$ in the two end-member cases.
(b) Compute the fractional changes in $v_p$ and $v_s$ between them.
(c) Compute the normal-incidence reflection coefficient against an overlying shale
of $Z = 6.0$ MRayl in both cases, and state the polarity difference.
(d) Explain why a time-lapse seismic survey looking for a gas-to-water
replacement would prefer to monitor the $v_s$ change over the $v_p$ change in a
uniform-saturation reservoir, and why that preference reverses for patchy
saturation.

---

**★★7.** Run the demo's ratio table.

(a) Report $v_p/v_s$ at $\nu = -0.5$, $-0.2$, $0$, $0.2$, $0.4$ and $0.49$.
(b) Verify each against $\sqrt{2(1-\nu)/(1-2\nu)}$.
(c) State the smallest value in the table and compare with $2/\sqrt3$.
(d) Explain in words why a material with a negative Poisson's ratio is physically
possible and what its microstructure must look like.

---

**★★8.** A rock-physics model predicts $v_p$ from $K$ and $\mu$ with 3 per cent
uncertainty on $K$, 2 per cent on $\mu$ and 1 per cent on $\rho$.

(a) Propagate the uncertainties to $v_p$ and $v_s$, assuming they are independent.
(b) State which input dominates each velocity error.
(c) Compute the uncertainty in the inferred $\nu$.
(d) Comment on the practical significance for a $v_p/v_s$ lithology
discrimination: how well must $v_p/v_s$ be known to separate two lithologies whose
ratios differ by 0.05?

---

## ★★★ Research-oriented

**★★★9.** Stress sensitivity of the elastic moduli.

(a) A simple model for a cracked rock has
$\mu(P) = \mu_0[1 - a\exp(-P/P^*)]$ with $a$ the crack density and $P^*$ a
characteristic closure pressure. Fit this qualitatively to the observation that
$v_s$ rises by 10 per cent between 5 and 40 MPa confining pressure; state the
values of $a$ and $P^*$ you choose and justify them.
(b) Compute $v_s$ at 5, 10, 20 and 40 MPa for $\mu_0 = 30$ GPa,
$\rho = 2600\ \mathrm{kg\,m^{-3}}$.
(c) Compute the implied depth dependence for a lithostatic gradient of
26.5 MPa km⁻¹, and state whether the modelled $v_s$ increase with depth is
consistent with typical log observations (state your source for the observation).
(d) Explain why this pressure sensitivity makes the comparison of laboratory and
field velocities a problem, and how the comparison is normally made.

---

**★★★10.** Gassmann's relation does not predict the frequency dependence of the
moduli.

(a) State the two limiting cases (Gassmann low frequency and the high-frequency
limit in which the pore fluid does not equilibrate) and explain what sets the
crossover frequency.
(b) Estimate the crossover frequency for a rock with permeability
$k = 100$ mD, porosity 0.2, fluid viscosity $10^{-3}$ Pa s and bulk modulus
2.2 GPa, using a diffusion length argument
$\ell = \sqrt{D/\omega}$ with $D \approx kK_f/(\eta\phi)$; state your assumptions.
(c) Compare the crossover with the seismic band (1–100 Hz) and with ultrasonic
laboratory frequencies (0.1–5 MHz), and state which limit each measurement
samples.
(d) Explain the consequence for interpreting a laboratory $v_p$ in terms of a
field $v_p$, and state what additional measurement resolves the ambiguity.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
