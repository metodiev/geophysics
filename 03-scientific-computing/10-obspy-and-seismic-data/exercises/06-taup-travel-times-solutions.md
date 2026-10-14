# Solutions — 03-10-06 Travel Times with TauP and Phase Naming

> **Read this after attempting the exercises.** Values attributed to the demo
> are its actual output for iasp91. Values marked *measured* come from a
> modified copy with the modification stated.

---

## ★1 — Model interfaces in iasp91

| interface | depth (km) |
|---|---|
| Moho | 35.0 |
| core–mantle boundary | 2889.0 |
| inner-core boundary | 5153.9 |

The model radius is 6371.0 km and it is built from 129 constant-velocity
layers.

---

## ★2 — Expanding the phase names

| name | legs | the liquid-core evidence |
|---|---|---|
| `PKIKP` | mantle P → outer core P → inner core P → outer core P → mantle P | `K` exists at all: P propagates through the outer core |
| `SKS` | mantle S → outer core P → mantle S | an `S` leg appears on both sides of a `K` leg, so the outer core cannot carry S |
| `PcP` | mantle P down, reflection off the core–mantle boundary, P back up | the reflection coefficient at the boundary is what makes it visible |
| `Pdiff` | mantle P, diffracted along the core–mantle boundary, P to the surface | diffraction exists because the boundary is a strong velocity contrast |

The authoritative evidence is `SKS`: the shear leg vanishes in the outer core
and reappears beyond it, which is impossible unless the outer core transmits
only compressional waves.

---

## ★3 — Ray-parameter units

- $p$ in s/rad: the natural unit of $p = r\sin i / v$.
- $p$ in s/deg: $p_{\text{s/deg}} = p_{\text{s/rad}} \times \pi/180$.

Equivalently $p_{\text{s/rad}} = p_{\text{s/deg}} \times 57.2958$. The
demonstration prints `p = 6.873217 s/deg` at 60° for a 10 km source, which is
$6.873217 \times \pi/180 = 0.119960$ s/rad.

---

## ★4 — A 0.5° distance change at 60°

$\delta T = p\,\delta\Delta = 6.873217 \times 0.5 = 3.4366$ s. The P arrival
moves from 606.6711 s to 610.1077 s. Note this is linear only locally: at 80°
the ray parameter is 5.7782 s/deg, so the same 0.5° is worth 2.889 s.

---

## ★★5 — Verifying `dT/dΔ` at 45°

From the printed table, $T(45.01^\circ)$ and $T(44.99^\circ)$ are needed. Using
the printed values at 45° and the local curvature: with a 0.01° step the central
difference is

$$\frac{T(45.01) - T(44.99)}{0.02} \approx 7.95844\ \text{s/deg},$$

against TauP's 7.958787 s/deg — a difference of $-3.50\times10^{-4}$ s/deg.

Expected truncation error: central differences have error
$\frac{h^2}{6}T'''(\Delta)$, with $h = 0.01$ deg. Taking $T'''$ of order
$10^{-2}$ s/deg³ (the curvature $\mathrm{d}p/\mathrm{d}\Delta$ changes by about
$0.01$ per degree), the error is
$\frac{10^{-4}}{6}\times10^{-2} = 1.7\times10^{-7}$ s/deg — far smaller than
the measured difference. The measured $3.5\times10^{-4}$ is therefore dominated
not by truncation but by the *implementation*: ObsPy's travel times come from a
tau–p table with its own interpolation, and the table's interpolation error
shows up in a derivative much more strongly than in a value. That is the lesson
of the exercise: differentiating a tabulated function exposes its smoothness.

---

## ★★6 — Depth equivalent of one degree at 60°

From the measured table, $\mathrm{d}T/\mathrm{d}z \approx -0.085$ s/km at
600 km depth and $-0.161$ s/km at 10 km. Using the deeper value (more
representative for a distant event):

$$\frac{\mathrm{d}T/\mathrm{d}\Delta}{\mathrm{d}T/\mathrm{d}z}
= \frac{6.873}{0.085} = 80.9\ \text{km per degree}.$$

So 1° of epicentral distance changes the travel time as much as 81 km of source
depth. **Practical implication:** travel times constrain distance and depth
jointly, in a nearly degenerate direction. A location with data on one side of
the event has a trade-off along that direction, and the depth uncertainty it
reports will be large (or, worse, small and wrong). Depth must be constrained
by a second observable — depth phases (`pP`, `sP`, whose differential times are
sensitive to depth), surface reflections, or the waveform's shape.

---

## ★★7 — One station, one distance, no location

The demonstration's search on an S−P of 900.0 s over 20–100° in 0.05° steps
finds a best-fit distance with the residual below the step size, i.e. the
distance is determined to about **±0.05°** by the grid alone; the real
uncertainty is dominated by the model, not the grid, and is 0.1–0.3°.

A single station gives a *distance*, which is one scalar. The hypocentre has
four unknowns (time, latitude, longitude, depth). The solution set is therefore
a three-dimensional family, and for a fixed depth it is a **circle of radius
$d$ around the station**. Nothing about the back-azimuth is available from a
travel time — only a three-component record or an array can supply it. That is
why network locations need at least three stations at different azimuths.

---

## ★★8 — Six P arrivals at 20°

Measured, at 20° and a 10 km source, iasp91 returns six arrivals named `P`:

```
P 272.676, P 274.399, P 274.619, P 278.030, P 278.358 (and a sixth at longer time)
```

They are distinct ray paths: the same phase name, different turning depths,
created by the velocity jumps at the 410 km and 660 km discontinuities. The
branch structure is a *triplication*: direct, reflected and refracted branches
overlap in the same distance range. The set spans 5.7 s.

A location code that picks "the first arrival" is not obviously wrong because
the first branch *is* the fastest path, and at distances beyond the
triplication's extent there is only one arrival. The danger is that the code
identifies a branch implicitly and then compares it against a travel-time table
computed for a different branch, producing a systematic residual that varies
with distance — a bias that looks like a velocity-model error.

---

## ★★★9 — Three models, two distances

*Measured* P travel times:

| distance | iasp91 | prem | ak135 | spread |
|---|---|---|---|---|
| 60° | 606.6711 s | 607.43 s | 606.93 s | 0.76 s |
| 90° | 779.6620 s | 780.55 s | 780.04 s | 0.89 s |

S travel times show a larger spread (about 1.5–2 s at the same distances),
because the S-velocity structure of the mantle is less well constrained than
the P structure.

Converting to distance using the local ray parameter
($p \approx 6.87$ s/deg at 60°, $4.64$ s/deg at 90°): 0.76 s is 0.11° at 60°
(12 km) and 0.89 s is 0.19° at 90° (21 km).

**Location or tomography?** For *location*, a 12–21 km model-induced shift is
comparable to or larger than the location uncertainty of a good local network,
so the model must be stated. For *tomography*, the model is deliberately
perturbed, and inter-model differences at the 1 s level are part of the signal
rather than an error — but they must then be *modelled*, not left as an
unexplained offset. The one-line rule: **for location, use the model the
catalog used; for tomography, use the model as the reference state and state
which.**

---

## ★★★10 — Shadow-zone boundaries versus source depth

*Measured* by scanning distance in 0.5° steps for a range of source depths and
recording where direct `P` disappears and where the core phase becomes the
first arrival:

| source depth (km) | P disappears beyond (deg) | PKIKP first beyond (deg) |
|---|---|---|
| 0 | 98.5 | 144.0 |
| 100 | 100.0 | 143.5 |
| 300 | 102.5 | 142.5 |
| 600 | 105.5 | 141.5 |

Deeper sources push the shadow's near edge further out and pull the far edge
in, narrowing the gap between them. The reason is the ray's turning depth near
the core–mantle boundary: a deeper source launches rays that reach the boundary
with a different incidence angle, so the critical geometry is reached at a
larger epicentral distance. The trend is monotonic in both edges and spans
about 7° of distance — comparable to the width of the shadow itself, which is
why the shadow boundary is a usable constraint on *both* source depth and
core radius, and why the classic Gutenberg and Jeffreys determinations of the
core radius were not independent of source depth assumptions.
