# Solutions — 14-01-03 Hydraulic Head, Darcy's Law and Groundwater Flow

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. All wells and parameters are **SYNTHETIC**.

Lesson: [03 Hydraulic Head, Darcy's Law and Groundwater Flow](../03-hydraulic-head-darcy.md).
Constants: $\rho_w = 1000\ \mathrm{kg\,m^{-3}}$, $g = 9.81\ \mathrm{m\,s^{-2}}$,
$\mu_w = 1.002 \times 10^{-3}\ \mathrm{Pa\,s}$.

---

## ★1 — Head from pressure and elevation

$$\frac{p}{\rho_w g} = \frac{2.50 \times 10^{5}}{1000 \times 9.81}
= 25.484\ \mathrm{m}, \qquad h = z + \frac{p}{\rho_w g} = -15.0 + 25.484
= +10.484\ \mathrm{m}.$$

At the water table $p = 0$, so $h = z = -8.000\ \mathrm{m}$.

**One sentence:** head is the elevation to which water would rise in a piezometer,
which is a statement about energy, while a depth is a statement about position —
they coincide only where the pressure is atmospheric.

Note the ordering of the two answers: the deeper point ($z = -15$ m) has the
*higher* head (+10.48 m) and the shallower point ($z = -8$ m) has the lower head
(−8.00 m). If those two points were connected, water would flow from 15 m depth
upwards towards 8 m depth. Head, not depth, decides the direction.

---

## ★2 — Gradient, flux, velocity and travel time

$$i = \frac{50.00 - 49.25}{300} = \frac{0.75}{300} = 2.50 \times 10^{-3},$$
$$q = K i = 8.0 \times 10^{-6} \times 2.50 \times 10^{-3}
= 2.00 \times 10^{-8}\ \mathrm{m\,s^{-1}}
= 1.728 \times 10^{-3}\ \mathrm{m\,d^{-1}},$$
$$v = \frac{q}{n_e} = \frac{2.00 \times 10^{-8}}{0.15}
= 1.333 \times 10^{-7}\ \mathrm{m\,s^{-1}}
= 1.152 \times 10^{-2}\ \mathrm{m\,d^{-1}},$$
$$t = \frac{L}{v} = \frac{300}{1.152 \times 10^{-2}} = 2.604 \times 10^{4}\
\mathrm{d} = 71.3\ \mathrm{yr}.$$

**Interpretation.** A gradient of 2.5 m per km is a healthy natural gradient, and
the tracer still needs 71 years to cross 300 m. Any claim of a contaminant
travelling kilometres in a year requires either a very high $K$ or a gradient far
above the natural range — or a fracture or conduit pathway that Darcy's law does
not describe (which is the point of ★3).

---

## ★3 — Reynolds number

$$\mathrm{Re} = \frac{\rho_w q d}{\mu_w}
= \frac{1000 \times 1.0 \times 10^{-6} \times 5.0 \times 10^{-4}}
{1.002 \times 10^{-3}}
= 4.99 \times 10^{-4}.$$

$\mathrm{Re} = 5 \times 10^{-4} \ll 1$: **Darcy's law is valid**, with an enormous
margin. To reach $\mathrm{Re} = 1$ at $d = 0.5$ mm would require
$q = \mu_w/(\rho_w d) = 1.002 \times 10^{-3}/(1000 \times 5.0 \times 10^{-4})
= 2.0 \times 10^{-3}\ \mathrm{m\,s^{-1}}$, i.e. 173 m d$^{-1}$ of specific
discharge — a flux seen only in gravel, karst or beside a well.

---

## ★★4 — Hydraulic diffusivity

Confined:
$$D = \frac{T}{S} = \frac{100}{2.0 \times 10^{-4}} = 5.0 \times 10^{5}\
\mathrm{m^2\,d^{-1}},$$
$$t = \frac{L^{2}}{4D} = \frac{(2000)^{2}}{4 \times 5.0 \times 10^{5}}
= \frac{4.0 \times 10^{6}}{2.0 \times 10^{6}} = 2.0\ \mathrm{d}.$$

Unconfined, same $T$, $S_y = 0.15$:
$$D = \frac{100}{0.15} = 666.7\ \mathrm{m^2\,d^{-1}}, \qquad
t = \frac{4.0 \times 10^{6}}{4 \times 666.7} = 1500\ \mathrm{d} = 4.11\ \mathrm{yr}.$$

Ratio: $1500/2.0 = 750$. Note that the ratio of times equals the ratio of
storativities ($0.15/2.0 \times 10^{-4} = 750$) — a general and useful result,
because $t = L^2 S/(4T)$ and only $S$ differs.

**Caution on units.** $D$ is in m$^2$ d$^{-1}$ only because $T$ was given in
m$^2$ d$^{-1}$ and $S$ is dimensionless. In SI the answer is
$5.0 \times 10^{5}/86400 = 5.79\ \mathrm{m^2\,s^{-1}}$ for the confined case. If
you report $D$ in m d$^{-1}$ you have treated $S$ as having units.

---

## ★★5 — Dupuit water table

$$R = 0.50\ \mathrm{mm\,d^{-1}} = \frac{0.50 \times 10^{-3}}{86400}
= 5.787 \times 10^{-9}\ \mathrm{m\,s^{-1}}, \qquad
\frac{R}{K} = \frac{5.787 \times 10^{-9}}{1.0 \times 10^{-4}}
= 5.787 \times 10^{-5}.$$

Mid-span, with $x = L/2 = 1000$ m:
$$\Delta u = \frac{R}{K}\left(\frac{L}{2}\right)^{2}
= 5.787 \times 10^{-5} \times 10^{6} = 57.87\ \mathrm{m^2},$$
$$u_{\text{mid}} = 15.0^{2} + 57.87 = 225 + 57.87 = 282.87\ \mathrm{m^2},$$
$$h_{\text{mid}} = \sqrt{282.87} = 16.819\ \mathrm{m},
\qquad \text{rise} = 1.819\ \mathrm{m}.$$

Small-rise approximation:
$$\Delta h \approx \frac{R L^{2}}{8 K h_1}
= \frac{5.787 \times 10^{-9} \times 4.0 \times 10^{6}}
{8 \times 1.0 \times 10^{-4} \times 15.0}
= \frac{2.315 \times 10^{-2}}{1.20 \times 10^{-2}} = 1.929\ \mathrm{m}.$$

Percentage difference: $(1.929 - 1.819)/1.819 = +6.1\%$ — the approximation is
**high**, and worse here than in the lesson's case (3.5%) because the rise is a
larger fraction of $h_1$ (1.82 m on 15 m versus 1.40 m on 20 m).

**What the comparison does not test.** It does not test the Dupuit assumptions
(neglect of vertical flow, hydrostatic vertical pressure distribution, no seepage
face at the outlet). Both expressions are solutions of the *same* depth-averaged
equation; comparing them compares a linearisation with its parent equation, not
the parent equation with the real problem.

---

## ★★6 — Refraction at a conductivity contrast

$$\frac{\tan\theta_2}{\tan\theta_1} = \frac{K_2}{K_1}.$$

Gravel to clay, $\theta_1 = 30^\circ$:
$$\tan\theta_2 = \frac{1.0 \times 10^{-6}}{1.0 \times 10^{-3}}\tan 30^\circ
= 10^{-3} \times 0.57735 = 5.7735 \times 10^{-4},$$
$$\theta_2 = \arctan(5.7735 \times 10^{-4}) = 0.0331^\circ.$$

Clay to gravel, $\theta_1 = 1^\circ$:
$$\tan\theta_2 = \frac{1.0 \times 10^{-3}}{1.0 \times 10^{-6}}\tan 1^\circ
= 10^{3} \times 1.7455 \times 10^{-2} = 17.455,$$
$$\theta_2 = \arctan(17.455) = 86.72^\circ.$$

**Consequence.** Flow leaving a clay into a gravel is bent almost parallel to the
boundary — it becomes a *lateral* flow. That is why a low-conductivity cover
delivers recharge to a permeable layer beneath it as a distributed sheet along the
interface, and why a gravel layer beneath a clay can transmit water many kilometres
without a large head gradient. It is also why the vertical flux through a clay
blanket is controlled almost entirely by the clay's $K$ and thickness, while the
lateral drainage is controlled by the gravel's.

---

## ★★★7 — Separating $R$ from $K$ in a synthetic basin

The lesson's non-uniqueness is that the Dupuit head solution depends on $R$ and $K$
only through $R/K$. Two independent measurements are needed: one for the ratio, one
for an absolute scale.

**Leg 1 — the head field gives $R/K$.** From
$u = h_1^{2} + (R/K)x(L-x)$, a mid-span rise of $\Delta h$ over a strip of length
$L$ gives
$$\frac{R}{K} = \frac{4\left[(h_1 + \Delta h)^{2} - h_1^{2}\right]}{L^{2}}
\approx \frac{8 h_1 \Delta h}{L^{2}}.$$
For $h_1 = 30$ m and $L = 5000$ m, resolving $\Delta h = 0.30$ m (achievable with
survey-grade levelling over 5 km, differential GNSS, or a pair of pressure
transducers with a common datum) gives
$$\frac{R}{K} \approx \frac{8 \times 30 \times 0.30}{2.5 \times 10^{7}}
= 2.88 \times 10^{-6}.$$
Note the precision requirement is on the **difference of two heads**, so a shared
datum error cancels: put both sensors on the same benchmark network.

**Leg 2 — a discharge measurement gives $R$.** In the 1-D balance the total
recharge per unit width is $RL$; for a basin of width $W$, the total is $R L W$.
With $W = 2000$ m and a target resolution of $1\ \mathrm{mm\,yr^{-1}}$
$= 3.17 \times 10^{-11}\ \mathrm{m\,s^{-1}}$,
$$Q = R L W = 3.17 \times 10^{-11} \times 5000 \times 2000
= 3.17 \times 10^{-4}\ \mathrm{m^3\,s^{-1}} = 0.317\ \mathrm{L\,s^{-1}},$$
which is 27 m$^3$ d$^{-1}$. A stream gauging station or a weir resolves this
comfortably, but the *difference* between two stations must be resolvable, so the
gauges must be accurate to better than 0.3 L s$^{-1}$ on a baseflow of perhaps
tens of litres per second — i.e. to about 1% of the baseflow. In practice this
means a calibrated weir or a salt-dilution gauge, not a rating curve.

**Leg 3 — an independent $K$ from a pumping test.** From
[04 Well Hydraulics](../04-well-hydraulics.md), a constant-rate test gives $T$ and $S$
from the drawdown curve. With $T$ known, $K = T/b$; combined with Leg 1 that gives
$R$ a second time, which is the cross-check.

**Cross-check design.** Legs 2 and 3 are independent: the discharge measurement is
affected by any unmeasured flux (a losing stream reach, evapotranspiration from the
riparian zone, an unmapped abstraction) but *not* by the well-test assumption of
homogeneity; the well test is affected by local heterogeneity and well losses but
not by the basin-scale water balance. Agreement within $20\%$ between the two
estimates of $R$ is meaningful evidence; disagreement localises the missing flux.

**Systematic errors.** Leg 1: a single datum for both sensors is mandatory, and an
unmapped regional gradient can be mistaken for a recharge mound. Leg 2: bank
storage and diurnal evapotranspiration contaminate the difference between gauges —
use night-time baseflow and a multi-week average. Leg 3: partial penetration and
well losses inflate the apparent $K$; a step-drawdown test isolates them.

---

## ★★★8 — What the machine-precision agreement proves

**What it proves.** That the linear system built for $u = h^{2}$ is a correct
discretisation of $u'' = -2R/K$ with the stated boundary conditions, and that the
linear solve, the exact-solution evaluation and the boundary-flux evaluation are
all implemented consistently. It is a *code verification* result: a bug in the
algebra, the assembly, the indexing or the boundary condition would break it. The
agreement at $6.4 \times 10^{-14}$ m on values of order 20 m is consistent with
round-off accumulation in double precision (relative error
$\sim 3 \times 10^{-15}$).

**What it does not prove.** It does not validate the *model*: both curves come from
the same depth-averaged equation. Dupuit's neglect of vertical flow, the
hydrostatic vertical pressure assumption, the absence of a seepage face, the
assumption of spatially uniform $R$ and $K$ — none of these is tested, and the
verification would pass unchanged if any of them were badly wrong.

**Grid-convergence test.** Refine the grid with
$n = 41, 81, 161, 321, 641$ nodes ($\Delta x = 25, 12.5, 6.25, 3.125, 1.5625$ m)
and compute $E(\Delta x) = \max_j |u_j - u(x_j)|$ against the exact $u$. The
second-order central difference for $u''$ has truncation error
$O(\Delta x^{2})$, so a correct implementation gives
$$E(\Delta x) \approx C\,\Delta x^{2}, \qquad
p = \log_2\frac{E(\Delta x)}{E(\Delta x/2)} \to 2.0.$$
With $u$ quadratic, the second difference is *exact* for a quadratic function, so
in this particular problem $E$ is at round-off for every $\Delta x$ and $p$ is
meaningless. **That is the point to state**: the parabola test cannot exhibit an
observed order of accuracy because the exact solution is in the scheme's exactness
class. To measure $p$ one must use a problem with a non-polynomial solution, or add
a heterogeneous $K(x)$ so that the operator is no longer exact on quadratics.

**An analytic solution that tests a Dupuit assumption.** The Thiem (radial, steady)
solution for flow to a well,
$$h(r) = h_w + \frac{Q}{2\pi T}\ln\frac{r}{r_w},$$
tests the *radial* geometry and the log-dependence of head on distance — the
solution of the full 2-D Laplace equation, not the depth-averaged 1-D form. It
still assumes horizontal flow, so the strongest test of the neglected vertical
component is a solution of the full 2-D problem (for example a seepage-face
solution at a drained boundary, or a variable-density interface), which requires a
numerical model in $x$ and $z$. The honest chain is: verify the code against an
analytic solution of the *same* equation, then validate the equation against field
data or a higher-dimensional model.

---

## Mastery checkpoint — worked

Synthetic confined unit: $K = 2.0 \times 10^{-5}\ \mathrm{m\,s^{-1}}$,
$b = 20\ \mathrm{m}$, $S = 5.0 \times 10^{-4}$, two piezometers 500 m apart with
$h_1 = 45.00$ m, $h_2 = 44.20$ m, $n_e = 0.20$, $d = 0.4\ \mathrm{mm}$.

**(a) Gradient, flux, velocity.**
$$i = \frac{45.00 - 44.20}{500} = 1.60 \times 10^{-3},$$
$$q = K i = 2.0 \times 10^{-5} \times 1.60 \times 10^{-3}
= 3.20 \times 10^{-8}\ \mathrm{m\,s^{-1}} = 2.765 \times 10^{-3}\
\mathrm{m\,d^{-1}},$$
$$v = \frac{q}{n_e} = \frac{3.20 \times 10^{-8}}{0.20}
= 1.60 \times 10^{-7}\ \mathrm{m\,s^{-1}} = 1.382 \times 10^{-2}\
\mathrm{m\,d^{-1}}.$$

**(b) Travel time over 500 m.**
$$t = \frac{500}{1.60 \times 10^{-7}} = 3.125 \times 10^{9}\ \mathrm{s}
= 3.617 \times 10^{4}\ \mathrm{d} = 99.0\ \mathrm{yr}.$$
This is the transport timescale for the *mean* pathway. In a confined aquifer with
a few fractures, the fast-path time could be orders of magnitude shorter; the Darcy
average says nothing about the tail of the travel-time distribution.

**(c) Reynolds number.**
$$\mathrm{Re} = \frac{\rho_w q d}{\mu_w}
= \frac{1000 \times 3.20 \times 10^{-8} \times 4.0 \times 10^{-4}}
{1.002 \times 10^{-3}} = 1.28 \times 10^{-5} \ll 1.$$
Darcy's law is valid with four orders of magnitude of margin.

**(d) Transmissivity and diffusivity.**
$$T = K b = 2.0 \times 10^{-5} \times 20 = 4.0 \times 10^{-4}\
\mathrm{m^2\,s^{-1}} = 34.56\ \mathrm{m^2\,d^{-1}},$$
$$D = \frac{T}{S} = \frac{4.0 \times 10^{-4}}{5.0 \times 10^{-4}}
= 0.80\ \mathrm{m^2\,s^{-1}} = 6.912 \times 10^{4}\ \mathrm{m^2\,d^{-1}},$$
$$t(5\ \mathrm{km}) = \frac{L^{2}}{4D}
= \frac{(5000)^{2}}{4 \times 0.80} = \frac{2.5 \times 10^{7}}{3.2}
= 7.81 \times 10^{6}\ \mathrm{s} = 90.4\ \mathrm{d}.$$
A pressure disturbance crosses 5 km in about three months. A *water particle* at
$1.6 \times 10^{-7}\ \mathrm{m\,s^{-1}}$ would need
$5000/1.6 \times 10^{-7} = 3.1 \times 10^{10}$ s $= 990$ years. **Pressure and
water move on wildly different timescales in a confined aquifer**, and conflating
them is one of the most consequential errors in groundwater interpretation.

**(e) The "recharge from two heads" claim.** Two heads in a confined aquifer cannot
determine recharge:

1. As the lesson demonstrates, the head solution depends on $R$ and $K$ only
   through $R/K$, so one head difference is one equation with two unknowns.
2. In a *confined* system recharge is not a surface flux at all; it is leakage
   through the overlying confining unit, which is controlled by the vertical
   gradient in that unit and by its vertical conductivity — neither of which the
   two screened piezometers measure.
3. The vertical flux is $q_z = -K_v \,\mathrm{d}h/\mathrm{d}z$; with no measurement
   above the unit, $\mathrm{d}h/\mathrm{d}z$ is simply unknown.

**What to request:** (i) heads in the confining unit, or a nested piezometer
completing the vertical head profile, so that the vertical gradient is measured;
(ii) an independent $K$ or $K_v$ from a pumping test, a packer test, or a borehole
geophysical estimate; (iii) a boundary-flux cross-check (baseflow separation,
streamflow gain, or a chloride mass balance) that measures the actual recharge. Any
one of the three converts the ambiguous statement into a testable one.
