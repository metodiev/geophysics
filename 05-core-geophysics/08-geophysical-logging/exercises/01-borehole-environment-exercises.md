# Exercises — 05-08-01 The Borehole Environment and Invasion Profiles

Attempt these **closed-book** before opening the
[solutions](./01-borehole-environment-solutions.md). Difficulty:
★ foundational · ★★ applied · ★★★ research-oriented.

Problems referring to
[`../code/borehole_env_demo.py`](../code/borehole_env_demo.py) require you to run
it and report its actual output. **State the mud, the hole condition and the time
since drilling for every invasion answer. No tool specification may be quoted as
universal.**

Constants: $\mu_0 = 4\pi\times10^{-7}$ H m⁻¹; $1\ \mathrm{psi} = 6.895$ kPa.

---

## ★ Foundational

**★1.** List the four ways drilling perturbs the formation, and for each the
measurement that is affected most.

**★2.** Distinguish $R_w$ and $R_{mf}$: what each is a property of, where it is
measured, and which one appears in Archie's law.

**★3.** Convert a filtrate diffusivity of 3 cm² s⁻¹ to SI and evaluate
$\sqrt{4Dt}$ at $t = 10$, 100 and 1000 h.

---

## ★★ Applied

**★★4.** Run [`../code/borehole_env_demo.py`](../code/borehole_env_demo.py).

(a) Report the planar and cylindrical front positions and exponents.
(b) Explain in two sentences why the cylindrical exponent is smaller.
(c) State the time at which the deep tool's reading exceeds the virgin formation's
conductivity by 5 per cent (interpolate the table).

---

**★★5.** Using the weighting function $w(r) \propto e^{-(r-r_w)/L}\,r$ with
$L = 0.15$ m and a step profile with $R_{xo} = 1$ Ω m, $R_t = 100$ Ω m,
$r_i = 0.25$ m:

(a) compute the geometric factor $a$ (fraction of the response inside $r_i$);
(b) compute the apparent conductivity and resistivity;
(c) state what a reported "resistivity" from that reading actually is.

---

**★★6.** For the demonstration's parameters, recompute the invasion correction at
$t = 36$ h instead of 100 h, and report $R_t$ and $S_w$ for both the smooth and the
step profiles.

---

## ★★★ Research-oriented

**★★★7.** Extend the solver to a two-layer formation with a radial permeability
contrast, using a stated model for the diffusivity contrast.

(a) Report how much the front departs from a circle for a 10:1 contrast.
(b) State the extra assumption your model needs.
(c) State the measurement that would test it.

---

**★★★8.** The demonstration's correction is exact for a step profile and fails for
a smooth one. Parameterise the invasion profile with one additional shape
parameter, invert for it jointly with $R_t$ using three readings (a micro-, a
shallow and a deep reading), and report the residual error in $R_t$ for both
profiles. State what field measurement would constrain the shape parameter
directly.

---

## Reference list used in this problem set

- [05-08-01 lesson](../01-borehole-environment.md)
- [05-08-03 Resistivity, Induction and Laterolog Tools](../03-resistivity-logging.md)
- [Solutions](./01-borehole-environment-solutions.md)
