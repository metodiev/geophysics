# Exercises — 02-04-07 Viscoelasticity, Creep and Anelastic Relaxation

Attempt these **closed-book** before opening the
[solutions](./07-viscoelasticity-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/viscoelasticity_demo.py`](../code/viscoelasticity_demo.py) require you
to run it and report its actual output.

---

## ★ Foundational

**★1.** For a Maxwell element with $\mu = 45$ GPa and $\eta = 3\times10^{19}$ Pa s:

(a) Compute the relaxation time $\tau$ in seconds and in years.
(b) Write the creep strain $\gamma(t)$ under a constant shear stress
$\sigma_0 = 2$ MPa, and give the numerical values of the elastic and viscous
terms at $t = \tau$.
(c) Write the stress relaxation $\sigma(t)$ under $\gamma_0 = 10^{-4}$, and give
$\sigma$ at $t = 0$, $\tau$ and $3\tau$.
(d) State at which times the element is a solid and at which it is a fluid.

---

**★2.** For a Kelvin–Voigt element with $\mu = 45$ GPa and $\eta = 3\times10^{19}$
Pa s:

(a) Write $\gamma(t)$ for a step stress of 2 MPa.
(b) Compute $\gamma(\tau)$ and $\gamma(3\tau)$, and compare with the
Maxwell element of ★1.
(c) Show that the long-time limit is finite and give it.
(d) Compute $Q(f)$ at 1 Hz, 10 Hz and 100 Hz for this element and state why the
result rules it out as a rock model.

---

**★3.** Starting from equation (13) of the lesson, show that the standard linear
solid's $Q = G'/G''$ is minimum at $x = \omega\tau_\sigma = 1/\sqrt{1+\Delta}$ and
that the minimum value is $Q_{\min} = 2\sqrt{1+\Delta}/\Delta$.

(a) Differentiate and find the stationary point.
(b) Evaluate $Q$ there.
(c) Show that the minimum is a minimum (not a maximum).
(d) For $Q_{\min} = 30$, solve for $\Delta$ and compute the corresponding
unrelaxed-to-relaxed modulus ratio.

---

**★4.** Show that the three definitions of $Q$ in equation (1) agree to first
order in $1/Q$.

(a) For a complex modulus $M = M'(1+i/Q)$ compute the energy dissipated per cycle
under harmonic strain, and hence $2\pi E_{\text{stored}}/\Delta E$.
(b) Compute the phase lag $\delta$ satisfying $\tan\delta = M''/M'$ and show
$Q = 1/\tan\delta \approx 1/\delta$ for small $\delta$.
(c) Estimate the fractional error of the approximation at $Q = 5$.
(d) State why the ambiguity matters for a fluid-like material with $Q < 1$.

---

## ★★ Applied

**★★5.** Run section 1 of the demo.

(a) Report $\tau$, the maximum absolute difference between numerical and analytic
relaxation over three relaxation times, and the relative size of that residual.
(b) Report the viscosity recovered from the steady creep rate and compare with
the input.
(c) Derive the creep expression used, and state the two parameters that can be
read off a creep curve.
(d) Explain why this numerical test cannot detect a modelling error (as opposed
to an integration error).

---

**★★6.** Run section 3 of the demo.

(a) Report the relaxed and unrelaxed moduli, the contrast $\Delta$, and
$V(f_0)$.
(b) Verify equation (16) of the lesson against the tabulated $Q$ values at 1, 5,
10, 50 and 100 Hz.
(c) Report the total velocity difference between 1 Hz and 100 Hz and compare with
the full relaxed-to-unrelaxed contrast $\sqrt{1+\Delta}-1$.
(d) Report the largest difference between the measured $V/V_0-1$ and the
nearly-constant-$Q$ prediction, and state the value of $\ln(f/f_0)$ there.

---

**★★7.** A rock has $Q = 200$, independent of frequency, and $v_p = 4000$ m s⁻¹
at 10 Hz.

(a) Compute the attenuation coefficient $\alpha$ at 10 Hz and at 100 Hz,
in m⁻¹ and in dB per km ($20\log_{10}$ per amplitude ratio).
(b) Compute the amplitude decay in dB over 1 km at each frequency.
(c) Compute the velocity at 1 Hz and at 100 Hz using the nearly-constant-$Q$
relation, and state the regime condition you are relying on.
(d) A reflection loses 20 dB relative to a reference; express that as a $Q$
equivalent for a 1 km path at 10 Hz.

---

**★★8.** Run section 4 of the demo, then answer:

(a) Report $\tau$ for $\eta = 10^{21}$ Pa s and $\mu = 70$ GPa, and $\omega\tau$
for the three listed phenomena.
(b) Compute the period at which $\omega\tau = 1$ and describe what a deformation
experiment at that timescale would look like.
(c) A region of the mantle has $\eta = 10^{20}$ Pa s instead. Recompute $\tau$ and
the three $\omega\tau$ values and state which regimes change.
(d) Explain why the Maxwell model's $Q = \omega\tau$ at 30 Hz
($\approx2.7\times10^{12}$) is inconsistent with seismic observations, and what
that implies about using creep-derived viscosity as a seismic-attenuation model.

---

## ★★★ Research-oriented

**★★★9.** Build a superposition model.

(a) Write the complex modulus of $N$ standard linear solids in parallel, each with
its own $Q_{\min,k}$ and $f_{\min,k}$, and show that the total $G'$ and $G''$ are
the sums of the individual contributions.
(b) Choose three SLS elements with $Q_{\min} = 30$ at $f_{\min} = 1$, 10 and
100 Hz and equal weights, compute $Q(f)$ at $f = 0.1, 1, 10, 100, 1000$ Hz, and
compare the flatness with a single SLS.
(c) State what determines the quality of the flatness, and identify the
mathematical price paid over a fixed band (how many parameters are needed for what
accuracy).
(d) Verify your numerical work with a script you write yourself (standard library
only) and report the measured $Q$ values.

---

**★★★10.** Attenuation mechanisms and their signatures.

(a) For each of the following, state whether it is intrinsic or apparent, and give
the frequency dependence you expect: (i) grain-boundary sliding, (ii) squirt flow
between cracks and pores, (iii) thin-layer interference, (iv) scattering by
random heterogeneities of size comparable with the wavelength, (v) thermoelastic
relaxation.
(b) For one of them, derive or justify the frequency dependence you claimed, and
state the microscopic parameter that sets the peak attenuation frequency.
(c) Design a laboratory experiment that would separate intrinsic from apparent
attenuation for a layered sample, stating the sample dimensions, frequencies and
the observable you would compare with the theory.
(d) State what cannot be determined from a single-frequency measurement and why.

Report measured values only if you verify them numerically, and state clearly
which of your claims are qualitative (mechanism ordering) rather than
quantitative.
