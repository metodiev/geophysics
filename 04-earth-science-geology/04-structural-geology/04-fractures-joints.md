---
id: 04-04-04
title: "Fractures, Joints and Their Geophysical Signature"
level: advanced
prereqs: ["04-04-01", "02-04-06"]
estimated_minutes: 105
tags: [fractures, joints, fracture-mechanics, anisotropy, shear-wave-splitting]
---

# Fractures, Joints and Their Geophysical Signature

A fracture is a mechanical object at the scale of a hand specimen and a
continuum property at the scale of a seismic wave. The bridge between those two
scales is the reason this lesson exists, and it is the reason **seismic
anisotropy exists**: aligned fractures make a rock compliant in one direction and
stiff in the others, which makes waves travel at different speeds in different
directions, which is measurable from the surface.

That chain — fracture mechanics to fracture statistics to an effective medium to
a measurable velocity difference — is what this lesson builds. Each link has its
own assumptions and its own regime of validity, and the failure of any one link
breaks the inference. A joint set whose apertures are not measured cannot be
inverted for permeability from a seismic velocity. A fracture density inferred
from anisotropy depends on a stiffness assumed, not measured. Keeping the links
separate is the skill.

## Learning objectives

By the end of this lesson you will be able to:

1. **Apply** the Griffith energy balance and the stress-intensity criterion to a
   flaw, and show that they are the same statement written twice.
2. **State** how the critical stress scales with flaw length, and why a measured
   laboratory strength exceeds the Griffith prediction.
3. **Fit** joint spacing against layer thickness, and state honestly what kind of
   relation it is and what its constant depends on.
4. **Compute** the coefficient of variation of a spacing distribution and explain
   what it does and does not indicate.
5. **Derive** the dimensionless normal and shear compliances of a fracture set
   from its stiffness and spacing, including the units.
6. **Build** the effective stiffness tensor of a fractured medium, verify that zero
   fracture compliance returns the isotropic background, and compute the resulting
   P- and S-wave velocities.
7. **Compute** Thomsen's anisotropy parameters and the shear-wave splitting delay
   over a stated path, and verify two of them against closed forms.
8. **State** why the cubic law makes fracture permeability dominated by the
   largest apertures, and why core measurements cannot be extrapolated to a
   reservoir.

## Prerequisites

- [01 Stress, Strain and Brittle vs Ductile Deformation](./01-stress-strain-rocks.md)
  — the brittle regime, effective stress and the Coulomb criterion.
- [02-04-06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)
  — the stiffness tensor and its symmetries, assumed known.
- [01-15-05 Representing Anisotropy: Voigt Notation and Symmetry Classes](../../01-mathematics/15-tensors-and-differential-geometry/05-anisotropy-representation.md)
  — the Voigt notation used in §5 and §6.
- [05-04-05 Anisotropy in Rocks: Causes and Magnitudes](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md)
  — the petrophysical context; this lesson supplies the fracture-specific
  mechanics.

## 1. Fracture mechanics: when does a flaw grow?

Rock in tension fails at a stress far below its theoretical strength, and the
reason is that it contains flaws. **Griffith's energy balance** states that a
crack grows when the elastic energy released by its growth exceeds the energy
required to create the new surfaces:

$$\sigma_c = \sqrt{\frac{2E\gamma_s}{\pi a}}, \tag{1}$$

with $E$ the Young's modulus, $\gamma_s$ the specific surface energy, and $a$ the
half-length of the flaw. Equivalently, and more usefully in practice, define the
**stress intensity factor** $K_I = \sigma\sqrt{\pi a}$; failure occurs when $K_I$
reaches the **fracture toughness** $K_{Ic}$. The two statements are related by
$K_{Ic} = \sqrt{2E\gamma_s}$.

The demo evaluates equation (1) over a range of flaw sizes:

```text
 flaw half-length a   sigma_c Griffith (MPa)   K_I at sigma_c (MPa m^0.5)
               0.001 m                    17.84                       1.0000
                0.01 m                     5.64                       1.0000
                 0.1 m                     1.78                       1.0000
                   1 m                     0.56                       1.0000
                  10 m                     0.18                       1.0000
```

The third column is **constant**, which is the whole point: the two criteria are
one statement in two notations, and reading it as a coincidence would miss the
structure. The scaling is what matters operationally:

- doubling the flaw length reduces the strength by $\sqrt2 = 1.414$;
- a factor of 100 in flaw length is a factor of 10 in strength.

Running the arithmetic backwards gives the size of flaw that grows at a stated
stress: from $K_{Ic} = 1.5$ MPa m$^{0.5}$ alone, a flaw of half-length 7.16 mm
grows at a remote tension of 10 MPa. That number is why a rock-mechanics
laboratory measures flaw populations rather than strengths, and why strength is
scale-dependent: a larger specimen is more likely to contain a larger flaw.

The honest caveat: the surface energy used above is a stated value, and it gives
$K_{Ic} = 1.000$ MPa m$^{0.5}$, which is **smaller than the tabulated toughness of
1.50** MPa m$^{0.5}$ used for the critical-flaw calculation. Real rock has a
microcrack process zone at the tip, so the measured toughness exceeds
$\sqrt{2E\gamma_s}$ computed from the surface energy alone. That gap is not an
inconsistency; it is the reason a quoted toughness is tied to a specimen size and
a test method.

## 2. Joint spacing: an empirical relation, labelled as one

The most widely used relation in fractured-reservoir description is that joint
spacing scales with layer thickness. The demo fits a synthetic data set
constructed with a slope of 0.80 and 0.12 m of noise:

```text
  least-squares fit: spacing = 0.8254 * thickness + -0.0226 m
  slope 0.8254 against the 0.80 used to construct the data (+3.18%)
  r^2 = 0.9916; rms residual 0.1196 m
  the spacing/thickness ratio ranges from 0.517 to 1.023
```

The fit recovers the input, and the last line is the more important one. **A
single spacing-to-thickness ratio is not a description of the data**, because the
ratio ranges over a factor of two in a data set whose trend is nearly perfect.
Reporting "spacing is about 0.8 times the thickness" hides a scatter that matters
as soon as the number is used for anything.

And the relation is **empirical**. Its mechanical explanation — that a layer stops
cracking when the stress transferred to the interface can no longer break the next
site — predicts a proportionality, not a value. The constant depends on the
formation, the loading history and the stiffness contrast between the layer and
its neighbours. That makes it exactly the kind of relation that has to be
calibrated locally and quoted with the calibration, and it makes it a
well-behaved example of a broader lesson: **a relation with a mechanism behind its
form and a calibration behind its constant is not a law.**

## 3. Spacing statistics: what a coefficient of variation means

Spacing distributions are characterised by their mean and by their coefficient of
variation $C_v = \sigma/\mu$. The demo compares three synthetic populations:

```text
      population   mean spacing (m)    std (m)      Cv   spacings per metre
  regular (clustered-free)             0.9947     0.0461   0.046               1.0053
  random (Poisson)             0.9799     0.9271   0.946               1.0205
       clustered             0.9996     0.7481   0.748               1.0004
```

The convention is that $C_v$ below about 0.5 indicates a **saturated** set — one
that has stopped growing because the spacing reached a mechanical limit. That
reading is a convention, not a measurement, and what it cannot do is distinguish a
saturated set from one whose spacing was inherited from the depositional fabric.
Spacing alone cannot make that distinction, and no field measurement of spacing
will.

Where the distribution does earn its place is in any calculation that depends on
**connectivity** rather than on density. Same mean spacing, different statistics,
different intact fraction of a scanline:

```text
 scanline (m)   Poisson: exp(-L/s)   regular: 1-L/s
          0.5              0.6065          0.5000
          1.0              0.3679          0.0000
          2.0              0.1353          0.0000
          4.0              0.0183          0.0000
```

For the same nominal spacing, a random set continuously samples intact rock at
long scanline lengths while a perfectly regular set has none. Permeability, block
size and rock-mass strength all depend on which is true, and all of them are
wrong if the mean is used in place of the distribution.

## 4. From fractures to an effective medium: the compliances

A set of fractures is treated as a set of compliant planes. A stack of fractures
each with normal stiffness $k_n$ (units Pa m$^{-1}$) and spacing $s$ (m) adds a
normal compliance to the medium, because the fracture strains add in series:

$$\Delta S_{NN} = \frac{1}{k_n s}. \tag{2}$$

Normalising by the background compliance $1/c_{11}$ gives the dimensionless
**excess compliances**

$$Z_N = \frac{c_{11}}{k_n s}, \qquad Z_T = \frac{c_{11}}{k_t s}. \tag{3}$$

The units are the reason to derive this rather than quote it: $c_{11}$ is in Pa and
$k_n s$ is in Pa, so $Z_N$ is dimensionless, and a formula that fails that check is
wrong. The demo prints them:

```text
spacing (m)       Z_N       Z_T   Vp(v) m/s   Vp(h) m/s  Vs(vh) m/s   Vs(h) m/s  Vp anisotropy
       20.0   0.06000   0.15000     4,639.7     4,785.9     2,586.3     2,773.5        -3.054%
        5.0   0.24000   0.60000     4,232.8     4,743.8     2,192.6     2,773.5       -10.771%
        1.0   1.20000   3.00000     3,075.3     4,643.7     1,386.8     2,773.5       -33.773%
```

## 5. The effective stiffness, and two exact checks

For fractures with normals along the vertical axis (horizontal fractures, giving a
VTI medium), the excess compliance sits only on the $S_{33}$, $S_{44}$ and
$S_{55}$ terms. The effective compliance is inverted to give the effective
stiffness, and the velocities follow. Three checks are performed.

**Zero fracture compliance returns the background exactly.** With a fracture
stiffness of $10^{30}$ Pa m$^{-1}$, so that the excess compliance is negligible
rather than notional:

```text
    Z_N = 6.000e-20, Z_T = 6.000e-20 -> Vp(vertical) = 4803.844614 m/s,
    Vp(horizontal) = 4803.844614 m/s, Vs(vh) = 2773.500981 m/s, Vs(h) = 2773.500981 m/s
    anisotropy: Vp(v)/Vp(h) - 1 = +2.220e-16, S splitting = +0.000e+00
```

The background P velocity is 4803.8 m/s and the S velocity 2773.5 m/s, and the
anisotropy is at the round-off floor. Any error in the tensor bookkeeping would
show up here as a spurious anisotropy in an unfractured rock.

**The anisotropy grows with fracture density and vanishes with spacing.** Reading
down the table of §4: at 100 m spacing the P anisotropy is $-0.63$ per cent, at
10 m it is $-5.85$ per cent, at 1 m it is $-33.8$ per cent. The sign is the
physics: $V_p$ is **reduced normal to the fractures and unchanged within the
fracture plane**, so a horizontal fracture set lowers the vertical velocity. That
is what "a compliant direction" means, and it is why anisotropy is not a curiosity
but a measurement — it is the only remote observable of aligned fracture
compliance.

**Two quantities have exact closed forms.** Because $C_{66}$ is untouched while
$C_{44}$ is reduced, the Thomsen $\gamma$ and the shear-wave splitting are known
analytically:

```text
spacing (m)       Z_T   gamma exact  gamma computed   split exact (ms/m)  split computed
       20.0    0.1500      0.075000        0.075000             0.026097        0.026097
        5.0    0.6000      0.300000        0.300000             0.095515        0.095515
        2.0    1.5000      0.750000        0.750000             0.209533        0.209533
```

**$\gamma = Z_T/2$ exactly**, and the splitting follows from
$1/V_{S}^{\text{fast}} - 1/V_{S}^{\text{slow}} = (\sqrt{1 + Z_T} - 1)/V_{S,0}$.
The agreement to six decimals between the numerical effective-medium calculation
and the closed forms is the evidence that the excess compliance is being placed on
the right tensor components.

The Thomsen parameters of the resulting medium:

```text
spacing (m)    epsilon      gamma      delta   split (ms/m)  delay over 1 km (ms)
       20.0    0.03200    0.07500   -0.04373       0.026097                26.097
        5.0    0.12800    0.30000   -0.11845       0.095515                95.515
```

$\varepsilon$ measures the fractional difference between horizontal and vertical P
velocity, $\gamma$ the shear-wave splitting, and $\delta$ the near-vertical P
behaviour. For a **single set of horizontal fractures both $\varepsilon$ and
$\gamma$ are positive**: the medium is stiffer along the fracture plane than across
it. A set of **vertical** fractures measured in a vertical well gives the opposite
sign, and that sign flip is the single most useful thing a crossed-dipole sonic
log reports — a fast shear direction that changes with azimuth is a direct
measurement of fracture orientation. Note also that **$\delta$ cannot be measured
from P velocities along the axes alone**, which is why it carries the largest
uncertainty of the three in any real dataset.

## 6. Fracture permeability: why the aperture distribution dominates

For a set of parallel planar fractures with aperture $b$ and spacing $s$, the
permeability along the fracture plane is

$$k = \frac{b^3}{12s}, \tag{4}$$

the cubic law for a slot divided by the number of fractures per unit length. The
demo evaluates it:

```text
 aperture (mm)  spacing (m)   k parallel (m^2)   k parallel (darcy)
             0.10         1.00          8.333e-14               0.0844
             0.50         1.00          1.042e-11              10.5547
             1.00         1.00          8.333e-11              84.4375
```

**The aperture enters as its cube.** Doubling the aperture multiplies the
permeability by eight; halving it divides it by eight. Two consequences follow, and
they are the reason this section exists. Fracture permeability is dominated by the
few largest apertures, so a mean aperture is close to meaningless. And a core-scale
measurement cannot be extrapolated to a reservoir, because the transport is
carried by the part of the aperture distribution that a core is least likely to
sample.

The anisotropy that goes with it, with the intact rock permeability taken as
$10^{-15}$ m²:

```text
    aperture 0.1 mm, spacing 1.0 m: k_parallel/k_perpendicular = 84.3
    aperture 0.5 mm, spacing 1.0 m: k_parallel/k_perpendicular = 10,417.7
    aperture 0.5 mm, spacing 0.1 m: k_parallel/k_perpendicular = 104,167.7
```

Ratios of one to five orders of magnitude are ordinary. This is the same geometric
reason as the seismic anisotropy of §4: a set of aligned compliant planes
transmits differently along and across itself. **Seismic anisotropy and
permeability anisotropy are two projections of the same fracture fabric**, which is
why joint orientation is mapped before either is interpreted — and why neither can
be inverted for the other without additional information.

## 7. Assumptions and regime of validity

- **An elliptical or penny-shaped crack in an infinite elastic body** is assumed in
  §1. Finite specimens, interaction between cracks and crack-face friction all
  change the stress intensity.
- **The surface energy is a stated constant.** It is a material property that
  varies, and its relation to the measured toughness includes the process zone.
- **The spacing-thickness relation is empirical.** Its constant is a local
  calibration, as §2 states.
- **The linear-slip model of §4 is a long-wavelength approximation.** It is valid
  when the seismic wavelength is much greater than the fracture spacing, which at
  seismic frequencies is usually satisfied and at ultrasonic frequencies in a
  laboratory specimen usually is not. This is the single most common misapplication
  of the model.
- **The fracture stiffnesses are assumed.** $k_n$ and $k_t$ are hard to measure in
  situ and vary with aperture, roughness and infill. An anisotropy-derived fracture
  density is therefore a density for a stated stiffness, not an absolute density.
- **Fractures are assumed to be aligned and planar, with no interaction.** Natural
  sets have orientation dispersion, and multiple sets give an orthorhombic rather
  than a VTI medium.
- **The cubic law assumes laminar flow between smooth parallel plates.** Natural
  fractures are rough and may be channeled, which can change the effective
  permeability by an order of magnitude in either direction.

## 8. Python demonstration

[`code/04-fractures_joints_demo.py`](./code/04-fractures_joints_demo.py) computes
the Griffith and Irwin criteria, fits the spacing-thickness relation, computes the
spacing statistics and connectivity, builds the effective stiffness tensor of a
fractured medium with its three checks, computes the Thomsen parameters and the
shear-wave splitting, and evaluates the cubic law. Its output is quoted in §1 to
§6.

The three verifications worth running yourself: the constant $K_I$ column in §1,
the exact isotropic background in §5, and the agreement of $\gamma$ with $Z_T/2$.

```bash
cd 04-earth-science-geology/04-structural-geology/code
.venv/bin/python 04-fractures_joints_demo.py
```

All material parameters are labelled TABULATED or TYPICAL, the spacing data set is
SYNTHETIC, and the script prints those labels.

## 9. Common mistakes

1. **Quoting a laboratory strength as a rock property.** It is a property of a
   specimen containing a flaw population, and it is scale-dependent.
2. **Treating the spacing-thickness relation as a law.** It is a local
   calibration with a mechanism behind its form.
3. **Reporting a mean spacing with no distribution.** Connectivity and block size
   depend on the distribution.
4. **Reading $C_v < 0.5$ as proof of saturation.** It is a convention, and it
   cannot distinguish saturation from an inherited fabric.
5. **Applying the linear-slip effective medium at ultrasonic frequencies in a
   small specimen.** The long-wavelength condition fails.
6. **Inverting anisotropy for fracture density without stating the stiffness
   assumed.** The answer changes when the stiffness does.
7. **Using a mean aperture in the cubic law.** The cube makes the largest
   apertures dominate.
8. **Extrapolating a core permeability to a reservoir.** The transport is carried
   by what the core did not sample.
9. **Confusing the sign of the P-wave anisotropy.** Horizontal fractures lower the
   vertical velocity; vertical fractures lower the horizontal one in the direction
   normal to them.
10. **Assuming a single fracture set.** Two or more sets give orthorhombic
    symmetry, and a VTI analysis of an orthorhombic medium gives wrong parameters.

## 10. Real-world applications

- **Fractured-reservoir characterisation.** Fracture density, orientation and
  aperture control permeability, and the orientation is measured from seismic
  anisotropy and image logs
  ([04-06-01 Source, Reservoir, Seal and Trap: The Petroleum System](../06-petroleum-and-mineral-systems/01-petroleum-system.md)).
- **Shear-wave splitting as a stress and fabric monitor.** Splitting in the
  crust and mantle is one of the few remote measurements of aligned fabric, and
  its temporal variation is used to monitor stress change
  ([06-08 Receiver Functions and Crustal Structure](../../06-seismology/08-receiver-functions-and-crustal-structure/README.md)).
- **Seismic anisotropy correction in imaging.** Ignoring anisotropy mispositions
  reflectors, and the size of the error grows with offset and depth
  ([06-09-04 Migration and Imaging: Time vs Depth, Kirchhoff and RTM](../../06-seismology/09-reflection-seismology/04-migration-imaging.md)).
- **Geothermal reservoir stimulation.** Whether a stimulation creates a connected
  fracture network depends on the orientation of the pre-existing fabric relative
  to the stress field ([04-06-03 Geothermal Systems, Heat Flow and Resource Assessment](../06-petroleum-and-mineral-systems/03-geothermal-systems.md)).
- **Rock-mass characterisation for engineering.** Block size and intact fraction,
  which come from the spacing distribution, set the strength and deformability of
  a rock mass ([04-07-03 Landslides, Slope Stability and Geotechnical Geophysics](../07-geologic-hazards/03-landslides.md)).
- **Groundwater flow in fractured rock.** The cubic law with a realistic aperture
  distribution is the basis of any fractured-aquifer model
  ([04-06-04 Aquifer Types and Groundwater Occurrence](../06-petroleum-and-mineral-systems/04-groundwater-aquifers.md)).

## 11. Further reading

- **Griffith, A. A. (1920). The phenomena of rupture and flow in solids.
  *Philosophical Transactions of the Royal Society A* 221, 163–198.** The energy
  balance of §1, and the origin of fracture mechanics. Level: advanced.
- **Hudson, J. A. (1981). Wave speeds and attenuation of elastic waves in material
  containing cracks. *Geophysical Journal of the Royal Astronomical Society* 64,
  133–150.** The crack-density effective-medium formulation, and one of the two
  standard routes to §4 and §5. Level: doctoral.
- **Schoenberg, M., & Sayers, C. M. (1995). Seismic anisotropy of fractured rock.
  *Geophysics* 60, 204–211.** The linear-slip formulation used here, with the
  compliance relations of §4. Level: doctoral.
- **Thomsen, L. (1986). Weak elastic anisotropy. *Geophysics* 51, 1954–1966.**
  The definition of the parameters used in §5, and the assumptions behind them.
  Level: advanced.
- **Jaeger, J. C., Cook, N. G. W., & Zimmerman, R. W. *Fundamentals of Rock
  Mechanics* (Wiley-Blackwell).** The fracture mechanics and the flow laws in
  fuller form. Level: advanced.
- **Nelson, R. A. *Geologic Analysis of Naturally Fractured Reservoirs*
  (Gulf Professional Publishing).** The geological and engineering practice of
  fracture description, with the statistics of §2 and §3 in use. Level:
  intermediate to advanced.
- **Priest, S. D. *Discontinuity Analysis for Rock Engineering* (Chapman & Hall).**
  The spacing statistics of §3 and their use in engineering classification.
  Level: advanced.

> Note on citations: bibliographic details are given so that you can locate the
> works. This repository does not host or reproduce copyrighted text; confirm
> editions and availability through your library before citing them yourself.

## 12. Related lessons

- [01 Stress, Strain and Brittle vs Ductile Deformation](./01-stress-strain-rocks.md)
  — the brittle regime in which fractures form, and the effective stress that
  controls it.
- [02 Fault Geometry, Kinematics and Fault Classification](./02-faults.md) — the
  large-scale shear fractures that joints and veins accompany.
- [03 Fold Geometry, Mechanisms and Interpretation](./03-folds.md) — the
  deformation that produces the fabrics that are the other main source of
  anisotropy.
- [05 Reading Geological Maps and Constructing Cross-Sections](./05-geologic-maps-sections.md)
  — mapping the fracture sets whose orientation the anisotropy measures.
- [02-04-06 Anisotropic Elasticity (VTI, HTI, Orthorhombic)](../../02-physics/04-elasticity-and-continuum-mechanics/06-anisotropic-elasticity.md)
  — the stiffness tensor and the symmetry classes.
- [05-04-05 Anisotropy in Rocks: Causes and Magnitudes](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md)
  — the petrophysical measurement of the same anisotropy.
- [06-01-08 Wave Propagation in Anisotropic Media](../../06-seismology/01-elastic-wave-propagation/08-anisotropic-propagation.md)
  — how the effective stiffness of this lesson governs wave propagation.

Exercises:
[`exercises/04-fractures-joints-exercises.md`](./exercises/04-fractures-joints-exercises.md)
and
[`exercises/04-fractures-joints-solutions.md`](./exercises/04-fractures-joints-solutions.md).

## Self-assessment checklist

- [ ] I can apply both the energy and the stress-intensity criteria to a flaw and
      say why they are the same statement. (§1)
- [ ] I can compute the critical flaw size at a stated stress and explain the
      scale dependence of strength. (§1)
- [ ] I can fit a spacing-thickness relation, report its scatter, and state what
      kind of relation it is. (§2)
- [ ] I can compute $C_v$ and say what it does not indicate. (§3)
- [ ] I can explain why the intact fraction of a scanline depends on the spacing
      distribution and not only on its mean. (§3)
- [ ] I can derive $Z_N$ and $Z_T$ from a fracture stiffness and spacing, and check
      the units. (§4)
- [ ] I can verify that zero fracture compliance returns the isotropic background.
      (§5)
- [ ] I can compute Thomsen's parameters and the shear-wave splitting delay over a
      path, and check $\gamma$ against $Z_T/2$. (§5)
- [ ] I can predict the sign of the P-wave anisotropy for horizontal and for
      vertical fracture sets. (§5)
- [ ] I can explain why fracture permeability is dominated by the largest
      apertures and why core measurements cannot be extrapolated. (§6)
- [ ] I can list the assumptions of the linear-slip effective medium and the
      regime in which each fails. (§7)
