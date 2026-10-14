# Solutions — 02-01-03 Scaling Laws, Similarity and Dimensional Reasoning

> **Read this after attempting the exercises, not before.**
>
> Numbers were computed; the π groups were obtained by exact rational
> elimination on the exponent matrix, not by guesswork. Where a value rests on a
> *nominal* or *assumed* input, that is stated in the answer, because it sets the
> number of defensible digits.

---

## ★1 — Dimensionless groups and their meaning

| | Group | Measures the competition between |
|---|---|---|
| (a) | $\mathrm{Re} = \rho u L/\eta$ | inertia and viscous stress |
| (b) | $\mathrm{Fo}$ (Fourier) $\kappa t/L^{2}$ | elapsed time and diffusion time |
| (c) | $\mathrm{Pe}$ (Péclet) $uL/\kappa$ | advection and diffusion |
| (d) | $\mathrm{De}$ (Deborah) $\tau_{\text{relax}}/\tau_{\text{obs}}$ | internal relaxation and observation time |
| (e) | $r/h = \rho_c/(\rho_m-\rho_c)$ | the buoyancy of the crust against the density contrast at the compensation depth |

Each is a ratio of two quantities with the *same dimensions*; this is why
dimensionless groups are the natural language for regimes.

---

## ★2 — Pendulum period and the small-angle regime

**(a)** $T_0 = 2\pi\sqrt{1/9.81} = 2.006\,067$ s.

**(b)** With $\theta_0 = 30° = 0.5236$ rad:
$T = 2.006\,067\,(1 + 0.5236^{2}/16 + 11(0.5236)^{4}/3072)
= 2.006\,067\,(1+0.017\,145+0.000\,166) = 2.040\,990$ s.
The small-angle form is low by $(2.040\,990-2.006\,067)/2.040\,990 = 1.71\%$.
(An exact quadrature of the elliptic integral gives 2.0409899 s, so the
two-term series is accurate to 5×10⁻⁷ s here.)

**(c)** Setting $\theta^{2}/16 = 0.01$ gives $\theta = 0.4$ rad $= 22.9°$; the
exact quadrature gives 0.998% at 22.9° and 1.10% at 24°, so **about 23°** is the
1% boundary. The regime statement is: "small-angle form usable to ~5° for
0.05% accuracy, ~23° for 1% accuracy, not usable beyond ~45°."

---

## ★3 — Diffusion lengths and times

**(a)** $\sqrt{\kappa t}$: at 1 Ma, $t = 3.1557\times10^{13}$ s, so
$\sqrt{10^{-6}\times3.1557\times10^{13}} = 5.618\times10^{3}$ m $= \mathbf{5.62\ km}$.
At 10 Ma it is $\sqrt{10}$ times larger: **17.76 km**.

**(b)** Setting $\sqrt{\kappa t} = 5\times10^{4}$ m gives
$t = (5\times10^{4})^{2}/10^{-6} = 2.5\times10^{12}$ s $= \mathbf{7.9\times10^{4}\ yr}$.

**(c)** $L \propto \sqrt{t}$, so doubling $L$ requires **four times** the time.

---

## ★4 — Reynolds numbers

**(a)** $u = 0.01\ \mathrm{m\,yr^{-1}} = 0.01/3.1557\times10^{7}
= 3.169\times10^{-10}\ \mathrm{m\,s^{-1}}$, so
$\mathrm{Re} = 3300\times3.169\times10^{-10}\times10^{6}/10^{21}
= 1.046\times10^{-21}$.

**(b)** $\mathrm{Re} = 1025\times0.1\times100/10^{-3} = 1.025\times10^{7}$.

**(c)** Ratio $= 1.025\times10^{7}/1.046\times10^{-21} = 9.80\times10^{27}$ —
about 28 orders of magnitude. No single dimensionless-number match is available
by adjusting one parameter.

---

## ★★5 — Rayleigh number and its uncertain inputs

**(a)**
$$\mathrm{Ra} = \frac{3300\times9.81\times3\times10^{-5}\times3000
\times(2.89\times10^{6})^{3}}{10^{-6}\times10^{21}} = 7.03\times10^{7}.$$

**(b)**

| $\eta$ (Pa s) | $\mathrm{Ra}$ |
|---|---|
| $10^{19}$ | $7.03\times10^{9}$ |
| $10^{20}$ | $7.03\times10^{8}$ |
| $10^{21}$ | $7.03\times10^{7}$ |
| $10^{22}$ | $7.03\times10^{6}$ |

**(c)** Only the order of magnitude is defensible. $\rho$, $\kappa$ and $\eta$
are *nominal* (each with a factor-of-several or worse range),
$\alpha$ and $\Delta T$ are *assumed* inputs of this calculation, and $\eta$
alone moves the answer over three decades across its nominal range. Report
$\mathrm{Ra} \sim 10^{7}$–$10^{8}$ and state the sensitivity — which is exactly
what the table provides. The *conclusion* that the mantle convects vigorously
(onset at $\mathrm{Ra} \sim 10^{3}$) is robust across the whole range; the
*number* is not.

---

## ★★6 — Airy isostasy

**(a)** Coefficient $= 2700/600 = 4.5$, so a 3 km plateau has a
$\mathbf{13.5\ km}$ root.

**(b)** With $\Delta\rho = 600 \pm 50$,
$$r = \frac{\rho_c h}{\Delta\rho},\qquad
u(r) = r\,\frac{u(\Delta\rho)}{\Delta\rho} = 13.5\times\frac{50}{600}
= 1.13\ \mathrm{km}.$$
So $r = (13.5 \pm 1.1)$ km. Note the sensitivity: a *half* term error in
$\Delta\rho$ is a 4% error in the root, because the answer depends on the
reciprocal of the contrast.

**(c)** The linear law fails when (i) compensation is not local but flexural, so
that the lithosphere's finite strength spreads the load, making the actual root
shallower and wider; and (ii) the density contrast is not a single constant,
e.g. when there are two compensation levels (crustal root and a deeper mantle
density change), or when the load is a surface load over a sedimentary basin
rather than a topography.

---

## ★★7 — Dynamic similarity of a tank

**(a)** $\mathrm{Re} = 1000\times0.1\times0.3/10^{-3} = 3\times10^{4}$.

**(b)** Requiring $1000\times0.1\times0.3/\eta = 1.046\times10^{-21}$ gives
$$\eta = \frac{30}{1.046\times10^{-21}} = 2.87\times10^{22}\ \mathrm{Pa\,s}.$$

**(c)** Requiring $1000\times u\times0.3/10^{-3} = 1.046\times10^{-21}$ gives
$$u = \frac{1.046\times10^{-21}\times10^{-3}}{300} = 3.49\times10^{-27}\
\mathrm{m\,s^{-1}}.$$

**(d)** Neither is realisable. A fluid with $\eta \approx 3\times10^{22}$ Pa s
would have to be a solid on laboratory timescales (even glass is of order
$10^{12}$ Pa s near its glass transition), and a speed of
$3.5\times10^{-27}\ \mathrm{m\,s^{-1}}$ is about 10⁻¹⁹ m per billion years,
utterly below Brownian motion and laboratory vibration. **The mantle has no
dynamically similar laboratory analogue in a normal gravity field**; analogue
experiments target sub-problems (a Rayleigh–Taylor instability, say) whose own
π groups can be matched.

---

## ★★8 — Strength does not scale

**(a)** Weight $\propto s^{3} = 10^{6}$; load-bearing area $\propto s^{2} = 10^{4}$;
stress $= $ weight/area $\propto s = 100$.

**(b)** If the material is the same, the failure strength is the same, so the
model's stress is 100 times *smaller* relative to strength than the prototype's:
the model has a factor-100 **larger** safety margin. The model will not fail, and
therefore cannot reproduce the prototype's failure mode.

**(c)** A centrifuge multiplies effective gravity by $N$, restoring
$g$-dependent similarity: weight scales as $Ns^{3}$ while area scales as $s^{2}$,
so choosing $N = 1/s$ makes the model stress match the prototype's. The adjusted
quantity is the effective gravity (by rotation), and the price is a strong
Coriolis effect from the rotation itself, which introduces a new dimensionless
group that must also be matched.

---

## ★★★9 — Stokes sinking by π theorem

**(a)** In $(M,L,T)$:

| Variable | Dimension vector |
|---|---|
| $v$ | $(0,1,-1)$ |
| $\Delta\rho$ | $(1,-3,0)$ |
| $g$ | $(0,1,-2)$ |
| $a$ | $(0,1,0)$ |
| $\eta$ | $(1,-1,-1)$ |

The exponent matrix (rows $M,L,T$; columns the five variables) has
**rank 3**.

**(b)** $n - r = 5 - 3 = 2$ independent groups. Exact rational elimination gives
$$\Pi_1 = \frac{ga}{v^{2}}, \qquad \Pi_2 = \frac{g\eta}{v^{3}\Delta\rho}.$$
(Any invertible transformation of these is equally valid — the null space is a
vector space and the basis is arbitrary; this is the point made in §2.1 of the
lesson.)

**(c)** The conventional group is
$$\frac{v\eta}{\Delta\rho g a^{2}}
= \frac{\Pi_2}{\Pi_1^{3/2}\cdot\Pi_1^{1/2}} \cdot \text{const}
= \frac{\Pi_2}{\Pi_1^{2}},$$
because $\Pi_2/\Pi_1^{2} = (g\eta/(v^{3}\Delta\rho))/(g^{2}a^{2}/v^{4})
= \eta v/(\Delta\rho g a^{2})$. So it is a combination of the two basis groups,
as claimed. Equivalently, the second independent group can be written
$\mathrm{Re} = \Delta\rho\,v\,a/\eta$, since
$1/\mathrm{Re} = \Pi_2/\Pi_1^{2}$ up to a conventional factor.

**(d)** Saying that $v\eta/(\Delta\rho g a^{2})$ is *identically* $2/9$ — i.e.
that it does not depend on the other group — asserts that **inertia is
irrelevant**. That is the Stokes (creeping-flow) regime
$\mathrm{Re} = \Delta\rho v a/\eta \ll 1$. Outside it the second group matters,
the $2/9$ coefficient changes (the drag coefficient becomes a function of
$\mathrm{Re}$), and the terminal velocity falls below the Stokes value. This is
the clearest example in the lesson of the general rule: dimensional analysis
supplies the groups; the *physics* tells you which groups the answer depends on,
and the regime of validity is the statement that one of them can be neglected.

---

## ★★★10 — Centrifuge scaling for a buoyancy instability

**(a)** $\mathrm{Ra} \propto g L^{3}$ with the other factors fixed, so
$\mathrm{Ra}_{\text{model}} = \mathrm{Ra}_{\text{proto}}$ requires
$$g_{\text{model}} = g_{\text{proto}}\left(\frac{L_{\text{proto}}}
{L_{\text{model}}}\right)^{3} = 1000^{3}\,g = 10^{9}\,g.$$
A billion-fold increase in effective gravity — not attainable. This is why
centrifuge models target $\mathrm{Ra}$-independent sub-problems (the growth rate
of a Rayleigh–Taylor instability, say) whose own groups can be matched.

**(b)** With $g_{\text{eff}} = \omega^{2}R$ and, say, a centrifuge arm
$R_{\text{model}} = 1$ m against an Earth radius $R_{\text{proto}} = 6.371\times
10^{6}$ m,
$$\frac{\omega_{\text{model}}}{\omega_{\text{proto}}}
= \sqrt{\frac{g_{\text{model}}}{g_{\text{proto}}}\cdot
\frac{R_{\text{proto}}}{R_{\text{model}}}}
= \sqrt{10^{9}\times6.371\times10^{6}} = 8.0\times10^{7}.$$
The Earth's rotation rate is $7.292\,115\times10^{-5}$ rad s⁻¹, so the model
would need $\omega_{\text{model}} = 5.8\times10^{3}$ rad s⁻¹ — about
930 revolutions per second, which no centrifuge and no material can survive.
(Stated as a ratio, the answer is independent of the arm radius only in the
inverse sense: a longer arm lowers the required $\omega$ as $R^{-1/2}$.)

**(c)** Two further conditions: the **viscosity ratio** (or, equivalently, the
rheology must be matched — a power-law exponent cannot be scaled away) and the
**Coriolis ratio** ($\omega L/U$, the Rossby number), since spinning the model
introduces a rotation the prototype may not have at that scale. The
most likely to fail in practice is the rheological one: rock deforms by
temperature- and stress-dependent creep, whereas model materials are usually
linear viscous or plastic with a different stress exponent, so no single
viscosity ratio can be matched simultaneously at all depths and strain rates.

---

## Self-assessment: have you actually learned this?

- [ ] I can name the dimensionless group appropriate to a process and say what
      competition it measures.
- [ ] I can compute the small-angle error at a stated angle and give the angle
      beyond which an approximation must be abandoned.
- [ ] I can derive and use $L \sim \sqrt{\kappa t}$ in a geophysical estimate.
- [ ] I can evaluate $\mathrm{Ra}$ and $\mathrm{Re}$, and state the number of
      digits my inputs support.
- [ ] I can decide, with numbers, whether two systems are dynamically similar.
- [ ] I can obtain π groups by computing the rank and null space of an exponent
      matrix, and check a named group for independence.
