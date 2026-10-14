---
id: 15-02-07
title: "Marine CSEM and EM for Gas Hydrates"
level: research
prereqs: ["09-05-03", "09-01-01", "15-02-02"]
tags: [oceanography, marine-geophysics, csem, electromagnetics, diffusion, skin-depth, gas-hydrates]
---

# Marine CSEM and EM for Gas Hydrates

> **All models and data in this module are SYNTHETIC.** The resistivities,
> thicknesses and frequencies used here are chosen teaching values, printed by the
> demonstration in `code/`. No survey, prospect, well, resistivity model or
> published result is reproduced. $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$
> is an exact constant.

Controlled-source electromagnetics is the youngest of the methods in this module,
and the only one that measures **resistivity** — the property that distinguishes a
fluid-filled pore space from a solid one. Its physics is a diffusion, not a wave:
the fields do not propagate through the Earth, they soak into it, and everything
about the method follows from one length, the **skin depth**.

That single length produces both the method's power and its characteristic
difficulty. Because the skin depth depends on resistivity and frequency, a
resistive layer perturbs the fields measurably; and because the ocean is
thirty times more conductive than the sediments and a kilometre and a half deep,
the water column screens the measurement so effectively that a plane-wave
(seafloor magnetotelluric) geometry is dominated by the water at every useful
frequency. Marine CSEM works because it *avoids* that screening with a
near-seafloor source and receiver geometry — not because it corrects for it.

## Learning objectives

By the end of this lesson you will be able to:

1. **Derive** the skin depth $\delta = \sqrt{2\rho/(\mu_0\omega)}$ from the
   quasi-static diffusion equation and **compute** it for stated resistivities and
   frequencies, checking it against the wavenumber.
2. **Quantify** the attenuation of the water column and **state** why the usable
   frequency band is narrow.
3. **Evaluate** a one-dimensional layered response using the impedance recursion,
   and **verify** it on a uniform half-space where the answer is analytic.
4. **Show**, with numbers, that a plane-wave seafloor response is water-dominated
   at every frequency in the band, and **draw** the design conclusion.
5. **Compute** the sub-seafloor apparent resistivity for a resistive layer and
   **identify** the frequency band and the size of the anomaly.
6. **Test** the transverse-resistance rule of thumb rather than quoting it, and
   **state** the regime in which it fails.
7. **State** what a marine CSEM survey can and cannot deliver, in one sentence each.

## Prerequisites

- [09-05-03 CSEM in Marine Environments](../../09-electrical-em-methods/05-em-methods-applications/03-csem-marine.md) —
  the method, its sources and its acquisition practice.
- [09-01-01 Resistivity, Conductivity and Conduction Mechanisms](../../09-electrical-em-methods/01-electrical-properties-of-earth/01-resistivity-conductivity.md) —
  what resistivity is a measurement of.
- [15-02-02 Multibeam Bathymetry and Swath Mapping](02-multibeam-bathymetry.md) —
  the near-seafloor geometry that the source and receivers share.

## 1. Skin depth

In the quasi-static limit ($\omega$ small enough that displacement currents are
negligible — always true in the ocean and in sediments below a few hertz) Maxwell's
equations reduce to a diffusion equation for the fields:

$$\nabla^{2}\mathbf{E} = \mu_0\sigma\frac{\partial \mathbf{E}}{\partial t}
\;\Longrightarrow\; k = \sqrt{\mathrm{i}\mu_0\omega\sigma}
= \frac{1+\mathrm{i}}{\delta},$$

$$\boxed{\;\delta = \frac{1}{\mathrm{Re}\,k}
= \sqrt{\frac{2\rho}{\mu_0\omega}}
= \sqrt{\frac{\rho}{\pi f \mu_0}}
\;\;(\mathrm{m})\;}$$

which with $\mu_0 = 4\pi\times10^{-7}$ evaluates to

$$\delta = 503.3\sqrt{\frac{\rho}{f}}\ \mathrm{m}
\qquad (\rho\ \text{in}\ \Omega\,\mathrm{m},\ f\ \text{in Hz}).$$

| $\rho$ ($\Omega$ m) | $f = 0.1$ Hz | 1 Hz | 10 Hz |
|---|---|---|---|
| 0.30 (seawater) | 871.7 | 275.7 | 87.2 |
| 1.0 | 1591.6 | 503.3 | 159.2 |
| 10 | 5032.9 | 1591.6 | 503.3 |
| 100 | 15915.5 | 5032.9 | 1591.6 |

The demonstration computes each entry twice — once from the closed form and once as
$1/\mathrm{Re}(k)$ — and the ratio is 1.0000 throughout, which is the check on the
algebra and on $\mu_0$.

**The numbers that matter.** At $1\ \mathrm{Hz}$ the skin depth in seawater is
$276\ \mathrm{m}$, so a $1500\ \mathrm{m}$ water column is **5.44 skin depths**,
and a one-way traversal loses $8.686 \times 1500/276 = 47.3\ \mathrm{dB}$. At
$0.1\ \mathrm{Hz}$ the water loss is $15.0\ \mathrm{dB}$; at $10\ \mathrm{Hz}$ it is
$149\ \mathrm{dB}$. **The ocean is an electromagnetic screen, and its attenuation
is exponential in frequency.**

## 2. Why the plane-wave geometry cannot work

A magnetotelluric-style measurement on the seafloor senses the parallel combination
of the impedance looking up (the water layer below the insulating atmosphere) and
the impedance looking down (the sediments). With the demonstration's water
($0.30\ \Omega\,\mathrm{m}$, $1500\ \mathrm{m}$), sediment
($1.00\ \Omega\,\mathrm{m}$), and a resistive target
($100\ \Omega\,\mathrm{m}$, $100\ \mathrm{m}$ at $300\ \mathrm{m}$ below the
seafloor):

| $f$ (Hz) | $\delta$ in seawater (m) | apparent $\rho$ ($\Omega$ m) | phase (deg) |
|---|---|---|---|
| 0.01 | 2756.6 | 0.198 | 25.50 |
| 0.03 | 1591.5 | 0.116 | 34.26 |
| 0.1 | 871.7 | 0.120 | 46.13 |
| 0.3 | 503.3 | 0.133 | 45.18 |
| 1 | 275.7 | 0.131 | 44.29 |
| 3 | 159.2 | 0.126 | 43.97 |
| 10 | 87.2 | 0.124 | 45.02 |

**The apparent resistivity is between $0.116$ and $0.198\ \Omega\,\mathrm{m}$ at
every frequency**, while the sediment is $1.00$ and the target is $100\ \Omega\,\mathrm{m}$.
The water column dominates completely, because it is 3.3 times more conductive than
the sediment and $1500\ \mathrm{m}$ thick.

This is not a defect of the calculation; it is the physics, and it explains the
instrument. **Marine CSEM therefore uses a controlled source towed close to the
seafloor with receivers on the seafloor**, so that the fields entering the sediment
have crossed metres of water rather than kilometres. The geometry *avoids* the
screening. A corollary worth stating: the same screening means that a deep-towed
system's signal at the receiver is dominated by the direct water-path arrival,
which is why the *shape* of the response as a source–receiver offset varies, rather
than its absolute level, carries the information.

## 3. The sub-seafloor response

Remove the water from the model and look only downward from the seafloor — the
idealised sensitivity of a controlled source and receiver both at the seafloor:

| $f$ (Hz) | $\delta$ in sediment (m) | apparent $\rho$ ($\Omega$ m) | phase (deg) |
|---|---|---|---|
| 0.01 | 5032.9 | 1.039 | 45.85 |
| 0.03 | 2905.8 | 1.067 | 46.18 |
| 0.1 | 1591.5 | 1.115 | 46.24 |
| 0.3 | 918.9 | 1.162 | 45.35 |
| 1 | 503.3 | 1.144 | 42.91 |
| 3 | 290.6 | 1.015 | 42.08 |
| 10 | 159.2 | 0.971 | 45.07 |

Now the response *does* move, and its shape is the whole story:

- at $10\ \mathrm{Hz}$ the apparent resistivity is $0.971\ \Omega\,\mathrm{m}$,
  **slightly below** the background, because the skin depth ($159\ \mathrm{m}$) is
  smaller than the layer depth and nothing has reached it;
- it **rises to a maximum of about $1.16\ \Omega\,\mathrm{m}$ near $0.3\ \mathrm{Hz}$**,
  a $16\,\%$ anomaly, where the skin depth ($919\ \mathrm{m}$) is a few times the
  layer depth;
- it **falls back at the lowest frequencies**, because the layer becomes
  electrically thin compared with the skin depth and its contribution is diluted.

**The response is therefore confined to a band whose position is set by the layer
depth and whose shape carries the layer's properties.** A single frequency cannot
characterise it, which is what makes the interpretation of a CSEM sounding a
shape-fitting problem rather than a lookup.

## 4. Quantifying the anomaly

Comparing three models over the same band:

| $f$ (Hz) | A: no target ($\Omega$ m) | B: $100\ \Omega$ m × $100$ m ($\Omega$ m) | C: $50\ \Omega$ m × $200$ m ($\Omega$ m) | B vs A (%) | C vs B (%) |
|---|---|---|---|---|---|
| 0.01 | 1.000 | 1.039 | 1.079 | 3.95 | 3.85 |
| 0.03 | 1.000 | 1.067 | 1.137 | 6.74 | 6.50 |
| 0.1 | 1.000 | 1.115 | 1.235 | 11.48 | 10.75 |
| 0.3 | 1.000 | 1.162 | 1.325 | **16.15** | 14.09 |
| 1 | 1.000 | 1.144 | 1.258 | 14.37 | 10.03 |
| 3 | 1.000 | 1.015 | 1.006 | 1.48 | $-0.90$ |

**The anomaly is tens of per cent, not a factor**, and it is confined to a band
peaking near $0.3\ \mathrm{Hz}$. A measurement that cannot resolve ten per cent of
apparent resistivity cannot detect the layer at all, whatever the processing. And
model C — half the resistivity, twice the thickness — gives a *different* response,
by up to $14\,\%$, so the shape does discriminate the two. That is a measurement of
the transverse-resistance rule of thumb, and it is partly a refutation of it.

## 5. Testing the transverse-resistance rule

The rule of thumb says a thin resistive layer is sensed through its **transverse
resistance** $\rho h$, so that a thin/very-resistive layer and a
thick/moderately-resistive layer are indistinguishable. Build five layers with the
same $\rho h = 10\,000\ \Omega\,\mathrm{m^{2}}$ and compare their response curves:

| $\rho$ ($\Omega$ m) | $h$ (m) | peak anomaly (%) | at $f$ (Hz) | max deviation from the (100,100) curve (%) |
|---|---|---|---|---|
| 200 | 50 | 8.52 | 0.562 | 8.44 |
| 100 | 100 | 16.88 | 0.422 | 0 (reference) |
| 50 | 200 | 33.42 | 0.422 | 16.54 |
| 25 | 400 | 64.15 | 0.316 | 47.85 |
| 12.5 | 800 | 114.34 | 0.237 | 99.01 |

**Models with the same transverse resistance differ by tens to hundreds of per
cent**, so $\rho h$ is *not* the quantity that controls this response. (The
$16.88\,\%$ at $0.422\ \mathrm{Hz}$ is the same model as the $16.15\,\%$ in
Section 4, sampled on a different frequency grid — the tabulated peak depends on
the grid, which is why the deviation column is the more meaningful comparison.)

### 5b. Controlling the experiment

Equal $\rho h$ with different $h$ changes two things at once, so it cannot identify
which matters. Fix the frequency at $0.422\ \mathrm{Hz}$, put the layer at the
seafloor over a $1.00\ \Omega\,\mathrm{m}$ half-space ($\delta_{\text{host}} =
774.8\ \mathrm{m}$), and vary $\rho$ and $h$ independently:

| $\rho$ ($\Omega$ m) | $h$ (m) | $\rho h$ ($\Omega\,\mathrm{m^{2}}$) | $h/\delta_{\text{host}}$ | $\rho_a$ ($\Omega$ m) | $h/\delta_{\text{layer}}$ |
|---|---|---|---|---|---|
| 10 | 100 | 1 000 | 0.129 | 1.2588 | 0.0408 |
| 100 | 100 | 10 000 | 0.129 | 1.2882 | 0.0129 |
| 1000 | 100 | 100 000 | 0.129 | 1.2911 | 0.0041 |
| 1000 | 10 | 10 000 | 0.013 | 1.0261 | 0.0004 |
| 10 000 | 1 | 10 000 | 0.001 | 1.0026 | 0.0000 |
| 10 | 1000 | 10 000 | 1.291 | 5.3988 | 0.4082 |

**Two groups of rows answer the question.** The first three rows have the same
thickness and transverse resistances spanning a **factor of 100**, and their
responses span $1.2588$ to $1.2911$ — a **$2.5\,\%$** range. The three rows with
$\rho h = 10\,000$ have anomalies of $28.8\,\%$ ($h = 100$), $2.6\,\%$ ($h = 10$) and
$0.26\,\%$ ($h = 1$): very nearly **proportional to $h$**, as the leading term
$\omega\mu_0\delta h$ of the expansion predicts ($25.8\,\%$, $2.6\,\%$, $0.26\,\%$;
the extra $3.3\,\%$ at $h = 100$ is the $\omega\mu_0h^{2}$ term). **A hundredfold
change in resistivity moves the response by $2.5\,\%$; a hundredfold change in
thickness moves it by a factor of $100$.**

**Why.** Expanding the impedance recursion for $h \ll \delta_{\text{layer}}$ gives

$$\rho k\tanh(kh) \to \rho k (kh) = \rho k^{2}h = \mathrm{i}\omega\mu_0 h ,$$

so the layer's contribution is a purely **inductive** impedance increment that
depends on the layer's **thickness alone**. Propagating it to the surface adds it
to the half-space impedance, and with
$Z = (1+\mathrm{i})\omega\mu_0\delta/2$,

$$\rho_a = \omega\mu_0\left(\frac{\delta^{2}}{2} + \delta h + h^{2}\right)
= 1.2915\ \Omega\,\mathrm{m}\ \text{for}\ h = 100\ \mathrm{m},$$

against the recursion's $1.2882$ ($\rho = 100$) and $1.2911$ ($\rho = 1000$) — a
$0.3\,\%$ agreement that confirms the expansion.
**So what does the transverse resistance belong to?** The resistivity enters only
once the fields attenuate *inside* the layer, $h \gtrsim \delta_{\text{layer}}$,
which requires

$$f \gtrsim \frac{\rho}{\pi\mu_0 h^{2}} = \frac{100}{\pi(1.2566\times10^{-6})(100^{2})}
= 2533\ \mathrm{Hz}$$

for $\rho = 100\ \Omega\,\mathrm{m}$, $h = 100\ \mathrm{m}$: three orders of
magnitude above the marine CSEM band. The transverse resistance $\rho h$ is the
resistance seen by a current crossing the layer **vertically** — the galvanic
geometry that a controlled source at finite offset exploits — and it is *not* what
a one-dimensional plane-wave sounding measures. That is the honest statement of the
rule: correct for its own geometry, wrong for this one, and the difference is
measurable because a single number ($\rho h$) cannot reproduce curves that differ
by $99\,\%$.

The consequences:

- a one-dimensional sounding constrains the layer's **thickness** well and its
  **resistivity** poorly, so the resistivity–thickness trade-off is real — but it
  runs in the *opposite* direction from the rule of thumb;
- the inversion of a single sounding is still non-unique, and **the honest product
  of a marine CSEM survey is a resistivity image with a stated resolution, not a
  "hydrate thickness"**. Converting resistivity to saturation requires a
  petrophysical relation (Archie-type) with its own parameters, and that conversion
  is a separate inference.

## 6. Assumptions and regime of validity

1. **Quasi-static (diffusive) fields.** Displacement currents are neglected. Valid
   below a few hertz in the ocean; at higher frequencies the physics becomes
   wave-like and a different formulation is needed.
2. **One-dimensional layering, plane-wave incidence.** The demonstration's
   response is a 1-D MT-style impedance, not a full three-dimensional
   dipole-source CSEM response. What it captures faithfully is the **sensitivity to
   the layered resistivity**; what it omits is the source geometry, the
   airwave, and the offset dependence that real acquisition exploits.
3. **Known water resistivity and depth.** The water layer dominates the response
   and must be constrained independently (by a CTD, or by the deep-towed
   receiver's own measurement).
4. **Isotropic resistivity.** Anisotropy in a finely layered sediment is common and
   is degenerate with layering in a 1-D interpretation.
5. **No induced polarisation.** Chargeable sediments have a complex resistivity;
   it is a second-order effect at CSEM frequencies but not zero.
6. **No three-dimensional effects.** A finite body, a rough seafloor or a
   topographic slope all break the 1-D model and can mimic a target or hide one.
7. **A petrophysical relation is needed for the last step.** Resistivity is the
   measurement; saturation is an inference through an empirical relation.

## 7. Worked examples

### Example 1 — the frequency a target needs

A target at $500\ \mathrm{m}$ below the seafloor in a $1\ \Omega\,\mathrm{m}$
sediment. Its effect peaks where the skin depth is a few times the depth;
taking $\delta \approx 2 \times 500 = 1000\ \mathrm{m}$:

$$\delta = 503.3\sqrt{\frac{\rho}{f}} \;\Longrightarrow\;
f = \frac{\rho}{( \delta/503.3)^{2}}
= \frac{1.0}{(1000/503.3)^{2}} = \frac{1.0}{3.948} = 0.253\ \mathrm{Hz}.$$

So a $500\ \mathrm{m}$ target is best seen near $0.25\ \mathrm{Hz}$ — and the water
loss at that frequency ($\delta_{sw} = 503.3\sqrt{0.3/0.253} = 548\ \mathrm{m}$) is
$8.686 \times 1500/548 = 23.8\ \mathrm{dB}$, one way. **Target depth and water depth together choose the
frequency**, and deeper targets need lower frequencies, which the water screens more
gently but which resolve less.

### Example 2 — the maximum detectable depth

If the receiver's dynamic range is $120\ \mathrm{dB}$ and the water column consumes
$2 \times 47.3 = 94.6\ \mathrm{dB}$ at $1\ \mathrm{Hz}$, only $25\ \mathrm{dB}$ is
left for the sub-seafloor. At $0.1\ \mathrm{Hz}$ the water consumes $30\ \mathrm{dB}$
two-way, leaving $90\ \mathrm{dB}$ — enough for several hundred metres of sediment.
**The frequency is set by the water column first and by the target second**, which
is why marine CSEM uses a low-frequency band and long offsets.

### Example 3 — is a $10\ \Omega$ m, $100$ m layer in $1\ \Omega$ m sediment visible?

From Section 5b, a $100\ \mathrm{m}$ layer at the seafloor with $h \ll
\delta_{\text{layer}}$ adds $\mathrm{i}\omega\mu_0 h$ to the host impedance, so at
$0.422\ \mathrm{Hz}$ ($\delta_{\text{host}} = 774.8\ \mathrm{m}$)

$$\rho_a = \omega\mu_0\left(\frac{\delta^{2}}{2} + \delta h + h^{2}\right)
= 1.2915\ \Omega\,\mathrm{m}$$

against $1.000\ \Omega\,\mathrm{m}$ for the bare half-space: **a $+29\,\%$
anomaly**, and it is $+25.9\,\%$ if the layer is $10\ \Omega\,\mathrm{m}$ instead of
$100$ — a $2.5\,\%$ change in the response for a **tenfold** change in resistivity.
So the anomaly says *there is $100\ \mathrm{m}$ of something more resistive than the
host*; it does not measure $10\ \Omega\,\mathrm{m}$.

To measure the resistivity the fields must attenuate inside the layer,
$f \gtrsim \rho/(\pi\mu_0h^{2})$: $253\ \mathrm{Hz}$ for $10\ \Omega\,\mathrm{m}$
and $2533\ \mathrm{Hz}$ for $100\ \Omega\,\mathrm{m}$, both far above the band. **So a
one-dimensional sounding resolves the layer's thickness and not its resistivity**,
and the field method's sensitivity to $\rho h$ comes from the offset-dependent
galvanic geometry that this plane-wave model deliberately omits. That is the
honest calibration of what each measurement can do.

## 8. Python demonstration

`code/marine_csem_em_demo.py` prints everything above with units:

1. the skin-depth table, computed from the closed form and from $1/\mathrm{Re}(k)$;
2. the plane-wave seafloor response, showing the water-column dominance;
3. the sub-seafloor apparent resistivity for the layered model, with phase;
4. the anomaly of three models against frequency (Section 4);
5. the five-model equal-$\rho h$ test and the controlled single-frequency test of
   Section 5b, including the thin-layer prediction against the recursion;
6. verification: the recursion against the closed-form two-layer impedance, and
   against the exact uniform-half-space result (ratio 1 to ten figures), plus a
   unit check on $\delta$.

Run it with

```bash
cd 15-oceanography-marine/02-marine-geophysics-methods/code
/Users/miroslav/Documents/workspace/geophysics/.venv/bin/python marine_csem_em_demo.py
```

Print-only, no network, fixed seed `np.random.default_rng(20261014)`, exit 0, in
under a second.

## 9. Exercises

Full sets with worked solutions are in
[`exercises/07-marine-csem-em-exercises.md`](exercises/07-marine-csem-em-exercises.md)
and
[`exercises/07-marine-csem-em-solutions.md`](exercises/07-marine-csem-em-solutions.md).

- ★ Compute the skin depth in seawater and in $2\ \Omega\,\mathrm{m}$ sediment at
  $0.25\ \mathrm{Hz}$ and at $4\ \mathrm{Hz}$.
- ★★ Compute the one-way and two-way water attenuation through $2000\ \mathrm{m}$ at
  $0.1$ and $1\ \mathrm{Hz}$, and state the frequency a system with $110\ \mathrm{dB}$
  of dynamic range should use.
- ★★ Compute the frequency at which a $300\ \mathrm{m}$ deep target is best seen in
  a $1.5\ \Omega\,\mathrm{m}$ sediment.
- ★★★ Design a CSEM survey for a $200\ \mathrm{m}$ target in $1500\ \mathrm{m}$ of
  water, stating the frequency band, the offset range, the required resistivity
  resolution, and the term in the error budget that binds.

## Mastery checkpoint

Without notes, and showing your arithmetic. Use
$\mu_0 = 4\pi\times10^{-7}\ \mathrm{H\,m^{-1}}$.

> A survey in $2000\ \mathrm{m}$ of seawater ($0.30\ \Omega\,\mathrm{m}$) targets a
> $150\ \mathrm{m}$ thick layer of $80\ \Omega\,\mathrm{m}$ at $400\ \mathrm{m}$ below
> the seafloor, in sediment of $1.2\ \Omega\,\mathrm{m}$.
> **(a)** Compute the skin depth in seawater at $0.1$, $0.5$ and $2\ \mathrm{Hz}$, and
> the one-way water attenuation at each.
> **(b)** Compute the skin depth in the sediment at those frequencies and state which
> frequency is best suited to the target.
> **(c)** State why the plane-wave seafloor response would be water-dominated and
> what geometric change fixes it.
> **(d)** The target's transverse resistance is $\rho h = 80 \times 150 =
> 12\,000\ \Omega\,\mathrm{m^{2}}$. Compute the ratio of the layer's thickness to
> the host's skin depth at the frequency of (b), and state in one sentence what the
> sounding therefore measures.

A worked version of (a)–(d) is in the lesson-07
[solutions](exercises/07-marine-csem-em-solutions.md).

## Common pitfalls

1. **Forgetting $\mu_0$ or the factor of 2 in $\delta$.** The demonstration computes
   $\delta$ twice for exactly this reason.
2. **Treating the water column as transparent.** It is 5.4 skin depths at $1\
   \mathrm{Hz}$ through $1500\ \mathrm{m}$.
3. **Assuming a seafloor MT measurement sees the sediments.** Section 2 shows it
   returns the water's resistivity at every frequency in the band.
4. **Quoting a single frequency.** The response is band-limited, and its *shape* is
   the information.
5. **Applying the transverse-resistance rule where it does not hold.** Section 5
   measures deviations of up to $99\,\%$ for equal $\rho h$, and shows that in the
   thin-layer regime the response measures thickness, not $\rho h$.
6. **Converting resistivity to saturation without stating the petrophysical
   relation.** That conversion is an inference, not a measurement.
7. **Using a 1-D model on a three-dimensional target.** A rough seafloor, a slope
   or a finite body can mimic a target.

## Related modules

- [02 Multibeam Bathymetry and Swath Mapping](02-multibeam-bathymetry.md) —
  the seafloor geometry a CSEM survey is planned against.
- [06 Ocean-Bottom Seismology and OBS Networks](06-obn-ocean-bottom-seismology.md) —
  the seafloor recording practice shared with CSEM receivers.
- [Module 15-04 Seafloor Mapping and Habitat Characterisation](../04-seafloor-mapping-and-habitats/README.md) —
  the gas-hydrate resource question that motivates the method.
- [09-05-03 CSEM in Marine Environments](../../09-electrical-em-methods/05-em-methods-applications/03-csem-marine.md) —
  the source, the acquisition geometry and the processing.
- [02-07-06 EM Fields in Conductors](../../02-physics/07-electromagnetism/06-em-in-conductors.md) —
  the diffusion equation and the skin depth derived there.
- [08-04-01 Electromagnetic Induction in the Earth](../../08-geomagnetism-electromagnetism/04-electromagnetic-induction/01-em-induction-basics.md) —
  the natural-source analogue with the same impedance recursion.

## Self-assessment checklist

- [ ] I can derive and evaluate the skin depth two ways.
- [ ] I can quantify water-column attenuation and choose a frequency band.
- [ ] I can evaluate a layered impedance and verify it on a half-space.
- [ ] I can explain why a plane-wave seafloor measurement is water-dominated.
- [ ] I can compute a sub-seafloor anomaly and identify its band.
- [ ] I can test the transverse-resistance rule and state where it fails.
- [ ] I can say what a CSEM survey does and does not deliver.
