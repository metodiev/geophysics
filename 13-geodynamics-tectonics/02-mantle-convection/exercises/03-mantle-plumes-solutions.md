# Solutions — 13-02-03 Mantle Plumes, Hotspots and Large Igneous Provinces

> **Read after attempting the exercises.** Numbers were computed, not estimated by
> hand. $g = 9.81\ \mathrm{m\,s^{-2}}$;
> $1\ \mathrm{Myr} = 3.1557\times10^{13}\ \mathrm{s}$,
> $1\ \mathrm{yr} = 3.1557\times10^{7}\ \mathrm{s}$.

Lesson: [03 Mantle Plumes](../03-mantle-plumes.md).

---

## ★1 — Density anomaly at 150 K

$$\Delta\rho = \rho_0\alpha\Delta T
= (3300)(3\times10^{-5})(150) = 14.85\ \mathrm{kg\,m^{-3}}
= 0.45\%\ \text{of }\rho_0 .$$

---

## ★2 — Conduit flow for a 40 km radius

$$u_{\max} = \frac{\Delta\rho\,g\,a^{2}}{4\eta_c}
= \frac{(19.8)(9.81)(4\times10^{4})^{2}}{4(2\times10^{19})}
= \frac{3.108\times10^{11}}{8\times10^{19}}
= 3.885\times10^{-9}\ \mathrm{m\,s^{-1}},$$

$$\langle u\rangle = \frac{u_{\max}}{2} = 1.942\times10^{-9}\ \mathrm{m\,s^{-1}},$$

$$Q = \pi a^{2}\langle u\rangle
= \pi(1.6\times10^{9})(1.942\times10^{-9}) = 9.763\ \mathrm{m^{3}\,s^{-1}},$$

$$B = \Delta\rho\,g\,Q = (19.8)(9.81)(9.763)
= 1.896\times10^{3}\ \mathrm{kg\,s^{-1}} .$$

The Poiseuille profile's factor of two between maximum and mean velocity is worth
keeping: heat and mass fluxes use the *mean*, and using $u_{\max}$ in a heat
budget overestimates it by 100%.

---

## ★3 — Heat carried and the plume count

$$q_{\text{plume}} = \rho_0 c_p\Delta T\,Q
= (3300)(1250)(200)(9.763)
= 8.055\times10^{9}\ \mathrm{W} = 8.06\ \mathrm{GW},$$

$$n = \frac{44.4\times10^{12}}{8.055\times10^{9}} = 5.51\times10^{3} .$$

**5512 conduits.** Against a few tens of recognised hotspots, this is a factor of
100 discrepancy, and it is the quantitative version of the lesson's conclusion:
circulation through narrow conduits cannot be the mantle's main heat-transport
mechanism. The escape routes are all in the model inputs — a much lower conduit
viscosity, a much larger conduit radius (which enters as $a^{4}$), or a
time-averaged flux dominated by short-lived, high-flux pulses rather than a steady
conduit.

---

## ★★4 — Rise speed of a 300 km head

$$u = \frac{2\Delta\rho\,g\,a^{2}}{9\eta}
= \frac{2(19.8)(9.81)(3\times10^{5})^{2}}{9(10^{21})}
= \frac{3.496\times10^{13}}{9\times10^{21}}
= 3.885\times10^{-9}\ \mathrm{m\,s^{-1}},$$

$$u = 3.885\times10^{-9}\times3.1557\times10^{7} = 0.1226\ \mathrm{m\,yr^{-1}},\qquad
t_{\text{rise}} = \frac{2.9\times10^{6}}{0.1226\times3.1557\times10^{7}/3.1557\times10^{7}}
= \frac{2.9\times10^{6}\ \mathrm{m}}{0.1226\ \mathrm{m\,yr^{-1}}}
= 2.37\times10^{7}\ \mathrm{yr} = 23.7\ \mathrm{Myr} .$$

**Scaling:** $u\propto a^{2}$. Going from the lesson's 250 km head
($0.085\ \mathrm{m\,yr^{-1}}$) to 300 km multiplies the speed by
$(300/250)^{2} = 1.44$, giving $0.1226$ ✔ — the rise time falls from 34.1 to
23.7 Myr, a factor of $1/1.44$.

---

## ★★5 — Blob Rayleigh number and diffusive time

$$Ra_{\text{blob}} = \frac{\Delta\rho\,g\,L^{3}}{\eta\kappa}
= \frac{(19.8)(9.81)(3\times10^{5})^{3}}{(10^{21})(10^{-6})}
= \frac{(19.8)(9.81)(2.7\times10^{16})}{10^{15}}
= 5.244\times10^{3},$$

$$\frac{Ra_{\text{blob}}}{Ra_c} = \frac{5244}{657.5} = 7.98 .$$

$$t_{\text{diff}} = \frac{L^{2}}{\kappa}
= \frac{9\times10^{10}}{10^{-6}} = 9\times10^{16}\ \mathrm{s} = 2.85\times10^{3}\ \mathrm{Myr}
= 2.85\ \mathrm{Gyr}.$$

**Conclusion.** The blob is unstable by a factor of 8 — modest but definite, and
*below* the factor of 37 for the lesson's 500 km blob, showing how sharply the
size matters ($Ra\propto L^{3}$). More importantly, the diffusive time (2.85 Gyr)
is 120 times the rise time (23.7 Myr): a thermal anomaly of this size is *not*
erased during ascent. The Péclet number is
$Pe = uL/\kappa = 3.885\times10^{-9}\times3\times10^{5}/10^{-6} = 1.17\times10^{3}$,
so advection beats conduction by three orders of magnitude. The obstacle to
plumes is therefore the existence of a buoyancy source and the survival of a
narrow conduit (79 Myr for a 50 km one), not the survival of the head.

---

## ★★6 — Shifting the solidus up by 50 K

With $T_{\text{sol}} = 1400+3z$ and $T_{\text{liq}} = T_{\text{sol}}+400$:

$$F(z) = \frac{T_{\text{plume}} - T_{\text{sol}}}{400}
= \frac{(1600 - 0.5z) - (1400+3z)}{400}
= \frac{200 - 3.5z}{400},$$

so $F = 0$ at $z = 200/3.5 = 57.1$ km, and $F = 0.5$ at $z = 0$.

| $z$ (km) | 0 | 10 | 20 | 30 | 40 | 50 | 55 |
|---|---|---|---|---|---|---|---|
| $F$ | 0.500 | 0.4125 | 0.325 | 0.2375 | 0.150 | 0.0625 | 0.0188 |

On the demonstration's 5 km grid the melting column is 60 km deep with mean melt
fraction 0.259, giving an igneous crustal thickness of
$0.5\times0.259\times60 = 7.78$ km at a productivity of 0.5.

**Comparison with the lesson** (75 km, 0.319, 12.0 km): every quantity is smaller.
The direction is easy to predict and worth predicting before computing: raising
the solidus means the same adiabat intersects it shallower, so the melting column
shortens (75 → 60 km) and the mean melt fraction falls (0.319 → 0.259), reducing
the crustal thickness by 35%. This is the origin of the non-uniqueness that
plagues igneous petrology: a 50 K difference in the solidus, well within the
uncertainty of a real phase diagram, changes the predicted crustal thickness by
more than a third.

---

## ★★★7 — Inverting a buoyancy flux

For $B = 3\times10^{3}\ \mathrm{kg\,s^{-1}}$, a conduit of radius 60 km, and
$B = \Delta\rho\,g\,Q$ with $Q = \pi\Delta\rho\,g\,a^{4}/(8\eta_c)$:

$$\Delta\rho = \left(\frac{8\eta_c B}{\pi g^{2}a^{4}}\right)^{1/2},
\qquad
\Delta T = \frac{\Delta\rho}{\rho_0\alpha},
\qquad
Q = \frac{B}{\Delta\rho\,g} .$$

With $a = 6\times10^{4}$ m, $\pi a^{4} = 4.072\times10^{19}$ and
$g^{2} = 96.24$:

| $\eta_c$ (Pa s) | $\Delta\rho$ (kg m$^{-3}$) | $\Delta T$ (K) | $Q$ (m$^{3}$/s) | conduit speed (m/s) |
|---|---|---|---|---|
| $10^{18}$ | 2.475 | 25.0 | $1.236\times10^{2}$ | $2.19\times10^{-8}$ |
| $10^{19}$ | 7.826 | 79.1 | $3.907\times10^{1}$ | $6.91\times10^{-9}$ |
| $10^{20}$ | 24.749 | 250.0 | $1.236\times10^{1}$ | $2.19\times10^{-9}$ |

Each viscosity is internally consistent with *the same* observed buoyancy flux —
and they imply excess temperatures from 25 K (too small to melt anything) to
250 K (enough to generate a large igneous province). The observation constrains
the *product* $\Delta\rho\,g\,Q$ and nothing else.

**A check that also teaches something.** The heat carried by the conduit is

$$q_{\text{plume}} = \rho_0 c_p\Delta T\,Q
= \frac{c_p B}{\alpha g}
= \frac{(1250)(3\times10^{3})}{(3\times10^{-5})(9.81)}
= 1.274\times10^{10}\ \mathrm{W} = 0.0127\ \mathrm{TW},$$

**independent of the conduit viscosity** — because $\Delta\rho$ and $Q$ move in
opposite directions as $\eta_c$ changes, and their product is fixed by $B$. So a
 buoyancy-flux measurement determines the heat carried by the plume, but not the
temperature or the flux separately. That is a stronger statement than "there are
three unknowns and one equation", and it shows exactly which physical quantity is
well posed.

**What the data actually constrain.** Only the buoyancy flux (and through it the
heat). To separate the factors one needs an independent measurement or argument
for at least one of (conduit radius, conduit viscosity, excess temperature): a
seismically imaged conduit, an independent viscosity (from postglacial rebound or
the geoid), or a petrological maximum temperature from the erupted lavas. The
250 K entry also fails an independent check: a 250 K excess temperature would melt
far more than is observed in most hotspot tracks, so the highest-viscosity
inversion is *petrologically* inconsistent even though it is arithmetically
fine — which is how an independent datum breaks the degeneracy.

---

## ★★★8 — Testing hotspot fixity

**Data.** (i) Radiometric ages along hotspot tracks on two plates that share a
hotspot (or on one plate for a track with a bend); (ii) plate reconstructions that
give relative plate motions from magnetic anomalies; (iii) the present-day
positions of hotspots relative to the reconstructed tracks.

**Model.** Predicted track geometry from relative plate motion plus an assumed
hotspot motion; the predicted age–distance relation is
$t(d) = d/v_{\text{rel}}$.

**Measured quantity.** The residual between the observed track (positions and
ages) and the prediction for zero hotspot motion, i.e. the misfit in track
geometry and the residual age progression.

**Signatures.** A fixed hotspot produces a smooth track parallel to the plate
velocity with a strictly linear age–distance relation (the lesson's measured
50.0 mm/yr for a 3000 km/60 Myr track) and a bend angle equal to the change in
plate velocity direction. A hotspot moving at 10 mm/yr — a fifth of the plate
speed, and comparable with the plume's own rise speed of 85 mm/yr — produces a
track that is systematically rotated away from the plate-velocity azimuth by
$v_{\text{hotspot}}/v_{\text{plate}}$ and an age–distance relation that is curved
wherever the *relative* velocity changed, i.e. exactly at the bends.

**Principal confound.** Absolute plate motion requires a reference frame: the
hotspot frame is itself the standard one, so using hotspot tracks to test hotspot
fixity is circular unless an independent frame is used. The independent routes are
palaeomagnetic (longitude is unresolvable), seismic anisotropy (which measures
mantle flow rather than the frame), and the geological record of track continuity
across a ridge. The test is therefore only conclusive where two tracks on
different plates cross the same hotspot and their *relative* motion can be
predicted independently — a geometry that is rare and must be sought rather than
assumed.
