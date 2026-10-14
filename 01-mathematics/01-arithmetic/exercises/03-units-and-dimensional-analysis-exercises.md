# Exercises — 01-01-03 Units, SI Conventions and Dimensional Analysis

Attempt these **closed-book**, on paper, before opening the
[solutions](./03-units-and-dimensional-analysis-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

For every numerical answer, do the **magnitude check** as well as the algebra:
state whether the result sits where the anchor table of lesson 02 says it should.
The demonstration
[`code/units_and_dimensions.py`](../code/units_and_dimensions.py) recomputes the
worked examples in the lesson.

---

## ★ Foundational

**★1.** Give the SI base-unit expansion of each derived unit. Derive each from
its defining relation rather than recalling it.

(a) newton (N) — force
(b) pascal (Pa) — pressure and stress
(c) joule (J) — energy and work
(d) watt (W) — power

Then state which two of these four have **identical** dimensions, and explain the
physical identity that makes it so rather than a naming coincidence.

---

**★2.** Convert each value to SI base units and perform a magnitude check
against a plausible geophysical range.

(a) $250\ \mathrm{mGal}$ to $\mathrm{m\,s^{-2}}$
   (use $1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$)
(b) $45\,000\ \mathrm{nT}$ to tesla
(c) $3.2\ \mathrm{g\,cm^{-3}}$ to $\mathrm{kg\,m^{-3}}$
(d) $65\ \mathrm{mW\,m^{-2}}$ to $\mathrm{W\,m^{-2}}$

For each, say in one sentence whether the result is plausible for the quantity it
describes and why.

---

**★3.** The deep-water phase speed of a surface gravity wave is
$v = \sqrt{g\lambda/(2\pi)}$, where $\lambda$ is the wavelength.

(a) Show **dimensionally** that the right-hand side has the dimensions of a
   velocity, and note which factor is dimensionless.
(b) Evaluate the speed for $\lambda = 200$ m using
   $g = 9.81\ \mathrm{m\,s^{-2}}$, and comment on whether the value is realistic
   for ocean swell.
(c) State what dimensional analysis alone could **not** have told you about this
   formula, and where the missing information comes from.

---

## ★★ Applied

**★★4.** The quality factor is defined as $Q = 2\pi E_{\text{stored}} /
E_{\text{dissipated}}$, and seismic amplitudes decay as
$A = A_0\exp(-\pi f x/(Qv))$.

(a) Show that $Q$ is dimensionless.
(b) Show that the exponent $\pi f x/(Qv)$ is dimensionless.
(c) Rewrite the exponent in terms of wavelength $\lambda = v/f$, and state the
   physical insight that follows about how attenuation depends on distance.
(d) Compute the amplitude fraction lost per wavelength for $Q = 100$ and for
   $Q = 1000$. Explain why seismic waves propagate many wavelengths before
   becoming unrecognisable.

---

**★★5.** Gravitational potential is $V = -GM/r$.

(a) Show that $[V] = \mathrm{L^{2}\,T^{-2}}$.
(b) Using $g = -\nabla V$, show that $[g] = \mathrm{L\,T^{-2}}$.
(c) Show that energy per unit mass has the same dimensions as $V$, and state the
   physical meaning this establishes.
(d) Give the geodetic use of this result: how does a potential difference in
   $\mathrm{m^{2}\,s^{-2}}$ convert to an equivalent height, and what is that
   height called?

---

**★★6.** In a magnetotelluric sounding, the impedance is $Z = E/H$, with $E$ in
$\mathrm{V\,m^{-1}}$ and $H$ in $\mathrm{A\,m^{-1}}$.

(a) Expand the volt in base units and hence write
   $[\mathrm{V\,m^{-1}}]$.
(b) Derive $[Z]$ in base units and identify the resulting combination with the
   ohm.
(c) Show dimensionally that the apparent resistivity
   $\rho_a = |Z|^{2}/(\mu_0\omega)$ has units of $\Omega\cdot\mathrm{m}$.
(d) In one sentence, state which quantity (dimensionless contrast, or ratio of a
   driving field to a resulting flow) makes the identification physically
   meaningful as well as dimensional.

---

**★★7.** For post-glacial rebound the relaxation timescale is often written in
one of two forms:
group 1, $\eta/(\rho g L)$; group 2, $\eta/(\rho g L^{2})$.

(a) Show that group 1 has dimensions of time and that group 2 does **not**; state
   the dimensions group 2 actually has.
(b) Using $\eta = 10^{21}\ \mathrm{Pa\,s}$, $\rho = 3300\ \mathrm{kg\,m^{-3}}$
   and $g = 10\ \mathrm{m\,s^{-2}}$, evaluate group 1 (in seconds and years) for
   $L = 1$ km, $L = 100$ km and $L = 2000$ km.
(c) Which row is the relevant one for rebound beneath the Fennoscandian and
   Laurentide ice sheets? Compare your value with observed relaxation times of
   order $10^{3}$–$10^{4}$ yr for the upper mantle.
(d) State how $\tau$ depends on $L$ here, and explain why a single-viscosity
   estimate is a bounding calculation rather than a prediction.

---

**★★8.** A heat-flow probe measures $q = 72\ \mathrm{mW\,m^{-2}}$ and a core
sample gives $k = 2.5\ \mathrm{W\,m^{-1}\,K^{-1}}$.

(a) Use Fourier's law $q = k\,\mathrm{d}T/\mathrm{d}z$ to compute the geothermal
   gradient, in $\mathrm{K\,m^{-1}}$ and $\mathrm{K\,km^{-1}}$.
(b) Show dimensionally that the ratio has units of $\mathrm{K\,m^{-1}}$.
(c) Compare with a crustal anchor of ~25 K/km and state whether the result is
   consistent.
(d) Explain why this calculation is an **inverse** problem — which quantities are
   measured, which is inferred, and why the gradient cannot be measured directly
   below the shallowest borehole.

---

## ★★★ Research-oriented

**★★★9.** **Buckingham Pi for mantle convection.** The quantities describing
convection in a layer are: depth $L$, temperature contrast $\Delta T$, gravity
$g$, density $\rho$, thermal expansivity $\alpha$, thermal diffusivity $\kappa$,
dynamic viscosity $\eta$, specific heat capacity $c_p$, and heat flux $q$.

(a) Assign dimensions to all nine quantities and count the independent
   dimensionless groups (four base dimensions: M, L, T, $\Theta$).
(b) Form the Rayleigh number $\mathrm{Ra}$ and the Nusselt number $\mathrm{Nu}$.
   State what each compares physically.
(c) Explain why $\mathrm{Ra}$ is better described as a ratio of *timescales* than
   of forces.
(d) With $\mathrm{Ra} \approx 1.78\times10^{7}$ from the lesson and
   $\mathrm{Ra}_c \approx 10^{3}$, estimate $\mathrm{Nu}$ for
   $\beta = 1/3$. State the caveat about $\beta$ and why you must cite the
   primary literature before using a specific exponent.
(e) Show that a factor-of-10 error in $\mathrm{Ra}$ changes $\mathrm{Nu}$ by only
   about 2.15, and explain why this makes the qualitative conclusion robust while
   the precise value is not.
(f) State at least three limitations of the estimate, and write the one-sentence
   defensible scientific conclusion it supports.

---

**★★★10.** **Unit forensics on gravity gradients.** Three papers report the same
regional gravity gradient in three different units: Paper A, $2.4$ Eötvös;
Paper B, $2.4\times10^{-9}\ \mathrm{s^{-2}}$; Paper C,
$24\ \mathrm{mGal\,km^{-1}}$.

(a) Give the dimensions of the Eötvös
   ($1\ \mathrm{E} = 10^{-9}\ \mathrm{s^{-2}}$), of $\mathrm{s^{-2}}$, and of
   $\mathrm{mGal\,km^{-1}}$. Show that all three are the same quantity, and
   explain why that is exactly what makes the error hard to spot.
(b) Working from first principles, derive the conversion
   $1\ \mathrm{mGal\,km^{-1}} = 10\ \acute{\mathrm{E}}$ (and
   $1\ \acute{\mathrm{E}} = 0.1\ \mathrm{mGal\,km^{-1}}$).
(c) Convert Paper C's value to Eötvös. Are Papers A and B consistent with each
   other? By what factor does Paper C differ from them?
(d) Note the trap: a superficial comparison of the leading numbers ($24$ vs
   $2.4$) finds only one factor of ten. Identify the **second** factor and where
   it comes from.
(e) Propose the most likely origin of the discrepancy, and write a two-sentence
   referee's comment requesting the fix. State why a dimensional check alone
   could never have caught this error.

---

## Extension ideas

- Build a one-page *unit card* for your own subfield: list every non-SI unit you
  use (mGal, Eötvös, nT, Gal, mK/km, W/m², Pa·s), its SI expansion and dimensions,
  and one anchor value for each.
- Take any three formulas from a paper you are reading and dimensional-check
  them. Record which ones fail and what that tells you.
- Rewrite ★3 as code that takes $g$ and $\lambda$ and returns $v$, then add an
  assertion that catches a unit error (for example $\lambda$ supplied in km
  without conversion).
