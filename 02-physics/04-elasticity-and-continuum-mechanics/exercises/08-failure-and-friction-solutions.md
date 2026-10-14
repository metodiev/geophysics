# Solutions — 02-04-08 Rock Failure, Fracture and Rate-State Friction

Solutions to [`08-failure-and-friction-exercises.md`](./08-failure-and-friction-exercises.md).
Numbers were produced with the companion script
[`../code/failure_friction_demo.py`](../code/failure_friction_demo.py) or with
standard-library Python written for the exercise. Model parameters are **chosen**,
not measured; $\mu = 0.6$ and $\mu = 0.7$ are the conventional roundings of
published compilations and are not measured for a specific rock here.

---

## ★1

(a) $\varphi = \arctan(0.7) = 34.992020^\circ$.

$$\sigma_1' = \frac{2C\cos\varphi + \sigma_3'(1+\sin\varphi)}{1-\sin\varphi}
= \frac{2(15\times10^6)(0.819152) + (50\times10^6)(1.573576)}{0.426424}
= 242.065556\ \text{MPa}.$$

(b) The plane's **normal** makes $45^\circ + \varphi/2 = 62.496010^\circ$ with
$\sigma_1$; the plane itself is inclined
$45^\circ - \varphi/2 = 27.503990^\circ$ to $\sigma_1$.

(c) With centre $146.032778$ MPa and radius $96.032778$ MPa, and
$\theta = 62.496010^\circ$ (so $2\theta = 124.992020^\circ$):

$$\sigma_n' = 146.032778 + 96.032778\cos(124.992020^\circ) = 90.961596\ \text{MPa},$$
$$\tau = 96.032778\sin(124.992020^\circ) = 78.673117\ \text{MPa}.$$

Check: $C + \mu\sigma_n' = 15 + 0.7(90.961596) = 78.673117$ MPa, identical to
$\tau$ to all printed digits ✓.

(d) Normal faulting ($\sigma_1$ vertical): dip $= 62.496010^\circ$. Thrust
($\sigma_1$ horizontal): dip $= 27.503990^\circ$.

---

## ★2

(a) With $C = 0$:

$$\sigma_1' = \sigma_3'\frac{1+\sin\varphi}{1-\sin\varphi}
= 50\frac{1.573576}{0.426424} = 184.445889\ \text{MPa}.$$

(b) From equation (7) of the lesson, $\sigma_1' = \sigma_3'\tan^2(45^\circ+\varphi/2)
+ 2C\tan(45^\circ+\varphi/2)$, so the cohesion appears **only** through the term
$2C\tan(45^\circ+\varphi/2)$ added to the cohesionless failure stress.

(c) $2(15)\tan(62.496010^\circ) = 57.619667$ MPa, and
$242.065556 - 184.445889 = 57.619667$ MPa ✓ — identical.

(d) $\tan^2(45^\circ+\varphi/2) = 3.688918$ here, so the friction term multiplies
$\sigma_3'$ while cohesion adds a constant. At 10 km with hydrostatic pore
pressure the effective normal stress is of order 150 MPa, so the frictional term
contributes $0.7\times150 \approx 105$ MPa against a cohesion of 15 MPa.
**Friction dominates at depth**; cohesion matters only near the surface (where
$\sigma_n' \to 0$) and in intact-rock strength, not in fault reactivation. That is
why crustal-strength models usually set $C = 0$ for pre-existing faults.

---

## ★3

(a) With $C = 0$, failure requires $\tau = \mu\sigma_n'$, which gives

$$\sigma_1' = \sigma_3'\frac{1+\sin\varphi}{1-\sin\varphi}
= 100\frac{1.514496}{0.485504} = 311.942845\ \text{MPa}.$$

Mohr circle: centre $= (311.942845+100)/2 = 205.971423$ MPa, radius
$= (311.942845-100)/2 = 105.971423$ MPa.

*Consistency check on the tangency:* the perpendicular distance from the centre to
the line $\tau = 0.6\sigma_n$ is $0.6(205.971423)/\sqrt{1.36} = 105.971423$ MPa,
**exactly** the radius ✓. If $\sigma_1'$ were larger, the circle would cut the line
(the state would already have failed).

(b) At the tangent point ($2\theta = 90^\circ+\varphi = 120.963757^\circ$):

$$\sigma_n' = 205.971423 + 105.971423\cos(120.963757^\circ) = 151.449576\
\text{MPa},$$
$$\tau = 105.971423\sin(120.963757^\circ) = 90.869745\ \text{MPa},$$
$$\mu\sigma_n' = 0.6(151.449576) = 90.869745\ \text{MPa}$$

— equal to 1.5×10⁻⁸ Pa, i.e. round-off ✓. The normal is at
$45^\circ+\varphi/2 = 60.481878^\circ$ from $\sigma_1$ and the plane is inclined
$29.518122^\circ$ to $\sigma_1$.

(c) The maximum shear stress over all planes is the circle radius,
$105.971423$ MPa, attained at $2\theta = 90^\circ$, i.e. $\theta = 45^\circ$ from
$\sigma_1$. There $\sigma_n' = 205.971423$ MPa and
$\mu\sigma_n' = 123.582854$ MPa $> \tau = 105.971423$ MPa, so **the friction law is
not satisfied** on the maximum-shear plane.

(d) Because failure requires the *combination* $\tau - \mu\sigma_n'$ to reach $C$,
and moving from $\theta = 45^\circ$ towards $\varphi$-controlled orientation reduces
$\tau$ slightly (by a factor $\cos\varphi = 0.857$) while reducing $\mu\sigma_n'$
more (the normal stress falls by $r\sin\varphi = 54.5$ MPa), so the net
$\tau-\mu\sigma_n'$ increases. The failure plane trades a little shear for a
substantially lower normal stress — the geometric content of the
$45^\circ\pm\varphi/2$ result.

---

## ★4

(a)

$$\mu = \mu_* + a\ln\frac{V}{V_*} + b\ln\frac{V_*\theta}{D_c}, \qquad
\frac{\mathrm d\theta}{\mathrm dt} = 1 - \frac{V\theta}{D_c} .$$

(b) At steady state $\mathrm d\theta/\mathrm dt = 0$, so $V\theta/D_c = 1$ and
$\theta_{ss} = D_c/V$ ✓ — the state variable is the ratio of the characteristic
slip distance to the slip rate, i.e. a timescale.

(c) Substituting $\theta = D_c/V$ into the friction law:

$$\mu_{ss}(V) = \mu_* + a\ln\frac{V}{V_*} + b\ln\frac{V_*(D_c/V)}{D_c}
= \mu_* + a\ln\frac{V}{V_*} - b\ln\frac{V}{V_*}
= \mu_* + (a-b)\ln\frac{V}{V_*} . \ \square$$

(d) $a > b$: velocity **strengthening** — steady-state friction rises with slip
rate, which resists acceleration and stabilises sliding. Geological consequence:
the fault creeps, produces slow slip or aseismic slip, and does not nucleate
earthquakes. $a < b$: velocity **weakening** — friction falls with slip rate, a
positive feedback that promotes acceleration. Geological consequence: the patch can
nucleate stick-slip earthquakes (provided the loading stiffness is below $k_c$),
and it is the standard explanation for the seismogenic zone. Since $a$ and $b$
depend on temperature, mineralogy and fluid content, the same fault can be
weakening in one depth interval and strengthening in another.

---

## ★5

(a) $C = 20$ MPa, $\mu = 0.60$, $\varphi = 30.9638^\circ$,
$\sigma_3' = 100$ MPa $\Rightarrow$ $\sigma_1' = 382.590461$ MPa. The scan over
9001 plane orientations gives
$\max(\tau-\mu\sigma_n-C) = -3.541570\times10^{-1}$ Pa.

(b) The scan locates the optimum where the plane's **normal** lies
$60.4800^\circ$ from $\sigma_1$, and the plane itself is inclined
$29.5200^\circ$ to $\sigma_1$. Analytic values:
$45^\circ+\varphi/2 = 60.4819^\circ$ (normal from $\sigma_1$) and
$45^\circ-\varphi/2 = 29.5181^\circ$ (plane to $\sigma_1$). Agreement to
$0.0019^\circ$.

(c) The residual is not exactly zero because the scan samples $\theta$ on a grid of
$0.01^\circ$ ($\pi/9000$ rad), and the residual varies quadratically about the
optimum. With a grid spacing $\Delta\theta$ the maximum of a smooth function is
underestimated by of order $\tfrac12|f''|\Delta\theta^2$; the observed
$-0.354$ Pa is $-3.5\times10^{-7}$ of $C$, consistent with a quadratic
discretisation error. Refining the grid by a factor of 10 should reduce it by
a factor of 100 — that is the correct convergence test for this calculation.

(d) The criterion says failure occurs where the stress circle reaches the friction
line. That contact happens at exactly one pair of points, whose orientation is
fixed by the radius-to-line geometry: the radius to the contact point is
perpendicular to the line, so $2\theta = 90^\circ+\varphi$ regardless of
$\sigma_1$ and $\sigma_3$. The "prediction" of the fault dip is therefore not a
separate law but a restatement of the geometry — which is why changing the stress
magnitudes changes the failure stress but *not* the predicted dip.

---

## ★6

(a)

| depth | $\sigma_v$ (MPa) | $\sigma_n'$ (MPa) | $\tau$ (MPa) |
|---|---|---|---|
| 2 km | 52.974 | 33.354 | 20.012 |
| 30 km | 794.610 | 500.310 | 300.186 |

Slope $= (300.186-20.012)/(30-2) = 10.006$ MPa km⁻¹.

(b) $\mu(\rho-\rho_w)g = 0.6(2700-1000)(9.81) = 1.0006\times10^{4}$ Pa m⁻¹
$= 10.006$ MPa km⁻¹ ✓ (Pa m⁻¹ and MPa km⁻¹ are numerically equal).

(c) $\tau = 100$ MPa at $z = 100/10.006 = 9.994$ km. Note the assumption: the
normal stress on the fault was taken equal to the vertical stress, which is exact
for a horizontal plane. For a dipping fault the normal stress is
$\sigma_n = \sigma_v\cos^2\delta + \sigma_h\sin^2\delta$, so the value above is an
*envelope* of the brittle strength, not the strength of a particular plane, and the
horizontal stress must be specified before a specific fault's strength can be
evaluated.

(d) Four things needed before quoting a transition depth: (i) the **geotherm**, or
equivalently the surface heat flow, thermal conductivity and radiogenic heating;
(ii) the **strain rate** or the imposed stress, since ductile strength is
strain-rate sensitive; (iii) the **mineralogy and grain size** of the deforming
rock, since quartz, feldspar and olivine have different flow laws and different
temperature sensitivities; (iv) the **pore pressure** (hydrostatic, overpressured
or dry), since it shifts the brittle envelope. The demo's table is the brittle half
only; without a flow law there is nothing to intersect it with, and the transition
is defined by the intersection. Published range for quartz-rich continental crust
is of order ten to twenty kilometres, but it is a range across assumptions, not a
constant.

---

## ★7

(a) $\sigma = 100$ MPa, $a = 0.010$, $b = 0.014$, $D_c = 10^{-5}$ m,
$V_{\text{pl}} = 10^{-9}$ m s⁻¹, $V_* = 10^{-6}$ m s⁻¹.
$k_c = \sigma(b-a)/D_c = 10^{8}(0.004)/10^{-5} = 4.0\times10^{10}$ Pa m⁻¹
$= 4.0\times10^{4}$ MPa m⁻¹.

(b) Final/initial perturbation after $3\times10^{5}$ s
$= 30\,D_c/V_{\text{pl}}$:

| $k/k_c$ | ratio | verdict |
|---|---|---|
| 0.2 | 3.543797 | GROWS |
| 0.9 | 1.215609 | GROWS |
| 1.1 | 1.011795 | GROWS |
| 5.0 | $3.736788\times10^{-11}$ | decays |

The transition lies between $k/k_c = 1.1$ and 2.0; note that the growth at 0.9 is
*smaller* than at 0.5 (1.22 against 37.4) because as $k \to k_c$ the growth rate
vanishes — the ordering of the ratios is a property of the eigenvalue magnitude,
not of stability.

(c) Measured threshold: $k = 3.6201\times10^{10}$ Pa m⁻¹ $= 0.905036\,k_c$. Exact
linearised trace at $k/k_c = 1.00$: $T = 1.355253\times10^{-20}$ s⁻¹ — zero to
round-off, so the exact threshold is $k_c$ ✓.

(d) Both eigenvalues pass through zero at $k_c$ (the trace changes sign there, and
$D>0$ throughout). Near the threshold the perturbation therefore grows
*algebraically* rather than exponentially over any finite window: at
$k/k_c = 1.1$ the amplitude changes by only 1.2 per cent in $3\times10^5$ s, which
is comparable with the truncation error of the explicit integrator. A bisection on
the sign of the growth ratio can therefore localise the threshold only to the
accuracy with which a marginal mode can be distinguished from numerical error. The
measured $0.905\,k_c$ should be reported as "consistent with $k_c$ within the
resolution of the measurement"; the *exact* value comes from the linearisation, and
the simulation's role is to confirm the unambiguous verdicts far from the threshold
(11 orders of magnitude at $k/k_c = 5$).

---

## ★8

(a) $k_c = \sigma'(b-a)/D_c = 150\times10^{6}(0.004)/20\times10^{-6}
= 3.0\times10^{10}$ Pa m⁻¹ $= 3.0\times10^{4}$ MPa m⁻¹.

(b) With $k \approx \mu/r$ (a **scaling estimate**; the exact elastic stiffness of a
circular patch involves a geometrical factor of order $0.5$–$2$ depending on the
loading configuration, and $\mu$ here is the rock's shear modulus, 30 GPa):
$r_c = \mu/k_c = 30\times10^{9}/3.0\times10^{10} = 1.0$ m.

(c) $k$ **decreases** as the patch grows ($k \propto 1/r$), so patches *larger* than
about 1 m have $k < k_c$ and tend to slip unstably, while smaller patches have
$k > k_c$ and slip stably. This is the standard argument for a minimum nucleation
size: a patch must be big enough that the surrounding elastic stiffness is softer
than the friction law's weakening rate.

(d) $k_c \propto 1/D_c$, so $D_c$ ten times larger gives
$k_c = 3.0\times10^{9}$ Pa m⁻¹, a factor of ten smaller, and
$r_c = 30\times10^{9}/3.0\times10^{9} = 10$ m — a ten times larger nucleation patch.

*Implication and honesty note.* Laboratory values of $D_c$ are typically microns,
which with these parameters predict nucleation patches of metres. Earthquake
observations imply much larger values ($\sim$centimetres to a metre, and
scale-dependent), which give nucleation sizes of hundreds of metres to kilometres,
in better agreement with the inferred dimensions of earthquake nucleation zones.
The discrepancy between laboratory and inferred $D_c$ is a long-standing open
problem, and any statement of a nucleation size must state which $D_c$ it used.
The $k \sim \mu/r$ relation used above is a scaling estimate, not an exact result.

---

## ★9

(a) $V = 30\ \text{mm yr}^{-1} = 30\times10^{-3}/3.15576\times10^{7} =
9.505703\times10^{-10}$ m s⁻¹.

(i) At 10 km, from the envelope of section 3.4:
$\tau = 0.6(2700-1000)(9.81)(10^{4}) = 100.062$ MPa, so

$$q = \tau V = (100.062\times10^{6})(9.505703\times10^{-10}) = 9.5116\times10^{-2}
\ \text{W m}^{-2} = 95.116\ \text{mW m}^{-2} .$$

(ii) Over a 2–12 km brittle zone the profile gives
$\tau(2\ \text{km}) = 20.012$ MPa and $\tau(12\ \text{km}) = 120.074$ MPa, average
$\bar\tau = 70.043$ MPa, so

$$q = \bar\tau V = 6.6581\times10^{-2}\ \text{W m}^{-2} = 66.581\ \text{mW m}^{-2} .$$

(b) For the comparison, a commonly used representative continental heat flow is of
order $60$–$70$ mW m⁻² (a round figure: 65 mW m⁻²). Taken at face value, the two
numbers above are of the *same order* as the entire background heat flow, and the
10-km value *exceeds* it. The expected signature of a strong fault is therefore a
localised heat-flow **high** of order tens of mW m⁻² along the fault trace,
superimposed on the regional background, and detectable because it would be
narrow and linear.

*The comparison is not like-for-like, and this matters.* $q = \tau V$ is the heat
generated per unit **fault area**; a fault is a narrow source, so the surface
heat-flow anomaly is smeared and reduced relative to $q$, by a factor that depends
on the fault width, the depth of the brittle zone and the thermal diffusivity. A
proper test requires a conductive heat-transfer calculation with the fault as a
finite-width source, not a comparison of $q$ with the background. The order of
magnitude is nevertheless the physical point: a strong fault is a large heat
source, and **the widely reported observation is that heat-flow profiles across
major faults do not show an anomaly of this size.** That observational statement
is a literature claim — it is stated here as commonly reported, and it is not
reproduced or verified in this repository.

(c) and (e) Mechanisms proposed, with one discriminating observation each:

1. **High pore pressure** (so that $\sigma_n'$, hence $\tau$, is much lower than the
   lithostatic estimate). *Support:* direct measurements of near-lithostatic pore
   pressure in some fault zones, and the failure of otherwise stable regions to
   explain observed weak fault strength. *Falsify:* measurements showing
   hydrostatic pore pressure at seismogenic depth on the same fault.
2. **Weak fault-zone minerals** (clays, serpentine, talc, graphite) with
   $\mu \approx 0.1$–0.2. *Support:* fault-gouge mineralogy analyses reporting such
   phases in the principal slip zones. *Falsify:* recovered gouge dominated by
   quartz and feldspar with no weak phases.
3. **Dynamic weakening during slip** (flash heating, thermal pressurisation,
   gelation), so that the *average* friction over the seismic cycle is low even
   though static friction is high. *Support:* laboratory friction experiments
   showing large weakening at high slip rates. *Falsify:* evidence that heating is
   small at natural slip rates, or heat-flow data implying a short high-friction
   phase that is nonetheless detectable.
4. **Underestimation of heat flow** by advection or by measurement artefacts (for
   example, groundwater flow redistributing heat away from the fault).
   *Support:* hydrological models reproducing the flat profiles.
   *Falsify:* measurements at sites with no possible advective escape.

(d) The estimate rests on: $\mu = 0.6$ (Byerlee), $\rho = 2700$ kg m⁻³,
hydrostatic pore pressure, $V = 30$ mm yr⁻¹, and the normal stress being the
vertical stress. Halving $\mu$ halves $q$; halving $V$ halves $q$; high pore
pressure can reduce $\sigma_n'$ by a factor of two or more, hence $q$
proportionally. So the *strong-fault* prediction can be brought down to
$\sim$10–20 mW m⁻² — comparable with the observational upper bounds — by assuming
any one of these effects. **That is the paradox's real content: the heat-flow
bound constrains the product $\mu\sigma_n' V$, and it cannot by itself distinguish
among the mechanisms in (c).** Distinguishing them requires mineralogy,
pore-pressure measurement or high-rate friction experiments.

---

## ★10

(a) $k_c = \sigma'(b-a)/D_c$ with $\sigma' = 100$ MPa, $D_c = 10\ \mu$m:

- weakening patch: $b-a = +0.004$ $\Rightarrow$
  $k_c = 10^{8}(0.004)/10^{-5} = 4.0\times10^{10}$ Pa m⁻¹ (positive: instability
  possible).
- strengthening patch: $b-a = -0.006$ $\Rightarrow$
  $k_c = -6.0\times10^{10}$ Pa m⁻¹.

A *negative* $k_c$ means the criterion $k < k_c$ cannot be satisfied for any
positive stiffness: the strengthening patch cannot nucleate unstable slip. It only
slides stably.

(b) The stress drop implied by the full weakening is
$\Delta\tau = \sigma'(b-a) = 10^{8}(0.004) = 0.4$ MPa, and the corresponding slip
$a_{\text{sw}} = D_c = 10\ \mu$m if the weakening proceeds over one $D_c$. More
generally $\Delta\tau = k_c D_c$ — a restatement of the definition — so the
weakening distance is set directly by $D_c$: this is why $D_c$ is often called the
slip-weakening distance, and why the nucleation patch size ($\mu/k_c \propto D_c$)
is proportional to it.

(c) The strengthening patch acts as a **stiffer** element in series with the
weakening one: to move the weakening patch, the strengthening patch must also slip,
and its friction *increases* with rate, which opposes acceleration. The effective
stiffness seen by the weakening patch is therefore **higher** (equivalently the
effective weakening rate $(b-a)$ is reduced), which raises the effective $k_c$
threshold and makes instability harder to reach. Observable consequences: a
weakening patch adjacent to a strengthening patch requires a larger patch, a larger
stress drop, or a larger effective $\sigma'$ to nucleate; and this is one of the
standard explanations for why some faults produce only slow slip — a small
weakening patch surrounded by strengthening material can slide slowly and stably
instead of running away.

(d) **Numerical experiment.** Two blocks, positions $x_1$, $x_2$, each with its own
rate-and-state law (the two parameter sets above), each loaded through its own
spring of stiffness $k$ from the same driver at $V_{\text{pl}}$, and coupled to each
other by a spring of stiffness $k_{12}$ (series and parallel combinations can be
built by choosing which springs exist). Integrate

$$\frac{\mathrm d\tau_i}{\mathrm dt} = k\left(V_{\text{pl}} - V_i\right) + k_{12}
\left(V_j - V_i\right), \qquad i \neq j,$$

with $\tau_i = \mu_i(V_i,\theta_i)\sigma'$ and the state evolution of equation (9).
**Measure:** (i) the maximum slip rate reached by block 1 as a function of
$k_{12}$ at fixed $k$; (ii) the boundary in $(k_{12}, k)$ space between decaying,
slow-slip (bounded, accelerating then decelerating) and runaway behaviour;
(iii) whether the strengthening patch ever slips faster than $V_{\text{pl}}$, and
by how much. Predict in advance, from (c), that increasing $k_{12}$ raises the
stiffness of the weakening block's loading and moves the boundary towards
requiring lower $k$ (softer loading) for instability. **Caveat:** whether a
two-block model reproduces the full behaviour of a 2-D fault is not obvious; the
model tests the mechanism, not the fault.
