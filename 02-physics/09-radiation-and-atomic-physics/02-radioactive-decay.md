---
id: 02-09-02
title: "Radioactive Decay, Half-Life and Dating"
level: intermediate
prereqs: ["02-09-01", "01-08-01", "02-01-02"]
estimated_minutes: 90
tags: [radioactive-decay, geochronology, isochron, half-life, closure-temperature]
---

# Radioactive Decay, Half-Life and Dating

A radiometric age is not a measurement of time. It is a measurement of a ratio
of concentrations, converted into a time by a model, and the model carries every
assumption that matters. This lesson derives the decay law, derives the
isochron equation rather than quoting it, and then is explicit about the two
things that turn a number of years into a defensible age: a **closure
temperature** and a **stated initial condition**.

The distinction the lesson is built around is between an **age** and a **model
age**. An age comes from a set of samples that together determine both the
slope and the intercept of a line — the isochron — so the initial isotopic
composition is measured rather than assumed. A model age comes from one sample
and one assumed initial composition, and it is exactly as good as that
assumption, no better. The demo in this lesson quantifies the difference: for
one synthetic Rb–Sr sample, two defensible assumptions about the initial
$^{87}$Sr/$^{86}$Sr ratio give ages of 451 Ma and 188 Ma, against an isochron
age of 349 Ma, for a rock whose true age is 350 Ma.

This is the module's mastery lesson. Work it, do not read it.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** $N(t) = N_0 e^{-\lambda t}$ from a constant probability of decay
   per unit time, and derive $T_{1/2} = \ln 2/\lambda$ and $\tau = 1/\lambda$.
2. **Convert** between half-life and decay constant in both s⁻¹ and a⁻¹, check
   the unit algebra, and compute a specific activity at a stated concentration.
3. **Derive** the two-member Bateman solution and the secular-equilibrium
   condition, and explain why one gamma line reports a whole chain.
4. **Derive** the isochron equation from the decay law and compute an age from a
   fitted slope.
5. **Distinguish** an isochron age from a model age, state the assumptions each
   requires, and identify which of them a dataset can test.
6. **Explain** closure temperature, solve the Dodson equation for a stated
   cooling rate, and say why two chronometers in one rock give different ages.
7. **Contrast** the Rb–Sr, U–Pb, K–Ar/Ar–Ar, Sm–Nd and $^{14}$C systems in
   half-life, in what they date, and in their dominant failure mode.
8. **State**, for any half-life you use, which compilation it came from and by
   how much another compilation differs.

## Prerequisites

- [02-09-01 Atomic Structure and Energy Levels](./01-atomic-structure.md) — what
  the nucleus leaves behind in the electron shells, and why a decay mode is
  visible in an X-ray spectrum.
- [01-08-01 First-Order ODEs: Separation of Variables and Integrating Factors](../../01-mathematics/08-ordinary-differential-equations/01-first-order-odes.md)
  — the mathematics of $\dot N = -\lambda N$ and of the coupled chain equations.
- [02-01-02 Measurement Uncertainty, Significant Figures and Error Bars](../01-measurement-and-physical-reasoning/02-measurement-uncertainty.md)
  — an age without an uncertainty and a stated model is not an age.

## 1. The decay law, derived

**The single physical assumption.** Each nucleus has, at every instant, the same
probability $\lambda\,\mathrm{d}t$ of decaying in the next interval
$\mathrm{d}t$, independently of its age and of its environment. There is no
"memory" and no clock inside the nucleus. Everything else is consequence.

Take a population of $N(t)$ identical nuclei. Either a nucleus has decayed or
it has not, so $N$ is a binomial count with survival probability
$p = (1 - \lambda\,\mathrm{d}t)$ per step. Over $k = t/\mathrm{d}t$ independent
steps the survival probability is

$$p^k = (1 - \lambda t/k)^k \;\xrightarrow[k \to \infty]{}\; e^{-\lambda t},
\tag{1}$$

using the standard limit of the exponential
([01-08-01](../../01-mathematics/08-ordinary-differential-equations/01-first-order-odes.md)).
Hence

$$N(t) = N_0 e^{-\lambda t}, \tag{2}$$

and, taking the derivative or the expectation of the decay count,

$$\frac{\mathrm{d}N}{\mathrm{d}t} = -\lambda N . \tag{3}$$

Equation (2) is exact given the assumption; equation (3) is the same statement
in differential form. Note what has not been used: no temperature, no pressure,
no chemistry, no mineralogy. This is why radiometric dating works at all — and
it is also why an age that is wrong is almost never wrong because the decay law
failed. It is wrong because a nucleus left or arrived.

**The three constants.** From (2), $N/N_0 = 1/2$ at

$$T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0.693\,147}{\lambda}, \tag{4}$$

and the mean life, which is the expectation of $t$ over the exponential
distribution, is $\tau = 1/\lambda = T_{1/2}/\ln 2 = 1.4427\,T_{1/2}$. The
**activity** of a sample is the decay rate,

$$A = \lambda N, \qquad A(t) = A_0 e^{-\lambda t}, \tag{5}$$

in becquerel (1 Bq = 1 decay per second). The legacy unit, still in some
regulations and instrument specifications, is the curie, defined exactly as
$1\ \mathrm{Ci} = 3.7 \times 10^{10}$ Bq.

**Half-lives are measured quantities and compilations differ.** This is not a
formality. The half-life of $^{87}$Rb has been quoted as $4.7$, $4.88$ and
$5.0 \times 10^{10}$ a in different eras of the literature — a spread of
6 per cent and therefore a 6 per cent spread in every Rb–Sr age. The community
resolved it by convention: the IUGS Subcommission on Geochronology recommended
(Steiger & Jäger, 1977) $\lambda_{^{87}\mathrm{Rb}} = 1.42 \times 10^{-11}$ a⁻¹,
and ages published before that convention are not directly comparable with ages
published after it unless recomputed. Likewise $^{40}$K has been tabulated as
$1.25$ and $1.277 \times 10^9$ a, and $^{14}$C as 5568 and 5730 a, with an
entire naming convention — "conventional radiocarbon age" — built on the
difference.

The rule this curriculum imposes is therefore: **state the value you use and
where it came from.** The values used below are listed in
[`code/radioactive_decay_demo.py`](./code/radioactive_decay_demo.py) as
tabulated inputs drawn from the evaluated nuclear-data compilations (NNDC
ENSDF, distributed with the NuDat interface) and the IUPAC isotopic abundances.
Confirm the current value in those compilations, and cite the edition, before
publishing a number.

Two checks on any half-life you use. Compute $\lambda = \ln 2/T_{1/2}$ and
confirm the unit: with $T_{1/2}$ in seconds, $\lambda$ is in s⁻¹, and
$\lambda T_{1/2}$ must return $\ln 2$ in any unit system. Confirm that the
implied mean life is *longer* than the half-life by 1.4427 — a factor of 1.4427
in the wrong direction is a common slip. The demo shows both columns side by
side for eight nuclides (§8).

## 2. Chains, Bateman equations and equilibrium

A decay rarely ends at the first step: $^{238}$U decays to $^{234}$Th, then to
$^{234}$Pa, and so on through fourteen steps to stable $^{206}$Pb. For each
member $i$ of a chain,

$$\frac{\mathrm{d}N_i}{\mathrm{d}t} = \lambda_{i-1}N_{i-1} - \lambda_i N_i . \tag{6}$$

For two members with $N_2(0) = 0$, $\lambda_1 \ne \lambda_2$, the solution is

$$N_2(t) = N_1(0)\frac{\lambda_1}{\lambda_2 - \lambda_1}
\left(e^{-\lambda_1 t} - e^{-\lambda_2 t}\right). \tag{7}$$

This is the **Bateman solution** for two members; the general $n$-member case is
a sum of exponentials built the same way. The script verifies (7) against
numerical integration of (6) and reports a maximum relative difference of
$6.6 \times 10^{-15}$ over the range tested, which is round-off.

Two limits matter in practice.

**Secular equilibrium:** $\lambda_1 \ll \lambda_2$, i.e. the parent lives far
longer than the daughter. The daughter's activity rises on the parent's
timescale and, after a few daughter half-lives, settles to $\lambda_2 N_2 =
\lambda_1 N_1$. For the top of the $^{238}$U chain, one year is 15.15 half-lives
of $^{234}$Th ($T_{1/2} = 24.10$ d) while $^{238}$U has decayed by
$1.55 \times 10^{-8}$ per cent. The demo measures the resulting activity ratio
as 0.999972 and compares the deficit with $2^{-15.15} = 2.760 \times 10^{-5}$:
agreement to three significant figures.

**Transient equilibrium:** the parent's half-life is comparable with or shorter
than the daughter's. The activity ratio settles to a constant different from
unity, and the rate of change of the whole chain is set by the parent.

The practical consequence of secular equilibrium is the single most useful fact
in radiometric prospecting: in an undisturbed rock **every member of a series
has the same activity**, so one gamma line of one member reports the whole
series. A spectrometer counting the 1764 keV line of $^{214}$Bi is measuring the
$^{238}$U series, not bismuth. This is why uranium from gamma-ray spectrometry is
reported as "equivalent uranium", eU: the measurement is a chain activity
converted through an assumed equilibrium, and any disequilibrium breaks the
conversion. Radon escape from the top metres of soil does exactly that, moving
the $^{226}$Ra–$^{222}$Rn pair out of equilibrium while the rest of the chain
stays put — which is why a radiometric uranium anomaly is a lead to be followed
up, not an assay.

## 3. The isochron, derived

Let a radioactive parent $P$ decay to a daughter $D$, and let a stable,
non-radiogenic isotope $S$ of the daughter element be present. The measured
daughter at time $t$ is the initial daughter plus the amount produced:

$$D(t) = D_0 + \left[P_0 - P(t)\right]. \tag{8}$$

Since $P(t) = P_0 e^{-\lambda t}$, we have $P_0 = P(t)e^{\lambda t}$ and

$$D(t) = D_0 + P(t)\left(e^{\lambda t} - 1\right). \tag{9}$$

Divide through by the stable isotope $S$, whose abundance does not change:

$$\underbrace{\frac{D}{S}}_{\text{measured}}
= \underbrace{\frac{D_0}{S}}_{\text{intercept}}
+ \underbrace{\frac{P}{S}}_{\text{measured}}
\left(e^{\lambda t} - 1\right). \tag{10}$$

**This is the isochron equation.** It is a straight line in the plane of the
two measured ratios: $D/S$ against $P/S$. The slope is $e^{\lambda t} - 1$ and
the intercept is the initial daughter ratio. Inverting,

$$t = \frac{1}{\lambda}\ln\left(1 + \text{slope}\right). \tag{11}$$

Everything about a defensible age is in (10) and (11):

- **The intercept is measured, not assumed.** Several samples that formed
  together with different $P/S$ ratios — different rubidium contents in
  different minerals — define a line whose intercept is the initial isotopic
  composition of that rock at that time.
- **The denominator must be stable and non-radiogenic.** $^{86}$Sr is produced
  by no decay, so it can serve as the reference; $^{87}$Sr cannot, and using it
  destroys the linearity.
- **A line is a test.** The samples must be cogenetic (same age, same initial
  ratio) and closed. If they scatter around a line by more than their analytical
  errors, one of those conditions fails and the slope is not an age. That test
  is not available to a model age at all.

**Worked example, from the demo.** A synthetic whole-rock Rb–Sr dataset was
generated with a true age of $3.5 \times 10^8$ a, an initial
$^{87}$Sr/$^{86}$Sr of 0.7065, and $T_{1/2}(^{87}\mathrm{Rb}) = 4.88 \times
10^{10}$ a, i.e. $\lambda = 1.420\,384 \times 10^{-11}$ a⁻¹. Least squares
returns

```text
  Least squares slope     = 4.965182e-03  +/- 5.37e-05
  Least squares intercept = 0.706530  (true 0.7065)
  Recovered age           = 3.487013e+08 a  +/- 3.76e+06
  Relative error in age   = 3.710e-03
```

The true age lies within one standard error of the recovered age, and the
intercept is recovered to five parts in $10^5$. Now treat the same single sample
$x = ^{87}\mathrm{Rb}/^{86}\mathrm{Sr} = 1.60$, $y = 0.714274$ as a model age,
with two defensible assumed initial ratios:

```text
  Model age of the single sample with 87Rb/86Sr = 1.60:
    assuming initial ratio 0.7040 -> 450.6 Ma
    assuming initial ratio 0.7100 -> 187.8 Ma
```

The isochron age is 349 Ma; the two model ages are 451 and 188 Ma — a spread of
263 Ma from a change of 0.006 in an assumption. Mantle-derived rocks have
initial $^{87}$Sr/$^{86}$Sr near 0.704 and granites near 0.71, so these are not
strawmen: they are the values a careful worker would consider. The lesson is not
that model ages are worthless — for some systems and rocks they are the only
option — but that a model age must be *labelled* as one, with its assumption
stated. A "Rb–Sr age" with neither an isochron nor a stated initial ratio is not
a reproducible measurement.

## 4. The chronometers, and what each one actually dates

| System | Parent → daughter | Half-life (TABULATED) | Denomination | What it dates |
|---|---|---|---|---|
| Rb–Sr | $^{87}$Rb → $^{87}$Sr | $4.88 \times 10^{10}$ a | $^{86}$Sr | Whole-rock crystallisation; metamorphism if the rock re-equilibrates |
| U–Pb | $^{238}$U → $^{206}$Pb | $4.468 \times 10^9$ a | $^{204}$Pb | Zircon crystallisation, with a built-in consistency test |
| U–Pb | $^{235}$U → $^{207}$Pb | $7.038 \times 10^8$ a | $^{204}$Pb | The same event, from an independent parent |
| K–Ar | $^{40}$K → $^{40}$Ar | $1.248 \times 10^9$ a | $^{36}$Ar | Cooling below the closure temperature of the host mineral |
| Sm–Nd | $^{147}$Sm → $^{143}$Nd | $1.06 \times 10^{11}$ a | $^{144}$Nd | Crystallisation of mafic and ancient rocks; resistant to alteration |
| $^{14}$C | $^{14}$C → $^{14}$N | 5730 a (see below) | stable carbon | Death of an organism, up to roughly 50 ka |

All half-lives in this table are commonly tabulated values and differ between
compilations in the digits shown; the Sm–Nd value in particular is quoted in the
literature anywhere between about $1.05 \times 10^{11}$ and $1.07 \times 10^{11}$
a, a difference of 2 per cent that matters for rocks older than 1 Ga. Confirm
each one in the compilation you cite.

**U–Pb has a built-in test.** Because $^{235}$U and $^{238}$U decay to
different lead isotopes in the same mineral, one sample gives two independent
ages. Plotting $^{206}$Pb/$^{238}$U against $^{207}$Pb/$^{235}$U traces the
**concordia** curve, parameterised by $t$:

$$\frac{^{206}\mathrm{Pb}}{^{238}\mathrm{U}} = e^{\lambda_{238}t} - 1,
\qquad
\frac{^{207}\mathrm{Pb}}{^{235}\mathrm{U}} = e^{\lambda_{235}t} - 1 . \tag{12}$$

A sample that lost lead lies below the concordia, on a chord (a **discordia**)
whose upper intercept is the crystallisation age and whose lower intercept is
the age of the disturbance. This is the most powerful self-checking chronometer
available, and it works because the two clocks have different half-lives and
therefore respond differently to the same disturbance.

**K–Ar and Ar–Ar date cooling, not crystallisation.** The argon that
accumulates is a noble gas and diffuses out above a blocking temperature, so the
measured age is the time since the mineral cooled through it. In the Ar–Ar
variant the sample is irradiated to convert $^{39}$K to $^{39}$Ar, so parent and
daughter are measured in the same gas release step; step-heating then produces
an age spectrum, and a **plateau** over several steps is evidence that the gas
has stayed put. In a slowly cooled terrain, K–Ar in hornblende, muscovite,
biotite and feldspar gives a *sequence* of ages recording the cooling history —
the basis of thermochronology, and the reason "the age of the rock" is often
several numbers.

**Radiocarbon is different in kind.** $^{14}$C is produced continuously in the
atmosphere by cosmic-ray neutrons acting on nitrogen, so the clock is not a
closed system but a *reservoir*. The age equation is unchanged, but the assumed
initial activity is a property of the atmosphere, and its $^{14}$C/$^{12}$C
ratio varies with the geomagnetic field, solar activity and — since the
industrial era — fossil-fuel burning and nuclear testing. Hence the two
half-lives and the two kinds of age:

```text
   measured A/A_modern   Libby age (a)  Cambridge age (a)  difference (a)
                 0.750          2310.9             2378.2            67.2
                 0.500          5568.0             5730.0           162.0
                 0.100         18496.5            19034.6           538.2
                 0.050         24064.5            24764.6           700.2
```

A **conventional radiocarbon age** is defined with the Libby half-life of 5568 a
and with a fixed reference standard, and it is *not* a calendar age. Converting
it to a calendar age requires **calibration** against a measured curve built
from dendrochronologically dated wood and other archives. The calibration
correction is typically hundreds of years and reaches more than a millennium in
places, because the atmospheric production rate has never been constant. Any
statement of a $^{14}$C age must therefore say which of the three it is:
conventional age, calibrated age with the curve named and its version, or
model age against an assumed initial activity.

## 5. Closure temperature

The isochron derivation assumed the system was closed. Nothing in nature is
closed for ever, and the transition happens at a temperature. A daughter isotope
diffusing through a mineral has $D(T) = D_0\exp(-E_a/RT)$, so diffusion falls
off exponentially as the rock cools and there is a temperature below which the
daughter is effectively immobile for the remaining history. Dodson's equation
for that **closure temperature** $T_c$ is

$$\frac{E_a}{RT_c} = \ln\left(\frac{A\,R\,T_c^2 D_0}
{E_a\,a^2\,(\mathrm{d}T/\mathrm{d}t)}\right), \tag{13}$$

where $a$ is the effective diffusion radius of the grain and $A$ is a geometry
factor (55 for a sphere, 27 for a cylinder, 8.7 for a plane sheet). It is
implicit in $T_c$ and is solved by iteration. The demo does exactly that with
declared, illustrative parameters ($E_a = 200$ kJ/mol, $D_0 = 10^{-4}$ m²/s,
$a = 0.5$ mm):

```text
   cooling rate (K/Ma)      Tc (K)      Tc (C)
                     1       551.5       278.3
                    10       580.8       307.6
                   100       613.2       340.1
                  1000       649.5       376.3
```

The physics to read off is the direction: **slower cooling gives a lower
closure temperature**. A grain cooling at 1 K/Ma has far longer at each
temperature than one cooling at 1000 K/Ma, so it continues losing the daughter
to lower temperatures before retention finally wins. "The closure temperature of
biotite" is therefore not a number but a number *given a cooling rate*, and a
closure temperature quoted without one is incomplete. Two consequences make
thermochronology possible: a mineral records the time it passed through its
$T_c$, and two chronometers with different $T_c$ in one rock record two
different times. A consistent sequence of ages from several chronometers is
evidence that the cooling history is real; a single age is one point on an
unknown curve.

## 6. Assumptions and regime of validity

Every age is a model output, and each model assumption has a diagnostic. The
**decay constant** is assumed known and constant: state the compilation, because
half-lives differ between them. The system is assumed **closed** for parent,
daughter and reference isotope: daughter loss or parent gain shows up as excess
scatter about the isochron, as discordia in U–Pb, or as a disturbed Ar–Ar age
spectrum. The samples are assumed **cogenetic** — one age and one initial ratio
— and a curved isochron or excessive scatter falsifies that. The chain is
assumed in **secular equilibrium**, tested by analysing more than one chain
member. And the initial daughter is assumed **zero** unless it is fitted as an
isochron intercept; a large nonzero intercept is the diagnostic for excess argon
or inherited lead.

The five failure modes worth naming in a report:

1. **Daughter loss.** Zircon that lost lead gives too young an apparent age,
   identified by the discordia construction; biotite that lost argon gives an
   age too young by an amount set by the cooling history, not by the rock.
2. **Excess daughter.** Argon trapped from the surrounding fluid, or inherited
   lead, gives too old an age. The diagnostic is a large, nonzero intercept.
3. **Inheritance.** A zircon with a 2.7 Ga core and a 1.1 Ga rim holds two ages
   in one grain, and a single-grain analysis reports a meaningless mixture.
4. **Chain disequilibrium.** A young volcanic rock can have $^{230}$Th out of
   equilibrium with $^{238}$U, and an age computed on the equilibrium
   assumption is then wrong by tens of per cent. U-series dating *models* the
   disequilibrium instead.
5. **A non-constant initial reservoir.** For $^{14}$C the assumption concerns
   the atmosphere, not the rock, and it is measurably false; the calibration
   curve is the acknowledgement.

The regime limits that make a system the wrong tool are the obvious pair —
**too young** relative to the half-life, so the daughter ratio is unmeasurable
(Rb–Sr cannot date a 10 ka basalt), and **too old** for the method, so the signal
falls below blank and contamination ($^{14}$C beyond about 50 ka) — plus the
chemical one: a host mineral that does not retain the daughter cannot record an
age in it at all.

## 7. Units and dimensional analysis

The unit discipline for this subject is short and every part of it is testable.

| Quantity | Unit | Check |
|---|---|---|
| Decay constant $\lambda$ | s⁻¹ or a⁻¹ | $\lambda T_{1/2} = \ln 2$, dimensionless |
| Mean life $\tau$ | same as $T_{1/2}$ | $\tau = 1.4427\,T_{1/2}$, always longer |
| Activity $A$ | Bq = s⁻¹; 1 Ci = $3.7\times10^{10}$ Bq exactly | $A = \lambda N$ |
| Specific activity | Bq kg⁻¹ or Bq g⁻¹ | $\lambda N_A/M$ for a pure nuclide |
| Concentration ratios $P/S$, $D/S$ | dimensionless | Molar or mass ratios, consistently |
| Isochron slope | dimensionless | $e^{\lambda t} - 1$ |
| Age | a, ka, Ma, Ga | Only as a *duration*; a "Ma" is $10^6$ a |

Three checks that catch most errors.

**Compute the specific activity and compare with a known conversion.** For
1 ppm of uranium in secular equilibrium, $N = w N_A/M$ with $w = 10^{-6}$ gives
$2.5116 \times 10^{18}$ atoms per kg, and
$\lambda(^{238}\mathrm{U}) = 4.915\,960 \times 10^{-18}$ s⁻¹ gives
**12.3472 Bq per kg**. The number quoted throughout the gamma-ray survey
literature is 12.4 Bq/kg per ppm U; the demo computes 4.0573 for Th against a
quoted 4.1, and 317.17 for K against a quoted 313 Bq/kg per % K. The 1 to
2 per cent differences are entirely in the tabulated half-lives and abundances,
and they are why a conversion factor copied from a paper must be recomputed from
the compilation that paper used.

**Check the natural-uranium activity ratio.** Natural uranium is 99.2745 %
$^{238}$U and 0.7200 % $^{235}$U by atom, but the *activity* ratio is
$\lambda_{235}N_{235}/\lambda_{238}N_{238}$, computed by the demo as 0.046042 —
1/21.72. Computing it avoids two wrong statements: that the activity ratio is
the abundance ratio (1/137.9), and that it is unity.

**Dimensional check on the age equation.** An isochron slope is a ratio of two
concentration ratios and is dimensionless; $e^{\lambda t}$ is dimensionless only
if $\lambda t$ is, so $\lambda$ and $t$ must share a unit of time. Mixing
$\lambda$ in s⁻¹ with $t$ in years is a factor of $3.155\,76 \times 10^7$; a
$\lambda$ in a⁻¹ with $t$ in Ma is a factor of $10^6$, and it looks like a very
young rock.

## 8. Python demonstration

[`code/radioactive_decay_demo.py`](./code/radioactive_decay_demo.py) is the
module's numerical-verification script. It converts tabulated half-lives to
decay constants, integrates the decay law with Euler and RK4 and compares both
with the closed form, locates the half-life by bisection, computes specific
activities, verifies the Bateman solution and secular equilibrium, fits an
isochron, contrasts the two radiocarbon half-lives, and solves the Dodson
equation. Every tabulated input is labelled TABULATED in the output.

The verification of the decay law:

```text
    step (s)   steps     Euler err   order       RK4 err   order
  3.9384e+14     200    1.2038e-03   1.003    6.7052e-12   4.008
  9.8460e+13     800    3.0045e-04   1.001    2.5702e-14   4.024
  2.4615e+13    3200    7.5081e-05    1.000    4.9960e-16   1.918

  Analytic N(2 T1/2)/N0 = exp(-2 ln2) = 0.250000000000000 = 1/4 exactly.
  |analytic - 0.25| = 0.000e+00 (round-off only).
```

The first-order column converging on 1.000 and the fourth-order column on 4.0
are the evidence that both integrators are correct. The collapse of the last RK4
order to 1.9 is the round-off floor of double precision: reporting an order from
that row would be reporting numerical noise. The analytic value being exactly
0.25 is the second verification — the numerical solutions converge to the closed
form and not to something else.

Half-life to decay constant, and the unit check:

```text
nuclide                          T1/2 (a)    lambda (1/s)  lambda (1/a)  mean life (a)
C-14  (Libby, conventional)          5568    3.944775e-12  1.244876e-04           8033
C-14  (Cambridge)                    5730    3.833248e-12  1.209681e-04           8267
K-40                            1.248e+09    1.759977e-17  5.554064e-10        1.8e+09
Rb-87                            4.88e+10    4.500924e-19  1.420384e-11       7.04e+10
U-238                           4.468e+09    4.915960e-18  1.551359e-10      6.446e+09
Th-232                          1.405e+10    1.563310e-18  4.933432e-11      2.027e+10
Cs-137                              30.08    7.302031e-10  2.304346e-02           43.4
Rn-222 (days)                   0.0104682    2.098218e-06  6.621473e+01         0.0151
```

Note the Rb–Sr row: $1.420\,384 \times 10^{-11}$ a⁻¹ is the IUGS-recommended
value, and any Rb–Sr age computed with a different $\lambda$ is a different age.
Note also that the mean life column is always 1.4427 times the half-life, which
is the dimensional self-check.

The chain and the equilibrium:

```text
   t (d)         A(238U)        A(234Th)    ratio Th/U
     1.0 4.915959876e-18 1.393754495e-19      0.028352
   100.0 4.915959876e-18 4.638933442e-18      0.943648
   365.0 4.915959875e-18 4.915824219e-18      0.999972
```

with the residual analysed as $2^{-15.15} = 2.760 \times 10^{-5}$ against a
measured $2.760 \times 10^{-5}$. The agreement of an analytic estimate with a
numerical integration to three significant figures is the check that the code
and the equation are the same object.

The roots located by bisection are *exactly* the tabulated half-lives, with a
residual of 0.0 at double precision: all the uncertainty in a decay constant is
in the tabulated half-life and none of it is in the arithmetic. The
specific-activity conversions differ from the widely quoted survey factors by
1 to 2 per cent, entirely because of the tabulated half-life and abundance
chosen — not a bug to be fixed but the point. And the isochron recovers the true
age to 0.37 per cent while the two model ages are wrong by 29 and 46 per cent:
the *method* is the difference.

## 9. Common mistakes

1. **Calling a model age an age.** If the intercept was assumed rather than
   fitted, say so and state the assumed value; a reader cannot evaluate the
   number without it.
2. **Quoting a half-life without its compilation.** The Rb–Sr half-life changed
   by 2 per cent in 1977 and every age published before that changed with it.
3. **Mixing units of time inside the age equation.** $\lambda$ and $t$ must
   share a unit — the easiest error to make with $\lambda$ in a⁻¹ and $t$ in Ma,
   and it produces a plausible-looking age that is wrong by $10^6$.
4. **Running an isochron on non-cogenetic samples.** A line through samples of
   different ages or initial ratios is a mixing line, and its slope is not an
   age. A "good" isochron from a bad dataset is a well-known failure mode.
5. **Forgetting that K–Ar and Ar–Ar date cooling.** The Ar–Ar age is the time
   since the mineral passed its closure temperature, and calling it the
   crystallisation age is wrong unless the rock cooled instantly.
6. **Treating a conventional radiocarbon age as a calendar age.** It is not, and
   the difference is usually centuries. Name the calibration curve and version.
7. **Assuming secular equilibrium.** Radon loss, young-sample disequilibrium and
   industrial processing all break it; measure more than one chain member if the
   conclusion depends on it.
8. **Reporting an age with too many digits.** A "$^{14}$C age of 19 034.6
   years" is false precision: the model and the measurement carry hundreds of
   years of uncertainty between them.
9. **Comparing two chronometers without the closure temperatures.** Two ages
   from one rock are evidence of a cooling history until proven otherwise.
10. **Computing $\tau = T_{1/2}\ln 2$.** The mean life is $T_{1/2}/\ln 2$,
    larger by 1.4427; the wrong factor is 2.08, not 1.

## 10. Real-world applications

- **Geological time scales.** Every boundary in the Phanerozoic and Precambrian
  time scale is pinned by U–Pb zircon ages, with Rb–Sr, Sm–Nd, Ar–Ar and
  Re–Os as cross-checks ([04-03-03](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/03-radiometric-dating.md)).
- **Thermochronology and exhumation.** The closure-temperature sequence *is*
  the measurement: K–Ar, Ar–Ar, fission-track and (U–Th)/He ages are inverted
  through a thermal model into a cooling and exhumation history.
- **Gamma-ray spectrometry.** Chain equilibrium is the assumption that converts
  a measured activity into an element concentration ([04](./04-gamma-spectrometry.md)).
- **Uranium-series disequilibrium.** In young carbonates and speleothems the
  disequilibrium is the clock, so dating them means modelling transport as well
  as decay.
- **Archaeology and palaeoclimate.** Radiocarbon with its calibration curve is
  the workhorse; the Suess effect, the bomb spike and the marine reservoir
  offset are facts about the reservoir, not the decay law.
- **Nuclear waste and environmental tracing.** The same decay constants set
  activity inventories, daughter ingrowth and repository heat generation
  ([06](./06-dosimetry.md)), and the same arithmetic gives the crustal
  radiogenic heat production that drives every lithospheric thermal model
  ([02-05-06](../05-thermodynamics/06-geotherms.md)).

## 11. Further reading

- **Steiger, R. H., & Jäger, E. (1977). Subcommission on geochronology:
  convention on the use of decay constants in geo- and cosmochronology.
  *Earth and Planetary Science Letters* 36, 359–362.** The paper that fixed the
  Rb–Sr convention, and a lesson in why conventions matter. Level: intermediate.
- **Dickin, A. P. *Radiogenic Isotope Geology* (Cambridge University Press).**
  The standard modern textbook: isochrons, concordia, closure temperature and
  the failure modes of each system, with worked data. Level: advanced.
- **Faure, G. *Principles of Isotope Geology* (Wiley).** Complementary account,
  stronger on classical systems and analytical chemistry. Level: intermediate.
- **Dodson, M. H. (1973). Closure temperature in cooling geochronological and
  petrological systems. *Contributions to Mineralogy and Petrology* 40,
  259–274.** The origin of equation (13). Level: graduate.
- **NNDC, *ENSDF/NuDat* evaluated nuclear structure data.** The source for
  half-lives, branching ratios and decay energies; confirm the current
  evaluation and its date, since the values are revised. Level: reference.
- **IUPAC, *Isotopic Compositions of the Elements* (current report).** The
  source for the abundances used in every element-to-activity conversion.
  Level: reference.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [01 Atomic Structure and Energy Levels](./01-atomic-structure.md) — the atomic
  half of a decay, and the X-rays that accompany it.
- [03 Interaction of Radiation with Matter](./03-radiation-interaction.md) — what
  the emitted alpha, beta and gamma particles then do.
- [04 Gamma-Ray Spectrometry and Natural Radioelements](./04-gamma-spectrometry.md)
  — how a chain activity is measured, and the equilibrium assumption in use.
- [06 Dosimetry, Radiation Safety and Regulatory Limits](./06-dosimetry.md) — the
  activity-to-dose half of the same physics.
- [01-08-01 First-Order ODEs: Separation of Variables and Integrating Factors](../../01-mathematics/08-ordinary-differential-equations/01-first-order-odes.md)
  — the mathematics of §1 and §2 in general form.
- [04-03-03 Radiometric Dating Methods and Their Assumptions](../../04-earth-science-geology/03-geologic-time-and-stratigraphy/03-radiometric-dating.md)
  — the geological use of these systems, with the stratigraphic context.
- [26-02-03 Physical Constants and Earth Parameters with Sources](../../26-reference-library/02-symbols-and-units/03-constant-handbook.md)
  — the exact/measured/nominal discipline that §1 imposes on half-lives.

Exercises:
[`exercises/02-radioactive-decay-exercises.md`](./exercises/02-radioactive-decay-exercises.md)
and
[`exercises/02-radioactive-decay-solutions.md`](./exercises/02-radioactive-decay-solutions.md).

## Self-assessment checklist

- [ ] I can derive $N = N_0e^{-\lambda t}$ from a constant decay probability,
      and derive $T_{1/2}$ and $\tau$ from it. (§1)
- [ ] I can convert a half-life into a decay constant in s⁻¹ and a⁻¹ and check
      the unit algebra. (§1, §7)
- [ ] I can state which compilation a half-life came from and why the
      provenance is part of the number. (§1)
- [ ] I can derive the Bateman solution for two members and state the secular
      and transient equilibrium conditions. (§2)
- [ ] I can explain why one gamma line reports a whole chain, and what breaks
      that. (§2)
- [ ] I can derive the isochron equation from the decay law and invert a slope
      into an age. (§3)
- [ ] I can distinguish an age from a model age and say which assumptions each
      requires. (§3)
- [ ] I can explain the concordia and why U–Pb has an internal test. (§4)
- [ ] I can explain closure temperature and why slower cooling lowers it. (§5)
- [ ] I can list the five failure modes of a dating system and the diagnostic
      for each. (§6)
- [ ] I can state the difference between a conventional and a calibrated
      radiocarbon age, and why the two half-lives exist. (§4, §7)
- [ ] I can compute a specific activity and compare it with a published
      conversion factor. (§7)
