---
id: 11-02-02
title: "Magnetics for IOCG, Porphyry and Magmatic Sulphides"
level: graduate
prereqs: ["08-03-02", "08-03-05", "11-02-01"]
tags: [exploration-geophysics, mineral-exploration, magnetics, remanence, reduction-to-pole, depth-estimation]
---

# Magnetics for IOCG, Porphyry and Magmatic Sulphides

Magnetics is the cheapest and most widely flown exploration method, and its
interpretation rests on a single awkward fact: **the anomaly shape is controlled by
the direction of the total magnetisation, not by the direction of the ambient
field.** Since remanence can be larger than the induced magnetisation and point
anywhere, the direction is an unknown that the method needs as an input. This
lesson derives the anomaly of a magnetised body, quantifies the Koenigsberger
ratio, computes reduction to the pole (RTP) and shows what RTP cannot fix, derives
the half-width depth rule and measures its bias from a wrong assumed direction,
and computes self-demagnetisation, which makes the linear
$\Delta B \propto \kappa$ relation fail by a factor at high susceptibility.

**All models and data in this module are SYNTHETIC.** Susceptibilities,
Koenigsberger ratios, magnetisation directions, geometry and noise are chosen
teaching values, not measurements or properties of any real deposit.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the field of a magnetic dipole and the total-field anomaly it
   produces, and **compute** a profile for a given magnetisation vector.
2. **Compute** the induced and remanent magnetisation of a body from
   $\kappa$, $Q$ and their directions, and **explain** why the vector sum, not
   the field direction, shapes the anomaly.
3. **Measure** how remanence moves the anomaly peak and changes the
   peak-to-trough ratio, and **state** why this cannot be filtered out.
4. **Explain** reduction to the pole as a re-synthesis with a vertical
   magnetisation, and **quantify** the residual when the assumed direction is
   wrong.
5. **Derive** the half-width-to-depth ratio for a vertically magnetised dipole
   from the analytic profile, and **measure** the depth bias from ignoring
   remanence.
6. **Compute** the self-demagnetised magnetisation
   $M = \kappa H/(1+N\kappa)$ and **quantify** the factor by which the linear
   formula over-predicts the anomaly.
7. **State** the exact scale-invariance of the dipole anomaly and what it implies
   for the (volume, depth, magnetisation) ambiguity.

## Prerequisites

- [08-03-02 Koenigsberger Ratio and Remanence](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/02-koenigsberger-and-remanence.md)
  — induced versus remanent magnetisation.
- [08-03-05 Magnetic Depth Estimation](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/05-magnetic-depth-estimation.md)
  — the general family of shape-based depth rules.
- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — where the magnetic contrast sits in the deposit-class table.

## 1. The field of a dipole, and the total-field anomaly

A magnetised body far from the observer is a dipole. Write the magnetisation as
$\mathbf{M}$ (A m⁻¹), so that a body of volume $V$ has moment
$\mathbf{m} = \mathbf{M}V$ (A m²). The field of a dipole at a source
$\mathbf{s}$, evaluated at observation points $\mathbf{r}$, is

$$\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4\pi}
\left[\frac{3(\mathbf{m}\cdot\hat{\mathbf{R}})\hat{\mathbf{R}}
- \mathbf{m}}{R^{3}}\right], \qquad
\mathbf{R} = \mathbf{r} - \mathbf{s}, \quad R = |\mathbf{R}|,$$

with $\mu_0/4\pi = 10^{-7}\ \mathrm{H\,m^{-1}}$. A total-field magnetometer does
not measure $\mathbf{B}$ but its component along the ambient field, so

$$\Delta T = \mathbf{B}\cdot\hat{\mathbf{B}}_0 .$$

For the vertical component of a *vertically magnetised* dipole this reduces to the
closed form used for depth rules:

$$Z(x) = \frac{\mu_0 m}{4\pi}\,
\frac{2h^{2} - x^{2}}{\left(x^{2}+h^{2}\right)^{5/2}},$$

which is the shape whose half-width §5 converts into a depth.

*Numerical check of the dipole formula* (SYNTHETIC: sphere $R = 200\
\mathrm{m}$, $z = 300\ \mathrm{m}$, $\kappa = 0.20$ SI, $Q = 1.5$, remanence
inclination $-30°$, $B_0 = 50\ \mathrm{\mu T}$ at $60°$ inclination; volume
$V = 3.3510\times10^{7}\ \mathrm{m^3}$):

$$|\mathbf{m}_{\text{ind}}| = \frac{\kappa}{1+\kappa/3}H_0 V
= \frac{0.20}{1.0667}(39.789)(3.3510\times10^{7}) = 2.5000\times10^{8}\
\mathrm{A\,m^{2}},$$

and with $Q = 1.5$ the remanent moment is $3.7500\times10^{8}\ \mathrm{A\,m^{2}}$
at $-30°$. Their vector sum has magnitude $4.5069\times10^{8}\ \mathrm{A\,m^{2}}$
at an inclination of only $3.7°$ — **the total magnetisation is nearly horizontal
even though the field is inclined at $60°$.** That single number explains every
anomaly shape below.

The demonstration verifies the dipole formula against a voxel sum: a uniformly
magnetised sphere represented by $12\,712$ dipoles on a $30^{3}$ grid gives
$-639.24\ \mathrm{nT}$ where the dipole formula gives $-646.81\ \mathrm{nT}$, a
difference of $1.17\%$ from the voxel representation of the sphere's surface. The
sphere is exactly a dipole *outside* itself, so the agreement is expected; the
residual measures the discretisation, not a physical discrepancy.

## 2. Induced plus remanent magnetisation

The induced magnetisation is parallel to the field and proportional to it,
$M_i = \kappa H$; the remanent magnetisation is a permanent property of the rock
with its own direction. The **Koenigsberger ratio**

$$Q = \frac{|\mathbf{M}_r|}{|\mathbf{M}_i|}$$

measures which dominates. The total is a vector sum:

$$\mathbf{M}_{\text{tot}} = \mathbf{M}_i + \mathbf{M}_r
= \kappa H_0\,\hat{\mathbf{B}}_0 + Q\,\kappa H_0\,\hat{\mathbf{M}}_r ,$$

$$\tan(\text{direction of } \mathbf{M}_{\text{tot}})
\text{ depends on } \angle(\hat{\mathbf{B}}_0, \hat{\mathbf{M}}_r)\ \text{and } Q .$$

In the SYNTHETIC example, $Q = 1.5$ with the remanence at $-30°$ pulls the total
magnetisation from $60°$ to $3.7°$.

### The profiles, measured

| case | peak (nT) | trough (nT) | position of peak (m) | peak/trough |
|---|---|---|---|---|
| induced only ($Q=0$) | 1501.17 | −271.51 | −80 | 5.529 |
| remanent only | 370.13 | −1963.79 | −315 | 0.188 |
| mixed ($Q=1.5$) | 1216.61 | −1518.38 | −190 | 0.801 |

The body is at $x = 0$. Three facts follow, and they are the practical content of
this lesson:

1. **An induced anomaly is already asymmetric** in an inclined field (peak/trough
   $5.5$), so asymmetry alone does not indicate remanence.
2. **Remanence moves the peak** from $-80\ \mathrm{m}$ to $-190\ \mathrm{m}$ in the
   mixed case, and to $-315\ \mathrm{m}$ for remanence alone.
3. **Remanence reverses which sign dominates**: induced has a dominant positive
   peak, remanence-only has a dominant negative trough.

None of this can be removed by filtering, because none of it is noise: it is the
signal of a magnetisation direction the survey has not measured.

## 3. Reduction to the pole, and what it cannot do

**Reduction to the pole** transforms a measured total-field anomaly into the
anomaly that would be observed at the magnetic pole with a vertical magnetisation
— a symmetric positive anomaly centred on the body. Defined that way, RTP can be
*computed* by re-synthesising the dipole with
$\mathbf{m}_{\text{RTP}} = |\mathbf{m}|\hat{\mathbf{z}}$, which is exactly what the
demonstration does. Two properties follow directly from §1: RTP removes the
inclination of the *field* and the inclination of the *magnetisation*, so it
requires **both** directions as inputs. The field inclination is known from a
global field model; the magnetisation direction is not.

For the SYNTHETIC body:

| profile | peak (nT) | position of peak (m) | peak/trough |
|---|---|---|---|
| measured $\Delta T$ (mixed) | 1216.61 | −190 | 0.801 |
| true RTP | 3061.47 | −40 | 12.886 |
| RTP assuming the remanence direction ($-30°$) | 444.84 | −315 | 0.188 |

Assuming the wrong direction **leaves the peak $315\ \mathrm{m}$ from the body**
and drives the amplitude down by a factor of seven. A corrected-looking map can
therefore be confidently wrong: the display is data-consistent (it is a legitimate
dipole field) but the body is not where the colours are. RTP is a *display*
convention, not a correction, and it cannot create information about a direction it
needs as input. Vector or full-tensor gradient data, or a fit of the direction as
a parameter, are the ways to supply it.

## 4. Worked example — is this anomaly remanent?

Take the remanence-dominated SYNTHETIC profile of §2 as the observation: a dominant
negative trough of $-1964\ \mathrm{nT}$ with a small positive peak of
$+370\ \mathrm{nT}$, the peak sitting at $-315\ \mathrm{m}$ while the body is at
$x = 0$. Compare with the three model cases of §2: the induced case has
peak/trough $5.53$, the mixed case $0.80$, and the remanence-only case $0.188$.
The observed ratio $370/1964 = 0.188$ matches the remanence-dominated case
exactly, and the peak position matches too.

1. **The ratio is the diagnostic.** Peak/trough is dimensionless and insensitive
   to the body's size, so it is a robust first test for a dominant remanence.
2. **RTP with the wrong direction would fail visibly**: applying the induced
   ($60°$) assumption to this profile gives a bipolar result whose peak is
   $315\ \mathrm{m}$ from the body (§3).
3. **The conclusion is bounded.** The data say "the total magnetisation lies near
   $-30°$"; they do not say which minerals carry it, nor what the grade is.
   Remanence is a property of the rock's magnetic history, and it is the reason
   two adjacent bodies of the same ore can produce opposite anomalies.

## 5. Depth from anomaly shape: derivation and bias

For a vertically magnetised dipole measured with a vertical component, §1 gives
$Z(x) = C(2h^{2}-x^{2})/(x^{2}+h^{2})^{5/2}$ with $C = \mu_0 m/4\pi$. Setting
$u = x^{2}/h^{2}$, the half-maximum condition $Z(x) = \tfrac12 Z(0)$ becomes

$$\frac{2-u}{(1+u)^{5/2}} = 1 \;\Longrightarrow\; u = 0.25068
\;\Longrightarrow\; \frac{x_{1/2}}{h} = \sqrt{u} = 0.500683 .$$

So **depth = half-width / 0.5007** for that shape, with no free parameters. The
demonstration confirms the constant two ways: $0.500683$ by solving the equation
and $0.500700$ by numerically evaluating the profile (the difference is the
$0.01\ \mathrm{m}$ grid spacing).

Applied to real profiles:

| profile | shape admissible? | apparent depth (m) | error (m) |
|---|---|---|---|
| true RTP (vertical magnetisation) | yes | 300.0 | 0.0 |
| RTP assuming no remanence ($60°$) | yes | 271.3 | −28.7 |
| RTP assuming remanence only ($-30°$) | no (bipolar) | undefined | – |
| measured $\Delta T$, not RTP'd | no (bipolar) | undefined | – |
| true RTP + 1 nT noise | yes | 296.2 | −3.8 |

Three results, in order of importance:

1. **$1\ \mathrm{nT}$ of noise costs $3.8\ \mathrm{m}$ of depth** at
   $300\ \mathrm{m}$. Shape-based depth is a low-noise technique.
2. **Ignoring a $Q = 1.5$ remanence biases the depth by $-28.7\ \mathrm{m}$**,
   i.e. $-9.6\%$, from a *systematic* cause that more data cannot reduce.
3. **When the assumed direction is badly wrong the profile is bipolar and the rule
   does not apply at all.** A bipolar anomaly is not a depth problem; it is a
   direction problem, and reporting a depth from it is meaningless.

## 6. Self-demagnetisation: why $\Delta B \propto \kappa$ fails

A magnetised body produces its own field, which opposes the applied field inside
it. For an ellipsoid with a demagnetising factor $N$ along the direction of
interest, the internal field is $H_{\text{int}} = H_0 - NM$, so

$$M = \kappa H_{\text{int}} = \kappa(H_0 - NM)
\;\Longrightarrow\;
\boxed{\;M = \frac{\kappa H_0}{1+N\kappa}\;}$$

For a sphere $N = 1/3$ in every direction, so $M \to 3H_0$ as
$\kappa \to \infty$: **the magnetisation saturates.** The measured consequences:

| $\kappa$ (SI) | $\lvert M\rvert$ linear (A m⁻¹) | $\lvert M\rvert$ demagnetised (A m⁻¹) | ratio | $\Delta B$ linear (nT) | $\Delta B$ demagnetised (nT) |
|---|---|---|---|---|---|
| 0.01 | 0.3979 | 0.3966 | 1.003 | 61.7 | 61.5 |
| 0.10 | 3.9789 | 3.8505 | 1.033 | 617.3 | 597.4 |
| 0.50 | 19.8944 | 17.0523 | 1.167 | 3086.4 | 2645.5 |
| 1.00 | 39.7887 | 29.8416 | 1.333 | 6172.8 | 4629.6 |
| 3.00 | 119.3662 | 59.6831 | 2.000 | 18518.5 | 9259.3 |
| 10.00 | 397.8874 | 91.8202 | 4.333 | 61728.4 | 14245.0 |

At $\kappa = 3$ SI the linear formula over-predicts the anomaly by a **factor of
2**; at $\kappa = 10$ by a factor of $4.3$. This is a factor-scale error, not a
percentage one, and it is one of the commonest quantitative errors in magnetic
interpretation. Two further points:

- The correction needs a **shape** as an input, because $N$ depends on it.
  $N = 1/3$ holds for a sphere; a flat sheet has $N \approx 1$ and the linear
  formula is then wrong by much more.
- The demonstration checks both limits: at $\kappa = 10^{-6}$ the formula returns
  $1.333333\times10^{3} = \kappa H_0$; at $\kappa = 10^{6}$ it returns
  $3.999988\times10^{9}$ against the exact saturation value
  $3H_0 = 4.000000\times10^{9}$.

## 7. The exact ambiguity: scale invariance

With $\kappa$, $Q$ and the magnetisation direction fixed, the dipole anomaly
depends on the body only through $m/z^{3} \propto R^{3}/z^{3} = (R/z)^{3}$. It is
therefore **invariant under $R \to \lambda R$, $z \to \lambda z$**. The
demonstration makes this explicit by solving for the depth that reproduces a fixed
observed peak:

| radius (m) | required depth (m) | depth/radius |
|---|---|---|
| 100 | 150.0 | 1.50 |
| 150 | 225.0 | 1.50 |
| 200 | 300.0 | 1.50 |
| 300 | 450.0 | 1.50 |
| 400 | 600.0 | 1.50 |

**The amplitude fixes only the ratio**, and the ratio is $1.50$ for every radius.
The width of the profile is what fixes the scale — which is why §5's bias matters
so much: the width is the *only* depth information, and it is distorted by the
magnetisation direction. This is an exact non-uniqueness of the dipole field, not
an observational limitation, and it is the same structure as the gravity
mass–depth ambiguity in
[11-02-03](03-gravity-for-minerals.md).

## 8. Assumptions and regime of validity

1. **Uniform magnetisation.** A body with internally varying $\kappa$ or
   remanence is not a single dipole; its anomaly is a sum with extra shape
   information — and extra ambiguity, because the internal distribution is another
   unknown.
2. **Known $Q$, and a single remanence direction.** Real rocks carry several
   remanence components acquired at different times; a viscous overprint can even
   change with time.
3. **Far field.** The dipole approximation requires $z \gtrsim 2R$; at
   $z = 300\ \mathrm{m}$, $R = 200\ \mathrm{m}$ we are at the edge of it, which is
   why the voxel check in §1 is worth doing.
4. **$\Delta T$ as a projection.** $\Delta T \approx \mathbf{B}\cdot\hat{\mathbf{B}}_0$
   is valid only for small anomalies relative to the total field; a
   $60\,000\ \mathrm{nT}$ anomaly in a $50\,000\ \mathrm{nT}$ field is not small,
   and the approximation fails in the same way as the small-angle approximation in
   trigonometry.
5. **Flat topography and a flat observation surface.** A draped survey is not at a
   constant $z$; the apparent width is then a mixture of depth and terrain.
6. **No adjacent sources.** The half-width rule assumes an isolated body; an
   overlap broadens the profile and therefore over-estimates the depth.
7. **Isotropic susceptibility.** Anisotropy changes the direction of
   $\mathbf{M}$ relative to $\mathbf{H}$, which is precisely the direction that
   §3–§5 need.
8. **All numbers SYNTHETIC**, and the anisotropy assumption in particular is a
   strong one for a foliated host.

## 9. Units and dimensional checks

| Quantity | Unit | Check |
|---|---|---|
| $\kappa$ | – (SI) | dimensionless |
| $H$ | A m⁻¹ | $B/\mu_0$ ✔ |
| $M$ | A m⁻¹ | $\kappa H$ ✔ |
| $m = MV$ | A m² | A m⁻¹ × m³ ✔ |
| $B$ | T (report nT) | $(\mu_0/4\pi)\,m/R^{3}$: H m⁻¹ × A m² / m³ = T ✔ |
| $Q$ | – | ratio of two magnetisations ✔ |
| $N$ | – | dimensionless demagnetising factor, $0\le N\le1$ |

Two checks that catch most mistakes: $N$ must be dimensionless and in
$[0,1]$, and the induction term $\kappa H$ must have the same units as the
remanence, i.e. A m⁻¹ — a remanence quoted in A m⁻¹ and a susceptibility in SI can
then be compared directly through $Q$.

## 10. Exercises

Full sets with worked solutions:
[`exercises/02-magnetics-for-minerals-exercises.md`](exercises/02-magnetics-for-minerals-exercises.md)
and
[`exercises/02-magnetics-for-minerals-solutions.md`](exercises/02-magnetics-for-minerals-solutions.md).

## Mastery checkpoint

Without notes:

> A SYNTHETIC body is a sphere of radius $150\ \mathrm{m}$ at $z = 250\
> \mathrm{m}$ with $\kappa = 0.5$ SI in $B_0 = 48\ \mathrm{\mu T}$ at $65°$
> inclination; it carries a remanent magnetisation with $Q = 2$ at $-40°$
> inclination. **(a)** Compute the induced magnetisation and the induced dipole
> moment, with self-demagnetisation included. **(b)** Compute the total dipole
> moment and its inclination. **(c)** State two observable features of the anomaly
> that would tell you remanence dominates, and why each is robust. **(d)** Compute
> the depth you would infer from the half-width of an RTP profile, and state the
> sign of the bias if you ignored the remanence. **(e)** State the one measurement
> that would remove the direction ambiguity.

A worked version is in the
[solutions](exercises/02-magnetics-for-minerals-solutions.md).

## Common pitfalls

1. **Reading RTP as a correction.** It is a re-synthesis that requires the
   magnetisation direction as an input; a wrong input gives a confidently wrong
   map.
2. **Using $\Delta B \propto \kappa$ for a magnetic body.** Self-demagnetisation
   changes it by a factor above $\kappa \approx 0.1$; the error is not a
   percentage.
3. **Assuming $\Delta T$ is the field.** It is a projection onto the ambient
   direction, valid only for small anomalies.
4. **Treating asymmetry as proof of remanence.** An induced anomaly in an inclined
   field is already asymmetric (peak/trough $5.5$ in this SYNTHETIC case).
5. **Applying a half-width rule to a bipolar anomaly.** The rule is defined for an
   RTP-shaped profile; if the shape is wrong the answer is meaningless, not
   merely biased.
6. **Reporting a depth without a shape check.** The width is the only depth
   information in the dipole field, and it is scale-covariant with the
   magnetisation direction.
7. **Forgetting that the sphere's $N = 1/3$ is shape-specific.** Using it for a
   sheet is an order-of-magnitude error.

## Related modules

- [11-02-01 Geophysical Signatures of Major Deposit Types](01-deposit-signatures.md)
  — where magnetics sits in the signature vector.
- [11-02-03 Gravity for Chromite, Massive Sulphide and Iron Ore](03-gravity-for-minerals.md)
  — the same shape-versus-amplitude logic for a method with no direction problem.
- [11-02-04 EM for Conductors, Massive Sulphides and Graphite](04-em-for-minerals.md)
  — the magnetic and conductivity signatures that separate sulphide from graphite.
- [08-03 Magnetic Anomalies and Modelling](../../08-geomagnetism-electromagnetism/03-magnetic-anomalies-and-modelling/README.md)
  — the general theory, including Euler deconvolution and inversion.
