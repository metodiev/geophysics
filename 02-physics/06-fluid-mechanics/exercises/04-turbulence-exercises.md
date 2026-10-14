# Exercises — 02-06-04 Turbulence, Mixing and Eddy Diffusivity

Attempt these **closed-book** before opening the
[solutions](./04-turbulence-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to [`../code/turbulence_demo.py`](../code/turbulence_demo.py)
require you to run it and report its actual output. Take $\nu = 10^{-6}$
m² s⁻¹, $\kappa = 0.41$ unless told otherwise.

---

## ★ Foundational

**★1.** A flow has $\nu = 10^{-6}\ \mathrm{m^2\,s^{-1}}$ and a dissipation rate
$\varepsilon = 10^{-3}\ \mathrm{m^2\,s^{-3}}$.

(a) Compute $\eta$, $u_\eta$ and $\tau_\eta$ from equation (1).
(b) Compute the ratio $\eta/L$ if the forcing scale is $L = 1$ m.
(c) Repeat (a) for $\varepsilon = 1\ \mathrm{m^2\,s^{-3}}$, i.e. a thousandfold
increase, and state the scaling of each microscale in $\varepsilon$.
(d) Explain why $\eta$ depends on $\varepsilon$ at all, when the dissipation is
the *end* of the cascade.

---

**★2.** The dissipation rate is often estimated from the large scales as
$\varepsilon \sim U^3/L$.

(a) Compute $\varepsilon$ for $U = 1\ \mathrm{m\,s^{-1}}$, $L = 1$ m.
(b) With $\nu = 10^{-6}$ m² s⁻¹, compute $\eta$.
(c) Compute $L/\eta$ and compare with $Re^{3/4}$.
(d) Compute the number of grid points needed to resolve all scales in three
dimensions and state the implication for direct numerical simulation of a
geophysical flow.

---

**★3.** The log law is $u(z) = (u_*/\kappa)\ln(z/z_0)$ with
$u_* = 0.05\ \mathrm{m\,s^{-1}}$ and $z_0 = 10^{-3}$ m.

(a) Compute $u$ at $z = 1$, 10 and 100 m.
(b) Compute $\mathrm{d}u/\mathrm{d}z$ at each height.
(c) Compute $\nu_t = \kappa u_* z$ at each height.
(d) State why $\nu_t$ growing without bound is a warning rather than a result.

---

**★4.** For $\theta = 300$ K, $g = 9.81\ \mathrm{m\,s^{-2}}$ and a mean shear
$\partial u/\partial z = 0.01\ \mathrm{s^{-1}}$, compute $N^2$, $Ri$ and the
suppression factor $1/(1+Ri/0.25)$ for
$\partial\theta/\partial z = 0.001,\ 0.01,\ 0.05$ K m⁻¹.

---

## ★★ Applied

**★★5.** A stably stratified layer has $\partial\theta/\partial z = 0.01\
\mathrm{K\,m^{-1}}$ and $\theta = 300$ K.

(a) Compute $N^2$ and $N$.
(b) Compute the buoyancy period $2\pi/N$.
(c) A shear of $0.02\ \mathrm{s^{-1}}$ is imposed. Compute $Ri$ and state
whether the layer is expected to be turbulent.
(d) Compute the shear at which $Ri = 0.25$.

---

**★★6.** Run [`../code/turbulence_demo.py`](../code/turbulence_demo.py).

(a) Report $\eta$, $u_\eta$ and $\tau_\eta$ for the ocean surface layer.
(b) Report $\nu_t$ at $y = 1$ m and the ratio $\nu_t/\nu$ quoted by the demo.
(c) Report the value of the last log-law column and explain what it demonstrates
about whether the log law *tests* the mixing-length closure.
(d) Report $K$ for a neutral and for a strongly stratified layer with the same
shear, and state the ratio.

---

**★★7.** Mixing timescales follow $t \sim h^2/K$.

(a) For a 10 m lake with $K = 10^{-3}$ m² s⁻¹, compute $t$ in seconds and days.
(b) For a 50 m mixed layer with $K = 0.1$ m² s⁻¹, compute $t$.
(c) For the abyssal ocean with $h = 4000$ m and $K = 10^{-4}$ m² s⁻¹, compute
$t$ in years.
(d) Explain how the answers to (b) and (c) can differ by seven orders of
magnitude while both describe ocean water.

---

**★★8.** The gradient-diffusion closure is
$\overline{w'\theta'} = -K\,\partial\overline{\theta}/\partial z$.

(a) A tower measures an **upward** heat flux of magnitude $0.05\
\mathrm{K\,m\,s^{-1}}$ in the entrainment zone at the top of the convective
boundary layer, where the mean potential temperature *increases* upward with
gradient $+10^{-3}\ \mathrm{K\,m^{-1}}$. Compute the $K$ the closure requires.
(b) Explain why that value is physically unacceptable.
(c) Describe the actual mechanism producing the flux in that region.
(d) Name one model class that does not suffer from this problem, and state its
cost.

---

## ★★★ Research-oriented

**★★★9.** The turbulent kinetic energy budget in a stationary, homogeneous shear
flow is, schematically,
$\mathrm{d}E/\mathrm{d}t = P - \varepsilon$ with $P$ the shear production.

(a) Show that in equilibrium $\varepsilon \approx P$, and that with
$P \sim U^2(U/L)$ the scaling $\varepsilon \sim U^3/L$ follows.
(b) Use Kolmogorov's hypothesis that $\varepsilon$ is set by the large scales,
independent of $\nu$, to argue why $\eta$ must be a function of $\nu$ and
$\varepsilon$ alone.
(c) Show that the ratio of the largest to smallest time scale is
$\tau_L/\tau_\eta \sim Re^{1/2}$.
(d) A climate model uses grid cells of 100 km in the horizontal and 100 m in the
vertical, in an atmosphere with $\eta \sim 1$ mm. State, with numbers, what
fraction of the scale range is resolved and what must be parameterised.

---

**★★★10.** Turbulence in the stratified ocean is intermittent: active patches
occupy a fraction $f$ of the volume and carry (almost) all the flux.

(a) A microstructure survey finds active patches with
$\varepsilon = 10^{-7}\ \mathrm{m^2\,s^{-3}}$ over a fraction $f = 0.05$ of a
500 m water column, and $\varepsilon = 10^{-10}\ \mathrm{m^2\,s^{-3}}$ elsewhere.
Compute the volume-averaged dissipation rate.
(b) If a model assumes uniform dissipation and calibrates $K$ to reproduce the
column-integrated mixing, what error does it make in each of the two regions?
(c) Name two observational quantities a model of this kind should be tested
against, and state why a column-integrated test alone is insufficient.
(d) Explain, in three sentences, why "intermittency" is a statement about the
*spatial distribution of $\varepsilon$*, not about the mean value.
