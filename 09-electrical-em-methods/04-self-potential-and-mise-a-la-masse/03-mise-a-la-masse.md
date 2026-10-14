---
id: 09-04-03
title: "Mise-a-la-Masse and Induced Polarisation Mapping"
level: graduate
prereqs: ["09-04-01", "09-02-01", "09-02-03", "09-03-01"]
tags: [electrical-methods, mise-a-la-masse, induced-polarisation, conducting-sphere, non-uniqueness, energised-body]
---

# Mise-à-la-Masse and Induced Polarisation Mapping

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** the mise-à-la-masse (MALM) geometry — a current electrode placed
   inside or against a target so that the target itself is energised — and state
   what it measures.
2. **Derive** the half-space potential of a buried point electrode by the image
   method, and **show** that the apparent resistivity of a buried electrode in a
   homogeneous half-space equals the true resistivity at every offset.
3. **Derive** the external potential of a conducting sphere in a locally uniform
   field and **verify** both boundary conditions and the perfect-conductor limit
   numerically.
4. **Compute** the surface anomaly of a buried conductor energised from a
   borehole electrode, and **demonstrate** that it saturates in conductivity
   contrast, so that amplitude measures distance rather than conductivity.
5. **Quantify** the distance–contrast ambiguity and state which feature of the
   anomaly pattern breaks it.
6. **State** the model's regime of validity precisely, including the case of a
   source *inside* the body, and **explain** what model is needed there.
7. **Compare** the MALM anomaly with the response of a surface dipole-dipole
   array over the same body, and **state** why the two are used together with an
   IP measurement.

## Prerequisites

- [09-04-01 Sources of Self-Potential: Electrokinetic, Electrochemical](01-self-potential-sources.md)
  — the image method and the half-space potential that this lesson extends.
- [09-02-01 Resistivity Principle and the Four-Electrode Arrangement](../02-dc-resistivity/01-resistivity-principle.md)
  — the geometric factor and apparent resistivity.
- [09-02-03 Apparent Resistivity and Geometric Factors](../02-dc-resistivity/03-apparent-resistivity.md)
  — how a measured potential difference is converted into an apparent
  resistivity.
- [09-03-01 IP Principle: Time-Domain and Frequency-Domain Measurement](../03-induced-polarisation/01-ip-principle.md)
  — the polarisation measurement that maps the same body a second way.

**All models and data in this module are SYNTHETIC.** Resistivities, contrasts,
depths, radii, currents and geometries are chosen teaching values, not
measurements of any real ore body, quarry, borehole or instrument.

---

## 1. Intuition: put the current where the target is

Every other electrical method infers a target from the *outside*: current is
injected at the surface, and the anomaly of the potential field is a small
perturbation of a large background. Mise-à-la-masse inverts that arrangement. If
a borehole or an outcrop puts a current electrode in contact with a conductive
body, then the body itself becomes the current source. Its surface, or a large
part of it, is at one potential, and the current spreads outward *from the body*
into the host. The measured surface pattern is then dominated by the body's
geometry rather than by a perturbation of a background field.

Three practical consequences follow, and they are the content of this lesson:

1. **The anomaly can be large.** A body energised directly may change the
   measured potential by tens of per cent where an array at the surface would
   produce a few per cent.
2. **The amplitude saturates in conductivity contrast.** Once a body is much more
   conductive than its host, making it more conductive changes almost nothing.
   The amplitude is set by the *geometry* — size and distance — not by the
   contrast. This is a measured result of Section 3.4, and it is the fundamental
   limitation of the method.
3. **The model changes character when the electrode enters the body.** The
   locally-uniform-field approximation used in Section 3 fails there; the body
   must be treated as an equipotential electrode, which is a different boundary
   value problem. Section 3.6 measures the failure and states what replaces it.

## 2. Precise definitions

### 2.1 Geometry

The model used throughout: a host of resistivity $\rho_0$ [$\Omega$ m], a current
electrode at $(x_s, z_s)$ carrying current $I$ [A], and a spherical conductor of
radius $a$ [m], conductivity $\sigma_1 = k\sigma_0$, centred at
$(x_c, z_c)$. The **contrast** is $k = \sigma_1/\sigma_0$ (dimensionless).

### 2.2 Apparent resistivity for a buried electrode

With a single current electrode at depth $z_s$ and a potential electrode at
horizontal offset $x$, the half-space potential is
$V = \rho I/\left(2\pi\sqrt{x^{2}+z_s^{2}}\right)$, so the apparent resistivity

$$\rho_a = \frac{2\pi\sqrt{x^{2}+z_s^{2}}\,V}{I}$$

equals the true $\rho$ at every offset in a homogeneous half-space. Any departure
of $\rho_a$ from a constant along a profile is the anomaly of a heterogeneity —
exactly the logic of a resistivity survey, but with the current source *inside*
the ground.

### 2.3 The sphere response

A sphere of radius $a$ in a locally uniform field $E_0$ has the external
potential (superposed on the primary $-E_0 r\cos\theta$)

$$\varphi_{\text{anom}} = \frac{A\cos\theta}{r^{2}}, \qquad
A = a^{3}E_0\,\frac{\sigma_1 - \sigma_0}{\sigma_1 + 2\sigma_0},$$

with $r$ and $\theta$ measured from the sphere centre and the axis along
$\mathbf{E}_0$. Two limits are exact and diagnostic: $A = 0$ when
$\sigma_1 = \sigma_0$ (no body), and $A \to a^{3}E_0$ as
$\sigma_1 \to \infty$ (a perfect conductor, whose surface is an equipotential).

### 2.4 The anomaly and its saturation

Define the surface anomaly as the percentage change in the potential at a station
above the body, $100\left|V_{\text{anom}}\right|/\left|V_{\text{primary}}\right|$.
The **saturated anomaly** is its limit as $k \to \infty$ at fixed geometry.

## 3. Derivations

### 3.1 The buried electrode, and the resistivity identity

Mirror the electrode in the insulating surface with the same sign (lesson 01
§3.4):

$$V(x) = \frac{\rho_0 I}{2\pi\sqrt{x^{2}+z_s^{2}}}.$$

With $\rho_0 = 100\ \Omega$ m, $I = 1$ A and $z_s = 50$ m the demonstration prints
$V(0) = 318.3099$ mV, matching the analytic
$\rho I/(2\pi z_s) = 318.3099$ mV, and then

| offset $x$ (m) | $V$ (mV) | $V/V(0)$ | $\rho_a$ ($\Omega$ m) |
|---|---|---|---|
| 0 | 318.310 | 1.0000 | 100.000 |
| 25 | 284.705 | 0.8944 | 100.000 |
| 50 | 225.079 | 0.7071 | 100.000 |
| 100 | 142.353 | 0.4472 | 100.000 |
| 200 | 77.201 | 0.2425 | 100.000 |
| 400 | 39.481 | 0.1240 | 100.000 |

The constant apparent resistivity in the last column is the identity of
Section 2.2, verified to the printed digits. The profile's width obeys the exact
point-source rule of lesson 01: FWHM $= 173.2$ m $= 3.4640 \times 50$ m against
the analytic $2\sqrt{3} = 3.4641$.

### 3.2 The conducting sphere: derivation and verification

Inside and outside the sphere write

$$\varphi_{\text{in}} = -B r\cos\theta, \qquad
\varphi_{\text{out}} = -E_0 r\cos\theta + \frac{A\cos\theta}{r^{2}},$$

using the fact that the interior solution must be finite at the origin and that
the $l = 0$ and $l \geq 2$ spherical harmonics are absent in a uniform applied
field. Continuity of $\varphi$ and of the normal current density
$\sigma\,\partial\varphi/\partial r$ at $r = a$ give two equations:

$$-Ba = -E_0 a + \frac{A}{a^{2}}, \qquad
-\sigma_1 B = -\sigma_0 E_0 - \frac{2\sigma_0 A}{a^{3}} .$$

Eliminating $B$ and using $\sigma_1 = k\sigma_0$:

$$A = a^{3}E_0\,\frac{k-1}{k+2}, \qquad
B = E_0\,\frac{3}{k+2},$$

which is the result quoted in Section 2.3.

**Verification.** The demonstration prints, for $a = 10$ m, $k = 100$,
$E_0 = 1$ V/m, $A = 970.5882$ V m and $B = 0.029412$ V/m, and then the two
boundary conditions at six angles:

| $\theta$ (deg) | $\varphi_{\text{in}} - \varphi_{\text{out}}$ (V) | $\sigma_1\partial_r\varphi_{\text{in}} - \sigma_0\partial_r\varphi_{\text{out}}$ (A/m²) |
|---|---|---|
| 0 | $-1.055\times10^{-15}$ | $+3.469\times10^{-18}$ |
| 30 | $-5.551\times10^{-16}$ | $+3.469\times10^{-18}$ |
| 60 | $-5.551\times10^{-16}$ | $0$ |
| 90 | $+6.163\times10^{-32}$ | $-3.852\times10^{-34}$ |
| 120 | $+4.718\times10^{-16}$ | $0$ |
| 180 | $+1.055\times10^{-15}$ | $-3.469\times10^{-18}$ |

Both are satisfied to round-off (worst case $1.05\times10^{-15}$ V and
$3.47\times10^{-18}$ A/m²). The parameter checks give $A = 0$ exactly for
$k = 1$, and for $k = 10^{6}$ a potential on $r = a$ within
$3\times10^{-5}$ V of zero at every angle — that is, equipotential to $0.0003\%$
of $E_0a = 10$ V, which is the perfect-conductor boundary condition.

### 3.3 The surface anomaly of an energised body

The electrode's field at the sphere centre is not uniform, so the response is
computed as follows: evaluate the primary field at the centre numerically
$\left(\mathbf{E}_0 = -\nabla V_{\text{primary}}\right)$, form the induced dipole
through $A$, convert it to an equivalent current dipole of moment
$p = 4\pi\sigma_0 A$ [A m], and place that dipole at the centre as a pair of
point electrodes — a construction that inherits the correct image treatment from
the machinery already verified in Section 3.1. The result for a source at
$5$ m depth, radius $15$ m:

| body centre (m) | distance/radius | anomaly above the body for $k = 10$ | $k = 100$ | $k = 1000$ |
|---|---|---|---|---|
| $(60, 40)$ | 4.63 | 2.011% | 2.602% | 2.673% |
| $(100, 60)$ | 7.61 | 0.530% | 0.686% | 0.705% |
| $(150, 90)$ | 11.49 | 0.157% | 0.204% | 0.209% |

Read the rows across: from $k = 100$ to $k = 1000$ the anomaly changes by less
than $3\%$ of itself, while from $k = 10$ to $k = 100$ it changes by about
$30\%$. **The response saturates in contrast** because the sphere's induced
moment $A \propto (k-1)/(k+2)$ approaches $a^{3}E_0$ as $k \to \infty$. The
distance/radius column is the variable that matters: the anomaly falls by a
factor $12.8$ over a factor $2.48$ in distance.

### 3.4 The distance–contrast ambiguity, measured

Insist on observing a $0.10\%$ anomaly above the body and ask which contrast
delivers it:

| body centre (m) | distance/radius | saturated anomaly | contrast for the target |
|---|---|---|---|
| $(60, 40)$ | 4.63 | 2.681% | 1.12 |
| $(100, 60)$ | 7.61 | 0.707% | 1.50 |
| $(150, 90)$ | 11.49 | 0.210% | 3.71 |

A factor $2.48$ in distance is compensated by a factor $3.3$ in contrast for the
same observed number. The saturated anomaly itself — the limit of the third
column — depends only on distance and radius:

$$\text{anomaly}_{\text{sat}} \approx \text{function}\left(\frac{d}{a}\right),$$

so **with a single anomaly amplitude the conductivity contrast is not
determined at all**; what is determined is a combination of distance, radius and
(size-dependent) position of the body. Breaking the degeneracy requires the
*shape* of the anomaly pattern — its width and decay with offset — and even that
is weak, exactly as lesson 02 §3.4 found for SP.

### 3.5 The surface array over the same body

A dipole-dipole array on the surface (electrodes at $-a$, $0$, $+a$, $+2a$) over
the same sphere gives:

| spacing $a$ (m) | $\rho_a$ with no body ($\Omega$ m) | $\rho_a$ with the body ($\Omega$ m) | anomaly |
|---|---|---|---|
| 30 | 100.000 | 94.754 | $-5.246\%$ |
| 60 | 100.000 | 96.700 | $-3.300\%$ |
| 120 | 100.000 | 99.302 | $-0.698\%$ |

The no-body column returning exactly $100.000\ \Omega$ m at every spacing is an
internal check of the array code and its geometric factor
$K = -6\pi a$ — the sign follows from the A-B-M-N ordering. The anomaly is
**negative** (a conductor lowers the apparent resistivity) and *falls* with
spacing because the array's sensitivity moves deeper and then past the body. Its
magnitude, a few per cent, is of the same order as the MALM anomaly at a
comparable distance.

The two geometries are complementary rather than redundant. With the source
inside the body, the MALM pattern is *centred on* the body, and its amplitude is
controlled by geometry and not by contrast. With surface electrodes, the array's
response depends on where the current and potential dipoles sit relative to the
body, and it grows without bound as the contrast grows (an array is not
saturated in the same way — its sensitivity is a spatial derivative of the
sphere response). Adding an IP measurement changes the question again: it
measures the polarisability of the body,
[09-03-04](../03-induced-polarisation/04-ip-applications.md), which is
independent of the conductivity contrast to first order and is therefore the
quantity that distinguishes a sulphide body from a conductive clay.

### 3.6 Where the model breaks

Move the source down towards a body centred at $(0, 40)$ m with radius $15$ m and
contrast $100$:

| source depth (m) | distance/radius | modelled anomaly above the body |
|---|---|---|
| 5 | 2.33 | 1.3% |
| 20 | 1.33 | 11.4% |
| 30 | 0.67 | 62.7% |
| 37.5 | 0.17 | 1229.8% |
| 39 | 0.07 | 7987.4% |
| 39.9 | 0.01 | 825 211.7% |

The modelled anomaly diverges as the source approaches the centre, because the
field at the centre diverges as $1/r^{2}$ while the model continues to treat the
sphere as if it sat in a uniform field. At the centre itself the numerical
gradient vanishes — the same singularity seen from the other side. This is not a
numerical artefact to be fixed: it is the statement that **the geometry of
mise-à-la-masse is outside the regime of the polarised-sphere model.** Physically,
current injected into a conductor makes the conductor an *extended electrode* at
one potential; the correct description is the potential field of a body with a
prescribed (nearly constant) surface potential, which is the classic MALM
forward problem and is solved by boundary-element or integral-equation methods.
The first row of the table, at $2.33$ radii, is marginally inside the model's
regime; every other row is not.

## 4. Physical interpretation

- **MALM measures geometry.** Because the contrast saturates, an anomaly is an
  image of a *conductor's position and size*, which is why the method is used to
  map the extent of a body already known from a borehole rather than to discover
  a new one.
- **The electrode's position is the experiment.** Whether the current electrode
  is inside the body, against its wall, or in a borehole beside it changes the
  current distribution qualitatively, and the survey report must state which.
- **Array and MALM responses differ in symmetry.** A surface array's anomaly is
  antisymmetric about the body's centre for a compact conductor (a low over the
  conductor and a high on the flanks), while an energised body gives a
  single-signed high centred on itself. The two together locate the body's centre
  and its edges.
- **Polarisation is the contrast-independent measurement.** IP chargeability
  responds to the body's interface chemistry, which survives where the
  conductivity contrast has saturated.

## 5. Assumptions and regime of validity

1. **A half-space host with an insulating surface**, with the image method used
   for both the electrode and the induced dipole. A layered or laterally varying
   host changes the pattern; the interpretation must be conditioned on a
   conductivity model.
2. **A spherical, homogeneous, isotropic conductor.** Real bodies are
   tabular, elongated or irregular; a sphere is the simplest shape that supports
   an analytic solution and the honest use of it is as a magnitude estimate.
3. **A locally uniform field at the body** (the assumption tested in Section 3.6).
   It requires the source-to-centre distance to exceed a few radii, and it fails
   completely for the defining MALM geometry.
4. **A far-field dipole response**, valid for observation distances much greater
   than the radius; the equivalent-electrode construction used here converges as
   the separation tends to zero.
5. **No induced polarisation of the host** in this model. An IP measurement
   superposes its own response, which is treated in module 09-03.
6. **Steady state, DC.** No induction, no capacitive coupling.
7. **Known current.** The fraction of the injected current that actually enters
   the body is *not* known; it is itself a model parameter. Every anomaly
   percentage in this lesson is therefore an upper-bound-style statement: it
   assumes the modelled geometry and a current known to be delivered to the
   source point, not to the body.
8. **No topography.** A surface with relief refracts current and shifts the
   apparent anomaly; the flat surface is a modelling convenience.

## 6. Units and dimensional analysis

| Quantity | Symbol | Unit | Check |
|---|---|---|---|
| resistivity | $\rho_0$ | $\Omega$ m | |
| conductivity | $\sigma$ | S/m | $\rho = 1/\sigma$ |
| current | $I$ | A | |
| potential | $V$ | V (reported mV) | $\rho I/(2\pi r)$ |
| field | $E_0$ | V/m | $I\rho/(2\pi R^{2})$ |
| sphere potential coefficient | $A$ | V m | $a^{3}[\mathrm{m^3}] \times E_0[\mathrm{V/m}]$ |
| dipole moment | $p = 4\pi\sigma_0 A$ | A m | $\mathrm{S/m}\times\mathrm{V\,m} = \mathrm{A\,m}$ |
| geometric factor | $K = -6\pi a$ | m | $[\mathrm{V}] = K \rho_a I / \text{(m)}$ |

Check the anomaly's dimensionality: it is a ratio of two potentials, so it is
dimensionless and cannot depend on the absolute current — which is why every
percentage in this lesson is independent of $I$. If a computed anomaly changes
when the current is doubled, there is an error in the potential evaluation, not
in the physics.

## 7. Worked examples

### Example 1 — the anomaly of a body from first principles

Body: sphere of radius $a = 15$ m, contrast $k = 100$, host
$\rho_0 = 100\ \Omega$ m, at distance $R = 4.63a$ from a source of $I = 1$ A.

1. Primary field at the centre, from the source at $(0, 5)$ m and the centre at
   $(60, 40)$ m: $R = 69.5$ m, and with the image contribution the field is of
   order $I\rho_0/(2\pi R^{2}) = 100/(2\pi \times 4830) = 3.30\times10^{-3}$ V/m.
2. Sphere coefficient: $A = a^{3}E_0(k-1)/(k+2) = 3375 \times 3.30\times10^{-3}
   \times 99/102 = 10.81$ V m.
3. Equivalent current dipole: $p = 4\pi\sigma_0 A =
   4\pi \times 0.01 \times 10.81 = 1.359$ A m.
4. The surface anomaly is then the ratio of the dipole potential to the primary
   potential at the chosen station, which the demonstration evaluates as
   $2.602\%$ — the table entry for $(60,40)$ at $k = 100$.

The arithmetic above is the demonstration's, step for step, and its last line is
the printed value; the point of the example is that **the anomaly is a ratio of
two computed potentials, with no free parameter.**

### Example 2 — the same number from two different bodies

From Section 3.4, a $0.10\%$ anomaly is produced by contrast $1.12$ at
$4.63$ radii and by contrast $3.71$ at $11.49$ radii. Now ask what the *same*
$0.10\%$ means in absolute terms: the primary potential above the body at
$60$ m horizontal offset and $40$ m depth from the source is

$$V_{\text{prim}} = \frac{100 \times 1}{2\pi\sqrt{60^{2}+35^{2}}}
= \frac{100}{2\pi\times69.46} = 0.229\ \mathrm{V},$$

so $0.10\%$ is $0.23$ mV — comparable to the per-station noise of a careful SP
survey. Hence the practical depth/offset limit of the method: a $\sim0.1$ mV
anomaly is at the edge of what a DC measurement can resolve, and both bodies of
this example sit there together, indistinguishable.

### Example 3 — why an IP measurement is added

The conductivity contrast saturates (Section 3.3), so no increase in contrast
makes a buried body more visible beyond $k \sim 100$. The IP response, by
contrast, scales with the body's *chargeability* $m_b$, which is a property of
its interface chemistry and not of the contrast. For a body occupying a fraction
$f$ of the current path, the apparent chargeability is of order
$M_a \approx f\,m_b$; with $f = 0.2$ (the pathway share of
[09-03-04](../03-induced-polarisation/04-ip-applications.md) §3.1) and
$m_b = 0.05$, $M_a \approx 0.01 = 10$ mV/V, which is a large, easily measured IP
anomaly. **That is the quantitative reason a MALM survey is normally accompanied
by an IP survey**: the conductivity contrast has stopped carrying information
while the polarisability has not.

## 8. Python demonstration

`code/mise_a_la_masse_demo.py` prints every number in this lesson. It:

1. computes the surface field of a buried point electrode, verifies it against
   $\rho I/(2\pi r)$, prints the apparent-resistivity identity and checks the
   FWHM rule ($3.4640$ against $3.4641$);
2. verifies both boundary conditions of the conducting-sphere solution at six
   angles, plus the $k=1$ and $k \to \infty$ limits;
3. tabulates the surface anomaly against body position and contrast, showing the
   saturation;
4. solves for the contrast that produces a fixed $0.10\%$ anomaly at three
   distances and reports the degeneracy;
5. demonstrates the divergence of the locally-uniform-field model as the source
   approaches the body centre, with the validity ratio printed for every row;
6. computes a dipole-dipole array response over the same body, checking the
   no-body column against the true resistivity and reporting the anomaly at three
   spacings.

Run it with the project virtual environment:

```bash
cd 09-electrical-em-methods/04-self-potential-and-mise-a-la-masse/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python mise_a_la_masse_demo.py
```

## 9. Exercises

Full sets with worked solutions are in
[`exercises/03-mise-a-la-masse-exercises.md`](./exercises/03-mise-a-la-masse-exercises.md)
and
[`exercises/03-mise-a-la-masse-solutions.md`](./exercises/03-mise-a-la-masse-solutions.md).

- **★** Compute the half-space potential at $x = 0$ and $x = 100$ m for a
  $1$ A electrode at $60$ m depth in a host of $50\ \Omega$ m.
- **★** State the values of $A$ in the limits $k = 1$ and $k\to\infty$, and what
  each means physically.
- **★★** Derive $A = a^{3}E_0(k-1)/(k+2)$ from the two boundary conditions,
  showing each step.
- **★★** Using the saturation table, explain why doubling the conductivity
  contrast of a well-conducting body changes its MALM anomaly by less than $3\%$,
  while the surface array's anomaly grows with contrast.
- **★★★** Design a field procedure that separates a body at $4.6$ radii with
  contrast $1.1$ from one at $11.5$ radii with contrast $3.7$, both giving the
  same $0.10\%$ anomaly. State the electrode geometry, the stations, and the
  statistic.

## 10. Common mistakes

1. **Reading an anomaly as a conductivity.** The response saturates, so the
   amplitude measures distance and size, not contrast.
2. **Ignoring the electrode's position.** Whether the current electrode is inside
   the body or beside it changes the current distribution qualitatively; the
   geometry is part of the measurement.
3. **Using the polarised-sphere model with the source inside the body.** Section
   3.6 shows the modelled anomaly diverging by four orders of magnitude; the
   correct model there is an equipotential body.
4. **Assuming the injected current enters the body.** The fraction that does is
   an unknown; anomalies are upper bounds unless the current path is
   constrained.
5. **Comparing a MALM anomaly directly with an array anomaly.** Their geometries
   and symmetries differ; a $-5\%$ array anomaly and a $+2.7\%$ MALM anomaly are
   not the same measurement of the same thing.
6. **Forgetting that IP measures something else.** After the contrast saturates,
   only the polarisability continues to discriminate.

## 11. Real-world applications

- **Ore-body delineation.** A borehole intersection of a sulphide body is
  energised and the surface pattern is mapped to outline the body's extent; the
  method's classical use.
- **Continuity between boreholes.** The same construction tests whether a
  conductor seen in one hole is connected to a conductor in another, which is
  often the decisive question in a resource evaluation.
- **Groundwater and geothermal systems.** A conductive fluid-filled fracture can
  be energised from a borehole to map its direction and persistence.
- **Combined surveys.** MALM plus IP plus resistivity is the standard
  three-measurement package over a known conductor, exploiting the fact that each
  saturates at a different question.

## 12. Further reading

- **Telford, W. M., Geldart, L. P., & Sheriff, R. E., *Applied Geophysics*
  (2nd ed., Cambridge University Press).** Level: textbook. The classical
  treatment of mise-à-la-masse and of the conducting-sphere solution.
- **Reynolds, J. M., *An Introduction to Applied and Environmental
  Geophysics* (2nd ed., Wiley-Blackwell).** Level: textbook. Field procedure and
  case histories.
- **Sumner, J. S., *Principles of Induced Polarization for Geophysical
  Exploration* (Elsevier).** Level: research monograph. The combination of MALM
  with IP, which is standard practice.
- **Revil, A., & Jardani, A., *The Self-Potential Method: Theory and
  Applications in Environmental Geosciences* (Cambridge University Press).**
  Level: research monograph. Useful for the general potential-field framing.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. **No number in this lesson is
> quoted from any of them**: every figure is printed by
> [`code/mise_a_la_masse_demo.py`](./code/mise_a_la_masse_demo.py), or derived
> from the analytic solution in Section 3.2.

## 13. Related lessons

- [01 Sources of Self-Potential: Electrokinetic, Electrochemical](01-self-potential-sources.md) —
  the passive potential field of the same half-space.
- [02 SP for Seepage, Dams, Landfills and Mineralisation](02-sp-applications.md) —
  what a passive survey can and cannot resolve.
- [09-02-03 Apparent Resistivity and Geometric Factors](../02-dc-resistivity/03-apparent-resistivity.md) —
  the array measurement used for comparison in Section 3.5.
- [09-03-04 IP for Sulphides, Clays, Contaminants and Permafrost](../03-induced-polarisation/04-ip-applications.md) —
  the polarisation measurement that survives the conductivity saturation.
- [09-02-06 Forward Modelling Resistivity Data](../02-dc-resistivity/06-resistivity-forward-modelling.md) —
  the numerical machinery needed for the equipotential-body problem of
  Section 3.6.

## 14. Self-assessment checklist

- [ ] I can derive the half-space potential of a buried electrode and verify the
      apparent-resistivity identity.
- [ ] I can derive the conducting-sphere coefficient $A$ and check both boundary
      conditions.
- [ ] I can explain the contrast saturation from $A \to a^{3}E_0$.
- [ ] I can quantify the distance–contrast degeneracy.
- [ ] I can state the regime of validity and explain what model replaces it when
      the electrode is inside the body.
- [ ] I can compare a MALM and an array response over the same body and say what
      each measures.
- [ ] I can explain, quantitatively, why an IP measurement is added.
