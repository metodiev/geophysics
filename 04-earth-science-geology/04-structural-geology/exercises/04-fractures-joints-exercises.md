# Exercises — 04-04-04 Fractures, Joints and Their Geophysical Signature

Attempt these **closed-book** before opening the
[solutions](./04-fractures-joints-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/04-fractures_joints_demo.py`](../code/04-fractures_joints_demo.py)
require you to run it and report its actual output.

**Parameters.** Use $E = 50$ GPa, $\nu = 0.25$, $\gamma_s = 10$ J m$^{-2}$,
$K_{Ic} = 1.5$ MPa m$^{0.5}$, $\rho = 2600$ kg m$^{-3}$,
$k_n = 50$ GPa m$^{-1}$ and $k_t = 20$ GPa m$^{-1}$ unless a problem states
otherwise. These are TYPICAL values; the script labels them as such.

---

## ★ Foundational

**★1.** Griffith's criterion states $\sigma_c = \sqrt{2E\gamma_s/(\pi a)}$ and
the stress-intensity criterion states failure at $K_I = \sigma\sqrt{\pi a} = K_{Ic}$.

(a) Compute $\sigma_c$ for $a = 1$ mm and for $a = 0.1$ m.
(b) Compute $K_I$ at each of those stresses and show the two columns are equal.
(c) Compute $K_{Ic}$ from $\sqrt{2E\gamma_s}$ and compare with the stated
tabulated value.
(d) Explain the discrepancy in (c) physically.

---

**★2.** With $\lambda = 20$ GPa and $\mu = 20$ GPa,

(a) compute $c_{11} = \lambda + 2\mu$ and $c_{44} = \mu$;
(b) compute the background P and S velocities at $\rho = 2600$ kg m$^{-3}$;
(c) state which mode is polarized in the plane containing the fracture normal for
a set of horizontal fractures, and which is not;
(d) state why that distinction produces shear-wave splitting.

---

**★3.** For a fracture set with $k_n = 50$ GPa m$^{-1}$ and spacing 10 m,

(a) compute the added normal compliance $\Delta S_{NN} = 1/(k_n s)$;
(b) compute $Z_N = c_{11}/(k_n s)$ and state its units;
(c) compute $Z_T$ for $k_t = 20$ GPa m$^{-1}$;
(d) state the long-wavelength condition under which these compliances apply.

---

## ★★ Applied

**★★4.** Run [`../code/04-fractures_joints_demo.py`](../code/04-fractures_joints_demo.py).

(a) Report the four velocities in the zero-fracture check and the anisotropy
value, and state what the check verifies.
(b) Report $Z_N$, $Z_T$ and the P anisotropy at spacings of 100 m, 10 m and 1 m,
and state the trend.
(c) Report $\gamma$ from the closed form and from the numerical inversion at
spacing 20 m, and the shear-wave splitting in ms/m.
(d) State which tensor components carry the excess compliance, and why that
produces the sign of the P anisotropy that the table shows.

---

**★★5.** Using the cubic law $k = b^3/(12s)$,

(a) compute the permeability along a fracture set with $b = 0.5$ mm and
$s = 1$ m, in m² and in darcy;
(b) recompute for $b = 1$ mm and state the factor of change;
(c) recompute for $s = 0.1$ m and state the factor of change;
(d) state the two consequences of the cube for fracture-reservoir description.

---

**★★6.** A spacing–thickness data set gives
`spacing = 0.8254 * thickness - 0.0226 m` with $r^2 = 0.9916$ and an rms residual
of 0.12 m, and the spacing/thickness ratio ranges from 0.517 to 1.023.

(a) State whether the relation is a law or an empirical relation, and what
determines its constant.
(b) Explain why the range of the ratio matters more than the fit quality.
(c) Compute the coefficient of variation for a perfectly regular set and for a
Poisson set with unit mean spacing, and state what $C_v$ does and does not
indicate.
(d) Compute the intact fraction of a 2 m scanline for both sets and explain why
connectivity, not density, is the quantity a permeability calculation needs.

---

## ★★★ Research-oriented

**★★★7.** Derive the dimensionless excess compliances of the linear-slip model.

(a) Show that a stack of fractures each of stiffness $k_n$ and spacing $s$ adds a
normal compliance $1/(k_n s)$, explaining why the fracture strains add.
(b) Show that normalising by the background compliance $1/c_{11}$ gives
$Z_N = c_{11}/(k_n s)$ and verify the dimensions.
(c) State which elements of the compliance matrix receive $Z_N$ and $Z_T$ for a
set of fractures with normals along axis 3, and why the answer would differ for
normals along axis 1.
(d) Show that for this configuration $C_{66}$ is unaffected while
$C_{44} = C_{44}^0/(1 + Z_T)$, and hence that $\gamma = Z_T/2$ exactly. Verify
your result against the demo's output.

---

**★★★8.** A crossed-dipole sonic log reports a fast shear direction and a
shear-wave splitting of 5 per cent over a 50 m interval.

(a) State what a 5 per cent splitting means in terms of velocities, and compute
the delay over the interval for a background $V_S = 3000$ m s$^{-1}$.
(b) Using $\gamma = Z_T/2$, estimate $Z_T$ and hence $k_t s$ for a stated $c_{44}$.
(c) State every assumption in the chain from the measured splitting to the
fracture stiffness, and identify the one that contributes the largest
uncertainty.
(d) State what additional measurement you would require before reporting a
fracture density, and what it would constrain.

Report measured values only if you verify them numerically, and state which of
your results are analytic.
