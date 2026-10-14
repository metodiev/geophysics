---
id: 05-07-01
title: "Qualitative Interpretation: Anomaly Shape and Position Rules"
level: advanced
prereqs: ["05-01-03", "05-03-02", "07-03-01"]
tags: [interpretation, potential-fields, gravity, magnetics, ambiguity, shape-rules]
---

# Qualitative Interpretation: Anomaly Shape and Position Rules

## Learning objectives

By the end of this lesson you will be able to:

1. **Separate** the three inferences that interpretation is constantly confused
   about — *detecting* an anomaly, *locating* it, and *identifying its cause* —
   and state which of them a geophysical dataset actually supports directly.
2. **Derive** the half-width constants for the point mass and the line mass, and
   use them to convert a measured half-width into a depth.
3. **Derive** the far-field amplitude falloff of a potential-field anomaly from
   its source geometry, and explain why the exponent classifies the source order.
4. **Apply** the horizontal-gradient rule to locate a contact, and state the
   regime in which the "half at the edge" rule is valid.
5. **Recognise** that a shape constant is a *model-dependent* number: a profile
   contains roughly one number's worth of shape information, and the choice of
   model contributes more to the answer than the measurement does.
6. **State** an interpretation as a model plus its assumptions plus a bound,
   rather than as a depth.

## Prerequisites

- [05-01-03 Resolution, Penetration Depth and the Fundamental Trade-Off](../01-what-geophysics-measures/03-resolution-depth-tradeoff.md)
  — why the shortest recoveryable wavelength, not the instrument, sets resolution.
- [05-03-02 Analytical Solutions for Simple Bodies (Sphere, Sheet, Dyke)](../03-forward-modelling-principles/02-analytical-solutions.md)
  — the closed forms used throughout; this lesson does not re-derive them, it
  measures what they imply.
- [07-03-01 Interpreting Anomalies: Geometry, Depth and Amplitude Rules](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/01-anomaly-interpretation.md)
  — the gravity-specific version of the same rules, with the reduction steps.

## 1. Intuition: detection, location and identification are three inferences

Almost every disagreement between a geophysicist and a driller comes from
conflating three logically different claims. Write them separately:

1. **Detection.** *"There is a source whose field is measurably different from
   the field of the surrounding rock."* This claim is about the data and the
   noise. It is testable by the survey itself, and only by the survey itself. A
   potential-field dataset, on its own, is a measurement of a **field**, and the
   only thing it asserts directly is that the field is anomalous.
2. **Location.** *"The anomalous source lies between these depths and within this
   horizontal footprint."* This claim is about a **model**, because depth is not
   measured: it is inferred from a decay rate, a curvature, or a width. It is
   testable by a second, independent dataset — or by a borehole.
3. **Identification.** *"The source is massive sulphide / a salt dome / a
   cavity / a kimberlite."* This claim is about **geology**, and no geophysical
   dataset contains geology. It requires a prior association between a physical
   property and a rock type, and that association is empirical, regional, and
   frequently wrong.

The reason this matters is not pedantry. Detection is the *only* one of the three
that geophysics does directly, and the other two borrow credibility from it. A
tight-looking anomaly map invites the reader to believe the interpretation, and
the interpretation is where the uncertainty lives.

This lesson is about the smallest, most honest version of inference 2: the part
of location that can be read off a single anomaly's shape and position. That
information is real but small. Section 3 derives it, Section 4 puts numbers on
it, and Section 6 shows how quickly the model choice swamps it.

## 2. Precise definitions

### 2.1 Anomaly

The **anomaly** is the residual field after regional field, datum, drift, terrain
and instrument effects have been removed:

$$\Delta g(\mathbf{r}) = g_{\text{observed}}(\mathbf{r}) - g_{\text{reference}}(\mathbf{r}).$$

Every term on the right is a modelling decision. There is no measurement of
$\Delta g$ that does not contain a choice, and this is the first place where a
"data interpretation" is already a model (Section 7 of the
[pitfalls lesson](./06-interpretation-pitfalls.md)).

### 2.2 Half-width

For a profile $g(x)$ with a single central maximum $g_{\max}$ at $x=x_c$, the
**half-width** is the horizontal distance from $x_c$ to the point where the
anomaly drops to $g_{\max}/2$. More generally define

$$w(f) = |x_f - x_c|, \qquad g(x_f) = f\,g_{\max}.$$

$w(1/2)$ is the half-width and $w(1/4)$ is the quarter-width.

### 2.3 Shape constant

A **shape constant** is a dimensionless number relating a geometric scale of the
source (a depth $z$, a radius $R$) to a measurable scale of the anomaly:

$$\frac{z}{w(1/2)} = c_{\text{shape}}.$$

The whole of the half-width rule is that $c_{\text{shape}}$ depends on the source
geometry and *not* on the amplitude, the density contrast, or the station
spacing. That is its strength and, as Section 4 shows, its limitation.

### 2.4 Structural index

The **structural index** $N$ is the exponent in the power law that the source's
field obeys in the far field. In two dimensions, a line mass ($N=1$ in the
standard Euler convention) falls as $r^{-1}$ in potential and $r^{-2}$ in field;
a point mass (a 3-D compact body, $N=2$) falls as $r^{-2}$ in potential and
$r^{-3}$ in field. The classification is asymptotic: "far field" is not a synonym
for "anywhere beyond the peak".

## 3. Derivations

### 3.1 Half-width of a point mass

A point mass $M$ at depth $z$ produces, directly above in a profile through it,

$$g_z(x) = \frac{GMz}{(x^2+z^2)^{3/2}}. \tag{1}$$

The peak is at $x=0$ with $g_{\max} = GM/z^2$. Half of it:

$$\frac{GMz}{(x^2+z^2)^{3/2}} = \frac{GM}{2z^2}
\;\Longrightarrow\; (x^2+z^2)^{3/2} = 2z^3
\;\Longrightarrow\; x^2+z^2 = 2^{2/3}z^2 .$$

Therefore

$$\boxed{\;w_p(1/2) = z\sqrt{2^{2/3}-1} = 0.76642\,z,
\qquad \frac{z}{w_p(1/2)} = 1.30477\;} \tag{2}$$

and, in the same way, $w_p(1/4) = z\sqrt{2^{4/3}-1} = 1.23278\,z$ so that

$$\frac{w_p(1/4)}{w_p(1/2)} = \frac{\sqrt{2^{4/3}-1}}{\sqrt{2^{2/3}-1}} = 1.60854. \tag{3}$$

### 3.2 Half-width of a line mass

An infinite horizontal cylinder is a line mass with mass per unit length $\lambda$:

$$g_z(x) = \frac{2G\lambda z}{x^2+z^2}. \tag{4}$$

The peak is $2G\lambda/z$, so $g_z = g_{\max}/2$ requires $x^2+z^2 = 2z^2$, i.e.

$$\boxed{\;w_\ell(1/2) = z, \qquad \frac{z}{w_\ell(1/2)} = 1\;} \tag{5}$$

and $w_\ell(1/4) = \sqrt{3}\,z$, giving $w_\ell(1/4)/w_\ell(1/2) = \sqrt{3} =
1.73205$.

### 3.3 What the two shapes imply about each other

Equations (2), (3) and (5) contain the entire content of the qualitative rulebook,
and they are worth reading as a warning:

- The same measured half-width implies a depth that differs by the ratio
  $1.30477/1 = 1.30477$ depending on which of the two models you assume. That is a
  **30.5 per cent model error**, and no improvement in the data can remove it.
- The shapes differ by only 7.7 per cent in the ratio
  $w(1/4)/w(1/2)$ — 1.60854 against 1.73205. To discriminate the two, you must
  measure a width ratio to better than that in the presence of noise.

So a single profile carries about **one bit** of shape information, and it is
spent on distinguishing a compact body from a cylindrical one. Everything else —
whether the body is a sphere, a prism, a thin sheet, or a stack of two bodies —
is unconstrained by the width alone (see
[05-01-04 Non-Uniqueness of Geophysical Models](../01-what-geophysics-measures/04-ambiguity-and-nonuniqueness.md)
and, for the full proof,
[02-08-06 Uniqueness Theorems and Boundary Conditions](../../02-physics/08-potential-theory/06-uniqueness-theorems.md)).

### 3.4 Far-field falloff

Expand equation (1) for $x \gg z$:

$$g_z(x) \approx \frac{GMz}{x^3}\left(1 - \frac{3z^2}{2x^2} + \cdots\right)
\;\Longrightarrow\; \log g_z = \text{const} - 3\log x . \tag{6}$$

For the line mass, equation (4) gives directly

$$g_z(x) \approx \frac{2G\lambda z}{x^2} \;\Longrightarrow\;
\log g_z = \text{const} - 2\log x . \tag{7}$$

Two consequences, and both are quantitative:

- The slope of $\log g$ against $\log x$ **is** $-N_{\text{field}}$: $-3$ for a
  compact 3-D body, $-2$ for a 2-D body. This is a model-independent diagnostic
  *provided* the window is genuinely far-field.
- The measurement must extend far enough. From the demonstration, the fitted
  slope over a window from one to two depths is $-2.01$ for a point mass
  (indistinguishable from a line mass), and only reaches $-2.97$ over a window
  from five to twenty depths. A profile whose aperture is two depths cannot
  classify its own source.

### 3.5 The contact: gradient position and the "half at the edge" rule

A semi-infinite slab (a density contact) with its edge at $x=0$, top $z_1$,
bottom $z_2$, and density contrast $\Delta\rho$ has, from integrating the
line-mass kernel over the slab,

$$g_z(x) = 2G\Delta\rho\int_{z_1}^{z_2}
\left[\frac{\pi}{2} + \arctan\!\left(\frac{x}{z}\right)\right]\mathrm{d}z ,
\qquad \frac{\partial g_z}{\partial x} = 2G\Delta\rho
\int_{z_1}^{z_2}\frac{z}{x^2+z^2}\,\mathrm{d}z . \tag{8}$$

Three statements follow, and all three are measured in the demonstration:

1. **The horizontal gradient peaks over the edge.** Each term in the integrand is
   a Lorentzian centred on $x=0$, so the integral is maximal at $x=0$. Measured
   extremum position: $x = -3.5$ m for a 5 m discretisation, consistent with the
   grid, not with a physical offset.
2. **The edge value is the mean of the two limits.** As $x\to-\infty$ the factor
   tends to $0$, as $x\to+\infty$ it tends to $\pi$, so $g_z(0)$ is exactly half
   of $g_z(\infty)$ *for a given $z$*.
3. **The half rule is asymptotic in the observation distance.** Comparing $g_z$
   at the edge with $g_z$ at an interior offset $x_i$ gives $0.5$ only when
   $x_i \gg z$. Measured for a slab between 50 and 100 m depth: the ratio is
   0.627 at 100 m, 0.564 at 200 m, 0.525 at 500 m, 0.5006 at 20 km. Quoting
   "half at the contact" for a shallow slab observed a few hundred metres inside
   is wrong by 13 per cent, which propagates directly into the estimated contrast.

## 4. Worked examples

### 4.1 Depth from a half-width, with the model error stated

**Problem.** A Bouguer anomaly profile has a single maximum of 0.267 mGal. The
anomaly falls to 0.134 mGal at $x = 383$ m from the peak. Estimate the depth.

*Step 1 — is the profile even?* Both candidate models are symmetric, so symmetry
is not diagnostic. Assume the anomaly is isolated and that the regional has been
removed.

*Step 2 — apply the compact-body rule.* From equation (2),

$$z = 1.30477 \times 383\ \mathrm{m} = 499.7\ \mathrm{m} \approx 500\ \mathrm{m}.$$

*Step 3 — apply the cylindrical-body rule.*

$$z = 1.00000 \times 383\ \mathrm{m} = 383\ \mathrm{m}.$$

*Step 4 — state the result honestly.* The depth is **between 383 and 500 m**; the
two ends correspond to a cylinder and a compact body, and the profile does not
distinguish them. Reporting "depth = 500 m" is a model choice presented as a
measurement.

*Step 5 — check the aperture.* The demonstration confirms that a fit inside three
source depths gives an apparent slope of $-2.9$ rather than $-3$; a profile that
does not extend to at least five depths should not be used even for the falloff
test.

### 4.2 Amplitude, contrast and the temptation to over-claim

The peak amplitude 0.267 mGal corresponds, for a compact body, to

$$M = \frac{g_{\max}z^2}{G} = \frac{(2.67\times10^{-6})(500^2)}{6.674\times10^{-11}}
= 1.00\times10^{10}\ \mathrm{kg}.$$

That is a *mass*, and it is the only thing the amplitude gives you directly. The
demonstration shows that converting it to a density requires a volume, the volume
requires a shape, and the shape is exactly what is unconstrained; using the
borehole's own intersection half-length of 120 m gives an implied contrast of
783.6 kg m⁻³ where the core measures 800.0 kg m⁻³ — a 2 per cent agreement in one
case and a 59 per cent error in another, from the same procedure.

### 4.3 Locating a contact edge

A vertical contact is sought. The horizontal gradient is computed from a 5 m
discretised model of a slab between 200 and 500 m depth.

*Measured:* the gradient extremum lies at $x = -3.5$ m relative to the true edge
at $x = 0$, i.e. within one grid cell. The gradient *half-width* is 299.2 m
against a model prediction of 300 m for a thin slab, a 0.3 per cent agreement.

*Interpretation.* The edge location is well determined because it depends on
symmetry rather than on amplitude; the depth to the slab is much less well
determined because it depends on the gradient's width, which the same noise
affects more. **Position is robust; depth and property are not.**

## 5. Assumptions

Stated separately, because each one is a failure mode:

1. **Isolated source.** The half-width rules assume a single anomaly on a removed
   regional. Two interfering bodies destroy the width.
2. **Known structural index.** The constant $c_{\text{shape}}$ is borrowed from a
   model. Using the wrong one costs 30 per cent, not 3 per cent.
3. **No remanence, no self-demagnetisation, no anisotropy** in the magnetic case;
   the gravity case is free of these but has its own issues with density
   heterogeneity.
4. **A profile through the centre of the body.** A profile that is off-centre
   gives a wider apparent anomaly and therefore an overestimated depth.
5. **A flat observation surface.** Topography shames the reduction before it
   shames the interpretation.
6. **Noise small enough that $w(1/2)$ is measurable.** If the peak is only a few
   times the noise, the half-width is not measurable and none of this applies.

## 6. Units and dimensional analysis

- $g_z$: m s⁻², quoted in mGal ($1\ \mathrm{mGal} = 10^{-5}\ \mathrm{m\,s^{-2}}$).
- $M$: kg. $G M z / (x^2+z^2)^{3/2}$:
  $\mathrm{m^3 kg^{-1} s^{-2}}\cdot\mathrm{kg}\cdot\mathrm{m}/\mathrm{m^3} =
  \mathrm{m\,s^{-2}}$ ✓.
- $\lambda$: kg m⁻¹. $2G\lambda z/(x^2+z^2)$:
  $\mathrm{m^3 kg^{-1} s^{-2}}\cdot\mathrm{kg\,m^{-1}}\cdot\mathrm{m}/
  \mathrm{m^2} = \mathrm{m\,s^{-2}}$ ✓. The factor of 2 is the standard
  $\int_{-\infty}^{\infty}$ of a 2-D kernel and carries no units.
- Shape constants are dimensionless, which is why they are transferable between
  units and why they must be checked for a factor-of-two convention difference
  ($\Delta\rho$ against $2\Delta\rho$) before use.
- The half-width $w(1/2)$ has units of length, and so does the depth it
  estimates: a half-width rule that produces a number with units of mass or
  contrast is wrong by construction.

A useful anchor: $G M / z^2$ in mGal with $M$ in units of $10^{9}$ kg and $z$ in
km is $6.674\times10^{3} M_{9} / z_{\mathrm{km}}^2$ µGal — worth memorising as a
sanity check on any potential-field amplitude.

## 7. Python demonstration

`code/qual_interp_demo.py` builds the profiles analytically, measures the
half-widths and far-field slopes numerically, and validates the 2-D model against
an independent quadrature of the slab integral. Predict each line before running.

```python
z_true = 100.0
gp = gz_point(x, z_true, 1.0e10)     # point mass
gl = gz_line(x, z_true, 1.0e9)       # line mass
for name, prof in (("point mass (sphere)", gp), ("line mass (cylinder)", gl)):
    w_half = width_at(x, prof, 0.5)
    print(f"{name:22s} depth/half-width = {z_true / w_half:9.5f}")
```

Measured output, abridged:

```
point mass (sphere)    half-width       =    76.642 m
                       depth/half-width =   1.30477
                       w(1/4)/w(1/2)    =   1.60854
line mass (cylinder)   half-width       =   100.000 m
                       depth/half-width =   1.00000
                       w(1/4)/w(1/2)    =   1.73205

source           1-2 z     2-5 z    5-20 z   exact
point mass     -2.0108   -2.7244   -2.9685      -3
line mass      -1.3405   -1.8163   -1.9790      -2

cell (m)   max |cells - quadrature| (mGal)   cells   ratio to previous
   20.0         3.769e-02                        1515
   10.0         1.885e-02                        6030              2.00
    5.0         9.426e-03                       24060              2.00
    2.5         4.713e-03                       96120              2.00

gradient extremum at x =    -3.50 m (true edge x = 0)

field at edge (x = 0)          =   0.3145 mGal
closed form 2 G d_rho (pi/2) t =   0.3145 mGal

interior offset (m)   edge/interior   (limit = 0.5)
             100          0.62720
             500          0.52485
           20000          0.50060
```

### What to observe, and why it matters

| Observation | Consequence |
|---|---|
| $z/w(1/2)$ is exactly $1.30477$ and exactly $1$, to five digits | The shape constant is a property of the geometry, not of the amplitude — which is why it is useful and why it is dangerous |
| The 1–2 depth slope is $-2.01$ for a point mass | A short profile cannot tell a sphere from a cylinder by its falloff |
| Error halves when the cell halves (ratio 2.00) | The discrete line-mass sum is first-order accurate; a 5 m model is already good to $10^{-2}$ mGal |
| Edge/interior is 0.627 at 100 m but 0.5006 at 20 km | The "half at the edge" rule has a stated regime; outside it, the rule fails silently |

> **Breaking exercise.** Change $z_{\text{true}}$ to 300 m and re-run. Predict,
> before running, which columns change and which do not. Only the far-field
> windows should change, and they should now reach $-3$ sooner in absolute
> distance — the window is measured in depths, not metres.

## 8. Exercises

Full problem sets, with worked solutions, are in
[`exercises/01-qualitative-interpretation-exercises.md`](./exercises/01-qualitative-interpretation-exercises.md)
and
[`exercises/01-qualitative-interpretation-solutions.md`](./exercises/01-qualitative-interpretation-solutions.md).

### ★ Foundational

**★1.** A magnetic anomaly falls to half its peak value 250 m from the peak.
Give the depth under (a) a compact-body model and (b) a 2-D body model, and state
which assumption each rests on.

**★2.** Show that the peak amplitude of a line mass is $2G\lambda/z$ and that a
line mass of $\lambda = 10^{9}$ kg m⁻¹ at 500 m gives 0.267 mGal.

**★3.** State the far-field log–log slope for the vertical field of: a point
mass, a line mass, and a semi-infinite slab. Explain the slab answer in one
sentence.

### ★★ Applied

**★★4.** A profile over an isolated anomaly has $w(1/2) = 383$ m and
$w(1/4) = 617$ m. Compute the ratio, compare it with 1.60854 and 1.73205, and
state what you can and cannot conclude.

**★★5.** Run `code/qual_interp_demo.py`. Record the edge/interior ratios for
offsets 100 m and 1000 m, and compute the depth at which the rule would be in
error by 5 per cent for a slab 50–100 m deep.

**★★6.** For the slab of Section 3.5, derive the asymptotic half-width of
$\partial g_z/\partial x$ for a *thin* slab ($z_2 - z_1$ small) and show that it
equals the slab depth.

### ★★★ Research-oriented

**★★★7.** The demonstration measures the discrete-sum convergence order as
first order in the cell size. Derive, or determine numerically, why a line-mass
sum for a smooth 2-D body is only first-order accurate, and identify what change
of discretisation would give second order. Report the measured order after the
change.

**★★★8.** Construct a profile that is the sum of a point mass at 300 m and a
second point mass of half the sign at 900 m. Show that a single-body half-width
estimate is biased, quantify the bias, and state the smallest second body that
would go undetected at a stated noise level. This is the ground-truthing problem
of [05-07-04](./04-ground-truthing.md) in miniature.

## 9. Common mistakes

1. **Quoting a depth from a rule without naming the model.** The half-width rule
   is a family of rules, one per shape, and they differ by 30 per cent.
2. **Measuring a half-width on a profile with an incompletely removed regional.**
   A sloping regional shifts the apparent peak and widens the anomaly, and the
   error is always towards *greater* depth.
3. **Using a profile that does not extend to several source depths** and then
   quoting a falloff exponent. The measured slope is a windowed average of
   curvature, not an asymptotic property.
4. **Treating a gradient maximum as an edge location without checking the depth.**
   For a steeply dipping contact the gradient maximum is offset from the surface
   projection of the edge, and the offset depends on the dip.
5. **Assuming "half at the contact" holds at the observation distance used.**
   Section 3.5 measures a 13 per cent error at 200 m for a shallow slab.
6. **Calling a well-fitted shape an identification.** Shape constrains geometry.
   It does not name a rock.

## 10. Real-world applications

- **Mineral exploration.** Half-width depth estimates are the standard first pass
  over a magnetic or gravity grid; they are useful precisely because they are
  cheap, and dangerous precisely because they look precise.
- **Engineering and cavity detection.** Microgravity surveys locate voids by
  their gradient signature; the position is reliable, the depth much less so
  ([07-03-06 Microgravity for Cavities, Tunnels and Archaeology](../../07-gravity-geodesy/03-gravity-anomalies-and-modelling/06-microgravity-applications.md)).
- **Archaeology and near-surface.** Small anomalies over shallow targets have
  half-widths of metres, so station spacing, not physics, sets the resolution.
- **Basin and contact mapping.** Horizontal-gradient and tilt-derivative maps
  locate contacts and are used routinely in regional interpretation; the
  gradient-peak rule is the reason they work.
- **Survey design.** The rule that a profile must extend to several source depths
  is a design constraint: it sets the required line length before mobilisation,
  and it belongs in the survey plan
  ([05-05-01 Survey Planning](../05-survey-design-and-acquisition/01-survey-planning.md)).

## 11. Further reading

- **Blakely, R. J. (1995). *Potential Theory in Gravity and Magnetic
  Applications*. Cambridge University Press.** Chapters 9–10. Level: advanced.
  The standard reference for the shape and derivative rules used here, with the
  harmonic-function basis for the spectral falloff in Section 3.4.
- **Telford, W. M., Geldart, L. P. & Sheriff, R. E. (1990). *Applied
  Geophysics* (2nd ed.). Cambridge University Press.** Chapter 2 for gravity,
  Chapter 3 for magnetics. Level: intermediate. The classic source of the
  half-width rules in the form practitioners use them.
- **Nettleton, L. L. (1976). *Gravity and Magnetics in Oil Prospecting*.
  McGraw-Hill.** Level: intermediate. Dated but unusually honest about how much
  the rules of thumb can and cannot deliver.
- **Nabighian, M. N. et al. (2005). 75th anniversary: Historical development of
  the gravity and magnetic methods. *Geophysics*, 70(5), 33ND–53ND.** Level:
  advanced. A review of how the qualitative rulebook was assembled and where it
  has been found wanting; check your library for current access.

> Note on citations: bibliographic details are given so you can locate the works.
> This repository does not host or reproduce copyrighted text; confirm current
> editions and availability through your library.

## 12. Related lessons

- [05-07-02 Quantitative Interpretation and Depth Estimation](./02-quantitative-interpretation.md)
  — the numerical version, including the regional-trend bias and the spectral
  depth estimate that Section 3.4 anticipates.
- [05-07-03 Integrating Multiple Methods and Constraints](./03-multi-method-integration.md)
  — what does reduce the 30 per cent model error, and by how much.
- [05-07-04 Ground Truthing: Boreholes, Outcrop and Drill Core](./04-ground-truthing.md)
  — the experiment that decides between two data-compatible models.
- [05-07-06 Common Interpretation Pitfalls and False Positives](./06-interpretation-pitfalls.md)
  — the trend-removal and aliasing failures that Section 3 has assumed away.
- [02-08-06 Uniqueness Theorems and Boundary Conditions](../../02-physics/08-potential-theory/06-uniqueness-theorems.md)
  — why the shape ambiguity of Section 3.3 is a theorem rather than a data
  limitation.

## Self-assessment checklist

- [ ] I can state the difference between detection, location and identification,
      and say which one geophysics supports directly. (§1)
- [ ] I can derive $w(1/2) = 0.76642z$ for a point mass and $w(1/2) = z$ for a
      line mass from the field expressions. (§3.1–3.2)
- [ ] I can explain why the ratio $w(1/4)/w(1/2)$ discriminates the two shapes and
      by how much. (§3.3)
- [ ] I can predict the far-field log–log slope for a given source order and say
      how wide a profile must be for the measurement to mean anything. (§3.4)
- [ ] I can locate a contact from a horizontal-gradient map and state the regime
      in which the edge equals half the interior value. (§3.5)
- [ ] I can write an interpretation as a model, its assumptions, and a bound, and
      I can name at least four assumptions that would invalidate it. (§4, §5)
- [ ] I can check a potential-field amplitude and a half-width for dimensional
      consistency without a calculator. (§6)
- [ ] I can run the demonstration and interpret each printed number. (§7)
