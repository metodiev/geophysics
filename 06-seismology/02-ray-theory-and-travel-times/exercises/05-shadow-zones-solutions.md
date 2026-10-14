# Solutions — 06-02-05 Shadow Zones, Triplications and the Low-Velocity Zone

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand; where a problem admits more than one defensible answer it is said so.

Lesson: [05 Shadow Zones, Triplications and the Low-Velocity Zone](../05-shadow-zones.md).

---

## ★1 — The velocity drop and the grazing ray parameter

$$\frac{v_{\text{below}}}{v_{\text{above}}} = \frac{8.05}{13.70} = 0.587591,
\qquad 1 - 0.587591 = 41.2\%\ \text{slower}.$$

Radius at the boundary: $r = 6371 - 2889 = 3482$ km. A grazing ray has
$\sin i = 1$ there, so

$$p = \frac{r}{v_{\text{above}}} = \frac{3482}{13.70}
= 254.161\ \mathrm{s\,rad^{-1}}
= 254.161 \times \frac{\pi}{180} = 4.435939\ \mathrm{s\,deg^{-1}}.$$

For comparison, the demonstration's own table (with the velocity sampled at
2888 km, $13.6906\ \mathrm{km\,s^{-1}}$) gives $4.438985\
\mathrm{s\,deg^{-1}}$ from the same formula, and the engine reports
$4.438920\ \mathrm{s\,deg^{-1}}$ for the branch that fills the shadow. All three
agree to five figures; the small differences are the sampling of the velocity step.

---

## ★2 — Width of the shadow

$$113.75 - 98.378 = 15.372^\circ, \qquad
15.372 \times 111.195 = 1709.3\ \mathrm{km}.$$

So the shadow at a 10 km source is a strip about 1700 km wide on the surface, and
its width changes with source depth (from $15.35^\circ$ at the surface to
$16.84^\circ$ at 600 km, per the demonstration's table).

---

## ★3 — Which interfaces produce head waves

| interface | $v$ above | $v$ below | $\sin i_c = v_{\text{above}}/v_{\text{below}}$ | head wave? |
|---|---|---|---|---|
| 1 | 6.20 | 5.80 | 1.0690 | no — no real critical angle |
| 2 | 5.80 | 6.80 | 0.8529 | yes |

Criterion: a head wave exists iff the medium below is *faster*, i.e.
$v_{\text{below}} > v_{\text{above}}$, equivalently
$\sin i_c \le 1$. Interface 1 is hidden; interface 2 refracts. Note that the
hidden interface still contributes to the intercept of the branch below it —
the 6.20 layer's thickness enters that branch's $\tau$ — so the hidden layer is
not absent from the data, only unlabelled by it.

---

## ★4 — Interface 3 of the demonstration's stack, by hand

$p = 1/v_4 = 1/7.50 = 0.133333\ \mathrm{s\,km^{-1}}$. Layers above:
$v_1 = 6.00$ (10 km), $v_2 = 5.70$ (10 km), $v_3 = 6.50$ (10 km).

| layer | $\sin\theta = pv$ | $\theta$ (°) | $\cos\theta$ | $\eta$ (s km⁻¹) | leg $h\tan\theta$ (km) |
|---|---|---|---|---|---|
| 1 | 0.800000 | 53.1301 | 0.600000 | 0.100000 | 13.3333 |
| 2 | 0.760000 | 49.4642 | 0.649923 | 0.114022 | 11.6937 |
| 3 | 0.866667 | 60.0736 | 0.498888 | 0.076752 | 17.3720 |

$$\tau = 2\left[10(0.100000) + 10(0.114021) + 10(0.076752)\right]
= 2(2.907735) = 5.815470\ \mathrm{s} \ ✔$$
$$X_c = 2(13.3333 + 11.6937 + 17.3720) = 2(42.399010)
= 84.7980\ \mathrm{km} \ ✔$$

Both match the demonstration's printed values. Note the check that they must:
$\tau/2 = \sum h_i\eta_i$ and $X_c/2 = \sum h_i p/\eta_i$ are the two slowness
integrals of Lesson 03, evaluated at $p = 1/v_4$.

---

## ★5 — Reading the arrival counts

- **Seven arrivals at one distance** means seven distinct ray parameters return to
  that offset with different travel times: the travel-time curve is folded, and
  $T(\Delta)$ is not single-valued in $p$. The count is a *measured* number, not
  an inference.
- **Where the caustics are.** A caustic is where $\mathrm{d}T/\mathrm{d}\Delta$
  is stationary, i.e. where two branches meet tangentially. The counts drop from 7
  to 3 between 25° and 22° and fluctuate 5-7-5-7-5 below that, so the folds lie in
  the 15°–25° band, and the outer edge of the triplication region is around 25°
  where the count settles at 3.
- **What an inversion assuming one arrival per distance does.** At 16° it would
  take one of the seven times and treat it as *the* arrival. Because the branches
  cross in time (note that at 16° two arrivals share essentially the same time,
  225.11 s, and at 18° two share 252.81 s), a single pick identifies a ray
  parameter only if the branch is also identified. A one-arrival inversion can
  therefore assign a pick to the wrong branch, and the resulting model would fit
  the picks while mislabelling the ray paths — a model that is wrong in a way the
  residuals would not reveal.

---

## ★6 — Inverting an intercept near the detection threshold

$$\tau = 2h\sqrt{v_1^{-2} - v_2^{-2}}
\quad\Longrightarrow\quad
\sqrt{v_1^{-2} - v_2^{-2}} = \frac{\tau}{2h} .$$

For $\tau = 0.50$ s, $h = 10$ km:
$\sqrt{\cdot} = 0.50/20 = 0.025000$; $v_1^{-2} = 0.027778$;
$v_2^{-2} = 0.027778 - 0.000625 = 0.027153$;
$v_2 = 6.0687\ \mathrm{km\,s^{-1}}$.

For $\tau = 0.25$ s:
$\sqrt{\cdot} = 0.012500$; $v_2^{-2} = 0.027778 - 0.000156 = 0.027622$;
$v_2 = 6.0169\ \mathrm{km\,s^{-1}}$.

**Implication.** Halving the measured intercept changed the inferred velocity by
$(6.0687 - 6.0169)/6.0687 = 0.85\%$ — less than one per cent. Because
$\sqrt{v_1^{-2} - v_2^{-2}}$ is flat in $v_2$ just above the threshold
$v_2 = v_1$, a detection near threshold pins the velocity tightly while saying
almost nothing about depth (the depth still trades off against velocity exactly
as in Lesson 02). Far above threshold the sensitivity reverses: the same
arithmetic with $\tau = 2.0$ s would give a much larger velocity change for the
same change in $\tau$.

---

## ★7 — Distinguishing a low-velocity zone from a hidden layer

Two hypotheses with different *signatures*:

| hypothesis | first-arrival curve | amplitudes |
|---|---|---|
| Hidden layer (a single velocity decrease, no fast lid beneath) | one branch with a normal slope; no branch from the LVZ at any offset | no later branch, no amplitude anomaly; the record simply lacks the arrivals |
| Genuine LVZ (a decrease *and* a return to higher velocity below) | the curve folds: a triplication with a gap in offset, then a later branch with a *negative* apparent slowness jump | the shadow-side amplitudes fall (geometric spreading and tunnelling through the low-velocity waveguide), then brighten at the triplication caustic; a strong later arrival exists |
| Both | the difference is the return branch | the LVZ case has energy where the hidden-layer case has none |

**The test.** Look for the *return* branch: a later arrival whose moveout is
consistent with a ray that escaped below the low-velocity region. In the
hidden-layer hypothesis no such arrival can exist, at any offset, with any
amplitude. Second, measure amplitudes across the offset range where the curve is
ambiguous: the LVZ predicts a trough on the shadow side and a sharp caustic
brightening, whereas the hidden layer predicts a smooth decay of the single
branch. In the tabulated numbers of this lesson the maximum arrival count is 7,
which is the observable counterpart of the folds — a hidden layer produces a
count of 1.

---

## ★8 — Core radius from the shadow boundary

At the shadow boundary the ray grazes the core, so its turning radius is the core
radius and $\sin i = 1$ there:

$$r_{\text{core}} = p\,v_{\text{CMB}} = 4.438920\ \mathrm{s\,deg^{-1}}
\times \frac{180}{\pi} = 254.3352\ \mathrm{s\,rad^{-1}},$$
$$r_{\text{core}} = 254.3352 \times 13.6906 = 3482.0\ \mathrm{km}
\quad\Longrightarrow\quad
\text{boundary depth} = 6371 - 3482 = 2889\ \mathrm{km}.$$

Both numbers reproduce the model's own values exactly, as they must, because the
velocity used was the model's velocity at the model's boundary.

**The extra assumption** is the identification itself: that the terminating ray is
*a ray that grazes the core*, rather than one that turns in the mantle a little
above it or one that is lost to another mechanism. That identification comes from
the refraction analysis (a velocity drop refracts rays away from the vertical) and
from the abruptness with which the branch family ends.

**Why it is a consistency argument.** The recovered radius is computed from a
velocity and a ray parameter that were themselves read off the same model, so the
calculation shows that the model's shadow boundary, its velocity at the boundary,
and its core radius are mutually consistent — not that the Earth's core has that
radius. An independent measurement needs the same numbers to come from
observations and hold across different paths and azimuths.
