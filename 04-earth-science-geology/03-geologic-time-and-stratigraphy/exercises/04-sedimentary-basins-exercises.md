# Exercises — 04-03-04 Sedimentary Basins: Formation, Fill and Subsidence

Attempt these **closed-book** before opening the
[solutions](./04-sedimentary-basins-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/04-basins_subsidence_demo.py`](../code/04-basins_subsidence_demo.py)
require you to run it and report its actual output.

**Parameters.** Unless a problem states otherwise use $\rho_m = 3300$,
$\rho_c = 2800$, $\rho_w = 1030$, $\rho_s = 2500$ kg m$^{-3}$,
$t_c = 35$ km, $a = 125$ km, $T_m = 1330$ °C,
$\alpha = 3.28 \times 10^{-5}$ K$^{-1}$ and
$\kappa = 10^{-6}$ m² s$^{-1}$. These are **commonly quoted values**, labelled
TYPICAL in the demo; a real study replaces each with a province-specific value
and a reference.

---

## ★ Foundational

**★1.** Compute the instantaneous subsidence of a uniformly stretched lithosphere
for $\beta = 2$ with a water load.

(a) Evaluate $\rho_m - \rho_c$ and $\rho_m - \rho_w$.
(b) Compute the density factor $(\rho_m - \rho_c)/(\rho_m - \rho_w)$.
(c) Compute $S_i$ from $S_i = t_c(1 - 1/\beta)(\rho_m - \rho_c)/(\rho_m - \rho_w)$.
(d) State why the answer is much smaller than the thickness of crust removed.

---

**★2.** Compute the thermal time constant and the asymptotic thermal subsidence.

(a) Compute $\tau = a^2/(\pi^2\kappa)$ in seconds and in Ma.
(b) Compute $E_0$ for $\beta = 2$ from
$E_0 = \alpha\rho_mT_ma(1 - 1/\beta)/[2(\rho_m - \rho_w)]$.
(c) Compute the total subsidence $S_i + E_0$.
(d) State which of the two terms dominates and whether that is general.

---

**★3.** A stratigraphic column has four units:

| age (Ma) | present top (m) | present base (m) | grain density (kg m$^{-3}$) |
|---|---|---|---|
| 40 | 0 | 400 | 2650 |
| 30 | 400 | 1100 | 2700 |
| 20 | 1100 | 2000 | 2720 |
| 10 | 2000 | 3200 | 2680 |

With $\phi(z) = \phi_0e^{-z/c}$, $\phi_0 = 0.55$ and $c = 2000$ m:

(a) compute $\phi$ at the present mid-depth of each unit;
(b) decompact the topmost unit;
(c) state why the decompacted thickness always exceeds the present thickness;
(d) state what the decompaction correction assumes about the burial history.

---

## ★★ Applied

**★★4.** Run [`../code/04-basins_subsidence_demo.py`](../code/04-basins_subsidence_demo.py).

(a) Report the verification errors of the heat solver at 100 and at 400 cells,
and state what the ratio between them implies.
(b) Report the modal weights for $n = 1, 3, 5$ and their signs.
(c) Report the worst difference between the numerical solution and the exact
series, and between the single-exponential law and the exact series.
(d) State in one sentence which of those two numbers is a defect and which is a
property of the approximation.

---

**★★5.** An observed water-loaded total subsidence of 3000 m is inverted for
$\beta$ using the demo's coefficient of 11 673 m per unit of $(1 - 1/\beta)$.

(a) Compute $1 - 1/\beta$ and hence $\beta$.
(b) Compute the crustal thinning implied.
(c) Explain why one observed number cannot determine a history.
(d) State which part of the subsidence curve constrains the thermal contribution,
and what the single-exponential approximation does to that part.

---

**★★6.** Run the demo's sensitivity section.

(a) Report the change in tectonic subsidence produced by varying $\phi_0$ from
0.45 to 0.65.
(b) Report the change produced by varying the porosity decay length from 1500 m
to 3000 m.
(c) Report the change produced by varying the grain density from 2650 to
2850 kg m$^{-3}$.
(d) State which class of assumption dominates, and what that implies for the
reporting of a backstripped curve.

---

## ★★★ Research-oriented

**★★★7.** The demo verifies its heat solver against a single-sine-mode initial
condition, for which the exact answer is $1 - e^{-t/\tau}$.

(a) State why the post-rift geotherm is not a single sine mode.
(b) Explain why the mode-$n$ decay rate is $n^2/\tau$.
(c) Using the reported weights, estimate the fractional subsidence at $t = 0.1\tau$
from the first three modes and compare it with the single-mode law.
(d) State the general condition under which a single-mode approximation to an
initial-value problem for the heat equation is adequate.

---

**★★★8.** A basin is filled with sediment of bulk density $\rho_s$ rather than
with water.

(a) Recompute $S_i$ for $\beta = 2$ using $\rho_L = \rho_s = 2500$ kg m$^{-3}$.
(b) Compute the ratio of the sediment-loaded to the water-loaded instantaneous
subsidence.
(c) Explain physically why the ratio is greater than one, and what it implies
about the depth of a basin after it has been filled.
(d) State the error made by a worker who computes the tectonic subsidence with
$\rho_L = \rho_w$ while the basin was in fact filled with compact sediment, and
express it as a fraction of the answer.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
