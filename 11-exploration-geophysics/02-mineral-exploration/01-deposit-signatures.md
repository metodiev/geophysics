---
id: 11-02-01
title: "Geophysical Signatures of Major Deposit Types"
level: advanced
prereqs: ["04-06-02", "05-01-01", "11-01-02"]
tags: [exploration-geophysics, mineral-exploration, deposit-signatures, detectability, ambiguity]
---

# Geophysical Signatures of Major Deposit Types

Mineral exploration geophysics does not measure metals. It measures a **signature**:
the pattern of anomaly amplitudes that a deposit class produces across several
methods because of its density, susceptibility, conductivity, chargeability and
radioelement contrasts. This lesson builds that object formally, computes it for
seven deposit classes in one common geometry, and then establishes the result that
governs the rest of the module — **a strong anomaly proves that something
anomalous is there, and the *direction* of the signature, not its magnitude, is
what identifies which class of thing it is.**

**All models and data in this module are SYNTHETIC.** The property contrasts of
the deposit classes below are chosen teaching values that span the ranges usually
quoted for such classes. They are not measurements, not database averages, and not
the properties of any named deposit, belt or district. The geometry, noise levels
and thresholds are synthetic too.

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** a signature vector and **construct** one from a property-contrast
   table using derived anomaly formulas.
2. **Compute** the gravity, magnetic and EM anomaly of one common body for every
   deposit class, and **explain** the two-to-four orders of magnitude of spread.
3. **Normalise** and **analyse** the signature matrix: singular values, rank and
   condition number, and **state** what the smallest singular direction means.
4. **Compute** pairwise cosine similarities and distances, and **identify** which
   deposit classes are confusable.
5. **Derive** the error probability of a two-class decision for the case where the
   body's size and depth are known, and for the reconnaissance case where they are
   not, and **explain** why the second is far worse.
6. **Explain** why a barren graphite schist is the same EM target as a massive
   sulphide body, and **state** which additional property resolves it.
7. **State** the assumptions under which signature-based class identification is
   legitimate, and the circumstances in which it must fail.

## Prerequisites

- [04-06-02 Mineral Deposit Types and Their Geophysical Signatures](../../04-earth-science-geology/06-petroleum-and-mineral-systems/02-mineral-deposits.md)
  — what the classes are, geologically.
- [05-01-01 The Central Idea: Property Contrasts Produce Signals](../../05-core-geophysics/01-what-geophysics-measures/01-physical-property-contrast.md)
  — the contrast logic formalised here.
- [11-01-02 Targeting Strategy and Method Selection](../01-exploration-workflow/02-targeting-and-strategy.md)
  — the single-method anomaly formulas and the detection-probability machinery.

## 1. From geology to a measurable object

A deposit's *geology* is not observable from the air. What is observable is a
small number of physical-property **contrasts** against the host, and every one of
them is an accident of mineralogy:

| Property | What supplies the contrast |
|---|---|
| Density | oxide and sulphide minerals (magnetite, chromite, hematite, pyrrhotite) are $1$–$2\ \mathrm{g\,cm^{-3}}$ denser than silicates |
| Susceptibility | magnetite (dominant), pyrrhotite; hematite and most sulphides are weak |
| Conductivity | connected sulphide or graphite; *not* the total sulphide content |
| Chargeability (IP) | polarisable grain surfaces; connected *or* disseminated sulphide, and clays |
| K, U, Th | alteration mineralogy (potassic, sericitic, argillic) and the radioelements in the host |

Two structural facts follow immediately and both are quantified below. First,
**several different minerals supply the same property** (magnetite and pyrrhotite
both magnetise; sulphide and graphite both conduct), so a property contrast
identifies a *mineral* family, not a metal. Second, **the same property appears in
the barren and the ore-bearing case** (a graphite schist is as conductive as a
massive sulphide body), which is the source of the false positives that dominate
the economics of minerals exploration.

## 2. The synthetic contrast table and the anomaly formulas

The demonstration uses seven deposit classes and one host with the chosen contrasts

| deposit class | $\Delta\rho$ (kg m⁻³) | $\kappa$ (SI) | $\rho$ (Ω m) | M (mV/V) | K (%) | eU (ppm) | eTh (ppm) |
|---|---|---|---|---|---|---|---|
| porphyry Cu (disseminated) | 100 | 0.010 | 20 | 15.0 | 3.0 | 3.0 | 12.0 |
| IOCG (magnetite-bearing) | 400 | 0.350 | 5 | 8.0 | 1.5 | 2.0 | 6.0 |
| VMS (massive sulphide) | 600 | 0.050 | 0.5 | 12.0 | 0.5 | 1.0 | 1.0 |
| magmatic Ni–Cu sulphide | 450 | 0.100 | 1.0 | 10.0 | 0.3 | 0.5 | 1.0 |
| chromite | 800 | 0.005 | 2000 | 1.0 | 0.1 | 0.2 | 0.5 |
| banded iron formation | 900 | 0.500 | 500 | 2.0 | 0.3 | 1.0 | 2.0 |
| graphite schist (barren) | −50 | 0.001 | 0.2 | 3.0 | 1.0 | 2.0 | 8.0 |
| **host (granodiorite)** | 0 | 0.005 | 100 | 1.0 | 2.0 | 2.0 | 10.0 |

and the same body geometry for every class (a sphere of radius
$R = 150\ \mathrm{m}$ centred at $z = 300\ \mathrm{m}$, ambient field
$50\ \mathrm{\mu T}$, EM at $100\ \mathrm{Hz}$). The anomaly formulas are those
derived in [11-01-02](../01-exploration-workflow/02-targeting-and-strategy.md):

$$\Delta g = \frac{4}{3}\pi G\,\Delta\rho\,\frac{R^{3}}{z^{2}}, \qquad
\Delta B = \frac{\kappa B_0 V}{2\pi z^{3}}, \qquad
\text{EM index} = \left(\frac{R}{z}\right)^{3}
e^{-2z/\delta}\frac{\omega\tau}{\sqrt{1+(\omega\tau)^{2}}},$$

with $\tau = \mu_0\sigma R^{2}/\pi^{2}$ and $\delta = \sqrt{2/\omega\mu_0\sigma_{\text{host}}}$.
For the radioelements the observable is a **relative** contrast, because the
surface flux is a concentration ratio and the host's absolute level is a
laboratory nuisance parameter:

$$\Delta\text{K} = \frac{[\text{K}]_{\text{class}} - [\text{K}]_{\text{host}}}
{[\text{K}]_{\text{host}}}\times 100\% ,$$

and similarly for U and Th. The measured result, printed by the demonstration:

| deposit class | $\Delta g$ (mGal) | $\Delta B$ (nT) | EM index | $\Delta$K (%) | $\Delta$U (%) | $\Delta$Th (%) |
|---|---|---|---|---|---|---|
| porphyry Cu | 0.105 | 41.67 | 0.00340 | +50.0 | +50.0 | +20.0 |
| IOCG | 0.419 | 1458.33 | 0.01285 | −25.0 | 0.0 | −40.0 |
| VMS | 0.629 | 208.33 | 0.03656 | −75.0 | −50.0 | −90.0 |
| magmatic Ni–Cu | 0.472 | 416.67 | 0.03317 | −85.0 | −75.0 | −90.0 |
| chromite | 0.839 | 20.83 | 0.00003 | −95.0 | −90.0 | −95.0 |
| banded iron formation | 0.944 | 2083.33 | 0.00014 | −85.0 | −50.0 | −80.0 |
| graphite schist | −0.052 | 4.17 | 0.03771 | −50.0 | 0.0 | −20.0 |

Four features of this table are worth stating explicitly, because they are the
physics of the whole module:

1. **Gravity spans one order of magnitude** ($0.05$–$0.94$ mGal) at fixed
   geometry; the density contrasts are all within a factor of twenty.
2. **Magnetics spans two-to-three orders** ($4$–$2083$ nT) and is the only method
   that separates magnetite-bearing from non-magnetic classes.
3. **The EM index spans four orders** ($3\times10^{-5}$ to $3.8\times10^{-2}$),
   because $(R/z)^{3}$ is common to all but $\delta$ and $\tau$ are not: the
   highly resistive, weakly polarisable classes (chromite, BIF) are invisible.
4. **The radiometric contrasts are sign-varying and modest** (±20% to ±95%), and
   they exist *only where the body outcrops*, a caveat made quantitative in §6.

## 3. The signature matrix: how many independent things are we measuring?

Stack the six numbers for each of the seven classes into a $7\times6$ matrix, and
normalise each **row** to unit length. The normalisation is the reconnaissance
assumption: at this stage the body's size and depth are unknown, so the
*amplitude* of the signature is not available as a discriminator and the direction
is.

The singular values of the normalised matrix are

$$2.0396,\quad 1.5770,\quad 0.5485,\quad 0.2285,\quad 0.0011,\quad
1.59\times10^{-5},$$

so the condition number is $\sigma_1/\sigma_6 = 1.29\times10^{5}$. All six
directions are formally non-zero, but the smallest carries almost nothing: its
weight is $99.8\%$ on the EM channel. Read that carefully — after normalisation,
**the EM measurement contributes almost no class-discriminating pattern.** The EM
information is almost entirely magnitude, which the normalisation removed. That is
exactly why an EM anomaly alone can say "there is a conductor" but rarely "which
kind of conductor".

The largest singular direction is $91.8\%$ magnetics with the rest shared among
the radioelements, i.e. the dominant axis of variation among these classes is how
magnetic they are.

## 4. Which classes are confusable: cosine similarity

The cosine between two unit signature vectors is a scale-free measure of how
similar their *patterns* are. The most similar pairs among the seven classes are

| pair | cosine | distance |
|---|---|---|
| IOCG / banded iron formation | 0.9994 | 0.0354 |
| VMS / magmatic Ni–Cu sulphide | 0.9751 | 0.2230 |
| magmatic Ni–Cu / banded iron formation | 0.9626 | 0.2734 |
| IOCG / magmatic Ni–Cu sulphide | 0.9530 | 0.3065 |

and the least similar, for contrast, include VMS against graphite schist
($\cos = 0.487$) and chromite against porphyry Cu ($\cos = -0.747$). The distance
matrix satisfies $D = \sqrt{2-2\cos}$, which the demonstration verifies, along
with symmetry and the triangle inequality.

An IOCG and a banded iron formation have virtually the same signature direction:
both are dense *and* strongly magnetic, and they differ only in the absolute
magnitudes. When magnitudes are unavailable, **no signal-to-noise ratio resolves
them**, because the angular separation is $0.06\%$ of a right angle.

## 5. The decision problem: known versus unknown amplitude

Make the classification problem explicit. Two candidate classes have signature
vectors $\mathbf{s}_i$ and $\mathbf{s}_j$, and the measurement is
$\mathbf{x} = A\mathbf{s}_i + \mathbf{n}$ where $\mathbf{n}$ is Gaussian noise with
per-method standard deviations $\sigma_k$ and $A$ is an unknown common amplitude.

**Case 1: $A$ known.** Decide by the sign of
$\langle\mathbf{x}, \mathbf{s}_i - \mathbf{s}_j\rangle$ with a boundary at the
midpoint, so

$$P_{\text{err}} = \Phi\!\left(
-\frac{\|\mathbf{s}_i-\mathbf{s}_j\|}{2\sqrt{\sum_k \sigma_k^{2}
d_k^{2}}}\right), \qquad
\mathbf{d} = \frac{\mathbf{s}_i-\mathbf{s}_j}{\|\mathbf{s}_i-\mathbf{s}_j\|} .$$

**Case 2: $A$ unknown.** Only directions are comparable, so the test becomes
"which reference direction is closer in angle", which is again a linear test on
$\mathbf{u}_i - \mathbf{u}_j$ with $\mathbf{u} = \mathbf{s}/\|\mathbf{s}\|$, but now

$$P_{\text{err}} = \Phi\!\left(
-\frac{A\,\langle\mathbf{s}_i, \mathbf{u}_i-\mathbf{u}_j\rangle}
{\sqrt{\sum_k \sigma_k^{2}\,(u_{i,k}-u_{j,k})^{2}}}\right).$$

The numerator contains $A(1-\cos)\|\mathbf{s}_i\|$: the *angular* gap times the
signal magnitude. The demonstration evaluates both, with
$\sigma = (0.02\ \mathrm{mGal},\, 0.2\ \mathrm{nT},\, 0.02,\, 5\%,\, 5\%,\, 5\%)$:

| pair | cosine | $P_{\text{err}}$, $A$ known | $P_{\text{err}}$, $A=1$ | $P_{\text{err}}$, $A=0.1$ |
|---|---|---|---|---|
| IOCG / BIF | 0.9994 | 0.0000 | 0.0000 | 0.3027 |
| VMS / Ni–Cu | 0.9751 | 0.0000 | 0.0000 | 0.2752 |
| VMS / graphite | 0.4866 | 0.0000 | 0.0000 | 0.0001 |

Three honest readings:

- With the amplitude known, even the closest pair is separated, because the
  *absolute* anomaly values differ by more than the noise. Class identification
  with a fixed target model is easy; that is not the reconnaissance problem.
- With the amplitude unknown and a reference-strength anomaly ($A = 1$), the
  classes are still separated here — but by the radioelement directions, which is
  a statement about **outcrop**, not about depth penetration. Restricting the
  test to the radiometric channels alone gives $P_{\text{err}} = 0.0131$ for
  IOCG/BIF and $0.0268$ for VMS/Ni–Cu: a few per cent, from three surface
  concentration ratios.
- Weaken the signature tenfold ($A = 0.1$, a smaller or deeper body) and the two
  closest pairs become coin flips ($0.30$ and $0.28$ error). That is the
  reconnaissance regime, and it is why regional programs rely on *geological*
  context and on mapping patterns rather than on identifying individual bodies.

## 6. Why a graphite schist is a massive sulphide body

In the synthetic table, VMS and graphite schist have EM indices $0.03656$ and
$0.03771$ — within 3% of each other — with magnetic anomalies of $208\ \mathrm{nT}$
and $4\ \mathrm{nT}$ and gravity anomalies of $+0.63$ and $-0.05\ \mathrm{mGal}$.
Restricting the decision to the EM channel alone, the two classes are confused with
probability **0.4885**, i.e. a coin flip, exactly as expected when the only
discriminating channel has been discarded.

| method set | $P_{\text{err}}$ (VMS vs graphite) |
|---|---|
| EM only | 0.4885 |
| gravity only | 0.0000 |
| magnetics only | 0.0000 |
| all methods | 0.0000 |

**The resolution does not come from better EM.** It comes from an independent
property: here, the density and magnetic contrasts (a sulphide body is denser and
more magnetic than a graphite schist in this table), and in practice from the IP
response, which separates a polarisable sulphide from a *conductive but far less
polarisable* graphite schist — treated in
[11-02-06 IP for Disseminated Sulphides](06-ip-for-minerals.md). Every multi-method
program is an attempt to buy such an independent property at the lowest cost.

## 7. Worked example — classifying one anomaly

A survey over a SYNTHETIC prospect returns, after corrections:

| channel | value | 1-σ noise |
|---|---|---|
| gravity | $+0.61\ \mathrm{mGal}$ | 0.02 mGal |
| magnetics | $+195\ \mathrm{nT}$ | 0.2 nT |
| EM index | 0.034 | 0.02 |

**Step 1 — candidate classes by magnitude.** The three channels agree to within
$10\%$ with the VMS row ($0.629$, $208.3$, $0.03656$) and are also within the
uncertainty of the Ni–Cu row ($0.472$, $416.7$, $0.03317$) for gravity and EM but
not for magnetics (195 against 417, a 500-σ discrepancy).

**Step 2 — formal decision.** Use the known-amplitude test on the two candidates,
with $\mathbf{s}_{\text{VMS}} = (0.629, 208.33, 0.03656)$ and
$\mathbf{s}_{\text{Ni}} = (0.472, 416.67, 0.03317)$:

$$\mathbf{s}_{\text{VMS}} - \mathbf{s}_{\text{Ni}} = (0.157,\,-208.34,\,0.0034),$$

$$\|\cdot\| = 208.34, \qquad
\mathbf{d} = (7.54\times10^{-4},\,-0.99999,\,1.6\times10^{-5}),$$

$$\sqrt{\sum_k\sigma_k^{2}d_k^{2}}
= \sqrt{(0.02)^2(7.54\times10^{-4})^2 + (0.2)^2(0.99999)^2 +
(0.02)^2(1.6\times10^{-5})^2} = 0.2000,$$

$$P_{\text{err}} = \Phi\!\left(-\frac{208.34}{2(0.2000)}\right)
= \Phi(-520.9) \approx 0 .$$

The magnetics decides it, and the decision is not marginal: $195\ \mathrm{nT}$
sits $520$ standard deviations from the Ni–Cu prediction. **A single well-calibrated
channel can settle a known-amplitude class question** — but note what was assumed:
the amplitude was taken as known, i.e. the target model (size and depth) was fixed
in advance. If the body were also allowed to be twice as deep, the amplitude would
fall by $2^{3} = 8$ in magnetics, and the test would have to be redone on
directions, where the answer is much weaker.

**Step 3 — the honest statement.** "The anomaly is consistent with a massive
sulphide body of the modelled size and depth; it is not consistent with a
magmatic Ni–Cu body at that geometry; a graphite schist is excluded only on the
basis of the density and magnetic contrasts, and that exclusion depends entirely
on the host rock being granodioritic."

## 8. Assumptions and regime of validity

1. **The contrast table is the model, and it is a chosen table.** Real contrasts
   overlap between classes and vary within a class; the table's clean separation of
   magnetic from non-magnetic, and conductive from resistive, is an idealisation.
   **The demonstration's answer changes if the table changes**, and the table is
   not evidence.
2. **One common geometry.** Every class is evaluated as the same sphere at the
   same depth. Real bodies differ in shape, depth and orientation, and the
   amplitudes therefore differ for reasons that have nothing to do with class.
3. **No remanent magnetisation.** Remanence can dominate induced magnetisation and
   reverse the sign of an anomaly; §2's formula includes only induction
   (§[11-02-02](02-magnetics-for-minerals.md)).
4. **No self-demagnetisation.** The linear $\Delta B \propto \kappa$ relation
   over-predicts for $\kappa \gtrsim 0.1$; the IOCG and BIF rows
   ($\kappa = 0.35, 0.50$) are the most affected.
5. **Host properties are uniform.** A single host resistivity and radioelement
   background is assumed; in reality a heterogeneous host is the largest
   contributor to false anomalies.
6. **The radioelement contrast requires outcrop or residual soil.** Per §5, this
   is the channel that separates the closest pairs, and it is the first to
   disappear under cover.
7. **Noise is Gaussian, independent and stationary.** Real noise is correlated
   along lines and between channels (a single bad flight line moves all channels
   together), which *reduces* the effective number of independent measurements.
8. **The decision is two-class and the options are known.** There may be a third
   class nobody has considered; the demonstration cannot report it, and that is
   the largest single risk in anomaly-based classification.

## 9. Units and dimensional checks

| Quantity | Unit | Check |
|---|---|---|
| $\Delta g$ | mGal ($10^{-5}\ \mathrm{m\,s^{-2}}$) | $\propto G\Delta\rho R^{3}/z^{2}$ ✔ |
| $\Delta B$ | nT ($10^{-9}$ T) | $\propto \kappa B_0 V/z^{3}$, $B$ and $\kappa B$ both T ✔ |
| EM index | – | ratio of two fields ✔ |
| radioelement contrast | % | a relative difference ✔ |
| cosine, distance | – | operations on normalised vectors ✔ |

Because the signature mixes units, the normalisation in §3 is not cosmetic: it is
what makes the cosine a well-posed object. A consequence, stated as a pitfall, is
that the normalisation makes the EM channel numerically negligible — a 3% EM
contrast and a 300% magnetic contrast are weighted by their components in a unit
vector, not by their significance to a geologist.

## 10. Exercises

Full sets with worked solutions:
[`exercises/01-deposit-signatures-exercises.md`](exercises/01-deposit-signatures-exercises.md)
and
[`exercises/01-deposit-signatures-solutions.md`](exercises/01-deposit-signatures-solutions.md).

## Mastery checkpoint

Without notes:

> A synthetic class has $\Delta\rho = 500\ \mathrm{kg\,m^{-3}}$,
> $\kappa = 0.08$ SI, $\rho = 2\ \Omega\,\mathrm{m}$ in a host of
> $100\ \Omega\,\mathrm{m}$, with K, U, Th of $1.0$, $1.0$, $3.0$ against a host of
> $2.0$, $2.0$, $10.0$. The body is a sphere of radius $150\ \mathrm{m}$ at
> $z = 300\ \mathrm{m}$; the field is $50\ \mathrm{\mu T}$ and the EM frequency
> $100\ \mathrm{Hz}$ — the same geometry as the table. **(a)** Compute the gravity
> anomaly in mGal and the magnetic anomaly in nT. **(b)** Compute the EM index.
> **(c)** Compute the three radioelement contrasts in per cent. **(d)** Which of
> the seven classes in the table does this signature most resemble, and what is
> the cosine between your computed signature and that class's row? **(e)** State
> the one measurement you would add to identify the class, and why.

A worked version is in the
[solutions](exercises/01-deposit-signatures-solutions.md).

## Common pitfalls

1. **Treating a signature as an identification.** A signature narrows the class;
   it does not name a deposit, and it never establishes grade.
2. **Believing that more data of the same kind will separate two classes with
   cosine $\approx 1$.** Direction is what carries class, and a direction gap does
   not widen with better data.
3. **Forgetting that the amplitude is normally unknown.** Known-amplitude
   classification is easy and irrelevant at the reconnaissance stage.
4. **Using EM alone to certify a sulphide.** The graphite false positive is a coin
   flip on EM alone.
5. **Ignoring cover.** The channel that separates the closest pairs is the surface
   radiometric one; under cover it is gone.
6. **Over-reading $\kappa$ from a linear formula.** Self-demagnetisation flattens
   the relation at high susceptibility.
7. **Assuming the class list is complete.** An unexplored class is an unmodelled
   alternative that no test can reject.

## Related modules

- [11-01-02 Targeting Strategy and Method Selection](../01-exploration-workflow/02-targeting-and-strategy.md)
  — where these anomaly formulas and detection probabilities come from.
- [11-02-02 Magnetics for IOCG, Porphyry and Magmatic Sulphides](02-magnetics-for-minerals.md)
  — remanence, reduction to pole and depth estimation.
- [11-02-04 EM for Conductors, Massive Sulphides and Graphite](04-em-for-minerals.md)
  — the conductivity ambiguity in detail.
- [11-02-07 Multi-Method Targeting and Prospectivity Analysis](07-multi-method-targeting.md)
  — how signatures are combined, and how combination fails.
