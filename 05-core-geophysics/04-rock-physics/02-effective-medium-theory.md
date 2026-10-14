---
id: 05-04-02
title: "Effective-Medium Theories (Voigt, Reuss, Hashin-Shtrikman)"
level: graduate
prereqs: ["05-04-01"]
tags: [voigt, reuss, hashin-shtrikman, bounds, effective-medium]
---

# Effective-Medium Theories (Voigt, Reuss, Hashin-Shtrikman)

## Learning objectives

1. **Derive** the Voigt (arithmetic) and Reuss (harmonic) averages from the
   isostrain and isostress assumptions.
2. **State** the Hashin-Shtrikman bounds and explain why they are tighter than
   Voigt/Reuss without knowing the geometry.
3. **Identify** the degenerate case where the lower bounds collapse to zero, and
   explain what that means physically.
4. **Verify** the algebra of the averages by an independent numerical
   experiment.
5. **Explain** why a bound is not a prediction, and how to decide which bound a
   real rock obeys.

## Prerequisites

- [05-04-01 Porosity, Density and Velocity](./01-porosity-density-velocity.md)
- [02-04-03 Constitutive Laws and Generalised Hooke's Law](../../02-physics/04-elasticity-and-continuum-mechanics/03-constitutive-laws.md)

## 1. Intuition

A mixture's modulus is not a single number. The volume fractions and the
constituent moduli bracket it; the geometry within the bracket; and no
measurement of volume fraction alone can tell you where in the bracket the rock
sits. Bounds are the honest answer to "what can we say without knowing the pore
geometry?"

## 2. Definitions

**Voigt (isostrain) average.** All constituents carry the same strain; the
effective modulus is the arithmetic mean weighted by volume fraction:

$$K_V = (1-\phi)K_s + \phi K_f, \qquad G_V = (1-\phi)G_s + \phi G_f.$$

**Reuss (isostress) average.** All constituents carry the same stress; the
effective compliance is the arithmetic mean, so the modulus is the harmonic
mean:

$$\frac{1}{K_R} = \frac{1-\phi}{K_s} + \frac{\phi}{K_f}, \qquad
\frac{1}{G_R} = \frac{1-\phi}{G_s} + \frac{\phi}{G_f}.$$

**Hill average.** $\frac12(K_V+K_R)$, an empirical midpoint widely used as a
convenient estimate.

**Hashin-Shtrikman bounds.** The tightest bounds that depend only on volume
fractions and isotropy, for a two-phase mixture with one phase as the host:

$$K_\pm = K_1 + \frac{f_2}{\frac{1}{K_2-K_1} + \frac{f_1\cdot3}{3K_1+4G_1}},$$

$$G_\pm = G_1 + \frac{f_2}{\frac{1}{G_2-G_1} + f_1\dfrac{2(K_1+2G_1)}
{5G_1\left(K_1+\frac43G_1\right)}},$$

where phase 1 is the host. Using the stiffer phase as host gives the upper
bounds; the weaker phase as host gives the lower bounds.

## 3. Derivations

### 3.1 Voigt from a parallel spring bank

$n$ springs of stiffness $k_i = E_iA_i/L$ sharing a common displacement
$\delta$: total force $= \delta\sum k_i$, effective stiffness
$\sum E_iA_i/\sum A_i$ = arithmetic mean weighted by area fraction. This *is*
the isostrain condition.

### 3.2 Reuss from a series chain

The same elements in series carry a common force: total elongation
$F\sum L_i/(E_iA_i)$, effective modulus $= $ harmonic mean. This is the
isostress condition.

### 3.3 The degenerate fluid case

Set $G_f = 0$ (a fluid cannot sustain static shear). Then $G_R = 0$ for any
$\phi>0$, and the Hashin-Shtrikman lower shear bound, whose formula is singular
for a host with $G = 0$, also has limit $0$. **Both lower bounds are identically
zero, for every porosity.** They carry no information. Only the HS-upper bound
constrains the shear modulus of a fluid-saturated rock.

More striking: with $G_f = 0$ the HS *lower bulk* bound collapses exactly onto
the Reuss bound. This is an identity, verifiable by substituting $G_f = 0$ into
the HS formula, and the demonstration confirms it numerically: $K_R$ and
$K_{HS-}$ agree to a relative $0.00\times10^{0}$ at $\phi = 0.20$ for a stated
synthetic pair $K_s = 37$ GPa, $G_s = 44$ GPa, $K_f = 2.2$ GPa.

### 3.4 Voigt and Reuss as energy bounds, derived

Section 3.1 built Voigt from a spring bank and Reuss from a spring chain. That
derivation shows the two are *attainable*; it does not show they bound every
geometry. The variational argument does.

**Voigt from minimum potential energy.** Let the mixture be subjected to a
uniform strain field equal to the average strain $\bar\varepsilon$. That is an
*admissible* strain field, so the strain energy it stores is greater than or
equal to the true minimum energy for the given boundary conditions. Therefore

$$W \le \tfrac12 K_V\bar\varepsilon^2
\qquad\Longrightarrow\qquad K \le K_V,$$

because a stiffer material stores more energy at the same strain. **Voigt is an
upper bound for every geometry**, not just the parallel one.

**Reuss from minimum complementary energy.** Now apply a uniform stress equal to
the average stress $\bar\sigma$. That is an admissible stress field, so

$$W_c \le \tfrac12 \frac{\bar\sigma^2}{K_R}
\qquad\Longrightarrow\qquad K \ge K_R,$$

because a softer material stores less complementary energy at the same stress.
**Reuss is a lower bound for every geometry.**

Together:

$$\boxed{\;K_R \le K \le K_V\;}$$

with equality only for the two degenerate geometries. The same argument applies
to $G$ term by term. **Physical interpretation:** the bounds are not empirical
limits but consequences of the two admissible-field inequalities, which is why
they cannot be violated by any arrangement of the constituents — only by wrong
inputs or by anisotropy, which breaks the isotropy the derivation assumes.

**A one-dimensional instance, checkable by hand.** For two springs in parallel,
$K = (1-\phi)K_1+\phi K_2 = K_V$ exactly; in series,
$1/K = (1-\phi)/K_1 + \phi/K_2$, giving $K = K_R$ exactly. The demonstration
reproduces both from assembled linear systems, to $1.33\times10^{-14}$ and
$0.00\times10^{0}$ respectively.

### 3.5 The Hashin–Shtrikman bounds, and why they are tighter

Voigt and Reuss correspond to two extreme geometries. Hashin and Shtrikman asked
a sharper question: among **all** geometries with given volume fractions and
isotropy, what is the maximum and minimum possible modulus? Their answer is the
coated-sphere assemblage — a sphere of phase 2 surrounded by a shell of phase 1
(and vice versa), packed to fill space — and the resulting bounds are attainable,
hence optimal *given only volume fractions*.

$$K_\pm = K_1 + \frac{f_2}{\dfrac{1}{K_2-K_1}
+ \dfrac{3f_1}{3K_1+4G_1}},$$

with $G_\pm$ following the analogous expression quoted in Section 2. Because the
extremising geometry is a specific composite, the bounds lie strictly inside the
Voigt–Reuss bracket except in the two limiting cases.

**Why the geometry can be extremised without knowing the geometry.** The
variational problem is solved by choosing a polarisation field; the optimal
choice is uniform for an ellipsoidal inclusion, and the coated sphere is the
geometry that saturates it. **That is the deep reason the HS bound exists and is
tight, and it is also its limitation: the bound is optimal for isotropic
two-phase mixtures of arbitrary geometry, so any information about the actual
geometry narrows the answer further — but the bound itself will never narrow.**

### 3.6 The identity $K_{HS-} = K_R$ when the fluid has no shear stiffness, derived

This identity is worth deriving because it explains the degenerate shear result
and because it is a check on any HS implementation.

Put $G_f = 0$ (a fluid) and use the fluid as the host in the HS bulk expression,
so $K_1 = K_f$, $G_1 = 0$, $f_1 = \phi$ (the host fraction) and
$f_2 = 1-\phi$:

$$K_{HS-} = K_f + \frac{1-\phi}{\dfrac{1}{K_s-K_f}
+ \dfrac{3\phi}{3K_f+0}}
= K_f + \frac{1-\phi}{\dfrac{1}{K_s-K_f} + \dfrac{\phi}{K_f}} .$$

Combine the denominator over a common factor:

$$\frac{1}{K_s-K_f} + \frac{\phi}{K_f}
= \frac{K_f + \phi\left(K_s-K_f\right)}{K_f\left(K_s-K_f\right)}
= \frac{(1-\phi)K_f + \phi K_s}{K_f\left(K_s-K_f\right)} .$$

Substituting and simplifying,

$$K_{HS-} = K_f + \frac{(1-\phi)K_f\left(K_s-K_f\right)}{(1-\phi)K_f+\phi K_s}
= \frac{K_fK_s}{(1-\phi)K_f+\phi K_s},$$

and the Reuss bound is

$$K_R = \frac{1}{\dfrac{1-\phi}{K_s}+\dfrac{\phi}{K_f}}
= \frac{K_fK_s}{(1-\phi)K_f+\phi K_s} .$$

**Identical.** So for any fluid-saturated rock the HS lower *bulk* bound carries
exactly the same information as the Reuss bound, and the demonstration confirms
it numerically ($8.886462882$ GPa both ways, relative difference
$0.00\times10^{0}$). The genuinely new information in HS is in the *upper* bulk
bound and the *upper* shear bound; the lower bounds are, for this case, Reuss
restated.

### 3.7 How the bracket width depends on the constituent contrast

The bounds are not equally informative for all mixtures, and the reason is
structural: **the bracket width vanishes as the two phases become identical.**

Measured with the stated synthetic solid ($K_s = 37$ GPa, $G_s = 44$ GPa) at
$\phi = 0.20$, varying only the fluid modulus:

| $K_f$ (GPa) | HS bracket (GPa) | width (GPa) | width / lower bound |
|---|---|---|---|
| 2.2 | $[8.8865,\,27.1832]$ | 18.2967 | 2.06 |
| 10 | $[24.0260,\,30.0252]$ | 5.9992 | 0.25 |
| 20 | $[31.6239,\,33.0366]$ | 1.4126 | 0.045 |
| 35 | $[36.5819,\,36.5932]$ | 0.0113 | $3.1\times10^{-4}$ |

**The width collapses as $K_f \to K_s$.** At $K_f = 35$ GPa the bracket is 0.0113
GPa — narrower than any laboratory measurement uncertainty — and the mixture is
effectively determined by the volume fractions alone. Conversely, at
$K_f = 2.2$ GPa a brine-like fluid the bracket is 2.06 times the lower bound, and
the answer is almost entirely unconstrained by the volume fractions.

**Physical interpretation.** A bound does work only when it separates the
possibilities. When the constituents are similar, every geometry gives nearly the
same modulus, and the bounds coincide — which is why bounds are informative for
porous rock (fluid versus solid, hugely different) and nearly useless for a
quartz–feldspar mixture (very similar). **State the bracket width alongside the
bounds**, because a bound that spans a factor of 2 is a different kind of result
from one that spans 0.1%.

## 4. Units and dimensional analysis

| Quantity | Unit |
|---|---|
| $K, G$ | Pa |
| $\phi$, $f_i$ | dimensionless |
| $K_V, K_R, K_\pm$ | Pa |

A useful check: at $\phi = 0$ and $\phi = 1$ every average must return the single
remaining phase. The demonstration confirms this for both ends.

## 5. Assumptions

1. **Isotropy** of the mixture and of each constituent.
2. **Perfect bonding** between phases; no slip.
3. **Linear elasticity.**
4. **Known constituent moduli.** These are themselves uncertain, often more so
   than the volume fractions.
5. **No pore-shape information.** This is the assumption that *creates* the
   width of the bracket; if you know the geometry (spheres, cracks, tubes), you
   can do better with a specific inclusion model, at the cost of new
   assumptions.

## 6. Worked examples (measured)

Stated SYNTHETIC inputs: $K_s = 37$ GPa, $G_s = 44$ GPa, $K_f = 2.2$ GPa,
$G_f = 0$, $\phi = 0.20$.

| estimate | $K$ (GPa) | $G$ (GPa) |
|---|---|---|
| Voigt (upper) | 30.0400 | 35.2000 |
| Hill average | 19.4632 | 17.6000 |
| Reuss (lower) | 8.8865 | 0.0000 |
| HS upper | 27.1832 | 28.8766 |
| HS lower | 8.8865 | 0.0000 |

Ordering checks all hold: $K_{HS-} \le K_{HS+} \le K_V$, and
$K_R = K_{HS-}$ to a relative $0.00\times10^{0}$. The HS bracket for bulk
modulus, 8.89 to 27.18 GPa, is more than twice as narrow as the Voigt–Reuss
bracket, 8.89 to 30.04 GPa — and it required no more information.

**Degenerate shear bounds by porosity** ($G_R$ and $G_{HS-}$ both exactly 0):

| $\phi$ | $G_R$ (GPa) | $G_{HS-}$ (GPa) | $G_{HS+}$ (GPa) |
|---|---|---|---|
| 0.05 | 0.000000 | 0.000000 | 39.630450 |
| 0.20 | 0.000000 | 0.000000 | 28.876647 |
| 0.40 | 0.000000 | 0.000000 | 18.359391 |

**Independent verification.** Assembling the same 200 elements as (a) a series
bar and (b) a bank of parallel springs, and solving the resulting linear
systems, reproduces the harmonic mean to a relative $1.33\times10^{-14}$ and
the arithmetic mean to $0.00\times10^{0}$. This confirms the *algebra* of the
averages via a different code path. It does **not** tell you which average a
rock obeys — that is a physical question about pore geometry.

### 6.1 Extended worked example: how much is the geometry worth?

Suppose only the volume fractions and the constituent moduli are known. The
question this lesson answers is: what is the largest error you would make by
reporting a single number?

Using the stated SYNTHETIC case ($K_s = 37$ GPa, $G_s = 44$ GPa,
$K_f = 2.2$ GPa, $G_f = 0$, $\phi = 0.20$), the bulk-modulus bracket widths are:

| bracket | low (GPa) | high (GPa) | width (GPa) | width/midpoint |
|---|---|---|---|---|
| Voigt–Reuss | 8.8865 | 30.0400 | 21.1535 | 0.108 |
| Hashin–Shtrikman | 8.8865 | 27.1832 | 18.2967 | 0.101 |

Reporting the midpoint of the HS bracket as "the" bulk modulus
(18.035 GPa) is wrong by up to $\pm9.1$ GPa, i.e. $\pm50\%$ of the midpoint, for
*any* geometry consistent with the inputs. The corresponding $V_p$ bracket, using
the *matched* pairs $(K_\text{HS-},G_\text{HS-}) = (8.8865, 0)$ GPa and
$(K_\text{HS+},G_\text{HS+}) = (27.1832, 28.8766)$ GPa with
$\rho = 2320$ kg/m³, is

$$V_p^{\text{low}} = \sqrt{\frac{8.8865\times10^9}{2320}} = 1957\ \mathrm{m\,s^{-1}},
\qquad
V_p^{\text{high}} = \sqrt{\frac{(27.1832+38.5021)\times10^9}{2320}}
= 5321\ \mathrm{m\,s^{-1}}.$$

That is a **2.7:1 velocity bracket from volume fractions alone** — and note the
discipline required to state it correctly: the bound pair must be matched
(use $G_\text{HS-}$ with $K_\text{HS-}$, not the upper shear bound), because
mixing terms from different bounds produces a combination that no geometry
attains.

**Now add one piece of information.** If a measurement establishes
$K_\text{sat} = 24$ GPa, the model space collapses: any geometry giving 24 GPa
is admissible, and the *reportable* statement becomes
"$K = 24$ GPa measured; the admissible geometric range consistent with this
value is narrower." This is the honest use of bounds — not as a prediction, but
as a *consistency test* and as a way to say how much information a measurement
has added.

**Why the shear bound is the more dramatic case.** As Section 6 shows, both
lower shear bounds are exactly zero for every porosity. The upper bound at
$\phi = 0.20$ is 28.877 GPa. So knowing only the volume fractions and the
constituent moduli, the shear modulus of the rock lies in $[0, 28.877]$ GPa — a
*complete* lack of information at the lower end, from a calculation that took
four numbers. The HS-upper bound is the only useful statement, and it is the one
practice should quote.

**Connecting to the assembly verification.** The independent assembly check
(series bar versus parallel spring bank) recovered the harmonic and arithmetic
means to $1.3\times10^{-14}$ and exactly 0. It confirmed the *algebra*. It did
not and cannot choose between them, because both are attained by real geometries
— a stack of layers in series, or a set of columns in parallel. Real rocks are
neither, which is exactly why the HS bounds, not the averages, are the
defensible statement.

### 6.2 Worked arithmetic: what a measured saturated modulus tells you about the frame

Section 3.5's bracket can be used in reverse, and that is its most practical
application. Suppose a laboratory measurement gives $K_\text{sat} = 24$ GPa on a
brine-saturated sample with $\phi = 0.20$, and the constituent moduli are the
stated synthetic set ($K_s = 37$, $G_s = 44$, $K_f = 2.2$ GPa, $G_f = 0$).

The HS bracket for the *saturated* mixture is $[8.8865,\,27.1832]$ GPa, so
24 GPa is admissible — the measurement passes the consistency test.

Now ask what frame moduli are compatible. Inverting Gassmann
([05-04-03](./03-gassmann-fluid-substitution.md)) gives $K_\text{dry} =
22.376$ GPa, and the requirement $K_\text{dry} \le K_s = 37$ GPa is
satisfied, as is $K_\text{dry} \ge K_R = 8.8865$ GPa. The point is
not the number but the *procedure*: **the bounds convert a modulus measurement
into an admissibility test on the derived frame**, and a failure of that test
means one of the inputs ($\phi$, $K_s$, $K_f$) is wrong, or the rock is
anisotropic, or the measurement is at a frequency where the relaxed-fluid
assumption fails.

**Quantified sensitivity.** Because the HS bracket is 18.3 GPa wide
(Section 6), a measurement of 24 GPa pins the mixture to about two thirds of the
admissible range — a genuine constraint but not a determination. Compare with the
Voigt–Reuss bracket, 21.2 GPa wide: the HS test is 14% tighter and costs nothing
extra.

### 6.3 A shortcut that fails: reporting the Hill average

**The shortcut.** Report $K_\text{Hill} = \tfrac12(K_V+K_R)$ as "the" mixture
modulus.

**Why it fails.** The Hill average is an *empirical midpoint* with no variational
standing. It is not attainable by any particular geometry except in the two
degenerate limits, and it is not a bound: a real rock may lie above or below it.
Worse, it looks precise — a single number — while carrying none of the
information about where the mixture actually lies between the bounds.

**Quantified.** From the measured table ($\phi = 0.20$): $K_V = 30.0400$,
$K_R = 8.8865$, so $K_\text{Hill} = 19.4632$ GPa. The admissible HS range is
$[8.8865, 27.1832]$, which contains the Hill value but is not narrowed by it. An
interpreter who reports 19.46 GPa implies a precision the inputs do not support:
**any value in an 18.3 GPa-wide interval is equally consistent with the volume
fractions.**

**What to report instead.** The bounds themselves, as an interval; and if a
specific value is needed, the *model* that produced it (a coated-sphere
assemblage, a crack-density model, a layered sequence) together with its
assumptions. "The modulus is between $x$ and $y$, and the model giving the
midpoint is $z$" is a defensible sentence. "The modulus is 19.46 GPa" is not.

## 7. Python demonstration

Run `code/bounds_demo.py`. It computes the table, the ordering checks, the
endpoint limits, the degenerate shear bounds and the independent assembly
verification. Break it by swapping the host/guest order in `hs_bounds` and
confirm that the ordering checks fail — a test that can fail is the only useful
one.

## 8. Exercises, mistakes, applications

Exercises: [`exercises/02-effective-medium-theory-exercises.md`](./exercises/02-effective-medium-theory-exercises.md).

**Common mistakes.** (1) Reporting "the Reuss shear modulus" of a saturated rock
— that is zero, always. (2) Treating Voigt as a prediction rather than a bound.
(3) Applying the averages to a mixture with strong anisotropy. (4) Forgetting
that constituent moduli are uncertain. (5) Using the Hill average outside the
porosity range in which it was calibrated.

**Applications.** Bounding moduli where only volume fractions are known;
sanity-checking laboratory measurements (a measurement outside the bounds means
the inputs or the sample are wrong); constructing starting models for
fluid-substitution studies; verifying that a computed mixture property is at
least admissible.

## 9. Further reading

- **Mavko, Mukerji & Dvorkin, *The Rock Physics Handbook*.** Chapter 4. Level:
  graduate. The HS formulas in the form used above.
- **Hashin, Z. & Shtrikman, S. (1963).** A variational approach to the theory of
  the elastic behaviour of multiphase materials. *J. Mech. Phys. Solids* 11,
  127–140. Level: graduate.
- **Watt, J. P., Davies, G. F. & O'Connell, R. J. (1976).** The elastic
  properties of composite materials. *Rev. Geophys.* 14, 541–563. Level:
  graduate. A critical comparison of the averaging schemes.

## 10. Related lessons

- [05-04-03 Gassmann Fluid Substitution](./03-gassmann-fluid-substitution.md)
- [05-04-05 Anisotropy in Rocks](./05-anisotropy-rock.md)
- [02-04-06 Anisotropic Elasticity](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)

## Self-assessment checklist

- [ ] I can derive the Voigt and Reuss averages from isostrain and isostress.
- [ ] I can state the HS formulas and explain why they are tighter.
- [ ] I can demonstrate that the fluid shear lower bounds are zero.
- [ ] I can verify an average numerically with an independent assembly.
- [ ] I can state why a bound is not a prediction.
