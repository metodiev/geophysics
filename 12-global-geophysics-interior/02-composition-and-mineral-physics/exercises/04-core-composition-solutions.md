# Solutions — 12-02-04 Core Composition, Light Elements and the Geodynamo

Worked solutions for
[04-core-composition-exercises.md](./04-core-composition-exercises.md).
The lesson is
[04 Core Composition, Light Elements and the Geodynamo](../04-core-composition.md).
All models are **SYNTHETIC**; every number below comes from the arithmetic shown
here and from the printed output of
[`code/core_composition_demo.py`](../code/core_composition_demo.py).

Useful relations:

$$\frac{dP}{dr} = -\rho g,\qquad
\Delta = 1 - \frac{\rho_\text{model}}{\rho_\text{Fe}},\qquad
\frac{1}{\rho_\text{mix}} = \frac{1-x}{\rho_\text{Fe}} + \frac{x}{\rho_\text{L}},$$
$$\frac{dT}{dr} = -\frac{\alpha g T}{C_p},\qquad
Q_\text{ad} = 4\pi R_c^{2}k\left|\frac{dT}{dr}\right|_\text{CMB},\qquad
\text{age} = \frac{D\,R_\text{ICB}}{\Gamma},\qquad
\Gamma = \frac{Q_\text{CMB}-Q_\text{ad}}{C_\text{core}+\Lambda_L},$$
with $\Lambda_L = L\rho_\text{ICB}4\pi R_\text{ICB}^{2}/D$.

---

## ★ Foundational

### ★1 — Pressure across the outer core

Take $\rho$ linear from 9.90 to 12.15 g cm$^{-3}$ and $g$ linear from 10.559 to
4.456 m s$^{-2}$ across the 2258.5 km of outer core. The means are

$$\bar\rho = \frac{9.90+12.15}{2} = 11.025\ \mathrm{g\,cm^{-3}}
= 1.1025\times10^{4}\ \mathrm{kg\,m^{-3}},$$
$$\bar g = \frac{10.559+4.456}{2} = 7.5075\ \mathrm{m\,s^{-2}}.$$

The product of two linear profiles is not exactly their product of means, but it is
close, so

$$\Delta P \simeq \bar\rho\,\bar g\,\Delta r
= (1.1025\times10^{4})(7.5075)(2.2585\times10^{6})
= 1.869\times10^{11}\ \mathrm{Pa} = 186.9\ \mathrm{GPa}.$$

The model gives $315.0 - 126.2 = 188.8$ GPa, so the hand calculation is low by 1.0 %.
The reason is the **convexity of $g(r)$**: gravity across the outer core is not
linear in $r$, because the mass that generates it lies mostly *outside* the outer
core. At the mid-thickness radius (2321.5 km) the model has $g = 7.635$ m s$^{-2}$
rather than the arithmetic mean of the endpoints, 7.508 m s$^{-2}$. Replacing the
true $g(r)$ by a straight line therefore underestimates $\int\rho g\,dr$, and the
integral is 2.4 % larger than the linear-profile result. A mean-value estimate is
better than a linear treatment here (the two errors partly cancel) but it is still
1 % low — which is the sort of number that decides whether a $P_\text{ICB}$ is
consistent with a mineral-physics phase boundary or not. The fix is to integrate
numerically, as the demonstration does.

### ★2 — Light-element fraction at the ICB

$$\frac{1}{\rho_\text{mix}} = \frac{1}{12.150} = 0.0823045,\qquad
\frac{1}{\rho_\text{Fe}} = \frac{1}{12.874} = 0.0776759,\qquad
\frac{1}{\rho_\text{L}} = \frac{1}{6.0} = 0.1666667\ \mathrm{cm^{3}g^{-1}}.$$

$$x = \frac{0.0823045-0.0776759}{0.1666667-0.0776759}
= \frac{0.0046286}{0.0889908} = 0.0520 = 5.2\ \text{mass}\,\%.$$

The density deficit itself is

$$\Delta = 1 - \frac{12.150}{12.874} = 0.0562 = 5.6\,\%.$$

Note the ratio: a 5.6 % deficit corresponds to only 5.2 mass % of a light element
because the light element is roughly half as dense as the iron, so a given mass
replaces more volume than it fills. **The deficit is not the composition** — the two
differ by the density contrast, which is itself an assumption.

### ★3 — The adiabatic gradient at the ICB

$$\left|\frac{dT}{dr}\right|_\text{ICB} = \frac{\alpha g T}{C_p}
= \frac{(10^{-5})(4.456)(4963)}{800}
= 2.764\times10^{-4}\ \mathrm{K\,m^{-1}} = 0.276\ \mathrm{K\,km^{-1}}.$$

Multiplying by the 2258.5 km thickness with this *constant* gradient gives

$$\Delta T = 0.276 \times 2258.5 = 624\ \mathrm{K},$$

against the model's 963 K. The difference is not an error: the gradient is
proportional to $g$, which falls by a factor of 2.4 from the CMB to the ICB, so most
of the temperature rise accumulates in the upper part of the outer core. A
one-point estimate of a rising, radially varying gradient always underestimates the
integral. (The proper calculation integrates $d\ln T/dr = -\alpha g/C_p$; because
$T$ appears on the right-hand side, the rise is also slightly super-linear in $g$.)

## ★★ Applied

### ★★4 — Conducted heat flow, cooling rate and age at $k = 75$

Core-side area: $4\pi R_c^{2} = 4\pi(3.48\times10^{6})^{2}
= 1.522\times10^{14}$ m$^{2}$.

$$Q_\text{ad} = 4\pi R_c^{2}k\left|\frac{dT}{dr}\right|_\text{CMB}
= (1.522\times10^{14})(75)(5.28\times10^{-4})
= 6.03\times10^{12}\ \mathrm{W} = 6.03\ \mathrm{TW}.$$

Excess heat available:

$$Q_\text{CMB} - Q_\text{ad} = 10 - 6.03 = 3.97\ \mathrm{TW}.$$

Cooling rate without latent heat, with $C_\text{core} = 1.53\times10^{27}$ J K$^{-1}$:

$$\Gamma = \frac{3.97\times10^{12}}{1.53\times10^{27}}
= 2.59\times10^{-15}\ \mathrm{K\,s^{-1}} = 0.082\ \mathrm{K\,Myr^{-1}}.$$

Age, with $D = 1.26\times10^{-4}$ K m$^{-1}$ and $R_\text{ICB} = 1.2215\times10^{6}$ m:

$$\text{age} = \frac{(1.26\times10^{-4})(1.2215\times10^{6})}{2.59\times10^{-15}}
= 5.94\times10^{16}\ \mathrm{s} = 1.88\ \mathrm{Gyr}.$$

Adding the latent-heat coefficient $4.74\times10^{26}$ J K$^{-1}$ (31 % of
$C_\text{core}$) gives $\Gamma = 3.97\times10^{12}/2.00\times10^{27}
= 1.98\times10^{-15}$ K s$^{-1}$ and an age of **2.46 Gyr**. Freezing the inner core
must therefore remove ~31 % more heat than cooling alone, so the same budget buys a
31 % longer growth time. Of the 10 TW, 6.03 TW is silently conducted and only
3.97 TW drives everything else — including the dynamo.

### ★★5 — Decomposing the ICB density jump

If freezing changed nothing but the phase, the inner core at the ICB would be

$$\rho_\text{ic}^\text{no-composition} = \rho_\text{oc}^\text{ICB} + \Delta\rho_\text{melting}
= 12.150 + 0.39 = 12.540\ \mathrm{g\,cm^{-3}},$$

and its deficit against the solid-iron reference (13.260 g cm$^{-3}$) would be

$$\Delta_\text{ic} = 1 - \frac{12.540}{13.260} = 0.0543 = 5.4\,\%,$$

essentially the same as the outer core's 5.6 %. The model's actual value,
12.750 g cm$^{-3}$, is 0.21 g cm$^{-3}$ denser than this, so the seismological jump
*requires* the inner core to be **enriched in iron** relative to the liquid it froze
from: its deficit falls to 3.8 %. That difference is a partition-coefficient
observable — the inner core records the composition of the liquid at the moment of
freezing, which is why the ICB jump is one of the few direct compositional
constraints in the whole core.

Caveat worth stating in any write-up: the split into 0.39 (melting) and 0.21
(composition) comes from *assuming* a 3 % melting density jump. Change that
assumption by half and the compositional part changes by nearly half.

### ★★6 — The uniform-composition consistency test

With $x = 0.078$, $\rho_\text{Fe}^\text{ICB} = 12.874$ and
$\rho_\text{L} = 6.0$ g cm$^{-3}$:

$$\frac{1}{\rho_\text{pred}} = \frac{1-0.078}{12.874} + \frac{0.078}{6.0}
= 0.071617 + 0.013000 = 0.084617\ \mathrm{cm^{3}g^{-1}},$$

$$\rho_\text{pred} = 11.819\ \mathrm{g\,cm^{-3}},$$

against the model's 12.150 g cm$^{-3}$ — the prediction is

$$\frac{12.150}{11.819} - 1 = +2.8\,\%$$

too light. Two physical ways to remove the mismatch:

1. **Stratification**: the light-element fraction is not uniform but decreases
   inward, e.g. because the top of the outer core is stably stratified against
   convection or because the core has been progressively depleted as the inner core
   grew. A stratified layer is independently suggested by seismic and geomagnetic
   observations of the topmost outer core.
2. **The EOS, temperature or light-element density is wrong by 2–3 %**: a slightly
   stiffer iron EOS at ICB pressure, a higher core temperature at depth, or a
   different light-element density all shift the prediction by about this much. The
   honest conclusion is that the deficit *profile* is a constraint that a single
   uniform composition does not satisfy — and that 2.8 % is right at the level where
   this class of model becomes ambiguous.

### ★★7 — Dynamo diagnostics for $\sigma = 5\times10^{5}$ S m$^{-1}$

$$\eta = \frac{1}{\mu_0\sigma} = \frac{1}{(4\pi\times10^{-7})(5\times10^{5})}
= \frac{1}{0.6283} = 1.592\ \mathrm{m^{2}s^{-1}},$$

$$Rm = \frac{UL}{\eta} = \frac{(8\times10^{-4})(2.258\times10^{6})}{1.592}
= \frac{1806}{1.592} = 1135,$$

$$\tau_\eta = \frac{L^{2}}{\eta} = \frac{(2.258\times10^{6})^{2}}{1.592}
= 3.20\times10^{12}\ \mathrm{s} = 1.02\times10^{5}\ \mathrm{yr}.$$

Dynamo action is plausible: $Rm \sim 10^{3}$ is two orders of magnitude above the
$\mathcal{O}(10\text{–}100)$ threshold. The same calculation shows the flip side:
because $\tau_\eta$ is only $10^{5}$ yr, a field that stopped being generated would
disappear almost immediately on geological time scales — so the palaeomagnetic record
of a field older than $10^{9}$ yr is evidence of a sustained dynamo, and hence of a
sustained buoyancy source.

## ★★★ Research-oriented

### ★★★8 — Distinguishing oxygen from silicon

A workable workflow, from the present state of a model to a discrimination:

1. **Fix the density constraint.** Choose the light-element mass fraction that
   matches the seismological density deficit at the CMB (7.8 mass % here, with its
   stated $\rho_\text{L}$ assumption). *Discriminates:* nothing yet — both candidates
   pass by construction.
2. **Compute the elastic constants of the candidate alloys.** Ab initio or
   experimental elastic constants for Fe–O and Fe–Si at core $P,T$, using the methods
   of [12-02-03](../03-ab-initio-mineral-physics.md) and
   [12-02-02](../02-high-pressure-experiments.md). *Discriminator:* the ratio
   $\partial \ln v_p / \partial \ln \rho$ at constant composition, which differs
   between O (interstitial, weakly coupled, low sound speed) and Si (substitutional,
   stiffer). **This step uses no seismological data.**
3. **Build the elastic aggregate and compute $v_p(\rho)$ along the outer core.** Apply
   the same volume-averaging rules used for the mantle, and compare the predicted
   $v_p$ profile with the reference model's. *Discriminator:* the slope
   $d v_p/d\rho$ — a purely seismic quantity.
4. **Consistency check against a second observable.** Whether the *same* candidate
   also explains the density deficit at the ICB without stratification; if it does not,
   the candidate needs the extra machinery of section 4.3. *This is a check, not a
   measurement.*
5. **Check the cosmochemical budget.** How much O or Si is available in the bulk
   Earth after accounting for the silicate mantle? A candidate that needs more of an
   element than exists is excluded regardless of the seismological fit.
6. **Predict the partitioning at the ICB.** Melting experiments/calculations give the
   partition coefficients; the sign and size of the predicted ICB density jump then
   become a prediction rather than a fitted number.
7. **Check the melting-curve slope**, since the candidate changes the liquidus and
   hence where the adiabat crosses it.
8. **Predict the free-core/dynamo consequences**: the light-element flux, the
   buoyancy available, and whether a thermal dynamo is needed at all.

The discriminating quantities are (i) the *slope* $dv_p/d\rho$ rather than $v_p$
itself, (ii) the ICB density jump, and (iii) the cosmochemical budget. Reporting only
"a 7.8 % deficit matches a light alloy" is not a discrimination.

### ★★★9 — The conductivity threshold

From $k^{*} = Q_\text{CMB}/(4\pi R_c^{2}|dT/dr|_\text{CMB})$ with
$4\pi R_c^{2}|dT/dr|_\text{CMB} = (1.522\times10^{14})(5.28\times10^{-4})
= 8.04\times10^{10}$ W m$^{-1}$K$^{-1}$:

| $Q_\text{CMB}$ | $k^{*}$ (W m$^{-1}$ K$^{-1}$) | $Q_\text{ad}$ at $k = 200$ |
|---|---|---|
| 8 TW | 99.6 | 16.07 TW |
| 12 TW | 149.3 | 16.07 TW |
| 16 TW | 199.3 | 16.07 TW |

(For $k = 200$ W m$^{-1}$ K$^{-1}$ the conducted flow is
$200 \times 8.04\times10^{10} = 1.61\times10^{13}$ W $= 16.1$ TW, so a CMB heat flow
of about 16 TW — with nothing left over for cooling — would be needed just to break
even.)

Accepting a 16 TW CMB heat flow is not a small adjustment: it is ~1.5 times the
model's assumed value, and it must be carried by the mantle. Consequences that would
have to be re-examined:

* **Mantle heat transport**: the higher flux implies faster mantle convection, more
  vigorous plate tectonics, and a correspondingly hotter mantle.
* **Core–mantle boundary temperature**: a larger flux requires a larger temperature
  drop across the thermal boundary layer, which raises $T_\text{CMB}$ and shifts the
  whole adiabat (and the inner-core age) upward.
* **Additional heat sources**: a radiogenic component in the core (e.g. $^{40}$K) or
  greater secular cooling would relieve the budget without demanding more from the
  mantle — the classic alternative to a low conductivity.
* **The other observables are not independent of these changes**: raising $T_\text{CMB}$
  changes the thermal EOS, the density deficit, and therefore the light-element
  budget computed in this lesson.

This is the sense in which the paradox is a *consistency problem across subfields*
rather than an isolated number: any single fix perturbs the others.

### ★★★10 — Age sensitivity and the leverage of the threshold

With latent heat, $\Gamma = (Q_\text{CMB}-Q_\text{ad})/(C_\text{core}+\Lambda_L)$ with
$C_\text{core}+\Lambda_L = 2.00\times10^{27}$ J K$^{-1}$, and
$\text{age} = D R_\text{ICB}/\Gamma$, where $D R_\text{ICB} = 153.9$ K:

| $k$ (W m$^{-1}$ K$^{-1}$) | $Q_\text{ad}$ (TW) | excess (TW) | age with latent heat (Gyr) |
|---|---|---|---|
| 100 | 8.04 | 1.97 | 4.98 |
| 118 | 9.48 | 0.52 | 18.9 |

Over 18 % more conductivity the age grows by a factor of 3.8. Differentiating,

$$\text{age} = \frac{D R_\text{ICB}\left(C_\text{core}+\Lambda_L\right)}
{Q_\text{CMB} - 8.04\times10^{10}k}
\quad\Longrightarrow\quad
\frac{d(\text{age})}{dk} \propto \frac{1}{\left(Q_\text{CMB}-Q_\text{ad}\right)^{2}} .$$

The gradient of the age with respect to conductivity diverges as
$Q_\text{ad}\to Q_\text{CMB}$, and the age itself diverges too. Hence:

* An observed age (were one available) would constrain $k$ only through the
  *difference* of two large, individually uncertain numbers;
* near the threshold, an arbitrarily small change in $k$ or $Q_\text{CMB}$ changes
  the age by geological amounts — the inverse problem is not merely ill-conditioned
  but singular at the threshold;
* a measured age of, say, 2 Gyr is consistent with $k \approx 90$, with $k \approx 60$
  and a lower $Q_\text{CMB}$, or with $k = 120$ and a higher $Q_\text{CMB}$.

Settling the conductivity question therefore requires an *independent* determination
of $k$ (from resistivity measurements or ab initio electron transport), an
independent determination of the CMB heat flow (from mantle dynamics and the
post-perovskite boundary of [12-01-05](../../01-seismic-structure-of-the-earth/05-core-mantle-boundary.md)),
or both — not a seismological one.
---

## Mastery checkpoint — worked solution

> Core mass $1.90\times10^{24}$ kg, $C_p = 800$ J kg$^{-1}$ K$^{-1}$, adiabatic
> gradient at the CMB $5.3\times10^{-4}$ K m$^{-1}$, $R_c = 3480$ km,
> $D = 1.2\times10^{-4}$ K m$^{-1}$.

### (a) $Q_\text{ad}$ at $k = 40$ W m$^{-1}$ K$^{-1}$

$$4\pi R_c^{2} = 4\pi(3.48\times10^{6})^{2} = 1.522\times10^{14}\ \mathrm{m^{2}},$$
$$Q_\text{ad} = (1.522\times10^{14})(40)(5.3\times10^{-4})
= 3.23\times10^{12}\ \mathrm{W} = 3.23\ \mathrm{TW}.$$

### (b) Cooling rate for $Q_\text{CMB} = 11$ TW

$$C_\text{core} = M_\text{core}C_p = (1.90\times10^{24})(800)
= 1.52\times10^{27}\ \mathrm{J\,K^{-1}},$$
$$\Gamma = \frac{11-3.23}{1.52\times10^{27}}\times10^{12}
= \frac{7.77\times10^{12}}{1.52\times10^{27}}
= 5.12\times10^{-15}\ \mathrm{K\,s^{-1}} = 0.162\ \mathrm{K\,Myr^{-1}}.$$

### (c) Inner-core age (no latent heat), and a reason it differs

$$R_\text{ICB} = 1221.5\ \mathrm{km},\qquad
D R_\text{ICB} = (1.2\times10^{-4})(1.2215\times10^{6}) = 146.6\ \mathrm{K},$$
$$\text{age} = \frac{146.6}{5.12\times10^{-15}}
= 2.87\times10^{16}\ \mathrm{s} = 0.91\ \mathrm{Gyr}.$$

Including latent heat: $\Lambda_L = L\rho_\text{ICB}4\pi R_\text{ICB}^{2}/D
= 2.5\times10^{5}(12750)(1.875\times10^{13})/(1.2\times10^{-4})
= 4.98\times10^{26}$ J K$^{-1}$, i.e. 33 % of $C_\text{core}$, giving
$\Gamma = 7.77\times10^{12}/2.02\times10^{27} = 3.85\times10^{-15}$ K s$^{-1}$ and
**age $= 1.21$ Gyr**. Two other reasons the true value would differ: gravitational
energy release is neglected (it powers the dynamo and would *reduce* the age), and
the melting-curve slope is assumed rather than measured (it sets $D$ directly).

### (d) Threshold conductivity

$$k^{*} = \frac{Q_\text{CMB}}{4\pi R_c^{2}\left|dT/dr\right|_\text{CMB}}
= \frac{11\times10^{12}}{1.522\times10^{14}\times5.3\times10^{-4}}
= \frac{11\times10^{12}}{8.07\times10^{10}} = 136\ \mathrm{W\,m^{-1}K^{-1}}.$$

Above $k \approx 136$ W m$^{-1}$ K$^{-1}$ the conducted flux alone exceeds the
11 TW leaving the core: the excess becomes negative, the core stops cooling, and the
inner core cannot grow at all.

---

## Module mastery checkpoint (from the module README)

> Pure-iron reference at 126 GPa and 4000 K: $\rho_\text{Fe} = 10.794$ g cm$^{-3}$;
> at the ICB: $\rho_\text{Fe} = 12.874$ g cm$^{-3}$. Model densities: 9.900 g cm$^{-3}$
> at the top of the outer core, 12.150 g cm$^{-3}$ at the ICB.

### (a) Density deficit at the CMB

$$\Delta = 1 - \frac{9.900}{10.794} = 1 - 0.91718 = 0.0828 = 8.3\,\%.$$

### (b) Light-element fraction with $\rho_\text{L} = 5.0$ g cm$^{-3}$

$$x = \frac{1/9.900 - 1/10.794}{1/5.0 - 1/10.794}
= \frac{0.1010101 - 0.0926441}{0.2000000 - 0.0926441}
= \frac{0.0083660}{0.1073559} = 0.0779 = 7.8\ \text{mass}\,\%.$$

The assumption that makes the number meaningful is **ideal volume additivity** — the
light element occupies its own volume, with no interaction and no compression
distinct from the iron's — together with the single assumed density contrast. Without
those, no mass fraction follows from a density at all.

### (c) The same deficit with $\rho_\text{L} = 6.5$ g cm$^{-3}$

$$x = \frac{0.0083660}{1/6.5 - 0.0926441}
= \frac{0.0083660}{0.1538462 - 0.0926441} = \frac{0.0083660}{0.0612021}
= 0.1367 = 13.7\ \text{mass}\,\%.$$

The deficit alone cannot decide: the light-element density sits in the *denominator*
as a contrast, so the inference inherits its full uncertainty — the same 8.3 %
deficit is 7.8 % or 13.7 % light elements according to an input that seismology does
not constrain. This is why sound-velocity (not just density) comparisons, partitioning
arguments and cosmochemical budgets are required to break the degeneracy.

### (d) The deficit with depth, and a uniformly mixed core

$$\Delta_\text{ICB} = 1 - \frac{12.150}{12.874} = 0.0562 = 5.6\,\%,$$

so the deficit **shrinks** with depth (8.3 % → 5.6 %). A uniformly mixed core would
have the *same* light-element fraction at both levels, which under the mixing model
predicts 11.819 g cm$^{-3}$ at the ICB — 2.8 % lighter than the model's
12.150 g cm$^{-3}$. Since the deficit profile is better determined than any
composition, the mismatch is a real constraint: either the light-element fraction
decreases with depth (a stratified outer core), or the reference EOS, the core
temperature profile or the assumed light-element density is wrong by a few per cent.
Either way, the *shape* of the deficit is a measurement-like quantity, and it is
harder for a wrong model to reproduce than its average value.

---

## Marking and sanity guide

* Any density comparison must state the $P$ **and** $T$; a thermal correction of
  4–5 % is not a detail.
* A light-element mass fraction must come with the assumed $\rho_\text{L}$.
* An age must come with $k$, $Q_\text{CMB}$, $D$ and the treatment of latent heat.
* Units: check that $Q_\text{ad}$ comes out in watts (W m$^{-1}$ K$^{-1}$
  $\times$ m$^{2}$ $\times$ K m$^{-1}$ = W), that $\Gamma$ is a rate (J s$^{-1}$/J K$^{-1}$
  = K s$^{-1}$), and that $D R_\text{ICB}$ is a temperature (K m$^{-1}$ $\times$ m = K).
* A dynamo answer must quote $Rm$, not merely "the core is hot and moving".
