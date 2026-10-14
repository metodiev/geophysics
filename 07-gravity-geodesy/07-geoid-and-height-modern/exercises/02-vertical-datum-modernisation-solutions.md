# Solutions — 07-07-02 Vertical Datum Modernisation and National Height Systems

> **Read after attempting the exercises.** Numbers were computed, not estimated
> by hand. All values are teaching values.

Lesson: [02 Vertical Datum Modernisation](../02-vertical-datum-modernisation.md).

---

## ★1 — Dynamic height

$$H_{\text{dyn}} = \frac{C}{\gamma_{45}} = \frac{5000}{9.806199}
= 509.881\ \mathrm{m}.$$

**The gravity used is the normal gravity at $45^\circ$ latitude**, a fixed
convention chosen so that dynamic heights are *internationally comparable* and
differ from the true potential only by the constant factor $\gamma_{45}$. It is a
convention rather than a physical quantity, which is exactly why dynamic heights
are useful for comparing stations in different countries and useless for
engineering: a dynamic height is not a distance from the geoid.

---

## ★2 — Orthometric correction estimate

Over a line with a gravity change $\Delta g$ and a height gain $\Delta H$,

$$\text{correction} \approx \frac{\Delta g}{g}\,\Delta H .$$

Take a typical $0.02\ \mathrm{mGal\,m^{-1}}$ Bouguer-like change over $500\
\mathrm{m}$ of climb: $\Delta g = 0.02\times500 = 10\ \mathrm{mGal}
= 1.0\times10^{-4}\ \mathrm{m\,s^{-2}}$, so

$$\text{correction} \approx \frac{1.0\times10^{-4}}{9.81}\times500
= 5.1\times10^{-3}\ \mathrm{m} = 5.1\ \mathrm{mm}.$$

**It depends on (i) the fractional gravity change along the path and (ii) the
height gain.** Over a 100 km line with a $500\ \mathrm{m}$ climb it is of order
millimetres; for a national network with kilometres of relief and tens of degrees
of latitude it reaches centimetres to decimetres (the demonstration measures
$15.9\ \mathrm{mm}$ over 223 km with an 800 m range).

---

## ★3 — A datum offset cancels in differences

Let every published height be $H_i' = H_i + \delta$ with $\delta$ constant. Then

$$H_2' - H_1' = (H_2+\delta) - (H_1+\delta) = H_2 - H_1 . \qquad\blacksquare$$

The offset cancels exactly, because it is the same at both points: a difference of
heights is insensitive to the origin, and sensitive only to the height *system*
(through the gravity used at each point). This is why levelling networks can be
adjusted, and used for engineering, long before anyone knows the offset to the
geoid — and why a datum offset is a problem only when absolute heights cross a
boundary.

---

## ★4 — Three heights for $C = 6000\ \mathrm{m^{2}\,s^{-2}}$

$$H_{\text{dyn}} = \frac{6000}{9.806199} = 611.857\ \mathrm{m},$$
$$H_{\text{ortho}} = \frac{6000}{9.8070} = 611.809\ \mathrm{m},$$
$$H_{\text{norm}} = \frac{6000}{9.8085} = 611.715\ \mathrm{m}.$$

Differences: $H_{\text{dyn}} - H_{\text{ortho}} = 0.048\ \mathrm{m}$;
$H_{\text{ortho}} - H_{\text{norm}} = 0.094\ \mathrm{m}$.

**Kind of quantity:** each difference is a *definitional* difference — the same
geopotential number divided by a different gravity — not an error, not a
measurement difference, and not something that can be reduced by more data. It is
exactly the size of the term that a transformation between two national height
systems must carry (see the demonstration's $0.288\ \mathrm{m}$ orthometric-to-normal
difference at 800 m height and $48^\circ$N).

---

## ★5 — Crossover lengths

**Absolute heights.** Levelling error $= 2\times10^{-3}\sqrt{L}$ m ($L$ in km);
GNSS+geoid error $= 0.030$ m. Setting them equal:

$$\sqrt{L} = \frac{0.030}{2\times10^{-3}} = 15
\;\Longrightarrow\; L = 225\ \mathrm{km}.$$

**Differences.** The GNSS error is white, so a difference over $L$ carries
$\sqrt{2}\times$ the point GNSS error:
$\sigma_{\Delta h} = \sqrt{2}\times1.5 = 2.12\ \mathrm{cm}$ (for a $1.5\ \mathrm{cm}$
GNSS point error). The geoid error is $90\%$ correlated, so in the difference it
contributes $\sqrt{2(1-0.9)}\,\sigma_N = 0.447\times3.0 = 1.34\ \mathrm{cm}$.
Total: $\sigma_{\Delta H} = \sqrt{2.12^2+1.34^2} = 2.51\ \mathrm{cm}$.
Levelling over the same baseline: $2\times10^{-3}\sqrt{L}$ m, equal to $0.0251$ m
at $L = 158\ \mathrm{km}$.

So with a $2\ \mathrm{mm\,\sqrt{km}^{-1}}$ levelling standard and a better geoid,
GNSS+geoid wins beyond roughly $160$–$225\ \mathrm{km}$ — shorter than in the
lesson's example, because both the levelling standard and the geoid error were
changed in opposite directions. **The crossover is a property of the error model,
and cannot be quoted from memory.**

---

## ★6 — Where each error term dominates

**Absolute heights matter:** flood-risk mapping (a height relative to a fixed
origin, where a decimetre changes the mapped flood extent); sea-level change
studies (the datum offset and the land motion add to the signal); cross-border
engineering where two datums meet; satellite altimetry calibration.

In these cases the **geoid model error and the datum offset** dominate: a $2\
\mathrm{cm}$ geoid error over an area is a systematic bowl or tilt, and the offset
is a constant that must be documented.

**Differences matter:** deformation monitoring (subsidence, volcanism, tectonic
strain), construction levelling, hydraulic gradients, and the internal consistency
of a levelling network.

In these cases the **baseline-dependent terms** dominate: the white GNSS error
(grows as $\sqrt{2}$ relative to a point) and the *un*-correlated part of the geoid
error. A fully correlated error is irrelevant for a difference, and the datum
offset is irrelevant everywhere.

**The practical consequence:** a modernisation study should report both errors, and
it should report the *correlation length* of its geoid error, because that single
number decides which of the two use cases benefits.

---

## ★7 — Making a datum change verifiable (specification)

| item to publish | diagnostic that detects an error in it | independent data that resolves it |
|---|---|---|
| the height system (orthometric/normal, gravity field) | compare the same benchmarks in both systems over a latitude range: an error in the *system* produces a latitude-dependent difference | a second country's transformation across the same latitude band |
| the datum offset and its uncertainty | compare the transformation's offset against independent tide-gauge/geoid comparisons | a GNSS/levelling comparison at a tide gauge |
| the geoid model (degree, data, epoch, error) | differences between GNSS-derived and levelled orthometric heights along a long line: a *tilt* or *bowl* pattern is a geoid error | an independent geoid model, or a levelling line that was not used in the model |
| the transformation equation and its domain | apply it to benchmarks *not* used to fit it | withheld checkpoints (the key item) |
| the epoch and the vertical motion | repeat the GNSS observations after some years: a difference not explained by the transformation is vertical motion or benchmark instability | continuous GNSS or InSAR |
| tide system and loading conventions | the same station documented under two conventions | the conventions' published definitions |

**The single most important item is the last-row-of-the-table discipline: a set of
*withheld* benchmarks.** Without checkpoints the transformation is a model
statement; with them it is a measurement, and its residuals are the only honest
accuracy figure available. Everything else on the list can be wrong in a way that
the transformation itself cannot detect.

---

## ★8 — Sensitivity to the mean-gravity hypothesis (specification)

1. **Model.** A synthetic station with a geopotential number $C$ and a *stated*
   density structure between the surface and the geoid, giving a true mean gravity
   $\bar g_{\text{true}} = g_{\text{surface}} + \Delta_{\text{density}}$, where
   $\Delta_{\text{density}}$ depends on the crustal density and the height.
2. **Two hypotheses.** (a) The Poincaré–Prey form with a free-air-like gradient
   ($+0.0424\ \mathrm{mGal\,m^{-1}}$), and (b) the same with a wrong density
   (say $2400$ instead of $2670\ \mathrm{kg\,m^{-3}}$).
3. **Diagnostic.** The bias in the orthometric height,
   $\delta H \approx -H\,\delta\bar g/\bar g$, as a function of $H$ and the density
   error. For a $500\ \mathrm{m}$ height and a $1\ \mathrm{mGal}$ error in $\bar g$:
   $\delta H = 500\times10^{-5}/9.81 = 5.1\times10^{-4}\ \mathrm{m} = 0.5\
   \mathrm{mm}$; for a $2\ \mathrm{km}$ height and $5\ \mathrm{mGal}$:
   $2\times10^{3}\times5\times10^{-5}/9.81 = 1.0\ \mathrm{cm}$.
4. **Normal heights.** Repeating with $H^{*} = C/\bar\gamma$ shows **no
   dependence on crustal density at all**, because $\bar\gamma$ is a *definition*
   from the normal field. The bias is therefore zero by construction.
5. **Which is affected and why.** Orthometric heights depend on a hypothesis about
   the density between the station and the geoid; normal heights do not. This is
   the standard argument for normal height systems, and its price is that a
   normal height is not a distance from the geoid — the two systems make different
   trade-offs between physical meaning and freedom from hypotheses, and a national
   choice should state which one it has made.
