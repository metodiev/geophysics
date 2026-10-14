# Exercises — 02-07-06 EM Fields in Conductors: Skin Depth and Diffusion

Attempt these **closed-book** before opening the
[solutions](./06-em-in-conductors-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/em_in_conductors_demo.py`](../code/em_in_conductors_demo.py) require you
to run it and report its actual output. Resistivities are **nominal** unless a
question states otherwise; say so when you use one.

---

## ★ Foundational

**★1.** For a uniform half-space of 100 Ω·m:

(a) Compute the skin depth at $f = 0.01$, 1 and 100 Hz.
(b) Compute $\delta\sqrt f$ for each and state what is constant.
(c) Compute the ratio $\delta(f/100)/\delta(f)$ and compare with $1/\sqrt{100}$.
(d) State in words why a decade of frequency buys only a factor 3.16 in depth, and
what a survey designer must do about it.

---

**★2.** Derive $\delta = \sqrt{2/(\mu\sigma\omega)}$ from
$\nabla^2\mathbf E = i\omega\mu\sigma\mathbf E$.

(a) Show $k = \sqrt{-i\omega\mu\sigma}$ and evaluate $\sqrt{-i}$.
(b) Hence write $\mathbf E(z,t)$ for a wave decaying in $+z$ and identify
$\delta$.
(c) Check the dimensions of $\delta$ from $\sqrt{2/(\mu\sigma\omega)}$ explicitly,
showing that $\mathrm{H\,S = s}$.
(d) Explain the difference between $\delta$ and the nominal wavelength
$2\pi\delta$, and why the latter should not be called a wavelength.

---

**★3.** The $\rho T$ form.

(a) Show $\delta = \sqrt{\rho T/(\pi\mu_0)}$ and evaluate the constant.
(b) Compute $\delta$ at $T = 1$ s for $\rho = 10$, 100 and 1000 Ω·m.
(c) Invert to find the period needed for $\delta = 1$ km, 10 km and 100 km at
$\rho = 100$ Ω·m.
(d) State the units in which $\rho$ and $T$ must be expressed, and what goes wrong
if $T$ is given in milliseconds.

---

**★4.** Phase.

(a) Show that the phase lag is $z/\delta$ radians at depth $z$.
(b) At what depth does the lag reach $180°$ for $\rho = 100$ Ω·m and $T = 10$ s?
(c) Express that depth in skin depths.
(d) State why the equality of decay exponent and phase lag is the signature of a
diffusion equation rather than a wave equation.

---

## ★★ Applied

**★5.** Sounding depth and its conventions. For $\rho = 100$ Ω·m:

(a) Compute the period required for $\delta = 10$ km.
(b) Recompute for a definition of sounding depth as $\delta/\sqrt2$, and for
$0.5\delta$.
(c) Express the three answers as a range and state the practical consequence for
choosing a recording bandwidth.
(d) Explain why the convention must be stated whenever a depth is attributed to a
period.

---

**★6.** Attenuation in the lossy-dielectric regime. For $\sigma = 0.01$ S/m,
$\varepsilon_r = 20$, $\mu = \mu_0$:

(a) Compute the crossover frequency $f_c = \sigma/(2\pi\varepsilon)$.
(b) At $f = 10^{6}$, $10^{7}$ and $10^{8}$ Hz compute the exact
$\alpha = \omega\sqrt{\mu\varepsilon/2}\left[\sqrt{1+(\sigma/\omega\varepsilon)^2}-1\right]^{1/2}$,
the low-loss approximation $\alpha_{\text{LL}} = (\sigma/2)\sqrt{\mu/\varepsilon}$,
and $1/\delta$.
(c) Convert the exact $\alpha$ at $10^{8}$ Hz to dB/m and compute the two-way loss
to a target at 5 m.
(d) State which approximation is acceptable in which frequency band, and what goes
wrong if you use the skin-depth formula at GPR frequencies.

---

**★7.** Depth windows. Compute $\delta$ for:

(a) $\rho = 0.25$ Ω·m at $T = 1$ s (sea water, nominal);
(b) $\rho = 1000$ Ω·m at $T = 1$ s and at $T = 1000$ s (crustal basement);
(c) $\rho = 10$ Ω·m at $T = 1$ day (mantle, nominal);
(d) $\rho = 100$ Ω·m at $T = 1$ yr (mantle, nominal) and state whether the answer
is physically sensible — and if not, why not.

---

**★8.** The time-domain face.

(a) Compute the magnetic diffusion time $\mu_0\sigma L^2$ for $L = 10$ km in
100 Ω·m rock.
(b) Compute the period for which $\delta = 10$ km in the same rock.
(c) Compare the two and explain why they are of the same order but not equal.
(d) State which is the right number to quote for (i) how long a crustal field
perturbation takes to relax, and (ii) what period an MT survey needs to sense that
depth.

---

## ★★★ Research-oriented

**★9.** Exact versus approximate propagation.

(a) Derive $\alpha$ and $\beta$ from $k = \beta - i\alpha$ and
$k^2 = \omega^2\mu\varepsilon - i\omega\mu\sigma$.
(b) Show that $\alpha/\beta = \sqrt{(\sqrt{1+x^2}-1)/(\sqrt{1+x^2}+1)}$ with
$x = \sigma/\omega\varepsilon$, and evaluate it at $x\to0$, $x = 1$ and
$x\to\infty$.
(c) Derive the phase velocity $v = \omega/\beta$ as a fraction of the lossless
$c/\sqrt{\varepsilon_r}$ and show it falls monotonically from 1 to 0 as $x$ grows,
quoting its value at $x = 1$.
(d) Show that $\alpha$ and $\beta$ both tend to $1/\delta$ when
$x\gg1$, and that both tend to the lossless values when $x\ll1$. Explain why the
*cross-over* between the two regimes happens at $x\sim1$ for the amplitude but that
the *phase velocity* is already 9 % below the lossless value there.

---

**★10.** When the half-space model fails: the conductance effect.

Consider a conducting sheet of resistivity 10 Ω·m and thickness 100 m over a
basement of $10^{8}$ Ω·m (a nominal, extreme contrast chosen to isolate the
effect).

(a) Compute the sheet's conductance $S = h/\rho$ and its skin depth at
$T = 1$, 100 and $10^{4}$ s.
(b) Show that the half-space formula predicts a penetration depth hundreds of times
the layer thickness, and state why that is a contradiction.
(c) Show analytically that a thin sheet of conductance $S$ over a perfect insulator
has impedance $Z = 1/S$ (real), and hence
$\rho_a = 1/(\omega\mu_0S^2)$, which *grows* with period and has zero phase.
(d) Check (c) numerically against the demo's impedance recursion for $T = 1$,
100 and $10^4$ s, tabulating $\rho_a$, the phase, and $1/(\omega\mu_0S^2)$. State
the criterion for the sheet to control the response rather than the basement, and
what that implies for interpreting a long-period sounding over a sedimentary basin.
