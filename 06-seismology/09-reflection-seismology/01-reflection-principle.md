---
id: 06-09-01
title: "Acoustic Impedance, Reflection Coefficients and the Convolution Model"
level: advanced
prereqs: ["06-01-02", "02-03-04"]
tags: [seismology, reflection-seismology, impedance, convolution-model, reflectivity]
---

# Acoustic Impedance, Reflection Coefficients and the Convolution Model

## Learning objectives

By the end of this lesson you will be able to:

1. **Define** acoustic impedance and derive the normal-incidence reflection
   coefficient $R=(Z_2-Z_1)/(Z_2+Z_1)$ from continuity of pressure and particle
   velocity.
2. **Explain** why only *contrasts* are visible, and why a layer whose impedance
   equals its surroundings is seismically invisible even if its velocity or its
   density differs.
3. **Derive** the convolutional model $s(t)=\sum_k R_k\,w(t-t_k)$ and the
   two-way time $t_k=2\sum_i h_i/v_i$.
4. **Verify** the convolutional model numerically: the amplitude of each
   reflected wavelet equals the analytic reflection coefficient.
5. **State** the assumptions the model makes and the two independent failures
   (impedance trade, wavelet phase) it cannot resolve.
6. **Convert** between depth and two-way time with stated units.

## Prerequisites

- [06-01-02 P and S Waves](../01-elastic-wave-propagation/02-p-and-s-waves.md) —
  elastic waves and their speeds.
- [02-03-04 Wave Basics](../../02-physics/03-oscillations-and-waves/04-wave-basics.md) —
  waves at an interface.

## 1. Intuition: seismic data are a picture of contrasts

A reflection seismogram is not a picture of the Earth; it is a picture of the
Earth's **impedance contrasts**, blurred by a wavelet. Rock properties matter
only through their product $Z=\rho v$, the acoustic impedance. Two rocks with
difference velocities and densities can have the same impedance, and at normal
incidence the seismic wave cannot tell them apart. This is the first and largest
non-uniqueness of reflection seismology, and this lesson derives exactly why it
arises.

The second idea is equally simple. A plane wave hitting an interface produces a
reflected wave whose amplitude is a fixed fraction of the incident amplitude —
the reflection coefficient. A layered Earth therefore gives a *train of spikes*
in time, one per interface, and the recorded trace is that spike train
convolved with the seismic wavelet. Everything downstream — deconvolution, NMO,
stacking, migration — is an attempt to undo part of that convolution or to
organise the traces geometrically.

Numbers in this lesson are **SYNTHETIC**.

## 2. Precise definitions

### 2.1 Acoustic impedance

For a medium of density $\rho$ and P-wave speed $v_p$, the **acoustic impedance**
is

$$Z = \rho\,v_p \qquad (\mathrm{kg\,m^{-2}\,s^{-1}}).$$

In the units used in the demonstration, $\rho$ in $\mathrm{g\,cm^{-3}}$ and $v_p$
in $\mathrm{km\,s^{-1}}$ give $Z$ in $\mathrm{g\,cm^{-3}\,km\,s^{-1}}$, which
differs from SI by a constant factor; since only ratios of $Z$ enter, the choice
is harmless provided it is consistent.

### 2.2 Reflection and transmission coefficients

At normal incidence on a boundary between media 1 and 2,

$$R = \frac{Z_2-Z_1}{Z_2+Z_1}, \qquad T = \frac{2Z_2}{Z_2+Z_1}.$$

Note $T$ here is the ratio of *particle velocity* amplitudes, not energy; the
energy reflection and transmission coefficients satisfy $R^2 + (Z_1/Z_2)T^2 = 1$.

### 2.3 Two-way time

For a stack of layers of thickness $h_i$ and speed $v_i$, the two-way time to the
base of layer $k$ at normal incidence is

$$t_k = 2\sum_{i=1}^{k}\frac{h_i}{v_i}.$$

## 3. Derivations

### 3.1 The reflection coefficient from boundary conditions

Let a plane P wave of amplitude $A_I$ travel downward in medium 1 and hit the
interface at $z=0$. Continuity of **pressure** (or, equivalently, of normal
stress) and of **particle velocity** across the interface gives two equations for
the reflected amplitude $A_R$ and the transmitted amplitude $A_T$:

$$A_I + A_R = A_T \quad\text{(velocity)},$$

$$Z_1(A_I - A_R) = Z_2 A_T \quad\text{(stress, using } \sigma \propto Z\,u).$$

Substitute $A_T = A_I + A_R$ into the second:

$$Z_1 A_I - Z_1 A_R = Z_2 A_I + Z_2 A_R
\;\Longrightarrow\; A_R(Z_1+Z_2) = A_I(Z_2-Z_1),$$

$$R \equiv \frac{A_R}{A_I} = \frac{Z_2-Z_1}{Z_2+Z_1}.$$

**Physical reading.** If $Z_2 > Z_1$ (a harder layer below), $R>0$: the reflected
wave keeps the incident polarity (a "peak" in a normal-polarity display). If
$Z_2 < Z_1$, $R<0$: the reflection is reversed (a "trough"). The magnitude
$|R|$ depends only on the *ratio* of the impedances and never exceeds 1; for
typical sedimentary contrasts $|R|$ lies between about $0.01$ and $0.2$.

### 3.2 The convolutional model

Assume the source wavelet $w(t)$ is stationary (the same at every interface),
the medium is horizontally layered, and each interface reflects once, with no
multiples and no transmission losses. Then the recorded trace is the sum of the
wavelet emitted at each two-way time, scaled by the reflection coefficient:

$$\boxed{\;s(t) = \sum_{k=1}^{N} R_k\,w(t-t_k) + n(t)\;}
\qquad\text{equivalently}\qquad
s(t) = w(t) * r(t) + n(t),$$

where $r(t)=\sum_k R_k\delta(t-t_k)$ is the **reflectivity series** and $n(t)$
is noise. The model says that a seismogram is the convolution of the Earth's
reflectivity with the wavelet — the foundational statement of exploration
seismology, and the reason a "spike" deconvolution is even conceivable.

### 3.3 Numerical verification of the convolutional model

The demonstration builds a three-interface model and checks the model against
its own definition: it convolves the reflectivity series with a wavelet, then
reads the peak amplitude at each interface time and divides by the analytic
reflection coefficient.

| interface | two-way time (s) | analytic $R$ | measured peak | ratio |
|---|---|---|---|---|
| base of layer 1 | 0.5455 | $+0.16456$ | $+0.16456$ | 1.00000 |
| base of layer 2 | 0.8312 | $+0.09804$ | $+0.09804$ | 1.00000 |
| base of layer 3 | 1.1437 | $+0.07873$ | $+0.07873$ | 1.00000 |

The ratios are exactly 1 because the wavelets do not overlap at these
separations. Where they do overlap (thin beds), the peaks no longer equal the
reflection coefficients individually — which is the subject of
[07 Seismic Attributes](07-seismic-attributes.md).

### 3.4 Two-way time and unit bookkeeping

With $h_i$ in km and $v_i$ in $\mathrm{km\,s^{-1}}$, $h_i/v_i$ is in seconds, and
the factor 2 accounts for the down-and-up path. The demonstration's model:

$$t_1 = \frac{2(0.60)}{2.20} = 0.5455\ \mathrm{s},\quad
t_2 = t_1 + \frac{2(0.40)}{2.80} = 0.5455+0.2857 = 0.8312\ \mathrm{s},$$
$$t_3 = t_2 + \frac{2(0.50)}{3.20} = 0.8312+0.3125 = 1.1437\ \mathrm{s}.$$

These match the printed values exactly.

### 3.5 Why normal-incidence data cannot separate velocity from density

Suppose layer 2's properties change while its impedance is held fixed:

$$v \to v(1+\epsilon), \qquad \rho \to \rho/(1+\epsilon).$$

Then $Z = \rho v$ is unchanged, so **both** bounding reflection coefficients are
unchanged and the normal-incidence seismogram is identical. The demonstration
confirms $Z = 6.4400$ for $\epsilon = 0$, $0.1$, $0.25$ and $R = +0.165$ for all
three. The two models differ in $v$ by $25\%$ and in $\rho$ by $20\%$ and are
indistinguishable at normal incidence.

This is the *impedance trade-off*, and it is **not** a resolution or noise
problem: more data at normal incidence cannot break it, because the data depend
on $(v,\rho)$ only through $v\rho$. Breaking it requires oblique incidence, where
the reflection coefficient depends on $v$ and $\rho$ separately — the subject of
[05 AVO/AVA Analysis and Its Assumptions](05-amplitude-vs-offset.md).

### 3.6 Two pitfalls from the impedance trade

**Pitfall 1: a fluid contact is a tuning target.** A fluid contact is not a
mirror-smooth surface; it is a transition whose thickness is set by capillary
forces and whose seismic expression is a *composite* of the contact reflection
and the reflections from the reservoir top and base. If the reservoir is thinner
than $\lambda/4$, the contact's amplitude is governed by the tuning curve of
[07](07-seismic-attributes.md), so "a flat spot" is a statement about wave
interference as much as about fluids.

**Pitfall 2: velocity–density compensation in real rocks.** In rocks, $v$ and
$\rho$ are correlated through porosity and mineralogy, so the impedance trade of
Section 3.5 is not the whole story. The correlation means that a change in
porosity usually moves $v$ and $\rho$ in opposite directions, partly preserving
$Z$ and reducing the seismic response. This is why "porosity from impedance" is a
*calibrated* relation rather than a physical law: the calibration absorbs the
correlation, and it fails whenever the lithology changes away from the
calibration wells.

### 3.7 The wavelet-phase ambiguity

The convolutional model contains a phase ambiguity that must be resolved before
any polarity-dependent interpretation:

$$s = w * r = (w * q) * (q^{-1} * r).$$

Any filter $q$ applied to the wavelet can be absorbed into the reflectivity, so
the *amplitude spectrum* of the data is consistent with infinitely many
wavelet–reflectivity pairs that differ by a phase rotation. The consequences:

- A zero-phase interpretation and a $90^\circ$-phase interpretation of the same
  data differ in *where* a reflection is placed and in *which polarity* it has;
  both fit the amplitude spectrum equally well.
- The ambiguity is resolved by (i) measuring the wavelet from the source, (ii)
  tying to a well, or (iii) assuming a phase and stating the assumption. It cannot
  be resolved from the seismic data alone.

Lesson 05's AVO analysis and lesson 09's interpretation both depend on the
polarity convention, so this ambiguity is not academic: it changes the sign of
every impedance contrast an interpreter reports.

## 4. Physical interpretation

- **Seismic sees contrasts, not properties.** A homogeneous Earth produces no
  reflections at all. A region of unusual rock that is smoothly gradational has
  no sharp impedance step and therefore no strong reflection.
- **Polarity carries the sign of the contrast.** In a normal-polarity display,
  a peak means an increase in impedance with depth and a trough a decrease;
  this convention must be established before any interpretation is attempted.
- **The convolutional model is a linear filter.** The Earth's reflectivity is the
  input, the wavelet is the filter, and the seismogram is the output. Deconvolution
  attempts to invert the filter; migration reorganises the geometry.
- **The impedance trade is a genuine ambiguity.** It cannot be removed by better
  acquisition at normal incidence, only by using the angle dependence.

## 5. Assumptions

1. **Plane waves, normal incidence** for the coefficient $R=(Z_2-Z_1)/(Z_2+Z_1)$.
   At oblique incidence the full Zoeppritz equations apply and no S conversion is
   assumed here.
2. **A single, stationary wavelet.** Real sources vary shot to shot; this is the
   reason "deterministic" deconvolution needs a measured wavelet.
3. **No multiples, no transmission losses, no attenuation.** The demonstration's
   model is deliberately lossless so that the convolutional identity can be
   verified exactly.
4. **Horizontally layered, isotropic media.**
5. **The reflectivity is sparse.** If the wavelet is long compared with the layer
   spacing, reflections overlap and the peak-amplitude identification fails.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $\rho$ | $\mathrm{g\,cm^{-3}}$ | |
| $v_p$ | $\mathrm{km\,s^{-1}}$ | |
| $Z$ | $\mathrm{g\,cm^{-3}\,km\,s^{-1}}$ | product of the two |
| $R, T$ | dimensionless | ratio of impedances |
| $h$ | km | |
| $t$ | s | $\mathrm{km/(km\,s^{-1})}$ |

If a computed $R$ has units, an impedance was divided by something that is not an
impedance. If a two-way time has units of length, a velocity was multiplied where
it should have been divided.

## 7. Worked examples

### Example 1 — a reflection coefficient and its polarity

A sandstone with $\rho_1 = 2.25\ \mathrm{g\,cm^{-3}}$, $v_1 = 2.60\
\mathrm{km\,s^{-1}}$ overlies a shale with $\rho_2 = 2.40\
\mathrm{g\,cm^{-3}}$, $v_2 = 2.30\ \mathrm{km\,s^{-1}}$.

$$Z_1 = 5.850,\quad Z_2 = 5.520, \qquad
R = \frac{5.520-5.850}{5.520+5.850} = -0.0290.$$

The reflection is weak and **negative**: the impedance decreases with depth, so
a normal-polarity display shows a trough.

### Example 2 — two-way time and depth conversion

A reflector is picked at $t_0 = 1.20\ \mathrm{s}$ two-way. Overburden at a
constant $2.40\ \mathrm{km\,s^{-1}}$ gives

$$h = \frac{v\,t_0}{2} = \frac{2.40 \times 1.20}{2} = 1.44\ \mathrm{km}.$$

If the true overburden is layered with an average speed of
$2.55\ \mathrm{km\,s^{-1}}$, the true depth is $1.53\ \mathrm{km}$ — a $6\%$
error from a single average-velocity mistake. Depth conversion is only as good as
the velocity model, which is why it is done with wells and stacking velocities,
not with a constant.

### Example 3 — the impedance trade in numbers

Layer 2 in the demonstration's model has $v=2.80\ \mathrm{km\,s^{-1}}$,
$\rho=2.30\ \mathrm{g\,cm^{-3}}$, $Z=6.440$. Replace it with
$v=3.50\ \mathrm{km\,s^{-1}}$, $\rho=1.840\ \mathrm{g\,cm^{-3}}$:

$$Z = 3.50\times1.840 = 6.440.$$

Both bounding coefficients are unchanged ($+0.1646$ at the top, $+0.0980$ at the
base, both computed from the same impedance triplet). The synthetic seismogram
is *identical*, yet the rock is $25\%$ faster and $20\%$ lighter. Only an
angle-dependent measurement can tell them apart.

### Example 4 — a synthetic seismogram by hand

Three interfaces with two-way times $0.5455$, $0.8312$, $1.1437\ \mathrm{s}$ and
coefficients $+0.1646$, $+0.0980$, $+0.0787$. A zero-phase Ricker of
$30\ \mathrm{Hz}$ peaks 1.0 at each time and has small positive side lobes
($\approx0.02$) at $\pm 20\ \mathrm{ms}$. Sampling at 1 ms, the trace is:

$$s(0.5455) = 1.00\times0.1646 = 0.1646,$$
$$s(0.5455\pm0.020) \approx 0.02\times0.1646 = 0.0033,$$

and similarly for the other two times. Because the times differ by more than
$200\ \mathrm{ms}$, no side lobe of one interface reaches another, and the trace
is exactly the sum of three isolated wavelets with peak amplitudes equal to the
coefficients — as the demonstration verifies (ratios 1.00000). **Had the
interfaces been 20 ms apart, the peaks would be a mixture and no longer equal any
single coefficient**, which is the thin-bed problem of lesson 07 in its simplest
form.

## 8. Python demonstration

`code/reflection_principle_demo.py`:

1. prints the impedance and reflection coefficient of every interface of a
   SYNTHETIC three-layer model;
2. prints every two-way time and checks the units;
3. builds the reflectivity series and convolves it with a 30 Hz Ricker;
4. **verifies** that each reflected peak equals its analytic coefficient
   (ratios 1.00000);
5. demonstrates the impedance trade-off by holding $Z$ fixed while changing $v$
   and $\rho$.

The demo prints the number of samples (1344), the number of spikes (3) and every
input, so each result is reproducible by hand.

## 9. Exercises

Full sets are in
[`exercises/01-reflection-principle-exercises.md`](./exercises/01-reflection-principle-exercises.md)
and
[`exercises/01-reflection-principle-solutions.md`](./exercises/01-reflection-principle-solutions.md).

- **★** Compute $R$ for $\rho_1=2.1$, $v_1=2.4$ and $\rho_2=2.4$,
  $v_2=2.8$ (units as in the lesson) and state the polarity.
- **★★** Derive $T=2Z_2/(Z_2+Z_1)$ from the same boundary conditions and verify
  $1+R=T$.
- **★★** Convert a two-way time of $1.6\ \mathrm{s}$ to depth for a
  three-layer overburden and compare with a single average-velocity conversion.
- **★★★** Build a two-layer model whose normal-incidence response is identical
  to a given three-layer model, and explain why it is impossible in general.

## 10. Common mistakes

1. **Forgetting that the units of $Z$ are a choice.** Only ratios matter; mixing
   unit systems within one calculation does not.
2. **Reading a "strong" reflection as a "big" contrast in one property.** The
   contrast may be in density, in velocity, or in both.
3. **Treating $T$ as an energy transmission coefficient.** The stated $T$ is an
   amplitude ratio; the energy balance involves $Z_1/Z_2$.
4. **Assuming a depth conversion is exact.** It is only as good as the velocity
   model, and a constant overburden velocity is usually wrong.
5. **Expecting normal-incidence data to separate $v$ from $\rho$.** It cannot;
   that is a property of the physics, not of the processing.

## 11. Real-world applications

- **Hydrocarbon exploration.** The impedance contrast between a reservoir and its
  seal is what makes a prospect visible; a "bright spot" is a strong negative
  reflection.
- **Reservoir characterisation.** Inverted impedance is a primary rock-property
  attribute, but its interpretation depends on the impedance trade-off identified
  here.
- **CO$_2$ storage and 4-D monitoring.** Injected fluid changes $v$ and $\rho$;
  the resulting impedance change is what time-lapse seismic measures (see
  [08 Time-Lapse (4-D) Seismic](08-4d-seismic.md)).
- **Quantitative interpretation.** Every amplitude-based method — AVO,
  inversion, attributes — rests on the coefficient and the convolution model
  derived here.

## 12. Further reading

- **Aki, K., & Richards, P. G. (2002). *Quantitative Seismology* (2nd ed.).
  University Science Books.** Level: advanced. The reflection/transmission
  coefficients and their derivation.
- **Sheriff, R. E., & Geldart, L. P. (1995). *Exploration Seismology* (2nd ed.).
  Cambridge University Press.** Level: intermediate. The convolutional model and
  exploration practice.
- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** Level: intermediate to advanced. The standard processing
  reference.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text. Confirm current editions through
> your library.

## 13. Related lessons

- [02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](02-processing-flow.md) —
  what is done to these traces.
- [05 AVO/AVA Analysis and Its Assumptions](05-amplitude-vs-offset.md) — how
  oblique incidence breaks the impedance trade.
- [07 Seismic Attributes and Quantitative Interpretation](07-seismic-attributes.md) —
  resolution limits of the convolution model.
- [05-04-01 Porosity, Density and Velocity Relationships](../../05-core-geophysics/04-rock-physics/01-porosity-density-velocity.md) —
  why $v$ and $\rho$ co-vary in rocks.

## 14. Self-assessment checklist

- [ ] I can derive $R=(Z_2-Z_1)/(Z_2+Z_1)$ from the boundary conditions.
- [ ] I can state the polarity convention and apply it to a given contrast.
- [ ] I can write the convolutional model and compute two-way times.
- [ ] I can verify the convolutional model numerically and say when it fails.
- [ ] I can construct an impedance-preserving trade and explain why it is invisible.
- [ ] I can convert a two-way time to depth and state the error from a wrong velocity.
