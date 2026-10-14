---
id: 06-09-06
title: "Multiple Attenuation: SRME, Radon and Deconvolution"
level: doctoral
prereqs: ["06-09-02", "06-09-03"]
tags: [seismology, reflection-seismology, multiples, radon, srme, deconvolution]
---

# Multiple Attenuation: SRME, Radon and Deconvolution

## Learning objectives

By the end of this lesson you will be able to:

1. **Classify** multiples (surface-related, interbed) and explain why they are
   coherent and therefore survive stacking.
2. **Describe** three families of attenuation — deconvolution, transform-domain
   separation, and prediction/subtraction (SRME) — and what each assumes.
3. **Derive** the parabolic Radon transform and why an event's moveout curvature
   separates it from another with a different velocity.
4. **Measure** the performance of a Radon mute: primary preservation and multiple
   attenuation, and state the trade the mute makes.
5. **Derive** a predictive-deconvolution filter and measure its effect on a
   periodic multiple.
6. **Choose** an attenuation strategy given the multiple's periodicity and the
   available offsets, and state the residual risk.

## Prerequisites

- [02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](02-processing-flow.md).
- [03 Velocity Analysis and Moveout Interpretation](03-velocity-analysis.md).

## 1. Intuition: multiples are echoes of the surface

A **multiple** is energy that has reflected more than once before being recorded:
a water-bottom bounce, a surface-related reverberation, an interbed reflection
trapped between two strong contrasts. Because the multiple travels a longer path,
it arrives later and — crucially — **with a different moveout** from the primary
it imitates. That moveout difference is the only handle we have on it.

The difficulty is that a multiple is not noise. It is a coherent, often strong
event that stacks just as well as a primary. Since stacking only suppresses what
is *incoherent* between traces, the multiple survives stacking intact (measured
in lesson 02: a 16-fold stack leaves the primary/coherent-event ratio essentially
unchanged, 0.916 against 1.000). Attenuation must exploit a *difference* — in
moveout, in periodicity, or by predicting the multiple from the data themselves.

All numbers are **SYNTHETIC**.

## 2. Precise definitions

### 2.1 Multiple classes

- **Surface-related multiple**: at least one reflection at the free surface
  (source or receiver side). Includes water-bottom multiples in marine data.
- **Interbed multiple**: trapped between two internal contrasts; short-period and
  quasi-periodic.
- **Long-period vs short-period**: the distinction matters because it selects the
  method. Short-period multiples within a wavelet length need deconvolution;
  long-period multiples with distinct moveout need transform separation.

### 2.2 Parabolic Radon transform

With $x$ the offset and $\tau$ the intercept time, the **parabolic Radon
transform** models the data as a superposition of parabolas:

$$d(x,t) = \sum_q m\!\left(q,\;\tau = t - qx^{2}\right),$$

where $q$ is the curvature parameter. Because a hyperbolic event
$t=\sqrt{t_0^{2}+x^{2}/v^{2}}$ is well approximated by a parabola in $x^{2}$ for
moderate offsets, an event's energy concentrates at a $q$ determined by its
velocity and intercept time — approximately $q \approx 1/(2t_0v^{2})$.

### 2.3 Predictive deconvolution

A **prediction filter** $f$ of length $L$ and prediction lag $\Delta$ estimates
$s(n+\Delta)$ from $s(n-L+1)\ldots s(n)$. Subtracting the prediction attenuates
anything that is predictable at lag $\Delta$ — in particular, a multiple that
repeats the primary at a constant lag.

## 3. Derivations

### 3.1 Why moveout separates multiples

An event's curvature in the parabolic parametrisation is, from the expansion of
$t=\sqrt{t_0^{2}+x^{2}/v^{2}}$,

$$t \approx t_0 + \frac{x^{2}}{2t_0v^{2}} \;\Longrightarrow\;
q = \frac{1}{2t_0v^{2}}.$$

A multiple has a **larger** $t_0$ and a **smaller** $v$ than the primary it
imitates (it spends extra time in the slow shallow section), so its $q$ is larger.
The separation in $q$ between primary and multiple is

$$\frac{q_{\text{mult}}}{q_{\text{prim}}}
= \frac{t_0^{\text{prim}}\,v_{\text{prim}}^{2}}
{t_0^{\text{mult}}\,v_{\text{mult}}^{2}}.$$

*Numerical check.* With the demonstration's SYNTHETIC pair — primary at
$t_0=1.00\ \mathrm{s}$, $v=2500\ \mathrm{m\,s^{-1}}$; multiple at
$t_0=1.80\ \mathrm{s}$, $v=1200\ \mathrm{m\,s^{-1}}$ —
$q_{\text{prim}} = 8.0\times10^{-8}$ and
$q_{\text{mult}} = 1.93\times10^{-7}\ \mathrm{s\,m^{-2}}$, a ratio of $2.41$.
The larger the ratio, the cleaner the separation.

### 3.2 Inversion of the Radon transform, and its round-trip check

Writing the transform as a linear operator $\mathbf{A}$ (a sparse matrix of
interpolation weights), the model is recovered by least squares

$$\mathbf{m} = \arg\min_{\mathbf{m}}\left\lVert\mathbf{A}\mathbf{m}-\mathbf{d}
\right\rVert^{2},$$

solved here with LSQR. **The check that matters is the round trip:** apply the
operator to the recovered model and compare with the data. The demonstration
reports a residual of **1.30%** after 400 LSQR iterations on a
$3300\times6820$ operator (data $15$ traces $\times$ $220$ samples; model
$31$ curvatures $\times$ $220$ intercept times). A transform whose round trip
does not reproduce the data is not being inverted correctly, and any mute applied
to it removes the wrong thing.

### 3.3 The mute trade-off, measured

Given a correct inversion, the multiple is attenuated by zeroing the $q$ rows
where its energy lies. The demonstration mutes 4 of 31 curvature rows and
measures:

| quantity | before | after | change |
|---|---|---|---|
| primary amplitude | 0.6464 | 0.5505 | 85.2% preserved |
| multiple amplitude | 0.5214 | 0.4402 | 84.4% remaining |
| primary/multiple ratio | 1.240 | 1.251 | $+0.9\%$ |

**This is a poor result, and it is reported as such.** The mute removed $15.6\%$
of the multiple but cost $14.8\%$ of the primary, and the ratio barely improved.
The reason is physical and instructive: the LSQR model is *smeared across
curvature* because the operator is underdetermined, so a curvature mute cuts
signal and noise together. Separation improves with a larger curvature
difference (a larger $q_{\text{mult}}/q_{\text{prim}}$), a longer offset range,
and a better-conditioned inversion (sparsity-promoting or high-resolution Radon).
**A method is not endorsed by being named in a textbook; it is judged by the
measured numbers, and these numbers say the mute is insufficient here.**

### 3.4 Predictive deconvolution for periodic multiples

For a short-period multiple the lag is constant, so a prediction filter can
estimate it. The least-squares problem is

$$\mathbf{f} = \arg\min_{\mathbf{f}}\sum_n
\left(s(n+\Delta) - \mathbf{f}^{\!\top}\mathbf{s}(n)\right)^{2},
\qquad \mathbf{s}(n) = \left[s(n-L+1),\dots,s(n)\right]^{\!\top},$$

with the normal equations
$\left(\mathbf{X}^{\!\top}\mathbf{X}\right)\mathbf{f}
= \mathbf{X}^{\!\top}\mathbf{y}$ and a small white-noise stabilisation added to
the diagonal. Subtracting $\mathbf{f}^{\!\top}\mathbf{s}(n)$ at lag $\Delta$
removes the predictable part.

*Numerical check.* A single trace with a primary at $t_0=1.00\ \mathrm{s}$ and a
multiple at lag $44$ samples ($0.704\ \mathrm{s}$), amplitudes 1.0 and 0.8,
filter length 12:

| quantity | before | after |
|---|---|---|
| multiple amplitude | 0.8000 | 0.3220 ($-60\%$) |
| primary amplitude | 1.0000 | 1.0000 |

The multiple is reduced by 60% with the primary untouched — a much better
outcome than the Radon mute, because the multiple here is *exactly* periodic and
the primary is a single isolated event. The method's weakness is that it also
shortens the wavelet (the filter is not a pure multiple predictor), so its two
effects must be disentangled by an independent criterion.

### 3.5 SRME: predict the multiple from the data

**Surface-related multiple elimination (SRME)** makes the strongest possible use
of the data: it predicts surface-related multiples by *convolving the data with
itself*. The idea is that a multiple is a primary that has been reflected at the
surface and then travelled the same path as another primary. In its simplest
one-dimensional form, if $d$ is the data and $m$ the unknown multiple,
$m = d * d \cdot (\text{surface reflectivity})$, and the attenuation step
subtracts an adaptively scaled version of the prediction:

$$d_{\text{out}} = d - a\,(d * d).$$

SRME requires the data to be densely sampled at the surface (ideally
source–receiver coverage with no gaps) and it needs an adaptive subtraction
because the predicted multiples are never amplitude- or phase-perfect. The
powerful part is that it needs **no velocity model** and **no subsurface
information**; the limitation is the data density and the accuracy of the
subtraction. It is the standard first-pass method for surface-related multiples
in modern marine processing.

### 3.6 Residual multiples and the QC metrics that matter

Attenuation never removes a multiple completely. What remains — the **residual**
— must be quantified, because a residual that is coherent and strong will migrate
to a spurious position (lesson 04) and bias amplitudes (lesson 05). Three metrics
summarise a multiple-attenuation step:

1. **Multiple attenuation** at a known multiple time, i.e. the amplitude ratio
   before/after on the *multiple*, measured in a window where no primary
   interferes.
2. **Primary preservation** at known primary times, measured on the same data —
   the number that is most often omitted and most often damaging.
3. **Residual moveout energy**, i.e. the energy remaining in the multiple's
   curvature range in a transform panel, which distinguishes "not removed" from
   "moved".

For the demonstration's Radon mute, the three numbers are 15.6% attenuation,
85.2% primary preservation, and a $+0.9\%$ ratio change — clearly insufficient.
For the predictive deconvolution, 60% attenuation and 100% primary preservation —
much better, but only because the synthetic multiple was exactly periodic.

*Worked comparison.* Suppose a processing sequence attenuates a multiple by 90%
and preserves 95% of the primary. The residual multiple is 10% of its original
amplitude; if the original multiple was twice the primary, the residual is 0.2 of
the primary — still large. **Attenuation percentages must be translated back into
residual amplitudes before they mean anything.** This is why a "90% attenuation"
headline can coexist with a visibly contaminated section.

### 3.7 Cascades and the risk of over-processing

Modern practice applies several methods in sequence because no single method
covers all multiple types:

1. **SRME** for surface-related multiples (needs dense data, no velocity model);
2. **Radon or f–k** for residual long-period, moveout-separated energy;
3. **Predictive deconvolution** for short-period, periodic reverberations.

Each stage consumes amplitudes and each can remove primaries that resemble
multiples. The cumulative primary loss is the product of the stages' losses
(0.95³ ≈ 0.86 for three stages each costing 5%), so a cascade that looks
acceptable stage by stage can destroy 14% of the primary amplitude in total. The
end-to-end primary-preservation number, not the per-stage numbers, is what the
interpreter needs, and it must be measured at the interpretation targets, not on
average over the section.

## 4. Physical interpretation

- **Multiples are coherent**, so the random-noise argument does not apply; only a
  *difference* from the primary can be exploited.
- **The three method families exploit three different differences**:
  periodicity (deconvolution), moveout (Radon/f–k), and causality/path structure
  (SRME).
- **Every method leaves residuals and damages primaries.** The honest reporting
  of a multiple-attenuation step includes both the attenuation achieved and the
  primary loss, as in the tables above.
- **Modern practice uses a cascade**: SRME for surface-related multiples, then a
  Radon or f–k pass for residual long-period energy, then deconvolution for
  short-period reverberations.

## 5. Assumptions

1. **A moveout difference exists** for transform-domain separation. Multiples
   that share the primary's moveout (rare but possible) cannot be separated this
   way.
2. **Sufficient offset range** for the curvature difference to be resolved, which
   is the same aperture requirement as velocity analysis.
3. **A correct, well-conditioned Radon inversion.** As Section 3.3 shows, a
   smeared model makes the mute a blunt instrument.
4. **Periodicity** for predictive deconvolution: a constant lag and a stable
   wavelet. Non-periodic multiples defeat it.
5. **Data density and an accurate adaptive subtraction** for SRME.
6. **Anelastic attenuation of multiples is negligible** relative to primaries in
   the window of interest; otherwise the multiple is not a simple copy.

## 6. Units and dimensional analysis

| Quantity | Unit | Check |
|---|---|---|
| $t$, $\tau$, $\Delta$ | s | |
| $x$ | m | |
| $q$ | $\mathrm{s\,m^{-2}}$ | $qx^{2}$ is s ✔ |
| $v$ | $\mathrm{m\,s^{-1}}$ | |
| $d$, $m$ | amplitude | |
| filter $f$ | dimensionless | predicts an amplitude |

## 7. Worked examples

### Example 1 — curvature of a water-bottom multiple

Water depth $h_w = 300\ \mathrm{m}$, water speed $v_w = 1500\
\mathrm{m\,s^{-1}}$. A primary from a shallow reflector at $t_0 = 0.400\
\mathrm{s}$ and the first water-bottom multiple at $t_0 = 1.20\ \mathrm{s}$ (three
water legs instead of one). Using $q = 1/(2t_0v^{2})$ with $v = 1500\
\mathrm{m\,s^{-1}}$ for both (the ray travels in water in each case):

$$q_{\text{prim}} = \frac{1}{2(0.400)(1500^{2})} = 5.56\times10^{-7}
\ \mathrm{s\,m^{-2}},$$
$$q_{\text{mult}} = \frac{1}{2(1.20)(1500^{2})} = 1.85\times10^{-7}
\ \mathrm{s\,m^{-2}}.$$

Here the multiple has the *smaller* curvature, because its larger $t_0$ dominates
in $q = 1/(2t_0v^{2})$. The ratio and its sign depend on the specific geometry,
which is why the first step of any design is to compute the two $q$ values from
the velocity model rather than to assume "multiples are more curved". When a
multiple and a primary have nearly equal $q$, the transform cannot separate them
at all and another method is required.

### Example 2 — how large an aperture do you need?

To separate two events at $q_1$ and $q_2$, the moveout difference across the
cable must exceed roughly one wavelet half-period:
$(q_2-q_1)x_{\max}^{2} \gtrsim 1/(2f_0)$. With
$q_2-q_1 = 1.13\times10^{-7}\ \mathrm{s\,m^{-2}}$, $f_0 = 25\ \mathrm{Hz}$, this
gives $x_{\max}\gtrsim\sqrt{1/(2\times25\times1.13\times10^{-7})}
= \sqrt{1.77\times10^{5}} = 421\ \mathrm{m}$ — easily satisfied. For closely
spaced curvatures or low frequencies the required aperture can exceed any real
cable, and that is when the method is impossible rather than merely difficult.

### Example 3 — the cost of a bad mute

Suppose a mute removes 20% of the primary amplitude at a target horizon. If the
target reflection is used for AVO (lesson 05), a 20% amplitude bias is far larger
than any fluid effect, and the AVO analysis is invalid. **This is why
multiple-attenuation quality is an AVO prerequisite**, and why the primary-loss
number must be reported.

### Example 4 — translating attenuation into residual amplitude

Suppose a multiple is originally twice the primary amplitude, and a cascade
attenuates it by 92% while preserving 94% of the primary. The residual multiple
is $2\times0.08 = 0.16$ of the *original* primary, and the primary is now $0.94$
of its original, so the residual multiple is $0.16/0.94 = 0.17$ of the *current*
primary. A 17% coherent contaminant will bias an AVO gradient estimate far more
than the fluid effect being sought. The headline "92% attenuation" is accurate
and, on its own, misleading. **Convert every attenuation figure to a residual
amplitude relative to the primary at the target, and compare that with the effect
you intend to measure.**

## 8. Python demonstration

`code/multiple_elimination_demo.py`:

1. builds a 15-trace CMP gather with a primary ($t_0=1.0\ \mathrm{s}$,
   $v=2500\ \mathrm{m\,s^{-1}}$) and a multiple ($t_0=1.8\ \mathrm{s}$,
   $v=1200\ \mathrm{m\,s^{-1}}$);
2. builds the parabolic Radon operator as a dense matrix (3300×6820, 180 MB) and
   inverts with LSQR, reporting a **1.30%** round-trip residual;
3. computes the curvature ratio (2.41) and mutes 4 of 31 curvature rows,
   reporting 85.2% primary preservation and 84.4% multiple retention — an
   honestly poor separation;
4. derives and applies a 12-sample predictive-deconvolution filter at a 44-sample
   lag, reducing the multiple from 0.8000 to 0.3220 with the primary unchanged.

No real data are used and no network access is required.

## 9. Exercises

Full sets are in
[`exercises/06-multiple-elimination-exercises.md`](./exercises/06-multiple-elimination-exercises.md)
and
[`exercises/06-multiple-elimination-solutions.md`](./exercises/06-multiple-elimination-solutions.md).

- **★** Compute $q$ for a primary at $t_0=1.2\ \mathrm{s}$,
  $v=2400\ \mathrm{m\,s^{-1}}$ and a multiple at $t_0=2.0\ \mathrm{s}$,
  $v=1500\ \mathrm{m\,s^{-1}}$.
- **★★** Derive the parabolic approximation to the hyperbolic moveout and state
  the neglected term.
- **★★** Explain why the Radon mute preserves only 85% of the primary in the
  demonstration, and propose a change that would improve it.
- **★★★** Design a three-stage attenuation sequence for a marine data set with
  strong water-bottom multiples and justify the order and the QC metrics.

## 10. Common mistakes

1. **Assuming stacking will remove multiples.** It will not (lesson 02).
2. **Applying a Radon mute without checking the round trip.** If the transform
   is not inverted correctly, the mute removes the wrong energy.
3. **Ignoring the primary loss.** A mute that removes a multiple and 20% of the
   primary is worse than useless for amplitude work.
4. **Using predictive deconvolution with the wrong lag.** The lag must match the
   multiple's periodicity; a mis-set lag removes the primary instead.
5. **Using SRME with sparse data.** The self-convolution prediction assumes
   dense surface coverage.

## 11. Real-world applications

- **Marine exploration.** Water-bottom multiples are the dominant coherent noise;
  SRME plus Radon is the standard cascade.
- **Land data.** Short-period interbed multiples dominate, and predictive
  deconvolution is the workhorse.
- **4-D seismic.** Residual multiples that change between surveys can masquerade
  as production signal; attenuation must be *consistent* between surveys.
- **Quantitative interpretation.** As Example 3 shows, multiple contamination
  invalidates AVO and inversion, so attenuation quality is a prerequisite for
  quantitative work.

## 12. Further reading

- **Yilmaz, Ö. (2001). *Seismic Data Analysis*. Society of Exploration
  Geophysicists.** Level: intermediate to advanced. Radon transforms and
  predictive deconvolution in practice.
- **Verschuur, D. J., Berkhout, A. J., & Wapenaar, C. P. A. (1992). Adaptive
  surface-related multiple elimination. *Geophysics*, 57(9), 1166–1177.**
  Level: research. The SRME method.
- **Sacchi, M. D., & Ulrych, T. J. (1995). High-resolution velocity gathers and
  offset space reconstruction. *Geophysics*, 60(4), 1169–1177.** Level:
  research. Better-conditioned Radon inversion.
- **ObsPy documentation.** <https://docs.obspy.org> — Level: reference.

> Bibliographic details are given so you can locate the works; this repository
> does not host or reproduce copyrighted text.

## 13. Related lessons

- [02 Reflection Processing Flow: Deconvolution, NMO, Stack, Migration](02-processing-flow.md) —
  where the multiple survives stacking.
- [03 Velocity Analysis and Moveout Interpretation](03-velocity-analysis.md) —
  the curvature/velocity relation used by the Radon transform.
- [04 Migration and Imaging](04-migration-imaging.md) — why multiples must be
  removed before imaging.
- [05 AVO/AVA Analysis and Its Assumptions](05-amplitude-vs-offset.md) — the
  analysis that multiple contamination invalidates.

## 14. Self-assessment checklist

- [ ] I can classify a multiple and name the method it needs.
- [ ] I can derive the curvature $q=1/(2t_0v^{2})$ and compute a separation ratio.
- [ ] I can check a Radon inversion with a round trip.
- [ ] I can measure and report the mute's primary loss.
- [ ] I can derive and apply a predictive-deconvolution filter.
- [ ] I can explain SRME's requirement and its lack of a velocity-model need.
