---
id: 09-03-04
title: "IP for Sulphides, Clays, Contaminants and Permafrost"
level: graduate
prereqs: ["09-01-02", "09-01-04", "09-03-02", "09-03-03"]
tags: [electrical-methods, induced-polarisation, sulphides, clay, contaminants, permafrost, non-uniqueness, monitoring]
---

# IP for Sulphides, Clays, Contaminants and Permafrost

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** the two conduction pathways that a polarisable rock presents — a
   non-polarisable electrolyte path and a polarisable surface or electronic path
   — and **derive** the resulting effective chargeability
   $m_{\text{eff}} = m_0 B/\left[A(1-m_0) + B\right]$.
2. **Compute** the effective chargeability and bulk conductivity of a synthetic
   ground from a pore-fluid conductivity, a formation factor and a surface
   conductance, and **state** the units of each input.
3. **Explain** why increasing the pore-fluid conductivity *lowers* the measured
   phase while raising the conductivity, and quantify both changes.
4. **Build** a confusion matrix for a set of synthetic end-members and
   **demonstrate** that a phase-only comparison confuses pairs that a joint
   conductivity-and-phase comparison separates.
5. **Demonstrate** that two structurally different mixtures produce models that
   are indistinguishable inside a band, and **state** what would separate them.
6. **Distinguish** the three scenarios of a clay-rich soil, a saline plume and
   frozen ground in the $(\rho, \varphi)$ plane, and **explain** why either
   measurement alone leaves an ambiguity.
7. **State** the limits of the pathway model: what it does not represent, and
   which conclusions may not be drawn from it.

## Prerequisites

- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md)
  — the formation factor and the porosity/saturation exponents.
- [09-01-04 Clay Effects, CEC and Membrane Polarisation](../01-electrical-properties-of-earth/04-clay-and-surface-conduction.md)
  — the surface conduction that this lesson's pathway $B$ represents.
- [09-03-02 IP Models: Cole-Cole, Debye, Constant-Phase Element](02-ip-models.md)
  — the parameters fitted to a measured spectrum.
- [09-03-03 IP Acquisition, Chargeability and Phase Units](03-ip-acquisition.md)
  — what the measurement noise permits one to resolve.

**All models and data in this module are SYNTHETIC.** The end-member parameters
are teaching values chosen to span a plausible range; they are *not* measurements
of any rock, ore body, soil, site or instrument, and no laboratory or field value
is quoted anywhere in this lesson. Every number comes from
[`code/ip_applications_demo.py`](./code/ip_applications_demo.py).

---

## 1. Intuition: the phase is not a target identifier

A common expectation is that IP identifies a target: sulphides are supposed to
give a large phase, clays a large phase at low frequency, contaminated ground
something else again. The expectation fails for a structural reason. What a
chargeability or a phase measures is *the fraction of the current that flows
through a polarisable pathway*, and that fraction depends on both the pathway and
the electrolyte. Change the pore fluid and you change the measured polarisation
of an unchanged mineral assemblage.

The organising idea of this lesson is therefore a **pathway split**. Model the
ground as two conducting paths in parallel:

- a **non-polarisable electrolyte path** of conductance $A$, which is the brine
  in the pores: it carries current by ion migration and it polarises only weakly;
- a **polarisable path** of conductance $B$, which is either a mineral with
  electronic conduction (a sulphide, graphite) or a surface charge layer on clay
  and on other high-surface-area grains.

The measured chargeability is the intrinsic polarisability of the second path,
multiplied by the fraction of current it carries. That single sentence explains
four field behaviours at once: why clays polarise strongly in fresh water and
weakly in brine; why a conductive contaminant plume reduces the phase of the
ground it invades; why a sulphide target is easier to see in a resistive host;
and why two very different grounds can produce the same phase.

## 2. Precise definitions

### 2.1 Synthetic end-members used for comparison

The demonstration defines six synthetic end-members by four numbers each,
$\left(\rho_0, m_0, c, \tau\right)$:

| name | $\rho_0$ ($\Omega\,\mathrm{m}$) | $m_0$ | $c$ | $\tau$ (s) |
|---|---|---|---|---|
| clean sand | 800.0 | 0.010 | 1.00 | 0.050 |
| clay-rich soil | 40.0 | 0.060 | 0.30 | 0.002 |
| disseminated sulphide | 120.0 | 0.200 | 0.55 | 0.300 |
| massive sulphide | 2.0 | 0.450 | 0.75 | 2.000 |
| graphitic schist | 15.0 | 0.350 | 0.60 | 5.000 |
| frozen ground | 3000.0 | 0.020 | 0.40 | 0.010 |

They are chosen to span the range, not to represent particular rocks. Their
measured peak phases are $5.025$, $7.427$, $51.371$, $197.611$, $109.216$ and
$3.282$ mrad respectively, at peak frequencies of $3.199$, $88.227$, $0.650$,
$0.119$, $0.046$ and $16.323$ Hz.

Two features of this table matter immediately. First, the peak phase spans a
factor $60$; second, the peak *frequency* spans nearly four decades. The
frozen-ground and clean-sand end-members have almost identical (small) phases but
peak at $16.3$ Hz and $3.2$ Hz — a difference that a survey band limited to
$0.1$–$1$ Hz cannot see at all.

### 2.2 The pathway split

For the bulk conductivity,

$$\sigma_{\text{bulk}} = A + B, \qquad
A = \frac{\sigma_w}{F}, \qquad F = \phi^{-\mathrm{CEM}},$$

with $\sigma_w$ the pore-fluid conductivity [S/m], $F$ the formation factor
(dimensionless), $\phi$ the porosity (dimensionless) and $\mathrm{CEM}$ the
Archie cementation exponent (dimensionless). The surface conductance $B$ [S/m]
carries the polarisability: it is the pathway that accumulates charge. Its
intrinsic chargeability is $m_0$, so the response is that of a Cole-Cole element
with

$$\boxed{\;m_{\text{eff}} = \frac{m_0 B}{A(1-m_0) + B}\;}.$$

### 2.3 What is assumed in every number below

The synthetic demonstration uses $\phi = 0.35$, $\mathrm{CEM} = 1.80$ (giving
$F = \phi^{-\mathrm{CEM}} = 6.617$), an intrinsic pathway chargeability
$m_0 = 0.30$ and a surface conductance $B = 0.0020$ S/m unless stated
otherwise. The scenario phases are computed for a Cole-Cole model with
$c = 0.50$ and $\tau = 0.3$ s and the $m_{\text{eff}}$ of the pathway model, so
the phase numbers are those of that model, not of the end-member table.

## 3. Derivations

### 3.1 Why $m_{\text{eff}}$ has that form

Put the two pathways in parallel. The electrolyte path is a resistor,
$G_A = A$. The polarisable path is a Debye element with intrinsic chargeability
$m_0$ and time constant $\tau$:

$$G_B(\omega) = B\left[(1-m_0) + \frac{m_0}{1+i\omega\tau}\right].$$

The measured resistivity is $1/\left[G_A + G_B(\omega)\right]$. Its DC value is
$1/(A+B)$; its high-frequency value is $1/\left[A + B(1-m_0)\right]$, because the
polarisable path shunts at high frequency. The chargeability is the fractional
drop between them:

$$m_{\text{eff}} = 1 - \frac{\rho_{\infty}}{\rho_0}
= 1 - \frac{A + B}{A + B/(1-m_0)}
= \frac{m_0 B}{A(1-m_0) + B}.$$

Two limits are worth naming:

- **Electrolyte-dominated, $A \gg B$:** $m_{\text{eff}} \to
  \frac{m_0}{1-m_0}\cdot\frac{B}{A}$ — small, and falling as $1/A$, i.e. as the
  pore fluid gets more conductive.
- **Polarisable-path-dominated, $B \gg A$:** $m_{\text{eff}} \to m_0$ — the
  intrinsic polarisability, fully expressed.

For small $m_0$ the result simplifies to the sentence of Section 1:
$m_{\text{eff}} \approx m_0\,B/(A+B)$, the intrinsic polarisability times the
fraction of current in the polarisable path. Since the current fraction is
$B/(A+B)$, this is a *derived* statement about a current split, not an
assumption.

### 3.2 The measured trade-off between conductivity and polarisability

With $F = 6.617$, $B = 0.0020$ S/m and $m_0 = 0.90$ (the demonstration's
section 2 uses a strongly polarisable pathway to make the effect unmistakable):

| $\sigma_w$ (S/m) | $A$ (S/m) | $\sigma_{\text{bulk}}$ (S/m) | $\rho$ ($\Omega\,\mathrm{m}$) | $m_{\text{eff}}$ | peak $-\varphi$ (mrad) |
|---|---|---|---|---|---|
| 0.005 | 0.0008 | 0.0108 | 92.97 | 0.8933 | 414.370 |
| 0.020 | 0.0030 | 0.0130 | 76.79 | 0.8736 | 388.887 |
| 0.050 | 0.0076 | 0.0176 | 56.96 | 0.8368 | 348.099 |
| 0.200 | 0.0302 | 0.0402 | 24.86 | 0.6911 | 235.451 |
| 1.000 | 0.1511 | 0.1611 | 6.21 | 0.3584 | 91.471 |

The last three columns move together in the *opposite* direction to the first
three: conductivity rises 15-fold while $m_{\text{eff}}$ falls from $0.893$ to
$0.358$ and the peak phase from $414$ to $91$ mrad. **Polarisation and
conductivity are not independent indicators; they are two projections of one
pathway split.** An interpreter who sees a conductor and a low phase must
consider both "the pore fluid became saline" and "the surface pathway was
removed", because either produces both signatures.

### 3.3 Discrimination: which end-members can be told apart?

A phase spectrum alone is a poor classifier. The demonstration compares every
end-member's exact phase spectrum with every other end-member's model over
$0.01$–$100$ Hz at $41$ frequencies, with a stated phase noise of
$\sigma_{\varphi} = 2.0$ mrad, and reports the rms misfit in units of that noise.
Three pairs fall below $3\sigma$ and are therefore **not separable by phase
alone at this noise**:

| pair | rms misfit (units of $\sigma_{\varphi}$) |
|---|---|
| clean sand vs frozen ground | 0.69 |
| clay-rich soil vs frozen ground | 1.39 |
| clean sand vs clay-rich soil | 1.81 |

Every distinguishable pair — for example disseminated sulphide against
clay-rich soil, $15.5$; graphitic schist against massive sulphide, $25.4$ — is
separated by *shape*, and the confusable pairs are exactly those with the
smallest phase amplitudes.

Adding the amplitude to the comparison changes the picture completely. With
$1\%$ noise on $|\rho|$ as well, the smallest rms misfit across all pairs rises
to $71.1$ (clay-rich soil against disseminated sulphide), and the previously
confusable pairs reach $212.6$ (clean sand against clay-rich soil), $93.3$
(clean sand against frozen ground) and $305.9$ (clay-rich against frozen
ground). **None of them is confusable any more.** The reason is that the
confusable pairs differed in $\rho_0$ by factors of $3$ to $75$
($800$ vs $40$ vs $3000\ \Omega\,\mathrm{m}$), which the phase spectrum does not
constrain at all.

The practical statement is a two-part one: the discriminant is the *pair*
$\left(\rho_0, \varphi(\omega)\right)$, and the shape of the phase spectrum is
what separates similar-amplitude responses.

### 3.4 Mixtures inside a band are not identifiable

Section 3.3 compared models from a fixed dictionary. The stronger statement is
that two structurally different grounds can produce the *same measurement*. The
demonstration generates an exact two-component response
($\rho_0 = 60.0\ \Omega\,\mathrm{m}$, $m = 0.25$, equal weights at
$\tau = 0.02$ s and $2.0$ s, $c = 0.50$ each), samples it over $0.01$–$100$ Hz
with $1\%$ amplitude and $2$ mrad phase noise, and fits two different models:

| model | parameters | rms phase residual |
|---|---|---|
| single Cole-Cole (4 parameters) | $\rho_0 = 61.52\ \Omega\,\mathrm{m}$, $m = 0.2936$, $c = 0.3112$, $\tau = 0.204$ s | 2.054 mrad |
| two-component mixture (5 parameters) | $\rho_0 = 60.11\ \Omega\,\mathrm{m}$, $m = 0.2532$, $\tau = 0.021$ s (0.511) and $2.257$ s (0.489) | 1.766 mrad |

Both are acceptable at the stated noise (the residuals are comparable to the
$2.0$ mrad noise), and the two-component fit recovers the truth (weights
$0.51/0.49$ against $0.5/0.5$) while the single Cole-Cole does not. Inside the
band they are the same measurement. Outside it they part: at $10^{-4}$ Hz the
phases are $7.737$ and $3.467$ mrad (a difference of $4.270$ mrad), at
$10^{3}$ Hz, $16.899$ and $10.296$ mrad ($6.603$ mrad), and the amplitudes
differ by up to $1.8\%$ at $10^{4}$ Hz.

So the honest report of an IP spectrum on a limited band is a *pair* of
admissible models with the residuals, not a fitted triple presented as rock
properties. The extra decade — down to $10^{-4}$ Hz or up to $10^{3}$ Hz — is
what would decide between them, and a survey design that cannot afford it should
say so.

### 3.5 Three scenarios in the $(\rho, \varphi)$ plane

Finally, apply the pathway model to three scenarios that a shallow survey might
actually encounter, using the base parameters of Section 2.3:

| scenario | what changes | $\rho$ ($\Omega\,\mathrm{m}$) | $m_{\text{eff}}$ | peak $-\varphi$ (mrad) |
|---|---|---|---|---|
| base | — | 104.65 | 0.0823 | 17.787 |
| clay-rich | surface conductance $\times 20$, pore fluid $0.02$ S/m | 23.24 | 0.2849 | 69.268 |
| plume | pore fluid $1.0$ S/m, surface unchanged | 6.53 | 0.0056 | 1.156 |
| frozen | pore fluid $10^{-5}$ S/m, surface $\times 0.02$, intrinsic $m_0 = 0.02$ | 24 089.88 | 0.0193 | 4.033 |

Against the base case, and using the stated detection thresholds of $1\%$ on
conductivity and $2$ mrad on phase, all three scenarios are detected by both
measurements ($-77.8\%$, $-93.8\%$, $+22\,920.3\%$ in resistivity; $+51.481$,
$-16.631$, $-13.754$ mrad in phase). The interesting question is not
detectability but separation, and here the two measurements do different jobs:

- **Resistivity alone** puts the clay-rich case ($-77.8\%$) and the plume
  ($-93.8\%$) both in the "conductor" class. Only the phase value separates
  them, and by a large margin: $1.156$ mrad against $69.268$ mrad.
- **Phase alone** puts the plume ($1.156$ mrad) and the frozen case
  ($4.033$ mrad) both in the "low-phase" class. Only the resistivity separates
  them: $6.53$ against $24\,089.88\ \Omega\,\mathrm{m}$.

Acquiring both puts the three scenarios at distinct points of the $(\rho,
\varphi)$ plane. That is the quantitative reason a resistivity and an IP
measurement are made together rather than either alone — and it is a statement
about *this model*, whose limitations are listed in Section 5.

## 4. Physical interpretation

- **$m_{\text{eff}}$ is a current split before it is a material property.**
  Anything that changes the pore-fluid conductivity changes the measured
  chargeability of an unchanged mineral assemblage.
- **Small phases carry little shape information.** The three confusable pairs of
  Section 3.3 all have peak phases below $8$ mrad. A phase of a few mrad, measured
  with $2$ mrad noise, cannot be classified by shape.
- **$\rho_0$ carries most of the discrimination.** Adding amplitude to the
  comparison raised the minimum misfit from $0.69\sigma$ to $71.1\sigma$.
- **Broadening and amplitude are separate questions.** An altered mineralogy
  changes the shape (Section 3.4); a changed pore fluid changes the level
  (Section 3.2). Confusing the two is the classic IP interpretation error.
- **Monitoring is the natural application.** Because the pathway split responds
  to the pore fluid, time-lapse IP is a pore-fluid measurement: a change in
  phase over a survey interval is evidence of a change in fluid chemistry or in
  saturation, provided the survey geometry and the noise are unchanged.

## 5. Assumptions and regime of validity

1. **A two-pathway parallel model.** Real ground has a continuum of surface
   conduction, of grain-size-controlled relaxations and of pore geometries. The
   two-pathway split is the minimal model that reproduces the trade-off of
   Section 3.2, and it should not be pushed to quantitative prediction.
2. **Archie-type electrolyte term** $\sigma_e = \sigma_w/F$ with a constant
   formation factor. This assumes a water-saturated, clay-free pore network for
   the electrolyte term; where $B$ is large, the electrolyte term is no longer
   the whole story and $F$ becomes an effective parameter.
3. **The surface conductance $B$ is constant** in Sections 3.2 and 3.5. In a real
   sample $B$ depends on the specific surface area, on the cation exchange
   capacity and on the pore-fluid concentration itself (through the double-layer
   thickness), so the model overstates the simplicity of the trade-off.
4. **No frequency dependence of $A$ or $B$.** Both are treated as constants; the
   polarisation lives entirely in the $m_0$ element.
5. **Isotropic, homogeneous each model element; no geometry.** No electrode
   array, no current distribution and no depth are represented — only the
   intrinsic response of a material.
6. **Frozen ground is modelled as three simultaneous changes** and in particular
   by setting the intrinsic chargeability of the ice-coated pathway to $0.02$.
   The model contains no unfrozen water film, no ice dielectric relaxation and no
   temperature dependence. **It quantifies sensitivity logic and nothing else.**
   Any statement about actual permafrost requires measurement.
7. **No mineralogy identification.** Nothing here maps $(\rho_0, m, c, \tau)$
   onto a mineral name. A phase is not a mineral.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| pore-fluid conductivity | $\sigma_w$ | S/m | |
| formation factor | $F = \phi^{-\mathrm{CEM}}$ | dimensionless | porosity dimensionless, exponent dimensionless |
| electrolyte conductance | $A = \sigma_w/F$ | S/m | |
| surface conductance | $B$ | S/m | same as $A$, so they can be added |
| bulk conductivity | $\sigma_{\text{bulk}} = A+B$ | S/m | |
| resistivity | $\rho_0 = 1/\sigma_{\text{bulk}}$ | $\Omega\,\mathrm{m}$ | reciprocal of S/m |
| effective chargeability | $m_{\text{eff}}$ | dimensionless | ratio of conductances times $m_0$ |
| phase | $\varphi$ | rad (reported mrad) | argument of a complex ratio |

A useful check on any $m_{\text{eff}}$ computation: it must lie between $0$ and
$m_0$, and it must equal $m_0$ when $A = 0$ and approach
$m_0/(1-m_0)\cdot B/A$ when $A \gg B$. If a computed value exceeds $m_0$, a
conductance or a bracket has been misplaced.

## 7. Worked examples

### Example 1 — the base case by hand

Inputs: $\sigma_w = 0.05$ S/m, $\phi = 0.35$, $\mathrm{CEM} = 1.80$,
$B = 0.0020$ S/m, $m_0 = 0.30$.

1. Formation factor: $F = \phi^{-\mathrm{CEM}} = 0.35^{-1.80} = 6.617$.
2. Electrolyte pathway: $A = \sigma_w/F = 0.05/6.617 = 0.007556$ S/m.
3. Bulk conductivity: $\sigma_{\text{bulk}} = A + B = 0.007556 + 0.002000
   = 0.009556$ S/m, hence $\rho_0 = 1/0.009556 = 104.65\ \Omega\,\mathrm{m}$ —
   the printed base case.
4. Current fraction in the polarisable pathway: $B/\sigma_{\text{bulk}} =
   0.002000/0.009556 = 0.2093$.
5. Effective chargeability:
   $m_{\text{eff}} = 0.30 \times 0.002000/\left(0.007556\times0.70 + 0.002000\right)
   = 0.000600/\left(0.005289 + 0.002000\right) = 0.000600/0.007289
   = 0.0823$ — the printed value.
6. Note the difference between steps 4 and 5: the current fraction is $0.2093$
   but $m_{\text{eff}}/m_0 = 0.0823/0.30 = 0.2744$. The two agree only in the
   limit $m_0 \to 0$, because a large $m_0$ also shunts the polarisable pathway at
   high frequency, which is exactly the $(1-m_0)$ in the denominator.

### Example 2 — why the plume lowers the phase

Same ground, pore fluid replaced by a saline one with $\sigma_w = 1.0$ S/m.

1. $A = 1.0/6.617 = 0.15113$ S/m; $\sigma_{\text{bulk}} = 0.15113 + 0.00200
   = 0.15313$ S/m; $\rho_0 = 6.53\ \Omega\,\mathrm{m}$.
2. $m_{\text{eff}} = 0.30\times0.00200/\left(0.15113\times0.70 + 0.00200\right)
   = 0.000600/\left(0.105791 + 0.002000\right) = 0.000600/0.107791
   = 0.00557$.
3. The peak phase falls from $17.787$ to $1.156$ mrad, i.e. by
   $-16.631$ mrad, while the resistivity falls by $93.8\%$.
4. In the "current fraction" language: the polarisable pathway's share falls from
   $0.2093$ to $0.00200/0.15313 = 0.01306$, a factor $16$. The measured
   chargeability ratio is $0.00557/0.0823 = 0.0677$, a factor $14.8$ — the
   small-$m_0$ approximation is accurate here to $8\%$.

### Example 3 — detecting a small salinity change

Both thresholds of Section 3.5 are exceeded by the plume of Example 2, but a
plume is not usually the question: the question is the *smallest* change
detectable. The demonstration scans the pore-fluid conductivity upward from
$0.050$ S/m in steps of $2.5\times10^{-4}$ S/m and records where each threshold
is first crossed:

| threshold reached | $\sigma_w$ (S/m) | change in $\sigma_w$ | change in $\rho$ | change in peak phase |
|---|---|---|---|---|
| $-2$ mrad of phase | 0.05850 | $+17.00\%$ | $-11.85\%$ | $-2.029$ mrad |
| $-1\%$ of resistivity | 0.05075 | $+1.50\%$ | $-1.17\%$ | $-0.200$ mrad |

Read it as two statements. To reach the phase threshold the pore fluid must
become $17.00\%$ more conductive, and by then the resistivity has *already*
moved $-11.85\%$, about twelve times its own $1\%$ threshold. Conversely a
$1.17\%$ resistivity change corresponds to a $1.50\%$ change in pore-fluid
conductivity and moves the phase by only $-0.200$ mrad — an order of magnitude
below what the phase measurement can resolve. **In this model the resistivity is
the more sensitive detector of a small salinity change, and the phase the better
classifier of a large one.** Both conclusions come from the same pathway
equation, and both are model statements: a real survey's relative sensitivity
depends on its own noise levels, which must be substituted here.

## 8. Python demonstration

`code/ip_applications_demo.py` prints every number in this lesson. It:

1. tabulates six synthetic end-members with their phase spectra, peak phases and
   peak frequencies;
2. tabulates the pathway model: bulk conductivity, $m_{\text{eff}}$ and peak
   phase against pore-fluid conductivity;
3. builds the confusion matrices (phase only, and phase plus amplitude) for all
   $36$ ordered pairs and lists the pairs that cannot be separated at the stated
   noise;
4. fits a single Cole-Cole and a two-component mixture to one exact
   two-component response, and compares the two fits inside and outside the band;
5. computes the base, clay-rich, plume and frozen scenarios and reports the
   resistivity and phase changes against the stated detection thresholds.

Run it with the project virtual environment:

```bash
cd 09-electrical-em-methods/03-induced-polarisation/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python ip_applications_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/04-ip-applications-exercises.md`](./exercises/04-ip-applications-exercises.md)
and
[`exercises/04-ip-applications-solutions.md`](./exercises/04-ip-applications-solutions.md).

- **★** With $F = 6.617$, $B = 0.002$ S/m, $m_0 = 0.3$, compute $m_{\text{eff}}$
  and $\rho_0$ for $\sigma_w = 0.01$ S/m.
- **★** State which of the six synthetic end-members has the largest peak phase
  and which has the largest peak frequency, and by what factors.
- **★★** Derive $m_{\text{eff}} = m_0B/[A(1-m_0)+B]$ from the parallel
  conductance model, and verify it for the extreme cases $A = 0$ and $A \gg B$.
- **★★** Using the confusion matrices, decide whether a survey can distinguish
  clay-rich soil from frozen ground using phase alone at $2$ mrad noise, and
  state the measurement that resolves it.
- **★★★** Design the extra band that would separate the two models of
  Section 3.4, and estimate the noise level at which the $6.6$ mrad out-of-band
  difference becomes significant.

## 10. Common mistakes

1. **Reading a phase as a mineralogy.** A phase is a current split in this
   model; the same mineral gives different phases in different pore fluids.
2. **Interpreting a low phase as "no polarisation".** It can equally be
   "polarisation swamped by a conductive pore fluid".
3. **Classifying by phase shape when the phase is a few mrad.** At $2$ mrad noise
   three synthetic pairs are inseparable.
4. **Discarding the amplitude.** It raised the minimum misfit from $0.69$ to
   $71.1$ noise units in Section 3.3.
5. **Quoting a single fitted Cole-Cole triple as the structure.** Section 3.4
   shows a single Cole-Cole and a two-component mixture are equally admissible in
   band.
6. **Treating permafrost as "just a resistor."** In this model the phase also
   changes, and the model's own limitations (no unfrozen film, no temperature
   dependence) must be stated with any claim.
7. **Comparing surveys with different windows or frequencies.** The numbers are
   convention-bound; see [09-03-03](03-ip-acquisition.md).

## 11. Real-world applications

- **Sulphide exploration.** Disseminated sulphide is the classic IP target
  because the electronic-conduction pathway polarises strongly; the lesson's
  contribution is the reminder that the *host* conductivity controls how much of
  that polarisation is visible.
- **Clay and salinity mapping.** The inverse relation between pore-fluid
  conductivity and $m_{\text{eff}}$ is what lets combined resistivity and IP
  distinguish a clay-rich layer from a saline one.
- **Leachate and contaminant plumes.** A conductive plume reduces the phase of
  the ground it invades even while raising the conductivity — the two
  measurements are complementary rather than redundant.
- **Permafrost and frozen ground monitoring.** Time-lapse resistivity is the
  standard tool; adding IP changes the question from "did it freeze" to "did the
  polarisable surface remain connected", which is a different and sometimes more
  useful question.
- **Archaeology and buried structures.** Where the target is a contrasting
  material rather than a polarisable one, IP adds shape discrimination to a
  resistivity image.

## 12. Further reading

- **Binley, A., & Kemna, A., "DC resistivity and induced polarization methods",
  in *Hydrogeophysics* (Springer).** Level: research review. The pathway and
  surface-conduction models in the hydrogeophysical setting.
- **Revil, A., et al., reviews of the induced-polarisation of soils and rocks
  (in *Journal of Geophysical Research* and *Water Resources Research*).**
  Level: research. The polarisation of the electrical double layer, quantitatively.
- **Sumner, J. S., *Principles of Induced Polarization for Geophysical
  Exploration* (Elsevier).** Level: research monograph. Case histories and
  the classical mineral-exploration interpretation.
- **Reynolds, J. M., *An Introduction to Applied and Environmental
  Geophysics* (2nd ed., Wiley-Blackwell).** Level: textbook. Environmental and
  engineering applications, including landfill and permafrost work.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. **No number in this lesson is
> quoted from any of them.** Every figure is printed by
> [`code/ip_applications_demo.py`](./code/ip_applications_demo.py), and every
> end-member parameter is a synthetic teaching value stated in Section 2.1.

## 13. Related lessons

- [01 IP Principle: Time-Domain and Frequency-Domain Measurement](01-ip-principle.md) —
  the chargeability and phase conventions.
- [02 IP Models: Cole-Cole, Debye, Constant-Phase Element](02-ip-models.md) —
  the spectral models fitted in Section 3.4.
- [03 IP Acquisition, Chargeability and Phase Units](03-ip-acquisition.md) —
  the noise levels that set the detection thresholds.
- [09-01-02 Archie's Law, Porosity and Saturation](../01-electrical-properties-of-earth/02-archies-law.md) —
  the formation factor used in $A = \sigma_w/F$.
- [09-05-05 EM for Contaminant Plumes, Salinity and Leachate](../05-em-methods-applications/05-em-environmental.md) —
  the same plume problem measured with electromagnetic induction instead of
  electrodes.

## 14. Self-assessment checklist

- [ ] I can draw the two pathways and label them with conductances.
- [ ] I can derive $m_{\text{eff}}$ and check it against its two limits.
- [ ] I can compute $\sigma_{\text{bulk}}$, $\rho_0$ and $m_{\text{eff}}$ from
      $\sigma_w$, $F$ and $B$.
- [ ] I can explain why a saline plume lowers the phase and raises the
      conductivity.
- [ ] I can read the confusion matrices and say what fraction of a phase is
      classifiable.
- [ ] I can state two models that are indistinguishable in a band and what would
      separate them.
- [ ] I can position a clay, a plume and frozen ground in the $(\rho, \varphi)$
      plane and say which measurement separates each pair.
- [ ] I can list what the pathway model does not represent.
