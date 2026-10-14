# Solutions — 23-06-07 Rock Mechanics Testing: Strength, Friction, Fracture

The lesson is [07 Rock Mechanics Testing](../07-rock-mechanics-lab.md). All values are
**SYNTHETIC**.

## ★1

$$E = \frac{25\times10^{6}}{0.8\times10^{-3}} = 3.125\times10^{10}\ \mathrm{Pa}
= 31.25\ \mathrm{GPa},$$

$$\frac{A}{K_mL} = \frac{1.13\times10^{-3}}{(4.0\times10^{9})(0.080)}
= 3.531\times10^{-12}\ \mathrm{Pa^{-1}} = \frac{1}{283.2\ \mathrm{GPa}} ,$$

$$E_{\text{app}} = \left(\frac{1}{31.25} + \frac{1}{283.2}\right)^{-1}
= \left(0.032000 + 0.003531\right)^{-1} = 28.144\ \mathrm{GPa},$$

an error of **−9.94 %**. The sign is always negative: the machine's compliance adds to the
measured displacement, so the apparent modulus is always *lower* than the rock's. A
one-signed error of 10 % cannot be removed by more tests, only by measuring $K_m$ (with a
specimen of known modulus) and subtracting its contribution.

## ★2

$$\frac{\sigma_1}{\sigma_3} > \frac{1+\mu}{1-\mu} = \frac{1.6}{0.4} = 4.0 .$$

With $\mu = 0.6$ a differential stress ratio of four is enough for reactivation, much lower
than the 12.3 of the lesson's $\mu = 0.85$ — the friction coefficient enters the threshold
strongly (a 40 % reduction in $\mu$ reduces the required ratio by 68 %).

A **rise in pore pressure lowers the effective normal stress** while leaving the shear stress
essentially unchanged (because the shear traction is carried by the rock framework), so the
*effective* $\sigma_1/\sigma_3$ ratio rises and the fault moves toward reactivation. The
number to report is therefore the threshold in *effective* stress, and the pore-pressure
scenario is part of the geomechanical analysis rather than an add-on to it. This is why
reservoir depletion (which *reduces* pore pressure and stabilizes the fault by raising the
effective normal stress) and injection (which destabilizes it) are opposite problems.

## ★3

Least-squares fit of $\sigma_1$ on $\sigma_3$:

$$\bar\sigma_3 = 30.0,\quad \bar\sigma_1 = 136.667\ \mathrm{MPa},$$

$$S_{xy} = (-25)(-56.667) + (-5)(-6.667) + (30)(63.333) = 3350.0,$$

$$S_{xx} = 625 + 25 + 900 = 1550.0 \;\Rightarrow\; q = \frac{3350.0}{1550.0} = 2.1613,$$

$$\mathrm{UCS} = 136.667 - (2.1613)(30.0) = 71.828\ \mathrm{MPa},$$

| $\sigma_3$ | $\sigma_1$ measured | Fitted | Residual |
|---|---|---|---|
| 5 | 80 | 82.63 | −2.63 |
| 25 | 130 | 125.86 | +4.14 |
| 60 | 200 | 201.51 | −1.51 |

$$\phi = \arcsin\left(\frac{q-1}{q+1}\right)
= \arcsin\left(\frac{1.1613}{3.1613}\right) = \arcsin(0.36736)
= 21.55^\circ,$$

$$c = \frac{\mathrm{UCS}(1-\sin\phi)}{2\cos\phi}
= \frac{71.828(0.63264)}{2(0.93013)} = \frac{45.435}{1.86026}
= 24.429\ \mathrm{MPa} .$$

The residuals alternate in sign, as in the lesson: consistent with scatter, but with three
points a slight curvature cannot be excluded, and the intercept is an extrapolation to zero
confinement. In a report the pair should be given **with their negative correlation** — a
steeper fit gives a larger $\phi$ and a smaller $c$ — and the confinement range (5–60 MPa)
must be stated, because extrapolating these parameters to 300 MPa or to 0 MPa is a
modelling decision.

## ★4

| $\sigma_n$ (MPa) | Branch | $\tau$ (MPa) | $\tau/\sigma_n$ |
|---|---|---|---|
| 30 | $\tau = 0.85\sigma_n$ | 25.50 | 0.850 |
| 500 | $\tau = 50 + 0.6\sigma_n$ | 350.00 | 0.700 |

The 30 MPa case is on the low-stress branch where the coefficient is constant; the 500 MPa
case is on the high-stress branch, where the apparent coefficient has fallen to 0.70 because
of the constant 50 MPa term. Two points: the high-stress branch is *weaker* in relative
terms, so extrapolating the simple $0.85$ rule to deep conditions **overestimates** the
friction there; and the branch boundary (about 200 MPa in normal stress) is itself an
empirical statement with scatter, so values near it should be quoted as a range.

## ★5

Size: with a power of −0.20,

$$\frac{\sigma(5d)}{\sigma(d)} = 5^{-0.20} = 0.7248
\quad\Rightarrow\quad \textbf{27.5 % weaker} .$$

Rate:

$$\Delta\tau = a\sigma_{\text{eff}}\ln(20) = 0.5 \times 2.9957 = 1.498\ \mathrm{MPa} .$$

If the reference strength is 150 MPa, the rate effect is 1.498/150 = **1.0 %** — so the size
effect is **27.5× larger** in this example. The practical conclusion: the size effect decides
whether a laboratory strength can be applied to a rock mass, while the rate effect is a small
correction that matters only for comparing tests done at very different rates (or for
earthquake mechanics, where the rate *is* the variable).

## ★6

A model answer.

**Geometry and confinement.** Core is 25 mm diameter, so with the lesson's aspect-ratio
argument ($L/D \ge 2.5$ for a 4–5 % end-effect bias) the specimens are 60–70 mm long; if the
core allows, 70 mm gives $L/D = 2.8$. Use **lubricated ends** (to reduce end friction and
barrelling) and grind the ends parallel, and measure the machine stiffness with an
aluminium or steel specimen before the campaign. The confinement range must **bracket the
in-situ effective stress** and probe the transition: with $\sigma_v' \approx 30$ MPa at 2 km,
test at $\sigma_3 = 5, 15, 30$ and 60 MPa — four pressures spanning a factor of 12, with the
in-situ value in the middle rather than at the end of the fit. If the caprock is weak
(common for shales), add a 2 MPa test to constrain the low-confinement behaviour, because
caprock failure during injection is a *low-effective-stress* problem.

**Number of tests and scatter.** Four confining pressures × 3 specimens = 12 tests, giving a
residual check on the fit's linearity and a standard error on $q$, hence on $\phi$. Caprocks
are heterogeneous (laminations, clay content), so the between-specimen standard deviation is
often 10–20 % of the strength; with 3 specimens per pressure the standard error of each
point is 6–12 %, and the fit's parameter uncertainties follow from that — which is a good
argument for *more specimens at fewer pressures* if the core is limited, because the fit's
precision is driven by the number of points, not by the number of pressures.

**Corrections.** Machine compliance (from a known-modulus specimen) applied to every modulus;
end friction minimized by lubrication and checked by comparing strengths from two
$L/D$ ratios; strain rate held constant across the programme and reported; pore pressure
controlled and reported (drained tests on a low-permeability caprock need very low rates, or
the test is effectively undrained and the pore pressure must be measured, not assumed).

**Friction and reactivation.** Use the fitted $c$ and $\phi$ for the intact rock and Byerlee's
law for any pre-existing discontinuity (a bedding plane or a fracture), because intact-rock
cohesion does not apply to a slip surface. For reactivation with $\mu = 0.6$ (a
clay-rich caprock can be lower), the threshold is $\sigma_1/\sigma_3 = 4.0$ in effective
stress. Then run the three scenarios explicitly:

| Scenario | $\sigma_v'$ (MPa) | Pore pressure change | Effect on reactivation |
|---|---|---|---|
| pre-production | 30 | 0 | reference |
| after 10 MPa depletion | 30 (total unchanged, $p_p$ −10) | $p_p$ falls | $\sigma_n'$ rises: **stabilizing** |
| injection, $p_p$ +5 | 30 | $p_p$ rises 5 | $\sigma_n'$ falls: **destabilizing**, and the induced poroelastic stress change must be added |

So the analysis must cover both directions: the caprock is *most* at risk not during
injection but when injection follows depletion and re-pressurizes the reservoir, which is
exactly the sequence that raises $p_p$ from a lowered baseline while the total stresses are
unchanged.

**Uncertainty budget for $c$ and $\phi$.** $\phi$ comes from the slope: with four pressures
spanning 5–60 MPa and 6–12 % strength scatter, the slope's relative uncertainty is roughly
5–10 %, which maps to $\pm 2$–4° in $\phi$; $c$ comes from the intercept, which is an
extrapolation and carries a larger relative uncertainty (often 20–30 %) **negatively
correlated** with $\phi$. The honest report is a covariance ellipse or a pair of extreme
parameter sets, not two independent error bars.

**What cannot be supported.** (i) The **rock-mass** strength and the discontinuity network's
behaviour: 25 mm plugs cannot sample a fracture population, and the size effect (a 10× larger
volume is 37 % weaker in the lesson's model) means plug strengths are an upper bound.
(ii) The **long-term** and **chemically coupled** behaviour: CO₂-brine-rock reactions change
the clay and the friction coefficient over years, and a laboratory test of days cannot bound
that. Both belong in the report as stated limits on the parameter values.
