---
id: 14-04-03
title: "Seawater Intrusion and Coastal Aquifer Monitoring"
level: doctoral
prereqs: ["14-04-01", "14-01-02", "14-01-05", "14-02-02", "14-03-02"]
tags: [hydrology, hydrogeophysics, saline-intrusion, ghyben-herzberg, coastal-aquifer, resistivity, transition-zone, time-lapse]
---

# Seawater Intrusion and Coastal Aquifer Monitoring

> **All models and data in this module are SYNTHETIC.** The end-member
> conductivities, the dispersive transition length, the porosity and the clay
> surface conductance are chosen teaching values for an idealised coastal
> archetype. No real coastline, well field or monitoring programme is described.
> The only standard constants used are the densities of fresh water and seawater,
> $1000$ and $1025\ \mathrm{kg\,m^{-3}}$.

Seawater intrusion is the easiest groundwater target in geophysics and the
hardest to manage. It is easy because the contrast is in the *fluid*: a factor of
about eighty in bulk resistivity between fresh and saline pore water, larger than
any rock-type contrast in the near surface, and therefore detectable almost
anywhere with almost any electrical method. It is hard because the interface
moves for reasons that have nothing to do with the survey — a change in recharge,
a season of pumping, a tidal cycle — and because the quantity that hydrology
regulates is a *head*, while the quantity geophysics measures is a *resistivity*
that responds to both salinity and porosity.

This lesson derives the Ghyben–Herzberg relation and its brutal 40:1
amplification, treats the dispersive transition zone as the thing a survey
actually images, and quantifies the one ambiguity that ruins more surveys than
any other: a clay-rich rock with fresh water has the same conductivity as a
clean rock with brackish water.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the Ghyben–Herzberg relation $z = \rho_f h/(\rho_s - \rho_f)$ from
   hydrostatic equilibrium, and **explain** the 40:1 amplification for standard
   densities.
2. **Compute** the interface rise produced by a stated head drop, and **state**
   the fresh-water volume change per unit area that accompanies it.
3. **Distinguish** the sharp hydrostatic interface from the dispersive transition
   zone, and **compute** the 10–90% width of the latter.
4. **Convert** a mixed-salinity pore fluid to a bulk resistivity, and **explain**
   why the resistivity is not a linear function of the saline fraction.
5. **Design** a time-lapse sounding for a stated interface movement, and
   **justify** the electrode spacings from the sensitivity rather than from
   habit.
6. **Quantify** the clay-versus-salinity ambiguity and **show** that its size
   depends on the strength of the salinity contrast.
7. **State** the Dupuit–Ghyben–Herzberg assumptions and **identify** the two that
   fail first in a real coastal aquifer.

## Prerequisites

- [14-04-01 Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md) —
  the concentration-to-property-to-data chain.
- [14-01-02 Aquifers, Porosity, Permeability and Storativity](../01-hydrology-fundamentals/02-aquifer-types-and-properties.md) —
  heads, transmissivity and the coastal setting.
- [14-01-05 Groundwater Chemistry and Salinity](../01-hydrology-fundamentals/05-groundwater-chemistry.md) —
  what salinity is and how it is expressed.
- [14-02-02 EM and TDEM for Groundwater Exploration](../02-hydrogeophysics-methods/02-em-for-hydrology.md) —
  the methods that map conductive pore fluid over a coastline.
- [14-03-02 Archie's Law and Saturation Estimation](../03-petrophysics-hydrology/02-archie-and-saturation.md) —
  the pore-fluid-to-bulk conversion.

## 1. Intuition: a stable balance of two densities

Fresh water floating on seawater is a density-stratified system, and its
interface sits where the pressures balance. The fresh water stands higher — a
lens with a water table a metre or two above sea level — and the saline water
beneath it presses upward. The balance is unforgiving because the density
difference is only $2.5\%$: a head change of a few centimetres moves the interface
by metres, and that amplification is both the physical content of the
Ghyben–Herzberg relation and the reason coastal aquifers are so easy to damage.

Geophysics enters because the interface is a conductivity boundary. Where the
pore water is saline the bulk resistivity is tens of times lower; that boundary
is what ERT, EM induction and TDEM image.

## 2. Definitions

**Fresh-water head** $h$: the water-table elevation above sea level, in metres.

**Interface depth** $z$: the depth below sea level at which fresh water meets
saline water, in metres. In the sharp-interface idealisation it is a surface; in
reality it is a transition zone several to tens of metres thick.

**Saline fraction** $c \in [0,1]$: the volume fraction of seawater in the pore
water, used here only as a mixing parameter for the property model.

**End members.** A fresh pore-water conductivity $\sigma_f$ and a saline
$\sigma_s$. The demonstration uses $\sigma_f = 0.050\ \mathrm{S\,m^{-1}}$ and
$\sigma_s = 4.00\ \mathrm{S\,m^{-1}}$ (a synthetic pair spanning the range from a
fresh coastal aquifer to something close to full-strength seawater), with a
linear mixing of *conductivities*:

$$
\sigma_w(c) = \sigma_f + c\,(\sigma_s - \sigma_f) .
$$

The linear-in-conductivity mixing is a modelling choice, not a law; the
non-linearity of real conductivity–salinity relations is one of the standard
sources of bias in this subject, and the model must say which quantity it mixed.

## 3. Derivation of the Ghyben–Herzberg relation

Take the interface at depth $z$ below sea level, and a water table at height $h$
above it. Consider the pressure at the interface, where the two columns meet.

*From the fresh side*, the column is fresh water of height $h + z$:

$$
p = \rho_f g (h + z).
$$

*From the saline side*, the column is saline water of height $z$ from sea level:

$$
p = \rho_s g z .
$$

Equating (the interface is a surface of equal pressure in the static
idealisation):

$$
\rho_f (h + z) = \rho_s z
\;\;\Longrightarrow\;\;
z = \frac{\rho_f}{\rho_s - \rho_f}\,h .
$$

With $\rho_f = 1000$ and $\rho_s = 1025\ \mathrm{kg\,m^{-3}}$,

$$
\boxed{\;z = \frac{1000}{25}\,h = 40\,h\;}
$$

so **one metre of fresh head supports forty metres of fresh water below sea
level**. The demonstration prints the whole family: $h = 0.25 \to z = 10.0\
\mathrm{m}$; $h = 1.00 \to 40.0\ \mathrm{m}$; $h = 2.00 \to 80.0\ \mathrm{m}$;
$h = 5.00 \to 200.0\ \mathrm{m}$.

Differentiating gives the sensitivity that matters operationally:

$$
\frac{\partial z}{\partial h} = \frac{\rho_f}{\rho_s - \rho_f} = 40 .
$$

A head drop of $\delta h$ raises the interface by $40\,\delta h$. The
demonstration's table:

| $\delta h$ (m) | new head (m) | new $z$ (m) | interface rise (m) |
|---|---|---|---|
| 0.05 | 1.95 | 78.0 | 2.0 |
| 0.10 | 1.90 | 76.0 | 4.0 |
| 0.25 | 1.75 | 70.0 | 10.0 |
| 0.50 | 1.50 | 60.0 | 20.0 |

A $5\%$ head change ($0.10\ \mathrm{m}$ of $2.00\ \mathrm{m}$) is a $5\%$
interface change ($4.0\ \mathrm{m}$ of $80.0\ \mathrm{m}$) — the ratio is exactly
the amplification. The fresh-water volume per unit area is
$\phi(h + z)$, so losing $0.10\ \mathrm{m}$ of head costs
$\phi\times(4.0+0.10) = 0.30\times4.1 = 1.23\ \mathrm{m^{3}}$ of fresh water per
square metre. **The lens is far more sensitive than the water table**, and a
monitoring programme that watches only head is watching the wrong end of a 40:1
lever.

## 4. The transition zone, which is what a survey images

The sharp interface is a hydrostatic idealisation. Transport disperses it, and a
sensible teaching profile is

$$
c(z) = \frac{1}{2}\operatorname{erfc}\!\left(\frac{z_i - z}{2\sigma}\right),
$$

with $\sigma$ a dispersive length scale. The demonstration uses
$z_i = 20.0\ \mathrm{m}$ and $\sigma = 3.0\ \mathrm{m}$:

| $z$ (m) | 0 | 10 | 15 | 20 | 25 | 30 | 40 |
|---|---|---|---|---|---|---|---|
| $c$ | 0.0000 | 0.0092 | 0.1193 | 0.5000 | 0.8807 | 0.9908 | 1.0000 |
| $\sigma_w$ ($\mathrm{S\,m^{-1}}$) | 0.0500 | 0.0864 | 0.5212 | 2.0250 | 3.5288 | 3.9636 | 4.0000 |
| $\rho_b$ ($\Omega$ m) | 222.20 | 128.63 | 21.32 | 5.49 | 3.15 | 2.80 | 2.78 |

The 10–90% width of the error-function profile is
$2\times1.2816\sqrt{2}\,\sigma = 10.87\ \mathrm{m}$, i.e. **54% of the interface
depth**. Two statements follow, and they are different statements: the
Ghyben–Herzberg interface is a hydrostatic surface; the transition zone is a
transport feature. A survey maps the second and reports a depth that is compared
with the first, and the comparison is only as good as the assumption that
$\sigma$ is small.

## 5. Worked example 1 — head, interface and volume

**Problem.** A synthetic coastal aquifer has $\phi = 0.30$, interface at
$z = 80.0\ \mathrm{m}$ (so $h = 2.00\ \mathrm{m}$). Pumping lowers the head by
$0.25\ \mathrm{m}$. Compute the interface rise, the depth to the interface after
the change, and the volume of fresh water lost per square metre of aquifer.

**Solution.** $z_0 = 40 h_0 = 40\times2.00 = 80.0\ \mathrm{m}$. After the change
$h_1 = 1.75\ \mathrm{m}$ and $z_1 = 40\times1.75 = 70.0\ \mathrm{m}$: the
interface rises by $10.0\ \mathrm{m}$ (the demonstration prints this row).

Fresh-water volume per unit area before:
$V_0 = \phi(h_0 + z_0) = 0.30\times82.00 = 24.60\ \mathrm{m^{3}\,m^{-2}}$. After:
$V_1 = 0.30\times(1.75 + 70.0) = 0.30\times71.75 = 21.525\ \mathrm{m^{3}\,m^{-2}}$.
The loss is $3.075\ \mathrm{m^{3}\,m^{-2}}$ — **a $12.5\%$ loss of fresh water
for a $12.5\%$ loss of head**, because both terms of $h + z$ scale together. The
amplification is in the *depth*, and the volume follows the head directly.

## 6. Worked example 2 — the resistivity profile, and why it is not linear

**Problem.** With $\phi = 0.30$, $a = 1$, $m = 2$ (so $\sigma_b = 0.09\sigma_w$),
compute the bulk resistivity at $c = 0$, $0.10$, $0.50$, $1.00$ and the fraction
of the *log* contrast each represents.

**Solution.**

| $c$ | $\rho_b$ ($\Omega$ m) | fraction of the log contrast |
|---|---|---|
| 0.00 | 222.22 | 0.000 |
| 0.10 | 24.97 | 0.499 |
| 0.25 | 10.71 | 0.692 |
| 0.50 | 5.49 | 0.845 |
| 0.90 | 3.08 | 0.976 |
| 1.00 | 2.78 | 1.000 |

Two features are worth stating precisely.

- The **contrast factor is 80.0** ($222.22/2.78$) — larger than any lithological
  contrast in the shallow subsurface. This is why saline intrusion is the
  easiest target in groundwater geophysics.
- The resistivity is **not** linear in $c$: a saline fraction of only $0.10$
  already accounts for half of the log contrast, because the mixture is a
  reciprocal of a linear function. Any interpretation that reads "half the
  contrast" as "half the salinity" is wrong by a factor of five at this point.

## 7. Time-lapse detection of a 1 m interface rise

The demonstration computes the two-layer Wenner response for
$\rho_1 = 222.2\ \Omega\,\mathrm{m}$ (fresh) over
$\rho_2 = 2.78\ \Omega\,\mathrm{m}$ (saline) at $z_i = 20\ \mathrm{m}$, and
repeats it with the interface at $19\ \mathrm{m}$:

| spacing $a$ (m) | $z_i = 20$ m | $z_i = 19$ m | change |
|---|---|---|---|
| 5 | 220.06 | 219.72 | $-0.16\%$ |
| 10 | 207.65 | 205.61 | $-0.98\%$ |
| 20 | 153.34 | 146.74 | $-4.30\%$ |
| 40 | 54.07 | 47.77 | $-11.64\%$ |

With a stated $2\%$ (one-sigma) repeatability, the 1 m rise is detectable at
$20\ \mathrm{m}$ and $40\ \mathrm{m}$ and **not** at $5\ \mathrm{m}$ or
$10\ \mathrm{m}$. The fractional change is largest where the spacing is
comparable to or larger than the interface depth. Two design rules follow, and
both are the opposite of habit:

1. The **smallest separations are the least useful** for tracking interface
   movement; they sample only the fresh layer and see nothing change.
2. The **value of a survey is in its repeatability**, not in its resolution. A
   $2\%$ repeatability detects a 1 m interface rise at $a = 20\ \mathrm{m}$; a
   $5\%$ repeatability would not, however many electrodes were added.

## 8. The clay ambiguity, quantified

A bulk conductivity is a statement about the product $\phi^{m}\sigma_w$ plus any
matrix conduction. A clay-rich rock with fresh water therefore looks like a clean
rock with brackish water, and the size of the equivalence is computable. With a
clay surface conductance $\sigma_\text{clay}$ added in parallel, the saline
fraction a clean rock would need to match a clayey rock with *fresh* water is

$$
c_\text{eq} = \frac{\sigma_\text{clay}}{\phi^{m}\left(\sigma_s - \sigma_f\right)} .
$$

The demonstration evaluates this for $\sigma_\text{clay} = 0.020\
\mathrm{S\,m^{-1}}$:

| $\sigma_s$ ($\mathrm{S\,m^{-1}}$) | end member | $c_\text{eq}$ at $\phi = 0.25$ | at $0.30$ | at $0.35$ |
|---|---|---|---|---|
| 4.00 | saline | 0.081 | 0.056 | 0.041 |
| 1.00 | brackish | 0.337 | 0.234 | 0.172 |
| 0.50 | weakly brackish | 0.711 | 0.494 | 0.363 |

**The ambiguity is proportional to how little conductivity the intrusion adds.**
Against a full-strength saline contrast the clay masquerades as a saline fraction
of at most $0.08$, which is small; against a weakly brackish contrast it
degenerates entirely — at $\sigma_s = 0.50\ \mathrm{S\,m^{-1}}$ and
$\phi = 0.25$ a **fresh** clayey rock is indistinguishable from one that is
$71\%$ saline. This is why a coastline whose pristine pore water is already
conductive is the hard case, and why the honest response is to measure a clay
indicator (natural gamma, cation exchange capacity, or an NMR bound-fluid
fraction) alongside the conductivity.

## 9. Assumptions and regime of validity

**Dupuit–Ghyben–Herzberg.** (i) The interface is *sharp*: dispersion is ignored,
which is the largest single error and is quantified in Section 4. (ii) The water
is *static*: no flow is considered, so the relation says nothing about how fast
the interface moves. (iii) Flow in each zone is horizontal (Dupuit), which fails
where the interface outcrops. (iv) No tidal or seasonal forcing, no recharge
transient, no density-driven circulation. (v) The saline end member is motionless
at the seawater density.

**Consequences of the assumptions failing.** Upconing beneath a pumping well — the
local rise of the interface into the screened interval — is a *flow* phenomenon
that the static relation cannot predict at all, and it is usually how an aquifer
is lost. A pumping well near the coast should be monitored, not merely modelled
with a 40:1 rule.

**Property model.** A clean matrix, a known and uniform porosity, full
saturation, and a stated mixing relation. In a real aquifer the porosity varies
by a factor of two, and the ambiguity of Section 8 applies in full.

**Survey model.** The two-layer sounding of Section 7 assumes a flat interface
and a uniform cover; a dipping or undulating interface is smeared by the array's
sensitivity kernel, which is the same smearing that limits the resolution of a
sharp plume edge (lesson 01 §9).

## 10. Python demonstration

[`code/saline_intrusion_demo.py`](./code/saline_intrusion_demo.py) prints the
Ghyben–Herzberg table, the head-drop table, the transition-zone profile and its
width, the resistivity-versus-salinity table with the log-contrast fractions, the
time-lapse sounding differences, and the clay-equivalence table.

```bash
cd 14-hydrology-hydrogeophysics/04-contaminant-and-environmental/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python saline_intrusion_demo.py
```

## 11. Exercises

Graded problems are in
[`exercises/03-saline-intrusion-exercises.md`](./exercises/03-saline-intrusion-exercises.md)
with worked solutions in
[`exercises/03-saline-intrusion-solutions.md`](./exercises/03-saline-intrusion-solutions.md).

## Mastery checkpoint

Answer without notes.

> **(a)** Derive $z = \rho_f h/(\rho_s-\rho_f)$ and evaluate it for
> $\rho_s = 1025\ \mathrm{kg\,m^{-3}}$ and $h = 1.50\ \mathrm{m}$.
> **(b)** The head then falls by $0.20\ \mathrm{m}$; compute the interface rise
> and the fresh-water volume change per unit area for $\phi = 0.25$.
> **(c)** State the difference between the Ghyben–Herzberg interface and the
> transition zone, and compute the 10–90% width of the latter for
> $\sigma = 5.0\ \mathrm{m}$.
> **(d)** For $\sigma_f = 0.05$, $\sigma_s = 4.00\ \mathrm{S\,m^{-1}}$,
> $\phi = 0.30$, $m = 2$, compute the bulk resistivity at $c = 0$ and $c = 0.2$,
> and state the fraction of the log contrast at $c = 0.2$.
> **(e)** A $1\ \mathrm{m}$ interface rise must be detected with a $2\%$
> repeatability. At which spacings, relative to the interface depth, would you
> place the array, and why not smaller?
> **(f)** Name the two Dupuit–Ghyben–Herzberg assumptions that fail first, and
> the phenomenon that each hides.

## Common pitfalls

1. **Reading the transition zone as the interface.** They differ by the
   dispersive width, which is often a large fraction of the depth.
2. **Treating resistivity as linear in salinity.** Half the log contrast is a
   saline fraction of about $0.10$, not $0.5$.
3. **Using the static relation to predict pumping upconing.** It cannot; upconing
   is a flow problem.
4. **Calling a conductive layer saline without a clay check.** The ambiguity is
   quantified in Section 8 and is unbounded for a weak contrast.
5. **Designing a time-lapse survey with the smallest spacings.** They are blind
   to interface movement.
6. **Comparing a measured interface depth with a Ghyben–Herzberg prediction
   without stating the dispersive width.** The comparison is otherwise
   meaningless.
7. **Watching only head.** The lever is 40:1 and the head record is the early
   warning, not the measurement.

## Related modules

- [01 Contaminant Plumes and Their Geophysical Signature](01-contaminant-plumes.md).
- [02 Landfill Investigation and Leachate Mapping](02-landfill-investigation.md) —
  the sounding tool used in Section 7.
- [04 Acid Mine Drainage and Mining Environmental Geophysics](04-acid-mine-drainage.md) —
  salinity generated by reaction.
- [Module 14-02 Hydrogeophysical Methods](../02-hydrogeophysics-methods/README.md) —
  ERT, EM and TDEM surveys over a coastline.
- [Module 14-01 Hydrology Fundamentals](../01-hydrology-fundamentals/README.md) —
  coastal hydrogeology and groundwater chemistry.
- [Module 02-06 Fluid Mechanics](../../02-physics/06-fluid-mechanics/README.md) —
  the buoyancy and porous-medium flow behind the density balance.
