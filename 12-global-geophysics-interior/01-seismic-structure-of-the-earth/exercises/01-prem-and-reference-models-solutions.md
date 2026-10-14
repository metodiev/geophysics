# Solutions — 12-01-01 PREM, IASP91 and Reference Earth Models

Worked solutions for
[01-prem-and-reference-models-exercises.md](./01-prem-and-reference-models-exercises.md).
The lesson is
[01 PREM, IASP91 and Reference Earth Models](../01-prem-and-reference-models.md).
All models are **SYNTHETIC**; convention values are labelled as such.

---

## ★ Foundational

### ★1 — Converting the ray parameter

The two conventions coincide at the surface, where $r = R$: the flat Earth's
$\sin i/v$ equals the sphere's $r\sin i/v$ divided by $R$. Hence

$$p_\text{rad} = R\,p_\text{flat} = 6371\ \mathrm{km} \times 0.0600\
\mathrm{s\,km^{-1}} = 382.26\ \mathrm{s\,rad^{-1}},$$

$$p_\text{deg} = \frac{382.26}{57.2958} = 6.6717\ \mathrm{s\,deg^{-1}}.$$

Check with $1° = 111.19\ \mathrm{km}$: $0.0600 \times 111.19 = 6.671\ \mathrm{s\,deg^{-1}}$,
agreeing to the last digit.

**Which to use:** the spherical ray integrals take $p$ in
$\mathrm{s\,rad^{-1}}$ (or numerically, if you keep $\Delta$ in degrees, in
$\mathrm{s\,deg^{-1}}$). The flat-Earth form is only valid where curvature can be
neglected, i.e. for paths short compared with $\sqrt{R\lambda}$; a teleseismic
ray is not in that regime.

### ★2 — Vertical time through a linear velocity gradient

With $v$ linear in radius, from $v_1 = 10.75$ at the top to $v_2 = 13.72\
\mathrm{km\,s^{-1}}$ over $L = 2891 - 670 = 2221\ \mathrm{km}$,

$$\int_0^L \frac{\mathrm{d}x}{v_1 + (v_2-v_1)x/L}
= \frac{L}{v_2 - v_1}\ln\frac{v_2}{v_1}
= \frac{2221}{2.97}\ln\frac{13.72}{10.75}
= 747.811 \times 0.243914 = 182.428\ \mathrm{s}.$$

The midpoint estimate is $L/\bar{v}$ with
$\bar{v} = (10.75+13.72)/2 = 12.235\ \mathrm{km\,s^{-1}}$:

$$L/\bar{v} = 2221/12.235 = 181.528\ \mathrm{s}.$$

The exact value is **larger by 0.900 s (0.5 %)**. The reason is that
$1/v$ is a convex function: it is larger on the slow side of the interval than the
midpoint value suggests, so dividing by the arithmetic mean velocity always
underestimates the time. The correct average for a transit-time integral is the
harmonic (here, logarithmic) mean.

### ★3 — A homogeneous sphere, by hand

$$\frac{r_{tp}}{R} = \frac{5000}{6371} = 0.784806,\qquad
\arccos(0.784806) = 0.668518\ \mathrm{rad},$$
$$\Delta = 2 \times 0.668518 = 1.337036\ \mathrm{rad} = 76.594°,$$
$$T = \frac{2\sqrt{6371^2 - 5000^2}}{8.00}
= \frac{2 \times 3948.37}{8.00} = 987.09\ \mathrm{s}.$$

(The square root is $\sqrt{40\,589\,641 - 25\,000\,000} = \sqrt{15\,589\,641} =
3948.37\ \mathrm{km}$, a straight chord.) These are the values a correct
spherical ray integrator must reproduce; the lesson's demonstration reproduces
the analogous case to $2\times10^{-11}$.

---

## ★★ Applied

### ★★4 — Turning depth from a slowness measurement

First estimate $p$ at $\Delta = 88°$ by linear interpolation of the two rows:

$$\frac{\mathrm{d}p}{\mathrm{d}\Delta} = \frac{4.5470 - 4.8099}{89.666 - 86.404}
= \frac{-0.2629}{3.262} = -0.08059\ \mathrm{s\,deg^{-1}\,deg^{-1}},$$
$$p(88°) = 4.8099 - 0.08059\,(88 - 86.404) = 4.8099 - 0.1286
= 4.6813\ \mathrm{s\,deg^{-1}} = 268.22\ \mathrm{s\,rad^{-1}}.$$

Now solve $r/v(r) = p$ with the supplied local model
$v(r) = 13.4 + 5.0\times10^{-3}(3580 - r)\ \mathrm{km\,s^{-1}}$
(i.e. $v$ increases upward at $5\times10^{-3}\ \mathrm{s^{-1}}$):

$$r = 268.22\left[13.4 + 5.0\times10^{-3}(3580 - r)\right]
= 3594.1 + 4801.1 - 1.3411\,r,$$
$$r\,(1 + 1.3411) = 8395.2 \;\Rightarrow\; r = 3586.0\ \mathrm{km}.$$

The turning **depth** is $6371 - 3586.0 = 2785\ \mathrm{km}$, i.e. the ray bottoms
about 106 km above the CMB — consistent with $\Delta = 88°$ being close to the
core-grazing limit of $91.16°$ in this model. Note the logic: the *slope* of the
travel-time curve gave $p$, and $p$ gave $r/v$ at the turning point. Nothing else
was needed. That is exactly why the local slope of a travel-time curve is treated
as a measurement of $r/v$ at depth.

### ★★5 — A two-layer moment of inertia

With $q = a/R = 3000/6371 = 0.470884$:

$$q^3 = 0.104410,\qquad q^5 = 0.023151,$$
$$\rho_c q^3 + \rho_m(1-q^3) = 11.0(0.104410) + 4.7(0.895590)
= 1.148510 + 4.209273 = 5.357783,$$
$$\rho_c q^5 + \rho_m(1-q^5) = 11.0(0.023151) + 4.7(0.976849)
= 0.254661 + 4.591190 = 4.845851,$$
$$\frac{C}{MR^2} = 0.4 \times \frac{4.845851}{5.357783}
= 0.4 \times 0.904444 = 0.361778.$$

**Not compatible** with 0.3307: the model is 9.4 % too high. A two-layer Earth is
less centrally concentrated than the real one, because all the compression is
carried by a single density jump. To lower $C/MR^2$ at fixed densities you must
either enlarge the dense core (which quickly overshoots) or let the density
increase *within* the core and mantle.

### ★★6 — Two vertical times that differ by a factor of nearly two

The numbers are $T_\text{surf,ICB} = 507.818\ \mathrm{s}$ and
$T_\text{surf,centre} = 617.471\ \mathrm{s}$. They do **not** differ by a factor of
two; the factor-of-two number in the demonstration is
$2 \times 507.818 = 1015.720\ \mathrm{s}$, the *down-and-up* time of a ray
reflected at the ICB. The lesson prints all three, and the reason the second is
twice the first is simply that a reflected ray traverses the same path twice,
while a radial ray to the centre traverses it once.

The inner-core leg is the difference:

$$T_\text{centre→ICB} = 617.471 - 507.818 = 109.653\ \mathrm{s},$$

which the demonstration reports as $109.559\ \mathrm{s}$ by integrating
$\mathrm{d}r/v_p$ over the innermost shell directly. The two differ by 0.09 %
because the subtraction uses the full grid while the direct integral uses the
samples with $r \le 1221.5\ \mathrm{km}$; with a 1 km grid, one or two nodes sit
on either side of the ICB and carry $O(0.1\ \mathrm{s})$ of the answer. The mean
inner-core velocity is therefore

$$\bar{v}_p^\text{IC} = \frac{1221.5\ \mathrm{km}}{109.56\ \mathrm{s}}
= 11.149\ \mathrm{km\,s^{-1}},$$

which matches the profile's 11.03–11.26 km s$^{-1}$ range as it must. The
assumption made explicit is that the leg is radial and purely P: no conversion,
no anisotropy, no density needed.

---

## ★★★ Research-oriented

### ★★★7 — A perturbation that no travel time can see

The classical exact null direction is the **similarity stretch of a layered
medium**. In flat-layer geometry, take any model $v(z)$ and define

$$z' = s z,\qquad v'(z') = s\,v(z),\qquad p' = p/s .$$

Then the vertical slowness $\sqrt{v^{-2}-p^{2}}$ becomes
$\sqrt{s^{-2}v^{-2} - s^{-2}p^{2}} = s^{-1}\sqrt{v^{-2}-p^{2}}$, and
$\mathrm{d}z' = s\,\mathrm{d}z$, so

$$T' = \int \frac{\mathrm{d}z'}{v'\sqrt{1-p'^2v'^2}}
= \int \frac{s\,\mathrm{d}z}{s v\, s^{-1}\sqrt{1-p^2v^2}} = T,$$

while $\Delta' = s\,\Delta$. So a model stretched in depth by $s$ and stretched in
velocity by $s$ produces **exactly the same travel-time curve** — provided you
also stretch the distance axis by $s$.

Two consequences follow, and both are examinable.

1. **The direction is exactly unconstrained in the flat approximation.** The
   data cannot separate $(z, v)$ from $(sz, sv)$; only an independent depth
   measurement (a borehole, a reflection arrival, a gravity constraint) can.
2. **Sphericity breaks it, but only at first order.** In a spherical Earth the
   surface is pinned at $r = R$ and $\Delta$ is an angle, not a length. The
   stretch above is not an exact symmetry because $r/v$ and $\mathrm{d}r/r$ do not
   scale the same way, which is why the ray parameter enters as $r/v$ and not as
   $1/v$. The residual ambiguity is a *stretch plus distance rescale*, and its
   size is $O(\Delta^2/6)$ — a few per cent at teleseismic distances, i.e. of the
   same order as the picking errors. This is why the crustal depth–velocity
   trade-off survives even in a spherical Earth.

**Quantify it with the two-layer crust.** For a head wave over a half space,
$T = \Delta/v_2 + 2H\sqrt{v_1^{-2}-v_2^{-2}}$. Holding $T$ fixed,

$$\frac{\delta H}{\delta v_1} =
\frac{H\,v_2^{2}}{v_1\left(v_2^{2}-v_1^{2}\right)},$$

which for $H = 30\ \mathrm{km}$, $v_1 = 6.00$, $v_2 = 8.00\ \mathrm{km\,s^{-1}}$
gives $30 \times 64 / (6 \times 28) = 11.43\ \mathrm{km}$ per
$\mathrm{km\,s^{-1}}$. So a 3 % error in $v_1$ ($0.18\ \mathrm{km\,s^{-1}}$) is
traded against $2.06\ \mathrm{km}$ of depth with *no* change in travel time: 7 % of
the layer's thickness. **Parameter count:** one branch of $T(\Delta)$ provides
$T$ and its slope for each ray, which constrain the two combinations
$v_1$ and $H/v_1$; the direction in which both move together is invisible.

### ★★★8 — A stronger validation test

The homogeneous sphere checks the *quadrature and the singularity treatment* but
it has constant velocity, so it contains no interface and no turning-point fold.
A stronger analytic reference is a **two-layer sphere with a closed-form
travel-time curve**: a uniform shell of velocity $v_1$ and radius $R$ over a
uniform core of velocity $v_2 > v_1$. Its rays are two straight chords joined at
the interface, and both $\Delta$ and $T$ are elementary expressions in $p$ and
the interface radius. That test exercises:

- the **splitting of the integral at a discontinuity** (the homogeneous sphere
  never crosses one);
- the **refraction condition** — a ray that crosses the interface must satisfy
  $\sin i$ continuity, which is where sign and index errors live;
- the **branch structure**: the two-layer sphere has a branch with a minimum in
  $\Delta(p)$, so the test also checks that the code finds the fold instead of
  stepping over it.

**Expected error:** the same $10^{-10}$–$10^{-11}$ as the homogeneous test if the
quadrature is correct, because the integrand is still elementary.
**Failure mode caught that the homogeneous sphere misses:** a code that ignores
the velocity jump, i.e. integrates the same velocity function across an interface.
Such a code reproduces the homogeneous sphere perfectly and fails the two-layer
sphere by a per-cent-level error in $\Delta$, growing with $p$.

### ★★★9 — Mass 3 % low while $C/MR^2$ is 0.4 % accurate

The two integrals are

$$M = 4\pi\int_0^R \rho r^2\,\mathrm{d}r,\qquad
C = \frac{8\pi}{3}\int_0^R \rho r^4\,\mathrm{d}r .$$

Both are linear in $\rho$, but the kernels differ: $r^2$ weights the outer
regions comparatively strongly, while $r^4$ weights the deep interior. Write
$C/MR^2 = \frac{2}{3}\frac{\int \rho r^4}{\int \rho r^2\,R^2}$: the ratio is a
*running mean of $r^2$*, so a model can have the right *shape* (right ratio) and
the wrong *scale* (wrong $\rho$ everywhere, hence wrong $M$). Indeed, scaling
$\rho(r) \to \lambda\rho(r)$ leaves $C/MR^2$ exactly unchanged while multiplying
$M$ by $\lambda$. Our synthetic model is 3.0 % light precisely because it is a
uniform-in-shape but slightly under-dense profile.

**Which is more sensitive to the centre?** $C$, and by a factor of $r^2$. The
relative contribution of a shell at radius $r$ is $\propto \rho r^2 \mathrm{d}r$
to $M$ and $\propto \rho r^4\mathrm{d}r$ to $C$. Form the ratio of the deep
(centre) weight to the whole:

$$w_M(r) = \frac{r^2\,\mathrm{d}r}{\int_0^R r^2 \mathrm{d}r} = \frac{3r^2\mathrm{d}r}{R^3},
\qquad
w_C(r) = \frac{r^4\,\mathrm{d}r}{\int_0^R r^4 \mathrm{d}r}
= \frac{5r^4\mathrm{d}r}{R^5},$$

so $w_C/w_M = \frac{5}{3}\,(r/R)^2$ — at the centre this is small, but the
*kernel ratio* comparing the centre with the surface is what matters for
sensitivity: a density error confined to the inner 20 % of the radius changes
$M$ by the fraction $0.2^3 = 0.008$ of its weight but changes $C$ by
$0.2^5 = 0.00032$ of *its* weight — yet $C$'s total weight is dominated by
large-$r$ shells too. The correct conclusion, and the one worth remembering, is
that $C/MR^2$ is a *shape* constraint (a ratio), while $M$ is a *scale*
constraint, and neither measures the central density directly: a density change
confined to the innermost 100 km is essentially invisible in both, because
$r^2\mathrm{d}r$ and $r^4\mathrm{d}r$ vanish there. That is precisely why the
inner core's density and composition rest on mineral physics rather than on
geodesy — the subject of
[Module 02](../../02-composition-and-mineral-physics/README.md).
