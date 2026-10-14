# Solutions — 02-07-01 Electrostatics, Coulomb's Law and Electric Potential

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

Throughout, $1/(4\pi\varepsilon_0) = 8.987\,551\,787\times10^{9}$
N m² C⁻² and $\varepsilon_0 = 8.854\,187\,812\,8\times10^{-12}$ F/m.

---

## ★1 — Two charges

**(a)** With $q_1 = +3$ nC at the origin and $q_2 = -2$ nC at $0.04$ m, the
distances from $\mathbf r = (0,0.03,0)$ are $r_1 = 0.03$ m and
$r_2 = \sqrt{0.04^2+0.03^2} = 0.05$ m. The field components are

$$E_x = \frac{q_1}{4\pi\varepsilon_0}\frac{x-x_1}{r_1^3}
+ \frac{q_2}{4\pi\varepsilon_0}\frac{x-x_2}{r_2^3}
= 0 + 8.9876\times10^9\frac{(-2\times10^{-9})(-0.04)}{0.05^3} = 5752.03\ \mathrm{V/m},$$

$$E_y = 8.9876\times10^9\left[\frac{3\times10^{-9}(0.03)}{0.03^3}
+ \frac{(-2\times10^{-9})(0.03)}{0.05^3}\right]
= 8.9876\times10^9(1.111\times10^{-4} - 4.8\times10^{-6})
= 25\,644.48\ \mathrm{V/m},$$

and $E_z = 0$. The magnitude is $\sqrt{5752.03^2 + 25644.48^2}
= 26\,281$ V/m. The potential is

$$V = 8.9876\times10^9\left(\frac{3\times10^{-9}}{0.03}
- \frac{2\times10^{-9}}{0.05}\right) = 8.9876(100 - 40) = 539.25\ \mathrm{V}.$$

**(b)** On the axis, both contributions to $E_x$ have the *same* sign for
$0 < x < 0.04$ (both point in $+x$), so no cancellation is possible between the
charges. Cancellation happens only beyond the smaller charge, where

$$\frac{3\times10^{-9}}{x^2} = \frac{2\times10^{-9}}{(x-0.04)^2}
\ \Longrightarrow\ \sqrt3\,(x-0.04) = \sqrt2\,x
\ \Longrightarrow\ x = \frac{0.04\sqrt3}{\sqrt3-\sqrt2} = 0.217\,980\ \mathrm m .$$

There is exactly one such point because the left side of $E_x = 0$ is monotonic in
$x$ on each of the three regions; on $x<0$ the fields also oppose but the required
equality has no positive solution, and as $x\to\infty$ the field tends to that of
the net charge $+1$ nC and never vanishes. The demo's scan of the exact field gives
$E_x = 0.000$ V/m at that point.

**(c)** $V = 8.9876\times10^9\left(\frac{3\times10^{-9}}{0.217980}
- \frac{2\times10^{-9}}{0.177980}\right) = 22.698$ V. Note that $V \neq 0$ at the
null of $\mathbf E$: a vanishing *gradient* says nothing about the value.

**(d)** $V(0.06) = -449.3776$ V and $V(0.10) = -29.9585$ V, so
$W = q\Delta V = 10^{-9}\times(-29.9585 + 449.3776) = 4.194\times10^{-7}$ J. The
work is positive because the test charge is repelled by the net positive charge
and must be pushed inward.

---

## ★2 — Shell, line, and which model applies where

**(a)** Gauss's law with spherical symmetry gives $E = 0$ for $r<a$,
$E = Q/(4\pi\varepsilon_0a^2)$ *at* $r = a$ (the field of the surface charge
density, $\sigma/(2\varepsilon_0)$), and $E = Q/(4\pi\varepsilon_0r^2)$ for $r>a$.

**(b)** At $r = a = 0.5$ m:
$E = 8.9876\times10^9\times10^{-9}/(2\times0.25) = 17.9751$ V/m. At $r = 1$ m:
$E = 8.9876\times10^9\times10^{-9}/1 = 8.9876$ V/m. The point-charge value at
$r = a$ would be 35.9502 V/m — exactly **twice** the shell value, because at the
surface half the shell's charge lies "outside" every local patch of surface. The
demo reproduces all three numbers to six digits from a direct surface integral.

**(c)** For an infinite line, $\mathbf E$ is radial with
$E = \lambda/(2\pi\varepsilon_0s) = 2\times10^{-9}/(2\pi\times8.8542\times10^{-12}
\times0.05) = 719.0$ V/m. The assumption is that the line is infinite — the
parameter that must be checked is $L/s$.

**(d)** The infinite-line (cylindrical) model is the borehole model: a long
electrode in a well is well approximated by a line or cylinder. The spherical
model fails in a borehole because the geometry is not spherical; conversely, the
line model fails for a surface electrode, whose current spreads
three-dimensionally.

---

## ★3 — Image charge

**(a)** The image configuration is $+q$ at $(0,0,+d)$ and $-q$ at $(0,0,-d)$. On
the plane $z = 0$ every field point is equidistant from the two charges, so the
two contributions to $V$ are equal and opposite: $V = 0$ exactly, for all $x,y$.
The demo prints $V = 0.000\times10^{0}$ V at four points.

**(b)** The field of the image at the position of the real charge is
$\mathbf E_{\text{im}} = -\frac{q}{4\pi\varepsilon_0(2d)^2}\hat{\mathbf z}$, so
$F = qE_{\text{im}} = -\frac{q^2}{16\pi\varepsilon_0d^2}
= -\frac{(2\times10^{-9})^2\times8.9876\times10^9}{4(0.01)^2}
= -8.9876\times10^{-5}$ N, attractive, matching the closed form quoted by the
demo.

**(c)** There is no gravitational image because there is no negative mass and no
material that screens gravity: the equivalence principle guarantees that every
mass responds to gravity identically, so no arrangement of matter can produce the
boundary condition $\Phi = 0$ on a plane in the way a grounded conductor does for
$V$.

**(d)** The method requires $V = 0$ on the surface, which requires the surface to
be an equipotential maintained by free charge — a conductor. A dry resistive rock
plane carries no free surface charge and does not enforce $V = 0$; the correct
treatment is then a dielectric boundary condition with $\varepsilon_1 \ne
\varepsilon_2$, which changes the field by a factor depending on the permittivity
ratio rather than removing it.

---

## ★4 — Harmonic potentials

**(a)** With $V = A/r$, $A = q/(4\pi\varepsilon_0)$:
$\mathrm dV/\mathrm dr = -A/r^2$, $r^2\mathrm dV/\mathrm dr = -A$,
$\mathrm d(-A)/\mathrm dr = 0$, so $\nabla^2V = 0$ for $r\neq0$. Numerically the
demo reports $-3.6\times10^{-12}$, $0$, $0$ V/m² at $r = 0.1, 0.5, 2$ m — the
residual at $r = 0.1$ is double-precision round-off in a difference of terms of
order $A/r^3$.

**(b)** The mean-value property: for a harmonic function, the average of $V$ over
any sphere containing no source equals $V$ at the centre. Numerically, for a
$+1$ nC charge 0.1 m from the sampling sphere's centre and $R = 0.05$ m, the mean
is $89.875\,517\,923$ V against a centre value of $89.875\,517\,923$ V — ratio
**1.000000000**. The property is exact, and the discretisation is the only
limitation.

**(c)** A finite-difference Laplacian of a smooth function has truncation error
$\tfrac{h^2}{12}V''''+O(h^4)$. With $V'''' = 24A/r^5$ this predicts
$5.752\times10^{-4}$ V/m² at $r = 0.5$ m, $h = 10^{-3}$ m, and the demo observes
$5.752\,123\times10^{-4}$. Halving $h$ reduces it by exactly 4.00. The non-zero
value is a property of the *scheme*, not of the potential; the diagnostic is the
$h^2$ scaling, which round-off does not show.

---

## ★5 — Finite versus infinite line

**(a)** The bracket is $L/\sqrt{s^2+L^2} = \left(1+s^2/L^2\right)^{-1/2} \to 1$.
At $L = s$ it is $1/\sqrt2 = 0.707\,106\,8$; at $L = 10s$ it is
$10/\sqrt{101} = 0.995\,037$, i.e. a 0.5 % shortfall.

**(b)** $L = 0.5$ m and $s = 0.5$ m gives $L/s = 1$, so the correction factor is
$1/\sqrt2$: the infinite-line model **overestimates** the field by 41 %. It is
emphatically not adequate.

**(c)** The demo's $L$ is the *half-length*: it reports 0.7071 at $L = 0.05$ m with
$s = 0.05$ m, i.e. $L/s = 1$, and 0.9950 at $L = 0.5$ m, i.e. $L/s = 10$. Both
agree with (a) to the printed digits.

**(d)** Require $L/s\gtrsim10$ for a 0.5 % error, and $L/s\gtrsim30$ for
0.05 %. State the tolerance you need, because the criterion is entirely a
tolerance statement.

---

## ★6 — Dipole

**(a)** $p = q\times2d = 10^{-9}\times0.02 = 2\times10^{-11}$ C m.

**(b)** On the perpendicular bisector (the equatorial plane) of the pair, both
charges are equidistant from every field point, so $V = 0$ **exactly** there. The
field, however, does not vanish: the two contributions are equal in magnitude and
both point along $-\mathbf p$. Writing the standard dipole forms

$$V = \frac{p\cos\theta}{4\pi\varepsilon_0r^2},
\qquad
\mathbf E = \frac{1}{4\pi\varepsilon_0r^3}\left[3(\mathbf p\cdot
\hat{\mathbf r})\hat{\mathbf r}-\mathbf p\right],$$

the magnitude on the equator ($\theta = \pi/2$) is $p/(4\pi\varepsilon_0r^3)$
and on the axis is twice that. So the potential falls as $r^{-2}$ and the field as
$r^{-3}$: one power of $r$ faster than a monopole, because the two charges cancel
in the leading term.

**(c)** At $r = 0.1$ m:
$E = 2\times10^{-11}\times8.9876\times10^9/10^{-3} = 179.75$ V/m; the exact
two-charge value is $177.09$ V/m, ratio $0.9852$ — the demo's number. At
$r = 2$ m: $E = 2\times10^{-11}\times8.9876\times10^9/8 = 0.022\,469$ V/m against
an exact $0.022\,468$ V/m, ratio 1.0000.

**(d)** On the axis, the two fields add along the axis and the far-field amplitude
is $2p/(4\pi\varepsilon_0r^3)$; on the equator they partly cancel and the amplitude
is $p/(4\pi\varepsilon_0r^3)$. Ratio 2, with the equatorial field directed
*opposite* to $\mathbf p$. The demo's loop-field table shows the ratio approaching
$-2$ from $-1.0374$ at $r/a = 2$ to $-1.9995$ at $r/a = 100$.

---

## ★7 — Charged ring

**(a)** With $\mathrm dq = \lambda a\,\mathrm d\phi$ at distance
$\sqrt{a^2+z^2}$ from the on-axis point:

$$V(z) = \frac{1}{4\pi\varepsilon_0}\frac{Q}{\sqrt{a^2+z^2}},
\qquad
E_z(z) = -\frac{\mathrm dV}{\mathrm dz} = \frac{Qz}{4\pi\varepsilon_0(a^2+z^2)^{3/2}} .$$

**(b)** At $z = a$: $V = 8.9876\times10^9\times10^{-9}/(0.1\sqrt2) = 63.552$ V and
$E_z = 8.9876\times10^9\times10^{-9}\times0.1/(0.02)^{3/2} = 317.76$ V/m.

**(c)** For $z\ll a$, $V\to Q/(4\pi\varepsilon_0a)$ (constant) and $E_z\approx
Qz/(4\pi\varepsilon_0a^3)$: a linear restoring force, i.e. a harmonic well, which
is why a charged particle on the axis of a ring executes simple harmonic motion
for small displacements. For $z\gg a$, $V\to Q/(4\pi\varepsilon_0z)$ and
$E_z\to Q/(4\pi\varepsilon_0z^2)$: the ring is a point charge.

**(d)** Off axis the distance to each source element depends on both the source and
field point azimuths, and the resulting integral over $\phi$ is elliptic. The
standard resolution is numerical quadrature — as the demo does for the magnetic
analogue — or a series expansion in multipoles.

---

## ★8 — The gravity comparison

**(a)** $\frac{1/(4\pi\varepsilon_0)}{G} = \frac{8.987\,551\,787\times10^9}
{6.674\,30\times10^{-11}} = 1.346\,591\times10^{20}$. For a body of charge $q$ and
mass $m$, equilibrium under gravity requires $qE = mg$, so
$E = (m/q)g$; for $m/q = 1$ kg/C, $E = g_n = 9.806\,65$ V/m.

**(b)** $[1/(4\pi\varepsilon_0G)] = \mathrm{N\,m^2C^{-2}}/(\mathrm{N\,m^2kg^{-2}})
= \mathrm{kg^2C^{-2}}$. Not dimensionless. The dimensionless statement is the
ratio of forces between two elementary charges of mass $m$, which scales as
$1/m^2$, so the two statements answer different questions and both are correct.

**(c)** Electrostatics *can* be screened because a conductor can redistribute free
charge to cancel an applied field: the image configuration of ★3 is precisely a
constructive proof that a conducting surface can impose $V = 0$. Gravity cannot be
screened because there is nothing to redistribute — mass is one-signed and the
equivalence principle makes any local rearrangement of matter irrelevant to the
external field of the whole body.

**(d)** A falsification would be a material that reduces the gravitational field
measured inside a cavity relative to the same geometry without the material
(preserving the total mass budget), or any observed difference in free-fall
acceleration of different substances exceeding the (extremely tight) experimental
bounds. No such observation exists; the equivalence principle has survived tests
at the $10^{-15}$ level and better, which is why the "gravitational shield" appears
in science fiction rather than in this curriculum.

---

## ★9 — Multipole expansion

**(a)** Total charge $= q+q-q-q = 0$. Dipole moment
$\mathbf p = \sum q_k\mathbf r_k = q(d,0)+q(-d,0)-q(0,d)-q(0,-d) = \mathbf 0$.

**(b)** Along $x$: at $(d,0)$, $3x^2-r^2 = 3d^2-d^2 = 2d^2$; at $(-d,0)$ likewise
$2d^2$; at $(0,\pm d)$, $3x^2-r^2 = -d^2$ and the charge is $-q$, contributing
$+qd^2$ each. Hence

$$D_{xx} = 2qd^2+2qd^2+qd^2+qd^2 = 6qd^2 = 6\times10^{-9}\times10^{-6}
= 6\times10^{-15}\ \mathrm{C\,m^2},$$

and on the $x$-axis

$$V \approx \frac{1}{4\pi\varepsilon_0}\frac{D_{xx}}{2r^3}
= \frac{8.9876\times10^9\times6\times10^{-15}}{2r^3}
= \frac{2.696\,3\times10^{-5}}{r^3}\ \mathrm V .$$

**(c)** The numerical check gives $Vr^3 = 2.7077\times10^{-5}$,
$2.696\,378\times10^{-5}$ and $2.696\,267\times10^{-5}$ V m³ at $r = 0.01$, 0.1 and
1 m, converging to $2.696\,3\times10^{-5}$ V m³ — the analytic value. The units are
V m³ because $Vr^3$ removes the $r^{-3}$ dependence and leaves the quadrupole
strength, which has dimensions of charge × length².

**(d)** Gravity's lowest multipole is the monopole ($GM/r^2$), its quadrupole and
higher terms being at most a few parts in $10^5$ for the Earth; so an anomaly is a
small *relative* perturbation and is naturally expressed as a fractional change of
$g$. Magnetism has no monopole and no (static, external) dipole-free structure:
the field of any localised source is at best dipolar, so an anomaly can be of the
same order as the field it rides on and is naturally reported in absolute units
against the background. In inversion terms, gravity data chiefly constrain the
total excess mass and its distribution, while magnetic data constrain the
distribution of *very* localised magnetisation and are correspondingly more
sensitive to near-surface sources — the standard reason aeromagnetics resolves
shallow structure that gravity cannot.

---

## ★10 — Screening

**(a)** $\tau_e = \varepsilon/\sigma = 6\varepsilon_0/0.01 = 5.31\times10^{-9}$ s.
A free charge placed in the rock is neutralised (its field drives a current that
deposits opposite charge around it) in nanoseconds. Electrostatic fields cannot be
maintained in a conductor.

**(b)** Any charge accumulation produces a field that drives a current opposing the
accumulation, so the equilibrium state of a conducting medium is
$\rho = 0$ in the bulk. Nevertheless a *steady* current field with sources outside
the region obeys $\nabla\cdot\mathbf J = 0$ and
$\mathbf J = \sigma\mathbf E$, giving $\nabla\cdot\mathbf E = 0$, and with
$\nabla\times\mathbf E = 0$ this is Laplace's equation for $V$. The mathematics of
electrostatics survives; its physics does not.

**(c)** An SP anomaly is not a static charge distribution: it is a *source*
distribution of current (electrokinetic, thermoelectric or electrochemical)
driving a steady current field. It is a Poisson problem with a distributed source,
measured as a potential difference at the surface.

**(d)** Place charge $q$ at depth in homogeneous rock: the surrounding conductor
neutralises it within $\tau_e\sim$ nanoseconds, leaving no external field. Place a
*density* excess there: nothing cancels it, because mass is conserved and
one-signed, and the resulting field is a permanent fractional change in $g$ that a
gravimeter can detect. The asymmetry is exactly the "one sign versus two signs"
entry of the analogy table in the lesson.
