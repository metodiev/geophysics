# Solutions — 02-07-02 Magnetostatics, Biot–Savart and Ampère's Law

> **Read this after attempting the exercises, not before.** Values attributed to
> the demo are its actual output.

With $\mu_0 = 1.256\,637\,062\,12\times10^{-6}$ N/A², all results are in tesla
unless stated.

---

## ★1 — Finite and infinite wire

**(a)** With $L = 0.5$ m, $s = 0.1$ m, $I = 5$ A:

$$B = \frac{\mu_0IL}{2\pi s\sqrt{s^2+L^2}}
= \frac{(1.2566\times10^{-6})(5)(0.5)}
{2\pi(0.1)\sqrt{0.01+0.25}} = 9.8058\times10^{-6}\ \mathrm T ,$$

against the infinite-wire value
$B_\infty = \mu_0I/(2\pi s) = 1.0000\times10^{-5}$ T.

**(b)** Ratio $= 0.980\,581$, which is exactly
$L/\sqrt{L^2+s^2} = 0.5/\sqrt{0.26} = 0.980\,581$ ✓. The demo checks the same
identity in the form of a numeric quadrature against the closed form at four
lengths and obtains ratio 1.000000.

**(c)** Require $(L/s)/\sqrt{(L/s)^2+1} = 0.99$. Squaring:
$x^2 = 0.9801(x^2+1)$, so $x^2 = 0.9801/0.0199 = 49.25$ and
$L/s = 7.02$. A 1 % tolerance therefore needs an aspect ratio of about 7.

**(d)** A borehole sonde is a cylinder tens of centimetres long in a hole of
centimetres diameter, so the *usable* aspect ratio is large, and the tool is
usually modelled as an infinite cylinder or line because the return path for the
current is far away. The criteria of (c) are about the *source* geometry, not the
medium, so they apply to the sonde's electrode spacing (where they can fail) and to
its coil (where the loop model of ★3 replaces the line model entirely).

---

## ★2 — Ampère's law applications

**(a)** $B = \mu_0nI = (1.2566\times10^{-6})(1000)(2) = 2.513\times10^{-3}$ T
$= 2513$ µT, i.e. **83.8 times** the nominal geomagnetic field of 30 µT. This is
why a solenoid can be used to *cancel* the Earth's field in a shielded room, and
why an unshielded one dominates its own noise budget.

**(b)** $B = \mu_0NI/(2\pi r) = (1.2566\times10^{-6})(500)/(2\pi\times0.05)
= 2.000\times10^{-3}$ T.

**(c)** $B = \mu_0I/(2\pi s) = (1.2566\times10^{-6})(5)/(2\pi\times0.05)
= 2.000\times10^{-5}$ T.

**(d)** (i) the current distribution must be steady; (ii) the field must be
constant in time (no displacement current); (iii) the path must be chosen so that
$\mathbf B$ is either constant-parallel or perpendicular to it everywhere — i.e.
enough symmetry to reduce the integral to a product. Without (iii) Ampère's law is
still true but useless as a shortcut.

---

## ★3 — The loop

**(a)** With $\mathbf r' = a(\cos\phi,\sin\phi,0)$ and
$\mathrm d\boldsymbol\ell = a\,\mathrm d\phi(-\sin\phi,\cos\phi,0)$, the
cross-product with $\mathbf R = (-a\cos\phi,-a\sin\phi,z)$ has $z$-component
$a^2\mathrm d\phi$ and transverse components that integrate to zero over a full
turn. Hence

$$B_z(z) = \frac{\mu_0I}{4\pi}\int_0^{2\pi}\frac{a^2\,\mathrm d\phi}{(a^2+z^2)^{3/2}}
= \frac{\mu_0Ia^2}{2(a^2+z^2)^{3/2}} .$$

**(b)** $a = 0.2$ m, $I = 10$ A:
$B_z(0) = \mu_0I/(2a) = 3.1416\times10^{-5}$ T;
$B_z(a) = \mu_0Ia^2/[2(2a^2)^{3/2}] = 1.1107\times10^{-5}$ T;
$B_z(10a) = 3.0951\times10^{-8}$ T. The demo reproduces the first two to six
figures and prints ratio 1.000000 at every $z$ it tests.

**(c)** $m = I\pi a^2 = 10\pi(0.04) = 1.2566$ A m².

**(d)** Near field $z\ll a$: $B\to\mu_0I/(2a)$, essentially uniform (the field of a
long solenoid's interior, and the reason a Helmholtz pair gives a uniform field).
Far field $z\gg a$: $B\propto1/z^3$, the dipole law. The far field falls faster
because the loop's total "magnetic charge" is zero: the leading $1/r^2$ term
cancels between the two sides of the loop, leaving the next term.

---

## ★4 — $\nabla\cdot\mathbf B = 0$

**(a)** Write the dipole field as
$\mathbf B = \frac{\mu_0}{4\pi r^3}\left[3(\mathbf m\cdot\hat{\mathbf r})
\hat{\mathbf r}-\mathbf m\right]$, i.e.
$B_i = \frac{\mu_0}{4\pi}\partial_j\partial_j\left(\frac{m_k x_k}{r}\right)$-type
combinations after using $\hat{\mathbf r}/r^3 = -\nabla(1/r)$ and
$\partial_i\partial_j(1/r)$ being symmetric and traceless. Concretely,

$$\mathbf B = \frac{\mu_0}{4\pi}\nabla\times\left(\frac{\mathbf m\times\hat{\mathbf r}}{r^2}\right),$$

so $\nabla\cdot\mathbf B = \frac{\mu_0}{4\pi}\nabla\cdot\nabla\times(\cdots) = 0$
identically, for every field point including the origin, because a divergence of a
curl vanishes pointwise. The demo confirms this numerically for the analytic
dipole over three step sizes.

**(b)** For the analytic dipole the only error is the central-difference truncation
$\propto h^2$: two successive halvings of $h$ reduce $|\nabla\cdot\mathbf B|$ from
$2.54\times10^{-10}$ to $6.34\times10^{-11}$ to $1.59\times10^{-11}$ T/m — ratios of
exactly 4.00 — and the scaled value falls to $3.7\times10^{-8}$ of $|\mathbf B|/a$.
For the numerically integrated loop the divergence stalls around
$10^{-6}$ relative and *does not* improve when $h$ is reduced, because the
undiminished error is in the 7200-segment quadrature, not in the differencing.
The two error sources have different signatures, and that is how you tell them
apart.

**(c)** $\nabla\cdot\mathbf B = 0$ *permits*: a vector potential with
$\mathbf B = \nabla\times\mathbf A$; and, wherever $\mathbf J = 0$, a scalar
magnetic potential with $\mathbf B = -\mu_0\nabla\Phi_m$ obeying Laplace's equation.
It *forbids* any magnetic monopole — no field line can begin or end, so there is no
$1/r^2$ magnetic field from a static source and no Gauss's-law-of-magnetism analogue
of a point charge.

**(d)** It would become $\nabla\cdot\mathbf B = \mu_0\rho_m$ with $\rho_m$ a
magnetic charge density, and the immediate instrumental consequence would be that
a magnetic field could be produced by a *static, spherically symmetric* source, so
a stationary monopole would be directly detectable by a magnetometer without any
coil or current — which no experiment has ever observed. Experiments to date set
extremely tight upper bounds on the monopole flux, and the observational absence is
why every EM formulation is built on $\nabla\cdot\mathbf B = 0$.

---

## ★5 — The dipole limit

**(a)** With $m = 1.2566$ A m² (from ★3c):

$$B_{\text{ax}} = \frac{\mu_0\,2m}{4\pi r^3}, \qquad
B_{\text{eq}} = -\frac{\mu_0\,m}{4\pi r^3} .$$

| $r$ (m) | $B_{\text{ax}}$ (T) | $B_{\text{eq}}$ (T) |
|---|---|---|
| 1 | $2.5133\times10^{-7}$ | $-1.2566\times10^{-7}$ |
| 2 | $3.1416\times10^{-8}$ | $-1.5708\times10^{-8}$ |
| 5 | $2.0106\times10^{-9}$ | $-1.0053\times10^{-9}$ |

**(b)** At $r = 2a$ the exact equatorial loop field is
$-2.7087\times10^{-6}$ T against a dipole value of $-1.9635\times10^{-6}$ T: 38 %
error. At $r = 5a$ the exact value is $-1.3156\times10^{-7}$ T against
$-1.2566\times10^{-7}$ T: 4.7 % error. Since the error scales as $(a/r)^2$, 1 %
requires $r/a \gtrsim 10$. The demo's axial/equatorial ratio column shows the same
convergence approaching $-2$: $-1.0374$, $-1.8012$, $-1.9869$, $-1.9995$ at
$r/a = 2, 5, 20, 100$.

**(c)** The equatorial field is anti-parallel to $\mathbf m$: writing
$\mathbf B = \frac{\mu_0}{4\pi r^3}[3(\mathbf m\cdot\hat{\mathbf r})
\hat{\mathbf r}-\mathbf m]$, an equatorial point has $\mathbf m\cdot\hat{\mathbf r}
= 0$ and the bracket is $-\mathbf m$. Because the *direction* of the anomaly is
part of the interpretation (it is how a reversed remanent magnetisation is
recognised), dropping the sign inverts the modelled anomaly and can flip a
palaeomagnetic conclusion.

**(d)** Ratio $-2$: on the axis, the contributions add with the full magnitude
$2m$; on the equator they cancel down to $m$. The factor 2 is geometric, not
dynamical.

---

## ★6 — Transmitter design

**(a)** $1/r^3$, so doubling the depth requires $2^3 = \mathbf{8\times}$ the moment.

**(b)** The moment is the product of turns, area and current, so 100 turns need
$1/100$ of the current: 2.5 A instead of 250 A (see ★10 for the numbers).

**(c)** $m = 100\times5\times\pi(0.1)^2 = 15.708$ A m². On-axis:
$B = \mu_0(2m)/(4\pi r^3)$ gives $3.1416\times10^{-6}$ T (3.14 µT) at 1 m,
$3.1416\times10^{-9}$ T (3.14 nT) at 10 m and $3.1416\times10^{-12}$ T
(3.1 pT $= 3.1\times10^{-3}$ nT) at 100 m.

**(d)** At 100 m the coil produces $3.1\times10^{-3}$ nT against a nominal
geomagnetic field of $\sim5\times10^{4}$ nT — a ratio of $6\times10^{-8}$. The
primary signal is unmeasurable against the background; what is measurable is the
*time-varying* secondary field, referenced to the transmitter waveform and
separated from the background by synchronous detection. That is the whole design
philosophy of a controlled-source EM system, and it is why the source strength
mostly cancels in the ratio the method reports.

---

## ★7 — Ampère's law with a finite wire

**(a)** By symmetry the field of a straight wire at a point in its midplane is
azimuthal, with magnitude
$B_\phi = \mu_0I(\sin\theta_1+\sin\theta_2)/(4\pi s)$, where
$\theta_1$, $\theta_2$ are the angles subtended at that point by the two ends of
the wire. Here $\sin\theta_1 = \sin\theta_2 = L/\sqrt{s^2+L^2}$, so
$B_\phi = \mu_0IL/(2\pi s\sqrt{s^2+L^2})$. A circular path of radius $s$ in the
midplane has length $2\pi s$, so

$$\oint\mathbf B\cdot\mathrm d\boldsymbol\ell
= 2\pi s\,B_\phi = \frac{\mu_0IL}{\sqrt{s^2+L^2}} .$$

The demo evaluates the same quantity by quadrature and obtains
$1.256\,637\,056\times10^{-5}$ T m for $I = 10$ A.

**(b)** $L/\sqrt{s^2+L^2} = 500/\sqrt{0.0025+250000} = 1 - 5.0\times10^{-9}$, i.e.
a shortfall of $5.0\times10^{-7}$ % — utterly negligible in practice, and printed
by the demo as such.

**(c)** Because the law is obtained from $\nabla\times\mathbf B = \mu_0\mathbf J$
by Stokes' theorem, and taking the divergence gives
$\nabla\cdot\mathbf J = 0$: steady current must be conserved. A finite wire with no
return path violates this locally, and the discrepancy appears as the
$L/\sqrt{s^2+L^2}$ factor. In a real circuit the return path supplies the missing
flux.

**(d)** The non-linking value is $2.4\times10^{-16}$ of the linking value
($\mu_0I$), i.e. of order the round-off of a sum of $\sim10^{4}$ terms of order
$10^{-5}$: double precision gives about $10^{-16}$ relative, and
$3\times10^{-21}/1.26\times10^{-5} = 2.4\times10^{-16}$ ✓. The path integral is
zero to machine precision, which is the correct statement of Ampère's law for a
path that does not link the current.

---

## ★8 — The Earth's dipole

**(a)** $m = \frac{4\pi R^3B_{\text{eq}}}{\mu_0}
= \frac{4\pi(6.371\times10^6)^3(3.0\times10^{-5})}{1.2566\times10^{-6}}
= 7.758\times10^{22}$ A m². The handbook's nominal value is
$8\times10^{22}$ A m²; the agreement to within 3 % is a consistency check on the
dipole interpretation, not a measurement of the moment.

**(b)** The axial surface field is exactly twice the equatorial one for a centred
dipole, so 60 000 nT — matching the nominal polar value quoted in the handbook.
That the two nominals and the dipole model agree so well is why the dipole is the
standard first-order description of the main field.

**(c)** Consult the current generation of the International Geomagnetic Reference
Field and evaluate the axial Gauss coefficient $g_1^0$; the IGRF is published by
IAGA and distributed through NOAA NCEI. The moment changes on human timescales, so
quoting a fixed value is a statement about an epoch, not about the Earth.

**(d)** Measured: the field vector at the surface, and its spatial and temporal
variation. Assumed: that the external field is dominated by a centred dipole; that
the surface field is representative of the whole surface (it is not — the real
field has non-dipole terms of order 10 % of the dipole); and that the mean Earth
radius is the right length scale. The first-order error is therefore about 10 %,
dominated by the non-dipole field, and the "moment" is a summary statistic of the
observations rather than a property one can measure directly.

---

## ★9 — Vector potentials

**(a)** With $\mathbf A = \frac{\mu_0}{4\pi}\frac{\mathbf m\times\hat{\mathbf r}}{r^2}$,
standard vector calculus gives
$\nabla\times\mathbf A = \frac{\mu_0}{4\pi}\frac{3(\mathbf m\cdot\hat{\mathbf r})
\hat{\mathbf r}-\mathbf m}{r^3}$, which is exactly $\mathbf B$; and
$\nabla\cdot\mathbf A = \frac{\mu_0}{4\pi}\mathbf m\cdot\nabla\times
(\hat{\mathbf r}/r^2) = 0$ because
$\nabla\times(\hat{\mathbf r}/r^2) = \mathbf 0$ away from the origin. This is the
Coulomb-gauge dipole potential.

**(b)** For an infinite wire along $z$, symmetry gives
$\mathbf A = A_z(s)\hat{\mathbf z}$ with
$(\nabla\times\mathbf A)_\phi = -\partial A_z/\partial s$. Setting this equal to
$\mu_0I/(2\pi s)$ and integrating gives
$A_z = -(\mu_0I/2\pi)\ln(s/s_0)$. The constant $s_0$ is a gauge choice: it shifts
$A_z$ by a constant, which changes nothing physical because $\mathbf B$ depends only
on derivatives of $\mathbf A$. Gauge freedom is a feature — it lets one impose
$\nabla\cdot\mathbf A = 0$ (Coulomb) or the Lorenz condition, whichever simplifies
the problem.

**(c)** Maxwell's equations in terms of potentials reduce from six coupled
first-order equations to a smaller number of second-order equations, and the
divergence constraint $\nabla\cdot\mathbf B = 0$ is satisfied *identically* rather
than being imposed numerically. In the induction equation for a moving conductor
the same substitution shows explicitly that the field is advected and diffused
rather than created. Numerical EM codes that solve for $\mathbf A$ (or for
$\mathbf A$-$\phi$) inherit the constraint automatically, whereas codes that solve
for $\mathbf B$ directly must enforce it.

**(d)** The scalar potential is the right choice for the external field of a
magnetised body where no current flows — i.e. essentially all of *magnetic
surveying*, including the anomaly formulas of lesson
[02-07-07](../07-magnetisation-materials.md). It fails wherever
$\mathbf J\neq0$, including inside and around a current-carrying transmitter
coil, because there $\mathbf B$ is not curl-free and no single-valued
$\Phi_m$ exists. That is why induction problems use $\mathbf A$ and potential-field
magnetics uses $\Phi_m$.

---

## ★10 — Units and design

**(a)** $\mathbf M$ and $\mathbf H$ are both in A/m, so their sum is in A/m;
multiplying by $\mu_0$ (in T m/A = H/m) gives T ✓ — the same unit as $\mathbf B$.
The non-trivial content is that $\mathbf B$ and $\mathbf H$ are *different
quantities* with different units, so the equation is a constitutive relation, not a
unit conversion.

**(b)** $H = B/\mu_0 = 50\,000\times10^{-9}/1.2566\times10^{-6} = 39.79$ A/m.

**(c)** $B_{\text{ax}} = \mu_0(2m)/(4\pi r^3)$, so

$$m = \frac{4\pi r^3B}{\mu_0\,2}
= \frac{4\pi(1)^3(5\times10^{-5})}{2(1.2566\times10^{-6})} = 250\ \mathrm{A\,m^2} .$$

**(d)** A single-turn 1 m² loop: $I = 250$ A. A 100-turn 1 m² coil: $I = 2.5$ A. A
100-turn coil of 0.1 m radius (area 0.0314 m², total effective area 3.14 m²):
$I = 250/3.14 = 79.6$ A. The 2.5 A design is the practical one: high current in a
thin conductor dissipates $I^2R$ heat and requires heavy cabling, while adding
turns increases the moment linearly at the cost of resistance (also linearly) and
of inductance — which limits how fast the current can be switched, and therefore
sets the highest usable frequency. Moment is cheap; moment *at frequency* is not.

**(e)** The conducting ground carries eddy currents induced by the coil, and those
currents produce a secondary field that (by Lenz's law) opposes the primary change
and loads the coil. The measured field is the sum of primary and secondary; the
free-space formula of (c)–(d) describes only the primary. Lesson
[02-07-04](../04-em-induction.md) §2–4 and lesson
[02-07-06](../06-em-in-conductors.md) quantify the loading through the skin depth and
the diffusion time — which is why a transmitter loop is usually laid on, or raised
well above, the ground.
