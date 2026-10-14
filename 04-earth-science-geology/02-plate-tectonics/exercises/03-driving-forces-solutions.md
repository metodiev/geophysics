# Solutions — 04-02-03 Mantle Convection, Slab Pull and Ridge Push

> **Read this after attempting the exercises, not before.** Where a value is
> attributed to the demo it is the demo's actual output.

---

## ★1 — Slab buoyancy

**(a)** $F = g\,\Delta m\,L = 9.81 \times 6.637\times10^6 \times 8.0\times10^5
= 5.21\times10^{13}$ N/m.

**(b)** $9.81 \times 6.637\times10^6 \times 6.6\times10^5 = 4.30\times10^{13}$ N/m.

**(c)** The ratio is $800/660 = 1.21$: the force is exactly proportional to the
length of slab counted, so "the slab pull" of a given slab is a range whose width
is set by a definition rather than by a measurement.

**(d)** The 660 km value, because most published estimates count the slab only
down to the 660 km discontinuity, where the phase changes and the viscosity
increase alter its behaviour. Quoting a number without saying which convention
was used makes the comparison meaningless.

---

## ★2 — Ridge push

**(a)** $9.81 \times 2300 \times 3547 = 8.00\times10^7$ Pa (80 MPa).

**(b)** $8.00\times10^7 \times 7.0\times10^4 = 5.60\times10^{12}$ N/m.

**(c)** The plate thickness $h$ over which the pressure difference acts. The
elevation $\Delta h$ and the densities are much better constrained. Since $h$ is
roughly the depth at which the cooling plate reaches the adiabat — precisely
where the thermal model stops being sharp — the answer inherits that softness.

**(d)** Of order $10^{12}$ N/m, which is an order of magnitude below slab pull at
$10^{13}$ N/m.

---

## ★3 — Basal drag

**(a)** $v = 30\times10^{-3}/3.15576\times10^7 = 9.507\times10^{-10}$ m/s, so
$\tau = 5\times10^{19}\times9.507\times10^{-10}/1.5\times10^5
= 3.17\times10^5$ Pa.

**(b)** $F = 3.17\times10^5 \times 8.0\times10^6 = 2.53\times10^{12}$ N/m.

**(c)** It does not tell you the **sign** — whether the drag drives or resists —
nor **where** in the asthenosphere the traction is applied, since a layered
viscosity structure with the same integrated traction would give a different
force distribution.

---

## ★★4 — The required viscosity

**(a)**
$$\eta = \frac{F d}{v L} = \frac{4.624\times10^{13}\times2.0\times10^5}
{1.268\times10^{-9}\times8.0\times10^6} = \frac{9.248\times10^{18}}{1.014\times10^{-2}}
= 9.12\times10^{20}\ \text{Pa·s}.$$

**(b)** $v = 60$ mm/a $= 1.902\times10^{-9}$ m/s and $L = 1.2\times10^7$ m:
$$\eta = \frac{4.624\times10^{13}\times2.0\times10^5}{1.902\times10^{-9}\times1.2\times10^7}
= 4.05\times10^{20}\ \text{Pa·s}.$$

**(c)** Both lie inside the range $10^{20}$ to $10^{21}$ Pa·s that post-glacial
rebound infers from the relaxation of Pleistocene ice loads — an entirely
different observation on an entirely different timescale.

**(d)** Because viscosity is the *only* free parameter in the force balance.
Changing the assumed plate speed or plate size moves the required viscosity
within a factor of a few, but nothing in this calculation can move it out of the
rebound range without also breaking the post-glacial rebound inference. Two
independent measurements agreeing on the one adjustable number is what turns a
set of force estimates into a model of the mantle.

---

## ★★5 — The Rayleigh number

**(a)** $\mathrm{Ra} = 3300\times9.81\times3\times10^{-5}\times1300
\times(2.89\times10^6)^3/(3\times10^{20}\times10^{-6})$.
The numerator is $3300\times9.81\times3\times10^{-5}\times1300 = 1262.6$, times
$(2.89\times10^6)^3 = 2.414\times10^{19}$ gives $3.048\times10^{22}$, and the
denominator is $3\times10^{14}$, so $\mathrm{Ra} = 1.02\times10^8$.

**(b)** The cube of the depth scales it by $(700/2890)^3 = 0.0142$, so
$\mathrm{Ra} = 1.44\times10^6$.

**(c)** Both exceed $10^3$ by three to five orders of magnitude. The mantle is
vigorously convecting by any measure.

**(d)** It settles *that* the mantle convects. It does not settle how fast, how
it is organised (one layer or two), or how the plates couple to it — because the
Rayleigh number is a single number summarising a system whose viscosity depends
on temperature, stress and water content, and whose boundary conditions are a
brittle lid rather than a free surface.

---

## ★★6 — Age dependence

**(a)** $7.870/3.642 = 2.16$.

**(b)** A slab that cooled for longer is thicker and colder, so more of its
cross-section carries a density excess. The dependence comes from the same
error-function profile that gives the seafloor its depth–age curve.

**(c)** Plates attached to older, more deeply subducted slabs should move faster,
for the same resistance.

**(d)** Weakly. The correlation between slab age and plate speed is present
across the large plates but far from tight, because plate speed also depends on
the length of the slab, the dip, the area of the plate and the drag on its base.
A prediction that is only partly confirmed is worth more than a force balance
with no prediction at all, but it should not be reported as a confirmation.

---

## ★★★7 — Dip and the useful force

**(a)** Horizontal components: $5.0\times10^{13}\cos 30° = 4.33\times10^{13}$;
$\cos 45° = 3.54\times10^{13}$; $\cos 60° = 2.50\times10^{13}$ N/m.

**(b)** The shallowest dip, 30°, gives the largest horizontal drive, because the
force acts down-dip and the horizontal component is $\cos(\text{dip})$ of it. The
shallower the slab, the more of its pull is directed along the plate's motion.

**(c)** The down-dip length to a given depth changes with dip as
$1/\sin(\text{dip})$, so a steeper slab has a *longer* slab at the same depth and
therefore a larger total pull. The two effects act in opposite directions: a
steeper slab has more force but transmits less of it horizontally.

**(d)** A steep slab is pulled hard but pulls its plate toward the trench weakly,
because most of the force is directed downward into the mantle rather than
horizontally along the plate. That is one reason the correlation between slab
dip and plate speed is not a simple one, and why the geometry of a slab has to be
known as well as its age before a force estimate means anything.

---

## ★★★8 — The demo's output

**(a)** Mass excess and scale depth: 20 Ma `3.642e+06 kg/m^2`, `50 km`; 60 Ma
`5.972e+06`, `87 km`; 100 Ma `7.142e+06`, `112 km`; 140 Ma `7.870e+06`,
`133 km`.

**(b)** At 100 Ma: `L = 660 km → 4.62e+13 N/m`; `L = 2900 km → 2.03e+14 N/m`;
ratio `4.4` for every age.

**(c)** Ridge push runs from `3.20e+12` at $h = 40$ km to `8.00e+12` N/m at
$h = 100$ km.

**(d)** Traction from `7.92e+04` Pa at $10^{19}$ Pa·s to `7.92e+06` Pa at
$10^{21}$ Pa·s; force over a 10 000 km plate from `7.92e+11` to
`7.92e+13` N/m.

**(e)** Required viscosity: `2.92e+21` (20 mm/a, 5000 km), `5.84e+20`
(50 mm/a, 10 000 km), `3.65e+20` (80 mm/a, 10 000 km), `3.89e+20`
(50 mm/a, 15 000 km) Pa·s.

**(f)** $\mathrm{Ra} = 4.33\times10^5$ ($10^{21}$ Pa·s, 700 km);
$3.05\times10^7$ ($10^{21}$, 2890 km); $4.33\times10^4$ ($10^{22}$, 700 km);
$3.05\times10^6$ ($10^{22}$, 2890 km).

**(g)** The robust conclusion is the **ranking**: slab pull exceeds ridge push
and basal drag by about an order of magnitude, and the mantle's Rayleigh number
exceeds the critical value by orders of magnitude. The definition-dependent
quantities are the actual values of slab pull (which changes by a factor of 4.4
with the slab length counted) and ridge push (which changes by a factor of 2.5
with the assumed plate thickness). The required viscosity is neither robust nor
arbitrary: it varies within a factor of about five across plausible plate sizes
and speeds, and it lands in the range that an independent observation
(post-glacial rebound) requires.

---

## ★★★9 — Ranking and its limits

A model answer, not the only acceptable one.

**Ranking.** Slab pull is of order $10^{13}$ N/m; ridge push and basal drag are
each of order $10^{12}$ N/m. The ranking is the robust part of the result: to
change it, one would have to change an input by more than a factor of ten.

**Dominant uncertainties.** For slab pull the dominant uncertainty is the
*definition* — whether the slab is counted to 660 km or through the whole mantle,
a factor of 4.4 — followed by the thermal structure, which is inherited from the
seafloor cooling model and its thermal constants. For ridge push it is the
thickness $h$ over which the pressure difference acts, which is ill-defined
because the thermal model has no sharp base. For basal drag it is the viscosity,
which varies by orders of magnitude with temperature, and then the sign.

**Robustness.** The rank order survives a factor-of-two change in every input.
The individual values do not, and neither does the *ratio* between ridge push and
basal drag, which can cross over within their uncertainties.

**Settling the sign of basal drag.** The observation that would do it is a
direct measurement of the asthenospheric flow beneath a plate and of the plate's
own motion at the same place — the sign of the drag is the sign of the difference
between them. It is hard because the asthenosphere is too deep to sample
directly, the flow can only be inferred from seismic anisotropy or from the
pattern of post-seismic and post-glacial deformation, and the inference is
model-dependent at exactly the level of precision the comparison requires.
