# Exercises — 02-09-02 Radioactive Decay, Half-Life and Dating

Attempt these **closed-book** before opening the
[solutions](./02-radioactive-decay-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/radioactive_decay_demo.py`](../code/radioactive_decay_demo.py) require
you to run it and report its actual output. This is the module's mastery lesson:
**every problem that produces an age requires you to state the decay constant you
used and the compilation it came from.**

Tabulated half-lives used below (state them in your answer):
$T_{1/2}(^{87}\mathrm{Rb}) = 4.88 \times 10^{10}$ a;
$T_{1/2}(^{14}\mathrm{C}) = 5568$ a and 5730 a;
$T_{1/2}(^{238}\mathrm{U}) = 4.468 \times 10^9$ a;
$T_{1/2}(\mathrm{Cs\text{-}137}) = 30.08$ a;
$T_{1/2}(^{40}\mathrm{K}) = 1.248 \times 10^9$ a.

---

## ★ Foundational

**★1.** (a) Convert $T_{1/2} = 30.08$ a into $\lambda$ in s⁻¹ and in a⁻¹.
(b) Compute the mean life in years and state the ratio to the half-life.
(c) Check that $\lambda T_{1/2} = \ln 2$ in both unit systems.
(d) Compute the activity of $1.00 \times 10^{18}$ atoms of this nuclide.

---

**★2.** (a) Compute the mass of caesium-137 in a 1.000 GBq source
($M = 136.907$ g mol⁻¹), in mg.
(b) Express that activity in curie.
(c) Compute the activity remaining after 100.0 a.
(d) Explain in one sentence why a sealed-source inventory records activity and a
reference date rather than a mass.

---

**★3.** (a) Compute the specific activity of pure $^{238}$U in Bq g⁻¹.
(b) Compute the activity per kilogram of rock containing 1 ppm of natural
uranium, using the natural abundance of $^{238}$U.
(c) Compare (b) with the conversion factor of 12.4 Bq kg⁻¹ per ppm U used in
gamma-ray surveying and explain the difference.
(d) Explain why the *activity* ratio $^{235}$U/$^{238}$U in natural uranium is
not the abundance ratio.

---

## ★★ Applied

**★★4.** A two-member chain has $T_{1/2}$(parent) = 10.0 a,
$T_{1/2}$(daughter) = 1.00 a and $N_1(0) = 1.000$ with no daughter present.

(a) Compute the daughter population at $t = 5.00$ a from the Bateman solution.
(b) Compute it at $t = 1.00$ a.
(c) Verify your answers against the demo's table.
(d) Explain why the daughter population at 30 a is smaller than at 5 a, and what
limit it is approaching.

---

**★★5.** An Rb–Sr isochron of eight whole-rock samples gives a slope of
$4.965\,182 \times 10^{-3}$ with a standard error of $5.37 \times 10^{-5}$.

(a) Compute the age using $\lambda = 1.420\,384 \times 10^{-11}$ a⁻¹, and state
it in Ma.
(b) Compute the age using $\lambda = 1.39 \times 10^{-11}$ a⁻¹ and quantify the
change in Ma and in per cent.
(c) Write the age equation and confirm its unit consistency.
(d) State what the intercept of the isochron means and why fitting it matters.

---

**★★6.** A single Rb–Sr whole-rock analysis gives
$^{87}\mathrm{Rb}/^{86}\mathrm{Sr} = 1.60$ and $^{87}\mathrm{Sr}/^{86}\mathrm{Sr}
= 0.714\,274$.

(a) Compute the model age assuming an initial ratio of 0.7040.
(b) Compute it assuming 0.7100.
(c) State the range of years spanned by the two assumptions, and what the
isochron age of the same dataset gives (from the demo).
(d) Write the two-sentence statement with which a report must present (a) or
(b).

---

## ★★★ Research-oriented

**★★★7.** Radiocarbon.

(a) Compute the conventional radiocarbon age for $A/A_\mathrm{modern} = 0.25$
using the Libby half-life.
(b) Compute the "Cambridge" age for the same ratio.
(c) State the difference in years.
(d) Explain why neither is a calendar age, and what has to happen before one can
be quoted.

---

**★★★8.** Closure temperature. Dodson's equation is
$E_a/(RT_c) = \ln\left(A R T_c^2 D_0/(E_a a^2\dot T)\right)$ with
$A = 55$ (sphere), $a = 0.5$ mm, $E_a = 200$ kJ mol⁻¹,
$D_0 = 10^{-4}$ m² s⁻¹.

(a) Solve for $T_c$ at a cooling rate of 1 K Ma⁻¹, in °C.
(b) Solve for $T_c$ at 100 K Ma⁻¹.
(c) State the direction of the change and give the physical reason.
(d) A rock cools at 100 K Ma⁻¹ from 700 °C and contains a mineral with
$T_c = 340$ °C and another with $T_c = 500$ °C. Which mineral records the older
age, and by roughly what time difference if the cooling rate is constant?

---

**★★★9.** Run [`../code/radioactive_decay_demo.py`](../code/radioactive_decay_demo.py)
and report:

(a) the observed convergence order in the Euler and RK4 columns at 400 steps;
(b) the analytic value of $N(2T_{1/2})/N_0$ and the absolute difference from
0.25;
(c) the specific activities computed for 1 ppm U, 1 ppm Th and 1 % K, with the
widely quoted values for comparison;
(d) the activity ratio $^{235}$U/$^{238}$U and the abundance ratio;
(e) the recovered isochron age, its standard error and the relative error against
the true age;
(f) the measured $^{234}$Th/$^{238}$U activity ratio at one year and the analytic
prediction it is compared with;
(g) two sentences on which numbers in the output are computed and which are
tabulated.
