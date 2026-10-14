# Solutions — 08-04-06 Geomagnetic Depth Sounding and Long-Period Induction

> **Read after attempting the exercises.** The lesson is
> [06 Geomagnetic Depth Sounding](../06-geomagnetic-depth-sounding.md).

---

## ★1 — The half-space response at one day

$$\delta = \sqrt{\frac{\rho T}{\pi\mu_0}}
= \sqrt{\frac{10\times86400}{3.9478\times10^{-6}}}
= \sqrt{2.188\times10^{11}} = 4.678\times10^{5}\ \mathrm{m} = 467.8\ \mathrm{km},$$
$$\left|C\right| = \frac{\delta}{\sqrt2} = 330.8\ \mathrm{km}, \qquad
\mathrm{Re}\,C = \frac{\delta}{2} = 233.9\ \mathrm{km}.$$

The two relations used are the exact half-space limits
$\left|C\right| = \delta/\sqrt2$ and $\mathrm{Re}\,C = \delta/2$, both verified
numerically in the demonstration at two resistivities.

---

## ★2 — Skin depth across the period band

$$T = 1\ \mathrm{hour}: \quad \delta = \sqrt{\frac{100\times3600}{3.9478\times10^{-6}}}
= \sqrt{9.119\times10^{10}} = 3.02\times10^{5}\ \mathrm{m} = 302\ \mathrm{km},$$
$$T = 100\ \mathrm{days}: \quad \delta = \sqrt{\frac{100\times8.64\times10^{6}}{3.9478\times10^{-6}}}
= \sqrt{2.188\times10^{14}} = 1.479\times10^{7}\ \mathrm{m} = 14794\ \mathrm{km}.$$

The band therefore samples from the upper mantle (a few hundred kilometres) to
well beyond the base of the mantle. In practice the deepest useful periods are
limited by the source, not by the skin depth — see ★4.

---

## ★3 — A non-zero tipper over a layered Earth

It means the **source is not spatially uniform**, or the **array is not
measuring a 1-D structure**. Two distinct causes:

1. **A spatially varying source.** An electrojet concentrated in the auroral zone
   or the equatorial electrojet has horizontal wavelengths comparable to the
   skin depth at long periods; the vertical field it produces is not an induction
   effect at all. The $k\delta$ criterion quantifies when this matters.
2. **Lateral structure below the site** — the ordinary case: a conductivity
   contrast nearby produces a real vertical field through the boundary between
   the regions of differing conductance. The tipper then indicates the direction
   of the contrast (its arrow is perpendicular to strike in the 2-D case).

A third, non-physical, cause worth naming is a **sensor orientation error**, which
converts horizontal signal into a spurious vertical component.

---

## ★4 — The $k\delta$ test

$$k = \frac{2\pi}{L} = \frac{2\pi}{3.0\times10^{6}} = 2.094\times10^{-6}\ \mathrm{rad\,m^{-1}},$$
$$\delta = 467.8\ \mathrm{km} = 4.678\times10^{5}\ \mathrm{m}, \qquad
k\delta = 2.094\times10^{-6}\times4.678\times10^{5} = 0.98 .$$

$k\delta \approx 1$: the criterion $k\delta\ll1$ is **not** satisfied, so a
plane-wave interpretation is not justified at this period for this source. The
response is contaminated by the source geometry at the order-unity level, which is
the same order as the depth scale itself — meaning the reported depths would be
wrong by tens of per cent, not by a few.

---

## ★5 — Does the equivalence hold at mantle depths?

The 21.27% difference **contradicts** the strong form of the claim and **supports**
the weaker, correct one. The equivalence holds in the limit of a layer thin
compared with the skin depth; at mantle depths the layers (100–200 km) are
comparable to $\delta$ at the periods that sense them, so the equivalence breaks
quantitatively. The correct statement is therefore: *the data constrain a
conductance and a depth range*, and to convert that into a resistivity one needs
either (i) a period band wide enough to break the equivalence, and hence to
constrain the thickness, or (ii) an assumption about the thickness, stated as
such. At mantle depths the second is usually what is done, and it should be stated.

---

## ★6 — The phase and the gradient

At **1 hour**, $\phi = 69.91^\circ \gg 45^\circ$: conductivity is increasing with
depth over the depth being sensed, because the current is concentrated in the
conductive layer at 150–250 km.

At **100 days**, $\phi = 45.75^\circ$, very close to $45^\circ$: at that period the
depth sampled (thousands of kilometres in skin-depth terms) is dominated by the
$30\ \Omega$m half-space, and the response is very nearly that of a uniform
medium. Almost all the structure above has been averaged out.

The $45^\circ$ rule therefore does two jobs: it identifies the sign of the
conductivity gradient, and it flags the periods at which a sounding loses
resolution because it is looking through the whole structure rather than at a
particular layer.

---

## ★★7 — Melt versus water in the mantle (specification)

**MT quantities.** The $\rho_a$ and phase curves over periods from $10^{3}$ to
$10^{5}$ s, the conductance of the conductor, and — crucially — whether the
conductor has a lateral geometry consistent with a compact body (melt) or a broad
sheet (graphite or fluid in a shear zone): the tipper and a 2-D/3-D inversion.

**Independent observations.**

1. **Seismic shear velocity and attenuation.** Melt lowers $v_s$ and strongly
   increases attenuation; dissolved hydrogen lowers $v_s$ more modestly and
   changes attenuation much less.
2. **Heat flow.** A melt interpretation requires a geotherm above the solidus at
   the conductor's depth; a conductive geotherm excludes melt and forces the
   water or graphite interpretation.
3. **Anisotropy**: shear-wave splitting and MT anisotropy both respond to
   aligned melt or aligned graphite.

**Decision rule.** If the heat flow requires a subsolidus geotherm at that depth,
melt is excluded regardless of the conductance; if $v_s$ is depressed with strong
attenuation and the geotherm is elevated, melt is required; otherwise hydration is
the default, and the burden of proof rests on whichever alternative needs the
least special pleading.

---

## ★★8 — Periods for a 5000 km source

With $\rho = 10\ \Omega$m and $k = 2\pi/5.0\times10^{6} = 1.257\times10^{-6}$
rad m$^{-1}$:

| Period | $\delta$ (km) | $k\delta$ | Justified? |
|---|---|---|---|
| 1 day | 467.8 | 0.59 | marginal ($\approx0.6$) |
| 10 days | 1479.4 | 1.86 | no |

So the interpretation is defensible only for periods of a day or less with this
source width, at a few tenths of $k\delta$. The deepest depth that may be claimed
is that reached at the longest acceptable period, i.e. of order $\delta$ at one
day, about 470 km — and even that is beyond the depth at which the source
geometry has been neglected. Prudence suggests halving it, or reporting the
response as a conductance at shallower depths until the source geometry is
modelled.
