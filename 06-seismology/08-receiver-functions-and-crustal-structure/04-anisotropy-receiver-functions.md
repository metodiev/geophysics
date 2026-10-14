---
id: 06-08-04
title: "Anisotropy from Receiver Functions and Shear-Wave Splitting"
level: doctoral
prereqs: ["06-08-01", "06-01-08"]
tags: [seismology, anisotropy, receiver-functions, shear-wave-splitting, transverse-component]
---

# Anisotropy from Receiver Functions and Shear-Wave Splitting

## Learning objectives

By the end of this lesson you will be able to:

1. **Explain** why a P-to-S conversion in an anisotropic layer puts energy on the
   *transverse* component and why an isotropic, horizontally layered Earth puts
   none there.
2. **Derive** the shear-wave splitting delay
   $\delta t = L(1/v_{\text{slow}} - 1/v_{\text{fast}})$ and its small-anisotropy
   limit $\delta t \approx 2\gamma L/v_s$.
3. **Recognise** the $180^\circ$-periodic (two-lobed) back-azimuthal signature of
   anisotropy, and the $360^\circ$ term that a dipping interface adds.
4. **Demonstrate**, using a design-matrix condition number, that a single station
   with a clustered back-azimuthal distribution cannot separate anisotropy from
   dip.
5. **Quantify** the fundamental trade-off between layer thickness and anisotropy
   percentage for a given splitting delay.
6. **State** what a single station can and cannot claim, without overclaiming.

## Prerequisites

- [01 Receiver Functions: Deconvolution and Ps Conversions](01-receiver-function-principle.md).
- [06-01-08 Anisotropic Wave Propagation](../01-elastic-wave-propagation/08-anisotropic-propagation.md) —
  hexagonal (transversely isotropic) symmetry and the fast/slow shear speeds.

## 1. Intuition: the transverse component is the tell-tale

For an isotropic, horizontally layered Earth beneath a station, the P-to-S
conversion at each interface is polarized in the vertical plane containing the
ray. With the radial direction defined along the ray's back-azimuth, **all the
converted energy appears on the radial component, and none on the transverse
component.** The transverse component is a null channel.

Anything that appears on the transverse component is therefore evidence of a
break in that symmetry: an anisotropic layer, a dipping interface, or a
scattering body. Anisotropy is the most common explanation, and it is also the
most over-claimed. This lesson develops both sides: the physical signature and
the ambiguity.

The physical picture for anisotropy is a *race between two shear waves*. In a
hexagonally symmetric rock, a shear wave splits into a fast and a slow
polarisation. A conversion that enters the anisotropic layer as a single pulse
leaves it as two pulses separated by a delay that grows with the layer thickness
and the strength of the anisotropy. The two pulses are polarised differently, so
their interference is recorded as a signal whose amplitude depends on the
back-azimuth of the incoming ray.

## 2. Precise definitions

### 2.1 Hexagonal anisotropy and the shear speeds

For weak hexagonal anisotropy with a horizontal symmetry (fast) axis, the two
shear polarisations travel at

$$v_{\text{fast}} = v_s(1+\gamma), \qquad v_{\text{slow}} = v_s(1-\gamma),$$

where $v_s$ is the isotropic average speed and $\gamma$ is the **shear
anisotropy** (dimensionless; often quoted in per cent). The two polarisations are
orthogonal: one is aligned with the fast axis, the other perpendicular to it.

### 2.2 The transverse receiver function

Decompose the horizontal components into radial (R) and transverse (T) using the
event back-azimuth $\varphi$. The **transverse receiver function** is the
deconvolution of T by the vertical. For symmetric structure it is zero; for
anisotropy or dip it is not.

### 2.3 Shear-wave splitting delay

The delay between the fast and slow arrivals after crossing the layer is

$$\delta t = L\left(\frac{1}{v_{\text{slow}}}-\frac{1}{v_{\text{fast}}}\right),$$

with $L$ the path length in the layer (the layer thickness for a near-vertical
ray).

## 3. Derivations

### 3.1 Splitting delay and its small-anisotropy limit

Substitute the two speeds:

$$\delta t = L\left(\frac{1}{v_s(1-\gamma)}-\frac{1}{v_s(1+\gamma)}\right)
= \frac{L}{v_s}\left(\frac{1+\gamma-(1-\gamma)}{1-\gamma^{2}}\right)
= \frac{2\gamma L}{v_s\left(1-\gamma^{2}\right)}.$$

For $\gamma \ll 1$, $(1-\gamma^2)\to 1$ and

$$\boxed{\;\delta t \approx \frac{2\gamma L}{v_s}.}$$

*Numerical check (SYNTHETIC).* With $v_s = 3.60\ \mathrm{km\,s^{-1}}$,
$\gamma = 0.040$, $L = 35.0\ \mathrm{km}$:

$$v_{\text{fast}} = 3.744,\quad v_{\text{slow}} = 3.456
\ \mathrm{km\,s^{-1}},$$
$$\delta t = 35.0\left(\frac{1}{3.456}-\frac{1}{3.744}\right)
= 35.0\,(0.289352-0.267094) = 0.779\ \mathrm{s}.$$

The approximation gives $2(0.040)(35.0)/3.60 = 0.778\ \mathrm{s}$ — agreement to
$0.1\%$, as expected for $\gamma=4\%$ since $(1-\gamma^{2}) = 0.9984$.

**The degeneracy.** The small-anisotropy relation shows $\delta t$ involves the
*product* $\gamma L$. Doubling the layer and halving $\gamma$ leaves the splitting delay
unchanged: the demonstration confirms $L = 70\ \mathrm{km}$, $\gamma = 2\%$ gives
$0.778\ \mathrm{s}$, matching $L = 35\ \mathrm{km}$, $\gamma = 4\%$ to three
decimals. A single splitting measurement therefore **cannot** give both thickness
and anisotropy.

### 3.2 Why the transverse amplitude is $180^\circ$-periodic

Represent the incoming S polarisation as a unit vector at angle $\alpha$ to the
fast axis. Decompose onto the fast and slow axes: the components are
$\cos\alpha$ and $\sin\alpha$. After the layer, the fast component has advanced
by one phase and the slow has lagged; at the observation level the two are
recombined. The transverse amplitude after recombination has the form

$$A_T(\varphi) = A_0\,\sin\!\big(2(\varphi-\varphi_{\text{fast}})\big),$$

where $\varphi$ is the back-azimuth and $\varphi_{\text{fast}}$ the azimuth of the
fast axis. The factor $\sin 2(\cdot)$ is the mathematical statement of the
two-lobed pattern:

- It is zero when the polarisation is aligned with either the fast or the slow
  axis — no splitting of the *transverse* projection occurs there.
- It is maximum at $45^\circ$ to the fast axis.
- It is **invariant under $\varphi \to \varphi + 180^\circ$**: the signature
  repeats twice per full turn.

*Numerical check.* With $A_0 = 0.08$ and $\varphi_{\text{fast}} = 30^\circ$, the
demonstration prints $A_T = 0$ at $30^\circ$ and $120^\circ$, $+0.0693$ at
$90^\circ$ and $270^\circ$, and $-0.0693$ at $0^\circ$ and $180^\circ$
(normalised to $A_0$ these are $\pm0.866$). The sign flip between the two lobes
is a physical polarity, not an artefact.

### 3.3 A dipping interface also produces a transverse signal

If the converting interface dips, the symmetry plane tilts and the conversion
leaves energy on the transverse component with a different azimuthal form,
dominated by a **$360^\circ$** (one-lobe) term:

$$A_T(\varphi) = c_1\cos\big(\varphi-\varphi_{\text{dip}}\big)
+ c_2\sin\big(2(\varphi-\varphi_{\text{fast}})\big).$$

The second term is the anisotropy signature; the first is the dip. When both are
present, the observed pattern is a mixture, and separating them requires sampling
the full $360^\circ$ of back-azimuths.

### 3.4 The ambiguity, quantified by a condition number

Fit the four-basis model
$\big[\cos\varphi,\ \sin\varphi,\ \cos2\varphi,\ \sin2\varphi\big]$ to the
observed transverse amplitudes. The first two columns are the dip terms, the last
two the anisotropy terms. Whether the fit can separate them is a property of the
**design matrix** $M$ whose columns are those basis functions evaluated at the
observed azimuths.

The demonstration computes, for a clustered azimuth set $(95^\circ$–$135^\circ$,
$5$ azimuths$)$ and a full set $(0^\circ$–$350^\circ$, $36$ azimuths$)$:

| azimuth coverage | condition number of $M$ |
|---|---|
| clustered $95^\circ$–$135^\circ$ | $319.0$ |
| full $0^\circ$–$350^\circ$ | $1.0$ |

A condition number of $319$ means that a $1\%$ perturbation in the data can move
the fitted dip amplitude by up to $\sim 319\%$ — the fit is meaningless. The
Monte Carlo confirms it: with data generated from *pure anisotropy* (true dip
amplitude zero) plus noise of $\sigma = 0.012$, the inferred one-lobe (dip)
amplitude is

$$0.839 \pm 0.671 \quad\text{(clustered)}, \qquad
0.004 \pm 0.002 \quad\text{(full)}.$$

Over clustered azimuths the fit invents a large and wildly unstable dip that is
not in the data. Over full azimuths it correctly recovers zero. **This is the
honest statement of the single-station ambiguity: it is a coverage problem, not
a modelling problem.**

## 4. Physical interpretation

- **Transverse energy is real.** It is not noise, and it is not a processing
  artefact if the components are correctly rotated. It is evidence that the
  Earth beneath the station is not isotropic and flat-layered.
- **Anisotropy and dip are different physics with similar fingerprints.** A
  $180^\circ$ pattern is *consistent with* anisotropy; a $360^\circ$ pattern is
  *consistent with* dip. With limited azimuths, both can fit the same numbers.
- **Splitting measures a product, not two numbers.** $\delta t \approx 2\gamma
  L/v_s$ means the data give $\gamma L$, not $\gamma$ and not $L$.
- **The fast axis is an apparent direction.** In a medium with several
  anisotropic layers, the recovered azimuth is a weighted average and need not
  correspond to a physical fabric direction.

## 5. Assumptions

1. A single hexagonal anisotropic layer with a horizontal symmetry axis, or a
   single dipping interface. Multiple layers are the common reality and break the
   simple two-parameter description.
2. The ray is near-vertical, so the path length in the layer is its thickness and
   the splitting delay is the vertical one.
3. Weak anisotropy ($\gamma \lesssim 10\%$) for the linearised relations.
4. A good estimate of the back-azimuth for every event; a systematic
   back-azimuth error rotates the entire pattern.
5. The receiver-function amplitudes are not distorted by the rotation or by
   near-surface structure.

### 5.1 Depth of anisotropy, and the multi-layer reality

The derivation assumed a *single* anisotropic layer and silently assigned all the
splitting to it. Real splitting accumulates along the ray: a crustal
contribution, a mantle-lithosphere contribution and possibly an asthenospheric
one all add. With one station the total delay and an apparent fast axis are all
that can be measured; the depth distribution is not recovered. Two safeguards are
available and both require more than one station:

1. **Back-azimuthal and incidence-angle variation.** Different event
   back-azimuths and distances sample the anisotropic structure with different
   path geometries; a frequency-dependent or azimuth-dependent splitting delay is
   evidence of layering.
2. **Joint interpretation with other data.** A crustal anisotropy estimate from
   receiver functions can be combined with mantle anisotropy from SKS splitting to
   apportion the total, but the apportionment relies on the assumed depths.

Without such constraints, the honest output of a single-station analysis is a
pair $(\delta t, \varphi_{\text{apparent}})$ with the statement that it is a
path-integrated average. That is a useful measurement — it is not a profile.

### Example 4 — a back-azimuth error rotates the whole pattern

Suppose the true fast axis is at $40^\circ$ but every event's back-azimuth is
mis-set by $+10^\circ$ through a rotation error. The fitted pattern then gives an
apparent fast axis at $50^\circ$, and the inferred splitting delay is unchanged
because it depends on the amplitude, not the phase. The error is a rigid rotation
of the interpretation: the anisotropy *strength* survives, the *direction* does
not. This is why careful horizontal-component orientation and an accurate event
back-azimuth are prerequisites for any directional claim, and why a study that
reports only $\delta t$ is more robust than one that reports only the fast axis.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $v_s$, $v_{\text{fast}}$, $v_{\text{slow}}$ | $\mathrm{km\,s^{-1}}$ | |
| $\gamma$ | dimensionless | velocity ratio |
| $L$ | km | |
| $\delta t$ | s | $\mathrm{km}\times(\mathrm{km\,s^{-1}})^{-1}$ |
| $A_T$, $A_0$ | same as the RF | amplitude |
| $\varphi$ | rad (input degrees) | must be converted before use in $\sin$, $\cos$ |

The argument of $\sin 2(\varphi-\varphi_{\text{fast}})$ is dimensionless, which
requires $\varphi$ in radians in code; passing degrees is one of the most common
programming errors in anisotropy papers.

## 7. Worked examples

### Example 1 — anisotropy from a splitting delay

A station shows a splitting delay of $1.20\ \mathrm{s}$ with a fast axis at
$N40^\circ E$. Assume the anisotropic layer is $100\ \mathrm{km}$ thick and
$v_s = 4.40\ \mathrm{km\,s^{-1}}$. From $\delta t \approx 2\gamma L/v_s$,

$$\gamma \approx \frac{\delta t\,v_s}{2L}
= \frac{1.20 \times 4.40}{2\times100} = 0.0264,$$

i.e. about $2.6\%$. **State the assumed $L$**: with $L = 50\ \mathrm{km}$ the
same delay gives $\gamma = 5.3\%$. The data alone do not choose.

### Example 2 — does the pattern support anisotropy or dip?

Transverse amplitudes at $90^\circ$, $120^\circ$, $150^\circ$ back-azimuths are
$+0.05$, $0.00$, $-0.05$. A two-lobed model with a node at $120^\circ$ fits
exactly. But three points cannot distinguish $A_0\sin2(\varphi-120^\circ)$ from
many one-lobe plus two-lobe combinations: with four basis functions and three
data, the system is underdetermined — the fit is exact for a family of models.
Collect more azimuths before interpreting.

### Example 3 — the thickness–anisotropy trade-off

A splitting delay of $0.78\ \mathrm{s}$ is measured with $v_s = 3.60\
\mathrm{km\,s^{-1}}$. Then $\gamma L = \delta t\,v_s/2 = 1.40\ \mathrm{km}$.
Possible explanations include $(L,\gamma) = (35\ \mathrm{km}, 4.0\%)$,
$(70\ \mathrm{km}, 2.0\%)$, and $(140\ \mathrm{km}, 1.0\%)$. Petrological
constraints, not the seismic data, must decide among them.

## 8. Python demonstration

`code/anisotropy_rf_demo.py`:

1. prints the $180^\circ$-periodic transverse amplitude for twelve
   back-azimuths, with the fast axis at $30^\circ$ (SYNTHETIC);
2. computes the splitting delay $0.779\ \mathrm{s}$ and verifies the
   thickness–anisotropy degeneracy;
3. tabulates a dipping model against a pure anisotropy model;
4. computes the design-matrix condition number ($319$ clustered versus $1$ full)
   and runs a $200$-realisation Monte Carlo showing the inferred dip amplitude is
   $0.839\pm0.671$ for clustered azimuths and $0.004\pm0.002$ for full coverage;
5. states, in plain language, what a single station can and cannot claim.

The demonstration does not use any real seismogram. It is a controlled
experiment on the *interpretation logic*, which is where the ambiguity lives.

## 9. Exercises

Full sets are in
[`exercises/04-anisotropy-receiver-functions-exercises.md`](./exercises/04-anisotropy-receiver-functions-exercises.md)
and
[`exercises/04-anisotropy-receiver-functions-solutions.md`](./exercises/04-anisotropy-receiver-functions-solutions.md).

- **★** Compute $v_{\text{fast}}$, $v_{\text{slow}}$ and $\delta t$ for
  $v_s = 4.2\ \mathrm{km\,s^{-1}}$, $\gamma = 3\%$, $L = 80\ \mathrm{km}$.
- **★★** Derive $\delta t \approx 2\gamma L/v_s$ and state the neglected term.
- **★★** Show that $\sin 2(\varphi-\varphi_0)$ has period $180^\circ$ and
  identify its nodes and maxima.
- **★★★** Given five back-azimuths spanning a narrow range, compute the
  condition number of the four-basis design matrix and interpret it.

## 10. Common mistakes

1. **Calling any transverse energy "anisotropy".** Dip, scattering and
   mis-rotation all produce it.
2. **Reporting $\gamma$ alone.** The data give $\gamma L$; report both or a
   range.
3. **Fitting one-lobe and two-lobe terms to too few azimuths.** The fit is
   underdetermined; check the condition number before believing a separation.
4. **Using degrees in a numerical sine.** The amplitude pattern silently shifts.
5. **Assuming the fast axis is a fabric direction.** With multiple layers the
   recovered azimuth is an apparent, not a physical, direction.
6. **Ignoring the depth of the anisotropy.** Splitting delays accumulate along
   the path; a crustal and a mantle contribution are not separable from a single
   measurement.
7. **Comparing fast-axis directions between stations without checking the
   reference frame.** A rotation convention error of a few degrees propagates
   into every reported direction and is invisible in the delay times.
8. **Treating the apparent fast axis as a fabric direction.** With two or more
   anisotropic layers the recovered azimuth is a weighted average that can
   differ substantially from either layer's physical axis.

## 11. Real-world applications

- **Mantle deformation.** Splitting delays and fast-axis directions are used to
  infer the orientation of olivine fabric, and hence the direction of past or
  present mantle flow.
- **Subduction zones.** Trench-parallel fast axes are a strong signal of
  mantle-wedge flow; the interpretation depends on separating crustal from
  mantle anisotropy, which needs more than one station.
- **Crustal fabrics.** In the crust, anisotropy from aligned cracks or
  metamorphic fabric is a target for both tectonics and resource studies; the
  crack-induced anisotropy also changes with pore pressure, which links it to
  monitoring.
- **Survey design.** Because the ambiguity is fundamentally about azimuthal
  coverage, network geometry is a scientific decision: a station with poor
  back-azimuthal coverage cannot resolve anisotropy no matter how good its data
  quality.

## 12. Further reading

- **Silver, P. G., & Chan, W. W. (1991). Shear wave splitting and subcontinental
  mantle deformation. *Journal of Geophysical Research*, 96(B10),
  16429–16454.** Level: research. The canonical treatment of splitting and its
  interpretation.
- **Savage, M. K. (1999). Seismic anisotropy and mantle deformation: what have
  we learned from shear wave splitting? *Reviews of Geophysics*, 37(1), 65–106.**
  Level: research. A critical review of what splitting can and cannot establish.
- **Long, M. D., & Silver, P. G. (2008). The subduction zone flow field from
  seismic anisotropy: a global view. *Science*, 319(5861), 315–318.** Level:
  research. An application where the coverage argument matters.
- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. The elasticity of hexagonal media.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Confirm current details through
> your library.

## 13. Related lessons

- [01 Receiver Functions: Deconvolution and Ps Conversions](01-receiver-function-principle.md).
- [02 H-K Stacking and Crustal Thickness Estimation](02-h-k-stacking.md).
- [05 Joint Inversion of Receiver Functions and Surface Waves](05-joint-inversion-rf.md) —
  what additional data do to the ambiguity.
- [06-01-08 Anisotropic Wave Propagation](../01-elastic-wave-propagation/08-anisotropic-propagation.md).
- [05-04-05 Anisotropy of Rocks](../../05-core-geophysics/04-rock-physics/05-anisotropy-rock.md) —
  where the fast/slow speeds come from physically.

## 14. Self-assessment checklist

- [ ] I can explain why the transverse component is a null channel when the Earth is isotropic.
- [ ] I can derive $\delta t \approx 2\gamma L/v_s$ and state its neglected term.
- [ ] I can state why $\delta t$ alone cannot give both $L$ and $\gamma$.
- [ ] I can distinguish a $180^\circ$ from a $360^\circ$ azimuthal pattern.
- [ ] I can compute a design-matrix condition number and interpret it.
- [ ] I can write a claim that a single station is entitled to make, and one it is not.
