---
id: 05-04-07
title: "Electrical Properties, Archie's Law and Clay Effects"
level: advanced
prereqs: ["05-04-01"]
tags: [archie, resistivity, clay, shaly-sand, cementation-exponent]
---

# Electrical Properties, Archie's Law and Clay Effects

## Learning objectives

1. **Derive** the form of Archie's law from a geometric scaling argument, and
   state what each exponent means.
2. **State** the assumptions of Archie's law and identify the rock types that
   violate each.
3. **Demonstrate** the failure of Archie's law in clay-bearing rock, and
   quantify the bias as a function of porosity.
4. **Describe** the conduction mechanisms that operate in parallel, and how a
   shaly-sand model adds an explicit clay term.
5. **Explain** why a resistivity measurement is a *bulk* property that depends on
   the fluid and on the geometry of the pore space.

## Prerequisites

- [05-04-01 Porosity, Density and Velocity](./01-porosity-density-velocity.md)
- [02-07-06 EM Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md)

## 1. Intuition

Current in a water-saturated rock flows through the pore water, along a
tortuous path whose length and connectivity depend on porosity. Add a
conducting mineral (clay, sulphide, graphite) and a second, solid-state path
appears. Archie's law describes the first path only; it therefore overestimates
water saturation whenever the second path is active. The failure is not
subtle — the demonstration below returns a saturation greater than 1.

## 2. Archie's law

$$S_w^n = \frac{a\,R_w}{\phi^m R_t}, \qquad \text{or} \qquad
R_t = \frac{a\,R_w}{\phi^m S_w^n}.$$

| Symbol | Meaning | Unit | Typical role |
|---|---|---|---|
| $R_t$ | bulk (true) resistivity of the formation | Ω·m | measured |
| $R_w$ | pore-water resistivity | Ω·m | measured or estimated |
| $\phi$ | porosity | dimensionless | measured |
| $S_w$ | water saturation | dimensionless | unknown to be found |
| $a$ | empirical prefactor | dimensionless | fitted, often near 1 |
| $m$ | cementation exponent | dimensionless | typically 1.3–3 |
| $n$ | saturation exponent | dimensionless | typically near 2 |

Dimensional check: $R_w/(\phi^m R_t)$ is dimensionless (Ω·m cancels), so the
left side must be dimensionless — it is. ✓

## 3. Derivation of the scaling form

Consider a cube of side $L$ saturated with water. Conduction along a
tortuous path of length $L_e = L\,L_r$ (tortuosity factor $L_r \ge 1$) and
effective cross-section $A_e = L^2\,\phi/L_r$ (volume conservation). Resistance
along the path:

$$R = \frac{R_w L_e}{A_e} = \frac{R_w\,L\,L_r}{L^2\phi/L_r}
= \frac{R_w L_r^2}{L\phi}.$$

Bulk resistivity $R_t = R(L^2/L) = R_w L_r^2/\phi$. Comparing with Archie's
form $R_t = aR_w/\phi^m$ shows:

- $m = 1$ corresponds to straight tubes ($L_r = 1$, $a = 1$);
- $m > 1$ arises because tortuosity *increases* as porosity decreases, which is
  an empirical statement (tortuosity is not known a priori);
- $a$ absorbs the geometry and the prefactor $L_r^2$.

Hence $m$ and $a$ are not constants of nature: they are fits. This is why they
should be measured on cores from the interval, not taken from a table.

The saturation exponent $n$ enters because the conducting water occupies only a
fraction $S_w$ of the pore space, and its distribution changes the tortuosity
path further — again empirically.

### 3.1 What the cementation exponent means: tortuosity, inverted

Section 3 showed that $R_t = R_wL_r^2/\phi$ and that Archie's form implies $m=1$
for straight tubes. Invert the comparison to read off what $m$ *is*.

Matching the two expressions for $R_t$,

$$\frac{R_wL_r^2}{\phi} = \frac{aR_w}{\phi^m}
\qquad\Longrightarrow\qquad
L_r^2 = a\,\phi^{\,1-m}
\qquad\Longrightarrow\qquad
\boxed{\;L_r = \sqrt{a}\,\phi^{\,(1-m)/2}\;}$$

So the cementation exponent is a statement about **how tortuosity grows as
porosity falls**. For $a = 1$:

| $m$ | $L_r$ at $\phi = 0.20$ | interpretation |
|---|---|---|
| 1.0 | 1.000 | straight, non-intersecting tubes |
| 1.5 | 1.495 | gently winding paths |
| 2.0 | 2.236 | the classical value: path length $=\phi^{-1/2}$ |
| 2.2 | 2.627 | more tortuous, typical of cemented or shaly sands |
| 3.0 | 5.000 | very tortuous; vuggy or highly cemented rock |

**Physical interpretation.** $m = 2$ is not a magic number: it is the exponent for
which path length grows as $\phi^{-1/2}$, and it corresponds to a pore network
whose connectivity degrades in a particular way. Higher $m$ means the current
must travel *further* through a smaller cross-section, and the sandstone
literature's range 1.8–2.2 corresponds to tortuosities of 2.1–2.6 at
$\phi = 0.20$ — physically similar rocks. **A value of $m = 3$ asserts a
tortuosity of 5 at 20% porosity, which is a strong geological claim about the
pore geometry**, not a fitting parameter to be chosen for convenience.

### 3.2 Inverting Archie: sensitivity to $m$ and $n$, and the impossibility threshold

Archie's law is invariably inverted, so the error propagation matters more than
the forward relation.

$$S_w = \left(\frac{aR_w}{\phi^mR_t}\right)^{1/n} .$$

Taking logarithms, $\ln S_w = \frac1n\left[\ln a + \ln R_w - m\ln\phi - \ln R_t\right]$,
and differentiating with respect to each input:

$$\frac{\partial\ln S_w}{\partial m} = -\frac{\ln\phi}{n},
\qquad
\frac{\partial\ln S_w}{\partial n}
= -\frac{\ln\left(aR_w/\phi^mR_t\right)}{n^2}
= -\frac{\ln S_w^n}{n^2},
\qquad
\frac{\partial\ln S_w}{\partial\ln R_w} = \frac{1}{n} .$$

**Numbers** for a typical case ($\phi = 0.15$, $S_w = 0.4$, $n = 2$, $m = 2$):

| error in input | resulting relative error in $S_w$ |
|---|---|
| $\Delta m = +0.1$ | $|\ln 0.15|\cdot0.1/2 = 9.5\%$ |
| $\Delta n = +0.1$ | $|2\ln0.4|\cdot0.1/4 = 4.6\%$ |
| $\Delta R_w/R_w = +10\%$ | 5.0% |
| $\Delta R_t/R_t = +2\%$ | 1.0% |

**The exponent $m$ is the dominant error source**, and it is usually assumed. This
is the quantitative form of the warning in the lesson's Section 4: **the
saturation log is only as good as the cementation exponent's provenance.**

**The impossibility threshold.** Since $S_w \le 1$ requires
$aR_w/(\phi^mR_t) \le 1$,

$$R_t \;\ge\; \frac{aR_w}{\phi^m} \quad\text{for an admissible saturation.}$$

For $a = 1$, $R_w = 0.5$ Ω·m, $\phi = 0.05$, $m = 2$ the threshold is
$\mathbf{200\ \Omega\cdot m}$: **any formation resistivity below 200 Ω·m at 5%
porosity cannot be explained by Archie at all**, whatever the saturation. Since
tight rocks are routinely below 200 Ω·m when they contain clay, the violation of
the bound is a diagnostic that the model — not the data — is at fault.

### 3.3 Why the clay term adds rather than modifies

Section 5 asserted that two conduction paths add. That is not an approximation; it
is the parallel-resistor law applied to a volume.

Let the rock contain a pore-water path of conductance $G_w$ and a solid/clay path
of conductance $G_c$ between the same two electrode surfaces. Both are driven by
the same potential difference, so the total current is the sum and

$$G_\text{total} = G_w + G_c
\qquad\Longrightarrow\qquad
\sigma_\text{total} = \sigma_w^\text{eff} + \sigma_c^\text{eff}
= \frac{\phi^mS_w^n}{aR_w} + \sigma_\text{clay}(S_w) .$$

Dimensional check: every term is S m⁻¹ ✓ (since $\phi^mS_w^n/(aR_w)$ has units of
conductance per unit length once the geometric factor is absorbed).

**Physical interpretation, and why the form of the clay term is model-specific.**
The *addition* is exact; the *form of $\sigma_\text{clay}$* is not. Waxman–Smits
writes it as proportional to the cation exchange capacity per unit pore volume and
to the water conductivity; other models use a clay-bound-water volume with its own
conductivity. All of them reduce to "a second path that Archie omits", and all of
them therefore predict the same qualitative failure: **Archie overestimates $S_w$
in clay-bearing rock, always, because it attributes the clay's current to the
water.** The size of the bias depends on the model only through
$\sigma_\text{clay}$, which must be calibrated.

## 4. Assumptions and their violations

| Assumption | Violated by |
|---|---|
| Conduction only through pore water | clay, sulphides, graphite, metallic minerals |
| No surface conduction | clay-bearing sands and shales (largest effect) |
| Water is the only fluid conducting | oil/gas are insulators (consistent) |
| Uniform, non-patchy saturation | patchy saturation; also affects the exponent $n$ |
| Porosity is intergranular and connected | vuggy, fractured, or isolated porosity |
| $m$, $a$, $n$ known for this rock | almost always the weakest link |
| Isotropic | anisotropic shale fabrics |

This is a long list, and it is honest: Archie's law works extremely well in
clean, high-porosity sandstones and poorly elsewhere.

### 4.1 Assumptions, and the size of each failure

| Assumption | Failure | Quantified consequence |
|---|---|---|
| Conduction only through pore water | clay, sulphides, graphite | $S_w$ biased high; 87% relative at $\phi = 0.10$ in Section 6 |
| No surface conduction | clay-bearing sands | the largest single error source in shaly formations |
| Uniform, non-patchy saturation | patchy saturation | also changes the exponent $n$ |
| Intergranular, connected porosity | vugs, fractures | $m$ is geometry-specific; a fracture porosity of 0.1% can dominate conduction |
| $a$, $m$, $n$ known | almost always assumed | $\Delta m = 0.1$ → 9.5% error in $S_w$; the dominant term |
| Isotropic | anisotropic shale fabric | resistivity anisotropy of 2–10 in shales is common; a single $R_t$ is then ill-defined |
| $R_w$ known | salinity, temperature | 10% error → 5% in $S_w$; salinity must be measured, not guessed |

## 5. Parallel conduction and the shaly-sand model

With two conduction paths, total conductivity is the sum:

$$\sigma_t = \sigma_\text{Archie} + \sigma_\text{clay}
= \frac{\phi^mS_w^n}{aR_w} + \text{(clay term)}.$$

The clay term is often written as proportional to $S_w$ or to the cation
exchange capacity per unit pore volume (Waxman–Smits). The exact form differs
between models; the *structure* — an additive term that Archie ignores — is the
essential point.

## 6. Worked example (measured): Archie inverted on clay-contaminated data

Stated SYNTHETIC inputs: $a = 1$, $m = 2$, $n = 2$, $R_w = 0.5$ Ω·m, and an
added clay conduction of $0.02$ S/m in parallel. True saturation
$S_w = 0.40$ in every case.

| $\phi$ | $S_w$ true | $S_w$ from Archie | error |
|---|---|---|---|
| 0.05 | 0.40 | **1.3266** | $+0.9266$ |
| 0.10 | 0.40 | 0.7483 | $+0.3483$ |
| 0.20 | 0.40 | 0.5099 | $+0.1099$ |
| 0.30 | 0.40 | 0.4522 | $+0.0522$ |

Two things to notice. First, the bias is **always positive**: the extra
conductivity is read as extra water. Second, at $\phi = 0.05$ the inversion
returns $S_w = 1.33$ — **greater than one**, which is physically impossible.
A bound being violated is the clearest possible signal that the model is
outside its assumptions, and it should be reported as such rather than clipped
to 1.0 silently.

The bias is worst at low porosity because the Archie term
$\propto\phi^m$ is then smallest relative to the fixed clay term.

### 6.1 Extended worked example: a two-term model versus Archie, done in full

Take the stated synthetic rock of Section 6, at $\phi = 0.10$,
$S_w = 0.4$, $a = 1$, $m = 2$, $n = 2$, $R_w = 0.5$ Ω·m, and a clay conduction
path contributing $S_w\cdot 0.02$ S/m.

**Pore-water conduction.** $\sigma_\text{Archie} = \phi^mS_w^n/(aR_w)
= 0.01\cdot0.16/0.5 = 3.2\times10^{-3}$ S/m, so the Archie-only bulk
resistivity is $R_t = 1/\sigma = 312.5$ Ω·m.

**Clay conduction.** $\sigma_\text{clay} = S_w\cdot0.02 = 8.0\times10^{-3}$ S/m.

**Total.** Conductivities in parallel add:
$\sigma_t = 3.2\times10^{-3}+8.0\times10^{-3} = 1.12\times10^{-2}$ S/m, so

$$R_t = 1/1.12\times10^{-2} = 89.3\ \Omega\cdot\mathrm{m}.$$

**What Archie makes of it.** Inverting the Archie model on
$R_t = 89.3$ Ω·m:

$$S_w^\text{Archie} = \left(\frac{aR_w}{\phi^mR_t}\right)^{1/n}
= \left(\frac{0.5}{0.01\cdot89.3}\right)^{1/2} = (0.5600)^{1/2} = 0.7483.$$

The true saturation is 0.40 and Archie returns 0.7483 — an overestimate of 87%
relative. (This value, 0.7483, is exactly what the demonstration prints at
$\phi = 0.10$, which is the cross-check that the hand calculation and the code
agree.)

**Why the clay term dominates here.** At $\phi = 0.10$ the pore-water
conductivity is $3.2\times10^{-3}$ S/m while the clay term is
$8.0\times10^{-3}$ S/m: the clay path carries **71%** of the current. Archie
attributes all of it to water and therefore demands more water than exists.

**The sensitivity that matters.** Doubling the assumed clay conductivity to
0.04 S/m gives $\sigma_t = 0.0032+0.016 = 0.0192$ S/m, $R_t = 52.1$ Ω·m, and
$S_w^\text{Archie} = (0.5/0.5208)^{1/2} = 0.9798$ — approaching the impossible
$S_w = 1$. So the *conclusion* "Archie fails badly at low porosity in clay-
bearing rock" is robust, while the *corrected saturation* is strongly dependent
on the clay conductivity, which is why shaly-sand models must calibrate that
term rather than assume it.

**The general lesson.** A model that has the wrong *structure* fails in a
way that is diagnosable (here, $S_w>1$ at the lowest porosity in the
demonstration's table) and not fixable by tuning its parameters. That is the
signature of an assumption being violated rather than a fit being imperfect.

### 6.2 Worked arithmetic: the porosity at which Archie becomes impossible

The threshold of Section 3.2, $R_t \ge aR_w/\phi^m$, converts a measured
resistivity into a *porosity* limit. Invert it:

$$\phi_{\min} = \left(\frac{aR_w}{R_t}\right)^{1/m} .$$

For $a = 1$, $R_w = 0.5$ Ω·m, $m = 2$:

| measured $R_t$ (Ω·m) | $\phi_{\min}$ for an admissible $S_w$ |
|---|---|
| 50 | 0.100 |
| 100 | 0.071 |
| 200 | 0.050 |
| 500 | 0.032 |

**Read the table as a screening tool.** If a resistivity log records
$R_t = 100$ Ω·m and an independent porosity measurement gives $\phi = 0.05$,
then Archie *cannot* be satisfied for any saturation — the rock is too resistive
for its porosity. The budget of the lesson's Section 3.2 says the likely causes
are (i) a wrong $m$ (too large), (ii) a wrong $R_w$, or (iii) a hydrocarbon
saturation combined with an over-large $\phi$ estimate. **The impossibility itself
is the most useful output of the calculation**, because it forces the assumptions
to be examined instead of the answer to be reported.

**Sensitivity of the threshold.** Since $\phi_{\min}\propto R_w^{1/m}$ and
$\propto R_t^{-1/m}$, the threshold is forgiving: doubling $R_w$ raises
$\phi_{\min}$ by only $\sqrt{2} = 41\%$ at $m = 2$. It is the *exponent* that
dominates, exactly as in Section 3.2 — a change in $m$ from 2.0 to 2.2 changes
$\phi_{\min}$ by $(100/50)^{0.1} = 7\%$ at 100 Ω·m, small, but changes the
*inverted saturation* by 9.5% (Section 3.2). **The exponent's influence is much
larger on $S_w$ than on the admissibility bound.**

### 6.3 A shortcut that fails: clipping $S_w$ to 1

**The shortcut.** The inversion returns $S_w = 1.33$; cap it at 1.0 and report a
fully water-saturated rock.

**Why it fails.** $S_w > 1$ is not a slightly-too-large saturation; it is a
formal proof that no saturation can explain the data under the model. Clipping
converts a *model failure* into an apparently *successful* interpretation, and in
doing so discards the only piece of information the calculation had to offer.
The demonstration's own table makes the point: at $\phi = 0.05$ the inversion
returns $1.3266$, and at $\phi = 0.30$ it returns $0.4522$ on the same rock with
the same true saturation of 0.40 — so the failure is confined to the low-porosity
end, which is precisely where the clay term dominates the pore-water term
(71% of the current in Section 6's worked example).

**What to do instead.** Report the violation, the porosity at which it begins, and
the model change that removes it: an explicit clay-conduction term, or a
lower $m$. Then report the corrected saturation *with* the clay term's uncertainty
— because the correction, unlike the failure, is strongly model-dependent.

**The generalisable lesson.** A bound violation is the clearest possible signal
that a model is outside its assumptions. Bounds are cheap to check, unambiguous
when violated, and they carry more information than the fitted number does. Every
physical inversion should be tested against the bounds of its own model before
the result is reported.

## 7. Practical guidance

1. **Measure $m$, $a$, $n$** on cores from the interval where possible; report
   them with the saturation.
2. **Check for clay** independently (gamma log, cation exchange capacity,
   mineralogy) before trusting an Archie saturation.
3. **Watch for $S_w > 1$** — it means the model, not the data, is wrong.
4. **Report a range**: the uncertainty in $m$ alone can dominate the
   uncertainty in $S_w$.
5. **Remember what is measured**: $R_t$ is a bulk property, an average over a
   volume far larger than a pore, and it depends on the fluid, the geometry and
   any conducting minerals.

### 7.1 Which constraint binds, and where

The two error sources of Section 3.2 and the clay bias of Section 3.3 dominate in
different regimes, and knowing which one binds is what determines where a
resistivity interpretation may be trusted.

| regime | binding constraint | evidence from this lesson |
|---|---|---|
| high porosity, clean rock | the exponents $m$, $n$ | $\Delta m = 0.1$ gives 9.5% in $S_w$; the clay term is a small share of the total |
| high porosity, shaly rock | the clay term | the clay path carries a rising share as $\phi$ falls; at 71% of the current in Section 6's worked example |
| low porosity, any rock | the clay term, and often admissibility itself | $S_w = 1.3266 > 1$ at $\phi = 0.05$ in the demonstration |
| low porosity, clean rock | the exponents, via $\lvert\ln\phi\rvert$ | the sensitivity $-\ln\phi/n$ grows as $\phi$ falls |

**Read the table as a map of where Archie may be used.** The two safe regimes are
*a* high-porosity clean rock (where the exponents dominate, and they are usually
measurable on cores) and *no* regime where the clay term is large — because that
term is the one least often measured. **The clay path, not the exponents, is the
practical limit on resistivity-derived saturation in shaly formations**, and it
appears exactly where the pore-water term is weakest.

**The one-line summary.** Archie's law is not wrong; it is *narrow*. The
combination of the admissibility bound ($R_t \ge aR_w/\phi^m$) and the sensitivity
table tells you in advance which intervals of a log it can be applied to, and
which need a shaly-sand model with a calibrated clay term. Applying it outside
those intervals is the error this lesson exists to prevent.

## 8. Python demonstration

`code/petrophysics_demo.py` Section 4. It computes the table above, including
the impossible saturation, and prints the diagnostic conclusion. Change the
clay conduction term to zero and confirm that Archie becomes exact — a check
that the forward model and the inversion are self-consistent.

## 9. Exercises, mistakes, applications

Exercises: [`exercises/07-electrical-properties-exercises.md`](./exercises/07-electrical-properties-rock-exercises.md).

**Common mistakes.** (1) Using a handbook $m$ for a different lithology.
(2) Silently clipping $S_w > 1$. (3) Treating an apparent resistivity from a
surface survey as a formation resistivity. (4) Ignoring temperature and salinity
dependence of $R_w$. (5) Reporting saturation without the exponents used.

**Applications.** Formation evaluation from resistivity logs; groundwater
salinity estimation; contaminant mapping (the contrast is in the pore fluid);
mineral exploration for sulphides (where Archie's assumptions fail in the
opposite direction — the conduction is through the *solid*); geothermal
reservoir characterisation.

## 10. Further reading

- **Archie, G. E. (1942).** The electrical resistivity log as an aid in
  determining some reservoir characteristics. *Trans. AIME* 146, 54–62.
- **Waxman, M. H. & Smits, L. J. M. (1968).** Electrical conductivities in
  oil-bearing shaly sands. *SPE Journal* 8, 107–122. Level: graduate. The
  canonical shaly-sand model.
- **Schön, J. H. *Physical Properties of Rocks* (2nd ed.).** Chapter 8. Level:
  graduate. Ranges of $m$ and $n$ with provenance.
- **09-01-02 Archie's Law** in the electrical methods module:
  [09-01-02 Archie's Law](../../09-electrical-em-methods/01-electrical-properties-of-earth/02-archies-law.md).

## 11. Related lessons

- [05-04-04 Velocity-Porosity-Clay Models](./04-velocity-porosity-clay.md)
- [09-01-01 Resistivity and Conductivity](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md)
- [09-01-04 Clay and Surface Conduction](../../09-electrical-em-methods/01-electrical-properties-of-earth/04-clay-and-surface-conduction.md)

## Self-assessment checklist

- [ ] I can derive Archie's scaling form and explain what $a$ and $m$ absorb.
- [ ] I can list six assumptions and a rock type that violates each.
- [ ] I can demonstrate and quantify the clay-induced bias.
- [ ] I can explain why $S_w > 1$ indicates a model failure.
- [ ] I can state what a resistivity measurement actually averages over.
