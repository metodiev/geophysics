# Solutions — 13-01-01 Momentum, Mass and Energy Balances in the Solid Earth

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. Several problems have more than one defensible answer; where that is
> true it is said so.

Lesson: [01 Momentum, Mass and Energy Balances](../01-momentum-mass-energy.md).
Conversions: $1\ \mathrm{yr} = 3.1557\times10^{7}\ \mathrm{s}$,
$g = 9.81\ \mathrm{m\,s^{-2}}$.

---

## ★1 — Stokes velocity and Reynolds number

$$u = \frac{2\Delta\rho\,g\,a^{2}}{9\eta}
= \frac{2(30)(9.81)(5\times10^{4})^{2}}{9(10^{21})}
= \frac{1.4715\times10^{12}}{9\times10^{21}}
= 1.635\times10^{-10}\ \mathrm{m\,s^{-1}} .$$

Converting: $u = 1.635\times10^{-10}\times3.1557\times10^{7}\times10^{3}
= 5.160\ \mathrm{mm\,yr^{-1}}$.

$$Re = \frac{\rho u a}{\eta}
= \frac{(3300)(1.635\times10^{-10})(5\times10^{4})}{10^{21}}
= 2.70\times10^{-23} .$$

**Validity.** $Re\ll1$ by 23 orders of magnitude, so Stokes' law applies with no
inertial correction whatsoever. The real caveats are physical: uniform viscosity,
no boundary interaction, and a blob that neither deforms nor shrinks while it
rises.

---

## ★2 — Dissipation in a shear zone

$$u = \frac{20\times10^{-3}}{3.1557\times10^{7}} = 6.338\times10^{-10}\ \mathrm{m\,s^{-1}},
\qquad
\dot\gamma = \frac{u}{d} = \frac{6.338\times10^{-10}}{2\times10^{4}}
= 3.169\times10^{-14}\ \mathrm{s^{-1}} .$$

$$\Phi = \eta\dot\gamma^{2} = (10^{21})(3.169\times10^{-14})^{2}
= 1.004\times10^{-6}\ \mathrm{W\,m^{-3}},$$

$$q = \Phi d = (1.004\times10^{-6})(2\times10^{4})
= 2.008\times10^{-2}\ \mathrm{W\,m^{-2}} = 20.1\ \mathrm{mW\,m^{-2}} .$$

That is a third of a typical continental surface flux, produced by one shear
zone. Because $\Phi\propto\dot\gamma^{2}\propto1/d^{2}$, halving the shear-zone
thickness quadruples the local dissipation.

---

## ★3 — Units

(a) $\eta u/L^{2}$: $\mathrm{Pa\,s}\times\mathrm{m\,s^{-1}}/\mathrm{m^{2}}
= \mathrm{Pa\,m^{-1}}$, a force per unit volume. ✔
(b) $uL/\kappa$: $\mathrm{m\,s^{-1}}\times\mathrm{m}/\mathrm{m^{2}\,s^{-1}}$,
dimensionless. ✔
(c) $\rho c_pV\Delta T$: $\mathrm{kg\,m^{-3}}\times\mathrm{J\,kg^{-1}\,K^{-1}}
\times\mathrm{m^{3}}\times\mathrm{K} = \mathrm{J}$. ✔

---

## ★★4 — Geotherm with strong radiogenic heating

**(a)**

$$q_s = k\left[\frac{T_{\text{Moho}}-T_s}{h} + \frac{Hh}{2k}\right]
= 2.5\left[\frac{650}{4\times10^{4}}\right] + \frac{(2\times10^{-6})(4\times10^{4})}{2}
= 0.040625 + 0.040 = 0.080625\ \mathrm{W\,m^{-2}},$$

$$q_s = 80.6\ \mathrm{mW\,m^{-2}}, \qquad
q_{\text{Moho}} = q_s - Hh = 0.080625 - 0.080 = 0.000625\ \mathrm{W\,m^{-2}}
= 0.63\ \mathrm{mW\,m^{-2}} .$$

The radiogenic share is $Hh/q_s = 0.080/0.080625 = 99.2\%$. The Moho flux is
nearly zero because essentially all the heat leaving the surface was generated
within the crust: the mantle contributes almost nothing to this column.

**(b)** Setting $q_{\text{Moho}} = k(T_{\text{Moho}}-T_s)/h - Hh/2 = 0$:

$$H^{*} = \frac{2k(T_{\text{Moho}}-T_s)}{h^{2}}
= \frac{2(2.5)(650)}{(4\times10^{4})^{2}}
= \frac{3250}{1.6\times10^{9}} = 2.031\times10^{-6}\ \mathrm{W\,m^{-3}} .$$

Physically, at this production rate the crust supplies exactly the flux it
conducts to the surface, and the mantle heat flux into the base of the crust is
zero. Above it, heat would flow *downwards* into the mantle — which happens in
regions of very high crustal heat production.

---

## ★★5 — Péclet numbers at two scales

$$u = \frac{30\times10^{-3}}{3.1557\times10^{7}} = 9.507\times10^{-10}\ \mathrm{m\,s^{-1}} .$$

| $L$ | $t_{\text{diff}} = L^{2}/\kappa$ | $t_{\text{adv}} = L/u$ | $Pe$ |
|---|---|---|---|
| 10 km | $10^{8}/10^{-6} = 10^{14}\ \mathrm{s} = 3.169$ Myr | $10^{4}/9.507\times10^{-10} = 1.052\times10^{13}\ \mathrm{s} = 0.333$ Myr | 9.51 |
| 1000 km | $10^{12}/10^{-6} = 10^{18}\ \mathrm{s} = 31.7$ Gyr | $10^{6}/9.507\times10^{-10} = 1.052\times10^{15}\ \mathrm{s} = 33.3$ Myr | 950.7 |

Advection dominates at both scales. The instructive entry is the 10 km one,
where $Pe = 9.5$: only one order of magnitude separates advection from
conduction, so at outcrop or shear-zone scale a fluid moving at plate speeds
still has time to conduct, and the two mechanisms are comparable. That is why
temperature profiles measured over kilometres are not simply advected.

---

## ★★6 — Inverting for viscosity

Observed speed: $u = 5\times10^{5}/20\times10^{6} = 0.025\ \mathrm{m\,yr^{-1}}
= 7.923\times10^{-10}\ \mathrm{m\,s^{-1}}$.

$$\eta = \frac{2\Delta\rho\,g\,a^{2}}{9u}
= \frac{2(25)(9.81)(1.2\times10^{5})^{2}}{9(7.923\times10^{-10})}
= \frac{7.063\times10^{12}}{7.131\times10^{-9}}
= 9.91\times10^{20}\ \mathrm{Pa\,s} .$$

**Largest error sources.** (1) The radius enters as $a^{2}$: a 20% radius error
becomes a 44% viscosity error, and the radius of a rising blob is itself rarely
observed (it is inferred from tomography or from the swell). (2) The density
contrast enters linearly and is itself a product $\rho\alpha\Delta T$ in which
$\alpha$ and $\Delta T$ are both uncertain. A third, arguably larger, problem is
the *model*: a blob with a free-slip surface rises three times faster than a
rigid one (the Hadamard–Rybczynski factor), so the choice of internal boundary
condition alone can change the answer by a factor of three.

---

## ★★★7 — Budget sensitivity

$$Q_{\text{loss}} = q_{\text{avg}}A = (0.100)(5.101\times10^{14})
= 5.101\times10^{13}\ \mathrm{W} = 51.0\ \mathrm{TW},$$

$$\text{Urey ratio} = \frac{25.0}{51.0} = 0.490,$$

$$t_{\text{cool}} = \frac{4.862\times10^{30}}{(5.101-2.500)\times10^{13}}
= 1.869\times10^{17}\ \mathrm{s} = 5.92\ \mathrm{Gyr} .$$

The Urey ratio moves from 0.451 to 0.490 (a 9% change) and the cooling time from
6.32 to 5.92 Gyr (a 6% change). Both inputs enter the Urey ratio as a ratio, so
a given *fractional* change in either shifts the conclusion comparably — but the
heat-loss term is the denominator of the cooling time and therefore nearly
cancels: the cooling time is controlled by the *difference* between loss and
production, which makes it considerably more sensitive to the production rate
than the Urey ratio is. That asymmetry is worth remembering: a Urey ratio near 1
makes the cooling time (and hence any inference about secular cooling) extremely
unstable.

---

## ★★★8 — Demonstrating the necessity of $\nabla\cdot\mathbf{u} = 0$

**Diagnostic.** The horizontally averaged temperature drift
$\mathrm{d}\langle T\rangle/\mathrm{d}t$ in a purely conducting state, where the
exact answer is zero. A divergent velocity field moves mass into or out of the
mean column and produces a nonzero drift even when the temperature perturbation
is zero.

**Initial condition.** $T = 1-z$ exactly (conduction), plus a *deliberately*
non-divergence-free velocity field with the same amplitude as a real flow at that
$Ra$, e.g. $\mathbf{u} = (\sin\pi x\cos\pi z, \sin\pi z\cos\pi x)$ without the
$\nabla\cdot\mathbf{u}$ correction.

**Test and length.** Compute $\max|\nabla\cdot\mathbf{u}|$ on the grid and the
drift of $\langle T\rangle$ over 1000 steps at $\mathrm{CFL} = 0.5$. Then repeat
with the divergence-free streamfunction field of the same amplitude.

**Acceptance.** A drift in the mean temperature proportional to
$\max|\nabla\cdot\mathbf{u}|$ would convincingly show the field is doing work
that does not exist physically; a mean-temperature drift below $10^{-10}$ per
step with the streamfunction field, over the same run, would show the
incompressible construction is exactly conservative. Any specification that omits
the *comparison* between a divergent and a divergence-free field at the same
amplitude has not isolated the effect.

---

## ★★★9 — Why 6 Gyr is a constraint, not a prediction

*Model answer.* The 6.32 Gyr figure is the heat content of the mantle divided by
the *present* difference between heat loss (44.4 TW) and radiogenic production
(20 TW). For it to be a prediction of the Earth's remaining time it would have to
be constant, which requires (i) the radiogenic production to be constant — false,
because the radioactive parent abundances decay, and in the past the production
was *higher*, which shortens the interval; (ii) the heat loss to be constant —
false, because plate-tectonic heat loss depends on seafloor age, continental
configuration and mantle temperature; and (iii) the heat content to be
independent of how the temperature profile is arranged, whereas what matters
dynamically is the *upper-mantle* temperature, which is partly decoupled from the
whole-mantle average.

Of these, the decay of the radiogenic inventory fails first and most
quantitatively: the difference between loss and production was larger in the
past, so the mantle cooled faster, so the interval implied by present values is
an underestimate of the time the system can have been running. The correct use of
the number is the converse: because the present-day rate cannot be sustained for
a time comparable to the age of the Earth, the rate must have been different, and
the geological record of that difference — increasing plate speeds, higher
Palaeoproterozoic heat production — is the evidence the budget is used to
constrain.
